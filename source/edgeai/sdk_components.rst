.. _pub_sdk_components:

===============
SDK Components
===============

The Processor SDK Linux Edge AI for  |__PART_FAMILY_NAME__| mainly comprises of three layers,

    - **Edge AI application stack**
    - **Linux foundations**
    - **Firmware builder**

Edge AI application stack
=========================

The Edge AI applications are designed for users to quickly evaluate various
deep learning networks with real-time inputs on the TI SoCs. Users can
evaluate pre-imported inference models or build a custom network for deployment
on the device. Once a network is finalized for performance and accuracy
it can be easily integrated in a GStreamer based applications for rapid
prototyping and deployment. The Edge AI application stack can be split into
below components which integrates well with the underlying foundational Linux
components and interacts with remote core firmware for acceleration.

The entire Edge AI application stack can be downloaded on a PC and
cross-compiled for the desired target. For more details on the setup,
build and install steps please refer to **edgeai-app-stack** on `GitHub <https://github.com/TexasInstruments/edgeai-app-stack>`_

.. figure:: ../images/edgeai/edgeai-app-stack.jpg
   :scale: 65
   :align: center

.. _pub_edgeai_gst_apps:

edgeai-gst-apps
---------------
These are plug-and-play deep learning applications which support running open
source runtime frameworks such as TFLite, ONNX and TVM-RT with a variety of
input and output configurations.

The latest source code with fixes can be pulled from `TI Edge AI GStreamer apps <https://github.com/TexasInstruments/edgeai-gst-apps>`_

.. _pub_edgeai_dl_inferer:

edgeai-dl-inferer
-----------------
This repo provides interface to TI OSRT library whose APIs can be used standalone
or with an application like edgeai-gst-apps. It also provides the source of NV12
post processing library and utils which are used with some custom GStreamer
plugins.

The latest source code with fixes can be pulled from `TI Edge AI DL Inferer <https://git.ti.com/cgit/edgeai/edgeai-dl-inferer>`_

.. _pub_edgeai_gst_plugins:

edgeai-gst-plugins
------------------
This repo provides the source of custom GStreamer plugins which helps offload
tasks to the hardware accelerators with the help of edgeai-tiovx-modules.

Source code and documentation `TI Edge AI GStreamer plugins <https://github.com/TexasInstruments/edgeai-gst-plugins>`_

.. _pub_edgeai_tiovx_modules:

edgeai-app-utils
--------------------
This repo provides utility APIs for NV12 drawing and font rendering, reporting
MPU and DDR performance, ARM Neon optimized kernels for color conversion,
pre-processing and scaling.

Source code and documentation: `TI Edge AI Apps utils <https://git.ti.com/cgit/edgeai/edgeai-apps-utils>`_

edgeai-tiovx-modules
--------------------
This repo provides OpenVx modules which help access underlying hardware
accelerators in the SoC and serves as a bridge between GStreamer
custom elements and underlying OpenVx custom kernels.

Source code and documentation: `TI Edge AI TIOVX modules <https://git.ti.com/cgit/edgeai/edgeai-tiovx-modules>`_

.. _pub_edgeai_tiovx_kernels:

edgeai-tiovx-kernels
--------------------
This repo provides OpenVx kernels which help accelerate color-convert,
DL-pre-processing and DL-post-processing using ARMv8 NEON accelerator

Source code and documentation: `TI Edge AI TIOVX kernels <https://git.ti.com/cgit/edgeai/edgeai-tiovx-kernels>`_

.. _pub_edgeai_tiovx_apps:

edgeai-tiovx-apps
-----------------

This repo provides a layer on top of OpenVX to easily create a OpenVX
graph and connect them to v4l2 blocks to realize various complex
usecases

Source code and documentation: `TI Edge AI TIOVX Apps <https://github.com/TexasInstruments/edgeai-tiovx-apps>`_

.. _pub_edgeai_modelzoo:

Foundation Linux
================
The Edge AI app stack is built on top of foundation Linux components which
includes, u-boot, Linux kernels, device drivers, multimedia codecs and many more.
Developers use the Yocto project and publicly available sources to build Foundation Linux entirely from scratch.
We also offer an installer, which packages pre-built Linux filesystem, board support
package and tools to customize Linux layers of the software stack.

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   Click `AM62AX Linux Foundational components <https://software-dl.ti.com/processor-sdk-linux/esd/AM62AX/11_01_07_05/exports/docs/linux/Foundational_Components.html>`_
   to explore more!

.. ifconfig:: CONFIG_part_variant in ('AM67A')

   Click `AM67A Linux Foundation components <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-am67a/10_01_00/exports/docs/linux/Foundational_Components.html>`_
   to explore more!

.. ifconfig:: CONFIG_part_variant in ('AM68A')

   Click `AM68A Linux Foundation components <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-am68a/10_01_00/exports/docs/linux/Foundational_Components.html>`_
   to explore more!

.. ifconfig:: CONFIG_part_variant in ('AM69A')

   Click `AM69A Linux Foundation components <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-am69a/10_01_00/exports/docs/linux/Foundational_Components.html>`_
   to explore more!

.. ifconfig:: CONFIG_part_variant in ('TDA4VM')

   Click `Processor SDK Linux J721E Foundation Components <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-jacinto7/09_02_00_05/exports/docs/linux/Foundational_Components.html>`_
   to explore more!

Firmware builder
================

|__PART_FAMILY_NAME__| firmware builder package is required only when dealing
with low level software components such as remote core firmware, drivers to
hardware accelerators, system memory map changes etc. For user space application
development this is not required.

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   Access to `FIRMWARE-BUILDER-AM62AX <https://www.ti.com/securesoftware/docs/autopagepreview.tsp?opnId=28084>`_
   is provided via MySecureSW and requires a login.

   Click `AM62AX REQUEST LINK <https://www.ti.com/licreg/docs/swlicexportcontrol.tsp?form_id=337627&prod_no=FIRMWARE-BUILDER-AM62A&ref_url=EP-Proc-Sitara-MPU>`_
   to request access.

.. ifconfig:: CONFIG_part_variant in ('AM68A')

   Access to `FIRMWARE-BUILDER-AM68A <https://www.ti.com/securesoftware/docs/autopagepreview.tsp?opnId=28089>`_
   is provided via MySecureSW and requires a login.

   Click `AM68A REQUEST LINK <https://www.ti.com/licreg/docs/swlicexportcontrol.tsp?form_id=337467&prod_no=FIRMWARE-BUILDER-AM68A&ref_url=ep_processors_jacinto_adas>`_
   to request access.

.. ifconfig:: CONFIG_part_variant in ('AM69A')

   Access to `FIRMWARE-BUILDER-AM69A <https://www.ti.com/securesoftware/docs/autopagepreview.tsp?opnId=28088>`_
   is provided via MySecureSW and requires a login.

   Click `AM69A REQUEST LINK <https://www.ti.com/licreg/docs/swlicexportcontrol.tsp?form_id=337467&prod_no=FIRMWARE-BUILDER-AM69A&ref_url=ep_processors_jacinto_adas>`_
   to request access.

.. ifconfig:: CONFIG_part_variant in ('TDA4VM')

   Access to `FIRMWARE-BUILDER-TDA4VM <https://www.ti.com/securesoftware/docs/autopagepreview.tsp?opnId=28088>`_
   is provided via MySecureSW and requires a login.

   Click `TDA4VM REQUEST LINK <https://www.ti.com/licreg/docs/swlicexportcontrol.tsp?form_id=337467&prod_no=FIRMWARE-BUILDER-TDA4VM&ref_url=ep_processors_jacinto_adas>`_
   to request access.
