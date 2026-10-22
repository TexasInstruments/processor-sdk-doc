.. _audioai-index:

#########################################
AM62D EdgeAI Software Developer's Guide
#########################################

.. rubric:: Welcome to the AM62D EdgeAI/DL Software Developer's Guide

This guide covers the EdgeAI model workflow (model zoo, compile/evaluate/inspect,
performance) as well as the GStreamer plugins that run audio processing and neural
network inference on the AM62Dx C7x DSP: ``tidspkernel`` for STFT, ISTFT and
deinterleave/interleave, and ``titvm`` for TVM model inference.

.. toctree::
   :maxdepth: 5
   :numbered:

   overview
   evm_hardware_setup
   out_of_box_demo
   models_artifacts_and_setup
   linux_audio_inference_app
   getting_started_gstreamer
   audio_ai_model_workflow
   model_zoo
   model_compile_evaluate
   model_inspect
   adding_new_model
   performance


|

+--------------------------------+--------------------------------------------------------------------------------------------------+
| .. Image:: /images/E2e.jpg     | For technical support please post your questions at `http://e2e.ti.com <http://e2e.ti.com/>`__.  |
+--------------------------------+--------------------------------------------------------------------------------------------------+
