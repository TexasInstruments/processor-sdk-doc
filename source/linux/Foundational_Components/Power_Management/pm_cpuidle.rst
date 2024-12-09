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

    The A53 cores on |__PART_FAMILY_DEVICE_NAMES__| currently support only the Wait for Interrupt (WFI)
    C-state. This state gets enabled by default in the CPUIdle driver without
    requiring any additional DT configuration.

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

