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

.. note:: Generic PRU-ICSS Ethernet is descoped in 09.03.xx release.

Processor SDK 9.3 Release has following new features:

- 2023 LTS Stable Update to 6.1.119
- Important Bug Fixes

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

   "SITSW-706","Top level makefile broken in AM335x & AM437x","am437x-idk,am437x-sk"
   "LCPD-25313","HDMI Audio playback tests are failing for all the frequencies ","am43xx-gpevm"
   "LCPD-25277","NAND rootfs as ubifs mount, read, write and delete test Fails","am43xx-gpevm"
   "LCPD-24853","USBDEV msc_mmc g_mass_storage.ko module not available ","am43xx-gpevm"
   "LCPD-24826","Power Manager Runtime is not suspending SERIAL","am43xx-gpevm"
   "LCPD-24820","HW SHA crypto acceleration error getting irq for crypto","am43xx-gpevm"
   "LCPD-24811","LTP test fail- No Timers","am43xx-gpevm"
   "LCPD-24239","IPC performance  test","am43xx-gpevm"
   "LCPD-23019","OPTEE tests are failing (Impact 5)","am43xx-hsevm"
   "LCPD-22828","Convert tps62360-regulator.txt: ""ti,tps62363"" to yaml","am437x-idk"
   "LCPD-21523","alpha blending test failure","am43xx-gpevm"
   "LCPD-20673","packaging: ipsec: command not found","am43xx-gpevm"
   "LCPD-19858","OE: OPTEE label used in SDK is old and wrong","am43xx-gpevm,am43xx-hsevm,am437x-idk,am437x-sk"
   "LCPD-19838","Cryptodev not building against 5.10 kernel","am43xx-gpevm,am43xx-hsevm,am437x-idk,am437x-sk"
   "LCPD-19279","openssl_perf.sh functionality to be included in rootfs (decouple from matrixgui)","am43xx-gpevm"
   "LCPD-18643","U-Boot: AM335x/AM473x: Both SPI CS signals get asserted","am43xx-gpevm,am43xx-hsevm,am437x-idk,am437x-sk"
   "LCPD-17817","Images created with Proc-SECDEV grow with number of times SECDEV has been used","am43xx-hsevm"
   "LCPD-7025","System takes more than 10 seconds to go from login prompt to system prompt","am43xx-gpevm"


|


Issues found and closed on this release that may be applicable to prior releases
--------------------------------------------------------------------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform"
   :widths: 15, 70, 20

   "SITSW-3404","installer-scripts: Version not auto updated for installer","am437x-idk,am437x-sk,am43xx-gpevm,am43xx-hsevm"
   "SITSW-3378","systemd-networkd-wait-online service timeouts ","am437x-idk,am437x-sk,am43xx-gpevm,am43xx-hsevm"
   "SITSW-1649","Create-sdcard.sh: Displays command not found error","am437x-sk,am43xx-gpevm,am43xx-hsevm"
   "LCPD-36626","am335x: am43xx: Display and Touchscreen is not functional","am43xx-gpevm,am43xx-hsevm"
   "LCPD-34652","AM437x: Failing POWERMGR_S_FUNC_CPUFREQ_BASIC test","am43xx-gpevm,am43xx-hsevm,am437x-sk"
   "LCPD-29650","AM437x: kernel init routine execution time regression","am43xx-gpevm"
   "LCPD-26692","Hardware + Software IPSec Performance Test Failures","am43xx-gpevm"

|


.. _release-specific-u-boot-known-issues:

U-Boot Known Issues
-------------------
.. csv-table::
   :header: "Record ID","Platform", "Title","Workaround"
   :widths: 15, 30, 70, 30


|

.. _release-specific-linux-kernel-known-issues:

Linux Kernel Known Issues
-------------------------
.. csv-table::
   :header: "Record ID", "Platform", "Title", "Workaround"
   :widths: 5, 10, 70, 10

   "LCPD-26730","am43xx-gpevm","Stack Exception observed while modetest command in HDMI tests ",""
   "LCPD-25498","am43xx-gpevm","Test to validate poweroff voltage on all voltage domains fails",""
   "LCPD-25272","am43xx-gpevm","Crypto_M_PERF_openssl_perf_software test Fails",""
   "LCPD-24728","am43xx-gpevm","Power measurement with Standby/Suspend/Resume failure",""
   "LCPD-24650","am43xx-gpevm","VPFE sensor capture fails",""
   "LCPD-24505","am43xx-gpevm","KMS properties test failed",""
   "LCPD-24456","am43xx-gpevm,am43xx-hsevm,am437x-idk,am437x-sk","Move IPC validation source from github to git.ti.com",""
   "LCPD-24302","am43xx-gpevm","The speed test built in to OpenSSL - cryptographic",""
   "LCPD-24182","am43xx-gpevm","Powermgr_xs_func_simple_suspend/standby resume tests",""
   "LCPD-17673","am43xx-gpevm","No software documentation for the Timer module",""
   "LCPD-17449","am43xx-gpevm,am43xx-hsevm,am437x-idk,am437x-sk","libasan_preinit.o is missing in devkit",""
   "LCPD-10974","am43xx-gpevm","am43xx-gpevm - usb camera gadget shows halting frames","None"
   "LCPD-9254","am43xx-hsevm","Kernel warnings in boot for am437x-hsevm",""
   "LCPD-7955","am43xx-gpevm","Uncorrectable Bitflip errors seen after switch to SystemD","Workaround to erase the NAND flash completely if flashed with an incompatible flash writer. SystemD tries to mount all partitions and that is the reason this is being seen now."
   "LCPD-1207","am43xx-gpevm","AM43XX/AM57XX/DRA7: CONNECTIVITY: dwc3_omap on am43xx and xhci_plat_hcd on dra7 - removal results in segmentation fault",""


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
