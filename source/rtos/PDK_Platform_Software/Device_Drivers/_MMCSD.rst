.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_MMCSD

Overview
--------

Introduction
^^^^^^^^^^^^

MMCSD module provides an interface between CPU and any
MMCSD-bus-compatible device that connects via MMCSD serial bus. External
components attached to MMCSD bus can serially transmit/receive data
to/from the CPU device through two-wire interface

.. rubric:: Key Features
   :name: key-features

| Type of transfers

   -   Read
   -   Write
   -   Write followed by read

| Operating modes

   -   Blocking(interrupt or Non interrupt)
   -   Callback mode(interrupt)

| Supports only controller mode. Peripheral mode is not supported

|

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

.. rubric:: **Board Specific Configuration**
   :name: board-specific-configuration

All board specific configurations eg:enabling clock and pin-mux for
UART pins are required before calling any driver APIs.By default
Board_Init() API supports all initialization sequence for TI supported
EVMs. In addition it initializes UART instance for Console/STDIO.Refer
`Processor SDK RTOS Board
Support <index_board.html#board-support>`__ for
additional details.Once board specific configuration is complete
MMCSD_init() API can be called to initialize driver.

.. rubric:: **MMCSD Configuration Structure**
   :name: mmcsd-configuration-structure

The MMCSD_soc.c file binds driver with hardware attributes on the
board through MMCSD_config structure. This structure must be
initialized before the MMCSD_init() function is called and cannot be
changed afterwards. For details about the individual fields of this
structure, see the Doxygen help by opening
\\docs\\doxygen\\html\\index.html

APIs
^^^^^

Reference for API header file with documentation

::

    #include <ti/drv/mmcsd/MMCSD.h>

.. rubric:: API Call Flow
   :name: api-call-flow

The below sequence indicates the calling sequence of MMCSD driver APIs
for a use case of write transaction in blocking mode:

::

     MMCSD_Handle MMCSD;
     UInt peripheralNum = 0; /* Such as MMCSD0 */
     MMCSD_Params MMCSDParams;
     ...
     MMCSD_Params_init(&MMCSDParams);
     MMCSD = MMCSD_open(peripheralNum, &MMCSDParams);<br>if (MMCSD == NULL) {<br> /* Error opening MMCSD */
     ...
     readOK = MMCSD_read(MMCSD, rxBuffer , startBlock, numBlock); /* Perform MMCSD read */
     if (!transferOK) { /* MMCSD transaction failed */}

     writeOK = MMCSD_write(MMCSD, TxBuffer , startBlock, numBlock); /* Perform MMCSD write */
     if (!writeOK) { /* MMCSD transaction failed */}


.. rubric:: eMMC Usage
   :name: emmc-usage

MMCSD driver supports eMMC device. Application need to configure the
eMMC device for an instance of peripheral. It is also recommended to
configure the operating bus width of eMMC device.

::

    mmcsdInitCfg[MMCSD_INSTANCE].cardType = MMCSD_CARD_EMMC;
    mmcsdInitCfg[MMCSD_INSTANCE].supportedBusWidth = MMCSD_BUS_WIDTH_8BIT;
    MMCSD_init();

.. rubric:: EDMA Usage
   :name: edma-usage

MMCSD driver supports EDMA operations to transfer data between memory
and MMCSD peripheral.

Driver uses separate source files for these operations.Refer source
MMCSD_soc.c for DMA MMCSD SOC configuration. Application need to create
EDMA handle and update the configuration before MMCSD_init() API.

::

    mmcsdInitCfg[MMCSD_INSTANCE].edmaHandle = MMCSDApp_edmaInit();/* Refer Example/Test */
    MMCSD_init();

Refer “MMCSD_[Usecase]_[Board/SoC]_DMA_[cpu][Example/Test]project” for
additional reference. Refer SDK Release Note for supported EVMs.

.. rubric:: UHS Mode Usage
   :name: uhs-mode-usage

The MMCSD driver supports UHS-I cards. Feature is available for AM57x
SOC and is dependent on board or platform support for run-time switching
from 3.0V to 1.8V. Feature is validated on AM572x GP EVM 3.0

Application
------------

Examples & Unit tests
^^^^^^^^^^^^^^^^^^^^^

+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| Name                             |   Description                 |  Expected Results     |  Supported SOCs | Build Type   |
+==================================+===============================+=======================+=================+==============+
| MMCSD_FATFS_ExampleProject       |   Example initializes         | When a card is        |  AM335x         |              |
|                                  |   the card and checks         | detected with valid   |  AM437x         |              |
|                                  |   for valid FAT               | FAT partition a       |  AM571x         |              |
|                                  |   partition. When a           | console interface     |  AM572x         |              |
|                                  |   valid FAT partition         | apperas like "0:> "   |  AM574x         |              |
|                                  |   is detected console         |                       |  K2G            |              |
|                                  |   interface for               |                       |  OMAPL137x      |              |
|                                  |   command execution           |                       |  OMAPL138x      |              |
|                                  |   is provided.                |                       |                 | CCS Project  |
|                                  |   Console commands            |                       |                 |              |
|                                  |   supported are ls            |                       |                 |              |
|                                  |   (to list files of           |                       |                 |              |
|                                  |   directory), cd              |                       |                 |              |
|                                  |   (change directory),         |                       |                 |              |
|                                  |   pwd (present                |                       |                 |              |
|                                  |   working directory)          |                       |                 |              |
|                                  |   and cat (text file          |                       |                 |              |
|                                  |   read operation).            |                       |                 |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_Test_Project               |                               | Prints  on  console   |  AM335x         |              |
|                                  |   Unit Test                   | All tests have passed |  AM437x         |              |
|                                  |   application                 |                       |  AM571x         |              |
|                                  |   demonstrating write         |                       |  AM572x         |              |
|                                  |   and read a fixed            |                       |  AM574x         | CCS Project  |
|                                  |   number of bytes             |                       |  K2G            |              |
|                                  |   into MMCSD card.            |                       |  OMAPL137x      |              |
|                                  |   Verifies written            |                       |  OMAPL138x      |              |
|                                  |   data pattern to             |                       |                 |              |
|                                  |   conclude PASS/FAIL.         |                       |                 |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_DMA_Test_Project           |                               | Prints on console     |  AM335x         |              |
|                                  |   Unit Test                   | All tests have passed |  AM437x         |              |
|                                  |   application                 |                       |  AM571x         |              |
|                                  |   demonstrating write         |                       |  AM572x         |              |
|                                  |   and read a fixed            |                       |  AM574x         | CCS Project  |
|                                  |   number of bytes             |                       |  K2G            |              |
|                                  |   into MMCSD card.            |                       |  OMAPL137x      |              |
|                                  |   Verifies written            |                       |  OMAPl138x      |              |
|                                  |   data pattern to             |                       |                 |              |
|                                  |   conclude PASS/FAIL.         |                       |                 |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_SMP_Test_Project           |                               | Prints  on  console   |  AM572x - EVM   |              |
|                                  |   Unit Test                   | All tests have passed |                 |              |
|                                  |   application                 |                       |                 |              |
|                                  |   demonstrating write         |                       |                 |              |
|                                  |   and read a fixed            |                       |                 | CCS Project  |
|                                  |   number of bytes             |                       |                 |              |
|                                  |   into MMCSD card.            |                       |                 |              |
|                                  |   Verifies written            |                       |                 |              |
|                                  |   data pattern to             |                       |                 |              |
|                                  |   conclude PASS/FAIL in SMP   |                       +-----------------+--------------+
|                                  |   mode.                       |                       |  am65xx,j721e   |   makefile   |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_SMP_DMA_Test_Project       |                               | Prints on console     |  AM572x - EVM   |              |
|                                  |   Unit Test                   | All tests have passed |                 |              |
|                                  |   application                 |                       |                 |              |
|                                  |   demonstrating write         |                       |                 |              |
|                                  |   and read a fixed            |                       |                 | CCS Project  |
|                                  |   number of bytes             |                       |                 |              |
|                                  |   into MMCSD card.            |                       |                 |              |
|                                  |   Verifies written            |                       |                 |              |
|                                  |   data pattern to             |                       |                 |              |
|                                  |   conclude PASS/FAIL in SMP   |                       +-----------------+--------------+
|                                  |   mode with DMA enabled.      |                       |  am65xx,j721e   |   makefile   |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_EMMC_TestProject           |                               | Prints on console     |  AM335x         |              |
|                                  |   Unit Test                   | All tests have passed |  AM437x         |              |
|                                  |   application                 |                       |  AM571x         |              |
|                                  |   demonstrating write         |                       |  AM572x         |              |
|                                  |   and read a fixed            |                       |  AM574x         | CCS Project  |
|                                  |   number of bytes             |                       |  K2G            |              |
|                                  |   into eMMC device.           |                       |  OMAPL137x      |              |
|                                  |   Verifies written            |                       |  OMAPL138x      |              |
|                                  |   data pattern to             |                       |                 |              |
|                                  |   conclude PASS/FAIL.         |                       |                 |              |
|                                  |                               |                       |                 |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_EMMC_DMA_TestProject       |                               | Prints on console     |  AM335x         |              |
|                                  |   Unit Test                   | All tests have passed |  AM437x         |              |
|                                  |   application                 |                       |  AM571x         |              |
|                                  |   demonstrating write         |                       |  AM572x         |              |
|                                  |   and read a fixed            |                       |  AM574x         |              |
|                                  |   number of bytes             |                       |  K2G            | CCS Project  |
|                                  |   into eMMC device.           |                       |  OMAPL137x      |              |
|                                  |   Verifies written            |                       |  OMAPL138x      |              |
|                                  |   data pattern to             |                       |                 |              |
|                                  |   conclude PASS/FAIL.         |                       |                 |              |
|                                  |                               |                       |                 |              |
|                                  |                               |                       |                 |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMC Test Application             |                               | Prints on console     |                 |              |
|                                  |   Unit Test                   | All tests have passed |                 |              |
|                                  |   application                 |                       |                 |              |
|                                  |   demonstrating write         |                       |                 |              |
|                                  |   and read a fixed            |                       |                 |              |
|                                  |   number of bytes             |                       |                 |              |
|                                  |   into MMC device.            |                       |                 |              |
|                                  |   Verifies written            |                       |                 |              |
|                                  |   data pattern to             |                       |                 |              |
|                                  |   conclude PASS/FAIL.         |                       |                 |              |
|                                  |   Supported only on           |                       |                 |              |
|                                  |   OMAPL137 platform.          |                       |  OMAPL137x      | CCS Project  |
|                                  |                               |                       |                 |              |
|                                  |   There is no on-board        |                       |                 |              |
|                                  |   eMMC chip on OMAPL137       |                       |                 |              |
|                                  |   platform. Need to use       |                       |                 |              |
|                                  |   external MMC card           |                       |                 |              |
|                                  |   inserted into MMCSD         |                       |                 |              |
|                                  |   slot of the board.          |                       |                 |              |
|                                  |   Currently the driver        |                       |                 |              |
|                                  |   supports standard MMC       |                       |                 |              |
|                                  |   card and other cards        |                       |                 |              |
|                                  |   like MMCplus may not        |                       |                 |              |
|                                  |   work. The example           |                       |                 |              |
|                                  |   requires the card           |                       |                 |              |
|                                  |   size to be at least         |                       |                 |              |
|                                  |   2GB.                        |                       |                 |              |
|                                  |                               |                       |                 |              |
|                                  |                               |                       |                 |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_TestApp                    |                               | Prints on console     |                 |              |
|                                  |   Unit Test                   | All tests have passed |                 |              |
|                                  |   application                 |                       |                 |              |
|                                  |   demonstrating write         |                       |                 |              |
|                                  |   and read a fixed            |                       |                 |              |
|                                  |   number of bytes             |                       |  AM65x          | Makefile     |
|                                  |   into MMCSD card.            |                       |  J721e          |              |
|                                  |   Verifies written            |                       |                 |              |
|                                  |   data pattern to             |                       |                 |              |
|                                  |   conclude PASS/FAIL.         |                       |                 |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
|  MMCSD_DMA_TestApp               |   Functionally same           | Prints on console     |                 |              |
|                                  |   as MMCSD_TestApp            | All tests have passed |                 |              |
|                                  |   but with DMA enabled        |                       |  AM65x          | Makefile     |
|                                  |                               |                       |  J721e          |              |
|                                  |                               |                       |                 |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_EMMC_TestApp               |                               |                       |                 |              |
|                                  |   Unit Test                   | Prints  on console    |                 |              |
|                                  |   application                 | All tests have passed |                 |              |
|                                  |   demonstrating write         |                       |                 |              |
|                                  |   and read a fixed            |                       |  AM65x          | Makefile     |
|                                  |   number of bytes             |                       |  J721e          |              |
|                                  |   into the onboard            |                       |                 |              |
|                                  |   EMMC.Verifies written       |                       |                 |              |
|                                  |   data pattern to             |                       |                 |              |
|                                  |   conclude PASS/FAIL.         |                       |                 |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_EMMC_DMA_TestApp           |   Functionally                | Prints on console     |                 |              |
|                                  |   Same as EMMC_TestApp        | All tests have passed |  AM65x          | Makefile     |
|                                  |   but using  DMA mode         |                       |  J721e          |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_Baremetal_TestApp          |   Baremetal version of        | Prints on console     |                 |              |
|                                  |   MMCSD_TestApp               | All tests have passed |                 |              |
|                                  |                               |                       |  AM65x          | Makefile     |
|                                  |                               |                       |  J721e          |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_Baremetal_DMA_TestApp      |   Baremetal version of        | Prints on console     |                 |              |
|                                  |   MMCSD_EMMC_TestApp          | All tests have passed |                 |              |
|                                  |                               |                       |  AM65x          | Makefile     |
|                                  |                               |                       |  J721e          |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_Baremetal_EMMC_TestApp     |   Baremetal version of        | Prints on console     |                 |              |
|                                  |   MMCSD_EMMC_TestApp          | All tests have passed |                 |              |
|                                  |                               |                       |  AM65x          | Makefile     |
|                                  |                               |                       |  J721e          |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_Baremetal_EMMC_DMA_TestApp |   Functionally same as        | Prints on console     |                 |              |
|                                  |   MMCSD_Baremetal_EMMC_TestApp| All tests have passed |                 |              |
|                                  |   but with DMA enabled        |                       |  AM65x          | Makefile     |
|                                  |                               |                       |  J721e          |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_Regression_TestApp         |   Menu driven regression test | Prints on console     |                 |              |
|                                  |   which tests various         | All tests have passed |  AM65x          | Makefile     |
|                                  |   configurations of SD card   |                       |  J721e          |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+
| MMCSD_EMMC_Regression_TestApp    |   Menu driven regression test | Prints on console     |                 |              |
|                                  |   which tests various         | All tests have passed |  AM65x          | Makefile     |
|                                  |   configurations of EMMC      |                       |  J721e          |              |
+----------------------------------+-------------------------------+-----------------------+-----------------+--------------+

Benchmarking Read/Write Performance (on AM65x/J721e)
-----------------------------------------------

The MMCSD_<EMMC>_Regression_TestApp application (listed above) measures
read/write throughput (in mega bytes per sec).

It measures the following:

- RAW read/write throughput:  This involves the reading/writing of a continuous
  block of data, say 1MB data buffer on to the SD/eMMC using
  MMCSD_Read()/MMCSD_Write().

- FATFS read/write (SD Only) throughput: This involves reading/writing of a 1MB
  buffer of data through f_read()/f_write(). Please note that FAT32 is tested
  with SD card only

Benchmarking Steps
------------------

The performance benchmarks on SD Read/Write can be done with the following
steps:

- Load the MMCSD_Regression_TestApp on A53/R5 core of AM65x or mpu1_0/mcu1_0
  core of J721e

- Insert SD Card formatted with FAT32 format preferably with allocation
  size=4096 bytes for better performance.

- Run the application. It presents with a menu of various modes the SD card
  which can be run on the UART console

- Select the desired mode from the list (say HS mode) and press Enter

- The test will run RAW & FATFS read/writes of various buffer sizes 256K, 512K,
  1024K and 2048K. This might take a minute or two to complete.

- Two tables are printed at the end of the test run for this mode with RAW &
  FATFS throughput numbers for each buffer size.

- Note: Instead of running each mode seperately, you can select "All non
  powercycle tests" option (-1)  which runs all the supported modes along with
  the throughput numbers for each of them.


EMMC performance benchmarks can be measured with the following steps

- Load the MMCSD_EMMC_Regression_TestApp on A53/R5 core of AM65x or
  mpu1_0/mcu1_0 core of J721e

- Run the application. It presents with a menu of various eMMC modes which can
  be run on the UART console

- Select the desired mode from the list (say HS-DDR mode) and press Enter

- The test will run RAW read/writes of various buffer sizes 256K, 512K, 1024K
  and 2048K. This might take a minute or two to complete.

- A table is printed at the end of the test with the RAW throughput numbers for
  each buffer size.

.. note:: Instead of running each mode seperately, you can select "All non
   powercycle tests" option (-1)  which runs all the supported modes along with
   the throughput numbers for each of them.

Building CCS projects based examples
------------------------------------

CCS Projects mentioned in the above table are built using pdkProjectCreate.bat/sh as explained in
`PDK Example and Test Project Creation <index_overview.html#pdk-example-and-test-project-creation>`__


Building MMCSD Test applications via makefiles
----------------------------------------------

- MMCSD Test applications and dependent libraries are built from the top level
  mmcsd makefile

- Refer to the `Processor SDK RTOS Getting Started Guide
  <index_overview.html#setup-environment>`__  for details of how to setup the
  build environment. Once you have setup the build environment, issue the
  following commands:

   - cd <pdk>/packages/

   - To build: make mmcsd

   - To clean: make mmcsd_clean

- Similarly, to build at the module level, issue the following commands for
  rebuilding:

   - cd <pdk>/packages/ti/drv/mmcsd

   - To build: make all

   - To clean: make clean


Additional References
---------------------

+-----------------------------------+--------------------------------------------+
| **Document**                      | **Location**                               |
+-----------------------------------+--------------------------------------------+
| API Reference Manual              | $(TI_PDK_INSTALL_DIR)\\packages\\ti        |
|                                   | \\drv\\mmcsd\\docs\\doxygen\\html\\inde    |
|                                   | x.html                                     |
+-----------------------------------+--------------------------------------------+
| Release Notes                     | $(TI_PDK_INSTALL_DIR)\\packages\\ti        |
|                                   | \\drv\\mmcsd\\docs\\ReleaseNotes_MMCS      |
|                                   | D_LLD.pdf                                  |
+-----------------------------------+--------------------------------------------+

|

