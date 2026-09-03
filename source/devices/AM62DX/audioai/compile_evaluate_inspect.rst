.. _audioai-compile-evaluate-inspect:

############################
Compile / Evaluate / Inspect
############################

.. |tm| unicode:: U+2122

The :ref:`Audio AI Model Zoo <audioai-model-zoo>` runs *pre-compiled* artifacts
on the |__PART_FAMILY_NAME__| target. This section covers the **x86 host
workflow** that produces those artifacts: how to compile each audio model for
the C7x\ |tm| NPU, run host-emulation inference, and measure accuracy against a
dataset — using **edgeai-tidlrunner**. It runs entirely on an Ubuntu x86 PC;
nothing here touches the target.

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

********************
Setup
********************

Model compilation runs on an x86 PC (Ubuntu Linux recommended). The TIDL tools
used for compilation target Python 3.10, so create a dedicated Python 3.10
environment. These steps assume `pyenv <https://github.com/pyenv/pyenv>`__.

**1. Clone the repository** (|__TIDLRUNNER_REPO_URL__|):

.. code-block:: console

   $ git clone https://bitbucket.itg.ti.com/scm/edgeai-algo/edgeai-tidlrunner.git
   $ cd edgeai-tidlrunner

**2. Create and activate the Python 3.10 environment.**

.. code-block:: console

   $ pyenv install 3.10
   $ pyenv virtualenv 3.10 tidlrunner
   $ pyenv activate tidlrunner

**3. Run the PC setup script.** This downloads the TIDL tools into
``tools/tidl_tools_package/`` and installs the runner:

.. code-block:: console

   $ ./setup_runner_pc.sh

The TIDL tools version is pinned by ``TIDL_TOOLS_VERSION`` inside
``setup_runner_pc.sh`` and can be overridden on the command line. **The tools
version used to compile must match the version on the target** — artifacts
compiled for a different TIDL version will not run:

.. code-block:: console

   $ TIDL_TOOLS_VERSION="11.2.x" ./setup_runner_pc.sh

**4. Install the audio extras.** The audio pipelines need extra Python packages
(``librosa``, ``soundfile``, ``scipy``, ``pesq``, ``pystoi``, ``scikit-learn``):

.. code-block:: console

   $ pip install -e "tidlrunner[audio]"

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
test set; the speech-enhancement configs use the VoiceBank-DEMAND-16k test set
(824 files).

.. _audioai-am62d-interim-setup:

Interim AM62D TVM-RT compile path
=================================

.. warning::

   The AM62D C7x\ |tm| compile path for the three TVM-RT models (VGGish11,
   YAMNet, GCRN) is currently an **interim feasibility flow**, not the
   productized ``setup_runner_pc.sh`` / ``TIDL_TOOLS_VERSION`` download. It is
   documented here for reproducibility and will be replaced before release.

The three TVM-RT models compile through a **dedicated environment**
(``tidlrunner-am62d``) that has the release-candidate TVM wheel installed. That
wheel ships the x86 AM62D TIDL tools *inside* the package, so the AM62D compile
uses the wheel-bundled tools rather than the ones ``setup_runner_pc.sh``
downloads. TVM ``dlopen``\ s the TIDL runtime before Python's own import runs,
so the tool paths must be exported into the environment *before* ``tidlrunner-cli``
starts. A small wrapper, ``agent_ws/am62d-run.sh``, does this and then runs the
command you pass it. It exports:

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
     - path to your aarch64 GNU toolchain (e.g. ``<arm-gnu-toolchain>``)
   * - ``CGT7X_ROOT``
     - path to your C7000 code-generation tools (e.g. ``<ti-cgt-c7000>``)
   * - ``SOC``
     - ``am62d``

Activate the dedicated environment, then prefix each TVM-RT command with the
wrapper (the whole ``tidlrunner-cli`` invocation is passed as one quoted
argument):

.. code-block:: console

   $ pyenv activate tidlrunner-am62d
   $ bash agent_ws/am62d-run.sh "tidlrunner-cli compile --config_path <cfg>"

.. note::

   GTCRN does **not** use this wrapper. It runs ARM-only through ONNX Runtime
   (``tidl_offload: false``) and compiles under the standard ``tidlrunner``
   environment from steps 1–4.

.. TODO(WI-004): replace the interim ``agent_ws/am62d-run.sh`` wrapper +
   ``tidlrunner-am62d`` venv with the productized ``setup_runner_pc.sh`` /
   ``TIDL_TOOLS_VERSION`` AM62D flow before release. Confirm the final tools
   version string (artifact folder 11_02_18_00 vs. RC bundled tools 11.02.16.00).

********************
Compile and evaluate
********************

Each model has one config that drives all stages. Three models compile to the
C7x\ |tm| NPU through the TVM runtime; GTCRN is the ONNX-RT exception that runs
ARM-only. The final AM62D config paths are:

.. list-table::
   :header-rows: 1
   :widths: 14 10 12 10 54

   * - Model
     - Model ID
     - Runtime
     - Bits
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
     - 16
     - ``data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_fixed_4sec_tvmrt_config.yaml``
   * - GTCRN
     - |__MODEL_ID_GTCRN__|
     - ONNX-RT
     - FP32
     - ``data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gtcrn_dns3_config.yaml``

VGGish11 (TVM-RT, 8-bit)
========================

Runs on the C7x\ |tm| NPU (``tidl_offload: true``). Use the AM62D wrapper:

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/audio_classification/urbansound8k/vggish11_tvmrt_config.yaml
   $ bash agent_ws/am62d-run.sh "tidlrunner-cli compile  --config_path $CFG"
   $ bash agent_ws/am62d-run.sh "tidlrunner-cli infer    --config_path $CFG"
   $ bash agent_ws/am62d-run.sh "tidlrunner-cli evaluate --config_path $CFG"

``evaluate`` reports top-1 / top-5 / macro-F1 over UrbanSound8K fold 10.

YAMNet (TVM-RT, 8-bit)
======================

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/audio_classification/urbansound8k/yamnet_tvmrt_config.yaml
   $ bash agent_ws/am62d-run.sh "tidlrunner-cli compile  --config_path $CFG"
   $ bash agent_ws/am62d-run.sh "tidlrunner-cli infer    --config_path $CFG"
   $ bash agent_ws/am62d-run.sh "tidlrunner-cli evaluate --config_path $CFG"

GCRN (TVM-RT, 16-bit)
=====================

GCRN is C7x\ |tm|-offloaded at 16-bit (``tidl_offload: true``, fixed 4-second
input). Same wrapper flow:

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_fixed_4sec_tvmrt_config.yaml
   $ bash agent_ws/am62d-run.sh "tidlrunner-cli compile  --config_path $CFG"
   $ bash agent_ws/am62d-run.sh "tidlrunner-cli infer    --config_path $CFG"
   $ bash agent_ws/am62d-run.sh "tidlrunner-cli evaluate --config_path $CFG"

``evaluate`` reports PESQ / STOI / SI-SDR over the VoiceBank-DEMAND-16k test set.

GTCRN (ONNX-RT, ARM-only)
=========================

GTCRN has a dynamic time axis and TIDL-unsupported operators, so it runs on the
Arm Cortex-A cores through ONNX Runtime (``tidl_offload: false``) — no C7x\ |tm|
offload and **no** AM62D wrapper. Run it directly under the standard
``tidlrunner`` environment:

.. code-block:: console

   $ pyenv activate tidlrunner
   $ CFG=data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gtcrn_dns3_config.yaml
   $ tidlrunner-cli compile  --config_path $CFG --target_device AM62D
   $ tidlrunner-cli infer    --config_path $CFG --target_device AM62D
   $ tidlrunner-cli evaluate --config_path $CFG --target_device AM62D

.. note::

   The shipped ``gtcrn_dns3_config.yaml`` sets ``target_device: AM62A``; because
   the model is ARM-only, execution is device-independent. Passing
   ``--target_device AM62D`` keeps its work directory under the AM62D tree,
   consistent with the other three models.

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

- **Model Summary** — acceleration ratio (layers on the C7x\ |tm| DSP vs. Arm
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
report shows a **real C7x\ |tm| DSP subgraph** rather than an all-Arm fallback:
the Subgraphs tab lists a single offloaded subgraph (16-bit) with its layer
mapping, and the Performance tab breaks that subgraph down by cycles and memory.
Generate it through the AM62D wrapper:

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_fixed_4sec_tvmrt_config.yaml
   $ bash agent_ws/am62d-run.sh "tidlrunner-cli inspect --config_path $CFG"

For contrast, running ``inspect`` on the GTCRN (ONNX-RT) config produces a
report with **no** DSP subgraph — every layer is Arm fallback — which is what a
non-offloaded model looks like in the inspector.
