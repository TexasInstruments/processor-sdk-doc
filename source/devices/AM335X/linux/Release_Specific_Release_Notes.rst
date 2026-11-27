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

Release versioning scheme
=========================

Processor SDK releases follow the 5-duplet versioning scheme ``YY.RR.EE.CC.SS``, where:

- ``YY`` - Yearly baseline. Increments with each new LTS baseline.
- ``RR`` - Release index within the yearly baseline. Each yearly baseline includes many stable releases.
- ``EE`` - Extended release index within a stable baseline.
- ``CC`` - Release Candidate for common foundational BSP components such as Linux, U-Boot, ATF, OPTEE, Firmware and OE manifest including meta-ti, meta-arago.
- ``SS`` - SDK Release identifier for Distro layers (Yocto meta-tisdk, Armbian, Buildroot) with OOB Demos and Installers.

Licensing
=========

Please refer to the software manifests, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page or in the installed directory as indicated below.

-  Linux Manifest:  :file:`<PSDK_PATH>/manifest/software_manifest.htm`

Software Bill of Materials (SBOM)
=================================

|__SDK_FULL_NAME__| releases include Software Bill of Materials (SBOM) files in SPDX 3.0
format for Yocto and CycloneDX 1.6 format for Buildroot. SBOMs for all released artifacts
are bundled into a single archive and can be found on the |__SDK_DOWNLOAD_URL__|.
For more refer :ref:`Working with SBOM <how-to-work-with-sbom>`.

Release 12.02.00.07.05
======================

Released on December 2026

What's new
----------

.. note:: As of Dec 2023, Linux SDK for AM335x is in long term maintenance mode. TI will support critical bug fixes and once a year LTS updates but no new development or new features are planned for this device SDK at this time. The SDK is supported and tested on BEAGL-BONE-GRN-ECO.

**Processor SDK Linux AM335X Release has following new features:**

  - New platform: `BEAGL-BONE-GRN-ECO <https://www.ti.com/tool/BEAGL-BONE-GRN-ECO>`__ support
  - RT-Linux Support
  - ICSSM bug fixes
  - ARM Analytics AI stack enabled in the filesystem
  - LVGL (Light and Versatile Graphics Library) based interactive demo as out-of-the-box (OOB) on display
  - Web-based dashboard (port 3000) for real-time CPU performance and Arm Audio analytics demo via standard web browser
  - Added support for McASP async mode: independent transmit (playback) and receive (capture) clocking
  - Review Issue Tracker Section for the new fixes.

**Key Release References:**


**Component version:**

  - Kernel 6.18.63
  - U-Boot 2026.01
  - Toolchain GCC 15.3
  - Yocto Wrynose/6.0
  - Graphics DDK 1.17

.. _release-specific-build-information:


Build Information
=================

Arago (Yocto/OE)
----------------

.. list-table::
   :header-rows: 1
   :widths: 15, 30, 30, 30

   * - Component
     - Branch Info
     - Tag Info
     - Config Info
   * - U-Boot
     - `ti-u-boot-2026.01 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/log/?h=ti-u-boot-2026.01>`__
     - `12.02.00.07 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tag/?h=12.02.00.07>`__
     - :ref:`Build Config <Build-U-Boot-label>`
   * - Linux Firmware
     - `ti-linux-firmware <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/log/?h=ti-linux-firmware>`__
     - `12.02.00.07 <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tag/?h=12.02.00.07>`__
     -
   * - Linux Kernel
     - `ti-linux-6.18.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.18.y>`__
     - `12.02.00.07 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=12.02.00.07>`__
     - `non-RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-6.18/ti33x/defconfig?h=12.02.00.07>`__
   * - RT-Linux Kernel
     - `ti-rt-linux-6.18.y-arm32 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-rt-linux-6.18.y-arm32>`__
     - `12.02.00.07-rt <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=12.02.00.07-rt>`__
     - `RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-rt-6.18/ti33x/defconfig?h=12.02.00.07>`__
   * - meta-ti
     - `wrynose <https://git.yoctoproject.org/meta-ti/log/?h=wrynose>`__
     - `12.02.00.07 <https://git.yoctoproject.org/meta-ti/tag/?h=12.02.00.07>`__
     - |__SDK_BUILD_MACHINE__|
   * - meta-arago
     - `wrynose <https://git.yoctoproject.org/meta-arago/log/?h=wrynose>`__
     - `12.02.00.07 <https://git.yoctoproject.org/meta-arago/tag/?h=12.02.00.07>`__
     -
   * - meta-tisdk
     - `wrynose <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/log/?h=wrynose>`__
     - `12.02.00.07.05 <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/tag/?h=12.02.00.07.05>`__
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
   "`EXT_EP-13174 <https://sir.ext.ti.com/jira/browse/EXT_EP-13174>`_","AM335x DDR initialization timing incorrect in DDR driver"
   "`EXT_EP-12079 <https://sir.ext.ti.com/jira/browse/EXT_EP-12079>`_","AM335x: UART and GPIO Wakeup from Standby Failed"
   "`EXT_EP-12056 <https://sir.ext.ti.com/jira/browse/EXT_EP-12056>`_","8250_omap: incorrect handling of dma->rx_running flag"
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
