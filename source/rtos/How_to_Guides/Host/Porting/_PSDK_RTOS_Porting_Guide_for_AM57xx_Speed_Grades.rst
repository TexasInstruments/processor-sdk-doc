.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Porting_Guide_for_AM571x/AM570x_Speed_Grades

Description
^^^^^^^^^^^

The AM57x Family of Processors includes a wide range of operating
performance to meet the needs of a number of broad applications. Among
these options are a variety of speed grades to meet different
performance points. These devices have a number of specialized cores to
provide applications specific computation capabilities. These cores can
be run at different speeds to fine tune the processor to the needs of
the application, power budget, thermal characteristics, etc.

The Processor SDK for RTOS is a software development package provided to
speed development by providing a software reference. This package now
includes support for then entire AM57x family of processors which can be
broken down into the AM572x, AM571x, and AM570x sets of devices or
sub-familes. Most of the devices in this family are supported by the
Processor SDK for RTOS right out of the box. This support is tested and
validated on TI designed EVMs. These EVMs use the highest performance
devices in the family in order to allow users to evaluate the entire
spectrum of performance.

The AM571X and AM570x supports several lower power speed grades. If one
of these devices is being used on the custom board, the GEL file and the
board library needs to be changed to account for this difference. If
this change is not made, the device could be running out of
specification. These changes may reach across other cores and clocks on
the device as well, depending on what speeds they need to operate at.
This document is not an exhaustive list of all the changes needed for a
proper board port as it focused on the changes needed to enable
different speed grades.

Comparison of AM572x, AM571x and AM570x devices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Quick Feature Set comparison between devices in Sitara AM57xx
family :**

.. Image:: /images/AM572x_AM571X_AM570x_Comparison.png

|
| **Supported OPP on AM57xx devices:**

.. Image:: /images/AM57xx_OPP.png

Code Composer Studio (CCS) and Emulation support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TI Supports following evaluation platform for AM57xx class of devices:

-  :ref:`AM572x GP EVM <RTOS-SDK-Supported-Platforms>`
-  :ref:`AM571x IDK <RTOS-SDK-Supported-Platforms>`
-  :ref:`AM572x IDK <RTOS-SDK-Supported-Platforms>`

When developer selects any of the above platforms in Code composer
Studio, the target configuration automatically brings in the required
initialization files and GEL files to configure the clocks, target cores,
external memory.

If you are using a custom platform or AM5708 device that is not
available on a TI Evaluation platform, you can follow the steps provided
below to connect to the SOC by reusing the GEL files that are provided
for TI evaluation platforms. For example, here we demonstrate how you
can create a target configuration for AM570x and connect to the device
if your board design is based of one of TI evalauation platforms listed
below. The assumption here is that the custom board is based off AM571X
IDK platform

.. note::
   Support for AM5708 was added to Sitara Chip Support Package 1.3.4
   in Code composer Studio. If you don`t see the device definition in CCS,
   then you can update the Sitara Chip Support package by going to
   `Help->Check
   Updates <http://ap-fpdsp-swapps.dal.design.ti.com/index.php/File:Check_Updates.png>`__


**Step 1: Select the AM570x part number that is populated on your custom
platform:**

.. Image:: /images/AM5708_EVM_target_configurations.png

**Step 2: Setup the GEL files for the SOC** Go to the Advanced Tab as
shown in the previous screenshot and update startup GEL file in the A15
Core as shown in the screenshot below

.. Image:: /images/Advanced_settings_GEL_setup.png

Board Library Changes to Consider for Using Processor SDK RTOS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Clock and PRCM Updates to consider
""""""""""""""""""""""""""""""""""

The board library provides setting for OPP_NOM, OPP_OD and OPP_HIGH in
the PLL settings using 20 MHz input clock that has been used on the
AM572x GP EVM as well as the AM571x IDK platform. This allows customers
to setup the MPU to 1.5, 1.176 and 1GHz. For AM570x devices, we support
the "J" and the "D" variant which support the following max speeds on
the DPLLs:

.. Image:: /images/AM5706_Speed_Grades.png

When using the "J" speed grade, ensure that the DPLLs in the board set
the DPLL to OPP_NOM and not for OPP_OD or OPP_HIGH.

To do this, you can invoke the Board_Init from your application using
either

.. code-block:: c

    Board_initCfg boardCfg;
    boardCfg = BOARD_INIT_PLL_OPP_NOM;
    boardCfg |= BOARD_INIT_UNLOCK_MMR |
           BOARD_INIT_MODULE_CLOCK |
           BOARD_INIT_PINMUX_CONFIG |
           BOARD_INIT_DDR |
           BOARD_INIT_UART_STDIO |
           BOARD_INIT_WATCHDOG_DISABLE;
    /* Board Library Init. */
       Board_init(boardCfg);

.. note::
   When bootloading direct from flash media, this change may also be
   required in the SBL code

When using "D" rated parts that run at 500 MHz, in addition to the
above configuration, you will also need to modify OPP_NOM settings in
the board library by updating the DPLL setting for MPU and DSP in the
file <BoardName>_pll.c as shown below:

**Step1 : Update MPU, DSP, IVA and GPU DPLL setting**

-  **MPU DPLL Changes:**

.. code-block:: c

      /* Default to OPP_NOM */
           /* 500MHz at 20MHz sys_clk */
           mpuPllcParam.mult = 250U;
           mpuPllcParam.div = 9U;
           mpuPllcParam.dccEnable = 0U;
           mpuPllcParam.divM2 = 1U;

-  **DSP DPLL Changes:**

.. code-block:: c

           /* 500MHz at 20MHz sys_clk */
           dspPllcParam.mult = 130U;
           dspPllcParam.div = 3U;
           dspPllcParam.divM2 = 1U;
           dspPllcParam.divM3 = 3U;

-  **Remove IVA and GPU PLL settings**

Since IVA and GPU modules are not available on the device, we recommend
removing the ivaPLL and gpuPLL settings in board.

.. code-block:: c

                  /* Default to OPP_NOM */
                  /* 388.3MHz at 20MHz sys_clk */
    -                ivaPllcParam.mult = 233U;
    -                ivaPllcParam.div = 3U;
    -                ivaPllcParam.divM2 = 3U;


                 /* Default to OPP_NOM */
                 /* 425MHz at 20MHz sys_clk */
    -                gpuPllcParam.mult = 170U;
    -                gpuPllcParam.div = 3U;
    -                gpuPllcParam.divM2 = 2U;

**Step 2 : Disable clocks configuration and wakeup for IVA in PRCM**

-  **Remove IVA wakeup and Module configuration**

The following updates need to be made in the file <BoardName>_clock.c to
remove IVA wakeup and clock configuration

.. code-block:: c

    -        CSL_FINST(ivaCmReg->CM_IVA_CLKSTCTRL_REG,
    -        IVA_CM_CORE_CM_IVA_CLKSTCTRL_REG_CLKTRCTRL, SW_WKUP);


       /* PRCM Specialized module mode setting functions */
    -   CSL_FINST(ivaCmReg->CM_IVA_SL2_CLKCTRL_REG,
    -       IVA_CM_CORE_CM_IVA_SL2_CLKCTRL_REG_MODULEMODE, AUTO);
    -  while(CSL_IVA_CM_CORE_CM_IVA_SL2_CLKCTRL_REG_IDLEST_DISABLE ==
    -      CSL_FEXT(ivaCmReg->CM_IVA_SL2_CLKCTRL_REG,
    -       IVA_CM_CORE_CM_IVA_SL2_CLKCTRL_REG_IDLEST));
    -   CSL_FINST(ivaCmReg->CM_IVA_IVA_CLKCTRL_REG,
    -       IVA_CM_CORE_CM_IVA_IVA_CLKCTRL_REG_MODULEMODE, AUTO);
    -   while(CSL_IVA_CM_CORE_CM_IVA_IVA_CLKCTRL_REG_IDLEST_DISABLE ==
    -      CSL_FEXT(ivaCmReg->CM_IVA_IVA_CLKCTRL_REG,
    -       IVA_CM_CORE_CM_IVA_IVA_CLKCTRL_REG_IDLEST));

Configure DDR Interfaces
^^^^^^^^^^^^^^^^^^^^^^^^

An important one to consider is the speed of the DDR memory. The clock
for the DDR is selected using the same dplls structure. Some higher
speed grade parts support a 667 MHz DDR clock, but some of the lower
speed grade parts only support a 533 MHz DDR3 clock. Make sure to choose
the appropriate DDR clock for the device on the custom board.

Over in the board/src/<BoardName>/<BoardName_ddr>.c file, make sure that
the EMIF is being configured correctly for the appropriate speed, and
that the appropriate number of EMIFs is being selected to match the part
being used. AM572x part has 2 DDR interfaces running at 533 MHz and the
AM571x (and AM570x) only have one running at 667 MHz. This code can be
kept or removed by the board port. As changes are made, the code must
make sure to configure the new board correctly, with the appropriate
number of DDR interfaces and speed configuration.

For AM571x and AM570x, make sure to use the code for the AM571x IDK in
board/src/<BoardName>/<BoardName_ddr>.c to select 1 EMIF:

.. code-block:: c

          /* MA_LISA_MAP_i */
          hMampuLsm->MAP_0 = 0x80600100U;
          /* DMM_LISA_MAP_i */
          hDmmCfg->LISA_MAP[0U] = 0x80600100U;

For AM572x, this is mapped as following

.. code-block:: c

      /* MA_LISA_MAP_i */
      hMampuLsm->MAP_0 = 0x80740300;
      hMampuLsm->MAP_1 = 0x80740300;
      /* DMM_LISA_MAP_i */
      hDmmCfg->LISA_MAP[0U] = 0x80740300;
      hDmmCfg->LISA_MAP[1U] = 0x80740300;

.. note::
   Processor SDK RTOS provides am570x_ddr.c file in the idkAM571x board
   library for reference for configuring DDR on AM570x parts

Pinmux Changes to Consider
^^^^^^^^^^^^^^^^^^^^^^^^^^

-  For part number where the Display subsystem or SATA is not available,
   the pins can be configured to any other pin functionality that may be
   required in the system. If you don`t need to use these pins, we
   recommend that you leave these pins in default MUXMODE and terminate
   the pinmux as recommended in the `Schematics
   Checklist <http://processors.wiki.ti.com/index.php/AM57xx_Schematic_Checklist>`__.
-  There is no pinmux setting for CSI2 module so you can leave the
   MUXMODE=0 on those pins if there is no instance of the peripheral

.. note::
   Processor SDK RTOS provides board/src/idkAM571x/include/am570x_pinmux.h
   file in the idkAM571x board library for reference for configuring pinmux
   on AM570x based hardware platform


Driver SOC Module clock changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some control drivers use default Module input clock frequency settings
in <module>_soc.c file that gets used by the Low level drivers to
configure the peripheral clocks. The default module input clock
frequency is set to the OPP_NOM values that are available on the
superset variant of the device so if you are using lower speed grades.
Ensure you change the default to match the module clock on the 500 MHz
settings or you can use the following sequence to update the settings.
Code below describes how the SPI driver module input clock frequency can
be modified

.. code-block:: c

       SPI_v1_HWAttrs spi_cfg;
       /* Get the default SPI init configurations */
       SPI_socGetInitCfg(TEST_SPI_PORT, &spi_cfg);
       /* Modify the default SPI configurations if necessary */
       spi_cfg.inputClkFreq = 24000000;
       /* Set the default SPI init configurations */
       SPI_socSetInitCfg(TEST_SPI_PORT, &spi_cfg);

Related Article for Processor SDK Linux developers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Linux_Porting_Guide_for_AM571x/AM570x_Speed_Grades <http://processors.wiki.ti.com/index.php/Linux_Porting_Guide_for_AM571x/AM570x_Speed_Grades>`__

.. rubric:: Useful Utilities
   :name: useful-utilities

-  `Clock Tree Tool <http://www.ti.com/tool/clockTreeTool>`__
-  `Pin Mux tool <http://www.ti.com/tool/PinMuxTool>`__

Support
^^^^^^^

For any questions related Usage of AM572x, AM571x and AM570x devices,
please post your question on TI E2E Forums

-  `TI E2E Forums for Sitara
   Processors <https://e2e.ti.com/support/arm/sitara_arm/>`__

