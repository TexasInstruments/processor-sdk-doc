.. _lpm_modes:

###############
Low Power Modes
###############

Overview
********

The following sections describe a high-level description of the different low power modes (LPM) of the
device. If your application requires inactive power management, you must determine which
low power mode described below satisfies your requirements. Each mode must be evaluated
based on power consumption and latency (the time it takes to wakeup to active mode) requirements. Specific
values are detailed in the device-specific data sheet. As part of this SDK offering,
Texas Instruments has added support for the following low power modes (ordered from lowest power consumption
to highest power consumption):

#. RTC Only
#. RTC Only Plus DDR
#. Deep Sleep

RTC Only
********

RTC Only mode is the deepest low power mode that allows the system to enter a complete poweroff state
with ultra-low power consumption while maintaining system time and wakeup capability.
Unlike other low power modes, RTC Only powers off all domains except the RTC, which remains active
to keep track of system time and provide wakeup via RTC alarm or RTC I/O event.

.. note::

   The system loses nearly all its state as DDR is also turned-off.
   RTC Only is comparable with a Linux poweroff state with system timer ON.

.. important::

   Jumper J14 position on the EVM determines which low power mode is entered. For RTC Only mode,
   connect jumper J14 to the position marked as "RTC ONLY MODE".

   .. image:: /images/am62l_lpm_j14.png

The reference implementation in this SDK implements RTC Only as a poweroff state.
When the system powers off, the RTC driver programs the RTC hardware for poweroff mode.
The final sequence to power off the system is executed by TF-A firmware, which pulls the PMIC_EN
signal low to turn off all the supply rails powered by the PMIC.

On AM62L platforms, if the ``system-power-controller`` device tree property is not set on the PMIC node,
the PMIC will not register a poweroff handler. In this configuration, TF-A firmware handles the
poweroff sequence and the system enters RTC Only mode. This allows the system to maintain accurate
system time and provide wakeup capability via RTC alarm or external button press while consuming
minimal power.

RTC Only mode supports two wakeup sources: RTC timer alarm and RTC I/O pins.

Use the following command to enter RTC Only mode with a timer alarm for wakeup:

.. code-block:: console

   root@<machine>:~# rtcwake -s <time> -m off

Use the following command to enter RTC Only mode with RTC I/O (button press) for wakeup:

.. code-block:: console

   root@<machine>:~# poweroff

At this point, the Linux kernel will go through its poweroff process and
the console output will stop at the following lines:

.. code-block:: dmesg

   [   51.698039] systemd-shutdown[1]: Powering off.
   [   51.769478] reboot: Power down

The system has entered RTC Only mode and can be woken up by activity on an RTC I/O pin
programmed for wakeup. If an alarm was set, the system will automatically wake up
when the alarm triggers.

During resume from RTC Only mode, the system goes through a normal Linux boot process. The RTC driver
detects that the RTC is already programmed and skips the full initialization, performing only minimal
cleanup to preserve the system time.

.. note::

   Please go through the s2idle docs to understand how to select between multiple low power modes.
   The steps and overall architecture/ sequence diagrams are documented in :ref:`pm_s2idle_psci`.
   The default mode via s2idle is RTC Only Plus DDR, since it's the deepest.
   If regular [mem] interface is selected in `/sys/power/mem_sleep`, the RTC Only + DDR low power mode requires special steps
   to enter. The steps are documented in :ref:`am62l_suspend_workarounds`.

RTC Only Plus DDR
*****************

RTC Only + DDR mode is the deepest low power mode that allows the system to enter a state of lowest power consumption
while still retaining the DDR RAM context.

.. important::

   Jumper J14 position on the EVM determines which low power mode is entered. For RTC Only + DDR mode,
   connect jumper J14 to the position marked as "RTC + DDR MODE" (different from RTC Only Mode).

In order to enter RTC Only + DDR mode, first disable USB0 and USB1 as wakeup
sources.

.. code-block:: console

   root@am62lxx-evm:~# echo disabled > /sys/devices/platform/bus@f0000/f900000.dwc3-usb/power/wakeup
   root@am62lxx-evm:~# echo disabled > /sys/devices/platform/bus@f0000/f910000.dwc3-usb/power/wakeup

Now the SoC can be suspended using the following command.

.. code-block:: console

   root@am62lxx-evm:~# rtcwake -s 5 -m mem
   rtcwake: assuming RTC uses UTC ...
   rtcwake: wakeup from "mem" using /dev/rtc0 at Thu Jan  1 00:04:20 1970
   [  222.269447] PM: suspend entry (s2idle)
   [  222.273481] Filesystems sync: 0.000 seconds
   [  222.281882] Freezing user space processes
   [  222.291800] Freezing user space processes completed (elapsed 0.002 seconds)
   [  222.298873] OOM killer disabled.
   [  222.302177] Freezing remaining freezable tasks
   [  222.308071] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
   [  222.349890] xhci-hcd xhci-hcd.1.auto: xHC error in resume, USBSTS 0x401, Reinit
   [  222.357227] usb usb1: root hub lost power or was reset
   [  222.362980] xhci-hcd xhci-hcd.1.auto: USB3 root hub has no ports
   [  222.395078] OOM killer enabled.
   [  222.398356] Restarting tasks: Starting
   [  222.419490] Restarting tasks: Done
   [  222.430220] random: crng reseeded on system resumption
   [  222.445468] PM: suspend exit

DeepSleep
*********

DeepSleep AKA Suspend-to-RAM is a low-power mode that allows the SoC
to retain its state in RAM while the processor is turned off.
DeepSleep mode is typically used during inactivity when the user requires very low power
while waiting for an event that requires processing or higher performance. DeepSleep
is a low power mode which still includes DDR in self-refresh, so wakeup events do not
require a full cold boot, significantly reducing wakeup latencies.
Since the power to Always-On power domains are ON throughout DeepSleep,
power to key modules such as GPIO and others is maintained to allow wakeup events
to exit out of this mode.

In order to enter DeepSleep,

   .. code-block:: console

      root@am62lxx-evm:~# echo mem > /sys/power/state
      [   88.507502] PM: suspend entry (deep)
      [   88.530523] Filesystems sync: 0.019 seconds
      [   88.537597] Freezing user space processes
      [   88.543218] Freezing user space processes completed (elapsed 0.001 seconds)
      [   88.550275] OOM killer disabled.
      [   88.553518] Freezing remaining freezable tasks
      [   88.559139] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
      [   88.566570] printk: Suspending console(s) (use no_console_suspend to debug)
      ERROR:   Wake up src 0x80
      ERROR:   Wake up interrupt 0xc
      [   88.591181] Disabling non-boot CPUs ...
      [   88.593309] psci: CPU1 killed (polled 0 ms)
      [   88.594858] Enabling non-boot CPUs ...
      [   88.595327] Detected VIPT I-cache on CPU1
      [   88.595379] GICv3: CPU1: found redistributor 1 region 0:0x0000000001860000
      [   88.595446] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
      [   88.596420] CPU1 is up
      [   88.634778] OOM killer enabled.
      [   88.637926] Restarting tasks ... done.
      [   88.642801] random: crng reseeded on system resumption
      [   88.649913] PM: suspend exit
      root@am62lxx-evm:~#

Memory Usage
************

The following table summarizes the usage of memory in different modes of
operation of the device.

+--------+-------------+----------------------+------------------+------------+-------------------+
| Domain | Memory      | Boot Operation       | Normal Operation | Deep Sleep | RTC Only + DDR    |
+========+=============+======================+==================+============+===================+
| WKUP   | TIFS SRAM   | TIFS load (144 KB)   | TIFS (144 KB)    | TIFS       | TIFS (144 KB)     |
|        | (196 KB)    | + Sec ROM (20 KB)    |                  | (144 KB)   |                   |
|        |             |                      |                  |            | SEC ROM (20 KB)   |
|        |             |                      |                  |            |                   |
|        |             |                      |                  |            | TIFS_STUB (32 KB) |
+--------+-------------+----------------------+------------------+------------+-------------------+
| WKUP   | WKUP PSRAM  | Pub ROM (64 KB)      |                  | A53 Stub,  | Pub ROM (64 KB)   |
|        | (512 KB)    | or (exclusively)     |                  | TF-A Stub  |                   |
|        |             | PreBL Stack &        |                  | (64 KB)    |                   |
|        |             | runtime data (64 KB) |                  |            |                   |
+--------+-------------+----------------------+------------------+------------+-------------------+
| Main   | MAIN MSRAM  | PreBL (64 KB)        | TIFS IPC (24 KB) | TIFS IPC   | PreBL (64 KB)     |
|        | (96 KB)     | DDR initialization   |                  | (24 KB)    | Non-destructive   |
|        |             |                      |                  |            | DDR initializtion |
|        |             | Pub ROM (8 KB)       |                  |            |                   |
|        |             |                      |                  |            | TIFS IPC +        |
|        |             | ROM IPC (8 KB)       |                  |            | ROM IPC (24 KB)   |
|        |             |                      |                  |            |                   |
|        |             |                      |                  |            | Pub ROM (8 KB)    |
+--------+-------------+----------------------+------------------+------------+-------------------+
| Main   | DDR         | Linux                | Linux            | Linux      | Linux             |
|        |             |                      |                  |            |                   |
|        |             | TF-A                 | TF-A             | TF-A       | TF-A              |
+--------+-------------+----------------------+------------------+------------+-------------------+
