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

-  Linux Manifest:  :file:`<PSDK_PATH>/docs/software_manifest.html`


Release 10.01.10.04
===================

Released on December 2024

What's new
----------

**Processor SDK Linux AM64X Release has following new features:**

  - LTS Stable Kernel update to 6.6.58
  - Important Bug Fixes on top of Processor SDK 10.00.07.04 Release
  - RT Kernel : Real-Time Linux Interrupt Latency numbers here - :ref:`RT Interrupt Latencies <RT-linux-performance>`


**Component version:**

  - Kernel 6.6.58
  - RT Kernel 6.6.58-rt45
  - U-Boot 2024.04
  - Toolchain GCC 13.3
  - ATF 2.11+
  - OPTEE 4.4.0
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


Issues Tracker
==============

Errata Workarounds Available in this Release
--------------------------------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform"
   :widths: 15, 30, 55

   "LCPD-37352","CDNS: USB2 PHY locks up due to short suspend","am64xx-evm"
   "LCPD-32825","PCIe: ls -al /dev/disk/by-id shows no nvme device","am64xx-hsevm"
   "LCPD-27886","USART: Erroneous clear/trigger of timeout interrupt","am62axx_sk-fs,am62xx-sk,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,j7200-evm,j721e-idk-gw,j784s4-evm,j784s4-hsevm"
   "LCPD-25264","BCDMA: Blockcopy Gets Corrupted if TR Read Responses Interleave with Source Data Fetch","am64xx-evm,am64xx-hsevm,am64xx_sk-fs"
   "LCPD-19965","OSPI PHY Controller Bug Affecting Read Transactions","am64xx-evm,am654x-idk,j7200-evm,j721e-idk-gw"

|

.. _known-issues:

Known Issues
------------
.. csv-table::
   :header: "Record ID", "Title", "Platform", "Workaround"
   :widths: 5, 10, 50, 35

   "LCPD-38695","Documentation: Kernel_Drivers/Network & PRU-ICSS sections doesn't follow sphinx convention","am64xx-evm",""
   "LCPD-38689","Linux benchmarks: add context to Boot-time measurement","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am64xx-evm,am654x-evm",""
   "LCPD-38688","RT Linux benchmarks: add histogram for cyclic test","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am64xx-evm",""
   "LCPD-38656","AM64x: Verify IPC kernel: main-r5f0(s)/main-r5f1(s) fails to run","am62axx_sk-fs,am64xx-evm,am64xx-hsevm",""
   "LCPD-38619","Documentation: kernel:  Update How_to_Check_Device_Tree_Info section","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,beagleplay-gp",""
   "LCPD-38572","ICSSG interfaces in switch mode running linuxptp not functional","am64xx-evm,am64xx-hsevm",""
   "LCPD-38561","CPSW switch mode running linuxptp shows ""received SYNC without timestamp""","am64xx-evm",""
   "LCPD-38550","CPSW EST schedule triggers netdev watchdog","am64xx-evm",""
   "LCPD-38549","CPSW Ethernet EST schedule is not taken down on link down","am64xx-evm",""
   "LCPD-38547","PRU_ICSSG: DOC: Undefined labels","am64xx_sk-fs,am654x-idk",""
   "LCPD-38525","U-Boot packages Encryption key (custMpk.key) as replica of the Signing key (custMpk.pem)","am62pxx_sk-se,am62xx_lp_sk-se,am62xx_sk-se,am64xx-evm,am64xx-hsevm",""
   "LCPD-38371","ICSSG ethernet 1PPS not synchronized between 2 boards","am64xx-evm,am64xx-hsevm",""
   "LCPD-38326","ICSSG Ethernet: Update FDB Config Bucket Size to 512","am64xx-evm",""
   "LCPD-38254","Watchdog reset not functional: ESM pins are wrong","am62axx_sk-fs,am62pxx_sk-fs,am64xx-hsevm",""
   "LCPD-38252","Remove warning about graceful shutdown not supported","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,am64xx-evm",""
   "LCPD-38197","Bringing down icssg ethernet interface while running 1PPS distorts the 1PPS signal","am64xx-evm",""
   "LCPD-38181","sdk-doc: missing SK-AM64B information in CDNS3 USB page","am64xx_sk-fs,am64xx_sk-se",""
   "LCPD-38139","Watchdog fails to reset chip when counter reaches 0","am62axx_sk-fs,am62pxx_sk-fs,am64xx-evm,am64xx_sk-fs",""
   "LCPD-38133","IPC_S_FUNC_PRU_ECHO functional test failures","am335x-evm,am43xx-gpevm,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am64xx-hsevm,am654x-idk",""
   "LCPD-38040","mailbox tests marked as passing, but seem to actually fail","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am64xx-evm",""
   "LCPD-38039","Spinlock tests marked as passing, but seem to actually fail","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am64xx-evm",""
   "LCPD-38007","cdns: device mode: Linux hangs when USB cable is disconnected","am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se",""
   "LCPD-37998","rpmsg_zerocopy MCU+ projects have outdated CCS files","am62axx_sk-fs,am62xx_lp_sk-fs,am64xx_sk-fs",""
   "LCPD-37920","ti-rpmsg-char should use the same toolchain as current Yocto build","am335x-evm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-gpevm,am571x-idk,am572x-idk,am574x-idk,am57xx-evm,am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am64xx-evm,am64xx_sk-fs,am654x-idk",""
   "LCPD-37824","Need to update AM64x EVM and SK links in documentation","am64xx-hsevm",""
   "LCPD-37746","AM64x: u-boot UHS104 card speed check test fails","am64xx-evm,am64xx-hsevm",""
   "LCPD-37744","AM64x: RNG S Func tests fail","am64xx-evm,am64xx-hsevm,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se",""
   "LCPD-37730","PRU_ICSSG PPS Support Documentation and DTS discrepancy","am64xx-evm",""
   "LCPD-37463","We don't have SMMU kernel options related to VFIO should be NOIOMMU set","am64xx-hsevm,j721e-idk-gw",""
   "LCPD-37226","Update Ubuntu Host version in Linux documentation","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am62axx_sk-fs,am62axx_sk-se,am62lxx_evm-fs,am62lxx_evm-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am654x-evm,am654x-hsevm,am654x-idk,beagleplay-gp",""
   "LCPD-37197","AM64x: ICSSG: Firmware is not updating the Host Port statistics","am64xx-evm,am64xx-hsevm",""
   "LCPD-36993","U-Boot: lpddr4.c: Error handling missing failure cases","am62axx_sk-fs,am62axx_sk-se,am62lxx-vlab,am62lxx-zebu,am62lxx_evm-fs,am62lxx_evm-se,am62pxx-zebu,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am69_sk-fs,bbai,bbai64-gp,beaglebone,beagleplay-gp,j7200-evm,j7200-hsevm,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j784s4-evm,j784s4-hsevm,J784S4_BASESIM",""
   "LCPD-36985","AM64 Yocto SDK UG: Invalid eMMC Programming Steps in U-Boot Section","am64xx-hsevm",""
   "LCPD-36981","AM64x missing DMTimer support","am64xx-evm,am64xx-hsevm",""
   "LCPD-36864","ICSSG1 is not working in Debian but working in Yocto","am64xx-evm",""
   "LCPD-36804","IPC performance test fail - modprobe fails","am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se",""
   "LCPD-36431","ti-linux:am64x: eMMC: Fix iTAP values dumps issue.","am64xx-evm",""
   "LCPD-36430","ti-linux: MMC: Fix MMC Tunning Algorithm","am64xx_sk-fs",""
   "LCPD-36414","Performance numbers for NOR, eMMC missing in doc","am62xx_sk-fs,am64xx-evm",""
   "LCPD-35352","AM64x dts file calls SYNC2_OUT the wrong name","am64xx-evm,am64xx_sk-fs",""
   "LCPD-35050","SDK 8.6 u-boot GPMC-NAND boot broken on AM64x EVM + NAND card","am64xx-evm",""
   "LCPD-35022","AM64x: Benchmark OOB doesn't show any load on A53 and R5 (core 0) with latest ti-rpmsg-char v6.1","am64xx-hsevm",""
   "LCPD-34926","Some LTP tests are failing due to missing configurations","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,am64xx-hsevm,j7200-evm",""
   "LCPD-32953","AM64x: SDK broken for lower core count on variant devices","am64xx-hsevm,am64xx_sk-fs",""
   "LCPD-32931","OSPI: Update PHY tuning algorithm for PHY Tuning limitations","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_sk-fs,am68_sk-fs,am69_sk-fs,j7200-evm,j7200-hsevm,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j784s4-evm,j784s4-hsevm","Forced Half-Cycle DLL Lock Mode 100MHz - 166MHz only (100MHz is a Master Mode DLL limitation) Full tuning range of 0-127 should be the default for both RX and TX"
   "LCPD-32906","OSPI: Read data mismatch(first 32 bytes) when using DMA memcpy","am62axx_sk-fs,am62axx_sk-hs4,am62axx_sk-hs5,am62axx_sk-se,am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-hs4,am62xx_sk-hs5,am62xx_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_sk-fs,am64xx_sk-hs4,am64xx_sk-hs5,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am69_sk-fs,j7200-evm,j7200-hsevm,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j784s4-evm,j784s4-hsevm",""
   "LCPD-29861","AM64x: IPC tests fail","am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_sk-fs",""
   "LCPD-29805","AM64: Doc: Add boot mode switch settings","am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_sk-fs",""
   "LCPD-25558","AM64x: 'nand' tool doesn't seem to be working","am64xx-evm,am64xx-hsevm,am64xx_sk-fs",""
   "LCPD-25535","UBoot: customized ${optargs} doesn't take affect on K3 devices","am64xx-evm,am64xx-hsevm,am64xx_sk-fs,am654x-evm,am654x-hsevm,am654x-idk,j7200-evm,j7200-hsevm,j721e-evm,j721e-hsevm,j721e-idk-gw,j721s2-evm,j721s2-hsevm,j721s2_evm-fs",""
   "LCPD-25494","AM64 EVM TSN IET tests is failing","am64xx-evm",""
   "LCPD-24726","Uboot qspi read write performance test  failed ","am64xx_sk-fs",""
   "LCPD-24648","Move dma-heaps-test and ion-tests to TI repositories","am335x-evm,am572x-idk,am64xx-evm,dra71x-evm,j7200-evm,j721e-evm",""
   "LCPD-24638","AM654x ICSS-G: Support PPS Out function in the PHC driver Test Gap","am64xx_sk-fs,am654x-evm",""
   "LCPD-24595","j721e-idk-gw USB Suspend/Resume with RTC Wakeup fail (Impact 1)","am64xx-evm,am64xx_sk-fs,j7200-evm,j721e-idk-gw,j721e-sk",""
   "LCPD-24456","Move IPC validation source from github to git.ti.com","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-epos,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am62axx_sk-fs,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am64xx-evm,am64xx-hsevm,am64xx_sk-fs,am654x-evm,am654x-hsevm,am654x-idk,bbai,beaglebone,beaglebone-black,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm,j7200-evm,j7200-hsevm,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,omapl138-lcdk",""
   "LCPD-23066","am64x-sk :gpio: direction test fail","am64xx_sk-fs",""
   "LCPD-22912","am64xx-evm SMP dual core test fails sporadically","am64xx-evm",""
   "LCPD-22834","am64xx-evm stress boot test fails","am64xx-evm",""
   "LCPD-21577","USBHOST_S_FUNC_SERIAL_0001 test passes even when the serial device is not enumerated","am64xx-evm",""
   "LCPD-20105","AM64x: Kernel: ADC: RX DMA channel request fails","am64xx-evm,am64xx-hsevm",""
   "SYSFW-6432","Set device API doesn't return Error when PD is in transition state","am62x,am62ax,am62px,am64x,am65x",""
   "SYSFW-6426","Ownership of a firewall region can be transferred to an invalid host","am62x,am62ax,am62px,am64x,am65x",""
   "PINDSW-7087","ICSSG Fw:IET FPE mac verify fails","am64xx-evm,am654x-evm",""
   "PINDSW-8022","ICSSG Fw:TAPRIO - Base-time is not used properly","am64xx-evm,am654x-evm",""
   "PINDSW-8023","ICSSG Fw:TAPRIO - Firmware can’t handle base-time which is not a multiple of cycle-time.","am64xx-evm,am654x-evm",""
   "PINDSW-7087","ICSSG Fw:Switch: PTP: Timestamp Interrupt is coming on the opposite port","am64xx-evm,am654x-evm",""
   "SITSW-3922","Flash writer - Benchmark script fails for emmc logs","am62x,am62ax,am62px,am64x",""
   "SITSW-4864","TI Debian SDK: Docker not working","am62xx-sk,am62xx-sk-lp,am62x-sip-sk,am62p-sk,am64xx-evm,am64xx-sk",""

|

Closed Issues in Current Release
--------------------------------

.. csv-table::
   :header: "Record ID", "Title", "Platform"
   :widths: 15, 70, 25

   "LCPD-38691","Documentation: Remove external links of Kernel 5.10/ 6.1 &/or U-Boot 2023.04","am62pxx_sk-fs,am62xx-evm,am64xx-evm,am654x-evm"
   "LCPD-38353","fitImage boot fails on HS-FS Platforms","am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx_sk-fs,am64xx_sk-se,beagleplay-gp"
   "LCPD-38265","tiU_24.4: OSPI NOR Read taking more time","am62pxx_sk-fs,am62xx_sk-fs,am64xx_sk-fs"
   "LCPD-38253","AM64: ICSSG tests failing","am64xx-hsevm"
   "LCPD-38098","IPC failure in LTS 2024","am62axx_sk-fs,am62axx_sk-se,am62lxx-vlab,am62lxx-zebu,am62lxx_evm-fs,am62lxx_evm-se,am62pxx-zebu,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am68_sk-se,am69_sk-fs,j7200-evm,j7200-hsevm,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j784s4-evm,j784s4-hsevm"
   "LCPD-38038","6.6.30 : Build Regression on K3 platforms due to kselftest","am335x-evm,am437x-idk,am57xx-evm,am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am64xx-hsevm,am654x-idk,am68_sk-fs,am69_sk-fs"
   "LCPD-38001","Doc: Uboot build instructions need to document specific python dependencies for binman","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am64xx-hsevm,j7200-evm,j721e-idk-gw,j721s2-evm,j721s2_evm-fs,j722s_evm-fs,j784s4-evm"
   "LCPD-37917","AM64: Wifi broken on SK-AM64B","am64xx-evm,am64xx-hsevm"
   "LCPD-37898","watchdog documentation should explain how to set timeout","am335x-evm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-gpevm,am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,am64xx-evm,am64xx_sk-fs,am654x-evm,am654x-idk"
   "LCPD-37875","U-boot: otapdly and otap_del_sel do not get written to PHY CTRL 4 reg","am62pxx_sk-fs,am62pxx_sk-se,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se"
   "LCPD-37743","AM64x: K3conf SoC rev kernel crash test fails","am62axx_sk-fs,am62axx_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk"
   "LCPD-37714","CAN suspend and loopback tests are failing","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk"
   "LCPD-36358","am64x: eth2 link fails to come up for test_nway test","am64xx-evm"
   "LCPD-35299","UART RX data loss in i2310 workaround","am64xx-evm,am64xx_sk-fs"
   "LCPD-32478","Linux Benchmark/performance data is missing","am62xx-sk,am62xx_sk-fs,am62xx_sk-se,am64xx-hsevm,am64xx-hssk,am64xx_sk-fs"
   "LCPD-32250","Doc: Linux driver for eQEP","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-hssk,am64xx_sk-fs,am64xx_sk-se"
   "LCPD-25540","AM64: u-boot: usb host boot failed","am64xx-hsevm,am64xx_sk-fs"
   "LCPD-24872","Am64x-sk :LCPD-16811 CPSW  failed while throughput metrics comparison ","am64xx_sk-fs"
   "LCPD-38690","Documentation: Remove reference of denx.de/wiki","am62pxx_sk-fs,am62pxx_sk-se,am62xx-evm,am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm"
   "LCPD-38237","ICSSG Ethernet: IEP1 needs to be enabled","am64xx-hsevm, am654x-evm"
   "LCPD-38236","ICSSG Ethernet: FDB access configuration for Mac mode is incorrect","am64xx-evm"
   "LCPD-38112","AM64x/AM65x: ICSSG Ethernet: Enable IEP1 Counter","am64xx-evm,am654x-evm"
   "LCPD-37892","U-boot build error for booting via Ethernet on AM62x","am64xx-evm,am64xx-hsevm"
   "SYSFW-7463","TISCI_MSG_GET_CLOCK always return Enabled for input clock","am62x,am62ax,am62px,am64x,am65x"
   "SYSFW-7485","Update the PLL driver in TIFS boot flow to follow correct sequence","am62x,am62ax,am62px,am64x,am65x"
   "SYSFW-7486","PM: Cleanup additional steps in pll init startup routine","am62x,am62ax,am62px,am64x,am65x"
   "PINDSW-7851","ICSSG Fw: Sporadic forwarding stall in Cut-through mode","am64xx-evm,am654x-evm"
   "PINDSW-7980","ICSSG Fw: FDB: Learning and Flushing Issues","am64xx-evm,am654x-evm"
   "PINDSW-7981","ICSSG Fw: FDB: All Slots are not cleared during initialization","am64xx-evm,am654x-evm"
   "PINDSW-7982","ICSSG Fw: Race condition during IEP configuration","am64xx-evm,am654x-evm"
   "PINDSW-7990","ICSSG Fw: HalfDuplex: Need to handle CRS, COL connections combination in firmware","am64xx-evm"
   "SITSW-4481","Debian SDK documentation misses instructions for building kernel package","am62x-sk,am62p-sk,am64xx-evm,am64xx-sk,am62xx-sk-lp,am62x-sip-sk"
   "SITSW-5040","TI Debian SDK: Build instructions no longer working due to ti-bdebstrap Advancement","am62xx-sk,am62xx-sk-lp,am62x-sip-sk,am62p-sk,am64xx-evm,am64xx-sk"


|
