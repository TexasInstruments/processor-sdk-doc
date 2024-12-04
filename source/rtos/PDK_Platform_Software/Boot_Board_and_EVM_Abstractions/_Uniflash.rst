
Introduction
^^^^^^^^^^^^^^
Uniflash is an Unified Flashing tool which provides utilities for flashing the application software
images to non-removable flash devices on TI hardware platforms.

Uniflash for TI processors platform includes two components

 - Flash Programmer
 - Host utility

Flash porgrammer runs on target platform which takes care of receiving the images from Uniflash host
utility and programming them onto flash devices. Flash programmer communicates with Uniflash host utility
over the UART interface.

Flash programmer which is part of the Uniflash release can be found at - "<Uniflash Root>/processors/FlashWriter/<Board Name>"

Host utility runs on host machine which provides Command-line Interface (CLI) to communicate with flash programmer.
Windows and Linux are the supported OS platforms for running Uniflash host utility. Host utility uses UART or JTAG
interface to download the flash programmer to the target platform. All data transfers between
Uniflash host utility and Flash programmer happens over UART interface.

Refer to `Uniflash Documentation <http://processors.wiki.ti.com/index.php/Category:CCS_UniFlash>`__
for more details on Uniflash tool.


Supported Platforms
^^^^^^^^^^^^^^^^^^^^
Below table shows the platforms supported by Uniflash and flash devices supported on each platform.
Download mode indicates the mode of communication for downloading flash programmer to target platform.

+----------------+----------------+------------------+---------------+------+------+---------------------------+
|      SOC       |    SOC Core    |    PLATFORM      |    FLASH DEVICE             |       DOWNLOAD MODE       |
|                |                |                  +-------+-------+------+------+------+--------------------+
|                |                |                  | SPI   | QSPI  | OSPI | EMMC | UART |       JTAG         |
|                |                |                  |       |       |      |      |      +------------+-------+
|                |                |                  |       |       |      |      |      |Uniflash CLI| Manual|
+================+================+==================+=======+=======+======+======+======+============+=======+
| AM335x         | Cortex-A8      | AM335x GP EVM    |   X   |       |      |      |   X  |     X      |       |
|                |                +------------------+-------+-------+------+------+------+------------+-------+
|                |                | AM335x ICEv2     |   X   |       |      |      |      |     X      |       |
|                |                +------------------+-------+-------+------+------+------+------------+-------+
|                |                | AMIC110 ICE      |   X   |       |      |      |   X  |     X      |       |
+----------------+----------------+------------------+-------+-------+------+------+------+------------+-------+
| AM437x         | Cortex-A9      | AM437x IDK       |       |   X   |      |      |      |     X      |       |
+----------------+----------------+------------------+-------+-------+------+------+------+------------+-------+
| AM571x         | Cortex-A15     | AM571x IDK       |       |   X   |      |      |      |     X      |       |
+----------------+----------------+------------------+-------+-------+------+------+------+------------+-------+
| AM572x         | Cortex-A15     | AM572x IDK       |       |   X   |      |      |      |     X      |       |
+----------------+----------------+------------------+-------+-------+------+------+------+------------+-------+
| AM574x         | Cortex-A15     | AM574x IDK       |       |   X   |      |      |      |     X      |       |
+----------------+----------------+------------------+-------+-------+------+------+------+------------+-------+
| K2G            | Cortex-A15     | K2G GP EVM       |       |   X   |      |      |      |     X      |       |
|                |                +------------------+-------+-------+------+------+------+------------+-------+
|                |                | K2G ICE          |       |   X   |      |      |      |     X      |       |
+----------------+----------------+------------------+-------+-------+------+------+------+------------+-------+
| AM65XX         | Cortex-R5      | AM65xx EVM       |       |       |   X  |   X  |   X  |            |   X   |
|                |                +------------------+-------+-------+------+------+------+------------+-------+
|                |                | AM65xx IDK       |       |       |   X  |   X  |   X  |            |   X   |
+----------------+----------------+------------------+-------+-------+------+------+------+------------+-------+
| J721E          | Cortex-R5      | J721E EVM        |       |   X   |   X  |   X  |   X  |            |   X   |
+----------------+----------------+------------------+-------+-------+------+------+------+------------+-------+


where,

 - X  : Supported

.. note:: For the platforms which support both UART and JTAG mode, UART is the recommended mode for
          downloading flash programmer. JTAG mode is supported along with UART for debug purpose.


Getting Started with Uniflash
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Downloads
"""""""""""
Latest version of Uniflash can be downloaded `here <http://www.ti.com/tool/download/UNIFLASH>`__


Command Options
""""""""""""""""
Uniflash CLI supports set of commands and configuration flags which are provided through dslite script.
Run the help command as described below to see all the options supported by Uniflash.

For Windows
::

        # cd <Path to Uniflash Root Folder>
        # dslite.bat --mode processors -h



For Linux

::

        # cd <Path to Uniflash Root Folder>
        # sudo ./dslite.sh --mode processors -h



This will display help menu.
Following is the sample output for help command.
::

    For more details and examples, please refer to the UniFlash Quick Start guide.


        ----------------------------------------------------------------------------
        ProcessorSDKSerialFlash CLI Tool
        Copyright (C) 2017-2019 Texas Instruments Incorporated - http://www.ti.com/
        Version 1.2.0.0
        ----------------------------------------------------------------------------

        Displaying Help..

        Usage:
        dslite.bat --mode processors -c <COM_Port> -f <Path_to_the_file_to_be_transfered> -d <Device_Type> -i <Image_Type> -e <erase_length> -o <Offset>

        Device_Type:
        0 - NAND
        1 - SPI
        2 - QSPI
        3 - OSPI
        4 - eMMC
        5 - HyperFlash
        6 - UFS

        Image_Type:
        0 - Flash
        1 - MLO
        2 - Uboot
        3 - UImage
        4 - Firmware
        5 - Custom Image

        erase_length:Length in Bytes

        Note: File Path should not be specified for Flash Erase command


.. note::

           Offset option(-o) expects hexadecimal value by default.
           The offset value can be provided with or without "0x"


Uniflash Execution Steps
"""""""""""""""""""""""""
Uniflash provides two modes of communication for downloading the flash programmer - UART and JTAG.
In JTAG mode Uniflash commnad-line interface is supported for most of the platforms.
Manual loading of the flash programmer through CCS is required for few cases.
Below diagram shows the execution steps for flashing the application images based on the Uniflash
supported mode for downloading the flash programmer.

.. Image:: /images/Uniflash_Execution_Steps.png
    :width: 650px
    :align: center
    :height: 1000px

Check the `Supported Platforms <index_board.html#supported-platforms>`__ for details of the mode of communication supported for
downloading the flash programmer on each platform.


Downloading Flash Programmer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UART Load
"""""""""""
Follow below steps for downloading the flash programer over UART

 - Confgure boot mode of the target platform to UART boot.
 - Connect UART serial port of the target platform to host PC
 - Power cycle the target platform
 - Open a serial console application (Minicom, TeraTerm etc) on host PC and configure it for 115200 baud 8n1.
 - Make a note of the COM port number on which character 'C' is getting printed. This COM port number shall be used
   in all the command inputs to Uniflash host utility.
 - Close all the serial console applications on host PC.
 - If the host PC is running Windows OS, disconnect the serial console cable from the board and reconnet before proceeding to next steps.
 - Run below commands on the Host PC from Uniflash root folder

For Windows
::

        # cd <Path to Uniflash Root Folder>
        # dslite.bat --mode processors -c <COM Port> -f <Flash Programmer Binary with Full Path> -i 0
        Example:
        # dslite.bat --mode processors -c COM10 -f <Uniflash Root>\processors\FlashWriter\am65xx_evm\uart_am65xx_evm_flash_programmer.tiimage -i 0


For Linux

::

        # cd <Path to Uniflash Root Folder>
        # sudo ./dslite.sh --mode processors -c <COM Port> -f <Flash Programmer Binary with Full Path> -i 0
        Example:
        # sudo ./dslite.sh --mode processors -c /dev/ttyUSB1 -f <Uniflash Root>/processors/FlashWriter/am65xx_evm/uart_am65xx_evm_flash_programmer.tiimage -i 0

.. note:: Specifying the image type with -i option is mandatory while downloading the flash programmer.

Uniflash CLI shows the progress of file transfer on the command console.
Following is the sample output for downloading Flash programmer over UART.

::

        C:\ti\uniflash_5.2.0>dslite.bat --mode processors -c COM10 -f C:\ti\uniflash_5.2.0\processors\FlashWriter\am65xx_evm\uart_am65xx_evm_flash_programmer.tiimage -i 0
        Executing the following command:
        > C:\ti\uniflash_5.2.0\processors\ProcessorSDKSerialFlash.exe -c COM10 -f C:\ti\uniflash_5.2.0\processors\FlashWriter\am65xx_evm\uart_am65xx_evm_flash_programmer.tiimage -i 0

        For more details and examples, please refer to the UniFlash Quick Start guide.


        ----------------------------------------------------------------------------
        ProcessorSDKSerialFlash CLI Tool
        Copyright (C) 2017-2019 Texas Instruments Incorporated - http://www.ti.com/
        Version 1.2.0.0
        ----------------------------------------------------------------------------
        Downloading Flash Programmer..

        Enabling SysFw transfer!!!

        Transferring File of size 182621 bytes
        File Transfer complete!
        Header Transfer complete
        Transferring System Firmware..
        Transferring File of size 263083 bytes
        File Transfer complete!

|
 - After successful download of the flash programmer, `Program the flash device <index_board.html#programming-the-flash-device>`__
   or `Erase the flash device <index_board.html#erasing-the-flash-device>`__
   by following the steps described in the corresponding secions.
|

JTAG Load
"""""""""""""

Uniflash CLI JTAG Load
'''''''''''''''''''''''''
Follow below steps for downloading the flash programer over JTAG using Uniflash CLI

 - Confgure boot mode of the target platform to 'No Boot' or 'JTAG mode'
 - Connect UART serial port of the target platform to host PC
 - Power cycle the target platform
 - Prepare the CCS target configuration file for the platform under test and JTAG emulator being used.
 - Connect the JTAG port of the board to host PC running CCS.
 - Run below commands on the Host PC from Uniflash root folder


For Windows

::

        # cd <Path to Uniflash Root Folder>
        # dslite.bat --mode load --config=<CCS Target Config file (ccxml) with Full Path>
        -f <Flash Programmer Binary with Full Path> -n <Core ID to be Connected to JTAG on the Target Platform>
        Example:
        # dslite.bat --mode load --config=C:\Users\username\ti\CCSTargetConfigurations\idkAM574x.ccxml -f C:\ti\uniflash_5.2.0\processors\FlashWriter\idkAM574x\uart_idkAM574x_flash_programmer.out -n 8



For Linux

::

        # cd <Path to Uniflash Root Folder>
        # sudo ./dslite.sh --mode load --config=<CCS Target Config file (ccxml) with Full Path>
        -f <Flash Programmer Binary with Full Path> -n <Core ID to be Connected to JTAG on the Target Platform>
        Example:
        # sudo ./dslite.sh --mode load --config=/home/ti/CCSTargetConfigurations/idkAM574x.ccxml -f /home/user/ti/uniflash_5.2.0/processors/FlashWriter/idkAM574x/uart_idkAM574x_flash_programmer.out -n 8



Uniflash CLI shows the progress of file transfer on the command console.
Following is the sample output on Windows.

::

        C:\ti\uniflash_5.2.0>dslite.bat --mode load --config=C:\Users\username\ti\CCSTargetConfigurations\idkAM574x.ccxml -f C:\ti\uniflash_5.2.0\processors\FlashWriter\idkAM574x\uart_idkAM574x_flash_programmer.out -n 8
        Executing the following command:
        > "C:\ti\uniflash_5.2.0\deskdb\content\TICloudAgent\win\ccs_base\DebugServer\bin\DSLite" load --config=C:\Users\username\ti\CCSTargetConfigurations\idkAM574x.ccxml -f .\processors\FlashWriter\idkAM574x\uart_idkAM574x_flash_programmer.out -n 8

        For more details and examples, please refer to the UniFlash Quick Start guide.

        DSLite version 9.2.0.1723
        Configuring Debugger (may take a few minutes on first launch)...
                Initializing Register Database...
                Initializing: IcePick_D
                Executing Startup Scripts: IcePick_D
                Initializing: ARM9_ICONT1
                Executing Startup Scripts: ARM9_ICONT1
                Initializing: ARM9_ICONT2
                Executing Startup Scripts: ARM9_ICONT2
                Initializing: CS_DAP_IPU_1_C0
                Executing Startup Scripts: CS_DAP_IPU_1_C0
                Initializing: Cortex_M4_IPU1_C0
                Executing Startup Scripts: Cortex_M4_IPU1_C0
        GEL: Cortex_M4_IPU1_C0: GEL Output: --->>> AM574x Cortex M4 Startup Sequence In Progress... <<<---
        GEL: Cortex_M4_IPU1_C0: GEL Output: --->>> AM574x Cortex M4 Startup Sequence DONE! <<<---
        . . .
        . . .
        . . .
        GEL: CortexA15_0: GEL Output: --->>> IVAHD Initialization is DONE! ... <<<---
        GEL: CortexA15_0: GEL Output: --->>> PRUSS 1 and 2 Initialization is in progress ... <<<---
        GEL: CortexA15_0: GEL Output: --->>> PRUSS 1 and 2 Initialization is in complete ... <<<---
        Loading Program: .\processors\FlashWriter\idkAM574x\uart_idkAM574x_flash_programmer.out
                Preparing ...
                .text: 0 of 72000 at 0x40330074
                .text: 32752 of 72000 at 0x40330074: 15%
                .text: 65504 of 72000 at 0x40330074: 30%
                Finished: 30%
                Setting PC to entry point.: 30%
        Running...
        Success
|

 - Open serial console application (Ex: Minicom, TeraTerm) on host PC and configure it for 115200 baud 8n1.
 - Make a note of the COM port number on which character 'C' is getting printed. This COM port number shall be used
   in all the command inputs to Uniflash host utility.
 - Close all the serial console applications on host PC.
 - If the host PC is running Windows OS, disconnect the serial console cable from the board and reconnet before proceeding to next steps.
 - After successful download of the flash programmer, `Program the flash device <index_board.html#programming-the-flash-device>`__
   or `Erase the flash device <index_board.html#erasing-the-flash-device>`__
   by following the steps described in the corresponding secions.
|

Manual JTAG Load
''''''''''''''''''
Follow below steps for downloading the flash programer over JTAG manually

 - Confgure boot mode of the target platform to 'No Boot' or 'JTAG mode'
 - Connect UART serial port of the target platform to host PC
 - Setup the CCS target configuration file for the platform under test and JTAG emulator being used.

.. note:: Refer the `Platform Specific Information <index_board.html#platform-specific-information>`__ for more details on
          additional setup needed for CCS target configuration.
|

 - Connect the JTAG port of the board to host PC running CCS.
 - Power ON the board
 - Launch the target configuration file from CCS
 - Connect to the target SoC core on which flash programmer is supported.
 - Load and run the flash programmer binary
 - Open a serial console application (Minicom, TeraTerm etc) on host PC and configure it for 115200 baud 8n1.
 - Make a note of the COM port number on which character 'C' is getting printed. This COM port number shall be used
   in all the command inputs to Uniflash host utility.
 - Close all the serial console applications on host PC.
 - If the host PC is running Windows OS, disconnect the serial console cable from the board and reconnet before proceeding to next steps.
 - After successful download of the flash programmer, `Program the flash device <index_board.html#programming-the-flash-device>`__
   or `Erase the flash device <index_board.html#erasing-the-flash-device>`__
   by following the steps described in the corresponding secions.
|


Programming the Flash Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Download the flash programmer using the steps described in section `Downloading Flash Programmer <index_board.html#downloading-flash-programmer>`__
before start programming application binaries to flash device.

Once the Flash Programmer is loaded and executed, use the following commands to program binaries onto the Flash Device.

For Windows
::

        # cd <Path to Uniflash Root Folder>
        # dslite.bat --mode processors -c <COM Port> -f <Path to the binary to be flashed> -d  <Flash Device Type> -o <offset>
        Example:
        # dslite.bat --mode processors -c COM10 -f C:\ti\pdk_am65xx_<ver>\packages\ti\boot\sbl\binary\am65xx_evm\ospi\bin\sbl_ospi_img_mcu1_0_release.tiimage -d 3 -o 0



For Linux
::

        # cd <Path to Uniflash Root Folder>
        # sudo ./dslite.sh --mode processors -c <COM Port> -f <Path to the binary to be flashed> -d  <Flash Device Type> -o <offset>
        Example:
        # sudo ./dslite.sh --mode processors -c /dev/ttyUSB1 -f /home/user/ti/pdk_am65xx_<ver>/packages/ti/boot/sbl/binary/am65xx_evm/ospi/bin/sbl_ospi_img_mcu1_0_release.tiimage -d 3 -o 0



Refer to `Uniflash Command Options <index_board.html#command-options>`__ for more details on command parameters.

Uniflash CLI shows the progress of file transfer on the command console.

.. note::
   Multiple images like bootloader, system firmware and application etc should be flashed to get the application
   booting from the boot device. Refer to the `FAQ section <index_board.html#uniflash-faq>`__ for additional references.

Following is the sample output for flashing RTOS application images on AM65xx platform.

::

        C:\ti\uniflash_5.2.0>dslite.bat --mode processors -c COM10 -f C:\ti\pdk_am65xx_1_0_6\packages\ti\boot\sbl\binary\am65xx_evm\ospi\bin\sbl_ospi_img_mcu1_0_release.tiimage -d 3 -o 0
        Executing the following command:
        > C:\ti\uniflash_5.2.0\processors\ProcessorSDKSerialFlash.exe -c COM10 -f C:\ti\pdk_am65xx_1_0_6\packages\ti\boot\sbl\binary\am65xx_evm\ospi\bin\sbl_ospi_img_mcu1_0_release.tiimage -d 3 -o 0

        For more details and examples, please refer to the UniFlash Quick Start guide.


        ----------------------------------------------------------------------------
        ProcessorSDKSerialFlash CLI Tool
        Copyright (C) 2017-2019 Texas Instruments Incorporated - http://www.ti.com/
        Version 1.2.0.0
        ----------------------------------------------------------------------------
        Transferring the Image to Flash Programmer..

        Transferring Header Information..
        Header Transfer Complete!

        Flashing Image of size 155614 bytes
        Flash Programming Success!


        C:\ti\uniflash_5.2.0\dslite --mode processors -c COM10 -f C:\ti\pdk_am65xx_1_0_6\packages\ti\drv\sciclient\soc\V0\sysfw.bin -d 3 -o 40000
        Executing the following command:
        > C:\ti\uniflash_5.2.0\processors\ProcessorSDKSerialFlash.exe -c COM10 -f C:\ti\pdk_am65xx_1_0_6\packages\ti\drv\sciclient\soc\V0\sysfw.bin -d 3 -o 40000

        For more details and examples, please refer to the UniFlash Quick Start guide.


        ----------------------------------------------------------------------------
        ProcessorSDKSerialFlash CLI Tool
        Copyright (C) 2017-2019 Texas Instruments Incorporated - http://www.ti.com/
        Version 1.2.0.0
        ----------------------------------------------------------------------------
        Transferring the Image to Flash Programmer..

        Transferring Header Information..
        Header Transfer Complete!

        Flashing Image of size 263083 bytes
        Flash Programming Success!


        C:\ti\uniflash_5.2.0\dslite --mode processors -c COM10 -f C:\ti\pdk_am65xx_1_0_6\packages\ti\board\bin\am65xx_evm\sd\armv8\led_TEST -d 3 -o A0000
        > C:\ti\uniflash_5.2.0\processors\ProcessorSDKSerialFlash.exe -c COM10 -f C:\ti\pdk_am65xx_1_0_6\packages\ti\board\bin\am65xx_evm\sd\armv8\led_TEST -d 3 -o A0000

        For more details and examples, please refer to the UniFlash Quick Start guide.


        ----------------------------------------------------------------------------
        ProcessorSDKSerialFlash CLI Tool
        Copyright (C) 2017-2019 Texas Instruments Incorporated - http://www.ti.com/
        Version 1.2.0.0
        ----------------------------------------------------------------------------
        Transferring the Image to Flash Programmer..

        Transferring Header Information..
        Header Transfer Complete!

        Flashing Image of size 72360 bytes
        Flash Programming Success!



Erasing the Flash Device
^^^^^^^^^^^^^^^^^^^^^^^^^
Download the flash programmer using the steps described in section `Downloading Flash Programmer <index_board.html#downloading-flash-programmer>`__
before start executing erase command.

Once the Flash programmer is loaded and executed, use the following commands to erase the Flash Device on the target platform

For Windows

::

        # cd <Path to Uniflash Root Folder>
        # dslite.bat --mode processors -c <COM Port> -e <Erase Length in Bytes> -d <Flash Device Type> -o <Erase Offset>
        Example:
        # dslite.bat --mode processors -c COM10 -e 10000 -d 3 -o 20000


For Linux

::

        # cd <Path to Uniflash Root Folder>
        # sudo ./dslite.sh --mode processors -c <COM Port> -e <Erase Length in Bytes> -d <Device Type> -o <Erase Offset>
        Example:
        # sudo ./dslite.sh  --mode processors -c /dev/ttyUSB1 -e 10000 -d 3 -o 20000


The application will output the status to the console on the Host PC.
Following is the sample output on Windows.

::

        C:\ti\uniflash_5.2.0>dslite.bat --mode processors -c COM10 -e 10000 -d 3 -o 0
        Executing the following command:
        > C:\ti\uniflash_5.2.0\processors\ProcessorSDKSerialFlash.exe -c COM10 -e 10000 -d 3 -o 0

        For more details and examples, please refer to the UniFlash Quick Start guide.


        ----------------------------------------------------------------------------
        ProcessorSDKSerialFlash CLI Tool
        Copyright (C) 2017-2019 Texas Instruments Incorporated - http://www.ti.com/
        Version 1.2.0.0
        ----------------------------------------------------------------------------
        Erasing Flash....

        Transferring Header information..
        Header Transfer Complete!!
        Flash Erase Success!


Platform Specific Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AM335x
""""""""
 - Make sure the Profile Selection switch on AM335x GP EVM is set to Profile#2 while programming SPI flash

AM65xx/J721E
"""""""""""""

- Flash programmer requires system firmware while downloading the flash
  programmer through UART on AM65xx and J721E platforms. Uniflash host CLI loads
  the system firmware automatically while loading the flash programmer on these
  platforms. Flash programmer and system firmware binary (sysfw.bin) should be
  kept in the same folder for succesful downloading of flash programmer and
  system firmware.

- System firmware should be loaded through CCS script while loading the flash
  programmer through JTAG. Refer the EVM CCS Setup Documentation section below
  for details of setting up the CCS target configuration with system firmware
  download.

   - `AM65xx
     <index_how_to_guides.html#advanced-am65x-debug-setup-with-dmsc-firmware-load>`__

   - `J721E
     <http://software-dl.ti.com/jacinto7/esd/processor-sdk-rtos-jacinto7/latest/exports/docs/psdk_rtos_auto/docs/user_guide/ccs_setup_j721e.html>`__

J721E
""""""

- Set the dip switch SW3.1 on CP board to OFF while running the flash programmer
  for OSPI flashing on J721E EVM

Uniflash FAQ
^^^^^^^^^^^^^

- How do I confirm my HW setup is proper for image download over UART? Board
  should be configured for UART boot mode for downloading the images over UART.
  RoM bootloader sends a character 'C' at regular intervals on serial port in
  UART boot mode. Connect a serial console application on host PC to the UART
  port used for booting and veirfy the character 'C' is getting displayed, which
  confirms the HW setup needed for image download over UART is proper.

- How do I verify which COM number to be used for Uniflash image download? There
  may be multiple UART ports supported on the board but Uniflash image download
  happens on one specific UART port which is meant for UART boot. RoM bootloader
  and Uniflash flash programmer sends a character 'C' at regular intervals on
  the UART port used for image download. COM port number to be used for image
  download can be identified by checking for the character 'C' displayed on host
  PC.

- I am running Uniflash on Windows host and Uniflash CLI is not able to open COM
  port. What could be the reason? Some of the serial console application like
  TeraTerm on Windows changes the COM port settings which causes the COM port
  open failure from Uniflash. Disconnect the UART cable and reconnet before
  running the Uniflash commands everytime a serial console application is used
  to access the COM port on Windows.

- Should the flash device be erased using Uniflash erase command before flashing
  the images? No, Uniflash Erase command is provided to explicity erase the
  images on the flash device. Uniflash flash programmer erases the flash by
  default before flashing the images.

- What all the images that need to be flashed to get my application boot? It
  depends on the SoC flamily and OS being used by the application. In general, a
  secondary bootloader, any configuration files needed for system configuration
  and an application image are the minimum images that need to be flashed for
  booting to happen. Refer below documentation for more details

   * `RTOS <index_Foundational_Components.html#boot>`__

   * `Linux
     <http://software-dl.ti.com/processor-sdk-linux/esd/docs/latest/linux/Foundational_Components_U-Boot.html#u-boot>`__

Rebuilding Board-utils
^^^^^^^^^^^^^^^^^^^^^^
- Use the following commands to rebuild Uniflash and Apploader supported as part of board utils

- For Windows

::

        # cd <pdk_install_path>/packages
        # pdksetupenv.bat
        # cd ti\board\utils
        # gmake clean
        # gmake

- For Linux

::

        # cd <pdk_install_path>/packages
        # ./pdksetupenv.sh
        # cd ti/board/utils
        # make clean
        # make

- Uniflash binaries will be created under the folder <pdk_install_path>/packages/ti/board/utils/uniflash/bin/<board_name>/
- Apploader binaries will be created under the folder <pdk_install_path>/packages/ti/board/utils/uartAppLoader/bin/<board_name>/
