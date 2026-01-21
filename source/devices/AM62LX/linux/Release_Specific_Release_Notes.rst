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

Licensing
=========

Please refer to the software manifests, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page or in the installed directory as indicated below.

-  Linux Manifest:  :file:`<PSDK_PATH>/manifest/software_manifest.htm`
-  Debian Manifest: `TI debian software manifest 11.01.16.13
   <https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-YjEeNKJJjt/11.01.16.13/software_manifest_debian_am62lxx-evm_am62lxx-evm.htm>`__

Release 11.02.08.02
===================

Released on Dec 2025

What's new
----------

**Processor SDK Linux AM62LX Release has following new features:**

  - Supported AM62Lx SR1.1 Only
  - New 2-Stage A53 Boot Flow including OPTEE
  - Low Power Mode: DeepSleep Wakeup Event - UART, GPIO, CPUFreq Framework with DFS
  - Added support for McASP async mode: independent transmit (playback) and receive (capture) clocking
  - Kernel: :ref:`DTHEv2 Crypto Accelerator <DTHEv2-Crypto-Accelerator>` OPTEE TRNG
  - Support for multiple Linux distributions, such as Yocto, Debian and Buildroot

**Key Release References:**

  - Tools: :ref:`K3conf <How-to-use-k3conf-label>`
  - U-Boot: :ref:`User and Reduced Bootmode OTP Programming  <programming-user-otp-fuses-label>`
  - U-Boot: :ref:`Key writer lite Programming <key-writer-lite-label>`
  - Kernel: :ref:`DTHEv2 Crypto Accelerator <DTHEv2-Crypto-Accelerator>`
  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Support for Wifi with M2 CC33xx cards - :ref:`How to Enable M.2-CC33xx in Linux <enable_m2cc3301>`
  - Out-of-Box experience based on LVGL (Light and Versatile Graphics Library) - :ref:`TI LVGL Demo - User Guide <TI-LVGL-Demo-User-Guide-label>`

**Component version:**

  - Kernel (Including RT) 6.12.57
  - U-Boot 2025.01
  - Toolchain GCC 13.4
  - OPTEE 4.7.0
  - ATF 2.12+
  - TIFS Firmware `v11.02.05 <https://software-dl.ti.com/tisci/esd/11_02_05/release_notes/release_notes.html>`__ (Click on the link for more information)
  - Yocto scarthgap 5.0
  - Armbian-based Debian 13 (Trixie)
  - Buildroot 2024.11.1

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
     - `ti-u-boot-2025.01 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/log/?h=ti-u-boot-2025.01>`__
     - `11.02.08 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tag/?h=11.02.08>`__
     - :ref:`Build Config <Build-U-Boot-label>`
   * - TF-A
     - `ti-master <https://github.com/TexasInstruments/arm-trusted-firmware/tree/ti-master>`__
     - `v2.12+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-bsp/trusted-firmware-a/trusted-firmware-a-ti.inc?h=11.02.08#n11>`__
     -
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.7.0+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-security/optee/optee-os-ti-version.inc?h=11.02.08#n1>`__
     - |__OPTEE_PLATFORM_FLAVOR__|
   * - Linux Firmware
     - `ti-linux-firmware <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/log/?h=ti-linux-firmware>`__
     - `11.02.08 <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tag/?h=11.02.08>`__
     -
   * - Linux Kernel
     - `ti-linux-6.12.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.12.y>`__
     - `11.02.08 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=11.02.08>`__
     - `non-RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-6.12/k3/defconfig?h=11.02.08>`__ , `RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-rt-6.12/k3/defconfig?h=11.02.08>`__
   * - meta-ti
     - `scarthgap <https://git.yoctoproject.org/meta-ti/log/?h=scarthgap>`__
     - `11.02.08 <https://git.yoctoproject.org/meta-ti/tag/?h=11.02.08>`__
     - |__SDK_BUILD_MACHINE__|
   * - meta-arago
     - `scarthgap <https://git.yoctoproject.org/meta-arago/log/?h=scarthgap>`__
     - `11.02.08 <https://git.yoctoproject.org/meta-arago/tag/?h=11.02.08>`__
     -
   * - meta-tisdk
     - `scarthgap <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/log/?h=scarthgap>`__
     - `11.02.08.02 <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/tag/?h=11.02.08.02>`__
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
     - `ti-u-boot-2025.01 <https://github.com/TexasInstruments/ti-u-boot/tree/ti-u-boot-2025.01>`__
     - `11.02.08 <https://github.com/TexasInstruments/ti-u-boot/releases/tag/11.02.08>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/ecbe405df4033fa536886336f3796705eaef7eb4/config/sources/families/include/k3_common.inc#L72>`__
   * - ATF
     - `ti-master <https://github.com/TexasInstruments/arm-trusted-firmware/tree/ti-master>`__
     - `v2.12+ <https://github.com/TexasInstruments/arm-trusted-firmware/commit/5939ceaeb664b8da5499dc4ecfa1caa7f5bcc31a>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/ecbe405df4033fa536886336f3796705eaef7eb4/config/sources/families/include/k3_common.inc#L70>`__
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.7.0+ <https://github.com/OP-TEE/optee_os/commit/a9690ae39995af36a31b7a4f446f27ea0787e3a4>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/ecbe405df4033fa536886336f3796705eaef7eb4/config/sources/families/include/k3_common.inc#L98>`__
   * - Linux Firmware
     - `ti-linux-firmware <https://github.com/TexasInstruments/ti-linux-firmware/tree/ti-linux-firmware>`__
     - `11.02.08 <https://github.com/TexasInstruments/ti-linux-firmware/releases/tag/11.02.08>`__
     - `Git Clone <https://github.com/TexasInstruments/armbian-build/blob/ecbe405df4033fa536886336f3796705eaef7eb4/config/sources/families/include/k3_common.inc#L85>`__
   * - Linux Kernel
     - `ti-linux-6.12.y <https://github.com/TexasInstruments/ti-linux-kernel/tree/ti-linux-6.12.y>`__
     - `11.02.08 <https://github.com/TexasInstruments/ti-linux-kernel/releases/tag/11.02.08>`__
     - `non-RT <https://github.com/TexasInstruments/armbian-build/blob/2025.12-release/config/kernel/linux-k3-vendor.config>`__, `RT <https://github.com/TexasInstruments/armbian-build/blob/2025.12-release/config/kernel/linux-k3-vendor-rt.config>`__
   * - Armbian Build
     - `2025.12-release <https://github.com/TexasInstruments/armbian-build/tree/2025.12-release>`__
     - `11.02.08.02 <https://github.com/TexasInstruments/armbian-build/releases/tag/11.02.08.02>`__
     - | Build: `k3_common.inc <https://github.com/TexasInstruments/armbian-build/blob/2025.12-release/config/sources/families/include/k3_common.inc>`__ + `k3.conf <https://github.com/TexasInstruments/armbian-build/blob/2025.12-release/config/sources/families/k3.conf>`__
       | Board: `TMDS62LEVM <https://github.com/TexasInstruments/armbian-build/blob/2025.12-release/config/boards/tmds62levm.conf>`__

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
     - `ti-u-boot-2025.01 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/log/?h=ti-u-boot-2025.01>`__
     - `11.02.08 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tag/?h=11.02.08>`__
     - `Build <https://github.com/TexasInstruments/buildroot-external-TI/blob/78d0a34cec662b7fd96bf7319e9c59d2b79c1df3/configs/ti_release_am62x_sk_defconfig#L60>`__
   * - ATF
     - `master <https://github.com/TexasInstruments/arm-trusted-firmware.git>`__
     - `v2.13+ <https://github.com/TexasInstruments/arm-trusted-firmware/commit/5939ceaeb664b8da5499dc4ecfa1caa7f5bcc31a>`__
     - `Build <https://github.com/TexasInstruments/buildroot-external-TI/blob/78d0a34cec662b7fd96bf7319e9c59d2b79c1df3/configs/ti_release_am62lx_evm_rt_defconfig#L39>`__
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.7.0+ <https://github.com/OP-TEE/optee_os/commit/a9690ae39995af36a31b7a4f446f27ea0787e3a4>`__
     - `Build <https://github.com/TexasInstruments/buildroot-external-TI/blob/78d0a34cec662b7fd96bf7319e9c59d2b79c1df3/configs/ti_release_am62lx_evm_rt_defconfig#L46>`__
   * - Linux Firmware
     - `ti-linux-firmware <https://github.com/TexasInstruments/ti-linux-firmware/tree/ti-linux-firmware>`__
     - `11.02.08 <https://github.com/TexasInstruments/ti-linux-firmware/releases/tag/11.02.08>`__
     - `Git Clone <https://github.com/buildroot/buildroot/blob/1a17185606161d7a03198e249c02bdc2bdc972d0/boot/ti-k3-boot-firmware/ti-k3-boot-firmware.mk#L8>`__
   * - Linux Kernel
     - `ti-linux-6.12.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.12.y>`__
     - `11.02.08 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=11.02.08>`__
     - `non-RT <https://github.com/TexasInstruments/buildroot-external-TI/blob/78d0a34cec662b7fd96bf7319e9c59d2b79c1df3/configs/ti_release_am62lx_evm_defconfig#L15C58-L15C60>`__, `RT <https://github.com/TexasInstruments/buildroot-external-TI/blob/78d0a34cec662b7fd96bf7319e9c59d2b79c1df3/configs/ti_release_am62lx_evm_rt_defconfig#L15C58-L15C60>`__
   * - Buildroot External TI
     - `main <https://github.com/TexasInstruments/buildroot-external-TI/tree/main>`__
     - `11.02.08.02 <https://github.com/TexasInstruments/buildroot-external-TI/releases/tag/11.02.08.02>`__
     - `Build <https://github.com/TexasInstruments/buildroot-external-TI/tree/main/configs>`__, `Board <https://github.com/TexasInstruments/buildroot-external-TI/tree/main/board/ti/am62lx-evm>`__
   * - Buildroot
     - `2025.08.x <https://github.com/buildroot/buildroot/tree/2025.08.x>`__
     - `2025.08.2 <https://github.com/buildroot/buildroot/releases/tag/2025.08.2>`__
     -

Issues Tracker
==============

.. note::

    - Release Specific Issues including details will be published through Software Incident Report (SIR) portal

    - Further Information can be found at `SIR Portal <https://sir.ext.ti.com/>`_


Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_SITMPUSW-174 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-174>`_","UDMA: HC/UHC channel allocation fails due to RM config mismatch with CSL defines"
   "`EXT_EP-13129 <https://sir.ext.ti.com/jira/browse/EXT_EP-13129>`_","cpsw: probe failed if CONFIG_DEBUG_FS is disabled"
   "`EXT_EP-13135 <https://sir.ext.ti.com/jira/browse/EXT_EP-13135>`_","Linux SDK docs: inconsistent TF-A git repo URL's"
   "`EXT_EP-12970 <https://sir.ext.ti.com/jira/browse/EXT_EP-12970>`_","AM6x - Sitara Socs MCASP and BCDMA issue"
   "`EXT_EP-12226 <https://sir.ext.ti.com/jira/browse/EXT_EP-12226>`_","Backport ""board: ti: common: Kconfig: add CMD_CACHE"" into TI U-Boot Tree"
   "`EXT_EP-13147 <https://sir.ext.ti.com/jira/browse/EXT_EP-13147>`_","padconfig: ST_EN bit not preserved"
   "`EXT_EP-13171 <https://sir.ext.ti.com/jira/browse/EXT_EP-13171>`_","AM62L Disable DPI when not used"
   "`EXT_EP-13172 <https://sir.ext.ti.com/jira/browse/EXT_EP-13172>`_","AM62L: RTC+DDR resume failure with dwc3_ti_resume"
   "`EXT_EP-13175 <https://sir.ext.ti.com/jira/browse/EXT_EP-13175>`_","AM62L: Suspend-Resume (RTC+DDR): eth0: failed to start"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-13124 <https://sir.ext.ti.com/jira/browse/EXT_EP-13124>`_","AM62L two stage BL booting from redundant GPMC-NAND partition"
   "`EXT_EP-12980 <https://sir.ext.ti.com/jira/browse/EXT_EP-12980>`_","AM62L: Random kernel crash observed on stress test"
   "`EXT_EP-13145 <https://sir.ext.ti.com/jira/browse/EXT_EP-13145>`_","AM62L: Network stability issues"
   "`EXT_EP-12979 <https://sir.ext.ti.com/jira/browse/EXT_EP-12979>`_","AM62L: Suspend-Resume (RTC+DDR): davinci_mdio timed out waiting for user access"

