.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_BOOT_K2G

Overview
^^^^^^^^^^

The Secondary Bootloader (SBL) for K2G does basic hardware
initialization for the board to load and run applications.

Bootloader Execution Sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Power On Reset occurs
-  ROM Bootloader (RBL) executes. It checks for bootmode and attempts to
   load+run the SBL from that bootmode.
-  SBL begins execution from internal memory (MSMC RAM)

   -  Board Initialization is done by a call to **Board_init()** API.
      For additional details refer to `Processor SDK Board
      Support <index_board.html#board-support>`__.
   -  SBL setup includes configuring Pinmux, enable peripheral clocks,
      set up PLLs, and configure EMIF for DDR.

-  SBL finishes setup and looks for "app" to execute next. This
   user-modifiable application may reside in SD card or QSPI memory
   depending on the bootmode chosen.
-  Once located, app will be loaded into memory and execution will be
   branched to the application's entry address

Tools and Binary Formats
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Making Bootable SBL image (MLO)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

RBL loads and runs "MLO", which is a .out executable formatted by TI
tools. To make a .out, such as SBL, bootable by ROM, you must follow
these steps:

#. **armhex [.out file] [.rmd file]**

   -  .out file is the file you want to boot, such as sbl.out
   -  .rmd file is an input file to specify sections information. An
      example can be found in:
      <PDK_INSTALL_DIR>/packages/ti/boot/sbl/board/evmK2G/build/sbl.rmd
   -  armhex is a tool in TI ARM CGT compiler. This generates a [hex
      file], name of which is specified by the .rmd file

#. **b2ccs [hex file] [ccs file]**

   -  hex file is the output from the previous step
   -  ccs file can be name of your choosing

#. **ccsAddGphdr -infile [ccs file] -outfile [gphdr file] -headerEndian
   BE**

   -  gphdr file can be the name of your choosing

#. **ccsAddGptlr -infile [gphdr file] -outfile [gptlr file]**

   -  gptlr file can be the name of your choosing

#. **byteswapccs [gptlr file] [MLO ccs file]**

   -  MLO ccs file can be the name of your choosing

#. **ccs2bin -swap [MLO ccs file] MLO**

   -  MLO will be created after this step

Armhex is part of TI ARM CGT, in
**<CCS_INSTALL_DIR>/tools/compiler/ti-cgt-arm_x.x.x/bin**. The rest of
the tools can be found in:
**<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools**

Making Loadable User Application image (app)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For converting the compiled .out files to a format loadable by TI's
Secondary Boot Loader (SBL), **you must follow these two steps:**

#. **out2rprc.exe [.out file] [rprc output]**
#. **MulticoreImageGen.exe LE 55 [output name] 0 [rprc output]**

Out2rprc.exe and MulticoreImageGen.exe are tools supplied by TI and can
be located in the **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools**
folder. "rprc output" can be any spare name of your choosing. "output
name" can also be any name of your choosing.

The '0' used in step 2 refers to the Core ID to boot. By default, '0' is
MPU (Cortex A15) core 0. You can input a different value to boot to
other cores. Valid values are:

+------------+-------+
| Core       | Value |
+============+=======+
| MPU Core 0 | 0     |
+------------+-------+
| DSP Core 0 | 5     |
+------------+-------+

If MPU SMP is chosen, the same boot image and entry will be used for all
MPU cores. SBL can also parse multiple boot images that are concatenated
together. Simply use MulticoreImageGen as such:

**MulticoreImageGen.exe LE 55 [output name] [Core ID a] [rprc output a]
[Core ID b] [rprc output b] [Core ID c] [rprc output c] ...**

Boot Modes
^^^^^^^^^^^

This release of SBL supports MMCSD and QSPI boot modes.

MMCSD Boot Mode
""""""""""""""""

Preparing the SD card
'''''''''''''''''''''''

#. To boot the target, the SD card needs to be bootable. Follow the
   steps at `Creating bootable SD card in windows <index_overview.html#windows-sd-card-creation-guide>`__
   or `Creating bootable SD card in Linux <index_overview.html#linux-sd-card-creation-guide>`__.
#. Copy "MLO" and "app" to your SD card.

   -  MLO is the SBL formatted by the aforementioned tools. A pre-built
      MLO can be found at:
      **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/binary/evmK2G/mmcsd/bin**
   -  app is the target application to be booted and also formatted by
      the aforementioned tools. (Note that the tools for making the
      bootable MLO and the loadable app are different).

Booting via SD Card
'''''''''''''''''''''

#. Insert micro SD card into the SD card slot of the board
#. Set the board to MMC/SD bootmode by configuring the DIP switches to
   '0111'. Verify the bootmode on the LCD display on your board
#. Open a serial communication terminal (such as TeraTerm, MiniCom,
   etc.) on host PC and connect to the UART console port
#. Power on the board

| Below is an example of K2G SBL successfully booting the diagnostic
  application:

.. Image:: /images/K2g_boot_diag.jpg

QSPI Boot Mode
""""""""""""""""

Preparing QSPI Flash
''''''''''''''''''''''

MLO and app needs to be flashed into QSPI memory so that they can be
booted. MLO will reside at offset 0 and app will reside at offset
0x80000. QSPI flash memory map:

+----------------+-----+
| Offset 0x0     | MLO |
+----------------+-----+
| Offset 0x80000 | app |
+----------------+-----+

The images can be flashed into QSPI flash by following steps given
below:

#. Copy MLO, app, and config to SD card

   -  MLO is the SBL formatted by the aforementioned tools. A pre-built
      MLO can be found at:
      **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/binary/evmK2G/qspi/bin**
   -  app is the target application to be booted and also formatted by
      the aforementioned tools. (Note that the tools for making the
      bootable MLO and the loadable app are different).
   -  config helps specify the memory map. The default config file can
      be found at:
      **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashWriter/qspi**.
      This config file may be altered to custom user settings if needed.

#. In the SD card, rename MLO to "boot". This is the default name
   specified by the config file.
#. Insert the SD card into the SD card slot on the board
#. Connect to the board with CCS. Launch target configuration and
   connect to the ARM A15 core. GEL file will run on-connect and do
   basic board-level initialization
#. Load the flash writer, qspi_flash_writer.out, to the connected core

   -  A pre-built qspi_flash_writer.out can be found at:
      **<PDK_INSTALL_DIR>/packages/ti/boot/sbl/tools/flashWriter/qspi/bin/evmK2G**

#. Run the QSPI flash writer application. You will see the following
   logs on the EVM's UART console:

::

     *** PDK QSPI Flash Writer ***
     Copying 'boot' to local memory
     Begin flashing 'boot' into QSPI
     Finished flashing 'boot' with size 20010 at offset 0
     Copying 'app' to local memory
     Begin flashing 'app' into QSPI
     Finished flashing 'app' with size 19398 at offset 80000
     Flashing completed!

.. note:: This application will flash the image at required offset without
   taking into consideration any overwriting to previously flashed image.

Booting via QSPI
''''''''''''''''''

#. Set the board to QSPI-48 bootmode by configuring the DIP switches to
   '1111'. Verify the bootmode on the LCD display on your board
#. Open a serial communication terminal (such as TeraTerm, MiniCom,
   etc.) on host PC and connect to the UART console port
#. Power on the board

Memory Usage
^^^^^^^^^^^^^^^^^^^^

SBL uses the last 0x40000 memory from MSMC RAM memory.

The SBL memory map is shown below:

.. Image:: /images/SBL_mem_k2g.jpg

.. note::
   app should not have loadable sections residing in SBL memory region to
   prevent overwriting SBL during load time. It is, however, free to use
   SBL memory after it is loaded and running.

