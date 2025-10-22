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

To simplify the user experience, Processor SDK Linux AM62Px installer provides everything needed as discussed below
to create the embedded system from “scratch” :

-  Platform/board-support software and configuration files for Linux
-  U-Boot and Kernel sources and configuration files
-  An ARM cross-compiling toolchain as well as other host binaries and components
-  A Yocto/OE compliant filesystem and sources for example applications
-  A variety of scripts and Makefiles to automate certain tasks
-  Other components needed to build an embedded system that don’t fit neatly into one of the above buckets
-  Reference Examples, benchmarks

This release supports High Security - Field Securable (HS-FS) devices.

Licensing
=========

Please refer to the software manifests, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page or in the installed directory as indicated below.

-  Linux Manifest:  :file:`<PSDK_PATH>/manifest/software_manifest.htm`


Release 11.01.16.13
===================

Released on Oct 2025

What's new
----------

**Processor SDK Linux AM62PX Release has following new features:**

  - Third 2025 LTS Reference Release Including RT combined branch model
  - Supported AM62Px SR 1.2 with eMMC HS400 mode
  - Important Bug Fixes on top of Processor SDK 11.01.05.03 Release.
  - Review Issue Tracker Section for the new fixes.

**Key Release References:**

  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Falcon mode through R5 SPL :ref:`U-Boot Falcon Mode <U-Boot-Falcon-Mode>`
  - Support for streaming from multiple OV5640 cameras with `Arducam V3Link (Fusion Mini) <https://www.arducam.com/product/arducam-v3link-camera-kit-for-ti-development-boards/>`_
  - TISCI: A53 hosts default priv_id value updated to 1 from 4 (to match all other SOCs)
  - How standby power mode works - :ref:`CPUIdle Documentation <cpuidle-guide>`
  - Out-of-Box TI Apps Launcher Application with Qt6 Framework - :ref:`TI Apps Launcher <TI-Apps-Launcher-User-Guide-label>`
  - Snagfactory Support - :ref:`Snagfactory Tool <Flash-via-Fastboot>`
  - Support for M2 CC33xx cards on Debian - `How to Enable M.2-CC33x1 in Linux <https://software-dl.ti.com/processor-sdk-linux/esd/AM62PX/10_01_10_04_Debian/exports/docs/linux/How_to_Guides/Target/How_To_Enable_M2CC3301_in_linux.html>`__


**Component version:**

  - Kernel 6.12.43
  - U-Boot 2025.01
  - Toolchain GCC 13.4
  - ATF 2.13+
  - OPTEE 4.7.0+
  - Graphics DDK 24.2
  - TIFS Firmware / SYSFW `v11.01.05d <https://software-dl.ti.com/tisci/esd/11_01_05/release_notes/release_notes.html>`__ (Click on the link for more information)
  - DM Firmware 11.01.01.04
  - Yocto scarthgap 5.0

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
     - `11.01.16 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tag/?h=11.01.16>`__
     - :ref:`Build Config <Build-U-Boot-label>`
   * - TF-A
     - `master <https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/+/refs/heads/master>`__
     - `v2.13+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-bsp/trusted-firmware-a/trusted-firmware-a-ti.inc?h=11.01.16#n3>`__
     -
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.7.0+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-security/optee/optee-os-ti-version.inc?h=11.01.16#n1>`__
     - |__OPTEE_PLATFORM_FLAVOR__|
   * - Linux Firmware
     - `ti-linux-firmware <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/log/?h=ti-linux-firmware>`__
     - `11.01.16 <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tag/?h=11.01.16>`__
     -
   * - Linux Kernel
     - `ti-linux-6.12.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.12.y>`__
     - `11.01.16 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=11.01.16>`__
     - `non-RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-6.12/k3/defconfig?h=11.01.16>`__ , `RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-rt-6.12/k3/defconfig?h=11.01.16>`__
   * - meta-ti
     - `scarthgap <https://git.yoctoproject.org/meta-ti/log/?h=scarthgap>`__
     - `11.01.16 <https://git.yoctoproject.org/meta-ti/tag/?h=11.01.16>`__
     - |__SDK_BUILD_MACHINE__|
   * - meta-arago
     - `scarthgap <https://git.yoctoproject.org/meta-arago/log/?h=scarthgap>`__
     - `11.01.16 <https://git.yoctoproject.org/meta-arago/tag/?h=11.01.16>`__
     -
   * - meta-tisdk
     - `scarthgap <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/log/?h=scarthgap>`__
     - `11.01.16.13 <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/tag/?h=11.01.16.13>`__
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
   "`EXT_EP-12124 <https://sir.ext.ti.com/jira/browse/EXT_EP-12124>`_","BCDMA: RX Channel can lockup in certain scenarios"
   "`EXT_EP-12114 <https://sir.ext.ti.com/jira/browse/EXT_EP-12114>`_","MMCSD: HS200 and SDR104 Command Timeout Window Too Small"
   "`EXT_EP-12294 <https://sir.ext.ti.com/jira/browse/EXT_EP-12294>`_","MMCHS: eMMC HS400 tDCD timing marginal to JEDEC spec"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_SITMPUSW-166 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-166>`_","ti-apps-launcher: Incomplete Demo Build steps"
   "`EXT_SITMPUSW-165 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-165>`_","inapplicable wl18xx message in Linux boot log"
   "`EXT_SITMPUSW-143 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-143>`_","Yocto Documentation: AM6x: SDK: Build Instruction missing steps for building K3R5 baremetal toolchain"
   "`EXT_EP-12816 <https://sir.ext.ti.com/jira/browse/EXT_EP-12816>`_","SDK Docs: Broken URL in How To Guides > EVM Setup"
   "`EXT_EP-12782 <https://sir.ext.ti.com/jira/browse/EXT_EP-12782>`_","SDK Doc: toolchain information is out of date"
   "`EXT_SITMPUSW-146 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-146>`_","Yocto: meta-ti*: kernel source has uncommited changes"
   "`EXT_EP-12824 <https://sir.ext.ti.com/jira/browse/EXT_EP-12824>`_","AM62P SR1.1 CPUFreq shows 800MHz instead of 1.4GHz"
   "`EXT_EP-12833 <https://sir.ext.ti.com/jira/browse/EXT_EP-12833>`_","AM62P PG1.1 CPU Freq show only 200-800MHz."

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-12825 <https://sir.ext.ti.com/jira/browse/EXT_EP-12825>`_","AM62P DFU log:dwc3-am62 usb@f900000: unable to get ti,syscon-phy-pll-refclk regmap"
   "`EXT_EP-12792 <https://sir.ext.ti.com/jira/browse/EXT_EP-12792>`_","CSI-2 Rx driver shall support frame width that is not 16-byte-aligned"
   "`EXT_EP-12747 <https://sir.ext.ti.com/jira/browse/EXT_EP-12747>`_","Codec: Wave5: Improve Decoder Performance and Fix SError Crash on Fluster test"
   "`EXT_EP-12969 <https://sir.ext.ti.com/jira/browse/EXT_EP-12969>`_","am62p: u-boot abort with 2GB DDR"
   "`EXT_EP-12970 <https://sir.ext.ti.com/jira/browse/EXT_EP-12970>`_","AM6x - Sitara Socs MCASP and BCDMA issue."
   "`EXT_EP-12972 <https://sir.ext.ti.com/jira/browse/EXT_EP-12972>`_","RPMsg zerocopy example: CMA allocation is broken"

