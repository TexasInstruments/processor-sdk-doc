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
  - Out-of-the-Box EdgeAI Gallery App powered by QT 6.9 for seamless AI experiences - :ref:`Edge AI Gallery - User Guide <Edge-AI-Gallery-User-Guide-label>`
  - EdgeAI memory carveouts now supported via `k3-am62a7-sk-edgeai.dtso <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62a7-sk-edgeai.dtso?h=11.01.07>`_ in ti-linux-kernel & applied by default in the AM62A board environment via the name_overlays variable in ti-u-boot as seen in `board/ti/am62ax/am62ax.env <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/board/ti/am62ax/am62ax.env?h=11.01.07#n22>`_ - `FAQ - EdgeAI memory carveouts <https://software-dl.ti.com/processor-sdk-linux/esd/AM62AX/11_01_07_05/exports/docs/devices/AM62AX/edgeai/faq.html#why-does-error-unable-to-map-memory-0xa2000000-appear-after-applying-a-custom-dtbo-using-name-overlays-from-sdk-11-1-with-edgeai>`__
  - Support for SELinux via meta-selinux with tisdk-edgeai-image - :ref:`Building the SELinux image with Yocto <building-the-sdk-with-yocto>` and :ref:`SELinux oeconfig file <yocto-layer-configuration>`
  - EdgeAI DM R5 (:file:`dm_edgeai_mcu1_0_release_strip.out`) & C7x IPC (:file:`dsp_edgeai_c7x_1_release_strip.out`) firmwares delivered via `ti-linux-firmware v11.01.07 <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tree/?h=11.01.07>`__
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
  - Negative edge panel support

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
  - TIFS Firmware / SYSFW `v11.01.05 <https://software-dl.ti.com/tisci/esd/11_01_05/release_notes/release_notes.html>`__ (Click on the link for more information)
  - DM Firmware `MSDK.11.01.00.16+ <https://github.com/TexasInstruments/mcupsdk-core-k3/tree/REL.MCUSDK.K3.11.01.00.16>`__ (Click on the link for more information)
  - Yocto scarthgap 5.0

.. _release-specific-build-information:

Build Information
=================

U-Boot
------

| Head Commit: 3bcfad6cee95403f7f62dd9d871cc3ea948c0761 PENDING: configs: am68_sk_r5_defconfig: Reduce ENV_SIZE
| uBoot Version: 2025.01
| uBoot Description: RC Release 11.01.07
| Clone: git://git.ti.com/ti-u-boot/ti-u-boot.git
| Branch: ti-u-boot-2025.01
| uBoot Tag: 11.01.07
|

TF-A
----
| Head Commit: e0c4d3903b382bf34f552af53e6d955fae5283ab Merge changes from topic "xlnx_fix_gen_con_datatype" into integration
| Repo: https://git.trustedfirmware.org/plugins/gitiles/TF-A/trusted-firmware-a.git/
| Branch: master
| Tag: (2.13 based)
|

OP-TEE
------
| Head Commit: 71785645fa6ce42db40dbf5a54e0eaedc4f61591 Update CHANGELOG for 4.6.0
| Repo: https://github.com/OP-TEE/optee_os/
| Branch: master
| Tag: 4.6.0
|

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

   "`EXT_EP-12128 <https://sir.ext.ti.com/jira/browse/EXT_EP-12128>`_","USB2 PHY locks up due to short suspend"
   "`EXT_EP-12123 <https://sir.ext.ti.com/jira/browse/EXT_EP-12123>`_","USART: Erroneous clear/trigger of timeout interrupt"
   "`EXT_EP-12124 <https://sir.ext.ti.com/jira/browse/EXT_EP-12124>`_","BCDMA: RX Channel can lockup in certain scenarios"
   "`EXT_EP-12114 <https://sir.ext.ti.com/jira/browse/EXT_EP-12114>`_","MMCSD: HS200 and SDR104 Command Timeout Window Too Small"

Issues Resolved
---------------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_SITMPUSW-143 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-143>`_","Yocto Documentation: AM6x: SDK: Build Instruction missing steps for building K3R5 baremetal toolchain"
   "`EXT_EP-12816 <https://sir.ext.ti.com/jira/browse/EXT_EP-12816>`_","SDK Docs: Broken URL in How To Guides > EVM Setup"
   "`EXT_EP-12314 <https://sir.ext.ti.com/jira/browse/EXT_EP-12314>`_","MJPEG Encoding doesn't work for 5MP resolution - 2592x1952."
   "`EXT_SITMPUSW-145 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-145>`_","Linux SDK User Manual needs Customer-Accessible Change Log / Revision History"
   "`EXT_SITMPUSW-146 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-146>`_","Yocto: meta-ti*: kernel source has uncommited changes"
   "`EXT_SITMPUSW-148 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-148>`_","Relocate Memory carveout for RTOS IPC"
   "`EXT_SITMPUSW-147 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-147>`_","Multichannel demo in EdgeAI gallery freezes on long run"
   "`EXT_SITMPUSW-149 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-149>`_","AM62A: Display starvation observed while running Semantic Segmentation usecase"
   "`EXT_SITMPUSW-140 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-140>`_","[AM62A]: Integrate existing solution meta-selinux solution into meta-edgeai"
   "`EXT_SITMPUSW-150 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-150>`_","Drop edgeai override for AM62A"
   "`EXT_SITMPUSW-152 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-152>`_","Heterogeneous-camera streaming with imx390 followed by ov2312 gets stalled."
   "`EXT_EP-12831 <https://sir.ext.ti.com/jira/browse/EXT_EP-12831>`_","Multichannel decoding of h264 video freezes on long run"
   "`EXT_EP-12832 <https://sir.ext.ti.com/jira/browse/EXT_EP-12832>`_","U-Boot: am62ax.env needs a fix while loading overlays"
   "`EXT_EP-12142 <https://sir.ext.ti.com/jira/browse/EXT_EP-12142>`_","Instabilities observed while resuming from IO Only plus DDR mode"
   "`EXT_EP-12063 <https://sir.ext.ti.com/jira/browse/EXT_EP-12063>`_","Update the DDR configuration with DDR syscfg 9.09+"
   "`EXT_EP-12111 <https://sir.ext.ti.com/jira/browse/EXT_EP-12111>`_","Linux SDK v10.0: TI-added support for W25N01JW SPI NAND breaks other existing Flash support"
   "`EXT_EP-12127 <https://sir.ext.ti.com/jira/browse/EXT_EP-12127>`_","Streaming with multiple cameras gets frozen in 2 minutes along with flickering images"
   "`EXT_EP-12112 <https://sir.ext.ti.com/jira/browse/EXT_EP-12112>`_","Add Timer PWM documentation and other infrastructure as needed"
   "`EXT_EP-12284 <https://sir.ext.ti.com/jira/browse/EXT_EP-12284>`_","Partial I/O not resuming from mcan"
   "`EXT_EP-12287 <https://sir.ext.ti.com/jira/browse/EXT_EP-12287>`_","lmbench: runLmDDRBandwidth.sh: bw_mem: command not found"
   "`EXT_EP-12291 <https://sir.ext.ti.com/jira/browse/EXT_EP-12291>`_","RPROC_DMABUF_ATTACH ioctl is not thread safe in ti-linux-6.12"
   "`EXT_EP-12295 <https://sir.ext.ti.com/jira/browse/EXT_EP-12295>`_","IO Only + DDR Resume Failure: platform 79000000.r5f: ti-sci processor set_config failed"
   "`EXT_EP-12342 <https://sir.ext.ti.com/jira/browse/EXT_EP-12342>`_","ETHERNET boot test fails"

Issues Open
-----------
.. csv-table::
   :header: "Record ID", "Title"
   :widths: 15, 70

   "`EXT_SITMPUSW-154 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-154>`_","MSC ROI function not creating the desired ROI"
   "`EXT_SITMPUSW-76 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-76>`_","Heterogeneous-camera streaming has high latency while streaming imx390+ov2312"
   "`EXT_EP-12792 <https://sir.ext.ti.com/jira/browse/EXT_EP-12792>`_","CSI-2 Rx driver shall support frame width that is not 16-byte-aligned"
   "`EXT_EP-12777 <https://sir.ext.ti.com/jira/browse/EXT_EP-12777>`_","OSPI XIP prefetch causes DMA transfer data corruption"
   "`EXT_SITMPUSW-144 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-144>`_","Multichannel EdgeAI pipeline - Multi Input Single Inference freezes on long run"
   "`EXT_SITMPUSW-151 <https://sir.ext.ti.com/jira/browse/EXT_SITMPUSW-154>`_","VPAC switching between WDR mode and linear mode causing wrong image color"
   "`EXT_EP-12747 <https://sir.ext.ti.com/jira/browse/EXT_EP-12747>`_","Codec: Wave5: Improve Decoder Performance and Fix SError Crash on Fluster test"
   "`EXT_EP-12787 <https://sir.ext.ti.com/jira/browse/EXT_EP-12787>`_","Multi channel decoding of h264 with high CPU load freezes on AM62A"
   "`EXT_EP-12785 <https://sir.ext.ti.com/jira/browse/EXT_EP-12785>`_","Cyclictest performance degradation on AM62x/AM64x/AM62A"
   "`EXT_EP-12043 <https://sir.ext.ti.com/jira/browse/EXT_EP-12043>`_","TPS6594: Error IRQ trap reach ilim, overcurrent for BUCK1/2 error"

