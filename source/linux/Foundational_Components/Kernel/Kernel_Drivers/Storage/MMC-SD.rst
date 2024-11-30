.. http://processors.wiki.ti.com/index.php/Linux_Core_MMC/SD_User%27s_Guide

MMC/SD
---------------------------------

Introduction
^^^^^^^^^^^^

The multimedia card high-speed/SDIO (MMC/SDIO) host controller provides
an interface between a local host (LH) such as a microprocessor unit
(MPU) or digital signal processor (DSP) and either MMC, SD® memory
cards, or SDIO cards and handles MMC/SDIO transactions with minimal LH
intervention.

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family')

   Main features of the MMC/SDIO host controllers:


   -  Full compliance with MMC/SD command/response sets as defined in the
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
      -  MMC/SD card hot insertion and removal

.. Image:: /images/Mmcsd_Driver.png

MMC/SD Driver Architecture

|

References
^^^^^^^^^^

#. JEDEC eMMC Homepage
   [http://www.jedec.org/category/technology-focus-area/flash-memory-ssds-ufs-emmc]
#. SD ORG Homepage [http://www.sdcard.org]

|

Acronyms & Definitions
^^^^^^^^^^^^^^^^^^^^^^

+-----------+--------------------+
| Acronym   | Definition         |
+===========+====================+
| MMC       | Multimedia Card    |
+-----------+--------------------+
| HS-MMC    | High Speed MMC     |
+-----------+--------------------+
| SD        | Secure Digital     |
+-----------+--------------------+
| SDHC      | SD High Capacity   |
+-----------+--------------------+
| SDIO      | SD Input/Output    |
+-----------+--------------------+

Table:  **MMC/SD: Acronyms**

|

Features
^^^^^^^^

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family')

   The SD driver supports the following features:

   -  The driver is built in-kernel (part of vmlinux)
   -  SD cards including SD High Speed and SDHC cards
   -  Uses block bounce buffer to aggregate scattered blocks

.. ifconfig:: CONFIG_part_family in ('J7_family')

   The SD/MMC driver supports the following features:

   - Support ADMA for DMA transfers
   - HS400 speed mode
   - Support for both built-in and module mode
   - ext2/ext3/ext4 file system support

Supported High Speed Modes
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_family in ('General_family')

   +--------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
   | Platform           | SDR104            | DDR50             | SDR50             | SDR25             | SDR12             |
   +====================+===================+===================+===================+===================+===================+
   | DRA74-EVM          | Y                 | Y                 | Y                 | Y                 | Y                 |
   +--------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
   | DRA72-EVM          | Y                 | Y                 | Y                 | Y                 | Y                 |
   +--------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
   | DRA71-EVM          | Y                 | Y                 | Y                 | Y                 | Y                 |
   +--------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
   | DRA72-EVM-REVC     | Y                 | Y                 | Y                 | Y                 | Y                 |
   +--------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
   | AM57XX-EVM         | N                 | N                 | N                 | N                 | N                 |
   +--------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
   | AM57XX-EVM-REVA3   | N		    | N			| N		    | N			| N		    |
   +--------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
   | AM572X-IDK         | N		    | N			| N		    | N			| N		    |
   +--------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
   | AM571X-IDK         | N		    | N			| N		    | N			| N		    |
   +--------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
   | AM654-SR2-EVM      | Y		    | Y			| Y		    | Y			| Y		    |
   +--------------------+-------------------+-------------------+-------------------+-------------------+-------------------+

   Table:  **MMC1/SD**

   **Note**: In AM654-SR1-EVM none of the UHS modes are supported.

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

   **Known Workaround**: For cards which doesn't enumerate in UHS mode,
   removing the PULLUP resistor in CLK line and changing the GPIO to
   PULLDOWN increases the frequency in which the card enumerates in UHS
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

   Table:  **MMC2/EMMC**

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

Driver Configuration
^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family')

   The default kernel configuration enables support for MMC/SD(built-in to kernel).

   The selection of MMC/SD/SDIO driver can be modified using the linux kernel
   configuration tool. Launch it by the following command:

   ::

       $ make menuconfig  ARCH=arm

   .. rubric:: **Building into Kernel**
      :name: building-into-kernel-mmcsd

   Ensure that the following config options are set to 'y':
	* CONFIG_MMC
	* CONFIG_MMC_BLOCK
	* CONFIG_MMC_SDHCI
	* CONFIG_MMC_SDHCI_OMAP		(for DRA7XX and AM57XX devices)
	* CONFIG_MMC_OMAP		(for AM335X and AM437X devices)

   .. rubric:: **Building as Loadable Kernel Module**

   Depending on your configuration, any of the above options can be set to 'm'
   to build them as a module. Use the following command to install all modules
   tp your filesystem.

   ::

      # sudo -E make modules_install ARCH=arm INSTALL_MOD_PATH=path/to/filesystem

   Boot the kernel upto kernel prompt and use modprobe to insert the driver
   module and all its dependencies.

   ::

      # modprobe sdhci-omap		(for DRA7XX and AM57XX devices)
      # modprobe omap_hsmmc		(for AM335X and AM437X devices)

   If 'udev' is running and the SD card is already inserted, the devices
   nodes will be created and filesystem will be automatically mounted if
   exists on the card.

.. ifconfig:: CONFIG_part_family in ('J7_family')

   The default kernel configuration enables support for MMC/SD driver as
   built-in to kernel. TI SDHCI driver is used. Following options need to be
   configured in Linux Kernel for successfully selecting SDHCI driver for
   |__PART_FAMILY_DEVICE_NAMES__|.

   - Enable SDHCI support (CONFIG_MMC_SDHCI)

   .. code-block:: text

      Device Drivers -->
         MMC/SD/SDIO card support -->
            <*> Secure Digital Host Controller Interface support

   - Enable SDHCI platform helper (CONFIG_MMC_SDHCI_PLTFM)

   .. code-block:: text

      Device Drivers -->
         MMC/SD/SDIO card support -->
            Secure Digital Host Controller Interface support -->
               <*> SDHCI platform and OF driver helper

   - Enable SDHCI controller for TI device (CONFIG_MMC_SDHCI_AM654)

   .. code-block:: text

      Device Drivers -->
         MMC/SD/SDIO card support -->
            <*> Support for the SDHCI Controller in TI's AM654 SOCs

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family')

   .. rubric:: **Enabling eMMC Card Background operations support**
      :name: enabling-emmc-card-background-operations-support

   | eMMC cards need to occasionally spend some time cleaning up garbage
     and perform cache/buffer related operations which are strictly on the
     card side and do not involve the host. These operations are at various
     levels based on the importance/severity of the operation 1- Normal, 2-
     Important and 3 - Critical. If an operation is delayed for long it
     becomes critical and the regular read/write from host can be delayed
     or take more time than expected.
   | To avoid such issues the MMC HW and core driver provide a framework
     which can check for pending background operations and give the card
     some time to clear up the same.
   | This feature is already part of the framework and to start using it
     the User needs to enable EXT\_CSD : BKOPS\_EN [163] BIT 0.

   **This can be done using the "mmc-utils" tool from user space or using
   the "mmc" command in U-boot.**

   Command to enable bkops from userspace using mmc-utils, assuming eMMC
   instance to be mmcblk0

   ::

       root@dra7xx-evm:mmc bkops enable /dev/mmcblk0

   You can find the instance of eMMC by reading the ios timing spec form
   debugfs

   ::

       root@dra7xx-evm:~# cat /sys/kernel/debug/mmc0/ios
       ----
       timing spec:    9 (mmc HS200)
       ---

   or by looking for boot partitions, eMMC has two bootpartitions
   mmcblk<x>boot0 and mmcblk<x>boot1

   ::

       root@dra7xx-evm:/# ls /dev/mmcblk*boot*
       /dev/mmcblk0boot0  /dev/mmcblk0boot1

Steps for working around SD card issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In some cases failure can be seen while using some SD cards,

#. Kernel fails to enumerate SD, thus failing to mount the root file
   system. This is the case when kernel hangs during boot with a message
   similar to the following,

    ::

        [    2.563279] Waiting for root device PARTUUID=835b171b-02...


#. A lot of SDHCI register dumps logs getting printed continuously,

    ::

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

Given below are the list of various workarounds that can be done in the
device tree node to get SD card working. The workarounds are ordered in
increasing order of reducing performance.

All the changes mentioned below, are to be done in the MMCSD device tree node
corresponding to the SD instance. This is usually the first (index starting
from zero) instance.

#. Restricting to a given speed mode

   - By default the kernel driver tries to enumerate a SD card in the highest
     supported speed mode. Given below is the order in which the driver
     tries to enumerate a SD card

      - SDR104
      - DDR50
      - SDR50
      - SD HS
      - SD legacy

   - These speed capabilites can be masked using device tree property
     sdhci-caps-mask.

      - Limit to DDR50: ``sdhci-caps-mask = <0x00000002 0x00000000>``
      - Limit to SDR50: ``sdhci-caps-mask = <0x00000006 0x00000000>``
      - Limit to SD HS: ``sdhci-caps-mask = <0x00000007 0x00000000>``
      - Limit to SD legacy: ``sdhci-caps-mask = <0x00000007 0x00200000>``

          ::

              &sdhci1 {
                  /* SD/MMC */
                 vmmc-supply = <&vdd_mmc1>;
                 vqmmc-supply = <&vdd_sd_dv>;
                 pinctrl-names = "default";
                 pinctrl-0 = <&main_mmc1_pins_default>;
                 ti,driver-strength-ohm = <50>;
                 disable-wp;
                 sdhci-caps-mask = <0x00000006 0x00000000>; /* Limiting to SDR50 speed mode */
              };

      - Limiting to SD HS speed mode can also be done by using the property
        ``no-1-8-v``. This disable switching to 1.8V which is required for
        UHS speed modes(SDR104, DDR50, SDR50)

          ::

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

  - The SD interface supports a bus width of 4. It can be reduced to 1 by
    changing the ``bus-width`` device tree property from 4 to 1.

      ::

          diff --git a/arch/arm64/boot/dts/ti/k3-am62-main.dtsi b/arch/arm64/boot/dts/ti/k3-am62-main.dtsi
          index 7bbfcb158842..2ef974f7206f 100644
          --- a/arch/arm64/boot/dts/ti/k3-am62-main.dtsi
          +++ b/arch/arm64/boot/dts/ti/k3-am62-main.dtsi
          @@ -424,7 +424,7 @@
                          ti,itap-del-sel-sdr12 = <0x0>;
                          ti,itap-del-sel-sdr25 = <0x0>;
                          ti,clkbuf-sel = <0x7>;
          -               bus-width = <4>;
          +               bus-width = <1>;
           };

           sdhci2: mmc@fa20000 {
