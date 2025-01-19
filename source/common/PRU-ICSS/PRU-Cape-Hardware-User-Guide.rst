.. _pru_cape_hardware_user_guide:

PRU Cape Hardware User Guide
----------------------------

.. contents:: :local:

Introduction
^^^^^^^^^^^^

This document describes the hardware architecture of the PRU Cape
which is compatible with the Beagle Bone Black development platform.

|

Description
"""""""""""

The PRU Cape is a test, development, and evaluation module system that
enables developers to write software and develop hardware around the PRU
subsystem. Examples of basic I/O such as push buttons and LEDs as well
as more complicated examples such as audio and 1-Wire for temperature
sensing are available on this cape to showcase what the PRU can
accomplish in terms of inputs and outputs.

The following sections give more details regarding the PRU Cape.

|

EVM System View
"""""""""""""""

The PRU Cape is shown below.

.. image:: /images/PCB_Angle.PNG

|

Schematics/Design/Errata Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Design Files <https://www.ti.com/tool/prucape>`__ (located under
Technical Documents), includes:

- Schematic
- Layout
- Assembly Drawings
- CAD Files
- Bill of Materials (BOM)

**Errata**

- **I2C SCL and SDA signals swapped (REV 1.2A)**

  The AM335x I2C2\_SDA signal (routed to BBB Header P9-20) is connected to
  the EEPROM SCL pin. The AM335x I2C2\_SCL signal (routed to BBB Header
  P9-19) is connected to the EEPROM SDA pin. The EEPROM is blank, and if
  it is to be used, the cape needs to be modified to physically swap the
  SDA and SCL signals.

:ref:`pru_cape_getting_started_guide`

|

System Description
^^^^^^^^^^^^^^^^^^

System Board Diagram
""""""""""""""""""""

The system block diagram of the PRU Cape are shown in the below Figures.


|

PRU Cape Board Layout:

.. image:: /images/Board_Layout.JPG

|

PRU Cape Functional Block Diagram

.. image:: /images/System_Diagram.JPG

|

Signals Used
""""""""""""

+------------------------------+------------------------------+------------------------+------------------------+
| **CAPE NAME**                | **BBB HEADER NUMBER**        | **BBB MODE 0 NAME**    | **CAPE USE**           |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU0\_GPO0              | P9-31                        | MCASP0\_ACLKX          | PRU0 Blue LED          |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU0\_GPO1              | P9-29                        | MCASP0\_FSX            | PRU0 Green LED         |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU0\_GPO2              | P9-30                        | MCASP0\_AXR0           | PRU0 Orange LED        |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU0\_GPO3              | P9-28                        | MCASP0\_AHCLKR         | PRU0 Red LED           |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU1\_GPO3              | P8-44                        | LCD\_DATA3             | PRU1 Blue LED          |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU1\_GPO4              | P8-41                        | LCD\_DATA4             | PRU1 Green LED         |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU1\_GPO5              | P8-42                        | LCD\_DATA5             | PRU1 Red LED           |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU0\_GPI7              | P9-27                        | GPIO3\_19              | SW1                    |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU0\_GPI5              | P9-25                        | GPIO3\_21              | SW2                    |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU1\_GPO0              | P8-45                        | LCD\_DATA0             | Audio Data             |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU1\_GPO1              | P8-46                        | LCD\_DATA1             | Audio Clock            |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU1\_GPO2              | P8-43                        | LCD\_DATA2             | Audio Sync             |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_UART0\_TXD              | P9-24                        | UART1\_TXD             | UART TxD               |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_UART0\_RXD              | P9-26                        | UART1\_RXD             | UART RxD               |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_UART0\_RTS              | P9-21                        | UART2\_TXD             | UART RTS               |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_UART0\_CTS              | P9-22                        | UART2\_RXD             | UART CTS               |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU\_EDIO\_DATA\_OUT6   | P8-39                        | LCD\_DATA6             | LCD RS                 |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU\_EDIO\_DATA\_OUT4   | P8-28                        | LCD\_PCLK              | LCD E                  |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU\_EDIO\_DATA\_OUT0   | P9-18                        | I2C1\_SDA              | LCD Data4              |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU\_EDIO\_DATA\_OUT1   | P9-17                        | I2C1\_SCL              | LCD Data5              |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU\_EDIO\_DATA\_OUT2   | P8-27                        | LCD\_VSYNC             | LCD Data6              |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU\_EDIO\_DATA\_OUT3   | P8-29                        | LCD\_HSYNC             | LCD Data7              |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU\_EDIO\_DATA\_OUT5   | P8-30                        | LCD\_DE                | HDQ input              |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU0\_GPI14             | P8-16                        | GPIO1\_14              | HDQ output             |
+------------------------------+------------------------------+------------------------+------------------------+
| I2C2\_SDA                    | P9-20                        | I2C2\_SDA              | I2C SCL                |
+------------------------------+------------------------------+------------------------+------------------------+
| I2C2\_SCL                    | P9-19                        | I2C2\_SCL              | I2C SDA                |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_ECAP0\_IN\_PWM0\_OUT    | P9-42                        | ECAP0\_IN\_PWM0\_OUT   | ECAP0\_IN\_PWM0\_OUT   |
+------------------------------+------------------------------+------------------------+------------------------+
| PR1\_PRU0\_GPI15             | P8-15                        | GPMC\_AD15             | PRU0\_GPI\_15          |
+------------------------------+------------------------------+------------------------+------------------------+
| VDD\_3V3C                    | P9-3, P9-4                   | VDD\_3V3C              | VDD\_3V3C              |
+------------------------------+------------------------------+------------------------+------------------------+
| DGND                         | P8-1, P8-2, P9-1,P9-2        | DGND                   | DGND                   |
+------------------------------+------------------------------+------------------------+------------------------+
| DGND                         | P9-43, P9-44, P9-45, P9-46   | DGND                   | DGND                   |
+------------------------------+------------------------------+------------------------+------------------------+

Table: **Table 1. Signals Used**

|

PRU Cape Functional Block Descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section describes major functional blocks of the PRU Cape.

|

Audio
"""""

The audio portion of the PRU Cape is composed of a Dual 8-bit DAC
(DAC082S085) and a dual 105 mW Amplifier (LM4808). The output is then
sent to a 3.5 mm Audio jack with a max pk-pk of .89V, following the
consumer standard.

|

+-------------------+-------------------------+-----------------------+----------------+
| **CAPE NAME**     | **BBB HEADER NUMBER**   | **BBB MODE 0 NAME**   | **CAPE USE**   |
+-------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU1\_GPO0   | P8-45                   | LCD\_DATA0            | Audio Data     |
+-------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU1\_GPO1   | P8-46                   | LCD\_DATA1            | Audio Clock    |
+-------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU1\_GPO2   | P8-43                   | LCD\_DATA2            | Audio Sync     |
+-------------------+-------------------------+-----------------------+----------------+
+-------------------+-------------------------+-----------------------+----------------+

|

EEPROM
""""""

The EEPROM on the PRU cape is the CAT24C256WI-G EEPROM 256Kb I2C SOIC8,
and has an attached DIP switch to manipulate the I2Caddress. The first
78 bytes hold a file that the Beagle Bone Black will read to identify
the cape, the rest of the EEPROM is available for use.

|

+--------------------------+-------------------------+-----------------------+----------------------+
| **CAPE NAME**            | **BBB HEADER NUMBER**   | **BBB MODE 0 NAME**   | **CAPE USE**         |
+--------------------------+-------------------------+-----------------------+----------------------+
| I2C2\_SDA                | P9-20                   | I2C2\_SDA             | I2C SCL              |
+--------------------------+-------------------------+-----------------------+----------------------+
| I2C2\_SCL                | P9-19                   | I2C2\_SCL             | I2C SDA              |
+--------------------------+-------------------------+-----------------------+----------------------+
+--------------------------+-------------------------+-----------------------+----------------------+

eCAP
""""

These pins are brought out on the board that connect to the eCAP0 PWM0
IN to allow use of the PRU Subsystem's eCAP IP.

|

+-----------------------------+-------------------------+------------------------+------------------------+
| **CAPE NAME**               | **BBB HEADER NUMBER**   | **BBB MODE 0 NAME**    | **CAPE USE**           |
+-----------------------------+-------------------------+------------------------+------------------------+
| PR1\_ECAP0\_IN\_PWM0\_OUT   | P9-42                   | ECAP0\_IN\_PWM0\_OUT   | ECAP0\_IN\_PWM0\_OUT   |
+-----------------------------+-------------------------+------------------------+------------------------+
| PR1\_PRU0\_GPI15            | P8-15                   | GPMC\_AD15             | PRU0\_GPI\_15          |
+-----------------------------+-------------------------+------------------------+------------------------+

LCD
"""

The LCD screen is on a duaghter board with its own built in
controller, model number  NHD-0208AZ-RN-YBW-33V. The LCD is connected to
the PRU Cape throught the 2x8 female header in the middle of the cape.
The LCD is a 2x8 Character display operating at 3.3V.

|

+------------------------------+-------------------------+-----------------------+----------------+
| **Cape Name**                | **BBB Header Number**   | **BBB Mode 0 Name**   | **Cape Use**   |
+------------------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU\_EDIO\_DATA\_OUT6   | P8-39                   | LCD\_DATA6            | LCD RS         |
+------------------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU\_EDIO\_DATA\_OUT4   | P8-28                   | LCD\_PCLK             | LCD E          |
+------------------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU\_EDIO\_DATA\_OUT0   | P9-18                   | I2C1\_SDA             | LCD Data4      |
+------------------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU\_EDIO\_DATA\_OUT1   | P9-17                   | I2C1\_SCL             | LCD Data5      |
+------------------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU\_EDIO\_DATA\_OUT2   | P8-27                   | LCD\_VSYNC            | LCD Data6      |
+------------------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU\_EDIO\_DATA\_OUT3   | P8-29                   | LCD\_HSYNC            | LCD Data7      |
+------------------------------+-------------------------+-----------------------+----------------+

|

LEDs
""""

The PRU Cape has 7 surface mounted LEDs, including Red, Orange, Blue and
Green colors. There are 4 LEDs connected to PRU0 output, and 3 connected
to PRU1 output.

|

+-------------------+-------------------------+-----------------------+-------------------+
| **CAPE NAME**     | **BBB HEADER NUMBER**   | **BBB MODE 0 NAME**   | **CAPE USE**      |
+-------------------+-------------------------+-----------------------+-------------------+
| PR1\_PRU0\_GPO0   | P9-31                   | MCASP0\_ACLKX         | PRU0 Blue LED     |
+-------------------+-------------------------+-----------------------+-------------------+
| PR1\_PRU0\_GPO1   | P9-29                   | MCASP0\_FSX           | PRU0 Green LED    |
+-------------------+-------------------------+-----------------------+-------------------+
| PR1\_PRU0\_GPO2   | P9-30                   | MCASP0\_AXR0          | PRU0 Orange LED   |
+-------------------+-------------------------+-----------------------+-------------------+
| PR1\_PRU0\_GPO3   | P9-28                   | MCASP0\_AHCLKR        | PRU0 Red LED      |
+-------------------+-------------------------+-----------------------+-------------------+
| PR1\_PRU1\_GPO3   | P8-44                   | LCD\_DATA3            | PRU1 Blue LED     |
+-------------------+-------------------------+-----------------------+-------------------+
| PR1\_PRU1\_GPO4   | P8-41                   | LCD\_DATA4            | PRU1 Green LED    |
+-------------------+-------------------------+-----------------------+-------------------+
| PR1\_PRU1\_GPO5   | P8-42                   | LCD\_DATA5            | PRU1 Red LED      |
+-------------------+-------------------------+-----------------------+-------------------+
+-------------------+-------------------------+-----------------------+-------------------+

|


Switches
""""""""

The PRU Cape has two pushbutton switches connected to PRU0 inputs.

|

+-------------------+-------------------------+-----------------------+----------------+
| **CAPE NAME**     | **BBB HEADER NUMBER**   | **BBB MODE 0 NAME**   | **CAPE USE**   |
+-------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU0\_GPI5   | P9-27                   | GPIO3\_19             | SW1            |
+-------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU0\_GPI7   | P9-25                   | GPIO3\_21             | SW2            |
+-------------------+-------------------------+-----------------------+----------------+
+-------------------+-------------------------+-----------------------+----------------+

|

|

Temperature Sensor
""""""""""""""""""

The temperature sensor is a MAX31820 ambient temperature sensor, with a
1-Wire interface. Two pins are tied together from the PRU to create
input and output on a single wire.

|

+------------------------------+-------------------------+-----------------------+----------------+
| **CAPE NAME**                | **BBB HEADER NUMBER**   | **BBB MODE 0 NAME**   | **CAPE USE**   |
+------------------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU\_EDIO\_DATA\_OUT5   | P8-30                   | LCD\_DE               | HDQ input      |
+------------------------------+-------------------------+-----------------------+----------------+
| PR1\_PRU0\_GPI14             | P8-16                   | GPIO1\_14             | HDQ output     |
+------------------------------+-------------------------+-----------------------+----------------+
+------------------------------+-------------------------+-----------------------+----------------+

|

Test Space
""""""""""

The test space is a set of 150 through holes (15x10). There is no
connection between the through holes and is meant for attaching a
through hole component, wheather it be an IC or passive to test with the
PRU or any signal that can be accessed through the Cape Headers.

|

UART
""""

There is one RS-232 connector (DB9 male) on the PRU Cape. The MAX3232ECD
is the line driver/receiver.

|

+-------------------+-------------------------+-----------------------+----------------+
| **CAPE NAME**     | **BBB HEADER NUMBER**   | **BBB MODE 0 NAME**   | **CAPE USE**   |
+-------------------+-------------------------+-----------------------+----------------+
| PR1\_UART0\_TXD   | P9 24                   | UART1\_TXD            | UART TxD       |
+-------------------+-------------------------+-----------------------+----------------+
| PR1\_UART0\_RXD   | P9 26                   | UART1\_RXD            | UART RxD       |
+-------------------+-------------------------+-----------------------+----------------+
| PR1\_UART0\_RTS   | P9 21                   | UART2\_TXD            | UART RTS       |
+-------------------+-------------------------+-----------------------+----------------+
| PR1\_UART0\_CTS   | P9 22                   | UART2\_RXD            | UART CTS       |
+-------------------+-------------------------+-----------------------+----------------+

|

Legal
"""""

-  `Standard Terms and Conditions for Evaluation
   Modules </images/7/7c/Sszz027h.pdf>`__

