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

-  Linux Manifest:  :file:`<PSDK_PATH>/docs/software_manifest.html`

Release 10.01.10.04
===================

Released on December 2024

What's new
----------

**Processor SDK Linux AM62X Release has following new features:**

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

| Head Commit: 836b1a3aa89d087474495ab4f77fc7a06ffcef0f edgeai-test-data.bb: edgeai-tidl-models.bb: Updated EDGEAI_SDK_VERSION
| Date: 2024-07-30 05:58:20 -0500

| Clone: https://git.ti.com/git/edgeai/meta-edgeai.git
| Branch: scarthgap
| Release Tag: 10.00.00.04
|

.. important::

    meta-edgeai layer is not applicable in case of SK-AM62-SIP (i.e. am62xxsip-evm)

Issues Tracker
==============

Errata Workarounds Available in this Release
--------------------------------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform"
   :widths: 15, 30, 150

   "LCPD-37965","BCDMA: RX Channel can lockup in certain scenarios","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se"
   "LCPD-37081","SNPS: USB2 PHY locks up due to short suspend","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xxsip_sk-fs"
   "LCPD-27887","i2327: RTC: Hardware wakeup event limitation","am62xx-sk,am62xx_sk-fs,am62xxsip_sk-fs,am62xxsip_sk-se"
   "LCPD-27886","USART: Erroneous clear/trigger of timeout interrupt","am62axx_sk-fs,am62xx-sk,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,j7200-evm,j721e-idk-gw,j784s4-evm,j784s4-hsevm"

|

.. _known-issues:

Known Issues
------------
.. csv-table::
   :header: "Record ID", "Title", "Platform", "Workaround"
   :widths: 5, 10, 60, 25

   "LCPD-38689","Linux benchmarks: add context to Boot-time measurement","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am64xx-evm,am654x-evm",""
   "LCPD-38688","RT Linux benchmarks: add histogram for cyclic test","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am64xx-evm",""
   "LCPD-38687","LPM: TI SCI: debug prints during suspend print wrong CPU device for max latency set","am62axx_sk-fs,am62axx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-38670","misleading GPMC message in kernel log","am62xx_lp_sk-fs,am62xx_lp_sk-se",""
   "LCPD-38669","PHY configs not restored afer suspend-resume","am62xx_lp_sk-fs,am62axx_sk-fs","Checkout to tag: 10.00.08 (https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/commit/?h=ti-linux-6.6.y-cicd&id=db88712931433e92a5f73cec57c82c5c7ebee593) or Apply the following 3 commits: 'c3c859de6142 spi: cadence-quadspi: Define cqspi_phy_set_dll_master', 'e64d4d321e85 spi: cadence-quadspi: Store phy_setting in flash private data', '6b5642d52397 spi: cadence-quadspi: Move restore_context to runtime_resume'"
   "LCPD-38662","rcu_preempt self-detected stall on CPU","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,j721e-idk-gw,j721s2-evm",""
   "LCPD-38660","AM62*: CAN: mcu_mcan0 regression","am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se",""
   "LCPD-38626","PRU needed in DTS for AM62x-lp for IPC PRU Echo Test","am62xx_lp_sk-fs",""
   "LCPD-38619","Documentation: kernel:  Update How_to_Check_Device_Tree_Info section","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,beagleplay-gp",""
   "LCPD-38617","Documentation: IPC_AM62x:  Remove references of am62-main-r5f0_0-fw","am62xx_lp_sk-fs,am62xx_sk-fs",""
   "LCPD-38528","Documentation: IPC:  Update 6.1.y links to 6.6.y","am62pxx_sk-fs,am62xx_sk-fs,j722s_evm-fs",""
   "LCPD-38525","U-Boot packages Encryption key (custMpk.key) as replica of the Signing key (custMpk.pem)","am62pxx_sk-se,am62xx_lp_sk-se,am62xx_sk-se,am64xx-evm,am64xx-hsevm",""
   "LCPD-38373","Linux: AM62 USB interoperability broken as LPM is enabled","am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-38370","Random data mismatch for reading from eMMC RPMB","am62xx_sk-fs",""
   "LCPD-38313","beagleplay: TI IPC is missing in SDK 10.0","beagleplay-gp",""
   "LCPD-38252","Remove warning about graceful shutdown not supported","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,am64xx-evm",""
   "LCPD-38243","beagleplay: davinci-mcasp warning spam on boot logs","beagleplay-gp",""
   "LCPD-38194","incorrect PRUSS clock ID in device tree","am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se",""
   "LCPD-38133","IPC_S_FUNC_PRU_ECHO functional test failures","am335x-evm,am43xx-gpevm,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am64xx-hsevm,am654x-idk",""
   "LCPD-38127","Deep Sleep GPIO Retention","am62xx_lp_sk-fs,am62xx_sk-fs",""
   "LCPD-38100","AM62x: sa2ul: Selftest failure","am62xx_sk-fs",""
   "LCPD-38097","am62 Boot Failure","am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se",""
   "LCPD-38074","Add Timer PWM documentation and other infrastructure as needed","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs",""
   "LCPD-38040","mailbox tests marked as passing, but seem to actually fail","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am64xx-evm",""
   "LCPD-38039","Spinlock tests marked as passing, but seem to actually fail","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am64xx-evm",""
   "LCPD-38005","GPMC NAND driver runtime_pm support","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-38004","serial NAND driver runtime_pm support","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-37998","rpmsg_zerocopy MCU+ projects have outdated CCS files","am62axx_sk-fs,am62xx_lp_sk-fs,am64xx_sk-fs",""
   "LCPD-37934","CAN: Dropped frames ","am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se",""
   "LCPD-37920","ti-rpmsg-char should use the same toolchain as current Yocto build","am335x-evm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-gpevm,am571x-idk,am572x-idk,am574x-idk,am57xx-evm,am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am64xx-evm,am64xx_sk-fs,am654x-idk",""
   "LCPD-37838","8250_omap: incorrect handling of dma->rx_running flag","am335x-evm,am62xx_sk-fs",""
   "LCPD-37828","SPL: Use speedgrade info to choose the A53 clock values","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs",""
   "LCPD-37750","SDK Documentation: Formatting: Spacing between Lines seems broken","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se",""
   "LCPD-37653","AM62B/-P1 SK: i2c1/audio goes haywire when 2nd IO expander is added","am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-37591","am62x-lp-fs : Power Suspend/Resume test failure  on automation platform over NFS","am62xx_lp_sk-fs",""
   "LCPD-37554","Update the AM625 DTS for AM62B-P1 board","am62xx_sk-fs",""
   "LCPD-37377","Doc: U-Boot: No documentation for OSPI NAND","am62axx_sk-fs,am62axx_sk-se,am62xx_lp_sk-fs",""
   "LCPD-37358","Eth: TCP bidir tests failing in CI ","am62xx_lp_sk-fs",""
   "LCPD-37342","cpufreq: schedutil: constant switch between CPU OPPs","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs",""
   "LCPD-37321","suspend-to-RAM wakeup by plugging in USB device is not reliable","am62xx_lp_sk-fs",""
   "LCPD-37226","Update Ubuntu Host version in Linux documentation","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am62axx_sk-fs,am62axx_sk-se,am62lxx_evm-fs,am62lxx_evm-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am654x-evm,am654x-hsevm,am654x-idk,beagleplay-gp",""
   "LCPD-37210","MMC driver runtime_pm support","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-37209","USB driver runtime_pm support","am62axx_sk-fs,am62axx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-37208","CPSW driver runtime_pm support","am62axx_sk-fs,am62axx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-37126","AM62x HS-FS resume failing","am62xx_sk-fs",""
   "LCPD-37076","Suspend/resume locks up due to OP-TEE RNG","beagleplay-gp",""
   "LCPD-37064","Linux kernel crash observed while booting from EMMC","am62xx_sk-fs",""
   "LCPD-37053","AM62x: Deep Sleep: tidss Timeout waiting for framedone on crtc 1","am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-36993","U-Boot: lpddr4.c: Error handling missing failure cases","am62axx_sk-fs,am62axx_sk-se,am62lxx-vlab,am62lxx-zebu,am62lxx_evm-fs,am62lxx_evm-se,am62pxx-zebu,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am69_sk-fs,bbai,bbai64-gp,beaglebone,beagleplay-gp,j7200-evm,j7200-hsevm,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j784s4-evm,j784s4-hsevm,J784S4_BASESIM",""
   "LCPD-36978","AM62xSiP: DeepSleep: Suspend-Resume not working","am62xxsip_sk-fs,am62xxsip_sk-se",""
   "LCPD-36950","crypto openssl performance test fail","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs",""
   "LCPD-36925","am62xx-lp-sk: power down from automation interface behaves differently between U-Boot and kernel","am62xx_lp_sk-fs,am62xx_lp_sk-se",""
   "LCPD-36918","meta-arago: Matrix GUI  change caused : runLmDDRBandwidth.sh failure","am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs",""
   "LCPD-36820","USB DFU: OSPI boot failure","am62xxsip_sk-fs",""
   "LCPD-36812","RTC: tests fail","am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se",""
   "LCPD-36805","ETHERNET boot test fail incorrect configuration","am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se",""
   "LCPD-36804","IPC performance test fail - modprobe fails","am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se",""
   "LCPD-36803","USBDEV:  test case fail - USB devices not enumerated","am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se",""
   "LCPD-36575","AM62Q: AM62A: OSPI:  tuning fails at certain PVTs","am62axx_sk-fs,am62axx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se",""
   "LCPD-36524","AM62x: sa2ul doesn't work after deepsleep","am62xx_sk-fs",""
   "LCPD-36462","ti-u-boot:AM62x SK: Update ITAP/OTAP values in device tree ","am62xx_lp_sk-fs,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-36457","am62xx-sk: DHCP, tftp occasionally fail when bothe network interfaces are connected","am62xx_sk-fs",""
   "LCPD-36436","ti-linux:AM62x SK: Update ITAP/OTAP values in device tree ","am62xx_lp_sk-fs,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-36423","am62sip: uboot: fdt memory region failed ","am62xxsip_sk-se",""
   "LCPD-36414","Performance numbers for NOR, eMMC missing in doc","am62xx_sk-fs,am64xx-evm",""
   "LCPD-36320","AM62x: DM FW sets wrong CPU core frequency","am62xx-sk,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-36282","OV5640 capture not working at two highest resolutions","am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-35042","Linux: AM62x: OSPI NOR Flash read speed is low (~2.5MBPS)","am62xx-sk,am62xx_sk-fs,am62xx_sk-hs4,am62xx_sk-hs5,am62xx_sk-se",""
   "LCPD-34951","AM62: Board not booting up with new auto-gen data","am62xx_sk-fs",""
   "LCPD-34926","Some LTP tests are failing due to missing configurations","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,am64xx-hsevm,j7200-evm",""
   "LCPD-34916","AM62x: op-tee with LOG_LEVEL=2 crashes after Deep Sleep","am62xx-sk,am62xx_sk-fs",""
   "LCPD-34912","AM62/AM62Ax: DM does not set correct pixel clock","am62axx_sk-fs,am62axx_sk-hs4,am62axx_sk-hs5,am62axx_sk-se,am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-hs4,am62xx_sk-hs5,am62xx_sk-se",""
   "LCPD-34906","R5 SPL OSPI NOR with PHY calibration not working","am62xx-sk",""
   "LCPD-34901","AM62: Reset button fails to reset AM625-SK-EVM after wakeup from deep sleep","am62xx-sk,am62xx_sk-fs",""
   "LCPD-34888","AM625-Beagleplay : u-boot: Fix MDIO bit bang","beagleplay-gp",""
   "LCPD-34816","rtcwake fails after resuming from Deep Sleep","am62xx-sk,am62xx_sk-fs",""
   "LCPD-34643","NAND is not using most optimized timing","am62xx_sk-fs",""
   "LCPD-34409","test case naming ""soft boot"" should be ""reboot""","am62axx_sk-fs,am62xx_sk-fs,j721e-idk-gw,j721s2-evm,j721s2_evm-fs",""
   "LCPD-34343","SDK: Am62x: Openssl commands for openssl_perf.sh gives wrong results","am62xx-sk",""
   "LCPD-34059","copying files to eMMC causes kernel crash","am62xx-lp-sk,am62xx-sk,am62xx_sk-fs",""
   "LCPD-32931","OSPI: Update PHY tuning algorithm for PHY Tuning limitations","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_sk-fs,am68_sk-fs,am69_sk-fs,j7200-evm,j7200-hsevm,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j784s4-evm,j784s4-hsevm","Forced Half-Cycle DLL Lock Mode, 100MHz - 166MHz only (100MHz is a Master Mode DLL limitation) Full tuning range of 0-127 should be the default for both RX and TX"
   "LCPD-32906","OSPI: Read data mismatch(first 32 bytes) when using DMA memcpy","am62axx_sk-fs,am62axx_sk-hs4,am62axx_sk-hs5,am62axx_sk-se,am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-hs4,am62xx_sk-hs5,am62xx_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_sk-fs,am64xx_sk-hs4,am64xx_sk-hs5,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am69_sk-fs,j7200-evm,j7200-hsevm,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j784s4-evm,j784s4-hsevm",""
   "LCPD-32813","AM62X U-Boot: Fails to mount UBIFS in OSPI-NOR","am62xx-sk,am62xx_sk-fs",""
   "LCPD-32706","Display: DRM tests fail inconsistently","am62xx-sk,am62xx_sk-fs",""
   "LCPD-32353","SBL remote core images does not fit the partition table defined by LINUX for serial NAND ","am62axx_sk-fs,am62xx-lp-sk,am62xx_lp_sk-fs",""
   "LCPD-32351","MMCSD: HS200 and SDR104 Command Timeout Window Too Small","am62xx-sk,am62xx_sk-fs,am62xx_sk-se","If the command requires a timeout longer than 700ms, then the MMC host controller command timeout can be disabled (MMCSD_CON[6] MIT=0x1) and a software implementation may be used in its place"
   "LCPD-29933","Linux SDK docs: GPIO Guide feels insufficient","am62xx-sk,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-29879","AM62x: MMC Modular NEG RMMOD when mount test fail","am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-29877","am62x: openssl crypto performance tests fail","am62xx-sk,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-29876","am62x: crypto RNG functional and performance tests failures","am62xx-sk,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se",""
   "LCPD-29875","am62x: crypto SHA performance tests failures","am62xx-sk,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-29873","AM62x: host does not detect USB gadget","am62xx-sk,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-29871","AM62xx-lp-sk: UHS104 card FAT write results are out of expected range","am62xx-lp-sk,am62xx_lp_sk-fs",""
   "LCPD-29862","AM62x: Uboot qspi read write performance tests fail","am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-29851","CI/CD Snapshot page doesn't have default images.","am62xx-sk,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-29409","DMIPS number should reflect all 4 cores","am62pxx_sk-fs,am62pxx_sk-se,am62xx-sk,am62xx_sk-fs,am62xx_sk-se,j721e-idk-gw,j721s2-evm",""
   "LCPD-29332","LPM Demo not Working on Linux RT","am62xx-sk,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-28742","AM62x: Make ""Debugging SPL"" doc specific to AM62x","am62xx-sk,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-28514","AM62x: MMC Card detect does not work","am62xx-sk,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-28491","WiLink not functional with fw_devlink option set to `on` ","am62xx-sk,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-28448","Wall time does not account for sleep time","am62xx-sk,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-28138","AM62x: RTC tests fail in automated testing","am62xx-sk,am62xx_sk-fs,am62xx_sk-se",""
   "LCPD-28104","Automated test failure - CPSW test is passing invalid parameters to switch-config","am62xx-sk,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se",""
   "LCPD-24456","Move IPC validation source from github to git.ti.com","am335x-evm,am335x-hsevm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-epos,am43xx-gpevm,am43xx-hsevm,am571x-idk,am572x-idk,am574x-hsidk,am574x-idk,am57xx-beagle-x15,am57xx-evm,am57xx-hsevm,am62axx_sk-fs,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am64xx-evm,am64xx-hsevm,am64xx_sk-fs,am654x-evm,am654x-hsevm,am654x-idk,bbai,beaglebone,beaglebone-black,dra71x-evm,dra71x-hsevm,dra72x-evm,dra72x-hsevm,dra76x-evm,dra76x-hsevm,dra7xx-evm,dra7xx-hsevm,j7200-evm,j7200-hsevm,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,omapl138-lcdk",""
   "LCPD-38707","Ethernet Boot on AM62-LP-SK is broken","am62xx_lp_sk-fs","`U-Boot fix <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2024.04-next&id=7986fd679935818d0ef11e6a334377df178774f6>`__ , `Kernel-Fix <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/commit/?h=ti-linux-6.6.y-cicd&id=d80245c38ed4432878e5fe309f6ba958fd2c2e8f>`__"
   "SYSFW-5992","Unable to set exact pixel clock for OLDI LCD display / HDMI Pixel clock","am62x, am62a, am62px",""
   "SYSFW-6369","DM unable to enter deep sleep mode when booting in SBL flow","am62x, am62a, am62px",""
   "SYSFW-6432","Set device API doesn't return Error when PD is in transition state","am62x,am62ax,am62px,am64x,am65x",""
   "SYSFW-6426","Ownership of a firewall region can be transferred to an invalid host","am62x,am62ax,am62px,am64x,am65x",""
   "SYSFW-7559","LPM: In MCU Only mode resume path the MCU_M4 LPSC is ON","am62x,am62ax,am62px",""
   "SYSFW-7571","LPM: Device IDs higher than 255 will not work with set device constraint","am62x,am62ax,am62px",""
   "SITSW-4773","DM is not receiving the exact flags passed by sender for all K3 devices","am62x,am62ax,am62px",""
   "SITSW-3922","Flash writer: Benchmark script fails for emmc logs","am62x,am62ax,am62px,am64x",""
   "SITSW-5041","Debian: LPM not working again on AM62P, AM62LP and AM62SIP","am62p-sk,am62xx-sk-lp,am62x-sip-sk",""
   "SITSW-5049","Debian: Chromium doesn't display minimize and maximize buttons","am62p-sk,am62xx-sk,am62xx-sk-lp",""
   "SITSW-4864","TI Debian SDK: Docker not working","am62xx-sk,am62xx-sk-lp,am62x-sip-sk,am62p-sk,am64xx-evm,am64xx-sk",""


|

Closed Issues in Current Release
--------------------------------
.. csv-table::
   :header: "Record ID", "Title", "Platform"
   :widths: 15, 70, 25

   "LCPD-38691","Documentation: Remove external links of Kernel 5.10/ 6.1 &/or U-Boot 2023.04","am62pxx_sk-fs,am62xx-evm,am64xx-evm,am654x-evm"
   "LCPD-38685","Documentation: U-Boot: Update doc references to 2024.04","am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs"
   "LCPD-38625","AM62x: RT-Linux Latency Regression","am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se"
   "LCPD-38532","Documentation: U-Boot: Update DDR doc references to 2024.04","am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs"
   "LCPD-38531","Documentation: Splash: Update doc to U-Boot 2024.04","am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs"
   "LCPD-38529","Documentation: PM: Update Docs for 10.00","am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs"
   "LCPD-38357","AM62: LPM failure: 29000000.mailbox: fifo 5 has unexpected unread messages","am62xx_sk-fs,am62xx_sk-se"
   "LCPD-38353","fitImage boot fails on HS-FS Platforms","am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx_sk-fs,am64xx_sk-se,beagleplay-gp"
   "LCPD-38305","tiL_6.6: OSPI NOR: UBIFS test fail","am62pxx_sk-fs,am62xx_sk-fs"
   "LCPD-38265","tiU_24.4: OSPI NOR Read taking more time","am62pxx_sk-fs,am62xx_sk-fs,am64xx_sk-fs"
   "LCPD-38239","AM62xx: Board doesn't resume from deepsleep","am62pxx_sk-fs,am62xx_sk-fs"
   "LCPD-38180","SK-AM62x: OSPI: spi-nor resume fails with error -22","am62pxx_sk-fs,am62xx_sk-fs"
   "LCPD-38098","IPC failure in LTS 2024","am62axx_sk-fs,am62axx_sk-se,am62lxx-vlab,am62lxx-zebu,am62lxx_evm-fs,am62lxx_evm-se,am62pxx-zebu,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se,am654x-evm,am654x-hsevm,am654x-idk,am68_sk-fs,am68_sk-se,am69_sk-fs,j7200-evm,j7200-hsevm,j721e-evm-ivi,j721e-hsevm,j721e-idk-gw,j721e-sk,j721s2-evm,j721s2-hsevm,j721s2_evm-fs,j721s2_evm-se,j722s_evm-fs,j784s4-evm,j784s4-hsevm"
   "LCPD-38038","6.6.30 : Build Regression on K3 platforms due to kselftest","am335x-evm,am437x-idk,am57xx-evm,am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am64xx-hsevm,am654x-idk,am68_sk-fs,am69_sk-fs"
   "LCPD-38001","Doc: Uboot build instructions need to document specific python dependencies for binman","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs,am62xxsip_sk-fs,am64xx-hsevm,j7200-evm,j721e-idk-gw,j721s2-evm,j721s2_evm-fs,j722s_evm-fs,j784s4-evm"
   "LCPD-37955","Uboot overlay paths are different for different boot sources","am62xx_sk-fs"
   "LCPD-37898","watchdog documentation should explain how to set timeout","am335x-evm,am335x-ice,am335x-sk,am437x-idk,am437x-sk,am43xx-gpevm,am62axx_sk-fs,am62pxx_sk-fs,am62xx_sk-fs,am64xx-evm,am64xx_sk-fs,am654x-evm,am654x-idk"
   "LCPD-37875","U-boot: otapdly and otap_del_sel do not get written to PHY CTRL 4 reg","am62pxx_sk-fs,am62pxx_sk-se,am62xx-sk,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk,am64xx_evm-se,am64xx_sk-fs,am64xx_sk-se"
   "LCPD-37714","CAN suspend and loopback tests are failing","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm,am64xx-hsevm,am64xx-hssk"
   "LCPD-37417","RGX_S_FUNC_APM test is failing","am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_sk-fs,am62xx_sk-se,am68_sk-fs,am69_sk-fs,j721e-idk-gw,j721s2-evm,j722s_evm-fs,j784s4-evm"
   "LCPD-37355","Watchdog timer cannot be pet","am62xx_sk-fs"
   "LCPD-37141","AM62x: Sync up USB R5 defconfigs with main R5 defconfig","am62axx_sk-fs,am62pxx_sk-fs,am62xx_lp_sk-fs,am62xx_sk-fs"
   "LCPD-36846","u-boot usb reset command fails","am62xx_sk-fs"
   "LCPD-36618","AM62SIP:  reserving fdt memory region failed error seen at bootup","am62xxsip_sk-fs,am62xxsip_sk-se"
   "LCPD-32478","Linux Benchmark/performance data is missing","am62xx-sk,am62xx_sk-fs,am62xx_sk-se,am64xx-hsevm,am64xx-hssk,am64xx_sk-fs"
   "LCPD-32344","AM62: McASP recording causes CPU freezes","am62axx_sk-fs,am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xx_sk-fs,am62xx_sk-se"
   "LCPD-32250","Doc: Linux driver for eQEP","am62axx_sk-fs,am62axx_sk-se,am62pxx_sk-fs,am62pxx_sk-se,am62xx_lp_sk-fs,am62xx_lp_sk-se,am62xx_p0_sk-fs,am62xx_sk-fs,am62xx_sk-se,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-hssk,am64xx_sk-fs,am64xx_sk-se"
   "LCPD-29649","inta_ack results in NULL pointer exception","beagleplay-gp"
   "LCPD-38690","Documentation: Remove reference of denx.de/wiki","am62pxx_sk-fs,am62pxx_sk-se,am62xx-evm,am62xx-lp-sk,am62xx-sk,am62xx_lp_sk-fs,am62xxsip_sk-fs,am62xxsip_sk-se,am64xx-evm"
   "SYSFW-7536","Sending JTAG unlock certificate to TIFS using T32 JTAG fails","am62x,am62ax,am62px,am64x,am65x"
   "SYSFW-7474","Write access from DMA initiators to RA GCFG region results in firewall exception","am62x,am62ax,am62px"
   "SYSFW-7463","TISCI_MSG_GET_CLOCK always return Enabled for input clock","am62x,am62ax,am62px,am64x,am65x"
   "SYSFW-7485","Update the PLL driver in TIFS boot flow to follow correct sequence","am62x,am62ax,am62px,am64x,am65x"
   "SYSFW-7486","PM: Cleanup additional steps in pll init startup routine","am62x,am62ax,am62px,am64x,am65x"
   "SITSW-4481","Debian SDK documentation misses instructions for building kernel package","am62x-sk,am62p-sk,am64xx-evm,am64xx-sk,am62xx-sk-lp,am62x-sip-sk"
   "SITSW-4288","Debian: Dual-display doesn't work out-of-box","am62xx-sk,am62p-sk,am62xx-sk-lp,am62x-sip-sk"
   "SITSW-5040","TI Debian SDK: Build instructions no longer working due to ti-bdebstrap Advancement","am62xx-sk,am62xx-sk-lp,am62x-sip-sk,am62p-sk,am64xx-evm,am64xx-sk"

|


