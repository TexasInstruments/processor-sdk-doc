.. _lpm_modes_socoff:

###############
Low power modes
###############

********
Overview
********

A typical SoC, from power to HLOS (Linux here for example) takes around 20 seconds to boot (reaching till Linux prompt), when it is ready to
run application.
However, requirement is to run applications within 2-3 seconds of power-on. For this purpose, developers have implemented many custom optimizations,
that do not scale from platform to platform.

In LPM state, partial SW state saved to DDR that helps in achieving faster boot.

The following sections describe a high-level description of the different low power modes (LPM) supported on |__PART_FAMILY_DEVICE_NAMES__| SoC (System on Chip).

+---------------------+---------------+---------------+-------------------------+-----------------------+
| **Low power Mode**  | **SoC State** | **DDR State** | **Retained SW context** | **Lost SW context**   |
+---------------------+---------------+---------------+-------------------------+-----------------------+
|       SOC OFF       | Power off     | Self Refresh  | HLOS driver and apps    | All fws (R5/M/C) core |
+---------------------+---------------+---------------+-------------------------+-----------------------+
| I/O only Plus DDR   | Power off     | Self Refresh  | HLOS driver and apps    | All fws (R5/M/C) core |
|                     | except wakeup |               |                         |                       |
|                     | I/O           |               |                         |                       |
+---------------------+---------------+---------------+-------------------------+-----------------------+

Based upon the requirement of power consumption and latency (the time it takes to wake-up to Active mode),
users can select the appropriate low power mode at **build time** to fit the needs of their application.
The default mode in the SDK is **SOC OFF**.

LPM entry overview
==================
After detecting the condition to enter standby, applications interacting with remote firmware shall be closed
before entering standby.

This section explains the high-level software flow of low power modes entry.

   .. image:: /images/jacinto_s2r_entry.png

LPM exit overview
=================
On receiving wakeup trigger, PMIC will restore power to SoC and SoC resume process will exit DDR from self-refresh mode and restore the
saved software context.
As part of resume process, firmwares of remote cores will be reloaded, therefore application interacting with remote firmware shall be started again.
This section explains the high-level software flow of low power modes exit.

   .. image:: /images/jacinto_s2r_exit.png


*********************
How to Test LPM modes
*********************
To test LPM modes, one needs to ensure that software and hardware configurations are correct.
The following sections have details regarding the hardware and software configurations on TI EVMs.

Hardware modifications
======================

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   Following board modifications are needed to validate SOC_OFF and IO_ONLY_PLUS_DDR low power modes on the J784S4 EVM.

   - Change R534 from pull-down to pull-up to VCCA_3V3 side of C320, VDD_IO_1V8 powered down so that VDD1_DDR_1V8 also powers down unless EN remains high.
   -  Remove R965, R1167, R1170, and R1169, During DDR RET, RESET must be pulled high.
   -  R658 moved to R659

.. ifconfig:: CONFIG_part_variant in ('J7200')

   By default, SOC_OFF mode can be validated on J7200 EVM without any hardware changes.
   In case IO_ONLY_PLUS_DDR mode needs to be tested,user needs to do the following board modification. These modifications will not impact SOC_OFF mode.

   - Remove R74 and place it at R610. This will pull the signal high.

Software modifications
======================
TI’s K3 Jacinto family of SoCs have a concept of boardcfg that can be used to configure certain parameters at build time.
By default, SOC_OFF mode enabled by default in SDK.
IO_ONLY_PLUS_DDR mode can be enabled by changing boardcfg in u-boot at build time.

The low power mode is set statically at build time in “lpm_cfg” section of the power management board config.
In the u-boot source tree the boardcfg is present at:

.. ifconfig:: CONFIG_part_variant in ('J7200')

   board/ti/j721e/pm-cfg_j7200.yaml
   `J7200 board config <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/board/ti/j721e/pm-cfg_j7200.yaml?h=ti-u-boot-2025.01>`_ .

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   board/ti/j784s4/pm-cfg.yaml
   `J784s4 board config <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/board/ti/j784s4/pm-cfg.yaml?h=ti-u-boot-2025.01>`_ .

In above board config file, default lpm_mode is 0x5 (SOC_OFF) and suspend_initiator is 0xA (A72_0 host).

To set the LPM mode as IO_RET_PLUS_DDR, change lpm_mode to 0x2.

Sample code is available at
https://gist.github.com/uditkumarti/fd0dfe8aa3dc094aadafecab67048307

The lpm mode value can be picked up from:
https://software-dl.ti.com/tisci/esd/latest/2_tisci_msgs/pm/lpm.html

Testing
=======
Below section explains, how to test supported LPM modes

SoC off
-------

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


IO_ONLY_PLUS_DDR mode
---------------------

Use u-boot build after changing lpm_mode to 0x2, in boardconfig file.
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

*****************
Known limitations
*****************
1. Only A core as suspend master supported and tested with Linux.
2. The LPM feature is not supported on HS-SE variant J784S4.
3. If PCIe is being used, the resume latency increases by 1 sec for every PCIe instance, If EP is not connected.
4. Remote core firmwares are getting loaded by Linux on resume.
5. MCU domain R5 core, cannot be used in split mode.
