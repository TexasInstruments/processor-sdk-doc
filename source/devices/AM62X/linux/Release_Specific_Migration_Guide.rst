###############
Migration Guide
###############

.. rubric:: Overview

This page covers migration information for applications built on top
of the Processor SDK Linux AM62X.

****************************************
Processor SDK Linux AM62X 11.xx Releases
****************************************

Processor SDK 11.02.08.02
=========================
- This is the third reference release on the 2025 LTS stream with 6.12 Kernel, 2025.01 U-Boot and Yocto Scarthgap/5.0
- ATF 2.13+
- OPTEE 4.7.0
- Yocto Scarthgap/5.0
- Platforms Supported : AM62x (HS-FS, HS-SE) : `SK-AM62 <https://www.ti.com/tool/SK-AM62>`__ , `SK-AM62B <https://www.ti.com/tool/SK-AM62B>`__ , `SK-AM62B-P1 <https://www.ti.com/tool/SK-AM62B-P1>`__
- Platforms Supported : AM62x LP (HS-FS, HS-SE) : `SK-AM62-LP <https://www.ti.com/tool/SK-AM62-LP>`__
- Platforms Supported : AM62SIP (HS-FS, HS-SE) : `SK-AM62-SIP <https://www.ti.com/tool/SK-AM62-SIP>`__
- Platforms Supported : BeaglePlay (GP) : `BeaglePlay <https://www.ti.com/tool/BEAGL-PLAY-SBC>`__

Processor SDK 11.01.05.03
=========================
- This is the second reference release on the 2025 LTS stream with 6.12 Kernel, 2025.01 U-Boot and Yocto Scarthgap/5.0
- ATF 2.13+
- OPTEE 4.6.0
- Yocto Scarthgap/5.0
- Platforms Supported : AM62x (HS-FS, HS-SE) : `SK-AM62 <https://www.ti.com/tool/SK-AM62>`__ , `SK-AM62B <https://www.ti.com/tool/SK-AM62B>`__ , `SK-AM62B-P1 <https://www.ti.com/tool/SK-AM62B-P1>`__
- Platforms Supported : AM62x LP (HS-FS, HS-SE) : `SK-AM62-LP <https://www.ti.com/tool/SK-AM62-LP>`__
- Platforms Supported : AM62SIP (HS-FS, HS-SE) : `SK-AM62-SIP <https://www.ti.com/tool/SK-AM62-SIP>`__
- Platforms Supported : BeaglePlay (GP) : `BeaglePlay <https://www.ti.com/tool/BEAGL-PLAY-SBC>`__

Processor SDK 11.00.09.04
=========================
- This is the first reference release on the 2025 LTS stream with 6.12 Kernel, 2025.01 U-Boot and Yocto Scarthgap/5.0
- ATF 2.12+
- OPTEE 4.5.0
- Yocto Scarthgap/5.0
- Platforms Supported : AM62x (HS-FS, HS-SE) : `SK-AM62 <https://www.ti.com/tool/SK-AM62>`__ , `SK-AM62B <https://www.ti.com/tool/SK-AM62B>`__ , `SK-AM62B-P1 <https://www.ti.com/tool/SK-AM62B-P1>`__
- Platforms Supported : AM62x LP (HS-FS, HS-SE) : `SK-AM62-LP <https://www.ti.com/tool/SK-AM62-LP>`__
- Platforms Supported : BeaglePlay (GP) : `BeaglePlay <https://www.ti.com/tool/BEAGL-PLAY-SBC>`__

.. note::

    - For U-Boot builds, k3-image-gen and core-secdev-k3 are no longer needed
      as **binman** is used instead. Please refer to :ref:`U-Boot build
      instructions<Build-U-Boot-label>` for the updated steps.

    - For Linux builds, generic ``defconfig`` is used instead of custom
      fragments. Please refer to :ref:`Linux Kernel User Guide <preparing-to-build>`
      for build instructions.

.. include:: _AM62_Enable_UHS_MMCSD.rst
