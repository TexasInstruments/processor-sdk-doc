.. _release-specific-migration-guide:

###############
Migration Guide
###############

.. rubric:: Overview

This page covers migration information for applications built on top
of the Processor SDK Linux AM64X.

****************************************
Processor SDK Linux AM64X 10.xx Releases
****************************************

Processor SDK 10.01.10.04
=========================
- This is the final release on the 2024 LTS stream 6.6 kernel, 2024.04 U-Boot and Yocto Scarthgap/5.0
- ATF 2.11+
- OPTEE 4.4.0
- Yocto Scarthgap/5.0
- Platforms Supported : AM64x 2.0 (HS-FS) : `EVM <https://www.ti.com/tool/TMDS64EVM>`__ , `SK <https://www.ti.com/tool/SK-AM64B>`__


Processor SDK 10.00.07.04
=========================
- This is the first release on the 2024 LTS stream 6.6 kernel, 2024.04 U-Boot and Yocto Scarthgap/5.0
- ATF 2.10+
- OPTEE 4.2.0
- Yocto Scarthgap/5.0
- Platforms Supported : AM64x 2.0 (HS-FS) : `EVM <https://www.ti.com/tool/TMDS64EVM>`__ , `SK <https://www.ti.com/tool/SK-AM64B>`__

.. note::

    - For U-Boot builds, k3-image-gen and core-secdev-k3 are no longer needed
      as **binman** is used instead. Please refer to :ref:`U-Boot build
      instructions<Build-U-Boot-label>` for the updated steps.

    - For Linux builds, generic ``defconfig`` is used instead of custom
      fragments. Please refer to `linux users guide
      <../../../linux/Foundational_Components_Kernel_Users_Guide.html#preparing-to-build>`__
      for build instructions.

.. include:: _Release_Specific_PLL.rst
