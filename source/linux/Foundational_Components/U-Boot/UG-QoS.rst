Quality of Service (QoS)
########################

The Common Bus Architecture (CBASS) module includes Quality of Service
(QoS) blocks. These can change attributes such as the priority, Address
Selection (ASEL), and Order ID (orderID) values of the transactions
created by blocks in the System on a Chip (SoC) to route and prioritize
the traffic on the bus in a particular way.

For example changing the Order ID can route traffic through a particular port
when more than port exists for that block on the bus. Most External
Memory Interface (EMIF) controllers for K3 SoCs will have two ports to
the CBASS so setting an Order ID value of 8 to 15 will route traffic
through the high priority port and serviced by the EMIF before standard
traffic. Setting an Order ID of 8 or higher for the display subsystem
will allow its traffic to use the EMIF's high priority port, helping to
minimize stuttering or jitter on the display.

Consult the Technical Reference Manual (TRM) for you processor for more
information about these QoS settings.

Modifying QoS Defaults
======================

By default, the majority of transactions will default to the lowest
priority level (ASEL is 0 and Order ID is 0). During boot-up `U-Boot can
change`_  the QoS settings for your board early on during boot-up using
the data generated from the Sysconfig Tool which you can download or
launch online `here`_.

.. _U-Boot can change: https://source.denx.de/u-boot/u-boot/-/blob/v2025.10/arch/arm/mach-k3/am62px/am62p5_init.c?ref_type=tags#L253
.. _here: https://www.ti.com/tool/SYSCONFIG

The MCU+ SDK documentation has `an excellent guide`_ on how to to use the
Sysconfig Tool to generate the needed configuration file. Once generated, copy
the file into the :file:`arch/arm/mach-k3/r5/${SOC}/${SOC}_qos_uboot.c` and
rebuild U-Boot to apply your changes.

.. _an excellent guide: https://software-dl.ti.com/mcu-plus-sdk/esd/AM62X/latest/exports/docs/api_guide_am62x/DRIVERS_QOS_PAGE.html

.. note::

   Configuring the QoS blocks of a running system can cause issues.
   You can only modify these settings during boot-up by the boot-loaders
   when many of the systems in the SoC are idle.


