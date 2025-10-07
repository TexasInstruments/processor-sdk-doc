.. _am62l_suspend_workarounds:

###############################
System Suspend Mode Workarounds
###############################

ARM Trusted Firmware changes
****************************

This patch updates the system suspend mode for the AM62L platform. After making the following changes,
re-build the ARM Trusted Firmware and then re-package it in the :file:`tispl.bin` file to ensure
the changes take effect. To learn more about TF-A and how to rebuild it, see :ref:`_foundational-components-atf`.
For rebuilding u-boot and generating the new :file:`tispl.bin` follow :ref:`Build-U-Boot-label`.

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

This modifies :file:`plat/ti/k3/common/am62l_psci.c`, which is the new Power
State Coordination Interface (PSCI) driver for AM62L in Arm Trusted Firmware.
The :func:`am62l_pwr_domain_suspend` function will change the default system
suspend mode from Deep Sleep to RTC only + DDR.

The default mode of 0 is the deep sleep state. Deep Sleep provides the lowest
latency wake-up but also uses more power. The updated default mode of 6 is
the RTC only + DDR state. In contrast, RTC only + DDR offers a lower power
consumption profile, but at the cost of higher wake-up latency.

This change is a temporary solution. A more robust solution is under development to pass a suspend parameter from the kernel
by leveraging the s2idle mechanism.

Once :file:`tispl.bin` is rebuilt and packaged, continue with entering LPM as described in :ref:`am62lx-power-management`.
