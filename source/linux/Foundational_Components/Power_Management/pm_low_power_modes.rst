.. _lpm_modes:

###############
Low Power Modes
###############

********
Overview
********

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. important::

      SK-AM62-SIP EVM does NOT support low power modes.

The following sections describe a high-level description of the different low power modes (LPM) of the
device. If your application requires inactive power management, you must determine which
low power mode described below satisfies your requirements. Each mode must be evaluated
based on power consumption and latency (the time it takes to wakeup to Active mode) requirements. Specific
values are detailed in the device-specific data sheet. As part of this SDK offering,
Texas Instruments has added support for the following low power modes (ordered from lowest power consumption
to highest power consumption):

#. Partial I/O
#. I/O Only Plus DDR
#. Deep Sleep
#. MCU Only

TI SDK 10.0 (ti-linux-6.6.y kernel and 10.0 DM firmware) adds support for
an updated LPM Software Architecture that seamlessly manages the various
Suspend-to-RAM modes supported by AM62 family of devices. More details about
this architecture can be found in :ref:`LPM constraints framework<pm_constraints_fwk>` section.

***********
Partial I/O
***********

In Partial I/O, only the I/O pins and a small digital logic in the CANUART I/O
Bank are active, while the rest of the SoC is turned off. The user can
use the I/O pins to aggregate multiple I/O wakeup events and toggle
PMIC_LPM_EN pin to enable PMIC or discrete power solution when an I/O
wakeup event is triggered.

.. note::

   The system looses nearly all its state as DDR is also turned-off.
   Partial I/O is comparable with a Linux poweroff state.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. important::

      Only AM62 LP-SK EVM supports Partial I/O mode.

The reference implementation in this SDK implements Partial I/O as a
poweroff state. On poweroff, Linux ti_sci driver checks the potential
Partial I/O wakeup sources for being enabled. If one of the wakeup
sources is found to be enabled, Partial I/O is entered instead of poweroff.

The following wakeup sources have been configured for Partial I/O:
mcu_uart0, mcu_mcan0, and mcu_mcan1. Partial I/O mode can only be tested
when `k3-am62x-sk-lpm-wkup-sources.dtso <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-lpm-wkup-sources.dtso?h=11.01.05>`__
overlay is loaded. Please refer to :ref:`How to enable DT overlays<howto_dt_overlays>` for more details.

After Linux boots, the MCAN wakeup for Partial I/O is enabled.

Enter Partial I/O mode with the following command:

.. code-block:: console

   root@<machine>:~# poweroff

At this point, Linux kernel will go through its poweroff process and
the console output will stop at the following lines:

.. code-block:: text

   [   51.698039] systemd-shutdown[1]: Powering off.
   [   51.769478] reboot: Power down

The system has entered Partial I/O and can only be woken up with an
activity on the I/O pin programmed for wakeup. For example, if mcu_mcan0
wakeup was enabled, grounding Pin 22 of J8 MCU Header will wakeup the
system and it will go through a normal Linux boot process.

.. _pm_io_only_plus_ddr:

*****************
I/O Only Plus DDR
*****************

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   This mode is not applicable for AM62X.

.. ifconfig:: CONFIG_part_variant in ('AM62AX' , 'AM62PX')

   This mode is similar to Partial I/O mode, with the major distinction being
   that the DDR memory is kept in self refresh to save context. All the processor
   power supplies are turned off except the LVCMOS I/O power supply while keeping
   DDR in self-refresh.
   The user can do system power state transitions, including power supply control,
   by a single interface signal (PMIC_LPM_EN signal) with PMIC register programming.

   The benefits of using I/O Only plus DDR in embedded devices:

   #. Lowest power consumption: I/O Only Plus DDR mode can save a significant amount of power, especially in battery-powered
      devices that are mostly idle or low activity most of the time with the full context being saved.
   #. Better efficiency: I/O Only Plus DDR mode can help to improve the efficiency of embedded devices by
      reducing the amount of time that the processor is idle. This is because the processor can
      be kept in a low-power state when it is not needed.

   .. ifconfig:: CONFIG_part_variant in ('AM62AX')

      .. important:: Jumper J9 should be connected on SK to enable system to enter I/O Only plus DDR mode.

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      .. important:: Jumper J12 should be connected on SK to enable system to enter I/O Only plus DDR mode.

   The wakeup sources that can be used to wake the system from I/O Only Plus
   DDR are mcu_uart0, mcu_mcan0, mcu_mcan1 and wkup_uart0. To use the mcu_mcan0
   and mcu_mcan1 wakeup sources, apply the
   `k3-am62x-sk-lpm-io-ddr-wkup-sources.dtso <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-lpm-io-ddr-wkup-sources.dtso?h=11.01.05>`__
   overlay. Please refer to :ref:`How to enable DT overlays<howto_dt_overlays>`
   for more details. To use the mcu_uart0 and wkup_uart0 wakeup sources, direct
   register writes can be used to enable wakeup after Linux boots.

   .. rubric:: Following commands set the wakeup EN bit, enable receive for pad in PADCONFIG register and can
               be used to enable wakeup from mcu_uart0 and wkup_uart0 pins respectively.

   .. important::

      The steps mentioned below are a workaround to enable wakeup for mcu_uart0
      and wkup_uart0 as there are more driver level changes required to enable
      the wakeup support.

   .. code-block:: console

      root@<machine>:~# devmem2 0x4084014 w 0x20050000  # MCU_PADCONFIG5 for mcu_uart0
      root@<machine>:~# devmem2 0x4084024 w 0x20050000  # MCU_PADCONFIG9 for wkup_uart0

   .. note::

      Atleast one of the wakeup sources listed above must be enabled to wakeup from I/O Only Plus DDR mode.

   .. rubric:: To enter I/O Only Plus DDR mode, first disable wakeup from RTC,
               Main UART, USB0, and USB1 as these wakeup sources are not
               supported for this mode.

   .. ifconfig:: CONFIG_part_variant in ('AM62AX')

      .. code-block:: console

         root@am62axx-evm:~# echo disabled > /sys/class/rtc/rtc0/device/power/wakeup
         root@am62axx-evm:~# echo disabled > /sys/bus/platform/devices/2800000.serial/power/wakeup
         root@am62axx-evm:~# echo disabled > /sys/devices/platform/bus@f0000/f900000.dwc3-usb/power/wakeup
         root@am62axx-evm:~# echo disabled > /sys/devices/platform/bus@f0000/f910000.dwc3-usb/power/wakeup

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      .. code-block:: console

         root@am62pxx-evm:~# echo disabled > /sys/class/rtc/rtc0/device/power/wakeup
         root@am62pxx-evm:~# echo disabled > /sys/bus/platform/devices/2800000.serial/power/wakeup
         root@am62pxx-evm:~# echo disabled > /sys/devices/platform/bus@f0000/f900000.usb/power/wakeup
         root@am62pxx-evm:~# echo disabled > /sys/devices/platform/bus@f0000/f910000.usb/power/wakeup

   .. rubric:: Then, configure PMIC register bit to turn off only selected rails for this mode.

   .. ifconfig:: CONFIG_part_variant in ('AM62AX')

      .. code-block:: console

         root@am62axx-evm:~# i2cset -f -y -m 0xFF -r -a 0 0x48 0x86 0x1

      The register write has been done to enable PMIC to enter `PMIC S2R <https://www.ti.com/lit/ug/slvucm3/slvucm3.pdf>`_ .

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      .. code-block:: console

         root@am62pxx-evm:~# i2cset -f -y -m 0xFF -r -a 0 0x48 0x86 0x2

   .. rubric:: Now, the SoC can be suspended using the following command:

   .. code-block:: console

      root@<machine>:~# echo mem > /sys/power/state
      [   26.132900] PM: suspend entry (deep)
      [   26.136759] Filesystems sync: 0.000 seconds
      [   26.151748] Freezing user space processes
      [   26.157256] Freezing user space processes completed (elapsed 0.001 seconds)
      [   26.164239] OOM killer disabled.
      [   26.167469] Freezing remaining freezable tasks
      [   26.173168] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
      [   26.180624] printk: Suspending console(s) (use no_console_suspend to debug)

   This indicates that the device has partially completed the I/O Only plus DDR entry sequence.

   .. ifconfig:: CONFIG_part_variant in ('AM62AX')

      For further confirmation, one can take a look at the on board LED LD2 on the SK
      (LED should turn off).

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      For further confirmation, one can take a look at the on board LED LD1 on the SK
      (LED should turn off).

   The system has entered I/O Only plus DDR and can be woken up either with an
   activity on the I/O pin programmed for wakeup or key press on wkup_uart0 (third serial port :file:`/dev/ttyUSB2`) or
   mcu_uart0 (fourth serial port :file:`/dev/ttyUSB3`).

   .. note::

      The system will enter I/O Only plus DDR mode only if DM selects it based on existing constraints.

**********
Deep Sleep
**********

Deep Sleep AKA Suspend-to-RAM is a low-power mode that allows an embedded device
to retain its state in RAM while the processor is turned off.
This can save a significant amount of power, especially in devices that are
battery-powered.

The benefits of using deep sleep in embedded devices:

#. Faster wake-up: devices can wake up from this low-power state much faster than
   a complete power cycle.
#. Better efficiency: deep sleep can help to improve the efficiency of embedded devices by
   reducing the amount of time that the processor is idle. This is because the processor can
   be kept in a low-power state when it is not needed.

In order to enter Deep Sleep, use the following command:

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. code-block:: console

      root@am62xx-evm:~# echo mem > /sys/power/state
      [  444.719520] PM: suspend entry (deep)
      [  444.723374] Filesystems sync: 0.000 seconds
      [  444.751309] Freezing user space processes
      [  444.756923] Freezing user space processes completed (elapsed 0.001 seconds)
      [  444.763924] OOM killer disabled.
      [  444.767141] Freezing remaining freezable tasks
      [  444.772908] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
      [  444.780328] printk: Suspending console(s) (use no_console_suspend to debug)
      [  444.796853] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 179: state: 1: ret 0
      [  444.797037] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 178: state: 1: ret 0
      [  444.805604] omap8250 2800000.serial: PM domain pd:146 will not be powered off
      [  444.806188] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 117: state: 1: ret 0
      [  444.816592] remoteproc remoteproc0: stopped remote processor 5000000.m4fss
      [  444.820627] Disabling non-boot CPUs ...
      [  444.822859] psci: CPU1 killed (polled 0 ms)
      [  444.826567] psci: CPU2 killed (polled 0 ms)
      [  444.830170] psci: CPU3 killed (polled 0 ms)

.. ifconfig:: CONFIG_part_variant in ('AM62AX' , 'AM62PX')

   .. code-block:: console

      root@<machine>:~# echo mem > /sys/power/state
      [  230.181404] PM: suspend entry (deep)
      [  230.185406] Filesystems sync: 0.000 seconds
      [  230.219094] Freezing user space processes
      [  230.224495] Freezing user space processes completed (elapsed 0.001 seconds)
      [  230.231506] OOM killer disabled.
      [  230.234736] Freezing remaining freezable tasks
      [  230.240432] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
      [  230.247825] printk: Suspending console(s) (use no_console_suspend to debug)
      [  230.266309] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 179: state: 1: ret 0
      [  230.266456] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 178: state: 1: ret 0
      [  230.273953] omap8250 2800000.serial: PM domain pd:146 will not be powered off
      [  230.274450] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 117: state: 1: ret 0
      [  230.284177] remoteproc remoteproc1: stopped remote processor 79000000.r5f
      [  230.287440] Disabling non-boot CPUs ...
      [  230.289569] psci: CPU1 killed (polled 0 ms)
      [  230.292413] psci: CPU2 killed (polled 4 ms)
      [  230.295457] psci: CPU3 killed (polled 0 ms)

This partially indicates that Linux has finished it's Deep Sleep suspend sequence.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   For further confirmation, program the PMCTRL_SYS register (0x43018080) to
   0x15. The PMIC_LPM_EN pin on the EVM is 3.3V when active and 0V when in 
   DeepSleep.

.. note::

   The system will enter deep sleep mode only if DM selects it based on existing constraints.

Refer to the :ref:`Wakeup Sources<pm_wakeup_sources>` section for information on how to wakeup the device from
Deep Sleep mode using one of the supported wakeup sources.

********
MCU Only
********

.. _pm_mcu_only:

Similar to Deep Sleep, with the major distinction being that the MCU core is kept alive to run applications.
The benefits of using MCU Only mode:

#. Low power consumption: MCU Only mode can save a significant amount of power, especially in battery-powered
   devices. This is because the rest of the SoC status is the same as Deep Sleep and DDR is in self-refresh.
#. Run background tasks: This mode can be used to run background tasks that do not require the full power of the system.
   For example, you could use the firmware on the MCU core to run a watchdog timer, a sensor polling loop,
   or a network communication task.
#. Respond to interrupts: This allows the system to still respond to external events, while it is in a low-power state.

To enter MCU Only mode, set :code:`100 msec` resume latency for CPU0 in Linux:

.. code-block:: console

   root@<machine>:~# echo 100000 > /sys/devices/system/cpu/cpu0/power/pm_qos_resume_latency_us

Now, the SoC can be suspended using the following command:

.. code-block:: console

   root@<machine>:~# rtcwake -s 5 -m mem
   rtcwake: wakeup from "mem" using /dev/rtc0 at Thu Jan  1 00:01:02 1970
   [   45.548480] PM: suspend entry (deep)
   [   45.552187] Filesystems sync: 0.000 seconds
   [   45.566606] Freezing user space processes
   [   45.572093] Freezing user space processes completed (elapsed 0.001 seconds)
   [   45.579083] OOM killer disabled.
   [   45.582309] Freezing remaining freezable tasks
   [   45.587984] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
   [   45.595432] printk: Suspending console(s) (use no_console_suspend to debug)
   [   45.627136] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 179: state: 1: ret 0
   [   45.640758] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 178: state: 1: ret 0
   [   45.648341] omap8250 2800000.serial: PM domain pd:146 will not be powered off
   [   45.648892] ti-sci 44043000.system-controller: ti_sci_cmd_set_device_constraint: device: 117: state: 1: ret 0
   [   45.648993] cpu cpu3: ti_sci_suspend: sending max CPU latency=100
   [   45.649033] ti-sci 44043000.system-controller: ti_sci_cmd_set_latency_constraint: latency: 100: state: 1: ret 0
   [   45.669270] Disabling non-boot CPUs ...
   [   45.671353] psci: CPU1 killed (polled 0 ms)
   [   45.674819] psci: CPU2 killed (polled 0 ms)
   [   45.676640] psci: CPU3 killed (polled 4 ms)
   [   45.677311] Enabling non-boot CPUs ...
   [   45.677632] Detected VIPT I-cache on CPU1
   [   45.677672] GICv3: CPU1: found redistributor 1 region 0:0x00000000018a0000
   [   45.677724] CPU1: Booted secondary processor 0x0000000001[0x410fd034]
   [   45.678694] CPU1 is up
   [   45.678934] Detected VIPT I-cache on CPU2
   [   45.678962] GICv3: CPU2: found redistributor 2 region 0:0x00000000018c0000
   [   45.679002] CPU2: Booted secondary processor 0x0000000002[0x410fd034]
   [   45.679778] CPU2 is up
   [   45.680016] Detected VIPT I-cache on CPU3
   [   45.680045] GICv3: CPU3: found redistributor 3 region 0:0x00000000018e0000
   [   45.680088] CPU3: Booted secondary processor 0x0000000003[0x410fd034]
   [   45.680939] CPU3 is up
   [   45.681332] ti-sci 44043000.system-controller: ti_sci_resume: wakeup source: 0x50
   [   45.703650] am65-cpsw-nuss 8000000.ethernet: set new flow-id-base 19
   [   45.719704] am65-cpsw-nuss 8000000.ethernet eth0: PHY[8000f00.mdio:00] driver[TI DP83867] (irq=POLL)
   [   45.719730] am65-cpsw-nuss 8000000.ethernet eth0: configuring for phy/rgmii-rxid link mode
   [   46.004264] OOM killer enabled.
   [   46.007406] Restarting tasks ... done.
   [   46.012454] random: crng reseeded on system resumption
   [   46.026923] platform 79000000.r5f: Core is on in resume
   [   46.032206] platform 79000000.r5f: received echo reply from 79000000.r5f
   [   46.032262] PM: suspend exit

Once the SoC enters MCU Only mode, the following log should be printed
on the MCU UART (in most cases it will be /dev/ttyUSB3)

.. code-block:: text

   [IPC RPMSG ECHO] Next MCU mode is 1
   [IPC RPMSG ECHO] Suspend request to MCU-only mode received
   [IPC RPMSG ECHO] Press a single key on this terminal to resume the kernel from MCU only mode

.. note::

   The system will enter MCU Only mode only if DM selects it based on existing constraints.

Refer to the :ref:`Wakeup Sources<pm_wakeup_sources>` section for information on how to wakeup the device from
MCU Only mode using one of the supported wakeup sources.

***********
Limitations
***********

HWRNG support on GP devices is incompatible with Deep Sleep and MCU Only
modes. To test LPM on GP devices, HWRNG has to be unloaded one-time
before running the Suspend-to-RAM command:

.. code-block:: console

   root@<machine>:@~# modprobe -r optee_rng

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   .. attention::

      Linux SDK for edge AI applications has a known issue that breaks
      Deep Sleep and MCU Only modes. To test these modes, the DSP module
      has to be unloaded before attempting LPM:

      .. code-block:: console

         root@am62axx-evm:@~# modprobe -rf ti_k3_dsp_remoteproc

Compatibility
=============

The compatibility between Kernel version and firmware version to enter low power mode is listed
in the below table:

+-----------------+-----------------------------------+------------------------------------+
|  LPM            |  Firmware v10.0                   |  Firmware < v10.0                  |
+=================+===================================+====================================+
| TI Kernel 6.6   |   All low power modes supported   |    Only Deep Sleep supported       |
+-----------------+-----------------------------------+------------------------------------+
| TI Kernel < 6.6 |   All low power modes supported   |    All low power modes supported   |
+-----------------+-----------------------------------+------------------------------------+

.. important::

   In case of Kernel 6.6 and Firmware < v10.0, the firmware is unaware of the constraints
   framework. Hence, the system will always enter deep sleep low power mode irrespective
   of the constraints set.

.. note::

   All low power mode supported implies all low power mode supported by the firmware as per firmware
   capabilities. `TISCI_MSG_QUERY_FW_CAPS <https://software-dl.ti.com/tisci/esd/latest/2_tisci_msgs/general/core.html#tisci-msg-query-fw-caps>`__
   can be sent to firmware to get the low power modes supported by firmware.
