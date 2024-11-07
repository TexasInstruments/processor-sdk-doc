
OMAP-L137/C6747 EVM Hardware Setup Guide
======================================

Setting up the Hardware
-----------------------

Follow the steps below to setup the hardware and enable communication
with the EVM.

.. Note:: The EVM is sensitive to static discharges. Use a grounding strap or other device to prevent damaging the board. Be sure to connect communication cables before applying power to any equipment.

-  Verify that the EVM board's SW2 (Boot) switch is correctly set. The
   setting to boot from SPI0 Flash are:

+----------------+-----+-----+-----+-----+-----+
| **Pin #**      | 7   | 2   | 1   | 0   | 3   |
+================+=====+=====+=====+=====+=====+
| **Position**   | 0   | 1   | 0   | 1   | X   |
+----------------+-----+-----+-----+-----+-----+

.. Note:: All boot switch modes can be found in the EVM Technical Reference Manual at the link provided under the Additional Resources section.

-  If you want to use networking, connect the Ethernet cable to one of
   the Ethernet ports on the EVM board and to an Ethernet network port.

-  Connect the USB cable provided in the kit to the on-board emulation
   USB port on the board (EMBED USB). Connect the other end to a
   computer with CCS installed.

-  If you plan to use UART port for a console window, connect the RS-232
   null modem cable to the EVM UART port and to the COM port of your
   host workstation.

-  Connect the power cable to the EVM power jack on the board. To be ESD
   safe, plug in the other end of the power cable only after you have
   connected the power cord to the board.

Connecting to a Console Window
--------------------------------

You can open a console window that allows you to watch boot and serial
console messages by following these steps:

1. Connect a serial cable between the serial port on the EVM and the
   serial port (for example COM1) on a PC.
2. Run a terminal session (such as Minicom on Linux or TeraTerm on
   Windows) on the workstation and configure it to connect to that
   serial port with the following characteristics:

   -  Bits per Second: 115200
   -  Data Bits: 8
   -  Parity: None
   -  Stop Bits: 1
   -  Flow Control: None
   -  Transmit delay: 0 msec/char, 100 msec/line

**For Linux**

3. When you power on the EVM, you will see boot sequence messages (If
   you have a boot loader in flash). You can press a key to interrupt the boot sequence and type
   commands in the U-Boot command shell.


Connecting to CCS
-------------------

.. Note:: CCS versions 9.0 and later are 64-bit applications. Due to this, the on-board Spectrum Digital XDS510USB emulator is not supported. The alternatives are to either stay with CCS 8.3 or earlier, or use an external emulator with CCS 9.0. For example, the low cost XDS110 emulator for $99 (http://www.ti.com/tool/TMDSEMU110-U).

Target Configuration
^^^^^^^^^^^^^^^^^^^^^^

-  Open CCS and select New->Target Configuration File.
-  Specify a file name or use default.
-  Select "Spectrum Digital XDS510USB Emulator" as Connection. **If using CCS 9.0 or later, you will need an external emulator as noted above.**

.. Image:: /images/OMAPL137_targetConfig.png


-  Check "OMAPL137" or "C6747" as Device and save.

.. Tip:: If you don't see "OMAPL137", ensure that you have installed CCS and selected Single Core DSP devices in the installation.

-  Open Target Configuration view in CCS by selecting "Window -> Show
   View -> Target Configurations" from menu.
-  Select newly created configuration, right-click on it and set it as
   default.
-  Launch Target configuration file



Connect Target and Load/Run Program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Connecting Target

   -  Select "View -> Debug" from menu to start a debug session.
   -  CCS will switch to Debug perspective with devices DSP and ARM.
   -  Select device to connect and then go to "Run -> Connect Target"
      from menu.

.. Note:: OMAPL137 is a DSP boot master device. Hence to connect to the ARM, you need to connect the DSP first (even if you do not load anything to DSP), then connect ARM (Reason: DSP’s GEL file enables and wakes up the ARM).

-  Loading Program

   -  Choose desired device (DSP or ARM).
   -  Go to "Run -> Load -> Load Program" from menu.
   -  Click “Browse” to choose a prebuilt \*.out or click “Browse project..” to choose \*.out of the open projects.
   -  Choose desired \*.out and click OK.


-  Running Program

   -  Go to "Run -> Resume"

Additional References
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
EVM Design and Support Files: http://support.spectrumdigital.com/boards/evmomapl137/revg/
