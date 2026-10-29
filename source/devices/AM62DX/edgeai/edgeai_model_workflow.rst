.. include:: <isonum.txt>

.. _edgeai-introduction:

#####################
EdgeAI Model Workflow
#####################

This guide covers the workflow for audio deep-learning (DL) models on the
|__PART_FAMILY_NAME__| platform, using |__SDK_FULL_NAME__|
|__EDGEAI_SDK_VERSION__|. It targets embedded developers. You can run,
compile, evaluate, and benchmark audio models on the AM62D. Run pre-compiled
artifacts directly on the target. Or use the 64-bit x86 compile-and-evaluate
workflow.

Four **reference models** serve as worked examples throughout the guide. The
workflow is not limited to them: the same compile-evaluate-inspect flow is a
bring-your-own-model (BYOM) flow that accepts any supported `ONNX
<https://onnx.ai/>`__ model. The guide will add more reference models over time.

The remaining sections cover:

- :ref:`EdgeAI Model Zoo <edgeai_model_zoo>` - out-of-box demos on the AM62D
  target (inference scripts and Jupyter notebooks) using pre-trained models and
  pre-compiled artifacts.
- :ref:`Model Compile and Evaluate <edgeai_compile_evaluate>` - the
  x86 BYOM workflow built on ``edgeai-tidlrunner``: compile a model for the AM62D
  and evaluate accuracy on a data set.
- :ref:`Model Inspect <edgeai_model_inspect>` - analyze the compiled subgraphs
  and per-layer behavior with Model Inspector.
- :ref:`Performance benchmark <edgeai_performance>` - latency and memory
  method with per-model tables.

********************
Development workflow
********************

The end-to-end path is the same for a reference model or your own model:

#. **Obtain an ONNX model** - a reference graph shipped with the EdgeAI ModelZoo,
   or your own exported ONNX.
#. **Compile** it for the C7\ |trade| Neural Processing Unit (NPU) on an x86 host
   (:ref:`Model Compile and Evaluate <edgeai_compile_evaluate>`).
#. **Evaluate** accuracy or audio-quality metrics on a data set.
#. **Inspect** the compiled subgraphs and per-layer analysis (:ref:`Model
   Inspect <edgeai_model_inspect>`).
#. **Run** on the AM62D target using the compiled artifact
   (:ref:`EdgeAI Model Zoo <edgeai_model_zoo>`).
#. **Benchmark** latency and memory (:ref:`Performance <edgeai_performance>`).

****************
Reference models
****************

Four reference models cover two task families. Each is a worked example of the
workflow, delivered as an `ONNX <https://onnx.ai/>`__ graph. Three of the four
run on the C7\ |trade| NPU through the TVM runtime (TVM-RT).

Audio analysis and classification
=================================

**VGGish11** (model ID ``ac-0101``)
   Audio-clip classification. Input is a log-mel patch of shape ``(1, 1, 64, 126)``;
   output is ``(1, 10)`` class logits plus a ``(1, 512)`` embedding. Runs at 8-bit,
   fully offloaded to the C7\ |trade| NPU via TVM-RT (a single TIDL subgraph).

**YAMNet** (model ID ``ac-0201``)
   Audio-event classification. Input is a log-mel patch of shape ``(1, 1, 96, 64)``;
   output is ``(1, 521)`` class scores. Runs at 8-bit, fully offloaded to the
   C7\ |trade| NPU via TVM-RT (a single TIDL subgraph).

Both classification models are evaluated on the UrbanSound8K data set.

Speech enhancement
==================

**GCRN** (model ID ``ase-0201``)
   Convolutional-recurrent speech enhancement (noise suppression) over a fixed 4-second
   window. Input and output are complex spectrograms of shape ``(1, 2, 401, 161)``.
   Runs at 16-bit and is offloaded to the C7\ |trade| NPU via TVM-RT
   (``tidl_offload: true``).

Both speech-enhancement models are evaluated on the VoiceBank-DEMAND-16k
data set.

.. _edgeai-tvm-tidl:

********************
TVM + TIDL framework
********************

The AM62D audio models compile and deploy with **TI TVM**. This is TI's fork
of the `Apache TVM <https://tvm.apache.org/>`__ deep-learning compiler. The
target accelerator is the **C7**\ |trade| **NPU** - TI's Neural Processing
Unit. It combines the **C7x DSP** with the **Matrix Multiplication
Accelerator (MMA)**. Older documents call this combination *C7x+MMA*.

TI TVM adds **TIDL** (TI Deep Learning) as an accelerator backend. TIDL
offloads supported layers to the MMA. TVM generates **C7x DSP** code for any
layers that are left. The MMA and the C7x DSP together form the C7\ |trade|
NPU. The result is one deployable artifact. The **entire model runs on the
C7**\ |trade| **NPU**.

Compilation runs on an x86 host in three stages:

#. **Model import** - TVM imports the ONNX graph.
#. **Partitioning** - the TIDL import API splits the graph into TIDL-supported
   subgraphs and the rest. The TIDL network compiler builds the subgraphs. TVM
   generates C7x DSP code for the rest.
#. **Artifact generation** - TVM packages both parts into one TVM-RT
   deployable artifact (:file:`deploy_lib.so` + :file:`deploy_graph.json` +
   :file:`deploy_param.params`).

At run time, the AM62D TVM runtime loads this artifact. It then sends the
offloaded subgraphs to TIDL-RT on the C7\ |trade| NPU.

.. figure:: /images/audioai/tvm_tidl_flow.svg
   :width: 80 %
   :align: center

   TVM + TIDL compile-and-deploy flow for the AM62D audio models. Green blocks
   are handled by TIDL; white blocks are handled by TVM.
