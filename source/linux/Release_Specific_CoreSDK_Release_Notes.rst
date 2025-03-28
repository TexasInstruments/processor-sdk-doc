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


Release 11.00
=============

Released March 2025

.. rubric:: What's New
   :name: whats-new

**Processor SDK 11.00 Sitara Release supports the following platforms**
  * tag: 11.00.09
       * AM62Px (HS-FS)
       * AM62x ( GP, HS-FS, HS-SE)
       * AM62x LP (HS-FS, HS-SE)
       * AM64x 2.0 (HS-FS)
       * AM62A (HS-FS, HS-SE)

**Processor SDK 11.00 Sitara Release has following Major Updates**
  * First 2025 LTS Release Including RT combined branch model
      * LTS Kernel Refresh from 6.6.58 to 6.12.17
      * Uboot Upgrade from v2024.04 to v2025.01
      * ATF Upgrade from 2.11+ to 2.12+
      * OPTEE Upgrade from 4.4.0 to 4.5.0
      * Graphics DDK from 24.1 to 24.2
  * Other Key Component Version updates
      * SYSFW: v11.00.07
      * DM: 11.00.00.06
  * Important Bug Fixes
      * Review Issue Tracker Section for the new fixes.


Build Information
=================

U-Boot
------
| Head Commit: cd91d73601810374d16a1f17505ab2e72e31f75d PENDING: mmc: am654_sdhci: Unset HIGH_SPEED_ENA for MMC_HS_52
| uBoot Version: 2025.01
| uBoot Description: RC Release 11.00.09
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| uBoot Tag: 11.00.09
|


Kernel
------
.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: c85877d40f8e70e1e201eca2ae1648781f238a37 PENDING: can: m_can: Support pinctrl wakeup state for Partial I/O
| Kernel Version: v6.12.17
| Kernel Description: RC Release 11.00.09

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.00.09
| use-kernel-config=defconfig
| non-rt-config-fragment=kernel/configs/ti_arm64_prune.config
| rt-config-fragment=config-fragment=kernel/configs/ti_arm64_prune.config kernel/configs/ti_rt.config


Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: 5385fb9231e8d48c30ddd965c4cc623a1f004e3e CI/CD Auto-Merger: cicd.scarthgap.202503251551

| Clone: git://git.yoctoproject.org/meta-ti
| Branch: scarthgap
| Release Tag: 11.00.09
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: 4ec7ae427f9a6aeb7d0b98ac7251bfc2436dbae2 CI/CD Auto-Merger: cicd.scarthgap.202503251551

| Clone: git://git.yoctoproject.org/meta-arago
| Branch: scarthgap
| Release Tag: 11.00.09
|

