.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_I2C

Overview
--------

Introduction
^^^^^^^^^^^^

I2C module provides an interface to any I2C-bus-compatible device
accessible via I2C serial bus. External components attached to I2C bus
can serially transmit/receive data to/from the CPU through two-wire
interface. Driver supports three types of transfers in both I2C controller
mode and target mode

-  Read
-  Write
-  Write followed by read

In addition driver supports following modes of operation:

-  **I2C_MODE_BLOCKING:** By default, driver operates in blocking mode.
   In blocking mode, a Task’s code execution is blocked until
   transaction is complete. This ensures only one transaction operates
   at a given time. Driver supports both interrupt or non-interrupt
   based blocking modes.
-  **I2C_MODE_CALLBACK** In callback mode, an I2C transaction functions
   asynchronously, which means that it does not block a Task’s code
   execution. After an I2C transaction is complete, I2C driver calls a
   user-provided hook function. Only interrupt based callback is
   supported.

.. note::

   If I2C peripheral is in reset during a transfer, it can cause the I2C
   bus to hang. I2C V0 IP (Keystone SoCs) does not have hardware support to
   recover the I2C bus from hanging, user needs to power cycle the board as
   a workaround. For I2C V1 IP (AM3/4/5 SoCs), the application can call
   I2C_control() API and use I2C_CMD_RECOVER_BUS to recover the I2C bus.


.. rubric::  Firmware
   :name: firmware

TI PRU-ICSS cores (Programmable Real-Time Unit Industrial Communication
Subsystem) is firmware programmable and can take on various
personalities. Processor SDK package includes I2C Firmware support.
Refer `I2C FW <index_pru_icss_fw.html#pru-icss-i2c>`__ for
additional details.

|

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

.. rubric::  **Board Specific Configuration**
   :name: board-specific-configuration

All the board specific configurations eg:enabling and pin-mux of I2C
pins should be performed before calling any driver APIs.By default
Board_Init() API supports all initialization sequence for TI supported
EVMs.Refer `Processor SDK RTOS Board
Support <index_board.html#board-support>`__ for additional
details.

Once the board specific configuration is complete driver API I2C_init()
can be called to initialize driver

.. rubric::  **I2C Configuration Structure**
   :name: i2c-configuration-structure

I2C_soc.c file binds driver with hardware attributes on the board
through I2C_config structure. This structure must be provided to I2C
driver. It must be initialized before the I2C_init() function is called
and cannot be changed afterwards. For details about the individual
fields of this structure, see the Doxygen help by opening
PDK_INSTALL_DIR\\packages\\ti\\drv\\i2c\\docs\\doxygen\\html\\index.html.

APIs
^^^^^

API reference for application:

::

    #include <ti/drv/i2c/I2C.h>

 Sample code for initiating I2C transaction:

::

    ...
    Board_init(boardCfg);
    ...
    I2C_socGetInitCfg(peripheralNum, &i2c_cfg);
    ...
    I2C_socSetInitCfg(peripheralNum, &i2c_cfg);
    ...
    i2c = I2C_open(peripheralNum, &i2cParams);
    ...
    ...

    /* Initiate I2C transfers. Refer Example for details
    */
    I2C_transactionInit(&i2cTransaction);
    transaction.controllerMode   = true;
    ...
    ...
    transferOK = I2C_transfer(i2c, &i2cTransaction);
    if (transferOK != I2C_STS_SUCCESS) {
    /* I2C transaction failed */
    }

Application
------------

Examples
^^^^^^^^

Refer Release Note for I2C support across different EVMs

+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
|| Name                 || Description          ||  Expected Results    | SoC Supported       | Build Type          |
+=======================+=======================+=======================+=====================+=====================+
| I2C_EepromRead        || Simple example to    || Following prints will|    AM335x,          | CCS project         |
| Example application   | read fixed number     |  come on console based|    AM437x,          |                     |
|                       | of bytes from         |  on pass/fail         |    AM571x,          |                     |
|                       | EEPROM on board and   |  criteria:            |    AM572x,          |                     |
|                       | compares it with      ||                      |    AM574x,          |                     |
|                       | expected data.        || **Pass criteria:**   |    k2g,             |                     |
|                       |                       ||                      |    k2hk,k2l,k2e,k2l |                     |
|                       |                       || EEPROM data matched  |    c6657,c6678      |                     |
|                       |                       |   All tests have      |    omapl137,        |                     |
|                       |                       |   passed.             |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
| I2C_TestApplication   || Driver Unit Test     || Following prints will|    AM335x,          | CCS project         |
|                       | application for       |  come on console based|    AM437x,          |                     |
|                       | additional I2C        |  on pass/fail         |    AM571x,          |                     |
|                       | speed and other tests |  criteria:            |    AM572x,          |                     |
|                       |                       ||                      |    AM574x,          |                     |
|                       |                       || **Pass criteria:**   |    k2g,             |                     |
|                       |                       ||                      |    k2hk,            |                     |
|                       |                       || I2C Test: 100Kbps:   |    k2l,             |                     |
|                       |                       |  PASS                 |    k2e,             |                     |
|                       |                       ||                      |    c6657,           |                     |
|                       |                       || I2C Test: 400Kbps:   |    c6678,           |                     |
|                       |                       |  PASS                 |    omapl137,        |                     |
|                       |                       ||                      |                     |                     |
|                       |                       || I2C Test: timeout    +---------------------+---------------------+
|                       |                       |  test passed          |    am65xx           | makefile            |
|                       |                       ||                      |    j721e            |                     |
|                       |                       || All tests have       |                     |                     |
|                       |                       |  passed.              |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
| I2C_SMP_Test          || Driver Unit Test     || Following prints will|   am572x-evm        | CCS project         |
| Application           | application for       |  come on console based|                     |                     |
|                       | additional I2C        |  on pass/fail         |                     |                     |
|                       | speed and other tests |  criteria:            |                     |                     |
|                       | with SMP enabled.     ||                      |                     |                     |
|                       | (A15 and A53 cores)   || **Pass criteria:**   |                     |                     |
|                       |                       ||                      |                     |                     |
|                       |                       || I2C Test: 100Kbps:   |                     |                     |
|                       |                       |  PASS                 |                     |                     |
|                       |                       ||                      |                     |                     |
|                       |                       || I2C Test: 400Kbps:   |                     |                     |
|                       |                       |  PASS                 |                     |                     |
|                       |                       ||                      |                     |                     |
|                       |                       || I2C Test: timeout    +---------------------+---------------------+
|                       |                       |  test passed          |    am65xx           | makefile            |
|                       |                       ||                      |    j721e            |                     |
|                       |                       || All tests have       |                     |                     |
|                       |                       |  passed.              |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
| I2C_TemperatureSensor || Example to get the   || Following prints will|    AM572x,          | CCS project         |
|                       | temperature value     |  come on console based|                     |                     |
|                       | from the temperature  |  on pass/fail         |                     |                     |
|                       | sensor and displays   |  criteria:            |                     |                     |
|                       | on the serial         ||                      |                     |                     |
|                       | console.              || **Pass criteria:**   |                     |                     |
|                       |                       ||                      |                     |                     |
|                       |                       || Temperature =        |                     |                     |
|                       |                       |  "value in            |                     |                     |
|                       |                       |  centigrades" C       |                     |                     |
|                       |                       |  All tests have       |                     |                     |
|                       |                       |  passed.              |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
| I2C_controller/target || Application          || Following prints will|    AM572x,          | CCS project         |
|                       | demonstrates          |  come on console based|    AM574x,          |                     |
|                       | controller/target     |  on pass/fail         |    k2g,             |                     |
|                       | transfer of I2C.      |  criteria:            |    omapl138,        |                     |
|                       | Application use       ||                      |                     |                     |
|                       | case requires two     || **Pass criteria:**   |                     |                     |
|                       | EVMs. One acts as     ||                      |                     |                     |
|                       | Controller and the    || All tests have       |                     |                     |
|                       | other as target. I2C  | passed.               |                     |                     |
|                       | connections           |                       |                     |                     |
|                       | information and       |                       |                     |                     |
|                       | addtional details     |                       |                     |                     |
|                       | are as follows:       |                       |                     |                     |
|                       ||                      |                       |                     |                     |
|                       || AM57xx boards I2C bus|                       |                     |                     |
|                       | connection on J9      |                       |                     |                     |
|                       | (controller board <-->|                       |                     |                     |
|                       | target board)         |                       |                     |                     |
|                       ||                      |                       |                     |                     |
|                       || pin22 (SCL)<-->      |                       |                     |                     |
|                       | pin22 (SCL)           |                       |                     |                     |
|                       ||                      |                       |                     |                     |
|                       || pin24 (SDA)<--> pin24|                       |                     |                     |
|                       | (SDA)                 |                       |                     |                     |
|                       ||                      |                       |                     |                     |
|                       || pin21 (GND)<--> pin21|                       |                     |                     |
|                       | (GND)                 |                       |                     |                     |
|                       ||                      |                       |                     |                     |
|                       || K2G boards I2C bus   |                       |                     |                     |
|                       | connection on J12     |                       |                     |                     |
|                       | (controller board <-->|                       |                     |                     |
|                       | target board)         |                       |                     |                     |
|                       | pin28 (SCL)<-->       |                       |                     |                     |
|                       | pin28 (SCL)           |                       |                     |                     |
|                       | pin30 (SDA)<-->       |                       |                     |                     |
|                       | pin30 (SDA)           |                       |                     |                     |
|                       | pin50 (GND)<-->       |                       |                     |                     |
|                       | pin50 (GND)           |                       |                     |                     |
|                       ||                      |                       |                     |                     |
|                       |                       |                       |                     |                     |
|                       || OMAPL138/C6748       |                       |                     |                     |
|                       | boards I2C bus        |                       |                     |                     |
|                       | connection on J15     |                       |                     |                     |
|                       | (controller board <-->|                       |                     |                     |
|                       | target board)         |                       |                     |                     |
|                       | pin13 (SCL)<-->       |                       |                     |                     |
|                       | pin13 (SCL)           |                       |                     |                     |
|                       | pin15 (SDA)<-->       |                       |                     |                     |
|                       | pin15 (SDA)           |                       |                     |                     |
|                       | pin35 (GND)<-->       |                       |                     |                     |
|                       | pin35 (GND)           |                       |                     |                     |
|                       ||                      |                       |                     |                     |
|                       || Run                  |                       |                     |                     |
|                       | "I2C_Target_<BoardTy  |                       |                     |                     |
|                       | pe>_<arm/c66x/m4>Test |                       |                     |                     |
|                       | Project"              |                       |                     |                     |
|                       | first on Target EVM   |                       |                     |                     |
|                       | and then              |                       |                     |                     |
|                       | "I2C_Controller_<Boar |                       |                     |                     |
|                       | dType>_<arm/c66x/m4>  |                       |                     |                     |
|                       | TestProject"          |                       |                     |                     |
|                       | on Controller EVM.    |                       |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+

.. note::

   I2C_Test Application supports write test on Keystone II EVMs, by default
   write test is disabled, user can enable the write test by defining
   I2C_EEPROM_WRITE_ENABLE in test/eeprom_read/src/I2C_board.h.
   I2C_TemperatureSensor Application is supported only on AM572x GP EVM.

Building I2C examples
----------------------

-  Makefile based examples and dependent libraries can be built from the top level or module level I2C makefile, refer to the `Processor SDK RTOS Getting Started Guide <index_overview.html#setup-environment>`__  for details of how to setup the build environment. Once you have setup the build environment, issue the following commands:
::

   To build and clean libs/apps from top-level makefile:
   cd <pdk>/packages
   make i2c
   make i2c_clean

   To build and clean libs/apps from module-level makefile:
   cd <pdk>/packages/ti/drv/i2c
   make all
   make clean


-  RTSC CCS project based examples are built from CCS
::

   cd <pdk>/packages
   ./pdkProjectCreate.sh [soc] [board] [endian] i2c [project type] [processor] [SECUREMODE=<yes/no>]
   Import and build CCS Project from  <pdk>/packages/MyExampleProjects/


Additional References
---------------------

+-----------------------+------------------------------------------+
| **Document**          |  **Location**                            |
+-----------------------+------------------------------------------+
| API Reference Manual  | $(TI_PDK_INSTALL_DIR)\\packages\\ti      |
|                       | \\drv\\i2c\\docs\\doxygen\\html\\index.  |
|                       | html                                     |
+-----------------------+------------------------------------------+
| Release Notes         | $(TI_PDK_INSTALL_DIR)\\packages\\ti      |
|                       | \\drv\\i2c\\docs\\ReleaseNotes_I2C_LL    |
|                       | D.pdf                                    |
+-----------------------+------------------------------------------+

|
