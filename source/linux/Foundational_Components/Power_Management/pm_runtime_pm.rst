##########
Runtime PM
##########

.. rubric:: Overview

Runtime Power Management (PM) framework reduces the active power
consumption of the SoC by allowing individual devices to suspend
themselves when they are idle. The decision to suspend is driven by the
device independently of the overall system state or any other devices
(except parent device). It is not necessary for the user space to idle
for a device to runtime suspend itself. Each device selects its desired
low power state based on its internal hardware capabilities like clock
and power domain, and wake-up capabilities. For more details, please
refer to the Linux Kernel documentation on `Runtime PM <https://docs.kernel.org/power/runtime_pm.html>`__.

.. rubric:: Supported Devices

The following drivers have been validated for Runtime PM in this release:

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    DSS, GPU, DPHY, CSI, McASP, OSPI, MCAN.

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    DSS, McASP, OSPI, MCAN, Video Codec, JPEG Encode.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    DSS, GPU, McASP, OSPI, MCAN, Video Codec.

.. rubric:: Driver Usage

Linux provides the following sysfs interface (/sys/devices/.../power/)
to control the Runtime PM behavior at per device level:

#. *autosuspend_delay_ms:* desired period of inactivity until which runtime suspend will be automatically delayed.
#. *control:* if set to "auto", driver manages power at runtime. If set to "on", it basically turns off runtime pm for the device.
#. *runtime_active_time:* period that device has been active.
#. *runtime_status:* current status of the device. It can be suspended, active, or unsupported.
#. *runtime_suspended_time:* period that device has been suspended.

For example, here are the default values for DSS device:

.. code-block:: console

    root@am62xx-evm:~# tail -n +1 /sys/devices/platform/bus@f0000/30200000.dss/power/*
    ==> /sys/devices/platform/bus@f0000/30200000.dss/power/autosuspend_delay_ms <==
    1000

    ==> /sys/devices/platform/bus@f0000/30200000.dss/power/control <==
    auto

    ==> /sys/devices/platform/bus@f0000/30200000.dss/power/runtime_active_time <==
    24129

    ==> /sys/devices/platform/bus@f0000/30200000.dss/power/runtime_status <==
    active

    ==> /sys/devices/platform/bus@f0000/30200000.dss/power/runtime_suspended_time <==
    0

To disable Runtime PM for the DSS device, the "control" parameter can be
changed to "on":

.. code-block:: console

    root@<machine>:~# echo on > /sys/devices/platform/bus@f0000/30200000.dss/power/control
    root@<machine>:~# cat /sys/devices/platform/bus@f0000/30200000.dss/power/*
    1000
    on
    4629
    active
    199277671
