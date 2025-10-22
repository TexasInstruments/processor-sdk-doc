.. http://processors.wiki.ti.com/index.php/Linux_Core_MUSB_User%27s_Guide

USB MUSB
---------------------------------

.. rubric:: **Quick Start Guide**
   :name: quick-start-guide

This section is a quick guide on how to start using usb ports on TI
platform with supplied pre-built binaries. Please refer to `USB Quick
Start <http://processors.wiki.ti.com/index.php/Am335x-USB-quick-start>`__

.. rubric:: **Introduction**
   :name: introduction-linux-core-musb-ug

The USB User's Guide provides information about

-  Overview of USB hardware and software
-  Supported linux driver features for USB host and device mode of
   operation
-  The Linux USB configuration through menuconfig. Please refer to `USB
   configuration <http://processors.wiki.ti.com/index.php/UsbgeneralpageLinuxCore>`__

.. rubric:: **Hardware Overview**
   :name: hardware-overview

.. rubric:: USBSS Overview
   :name: usbss-overview

-  The USB subsystem includes

-  Two instances of USB (Mentor Graphic's USB2.0 OTG) controllers. Each
   MUSB controller supports USB 1.1 and USB 2.0 standard.
-  CPPI 4.1 compliant DMA controller sub-module with 30 RX and 30 TX
   simultaneous DMA channels
-  CPPI 4.1 DMA scheduler
-  CPPI Queue Manager module with 92 queues for queuing/dequeuing
   packets

-  Interfaces to the CPU via 3 OCP interfaces

-  Master OCP HP interface for the DMA (for data transfers)
-  Master OCP HP interface for the Queue manager (to manage CPPI
   descriptors)
-  Slave OCP MMR interface (for CPU to access USBSS/MUSB registers)

-  Signals the standard Charge Pump (part of EVM BOM) for VBUS 5V
   generation

.. rubric:: **MUSB Controller Overview**
   :name: musb-controller-overview

The salient features of the MUSB USB2.0 OTG controller are:

-  High/full speed operation as USB peripheral.
-  High/full/low speed operation as Host controller.
-  Compliant with OTG spec.
-  15 Transmit and 15 Receive Endpoints other than the mandatory Control
   Endpoint 0.
-  Double buffering support in FIFO.
-  Support for high bandwidth Isochronous transfer
-  32 Kilobytes of Endpoint FIFO RAM for USB packet buffering.
-  Interfaced with CPPI4.1 DMA controller with 15 Rx and 15 Tx channels
   (for each usb controller).
-  Defer interrupt enable feature is supported for each packet
   descriptor of cppi-dma.

.. rubric:: **Software Overview**
   :name: software-overview

.. rubric:: **Mentor graphics controller driver (or MUSB driver)**
   :name: mentor-graphics-controller-driver-or-musb-driver

The MUSB driver is implemented on top of Mentor controller IP which
supports all the speeds (High, Full and Low). AM33XX USBOTG subsytem
uses CPPI 4.1 DMA for all the transfers. The musb driver conforms to
linux usb framework and supports both PIO and DMA mode of operation. The
musb host controller driver (HCD) binds the controller hardware to linux
usb core stack. The musb device or gadget controller driver binds the
controller hardware and specific gadget driver (filestorage, cdc/rndis
etc).

.. rubric:: **Linux USB Stack Architecture**
   :name: linux-usb-stack-architecture

As shown in the figure, linux usb stack is a layered architecture, with
musb controller at the lowest layer, the musb host/device controller
driver binds the musb controller hardware to linux usb stack framework.
The CPPI4.1 DMA controller driver is responsible for transmit/receive of
packets over the musb endpoints.

.. Image:: /images/Usb-stack-arch-image.JPG

.. rubric:: **Driver Features List**
   :name: driver-features-list

-  The Mentor USB driver can be built as module or built-in to kernel
-  Support both PIO and DMA mode (The DMA mode not applicable for
   control endpoint)
-  Support two instances musb controller in otg mode (both usb0 and usb1
   controller in otg mode. This will allow host or device operation on
   each port simultaneously.

.. rubric:: **The driver supports the following features for USB Host
   (AM33XX)**
   :name: the-driver-supports-the-following-features-for-usb-host-am33xx

+--------------------------------------------------------------------------------------------------------------+-----------+
| Host Mode Feature                                                                                            | AM33xx    |
+==============================================================================================================+===========+
| HUB class support                                                                                            | **Yes**   |
+--------------------------------------------------------------------------------------------------------------+-----------+
| `Human Interface Class (HID) <http://processors.wiki.ti.com/index.php/Usbgeneralpage#USB_HID_Class>`__       | **Yes**   |
+--------------------------------------------------------------------------------------------------------------+-----------+
| `Mass Storage Class (MSC) <http://processors.wiki.ti.com/index.php/Usbgeneralpage#Mass_Storage_Driver>`_ _   | **Yes**   |
+--------------------------------------------------------------------------------------------------------------+-----------+

Table:

.. rubric:: **The driver supports the following features for USB Gadget
   (AM33XX)**
   :name: the-driver-supports-the-following-features-for-usb-gadget-am33xx

+--------------------------------------------------------------------------------------------------------------+-----------+
| Gadget Mode Feature                                                                                          | AM33xx    |
+==============================================================================================================+===========+
| `Mass Storage Class (MSC) <http://processors.wiki.ti.com/index.php/Usbgeneralpage#Mass_Storage_Gadget>`__    | **Yes**   |
+--------------------------------------------------------------------------------------------------------------+-----------+
| `USB Networking - RNDIS <http://processors.wiki.ti.com/index.php/Usbgeneralpage#CDC.2FRNDIS_gadget>`__       | **Yes**   |
+--------------------------------------------------------------------------------------------------------------+-----------+
| `USB Networking - CDC <http://processors.wiki.ti.com/index.php/Usbgeneralpage#CDC.2FRNDIS_gadget>`__         | **Yes**   |
+--------------------------------------------------------------------------------------------------------------+-----------+

Table:

.. rubric:: **The driver supports the following features for Dual
   host/gadget (AM33xx)**
   :name: the-driver-supports-the-following-features-for-dual-hostgadget-am33xx

+------------------------------------------------------------------------------------------------------------------------+-----------+
| Dual Mode Feature                                                                                                      | AM33x     |
+========================================================================================================================+===========+
| `USB0 as OTG, USB1 as OTG <http://processors.wiki.ti.com/index.php/UsbgeneralpageLinux-v3p1#Driver_configuration>`__   | **Yes**   |
+------------------------------------------------------------------------------------------------------------------------+-----------+

Table:

.. rubric:: **Not verified features of AM33xx**
   :name: not-verified-features-of-am33xx

+-------------------------+--------------------+
| Not verified features   | am33x              |
+=========================+====================+
| **Wifi support**        | **Not verified**   |
+-------------------------+--------------------+
| **Serial device**       | **Not verified**   |
+-------------------------+--------------------+

Table:

.. rubric:: **Known limitations**
   :name: known-limitations

.. ifconfig:: CONFIG_part_family in ('AM335X_family')

        -  musb\_am335x.ko can't be removed (and we don't allow that to happen)
           to workaround a known hwmod issue.

.. rubric:: **References**
   :name: references

-  For more details about EVM, please refer to `EVM reference
   manual <http://www.ti.com/tool/tmdxevm3358>`__.

.. rubric:: **USB Configuration through menuconfig**
   :name: usb-configuration-through-menuconfig

-  The Mentor USB driver can be built as module or built into kernel.
   For more information refer to `USB
   configuration <http://processors.wiki.ti.com/index.php/UsbgeneralpageLinuxCore>`__

