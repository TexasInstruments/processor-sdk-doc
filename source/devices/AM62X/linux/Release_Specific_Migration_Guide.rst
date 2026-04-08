###############
Migration Guide
###############

.. rubric:: Overview

This page covers migration information for applications built on top
of the Processor SDK Linux AM62X.

****************************************
Processor SDK Linux AM62X 12.xx Releases
****************************************

Processor SDK 12.00.00.07.04
============================
- This is the first reference release on the 2026 LTS stream with 6.18 Kernel, 2026.01 U-Boot
- ATF 2.14+
- OPTEE 4.9.0+
- Yocto Master
- Platforms Supported : AM62x (HS-FS, HS-SE) : `SK-AM62 <https://www.ti.com/tool/SK-AM62>`__ , `SK-AM62B <https://www.ti.com/tool/SK-AM62B>`__ , `SK-AM62B-P1 <https://www.ti.com/tool/SK-AM62B-P1>`__
- Platforms Supported : AM62x LP (HS-FS, HS-SE) : `SK-AM62-LP <https://www.ti.com/tool/SK-AM62-LP>`__
- Platforms Supported : AM62SIP (HS-FS, HS-SE) : `SK-AM62-SIP <https://www.ti.com/tool/SK-AM62-SIP>`__
- Platforms Supported : BeaglePlay (GP) : `BeaglePlay <https://www.ti.com/tool/BEAGL-PLAY-SBC>`__

.. note::

    - For U-Boot builds, k3-image-gen and core-secdev-k3 are no longer needed
      as **binman** is used instead. Please refer to :ref:`U-Boot build
      instructions<Build-U-Boot-label>` for the updated steps.

    - For Linux builds, generic ``defconfig`` is used instead of custom
      fragments. Please refer to :ref:`Linux Kernel User Guide <preparing-to-build>`
      for build instructions.

.. include:: _AM62_Enable_UHS_MMCSD.rst
