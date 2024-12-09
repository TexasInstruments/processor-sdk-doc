.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Gravity_Simulator_Demo

Overview
========

This demo showcases a simple video display with Processor SDK RTOS. This
demo uses Gravit, a GPL-licensed open-sourced library, to simulate
gravity of particles in space.

Version Details
===============

Latest version: 1.0.0

Supported platforms: idkAM572x

Available in: Processor SDK RTOS 4.0.0.4

Components Used
===============

Open Sourced Libraries:

-  Gravit

RTOS Components:

-  SYSBIOS
-  XDC

Processor SDK RTOS Drivers:

-  VPS
-  PM
-  I2C
-  UART
-  Board
-  OSAL
-  CSL

Building the Demo
=================

The demo is available pre-built for Processor SDK RTOS version 4.0.0.4
or higher. You must first set up your development environment. Refer to
the `Processor SDK RTOS Building <index_overview.html#building-the-sdk>`__ page for
information on setting up your build environment.

The following are steps to clean the demo:

::

     cd [SDK Install Path]/processor_sdk_rtos_[soc]_[version]/demos/gravit
     make clean BOARD=idkAM572x

The following are steps to compile the demo:

::

     cd [SDK Install Path]/processor_sdk_rtos_[soc]_[version]/demos/gravit
     make BOARD=idkAM572x

Running the Demo
================

You will need the following:

#. Code Composer Studio to load and run the demo. Refer to :ref:`Processor
   SDK RTOS Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>` for
   installing CCS.
#. idkAM572x board with attached LCD screen
#. USB cable for JTAG and serial terminal (micro USB port)

To load and run the demo:

#. Connect the USB cable from your computer to the idkAM572x's JTAG port
#. Power on the idkAM572x board. Ensure that no boot mode is entered (do
   not have SD card loaded or QSPI flashed)
#. Open up a serial terminal for UART communication (Refer to :ref:`Processor
   SDK RTOS Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>`, setup
   EVM hardware)
#. Open CCS and launch target config file for idkAM572x (Refer to
   `Processor SDK RTOS Setup CCS <index_how_to_guides.html#setup-ccs-for-evm-and-processor-sdk-rtos>`__ for setting up CCS)
#. Connect to CortexA15_0
#. Load and launch the demo executable:

::

     [SDK Install Path]/processor_sdk_rtos_[soc]_[version]/demos/gravit/bin/idkAM572x/gravit_a15_0_release.xa15fg

Terminal Screenshot
===================

-  When launched, you will be prompt for number of particles to
   simulate. Enter a value up to 1000.
-  Use w-a-s-d for display rotation
-  Use i-j-k-l for display translation
-  Press Esc to end current simulation and display accumulated
   statistics
-  Frames per second (FPS) and floating point operations per second
   (FLOPS) are displayed on the terminal

Below is a screenshot of the terminal after one simulation:

.. Image:: /images/Gravit-screenshot_version_01_00_00.png

Display Output
==============

-  Particles are set to rotate around a gravity center positioned at the
   center of the LCD screen
-  Particles are represented with 3D coordinates, projected to a 2D LCD
   screen. The projection is simplified such that the camera (or the
   viewer) does not change display angles.

Below is an example display of a 500-particle simulation:

.. Image:: /images/Gravit-displayshot_version_01_00_00.jpg

Useful References
=================

Main Gravit website: https://gravit.slowchop.com/

Gravit github: https://github.com/gak/gravit

Physics algorithm behind gravit, Barnes-hut:
`https://en.wikipedia.org/wiki/Barnes-Hut_simulation <https://en.wikipedia.org/wiki/Barnes%E2%80%93Hut_simulation>`__

Bresenham's line algorithm:
`https://en.wikipedia.org/wiki/Bresenham's_line_algorithm <https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm>`__

