.. _Power-Management:

#########################
Power Management Overview
#########################

.. rubric:: Power Management Overview

Reducing the power consumption of a device for a specific use-case
requires coordination between multiple software and hardware frameworks.
Power Management techniques can broadly be classified into two categories:
Dynamic Power Management and Static Power Management.

.. rubric:: Dynamic Power Management

Dynamic Power Management techniques reduce the active power
consumption of the SoC when the system is actively performing tasks.
Dynamic PM also optimizes the idle power consumption in between tasks,
when an individual device or CPU is idle for relatively short duration.

The dynamic power management features enabled on |__PART_FAMILY_DEVICE_NAMES__| are as follows:

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family')

   #. DVFS
   #. CPUIdle

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   #. Dynamic Frequency Scaling
   #. CPUIdle
   #. Runtime PM

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   #. Dynamic Frequency Scaling
   #. Runtime PM
   #. CPUIdle

   .. note::

      Dynamic Frequency Scaling and runtime PM are not fully supported on |__PART_FAMILY_DEVICE_NAMES__| as of today,
      and shall be enabled in a future release.

.. rubric:: Static Power Management

Static Power Management ensures the SoC is drawing minimum power when
no use-case is running and the system is inactive for relatively long
duration. This is accomplished by leveraging the low power modes supported
by the SoC and the `System Sleep States <https://docs.kernel.org/admin-guide/pm/sleep-states.html>`__
supported by the Linux kernel.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   The static power management features on |__PART_FAMILY_DEVICE_NAMES__| are:

   #. Partial I/O
   #. I/O Only Plus DDR
   #. Deep Sleep
   #. MCU Only Mode

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   The static power management features on |__PART_FAMILY_DEVICE_NAMES__| are:

   #. RTC Only
   #. RTC Only Plus DDR
   #. Deep Sleep
