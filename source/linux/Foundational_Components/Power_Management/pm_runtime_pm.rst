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

.. ifconfig:: CONFIG_part_variant in ('AM62DX')

    McASP, OSPI, MCAN.

.. rubric:: Driver Usage

Linux provides the following sysfs interface (/sys/devices/.../power/)
to control the Runtime PM behavior at per device level:

#. *autosuspend_delay_ms:* desired period of inactivity until which runtime suspend will be automatically delayed.
#. *control:* if set to "auto", driver manages power at runtime. If set to "on", it basically turns off runtime pm for the device.
#. *runtime_active_time:* period that device has been active.
#. *runtime_status:* current status of the device. It can be suspended, active, or unsupported.
#. *runtime_suspended_time:* period that device has been suspended.

For example, here are the default values for OSPI device:

.. code-block:: console

   root@<machine>:~# tail -n +1 /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/*
   ==> /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/autosuspend_delay_ms <==
   2000

   ==> /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/control <==
   auto

   ==> /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/runtime_active_time <==
   8612

   ==> /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/runtime_status <==
   suspended

   ==> /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/runtime_suspended_time <==
   734540

To disable Runtime PM for the OSPI device, the "control" parameter can be
changed to "on":

.. code-block:: console

   root@<machine>:~# echo on > /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/control
   root@<machine>:~# tail -n +1 /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/*
   ==> /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/autosuspend_delay_ms <==
   2000

   ==> /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/control <==
   on

   ==> /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/runtime_active_time <==
   11797

   ==> /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/runtime_status <==
   active

   ==> /sys/devices/platform/bus@f0000/fc00000.bus/fc40000.spi/power/runtime_suspended_time <==
   770604
