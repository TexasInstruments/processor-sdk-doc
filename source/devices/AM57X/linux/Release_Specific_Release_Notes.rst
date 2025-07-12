.. _release-specific-release-notes:

*************
Release Notes
*************

Overview
========

The **Processor Software Development Kit (Processor-SDK) for Linux**
provides a fundamental software platform for development, deployment and
execution of Linux based applications and includes the following:

-  Bootloaders & Filesystems
-  SDK Installer
-  Setup Scripts
-  Makefiles
-  Example Applications

Licensing
=========

Please refer to the software manifest, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page. The manifest can be found on the SDK
download page or in the installed directory as indicated below. In
addition, see `GPLv3 Disclaimer <Overview_GPLv3_Disclaimer.html>`__

Documentation
=============

-  `Processor SDK Linux Software Developer's Guide <index.html>`__: Provides information on features, functions, delivery package and,
   compile tools for the Processor SDK Linux release. This also provides
   detailed information regarding software elements and software
   infrastructure to allow developers to start creating applications.
-  `Processor SDK Linux Getting Started Guide <Overview_Getting_Started_Guide.html>`__: Provides information on getting the software and running
   examples/demonstrations bundled in the SDK.
-  **Software Manifest**: Provides license information on software
   included in the SDK release. This document is in the release at
   ``[INSTALL-DIR]/docs``.
-  **EVM Quick Start Guide**: Provides information on hardware setup and
   running the demonstration application that is loaded on flash. This
   document is provided as part of the EVM kit.

Release 09.03.00
================

Released December 2024

.. rubric:: What's New
   :name: whats-new

Processor SDK 9.3 Release supports the following platforms:

  * AM570x
  * AM571x
  * AM572x
  * AM574x


Processor SDK 9.3 Release has following new features:

  * This is the Second release in the 2023 LTS stream 6.1 kernel, 2023.04 U-Boot and Yocto Kirkstone/4.0
  * Early Boot / Late Attach for remote cores
  * PRUETH Driver
  * SGX graphics updates

.. rubric::  Descoped SDK features from 9.3
   :name: descoped-sdk-features-from-9.3

#. CAL
#. Matrix GUI
#. IVA
#. libdce
#. H264 codec


.. _release-specific-sdk-components-versions:

.. rubric:: SDK Components & Versions
   :name: sdk-components-versions

+--------------------------+----------------------------+
| Component                | Version                    |
+==========================+============================+
| Linux Kernel             | 6.1 (2023 LTS)             |
+--------------------------+----------------------------+
| U-Boot                   | 2023.04                    |
+--------------------------+----------------------------+
| Yocto Project            | 4.0 (krikstone)            |
+--------------------------+----------------------------+
| ARM Toolchain (gcc)      | 11.4                       |
+--------------------------+----------------------------+
| Wayland                  | 1.20                       |
+--------------------------+----------------------------+
| GStreamer                | 1.20.7                     |
+--------------------------+----------------------------+
| QT5                      | 5.15.7                     |
+--------------------------+----------------------------+

|

Supported Platforms
===================
See `here <../../../linux/Release_Specific_Supported_Platforms_and_Versions.html>`__ for a list of supported platforms and links to more information.

|


Build Information
=================

.. _u-boot-release-notes:

U-Boot
------

| The U-Boot git repository, branch and commit id can be found below:
| Based on verson: 2023.04
| URL: git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2023.04
| Commit ID: 2bedcd265ca6de803c90505df5962cbd70cda611

|

.. _release-specific-build-information-kernel:

Kernel
------

.. _release-specific-build-information-linux-kernel:

.. rubric:: Linux Kernel
   :name: linux-kernel

| The kernel git repository, branch and commit id can be found below:
| Based on Version: 6.1
| URL: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.1.y
| Commit ID: e4e8b16e66f592749984b2d287e0479e93ef35b3

|

.. _release-specific-build-information-rt-linux-kernel:

.. rubric:: Real Time (RT) Linux Kernel
   :name: real-time-rt-linux-kernel

| The RT kernel git repository, branch and commit id can be found below:
| Based on:
| Kernel Version: 6.1
| RT Kernel Version: 6.1-rt62

| URL: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-rt-linux-6.1.y
| Commit ID: 9e8992fb839c642e3c20ee8ce69a30dbaae7f498

|

.. note::

   meta-tisdk Yocto layer contains additional patches for Kernel `here <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/tree/recipes-kernel/linux/linux-ti-staging?h=am57x-9.x&id=0eed214c0ff621f4d03700a647a1b4f1a02b5a7c>`__.


.. _release-specific-generic-kernel-release-notes:

.. rubric:: Generic Kernel Release Notes
   :name: generic-kernel-release-notes

| Generic kernel release notes from kernelnewbies.org can be found at:
  https://kernelnewbies.org/Linux_6.1
| Archived versions can be found at:
  http://kernelnewbies.org/LinuxVersions

|

Yocto
-----

.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: 417233481d8daa46633045fac358260d07cf1670 CI/CD Auto-Merger: cicd.kirkstone.202412111800

| Clone: git://git.yoctoproject.org/meta-ti
| Branch: kirkstone
| Release Tag: 09.03.06
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: f8ad2232a4e52b50aecc6c847ee7cfa24fc84070 ti-test: Add rng-tools

| Clone: git://git.yoctoproject.org/meta-arago
| Branch: kirkstone
| Release Tag: 09.03.06
|

.. rubric:: meta-tisdk
   :name: meta-tisdk

| Head Commit: 0eed214c0ff621f4d03700a647a1b4f1a02b5a7c tisdk-core-bundle: omap-a15: Add IPU firmware to prebuilt images

| Clone: git://git.ti.com/ti-sdk-linux/meta-tisdk.git
| Branch: am57x-9.x
|

Issues Tracker
==============

Issues closed on this release
-----------------------------
.. csv-table::
   :header: "Record ID", "Summary"
   :widths: 20, 80

   LCPD-37832,AM57x: Early boot fails

SDK Known Issues
----------------
.. csv-table::
   :header: "Record ID", "Platform", "Title"
   :widths: 25, 30, 100

   LCPD-35049,"am571x-idk, am572x-idk, am574x-hsidk, am574x-idk, am57xx-beagle-x15, am57xx-evm, am57xx-hsevm",General Information U-Boot User guide is not relevant to AM57
   LCPD-35314,"am571x-idk, am572x-idk, am574x-hsidk, am574x-idk, am57xx-beagle-x15, am57xx-evm, am57xx-hsevm","DOC: Kernel build instructions are incorrect, provides the wrong information for building K3 Arm64 architecture"
   LCPD-37747,"am571x-idk, am572x-idk, am574x-hsidk, am574x-idk, am57xx-beagle-x15, am57xx-evm, am57xx-hsevm",DOC: Ethernet Switch Instructions are not included
   LCPD-37745,"am571x-idk, am572x-idk, am574x-hsidk, am574x-idk, am57xx-beagle-x15, am57xx-evm, am57xx-hsevm",Deprecated Multimedia support is not clearly mentioned in our documentation
   LCPD-24682,"am57xx-evm",Timer - DUT time is deviating more than 0.0005
   LCPD-38702,"am571x-idk, am572x-idk, am574x-hsidk, am574x-idk, am57xx-beagle-x15, am57xx-evm, am57xx-hsevm",meta-arago: Unable to build gstreamer plugins
   LCPD-25295,"am57xx-evm",DRM test fails due to color mismatch between captured and golden videos
   LCPD-34691,"am571x-idk, am572x-idk, am574x-hsidk, am574x-idk, am57xx-beagle-x15, am57xx-evm, am57xx-hsevm","AM57x TIDL demos are already removed, need to remove heading in documentation"
   LCPD-34690,"am571x-idk, am572x-idk, am574x-hsidk, am574x-idk, am57xx-beagle-x15, am57xx-evm, am57xx-hsevm",Broken link in User guide for Linux SDK
   LCPD-34805,"am571x-idk, am572x-idk, am574x-hsidk, am574x-idk, am57xx-beagle-x15, am57xx-evm, am57xx-hsevm",Missing command entry in documentation for Cross-Compile Toolchain as well as broken Yocto build instructions
   LCPD-39022,"am572x-idk, am574x-idk, am57xx-evm, am57xx-hsevm",UART: test fails on am57x and kirkstone
   LCPD-42070,"am572x-idk, am57xx-beagle-x15, am654x-evm, am654x-hsevm, am654x-idk",SGX544: GLES 2 conformance issues (94% pass)
   LCPD-42072,"am335x-evm, am335x-hsevm, am335x-sk, am437x-idk, am437x-sk, am57xx-beagle-x15, am57xx-evm, am57xx-hsevm",SGX: EGL_EXT_image_dma_buf_import_modifiers missing
   LCPD-37833,"am571x-idk, am572x-idk, am574x-hsidk, am574x-idk",ICSS-M: RSTP offload bug introduced with HSR/PRP
   LCPD-38034,"am571x-idk, am572x-idk, am574x-hsidk, am574x-idk, am57xx-beagle-x15, am57xx-evm",configs/processor-sdk-linux/processor-sdk-linux-09_02_00.txt is missing from the arago project repo
   LCPD-34948,"am571x-idk, am57xx-beagle-x15, am57xx-evm, am57xx-hsevm",DOC: There is no entry for CSI2 under kernel driver
   LCPD-38439,"am574x-idk",AM57X taking old function names for the McSPI
   LCPD-39354,"am571x-idk",timer16 is throwing EINVAL error in kernel boot
   LCPD-42139,"am571x-idk",USB Core Hangs during kernel boot on AM571X-idk
   LCPD-42167,"am335x-evm, am437x-sk, am571x-idk, am572x-idk, am62xx_sk-fs, am64xx-evm, am64xx_sk-fs, am654x-idk, beaglebone-black",PRU RPMsg swaps which message is sent to which core
   LCPD-42168,"am572x-idk","AM572x_IDK boot issue, expects wrong dtb name and does not follow 6.1 convention"
   LCPD-37226,"am335x-evm, am335x-hsevm, am335x-ice, am335x-sk, am437x-idk, am437x-sk, am43xx-gpevm, am43xx-hsevm, am571x-idk",Update Ubuntu Host version in Linux documentation

|

.. _release-specific-linux-kernel-known-issues:

Linux Kernel Known Issues
-------------------------
.. csv-table::
   :header: "Record ID", "Priority", "Title", "Component", "Subcomponent", "Platform", "Workaround", "Impact"
   :widths: 5, 10, 70, 10, 5, 20, 35, 20

   LCPD-18676,P4-Low,Some Uboot upstream Pytests failed on am5,Baseport,,am57xx-evm,,
   LCPD-18869,P3-Medium,PRUETH driver unstable if DUT is spammed with specific traffic,Connectivity,PRUSS/ETH,"am572x-idk, am574x-idk",,
   LCPD-18070,P3-Medium,usb: device: support custom builds for full speed tests,System Test,USBCLIENT,"am654x-evm, am335x-evm, am335x-hsevm, am335x-sk, am43xx-epos, am43xx-gpevm, am43xx-hsevm, am437x-sk, am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-beagle-x15, am57xx-hsevm, beaglebone, beaglebone-black, dra71x-evm, dra71x-hsevm, dra72x-evm, dra72x-hsevm, dra76x-evm, dra76x-hsevm, dra7xx-evm, dra7xx-hsevm, omapl138-lcdk",,
   LCPD-17673,P3-Medium,No software documentation for the Timer module,Baseport,Timers,"am654x-evm, am335x-evm, am43xx-gpevm, am571x-idk, am572x-idk, am574x-idk, am57xx-evm, beaglebone-black, dra71x-evm, dra72x-evm, dra7xx-evm, j721e-evm",,
   LCPD-19260,P3-Medium,PRUETH: Single EMAC doesn't ping with ICSS-1 Port 2 (MII-1),Connectivity,,am571x-idk,,
   LCPD-19596,P3-Medium,cpsw: switchdev: fix case when brX has MAC assigned,Connectivity,"CPSW, ETHERNET, ETHERNETSWITCH, Network",am571x-idk,,
   LCPD-15864,P3-Medium,SoC Performance Monitoring tool is still not enabled,Graphics,,am57xx-evm,,
   LCPD-9481,P5-Not Prioritized,Sometime the system hangs while loading the rpmsg rpc modules,IPC,RPMSG-RPC,"am571x-idk, am572x-idk, am57xx-evm, am57xx-hsevm",,
   LCPD-24506,P5-Not Prioritized,simulates touch events using Tapbot failed,System Test,,am57xx-evm,,
   LCPD-24505,P3-Medium,KMS properties test failed,Baseport,Display,"am43xx-gpevm, am57xx-evm",,
   LCPD-24626,P3-Medium,"""Verify kernel boots 100 times successfully using SD card"" fails",System Test,boot,"am335x-evm, am57xx-evm",,
   LCPD-24728,P3-Medium,Power measurement with Standby/Suspend/Resume failure,Baseport,Power_Management,"am335x-evm, am43xx-gpevm, am57xx-evm",,
   LCPD-24463,P4-Low,HSR/PRP: Root cause NetJury issues with HSR/PRP with RBX and VDAN node,Connectivity,,"am571x-idk, am572x-idk",,
   LCPD-24719,P4-Low,GStreamer crashes,Baseport,,am57xx-evm,,
   LCPD-24648,P3-Medium,Move dma-heaps-test and ion-tests to TI repositories,System Test,,"am64xx-evm, am335x-evm, am572x-idk, dra71x-evm, j721e-evm, j7200-evm",,
   LCPD-24818,P4-Low,AM57x: Warnings during HS device boot,Baseport,,am574x-hsidk,,
   LCPD-24251,P3-Medium,LTP Linux System Calls failed,Baseport,,"am43xx-gpevm, am57xx-evm",,
   LCPD-24590,P4-Low,cannot load such file -- wx,System Test,DRM,am57xx-evm,,
   LCPD-24456,P3-Medium,Move IPC validation source from github to git.ti.com,Baseport,IPC,"am654x-evm, am654x-idk, am654x-hsevm, am64xx-evm, am64xx-hsevm, am62xx_sk-fs, am62xx_sk-se, am62xx_lp_sk-fs, am62xx_lp_sk-se, am62axx_sk-fs, am335x-evm, am335x-hsevm, am335x-ice, am335x-sk, am43xx-epos, am43xx-gpevm, am43xx-hsevm, am437x-idk, am437x-sk, am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-beagle-x15, am57xx-hsevm, am62xx-sk, am64xx_sk-fs, beaglebone, bbai, beaglebone-black, dra71x-evm, dra71x-hsevm, dra72x-evm, dra72x-hsevm, dra76x-evm, dra76x-hsevm, dra7xx-evm, dra7xx-hsevm, j721e-hsevm, j721e-idk-gw, j721e-sk, j721s2-evm, j721s2-hsevm, j721s2_evm-fs, j7200-evm, j7200-hsevm, omapl138-lcdk",,
   LCPD-34757,P5-Not Prioritized,Am572x IDK fails boot on 6.1 cicd due to DRM issues,Baseport,,am572x-idk,,
   LCPD-34377,P2-High,kirkstone/6.1: am57x builds fail due to ipcdev,Baseport,,"am57xx-evm, dra7xx-evm, dra7xx-hsevm",,
   LCPD-37495,P5-Not Prioritized,Missing wayland-ivi-extension from packages,Graphics,,am57xx-evm,,
   LCPD-36742,P3-Medium,AM57x: CONFIG_NL80211_TESTMODE is not =y,Connectivity,,am57xx-evm,,
   LCPD-36792,P2-High,Capability Gap: usbgadgetfbs,System Test,farm,am57xx-evm,,
   LCPD-37131,P3-Medium,aes-128-ecb_throughput_16_bytes out of expected range,Baseport,"Crypto, SHA",am57xx-evm,,
   LCPD-37062,P2-High,Capability Gap: power,System Test,farm,am57xx-evm,,
   LCPD-36752,P3-Medium,AM57x: Module galcore not found,Graphics,,am57xx-evm,,
   LCPD-37648,P5-Not Prioritized,Dual camera Demo,Baseport,,am57xx-evm,,
   LCPD-37643,P5-Not Prioritized,GPIO driver shall disable a GPIO module when all the pins of this GPIO module are inactive (clock gating forced at module level).,Baseport,,am57xx-evm,,
   LCPD-37631,P5-Not Prioritized,Support for configuring Color Space Conversion (CSC) from user space,Audio & Display,,am57xx-evm,,
   LCPD-37715,P5-Not Prioritized,InCorrect DTB used in testing,Baseport,,am57xx-evm,,
   LCPD-37428,P5-Not Prioritized,FAT driver part of the eMMC-boot functionality of ROM code can only read a limited amount of entries of the FAT table,Baseport,ROM_Boot,"am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-beagle-x15, am57xx-hsevm",,
   LCPD-37241,P3-Medium,NBench performance is below par in 9.1 SDK when compared to the previous release 8.2,Baseport,CPU,am57xx-evm,,
   LCPD-37629,P3-Medium,DSS: support Writeback capture mode,Audio & Display,,am57xx-evm,,
   LCPD-15402,P5-Not Prioritized,rpmsg-rpc: test application does not bail out gracefully upon error recovery,IPC,"DSP_remoteproc, IPU_remoteproc","am571x-idk, am572x-idk, am574x-idk, am57xx-evm, am57xx-beagle-x15, dra71x-evm, dra72x-evm, dra76x-evm, dra7xx-evm",,
   LCPD-15400,P4-Low,remoteproc/omap: System suspend fails for IPU1 domain without any remoteprocs loaded,IPC,IPU_remoteproc,"am571x-idk, am572x-idk, am574x-idk, am57xx-evm, am57xx-beagle-x15, dra71x-evm, dra72x-evm, dra76x-evm, dra7xx-evm",,
   LCPD-16642,P3-Medium,"omapdrm: in some cases, DPI output width does not need to be divisible by 8",Baseport,Display,"am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-beagle-x15, am57xx-hsevm, dra71x-evm, dra71x-hsevm, dra72x-evm, dra72x-hsevm, dra76x-evm, dra76x-hsevm, dra7xx-evm, dra7xx-hsevm",,
   LCPD-24865,P4-Low,exception while building run-full-tests for am57xx form Jenkins,System,,am57xx-evm,,
   LCPD-25324,P5-Not Prioritized,remoteproc/omap: messageq_fault firmware image does not work for DSP1,IPC,Firmware,"am571x-idk, am572x-idk, am574x-idk, am57xx-evm, am57xx-beagle-x15",,
   LCPD-25323,P3-Medium,remoteproc/omap: circular lockdep being reported on some runs with rpmsg-proto recovery testing,IPC,"DSP_remoteproc, IPU_remoteproc","am571x-idk, am572x-idk, am574x-idk, am57xx-evm, am57xx-beagle-x15",,
   LCPD-25295,P3-Medium,DRM test fails due to color mismatch between captured and golden videos,"Audio & Display, System Test",DRM,am57xx-evm,,
   LCPD-25571,P3-Medium,GPIO EDGE_ALL_BANK test fails,Baseport,GPIO,am57xx-evm,,
   LCPD-25570,P3-Medium,GST Decode Tests fails,Baseport,CAPTURE,am57xx-evm,,
   LCPD-25554,P3-Medium,VIP: V4L2 Capture test fails with one or more compliance tests,Connectivity,VIP,am57xx-evm,,
   LCPD-25537,P3-Medium,VIP: unable to get reference files,Connectivity,VIP,am57xx-evm,,
   LCPD-25532,P3-Medium,VIP: Failed to load vivid module,Connectivity,VIP,am57xx-evm,,
   LCPD-25533,P2-High,VIP capture + scaling Test failure,"Connectivity, System Test",VIP,am57xx-evm,,
   LCPD-10726,P3-Medium,Update DDR3 emif regs structure for EMIF2 for the beagle_x15 board in U-Boot board file,Baseport,,"am572x-idk, am57xx-evm",None,
   LCPD-36396,P3-Medium,Instructions for taking the C66 out of reset do not work,Baseport,,"am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-beagle-x15, am57xx-hsevm",,
   LCPD-37497,P5-Not Prioritized,No SATA device detected,Baseport,"SATA, UBoot",am57xx-evm,,
   LCPD-37553,P5-Not Prioritized,USB host driver shall support selective suspend FAILS,Connectivity,USB,am57xx-evm,,
   LCPD-37555,P5-Not Prioritized,"DSS: Failed: Measured op + pause time is 16.88, expected at least 17.0 sec delay",Audio & Display,DSS,am57xx-evm,,
   LCPD-37269,P3-Medium,Capability Gap: ptp,System Test,farm,"am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-hsevm",,
   LCPD-6075,P5-Not Prioritized,BUG: using smp_processor_id() in preemptible [00000000] code during remoteproc suspend/resume,"Baseport, IPC",,"am572x-idk, am57xx-evm, dra7xx-evm",,

|

.. _release-specific-rt-linux-kernel-known-issues:

RT Linux Kernel Known Issues
----------------------------

.. csv-table::
   :header: "Record ID", "Priority", "Title", "Component", "Platform", "Workaround"
   :widths: 5, 10, 70, 10, 20, 15

   LCPD-6663 ,P3-Medium ,[RT] Kmemleak is buggy and boot is crashed randomly ,Baseport ,  ,
   LCPD-7623 ,P3-Medium ,Seeing SPI transfer failed error sometimes on k2hk when using rt kernel ,Connectivity ,k2hk-evm ,
   LCPD-11586 ,P3-Medium ,dhcp failed to get IP address after reboot for K2G-ICE non-RT linux ,Baseport  ,"k2g-ice ",

|

.. _sdk-features-descoped-from-9-3-release:

SDK features descoped from 9.3 release
--------------------------------------

.. csv-table::
  :header: "ID", "Head Line", "Components", "Sub-Components", "Platform"
  :widths: 20, 90, 30, 30, 90

	PLSDK-2583,ICSS Ethernet Support - Standard Dual EMAC Ethernet,Connectivity,PRUSS/ETH,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-hsidk, am574x-idk, k2g-ice"
	PLSDK-2570,Include video-graphics-test application in Matrix GUI launcher,"Audio & Display, Graphics","DSS, GC320, QT, SGX, VIP","am570x-evm, am571x-idk, am572x-evm, am572x-hsevm, am572x-idk, am574x-hsidk, am574x-idk, dra76x-evm"
	PLSDK-1403,omapdrmtest example application in PLSDK,Multimedia,"Capture, Display, VIP","am570x-evm, am571x-idk, am572x-evm, am572x-idk, am574x-idk"
	LCPD-20532,AM57 HSR and PRP driver improvements,Connectivity,"HSR, PRUSS/ETH","am571x-idk, am572x-idk, am574x-idk"
	LCPD-18760,ICSS-M: RSTP: Linux shall support PTP TC,Connectivity,"PRUSS/ETH, PTP, RSTP",am571x-idk
	LCPD-18759,ICSS-M: HSR/PRP: Linux shall support PTP Boundary Clock with 3/4/5-leg configurations,Connectivity,"HSR-PRP, PRUSS/ETH, PTP","am571x-idk, am572x-idk, am574x-idk"
	LCPD-18468,ICSS-M: Support multicast filtering on RSTP switch implementation,Connectivity,"PRUSS/ETH, RSTP","am571x-idk, am572x-idk, am574x-idk"
	LCPD-17686,ICSS-M: Support run time Ethernet protocol switching,Connectivity,"HSR-PRP, PRUSS/ETH, RSTP","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17510,"ICSS-M: Support 2 instances of HSR, PRP and/or EMAC, with offload",Connectivity,"HSR-PRP, PRUSS/ETH",am571x-idk
	LCPD-17509,ICSS-M: Support SNMP Agent for IEC62439 specified MIBs (HSR/PRP),Connectivity,"HSR-PRP, PRUSS/ETH","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17508,ICSS-M: Support storm prevention in HSR/PRP,Connectivity,"HSR-PRP, PRUSS/ETH","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17507,ICSS-M: Support multicast filtering on HSR/PRP,Connectivity,"HSR-PRP, PRUSS/ETH","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17506,ICSS-M: Support VLAN filtering on HSR/PRP,Connectivity,"HSR-PRP, PRUSS/ETH","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17505,ICSS-M: Support VLAN on HSR/PRP,Connectivity,"HSR-PRP, PRUSS/ETH","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17503,ICSS-M: PPS performance for small-size packets for HSR/PRP implementation,Connectivity,"HSR-PRP, PRUSS/ETH","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17501,ICSS-M: MTU frame performance for HSR/PRP implementation,Connectivity,"HSR-PRP, PRUSS/ETH","am571x-idk, am572x-idk, am574x-idk"
	LCPD-17500,Run NetJury test for HSR/PRP protocol compliance,Connectivity,"HSR-PRP, PRUSS/ETH",am572x-idk
	LCPD-17499,ICSS-M: Support HSR/PRP protocol functionality via HSR/PRP firmware,Connectivity,PRUSS/ETH,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk, k2g-ice"
	LCPD-17498,ICSS-M: HSR/PRP Ethernet,Connectivity,"HSR-PRP, PRUSS/ETH","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17467,ICSS-M: RSTP: Linux shall support PTP OC(slave and master),Connectivity,"PRUSS/ETH, RSTP",am571x-idk
	LCPD-17466,ICSS-M: Support RSTP switch,Connectivity,"PRUSS/ETH, RSTP","am571x-idk, am574x-idk, am574x-hsidk"
	LCPD-17465,ICSS-M: Dual EMAC: Linux shall support PTP E2E and UDP transport (Telecom Profile),Connectivity,"PRUSS/ETH, PTP","am571x-idk, am572x-idk, am574x-idk"
	LCPD-17464,ICSS-M: Dual EMAC: Linux shall support PTP over VLAN,Connectivity,"PRUSS/ETH, PTP","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17463,ICSS-M: HSR/PRP: Linux shall support PTP over VLAN,Connectivity,"HSR-PRP, PRUSS/ETH, PTP","am571x-idk, am572x-idk, am574x-idk"
	LCPD-17462,ICSS-M: Dual EMAC: Linux shall support PPS generation by ICSS IEP,Connectivity,"PRUSS/ETH, PTP","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17461,ICSS-M: HSR/PRP: Linux shall support PPS generation by ICSS IEP,Connectivity,"HSR-PRP, PRUSS/ETH, PTP","am571x-idk, am572x-idk, am574x-idk"
	LCPD-17459,ICSS-M: Dual EMAC: Linux shall support PTP Boundary Clock with 3/4/5-leg configurations,Connectivity,"HSR-PRP, PRUSS/ETH, PTP","am571x-idk, am572x-idk, am574x-idk"
	LCPD-17458,ICSS-M: HSR/PRP: Linux shall support PTP OC (slave/master),Connectivity,"HSR-PRP, PRUSS/ETH, PTP","am335x-ice, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17457,ICSS-M: HSR: Linux shall support PTP TC,Connectivity,"HSR-PRP, PRUSS/ETH, PTP","am335x-ice, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17456,ICSS-M: Dual EMAC: Linux shall support PTP OC (slave/master),Connectivity,"PRUSS/ETH, PTP","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17454,ICSS-M: Support VLAN filtering using Dual EMAC firmware,Connectivity,PRUSS/ETH,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17453,ICSS-M: Support storm prevention in DualEMAC,Connectivity,PRUSS/ETH,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17452,ICSS-M: Support multicast filtering on Dual EMAC implementation,Connectivity,PRUSS/ETH,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17450,ICSS-M: PPS performance for small-size packets for DualEMAC implementation,Connectivity,PRUSS/ETH,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17448,ICSS-M: ethernet performance for Dual EMAC,Connectivity,PRUSS/ETH,"am571x-idk, am572x-idk, am574x-idk"
	LCPD-10725,16 bit RAW video capture,Audio & Display,"Capture, VIP","am571x-idk, am572x-idk, am57xx-evm, am57xx-hsevm"
	LCPD-10439,PRUETH driver must support a single PHY instead of requiring 2,Connectivity,PRUSS/ETH,"am654x-evm, am654x-idk, am654x-hsevm, am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk, am574x-hsidk"
	LCPD-10307,PRU Ethernet driver shall support placing the interface in promiscuous mode,Connectivity,PRUSS/ETH,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, k2g-ice"
	LCPD-9738,PRUSS/ETH: Support transmission and reception of VLAN tagged packets,Connectivity,PRUSS/ETH,"am654x-evm, am654x-idk, am654x-hsevm, am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, k2g-ice"
	LCPD-9729,Add Linux bridge support over PRU Switch ports,Connectivity,"Ethernet, PRUSS/ETH","am335x-ice, am437x-idk, am571x-idk, am572x-idk, k2g-ice"
	LCPD-9701,Add flexibility to run different Ethernet protocols on a PRU ICSS,Connectivity,PRUSS/ETH,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, k2g-ice"
	LCPD-8407,PRU Kernel Eth driver to work with Profinet firmware,Connectivity,"PRUSS-Ethernet, PRUSS/ETH","am335x-ice, am437x-idk, am571x-idk, am572x-idk, k2g-ice"
	LCPD-7814,VIP 8 bit capture support,Audio & Display,"Capture, VIP","am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-hsevm, dra71x-evm, dra71x-hsevm, dra72x-evm, dra72x-hsevm, dra76x-evm, dra76x-hsevm, dra7xx-evm, dra7xx-hsevm"
	LCPD-7221,ICSS Ethernet Support - UIO co-exist with Kernel Ethernet Driver,"Connectivity, IPC",PRUSS/ETH,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, k2g-ice"
	LCPD-6431,Support format conversion to RGB by VIP driver,Audio & Display,"Capture, VIP",am57xx-evm
	LCPD-6320,ICSS Ethernet Support - AM571x IDK: Support 6-port Ethernet configuration co-existing with CPSW,Connectivity,PRUSS/ETH,am571x-idk
	LCPD-5710,ICSS Ethernet Support - Standard Switch Ethernet,Connectivity,"ETHERNET, PRUSS/ETH","am571x-idk, am572x-idk, am57xx-evm"
	LCPD-5553,AM57xx VIP driver color space conversion support,Audio & Display,"Capture, VIP","am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm"
	LCPD-5505,ICSS Ethernet Support - RT Use Case - UIO,Connectivity,PRUSS/ETH,"am571x-idk, am572x-idk, am57xx-evm"
	LCPD-5450,ICSS Ethernet Support - Standard Dual EMAC Ethernet,Connectivity,PRUSS/ETH,"am437x-idk, am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, k2g-ice"
	LCPD-5254,Scaler support in VIP driver,Audio & Display,"CAPTURE, VIP","am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-hsevm, dra71x-evm, dra71x-hsevm, dra72x-evm, dra72x-hsevm, dra76x-evm, dra76x-hsevm, dra7xx-evm, dra7xx-hsevm"
	IVIREQ-649,V4L2 raw mode 12bit for VIP/CSI2 on J6 platform,"Camera, Drivers","CSI2, VIP","dra71x-evm, dra7xx-evm"

|

.. rubric:: Installation and Usage
   :name: installation-and-usage

The `Software Developer's Guide <index.html>`__ provides instructions on how to setup up your Linux development
environment, install the SDK and start your development.  It also includes User's Guides for various Example Applications and Code
Composer Studio.

|

.. rubric:: Host Support
   :name: host-support

The Processor SDK is developed, built and verified on Ubuntu 16.04 and 18.04. Details on how to create a virtual machine to load Ubuntu
are described in `this page <How_to_Guides/Host/How_to_Build_a_Ubuntu_Linux_host_under_VMware.html>`__.


.. note::
   Processor SDK Installer is 64-bit, and installs only on 64-bit host
   machine. Support for 32-bit host is dropped as Linaro toolchain is
   available only for 64-bit machines

|
