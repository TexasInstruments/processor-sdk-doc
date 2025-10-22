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

Release 11.01.05.03
===================

Released on July 2025

What's included
---------------

**Key Release References:**

  - Snagfactory Support - :ref:`Snagfactory Tool <Flash-via-Fastboot>`
  - How to Enable PRU RPMsg - `Read FAQ <https://e2e.ti.com/support/processors-group/processors/f/791/t/1494495>`__

**Component version:**

  - Kernel 6.12.35
  - U-Boot 2025.01
  - Toolchain GCC 13.4
  - ATF 2.13+
  - OPTEE 4.6.0
  - TIFS Firmware / SYSFW `v11.01.02 <https://software-dl.ti.com/tisci/esd/11_01_02/release_notes/release_notes.html>`__ (Click on the link for more information)
  - IPC Firmware REL.MCUSDK.11.01.00.00
  - TAD5212 Firmware 1.0.0.0
  - DM Firmware 11.01.00.05
  - Yocto scarthgap 5.0

.. _release-specific-build-information:

Build Information
=================

.. _u-boot-release-notes:

U-Boot
------

| Head Commit: d2a72467939e169210bcd8e57de4b3e6ce2ef149 TI: dts: arm64: ti: sync dtbs from ti-linux-6.12.y upto e3e551586dfa
| uBoot Version: 2025.01
| uBoot Description: RC Release 11.01.05
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| uBoot Tag: 11.01.05
|

.. _tf-a-release-notes:

TF-A
----
| Head Commit: e0c4d3903b382bf34f552af53e6d955fae5283ab Merge changes from topic "xlnx_fix_gen_con_datatype" into integration
| Repo: https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/
| Branch: master
| Tag: (2.13 based)
|

.. _optee-release-notes:

OP-TEE
------
| Head Commit: 71785645fa6ce42db40dbf5a54e0eaedc4f61591 Update CHANGELOG for 4.6.0
| Repo: https://github.com/OP-TEE/optee_os/
| Branch: master
| Tag: 4.6.0
|

.. _ti-linux-fw-release-notes:

ti-linux-firmware
-----------------
| Head Commit: 33bec0e2ea9a25362c0c8243b2f1ed392dbc5b02 Merge branch 'main' of git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware into ti-linux-firmware-next
| Clone: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 11.01.05
|

Kernel
------

| Head Commit: e3e551586dfad357550da433969d6d9f458e06ce PENDING: arm64: dts: ti: k3-am62d2: Enable heartbeat led
| Kernel Version: v6.12.35
| Kernel Description: RC Release 11.01.05

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.01.05
| use-kernel-config=defconfig
| non-rt-config-fragment=kernel/configs/ti_arm64_prune.config
| rt-config-fragment=config-fragment=kernel/configs/ti_arm64_prune.config kernel/configs/ti_rt.config
|

Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: 59354be6c2362b9f7d0a3cd2c017f2f3c6ab7f2e CI/CD Auto-Merger: cicd.scarthgap.202507011953

| Clone: git://git.yoctoproject.org/meta-ti
| Branch: scarthgap
| Release Tag: 11.01.05
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: 0a9d75bc9eab472baa1eef57e1166954c557550a CI/CD Auto-Merger: cicd.scarthgap.202506261626

| Clone: git://git.yoctoproject.org/meta-arago
| Branch: scarthgap
| Release Tag: 11.01.05
|

.. rubric:: meta-tisdk
   :name: meta-tisdk

| Head Commit: 3265fc78d1dddd1642c112a2f3f42507bfa176d9 meta-ti-foundational: ti-apps-launcher: Update SRCREV

| Clone: https://github.com/TexasInstruments/meta-tisdk.git
| Branch: scarthgap
| Release Tag: 11.01.05.03
|
