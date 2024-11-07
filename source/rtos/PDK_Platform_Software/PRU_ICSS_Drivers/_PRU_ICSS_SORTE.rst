
Introduction
============

| The Simple Open Real-time Ethernet protocol (SORTE) serves as an
  example for Texas Instruments programmable approach to real-time
  communication for input/output (IO) networks with a maximum of 254
  devices. This protocol is fully documented and released in source
  code. It is open to customers to learn, adapt and enhance the protocol
  for their application requirements. SORTE is not bound to a given
  communication standard and breaks some of the limits of existing
  standards such as minimum Ethernet frame size, addressing and error
  detection. The primary use case of the protocol is to connect
  different end-equipment using Ethernet physical layer devices and 100
  Mbit Ethernet cable.

Protocol Overview
=================

The SORTE protocol is a TI-developed industrial Ethernet protocol that
supports 4-µs cycle time. The SORTE protocol operates on the PRU-ICSS,
which is an industrial peripheral within Sitara and KeyStone processors
from Texas Instruments. SORTE protocol operates exclusively on the
PRU-ICSS; therefore, the ARM Cortex-A8, A9 or A15 processors – depending
on the device family – are available for industrial applications. The
SORTE protocol differentiate between two network components: the master
and one or more slave devices. For in depth details of the protocol
please refer to the the design documents as listed in the References
section below.

Code Organization
=================

THE SORTE ARM application and firmware sources can be found under the
following directory :

**<PDK>/packages/ti/drv/pruss/example/apps/sorte/**

Refer to the README.txt in this directory for details of directory
layout.

In addition, there is a README.txt which provides high-level over of how
the protocol is implmented for master and slave device network
compoments which can be found at:

**<PDK>/packages/ti/drv/pruss/example/apps/sorte/firmware/src/master/README.txt**

**<PDK>/packages/ti/drv/pruss/example/apps/sorte/firmware/src/slave/README.txt**

|

Building the Examples
=====================

Pre-requisites to Building
--------------------------

#. Set your environment using pdksetupenv.sh. Building the Firmware
   binaries and ARM application uses the same environment variables as
   the pruss driver library build. Refer to the `Processor SDK RTOS
   Building <index_overview.html#building-the-sdk>`__ page for
   information on setting up your build environment.

Compiling the PRUSS SORTE Firmware
----------------------------------

To build the SORTE firmware binaries:

#. **cd <PDK>/packages/ti/drv/pruss**
#. **make firm**

This will make the firmware binaries which will be located in:

**<PDK>/packages/ti/drv/pruss/example/apps/sorte/firmware/bin/<BOARD>**

|

Compiling the PRUSS SORTE Application
-------------------------------------

To build the SORTE ARM applications:

#. **cd <PDK>/packages/ti/drv/pruss**
#. **make apps**

This will make the ARM applications for both master and slave device
which will be located in:

**<PDK>/packages/ti/drv/pruss/example/apps/sorte/slave<BOARD>**

**<PDK>/packages/ti/drv/pruss/example/apps/sorte/master<BOARD>**

|

Supported EVMs
==============

The following is a list of EVMS supported and the PRU-ICSS ethernet
ports to be used:

+--------------+-----------------------+-----------+-----------+
| **EVM Name** | **PRU-ICSS Instance** | **Port0** | **Port1** |
+--------------+-----------------------+-----------+-----------+
| icev2AM335x  | PRU-ICSS instance 1   | J2        | J1        |
+--------------+-----------------------+-----------+-----------+
| idkAM437x    | PRU-ICSS instance 2   | J6        | J9        |
+--------------+-----------------------+-----------+-----------+
| idkAM571x    | PRU-ICSS instance 2   | J6        | J8        |
+--------------+-----------------------+-----------+-----------+
| idkAM572x    | PRU-ICSS instance 2   | J6        | J8        |
+--------------+-----------------------+-----------+-----------+
| iceK2G       | PRU-ICSS instance 2   | J8A       | J8B       |
+--------------+-----------------------+-----------+-----------+

|

Running the PRUSS SORTE Example
===============================

In order to run the SORTE applications, you will require 1 EVM running
as master and 2 EVMs running as slave(slave1/slave2). Use CCS to load
and run the master and slave applications respectively.

Prior to running the applications its best to connect the EVMS as
follows:

Connect master Port0 to slave1 Port0. Connect slave1 Port1 to slave2
Port0.

After loading the application binaries from CCS, run the master first,
then run the slave2, finally run the slave1 with Port0 connecting to the
the master Port 0.

Note that the master device will wait until it discovers 2 slave devices
in the network. UART console on the master will print the following
until 2 slave devices are detected:

**sorte master: waiting for atleast 2 SLAVE devices connected**

Once 2 slave devices are detected by the master, the following print
will be seen on UART console and master will continue with state machine
and protocol processing:

**sorte master: 2 SLAVE devices connected**

The slave device via the UART console will continuosly display the
number of packets its received during input output exchange state of the
protocol until pass criteria is reached as follows(as an example):

**sorte slave: test in progress: current receive packet count: 35000**

**sorte slave: test in progress: current receive packet count: 40000**

Once pass criteria number of packets have been received, the following
print will be displayed on UART console:

**All tests have passed**

|

|

Additional Reference
====================

+-----------------------------------+-----------------------------------+
| **Document**                      | **Location**                      |
+-----------------------------------+-----------------------------------+
| SORTE Master with PRU-ICSS        | http://www.ti.com/tool/TIDEP-0085 |
| Reference Design                  |                                   |
+-----------------------------------+-----------------------------------+
| SORTE Slave Device with PRU-ICSS  | http://www.ti.com/tool/TIDEP-0086 |
| Reference Design                  |                                   |
+-----------------------------------+-----------------------------------+

|

