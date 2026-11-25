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

.. note:: As of Dec 2023, Linux SDK for AM65 is in long term maintenance mode. TI will support critical bug fixes and once a year LTS updates but no new development or new features are planned for this device SDK at this time. The SDK is supported and tested on TMDX654IDKEVM. TMDX654GPEVM is no longer supported.

**Processor SDK Linux AM65X Release has following new features:**

  - 2026 LTS Stable Update to 6.18.63 and common RT-kernel branch
  - ICSSM bug fixes
  - VLAN Multicast filtering on ICSSG
  - ICSSG XDP Support (Zero Copy)
  - ARM Analytics AI stack enabled in the filesystem
  - LVGL (Light and Versatile Graphics Library) based interactive demo as out-of-the-box (OOB) on display
  - Added support for McASP async mode: independent transmit (playback) and receive (capture) clocking
  - Review Issue Tracker Section for the new fixes.

**Key Release References:**

  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`

**Component version:**

  - Kernel 6.18.63
  - U-Boot 2026.01
  - Toolchain GCC 15.3
  - ATF 2.15
  - OPTEE 4.11
  - TIFS Firmware `v12.02.02 <https://software-dl.ti.com/tisci/esd/12_02_02/release_notes/release_notes.html>`__ (Click on the link for more information)
  - Yocto Wrynose/6.0
  - Graphics DDK 1.17

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
     - `ti-u-boot-2026.01 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/log/?h=ti-u-boot-2026.01>`__
     - `12.02.00.07 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tag/?h=12.02.00.07>`__
     - :ref:`Build Config <Build-U-Boot-label>`
   * - TF-A
     - `master <https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/+/refs/heads/master>`__
     - `v2.15 <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-bsp/trusted-firmware-a/trusted-firmware-a-ti.inc?h=12.02.00.07#n5>`__
     -
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.11.0 <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-security/optee/optee-os-ti-version.inc?h=12.02.00.07#n1>`__
     - |__OPTEE_PLATFORM_FLAVOR__|
   * - Linux Firmware
     - `ti-linux-firmware <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/log/?h=ti-linux-firmware>`__
     - `12.02.00.07 <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tag/?h=12.02.00.07>`__
     -
   * - Linux Kernel
     - `ti-linux-6.18.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.18.y>`__
     - `12.02.00.07 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=12.02.00.07>`__
     - `non-RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-6.18/k3/defconfig?h=12.02.00.07>`__ , `RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-rt-6.18/k3/defconfig?h=12.02.00.07>`__
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
