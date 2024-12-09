..
    The top level heading in this rst file would be level 2 header with `====`

###########################
Rogue Power Management Info
###########################

Rogue graphics drivers have supported active power management on AXE devices
since TISDK release 8.6 and 8XE/BXS devices since release 9.0 with some
discrepancy in the implementation between cores.

***
APM
***

.. ifconfig:: CONFIG_gpu_ip in ('Rogue_8XE', 'Rogue_BXS')

   In devices running a 8XE or BXS core there are two power domains for the
   GPU. One specifically set aside for the "core" which is the primary device
   running the GPU's firmware, and a second peripheral domain for what
   Imagination refers to as the "dust" components.

   The "dust" components are not necessary for all GPU interactions and as such
   are directly controlled by the GPU core to avoid any unnecessary uptime.

.. ifconfig:: CONFIG_gpu_ip in ('Rogue_AXE')

   In devices running a AXE core there is only one power domain for the GPU.

The "core" power domain is required for all interactions. This power domain is
controlled directly by Linux through APM hooks in the kernel module. This
domain is powered up for all transactions and subsequently powered down after
an idle period.

Active Power Management is enabled by default, but it can be disabled at runtime
by setting the power control to "on" through the devices
:file:`/sys/devices/{path-to-device}/power/control` interface. Subsequently, it's
status can be checked by reading that device file.

****************
Suspend & Resume
****************

Suspend and resume features are also enabled for Rogue cores. To test this
manually the following procedure can be used on products supporting full device
suspend / resume features:

Initiate a load to wake up the GPU using ``glmark2``:

.. code-block:: console

   # glmark2-es2-wayland &

Trigger a suspend event with a scheduled wakeup:

.. code-block:: console

   # rtcwake -s 3 -m mem

Wait for the scheduled wakeup.

The above sequence should result in the background compute task being paused
for the suspend action and then resumed after the scheduled wakeup 3 seconds
later.

.. note::

   Driver specific unit tests (like ``rgx_compute_test``) will hold the device
   in the powered on state starting with driver version 24.1. You cannot use
   these tests as a load when attempting to test suspend/resume functionality.
