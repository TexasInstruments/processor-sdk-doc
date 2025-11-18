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

Release 11.02
=============

Released November 2025

.. rubric:: What's New
   :name: whats-new

Processor SDK 11.02 Release has following new features:

 - 2025 LTS Stable Update to 6.12.57
 - New platform: Beaglebone Green Eco support
 - ICSSM bug fixes
 - Test automation improvements

|

.. rubric:: SDK Components & Versions
   :name: sdk-components-versions

+--------------------------+----------------------------+
| Component                | Version                    |
+==========================+============================+
| Linux Kernel             | 6.12.57 (2025 LTS)         |
+--------------------------+----------------------------+
| U-Boot                   | 2025.01                    |
+--------------------------+----------------------------+
| Yocto Project            | 5.0 (Scarthgap)            |
+--------------------------+----------------------------+
| ARM Toolchain (gcc)      | 13.4+                      |
+--------------------------+----------------------------+

|

Supported Platforms
===================
See :ref:`here <release-specific-supported-platforms-and-versions>` for a list of supported platforms and links to more information.

|

.. _release-specific-build-information:

Build Information
=================

U-Boot
------

| Head Commit: a44465cad8a30cbad5e8b22baef59aa7f5151494 TI: dts: arm64: ti: sync dtbs from ti-linux-6.12.y upto 1a86d36433ea
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| Tag: 11.02.05
|

.. _release-specific-build-information-kernel:

Kernel
------

.. _release-specific-build-information-linux-kernel:

.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: 1a86d36433eac7cef246d41fbd4d2bdd9612253f PENDING: arm64: dts: ti: k3-am62p-j722s-common-main: Change reg value for OLDI TX
| Clone: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.1.y
| Tag: 11.02.05
|

.. _release-specific-build-information-rt-linux-kernel:

.. rubric:: Real Time (RT) Linux Kernel
   :name: real-time-rt-linux-kernel

| There will be no am3* RT Linux kernel support this release
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

| Head Commit: f483464c72055cdcb81853e06afc89719e73073f CI/CD Auto-Merger: cicd.scarthgap.202511140456
| Clone: git://git.yoctoproject.org/meta-ti
| Branch: scarthgap
| Release Tag: 11.02.05
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: 0d3641074b98f79096d415483402e580318249f2 CI/CD Auto-Merger: cicd.scarthgap.202511140456
| Clone: git://git.yoctoproject.org/meta-arago
| Branch: scarthgap
| Release Tag: 11.02.05
|

.. rubric:: meta-tisdk
   :name: meta-tisdk

| Head Commit: 	13c9c57b790a940c8f7b8b6a5d634ef04e3c7f03 meta-ti-foundational: recipes-core: include ti-lvgl-demo
| Clone: git://git.ti.com/ti-sdk-linux/meta-tisdk.git
| Branch: scarthgap
| Release Tag:
|

Issues Tracker
==============

.. note::

    - Release Specific Issues including details will be published through Software Incident Report (SIR) portal

    - Further Information can be found at `SIR Portal <https://sir.ext.ti.com/>`_


Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXTSYNC-4980","AM335x: UART and GPIO Wakeup from Standby Failed"
   "EXTSYNC-6118","AM335x DDR initialization timing incorrect in DDR driver"


Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXTSYNC-5849","PRU RPMsg swaps which message is sent to which core"
   "EXTSYNC-5814","Does Remoteproc driver for PRU-ICSS still zero out memory?"
   "EXTSYNC-6119","tilcdc faults during device init"


.. rubric:: Installation and Usage
   :name: installation-and-usage

The :ref:`Software Developer's Guide <linux-index>` provides instructions on how to setup up your Linux development
environment, install the SDK and start your development.  It also includes User's Guides for various Example Applications and Code
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
