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
Release 10.00.00
****************

Released on July 2024

What's new
==========

* This is a Android 14 based release of Processor SDK Android


Release Features
================

Following features are enabled/tested in this release for AM62Px Android:

* **Boot:** eMMC boot, fastboot based flashing, A/B partition
* **Security:** Keymint and gatekeeper implementation with OP-TEE
* **Platform:** SELinux enforced mode with user build, ADB over USB
* **Connectivity:** Ethernet, USB touch, CC33XX M.2 Module Wi-Fi support
* **Graphics:** GPU accelerated UI with drm_hwcomposer
* **Audio:** HDMI output and jack audio output/input
* **Multimedia:** :ref:`HW video decode (h264, hevc) encode (h264) <Android Multimedia Wave5>`, USB camera, :ref:`CSI camera <android-csi-camera>`
* **Android Baseport:** Support of Generic System Image
* **Display:** Support for LVDS panel and dual display (mirroring and extended)

SDK Components and Versions
===========================

+------------------------------------+-------------------------------------------------------------------------------+
| **Component**                      |  **Version**                                                                  |
+====================================+===============================================================================+
| **Android**                        | Android 14 / Android 14 Car                                                   |
+------------------------------------+-------------------------------------------------------------------------------+
| **Linux Kernel**                   | Linux 6.1.78 (6.6.30 preview available)                                       |
+------------------------------------+-------------------------------------------------------------------------------+
| **Linux Kernel Toolchain**         | clang-r487747c                                                                |
+------------------------------------+-------------------------------------------------------------------------------+
| **U-boot**                         | 2023.04 (2024.04 preview available)                                           |
+------------------------------------+-------------------------------------------------------------------------------+
| **GCC Toolchain**                  | GNU Toolchain for the A-profile Architecture 13.2 (rel1)                      |
+------------------------------------+-------------------------------------------------------------------------------+
| **Base Linux SDK**                 | PROCESSOR-SDK-LINUX-AM62PX 10.00.07                                           |
+------------------------------------+-------------------------------------------------------------------------------+
| **Hardware Supported**             | AM62PX-SK                                                                     |
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

   * - **SITSW-4268**
     - Android: Seek operation not functional
     - N/A
     - N/A

   * - **SITSW-5071**
     - U-Boot 2024.04 crashes with ``adtbo_idx=1``
     - https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2024.04&id=afd0e59eb7bfce8945635e36562ee03046cc489b
     - N/A

   * - **SITSW-1387**
     - Mcasp: Buffer underflow console messages seen
     - N/A
     - N/A

   * - **SITSW-1386**
     - Some commands don't work from native console, but work via adb shell
     - N/A
     - N/A
