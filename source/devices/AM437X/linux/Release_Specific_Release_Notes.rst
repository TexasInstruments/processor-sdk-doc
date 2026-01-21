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

Release 11.02.05.02
===================

Released November 2025

.. rubric:: What's New
   :name: whats-new

Processor SDK 11.02 Release has following new features:

 - 2025 LTS Stable Update to 6.12.49
 - ICSSM bug fixes
 - Test automation improvements
 - HDMI suport in Linux
 - ARM Analytics AI stack enabled in the filesystem
 - LVGL (Light and Versatile Graphics Library) based interactive demo as out-of-the-box (OOB) on display
 - Added support for McASP async mode: independent transmit (playback) and receive (capture) clocking

.. rubric:: SDK Components & Versions
   :name: sdk-components-versions

+--------------------------+----------------------------+
| Component                | Version                    |
+==========================+============================+
| Linux Kernel             | 6.12.49 (2025 LTS)         |
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

.. list-table::
   :header-rows: 1
   :widths: 15, 30, 30, 30

   * - Component
     - Branch Info
     - Tag Info
     - Config Info
   * - U-Boot
     - `ti-u-boot-2025.01 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/log/?h=ti-u-boot-2025.01>`__
     - `11.02.05 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tag/?h=11.02.05>`__
     - :ref:`Build Config <Build-U-Boot-label>`
   * - Linux Kernel
     - `ti-linux-6.12.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.12.y>`__
     - `11.02.05 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=11.02.05>`__
     - `non-RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-6.12/ti43x/defconfig?h=11.02.05>`__
   * - meta-ti
     - `scarthgap <https://git.yoctoproject.org/meta-ti/log/?h=scarthgap>`__
     - `11.02.05 <https://git.yoctoproject.org/meta-ti/tag/?h=11.02.05>`__
     - |__SDK_BUILD_MACHINE__|
   * - meta-arago
     - `scarthgap <https://git.yoctoproject.org/meta-arago/log/?h=scarthgap>`__
     - `11.02.05 <https://git.yoctoproject.org/meta-arago/tag/?h=11.02.05>`__
     -
   * - meta-tisdk
     - `scarthgap <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/log/?h=scarthgap>`__
     - `11.02.05.02 <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/tag/?h=11.02.05.02>`__
     -

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

   "`EXT_SITMPUSW-146 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-146>`_","Yocto: meta-ti*: kernel source has uncommited changes"
   "`EXT_SITMPUSW-145 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-145>`_","Linux SDK User Manual needs Customer-Accessible Change Log / Revision History"
   "`EXT_EP-12830 <https://sir.ext.ti.com/jira/browse/EXT_EP-12830>`_","Dhrystone performance report contains wrong cpu frequency"
   "`EXT_EP-12067 <https://sir.ext.ti.com/jira/browse/EXT_EP-12067>`_","AM335x/AM437x PRU Ethernet slowdown from kernel 4.19 -> 5.4/5.10"

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
