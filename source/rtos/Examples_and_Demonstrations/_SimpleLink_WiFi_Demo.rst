.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_SimpleLink_WiFi_Demo


Overview
========

This page describes the SimpleLink WiFi Demo provided in the
Processor-SDK for RTOS. This demo illustrates the integration of CC3120
BoosterPack and AMIC110 ICE using components in the SDK to provides a
low cost WiFi solution for application development.


Supported platforms
===================

-  iceAMIC110 ( A8 )


Requirements
============

Following are required to run the application:

Hardware

-  TI CC3120 BoosterPack
-  TI EVM (see list above)
-  Blue wires between CC3120 BP and AMIC110 ICE
-  Serial UART cable (provided in EVM kit)
-  Connection Diagram

   .. Image:: /images/sl_wifi_demo_connection.jpg

-  Picture of connected EVMs

   .. Image:: /images/sl_wifi_demo_connected.jpg

Software

-  Processor-SDK RTOS 5.1.0 and later
-  Code Composer Studio 8.0 and later


Components Used
===============

RTOS Components:

-  SYS/BIOS
-  XDCTools
-  Processor SDK RTOS PDK: SPI, UART, GPIO LLDs, OSAL, Board etc.


Software Design
===============

The demo implemented a network terminal application to illustrate
how the SimpleLink WiFi Plugin for Processor SDK RTOS can be used to provide
a low cost solution for Sitara devies (AM3/4/5). The AMIC110 ICE and CC3120
BoosterPack are connected via SPI and GPIO pins. The SPI interface will provide
The data and command channels for SimpleLink WiFi Plugin, while the GPIO pins
are providing the INT and RESET signals.

The following diagram shows the overview of the demo:

.. Image:: /images/sl_wifi_demo_overview.jpg


The source files are organized as follows:

::

              └── simplelink-wifi-demo
                  ├── bin --> Folder for the executables
                  ├── examples --> Demo source code, projectspec file and makefile
                  ├── lib --> Folder for SimpleLink WiFi Plugin liraray
                  ├── source --> Folder for SimpleLink WiFi Plugin source


How to Build the SimpleLink WiFi Plugin Demo using CCS
=====================================

Please follow below step by step procedure to build the application.

#. Install Code Composer Studio.
#. Install Processor SDK RTOS for the respective platform needed, in a
   location where CCS expects: (by default $HOME/ti or c:/ti) Refer
   :ref:`Processor SDK RTOS Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>`
   for details.
#. Open CCS:
#. Click Project-->Import CCS Projects and select network_terminal_AMIC110_ICE_RTOS_ccs
   under directory :
   processor_sdk_rtos_<platform>_<version>/demos/simplelink-wifi-demo/
#. Build the application . ( By right clicking on imported project and
   clicking "Build project")

.. note::
   This will create executable binary under <CCS_Workspace>/network_terminal_AMIC110_ICE_RTOS_RTOS_ccs/Debug/network_terminal_AMIC110_ICE_RTOS_RTOS_ccs.out

.. Image:: /images/sl_wifi_demo_ccs_import.jpg


How to Build the SimpleLink WiFi Plugin Demo using makefile on Windows
=====================================

Please follow below step by step procedure to build the application.

#. Install Processor SDK RTOS for the respective platform needed, in a
   location where CCS expects: (by default c:/ti) Refer
   :ref:`Processor SDK RTOS Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>`
   for details.
#. Under DOS command prompt type:
#. cd processor_sdk_rtos_<platform>_<version>/ folder
#. setupenv.bat
#. cd processor_sdk_rtos_<platform>_<version>/demos/simplelink-wifi-demo/examples\rtos/AMIC110_ICE/demos/network_terminal/tirtos/ccs
#. gmake clean
#. gmake all
#. The executable binary will be generated under
   processor_sdk_rtos_<platform>_<version>/demos/simplelink-wifi-demo/examples\rtos/AMIC110_ICE/demos/network_terminal/tirtos/ccs and
   The executable network_terminal.out, boot image files network_terminal.bin and app will be under
   processor_sdk_rtos_<platform>_<version>/demos/simplelink-wifi-demo/bin/am335x/a8/debug


How to Build the SimpleLink WiFi Plugin Demo using makefile on Linux
=====================================

Please follow below step by step procedure to build the application.

#. Install Processor SDK RTOS for the respective platform needed, in a
   location where CCS expects: (by default $HOME/ti) Refer
   :ref:`Processor SDK RTOS Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>`
   for details.
#. Under Linux command prompt type:
#. cd processor_sdk_rtos_<platform>_<version>/ folder
#. source setupenv.sh
#. cd processor_sdk_rtos_<platform>_<version>/demos/simplelink-wifi-demo/examples\rtos/AMIC110_ICE/demos/network_terminal/tirtos/ccs
#. make clean
#. make all
#. The executable binary will be generated under
   processor_sdk_rtos_<platform>_<version>/demos/simplelink-wifi-demo/examples\rtos/AMIC110_ICE/demos/network_terminal/tirtos/ccs


How to Run the SimpleLink WiFi Plugin Demo using CCS
===================================

You will need the following:

#. Install Code Composer Studio to load and run the Template
   Application. Refer to :ref:`Processor SDK RTOS Getting Started
   Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>` for
   installing CCS.
#. AMIC110 ICE board
#. JTAG Emulator

To load and run SimpleLink WiFi Plugin Demo:

#. Connect the computer to the JTAG port on the board using the JTAG
   emulator.
#. Power on the EVM/board. Ensure that no boot mode is
   entered (do not have SD card loaded or QSPI flashed)
#. Open up a serial terminal for UART communication (Refer to :ref:`Processor
   SDK RTOS Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>`, setup
   EVM hardware)
#. Open CCS and launch target config file for the EVM (Refer to
   `Processor SDK RTOS Setup
   CCS <index_how_to_guides.html#setup-ccs-for-evm-and-processor-sdk-rtos>`__ for setting up CCS)
#. Connect to the primary core to make sure on connect gels are run
   A8 core for AM335x
#. Connect to core where the application is expected to run, if not the primary core.
#. Load executable by clicking("Run --> Load --> Load Program.). Click
   on Browse Project and select outfile under:
   <CCS_Workspace>/network_terminal_AMIC110_ICE_RTOS_RTOS_ccs/Debug/network_terminal_AMIC110_ICE_RTOS_RTOS_ccs.out
#. Run application by clicking the Run icon. ( Or Click Run --> Resume)

Now the network terminal demo will run and print progress through the UART.

-  The inital display on the UART
.. Image:: /images/sl_wifi_demo_uart_init.jpg

-  Enter "help" at UART prompt
.. Image:: /images/sl_wifi_demo_uart_help.jpg

-  Enter "scan -n 10" at UART prompt
.. Image:: /images/sl_wifi_demo_uart_scan.jpg

-  Enter " wlanconnect -s "dir645" -t WPA/WPA2 -p "12345678" " at UART prompt
.. Image:: /images/sl_wifi_demo_uart_wlanconnect.jpg

-  Enter "ping 192.168.0.1" at UART prompt
.. Image:: /images/sl_wifi_demo_uart_ping.jpg

.. note::
   This demo uses the D-Link DIR-645 wirless router with DHCP server. "dir645" is its SSID. "12345678" is its
   connection password. "192.168.0.1" is its default gateway. Users should adjust those parameters according
   to their own wireless routers.


How to Run the SimpleLink WiFi Plugin Demo using UART Boot
===================================

To load and run SimpleLink WiFi Plugin Demo:

#. Connect the J3 to the USB port on a PC via the UART to USB cable.
#. Power on the EVM/board.
#. Open up a serial terminal for UART communication (Refer to :ref:`Processor
   SDK RTOS Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>`, setup
   EVM hardware)
#. Send the bootloader_boot_uart_a8host_debug.bin under
   pdk_<platform>_<version>/packages/ti/starterware/binary/bootloader/bin/am335x-evm/gcc
   using the XMODEM.

   .. Image:: /images/sl_uart_boot_1st.jpg

#. Upon completion,  then send the network_terminal.bin under
   processor_sdk_rtos_<platform>_<version>/demos/simplelink-wifi-demo/bin/am335x/a8/debug
   using the XMODEM.

   .. Image:: /images/sl_uart_boot_2nd.jpg

Now the network terminal demo will run and print progress through the UART.

-  The inital display on the UART
.. Image:: /images/sl_wifi_demo_uart_init.jpg

-  Enter "help" at UART prompt
.. Image:: /images/sl_wifi_demo_uart_help.jpg

-  Enter "scan -n 10" at UART prompt
.. Image:: /images/sl_wifi_demo_uart_scan.jpg

-  Enter " wlanconnect -s "dir645" -t WPA/WPA2 -p "12345678" " at UART prompt
.. Image:: /images/sl_wifi_demo_uart_wlanconnect.jpg

-  Enter "ping 192.168.0.1" at UART prompt
.. Image:: /images/sl_wifi_demo_uart_ping.jpg

.. note::
   This demo uses the D-Link DIR-645 wirless router with DHCP server. "dir645" is its SSID. "12345678" is its
   connection password. "192.168.0.1" is its default gateway. Users should adjust those parameters according
   to their own wireless routers.

