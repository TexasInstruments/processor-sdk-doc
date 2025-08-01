***************
Migration Guide
***************

.. rubric:: Overview

This page covers migration information for applications built on top
of the Processor SDK Linux AM62A.

Processor SDK Linux AM62A 11.xx Releases
========================================

Processor SDK 11.01.07.05
=========================
- This is the first reference release on the 2025 LTS stream with 6.12 Kernel, 2025.01 U-Boot and Yocto Scarthgap/5.0
- ATF 2.13+
- OPTEE 4.6.0
- Yocto Scarthgap/5.0
- Platforms Supported : AM62A (HS-FS, HS-SE) : `SK-AM62A-LP <https://www.ti.com/tool/SK-AM62A-LP>`__


.. note::

    - For U-Boot builds, k3-image-gen and core-secdev-k3 are no longer needed
      as **binman** is used instead. Please refer to :ref:`U-Boot build
      instructions<Build-U-Boot-label>` for the updated steps.

    - For Linux builds, generic ``defconfig`` is used instead of custom
      fragments. Please refer to `linux users guide
      <../../../linux/Foundational_Components_Kernel_Users_Guide.html#preparing-to-build>`__
      for build instructions.
