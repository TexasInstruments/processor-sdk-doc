Quality of Service (QoS)
########################

The Common Bus Architecture (CBASS) module includes Quality of Service
(QoS) blocks to route and prioritize SoC bus traffic. By adjusting
attributes such as priority, Address Selection (ASEL), and Order ID
(orderID), you can optimize transaction handling.

For example, most K3 SoC External Memory Interface (EMIF) controllers
use two ports. Setting an Order ID between 8 and 15 routes traffic
through a high-priority port, ensuring it gets serviced before standard
traffic. Applying this to the display subsystem helps prevent stuttering
and jitter.

For more details, see your processor's Technical Reference Manual (TRM).

Modifying QoS defaults
======================

Most transactions default to the lowest priority (ASEL 0, orderID 0).
During boot-up, `U-Boot can update`_ these settings by using data from
the SysConfig tool, which you can download or use online `here`_.

.. _U-Boot can update: https://source.denx.de/u-boot/u-boot/-/blob/v2026.04/arch/arm/mach-k3/am62px/am62p5_init.c?ref_type=tags#L216
.. _here: https://www.ti.com/tool/SYSCONFIG

The MCU+ SDK documentation has an excellent `guide`_ on how to use the
SysConfig tool to generate the needed :file:`<soc>_qos_uboot.c`
configuration file. Once generated, copy it into
:file:`arch/arm/mach-k3/r5/<soc>/<soc>_qos_uboot.c`, where ``<soc>``
is your SoC name, e.g. ``am62px``. Then rebuild U-Boot to apply your
changes.

.. _guide: https://software-dl.ti.com/mcu-plus-sdk/esd/AM62X/latest/exports/docs/api_guide_am62x/DRIVERS_QOS_PAGE.html

.. note::

   Configuring the QoS blocks of a running system can cause issues.
   You can only change these settings during boot-up by using the
   bootloaders, when many of the systems in the SoC are idle.
