.. http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_Migration_Guide

************************************
Processor SDK Linux Migration Guide
************************************

.. rubric:: Overview

This page covers migration information for applications built on top
of the Processor SDK for Linux.

Processor SDK 10.xx Releases
================================

Processor SDK Jacinto 10.01
-------------------------------
- This is the Second release in the 2024 LTS stream 6.6 kernel, 2024.04 U-Boot and Yocto scarthgap/5.0
- Device tree updated with dual license
- ATF 2.11+
- OPTEE 4.20
- Yocto Scarthgap/5.0
- Platforms Supported : J721E, J7200, J721S2, J784S4, AM68, AM69, J722S, J742S2

Processor SDK Jacinto 10.00
-------------------------------
- This is the first release in the 2024 LTS stream 6.6 kernel, 2024.04 U-Boot and Yocto scarthgap/5.0
- ATF 2.10+
- OPTEE 4.20
- Yocto Scarthgap/5.0
- Platforms Supported : J721E, J7200, J721S2, J784S4, AM68, AM69, J722S

.. note::

    - For U-Boot builds, k3-image-gen and core-secdev-k3 are no longer needed
      as **binman** is used instead. Please refer to :ref:`U-Boot build
      instructions<Build-U-Boot-label>` for the updated steps.

    - For Linux builds, generic ``defconfig`` is used instead of custom
      fragments. Please refer to `linux users guide
      <../../../linux/Foundational_Components_Kernel_Users_Guide.html#preparing-to-build>`__
      for build instructions.
