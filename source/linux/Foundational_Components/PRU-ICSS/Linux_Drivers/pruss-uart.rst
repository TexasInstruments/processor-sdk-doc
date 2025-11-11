PRU-ICSS Serial UART
--------------------

.. rubric:: Introduction

As of Processor SDK v7.1, Linux supports the PRU UART peripheral within the
PRU-ICSS, which is based on the industry standard TL16C550.
The kernel driver is at drivers/tty/serial/8250/8250_pruss.c.


.. rubric:: Support Devices

- |__PART_FAMILY_NAME__|


.. rubric:: Supported Driver Features

- Baud rates up to 12Mbps
- Hardware flow control


.. rubric:: Unsupported Driver Features

- DMA support


.. rubric:: Kernel Config

The PRUSS UART Linux kernel driver depends on the PRU-ICSS kernel drivers. So
the following kernel Kconfig options should be enabled to use the PRUSS UART
module.

.. code-block:: menuconfig

   Device Drivers  --->
      SOC (System On Chip) specific Drivers  --->
         [*] TI SOC drivers support  --->
            <M> TI PRU-ICSS Subsystem Platform drivers

   Device Drivers  --->
      IRQ chip support  --->
         <M> TI PRU-ICSS Interrupt Controller

   Device Drivers  --->
      Character devices  --->
         Serial drivers  --->
            <M> TI PRU-ICSS UART support


.. rubric:: Example DT configuration

From am335x-evmsk.dts

.. code-block:: dts

   &pruss_uart {
      prus = <&pru0>;
      ti,pru-interrupt-map = <0 6 2 2>;
      pinctrl-names = "default";
      pinctrl-0 = <&prussuart_pins>;
      status = "okay";
   };


.. rubric:: Driver Usage

Once the driver is probed, kernel log shows the following message.

.. code-block:: dmesg

   [   28.617700] 4a328000.serial: ttyS1 at MMIO 0x4a328000 (irq = 77, base_baud = 12000000) is a 16550A

Therefore the device node /dev/ttyS1 is associated to the PRUSS UART, user
space application can read/write this serial port. For detalls please refer
to :ref:`kernel uart driver usage <linux-kernel-omap-uart-driver-usage>`.

.. note::

    The index in ttyS1 could vary depending on the serial alias configuration
    in the device tree.


