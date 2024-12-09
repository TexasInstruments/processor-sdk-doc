.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Template_App

Introduction
============
.. note::
   This workshop duplicates information found elsewhere in the RTOS Software
   Developer Guide for the purpose of creating a cohesive document.

This workshop is a simple introduction for software development using
Processor SDK RTOS. The goal of this workshop is to get you familiarized with
Processor SDK RTOS and introduce you to using Sitara Evaluation Modules (EVMs)
and TI tools.

To accomplish this goal, we will work through an interactive lab using the
RTOS/Bare-metal Template Application. This application will introduce key concepts of
the SDK and serves as the starting point for creating your own application.

Here's what we will learn over the course of this lab:

- Basic usage of Code Composer Studio (CCS)

  - Importing
  - Editing
  - Building
  - Flashing
- Processor SDK RTOS Software

  - Low level drivers (LLDs) such as UART, GPIO, etc.
  - Operating System Abstraction Layer (OSAL)
  - Board library

|

Prerequisites
=============

Software
--------
- Processor SDK RTOS for your platform

  - `AM335x <http://www.ti.com/tool/PROCESSOR-SDK-AM335X>`_
  - `AM437x <http://www.ti.com/tool/PROCESSOR-SDK-AM437X>`_
  - `AM57x <http://www.ti.com/tool/PROCESSOR-SDK-AM57X>`_
  - `AM65x <http://www.ti.com/tool/PROCESSOR-SDK-AM65X>`_

- CCS Version associated with your SDK Release

  - A download link for CCS is located on the same page as the SDK download.

.. note::
   If you are using AM65x, you will also need to install latest TI Emulators
   and Sitara device support packages into CCS. This can be done through
   CCS --> Help --> Check for Updates.

Hardware
--------
- A supported Sitara Evaluation Module

  - `AM335x EVM <http://www.ti.com/tool/TMDXEVM3358>`_
  - `AM437x EVM <http://www.ti.com/tool/TMDSEVM437X>`_
  - `AM572x EVM <http://www.ti.com/tool/TMDSEVM572X>`_
  - `AM654x EVM <http://www.ti.com/tool/TMDX654IDKEVM>`_

- JTAG Debug Probe if using AM572x EVM

  - XDS100-class JTAG debug probes

    - Low cost, low performance
    - XDS100v1 is not supported.
  - XDS200-class JTAG debug probes

    - Recommended
  - XDS560v2-class JTAG debug probes

    - High performance
- Serial UART cable provided in the EVM kit

Recommended Training Videos
---------------------------
- `Processor SDK Training Series`__

  - Introduction to the Processor SDK Training Series
  - Processor SDK Overview
  - Introduction to Processor SDK RTOS Part 1
  - Introduction to Processor SDK RTOS Part 2
  - Application Development Using Processor SDK RTOS
- `AM437x Sitara Processors Training Series`__
- `AM57x Sitara Processors Training Series`__
- `AM65x Sitara Processors Training Series`__

__ https://training.ti.com/processor-sdk-training-series
__ https://training.ti.com/am437x-sitara-processors-training-series
__ https://training.ti.com/am57x-sitara-processors-training-series
__ https://training.ti.com/am6x

|

Template Application Overview
=============================
The Template Application is intended for
customers to use as a starting point during software development using
Processor SDK RTOS software. The Template Application can be quickly brought up
by importing the included Code Composer Studio (CCS) project into the CCS
development environment. The application currently includes the typical low
level drivers such as UART, GPIO, and I2C, the OSAL layer, and Board Library.
For additional details refer to the **README.txt** file in the installed
package.

Components Used
---------------

-  SYS/BIOS (RTOS only)
-  XDCTools (RTOS only)
-  Processor SDK RTOS PDK

   - Drivers, OSAL, etc.

Software Design
---------------

The Template Application is designed to provide a foundational project with a
clean separation of the application-specific submodule from the startup and
initialization code. This gives users the ability to focus on
application-specific code and quickly get it up and running. This separation is
achieved by splitting the "main" and "app" submodules into different files.

The source files are organized as follows::

    └── template_app
        ├── baremetal
        │   ├── app.c --> Application tasks are here
        │   ├── app.h --> Application header file
        │   ├── baremetal_template_app_am572x_a15_evmAM572X.projectspec --> Project spec file
        |   ├── main.c --> Main file which has board and driver init code
        │   ├── lnk_a15.cmd --> Linker command file.
        ├── GPIO_board.h --> Gpio board header
        ├── GPIO_evmAM572x_board.c --> Gpio board configuration
        └── rtos
            ├── app.c --> Application tasks are here
            ├── app.cfg --> Application specific config file
            ├── app.defs --> Definitions (Currently empty)
            ├── app.h --> Application header file
            ├── main.c --> Main file which has board and driver init cod
            ├── main.cfg --> Main BIOS config file
            └── rtos_template_app_am572x_a15_evmAM572X.projectspec --> Project spec file

In general, to write a new application **app.c** and **app.h** can be
modified, recompiled, and run.

|

Lab
===
Now that the introductory material is out of the way, it is time to get our
hands dirty and begin the lab.

.. Note::
   The AM572x EVM was used for the creation of this lab material, but the same
   instructions apply for the other supported platforms -- AM335x EVM,
   AM437x EVM, and AM654x EVM.

Task 1 - Installing the Processor SDK into CCS
----------------------------------------------
Before using the Processor SDK, we must install its components into Code
Composer Studio (CCS). Typically -- if you chose to install the Software
Development Kit (SDK) into the default **$HOME/ti**
or **C:\\ti** location -- CCS will automatically detect the new products the
next time it is opened and prompt you to install them. If you are not prompted
to install the new products, you can do so manually through the *Window -->
Preferences --> Code Composer Studio --> Products* menu. This menu will allow
you define product discovery paths and rediscover, install, and unistall
products.

.. image:: /images/install-discovered-products.png
   :scale: 70 %

For more info on setting up CCS. Check out
`Setup CCS for EVM and Processor-SDK RTOS <index_how_to_guides.html#setup-ccs-for-evm-and-processor-sdk-rtos>`__
in the How To Guides.

Task 2 - Importing and Building the  Template Application
---------------------------------------------------------
We begin the lab by importing the RTOS or Bare-metal Template Application into CCS. The
Template Application is delivered as a preconfigured CCS Project, making this
process very simple. We will also use this as an opportunity to briefly dive
into the structure of the SDK.

To import a project into CCS, go to the *Project --> Import CCS Projects...*
menu. Typically, you will import SDK projects from either the
**pdk_<platform>_<version>** or **processor_sdk_rtos_<platform>_<version>**
directories. The **pdk_<platform>_<version>** directory contains Chip Support
Library (CSL), Low Level Drivers (LLDs), Boot, Diagnostics, and other
functions. It is also where LLD example projects are created. The
**processor_sdk_rtos_<platform>_<version>** directory contains demos
(including the Template App), documentation, and resources for creating
bootable SD cards.

Now that you have an understanding of these directories, let us move on to
importing the Template Application.

To import a project into CCS open the *Project --> Import CCS Projects...*
menu. Then click *Browse...* to locate the template app which can be found at:
**processor_sdk_rtos_<platform>_<version>/demos/rtos_template_app/<soc_name>/<evm_name>/<core_name>**.
This will create a copy of the project in your CCS workspace.

.. image:: /images/import-ccs-project.png
   :scale: 70 %

After project import is complete you will see the Template Application under
the *Project Explorer* on the left side of CCS. Next, right click on the
project and select *Build Project*. You should get a message that says
``**** Build Finished ****`` in the CCS Console.

Task 3 - Hardware Setup
-----------------------

.. Warning::
   The EVM board is sensitive to electrostatic discharges
   (ESD). Use a grounding strap or other device to prevent damaging the
   board. Be sure to connect communication cables before applying power to
   any equipment.

Hardware setup will vary depending on which EVM you are using. Generally,
you need to make sure that the boot switches are set correctly and that serial,
a JTAG debug probe, and power are connected to the board.

Refer to the Quick Start Guide that came with your board and the Hardware
User's Guide for more detailed hardware setup information.

- AM335x EVM:

  - `Quick Start Guide`__
  - `HW User's Guide`__
- AM437x EVM:

  - `Quick Start Guide`__
  - `HW User's Guide`__
- AM572x EVM:

  - `Quick Start Guide`__
  - `HW User's Guide`__
- AM654x EVM
  - `Quick Start Guide`__

__ http://www.ti.com/lit/ml/sprw225d/sprw225d.pdf
__ http://processors.wiki.ti.com/index.php/AM335x_General_Purpose_EVM_HW_User_Guide
__ http://www.ti.com/lit/ml/sprw256/sprw256.pdf
__ http://processors.wiki.ti.com/index.php/AM437x_General_Purpose_EVM_HW_User_Guide
__ http://www.ti.com/lit/ug/sprw275/sprw275.pdf
__ http://www.ti.com/lit/pdf/spruig1
__ http://www.ti.com/lit/pdf/sprw323

Example connections for the AM572x EVM are provided below:

Front
^^^^^
.. image:: /images/am572x-evm-hw-setup-front.jpg
   :scale: 50 %

Back
^^^^
.. image:: /images/am572x-evm-hw-setup-back.jpg
   :scale: 44 %

Task 4 - Loading and Running the Template Application
-----------------------------------------------------

Creating a Target Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In order to connect to the target platform we first need to create a target
configuration file. To do this, open CCS and go to the *File --> New -->
Target Configuration File* menu and create a new target configuration file
named after your board. For example, **am572x-evm.ccxml**. Next, you need to
choose your *connection* and *board* on the target configuration file page.
The *connection* is your chosen JTAG Debug Probe (for example, the XDS200) and
the *board* is the name of your EVM (either *EVMAM3358*, *EVMAM437X*, or
*GPEVM_AM572x_SiRevA*).

For example, here is the target configuration for the AM572x EVM using an
XDS200 Debug Probe:

.. image:: /images/am572x-evm-target-config.png
   :scale: 70 %

After setup is complete, clike the *Save* button to save your target
configuration. Then click *Test Connection* to verify that you can connect
to the board. If the test is successful you should receive the following
message::

    The JTAG DR Integrity scan-test has succeeded.

Connecting to the Target
^^^^^^^^^^^^^^^^^^^^^^^^
With our target configuration confirmed, we can now move on to connecting to
the target and loading our application.

First, set up the UART connection using the following host configuration
in your favorite serial terminal program (e.g. Tera Term, screen, Minicom):

-  **Baud Rate**: 115200
-  **Data Bits**: 8
-  **Parity**: None
-  **Flow Control**: Off

Next, click on *View --> Target Configurations* in CCS. Then, right click on
the target configuration that you created earlier and click *Launch Selected
Configuration*. This action will switch CCS into the debug perspective. Your
CCS instance should look similar to below:

.. image:: /images/ccs-debug-pers.png
   :scale: 70 %

In the top left corner of CCS you should see a list of all of the available
cores on your device. Right click on the primary core (listed below) and choose
the *Connect Target* option. During this process you should see GEL output in
the CCS console and the status of the core should change from "Disconnected"
to "Suspended".

Primary cores for each target:

+--------+--------+--------+--------+
| AM335x | AM437x | AM572x | AM654x |
+========+========+========+========+
|   A8   |   A9   | A15_0  | A53_0  |
+--------+--------+--------+--------+

.. Note::
   For AM572x EVM, the template application can also run on the M4 and DSP
   cores. If you intend to run the application on one of these cores you must
   still connect to the main A15_0 core **first**. After connecting to the
   A15_0 core you can then follow the same procedure as above to connect
   to the secondary core where you would like to run the application. Do not
   attempt to load and run the template application on two cores simultaneously
   as the Template Application is not designed to run this way.

   Similar instructions apply to AM654x EVM, where you should connect to the M3
   core first before running on your application core.

Running the Application
^^^^^^^^^^^^^^^^^^^^^^^

Now that we are connected to the target, it is time to load the application.
To do this, go to the *Run --> Load --> Load Program* menu in CCS. Then, click
the *Browse project...* button and choose the
**[rtos or baremetal]_template_app_<board>_<core>.out** executable. Then click *OK* to load
the executable.

.. image:: /images/load-executable.png

You should now see the **main.c** file open in CCS and the program halted at
the beginning of the ``main()`` function. At this point you can click on the
*Resume (F8)* |resume| button to start executing the Template Application.

.. |resume| image:: /images/resume-button.png

The application will begin running and print progress over the UART. You should
see the following text printed to your serial terminal::

    Board Init complete
    Uart Init complete
    I2C Init complete
    Gpio Init complete
    MCSPI Init complete
    ======== Peripheral Initialization complete ========

    ======== Starting to create application tasks ========

    gpio_toggle_led_task task created.
    uart_task task created.
    spi_test_task task created.
    i2c_eeprom_read_and_display_task task created.
    ======== Application tasks created successfully ========

    gpio_toggle_led task started
    uart_task task started

    i2c_eeprom_read_and_display task started
    spi_test task started
    Board Name read: AM572PM_
    Board version read: A.30
    spi_test task ended
    i2c_eeprom_read_and_display task ended
    uart_task :Enter a word or Esc to quit >

Type a word into the serial terminal. It should be echoed back to you. Then,
enter the ``ESC`` character to exit the Template Application. For example::

    uart_task :Enter a word or Esc to quit >hello
    Data received is:hello

    uart_task :Enter a word or Esc to quit >test
    Data received is:test

    uart_task :Enter a word or Esc to quit >^[

    uart_task task ended
    Template app ended

Next, click the *Terminate* |terminate| button to disconnect from the target.
At this point you have successfully imported, built, and run the Template
Application.

.. |terminate| image:: /images/terminate-button.png

Task 5 - Examining the Template Application
------------------------------------------------
Now that you're familiar with using the Template Application, let us look into
the code to see how it all works.

The main.c File
^^^^^^^^^^^^^^^
Begin by opening the **main.c** file. At the top of this file, after the
copyright header, there are a series of ``#include`` statements gathering
the necessary header files for the application:

.. code-block:: c

    /* Standard header files */
    #include <string.h>

    /* XDCtools Header files (RTOS only) */
    #include <xdc/std.h>
    #include <xdc/cfg/global.h>
    #include <xdc/runtime/System.h>
    #include <xdc/runtime/Error.h>

    /* BIOS Header files (RTOS only) */
    #include <ti/sysbios/BIOS.h>
    #include <ti/sysbios/knl/Task.h>

    /* Board header file */
    #include <ti/board/board.h>

    /* Local template app header file */
    #include "app.h"

- (RTOS only) XDCtools provides configuration tools to create and build a static
  configuration as part of your application. These headers are necessary
  for the ``*.cfg`` configuration files.
- (RTOS only) BIOS is a synonym for TI-RTOS. These headers are necessary for accessing
  common RTOS features such as tasks.
- The Board Library is a thin utility
  layer on top of  CSL and other board utilities. It provides uniform
  Application Programming Interfaces (APIs)
  for all supported boards. It aims to assist the user to quickly write
  portable applications for supported boards by hiding board level details
  from the user.
- The ``app.h`` header file includes header files for drivers used
  in the application code as well as macros and function prototypes.
  Specifically, ``app.h`` includes headers for the following LLDs
  which are used by the application:

    .. code-block:: c

        /* Low level driver header files */
        #include <ti/drv/gpio/GPIO.h>
        #include <ti/drv/uart/src/UART_utils_defs.h>
        #include <ti/drv/uart/UART_stdio.h>
        #include <ti/drv/uart/UART.h>
        #include <ti/drv/i2c/I2C.h>
        #include <ti/drv/spi/MCSPI.h>

Next, we come across the ``main()`` function which demonstrates the common
procedure for initializing an RTOS or bare-metal application. You can read the comments in
the code for further clarification. Let's break down the steps:

1) Initialize the board::

    Board_initCfg boardCfg;
    boardCfg =
        BOARD_INIT_PINMUX_CONFIG |
        BOARD_INIT_MODULE_CLOCK |
        BOARD_INIT_UART_STDIO;
    Board_init(boardCfg);

2) Intialize the peripherals::

    UART_init();
    I2C_init();
    GPIO_init();
    MCSPI_init();

3) (RTOS only) Create the application tasks. We will discuss this further in the section
   covering the ``app.c`` file.

4) Start BIOS (RTOS) or start the application tasks directly (Bare-metal)::

    BIOS_start();

    or

    appRunTasks();

The app.c File
^^^^^^^^^^^^^^

**RTOS**

Open the **app.c** file and take a look at the ``appTasksCreate()``
function. You should recall that this function was called in step three
of ``main()``. Inside of ``appTasksCreate()`` there are ``biosTaskCreate()``
function calls for each peripheral task. ``biosTaskCreate()`` just wraps the
common task creation procudure into an easy-to-use function call. Navigate to
the bottom of the **app.c** file to check out ``biosTaskCreate()``.

The task creation procudure is as follows:

1) Create task variables

    .. code-block:: c

            Task_Params taskParams;
            Error_Block eb;
            Task_Handle task;

2) Initialize ``Error_Block`` and ``Task_Params`` to their default values

    .. code-block:: c

        Error_init(&eb);
        Task_Params_init(&taskParams);

3) Apply user arguments for stack name, priority, and stack size

    .. code-block:: c

            taskParams.instance->name = taskName;
            taskParams.priority = taskPriority;
            taskParams.stackSize = stackSize;

4) Create the task

    .. code-block:: c

        task = Task_create(taskFunctionPtr, &taskParams, &eb);

The tasks themselves are simply functions in your code following the format
below:

.. code-block:: c

    void myTaskFunc(UArg arg0, UArg arg1)

**Bare-metal**

Open the **app.c** file and take a look at the ``appRunTasks()`` function.
Inside of ``appRunTasks()`` there are function calls for each peripheral task.
This file also contains setup code for a timer interrupt that controls
the LED blink task.

.. note::
   The application functions are called "tasks" for naming consistency
   with the RTOS template application, but they are not actual SYS/BIOS
   tasks.

Next, let's take a look at ``i2c_eeprom_read_and_display_task()`` to
see how to use TI Drivers. The procedure for opening a TI Driver generally
follows these steps:

1) Create driver handle and params structure

    .. code-block:: c

        I2C_Handle      handle;
        I2C_Params      params;

2) Initialize and set the driver parameters

    .. code-block:: c

        I2C_Params_init(&params);
        params.transferMode  = I2C_MODE_CALLBACK;
        params.transferCallbackFxn = someI2CCallbackFunction;
        // etc...

3) Open the driver

    .. code-block:: c

        handle = I2C_open(someI2C_configIndexValue, &params);
        if (!handle) {
            System_printf("I2C did not open");
        }

For more information on TI Drivers, check out the included documentation for
each driver at **pdk_<platform>_<version>/packages/ti/drv/<driver>/docs**.

For more infomation on SYS/BIOS, check out the  User Guide at
**bios_<version>/docs**.

Task 6 - Modifying the RTOS Template Application
------------------------------------------------
.. note::
   The instructions below apply to the RTOS Template Application only.

Now that you have an understanding of how to use the drivers and create RTOS
tasks, let us make some simple modifications to create our own application.

We will create a simple application which allows the user to control the LED
blink rate over the UART terminal. The user should be able to enter an LED
blink period (between 0 and 5 seconds) and the user LED
should blink at that rate.

This part of the lab is broken down into several sections. In each section,
you will be given general instructions for modifications to make to the source
files. After you make your own modifications they will be verified against
provided code examples. Try to make the modifications on your own before
looking at the answers!

Delete the Code You Don't Need
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Template Application has tasks for UART, I2C, GPIO, and MCSPI drivers. Some
of these tasks will not be used by our application. Go ahead and remove any
tasks that you do not think you will need to create the
application. Hold off on modifying tasks that will be reused until later
steps.

.. attention::
   Don't peek! The next section will discuss answers to the task above.

Since our application is only consuming user input and blinking the LEDs, we
only need the UART and GPIO tasks. That means the I2C and SPI tasks can be
removed.

Add Support for Additional Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Our application will require that the UART task has a way to communicate the
delay value it receives from the user to the LED task to modify the blink rate.
While this could be accomplished with something as simple as a shared global
variable, TI-RTOS provides many other ways to accomplish inter-process
communication. Take a look at the BIOS User Guide, which is bundled with the
SDK at **bios_<version>/docs/Bios_User_Guide.pdf** for ideas on how to share
data between tasks. After you decide on a method, you can use the API
documentation located at **bios_<version>/docs/Bios_APIs.html** to figure out
how to use the API in your application.

.. attention::
   Don't peek! The next section will discuss answers to the task above.

A good choice for passing the LED blink rate is the ``ti.sysbios.knl.Mailbox``
module. This module can be used to pass buffers from one task to another on the
same processor.

To include ``Mailbox`` in your project you first need to add the module to the
**app.cfg** file:

.. code-block:: javascript

    var Mailbox = xdc.useModule('ti.sysbios.knl.Mailbox');

Next, you need to include the ``ti/sysbios/knl/Mailbox.h`` header file in
**app.h**:

.. code-block:: c

    #include <ti/sysbios/knl/Mailbox.h>

To create a Mailbox, use the ``Mailbox_create()`` API which is defined below:

.. code-block:: c

    Mailbox_Handle Mailbox_create(SizeT             bufsize,
                                  UInt              numBufs,
                                  Mailbox_Params    *params,
                                  Error_Block       *eb)

You are now set up to use ``Mailbox`` in your application code.

Add New Application Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Modify the existing UART and LED task code to functions for the new application.
If you run in to any issues, make sure to use CCS debug features such as
breakpoints and variable watching to verify that the application is functioning
in the way that you expect. Functional example code for the AM572x EVM will be
provided at the end.

.. attention::
   Don't peek! The next section will discuss answers to the task above.

1) Create a global ``Mailbox_Handle`` to be shared by the ``uart_task()`` and
   ``gpio_toggle_led_task()``. Then create a Mailbox at the end of the
   ``appTasksCreate()`` function.
2) Modify the ``uart_task()`` code to scan for an unisgned integer delay value
   instead of a string. This value should then be placed in the Mailbox by
   using the ``Mailbox_post()`` API.
3) Modify ``gpio_toggle_led_task()`` to retrieve a delay value from the
   Mailbox via the ``Mailbox_pend()`` API. This delay value should be used in
   the ``task_sleep()`` function calls.

Now, give your project a try. You should be able to type in LED delay values to
the UART terminal and see the blink rate of the LED change accordingly. To see
a functioning solution, you can download the modified source files from the
links below. Sections of the source files that were modified from the originals
are marked with a ``/* Modification: */`` comment.

  - :download:`app.c <../example_code/template_app_mods/app.c>`
  - :download:`app.h <../example_code/template_app_mods/app.h>`
  - :download:`app.cfg <../example_code/template_app_mods/app.cfg>`

|

Additional Information
======================
Porting to a Custom Board
-------------------------
The Template Application can be easily modified to run on a custom board. The
major change required is to link in a new Board Library. Modifying the
Template Application for your custom Board can be achieved by simply removing
the ``ti.board`` library and PATH from the project and replacing with your
specific board libraty and PATH under the linker build options in CCS by
right clicking on the project and selecting
*Properties --> GNU Linker --> Libraries*.

For example, currently the library linked for AM572x is specified in the
**.projectspec** file as follows::

    linkerBuildOptions=
        -L${TI_PDK_INSTALL_DIR}/packages/ti/board/lib/evmAM572x/a15/release/
        -l:ti.board.aa15fg

.. note::
   Currently for AM572x EVM there is also a dependemcy on the
   **GPIO_evmAM572x_board.c** and **GPIO_board.h** files. These files can be
   modified for your custom board.

Next Steps
==========
Thanks for taking the time to read through this getting started workshop.
At this point you should be comfortable with the basic structure of the SDK,
know how to import, build, modify, and run applications on the target, and know
where to find various documentation in the SDK and Software Developer Guide.

Next, you can check out our various video training series in the `TI training
portal`__, check out our
`Examples and Demonstrations <index_examples_demos.html>`__, and get
started writing your own application!

__ https://training.ti.com/

If you have any questions along the way please remember to read the
`FAQ <index_faq.html>`__ or reach out to our engineers on the `E2E forums`__.

__ http://e2e.ti.com/
