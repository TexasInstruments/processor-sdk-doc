.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_BOOT_AM335x/AM437x

Overview
^^^^^^^^^

Bootloader supports power-on-reset bootstraps for the board. It
initializes board, loads application from the memory device to DDR and
transfers control to application. Section provides additional details
including flashing and booting instructions across different media.

Source Reference
^^^^^^^^^^^^^^^^^^

::

    < BASE_DIR = PDK_INSTALL_DIR\packages\ti\starterware>


Bootloader build files for AM335x/AM437x
"""""""""""""""""""""""""""""""""""""""""

**Source files:**

-  **BASE_DIR/bootloader/src**: Common source files for bootloader
   functionality
-  **BASE_DIR/bootloader/src/<device>**: Files specific to device to
   initialize platform features like PLL, pinmux and DDR

**Build Files:**

-  **BASE_DIR/build/makerules/rules_a8.mk**: Common Compiler flags used
   for A8 cores. Applies to AMIC110 and AM335x
-  **BASE_DIR/build/makerules/rules_a9.mk**: Common Compiler flags used
   for A9 cores. Applies to AM437x devices
-  **BASE_DIR/build/makerules/platform.mk**: Global settings for all
   components for a particular platform.
-  **BASE_DIR/build/makerules/components.mk**: Specific settings for
   components in starterware
-  **BASE_DIR/build/makerules/build_cfg.mk**: Flags to enable features
   in the build
-  **BASE_DIR/bootloader/Makefile**: Makefile for bootloader that
   provides list of source files and library to create bootloader
   binary.

**Boot and flashing tools:**

-  **BASE_DIR/tools Contains tools to create boot images and flashing
   tools to program the boot binary on the boot media.**

|

Bootloader execution sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Processor SDK RTOS boot loader uses a two stage boot process. The
different stages of the application boot sequence using Processor SDK
RTOS bootloader are shown below:

Boot Sequence
"""""""""""""""

#. Power on Reset
#. ROM Bootloader (RBL)

   -  Platform configuration and initialization.

      -  DPLL and clock settings for MPU, I2C, MMCSD, USB, SPI, QSPI,
         Ethernet etc.

   -  Checks Sysboot pins and choose booting device

      -  If no valid bootloader found on booting device, RBL checks for
         next booting device. The sequence depends on RBL execution flow
         and Sysboot pins.

   -  RBL gets image size and load address by checking TI Image Header
      appended on bootloader binary(.bin). Check `binary
      formats <index_Foundational_Components.html#tools-and-binary-formats>`__.
   -  Loads the binary to internal OCMC memory at the Load address
      fetched from TI Image Header
   -  Passes control to Secondary Bootloader(SBL)

#. Secondary Bootloader(SBL)

   -  Configure PLL and Initialize DDR
   -  Configure PRCM and PinMux  for Boot Peripherals
   -  Copies application image to DDR
   -  Passes execution control to Application

#. Application execution

Tools and Binary formats
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------+-----------------------+-----------------------+
| Binary format         | Requirement           | Details               |
+-----------------------+-----------------------+-----------------------+
| .bin                  | QSPI bootloader,      | QSPI bootloader       |
|                       |                       | binary should in .bin |
|                       | UART bootloader and   | format and            |
|                       | app                   | Application binary    |
|                       |                       | should be in \_ti.bin |
|                       |                       | format.               |
|                       |                       |                       |
|                       |                       | UART bootloader and   |
|                       |                       | applications are      |
|                       |                       | loaded in .bin format |
|                       |                       | through XMODEM in     |
|                       |                       | terminal.             |
+-----------------------+-----------------------+-----------------------+
| \_ti.bin              | MMCSD bootloader      | .bin binaries are     |
|                       | and app,              | converted to          |
|                       |                       | \_ti.bin format by    |
|                       | NAND bootloader and   | adding Image          |
|                       | app,                  | size(4bytes) and      |
|                       |                       | Image load            |
|                       | MCSPI boot loader and | address(4bytes) as    |
|                       | app,                  | image header.         |
|                       |                       | Refer to Image        |
|                       | QSPI app.             | format section in     |
|                       |                       | Initialization        |
|                       |                       | chapter of `AM437x    |
|                       |                       | TRM`_                 |
|                       |                       |                       |
|                       |                       | MMCSD, NAND and MCSPI |
|                       |                       | boot loaders and      |
|                       |                       | application binaries  |
|                       |                       | should be appended    |
|                       |                       | with ti image header. |
|                       |                       |                       |
+-----------------------+-----------------------+-----------------------+

.. _AM437x TRM: http://www.ti.com/lit/ug/spruhl7h/spruhl7h.pdf

|

**TI Boot image**

+------------+----------------------------+
| Offset     | Binary value               |
+============+============================+
| 0x00000000 | **Size**                   |
+------------+----------------------------+
| 0x00000004 | **Entry Point (Location)** |
+------------+----------------------------+
| 0x00000008 | **Binary (.bin)**          |
+------------+----------------------------+

.. note::
   - For bootloader, the entry point is usually 0x402f0000
   - For app, the entry point is usually 0x80000000.


Binary format conversion procedure
"""""""""""""""""""""""""""""""""""

The GCC tool chain, referred as GCC_TOOLCHAIN_PATH below, is installed during
the Processor-SDK RTOS installation. For example, Processor-SDK RTOS 6.3 has
gcc-arm-none-eabi-7-2018-q2-update.

Binary format conversion in Linux
''''''''''''''''''''''''''''''''''
1) To convert from .out -> .bin

::

    <GCC_TOOLCHAIN_PATH>/bin/arm-none-eabi-objcopy -O binary <application>.out <application>.bin

2) Build tiimage.out. Go to starterware/tools/ti_image/

::

    gcc tiimage.c –o tiimage.out

3) To convert from .bin -> \_ti.bin

::

    tiimage.out <Image Load Address> NONE <application>.bin <application>_ti.bin

Binary format conversion in Windows
''''''''''''''''''''''''''''''''''''
1) To convert from .out -> .bin

::

    <GCC_TOOLCHAIN_PATH>/bin/arm-none-eabi-objcopy -O binary <application>.out <application>.bin

2) To convert from .bin -> \_ti.bin. tiimage.exe is provided as prebuilt
binary in starterware/tools/ti_image.

::

    tiimage.exe <Image Load Address> NONE <application>.bin <application>_ti.bin

|

Boot Modes supported
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Following are the Boot Modes supported through AM335x/AM437x bootloader
for the various EVMs.

+-----------+-----------+-----------+-----------+-----------+-----------+
|           | **MMCSD** | **NAND**  | **McSPI** | **QSPI**  | **UART**  |
+-----------+-----------+-----------+-----------+-----------+-----------+
| **AM335x  |    YES    |    YES    |    YES    |    NO     |    YES    |
| GPEVM**   |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| **AM335x  |    YES    |    NO     |    YES    |    NO     |    NO     |
| ICEv2**   |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| **AM335x  |    YES    |    NO     |    NO     |    NO     |    YES    |
| StarterKi |           |           |           |           |           |
| t**       |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| **AM335x  |    YES    |    NO     |    NO     |    NO     |    YES    |
| BeagleBon |           |           |           |           |           |
| eBlack**  |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| **AMIC110 |    NO     |    NO     |    YES    |    NO     |    YES    |
| ICE**     |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| **AM437x  |    YES    |    NO     |    NO     |    NO     |    YES    |
| GPEVM**   |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| **AM437x  |    YES    |    NO     |    NO     |    YES    |    NO     |
| IDK**     |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| **AM437x  |    YES    |    NO     |    NO     |    NO     |    NO     |
| StarterKi |           |           |           |           |           |
| t**       |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+

|

Building the Bootloader
^^^^^^^^^^^^^^^^^^^^^^^

**Pre-requisite:** Setup SDK build environment as described in article
 `Setup_Environment <index_overview.html#setup-environment>`__

Change working directory to the packages/ti/starterware directory
    cd <procsdk_install_dir>/pdk_<soc>_<version>/packages/ti/starterware

NOTE: For the starterware build targets below, the parallel make option (-j) is not supported. Please ensure that the below are built without parallel make option.

Normal Operation of Bootloader:
"""""""""""""""""""""""""""""""""""

Bootloading an application from flash into DDR memory as in case of TI
evaluation platforms is described as normal operation mode for the
bootloader. This is the default behavior of the bootloader and can be
built using the following command in starterware.

::

    gmake bootloader BUILDCFG=boot BOOTMODE=<BOOT_MODE> PLATFORM=<EVM> PROFILE=<BUILD_PROFILE> -s KW_BUILD=no

-  BOOT_MODE: mcspi, nand, qspi, mmcsd, uart (Check supported boot modes
   for your evaluation platform)
-  EVM: am335x-evm (for all AM335x/AMIC110 based boards), am43xx-evm (for all AM43xx based boards)
-  BUILD_PROFILE: debug, release

Additional Build Options
""""""""""""""""""""""""

The build options listed below are currently supported only for AMIC110/AM335x ICE Users.

-  **DDR less Application boot setup**

::

    gmake bootloader BUILDCFG=boot BOOTMODE=mcspi PLATFORM=amic110-ddrless PROFILE=debug -s KW_BUILD=no USE_DDR=no
    gmake bootloader BUILDCFG=boot BOOTMODE=mcspi PLATFORM=amic110-ddrless PROFILE=release -s KW_BUILD=no USE_DDR=no

This option builds an ultra light weight (<10 KB) bootloader for cost
optimized application that doesn't use external DDR memory.

-  **PRU/ICSS Enable in SBL**

::

    gmake bootloader BUILDCFG=boot BOOTMODE=mcspi PLATFORM=am335x-evm PROFILE=debug -s KW_BUILD=no ENABLE_PRU=yes
    gmake bootloader BUILDCFG=boot BOOTMODE=mcspi PLATFORM=am335x-evm PROFILE=release -s KW_BUILD=no ENABLE_PRU=yes

This feature is required in application that need to quick wake up of
ICSS/PRU cores. The PRU cores can be woken up and loaded from the SBL by
combining the ENABLE_PRU and BIN_LOAD arguments.

-  **Load additional binaries from flash**

::

    gmake bootloader BUILDCFG=boot BOOTMODE=mcspi PLATFORM=am335x-evm PROFILE=debug -s KW_BUILD=no BIN_LOAD=yes
    gmake bootloader BUILDCFG=boot BOOTMODE=mcspi PLATFORM=am335x-evm PROFILE=release -s KW_BUILD=no BIN_LOAD=yes

The location of binaries in offset is configured using
sbl_flash_offset_cfg.h in the bootloader source. Users are required to
use TIIMAGE tool to append an header to the binary so that the
bootloader knows the location and size of the binary to be loaded.

Special Build Option for Industrial DDRless Booting
"""""""""""""""""""""""""""""""""""""""""""""""""""

The AMIC110 DDRLESS platform provides a superset flag to enable all the
above features and build the bootloader. The superset build is invoked
using **BUILD_ICSS_DDRLESS_BOOT=yes** as shown below:

::

    gmake bootloader BUILDCFG=boot BOOTMODE=mcspi PLATFORM=amic110-ddrless PROFILE=debug -s KW_BUILD=no BUILD_ICSS_DDRLESS_BOOT=yes
    gmake bootloader BUILDCFG=boot BOOTMODE=mcspi PLATFORM=amic110-ddrless PROFILE=release -s KW_BUILD=no BUILD_ICSS_DDRLESS_BOOT=yes


Prebuilt binaries inside the Processor SDK RTOS for AMIC110-DDRLESS will
be configured using this option to allow for testing of cost optimized
industrial use case.

|

Boot Mode settings
^^^^^^^^^^^^^^^^^^

Boot mode settings for supported AM335x and AM437x boards can be found in
the applicable `EVM Hardware User's Guide <index_release_specific.html#supported-platforms-and-versions>`__.

Boot Modes
^^^^^^^^^^

Booting Via SD Card
"""""""""""""""""""""

Booting from SD Card involves two steps.

#. Preparing SD card.
#. Booting target.

Preparing SD card
'''''''''''''''''''

#. To boot target the SD card should be bootable. Follow the steps at
   `Creating bootable SD card in windows <index_overview.html#windows-sd-card-creation-guide>`__
   or `Creating bootable SD card in Linux <index_overview.html#linux-sd-card-creation-guide>`__.
#. Delete the "*MLO*" and "*app*" in the bootable SD card which are
   created in the process of making the SD bootable.
#. Bootloader images with ti header (<mmcsd_bootloader>_ti.bin)should be
   renamed to "*MLO*". Bootloader images are located at
   *<PDK_INSTALL_DIR/packages/ti/starterware/binary/bootloader/bin/<TargetType*>
#. Similarly the converted application binary image has to be renamed to
   "*app*" from "*<app_name>_ti.bin*"
#. Copy both the boot loader image "*MLO*" and the application image
   "*app*" to the SD card.
#. The SD card is ready for use on target.

Booting target
'''''''''''''''

#. Insert SD card to the base board SD slot. Connect a UART cable to a
   host running a serial terminal application (teraterm/hyperterminal)
   with 115200 baud, 8bit, No parity and 1 STOP bit configuration.
#. Configure the board for SD Boot mode

   #. SD instance 0 (on base board) is available in all profiles.
   #. SD instance 0 boot mode needs to appropriately set. For SD boot to
      be selected first, SD boot should appear first in the boot device
      list in the boot mode. If any other boot mode is selected, even if
      a SD boot card is inserted, and does not appear first in the list,
      the first available sane boot image (like NAND or SPI etc) is
      booted and SD is not selected. Only if no sane boot image is found
      in the first devices, SD boot image will be selected.

#. Once SD boot image is chosen, the *MLO* is first detected and copied
   and executed from the OCMC0 RAM. The *MLO* then copies the
   application image (*app*) from the card to the SDRAM and passes the
   control to the application. If the process is successful, messages
   identifying board and SoC will appear on the serial console.

After this the application will take control and execute.

**NOTE:** If board has boot mode selection pins, choose proper boot mode
selection pins from hardware reference manuals.

| If the boards have no boot mode selection pins and a valid boot image
  is present on McSPI flash, booting will happen from McSPI flash. Erase
  McSPI flash in such cases to boot from SD card.
  Refer to `Booting Via McSPI <index_Foundational_Components.html#booting-via-mcspi>`__
  for how to rease McSPI flash.
  The boot sequence depends on ROM bootloader.


Booting Via QSPI
""""""""""""""""""

Booting from QSPI flash involves two steps-

#. Preparing Flash Device
#. Booting target.

Preparing Flash Device
'''''''''''''''''''''''

Procedure relies on contents being copied to SD card. Additional
details below:

#. Copy bootloader image(bootloader_boot_qspi_a9host_debug.bin rename)
   and app image("<app_name>_ti.bin") into the SD card.
   The file names have to be renamed in such a way that the length of
   name is less than 9 characters. Any file name less than 9 characters
   can be used.
   Rename the bootloader file to 'boot' and application image to 'app'
   with no extensions.
#. Copy the 'config' file into the SD card which will contain the names
   of the image to be flashed and the offset.
   A sample config file can be found at
   *<PDK_INSTALL_DIR/packages/ti/starterware/tools/qspi/config/>
   directory*. Do not change name of the **config** file.
   **NOTE:** "config" file can be used without any modifications if
   bootloader and application images are renamed to "boot" and "app".
   **NOTE:** Do not rename bootloader to be copied to SD card as
   "*MLO*", as MMCSD bootloader expects "*MLO*" and "*app*" to boot.
#. Now SD card contains 1)boot 2)app 3)config files.
   config file contains the address of boot image as **0x0** and app
   image as **0x80000**.
   Insert it into the SD card slot.
#. Connect the board with CCS and load the prebuilt qspi flash writer
   application from
   *<PDK_INSTALL_DIR/packages/ti/starterware/binary/qspi_app_flash_writer/bin/m43xx-evm>*
#. Run the QSPI flash writer application. Following logs expected on
   console.

::

    StarterWare QSPI Flash Writer!!
    BOARDInit status [0x0]
    SoC                   : [AM43XX]
    Core                  : [A9]
    Board Detected        : [IDKEVM]
    Base Board Revision   : [UNKNOWN]
    Daughter Card Revision: [UNKNOWN]
    Copying boot to QSPI Flash
    Copying app to QSPI Flash
    Changing read to quad mode
    Read mode has been changed to Quad mode
    SUCCESS!!!
    Flashing completed

Booting the target.
''''''''''''''''''''

#. Connect UART cable to a host running serial terminal application
   (teraterm/hyperterminal) with 115200 baud, 8bit, No parity and 1 STOP
   bit configuration.
#. After flashing successfully remove SD card and reboot to see
   following logs

::

    StarterWare Boot Loader
    BOARDInit status [0x0]
    SoC                   : [AM43XX]
    Core                  : [A9]
    Board Detected        : [IDKEVM]
    Base Board Revision   : [UNKNOWN]
    Daughter Card Revision: [UNKNOWN]
    Copying Header of the application image
    Copying image from flash to DDR
    Jumping to StarterWare Application...

::

     NOTE: Boot logs will appear approximately after 25 seconds on reset.

::

     NOTE:If there is no boot mode selection present on board, boot image will be loaded depending on ROM boot sequence
    Example: If QSPI flash and MMCSD has valid bootloaders, on reset MMCSD boot image will be loaded following ROM Boot sequence.

Booting Via UART
""""""""""""""""""

ROM and Bootloader supports XMODEM protocol with images being binary
not requiring any additional headers. Following are steps for boot:

#. Configure board for UART boot mode :
   UART boot need to be first in the boot device list. Note: In case if
   any other boot mode is selected, the first available boot image
   (eg:NAND or MMCSD etc) will override. In case of no valid images,
   UART boot will be selected.

   -  Select View->Memory Browser through CCS.
   -  Select address 0x44e10040.
   -  Write 0x19 to last 2 bytes of this memory address.(UART boot)
   -  Soft reset the board. This is a volatile bit which gets reset
      after power on.

#. ROM code will print "CC.." on UART console expecting Bootloader via
   XMODEM. File can be sent via xmodem through tera-term File-> Transfer
   -> XMODEM -> Send.
#. On transmitting bootloader
   image, bootloader_boot_uart_a9host_debug.bin via XMODEM, following
   message will be expected on serial console.

::

    CCCCCCCCCCCCCCCCCCCCCCCCCCCC
    StarterWare Boot Loader
    BOARDInit status [0x0]
     SoC                   : [AM43XX]
     Core                  : [A9]
     Board Detected        : [IDKEVM]
     Base Board Revision   : [UNKNOWN]
     Daughter Card Revision: [UNKNOWN]
    GPIO Instance number: 0
    Pin number: 22
    Please transfer file:
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC

#. As a next step application binary (without header) can be sent via XMODEM
   which will lead to application start executing.

Booting Via McSPI
"""""""""""""""""""

Booting from McSPI involves two steps.

#. Preparing Flash Device
#. Booting the target.

.. rubric:: Preparing Flash Device
   :name: preparing-flash-device-1

-  Set the appropriate bootmode if applicable for EVM. Refer to corresponding
   hardware user's guide for bootmode settings.
   **Note**: Most of the boards may not have switch settings.
-  Add a required target configuration in CCS depending on emulator and
   board connected.
-  Connect target to required core. Ex: A8.
-  Load the flash writer from
   *<PDK_INSTALL_DIR/packages/ti/starterware/tools/flash_writer/spi_flash_writer_AM335X.out*
   onto the EVM.
-  Run the application and observe the logs on CCS console.

::

    Starting SPIWriter.
    Choose Operation:
    Enter 1 ----> To FLASH an Image
    Enter 2 ----> To ERASE Flash
    Enter 3 ----> To EXIT

-  When Flash option is chosen program prompts to enter file name.

::

    Enter the File Name

-  Provide the complete path of file
   *bootloader_boot_mcspi_a8host_release_ti.bin* at directory
   "binary/bootloader/bin/<PLATFORM>/<gcc/ccs>/" and hit Enter.

::

    Enter the Offset in bytes (in HEX)

-  Provide **0x00000** to flash bootloader.

-  Wait for few minutes as flashing is a slower process.

::

    Erasing flash at byte offset: xx, byte length: xxxx
    SF: Successfully erased xxxx bytes @ xxxx
    Writing flash at page offset: x, number of pages: xxxx
    Flashing is in progress...
    Verifying... Success.

-  Repeat the steps to load and run the flash writer, then choose the application
   binary image <app_name>_a8host_ti.bin and enter **0x20000** as the offset.
   Wait until the flashing completes.

-  Once SPI flash writing completes disconnect target.

.. rubric:: Booting the target
   :name: booting-the-target

#. Connect a serial cable to a host running a serial terminal
   application (teraterm/hyperterminal) with 115200 baud, 8bit, No
   parity and 1 STOP bit configuration.
#. Configure the board for SPI boot mode.
#. On reset, ROM bootloader copies the bootloader from flash to internal
   memory. The bootloader then copies the application image from flash
   to DDR and passes the control to the application.

|

Booting Via NAND
""""""""""""""""""

Booting from NAND involves two steps.

#. Preparing Flash Device
#. Booting the target.

.. rubric:: Preparing Flash Device
   :name: preparing-flash-device-2

-  Configure BOOT pins for NAND according to the hardware user's guide.
-  Connect target with CCS.
-  Load the
   *<PDK_INSTALL_DIR/packages/ti/starterware/tools/flash_writer/nand_flash_writer_AM335X.out>*
   to target and Run. Flash writer will output messages to CCS console.
   When it prompts for inputs, proper inputs shall be given via CCS
   console.
-  When prompted for binary file name, update file with proper path.
-  Select option for flashing.

::

    Choose your operation
    Enter 1 ---> To Flash an Image
    Enter 2 ---> To ERASE the whole NAND
    Enter 3 ---> To EXIT

-  If Option 1 is selected, enter image path to flash when prompted as
   shown below.

   ::

       Enter image file path

   Provide the complete path (e.g.
   <PDK_INSTALL_DIR/packages/ti/starterware/binary/bootloader/bin/<am335x/am437x-evm>/<compiler>/bootloader_boot_nand_a8host_<debug/release>_ti.bin)

-  Enter offset when prompted as shown below.

::

    Enter offset (in hex):

|     This offset is start location from where the image should be
  flashed.
| NOTE:

#. Use hex format
#. If bootloader is to be flashed, provide **0x00000**. For application
   binary, provide **0x80000**.

-  Select ECC for flashing.

   ::

       Choose the ECC scheme from given options
       Enter 1 ---> BCH 8 bit
       Enter 2 ---> HAM
       Enter 3 ---> T0 EXIT
       Please enter ECC scheme type:

   Always select BCH8 for bootloader and application as ROM code and
   bootloader uses the BCH8 ECC scheme.

-  Ensure that flash info displayed by tool matches NAND flash in EVM.
-  After this tool should first erase the required region in flash and
   then start flashing new image.
-  If flashing procedure is complete following message should be
   displayed.

::

    Application is successfully flashed
    NAND flashing successful!

-  Once NAND flash writing completes, disconnect from CCS.

.. rubric:: Booting the target
   :name: booting-the-target-1

-  Connect a UART cable to a host running a serial terminal application
   (teraterm/hyperterminal) with 115200 baud, 8bit, No parity and 1 STOP
   bit configuration.
-  Configure the board for NAND boot mode. Refer to corresponding
   hardware user's guide for bootmode settings.
-  On reset, ROM detects bootloader from NAND and copies it to internal
   memory. Bootloader then copies application image from the NAND to DDR
   and passes control to application. If the process is successful,
   following messages appear in serial console.

::

       StarterWare Boot Loader
    BOARDInit status [0x0]
    SoC                   : [AM335X]
    Core                  : [A8]
    Board Detected        : [GPEVM]
    Base Board Revision   : [1.5]
    Daughter Card Revision: [UNKNOWN]
    NAND flash is connected to GPMC on this board
    Jumping to StarterWare Application...

After this application should take control and execute.

Test Application
^^^^^^^^^^^^^^^^^^

The section explains steps for building and booting a sample pdk
application for am335x or am437x using MMCSD bootloader.

Test Application Image Creation
""""""""""""""""""""""""""""""""""

Follow below steps to generate the bootable application image.

#. Generate .out files using steps for `Rebuilding
   PDK <index_how_to_guides.html#rebuild-drivers-from-pdk-directory>`__. Locate .out file in directory
   *<PDK_INSTALL_PATH/MyExampleProjects/<ExampleProjectDirectory>/Debug>*
#. Convert files to support MMCSD boot using steps as per `Binary format
   conversion procedure <index_Foundational_Components.html#binary-format-conversion-procedure>`__.
#. Rename generated <Application>_ti.bin to "app".

Loading Test application
"""""""""""""""""""""""""

Follow procedure to use "app" file as per section `Booting Via SD
Card <index_Foundational_Components.html#booting-via-sd-card>`__.

Usage Notes
^^^^^^^^^^^^^

-  **Bootloader Memory map**

The bootloader code runs from internal OCMC memory and occupies certain
amount of OCMC memory that is not available for application to use
during booting.

Refer to the map file for the boot loader to check for latest
information on the memory utilization in the boot loader.

Location of linker command file:

::

    BASE_DIR\binary\bootloader\bin\<platform>\gcc

After SBL execution is complete, this region can be used as per
application requirement.

-  **Configuring entry point for SBL**

The three files that help setup the entry point in the bootloader build
are "PDK_INSTALL_PATH/packages/ti/starterware/soc/armv7a/gcc/sbl_init.S"
and the linker command file
"PDK_INSTALL_PATH/packages/ti/starterware/examples/gcc/<device>_boot.lds".
The global symbol Entry is used to provide the entry point to the
bootloader. The Base address of the memory section OCMCRAM (starts at 1K
offset in OCMC RAM as defined in TRM) is then used by the tiimage or
GPHEader tool to provide RBL the guidance to find the entry point to
pass control. After MLO is created check the TI image format file(
\_ti.bin) to confirm that the entry point matches the location of Entry
symbol in the .map file.

.. note::
   The object file created by sbl_init.S should always be the first object
   file in the link order for the symbol Entry to be placed at the BASE
   address of the memory section SBL_MEM

-  **Boot image creation tools generates a large boot image if load
   sections are fragmented**

Please note that when using objcopy the compiler generates a contiguous
binary that gets loaded by the bootloader at the location specified in
the header appended by TIIMAGE boot utility. IF you have some code
sections in OCMC or SRAM and some section in DDR the compiler will
generates a binary that spans across full memory range which would be in
order of MB or even GB size so it is recommended that you create compact
binaries that can be loaded into memory or implement a ELF parser to
bootloader memory sections that may be fragmented in the address space.
you can also load separate binaries for OCMC sections and DDR memory and
load the sections separately

-  **Removing Heap section from application binary to speed up boot
   times**

A common issue reported with the ARM GCC compiler is that it appends
Heap section associated with the binary to the binary image used to
boot. The Heap section is usually filled with zeros so can cause
significant delay in boot times. Essentially the bootloader will be
writing a bunch of zeros in memory so is inefficient. Following work
around has been used to circumvent the issue

**Option 1:** Eliminate the heap by using the compiler option
"--remove-section" as described in the E2E post below:

**Refer:** `E2E post to configure Heap in ARM application binary by
adding
"--remove-section" <https://e2e.ti.com/support/arm/sitara_arm/f/791/p/604616/2225826>`__

**Example BIOS configuration:**

::

    var heap1 = HeapMem.create();
    heap1.size = 256 * 1024 * 1024;
    heap1.sectionName = ".stack";
    Memory.defaultHeapInstance = heap1;

**Compiler Setting :** --remove-section=.stack

**Option 2** Configure Segment type to be "NO LOAD" in .cfg and use
excludeSections

SYSBIOS Memory map configurations allows user to specify the section
name, length and type. by configuring the section type to "NOLOAD" and
using excludeSection option the heap memory can be eliminated from the
final binary.

**Example BIOS configuration:**

::

    Program.sectMap[".biosheap"] = new Program.SectionSpec();
    Program.sectMap[".biosheap"].runSegment = "DDR2"
    Program.sectMap[".biosheap"].type = "NOLOAD";

::

    Program.sectionsExclude = ".biosheap"

Alternate approach using linker command file:

::

     .ddr3Heap (NOLOAD):
       {
           *(.ddr3Heap)
       } > HOST_DDR3

.. note::
   The approach described above helps improve boot times but Users are
   recommended to initialize the HEAP sections to zeros post boot during
   initialization to avoid any undesired behavior during normal operation
   of the app

Debugging application boot
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Steps to debug application boot using Processor SDK RTOS bootloader are
discussed in the article **`Common steps to debug application
boot <index_Foundational_Components.html#common-steps-to-debug-application-boot>`__**

