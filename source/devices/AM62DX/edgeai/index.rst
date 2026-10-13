.. _audioai-index:

#########################################
AM62D Audio AI Software Developer's Guide
#########################################

.. rubric:: Welcome to the AM62D Audio AI/DL Software Developer's Guide

.. toctree::
   :maxdepth: 5
   :numbered:

   overview
   getting_started_platform
   out_of_box_demo
   linux_audio_inference_app
   getting_started_gstreamer
   audio_ai_model_workflow
   model_zoo
   model_compile_evaluate
   model_inspect
   performance


|

.. rubric:: What the GStreamer plugins do

- **tidspkernel** runs STFT, ISTFT and deinterleave/interleave kernels on the C7x DSP.
- **titvm** runs TVM-compiled models, through the model daemon or in-process.
- Both elements exchange data with the DSP over RPMsg. Buffers are shared with DMA
  where the pipeline allows it.

|

+--------------------------------+--------------------------------------------------------------------------------------------------+
| .. Image:: /images/E2e.jpg     | For technical support please post your questions at `http://e2e.ti.com <http://e2e.ti.com/>`__.  |
+--------------------------------+--------------------------------------------------------------------------------------------------+
