.. _release-specific-release-notes:

************************************
Release Notes
************************************

Overview
========

The **Processor Software Development Kit (Processor-SDK) for Linux**
provides a fundamental software platform for development, deployment and
execution of Linux based applications and includes the following:

-  Bootloaders, Linux Kernel & Filesystem
-  SDK installer
-  Setup scripts
-  Documentation

.. Note::
    For building some of the RTOS-based demonstrations, you should also download
    Processor SDK RTOS installer. For more information,
    refer to <PSDKRA install path>/index.html.


Licensing
=========

Please refer to the software manifest, which outlines the licensing
status for all packages included in this release. The manifest can be found on the SDK
download page or in the installed directory as indicated below. In
addition, see :ref:`Processor SDK Linux GPLv3 Disclaimer <overview-gplv3-disclaimer>`.


Documentation
===============
-  :ref:`Processor SDK Linux Software Developer's Guide <linux-index>`: Provides information on features, functions, delivery package and,
   compile tools for the Processor SDK Linux release. This also provides
   detailed information regarding software elements and software
   infrastructure to allow developers to start creating applications.
-  :ref:`Processor SDK Linux Getting Started Guide <overview-getting-started>`: Provides information on getting the software and running
   examples/demonstrations bundled in the SDK.
-  **Software Manifest**: Provides license information on software
   included in the SDK release. This document is in the release at
   ``[INSTALL-DIR]/docs``.
-  **EVM Quick Start Guide**: Provides information on hardware setup and
   running the demonstration application that is loaded on flash. This
   document is provided as part of the EVM kit.


Supported Platforms
=====================================
See :ref:`here <release-specific-supported-platforms-and-versions>` for a list of supported platforms and links to more information.

Release 07.03.00
================
Released April 2021

What's New
----------
- Final release on 2020 LTS 5.4 kernel
- J7200 Kernel and Uboot Support for SDR104 speed mode
- J7200 Kernel eMMC HS200 and HS400 speed modes

Release features
----------------

-  A72 U-boot:

   -  Support for booting both compressed and uncompressed kernel image
   -  Basic HYP mode support - boots up uboot in EL2 privileged mode
   -  OSPI support, MMCSD support
   -  SD card boot support
   -  USB Host and mass storage support
   -  Support for DFU download to SD card, eMMC, OSPI
   -  UFS support
   -  eMMC boot support
-  Kernel: Kernel image includes support for the following drivers

   -  MMC support
   -  I2C support
   -  CPSW2G Ethernet driver
   -  UART driver, UART console support
   -  USB driver with support for device/host mode of operation
   -  PCIe Root Complex  and Endpoint drivers
   -  USB gadget driver support

      -  Composite device
      -  Multifunction composite device
   -  USB DRD dual role support
   -  Support for dual voltage SD cards (UHS mode)
   -  PCIe Gen3 2xlane support
   -  eMMC HS400 speed mode support
   -  UART DMA mode support
   -  UFS support
   -  ADC basic functionality
   -  Crypto acceleration support for AES, 3-DES, and RNG
-  Profiling

   -  A72 PMU support for Performance profiling

.. _release-specific-build-information:

Component versions
------------------

.. csv-table::
   :header: "component", "source", "branch", "version"
   :widths: 20,40,20,30

   arm-trusted-firmware,git://git.ti.com/atf/arm-trusted-firmware.git,ti-atf,65dd16b4ea5032752af62e94ca64cff41733a123
   optee-os,git://git.ti.com/optee/ti-optee-os.git,ti-optee-os,36905c9566936f7502e3741b48015c1f147b3bd3
   U-boot,git://git.ti.com/ti-u-boot/ti-u-boot.git,ti-u-boot-2020.01,2781231a33c3d779e32445f4fe55164c45d6d7c1
   Linux Kernel,git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git,ti-linux-5.4.y,023faefa70274929bff92dc41167b007f7523792


Issues Tracker
===============
..
   project = LCPD AND issuetype = Bug AND status = Closed AND resolution = Done AND component in ("Audio & Display", Baseport, Connectivity, IPC, "Power & Thermal", Graphics, Multimedia, Wireless, "System Integration", Security) AND closedDate > 2020-11-18 AND createdDate <= 2020-11-17 AND (Labels not in (LCPD_K3.14_MAINT, MAINTENANCE, PLSDK_NOT_RN) OR labels is EMPTY) AND OS in (Linux, RT-linux) AND Platform in (j7200-evm) ORDER BY key DESC, priority DESC

Issues opened in previous releases that were closed on this release
---------------------------------------------------------------------
.. csv-table::
   :header: "Record ID", "Summary"
   :widths: 20, 80

   LCPD-19772,ATF/Uboot GTC frequency handover bug
   LCPD-19733,[ti:ti-rt-linux-5.4.y 3364/11241] drivers/pci/endpoint/functions/pci-epf-ntb.c:860 epf_ntb_init_epc_bar_interface() warn: unsigned 'barno' is never less than zero.
   LCPD-19731,HSR/PRP : warning: ignoring return value of ‘skb_put_padto'

..
   project = LCPD AND issuetype = Bug AND status = Closed AND resolution = Done AND component in ("Audio & Display", Baseport, Connectivity, IPC, "Power & Thermal", "System Integration", Wireless, Graphics, Multimedia, Security) AND closedDate > 2020-11-18 AND createdDate > 2020-11-18 AND (Labels not in (LCPD_K3.14_MAINT, MAINTENANCE, PLSDK_NOT_RN) OR labels is EMPTY) AND OS in (Linux, RT-linux) AND fixversion not in (Upstream) AND Platform in (j7200-evm) ORDER BY key DESC, priority DESC

Issues found and closed on this release that may be applicable to prior releases
--------------------------------------------------------------------------------
.. csv-table::
   :header: "Record ID", "Summary"
   :widths: 20, 80

   LCPD-20634,J7200: SDK Builds fail to complete
   LCPD-20618,k3: cpswxg: bindings not updated
   LCPD-20524,doc: i2027 errata incorrectly documented as applicable for J721E/J7200.
   LCPD-20299,"Obsolete ti,sci-rm-range-girq usage in Wkup GPIO Interrupt Routers"
   LCPD-20177,J7200 UART boot not working
   LCPD-20122,Add external power supply to PCIe USB card on am64xx and j7200
   LCPD-20058,Kernel: Fix UBIFS errors on Cypress S28 flash
   LCPD-19969,Kernel: Random DMA timeouts on OSPI
   LCPD-19946,remoteproc/k3-r5f: Fix couple of warnings
   LCPD-19936,OSPI UBIFS test fails on j7200
   LCPD-19884,Images missing for j7200 custom build: 07.01.00-005_usbdev-hs
   LCPD-19862,USB SuperSpeed enumeration not working on j7200e

..
   project = LCPD AND Platform in (j7200-evm) AND ErrataID is not EMPTY AND status = Closed AND (Labels not in (PLSDK_NOT_RN) OR labels is EMPTY) ORDER BY priority DESC

Errata workarounds
------------------
.. csv-table::
   :header: "Record ID", "Summary", "Workaround", "ErrataID"
   :widths: 20, 80, 60, 20

   LCPD-19965,OSPI PHY Controller Bug Affecting Read Transactions,,i2189


..
   project = LCPD AND issuetype = Bug AND (status not in (Closed, "In Build") OR status = Closed AND resolution in ("Known Issue : HW Limitation", "Known Issue : Other")) AND component in ("System Integration", Graphics, Wireless, Security, Multimedia) AND (labels not in (LCPD_K3.14_MAINT, MAINTENANCE, DO_NOT_RELEASE_NOTE, PLSDK_NOT_RN, SKIP_REL_NOTES) OR labels is EMPTY) AND ((affectedVersion <= 07.03.00 AND affectedVersion >upstream ) OR affectedVersion is EMPTY OR affectedVersion not in (Upstream, upstream)) AND Platform in (j7200-evm) AND OS = "Linux" ORDER BY key DESC, priority DESC, component ASC

.. _release-specific-known-issues:

SDK Known Issues
----------------
.. csv-table::
   :header: "Record ID", "Summary", "Workaround"
   :widths: 20, 80, 60

   LCPD-19858,OE: OPTEE label used in SDK is old and wrong,
   LCPD-19743,Packages.gz is missing,

..
   project = LCPD AND issuetype = Bug AND (status not in (Closed, "In Build") OR status = Closed AND resolution in ("Known Issue : HW Limitation", "Known Issue : Other")) AND component in ("Power & Thermal", Baseport, "Audio & Display", Connectivity, IPC) AND (labels not in (LCPD_K3.14_MAINT, upstream, MAINTENANCE, DO_NOT_RELEASE_NOTE, PLSDK_NOT_RN, SKIP_REL_NOTES) OR labels is EMPTY) AND (summary ~ u-boot OR Subcomponent in (u-boot, UBOOT, Uboot)) AND (affectedVersion <= 07.03.00 AND affectedVersion > upstream OR affectedVersion is EMPTY OR affectedVersion not in (Upstream, upstream)) AND Platform in (j7200-evm) ORDER BY key DESC, priority DESC, component ASC

U-Boot Known Issues
-------------------
.. csv-table::
   :header: "Record ID", "Summary", "Workaround"
   :widths: 20, 80, 60

   LCPD-20131,Uboot fails to enumerate devices attached to a usb hub on the first 'usb reset' call ,Re-run usb reset command
   LCPD-19871,U-boot: Documentation: Combined Boot flow and SPL Rearch,
   LCPD-17523,R5-SPL - Support to dump EEPROM to shared memory,

..
   project = LCPD AND issuetype = Bug AND (status not in (Closed, "In Build") OR status = Closed AND resolution in ("Known Issue : HW Limitation", "Known Issue : Other")) AND component in ("Audio & Display", Baseport, Connectivity, IPC, "Power & Thermal") AND (affectedVersion <= 07.03.00 AND affectedVersion > upstream OR affectedVersion is EMPTY OR affectedVersion not in (Upstream, upstream)) AND (labels not in (LCPD_K3.14_MAINT, upstream, MAINTENANCE, DO_NOT_RELEASE_NOTE, PLSDK_NOT_RN, SKIP_REL_NOTES) OR labels is EMPTY) AND summary !~ u-boot AND (Subcomponent not in (u-boot, UBOOT, Uboot) OR Subcomponent is EMPTY) AND Platform in (j7200-evm) ORDER BY key DESC, priority DESC, component DESC

Linux Kernel Known Issues
---------------------------
.. csv-table::
   :header: "Record ID", "Summary", "Workaround"
   :widths: 20, 80, 60

   LCPD-21508,USB stick attached to a PCIe USB card on j7200 not enumerated after reboot,
   LCPD-21507,am64xx and j7200 PCIe USB card must use an external power supply to enumerate the attached USB stick,
   LCPD-21350,j7200 PCIE-EP tests failing,
   LCPD-20320,CPSW5g high packet loss,
   LCPD-20309,TCP/UDP performance tests sometimes fail due to no netperf output,
   LCPD-20106,USBDEVICE ping from DUT to host fails when packet_count=470,
   LCPD-19942,"UART tests at certain speeds fail on j7200, j721e",
   LCPD-19723,RTI watchdog test fails on J7VCL E5 SOM,
   LCPD-19659,Doc: PCIe: Update documentation to indicate how to move to compliance mode,
   LCPD-19499,Kernel: OSPI write throughput is less than 1MB/s,
   LCPD-19497,J7200: CPSW2g: interface goes up and down sporadically,Seen only on very few EVMs. No workaround.
   LCPD-19460,J7200: USB3 devices fail to enumerate at 2.0/3.0 when SERDES multi-link (PCIe + USB3),No workaround for USB 3.0 devices exists. USB 2.0 devices enumerate fine.
   LCPD-17798,2020 LTS: INTA/INTR smp_affinity failure and IRQ allocation issues.,

|


Installation and Usage
======================

The :ref:`Software Developer's Guide <linux-index>` provides instructions on how to setup your Linux development environment, install the SDK and start your development. It also includes User's Guides for various Example Applications.


|

Host Support
============

For the specific supported hosts for current SDK, see :ref:`this page <how-to-build-a-ubuntu-linux-host-under-vmware>`.


.. note::
   Processor SDK Installer is 64-bit, and installs only on 64-bit host machine.

.. |reg| unicode:: U+00AE .. REGISTERED SIGN
