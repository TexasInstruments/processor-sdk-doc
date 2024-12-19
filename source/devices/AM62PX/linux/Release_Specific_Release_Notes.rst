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

To simplify the end user experience, Processor SDK Linux AM62Px installer provides everything needed as discussed below
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

-  Linux Manifest:  :file:`<PSDK_PATH>/docs/software_manifest.html`


Release 10.01.10.04
===================

Released on December 2024

What's new
----------

**Processor SDK Linux AM62PX Release has following new features:**

  - LTS Stable Kernel update to 6.6.58
  - Important Bug Fixes on top of Processor SDK 10.00.07.04 Release
  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Support for streaming from multiple 0V5640 cameras with `Arducam V3Link (Fusion Mini) <https://www.arducam.com/product/arducam-v3link-camera-kit-for-ti-development-boards/>`_
  - TISCI: A53 hosts default priv_id value updated to 1 from 4 (to match all other SOCs)
  - Power Management: :ref:`I/O Only Plus DDR <pm_io_only_plus_ddr>` mode
  - TI Apps Launcher: New Wi-Fi and Terminal Demo - :ref:`TI Apps Launcher <TI-Apps-Launcher-User-Guide-label>`
  - Snagfactory Support - :ref:`Snagfactory Tool <Flash-via-Fastboot>`


**Component version:**

  - Kernel 6.6.58
  - RT Kernel 6.6.58-rt45
  - U-Boot 2024.04
  - Toolchain GCC 13.3
  - ATF 2.11+
  - OPTEE 4.4.0
  - Graphics DDK 24.1
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


.. rubric:: meta-edgeai
   :name: meta-edgeai

| Head Commit: 4cba875d5173dee6b4ca34bd41d5a8b47891e0c7 ti-tidl: Update concerto SRC_REV
| Date: 2024-12-04 12:21:41 -0600

| Clone: https://git.ti.com/git/edgeai/meta-edgeai.git
| Branch: scarthgap
| Release Tag: 10.01.10.04
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
   "EXT_EP-12124","BCDMA: RX Channel can lockup in certain scenarios"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12109","Multi Instance Hang with Reduced CPU load patch"
   "EXT_EP-12108","audit for potential bugs with 6.6.44 stable merge "
   "EXT_EP-12107","Running camera pipelines causes kernel crash on all platforms"
   "EXT_EP-12061","Single Link LVDS is broken with 10.0"
   "EXT_EP-12106","higher latency metrics with Wave5"
   "EXT_EP-12058","rcu_preempt self-detected stall on CPU while running DSS usecases"
   "EXT_EP-12063","Update the DDR configuration with DDR syscfg 9.09+"
   "EXT_EP-12098","Uboot docs: document renaming tiboot3-<evm>.bin file"
   "SITSW-4773","DM is ignoring the exact flags sent in TISCI message"
   "SYSFW-5992","Unable to set exact pixel clock for OLDI LCD display / HDMI Pixel clock"
   "SYSFW-6426","Ownership of a firewall region can be transferred to an invalid host"
   "SYSFW-6432","Set device API doesn't return Error when PD is in transition state"
   "SYSFW-7571","Device IDs higher than 255 does not work with set device constraint API"
   "SYSFW-7602","RTC count value not getting updated after DeepSleep exit"
   "SYSFW-7614","Unable to configure DSS clock below 15.625MHz"
   "SYSFW-7617","LPM mode selection logic does not check for constraints on all the hosts/devices"
   "SYSFW-7739","LPM constraint messages received by TIFS not forwarded to DM"
   "SYSFW-7740","Only the last latency constraint value passed from a host considered in LPM selection"
   "SYSFW-7753","A53 privid is set to 4 and does not match other SOCs value of 1"
   "EXT_SITMPUSW-33", "Resolve GPU crash caused by Display cluster demo"
   "EXT_SITMPUSW-32", "SDK Makefile: Fix logic to pick key directory for mkimage"
   "EXT_SITMPUSW-31", "IPC Firmwares missing from base images."
   "EXT_SITMPUSW-30", "Debian: Deepsleep doesn't work on AM62P"
   "EXT_SITMPUSW-29", "TI Debian SDK: Docker not working"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12111","Linux SDK v10.0: TI-added support for W25N01JW SPI NAND breaks other existing Flash support"
   "EXT_EP-12112","Add Timer PWM documentation and other infrastructure as needed"
   "SYSFW-7622","DeepSleep resume failure when RTC wake is set for 1 second"
   "SYSFW-7781","Get device API does not return error when the LPSC is in transition state"
   "SYSFW-7831","DMA Resources used by ROM are not cleaned up when resuming from IO Only + DDR mode"
   "SYSFW-7884","There is an additional divide by 4 on all clocks of WKUP/MCU GPIO clock mux"
   "SYSFW-7887","DeepSleep fails if entered immediately after bootup"
   "SYSFW-7897","Partial I/O mode fails after few hundred iterations"
   "SYSFW-7899","LPM configuration is not enabled in HS-SE firmware"
   "SYSFW-7903","Processor ownership info is not part of minimal TIFS context in IO only + DDR mode"

