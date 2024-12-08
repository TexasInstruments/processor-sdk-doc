************************************
Release Notes
************************************

Overview
========

The **Processor-CoreSDK for Linux**
provides a fundamental software platform for development, deployment and
execution of Linux based applications and includes the following:

  * Bootloaders & Filesystems.
  * Prebuilt Binaries.
  * Detailed Release Notes.

Licensing
=========

Please refer to the software manifest, which outlines the licensing
status for all packages included in the prebuilt binaries location.


Release 10.01
=============

Released December 2024

.. rubric:: What's New
   :name: whats-new

**Processor SDK 10.01 Sitara Release supports the following platforms**
  * tag: 10.01.10
       * AM62Px (HS-FS)
       * AM62x ( GP, HS-FS, HS-SE)
       * AM62x LP (HS-FS, HS-SE)
       * AM62SIP ( HS-FS, HS-SE)
       * AM64x 2.0 (HS-FS)
       * AM62A (HS-FS, HS-SE)

**Processor SDK 10.01 Sitara Release has following Major Updates**
  * 2024 LTS Update with
      * Stable Kernel from 6.6.32 to 6.6.58
      * ATF from 2.10+ to 2.11+
      * OPTEE from 4.2.0 to 4.4.0
  * Other Key Component Version updates
      * SYSFW: v10.01.08
      * DM: 10.01.00.10
  * Important Bug and Stability fixes on top of 10.0 Release
      * Review Issue Tracker Section for the new fixes.


Build Information
=================

U-Boot
------
| Head Commit: 29d0c23d67ee7b88e46fe1753cd020e2b04c2ef6 arm: mach-k3: common: Print TIFS context save addr on resume
| uBoot Version: 2024.04
| uBoot Description: RC Release 10.01.10
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2024.04
| uBoot Tag: 10.01.10
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

