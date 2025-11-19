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

Release 11.02
=============

Released November 2025

.. rubric:: What's New
   :name: whats-new

.. note:: As of Dec 2023, Linux SDK for AM65 is in long term maintenance mode. TI will support critical bug fixes and once a year LTS updates but no new development or new features are planned for this device SDK at this time. The SDK is supported and tested on TMDX654IDKEVM. TMDX654GPEVM is no longer supported.

**Processor SDK Linux AM65X Release has following new features:**

 - 2025 LTS Stable Update to 6.12.57
 - ICSSM bug fixes
 - VLAN Multicast filtering on ICSSG
 - ICSSG XDP Support (Zero Copy)
 - Test automation improvements


**Component version:**

  - Kernel 6.12.57
  - RT Kernel 6.12.57
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

U-Boot
------

| Head Commit: a44465cad8a30cbad5e8b22baef59aa7f5151494 TI: dts: arm64: ti: sync dtbs from ti-linux-6.12.y upto 1a86d36433ea
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| Tag: 11.02.05
|

TF-A
----

| Head Commit: e0c4d3903b382bf34f552af53e6d955fae5283ab Merge changes from topic "xlnx_fix_gen_con_datatype" into integration
| Repo: https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git
| Branch: master
| Tag: 2.13+
|

OP-TEE
------

| Head Commit: a9690ae39995af36a31b7a4f446f27ea0787e3a4 plat-k3: drivers: Add TRNG driver support in AM62L
| Repo: https://github.com/OP-TEE/optee_os/
| Branch: master
| Tag: 4.7+
|

ti-linux-firmware
-----------------

| Head Commit: 0a37dc07b1120127eba73c7196a0b532350b9639 ti-ipc: am62x/am62ax/am62px: Update ipc firmware
| Repo: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 11.02.05
|


Kernel
------
.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: 1a86d36433eac7cef246d41fbd4d2bdd9612253f PENDING: arm64: dts: ti: k3-am62p-j722s-common-main: Change reg value for OLDI TX
| Clone: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.02.05
| use-kernel-config=defconfig
| config-fragment=kernel/configs/ti_arm64_prune.config
|

.. rubric:: Real Time (RT) Linux Kernel
   :name: real-time-rt-linux-kernel

| Head Commit: 1a86d36433eac7cef246d41fbd4d2bdd9612253f PENDING: arm64: dts: ti: k3-am62p-j722s-common-main: Change reg value for OLDI TX
| Clone: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.02.05
| use-kernel-config=defconfig
| config-fragment=config-fragment=kernel/configs/ti_arm64_prune.config kernel/configs/ti_rt.config
|


Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: f483464c72055cdcb81853e06afc89719e73073f CI/CD Auto-Merger: cicd.scarthgap.202511140456
| Clone: git://git.yoctoproject.org/meta-ti
| Branch: scarthgap
| Release Tag: 11.02.05
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: 0d3641074b98f79096d415483402e580318249f2 CI/CD Auto-Merger: cicd.scarthgap.202511140456
| Clone: git://git.yoctoproject.org/meta-arago
| Branch: scarthgap
| Release Tag: 11.02.05
|


.. rubric:: meta-tisdk

| Head Commit: 	13c9c57b790a940c8f7b8b6a5d634ef04e3c7f03 meta-ti-foundational: recipes-core: include ti-lvgl-demo
| Clone: git://git.ti.com/ti-sdk-linux/meta-tisdk.git
| Branch: scarthgap
| Release Tag:
|


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
