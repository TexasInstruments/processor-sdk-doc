.. _pm_s2idle_psci:

#############################################
Suspend-to-Idle (S2Idle) and PSCI Integration
#############################################

**********************************
Suspend-to-Idle (S2Idle) Overview
**********************************

Suspend-to-Idle (s2idle), also known as "freeze," is a generic, pure software, light-weight variant of system suspend.
In this state, the Linux kernel freezes user space tasks, suspends devices, and then puts all CPUs into their deepest available idle state.

*******************
PSCI as the Enabler
*******************

The Power State Coordination Interface (PSCI) is an ARM-defined standard that acts as the fundamental
enabler for s2idle on all ARM platforms that support it. PSCI defines a standardized firmware interface that allows the
Operating System (OS) to request power states without needing intimate knowledge of the underlying
SoC.

**s2idle Call Flow:**

.. code-block:: text

   Linux Kernel                    PSCI Firmware (TF-A)
   ============                    ====================

   1. Freeze tasks
        |
        v
   2. Suspend devices
        |
        v
   3. cpuidle framework -----------> CPU_SUSPEND
      (per CPU)                          |
        |                                v
        |                         Coordinate power
        |                         state requests
        |                                |
        |                                v
        |                         CPU enters low-power
        |                         hardware state
        |                                |
        |                                V
        |                         Wakeup event (eg. RTC)
        |<--------- Resume ---------
        |
        v
   4. Resume devices
        |
        v
   5. Thaw tasks

The ``cpuidle`` framework calls the PSCI ``CPU_SUSPEND`` API to set each CPU to their corresponding low-power state.
The effectiveness of s2idle depends heavily on the PSCI implementation's ability to coordinate these
requests and enter the deepest possible hardware state.

************************
OS Initiated (OSI) Mode
************************

PSCI 1.0 introduced **OS Initiated (OSI)** mode, which shifts the responsibility of power state coordination from the platform firmware to the Operating System.
In the default **Platform Coordinated (PC)** mode, the OS independently requests a state for each core. The firmware then aggregates these requests (voting) to
determine if a cluster or the system can be powered down.

In **OS Initiated (OSI)** mode, the OS explicitly manages the hierarchy. The OS determines when the last core in a power domain (e.g., a cluster) is going idle
and explicitly requests the power-down of that domain.

Why OSI?
========

OSI mode allows the OS to make better power decisions because it has visibility into:

* **Task Scheduling:** The OS knows when other cores will wake up.
* **Wakeup Latencies:** The OS can respect Quality of Service (QoS) latency constraints more accurately.
* **Usage Patterns:** The OS can predict idle duration better than firmware.

OSI Sequence
============

The coordination in OSI mode follows a specific "Last Man Standing" sequence. The OS tracks the state of all cores in a topology node (e.g., a cluster).

.. code-block:: text

                         OSI "Last Man Standing" Flow

   Cluster with 2 Cores           OS Action                    PSCI Request
   ====================           =========                    =============

   1. Core 0,1: ACTIVE
            |
            | Core 0 becomes idle
            v
   2. Core 0: IDLE           --> OS requests local        --> CPU_SUSPEND
      Core 1: ACTIVE             Core Power Down              (Core PD only)
                                 Cluster stays ON
            |
            | Core 1 (LAST) becomes idle
            v
   3. Core 0,1: IDLE         --> OS recognizes            --> CPU_SUSPEND
                                 "Last Man" scenario          (Composite State)
                                 Requests Composite:
                                 - Core 1: PD                 Core:    PD
                                 - Cluster: PD                Cluster: PD
                                 - System: PD                 System:  PD
            |
            v
   4. Firmware Verification  --> PSCI firmware checks
      & System Power Down        all cores/clusters idle
                                 If verified: Power down
                                 entire system
                                 If not: Deny request
                                 (race condition)

**Detailed Steps:**

1. **First Core Idle:** When the first core in a cluster goes idle, the OS requests a local idle state
   for that core (e.g., Core Power Down) but keeps the cluster running.

2. **Last Core Idle:** When the *last* active core in the cluster is ready to go idle, the OS recognizes
   that the entire cluster, and potentially the system, can now be powered down.

3. **Composite Request:** The last core issues a ``CPU_SUSPEND`` call that requests a **composite state**:

   * **Core State:** Power Down
   * **Cluster State:** Power Down
   * **System State:** Power Down (as demonstrated in the diagram)

4. **Firmware Enforcement:** The PSCI firmware verifies that all other cores and clusters in the requested node are indeed idle.
   If they are not, the request is denied (to prevent race conditions).

***********************************
Understanding the Suspend Parameter
***********************************

The ``power_state`` parameter passed to ``CPU_SUSPEND`` is the key to requesting these states.
In OSI mode, this parameter must encode the intent for the entire hierarchy.

Power State Parameter Encoding
================================

The ``power_state`` is a 32-bit parameter defined by the ARM PSCI specification (ARM DEN0022C).
It has two encoding formats, controlled by the platform's build configuration.

Standard Format
===============

This is the default format used by most platforms:

.. code-block:: text

   31            26 25  24 23            17 16   15                    0
   +---------------+------+----------------+----+----------------------+
   |   Reserved    | Pwr  |   Reserved     | ST |      State ID        |
   |   (must be 0) | Level|   (must be 0)  |    |  (platform-defined)  |
   +---------------+------+----------------+----+----------------------+

.. list-table:: Standard Format Bit Fields
   :widths: 20 80
   :header-rows: 1

   * - Bit Field
     - Description

   * - **[31:26]**
     - **Reserved**: Must be zero.

   * - **[25:24]**
     - **Power Level**: Indicates the deepest power domain level that can be powered down.

       * ``0``: CPU/Core level
       * ``1``: Cluster level
       * ``2``: System level
       * ``3``: Higher levels (platform-specific)

   * - **[23:17]**
     - **Reserved**: Must be zero.

   * - **[16]**
     - **State Type (ST)**: Type of power state.

       * ``0``: Standby or Retention (low latency, context preserved)
       * ``1``: Power Down (higher latency, may lose context)

   * - **[15:0]**
     - **State ID**: Platform-specific identifier for the requested power state. The OS and
       platform firmware must agree on the meaning of these values, typically defined through
       device tree bindings.

**OSI Mode Consideration:**

In OSI mode, the OS is responsible for tracking which cores are idle. When the last core
in a cluster issues the `CPU_SUSPEND` call with Power Level = 1, the PSCI firmware:

1. Verifies that all other cores in the cluster are already in a low-power state
2. If verified, powers down the entire cluster
3. If not verified (race condition), denies the request with an error code

The State ID field is platform-defined and typically documented in the device tree
``idle-state`` nodes using the ``arm,psci-suspend-param`` property. This mechanism,
leveraging ``cpuidle`` and ``s2idle``, allows the kernel to abstract complex platform-specific
low-power modes into a generic framework. The ``idle-state`` nodes in the Device Tree define these power states,
including their entry/exit latencies and target power consumption, enabling the ``cpuidle`` governor to make informed
decisions about which idle state to enter based on system load and predicted idle duration.
The ``arm,psci-suspend-param`` property then directly maps these idle states to the corresponding PSCI ``power_state``
parameter values that the firmware understands.

It's worth noting that in the `s2idle` path (ie. when the user initiates the suspend to idle),
the kernel is designed to always pick the deepest possible idle state.

Example: System Suspend (Standard Format)
=========================================

When the OS targets a system-wide suspend state (e.g., Suspend-to-RAM), the `power_state` parameter is constructed to target the highest power level.
Consider the example value **0x02012234**:

.. list-table:: Power State Parameter Breakdown (0x02012234)
   :widths: 20 20 20 40
   :header-rows: 1

   * - Field
     - Bits
     - Value
     - Meaning

   * - Reserved
     - [31:26]
     - 0
     - Must be zero

   * - Power Level
     - [25:24]
     - 2
     - System level

   * - Reserved
     - [23:17]
     - 0
     - Must be zero

   * - State Type
     - [16]
     - 1
     - Power Down

   * - State ID
     - [15:0]
     - 0x2234
     - Platform-specific (e.g., "S2RAM")

**Interpretation:**

* **Power Level = 2** tells the firmware that a system-level transition is requested.
* **State Type = 1** indicates a power-down state.
* **State ID = 0x2234** is the platform-specific identifier for this system state.

In the context of **s2idle**, if the OS determines that all constraints are met for system suspension,
the last active CPU (Last Man) will invoke `CPU_SUSPEND` with this parameter. The PSCI firmware then
coordinates the final steps to suspend the system (e.g., placing DDR in self-refresh and powering down the SoC).

**************************
S2Idle vs Deep Sleep (mem)
**************************

The Linux kernel has sleep states that are global low-power states of the entire system in which user space
code cannot be executed and the overall system activity is significantly reduced.
There's different types of sleep states as mentioned in it's
`documentation <https://docs.kernel.org/admin-guide/pm/sleep-states.html>`__.
System sleep states can be selected using the sysfs entry :file:`/sys/kernel/mem_sleep`

On TI K3 AM62L platform, we currently support the ``s2idle`` and ``deep`` states.
Both of them can achieve similar power savings (e.g., by suspending to RAM / putting DDR into Self-Refresh).
The primary differences lie in the software execution flow, specifically how CPUs are managed and which
PSCI APIs are invoked.

.. list-table:: S2Idle vs Deep Sleep
   :widths: 20 40 40
   :header-rows: 1

   * - Feature
     - s2idle (Suspend-to-Idle)
     - deep (Suspend-to-RAM)

   * - **Kernel String**
     - ``s2idle`` or ``freeze``
     - ``deep`` or ``mem``

   * - **Non-boot CPUs**
     - **Online**: Non-boot CPUs are put into a deep idle state but remain logically online.
     - **Offline**: Non-boot CPUs are hot-unplugged (removed) from the system via ``CPU_OFF``.

   * - **Entry Path**
     - **cpuidle**: Uses the standard CPUidle framework. Additionally, each driver is made idle by calling respective runtime suspend hooks.
     - **suspend_ops**: Uses driver specific suspend operations before ``PSCI_SYSTEM_SUSPEND`` is called.
       No governors exist to make any decisions.

   * - **PSCI Call**
     - ``CPU_SUSPEND``: Invoked for every core (Last Man Standing logic coordinates the cluster/system depth).
     - ``SYSTEM_SUSPEND``: Typically invoked by the last active CPU after others are offlined.

   * - **Resume Flow**
     - **Fast**: CPUs exit the idle loop immediately upon interrupt. Context is preserved.
     - **Slow**: Kernel must serially bring secondary CPUs back online (Hotplug). Kernel must recreate
       threads, re-enable interrupts, resume each driver and restore per-CPU state for every non-boot core.

   * - **Latency**
     - Lower
     - High, primarily due to the overhead of **CPU Hotplug** for non-boot CPUs

