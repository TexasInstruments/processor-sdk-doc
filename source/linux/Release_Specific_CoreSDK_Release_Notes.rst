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


Release 11.01
=============

Released July 2025

.. rubric:: What's New
   :name: whats-new

**Processor SDK 11.01 Sitara Release supports the following platforms**
  * tag: 11.01.05
       * AM62Px (HS-FS)
       * AM62x ( GP, HS-FS, HS-SE)
       * AM62x LP (HS-FS, HS-SE)
       * AM62SIP (HS-FS, HS-SE)
       * AM64x 2.0 (HS-FS)
       * AM62A (HS-FS, HS-SE)
       * AM62D (HS-FS)

**Processor SDK 11.01 Sitara Release has following Major Updates**
  * Second 2025 LTS Release Including RT combined branch model
      * LTS Kernel Refresh from 6.12.17 to 6.12.35
      * ATF Upgrade from 2.12+ to 2.13+
      * OPTEE Upgrade from 4.5.0 to 4.6.0
  * Other Key Component Version updates
      * SYSFW: v11.01.02
      * DM: 11.01.00.05
  * Important Bug Fixes
      * Review Issue Tracker Section for the new fixes.

.. _release-specific-build-information:

Build Information
=================

U-Boot
------
| Head Commit: d2a72467939e169210bcd8e57de4b3e6ce2ef149 TI: dts: arm64: ti: sync dtbs from ti-linux-6.12.y upto e3e551586dfa
| uBoot Version: 2025.01
| uBoot Description: RC Release 11.01.05
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| uBoot Tag: 11.01.05
|


Kernel
------
.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: e3e551586dfad357550da433969d6d9f458e06ce PENDING: arm64: dts: ti: k3-am62d2: Enable heartbeat led
| Kernel Version: v6.12.35
| Kernel Description: RC Release 11.01.05

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.01.05
| use-kernel-config=defconfig
| non-rt-config-fragment=kernel/configs/ti_arm64_prune.config
| rt-config-fragment=config-fragment=kernel/configs/ti_arm64_prune.config kernel/configs/ti_rt.config


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

