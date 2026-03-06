J742S2 EVM Hardware Setup
=========================

.. rubric:: Description

The J742S2 Evaluation Module provides an affordable platform to quickly
start evaluation of Jacinto™ DRA8xx Processors and accelerate development
for ADAS, Gateway and many other edge analytics applications.

.. rubric:: J742S2 EVM

Whereas other J7 family boards consist of a Common Processor Board plus SOM, the J742S2 Evaluation Module (EVM) has these
two components combined into a single board. The J742S2 EVM is the main board which includes the following:

- J742S2 SoC
- Leo PMIC (Power controller)
- 16 (2x8) GiB LPDDR4 RAM
- XSPI NOR flash

In addition, the J742S2 EVM has peripherals to provide most common functionality. It has expander ports to
connect to different adapter cards. Following is the image of the EVM with the J742S2 SoC:

.. figure:: /images/j742s2_evm_front.png
   :scale: 75%

   J742S2 EVM Front

.. figure:: /images/j742s2_evm_back.png
   :scale: 75%

   J742S2 EVM Back

Contents of the board

#. 4xUART to USB port for Main uarts

   - Port0 from this is used this for Linux, RTOS UART terminal from A72

#. 2xUART to USB port MCU domain uarts

   - Port0 from this is used for Cortex M4F UART
   - Port1 from this is used for MCU R5F UART

#. 6x CAN FD Interfaces
#. MCU Domain Ethernet (CPSW2G) port
#. Main Domain Ethernet (CPSW2G) port
#. MIPI JTAG connector
#. SD card slot
#. XDS110 on board USB JTAG connector
#. USB Host ports
#. Quad Port Ethernet daughter card (bottom of EVM) **sold separately**
#. 2x Display (eDP/DP) ports

   - Display0 is used by software for eDP/DP output

#. USBC port
#. 12V Power input
#. Power switch

Refer to `EVM connections <J742S2_EVM_Hardware_Setup.html#evm-connections>`__
for detailed information regarding connecting peripherals to the EVM

.. rubric:: Switch settings

Bootmodes are selected using the SW11 and SW7 switches on the EVM.
Most common boot method is to use SD card. Following are the switch settings to
set the boot mode to SD for the EVM.

   SW11[1-8] = 1000 0010
   SW7[1-8]  = 0000 0000

.. Image:: /images/K3-J784S4-EVM-Switch-SD-boot.png

When you want the binaries to be loaded from a debugger like CCS, the common
processor boards has to be set in the NO boot mode.  Following are the switch settings
to do the same.

   SW11[1-8] = 1000 1000
   SW7[1-8]  = 0111 0000

.. Image:: /images/K3-J784S4-EVM-Switch-NO-boot.png

.. rubric:: EVM connections

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

4. Connect ethernet at the RJ45 connector in the commonProcBoard as shown.
5. Insert micro SD card at the slot shown in the "J742S2 EVM Back" image
6. Connect the XDS110 connector if you want to run RTOS demos or use CCS.
7. Connect a 1080p HDMI monitor to the HDMI port on the Infotainment
   daughter card.

.. note::
    For Linux demos, keep the bootswitch settings in SD mode
    For Gateway demos, keep the bootswitch settings in noboot mode

8. Connect a 12V power supply
9. Power on the board
