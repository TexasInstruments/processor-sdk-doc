*****************************
CoreSDK Linux Migration Guide
*****************************

.. rubric:: Overview

This page covers migration information for applications built on top
of the Processor SDK for Linux.

Processor CoreSDK 11.xx Releases
================================


Processor CoreSDK Sitara 11.01
------------------------------

- Tag Info: 11.01.16
- This is the Fifth Reference release in the 2025 LTS stream, with new stable versions of Kernel, U-boot, toolchain and Yocto Distribution.
- Platforms Supported : AM62L SR1.1 (HS-FS, HS-SE),  AM62Px SR1.1 (HS-FS, HS-SE) ,  AM62Px SR1.2 (HS-FS, HS-SE)
- Kernel 6.12.43
- U-Boot 2025.01
- ATF 2.13+ (For AM62Px), 2.12+ (For AM62Lx)
- OPTEE 4.7.0+
- Toolchain GCC 13.4
- Yocto Scarthgap/5.0


Processor CoreSDK Sitara 11.01
------------------------------

- Tag Info: 11.01.07
- This is the Fourth Reference release in the 2025 LTS stream, with new stable versions of Kernel, U-boot, toolchain and Yocto Distribution.
- Platforms Supported : AM62A (HS-FS, HS-SE)
- Kernel 6.12.35
- U-Boot 2025.01
- ATF 2.13+
- OPTEE 4.6.0
- Toolchain GCC 13.4
- Yocto Scarthgap/5.0


Processor CoreSDK Sitara 11.01
------------------------------

- Tag Info: 11.01.05
- This is the Third Reference release in the 2025 LTS stream, with new stable versions of Kernel, U-boot, toolchain and Yocto Distribution.
- Platforms Supported : AM62Px SR1.0 (HS-FS, HS-SE), AM62Px SR1.1 (HS-FS, HS-SE),  AM62x ( GP, HS-FS, HS-SE), AM62x LP (HS-FS, HS-SE), AM64x 2.0 (HS-FS), AM62SIP (HS-FS, HS-SE) , AM62D (HS-FS)
- Kernel 6.12.35
- U-Boot 2025.01
- ATF 2.13+
- OPTEE 4.6.0
- Toolchain GCC 13.4
- Yocto Scarthgap/5.0
- Graphics DDK 24.2


Processor CoreSDK Sitara 11.00
------------------------------

- Tag Info: 11.00.15
- This is the Second Reference release in the 2025 LTS stream, with new stable versions of Kernel, U-boot, toolchain and Yocto Distribution.
- Platforms Supported : AM62Lx 1.0 (HS-FS, HS-SE)
- Kernel 6.12.24
- U-Boot 2025.01
- ATF 2.12+
- Toolchain GCC 13.3
- Yocto Scarthgap/5.0


Processor CoreSDK Sitara 11.00
------------------------------

- Tag Info: 11.00.09
- This is the First Reference release in the 2025 LTS stream, with new stable versions of Kernel, U-boot, toolchain and Yocto Distribution.
- Platforms Supported : AM62Px (HS-FS, HS-SE), AM62x ( GP, HS-FS, HS-SE), AM62x LP (HS-FS, HS-SE), AM64x 2.0 (HS-FS), AM62A (HS-FS, HS-SE)
- Kernel 6.12.17
- U-Boot 2025.01
- ATF 2.12+
- OPTEE 4.5.0
- Toolchain GCC 13.3
- Yocto Scarthgap/5.0
- Graphics DDK 24.2


.. note::

    - For U-Boot builds, k3-image-gen and core-secdev-k3 are no longer needed
      as **binman** is used instead. Please refer to :ref:`U-Boot build
      instructions<Build-U-Boot-label>` for the updated steps.

    - For Linux builds, generic ``defconfig`` is used instead of custom
      fragments. Please refer to :ref:`linux users guide <preparing-to-build>`
      for build instructions.
