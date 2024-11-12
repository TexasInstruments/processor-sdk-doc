.. http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_Migration_Guide

.. _release-specific-migration-guide:

************************************
Migration Guide for AM335X
************************************

.. rubric:: Overview

This page covers migration information for applications built on top
of the Processor SDK for Linux.

As of Oct 2023, Linux SDK for AM335x is in long term maintenance mode. TI will support critical bug fixes and once a year LTS updates but no new development or new features are planned for this device SDK at this time.

Processor SDK 09.xx Releases
============================

Processor SDK 09.01.00
-----------------------
- 2023 LTS Update release, with new versions of Kernel and U-boot. Please see :ref:`release-specific-sdk-components-versions`.

Processor SDK 08.xx Releases
============================

Processor SDK 08.02.00
-----------------------
- 2021 LTS Update release, with new versions of Kernel and U-boot. Please see :ref:`release-specific-sdk-components-versions`.

Processor SDK 07.xx Releases
============================

Processor SDK 07.03.00
-----------------------
- 2020 LTS Update release, with new versions of Kernel, U-boot, toolchain and Yocto. Please see :ref:`release-specific-sdk-components-versions`.
- Linux HSR, PRP driver. The source directory is now net/hsr instead of
  net/hsr-prp and all source files are prefixed as originally with hsr
  prefix instead of hsr_prp. Consequently CONFIG_HSR_PRP is changed to
  CONFIG_HSR as well.
- ip link command for prp interface creation is changed to use type hsr
  and a new proto parameter with a value of 1 for prp and 0 for hsr.
- PRUETH Driver uses NAPI vs irq thread based processing in older release.
  User is expected to issue a chrt command and raise priority of softirq
  daemon to avoid packet loss.
- The boot parameters for Ethernet type is now removed. User is expected
  to switch to HSR/PRP/Switch following instructions from user guide.
- Network Storm Prevention now uses tc filter command instead of sysfs file
  as documented in the User guide.
- VLAN/MC filter dump now uses switch-config instead of debugfs.
- Tx IRQ is removed for PRUETH EMAC driver because testing showed that
  performance for small size frames is better with IRQ not used. For
  MTU frames, Tx IRQ provides better performance. User may add DT entry
  for Tx IRQ to enable this if the use case is predominantly using MTU
  size frames to take advantage of this. See
  Documentation/devicetree/bindings/net/ti-prueth.txt
  for details on DT changes needed to use Tx IRQ.
- PRP Emac mode is obsolete and not supported anymore.
- HSR/PRP with PRU-ICSS firmware offload is not supported.
- ICSS-EMAC is not supported.
- SORTE is not supported.

Processor SDK 06.xx Releases
============================

Processor SDK 06.03
--------------------
- This is a quarterly update release on 2019 LTS stream and final release on that stream.
- ICSSM PRUETH: Network storm prevention enhancements. Please check 4.2.4.7 Network Storm Prevention section of user guide, for changes in user interface for configuring storm prevention.

Processor SDK 06.02
---------------------
- This is a quarterly update release on 2019 LTS stream.
- Note that this version of Processor SDK updates only AM5 and AM6 platforms w/ Linux OS.
- The SGX driver has been enhanced to replace IMG WSEGL with MESA-EGL which supports the essential EGL 1.5 extensions required by the latest versions of certain graphics applications such as Chromium browser. See :ref:`here <from-processor-sdk-6-1-to-6-2-for-am3-4-5-6>` for more details about compatability.

Processor SDK 06.01
---------------------
- This is a quarterly update release on 2019 LTS stream.
- EMAC firmware
  - PRP Firmware in EMAC mode can be obsolete, as EMAC firmware has been made to be feature parity for SAN

Processor SDK 06.00
----------------------
- This is the first release in 2019 LTS stream, with new versions of Kernel, U-boot, toolchain and Yocto branch. Please see :ref:`release-specific-sdk-components-versions`.
- Toplevel Makefile: There are additional packages required on the host, such as flex, bison and libssl-dev, for the top-level Makefile to build successfully. You can find the complete list of required host packages in `this chapter <../../../linux/Overview/Top_Level_Makefile.html>`__
- Resistive Touchscreen TSCADC (resistive touchscreen) wakeup control on AM335x and AM437x has moved from TSCADC MFD device node to TSC input device node.
   - Disable touchscreen as wakeup source use: echo disabled > /sys/devices/platform/ocp/44e0d000.tscadc/TI-am335x-tsc.0.auto/power/wakeup
   - Enable touchscreen as wakeup source use: echo enabled > /sys/devices/platform/ocp/44e0d000.tscadc/TI-am335x-tsc.0.auto/power/wakeup
- IPC
   - Remoteproc core
      - Error recovery with virtio-rpmsg-bus stack is broken on Upstream vanilla 4.19 kernel. Error recovery is supported only on TI kernels.
   - PRUSS remoteproc
      - The PRUSS remoteproc bindings and drivers have been split up into three separate folders
      - New bindings are defined in soc/ti/ti,pruss.txt, interrupt-controller/ti,pruss-intc.txt and remoteproc/ti,pru-rproc.txt under the Documentation/devicetree/bindings folder and replaces remoteproc/ti,pruss-remoteproc.txt
      - PRUSS INTC module pruss_intc.ko is now irq-pruss-intc.ko and is built in drivers/irqchip folder
      - pruss_soc_bus and pruss platform drivers are now built in drivers/soc/ti folder.
   - Userspace
      - New IPC and CMEM releases are needed to use with 4.19 kernel due to difference in AF_RPMSG family number and other kernel API changes. Minimum required versions are IPC 3.50.03.05 and CMEM 4.16.00.00

- PRUETH
   - On AM571x IDK boards, the naming of the PRUETH supported ethernet ports has changed. In previous releases, PRU-ICSS1 (J3, J5 on IDK) corresponded to eth4/5, and PRU-ICSS2 (J6, J8 on IDK) corresponded to eth2/3. As of 06.00, this has swapped, and now PRU-ICSS1 corresponds to eth2/3, and PRU-ICSS2 corresponds to eth4/5.

- Jailhouse AM57xx support rebased to v0.10 version
   - Added shared memory region between Linux, hypervisor, and inmate console
   - Startup code of the inmate library enables MMU. An inmate has to initialize its MMU table by itself.



Processor SDK 05.xx Releases
============================

Processor SDK 05.03
----------------------

- This release is backwards compatible with 05.02 release.


Processor SDK 05.02
----------------------

- The minimum SD card size is now 16GB when creating an SD card with the default images for Processor SDK Linux.

.. rubric:: Multicast Filtering Mask

* The parameter for setting a multicast filtering mask is now 'pruss<ID>_port<PORT>_mc_mask' instead of 'pruss<ID>_mc_mask' because support was added to enable per port multicast filtering for Dual EMAC.

.. rubric:: ip link command

* ip link parameter for setting up VLAN tag for HSR/PRP, sv_cfi is renamed to sv_dei.

Processor SDK 05.01
----------------------

- Introduced AM65x as a new platform. Please refer to release notes for more details

.. rubric:: PRUETH Driver

**1. debugfs file path has changed**

The path for debugfs file has changed to include the PRU-ICSS ID as there could be upto two instances of offloaded hsr/prp prueth driver and so has to distictly identify which instance the debugfs file refers to.

For example, the path for hsr/prp changed from

- /sys/kernel/debug/prueth-<hsr/prp>/

 to

- /sys/kernel/debug/prueth-<hsr/prp>-<ID>/

Where ID is the PRU-ICSS ID as described in the HSR/PRP User Guide.

- For HSR on PRU-ICSS2 of AM571x, path is changed to /sys/kernel/debug/prueth-hsr-2/
- For HSR on PRU-ICSS1 of AM571x, path is changed to /sys/kernel/debug/prueth-hsr-1/
- For PRP on PRU-ICSS2 of AM571x, path is changed /sys/kernel/debug/prueth-prp-2/
- for PRP on PRU-ICSS1 of AM571x, path is changed to /sys/kernel/debug/prueth-prp-1/

All of the existing debugfs files except prp_emac_mode have moved to the new location. prp_emac_mode is now changed to sysfs file as decribed in the below section.  The files are not writeable anymore as it is meant only for showing debug information. The write functions are moved to the upper layer HSR/PRP driver and implemented though proc entries. See the Linux HSR/PRP driver section for more details.

**2. sysfs file path has changed**

The path for sysfs files have also changed from

- /sys/devices/platform/pruss<ID>_eth/eth2/

 to

- /sys/devices/platform/pruss<ID>_eth/net/eth2/

Where ID is the PRU-ICSS ID as described in the User Guide.

For example, nsp_credit sysfs file is now accessed at

 /sys/devices/platform/pruss2_eth/net/eth2/nsp_credit

prp_emac_mode file is at

 /sys/devices/platform/pruss2_eth/net/eth2/prp_emac_mode

.. rubric:: Linux HSR/PRP Driver

**1. debugfs file path has changed**

The debugfs file directory created by the driver now uses the interface name so that multiple
instances of the device can co-exist and each will have its own unique path names.

Path is now changed from

- /sys/kernel/debug/<hsr/prp>/

 to

- /sys/kernel/debug/<if_name>/

For example, if hsr interface name is hsr0, the path will be
- /sys/kernel/debug/hsr0/

Write functions are now supported through proc entries. So similar functions are removed from debugfs.
See below section for details of proc entries.
stats file is renamed to lre_info which shows SV frame tx count along with additional debug information
about the LRE.

**2. proc file paths**

Following commands can be used for updating values at the prueth offloaded device which was earlier
supported through debugfs files at the prueth device.

- /proc/<if_name>/clear-nt - Replaces /sys/kernel/debug/prueth-<hsr/prp>/node_table_clear
- /proc/<if_name>/hsr-mode - Replaces /sys/kernel/debug/prueth-<hsr/prp>/hsr_mode
- /proc/<if_name>/dlrmt - Replaces /sys/kernel/debug/prueth-<hsr/prp>/dup_list_reside_max_time
- /proc/<if_name>/dd-mode  - Replaces /sys/kernel/debug/prueth-<hsr/prp>/duplicate_discard
- /proc/<if_name>/prp-tr - Replaces  /sys/kernel/debug/prueth/transparent_reception


Processor SDK 05.00
---------------------
- This is the first release for 2018 LTS (Kernel: 4.14, U-boot: 2018.01, gcc: 7.2.1 and Yocto: 2.4 (rocko)).
- With Yocto migration, several open source components (Qt, Wayland, Weston, GStreamer, iPerf, etc.) are all upgraded. For the exact versions of the new components, please refer to the
  Software Manifest., and for any migration issues, refer to the corresponding component's release notes, and Processor SDK Known Issues list.
- Following are major compatability changes for TI drivers, components.
- IPC
   - Remoteproc core
        - RPMSG_VIRTIO is no longer automatically selected by remoteproc platform drivers, has to be enabled specifically in defconfigs
        - The RSC_CUSTOM remoteproc custom resource type has been replaced with two new RSC_PRELOAD_VENDOR and RSC_POSTLOAD_VENDOR resource types.
        - Two new debugfs variables "resource_table" and "carveout_memories" are added to print the resource table and carveout memories used by a remoteproc
        - Error recovery with virtio-rpmsg-bus stack is broken on Upstream vanilla 4.14 kernel. Error recovery is supported only on TI kernels.
   - PRUSS remoteproc
        - The PRUSS remoteproc bindings have been revised significantly to improve scalability and flexibility
             - New child nodes are added to represent the CFG, IEP and MII_RT sub-modules.
             - Default firmware names are moved from driver to DT
             - Client users will require a new "prus" mandatory property instead of the previous "pruss" property
             - "ti,pruss-gp-mux-sel" property is removed from PRU nodes and added as an optional property to client nodes.
             - "label" property is dropped from PRU nodes
             - "interrupts" and "interrupt-names" properties were moved from INTC node to their parent node.
        - Client user API has changed to acquire and use a PRU core
   - Keystone_remoteproc
        - The "label" binding property is dropped from the driver bindings, and is replaced with an alias using the stem "rproc"
        - The "ti,sci-id" property for K2G DSP nodes is also dropped.
        - The keystone-dsp-mem driver is converted to a regular module from a platform driver, so the dspmem nodes are dropped. The module uses revised bindings.
   - Userspace
        - New IPC and CMEM releases are needed to use with 4.14 kernel due to difference in AF_RPMSG family number and other kernel API changes
- iperf2 is now replaced by iperf3
- Keystone-2: PA/PA2 is not supported in NetCP driver.
- Keystone-2: NWAL is not supported
- MMC: AM57x uses sdhci-omap.c driver instead of omap_hsmmc.c driver
- PCIe: The way in which PCIe endpoint is configured has changed. More details can be found from :ref:`PCIe End Point Driver <pcie-end-point-4-14-kernel>`.
- AM335x ICE v2: A new DT file (am335x-ice-v2-prueth.dts) is added to support PRUSS Ethernet ports. The following configurations are supported.

::

   am335x-ice-v2.dts: Both ports are CPSW controlled (Board jumpers J18 and J19 at RMII).
   am335x-ice-v2-prueth.dts: Both ports are PRUSS controlled (Board jumpers J18 and J19 at MII).

   Also note that there is an update to the u-boot env script to select DTB file
   name based on jumper settings. So user needs to do following when upgrading
   to the latest u-boot from this release:

   >env default -a
   >saveenv
   >reset

Processor SDK 04.xx Releases
============================

Processor SDK 04.03
----------------------
-  Added am572x-idk-pps.dts and am571x-idk-pps.dts which are extensions of the
   am572x-idk.dts abd an571x-idk.dts respectively. The new DTS enables the PPS
   IO pins (sync/latch) and PTP BC bindings at the modified AM572x-idk and
   AM571x-idks, where the USB/LCD Display are disabled
-  Camera support for AM572x GPEVM is not in the default DTB.Use
   am57xx-evm*-cam-mt9t111.dtb for mt9t111 camera, and am57xx-evm*-cam-ov10635.dtb
   for ov10635 camera
-  Processor SDK documentation is now created from reStructuredText sources using
   Sphinx, and hosted on software-dl.ti.com instead of processors wiki
-  For AM57xx, with the addition of new components in the filesystem, the minimum
   SD-card size is 8 GB (4 GB SD cards no longer work).
-  For am57xx devices, the location of the saved U-Boot environment has moved
   from the external SD card to eMMC. Because of this change, the state of the
   U-Boot environment can no longer be guaranteed on a newly created SD card.
   The uEnv.txt file located on the boot partition of the SD card contains the
   logic to compensate for this change. Upon the initial boot, the environment
   will be reset to the default, and the empty file ".psdk_setup" will be
   created on the boot partition. Subsequent boots will detect this file and
   bypass resetting the environment.

Processor SDK 04.02
----------------------
.. rubric:: Linux

.. rubric:: PRUETH Driver
   :name: prueth-driver

| The module parameter syntax has changed from "prueth.pruss1\_ethtype"
  and "prueth.pruss2\_ethtype" in older release to
  "ti\_prueth.pruss1\_ethtype" and "ti\_prueth.pruss2\_ethtype".

|

Processor SDK 04.01
----------------------

.. rubric:: IPC
   :name: ipc

.. rubric:: PRUSS remoteproc
   :name: pruss-remoteproc

-  PRUs are no longer automatically booted (remoteproc 'auto\_boot' is
   set to false) by remoteproc core. A PRU has to be booted either by
   PRU Client Drivers or a PRU applications in userspace. The
   kernel-space boot is triggered using the rproc\_boot() kernel API,
   and the user-space applications can use the sysfs to start and stop
   the corresponding remoteproc. Please see
   Documentation/ABI/testing/sysfs-class-remoteproc file in kernel for
   sysfs usage details.
-  PRU remoteproc driver no longer configures the PRU Ethernet firmwares
   automatically using board-machine compatibles. The needed firmware
   names are configured by the PRU Ethernet driver now using the
   rproc\_set\_firmware() function.
-  Userspace PRU applications have to make sure to unload any existing
   PRU client drivers using a specific PRU, and set their firmware using
   sysfs before starting and using a PRU

|

Processor SDK 04.00
----------------------

-  This is the first release for 2017 LTS (Kernel: 4.9, U-boot: 2017.01,
   gcc: 6.2.1 and Yocto: 2.2 (morty)), with following major changes.

.. rubric:: IPC
   :name: ipc-1

.. rubric:: remoteproc

-  The debugfs 'state' variable is replaced with a sysfs 'state'
   variable accepting 'start' and 'stop' to boot and shutdown a remote
   processor from userspace
-  A new sysfs variable 'firmware' is also added to set a new firmware.
   remoteprocs need to be in stopped state before a firmware can be set.
   New firmwares still need to reside in /lib/firmware
-  Booting a remote processor is now triggered by the insertion of the
   respective remoteproc platform driver. On 4.4, with virtio-rpmsg
   enabled firmwares, this only happened when both the remoteproc
   platform driver and virtio\_rpmsg\_bus module were installed.
-  Upstream 4.9 remoteproc and rpmsg cores are not suitable for TI
   platforms. A minimum of 4.10-rc4 (or the required remoteproc/rpmsg
   patches from 4.10-rc4) is needed if porting TI remoteproc drivers
   onto upstream.

.. rubric:: rpmsg

-  virtio\_rpmsg\_bus module split into a 'rpmsg\_core' and virtio-rpmsg
   transport specific 'virtio\_rpmsg\_bus' modules.
-  Removal of virtio\_rpmsg\_bus no longer stops a remote processor and
   should be avoided if a remote processor is running. \* If removed and
   installed again, the rpmsg communication devices will not be
   reprobed.

.. rubric:: Keystone\_remoteproc
   :name: keystone_remoteproc

-  A new 'label' binding property is now mandatory. It will have the
   string names for the DSPs in the format "dsp<X>" (eg: dsp0, dsp7 etc)
-  K2G DSP nodes will require a new "ti,sci-id" property, and a
   different value for "power-domains" property (this is generic to all
   K2G devices)

.. rubric:: PRUSS remoteproc
   :name: pruss-remoteproc-1

-  The AM437x specific am437x\_pruss\_wrapper module has been replaced
   with a generic pruss\_soc\_bus module, and is required to be
   installed on all SoCs.
-  New compatibles on AM335x and AM437x SoCs - The previous 'am3352-xxx'
   and 'am4372-xxx' have been replaced with a 'am3356-xxx' and
   'am4376-xxx' compatibles since PRUSS are not present on AM3352 and
   AM4372 SoCs. The PRU nodes are also not enabled by default in base
   'am33xx.dtsi' and 'am4372.dtsi' files.
-  New device hierarchy structure - The PRUSS node hierarchy from 4.4 is
   moved one-level down under a new parent pruss\_soc\_bus node.

.. rubric:: CPSW CPDMA Descriptor Usage
   :name: cpsw-cpdma-descriptor-usage

There is a notable change in how to place cpsw cpdma descriptors in DDR
and configure descs number: **TI K4.4** device tree property was used
"descs\_pool\_size" - descs\_pool\_size : total number of CPDMA CPPI
descriptors to be used for both ingress/egress packets processing. if
not specified the default value 256 will be used which will allow to
place descriptors pool into the internal CPPI RAM.

**New approach**
http://processors.wiki.ti.com/index.php/Linux_Core_CPSW_User%27s_Guide#Configure_number_of_TX.2FRX_descriptors

.. rubric:: PCI ENDPOINT
   :name: pci-endpoint

The usage of 'pci-ep' configfs directory to configure PCI Endpoint has
been changed in accordance with upstream review comments. Please see
http://processors.wiki.ti.com/index.php/Linux_Core_PCIe_EP_User%27s_Guide#4.9_Kernel,
for additional details

.. rubric:: Display
   :name: display

fbdev is only set up for the primary display, instead of all displays.
This results in the secondary displays to be left disabled by the
kernel, until an userspace application enables the displays.

.. rubric:: U-Boot RNDIS boot
   :name: u-boot-rndis-boot

AM335x USB client (RNDIS) boot and Ethernet boot modes are now supported
using default defconfig (am335x\_evm\_defconfig). Similarly AM437x USB
client (RNDIS) boot is now supported by am43xx\_evm\_defconfig. Separate
defconfigs for above boot modes no longer exist.

.. rubric:: Keystone-2 features
   :name: keystone-2-features

The following features are not ported to 2017 LTS

-  SRIO Kernel driver
-  10G Uboot
-  IPSec sideband and inflow mode
-  QoS

|

Processor SDK 03.xx Releases
============================

Processor SDK 03.03
-------------------

-  HDMI-connected monitor no longer takes precedence over built-in LCD
   as a default graphics display for e.g. Matrix
-  See the Release Notes for full list of modifications.

|

Processor SDK 03.02
-------------------

-  The QT QPA eglfs\_kms, which supports multiple screens, has been
   enabled and used as the default eglfs platform plugin. For more
   information, see `QT and Graphics
   Migration <../../../linux/Foundational_Components_Graphics.html>`__
-  bootmonitor now goes thru mkimage and as a result the load address
   changed. Users should manually execute following commands in their
   u-boot environment to properly install the secure monitor on k2
   platforms:

::

    setenv addr_mon 0xc08000
    setenv addr_mon_mkimg 0xc07ffc0
    setenv mon_size 0x1210
    setenv sec_bm_install 'go ${addr_mon}4 0xc084000 ${mon_size}; mon_install ${addr_mon_mkimg}'
    run sec_bm_install

-  HDMI-connected monitor no longer takes precedence over built-in LCD
   as a default graphics display for e.g. Matrix

|

Processor SDK 03.01
-------------------

-  defconfig\_builder is now used to generate working kernel defconfigs
-  In K2 U-Boot, added multi slave support.
-  In K2 Linux PA driver, added pre-classification support. So explicit
   lut rules for broadcast and multicast are removed and the same is
   achieved through this feature in PA
-  10G Ethernet driver now supports auto configuration using MCU
   firmware (a.k.a 10G KR firmware). The firmware file name is
   ks2\_xgbe\_serdes\_mcu\_fw.bin which is available at the same
   location as other serdes firmwares.
-  The current version of the serdes firmware is 03.03.00.02C and the
   same is not backward compatible with the firmware in the previous SDK
   release (03.00.00)

|

Processor SDK 03.00
-------------------

-  First 2016 LTS Release (Linux Kernel: 4.4, U-Boot: 2016.05, GCC 5.3,
   Yocto 2.1)
-  Unified kernel configuration based on multi\_v7\_defconfig
-  Migrated from SysVinit to systemd for user space initialization.
-  U-Boot drivers now uses DT, but is transparent to users
-  The content of <evm>-<os>-sdk-arago-src-<ver>.tar.gz on the download
   page changed from sources to a fetcher script that obtains the
   sources. This is to efficiently share the sources between different
   platforms and OSes supported by Processor SDK. See the README inside
   the tar-ball for instructions
-  This release adds support for RT Linux on AM335x ICE and K2G GPEVM
-  In K2 U-Boot, multi slave support is currently missing. To use
   multiple interfaces, please disable CONFIG\_DM\_ET option in u-boot
   .config and build.
-  See the Release Notes for full list of modifications.

|

Processor SDK 02.xx Releases
============================

Processor SDK 02.00.02
----------------------
-  This release adds RT Linux support on AM335x, K2H/K, K2E, K2L
-  This release supports AM572x IDK and K2G EVM
-  OpenCV now uses OpenCL under the hood, to offload compute tasks to
   C66x cores. This is transparent to the application
-  The SGX driver for AM335x has been enhanced to support DRM/WAYLAND
   based Multi-Window Display. For more information, see `AM3 Graphics
   Migration <../../../linux/Foundational_Components/Graphics/SGX/Migration_From_Prior_Releases.html#from-processor-sdk-2-0-1-to-2-0-x-for-am3-4-5>`__
-  See the Release Notes for full list of modifications.

|

Processor SDK 02.00.01
----------------------
-  This release adds support for devices from the KeyStone architecture:
   K2E, K2H/K, and K2L
-  This release also supports RT Linux is supported on AM4 and AM5
   device
-  The SGX driver for AM4 has been enhanced to support DRM/WAYLAND based
   Multi-Window Display. For more information, see `AM4 Graphics
   Migration <../../../linux/Foundational_Components/Graphics/SGX/Migration_From_Prior_Releases.html#from-processor-sdk-2-0-0-to-2-0-x-for-am4>`__
-  There is no migration impact to customers using AM3, and AM5.
-  See the Release Notes for full list of modifications.

|

Processor SDK 02.00.00
----------------------
-  This release adds support for AM57x
-  First 2015 LTS (Kernel 4.1, U-boot 2015.07) Release
-  Starting this release, Processor SDK Installer is 64-bit, and
   installs only on 64-bit host machine. Support for 32-bit host is
   dropped as Linaro toolchain is available only for 64-bit machines
-  For AM3, AM4, Graphics SDK is now obsolete and Graphics stack is
   integrated into Processor SDK, and supports null DRM based Full
   Window, with Front and Flip modes. For more information, see
   `Graphics
   Migration <../../../linux/Foundational_Components/Graphics/SGX/Migration_From_Prior_Releases.html#from-processor-sdk-1-x-to-2-x-for-am3-am4>`__
-  Ethernet performance degraded ~10% on am335x-evm due to move from
   preempt\_voluntary
-  See the Release Notes for full list of modifications.

