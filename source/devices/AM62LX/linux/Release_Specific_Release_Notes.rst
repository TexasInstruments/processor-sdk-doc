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

Release 11.00.15.05
===================

Released on June 2025

What's new
----------

**Processor SDK Linux AM62LX Release has following new features:**

  - 2025 LTS Release Including RT combined branch model
  - New 2-Stage A53 Boot Flow
  - ATF Based Device Manager including SCMI
  - U-Boot: Legacy Boot Flow, Boot modes (UART, MMCSD, OSPI), GPMC NAND, CPSW, DMA
  - U-Boot: :ref:`User and Reduced Bootmode OTP Programming  <programming-user-otp-fuses-label>`
  - U-Boot: :ref:`Key writer lite Programming <key-writer-lite-label>`
  - Kernel: DMA, GPIO, I2C, UART, MMCSD, OSPI NOR, eCAP, eQEP, CPSW, McASP/Audio, DSS, DSI
  - Kernel: :ref:`DTHEv2 Crypto Accelerator <DTHEv2-Crypto-Accelerator>`
  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Support for Wifi with M2 CC33xx cards - :ref:`How to Enable M.2-CC33xx in Linux <enable_m2cc3301>`
  - Out-of-Box experience based on LVGL (Light and Versatile Graphics Library) - :ref:`TI LVGL Demo - User Guide <TI-LVGL-Demo-User-Guide-label>`
  - Jailhouse with Kernel 6.12
  - Debian distribution based on Armbian
  - Support for multiple Linux distributions, such as Yocto, Debian and Buildroot

**Component version:**

  - Kernel (Including RT) 6.12.24
  - U-Boot 2025.01
  - Toolchain GCC 13.3
  - ATF 2.12+
  - TIFS Firmware `v11.00.12 <https://software-dl.ti.com/tisci/esd/11_00_12/release_notes/release_notes.html>`__ (Click on the link for more information)
  - Yocto scarthgap 5.0
  - Armbian-based Debian 13 (Trixie)
  - Buildroot 2024.11.1

.. _release-specific-build-information:

Build Information
=================

.. _u-boot-release-notes:

U-Boot
------

| Head Commit: 1d6ba4a32cdd8c987533d5789b5bc7b84c41fabe TI: dts: arm64: ti: sync dtbs from ti-linux-6.12.y upto b0afb35642d7
| uBoot Version: 2025.01
| uBoot Description: RC Release 11.00.15
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| uBoot Tag: 11.00.15
|

.. _tf-a-release-notes:

TF-A
----
| Head Commit: a70f82d5a439cb9e21426908c7410c4f2a646364 PENDING: feat(ti): Add SiP SVC calls for fuse programming
| Repo: https://github.com/TexasInstruments/arm-trusted-firmware.git
| Branch: ti-master
| Tag: 11.00.15 (2.12+ Based)
|

.. _ti-linux-fw-release-notes:

ti-linux-firmware
-----------------
| Head Commit: 1ea29f4b3ec17bdc1a3431a014ea5224962dc779 Merge branch 'main' of git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware into ti-linux-firmware-next
| Clone: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 11.00.15
|

Kernel
------
.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: b0afb35642d79e776a4cf940945367cef87ba127 UPSTREAM: softirq: Use a dedicated thread for timer wakeups on PREEMPT_RT.
| Kernel Version: 6.12.24
| Kernel Description: RC Release 11.00.15

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.00.15
| use-kernel-config=defconfig
| config-fragment=kernel/configs/ti_arm64_prune.config
|


.. rubric:: Real Time (RT) Linux Kernel
   :name: real-time-rt-linux-kernel

| Head Commit: b0afb35642d79e776a4cf940945367cef87ba127 UPSTREAM: softirq: Use a dedicated thread for timer wakeups on PREEMPT_RT.
| Kernel Version: 6.12.24
| Kernel Description: RC Release 11.00.15

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.00.15
| use-kernel-config=defconfig
| config-fragment=config-fragment=kernel/configs/ti_arm64_prune.config kernel/configs/ti_rt.config
|


Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: 3de174b8c5807a5194b492a55d991ec628d937a8 CI/CD Auto-Merger: cicd.scarthgap.202505291514

| Clone: git://git.yoctoproject.org/meta-ti
| Branch: scarthgap
| Release Tag: 11.00.15
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: 822184f1a9a16b2424445793b2ce10267ed8bb5d CI/CD Auto-Merger: cicd.scarthgap.202505291514

| Clone: git://git.yoctoproject.org/meta-arago
| Branch: scarthgap
| Release Tag: 11.00.15
|

.. rubric:: meta-tisdk
   :name: meta-tisdk

| Head Commit: 7dd7103397637911b7ca709ce2981ff049b0d9a1 meta-ti-foundational: Update Jailhouse SRCREV for 11.00.15

| Clone: https://github.com/TexasInstruments/meta-tisdk.git
| Branch: scarthgap
| Release Tag: 11.00.15.05
| Tag Description: SITARA MPU Processor SDK 11.00 Release Tag for AM62L
|

Issues Tracker
==============

.. note::

    - Release Specific Issues including details will be published through Software Incident Report (SIR) portal

    - Further Information can be found at `SIR Portal <https://sir.ext.ti.com/>`_


Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-12673 <https://sir.ext.ti.com/jira/browse/EXT_EP-12673>`_","AM62L NETDEV WATCHDOG timeout when only one core enabled"
   "`EXT_EP-12674 <https://sir.ext.ti.com/jira/browse/EXT_EP-12674>`_","AM62L: Enabling wkup uart causes Linux console (main_uart0) garbled"
   "`EXT_EP-12667 <https://sir.ext.ti.com/jira/browse/EXT_EP-12667>`_","AM62L: nfsroot fails if the CPUs are limited to 1"
   "`EXT_EP-12668 <https://sir.ext.ti.com/jira/browse/EXT_EP-12668>`_","AM62L DMA: udma_stop not functional for cyclic packets"
   "`EXT_EP-12669 <https://sir.ext.ti.com/jira/browse/EXT_EP-12669>`_","AM62L DMA: Disabling CONFIG_TI_K3_UDMA causes build failures"
   "`EXT_EP-12670 <https://sir.ext.ti.com/jira/browse/EXT_EP-12670>`_","AM62L: bl31 setup: Failed to get response error messages"
   "`EXT_EP-12671 <https://sir.ext.ti.com/jira/browse/EXT_EP-12671>`_","AM62L: CPU hotplug is failing"
   "`EXT_EP-12672 <https://sir.ext.ti.com/jira/browse/EXT_EP-12672>`_","AM62L: LPM: RTC+DDR: suspend-resume fails with 2 cores enabled"
   "`EXT_EP-12676 <https://sir.ext.ti.com/jira/browse/EXT_EP-12676>`_","AM62L DMA: McASP is disabled when CONFIG_TI_K3_UDMA is disabled"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-12340 <https://sir.ext.ti.com/jira/browse/EXT_EP-12340>`_","Suspend-to-RAM failure: tps65219: device creates a circular dependency and device fails to enter suspend"

