Quality of Service (QoS)
########################

Much like with the `Advanced eXtensible Interface (AXI)`_ bus, the
Common Bus Architecture (CBASS) module in TI's K3 processors includes
Quality of Service (QoS) blocks which can be used to modify attributes
like the priority, Address Selection (ASEL), and Order ID (orderID)
values of the transactions spawning from initiator blocks to shape how
their traffic is routed and prioritized on the bus over other blocks on
the SoC.

.. _Advanced eXtensible Interface (AXI): https://en.wikipedia.org/wiki/Advanced_eXtensible_Interface

This concept allows us to prioritize traffic spawning from things like
the display subsystem where traffic congestion can be more noticeable
when traffic spikes occur during normal operation.

For example the Order ID can be used to route traffic through a
particular port when multiple ports exists on the crossbar for the
interface like with the DDR controllers. Most DDR controllers on K3
processors have two ports to the CBASS a high priority port and a second
for standard traffic. Setting an Order ID of 0 to 7 will route the
traffic through the standard port while a value of 8 to 15 will route
traffic through the high priority port and be serviced by the DDR
controller before standard traffic in a leaky-bucket priority based
round robin algorithm.

So setting an Order ID of 8 or higher for the display subsystem will
allow its traffic to use the DDR's high priority port and will help
minimize stuttering or jitter on the display which can be more
noticeable to end users.

More information about these QoS settings an be found in the Technical
Reference Manuals (TRM) of your processor.

Modifying QoS Defaults
======================

By default, the majority of transactions will default to the lowest
priority level (ASEL is 0 and Order ID is 0). During boot-up `U-Boot can
modify`_  the QoS settings for your board early on during boot-up using
the data generated from the `Sysconfig Tool`_ which you can download or
launch online `here`_.

.. _U-Boot can modify: https://source.denx.de/u-boot/u-boot/-/blob/v2025.10/arch/arm/mach-k3/am62px/am62p5_init.c?ref_type=tags#L253
.. _Sysconfig Tool: https://www.ti.com/tool/SYSCONFIG
.. _here: https://www.ti.com/tool/SYSCONFIG

The MCU+ SDK documentation has `an excellent guide`_ on how to to use the
Sysconfig Tool to generate the needed configuration file. Once generated, copy
the file into the :file:`arch/arm/mach-k3/r5/${SOC}/${SOC}_qos_uboot.c` and
rebuild U-Boot to apply your changes.

.. _an excellent guide: https://software-dl.ti.com/mcu-plus-sdk/esd/AM62X/latest/exports/docs/api_guide_am62x/DRIVERS_QOS_PAGE.html

.. note::

   Changing the QoS blocks after the system is running is considered undefined
   behaviour. These blocks can only be modified during boot-up by the
   boot-loaders when many of the blocks in the SoC are idle


