.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_CAN_Eth_Gateway_Demo

Overview
========

Gateway is one of the major use-cases in the modern cars. Performance
requirements for Gateway applications are ever increasing due to advanced
connected car architecture having multiple domain controllers. The CAN - Ethernet
gateway demo showcases P2P (Protocol to Protocol) translation i.e. translating data
and control information between incompatible networks like Ethernet and CAN for
communication on AM65xx device. The demo enables full duplex
routing between CAN and Ethernet (CAN to Ethernet & Ethernet to CAN).
The gateway demo shows handling of high bandwidth data traffic on Cortex-R5 with
low CPU load and latency for bridging application leaving cortex A53 free
for application processing.

Architecture Overview
=====================

The following block diagram shows the various functional blocks & the data flow
used in the gateway application. As shown in the diagram the PC Ethernet
applications are used for transmitting & receiving the Ethernet frames from/to
PC, similarly for CAN message reception & transmission, any compatible CAN tool
can be used.

.. Image:: /images/can-eth-gateway.png
   :height: 1000px
   :width: 1500px
   :scale: 50 %
   :alt: can-to-eth data flow
   :align: center

Software Features
=================

-  Routing application for CAN to Eth and Eth to CAN.
-  Network APIs for creating TCP/IP applications.
-  CPU load benchmark utils.

Directory Structure
===================

The CAN_ETH Gateway demo is located in the Processor SDK RTOS
release under the directory path

::

    [SDK Install Path]/processor_sdk_rtos_[soc]_[version]/demos/gateway-demos/can-eth-gateway

Detailed description of the directory structure is given below:

-  output - directory contains prebuilt out file and PC tools executables.
-  build - directory contains makefiles and SYSBIOS configuration, linker files for build
-  pctools - directory contains Ethernet PC tools
-  src - Source files for gateway application, utils and network APIs.

.. note::

    * Only Linux PC tools pre-built binaries are provided. For Windows, user needs
      to build it locally.

Components Used
===============

RTOS Components:

-  SYSBIOS
-  XDC
-  NDK

Processor SDK RTOS Drivers:

-  EMAC
-  NIMU
-  UART
-  Board
-  OSAL
-  CSL
-  udma
-  sciclient

Building the Demo
=================

The demo application is built using makefile. Also the demo is available pre-built
for Processor SDK RTOS version 5.3.0.0 or higher.

You must first set up your development environment. Refer to
the `Processor SDK RTOS Building <index_overview.html#building-the-sdk>`__ page for
information on setting up your build environment.

The following are steps to clean the demo:

::

     cd [SDK Install Path]/processor_sdk_rtos_[soc]_[version]/demos/gateway-demos/can-eth-gateway/build
     make clean BOARD=am65xx_idk

The following are steps to compile the demo:

::

     cd [SDK Install Path]/processor_sdk_rtos_[soc]_[version]/demos/gateway-demos/can-eth-gateway/build
     make all BOARD=am65xx_idk

Host Applications
==================

The PC tools for Ethernet reception and transmission are located under pctools
directory. These tools can be built for Linux and Windows.
::

     cd [SDK Install Path]/processor_sdk_rtos_[soc]_[version]/demos/gateway-demos/can-eth-gateway/pctools
     make all

Running the Demo
================

You will need the following:

+-----------------------+-------+
| EVM's supported       | Bare  |
|                       | metal |
+=======================+=======+
|  AM65xx EVM/IDK       |  No   |
+-----------------------+-------+

Tools
-----
#. CAN Receiver/Transmitter - PC tool to receive and transmit the CAN messages.
#. LAN Cable (preferably CAT6)
#. Gigabit switch connection - as mentioned in the known issues demo does not work
   with 100Mbps mode. The gigabit connection is needed to AM65xx EVM.

    .. note::

        * PCAN - PC CAN Emulation tool is used for testing CAN_ETH Gateway demo.
        * Refer section PCAN Tool Set up for more details.
        * For receiving and transmitting data over Ethernet, use/run "eth_rx.out" and "eth_tx.out" utilities on host PC.
        * Above utilities are available at "[SDK Install Path]/processor_sdk_rtos_[soc]_[version]/demos/gateway-demos/can-eth-gateway/pctools".

Set up
------

#. Code Composer Studio to load and run the demo. Refer to :ref:`Processor
   SDK RTOS Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>` for
   installing CCS.
#. AM65xx_EVM board with attached LAN cable and CAN tool.
#. USB cable for JTAG and serial terminal (micro USB port)
#. Configure PC running Ethernet PC tools with below static IP
    * IP Address = "192.168.1.20"
    * Subnet mask = "255.255.255.0"
    * Default Gateway = "192.168.1.1"


    .. note::

        You can enable DHCP for AM65xx board if PC is connected to network and static
        IP configuration is not feasible. Set enableStaticIP flag to 1 in

     ::

        [SDK Install Path]/processor_sdk_rtos_[soc]_[version]/demos/gateway-demos/can-eth-gateway/build/am65xx/nimuExample_r5.cfg

AM65x EVM/IDK Board Set up
----------------------------

#. Adding Termination Resistors to the MCAN Interface

    Reason for change
        * The IDK Application board has two MCAN ports. The termination for the MCAN ports is not installed by default. If the termination is needed on the board, the following steps can be followed to add it.

    Items Needed
        * Two 120 ohm resistors in 0603 package

    Modification
        * Carefully remove the IDK application board by removing the four screws and gently separating the board from the connectors.
        * On the top of the board, solder a 120 ohm resistor to the footprint for R252.

        .. Image:: /images/am65x_evm_idk_board_changes_for_mcan_interface1.png
          :height: 500px
          :width: 800px
          :scale: 50 %
          :alt: can-to-eth data flow
          :align: center

        * On the bottom of the board, solder a 120 ohm resistor to the footprint for R130.

        .. Image:: /images/am65x_evm_idk_board_changes_for_mcan_interface2.png
          :height: 500px
          :width: 800px
          :scale: 50 %
          :alt: can-to-eth data flow
          :align: center

        * Reinstall the IDK Application board and return the screws.

PCAN Tool Set up
----------------

CAN FD adapter PCAN-USB FD allows the connection of CAN FD and CAN networks to a computer via USB.
   Product details: https://www.peak-system.com/PCAN-USB-FD.365.0.html?&L=1

#. Prerequisite (PC Setup):
    * Download and install PCAN driver from: https://www.peak-system.com/quick/DrvSetup
    * Download and install PCAN driver from: https://www.peak-system.com/quick/DrvSetup
    * Download PCAN-View from: https://www.peak-system.com/fileadmin/media/files/pcanview.zip
    * PCAN-View is a GUI based tool used to configure bit-rate of the PCAN tool. It provides a convenient was to see sent and received messages. It also provides an option to enable tracing of CAN messages along with timestamp
    * Please refer to PCAN-USB FD manual for more details

.. note::

    Please check licensing information & terms of usage of PCAN-USB product and make sure it
    adheres your organizations policy before downloading the drivers.

#. PCAN Setup:
    * Once driver is installed, connect PCAN to PC. It should be auto detected as ‘PCAN-USB FD’ in ‘Device Manager’. If it is not auto detected then re-install the PCAN driver
    * Once it is detected in Device Manager, open PCAN-View and follow below steps
        * Click on ‘Connect’ from ‘CAN’ menu (as shown in below figure)
            * Popped up window shall show connected PCAN hardware. Select that device.
            * Tick in the checkbox shown next to ‘Data Bit rate’
                * This will enable Bit
            * Select ‘Nominal Bit Rate’ as ‘1 MBits/s’
            * Select ‘Data Bit Rate’ as ‘5 MBits/s’
                * Bit rates may vary from use-case to use-case.
            * Click on Ok button.

            .. Image:: /images/pcan_view_device_selection.png
               :height: 500px
               :width: 500px
               :scale: 50 %
               :alt: can-to-eth data flow
               :align: center

        * Create and send message at period of 2sec
            * Click on ‘New Message’ under ‘Transmit’ menu
            * Tick the check box present next to ‘CAN FD’
            * Tick the check box present next to ‘Bit Rate Switch’
            * Give below parameters /inputs:
                * ID as hex ‘004’
                * Length as ‘64’
                * Cycle Time as ‘2000’
                * Data: as use-case needs

            .. Image:: /images/CanEth_PCANViewTransmitMessageConfig.png
               :height: 500px
               :width: 600px
               :scale: 50 %
               :alt: can-to-eth data flow
               :align: center

#. Creating Bit Rate Configurations:
    * Example for creating 5 Mbps bit rate configuration for ‘Data Bit Rate’(shown in below diagram)
        * Click on ‘Connect’ under ‘CAN’ menu
        * Tick in the checkbox shown next to ‘Data Bit rate’
        * Click on Play button present below ‘Data Bit rate’ and then ‘Manage Bit rates’
        * Click on ‘Data’ in newly popped window
        * Select clock frequency as 80 MHz
        * Click on ‘Add’ button
        * Give caption as ‘5 MBits/s’
        * Program ‘Prescalar’, ‘tseg1’, ‘tseg2’, ‘Sync Jump Width’ as ‘1’, ‘12’, ‘3’, ‘1’ respectively.
        * Bit Rate text box shall show ‘5 Mbit/s’ after programming above values.
        * Click on ‘Ok’ and then again on ‘Ok’

    .. Image:: /images/CanEth_PCANViewBitRateConfig.png
      :height: 500px
      :width: 800px
      :scale: 50 %
      :alt: can-to-eth data flow
      :align: center


#. CAN Bus Connections:
    * CAN_H of all the nodes on the bus shall be connected together
    * Similarly CAN_L of all the nodes on the bus shall be connected together
    * Please refer to ‘PCAN-USB FD manual’ for more details about connections.

Load and run the demo
-------------------------

#. Connect the USB cable from your computer to the AM65xx_EVM's JTAG port
#. Power on the AM65xx_EVM board. Ensure that no boot mode is entered (do
   not have SD card loaded or QSPI flashed)
#. Open up a serial terminal for UART communication (Refer to :ref:`Processor
   SDK RTOS Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>`, setup
   EVM hardware)
#. Open CCS and launch target config file for AM65xx_EVM (Refer to
   `Processor SDK RTOS Setup CCS <index_how_to_guides.html#setup-ccs-for-evm-and-processor-sdk-rtos>`__ for setting up CCS)
#. Connect to MCU_PULSAR_Cortex_R5_0
#. Load the System firmware as specified in SCICLIENT documentation
#. Load and launch the demo executable:

    ::

     [PDK Install Path]/packages/ti/binary/gatewayapp/bin/am65xx_idk/gatewayapp_mcu1_0_release.xer5f

#. The application print will be displayed on the CCS and UART console. The UART console used depends on the core in which the application is run.
#. Confirm the network connectivity of PC with board.
   ping 192.168.1.4

CAN to ETH
^^^^^^^^^^
#. Connect the CAN PC tool.
#. Start the Ethernet receive application

    ::

       ./eth_tx.exe[or eth_tx.out] 192.168.1.4

#. Start CAN message transmission from the CAN tool with below information
    * ID as hex ‘004’
    * Length as ‘64’
    * Cycle Time as ‘2000’
    * Data can be any user specified data

ETH to CAN
^^^^^^^^^^

#. Connect the CAN PC tool.
#. Start the Ethernet transmit application

    ::

       ./eth_rx.exe[or eth_rx.out] --ip 192.168.1.4 [--port <portNum>] [--framerate <frames per seconds>]

        port and framerate are optional

#. Once Ethernet transmit application starts sending data out, CAN PC tool shall receive a CAN FD message with ID hex ‘009’

Terminal Screen-shot
====================

Below is a terminal output after one simulation:

::

    Board_init success

    GatewayApp: BOARD IP address I/F 1: 192.168.1.14

    GatewayApp: Starting GATEWAY Tasks...
    Gateway Tx: Server listening (port=1000) !!!

    GatewayApp: Network Tx socket open done..
    Gateway Tx: Server listening (port=2000) !!!

    GatewayApp: Network Rx socket open done..
    GatewayApp: CrossBar/Interrupt Configuration done.
    GatewayApp: MCANSS Revision ID:
    GatewayApp: scheme:0x1
    GatewayApp: Business Unit:0x2
    GatewayApp: Module ID:0x8e0
    GatewayApp: RTL Revision:0x5
    GatewayApp: Major Revision:0x1
    GatewayApp: Custom Revision:0x0
    GatewayApp: Minor Revision:0x1
    GatewayApp: CAN-FD operation is enabled through E-Fuse.
    GatewayApp: Endianess Value: 0x87654321

    GatewayApp: MCAN Transmitter app started..

    Received 0 Transmitted 0
    LOAD: CPU: 0.6% HWI: 0.1%, SWI:0.1%
    LOAD: TSK: Gateway Tx: 0.1%
    MISC: 0.3%

    GatewayApp: CAN stats - Received 500 Transmitted 500
    LOAD: CPU: 6.6% HWI: 0.5%, SWI:0.1%
    LOAD: TSK: Gateway Rx: 1.6%
    LOAD: TSK: Gateway Tx: 0.6%
    MISC: 3.8%

Known issues & limitations
--------------------------
#. Polling mode is not supported in the Gateway application.
#. Re-transmission of failed CAN message is not supported.
#. Ethernet 100Mbps is not supported. Gigabit only supported.

