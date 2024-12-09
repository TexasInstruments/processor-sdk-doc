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
-  Matrix Application Launcher
-  Example Applications
-  WLAN support (Wilink 8)
-  Code Composer Studio

Licensing
=========

Please refer to the software manifest, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page. The manifest can be found on the SDK
download page or in the installed directory as indicated below. In
addition, see :ref:`GPLv3 Disclaimer <overview-gplv3-disclaimer>`.

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

Released Dec 2024

.. rubric:: What's New
   :name: whats-new

.. note:: Generic PRU-ICSS Ethernet is descoped in 09.03 release.

Processor SDK 9.3 Release has following new features:

 - 2023 LTS Stable Update to 6.1.119
 - Splash Screen Feature
 - Important Bug Fixes

|

.. _release-specific-sdk-components-versions:

.. rubric:: SDK Components & Versions
   :name: sdk-components-versions

+--------------------------+----------------------------+
| Component                | Version                    |
+==========================+============================+
| Linux Kernel             | 6.1.119 (2023 LTS)         |
+--------------------------+----------------------------+
| U-Boot                   | 2023.04                    |
+--------------------------+----------------------------+
| Yocto Project            | 4.0 (kirkstone)            |
+--------------------------+----------------------------+
| ARM Toolchain (gcc)      | 11.5                       |
+--------------------------+----------------------------+

|

Supported Platforms
===================
See :ref:`here <release-specific-supported-platforms-and-versions>` for a list of supported platforms and links to more information.

|


Build Information
=================

.. _u-boot-release-notes:

U-Boot
------

| Head Commit: 2a13324ec63cc488f5f578886d0cf6ece348dfda arm: dts: am335x: Use PWM for LCD backlight

| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2023.04
| Tag: 09.03.05
|

.. _release-specific-build-information-kernel:

Kernel
------

.. _release-specific-build-information-linux-kernel:

.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: c490f4c0fe51281818c45159c0fbed94f852978e HACK: arm: dts: am57: disable late attach as default

| Clone: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.1.y
| Tag: 09.03.05
|

.. _release-specific-build-information-rt-linux-kernel:

.. rubric:: Real Time (RT) Linux Kernel
   :name: real-time-rt-linux-kernel

| Head Commit: b0f9de804a162329bc81857ad50947311228dfb2 Merge branch 'ti-linux-6.1.y-cicd' into ti-rt-linux-6.1.y-cicd

| Clone: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-rt-linux-6.1.y
| Tag: 09.03.05-rt
|

.. _release-specific-generic-kernel-release-notes:

.. rubric:: Generic Kernel Release Notes
   :name: generic-kernel-release-notes

| Generic kernel release notes from kernelnewbies.org can be found at:
  http://kernelnewbies.org/Linux_6.1
| Archived versions can be found at:
  http://kernelnewbies.org/LinuxVersions

|

Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: 963140e3b5820d6ebf54a4418946a628e0fea2c6 CI/CD Auto-Merger: cicd.kirkstone.202412041235

| Clone: git://git.yoctoproject.org/meta-ti
| Branch: kirkstone
| Release Tag: 09.03.05
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: f59caa5f47a625ef9eecada069ae6a74c70bcc47 CI/CD Auto-Merger: cicd.kirkstone.202412041235

| Clone: git://git.yoctoproject.org/meta-arago
| Branch: kirkstone
| Release Tag: 09.03.05
|

.. rubric:: meta-tisdk
   :name: meta-tisdk

| Head Commit: 2ee8bead9d04afcb61234738e0d9a644395d27bf recipes-core: packagegroups: Drop SGX sources from am65xx

| Clone: git://git.ti.com/ti-sdk-linux/meta-tisdk.git
| Branch: kirkstone
| Release Tag: 09.03.05.02
|

Issues Tracker
==============

Issues opened in previous releases that were closed on this release
-------------------------------------------------------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform"
   :widths: 15, 70, 20

   "SITSW-706","Top level makefile broken in AM335x & AM437x","am335x-evm,am335x-ice,am335x-sk"
   "SITSW-703","AM335x SDK 7.3 has misleading information on HSR/PRP support","am335x-ice"
   "LCPD-24835","ADC_S_FUNC_TSCADC_ONESHOT_0001 fails","am335x-evm"
   "LCPD-24834","ADC continuous mode test failed ","am335x-evm"
   "LCPD-24826","Power Manager Runtime is not suspending SERIAL","am335x-evm"
   "LCPD-24811","LTP test fail- No Timers","am335x-evm"
   "LCPD-24792","RTC reliable test by using alarm fails","am335x-evm"
   "LCPD-24786","DRM Stress Test: Test setting different video modes frequently 1000 times fails","am335x-evm"
   "LCPD-24649","dma-heaps-test fails to build with 5.16-rc3 kernel+","am335x-evm"
   "LCPD-24239","IPC performance  test","am335x-evm"
   "LCPD-22828","Convert tps62360-regulator.txt: ""ti,tps62363"" to yaml","am335x-evm"
   "LCPD-19858","OE: OPTEE label used in SDK is old and wrong","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk"
   "LCPD-19838","Cryptodev not building against 5.10 kernel","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk"
   "LCPD-19279","openssl_perf.sh functionality to be included in rootfs (decouple from matrixgui)","am335x-evm"
   "LCPD-18643","U-Boot: AM335x/AM473x: Both SPI CS signals get asserted","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk"
   "LCPD-17817","Images created with Proc-SECDEV grow with number of times SECDEV has been used","am335x-hsevm"
   "LCPD-7366","uboot McSPI driver drives multiple chip selects simultaneously","am335x-evm"


|


Issues found and closed on this release that may be applicable to prior releases
--------------------------------------------------------------------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform"
   :widths: 15, 70, 20

   "SITSW-3404","installer-scripts: Version not auto updated for installer","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,beaglebone-black"
   "SITSW-3378","systemd-networkd-wait-online service timeouts ","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,beaglebone-black"
   "SITSW-1649","Create-sdcard.sh: Displays command not found error","am335x-evm,am335x-hsevm,am335x-sk"
   "LCPD-37016","u-boot NAND boot failure with SDK 9.1 on AM335x EVM","am335x-evm"
   "LCPD-36892","am335 : Fails to Boot : Halts at ""Starting Kernel"" Stage","am335x-evm,am335x-hsevm"
   "LCPD-36626","am335x: am43xx: Display and Touchscreen is not functional","am335x-evm,am335x-hsevm,am335x-sk"
   "LCPD-36625","am335x: kernel crash reported on few boards with default SMP config","am335x-evm,am335x-hsevm"
   "LCPD-36624","am335x: boot to console root prompt is taking longer","am335x-evm,am335x-hsevm"
   "LCPD-34990","am335x: initcall sequence failure in u-boot (USB ether init failed)","am335x-evm,am335x-ice,am335x-sk"
   "LCPD-29349","[AM335x] Write to Write Protected Block on 16GB, 32GB eMMC Causes Timeout and Data Corruption","am335x-evm"
   "LCPD-28032","AM335x HS Boot Failure","am335x-hsevm"
   "LCPD-27524","Yocto: SRCIPK Packaging Build Failures for Kernel/U-Boot","am335x-evm,am335x-sk"
   "LCPD-26692","Hardware + Software IPSec Performance Test Failures","am64xx-evm,am335x-evm"

|

SDK Known Issues
----------------
.. csv-table::
   :header: "Record ID", "Platform", "Title", "Workaround"
   :widths: 25, 30, 50, 600

   SITSW-1357,"am335x-evm,am335x-sk","Some of the Matrix QT5 demos (Touch, Thermostat, Browser) are failing",""
   SITSW-1358,"am335x-evm,am335x-sk","Matrix KMScube demo is failing",""
   SITSW-1376,"am335x-evm,am335x-sk","Matrix demo does not start until XFRM netlink socket initialization is complete","Reload localhost URL after XFRM netlink socket initialization is completed"

|

.. _release-specific-u-boot-known-issues:

U-Boot Known Issues
-------------------
.. csv-table::
   :header: "Record ID","Platform", "Title","Workaround"
   :widths: 15, 30, 70, 30

   "LCPD-37017","am335x-evm","u-boot NAND boot failure with SDK 8.2 on AM335x EVM",""
   "LCPD-19133","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk","Netconsole output corrupted when CONFIG_NETCONSOLE_BUFFER_SIZE >= 281",""


|

.. _release-specific-linux-kernel-known-issues:

Linux Kernel Known Issues
-------------------------
.. csv-table::
   :header: "Record ID", "Platform", "Title", "Workaround"
   :widths: 5, 10, 70, 10

   "LCPD-27472","am335x-evm","DRM stress failed ,Test setting different video modes frequently 1000 times",""
   "LCPD-25272","am335x-evm","Crypto_M_PERF_openssl_perf_software test Fails",""
   "LCPD-24728","am335x-evm","Power measurement with Standby/Suspend/Resume failure",""
   "LCPD-24456","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk","Move IPC validation source from github to git.ti.com",""
   "LCPD-24302","am335x-evm","The speed test built in to OpenSSL - cryptographic",""
   "LCPD-24182","am335x-evm,beaglebone-black","Powermgr_xs_func_simple_suspend/standby resume tests",""
   "LCPD-24104","am335x-evm","nandtest util crashes NAND ubifs filesystem",""
   "LCPD-23096","am335x-ice","PTP broken with PRU-ETH on AM335x ICEv2",""
   "LCPD-22417","am335x-evm","No throughput on ipsec aes128 hardware test",""
   "LCPD-17790","am335x-evm","AM335x: USB Device: 15% performance drop",""
   "LCPD-17673","am335x-evm,beaglebone-black","No software documentation for the Timer module",""
   "LCPD-17449","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,beaglebone-black","libasan_preinit.o is missing in devkit",""
   "LCPD-14855","am335x-evm,am335x-ice,am335x-sk","omap_i2c_prepare_recovery() function can Lock System",""
   "LCPD-13947","am335x-evm","nativesdk-opkg is broken in the devkit",""
   "LCPD-10221","am335x-evm","Longer resume times observed on setup with usb device cable",""
   "LCPD-9455","am335x-evm","Kernel Warning reported for a USB audio device when listing with pulseaudio",""
   "LCPD-9372","am335x-evm","Nand stress tests failed on a particular am335x-evm board",""
   "LCPD-8636","am335x-evm","Serial corruption being seen in kernel",""
   "LCPD-8133","am335x-evm","USB: ""cannot reset"" errors observed sometimes",""
   "LCPD-7955","am335x-evm","Uncorrectable Bitflip errors seen after switch to SystemD","Workaround to erase the NAND flash completely if flashed with an incompatible flash writer. SystemD tries to mount all partitions and that is the reason this is being seen now."
   "LCPD-5362","am335x-evm","MUSB: Isoch IN only utilises 50% bandwidth",""

|




.. rubric:: Installation and Usage
   :name: installation-and-usage

The :ref:`Software Developer's Guide <linux-index>` provides instructions on how to setup up your Linux development
environment, install the SDK and start your development.  It also includes User's Guides for various Example Applications and Code
Composer Studio.

|

.. rubric:: Host Support
   :name: host-support

The Processor SDK is developed, built and verified on Ubuntu |__LINUX_UBUNTU_VERSION_SHORT__|.


.. note::
   Processor SDK Installer is 64-bit, and installs only on 64-bit host
   machine. Support for 32-bit host is dropped as Linaro toolchain is
   available only for 64-bit machines

|
