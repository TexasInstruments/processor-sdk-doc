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


Release 10.01.00
================

Released on December 2024

What's new
----------

**Processor SDK Linux AM62A Release has following new features:**

  - LTS Stable Kernel update to 6.6.58
  - Important Bug Fixes on top of Processor SDK 10.00.07.04 Release
  - RT Kernel : Real-Time Linux Interrupt Latency numbers here :ref:`RT Interrupt Latencies <RT-linux-performance>`

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

.. ifconfig:: CONFIG_image_type in ('edgeai','adas')

    .. note::

       meta-edgeai Yocto layer contains additional patches for U-Boot `here <https://git.ti.com/cgit/edgeai/meta-edgeai/tree/recipes-bsp/u-boot?h=10.01.00.03>`__.


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

.. ifconfig:: CONFIG_image_type in ('edgeai','adas')

   .. note::

      meta-edgeai Yocto layer contains additional patches for Kernel `here <https://git.ti.com/cgit/edgeai/meta-edgeai/tree/recipes-kernel/linux?h=10.01.00.03>`__.


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

| Head Commit: 836b1a3aa89d087474495ab4f77fc7a06ffcef0f edgeai-test-data.bb: edgeai-tidl-models.bb: Updated EDGEAI_SDK_VERSION
| Date: 2024-07-30 05:58:20 -0500

| Clone: https://git.ti.com/git/edgeai/meta-edgeai.git
| Branch: scarthgap
| Release Tag: 10.00.00.04
|


.. ifconfig:: CONFIG_image_type in ('edgeai', 'adas')

   .. rubric:: meta-edgeai

   | Head Commit: c9351accf9c3ec152ffde84507c674901b7f23f1 [20240814] EDGEAI Auto Update
   | Date: 2024-08-14

   | Clone: git://git.ti.com/edgeai/meta-edgeai.git
   | Branch: scarthgap
   | Release Tag: 10.01.00.03
   |

Issues Tracker
==============

Errata Workarounds Available in this Release
--------------------------------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform"
   :widths: 15, 30, 55

   "LCPD-37965","BCDMA: RX Channel can lockup in certain scenarios","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se"
   "LCPD-37081","SNPS: USB2 PHY locks up due to short suspend","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xxsip_sk-fs"
   "LCPD-27886","USART: Erroneous clear/trigger of timeout interrupt","am62axx_sk-fs,am62xx-sk,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,j7200-evm,j721e-idk-gw,j784s4-evm,j784s4-hsevm"

|

.. _known-issues:

Known Issues
------------
.. csv-table::
   :header: "Record ID", "Title", "Platform", "Workaround"
   :widths: 15, 40, 20, 25

   "LCPD-38689","Linux benchmarks: add context to Boot-time measurement","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am64xx-evm,am654x-evm",""
   "LCPD-38688","RT Linux benchmarks: add histogram for cyclic test","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am64xx-evm",""
   "LCPD-38687","LPM: TI SCI: debug prints during suspend print wrong CPU device for max latency set","am62axx_sk-fs,am62axx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-38669","PHY configs not restored afer suspend-resume","am62xx_lp_sk-fs,am62axx_sk-fs","Checkout to tag: 10.00.08 (https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/commit/?h=ti-linux-6.6.y-cicd&id=db88712931433e92a5f73cec57c82c5c7ebee593) or Apply the following 3 commits: 'c3c859de6142 spi: cadence-quadspi: Define cqspi_phy_set_dll_master', 'e64d4d321e85 spi: cadence-quadspi: Store phy_setting in flash private data', '6b5642d52397 spi: cadence-quadspi: Move restore_context to runtime_resume'"
   "LCPD-38667","AM62ax: Verify IPC U-Boot: c71_0","am62axx_sk-fs",""
   "LCPD-38666","AM62ax: Verify IPC SPL: mcu-r5f0 in split mode","am62axx_sk-fs",""
   "LCPD-38662","rcu_preempt self-detected stall on CPU","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,j721e-idk-gw,j721s2-evm",""
   "LCPD-38656","AM64x: Verify IPC kernel: main-r5f0(s)/main-r5f1(s) fails to run","am62axx_sk-fs,am64xx-evm,am64xx-hsevm",""
   "LCPD-38619","Documentation: kernel:  Update How_to_Check_Device_Tree_Info section","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,beagleplay-gp",""
   "LCPD-38254","Watchdog reset not functional: ESM pins are wrong","am62axx_sk-fs,am62pxx_sk-fs,am64xx-hsevm",""
   "LCPD-38252","Remove warning about graceful shutdown not supported","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,am64xx-evm",""
   "LCPD-38139","Watchdog fails to reset chip when counter reaches 0","am62axx_sk-fs,am62pxx_sk-fs,am64xx-evm,am64xx_sk-fs",""
   "LCPD-38074","Add Timer PWM documentation and other infrastructure as needed","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs",""
   "LCPD-38040","mailbox tests marked as passing, but seem to actually fail","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am64xx-evm",""
   "LCPD-38039","Spinlock tests marked as passing, but seem to actually fail","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am64xx-evm",""
   "LCPD-38005","GPMC NAND driver runtime_pm support","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-38004","serial NAND driver runtime_pm support","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-37998","rpmsg_zerocopy MCU+ projects have outdated CCS files","am62axx_sk-fs,am62xx_lp_sk-fs,am64xx_sk-fs",""
   "LCPD-37977","upstream early boot support for AM62A","am62axx_sk-fs,am62axx_sk-se",""
   "LCPD-37935","AM62A Deep Sleep Cycle Failure","am62axx_sk-fs",""
   "LCPD-37920","ti-rpmsg-char should use the same toolchain as current Yocto build","am335x-evm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-gpevm,am571x-idk,am572x-idk,am574x-idk,am57xx-evm,am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am64xx-evm,am64xx_sk-fs,am654x-idk",""
   "LCPD-37828","SPL: Use speedgrade info to choose the A53 clock values","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs",""
   "LCPD-37812","Linux headers in targetfs is not same as in ti-linux-kenel","am62axx_sk-fs,am62axx_sk-se,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j784s4-evm,j784s4-hsevm",""
   "LCPD-37789","Automate_Test: E0510 jpeg encoder should support system PM, runtime PM and active use-case suspend/resume","am62axx_sk-fs",""
   "LCPD-37750","SDK Documentation: Formatting: Spacing between Lines seems broken","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se",""
   "LCPD-37732","Linux SDK 09.02: CPSW EST Switch mode does not work","am62axx_sk-fs",""
   "LCPD-37543","AM62A Yocto SDK UG: OSPI U-Boot Section Incomplete (PHY Calibration, Programming, etc.)","am62axx_sk-fs",""
   "LCPD-37377","Doc: U-Boot: No documentation for OSPI NAND","am62axx_sk-fs,am62axx_sk-se,am62xx_lp_sk-fs",""
   "LCPD-37342","cpufreq: schedutil: constant switch between CPU OPPs","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs",""
   "LCPD-37226","Update Ubuntu Host version in Linux documentation","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am62axx_sk-fs,am62axx_sk-se,am62lxx_evm-fs,am62lxx_evm-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am654x-evm,am654x-hsevm,am654x-idk,beagleplay-gp",""
   "LCPD-37210","MMC driver runtime_pm support","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-37209","USB driver runtime_pm support","am62axx_sk-fs,am62axx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-37208","CPSW driver runtime_pm support","am62axx_sk-fs,am62axx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-37187","Enable remaining GPIO SOC pins on am62a for RPi Header Expansion","am62axx_sk-fs,am62axx_sk-se",""
   "LCPD-36993","U-Boot: lpddr4.c: Error handling missing failure cases","am62axx_sk-fs,am62axx_sk-se,am62lxx-vlab,am62lxx-zebu,am62lxx_evm-fs,am62lxx_evm-se,am62pxx-zebu,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am69_sk-fs,bbai,bbai64-gp,beaglebone,beagleplay-gp,j7200-evm,j7200-hsevm,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j784s4-evm,j784s4-hsevm,J784S4_BASESIM",""
   "LCPD-36950","crypto openssl performance test fail","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs",""
   "LCPD-36630","AM62A dts files missing RTI nodes","am62axx_sk-fs",""
   "LCPD-36575","AM62Q: AM62A: OSPI:  tuning fails at certain PVTs","am62axx_sk-fs,am62axx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se",""
   "LCPD-34926","Some LTP tests are failing due to missing configurations","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,am64xx-hsevm,j7200-evm",""
   "LCPD-34912","AM62/AM62Ax: DM does not set correct pixel clock","am62axx_sk-fs,am62axx_sk-hs4,am62axx_sk-hs5,am62axx_sk-se,am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-hs4,am62xx_sk-hs5,am62xx_sk-se",""
   "LCPD-34409","test case naming ""soft boot"" should be ""reboot""","am62axx_sk-fs,am62xx_sk-fs,j721e-idk-gw,j721s2-evm,j721s2_evm-fs",""
   "LCPD-34360","Display distorted above certain resolution","am62axx_sk-fs",""
   "LCPD-34137","U-Boot OSPI-NAND read performance needs to be optimized","am62axx_sk-fs",""
   "LCPD-32931","OSPI: Update PHY tuning algorithm for PHY Tuning limitations","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_sk-fs,am68_sk-fs,am69_sk-fs,j7200-evm,j7200-hsevm,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j784s4-evm,j784s4-hsevm","Forced Half-Cycle DLL Lock Mode ,100MHz - 166MHz only (100MHz is a Master Mode DLL limitation) Full tuning range of 0-127 should be the default for both RX and TX"
   "LCPD-32906","OSPI: Read data mismatch(first 32 bytes) when using DMA memcpy","am62axx_sk-fs,am62axx_sk-hs4,am62axx_sk-hs5,am62axx_sk-se,am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-hs4,am62xx_sk-hs5,am62xx_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_sk-fs,am64xx_sk-hs4,am64xx_sk-hs5,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am69_sk-fs,j7200-evm,j7200-hsevm,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j784s4-evm,j784s4-hsevm",""
   "LCPD-32353","SBL remote core images does not fit the partition table defined by LINUX for serial NAND ","am62axx_sk-fs,am62xx-lp-sk,am62xx_lp_sk-fs",""
   "LCPD-24456","Move IPC validation source from github to git.ti.com","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-epos,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am62axx_sk-fs,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am64xx-evm,am64xx-hsevm,am64xx_sk-fs,am654x-evm,am654x-hsevm,am654x-idk,bbai,beaglebone,beaglebone-black,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm,j7200-evm,j7200-hsevm,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,omapl138-lcdk",""
   "LCPD-23936","Test: AM62A: Linux: Add support for MCAN","am62axx_sk-fs",""
   "SYSFW-5992","Unable to set exact pixel clock for OLDI LCD display / HDMI Pixel clock","am62x, am62a, am62px",""
   "SYSFW-6369","DM unable to enter deep sleep mode when booting in SBL flow","am62x, am62a, am62px",""
   "SYSFW-6432","Set device API doesn't return Error when PD is in transition state","am62x,am62ax,am62px,am64x,am65x",""
   "SYSFW-6426","Ownership of a firewall region can be transferred to an invalid host","am62x,am62ax,am62px,am64x,am65x",""
   "SYSFW-7096","TIFS halts when proc auth boot TISCI message is sent for an AES-256 encrypted appimage","am62ax",""
   "SYSFW-7559","LPM: In MCU Only mode resume path the MCU_M4 LPSC is ON","am62x,am62ax,am62px",""
   "SYSFW-7571","LPM: Device IDs higher than 255 will not work with set device constraint","am62x,am62ax,am62px",""
   "SITSW-4773","DM is not receiving the exact flags passed by sender for all K3 devices","am62x,am62ax,am62px",""

|

Closed Issues in Current Release
--------------------------------

.. csv-table::
   :header: "Record ID", "Title", "Platform"
   :widths: 15, 70, 25

   "LCPD-38600","RPROC_DMABUF_ATTACH ioctl is not thread safe","am62axx_sk-fs,am62axx_sk-se,j721e-idk-gw,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j722s_evm-fs,j784s4-evm,j784s4-hsevm"
   "LCPD-38529","Documentation: PM: Update Docs for 10.00","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs"
   "LCPD-38372","FPDLink: RX Port skipping leads to corrupt VC","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,j7200-evm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2_evm-fs,j722s_evm-fs,j784s4-evm"
   "LCPD-38350","DMABuf import not working with CnM codec in ti-linux-6.6","am62axx_sk-fs,j721s2-evm,j784s4-evm"
   "LCPD-38196","AM62a Encode/Decode broken by introducing Runtime PM for Wave5","am62axx_sk-fs"
   "LCPD-38135","POWERMGR_S_FUNC_CPUFREQ_BASIC functional test failure","am62axx_sk-fs"
   "LCPD-38098","IPC failure in LTS 2024","am62axx_sk-fs,am62axx_sk-se,am62lxx-vlab,am62lxx-zebu,am62lxx_evm-fs,am62lxx_evm-se,am62pxx-zebu,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am68_sk-se,am69_sk-fs,j7200-evm,j7200-hsevm,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j784s4-evm,j784s4-hsevm"
   "LCPD-38094","AM62A MJPEG Encoder - Add Metadata support","am62axx_sk-fs,am62axx_sk-se"
   "LCPD-38038","6.6.30 : Build Regression on K3 platforms due to kselftest","am335x-evm,am437x-idk,am57xx-evm,am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am64xx-hsevm,am654x-idk,am68_sk-fs,am69_sk-fs"
   "LCPD-38001","Doc: Uboot build instructions need to document specific python dependencies for binman","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am64xx-hsevm,j7200-evm,j721e-idk-gw,j721s2-evm,j721s2_evm-fs,j722s_evm-fs,j784s4-evm"
   "LCPD-37898","watchdog documentation should explain how to set timeout","am335x-evm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-gpevm,am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,am64xx-evm,am64xx_sk-fs,am654x-evm,am654x-idk"
   "LCPD-37886","AM62a: Linux: SD is not enumerated in SDR104 speed mode","am62axx_sk-fs,am62axx_sk-se"
   "LCPD-37743","AM64x: K3conf SoC rev kernel crash test fails","am62axx_sk-fs,am62axx_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk"
   "LCPD-37714","CAN suspend and loopback tests are failing","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk"
   "LCPD-37373","wave5 VPU page-faults on poison memory address during long test","am62axx_sk-fs"
   "LCPD-37320","AM62P: AM62A: update OPP speed grade decoding","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se"
   "LCPD-37141","AM62x: Sync up USB R5 defconfigs with main R5 defconfig","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs"
   "LCPD-35360","TIDEC_S_FUNC_GST_DECODE_AHP_MULTICHANNEL_FILE_AUD_MW_E test failure","am62axx_sk-se"
   "LCPD-32344","AM62: McASP recording causes CPU freezes","am62axx_sk-fs,am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xx_sk-fs,am62xx_sk-se"
   "LCPD-32250","Doc: Linux driver for eQEP","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-hssk,am64xx_sk-fs,am64xx_sk-se"
   "SYSFW-7536","Sending JTAG unlock certificate to TIFS using T32 JTAG fails","am62x,am62ax,am62px,am64x,am65x"
   "SYSFW-7474","Write access from DMA initiators to RA GCFG region results in firewall exception","am62x,am62ax,am62px"
   "SYSFW-7463","TISCI_MSG_GET_CLOCK always return Enabled for input clock","am62x,am62ax,am62px,am64x,am65x"
   "SYSFW-7485","Update the PLL driver in TIFS boot flow to follow correct sequence","am62x,am62ax,am62px,am64x,am65x"
   "SYSFW-7486","PM: Cleanup additional steps in pll init startup routine","am62x,am62ax,am62px,am64x,am65x"


|
