Introduction
------------

SPI driver enables communication for general SPI, MCSPI (Multichannel
SPI), QSPI (Quad SPI) and OSPI (Octal SPI) based peripherals on board
through common API to application.
MCSPI is a generic full-duplex interface supporting transmit and
receive of data over SPI bus. QSPI/OSPI is a variant of SPI supports four
receive data lanes. Driver supports configuration for either single,
dual, quad or octal data lines

Modes of Operation
------------------

Following modes of operations are supported:

**SPI_MODE_BLOCKING**
*SPI_transfer()* API blocks code execution until transaction has
completed. By default, SPI driver operates in blocking mode. This
ensures only one SPI transaction operates at a given time. This mode
is supported in both interrupt or non-interrupt configurations.

**SPI_MODE_CALLBACK**
*SPI_transfer()* API returns without waiting for completion of
transaction in this case. Callback function registered by application
is invoked once transaction is complete.This mode is supported only in
interrupt configuration.

Driver Configuration
--------------------

Board Specific Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All board specific configurations eg:enabling clock and pin-mux for SPI
pins are required before calling any driver APIs.By default Board_Init()
API supports all initialization sequence for TI supported EVMs. In
addition it initializes UART instance for Console/STDIO.Refer `Processor
SDK RTOS Board Support <index_board.html#board-support>`__
for additional details.Once board specific configuration is
complete \ *SPI_init()* API should be called to initialize driver.

SoC Specific Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

All SoC specific configurations (eg: SPI module registers base address,
interrupt configurations, etc.) can be set using SPI_socSetInitCfg() SoC
driver API before calling any SPI driver APIs. The default SoC specific
configurations can be retrieved using SPI_socGetInitCfg() SoC driver
API.

SPI Configuration Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The *SPI_soc.c* file binds driver with hardware attributes on the board
through *SPI_config[]* structure. This structure must be provided to the
SPI driver. It must be initialized before the *SPI_init()* function is
called and cannot be changed afterwards. For details about individual
fields of this structure, see Doxygen help by opening
*PDK_INSTALL_DIR\packages\ti\drv\spi\docs\doxygen\html\index.html.*

Driver  requires common *SPI_config[]*  to configure hardware attributes
of MCSPI and QSPI/OSPI peripherals on SOC and board. First all MCSPI related
hardware attributes is defined followed by QSPI/OSPI hardware attributes.
Application will need to include appropriate offset to instance while
invoking *SPI_open()* API..

APIs
----

API Reference for application:

::

    #include <ti/drv/spi/SPI.h>

SPI IP V1 driver also supports multi-channel API's:

::

    #include <ti/drv/spi/MCSPI.h>

Open SPI
^^^^^^^^

::

    ...
    Board_init(boardCfg);
    ...
    SPI_socGetInitCfg(peripheralNum, &spi_cfg);
    ...
    SPI_socSetInitCfg(peripheralNum, &spi_cfg);
    SPI_Params_init(&spiParams);
    spiParams.transferMode = SPI_MODE_BLOCKING;
    spiParams.transferCallbackFxn = NULL;
    handle = SPI_open(peripheralNum, &spiParams);

SPI IP V1 driver also supports multi-channel open API's:

::

    ...
    Board_init(boardCfg);
    ...
    MCSPI_Params_init(&spiParams);
    spiParams.transferMode = SPI_MODE_BLOCKING;
    spiParams.transferCallbackFxn = NULL;
    handle = MCSPI_open(peripheralNum, channel, &spiParams);

|
At this point SPI driver is ready for data transfer in blocking mode
on specific instance identified by handle. Pseudo/Sample code for
SPI read/write transaction is included below. Refer example for
additional details

::

    ...
    spiTransaction.count = n;    /* Transfer Length */
    spiTransaction. txBuf = transmitBuffer; /* Buffer to be written */
    spiTransaction.rxBuf = NULL;  /* Buffer holding the received data */
    transferOK = SPI_transfer(spi, &spiTransaction); /* Perform SPI transfer */
    if (!transferOK) {
    /* SPI transaction failed */
    }

SPI IP V1 driver also supports multi-channel transfer API's:

::

    ...
    spiTransaction.count = n;    /* Transfer Length */
    spiTransaction. txBuf = transmitBuffer; /* Buffer to be written */
    spiTransaction.rxBuf = NULL;  /* Buffer holding the received data */
    transferOK = MCSPI_transfer(spi, &spiTransaction); /* Perform SPI transfer */
    if (!transferOK) {
    /* SPI transaction failed */
    }

.. note::

  SPI_open API supports configuration of data word length in the
  SPI_Params. Currently IP V1 driver (for AM3/4/5 devices) supports
  8/16/32-bit word length, IP V0 driver (for Keystone devices) supports
  8/16-bit word length.

Examples
--------

SPI
^^^

+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
| Name                  | Description           | Expected Results      | SoC Supported       | Build Type          |
+=======================+=======================+=======================+=====================+=====================+
| SPI_FlashReadWrite    | Sample application    | Following prints on   |    k2g,             | CCS project         |
|                       | demonstrating read    | console expected:     |    k2hk,            |                     |
| Example application   | and write of data     | **Pass criteria:**    |    k2l,             |                     |
|                       | to a NOR flash        |                       |    k2e,             |                     |
|                       | device connected      | All tests have        |    c6657,           |                     |
|                       | over SPI interface.   | passed.               |    c6678,           |                     |
|                       | By default, write     |                       |    omapl137,        |                     |
|                       | test is disabled,     |                       |                     |                     |
|                       | user can enable       |                       |                     |                     |
|                       | write test by         |                       |                     |                     |
|                       | defining              |                       |                     |                     |
|                       | TEST_SPI_NOR_WRITE    |                       |                     |                     |
|                       | in                    |                       |                     |                     |
|                       | test/src/SPI_board.h  |                       |                     |                     |
|                       |                       |                       |                     |                     |
|                       | If write test is      |                       |                     |                     |
|                       | enabled, write        |                       |                     |                     |
|                       | transaction is        |                       |                     |                     |
|                       | verified              |                       |                     |                     |
|                       | for correctness by    |                       |                     |                     |
|                       | reading contents      |                       |                     |                     |
|                       | back.                 |                       |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
| SPI_TestApplication   |                       | Following prints on   |    am335x           | CCS project         |
|                       | Driver unit test      | console expected:     |    AM437x,          |                     |
|                       | application to        | **Pass criteria:**    |    AM571x,          |                     |
|                       | validate features     | All tests have        |    AM572x,          |                     |
|                       | and interfaces for    | passed.               |    AM574x,          |                     |
|                       | SPI driver            |                       |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
| spiLoopback example   |                       | Following prints on   |    k2g,             | CCS project         |
|                       | Example application   | console expected:     |    k2l,             |                     |
|                       | to validate           | **Pass criteria:**    |    k2e,             |                     |
|                       | features and          | All tests have        |    omapl138,        |                     |
|                       | interfaces for SPI    | passed.               |    AM335x,          |                     |
|                       | driver in loopback    |                       |    AM437x,          |                     |
|                       | mode. Configures      |                       |    AM571x,          |                     |
|                       | the SPI in loopback   |                       |    AM572x,          |                     |
|                       | mode, transmits a     |                       |    AM574x,          |                     |
|                       | test pattern and      |                       |                     |                     |
|                       | receives it back      |                       |                     |                     |
|                       | from SPI.             |                       |                     |                     |
|                       |                       |                       |                     |                     |
|                       |                       |                       |                     |                     |
|                       | Note: This example    |                       |                     |                     |
|                       | is intended to        |                       |                     |                     |
|                       | demonstrate the SPI   |                       |                     |                     |
|                       | LLD API usage on      |                       |                     |                     |
|                       | the HW platforms      |                       |                     |                     |
|                       | where SPI memory is   |                       |                     |                     |
|                       | not available.        |                       |                     |                     |
|                       | Currently this        |                       |                     |                     |
|                       | example is            |                       |                     |                     |
|                       | supported on          |                       |                     |                     |
|                       | OMAPL138/C6748        |                       |                     |                     |
|                       | platforms.            |                       |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+

|
QSPI
^^^^

+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
| Name                  | Description           | Expected Results      | SoC Supported       | Build Type          |
+=======================+=======================+=======================+=====================+=====================+
| QSPI_FlashReadWrite   | Sample application    | Following prints on   |    AM437x,          | CCS project         |
|                       | demonstrating read    | console expected:     |    AM571x,          |                     |
| Example application   | and write of data     | **Pass criteria:**    |    AM572x,          |                     |
|                       | to a flash device     |                       |    AM574x,          |                     |
|                       | connected over QSPI   | All tests have        |    k2g,             |                     |
|                       | interface. Write      | passed.               |                     |                     |
|                       | transaction is        |                       |                     |                     |
|                       | verified  for         |                       |                     |                     |
|                       | correctness by        |                       |                     |                     |
|                       | reading contents      |                       |                     |                     |
|                       | back.                 |                       |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
| QSPI_TestApplication  |                       | Following prints on   |    AM437x,          | CCS project         |
|                       | Driver unit test      | console expected:     |    AM571x,          |                     |
|                       | application to        | **Pass criteria:**    |    AM572x,          |                     |
|                       | validate features     | All tests have        |    AM574x,          |                     |
|                       | and interfaces for    | passed.               |    k2g,             |                     |
|                       | QSPI driver           |                       |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+

|
OSPI
^^^^

+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
| Name                  | Description           | Expected Results      | SoC Supported       | Build Type          |
+=======================+=======================+=======================+=====================+=====================+
| OSPI_TestApplication  |                       | Following prints on   |    am65xx           | makefile            |
|                       | Driver unit test      | console expected:     |    j721e            |                     |
|                       | application to        | **Pass criteria:**    |                     |                     |
|                       | validate features     | All tests have        |                     |                     |
|                       | and interfaces for    | passed.               |                     |                     |
|                       | OSPI driver           |                       |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+
| OSPI_SMP_Test         |                       | Following prints on   |    am65xx           | makefile            |
| Application           | Driver unit test      | console expected:     |    j721e            |                     |
|                       | application to        | **Pass criteria:**    |                     |                     |
|                       | validate features     | All tests have        |                     |                     |
|                       | and interfaces for    | passed.               |                     |                     |
|                       | OSPI driver in SMP    |                       |                     |                     |
|                       | mode. (A53 core)      |                       |                     |                     |
+-----------------------+-----------------------+-----------------------+---------------------+---------------------+

|

MCSPI
^^^^^

+-----------------+-----------------+-------------------------------------------+---------------------+----------------+-------------------+
| Name            | Description     | Additional EVM                            | Expected            | SoC Supported  | Build Type        |
|                 |                 | Configuration                             | Results             |                |                   |
+=================+=================+===========================================+=====================+================+===================+
| MCSPI_Serialize | Sample          | **AM57x IDK EVM:**                        | |                   |    AM335x,     | CCS project       |
| r               | Application     |                                           | | ** **             |    AM437x,     |                   |
| Example         | demonstrating   |                                           |                     |    AM571x,     |                   |
| application     | reading data    | Short pins 1  and 2 on header             | Following           |    AM572x,     |                   |
|                 | generated from  | J37(Industrial I/O)                       | prints  on          |    AM574x,     |                   |
|                 | industrial      |                                           | console             |                |                   |
|                 | input module.   | **AM335x ICE v2:**                        | expected:           |                |                   |
|                 | Application     | Short pins 1 and 2 on header              |                     |                |                   |
|                 | uses GPIO pins  | J14(Industrial I/O)                       | **Pass              |                |                   |
|                 | to assert load  |                                           | criteria:**         |                |                   |
|                 | signal in order | **AM437x IDK EVM:**                       |                     |                |                   |
|                 | to generate     | Short pins 1 and 2 on                     | All tests have      |                |                   |
|                 | date from       | header J1(Industrial I/O)                 | passed.             |                |                   |
|                 | industrial      |                                           |                     |                |                   |
|                 | input module.   |                                           |                     |                |                   |
+-----------------+-----------------+-------------------------------------------+---------------------+----------------+-------------------+
| MCSPI_Dma_Seria | Sample          | **AM57x IDK EVM:**                        | |                   |    AM437x,     | CCS project       |
| lizer           | Application     | Short pins 1 and 2 on header              | | ** **             |    AM571x,     |                   |
| Example         | demonstrating   | J37(Industrial I/O)                       |                     |    AM572x,     |                   |
| application     | reading data    | |                                         | Following           |    AM574x,     |                   |
|                 | generated from  | **AM437x IDK EVM:**                       | prints  on          |                |                   |
|                 | industrial      | Short pins 1 and 2 on header              | console             |                |                   |
|                 | input module    | J1(Industrial I/O)                        | expected:           |                |                   |
|                 | through EDMA.   |                                           |                     |                |                   |
|                 | Application     |                                           | **Pass              |                |                   |
|                 | uses GPIO pins  |                                           | criteria:**         |                |                   |
|                 | to assert load  |                                           |                     |                |                   |
|                 | signal in order |                                           | All tests have      |                |                   |
|                 | to generate     |                                           | passed.             |                |                   |
|                 | date from       |                                           |                     |                |                   |
|                 | industrial      |                                           |                     |                |                   |
|                 | input module.   |                                           |                     |                |                   |
+-----------------+-----------------+-------------------------------------------+---------------------+----------------+-------------------+
| MCSPI_SerialFla | Sample          | **AM335x GP EVM:**                        | |                   |    AM335x,     | CCS project       |
| sh              | Application     | Set the EVM in profile 2                  | | ** **             |                |                   |
|                 | demonstrating   | (SW8[1] = OFF,                            |                     |                |                   |
|                 | writing and     |  SW8[2] = ON,                             | Following           |                |                   |
|                 | reading data    |  SW8[3:4] = OFF)                          | prints  on          |                |                   |
|                 | from the serial |                                           | console             |                |                   |
|                 | flash through   |                                           | expected:           |                |                   |
|                 | MCSPI EDMA      |                                           |                     |                |                   |
|                 | interface.      |                                           | **Pass              |                |                   |
|                 |                 |                                           | criteria:**         |                |                   |
|                 |                 |                                           |                     |                |                   |
|                 |                 |                                           | All tests have      |                |                   |
|                 |                 |                                           | passed.             |                |                   |
+-----------------+-----------------+-------------------------------------------+---------------------+----------------+-------------------+
| MCSPI_periphera | Application     | **Pin Connections:**                      | | **On              |    AM335x,     | CCS project       |
| lmode example   | demonstrates    |                                           |   peripheral        |    AM437x,     |                   |
| application     | peripheral      |                                           |   EVM console:      |    AM571x,     |                   |
|                 | reciever and    | | **IDK AM571x,**                         |   **\ SPI           |    AM572x,     |                   |
|                 | transmit        | | **IDK AM572x or IDK AM574x:**           |    initialized      |    AM574x,     |                   |
|                 | features of     | | EVM1(controller) ==== EVM2(peripheral)  | | Peripheral:PASS:  |    k2g,        |                   |
|                 | McSPI.          | | J21-Pin24(CLK)---J21-Pin24(CLK)         |   Txd from          |                |                   |
|                 | Application use | | J21-Pin26(MISO)---J21-Pin28(MISO)       |   controller SPI    +----------------+-------------------+
|                 | case requires   | | J21-Pin28(MOSI)---J21-Pin26(MOSI)       |                     |    am65xx,     | makefile          |
|                 | two EVMs. One   | | J21-Pin30(CS)------J21-Pin30(CS)        |                     |    j721e       |                   |
|                 | acts as         | | J21-Pin22(DGND)--J21-Pin22(DGND)        | | **On Controller   |                |                   |
|                 | Controller      | |                                         |   EVM console:      |                |                   |
|                 | and Another as  | | **IDK AM437x:**                         |                     |                |                   |
|                 | peripheral.     | | EVM1(controller) ==== EVM2(peripheral)  |   initialized       |                |                   |
|                 | McSPI           | | J16-Pin24(CLK)-----J16-Pin24(CLK)       | | Controller: PASS: |                |                   |
|                 | connections     | | J16-Pin26(MISO)---J16-Pin28(MISO)       |   Txd from          |                |                   |
|                 | information and | | J16-Pin28(MOSI)---J16-Pin26(MOSI)       |   peripheral SPI    |                |                   |
|                 | addtional       | | J16-Pin30(CS)------J16-Pin30(CS)        | | Done              |                |                   |
|                 | details are as  | | J16-Pin22(DGND)--J16-Pin22(DGND)        |                     |                |                   |
|                 | follows.        | |                                         |                     |                |                   |
|                 |                 | | **ICEv2AM335x:**                        |                     |                |                   |
|                 | **No of Boards  | | EVM1(controller) ==== EVM2(peripheral)  |                     |                |                   |
|                 | Required**:     | | J3-Pin12(CLK)---------J3-Pin12(CLK)     |                     |                |                   |
|                 |                 | | J3-Pin14(MIS0)-------J3-Pin16(MISO)     |                     |                |                   |
|                 | 2               | | J3-Pin16(MOSI)-------J3-Pin14(MOSI)     |                     |                |                   |
|                 |                 | | J3-Pin18(CS)-----------J3-Pin18(CS)     |                     |                |                   |
|                 | **Connection    | | J3-Pin2(DGND)--------J3-Pin2(DGND)      |                     |                |                   |
|                 | requirements:** | |                                         |                     |                |                   |
|                 |                 | | **BBB AM335x:**                         |                     |                |                   |
|                 | | Consider EVM1 | | EVM1(controller) ==== EVM2(peripheral)  |                     |                |                   |
|                 |   as Controller | | P9-Pin31(CLK)-------P9-Pin31(CLK)       |                     |                |                   |
|                 |   and EVM2 as   | | P9-Pin29(MISO)------P9-Pin30(MISO)      |                     |                |                   |
|                 |   peripheral.   | | P9-Pin30(MOSI)------P9-Pin29(MOSI)      |                     |                |                   |
|                 | | ControllerSPI | | P9-Pin28(CS)---------P9-Pin28(CS)       |                     |                |                   |
|                 |   _CLK          | | P9-Pin1(DGND)-------P9-Pin1(DGND)       |                     |                |                   |
|                 |   --PeripheralS | |                                         |                     |                |                   |
|                 |   PI_CLK        | | **K2G EVM:**                            |                     |                |                   |
|                 | | ControllerSPI | | EVM1(controller) ==== EVM2(peripheral)  |                     |                |                   |
|                 |   _D0-          | | J12-Pin9(MISO)-------J12-Pin9(MISO)     |                     |                |                   |
|                 |   --PeripheralS | | J12-Pin11(MOSI)----J12-Pin11(MOSI)      |                     |                |                   |
|                 |   PI_D1         | | J12-Pin13(CLK)------J12-Pin13(CLK)      |                     |                |                   |
|                 | | ControllerSPI | | J12-Pin15(CS0)------J12-Pin15(CS0)      |                     |                |                   |
|                 |   _D1-          | | J12-Pin49(DGND)--J12-Pin49(DGND)        |                     |                |                   |
|                 |   ---Peripheral | |                                         |                     |                |                   |
|                 |   SPI_D0        | | **icev2AMIC110 EVM:**                   |                     |                |                   |
|                 | | ControllerSPI | | EVM1(controller) ==== EVM2(peripheral)  |                     |                |                   |
|                 |   _CS0          | | J5-Pin12(MISO)-------J5-Pin14(MISO)     |                     |                |                   |
|                 |   PeripheralSPI | | J5-Pin14(MOSI)------J5-Pin12(MOSI)      |                     |                |                   |
|                 |   _CS0          | | J4-Pin13(CLK)------J4-Pin13(CLK)        |                     |                |                   |
|                 | | DGND--------- | | J5-Pin4(CS)---------J5-Pin4(CS)         |                     |                |                   |
|                 |   -----------DG | | J5-Pin2(DGND)-------J5-Pin2(DGND)       |                     |                |                   |
|                 |   ND            | |                                         |                     |                |                   |
|                 |                 | | **am65xx EVM/IDK:**                     |                     |                |                   |
|                 | **Additional    | | MCU1_0 (controller) ===== MPU1_0        |                     |                |                   |
|                 | Requirements:** |   (peripheral)                            |                     |                |                   |
|                 |                 |                                           |                     |                |                   |
|                 | Run             | | **J721e EVM:**                          |                     |                |                   |
|                 | "MCSPI_Peripher | | MCU1_0 (controller) ====== MPU1_0       |                     |                |                   |
|                 | alMode_Peripher |   (peripheral)                            |                     |                |                   |
|                 | alExample_      |                                           |                     |                |                   |
|                 | <BoardType><arm |                                           |                     |                |                   |
|                 | /c66x/m4>Exampl |                                           |                     |                |                   |
|                 | eProject"       |                                           |                     |                |                   |
|                 | first on        |                                           |                     |                |                   |
|                 | Peripheral      |                                           |                     |                |                   |
|                 | EVM and then    |                                           |                     |                |                   |
|                 | "MCSPI_Peripher |                                           |                     |                |                   |
|                 | alMode          |                                           |                     |                |                   |
|                 | _ControllerExam |                                           |                     |                |                   |
|                 | ple             |                                           |                     |                |                   |
|                 | <BoardType>_<ar |                                           |                     |                |                   |
|                 | m/c66x/m4>Examp |                                           |                     |                |                   |
|                 | leProject"      |                                           |                     |                |                   |
|                 | on Controller   |                                           |                     |                |                   |
|                 | EVM.            |                                           |                     |                |                   |
|                 |                 |                                           |                     |                |                   |
|                 | |               |                                           |                     |                |                   |
|                 | | **Note:**     |                                           |                     |                |                   |
|                 |                 |                                           |                     |                |                   |
|                 | A DGND          |                                           |                     |                |                   |
|                 | connection may  |                                           |                     |                |                   |
|                 | be required     |                                           |                     |                |                   |
|                 | from expansion  |                                           |                     |                |                   |
|                 | connector on    |                                           |                     |                |                   |
|                 | each board to   |                                           |                     |                |                   |
|                 | make sure the   |                                           |                     |                |                   |
|                 | data transfer   |                                           |                     |                |                   |
|                 | is proper.      |                                           |                     |                |                   |
|                 |                 |                                           |                     |                |                   |
|                 | For AM6 or J7,  |                                           |                     |                |                   |
|                 | only one EVM is |                                           |                     |                |                   |
|                 | required.       |                                           |                     |                |                   |
|                 | Peripheral is   |                                           |                     |                |                   |
|                 | run on MPU1_0   |                                           |                     |                |                   |
|                 | core and Cont   |                                           |                     |                |                   |
|                 | roller is run   |                                           |                     |                |                   |
|                 | on MCU1_0 core  |                                           |                     |                |                   |
+-----------------+-----------------+-------------------------------------------+---------------------+----------------+-------------------+
| MCSPI_SMP_Basic | Sample          |                                           | |                   |    AM572x-EVM  | CCS project       |
| Example         | Application     |                                           | | ** **             |                |                   |
| application     | demonstrating   |                                           |                     |                |                   |
|                 | reading data    |                                           | Following           |                |                   |
|                 | generated from  |                                           | prints  on          |                |                   |
|                 | industrial      |                                           | console             |                |                   |
|                 | input module.   |                                           | expected:           |                |                   |
|                 | Application     |                                           |                     |                |                   |
|                 | uses GPIO pins  |                                           | **Pass              |                |                   |
|                 | to assert load  |                                           | criteria:**         |                |                   |
|                 | signal in order |                                           |                     |                |                   |
|                 | to generate     |                                           | All tests have      |                |                   |
|                 | date from       |                                           | passed.             |                |                   |
|                 | industrial      |                                           |                     |                |                   |
|                 | input module    |                                           |                     |                |                   |
|                 | in SMP mode.    |                                           |                     |                |                   |
|                 | (A15 core)      |                                           |                     |                |                   |
+-----------------+-----------------+-------------------------------------------+---------------------+----------------+-------------------+

Building SPI examples
----------------------

-  Makefile based examples and dependent libraries can be built from the top level or module level SPI makefile, refer to the `Processor SDK RTOS Getting Started Guide <index_overview.html#setup-environment>`__  for details of how to setup the build environment. Once you have setup the build environment, issue the following commands:
::

   To build and clean libs/apps from top-level makefile:
   cd <pdk>/packages
   make spi
   make spi_clean

   To build and clean libs/apps from module-level makefile:
   cd <pdk>/packages/ti/drv/spi
   make all
   make clean


-  RTSC CCS project based examples are built from CCS
::

   cd <pdk>/packages
   ./pdkProjectCreate.sh [soc] [board] [endian] spi [project type] [processor] [SECUREMODE=<yes/no>]
   Import and build CCS Project from  <pdk>/packages/MyExampleProjects/

OSPI Driver Configuration to support QSPI flash
-----------------------------------------------

If the board has a QSPI flash, the PDK driver needs to be updated to support the QSPI flash:

-  Board QSPI Flash Instance Configuration in board_cfg.h
::

    #define BOARD_QSPI_NOR_INSTANCE  <OSPI instance connected to QSPI flash>

-  SPI SoC Driver Configurations:
::

    ...
    OSPI_v0_HwAttrs ospi_cfg;

    SPI_init();

    OSPI_socGetInitCfg(BOARD_QSPI_NOR_INSTANCE, &ospi_cfg);
    ospi_cfg.xferLines      = OSPI_XFER_LINES_QUAD;
    ospi_cfg.pageSize       = <QSPI flash page size>;
    ospi_cfg.devDelays[0]   = <QSPI device delay>;
    ospi_cfg.devDelays[1]   = <QSPI device delay>;
    ospi_cfg.devDelays[2]   = <QSPI device delay>;
    ospi_cfg.devDelays[3]   = <QSPI device delay>;
    ospi_cfg.rdDataCapDelay = <QSPI read capture delay>;
    OSPI_socSetInitCfg(BOARD_OSPI_NOR_INSTANCE, &ospi_cfg);

Support for Benchmark Testing
------------------------------

+-----------------------+-----------------------+-----------------------------------------+-----------------------+-----------------------+
| Name                  | Description           | Expected Results                        | SOC/Core Suppported   | Build Type            |
+=======================+=======================+=========================================+=======================+=======================+
| OSPI flash Test App   | Test application used | Test application                        |  am65xx/A53           | make                  |
|                       | for performance       | will print on the UART console:         |  am65xx/R5            |                       |
|                       | benchmarking          |                                         |  j721e/mpu1_0         |                       |
|                       |                       | Board_flashWrite ### bytes at transfer  |  j721e/mcu1_0         |                       |
|                       |                       | rate #### Kbps                          |                       |                       |
|                       |                       |                                         |                       |                       |
|                       |                       | Board_flashRead ### bytes at transfer   |                       |                       |
|                       |                       | rate #### Mbps                          |                       |                       |
|                       |                       |                                         |                       |                       |
|                       |                       | Board_flashWrite CPU Load %##           |                       |                       |
|                       |                       |                                         |                       |                       |
|                       |                       | Board_flashRead CPU Load %##            |                       |                       |
+-----------------------+-----------------------+-----------------------------------------+-----------------------+-----------------------+

.. note::

  1. Data transfer between DDR and OSPI flash memory, performance measurement does not include time to invalidate/write back cache
  2. GTC counter (200MHz) used for throughput measurement on A53, and PMU cycle counter (400MHz) on R5
  3. sysbios load moduel used for load measurement
  4. Pipeline PHY enabled, DDR mode enabled in DAC mode
  5. Pipeline PHY disabled, DDR mode disabled in INDAC mode with ospi clock divider of 32
  6. Read/write transfer size of 1M bytes
  7. Write transfer size 1M bytes with DMA chunk size of 16 bytes in DAC DMA mode

|
Additional References
---------------------

+-----------------------------------+-----------------------------------+
| **Document**                      | **Location**                      |
+-----------------------------------+-----------------------------------+
| API Reference Manual              | $(TI_PDK_INSTALL_DIR)\packages\ti |
|                                   | \drv\spi\docs\doxygen\html\index. |
|                                   | html                              |
+-----------------------------------+-----------------------------------+
| Release Notes                     | $(TI_PDK_INSTALL_DIR)\packages\ti |
|                                   | \drv\spi\docs\ReleaseNotes_SPI_LL |
|              git                  | D.pdf                             |
+-----------------------------------+-----------------------------------+

|

