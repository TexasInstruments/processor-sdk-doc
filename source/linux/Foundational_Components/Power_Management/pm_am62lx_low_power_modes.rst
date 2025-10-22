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

#. RTC Only Plus DDR
#. Deep Sleep

RTC Only Plus DDR
*****************

.. note::

   For this release, the RTC Only + DDR low power mode requires special steps
   to enter. The steps are documented in :ref:`am62l_suspend_workarounds`.

RTC Only + DDR mode is the deepest low power mode that allows the system to enter a state of lowest power consumption
while still retaining the DDR RAM context.

In order to enter RTC Only + DDR mode, first disable USB0 and USB1 as wakeup
sources.

.. code-block:: console

   root@am62lxx-evm:~# echo disabled > /sys/devices/platform/bus@f0000/f900000.dwc3-usb/power/wakeup
   root@am62lxx-evm:~# echo disabled > /sys/devices/platform/bus@f0000/f910000.dwc3-usb/power/wakeup

Now the SoC can be suspended using the following command.

.. code-block:: console

   root@am62lxx-evm:~# echo mem > /sys/power/state
   [   67.335138] PM: suspend entry (deep)
   [   67.358190] Filesystems sync: 0.019 seconds
   [   67.363206] Freezing user space processes
   [   67.368991] Freezing user space processes completed (elapsed 0.001 seconds)
   [   67.376038] OOM killer disabled.
   [   67.379271] Freezing remaining freezable tasks
   [   67.384973] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
   [   67.392398] printk: Suspending console(s) (use no_console_suspend to debug)
   NOTICE:  bl1_plat_arch_setup arch setup
   NOTICE:  Booting Trusted Firmware
   NOTICE:  BL1: v2.12.0(release):11.00.04-7-gaa3963759-dirty
   NOTICE:  BL1: Built : 15:56:37, Feb 25 2025
   NOTICE:  lpdd4_init <--
   NOTICE:  DDR ram size =80000000
   NOTICE:  bl1_platform_setup DDR init done
   NOTICE:  k3_bl1_handoff sent message to tifs
   ERROR:   Wake up src 0x0
   ERROR:   Wake up interrupt 0xc
   [   67.405953] Disabling non-boot CPUs ...
   [   67.408032] psci: CPU1 killed (polled 0 ms)
   [   67.408974] Enabling non-boot CPUs ...
   [   67.409281] Detected VIPT I-cache on CPU1
   [   67.409330] GICv3: CPU1: found redistributor 1 region 0:0x0000000001860000
   [   67.409393] CPU1: Booted secondary processor 0x0000000001 [0x410fd034]
   [   67.410371] CPU1 is up
   [   67.446329] OOM killer enabled.
   [   67.449479] Restarting tasks ... done.
   [   67.454324] random: crng reseeded on system resumption
   [   67.459689] PM: suspend exit


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
