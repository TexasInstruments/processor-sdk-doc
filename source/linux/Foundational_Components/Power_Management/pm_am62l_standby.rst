.. _am62l_standby_mode:

##################
AM62L Standby Mode
##################

********
Overview
********

Unlike system suspend modes that require explicit user intervention, Standby Mode operates transparently
during normal system operation. The system continuously evaluates the idle state of processor clusters and
automatically adjusts clock frequencies, disables non-critical power domains, and enables DDR auto-self-refresh
when all cores are idle. On receiving an interrupt, quickly restores full operational state.

Key characteristics of this opportunistic approach:

* **Automatic Operation**: No user configuration required; the system continuously monitors CPU activity and automatically enters power-saving states when cores are idle, then exits when work resumes. This contrasts with system suspend modes that require explicit commands.
* **Transparent**: Happens silently in the background during normal idle periods
* **Fast Response**: Wakeup latency is in microseconds, meaning the system can instantly resume full performance when an interrupt arrives. This makes standby suitable for real-time responsiveness.
* **Hierarchical Power Management**: The system optimizes power at multiple levels: first at individual CPU cores (via CPU idle states), then at the cluster level (via cluster standby). This multi-level approach allows fine-grained control, reducing power consumption incrementally based on the number of active cores.

*************************
Device Tree Configuration
*************************

Idle states
===========

The AM62L Standby Mode configuration includes the following idle states:

.. list-table:: AM62L Idle States
   :widths: 20 50 30
   :header-rows: 1

   * - Idle State
     - Description
     - Latency

   * - **cpu_sleep_0** (CPU Level)
     - Individual CPU WFI (Wait For Interrupt) state
     - Very Low (microseconds)

   * - **cluster_sleep_0** (Low Latency Cluster standby)
     - Cluster low-latency standby mode when all cores are idle, with reduced clock frequencies and non-critical power domains disabled
     - Low (milliseconds)

The configuration can be loaded from the device tree overlay :file:`k3-am62l3-evm-idle-states.dtso`, which defines
these states and their power management characteristics.

Power Domain Hierarchy
======================

In addition to idle states, the device tree defines the power domain hierarchy that allows CPUIdle to understand
how different power domains relate to each other:

* **CPU_PD** (CPU Power Domain): Per-CPU power domain
* **CLUSTER_PD** (Cluster Power Domain): Cluster-level power domain that groups multiple CPUs

These power domains inform CPUIdle about which non-critical domains can be disabled when all cores within them are idle.

.. note::

   The device tree overlay also includes additional idle states for Suspend-to-Idle (S2Idle) functionality
   that can be referred from :ref:`pm_s2idle_psci`.
   The Standby Mode uses the **cpu_sleep_0** and **cluster_sleep_0** idle states, coordinated through the
   **CPU_PD** and **CLUSTER_PD** power domain hierarchy.

Critical Prerequisites
======================

The AM62L Standby Mode implementation has important prerequisites that must be met for correct operation.

**CPSW (Gigabit Ethernet) Driver Suspension**

The entry into Cluster level standby is conditional on CPSW driver being suspended, since hardware CRC errors
occur when CPSW continues operation during cluster standby. The CPSW is an Always-On IP in the AM62L SoC.

**Display Driver Suspension**

Similarly, the display driver must be in a suspended state for cluster standby due to frame buffer overflow issues.
Ensure display is not actively driving output when testing or relying on Standby Mode for power savings.

.. warning::

   Standby Mode only functions correctly when the DISPLAY and CPSW drivers are suspended. The device tree
   overlay :file:`k3-am62l3-evm-idle-states.dtso` disables the CPSW driver to ensure this
   condition is met. Do not override this configuration without understanding the implications for cluster
   idle transitions and hardware stability.

***********************************************
Power Sequencing and Cluster Standby Entry/Exit
***********************************************

When the all cores in a cluster become idle and AM62L system enters Standby Mode:

1. **Detection Phase**:
      - CPUIdle monitors per-CPU idle state transitions
      - Domain idle state manager tracks core idle status
      - When all cores in a cluster are idle, cluster standby opportunity is identified

2. **Coordination Phase**:
      - Linux CPUIdle framework signals cluster idle state via PSCI ``CPU_SUSPEND`` call
      - PSCI parameter encodes cluster standby request with standby state type (not power-down)
      - TF-A receives request in secure monitor

3. **Validation Phase**:
      - TF-A validates the PSCI request parameter sent for cluster standby
      - Checks all cores in cluster are idle

4. **Standby Entry Phase**:
      - TF-A executes cluster standby entry sequence
      - Reduces PLL clock frequencies for non-critical subsystems
      - Disables non-critical power domains
      - Puts DDR into auto-self-refresh mode
      - System enters low-power standby state with reduced power consumption

5. **Wake-Up Phase**:
      - Incoming interrupt(*any* interrupt can wake the system) triggers wake-up
      - TF-A restores normal PLL frequencies and power domains
      - DDR exits auto-self-refresh mode
      - Cores resume execution with minimal latency
      - System returns to active operation

***************************
Monitoring Standby Activity
***************************

Once Standby Mode is enabled, you can monitor idle state activity through the PM generic power domain (genpd)
sysfs interface. The power domain names are derived from the PSCI power domain hierarchy defined in the device
tree overlay.

.. rubric:: CPU Idle Activity

To monitor per-CPU idle state usage:

.. code-block:: console

   # View CPU idle state statistics
   $ cat /sys/kernel/debug/pm_genpd/power-controller-cpu/idle_states

   State  Time(ms)       Usage      Rejected   Above      Below      S2idle
   S0     1052189         34224       0        0       0          0

.. rubric:: Cluster Standby Activity (Recommended)

To monitor cluster-level standby mode usage, which is the most useful metric for verifying that the system
is successfully entering the low-latency standby mode when all cores are idle:

.. code-block:: console

   # View cluster standby state statistics
   $ cat /sys/kernel/debug/pm_genpd/power-controller-cluster/idle_states

   State  Time(ms)       Usage      Rejected   Above      Below      S2idle
   S0     263595         5415       647        2854       0          0

The ``Usage`` counter shows how many times the cluster entered the standby state, while ``Time(ms)`` shows
the total milliseconds spent in that state. A non-zero Usage count indicates that the cluster standby mode
is being actively used during idle periods.

**********************************
Difference from System Sleep Modes
**********************************

Standby Mode is distinct from deeper system sleep modes like Deep Sleep or RTC-Only+DDR:

.. list-table:: Standby versus Deep Sleep Modes
   :widths: 25 35 40
   :header-rows: 1

   * - Feature
     - Standby Mode
     - Deep Sleep (mem)

   * - **Entry**
     - Automatic, opportunistic
     - Explicit user request

   * - **CPU State**
     - Idle in standby state, context preserved
     - Offline via hotplug

   * - **Wakeup Latency**
     - Microseconds
     - Milliseconds

   * - **PLL/Clock State**
     - Reduced frequencies for non-critical subsystems
     - Full frequency restoration required

   * - **DDR State**
     - Auto-self-refresh during cluster standby
     - Self-refresh

   * - **Wakeup Interrupts**
     - Any SoC interrupt event
     - Only specific wakeup sources - GPIO, RTC, etc.

   * - **Use Case**
     - Normal idle periods with fast wakeup
     - Extended inactivity periods

****************************************
Platform-Specific Implementation Details
****************************************

The AM62L Standby Mode implementation uses platform-specific handlers in TF-A:

* :file:`plat/ti/k3low/common/am62l_psci.c` - AM62L PSCI implementation
* :file:`plat/ti/k3low/board/am62lx/lpm/standby.c` - Cluster standby handler and power sequencing logic

These files implement the ``validate_power_state()`` and ``am62l_entry/exit_standby()`` PSCI platform operations that
coordinate the idle state requests and manage the actual hardware sequencing for cluster standby entry/exit,
including clock frequency adjustments and power domain transitions.

**References**

* :ref:`cpuidle-guide` - General CPUIdle framework documentation
* :ref:`pm_s2idle_psci` - To understand PSCI and OSI mode
* :ref:`lpm_modes` - Low power modes overview
* :ref:`howto_dt_overlays` - Device Tree Overlay Documentation
