.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_IOLINK

Overview
--------

Introduction
^^^^^^^^^^^^

The IO-LINK Master driver provides an interface to any IO-Link devices
(sensors or actuators) accessible via a half-duplex UART serial bus on
SoC. It also provides a well-defined API layer which allows applications
(IO-Link master stack) to manage IO-Link devices via simple portable APIs.

The driver supports the following major functionalities:

-  Standard APIs to initialize/de-initialize/control the common Software
   IP driver
-  Configuration/Control of the PRU Frame Handler firmware to handle the
   messages transferred between the IO-Link master and device
-  Timer/Interrupt driven IO-Link communication between IO-Link master and
   device to meet the timing requirement of IO-Link master protocol

In addition a sample IO-Link master stack interface layer is provided in
the IO-Link master demo application to provide an interface between the
IO-Link master stack and the driver.

.. note::

   The stack interface layer should be ported to integrate a new master
   stack.


.. rubric::  Firmware
   :name: firmware

TI PRU-ICSS cores (Programmable Real-Time Unit Industrial Communication
Subsystem) is firmware programmable and can take on various
personalities. Processor SDK package includes IOLINK Firmware support.
Refer `IOLINK Frame Handler FW <index_pru_icss_fw.html#pru-icss-iolink>`__ for
additional details.

|

User Interface
--------------

Driver Configuration
^^^^^^^^^^^^^^^^^^^^^

.. rubric::  **Board Specific Configuration**
   :name: board-specific-configuration

All the board specific configurations eg:enabling and pin-mux of IO-Link
PRU pins should be performed before calling any driver APIs. By default
Board_Init() API supports all initialization sequence for TI supported
EVMs. Refer `Processor SDK RTOS Board
Support <index_board.html#board-support>`__ for additional
details.

Once the board specific configuration is complete driver API IOLINK_init()
can be called to initialize driver

.. rubric::  **IOLINK Configuration Structure**
   :name: iolink-configuration-structure

IOLINK_soc.c file binds driver with hardware attributes on the board
through IOLINK_config structure. This structure must be provided to IOLINK
driver. It must be initialized before the IOLINK_init() function is called
and cannot be changed afterwards. For details about the individual
fields of this structure, see the Doxygen help by opening
PDK_INSTALL_DIR\\packages\\ti\\drv\\iolink\\docs\\doxygen\\html\\index.html.

APIs
^^^^^

API reference for application:

::

    #include <ti/drv/iolink/IOLINK.h>

 Sample code for IOLINK control operation:

::

    ...
    Board_init(boardCfg);
    ...
    IOLINK_socGetFwCfg(peripheralNum, &iolink_cfg);
    ...
    IOLINK_socSetFwCfg(peripheralNum, &iolink_cfg);
    ...
    IOLINK_init();
    ...
    iolinkHandle = IOLINK_open(peripheralNum, &iolinkParams);
    ...
    status = IOLINK_control(iolinkHandle, iolinkCmd, &iolinkCmdArg);
    ...


Application
------------

Examples
^^^^^^^^

Refer Release Note for IOLINK support across different EVMs

+-----------------------+-----------------------+------------------------------------------------+---------------+------------+
|| Name                 || Description          ||  Expected Results                             | SoC Supported | Build Type |
+=======================+=======================+================================================+===============+============+
| IOLINK_Stack          || Demo stack example   || Following prints will come on console         | AM437x        | makefile   |
| Example application   |  to control 4 Autosen |  based on devices connected to the master:     | (TIDA-010016) |            |
|                       |  AO001 (sensor) and 4 || autosen gmbh device AO001 connected on port 0 |               |            |
|                       |  AD003 (actuator)     || autosen gmbh device AO001 detected an object  |               |            |
|                       |  devices              || autosen gmbh device AD003 connected on port 1 |               |            |
|                       |                       || autosen gmbh device AD003 display turned on   |               |            |
|                       |                       |                                                |               |            |
+-----------------------+-----------------------+------------------------------------------------+---------------+------------+

.. note::

   IOLINK demo example application uses 4 Autosen sensor devices and 4
   Autosen actuator devices. It pairs one sensor with one actuator
   when the devices are connected. If a sensor detects an object, it
   controls the paired acutator to turn on the display on the actuator.
   If the sensor does not detect an object, it controls the paired
   actuator to turn off the display.

Building IOLINK example
----------------------

-  Makefile based examples and dependent libraries can be built from
   the top level or module level IOLINK makefile, refer to the
   `Processor SDK RTOS Getting Started Guide <index_overview.html#setup-environment>`__
   for details of how to setup the build environment. Once you have
   setup the build environment, issue the following commands:
::

   To build and clean libs/apps from top-level makefile:
   cd <pdk>/packages
   make iolink
   make iolink_clean

   To build and clean libs/apps from module-level makefile:
   cd <pdk>/packages/ti/drv/iolink
   make all
   make clean


Additional References
---------------------

+-----------------------+--------------------------------------------------+
| **Document**          |  **Location**                                    |
+-----------------------+--------------------------------------------------+
| API Reference Manual  | $(TI_PDK_INSTALL_DIR)\\packages\\ti              |
|                       | \\drv\\iolink\\docs\\doxygen\\html\\index.html   |
+-----------------------+--------------------------------------------------+
| Release Notes         | $(TI_PDK_INSTALL_DIR)\\packages\\ti              |
|                       | \\drv\\iolink\\docs\\ReleaseNotes_IOLINK_LLD.pdf |
+-----------------------+--------------------------------------------------+

|
