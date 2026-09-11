.. http://processors.wiki.ti.com/index.php/Pin_Mux_Utility_for_ARM_MPU_Processors

Pin Mux Tools
==================================

.. rubric:: Introduction
   :name: introduction-linux-pinmux-utility

The TI PinMux Tool is a Cloud, Windows, or Linux-based software tool for
configuring pin multiplexing settings and I/O cell characteristics for
TI Processors. Pin multiplexing controls the routing of internal signals
to the external balls of the device while the I/O cell characteristics
include enabling of internal pull-up / pull-down resistors. The Pin Mux
Tool provides a graphical user interface for selecting the peripheral
interfaces that will be used in the system design. Its intelligent
solver atomatically selects pin combinations that help the designer make
sure there are no multiplexing conflicts. All selections and settings
can be saved as a pinmux design file which can be reloaded later.

.. rubric:: Disclaimer
   :name: disclaimer

**NOTE:** Although these utilities are tested and intended to be
accurate, they are provided ‘as is’ and are not guaranteed to provide
accurate results. In the event of a conflict between the device data
contained in this software tool and the device datasheet, the datasheet
shall take precedence. Please check configuration results against the
datasheet for your device to be assured your pinmux configuration is
*possible* and accurate. It is up to the user to verify all of the bits
in the registers based on the information in the device datasheet and
that all IOSETs selected by the tool are valid and supported. Although
we try to maintain backwards compatibility between PinMux Tool versions
it isn't guarunteed.

.. rubric:: Software User's Guide
   :name: software-users-guide

A quick overview of the TI PinMux Tool's UI and usage is available on
the main `PinMux Tool
Wiki <http://processors.wiki.ti.com/index.php/TI_PinMux_Tool_v4>`__. The
rest of this guide will focus on usage for the |__PRODUCT_LINE_NAME__| Processors.

.. rubric:: Release Notes
   :name: release-notes

`TI PinMux Tool Release
Notes <http://processors.wiki.ti.com/index.php/TI_PinMux_Tool_Release_Notes>`__

.. rubric:: Application Launch
   :name: application-launch

At launch the tool will present the option to start a new design or to
open an existing design. To start a new design use the drop-down menu
indicating which devices are supported by this installation of the
PinMux Tool. Select your device and click **Start**. Previously saved
designs can be opened too. Although we try to maintain backwards
compatibility between PinMux Tool versions, it isn't guaranteed.

.. rubric:: IOSETs
   :name: iosets

Timing restrictions make the concept of IOSETs an important subject for
|__PRODUCT_LINE_NAME__| Processors. The device datasheet timing specifications define the
relationship between clock lines and data lines. A peripheral instance
like McASP may be available on any number of pins but not all
combinations of clock and data pins may be available. We only define
IOSETs for combinations of pins that are guarunteed to meet the
datasheet timing requirements. Pin conflict errors will be raised if the
remaining available pins don't come together to build an IOSET or if
pins are manually selected that don't match a defined IOSET. **This is
why it is important to start your system design with the PinMux Tool
first before any schematic or board design is started.**

.. rubric:: Use Cases
   :name: use-cases

Some peripherals may expose Use Cases to allow you to quickly eliminate
the signals you won't need.

.. rubric:: Power Domain Checking
   :name: power-domain-checking

Some devices support dual-voltage inputs on the IO pins (VDDSHVx). The
PinMux Tool is capable of tracking the IO power supply domains of an SoC
and allows you to select which voltage is applied on the dual-voltage IO
rails. With this information the PinMux Tool can raise a voltage
conflict warning if a peripheral's IO requires a different voltage than
is applied to the dual-voltage IO rail.

.. rubric:: Changing Pad Configuration Parameters
   :name: changing-pad-configuration-parameters

Pad configuration parameters are used to set the values of other bit
fields in each Pad Configuration Register. The parameters are typically
for internal resistor pull and a check box for enabling receive
functionality. These configuration parameters are SoC specific and may
vary.

.. rubric:: RX Enable / Input Enable
   :name: rx-enable-input-enable

Most devices, K2G excluded, support the ability to disable the input
buffer on a pin. When the RX buffer is disabled the pin can still be
used as an output for clocks and GPIO but it cannot be used as an input
for any function. Many peripherals require the input buffer to be
enabled even if it is an output. Examples are I2C clock, MDIO clock, SPI
chip select, MMC/SD clock & cmd lines, etc. For the most part, the
PinMux Tool will not let you disable the input buffer on pins that
require it.

.. rubric:: Output File Formats
   :name: output-file-formats

Code files generated by the PinMux Tool vary by each device and its
requirements. They generally include C code for Processor SDK RTOS which
should be drop-in compatibile with the PDK Board Library. Reference the
`Processor SDK RTOS Board
Support <http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Board_Support>`__
page for more details. A partial devicetree format is generated for
Processor SDK Linux and that should be manually patched into the
reference devicetree file included with the `Linux
kernel  <../../Foundational_Components_Kernel_Users_Guide.html>`__.

Some devices will have a generic format that is intended for use with
:ref:`U-Boot <u-boot-user-guide>`.
These devices require pin multiplexing to be done once, in isolation,
and while executing from SRAM. U-boot takes care of this by applying pin
configurations while the MLO file (secondary bootloader) executes from
OCMC RAM. This guide will include how to convert the generic format for
U-boot.

.. rubric:: Processor SDK Linux
   :name: processor-sdk-linux

Recompiling u-boot is required after making updates. Instructions are
available in the :ref:`Linux Core U-Boot User's Guide <u-boot-user-guide>`.
Compiling the devicetree dts to dtb is also required after making
updates. Instructions are available in the `Linux Kernel Users
Guide <../../Foundational_Components_Kernel_Users_Guide.html#compiling-the-sources>`__.

.. rubric:: devicetree
   :name: devicetree

Edit the appropriate file in this directory:

.. ifconfig:: CONFIG_part_family in ('J7_family')

    ${SDK\_INSTALL\_DIR}\\board\_support\\linux-\*\\arch\\arm64\\boot\\dts\\${BOARD}.dts

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family')

    ${SDK\_INSTALL\_DIR}\\board\_support\\linux-\*\\arch\\arm\\boot\\dts\\${BOARD}.dts


.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family')

    .. rubric:: AM3 and AM4 u-boot
       :name: am3-and-am4-u-boot

    The PinMux Tool does not export any u-boot files for these devices. But
    the file below may still need to be modified.

    ${SDK\_INSTALL\_DIR}\\board\_support\\u-boot-\*\\board\\ti\\am335x\\mux.c

    ${SDK\_INSTALL\_DIR}\\board\_support\\u-boot-\*\\board\\ti\\am43xx\\mux.c


