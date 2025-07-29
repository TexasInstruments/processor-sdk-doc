OSPI/QSPI NOR/NAND
------------------

.. rubric:: Introduction
   :name: u-boot-introduction-qspi-ug

Octal Serial Peripheral Interface (OSPI) and Quad Serial Peripheral Interface
(QSPI) are SPI modules that have x8 IO lines and x4 IO lines respectively.
These controllers are mainly used to interface with Octal and Quad SPI flashes.
OSPI is backward compatible with QSPI. These modules can also work in dual (x2)
and single (x1) modes. OSPI and QSPI controllers on TI SoCs support memory
mapped IO interface, which provide a direct interface for accessing data from
the external SPI flash, thereby simplifying software requirements. These
controllers work only in master mode.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   +------------+------------+------------------------------------+
   | SoC Family | Capability | Driver                             |
   +============+============+====================================+
   | AM64x      | OSPI NOR   | :file:`drivers/spi/cadence_qspi.c` |
   +------------+------------+------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   +-------------+------------+------------------------------------+
   | SoC Family  | Capability | Driver                             |
   +=============+============+====================================+
   | AM62x SK    | OSPI NOR   | :file:`drivers/spi/cadence_qspi.c` |
   +-------------+------------+------------------------------------+
   | AM62x LP SK | OSPI NAND  | :file:`drivers/spi/cadence_qspi.c` |
   +-------------+------------+------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   +-------------+------------+------------------------------------+
   | SoC Family  | Capability | Driver                             |
   +=============+============+====================================+
   |             | OSPI NOR   | :file:`drivers/spi/cadence_qspi.c` |
   + AM62Lx EVM  +------------+------------------------------------+
   |             | QSPI NAND  | :file:`drivers/spi/cadence_qspi.c` |
   +-------------+------------+------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   +------------+------------+------------------------------------+
   | SoC Family | Capability | Driver                             |
   +============+============+====================================+
   | AM62Ax     | OSPI NAND  | :file:`drivers/spi/cadence_qspi.c` |
   +------------+------------+------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J7200')

   +--------------+------------+------------------------------------+
   | SoC Family   | Capability | Driver                             |
   +==============+============+====================================+
   | AM62Px/J7200 | OSPI NOR   | :file:`drivers/spi/cadence_qspi.c` |
   +--------------+------------+------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J721E')

   +-------------+--------------+------------------------------------+
   | SoC Family  | Capability   | Driver                             |
   +=============+==============+====================================+
   | AM654/J721e | 1x QSPI NOR, | :file:`drivers/spi/cadence_qspi.c` |
   |             | 1x OSPI NOR  |                                    |
   +-------------+--------------+------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J722S')

   +------------+--------------+------------------------------------+
   | SoC Family | Capability   | Driver                             |
   +============+==============+====================================+
   |            | 1x OSPI NOR  | :file:`drivers/spi/cadence_qspi.c` |
   + J722S      +--------------+------------------------------------+
   |            | 1x OSPI NAND | :file:`drivers/spi/cadence_qspi.c` |
   +------------+--------------+------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J721S2', 'J784S4','J742S2')

   +---------------+--------------+------------------------------------+
   | SoC Family    | Capability   | Driver                             |
   +===============+==============+====================================+
   |               | 1x QSPI NOR, | :file:`drivers/spi/cadence_qspi.c` |
   | J721S2/J784S4 | 1x OSPI NOR  |                                    |
   +               +--------------+------------------------------------+
   |               | 1x OSPI NAND | :file:`drivers/spi/cadence_qspi.c` |
   +---------------+--------------+------------------------------------+

.. ifconfig:: CONFIG_part_variant not in ('AM57X')

   .. note::

      Not all OSPI flashes can be supported. Users are recommended to check
      whether or not the OSPI flash part chosen for custom board designs meets all
      the criteria listed at https://e2e.ti.com/support/processors/f/791/t/946418

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'AM64X')

   .. important::

      Apply this `patch <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2025.01-next&id=3d64c9fb4274ff1c7cbc7a2c8e8e33790b923bc6>`__
      as it's not added with the ``11.01`` SDK release.

.. rubric:: Driver Features

OSPI controllers supports PHY Calibration in DQS + Double Data Rate (DDR) mode
for OSPI/QSPI NOR flashes in Octal configuration wherein data can be read on
both edges of the clock, and non-DQS + Single Data Rate (SDR) mode for
OSPI/QSPI NAND flashes in Quad and Octal configuration.

.. rubric:: Memory mapped read support
   :name: u-boot-memory-mapped-read-support

Once the controller is configured in memory map mode, the whole
flash memory is made available as a memory region at an SoC specific address.
This region can be accessed using normal memcpy() (or mem-to-mem dma
copy). Controller hardware will internally communicate with
SPI flash over SPI bus and get the requested data. This mode provides
the best throughput and is the default mode in the SDK.

.. rubric:: Supported SPI modes
   :name: u-boot-supported-spi-modes

The :file:`cadence_qspi.c` driver supports standard SPI mode 0 only.

.. rubric:: DMA support
   :name: u-boot-dma-support

The driver uses mem-to-mem DMA copy on top of an OSPI/QSPI memory mapped port
during flash read operations for maximum throughput and reduced CPU load.

The OSPI Controller does not support interfacing with non-flash SPI slaves.

.. rubric:: Driver Configuration
   :name: u-boot-driver-configuration-qspi

.. rubric:: Source Location
   :name: u-boot-source-location-qspi

OSPI driver is at: :file:`drivers/spi/cadence_qspi.c` under U-Boot source tree.
This driver also supports QSPI version of the same IP.

.. rubric:: DT Configuration
   :name: dt-configuration-u-boot-qspi

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'AM62X', 'AM62PX', 'J7200', 'J721E', 'J722S', 'J721S2', 'J784S4','J742S2')

   The following is an example device-tree node for an OSPI NOR device

   .. code-block:: dts

      &ospi0 {

         flash@0{
            compatible = "jedec,spi-nor";
            reg = <0x0>;
            spi-tx-bus-width = <8>;
            spi-rx-bus-width = <8>;
            spi-max-frequency = <25000000>;
            cdns,tshsl-ns = <60>;
            cdns,tsd2d-ns = <60>;
            cdns,tchsh-ns = <60>;
            cdns,tslch-ns = <60>;
            cdns,read-delay = <4>;

            partitions {
               compatible = "fixed-partitions";
               #address-cells = <1>;
               #size-cells = <1>;
               bootph-all;

               partition@0 {
                  label = "ospi.tiboot3";
                  reg = <0x00 0x80000>;
               };

               partition@80000 {
                  label = "ospi.tispl";
                  reg = <0x80000 0x200000>;
               };

               // other partitions
            };
         };
      };

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'J722S', 'J721S2', 'J784S4','J742S2')

   The following is an example device-tree node for an OSPI NAND device

   .. code-block:: dts

      &ospi0 {

         flash@0 {
            compatible = "spi-nand";
            reg = <0x0>;
            spi-tx-bus-width = <8>;
            spi-rx-bus-width = <8>;
            spi-max-frequency = <25000000>;
            cdns,tshsl-ns = <60>;
            cdns,tsd2d-ns = <60>;
            cdns,tchsh-ns = <60>;
            cdns,tslch-ns = <60>;
            cdns,read-delay = <2>;

            partitions {
               compatible = "fixed-partitions";
               #address-cells = <1>;
               #size-cells = <1>;

               partition@0 {
                  label = "ospi_nand.tiboot3";
                  reg = <0x0 0x80000>;
               };

               partition@80000 {
                  label = "ospi_nand.tispl";
                  reg = <0x80000 0x200000>;
               };

               // other partitions
            };
         };
      };

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   The following is an example device-tree node for an OSPI NOR device

   .. code-block:: dts

      &ospi0 {

         flash@0{
            compatible = "jedec,spi-nor";
            reg = <0x0>;
            spi-tx-bus-width = <8>;
            spi-rx-bus-width = <8>;
            spi-max-frequency = <25000000>;
            cdns,tshsl-ns = <60>;
            cdns,tsd2d-ns = <60>;
            cdns,tchsh-ns = <60>;
            cdns,tslch-ns = <60>;
            cdns,read-delay = <4>;

            partitions {
               compatible = "fixed-partitions";
               #address-cells = <1>;
               #size-cells = <1>;
               bootph-all;

               partition@0 {
                  label = "ospi.tiboot3";
                  reg = <0x00 0x80000>;
               };

               partition@80000 {
                  label = "ospi.tispl";
                  reg = <0x80000 0x200000>;
               };

               // other partitions
            };
         };
      };

   The following is an example device-tree node for an QSPI NAND device

   .. code-block:: dts

      &ospi0 {

         flash@0 {
            compatible = "spi-nand";
            reg = <0x0>;
            spi-tx-bus-width = <4>;
            spi-rx-bus-width = <4>;
            spi-max-frequency = <25000000>;
            cdns,tshsl-ns = <60>;
            cdns,tsd2d-ns = <60>;
            cdns,tchsh-ns = <60>;
            cdns,tslch-ns = <60>;
            cdns,read-delay = <2>;

            partitions {
               compatible = "fixed-partitions";
               #address-cells = <1>;
               #size-cells = <1>;

               partition@0 {
                  label = "ospi_nand.tiboot3";
                  reg = <0x0 0x80000>;
               };

               partition@80000 {
                  label = "ospi_nand.tispl";
                  reg = <0x80000 0x200000>;
               };

               // other partitions
            };
         };
      };

Flash properties:

1. **compatible:** specifies the compatible string for the device, the operating
   system uses this string to identify and the match the driver for the device.
   Use 'jedec,spi-nor' for OSPI/QSPI NOR flashes and 'spi-nand' for OSPI/QSPI
   NAND flashes.

2. **spi-tx-bus-width and spi-rx-bus-width:** specifies the bus width in bits for
   SPI transactions when transmitting (tx) and receiving (rx) data. Set for '8'
   for OSPI flashes and '4' for QSPI flashes.

3. **spi-max-frequency:** defines the maximum frequency in Hertz at which the SPI
   bus can operate. Set 1/4th or 1/8th of 'assigned-clocks' value of 'ospi0'
   node for SDR and DDR mode respectively. If PHY Calibration is enabled, this
   value is ignored, and the maximum frequency is determined by the value
   specified in the 'assigned-clocks' property of 'ospi0' node.

4. **cdns,read-delay:** specifies the delay in clock cycles between the fetch of a
   command and responding to that command by the flash devices. This differs
   with flashes, try with different read delays starting from 0 and find the
   minimum read-delay at which the flash driver probes correctly.

.. note::

    The :command:`sf` command is used to access SPI NOR flash, supporting
    read/write/erase and a few other functions. For more information on sf
    command in U-boot please refer to the u-boot documentation:
    `here <https://u-boot.readthedocs.io/en/latest/usage/cmd/sf.html>`__.
    And for accessing SPI NAND flash, the :command:`mtd` command is used,
    supporting read/write/erase and bad block management.

.. ifconfig:: CONFIG_part_variant in ('AM65X', 'J721E')

    ROM supports booting from OSPI from offset 0x0.

    **Flashing Images to OSPI**

    Below commands can be used to download tiboot3.bin, tispl.bin and
    u-boot.img over tftp and then flash it to OSPI at respective addresses.

    .. code-block:: console

      => sf probe
      => tftp ${loadaddr} tiboot3.bin
      => sf update $loadaddr 0x0 $filesize
      => tftp ${loadaddr} tispl.bin
      => sf update $loadaddr 0x80000 $filesize
      => tftp ${loadaddr} u-boot.img
      => sf update $loadaddr 0x280000 $filesize
      => tftp ${loadaddr} sysfw.itb
      => sf update $loadaddr 0x6C0000 $filesize

    **PHY Calibration**

    PHY calibration allows for higher read performance. To enable PHY, the PHY
    calibration pattern must be flashed to OSPI at the start of the last erase
    sector. For the Micron MT35XU512ABA flash, this lies at the address 0x3fe0000.

    Download the binary file containing the PHY pattern from :download:`here </files/ospi_phy_pattern>`.
    Below commands can be used to flash the PHY pattern, with the location of the
    pattern depending on which flash is being used:

    .. code-block:: console

       => sf probe
       => tftp ${loadaddr} ospi_phy_pattern
       => sf update $loadaddr 0x3fe0000 $filesize

    **Flash Layout for OSPI**

    .. code-block:: console

             0x0 +----------------------------+
                 |     ospi.tiboot3(512K)     |
                 |                            |
         0x80000 +----------------------------+
                 |     ospi.tispl(2M)         |
                 |                            |
        0x280000 +----------------------------+
                 |     ospi.u-boot(4M)        |
                 |                            |
        0x680000 +----------------------------+
                 |     ospi.env(128K)         |
                 |                            |
        0x6A0000 +----------------------------+
                 |   ospi.env.backup (128K)   |
                 |                            |
        0x6C0000 +----------------------------+
                 |      ospi.sysfw(1M)        |
                 |                            |
        0x7C0000 +----------------------------+
                 |      padding (256k)        |
        0x800000 +----------------------------+
                 |     ospi.rootfs(UBIFS)     |
                 |                            |
       0x3FE0000 +----------------------------+
                 |   ospi.phypattern (128k)   |
                 |                            |
                 +----------------------------+

    Kernel Image and DT are expected to be present in the /boot folder of UBIFS
    ospi.rootfs just like in SD card case. U-Boot looks for UBI volume named
    "rootfs" for rootfs.

    To boot kernel from OSPI, at the U-Boot prompt:

    .. code-block:: console

      => setenv boot ubi
      => boot

    **Writing to OSPI using DFU**

    Setup: Connect the Type C port (USB0 port) of EVM to ubuntu host PC. Make sure
    dfu-util tool is installed and USB0 port is in UFP/DRP mode: SW3[3:4] = 01 or 1x.

    .. code-block:: console

         #sudo apt-get install dfu-util

    From u-boot(for OSPI flash):

    .. code-block:: console

        U-Boot # env default -a
        U-Boot # setenv dfu_alt_info ${dfu_alt_info_ospi}; dfu 0 sf "0:0:25000000:0"

    From u-boot(for QSPI flash):

    .. code-block:: console

        U-Boot # env default -a
        U-Boot # setenv dfu_alt_info ${dfu_alt_info_ospi}; dfu 0 sf "1:0:40000000:0"

    From ubuntu PC: Using dfu-util utilities to flash the binares to OSPI/QSPI flash.

    .. code-block:: console

        # sudo dfu-util -l
        Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
        Copyright 2010-2016 Tormod Volden and Stefan Schmidt
        This program is Free Software and has ABSOLUTELY NO WARRANTY
        Found DFU: [0451:6163] ver=0224, devnum=75, cfg=1, intf=0, path="1-5", alt=5, name="rootfs", serial="0000000000000110"
        Found DFU: [0451:6163] ver=0224, devnum=75, cfg=1, intf=0, path="1-5", alt=4, name="sysfw.itb", serial="0000000000000110"
        Found DFU: [0451:6163] ver=0224, devnum=75, cfg=1, intf=0, path="1-5", alt=3, name="u-boot-env", serial="0000000000000110"
        Found DFU: [0451:6163] ver=0224, devnum=75, cfg=1, intf=0, path="1-5", alt=2, name="u-boot.img", serial="0000000000000110"
        Found DFU: [0451:6163] ver=0224, devnum=75, cfg=1, intf=0, path="1-5", alt=1, name="tispl.bin", serial="0000000000000110"
        Found DFU: [0451:6163] ver=0224, devnum=75, cfg=1, intf=0, path="1-5", alt=0, name="tiboot3.bin", serial="0000000000000110""

    Flash the binaries to the respective regions using alternate interface
    number (alt=<x>).

    .. code-block:: console

        # sudo dfu-util -c 1 -i 0 -a 0 -D tiboot3.bin
        # sudo dfu-util -c 1 -i 0 -a 1 -D tispl.bin
        # sudo dfu-util -c 1 -i 0 -a 2 -D u-boot.img
        # sudo dfu-util -c 1 -i 0 -a 3 -D sysfw.itb

.. ifconfig:: CONFIG_part_variant in ('J7200')

    j7200 is largely similar to j721e and am654. the major differences are that it
    has the cypress s28hs512t flash and sysfw is bundled with tiboot3.bin.

    **flashing images to ospi**

    below commands can be used to download tiboot3.bin, tispl.bin and
    u-boot.img over tftp and then flash it to ospi at respective addresses.

    .. code-block:: console

      => sf probe
      => tftp ${loadaddr} tiboot3.bin
      => sf update $loadaddr 0x0 $filesize
      => tftp ${loadaddr} tispl.bin
      => sf update $loadaddr 0x100000 $filesize
      => tftp ${loadaddr} u-boot.img
      => sf update $loadaddr 0x300000 $filesize

    **phy calibration**

    phy calibration allows for higher read performance. to enable phy, the phy
    calibration pattern must be flashed to ospi at the start of the last erase
    sector. for the cypress s28hs512t flash, this lies at the address 0x3fc0000.

    download the binary file containing the phy pattern from :download:`here </files/ospi_phy_pattern>`.
    below commands can be used to flash the phy pattern, with the location of the
    pattern depending on which flash is being used:

    .. code-block:: console

       => sf probe
       => tftp ${loadaddr} ospi_phy_pattern
       => sf update $loadaddr 0x3fc0000 $filesize

    **flash layout for ospi**

    .. code-block:: console

             0x0 +----------------------------+
                 |     ospi.tiboot3(1m)       |
                 |                            |
        0x100000 +----------------------------+
                 |     ospi.tispl(2m)         |
                 |                            |
        0x300000 +----------------------------+
                 |     ospi.u-boot(4m)        |
                 |                            |
        0x700000 +----------------------------+
                 |     ospi.env(128k)         |
                 |                            |
        0x720000 +----------------------------+
                 |   ospi.env.backup(128k)    |
                 |                            |
        0x740000 +----------------------------+
                 |      padding (768k)        |
        0x800000 +----------------------------+
                 |     ospi.rootfs(ubifs)     |
                 |                            |
       0x3fc0000 +----------------------------+
                 |   ospi.phypattern (256k)   |
                 |                            |
                 +----------------------------+

    **Writing to OSPI using DFU**

    Setup: Connect the Type C port (USB0 port) of EVM to ubuntu host PC. Make sure
    dfu-util tool is installed and USB0 port is in UFP/DRP mode: SW3[3:4] = 01 or 1x.

    .. code-block:: console

         #sudo apt-get install dfu-util

    From u-boot:

    .. code-block:: console

        U-Boot # env default -a
        U-Boot # setenv dfu_alt_info ${dfu_alt_info_ospi}; dfu 0 sf "0:0:25000000:0"

    From ubuntu PC: Using dfu-util utilities to flash the binares to QSPI flash.

    .. code-block:: console

        # sudo dfu-util -l
        Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
        Copyright 2010-2016 Tormod Volden and Stefan Schmidt
        This program is Free Software and has ABSOLUTELY NO WARRANTY
        Found DFU: [0451:6164] ver=0224, devnum=77, cfg=1, intf=0, path="1-5", alt=4, name="rootfs", serial="0000000000000005"
        Found DFU: [0451:6164] ver=0224, devnum=77, cfg=1, intf=0, path="1-5", alt=3, name="u-boot-env", serial="0000000000000005"
        Found DFU: [0451:6164] ver=0224, devnum=77, cfg=1, intf=0, path="1-5", alt=2, name="u-boot.img", serial="0000000000000005"
        Found DFU: [0451:6164] ver=0224, devnum=77, cfg=1, intf=0, path="1-5", alt=1, name="tispl.bin", serial="0000000000000005"
        Found DFU: [0451:6164] ver=0224, devnum=77, cfg=1, intf=0, path="1-5", alt=0, name="tiboot3.bin", serial="0000000000000005"

    Flash the binaries to the respective regions using alternate interface
    number (alt=<x>).

    .. code-block:: console

        # sudo dfu-util -c 1 -i 0 -a 0 -D tiboot3.bin
        # sudo dfu-util -c 1 -i 0 -a 1 -D tispl.bin
        # sudo dfu-util -c 1 -i 0 -a 2 -D u-boot.img

.. ifconfig:: CONFIG_part_variant in ('AM64X')

    AM64x has a Cypress S28HS512T OSPI NOR flash and SYSFW is bundled with
    :file:`tiboot3.bin`.

    Below are two methods which can be used to flash the OSPI NOR device. For
    all methods, we will load the bootloaders into memory and then flash each
    to OSPI NOR at the respective addresses.

    **Flashing Images to OSPI NOR using TFTP server**

    In this example, we'll use the ``tftp-hpa`` package from Ubuntu for our
    tftp server. Assume bootloader names are :file:`tiboot3.bin`,
    :file:`tispl.bin`, :file:`u-boot.img`. Verify ethernet connection between
    AM64x and host machine before proceeding.

    1. Setup TFTP server in Host machine

       .. code-block:: console

          # For complete instructions refer to: https://help.ubuntu.com/community/TFTP
          $ sudo apt install tftp-hpa
          $ sudo vi /etc/default/tftpd-hpa # optional to change tftp directory and other options
          $ sudo chown -R tftp /tftp # change owner/group of new directory /tftp
          $ sudo systemctl restart tftpd-hpa # restart server

    2. Setup U-boot environment for AM64x

       .. code-block:: console

          # Boot to U-boot prompt using a working boot method
          => setenv ipaddr <ip-address-of-am64x>
          => setenv serverip <ip-address-of-tftp-server>
          => saveenv # optional to save the U-boot ENV

    3. Use tftp command to load the bootloaders into memory and flash to OSPI
       NOR

       .. code-block:: console

          => sf probe
          => tftp ${loadaddr} tiboot3.bin
          => sf update $loadaddr 0x0 $filesize
          => tftp ${loadaddr} tispl.bin
          => sf update $loadaddr 0x100000 $filesize
          => tftp ${loadaddr} u-boot.img
          => sf update $loadaddr 0x300000 $filesize

    4. Change boot mode pins to OSPI boot mode and reboot AM64x

    **Flashing images to OSPI NOR using SD card**

    In this example, load binaries from SD card. Assume bootloader names are
    :file:`tiboot3.bin`, :file:`tispl.bin`, :file:`u-boot.img`. Boot via SD
    card boot and stop at U-boot prompt before procceeding.

    1. Use fatload command to load the bootloaders into memory and flash to
       OSPI NOR

       .. code-block:: console

          => sf probe
          => fatload mmc 1 ${loadaddr} tiboot3.bin
          => sf update $loadaddr 0x0 $filesize
          => fatload mmc 1 ${loadaddr} tispl.bin
          => sf update $loadaddr 0x100000 $filesize
          => fatload mmc 1 ${loadaddr} u-boot.img
          => sf update $loadaddr 0x300000 $filesize

    2. Change boot mode pins to OSPI boot mode and reboot AM64x

    **OSPI Boot Mode**

    Please refer to the AM64x TRM Section 4.4 for more information.

    **Phy Calibration**

    Phy Calibration allows for higher read performance. To enable phy, the phy
    calibration pattern must be flashed to OSPI at the start of the last erase
    sector. For the Cypress S28HS512T flash, this lies at the address 0x3FC0000.
    The partition name should be 'ospi.phypattern' as the driver looks for it
    before PHY Calibration.

    Download the binary file containing the phy pattern from :download:`here </files/ospi_phy_pattern>`.
    The commands below can be used to flash the phy pattern, with the location
    of the pattern depending on which flash is being used:

    .. code-block:: console

       => sf probe
       => tftp ${loadaddr} ospi_phy_pattern
       => sf update $loadaddr 0x3fc0000 $filesize

    **Flash layout for OSPI NOR**

    .. code-block:: text

       +---------------------+ 0x0
       |   ospi.tiboot3      |
       |   (1m)              |
       +---------------------+ 0x100000
       |   ospi.tispl        |
       |   (2m)              |
       +---------------------+ 0x300000
       |   ospi.u-boot       |
       |   (4m)              |
       +---------------------+ 0x700000
       |   ospi.env          |
       |   (256k)            |
       +---------------------+ 0x740000
       |   ospi.env.backup   |
       |   (256k)            |
       +---------------------+ 0x780000
       |   padding           |
       |   (512k)            |
       +---------------------+ 0x800000
       |   ospi.rootfs       |
       |   (55m)(ubifs)      |
       +---------------------+ 0x3FC0000
       |   ospi.phypattern   |
       |   (256k)            |
       +---------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    **AM62x SK**

    AM62x Starter Kit (SK) has a Cypress S28HS512T OSPI NOR flash and SYSFW is
    bundled with :file:`tiboot3.bin`.

    Below are two methods which can be used to flash the OSPI NOR device. For
    all methods, we will load the bootloaders into memory and then flash each
    to OSPI NOR at the respective addresses.

    **Flashing Images to OSPI NOR using TFTP server**

    In this example, we'll use the ``tftp-hpa`` package from Ubuntu for our
    tftp server. Assume bootloader names are :file:`tiboot3.bin`,
    :file:`tispl.bin`, :file:`u-boot.img`. Verify ethernet connection between
    AM62x SK and host machine before proceeding.

    1. Setup TFTP server in Host machine

       .. code-block:: console

          # For complete instructions refer to: https://help.ubuntu.com/community/TFTP
          $ sudo apt install tftp-hpa
          $ sudo vi /etc/default/tftpd-hpa # optional to change tftp directory and other options
          $ sudo chown -R tftp /tftp # change owner/group of new directory /tftp
          $ sudo systemctl restart tftpd-hpa # restart server

    2. Setup U-boot environment for AM62x SK

       .. code-block:: console

          # Boot to U-boot prompt using a working boot method
          => setenv ipaddr <ip-address-of-am62x-sk>
          => setenv serverip <ip-address-of-tftp-server>
          => saveenv # optional to save the U-boot ENV

    3. Use tftp command to load the bootloaders into memory and flash to OSPI
       NOR

       .. code-block:: console

          => sf probe
          => tftp ${loadaddr} tiboot3.bin
          => sf update $loadaddr 0x0 $filesize
          => tftp ${loadaddr} tispl.bin
          => sf update $loadaddr 0x80000 $filesize
          => tftp ${loadaddr} u-boot.img
          => sf update $loadaddr 0x280000 $filesize

    4. Change boot mode pins to OSPI boot mode and reboot AM62x SK

    **Flashing images to OSPI NOR using SD card**

    In this example, load binaries from SD card. Assume bootloader names are
    :file:`tiboot3.bin`, :file:`tispl.bin`, :file:`u-boot.img`. Boot via SD
    card boot and stop at U-boot prompt before procceeding.

    1. Use fatload command to load the bootloaders into memory and flash to
       OSPI NOR

       .. code-block:: console

          => sf probe
          => fatload mmc 1 ${loadaddr} tiboot3.bin
          => sf update $loadaddr 0x0 $filesize
          => fatload mmc 1 ${loadaddr} tispl.bin
          => sf update $loadaddr 0x80000 $filesize
          => fatload mmc 1 ${loadaddr} u-boot.img
          => sf update $loadaddr 0x280000 $filesize

    2. Change boot mode pins to OSPI boot mode and reboot AM62x SK

    **OSPI Boot Mode**

    Please refer to the AM62x TRM Section 5.4 for more information.

    **Phy Calibration**

    Phy Calibration allows for higher read performance. To enable phy, the phy
    calibration pattern must be flashed to OSPI at the start of the last erase
    sector. For the Cypress S28HS512T flash, this lies at the address 0x3FC0000.
    The partition name should be 'ospi.phypattern' as the driver looks for it
    before PHY Calibration.

    Download the binary file containing the phy pattern from :download:`here </files/ospi_phy_pattern>`.
    The commands below can be used to flash the phy pattern, with the location
    of the pattern depending on which flash is being used:

    .. code-block:: console

       => sf probe
       => tftp ${loadaddr} ospi_phy_pattern
       => sf update $loadaddr 0x3fc0000 $filesize

    **Flash layout for OSPI NOR**

    .. code-block:: text

       +---------------------+ 0x0
       |   ospi.tiboot3      |
       |   (512k)            |
       +---------------------+ 0x80000
       |   ospi.tispl        |
       |   (2m)              |
       +---------------------+ 0x280000
       |   ospi.u-boot       |
       |   (4m)              |
       +---------------------+ 0x680000
       |   ospi.env          |
       |   (256k)            |
       +---------------------+ 0x6C0000
       |   ospi.env.backup   |
       |   (256k)            |
       +---------------------+ 0x700000
       |   padding           |
       |   (1m)              |
       +---------------------+ 0x800000
       |   ospi.rootfs       |
       |   (55m)(ubifs)      |
       +---------------------+ 0x3FC0000
       |   ospi.phypattern   |
       |   (256k)            |
       +---------------------+

    **AM62x LP SK**

    AM62x Low Power Starter Kit (LP-SK) has a Winbond W35N01JW OSPI NAND flash
    and SYSFW is bundled with :file:`tiboot3.bin`.

    Below are two methods which can be used to flash the OSPI NAND device.
    For all methods, we will load the bootloaders into memory and then flash
    each to OSPI NAND at the respective addresses.

    **Flashing Images to OSPI NAND using TFTP server**

    In this example, we'll use the ``tftp-hpa`` package from Ubuntu for our
    tftp server. Assume bootloader names are :file:`tiboot3.bin`,
    :file:`tispl.bin`, :file:`u-boot.img`. Verify ethernet connection between
    AM62x LP-SK and host machine before proceeding.

    1. Setup TFTP server in Host machine

       .. code-block:: console

          # For complete instructions refer to: https://help.ubuntu.com/community/TFTP
          $ sudo apt install tftp-hpa
          $ sudo vi /etc/default/tftpd-hpa # optional to change tftp directory and other options
          $ sudo chown -R tftp /tftp # change owner/group of new directory /tftp
          $ sudo systemctl restart tftpd-hpa # restart server

    2. Setup U-boot environment for AM62x LP-SK

       .. code-block:: console

          # Boot to U-boot prompt using a working boot method
          => setenv ipaddr <ip-address-of-am62x-lp-sk>
          => setenv serverip <ip-address-of-tftp-server>
          => saveenv # optional to save the U-boot ENV

    3. Use tftp command to load the bootloaders into memory and flash to OSPI
       NAND

       .. code-block:: console

          => mtd list
          => tftp ${loadaddr} tiboot3.bin
          => mtd write spi-nand0 $loadaddr 0x0 $filesize
          => tftp ${loadaddr} tispl.bin
          => mtd write spi-nand0 $loadaddr 0x80000 $filesize
          => tftp ${loadaddr} u-boot.img
          => mtd write spi-nand0 $loadaddr 0x280000 $filesize

    4. Change boot mode pins to boot with Serial NAND boot mode and reboot
       AM62x LP-SK

    **Flashing images to OSPI NAND using SD card**

    In this example, load binaries from SD card. Assume bootloader names are
    :file:`tiboot3.bin`, :file:`tispl.bin`, :file:`u-boot.img`. Boot via SD
    card boot and stop at U-boot prompt before procceeding.

    1. Use fatload command to load the bootloaders into memory and flash to
       OSPI NAND

    .. code-block:: console

       => mtd list
       => fatload mmc 1 ${loadaddr} tiboot3.bin
       => mtd write spi-nand0 $loadaddr 0x0 $filesize
       => fatload mmc 1 ${loadaddr} tispl.bin
       => mtd write spi-nand0 $loadaddr 0x80000 $filesize
       => fatload mmc 1 ${loadaddr} u-boot.img
       => mtd write spi-nand0 $loadaddr 0x280000 $filesize

    2. Change boot mode pins to boot with Serial NAND boot mode and reboot
    AM62x LP-SK

    **Serial NAND Boot Mode**

    Please refer to the AM62x TRM Section 5.4 for more information. Both OSPI
    NAND and QSPI NAND lie under Serial NAND Boot mode.

    **Phy Calibration**

    Phy Calibration allows for higher read and write performance. To enable
    phy, the phy calibration pattern must be flashed to OSPI NAND at the start
    of the last erase block. For the Winbond W35N01JW flash, this lies at the
    address 0x7FC0000. The partition name should be 'ospi_nand.phypattern' as
    the driver looks for it before PHY Calibration.

    Download the binary file containing the phy pattern from :download:`here </files/ospi_phy_pattern>`.
    The commands below can be used to flash the phy pattern, with the location
    of the pattern depending on which flash is being used:

    .. code-block:: console

       => mtd list
       => tftp ${loadaddr} ospi_phy_pattern
       => mtd write spi-nand0 $loadaddr 0x7fc0000 $filesize

    **Flash layout for OSPI NAND**

    .. code-block:: text

       +--------------------------+ 0x0
       |   ospi_nand.tiboot3      |
       |   (512k)                 |
       +--------------------------+ 0x80000
       |   ospi_nand.tispl        |
       |   (2m)                   |
       +--------------------------+ 0x280000
       |   ospi_nand.u-boot       |
       |   (4m)                   |
       +--------------------------+ 0x680000
       |   ospi_nand.env          |
       |   (256k)                 |
       +--------------------------+ 0x6C0000
       |   ospi_nand.env.backup   |
       |   (256k)                 |
       +--------------------------+ 0x700000
       |   padding                |
       |   (25m)                  |
       +--------------------------+ 0x2000000
       |   ospi_nand.rootfs       |
       |   (95m)(ubifs)           |
       +--------------------------+ 0x7FC0000
       |   ospi_nand.phypattern   |
       |   (256k)                 |
       +--------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

    **OSPI NOR (Boot media)**

    AM62Lx EVM has a Cypress S28HS512T OSPI NOR flash and SYSFW is bundled with
    :file:`tiboot3.bin`.

    Below are two methods which can be used to flash the OSPI NOR device. For
    all methods, we will load the bootloaders into memory and then flash each
    to OSPI NOR at the respective addresses.

    **Flashing Images to OSPI NOR using TFTP server**

    In this example, we'll use the ``tftp-hpa`` package from Ubuntu for our
    tftp server. Assume bootloader names are :file:`tiboot3.bin`,
    :file:`tispl.bin`, :file:`u-boot.img`. Verify ethernet connection between
    AM62Lx EVM and host machine before proceeding.

    1. Setup TFTP server in Host machine

       .. code-block:: console

          # For complete instructions refer to: https://help.ubuntu.com/community/TFTP
          $ sudo apt install tftp-hpa
          $ sudo vi /etc/default/tftpd-hpa # optional to change tftp directory and other options
          $ sudo chown -R tftp /tftp # change owner/group of new directory /tftp
          $ sudo systemctl restart tftpd-hpa # restart server

    2. Setup U-boot environment for AM62Lx EVM

       .. code-block:: console

          # Boot to U-boot prompt using a working boot method
          => setenv ipaddr <ip-address-of-am62lx-evm>
          => setenv serverip <ip-address-of-tftp-server>

    3. Use tftp command to load the bootloaders into memory and flash to OSPI
       NOR

       .. code-block:: console

          => sf probe
          => tftp ${loadaddr} tiboot3.bin
          => sf update $loadaddr 0x0 $filesize
          => tftp ${loadaddr} tispl.bin
          => sf update $loadaddr 0x80000 $filesize
          => tftp ${loadaddr} u-boot.img
          => sf update $loadaddr 0x280000 $filesize

    4. Change boot mode pins to OSPI boot mode and reboot AM62Lx EVM

    **Flashing images to OSPI NOR using SD card**

    In this example, load binaries from SD card. Assume bootloader names are
    :file:`tiboot3.bin`, :file:`tispl.bin`, :file:`u-boot.img`. Boot via SD
    card boot and stop at U-boot prompt before procceeding.

    1. Use fatload command to load the bootloaders into memory and flash to
       OSPI NOR

       .. code-block:: console

          => sf probe
          => fatload mmc 1 ${loadaddr} tiboot3.bin
          => sf update $loadaddr 0x0 $filesize
          => fatload mmc 1 ${loadaddr} tispl.bin
          => sf update $loadaddr 0x80000 $filesize
          => fatload mmc 1 ${loadaddr} u-boot.img
          => sf update $loadaddr 0x280000 $filesize

    2. Change boot mode pins to OSPI boot mode and reboot AM62Lx EVM

    **OSPI Boot Mode**

    Please refer to the AM62Lx TRM Section 5.4 for more information.

    **Phy Calibration**

    Phy Calibration allows for higher read performance. To enable phy, the phy
    calibration pattern must be flashed to OSPI at the start of the last erase
    sector. For the Cypress S28HS512T flash, this lies at the address 0x3FC0000.
    The partition name should be 'ospi.phypattern' as the driver looks for it
    before PHY Calibration.

    Download the binary file containing the phy pattern from :download:`here </files/ospi_phy_pattern>`.
    The commands below can be used to flash the phy pattern, with the location
    of the pattern depending on which flash is being used:

    .. code-block:: console

       => sf probe
       => tftp ${loadaddr} ospi_phy_pattern
       => sf update $loadaddr 0x3fc0000 $filesize

    **Flash layout for OSPI NOR**

    .. code-block:: text

       +---------------------+ 0x0
       |   ospi.tiboot3      |
       |   (512k)            |
       +---------------------+ 0x80000
       |   ospi.tispl        |
       |   (2m)              |
       +---------------------+ 0x280000
       |   ospi.u-boot       |
       |   (4m)              |
       +---------------------+ 0x680000
       |   ospi.env          |
       |   (256k)            |
       +---------------------+ 0x6C0000
       |   ospi.env.backup   |
       |   (256k)            |
       +---------------------+ 0x700000
       |   padding           |
       |   (1m)              |
       +---------------------+ 0x800000
       |   ospi.rootfs       |
       |   (55m)(ubifs)      |
       +---------------------+ 0x3FC0000
       |   ospi.phypattern   |
       |   (256k)            |
       +---------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    AM62Ax has a Winbond W35N01JW OSPI NAND flash and SYSFW is bundled with
    :file:`tiboot3.bin`.

    Below are two methods which can be used to flash the OSPI NAND device.
    For all methods, we will load the bootloaders into memory and then flash
    each to OSPI NAND at the respective addresses.

    **Flashing Images to OSPI NAND using TFTP server**

    In this example, we'll use the ``tftp-hpa`` package from Ubuntu for our
    tftp server. Assume bootloader names are :file:`tiboot3.bin`,
    :file:`tispl.bin`, :file:`u-boot.img`. Verify ethernet connection between
    AM62Ax and host machine before proceeding.

    1. Setup TFTP server in Host machine

       .. code-block:: console

          # For complete instructions refer to: https://help.ubuntu.com/community/TFTP
          $ sudo apt install tftp-hpa
          $ sudo vi /etc/default/tftpd-hpa # optional to change tftp directory and other options
          $ sudo chown -R tftp /tftp # change owner/group of new directory /tftp
          $ sudo systemctl restart tftpd-hpa # restart server

    2. Setup U-boot environment for AM62Ax

       .. code-block:: console

          # Boot to U-boot prompt using a working boot method
          => setenv ipaddr <ip-address-of-am62ax>
          => setenv serverip <ip-address-of-tftp-server>
          => saveenv # optional to save the U-boot ENV

    3. Use tftp command to load the bootloaders into memory and flash to OSPI
       NAND

       .. code-block:: console

          => mtd list
          => tftp ${loadaddr} tiboot3.bin
          => mtd write spi-nand0 $loadaddr 0x0 $filesize
          => tftp ${loadaddr} tispl.bin
          => mtd write spi-nand0 $loadaddr 0x80000 $filesize
          => tftp ${loadaddr} u-boot.img
          => mtd write spi-nand0 $loadaddr 0x280000 $filesize

    4. Change boot mode pins to boot with Serial NAND boot mode and reboot
       AM62Ax

    **Flashing images to OSPI NAND using SD card**

    In this example, load binaries from SD card. Assume bootloader names are
    :file:`tiboot3.bin`, :file:`tispl.bin`, :file:`u-boot.img`. Boot via SD
    card boot and stop at U-boot prompt before procceeding.

    1. Use fatload command to load the bootloaders into memory and flash to
       OSPI NAND

    .. code-block:: console

       => mtd list
       => fatload mmc 1 ${loadaddr} tiboot3.bin
       => mtd write spi-nand0 $loadaddr 0x0 $filesize
       => fatload mmc 1 ${loadaddr} tispl.bin
       => mtd write spi-nand0 $loadaddr 0x80000 $filesize
       => fatload mmc 1 ${loadaddr} u-boot.img
       => mtd write spi-nand0 $loadaddr 0x280000 $filesize

    2. Change boot mode pins to boot with Serial NAND boot mode and reboot EVM

    **Serial NAND Boot Mode**

    Please refer to the AM62Ax TRM Section 5.4 for more information. Both OSPI
    NAND and QSPI NAND lie under Serial NAND Boot mode.

    **Phy Calibration**

    Phy Calibration allows for higher read and write performance. To enable
    phy, the phy calibration pattern must be flashed to OSPI NAND at the start
    of the last erase block. For the Winbond W35N01JW flash, this lies at the
    address 0x7FC0000. The partition name should be 'ospi_nand.phypattern' as
    the driver looks for it before PHY Calibration.

    Download the binary file containing the phy pattern from :download:`here </files/ospi_phy_pattern>`.
    The commands below can be used to flash the phy pattern, with the location
    of the pattern depending on which flash is being used:

    .. code-block:: console

       => mtd list
       => tftp ${loadaddr} ospi_phy_pattern
       => mtd write spi-nand0 $loadaddr 0x7fc0000 $filesize

    **Flash layout for OSPI NAND**

    .. code-block:: text

       +--------------------------+ 0x0
       |   ospi_nand.tiboot3      |
       |   (512k)                 |
       +--------------------------+ 0x80000
       |   ospi_nand.tispl        |
       |   (2m)                   |
       +--------------------------+ 0x280000
       |   ospi_nand.u-boot       |
       |   (4m)                   |
       +--------------------------+ 0x680000
       |   ospi_nand.env          |
       |   (256k)                 |
       +--------------------------+ 0x6C0000
       |   ospi_nand.env.backup   |
       |   (256k)                 |
       +--------------------------+ 0x700000
       |   padding                |
       |   (25m)                  |
       +--------------------------+ 0x2000000
       |   ospi_nand.rootfs       |
       |   (95m)(ubifs)           |
       +--------------------------+ 0x7FC0000
       |   ospi_nand.phypattern   |
       |   (256k)                 |
       +--------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    AM62Px has a Cypress S28HS512T OSPI NOR flash and SYSFW is bundled with
    :file:`tiboot3.bin`.

    Below are two methods which can be used to flash the OSPI NOR device. For
    all methods, we will load the bootloaders into memory and then flash each
    to OSPI NOR at the respective addresses.

    **Flashing Images to OSPI NOR using TFTP server**

    In this example, we'll use the ``tftp-hpa`` package from Ubuntu for our
    tftp server. Assume bootloader names are :file:`tiboot3.bin`,
    :file:`tispl.bin`, :file:`u-boot.img`. Verify ethernet connection between
    AM62Px and host machine before proceeding.

    1. Setup TFTP server in Host machine

       .. code-block:: console

          # For complete instructions refer to: https://help.ubuntu.com/community/TFTP
          $ sudo apt install tftp-hpa
          $ sudo vi /etc/default/tftpd-hpa # optional to change tftp directory and other options
          $ sudo chown -R tftp /tftp # change owner/group of new directory /tftp
          $ sudo systemctl restart tftpd-hpa # restart server

    2. Setup U-boot environment for AM62Px

       .. code-block:: console

          # Boot to U-boot prompt using a working boot method
          => setenv ipaddr <ip-address-of-am62px>
          => setenv serverip <ip-address-of-tftp-server>
          => saveenv # optional to save the U-boot ENV

    3. Use tftp command to load the bootloaders into memory and flash to OSPI
       NOR

       .. code-block:: console

          => sf probe
          => tftp ${loadaddr} tiboot3.bin
          => sf update $loadaddr 0x0 $filesize
          => tftp ${loadaddr} tispl.bin
          => sf update $loadaddr 0x80000 $filesize
          => tftp ${loadaddr} u-boot.img
          => sf update $loadaddr 0x280000 $filesize

    4. Change boot mode pins to OSPI boot mode and reboot AM62Px

    **Flashing images to OSPI NOR using SD card**

    In this example, load binaries from SD card. Assume bootloader names are
    :file:`tiboot3.bin`, :file:`tispl.bin`, :file:`u-boot.img`. Boot via SD
    card boot and stop at U-boot prompt before procceeding.

    1. Use fatload command to load the bootloaders into memory and flash to
       OSPI NOR

       .. code-block:: console

          => sf probe
          => fatload mmc 1 ${loadaddr} tiboot3.bin
          => sf update $loadaddr 0x0 $filesize
          => fatload mmc 1 ${loadaddr} tispl.bin
          => sf update $loadaddr 0x80000 $filesize
          => fatload mmc 1 ${loadaddr} u-boot.img
          => sf update $loadaddr 0x280000 $filesize

    2. Change boot mode pins to OSPI boot mode and reboot AM62Px

    **OSPI Boot Mode**

    Please refer to the AM62Px TRM Section 5.4 for more information.

    **Phy Calibration**

    Phy Calibration allows for higher read performance. To enable phy, the phy
    calibration pattern must be flashed to OSPI at the start of the last erase
    sector. For the Cypress S28HS512T flash, this lies at the address 0x3FC0000.
    The partition name should be 'ospi.phypattern' as the driver looks for it
    before PHY Calibration.

    Download the binary file containing the phy pattern from :download:`here </files/ospi_phy_pattern>`.
    The commands below can be used to flash the phy pattern, with the location
    of the pattern depending on which flash is being used:

    .. code-block:: console

       => sf probe
       => tftp ${loadaddr} ospi_phy_pattern
       => sf update $loadaddr 0x3fc0000 $filesize

    **Flash layout for OSPI NOR**

    .. code-block:: text

       +---------------------+ 0x0
       |   ospi.tiboot3      |
       |   (512k)            |
       +---------------------+ 0x80000
       |   ospi.tispl        |
       |   (2m)              |
       +---------------------+ 0x280000
       |   ospi.u-boot       |
       |   (4m)              |
       +---------------------+ 0x680000
       |   ospi.env          |
       |   (256k)            |
       +---------------------+ 0x6C0000
       |   ospi.env.backup   |
       |   (256k)            |
       +---------------------+ 0x700000
       |   padding           |
       |   (1m)              |
       +---------------------+ 0x800000
       |   ospi.rootfs       |
       |   (55m)(ubifs)      |
       +---------------------+ 0x3FC0000
       |   ospi.phypattern   |
       |   (256k)            |
       +---------------------+

.. ifconfig:: CONFIG_part_variant in ('J721S2')

    J721S2 is largely similar to J721E and AM654. The major differences are
    that it has the cypress s28hs512t flash, sysfw is bundled with tiboot3.bin
    and, OSPI0 is muxed externally between a NOR and a NAND flash through a
    physical switch. OSPI NOR and OSPI NAND can't be used at the same time,
    they need to be selected by changing a physical configuration switch on
    the EVM board before driver probes them. CONFIG SW3.1 should be in OFF
    state to use OSPI NOR, and in ON STATE for OSPI NAND.

    **Flashing images to OSPI NOR/NAND**

    Below commands can be used to download tiboot3.bin, tispl.bin and
    u-boot.img over tftp and then flash it to OSPI NOR/NAND at respective
    addresses.

    * OSPI NOR:

        .. code-block:: console

            => sf probe
            => tftp ${loadaddr} tiboot3.bin
            => sf update $loadaddr 0x0 $filesize
            => tftp ${loadaddr} tispl.bin
            => sf update $loadaddr 0x80000 $filesize
            => tftp ${loadaddr} u-boot.img
            => sf update $loadaddr 0x280000 $filesize

    * OSPI NAND:

        .. code-block:: console

            => mtd list
            => mtd erase spi-nand0
            => tftp $loadaddr tiboot3.bin
            => mtd write spi-nand0 $loadaddr 0x0 $filesize
            => tftp $loadaddr tispl.bin
            => mtd write spi-nand0 $loadaddr 0x80000 $filesize
            => tftp $loadaddr u-boot.img
            => mtd write spi-nand0 $loadaddr 0x280000 $filesize

    **phy calibration**

    phy calibration allows for higher read performance. to enable phy, the phy
    calibration pattern must be flashed to ospi at the start of the last erase
    sector. for the cypress s28hs512t flash, this lies at the address 0x3fc0000.
    note, phy calibration is currently supported only for ospi nor flash.

    download the binary file containing the phy pattern from :download:`here </files/ospi_phy_pattern>`.
    below commands can be used to flash the phy pattern, with the location of the
    pattern depending on which flash is being used:

    .. code-block:: console

       => sf probe
       => tftp ${loadaddr} ospi_phy_pattern
       => sf update $loadaddr 0x3fc0000 $filesize

    **Flash layout for OSPI NOR**

    .. code-block:: console

             0x0 +----------------------------+
                 |     ospi.tiboot3(1m)       |
                 |                            |
         0x80000 +----------------------------+
                 |     ospi.tispl(2m)         |
                 |                            |
        0x280000 +----------------------------+
                 |     ospi.u-boot(4m)        |
                 |                            |
        0x680000 +----------------------------+
                 |     ospi.env(128k)         |
                 |                            |
        0x6A0000 +----------------------------+
                 |   ospi.env.backup(128k)    |
                 |                            |
        0x6C0000 +----------------------------+
                 |      padding (1280k)       |
        0x800000 +----------------------------+
                 |     ospi.rootfs(ubifs)     |
                 |                            |
       0x3fc0000 +----------------------------+
                 |   ospi.phypattern (256k)   |
                 |                            |
                 +----------------------------+

    **Flash layout for OSPI NAND**

    .. code-block:: console

             0x0 +---------------------------------+
                 |      ospi_nand.tiboot3(1m)      |
                 |                                 |
         0x80000 +---------------------------------+
                 |        ospi_nand.tispl(2m)      |
                 |                                 |
        0x280000 +---------------------------------+
                 |       ospi_nand.u-boot(4m)      |
                 |                                 |
        0x680000 +---------------------------------+
                 |       ospi_nand.env(128k)       |
                 |                                 |
        0x6A0000 +---------------------------------+
                 |    ospi_nand.env.backup(128k)   |
                 |                                 |
        0x6C0000 +---------------------------------+
                 |        padding (98048K)         |
       0x2000000 +---------------------------------+
                 |     ospi_nand.rootfs(ubifs)     |
                 |                                 |
       0x7fc0000 +---------------------------------+
                 |   ospi_nand.phypattern (256k)   |
                 |                                 |
                 +---------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2', 'J722S')

    |__PART_FAMILY_DEVICE_NAMES__| is similar to J721S2, only difference
    being that OSPI0 is muxed externally between a NOR and a NAND flash
    through a physical switch. OSPI NOR and OSPI NAND can't be used at the
    same time, they need to be selected by changing a physical configuration
    switch on the EVM board before driver probes them. CONFIG SW3.1 should be
    in OFF state to use OSPI NOR, and in ON STATE for OSPI NAND.

    **Flashing images to OSPI NOR flash**

    Following commands can be used to download tiboot3.bin, tispl.bin and
    u-boot.img over tftp and then flash it to OSPI NOR/NAND at respective
    addresses.

      * OSPI NOR:

         .. code-block:: console

            => sf probe
            => tftp ${loadaddr} tiboot3.bin
            => sf update $loadaddr 0x0 $filesize
            => tftp ${loadaddr} tispl.bin
            => sf update $loadaddr 0x80000 $filesize
            => tftp ${loadaddr} u-boot.img
            => sf update $loadaddr 0x280000 $filesize

      .. ifconfig:: CONFIG_part_variant in ('J742S2', 'J722S')

         * OSPI NAND:

            .. code-block:: console

               => mtd list
               => mtd erase spi-nand0
               => tftp $loadaddr tiboot3.bin
               => mtd write spi-nand0 $loadaddr 0x0 $filesize
               => tftp $loadaddr tispl.bin
               => mtd write spi-nand0 $loadaddr 0x80000 $filesize
               => tftp $loadaddr u-boot.img
               => mtd write spi-nand0 $loadaddr 0x280000 $filesize

      .. ifconfig:: CONFIG_part_variant in ('J784S4')

         * OSPI NAND:

            .. code-block:: console

               => mtd list
               => mtd erase spi-nand0
               => tftp $loadaddr tiboot3.bin
               => mtd write spi-nand0 $loadaddr 0x0 $filesize
               => tftp $loadaddr tispl.bin
               => mtd write spi-nand0 $loadaddr 0x100000 $filesize
               => tftp $loadaddr u-boot.img
               => mtd write spi-nand0 $loadaddr 0x300000 $filesize

    **PHY calibration**

    PHY calibration allows for higher read performance. To enable PHY, the PHY
    calibration pattern must be flashed to ospi at the start of the last erase
    sector. For the cypress s28hs512t flash, this lies at the address 0x3fc0000.
    Note, PHY calibration is currently supported only for OSPI NOR flash.

    download the binary file containing the phy pattern from :download:`here </files/ospi_phy_pattern>`.
    below commands can be used to flash the phy pattern, with the location of the
    pattern depending on which flash is being used:

    .. code-block:: console

       => sf probe
       => tftp ${loadaddr} ospi_phy_pattern
       => sf update $loadaddr 0x3fc0000 $filesize

    **Flash layout for OSPI NOR**

    .. code-block:: console

             0x0 +----------------------------+
                 |     ospi.tiboot3(1m)       |
                 |                            |
         0x80000 +----------------------------+
                 |     ospi.tispl(2m)         |
                 |                            |
        0x280000 +----------------------------+
                 |     ospi.u-boot(4m)        |
                 |                            |
        0x680000 +----------------------------+
                 |     ospi.env(128k)         |
                 |                            |
        0x6A0000 +----------------------------+
                 |   ospi.env.backup(128k)    |
                 |                            |
        0x6C0000 +----------------------------+
                 |      padding (1280k)       |
        0x800000 +----------------------------+
                 |     ospi.rootfs(ubifs)     |
                 |                            |
       0x3fc0000 +----------------------------+
                 |   ospi.phypattern (256k)   |
                 |                            |
                 +----------------------------+

    **Flash layout for OSPI NAND**

    .. code-block:: console

             0x0 +---------------------------------+
                 |      ospi_nand.tiboot3(1m)      |
                 |                                 |
         0x80000 +---------------------------------+
                 |        ospi_nand.tispl(2m)      |
                 |                                 |
        0x280000 +---------------------------------+
                 |       ospi_nand.u-boot(4m)      |
                 |                                 |
        0x680000 +---------------------------------+
                 |       ospi_nand.env(128k)       |
                 |                                 |
        0x6A0000 +---------------------------------+
                 |    ospi_nand.env.backup(128k)   |
                 |                                 |
        0x6C0000 +---------------------------------+
                 |        padding (98048K)         |
       0x2000000 +---------------------------------+
                 |     ospi_nand.rootfs(ubifs)     |
                 |                                 |
       0x7fc0000 +---------------------------------+
                 |   ospi_nand.phypattern (256k)   |
                 |                                 |
                 +---------------------------------+

    **Writing to OSPI using DFU**

    Setup: Connect the Type C port (USB0 port) of EVM to ubuntu host PC. Make sure
    dfu-util tool is installed and USB0 port is in UFP/DRP mode: SW3[3:4] = 01 or 1x.

    .. code-block:: console

         #sudo apt-get install dfu-util

    From u-boot(for OSPI flash):

    .. code-block:: console

        U-Boot # env default -a
        U-Boot # setenv dfu_alt_info ${dfu_alt_info_ospi}; dfu 0 sf "0:0:25000000:0"

    From ubuntu PC: Using dfu-util utilities to flash the binares to OSPI/QSPI flash.

    .. code-block:: console

        # sudo dfu-util -l
        Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
        Copyright 2010-2016 Tormod Volden and Stefan Schmidt
        This program is Free Software and has ABSOLUTELY NO WARRANTY

        Found DFU: [0451:6168] ver=0224, devnum=44, cfg=1, intf=0, path="1-3", alt=5, name="rootfs", serial="UNKNOWN"
        Found DFU: [0451:6168] ver=0224, devnum=44, cfg=1, intf=0, path="1-3", alt=4, name="sysfw.itb", serial="UNKNOWN"
        Found DFU: [0451:6168] ver=0224, devnum=44, cfg=1, intf=0, path="1-3", alt=3, name="u-boot-env", serial="UNKNOWN"
        Found DFU: [0451:6168] ver=0224, devnum=44, cfg=1, intf=0, path="1-3", alt=2, name="u-boot.img", serial="UNKNOWN"
        Found DFU: [0451:6168] ver=0224, devnum=44, cfg=1, intf=0, path="1-3", alt=1, name="tispl.bin", serial="UNKNOWN"
        Found DFU: [0451:6168] ver=0224, devnum=44, cfg=1, intf=0, path="1-3", alt=0, name="tiboot3.bin", serial="UNKNOWN"

    Flash the binaries to the respective regions using alternate interface
    number (alt=<x>).

    .. code-block:: console

        # sudo dfu-util -c 1 -i 0 -a 0 -D tiboot3.bin
        # sudo dfu-util -c 1 -i 0 -a 1 -D tispl.bin
        # sudo dfu-util -c 1 -i 0 -a 2 -D u-boot.img

.. ifconfig:: CONFIG_part_variant in ('Gen')

    Memory Layout of QSPI Flash

    .. code-block:: text

        +----------------+ 0x00000
        |      MLO       |
        |                |
        +----------------+ 0x040000
        |   u-boot.img   |
        |                |
        +----------------+ 0x140000
        |   DTB blob     |
        +----------------+ 0x1c0000
        |   u-boot env   |
        +----------------+ 0x1d0000
        |   u-boot env   |
        |    (backup)    |
        +----------------+ 0x1e0000
        |                |
        |     uImage     |
        |                |
        |                |
        +----------------+ 0x9e0000
        |                |
        |  other data    |
        |                |
        +----------------+

    .. rubric:: Writing to QSPI from U-Boot
       :name: writing-to-qspi-from-u-boot

    Note:

    -  From the U-Boot build, the **MLO** and **u-boot.img** files are the
       ones to be written.
    -  We load all files from an SD card in this example but they can just
       as easily be loaded via network (documented above) or other interface
       that exists.

    Writing MLO and u-boot.img binaries.

    For QSPI\_1 build U-Boot with ``dra7xx_evm_config``

    .. code-block:: console

        U-Boot # mmc rescan
        U-Boot # fatload mmc 0 ${loadaddr} MLO
        U-Boot # sf probe 0
        U-Boot # sf erase 0x00000 0x200000
        U-Boot # sf write ${loadaddr} 0x00000 ${filesize}
        U-Boot # fatload mmc 0 ${loadaddr} u-boot.img
        U-Boot # sf write ${loadaddr} 0x40000 ${filesize}

    change SW2[5:0] = 110110 for qspi boot.

    For QSPI\_4 build U-Boot with ``dra7xx_evm_qspiboot_config``

    .. code-block:: console

        U-Boot # mmc rescan
        U-Boot # fatload mmc 0 ${loadaddr} MLO
        U-Boot # sf probe 0
        U-Boot # sf erase 0x00000 0x200000
        U-Boot # sf write ${loadaddr} 0x00000 0x10000
        U-Boot # fatload mmc 0 ${loadaddr} u-boot.img
        U-Boot # sf write ${loadaddr} 0x40000 0x60000

    change SW2[5:0] = 110111 for qspi boot.

    |

    .. rubric:: Writing to QSPI using DFU
       :name: writing-to-qspi-using-dfu

    Setup: Connect the usb0 port of EVM to ubuntu host PC. Make sure
    dfu-util tool is installed.

    .. code-block:: console

         #sudo apt-get install dfu-util

    From u-boot:

    .. code-block:: console

        U-Boot # env default -a
        U-Boot # setenv dfu_alt_info ${dfu_alt_info_qspi}; dfu 0 sf "0:0:64000000:0"

    From ubuntu PC: Using dfu-util utilities to flash the binares to QSPI
    flash.

    .. code-block:: console

        # sudo dfu-util -l
        (C) 2005-2008 by Weston Schmidt, Harald Welte and OpenMoko Inc.
        (C) 2010-2011 Tormod Volden (DfuSe support)
        This program is Free Software and has ABSOLUTELY NO WARRANTY
        dfu-util does currently only support DFU version 1.0
        Found DFU: [0451:d022] devnum=0, cfg=1, intf=0, alt=0, name="MLO"
        Found DFU: [0451:d022] devnum=0, cfg=1, intf=0, alt=1, name="u-boot.img"
        Found DFU: [0451:d022] devnum=0, cfg=1, intf=0, alt=2, name="u-boot-spl-os"
        Found DFU: [0451:d022] devnum=0, cfg=1, intf=0, alt=3, name="u-boot-env"
        Found DFU: [0451:d022] devnum=0, cfg=1, intf=0, alt=4, name="u-boot-env.backup"
        Found DFU: [0451:d022] devnum=0, cfg=1, intf=0, alt=5, name="kernel"

    Flash the binaries to the respective regions using alternate interface
    number (alt=<x>).

    .. code-block:: console

        # sudo dfu-util -c 1 -i 0 -a 0 -D MLO
        # sudo dfu-util -c 1 -i 0 -a 1 -D u-boot.img
        # sudo dfu-util -c 1 -i 0 -a 2 -D <DTB-file>
        # sudo dfu-util -c 1 -i 0 -a 5 -D uImage

    .. rubric:: Booting from QSPI from u-boot
       :name: booting-from-qspi-from-u-boot

    The default environment does not contain a QSPI boot command. The
    following example uses the partition table found in the kernel.

    .. code-block:: console

        U-Boot # sf probe 0
        U-Boot # sf read ${loadaddr} 0x1e0000 0x800000
        U-Boot # sf read ${fdtaddr} 0x140000 0x80000
        U-Boot # setenv bootargs console=${console} root=/dev/mtdblock19 rootfstype=jffs2
        U-Boot # bootz ${loadaddr} - ${fdtaddr}

    .. rubric:: Booting from QSPI from SPL (Single stage or Falcon mode)
       :name: booting-from-qspi-from-spl-single-stage-or-falcon-mode

    In this boot mode SPL (first stage bootloader) directly boots the Linux
    kernel. Optionally, in order to enter into U-Boot, reset the board while
    keeping 'c' key on the serial terminal pressed. When falcon mode is
    enabled in U-Boot build (usually enabled by default), MLO checks if
    there is a valid uImage present at a defined offset. If uImage is
    present, it is booted directly. If valid uImage is not found, MLO falls
    back to booting u-boot.img.

    For QSPI single stage or Falcon mode, the CONFIG\_QSPI\_BOOT shall
    enabled.

    .. code-block:: text

        Menuconfig->Bood media
           [ ] Support for booting from NAND flash
           ..
           [*] Support for booting from QSPI flash
           [ ] Support for booting from SATA
           ...

    MLO, u-boot.img (optional), DTB, uImage are stored in QSPI flash memory.
    Refer the "Memory Layout" section for offset details. To flash binaries
    to QSPI, you can use
    `DFU <Foundational_Components_U-Boot.html#writing-to-qspi-using-dfu>`__,
    for example.

    The QSPI boot uses uImage. Build the kernel uImage. You will need to
    keep the U-Boot tool ``mkimage`` in your ``$PATH``

    .. code-block:: console

        # make uImage modules dtbs LOADADDR=80008000

    If kernel is not build with ``CONFIG_CMDLINE`` to set correct bootargs,
    then add the needed bootargs in chosen node in DTB file, using fdtput
    host utility. For example, for DRA74x EVM:

    .. code-block:: console

        # fdtput -v -t s arch/arm/boot/dts/dra7-evm.dtb "/chosen" bootargs "console=ttyO0,115200n8 root=<rootfs>"

    Set the environment variable "boot\_os" to 1.

    From u-boot prompt

    .. code-block:: console

        => setenv boot_os 1
        => saveenv

    Set the `board boot from
    QSPI <Foundational_Components_U-Boot.html#writing-to-qspi-from-u-boot>`__
    and reset the EVM. The SPL directly boots the kernel image from QSPI.

.. ifconfig:: CONFIG_part_variant in ('AM335X')

    SPI boot is supported on the following platforms:

    +--------------+-----------------------------------------------------------+
    | Board        | Config target                                             |
    +==============+===========================================================+
    | AM335x ICE   | am335x\_evm\_spiboot_defconfig                            |
    +--------------+-----------------------------------------------------------+

    .. code-block:: console

	    U-Boot # mmc rescan
	    U-Boot # sf probe 0
	    U-Boot # sf erase 0x0 0x100000
	    U-Boot # fatload mmc 0 ${loadaddr} MLO.byteswap
	    U-Boot # sf write ${loadaddr} 0x0 ${filesize}
	    U-Boot # fatload mmc 0 ${loadaddr} u-boot.img
	    U-Boot # sf write ${loadaddr} 0x20000 ${filesize}

    Note:

    -  AM335X ICE boots from SPI by default. To boot from SD card, erase the
       MLO partition:

    .. code-block:: console

	    U-Boot # sf erase 0x0 0x20000

.. ifconfig:: CONFIG_part_variant in ('AM437X')

    Using QSPI on AM43xx platforms is done as eXecute In Place and U-Boot is
    directly booted.

    .. rubric:: Writing to QSPI from U-Boot
       :name: writing-to-qspi-from-u-boot-1

    Note:

    -  From the U-Boot build the **u-boot.bin** file is the one to be
       written.
    -  We load all files from an SD card in this example but they can just
       as easily be loaded via network (documented above) or other interface
       that exists.

    .. code-block:: console

        U-Boot # mmc rescan
        U-Boot # fatload mmc 0 ${loadaddr} u-boot.bin
        U-Boot # sf probe 0
        U-Boot # sf erase 0x0 0x100000
        U-Boot # sf write ${loadaddr} 0x0 ${filesize}

    .. rubric:: Booting from QSPI
       :name: booting-from-qspi

    The default environment does not contain a QSPI boot command. The
    following example uses the partition table found in the kernel.

    .. code-block:: console

        U-Boot # sf probe 0
        U-Boot # sf read ${loadaddr} 0x1a0000 0x800000
        U-Boot # sf read ${fdtaddr} 0x100000 0x80000
        U-Boot # setenv bootargs console=${console} spi-ti-qspi.enable_qspi=1 root=/dev/mtdblock6 rootfstype=jffs2
        U-Boot # bootz ${loadaddr} - ${fdtaddr}
