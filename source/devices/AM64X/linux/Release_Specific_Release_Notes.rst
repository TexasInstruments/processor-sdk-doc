.. _Release-note-label:

#############
Release Notes
#############

Overview
========

The **Processor Software Development Kit (Processor SDK)** is a unified software platform for TI embedded processors
providing easy setup and fast out-of-the-box access to benchmarks and demos.  All releases of Processor SDK are
consistent across TI’s broad portfolio, allowing developers to seamlessly reuse and develop software across devices.
Developing a scalable platform solutions has never been easier than with the Processor SDK and TI’s embedded processor
solutions.

To simplify the end user experience, Processor SDK Linux AM64x installer provides everything needed as discussed below
to create the embedded system from “scratch” :

-  Platform/board-support software and configuration files for Linux
-  U-Boot and Kernel sources and configuration files
-  An ARM cross-compiling toolchain as well as other host binaries and components
-  A Yocto/OE compliant filesystem and sources for example applications
-  A variety of scripts and Makefiles to automate certain tasks
-  Other components needed to build an embedded system that don’t fit neatly into one of the above buckets
-  Reference Examples, benchmarks

This release supports SR2.0 High Security - Field Securable (HS-FS) devices. For migration guide and other info, refer :ref:`HS-Migration-Guide`

Licensing
=========

Please refer to the software manifests, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page or in the installed directory as indicated below.

-  Linux Manifest:  :file:`<PSDK_PATH>/docs/software_manifest.html`


Release 10.01.10.04
===================

Released on December 2024

What's new
----------

**Processor SDK Linux AM64X Release has following new features:**

  - LTS Stable Kernel update to 6.6.58
  - Important Bug Fixes on top of Processor SDK 10.00.07.04 Release
  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`


**Component version:**

  - Kernel 6.6.58
  - RT Kernel 6.6.58-rt45
  - U-Boot 2024.04
  - Toolchain GCC 13.3
  - ATF 2.11+
  - OPTEE 4.4.0
  - TIFS Firmware v10.01.08
  - DM Firmware 10.01.00.10
  - Yocto scarthgap 5.0


Build Information
=================

.. _u-boot-release-notes:

U-Boot
------

.. rubric:: u-boot
   :name: u-boot

| Head Commit: 29d0c23d67ee7b88e46fe1753cd020e2b04c2ef6 arm: mach-k3: common: Print TIFS context save addr on resume
| uBoot Version: 2024.04
| uBoot Description: RC Release 10.01.10
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2024.04
| uBoot Tag: 10.01.10
|

.. _tf-a-release-notes:

TF-A
----
| Head Commit: 58b25570c9ef91753b14c2103f45f4be9dddb696 Merge "feat(ti): implement DM_MANAGED suspend" into integration
| Repo: https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git
| Branch: master
| Tag: 2.11+
|

.. _optee-release-notes:

OP-TEE
------
| Head Commit: 8f645256efc0dc66bd5c118778b0b50c44469ae1 Update CHANGELOG for 4.4.0
| Repo: https://github.com/OP-TEE/optee_os/
| Branch: master
| Tag: 4.4.0
|

.. _ti-linux-fw-release-notes:

ti-linux-firmware
-----------------
| Head Commit: 1eaf07dc4ec5cdeb98078f17a9d4635e88f43f75 ti-dm: Update display sharing firmware for am62px
| Clone: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 10.01.10
|

Kernel
------
.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: a7758da17c2807e5285d6546b6797aae1d34a7d6 driver core: fw_devlink: Stop trying to optimize cycle detection logic
| Kernel Version: 6.6.58
| Kernel Description: RC Release 10.01.10

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.6.y
| Tag: 10.01.10
| use-kernel-config=defconfig
| config-fragment=kernel/configs/ti_arm64_prune.config
|


.. rubric:: Real Time (RT) Linux Kernel
   :name: real-time-rt-linux-kernel

| Head Commit: c79d7ef3a56ff61dd83d5527520b419a4f0e32e2 Merge branch 'ti-linux-6.6.y-cicd' of https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel into ti-rt-linux-6.6.y-cicd
| Kernel Version: 6.6.58-rt45
| Kernel Description: RC Release 10.01.10-rt

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-rt-linux-6.6.y
| Tag: 10.01.10-rt
| use-kernel-config=defconfig
| config-fragment=config-fragment=kernel/configs/ti_arm64_prune.config kernel/configs/ti_rt.config
|


Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: 50acaea23568f72121020a97bf13869770929cb7 CI/CD Auto-Merger: cicd.scarthgap.202412030400

| Clone: git://git.yoctoproject.org/meta-ti
| Branch: scarthgap
| Release Tag: 10.01.10
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: 2b1f8572ac54cd64ca5d5b40e344bb32b00a05f5 CI/CD Auto-Merger: cicd.scarthgap.202412030400

| Clone: git://git.yoctoproject.org/meta-arago
| Branch: scarthgap
| Release Tag: 10.01.10
|

.. rubric:: meta-tisdk
   :name: meta-tisdk

| Head Commit: fcd7661087b0dd5b5b57d30ba0d45f2698e962f8 Jailhouse: Update SRCREV for 10.01.10 tag

| Clone: https://github.com/TexasInstruments/meta-tisdk.git
| Branch: scarthgap
| Release Tag: 10.01.10.04
|


Issues Tracker
==============

.. note::

    - Release Specific Issues including details will be published through Software Incident Report (SIR) portal

    - Further Information can be found at `SIR Portal <https://sir.ext.ti.com/>`

