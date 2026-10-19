.. _am62dx_edgeai_overview:

########
Overview
########

**Welcome to Processor SDK Linux Edge AI for AM62DX!**

The SDK provides software and tools to run high-performance deep learning inference
on Texas Instruments' AM62DX processor. It enables a practical Edge AI solution by
combining a high-performance A53 ARM processor with a dedicated C7x DSP optimized for
neural network inference and digital signal processing. This Edge AI inference chain
is a common pattern across TI devices, allowing efficient on-device AI workloads with
real-time performance. The AM62DX specifically supports audio modality (no vision);
for example, you can run audio analytics pipelines such as speech enhancement and
audio classification on the C7x DSP.

.. |pic1| image:: /images/am62dx_web_gui_home.png
   :align: middle
.. |pic2| image:: /images/am62dx_web_gui_speech_enhancement.png
   :align: middle
.. |pic3| image:: /images/am62dx_web_gui_audio_classification.png
   :align: middle

+--------+--------+--------+
| |pic1| | |pic2| | |pic3| |
+--------+--------+--------+

.. figure:: /images/edgeai/edgeai-sdk-feature.png
   :scale: 50
   :align: center

   Processor SDK Linux Edge AI for AM62DX feature overview

The SDK enables an interplay of open-source components such as GStreamer and
deep learning runtimes such as TVM-RT. The reference applications showcase
inference examples in C++ variants (audio AI for AM62DX). The SDK supports
edit-build-debug cycles directly on the target and also on a host PC to
cross-compile and build the applications.

.. figure:: /images/am62dx_open_src_comp.png
   :scale: 50
   :align: center

   Industry Standard Components supported in Processor SDK Linux Edge AI for AM62DX

The SDK mainly comprises of three parts as shown in the illustration below.
The Edge AI application stack is used to run audio analytics applications with
real-time inputs/outputs. The Foundational Linux components provide OS, U-Boot,
kernel, filesystem, Linux drivers and firmware for the C7x DSP and hardware
accelerators.

.. figure:: /images/am62dx_sdk_overview.jpg
   :scale: 80
   :align: center

To get started with the setup click the **Next** button.
