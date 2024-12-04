.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_DIAG

Overview
-----------

The Processor SDK RTOS Diagnostic package is designed to be a set of
baremetal tests to run on a given board to provide data path continuity
testing on peripherals. For K2H/K2E/K2L/C66x devices, this functionality
is provided by `POST <index_board.html#power-on-self-test>`__.

Building the Examples
----------------------

Pre-requisites to Building
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Set your environment using pdksetupenv.bat or pdksetupenv.sh. The
   diagnostic application uses the same environment variables as the
   board library build. Refer to the `Processor SDK RTOS
   Building <index_overview.html#building-the-sdk>`__ page for
   information on setting up your build environment.
#. You will need the following libraries built:

-  Board
-  UART
-  GPIO
-  I2C
-  SPI
-  CSL
-  ICSS
-  PRUSS
-  MMCSD
-  EMAC
-  USB
-  UDMA
-  SCICLIENT

(Note: not every library is used for every application, and these
libraries should come pre-built with any fresh installation of the
Processor SDK)

Compiling the Diagnostic Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To build the diagnostic examples:

#. **cd <PDK>/packages/ti/board/diag**
#. **make <BOARD>**

This will make the diagnostic applications for a specific $BOARD.
Output files will be located in: **<PDK>/packages/ti/board/bin/<BOARD>**

Creating the SD Card Loadable Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For converting the compiled .out files to a format loadable by TI's
Secondary Boot Loader (SBL), you must follow these two steps:

#. **out2rprc.exe [.out file] [rprc output]**
#. **MulticoreImageGen.exe LE 55 [output name] 0 [rprc output]**

Out2rprc.exe and MulticoreImageGen.exe are tools supplied by TI and can
be located in the **<PDK>/packages/ti/boot/sbl/tools** folder. "rprc
output" can be any spare name of your choosing. "output name" can also
be any name of your choosing. **For diagnostic applications, your final
output name must have the keyword "TEST" in it.** You will have to do
this process for every .out application you wish to be loadable on the
SD card.

Alternatively, there is also a make target to automate this process:

#. **cd <PDK>/packages/ti/board/diag**
#. **make <BOARD>_sd**

This will compile all the applications for a specific $BOARD, and also
create the SD card loadable files. The output files will be located in:
**<PDK>/packages/ti/board/bin/<BOARD>/sd**. Note that the framework
application is named "app" to allow it to be the default application to
be loaded by the SBL.

.. note::
    Diagnostic tests on AM65xx platform supports A53 and R5 cores.
    A53 binary path: <PDK>/packages/ti/board/bin/<BOARD>/sd/armv8.
    R5 binary path: <PDK>/packages/ti/board/bin/<BOARD>/sd/armv7.

Creating the SPI Flash Loadable Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SPI boot shall be the primary boot option for the platforms (Ex: AMIC110
ICE) which does not support SD card interface. All the diagnostic tests
are integrated into framework binary for the ease of use in the case of
SPI boot. Integrated diagnostic framework test binary can be loaded and
executed through UART port.

Use below command to build the diagnostic tests and create SPI flash
loadable files.

-  **make <BOARD>_spi**

|

Make targets
^^^^^^^^^^^^^^^

The simplest invocation is to use "make <BOARD>" to compile all the
applications. Here is a list of make targets implemented for the
diagnostic makefile:

-  **make <BOARD>** - compile all diagnostic applications for one
   specific BOARD
-  **make clean** - clean and remove all applications for all supported
   BOARDs
-  **make <BOARD>_clean** - clean and remove all application for one
   specific BOARD
-  **make <BOARD>_sd** - compile all diagnostic applications for one
   specific BOARD and create the SD card loadable files with those
   compiled applications
-  **make <BOARD>_spi** - compile all diagnostic applications for one
   specific BOARD and create the SPI flash loadable files with those
   compiled applications

The <BOARD> supported depends on your Processor SDK RTOS variant. Refer
to following table for available <BOARD> for each Processor SDK RTOS
variant:

+-----------+-----------+-----------+-----------+-----------+-----------+------------+
| make      | am335x    | am437x    | am57xx    | k2g       | omapl13x  | AM65xx     |
| target /  |           |           |           |           |           |            |
| Variant   |           |           |           |           |           |            |
+===========+===========+===========+===========+===========+===========+============+
| <Board>   | evmAM335x | evmAM437x | idkAM572x | evmK2G    | evmOMAPL1 | am65xx_evm |
|           | skAM335x  | skAM437x  | idkAM571x | iceK2G    | 37        | am65xx_idk |
|           | bbbAM335x | idkAM437x | evmAM572x |           | (No Boot  | (Supports  |
|           | icev2AM33 |           | idkAM574x |           | support.  | A53 & R5   |
|           | 5x        |           |           |           |           | cores)     |
|           | iceAMIC11 |           |           |           | Diagnosti |            |
|           | 0         |           |           |           | cs        |            |
|           |           |           |           |           | need to   |            |
|           |           |           |           |           | run from  |            |
|           |           |           |           |           | CCS)      |            |
+-----------+-----------+-----------+-----------+-----------+-----------+------------+

.. note::
   OMAPL137 EVM diagnostic tests does not support executing from
   a boot device. Use the command **make evmOMAPL137** to build the
   diagnostics. Diagnostics test binaries need to be executed from CCS.

Running the Diagnostic Examples
-----------------------------------

Loading through SD Card (Default Method)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Your SD card must be set up to a bootable format. Refer to the
`Processor SDK RTOS Boot <index_Foundational_Components.html#boot>`__ page
for information on how the SD card is handled.

You will need to compile the diagnostic applications for your BOARD,
created their respective SD card loadable files, and copied them onto an
SD card. You will also need the SBL (renamed to "MLO") on the SD card.
To do so:

#. cd <PDK>/packages/ti/board/diag
#. make <BOARD>_sd
#. copy all the content under <PDK>/packages/ti/board/bin/<BOARD>/sd to
   your SD card
#. copy the MLO to your SD card (default location at
   <PDK>/packages/ti/boot/sbl/binary/<BOARD>/mmcsd
#. insert your SD card into your board and power on your board
#. open Terminal emulator program eg: Teraterm to connect to the board's
   UART console

.. note::
    Use MAIN UART0 console for running the tests on A53 core and MCU UART console
    for running the tests on R5 core for AM65xx platform.

#. press the "Hard Reset" button on your board. (This is to force
   re-booting, and not absolutely necessary. Because Terminal emulator
   program is opened after boot is powered on, you would've missed the
   initial printout messages. This step is for demonstration and
   confidence checking that the board has booted correctly)

.. note::
    Diagnostic tests on AM65xx platform supports A53 and R5 cores.
    A53 binary path: <PDK>/packages/ti/board/bin/<BOARD>/sd/armv8.
    R5 binary path: <PDK>/packages/ti/board/bin/<BOARD>/sd/armv7.

.. note::
    SBL binary name is different on AM65xx platform and requires
    system firmware binary also to be copied to SD card.
    Copy the sbl_mmcsd_img_mcu1_0_release.tiimage file from
    <PDK>/packages/ti/boot/sbl/binary/mmcsd/<BOARD> to SD card and
    rename it to tiboot3.bin.
    Copy the system firmware image <PDK>/packages/ti/drv/sciclient/soc/V0/sysfw.bin to SD card
    (for AM65xx SR2, copy "sysfw_sr2.bin" instead and rename it "sysfw.bin" on the SD card)

You should see the following screen when board is bootted with diagnostic binaries in SD card:

.. Image:: /images/Diag-screen1.jpg

The framework diagnostic application should be loaded through SBL, and
gives you the options:

-  help - prints the command menu and descriptions of the commands
-  run - run a diagnostic application found on the SD card
-  status - current status of the framework run

Below is an example of running a diagnostic application:

.. Image:: /images/Diag-screen2.jpg

Result of return from above run:

.. Image:: /images/Diag-screen3.png

Loading through SPI Flash
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describes creating the diagnostic test images for SPI flash
booting, programming and running them from SPI flash. Currently SPI boot
is supported only by iceAMIC110 platform.

You will need to compile the diagnostic applications for your BOARD,
create their respective SPI flash loadable files, and program them onto
SPI flash. To do so:

#. cd <PDK>/packages/ti/board/diag
#. make <BOARD>_spi
#. Start CCS and launch target configuration file for AMIC110 ICE board
#. Connect the target, load and run the SPI flash writer binary.
   Prebuilt SPI flash writer is available at **<AM335x
   PDK>\packages\ti\starterware\tools\flash_writer\spi_flash_writer_AM335X.out**
#. Choose option 1 to initiate image flashing
#. Enter the file name as SPI bootloader along with full path **(Ex:
   <AM335x
   PDK>\packages\ti\starterware\binary\bootloader\bin\am335x-evm\gcc\bootloader_boot_mcspi_a8host_release_ti.bin)**
#. Enter offset as 0
#. Wait until flashing completes successfully
#. Rerun the SPI flash writer binary and program diagnostic framework
   loader at offset 20000. Diagnostic framework loader binary will be
   available at **<AM335x
   PDK>\packages\ti\board\bin\iceAMIC110\spi\app**
#. Rerun the SPI flash writer binary and program diagnostic framework at
   offset 40000. Diagnostic framework binary will be available at
   **<AM335x PDK>\packages\ti\board\bin\iceAMIC110\spi\framework**

Sample CCS output of SPI flash writer is shown below:

.. Image:: /images/Spi_flash_writer_output.jpg

|

#. open Terminal emulator program eg: Teraterm to connect to the board's
   UART console
#. press the "Hard Reset" button on your board. (This is to force
   re-booting, and not absolutely necessary. Because Terminal emulator
   program is opened after boot is powered on, you would've missed the
   initial printout messages. This step is for demonstration and
   confidence checking that the board has booted correctly)

You should see the following screen:

.. Image:: /images/Amic110_ice_spi_boot_diag1.jpg

|
| The framework diagnostic application should be loaded through SBL, and
  gives you the options:

-  help - prints the command menu and descriptions of the commands
-  run - run a diagnostic application found on the SD card
-  status - current status of the framework run

Below is an example of running a diagnostic application:

.. Image:: /images/Amic110_ice_spi_boot_diag2.jpg

|
| Result of return from above run:

.. Image:: /images/Amic110_ice_spi_boot_diag3.jpg

|

Running or debugging on CCS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To debug your application, CCS can give you access to the chip's memory
and register values. You can follow the below steps to load and run an
application in CCS. If you have a SD card loadable image, and is able to
load your application, you can connect to the A15 core in CCS and load
symbols without having to load and run the entire application. After
running "make all" or "make $BOARD", the output files should be
generated under <PDK>/packages/ti/board/bin/ directory. You will have to
navigate down to the $BOARD you're building (eg. idkAM572x, evmAM572x,
etc.) and the $TARGET core you're building for (eg. armv7).

**For the existing diagnostic applications, you may need to define
PDK_RAW_BOOT before compiling**. This is done by adding the line
"#define PDK_RAW_BOOT" to an individual application source file or to
<PDK>/packages/ti/board/src/<BOARD>/include/board_cfg.h to apply for all
applications. This is used because the default diagnostic loading method
is through SD card, and the pinmux is done already. Adding this option
only forces the diagnostic applications to do pinmuxing within the
application itself (and not depend it being done).

To run on CCS:

#. Connect USB cable to the board's JTAG
#. Connect the UART serial cable. For the IDK boards, the UART console
   is the same as the usb JTAG connector, so no additional cable is
   necessary.
#. Plug in power cord to your board
#. Press the power button on the board to turn the board on
#. Setup and run CCSv6.1 (or higher). Follow the `Processor SDK RTOS
   Getting Started
   Guide <index_overview.html#processor-sdk-rtos-getting-started-guide>`__ on how
   to setup your CCS to connect to the board
#. Launch target configuration for the board
#. Connect to the core that you built your application for. For example:
   for idkAM572x armv7 projects, click on the Cortex A-15 MPU0 core and
   press the connect button
#. Load the program by pressing the load button and navigate the
   explorer to the .out file that you want to load
#. Press the Run button to run the program
#. Check UART console to see if anything is printed out. \**If nothing
   is printed out, pause the core and see where the program counter is
   at. If it is at 0x3808c (or near it), try reloading the program and
   running again.

.. note:: Diagnostics are built for both DSP (C674x) and ARM (arm9) cores
   on omapl13x platform.

Running on a different ARM core
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The diagnostic baremetal applications are typically targeted for Core 0
of an ARM corepac. It is possible to load and run it on one of the
subcores in CCS. To do so, please consider the following:

#. Enable Cache - setup typically only enables cache for the main ARM
   core. You may have to explicitly enable the data and instruction
   cache. See relevant cache functions under pdk/packages/ti/csl/arch.
#. [For AM57x boards] Set OPP to high - SBL would set OPP to high for
   Core 0, but may not do it for the subcores. You can do so by using
   the GEL file. After connecting to the core, run the function under
   Scripts -> AM572x PRCM CLOCK configuration ->
   AM572x_PRCM_Clock_Config_OPPHIGH (similarly named for AM571x).

Diagnostic Applications
-----------------------------


+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                      Name                       |    Description    | AM65xx | AM65xx | GP     | IDK           | IDK    | EVM | ICE | EVM    | SK     | BBB    | ICEv2  | EVM    | SK     | IDK    | EVM      | ICE     |
|                                                 |                   | EVM    | IDK    | AM572x | AM572x/AM574x | AM571x | K2G | K2G | AM335x | AM335x | AM335x | AM335x | AM437x | AM437x | AM437x | OMAPL137 | AMIC110 |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+=================================================+===================+========+========+========+===============+========+=====+=====+========+========+========+========+========+========+========+==========+=========+
|                                                 | Test for device   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    lcdTouchscreen_TEST                          | detection and     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | read the X, Y     |        |        |        |               |        |     |     |    x   |  x     |        |        |  x     |  x     |        |          |         |
|                                                 | and Z axis        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | values to confirm |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | values within     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | range.            |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Test for ADC      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    adc_TEST                                     | configuration for |        |        |        |               |        |     |     |    x   |  x     |        |        |    x   |  x     |        |          |         |
|                                                 | Channel sequencing|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and One shot mode |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | operation.        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Test for device   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    ambient_TEST                                 | detection on board|        |        |        |               |        |     |     |    x   |        |        |        |    x   |        |        |          |         |
|                                                 | and working of    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the light sensor. |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Writes to GPIO in |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    buzzer_TEST                                  | connected to a    |        |        |        |               |        |     |     |    x   |        |        |        |    x   |        |        |          |         |
|                                                 | buzzer. Requires  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | user to verify    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | sound             |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Probes the clock  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    clock_TEST                                   | generator on      |        |        |        |               |        |     |  x  |        |        |        |        |        |        |        |          |         |
|                                                 | I2C bus           |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Read voltage,     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    currentMonitor_TEST                          | current on I2C    |   x    |   x    |        |               |        |     |  x  |        |        |        |        |        |        |        |          |         |
|                                                 | devices           |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Read voltage,     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    currentMonitorStress_TEST                    | current on I2C    |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | devices. Test is  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | repeated for 100  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | cycles. Press 'b' |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | to stop the test  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | before completing |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | test cycles.      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Does DCAN loopback|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    dcan_TEST                                    | writes and reads. |        |        |        |     x         |    x   |  x  |     |        |        |        |        |        |        |        |          |         |
|                                                 | Passes on         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | successful return.|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Reads the EEPROM  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    eeprom_TEST                                  | and prints out the|    x   |    x   |    x   |     x         |    x   |  x  |  x  |    x   |    x   |    x   |     x  |    x   |    x   |    x   |          |    x    |
|                                                 | board's ID        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | information.      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Passes on         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | successful I2C    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | reads. EEPROM will|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | need to be        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | programmed prior  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | in order for a    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | correct read.     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Sends packet o    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    emac_TEST                                    | PHY loopback t    |        |        |        |               |        |     |  x  |        |        |        |        |        |        |        |          |         |
|                                                 | verify MAC        |   x    |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | operations        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies EMAC     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    emacStress_TEST                              | Ethernet ports by |   x    |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | sending and       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | receiving 10240   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | packets.          |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Writes to and read|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    emmc_TEST                                    | from eMMC memory. |    x   |    x   |    x   |    x          |  x     |  x  |     |        |        |        |        |        |        |        |          |         |
|                                                 | Passes on reading |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | back the correct  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | value as the one  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | written           |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Writes to and read|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    emmcStress_TEST                              | from eMMC memory. |    x   |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Test covers the   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | entire eMMC memory|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | The main          |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    app                                          | diagnostic        |    x   |    x   |    x   |     x         |    x   |  x  |  x  |    x   |    x   |    x   |     x  |    x   |    x   |    x   |          |    x    |
|                                                 | application. This |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | is loaded by SBL  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and can load other|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | diagnostic        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | applications on   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the SD card.      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Sends and receive |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    gmac_TEST                                    | packets over      |        |        |        |    x          |    x   |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | ethernet, both    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | internally and    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | externally. Passes|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | on receiving all  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | packets.          |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Writes to the GPIO|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    haptics_TEST                                 | pin connected to a|        |        |        |    x          |  x     |     |     |        |        |        |        |   x    |        |        |          |         |
|                                                 | motor (haptics).  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Requires user to  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | verify that the   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | motor is active.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests HDMI        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    hdmi_TEST                                    | display output    |        |        |        |               |        |  x  |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Configures one    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    icssEmac_TEST                                | ICSS EMAC port    |        |        |        |     x         |  x     |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and tests         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | functionality via |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | packet loopback.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests LCD display |   x    |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    lcd_TEST                                     | output and touch  |        |        |        |               |        |  x  |     |        |        |        |        |        |        |        |          |         |
|                                                 | input             |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Prompts the user  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    lcdTouchscreen_TEST                          | for touches on the|        |        |        |     x         |   x    |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | LCD touchscreen   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and report back   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | its location.     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Requires user to  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | input 9           |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | simultaneous      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | touches to        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | verify pass.      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Cycles through    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    led_TEST                                     | GPIO LEDs on the  |    x   |    x   |    x   |     x         |   x    |  x  |  x  |    x   |    x   |   x    |   x    |    x   |    x   |    x   |          |    x    |
|                                                 | board. Requires   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | user to verify    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the LEDs blink.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Cycles through    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    ledStress_TEST                               | GPIO LEDs on the  |    x   |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board. Requires   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | user to verify    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the LEDs blink.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Test is repeated  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | for 100 cycles.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Press 'b' to stop |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the test before   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | completing test   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | cycles.           |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Cycles through the|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    ledIndustrial_TEST                           | I2C LEDs on the   |   x    |   x    |        |     x         |   x    |     |  x  |        |        |        |        |        |        |        |          |         |
|                                                 | board. Requires   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | user to verify    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | LEDs blink.       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Cycles through the|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    ledIndustrialStress_TEST                     | I2C LEDs on the   |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board. Requires   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | user to verify    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | LEDs blink.       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Test is repeated  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | for 100 cycles.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Press 'b' to stop |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the test before   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | completing test   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | cycles.           |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Attempts one      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    mcspi_TEST                                   | write and read on |        |        |        |     x         |   x    |     |     |        |        |        |        |        |        |    x   |          |    x    |
|                                                 | the MCSPI header. |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Requires user to  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | verify the value  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | being read back   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | is as expected.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Writes and reads  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    mem_TEST                                     | to external (DDR) |   x    |   x    |   x    |     x         |    x   |  x  |  x  |    x   |   x    |   x    |   x    |    x   |    x   |    x   |          |    x    |
|                                                 | memory of the     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board. Value      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | written/read is   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the address of    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the word. This is |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | done two times,   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | for value and     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | ~value            |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | (complement), to  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | test for all bits.|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Writes and reads  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    memStress_TEST                               | to external (DDR) |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | memory of the     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board. Walking 1's|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and walking 0's   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | tests are executed|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | on the whole DDR  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | memory            |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Writes to and     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    mmcsd_TEST                                   | read from MMCSD   |   x    |   x    |   x    |     x         |    x   |     |     |    x   |   x    |   x    |   x    |    x   |    x   |    x   |          |         |
|                                                 | memory. Passes on |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | reading back the  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | correct value as  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the one written   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Writes to and     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    mmcsdStress_TEST                             | read from MMCSD   |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | memory. Passes on |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | reading back the  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | correct value as  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the one written.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Entire SD card    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | memory starting   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | from 1.5GB offset |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | is written/read   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | during the test.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests reading and |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    nand_TEST                                    | writing to NAND   |        |        |        |               |        |  x  |     |        |        |        |        |        |        |        |          |         |
|                                                 | flash memory      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests reading and |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    norflash_TEST                                | writing to NOR    |   x    |   x    |        |               |        |  x  |     |        |        |        |        |        |        |        |          |         |
|                                                 | flash memory      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests reading and |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    norflashStress_TEST                          | writing to NOR    |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | flash memory.     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Entire NOR flash  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | memory is accessed|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | during the test.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Light up the OLED |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    oled_TEST                                    | display to verify |        |        |        |               |        |     |  x  |        |        |        |        |        |        |        |          |         |
|                                                 | functionality     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Writes and reads  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    pmic_TEST                                    | to the PMIC       |        |        |   x    |     x         |    x   |     |     |     x  |    x   |    x   |   x    |    x   |    x   |        |          |         |
|                                                 | controller. This  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | is to verify      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | ability to use    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | I2C to control    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | PMIC. Test passes |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | on successful read|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and write.        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests the Quad    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    qspi_TEST                                    | SPI by writing    |        |        |        |     x         |    x   |  x  |  x  |        |        |        |        |        |    x   |        |          |         |
|                                                 | and reading back  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the value written |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | to memory. Test   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | passes on correct |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | data read back.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests the rotary  |        |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    rotarySwitch_TEST                            | switch at the     |        |        |        |               |        |     |  x  |        |        |        |        |        |        |        |          |         |
|                                                 | 10 possible       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | positions         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Test for setting  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    rtc_TEST                                     | date and time to  |        |        |        |               |        |     |     |    x   |    x   |    x   |    x   |    x   |    x   |    x   |          |         |
|                                                 | RTC registers and |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | running the clock |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests reading     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    temperature_TEST                             | back from         |   x    |   x    |   x    |               |        |  x  |     |    x   |        |        |        |    x   |        |        |          |         |
|                                                 | temperature sensor|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | via I2C. Test     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | passes on         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | successful I2C    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | reads.            |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests reading     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    temperatureStress_TEST                       | back from         |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | temperature sensor|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | via I2C. Test     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | passes on         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | successful I2C    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | reads.            |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Test is repeated  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | for 100 cycles.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Press 'b' to stop |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the test before   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | completing test   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | cycles.           |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests uart        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    uart2usb_TEST                                | messages over usb |        |        |        |               |        |  x  |     |        |        |        |        |        |        |        |          |         |
|                                                 | port.             |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Data Path         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    uart_TEST                                    | continuity test   |   x    |   x    |   x    |    x          |    x   |  x  |  x  |    x   |    x   |    x   |    x   |    x   |     x  |    x   |          |         |
|                                                 | for UART output.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Requires user to  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | verify that       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | outputs do appear |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | on console.       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies UART port|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    uartStress_TEST                              | with large block  |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | of data transfer. |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Sends 10MB of data|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | from the board to |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | serial console.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Teraterm script   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | loops the data    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | back to the board.|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Data recieved on  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the board and     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | verified.         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | RS485 to RS232    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | coverter is needed|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | to run the test on|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | AM65xx platform.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Need to run this  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | test from CCS.    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | SD boot support is|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | not available.    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | On-board          |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    mcasp_TEST                                   | audio codec       |        |        |        |               |        |  x  |     |        |        |        |        |        |        |        |    x     |         |
|                                                 | functionality is  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | exercised by this |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | test. Audio       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | supplied at EVM   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | audio input port  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | will loopback to  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | audio output port.|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | This test is      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | intended to       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | demonstrate       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | baremetal         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | functionality of  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | mcasp, edma3 and  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | i2c CSL modules   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | without depending |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | on the LLD        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | libraries. No     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | console output is |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | supported by this |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | test.             |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Multi-channel     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    mcaspAudioDC_TEST                            | audio daughter    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |    x     |         |
|                                                 | card              |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | functionality is  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | exercised by      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | this test. Audio  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | supplied at audio |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | DC input ports    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | will loopback to  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | audio DC output   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | ports. This test  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | is intended to    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | demonstrate bare  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | metal             |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | functionality of  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | mcasp, edma3 and  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | spi CSL modules   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | without depending |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | on the LLD        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | libraries. No     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | console output is |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | supported by      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | this test.	      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Demonstrates the  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    pwm_TEST                                     | usage of PWM CSL  |        |        |   x    |               |        |  x  |     |    x   |        |        |        |        |        |    x   |          |         |
|                                                 | FL APIs by        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | configuring the   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | PWM module to     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | generate a pulse  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | of 1KHz with      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | different         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | duty cycle - 25,  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | 50 and 75%.       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies the USB  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    usbDevice_TEST                               | device mode       |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | operation of      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board under test. |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | USB modules       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | operates at high  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | speed (2.0)       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Board is exposed  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | as USB MSC device |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | to host PC during |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the test.         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies the USB  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    usbHost_TEST                                 | host mode         |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | operation of      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | boardf under test.|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | USB modules       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | operates at high  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | speed (2.0)       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | during the test.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | File write/read   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and data          |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | verification on   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the connected USB |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | device is done    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | during the test   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies the USB  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    usbHostStress_TEST                           | host mode         |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | operation of      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | boardf under test.|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | USB modules       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | operates at high  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | speed (2.0)       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | during the test.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | File write/read   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and data          |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | verification on   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the connected USB |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | device is done    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | during the test   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Test is repeated  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | for 100 cycles.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Press 'b' to stop |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the test before   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | completing test   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | cycles.           |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests the Octal   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    ospi_TEST                                    | SPI by writing    |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and reading back  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the value written |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | to memory. Test   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | passes on correct |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | data read back.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests the Octal   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    ospiStress_TEST                              | SPI by writing    |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and reading back  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the value written |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | to memory. Test   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | passes on correct |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | data read back.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Entire OSPI flash |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | memory is accessed|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | during the test.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Tests the PCIe    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    pcie_TEST                                    | interface in      |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | end point and     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | rootcomplex mode  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | using two boards. |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Data is sent from |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | one board to other|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and sent it back  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | to the first board|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | for verification. |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies boot     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    bootEeprom_TEST                              | EEPROM by writing |    x   |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | a block of data,  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | reading back      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | written data      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | for correctness.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies boot     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    bootEepromStress_TEST                        | EEPROM read/write |    x   |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | covering entire   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | memory.           |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Test for setting  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    extRtc_TEST                                  | date and time to  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | external RTC and  |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | running the clock |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Test for setting  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    extRtcStress_TEST                            | date and time to  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | external RTC and  |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | running the clock.|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Test is repeated  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | for 100 cycles.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Press 'b' to stop |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the test before   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | completing test   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | cycles.           |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies ICSSG    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    icssgEmac_TEST                               | EMAC ports in     |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | loopback with one |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | port connected to |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | another port.     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | 10 packets are    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | sent and received |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | during the test.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies ICSSG    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    icssgEmacStress_TEST                         | EMAC ports in     |   x    |   x    |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | loopback with one |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | port connected to |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | another port.     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | 10240 packets are |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | sent and received |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | during the test.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Cycles through    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    icssgLed_TEST                                | LEDs on the IDK   |        |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | application       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board.            |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Cycles through    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    icssgLedStress_TEST                          | LEDs on the IDK   |        |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | application       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board.            |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Test is repeated  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | for 100 cycles.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Press 'b' to stop |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the test before   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | completing test   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | cycles.           |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies boot mode|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    bootSwitch_TEST                              | switch by         |    x   |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | configuring boot  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | strap pins as     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | GPIOs and reading |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the pin state with|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | boot switch set in|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | different patterns|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies push     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    button_TEST                                  | buttons on the    |    x   |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board. Test       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | prompts for       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | pressing a        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | specific button   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | which will be     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | detected by the   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | test.             |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies MCAN     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    mcan_TEST                                    | ports on the      |        |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board with two    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | ports connected   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | with each other.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Data is sent from |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | one port and      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | received on       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | another port. Both|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | ports are         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | veirified for Tx  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and Rx            |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies MCAN     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    mcanStress_TEST                              | ports on the      |        |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board with two    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | ports connected   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | with each other.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | 10240 packets     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | are sent from     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | one port and      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | received on       |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | another port. Both|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | ports are         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | veirified for Tx  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | and Rx            |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies PRU UART |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    rs485_TEST                                   | port on the       |        |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board.            |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Supports board to |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board test and    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | single board test.|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | RS485 to RS232    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | coverter is needed|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | to run the test on|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | AM65xx platform   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies PRU UART |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    rs485Stress_TEST                             | port on the       |        |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board.            |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Sends 10MB of data|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | from the board to |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | serial console.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Teraterm script   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | loops the data    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | back to the board.|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Data recieved on  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the board and     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | verified.         |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | RS485 to RS232    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | coverter is needed|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | to run the test on|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | AM65xx platform.  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 |                   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Need to run this  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | test from CCS.    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | SD boot support is|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | not available.    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+
|                                                 | Verifies basic    |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|    Power On Self Test                           | memory devices    |   x    |    x   |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | on the board and  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | displays the      |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | board ID details. |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Executed on boot  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | automatically     |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | before displaying |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | diag main menu.   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | Can be skipped by |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | entering 'b' in   |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | the serial console|        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | within 5 secs of  |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
|                                                 | diag boot.        |        |        |        |               |        |     |     |        |        |        |        |        |        |        |          |         |
+-------------------------------------------------+-------------------+--------+--------+--------+---------------+--------+-----+-----+--------+--------+--------+--------+--------+--------+--------+----------+---------+

| Some diagnostic applications expect additional jumpers or hardware
  settings to complete. Refer to below section.

Additional Jumper or Hardware Settings
----------------------------------------

Current Monitor
^^^^^^^^^^^^^^^^

For iceK2G, this test expects J16 and J17 to be connected with jumper
shunts. This enables the current monitors to be used.

GMAC
^^^^^

For idkAM572x, idkAM571x, idkAM574x and evmAM572x, this test expects
loopback plugs to be used on both Ethernet ports. These loopback plugs
will loopback the TX lines back to the RX lines. The Ethernet ports are
the RJ-45 connectors labeled "Ethernet" on the board.

ICSS EMAC
^^^^^^^^^^

For idkAM572x, idkAM574x and idkAM571x, this test expects loopback plug
to be used on J6. These loopback plugs will loopback the TX lines back
to the RX lines. For iceK2G, this test expects loopback plugs to be used
on all four ICSS EMAC ports.

LCD Touchscreen
^^^^^^^^^^^^^^^^^^

For idkAM572x, idkAM574x and idkAM571x, this test expects the LCD module
to be connected. This requires the two ribbon cables (one for display,
one for the capacitive-touch IC) to be connected.

McSPI
^^^^^^^

For idkAM572x, idkAM574x and idkAM571x, this test expects pins to be
connected to the Industrial I/O header. The Industrial I/O header, J37,
has two columns in parallel, one of which is the McSPI input and the
other being VDD. Thus, connecting any row with a jumper will yield a '1'
read on that McSPI input. By connecting the first, second, third, and
forth row with jumpers would yield 0x1, 0x2, 0x4, and 0x8 being read
respectively.

PWM
^^^^^

PWM output generated while running the diagnostic test can be verified
at below pins.

evmK2G - J12 pin 33

evmAM572x - P17 pin 5

idkAM437x - J16 pin 14

evmAM335x - J5 pin 13

