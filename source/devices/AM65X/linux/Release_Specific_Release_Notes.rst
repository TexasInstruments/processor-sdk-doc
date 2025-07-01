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

Release 09.03.05.02
===================

Released December 2024

.. rubric:: What's New
   :name: whats-new

.. note:: As of Dec 2023, Linux SDK for AM65 is in long term maintenance mode. TI will support critical bug fixes and once a year LTS updates but no new development or new features are planned for this device SDK at this time. The SDK is supported and tested on TMDX654IDKEVM. TMDX654GPEVM is no longer supported.

**Processor SDK Linux AM65X Release has following new features:**

  - LTS Stable Kernel update to 6.1.119
  - Important Bug Fixes on top of Processor SDK 09.01.00.007 Release


**Component version:**

  - Kernel 6.1.119
  - RT Kernel 6.1.119-rt45
  - U-Boot 2023.04
  - Toolchain GCC 11.5
  - ATF 2.10+
  - OPTEE 4.1.0
  - Graphics DDK 1.17
  - SYSFW v10.01.08
  - Yocto Kirkstone


Supported Platforms
===================
See :ref:`here <release-specific-supported-platforms-and-versions>` for a list of supported platforms and links to more information.


.. _release-specific-sdk-components-versions:

.. _release-specific-build-information:

Build Information
=================

.. _u-boot-release-notes:

U-Boot
------

| Head Commit: 2a13324ec63cc488f5f578886d0cf6ece348dfda arm: dts: am335x: Use PWM for LCD backlight
| uBoot Version: 2023.04
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2023.04
| uBoot Tag: 09.03.05
|

.. _tf-a-release-notes:

TF-A
----

| Head Commit: 00f1ec6b8740ccd403e641131e294aabacf2a48b Merge changes from topic "revert-ti-dm-workaround" into integration
| Repo: https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git
| Branch: master
| Tag: 2.10+
|

.. _optee-release-notes:

OP-TEE
------

| Head Commit: 012cdca49db398693903e05c42a254a3a0c0d8f2 plat-k3: drivers: sec_proxy: increment while reading trail bytes
| Repo: https://github.com/OP-TEE/optee_os/
| Branch: master
| Tag: 4.1.0
|

.. _ti-linux-fw-release-notes:

ti-linux-firmware
-----------------

| Head Commit: 1eaf07dc4ec5cdeb98078f17a9d4635e88f43f75 ti-dm: Update display sharing firmware for am62px
| Clone: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 09.03.05
|


Kernel
------
.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: c490f4c0fe51281818c45159c0fbed94f852978e HACK: arm: dts: am57: disable late attach as default
| Kernel Version: 6.1.119

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.1.y
| Tag: 09.03.05
| use-kernel-config=defconfig
| config-fragment=kernel/configs/ti_arm64_prune.config
|

.. rubric:: Real Time (RT) Linux Kernel
   :name: real-time-rt-linux-kernel

| Head Commit: b0f9de804a162329bc81857ad50947311228dfb2 Merge branch 'ti-linux-6.1.y-cicd' into ti-rt-linux-6.1.y-cicd
| Kernel Version: 6.1.119-rt45

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-rt-linux-6.1.y
| Tag: 09.03.05-rt
| use-kernel-config=defconfig
| config-fragment=config-fragment=kernel/configs/ti_arm64_prune.config kernel/configs/ti_rt.config
|


Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: 963140e3b5820d6ebf54a4418946a628e0fea2c6 CI/CD Auto-Merger: cicd.kirkstone.202412041235
| Version: Kirkstone-4.0
| Clone: git://git.yoctoproject.org/meta-ti
| Branch: kirkstone
| Release Tag: 09.03.05
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: f59caa5f47a625ef9eecada069ae6a74c70bcc47 CI/CD Auto-Merger: cicd.kirkstone.202412041235
| Version: Kirkstone-4.0
| Clone: git://git.yoctoproject.org/meta-arago
| Branch: kirkstone
| Release Tag: 09.03.05
|


.. rubric:: meta-tisdk

| Head Commit: 2ee8bead9d04afcb61234738e0d9a644395d27bf recipes-core: packagegroups: Drop SGX sources from am65xx
| Version: Kirkstone-4.0
| Clone:  git://git.ti.com/ti-sdk-linux/meta-tisdk.git
| Branch: kirkstone
| Release Tag: 09.03.05.02
|



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

   "EXT_EP-12052","PRU_ICSSG: DOC: Undefined labels"
   "EXT_EP-12118","PCI-Express: GEN3 (8GT/s) Operation Not Supported."
   "EXT_EP-12121","USB: USB2PHY Charger Detect is enabled by default without VBUS presence"
   "EXT_EP-12120","DSS : DSS Does Not Support YUV Pixel Data Formats"
   "EXT_EP-12119","USB:  SuperSpeed USB Non-Functional"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12108","audit for potential bugs with 6.6.44 stable merge "
   "EXT_EP-12050","AM642-EVM: PCIe0 EP node is not defined"
   "EXT_EP-12098","Uboot docs: document renaming tiboot3-<evm>.bin file"
   "EXT_EP-12053","AM65x documentation several major issues no CPSW, incorrect ICSS section"
   "EXT_SITMPUSW-31","IPC Firmwares missing from base images."

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12111","Linux SDK v10.0: TI-added support for W25N01JW SPI NAND breaks other existing Flash support"
   "EXT_EP-12080","AM654x: USB MSC boot mode fails"
   "EXT_EP-12048","am654x-idk DFU boot is failing"


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
