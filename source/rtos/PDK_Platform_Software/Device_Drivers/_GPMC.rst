.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_GPMC

Overview
--------

Introduction
^^^^^^^^^^^^

The general-purpose memory controller (GPMC) is an unified memory
controller dedicated to interfacing external memory devices:

-  Asynchronous SRAM-like memories and application-specific integrated
   circuit (ASIC) devices
-  Asynchronous, synchronous, and page mode (only available in
   non-multiplexed mode) burst NOR flash devices
-  NAND Flash

Driver supports two types of transfers with data path to external memory
device configured to be 16- or 8-bit:

-  Read
-  Write

| In addition driver supports following modes of operation:

-  **GPMC_MODE_BLOCKING:** By default, driver operates in blocking mode.
   In blocking mode, a Task’s code execution is blocked until
   transaction is complete. This ensures only one transaction operates
   at a given time. Driver supports both interrupt or non-interrupt
   based blocking modes.
-  **GPMC_MODE_CALLBACK** In callback mode, an GPMC transaction
   functions asynchronously, which means that it does not block a Task’s
   code execution. After an GPMC transaction is complete, GPMC driver
   calls a user-provided hook function. Only interrupt based callback is
   supported.

In NAND flash mode, driver supports following ECC algorithms:

-  BCH code 8-bit
-  HAMMING code 1-bit

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

.. rubric:: **Board Specific Configuration**
   :name: board-specific-configuration

All the board specific configurations eg:enabling and pin-mux of GPMC
pins should be performed before calling any driver APIs.By default
Board_Init() API supports all initialization sequence for TI supported
EVMs.Refer `Processor SDK RTOS Board Support <index_board.html#board-support>`__
for additional details.

Once the board specific configuration is complete driver API GPMC_init()
can be called to initialize driver

.. rubric:: **GPMC Configuration Structure**
   :name: gpmc-configuration-structure

GPMC_soc.c file binds driver with hardware attributes on the board
through GPMC_config structure. This structure must be provided to GPMC
driver. It must be initialized before the GPMC_init() function is called
and cannot be changed afterwards. For details about the individual
fields of this structure, see the Doxygen help by opening
PDK_INSTALL_DIR\\packages\\ti\\drv\\gpmc\\docs\\doxygen\\html\\index.html.

APIs
^^^^^

API reference for application:

::

    #include <ti/drv/gpmc/GPMC.h>

 Sample code for initiating GPMC transaction:

.. code-block:: c

    ...
    Board_init(boardCfg);
    ...
    ...
    gpmc = GPMC_open(peripheralNum, &gpmcParams);
    ...
    ...

    /* Initiate GPMC transfers. Refer Example for details
    */
    transferOK = GPMC_transfer(gpmc, &gpmcTransaction);
    if (!transferOK) {
    /* GPMC transaction failed */
    }

Application
------------

Examples
^^^^^^^^

Refer Release Note for GPMC support across different EVMs

+-----------------------+-----------------------+-----------------------+
| Name                  | | Description         | Expected Results      |
+=======================+=======================+=======================+
| GPMC NOR/NAND Read    | | Simple example to   | Following prints will |
| Example Application   |   read data from GPMC | come on console based |
|                       |   NOR/NAND flash on   | on pass/fail          |
|                       |   board.              | criteria:             |
|                       |                       |                       |
|                       |                       | **Pass criteria:**    |
|                       |                       |                       |
|                       |                       | GPMC flash device ID: |
|                       |                       | 0x##, manufacturer    |
|                       |                       | ID: 0x##              |
|                       |                       |                       |
|                       |                       | GPMC flash read test  |
|                       |                       | passed.               |
|                       |                       |                       |
|                       |                       | All tests have        |
|                       |                       | passed.               |
+-----------------------+-----------------------+-----------------------+
| GPMC NOR/NAND test    | | Driver Unit Test    | Following prints will |
| application           |   application to test | come on console based |
|                       |   GPMC NOR/NAND flash | on pass/fail          |
|                       |   read/erase/write    | criteria:             |
|                       |                       |                       |
|                       |                       | **Pass criteria:**    |
|                       |                       |                       |
|                       |                       | GPMC flash device ID: |
|                       |                       | 0x##, manufacturer    |
|                       |                       | ID: 0x##              |
|                       |                       |                       |
|                       |                       | GPMC flash block      |
|                       |                       | erase test passed.    |
|                       |                       |                       |
|                       |                       | GPMC flash write test |
|                       |                       | passed.               |
|                       |                       |                       |
|                       |                       | GPMC flash read test  |
|                       |                       | passed.               |
|                       |                       |                       |
|                       |                       | All tests have        |
|                       |                       | passed.               |
+-----------------------+-----------------------+-----------------------+
|                       |                       |                       |
+-----------------------+-----------------------+-----------------------+

.. note::

   1. GPMC Test Application supports write test, by default write test is
      disabled, user can enable the write test by defining
      TEST_GPMC_FLASH_WRITE in test/src/GPMC_board.h.

   2. In GPMC_Test_icev2AM335x, J5 pin2 & 3 should be shorted on
      iceV2AM335x board in order to test GPMC NOR flash.

   3. In GPMC_Test_evmAM437x, J2 pin1 & 2 should NOT be shorted on
   evmAM437x board in order to test GPMC NAND flash.

Additional References
---------------------

+-----------------------------------+-----------------------------------------+
| **Document**                      | **Location**                            |
+-----------------------------------+-----------------------------------------+
| API Reference Manual              | $(TI_PDK_INSTALL_DIR)\\packages\\ti     |
|                                   | \\drv\\gpmc\\docs\\doxygen\\html\\index |
|                                   | .html                                   |
+-----------------------------------+-----------------------------------------+
| Release Notes                     | $(TI_PDK_INSTALL_DIR)\\packages\\ti     |
|                                   | \\drv\\gpmc\\docs\\ReleaseNotes_GPMC_   |
|                                   | LLD.pdf                                 |
+-----------------------------------+-----------------------------------------+

|

