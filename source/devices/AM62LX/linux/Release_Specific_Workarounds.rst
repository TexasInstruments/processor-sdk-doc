###############################
System Suspend Mode Workarounds
###############################

This patch updates the system suspend mode indication for the AM62L platform.

ARM Trusted Firmware side changes
*********************************

.. code-block:: diff

   diff --git a/plat/ti/k3/common/am62l_psci.c b/plat/ti/k3/common/am62l_psci.c
   index 70f2aecdd..115729f4a 100644
   --- a/plat/ti/k3/common/am62l_psci.c
   +++ b/plat/ti/k3/common/am62l_psci.c
   @@ -133,7 +133,7 @@ static void am62l_pwr_domain_suspend(const psci_power_state_t *target_state)
   	/* TODO: Pass the mode passed from kernel using s2idle
   	 * For now make mode=6 for RTC only + DDR and mdoe=0 for deepsleep
   	 */
   -       uint32_t mode = 0;
   +       uint32_t mode = 6;
   
   	core = plat_my_core_pos();
   	proc_id = PLAT_PROC_START_ID + core;

The change is made in :file:`plat/ti/k3/common/am62l_psci.c`, which is the new PSCI driver for AM62L in Arm Trusted Firmware.
The :func:`am62l_pwr_domain_suspend` function has been modified to change the default system suspend mode from deep sleep
to RTC only + DDR.

The default mode indicates a deep sleep state, which provides the lowest latency wake-up times but also consumes
more power. In contrast, the new default mode, RTC only + DDR, offers a lower power consumption profile but at the cost
of higher latency wake-up times.

This change sets the default system suspend mode indication to 6, which corresponds to the RTC only + DDR mode.

This change is a temporary solution, as the ultimate goal is to pass the suspend mode from the kernel using the s2idle
mechanism.

Linux-side changes
******************

Since there are a few new drivers in AM62L, they are yet to add suspend resume support
functionality in Linux. Hence, to avoid any blockers during suspend resume of Linux
make use of the :file:`k3-am62l3-evm-lpmdemo.dtb` instead of the regular :file:`k3-am62l3-evm.dtb`.

One can find the DT source of this file from
`here <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62l3-evm-lpmdemo.dts?h=11.00.05>`__.

The :file:`k3-am62l3-evm-lpmdemo.dtb` file disables many drivers which may not behave well during suspend/resume
of the device. These are planned to be enabled in the future after fixing any suspend resume related issues
and thorough testing.

How-to suspend/resume
*********************

To suspend the device, use the following command in Linux:

.. code-block:: console

   $ echo mem > /sys/power/state

To resume the device, press the following button on the EVM:

.. image:: /images/am62l_lpm_wakeup_evm_pin.jpg

.. important::

    Only the above button ie. the RTC ext pin is wake up capable as of now. More wakeup sources
    will be added in the future.
