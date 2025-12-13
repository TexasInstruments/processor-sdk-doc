.. _lpm_modes_socoff:

###############
Low power modes
###############

********
Overview
********

The following sections describe a high-level description of the different low power modes (LPM) supported on |__PART_FAMILY_NAME__| SoC (System on Chip).
Validation of these modes are done on TI EVMs (Evaluation Modules). Users must select the appropriate low power mode at build time, which meets the requirements.
Each mode needs evaluation based on power consumption and latency (the time it takes to wake-up to Active mode) requirements.
In SDK offering, following low power modes are supported:

#. SoC off
#. I/O Only Plus DDR (Double Data Rate)

*******
SoC off
*******

In SoC off low-power mode, DDR retains partial SW context (Mainly HLOS (High Level Operating System) Linux) while the SoC is turned off. This can save a significant amount of boot time, because it does not reinitialize whole kernel as it is already present in DDR.

The benefits of using SoC off in embedded devices:

#. Faster wake-up: Devices can wake-up from this low-power state much faster than
   a complete power cycle.
#. Better efficiency: This mode can help to improve the efficiency of embedded devices by
   reducing the amount of time that the processor is idle. This is because we can keep the processor in a low-power state when it is not needed.

To enter SoC off, use the following command:

   .. code-block:: console

      root@<machine>-evm:~# echo mem > /sys/power/state
      [18.380346] PM: suspend entry (deep)
      [18.576999] Filesystems sync: 0.193 seconds
      [18.587643] Freezing user space processes
      [18.593191] Freezing user space processes completed (elapsed 0.001 seconds)
      [18.600179] OOM killer disabled.
      [18.603395] Freezing remaining freezable tasks
      [18.608964] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
      [18.616364] printk: Suspending console(s) (use no_console_suspend to debug)

This indicates that Linux has finished its suspend sequence.

To exit from SoC off,

.. ifconfig:: CONFIG_part_variant in ('J7200')

   Press SW12 push button on J7200 evm.

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   Press SW15 push button on J784S4 evm.

*****************
I/O only plus DDR
*****************

In I/O only plus DDR, only the I/O pins remain active while the system turns off the rest of SoC.

#. Low power consumption: IO Only mode can save a significant amount of power, especially in battery-powered
   devices. This is because the DDR is in self-refresh and except for the IO pins, the system turns off the rest of the SoC.
#. Better efficiency: I/O Only Plus DDR mode can help to improve the efficiency of embedded devices by reducing
   the amount of time that the processor is idle. This is because we can keep the processor in a low-power state when it is not needed.
#. Respond to external wake-up sources: This allows the system to still respond to external events, while it is in a low-power state and wake-up faster improving boot time.


.. ifconfig:: CONFIG_part_variant in ('J7200')

   To enter I/O only mode, Enable edge sensitive wake-up for MCAN1_RX pin by writing to PADCONFIG_11 (0x0011C02C)

   .. code-block:: console

      # devmem2 0x0011C02C w 0x20050000
      # echo mem > /sys/power/state

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   To enter I/O only mode, Enable level sensitive wake-up for MCU_MCAN0_RX pin by writing to WKUP_PADCONFIG_47 (at address 0x4301C0BC)

   .. code-block:: console

      # devmem2 0x4301C0BC w 0x20050180
      # echo mem > /sys/power/state


.. code-block:: console

   root@<machine>-evm:~# echo mem > /sys/power/state
   [18.380346] PM: suspend entry (deep)
   [18.576999] Filesystems sync: 0.193 seconds
   [18.587643] Freezing user space processes
   [18.593191] Freezing user space processes completed (elapsed 0.001 seconds)
   [18.600179] OOM killer disabled.
   [18.603395] Freezing remaining freezable tasks
   [18.608964] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
   [18.616364] printk: Suspending console(s) (use no_console_suspend to debug)

To exit from IO_ONLY_PLUS_DDR,

.. ifconfig:: CONFIG_part_variant in ('J7200')

   Press SW1 push button on |__PART_FAMILY_NAME__| SOM

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   On the |__PART_FAMILY_NAME__| EVM, the second pin-out of J33 is MCU_MCAN0_RX and it connects directly to the SoC.
   A voltage of 3.3V should be applied on that pin to wake it up from low power.

.. note::

   Firmware capabilities determine the supported low power modes.
   `TISCI_MSG_QUERY_FW_CAPS <https://software-dl.ti.com/tisci/esd/latest/2_tisci_msgs/general/core.html#tisci-msg-query-fw-caps>`__
   sent to firmware to get the low power modes supported by firmware.
