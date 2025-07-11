.. _Release-note-label:

************************************
Release Notes
************************************

Overview
========

The **Processor Software Development Kit (Processor SDK)** is a unified software platform for TI embedded processors
providing easy setup and fast out-of-the-box access to benchmarks and demos.  All releases of Processor SDK are
consistent across TI’s broad portfolio, allowing developers to seamlessly reuse and develop software across devices.
Developing a scalable platform solutions has never been easier than with the Processor SDK and TI’s embedded processor
solutions.

To simplify the end user experience, Processor SDK Linux AM62A installer provides everything needed as discussed below
to create the embedded system from “scratch” :

-  Platform/board-support software and configuration files for Linux
-  U-Boot and Kernel sources and configuration files
-  An ARM cross-compiling toolchain as well as other host binaries and components
-  A Yocto/OE compliant filesystem and sources for example applications
-  A variety of scripts and Makefiles to automate certain tasks
-  Other components needed to build an embedded system that don’t fit neatly into one of the above buckets
-  Reference Examples, benchmarks


Licensing
=========

Please refer to the software manifests, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page or in the installed directory as indicated below.

-  Linux Manifest:  "/docs/software_manifest.html"


Release 11.00.09.04
===================

Released on April 2025

What's new
----------

**Processor SDK Linux AM62AX Release has following new features:**

  - First 2025 LTS Reference Release Including RT combined branch model
  - Falcon mode through R5 SPL :ref:`U-Boot Falcon Mode <U-Boot-Falcon-Mode>`
  - Important Bug Fixes on top of Processor SDK 10.01.10.04 Release
  - Review Issue Tracker Section for the new fixes.

**Key Release References:**

  - RT Kernel : Real-Time Linux Interrupt Latency numbers here :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Support for streaming from OV2312 camera with `DS90UB954-Q1EVM <https://www.ti.com/tool/DS90UB954-Q1EVM>`_
  - Power Management: :ref:`I/O Only Plus DDR <pm_io_only_plus_ddr>` mode

**Component version:**

  - Kernel 6.12.17
  - U-Boot 2025.01
  - Toolchain GCC 13.3
  - ATF 2.12+
  - OPTEE 4.5.0
  - Graphics DDK 24.2
  - TIFS Firmware / SYSFW `v11.00.07 <https://software-dl.ti.com/tisci/esd/11_00_07/release_notes/release_notes.html>`__ (Click on the link for more information)
  - DM Firmware 11.00.00.06
  - Yocto scarthgap 5.0


Build Information
=================

.. _u-boot-release-notes:

U-Boot
------

.. rubric:: u-boot
   :name: u-boot

.. ifconfig:: CONFIG_image_type in ('edgeai','adas')

    .. note::

       meta-edgeai Yocto layer contains additional patches for U-Boot `here <https://git.ti.com/cgit/edgeai/meta-edgeai/tree/recipes-bsp/u-boot?h=10.01.00.05>`__.

| Head Commit: cd91d73601810374d16a1f17505ab2e72e31f75d PENDING: mmc: am654_sdhci: Unset HIGH_SPEED_ENA for MMC_HS_52
| uBoot Version: 2025.01
| uBoot Description: RC Release 11.00.09
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| uBoot Tag: 11.00.09
|

.. _tf-a-release-notes:

TF-A
----
| Head Commit: b11beb2b6bd30b75c4bfb0e9925c0e72f16ca53f PENDING: feat(ti): Update DDR Configurations
| Repo: https://github.com/TexasInstruments/arm-trusted-firmware.git
| Branch: ti-master
| Tag: (2.12 based): 11.00.09
|

.. _optee-release-notes:

OP-TEE
------
| Head Commit: ef1ebdc23034a804a72da2207f1a825ce96a1464 plat-k3: Add initial support for AM62Lx SoC
| Repo: https://github.com/OP-TEE/optee_os/
| Branch: master
| Tag: 4.5.0+
|

.. _ti-linux-fw-release-notes:

ti-linux-firmware
-----------------
| Head Commit: 27003b6bff61a55dd1fff2cc777e5e07b092b1f7 ti-eth: j721e/j784s4/j7200: update firmware to version 11.00.02
| Clone: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 11.00.09
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

.. ifconfig:: CONFIG_image_type in ('edgeai','adas')

   .. note::

      meta-edgeai Yocto layer contains additional patches for Kernel `here <https://git.ti.com/cgit/edgeai/meta-edgeai/tree/recipes-kernel/linux?h=10.01.00.05>`__.

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

.. rubric:: meta-tisdk
   :name: meta-tisdk

| Head Commit: e5820fc658978e74bf9270e911e966c417105650 meta-ti-foundational: emptty: Move disabling weston logic to emptty recipe

| Clone: https://github.com/TexasInstruments/meta-tisdk.git
| Branch: scarthgap
| Release Tag: 11.00.09.04
|

.. rubric:: meta-edgeai
   :name: meta-edgeai

| Head Commit: bccfd706c87e0017360e75bdf9803679fe24db13 [20241210] EDGEAI Auto Update
| Date: 2024-12-10 10:21:16 -0600

| Clone: https://git.ti.com/git/edgeai/meta-edgeai.git
| Branch: scarthgap
| Release Tag: 10.01.00.05
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

   "EXT_EP-12128","USB2 PHY locks up due to short suspend"
   "EXT_EP-12123","USART: Erroneous clear/trigger of timeout interrupt"
   "EXT_EP-12124","BCDMA: RX Channel can lockup in certain scenarios"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12108","audit for potential bugs with 6.6.44 stable merge "
   "EXT_EP-12098","Uboot docs: document renaming tiboot3-<evm>.bin file"
   "EXT_EP-12103","PHY configs not restored after suspend-resume"
   "EXT_EP-12058","rcu_preempt self-detected stall on CPU while running DSS usecases"
   "EXT_EP-12093","GPIO glitch observed while resuming from DeepSleep"
   "EXT_EP-12059","AM62A: Missing UB954-Q1 support"
   "EXT_EP-12063","Update the DDR configuration with DDR syscfg 9.09+"
   "EXT_EP-12064","AM62A Yocto SDK UG: OSPI U-Boot Section Incomplete (PHY Calibration, Programming, etc.)"
   "EXT_EP-12101","AM62A dts files missing RTI nodes"
   "EXT_EP-12109","Multi Instance Hang with Reduced CPU load patch"
   "EXT_EP-12107","Running camera pipelines causes kernel crash on all platforms"
   "EXT_EP-12106","higher latency metrics with Wave5"
   "EXT_EP-12105","Multistream decode stall during stop sequence"
   "SITSW-4773","DM is ignoring the exact flags sent in TISCI message"
   "SYSFW-5992","Unable to set exact pixel clock for OLDI LCD display / HDMI Pixel clock"
   "SYSFW-6426","Ownership of a firewall region can be transferred to an invalid host"
   "SYSFW-6432","Set device API doesn't return Error when PD is in transition state"
   "SYSFW-7096","TIFS halts when proc auth boot message is sent for an AES-256 encrypted image"
   "SYSFW-7571","Device IDs higher than 255 does not work with set device constraint API"
   "SYSFW-7602","RTC count value not getting updated after DeepSleep exit"
   "SYSFW-7614","Unable to configure DSS clock below 15.625MHz"
   "SYSFW-7617","LPM mode selection logic does not check for constraints on all the hosts/devices"
   "SYSFW-7739","LPM constraint messages received by TIFS not forwarded to DM"
   "SYSFW-7740","Only the last latency constraint value passed from a host considered in LPM selection"
   "SYSFW-7758","MAIN PLL15 HSDIVs (DM) if updated in SBL flow results in boot failure in later stages"


Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12111","Linux SDK v10.0: TI-added support for W25N01JW SPI NAND breaks other existing Flash support"
   "EXT_EP-12078","SK-AM62A: Stability issues with DDR Config v0.10.02"
   "EXT_EP-12077","Failure to enter DeepSleep with JPEG Encoder"
   "EXT_EP-12073","AM62Ax MCU domain pinmux disabled by default"
   "EXT_EP-12112","Add Timer PWM documentation and other infrastructure as needed"
   "EXT_EP-12127","Streaming with multiple cameras gets frozen in 2 minutes"
   "EXT_EP-12142","Instabilities observed while resuming from IO Only plus DDR mode"
   "SYSFW-7034","Read lock on extended OTP area does not work after doing write lock"
   "SYSFW-7622","DeepSleep resume failure when RTC wake is set for 1 second"
   "SYSFW-7781","Get device API does not return error when the LPSC is in transition state"
   "SYSFW-7811","Resume from IO Only + DDR mode fails sometimes"
   "SYSFW-7831","DMA Resources used by ROM are not cleaned up when resuming from IO Only + DDR mode"
   "SYSFW-7884","There is an additional divide by 4 on all clocks of WKUP/MCU GPIO clock mux"
   "SYSFW-7887","DeepSleep fails if entered immediately after bootup"
   "SYSFW-7897","Partial I/O mode fails after few hundred iterations"
   "SYSFW-7903","Processor ownership info is not part of minimal TIFS context in IO only + DDR mode"

