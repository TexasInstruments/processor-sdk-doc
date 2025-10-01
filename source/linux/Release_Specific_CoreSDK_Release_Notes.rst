************************************
Release Notes
************************************

Overview
========

The **Processor-CoreSDK for Linux**
provides a fundamental software platform for development, deployment and
execution of Linux based applications and includes the following:

  * Bootloaders and Filesystems.
  * Prebuilt Binaries.
  * Detailed Release Notes.

Licensing
=========

Please see software manifest, which outlines the licensing
status for all packages included in the prebuilt binaries location.


Release 11.01
=============

Released July 2025, October 2025 ( For AM62Lx SR1.1, AM62Px SR 1.2)

.. rubric:: What's New
   :name: whats-new

**Processor SDK 11.01 Sitara Release supports the following platforms**
  * tag: 11.01.16
       * AM62L SR1.1 (HS-FS, HS-SE), AM62Px 1.1,1.2 (HS-FS, HS-SE)
  * tag: 11.01.07
       * AM62A (HS-FS, HS-SE)
  * tag: 11.01.05
       * AM62Px 1.0,1.1 (HS-FS, HS-SE)
       * AM62x ( GP, HS-FS, HS-SE)
       * AM62x LP (HS-FS, HS-SE)
       * AM62SIP (HS-FS, HS-SE)
       * AM64x 2.0 (HS-FS)
       * AM62D (HS-FS)

.. _release-specific-build-information:

Release Tag Information
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 15, 30, 30, 30

   * - Component
     - Branch Info
     - Tag Info
     - Config Info
   * - U-Boot
     - `ti-u-boot-2025.01 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/log/?h=ti-u-boot-2025.01>`__
     - `11.01.16 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tag/?h=11.01.16>`__
     - `Board Configs <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/configs?h=11.01.16>`__
   * - TF-A
     - AM62Lx `ti-master <https://github.com/TexasInstruments/arm-trusted-firmware/tree/ti-master>`__ , All other K3 `master <https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/+/refs/heads/master>`__
     - AM62Lx `v2.12+ <https://github.com/TexasInstruments/arm-trusted-firmware/blob/ti-master/Makefile#L10>`__, All other K3 `v2.13 <https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/+/refs/tags/v2.13/Makefile#10>`__
     -
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.7.0+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-security/optee/optee-os-ti-version.inc?h=11.01.16#n1>`__
     - 
   * - Linux Kernel
     - `ti-linux-6.12.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.12.y>`__
     - `11.01.16 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=11.01.16>`__
     - `non-RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-6.12/k3/defconfig?h=11.01.16>`__ , `RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-rt-6.12/k3/defconfig?h=11.01.16>`__
   * - meta-ti
     - `scarthgap <https://git.yoctoproject.org/meta-ti/log/?h=scarthgap>`__
     - `11.01.16 <https://git.yoctoproject.org/meta-ti/tag/?h=11.01.16>`__
     - `Board Configs <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/conf/machine?h=11.01.16>`__
   * - meta-arago
     - `scarthgap <https://git.yoctoproject.org/meta-arago/log/?h=scarthgap>`__
     - `11.01.16 <https://git.yoctoproject.org/meta-arago/tag/?h=11.01.16>`__
     -
