.. http://ap-fpdsp-swapps.dal.design.ti.com/index.php/Processor_SDK_RTOS_I2C_FIRMWARE

Introduction
============

| PRU-ICSS I2C serves as an example for firmware-based I2C peripheral
  support. The I2C firmware (I2C FW) allows additional I2C instances for SOCs
  beyond those supported by SOC hardware. The Processor SDK package includes
  full source code for I2C FW.

|

FIRMWARE FEATURES
=================

I2C FW supports the standard two pin I2C interface through three GPIO pins
from the PRU-ICSS module. The I2C SCL pin is implemented using a single
GPIO configured in GPO mode. The I2C SDA pin is implemented using two GPIO
pins: one pin configured in GPI mode for sampling SDA, and a second pin
configured in GPO mode for driving the SDA. Depending on the I2C clock
speed, I2C FW can emulate multiple I2C instances from a single PRU core.
Following are high-level I2C FW features:

+-----------------------------------+-----------------------------------+
| **Feature**                       | **Remarks**                       |
+-----------------------------------+-----------------------------------+
| No. of instances                  | 4 (Standard mode)                 |
|                                   |                                   |
|                                   | 1 (Fast mode)                     |
+-----------------------------------+-----------------------------------+
| SMBus support                     | Supported                         |
+-----------------------------------+-----------------------------------+
| Addressing modes                  | 7/10-bit                          |
+-----------------------------------+-----------------------------------+
| Controller mode                   | Supported                         |
+-----------------------------------+-----------------------------------+
| I2C data transfer rate from       | 100 kHz / 400 kHz                 |
| 100 kbps up to 400 kbps           |                                   |
+-----------------------------------+-----------------------------------+
| Bit format transfer               | 8 bit                             |
+-----------------------------------+-----------------------------------+
| Number of host interrupts         | 1                                 |
+-----------------------------------+-----------------------------------+
| Peripheral enable/disable         | Supported                         |
| capability                        |                                   |
+-----------------------------------+-----------------------------------+
| Start/Restart/Stop                | Supported                         |
+-----------------------------------+-----------------------------------+
| Built-in configurable FIFOs (8,   | 8/16/32/64/128/256                |
| 16, 32, 64 bytes) for buffered    |                                   |
| read/write                        |                                   |
+-----------------------------------+-----------------------------------+
| 8-bit-wide data access            | Supported                         |
+-----------------------------------+-----------------------------------+
| Target reset feature              | Supported                         |
+-----------------------------------+-----------------------------------+
| Internal loopback feature         | Supported                         |
+-----------------------------------+-----------------------------------+
| Target mode                       | Not Supported                     |
+-----------------------------------+-----------------------------------+
| Combined Controller-Target        | Not Supported                     |
| mode/transaction                  |                                   |
+-----------------------------------+-----------------------------------+
| DMA support                       | Not Supported                     |
+-----------------------------------+-----------------------------------+
| Programmable clock generation     | Not Supported                     |
+-----------------------------------+-----------------------------------+
| Implement Auto Idle mechanism     | Not Supported                     |
| (SOC specific feature)            |                                   |
+-----------------------------------+-----------------------------------+
| Implement Idle Request/Idle       | Not Supported                     |
| Acknowledge handshake mechanism   |                                   |
| (SOC specific feature)            |                                   |
+-----------------------------------+-----------------------------------+
| Support for asynchronous wakeup   | Not Supported                     |
| mechanism                         |                                   |
+-----------------------------------+-----------------------------------+

Firmware Organization
=====================

+-------------------------+--------------------------------------------------+
| **FW Item**             | **Directory**                                    |
+-------------------------+--------------------------------------------------+
| Source code             | <PDK>/packages/ti/drv/i2c/firmware/icss_i2c/src  |
+-------------------------+--------------------------------------------------+
| Design Guide            | <PDK>/packages/ti/drv/i2c/firmware/icss_i2c/docs |
+-------------------------+--------------------------------------------------+
| Firmware binaries       | <PDK>/packages/ti/drv/i2c/firmware/icss_i2c/bin  |
+-------------------------+--------------------------------------------------+

|

Firmware Build Instruction
==========================

Build instruction from Processor SDK Release package
----------------------------------------------------

.. rubric::  Pre-requisites to Building
   :name: pre-requisites-to-building

Refer to the Processor SDK RTOS Building page for information on setting up the build environment.

.. rubric::  Compiling I2C FIRMWARE
   :name: compiling-i2c-firmware

-  cd <PDK>/packages/ti/drv/i2c
-  make firm

Firmware binaries at the end of the build will be located at:

-  <PDK>/packages/ti/drv/i2c/firmware/<FIRMWARE_TYPE>/bin/<SOC>/<HOST_CORE>/<REVISION>

-  <FIRMWARE_TYPE> indicates the firmware type i.e. icss_i2c

-  <SOC> indicates the SOC type, e.g. am437x

-  <HOST_CORE> indicates the Host core type on which the built binary
   can be loaded, e.g. a9host

-  <REVISION> indicates the revision of the firmware binary based on
   core (there are 2 revision of PRU-ICSS core), e.g. REV1.

|

Build instruction for GIT
-------------------------

Following are the steps for building firmware from any external
environment outside Processor SDK RTOS package.

-  Creation of directories

   -  Create a working directory e.g. <WORK_DIR>
   -  Create a new directory named ti inside working directory. i.e.
      <WORK_DIR/ti>
   -  Create a new directory called drv inside ti. i.e.
      <WORK_DIR/ti/drv>

-  Clone of Repos

   -  Git clone pdk build repo into ti directory. i.e.
      <WORK_DIR/ti/build>
   -  Git clone i2c repo into ti/drv directory. i.e.
      <WORK_DIR/ti/drv/i2c>

-  Setting Environment Variables

   -  Export CLPRU install path. i.e. export CL_PRU_INSTALL_PATH=clpru
      toolchain directory
   -  Export pdk install path. i.e. export PDK_INSTALL_PATH=<WORK_DIR>
   -  Export LIMIT_SOCS Variable i.e. LIMIT_SOCS=<SOC> [Optional for
      limiting to some SOCs]

-  Build command

   -  Run make firm_clean/firm to clean/build firmware from i2c
      directory i.e. <WORK_DIR/ti/drv/i2c>

-  Generated binaries

   -  the firmware binaries which will be located in
      <WORK_DIR/ti/drv/i2c/firmware/<FIRMWARE_TYPE>/bin/<SOC>/<HOST_CORE>/<REVISION>>

|

Supported EVMs
==============

Supported EVMs and pin configurations for these EVMs are listed below.

+-------------+---------------------+-------------------+
| EVM Name    | PRU-ICSS Instances  | PRU-ICSS Revision |
+=============+=====================+===================+
| icev2AM335x | 1                   | REV1              |
+-------------+---------------------+-------------------+
| idkAM437x   | 2                   | REV1              |
+-------------+---------------------+-------------------+
| idkAM574x   | 2                   | REV2              |
+-------------+---------------------+-------------------+
| idkAM572x   | 2                   | REV2              |
+-------------+---------------------+-------------------+

|

.. rubric::  icev2AM335x
   :name: icev2am335x

+---------+-------+----------+--------------+---------------------+--------+-------+
| ICSS    | PRU   | Instance |Functional Pin|PRU GPIO Pins        |EVM Port|EVM Pin|
+=========+=======+==========+==============+=====================+========+=======+
|         |       |          | SCL          |pr1_pru0_pru_r30_1   | J3     | 14    |
|         |       |          +--------------+---------------------+--------+-------+
| ICSS1   | PRU0  | I2C0     |              |pr1_edio_data_out7   | J4     | 21    |
|         |       |          | SDA          +---------------------+--------+-------+
|         |       |          |              |pr1_pru0_pru_r31_0   | J3     | 12    |
+---------+-------+----------+--------------+---------------------+--------+-------+

.. rubric::  idkAM437x
   :name: idkAM437x

+---------+-------+----------+--------------+---------------------+--------+-------+
| ICSS    | PRU   | Instance |Functional Pin|PRU GPIO Pins        |EVM Port|EVM Pin|
+=========+=======+==========+==============+=====================+========+=======+
|         |       |          | SCL          |pr1_pru0_pru_r30_8   | J3     | 6     |
|         |       |          +--------------+---------------------+--------+-------+
|         |       | I2C0     |              |pr1_edio_data_out0   | J3     | 5     |
|         |       |          | SDA          +---------------------+--------+-------+
|         |       |          |              |pr1_pru0_pru_r31_9   | J3     | 8     |
| ICSS1   | PRU0  +----------+--------------+---------------------+--------+-------+
|         |       |          | SCL          |pr1_pru0_pru_r30_10  | J16    | 46    |
|         |       |          +--------------+---------------------+--------+-------+
|         |       | I2C1     |              |pr1_edio_data_out1   | J3     | 7     |
|         |       |          | SDA          +---------------------+--------+-------+
|         |       |          |              |pr1_pru0_pru_r31_11  | J16    | 48    |
+---------+-------+----------+--------------+---------------------+--------+-------+
|         |       |          | SCL          |pr0_pru0_pru_r30_8   | J16    | 56    |
|         |       |          +--------------+---------------------+--------+-------+
|         |       | I2C0     |              |pr1_edio_data_out0   | J3     | 5     |
|         |       |          | SDA          +---------------------+--------+-------+
|         |       |          |              |pr0_pru0_pru_r31_9   | J16    | 37    |
| ICSS0   | PRU0  +----------+--------------+---------------------+--------+-------+
|         |       |          | SCL          |pr0_pru0_pru_r30_10  | J16    | 38    |
|         |       |          +--------------+---------------------+--------+-------+
|         |       | I2C1     |              |pr1_edio_data_out1   | J3     | 7     |
|         |       |          | SDA          +---------------------+--------+-------+
|         |       |          |              |pr0_pru0_pru_r31_11  | J16    | 58    |
+---------+-------+----------+--------------+---------------------+--------+-------+

.. rubric::  idkAM572x/idkAM574x
   :name: idkAM572x-idkAM574x

+---------+-------+----------+--------------+---------------------+--------+-------+
| ICSS    | PRU   | Instance |Functional Pin|PRU GPIO Pins        |EVM Port|EVM Pin|
+=========+=======+==========+==============+=====================+========+=======+
|         |       |          | SCL          |pr1_pru1_gpo1        | J21    | 5     |
|         |       |          +--------------+---------------------+--------+-------+
| ICSS1   | PRU0  | I2C0     |              |pr1_edio_data_out1   | J46    | 4     |
|         |       |          | SDA          +---------------------+--------+-------+
|         |       |          |              |pr1_pru1_gpi0        | J21    | 3     |
+---------+-------+----------+--------------+---------------------+--------+-------+

|

I2C FIRMWARE Example
====================

Sample code for I2C transaction:

.. code-block:: c

    /* Refer to I2C FW Example for details */
    ...

    /* Initialize the I2C FW configuration */
    I2C_socInitFwCfg();

    /* Get the default I2C init configuration */
    I2C_socGetFwCfg(I2C_TEST_INSTANCE1, &i2c_cfg);

    /* Modify the default I2C configurations if necessary */

    /* Set the default I2C init configurations */
    I2C_socSetFwCfg(I2C_TEST_INSTANCE1, &i2c_cfg);
    ...

    Board_init(boardCfg);
    ...

    I2C_init();

    handle = I2C_open(I2C_TEST_INSTANCE1, &i2cParams);
    ...

    /* Initiate I2C transfers */
    I2C_transactionInit(&i2cTransaction);
    i2cTransaction.targetAddress = I2C_EEPROM_ADDR;
    ...

    status = I2C_transfer(handle, &i2cTransaction);
    if (status!= I2C_STS_SUCCESS) {
        /* I2C transaction failed */
    }

Sample code for SMBus transaction:

.. code-block:: c

    /* Refer to I2C FW Test for details */
    ...

    testCmd.transferCmd = SMBUS_WRITE_BYTE_CMD;
    testCmd.cmdCode = WRITE_SMBUS_COMMAND_CODE;
    controlStatus = I2C_control(handle, I2C_CMD_SMBUS_TYPE, ((void*)&testCmd));
    I2C_transactionInit(&i2cTransaction);
    ...

    status = I2C_transfer(handle, &i2cTransaction);
    if (status != I2C_STS_SUCCESS) {
        /* I2C transaction failed */
    }

|

.. rubric::  Examples List
   :name: examples-list

Refer to the Release Notes for details concerning I2C support across different EVMs.

+-----------------------+-----------------------+------------------------+
| Name                  | Description           | Expected Results       |
+=======================+=======================+========================+
| I2C_FwExample         | Driver Firmware       | Status messages will   |
|                       | example application   | be displayed on        |
|                       | for I2C FW instances  | console based based    |
|                       |                       | on pass/fail criteria: |
|                       |                       |                        |
|                       |                       | **Pass criteria:**     |
|                       |                       |                        |
|                       |                       | I2C Test: Instance:    |
|                       |                       | Baud Rate 100KHz:      |
|                       |                       |                        |
|                       |                       | All tests have         |
|                       |                       | passed.                |
+-----------------------+-----------------------+------------------------+

|

.. rubric::  Firmware Design Guide
   :name: firmware-design-guide

+-----------------------------------+--------------------------------------------------------------------------+
| **Document**                      | **Location**                                                             |
+-----------------------------------+--------------------------------------------------------------------------+
| I2C FIRMWARE Design Guide         | <PDK>/packages/ti/drv/i2c/firmware/icss_i2c/docs/I2C_FW_DESIGN_GUIDE.pdf |
+-----------------------------------+--------------------------------------------------------------------------+

**NOTE: For normal use of I2C FW, there is no need to refer to the design guide.
This document can be cosulted in case of interest in details of internal firmware
operation, or a desire to modify the firmware.**

|

