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

   * - **cpu_sleep_stby** (CPU Level)
     - Individual CPU WFI (Wait For Interrupt) state
     - Very Low (microseconds)

   * - **cluster_sleep_stby** (Cluster standby)
     - The default cluster standby mode when all cores are idle, with reduced clock frequencies and non-critical power domains disabled
     - Low (milliseconds)

   * - **cluster_sleep_deep_stby*** (Cluster Deep Standby)
     - Additional deep standby mode similar to cluster standby, with additional clock gating and power domain shutdown for more aggressive power savings.
     - Low (milliseconds)

.. note::

   The ``cluster_sleep_deep_stby`` state is an optional configuration. Enable it using the device tree overlay
   :file:`k3-am62l3-evm-idle-states.dtso`.

   **Only enable deep standby when CPSW and Display drivers are not needed.**
   See :ref:`deep-standby-mode` for more details.

Power Domain Hierarchy
======================

In addition to idle states, the device tree defines the power domain hierarchy that allows CPUIdle to understand
how different power domains relate to each other:

* **CPU_PD** (CPU Power Domain): Per-CPU power domain
* **CLUSTER_PD** (Cluster Power Domain): Cluster-level power domain that groups multiple CPUs

These power domains tell CPUIdle what non-critical domains to disable when all cores within them are idle.

.. _deep-standby-mode:

Deep Standby Mode
=================

Critical Prerequisites
----------------------

The following prerequisites must be met before using AM62L deep standby mode.

**CPSW (Gigabit Ethernet) Driver Suspension**

Deep standby entry requires suspending the CPSW driver. Deep standby reduces the CBASS clock
frequency for power savings, which can cause the CPSW driver to malfunction with hardware CRC errors if it is actively driving traffic.

**Display Driver Suspension**

Similarly, the display driver must not drive output during deep standby. The DDR enters auto self-refresh
mode during this state, which causes frame buffer overflow errors.

How to Enable Deep Standby Mode
-------------------------------

To enable deep standby mode, apply the device tree overlay :file:`k3-am62l3-evm-idle-states.dtso` to your system.
See :ref:`howto_dt_overlays` for the steps to enable the overlay.

This overlay adds the ``cluster_sleep_deep_stby`` idle state to the device tree configuration.
The overlay also disables the CPSW and Display drivers to ensure that the system can safely enter deep standby.

***********************************************
Power Sequencing and Cluster Standby Entry/Exit
***********************************************

When the all cores in a cluster become idle and AM62L system enters Standby Mode:

1. **Detection Phase**:
      - CPUIdle monitors per-CPU idle state transitions
      - Domain idle state manager tracks core idle status
      - When all cores in a cluster are idle, the system identifies a cluster standby opportunity

2. **Coordination Phase**:
      - Linux CPUIdle framework signals cluster idle state via PSCI ``CPU_SUSPEND`` call
      - PSCI parameter encodes cluster standby request with standby state type (not power-down)
      - TF-A receives request in secure monitor

3. **Validation Phase**:
      - TF-A validates the PSCI request parameter sent for cluster standby
      - Checks all cores in cluster are idle

4. **Standby Entry Phase**:
      - TF-A executes cluster standby entry sequence
      - Performs the hardware sequence as mentioned in :ref:`hardware-sequence-details`
      - System enters low-power standby state with reduced power consumption

5. **Wake-Up Phase**:
      - Incoming interrupt(*any* interrupt can wake the system) triggers wake-up
      - TF-A restores original PLL frequencies and power domains
      - Cores resume execution with minimal latency
      - System returns to active operation

.. _hardware-sequence-details:

*************************
Hardware Sequence Details
*************************

The following table outlines the specific hardware sequences executed during standby and deep standby modes:

.. list-table:: Hardware Sequences for Standby Modes
   :widths: 30 70
   :header-rows: 1

   * - Mode
     - Hardware Sequence Steps
   * - **Shallow Standby Mode**
     - * Disable GP Test, PBIST, and DEBUGSS LPSCs
       * Disable DEBUGSS PLL HSDIV
       * Enable auto-clock-gating for CBASS
       * Put PLL8(A53 clock) in bypass
   * - **Deep Standby Mode**
     - * All default standby mode steps
       * Reduce CBASS frequency to lowest functional value (125Mhz)
       * Put DDR in auto self-refresh

The 2 additional changes in deep standby mode (CBASS frequency reduction and DDR auto-self-refresh) result in significantly higher power savings compared to default standby mode.

***************************
Monitoring Standby Activity
***************************

After enabling standby modes, the PM generic power domain (genpd) sysfs interface displays the idle state activity.
The power domain names come from the PSCI power domain hierarchy in the device tree overlay.

.. rubric:: CPU Idle Activity

To monitor per-CPU idle state usage:

.. code-block:: console

   # View CPU idle state statistics
   $ cat /sys/kernel/debug/pm_genpd/power-controller-cpu/idle_states

   State  Time(ms)       Usage      Rejected   Above      Below      S2idle
   S0     1052189         34224       0        0       0          0

.. rubric:: Cluster Standby Activity (Recommended)

The cluster-level standby mode usage metric is useful for verifying that the system
is successfully entering standby mode. To check this value, issue the following:

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
