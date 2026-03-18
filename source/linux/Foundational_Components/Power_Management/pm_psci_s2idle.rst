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

**********************************************
Low Power Mode Selection in S2Idle (OSI Mode)
**********************************************

S2Idle with OSI mode enables sophisticated low-power mode selection based on system constraints,
power domain hierarchy, and predicted idle duration. The system can automatically select between
multiple low-power modes without user intervention, adapting to the runtime requirements.

Power Domain Hierarchy in Device Tree
======================================

The power domain hierarchy in the Device Tree defines how different system components are grouped
and how their power states are coordinated. This hierarchical structure is fundamental to OSI mode's
"Last Man Standing" logic.

**Hierarchical Structure:**

.. code-block:: text

   MAIN_PD (System Level)
       │
       ├──> CLUSTER_PD (Cluster Level)
       │        │
       │        ├──> CPU_PD (CPU Level)
       │        │       ├──> CPU0
       │        │       └──> CPU1
       │        │
       │        └──> Cluster-sensitive peripherals
       │             ├──> CPSW3G (Ethernet)
       │             └──> DSS0 (Display)
       │
       └──> Main domain peripherals
            ├──> UART, I2C, SPI controllers
            ├──> Timers
            ├──> SDHCI controllers
            └──> USB controllers

**Device Tree Implementation:**

In the Device Tree, this hierarchy is established through power domain mappings:

.. code-block:: dts

   &psci {
       CPU_PD: power-controller-cpu {
           #power-domain-cells = <0>;
           power-domains = <&CLUSTER_PD>;
           domain-idle-states = <&cpu_sleep_0>, <&cpu_sleep_1>;
       };

       CLUSTER_PD: power-controller-cluster {
           #power-domain-cells = <0>;
           domain-idle-states = <&cluster_sleep_0>;
           power-domains = <&MAIN_PD>;
       };

       MAIN_PD: power-controller-main {
           #power-domain-cells = <0>;
           domain-idle-states = <&main_sleep_deep>, <&main_sleep_rtcddr>;
       };
   };

**Why Domain Grouping is Needed:**

The domain grouping serves several critical purposes:

1. **Hardware Dependency Management**: Certain peripherals must remain active for specific low-power
   states. For example, DDR controllers must remain operational in RTC+DDR mode, but can be powered
   down in Deep Sleep mode.

2. **Constraint Propagation**: When a device in the CLUSTER_PD is active (e.g., Display Subsystem),
   the cluster cannot enter its deepest idle state. The constraint propagates up the hierarchy,
   preventing both CLUSTER_PD and MAIN_PD from entering deeper states.

3. **Automatic Mode Selection**: The cpuidle framework uses the hierarchy to automatically select
   the deepest possible state. If any device in a power domain is active or has latency constraints,
   shallower states are automatically chosen.

4. **Race Condition Prevention**: The hierarchy ensures that the PSCI firmware can verify all
   components in a domain are truly idle before powering down that domain.

**Peripheral Power Domain Mapping:**

The ``power-domain-map`` property explicitly assigns peripherals to power domains:

.. code-block:: dts

   &scmi_pds {
       power-domain-map = <3 &CLUSTER_PD>,  /* CPSW3G Ethernet */
                          <39 &CLUSTER_PD>, /* DSS0 Display */
                          <38 &CLUSTER_PD>, /* DSS_DSI0 */
                          <15 &MAIN_PD>,    /* TIMER0 */
                          <26 &MAIN_PD>,    /* SDHCI1 */
                          <89 &MAIN_PD>,    /* UART0 */
                          <95 &MAIN_PD>;    /* USBSS0 */
   };

This mapping ensures that when the Display (DSS0) is active, the system won't enter states that
would cause DDR Auto Self-Refresh issues. Similarly, active UART or USB connections prevent
deeper system states that would disconnect those interfaces.

Role in Mode Selection
=======================

During s2idle entry, the cpuidle framework traverses the power domain hierarchy from bottom to top:

.. code-block:: text

   Mode Selection Flow during S2Idle Entry
   ========================================

   1. Freeze user space tasks
   2. Suspend all devices (call runtime_suspend hooks)
   3. For each CPU (in cpuidle framework):

      CPU Level (CPU_PD):
      ├─> Check QoS latency constraints
      ├─> Check device activity in CPU_PD
      └─> Select CPU idle state: cpu_sleep_0 (Standby) or cpu_sleep_1 (PowerDown)

      Cluster Level (CLUSTER_PD):
      ├─> Check if this is the last CPU in cluster
      ├─> Check device activity in CLUSTER_PD (e.g., Display, Ethernet)
      ├─> If last CPU and no constraints:
      │   └─> Select cluster idle state: cluster_sleep_0
      └─> Else: Skip cluster power-down

      System Level (MAIN_PD):
      ├─> Check if last CPU in system
      ├─> Check device activity in MAIN_PD (e.g., UART, USB, Timers)
      ├─> Check QoS constraints for entire system
      ├─> Compare latency requirements to available states:
      │   ├─> main_sleep_rtcddr (exit latency: 600ms)
      │   └─> main_sleep_deep (exit latency: 10ms)
      └─> Select deepest state that meets all constraints

   4. Last CPU issues composite CPU_SUSPEND with selected state
   5. PSCI firmware verifies and executes power-down

Idle State Definitions
=======================

The Device Tree defines multiple idle states at each level of the hierarchy, each with different
power/latency trade-offs:

**CPU-Level Idle States:**

.. code-block:: dts

   idle-states {
       cpu_sleep_0: stby {
           compatible = "arm,idle-state";
           idle-state-name = "Standby";
           arm,psci-suspend-param = <0x00000001>;
           entry-latency-us = <25>;
           exit-latency-us = <100>;
           min-residency-us = <1000>;
       };

       cpu_sleep_1: powerdown {
           compatible = "arm,idle-state";
           idle-state-name = "PowerDown";
           arm,psci-suspend-param = <0x012233>;
           entry-latency-us = <250000>;
           exit-latency-us = <100000>;
           min-residency-us = <1000000>;
           local-timer-stop;
       };
   };

**Domain-Level Idle States:**

.. code-block:: dts

   domain-idle-states {
       cluster_sleep_0: low-latency-stby {
           compatible = "domain-idle-state";
           arm,psci-suspend-param = <0x01000021>;
           entry-latency-us = <200>;
           exit-latency-us = <300>;
           min-residency-us = <10000>;
       };

       main_sleep_deep: main-sleep-deep {
           compatible = "domain-idle-state";
           arm,psci-suspend-param = <0x2012235>;
           entry-latency-us = <10000>;
           exit-latency-us = <10000>;
           min-residency-us = <500000>;
           local-timer-stop;
       };

       main_sleep_rtcddr: main-sleep-rtcddr {
           compatible = "domain-idle-state";
           arm,psci-suspend-param = <0x2012234>;
           local-timer-stop;
           entry-latency-us = <300000>;
           exit-latency-us = <600000>;
           min-residency-us = <1000000>;
       };
   };

Understanding the Suspend Parameters
=====================================

The ``arm,psci-suspend-param`` values encode the target power state using the PSCI standard format
described earlier. Let's decode the key parameters for the main domain states:

**Deep Sleep Mode (main_sleep_deep):**

Parameter: ``0x2012235``

.. code-block:: text

   Binary:     0000 0010 0000 0001 0010 0010 0011 0101
   Hex:        0x02012235

   [31:26] = 0  → Reserved
   [25:24] = 2  → Power Level = System (0x2)
   [23:17] = 0  → Reserved
   [16]    = 1  → State Type = Power Down
   [15:0]  = 0x2235 → State ID (platform-specific)

**Interpretation:**

- **Power Level = 2 (System)**: The entire system, including the SoC, enters a low-power state
- **State Type = 1 (Power Down)**: Context is lost; firmware must restore state on resume
- **State ID = 0x2235**: Platform-specific identifier that the PSCI firmware (TF-A) recognizes
  as "Deep Sleep" mode where DDR is in Self-Refresh and more peripherals in the Main domain
  remain powered compared to RTC+DDR mode, providing faster resume at the cost of higher power

**RTC+DDR Mode (main_sleep_rtcddr):**

Parameter: ``0x2012234``

.. code-block:: text

   Binary:     0000 0010 0000 0001 0010 0010 0011 0100
   Hex:        0x02012234

   [31:26] = 0  → Reserved
   [25:24] = 2  → Power Level = System (0x2)
   [23:17] = 0  → Reserved
   [16]    = 1  → State Type = Power Down
   [15:0]  = 0x2234 → State ID (platform-specific)

**Interpretation:**

- **Power Level = 2 (System)**: System-level power state
- **State Type = 1 (Power Down)**: Power-down with context loss
- **State ID = 0x2234**: Platform-specific identifier for "RTC+DDR" mode where DDR is in
  Self-Refresh and only minimal peripherals (RTC, I/O retention) remain powered in the Main
  domain, providing maximum power savings at the cost of longer resume latency

**Key Differences:**

.. list-table:: Deep Sleep vs RTC+DDR Mode Comparison
   :widths: 30 35 35
   :header-rows: 1

   * - Property
     - Deep Sleep (0x2012235)
     - RTC+DDR (0x2012234)

   * - **State ID**
     - 0x2235
     - 0x2234

   * - **DDR State**
     - Self-Refresh
     - Self-Refresh

   * - **Main Domain State**
     - Partially powered (more peripherals ON)
     - Minimal power (only RTC, I/O retention)

   * - **Exit Latency**
     - 10ms (10,000 μs) - Shallower state
     - 600ms (600,000 μs) - Deeper state

   * - **Entry Latency**
     - 10ms (10,000 μs)
     - 300ms (300,000 μs)

   * - **Min Residency**
     - 500ms (500,000 μs)
     - 1000ms (1,000,000 μs)

   * - **Power Consumption**
     - Higher (more peripherals active)
     - Lower (minimal peripherals active)

   * - **Use Case**
     - Short to moderate idle periods where faster resume is needed
     - Long idle periods where maximum power savings needed

The cpuidle governor uses these latency and residency values to automatically select the appropriate
mode. If predicted idle time is short and latency constraints are tight, Deep Sleep mode (the
shallower state) is chosen for faster resume. For longer predicted idle periods with relaxed
latency requirements, RTC+DDR mode (the deeper state) is preferred for maximum power savings.

QoS Latency Constraints and Mode Selection
===========================================

The Linux kernel's PM QoS (Quality of Service) framework allows drivers and applications to
specify maximum acceptable wakeup latency. These constraints directly influence which idle
state can be entered during s2idle.

**How QoS Constraints Work:**

1. Each device or CPU can register a latency constraint (in nanoseconds)
2. The cpuidle governor queries these constraints before selecting an idle state
3. Only idle states with ``exit-latency-us`` ≤ constraint are considered
4. The deepest eligible state is selected

**Example: Deep Sleep Mode Selection:**

Consider a scenario where the system has active I2C or SPI communication requiring responses
within 20ms. A QoS constraint of 20,000 μs (20ms) would be applied:

.. code-block:: text

   Available Main Domain States:
   ├─> main_sleep_rtcddr: exit-latency = 600,000 μs (600ms) → REJECTED (exceeds constraint)
   └─> main_sleep_deep:   exit-latency = 10,000 μs (10ms)   → SELECTED (meets constraint)

   Result: System enters Deep Sleep mode instead of RTC+DDR mode

In this example, even though RTC+DDR provides better power savings, the 20ms latency constraint
forces the system to use the shallower Deep Sleep mode. The selection is between the two main
domain idle states defined for s2idle suspend.

**Setting QoS Constraints from User Space:**

Applications can constrain the system's low-power behavior by writing to the PM QoS device file.
Below is a C program that demonstrates this:

.. code-block:: c

   /* testqos.c - Set CPU wakeup latency constraint */
   #include <stdio.h>
   #include <fcntl.h>
   #include <unistd.h>
   #include <signal.h>

   #define QOS_DEV "/dev/cpu_wakeup_latency"
   #define LATENCY_VAL "0x1000"  /* 4096 ns (4 μs) in hex */

   static volatile int keep_running = 1;

   void sig_handler(int sig) {
       keep_running = 0;
   }

   int main(void) {
       int fd;

       signal(SIGINT, sig_handler);
       signal(SIGTERM, sig_handler);

       fd = open(QOS_DEV, O_RDWR);
       if (fd < 0) {
           perror("open");
           return 1;
       }

       if (write(fd, LATENCY_VAL, sizeof(LATENCY_VAL) - 1) < 0) {
           perror("write");
           close(fd);
           return 1;
       }

       printf("QoS set to %s. Press Ctrl+C to exit.\n", LATENCY_VAL);

       while (keep_running)
           sleep(1);

       close(fd);
       printf("Released.\n");
       return 0;
   }

**Why This Program is Needed:**

This program demonstrates how to control low-power mode selection by setting QoS latency constraints.
By applying a tight latency constraint (4 μs in the example), you can force the system to stay in
shallow idle states, preventing entry into Deep Sleep or RTC+DDR modes. This is useful for testing
that the cpuidle governor correctly respects QoS constraints and selects the appropriate idle state
based on latency requirements.

**Selecting Specific Low-Power Modes:**

To force selection of a specific mode, set the QoS constraint strategically based on the exit
latencies of the available states. The latency value must be provided as a **hex string**
(e.g., "0x7ef41").

* **To force Deep Sleep mode**: Set constraint above Deep Sleep's exit latency (10ms = 10,000 μs)
  but below RTC+DDR's exit latency (600ms = 600,000 μs). For example, use **520 μs (520,001 ns)**:

  .. code-block:: c

     #define LATENCY_VAL "0x7ef41"  /* 520,001 ns = 520 μs in hex */

  **Calculation:**

  - Target latency: 520 μs = 520,000 ns (round to 520,001 for convenience)
  - Convert to hex: 520,001₁₀ = 0x7EF41₁₆
  - Write as hex string: ``"0x7ef41"``
  - This allows Deep Sleep (10,000 μs exit latency) but blocks RTC+DDR (600,000 μs exit latency)

* **To allow RTC+DDR mode**: Set constraint higher than 600ms (600,000 μs) or don't apply any
  constraint, allowing the cpuidle governor to select the deepest state (RTC+DDR) during long
  idle periods.

**How It Sets QoS Constraints:**

The program opens the special device file ``/dev/cpu_wakeup_latency``, which is part of the
kernel's PM QoS framework. Writing a latency value (in nanoseconds) to this file:

1. Registers a global CPU wakeup latency constraint
2. Causes the cpuidle governor to filter out any idle states with exit latency exceeding this value
3. Remains active as long as the file descriptor is open
4. Automatically releases the constraint when the file descriptor is closed (on program exit)

**Usage Example:**

.. code-block:: console

   root@am62lxx-evm:~# gcc testqos.c -o testqos
   root@am62lxx-evm:~# ./testqos
   QoS set to 0x1000. Press Ctrl+C to exit.

   # In another terminal, observe the constrained behavior:
   root@am62lxx-evm:~# cat /sys/devices/system/cpu/cpu0/cpuidle/state*/latency
   0          # state0: WFI
   125        # state1: Standby
   350125     # state2: PowerDown (disabled by QoS)

   # Press Ctrl+C in the first terminal
   Released.

   # Now the deeper states are available again:
   root@am62lxx-evm:~# cat /sys/devices/system/cpu/cpu0/cpuidle/state*/latency
   0
   125
   350125     # state2: PowerDown (now enabled)

The value ``0x1000`` (4096 ns = ~4 μs) prevents any idle state with exit latency greater than
4 μs from being entered. In the example above, the PowerDown state with 350ms exit latency
is effectively disabled while the constraint is active.

