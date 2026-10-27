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

.. figure:: /images/am62dx/edgeai/web_oob_home_screen.gif
   :align: center
   :width: 80%

   AM62DX out-of-box web GUI home screen

.. figure:: /images/edgeai/edgeai-sdk-feature.png
   :scale: 50
   :align: center

   Processor SDK Linux Edge AI for AM62DX feature overview

The SDK enables an interplay of open-source components such as GStreamer and
Apache TVM. The SDK supports editing, building, and debugging applications directly
on the target, as well as on a host PC where applications are cross-compiled and
built before being deployed to the target.

.. figure:: /images/am62dx_open_src_comp.png
   :scale: 50
   :align: center

   Industry Standard Components supported in Processor SDK Linux Edge AI for AM62DX

The SDK mainly comprises of three parts as shown in the illustration below.

- **Edge AI application stack** — Linux-side applications and GStreamer pipelines
  that drive audio inference using TVM-RT and open-source components.
- **Foundational Linux components** — AArch64 Linux , secure boot, filesystem, and Linux
  drivers that form the base platform.
- **MCU+ SDK** — firmware framework for the C7x™ DSP, handles signal chains (STFT/ISTFT, pre/post-processing)
  and model dispatch. Includes build system and flashing utilities.

.. figure:: /images/am62dx_sdk_overview.png
   :scale: 80
   :align: center

To get started with the setup click the **Next** button.
