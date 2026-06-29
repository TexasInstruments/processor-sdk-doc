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

Release 11.02.01
================

Released June 2026

.. rubric:: What's New
   :name: whats-new

Processor SDK 11.02.01 Release supports the following platforms:

  * J721E
  * J7200
  * J721S2
  * J784S4
  * J722S
  * J742S2

Processor SDK 11.02.01 Release has following features

  * Fourth 2025 LTS (Linux 6.12 and u-boot 2025.01)
  * ATF v2.13.0+
  * OPTEE 4.7.0
  * Yocto Scarthgap/5.0
  * Bug fixes for errata.

.. _release-specific-build-information:

Build Information
=================

U-Boot
------
| Head Commit: 1612e4d1deb11d49304c715576854b28cc10e34d: TI: dts: upstream: arm64: ti: Sync dtbs from ti-linux sha 98bbe0d37952
| Date: Thu Jun 11 18:38:10 2026 +0530
| uBoot Version: 2025.01
| uBoot Description: 11.02.15

| Repo: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| uBoot Tag: 11.02.15

| Compiler Information: arm-oe-eabi-gcc (GCC) 13.4.0, aarch64-oe-linux-gcc (GCC) 13.4.0
|

.. ifconfig:: CONFIG_image_type in ('edgeai', 'adas')

   .. note::

      meta-edgeai Yocto layer contains additional patches for U-Boot `here <https://git.ti.com/cgit/edgeai/meta-edgeai/tree/recipes-bsp/u-boot?h=REL.PSDK.ANALYTICS.11.02.00.06>`__.

.. _kernel-release-notes:

Kernel
------
.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: 98bbe0d37952d0ce1b6508f108c357ceb6d58bf3: PENDING: remoteproc: k3-dsp: Add support to suspend attached rprocs
| Date:  Thu Jun 11 17:56:58 2026 +0530
| Kernel Version: 6.12.57
| Kernel Description: 11.02.15

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.02.15
| Non-RT Kernel defconfig: defconfig + ti_arm64_prune.config
| RT Kernel defconfig: defconfig + ti_rt.config + ti_arm64_prune.config

| Compiler Information: aarch64-oe-linux-gcc (GCC) 13.4.0, GNU ld (GNU Binutils) 2.42.0
|


.. ifconfig:: CONFIG_image_type in ('edgeai', 'adas')

   .. note::

      meta-edgeai Yocto layer contains additional patches for Kernel `here <https://git.ti.com/cgit/edgeai/meta-edgeai/tree/recipes-kernel/linux?h=REL.PSDK.ANALYTICS.11.02.00.06>`__.

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
| Head Commit: 59351d453295295909a25a68b30f87e5c85a6e8a: ti-ipc: j721s2/j7200/j784s4/j742s2/j721e/j722s: update ipc binaries
| Date: Mon Jun 8 16:45:01 2026 +0530

| Repo: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 11.02.15
|



Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: 9859d582984a87b42db107127e829c976f315ee3: CI/CD Auto-Merger: cicd.scarthgap.202606151035
| Date: Mon Jun 15 10:35:34 2026 -0500

| Repo: https://git.ti.com/cgit/arago-project/meta-ti
| Branch: scarthgap
| Release Tag: 11.02.15
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: f6dc5e4817c6551ea5250ab1beed6ffc6fc235f2: CI/CD Auto-Merger: cicd.scarthgap.202606151035
| Date: Thu Feb 12 15:38:01 2026 -0600

| Repo: https://git.yoctoproject.org/meta-arago
| Branch: scarthgap
| Release Tag: 11.02.15
|

.. rubric:: meta-tisdk

| Head Commit: 078b37b05e191a0e69ddbe74b402e0f1b29e6b30 tisdk-evse-image: add image recipe for EVSE OOB
| Date: Tue Dec 23 00:26:58 2025 -0600

| Repo: https://github.com/TexasInstruments/meta-tisdk.git
| Branch: scarthgap
| Release Tag: REL.PSDK.ANALYTICS.11.02.00.06
|

.. ifconfig:: CONFIG_image_type in ('edgeai', 'adas')

   .. rubric:: meta-edgeai

   | Head Commit: 7d07e25a15632494d6c30efb09d68de1c95f9394 recipes-core/packagegroup: Add yaml-cpp packagegroup
   | Date: Fri Jan 23 04:50:28 2026 -0600

   | Clone: git://git.ti.com/edgeai/meta-edgeai.git
   | Branch: scarthgap
   | Release Tag: REL.PSDK.ANALYTICS.11.02.00.06
   |

Issues Tracker
==============

Issues opened in previous releases that were closed on this release
-------------------------------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform"
  :widths: 15, 70, 20

  "LCPD-45902","J722s/AM67 & AM62P: eDP HPD failure","am62pxx_sk-fs,j722s_evm-fs,j722s_evm-se"
  "LCPD-45771","GPIO PADCONFIG Bits Changing after using gpiod userspace","am62pxx_sk-fs,am62pxx_sk-se,j722s_evm-fs,j722s_evm-se"
  "LCPD-45577","Job_ready false reporting ready state too frequently in Wave5 driver","am62axx_sk-fs,am62pxx_sk-fs,am68_sk-fs,am69_sk-fs,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm"
  "LCPD-45257","MK-Image tool packaged in U-boot increasing size of u-boot.img","j721e-hsevm,j721s2_evm-se,j722s_evm-se,j784s4-hsevm"
  "LCPD-44298","J722s: MAIN_I2C4 device tree node is missing","j722s_evm-fs,j722s_evm-se"
  "LCPD-42341","Missing Test support to verify order of remotecores being loaded at U-Boot","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j784s4-evm"
  "LCPD-24654","MCAN: Implement workaround for errata i2279","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm"
  "LCPD-19068","DSS: Disabling a layer connected to Overlay may result in synclost during the next frame","j721e-evm,j721e-evm-ivi,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm"

|

Issues found and closed on this release that may be applicable to prior releases
--------------------------------------------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform"
  :widths: 15, 70, 20

  "LCPD-47654","DDR: Valid VRef range must be defined during LPDDR4 Command Bus Training","j7200-evm,j7200-hsevm,j721e-idk-gw,j721s2-hsevm,j721s2_evm-fs,j722s_evm-fs,j722s_evm-se,j784s4-evm,j784s4-hsevm"
  "LCPD-47605","k3conf tool does not show k3conf ddrbw","j722s_evm-fs"
  "LCPD-47389","USART: Erroneous clear/trigger of timeout interrupt","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm"
  "LCPD-47381","MCAN: Message Transmit order not guaranteed from dedicated Tx Buffers configured with same Message ID","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm"
  "LCPD-46928","gstreamer 1.26.9: v4l2src format negotiation fails with capsfilter constraints","am62axx_sk-fs,am62dxx_evm-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am68_sk-fs,am69_sk-fs,j721e-idk-gw,j721s2_evm-fs,j722s_evm-fs,j784s4-hsevm"
  "LCPD-46401","Resolve and test the parameters passed to cppi5_trdesc_calc_size() function","am62axx_sk-fs,am62axx_sk-se,am62dxx_evm-fs,am62dxx_evm-se,am62lxx_evm-fs,am62lxx_evm-se,am62pxx-zebu,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am68_sk-se,am69_sk-fs,bbai64-gp,beagleplay-gp,beagleplay-gp-uart,beagley_ai,j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm"

|

Errata Fixes Available Before this Release
------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform", "ErrataId"
  :widths: 15, 30, 70, 60

  "LCPD-47389","USART: Erroneous clear/trigger of timeout interrupt","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2310"
  "LCPD-32351","MMCSD: HS200 and SDR104 Command Timeout Window Too Small","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-hsevm,am68_sk-fs,am69_sk-fs,j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm","i2312"

|

Errata Workarounds Available in this Release
--------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform", "ErrataId"
  :widths: 15, 30, 70, 60

  "LCPD-47654","DDR: Valid VRef range must be defined during LPDDR4 Command Bus Training","j7200-evm,j7200-hsevm,j721e-idk-gw,j721s2-hsevm,j721s2_evm-fs,j722s_evm-fs,j722s_evm-se,j784s4-evm,j784s4-hsevm","i2160"
  "LCPD-47381","MCAN: Message Transmit order not guaranteed from dedicated Tx Buffers configured with same Message ID","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2278"
  "LCPD-24654","MCAN: Implement workaround for errata i2279","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm","i2279"
  "LCPD-19068","DSS: Disabling a layer connected to Overlay may result in synclost during the next frame","j721e-evm,j721e-evm-ivi,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm","i2097"

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

  "LCPD-47799","BCDMA RX_IGNORE_LONG setting in RX CHAN CFG register doesnt work","j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","i2436"

|

U-Boot Known Issues
-------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform", "Workaround"
  :widths: 15, 30, 70, 30

  "LCPD-44857","j722s_evm-fs: RC-08: Failure: UBOOT : MSC boot shall be supported","j722s_evm-fs",""
  "LCPD-38569","j722s: Unable to communicate with MCU R5 and Main R5 when FW loaded from U-Boot","j722s_evm-fs",""

|

Linux Known Issues
------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform", "Workaround"
   :widths: 5, 10, 70, 35

   "LCPD-48097","MCAN: Implement workaround for errata i2279","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
   "LCPD-48096","MCAN: Message Transmit order not guaranteed from dedicated Tx Buffers configured with same Message ID","j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","Workaround #1: After writing the Tx messages with same Message ID to the Message RAM, request transmission of all these message concurrently by single write access to TXBAR. Make sure none of these messages have a pending Tx request before making the concurrent request. Workaround #2: Use the Tx FIFO instead of dedicated Tx Buffers (set bit MCAN_TXBC[30] TFQM = 0 to use Tx FIFO) for the transmission of several messages with the same Message ID in a specific order."
   "LCPD-48061","DSS: Disabling a layer connected to Overlay may result in synclost during the next frame","j721e-evm-ivi,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
   "LCPD-48060","J722s/AM67 & AM62P: eDP random display init failure","am62pxx_sk-fs,j722s_evm-fs,j722s_evm-se",""
   "LCPD-48059","J722s/AM67 & AM62P: eDP HPD failure","am62pxx_sk-fs,j722s_evm-fs,j722s_evm-se",""
   "LCPD-47981","NFS BOOT Fails while at CORE LINUX FUCNTIONALITY level while running ETHFW standalone code","j722s_evm-fs",""
   "LCPD-47918","Kernel crash due to CPSW Tx timeout","j722s_evm-fs",""
   "LCPD-47868","When booted in attached mode (IPC does not work after s2r)","j7200-evm,j721s2-evm,j722s_evm-se,j742s2_evm-fs,j784s4-evm",""
   "LCPD-47799","BCDMA RX_IGNORE_LONG setting in RX CHAN CFG register doesnt work","j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","Workaround: RX_IGNORE_LONG is unusable, so remote endpoint such as PDMA should close packet by sending EOP to match TR boundary (PDMA X*Y*Z should match TR ICNT0*ICNT1*ICNT2*ICNT3). If infinite stream is desired (PDMA Z=0) then switch to PKTDMA and use Single Buffer Mode"
   "LCPD-47763","Defects for J7AEN 11.02 release","j722s_evm-fs,j722s_evm-se",""
   "LCPD-47749","NFS boot fails when EthFW is enabled on MCU2_0 R5F core due to CPSW Proxy Client driver circular dependency","j722s_evm-fs,j722s_evm-se",""
   "LCPD-47686","ETH_CPSW2g_PTP_DUT_TEE is failing in 11.02.13","j722s_evm-fs",""
   "LCPD-47393","DWC3 USB should not be configured as a wakeup source by default","j722s_evm-fs,j722s_evm-se",""
   "LCPD-47267","J722S: Dual Ethernet port testcases are failing","j722s_evm-fs",""
   "LCPD-47223","TEST: RC-07: CPSW: Add test automation support for packet classification based on ALE engine","j722s_evm-fs",""
   "LCPD-47220","TEST: RC-07: CPSW: Capability gap for testing XDP tests on j722s","j722s_evm-fs",""
   "LCPD-46418","Crypto: cbc and ecb sa2ul self tests fails on few platforms","am62axx_sk-fs,am62pxx_sk-fs,j722s_evm-fs",""
   "LCPD-46190","j722s_evm-fs: RC-08: TESTGAP: Linux SDK: CPSW: Native XDP Support + zero copy su...","j722s_evm-fs",""
   "LCPD-46120","cpuloadgen testcase fails to run on all cores","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
   "LCPD-46058","USBDEV_fullspeed_cdc_ping is failing in 12.00.00.07","am62xxsip_sk-fs,j722s_evm-fs",""
   "LCPD-46057","USBDEV_fullspeed_msc_func is failing in 12.00.00.07","j722s_evm-fs",""
   "LCPD-46056","USBDEV_highspeed_cdc_ping_zlp is failing in 12.00.00.07","j722s_evm-fs",""
   "LCPD-46055","USBDEV_highspeed_msc_enumeration is failing in 12.00.00.07","j722s_evm-fs",""
   "LCPD-46054","USBDEV_highspeed_cdc_ncm_ping is failing in 12.00.00.07","j722s_evm-fs",""
   "LCPD-46052","USBDEV_highspeed_cdc_ping is failing in 12.00.00.07","j722s_evm-fs",""
   "LCPD-46050","USBDEV_fullspeed_cdc_ncm_ping is failing in 12.00.00.07","j722s_evm-fs",""
   "LCPD-46049","USBDEV_fullspeed_serial_enumerate is failing in 12.00.00.07","j722s_evm-fs",""
   "LCPD-46047","USBDEV_highspeed_serial_enumerate is failing in 12.00.00.07","j722s_evm-fs",""
   "LCPD-46045","ETH_CPSW2g_PTP_Switch is failing in 12.00.00.07","am62axx_sk-fs,am62xxsip_sk-fs,j7200-evm,j721e-idk-gw,j722s_evm-fs,j784s4-evm",""
   "LCPD-46044","USBDEV_highspeed_msc_slave_perf is failing in 12.00.00.07","j722s_evm-fs",""
   "LCPD-46043","ETH_CPSW2g_CBS_DUT_TEE is failing in 12.00.00.07","j722s_evm-fs",""
   "LCPD-45969","J722S: Changing DPHY parent refclk breaks USB","am62pxx_sk-fs,j722s_evm-fs",""
   "LCPD-45963","OPTEE xtest failures","am62pxx_sk-fs,am64xx-hsevm,am64xx-hssk,j722s_evm-fs",""
   "LCPD-45903","J722s/AM67 & AM62P: eDP random display init failure","am62pxx_sk-fs,j722s_evm-fs,j722s_evm-se",""
   "LCPD-45253","c7x ipc failure on linux loading remote core firmwares","j722s_evm-fs",""
   "LCPD-45239","VTM module sensor reset sequence modification for reliable functionality","am62axx_sk-fs,am62axx_sk-se,am62dxx_evm-fs,am62dxx_evm-se,am62lxx_evm-fs,am62lxx_evm-se,am62pxx-zebu,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am68_sk-se,am69_sk-fs,j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm",""
   "LCPD-44854","Test: Ethernet slave peripheral boot failure","am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am69_sk-fs,j722s_evm-fs",""
   "LCPD-44841","PCI_S_FUNC_CDNS_MSIX is failing in 12.00.00.07","j722s_evm-fs",""
   "LCPD-44505","WDT_RTI: Make the watchdog timeout configurable","j722s_evm-fs,j722s_evm-se",""
   "LCPD-43407","IPC Graceful Shutdown on C7x cores","j721e-idk-gw,j721s2-evm,j722s_evm-fs,j784s4-evm",""
   "LCPD-43304","CSI RX driver does not consider byterperline parameter in set format","am62axx_sk-fs,am62axx_sk-se,j721e-evm-ivi,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm",""
   "LCPD-42843","remoteproc/k3-dsp: PDK IPC echo test binaries fails to do IPC in remoteproc mode on second run","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j784s4-evm",""
   "LCPD-41066","CSI outputs black images when DMA is set to ASEL 15","am62pxx_sk-fs,j722s_evm-fs",""
   "LCPD-41044","ARM toolchain used in Yocto build keeps on updating every release","am62axx_sk-fs,am62axx_sk-se,am68_sk-fs,am68_sk-se,am69_sk-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j742s2_evm-fs,j784s4-evm,j784s4-hsevm",""
   "LCPD-38311","Power off test case failing","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm",""
   "LCPD-38267","J722S: tiboot3.bin / R5 SPL within size limit fails to boot","j722s_evm-fs",""
   "LCPD-37705","crypto perf failure","am68_sk-fs,j7200-evm,j722s_evm-fs",""
   "LCPD-37702","J722S : Crypto perf (ipsec) test failed","j722s_evm-fs",""
   "LCPD-37314","NFS in UBOOT on J722S EVM (HS-FS) Fails","j722s_evm-fs",""
   "LCPD-34712","OSPI: 2-byte address is not supported in PHY DDR mode","j7200-evm,j721e-idk-gw,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","For compatible OSPI memories that have programmable address byte settings, set the amount of address bytes required from 2 to 4 on the flash. This may involve sending a specific command to change address bytes and/or writing a configuration register on the flash. Once done, update the amount of address bytes sent in the controller settings from 2 to 4. For compatible OSPI memories that only support 2-byte addressing and cannot be re-programmed, PHY DDR mode will not be compatible with that memory. Alternative modes include: PHY SDR mode TAP (no-PHY) DDR mode TAP (no-PHY) SDR mode"
   "LCPD-20653","ltp: kernel syscall tests fail","am335x-evm,am43xx-gpevm,am654x-idk,j721e-idk-gw,j722s_evm-fs",""

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
