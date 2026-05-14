PRU-ICSS Serial UART
--------------------

.. rubric:: Introduction

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   Linux supports the PRU HW UART peripheral within the Programmable Real-Time Unit Subsystem
   (PRUSS), which is based on the industry standard TL16C550.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   Linux supports the PRU HW UART peripheral within the Programmable Real-Time Unit (PRU) and
   Industrial Communication Subsystem - Gigabit (ICSSG) or PRU-ICSSG, which is based on the
   industry standard TL16C550.

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM57XX')

   Linux supports the PRU HW UART peripheral within the Programmable Real-Time Unit Subsystem
   and Industrial Communication Subsystem (PRU-ICSS), which is based on the industry standard
   TL16C550.

The kernel driver is at :file:`drivers/tty/serial/8250/8250_pruss.c`.

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

Therefore the device node /dev/ttyS1 is associated with PRUSS UART and
user-space applications can read/write to this serial port. For details,
please refer to :ref:`kernel uart driver usage <linux-kernel-omap-uart-driver-usage>`.

.. note::

   The index in ttyS1 could vary depending on the serial alias configuration
   in the device tree.

.. note::

   PRU cores do not need to be initialized in order for Linux to use the HW UART.
