.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_GPIO

Overview
--------

Introduction
^^^^^^^^^^^^

GPIO module allows application to manage General Purpose I/O  instances
and pins via simple portable APIs. Because of its simplicity, APIs are
pin based and does not follow model of other drivers inside PDK which
requires handle abstraction.

.. rubric:: Modes of Operation
   :name: modes-of-operation

Following modes of operations are supported
**Input or Output**
Each gpio pin can be configured as either input: GPIO_CFG_INPUT or
output: GPIO_CFG_OUTPUT. If it is configured as an output then pin
level can be additionally configured

**Interrupt support**
Each gpio pin can be configured to generate interrupts based on event
type GPIO_CFG_IN_INT_XXX configuration. To generate interrupt, gpio
pin has to be configured as input pin.

.. rubric:: Driver Configuration
   :name: driver-configuration-gpio

.. rubric:: **Board Specific Configuration**
   :name: board-specific-configuration

All board specific configurations like enabling clock and pin-mux are
required before calling any driver APIs. By default Board_Init() API
available under board module supports all initialization sequence for TI
supported EVMs. In addition it initializes UART instance for
Console/STDIO. Refer `Processor SDK RTOS Board
Support <index_board.html#board-support>`__ for additional
details.

.. rubric:: **GPIO Configuration Structure**
   :name: gpio-configuration-structure

GPIO_soc.c binds driver with hardware attributes on the board.
Hardware attributes includes base address, interrupt number etc. GPIO
pin behavior can be configured statically, or alternatively
dynamically during runtime.

GPIO_init () API triggers all static configuration information available
through hardware attributes. Once initialization is complete additional
APIs can be used to configure and access pins.

APIs
^^^^^

API reference for Application:

.. code-block:: c

    #include <ti/drv/gpio/GPIO.h>

Below sequence indicates API calling sequence for a simple use case of
LED toggling

.. code-block:: c

    ...
    Board_init(boardCfg);
    GPIO_init();
    While(1)
    {
    GPIO_write(Board_LED1, GPIO_PIN_VAL_HIGH);
    Delay();
    GPIO_write(Board_LED1, GPIO_PIN_VAL_LOW);
    Delay();
    }

Application
------------

Examples
^^^^^^^^

Refer SDK Release Note for GPIO support across different EVMs.

+-------------------+-----------------------+-----------------------+---------------------+---------------------+
|       Name        |      Description      || Expected Results     | SoC Supported       | Build Type          |
+===================+=======================+=======================+=====================+=====================+
| GPIO_LedBlink     | Simple example        || Following LED        |    AM335x,          | CCS project         |
|                   | demonstrating LED     | blinks based on EVM   |    AM437x,          |                     |
|                   | Toggling              | being used.           |    AM571x,          |                     |
|                   |                       |                       |    AM572x,          |                     |
|                   |                       || **AM335x             |    AM574x,          |                     |
|                   |                       | ICEv2**:              |    k2g,             |                     |
|                   |                       | USER  LED 1           |    k2hk,            |                     |
|                   |                       |                       |    k2l,             |                     |
|                   |                       || **AM437x             |    k2e,             |                     |
|                   |                       | EVM**:                |    c6657,           |                     |
|                   |                       | USER  LED 1           |    c6678,           |                     |
|                   |                       |                       |    omapl137,        |                     |
|                   |                       || **AM572x IDK** :     |                     |                     |
|                   |                       | STATUS LED 1 Yellow   +---------------------+---------------------+
|                   |                       | **AM572x GP           |    am65xx           | makefile            |
|                   |                       | EVM** : USER LED1     |    j721e            |                     |
|                   |                       | **AM574x IDK** :      |                     |                     |
|                   |                       | STATUS LED 1 Yellow   |                     |                     |
|                   |                       | **AM572x GP           |                     |                     |
|                   |                       | EVM** : USER LED1     |                     |                     |
|                   |                       | **AM571x IDK** :      |                     |                     |
|                   |                       | Industrial LED 3      |                     |                     |
|                   |                       | Red                   |                     |                     |
|                   |                       |                       |                     |                     |
|                   |                       || **K2H EVM:**         |                     |                     |
|                   |                       | USER LED 2 Blue       |                     |                     |
|                   |                       |                       |                     |                     |
|                   |                       || **K2E EVM:**         |                     |                     |
|                   |                       | USER LED 1 Blue       |                     |                     |
|                   |                       |                       |                     |                     |
|                   |                       || **K2G EVM:**         |                     |                     |
|                   |                       | USER LED 1 Yellow     |                     |                     |
|                   |                       |                       |                     |                     |
|                   |                       || **AM65xx EVM:**      |                     |                     |
|                   |                       | USER LD16, LD17       |                     |                     |
|                   |                       |                       |                     |                     |
|                   |                       || **J721E EVM:**       |                     |                     |
|                   |                       | USER LED 1            |                     |                     |
|                   |                       |                       |                     |                     |
+-------------------+-----------------------+-----------------------+---------------------+---------------------+

.. note::

   There are no user mode LEDs directly connected to GPIO pins on K2L, C6678 and C6657 EVMs.

Building GPIO examples
----------------------

-  Makefile based examples and dependent libraries can be built from the top level or module level GPIO makefile, refer to the `Processor SDK RTOS Getting Started Guide <index_overview.html#setup-environment>`__  for details of how to setup the build environment. Once you have setup the build environment, issue the following commands:
::

   To build and clean libs/apps from top-level makefile:
   cd <pdk>/packages
   make gpio
   make gpio_clean

   To build and clean libs/apps from module-level makefile:
   cd <pdk>/packages/ti/drv/gpio
   make all
   make clean


-  RTSC CCS project based examples are built from CCS
::

   cd <pdk>/packages
   ./pdkProjectCreate.sh [soc] [board] [endian] gpio [project type] [processor] [SECUREMODE=<yes/no>]
   Import and build CCS Project from  <pdk>/packages/MyExampleProjects/

FAQ
----------------------

**Is there any example using GPIO as input**

Please refer to `RTOS Customization: using an external input to trigger an interrupt
on AM57x <index_how_to_guides.html#rtos-customization-using-an-external-input-to-trigger-an-interrupt-on-am57x>`_ for details.

Additional References
---------------------

+----------------------------+-----------------------------------+
| **Document**               | **Location**                      |
+----------------------------+-----------------------------------+
| API Reference Manual       | $(TI_PDK_INSTALL_DIR)/packages/ti |
|                            | /drv/gpio/docs/doxygen/html/index |
|                            | .html                             |
+----------------------------+-----------------------------------+
| Release Notes              | $(TI_PDK_INSTALL_DIR)/packages/ti |
|                            | /drv/gpio/docs/ReleaseNotes_GPIO  |
|                            | _LLD.pdf                          |
+----------------------------+-----------------------------------+

|
