
TMDXEVM6670L EVM Hardware Setup
=======================================

This page will walk you through setting up your
`TMDSEVM6670L <http://www.ti.com/tool/tmdsevm6670>`__
Evaluation Module (EVM). These guidelines also apply to the LE and LXE
EVM models.

.. note:: Some of the steps in this section have been updated from those used in the EVM *Quick Start Guide*.

Hardware Setup Overview
-----------------------

The picture below shows the TMDXEVM6670L EVM and the locations of
relevant switches and connectors.

.. image:: /images/TMD6670L.jpg


Hardware Setup Steps
--------------------

.. note:: The EVM board is sensitive to electrostatic discharges (ESD). Use a grounding strap or other device to prevent damaging the board. Be sure to connect communication cables before applying power to any equipment.

|
| **1. Attach the Ethernet cable**
| Using the Ethernet cable supplied, connect one end of the cable to the Ethernet port on the EVM and the other end to your PC.

|
| **2. Connect the JTAG interface**
| Use the USB to USB mini-B cable provided. Connect the USB mini-B connector to the USB mini-B interface on the EVM and the USB connector to your PC. This enables XDS-100 emulation and is directly useable by CCS. If you are using a different JTAG, connect it now.

|
| **3. Verify Endian mode in the SW3 settings**
| The Endian mode should be set to Little Endian. SW3 also contains the boot device settings.

.. image:: /images/TMD6678LSW3.png
   :scale: 40%

|
| **4. Verify boot mode in the SW3 - SW6 settings**
| The boot mode settings below enable NOR boot by loading the boot loader from EEPROM address 0x51.

.. image:: /images/TMD6678LSW3-6.png
   :scale: 40%

|
| **5. Set User Switch 2 for the demo application**
| The application needs an IP address. It can use either a static IP address (pre-configured) or it can request one using DHCP. This is controlled by setting User Switch 2 to ON for DHCP and OFF for Static.  See SW9.

.. image:: /images/TMD6670LSW9.png

|
| **6. Attach the serial port cable**
| This EVM can use either a USB serial port or the standard DB-9 (use the cable shipped with the platform). By default the shunts which control this on the platforms are set to use the USB by default. We recommend changing them to use the DB-9 as there are no known issues with this approach.

| To change the shunts refer to the picture below.

.. image:: /images/TMD6670LShunts.jpg

.. note:: If the USB serial port output does not work, ensure that the cable is connected directly to a USB port on the PC/laptop rather than going through an extender or USB hub.

|
| **7. Connect the power cable**
| Connect the power cable to the EVM power jack on the board. To be ESD safe, plug in the other end of the power cable only after you have connected the power cord to the board. Then turn on the board.

|

Boot Mode Dip Switch Settings
-----------------------------

The EVM supports booting image from various devices (EEPROM, NAND or
NOR) via IBL, it also supports ROM Boot modes, such as Ethernet, SRIO,
PCIe, etc. Below is the table showing the boot mode dip switch settings
for different boot mode that the EVM supports:

+----------------+----------------+----------------+----------------+----------------+
| Boot Mode      | DIP SW3        | DIP SW4        | DIP SW5        | DIP SW6        |
|                |                |                |                |                |
|                | (Pin1, 2, 3,   | (Pin1, 2, 3,   | (Pin1, 2, 3,   | (Pin1, 2, 3,   |
|                | 4)             | 4)             | 4)             | 4)             |
+================+================+================+================+================+
| IBL NOR boot   | (off, off, on, | (on, on, on,   | (on, on, on,   | (on, on, on,   |
| on image 0     | off)\ :sup:`1, | on)\ :sup:`3`  | off)\ :sup:`4` | on)            |
| (default)      | 2`             |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| IBL NOR boot   | (off, off, on, | (off, on, on,  | (on, on, on,   | (on, on, on,   |
| on image 1     | off)           | on)            | off)           | on)            |
+----------------+----------------+----------------+----------------+----------------+
| IBL NAND boot  | (off, off, on, | (on, off, on,  | (on, on, on,   | (on, on, on,   |
| on image 0     | off)           | on)            | off)           | on)            |
+----------------+----------------+----------------+----------------+----------------+
| IBL NAND boot  | (off, off, on, | (off, off, on, | (on, on, on,   | (on, on, on,   |
| on image 1     | off)           | on)            | off)           | on)            |
+----------------+----------------+----------------+----------------+----------------+
| IBL TFTP boot  | (off, off, on, | (on, on, off,  | (on, on, on,   | (on, on, on,   |
|                | off)           | on)            | off)           | on)            |
+----------------+----------------+----------------+----------------+----------------+
| I2C POST boot  | (off, off, on, | (on, on, on,   | (on, on, on,   | (on, on, on,   |
|                | off)           | on)            | on)            | on)            |
+----------------+----------------+----------------+----------------+----------------+
| ROM SPI        | (off, on, off, | (on, on, on,   | (on, on, off,  | (off, on, on,  |
| Boot\ :sup:`8` | off)           | on)            | on)            | on)            |
+----------------+----------------+----------------+----------------+----------------+
| ROM SRIO       | (off, off, on, | (on, on, on,   | (on, off, on,  | (off, off, on, |
| Boot\ :sup:`5` | on)            | off)           | off)           | on)            |
+----------------+----------------+----------------+----------------+----------------+
| ROM Ethernet   | (off, on, off, | (on, on, on,   | (on, off, on,  | (off, off, on, |
| Boot\ :sup:`6` | on)            | off)           | off)           | on)            |
+----------------+----------------+----------------+----------------+----------------+
| ROM PCIE       | (off, on, on,  | (on, on, on,   | (on, on, on,   | (off, on, on,  |
| Boot\ :sup:`7` | off)           | on)            | off)           | on)            |
+----------------+----------------+----------------+----------------+----------------+
| No boot        | (off, on, on,  | (on, on, on,   | (on, on, on,   | (on, on, on,   |
|                | on)            | on)            | on)            | on)            |
+----------------+----------------+----------------+----------------+----------------+

|

**Footnotes:**

| 1. Pin 1 of SW3 is the endian pin, by default, it is set to off (Little Endian)
|

| 2. Pin 2-4 of SW3 are the boot mode pins, by default it is set to I2C boot mode (off, on, off)
|

| 3. Pin 1-4 of SW4 and pin 1-2 of SW5 are the boot parameter index pins for I2C boot (paramter index 0/1 for NOR boot image 0/1, parameter index 2/3 for NAND boot image 0/1, parameter index 4 for TFTP boot). By default, image 0 is programmed to offset byte address 0x0 on NOR, and 0x4000 (block 1 start address) on NAND, image 1 is programmed to offset byte address 0xA00000 on NOR, and 0x2000000 on NAND.
|

| 4. Pin 4 of SW5 is the I2C address pin (off: 0x51, on: 0x50)  for I2C boot mode
|

| 5. This will set the board to boot from SRIO boot mode, with reference clock at 250 MHz, data rate at 3.125 GBs, and lane setup 4-1x ports and DSP System PLL at 122.88 MHz.
|

| 6. This will set the board to boot from Ethernet boot mode, with SerDes clock multiplier x 5, DSP System PLL clock at 122.88 MHz.
|

| 7. This will set the board to boot form PCIE boot mode, with PCIE in end point mode and DSP System PLL at 100 MHz.
|

| 8. This will set the board to boot from SPI NOR via the ROM code, with boot-table contents expected in the NOR. 24bit addressing has been set.
|
|

Please refer to
`Technical\_Reference\_Manual <http://www.advantech.com/Support/TI-EVM/6670le_sd.aspx>`__
for the boot mode switch settings on the board.

