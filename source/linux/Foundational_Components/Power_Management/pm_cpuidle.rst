.. _cpuidle-guide:

#######
CPUIdle
#######

.. rubric:: Overview

The cpuidle framework consists of two key components:

A governor that decides the target C-state of the system. A driver that
implements the functions to transition to target C-state. The idle loop
is executed when the Linux scheduler has no thread to run. When the idle
loop is executed, current 'governor' is called to decide the target
C-state. Governor decides whether to continue in current state/
transition to a different state. Current 'driver' is called to
transition to the selected state.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX', 'J722S')

    .. rubric:: Standby Mode

    On |__PART_FAMILY_DEVICE_NAMES__| platforms, "Standby" mode is implemented through the Linux CPUIdle
    framework. Standby is the default low-power state that the system enters automatically when idle,
    using the WFI (Wait For Interrupt) C-state. This power-saving mechanism activates whenever the
    system is "just sitting idle" without requiring any special configuration or activation from
    the user.

    When your device appears inactive, it is actually cycling in and out of this standby state
    many times per second, seamlessly managing power while remaining responsive.

    .. rubric:: Enable Standby

    In order to enable Standby the `k3-am62x-sk-lpm-standby.dtso
    <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-lpm-standby.dtso?h=11.01.05>`__
    overlay should be applied. Refer to :ref:`How to enable DT overlays
    <howto_dt_overlays>` for more details. More information on what the overlay
    does is in the :ref:`linux-device-tree-label` section.

    .. rubric:: Standby Implementation Architecture

    For |__PART_FAMILY_DEVICE_NAMES__|, the Standby implementation involves a multi-layer architecture:

    1. **Linux CPUIdle Framework**:
       - Determines when to place CPUs into idle states based on system activity
       - Uses governors (like the menu governor) to predict how long CPUs will be idle
       - Invokes platform-specific drivers to transition to appropriate C-states

    2. **ARM Generic CPUIdle Driver**:
       - Implements the Linux CPUIdle driver interface for ARM platforms
       - Communicates with TF-A through PSCI SMC (Secure Monitor Call) interface

    3. **PSCI Interface in Linux**:
       - Provides a standardized method for the kernel to request power management operations
       - Translates Linux-side requests into PSCI calls to TF-A

    4. **TF-A PSCI Implementation**:
       - Runs in secure world (EL3)
       - Implements the PSCI specification
       - Provides platform-specific handlers via the ``plat_psci_ops`` structure

    When your system goes idle, the following sequence occurs:

    - Linux idle loop detects no runnable tasks
    - CPUIdle governor selects the appropriate C-state ("stby" for these platforms)
    - CPUIdle driver communicates with TF-A via the PSCI interface
    - TF-A's PSCI implementation validates the requested power state through ``validate_power_state()``
    - TF-A executes the ``cpu_standby()`` handler from ``plat_psci_ops``
    - The actual WFI instruction is executed within the TF-A's standby handler
    - On interrupt: CPU automatically exits WFI state
    - Control returns to Linux

    This automated process happens continuously during system operation, seamlessly
    transitioning between active and idle states to save power whenever possible.

    .. rubric:: Standby vs. Deep Sleep: Understanding the Difference

    It's important to distinguish between the lightweight "standby" provided by CPUIdle and deeper sleep states:

    * **CPUIdle Standby (WFI)**:
      - Processor-level power saving only
      - Very fast entry and exit (microseconds)
      - Occurs automatically hundreds of times per second
      - No user intervention required
      - All peripherals remain operational
      - Perfect for normal "idle" periods

    * **Deep Sleep Modes**:
      - System-wide power saving
      - Slower entry and exit (milliseconds to seconds)
      - Requires explicit software requests
      - May require peripheral reconfiguration
      - Suitable for extended inactive periods

    .. rubric:: Source Location

    **Linux Side**:

    - :file:`drivers/cpuidle/cpuidle-arm.c` - ARM CPU idle driver
    - :file:`drivers/cpuidle/dt_idle_states.c` - Device tree parsing for idle states
    - :file:`drivers/cpuidle/cpuidle.c` - Core CPUIdle framework
    - :file:`kernel/sched/idle.c` - Kernel idle loop implementation
    - :file:`drivers/firmware/psci.c` - PSCI interface to TF-A

    **TF-A Side** (not part of Linux kernel):

    - :file:`plat/ti/k3/common/k3_psci.c` - PSCI implementation for K3 platforms

    .. _linux-device-tree-label:

    .. rubric:: Linux Device Tree Implementation

    In order to implement Standby in Linux, an idle-states node has to be added
    and then referenced by the CPU node. The `k3-am62x-sk-lpm-standby.dtso
    <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-lpm-standby.dtso?h=11.01.05>`__
    can be used as a reference.

    .. code-block:: dts

       idle-states {
                entry-method = "psci";

                CPU_SLEEP_0: stby {
                        compatible = "arm,idle-state";
                        idle-state-name = "standby";
                        arm,psci-suspend-param = <0x00000001>;
                        entry-latency-us = <100>;
                        exit-latency-us = <50>;
                        min-residency-us = <1000>;
                };
        };


    The ``entry-latency-us``, ``exit-latency-us``, and ``min-residency-us``
    properties are explained in depth `here
    <https://www.kernel.org/doc/Documentation/devicetree/bindings/arm/idle-states.txt>`__.
    The ``min-residency-us`` can be fine tuned to change the minimum amount of
    time Linux is in idle which can change the power savings.

    .. rubric:: Driver Usage

    CPUIdle works automatically once enabled in the kernel, with no user intervention required.
    The CPUIdle framework statistics can be accessed through the sysfs interface:

    .. code-block:: console

       # ls -l /sys/devices/system/cpu/cpu0/cpuidle/
       drwxr-xr-x    2 root     root             0 Jan  1 00:01 state0
       drwxr-xr-x    2 root     root             0 Jan  1 00:01 state1

       # ls -l /sys/devices/system/cpu/cpu0/cpuidle/state1/
       -r--r--r--    1 root     root         4096 Jan  1 00:02 desc
       -r--r--r--    1 root     root         4096 Jan  1 00:02 latency
       -r--r--r--    1 root     root         4096 Jan  1 00:02 name
       -r--r--r--    1 root     root         4096 Jan  1 00:02 power
       -r--r--r--    1 root     root         4096 Jan  1 00:02 time
       -r--r--r--    1 root     root         4096 Jan  1 00:02 usage

    To view the current C-state statistics:

    .. code-block:: console

       # cat /sys/devices/system/cpu/cpu0/cpuidle/state1/name
       stby
       # cat /sys/devices/system/cpu/cpu0/cpuidle/state1/usage
       6245738

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family')

    .. rubric:: Driver Features

    AM335x supports two different C-states

    -  MPU WFI
    -  MPU WFI + Clockdomain gating

    AM437x supports two different C-states

    -  MPU WFI
    -  MPU WFI + Clockdomain gating

    .. rubric:: Source Location

    arch/arm/mach-omap2/pm33xx-core.c
    drivers/soc/ti/pm33xx.c
    drivers/cpuidle/cpuidle-arm.c

    .. rubric:: Kernel Configuration Options

    The driver can be built into the kernel as a static module.

    $ make menuconfig

    Select CPU Power Management from the main menu.

    .. code-block:: text

        ...
        ...
        Boot options --->
        CPU Power Management --->
        Floating point emulation --->
        ...

    Select CPU Idle as shown here:

    .. code-block:: text

        ...
        ...
            CPU Frequency Scaling --->
            CPU Idle --->
        ...

    All relevant options are listed below:

    .. code-block:: text

            [*] CPU idle PM support
            [ ]   Support multiple cpuidle drivers
            [*]   Ladder governor (for periodic timer tick)
            -*-   Menu governor (for tickless system)
                    ARM CPU Idle Drivers  ----

    .. rubric:: DT Configuration

    .. code-block:: dts

        cpus {
                cpu: cpu0 {
                        compatible = "arm,cortex-a9";
                        enable-method = "ti,am4372";
                        device-type = "cpu";
                        reg = <0>;

                        cpu-idle-states = <&mpu_gate>;
                };

                idle-states {
                        compatible = "arm,idle-state";
                        entry-latency-us = <40>;
                        exit-latency-us = <100>;
                        min-residency-us = <300>;
                        local-timer-stop;
                };
        };

    .. rubric:: Driver Usage

    CPUIdle requires no intervention by the user for it to work, it just
    works transparently in the background. By default the ladder governor is
    selected.

    It is possible to get statistics about the different C-states during
    runtime, such as how long each state is occupied.

    .. code-block:: console

       # ls -l /sys/devices/system/cpu/cpu0/cpuidle/state0/
       -r--r--r--    1 root     root         4096 Jan  1 00:02 desc
       -r--r--r--    1 root     root         4096 Jan  1 00:02 latency
       -r--r--r--    1 root     root         4096 Jan  1 00:02 name
       -r--r--r--    1 root     root         4096 Jan  1 00:02 power
       -r--r--r--    1 root     root         4096 Jan  1 00:02 time
       -r--r--r--    1 root     root         4096 Jan  1 00:02 usage
       # ls -l /sys/devices/system/cpu/cpu0/cpuidle/state1/
       -r--r--r--    1 root     root         4096 Jan  1 00:05 desc
       -r--r--r--    1 root     root         4096 Jan  1 00:05 latency
       -r--r--r--    1 root     root         4096 Jan  1 00:03 name
       -r--r--r--    1 root     root         4096 Jan  1 00:05 power
       -r--r--r--    1 root     root         4096 Jan  1 00:05 time
       -r--r--r--    1 root     root         4096 Jan  1 00:02 usage

