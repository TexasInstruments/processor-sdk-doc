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

.. _release-specific-build-information:

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

.. note::

    - Release Specific Issues including details will be published through Software Incident Report (SIR) portal

    - Further Information can be found at `SIR Portal <https://sir.ext.ti.com/>`_

Errata Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12116","i897: USB Stop Endpoint doesnt work in certain circumstances"
   "EXT_EP-12117","i896: USB Port disable doesnt work"


Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12092","MPU_DPLL miscalculation in AM335x Linux kernel clock drivers"
   "EXT_EP-12089","AM335x/AM437x PRU Remoteproc broken in SDK 9.1"
   "EXT_EP-12087","AM437x: AUTOIDLE bit shouldn't be set in all UART device tree nodes"
   "EXT_EP-12089","AM335x/AM437x PRU Remoteproc broken in SDK 9.1"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12067","AM335x/AM437x PRU Ethernet slowdown from kernel 4.19 -> 5.4/5.10"


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
