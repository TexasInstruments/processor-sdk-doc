Overview
--------

Introduction
^^^^^^^^^^^^

This tool demonstrates how to configure and use the Serdes Diag APIs
on KeyStone 3 device family. The DIAG APIs currently support R5F arch.
There are 2 tests included in the package:

-  Serdes Diag BER Test
-  Serdes Diag EYE Test

-  **Serdes Diag BER Test:** The example finds out the optimal TX coefficients
   (CM, C1, C2) by performing Bit Error Rate (BER) sweeps on the Serdes where the
   EVM sends the transmit pattern (for example PRBS 31) and the EVM also detects
   the receive sequence and performs BER calculations across the desired serdes
   using the CPU. The sweep results are printed into a text file.
-  **Serdes Diag EYE Test** The example performs on chip eye measurement
   allowing the user to see the eye opening of the receive data after
   equalization. The EVM sends the transmit pattern (for example PRBS 31) and
   detects the sequence and performs EYE measurements across the desired serdes
   using the CPU. The results are printed into a text file.

.. note::

   Currently only internal loopback is supported on the EVM.

|

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

.. rubric::  **Serdes Diag Configuration Structure**
   :name: serdes_diag-configuration-structure

serdes_diag_test_main.c contains the main function. It initializes all the
serdes peripherals using the serdes_diag_test_init( ) API. The
serdes_diag_test_phy_type should be specified in serdes_diag_platform.h
in order to run the BER/EYE test for that specific SERDES.

APIs
^^^^^

API reference for application:

::

    #include <ti/diag/serdes_diag/src/am65xx/serdes_diag_k3.h>

 Sample code for initiating Serdes Diag transaction:

::

    ...
    /* Initiatize the serdes using serdes_diag_platform.h
    */
    serdes_diag_test_init();
    ...
    /* BER Test Initialization Parameters can be edited
    inside this API */
    Serdes_Example_BERTest();
    OR
    /* On Die Scope/Eye Scan Test Initialization Parameters
    can be edited inside this API */
    Serdes_Example_EYETest();
    ...
    ...



Application
------------

Examples
^^^^^^^^

Refer Release Note for Serdes Diag support across different EVMs

+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
|| Name                 || Description          ||  Expected Results    | SoC Supported       | Build Type          |
+=======================+=======================+=======================+=====================+=====================+
| serdes_diag_BER_app   || BER example          || Following prints will|    am65xx           | makefile            |
|                       |                       |  come on console based|                     |                     |
|                       |                       |  on pass/fail         |                     |                     |
|                       |                       |  criteria:            |                     |                     |
|                       |                       ||                      |                     |                     |
|                       |                       || **Pass criteria:**   |                     |                     |
|                       |                       ||                      |                     |                     |
|                       |                       || The sweep results are|                     |                     |
|                       |                       |  printed into a text  |                     |                     |
|                       |                       |  file                 |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
| serdes_diag_EYE_app   || EYE example          || Following prints will|    am65xx           | makefile            |
|                       |                       |  come on console based|                     |                     |
|                       |                       |  on pass/fail         |                     |                     |
|                       |                       |  criteria:            |                     |                     |
|                       |                       ||                      |                     |                     |
|                       |                       || **Pass criteria:**   |                     |                     |
|                       |                       ||                      |                     |                     |
|                       |                       || I2C Test: 100Kbps:   |                     |                     |
|                       |                       |  PASS                 |                     |                     |
|                       |                       ||                      |                     |                     |
|                       |                       || I2C Test: 400Kbps:   |                     |                     |
|                       |                       |  PASS                 |                     |                     |
|                       |                       ||                      |                     |                     |
|                       |                       || I2C Test: timeout    |                     |                     |
|                       |                       |  test passed          |                     |                     |
|                       |                       ||                      |                     |                     |
|                       |                       || All tests have       |                     |                     |
|                       |                       |  passed.              |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+

.. note::

   Currently only R5F platform is supported with the above examples.

Building Serdes Diag examples
----------------------

-  Makefile based examples and dependent libraries can be built from the top level or module level Serdes Diag makefile, refer to the `Processor SDK RTOS Getting Started Guide <index_overview.html#setup-environment>`__  for details of how to setup the build environment. Once you have setup the build environment, issue the following commands:
::

   To build and clean libs/apps from top-level makefile:
   cd <pdk>/packages
   make serdes_diag
   make serdes_diag_clean

   To build and clean libs/apps from module-level makefile:
   cd <pdk>/packages/ti/diag/serdes_diag
   make all
   make clean


-  CCS project based examples are built from CCS
::

   cd <pdk>/packages
   ./pdkProjectCreate.sh [soc] [board] [endian] serdes_diag [project type] [processor] [SECUREMODE=<yes/no>]
   Import and build CCS Project from  <pdk>/packages/MyExampleProjects/


Additional References
---------------------

+-----------------------+------------------------------------------+
| **Document**          |  **Location**                            |
+-----------------------+------------------------------------------+
| API Reference Manual  | $(TI_PDK_INSTALL_DIR)\\packages\\ti      |
|                       | \\diag\\serdes_diag\\docs\\doxygen\\html |
|                       | \\index.html                             |
+-----------------------+------------------------------------------+
| Release Notes         | $(TI_PDK_INSTALL_DIR)\\packages\\ti      |
|                       | \\diag\\serdes_diag\\docs\\Serdes_Diag_  |
|                       | Release_Notes.pdf                        |
+-----------------------+------------------------------------------+

|
