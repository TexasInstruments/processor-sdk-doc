.. _release-specific-release-notes:

************************************
Release Notes
************************************

Overview
========

The **Processor Software Development Kit (Processor-SDK) for Linux**
provides a fundamental software platform for development, deployment and
execution of Linux based applications and includes the following:

-  Bootloaders & Filesystems
-  SDK Installer
-  Setup Scripts
-  Makefiles
-  Matrix Application Launcher
-  Example Applications
-  Code Composer Studio

Licensing
=========

Please refer to the software manifest, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page. The manifest can be found on the SDK
download page or in the installed directory as indicated below. In
addition, see `GPLv3 Disclaimer <Overview_GPLv3_Disclaimer.html>`__

Documentation
===============
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

Release 08.02.01
==================

Released June 2022

.. rubric:: What's New
   :name: whats-new

- Second release on 2021 LTS 5.10 kernel, 2021.01 U-Boot

.. rubric::  Other Updates

- Bug Fixes
   - The IDK boards' LCD issue has been resolved. With this release, SDK boots properly on IDK boards with LCD connected.
   - The HSR and PRP multicast and vlan filtering issue has been fixed.
   - ICSS Firmware updated with the following fix
       - HSR/PRP - Queue number corruption in memory, Dropping of packets even after the credits are expired have been resolved.
	   - PTP Message ID check field is updated to 4 bits field.
	   - HSR/PRP LRE NODE TABLE LOOKUP ERROR counters are removed.


.. _release-specific-sdk-components-versions:

.. rubric:: SDK Components & Versions
   :name: sdk-components-versions

+--------------------------+----------------------------+
| Component                | Version                    |
+==========================+============================+
| Linux Kernel             | 5.10.100 (2021 LTS)        |
+--------------------------+----------------------------+
| U-Boot                   | 2021.01                    |
+--------------------------+----------------------------+
| Yocto Project            | 3.1 (dunfell)              |
+--------------------------+----------------------------+
| ARM Toolchain (gcc)      | 9.2 2019.12 hard-float     |
+--------------------------+----------------------------+
| Qt                       | 5.14.2                     |
+--------------------------+----------------------------+
| Wayland                  | 1.18                       |
+--------------------------+----------------------------+
| GStreamer                | 1.16.3                     |
+--------------------------+----------------------------+
| TI PRU Compiler          | 2.3.2                      |
+--------------------------+----------------------------+
| TI C66x CGT Compiler     | 8.3.2                      |
+--------------------------+----------------------------+

|

Supported Platforms
=====================================
See `here <Release_Specific_Supported_Platforms_and_Versions.html>`__ for a list of supported platforms and links to more information.

|


Build Information
=====================================

.. _u-boot-release-notes:

U-Boot
-------------------------

| The U-Boot git repository, branch and commit id can be found below:
| Based on verson: 2021.01
| URL: git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2021.01
| Commit ID: 44a87e3ab85c6d64044f0b5ad677008316baad70

|

.. _release-specific-build-information-kernel:

Kernel
-------------------------

.. _release-specific-build-information-linux-kernel:

.. rubric:: Linux Kernel
   :name: linux-kernel

| The kernel git repository, branch and commit id can be found below:
| Based on Version: 5.10.100
| URL: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-5.10.y
| Commit ID: 7a7a3af903da2b2d551d058f8262a66e6b42b6b1

|

.. _release-specific-build-information-rt-linux-kernel:

.. rubric:: Real Time (RT) Linux Kernel
   :name: real-time-rt-linux-kernel

| The RT kernel git repository, branch and commit id can be found below:
| Based on:
| Kernel Version: 5.10.100
| RT Kernel Version: 5.10.100-rt62

| URL: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-rt-linux-5.10.y
| Commit ID: 204ec708dc86f4334f585f04835527570be1c4eb

|


.. _release-specific-generic-kernel-release-notes:

.. rubric:: Generic Kernel Release Notes
   :name: generic-kernel-release-notes

| Generic kernel release notes from kernelnewbies.org can be found at:
  https://kernelnewbies.org/Linux_5.10
| Archived versions can be found at:
  http://kernelnewbies.org/LinuxVersions

|

Issues Tracker
=====================================

Issues closed on this release
---------------------------------------------------------------------
.. csv-table::
   :header: "Record ID", "Summary"
   :widths: 20, 80

   LCPD-28151,"HSR/PRP Multicast Filtering failure"
   LCPD-28152,"AM571x-idk: Failed to load /boot/am571x-idk-lcd-osd101t2587.dtb during boot"
   LCPD-26605,"am571x-idk and am572x-idk not booting from SD card"

SDK Known Issues
-----------------
.. csv-table::
   :header: "Record ID", "Platform", "Title", "Workaround"
   :widths: 25, 30, 50, 600

   ADASVISION-5143,AM57,QT5 Browser is failing due to the python2 dependency
   LCPD-25762,am571x-idk,AM57x: Runtime switching between HSR/PRP and EMAC failed
   LCPD-25571,am57xx-evm,GPIO EDGE_ALL_BANK test fails
   LCPD-25570,am57xx-evm,GST Decode Tests fails
   LCPD-25554,am57xx-evm,VIP: V4L2 Capture test fails with one or more compliance tests
   LCPD-25537,am57xx-evm,VIP: unable to get reference files
   LCPD-25533,am57xx-evm,VIP capture + scaling Test failure
   LCPD-25532,am57xx-evm,VIP: Failed to load vivid module
   LCPD-25506,am57xx-evm,Performance test failed for glmark2 benchmark ( Graphics-Glmark2-DRM)
   LCPD-25333,"am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm",remoteproc: failure to stop a suspended processor
   LCPD-25326,"am335x-evm,am57xx-evm",MMC_L_PERF performance test failed
   LCPD-25323,"am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm",remoteproc/omap: circular lockdep being reported on some runs with rpmsg-proto recovery testing
   LCPD-25295,am57xx-evm,DRM test fails due to color mismatch between captured and golden videos
   LCPD-25280,am57xx-evm,Ethernet ping tests fails while doing power suspend/resume operations
   LCPD-25279,am57xx-evm,suspend resume by UART test failure
   LCPD-24728,"am335x-evm,am43xx-gpevm,am57xx-evm",Power measurement with Standby/Suspend/Resume failure

|

.. _release-specific-linux-kernel-known-issues:

Linux Kernel Known Issues
---------------------------
.. csv-table::
   :header: "Record ID", "Priority", "Title", "Component", "Subcomponent", "Platform", "Workaround", "Impact"
   :widths: 5, 10, 70, 10, 5, 20, 35, 20

   LCPD-26692,P5-Not Prioritized,"Hardware + Software IPSec Performance Test Failures",Crypto,,"am335x-evm,am43xx-gpevm,am57xx-evm,am64xx-evm,j721e-idk-gw",,
   LCPD-25326,P5-Not Prioritized,"MMC_L_PERF performance test failed",Connectivity,,"am335x-evm,am57xx-evm",,
   LCPD-24728,P3-Medium,"Power measurement with Standby/Suspend/Resume failure,Power & Thermal",,,"am335x-evm,am43xx-gpevm,am57xx-evm",,
   LCPD-24689,P3-Medium,"libcurl does not honor http_proxy",System Integration,,"am335x-evm,am57xx-evm",,
   LCPD-24681,P3-Medium,"IPSEC software and hardware performances",Baseport,,"am335x-evm,am57xx-evm",,
   LCPD-24648,P3-Medium,"Move dma-heaps-test and ion-tests to TI repositories",System Test,,"am335x-evm,am572x-idk,am64xx-evm,dra71x-evm,j7200-evm,j721e-evm",,
   LCPD-24626,P3-Medium,"Verify kernel boots 100 times successfully using SD card fails",System Test,boot,"am335x-evm,am57xx-evm",,
   LCPD-24589,P2-High,"no new usb reported on host after g_multi","Connectivity,System Test",USBDEVICE,"am335x-evm,am57xx-evm,j721e-idk-gw",,
   LCPD-24456,P3-Medium,"Move IPC validation source from github to git.ti.com",IPC,,"am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-epos,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am62a-evm,am62xx-evm,am62xx-hsevm,am62xx-sk,am62xx-vlab,am62xx-zebu,am64xx-evm,am64xx-hsevm,am64xx-sk,am654x-evm,am654x-hsevm,am654x-idk,bbai,beaglebone,beaglebone-black,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm,j7200-evm,j7200-hsevm,j721e-evm,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721e-vlab,j721s2-evm,j721s2-hsevm,j7ae-evm,j7aep-zebu,j7ae-zebu,j7am-evm,j7amp-evm,j7amp-vlab,j7amp-zebu,j7am-vlab,j7am-zebu,k2e-evm,k2e-hsevm,k2g-evm,k2g-hsevm,k2g-ice,k2hk-evm,k2hk-hsevm,k2l-evm,k2l-hsevm,omapl138-lcdk",,
   LCPD-24302,P3-Medium,"The speed test built in to OpenSSL - cryptographic",Crypto,,"am335x-evm,am43xx-gpevm,am57xx-evm",,
   LCPD-24182,P2-High,"Powermgr_xs_func_simple_suspend/standby resume tests,Power & Thermal",,,"am335x-evm,am43xx-gpevm,am57xx-evm,beaglebone-black",,
   LCPD-22828,P5-Not Prioritized,"Convert tps62360-regulator.txt: ti,tps62363 to yaml",Baseport,,"am335x-evm,am437x-idk,am572x-idk",,
   LCPD-22824,P3-Medium,"Convert ssd1307fb.txt:  solomon,ssd1306fb-i2c to yaml",Audio & Display,,"am335x-evm,am437x-idk,am572x-idk",,
   LCPD-22426,P3-Medium,"USBDEV_highspeed_perf_cdc_iperf test is failing due to iperf issues",System Test,USBDEVICE,"am335x-evm,am57xx-evm",,
   LCPD-19858,P4-Low,"OE: OPTEE label used in SDK is old and wrong,Security","System Integration,OPTEE",OP-TEE,"am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-epos,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am64xx-evm,am64xx-vlab,am64xx-zebu,am654x-evm,am654x-hsevm,am654x-idk,bbai,beaglebone,beaglebone-black,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm,j7200-evm,j7200-hsevm,j721e-evm,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,k2e-evm,k2e-hsevm,k2g-evm,k2g-hsevm,k2g-ice,k2hk-evm,k2hk-hsevm,k2l-evm,k2l-hsevm",,
   LCPD-18232,P3-Medium,"RTC alarm test failed due to busybox's timeout syntax changes",System Test,,"am335x-evm,am57xx-evm,omapl138-lcdk",,
   LCPD-18070,P3-Medium,"usb: device: support custom builds for full speed tests",System Test,USBCLIENT,"am335x-evm,am335x-hsevm,am335x-sk,am437x-sk,am43xx-epos,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am654x-evm,beaglebone,beaglebone-black,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm,omapl138-lcdk",,
   LCPD-17673,P3-Medium,"No software documentation for the Timer module",Baseport,Timers,"am335x-evm,am43xx-gpevm,am571x-idk,am572x-idk,am574x-idk,am57xx-evm,am654x-evm,beaglebone-black,dra71x-evm,dra72x-evm,dra7xx-evm,j721e-evm",,
   LCPD-17449,P2-High,"libasan_preinit.o is missing in devkit",System Integration,Toolchain,"am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-epos,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am654x-evm,am654x-hsevm,am654x-idk,beaglebone,beaglebone-black,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm",,
   LCPD-17413,P3-Medium,"QT Webengine-based browser: the mouse does not work within the web page with QPA EGLFS",Graphics,,"am335x-evm,am43xx-gpevm,am57xx-evm,am654x-evm",,
   LCPD-15367,P4-Low,"Boot time increased about 15s",System Integration,,"am335x-evm,am574x-idk",,
   LCPD-12405,P3-Medium,"Openssl certgen fails due to coredump in openssl_gen_cert.sh",System Integration,,"am335x-evm,am335x-ice,am43xx-epos,am43xx-gpevm,am57xx-evm,dra71x-evm,k2e-evm,k2e-hsevm,k2g-evm,k2g-hsevm,k2l-evm",,
   LCPD-19660,P4-Low,"Remove unused definitions and related code for SV frame MAC address",Connectivity,,"am335x-ice,am437x-idk,am571x-idk,am572x-idk,am574x-idk",,
   LCPD-24505,P3-Medium,"KMS properties test failed",Audio & Display,,"am43xx-gpevm,am57xx-evm",,
   LCPD-24251,P3-Medium,LTP Linux System Calls failed,System,,"am43xx-gpevm,am57xx-evm",,
   LCPD-25762,P5-Not Prioritized,AM57x: Runtime switching between HSR/PRP and EMAC failed,Connectivity,,am571x-idk,,
   LCPD-25324,P5-Not Prioritized,"remoteproc/omap: messageq_fault firmware image does not work for DSP1",IPC,Firmware,"am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm",,
   LCPD-25323,P3-Medium,remoteproc/omap: circular lockdep being reported on some runs with rpmsg-proto recovery testing,"IPC,DSP_remoteproc",IPU_remoteproc,"am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm",,
   LCPD-24463,P4-Low,HSR/PRP: Root cause NetJury issues with HSR/PRP with RBX and VDAN node,Connectivity,,"am571x-idk,am572x-idk",,
   LCPD-22910,P3-Medium,Boundary Clock jitter exceeds 800us when SV traffic is added to setup,Connectivity,HSR-PRP,"am571x-idk,am572x-idk",,
   LCPD-21963,P2-High,"AM5726 hangs during PRU initialization","Connectivity,IPC",PRUSS,"am571x-idk,am572x-idk,am574x-idk",,
   LCPD-19596,P3-Medium,"cpsw: switchdev: fix case when brX has MAC assigned",Connectivity,"CPSW,ETHERNET,ETHERNETSWITCH,Network",am571x-idk,,
   LCPD-19260,P3-Medium,"PRUETH: Single EMAC doesn't ping with ICSS-1 Port 2 (MII-1)",Connectivity,,am571x-idk,,
   LCPD-18109,P4-Low,"am5xx-idk: pruss: l4per-clkctrl:0040:0: failed to disable on prueth removal",IPC,PRUSS,"am571x-idk,am572x-idk,am574x-idk",,
   LCPD-16642,P3-Medium,"omapdrm: in some cases, DPI output width does not need to be divisible by 8",Audio & Display,Display,"am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm",,
   LCPD-24719,P4-Low,GStreamer crashes,"Audio & Display",,am57xx-evm,,
   LCPD-24682,P4-Low,"Timer - DUT time is deviating more than 0.0005",System Test,,am57xx-evm,,
   LCPD-24588,P4-Low,"Validate that a non-root user that belongs to the right groups",System Test,,am57xx-evm,,
   LCPD-24506,P5-Not Prioritized,"simulates touch events using Tapbot failed",System Test,,am57xx-evm,,
   LCPD-24499,P4-Low,"OpenCL demos provided with root filesystem Failed",System Test,OpenCL,am57xx-evm,,
   LCPD-24489,P3-Medium,"Verify that primary planes can be used as overlay planes when not used in use",System Test,DRM,am57xx-evm,,
   LCPD-22361,P5-Not Prioritized,"SGX Lockup with gstreamer + weston,Graphics",,,am57xx-evm,,
   LCPD-19948,P3-Medium,"Yocto: stream recipe is incorrect",System Integration,,"am57xx-evm,am654x-evm,j721e-evm",,
   LCPD-19120,P2-High,"glsdk-example-apps package is needed for some Audio and Display tests",System Integration,,am57xx-evm,,
   LCPD-18684,P3-Medium,"syscalls sync failures: fdatasync03, fsync04, sync03, syncfs01, sync_file_range02",Baseport,System Test,"am57xx-evm,am654x-evm,j721e-idk-gw",,
   LCPD-18676,P4-Low,"Some Uboot upstream Pytests failed on am5",Baseport,,am57xx-evm,,
   LCPD-15864,P3-Medium,"SoC Performance Monitoring tool is still not enabled",Graphics,,am57xx-evm,,
   LCPD-24818,P4-Low,"AM57x: Warnings during HS device boot",Baseport,,am574x-hsidk,,
   LCPD-19835,P4-Low,"AM57-HS : E/TC:0 ti_sip_handler boot warning",Security,,am574x-hsidk,,
   LCPD-25571,P3-Medium,"GPIO EDGE_ALL_BANK test fails",Baseport,GPIO,am57xx-evm,,
   LCPD-25570,P3-Medium,"GST Decode Tests fails","Audio & Display",CAPTURE,am57xx-evm,,
   LCPD-25554,P3-Medium,"VIP: V4L2 Capture test fails with one or more compliance tests",Connectivity,VIP,am57xx-evm,,
   LCPD-25537,P3-Medium,"VIP: unable to get reference files",Connectivity,VIP,am57xx-evm,,
   LCPD-25533,P2-High,"VIP capture + scaling Test failure",Connectivity,"System Test,VIP",am57xx-evm,,
   LCPD-25532,P3-Medium,"VIP: Failed to load vivid module",Connectivity,VIP,am57xx-evm,,
   LCPD-25506,P5-Not Prioritized,"Performance test failed for glmark2 benchmark ( Graphics-Glmark2-DRM)",Graphics,System Integration,am57xx-evm,,
   LCPD-25295,P3-Medium,"DRM test fails due to color mismatch between captured and golden videos","Audio & Display","System Test,DRM",am57xx-evm,,
   LCPD-25280,P2-High,"Ethernet ping tests fails while doing power suspend/resume operations",System Test,POWER,am57xx-evm,,
   LCPD-25279,P3-Medium,suspend resume by UART test failure,"Power & Thermal",UART,am57xx-evm,,
   LCPD-15402,P5-Not Prioritized,"rpmsg-rpc: test application does not bail out gracefully upon error recovery",IPC,"DSP_remoteproc,IPU_remoteproc","am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm,dra71x-evm,dra72x-evm,dra76x-evm,dra7xx-evm",,
   LCPD-15400,P4-Low,"remoteproc/omap: System suspend fails for IPU1 domain without any remoteprocs loaded",IPC,IPU_remoteproc,"am571x-idk,am572x-idk,am574x-idk,am57xx-beagle-x15,am57xx-evm,dra71x-evm,dra72x-evm,dra76x-evm,dra7xx-evm",,
   LCPD-9481,P5-Not Prioritized,"Sometime the system hangs while loading the rpmsg rpc modules",IPC,RPMSG-RPC,"am571x-idk,am572x-idk,am57xx-evm,am57xx-hsevm",,
   LCPD-23061,P3-Medium,"AM572 : Kernel hangs when trying to access PRU Debug register space",Connectivity,PRU-ICSS,am572x-idk,,
   LCPD-10726,P3-Medium,"Update DDR3 emif regs structure for EMIF2 for the beagle_x15 board in U-Boot board file",Baseport,,"am572x-idk,am57xx-evm",,
   LCPD-6075,P5-Not Prioritized,"BUG: using smp_processor_id() in preemptible [00000000] code during remoteproc suspend/resume",Baseport,IPC,"am572x-idk,am57xx-evm,dra7xx-evm",,

|

.. _release-specific-rt-linux-kernel-known-issues:

RT Linux Kernel Known Issues
-----------------------------

.. csv-table::
   :header: "Record ID", "Priority", "Title", "Component", "Platform", "Workaround"
   :widths: 5, 10, 70, 10, 20, 15

   LCPD-6663 ,P3-Medium ,[RT] Kmemleak is buggy and boot is crashed randomly ,Baseport ,  ,
   LCPD-7623 ,P3-Medium ,Seeing SPI transfer failed error sometimes on k2hk when using rt kernel ,Connectivity ,k2hk-evm ,
   LCPD-11586 ,P3-Medium ,dhcp failed to get IP address after reboot for K2G-ICE non-RT linux ,Baseport  ,"k2g-ice ",

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
