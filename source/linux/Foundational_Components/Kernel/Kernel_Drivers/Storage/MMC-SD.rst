.. http://processors.wiki.ti.com/index.php/Linux_Core_MMC/SD_User%27s_Guide

MMCSD
#####

.. ifconfig:: CONFIG_part_family in ('AM62X_family', 'AM62PX_family')

   .. warning::

      There is important information on multimedia card (MMC) support for |__PART_FAMILY_DEVICE_NAMES__| device, go
      :ref:`here <mmc-support-linux>` for more information.

Introduction
************

The multimedia card secure digital (MMCSD) host controller provides an interface between a local host (LH)
such as a microprocessor unit (MPU) or digital signal processor (DSP) and either embedded multimedia card (eMMC),
secure digital (SD), or secure digital input/output (SDIO) devices. The MMCSD host controller handles MMCSD and
SDIO protocol with minimal LH intervention.

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family', 'AM57X_family')

   Main features of the MMCSD host controllers:

   -  Full compliance with MMCSD command/response sets as defined in the
      Specification.

   -  Support:

      -  4-bit transfer mode specifications for SD and SDIO cards
      -  8-bit transfer mode specifications for eMMC
      -  Built-in 1024-byte buffer for read or write
      -  32-bit-wide access bus to maximize bus throughput
      -  Single interrupt line for multiple interrupt source events
      -  Two slave DMA channels (1 for TX, 1 for RX)
      -  Designed for low power and programmable clock generation
      -  Maximum operating frequency of 48MHz
      -  MMCSD card hot insertion and removal

The following image shows the MMCSD Driver Architecture:

.. Image:: /images/Mmcsd_Driver.png

References
**********

#. `JEDEC eMMC homepage <http://www.jedec.org/category/technology-focus-area/flash-memory-ssds-ufs-emmc//>`__
#. `SD organization homepage <http://www.sdcard.org//>`__

Features
********

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family', 'AM57X_family')

   The SD driver supports the following features:

   -  The driver is built in-kernel (part of vmlinux)
   -  SD cards including SD High Speed and secure digital high capacity (SDHC) cards
   -  Uses block bounce buffer to aggregate scattered blocks

.. ifconfig:: CONFIG_part_family in ('J7_family')

   The MMCSD driver supports the following features:

   - Support ADMA for DMA transfers
   - HS400 speed mode
   - Support for both built-in and module mode
   - ext2/ext3/ext4 file system support

.. ifconfig:: CONFIG_part_family in ('AM62X_family', 'AM62AX_family', 'AM64X_family', 'AM62LX_family', 'AM62PX_family')

   The MMCSD driver supports the following features:

   - Support ADMA for DMA transfers
   - HS200 speed mode
   - Support for both built-in and module mode
   - ext2/ext3/ext4 file system support

.. _mmc-supported-uhs-modes:

Supported ultra high speed (UHS) modes
**************************************

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM57X_family', 'AM65X_family')

   +--------------------+--------+-------+-------+-------+-------+
   | Platform           | SDR104 | DDR50 | SDR50 | SDR25 | SDR12 |
   +====================+========+=======+=======+=======+=======+
   | DRA74-EVM          | Y      | Y     | Y     | Y     | Y     |
   +--------------------+--------+-------+-------+-------+-------+
   | DRA72-EVM          | Y      | Y     | Y     | Y     | Y     |
   +--------------------+--------+-------+-------+-------+-------+
   | DRA71-EVM          | Y      | Y     | Y     | Y     | Y     |
   +--------------------+--------+-------+-------+-------+-------+
   | DRA72-EVM-REVC     | Y      | Y     | Y     | Y     | Y     |
   +--------------------+--------+-------+-------+-------+-------+
   | AM57XX-EVM         | N      | N     | N     | N     | N     |
   +--------------------+--------+-------+-------+-------+-------+
   | AM57XX-EVM-REVA3   | N      | N     | N     | N     | N     |
   +--------------------+--------+-------+-------+-------+-------+
   | AM572X-IDK         | N      | N     | N     | N     | N     |
   +--------------------+--------+-------+-------+-------+-------+
   | AM571X-IDK         | N      | N     | N     | N     | N     |
   +--------------------+--------+-------+-------+-------+-------+
   | AM654-SR2-EVM      | Y      | Y     | Y     | Y     | Y     |
   +--------------------+--------+-------+-------+-------+-------+

   .. note::

      In AM654-SR1-EVM none of the UHS modes are supported.

   **Important Info**: Certain UHS cards do not enumerate.
   The list of functional UHS cards is given in the following tables

   +-------------------------------------------------------------------------------------------+
   | FUNCTIONAL UHS CARDS                                                                      |
   +===========================================================================================+
   | ATP 32GB UHS CARD AF32GUD3                                                                |
   +-------------------------------------------------------------------------------------------+
   | STRONTIUM NITRO 466x UHS CARD                                                             |
   +-------------------------------------------------------------------------------------------+
   | SANDISK EXTREME UHS CARD                                                                  |
   +-------------------------------------------------------------------------------------------+
   | SANDISK ULTRA UHS CARD                                                                    |
   +-------------------------------------------------------------------------------------------+
   | SAMSUNG EVO+ UHS CARD                                                                     |
   +-------------------------------------------------------------------------------------------+
   | SAMSUNG EVO UHS CARD                                                                      |
   +-------------------------------------------------------------------------------------------+
   | KINGSTON UHS CARD (DDR mode)                                                              |
   +-------------------------------------------------------------------------------------------+
   | TRANSCEND PREMIUM 400X UHS CARD (Non fatal error and then it re-enumerates in UHS mode)   |
   +-------------------------------------------------------------------------------------------+

   +------------------------------------------------------------------------------+
   | FUNCTIONAL (WITH LIMITED CAPABILITY) UHS CARD                                |
   +==============================================================================+
   | SONY UHS CARD - Voltage switching fails and enumerates in high speed         |
   +------------------------------------------------------------------------------+
   | GSKILL UHS CARD - Voltage switching fails and enumerates in high speed       |
   +------------------------------------------------------------------------------+
   | PATRIOT 8G UHS CARD - Voltage switching fails and enumerates in high speed   |
   +------------------------------------------------------------------------------+

   **Known Workaround**: For cards that don't enumerate in UHS mode,
   removing the PULLUP resistor in CLK line and changing the GPIO to
   PULLDOWN increases the frequency that the card enumerates in UHS
   modes.

   +--------------------+-------+---------+
   | Platform           | DDR   | HS200   |
   +====================+=======+=========+
   | DRA74-EVM          | Y     | Y       |
   +--------------------+-------+---------+
   | DRA72-EVM          | Y     | Y       |
   +--------------------+-------+---------+
   | DRA71-EVM          | Y     | Y       |
   +--------------------+-------+---------+
   | DRA72-EVM-REVC     | Y     | Y       |
   +--------------------+-------+---------+
   | AM57XX-EVM         | Y     | N       |
   +--------------------+-------+---------+
   | AM57XX-EVM-REVA3   | Y     | N       |
   +--------------------+-------+---------+
   | AM572X-IDK         | Y     | N       |
   +--------------------+-------+---------+
   | AM571X-IDK         | Y     | N       |
   +--------------------+-------+---------+
   | AM654-SR2-EVM      | Y     | Y       |
   +--------------------+-------+---------+

.. ifconfig:: CONFIG_part_family in ('J7_family')

   * SD

   .. csv-table::
      :header: "Platform", "SDR104", "DDR50", "SDR50", "SDR25", "SDR12"
      :widths: auto

      J721e-EVM, N, Y, Y, Y, Y
      J7200-EVM, Y, Y, Y, Y, Y
      J721s2-EVM, Y, Y, Y, Y, Y
      J784s4-EVM, Y, Y, Y, Y, Y
      J721e-sk, Y, Y, Y, Y, Y
      AM68-sk, Y, Y, Y, Y, Y
      AM69-sk, Y, Y, Y, Y, Y

   * eMMC

   .. csv-table::
      :header: "Platform", "DDR52", "HS200", "HS400"
      :widths: auto

      J721e-EVM, Y, Y, N
      J7200-EVM, Y, Y, Y
      J721s2-EVM, Y, Y, Y
      J784s4-EVM, Y, Y, Y
      AM69-sk, Y, Y, Y

   J721e-sk and AM68-sk does not support eMMC.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM64X', 'AM62PX' ,'AM62LX')

   * SD

   .. csv-table::
      :header: "Platform", "SDR12", "SDR25", "SDR50", "DDR50", "SDR104"
      :widths: auto

      AM62*, Y, Y, Y, Y, Y
      AM62ax, Y, Y, Y, Y, Y
      am64x, Y, Y, Y, Y, Y
      am62px, Y, Y, Y, Y, Y
      am62lx, N, N, N, N, N

   * eMMC

   .. csv-table::
      :header: "Platform", "DDR52", "HS200", "HS400"
      :widths: auto

      AM62*, Y, Y, N
      AM62ax, Y, Y, N
      am64x, Y, Y, N
      am62px, Y, Y, N
      am62lx, Y, Y, N

Driver configuration
********************

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family', 'AM57X_family')

   The default kernel configuration enables support for MMCSD(built-in to kernel).

   The selection of MMCSD/SDIO driver can be modified using the linux kernel
   configuration tool. Launch it by the following command:

   .. code-block:: console

      $ make menuconfig  ARCH=arm

   .. rubric:: **Building into Kernel**
      :name: building-into-kernel-mmcsd

   Ensure that the following config options are set to 'y':
   * CONFIG_MMC
   * CONFIG_MMC_BLOCK
   * CONFIG_MMC_SDHCI
   * CONFIG_MMC_SDHCI_OMAP  (for DRA7XX and AM57XX devices)
   * CONFIG_MMC_OMAP        (for AM335X and AM437X devices)

   .. rubric:: **Building as Loadable Kernel Module**

   Depending on your configuration, any of the above options can be set to 'm'
   to build them as a module. Use the following command to install all modules
   tp your filesystem.

   .. code-block:: console

      $ sudo -E make modules_install ARCH=arm INSTALL_MOD_PATH=path/to/filesystem

   Boot the kernel up-to kernel prompt and use modprobe to insert the driver
   module and all its dependencies.

   .. code-block:: console

      $ modprobe sdhci-omap		# for DRA7XX and AM57XX devices
      $ modprobe omap_hsmmc		# for AM335X and AM437X devices

   If **udev** is running and the SD card is already inserted, the required
   modules will be loaded and any valid filesystem will be automatically mounted
   if they exist on the card.

.. ifconfig:: CONFIG_part_family in ('J7_family', 'AM62X_family', 'AM64X_family', 'AM62AX_family', 'AM62PX_family', 'AM62LX_family')

   The default kernel configuration enables support for MMCSD driver as
   built-in to kernel. TI SDHCI driver is used. Following options need to be
   configured in Linux Kernel for successfully selecting SDHCI driver for
   |__PART_FAMILY_DEVICE_NAMES__|.

   - Enable SDHCI support (CONFIG_MMC_SDHCI)

   .. code-block:: Kconfig

      Device Drivers -->
         MMC/SD/SDIO card support -->
            <*> Secure Digital Host Controller Interface support

   - Enable SDHCI platform helper (CONFIG_MMC_SDHCI_PLTFM)

   .. code-block:: Kconfig

      Device Drivers -->
         MMC/SD/SDIO card support -->
            Secure Digital Host Controller Interface support -->
               <*> SDHCI platform and OF driver helper

   - Enable SDHCI controller for TI device (CONFIG_MMC_SDHCI_AM654)

   .. code-block:: Kconfig

      Device Drivers -->
         MMC/SD/SDIO card support -->
            <*> Support for the SDHCI Controller in TI's AM654 SOCs

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family', 'AM57X_family')

   .. rubric:: **Enabling eMMC Card Background operations support**
      :name: enabling-emmc-card-background-operations-support

   eMMC cards need to occasionally spend some time cleaning up garbage and
   perform cache/buffer related operations. These are strictly on the card
   side and do not involve the host. They occur at one of the three
   levels based on the importance/severity of the operation:

      1. Normal
      2. Important
      3. Critical

   If an operation is delayed for too long, it becomes critical, taking
   priority over the regular read/write from host. This can cause host
   operations to be delayed or take more time than expected. To avoid such
   issues the multimedia card (MMC) HW and core driver provide a framework that can check
   for pending background operations and give the card some time to service
   them before they become critical. This feature is already part of the
   framework and to start using it the User needs to enable:
   EXT\_CSD : BKOPS\_EN [163] BIT 0.

   **This can be done using the "mmc-utils" tool from user space or using
   the "mmc" command in U-boot.**

   Command to enable bkops from userspace using mmc-utils, assuming eMMC
   instance to be mmcblk0

   .. code-block:: console

      root@<machine>:mmc bkops enable /dev/mmcblk0

   You can find the instance of eMMC by reading the ios timing spec from
   debug filesystem (debugfs):

   .. code-block:: console

      root@<machine>:~# cat /sys/kernel/debug/mmc0/ios
      ----
      timing spec:    9 (mmc HS200)
      ---

   or by looking for boot partitions, eMMC has two boot partitions
   mmcblk<x>boot0 and mmcblk<x>boot1

   .. code-block:: console

      root@<machine>:/# ls /dev/mmcblk*boot*
      /dev/mmcblk0boot0  /dev/mmcblk0boot1

|

.. _mmc-support-linux:

MMC support in Linux
********************

.. ifconfig:: CONFIG_part_family in ('AM62PX_family')

   **eMMC HS400 support**

   For 11.0 and 11.1 SDK, am62px device does not support eMMC HS400 mode due to errata `i2458 <https://www.ti.com/lit/pdf/sprz574>`__.
   If support for HS400 is required, please add the following to k3-am62p-j722s-common-main.dtsi:

   .. code-block:: diff

      diff --git a/arch/arm64/boot/dts/ti/k3-am62p-j722s-common-main.dtsi b/arch/arm64/boot/dts/ti/k3-am62p-j722s-common-main.dtsi
      index 3e5ca8a3eb86..a05b22a6e5a2 100644
      --- a/arch/arm64/boot/dts/ti/k3-am62p-j722s-common-main.dtsi
      +++ b/arch/arm64/boot/dts/ti/k3-am62p-j722s-common-main.dtsi
      @@ -593,12 +593,16 @@ sdhci0: mmc@fa10000 {
                      bus-width = <8>;
                      mmc-ddr-1_8v;
                      mmc-hs200-1_8v;
      +               mmc-hs400-1_8v;
                      ti,clkbuf-sel = <0x7>;
                      ti,trm-icp = <0x8>;
      +               ti,strobe-sel = <0x55>;
                      ti,otap-del-sel-legacy = <0x1>;
                      ti,otap-del-sel-mmc-hs = <0x1>;
                      ti,otap-del-sel-ddr52 = <0x6>;
                      ti,otap-del-sel-hs200 = <0x8>;
      +               ti,otap-del-sel-hs400 = <0x5>; // at 0.85V VDD_CORE
      +               //ti,otap-del-sel-hs400 = <0x7>; // at 0.75V VDD_CORE
                      ti,itap-del-sel-legacy = <0x10>;
                      ti,itap-del-sel-mmc-hs = <0xa>;
                      ti,itap-del-sel-ddr52 = <0x3>;

.. ifconfig:: CONFIG_part_family in ('AM62X_family')

   **Missing eMMC support**

   Support for eMMC is missing for AM62SIP SK in Processor SDK 11.01. Therefore, eMMC boot, reading/writting/accessing
   the eMMC will not work on AM62SIP SK. If eMMC support is required, apply the following:
   `commit <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/commit/?h=ti-linux-6.12.y&id=78e6abff3220>`__
   in TI-Linux ti-linux-6.12.y branch to enable eMMC support in Linux.

.. ifconfig:: CONFIG_part_family not in ('AM62X_family', 'AM62PX_family')

   There is no missing MMC support for |__PART_FAMILY_DEVICE_NAMES__| device.

Steps for working around SD card issues in Linux
************************************************

.. ifconfig:: CONFIG_part_family not in ('General_family', 'AM57X_family', 'AM335X_family', 'AM437X_family')

   In some cases, failures can be seen while using some SD cards:

   - Kernel fails to enumerate SD, thus failing to mount the root file system. This is
     the case when kernel hangs during boot with a message similar to the following:

      .. code-block:: dmesg

         [    2.563279] Waiting for root device PARTUUID=835b171b-02...

   - A lot of SDHCI register dumps logs getting printed continuously:

      .. code-block:: dmesg

         [   10.811723] mmc1: Got data interrupt 0x00000002 even though no data operation was in progress.
         [   10.820321] mmc1: sdhci: ============ SDHCI REGISTER DUMP ===========
         [   10.826745] mmc1: sdhci: Sys addr:  0x00000080 | Version:  0x00001004
         [   10.833169] mmc1: sdhci: Blk size:  0x00007200 | Blk cnt:  0x00000080
         [   10.839593] mmc1: sdhci: Argument:  0x00000000 | Trn mode: 0x00000033
         [   10.846016] mmc1: sdhci: Present:   0x01f70000 | Host ctl: 0x0000001f
         [   10.852440] mmc1: sdhci: Power:     0x0000000f | Blk gap:  0x00000080
         [   10.858864] mmc1: sdhci: Wake-up:   0x00000000 | Clock:    0x00000007
         [   10.865287] mmc1: sdhci: Timeout:   0x00000000 | Int stat: 0x00000000
         [   10.871711] mmc1: sdhci: Int enab:  0x03ff008b | Sig enab: 0x03ff008b
         [   10.878134] mmc1: sdhci: ACmd stat: 0x00000000 | Slot int: 0x00000000
         [   10.884557] mmc1: sdhci: Caps:      0x3de8c801 | Caps_1:   0x18002407
         [   10.890981] mmc1: sdhci: Cmd:       0x00000c1a | Max curr: 0x00000000
         [   10.897404] mmc1: sdhci: Resp[0]:   0x00000b00 | Resp[1]:  0x0075cf7f
         [   10.903828] mmc1: sdhci: Resp[2]:   0x32db7900 | Resp[3]:  0x00000900
         [   10.910251] mmc1: sdhci: Host ctl2: 0x0000000b
         [   10.914682] mmc1: sdhci: ADMA Err:  0x00000000 | ADMA Ptr: 0x00000000a2e90200

   Given below are the list of various workarounds that can be done in the device tree
   node to get SD card working. The workarounds are ordered from least to most performance
   impacting.

   .. note::

      All the changes mentioned below, are to be done in the MMCSD device tree node
      corresponding to the SD instance. This is usually the first (index starting
      from zero) instance.

   #. Restricting to a given speed mode

      By default the kernel driver tries to enumerate an SD card in the highest supported
      speed mode. Below is the order that the driver tries to enumerate an SD card:

         - SDR104
         - DDR50
         - SDR50
         - SD HS
         - SD legacy

      The **sdhci-caps-mask** can be added to the DT node to cap at a specific mode:

         - Limit to DDR50: ``sdhci-caps-mask = <0x00000003 0x00000000>``
         - Limit to SD HS: ``sdhci-caps-mask = <0x00000007 0x00000000>``
         - Limit to SD legacy: ``sdhci-caps-mask = <0x00000007 0x00200000>``

      The following is an example DT node with the added **sdhci-caps-mask**:

      .. code-block:: dts

         &sdhci1 {
            /* SD/MMC */
            vmmc-supply = <&vdd_mmc1>;
            vqmmc-supply = <&vdd_sd_dv>;
            pinctrl-names = "default";
            pinctrl-0 = <&main_mmc1_pins_default>;
            ti,driver-strength-ohm = <50>;
            disable-wp;
            sdhci-caps-mask = <0x00000003 0x00000000>; /* Limiting to DDR50 speed mode */
         };

      Limiting to SD HS speed mode can also be done by using the property
      **no-1-8-v**. This disables switching to 1.8V, which is required for
      UHS speed modes(SDR104, DDR50, SDR50, SDR25, SDR12):

      .. code-block:: dts

         &sdhci1 {
            /* SD/MMC */
            vmmc-supply = <&vdd_mmc1>;
            vqmmc-supply = <&vdd_sd_dv>;
            pinctrl-names = "default";
            pinctrl-0 = <&main_mmc1_pins_default>;
            ti,driver-strength-ohm = <50>;
            disable-wp;
            no-1-8-v; /* disabling all the UHS modes */
         };

   #. Reduce the bus width

      The SD interface supports a bus width of 4. It can be reduced to 1 by
      changing the **bus-width** device tree property from 4 to 1.

      .. code-block:: diff

         diff --git a/arch/arm64/boot/dts/ti/k3-am62-main.dtsi b/arch/arm64/boot/dts/ti/k3-am62-main.dtsi
         index 7bbfcb158842..2ef974f7206f 100644
         --- a/arch/arm64/boot/dts/ti/k3-am62-main.dtsi
         +++ b/arch/arm64/boot/dts/ti/k3-am62-main.dtsi
         @@ -424,7 +424,7 @@
            ti,itap-del-sel-sdr12 = <0x0>;
            ti,itap-del-sel-sdr25 = <0x0>;
            ti,clkbuf-sel = <0x7>;
         -     bus-width = <4>;
         +     bus-width = <1>;
         };

         sdhci2: mmc@fa20000 {

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM57X_family', 'AM335X_family', 'AM437X_family')

   Steps for working around SD card issues in Linux documentation is pending for |__PART_FAMILY_DEVICE_NAMES__|
   please reach out to:  `Help e2e <https://e2e.ti.com//>`__ for additional information.

|

.. _mmc-listing-mmc-devices-linux:

Listing MMC devices from Linux
******************************
eMMC and SD cards register with the MMC subsystem and are available as a block device
as :file:`/dev/mmcblk{n}`. To find the device index **n** corresponding to an eMMC device,
check which device includes :file:`mmcblk{n}boot0` and :file:`mmcblk{n}boot1`. Here,
mmcblk0* is in eMMC.

.. code-block:: console

   root@<machine>:~# ls -l /dev/mmcblk*
   brw-rw---- 1 root disk 179,  0 Jan  1 00:10 /dev/mmcblk0
   brw-rw---- 1 root disk 179, 32 Jan  8  2025 /dev/mmcblk0boot0
   brw-rw---- 1 root disk 179, 64 Jan  8  2025 /dev/mmcblk0boot1
   brw-rw---- 1 root disk 179,  1 Jan  1 00:14 /dev/mmcblk0p1
   crw------- 1 root root 239,  0 Jan  1 00:00 /dev/mmcblk0rpmb
   brw-rw---- 1 root disk 179, 96 Jan  8  2025 /dev/mmcblk1
   brw-rw---- 1 root disk 179, 97 Jan  1 00:00 /dev/mmcblk1p1
   brw-rw---- 1 root disk 179, 98 Jan  8  2025 /dev/mmcblk1p2

The disk partitions for each MMC device are displayed as :file:`/dev/mmcblk{n}p{x}`.
To check existing or mounted disk partitions for an eMMC device, use the
command :command:`lsblk`, such as:

.. code-block:: console

   root@<machine>:~# lsblk
   NAME         MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
   mmcblk0      179:0    0 14.8G  0 disk
   mmcblk0boot0 179:32   0 31.5M  1 disk
   mmcblk0boot1 179:64   0 31.5M  1 disk
   mmcblk1      179:96   0 14.8G  0 disk
   |-mmcblk1p1  179:97   0  128M  0 part /run/media/boot-mmcblk1p1
   `-mmcblk1p2  179:98   0  1.9G  0 part /

Use the :command:`mount` and :command:`umount` commands to mount and unmount formatted disk
partitions, usually to virtual file allocation table (vfat) or fourth extended file system (ext4) types.

.. _mmc-create-partitions-in-emmc-linux:

Create partitions in eMMC UDA
*****************************

In eMMC, the user data area (UDA) HW partition is the primary storage space generally used
to flash the root filesystem (rootfs). To create disk partitions in UDA, use the :command:`fdisk` command.
For ex: :samp:`fdisk /dev/mmcblk{n}` in which **n** is typically 0 or 1. In the previous example,
eMMC is :samp:`fdisk /dev/mmcblk0`.

For documentation on using fdisk command, go to: `fdisk how-to <https://tldp.org/HOWTO/Partition/fdisk_partitioning.html>`__.

**Erase eMMC UDA**

In Linux, before creating disk partitions, we can optionally erase eMMC UDA by using :command:`dd`
command:

.. code-block:: console

   root@<machine>:~# umount /dev/mmcblk0*
   root@<machine>:~# dd if=/dev/zero of=/dev/mmcblk0 bs=1M count=n

where ``n`` should be determined according to the following formula: ``count = total size UDA (bytes) / bs``.

.. _mmc-create-boot-partition-emmc-linux:

Create "boot" partition
=======================

In this example create a "boot" partition of size 400 MiB which can be formatted to vfat type
and will store the boot loader binaries.

.. code-block:: console

   root@<machine>:~# fdisk /dev/mmcblk0

   Welcome to fdisk (util-linux 2.39.3).
   Changes will remain in memory only, until you decide to write them.
   Be careful before using the write command.

   Command (m for help): n
   Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
   Select (default p):

   Using default response p.
   Partition number (1-4, default 1):
   First sector (2048-31080447, default 2048):
   Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-31080447, default 31080447): +400M

   Created a new partition 1 of type 'Linux' and of size 400 MiB.
   Partition #1 contains a vfat signature.

   Do you want to remove the signature? [Y]es/[N]o: y

   The signature will be removed by a write command.

   Command (m for help): a
   Selected partition 1
   The bootable flag on partition 1 is enabled now.

   Command (m for help): t
   Selected partition 1
   Hex code or alias (type L to list all): c
   Changed type of partition 'Linux' to 'W95 FAT32 (LBA)'.

   Command (m for help): w
   The partition table has been altered.
   [  644.818358]  mmcblk0: p1
   Calling ioctl() to re-read partition table.
   Syncing disks.

Make sure bootable flag is set for "boot" partition, ROM might not boot from this partition
if bootable flag is not set.

.. _mmc-create-root-partition-emmc-linux:

Create "root" partition
=======================

In this example create a "root" partition which can be formatted to ext4 type and will store
Linux kernel Image, DTB, and the rootfs.

.. code-block:: console

   root@<machine>:~# fdisk /dev/mmcblk0

   Welcome to fdisk (util-linux 2.39.3).
   Changes will remain in memory only, until you decide to write them.
   Be careful before using the write command.

   This disk is currently in use - repartitioning is probably a bad idea.
   It's recommended to umount all file systems, and swapoff all swap
   partitions on this disk.


   Command (m for help): n
   Partition type
   p   primary (1 primary, 0 extended, 3 free)
   e   extended (container for logical partitions)
   Select (default p):

   Using default response p.
   Partition number (2-4, default 2):
   First sector (821248-31080447, default 821248):
   Last sector, +/-sectors or +/-size{K,M,G,T,P} (821248-31080447, default 31080447):

   Created a new partition 2 of type 'Linux' and of size 14.4 GiB.

   Command (m for help): t
   Partition number (1,2, default 2): 2
   Hex code or alias (type L to list all): 83

   Changed type of partition 'Linux' to 'Linux'.

   Command (m for help): w
   The partition table has been altered.
   Syncing disks.

.. _mmc-format-partition-linux:

Formatting eMMC partitions from Linux
*************************************

After creating a partition/s, the partition can be formatted with the :command:`mkfs` command.
For ex: :samp:`mkfs -t ext4 /dev/mmcblk{n}` where **mmcblk{n}** is the MMC device with the new
disk partitions to format. The general syntax for formatting disk partitions in Linux is:

.. code-block:: console

   mkfs.vfat [OPTIONS] TARGET [BLOCKS]
   mkfs.ext4 [-c|-l filename] [-b block-size] [-C cluster-size]

.. _mmc-format-partition-vfat:

Format to vfat
==============

In this example, format the "boot" partition to type vfat.

.. code-block:: console

   root@<machine>:~# mkfs.vfat -F 32 -n "boot" /dev/mmcblk0p1

.. _mmc-format-partition-ext4:

Format to ext4
==============

In this example, format the "root" partition to type ext4.

.. code-block:: console

   root@<machine>:~# mkfs.ext4 -L "root" /dev/mmcblk0p2

**Verify partitions**

   Verify setup of :file:`mmcblk0p1` and :file:`mmcblk0p2` with :command:`lsblk` command.

   .. code-block:: console

      root@<machine>:~# lsblk -o name,mountpoint,label,size,uuid
      NAME         MOUNTPOINT                LABEL  SIZE UUID
      mmcblk0                                      14.8G
      |-mmcblk0p1                            boot   400M E4D4-4879
      `-mmcblk0p2                            root  14.4G 74d40075-07e4-4bce-9401-6fccef68e934
      mmcblk0boot0                                 31.5M
      mmcblk0boot1                                 31.5M
      mmcblk1                                      29.7G
      |-mmcblk1p1  /run/media/boot-mmcblk1p1 boot   128M 681F-55DD
      `-mmcblk1p2  /                         root   8.7G ead4c8bb-fa37-4c4d-9ba3-47a1f3824764

.. _mmc-flash-emmc-uda:

Flash eMMC for MMCSD boot
*************************

In this example, we show one simple method for flashing to eMMC for MMCSD boot from
eMMC UDA in filesystem (FS) mode. Know this is not the only method for flashing the eMMC for this
boot mode.

This example assumes the current boot mode is MMCSD boot from SD (FS mode)

.. _mmc-flash-emmc-uda-boot:

Flash to eMMC "boot" partition
==============================

.. code-block:: console

   root@<machine>:~# umount /run/media/*
   root@<machine>:~# mkdir /mnt/eboot /mnt/sdboot
   root@<machine>:~# mount /dev/mmcblk0p1 /mnt/eboot
   root@<machine>:~# mount /dev/mmcblk1p1 /mnt/sdboot

Verify the partitions are mounted to the correct folders by using :command:`lsblk` command in the
column labeled :file:`MOUNTPOINTS`.

.. code-block:: console

   root@<machine>:~# lsblk
   NAME         MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
   mmcblk0      179:0    0 14.8G  0 disk
   |-mmcblk0p1  179:1    0  400M  0 part /mnt/eboot
   `-mmcblk0p2  179:2    0 14.4G  0 part
   mmcblk0boot0 179:32   0 31.5M  1 disk
   mmcblk0boot1 179:64   0 31.5M  1 disk
   mmcblk1      179:96   0 29.7G  0 disk
   |-mmcblk1p1  179:97   0  128M  0 part /mnt/sdboot
   `-mmcblk1p2  179:98   0  8.7G  0 part /

Now we can copy boot loader binaries to eMMC and umount the partitions when writes finish.

.. code-block:: console

   root@<machine>:~# ls /mnt/sdboot/
   tiboot3.bin  tispl.bin	u-boot.img  uEnv.txt
   root@<machine>:~# cp /mnt/sdboot/* /mnt/eboot/
   root@<machine>:~# sync && umount /mnt/*

.. _mmc-flash-emmc-uda-root:

Flash to eMMC "root" partition
==============================

.. code-block:: console

   root@<machine>:~# umount /run/media/*
   root@<machine>:~# mkdir /mnt/eroot /mnt/sdroot
   root@<machine>:~# mount /dev/mmcblk0p2 /mnt/eroot
   [69229.982452] EXT4-fs (mmcblk0p2): mounted filesystem 74d40075-07e4-4bce-9401-6fccef68e934 r/w with ordered data mode. Quota mode: none.
   root@<machine>:~# mount /dev/mmcblk1p2 /mnt/sdroot

Verify the partitions are mounted to the correct folders by using :command:`lsblk` command in the
column labeled :file:`MOUNTPOINTS`.

.. code-block:: console

   root@<machine>:~# lsblk
   NAME         MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
   mmcblk0      179:0    0 14.8G  0 disk
   |-mmcblk0p1  179:1    0  400M  0 part
   `-mmcblk0p2  179:2    0 14.4G  0 part /mnt/eroot
   mmcblk0boot0 179:32   0 31.5M  1 disk
   mmcblk0boot1 179:64   0 31.5M  1 disk
   mmcblk1      179:96   0 29.7G  0 disk
   |-mmcblk1p1  179:97   0  128M  0 part
   `-mmcblk1p2  179:98   0  8.7G  0 part /mnt/sdroot
                                         /

Now we can copy rootfs to eMMC (either from SD rootfs or from tar file) and umount the partitions
when writes finish.

**From SD**

.. code-block:: console

   root@<machine>:~# ls /mnt/sdroot
   bin   dev  home  lost+found  mnt  proc	run   srv  tmp	var
   boot  etc  lib	 media	     opt  root	sbin  sys  usr
   root@<machine>:~# cp -r -a /mnt/sdroot/* /mnt/eroot
   root@<machine>:~# sync
   root@<machine>:~# umount /mnt/*
   [70154.205154] EXT4-fs (mmcblk0p2): unmounting filesystem 74d40075-07e4-4bce-9401-6fccef68e934.

**From tar file**

This sections requires for tisdk-base-image-<soc>evm.rootfs.tar.xz to have been previously copied
to the SD card rootfs.

.. code-block:: console

   root@<machine>:~# ls
   tisdk-base-image-<soc>-evm.rootfs.tar.xz
   root@<machine>:~# tar -xpf tisdk-base-image-<soc>-evm.rootfs.tar.xz -C /mnt/eroot
   root@<machine>:~# sync
   root@<machine>:~# umount /mnt/*
