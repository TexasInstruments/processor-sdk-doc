.. _audioai-compile-evaluate-inspect:

##################################
Model Compile / Evaluate / Inspect
##################################

.. |tm| unicode:: U+2122

The :ref:`Audio AI Model Zoo <audioai-model-zoo>` runs *pre-compiled* artifacts
on the |__PART_FAMILY_NAME__| target. This section covers the **x86 host
workflow** that produces those artifacts: how to compile an audio model for
the C7\ |tm| NPU, run host-emulation inference, and measure accuracy against a
dataset — using **edgeai-tidlrunner**. It runs entirely on an Ubuntu x86 PC;
nothing here touches the target.

This is the workflow for *any* audio model, not just the reference models. The
four reference models below are worked examples. To bring your own model you
point the same ``tidlrunner-cli`` at your ONNX graph and a per-model YAML config,
using a reference config as a starting template. Which operators offload to the
C7\ |tm| NPU (vs. fall back to the Arm core) is determined by TIDL — see
`edgeai-tidl-tools <https://github.com/TexasInstruments/edgeai-tidl-tools>`__ for
the authoritative list of supported operators.

********************
edgeai-tidlrunner
********************

edgeai-tidlrunner is a bring-your-own-model (BYOM) command-line wrapper over the
core `edgeai-tidl-tools <https://github.com/TexasInstruments/edgeai-tidl-tools>`__
compilation stack. A single YAML config per model drives every stage, and one
CLI — ``tidlrunner-cli`` — exposes the stages this section uses:

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
     - Runs the compiled model over a dataset and reports accuracy or
       speech-enhancement metrics.
   * - ``inspect``
     - One-shot compile + inference + reference comparison that emits an
       interactive HTML analysis report (see `Model Inspector`_).

All commands are run from the repository root (``edgeai-tidlrunner/``) and take
``--config_path <cfg>`` pointing at the per-model YAML. The same config file is
reused across ``compile``, ``infer``, and ``evaluate``.

.. _audioai-am62d-setup:

********************
Setup
********************

Model compilation runs on an x86 PC (Ubuntu Linux recommended). The AM62D audio
flow is self-contained: a single setup script installs the whole TVM toolchain
into a dedicated Python 3.10 environment. The TIDL tools target Python 3.10.
These steps assume `pyenv <https://github.com/pyenv/pyenv>`__.

**1. Clone the repository** (|__TIDLRUNNER_REPO_URL__|):

.. code-block:: console

   $ git clone https://github.com/TexasInstruments/edgeai-tidlrunner.git
   $ cd edgeai-tidlrunner

**2. Create and activate a dedicated Python 3.10 environment.** The AM62D flow
uses a TI TVM wheel; keep it in its own venv (``tidlrunner-am62d``)
so it never clobbers a standard ``tidlrunner`` setup:

.. code-block:: console

   $ pyenv install 3.10
   $ pyenv virtualenv 3.10 tidlrunner-am62d
   $ pyenv activate tidlrunner-am62d

**3. Run the AM62D setup script.** With the venv active, one script installs
everything this flow needs:

.. code-block:: console

   $ ./devices/setup_am62d.sh

It downloads the ARM GCC 15.2 and C7000 CGT 5.0.0.LTS cross-toolchains into
``tools/tidl_tools_package/bin/`` (skipped if already present), installs the
x86 TI TVM wheel — which bundles the AM62D x86 TIDL tools *inside*
the package — and installs ``tidlrunner[pc,audio]``, ``tools``, ``onnxruntime``,
and ``tidl_onnx_model_optimizer``. The ``[audio]`` extra pulls in the audio
packages (``librosa``, ``soundfile``, ``scipy``, ``pesq``, ``pystoi``,
``scikit-learn``). No separate ``pip install`` is needed.

**4. Source the env script once per shell.** TVM ``dlopen``\ s the TIDL runtime
(``libvx_tidl_rt.so``) before Python's own import runs, so the tool paths must be
live in the shell *before* ``tidlrunner-cli`` starts. Source — do **not** execute
— ``devices/am62d_env.sh`` once; every ``tidlrunner-cli`` command run afterward in
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
     - ``<tvm-package-dir>/3rdparty/x86_tidl_tools/AM62D`` (resolved from the
       active venv's installed ``tvm``)
   * - ``LD_LIBRARY_PATH``
     - prepends ``TIDL_TOOLS_PATH`` so ``libvx_tidl_rt.so`` resolves
   * - ``ARM64_GCC_PATH``
     - the aarch64 GNU toolchain installed by ``setup_am62d.sh`` under
       ``tools/tidl_tools_package/bin/`` (override by exporting before sourcing)
   * - ``CGT7X_ROOT``
     - the C7000 code-generation tools installed by ``setup_am62d.sh`` under
       ``tools/tidl_tools_package/bin/`` (override by exporting before sourcing)
   * - ``SOC``
     - ``am62d``

Datasets
========

Accuracy evaluation needs the reference datasets. Compilation alone can run on
random data (for latency-only measurement), but ``evaluate`` requires the real
sets. Download them from the repository root:

.. code-block:: console

   $ # UrbanSound8K (~5.6 GB) — sound classification (VGGish11, YAMNet)
   $ bash examples/audio/scripts/download_urbansound8k.sh

   $ # VoiceBank-DEMAND-16k (~2 GB) — speech enhancement (GCRN, GTCRN)
   $ python3 examples/audio/scripts/download_voicebank_demand.py

They land under ``data/datasets/UrbanSound8K/`` and
``data/datasets/VoiceBank-DEMAND-16k/`` — the paths the model configs expect.
The classification configs use UrbanSound8K **fold 10** (837 samples) as the
test set; the speech-enhancement configs use the VoiceBank-DEMAND-16k **test** set
(824 files).

The reference ONNX models auto-download at compile time via ``.link`` files, so
fetching them ahead of time is **optional**. To pre-download all reference ONNX models:

.. code-block:: console

   $ bash examples/audio/scripts/download_audio_models.sh

********************
Compile and evaluate
********************

Each model has one config that drives all stages. All four run under the
``tidlrunner-am62d`` environment with ``devices/am62d_env.sh`` already sourced
(see `Setup`_). Three models compile to the C7\ |tm| NPU through the TVM runtime;
GTCRN runs ARM-only through ONNX Runtime (no C7\ |tm| NPU offload) but uses the
same environment. The AM62D config paths are:

.. list-table::
   :header-rows: 1
   :widths: 12 10 12 18 54

   * - Model
     - Model ID
     - Runtime
     - Tensor Bits
     - Config path (relative to ``edgeai-tidlrunner/``)
   * - VGGish11
     - |__MODEL_ID_VGGISH11__|
     - TVM-RT
     - 8
     - ``data/configs/samples/models/audio/audio_classification/urbansound8k/vggish11_tvmrt_config.yaml``
   * - YAMNet
     - |__MODEL_ID_YAMNET__|
     - TVM-RT
     - 8
     - ``data/configs/samples/models/audio/audio_classification/urbansound8k/yamnet_tvmrt_config.yaml``
   * - GCRN
     - |__MODEL_ID_GCRN__|
     - TVM-RT
     - 16 (LSTM), FP32 (Enc/Dec)
     - ``data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_fixed_4sec_tvmrt_config.yaml``
   * - GTCRN
     - |__MODEL_ID_GTCRN__|
     - ONNX-RT
     - FP32
     - ``data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gtcrn_dns3_config.yaml``

VGGish11 (TVM-RT, 8-bit)
========================

Runs on the C7\ |tm| NPU (``tidl_offload: true``):

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

GCRN is C7\ |tm| NPU-offloaded at 16-bit (``tidl_offload: true``, fixed 4-second
input):

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_fixed_4sec_tvmrt_config.yaml
   $ tidlrunner-cli compile  --config_path $CFG
   $ tidlrunner-cli infer    --config_path $CFG
   $ tidlrunner-cli evaluate --config_path $CFG

``evaluate`` reports PESQ / STOI / SI-SDR over the VoiceBank-DEMAND-16k test set.

GTCRN (ONNX-RT, ARM-only)
=========================

GTCRN has a dynamic time axis and TIDL-unsupported operators, so it runs on the
Arm Cortex-A cores through ONNX Runtime (``tidl_offload: false``) — no C7\ |tm| NPU
offload. It uses the same ``tidlrunner-am62d`` environment as the other models;
it simply does not offload to the DSP:

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gtcrn_dns3_config.yaml
   $ tidlrunner-cli compile  --config_path $CFG
   $ tidlrunner-cli infer    --config_path $CFG
   $ tidlrunner-cli evaluate --config_path $CFG

********************
Model Inspector
********************

``tidlrunner-cli inspect`` is a one-shot analysis pipeline: it compiles the
model for TIDL, runs inference, re-runs a non-TIDL reference for comparison,
computes per-layer signal-to-noise ratios, and emits a **self-contained
interactive HTML report** — no need to run ``compile`` and ``infer``
separately. The report opens in any browser and lands at:

.. code-block:: text

   work_dirs/compile/<target_device>/<bits>/<model_id>/inspector/modelinspector.html

The report has three tabs:

- **Model Summary** — acceleration ratio (layers on the C7x DSP vs. Arm
  fallback), input/output specs, and an interactive ONNX graph.
- **Subgraphs** — the TIDL subgraph(s) offloaded to the DSP, with per-layer
  identity and a quantization analysis (INT8 vs. FP32 activation histograms and
  scatter plots).
- **Performance** — *estimated* per-layer processing time, DSP cycle breakdown
  (total / IO / kernel), memory usage (DDR / L2 / MSMC), and SNR metrics.

.. note::

   All Performance-tab numbers are **estimates** from the compiler, not
   on-target measurements. Model Inspector requires TIDL tools **11.02 or
   later** (earlier versions emit SVG subgraph files it cannot read).

GCRN showcase — an offloaded DSP subgraph
=========================================

Because GCRN now compiles with ``tidl_offload: true`` on AM62D, its inspector
report shows a **real C7x DSP subgraph** rather than an all-Arm fallback:
the Subgraphs tab lists a single offloaded subgraph (16-bit) with its layer
mapping, and the Performance tab breaks that subgraph down by cycles and memory.
Generate it with the AM62D env sourced (see `Setup`_):

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_fixed_4sec_tvmrt_config.yaml
   $ tidlrunner-cli inspect --config_path $CFG

For contrast, running ``inspect`` on the GTCRN (ONNX-RT) config produces a
report with **no** DSP subgraph — every layer is Arm fallback — which is what a
non-offloaded model looks like in the inspector. GTCRN also runs with
``tidl_offload: false``, so its work directory uses a ``notidl`` segment in
place of the ``<bits>`` shown in the path template above, e.g.
``work_dirs/compile/AM62D/notidl/<model_id>/...``.
