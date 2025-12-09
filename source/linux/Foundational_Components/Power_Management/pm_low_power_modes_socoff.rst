.. _lpm_modes_socoff:

###############
Low power modes
###############

********
Overview
********

The following sections describe a high-level description of the different low power modes (LPM) supported on |__PART_FAMILY_NAME__| SoC (System on Chip).
TI EVMs (Evaluation Modules) validate supported low power modes. Each mode needs evaluation based on power consumption and latency (the time it takes to wake-up to Active mode) requirements.
There is a tradeoff between power and latency based on the mode. Users must select the appropriate low power mode at build time to fit the needs of the application. The default mode in the SDK is SoC off.

In SDK offering, following low power modes are supported:

#. SoC off
#. I/O Only Plus DDR

*******
SoC off
*******

In SoC off low power mode, DDR retains partial software context (Mainly HLOS - High Level Operating System, Linux in this case) powering off the rest of SoC. This can save a significant amount of boot time, because it does not reinitialize whole kernel as it is already present in DDR.

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
I/O only Plus DDR
*****************

In I/O only plus DDR, only the I/O pins remain active while the system turns off the rest of SoC.

#. Low power consumption: IO Only Plus DDR mode can save a significant amount of power, especially in battery-powered
   devices. DDR is in self-refresh and the system turns off the rest of the SoC, except for the I/O pins.
#. Better efficiency: I/O Only Plus DDR mode can help to improve the efficiency of embedded devices by reducing
   the amount of time that the processor is idle. This is because we can keep the processor in a low-power state when it is not needed.
#. Respond to external wake-up sources: This allows the system to still respond to external events, while it is in a low-power state and wake-up faster improving boot time.


.. ifconfig:: CONFIG_part_variant in ('J7200')

   To enter I/O only Plus DDR mode, Enable edge sensitive wake-up for MCAN1_RX pin by writing to PADCONFIG_11 (0x0011C02C)

   .. code-block:: console

      # devmem2 0x0011C02C w 0x20050000

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   To enter I/O only Plus DDR mode, Enable level sensitive wake-up for MCU_MCAN0_RX pin by writing to WKUP_PADCONFIG_47 (at address 0x4301C0BC)

   .. code-block:: console

      # devmem2 0x4301C0BC w 0x20050180


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

To exit from I/O only Plus DDR mode,

.. ifconfig:: CONFIG_part_variant in ('J7200')

   Press SW1 push button on |__PART_FAMILY_NAME__| SOM

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   On the |__PART_FAMILY_NAME__| EVM, the second pin-out of J33 is MCU_MCAN0_RX and it connects directly to the SoC.
   A voltage of 3.3V should be applied on that pin to wake it up from low power.


Resume flow,

.. code-block:: console

   U-Boot SPL 2025.01-00676-g0373244c939d (Oct 23 2025 - 18:28:04 +0530)
   SYSFW ABI: 4.0 (firmware rev 0x000b '11.2.0-6-ge1d0d+ (Fancy Rat)')
   Trying to boot from MMC2
   Starting ATF on ARM64 core...

   [   41.242486] Enabling non-boot CPUs ...
   I/TC: Secondary CPU 1 initializing
   I/TC: Secondary CPU 1 switching to normal world boot
   [   41.265404] Detected PIPT I-cache on CPU1
   [   41.269427] GICv3: CPU1: found redistributor 1 region 0:0x0000000001920000
   [   41.276323] CPU1: Booted secondary processor 0x0000000001 [0x411fd080]
   [   41.283475] CPU1 is up
   [   41.305953] am65-cpsw-nuss 46000000.ethernet: set new flow-id-base 48
   [   41.323544] am65-cpsw-nuss 46000000.ethernet eth0: PHY [46000f00.mdio:00] driver [TI DP83867] (irq=POLL)
   [   41.333027] am65-cpsw-nuss 46000000.ethernet eth0: configuring for phy/rgmii-rxid link mode
   [   41.343885] OOM killer enabled.
   [   41.347048] Restarting tasks ... done.
   [   41.353184] random: crng reseeded on system resumption
   [   41.359868] platform 41000000.r5f: R5F core may have been powered on by a different host, programmed state (0) != actual state (1)
   [   41.371848] platform 41000000.r5f: configured R5F for IPC-only mode
   [   41.378136] remoteproc remoteproc0: attaching to 41000000.r5f
   [   41.384636] rproc-virtio rproc-virtio.10.auto: assigned reserved memory node r5f-dma-memory@a0000000
   [   41.395697] virtio_rpmsg_bus virtio0: rpmsg host is online
   [   41.401350] rproc-virtio rproc-virtio.10.auto: registered virtio0 (type 7)
   [   41.408925] remoteproc remoteproc0: remote processor 41000000.r5f is now attached
   [   41.416506] PM: suspend exit
   root@<machine>-evm:~#
   root@<machine>-evm:~#
