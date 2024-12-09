.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_PRUSS

Overview
--------

Introduction
^^^^^^^^^^^^

| The PRUSS (Programmable Real-Time Unit Subsystem) provides a
  well-defined API layer which allows applications to use the PRUSS low
  level driver to control  sub system.

|

.. rubric:: Firmware
   :name: firmware

The PRUSS (Programmable Real-Time Unit Subsystem) is firmware
programmable and can take on various personalities. Examples include an
ethernet MAC, ethernet Switch, Industrial protocol switch. For a good
example, please refer to `Simple Open Real Time Ethernet Protocol (SORTE)
<index_pru_icss_fw.html#pru-icss-sorte>`__

.. rubric:: Driver Features
   :name: driver-features

-  PRU control features i.e enable/disable/reset a PRU
-  Helper functions i.e. load and execute firmware in PRU
-  Memory mapping of PRU/L3/External memories
-  PRU and Host event management (i.e. map sys_evt/channel/hosts in PRU
   INTC generate interrupts, wait for occurrence of an event, and
   acknowledge interrupts
-  Interrupt management for A15/C66x CPU targets

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

.. rubric::  **Board Specific Configuration**
   :name: board-specific-configuration

All the board specific configurations like enabling the clock and
pin-mux of UART/GPIO/PRUSS ICSS pins should be performed before
calling any of the driver APIs.

|
.. rubric::  **PRUSS Configuration Structure**
   :name: pruss-configuration-structure

The pruicss_device.c file contains the declaration of the PRUICSS
config structure. This structure must be provided to the driver at the
time when PRUICSS_create() API is called to creat the PRUICSS_Handle.
This handle is subsequently required to make any PRUSS LLD API call.

APIs
^^^^^

Reference API header file:

::

    #include <ti/drv/pruss/pruicss.h>

.. rubric:: API Call Flow
   :name: api-call-flow

Below sequence indicates calling sequence of PRUSS driver APIs for a use
case of sending INTC event to the PRU. Refer example code within module
for additional details

::

     ...
     /* Initialize Board */
     Board_init(boardCfg);

     /* Creates handle for PRUICSS instance */
     handle = PRUICSS_create(pruss_config,instance);

     /* Disable PRUICSS instance */
     PRUICSS_pruDisable(handle,instance );

     /* Register an Interrupt Handler for an event */
     PRUICSS_registerIrqHandler(handle,pruEvtoutNum,intrNum,eventNum,waitEnable,irqHandler);

     /* Sets the buffer pointer for PRU */
     PRUICSS_setPRUBuffer(..);

     /* API to do Interrupt-Channel-host mapping */
     PRUICSS_pruIntcInit(handle,&pruss_intc_initdata);

     /* Execute program on PRU */
     PRUICSS_pruExecProgram(handle,0);

      /* Enable PRU */
     PRUICSS_pruEnable(handle,0);

     /* Generates INTC event */
     PRUICSS_pruSendEvent(handle,ARM_PRU0_EVENT);


Application
------------

Examples
^^^^^^^^

+-----------------------+-----------------------+-----------------------+
| Name                  ||  Description         ||  Expected Results    |
+=======================+=======================+=======================+
| PRUSS_TestApplication || Test application is  || Following prints     |
|                       |   designed to ping    | expected on console   |
|                       |   pong an event       | based on pass/fail    |
|                       |   between CPU         | criteria:             |
|                       |   target(A15/C66x)    ||                      |
|                       |   and PRU for a fixed || **Pass criteria:**   |
|                       |   count.Application   |                       |
|                       |   is to test PRU’s    || Prints related to    |
|                       |   load, control and   | sending and           |
|                       |   Interrupt           | receiving  event from |
|                       |   controller          | PRU will be printed   |
|                       |   functionalities.    | on  console. Test     |
|                       |                       | program at the end    |
|                       |                       | expected to output:   |
|                       |                       | "All tests have       |
|                       |                       | passed"               |
+-----------------------+-----------------------+-----------------------+

Additional References
---------------------

+-----------------------------------+----------------------------------------+
|   **Document**                    | **Location**                           |
+-----------------------------------+----------------------------------------+
| API Reference Manual              | $(TI_PDK_INSTALL_DIR)\\packages\\ti    |
|                                   | \\drv\\pruss\\docs\\doxygen\\html\\inde|
|                                   | x.html                                 |
+-----------------------------------+----------------------------------------+
| Release Notes                     | $(TI_PDK_INSTALL_DIR)\\packages\\ti    |
|                                   | \\drv\\pruss\\docs\\ReleaseNotes_PRUS  |
|                                   | S_LLD.pdf                              |
+-----------------------------------+----------------------------------------+

|

