PRU-ICSS Soft UART
------------------

.. rubric:: Introduction

As of Processor SDK Linux v6.1, AM335x supports up to 6 additional UARTs
through PRU-ICSS GPIO pins. The UART function is implemented in PRU firmware.
The firmware is self-contained in the same PRU, which means the firmware does
not use shared resources within an ICSS including IEP timer and Scratchpad.


.. rubric:: PRU Soft UART Features

Up to 3 independent UARTs are supported per PRU with the following features:

  - Common baud rates up to 115200 Mbps
  - 5, 6, 7, or 8-bit characters per transfer
  - 1, 1.5, or 2 stop bit generation
  - Even, odd, or none parity bit generation and detection
  - Auto-RTS/CTS based harware flow control
  - Full-duplex communication


.. rubric:: PRU Soft UART Unsupported Features

The following features are not supported in PRU Soft UART:

  - Full modem control
  - Software flow control


.. rubric:: PRU Soft UART Pin Configuration

The PRU GPIO pins are assigned for the functional pins of each UART port. The
PRU GPIO pin assignment is specified in the "ti,pru-suart-pins" properties in
the device tree bindings.

The device tree "ti,pru-suart-pins" property contains 2 or 4 byte values. The
first two values are for TXD and TXD pins, and next two values are optional
which are for CTS and RTX pins. The value is the index of the PRU GPIOs defined
in PRU R30 and R31.

For details please refer to the kernel device tree binding doc:

.. code-block:: text

   Documentation/devicetree/bindings/serial/pru-suart.txt

The Processor SDK Linux kernel also provides an device tree example for
Beaglebone Black:

.. code-block:: text

   arch/arm/boot/dts/am335x-boneblack-prusuart.dts

This example defines the 3 UARTs on PRU0 without hardware flow control and 3
UARTs on PRU1 with hardware flow control. All the UART pins are available on
the Beaglebone Black expansion headers.


.. rubric:: PRU Soft UART driver Kernel Config

The PRU Soft UART Linux kernel driver depends on the PRU-ICSS kernel driver. So
the following kernel Kconfig options should be enabled to use the PRU Soft UART
module.

.. code-block:: menuconfig

   Device Drivers  --->
      SOC (System On Chip) specific Drivers  --->
         [*] TI SOC drivers support  --->
            <M> TI PRU-ICSS Subsystem Platform drivers

   Device Drivers  --->
      Character devices  --->
         Serial drivers  --->
            <M> TI PRU Software UART suppor


