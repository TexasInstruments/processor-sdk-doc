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
Release 11.00.01
****************

Released on February 2026

What's new
==========

This is a refresh release of Android 16 11.00.00 release addressing below issues:
* Fix for LPM DeepSleep regression
* Fix for Cpufreq regression
* Fix RPI display support
* Fix getrootoftrust security features in factory build mode

Release Features
================

Following features are enabled/tested in this release for AM62Px Android:

* **Boot:** eMMC boot, fastboot based flashing, A/B partition
* **Security:** Keymint and gatekeeper implementation with OP-TEE, device lock/unlock support, custom AVB keys support
* **Platform:** SELinux enforced mode with user build, ADB over USB
* **Connectivity:** Ethernet, USB touch, basic USB NCM, CC33XX M.2 Module Wi-Fi support
* **Graphics:** GPU accelerated UI with drm_hwcomposer
* **Audio:** HDMI output and jack audio output/input
* **Multimedia:** :ref:`HW video decode (h264, hevc) encode (h264) <Android Multimedia Wave5>`, USB camera, :ref:`CSI camera <android-csi-camera>`
* **Android Baseport:** Support of Generic System Image
* **Display:** Support for LVDS panel and dual display (mirroring and extended)
* **Display:** Support for the RPI 7Inch touchscreen DSI panel.

.. _release-specific-build-information:

SDK Components and Versions
===========================

+------------------------------------+-------------------------------------------------------------------------------+
| **Component**                      |  **Version**                                                                  |
+====================================+===============================================================================+
| **Android**                        | Android 16 / Android 16 Car                                                   |
+------------------------------------+-------------------------------------------------------------------------------+
| **Linux Kernel**                   | Linux 6.12.23                                                                 |
+------------------------------------+-------------------------------------------------------------------------------+
| **Linux Kernel Toolchain**         | clang-r530567                                                                 |
+------------------------------------+-------------------------------------------------------------------------------+
| **U-boot**                         | 2025.01                                                                       |
+------------------------------------+-------------------------------------------------------------------------------+
| **GCC Toolchain**                  | GNU Toolchain for the A-profile Architecture 13.3 (rel1)                      |
+------------------------------------+-------------------------------------------------------------------------------+
| **Base Linux SDK**                 | PROCESSOR-SDK-LINUX-AM62PX 11.00.00                                           |
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
     - Android: Seek operation not functional during playback
     - N/A
     - N/A

   * - **SITSW-6901**
     - Android: In middle of video playback relaunching another video results in crash
     - N/A
     - N/A
