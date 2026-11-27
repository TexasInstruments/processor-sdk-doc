.. include:: <isonum.txt>

.. _edgeai_compile_evaluate:

##########################
Model Compile and Evaluate
##########################

The :ref:`EdgeAI Model Zoo <edgeai_model_zoo>` runs *pre-compiled* artifacts
on the |__PART_FAMILY_NAME__| target. This section covers the **x86 host
workflow** that produces those artifacts: how to compile an audio model for
the C7\ |trade| NPU, run host-emulation inference, and measure accuracy against a
data set - using **edgeai-tidlrunner**. Everything runs on an Ubuntu x86 PC,
except the optional `Run inference on the EVM`_ step.

This is the workflow for *any* audio model, not just the reference models. The
reference models below are worked examples. To bring your own model you
point the same ``tidlrunner-cli`` at your ONNX graph and a per-model YAML config,
using a reference config as a starting template. TIDL determines which operators
it accelerates; TVM generates C7x DSP code for the rest - see the `Supported
Operators
<https://software-dl.ti.com/codegen/docs/tvm/tvm_tidl_users_guide/supported-operators.html>`__
chapter of the TI TVM User's Guide for the authoritative list.

*****************
edgeai-tidlrunner
*****************

edgeai-tidlrunner is a bring-your-own-model (BYOM) command-line wrapper over the
`TI TVM + TIDL <https://software-dl.ti.com/codegen/docs/tvm/tvm_tidl_users_guide/index.html>`__
compilation stack. A single YAML config per model drives every stage, and one
CLI - ``tidlrunner-cli`` - exposes the stages this section uses:

.. list-table::
   :header-rows: 1
   :widths: 18 82

   * - Command
     - What it does
   * - ``compile``
     - Imports the ONNX graph, quantizes and partitions it, and writes the
       deployable TIDL/TVM-RT artifacts.
   * - ``infer``
     - Runs the compiled model on the x86 host (PC emulation), or on the AM62D
       evaluation module (EVM) itself, to check output correctness before deploying to the target.
   * - ``evaluate``
     - Runs the compiled model over a data set and reports accuracy or
       speech-enhancement metrics.
   * - ``inspect``
     - One-shot compile + inference + reference comparison that emits an
       interactive HTML analysis report (see :ref:`Model Inspector <edgeai_model_inspector>`).

All commands are run from the repository root (``edgeai-tidlrunner/``) and take
``--config_path <cfg>`` pointing at the per-model YAML. The same config file is
reused across ``compile``, ``infer``, and ``evaluate``.

.. note::

   ``compile``, ``infer`` and ``evaluate`` also write or refresh the Model
   Inspector report (:file:`work_dirs/.../inspect/modelinspector.html`) at the end
   of the run. Running ``infer`` on the EVM with ``--debug_level 2`` adds
   measured per-layer cycle counts to the report.
   See :ref:`Model Inspector <edgeai_model_inspector>` for details.

.. _edgeai-am62d-setup:

*****
Setup
*****

Model compilation runs on an x86 PC (Ubuntu Linux recommended). The AM62D audio
flow is self-contained: a single setup script installs the whole TVM toolchain
into a dedicated Python 3.10 environment. The TIDL tools target Python 3.10.
These steps assume `pyenv <https://github.com/pyenv/pyenv>`__.

The flow uses these toolchain versions:

.. list-table::
   :header-rows: 1
   :widths: 24 30 46

   * - Component
     - Version
     - Location
   * - TVM wheel (x86, cp310)
     - ``ti_tvm_am62x-3.0.0``
     - ``tidlrunner-am62d`` Python environment
   * - TIDL tools (x86)
     - Bundled in the TVM wheel, CPU and GPU builds
     - ``<tvm-package-dir>/3rdparty/x86_tidl_tools/AM62D/{cpu,gpu}``
   * - C7000 CGT
     - ``6.2.1.LTS``
     - ``tools/tidl_tools_package/bin/ti-cgt-c7000_6.2.1.LTS``
   * - ARM GCC
     - ``15.2.rel1``
     - ``tools/tidl_tools_package/bin/arm-gnu-toolchain-15.2.rel1-x86_64-aarch64-none-linux-gnu``

#. **Clone the repository** (https://github.com/TexasInstruments/edgeai-tidlrunner):

   .. code-block:: console

      $ git clone https://github.com/TexasInstruments/edgeai-tidlrunner.git
      $ cd edgeai-tidlrunner

#. **Create and activate a dedicated Python 3.10 environment.** The AM62D flow
   uses a TI TVM wheel; keep it in its own venv (``tidlrunner-am62d``)
   so it never clobbers a standard ``tidlrunner`` setup:

   .. code-block:: console

      $ pyenv install 3.10
      $ pyenv virtualenv 3.10 tidlrunner-am62d
      $ pyenv activate tidlrunner-am62d

#. **Run the AM62D setup script.** With the venv active, one script installs
   everything this flow needs:

   .. code-block:: console

      $ ./devices/setup_am62d.sh

   It downloads the ARM GCC 15.2 and C7000 CGT 6.2.1 LTS cross-toolchains into
   :file:`tools/tidl_tools_package/bin/` (skipped if already present), installs the
   x86 TI TVM wheel - which bundles the AM62D x86 TIDL tools *inside*
   the package - and installs ``tidlrunner[pc,audio]``, ``tools``, ``onnxruntime``,
   and ``tidl_onnx_model_optimizer``. The ``[audio]`` extra pulls in the audio
   packages (``librosa``, ``soundfile``, ``scipy``, ``pesq``, ``pystoi``,
   ``scikit-learn``). No separate ``pip install`` is needed.

#. **Source the env script once per shell.** TVM ``dlopen``\ s the TIDL runtime
   (:file:`libvx_tidl_rt.so`) before Python's own import runs, so the tool paths must be
   live in the shell *before* ``tidlrunner-cli`` starts. Source (do **not** execute)
   :file:`devices/am62d_env.sh` once; every ``tidlrunner-cli`` command run afterward in
   that shell picks the vars up:

   .. code-block:: console

      $ source devices/am62d_env.sh

   It exports:

   .. list-table::
      :header-rows: 1
      :widths: 26 74

      * - Variable
        - Value
      * - ``TIDL_TOOLS_PATH``
        - :file:`<tvm-package-dir>/3rdparty/x86_tidl_tools/AM62D/cpu` (or
          :file:`.../gpu`, see `GPU TIDL tools`_), resolved from the active
          venv's installed ``tvm``
      * - ``LD_LIBRARY_PATH``
        - prepends ``TIDL_TOOLS_PATH`` so :file:`libvx_tidl_rt.so` resolves
      * - ``ARM64_GCC_PATH``
        - the aarch64 GNU toolchain installed by :file:`setup_am62d.sh` under
          :file:`tools/tidl_tools_package/bin/` (override by exporting before sourcing)
      * - ``CGT7X_ROOT``
        - the C7000 code-generation tools installed by :file:`setup_am62d.sh` under
          :file:`tools/tidl_tools_package/bin/` (override by exporting before sourcing)
      * - ``SOC``
        - ``am62d``

GPU TIDL tools
==============

The TVM wheel bundles two builds of the x86 TIDL tools: ``cpu`` (default) and
``gpu`` (CUDA). The GPU build speeds up calibration during ``compile`` and
host-emulation ``infer``. Select it when sourcing the env script:

.. code-block:: console

   $ AM62D_TIDL_TOOLS=gpu source devices/am62d_env.sh

- The GPU build needs an NVIDIA GPU and driver (:file:`libcuda.so.1`). The CUDA
  runtime is linked statically, so no CUDA toolkit install is required.
  :file:`am62d_env.sh` prints a warning if the driver is missing.
- ``TIDL_TOOLS_PATH`` and ``LD_LIBRARY_PATH`` both point at the selected build.
  Compile and infer with the same build. To switch builds, open a new shell:
  re-sourcing prepends the new path but leaves the old one in
  ``LD_LIBRARY_PATH``.
- The EVM artifacts are produced either way; the choice only affects the x86
  host side.

Data Sets
=========

Accuracy evaluation needs the reference data sets. Compilation alone can run on
random data (for latency-only measurement), but ``evaluate`` requires the real
sets. Download them from the repository root:

.. code-block:: console

   $ # UrbanSound8K (~5.6 GB) - sound classification (VGGish11, YAMNet)
   $ bash examples/audio/scripts/download_urbansound8k.sh

   $ # VoiceBank-DEMAND-16k (~2 GB) - speech enhancement (GCRN-mod, GTCRN)
   $ python3 examples/audio/scripts/download_voicebank_demand.py

They land under :file:`data/datasets/UrbanSound8K/` and
:file:`data/datasets/VoiceBank-DEMAND-16k/` - the paths the model configs expect.
The classification configs use UrbanSound8K **fold 10** (837 samples) as the
test set; the speech-enhancement configs use the VoiceBank-DEMAND-16k **test** set
(824 files).

The reference ONNX models auto-download at compile time via :file:`.link` files, so
fetching them ahead of time is **optional**. To pre-download all reference ONNX models:

.. code-block:: console

   $ bash examples/audio/scripts/download_audio_models.sh

********************
Compile and evaluate
********************

Each model has one config that drives all stages. All of them run under the
``tidlrunner-am62d`` environment with :file:`devices/am62d_env.sh` already sourced
(see `Setup`_). The models below compile to the C7\ |trade| NPU through the TVM
runtime (``session_name: tvmrt``). The AM62D config paths are:

.. list-table::
   :header-rows: 1
   :widths: 12 10 12 18 54

   * - Model
     - Model ID
     - Runtime
     - Tensor Bits
     - Config path (relative to ``edgeai-tidlrunner/``)
   * - VGGish11
     - ``ac-0101``
     - TVM-RT
     - 8
     - :file:`data/configs/samples/models/audio/audio_classification/urbansound8k/vggish11_config.yaml`
   * - YAMNet
     - ``ac-0201``
     - TVM-RT
     - 8
     - :file:`data/configs/samples/models/audio/audio_classification/urbansound8k/yamnet_config.yaml`
   * - GCRN-mod-g16
     - ``ase-0212``
     - TVM-RT
     - 16 (Enc/Dec), FP32 (LSTM)
     - :file:`data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_mod_g16_fixed_4sec_config.yaml`
   * - GCRN-mod-g8
     - ``ase-0213``
     - TVM-RT
     - 16 (Enc/Dec, LSTM)
     - :file:`data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_mod_g8_fixed_4sec_config.yaml`

VGGish11 (TVM-RT, 8-bit)
========================

Runs on the C7\ |trade| NPU (``tidl_offload: true``):

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/audio_classification/urbansound8k/vggish11_config.yaml
   $ tidlrunner-cli compile  --config_path $CFG --target_device AM62D
   $ tidlrunner-cli infer    --config_path $CFG --target_device AM62D
   $ tidlrunner-cli evaluate --config_path $CFG --target_device AM62D

``evaluate`` reports top-1 / top-5 / macro-F1 over UrbanSound8K fold 10.

A successful ``compile`` leaves two deployable libraries in the model's
:file:`artifacts/` folder: :file:`deploy_lib.so.pc` (x86 host emulation) and
:file:`deploy_lib.so.evm` (AArch64, for the target). It also writes
:file:`model_info.json` with the per-layer offload decisions.
:file:`artifacts/tempDir/relay_graph.partitioned.txt` shows the split: functions
named ``@tvmgen_default_tidl_main_*`` are TIDL subgraphs, and operators left in
``@main`` fall back to C7\ |trade| code generation.

YAMNet (TVM-RT, 8-bit)
======================

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/audio_classification/urbansound8k/yamnet_config.yaml
   $ tidlrunner-cli compile  --config_path $CFG --target_device AM62D
   $ tidlrunner-cli infer    --config_path $CFG --target_device AM62D
   $ tidlrunner-cli evaluate --config_path $CFG --target_device AM62D

GCRN-mod (TVM-RT)
=================

GCRN-mod is a GCRN variant modified by TI for TIDL: the encoder and decoder
layers are rewritten so that TIDL supports them, while the grouped LSTM of the
original GCRN is kept. Both variants compile into a single TIDL subgraph on the
C7\ |trade| NPU (``tidl_offload: true``, fixed 4-second input), with the encoder
and decoder layers quantized to 16 bits. They differ in the number of LSTM
groups:

- **GCRN-mod-g16** (``ase-0212``) splits the LSTM into 16 groups, each with
  input size 64 and hidden size 64. The LSTM layers run in FP32. This is the
  reference model of the EdgeAI Model Zoo.
- **GCRN-mod-g8** (``ase-0213``) splits the LSTM into 8 groups, each with input
  size 128 and hidden size 128. The LSTM layers are quantized to 16 bits, and
  the model runs faster than GCRN-mod-g16 (see `Performance benchmark`_).

The LSTM precision follows from a TIDL rule: an LSTM layer runs in fixed point
only when both its hidden size and its input size are greater than 64.
Otherwise TIDL keeps the layer in FP32, whatever ``tensor_bits`` the config
sets. Fewer groups make each LSTM wider, so GCRN-mod-g8 meets the rule and
GCRN-mod-g16 does not.

The example below uses GCRN-mod-g8. Its ``compile`` takes much longer than the
classifiers because 16-bit calibration dominates (see ``advanced_options:calibration_frames`` and
``advanced_options:calibration_iterations`` in the config); the
`GPU TIDL tools`_ shorten it:

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_mod_g8_fixed_4sec_config.yaml
   $ tidlrunner-cli compile  --config_path $CFG --target_device AM62D
   $ tidlrunner-cli infer    --config_path $CFG --target_device AM62D
   $ tidlrunner-cli evaluate --config_path $CFG --target_device AM62D

``evaluate`` reports PESQ / STOI / SI-SDR over the VoiceBank-DEMAND-16k test set.

To listen to the result, add ``--save_output True``. The enhanced audio is
written as :file:`.wav` files, named after the input files, to
:file:`<run_dir>/outputs/` (the first 10 files by default; change the count with
``--save_output_frames``). The config ships with ``postprocess.save_output: false``.

The same commands work for GCRN-mod-g16: set ``CFG`` to
:file:`data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_mod_g16_fixed_4sec_config.yaml`.

************************
Run inference on the EVM
************************

``infer`` can also run the compiled model on the |__PART_FAMILY_NAME__| EVM to check
output on the real hardware. The steps below assume the repository is
available on the EVM at :file:`/opt/edgeai-tidlrunner` (for example NFS-mapped
from the host), so the compiled :file:`artifacts/` (with
:file:`deploy_lib.so.evm`) are already in place.

#. **Set up the EVM environment once.** On the EVM, run:

   .. code-block:: console

      $ cd /opt/edgeai-tidlrunner
      $ ./devices/setup_runner_evm_am62d.sh

   The script creates a Python virtual environment at
   :file:`~/venv/tidlrunner` with ``--system-site-packages``, so it reuses the
   ``numpy``, ``tvm`` and TIDL runtime stack already in the SDK image. It then
   installs ``tidlrunner`` without dependencies, plus the short list of packages
   in :file:`devices/requirements_evm_am62d.txt`. Inference uses the SDK image's
   TVM runtime and C7\ |trade| firmware as shipped; no TVM wheel or firmware
   update is needed on the EVM.

#. **Activate the environment in every new shell, then run inference.** The
   setup script activates the environment only inside its own process, so
   activate it in each new SSH login or terminal; otherwise
   ``tidlrunner-cli`` is not found:

   .. code-block:: console

      $ source ~/venv/tidlrunner/bin/activate
      $ cd /opt/edgeai-tidlrunner
      $ CFG=data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_mod_g8_fixed_4sec_config.yaml
      $ tidlrunner-cli infer --config_path $CFG --target_device AM62D --num_frames 3

   :file:`devices/am62d_env.sh` is only for the x86 host and is not needed on
   the EVM.

.. _edgeai_performance:

*********************
Performance benchmark
*********************

:file:`devices/run_audio_latency_am62d_evm.sh` measures the inference latency of
the audio models on the EVM. It runs ``tidlrunner-cli infer`` for each model
and collects the results into one summary table. The models must already be
compiled on the x86 host, so that their artifacts are in
:file:`work_dirs/compile/AM62D/`.

On the EVM, set up the environment as described in `Run inference on the EVM`_,
then run:

.. code-block:: console

   $ source ~/venv/tidlrunner/bin/activate
   $ cd /opt/edgeai-tidlrunner
   $ ./devices/run_audio_latency_am62d_evm.sh

Without arguments the script benchmarks VGGish11, YAMNet, GTCRN, GCRN-mod-g16
and GCRN-mod-g8. To benchmark only some models, pass their config files:

.. code-block:: console

   $ ./devices/run_audio_latency_am62d_evm.sh \
       data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_mod_g8_fixed_4sec_config.yaml

Each model runs over 10 frames by default; set ``NUM_FRAMES`` to change the
count. GTCRN takes variable-length input, so the script fixes its clip length
to 4 seconds (``GTCRN_BENCH_SECONDS``). The script writes a log per model and
:file:`summary.md` to :file:`work_dirs/benchmark_reports/<timestamp>/`.

The table below shows the results measured on the AM62D EVM with Processor SDK
12.2:

.. list-table::
   :header-rows: 1
   :widths: 22 14 14 16 16 18

   * - Model
     - Precision
     - Audio per call (s)
     - Wall-clock (ms)
     - C7\ |trade| NPU (ms)
     - RTF
   * - VGGish11
     - 8-bit
     - 4.00
     - 11.270
     - 8.184
     - 0.0028
   * - YAMNet
     - 8-bit
     - 0.96
     - 6.098
     - 3.362
     - 0.0064
   * - GTCRN
     - FP32 (Arm)
     - 4.00
     - 358.805
     - N/A
     - 0.0897
   * - GCRN-mod-g16
     - 16-bit, FP32 LSTM
     - 4.00
     - 2255.496
     - 2249.852
     - 0.5639
   * - GCRN-mod-g8
     - 16-bit
     - 4.00
     - 1957.377
     - 1951.783
     - 0.4893

- **Audio per call**: seconds of audio processed by one inference call.
- **Wall-clock**: time of one inference call as seen from Python, averaged over
  the frames. It includes the Arm-side overhead (RPMsg, data copies, Python).
  For GTCRN, which runs only on the Arm cores, this is the full processing time.
- **C7**\ |trade| **NPU**: time spent running the model on the C7\ |trade| NPU,
  measured on the device and averaged over the frames. It excludes the Arm-side
  overhead. GTCRN does not use the C7\ |trade| NPU, so it has no value.
- **RTF**: real-time factor, the wall-clock time divided by the audio duration
  of one call. A value below 1 means the model runs faster than real time.

The latency covers the model call only; pre-processing (STFT, log-mel) and
post-processing (iSTFT) are not included. Results vary with system conditions.

**********
Next steps
**********

To see how a compiled model behaves, read :ref:`Model Inspector
<edgeai_model_inspector>`. The report shows what runs on the C7\ |trade| Neural
Processing Unit (NPU) and what falls back to the Arm core. It also shows how much
accuracy quantization costs, and where the time and memory go.

The page explains the interactive HTML report that ``compile``, ``infer`` and
``evaluate`` generate. It also explains how to produce the full analysis with
``tidlrunner-cli inspect``.
