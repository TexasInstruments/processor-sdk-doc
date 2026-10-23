.. _audioai-model-inspect:

#############
Model Inspect
#############

Model Inspector analyzes a model on the x86 host after (or instead of) the
:ref:`compile and evaluate <audioai-compile-evaluate>` flow. It uses the same
edgeai-tidlrunner installation and environment described in
:ref:`Setup <audioai-am62d-setup>`.

***************
Model Inspector
***************

``tidlrunner-cli inspect`` is a one-shot analysis pipeline: it compiles the
model for TIDL, runs inference, re-runs a non-TIDL reference for comparison,
computes per-layer signal-to-noise ratios, and emits a **self-contained
interactive HTML report** - no need to run ``compile`` and ``infer``
separately. The report opens in any browser and lands at:

.. code-block:: text

   work_dirs/compile/<target_device>/<bits>/<model_dir>/inspect/modelinspector.html

``<model_dir>`` is the model's work directory, named after its model ID,
runtime, task, dataset, and model, e.g.
``ase-0201_tvmrt_speech_enhancement_voicebank_demand_16k_gcrn_fixed_4sec_onnx``.

The report has three tabs:

- **Model Summary** - acceleration ratio (layers on the C7x™ DSP vs. Arm
  fallback), input/output specs, and an interactive ONNX graph.
- **Subgraphs** - the TIDL subgraph(s) offloaded to the DSP, with per-layer
  identity and a quantization analysis (INT8 vs. FP32 activation histograms and
  scatter plots).
- **Performance** - *estimated* per-layer processing time, DSP cycle breakdown
  (total / IO / kernel), memory usage (DDR / L2 / MSMC), and SNR metrics.

.. note::

   All Performance-tab numbers are **estimates** from the compiler, not
   on-target measurements. Model Inspector requires TIDL tools **11.02 or
   later** (earlier versions emit SVG subgraph files it cannot read).

GCRN showcase - an offloaded DSP subgraph
=========================================

Because GCRN now compiles with ``tidl_offload: true`` on AM62D, its inspector
report shows a **real C7x™ DSP subgraph** rather than an all-Arm fallback:
the Subgraphs tab lists a single offloaded subgraph (16-bit) with its layer
mapping, and the Performance tab breaks that subgraph down by cycles and memory.
Generate it with the AM62D env sourced (see :ref:`Setup <audioai-am62d-setup>`):

.. code-block:: console

   $ CFG=data/configs/samples/models/audio/speech_enhancement/voicebank_demand_16k/gcrn_fixed_4sec_tvmrt_config.yaml
   $ tidlrunner-cli inspect --config_path $CFG

For contrast, running ``inspect`` on the GTCRN (ONNX-RT) config produces a
report with **no** DSP subgraph - every layer is Arm fallback - which is what a
non-offloaded model looks like in the inspector. GTCRN also runs with
``tidl_offload: false``, so its work directory uses a ``notidl`` segment in
place of the ``<bits>`` shown in the path template above, e.g.
``work_dirs/compile/AM62D/notidl/<model_dir>/...``.
