.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_BOOT_OMAPL13x

Overview
^^^^^^^^^^

The Secondary Bootloader (SBL) for OMAPL137/OMAPL138/C6748 does basic
hardware initialization for the board to load and run applications.
Processor SDK boot support for each of these SoC is shown below

+-------------+-------------+-------------+-------------+-------------+
| Device      | Cores       | Boot Master | Supported   | HW          |
|             |             |             | Boot        | Platforms   |
|             |             |             | modes in    |             |
|             |             |             | SBL         |             |
+=============+=============+=============+=============+=============+
| OMAPL137    | ARM (ARM9)  | DSP         | SPI         | OMAPL137    |
|             | DSP (C674x) |             |             | EVM         |
+-------------+-------------+-------------+-------------+-------------+
| OMAPL138    | ARM (ARM9)  | ARM         | MMCSD       | OMAPL138    |
|             | DSP (C674x) |             |             | LCDK        |
+-------------+-------------+-------------+-------------+-------------+
| C6748       | DSP (C674x) | DSP         | MMCSD       | C6748 LCDK  |
+-------------+-------------+-------------+-------------+-------------+

Bootloader Execution Sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Power On Reset occurs
-  ROM Bootloader (RBL) executes. It checks for bootmode and attempts to
   load+run the SBL from that bootmode.
-  SBL begins execution from internal memory (Shared RAM)

   -  Board Initialization is done by a call to **Board_init()** API.
      For additional details refer to `Processor SDK Board
      Support <index_board.html#board-support>`__.
   -  SBL setup includes configuring Pinmux, enable peripheral clocks,
      set up PLLs, and configure EMIF for SDRAM/DDR.

-  SBL finishes setup and looks for "app" to execute next. This
   user-modifiable application shall reside on the boot media.
-  Once located, app will be loaded into memory and execution will be
   branched to the application's entry address

Tools and Binary Formats
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Making Bootable SBL image (MLO)
""""""""""""""""""""""""""""""""

RBL loads and runs "MLO", which is a .out executable formatted by TI
tools. HexAIS tool should be used to convert the .out into MLO using the
below command.

Windows Host

**<HexAIS_Tool> -o <output file> -ini <ini file> <input file>**

Linux Host

HexAIS executable can be run on Linux PC by using mono tool as shown
below

**mono <HexAIS_Tool> -o <output file> -ini <ini file> <input file>**

-  <HexAIS_Tool> is HexAIS_OMAP-L137.exe for OMAPL137 and
   HexAIS_OMAP-L138.exe for OMAPL138/C6748
-  ‘output file’ is name of the output file. MLO in this case
-  ‘ini file’ is configuration file for defining the boot parameters.
   This file provides option to instruct RBL to take certain actions
   before loading the MLO into internal memory. Sample ini file is
   available at **< PDK_INSTALL_DIR
   >/packages/ti/boot/sbl/soc/<device>**

<device> can be omapl137, omapl138 or c6748

-  ‘input file’ is the input .out file name which needs to be converted
   into MLO

OMAPL137 HexAIS tool is available at **< PDK_INSTALL_DIR
>/packages/ti/boot/sbl/tools/omapl13x_boot_utils/OMAP-L137/GNU/AISUtils**.

OMAPL138/C6748 HexAIS tool is available at **< PDK_INSTALL_DIR
>/packages/ti/boot/sbl/tools/omapl13x_boot_utils/OMAP-L138/GNU/AISUtils**

Making Loadable User Application image (app)
""""""""""""""""""""""""""""""""""""""""""""""

For converting the compiled .out files to a format loadable by TI's
Secondary Boot Loader (SBL), you must follow these two steps:

#. **out2rprc.exe [.out file] [rprc output]**
#. **MulticoreImageGen.exe LE 55 [output name] <Core ID> [rprc output]**

Out2rprc.exe and MulticoreImageGen.exe are tools supplied by TI and can
be located in the **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools**
folder. "rprc output" can be any spare name of your choosing. "output
name" can also be any name of your choosing.

The <Core ID> used in step 2 refers to the Core ID to boot. Use '0' as
Core ID for ARM core and '1' for DSP core. Valid values are:. You can
input a different value to boot to other cores. Valid values are:

+----------+-------+
| Core     | Value |
+==========+=======+
| ARM Core | 0     |
+----------+-------+
| DSP Core | 1     |
+----------+-------+

.. note::
   Program entry point of DSP app images on OMAPL138 platform should be 1KByte aligned for loading and executing the DSP images from
   ARM core. GPIO LLD LED blink example for C674x core can be used as reference for aligning the DSP entry point to run the DSP code from
   SBL. Other LLD examples does not work from SBL as is.

Boot Modes
^^^^^^^^^^^^

This release of SBL supports SPI and MMCSD boot modes.

SPI Boot Mode
""""""""""""""

Preparing SPI Flash
'''''''''''''''''''''

MLO and app needs to be flashed into SPI memory so that they can be
booted. MLO will reside at offset 0 and app will reside at offset
0x80000. SPI flash memory map:

+----------------+-----+
| Offset 0x0     | MLO |
+----------------+-----+
| Offset 0x80000 | app |
+----------------+-----+

The images can be flashed into SPI flash by following steps given below:

#. Copy MLO and app to SPI flash writer binary folder -
   **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashWriter/spi/bin/evmOMAPL137**.
   Make sure config file also present in the SPI flash writer binary
   folder.

   -  MLO is the SBL formatted by the aforementioned tools. A pre-built
      MLO can be found at:
      **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/binary/evmOMAPL137/spi/bin**
   -  app is the target application to be booted and also formatted by
      the aforementioned tools. (Note that the tools for making the
      bootable MLO and the loadable app are different).
   -  config helps specify the memory map. The default config file can
      be found at:
      **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashWriter/spi/bin/evmOMAPL137**.
      This config file may be altered to custom user settings if needed.

#. Connect the DB9 port of the EVM to host PC. Open serial communication
   applications like TeraTerm, MiniCom, etc and configure for ‘115200
   8N1’.
#. Connect to the board with CCS. Launch target configuration and
   connect to the DSP C674x core. GEL file will run on-connect and do
   basic board-level initialization
#. Load the flash writer, spi_flash_writer.out, to the connected core

   -  A pre-built spi_flash_writer.out can be found at:
      **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashWriter/spi/bin/evmOMAPL137**

#. Run the SPI flash writer application. You will see the following logs
   on the EVM's UART console:

::

     *** PDK SPI Flash Writer ***
    Opening SPI handle...
    SPI handle opened!
    Parsing config file and flashing content to SPI NOR...
    Parsed config line, received parameters: filename = MLO, address = 0x0
           Size of MLO is 0xc81c
           Loading binary to memory ...
           Finished loading binary to memory!
           Flashed MLO to offset 0x0!
           Read flash memory at 0x0, checking flashed content...
           Verified flash data equal expected data!
    Parsed config line, received parameters: filename = app, address = 0x80000
           Size of app is 0x16144
           Loading binary to memory ...
           Finished loading binary to memory!
           Flashed app to offset 0x80000!
           Read flash memory at 0x80000, checking flashed content...
           Verified flash data equal expected data!
    Successfully flashed memory content!

.. note::
   This application will flash the image at required offset without taking
   into consideration any overwriting to previously flashed image.

Booting via SPI
''''''''''''''''''''

#. Set the OMAPL137 EVM to SPI bootmode by configuring the SW2 DIP
   switches 1-4 to 'OFF ON OFF ON'. Other switch positions on SW2 are
   don’t care for SPI boot.
#. Connect the DB9 port of the EVM to host PC. Open serial communication
   applications like TeraTerm, MiniCom, etc and configure for ‘115200
   8N1’
#. Power on the board

Below is an example of OMAPL137 SBL successfully booting the GPIO LED
blink application

.. Image:: /images/Omapl137_boot_example.jpg

|

MMCSD Boot Mode
""""""""""""""""

OMAPL138/C6848 RBL does not support reading the boot images as files
from SD card. Secondary Boot loader image should be written to SD card
as raw data. Special formatting is needed for SD card to create
un-formatted area at the beginning of the card to store SBL.

Formatting the SD Card
''''''''''''''''''''''''

SD card for booting OMAPL138/C6748 needs to be formatted from Linux PC
due to un-formatted area requirement. Formatting the SD card from
Windows PC is not supported in this release.

Connect the SD card to Linux PC and use below command to format the SD
card

**sudo sh create-sdcard-omapl13x.sh <Drive Name>**

-  <Drive Name> is name of the drive on which SD card is mounted. Be
   cautious while selecting the drive name. Running the script with
   system drive name will corrupt the file system.
-  create-sdcard-omapl13x.sh script is available at
   **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/omapl13x_sd_card_format**

Preparing the SD Card
''''''''''''''''''''''

For both OMAPL138 and C6748, MLO needs to be flashed onto SD card
un-formatted area and app should be copied onto SD card.

MLO can be flashed into SD card un-formatted area by following steps
given below:

#. Build the MMCSD flash writer using below commands

   -  cd <PDK_INSTALL_DIR>/packages/ti/boot/sbl
   -  gmake mmcsd_flashwriter SOC=OMAPL138 BOARD=lcdkOMAPL138
      BOOTMODE=mmcsd

#. Copy 'app' to SD card and insert the card into MMCSD slot of the
   board
#. Copy MLO to MMCSD flash writer binary folder -
   **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashWriter/mmcsd/bin/lcdkOMAPL138**.
   Make sure config file also present in the MMCSD flash writer binary
   folder.

   -  MLO is the SBL formatted by the aforementioned tools. A pre-built
      MLO can be found at:
      **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/binary/lcdkOMAPL138/mmcsd/bin**
   -  app is the target application to be booted and also formatted by
      the aforementioned tools. (Note that the tools for making the
      bootable MLO and the loadable app are different).
   -  config helps specify the memory map. The default config file can
      be found at:
      **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashWriter/mmcsd/bin/lcdkOMAPL138**.
      This config file may be altered to custom user settings if needed.

#. Connect the USB serial port of the EVM to host PC. Open serial
   communication applications like TeraTerm, MiniCom, etc and configure
   for ‘115200 8N1’.
#. Connect to the board with CCS. Launch target configuration, connect
   to ARM core first (not needed for C6748) and then connect to the DSP
   C674x core. GEL file will run on-connect and do basic board-level
   initialization
#. Load the flash writer, mmcsd_flash_writer.out, to the connected core

   -  mmcsd_flash_writer.out can be found at:
      **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashWriter/mmcsd/bin/lcdkOMAPL138**

#. Run the MMCSD flash writer application. You will see the following
   logs on the EVM's UART console:

::

    Opening MMCSD handle...
    MMCSD handle opened!
    Parsing config file and flashing content to MMCSD...
    Parsed config line, received parameters: filename = MLO, address = 0x200
           Size of MLO is 0xb9b8
           Loading binary to memory ...
           Finished loading binary to memory!
           Flashed MLO to offset 0x200!
           Read flash memory at 0x200, checking flashed content...
           Verified flash data equal expected data!
    Successfully flashed memory content!

Procedure to flash the MLO described above is applicable to C6748 also.
Use C6748 for OMAPL138 and lcdkC6748 for lcdkOMAPL138 in all the paths
mentioned above.

::

    MLO offset in config file is set to 200 by default which indicates that MLO will be written to second sector of the SD card. MLO offset can be any non-
    zero value which is multiple of 512 and should be within first 2Mbytes of SD card memory. DO NOT set the MLO offset to '0' which will corrupt the file
    system on the card.

.. note::
   This application will flash the image at required offset without taking
   into consideration any overwriting to previously flashed image.

|

Booting via MMCSD
''''''''''''''''''''

#. Set the OMAPL138/C6748 LCDK to MMCSD bootmode by configuring the SW1
   DIP switches 1-4 to 'OFF OFF OFF ON'. Other switch positions on SW1
   are don’t care for MMCSD boot.
#. Connect the USB serial port of the EVM to host PC. Open serial
   communication applications like TeraTerm, MiniCom, etc and configure
   for ‘115200 8N1’
#. Power on the board

Below is an example of OMAPL138 SBL successfully booting the GPIO LED
blink application

.. Image:: /images/Omapl138_boot_example.png

|

Memory Usage
^^^^^^^^^^^^^^^

SBL uses 0x20000 bytes from shared RAM (0x80000000 to 0x8001FFFF).

|

.. note::
   app should not have loadable sections residing in SBL memory region to
   prevent overwriting SBL during load time. It is, however, free to use
   SBL memory after it is loaded and running.

|

Additional Details
^^^^^^^^^^^^^^^^^^^^

Use below commands to clean and build the SBL and associated tools.

Initial Steps
"""""""""""""""

Setup the environment variables to configure the build tools

cd <PDK_INSTALL_DIR>/packages

Run pdksetupenv script

cd ti/boot/sbl

Cleaning SBL
"""""""""""""""

gmake clean SOC=<SoC Name> BOARD=<Board Name> BOOTMODE=<Boot Mode>

Building SBL
"""""""""""""""

gmake SOC=<SoC Name> BOARD=<Board Name> BOOTMODE=<Boot Mode>

Cleaning Flash Writer
""""""""""""""""""""""

gmake <Flash Writer>_clean SOC=<SoC Name> BOARD=<Board Name>
BOOTMODE=<Boot Mode>

building-flash-writer
""""""""""""""""""""""

gmake <Flash Writer> SOC=<SoC Name> BOARD=<Board Name> BOOTMODE=<Boot
Mode>

-  use 'make' instead of 'gmake' on Linux host
-  <SoC Name> - OMAPL137, OMAPL138 or C6748
-  <Board Name> - evmOMAPL137, lcdkOMAPL138 or lcdkC6748
-  <Boot Mode> - spi or mmcsd as supported by the device
-  <Flash Writer> - spi_flashwriter for spi boot mmcsd_flashwriter for
   mmcsd boot

::

     Examples:
     Cleaning & Building OMAPL137 SBL
     gmake clean SOC=OMAPL137 BOARD=evmOMAPL137 BOOTMODE=spi
     gmake SOC=OMAPL137 BOARD=evmOMAPL137 BOOTMODE=spi

     Cleaning & Building OMAPL137 flash writer
     gmake spi_flashwriter_clean SOC=OMAPL137 BOARD=evmOMAPL137 BOOTMODE=spi
     gmake spi_flashwriter SOC=OMAPL137 BOARD=evmOMAPL137 BOOTMODE=spi

On successful build, SBL .out and MLO will be created at
**<PDK_INSTALL_DIR>/packages/ti/boot/sbl/binary/<Board Name>/<Boot
Mode>/bin** and flash writer binary will be created at
**<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashWriter/<Boot
Mode>/bin/<Board Name>**

