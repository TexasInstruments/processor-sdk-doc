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

Release versioning scheme
=========================

Processor SDK releases follow the 5-duplet versioning scheme ``YY.RR.EE.CC.SS``, where:

- ``YY`` - Yearly baseline. Increments with each new LTS baseline.
- ``RR`` - Release index within the yearly baseline. Each yearly baseline includes many stable releases.
- ``EE`` - Extended release index within a stable baseline.
- ``CC`` - Release Candidate for common foundational BSP components such as Linux, U-Boot, ATF, OPTEE, Firmware and OE manifest including meta-ti, meta-arago.
- ``SS`` - SDK Release identifier for Distro layers (Yocto meta-tisdk, Armbian, Buildroot) with OOB Demos and Installers.

Licensing
=========

Please refer to the software manifests, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page or in the installed directory as indicated below.

-  Linux Manifest:  :file:`<PSDK_PATH>/manifest/software_manifest.htm`
-  Debian Manifest: `AM64x 12.00.00.07.04
   <https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-yXgchBCk98/12.00.00.07.04/software_manifest_debian_sk-am64b_sk-am64b.htm>`__


Release 12.00.00.07.04
======================

Released on Apr 2026

What's new
----------

**Processor SDK Linux AM64X Release has following new features:**

  - First 2026 LTS Reference Release Including RT combined branch model
  - Important Bug Fixes on top of Processor SDK 11.02.08.02 Release
  - Review Issue Tracker Section for the new fixes.
  - Security: ATF and OPTEE memory firewall for isolation from Linux

**Key Release References:**

  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Snagfactory Support - :ref:`Snagfactory Tool <Flash-via-Fastboot>`

**Component version:**

  - Kernel 6.18.13
  - U-Boot 2026.01
  - Toolchain GCC 15.2
  - ATF 2.14+
  - OPTEE 4.9.0+
  - TIFS Firmware `v12.00.02 <https://software-dl.ti.com/tisci/esd/12_00_02/release_notes/release_notes.html>`__ (Click on the link for more information)
  - Yocto Master

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
     - `ti-u-boot-2026.01 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/log/?h=ti-u-boot-2026.01>`__
     - `12.00.00.07 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tag/?h=12.00.00.07>`__
     - :ref:`Build Config <Build-U-Boot-label>`
   * - TF-A
     - `master <https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/+/refs/heads/master>`__
     - `v2.14+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-bsp/trusted-firmware-a/trusted-firmware-a-ti.inc?h=12.00.00.07#n5>`__
     -
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.9.0+ <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-security/optee/optee-os-ti-version.inc?h=12.00.00.07#n1>`__
     - |__OPTEE_PLATFORM_FLAVOR__|
   * - Linux Firmware
     - `ti-linux-firmware <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/log/?h=ti-linux-firmware>`__
     - `12.00.00.07 <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tag/?h=12.00.00.07>`__
     -
   * - Linux Kernel
     - `ti-linux-6.18.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.18.y>`__
     - `12.00.00.07 <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tag/?h=12.00.00.07>`__
     - `non-RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-6.18/k3/defconfig?h=12.00.00.07>`__ , `RT <https://git.yoctoproject.org/meta-ti/tree/meta-ti-bsp/recipes-kernel/linux/linux-ti-staging-rt-6.18/k3/defconfig?h=12.00.00.07>`__
   * - meta-ti
     - `master <https://git.yoctoproject.org/meta-ti/log/?h=master>`__
     - `12.00.00.07 <https://git.yoctoproject.org/meta-ti/tag/?h=12.00.00.07>`__
     - |__SDK_BUILD_MACHINE__|
   * - meta-arago
     - `master <https://git.yoctoproject.org/meta-arago/log/?h=master>`__
     - `12.00.00.07 <https://git.yoctoproject.org/meta-arago/tag/?h=12.00.00.07>`__
     -
   * - meta-tisdk
     - `master <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/log/?h=scarthgap>`__
     - `12.00.00.07.04 <https://git.ti.com/cgit/ti-sdk-linux/meta-tisdk/tag/?h=12.00.00.07.04>`__
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
     - `ti-u-boot-2026.01 <https://github.com/TexasInstruments/ti-u-boot/tree/ti-u-boot-2026.01>`__
     - `12.00.00.07 <https://github.com/TexasInstruments/ti-u-boot/releases/tag/12.00.00.07>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/9f81d13cc640f9ad876faf2a906a0eda11a6bffd/config/sources/families/include/k3_common.inc#L76>`__
   * - TF-A
     - `master <https://github.com/ARM-Software/arm-trusted-firmware/tree/master>`__
     - `v2.14+ <https://github.com/ARM-software/arm-trusted-firmware/commit/76500ceaeefcda967d8a1f4e30bb04f9fe0425a2>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/9f81d13cc640f9ad876faf2a906a0eda11a6bffd/config/sources/families/include/k3_common.inc#L74>`__
   * - OPTEE
     - `master <https://github.com/OP-TEE/optee_os/tree/master>`__
     - `4.9.0+ <https://github.com/OP-TEE/optee_os/commit/f2a7ad0638aeff5243593b33cc56ad064cae7615>`__
     - `Build <https://github.com/TexasInstruments/armbian-build/blob/9f81d13cc640f9ad876faf2a906a0eda11a6bffd/config/sources/families/include/k3_common.inc#L102>`__
   * - Linux Firmware
     - `ti-linux-firmware <https://github.com/TexasInstruments/ti-linux-firmware/tree/ti-linux-firmware>`__
     - `12.00.00.07 <https://github.com/TexasInstruments/ti-linux-firmware/releases/tag/12.00.00.07>`__
     - `Git Clone <https://github.com/TexasInstruments/armbian-build/blob/9f81d13cc640f9ad876faf2a906a0eda11a6bffd/config/sources/families/include/k3_common.inc#L89>`__
   * - Linux Kernel
     - `ti-linux-6.18.y <https://github.com/TexasInstruments/ti-linux-kernel/tree/ti-linux-6.18.y>`__
     - `12.00.00.07 <https://github.com/TexasInstruments/ti-linux-kernel/releases/tag/12.00.00.07>`__
     - `non-RT <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/kernel/linux-k3-vendor.config>`__, `RT <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/kernel/linux-k3-vendor-rt.config>`__
   * - Armbian Build
     - `2026.04-release <https://github.com/TexasInstruments/armbian-build/tree/2026.04-release>`__
     - `12.00.00.07.04 <https://github.com/TexasInstruments/armbian-build/releases/tag/12.00.00.07.04>`__
     - | Build: `k3_common.inc <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/sources/families/include/k3_common.inc>`__ + `k3.conf <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/sources/families/k3.conf>`__
       | Board: `SK-AM64B <https://github.com/TexasInstruments/armbian-build/blob/2026.04-release/config/boards/sk-am64b.conf>`__

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

   "`EXT_EP-13313 <https://sir.ext.ti.com/jira/browse/EXT_EP-13313>`_","PRUETH: 100M Link fails if auto negotiation disabled"
   "`EXT_EP-13131 <https://sir.ext.ti.com/jira/browse/EXT_EP-13131>`_","MMCSD: PHY DLL frequency is setting incorrectly for any clock < 200MHz"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_EP-13331 <https://sir.ext.ti.com/jira/browse/EXT_EP-13331>`_","am64x: incorrect device id in icssg0_mdio devicetree node"
   "`EXT_EP-12051 <https://sir.ext.ti.com/jira/browse/EXT_EP-12051>`_","AM64x: DFU Boot hangs on repetitive test"
   "`EXT_EP-13306 <https://sir.ext.ti.com/jira/browse/EXT_EP-13306>`_","ICSSG: HSR packet out of order"
   "`EXT_EP-13309 <https://sir.ext.ti.com/jira/browse/EXT_EP-13309>`_","U-Boot binman does not have the provision of SWREV for Board Configurations"
   "`EXT_EP-13310 <https://sir.ext.ti.com/jira/browse/EXT_EP-13310>`_","Docs: Incorrect secure boot flow description"
   "`EXT_EP-12819 <https://sir.ext.ti.com/jira/browse/EXT_EP-12819>`_","AM64x CICD does not test PRU"
   "`EXT_EP-12818 <https://sir.ext.ti.com/jira/browse/EXT_EP-12818>`_","PRU RPMsg swaps which message is sent to which core"
   "`EXT_EP-12749 <https://sir.ext.ti.com/jira/browse/EXT_EP-12749>`_","cdns: device mode: Linux hangs when USB cable is disconnected"
   "`EXT_EP-12060 <https://sir.ext.ti.com/jira/browse/EXT_EP-12060>`_","AM64x: Lower core count on variant devices no supported"

