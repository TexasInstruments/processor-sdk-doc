.. include:: <isonum.txt>

.. http://ap-fpdsp-swapps.dal.design.ti.com/index.php/Processor_SDK_RTOS_IOLINK_FIRMWARE

Introduction
============

| PRU-ICSS IOLINK serves as an example for firmware-based IOLINK Master
  Frame Handler support. The Processor SDK package includes
  full source code for IOLINK FW.

|

FIRMWARE FEATURES
=================

IOLINK FW supports 8 channels per IO-Link instance in a single PRU core.
Each channel uses three GPI/O pins from the PRU-ICSS module. The IOLINK
TXD and TX_EN pins are implemented using two GPO pins, the IOLINK RXD
pin is implemented using a single GPI pin.

Following are high-level IOLINK FW features:

+-----------------------------------+-----------------------------------+
| **Feature**                       | **Remarks**                       |
+-----------------------------------+-----------------------------------+
| No. of instances                  | 1                                 |
+-----------------------------------+-----------------------------------+
| No. of channels per instance      | 8                                 |
+-----------------------------------+-----------------------------------+
| Baud Rate                         | COM1/COM2/COM3                    |
+-----------------------------------+-----------------------------------+
| Minumum Cycle Time                | 400 |micro|\ s                    |
+-----------------------------------+-----------------------------------+
| Maximum Cycle Time                | 132 ms                            |
+-----------------------------------+-----------------------------------+
| Channel Independent Cycle Time    | Supported                         |
+-----------------------------------+-----------------------------------+
| Receive Buffer                    | 1 buffer of 68 bytes              |
+-----------------------------------+-----------------------------------+
| Transmit Buffer                   | 2 buffer of 68 bytes              |
+-----------------------------------+-----------------------------------+
| Channel Independent Time Control  | Supported                         |
| and Monitoring                    |                                   |
+-----------------------------------+-----------------------------------+
| Receive Glitch Filter and 8x      | Supported                         |
| Oversampling                      |                                   |
+-----------------------------------+-----------------------------------+
| Receive Tolerance (per baud rate) | 3%                                |
+-----------------------------------+-----------------------------------+
| Programmable Max Response Time TA | Supported                         |
+-----------------------------------+-----------------------------------+
| Start/Restart/Stop                | Supported                         |
+-----------------------------------+-----------------------------------+
| Start Bit                         | 1-bit                             |
+-----------------------------------+-----------------------------------+
| Stop Bit                          | 1-bit                             |
+-----------------------------------+-----------------------------------+
| Data Length                       | 8-bit                             |
+-----------------------------------+-----------------------------------+
| Parity Check                      | Even Parity                       |
+-----------------------------------+-----------------------------------+
| Interrupts that the CPU can use   | 1                                 |
+-----------------------------------+-----------------------------------+


Firmware Organization
=====================

+-------------------------+--------------------------------------------------------+
| **FW Item**             | **Directory**                                          |
+-------------------------+--------------------------------------------------------+
| Source code             | <PDK>/packages/ti/drv/iolink/firmware/icss_iolink/src  |
+-------------------------+--------------------------------------------------------+
| Design Guide            | <PDK>/packages/ti/drv/iolink/docs                      |
+-------------------------+--------------------------------------------------------+
| Firmware binaries       | <PDK>/packages/ti/drv/iolink/firmware/icss_iolink/bin  |
+-------------------------+--------------------------------------------------------+

|

Firmware Build Instruction
==========================

Build instruction from Processor SDK Release package
----------------------------------------------------

.. rubric::  Pre-requisites to Building
   :name: pre-requisites-to-building

Refer to the Processor SDK RTOS Building page for information on setting up the build environment.

.. rubric::  Compiling IOLINK FIRMWARE
   :name: compiling-iolink-firmware

-  cd <PDK>/packages/ti/drv/iolink
-  make firm

Firmware binaries at the end of the build will be located at:

-  <PDK>/packages/ti/drv/iolink/firmware/<FIRMWARE_TYPE>/bin/<SOC>/<HOST_CORE>/<REVISION>

-  <FIRMWARE_TYPE> indicates the firmware type i.e. icss_iolink

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
   -  Git clone iolink repo into ti/drv directory. i.e.
      <WORK_DIR/ti/drv/iolink>

-  Setting Environment Variables

   -  Export CLPRU install path. i.e. export CL_PRU_INSTALL_PATH=clpru
      toolchain directory
   -  Export pdk install path. i.e. export PDK_INSTALL_PATH=<WORK_DIR>
   -  Export LIMIT_SOCS Variable i.e. LIMIT_SOCS=<SOC> [Optional for
      limiting to some SOCs]

-  Build command

   -  Run make firm_clean/firm to clean/build firmware from iolink
      directory i.e. <WORK_DIR/ti/drv/iolink>

-  Generated binaries

   -  the firmware binaries which will be located in
      <WORK_DIR/ti/drv/iolink/firmware/<FIRMWARE_TYPE>/bin/<SOC>/<HOST_CORE>/<REVISION>>

|

Supported EVMs
==============

Supported EVMs are listed below.

+-------------+---------------------+-------------------+
| EVM Name    | PRU-ICSS Instances  | PRU-ICSS Revision |
+=============+=====================+===================+
| idkAM437x   | ICSS0               | REV1              |
+-------------+---------------------+-------------------+



|


.. rubric::  Firmware Design Guide
   :name: firmware-design-guide

+-----------------------------------+--------------------------------------------------------------------------+
| **Document**                      | **Location**                                                             |
+-----------------------------------+--------------------------------------------------------------------------+
| IOLINK FIRMWARE Design Guide      | <PDK>/packages/ti/drv/iolink/docs/IOLINK_FW_DESIGN_GUIDE.pdf             |
+-----------------------------------+--------------------------------------------------------------------------+

**NOTE: For normal use of IOLINK FW, there is no need to refer to the design guide.
This document can be cosulted in case of interest in details of internal firmware
operation, or a desire to modify the firmware.**

|

