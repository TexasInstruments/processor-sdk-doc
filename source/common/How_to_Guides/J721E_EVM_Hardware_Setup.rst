J721E EVM Hardware Setup
====================================================

.. rubric:: Description
   :name: description

The J721E Evaluation Module provides an affordable platform to quickly
start evaluation of Jacinto™ DRA8xx Processors and accelerate development
for Infotainment, ADAS, Gateway and many other automotive
applications.

The J721E Evaluation Module consists of a SoM(System on Module) and a
common processor board.

.. rubric:: J7ES SOM
   :name: j7es-som

System on Module is a small board which has the SoC specific socket and
other important platform specific hardware like PMIC, DDR memory, etc

There are 2 variants. Following are the images of EVMs with different versions
of SoM:

1. Alpha board

.. note::
    Alpha EVMs have "Interim PMIC" sticker on the SoM board.

.. Image:: /images/J721E_Alpha_Board_1.jpg

.. Image:: /images/J721E_Alpha_Board_2.jpg

2. Beta board

.. note::
    Beta EVMs don't have a "Interim PMIC" sticker on the SoM board.

.. Image:: /images/J721E_Beta_Board.jpg


Contents of the board

- J721e SoC
- Power controller
- 4 GiB DDR RAM
- OSPI NOR flash
- Hyperflash

.. rubric:: Common Processor Board
   :name: common-proc-board

Common Processor Board is the main board which has peripherals to provide
most common functionality. It allows to connect to different adapter cards.

Common Processor Board with ALPHA-SOM

.. Image:: /images/K3-Common-Proc-Board-with-Alpha-som.png

Common Processor Board with BETA-SOM

.. Image:: /images/K3-Common-Proc-Board-with-Beta-som.png

Contents of the board

Refer to `EVM connections <J721E_EVM_Hardware_Setup.html#evm-connections>`__
for detail information regarding connecting peripherals to Common Processor Board

- 12V Power input
- 4xUART to USB port for Main uarts
- 2xUART to USB port MCU domain uarts
- 5x Ethernet ports
- 2x Display ports
- 2x FPDlink display connectors
- 7x 3.5mm audio jacks
- 2x PCIe connectors
- SD card slot
- 8GiB eMMC

.. rubric:: Infotainment daughter card
   :name: ivi-daughter-card

Infotainment daughter card is adapter board which has additional peripherals for
infotainment use cases. This has support for HDMI display, FPDlink display
extra audio channels, CSI camera, etc

.. Image:: /images/K3-Infotainment-card.png

Contents of the board

- 14x 3.5mm audio jacks
- 2x FPDlink display connectors
- Parallel port Omnivision camera connector
- CSI camera connector
- HDMI display connector

.. rubric:: GESI daughter card
   :name: gesi-daughter-card

GESI(Gateway/Ethernet Switch/ Industrial) daughter card is adapter board which
has additional peripherals for gateway and industrial use cases.
This has support for extra ethernet ports and CAN ports, etc

.. Image:: /images/K3-GESI-card.png

Contents of the board

- 5x ethernet ports
- Profinet connector
- Motor control headers
- Additional CAN headers

.. rubric:: Switch settings
   :name: switch-settings

Most common boot method is to use SD card. Following are the switch settings to
set the boot mode to SD for common processor board.

.. Image:: /images/K3-J721E-EVM-Switch-SD-boot.png

When you want the binaries to be loaded from a debugger like CCS, the common
processor boards has to be set in the NO boot mode.  Following are the switch settings
to do the same.

.. Image:: /images/K3-J721E-EVM-Switch-NO-boot.png

.. rubric:: EVM connections
   :name: evm-connections

Connect Following peripherals for working with processor SDK Linux

1. MAIN_UART is a USB connector to connect 4x main UART devices,
   this will register /dev/ttyUSB[0-3] in your Linux machine.
2. MCU_UART is a USB connector to connect 2x mcu UART devices.
   this will register /dev/ttyUSB[4-5] in your Linux machine.

.. note::
    Connect the MAIN_UART and MCU_UART in order so that the device numbers
    are assigned correctly.

3. Connect a Display Port 1080p monitor to the Display0 port of the
   commonProcBoard.

.. note::
    Only the monitor with preferred resolution as 1080p shall
    be used, any other resolution is not supported.

4. Connect ethernet at the RJ45 connector[4] in the commonProcBoard as shown.
5. Insert micro SD card at the slot shown in ][5]
6. Connect the XDS110 connector[6] if you want to run RTOS demos or use CCS.
7. Connect a 1080p HDMI monitor to the HDMI port[7] port on the Infotainment
   daughter card.

.. note::
    For Linux demos, keep the bootswitch settings in SD mode
    For Gateway demos, keep the bootswitch settings in noboot mode

8. Connect a 12V power supply
9. Power on the board
