.. _audioai-performance:

#####################
Performance Benchmark
#####################

.. |tm| unicode:: U+2122

This section reports **inference performance** — latency and memory — for the
four |__PART_FAMILY_NAME__| Audio AI models. It is **not** an accuracy or
audio-quality benchmark: model quality (classification accuracy, PESQ / STOI /
SI-SDR) is measured by the ``evaluate`` step in
:ref:`Compile / Evaluate / Inspect <audioai-compile-evaluate-inspect>`.

***********
Methodology
***********

Two independent figures are reported for each model, and they must not be
confused:

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Figure
     - How it is obtained
   * - **perfsim estimate**
     - Produced by the TIDL performance simulator during ``compile``. The
       compiler writes a ``result.yaml`` per model under its work directory;
       the ``perfsim`` latency, GMAC count, and estimated DDR transfer are
       read directly from it. This is a *static estimate* for the C7x\ |tm|
       NPU subgraph — it does not include Arm-side pre/post-processing or
       runtime overhead.
   * - **on-target measured**
     - Wall-clock latency timed on the AM62D target while running the
       :ref:`Model Zoo <audioai-model-zoo>` inference scripts. For the
       streaming speech-enhancement models it is also expressed as a
       **real-time factor (RTF)** = processing time ÷ audio duration; RTF < 1
       means the model keeps up with real-time audio.

Only models compiled for the C7x\ |tm| NPU (TVM-RT + TIDL) have a perfsim
estimate. GTCRN runs FP32 on the Arm core through the ONNX runtime and has no
TIDL subgraph, so perfsim does not apply to it.

.. note::

   The perfsim values below are read from ``result.yaml`` and are labelled
   *estimated (perfsim)*. On-target measured latency and RTF are marked **TBD**
   until measured on the AM62D EVM.

*****************
Per-model results
*****************

.. list-table::
   :header-rows: 1
   :widths: 16 12 12 20 14 26

   * - Model
     - Model ID
     - Precision
     - perfsim latency *(estimated)*
     - GMACs
     - DDR transfer *(estimated)*
   * - VGGish11
     - |__MODEL_ID_VGGISH11__|
     - 8-bit
     - 5.235 ms
     - 1.1515
     - 10.73 MB
   * - YAMNet
     - |__MODEL_ID_YAMNET__|
     - 8-bit
     - 1.990 ms
     - 0.0692
     - 3.55 MB
   * - GCRN
     - |__MODEL_ID_GCRN__|
     - 16-bit
     - TBD
     - TBD
     - TBD
   * - GTCRN
     - |__MODEL_ID_GTCRN__|
     - FP32 (Arm)
     - N/A
     - N/A
     - N/A

VGGish11 and YAMNet are compiled and have ``result.yaml`` perfsim values (shown
above). GCRN is compiled at 16-bit but its ``result.yaml`` is not yet captured,
so its perfsim figures are **TBD**. GTCRN is Arm-only (no TIDL subgraph), so
perfsim is **N/A**.

On-target measured latency and RTF for all four models are **TBD** — to be
filled in from the Model Zoo inference scripts on the AM62D EVM:

.. list-table::
   :header-rows: 1
   :widths: 20 20 30 30

   * - Model
     - On target
     - Measured latency
     - RTF
   * - VGGish11
     - C7x\ |tm| NPU
     - TBD
     - — (clip classifier)
   * - YAMNet
     - C7x\ |tm| NPU
     - TBD
     - — (clip classifier)
   * - GCRN
     - C7x\ |tm| NPU
     - TBD
     - TBD
   * - GTCRN
     - Arm core
     - TBD
     - TBD

RTF is reported only for the streaming speech-enhancement models (GCRN, GTCRN);
VGGish11 and YAMNet classify a whole clip, so a real-time factor is not
meaningful for them.

********
Non-goal
********

This section does **not** assess model quality. Classification accuracy and
speech-enhancement quality metrics are produced by ``tidlrunner-cli evaluate``
and documented in
:ref:`Compile / Evaluate / Inspect <audioai-compile-evaluate-inspect>`.
