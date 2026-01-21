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

Release 11.02.05.02
===================

Released November 2025

.. rubric:: What's New
   :name: whats-new

.. note:: As of Dec 2023, Linux SDK for AM65 is in long term maintenance mode. TI will support critical bug fixes and once a year LTS updates but no new development or new features are planned for this device SDK at this time. The SDK is supported and tested on TMDX654IDKEVM. TMDX654GPEVM is no longer supported.

**Processor SDK Linux AM65X Release has following new features:**

 - 2025 LTS Stable Update to 6.12.49
 - ICSSM bug fixes
 - VLAN Multicast filtering on ICSSG
 - ICSSG XDP Support (Zero Copy)
 - ARM Analytics AI stack enabled in the filesystem
 - LVGL (Light and Versatile Graphics Library) based interactive demo as out-of-the-box (OOB) on display
 - Added support for McASP async mode: independent transmit (playback) and receive (capture) clocking

**Component version:**

  - Kernel 6.12.49
  - RT Kernel 6.12.49
  - U-Boot 2025.01
  - Toolchain GCC 13.4+
  - ATF 2.13+
  - OPTEE 4.7+
  - Graphics DDK 1.17
  - SYSFW v11.02.05
  - Yocto Scarthgap


Supported Platforms
===================
See :ref:`here <release-specific-supported-platforms-and-versions>` for a list of supported platforms and links to more information.

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
   * - TF-A
     - `master <https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/+/refs/heads/master>`__
     - `v2.13+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-bsp/trusted-firmware-a/trusted-firmware-a-ti.inc?h=11.02.05#n3>`__
     -
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.7.0+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-security/optee/optee-os-ti-version.inc?h=11.02.05#n1>`__
     - |__OPTEE_PLATFORM_FLAVOR__|
   * - Linux Firmware
     - `ti-linux-firmware <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/log/?h=ti-linux-firmware>`__
     - `11.02.05 <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tag/?h=11.02.05>`__
     -
   * - Linux Kernel
     - `ti-linux-6.12.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.12.y>`__
     - `11.02.05 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=11.02.05>`__
     - `non-RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-6.12/k3/defconfig?h=11.02.05>`__ , `RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-rt-6.12/k3/defconfig?h=11.02.05>`__
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

Errata Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-12052 <https://sir.ext.ti.com/jira/browse/EXT_EP-12052>`_","PRU_ICSSG: DOC: Undefined labels"
   "`EXT_EP-12118 <https://sir.ext.ti.com/jira/browse/EXT_EP-12118>`_","PCI-Express: GEN3 (8GT/s) Operation Not Supported"
   "`EXT_EP-12121 <https://sir.ext.ti.com/jira/browse/EXT_EP-12121>`_","USB: USB2PHY Charger Detect is enabled by default without VBUS presence"
   "`EXT_EP-12120 <https://sir.ext.ti.com/jira/browse/EXT_EP-12120>`_","DSS : DSS Does Not Support YUV Pixel Data Formats"
   "`EXT_EP-12119 <https://sir.ext.ti.com/jira/browse/EXT_EP-12119>`_","USB: SuperSpeed USB Non-Functional"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_SITMPUSW-146 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-146>`_","Yocto: meta-ti*: kernel source has uncommited changes"
   "`EXT_SITMPUSW-145 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-145>`_","Linux SDK User Manual needs Customer-Accessible Change Log / Revision History"
   "`EXT_EP-13129 <https://sir.ext.ti.com/jira/browse/EXT_EP-13129>`_","cpsw: probe failed if CONFIG_DEBUG_FS is disabled"
   "`EXT_EP-12226 <https://sir.ext.ti.com/jira/browse/EXT_EP-12226>`_","Backport ""board: ti: common: Kconfig: add CMD_CACHE"" into TI U-Boot Tree"
   "`EXT_EP-13147 <https://sir.ext.ti.com/jira/browse/EXT_EP-13147>`_","padconfig: ST_EN bit not preserved"
   "`EXT_EP-12344 <https://sir.ext.ti.com/jira/browse/EXT_EP-12344>`_","SDK DOC: Both MII ports still have to be enabled in single port case"
   "`EXT_EP-12111 <https://sir.ext.ti.com/jira/browse/EXT_EP-12111>`_","Linux SDK v10.0: TI-added support for W25N01JW SPI NAND breaks other existing Flash support"
   "`EXT_EP-12048 <https://sir.ext.ti.com/jira/browse/EXT_EP-12048>`_","am654x-idk DFU boot is failing"
   "`EXT_EP-12828 <https://sir.ext.ti.com/jira/browse/EXT_EP-12828>`_","Fix order of MCU R5 shutdown depending on cluster mode"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-12818 <https://sir.ext.ti.com/jira/browse/EXT_EP-12818>`_","PRU RPMsg swaps which message is sent to which core"
   "`EXT_EP-12080 <https://sir.ext.ti.com/jira/browse/EXT_EP-12080>`_","AM654x: USB MSC boot mode fails"

Installation and Usage
======================

The :ref:`Software Developer's Guide <linux-index>` provides instructions on how to setup up your Linux development
environment, install the SDK and start your development.  It also includes User's Guides for various Example Applications and Code
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
