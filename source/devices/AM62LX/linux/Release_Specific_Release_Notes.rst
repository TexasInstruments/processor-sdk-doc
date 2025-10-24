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

To simplify the user experience, Processor SDK Linux AM62L installer provides everything needed as discussed below
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

**Processor SDK Linux AM62LX Release has following new features:**

  - Supported AM62Lx SR1.1 Only
  - New 2-Stage A53 Boot Flow including OPTEE
  - ATF Based Device Manager including SCMI
  - Tools: :ref:`K3conf <How-to-use-k3conf-label>`
  - U-Boot: Legacy Boot Flow, Boot modes (UART, MMCSD, OSPI), GPMC NAND, CPSW, DMA
  - U-Boot: :ref:`User and Reduced Bootmode OTP Programming  <programming-user-otp-fuses-label>`
  - U-Boot: :ref:`Key writer lite Programming <key-writer-lite-label>`
  - Kernel: RTC, DMA, GPIO, I2C, UART, MMCSD, OSPI NOR, eCAP, eQEP, CPSW, McASP/Audio, DSS, DSI
  - Kernel: :ref:`DTHEv2 Crypto Accelerator <DTHEv2-Crypto-Accelerator>` AES, SHA, MD5, HMAC
  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Support for Wifi with M2 CC33xx cards - :ref:`How to Enable M.2-CC33xx in Linux <enable_m2cc3301>`
  - Out-of-Box experience based on LVGL (Light and Versatile Graphics Library) - :ref:`TI LVGL Demo - User Guide <TI-LVGL-Demo-User-Guide-label>`
  - Jailhouse with Kernel 6.12
  - Debian distribution based on Armbian
  - Support for multiple Linux distributions, such as Yocto, Debian and Buildroot

**Component version:**

  - Kernel (Including RT) 6.12.43
  - U-Boot 2025.01
  - Toolchain GCC 13.4
  - ATF 2.12+
  - TIFS Firmware `v11.01.12 <https://software-dl.ti.com/tisci/esd/11_01_12/release_notes/release_notes.html>`__ (Click on the link for more information)
  - Yocto scarthgap 5.0
  - Armbian-based Debian 13 (Trixie)
  - Buildroot 2024.11.1

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
     - `ti-master <https://github.com/TexasInstruments/arm-trusted-firmware/tree/ti-master>`__
     - `v2.12+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-bsp/trusted-firmware-a/trusted-firmware-a-ti.inc?h=11.01.16#n11>`__
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


Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_SITMPUSW-165 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-165>`_","inapplicable wl18xx message in Linux boot log"
   "`EXT_EP-12816 <https://sir.ext.ti.com/jira/browse/EXT_EP-12816>`_","SDK Docs: Broken URL in How To Guides > EVM Setup"
   "`EXT_EP-12780 <https://sir.ext.ti.com/jira/browse/EXT_EP-12780>`_","AM62L Dynamic IP address cannot be obtained when eth interface brought down with command"
   "`EXT_EP-12674 <https://sir.ext.ti.com/jira/browse/EXT_EP-12674>`_","AM62L: Enabling wkup uart causes Linux console (main_uart0) garbled"
   "`EXT_EP-12340 <https://sir.ext.ti.com/jira/browse/EXT_EP-12340>`_","Suspend-to-RAM failure: tps65219: device creates a circular dependency and device fails to enter suspend"
   "`EXT_EP-12977 <https://sir.ext.ti.com/jira/browse/EXT_EP-12977>`_","AM62L: PM: add missing PDs (devices) in the scmi wrapper"
   "`EXT_EP-12973 <https://sir.ext.ti.com/jira/browse/EXT_EP-12973>`_","AM62L: Suspend-Resume (RTC+DDR): MMC fails"
   "`EXT_EP-12976 <https://sir.ext.ti.com/jira/browse/EXT_EP-12976>`_","DSI fails to reconnect after suspend/resume"
   "`EXT_EP-12975 <https://sir.ext.ti.com/jira/browse/EXT_EP-12975>`_","DSS clock warnings appear during suspend/resume when HDMI is connected"
   "`EXT_EP-12784 <https://sir.ext.ti.com/jira/browse/EXT_EP-12784>`_","AM62L: LPM: 2nd core randomly fails to come online during suspend/resume"
   "`EXT_EP-12778 <https://sir.ext.ti.com/jira/browse/EXT_EP-12778>`_","AM62L: PG1.1: PM: during clock init the pm driver is touching wkup PLL"
   "`EXT_EP-12974 <https://sir.ext.ti.com/jira/browse/EXT_EP-12974>`_","AM62L: Heartbeat LED stops blinking on resume from RTC+DDR"
   "`EXT_EP-12978 <https://sir.ext.ti.com/jira/browse/EXT_EP-12978>`_","AM62L: Suspend-Resume (RTC+DDR): spi-nor resume() fails"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-12970 <https://sir.ext.ti.com/jira/browse/EXT_EP-12970>`_","AM6x - Sitara Socs MCASP and BCDMA issue."
   "`EXT_EP-12980 <https://sir.ext.ti.com/jira/browse/EXT_EP-12980>`_","AM62L: Random kernel crash observed on stress test"
   "`EXT_EP-12979 <https://sir.ext.ti.com/jira/browse/EXT_EP-12979>`_","AM62L: Suspend-Resume (RTC+DDR): davinci_mdio timed out waiting for user access"

