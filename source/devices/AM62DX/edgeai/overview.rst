.. _am62dx_edgeai_overview:

########
Overview
########

**Welcome to Processor SDK Linux Edge AI for AM62DX!**

The SDK provides software and tools to run high-performance deep learning inference
on Texas Instruments' AM62DX processor. It enables a practical Edge AI solution by
combining a high-performance A53 ARM processor with a dedicated DSP optimized for
neural network inference and digital signal processing. This Edge AI inference chain
is a common pattern across TI devices, allowing efficient on-device AI workloads with
real-time performance. The AM62DX specifically supports audio modality to run
audio analytics pipelines such as speech enhancement and audio classification
on the DSP.

.. figure:: /images/am62dx_web_gui_home.png
   :scale: 50
   :align: center

   AM62DX out-of-box web GUI home screen

.. figure:: /images/am62dx_web_gui_speech_enhancement_result_1.png
   :scale: 50
   :align: center

   AM62DX out-of-box web GUI Audio Intelligence demo

.. figure:: /images/edgeai/edgeai-sdk-feature.png
   :scale: 50
   :align: center

   Processor SDK Linux Edge AI for AM62DX feature overview

The SDK enables an interplay of open-source components such as GStreamer and
deep learning runtimes such as TVM-RT. The SDK supports edit-build-debug
cycles directly on the target and also on a host PC to cross-compile and
build the applications.

.. figure:: /images/am62dx_open_src_comp.png
   :scale: 50
   :align: center

   Industry Standard Components supported in Processor SDK Linux Edge AI for AM62DX

The SDK mainly comprises of three parts as shown in the illustration below.

- **Edge AI application stack** — Linux-side applications and GStreamer pipelines
  that drive audio inference using TVM-RT and open-source components.
- **Foundational Linux components** — OS, U-Boot, kernel, filesystem, and Linux
  drivers that form the base platform.
- **DSP firmware** — C7x DSP firmware that runs the signal chain (STFT/ISTFT) and
  TVM model inference on the dedicated DSP hardware.

.. figure:: /images/am62dx_edgeai_stack.png
   :scale: 80
   :align: center

To get started with the setup click the **Next** button.
