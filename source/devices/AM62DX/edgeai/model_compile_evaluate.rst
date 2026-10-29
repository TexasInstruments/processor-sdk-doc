.. include:: <isonum.txt>

.. _edgeai_compile_evaluate:

##########################
Model Compile and Evaluate
##########################

The :ref:`EdgeAI Model Zoo <edgeai_model_zoo>` runs *pre-compiled* artifacts
on the |__PART_FAMILY_NAME__| target. This section covers the **x86 host
workflow** that produces those artifacts: how to compile an audio model for
the C7\ |trade| NPU, run host-emulation inference, and measure accuracy against a
data set - using **edgeai-tidlrunner**. It runs entirely on an Ubuntu x86 PC;
nothing here touches the target.

This is the workflow for *any* audio model, not just the reference models. The
four reference models below are worked examples. To bring your own model you
point the same ``tidlrunner-cli`` at your ONNX graph and a per-model YAML config,
using a reference config as a starting template. Which operators offload to the
C7\ |trade| NPU (versus fall back to the Arm core) is determined by TIDL - see
`edgeai-tidl-tools <https://github.com/TexasInstruments/edgeai-tidl-tools>`__ for
the authoritative list of supported operators.

*****************
edgeai-tidlrunner
*****************

edgeai-tidlrunner is a bring-your-own-model (BYOM) command-line wrapper over the
core `edgeai-tidl-tools <https://github.com/TexasInstruments/edgeai-tidl-tools>`__
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
     - Runs the compiled model on the x86 host (PC emulation) to check output
       correctness before deploying to the target.
   * - ``evaluate``
     - Runs the compiled model over a data set and reports accuracy or
       speech-enhancement metrics.
   * - ``inspect``
     - One-shot compile + inference + reference comparison that emits an
       interactive HTML analysis report (see :ref:`Model Inspect <edgeai_model_inspect>`).

All commands are run from the repository root (``edgeai-tidlrunner/``) and take
``--config_path <cfg>`` pointing at the per-model YAML. The same config file is
reused across ``compile``, ``infer``, and ``evaluate``.

.. _edgeai-am62d-setup:

*****
Setup
*****

Model compilation runs on an x86 PC (Ubuntu Linux recommended). The AM62D audio
flow is self-contained: a single setup script installs the whole TVM toolchain
into a dedicated Python 3.10 environment. The TIDL tools target Python 3.10.
These steps assume `pyenv <https://github.com/pyenv/pyenv>`__.

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

   It downloads the ARM GCC 15.2 and C7000 CGT 5.0.0 LTS cross-toolchains into
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
        - :file:`<tvm-package-dir>/3rdparty/x86_tidl_tools/AM62D` (resolved from the
          active venv's installed ``tvm``)
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

Data Sets
=========

Accuracy evaluation needs the reference data sets. Compilation alone can run on
random data (for latency-only measurement), but ``evaluate`` requires the real
sets. Download them from the repository root:

.. code-block:: console

   $ # UrbanSound8K (~5.6 GB) - sound classification (VGGish11, YAMNet)
   $ bash examples/audio/scripts/download_urbansound8k.sh

   $ # VoiceBank-DEMAND-16k (~2 GB) - speech enhancement (GCRN)
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

Each model has one config that drives all stages. All four run under the
``tidlrunner-am62d`` environment with :file:`devices/am62d_env.sh` already sourced
(see `Setup`_). Three models compile to the C7\ |trade| NPU through the TVM runtime.
The AM62D config paths are:

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
     - :file:`data/configs/samples/models/audio/audio_classification/urbansound8k/vggish11_tvmrt_config.yaml`
   * - YAMNet
     - ``ac-0201``
     - TVM-RT
     - 8
     - :file:`data/configs/samples/models/audio/audio_classification/urbansound8k/yamnet_tvmrt_config.yaml`
   * - GCRN
     - ``ase-0201``
     - TVM-RT
     - 16 (LSTM), FP32 (Enc/Dec)
     - :file:`data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_fixed_4sec_tvmrt_config.yaml`

VGGish11 (TVM-RT, 8-bit)
========================

Runs on the C7\ |trade| NPU (``tidl_offload: true``):

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/audio_classification/urbansound8k/vggish11_tvmrt_config.yaml
   $ tidlrunner-cli compile  --config_path $CFG
   $ tidlrunner-cli infer    --config_path $CFG
   $ tidlrunner-cli evaluate --config_path $CFG

``evaluate`` reports top-1 / top-5 / macro-F1 over UrbanSound8K fold 10.

YAMNet (TVM-RT, 8-bit)
======================

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/audio_classification/urbansound8k/yamnet_tvmrt_config.yaml
   $ tidlrunner-cli compile  --config_path $CFG
   $ tidlrunner-cli infer    --config_path $CFG
   $ tidlrunner-cli evaluate --config_path $CFG

GCRN (TVM-RT, 16-bit)
=====================

GCRN is C7\ |trade| NPU-offloaded at 16-bit (``tidl_offload: true``, fixed 4-second
input):

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_fixed_4sec_tvmrt_config.yaml
   $ tidlrunner-cli compile  --config_path $CFG
   $ tidlrunner-cli infer    --config_path $CFG
   $ tidlrunner-cli evaluate --config_path $CFG

``evaluate`` reports PESQ / STOI / SI-SDR over the VoiceBank-DEMAND-16k test set.
