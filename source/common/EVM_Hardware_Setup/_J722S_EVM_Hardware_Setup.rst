J722S EVM Hardware Setup
====================================================

.. rubric:: Description

The J722S evaluation module (or TDA4VEN and AM67 EVM) is a stand-alone test and development platform
built around the J722S system-on-a-chip (SoC). J722S processors are comprised of a quad-core 64-bit
Arm®-Cortex®-A53 microprocessor, dual-core Arm Cortex-R5F microcontroller (MCU).
The EVM gives developers the basic resources needed for most general‐purpose type projects.

.. rubric:: J722S EVM

.. figure:: /images/j722s_evm_front.png
   :scale: 75%

   J722S EVM Front

.. figure:: /images/j722s_evm_back.png
   :scale: 75%

   J722S EVM Back


Key Features of EVM

- J722S SoC
- 20V DC nominal supply (Max output current 5A)
- 1x 8GB LPDDR4 memory
- 1x Octal‐SPI NOR flash, 512Mb memory
- 512Mb Octal NAND
- eMMC flash memory (32GB memory)
- XDS110 Emulator support
- 1x Display Port Interface (DP0 from eDP bridge)
- DVI (v1.0) via HDMI Type A, supports 1080p
- 4x UART terminals via 1x USB FTDI (UART‐over‐USB)
- 1x Gigabit Ethernet (RJ45 Connector)
- 3x CAN Headers, full CAN‐FD support
- 4x 22‐Pin Flex Cable Interface (CSI‐4L)
- 2x 40‐pin High Speed Connector
- Audio Line in and MIC + Headphone out
- USB3.1 (Gen1) Hub to 3x Type A (Host)
- USB3.1 (Gen1) Type C (DFP,UFP modes)
- USB2.0 Micro B (for Quad UART‐over‐USB Transceiver)
- USB 2.0 Micro B (for XDS110)

Expansion and Add-on support

- 1‐Lane PCIe Card Slot Gen3
- Fan Header(12V)
- 40‐pin Header (2x20)
- 4x CSI‐RX ports support over QSH connector for Add on Card
- LVDS Display connector (OLDI)
- DSI Display connector

Refer to `EVM connections <J722S_EVM_Hardware_Setup.html#evm-connections>`__
for detailed information regarding connecting peripherals to the EVM

.. rubric:: Switch settings

Bootmodes are selected using the SW3 and SW4 switches on the EVM.
Most common boot method is to use SD card. Following are the switch settings to
set the boot mode to SD for the EVM.

   SW3[1:8] = 1100 0010
   SW4[1:8] = 0100 0000

.. Image:: /images/K3-J722S-EVM-Switch-SD-boot.png
   :scale: 50%

When you want the binaries to be loaded from a debugger like CCS, the common
processor boards has to be set in the NO boot mode.  Following are the switch settings
to do the same.

   SW3[1:8] = 1101 111
   SW4[1:8] = 0000 0000

.. rubric:: EVM connections

Connect Following peripherals for working with processor SDK Linux

1. USB connector (J6) connect to 4x UART devices that are registered
   as /dev/ttyUSB[0-3] in your Linux machine.
2. MAIN_UART and MCU_UART are muxed through the same USB connector(J6).
   MAIN_UART is /dev/ttyUSB2 and MCU_UART is /dev/ttyUSB0
3. Connect a Display Port 1080p monitor to the Display0 port of the
   EVM (J19).
4. Connect ethernet at the RJ45 connector (J11) in the EVM as shown.
5. Insert micro SD card at the slot shown in (J38)
6. Connect the XDS110 connector (J15) if you want to run RTOS demos or use CCS.
7. Connect a 1080p HDMI monitor to the HDMI port (J19) on the EVM.
8. Connect a 12V C-type power supply (J24)
9. Power on the board
