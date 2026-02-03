Quality of Service (QoS)
########################

The Common Bus Architecture (CBASS) module includes Quality of Service
(QoS) blocks to route and prioritize SoC bus traffic. By adjusting
attributes like priority, Address Selection (ASEL), and Order ID
(orderID), you can optimize transaction handling.

For example, most K3 SoC External Memory Interface (EMIF) controllers
use two ports. Setting an Order ID between 8 and 15 routes traffic
through a high-priority port, ensuring it is serviced before standard
traffic. Applying this to the display subsystem helps prevent stuttering
and jitter.

For more details, see your processor's Technical Reference Manual (TRM).

Modifying QoS Defaults
======================

Most transactions default to the lowest priority (ASEL 0, Order ID 0).
During boot-up, `U-Boot can update`_ these settings using data from the.
Sysconfig Tool which you can download or launch online `here`_.

.. _U-Boot can update: https://source.denx.de/u-boot/u-boot/-/blob/v2025.10/arch/arm/mach-k3/am62px/am62p5_init.c?ref_type=tags#L253
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


