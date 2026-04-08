.. _Release-note-label:

#############
Release Notes
#############

Overview
========

The **Processor Software Development Kit (Processor SDK)** is a unified software platform for TI embedded processors
providing easy setup and fast out-of-the-box access to benchmarks and demos. All releases of Processor SDK are
consistent across TI’s broad portfolio, allowing developers to seamlessly reuse and develop software across devices.
Developing a scalable platform solutions has never been easier than with the Processor SDK and TI’s embedded processor
solutions.

To simplify the end user experience, Processor SDK Linux AM62Dx installer provides everything needed as discussed below
to create the embedded system from “scratch” :

-  Platform/board-support software and configuration files for Linux
-  U-Boot and Kernel sources and configuration files
-  An ARM cross-compiling toolchain as well as other host binaries and components
-  A Yocto/OE compliant filesystem and sources for example applications
-  A variety of scripts and Makefiles to automate certain tasks
-  Other components needed to build an embedded system that don’t fit neatly into one of the above buckets
-  Reference Examples, benchmarks

This release supports High Security - Field Securable (HS-FS) devices. For migration guide and other info, refer :ref:`HS-Migration-Guide`

Licensing
=========

Please refer to the software manifests, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page or in the installed directory as indicated below.

-  Linux Manifest:  :file:`<PSDK_PATH>/manifest/software_manifest.htm`

Release 12.00.00.07.04
======================

Released on Apr 2026

What's new
----------

**Processor SDK Linux AM62DX Release has following new features:**

  - First 2026 LTS Reference Release Including RT combined branch model
  - Important Bug Fixes on top of Processor SDK 11.02.08.02 Release.
  - Review Issue Tracker Section for the new fixes.

What's included
---------------

**Key Release References:**

  - Snagfactory Support - :ref:`Snagfactory Tool <Flash-via-Fastboot>`

**Component version:**

  - Kernel 6.18.13
  - U-Boot 2026.01
  - Toolchain GCC 15.2
  - ATF 2.14+
  - OPTEE 4.9.0+
  - TIFS Firmware `v12.00.02 <https://software-dl.ti.com/tisci/esd/12_00_02/release_notes/release_notes.html>`__ (Click on the link for more information)
  - Yocto Master
  - IPC Firmware REL.MCUSDK.K3.12.00.00.04
  - PCM6240 ADC Firmware 1.0.0.0
  - DM Firmware 12.00.00.09

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
     - `12.00.00.07 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tag/?h=12.00.00.07>`__
     - :ref:`Build Config <Build-U-Boot-label>`
   * - TF-A
     - `master <https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/+/refs/heads/master>`__
     - `v2.14+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-bsp/trusted-firmware-a/trusted-firmware-a-ti.inc?h=12.00.00.07#n5>`__
     -
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.9.0+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-security/optee/optee-os-ti-version.inc?h=12.00.00.07#n1>`__
     - |__OPTEE_PLATFORM_FLAVOR__|
   * - Linux Firmware
     - `ti-linux-firmware <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/log/?h=ti-linux-firmware>`__
     - `12.00.00.07 <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tag/?h=12.00.00.07>`__
     -
   * - Linux Kernel
     - `ti-linux-6.18.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.18.y>`__
     - `12.00.00.07 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=12.00.00.07>`__
     - `non-RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-6.18/k3/defconfig?h=12.00.00.07>`__ , `RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-rt-6.18/k3/defconfig?h=12.00.00.07>`__
   * - meta-ti
     - `master <https://git.yoctoproject.org/meta-ti/log/?h=master>`__
     - `12.00.00.07 <https://git.yoctoproject.org/meta-ti/tag/?h=12.00.00.07>`__
     - |__SDK_BUILD_MACHINE__|
   * - meta-arago
     - `master <https://git.yoctoproject.org/meta-arago/log/?h=master>`__
     - `12.00.00.07 <https://git.yoctoproject.org/meta-arago/tag/?h=12.00.00.07>`__
     -
   * - meta-tisdk
     - `master <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/log/?h=scarthgap>`__
     - `12.00.00.07.04 <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/tag/?h=12.00.00.07.04>`__
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

   "`EXT_EP-12128 <https://sir.ext.ti.com/jira/browse/EXT_EP-12128>`_","USB2 PHY locks up due to short suspend"
   "`EXT_EP-12123 <https://sir.ext.ti.com/jira/browse/EXT_EP-12123>`_","USART: Erroneous clear/trigger of timeout interrupt"
   "`EXT_EP-12124 <https://sir.ext.ti.com/jira/browse/EXT_EP-12124>`_","BCDMA: RX Channel can lockup in certain scenarios"
   "`EXT_EP-12114 <https://sir.ext.ti.com/jira/browse/EXT_EP-12114>`_","MMCSD: HS200 and SDR104 Command Timeout Window Too Small"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_SITMPUSW-174 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-174>`_","UDMA: HC/UHC channel allocation fails due to RM config mismatch with CSL defines"
   "`EXT_EP-13163 <https://sir.ext.ti.com/jira/browse/EXT_EP-13163>`_","AM62D: McASP: Wrong sampling rate when do record & play togather"
   "`EXT_EP-13134 <https://sir.ext.ti.com/jira/browse/EXT_EP-13134>`_","McASP not generating clock signal in async mode"
   "`EXT_EP-13135 <https://sir.ext.ti.com/jira/browse/EXT_EP-13135>`_","Linux SDK docs: inconsistent TF-A git repo URL's"
