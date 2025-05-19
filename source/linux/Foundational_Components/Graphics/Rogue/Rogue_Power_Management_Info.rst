..
    The top level heading in this rst file would be level 2 header with `====`

###########################
Rogue power management info
###########################

Rogue graphics drivers have supported active power management on AXE devices
since TISDK release 8.6 and 8XE/BXS devices since release 9.0 with some
discrepancy in the implementation between cores.

***********************
Active power management
***********************

.. ifconfig:: CONFIG_gpu_ip in ('Rogue_8XE', 'Rogue_BXS')

   In devices running a 8XE or BXS core there are two power domains for the
   GPU. One specifically set aside for the "core" which is the primary device
   running the GPU's firmware, and a second peripheral domain for what
   Imagination refers to as the "dust" components.

   The "dust" components are not necessary for all GPU interactions and as such
   are directly controlled by the GPU core to avoid any unnecessary uptime.

.. ifconfig:: CONFIG_gpu_ip in ('Rogue_AXE')

   In devices running a AXE core there is only one power domain for the GPU.

All interactions require the "core" power domain to be up. Linux controls this
domain through the Active Power Management (APM) hooks in the kernel module.
This domain remains online for all transactions and is offline after an idle
period.

Enabled by default, APM allows modification at runtime through the devices
:file:`/sys/devices/{path_to_device}/power/control` interface. Reading the
device file returns the current setting.

******************
Suspend and resume
******************

Suspend and resume features are also enabled for Rogue cores. The following
procedure will test this on products supporting full device suspend and resume
features:

Start a task to wake up the GPU by using ``glmark2``:

.. code-block:: console

   # glmark2-es2-wayland &

Trigger a suspend event with a scheduled wake-up:

.. code-block:: console

   # rtcwake -s 3 -m mem

Wait for the scheduled wake-up.

The earlier sequence should result in the background compute task pausing during
the suspend action and then resuming after the scheduled wake-up 3 seconds
later.

.. note::

   Driver specific unit tests (such as ``rgx_compute_test``) will hold the
   device in the powered on state starting with driver version 24.1. You cannot
   use these tests as a load when attempting to test suspend and resume
   functionality.
