.. _release-specific-release-notes:

#############
Release Notes
#############

************
Introduction
************

The Processor Software Development Kit for Android provides a fundamental software platform for development, deployment and execution of Android-based application and includes the following:

   * Bootloader components
   * Linux kernel and
   * Android file system


*********
Licensing
*********

Please refer to the software manifest, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page.


****************
Release 10.01.01
****************

Released on March 2025

What's new
==========

* This is a Android 15 based release of Processor SDK Android


Release Features
================

Following features are enabled/tested in this release for AM62x Android:

* **Boot:** eMMC boot, fastboot based flashing, A/B partition
* **Security:** Keymint and gatekeeper implementation with OP-TEE
* **Platform:** SELinux enforced mode with user build, ADB over USB
* **Connectivity:** Ethernet, USB touch, basic USB NCM, CC33XX M.2 Module Wi-Fi support
* **Graphics:** GPU accelerated UI with drm_hwcomposer
* **Audio:** HDMI output and jack audio output/input
* **Multimedia:** SW video decode/encode, USB camera, :ref:`CSI camera <android-csi-camera>`
* **Android Baseport:** Support of Generic System Image
* **Display:** Support for LVDS panel and dual display (mirroring and extended)

SDK Components and Versions
===========================

+------------------------------------+-------------------------------------------------------------------------------+
| **Component**                      |  **Version**                                                                  |
+====================================+===============================================================================+
| **Android**                        | Android 15 / Android 15 Car                                                   |
+------------------------------------+-------------------------------------------------------------------------------+
| **Linux Kernel**                   | Linux 6.6.56                                                                  |
+------------------------------------+-------------------------------------------------------------------------------+
| **Linux Kernel Toolchain**         | clang-r510928                                                                 |
+------------------------------------+-------------------------------------------------------------------------------+
| **U-boot**                         | 2024.04                                                                       |
+------------------------------------+-------------------------------------------------------------------------------+
| **GCC Toolchain**                  | GNU Toolchain for the A-profile Architecture 13.3 (rel1)                      |
+------------------------------------+-------------------------------------------------------------------------------+
| **Base Linux SDK**                 | PROCESSOR-SDK-LINUX-AM62X 10.01.10                                            |
+------------------------------------+-------------------------------------------------------------------------------+
| **Hardware Supported**             | AM62X-SK / AM62X-LP / AM62B-P1 / Beagle Play                                  |
+------------------------------------+-------------------------------------------------------------------------------+

*************
Documentation
*************

- :ref:`android-prebuilts` page provides information on getting started with pre-built binaries and booting the Android images on EVM.
- :ref:`android-building` page provides information on downloading and building the Android images from sources.
- :ref:`android-application-notes` page provides Application Notes.

************
Host Support
************

The Processor SDK is developed, built and verified on Ubuntu 20.04 and 22.04. For all other
versions of host support refer to Android documentation.


************
Known Issues
************

.. list-table::
   :header-rows: 1
   :widths: 10 40 40 10

   * - Issues
     - Description
     - Post Release Fix
     - Component

   * - **SITSW-1387**
     - Mcasp: Buffer underflow console messages seen
     - N/A
     - N/A

   * - **SITSW-1386**
     - Some commands don't work from native console, but work via adb shell
     - N/A
     - N/A

   * - **LCPD-42548**
     - Can't override kernel cmdline in U-Boot
     - `969cb05aea9 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?id=969cb05aea9>`__
       `dca2919115b <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?id=dca2919115b>`__
       `c095b62dfaf <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?id=c095b62dfaf>`__
       `547cdd9aebd <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?id=547cdd9aebd>`__
       `9d802d798ac <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?id=9d802d798ac>`__
     - N/A
