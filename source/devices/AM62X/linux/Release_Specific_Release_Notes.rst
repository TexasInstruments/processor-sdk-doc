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

Release 11.02.08.02
===================

Released on Dec 2025

What's new
----------

**Processor SDK Linux AM62X Release has following new features:**

  - Third 2025 LTS Reference Release Including RT combined branch model
  - PRU Remoteproc boot
  - McSPI Turbo mode
  - Low Power Mode - Standby Via CPUIdle
  - Added support for McASP async mode: independent transmit (playback) and receive (capture) clocking
  - Important Bug Fixes on top of Processor SDK 11.01.05.03 Release
  - Review Issue Tracker Section for the new fixes.

**Key Release References:**

  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Falcon mode through R5 SPL :ref:`U-Boot Falcon Mode <U-Boot-Falcon-Mode>`
  - Out-of-Box TI Apps Launcher Application with Qt6 Framework - :ref:`TI Apps Launcher <TI-Apps-Launcher-User-Guide-label>`
  - Snagfactory Support - :ref:`Snagfactory Tool <Flash-via-Fastboot>`
  - Support for M2 CC33xx cards on Debian - `How to Enable M.2-CC33x1 in Linux <https://software-dl.ti.com/processor-sdk-linux/esd/AM62X/10_01_10_04_Debian/exports/docs/linux/How_to_Guides/Target/How_To_Enable_M2CC3301_in_linux.html>`__
  - How to Enable PRU RPMsg - `Read FAQ <https://e2e.ti.com/support/processors-group/processors/f/791/t/1494495>`__
  - How standby power mode works - :ref:`CPUIdle Documentation <cpuidle-guide>`

**Component version:**

  - Kernel 6.12.57
  - U-Boot 2025.01
  - Toolchain GCC 13.4
  - ATF 2.13+
  - OPTEE 4.7.0
  - Graphics DDK 25.2
  - TIFS Firmware `v11.02.05 <https://software-dl.ti.com/tisci/esd/11_02_05/release_notes/release_notes.html>`__ (Click on the link for more information)
  - DM Firmware 11.02.00.11
  - Yocto scarthgap 5.0

.. _release-specific-build-information:

Build Information
=================

Arago (Yocto/OE)
----------------

.. list-table::
   :header-rows: 1
   :widths: 15, 30, 30, 30

   * - Component
     - Branch Info
     - Tag Info
     - Config Info
   * - U-Boot
     - `ti-u-boot-2025.01 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/log/?h=ti-u-boot-2025.01>`__
     - `11.02.08 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tag/?h=11.02.08>`__
     - :ref:`Build Config <Build-U-Boot-label>`
   * - TF-A
     - `master <https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/+/refs/heads/master>`__
     - `v2.13+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-bsp/trusted-firmware-a/trusted-firmware-a-ti.inc?h=11.02.08#n3>`__
     -
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.7.0+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-security/optee/optee-os-ti-version.inc?h=11.02.08#n1>`__
     - |__OPTEE_PLATFORM_FLAVOR__|
   * - Linux Firmware
     - `ti-linux-firmware <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/log/?h=ti-linux-firmware>`__
     - `11.02.08 <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tag/?h=11.02.08>`__
     -
   * - Linux Kernel
     - `ti-linux-6.12.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.12.y>`__
     - `11.02.08 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=11.02.08>`__
     - `non-RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-6.12/k3/defconfig?h=11.02.08>`__ , `RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-rt-6.12/k3/defconfig?h=11.02.08>`__
   * - meta-ti
     - `scarthgap <https://git.yoctoproject.org/meta-ti/log/?h=scarthgap>`__
     - `11.02.08 <https://git.yoctoproject.org/meta-ti/tag/?h=11.02.08>`__
     - |__SDK_BUILD_MACHINE__|
   * - meta-arago
     - `scarthgap <https://git.yoctoproject.org/meta-arago/log/?h=scarthgap>`__
     - `11.02.08 <https://git.yoctoproject.org/meta-arago/tag/?h=11.02.08>`__
     -
   * - meta-tisdk
     - `scarthgap <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/log/?h=scarthgap>`__
     - `11.02.08.02 <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/tag/?h=11.02.08.02>`__
     -

Debian (Armbian)
----------------

.. list-table::
   :header-rows: 1
   :widths: 15, 30, 30, 30

   * - Component
     - Branch Info
     - Tag Info
     - Config Info
   * - U-Boot
     - `ti-u-boot-2025.01 <https://github.com/TexasInstruments/ti-u-boot/tree/ti-u-boot-2025.01>`__
     - `11.01.05 <https://github.com/TexasInstruments/ti-u-boot/releases/tag/11.01.05>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/5f357a146d6a72dad1b5677e4cfdc111a9f3a935/config/sources/families/k3.conf#L85>`__
   * - ATF
     - `master <https://github.com/ARM-Software/arm-trusted-firmware/tree/master>`__
     - `v2.13+ <https://github.com/ARM-software/arm-trusted-firmware/commit/d90bb650fe4cb3784f62214ab5829f4051c38d0a>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/5f357a146d6a72dad1b5677e4cfdc111a9f3a935/config/sources/families/k3.conf#L83>`__
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.6.0 <https://github.com/OP-TEE/optee_os/releases/tag/4.6.0>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/5f357a146d6a72dad1b5677e4cfdc111a9f3a935/config/sources/families/k3.conf#L111>`__
   * - Linux Firmware
     - `ti-linux-firmware <https://github.com/TexasInstruments/ti-linux-firmware/tree/ti-linux-firmware>`__
     - `11.01.05 <https://github.com/TexasInstruments/ti-linux-firmware/releases/tag/11.01.05>`__
     - `Git Clone <https://github.com/TexasInstruments/armbian-build/blob/5f357a146d6a72dad1b5677e4cfdc111a9f3a935/config/sources/families/k3.conf#L98>`__
   * - Linux Kernel
     - `ti-linux-6.12.y <https://github.com/TexasInstruments/ti-linux-kernel/tree/ti-linux-6.12.y>`__
     - `11.01.05 <https://github.com/TexasInstruments/ti-linux-kernel/releases/tag/11.01.05>`__
     - `non-RT <https://github.com/TexasInstruments/armbian-build/blob/2025.07-release/config/kernel/linux-k3-current.config>`__, `RT <https://github.com/TexasInstruments/armbian-build/blob/2025.07-release/config/kernel/linux-k3-current-rt.config>`__
   * - Armbian Build
     - `2025.07-release <https://github.com/TexasInstruments/armbian-build/tree/2025.07-release>`__
     - `11.01.05.03 <https://github.com/TexasInstruments/armbian-build/releases/tag/11.01.05.03>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/2025.07-release/config/sources/families/k3.conf>`__, `Board <https://github.com/TexasInstruments/armbian-build/blob/2025.07-release/config/boards/sk-am62b.conf>`__


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

   "`EXT_EP-12128 <https://sir.ext.ti.com/jira/browse/EXT_EP-12128>`_","USB2 PHY locks up due to short suspend"
   "`EXT_EP-12123 <https://sir.ext.ti.com/jira/browse/EXT_EP-12123>`_","USART: Erroneous clear/trigger of timeout interrupt"
   "`EXT_EP-12124 <https://sir.ext.ti.com/jira/browse/EXT_EP-12124>`_","BCDMA: RX Channel can lockup in certain scenarios"
   "`EXT_EP-12125 <https://sir.ext.ti.com/jira/browse/EXT_EP-12125>`_","i2327: RTC: Hardware wakeup event limitation"
   "`EXT_EP-12114 <https://sir.ext.ti.com/jira/browse/EXT_EP-12114>`_","MMCSD: HS200 and SDR104 Command Timeout Window Too Small"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_SITMPUSW-143 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-143>`_","Yocto Documentation: AM6x: SDK: Build Instruction missing steps for building K3R5 baremetal toolchain"
   "`EXT_EP-12816 <https://sir.ext.ti.com/jira/browse/EXT_EP-12816>`_","SDK Docs: Broken URL in How To Guides > EVM Setup"
   "`EXT_EP-12817 <https://sir.ext.ti.com/jira/browse/EXT_EP-12817>`_","PRUSS should be disabled for AM62 LP SK board"
   "`EXT_EP-12081 <https://sir.ext.ti.com/jira/browse/EXT_EP-12081>`_","AM62x: Make Debugging SPL doc specific to AM62x"
   "`EXT_SITMPUSW-146 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-146>`_","Yocto: meta-ti*: kernel source has uncommited changes"
   "`EXT_EP-12779 <https://sir.ext.ti.com/jira/browse/EXT_EP-12779>`_","Null dereference on fdinfo when not bound to a render task"
   "`EXT_EP-12296 <https://sir.ext.ti.com/jira/browse/EXT_EP-12296>`_","AM62x: 6.12 LTS Regression: PRU IPC Failure due to driver missing"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-12823 <https://sir.ext.ti.com/jira/browse/EXT_EP-12823>`_","CPSW ptp4l PDELAY_REQ and DELAY_REQ without timestamp messages"
   "`EXT_EP-12743 <https://sir.ext.ti.com/jira/browse/EXT_EP-12743>`_","Fixup A53 CPU Frequency by Speed Grade Problem"
   "`EXT_EP-12792 <https://sir.ext.ti.com/jira/browse/EXT_EP-12792>`_","CSI-2 Rx driver shall support frame width that is not 16-byte-aligned"
   "`EXT_EP-12818 <https://sir.ext.ti.com/jira/browse/EXT_EP-12818>`_","PRU RPMsg swaps which message is sent to which core"
   "`EXT_EP-12072 <https://sir.ext.ti.com/jira/browse/EXT_EP-12072>`_","misleading GPMC message in kernel log"
   "`EXT_EP-12785 <https://sir.ext.ti.com/jira/browse/EXT_EP-12785>`_","Cyclictest performance degradation on AM62x/AM64x/AM62A"
   "`EXT_EP-12815 <https://sir.ext.ti.com/jira/browse/EXT_EP-12815>`_","UDP Ingress failing"
   "`EXT_EP-12340 <https://sir.ext.ti.com/jira/browse/EXT_EP-12340>`_","Suspend-to-RAM failure: tps65219: device creates a circular dependency and device fails to enter suspend"
   "`EXT_EP-12345 <https://sir.ext.ti.com/jira/browse/EXT_EP-12345>`_","beagleplay: Segmentation-Fault: SD Boot failure and needs bootcmd update"

