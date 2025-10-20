.. _release-specific-release-notes:

************************************
Release Notes
************************************
.. http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_Release_Notes

Overview
========

The **Processor Software Development Kit (Processor-SDK) for Linux**
provides a fundamental software platform for development, deployment and
execution of Linux based applications and includes the following:

-  Bootloaders & Filesystems
-  SDK Installer
-  Setup Scripts
-  Makefiles
-  Example Applications
-  WLAN support (Wilink 8)
-  Code Composer Studio

Licensing
=========

Please refer to the software manifest, which outlines the licensing
status for all packages included in this release. The manifest can be
found on the SDK download page. The manifest can be found on the SDK
download page or in the installed directory as indicated below. In
addition, see `GPLv3 Disclaimer <Overview_GPLv3_Disclaimer.html>`__

Documentation
===============
-  `Processor SDK Linux Software Developer's Guide <index.html>`__: Provides information on features, functions, delivery package and,
   compile tools for the Processor SDK Linux release. This also provides
   detailed information regarding software elements and software
   infrastructure to allow developers to start creating applications.
-  `Processor SDK Linux Getting Started Guide <Overview_Getting_Started_Guide.html>`__: Provides information on getting the software and running
   examples/demonstrations bundled in the SDK.
-  **Software Manifest**: Provides license information on software
   included in the SDK release. This document is in the release at
   ``[INSTALL-DIR]/docs``.
-  **EVM Quick Start Guide**: Provides information on hardware setup and
   running the demonstration application that is loaded on flash. This
   document is provided as part of the EVM kit.

Release 06.03.00
==================

Released April 2020

.. rubric:: What's New
   :name: whats-new

Processor SDK 6.3 Release has following new features:


- Analytics
    - TensorFlow Lite classification and segmentation demos with OpenCV
    - TensorFlow Lite heterogeneous execution with TIDL acceleration with EVE’s and DSP’s on AM5729 and AM5749 devices
    - sitara_am57x supported as AWS Sagemaker NEO target device

- ICSSM PRUETH
    -  Network storm prevention enhancements

- ICSSG PRUETH
    -  100M Uboot Support in ICSSG on AM654x


.. _release-specific-sdk-components-versions:

.. rubric:: SDK Components & Versions
   :name: sdk-components-versions

+--------------------------+----------------------------+
| Component                | Version                    |
+==========================+============================+
| Linux Kernel             | 4.19.94 (2019 LTS)         |
+--------------------------+----------------------------+
| U-Boot                   | 2019.01                    |
+--------------------------+----------------------------+
| Yocto Project            | 2.6 (thud)                 |
+--------------------------+----------------------------+
| ARM Toolchain (gcc)      | 8.3 2019.03 hard-float     |
+--------------------------+----------------------------+
| Qt                       | 5.11.3                     |
+--------------------------+----------------------------+
| OpenCL                   | 1.1.19                     |
+--------------------------+----------------------------+
| OpenCV                   | 3.1                        |
+--------------------------+----------------------------+
| Wayland                  | 1.16                       |
+--------------------------+----------------------------+
| GStreamer                | 1.14.4                     |
+--------------------------+----------------------------+
| TI PRU Compiler          | 2.2.1                      |
+--------------------------+----------------------------+
| TI C66x CGT Compiler     | 8.3.2                      |
+--------------------------+----------------------------+

|

Supported Platforms
=====================================
See :ref:`release-specific-supported-platforms-and-versions` for a list of supported platforms and links to more information.

|

.. _release-specific-build-information:

Build Information
=====================================

.. _u-boot-release-notes:

U-Boot
-------------------------

| The U-Boot git repository, branch and commit id can be found below:
| Based on verson: 2019.01
| URL: git.ti.com/processor-sdk/processor-sdk-u-boot.git
| Branch: processor-sdk-u-boot-2019.01
| Commit ID: 333c3e72d362c1fd1e5011e4e961c231b8f8edc8

|

.. _release-specific-build-information-kernel:

Kernel
-------------------------

.. _release-specific-build-information-linux-kernel:

.. rubric:: Linux Kernel
   :name: linux-kernel

| The kernel git repository, branch and commit id can be found below:
| Based on Version: 4.19.94
| URL: git://git.ti.com/processor-sdk/processor-sdk-linux.git
| Branch: processor-sdk-linux-4.19.y
| Commit ID: be5389fd85b69250aeb1ba477447879fb392152f

|

.. _release-specific-build-information-rt-linux-kernel:

.. rubric:: Real Time (RT) Linux Kernel
   :name: real-time-rt-linux-kernel

| The RT kernel git repository, branch and commit id can be found below:
| Based on:
| Kernel Version: 4.19.94
| RT Kernel Version: 4.19.94-rt39

| URL: git://git.ti.com/processor-sdk/processor-sdk-linux.git
| Branch: processor-sdk-linux-rt-4.19.y
| Commit ID: a242ccf3f13f03d41d521411ce2cc09775c873a2

|


.. _release-specific-generic-kernel-release-notes:

.. rubric:: Generic Kernel Release Notes
   :name: generic-kernel-release-notes

| Generic kernel release notes from kernelnewbies.org can be found at:
  http://kernelnewbies.org/Linux_4.19
| Archived versions can be found at:
  http://kernelnewbies.org/LinuxVersions

|

Issues Tracker
=====================================

Issues opened in previous releases that were closed on this release
---------------------------------------------------------------------

.. csv-table::
   :header: "Record ID", "Platform", "Title"
   :widths: 15, 30, 100

   PLSDK-1398,"k2e-evm,k2e-hsevm,k2h-hsevm,k2g-hsevm",Documentation IPC Demo hangs if run after OpenCL demos
   PLSDK-3143,"am335x-evm, am437x-evm, am437x-idk, am572x-evm, am572x-idk, am574x-idk",TVM inside PLSDK Linux devkit not working for code generation

|


Issues found and closed on this release that may be applicable to prior releases
-----------------------------------------------------------------------------------
.. csv-table::
   :header: "Record ID", "Platform", "Title"
   :widths: 15, 20, 70

   PLSDK-3157,"am654x-evm,am654x-idk,am654x-hsevm", ICSSG: Driver has to support changing of speed/duplex on the fly
   PLSDK-3067,"am574x-idk", M4 Bind/Unbind Causes Hang
   PLSDK-2642,"am574x-idk", PRU Ethernet links on IDK Application board are unstable

|

Errata Workarounds Available in this Release
------------------------------------------------
.. csv-table::
   :header: "Record ID",  "Title"
   :widths: 15, 80

   LCPD-5310,"i900: CTRL_CORE_MMR_LOCK_5 region after locking results in ctrl module inaccessible, recoverable only post a reset"
   LCPD-5311,i893: DCAN ram init issues in HW AUTO and when traffic hitting CAN bus (open investigation)
   LCPD-5309,   LCPD: i896: USB Port disable doesnt work
   LCPD-7642,MMC/SD: i832: return DLL to default reset state with CLK gated if not in SDR104/HS200 mode.
   LCPD-4195,J6: SATA: Investigate applicability of i807
   LCPD-4225,J6: Errata: i834: Investigate possibility of software workaround
   LCPD-976,J6/J6eco: 32clk is psuedo (erratum i856) - clock source
   LCPD-975,J6/J6eco: 32clk is psuedo (erratum i856) - realtime counter
   LCPD-1022,J6: Errata: i694: System I2C hang due to miss of Bus Clear support @ OMAP level
   LCPD-1188,J6: Baseport: Errata i877: RGMII clocks must be enabled to avoid IO timing degradation due to Assymetric Aging
   LCPD-9084,i887: Software workaround to limit mmc3 speed to 64MHz
   LCPD-16904,PCIe: Unsupported request (UR) or Configuration Request Retry Status (CRS) in configuration completion response packets results in external abort
   LCPD-5836,CAL: Errata: i913: CSI2 LDO needs to be disabled when module is powered on
   LCPD-5460,Implement WA for Vayu errata i829 (Reusing Pipe Connected To Writeback Pipeline On The Fly To An Active Panel)
   LCPD-5052,Upstream: Post the dmtimer errata fix for i874
   LCPD-4910,J6/OMAP5: errata i810 implementation
   LCPD-4911,DRA7: USB: Investigate applicability of Errata i897: StopEndpoint_issue
   LCPD-4912,DRA7: USB: Implement ErrataID_i896_PED_issue
   LCPD-16363,"IO, MMCSD: Incorrect IO Power Supply Connectivity Prevent Dynamic Voltage Change on VDDSHV6 and VDDSHV7"
   LCPD-16364,MMCSD: Negative Current from UHS-I PHY May Create an Over-Voltage Condition on VDDS6 and VDDS7 which exposes the Device to a Significant Reliability Risk
   LCPD-16538,PCI-Express (PCIe) May Corrupt Inbound Data
   LCPD-14184,USB: SuperSpeed USB Non-Functional
   LCPD-14187,UDMA-P Real-time Remote Peer Registers not Functional Across UDMA-P Domains
   LCPD-14185,MSMC: Non-coherent memory access to coherent memory can cause invalidation of snoop filter
   LCPD-14159,The assertion of warm reset coinciding with a debug configuration access targeting the STM Subsystem may result in a hang of said debug configuration access
   LCPD-13884,CPTracer Bus Probes MAIN_CAL0_0 and MCU_SRAM_SLV_1 are not able to distinguish between secure and non-secure transactions
   LCPD-13887,DDR Controller ECC Scrubbing feature can cause DRAM data corruption
   LCPD-4647,[rpmsg 2015 LTS] Implement errata i879 - DSP MStandby requires CD_EMU in SW_WKUP
   LCPD-4648,[rpmsg 2014 LTS] Implement errata i879 - DSP MStandby requires CD_EMU in SW_WKUP
   LCPD-4975,DSS AM5/DRA7: implement WA for errata i886
   LCPD-14941,RINGACC and UDMA ring state interoperability issue after channel teardown
   LCPD-14579,DSS : DSS Does Not Support YUV Pixel Data Formats
   LCPD-14580,DSS : DSS Does Not Support YUV Pixel Data Formats
   LCPD-14578,DSS : DSS DPI Interface does not support BT.656 and BT.1120 output modes
   LCPD-14577,CPSW does not support CPPI receive checksum (Host to Ethernet) offload feature
   LCPD-8277,u-boot: j6: SATA is not shutdown correctly as per errata i818
   LCPD-8294,37 pins + VOUT pins need slow slew enabled for timing and reliability respectively
   LCPD-5308,i897: USB Stop Endpoint doesnt work in certain circumstances
   LCPD-6907,Workaround errata i880 for RGMII2 is missing
   LCPD-5931,DRA7xx: AM57xx: mmc: upstream errata workaround for i834
   LCPD-5924,ALL: CONNECTIVITY: CPSW: errata i877 workarround for cpsw
   LCPD-4218,Implement Workaround for Errata i813 - Spurious Thermal Alert Generation When Temperature Remains in Expected Range
   LCPD-4217,Implement Workaround for Errata i814 - Bandgap Temperature read Dtemp can be corrupted
   LCPD-4184,Implement workaround for errata i814 - Bandgap Temperature read Dtemp can be corrupted
   LCPD-1146,DMM hang: Errata VAYU-BUG02976 (i878) (register part)
   LCPD-1087,J6: MMC: Errata: i802: OMAP5430 MMCHS: DCRC errors during tuning procedure
   LCPD-1108,J6: Wrong Access In 1D Burst For YUV4:2:0-NV12 Format (Errata i631)
   LCPD-876,OMAP5: Errata i810: DPLL Controller Sticks when left clock requests are removed
   LCPD-16605,MMC: MMC1/2 Speed Issue
   LCPD-17220,U-Boot Hyperbus: Hyperflash reads limited to 125MHz max. frequency
   LCPD-16643,Hyperbus: Hyperflash reads limited to 125MHz max. frequency
   LCPD-16350,DSS: Frame Buffer Flip/Mirror Feature Using RGB24/BGR24 Packed Format can Result in Pixel Corruption
   LCPD-9173,i897: USB Stop Endpoint doesnt work in certain circumstances
   LCPD-17333,[CPTS] GENF (and ESTF) Reconfiguration Issue
   LCPD-14186,UDMA-P Host Packet Descriptors 0x3FFFFF Packet Length Mode not Functional
   LCPD-1776,"[J6 SATA Adaptation] J6 - Errata i783, SATA Lockup After SATA DPLL Unlock/Relock"
   LCPD-941,"OMAP4,5: DSS: implement workaround for errata i740"
   LCPD-1171,DRA7: DMM errata i878 (framebuffer part)


|

SDK Known Issues
-----------------
.. csv-table::
   :header: "Record ID", "Platform", "Title", "Workaround"
   :widths: 25, 30, 50, 600

   LCPD-15810,"am335x-evm, am43xx-gpevm, k2g-evm",Illegal instruction reported when trying to decode h264 stream with gstreamer,None
   PLSDK-1398,"k2e-evm, k2e-hsevm, k2g-hsevm, k2hk-hsevm",IPC demo hangs if run after OpenCL demos,Run IPC demo w/o running OpenCL first
   PLSDK-1419,k2l-evm,Intermittent-IP address display issue on LCD for K2L RT,"Use ifconfig once Linux boots, to acquire IP address"
   PLSDK-2178,"am335x-ice, am437x-idk, am574x-idk",ICSS EMAC intermittent error in received acyclic packet content,None
   PLSDK-2466,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, k2g-ice",Fix Race condition in updating NSP credit value,None
   PLSDK-2530,"am335x-ice, am437x-idk",AM3/4 PTP PPS fails intermittently,No complete workaround. Restarting the ethernet interface should reset PPS and likely resolve the issue temporarily.
   PLSDK-2642,am654x-idk,PRU Ethernet links on IDK Application board are unstable,"IDK Limitation, requires re-work"
   PLSDK-2662,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk, k2g-ice",HSR/PRP: Bringing down one slave port stops HSR/PRP interface,None
   PLSDK-2861,"k2e-evm, k2g-evm, k2hk-evm, k2l-evm",Crypto is not functional on 2019 LTS,None
   PLSDK-2873,k2g-ice,K2G-ICE kernel warnings when removing PRUETH module,None
   PLSDK-2895,am571x-idk,AM571x-IDK: Icss Emac: TTS Port 1: Packet cyclic timestamp error.,None
   PLSDK-2896,"k2e-evm, k2e-hsevm, k2hk-evm",mpm_transport_hyperlink_loopback: transport arm-loopback-hyplnk-0 failed (error: -114) retval -1001,No workaround
   PLSDK-2900,"am335x-evm, am437x-evm, k2e-evm, k2g-evm, k2hk-evm, k2l-evm","crypto examples are skipped from toplevel SDK Makefile, due to OpenSSL dependency",No workaround
   PLSDK-2913,am572x-idk,NetJury Test Failure: TC_PRP_4_3_4_____Reception_of_a_PRP_Supervision_frame_and_Nodes_Table - test_VLAN,No workaround
   PLSDK-2936,am572x-evm,jailhouse: failed in destroy cell,None
   PLSDK-2937,am572x-evm,jailhouse: ti-app demo doesn't start,None
   PLSDK-2960,am571x-idk,HSR/PRP: Noticed 1 packet loss seen with UDP tests over 60 minute test,None
   PLSDK-2989,"am335x-evm, am437x-evm, am437x-hsevm, am572x-evm, am572x-hsevm, k2e-evm, k2g-evm, k2l-evm, k2l-hsevm",defconfig build failure: reported diff,
   PLSDK-3031,"am571x-idk, am572x-idk, am574x-idk",HSR: erroneous A-B forwarding of frames,
   PLSDK-3032,"am571x-idk, am572x-idk, am574x-idk","HSR: forwarding of untagged frames in default mode H not according to IEC 62439-3:2016, 5.3.3 DANH receiving from an HSR port.",None
   PLSDK-3057,"am335x-evm, am437x-evm, am572x-evm, am654x-evm, am654x-idk",ARMNN with TFLite parser: performance/accuracy issue with quantized mobilenet models,Patch from arm compute library https://review.mlplatform.org/c/ml/ComputeLibrary/+/1620/.
   PLSDK-3071,"am571x-idk, am572x-evm, am572x-idk, am574x-idk",Dual camera demo: Overlapping of camera and stats panel due to big font size,None
   PLSDK-3074,am572x-idk,NetJury Test Failure: TC_PRP_4_2_4_____IP_addresses,None
   PLSDK-3086,"am571x-idk, am572x-idk",Unable to handle kernel NULL pointer dereference when disabling HSR,None
   PLSDK-3089,"am572x-evm, k2l-evm",openmpacc example test failed on am572x-evm and k2l-evm,
   PLSDK-3091,am572x-idk,Jailhouse: ICSS_EMAC_LLD test hangs during TTS tests on ICSS_EMAC_TEST_PRU2ETH0 and ICSS_EMAC_TEST_PRU2ETH1,
   PLSDK-3125,"am571x-idk, am572x-idk, am574x-idk",clean up timestamp queue when extts is disabled,
   PLSDK-3128,"am572x-evm, am572x-hsevm, am572x-idk, am574x-hsidk, am574x-idk",SDK disk image for Windows users too large for 16GB SD card,
   PLSDK-3138,,EtherCAT in Jailhouse inmate: instruction abort at 0x80013f00,
   PLSDK-3147,am654x-idk,ICSSG: < 0.01 packet loss at 3/4/4.5 Mbits/sec for 10M Half Duplex link,
   PLSDK-3148,am654x-idk,ICSSG: 10M/100M Half duplex doesn't work with 10/100M Hub,
   PLSDK-3152,am654x-idk,10M/100M EVM <-------> PC / H3C S5120V2: setup results in kernel errors and ping failures,
   PLSDK-3171,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk, k2g-ice",DualEMAC PTP IPv4/UDP transport does not support VLAN,
   PLSDK-3172,"am335x-ice, am437x-idk, am571x-idk, am572x-idk, am574x-idk, k2g-ice",DualEMAC PTP IPv4/UDP transport does not drop SYNC messages from unknown PTP masters,
   PLSDK-3179,"am572x-idk",OpenCV_stereoBM_implementation test failed on am5729-idk,
   PLSDK-3182,"am571x-idk",RSTP switch PRU ethernet driver should use 4 tx queues instead of 2,
   PLSDK-3183,"am571x-idk",RSTP switch PRU ethernet driver should purge FDB only when going in or out of blocking state,
   PLSDK-3184,"am571x-idk",RSTP switch PRU ethernet driver should age out dynamically learned FDB,
   PLSDK-3185,"am571x-idk",RSTP switch PRU ethernet driver multicast filtering is not working,
   PLSDK-3191,"am335x-ice",icss-m: prueth: AM335x Single EMAC broken,
   PLSDK-3213,"am654x-idk",DP83867: auto negotiation at 10M/100M unstable,
   PLSDK-3215,"omapl138-lcdk",Windows SD card creation does not result in bootable binary,
   PLSDK-3219,"am571x-idk,am572x-idk,am574x-idk",Invalid PTP message type warnings,
   PLSDK-3219,"am571x-idk,am572x-idk,am574x-idk",Invalid PTP message type warnings,
   PLSDK-3220,"am572x-evm,am572x-idk", Neo-AI DLR TIDL demo image preprocssing incorrectly indexing pixels,
   PLSDK-3225,"am654x-evm", bin/create-ubifs.sh not available in SDK,
   PLSDK-3232,"am654x-evm", UDP throughput numbers are half of what they should be,
   PLSDK-3238,"am335x-evm,am437x-evm", Docker hello world test failure on am335x-evm/am437x-evm/dra76x-evm,
   PLSDK-3240,"am571x-idk,am572x-idk,am574x-idk", RSTP prueth: cable removal can cause instability on disabled Ethernet port,
   PLSDK-3241,"am571x-idk,am572x-idk,am574x-idk", RSTP_SWITCH_FW: Re-calculate timeout value for PRU-side locking,

|

.. _release-specific-u-boot-known-issues:

U-Boot Known Issues
------------------------
.. csv-table::
   :header: "Record ID","Platform", "Title","Workaround"
   :widths: 15, 30, 70, 30

   LCPD-16524,"am654x-evm, am654x-idk, am654x-hsevm",Need to adjust RMW bit when using enabling ECC,None
   LCPD-16103,am654x-evm,AM6: MMC: Probe fail warning in bootloader,None
   LCPD-15873,am654x-evm,There is no dtbo in u-boot for PCIe x1 + usb3 daughter card,None
   LCPD-15127,am654x-evm,u-boot: net: Stop called even without start leading to crash,None
   LCPD-15054,"am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-beagle-x15, am57xx-hsevm",[u-boot] AM57xx phy_ctrl structures must be board-specific,None
   LCPD-14843,"am654x-evm, am654x-idk",U-boot should support default settings for netboot,None
   LCPD-14638,"k2g-evm, k2g-ice",Invalid DDR_PHY_MR2 setting in K2G board library,None
   LCPD-10726,"am572x-idk, am57xx-evm",Update DDR3 emif regs structure for EMIF2 for the beagle_x15 board in U-Boot board file,None
   LCPD-10668,k2g-evm,Ethernet boot: Sometimes the board could not boot uboot from Ethernet on k2g-evm,None
   LCPD-7366,am335x-evm,uboot McSPI driver drives multiple chip selects simultaneously,None


|

.. _release-specific-linux-kernel-known-issues:

Linux Kernel Known Issues
---------------------------
.. csv-table::
   :header: "Record ID", "Priority", "Title", "Component", "Subcomponent", "Platform", "Workaround", "Impact"
   :widths: 5, 10, 70, 10, 5, 20, 35, 20

   LCPD-16877,P3-Medium,ti-ipc-examples-linux intermittent build failure,"IPC, System Integration",,k2hk-evm,,
   LCPD-16534,P3-Medium,remoteproc/k3-r5f: PDK IPC echo_test image fails to do IPC in remoteproc mode on second run,IPC,Firmware,"am654x-evm, am654x-idk",None,
   LCPD-17529,P3-Medium,Could not access usbhost when booting from SD card,Connectivity,,am43xx-gpevm,,
   LCPD-17441,P3-Medium,TI_CPSW Module cannot be removed and reinserted,Connectivity,,am57xx-evm,,
   LCPD-17329,P3-Medium,K2E RT-Linux USB fails when using USB-Ethernet dongle to scp file (512MB),Connectivity,USB,k2e-evm,,
   LCPD-17118,P3-Medium,Kernel MMC/SD user's guide incorrectly refers to OMAP-HSMMC,Connectivity,MMCSD,"am57xx-evm, dra7xx-evm",None,
   LCPD-16590,P3-Medium,am335x: usb bus power lost after system suspend resume,Connectivity,usb,"am335x-evm, am335x-sk, beaglebone-black",,
   LCPD-16406,P3-Medium,"Seeing ""e1000#0: ERROR: Hardware Initialization Failed"" sometimes when do dhcp via pcie-eth",Connectivity,,am654x-idk,,
   LCPD-16029,P3-Medium,AM65: icssg: PRU ethernet links might be unstable with new PHY package,Connectivity,PRUSS-Ethernet,"am654x-evm, am654x-idk, am654x-hsevm",,
   LCPD-15952,P3-Medium,DCAN Documentation incorrect,Connectivity,,am335x-evm,None,
   LCPD-15885,P3-Medium,Uboot usb start trigger the board resetting with one usb stick,Connectivity,,k2hk-evm,,
   LCPD-15787,P3-Medium,Power suspend fails due to USB (scsi_bus_suspend) failure when HDD is in use,Connectivity,,am335x-evm,,
   LCPD-15737,P3-Medium,AM65x: MMC OTAPDLY values must match values in the Data Manual,Connectivity,MMCSD,"am654x-evm, am654x-idk",,
   LCPD-15660,P3-Medium,pcie sata or usb drive no device node being created,Connectivity,,k2g-evm,,
   LCPD-15649,P3-Medium,Uboot: sata could not be detected,Connectivity,,am57xx-evm,,
   LCPD-15540,P3-Medium,uvc-gadget results in segmentation fault,Connectivity,,"am57xx-evm, am654x-evm, dra71x-evm, dra7xx-evm",,
   LCPD-15515,P3-Medium,PCI: Endpoint: MSIX interrupts do not work on AM654,Connectivity,PCIe,am654x-evm,,
   LCPD-15405,P3-Medium,DFU: could not update eMMC bootloaders when using dfu_alt_info_emmc set in uboot env,Connectivity,,"am57xx-evm, dra71x-evm, dra7xx-evm",,
   LCPD-15365,P3-Medium,warning dump in fs/nfs/inode.c seen sometimes,Connectivity,CPSW,am654x-evm,,
   LCPD-14855,P3-Medium,omap_i2c_prepare_recovery() function can Lock System,Connectivity,I2C,"am335x-evm, am335x-ice, am335x-sk",,
   LCPD-14842,P3-Medium,musb: unplug usb-serial device cause console lockup,Connectivity,USB,"am335x-evm, am335x-sk, beaglebone-black",,
   LCPD-14511,P3-Medium,AM65x: Soft reset fails when booting from eMMC,Connectivity,MMCSD,"am654x-evm, am654x-idk",,
   LCPD-14497,P3-Medium,PCIe Gen3 problems on AM654x,Connectivity,,"am654x-evm, am654x-idk",,
   LCPD-14460,P3-Medium,am654x-idk failed to boot to kernel prompt occasionally,Connectivity,,am654x-idk,,
   LCPD-14171,P3-Medium,Failed to read uboot from SD card 1/1000 times,Connectivity,,"am57xx-evm, dra7xx-evm",,
   LCPD-13936,P3-Medium,Uboot dhcp timeout 1 of 100 times,Connectivity,,am654x-evm,,
   LCPD-13720,P3-Medium,SPI DMA TX Mode Halts During Continuous 16/32/64 bit Transfers,Connectivity,,beaglebone-black,,
   LCPD-13452,P3-Medium,USB Gadget Camera Capture - guvcview causes kernel oops,Connectivity,,k2g-evm,,
   LCPD-13445,P3-Medium,Seldom kernel oops triggered by prueth_netdev_init,Connectivity,,am654x-evm,,
   LCPD-11952,P3-Medium,AM57x: disabling USB super-speed phy in DT causes kernel crash,Connectivity,USB,"am571x-idk, dra72x-evm",,
   LCPD-11564,P3-Medium,AM57xx-evm: eth1 1G connection failure to netgear switch,Connectivity,"CPSW, ETHERNET, PHYIF",am57xx-evm,,
   LCPD-10974,P3-Medium,am43xx-gpevm - usb camera gadget shows halting frames,Connectivity,USB,am43xx-gpevm,None,
   LCPD-9905,P3-Medium,AM437x: UART: Implement workaround for Advisory 27 - Spurious UART interrupts when using EDMA,Connectivity,UART,am43xx-gpevm,,
   LCPD-9366,P3-Medium,PCIe USB drive sometimes could not be enumerated,Connectivity,PCIe,k2g-evm,,
   LCPD-7623,P3-Medium,Seeing SPI transfer failed error sometimes on k2hk when using rt kernel,Connectivity,SPI,k2hk-evm,,
   LCPD-1106,P3-Medium,Connectivity:PCIe-SATA ext2 1G write performance is poor due to ata failed command,Connectivity,PCIe,"am57xx-evm, dra71x-evm, dra71x-hsevm, dra72x-evm, dra72x-hsevm, dra7xx-evm, dra7xx-hsevm",None,
   LCPD-17673,P3-Medium,No software documentation for the Timer module,Baseport,Timers,"am335x-evm, am43xx-gpevm, am571x-idk, am572x-idk, am574x-idk, am57xx-evm, am654x-evm, beaglebone-black, dra71x-evm, dra72x-evm, dra7xx-evm, j721e-evm",,
   LCPD-17422,P3-Medium,Disabling IRQ #64 message observed sometimes,Baseport,,"am654x-evm, am654x-hsevm",,
   LCPD-16845,P3-Medium,OPP freq update in DT impacts only cluster0,Baseport,,"am654x-evm, am654x-idk",,
   LCPD-14191,P3-Medium,IPSec hardware-based throughput is 30% lower than 2018.03,Baseport,,"am335x-evm, am57xx-evm",,
   LCPD-16642,P3-Medium,"omapdrm: in some cases, DPI output width does not need to be divisible by 8",Audio & Display,Display,"am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-beagle-x15, am57xx-hsevm, dra71x-evm, dra71x-hsevm, dra72x-evm, dra72x-hsevm, dra76x-evm, dra76x-hsevm, dra7xx-evm, dra7xx-hsevm",,
   LCPD-15819,P3-Medium,"tidss: the driver should reject dual-display setup, as it is not supported",Audio & Display,Display,am654x-evm,,
   LCPD-15518,P3-Medium,omapdrm: WB M2M: Headless mode is not working,Audio & Display,Writeback,"am571x-idk, am572x-idk, am574x-idk, am574x-hsidk, am57xx-evm, am57xx-beagle-x15, am57xx-hsevm, dra71x-evm, dra71x-hsevm, dra72x-evm, dra72x-hsevm, dra76x-evm, dra76x-hsevm, dra7xx-evm, dra7xx-hsevm",,
   LCPD-15402,P4-Low,rpmsg-rpc: test application does not bail out gracefully upon error recovery,IPC,"DSP_remoteproc, IPU_remoteproc","am571x-idk, am572x-idk, am574x-idk, am57xx-evm, am57xx-beagle-x15, dra71x-evm, dra72x-evm, dra76x-evm, dra7xx-evm",,
   LCPD-15400,P4-Low,remoteproc/omap: System suspend fails for IPU1 domain without any remoteprocs loaded,IPC,IPU_remoteproc,"am571x-idk, am572x-idk, am574x-idk, am57xx-evm, am57xx-beagle-x15, dra71x-evm, dra72x-evm, dra76x-evm, dra7xx-evm",,
   LCPD-10455,P4-Low,remoteproc/keystone: Hang observed while running RPMSG_PROTO example app,IPC,DSP_remoteproc,"k2g-evm, k2g-ice, k2hk-evm, k2l-evm",,
   LCPD-9481,P4-Low,Sometime the system hangs while loading the rpmsg rpc modules,IPC,RPMSG-RPC,"am571x-idk, am572x-idk, am57xx-evm, am57xx-hsevm",,
   LCPD-7495,P4-Low,Sometimes a Kernel Warning + Oops is seen when removing keystone_remoteproc module,IPC,,k2hk-evm,,
   LCPD-4855,P4-Low,[rpmsg 2015 LTS] J6Eco: IPC: Board hangs when an MMU fault occurs in the first message,IPC,,"am572x-idk, dra72x-evm",,
   LCPD-4699,P4-Low,[rpmsg 2015 LTS] rpmsg-rpc: kernel crash during error recovery with dynamic debug traces enabled,IPC,,"am571x-idk, am572x-idk, am57xx-evm, dra72x-evm, dra7xx-evm",,
   LCPD-17116,P4-Low,AM335x rmii2_crs_dv is not being muxed in due to SMA rmii2_crs_dv_sel not set,Connectivity,,am335x-evm,,
   LCPD-16437,P4-Low,Nand with prefetch dma: read perf drop ~20% comparing to 2018,Connectivity,,am335x-evm,,
   LCPD-15648,P4-Low,Uboot mmc performance decreased,Connectivity,,am335x-evm,,
   LCPD-12783,P4-Low,Missing instruction for pcie-ep config on k2g-evm for 4.19 kernel,Connectivity,,k2g-evm,,
   LCPD-12392,P4-Low,USBhost video: higher resolution tests fail with some cameras,Connectivity,,am335x-evm,,
   LCPD-6075,P4-Low,BUG: using smp_processor_id() in preemptible [00000000] code during remoteproc suspend/resume,"Baseport, IPC",,"am572x-idk, am57xx-evm, dra7xx-evm",,
   LCPD-9098,P4-Low,Writeback: error prints seen when doing wb capture,Audio & Display,"Capture, Display, Writeback","am571x-idk, am572x-idk, am57xx-evm, dra71x-evm, dra71x-hsevm, dra72x-evm, dra72x-hsevm, dra7xx-evm, dra7xx-hsevm",,


|

.. _release-specific-rt-linux-kernel-known-issues:

RT Linux Kernel Known Issues
-----------------------------

.. csv-table::
   :header: "Record ID", "Priority", "Title", "Component", "Platform", "Workaround"
   :widths: 5, 10, 70, 10, 20, 15

   LCPD-6663 ,P3-Medium ,[RT] Kmemleak is buggy and boot is crashed randomly ,Baseport ,  ,
   LCPD-7623 ,P3-Medium ,Seeing SPI transfer failed error sometimes on k2hk when using rt kernel ,Connectivity ,k2hk-evm ,
   LCPD-11586 ,P3-Medium ,dhcp failed to get IP address after reboot for K2G-ICE non-RT linux ,Baseport  ,"k2g-ice ",

|


.. rubric:: Installation and Usage
   :name: installation-and-usage

The `Software Developer's Guide <index.html>`__ provides instructions on how to setup up your Linux development
environment, install the SDK and start your development.  It also includes User's Guides for various Example Applications and Code
Composer Studio.

|

.. rubric:: Host Support
   :name: host-support

The Processor SDK is developed, built and verified on Ubuntu 16.04 and 18.04. Details on how to create a virtual machine to load Ubuntu
are described in `this page <How_to_Guides/Host/How_to_Build_a_Ubuntu_Linux_host_under_VMware.html>`__.


.. note::
   Processor SDK Installer is 64-bit, and installs only on 64-bit host
   machine. Support for 32-bit host is dropped as Linaro toolchain is
   available only for 64-bit machines

|
