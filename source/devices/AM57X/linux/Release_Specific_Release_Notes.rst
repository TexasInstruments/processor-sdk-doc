.. _release-specific-release-notes:

*************
Release Notes
*************

Overview
========

The **Processor Software Development Kit (Processor-SDK) for Linux**
provides a fundamental software platform for development, deployment and
execution of Linux based applications and includes the following:

-  Bootloaders and Filesystems
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

Release 11.01.00
================

Released October 2025

.. rubric:: What's New
   :name: whats-new

Processor SDK 11.01 Release supports the following platforms:

  * AM570x
  * AM571x
  * AM572x
  * AM574x


Processor SDK 11.01 Release has following new features:

  * This is the first release in the 2025 LTS stream 6.12 kernel, 2025.01 U-Boot and Yocto Scarthgap/5.0

.. warning::

   This will be the last LTS SDK release for AM57x devices.

.. rubric::  Descoped SDK features from 11.01
   :name: descoped-sdk-features-from-11.01

#. CAL
#. Matrix GUI
#. IVA
#. libdce
#. H264 codec
#. Multimedia
#. glsdk-example-applications is deprecated due to dependency on deprecated
   libkms library.
#. gstreamer1.0-plugins-ducati and gstreamer1.0-plugins-vpe due to dependency on
   deprecated library
#. Example applications: dual-camera, evse, mmwavegesture, refresh-screen,
   pdm-anomaly-detection are deprecated due to dependency on Matrix GUI/QT5
   which is no longer supported with Scarthgap.


.. _release-specific-sdk-components-versions:

.. rubric:: SDK Components & Versions
   :name: sdk-components-versions

+--------------------------+----------------------------+
| Component                | Version                    |
+==========================+============================+
| Linux Kernel             | 6.12 (2025 LTS)            |
+--------------------------+----------------------------+
| U-Boot                   | 2025.01                    |
+--------------------------+----------------------------+
| Yocto Project            | 5.0 (Scarthgap)            |
+--------------------------+----------------------------+
| ARM Toolchain (gcc)      | 13.4.0                     |
+--------------------------+----------------------------+
| Wayland                  | 1.22.0                     |
+--------------------------+----------------------------+
| GStreamer                | 1.22.12                    |
+--------------------------+----------------------------+
| QT6                      | 6.9.3                      |
+--------------------------+----------------------------+

|

Supported Platforms
===================
See `here <../../../linux/Release_Specific_Supported_Platforms_and_Versions.html>`__ for a list of supported platforms and links to more information.

|

.. _release-specific-build-information:

Build Information
=================

.. _u-boot-release-notes:

U-Boot
------

| The U-Boot git repository, branch and commit id can be found below:
| Based on verson: 2025.01
| URL: git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| Commit ID: 3c06cd621447331aeab0bbb2e5c063a2b1d79d1b

|

.. note::

   meta-tisdk Yocto layer contains additional patches for U-Boot `here <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/tree/meta-ti-foundational/recipes-bsp/u-boot/u-boot-ti-staging?h=am57x>`__.


.. _release-specific-build-information-kernel:

Kernel
------

.. _release-specific-build-information-linux-kernel:

.. rubric:: Linux Kernel
   :name: linux-kernel

| The kernel git repository, branch and commit id can be found below:
| Based on Version: 6.12
| URL: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Commit ID: af3896fca24b7945db015d2ac411ef50e93a11c9

|

.. _release-specific-build-information-rt-linux-kernel:

.. rubric:: Real Time (RT) Linux Kernel
   :name: real-time-rt-linux-kernel

| The RT kernel git repository, branch and commit id can be found below:
| Based on:
| Kernel Version: 6.12

| URL: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-rt-linux-6.12.y-arm32
| Commit ID: 4235794ce373baf55d9ff5cf920b1d44b7e31455

|

.. note::

   meta-tisdk Yocto layer contains additional patches for Kernel `here <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/tree/meta-ti-foundational/recipes-kernel/linux/linux-ti-staging?h=am57x>`__.


.. _release-specific-generic-kernel-release-notes:

.. rubric:: Generic Kernel Release Notes
   :name: generic-kernel-release-notes

| Generic kernel release notes from kernelnewbies.org can be found at:
  https://kernelnewbies.org/Linux_6.12
| Archived versions can be found at:
  http://kernelnewbies.org/LinuxVersions

|

Yocto
-----

.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: 0e2876e2ea7c28ddff5bc0052bdbc83dd07b7c98 CI/CD Auto-Merger: cicd.scarthgap.202509111148

| Clone: git://git.yoctoproject.org/meta-ti
| Branch: scarthgap
| Release Tag: 11.01.13
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: 67c473bc6d88a2cce13b2e8c36fcb79cb0015339 CI/CD Auto-Merger: cicd.scarthgap.20250911114

| Clone: git://git.yoctoproject.org/meta-arago
| Branch: scarthgap
| Release Tag: 11.01.13
|

.. rubric:: meta-tisdk
   :name: meta-tisdk

| Head Commit: 982761ae3031c12ab7c270fb4e91b15198795299 systemd: add system clock drift service

| Clone: git://git.ti.com/ti-sdk-linux/meta-tisdk.git
| Branch: am57x
|

Issues Tracker
==============

Issues closed on this release
-----------------------------
.. csv-table::
   :header: "Record ID", "Summary"
   :widths: 20, 80

   "LCPD-37832","AM57x: Early boot fails"
   "LCPD-43533","EGLFS not releasing buffers when using clones"
   "LCPD-43532","SGX: Hardfloat compiler selection"
   "LCPD-43003","libdce SRC_URI points to a dead link"
   "LCPD-42783","Display  DRM warning"
   "LCPD-42635","9.3 Documentation has outdated message under Host support"
   "LCPD-43931","Dhrystone performance report contains wrong cpu frequency"
   "LCPD-42168","AM572x_IDK boot issue, expects wrong dtb name and does not follow 6.1 convention"
   "LCPD-39058","[Upstream] omap-iommu: Driver needs to adapt to framework change since v6.7"
   "LCPD-38702","meta-arago: Unable to build gstreamer plugins"
   "LCPD-37833","ICSS-M: RSTP offload bug introduced with HSR/PRP"
   "LCPD-37745","DOC:  Deprecated Multimedia support is not clearly mentioned in our documentation"
   "LCPD-37715","InCorrect DTB used in testing"
   "LCPD-37631","Support for configuring Color Space Conversion (CSC) from user space"
   "LCPD-37555","DSS: Failed: Measured op + pause time is 16.88, expected at least 17.0 sec delay"
   "LCPD-37226","Update Ubuntu Host version in Linux documentation"
   "LCPD-37131","aes-128-ecb_throughput_16_bytes out of expected range"
   "LCPD-35314","DOC: Kernel build instructions are incorrect, provides the wrong information for building K3 Arm64 architecture"
   "LCPD-35049","DOC: Section 3.1.1.1. General Information U-Boot User guide is not relevant to AM57"
   "LCPD-34805","Missing command entry in documentation for Cross-Compile Toolchain as well as broken Yocto build instruccions"
   "LCPD-34804","DOC: Broken Link in Getting Started page Building the SDK"
   "LCPD-25533","VIP capture + scaling Test failure"
   "LCPD-24302","Speed test built in to OpenSSL Cryptographic - performance failures"
   "LCPD-17673","No software documentation for the Timer module"
   "LCPD-42797","AM57x: ICSSM Dual EMAC support"
   "LCPD-43525","AM57x: ICSSM Switch Support"
   "LCPD-43526","AM57x: ICSSM HSR Support"
   "LCPD-43527","AM57x: ICSSM PRP Support"

SDK Known Issues
----------------
.. csv-table::
   :header: "Record ID", "Platform", "Title"
   :widths: 25, 30, 100

   "LCPD-44987","am57xx-evm","glsdk is removed from scratch gap "
   "LCPD-44886","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm","U-boot patch for Linux addressing AM57xx errata i2446"
   "LCPD-44484","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm","DSS Kernel Documentation is not present"
   "LCPD-44346","am335x-evm,am437x-sk,am57xx-evm,am654x-evm","SGX: RGB565 texture and scanout conformance"
   "LCPD-43870","am57xx-evm","am57xx-evm pg1.1 boards fail to boot with 11.00 RC12 image"
   "LCPD-43555","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm","9.3 Documentation IPC for AM57xx has TODOs in sections"
   "LCPD-42841","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm","9.3 Documentation GCC_Toolchain instructions do not work"
   "LCPD-42698","am572x-idk,am57xx-evm","AM57x: Etnaviv GPU driver causes the Kernel to hang in race conditions"
   "LCPD-42680","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm","32 bit processors should document y2038"
   "LCPD-42484","am57xx-evm","SDK 9.3 RC6: CPU freq test , Some perf (wheatstone and Dhrystone) failure"
   "LCPD-42167","am335x-evm,am437x-sk,am571x-idk,am572x-idk,am62xx_sk-fs,am64xx-evm,am64xx_sk-fs,am654x-idk,beaglebone-black","PRU RPMsg swaps which message is sent to which core"
   "LCPD-42139","am571x-idk","USB Core Hangs during kernel boot on AM571X-idk"
   "LCPD-42072","am335x-evm,am335x-hsevm,am335x-sk,am437x-idk,am437x-sk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am654x-evm,am654x-hsevm,am654x-idk","SGX: EGL_EXT_image_dma_buf_import_modifiers missing"
   "LCPD-42070","am572x-idk,am57xx-beagle-x15,am654x-evm,am654x-hsevm,am654x-idk","SGX544: GLES 2 conformance issues (94% pass)"
   "LCPD-39354","am571x-idk","timer16 is throwing EINVAL error in kernel boot"
   "LCPD-39022","am572x-idk,am574x-idk,am57xx-evm,am57xx-hsevm","UART: test fails on am57x and kirkstone"
   "LCPD-37920","am335x-evm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-gpevm,am571x-idk,am572x-idk,am574x-idk,am57xx-evm,am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_p0_sk-fs,am62xx_sk-fs,am64xx-evm,am64xx_sk-fs,am654x-evm,am654x-idk","ti-rpmsg-char should use the same toolchain as current Yocto build"
   "LCPD-37747","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm","DOC:  Ethernet Switch Instructions are not included"
   "LCPD-37648","am57xx-evm","Dual camera Demo "
   "LCPD-37643","am57xx-evm","GPIO driver shall disable a GPIO module when all the pins of this GPIO module are inactive (clock gating forced at module level)."
   "LCPD-37497","am57xx-evm","No SATA device detected"
   "LCPD-37428","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm","FAT driver part of the eMMC-boot functionality of ROM code can only read a limited amount of entries of the FAT table"
   "LCPD-37241","am57xx-evm","NBench performance is below par in 9.1 SDK  when compared to the previous release 8.2"
   "LCPD-36742","am57xx-evm","AM57x: CONFIG_NL80211_TESTMODE is not =y "
   "LCPD-36655","am57xx-evm","AM57x: Unable to load vpe modules"
   "LCPD-36396","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm","Instructions for taking the C66 out of reset do not work"
   "LCPD-25571","am57xx-evm","GPIO EDGE_ALL_BANK test fails"
   "LCPD-25570","am57xx-evm","GST Decode Tests fails"
   "LCPD-25333","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm","remoteproc: failure to stop a suspended processor"
   "LCPD-25324","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm","remoteproc/omap: messageq_fault firmware image does not work for DSP1"
   "LCPD-25323","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm","remoteproc/omap: circular lockdep being reported on some runs with rpmsg-proto recovery testing"
   "LCPD-24818","am574x-hsidk","AM57x: Warnings during HS device boot"
   "LCPD-24728","am335x-evm,am43xx-gpevm,am57xx-evm","Power measurement with Standby/Suspend/Resume failure"
   "LCPD-24719","am57xx-evm","GStreamer crashes"
   "LCPD-24682","am57xx-evm","Timer - DUT time is deviating more than 0.0005"
   "LCPD-24648","am335x-evm,am572x-idk,am64xx-evm,dra71x-evm,j7200-evm,j721e-evm","Move dma-heaps-test and ion-tests to TI repositories"
   "LCPD-24626","am335x-evm,am57xx-evm","""Verify kernel boots 100 times successfully using SD card"" fails"
   "LCPD-24506","am57xx-evm","simulates touch events using Tapbot failed"
   "LCPD-24456","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-epos,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am62axx_sk-fs,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am64xx-evm,am64xx-hsevm,am64xx_sk-fs,am654x-evm,am654x-hsevm,am654x-idk,bbai,beaglebone,beaglebone-black,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm,j7200-evm,j7200-hsevm,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,omapl138-lcdk","Move IPC validation source from github to git.ti.com"
   "LCPD-24251","am43xx-gpevm,am57xx-evm","LTP Linux System Calls failed"
   "LCPD-19043","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm,dra71x-evm,dra72x-evm,dra76x-evm,dra7xx-evm","kernel: dtbs_check command cannot be run with dtb-merge changes"
   "LCPD-16642","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm","omapdrm: in some cases, DPI output width does not need to be divisible by 8"
   "LCPD-16207","am574x-hsidk","Board does not boot sometimes due to crypto crash when debug options are enabled"
   "LCPD-15864","am57xx-evm","SoC Performance Monitoring tool is still not enabled"
   "LCPD-15402","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm,dra71x-evm,dra72x-evm,dra76x-evm,dra7xx-evm","rpmsg-rpc: test application does not bail out gracefully upon error recovery"
   "LCPD-15400","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm,dra71x-evm,dra72x-evm,dra76x-evm,dra7xx-evm","remoteproc/omap: System suspend fails for IPU1 domain without any remoteprocs loaded"
   "LCPD-13443","am57xx-hsevm","Camera is not detected on AM572x-HSEVM"
   "LCPD-10726","am572x-idk,am57xx-evm","Update DDR3 emif regs structure for EMIF2 for the beagle_x15 board in U-Boot board file"
   "LCPD-9923","am335x-evm,am43xx-gpevm,am57xx-evm,k2e-evm,k2g-evm,k2hk-evm,k2l-evm","Error message in boot log for K2 and AM platforms"
   "LCPD-9616","am57xx-evm","QtCreator GDB (remote) debugging stops working since QT5.7.1"
   "LCPD-9364","am57xx-hsevm","There are SCM FW warnings during the am57xx-hsevm boot"
   "LCPD-9006","am57xx-evm,dra72x-evm,dra7xx-evm","Some GLBenchmark tests fail to run"
   "LCPD-8352","am43xx-gpevm,am57xx-evm,dra7xx-evm","weston: stress testing with 75 concurrent instances of simple-egl leads to unresponsive HMI due to running out of memory"
   "LCPD-8350","am57xx-evm","UART boot does not work on am57xx-evm"
   "LCPD-8210","am571x-idk,am572x-idk,am57xx-evm","QT Touchscreen interaction (Bear Whack) crash"
   "LCPD-7255","am335x-evm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am57xx-evm,beaglebone,beaglebone-black,beaglebone-black-ice,dra72x-evm,dra72x-hsevm,dra7xx-evm,dra7xx-hsevm,k2e-evm,k2g-evm,k2g-ice,k2hk-evm,k2l-evm","Telnet login takes too long (~40 seconds)"
   "LCPD-6075","am572x-idk,am57xx-evm,dra7xx-evm","BUG: using smp_processor_id() in preemptible [00000000] code during remoteproc suspend/resume"

|

.. _release-specific-linux-kernel-known-issues:

Linux Kernel Known Issues
-------------------------
.. csv-table::
   :header: "Record ID", "Priority", "Title", "Component", "Subcomponent", "Platform", "Workaround", "Impact"
   :widths: 5, 10, 70, 10, 5, 20, 35, 20

   "LCPD-45238","P5-Not Prioritized","am57xx-evm: RC-13: Failure: CPSW: The Ethernet driver will be a standard Linux...","Connectivity","CPSW","am57xx-evm"
   "LCPD-45237","P5-Not Prioritized","am57xx-evm: RC-13: Failure: CPSW: The Ethernet switch driver shall provide the...","Connectivity","CPSW","am57xx-evm"
   "LCPD-45236","P5-Not Prioritized","am57xx-evm: RC-13: Failure: Linux : USB : DEVICE : NCM class shall be supporte...","Connectivity","USB","am57xx-evm"
   "LCPD-45235","P5-Not Prioritized","am57xx-evm: RC-13: Failure: CPSW: In switch mode the ethernet driver downstrea...","Connectivity","CPSW","am57xx-evm"
   "LCPD-45234","P5-Not Prioritized","am57xx-evm: RC-13: Failure: Linux : USB : HOST : Selective suspend shall be su...","Connectivity","USB","am57xx-evm"
   "LCPD-45233","P5-Not Prioritized","am57xx-evm: RC-13: Failure: CPSW: Ethernet driver shall support suspend/resume...","Connectivity","CPSW Suspend/Resume","am57xx-evm"
   "LCPD-45232","P5-Not Prioritized","am57xx-evm: RC-13: Failure: CPSW: Switch mode eth supports suspend/resume","Connectivity","CPSW Suspend/Resume","am57xx-evm"
   "LCPD-45231","P5-Not Prioritized","am57xx-evm: RC-13: Failure: PTP using CPSW CPTS for 1588 Time-stamping in Linu...","Connectivity","CPTS","am57xx-evm"
   "LCPD-45230","P5-Not Prioritized","am57xx-evm: RC-13: Failure: Linux : USB : DEVICE : Full-speed NCM client gadge...","Connectivity","USB","am57xx-evm"
   "LCPD-45229","P5-Not Prioritized","am57xx-evm: RC-13: Failure: Linux : USB : DEVICE : ECM class shall be supporte...","Connectivity","USB","am57xx-evm"
   "LCPD-45228","P5-Not Prioritized","am57xx-evm: RC-13: Failure: Linux : USB : DEVICE : High-speed NCM client gadge...","Connectivity","USB","am57xx-evm"
   "LCPD-45227","P5-Not Prioritized","am57xx-evm: RC-13: Failure: Linux : USB : DEVICE : High-speed ECM client gadge...","Connectivity","USB","am57xx-evm"
   "LCPD-45226","P5-Not Prioritized","am57xx-evm: RC-13: Failure: Linux : USB : DEVICE : Full-speed ECM client gadge...","Connectivity","USB","am57xx-evm"
   "LCPD-45225","P5-Not Prioritized","am57xx-evm: RC-13: Failure: CPSW: Ethernet driver shall support placing CPDMA ...","Connectivity","CPSW","am57xx-evm"
   "LCPD-45224","P5-Not Prioritized","am57xx-evm: RC-13: Failure: Linux : USB : DEVICE : ZLP shall be supported.","Connectivity","USB","am57xx-evm"
   "LCPD-45223","P5-Not Prioritized","am57xx-evm: RC-13: Failure: Linux : USB : HOST : ACM class client devices shal...","Connectivity","USB","am57xx-evm"
   "LCPD-45222","P5-Not Prioritized","am57xx-evm: RC-13: Failure: CPSW: The ethernet switch driver shall support mul...","Connectivity","CPSW","am57xx-evm"
   "LCPD-45218","P5-Not Prioritized","am57xx-evm: RC-13: Failure: Linux : USB : DEVICE : Cable connect disconnect fe...","Connectivity","USB","am57xx-evm"
   "LCPD-45137","P5-Not Prioritized","TEST: Add storm prevention support for RSTP and HSR","Connectivity","","am335x-ice,am43xx-hsevm,am574x-idk"
   "LCPD-45136","P5-Not Prioritized","TEST: HSR HW offload TCP iperf numbers are low for AM57x","Connectivity","","am574x-idk"
   "LCPD-45134","P5-Not Prioritized","TEST: Add PRP Automation support for AM57x","Connectivity","","am574x-idk"
   "LCPD-44484","P3-Medium","DSS Kernel Documentation is not present","Baseport","Documentation","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm"
   "LCPD-43870","P5-Not Prioritized","am57xx-evm pg1.1 boards fail to boot with 11.00 RC12 image","Baseport","boot","am57xx-evm"
   "LCPD-43555","P5-Not Prioritized","9.3 Documentation IPC for AM57xx has TODOs in sections","Baseport","Documentation","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm"
   "LCPD-42841","P5-Not Prioritized","9.3 Documentation GCC_Toolchain instructions do not work","Baseport","Documentation","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm"
   "LCPD-42680","P3-Medium","32 bit processors should document y2038","Baseport","","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm"
   "LCPD-42484","P5-Not Prioritized","SDK 9.3 RC6: CPU freq test , Some perf (wheatstone and Dhrystone) failure","Baseport","","am57xx-evm"
   "LCPD-42167","P3-Medium","PRU RPMsg swaps which message is sent to which core","Baseport","","am335x-evm,am437x-sk,am571x-idk,am572x-idk,am62xx_sk-fs,am64xx-evm,am64xx_sk-fs,am654x-idk,beaglebone-black"
   "LCPD-42139","P5-Not Prioritized","USB Core Hangs during kernel boot on AM571X-idk","Baseport","","am571x-idk"
   "LCPD-39354","P3-Medium","timer16 is throwing EINVAL error in kernel boot","Baseport","TIMER","am571x-idk"
   "LCPD-39022","P5-Not Prioritized","UART: test fails on am57x and kirkstone","Baseport","UART","am572x-idk,am574x-idk,am57xx-evm,am57xx-hsevm"
   "LCPD-37920","P5-Not Prioritized","ti-rpmsg-char should use the same toolchain as current Yocto build","IPC","","am335x-evm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-gpevm,am571x-idk,am572x-idk,am574x-idk,am57xx-evm,am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_p0_sk-fs,am62xx_sk-fs,am64xx-evm,am64xx_sk-fs,am654x-evm,am654x-idk"
   "LCPD-37747","P3-Medium","DOC:  Ethernet Switch Instructions are not included","Baseport,Connectivity","Documentation","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm"
   "LCPD-37648","P5-Not Prioritized","Dual camera Demo ","Baseport","","am57xx-evm"
   "LCPD-37643","P5-Not Prioritized","GPIO driver shall disable a GPIO module when all the pins of this GPIO module are inactive (clock gating forced at module level).","Baseport","","am57xx-evm"
   "LCPD-37629","P3-Medium","DSS: support Writeback capture mode","Audio & Display","","am57xx-evm"
   "LCPD-37553","P5-Not Prioritized","USB host driver shall support selective suspend FAILS","Connectivity","USB","am57xx-evm"
   "LCPD-37428","P5-Not Prioritized","FAT driver part of the eMMC-boot functionality of ROM code can only read a limited amount of entries of the FAT table","Baseport","ROM_Boot","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm"
   "LCPD-37241","P3-Medium","NBench performance is below par in 9.1 SDK  when compared to the previous release 8.2","Baseport","CPU","am57xx-evm"
   "LCPD-36742","P3-Medium","AM57x: CONFIG_NL80211_TESTMODE is not =y ","Baseport","","am57xx-evm"
   "LCPD-36655","P2-High","AM57x: Unable to load vpe modules","Audio & Display,Baseport","","am57xx-evm"
   "LCPD-36396","P3-Medium","Instructions for taking the C66 out of reset do not work","Baseport","","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm"
   "LCPD-25571","P3-Medium","GPIO EDGE_ALL_BANK test fails","Baseport","GPIO","am57xx-evm"
   "LCPD-25570","P3-Medium","GST Decode Tests fails","Baseport","CAPTURE","am57xx-evm"
   "LCPD-25532","P3-Medium","VIP: Failed to load vivid module","Connectivity","VIP","am57xx-evm"
   "LCPD-25333","P2-High","remoteproc: failure to stop a suspended processor","IPC","DSP_remoteproc IPU_remoteproc","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm"
   "LCPD-25324","P5-Not Prioritized","remoteproc/omap: messageq_fault firmware image does not work for DSP1","IPC","Firmware","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm"
   "LCPD-25323","P3-Medium","remoteproc/omap: circular lockdep being reported on some runs with rpmsg-proto recovery testing","Baseport,IPC","DSP_remoteproc IPU_remoteproc","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm"
   "LCPD-25295","P3-Medium","DRM test fails due to color mismatch between captured and golden videos","Audio & Display","DRM","am57xx-evm"
   "LCPD-24818","P4-Low","AM57x: Warnings during HS device boot","Baseport","","am574x-hsidk"
   "LCPD-24728","P3-Medium","Power measurement with Standby/Suspend/Resume failure","Baseport","Power_Management","am335x-evm,am43xx-gpevm,am57xx-evm"
   "LCPD-24719","P4-Low","GStreamer crashes","Baseport","","am57xx-evm"
   "LCPD-24682","P2-High","Timer - DUT time is deviating more than 0.0005","Baseport","","am57xx-evm"
   "LCPD-24648","P3-Medium","Move dma-heaps-test and ion-tests to TI repositories","Baseport","","am335x-evm,am572x-idk,am64xx-evm,dra71x-evm,j7200-evm,j721e-evm"
   "LCPD-24626","P3-Medium","""Verify kernel boots 100 times successfully using SD card"" fails","Baseport","boot","am335x-evm,am57xx-evm"
   "LCPD-24590","P4-Low","cannot load such file -- wx","Audio & Display","","am57xx-evm"
   "LCPD-24589","P2-High","no new usb reported on host after g_multi ","Connectivity","USBDEVICE","am57xx-evm,j721e-idk-gw"
   "LCPD-24506","P5-Not Prioritized","simulates touch events using Tapbot failed","Baseport","","am57xx-evm"
   "LCPD-24463","P4-Low","HSR/PRP: Root cause NetJury issues with HSR/PRP with RBX and VDAN node","Connectivity","","am571x-idk,am572x-idk"
   "LCPD-24456","P3-Medium","Move IPC validation source from github to git.ti.com","Baseport","IPC","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-epos,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am62axx_sk-fs,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am64xx-evm,am64xx-hsevm,am64xx_sk-fs,am654x-evm,am654x-hsevm,am654x-idk,bbai,beaglebone,beaglebone-black,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm,j7200-evm,j7200-hsevm,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,omapl138-lcdk"
   "LCPD-24251","P3-Medium","LTP Linux System Calls failed","Baseport","","am43xx-gpevm,am57xx-evm"
   "LCPD-19260","P3-Medium","PRUETH: Single EMAC doesn't ping with ICSS-1 Port 2 (MII-1)","Connectivity","","am571x-idk"
   "LCPD-19043","P4-Low","kernel: dtbs_check command cannot be run with dtb-merge changes","Baseport","","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm,dra71x-evm,dra72x-evm,dra76x-evm,dra7xx-evm"
   "LCPD-18227","P3-Medium","cam and  vpe could not suspend","Audio & Display","Capture","am57xx-evm,dra7xx-evm"
   "LCPD-16642","P3-Medium","omapdrm: in some cases, DPI output width does not need to be divisible by 8","Baseport","Display","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm"
   "LCPD-15649","P3-Medium","Uboot: sata could not be detected ","Connectivity","","am57xx-evm"
   "LCPD-15540","P3-Medium","uvc-gadget results in segmentation fault","Connectivity","","am57xx-evm,am654x-evm,dra71x-evm,dra7xx-evm"
   "LCPD-15402","P5-Not Prioritized","rpmsg-rpc: test application does not bail out gracefully upon error recovery","IPC","DSP_remoteproc IPU_remoteproc","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm,dra71x-evm,dra72x-evm,dra76x-evm,dra7xx-evm"
   "LCPD-15400","P4-Low","remoteproc/omap: System suspend fails for IPU1 domain without any remoteprocs loaded","IPC","IPU_remoteproc","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm,dra71x-evm,dra72x-evm,dra76x-evm,dra7xx-evm"
   "LCPD-14171","P3-Medium","Failed to read uboot from SD card 1/1000 times","Connectivity","","am57xx-evm,dra7xx-evm"
   "LCPD-13412","P2-High","VIP camera sensor (mt9t11) is not initialized properly","Audio & Display","","am57xx-evm"
   "LCPD-12226","P3-Medium","mmcsd first write perf decreased on some platforms","Connectivity","","am43xx-gpevm,am574x-idk,am57xx-evm,omapl138-lcdk"
   "LCPD-11952","P3-Medium","AM57x: disabling USB super-speed phy in DT causes kernel crash","Connectivity","USB","am571x-idk,dra72x-evm"
   "LCPD-11564","P3-Medium","AM57xx-evm: eth1 1G connection failure to netgear switch","Connectivity","CPSW ETHERNET PHYIF","am57xx-evm"
   "LCPD-11138","P3-Medium","VIP driver multi-channel capture issue with TVP5158","Audio & Display","Capture VIP","am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,dra7,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm"
   "LCPD-9974","P3-Medium","PCIe x2 width is not at expected width on am571x-idk","Connectivity","PCIe","am571x-idk"
   "LCPD-9466","P3-Medium","SATA PMP causes suspend failures","Connectivity","SATA","am57xx-evm,dra7xx-evm"
   "LCPD-9222","P4-Low","PRUSS Ethernet does not work on AM572x ES1.1","Connectivity","PRUSS-Ethernet","am572x-idk"
   "LCPD-8350","P3-Medium","UART boot does not work on am57xx-evm","Baseport","","am57xx-evm"
   "LCPD-7998","P4-Low","Realtime OSADL Test results degraded slightly for am572x-idk","Connectivity","","am572x-idk"
   "LCPD-7829","P3-Medium","uboot: UHS card did not work on the expected speed in uboot","Connectivity","","am57xx-evm"
   "LCPD-7744","P3-Medium","UHS SDR104 card works on different speed after soft reboot","Connectivity","","am57xx-evm"
   "LCPD-7735","P3-Medium","Powerdomain (vpe_pwrdm) didn't enter target state 0","Audio & Display,Power & Thermal","","am57xx-evm,dra71x-evm,dra71x-hsevm,dra72x-evm,dra7xx-evm"
   "LCPD-7696","P3-Medium","DRA7xx: VPE: File2File checksum changes across multiple runs","Audio & Display","","am571x-idk,am572x-idk,am57xx-evm,am57xx-hsevm,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra7xx-evm,dra7xx-hsevm"
   "LCPD-7265","P3-Medium","Uboot eMMC does not use HS200 on am57xx-gpevm","Connectivity","","am57xx-evm"
   "LCPD-7256","P3-Medium","Board sometimes hangs after suspend/resume cycle","Power & Thermal","","am335x-evm,am335x-hsevm,am57xx-evm,dra72x-evm,dra7xx-evm"
   "LCPD-7188","P4-Low","PCIe-SATA test failed","Connectivity","","am57xx-evm,dra72x-evm,dra7xx-evm"
   "LCPD-6300","P3-Medium","am57xx-evm: A few UHS cards could not be numerated in kernel and mmc as rootfs failed.","Connectivity","","am57xx-evm"
   "LCPD-6075","P5-Not Prioritized","BUG: using smp_processor_id() in preemptible [00000000] code during remoteproc suspend/resume","Baseport,IPC","","am572x-idk,am57xx-evm,dra7xx-evm"
   "LCPD-5522","P3-Medium","pcie-usb sometimes the usb drive/stick could not be enumerated","Connectivity","","am571x-idk,am572x-idk,am57xx-evm,am57xx-hsevm,dra72x-evm,dra72x-hsevm,dra7xx-evm,dra7xx-hsevm"
   "LCPD-1239","P3-Medium","Connectivity: DUT could not resume when PCI-SATA card is in","Connectivity","PCIe","am572x-idk,am57xx-evm,dra72x-evm,dra7xx-evm"
   "LCPD-1207","P4-Low","AM43XX/AM57XX/DRA7: CONNECTIVITY: dwc3_omap on am43xx and xhci_plat_hcd on dra7 - removal results in segmentation fault","Connectivity","USB","am43xx-gpevm,am57xx-evm,dra7xx-evm"
   "LCPD-1106","P3-Medium","Connectivity:PCIe-SATA ext2 1G write performance is poor due to ata failed command","Connectivity","PCIe","am57xx-evm,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra7xx-evm,dra7xx-hsevm"


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
	LCPD-18760,ICSS-M: RSTP: Linux shall support PTP TC,Connectivity,"PRUSS/ETH, PTP, RSTP",am571x-idk
	LCPD-18759,ICSS-M: HSR/PRP: Linux shall support PTP Boundary Clock with 3/4/5-leg configurations,Connectivity,"HSR-PRP, PRUSS/ETH, PTP","am571x-idk, am572x-idk, am574x-idk"
	LCPD-17509,ICSS-M: Support SNMP Agent for IEC62439 specified MIBs (HSR/PRP),Connectivity,"HSR-PRP, PRUSS/ETH","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17500,Run NetJury test for HSR/PRP protocol compliance,Connectivity,"HSR-PRP, PRUSS/ETH",am572x-idk
	LCPD-17467,ICSS-M: RSTP: Linux shall support PTP OC(slave and master),Connectivity,"PRUSS/ETH, RSTP",am571x-idk
	LCPD-17463,ICSS-M: HSR/PRP: Linux shall support PTP over VLAN,Connectivity,"HSR-PRP, PRUSS/ETH, PTP","am571x-idk, am572x-idk, am574x-idk"
	LCPD-17462,ICSS-M: Dual EMAC: Linux shall support PPS generation by ICSS IEP,Connectivity,"PRUSS/ETH, PTP","am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17461,ICSS-M: HSR/PRP: Linux shall support PPS generation by ICSS IEP,Connectivity,"HSR-PRP, PRUSS/ETH, PTP","am571x-idk, am572x-idk, am574x-idk"
	LCPD-17458,ICSS-M: HSR/PRP: Linux shall support PTP OC (slave/master),Connectivity,"HSR-PRP, PRUSS/ETH, PTP","am335x-ice, am571x-idk, am572x-idk, am574x-idk"
	LCPD-17457,ICSS-M: HSR: Linux shall support PTP TC,Connectivity,"HSR-PRP, PRUSS/ETH, PTP","am335x-ice, am571x-idk, am572x-idk, am574x-idk"
	LCPD-10725,16 bit RAW video capture,Audio & Display,"Capture, VIP","am571x-idk, am572x-idk, am57xx-evm, am57xx-hsevm"
	LCPD-8407,PRU Kernel Eth driver to work with Profinet firmware,Connectivity,"PRUSS-Ethernet, PRUSS/ETH","am335x-ice, am437x-idk, am571x-idk, am572x-idk, k2g-ice"
	LCPD-7814,VIP 8 bit capture support,Audio & Display,"Capture, VIP","am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-hsevm, dra71x-evm, dra71x-hsevm, dra72x-evm, dra72x-hsevm, dra76x-evm, dra76x-hsevm, dra7xx-evm, dra7xx-hsevm"
	LCPD-7221,ICSS Ethernet Support - UIO co-exist with Kernel Ethernet Driver,"Connectivity, IPC",PRUSS/ETH,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, k2g-ice"
	LCPD-6431,Support format conversion to RGB by VIP driver,Audio & Display,"Capture, VIP",am57xx-evm
	LCPD-6320,ICSS Ethernet Support - AM571x IDK: Support 6-port Ethernet configuration co-existing with CPSW,Connectivity,PRUSS/ETH,am571x-idk
	LCPD-5553,AM57xx VIP driver color space conversion support,Audio & Display,"Capture, VIP","am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm"
	LCPD-5505,ICSS Ethernet Support - RT Use Case - UIO,Connectivity,PRUSS/ETH,"am571x-idk, am572x-idk, am57xx-evm"
	LCPD-5254,Scaler support in VIP driver,Audio & Display,"CAPTURE, VIP","am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-hsevm, dra71x-evm, dra71x-hsevm, dra72x-evm, dra72x-hsevm, dra76x-evm, dra76x-hsevm, dra7xx-evm, dra7xx-hsevm"
	IVIREQ-649,V4L2 raw mode 12bit for VIP/CSI2 on J6 platform,"Camera, Drivers","CSI2, VIP","dra71x-evm, dra7xx-evm"

|

.. rubric:: Installation and Usage
   :name: installation-and-usage

The `Software Developer's Guide <index.html>`__ provides instructions on how to setup up your Linux development
environment, install the SDK and start your development. It also includes User's Guides for various Example Applications and Code
Composer Studio.

|

.. rubric:: Host Support
   :name: host-support

For the specific supported hosts for current SDK, see :ref:`this page
<how-to-build-a-ubuntu-linux-host-under-vmware>`.

.. note::
   Processor SDK Installer is 64-bit, and installs only on 64-bit host
   machine. Support for 32-bit host is dropped as Linaro toolchain is
   available only for 64-bit machines

|
