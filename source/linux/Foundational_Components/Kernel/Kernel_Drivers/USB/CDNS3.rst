###
USB
###

Introduction
************

The USB subsystem has a SuperSpeed (SS) USB3.1 Gen1 Dual-Role-Device (DRD)
controller with on-chip SS (USB3.1 Gen1) PHY and HS/FS/LS (USB2.0) PHY.

.. note::
    LowSpeed (LS) is only supported in host mode.

TI SoC Integration
******************

The USB subsystem is integrated in TI |__PART_FAMILY_NAME__| devices.

EVM
***

.. ifconfig:: CONFIG_part_variant in ('J721E')

    The following diagram depicts USB integration in J721E EVM.

    .. image:: /images/usb_j721e_evm.png

    USB0 controller operates in super-speed dual role mode and is available on
    a Type-C connector.

    .. note::

       The Type-C config DIP switch (SW3) must be set for DRP (Dual-role-Port)
       operation. SW3.3 = OFF, SW3.4 = ON.

    USB1 operates in high-speed host mode and is connected to an onboard 4-port
    HUB.  Of the 4 hub ports, 2 ports are available on stacked Type-A connectors,
    1 is available on J2 header for USB-WiFi/Bluetooth adapter and 1 is available
    on the **EVM EXPANSION** connector J51.

    USB2 controller is not present on J721E SoC so micro-AB 3.0 connector is not
    usable.

.. ifconfig:: CONFIG_part_variant in ('J784S4, J742S2')

   The following diagram depicts USB integration in |__PART_FAMILY_NAME__| EVM.

   .. image:: /images/usb_j784s4_j742s2_evm.png

   The EVM supports one USB3.1 Gen1 Type C interface, which can function as DFP, UFP,
   or DRP.

   .. note::

      The Type-C config DIP switch (SW2) must be set for DRP (Dual-role-Port)
      operation. SW2.3 = ON, SW2.4 = OFF.

   The EVM supports two USB2.0 Type A interfaces via an on-board USB hub. These ports
   can only function as Host. The processor supports a single USB interface. Therefore,
   the user must configure for either the USB3.1 Type C interface or the USB2.0 Type A
   interface. Both cannot be operated simultaneously.

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   The following diagram depicts USB integration in |__PART_FAMILY_NAME__| EVM.

   .. image:: /images/usb_j721s2_evm.png

   The EVM supports one USB3.1 Gen1 Type C interface, which can function as DFP, UFP, or
   DRP. The EVM supports two USB2.0 Type A interfaces via an on-board USB hub. These
   ports can only function as Host.

   .. note::

      The Type-C config DIP switch (SW3) must be set for DRP (Dual-role-Port)
      operation. SW3.3 = OFF, SW3.4 = ON.

   The processor supports a single USB interface. Therefore, the user must configure
   for either the USB3.1 Type C interface or the USB2.0 Type A interface. Both cannot
   be operated simultaneously.

.. ifconfig:: CONFIG_part_variant in ('J7200')

   The following diagram depicts USB integration in |__PART_FAMILY_NAME__| EVM.

   .. image:: /images/usb_j7200_evm.png

   The EVM supports one USB3.1 Gen1 Type C interface, which can function as DFP, UFP,
   or DRP.  USB Super speed signals from SERDES0 port of J7200 SoC are connected to
   USB Type C interface.  The EVM also supports two USB2.0 Type A interfaces via an
   on-board four port USB hub. These ports can only function as Host.

   .. note::

      The Type-C config DIP switch (SW3) must be set for DRP (Dual-role-Port)
      operation. SW3.3 = OFF, SW3.4 = ON.

   Ports of the HUB are connected as below.

   - Two USB ports are terminated to Type A Stacked Connector
   - One USB port is connected to 4 Pin Header (PCIe Card - Wi-Fi®/BT)
   - One USB port is connected to EVM Expansion connector

   J7200 EVM only supports single USB interface, so the USB3.1 and USB2.0 cannot be
   supported simultaneously.

.. ifconfig:: CONFIG_part_variant in ('J722S')

   The following diagram depicts USB integration in |__PART_FAMILY_NAME__| EVM.

   .. image:: /images/usb_j722s_evm.png

   .. note::

      The Type-C config DIP switch (SW2) must be set for DRP (Dual-role-Port)
      operation. SW2.2 = OFF, SW2.3 = OFF.

   The EVM supports up to four USB3.0 Gen1 interfaces, three Type A ports plus
   one USB3.0 Gen1 port on the Type C port. The USB3.0 ports are connected to
   on-board USB hub and support only DFP mode. The Type C port has option
   (and defaults) to support USB2.0 multiple roles (DFP/UFP/DRP). This provides
   support for the USB boot modes of the processor.

   Type C port can be configured using IO expander port P05 USB2.0_MUX_SEL.

   - USB2.0_MUX_SEL = 0 ( USB2.0 (DFP/UFP/DRP) )
   - USB2.0_MUX_SEL = 1 ( USB3.0 (DFP) )

.. ifconfig:: CONFIG_part_family in ('AM64X_family')

   **AM64X_EVM**

   The following diagram depicts USB integration in |__PART_FAMILY_NAME__| EVM.

   .. image:: /images/usb_am64xx_evm.png

   The following image shows the top view of |__PART_FAMILY_NAME__| EVM.

   .. image:: /images/am64xx_evm.png

   The USB controller operates in USB2.0 dual role mode on |__PART_FAMILY_NAME__|
   EVM with a microAB receptacle (labeled as J24).

   A 2x3 header (labeled as J23) is provided on |__PART_FAMILY_NAME__|
   EVM to configure the port for host-only mode. Connecting Pin 1 and 2 to enable
   bulk capacitance on VBUS, and connecting Pin 5 and 6 to ground the ID pin.

   **SK-AM64B**

   The following diagram depicts USB integration in SK-AM64B.

   .. image:: /images/usb_am64xx_skevm.png

   On SK-AM64B, USB 3.0 HOST Interface is offered through USB
   Type-A Connector which supports data rate up-to 5Gbps.

   USB3.0 lines from Type-A connector are connected to the SERDES-0 block of SoC
   via choke and ESD protection device. USB2.0 Lines of the Type-A Connector are
   directly interfaced to the USB0 port of AM64x SOC.
