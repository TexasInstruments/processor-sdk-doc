.. http://processors.wiki.ti.com/index.php/Adding_Custom_Board_Library_Target_to_Processor_SDK_RTOS_makefiles

Introduction
^^^^^^^^^^^^^

The following article describes how a custom Board can be added to the
Processor SDK RTOS. The scope of this article is to only describe how to
modify the build files in the PDK to add build steps for your custom
board library. The article does not describe modification of source
files to reflect changes to clocking, DDR and pinmux setup for the
custom board.

The instructions provided in this article uses example of AM572x custom
board but the instructions apply to all the processors supported in
Processor SDK RTOS. Note that the instructions on this wiki were created
using Processor SDK RTOS v3.2 and PDK_AM57xx_1_0_5 and are subject to
change. Also the wiki was created specifically for the newer board
variants like evmAM572x, idkAM572x and evmK2G. For AM335x and AM437x
variant board library has several dependencies on legacy starterware
package, hence additional steps are required and not covered in the
wiki.

Instructions to add custom Board to the PDK build
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Step 1: Creating new directory for custom board library**

In pdk_am57xx_x_x_x/packages/ti/board/src,
Create new directory myCustomBoard and copy files from existing board
library package. We recommend that you copy files from the board which
closely matches your custom board design. In this case, we assume that
the custom board is based on the design of evmAM572x so we copy over
the files from that directory into myCustomBoard folder.

**Step 2: Updating names and makefile inside the customBoard package**

In pdk_am57xx_x_x_x/packages/ti/board/src/myCustomBoard, Rename file
src_files_evmAM572x.mk to src_files_myCustomBoard.mk. This file will
need a bit of work depending on what elements of board you need for your
platform. We have left all the files evmAM572x_*.c but you can modify as
needed.

**Step 3: Adding MACRO based inclusion of updated board_cfg.h
corresponding to custom Board**

In packages/ti/board/board_cfg.h, add the lines pointing to board_cfg.h
file in your customBoard package so that updated peripheral instances
and board specific defines can be picked up

::

    #if defined (myCustomBoard)
    #include <ti/board/src/myCustomBoard/include/board_cfg.h>
    #endif

**Step 4: Update top level board package makefile to include build for
customBoard Library** The makefile is used to include all relevant make
files for including Low level driver(LLD), source files relevant to
board and the common board.c file

-  In packages/ti/board/build/makefile.mk, add board.c to the
   customBoard build :

::

    ifeq ($(BOARD),$(filter $(BOARD),evmAM335x icev2AM335x skAM335x bbbAM335x evmAM437x idkAM437x skAM437x myCustomBoard evmAM572x idkAM571x idkAM572x evmK2H evmK2K evmK2E evmK2L evmK2G iceK2G evmC6678 evmC6657))
    # Common source files across all platforms and cores
    SRCS_COMMON += board.c
    endif

-  Add board library source files and LLD files to the customBoard build

In packages/ti/board/build/makefile.mk, change

::

    ifeq ($(BOARD),$(filter $(BOARD), evmAM572x idkAM571x idkAM572x))
    include $(PDK_BOARD_COMP_PATH)/src/$(BOARD)/src_files_$(BOARD).mk
    include $(PDK_BOARD_COMP_PATH)/src/src_files_lld.mk
    CFLAGS_LOCAL_$(BOARD) += -D$(BOARD)
    endif

to

::

    ifeq ($(BOARD),$(filter $(BOARD), myCustomBoard evmAM572x idkAM571x idkAM572x))
    include $(PDK_BOARD_COMP_PATH)/src/$(BOARD)/src_files_$(BOARD).mk
    include $(PDK_BOARD_COMP_PATH)/src/src_files_lld.mk
    CFLAGS_LOCAL_$(BOARD) += -D$(BOARD)
    endif

**Step 5: Update Global makerules**

build_config.mk defines the global CFLAGS used to compile different PDK
components. Add the following line in the BOARD Specific configurations.

::

    CFLAGS_GLOBAL_customAM572x  = -DSOC_AM572x -DevmAM572x

The SOC_AM572x macro ensures that the CSL aplicable to this SOC will be
included in the build and evmAM572x define will ensure all evmAM572x
specific includes that apply to the customAM572x are part of the build.


**Optional step to update RTSC platform definition** If you have a
custom RTSC platform definition for your custom board that updates the
memory and platform configuration using RTSC Tool then you need to
update the platform.mk file that associates the RTSC platfom with the
corresponding board library

In packages/ti/buildmakerules/platform.mk, add the following lines:


::

     ifeq ($(BOARD),$(filter $(BOARD), evmAM572x))
       PLATFORM_XDC = "ti.platforms.evmAM572X"
     endif

::

     ifeq ($(BOARD),$(filter $(BOARD), myCustomBoard))
       PLATFORM_XDC = "evmAM572XCustom"
     endif

.. note::
   The SYSBIOS platforms follow the convention to consolidate all
   platform definitions under SYSBIOS_INSTALL_PATH/packages/ti/platforms/\*
   hence the convention ti.platorms.<platformName> but for custom platform,
   users are not required to follow this convention.

**Step 6: Update source files corresponding to drivers used in board
library**. src_files_lld.mk file adds source files corresponding to LLD
drivers used in the board library. Usually most boards utilitize control
driver like I2C (for programming the PMIC or reading EEPROM), UART
drivers (for IO) and boot media drivers like (SPI/QSPI, MMC or NAND). In
the example below, we assume that the custom Board library has
dependency on I2C, SPI and UART LLD drivers. Since the LLD drivers will
be linked to the application along with board library, board library
only needs <driver>_soc.c corresponding to SOC used on the custom Board.

In packages/ti/board/src/src_files_lld.mk, add the following lines:


::

    ifeq ($(BOARD),$(filter $(BOARD), myCustomBoard))
    SRCDIR +=  $(PDK_INSTALL_PATH)/ti/drv/i2c/soc/am572x \
               $(PDK_INSTALL_PATH)/ti/drv/uart/soc/am572x \
               $(PDK_INSTALL_PATH)/ti/drv/spi/soc/am572x

::

    INCDIR +=  $(PDK_INSTALL_PATH)/ti/drv/i2c/soc/am572x \
               $(PDK_INSTALL_PATH)/ti/drv/uart/soc/am572x \
               $(PDK_INSTALL_PATH)/ti/drv/spi/soc/am572x

::

    # Common source files across all platforms and cores
    SRCS_COMMON += I2C_soc.c UART_soc.c SPI_soc.c
    endif


.. note::
   For all LLD drivers linked to the board library you need to include
   corresponding <drv>_soc.c file. For example if you include GPIO driver
   for setting board mux then GPIO_soc.c needs to be added to LLD source
   files.

**Step 7: Add custom Board to BOARDLIST and update CORELIST**

In packages/ti/board/board_component.mk, modify the build to add your
custom board and specify the cores for which you want to build the board
library. Example to build board library for only A15 and C66x cores,
limit the build by specify only a15_0 and C66x in the CORELIST

::

    board_lib_BOARDLIST       = myCustomBoard evmAM335x icev2AM335x skAM335x bbbAM335x evmAM437x idkAM437x skAM437x evmAM572x idkAM571x idkAM572x evmK2H evmK2K evmK2E evmK2L evmK2G iceK2G \

::

    #board_lib_am572x_CORELIST = c66x a15_0 ipu1_0
    board_lib_am572x_CORELIST = a15_0 c66x

**Step 8: Update .bld files for XDCTOOL based build steps.**

Make corresponding changes in packages/ti/board/config.bld, by adding
the following lines:

::

    var myCustomBoard = {
       name: "myCustomBoard",
       ccOpts: "-DevmAM572x -DSOC_AM572x",
       targets: [C66LE,A15LE ]
       lldFiles: [ "$(PDK_INSTALL_PATH)/ti/drv/i2c/soc/am572x/I2C_soc.c",
               "$(PDK_INSTALL_PATH)/ti/drv/uart/soc/am572x/UART_soc.c",
               "$(PDK_INSTALL_PATH)/ti/drv/spi/soc/am572x/SPI_soc.c"]
    }

::

    var boards = [ evmAM335x, icev2AM335x, skAM335x, bbbAM335x, evmAM437x, idkAM437x, skAM437x, myCustomBoard, evmAM572x, idkAM571x, idkAM572x, evmK2H, evmK2K, evmK2E, evmK2L, evmK2G, evmC6678, evmC6657 ];

Also, in packages/ti/board/package.bld, I added the following line:

::

    Pkg.otherFiles[Pkg.otherFiles.length++] = "src/myCustomBoard/src_files_myCustomBoard.mk";


**Step 9: Setup Top level PDK build files to add the Custom board to
setup environment.**

Final setup involves updating the top level setup file for PDK package
to update to setup the build environment to include the custom Board in
setup. This can be done by commenting out the top line and adding in the
bottom line in pdksetupenv.bat:


::

    @REM if not defined LIMIT_BOARDS set LIMIT_BOARDS=evmAM572x idkAM571x idkAM572x
    if not defined LIMIT_BOARDS set LIMIT_BOARDS=myCustomBoard

**Alternative:** Invoke the build using command line options to limit
the build to specific board, specific SOC and specific CORE. For
example, if you want to build the A15 version of board library for
AM572x EVM, you can invoke the build using:

::

    gmake board_lib LIMIT_SOCS=am572x LIMIT_BOARDS=customAM572x LIMIT_CORES=a15_0



**Step 10 : Building the custom board with the updated settings**

To build package change directory to
<SDK_INSTALL_PATH>/pdk_am57xx_x_x_x/packages, first run pdksetupenv.bat

To make just the board library: gmake board_lib


Example custom Board library for reference
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The package provided below provides updated files for building
customBoard "customAM572x" following all steps described above. Please
compare the files to the evmAM57xx board library files to follow the
steps to add your own board library.

`File:Pdk packages ti board
customAM572x.zip </index.php?title=Special:Upload&wpDestFile=Pdk_packages_ti_board_customAM572x.zip>`__

.. note::
   Due to software distribution policy on the wiki, we have removed the
   file linked here. Users can refer to the discussion and zipped package
   linked from E2E post provided below:

-  `E2E post on creation of custom board
   library <https://e2e.ti.com/support/arm/sitara_arm/f/791/p/555022/2040948#pi316653=2>`__

Additional steps for AM335x/AM437x users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   Currently the AM335x and AM437x board libraries re-use the board support
   that was used in legacy starterware software. AM335x and AM437x users
   will need to additionally modify build files in starterware to build
   their custom board library. Additional steps required for AM335x/AM437x
   will be added to this article soon in this section

