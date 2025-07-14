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


Release 11.01.05.03
===================

Released on July 2025

What's new
----------

**Processor SDK Linux AM64X Release has following new features:**

- Second 2025 LTS Reference Release Including RT combined branch model
  - Kernel: PRU HW UART
  - Important Bug Fixes on top of Processor SDK 11.00.09.04 Release
  - Review Issue Tracker Section for the new fixes.

**Key Release References:**

  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Snagfactory Support - :ref:`Snagfactory Tool <Flash-via-Fastboot>`

**Component version:**

  - Kernel 6.12.35
  - U-Boot 2025.01
  - Toolchain GCC 13.4
  - ATF 2.13+
  - OPTEE 4.6.0
  - TIFS Firmware `v11.01.02 <https://software-dl.ti.com/tisci/esd/11_01_02/release_notes/release_notes.html>`__ (Click on the link for more information)
  - Yocto scarthgap 5.0


Build Information
=================

.. _u-boot-release-notes:

U-Boot
------

.. rubric:: u-boot
   :name: u-boot

| Head Commit: d2a72467939e169210bcd8e57de4b3e6ce2ef149 TI: dts: arm64: ti: sync dtbs from ti-linux-6.12.y upto e3e551586dfa
| uBoot Version: 2025.01
| uBoot Description: RC Release 11.01.05
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| uBoot Tag: 11.01.05
|

.. _tf-a-release-notes:

TF-A
----
| Head Commit: e0c4d3903b382bf34f552af53e6d955fae5283ab Merge changes from topic "xlnx_fix_gen_con_datatype" into integration
| Repo: https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/
| Branch: master
| Tag: (2.13 based)
|

.. _optee-release-notes:

OP-TEE
------
| Head Commit: 71785645fa6ce42db40dbf5a54e0eaedc4f61591 Update CHANGELOG for 4.6.0
| Repo: https://github.com/OP-TEE/optee_os/
| Branch: master
| Tag: 4.6.0
|

.. _ti-linux-fw-release-notes:

ti-linux-firmware
-----------------
| Head Commit: 33bec0e2ea9a25362c0c8243b2f1ed392dbc5b02 Merge branch 'main' of git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware into ti-linux-firmware-next
| Clone: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 11.01.05
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
|

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

.. rubric:: meta-tisdk
   :name: meta-tisdk

| Head Commit: 3265fc78d1dddd1642c112a2f3f42507bfa176d9 meta-ti-foundational: ti-apps-launcher: Update SRCREV

| Clone: https://github.com/TexasInstruments/meta-tisdk.git
| Branch: scarthgap
| Release Tag: 11.01.05.03
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
   "EXT_EP-12337","ICSSG: TAPRIO - Firmware can’t handle base-time which is not a multiple of cycle-time."
   "EXT_EP-12338","ICSSG: PA_STATS are not sequenced properly"
   "EXT_EP-12339","Switch/MAC/HSR firmware does not drop corrupted packets"


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
   "EXT_EP-12336","Last 1B of payload missing in forwarding scenario"

