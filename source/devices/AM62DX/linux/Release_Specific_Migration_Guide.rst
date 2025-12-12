###############
Migration Guide
###############

.. rubric:: Overview

This page covers migration information for applications built on top
of the Processor SDK Linux AM62D.

****************************************
Processor SDK Linux AM62D 11.xx Releases
****************************************

Processor SDK 11.02.08.02
=========================
- This is the second reference release on the 2025 LTS stream with 6.12 Kernel, 2025.01 U-Boot and Yocto Scarthgap/5.0
- ATF 2.13+
- OPTEE 4.7.0
- Yocto Scarthgap/5.0
- Platforms Supported : AM62Dx (HS-FS, HS-SE) : `AM62D-EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__

Processor SDK 11.01.05.03
=========================
- This is the first reference release on the 2025 LTS stream with 6.12 Kernel, 2025.01 U-Boot and Yocto Scarthgap/5.0
- ATF 2.13+
- OPTEE 4.6.0
- Yocto Scarthgap/5.0
- Platforms Supported : AM62Dx (HS-FS, HS-SE) : `AM62D-EVM <https://www.ti.com/tool/AUDIO-AM62D-EVM>`__

.. note::

   - For U-Boot builds, k3-image-gen and core-secdev-k3 are no longer needed
     as **binman** is used instead. Please refer to :ref:`U-Boot build
     instructions<Build-U-Boot-label>` for the updated steps.

   - For Linux builds, generic ``defconfig`` is used instead of custom
     fragments. Please refer to :ref:`Kernel doc<preparing-to-build>` for
     build instructions.
