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

-  Linux Manifest:  :file:`<PSDK_PATH>/manifest/software_manifest.htm`


Release 11.00.09.04
===================

Released on April 2025

What's new
----------

**Processor SDK Linux AM64X Release has following new features:**

- First 2025 LTS Reference Release Including RT combined branch model
  - Important Bug Fixes on top of Processor SDK 10.01.10.04 Release
  - Review Issue Tracker Section for the new fixes.

- This release adds support for PRP Offload to the ICSSG prueth-driver. This allows to offload PRP functionality
  to the ICSSG hardware, which helps in reducing load on the A53 cores.

**Key Release References:**

  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Snagfactory Support - :ref:`Snagfactory Tool <Flash-via-Fastboot>`

**Component version:**

  - Kernel 6.12.17
  - U-Boot 2025.01
  - Toolchain GCC 13.3
  - ATF 2.12+
  - OPTEE 4.5.0
  - TIFS Firmware `v11.00.07 <https://software-dl.ti.com/tisci/esd/11_00_07/release_notes/release_notes.html>`__ (Click on the link for more information)
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

| Head Commit: c1f4a8eaf9b0779e9dfa66d2e4de0ac4173772c4 meta-ti-foundational: seva: Make service file work with emptty

| Clone: https://github.com/TexasInstruments/meta-tisdk.git
| Branch: scarthgap
| Release Tag: 11.00.09.04
|


Issues Tracker
==============

.. note::

    - Release Specific Issues including details will be published through Software Incident Report (SIR) portal

    - Further Information can be found at `SIR Portal <https://sir.ext.ti.com/>`

Errata Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12122","USB2 PHY locks up due to short suspend"
   "EXT_EP-12123","USART: Erroneous clear/trigger of timeout interrupt"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12315","eMMC High Speed SDR mode is not configured correctly in the U-Boot"
   "EXT_EP-12311","AM64x: Software Build Sheet needs update at SOC level SW readiness"
   "EXT_EP-12111","Linux SDK v10.0: TI-added support for W25N01JW SPI NAND breaks other existing Flash support"
   "EXT_EP-12051","AM64x: Linux hangs on repetitive probe/removal of gadget zero"
   "EXT_EP-12071","sdk-doc: missing SK-AM64B information in CDNS3 USB page"
   "EXT_EP-12336","Last 1B of payload missing in forwarding scenario"
   "EXT_EP-12337","ICSSG: TAPRIO - Firmware can’t handle base-time which is not a multiple of cycle-time."
   "EXT_EP-12338","ICSSG: PA_STATS are not sequenced properly"
   "EXT_EP-12339","Switch/MAC/HSR firmware does not drop corrupted packets"
   "EXT_EP-12715","Local injection (TX) - Transmission failure due ""TX Pkt not available"""
   "EXT_EP-12716","PRU - Task Manager disable during firmware init"
   "EXT_EP-12717","Packets reception failure: 10Mbps speed"
   "EXT_EP-12718","Non-recoverable TX underflow with Bidirectional traffic in 100M MII mode"
   "EXT_EP-12719","Throughput drop: Software buffer pool implementation @1G speed"


Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12310","Resource Table generating wrong format for rm-cfg.yaml"
   "EXT_EP-12285","SK-AM64B: Deferred probe of i2c bus warning"
   "EXT_EP-12300","ICSSG: Ethernet: Promiscuous mode is always enabled in bridge mode"
   "EXT_EP-12075","U-boot gets stuck when DDR size changed to 512 MB"
   "EXT_EP-12060","AM64x: Lower core count on variant devices no supported"

