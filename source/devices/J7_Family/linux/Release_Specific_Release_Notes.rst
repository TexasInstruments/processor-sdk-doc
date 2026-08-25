.. _release-specific-release-notes:

************************************
Release Notes
************************************
.. http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_Release_Notes

Overview
========

The **Processor Software Development Kit (Processor-SDK) for Linux**
provides a fundamental software platform for development, deployment and
execution of Linux based applications and includes the following:

-  Bootloaders, Linux Kernel & Filesystem
-  SDK installer & Prebuilt Binaries
-  Setup scripts
-  Demo applications
-  Documentation

.. ifconfig:: CONFIG_sdk in ('JACINTO')

   .. Note::
      For building some of the RTOS-based demonstrations, you should also download
      Processor SDK RTOS installer. For more information,
      refer to <PSDKRA install path>/index.html.


Licensing
=========

Please refer to the software manifest, which outlines the licensing
status for all packages included in this release. The manifest can be found on the SDK
download page or in the installed directory as indicated below. In
addition, see :ref:`Processor SDK Linux GPLv3 Disclaimer <overview-gplv3-disclaimer>`.


Documentation
=============
-  :ref:`Processor SDK Linux Software Developer's Guide <linux-index>`: Provides information on features, functions, delivery package and,
   compile tools for the Processor SDK Linux release. This also provides
   detailed information regarding software elements and software
   infrastructure to allow developers to start creating applications.
-  :ref:`Processor SDK Linux Getting Started Guide <overview-getting-started>`: Provides information on getting the software and running
   examples/demonstrations bundled in the SDK.
-  **Software Manifest**: Provides license information on software
   included in the SDK release. This document is in the release at
   ``[INSTALL-DIR]/manifest``.
-  **EVM Quick Start Guide**: Provides information on hardware setup and
   running the demonstration application that is loaded on flash. This
   document is provided as part of the EVM kit.


Supported Platforms
===================
See :ref:`here <release-specific-supported-platforms-and-versions>` for a list of supported platforms and links to more information.

Release 11.02.02
================

Released Aug 2026

.. rubric:: What's New
   :name: whats-new

Processor SDK 11.02.02 Release supports the following platforms:

  * J721E
  * J7200
  * J721S2
  * J784S4
  * J722S
  * J742S2

Processor SDK 11.02.02 Release has following features

  * Fourth 2026 LTS (Linux 6.12 and u-boot 2025.01)
  * ATF v2.13.0+
  * OPTEE 4.7.0
  * Yocto Scarthgap/5.0
  * Bug Fixes

.. _release-specific-build-information:

Build Information
=================

U-Boot
------
| Head Commit: 4ca322ca563a21cccad8c9ba65e386b9fd34dd16: TI: mmc: am654_sdhci: Fix up eMMC OTAP delay for HS200 on SR2.0
| Wed Aug 12 12:08:10 2026 +0530
| uBoot Version: 2025.01
| uBoot Description: 11.02.18

| Repo: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| uBoot Tag: 11.02.18

| Compiler Information: arm-oe-eabi-gcc (GCC) 13.4.0, aarch64-oe-linux-gcc (GCC) 13.4.0
|

.. ifconfig:: CONFIG_image_type in ('edgeai', 'adas')

   .. note::

      meta-edgeai Yocto layer contains additional patches for U-Boot `here <https://git.ti.com/cgit/edgeai/meta-edgeai/tree/recipes-bsp/u-boot?h=REL.PSDK.ANALYTICS.11.02.01.02>`__.

.. _kernel-release-notes:

Kernel
------
.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: ca77f7291a4f1c5f6927fee4e47282b03a39ebfd: UPSTREAM: PCI: j721e: Fix incorrect max_lanes for J7200
| Date:   Thu Aug 13 09:49:37 2026 +0530
| Kernel Version: 6.12.57
| Kernel Description: 11.02.18

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.02.18
| Non-RT Kernel defconfig: defconfig + ti_arm64_prune.config
| RT Kernel defconfig: defconfig + ti_rt.config + ti_arm64_prune.config

| Compiler Information: aarch64-oe-linux-gcc (GCC) 13.4.0, GNU ld (GNU Binutils) 2.42.0
|


.. ifconfig:: CONFIG_image_type in ('edgeai', 'adas')

   .. note::

      meta-edgeai Yocto layer contains additional patches for Kernel `here <https://git.ti.com/cgit/edgeai/meta-edgeai/tree/recipes-kernel/linux?h=REL.PSDK.ANALYTICS.11.02.01.02>`__.

TF-A
----
| Head Commit: e0c4d3903b382bf34f552af53e6d955fae5283ab: Merge changes from topic "xlnx_fix_gen_con_datatype" into integration
| Date : Tue Jul 1 07:01:36 2025 +0000
| Version:  2.13

| Repo: https://github.com/ARM-software/arm-trusted-firmware
| Branch: master
|

.. note::

   meta-ti Yocto layer contains additional patches for TF-A `here <https://git.ti.com/cgit/arago-project/meta-ti/tree/meta-ti-bsp/recipes-bsp/trusted-firmware-a/trusted-firmware-a?h=11.02.08>`__.

OP-TEE
------
| Head Commit: a9690ae39995af36a31b7a4f446f27ea0787e3a4: plat-k3: drivers: Add TRNG driver support in AM62L
| Date : Fri Aug 1 15:40:58 2025 +0530
| Version: 4.7.0

| Repo: https://github.com/OP-TEE/optee_os/
| Branch: master
| Tag: 4.7.0
|

.. note::

   meta-ti Yocto layer contains additional patches for OP-TEE `here <https://git.ti.com/cgit/arago-project/meta-ti/tree/meta-ti-bsp/recipes-security/optee/optee-os?h=11.02.08>`__.

ti-linux-firmware
-----------------
| Head Commit: 639e8ed77b8c51071537ec9353fdc6200371235e: ti-ipc: j721s2/j7200/j784s4/j742s2/j721e/j722s: update ipc binaries
| Date:   Mon Aug 17 17:12:08 2026 +0530

| Repo: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 11.02.18
|



Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: ef43a90c91d5a9754b2f28f09debd553fbc6a2d5: CI/CD Auto-Merger: cicd.scarthgap.202608190946
| Date:   Wed Aug 19 09:46:45 2026 -0500

| Repo: https://git.ti.com/cgit/arago-project/meta-ti
| Branch: scarthgap
| Release Tag: 11.02.18
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: 73ab0405254988a501b849d221acf5f468cb8997: libyang: Fix CVE-2026-41401
| Date:   Wed Jul 22 11:59:56 2026 -0500

| Repo: https://git.yoctoproject.org/meta-arago
| Branch: scarthgap
| Release Tag: 11.02.18
|

.. rubric:: meta-tisdk

| Head Commit: 8ccd0f212ef01517a9c92f77dfb4da0f4ee0cb65 recipes-graphics: disable emptty for AM62A
| Date: Wed Jan 28 00:33:58 2026 -0600

| Repo: https://github.com/TexasInstruments/meta-tisdk.git
| Branch: scarthgap
| Release Tag: REL.PSDK.ANALYTICS.11.02.01.02
|

.. ifconfig:: CONFIG_image_type in ('edgeai', 'adas')

   .. rubric:: meta-edgeai

   | Head Commit: 04db1a86f468b1072eaf72cb723b0d1b76a505ce tisdk-adas-image: Add edgeai-gst-plugins into ADAS_STACK
   | Date: Sat June 27 01:38:24 2026 -0500

   | Clone: git://git.ti.com/edgeai/meta-edgeai.git
   | Branch: scarthgap
   | Release Tag: REL.PSDK.ANALYTICS.11.02.01.02
   |

Issues Tracker
==============

Issues opened in previous releases that were closed on this release
-------------------------------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform"
  :widths: 15, 70, 20

  "LCPD-48208","Audio codec MCLK is set to incorrect speed on J722S EVM rev 2 and later","j722s_evm-fs,j722s_evm-se"
  "LCPD-48187","u-boot: DDR inline ECC does not cover the full memory","am62axx_sk-fs,am62dxx_evm-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am64xx-evm,am64xx_sk-fs,am68_sk-fs,am69_sk-fs,j7200-evm,j721e-sk,j721s2-evm,j742s2_evm-fs,j784s4-evm"
  "LCPD-48186","u-boot: DDR partial inline ECC support is broken","am62axx_sk-fs,am62dxx_evm-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am64xx-evm,am64xx_sk-fs,am68_sk-fs,am69_sk-fs,j7200-evm,j721e-sk,j721s2-evm,j784s4-evm"
  "LCPD-47868","When booted in attached mode (IPC does not work after s2r)","j7200-evm,j721s2-evm,j722s_evm-se,j742s2_evm-fs,j784s4-evm"
  "LCPD-46946","PCIe1 fails for specific devices on the J784S4 EVM","j784s4-evm"
  "LCPD-46929","TDA4VH: Turning off/on secondary ARM cores in parallel fails","j784s4-evm"
  "LCPD-46093","j721e: IPC with C7x fails","j721e-idk-gw,j721e-sk"

|

Issues found and closed on this release that may be applicable to prior releases
--------------------------------------------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform"
  :widths: 15, 70, 20

  "LCPD-48407","DRA821 max lane number is 2 instead of 4","j7200-evm"

|


Errata Fixes Available Before this Release
------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform", "ErrataId"
  :widths: 15, 30, 70, 60

  "LCPD-47389","USART: Erroneous clear/trigger of timeout interrupt","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2310"
  "LCPD-47381","MCAN: Message Transmit order not guaranteed from dedicated Tx Buffers configured with same Message ID","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2278"
  "LCPD-44174","Add workaround for SE in C7x boot sequence","j721s2-evm,j784s4-evm","i2437"
  "LCPD-32351","MMCSD: HS200 and SDR104 Command Timeout Window Too Small","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-hsevm,am68_sk-fs,am69_sk-fs,j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm","i2312"
  "LCPD-27886","USART: Erroneous clear/trigger of timeout interrupt","am62axx_sk-fs,am62xx-sk,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,j7200-evm,j721e-idk-gw,j784s4-evm,j784s4-hsevm","i2310"
  "LCPD-24654","MCAN: Implement workaround for errata i2279","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm","i2279"
  "LCPD-22905","UDMA: TR15 hangs if ICNT0 is less than 64 bytes","am654x-evm,j721e-idk-gw","i2234"
  "LCPD-22752","DDR: VRCG high current mode must be used during LPDDR4 CBT and Write DQ Vref Training","j7200-evm,j721e-idk-gw,j721s2-evm,j784s4-evm","i2159"
  "LCPD-22750","MSMC: Set-hazarding logic withholding RT access waiting on NRT access completion","am654x-evm,am654x-hsevm,am654x-idk,j7200-evm,j721e-idk-gw","i2116"
  "LCPD-22544","DDR: LPDDR4 should be configured to 2666 MT/S","j7200-evm","i2186"
  "LCPD-20007","VTM Temperature Monitors (TEMPSENSORs) should use a software trimming method","j721e-idk-gw","i2128"
  "LCPD-19965","i2189: OSPI PHY Controller Bug Affecting Read Transactions","am64xx-evm,am654x-idk,j7200-evm,j721e-idk-gw","i2189"
  "LCPD-19068","DSS: Disabling a layer connected to Overlay may result in synclost during the next frame","j721e-evm,j721e-evm-ivi,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm","i2097"
  "LCPD-19047","USB: Race condition while reading TRB from system memory in device mode","j721e-evm,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw","i2067"
  "LCPD-17220","U-Boot Hyperbus: Hyperflash reads limited to 125MHz max. frequency","j721e-idk-gw","i2088"
  "LCPD-16605","MMC: MMC1/2 Speed Issue","j721e-evm,j721e-evm-ivi,j721e-idk-gw","i2090"

|

Errata Fixes Available in this Release
--------------------------------------

.. csv-table::
  :header: "Record ID", "Title", "Platform", "ErrataId"
  :widths: 15, 30, 70, 60



|

Errata Rejected as Not Applicable
---------------------------------

.. csv-table::
  :header: "Record ID", "Title", "Platform", "ErrataId"
  :widths: 15, 30, 70, 60

  "LCPD-47318","DDR: Controller anomaly in setting wakeup time for low power states","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2157"
  "LCPD-47230","[Errata] Torrent lane master signals are set to 1'b0 by default","j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk","i2323"
  "LCPD-43439","J722S: ROM boot fails for large file sizes","j722s_evm-fs","i2466"
  "LCPD-34048","PCIe: AFS bit in PCIE_CORE_RP_I_PCIE_CAP_2 register is not set,","j7200-evm,j721s2-evm,j721s2_evm-fs","i2086"
  "LCPD-22715","i2232: DDR: Controller postpones more than allowed refreshes after frequency change","am62xx-sk,am62xx_sk-fs,am62xx_sk-se,j7200-evm,j721e-idk-gw,j721s2-evm,j721s2_evm-fs,j742s2_evm-fs,j784s4-evm","i2232"
  "LCPD-19988","MCU: MCU domain may hang if main domain is issued a reset","am654x-hsevm,am654x-idk,j721e-idk-gw","i2173"
  "LCPD-19812","UDMAP: UDMA transfers with ICNTs and/or src/dst addr NOT aligned to 64B fail when used in ""event trigger"" mode","j7200-evm,j721e-idk-gw","i2163"
  "LCPD-19517","R5FSS: The same interrupt cannot be nested back-2-back within another interrupt","j721e-evm,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw","i2162"
  "LCPD-16350","DSS: Frame Buffer Flip/Mirror Feature Using RGB24/BGR24 Packed Format can Result in Pixel Corruption","j721e-idk-gw","i2039"

|

Open Erratum
------------

.. csv-table::
  :header: "Record ID", "Title", "Platform", "ErrataId"
  :widths: 15, 30, 70, 60

  "LCPD-48098","USB: 2.0 compliance receive sensitivity test limitation","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2134"
  "LCPD-48096","MCAN: Message Transmit order not guaranteed from dedicated Tx Buffers configured with same Message ID","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2278"
  "LCPD-47858","USB: 2.0 compliance receive sensitivity test limitation","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2134"
  "LCPD-47355","DDR: Entry and exit to/from Deep Sleep low-power state can cause PHY internal clock misalignment","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2166"
  "LCPD-47295","USB: 2.0 compliance receive sensitivity test limitation","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2134"

|

U-Boot Known Issues
-------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform", "Workaround"
  :widths: 15, 30, 70, 30

  "LCPD-48474","Boot modes: Ethernet with kernel is failing in 12.01.00.05","am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am68_sk-fs,am69_sk-fs,j722s_evm-fs",""
  "LCPD-48076","J784S4: Autogen output clk-data.c and dev-data.c do not match U-Boot","j784s4-evm,j784s4-hsevm",""
  "LCPD-48075","J721S2: Autogen output clk-data.c and dev-data.c do not match U-Boot","j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se",""
  "LCPD-48074","J7200: Autogen output clk-data.c and dev-data.c do not match U-Boot","j7200-evm,j7200-hsevm,j7200_evm-fs",""
  "LCPD-48073","J721E: Autogen output clk-data.c and dev-data.c do not match U-Boot","j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk",""
  "LCPD-47304","Autogen output clk-data.c and dev-data.c do not match U-Boot (Jacinto devices)","j7200-evm,j721e-evm-ivi,j721s2-evm",""
  "LCPD-46031","DFU: SPL-DFU boot support is failing in 12.01.00.05","am62axx_sk-fs,am62dxx_evm-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am64xx-hsevm,j721e-idk-gw,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
  "LCPD-46016","DFU: Update bootloaders in RAW eMMC via DFU is failing in 12.01.00.05","am62axx_sk-fs,am62dxx_evm-fs,am62xx_lp_sk-fs,am62xx_sk-fs,j7200-evm,j742s2_evm-fs,j784s4-evm",""
  "LCPD-45251","U-Boot: Enable CONFIG_TIMER","j7200-evm",""
  "LCPD-44857","j722s_evm-fs: RC-08: Failure: UBOOT : MSC boot shall be supported","j722s_evm-fs",""
  "LCPD-42041","Upstream: j721e: Initial U-boot prints taking around 10s","j721e-idk-gw",""
  "LCPD-38569","j722s: Unable to communicate with MCU R5 and Main R5 when FW loaded from U-Boot","j722s_evm-fs",""
  "LCPD-34106","SPL: USB DFU Boot fails on J721S2 EVM on upstream U-Boot(also ti-u-boot-2023.04)","j721s2-evm,j721s2_evm-fs",""
  "LCPD-24108","U-Boot: TISCI config ring fail traces seen in OSPI boot mode on J721E","j721e-evm,j721e-evm-ivi,j721e-idk-gw",""
  "LCPD-17789","UBOOT J7: Could not see UFS device by scsi scan","j721e-idk-gw",""

|

Linux Known Issues
------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform", "Workaround"
   :widths: 5, 10, 70, 35

  "LCPD-48716","J722S: NFS BOOT Fails while running ETHFW due to RPMsg Response Timeout","j722s_evm-fs,j722s_evm-se",""
  "LCPD-48669","Forced PWM bit not set in PMIC-B in j7200","j7200-evm",""
  "LCPD-48630","Linux SDK Documentation doesn't capture MCAN Performance Data","am62xx_sk-fs,am64xx_sk-fs,am654x-evm,j7200-evm,j7200_evm-fs,j721s2-evm,j721s2_evm-fs,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm",""
  "LCPD-48587","TDA4VH: Turning off/on secondary ARM cores in parallel fails","j784s4-evm",""
  "LCPD-48482","USBHOST_S_FUNC_SUPERSPEED_HUB_SUPERSPEED_0001 is failing in 12.01.00.05","j721s2-evm",""
  "LCPD-48480","USBHOST_S_FUNC_HIGHSPEED_HUB_FULLSPEED_0001 is failing in 12.01.00.05","j722s_evm-fs",""
  "LCPD-48478","USBDEV_superspeed_serial_enumerate is failing in 12.01.00.05","j721s2-evm,j742s2_evm-fs",""
  "LCPD-48477","USBDEV_superspeed_msc_slave_perf is failing in 12.01.00.05","j721s2-evm,j742s2_evm-fs",""
  "LCPD-48476","USBDEV_highspeed_multi_performance_msc is failing in 12.01.00.05","am62axx_sk-fs,j7200-evm,j742s2_evm-fs",""
  "LCPD-48470","Ethernet tests failing in 12.1","am62axx_sk-fs,am62dxx_evm-fs,am62lxx_evm-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am64xx-hsevm,j721e-idk-gw",""
  "LCPD-48394","USBHOST_XS_FUNC_AUDIO_LOOPBACK_ACCESSTYPE_NONINTER_01 is failing in 12.01.00.05","j7200-evm,j721e-idk-gw,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
  "LCPD-48393","USBDEV_highspeed_msc_enumeration is failing in 12.01.00.05","am62axx_sk-fs,am62dxx_evm-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xxsip_sk-fs,j7200-evm,j721e-idk-gw,j722s_evm-fs,j784s4-evm",""
  "LCPD-48330","S2R: Kernel panic during resume from suspend","j7200-evm",""
  "LCPD-48308","DDR memory wasted when inline ECC enabled","am62axx_sk-fs,am62lxx_evm-fs,am62pxx_sk-fs,am62xx_sk-fs,am64xx_sk-fs,j7200-evm,j7200_evm-fs,j721e-sk,j721s2_evm-fs,j742s2_evm-fs",""
  "LCPD-48212","USBHOST_S_FUNC_HIGHSPEED_HUB_MULTI_SPEED_0001 is failing in 12.01.00.05","am62xxsip_sk-fs,j722s_evm-fs",""
  "LCPD-48211","CICD: j721s2 : ALSA_S_FUNC_CAP_SMPRT_32000 failure","j721s2-evm",""
  "LCPD-48166","DP_S_FUNC_PLAYBACK_3840x2160 tests failing inconsistently","j721e-idk-gw",""
  "LCPD-48164","J7 docs refering to instructions for Sitara devices","j7200-evm,j721e-idk-gw,j721s2-evm,j784s4-evm",""
  "LCPD-48097","MCAN: Implement workaround for errata i2279","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
  "LCPD-48096","MCAN: Message Transmit order not guaranteed from dedicated Tx Buffers configured with same Message ID","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","Workaround #1: After writing the Tx messages with same Message ID to the Message RAM, request transmission of all these message concurrently by single write access to TXBAR. Make sure none of these messages have a pending Tx request before making the concurrent request. Workaround #2: Use the Tx FIFO instead of dedicated Tx Buffers (set bit MCAN_TXBC[30] TFQM = 0 to use Tx FIFO) for the transmission of several messages with the same Message ID in a specific order."
  "LCPD-47981","NFS BOOT Fails while at CORE LINUX FUCNTIONALITY level while running ETHFW standalone code","j722s_evm-fs",""
  "LCPD-47970","CICD: eMMC Failures","j784s4-evm",""
  "LCPD-47969","CICD: OSPI Failures","j721e-idk-gw,j784s4-evm",""
  "LCPD-47964","CICD: J7200: OSPI functional test failures","j7200-evm",""
  "LCPD-47963","CICD: J7200: Hyperflash functional test failures","j7200-evm",""
  "LCPD-47960","CICD: USB Failures: Multiple patterns and platforms","am335x-evm,am62axx_sk-fs,am62dxx_evm-fs,am64xx-hsevm,j7200-evm,j7200_evm-fs,j721e-idk-gw,j721e-sk,j742s2_evm-fs",""
  "LCPD-47957","CICD: Connectivity tests failing or not run","am62lxx_evm-fs,am62xx_lp_sk-fs,am62xxsip_sk-fs,am68_sk-fs,am69_sk-fs,j742s2_evm-fs",""
  "LCPD-47955","CICD: ETH_CPSW2g_IET_4 not running","am62axx_sk-fs,am62lxx_evm-fs,am62xx_lp_sk-fs,am62xxsip_sk-fs,j742s2_evm-fs",""
  "LCPD-47918","Kernel crash due to CPSW Tx timeout","j722s_evm-fs",""
  "LCPD-47889","J721e: Linux: USB 3.0 devices are not getting enumerated","j721e-idk-gw",""
  "LCPD-47875","PCIe Suspend-Resume results in kernel panic when EP connected to PCIe0 on J784S4","j784s4-evm",""
  "LCPD-47799","BCDMA RX_IGNORE_LONG setting in RX CHAN CFG register doesnt work","j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","Workaround: RX_IGNORE_LONG is unusable, so remote endpoint such as PDMA should close packet by sending EOP to match TR boundary (PDMA X*Y*Z should match TR ICNT0*ICNT1*ICNT2*ICNT3) If infinite stream is desired (PDMA Z=0) then switch to PKTDMA and use Single Buffer Mode"
  "LCPD-47763","Defects for J7AEN 11.02 release","j722s_evm-fs,j722s_evm-se",""
  "LCPD-47749","NFS boot fails when EthFW is enabled on MCU2_0 R5F core due to CPSW Proxy Client driver circular dependency","j722s_evm-fs,j722s_evm-se",""
  "LCPD-47715","CPSW: Linux: Convert networking drivers as a loadable module","am62xx_sk-fs,j721e-idk-gw",""
  "LCPD-47355","DDR: Entry and exit to/from Deep Sleep low-power state can cause PHY internal clock misalignment","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","If using software initiated low-power mode by writing to LP_CMD in the DENALI_CTL_132 register, ensure that once entry into low-power mode has been acknowledged, wait for a minimum of 160 DDR clock cycles before requesting an exit from low-power mode. Another option is to use workaround list below. If using PSC to disable DDR interface, ensure that once disabling of DDR interface has been acknowledged, wait for a minimum of 160 DDR clock cycles before sending a request to enable it. Another option is to use workaround list below. If using controller’s automatic mechanism for low power entry/exit using LP_AUTO_ENTRY_EN in the DENALI_CTL_141 register, use the workaround listed below. Workaround: Ensure that DDR PHY does not enter Deep Sleep low-power state. This can be ensured by programming the value of PHY_LP_WAKEUP[3:0] in the DENALI_PHY_1318 register is greater than the values of all the following thresholds in DDR controller registers. LPI_CTRL_IDLE_WAKEUP_FN, LPI_PD_WAKEUP_FN, LPI_SR_SHORT_WAKEUP_FN, LPI_SR_LONG_WAKEUP_FN, LPI_SRPD_SHORT_WAKEUP_FN, LPI_SRPD_LONG_WAKEUP_FN, LPI_SR_LONG_MCCLK_GATE_WAKEUP_FN, LPI_SRPD_LONG_MCCLK_GATE_WAKEUP_FN, and LPI_TIMER_WAKEUP_FN where FN = F0, F1, and F2 for different frequency set points."
  "LCPD-47295","USB: 2.0 compliance receive sensitivity test limitation","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","Workaround for J7ES_SR1.0 and J7ES_SR1.1: It may be necessary to perform the receive sensitivity test manually by breaking it into two parts. The first part begins the same as described above, with the initial amplitude set to a value less than 100 mV, verify the DUT NAK’d all packets while increasing the amplitude until it reaches 100 mV. The other part of the test begins by setting the amplitude above 150 mV, verify the DUT NAK’d no packets while decreasing the amplitude until it reaches 150 mV. This confirms the squelch threshold lies between 100 mV and 150 mV as required by the USB specification without sweeping the amplitude through the squelch threshold which can lock the PHY. Workaround for J7VCL_SR1.0, J7VCL_SR2.0, and J7AEP_SR1.0 and AM64x_SR1.0: Enable both of the following hardware workarounds. Set cdr_eb_wr_reset bit (bit 7) to 1’b1 in UTMI_REG28 register present in USB*_PHY2 region. Set phyrst_a_enable bit (bit 0) to 1’b1 in PHYRST_CFG register present in USB*_MMR_MMRVBP_USBSS_CMN region. Please note that phyrst_a_value (bits 12:8) in PHYRST_CFG register should be retained at default value of 0xE."
  "LCPD-47270","UMS support at uboot is failing in 12.01.00.05","j742s2_evm-fs,j784s4-evm",""
  "LCPD-47268","USBHOST_S_FUNC_DD_RW_10M is failing in 12.01.00.05","am64xx-hsevm,am69_sk-fs,j784s4-evm",""
  "LCPD-47267","ETH_CPSW2g_PTP_Switch is failing in 12.01.00.05","j784s4-evm",""
  "LCPD-47265","CPSWng_Native testcase are NR","am68_sk-fs,am69_sk-fs,j7200-evm,j721e-idk-gw,j721s2-evm,j784s4-evm",""
  "LCPD-47251","USBDEV_superspeed_cdc_ping is failing in 12.01.00.05","j721e-idk-gw,j721s2-evm,j742s2_evm-fs",""
  "LCPD-47243","Manual Test: Linux: CPSW Proxy Client shall support dynamic VLAN is failing in 12.00.00.07","am62pxx_sk-fs,j7200-evm,j721e-idk-gw,j784s4-evm",""
  "LCPD-47237","ETH_XS_FUNC_RGMII_RXID_CPSWnG_NATIVE is failing in 12.00.00.07","am62xxsip_sk-fs,j742s2_evm-fs",""
  "LCPD-47234","Linux: Virtual Client Handling for CPSW reset/recovery is failing in 12.00.00.07","am62axx_sk-fs,am62dxx_evm-fs,j7200-evm,j721e-idk-gw,j742s2_evm-fs,j784s4-evm",""
  "LCPD-47223","TEST: RC-07: CPSW: Add test automation support for packet classification based on ALE engine","j722s_evm-fs",""
  "LCPD-47220","TEST: RC-07: CPSW: Capability gap for testing XDP tests on j722s","j722s_evm-fs",""
  "LCPD-47185","DFU: Update bootloaders in OSPI via DFU is failing in 12.01.00.05","am62axx_sk-fs,am62dxx_evm-fs,am62xx_lp_sk-fs,am62xx_sk-fs,j7200-evm,j742s2_evm-fs,j784s4-evm",""
  "LCPD-46614","Cannot suspend after booting eth-fw in IPC-only mode on J7200 due to ESM failure","j7200-evm",""
  "LCPD-46418","Crypto: cbc and ecb sa2ul self tests fails on few platforms","am62axx_sk-fs,am62pxx_sk-fs,j722s_evm-fs",""
  "LCPD-46208","EHPWM: Period and dutycycle not getting set initially.","j784s4-evm",""
  "LCPD-46191","Linux: Virtual Client Handling for CPSW reset/recovery is failing in 12.00.00.07","j742s2_evm-fs",""
  "LCPD-46187","j784s4-evm: RC-08: TESTGAP: Linux: CPSW Proxy Client shall support dynamic VLA...","j784s4-evm",""
  "LCPD-46186","j784s4-evm: RC-08: TESTGAP: TDA4VH: PCIe boot support","j784s4-evm",""
  "LCPD-46185","Linux: Virtual Client Handling for CPSW reset/recovery is failing in 12.00.00.07","j784s4-evm",""
  "LCPD-46184","j7200-evm: RC-08: TESTGAP: Linux: CPSW Proxy Client shall support dynamic VLA...","j7200-evm",""
  "LCPD-46182","Linux: Virtual Client Handling for CPSW reset/recovery is failing in 12.00.00.07","j7200-evm",""
  "LCPD-46179","CPSW XDP tests are failing in 12.01.00.05","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,j7200-evm,j721e-idk-gw,j722s_evm-fs",""
  "LCPD-46150","ETH_CPSW2g_PTP is failing in 12.01.00.05","j784s4-evm",""
  "LCPD-46142","Low latency audio support failing","j721e-idk-gw",""
  "LCPD-46140","Kernel test case for supporting SDR104 speed mode in SD card fails","j721e-idk-gw",""
  "LCPD-46120","cpuloadgen testcase fails to run on all cores","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
  "LCPD-46099","Test gap: Wake-up from DeepSleep","am62dxx_evm-fs,am62lxx_evm-fs,am64xx-hsevm,am68_sk-fs,am69_sk-fs,j721e-idk-gw,j742s2_evm-fs,j784s4-evm",""
  "LCPD-46058","USBDEV_fullspeed_cdc_ping is failing in 12.01.00.05","am62xxsip_sk-fs,j7200-evm,j722s_evm-fs",""
  "LCPD-46057","USBDEV_fullspeed_msc_func is failing in 12.01.00.05","am62xxsip_sk-fs,j722s_evm-fs,j742s2_evm-fs",""
  "LCPD-46056","USBDEV_highspeed_cdc_ping_zlp is failing in 12.01.00.05","j722s_evm-fs",""
  "LCPD-46054","USBDEV_highspeed_cdc_ncm_ping is failing in 12.01.00.05","j722s_evm-fs,j784s4-evm",""
  "LCPD-46052","USBDEV_highspeed_cdc_ping is failing in 12.01.00.05","j722s_evm-fs",""
  "LCPD-46050","USBDEV_fullspeed_cdc_ncm_ping is failing in 12.01.00.05","am62axx_sk-fs,am62xxsip_sk-fs,j721e-idk-gw,j721s2-evm,j722s_evm-fs",""
  "LCPD-46049","USBDEV_fullspeed_serial_enumerate is failing in 12.01.00.05","j722s_evm-fs",""
  "LCPD-46047","USBDEV_highspeed_serial_enumerate is failing in 12.01.00.05","j722s_evm-fs",""
  "LCPD-46045","ETH_CPSW2g_PTP_Switch is failing in 12.00.00.07","am62axx_sk-fs,am62xxsip_sk-fs,j7200-evm,j721e-idk-gw,j722s_evm-fs,j784s4-evm",""
  "LCPD-46044","USBDEV_highspeed_msc_slave_perf is failing in 12.01.00.05","j722s_evm-fs",""
  "LCPD-46043","CPSW: Linux: Update the CBS test case capability to run it between DUT and TEE","j722s_evm-fs",""
  "LCPD-46026","ETH-CPSW2G_USXGMII_MODE is failing in 12.01.00.05","j784s4-evm",""
  "LCPD-45969","J722S: Changing DPHY parent refclk breaks USB","am62pxx_sk-fs,j722s_evm-fs",""
  "LCPD-45963","OPTEE xtest failures","am62pxx_sk-fs,am64xx-hsevm,am64xx-hssk,j722s_evm-fs",""
  "LCPD-45607","McSPI performance improvements","j7200-evm,j721s2-evm",""
  "LCPD-45340","J784S4 Support USB3.0 LANE SWAP functionality","j721s2_evm-fs,j784s4-evm",""
  "LCPD-45253","c7x ipc failure on linux loading remote core firmwares","j722s_evm-fs",""
  "LCPD-45212","Linux kernel crash if R5F firmware is stopped while rpmsg char simple is running","j7200-evm,j721e-evm-ivi,j721s2-evm,j784s4-evm",""
  "LCPD-44947","J784S4 PCIe legacy interrupt removed","am69_sk-fs,j784s4-evm",""
  "LCPD-44854","Test: Ethernet slave peripheral boot failure","am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am69_sk-fs,j722s_evm-fs",""
  "LCPD-44846","USBDEV_superspeed_cdc_ncm_ping is failing in 12.01.00.05","j721e-idk-gw,j721s2-evm,j742s2_evm-fs",""
  "LCPD-44845","USBDEV_superspeed_cdc_enumerate is failing in 12.01.00.05","j721e-idk-gw,j721s2-evm,j742s2_evm-fs",""
  "LCPD-44841","PCI_S_FUNC_CDNS_MSIX is failing in 12.01.00.05","j722s_evm-fs",""
  "LCPD-44834","MMC card is not getting probed corrected on J721E","j721e-idk-gw",""
  "LCPD-44505","WDT_RTI: Make the watchdog timeout configurable","j722s_evm-fs,j722s_evm-se",""
  "LCPD-43476","Linux: USB: UMS tests is failing","am68_sk-fs,am69_sk-fs,j721e-idk-gw,j721s2-evm,j742s2_evm-fs,j784s4-evm",""
  "LCPD-43407","IPC Graceful Shutdown on C7x cores","j721e-idk-gw,j721s2-evm,j722s_evm-fs,j784s4-evm",""
  "LCPD-43304","CSI RX driver does not consider byterperline parameter in set format","am62axx_sk-fs,am62axx_sk-se,j721e-evm-ivi,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm",""
  "LCPD-42843","remoteproc/k3-dsp: PDK IPC echo test binaries fails to do IPC in remoteproc mode on second run","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j784s4-evm",""
  "LCPD-42557","MSMC: A53, A72 Coherent Streaming Writes have minor sub-optimal performance","am654x-idk,j7200-evm,j721e-idk-gw,j721s2-evm,j784s4-evm","See description"
  "LCPD-42294","[uboot-eMMC]: Incorrect OTAP Delay for J721E SR2.0","j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk",""
  "LCPD-42099","UFS failure in Farm on J742s2/J784s4 device","j742s2_evm-fs,j784s4-evm",""
  "LCPD-41066","CSI outputs black images when DMA is set to ASEL 15","am62pxx_sk-fs,j722s_evm-fs",""
  "LCPD-41044","ARM toolchain used in Yocto build keeps on updating every release","am62axx_sk-fs,am62axx_sk-se,am68_sk-fs,am68_sk-se,am69_sk-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j742s2_evm-fs,j784s4-evm,j784s4-hsevm",""
  "LCPD-38898","Hyperflash Unstability issue","j7200-evm",""
  "LCPD-38756","AM64x: Linux hangs on repetitive probe/removal of gadget zero","am64xx-evm,am64xx_sk-fs,am68_sk-fs,am68_sk-se,am69_sk-fs,j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm",""
  "LCPD-38558","Unable to gracefully shutdown both cores in R5 Cluster","j7200-evm,j721e-idk-gw,j721s2-evm,j784s4-evm",""
  "LCPD-38311","Power off test case failing","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
  "LCPD-38267","J722S: tiboot3.bin / R5 SPL within size limit fails to boot","j722s_evm-fs",""
  "LCPD-38070","Misbehavior of CPSW due to ALE entries overwritten by driver","j721e-hsevm",""
  "LCPD-37953","NFS boot stress test causing FWL exception","j721s2-evm,j784s4-evm",""
  "LCPD-37705","crypto perf failure","am68_sk-fs,j7200-evm,j722s_evm-fs",""
  "LCPD-37702","J722S : Crypto perf (ipsec) test failed","j722s_evm-fs",""
  "LCPD-37690","UFS test case failing due test setup issue","j721e-idk-gw,j784s4-evm",""
  "LCPD-37463","We don't have SMMU kernel options related to VFIO should be NOIOMMU set","am64xx-hsevm,j721e-idk-gw",""
  "LCPD-37314","NFS in UBOOT on J722S EVM (HS-FS) Fails","j722s_evm-fs",""
  "LCPD-36952","Add support for J721S2 PG 1.1 in uboot","j721s2-evm",""
  "LCPD-36863","OPTEE/ATF are not protected by c7x","am68_sk-fs,j7200-hsevm,j721e-hsevm",""
  "LCPD-36794","j7200-evm: eth firmware floods network with dhcp packets","j7200-evm",""
  "LCPD-36474","J721s2 incorrect autogen generated data","j721s2-evm",""
  "LCPD-36386","IPSEC connection failure on automated setup in testfarm","j721e-idk-gw",""
  "LCPD-34712","OSPI: 2-byte address is not supported in PHY DDR mode","j7200-evm,j721e-idk-gw,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","For compatible OSPI memories that have programmable address byte settings, set the amount of address bytes required from 2 to 4 on the flash. This may involve sending a specific command to change address bytes and/or writing a configuration register on the flash. Once done, update the amount of address bytes sent in the controller settings from 2 to 4. For compatible OSPI memories that only support 2-byte addressing and cannot be re-programmed, PHY DDR mode will not be compatible with that memory. Alternative modes include: PHY SDR mode TAP (no-PHY) DDR mode TAP (no-PHY) SDR mode"
  "LCPD-32544","J7200: OSPI Phy calibration fails intermittently","j7200-evm",""
  "LCPD-28501","Mic input is very noisy on j721e platform","j721e-sk",""
  "LCPD-28250","J721S2: QSPI Write corrupted when the first operation after powerup is erase","j721s2-evm,j721s2_evm-fs",""
  "LCPD-24715","CONFIG_GPIO_HOG is not set in the uboot config file","j721s2-evm",""
  "LCPD-22926","PCIe: The SerDes PCIe Reference Clock Output can exceed the 5.0 GT/s Data Rate RMS jitter limit","j7200-hsevm,j7200_evm-fs",""
  "LCPD-22925","PCIe: SerDes Reference Clock Output does not comply to Vcross, Rise-Fall Matching, and Edge Rate limits","j7200-evm,j7200-hsevm,j7200_evm-fs,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se",""
  "LCPD-22895","CBASS Null Error Interrupt Not Masked By Enable Register","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se",""
  "LCPD-22339","PCI-E USBCARD, ETHCARD don't indicate 2-lane support with lspci","j7200-evm,j721e-idk-gw",""
  "LCPD-20653","Test: Legacy: ltp: kernel syscall tests fail","am335x-evm,am43xx-gpevm,am654x-idk,j721e-idk-gw,j722s_evm-fs",""
  "LCPD-19739","AM65 shutdown error","am654x-idk,j7200-evm",""
  "LCPD-19499","Kernel: OSPI write throughput is less than 1MB/s","j7200-evm,j7200-hsevm",""
  "LCPD-19497","J7200: CPSW2g: interface goes up and down sporadically","j7200-evm","Seen only on very few EVMs. No workaround."
  "LCPD-19084","Few SD cards not enumerating in Kernel with Alpha EVM","j721e-idk-gw",""
  "LCPD-18790","eMMC tests failed on J7 rev E2 EVM","j721e-idk-gw",""
  "LCPD-17172","Uboot USBhost: Sandisk Extreme USB 3.0 msc stick could not be detected at second time","j721e-idk-gw",""
  "LCPD-17171","Uboot dhcp occasionally failed","j721e-idk-gw",""
  "LCPD-16640","PCIe RC: GIC ITS misbehaves when more than 4 devices use it simultaneously","j721e-idk-gw",""
  "LCPD-16396","J721E: RC: Unsupported request in configuration completion packets results in an abort","j721e-evm,j721e-evm-ivi,j721e-idk-gw","Workaround for Multifunction: Configure all the physical functions supported by the endpoint. For configuring all the 6 functions of PCIe controller instance '1' in J721E, the following can be used. mount -t configfs none /sys/kernel/config; cd /sys/kernel/config/pci_ep/; mkdir functions/pci_epf_test/func1; echo 0x104c > functions/pci_epf_test/func1/vendorid; echo 0xb00d > functions/pci_epf_test/func1/deviceid; echo 1 > functions/pci_epf_test/func1/msi_interrupts; echo 16 > functions/pci_epf_test/func1/msix_interrupts; ln -s functions/pci_epf_test/func1 controllers/d800000.pcie-ep/; mkdir functions/pci_epf_test/func2; echo 0x104c > functions/pci_epf_test/func2/vendorid; echo 0xb00d > functions/pci_epf_test/func2/deviceid; echo 1 > functions/pci_epf_test/func2/msi_interrupts; echo 16 > functions/pci_epf_test/func2/msix_interrupts; ln -s functions/pci_epf_test/func2 controllers/d800000.pcie-ep/; mkdir functions/pci_epf_test/func3; echo 0x104c > functions/pci_epf_test/func3/vendorid; echo 0xb00d > functions/pci_epf_test/func3/deviceid; echo 1 > functions/pci_epf_test/func3/msi_interrupts; echo 16 > functions/pci_epf_test/func3/msix_interrupts; ln -s functions/pci_epf_test/func3 controllers/d800000.pcie-ep/; mkdir functions/pci_epf_test/func4; echo 0x104c > functions/pci_epf_test/func4/vendorid; echo 0xb00d > functions/pci_epf_test/func4/deviceid; echo 1 > functions/pci_epf_test/func4/msi_interrupts; echo 16 > functions/pci_epf_test/func4/msix_interrupts; ln -s functions/pci_epf_test/func4 controllers/d800000.pcie-ep/; mkdir functions/pci_epf_test/func5; echo 0x104c > functions/pci_epf_test/func5/vendorid; echo 0xb00d > functions/pci_epf_test/func5/deviceid; echo 1 > functions/pci_epf_test/func5/msi_interrupts; echo 16 > functions/pci_epf_test/func5/msix_interrupts; ln -s functions/pci_epf_test/func5 controllers/d800000.pcie-ep/; mkdir functions/pci_epf_test/func6; echo 0x104c > functions/pci_epf_test/func6/vendorid; echo 0xb00d > functions/pci_epf_test/func6/deviceid; echo 1 > functions/pci_epf_test/func6/msi_interrupts; echo 16 > functions/pci_epf_test/func6/msix_interrupts; ln -s functions/pci_epf_test/func6 controllers/d800000.pcie-ep/; echo 1 > controllers/d800000.pcie-ep/start; echo 1 > /sys/bus/pci/devices/0000:00:00.0/remove; echo 1 > /sys/bus/pci/rescan; Workaround for switch card: No workarounds available."
  "LCPD-9981","Some LTP's memory management tests fail due to low amount of free memory","j721e-vlab,omapl138-lcdk",""

|

Issues closed in system firmware in this release
-------------------------------------------------

System firmware Known Issues
------------------------------

Change Requests
===============

SDK features descoped from 11.02 release
----------------------------------------
.. csv-table::
   :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
   :widths: 20, 90, 90, 20, 20

   JACINTOREQ-9115, "Linux DSS driver to support frame freeze detect", "All J7 Platforms", 11.02.00, "Dropped"
   JACINTOREQ-8931, "J784S4 firewalling support", "J784S4,J742S2", 11.02.00, "Future Release"
   JACINTOREQ-9146, "Low power support on HS-SE/J784S4, R5 as suspend master", "J784S4,J7200", 11.02.00, 11.02.01

SDK features descoped from 11.01 release
----------------------------------------
.. csv-table::
   :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
   :widths: 20, 90, 90, 20, 20

   JACINTOREQ-7915, "J7: Support for Kexec/Kdump in Linux", "All J7 Platforms", 11.01.00, 12.00.00
   JACINTOREQ-7596, "[Linux]: Support for Headless display using QT", "J722S,J7ES,J784S4,J721S2", 11.01.00, "Future Release"

SDK features descoped from 11.00 release
----------------------------------------
.. csv-table::
  :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
  :widths: 20, 90, 90, 20, 20

  JACINTOREQ-3987, "Linux SDK shall support ADC: 12-bit, 4MSPS analog to digital converter", "J784S4", 11.00.00, Descoped
  JACINTOREQ-5770, "U-Boot: support remoteproc load of HSM M4F core", "J722S", 11.00.00, 11.01.00

SDK features descoped from 10.01 release
----------------------------------------
.. csv-table::
  :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
  :widths: 20, 90, 90, 20, 20

  JACINTOREQ-5776 ,Linux Driver for GPMC - FPGA connection, "J722S", 10.01.00 , Dropped
  JACINTOREQ-5138 ,"Linux SDK shall support SA2UL: HMAC using MD5, SHA1, SHA2-224, SHA2-256 and SHA2-512", "J784S4, J721E, J721S2, J7200, J722S", 10.00.00 , 11.01.00
  JACINTOREQ-5529 ,Power Management support, "J722S", 10.01.00 ,11.01.00

SDK features descoped from 10.00 release
----------------------------------------
.. csv-table::
  :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
  :widths: 20, 90, 90, 20, 20

  JACINTOREQ-7514 ,Linux SDK shall support MSMC: Security Firewall, "J784S4", 10.00.00 ,10.01.00
  JACINTOREQ-5042 ,Linux SDK shall support cpufreq [opp] DFS, "J784S4, J721E, J721S2, J7200, J722S", 10.00.00 ,Dropped
  JACINTOREQ-4121 ,Support to boot MCU R5 1_1 in split mode, "J784S4, J721E, J721S2, J7200", 10.00.00 ,10.01.00

SDK features descoped from 9.2 release
--------------------------------------
.. csv-table::
  :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
  :widths: 20, 90, 90, 20, 20

  JACINTOREQ-3970 ,Linux SDK shall support MSMC: Security Firewall, "J784S4", 09.02.00 ,10.00.00
  JACINTOREQ-5042 ,AM69/J784S4 Linux SDK shall support cpufreq [opp], "AM69, J784S4", 09.02.00 ,10.00.00

SDK features scoped in 9.1 release
----------------------------------
.. csv-table::
  :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
  :widths: 20, 90, 90, 20, 20

   JACINTOREQ-3761 ,Linux SDK shall support RTI: Watchdog support J721S2, "J721S2", 09.02.00 ,09.01.00
   JACINTOREQ-3981 ,Linux SDK shall support RTI: Watchdog support J784S4, "J784S4", 09.02.00 ,09.01.00

SDK features descoped from 9.1 release
--------------------------------------
.. csv-table::
  :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
  :widths: 20, 90, 90, 20, 20

  JACINTOREQ-3970 ,Linux SDK shall support MSMC: Security Firewall, "J784S4", 09.01.00 ,09.02.00
  JACINTOREQ-3920 ,"Linux SDK shall support SA2UL: HMAC using MD5, SHA1, SHA2-224, SHA2-256 and SHA2-512", "J784S4", 09.01.00 ,09.02.00

SDK features descoped from 9.0 release
--------------------------------------
.. csv-table::
  :header: "ID", "Head Line", "Platform", "Original Fix Version", "New Fix Version"
  :widths: 20, 90, 90, 20, 20

   JACINTOREQ-3598 ,Jacinto Device firewalling support, "J7200, J721e, J721s2, J784s4", 09.00.00 ,09.01.00

SDK features descoped from 8.6 release
--------------------------------------
.. csv-table::
  :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
  :widths: 20, 90, 90, 20, 20

   JACINTOREQ-5338 ,Jacinto PSDK 8.6 AEP/AHP industrial APL pull-in impact, "J721e, J7200, J721S2 , J784S4", 08.06.00 ,09.00.00


SDK features descoped from 8.5 release
--------------------------------------
.. csv-table::
  :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
  :widths: 20, 90, 90, 20, 20

   JACINTOREQ-5060, Jacinto networking requirements - CR to 8.6, "J721S2, J784S4", 08.05.00, 08.06.00
   JACINTOREQ-4991, "Jacinto Baseport, Graphics, Multimedia CR to 8.6", "J721S2, J784S4", 08.05.00, 08.06.00
   JACINTOREQ-4934, CSI Capture Automated Testing for J7AEP, J721S2, 08.05.00, 08.06.00
   JACINTOREQ-4928, J7AEP Multimedia Scope Modify, J721S2, 08.05.00, 08.06.00
   JACINTOREQ-5001, Configurable Buffering Descope, J784S4, 08.05.00, None
   JACINTOREQ-4993, Descope GLBenchmark, J784S4, 08.05.00, None
   JACINTOREQ-4927, J7AHP Graphics Scope Modify, J784S4, 08.05.00, 08.06.00

SDK features scope change for 8.5 release
-----------------------------------------
.. csv-table::
   :header: "ID", "Headline", "Platform"
   :widths: 40, 60, 60

   JACINTOREQ-4994 , Video Codec Memory Optimization Scope Change, J721e

SDK features descoped from 8.4 release
--------------------------------------
.. csv-table::
   :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
   :widths: 20, 90, 90, 20, 20

   JACINTOREQ-4930 ,k3conf Doc and Test Modify, J721e, 08.04.00 ,08.05.00
   JACINTOREQ-4905 ,J7AEP Graphics Scope Modify, J721s2, 08.04.00 ,08.05.00/08.06.00
   JACINTOREQ-4898 ,SERDES: PCIe + USB schedule update, J721s2, 08.04.00 ,08.05.00
   JACINTOREQ-4864 ,4k Resolution Scope change, J721s2, 08.04.00 ,08.05.00
   JACINTOREQ-4854 ,McASP Scope Change, J721s2, 08.04.00 ,08.05.00
   JACINTOREQ-4930 ,k3conf Doc and Test Modify, J721s2, 08.04.00 ,08.05.00

SDK features descoped from 8.0 release
--------------------------------------
.. csv-table::
   :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
   :widths: 20, 90, 90, 20, 20

    JACINTOREQ-1559 ,Linux H264 decoder support, J721e, 08.00.00 ,08.01.00
    JACINTOREQ-1485 ,Linux writeback pipeline support , J721e, 08.00.00 ,None
    JACINTOREQ-1444 ,Vision apps inclusion in yocto build  , J721e, 08.00.00 ,None


SDK features present in 7.0 that were descoped in 7.1
-----------------------------------------------------
.. csv-table::
   :header: "Feature", "Comments", "Platform"
   :widths: 40, 60, 60

    HS support,Restored in 7.3, J721e
    SPL/Uboot boot modes restricted to SD card boot mode,Restored in 7.3, J721e
    1s Linux boot, , "J721e"
    Descope for support of native H264 encode/decode,Use R5F based driver with OpenVX as interface.  H.264 decoder support restored in 7.3, J721e
    GPU compression, , J712e
    SA2UL driver optimization, , J721e
    Display Sharing,Display sharing demo available in SDK v6.1, J721e
    Virtualization (Jailhouse hypervisor/IPC virtualization/CPSW9G virtualization),Does not affect 3P virtualization solutions. Basic Jailhouse demo can be seen in SDK 7.0, J721e


Installation and Usage
======================

The :ref:`Software Developer's Guide <linux-index>` provides instructions on how to setup your Linux development environment, install the SDK and start your development. It also includes User's Guides for various Example Applications.

|

Host Support
============

For the specific supported hosts for current SDK, see :ref:`this page <how-to-build-a-ubuntu-linux-host-under-vmware>`.
