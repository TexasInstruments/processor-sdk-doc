.. _Release-note-label:

#############
Release Notes
#############

Overview
========

The **Processor Software Development Kit (Processor-SDK) for Linux**
provides a fundamental software platform for development, deployment and
execution of Linux based applications and includes the following:

-  Bootloaders & Filesystems
-  SDK Installer
-  Setup Scripts
-  Makefiles
-  WLAN support (Wilink 8)
-  Code Composer Studio

Licensing
=========

Please refer to the software manifest, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page. The manifest can be found on the SDK
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
   ``[INSTALL-DIR]/docs``.
-  **EVM Quick Start Guide**: Provides information on hardware setup and
   running the demonstration application that is loaded on flash. This
   document is provided as part of the EVM kit.

Release 09.03.05.02
===================

Released December 2024

.. rubric:: What's New
   :name: whats-new

.. note:: As of Dec 2023, Linux SDK for AM65 is in long term maintenance mode. TI will support critical bug fixes and once a year LTS updates but no new development or new features are planned for this device SDK at this time. The SDK is supported and tested on TMDX654IDKEVM. TMDX654GPEVM is no longer supported.

**Processor SDK Linux AM65X Release has following new features:**

  - LTS Stable Kernel update to 6.1.119
  - Important Bug Fixes on top of Processor SDK 09.01.00.007 Release


**Component version:**

  - Kernel 6.1.119
  - RT Kernel 6.1.119-rt45
  - U-Boot 2023.04
  - Toolchain GCC 11.5
  - ATF 2.10+
  - OPTEE 4.1.0
  - Graphics DDK 1.17
  - SYSFW v10.01.08
  - Yocto Kirkstone


Supported Platforms
===================
See :ref:`here <release-specific-supported-platforms-and-versions>` for a list of supported platforms and links to more information.


.. _release-specific-sdk-components-versions:


Build Information
=================

.. _u-boot-release-notes:
.. _optee-release-notes:
.. _tf-a-release-notes:
.. _ti-linux-fw-release-notes:


U-Boot
------

| Head Commit: 2a13324ec63cc488f5f578886d0cf6ece348dfda arm: dts: am335x: Use PWM for LCD backlight
| uBoot Version: 2023.04
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2023.04
| uBoot Tag: 09.03.05
|


TF-A
----

| Head Commit: 00f1ec6b8740ccd403e641131e294aabacf2a48b Merge changes from topic "revert-ti-dm-workaround" into integration
| Repo: https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git
| Branch: master
| Tag: 2.10+
|

OP-TEE
------

| Head Commit: 012cdca49db398693903e05c42a254a3a0c0d8f2 plat-k3: drivers: sec_proxy: increment while reading trail bytes
| Repo: https://github.com/OP-TEE/optee_os/
| Branch: master
| Tag: 4.1.0
|

ti-linux-firmware
-----------------

| Head Commit: 1eaf07dc4ec5cdeb98078f17a9d4635e88f43f75 ti-dm: Update display sharing firmware for am62px
| Clone: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 09.03.05
|


Kernel
------
.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: c490f4c0fe51281818c45159c0fbed94f852978e HACK: arm: dts: am57: disable late attach as default
| Kernel Version: 6.1.119

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.1.y
| Tag: 09.03.05
| use-kernel-config=defconfig
| config-fragment=kernel/configs/ti_arm64_prune.config
|

.. rubric:: Real Time (RT) Linux Kernel
   :name: real-time-rt-linux-kernel

| Head Commit: b0f9de804a162329bc81857ad50947311228dfb2 Merge branch 'ti-linux-6.1.y-cicd' into ti-rt-linux-6.1.y-cicd
| Kernel Version: 6.1.119-rt45

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-rt-linux-6.1.y
| Tag: 09.03.05-rt
| use-kernel-config=defconfig
| config-fragment=config-fragment=kernel/configs/ti_arm64_prune.config kernel/configs/ti_rt.config
|


Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: 963140e3b5820d6ebf54a4418946a628e0fea2c6 CI/CD Auto-Merger: cicd.kirkstone.202412041235
| Version: Kirkstone-4.0
| Clone: git://git.yoctoproject.org/meta-ti
| Branch: kirkstone
| Release Tag: 09.03.05
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: f59caa5f47a625ef9eecada069ae6a74c70bcc47 CI/CD Auto-Merger: cicd.kirkstone.202412041235
| Version: Kirkstone-4.0
| Clone: git://git.yoctoproject.org/meta-arago
| Branch: kirkstone
| Release Tag: 09.03.05
|


.. rubric:: meta-tisdk

| Head Commit: 2ee8bead9d04afcb61234738e0d9a644395d27bf recipes-core: packagegroups: Drop SGX sources from am65xx
| Version: Kirkstone-4.0
| Clone:  git://git.ti.com/ti-sdk-linux/meta-tisdk.git
| Branch: kirkstone
| Release Tag: 09.03.05.02
|



Issues Tracker
==============

Errata Workarounds Available in this Release
--------------------------------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform"
   :widths: 15, 30, 150

   "LCPD-22905","UDMA: TR15 hangs if ICNT0 is less than 64 bytes","am654x-evm,j721e-idk-gw"
   "LCPD-19965","OSPI PHY Controller Bug Affecting Read Transactions","am654x-idk,am64xx-evm,j721e-idk-gw,j7200-evm"
   "LCPD-19447","DSS: Disabling a layer connected to Overlay may result in synclost during the next frame","am654x-evm,am654x-idk"
   "LCPD-18979","MCAN: Message Transmitted with Wrong Arbitration and Control Fields (Early Start of Frame)","am654x-idk"
   "LCPD-17788","PCI-Express: GEN3 (8GT/s) Operation Not Supported.","am654x-evm,am654x-idk"
   "LCPD-17783","USB: USB2PHY Charger Detect is enabled by default without VBUS presence","am654x-evm,am654x-idk"
   "LCPD-14579","DSS : DSS Does Not Support YUV Pixel Data Formats","am654x-evm,am654x-idk"
   "LCPD-14184","USB:  SuperSpeed USB Non-Functional","am654x-evm"


|


U-Boot Known Issues
-------------------
.. csv-table::
   :header: "Record ID", "Platform", "Title", "Workaround"
   :widths: 15, 30, 70, 30

   "LCPD-28436","am654x-idk","AM65x Uboot PRUETH is broken",""
   "LCPD-24717","am654x-evm,am654x-idk","am654: PCI-E ethernet interface shows link down in U-Boot",""
   "LCPD-24628","am654x-evm,am654x-idk","am654x-idk DFU boot is failing",""
   "LCPD-17770","am654x-evm,am654x-idk,am654x-hsevm","U-Boot: Fix order of MCU R5 shutdown depending on cluster mode",""
   "LCPD-16696","am654x-evm,am654x-idk","U-Boot does not recognize SD-Card after re-insert/change",""
   "LCPD-16524","am654x-evm,am654x-idk,am654x-hsevm","Need to adjust RMW bit when using enabling ECC","None"
   "LCPD-14843","am654x-evm,am654x-idk","U-boot should support  default settings for netboot ","None"


|

Linux Known Issues
------------------
.. csv-table::
   :header: "Record ID", "Platform", "Title", "Workaround"
   :widths: 5, 10, 70, 35

   "LCPD-37152","am654x-idk","ICSSG: IET FPE mac verify fails",""
   "LCPD-36622","am654x-evm,am654x-idk,am654x-hsevm,am64xx-evm","Errata i2028: USB3.0 Host and Device Non-Functional",""
   "LCPD-32868","am654x-idk,am64xx-evm","Kernel crash from PRU auto-forwarding packet",""
   "LCPD-24718","am654x-evm,am654x-idk","am654x hwspinlock test failing",""
   "LCPD-24541","am654x-evm","am65xx OSPI boot does not work",""
   "LCPD-24537","am654x-evm,am64xx-evm,am64xx-hsevm","am654x-idk nslookup times out when all netwokring interfaces are active",""
   "LCPD-24456","am654x-evm,am654x-idk,am654x-hsevm,am64xx-evm,am64xx-hsevm,am62xx_sk-fs,am62xx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62axx_sk-fs,am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am43xx-epos,am43xx-gpevm,am43xx-hsevm,am437x-idk,am437x-sk,am571x-idk,am572x-idk,am574x-idk,am574x-hsidk,am57xx-evm,am57xx-beagle-x15,am57xx-hsevm,am62xx-sk,am64xx_sk-fs,beaglebone,bbai,beaglebone-black,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j7200-evm,j7200-hsevm,omapl138-lcdk","Move IPC validation source from github to git.ti.com",""
   "LCPD-24319","am654x-evm","am654x-evm DRM tests fail due to frequency mismatch (Impact 7)",""
   "LCPD-24134","am654x-evm","AM654x CAL DMABUF tests fail (Impact 4.0)",""
   "LCPD-24130","am654x-evm","AM654x: USB MSC boot mode fails",""
   "LCPD-24128","am654x-idk","Performance issues with CPSW/ICSSG Linux Driver",""
   "LCPD-23008","am654x-evm","AM65xx - display port scenario not enabled",""
   "LCPD-23007","am654x-evm","k3-am654-evm-hdmi.dtbo file is missing in CoreSDK for am654x",""
   "LCPD-22959","am654x-evm","UART Read/Write tests at baud rate 115200 fails",""
   "LCPD-22947","am654x-evm","Alsa performance test fails [waiting for TF]",""
   "LCPD-22892","am654x-evm,am654x-idk,am64xx-evm","icssg: due to FW bug both interfaces has to be loaded always",""
   "LCPD-19580","am654x-evm","am654- unable to select a mode (sdhci?)",""
   "LCPD-18665","am654x-evm,am654x-idk","Am65x Pg2: Board cannot do soft reboot when booting from SD card",""
   "LCPD-18297","am654x-evm","AM6: OV5640: 176x144 does not work",""
   "LCPD-17673","am654x-evm,am335x-evm,am43xx-gpevm,am571x-idk,am572x-idk,am574x-idk,am57xx-evm,beaglebone-black,dra71x-evm,dra72x-evm,dra7xx-evm,j721e-evm","No software documentation for the Timer module",""
   "LCPD-17449","am654x-evm,am654x-idk,am654x-hsevm,am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am43xx-epos,am43xx-gpevm,am43xx-hsevm,am437x-idk,am437x-sk,am571x-idk,am572x-idk,am574x-idk,am574x-hsidk,am57xx-evm,am57xx-beagle-x15,am57xx-hsevm,beaglebone,beaglebone-black,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm","libasan_preinit.o is missing in devkit",""
   "LCPD-16534","am654x-evm,am654x-idk","remoteproc/k3-r5f: PDK IPC echo_test image fails to do IPC in remoteproc mode on second run","None"


|

Issues opened in previous releases that were closed on this release
-------------------------------------------------------------------

.. csv-table::
   :header: "Record ID", "Title", "Platform"
   :widths: 15, 70, 20

   "LCPD-29872","PTP Time Synchronization needs to be restarted after link downs","am654x-evm,am654x-idk"
   "LCPD-29635","PCIe: x2 lane configuration is non functional","am654x-idk"
   "LCPD-29588","CPSW documentation: Time Sync Router no longer firewalled","am654x-evm,am654x-idk,am64xx-evm,am62xx_sk-fs,am62xx_sk-se,am62xx_lp_sk-fs,am62axx_sk-fs,am62xx-lp-sk,am62xx-sk,am64xx_sk-fs"
   "LCPD-29580","ICSSG IET Statistics are not getting counted","am654x-evm,am654x-idk,am64xx-evm"
   "LCPD-29446","Linux SDK docs should explicitly state what peripherals are supported","am654x-evm,am654x-idk,am64xx-evm,am62xx_sk-fs,am62xx_sk-se,am335x-evm,am335x-ice,am335x-sk,am43xx-gpevm,am437x-idk,am437x-sk,am62xx-sk,am64xx_sk-fs"
   "LCPD-29397","AM65x Linux SDK lists unsupported industrial protocols","am654x-evm,am654x-idk"
   "LCPD-28492","AM65: ICSSG: phc_ctl: Seeing clock jumps in get","am654x-evm,am64xx-evm"
   "LCPD-28107","Upstream: Broken USB boot modes on AM654","am654x-idk"
   "LCPD-25526","rproc_get() failure on certain race conditions","am654x-idk"
   "LCPD-25314","ICSSG: Timestamp for back-to-back with IPG < 100us not received","am654x-evm,am654x-idk,am654x-hsevm"
   "LCPD-25276","Kernel warning with panel_simple probe","am654x-evm,am654x-idk"
   "LCPD-24199","AM654x UART HWFLOW FUNC, PERF, STRESS tests fail (Impact 2)","am654x-evm"
   "LCPD-24127","AM654x IPSEC Software Crypto tests fail (Impact 4)","am654x-evm,j721e-idk-gw"
   "LCPD-22931","RemoteProc documentation missing","am654x-evm,am654x-idk,am64xx-evm,am64xx_sk-fs"
   "LCPD-22829","Convert toshiba,tc358767.txt:  ""toshiba,tc358767"" to yaml","am654x-evm,am654x-idk"
   "LCPD-22423","Removing FixMe and TODO from ICSSG Driver code","am654x-idk"
   "LCPD-20686","am65xx mainline build with dunfell is missing rproc test images","am654x-evm"
   "LCPD-19861","ICSSG: Unregistered multicast MAC packets are still visible in non-promiscuous mode","am654x-evm"
   "LCPD-19859","ETH ICSSG netperf benchmark returns lower performance than expected","am654x-evm"
   "LCPD-19177","u-boot:pytest: test_efi_helloworld_net failed on am6 and J7","am654x-evm,j721e-idk-gw"
   "LCPD-18788","Uboot: Could not bring up PCIe interface","am654x-idk"
   "LCPD-18627","uboot does not read the reserve-memory from the fdt ","am654x-idk"
   "LCPD-18289","pcie-usb tests sometimes fail","am654x-evm,k2g-evm"
   "LCPD-18258","IPSEC perfomance failures","am654x-evm,j721e-idk-gw"
   "LCPD-17798","2020 LTS: INTA/INTR smp_affinity failure and IRQ allocation issues.","am654x-evm,am654x-idk,j7am-evm,j721e-evm,j721e-hsevm,j721e-evm-ivi,j721e-idk-gw,j721e-vlab,j7200-evm,j7200-hsevm"
   "LCPD-16406","Seeing ""e1000#0: ERROR: Hardware Initialization Failed"" sometimes when do dhcp via pcie-eth","am654x-idk"
   "LCPD-15873","There is no dtbo in u-boot for PCIe x1 + usb3 daughter card","am654x-evm"
   "LCPD-14843","U-boot should support  default settings for netboot ","am654x-evm,am654x-idk"



|


Issues found and closed on this release that may be applicable to prior releases
--------------------------------------------------------------------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform"
   :widths: 15, 70, 20

   "LCPD-36968","am65x/debug: Display breaks with sysfw","am654x-evm,am654x-idk,am654x-hsevm"
   "LCPD-36947","AM65: eMMC/MMC tests fail","am654x-evm,am654x-idk"
   "LCPD-36914","am654: ICSSG Performance degradation","am654x-idk"
   "LCPD-36612","TMDX654IDKEVM: Clock jump of PTP device for ICSSG #2","am654x-idk"
   "LCPD-36578","AM65: USB hub on the daughter card does not work OOB ","am654x-evm,am654x-idk"
   "LCPD-36549","ICSSG: Ping to bridge not working in switch mode","am654x-idk,am64xx-hsevm"
   "LCPD-36517","TCP Performance Failure","am654x-idk"
   "LCPD-36510","BitBake Network Connectivity Check","am654x-hsevm"
   "LCPD-36403","Rx Stall during Uboot in presence of Broadcast Traffic","am654x-evm,am654x-idk"
   "LCPD-36325","MMC Error Getting Device Node","am654x-idk,j784s4-evm"
   "LCPD-34852","Few times payload is packed at size boundary by binman ","am654x-evm,am64xx-evm,am62xx_sk-se,j721e-idk-gw,j721s2-evm,j7200-evm"
   "LCPD-34593","DISTRO BOOT: Not enabled on all Sitara Platforms","am654x-evm,am654x-idk,am654x-hsevm,am64xx-evm,am64xx-hsevm,am62xx_sk-fs,beagleplay-gp,am62axx_sk-fs,am62xx-sk"
   "LCPD-34531","AM62a: eMMC LTP tests failure","am654x-evm,am62axx_sk-fs"
   "LCPD-34520","AM65: USB and PCIE DT overlays doesnt exist","am654x-evm,am654x-idk"
   "LCPD-34414","AM65: Missing k3-am654-pcie-usb3 from kirkstone build","am654x-evm"
   "LCPD-34413","RT Linux: Interrupt latency issue with >200us outliers","am654x-evm,am654x-hsevm,am64xx-hsevm,am64xx-hssk,am62xx_sk-fs,am62xx_lp_sk-fs,am62axx_sk-fs,am62xx-sk,am64xx_sk-fs,j721e-sk,j721s2-evm,j721s2_evm-fs,j7200-evm,j784s4-evm"
   "LCPD-34316","AM65x : ICSSG : Switching between Dual EMAC and Switch mode fails","am654x-idk"
   "LCPD-34125","AM65x Linux SDK : Missing ICSSG Performance numbers","am654x-evm,am654x-idk"
   "LCPD-32958","AM6xx/J7: Issue with MCSPI clocking in Linux driver","am654x-evm,am654x-idk,am654x-hsevm,am64xx-evm,am64xx-hsevm,am64xx-hssk,am62xx_sk-fs,am62xx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62axx_sk-fs,am62axx_sk-se,am62xx-lp-sk,am62xx-sk,am64xx_sk-fs"
   "LCPD-32946","RT Linux: PRU Ethernet link down causes kernel crash","am654x-evm,am654x-idk,am64xx-evm"
   "LCPD-32823","ICSS firmware does not process Rx packets once Min error frame is received","am654x-idk,am64xx-evm"
   "LCPD-32773","Rx stall seen when there is network traffic during startup","am654x-idk,am64xx-evm"

|

Installation and Usage
======================

The :ref:`Software Developer's Guide <linux-index>` provides instructions on how to setup up your Linux development
environment, install the SDK and start your development.  It also includes User's Guides for various Example Applications and Code
Composer Studio.

|

Host Support
============

The Processor SDK is developed, built and verified on Ubuntu |__LINUX_UBUNTU_VERSION_SHORT__|.


.. note::
   Processor SDK Installer is 64-bit, and installs only on 64-bit host
   machine. Support for 32-bit host is dropped as Linaro toolchain is
   available only for 64-bit machines

|
