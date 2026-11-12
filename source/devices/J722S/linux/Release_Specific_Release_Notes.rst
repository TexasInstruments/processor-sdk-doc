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

Released Oct 2026

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

  * Fifth 2025 LTS (Linux 6.12 and u-boot 2025.01)
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

      meta-edgeai Yocto layer contains additional patches for Kernel `here <https://git.ti.com/cgit/edgeai/meta-edgeai/tree/recipes-kernel/linux?h=REL.PSDK.ANALYTICS.11.02.02.07>`__.

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
| Release Tag: REL.PSDK.ANALYTICS.11.02.02.07
|

.. ifconfig:: CONFIG_image_type in ('edgeai', 'adas')

   .. rubric:: meta-edgeai

   | Head Commit: 32a1b0832dd7f545cd88808419916be71b7b35fa ti-vision-apps: J722S: Bump up to REL.PSDK.ANALYTICS.11.02.02.07
   | Date: Wed Oct 07 13:57:25 2026 -0500

   | Clone: git://git.ti.com/edgeai/meta-edgeai.git
   | Branch: scarthgap
   | Release Tag: REL.PSDK.ANALYTICS.11.02.02.07
   |

Issues Tracker
==============

Issues opened in previous releases that were closed on this release
-------------------------------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform"
  :widths: 15, 70, 20

  "LCPD-48208","Audio codec MCLK is set to incorrect speed on J722S EVM rev 2 and later","j722s_evm-fs,j722s_evm-se"
  "LCPD-48085","Wave5 Decoder Test Failing Because File not found","j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm"
  "LCPD-47868","When booted in attached mode (IPC does not work after s2r)","j7200-evm,j721s2-evm,j722s_evm-se,j742s2_evm-fs,j784s4-evm"

|

Issues found and closed on this release that may be applicable to prior releases
--------------------------------------------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform"
  :widths: 15, 70, 20


|

Errata Fixes Available Before this Release
------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform", "ErrataId"
  :widths: 15, 30, 70, 60

  "LCPD-47654","DDR: Valid VRef range must be defined during LPDDR4 Command Bus Training","j7200-evm,j7200-hsevm,j721e-idk-gw,j721s2-hsevm,j721s2_evm-fs,j722s_evm-fs,j722s_evm-se,j784s4-evm,j784s4-hsevm","i2160"
  "LCPD-47389","USART: Erroneous clear/trigger of timeout interrupt","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2310"
  "LCPD-47381","MCAN: Message Transmit order not guaranteed from dedicated Tx Buffers configured with same Message ID","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2278"
  "LCPD-32351","MMCSD: HS200 and SDR104 Command Timeout Window Too Small","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-hsevm,am68_sk-fs,am69_sk-fs,j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm","i2312"
  "LCPD-24654","MCAN: Implement workaround for errata i2279","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm","i2279"
  "LCPD-19068","DSS: Disabling a layer connected to Overlay may result in synclost during the next frame","j721e-evm,j721e-evm-ivi,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm","i2097"

|

Errata Workarounds Available in this Release
--------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform", "ErrataId"
  :widths: 15, 30, 70, 60


|

Errata Rejected as Not Applicable
----------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform", "ErrataId"
  :widths: 15, 30, 70, 60

  "LCPD-43439","J722S: ROM boot fails for large file sizes","j722s_evm-fs","i2466"

|

Open Erratum
------------
.. csv-table::
  :header: "Record ID", "Title", "Platform", "ErrataId"
  :widths: 15, 30, 70, 60

  "LCPD-49333","Update to i2189: OSPI: Controller PHY Tuning Algorithm - U-Boot","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2509"
  "LCPD-48726","Update to i2189: OSPI: Controller PHY Tuning Algorithm","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2509"
  "LCPD-48725","OSPI: XIP in PHY Mode Not Supported","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2510"

|

U-Boot Known Issues
-------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform", "Workaround"
  :widths: 15, 30, 70, 30

  "LCPD-48474","Boot modes: Ethernet with kernel is failing in 12.01.00.05","am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am68_sk-fs,am69_sk-fs,j722s_evm-fs",""
  "LCPD-46031","DFU: SPL-DFU boot support is failing in 12.01.00.05","am62axx_sk-fs,am62dxx_evm-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am64xx-hsevm,j721e-idk-gw,j722s_evm-fs,j742s2_evm-fs",""
  "LCPD-44857","j722s_evm-fs: RC-08: Failure: UBOOT : MSC boot shall be supported","j722s_evm-fs",""
  "LCPD-38569","j722s: Unable to communicate with MCU R5 and Main R5 when FW loaded from U-Boot","j722s_evm-fs",""

|

Linux Known Issues
------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform", "Workaround"
   :widths: 5, 10, 70, 35

   "LCPD-49301","CICD: Boot modes: eMMC boot from boot0 failing","j722s_evm-fs",""
   "LCPD-49213","CICD:  Crypto test NOTRUN","am62lxx_evm-fs,am64xx-hsevm,am654x-hsevm,am68_sk-fs,j7200-evm,j721s2_evm-fs,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
   "LCPD-49110","j722s_evm-fs: RNG_S_FUNC_10000 test is failing with in 12.02 CICD","j722s_evm-fs",""
   "LCPD-49072","SDK 11.02.02 Audio bugs","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
   "LCPD-48967","PCIe MSIX failure in 11.02.18","j722s_evm-fs",""
   "LCPD-48743","Linux SDK Documentation doesn't capture MCAN Performance Data","j7200-evm,j7200-hsevm,j7200_evm-fs,j721s2-evm,j721s2_evm-fs,j722s_evm-fs,j722s_evm-se",""
   "LCPD-48726","Update to i2189: OSPI: Controller PHY Tuning Algorithm","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","In order to sample data under some conditions, it is necessary to increment the Read Delay field to shift the internal clock sampling window. This allows sampling of the data anywhere within the data eye. However, this has two side effects: 1) PHY Pipeline mode must be enabled for all read operations. Since PHY Pipeline mode must be disabled for writes, reads and writes must be handled separately. 2)Hardware polling of the busy bit is broken when the workaround is in place, so SW polling must be used instead. Writes must occur through DMA accesses, within page boundaries, to prevent interruption from either the host or the flash device. Software must poll the busy bit between page writes. Alternatively, writes can be performed in non-PHY mode with Hardware polling enabled. 3) STIG reads must be padded with extra bytes, and the received data must be right-shifted. To select optimal TX, RX, and Read delay values a tuning algorithm must be run. The original implementation of this software tuning algorithm is described in detail in the application note SPRACT2 (link: https://www.ti.com/lit/spract2 ). This tuning algorithm has been revised in order to improve robustness of the optimal tuning point selected. This algorithm is updated to pick a centered tuning point with run time validation to adjust this point as needed to account for temperature fluctuations. The implementation of this algorithm is described in detail in the application note SDAA315 (link: https://www.ti.com/lit/pdf/SDAA315 )."
   "LCPD-48725","OSPI: XIP in PHY Mode Not Supported","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","If OSPI XIP is needed use TAP mode."
   "LCPD-48716","J722S: NFS BOOT Fails while running ETHFW due to RPMsg Response Timeout","j722s_evm-fs,j722s_evm-se",""
   "LCPD-48480","USBHOST_S_FUNC_HIGHSPEED_HUB_FULLSPEED_0001 is failing in 12.01.00.05","j722s_evm-fs",""
   "LCPD-48470","Ethernet tests failing in 12.1","am62lxx_evm-fs,am62xx_sk-fs,am64xx-hsevm,j7200-evm,j721s2-evm,j722s_evm-fs",""
   "LCPD-48394","USBHOST_XS_FUNC_AUDIO_LOOPBACK_ACCESSTYPE_NONINTER_01 is failing in 12.01.00.05","j721e-idk-gw,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
   "LCPD-48393","USBDEV_highspeed_msc_enumeration is failing in 12.01.00.05","am62axx_sk-fs,am62dxx_evm-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j784s4-evm",""
   "LCPD-48212","USBHOST_S_FUNC_HIGHSPEED_HUB_MULTI_SPEED_0001 is failing in 12.01.00.05","j722s_evm-fs",""
   "LCPD-47981","NFS BOOT Fails while at CORE LINUX FUCNTIONALITY level while running ETHFW standalone code","j722s_evm-fs",""
   "LCPD-47918","Kernel crash due to CPSW Tx timeout","j722s_evm-fs",""
   "LCPD-47799","BCDMA RX_IGNORE_LONG setting in RX CHAN CFG register doesnt work","j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","Workaround: RX_IGNORE_LONG is unusable, so remote endpoint such as PDMA should close packet by sending EOP to match TR boundary (PDMA X*Y*Z should match TR ICNT0*ICNT1*ICNT2*ICNT3). If infinite stream is desired (PDMA Z=0) then switch to PKTDMA and use Single Buffer Mode"
   "LCPD-47763","Defects for J7AEN 11.02 release","j722s_evm-fs,j722s_evm-se",""
   "LCPD-47749","NFS boot fails when EthFW is enabled on MCU2_0 R5F core due to CPSW Proxy Client driver circular dependency","j722s_evm-fs,j722s_evm-se",""
   "LCPD-47220","TEST: RC-07: CPSW: Capability gap for testing XDP tests on j722s","j722s_evm-fs",""
   "LCPD-46418","Crypto: cbc and ecb sa2ul self tests fails on few platforms","am62axx_sk-fs,am62pxx_sk-fs,j722s_evm-fs",""
   "LCPD-46120","cpuloadgen testcase fails to run on all cores","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
   "LCPD-46058","USBDEV_fullspeed_cdc_ping is failing in 12.01.00.05","am62axx_sk-fs,am62xxsip_sk-fs,j721s2-evm,j722s_evm-fs",""
   "LCPD-46057","USBDEV_fullspeed_msc_func is failing in 12.01.00.05","am62xxsip_sk-fs,j722s_evm-fs",""
   "LCPD-46056","USBDEV_highspeed_cdc_ping_zlp is failing in 12.01.00.05","j721s2-evm,j722s_evm-fs",""
   "LCPD-46054","USBDEV_highspeed_cdc_ncm_ping is failing in 12.01.00.05","j721s2-evm,j722s_evm-fs",""
   "LCPD-46052","USBDEV_highspeed_cdc_ping is failing in 12.01.00.05","am62pxx_sk-fs,j721s2-evm,j722s_evm-fs",""
   "LCPD-46050","USBDEV_fullspeed_cdc_ncm_ping is failing in 12.01.00.05","am62axx_sk-fs,am62xxsip_sk-fs,j721s2-evm,j722s_evm-fs",""
   "LCPD-46049","USBDEV_fullspeed_serial_enumerate is failing in 12.01.00.05","j722s_evm-fs",""
   "LCPD-46047","USBDEV_highspeed_serial_enumerate is failing in 12.01.00.05","j722s_evm-fs",""
   "LCPD-46045","ETH_CPSW2g_PTP_Switch is failing in 12.00.00.07","am62axx_sk-fs,am62xxsip_sk-fs,j7200-evm,j721e-idk-gw,j722s_evm-fs,j784s4-evm",""
   "LCPD-46044","USBDEV_highspeed_msc_slave_perf is failing in 12.01.00.05","j722s_evm-fs",""
   "LCPD-45975","USBHOST_L_FUNC_HID_Mouse_Detection_Test is failing in 12.01.00.05","j722s_evm-fs",""
   "LCPD-45969","J722S: Changing DPHY parent refclk breaks USB","am62pxx_sk-fs,j722s_evm-fs",""
   "LCPD-45963","OPTEE xtest failures","am62pxx_sk-fs,am64xx-hsevm,am64xx-hssk,j722s_evm-fs",""
   "LCPD-45253","c7x ipc failure on linux loading remote core firmwares","j722s_evm-fs",""
   "LCPD-44854","Test: Ethernet slave peripheral boot failure","am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am69_sk-fs,j722s_evm-fs",""
   "LCPD-44505","WDT_RTI: Make the watchdog timeout configurable","j722s_evm-fs,j722s_evm-se",""
   "LCPD-43407","IPC Graceful Shutdown on C7x cores","j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
   "LCPD-42843","remoteproc/k3-dsp: PDK IPC echo test binaries fails to do IPC in remoteproc mode on second run","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j784s4-evm",""
   "LCPD-41066","CSI outputs black images when DMA is set to ASEL 15","am62pxx_sk-fs,j722s_evm-fs",""
   "LCPD-41044","ARM toolchain used in Yocto build keeps on updating every release","am62axx_sk-fs,am62axx_sk-se,am68_sk-fs,am68_sk-se,am69_sk-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j742s2_evm-fs,j784s4-evm,j784s4-hsevm",""
   "LCPD-38756","AM64x: Linux hangs on repetitive probe/removal of gadget zero","am64xx-evm,am64xx_sk-fs,am68_sk-fs,am68_sk-se,am69_sk-fs,j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm",""
   "LCPD-38311","Power off test case failing","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
   "LCPD-38267","J722S: tiboot3.bin / R5 SPL within size limit fails to boot","j722s_evm-fs",""
   "LCPD-37705","crypto perf failure","am68_sk-fs,j7200-evm,j722s_evm-fs",""
   "LCPD-37702","J722S : Crypto perf (ipsec) test failed","j722s_evm-fs",""
   "LCPD-37314","NFS in UBOOT on J722S EVM (HS-FS) Fails","j722s_evm-fs",""
   "LCPD-34712","OSPI: 2-byte address is not supported in PHY DDR mode","j7200-evm,j721e-idk-gw,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","For compatible OSPI memories that have programmable address byte settings, set the amount of address bytes required from 2 to 4 on the flash. This may involve sending a specific command to change address bytes and/or writing a configuration register on the flash. Once done, update the amount of address bytes sent in the controller settings from 2 to 4. For compatible OSPI memories that only support 2-byte addressing and cannot be re-programmed, PHY DDR mode will not be compatible with that memory. Alternative modes include: PHY SDR mode TAP (no-PHY) DDR mode TAP (no-PHY) SDR mode"

|

Issues closed in system firmware in this release
-------------------------------------------------

System firmware Known Issues
------------------------------

Change Requests
===============

SDK features descoped from 11.02 (J722s) release
------------------------------------------------
.. csv-table::
   :header: "ID", "Headline", "Platform", "Original Fix Version", "New Fix Version"
   :widths: 20, 90, 90, 20, 20

   JACINTOREQ-9373, "Scope Change for LPM Support on J722S", "J722S", 11.02.00, 12.02.00

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

.. note::
   Processor SDK Installer is 64-bit, and installs only on 64-bit host machine.

.. |reg| unicode:: U+00AE .. REGISTERED SIGN
