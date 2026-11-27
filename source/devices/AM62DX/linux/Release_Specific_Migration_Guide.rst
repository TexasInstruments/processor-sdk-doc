###############
Migration Guide
###############

.. rubric:: Overview

This page covers migration information for applications built on top
of the Processor SDK Linux AM62D.

****************************************
Processor SDK Linux AM62D 12.xx Releases
****************************************

Processor SDK 12.02.00.07.04
============================
- This is the second reference release on the 2026 LTS stream with 6.18 Kernel, 2026.01 U-Boot. Please see :ref:`release-specific-build-information`.
- Kernel 6.18.63
- U-Boot 2026.01
- ATF 2.15
- OPTEE 4.11.0
- Yocto Wrynose/6.0
- Platforms Supported : AM62Dx (HS-FS, HS-SE) : `AM62D-EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__

Processor SDK 12.00.00.07.04
============================
- This is the first reference release on the 2026 LTS stream with 6.18 Kernel, 2026.01 U-Boot
- ATF 2.14+
- OPTEE 4.9.0+
- Yocto Master
- Platforms Supported : AM62Dx (HS-FS, HS-SE) : `AM62D-EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__

.. note::

   - For U-Boot builds, k3-image-gen and core-secdev-k3 are no longer needed
     as **binman** is used instead. Please refer to :ref:`U-Boot build
     instructions<Build-U-Boot-label>` for the updated steps.

   - For Linux builds, generic ``defconfig`` is used instead of custom
     fragments. Please refer to :ref:`Kernel doc<preparing-to-build>` for
     build instructions.
