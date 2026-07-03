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
#. DSS plus Deep Sleep

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

RTC Only Plus DDR
*****************

.. note::

   Please go through the s2idle docs to understand how to select between multiple low power modes.
   The steps and overall architecture/ sequence diagrams are documented in :ref:`pm_s2idle_psci`.
   The default mode via s2idle is RTC Only Plus DDR, since it's the deepest.

   If regular [mem] interface is selected in `/sys/power/mem_sleep`, the RTC Only + DDR low power mode
   requires special steps to enter. The steps are documented in :ref:`am62l_suspend_workarounds`.

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

DSS plus Deep Sleep
*******************

DSS plus Deep Sleep is a low-power mode where the Display Subsystem (DSS) is **ON** to display
a static image while the rest of the system enters Deep Sleep. This mode is useful for
applications that need to keep visual output during system suspend, such as displaying
status information, warnings, or other static content while minimizing overall power consumption.

In DSS plus Deep Sleep mode, the system state stays in RAM with DDR in self-refresh,
similar to standard Deep Sleep. The key difference is that the DSS remains active and
powered to continue driving the display with a static framebuffer. The DSS has a self-refresh
feature that allows it to fetch the framebuffer from its internal memory instead of accessing
DDR, which helps reduce power consumption while maintaining display output.

How It Works
============

DSS plus Deep Sleep requires two display properties:

**SELF_REFRESH**

This property enables the DSS hardware to replay the last displayed frame from its internal
on-chip memory (a small FIFO buffer) instead of continuously fetching from DDR. This
significantly reduces memory bandwidth and power consumption during suspend.

The AM62L-DSS has a 20 KB FIFO buffer. For the self-refresh feature to work, the static
image must fit within this buffer. The size is:

   **Frame Size = Width × Height × Bytes-per-pixel**

For NV12 format (1.5 bytes per pixel), this means:

   **Width × Height × 1.5 ≤ 20,480 bytes**

   **Width × Height ≤ 13,653 pixels**

For example, a 116×116 NV12 image requires 116 × 116 × 1.5 = 20,184 bytes, which is the
maximum size that fits within the 20 KB limit. If the frame is too large, self-refresh will
not activate.

**ALWAYS_ON_DISPLAY**

This property keeps the display pipeline powered on during system suspend. Without this,
the display would be turned off even if self-refresh is active. Together with self-refresh,
it ensures the static frame remains visible throughout the suspend period.

Entering DSS plus Deep Sleep Mode
=================================

Entering DSS plus Deep Sleep requires several steps to configure the display subsystem properly.
First, stop any display manager service that might be actively managing the display:

.. code-block:: console

   root@am62lxx-evm:~# systemctl stop emptty

Next, enable always on display to keep the screen active and the DSS self-refresh feature.
This configures the display controller to fetch the framebuffer from its internal memory
instead of accessing DDR. Use ``modetest -M tidss -p`` or ``kmsprint`` to check the CRTC ID
(for ALWAYS_ON_DISPLAY) and plane ID (for SELF_REFRESH) on your system:

.. code-block:: console

   root@am62lxx-evm:~# modetest -M tidss -w 42:ALWAYS_ON_DISPLAY:1  # 42 is the CRTC ID
   root@am62lxx-evm:~# modetest -M tidss -w 35:SELF_REFRESH:1       # 35 is the plane ID

Display a static image on the screen that remains visible during suspend. This example
uses GStreamer to display a test pattern. Press Ctrl+C to terminate the pipeline. This
keeps the last frame on the screen, allowing the system to enter low power mode:

.. code-block:: console

   root@am62lxx-evm:~# gst-launch-1.0 videotestsrc pattern=ball ! video/x-raw, width=50, height=50, framerate=60/1, format=RGB ! fpsdisplaysink text-overlay=false video-sink="kmssink can-scale=false sync=false" sync=false -v
   Setting pipeline to PAUSED ...
   Pipeline is PREROLLING ...
   /GstPipeline:pipeline0/GstFPSDisplaySink:fpsdisplaysink0/GstKMSSink:kmssink0: display-width = 800
   /GstPipeline:pipeline0/GstFPSDisplaySink:fpsdisplaysink0/GstKMSSink:kmssink0: display-height = 480
   /GstPipeline:pipeline0/GstFPSDisplaySink:fpsdisplaysink0/GstKMSSink:kmssink0: sync = false
   /GstPipeline:pipeline0/GstVideoTestSrc:videotestsrc0.GstPad:src: caps = video/x-raw, format=(string)RGB, width=(int)50, height=(int)50, framerate=(fraction)60/1, multiview-mode=(string)mono, pixel-aspect-ratio=(fraction)16/15, interlace-mode=(string)progressive
   /GstPipeline:pipeline0/GstCapsFilter:capsfilter0.GstPad:src: caps = video/x-raw, format=(string)RGB, width=(int)50, height=(int)50, framerate=(fraction)60/1, multiview-mode=(string)mono, pixel-aspect-ratio=(fraction)16/15, interlace-mode=(string)progressive
   /GstPipeline:pipeline0/GstFPSDisplaySink:fpsdisplaysink0.GstGhostPad:sink.GstProxyPad:proxypad0: caps = video/x-raw, format=(string)RGB, width=(int)50, height=(int)50, framerate=(fraction)60/1, multiview-mode=(string)mono, pixel-aspect-ratio=(fraction)16/15, interlace-mode=(string)progressive
   /GstPipeline:pipeline0/GstFPSDisplaySink:fpsdisplaysink0/GstKMSSink:kmssink0.GstPad:sink: caps = video/x-raw, format=(string)RGB, width=(int)50, height=(int)50, framerate=(fraction)60/1, multiview-mode=(string)mono, pixel-aspect-ratio=(fraction)16/15, interlace-mode=(string)progressive
   /GstPipeline:pipeline0/GstFPSDisplaySink:fpsdisplaysink0.GstGhostPad:sink: caps = video/x-raw, format=(string)RGB, width=(int)50, height=(int)50, framerate=(fraction)60/1, multiview-mode=(string)mono, pixel-aspect-ratio=(fraction)16/15, interlace-mode=(string)progressive
   /GstPipeline:pipeline0/GstCapsFilter:capsfilter0.GstPad:sink: caps = video/x-raw, format=(string)RGB, width=(int)50, height=(int)50, framerate=(fraction)60/1, multiview-mode=(string)mono, pixel-aspect-ratio=(fraction)16/15, interlace-mode=(string)progressive
   Pipeline is PREROLLED ...
   Setting pipeline to PLAYING ...
   Redistribute latency...
   New clock: GstSystemClock
   /GstPipeline:pipeline0/GstFPSDisplaySink:fpsdisplaysink0/GstKMSSink:kmssink0: sync = false
   /GstPipeline:pipeline0/GstFPSDisplaySink:fpsdisplaysink0: last-message = rendered: 16, dropped: 0, current: 30.68, average: 30.68
   /GstPipeline:pipeline0/GstFPSDisplaySink:fpsdisplaysink0: last-message = rendered: 32, dropped: 0, current: 30.05, average: 30.36
   handling interrupt.:99.
   Interrupt: Stopping pipeline ...
   Execution ended after 0:00:01.497017765
   Setting pipeline to NULL ...
   Freeing pipeline ...

After the GStreamer pipeline terminates, the last displayed frame remains on the screen.
Configure the system to use s2idle suspend which will allow the system to enter the lowest
power state available. Since the display is configured to be ALWAYS ON, DeepSleep + DSS is
the lowest available power state:

.. code-block:: console

   root@am62lxx-evm:~# echo s2idle > /sys/power/mem_sleep

The SoC can now suspend using the following command:

.. code-block:: console

   root@am62lxx-evm:~# echo mem > /sys/power/state
   [  101.964352] PM: suspend entry (s2idle)
   [  101.968392] Filesystems sync: 0.000 seconds
   [  101.973713] Freezing user space processes
   [  101.980059] Freezing user space processes completed (elapsed 0.002 seconds)
   [  101.987068] OOM killer disabled.
   [  101.990296] Freezing remaining freezable tasks
   [  101.996139] Freezing remaining freezable tasks completed (elapsed 0.001 seconds)
   [  102.027260] k3_wkup_src_notify wkup-src-notify: wakeup source:0x10000, pin:0x6d, mode:0x8
   [  102.060012] am65-cpsw-nuss 8000000.ethernet: set new flow-id-base 96
   [  102.080175] am65-cpsw-nuss 8000000.ethernet eth0: PHY [8000f00.mdio:00] driver [TI DP83867] (irq=POLL)
   [  102.090380] am65-cpsw-nuss 8000000.ethernet eth0: configuring for phy/rgmii-rxid link mode
   [  102.112383] am65-cpsw-nuss 8000000.ethernet eth1: PHY [8000f00.mdio:01] driver [TI DP83867] (irq=POLL)
   [  102.122586] am65-cpsw-nuss 8000000.ethernet eth1: configuring for phy/rgmii-rxid link mode
   [  102.474090] OOM killer enabled.
   [  102.477363] Restarting tasks: Starting
   [  102.499994] Restarting tasks: Done
   [  102.503505] random: crng reseeded on system resumption
   [  102.509008] PM: suspend exit
   root@am62lxx-evm:~#

Changing from Always-On Static Display to Active Dynamic Display
=================================================================

After the system resumes from DSS plus Deep Sleep, the static frame continues to be displayed
from the FIFO. The display does **not** automatically change back to dynamic content.
To return to normal active display operation, disable the SELF_REFRESH and ALWAYS_ON_DISPLAY
properties:

.. code-block:: console

   root@am62lxx-evm:~# modetest -M tidss -w 35:SELF_REFRESH:0  # Disable FIFO replay
   root@am62lxx-evm:~# modetest -M tidss -w 42:ALWAYS_ON_DISPLAY:0  # Allow display pipeline to be powered off

Once disabled, the display subsystem returns to fetching framebuffers
from DDR and can display dynamic content normally. Any display manager or application can
then take control of the display again.

Memory Usage
************

The following table summarizes the usage of memory in different modes of
operation of the device.

+--------+-------------+----------------------+------------------+-------------------------+-------------------+
| Domain | Memory      | Boot Operation       | Normal Operation | Deep Sleep /            | RTC Only + DDR    |
|        |             |                      |                  | DSS plus Deep Sleep     |                   |
+========+=============+======================+==================+=========================+===================+
| WKUP   | TIFS SRAM   | TIFS load (144 KB)   | TIFS (144 KB)    | TIFS                    | TIFS (144 KB)     |
|        | (196 KB)    | + Sec ROM (20 KB)    |                  | (144 KB)                |                   |
|        |             |                      |                  |                         | SEC ROM (20 KB)   |
|        |             |                      |                  |                         |                   |
|        |             |                      |                  |                         | TIFS_STUB (32 KB) |
+--------+-------------+----------------------+------------------+-------------------------+-------------------+
| WKUP   | WKUP PSRAM  | Pub ROM (64 KB)      |                  | A53 Stub,               | Pub ROM (64 KB)   |
|        | (512 KB)    | or (exclusively)     |                  | TF-A Stub               |                   |
|        |             | PreBL Stack &        |                  | (64 KB)                 |                   |
|        |             | runtime data (64 KB) |                  |                         |                   |
+--------+-------------+----------------------+------------------+-------------------------+-------------------+
| Main   | MAIN MSRAM  | PreBL (64 KB)        | TIFS IPC (24 KB) | TIFS IPC                | PreBL (64 KB)     |
|        | (96 KB)     | DDR initialization   |                  | (24 KB)                 | Non-destructive   |
|        |             |                      |                  |                         | DDR initializtion |
|        |             | Pub ROM (8 KB)       |                  |                         |                   |
|        |             |                      |                  |                         | TIFS IPC +        |
|        |             | ROM IPC (8 KB)       |                  |                         | ROM IPC (24 KB)   |
|        |             |                      |                  |                         |                   |
|        |             |                      |                  |                         | Pub ROM (8 KB)    |
+--------+-------------+----------------------+------------------+-------------------------+-------------------+
| Main   | DDR         | Linux                | Linux            | Linux                   | Linux             |
|        |             |                      |                  |                         |                   |
|        |             | TF-A                 | TF-A             | TF-A                    | TF-A              |
+--------+-------------+----------------------+------------------+-------------------------+-------------------+
