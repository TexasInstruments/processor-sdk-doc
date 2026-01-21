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


Release 11.02.08.02
===================

Released on Dec 2025

What's new
----------

**Processor SDK Linux AM64X Release has following new features:**

- Third 2025 LTS Reference Release Including RT combined branch model
  - PRU Remoteproc boot
  - Added support for McASP async mode: independent transmit (playback) and receive (capture) clocking
  - Important Bug Fixes on top of Processor SDK 11.01.05.03 Release
  - Review Issue Tracker Section for the new fixes.

**Key Release References:**

  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Snagfactory Support - :ref:`Snagfactory Tool <Flash-via-Fastboot>`

**Component version:**

  - Kernel 6.12.57
  - U-Boot 2025.01
  - Toolchain GCC 13.4
  - ATF 2.13+
  - OPTEE 4.7.0
  - TIFS Firmware `v11.02.05 <https://software-dl.ti.com/tisci/esd/11_02_05/release_notes/release_notes.html>`__ (Click on the link for more information)
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
     - `11.02.08 <https://github.com/TexasInstruments/ti-u-boot/releases/tag/11.02.08>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/ecbe405df4033fa536886336f3796705eaef7eb4/config/sources/families/include/k3_common.inc#L72>`__
   * - ATF
     - `master <https://github.com/ARM-Software/arm-trusted-firmware/tree/master>`__
     - `v2.13+ <https://github.com/ARM-software/arm-trusted-firmware/commit/e0c4d3903b382bf34f552af53e6d955fae5283ab>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/ecbe405df4033fa536886336f3796705eaef7eb4/config/sources/families/include/k3_common.inc#L70>`__
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.7.0+ <https://github.com/OP-TEE/optee_os/commit/a9690ae39995af36a31b7a4f446f27ea0787e3a4>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/ecbe405df4033fa536886336f3796705eaef7eb4/config/sources/families/include/k3_common.inc#L98>`__
   * - Linux Firmware
     - `ti-linux-firmware <https://github.com/TexasInstruments/ti-linux-firmware/tree/ti-linux-firmware>`__
     - `11.02.08 <https://github.com/TexasInstruments/ti-linux-firmware/releases/tag/11.02.08>`__
     - `Git Clone <https://github.com/TexasInstruments/armbian-build/blob/ecbe405df4033fa536886336f3796705eaef7eb4/config/sources/families/include/k3_common.inc#L85>`__
   * - Linux Kernel
     - `ti-linux-6.12.y <https://github.com/TexasInstruments/ti-linux-kernel/tree/ti-linux-6.12.y>`__
     - `11.02.08 <https://github.com/TexasInstruments/ti-linux-kernel/releases/tag/11.02.08>`__
     - `non-RT <https://github.com/TexasInstruments/armbian-build/blob/2025.12-release/config/kernel/linux-k3-vendor.config>`__, `RT <https://github.com/TexasInstruments/armbian-build/blob/2025.12-release/config/kernel/linux-k3-vendor-rt.config>`__
   * - Armbian Build
     - `2025.12-release <https://github.com/TexasInstruments/armbian-build/tree/2025.12-release>`__
     - `11.02.08.02 <https://github.com/TexasInstruments/armbian-build/releases/tag/11.02.08.02>`__
     - | Build: `k3_common.inc <https://github.com/TexasInstruments/armbian-build/blob/2025.12-release/config/sources/families/include/k3_common.inc>`__ + `k3.conf <https://github.com/TexasInstruments/armbian-build/blob/2025.12-release/config/sources/families/k3.conf>`__
       | Board: `SK-AM64B <https://github.com/TexasInstruments/armbian-build/blob/2025.12-release/config/boards/sk-am64b.conf>`__

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

   "`EXT_EP-12122 <https://sir.ext.ti.com/jira/browse/EXT_EP-12122>`_","USB2 PHY locks up due to short suspend"
   "`EXT_EP-12123 <https://sir.ext.ti.com/jira/browse/EXT_EP-12123>`_","USART: Erroneous clear/trigger of timeout interrupt"
   "`EXT_EP-12114 <https://sir.ext.ti.com/jira/browse/EXT_EP-12114>`_","MMCSD: HS200 and SDR104 Command Timeout Window Too Small"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-13164 <https://sir.ext.ti.com/jira/browse/EXT_EP-13164>`_","CSI fails to stream due to DMA"
   "`EXT_EP-13127 <https://sir.ext.ti.com/jira/browse/EXT_EP-13127>`_","AM64x PRU Ethernet dual EMAC requires 256kB SRAM"
   "`EXT_EP-13129 <https://sir.ext.ti.com/jira/browse/EXT_EP-13129>`_","cpsw: probe failed if CONFIG_DEBUG_FS is disabled"
   "`EXT_EP-13166 <https://sir.ext.ti.com/jira/browse/EXT_EP-13166>`_","U-Boot: CONFIG_DEFAULT_DEVICE_TREE is not effective"
   "`EXT_EP-13132 <https://sir.ext.ti.com/jira/browse/EXT_EP-13132>`_","ptp4l gm_hsr0.cfg and oc_hsr0.cfg nonoffload example is deprecated"
   "`EXT_EP-13133 <https://sir.ext.ti.com/jira/browse/EXT_EP-13133>`_","PRP not working - AM64x"
   "`EXT_EP-12226 <https://sir.ext.ti.com/jira/browse/EXT_EP-12226>`_","Backport ""board: ti: common: Kconfig: add CMD_CACHE"" into TI U-Boot Tree"
   "`EXT_EP-13160 <https://sir.ext.ti.com/jira/browse/EXT_EP-13160>`_","Need PTPv1 support / fixes on AM62x family along with PTPv2"
   "`EXT_EP-13138 <https://sir.ext.ti.com/jira/browse/EXT_EP-13138>`_","Duplicate packets not removed when HSR firmwares reloaded"
   "`EXT_EP-13161 <https://sir.ext.ti.com/jira/browse/EXT_EP-13161>`_","HSR Offload 100Mbps cannot ping on SDK 10.1 or 11.0"
   "`EXT_EP-13147 <https://sir.ext.ti.com/jira/browse/EXT_EP-13147>`_","padconfig: ST_EN bit not preserved"
   "`EXT_EP-12785 <https://sir.ext.ti.com/jira/browse/EXT_EP-12785>`_","Cyclictest performance degradation on AM62x/AM64x/AM62A"
   "`EXT_EP-12751 <https://sir.ext.ti.com/jira/browse/EXT_EP-12751>`_","AM64x PRU Ethernet Benchmark testing low throughput"
   "`EXT_EP-12972 <https://sir.ext.ti.com/jira/browse/EXT_EP-12972>`_","RPMsg zerocopy example: CMA allocation is broken"
   "`EXT_EP-12750 <https://sir.ext.ti.com/jira/browse/EXT_EP-12750>`_","TMDS64EVM: PCIe refclk contention"
   "`EXT_EP-12815 <https://sir.ext.ti.com/jira/browse/EXT_EP-12815>`_","UDP Ingress failing"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-13131 <https://sir.ext.ti.com/jira/browse/EXT_EP-13131>`_","MMCSD: PHY DLL frequency is setting incorrectly for any clock < 200MHz"
   "`EXT_EP-12819 <https://sir.ext.ti.com/jira/browse/EXT_EP-12819>`_","AM64x CICD does not test PRU"
   "`EXT_EP-12818 <https://sir.ext.ti.com/jira/browse/EXT_EP-12818>`_","PRU RPMsg swaps which message is sent to which core"
   "`EXT_EP-12060 <https://sir.ext.ti.com/jira/browse/EXT_EP-12060>`_","AM64x: Lower core count on variant devices no supported"

