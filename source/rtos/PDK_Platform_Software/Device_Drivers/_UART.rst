.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_UART

Overview
--------

Introduction
^^^^^^^^^^^^

Driver enables UART's available on SOC for reading and writing to any
peripherals on board. Additionally it supports simple APIs for
Console/STDIO operations.

.. rubric:: Modes of Operation
   :name: modes-of-operation

Following modes of operations are supported

**UART_MODE_BLOCKING**: In this mode, read and write APIs, blocks on
semaphore until required operation is complete. By default, UART driver
operates in blocking mode. In this mode, code execution of a task blocks
until UART transaction is complete. While transaction is in progress
additional tasks pending requests will remain in blocked state waiting
for semaphore.

**UART_MODE_CALLBACK**: In this mode, read and write operation returns
immediately. On trigger of hardware Interrupt (hwi) callback function
gets triggered.

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

.. rubric:: **Board Specific Configuration**
   :name: board-specific-configuration

All board specific configurations eg:enabling clock and pin-mux for UART
pins are required before calling any driver APIs.By default Board_Init()
API supports all initialization sequence for TI supported EVMs. In
addition it initializes UART instance for Console/STDIO.Refer `Processor
SDK RTOS Board Support <index_board.html#board-support>`__
for additional details.Once board specific configuration is complete
UART_init() API can be called to initialize driver.

.. rubric:: **UART Configuration Structure**
   :name: uart-configuration-structure

The UART_soc.c file binds driver with hardware attributes on the board
through UART_config structure. This structure must be provided to UART
driver. It must be initialized before the UART_init() function is called
and cannot be changed afterwards. For details about individual fields of
this structure, see the Doxygen help by opening
PDK_INSTALL_DIR\packages\ti\drv\uart\docs\doxygen\html\index.html.

APIs
^^^^

API reference for application:

::

    #include <ti/drv/uart/UART.h>

STDIO API reference for application:

::

    #include <ti/drv/uart/UART_stdio.h>

.. rubric:: Open UART
   :name: open-uart

There are three ways to open a UART instance:

1. UART_open()

::

    ...
    Board_init(boardCfg);
    ...
    UART_socGetInitCfg(UART_INSTANCE, &uart_cfg);
    ...
    UART_socSetInitCfg(UART_INSTANCE, &uart_cfg);
    ...
    UART_Params_init(&params);
    ...
    handle = UART_open(UART_INSTANCE, &params);

At this point UART driver is ready for data transfer on specific
instance identified by handle. Application can call UART_read/write
API for read/write operation

2. UART_stdioInit() using the default UART parameters

::

    ...
    Board_init(boardCfg);
    ...
    UART_socGetInitCfg(UART_INSTANCE, &uart_cfg);
    ...
    UART_socSetInitCfg(UART_INSTANCE, &uart_cfg);
    ...
    UART_stdioInit(UART_INSTANCE);

At this point UART driver is ready for data transfer on specific
instance. Application can call UART_printf/scanFmt API for read/write
operation

3. UART_stdioInit2() using Application specified UART parameters

::

    ...
    Board_init(boardCfg);
    ...
    UART_socGetInitCfg(UART_INSTANCE, &uart_cfg);
    ...
    UART_socSetInitCfg(UART_INSTANCE, &uart_cfg);
    ...
    UART_Params_init(&params);
    ...
    UART_stdioInit2(UART_INSTANCE, &params);

At this point UART driver is ready for data transfer on specific
instance. Application can call UART_printf/scanFmt API for read/write
operation

.. rubric:: Read/Write APIs
   :name: readwrite-apis

**Interrupt**:

::

    UART_read(handle,scanPrompt, sizeof(scanPrompt));/* Read API */
    ...
    UART_write(handle, bufferPrompt, sizeof(bufferPrompt));/* Write API */

    Or

    UART_transactionInit(&transaction);
    transaction.buf = (void *)scanPrompt;
    transaction.count = sizeof(scanPrompt);
    UART_read2(uart, &transaction);
    ...
    UART_transactionInit(&transaction);
    transaction.buf = (void *)bufferPrompt;
    transaction.count = sizeof(bufferPrompt);
    UART_write2(uart, &transaction);

**Polling**:

::

    UART_readPolling(handle,scanPrompt, sizeof(scanPrompt));/* Read Polling mode API */
    ...
    UART_writePolling(handle, bufferPrompt, sizeof(bufferPrompt));/* Write Polling API */

.. rubric:: DMA Usage :
   :name: dma-usage

UART driver supports DMA operations to transfer data between

-  Memory and RX FIFO for read transfer
-  Memory and TX FIFO for write transfer.

DMA Driver is DMA family IP (EDMA and UDMA) and UART IP (V0 and V1) specific.
Refer soc/dma/v#/UART_dma.c for these operations. Application need to
create DMA handle and update the configuration before UART_init() API.

::

    uartInitCfg[UART_INSTANCE].edmaHandle = UartApp_edmaInit();/* For AM/K1/K2 devices */

    or

    uartInitCfg[UART_INSTANCE].udmaHandle = UartApp_udmaInit();/* For K3 devices */

    UART_init();

Refer “UART_BasicExample_[SOC]_[cpu]DMATestproject” or "UART_DMA_[evm]_[cpu]TestApp"
for additional reference. Refer SDK Release Note for supported EVMs.

Application
------------

Examples
^^^^^^^^

+-------------------------+---------------------+---------------------+---------------------+---------------------+
|         Name            |    Description      |  Expected Results   | SoC Supported       | Build Type          |
+=========================+=====================+=====================+=====================+=====================+
| UART_Example            | Example             | Application prompts |    AM335x,          | CCS project         |
| application             | demonstrating       | user to enter input |    AM437x,          |                     |
|                         | *simple* UART use   | data in console.    |    AM571x,          |                     |
|                         | case. Reference     |                     |    AM572x,          |                     |
|                         | example for         | User can enter up   |    AM574x,          |                     |
|                         | developers          | to 16 characters or |    k2g,             |                     |
|                         |                     | terminate with      |    k2hk,k2l,k2e,k2l |                     |
|                         |                     | enter               |    c6657,c6678      |                     |
|                         |                     | key.Application     |    omapl137,        |                     |
|                         |                     | echoes back         |    omapl138,        |                     |
|                         |                     | characters.         |                     |                     |
+-------------------------+---------------------+---------------------+---------------------+---------------------+
| UART_TestApplication    | Unit Test           | User can enter up to| AM335x,AM437x,AM571x| CCS project         |
|                         | application to test | 16 characters using | AM572x,AM574X       |                     |
|                         | all APIs            | serial              | k2g,k2hk,k2l,k2e,k2l|                     |
|                         |                     | console.Application | c6657,c6678         |                     |
|                         |                     | echoes back         | omapl137,omapl138   |                     |
|                         |                     |                     +---------------------+---------------------+
|                         |                     |                     | am65xx,j721e        | makefile            |
+-------------------------+---------------------+---------------------+---------------------+---------------------+
| UART_DMATestApplication | Unit Test           | User can enter up to| AM335x,AM437x,AM571x| CCS project         |
|                         | application with    | 16 characters using | AM572x,AM574X       |                     |
|                         | DMA mode.           | serial              | k2g,k2hk,k2l,k2e,k2l|                     |
|                         |                     | console.Application | c6657,c6678         |                     |
|                         |                     | echoes back         | omapl137,omapl138   |                     |
|                         |                     |                     +---------------------+---------------------+
|                         |                     |                     | am65xx,j721e        | makefile            |
+-------------------------+---------------------+---------------------+---------------------+---------------------+
| UART_SMP_TestApplication| Unit Test           | User can enter up to| AM572x-EVM          | CCS project         |
|                         | application to test | 16 characters using |                     |                     |
|                         | all APIs in SMP mode| serial              |                     |                     |
|                         | *(A15 & A53 cores)* | console.Application |                     |                     |
|                         |                     | echoes back         |                     |                     |
|                         |                     |                     +---------------------+---------------------+
|                         |                     |                     | am65xx,j721e        | makefile            |
+-------------------------+---------------------+---------------------+---------------------+---------------------+
| UART_SMP_DMATestApplica | Unit Test           | User can enter up to| AM572x-EVM          | CCS project         |
| tion                    | application         | 16 characters using |                     |                     |
|                         | in SMP mode with DMA| serial              |                     |                     |
|                         | enabled             | console.Application |                     |                     |
|                         | *(A15 & A53 cores)* | echoes back         |                     |                     |
|                         |                     |                     +---------------------+---------------------+
|                         |                     |                     | am65xx,j721e        | makefile            |
+-------------------------+---------------------+---------------------+---------------------+---------------------+

Building UART examples
----------------------

-  Makefile based examples and dependent libraries can be built from the top level or module level UART makefile, refer to the `Processor SDK RTOS Getting Started Guide <index_overview.html#setup-environment>`__  for details of how to setup the build environment. Once you have setup the build environment, issue the following commands:
::

   To build and clean libs/apps from top-level makefile:
   cd <pdk>/packages
   make uart
   make uart_clean

   To build and clean libs/apps from module-level makefile:
   cd <pdk>/packages/ti/drv/uart
   make all
   make clean


-  RTSC CCS project based examples are built from CCS
::

   cd <pdk>/packages
   ./pdkProjectCreate.sh [soc] [board] [endian] uart [project type] [processor] [SECUREMODE=<yes/no>]
   Import and build CCS Project from  <pdk>/packages/MyExampleProjects/


Additional References
---------------------

+----------------------+-----------------------------------+
|     **Document**     |           **Location**            |
+----------------------+-----------------------------------+
| API Reference Manual | $(TI_PDK_INSTALL_DIR)/packages/ti |
|                      | /drv/gpio/docs/doxygen/html/index |
|                      | .html                             |
+----------------------+-----------------------------------+
| Release Notes        | $(TI_PDK_INSTALL_DIR)/packages/ti |
|                      | /drv/gpio/docs/ReleaseNotes_UART  |
|                      | _LLD.pdf                          |
+----------------------+-----------------------------------+

|

