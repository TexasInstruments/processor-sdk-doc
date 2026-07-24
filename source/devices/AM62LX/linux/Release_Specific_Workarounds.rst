.. _am62l_suspend_workarounds:

###############################
System Suspend Mode Workarounds
###############################

ARM Trusted Firmware changes
****************************

The AM62L platform supports multiple low power modes. ARM Trusted Firmware (TF-A) sets the
active mode through the ``mode`` variable in the :func:`am62l_pwr_domain_suspend`
function. The following table lists all available modes:

+--------------+---------------------------+----------------------------------------------+
| Mode Value   | Low Power Mode            | Description                                  |
+==============+===========================+==============================================+
| 0            | DeepSleep                 | Default mode. Low latency, higher power      |
+--------------+---------------------------+----------------------------------------------+
| 6            | RTC + I/O + DDR           | Lowest power with DDR retention              |
+--------------+---------------------------+----------------------------------------------+
| 8            | DSS plus DeepSleep        | DeepSleep with Display Subsystem powered     |
+--------------+---------------------------+----------------------------------------------+

To change the low power mode, modify the ``mode`` value in the TF-A source code as shown in the following code block.
After making the changes, re-build the TF-A and then re-package it in the
:file:`tispl.bin` file to ensure the changes take effect. To learn more about TF-A and how to
rebuild it, see :ref:`foundational-components-atf`. For rebuilding U-Boot and generating the new
:file:`tispl.bin` follow :ref:`Build-U-Boot-label`.

.. code-block:: diff

   diff --git a/plat/ti/k3low/common/am62l_psci.c b/plat/ti/k3low/common/am62l_psci.c
   index 6bb9a4298..d8da7e6a9 100644
   --- a/plat/ti/k3low/common/am62l_psci.c
   +++ b/plat/ti/k3low/common/am62l_psci.c
   @@ -233,7 +233,7 @@ static int am62l_validate_power_state(unsigned int power_state,
    static void am62l_pwr_domain_suspend(const psci_power_state_t *target_state)
    {
           uint32_t core, proc_id;
   -       uint32_t mode = 0;
   +       uint32_t mode = 6;
           core = plat_my_core_pos();
           uint64_t context_save_addr = TIFS_LPM_SAVE_CTX;

This modifies :file:`plat/ti/k3/common/am62l_psci.c`, the PSCI driver for AM62L in
Arm Trusted Firmware. The previous example changes the default suspend mode from DeepSleep
(mode 0) to RTC + I/O + DDR (mode 6). Replace the ``mode`` value with any value from the
table shown to select a different low power mode.

.. note::

   This is a workaround required for selecting the low power mode when using ``[deep]`` in the :file:`/sys/power/suspend` interface.
   A more robust solution to select the suspend mode at runtime from the kernel is by using the ``[s2idle]`` mechanism, without requiring
   a firmware rebuild. See :ref:`pm_s2idle_psci` for details.

Once :file:`tispl.bin` is rebuilt and packaged, continue with entering LPM as described in :ref:`lpm_modes`.
