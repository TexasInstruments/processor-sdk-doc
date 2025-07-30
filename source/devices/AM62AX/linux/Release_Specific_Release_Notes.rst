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

-  Linux Manifest: :file:`<PSDK_PATH>/manifest/software_manifest.htm`


Release 11.01.07.05
===================

Released on Aug 2025

What's new
----------

**Processor SDK Linux AM62AX Release has following new features:**

  - First 2025 LTS Reference Release Including RT combined branch model
  - Out-of-the-Box EdgeAI Gallery App powered by QT 6.9 for seamless AI experiences
  - EdgeAI memory carveouts now supported via `k3-am62a7-sk-edgeai.dtso <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62a7-sk-edgeai.dtso?h=11.01.07>`_ in ti-linux-kernel & applied by default in the AM62A board environment via the name_overlays variable in ti-u-boot as seen in `board/ti/am62ax/am62ax.env <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/board/ti/am62ax/am62ax.env?h=11.01.07#n22>`_
  - Support for SELinux via meta-selinux with tisdk-edgeai-image
  - EdgeAI DM R5 (:file:`dm_edgeai_mcu1_0_release_strip.out`) & C7x IPC (:file:`dsp_edgeai_c7x_1_release_strip.out`) firmwares delivered via `ti-linux-firmware <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tree/?h=11.01.07>`_
  - Linux Remoteproc driver now boots remote cores (MCU R5 & C7x) by default during Linux kernel boot time to support Low Power Mode (LPM) with EdgeAI firmwares.
  - Simplified the Yocto build process for :file:`tisdk-edgeai-image` by eliminating the unnecessary edgeai branding step - :ref:`Building the SDK with Yocto <building-the-sdk-with-yocto>`
  - EdgeAI DM R5 & C7x firmwares now default to remote endpoint 14 for consistency across Sitara AM6x platforms with Linux RPMsg userspace application - :ref:`IPC for AM62ax <foundational-components-ipc>`
  - Support for suspend/resume of C7x in Edge AI Stack (currently context for VPAC and TIDL is not saved)
  - Falcon mode through R5 SPL :ref:`U-Boot Falcon Mode <U-Boot-Falcon-Mode>`
  - TIDL - TI Deep Learning Library
     - Module safety for TIDL
     - Added support for 6 dimensions in Transpose
     - Added support for several new operators: Unsqueeze, Acos, Atan, Cos, CosH, ELU, Neg, Tan, TanH, ScatterElements, SiLU
     - Enhanced broadcast capabilities for MatMul, Add & Mul operators
     - TIDL Host emulation supports runtime redirection of temporary buffers to a specified path (Instead of :file:`/dev/shm`)
  - Imaging
     - Support for IMX728 camera sensor
     - Support for RGB color space
     - Support to access VPAC PSA signature data
     - Added support for YUV422I format
     - Multiple bug fixes w.r.t VPAC MSC and LDC subsystem
  - Important Bug Fixes on top of Processor SDK 10.01.00.05 Release
  - Review Issue Tracker Section for the new fixes - :ref:`Link to Issues Tracker <issue-tracker>`

**Key Release References:**

  - RT Kernel : Real-Time Linux Interrupt Latency numbers here :ref:`RT Interrupt Latencies <RT-linux-performance>`
  - Support for streaming from OV2312 camera with `DS90UB954-Q1EVM <https://www.ti.com/tool/DS90UB954-Q1EVM>`_
  - How standby power mode works - :ref:`CPUIdle Documentation <cpuidle-guide>`

**Component version:**

  - Kernel 6.12.35
  - U-Boot 2025.01
  - Toolchain GCC 13.4
  - ATF 2.13+
  - OPTEE 4.6.0
  - TIFS Firmware / SYSFW `v11.01.02 <https://software-dl.ti.com/tisci/esd/11_01_02/release_notes/release_notes.html>`__ (Click on the link for more information)
  - DM Firmware 11.01.00.05
  - Yocto scarthgap 5.0


Build Information
=================

.. _u-boot-release-notes:

U-Boot
------

| Head Commit: 3bcfad6cee95403f7f62dd9d871cc3ea948c0761 PENDING: configs: am68_sk_r5_defconfig: Reduce ENV_SIZE
| uBoot Version: 2025.01
| uBoot Description: RC Release 11.01.07
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| uBoot Tag: 11.01.07
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
| Head Commit: f59a711599249ecac75fea38b7a15ef9137d650d Merge branch 'main' of git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware into ti-linux-firmware-next
| Clone: https://git.ti.com/cgit/processor-firmware/ti-linux-firmware
| Branch: ti-linux-firmware
| Tag: 11.01.07
|

Kernel
------
.. rubric:: Linux Kernel
   :name: linux-kernel

| Head Commit: 72f48d59b8f087fa0dd1f1e8c2c0b5bc0baa537c TI: arm64: dts: ti: k3-am642: Add eqep overlay
| Kernel Version: v6.12.35
| Kernel Description: RC Release 11.01.07

| Repo: git://git.ti.com/ti-linux-kernel/ti-linux-kernel.git
| Branch: ti-linux-6.12.y
| Tag: 11.01.07
| use-kernel-config=defconfig
| non-rt-config-fragment=kernel/configs/ti_arm64_prune.config
| rt-config-fragment=config-fragment=kernel/configs/ti_arm64_prune.config kernel/configs/ti_rt.config
|


Yocto
-----
.. rubric:: meta-ti
   :name: meta-ti

| Head Commit: 4b943f75bfeb04278b11c477a1e3b9ed768c56c1 CI/CD Auto-Merger: cicd.scarthgap.202507231325

| Clone: git://git.yoctoproject.org/meta-ti
| Branch: scarthgap
| Release Tag: 11.01.07
|

.. rubric:: meta-arago
   :name: meta-arago

| Head Commit: af3a6dd837018f70a2f7e1b6c78b593ece01d92f meta-arago-test: packagegroups: Add off-screen demo to ti-test package group

| Clone: git://git.yoctoproject.org/meta-arago
| Branch: scarthgap
| Release Tag: 11.01.07
|

.. rubric:: meta-tisdk
   :name: meta-tisdk

| Head Commit: 3265fc78d1dddd1642c112a2f3f42507bfa176d9 meta-ti-foundational: ti-apps-launcher: Update SRCREV

| Clone: https://github.com/TexasInstruments/meta-tisdk.git
| Branch: scarthgap
| Release Tag: 11.01.07.05
|

.. rubric:: meta-edgeai
   :name: meta-edgeai

| Head Commit: 2f3ea75ca6733035d5a60fc2a3fc7d15af9e9851 ti-vision-apps: am62axx: Bump up to REL.PSDK.ANALYTICS.AM62A.11.01.00.05

| Clone: https://git.ti.com/git/edgeai/meta-edgeai.git
| Branch: scarthgap
| Release Tag: 11.01.07.05
|

.. _issue-tracker:

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

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12108","audit for potential bugs with 6.6.44 stable merge "
   "EXT_EP-12098","Uboot docs: document renaming tiboot3-<evm>.bin file"
   "EXT_EP-12103","PHY configs not restored after suspend-resume"
   "EXT_EP-12058","rcu_preempt self-detected stall on CPU while running DSS usecases"
   "EXT_EP-12093","GPIO glitch observed while resuming from DeepSleep"
   "EXT_EP-12059","AM62A: Missing UB954-Q1 support"
   "EXT_EP-12063","Update the DDR configuration with DDR syscfg 9.09+"
   "EXT_EP-12064","AM62A Yocto SDK UG: OSPI U-Boot Section Incomplete (PHY Calibration, Programming, etc.)"
   "EXT_EP-12101","AM62A dts files missing RTI nodes"
   "EXT_EP-12109","Multi Instance Hang with Reduced CPU load patch"
   "EXT_EP-12107","Running camera pipelines causes kernel crash on all platforms"
   "EXT_EP-12106","higher latency metrics with Wave5"
   "EXT_EP-12105","Multistream decode stall during stop sequence"
   "SITSW-4773","DM is ignoring the exact flags sent in TISCI message"
   "SYSFW-5992","Unable to set exact pixel clock for OLDI LCD display / HDMI Pixel clock"
   "SYSFW-6426","Ownership of a firewall region can be transferred to an invalid host"
   "SYSFW-6432","Set device API doesn't return Error when PD is in transition state"
   "SYSFW-7096","TIFS halts when proc auth boot message is sent for an AES-256 encrypted image"
   "SYSFW-7571","Device IDs higher than 255 does not work with set device constraint API"
   "SYSFW-7602","RTC count value not getting updated after DeepSleep exit"
   "SYSFW-7614","Unable to configure DSS clock below 15.625MHz"
   "SYSFW-7617","LPM mode selection logic does not check for constraints on all the hosts/devices"
   "SYSFW-7739","LPM constraint messages received by TIFS not forwarded to DM"
   "SYSFW-7740","Only the last latency constraint value passed from a host considered in LPM selection"
   "SYSFW-7758","MAIN PLL15 HSDIVs (DM) if updated in SBL flow results in boot failure in later stages"


Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "EXT_EP-12111","Linux SDK v10.0: TI-added support for W25N01JW SPI NAND breaks other existing Flash support"
   "EXT_EP-12078","SK-AM62A: Stability issues with DDR Config v0.10.02"
   "EXT_EP-12077","Failure to enter DeepSleep with JPEG Encoder"
   "EXT_EP-12073","AM62Ax MCU domain pinmux disabled by default"
   "EXT_EP-12112","Add Timer PWM documentation and other infrastructure as needed"
   "EXT_EP-12127","Streaming with multiple cameras gets frozen in 2 minutes"
   "EXT_EP-12142","Instabilities observed while resuming from IO Only plus DDR mode"
   "SYSFW-7034","Read lock on extended OTP area does not work after doing write lock"
   "SYSFW-7622","DeepSleep resume failure when RTC wake is set for 1 second"
   "SYSFW-7781","Get device API does not return error when the LPSC is in transition state"
   "SYSFW-7811","Resume from IO Only + DDR mode fails sometimes"
   "SYSFW-7831","DMA Resources used by ROM are not cleaned up when resuming from IO Only + DDR mode"
   "SYSFW-7884","There is an additional divide by 4 on all clocks of WKUP/MCU GPIO clock mux"
   "SYSFW-7887","DeepSleep fails if entered immediately after bootup"
   "SYSFW-7897","Partial I/O mode fails after few hundred iterations"
   "SYSFW-7903","Processor ownership info is not part of minimal TIFS context in IO only + DDR mode"

