###############
Migration Guide
###############

.. rubric:: Overview

This page covers migration information for applications built on top
of the Processor SDK Linux AM64X.

****************************************
Processor SDK Linux AM64X 12.xx Releases
****************************************

Processor SDK 12.00.00.07.04
============================
- This is the first reference release on the 2026 LTS stream with 6.18 Kernel, 2026.01 U-Boot
- ATF 2.14+
- OPTEE 4.9.0+
- Yocto Master
- Platforms Supported : AM64x 2.0 (HS-FS) : `EVM <https://www.ti.com/tool/TMDS64EVM>`__ , `SK <https://www.ti.com/tool/SK-AM64B>`__

.. note::

    - For U-Boot builds, k3-image-gen and core-secdev-k3 are no longer needed
      as **binman** is used instead. Please refer to :ref:`U-Boot build
      instructions<Build-U-Boot-label>` for the updated steps.

    - For Linux builds, generic ``defconfig`` is used instead of custom
      fragments. Please refer to `linux users guide
      <../../../linux/Foundational_Components_Kernel_Users_Guide.html#preparing-to-build>`__
      for build instructions.
