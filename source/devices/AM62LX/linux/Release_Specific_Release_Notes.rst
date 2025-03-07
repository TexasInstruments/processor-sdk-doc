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

To simplify the end user experience, Processor SDK Linux AM62L installer provides everything needed as discussed below
to create the embedded system from “scratch” :

-  Platform/board-support software and configuration files for Linux
-  U-Boot and Kernel sources and configuration files
-  An ARM cross-compiling toolchain as well as other host binaries and components
-  A Yocto/OE compliant filesystem and sources for example applications
-  A variety of scripts and Makefiles to automate certain tasks
-  Other components needed to build an embedded system that don’t fit neatly into one of the above buckets
-  Reference Examples, benchmarks

This release supports High Security - Field Securable (HS-FS) devices.

Licensing
=========

Please refer to the software manifests, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page or in the installed directory as indicated below.

-  Linux Manifest:  :file:`<PSDK_PATH>/manifest/software_manifest.htm`

Release 11.00.05.02
===================

Released on March 2025

What's new
----------

**Processor SDK Linux AM62LX Release has following new features:**

  - First 2025 LTS Release Including RT combined branch model
  - New 2-Stage A53 Boot Flow
  - ATF Based Device Manager including SCMI
  - U-Boot: Legacy Boot Flow, Boot modes (UART, MMCSD, OSPI), CPSW, DMA
  - Kernel: DMA, GPIO, I2C, UART, MMCSD, OSPI NOR, eCAP, eQEP, CPSW, McASP/Audio, DSS, DSI
  - :ref:`Power Management <am62lx-power-management>`: DeepSleep and RTC+DDR low power modes.
  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Support for Wifi with M2 CC33xx cards - :ref:`How to Enable M.2-CC33xx in Linux <enable_m2cc3301>`
  - Out-of-Box experience based on LVGL (Light and Versatile Graphics Library) - :ref:`TI LVGL Demo - User Guide <TI-LVGL-Demo-User-Guide-label>`
  - Jailhouse with Kernel 6.12
  - Support for multiple Linux distributions, such as Yocto, Debian and Buildroot

**Component version:**

  - Kernel (Including RT) 6.12.13
  - U-Boot 2025.01
  - Toolchain GCC 13.3
  - ATF 2.12+
  - TIFS Firmware v11.00.05
  - Yocto scarthgap 5.0
  - Debian 13 (Trixie)
  - Buildroot 2024.11.1


Build Information
=================

.. _u-boot-release-notes:

U-Boot
------

| Head Commit: 9a3137c5c11a02fef9f2b66a7e9cb2af6a6a15ba PENDING: configs: am62lx_evm_defconfig: Switch to new DMA driver
| uBoot Version: 2025.01
| uBoot Description: RC Release 11.00.05
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| uBoot Tag: 11.00.05
|

.. _tf-a-release-notes:

TF-A
----
| Head Commit: dd46885ec58f9394b37f0c3d957e79838999b79d PENDING: fix(ti): am62l: fix am62l-bl1-dtb.sh for readelf parsing issue
| Repo: https://github.com/TexasInstruments/arm-trusted-firmware.git
| Branch: ti-master
| Tag: 11.00.05 (2.12+ Based)
|

.. _ti-linux-fw-release-notes:

ti-linux-firmware
-----------------
| Head Commit: 6bdfa48f6006e9b4a39befb613ad2a46d0f8746e ti-sysfw: am62lx: update to version v11.00.05
| Clone: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 11.00.05
|

Kernel
------
.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: 1a2d611ee02d63eda3ad6d636e1b0cbf5af87b95 PENDING: dmaengine: ti: k3-udma Fix warnings with W=1
| Kernel Version: 6.12.13
| Kernel Description: RC Release 11.00.05

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.00.05
| use-kernel-config=defconfig
| config-fragment=kernel/configs/ti_arm64_prune.config
|


.. rubric:: Real Time (RT) Linux Kernel
   :name: real-time-rt-linux-kernel

| Head Commit: 1a2d611ee02d63eda3ad6d636e1b0cbf5af87b95 PENDING: dmaengine: ti: k3-udma Fix warnings with W=1
| Kernel Version: 6.12.13
| Kernel Description: RC Release 11.00.05

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.00.05
| use-kernel-config=defconfig
| config-fragment=config-fragment=kernel/configs/ti_arm64_prune.config kernel/configs/ti_rt.config
|


Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: d1f9c4761e9f65f8a6f049f3ffdc85a8b0f0f63f CI/CD Auto-Merger: cicd.scarthgap.202502261418

| Clone: git://git.yoctoproject.org/meta-ti
| Branch: scarthgap
| Release Tag: 11.00.05
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: 3cdf522bfc998250793ddfd58cd503d822f6ee6a CI/CD Auto-Merger: cicd.scarthgap.202502261418

| Clone: git://git.yoctoproject.org/meta-arago
| Branch: scarthgap
| Release Tag: 11.00.05
|

.. rubric:: meta-tisdk
   :name: meta-tisdk

| Head Commit: e0fd39e02bf37233d51a7f7840a5e35900735179 jailhouse: Update SRCREV for 11.00.05 tag

| Clone: https://github.com/TexasInstruments/meta-tisdk.git
| Branch: scarthgap
| Release Tag: 11.00.05.02
| Tag Description: Processor SDK Tag for AM62L APL release
|

