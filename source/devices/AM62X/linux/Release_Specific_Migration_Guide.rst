.. _release-specific-migration-guide:

###############
Migration Guide
###############

.. rubric:: Overview

This page covers migration information for applications built on top
of the Processor SDK Linux AM62X.

****************************************
Processor SDK Linux AM62X 10.xx Releases
****************************************

Processor SDK 10.01.10.04
=========================
- This is the final release on the 2024 LTS stream 6.6 kernel, 2024.04 U-Boot and Yocto Scarthgap/5.0
- ATF 2.11+
- OPTEE 4.4.0
- Yocto Scarthgap/5.0
- Platforms Supported : AM62x (HS-FS, HS-SE) : `SK-AM62 <https://www.ti.com/tool/SK-AM62>`__ , `SK-AM62B <https://www.ti.com/tool/SK-AM62B>`__ , `SK-AM62B-P1 <https://www.ti.com/tool/SK-AM62B-P1>`__
- Platforms Supported : AM62x LP (HS-FS, HS-SE) : `SK-AM62-LP <https://www.ti.com/tool/SK-AM62-LP>`__
- Platforms Supported : AM62SIP (HS-FS, HS-SE) : `SK-AM62-SIP <https://www.ti.com/tool/SK-AM62-SIP>`__
- Platforms Supported : BeaglePlay (GP) : `BeaglePlay <https://www.ti.com/tool/BEAGL-PLAY-SBC>`__


Processor SDK 10.00.07.04
=========================
- This is the first release on the 2024 LTS stream 6.6 kernel, 2024.04 U-Boot and Yocto Scarthgap/5.0
- ATF 2.10+
- OPTEE 4.2.0
- Yocto Scarthgap/5.0
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

.. include:: /linux/Release_Specific/_AM62_Enable_UHS_MMCSD.rst

.. include:: _Release_Specific_PLL.rst
