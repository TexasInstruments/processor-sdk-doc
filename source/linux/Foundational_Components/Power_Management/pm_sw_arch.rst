.. _pm_sw_arch:

##################################
S/W Architecture of System Suspend
##################################

********
Overview
********

TI AM62 family of devices support multiple Suspend-to-RAM modes, including Deep Sleep
and MCU Only as described in :ref:`Low Power Modes<lpm_modes>` section.
The SoC consumes very low power overall yet it is not completely shut off in these modes.
For example, during Deep Sleep, certain IPs
(depending on the power domain to which then belong) will lose context on suspend.
S/W should save and restore the context as required across state transitions. DDR is in self-
refresh to allow context saving.

This section explains the high-level software flow of low power modes in AM62 family of devices.
It also introduces the LPM constraints framework that enables seamless management of
multiple Suspend-to-RAM modes.

*****************************
System diagram and components
*****************************

.. Image:: /images/AM62x_Deep_Sleep_Flow.png


Above diagram has software sequence for how Deep Sleep (ie. Suspend to RAM) works on
SK-AM62 ( Read more on the Starter Kit `here <https://www.ti.com/tool/SK-AM62>`__ ).

Deep Sleep Entry
================

#. The user first instructs the system to suspend. This triggers a suspend
   sequence from Linux side (which runs on the A53 cluster of the SoC).

#. As part of the TI_SCI driver's suspend hook, I/O isolation is invoked which
   isolates all the pads from their respective pinmuxed controllers. Refer to
   :ref:`Wakeup sources Documentation<pm_wakeup_sources>` to understand more on this.

#. Linux then suspends all the drivers in the order that they are probed.
   After ensuring that there were no faults in suspending the drivers, Linux
   then issues core system suspend which ultimately is a PSCI system
   suspend call. Read more about PSCI `here <https://developer.arm.com/Architectures/Power%20State%20Coordination%20Interface>`__

#. At this point only ATF is running on A53 cores and it does the job of
   sending a TISCI Message to the TIFS Core telling it to enter Deep Sleep
   and then it puts A53 into standby.

#. The TIFS Core then encrypts and writes the contents of it's own SRAM to DDR.

#. Further it stops tick timer, disables interrupts that are not needed, and suspends local drivers.
   After the above steps it sends TISCI To DM for Suspend Finish and enters WFI.

#. The DM (Device Manager) is the final entity in this entire Deep Sleep sequence. It does the following:

   a. Saves own context to DDR
   b. Disables Security IP LPSCs, such as LPSC_SAUL.
   c. Disables non-critical "IP-less" LPSCs, such as LPSC_main_test.
   d. Saves MAIN PADCONF MMRs
   e. Saves GTC counter and Disable it.
   f. Finally, Suspends OS.

   The OS in this case is the Free RTOS based Device Manager firmware itself. After this step, it starts performing
   the final few steps toward completion of Suspend to RAM.

#. These steps include the following:

   a. Place DDR into Self Refresh
   b. Place USB into reset isolation
   c. Disable all LPSCs in MAIN except Debug, Always ON
   d. Disable all HSDIVs in MAIN_PLL.
   e. Bypass all MAIN PLLs.
   f. Configure selected wake sources, Enable MAIN IO Isolation.
   g. Disable MCU Core LPSCs, PDs
   h. Bypass MCU PLL

#. Finally, DM R5 Enters WFI with all the other power domains turned OFF except WKUP Always ON.
   DM in WFI will basically wait for the configured wakeup source to trigger
   an interrupt that will act as the wakeup signal.

Deep Sleep Exit
===============

#. External async wakeup from wake source triggers the DM to resume.
#. The DM brings MAIN Domain out of reset.
#. Secure (TIFS) ROM begins to boot.
#. A small piece of code called the FS Stub is required to restore the remaining context and resume the
   TIFS firmware.

   The TIFS Stub is loaded into the ATCM (Tightly Coupled Memory A of the DM R5) during device boot.
   The R5 SPL loads the TIFS Stub (which is a part of tispl.bin) onto DDR at address 0x9dc00000. The DM Firmware
   pulls in this TIFS Stub from DDR RAM to it's ATCM where it then resides as long as the
   device is not shutdown.
#. Then, the rest of the resume sequence is a mirror image of the deep sleep entry sequence.
#. As the A53 core resumes, and subsequently the linux TI_SCI driver's resume hook is called,
   I/O isolation is disabled. This allows the pads to be re-connected to their respective controllers
   and allow the device to function normally post resume.

.. _pm_constraints_fwk:

*************************
LPM constraints framework
*************************

Starting with 10.0 DM firmware and ti-linux-6.6.y kernel, TI is offering
an updated LPM Software Architecture that seamlessly manages the various
Suspend-to-RAM modes supported by AM62 family of devices. The first part
of this architecture is the introduction of "DM Managed" mode []. In this
mode, the DM will by default attempt the deepest low power mode
available during system wide suspend/resume.

However, Linux (or OSes running on remote cores) may want to constrain
the DM for certain use cases.  For example, the deepest state may have
a resume latency that is too long for certain use cases, or a
host OS may want certain wakeup-capable devices to stay enabled during
suspend/resume.

To communicate these constraints to the DM, TI SCI has added new
constraint APIs. On the Linux side, existing per-device PM QoS
framework is used to collect these constraints and then pass them
to the DM. Remote cores can directly register their constraints with
DM using the new constraint APIs.

Types of Constraints
====================

#. **Device Constraint:** The LPM constraint can be set on behalf of a device. By setting this constraint,
   the host ensures that the device will not be powered off or reset in the selected mode.

#. **Resume Latency Constraint:** The LPM resume latency constraint can be set to specify the maximum system
   resume latency value. By setting this constraint, the host ensures that the resume time from selected mode
   will be less than the constraint value.

For more detailed explanation of these constraints, refer to
`TISCI_MSG_LPM_SET_DEVICE_CONSTRAINT <https://software-dl.ti.com/tisci/esd/latest/2_tisci_msgs/pm/lpm.html#tisci-msg-lpm-set-device-constraint>`__
and
`TISCI_MSG_LPM_SET_LATENCY_CONSTRAINT <https://software-dl.ti.com/tisci/esd/latest/2_tisci_msgs/pm/lpm.html#tisci-msg-lpm-set-latency-constraint>`__
of TISCI documentation.

On the Linux side, the constraints framework is managed within TI SCI code.
No new APIs are needed by Linux drivers. Any device that is managed by TI SCI
will be checked for QoS constraints or wakeup capability and the constraints will
be sent to the DM (via the new SCI APIs.)

Specifically, checking of constraints is done at two levels:
1) Runtime PM suspend
2) System-wide suspend

The code enabling the constraints framework can be found in:

#. TISCI PM Domain driver: https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/drivers/pmdomain/ti/ti_sci_pm_domains.c?h=11.02.08
#. TISCI driver: https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/drivers/firmware/ti_sci.c?h=11.02.08

Examples of adding constraints from the remote core side are being implemented and will
be enabled in future release.

How to set constraints
======================

Constraints can be placed from the Linux side in the following ways:

Device Constraint
-----------------

These are automatically placed on behalf of any device that is wakeup-capable or
wakeup-enabled by the TISCI PM domain driver. No additional driver-level changes
are required.

.. note::

   Some devices may disable the wakeup property by default. These can be enabled via
   the sysfs interface (e.g., :file:`/sys/bus/platform/devices/\*/power/wakeup`)

Resume Latency Constraint
-------------------------

This constraint is exposed to the user-level through the existing sysfs PM QoS interface for CPU Cores.
Default constraint is "no constraint", but it can be changed as shown in the examples below:

   a. To set 100 msec resume latency for the SoC, a constraint can be placed for
   CPU0 (or any other CPU core):

   .. code:: console

      root@evm:~# echo 100000 > /sys/devices/system/cpu/cpu0/power/pm_qos_resume_latency_us

   b. To clear the constraint, 0 has to be written to the same parameter:

   .. code:: console

      root@evm:~# echo 0 > /sys/devices/system/cpu/cpu0/power/pm_qos_resume_latency_us

Setting a resume latency constraint impacts the deepest low power mode system can enter.
The various modes and their latencies are documented here: https://downloads.ti.com/tisci/esd/latest/2_tisci_msgs/pm/lpm.html#tisci-msg-lpm-set-latency-constraint

.. note::

   The constraints need to be set before each system suspend as DM firmware clears all
   constraints at resume time.

Constraints and mode selection explained
========================================

By default, if no constraint is set, then the deepest low power mode for SOC is selected.
Otherwise, the mode selection is done as described below:

.. rubric:: Device Constraint:

.. Image:: /images/AM62_LPM_Dev_Cons.png

Above diagram shows the mode selection if constraints are set on MCU_WAKEUP devgroup devices.
As shown, if the constraints are set on WAKEUP Domain devices or Always ON MCU domain devices,
Deep Sleep mode will be selected. Otherwise, MCU Only mode will be selected.

If constraint is put on MAIN devgroup devices, then no low power mode is possible.

.. important::

   USB devices are an exception in MAIN devgroup as there is extra hardware logic preventing
   reset of USB devices in Deep Sleep and MCU Only mode.
   If constraints are set on USB devices, Deep Sleep mode will be selected even though it's
   technically part of MAIN devgroup.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   For detailed description for devgroup of these devices, refer to
   `Devgroup section <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/am62x/soc_devgrps.html#am62x-device-group-descriptions>`__
   of TISCI documentation.

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   For detailed description for devgroup of these devices, refer to
   `Devgroup section <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/am62ax/soc_devgrps.html#am62ax-device-group-descriptions>`__
   of TISCI documentation.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   For detailed description for devgroup of these devices, refer to
   `Devgroup section <https://software-dl.ti.com/tisci/esd/latest/5_soc_doc/am62px/soc_devgrps.html#am62px-device-group-descriptions>`__
   of TISCI documentation.

.. rubric:: Resume Latency Constraint:

The mode selection is done using resume latencies as mentioned in TI SCI LPM Documentation:
`Latency Table <https://software-dl.ti.com/tisci/esd/latest/2_tisci_msgs/pm/lpm.html#latency-table>`__

******************
Learning Resources
******************

#. `AM62x Technical Reference Manual <https://www.ti.com/lit/pdf/spruiv7>`__
#. `Technical White Paper on Enabling Low Power on AM62x <https://www.ti.com/lit/wp/sprad41/sprad41.pdf>`__
#. :ref:`Low Power Modes Documentation<lpm_modes>`

