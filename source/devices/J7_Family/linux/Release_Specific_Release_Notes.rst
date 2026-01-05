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


Release 11.02.00
================

Released Dec 2025

.. rubric:: What's New
   :name: whats-new

Processor SDK 11.02 Release supports the following platforms:

  * J721E
  * J7200
  * J721S2
  * J784S4
  * J722S
  * J742S2

Processor SDK 11.02 Release has following new features:

  * Third 2025 LTS (Linux 6.12 and u-boot 2025.01)
  * ATF v2.13.0+
  * OPTEE 4.7.0
  * Yocto Scarthgap/5.0
  * Low power mode support for J784S4 and J7200
  * Temperature based refresh rate change for DDR
  * Crypto: Add AES-CMAC algorithm support in SA2UL driver
  * Added support for McASP async mode: independent transmit (playback) and receive (capture) clocking

.. _release-specific-build-information:

Build Information
=================

U-Boot
------
| Head Commit: df1fe238230433ba3e5b731356156e145aa90917: TI: dts: arm64: ti: sync dtbs from ti-linux-6.12.y upto 15b58b1dcd0e
| Date: Wed Dec 24 13:19:54 2025 +0530
| uBoot Version: 2025.01
| uBoot Description: 11.02.11

| Repo: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| uBoot Tag: 11.02.11

| Compiler Information: arm-oe-eabi-gcc (GCC) 13.4.0, aarch64-oe-linux-gcc (GCC) 13.4.0
|

.. ifconfig:: CONFIG_image_type in ('edgeai', 'adas')

   .. note::

      meta-edgeai Yocto layer contains additional patches for U-Boot `here <https://git.ti.com/cgit/edgeai/meta-edgeai/tree/recipes-bsp/u-boot?h=REL.PSDK.ANALYTICS.11.02.00.05>`__.

.. _kernel-release-notes:

Kernel
------
.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: 15b58b1dcd0e0a79d83740b81da1a1367f6f3f68: FROMLIST: arm64: dts: ti: Remove 4 watchdogs from common file and move them to J784S4
| Date:   Wed Dec 24 11:32:20 2025 +0530
| Kernel Version: 6.12.57
| Kernel Description: 11.02.11

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.02.11
| Non-RT Kernel defconfig: defconfig + ti_arm64_prune.config
| RT Kernel defconfig: defconfig + ti_rt.config + ti_arm64_prune.config

| Compiler Information: aarch64-oe-linux-gcc (GCC) 13.4.0, GNU ld (GNU Binutils) 2.42.0
|


.. ifconfig:: CONFIG_image_type in ('edgeai', 'adas')

   .. note::

      meta-edgeai Yocto layer contains additional patches for Kernel `here <https://git.ti.com/cgit/edgeai/meta-edgeai/tree/recipes-kernel/linux?h=REL.PSDK.ANALYTICS.11.02.00.05>`__.

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
| Head Commit: d7b3607a76e08b3be8f61ba69d959fa063f44b11: ti-dm: am62px: Update DSS firmware to 11.02.00.11
| Date: Tue Nov 18 06:29:07 2025 -0600

| Repo: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 11.02.08
|



Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: 802cd01e783aeec00af81d99cd242f20ede3adc9: CI/CD Auto-Merger: cicd.scarthgap.202512041635
| Date: Thu Dec 4 16:35:49 2025 -0600

| Repo: https://git.ti.com/cgit/arago-project/meta-ti
| Branch: scarthgap
| Release Tag: 11.02.08
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: b9c8be5cceb1b67c6d14a871fe20e599542999f1: CI/CD Auto-Merger: cicd.scarthgap.202512041635
| Date: Thu Dec 4 16:35:49 2025 -0600

| Repo: https://git.yoctoproject.org/meta-arago
| Branch: scarthgap
| Release Tag: 11.02.08
|

.. rubric:: meta-tisdk

| Head Commit: 71e97d787810978a21dc536dfe59d0c821b554fd ti-lvgl-demo: Simplify recipe and align source

| Repo: https://github.com/TexasInstruments/meta-tisdk.git
| Branch: scarthgap
| Release Tag: REL.PSDK.ANALYTICS.11.02.00.05
|

.. ifconfig:: CONFIG_image_type in ('edgeai', 'adas')

   .. rubric:: meta-edgeai

   | Head Commit: e814c23648afeb0efd277ae6a9fce9aba0aee025 ti-vision-apps: J7*: Bump up to REL.PSDK.ANALYTICS.11.02.00.05
   | Date: 2025-09-13

   | Clone: git://git.ti.com/edgeai/meta-edgeai.git
   | Branch: scarthgap
   | Release Tag: REL.PSDK.ANALYTICS.11.02.00.05
   |

Issues Tracker
==============

Issues opened in previous releases that were closed on this release
-------------------------------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform"
  :widths: 15, 70, 20

   "LCPD-45340","J784S4 Support USB3.0 LANE SWAP functionality","j721s2_evm-fs,j784s4-evm"
   "LCPD-44655","J722S: DFU test case is broken in SDK 11.01 RC7","j722s_evm-fs"
   "LCPD-44644","maxItems for resasg_entries is incorrect","j7200-evm,j721e-sk,j721s2-evm,j784s4-evm"
   "LCPD-44521","U-Boot cannot relocate the initrd","am62axx_sk-fs,am62axx_sk-se,am62lxx-vlab,am62lxx-zebu,am62lxx_evm-fs,am62lxx_evm-se,am62pxx-zebu,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am68_sk-se,am69_sk-fs,bbai,bbai64-gp,beagleplay-gp,j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm,am62dxx_evm-fs,am62dxx_evm-se"
   "LCPD-44466","Codec: Wave5: Improve Decoder Performance and Fix SError Crash on Fluster test","am62axx_sk-fs,am62pxx_sk-fs,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm"
   "LCPD-44297","CPSW crash due to NULL pointer dereference in Linux","j721e-idk-gw"
   "LCPD-44174","Add workaround for SE in C7x boot sequence","j721s2-evm,j784s4-evm"
   "LCPD-43937","j7200: u-boot: Fix eMMC write error","j7200-evm"
   "LCPD-43919","U-Boot: Intermittent TFTP failure due to PHY Auto-Negotiation failure","am64xx-hsevm,j721e-idk-gw"
   "LCPD-43753","Fix HPD in SN65DSI86 driver upstream","am68_sk-fs,j721s2-evm,j784s4-evm"
   "LCPD-43680","ltp-ddt flow: test.sh execution expired on vulkan-cts tests","j721e-idk-gw"
   "LCPD-43636","Test : J7200 : Test for DFU download to eMMC is failing","j7200-evm"
   "LCPD-43548","U-Boot: DDR: Partial inline ECC does not account for second bank","j721s2-evm,j784s4-evm"
   "LCPD-43540","UDP Ingress failing","am62xxsip_sk-fs,am64xx-hsevm,j721e-idk-gw,j742s2_evm-fs,j784s4-evm"
   "LCPD-43472","Test: Test for full-speed NCM USB devices is failing.","j7200-evm,j721s2-evm"
   "LCPD-43465","TIDEC_GST_filesink_rush_hour_p1920x1080_cbr_10mbps.264 test fails","j721s2-evm,j742s2_evm-fs,j784s4-evm"
   "LCPD-43464","TIDEC_GST_filesink_pedestrian_1920x1080_vbr_10mbps.264 fails","j721s2-evm,j742s2_evm-fs,j784s4-evm"
   "LCPD-43264","J721S2 OV5640 Module not functional in Test farm","j721s2-evm"
   "LCPD-43260","UFS tests failure: manual test","j784s4-evm"
   "LCPD-42572","IPC: Testscript: Sometimes U-Boot not able to find firmware from boot media after symlink update","am68_sk-fs,am69_sk-fs,j721e-idk-gw,j721s2_evm-fs,j722s_evm-fs,j742s2_evm-fs,j784s4-evm"
   "LCPD-42095","Hyperflash boot failling","j7200-evm,j721e-idk-gw"
   "LCPD-42039","u-boot: ddrss ecc_err command fails for J7","j721s2-evm,j784s4-evm"
   "LCPD-37288","J784S4: USXGMII: Add automated test case","j784s4-evm,j784s4-hsevm"
   "LCPD-34238","U-boot: Convert MDIO into DM model (impacts ALL TI K3 platforms)","am62axx_sk-fs,am62xx-lp-sk,am62xx-sk,am64xx_sk-fs,am654x-evm,am68_sk-fs,am69_sk-fs,j7200-evm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2_evm-fs"
   "LCPD-24725","PCIE RC Link fails when linux prints are made quiet","j721e-idk-gw"
   "LCPD-24456","Move IPC validation source from github to git.ti.com","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-epos,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am62axx_sk-fs,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am64xx-evm,am64xx-hsevm,am64xx_sk-fs,am654x-evm,am654x-hsevm,am654x-idk,bbai,beaglebone,beaglebone-black,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm,j7200-evm,j7200-hsevm,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,omapl138-lcdk"

|

Issues found and closed on this release that may be applicable to prior releases
--------------------------------------------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform"
  :widths: 15, 70, 20

   "LCPD-45576","Improper Timestamp Handling in Wave5 driver","am62axx_sk-fs,am62pxx_sk-fs,am68_sk-fs,am69_sk-fs,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm"
   "LCPD-45566","OSPI : Unable to create MTD partitions","j7200-evm"
   "LCPD-45554","NFS boot takes too much time due to PHY negotiation for every request","am62axx_sk-fs,am62axx_sk-se,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm"
   "LCPD-45495"," K3CONF_SOC_PD_TEST fail","am62axx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am68_sk-fs,am69_sk-fs,j7200_evm-fs,j721e-idk-gw,j721s2-evm,am62dxx_evm-fs"
   "LCPD-45439","Linux: J784S4 PCIe Endpoint DMA Throughput is low","j784s4-evm,j784s4-hsevm"
   "LCPD-45421","UFS within U-Boot fails to set bRefClkFreq","j784s4-evm"
   "LCPD-45386","ltp-ddt: ltp result file not found ","am62pxx_sk-fs,am68_sk-fs,j721s2-evm"
   "LCPD-45261","Incorrect Pullup for I2C pins in Linux device tree.","j784s4-evm"
   "LCPD-45210","J784S4: Test Farm: U-Boot DHCP Failure","j784s4-evm,j784s4-hsevm"
   "LCPD-45142","Adding thermistor using generic-adc-thermal driver to tscadc","j784s4-evm"
   "LCPD-45040","CICD: HWSPINLOCK_S_FUNC functional test failures","am62xxsip_sk-fs,j722s_evm-fs"
   "LCPD-44983","U-Boot: J7200: DP83867 PHY driver replaced by Generic PHY driver","j7200-evm"
   "LCPD-44980","Backport ""board: ti: common: Kconfig: add CMD_CACHE"" into TI U-Boot Tree","am62axx_sk-fs,am62axx_sk-se,am62lxx_evm-fs,am62lxx_evm-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am68_sk-se,am69_sk-fs,bbai,bbai64-gp,j7200-evm,j7200-hsevm,j721e-idk-gw,j721s2-evm,j721s2-hsevm,j722s_evm-fs,j722s_evm-se,j784s4-evm,j784s4-hsevm"
   "LCPD-44850","j721s2-evm: RC-08: Failure: Linux : USB : HOST : Selective suspend shall be su...","j721s2-evm"
   "LCPD-44847","j721e-idk-gw: RC-08: Failure: Linux : USB : DUALROLE : USB Role switch support w...","j721e-idk-gw"

|

Errata Workarounds Available in this Release
--------------------------------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform"
  :widths: 15, 30, 150

   "LCPD-44174","Add workaround for SE in C7x boot sequence"
   "LCPD-38547","PRU_ICSSG: DOC: Undefined labels"
   "LCPD-37965","BCDMA: RX Channel can lockup in certain scenarios"
   "LCPD-37352","USB2 PHY locks up due to short suspend"
   "LCPD-37081","USB2 PHY locks up due to short suspend"
   "LCPD-32855","VTM: Temperature Monitors (TEMPSENSORs) should use a software trimming method"
   "LCPD-32825","PCIe: ls -al /dev/disk/by-id shows no nvme device"
   "LCPD-32351","MMCSD: HS200 and SDR104 Command Timeout Window Too Small"
   "LCPD-28496","CPSW: Device lockup when reading CPSW registers"
   "LCPD-27887","i2327: RTC: Hardware wakeup event limitation"
   "LCPD-27886","USART: Erroneous clear/trigger of timeout interrupt"
   "LCPD-25264","BCDMA: Blockcopy Gets Corrupted if TR Read Responses Interleave with Source Data Fetch"
   "LCPD-24274","PCIe: Link up failure when unused lanes are not assigned to PCIe Controller"
   "LCPD-22905","UDMA: TR15 hangs if ICNT0 is less than 64 bytes"
   "LCPD-22890","PCIe: Link up failure when unused lanes are not assigned to PCIe Controller"
   "LCPD-22576","UART: Possible underflow condition when using EDMA with UART1, UART2, UART3"
   "LCPD-22573","DPHY: Reset sequence issue can lead to undefined module behavior"
   "LCPD-22544","DDR: LPDDR4 should be configured to 2666 MT/S"
   "LCPD-22543","CPSW: ALE IET Express Packet Drops"
   "LCPD-22424","PCIe: SERDES output reference clock cannot be used"
   "LCPD-22293","UFS: Auto-Hibernate can cause false entry/exit errors"
   "LCPD-22249","UDMA: Force teardown bitfield readback is masked in realtime TX/RX registers"
   "LCPD-20123","MPU COUNTER_REALTIME saturates after several hundred days"
   "LCPD-19987","UDMAP: Spurious ECC errors due to MAIN/MCU NAVSS rofifo_wr_byten issue"
   "LCPD-19986","UDMAP: TX Channel SA2UL teardown issue"
   "LCPD-19966","I3C: SDAPULLEN drives low instead of Hi-Z"
   "LCPD-19965","OSPI PHY Controller Bug Affecting Read Transactions"
   "LCPD-19874","PSIL: Clock stop operation can result in undefined behavior"
   "LCPD-19811","CPSW: ALE incorrectly routes packets with CRC errors"
   "LCPD-19586","USB: 2.0 PHY hangs if received signal amplitude crosses squelch threshold multiple times within the same packet"
   "LCPD-19561","R5FSS: Lock-step mode of operation is not functional"
   "LCPD-19447","DSS: Disabling a layer connected to Overlay may result in synclost during the next frame"
   "LCPD-19068","DSS: Disabling a layer connected to Overlay may result in synclost during the next frame"
   "LCPD-19056","USB: DMA hangs if USB reset is received during DMA transfer in device mode"
   "LCPD-19048","USB: Invalid termination of DMA transfer for endpoint following Isochronous endpoint in Superspeed device mode"
   "LCPD-19047","USB: Race condition while reading TRB from system memory in device mode"
   "LCPD-19041","PCIe: End of Interrupt (EOI) not enabled for PCIe legacy interrupts"
   "LCPD-19032","CPSW: CPSW Does Not Support Intersperced Express Traffic (IET – P802.3br/D2.0) In 10/100Mbps Mode"
   "LCPD-19031","[CPTS] GENF (and ESTF)  Reconfiguration Issue"
   "LCPD-19030","USB: USB2PHY Charger Detect is enabled by default without VBUS presence"
   "LCPD-19029","PCI-Express (PCIe) May Corrupt Inbound Data"
   "LCPD-19028","DSS : DSS DPI Interface does not support BT.656 and BT.1120 output modes"
   "LCPD-19027","CPSW does not support CPPI receive checksum (Host to Ethernet) offload feature"
   "LCPD-19026","MMCSD: Negative Current from UHS-I PHY May Create an Over-Voltage Condition on VDDS6 and VDDS7 which exposes the Device to a Significant Reliability Risk"
   "LCPD-19025","IO, MMCSD: Incorrect IO Power Supply Connectivity Prevent Dynamic Voltage Change on VDDSHV6 and VDDSHV7"
   "LCPD-19024","RINGACC and UDMA ring state interoperability issue after channel teardown"
   "LCPD-19022","UDMA-P Real-time Remote Peer Registers not Functional Across UDMA-P Domains"
   "LCPD-18999","PCIe: Endpoint destination select attribute (ASEL) based routing issue"
   "LCPD-18996","Hyperflash: Hyperflash is not functional"
   "LCPD-18995","OSPI: OSPI Boot doesn't support some xSPI modes or xSPI devices"
   "LCPD-18981","UDMAP: Packet mode descriptor Address Space Select Field Restrictions"
   "LCPD-18980","PCIe: Gen2 capable endpoint devices always enumerate as Gen1"
   "LCPD-18979","MCAN: Message Transmitted with Wrong Arbitration and Control Fields (Early Start of Frame)"
   "LCPD-18952","DSS : DSS Does Not Support YUV Pixel Data Formats"
   "LCPD-17806","Cortex-R5F: Deadlock might occur  when one or more MPU regions is configured for write allocate mode"
   "LCPD-17788","PCI-Express: GEN3 (8GT/s) Operation Not Supported."
   "LCPD-17786","UART: Spurious UART Interrupts When Using DMA"
   "LCPD-17784","CPSW: CPSW Does Not Support Intersperced Express Traffic (IET – P802.3br/D2.0) In 10/100Mbps Mode"
   "LCPD-17783","USB: USB2PHY Charger Detect is enabled by default without VBUS presence"
   "LCPD-17333","[CPTS] GENF (and ESTF)  Reconfiguration Issue"
   "LCPD-17220","U-Boot Hyperbus: Hyperflash reads limited to 125MHz max. frequency"
   "LCPD-16904","PCIe: Unsupported request (UR) or Configuration Request Retry Status (CRS) in configuration completion response packets results in external abort"
   "LCPD-16643","Hyperbus: Hyperflash reads limited to 125MHz max. frequency"
   "LCPD-16605","MMC: MMC1/2 Speed Issue"
   "LCPD-16538","PCI-Express (PCIe) May Corrupt Inbound Data"
   "LCPD-14941","RINGACC and UDMA ring state interoperability issue after channel teardown"
   "LCPD-14579","DSS : DSS Does Not Support YUV Pixel Data Formats"
   "LCPD-14577","CPSW does not support CPPI receive checksum (Host to Ethernet) offload feature"
   "LCPD-14187","UDMA-P Real-time Remote Peer Registers not Functional Across UDMA-P Domains"
   "LCPD-14185","MSMC: Non-coherent memory access to coherent memory can cause invalidation of snoop filter"
   "LCPD-14184","USB:  SuperSpeed USB Non-Functional"
   "LCPD-9084","i887: Software workaround to limit mmc3 speed to 64MHz"
   "LCPD-8294","37 pins + VOUT pins need slow slew enabled for timing and reliability respectively"
   "LCPD-8277","u-boot: j6: SATA is not shutdown correctly as per errata i818"
   "LCPD-7642","MMC/SD: i832: return DLL to default reset state with CLK gated if not in SDR104/HS200 mode."
   "LCPD-6907","Workaround errata i880 for RGMII2 is missing"
   "LCPD-5931","DRA7xx: AM57xx: mmc: upstream errata workaround for i834"
   "LCPD-5924","ALL: CONNECTIVITY: CPSW: errata i877 workarround for cpsw"
   "LCPD-5836","CAL: Errata: i913: CSI2 LDO needs to be disabled when module is powered on"
   "LCPD-5309","i896: USB Port disable doesnt work"
   "LCPD-5308","i897: USB Stop Endpoint doesnt work in certain circumstances"
   "LCPD-5052","Upstream: Post the dmtimer errata fix for i874"
   "LCPD-4975","DSS AM5/DRA7: implement WA for errata i886"
   "LCPD-4912","DRA7: USB: Implement ErrataID_i896_PED_issue"
   "LCPD-4910","J6/OMAP5: errata i810 implementation"
   "LCPD-4648","[rpmsg 2014 LTS] Implement errata i879 - DSP MStandby requires CD_EMU in SW_WKUP"
   "LCPD-4647","[rpmsg 2015 LTS] Implement errata i879 - DSP MStandby requires CD_EMU in SW_WKUP"
   "LCPD-4225","J6: Errata: i834: Investigate possibility of software workaround"
   "LCPD-4218","Implement Workaround for Errata i813 - Spurious Thermal Alert Generation When Temperature Remains in Expected Range"
   "LCPD-4217","Implement Workaround for Errata i814 - Bandgap Temperature read Dtemp can be corrupted"
   "LCPD-4195","J6: SATA: Investigate applicability of i807"
   "LCPD-4184","Implement workaround for errata i814 - Bandgap Temperature read Dtemp can be corrupted"
   "LCPD-1776","[J6 SATA Adaptation] J6 - Errata i783, SATA Lockup After SATA DPLL Unlock/Relock"
   "LCPD-1188","J6: Baseport: Errata i877: RGMII clocks must be enabled to avoid IO timing degradation due to Assymetric Aging"
   "LCPD-1146","DMM hang: Errata VAYU-BUG02976 (i878) (register part)"
   "LCPD-1108","J6: Wrong Access In 1D Burst For YUV4:2:0-NV12 Format (Errata i631)"
   "LCPD-1087","J6: MMC: Errata: i802: OMAP5430 MMCHS: DCRC errors during tuning procedure"
   "LCPD-976","J6/J6eco: 32clk is psuedo (erratum i856) - clock source"
   "LCPD-975","J6/J6eco: 32clk is psuedo (erratum i856) - realtime counter"
   "LCPD-876","OMAP5: Errata i810: DPLL Controller Sticks when left clock requests are removed"



|

U-Boot Known Issues
-------------------
.. csv-table::
  :header: "Record ID", "Title", "Platform", "Workaround"
  :widths: 15, 30, 70, 30

   "LCPD-42341","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j784s4-evm","Missing Test support to verify order of remotecores being loaded at U-Boot",""
   "LCPD-42041","j721e-idk-gw","Upstream: j721e: Initial U-boot prints taking around 10s",""
   "LCPD-34106","j721s2-evm,j721s2_evm-fs","SPL: USB DFU Boot fails on J721S2 EVM on upstream U-Boot(also ti-u-boot-2023.04)",""
   "LCPD-24108","j721e-evm,j721e-evm-ivi,j721e-idk-gw","U-Boot: TISCI config ring fail traces seen in OSPI boot mode on J721E",""
   "LCPD-22904","j7200-evm,j721e-idk-gw","U-boot: Update EMIFtool for i2244:DDR: Valid stop value must be defined for write DQ VREF training",""
   "LCPD-17789","j721e-idk-gw","UBOOT J7:  Could not see UFS device by scsi scan",""


|

Linux Known Issues
------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform", "Workaround"
   :widths: 5, 10, 70, 35

   "LCPD-45962","j7200-evm,j784s4-evm","Remotecore IPC communication is not functional after suspend-resume",""
   "LCPD-45771","am62pxx_sk-fs,am62pxx_sk-se,j722s_evm-fs,j722s_evm-se","GPIO PADCONFIG Bits Changing after using gpiod userspace",""
   "LCPD-45607","j7200-evm,j721s2-evm","McSPI performance improvements",""
   "LCPD-45569","j7200-evm","J7200: UART: Infinite IRQs storm upon error condition on the RX Line",""
   "LCPD-45418","j784s4-evm","PCIe-1 does not work after resuming from low power mode",""
   "LCPD-45253","j722s_evm-fs","c7x ipc failure on linux loading remote core firmwares",""
   "LCPD-45239","am62axx_sk-fs,am62axx_sk-se,am62lxx_evm-fs,am62lxx_evm-se,am62pxx-zebu,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am68_sk-se,am69_sk-fs,j7200-evm,j7200-hsevm,j7200_evm-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm,am62dxx_evm-fs,am62dxx_evm-se","VTM module sensor reset sequence modification for reliable functionality ",""
   "LCPD-45212","j7200-evm,j721e-evm-ivi,j721s2-evm,j784s4-evm","Linux kernel crash if R5F firmware is stopped while rpmsg char simple is running",""
   "LCPD-44947","am69_sk-fs,j784s4-evm","J784S4 PCIe legacy interrupt removed",""
   "LCPD-44859","j742s2_evm-fs","j722s_evm-fs: RC-08: Failure: Support CPSW 3G credit based shaper (802.1qav) wit...",""
   "LCPD-44856","j742s2_evm-fs","j742s2_evm-fs: RC-08: Failure: PTP using CPSW CPTS for 1588 Time-stamping in Linu...",""
   "LCPD-44855","j722s_evm-fs","j722s_evm-fs: RC-08: Failure: Core SDK Linux shall include performance documenta...",""
   "LCPD-44854","am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am69_sk-fs,j722s_evm-fs","Test: Ethernet slave peripheral boot failure",""
   "LCPD-44851","j784s4-evm","j784s4-evm: RC-08: Failure: Core SDK Linux shall include performance documenta...",""
   "LCPD-44846","j721e-idk-gw","j721e-idk-gw: RC-08: Failure: Linux : USB : DEVICE : Super-speed NCM client gadg...",""
   "LCPD-44845","j721e-idk-gw","j721e-idk-gw: RC-08: Failure: Linux : USB : DEVICE : Super-speed ECM client gadg...",""
   "LCPD-44842","j742s2_evm-fs","RC8 cpsw PTP failure",""
   "LCPD-44841","j722s_evm-fs,j722s_evm-se","Linux: J722S RC MSI and MSI-X Testing requires non-J722S EP EVM",""
   "LCPD-44834","j721e-idk-gw","MMC card is not getting probed corrected on J721E",""
   "LCPD-44505","j722s_evm-fs,j722s_evm-se","WDT_RTI: Make the watchdog timeout configurable",""
   "LCPD-44298","j722s_evm-fs,j722s_evm-se","J722s: MAIN_I2C4 device tree node is missing",""
   "LCPD-43842","j722s_evm-fs,j722s_evm-se","Missing k3-am625-sk-mcspi-loopback.dtbo in latest build for AM67",""
   "LCPD-43635","j721s2-evm","USB: J721s2: USB Super-speed tests are failing",""
   "LCPD-43625","j7200-evm","Test: USB audio class client device tests are failing",""
   "LCPD-43611","am62lxx_evm-fs,am64xx-hsevm,am68_sk-fs,am69_sk-fs,j721e-idk-gw,j742s2_evm-fs,j784s4-evm","Test: USB audio tests are failing",""
   "LCPD-43480","am68_sk-fs,am69_sk-fs,j7200-evm,j721e-idk-gw,j721s2_evm-fs,j722s_evm-fs,j742s2_evm-fs,j784s4-evm","USB : Selective suspend to RAM test is failing",""
   "LCPD-43475","am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am64xx-hsevm,j7200-evm,j721e-idk-gw,j742s2_evm-fs,j784s4-evm","Test: Test for test for USB MSC device enumeration is failing",""
   "LCPD-43407","j721e-idk-gw,j721s2-evm,j722s_evm-fs,j784s4-evm","IPC Graceful Shutdown on C7x cores",""
   "LCPD-43304","am62axx_sk-fs,am62axx_sk-se,j721e-evm-ivi,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j722s_evm-se,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","CSI RX driver does not consider byterperline parameter in set format",""
   "LCPD-42843","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j784s4-evm","remoteproc/k3-dsp: PDK IPC echo test binaries fails to do IPC in remoteproc mode on second run",""
   "LCPD-42557","am654x-idk,j7200-evm,j721e-idk-gw,j721s2-evm,j784s4-evm","MSMC: A53, A72 Coherent Streaming Writes have minor sub-optimal performance","See description"
   "LCPD-42345","j742s2_evm-fs,j784s4-hsevm","Missing Test support for verifying RTOS<->RTOS IPC parallely with Kernel IPC",""
   "LCPD-42294","j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk","[uboot-eMMC]: Incorrect OTAP Delay for J721E SR2.0",""
   "LCPD-42099","j742s2_evm-fs,j784s4-evm","UFS failure in Farm on J742s2/J784s4  device",""
   "LCPD-41066","am62pxx_sk-fs,j722s_evm-fs","CSI outputs black images when DMA is set to ASEL 15",""
   "LCPD-41044","am62axx_sk-fs,am62axx_sk-se,am68_sk-fs,am68_sk-se,am69_sk-fs,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j742s2_evm-fs,j784s4-evm,j784s4-hsevm","ARM toolchain used in Yocto build keeps on updating every release",""
   "LCPD-38558","j7200-evm,j721e-idk-gw,j721s2-evm,j784s4-evm","Unable to gracefully shutdown both cores in R5 Cluster",""
   "LCPD-38311","j7200-evm,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j742s2_evm-fs,j784s4-evm","Power off test case failing",""
   "LCPD-38267","j722s_evm-fs","J722S: tiboot3.bin / R5 SPL within size limit fails to boot",""
   "LCPD-38070","j721e-hsevm","Misbehavior of CPSW due to ALE entries overwritten by driver",""
   "LCPD-37953","j721s2-evm,j784s4-evm","NFS boot stress test causing FWL exception",""
   "LCPD-37705","am68_sk-fs,j7200-evm,j722s_evm-fs","crypto perf failure ",""
   "LCPD-37704","j722s_evm-fs","J722S : i2c test failing ",""
   "LCPD-37702","j722s_evm-fs","J722S : Crypto perf (ipsec) test failed ",""
   "LCPD-37690","j721e-idk-gw,j784s4-evm","UFS test case failing due test setup issue",""
   "LCPD-37463","am64xx-hsevm,j721e-idk-gw","We don't have SMMU kernel options related to VFIO should be NOIOMMU set",""
   "LCPD-37314","j722s_evm-fs","NFS in UBOOT on J722S EVM (HS-FS) Fails",""
   "LCPD-37199","am62axx_sk-fs,j721e-idk-gw,j721s2-evm","TPS6594: Error IRQ trap reach ilim, overcurrent for BUCK1/2 error",""
   "LCPD-36952","j721s2-evm","Add support for J721S2 PG 1.1 in uboot",""
   "LCPD-36863","am68_sk-fs,j7200-hsevm,j721e-hsevm","OPTEE/ATF are not protected by c7x",""
   "LCPD-36841","j721e-evm,j721e-idk-gw","TDA4VM/J721e: An indirect write completion error occurred in the linux OSPI driver",""
   "LCPD-36794","j7200-evm","j7200-evm: eth firmware floods network with dhcp packets  ",""
   "LCPD-36474","j721s2-evm","J721s2 incorrect autogen generated data",""
   "LCPD-36386","j721e-idk-gw","IPSEC connection failure on automated setup in testfarm",""
   "LCPD-35384","j721s2-evm","After repetative connect/Disconnect EVM is  not getting detected to HOST pc in device mode ",""
   "LCPD-34902","j721e-evm-ivi","J721E EVM PCIe switch causes kernel panic",""
   "LCPD-34619","j7200-evm","k3conf reports wrong error information while setting the clock frequency",""
   "LCPD-32544","j7200-evm","J7200: OSPI Phy calibration fails intermittently",""
   "LCPD-29647","j7200-evm","Non-fatal failure logs seen during system boot up",""
   "LCPD-29409","am62pxx_sk-fs,am62pxx_sk-se,am62xx-sk,am62xx_sk-fs,am62xx_sk-se,j721e-idk-gw,j721s2-evm","DMIPS number should reflect all 4 cores",""
   "LCPD-28250","j721s2-evm,j721s2_evm-fs","J721S2: QSPI Write corrupted when the first operation after powerup is erase",""
   "LCPD-25304","j721s2-evm,j721s2_evm-fs","J721S2: USB: USB 3.0 devices not getting enumerated in high speed",""
   "LCPD-24648","am335x-evm,am572x-idk,am64xx-evm,dra71x-evm,j7200-evm,j721e-evm","Move dma-heaps-test and ion-tests to TI repositories",""
   "LCPD-24589","am57xx-evm,j721e-idk-gw","no new usb reported on host after g_multi ",""
   "LCPD-22339","j7200-evm,j721e-idk-gw","PCI-E USBCARD, ETHCARD don't indicate 2-lane support with lspci",""
   "LCPD-20653","am335x-evm,am43xx-gpevm,am654x-idk,j721e-idk-gw,j722s_evm-fs","ltp: kernel syscall tests fail",""
   "LCPD-19739","am654x-idk,j7200-evm","AM65 shutdown error",""
   "LCPD-19499","j7200-evm,j7200-hsevm","Kernel: OSPI write throughput is less than 1MB/s",""
   "LCPD-19497","j7200-evm","J7200: CPSW2g: interface goes up and down sporadically","Seen only on very few EVMs. No workaround. "
   "LCPD-19084","j721e-idk-gw","Few SD cards not enumerating in Kernel with Alpha EVM",""
   "LCPD-19068","j721e-evm,j721e-evm-ivi,j721e-idk-gw","DSS: Disabling a layer connected to Overlay may result in synclost during the next frame",""
   "LCPD-18790","j721e-idk-gw","eMMC tests failed on J7 rev E2 EVM",""
   "LCPD-17172","j721e-idk-gw","Uboot USBhost: Sandisk Extreme USB 3.0 msc stick could not be detected at second time",""
   "LCPD-17171","j721e-idk-gw","Uboot dhcp occasionally failed",""
   "LCPD-16640","j721e-idk-gw","PCIe RC: GIC ITS misbehaves when more than 4 devices use it simultaneously",""
   "LCPD-16396","j721e-evm,j721e-evm-ivi,j721e-idk-gw","J721E: RC: Unsupported request in configuration completion packets results in an abort","Workaround for Multifunction: Configure all the physical functions supported by the endpoint. For configuring all the 6 functions of PCIe  controller instance '1' in J721E, the following can be used. mount -t configfs none /sys/kernel/config; cd /sys/kernel/config/pci_ep/; mkdir functions/pci_epf_test/func1; echo 0x104c > functions/pci_epf_test/func1/vendorid; echo 0xb00d > functions/pci_epf_test/func1/deviceid; echo 1 > functions/pci_epf_test/func1/msi_interrupts; echo 16 > functions/pci_epf_test/func1/msix_interrupts; ln -s functions/pci_epf_test/func1 controllers/d800000.pcie-ep/; mkdir functions/pci_epf_test/func2; echo 0x104c > functions/pci_epf_test/func2/vendorid; echo 0xb00d > functions/pci_epf_test/func2/deviceid; echo 1 > functions/pci_epf_test/func2/msi_interrupts; echo 16 > functions/pci_epf_test/func2/msix_interrupts; ln -s functions/pci_epf_test/func2 controllers/d800000.pcie-ep/; mkdir functions/pci_epf_test/func3; echo 0x104c > functions/pci_epf_test/func3/vendorid; echo 0xb00d > functions/pci_epf_test/func3/deviceid; echo 1 > functions/pci_epf_test/func3/msi_interrupts; echo 16 > functions/pci_epf_test/func3/msix_interrupts; ln -s functions/pci_epf_test/func3 controllers/d800000.pcie-ep/; mkdir functions/pci_epf_test/func4; echo 0x104c > functions/pci_epf_test/func4/vendorid; echo 0xb00d > functions/pci_epf_test/func4/deviceid; echo 1 > functions/pci_epf_test/func4/msi_interrupts; echo 16 > functions/pci_epf_test/func4/msix_interrupts; ln -s functions/pci_epf_test/func4 controllers/d800000.pcie-ep/; mkdir functions/pci_epf_test/func5; echo 0x104c > functions/pci_epf_test/func5/vendorid; echo 0xb00d > functions/pci_epf_test/func5/deviceid; echo 1 > functions/pci_epf_test/func5/msi_interrupts; echo 16 > functions/pci_epf_test/func5/msix_interrupts; ln -s functions/pci_epf_test/func5 controllers/d800000.pcie-ep/; mkdir functions/pci_epf_test/func6; echo 0x104c > functions/pci_epf_test/func6/vendorid; echo 0xb00d > functions/pci_epf_test/func6/deviceid; echo 1 > functions/pci_epf_test/func6/msi_interrupts; echo 16 > functions/pci_epf_test/func6/msix_interrupts; ln -s functions/pci_epf_test/func6 controllers/d800000.pcie-ep/; echo 1 > controllers/d800000.pcie-ep/start; echo 1 > /sys/bus/pci/devices/0000:00:00.0/remove; echo 1 > /sys/bus/pci/rescan; Workaround for switch card: No workarounds available."
   "LCPD-15708","j721e-vlab","J721E: vlab: MMC1 not functional",""
   "LCPD-14249","j721e-vlab","PCI kernel oops seen between rc7 and rc8 of 4.19",""
   "LCPD-9981","j721e-vlab,omapl138-lcdk","Some LTP's memory management tests fail due to low amount of free memory",""


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

.. note::
   Processor SDK Installer is 64-bit, and installs only on 64-bit host machine.

.. |reg| unicode:: U+00AE .. REGISTERED SIGN
