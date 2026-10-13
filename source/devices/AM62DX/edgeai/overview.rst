.. _am62dx_edgeai_overview:

########
Overview
########

**Welcome to Processor SDK Linux Edge AI for AM62DX!**

The SDK provides software and tools to let users run high-performance audio deep
learning inference on Texas Instruments' AM62DX processor. We offer a practical
embedded audio AI solution for smart speakers, industrial monitoring, voice interfaces,
and acoustic event detection applications. The AM62DX integrates a high-performance
A53 ARM processor with a dedicated C7x DSP optimized for neural network inference
and digital signal processing. With a few simple steps one can run real-time audio
AI pipelines such as speech enhancement and audio classification on the C7x DSP.

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
audio AI examples such as speech enhancement and audio classification in C++
variants. The SDK supports edit-build-debug cycles directly on the target and
also on a host PC to cross compile and build the applications.

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
