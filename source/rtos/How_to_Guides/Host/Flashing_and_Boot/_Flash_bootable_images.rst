.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Flashing_Bootable_Images

Overview
^^^^^^^^

The Processor SDK RTOS for C6657, C6678, K2H, K2E, and K2L EVMs includes
a script in the directory

::

     [SDK Install Path]/processor_sdk_rtos_<platform>_<version>/bin

named **program_evm.js**. The purpose of this script is to automatically
flash bootable images onto your EVM.

The following sections will describe how to use this script and the
default flashable binaries in the Processor SDK RTOS.

Requirements
^^^^^^^^^^^^

-  A Windows or Linux PC
-  Processor SDK RTOS installed on your PC. The version to install must
   match the SOC you plan to use
-  Code Composer Studio installed on your PC
-  An USB connection to your EVM emulator

.. note::
   Your board should be set to NO-BOOT mode. Please refer to the boot mode
   dip switch settings for different boot modes on your EVM Hardware User
   Guide. See :ref:`this page <RTOS-SDK-Supported-Platforms>` for
   a link to all supported EVM information.

Directory Structure
^^^^^^^^^^^^^^^^^^^

The files used are in the Processor SDK RTOS directory. Expanded below
are the relevant files and directories for flashing the bootable images
for C667x, but a similar structure is used for C665x.

::

    ├── bin
    │   ├── configs
    │   │   └── evm6678l
    │   │       ├── evm6678l.ccxml
    │   │       ├── evm6678le.ccxml
    │   │       ├── evm6678le-linuxhost.ccxml
    │   │       └── evm6678l-linuxhost.ccxml
    │   ├── logs
    │   └── program_evm.js
    └── prebuilt-images
        ├── eeprom50.bin
        ├── eeprom51.bin
        ├── eepromwriter_evm6678l.out
        ├── eepromwriter_input50.txt
        ├── eepromwriter_input51.txt
        ├── eepromwriter_input.txt
        ├── nandwriter_evm6678l.out
        ├── nand_writer_input.txt
        ├── norwriter_evm6678l.out
        └── nor_writer_input.txt

Below is the expanded tree for K2H. Similarly, this also applies to K2E
and K2L EVMs.

::

    ├── bin
    │   ├── configs
    │   │   └── evmk2h
    │   │       ├── evmk2h.ccxml
    │   │       ├── evmk2h-linuxhost.ccxml
    │   │       └── program_evm_config
    │   ├── logs
    │   └── program_evm.js
    └── prebuilt-images
        ├── app
        ├── config
        ├── MLO
        └── spi_flash_writer.out

Default Binaries and Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^

Processor SDK RTOS provides the basic CCXML files to connect to your
SOC. There is a separate CCXML file for each SOC, emulator, and host OS
combination. These CCXML files are located in:

::

     [SDK Install Path]/processor_sdk_rtos_<platform>_<version>/bin/config/<SOC>

Users can choose to use their own CCXML file by setting the environment
variable, **PROGRAM_EVM_TARGET_CONFIG_FILE**, to point to their CCXML
file in their terminal or command prompt.

You can create your own CCXML file by opening CCSv6 --> View --> Target
Configurations, and right-clicking on the Target Configuration pane to
select New Target Configuration. After selecting your SOC and emulator,
remember to set the appropriate GEL file in the advance options for Core
0. The GEL file is used to do basic SOC initialization upon connecting
to the core.

Processor SDK RTOS also provides the basic binaries needed to perform
flashing. These are separated into two categories - flashwriters and
flash images.

Flashwriters

-  [C66x] eepromwriter_<SOC>.out - writes content to your EVM EEPROM
   flash memory
-  [C66x] norwriter_<SOC>.out - writes content to your EVM NOR flash
   memory
-  [C66x] nandwriter_<SOC>.out - writes content to your EVM NAND flash
   memory
-  [K2H/E/L] spi_flash_writer.out - writes multiple images to your NOR
   flash memory

Flash images

-  [C66x] eeprom50.bin - eeprom binary for address 0x50. The default for
   C66x is the POST application.
-  [C66x] eeprom51.bin - eeprom binary for address 0x51. The default for
   C66x is the Intermediate Boot Loader (IBL).
-  [C66x] nor.bin - nor binary to be used for NOR boot. May not be
   provided for every EVM or release version.
-  [C66x] nand.bin - nand binary to be used for NAND boot. May not be
   provided for every EVM or release version.
-  [K2H/K2E/K2L] app - NOR binary to be booted by Secondary Bootloader.
   The default for Keystone 2 is the POST application
-  [K2H/K2E/K2L] MLO - Secondary Bootloader. The default flash location
   is in SPI NOR flash memory at offset 0.

Usage
^^^^^

For Windows users:

::

     > cd [SDK Install Path]\processor_sdk_rtos_<platform>_<version>\bin
     > set DSS_SCRIPT_DIR=[CCS Install Path]\ccsv6\ccs_base\scripting\bin
     > %DSS_SCRIPT_DIR%\dss.bat program_evm.js [tmdx|tmds]evm(6678|6657|k2h|k2e|k2l)[l|le|ls][-le|-be]

For Linux users:

::

     > cd [SDK Install Path]/processor_sdk_rtos_<platform>_<version>/bin
     > export DSS_SCRIPT_DIR=[CCS Install Path]/ccsv6/ccs_base/scripting/bin
     > $DSS_SCRIPT_DIR/dss.sh program_evm.js [tmdx|tmds]evm(6678|6657|k2h|k2e|k2l)[l|le|ls][-le|-be]

The last argument depends on the SOC that you have, concatenated with
the options to select emulator and endianness:

-  l: EVM uses XDS100 on-board Emulator
-  le: EVM uses 560 Mezzanine Emulator daughter card
-  ls: EVM uses XDS200 Emulator card
-  -le: Little Endian
-  -be: Big Endian

.. note::
   -  By default, the images provided are little endian.
   -  Also by default, Keystone 2 EVMs are expected to only use the XDS2xx
      Emulator. You do not have to supply the emulator in the parameter for
      K2H/K2E/K2L.

Some examples are:

TMDXEVM6678LE little endian

::

      > $DSS_SCRIPT_DIR/dss.sh program_evm.js tmdxevm6678le-le

TMDSEVM6657LS little endian

::

      > $DSS_SCRIPT_DIR/dss.sh program_evm.js tmdxevm6657ls-le

EVMK2H little endian

::

      > $DSS_SCRIPT_DIR/dss.sh program_evm.js tmdsevmk2h

EVMK2E little endian

::

      > $DSS_SCRIPT_DIR/dss.sh program_evm.js tmdsevmk2e

Sample Output
^^^^^^^^^^^^^

::

    C:\ti\processor_sdk_rtos_c665x_2_00_01_07\bin>%DSS_SCRIPT_DIR%\dss.bat program_evm.js tmdxevm6657ls-le
    board: evm6657l
    endian: Little
    emulation: XDS200 emulator
    binaries: ../prebuilt-images/
    ccxml: C:\ti\processor_sdk_rtos_c665x_2_00_01_07\bin/configs/evm6657l/evm6657ls.ccxml
    C66xx_0: GEL Output:
    Connecting Target...

    C66xx_0: GEL Output: DSP core #0

    C66xx_0: GEL Output: C6657L GEL file Ver is 1.006

    C66xx_0: GEL Output: Global Default Setup...

    C66xx_0: GEL Output: Setup Cache...

    C66xx_0: GEL Output: L1P = 32K

    C66xx_0: GEL Output: L1D = 32K

    C66xx_0: GEL Output: L2 = ALL SRAM

    C66xx_0: GEL Output: Setup Cache... Done.

    C66xx_0: GEL Output: Main PLL (PLL1) Setup ...

    C66xx_0: GEL Output: PLL in Bypass ...

    C66xx_0: GEL Output: PLL1 Setup for DSP @ 1000.0 MHz.

    C66xx_0: GEL Output:            SYSCLK2 = 333.3333 MHz, SYSCLK5 = 200.0 MHz.

    C66xx_0: GEL Output:            SYSCLK8 = 15.625 MHz.

    C66xx_0: GEL Output: PLL1 Setup... Done.

    C66xx_0: GEL Output: Power on all PSC modules and DSP domains...

    C66xx_0: GEL Output: Set_PSC_State... Timeout Error #03 pd=12, md=4!

    C66xx_0: GEL Output: Power on all PSC modules and DSP domains... Done.

    C66xx_0: GEL Output: DDR3 PLL (PLL2) Setup ...

    C66xx_0: GEL Output: DDR3 PLL Setup... Done.

    C66xx_0: GEL Output: DDR3 Init begin (1333 auto)

    C66xx_0: GEL Output: XMC Setup ... Done

    C66xx_0: GEL Output: IFRDY bit is SET: DDR3 Interface Ready

    C66xx_0: GEL Output:
    DDR3 initialization is complete.

    C66xx_0: GEL Output: DDR3 Init done

    C66xx_0: GEL Output: DDR3 memory test... Started

    C66xx_0: GEL Output: DDR3 memory test... Passed

    C66xx_0: GEL Output: PLL and DDR3 Initialization completed(0) ...

    C66xx_0: GEL Output: configSGMIISerdes Setup... Begin

    C66xx_0: GEL Output: SGMII SERDES has been configured.

    C66xx_0: GEL Output: Enabling EDC ...

    C66xx_0: GEL Output: L1P error detection logic is enabled.

    C66xx_0: GEL Output: L2 error detection/correction logic is enabled.

    C66xx_0: GEL Output: MSMC error detection/correction logic is enabled.

    C66xx_0: GEL Output: Enabling EDC ...Done

    C66xx_0: GEL Output: Global Default Setup... Done.

    Start writing eeprom50
    Writer:../prebuilt-images/eepromwriter_evm6657l.out

    Image:../prebuilt-images/eeprom50.bin

    C66xx_0: GEL Output: Invalidate All Cache...

    C66xx_0: GEL Output: Invalidate All Cache... Done.

    C66xx_0: GEL Output: GEL Reset...

    C66xx_0: GEL Output: GEL Reset... Done.

    C66xx_0: GEL Output: Disable all EDMA3 interrupts and events.

    EEPROM Writer Utility Version 01.00.00.05

    Writing 57432 bytes from DSP memory address 0x0c000000 to EEPROM bus address 0x0050 starting from device address 0x0000
    ...
    Reading 57432 bytes from EEPROM bus address 0x0050 to DSP memory address 0x0c010000 starting from device address 0x0000
    ...
    Verifying data read ...
    EEPROM programming completed successfully
    Start writing eeprom51
    Writer:../prebuilt-images/eepromwriter_evm6657l.out

    Image:../prebuilt-images/eeprom51.bin

    C66xx_0: GEL Output: Invalidate All Cache...

    C66xx_0: GEL Output: Invalidate All Cache... Done.

    C66xx_0: GEL Output: GEL Reset...

    C66xx_0: GEL Output: GEL Reset... Done.

    C66xx_0: GEL Output: Disable all EDMA3 interrupts and events.

    EEPROM Writer Utility Version 01.00.00.05

    Writing 47888 bytes from DSP memory address 0x0c000000 to EEPROM bus address 0x0051 starting from device address 0x0000
    ...
    Reading 47888 bytes from EEPROM bus address 0x0051 to DSP memory address 0x0c010000 starting from device address 0x0000
    ...
    Verifying data read ...
    EEPROM programming completed successfully
    Writer:../prebuilt-images/nandwriter_evm6657l.out

    NAND:../prebuilt-images/nand.bin

    Required NAND files does not exist in ../prebuilt-images/

    Writer:../prebuilt-images/norwriter_evm6657l.out

    NOR:../prebuilt-images/nor.bin

    Required NOR files does not exist in ../prebuilt-images/

In the above example, nothing was flashed to NAND or NOR since there
were no nand.bin or nor.bin binaries to flash.

