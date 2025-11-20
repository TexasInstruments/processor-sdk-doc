###
USB
###

Introduction
************

The USB subsystem has a USB2.0 Dual-Role-Device (DRD) controller,
with on-chip  HS/FS/LS (USB2.0) PHY.

.. note::
    LowSpeed (LS) is only supported in host mode.


TI SoC Integration
******************

The USB subsystem is integrated in TI |__PART_FAMILY_NAME__| devices.

Starter Kit (SK)
****************

The two instances of USB controller present in AM62 SoC are brought on the Starter Kit(SK)
board. The zeroth instance is brought out with a Type C port(labelled as J13) through a
TPS65987D USB Type-C PD controller. The role detection is done by the PD controller
and updates are sent to the USB driver using the Role switch framework. The first
instance is brought out with a Type A port(labelled as J7).


.. rubric:: **Driver Configuration**
   :name: driver-configuration-dwc3

The default kernel configuration enables support for USB\_DWC3
and USB\_DWC3\_AM62 (the wrapper driver).

The selection of DWC3 driver can be modified as follows: start Linux
Kernel Configuration tool.

::

    $ make menuconfig  ARCH=arm64

-  Select Device Drivers from the main menu.

::

    ...
    Kernel Features  --->
    Boot options  --->
    CPU Power Management  --->
    Floating point emulation  --->
    Userspace binary formats  --->
    Power management options  --->
    [*] Networking support  --->
    Device Drivers  --->
    ...

-  Select USB support from the menu.

::

    ...
    Multimedia support  --->
    Graphics support  --->
    <M> Sound card support  --->
    HID support  --->
    [*] USB support  --->
    < > Ultra Wideband devices  ----
    <*> MMC/SD/SDIO card support  --->
    ...

-  Enable Host-side support and Gadget support

::

    ...
    <M>   Support for Host-side USB
    ...
    <M>   USB Gadget Support
    ...


-  Select DesignWare USB3 DRD Core Support and Texas Instruments AM62
   Platforms

::

    ...
    <M>   DesignWare USB3 DRD Core Support
     DWC3 Mode Selection (Dual Role mode)  --->
     *** Platform Glue Driver Support ***
    ...
    <M>     Texas Instruments AM62 Platforms
    ...

-  Select 'xHCI HCD (USB 3.0) SUPPORT' from  menuconfig in 'USB support'

::

    < >     Support WUSB Cable Based Association (CBA)
    *** USB Host Controller Drivers ***
    ...
    <*>     xHCI HCD (USB 3.0) support
    ...

-  Select 'USB Gadget Support --->' from menuconfig in 'USB support' and
   select the needed gadgets. (By default all gadgets are made as
   modules)

::

    --- USB Gadget Support
    [ ]   Debugging messages (DEVELOPMENT)
    [ ]   Debugging information files (DEVELOPMENT)
    [ ]   Debugging information files in debugfs (DEVELOPMENT)
    (2)   Maximum VBUS Power usage (2-500 mA)
    (32)  Number of storage pipeline buffers
    [ ]   Serial gadget console support
          USB Peripheral Controller  --->
    <M>   USB Gadget functions configurable through configfs
    [*]     Generic serial bulk in/out
    [*]     Abstract Control Model (CDC ACM)
    [*]     Object Exchange Model (CDC OBEX)
    [*]     Network Control Model (CDC NCM)
    [*]     Ethernet Control Model (CDC ECM)
    [*]     Ethernet Control Model (CDC ECM) subset
    [*]     RNDIS
    [*]     Ethernet Emulation Model (EEM)
    [*]     Mass storage
    [*]     Loopback and sourcesink function (for testing)
    [*]     Function filesystem (FunctionFS)
    [*]     Audio Class 1.0
    [ ]     Audio Class 1.0 (legacy implementation)
    [*]     Audio Class 2.0
    [*]     MIDI function
    [*]     HID function
    [*]     USB Webcam function
    [*]     Printer function
          USB Gadget precomposed configurations  --->
