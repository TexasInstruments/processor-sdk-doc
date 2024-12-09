************************************
CoreSDK Linux Migration Guide
************************************

.. rubric:: Overview

This page covers migration information for applications built on top
of the Processor SDK for Linux.

Processor CoreSDK 10.xx Releases
================================

Processor CoreSDK Sitara 10.01
------------------------------

- Tag Info: 10.01.10
- This is the final release in the 2024 LTS stream, with new stable versions of Kernel, U-boot, toolchain and Yocto Distribution.
- Platforms Supported : AM62Px (HS-FS, HS-SE), AM62x ( GP, HS-FS, HS-SE), AM62x LP (HS-FS, HS-SE), AM62SIP ( HS-FS, HS-SE), AM64x 2.0 (HS-FS), AM62A (HS-FS, HS-SE)
- Kernel 6.6.58
- U-Boot 2024.04
- ATF 2.11+
- OPTEE 4.4.0
- Toolchain GCC 13.3
- Yocto Scarthgap/5.0
- Graphics DDK 24.1


Processor CoreSDK Sitara 10.00
------------------------------

- Tag Info: 10.00.07
- This is the first release in the 2024 LTS stream, with new stable versions of Kernel, U-boot, toolchain and Yocto Distribution.
- Platforms Supported : AM62Px (HS-FS, HS-SE), AM62x ( GP, HS-FS, HS-SE), AM62x LP (HS-FS, HS-SE), AM62SIP ( HS-FS, HS-SE), AM64x 2.0 (HS-FS), AM62A (HS-FS, HS-SE)
- Kernel 6.6.32
- U-Boot 2024.04
- ATF 2.10+
- OPTEE 4.2.0
- Toolchain GCC 13.2
- Yocto Scarthgap/5.0
- Graphics DDK 24.1


.. note::

    - For U-Boot builds, k3-image-gen and core-secdev-k3 are no longer needed
      as **binman** is used instead. Please refer to :ref:`U-Boot build
      instructions<Build-U-Boot-label>` for the updated steps.

    - For Linux builds, generic ``defconfig`` is used instead of custom
      fragments. Please refer to :ref:`linux users guide <preparing-to-build>`
      for build instructions.
