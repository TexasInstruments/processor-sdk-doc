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

To simplify the end user experience, Processor SDK Linux AM62x installer provides everything needed as discussed below
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

Release 11.00.09.04
===================

Released on April 2025

What's new
----------

**Processor SDK Linux AM62X Release has following new features:**

- First 2025 LTS Reference Release Including RT combined branch model
  - Important Bug Fixes on top of Processor SDK 10.01.10.04 Release
  - Review Issue Tracker Section for the new fixes.

**Key Release References:**

  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Out-of-Box TI Apps Launcher Application with Qt6 Framework - :ref:`TI Apps Launcher <TI-Apps-Launcher-User-Guide-label>`
  - Snagfactory Support - :ref:`Snagfactory Tool <Flash-via-Fastboot>`
  - Support for M2 CC33xx cards on Debian - `How to Enable M.2-CC33x1 in Linux <https://software-dl.ti.com/processor-sdk-linux/esd/AM62X/10_01_10_04_Debian/exports/docs/linux/How_to_Guides/Target/How_To_Enable_M2CC3301_in_linux.html>`__
  - How to Enable PRU RPMsg - `Read FAQ <https://e2e.ti.com/support/processors-group/processors/f/791/t/1494495>`__
  - How standby power mode works - :ref:`CPUIdle Documentation <cpuidle-guide>`

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

| Head Commit: 2f497ac1090c5b256878d803b96901d73a285840 meta-ti-foundational: powervr-drivers: Add ti-img-rogue-driver bbappend

| Clone: https://github.com/TexasInstruments/meta-tisdk.git
| Branch: scarthgap
| Release Tag: 11.00.09.04
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
   "EXT_EP-12125","i2327: RTC: Hardware wakeup event limitation"

Errata Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12114","MMCSD: HS200 and SDR104 Command Timeout Window Too Small"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12063","Update the DDR configuration with DDR syscfg 10.03"
   "EXT_EP-12303","AM62x IPV6 UDP TX Checksum Offload Produces Illegal Checksum 0"
   "EXT_EP-12111","Linux SDK v10.0: TI-added support for W25N01JW SPI NAND breaks other existing Flash support"
   "EXT_EP-12313","OTP config structure is incorrectly defined in the secure board configurations"
   "EXT_EP-12312","AM62x: Add firewall changes to SPL on PG1.1 ROM update for compatibility with ES1.0"
   "EXT_EP-12112","Add Timer PWM documentation and other infrastructure as needed"
   "EXT_EP-12056","8250_omap: incorrect handling of dma->rx_running flag"
   "EXT_EP-12298","suspend-to-RAM wakeup by plugging in USB device is not reliable"
   "EXT_EP-12286","CICD-next: PIGLIT_S_BGRA_GLES_TEXTURE failure"
   "EXT_EP-12287","lmbench: runLmDDRBandwidth.sh: bw_mem: command not found"
   "EXT_EP-12289","Unable to boot kernel from eMMC"
   "EXT_EP-12342","ETHERNET boot test fails"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12299","AM62x large number of TCP packets with TX checksum errors"
   "EXT_EP-12076","copying files to eMMC triggers cqe error"
   "EXT_EP-12074","ti-rpmsg-char: Squash resource leaks"
   "EXT_EP-12072","misleading GPMC message in kernel log"
   "EXT_EP-12081","AM62x: Make Debugging SPL doc specific to AM62x"
   "EXT_EP-12345","beagleplay: Segmentation-Fault: SD Boot failure and needs bootcmd update"
   "EXT_EP-12296","AM62x: 6.12 LTS Regression: PRU IPC Failure due to driver missing"
   "EXT_EP-12341","Linux: AM62-LP-SK: SDK 11 Deep Sleep is non-functional"

