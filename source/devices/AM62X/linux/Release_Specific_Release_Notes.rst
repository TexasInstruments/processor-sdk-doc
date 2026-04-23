.. _Release-note-label:

#############
Release Notes
#############

Overview
========

The **Processor Software Development Kit (Processor SDK)** is a unified software platform for TI embedded processors
providing easy setup and fast out-of-the-box access to benchmarks and demos.  All releases of Processor SDK are
consistent across TI’s broad portfolio, allowing developers to seamlessly reuse and develop software across devices.
Developing a scalable platform solutions has never been easier than with the Processor SDK and TI’s embedded processor
solutions.

To simplify the end user experience, Processor SDK Linux AM62x installer provides everything needed as discussed below
to create the embedded system from “scratch” :

-  Platform/board-support software and configuration files for Linux
-  U-Boot and Kernel sources and configuration files
-  An ARM cross-compiling toolchain as well as other host binaries and components
-  A Yocto/OE compliant filesystem and sources for example applications
-  A variety of scripts and Makefiles to automate certain tasks
-  Other components needed to build an embedded system that don’t fit neatly into one of the above buckets
-  Reference Examples, benchmarks

This release supports High Security - Field Securable (HS-FS) devices. For migration guide and other info, refer :ref:`HS-Migration-Guide`

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
-  Debian Manifest:

   -  `AM62x 12.00.00.07.04
      <https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-PvdSyIiioq/12.00.00.07.04/software_manifest_debian_sk-am62b.html>`__
   -  `AM62x-SIP 12.00.00.07.04
      <https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-PvdSyIiioq/12.00.00.07.04/software_manifest_debian_sk-am62-sip_sk-am62-sip.htm>`__

Release 12.00.00.07.04
======================

Released on Apr 2026

What's new
----------

**Processor SDK Linux AM62X Release has following new features:**

  - First 2026 LTS Reference Release Including RT combined branch model
  - Important Bug Fixes on top of Processor SDK 11.02.08.02 Release
  - Review Issue Tracker Section for the new fixes.
  - Security: ATF and OPTEE memory firewall for isolation from Linux
  - Security: Yocto reference for LUKS2 root filesystem encryption with fTPM key management
  - Power: Reduced power consumption using MCU Only low power mode by 13%

**Key Release References:**

  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Falcon mode through R5 SPL :ref:`U-Boot Falcon Mode <U-Boot-Falcon-Mode>`
  - Out-of-Box TI Apps Launcher Application with Qt6 Framework - :ref:`TI Apps Launcher <TI-Apps-Launcher-User-Guide-label>`
  - Support for multiple GUI frameworks (Flutter and Slint) - :ref:`GUI Frameworks <GUI_Frameworks_User_Guide>`
  - Snagfactory Support - :ref:`Snagfactory Tool <Flash-via-Fastboot>`
  - Support for M2 CC33xx cards on Debian - `How to Enable M.2-CC33x1 in Linux <https://software-dl.ti.com/processor-sdk-linux/esd/AM62X/10_01_10_04_Debian/exports/docs/linux/How_to_Guides/Target/How_To_Enable_M2CC3301_in_linux.html>`__
  - How to Enable PRU RPMsg - `Read FAQ <https://e2e.ti.com/support/processors-group/processors/f/791/t/1494495>`__
  - How standby power mode works - :ref:`CPUIdle Documentation <cpuidle-guide>`

**Component version:**

  - Kernel 6.18.13
  - U-Boot 2026.01
  - Toolchain GCC 15.2
  - ATF 2.14+
  - OPTEE 4.9.0+
  - TIFS Firmware `v12.00.02 <https://software-dl.ti.com/tisci/esd/12_00_02/release_notes/release_notes.html>`__ (Click on the link for more information)
  - Yocto Master
  - Graphics DDK 25.3
  - DM Firmware 12.00.00.09

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
     - `master <https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/+/refs/heads/master>`__
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
   :widths: 15, 30, 30, 32

   * - Component
     - Branch Info
     - Tag Info
     - Config Info
   * - U-Boot
     - `ti-u-boot-2026.01 <https://github.com/TexasInstruments/ti-u-boot/tree/ti-u-boot-2026.01>`__
     - `12.00.00.07 <https://github.com/TexasInstruments/ti-u-boot/releases/tag/12.00.00.07>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/9f81d13cc640f9ad876faf2a906a0eda11a6bffd/config/sources/families/include/k3_common.inc#L76>`__
   * - TF-A
     - `master <https://github.com/ARM-Software/arm-trusted-firmware/tree/master>`__
     - `v2.14+ <https://github.com/ARM-software/arm-trusted-firmware/commit/76500ceaeefcda967d8a1f4e30bb04f9fe0425a2>`__
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
       | Board: `SK-AM62B <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/boards/sk-am62b.conf>`__, `SK-AM62-LP <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/boards/sk-am62-lp.conf>`__, `SK-AM62-SIP <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/boards/sk-am62-sip.conf>`__

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
     - `Build <https://github.com/TexasInstruments/buildroot-external-TI/blob/main/configs/ti_release_am62x_sk_defconfig#L60>`__
   * - ATF
     - `master <https://github.com/ARM-Software/arm-trusted-firmware/tree/master>`__
     - `v2.14+ <https://github.com/ARM-software/arm-trusted-firmware/commit/76500ceaeefcda967d8a1f4e30bb04f9fe0425a2>`__
     - `Build <https://github.com/TexasInstruments/buildroot-external-TI/blob/main/configs/ti_release_am62x_sk_defconfig#L40>`__
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.9.0+ <https://github.com/OP-TEE/optee_os/commit/f2a7ad0638aeff5243593b33cc56ad064cae7615>`__
     - `Build <https://github.com/TexasInstruments/buildroot-external-TI/blob/main/configs/ti_release_am62x_sk_defconfig#L47>`__
   * - Linux Firmware
     - `ti-linux-firmware <https://github.com/TexasInstruments/ti-linux-firmware/tree/ti-linux-firmware>`__
     - `12.00.00.07 <https://github.com/TexasInstruments/ti-linux-firmware/releases/tag/12.00.00.07>`__
     - `Git Clone <https://github.com/buildroot/buildroot/blob/1a17185606161d7a03198e249c02bdc2bdc972d0/boot/ti-k3-boot-firmware/ti-k3-boot-firmware.mk#L8>`__
   * - Linux Kernel
     - `ti-linux-6.18.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.18.y>`__
     - `12.00.00.07 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=12.00.00.07>`__
     - `non-RT <https://github.com/TexasInstruments/buildroot-external-TI/blob/main/configs/ti_release_am62x_sk_defconfig#L15>`__, `RT <https://github.com/TexasInstruments/buildroot-external-TI/blob/main/configs/ti_release_am62x_sk_rt_defconfig#L15>`__
   * - Buildroot External TI
     - `main <https://github.com/TexasInstruments/buildroot-external-TI/tree/main>`__
     - `12.00.00.07.04 <https://github.com/TexasInstruments/buildroot-external-TI/releases/tag/12.00.00.07.04>`__
     - `Build <https://github.com/TexasInstruments/buildroot-external-TI/tree/main/configs>`__, `Board <https://github.com/TexasInstruments/buildroot-external-TI/tree/main/board/ti/am62x-sk>`__
   * - Buildroot
     - `2026.02.x <https://github.com/buildroot/buildroot/tree/2026.02.x>`__
     - `2026.02 <https://github.com/buildroot/buildroot/releases/tag/2026.02>`__
     -

Issues Tracker
==============

.. note::

    - Release Specific Issues including details will be published through Software Incident Report (SIR) portal

    - Further Information can be found at `SIR Portal <https://sir.ext.ti.com/>`_

Errata Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-13303 <https://sir.ext.ti.com/jira/browse/EXT_EP-13303>`_","Kernel: MMCSD HS200 Write Failures"
   "`EXT_EP-12124 <https://sir.ext.ti.com/jira/browse/EXT_EP-12124>`_","BCDMA: RX Channel can lockup in certain scenarios"
   "`EXT_EP-12128 <https://sir.ext.ti.com/jira/browse/EXT_EP-12128>`_","USB2 PHY locks up due to short suspend"
   "`EXT_EP-12114 <https://sir.ext.ti.com/jira/browse/EXT_EP-12114>`_","MMCSD: HS200 and SDR104 Command Timeout Window Too Small"
   "`EXT_EP-12125 <https://sir.ext.ti.com/jira/browse/EXT_EP-12125>`_","i2327: RTC: Hardware wakeup event limitation"
   "`EXT_EP-12123 <https://sir.ext.ti.com/jira/browse/EXT_EP-12123>`_","USART: Erroneous clear/trigger of timeout interrupt"

Errata Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-13304 <https://sir.ext.ti.com/jira/browse/EXT_EP-13304>`_","U-Boot: MMCSD HS200 Write Failures"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-13314 <https://sir.ext.ti.com/jira/browse/EXT_EP-13314>`_","AM62Lx Linux SDK documentation on CPSW XDP points to PRU-ICSSG XDP"
   "`EXT_EP-13305 <https://sir.ext.ti.com/jira/browse/EXT_EP-13305>`_","OPTEE build fails with the steps mentioned in the documentation"
   "`EXT_EP-13142 <https://sir.ext.ti.com/jira/browse/EXT_EP-13142>`_","R5 SPL fails to boot A53 SPL from eMMC backup boot with primary boot configured to eMMC alternate boot"
   "`EXT_EP-13316 <https://sir.ext.ti.com/jira/browse/EXT_EP-13316>`_","Board fails to resume after multiple iterations of MCU Only LPM"
   "`EXT_EP-13321 <https://sir.ext.ti.com/jira/browse/EXT_EP-13321>`_","gstreamer 1.26.9: v4l2src format negotiation fails with capsfilter constraints"
   "`EXT_EP-13317 <https://sir.ext.ti.com/jira/browse/EXT_EP-13317>`_","Mailbox timeout for TI SCI commands"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-13125 <https://sir.ext.ti.com/jira/browse/EXT_EP-13125>`_","incorrect pinmux config of MMC_CLK pin"
   "`EXT_EP-13309 <https://sir.ext.ti.com/jira/browse/EXT_EP-13309>`_","U-Boot binman does not have the provision of SWREV for Board Configurations"
   "`EXT_EP-13311 <https://sir.ext.ti.com/jira/browse/EXT_EP-13311>`_","byte loss in multiple uart external loopback test simultaneously"
   "`EXT_EP-12818 <https://sir.ext.ti.com/jira/browse/EXT_EP-12818>`_","PRU RPMsg swaps which message is sent to which core"

