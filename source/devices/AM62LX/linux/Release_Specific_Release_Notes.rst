.. _Release-note-label:

#############
Release Notes
#############

Overview
========

The **Processor Software Development Kit (Processor SDK)** is a unified software platform for TI embedded processors
providing easy setup and fast out-of-the-box access to benchmarks and demos. All releases of Processor SDK are
consistent across TI’s broad portfolio, allowing developers to seamlessly reuse and develop software across devices.
Developing a scalable platform solutions has never been easier than with the Processor SDK and TI’s embedded processor
solutions.

To simplify the user experience, Processor SDK Linux AM62L installer provides everything needed as discussed below
to create the embedded system from “scratch” :

-  Platform/board-support software and configuration files for Linux
-  U-Boot and Kernel sources and configuration files
-  An ARM cross-compiling toolchain as well as other host binaries and components
-  A Yocto/OE compliant filesystem and sources for example applications
-  A variety of scripts and Makefiles to automate certain tasks
-  Other components needed to build an embedded system that don’t fit neatly into one of the above buckets
-  Reference Examples, benchmarks

This release supports High Security - Field Securable (HS-FS) devices.

Release versioning scheme
=========================

Processor SDK releases follow the 5-duplet versioning scheme ``YY.RR.EE.CC.SS``, where:

- ``YY`` - Yearly baseline. Increments with each new LTS baseline.
- ``RR`` - Release index within the yearly baseline. Each yearly baseline includes many stable releases.
- ``EE`` - Extended release index within a stable baseline.
- ``CC`` - Release Candidate for common foundational BSP components such as Linux, U-Boot, ATF, OPTEE, Firmware and OE manifest including meta-ti, meta-arago.
- ``SS`` - SDK Release identifier for Distro layers (Yocto meta-tisdk, Armbian, Buildroot) with OOB Demos and Installers.

Licensing
=========

Please refer to the software manifests, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page or in the installed directory as indicated below.

-  Linux Manifest:  :file:`<PSDK_PATH>/manifest/software_manifest.htm`
-  Debian Manifest: `AM62Lx 12.00.00.07.04
   <https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-YjEeNKJJjt/12.00.00.07.04/software_manifest_debian_tmds62levm_tmds62levm.htm>`__

Software Bill of Materials (SBOM)
=================================

|__SDK_FULL_NAME__| releases include Software Bill of Materials (SBOM) files in SPDX 3.0
format for Yocto and CycloneDX 1.6 format for Buildroot. SBOMs for all released artifacts
are bundled into a single archive and can be found on the |__SDK_DOWNLOAD_URL__|.
For more refer :ref:`Working with SBOM <how-to-work-with-sbom>`.

Release 12.00.00.07.04
======================

Released on Apr 2026

What's new
----------

**Processor SDK Linux AM62LX Release has following new features:**

  - First 2026 LTS Reference Release Including RT combined branch model
  - Uboot: :ref:`A53 SPL Falcon boot <U-Boot-Falcon-Mode>`
  - Important Bug Fixes on top of Processor SDK 11.02.08.02 Release.
  - Review Issue Tracker Section for the new fixes.
  - Support for multiple Linux distributions, such as Yocto, Debian and Buildroot
  - OPTEE: Hardware-backed secure key storage via RPMB with PKCS#11 interface
  - Security: ATF, OPTEE and RNG memory firewall for isolation from Linux
  - Security: Yocto reference for LUKS2 root filesystem encryption with fTPM key management
  - Secure boot: Support for U-boot FIT image signing and verification

**Key Release References:**

  - Tools: :ref:`K3conf <How-to-use-k3conf-label>`
  - U-Boot: :ref:`User and Reduced Bootmode OTP Programming  <programming-user-otp-fuses-label>`
  - U-Boot: :ref:`Key writer lite Programming <key-writer-lite-label>`
  - Kernel: :ref:`DTHEv2 Crypto Accelerator <DTHEv2-Crypto-Accelerator>`
  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Support for Wifi with M2 CC33xx cards - :ref:`How to Enable M.2-CC33xx in Linux <enable_m2cc3301>`
  - Out-of-Box experience based on LVGL (Light and Versatile Graphics Library) - :ref:`TI LVGL Demo - User Guide <TI-LVGL-Demo-User-Guide-label>`

**Component version:**

  - Kernel (Including RT) 6.18.13
  - U-Boot 2026.01
  - Toolchain GCC 15.2
  - OPTEE 4.9.0+
  - ATF 2.14+
  - TIFS Firmware `v12.00.02 <https://software-dl.ti.com/tisci/esd/12_00_02/release_notes/release_notes.html>`__ (Click on the link for more information)
  - Yocto Master
  - Armbian-based Debian 13 (Trixie)
  - Buildroot 2026.02

.. _release-specific-build-information:

Build Information
=================

Arago (Yocto/OE)
----------------

.. list-table::
   :header-rows: 1
   :widths: 15, 30, 30, 30

   * - Component
     - Branch Info
     - Tag Info
     - Config Info
   * - U-Boot
     - `ti-u-boot-2026.01 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/log/?h=ti-u-boot-2026.01>`__
     - `12.00.00.07 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tag/?h=12.00.00.07>`__
     - :ref:`Build Config <Build-U-Boot-label>`
   * - TF-A
     - `ti-tfa-2.14.y <https://github.com/TexasInstruments/arm-trusted-firmware/tree/ti-tfa-2.14.y>`__
     - `v2.14+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-bsp/trusted-firmware-a/trusted-firmware-a-ti.inc?h=12.00.00.07#n5>`__
     -
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.9.0+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-security/optee/optee-os-ti-version.inc?h=12.00.00.07#n1>`__
     - |__OPTEE_PLATFORM_FLAVOR__|
   * - Linux Firmware
     - `ti-linux-firmware <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/log/?h=ti-linux-firmware>`__
     - `12.00.00.07 <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tag/?h=12.00.00.07>`__
     -
   * - Linux Kernel
     - `ti-linux-6.18.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.18.y>`__
     - `12.00.00.07 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=12.00.00.07>`__
     - `non-RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-6.18/k3/defconfig?h=12.00.00.07>`__ , `RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-rt-6.18/k3/defconfig?h=12.00.00.07>`__
   * - meta-ti
     - `master <https://git.yoctoproject.org/meta-ti/log/?h=master>`__
     - `12.00.00.07 <https://git.yoctoproject.org/meta-ti/tag/?h=12.00.00.07>`__
     - |__SDK_BUILD_MACHINE__|
   * - meta-arago
     - `master <https://git.yoctoproject.org/meta-arago/log/?h=master>`__
     - `12.00.00.07 <https://git.yoctoproject.org/meta-arago/tag/?h=12.00.00.07>`__
     -
   * - meta-tisdk
     - `master <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/log/?h=scarthgap>`__
     - `12.00.00.07.04 <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/tag/?h=12.00.00.07.04>`__
     -

Debian (Armbian)
----------------

.. list-table::
   :header-rows: 1
   :widths: 15, 30, 30, 30

   * - Component
     - Branch Info
     - Tag Info
     - Config Info
   * - U-Boot
     - `ti-u-boot-2026.01 <https://github.com/TexasInstruments/ti-u-boot/tree/ti-u-boot-2026.01>`__
     - `12.00.00.07 <https://github.com/TexasInstruments/ti-u-boot/releases/tag/12.00.00.07>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/9f81d13cc640f9ad876faf2a906a0eda11a6bffd/config/sources/families/include/k3_common.inc#L76>`__
   * - TF-A
     - `ti-tfa-2.14.y <https://github.com/TexasInstruments/arm-trusted-firmware/tree/ti-tfa-2.14.y>`__
     - `v2.14+ <https://github.com/TexasInstruments/arm-trusted-firmware/commit/d203b8453905178252094416448de009931087e0>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/9f81d13cc640f9ad876faf2a906a0eda11a6bffd/config/sources/families/include/k3_common.inc#L74>`__
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.9.0+ <https://github.com/OP-TEE/optee_os/commit/f2a7ad0638aeff5243593b33cc56ad064cae7615>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/9f81d13cc640f9ad876faf2a906a0eda11a6bffd/config/sources/families/include/k3_common.inc#L102>`__
   * - Linux Firmware
     - `ti-linux-firmware <https://github.com/TexasInstruments/ti-linux-firmware/tree/ti-linux-firmware>`__
     - `12.00.00.07 <https://github.com/TexasInstruments/ti-linux-firmware/releases/tag/12.00.00.07>`__
     - `Git Clone <https://github.com/TexasInstruments/armbian-build/blob/9f81d13cc640f9ad876faf2a906a0eda11a6bffd/config/sources/families/include/k3_common.inc#L89>`__
   * - Linux Kernel
     - `ti-linux-6.18.y <https://github.com/TexasInstruments/ti-linux-kernel/tree/ti-linux-6.18.y>`__
     - `12.00.00.07 <https://github.com/TexasInstruments/ti-linux-kernel/releases/tag/12.00.00.07>`__
     - `non-RT <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/kernel/linux-k3-vendor.config>`__, `RT <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/kernel/linux-k3-vendor-rt.config>`__
   * - Armbian Build
     - `2026.04-release <https://github.com/TexasInstruments/armbian-build/tree/2026.04-release>`__
     - `12.00.00.07.04 <https://github.com/TexasInstruments/armbian-build/releases/tag/12.00.00.07.04>`__
     - | Build: `k3_common.inc <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/sources/families/include/k3_common.inc>`__ + `k3.conf <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/sources/families/k3.conf>`__
       | Board: `TMDS62LEVM <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/boards/tmds62levm.conf>`__

Buildroot (Buildroot External TI)
---------------------------------

.. list-table::
   :header-rows: 1
   :widths: 15, 30, 30, 30

   * - Component
     - Branch Info
     - Tag Info
     - Config Info
   * - U-Boot
     - `ti-u-boot-2026.01 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/log/?h=ti-u-boot-2026.01>`__
     - `12.00.00.07 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tag/?h=12.00.00.07>`__
     - `Build <https://github.com/TexasInstruments/buildroot-external-TI/blob/main/configs/ti_release_am62lx_evm_defconfig#L55>`__
   * - ATF
     - `ti-tfa-2.14.y <https://github.com/TexasInstruments/arm-trusted-firmware/tree/ti-tfa-2.14.y>`__
     - `v2.14+ <https://github.com/TexasInstruments/arm-trusted-firmware/commit/d203b8453905178252094416448de009931087e0>`__
     - `Build <https://github.com/TexasInstruments/buildroot-external-TI/blob/main/configs/ti_release_am62lx_evm_defconfig#L40>`__
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.9.0+ <https://github.com/OP-TEE/optee_os/commit/f2a7ad0638aeff5243593b33cc56ad064cae7615>`__
     - `Build <https://github.com/TexasInstruments/buildroot-external-TI/blob/main/configs/ti_release_am62lx_evm_defconfig#L46>`__
   * - Linux Firmware
     - `ti-linux-firmware <https://github.com/TexasInstruments/ti-linux-firmware/tree/ti-linux-firmware>`__
     - `12.00.00.07 <https://github.com/TexasInstruments/ti-linux-firmware/releases/tag/12.00.00.07>`__
     - `Git Clone <https://github.com/buildroot/buildroot/blob/1a17185606161d7a03198e249c02bdc2bdc972d0/boot/ti-k3-boot-firmware/ti-k3-boot-firmware.mk#L8>`__
   * - Linux Kernel
     - `ti-linux-6.18.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.18.y>`__
     - `12.00.00.07 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=12.00.00.07>`__
     - `non-RT <https://github.com/TexasInstruments/buildroot-external-TI/blob/main/configs/ti_release_am62lx_evm_defconfig#L15>`__, `RT <https://github.com/TexasInstruments/buildroot-external-TI/blob/main/configs/ti_release_am62lx_evm_rt_defconfig#L15>`__
   * - Buildroot External TI
     - `main <https://github.com/TexasInstruments/buildroot-external-TI/tree/main>`__
     - `12.00.00.07.04 <https://github.com/TexasInstruments/buildroot-external-TI/releases/tag/12.00.00.07.04>`__
     - `Build <https://github.com/TexasInstruments/buildroot-external-TI/tree/main/configs>`__, `Board <https://github.com/TexasInstruments/buildroot-external-TI/tree/main/board/ti/am62lx-evm>`__
   * - Buildroot
     - `2026.02.x <https://github.com/buildroot/buildroot/tree/2026.02.x>`__
     - `2026.02 <https://github.com/buildroot/buildroot/releases/tag/2026.02>`__
     -

Issues Tracker
==============

.. note::

    - Release Specific Issues including details will be published through Software Incident Report (SIR) portal

    - Further Information can be found at `SIR Portal <https://sir.ext.ti.com/>`_

Errata Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-13304 <https://sir.ext.ti.com/jira/browse/EXT_EP-13304>`_","U-Boot: MMCSD HS200 Write Failures"

Errata Closed
-------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-13303 <https://sir.ext.ti.com/jira/browse/EXT_EP-13303>`_","Kernel: MMCSD HS200 Write Failures"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-13314 <https://sir.ext.ti.com/jira/browse/EXT_EP-13314>`_","AM62Lx Linux SDK documentation on CPSW XDP points to PRU-ICSSG XDP"
   "`EXT_EP-13315 <https://sir.ext.ti.com/jira/browse/EXT_EP-13315>`_","U-Boot: Enable caches for A53 SPL AM62l"
   "`EXT_EP-13145 <https://sir.ext.ti.com/jira/browse/EXT_EP-13145>`_","AM62L: Network stability issues"
   "`EXT_EP-12979 <https://sir.ext.ti.com/jira/browse/EXT_EP-12979>`_","AM62L: Suspend-Resume (RTC+DDR): davinci_mdio timed out waiting for user access"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-13319 <https://sir.ext.ti.com/jira/browse/EXT_EP-13319>`_","[AM62L OSPI NOR] Fix OSPI NOR Flash random corruption in IO"
   "`EXT_EP-12980 <https://sir.ext.ti.com/jira/browse/EXT_EP-12980>`_","AM62L: Random kernel crash observed on stress test"
   "`EXT_EP-13124 <https://sir.ext.ti.com/jira/browse/EXT_EP-13124>`_","AM62L two stage BL booting from redundant GPMC-NAND partition"

