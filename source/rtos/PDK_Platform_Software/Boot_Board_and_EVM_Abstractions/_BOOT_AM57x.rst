.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_BOOT_AM57x

Overview
^^^^^^^^^

The Secondary Bootloader (SBL) for AM57xx device initializes the
execution environment for multi-core application and this can be used to
demonstrate an out-of-box experience.The section covers additional
details including execution sequence, tools and additional flashing
instructions.

Bootloader Execution Sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **Power On Reset**
-  **ROM Bootloader (RBL)**

   -  Software pre-programmed in ROM memory starts executing
   -  Checks Sysboot pins and choose booting device
   -  If no valid bootloader found on booting device, RBL checks for
      next booting device.
   -  Platform configuration and initialization.
   -  Configures DPLL and clock settings for MPU, and boot media like
      I2C, MMCSD, SD/MMC, SPI, QSPI, Ethernet etc for reliable boot.
   -  The sequence depends on RBL execution flow and Sysboot pins.
   -  RBL gets image size and load address by checking TI Image Header
      appended on bootloader binary(.bin). Check binary formats.
   -  Loads the binary to internal memory at the Load address fetched
      from TI Image Header
   -  Passes control to Secondary Bootloader(SBL)

.. note::
   Detailed description of ROM bootloader is provided in Initialization
   Chapter in `AM57xx Technical Reference
   manual <http://www.ti.com/lit/pdf/spruhz6>`__

-  **Secondary bootloader(SBL)**

   -  User level secondary bootloader(SBL) begins execution from
      internal memory by running basic initialization routines like
      setting up Stack, BSS and then jumps to main() to begin Board
      Initialization.
   -  Board Initialization is done by a call to **Board_init()** API.For
      additional details refer `Processor SDK Board
      Support <index_board.html#board-support>`__.
   -  It includes setting up PLLs, enabling clocks to all interfaces and
      modules, performing pinmux and setting up UART console.
   -  Once Board Initialization is complete, it enables clocks to the
      target cores like C66x/DSP, IPU, etc and brings them out of reset.
   -  Parses Multicore Application image located in memory device and
      copies it to DDR memory based on load address for different
      sections.
   -  Once copy is successful it transfers control to application.

-  **Application then starts executing from DDR**.

.. note::

    -  RBL requires boot loader to be in a special format with a header
       appended to the binary image. The header shall contain the load
       address of the bootloader and size of the bootloader image.
    -  For more information on the TI header refer TRM document

Directory structure
^^^^^^^^^^^^^^^^^^^^

**Makefiles:**

-  **PDK_INSTALL_PATH/ti/boot/sbl/board/<EVAL_BOARD>/build**: Makefile
   for bootloader that provides list of source files and library and
   compiler options to create bootloader binary.

**Source Files:**

-  **PDK_INSTALL_PATH/ti/boot/sbl/board/<EVAL_BOARD>**: Source to SBL
   main function that consolidates all features
-  **PDK_INSTALL_PATH/ti/boot/sbl/soc**: Source to SOC specific
   initialization used in the SBL.
-  **PDK_INSTALL_PATH/ti/boot/sbl/src**: Source to boot media specific
   initialization used in the SBL.

|

Tools and Binary Formats
^^^^^^^^^^^^^^^^^^^^^^^^^^

This section lists out the various tools and scripts used by SBL for
different boot modes and those required to create a bootable application
image.

**SBL/MLO image format:**
To generate the *MLO*, SBL uses tiImageGen tool to prepend the sbl.bin
image with the TI header information. The image format has been
described in detail in the Image Format Section of the\ `AM57xx
Technical Reference manual <http://www.ti.com/lit/pdf/spruhz6>`__

|
**Application image format:**
A bootable application image can be created by using the Am57xImageGen
script provided under tools folder as part of sbl. It can be located at
*<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/scripts* folder.

The Am57xImageGen script uses out2rprc and multicoreImageGen format
conversion tools to create the final application image. Graphical view
of the multicore application image is provided below:

.. Image:: /images/Multicore_app_image.png

The script creates the bootable image in 2 steps

**Step 1: Conversion to RPRC format conversion**

-  Firstly, application executable is converted from ELF/COFF format
   (.out) to custom TI Rprc binary image using out2rprc tool. This tool
   strips out the initialized sections from the executable file (i.e.
   \*.out) and places them in a compact format that the SBL can
   understand. The output (bin) file is typically much smaller than the
   original executable (out) file.
-  The rprc files are intermediate files in a format that is consumed by
   MulticoreImageGen tool that generates the final binary.

**RPRC File Header Format**

+------------+----------------------------+
| Offset     | Binary value               |
+============+============================+
| 0x00000000 | **Magic Word(43525052)**   |
+------------+----------------------------+
| 0x00000004 | **Entry Point (Location)** |
+------------+----------------------------+
| 0x00000008 | **Reserved Addr**          |
+------------+----------------------------+
| 0x0000000C | **Section Count**          |
+------------+----------------------------+
| 0x00000010 | **Version**                |
+------------+----------------------------+

**RPRC Section Header Format**

+------------+---------------------------+
| Offset     | Binary value              |
+============+===========================+
| 0x00000000 | **Section start Address** |
+------------+---------------------------+
| 0x00000004 | **Reserved Addr**         |
+------------+---------------------------+
| 0x00000008 | **Size**                  |
+------------+---------------------------+
| 0x0000000C | **Reserved CRC**          |
+------------+---------------------------+
| 0x00000010 | **Reserved**              |
+------------+---------------------------+

|
**Step 2: Multicore Image file generation**

-  RPRC files for each cores is combined into a single multicore
   bootable application image.

**Multicore boot image format**

**Meta Header Start**

+------------+-------------------------------+
| Offset     | Binary value                  |
+============+===============================+
| 0x00000000 | **Magic String (0x5254534D)** |
+------------+-------------------------------+
| 0x00000004 | **Number of Files**           |
+------------+-------------------------------+
| 0x00000008 | **Device ID**                 |
+------------+-------------------------------+
| 0x0000000C | **Reserved**                  |
+------------+-------------------------------+

**Meta Header per Core**

+------------+------------------+
| Offset     | Binary value     |
+============+==================+
| 0x00000000 | **Core ID**      |
+------------+------------------+
| 0x00000004 | **Image Offset** |
+------------+------------------+

Core ID and Device ID for specific devices can be located in the file
sbl_target_core_boot.h in the boot/sbl/soc/<SOC_NAME> folder

Refer section `App Image
Creation <index_Foundational_Components.html#application-image-creation>`__
for more details on usage of this script and application image creation.

**Flashing Tools**


SBL provides a CCS based qspi flash writer utility to flash image and
multicore AppImage from a SD card to onboard QSPI device. It
is located at *<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashWriter/qspi*


Building the SBL
^^^^^^^^^^^^^^^^^^^^

**Pre-requisites to Building**

-  Set your environment using pdksetupenv.bat or pdksetupenv.sh. Refer
   to the Processor SDK RTOS Building page for information on setting up
   your build environment
-  The SBL has following dependencies and will need the following
   libraries built

   -  Board
   -  UART
   -  I2C
   -  SPI
   -  CSL
   -  OSAL
   -  MMCSD
   -  PM

.. note::
   Refer to the makefile for the board you are using for the latest driver
   dependency. These libraries should come pre-built with any fresh
   installation of the Processor SDK RTOS but may be removed if a gmake
   clean is invoked

**Compiling the SBL Components**

To build the SBL components:

#. **cd <PDK>/packages**
#. **Run pdksetupenv script**
#. **make all -C ti/boot/sbl BOARD=<BOARD_NAME> SOC=<SOC_NAME> BOOTMODE=<BOOTMEDIA>**

-  BOARD_NAME : idkAM572x, idkAM571x, evmAM572x, idkAM574x
-  SOC_NAME : AM572x, AM571x, AM574x

SBL can be built for all the AM57x platforms using below command

#. **cd <PDK>/packages**
#. **Run pdksetupenv script**
#. **cd <PDK>/packages/ti/boot/sbl**
#. **make all_sbl_images SBL_PLATFORM=am57xx**

This will make the SBL for a specific $BOARD and $BOOT_MEDIA. Output
files will be located in: **<PDK>/packages/ti/boot/sbl/binary/<BOARD>**

.. note::
   Refer **<PDK>/packages/ti/boot/sbl/sbl_<DEVICE>.sh** for more build
   options


.. rubric:: Boot Modes
   :name: boot-modes

This Release of SBL supports MMCSD and QSPI Boot modes. The different
boot modes supported for all the boards is tabulated in the table below.

+-----------------------+--------+------+------+
|                       | MMCSD  | QSPI | eMMC |
+-----------------------+--------+------+------+
| AM572x GPEVM          |  YES   | NO   | YES  |
+-----------------------+--------+------+------+
| AM572x IDKEVM         |  YES   | YES  | NO   |
+-----------------------+--------+------+------+
| AM571x IDKEVM         |  YES   | YES  | NO   |
+-----------------------+--------+------+------+
| AM574x IDKEVM         |  YES   | YES  | NO   |
+-----------------------+--------+------+------+

|

Booting Via SD Card
""""""""""""""""""""""

#. Preparing the SD card.
#. Booting the target.

Preparing the SD card 
'''''''''''''''''''''''

#. To boot the target the SD card should be bootable. Follow the steps
   at `Creating bootable SD card in windows <index_overview.html#windows-sd-card-creation-guide>`__
   or `Creating bootable SD card in Linux <index_overview.html#linux-sd-card-creation-guide>`__.
#. Delete the "MLO" and "app" in the bootable SD card which are created
   in the process of making the SD bootable.
#. Copy the sbl binary(MLO) to the SD card.
#. Copy the Application image(app) generated using the
   `Script <index_Foundational_Components.html#application-image-creation>`__
   to the SD card.

Booting the target
''''''''''''''''''''

#. Insert micro SD card into the SD card slot of the board.
#. Open a serial communication terminal like TeraTerm, MiniCom on host
   PC and connect to the UART console port
#. Do a power reset of the board to boot the appliation from the SD
   card.

Booting Via eMMC
""""""""""""""""""""""

#. Preparing the eMMC.
#. Booting the target.

Preparing the eMMC 
'''''''''''''''''''

#. To format the eMMC of the target board, Run the following application on the target board
   `USB_DevMsc_mmcsd <Device_Drivers.html#id6>`__ .
#. To boot the target the eMMC should be bootable. Follow the steps same as SD card
   formatting as given
   at `Creating bootable SD card in windows <Overview.html#windows-sd-card-creation-guide>`__
   or `Creating bootable SD card in Linux <Overview.html#linux-sd-card-creation-guide>`__
   except instead of SD card, connect the target board eMMC to the host PC.
#. Delete the "MLO" and "app" in the bootable eMMC which are created
   in the process of making the eMMC bootable.
#. Copy the sbl binary(MLO) to the eMMC.
#. Copy the Application image(app) generated using the
   `Script <Foundational_Components.html#application-image-creation>`__
   to the eMMC.

Booting the target
''''''''''''''''''''

#. Set boot settings to eMMC by selecting J3, J4 and J6 jumpers on Pin 2 and 3
   of AM572x EVM Board.
#. Ensure there is no SD card inserted in the SD card slot.
#. Open a serial communication terminal like TeraTerm, MiniCom on host
   PC and connect to the UART console port
#. Do a power reset of the board to boot the appliation from the eMMC.

Booting Via QSPI
""""""""""""""""""
Booting from QSPI flash involves two steps-

#. Flashing bootloader and app image to QSPI flash.
#. Booting the target.

Preparing Flash Device
''''''''''''''''''''''''

Use the CCS based qspi_flash_writer.out utility provided in
<*TI_PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashwriter/qspi/<Board>'*
to flash the SBL image at offset 0 and application image at offset
0x80000 to the QSPI device.

QSPI device Memory Map:

+----------------+-----------------------------+
| Offset 0x00    | SBL                         |
+----------------+-----------------------------+
| Offset 0x80000 | Application Multicore Image |
+----------------+-----------------------------+

The images can be flashed into QSPI flash by following steps given
below.

#. Copy QSPI mode SBL image
   *<TI_PDK_INSTALL_DIR>/packages/ti/boot/sbl/binary/<BoardName>/qspi/bin/MLO*
   and application image(app) generated using the Script into the SD
   card.
   Rename the bootloader file to 'boot' and application image to 'app'
   with no extensions. 
#. Copy 'config' file into the SD card, the config file should contain
   names of the image to be flashed and the offset.
   A sample config file can be found at
   *<TI_PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashWriter/qspi/config*.
   Do not change the name of the config file.
   **NOTE:** "config" file can be used without any modifications if
   bootloader and application images are renamed to "boot" and "app".
   **NOTE:** Do not rename the bootloader to be copied to SD card as
   "MLO", as MMCSD bootloader expects "MLO" and "app" to boot.
#. Now SD card contains 3 files 1)boot 2)app 3)config files.
   config file contains the address of boot image as 0x0 and app image
   as 0x80000.
   Insert it into the SD card slot.
#. Connect the board with CCS and and load the prebuilt qspi flash
   writer application from
   <TI_PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashWriter/qspi/bin/<BoardName>
#. Run the QSPI flash writer application. You will see the following
   logs on the EVM's UART console.
#. After the images have been flashed to the QSPI device disconnect from
   CCS and do a power reset to boot from the QSPI memory. 

::

    PDK QSPI Flash Writer!!
    Copying boot to QSPI Flash
    Copying app to QSPI Flash
    Changing read to quad mode
    Read mode has been changed to Quad mode
    SUCCESS!!!
    Flashing completed


.. note::

   -  The file names have to be renamed in such a way that the length of
      name is less than 9 characters. Any file name less than 9 characters
      can be used.
   -  This application will flash the image at required offset without
      taking into consideration any overwriting to previously flashed
      image.
   -  It is the responsibility of the user to provide proper offsets.


Test Application
^^^^^^^^^^^^^^^^^^

SBL provides a test application to demonstrate booting of multicore
application image on A15 and DSP cores.The multicore sample
application uses mailbox for inter-processor communication. It is used
to validate the multi-core boot-up use case.

Master application sends wake-up message to the DSP target cores & waits
for acknowledgement message from the target cores in an infinite
loop.Each target DSP core waits for wake-up message from the master core 
responds back with an acknowledgement message.

Application Image Creation
"""""""""""""""""""""""""""""
Application Image creation involves two steps.

#. Generating the .outs of applications for individual cores
#. Combining the .outs of individual cores to create a bootable
   multicore image

The steps to create the bootable image in Linux and Windows environment
are listed below.

.. note::
   -  Valid SOC settings are AM571x/AM572x
   -  Valid BOARD settings are evmAM572x/idkAM571x/idkAM572x

Linux Environment
"""""""""""""""""""
Command to build the test application.

::

    Go to cd (TI_PDK_INSTALL_DIR)\packages\ti\boot\sbl

    make example BOARD=<BOARD> SOC=<SOC> to build the application
    make example_clean BOARD=<BOARD>

Example:

::

    make example BOARD=idkAM572x SOC=AM572x

To create the final bootable application image use the AM57xImageGen
script and follow these steps

1. Set the following environment variable in the shell.  BIN_PATH:
Pointing to the path where the AppImage needs to be generated

::

    Ex: export BIN_PATH=$(TI_PDK_INSTALL_DIR)/packages/ti/boot/sbl/binary

2. Edit the script file to point to the application elf files by setting
the input application variables. 

App_MPU_CPU0: Point to the path where the application .out for A15 MPU is located
App_DSP1: Point to the path where the dsp core 1 application is located
App_DSP2: Point to the path where the dsp core 2 application is located

::

    export APP_MPU_CPU0=$(TI_PDK_INSTALL_DIR)/packages/ti/boot/sbl/binary/idkAM572x/example/armv7/bin/sbl_app.out

    export APP_DSP1=$(TI_PDK_INSTALL_DIR)/packages/ti/boot/sbl/binary/idkAM572x/example/c66/dsp1/bin/sbl_app.xe66

    export APP_DSP2=$(TI_PDK_INSTALL_DIR)/packages/ti/boot/sbl/binary/idkAM572x/example/c66/dsp2/bin/sbl_app.xe663

    export APP_IPU1_CPU0=$(TI_PDK_INSTALL_DIR)/packages/ti/boot/sbl/binary/idkAM572x/example/m4/ipu1/bin/sbl_app.xem4

    export APP_IPU1_CPU0=$(TI_PDK_INSTALL_DIR)/packages/ti/boot/sbl/binary/idkAM572x/example/m4/ipu2/bin/sbl_app.xem4

3. If it is not required to load an application on specific core leave
the variable blank.

4. Run the script file AM57xImageGen found under the path $(TI_PDK_INSTALL_DIR)/packages/ti/boot/sbl/tools/scripts

5. An application image by name app is created in the path pointed by
BIN_PATH variable

6. Copy the Bootlaoder image(MLO) and application(app) in the SD card to
boot using MMCSD boot mode.

.. note::

   -  The AM57xImageGen.sh script depends on tools like mono to execute the
      out2rprc.exe.
   -  The linux host environment needs to have this tool installed to
      execute this script.
   -  Refer this link to download the
      `mono <http://www.mono-project.com>`__ tool

Windows environment
"""""""""""""""""""""
Command to build the test application.

::

    Go to cd (TI_PDK_INSTALL_DIR)\packages\ti\boot\sbl

    gmake example BOARD=<BOARD> SOC=<SOC> to build the application
    gmake example_clean BOARD=<BOARD>

Example:

::

    gmake example BOARD=idkAM572x SOC=AM572x

To create the final bootable application image use the AM57xImageGen
script and follow these steps

1. Set the following environment variable in windows command prompt

BIN_PATH: Pointing to the path where the AppImage needs to be generated 

::

    Ex:  set BIN_PATH=%TI_PDK_INSTALL_DIR%\packages\ti\boot\sbl\binary

2. Edit the batch file to point to the application elf files by setting
the input application variables.

App_MPU_CPU0: Point to the path where the application .out for A15 MPU is located
App_DSP1: Point to the path where the dsp core 1 application is located
App_DSP2: Point to the path where the dsp core 2 application is located

::

    set App_MPU_CPU0=%TI_PDK_INSTALL_DIR%\packages\ti\boot\sbl\binary\idkAM572x\example\armv7\bin\sbl_app.out

    set App_DSP1=%TI_PDK_INSTALL_DIR%\packages\ti\boot\sbl\binary\idkAM572x\example\c66\dsp1\bin\sbl_app.xe66

    set App_DSP2=%TI_PDK_INSTALL_DIR%\packages\ti\boot\sbl\binary\idkAM572x\example\c66\dsp2\bin\sbl_app.xe66

    set App_IPU1_CPU0=%TI_PDK_INSTALL_DIR%\packages\ti\boot\sbl\binary\idkAM572x\example\m4\ipu1\bin\sbl_app.xem4

    set App_IPU2_CPU0=%TI_PDK_INSTALL_DIR%\packages\ti\boot\sbl\binary\idkAM572x\example\m4\ipu2\bin\sbl_app.xem4

3. If it is not required to load an application on specific core leave
the variable blank.

4. Run the batch file AM57xImageGen found under the path $(TI_PDK_INSTALL_DIR)/packages/ti/boot/sbl/tools/scripts

5. Follow the steps 4 to 6 listed above for Linux environment.
|
Setup Requirements
""""""""""""""""""""
For information on board specific requirements like power supply, UART
console port connections refer the Hardware User guide of the respective
boards.

The configurations needed to setup UART console through a serial
terminal application on host PC are listed in the next section.

UART Console Setup
'''''''''''''''''''
PDK SBL prints messages on the UART Serial Console running on the host.
Hence, a serial terminal application (like Tera
Term/HyperTerminal/minicom) should be running on the host.

The host serial port must be configured at 115200 baud, no parity, 1
stop bit and no flow control.
Please ensure that the local echo setting for the terminal is turned off.

Loading the test application
''''''''''''''''''''''''''''''
Follow these steps to load the test application using a SD card on the
target

copy the MLO to your SD card (located
at $(TI_PDK_INSTALL_DIR)/packages/ti/boot/sbl/binary/[BOARD]/mmcsd)

#. copy the example app located at path pointed to by BIN_PATH to your
   SD card
#. insert your SD card into your board and power on your board
#. open teraterm to connect to the board's UART console
#. press the "Hard Reset" button on your board

On Successful bootup you should see the following logs on the UART
console for a AM572x based board.

.. Image:: /images/Sbl_example.jpg

.. note::
   MPU Core 0 example does a sequential check of mailbox messages sent from
   the other cores. On rare occasions, the check happens before the message
   is sent - the "<core> boot-up Successful" message might not be displayed
   even though the core(s) were booted successfully.

Application Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^

Memory Map
""""""""""""

Table indicated below provides memory map details for SBL image in
OCMC_RAM1.  For more details on pinmux and IO delay requirements refer
this link `Processor SDK Board
Support <index_board.html#board-support>`__

We recommend that users should refer to the linker command file and the
map file for the boot loader to check for latest information on the
memory utilization in the boot loader.

**Location of linker command file**:
<PDK_INSTALL_PATH>/packages/ti/boot/sbl/board/<BOARD>/build

The SBL memory map is shown below

.. Image:: /images/SBL_memory_map.png

..  note::
   -  After the application boots and is running on the SOC, it is free to
      use the SBL_MEM region.
   -  The pinmux data from the board library and MMU Table are part of the
      SBL_MEM region indicated in the figure above. If pinmux data needs to
      be placed at a specific location then users can update the SBL linker
      command file to add the BOARD_IO_DELAY_CODE and BOARD_IO_DELAY_DATA
      as described in `Application Integration of board library for
      AM5x <index_board.html#application-integration-for-am5x-dra7xx>`__


SBL Customization
^^^^^^^^^^^^^^^^^^^

Changing boot media offsets
"""""""""""""""""""""""""""""
The location at which SBL resides on the flash is predefined by the ROM
bootloader spec and so these defaults can`t be changed. However the SBL
is a user defined bootloader so many of the defaults can easily be
modified to meet application requirements. For example the flash offset
location from which the bootloader reads the application is configured
in the source files located under
<PDK_INSTALL_PATH>/packages/ti/boot/sbl/src/<BOOT_MEDIA>

Examples of customization that can be changed:

- QSPI/SPI flash offsets: These offsets are configured in sbl_qspi.c and
  sbl_spi.c

- MMCSD: The name of the application is hard coded as app in function
  SBL_MMCBootImage in the sbl_mmcsd.c

Speeding up boot by increasing speed of the boot interface
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
The SBL for AM57xx devices uses LLD drivers to read and write from boot
media supported. The SBL uses the default SOC configuration of the
drivers and the speeds setup. For example, the SPI driver default SPI
bitrate is 1 MHz (Refer
<PDK_INSTALL_PATH>/packages/ti/drv/spi/src/SPI_drv.c) so if you wish to
speed up boot you can update the SPI parameter in the SBL as shown
below:

::

     SPI_Params_init(&spiParams);
     spiParams.bitRate = 24000000U;

The configuration of the driver is usually done in the
boot/sbl/soc/<device>/sbl_soc.c file.

-  **For SD/MMC**: You can configure higher speed and change bus width
   using MMCSD_v1_HwAttrs_s or MMCSD_v0_HwAttrs_s
-  **For QSPI**: 2 pin and 4 pin mode, and input frequency is configured
   using QSPI_HwAttrs in the QSPI driver. Check driver for defaults.

Also, check to see if the CACHE and MMU settings for the ARM core are
setup to enable fast boot.

.. note::
   **SYSBOOT settings for AM57xx**

   The SYSBOOT configuration in your hardware using Sitara devices
   (AM3/AM4/AM5) can play a big role in the time required to boot
   successfully. On these devices the boot pins configure a boot sequence
   for the ROM bootloader to check for valid boot image so if you have a
   preferred boot mode designers are required to use SYSBOOT setup such
   that the preferred boot media is first in the boot sequence. If the
   preferred boot media occurs later boot sequence, the boot is likely to
   add the time required by RBL to check other boot media for an valid
   image. For example if QSPI is the preferred boot media on your AM57xx
   hardware then you should have system configure SYSBOOT to boot of QSPI
   first using SYSBOOT setting for QSPI_1 or QSPI4 for Memory preferred
   booting or Production booting (Refer: Initialization chapter in
   TRM).Incorrect SYSBOOT configuration can causes long delays especially
   if peripheral boot is configured to be one of the preferred boot modes
   in the boot order


Reducing size of SBL and application
"""""""""""""""""""""""""""""""""""""
Another way to optimize boot times is to reduce the size of the binary
that needs to be loaded by the bootloader by building the app with
optimization for code size using -Os (GNU GCC) and for -O<level> when
using TI compilers.

Other than compiler based optimizations developers can actively shutdown
non-essential modules and features to reduce code size. For example if
UART logging is not required or DDR memory is not connected in the
system, the initialization functions can be removed to reduce code size.

Usage Notes
^^^^^^^^^^^^^

SBL AVS and ABB setup
""""""""""""""""""""""
AVS and ABB configuration is mandated for normal operation of AM57xx
devices. All Processor SDK RTOS releases v3.3 and later contain SBL that
sets up AVS and ABB configuration features using PM LLD APIs The
complete details of PMIC configuration and AVS and ABB configuration
required by the chip for different OPP has been implemented in the file:

<PDK_INSTALL_PATH>/packages/ti/boot/sbl/board/src/sbl_avs_config.c If you
are using the same PMIC as GP EVM or IDK platform then you can reuse the
settings as is in SBL for your custom platform

Configuring entry point for SBL
""""""""""""""""""""""""""""""""

The two key files that help setup the entry point in the SBL build are
"sbl/soc/<SOC_NAME>/sbl_init.S" and the linker command file
"sbl/soc/<SOC_NAME>/linker.cmd". The global symbol Entry is used to
provide the entry point to the SBL. The Base address of the memory
section SBL_MEM is then used by the tiimage and GP Header tool to
provide RBL the guidance to find the entry point to pass control. After
MLO is created check the TI image format file(MLO or \_ti.bin) or the GP
Header file to confirm that the entry point matches the location of
Entry symbol in the sbl.map

.. note::
   The object file created by sbl_init.S should always be the first object
   file in the link order for the symbol Entry to be placed at the BASE
   address of the memory section SBL_MEM


Debugging application boot
""""""""""""""""""""""""""""
Steps to debug application boot using Processor SDK RTOS bootloader are
discussed in the article `Common steps to debug application
boot <index_Foundational_Components.html#common-steps-to-debug-application-boot>`__

