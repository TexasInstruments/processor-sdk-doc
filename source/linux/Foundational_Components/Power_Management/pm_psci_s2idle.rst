.. _pm_s2idle_psci:

#############################################
Suspend-to-Idle (S2Idle) and PSCI Integration
#############################################

*********************************
Suspend-to-Idle (S2Idle) Overview
*********************************

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

***********************
OS Initiated (OSI) Mode
***********************

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
==============================

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

Linux provides two distinct system sleep states accessible via :file:`/sys/power/mem_sleep`:
**s2idle (freeze)** and **deep (mem)**. While both can achieve similar power savings by suspending devices
and putting DDR into self-refresh, they differ fundamentally in their implementation approach and
system behavior.

Design Philosophy
=================

**s2idle (Suspend-to-Idle):**

This is a generic, pure software, light-weight variant of system suspend (also referred to as S2I or S2Idle).
It allows more energy to be saved relative to runtime idle by freezing user space, suspending the timekeeping
and putting all I/O devices into low-power states (possibly lower-power than available in the working state),
such that the processors can spend time in their deepest idle states while the system is suspended.

**deep (Suspend-to-RAM):**

A traditional system-wide suspend that coordinates with platform firmware to achieve deep hardware
sleep states. Provides explicit control over system context save/restore through firmware contracts.

Key Differences
===============

.. list-table:: S2Idle vs Deep Sleep Comparison
   :widths: 25 35 40
   :header-rows: 1

   * - Aspect
     - s2idle (freeze)
     - deep (mem)

   * - **CPU Management**
     - All CPUs stay online, enter idle states via cpuidle governor
     - Non-boot CPUs hot-unplugged before suspend

   * - **PSCI Call**
     - ``CPU_SUSPEND`` (per-CPU, coordinated via OSI mode)
     - ``SYSTEM_SUSPEND`` (system-wide firmware call)

   * - **Context Save/Restore**
     - Linux assumes that there's no context loss and skips any core system restore ops
     - Full system context: GIC distributor, ITS tables, timekeeping, generic IRQ chips

   * - **System Hooks**
     - ``syscore_suspend/resume()`` **NOT called**
     - ``syscore_suspend/resume()`` **called** (saves critical platform state)

   * - **Driver Suspend**
     - Same device PM callbacks as deep sleep
     - Same device PM callbacks as s2idle

Context loss considerations
===========================

On TI K3 platforms with OSI mode enabled, s2idle can dynamically enter deep power states
(standby, Deep Sleep, RTC+DDR) that power down the MAIN domain. This creates a hybrid scenario:

- **s2idle behavior**: no CPU hotplug, interrupt-driven wakeup
- **Hardware reality**: GIC and system peripherals lose power and context

This requires firmware (TF-A/TIFS) to handle context save/restore for these states even during
``CPU_SUSPEND`` calls, not just ``SYSTEM_SUSPEND``. The kernel's ``syscore_suspend()`` path
that normally saves GIC ITS tables, timekeeping state, and interrupt controller configuration
is bypassed in s2idle, making firmware-managed context preservation critical.

*********************************************
Low Power Mode Selection in S2Idle (OSI Mode)
*********************************************

S2Idle with OSI mode enables sophisticated low-power mode selection based on system constraints and
power domain hierarchy. The system can automatically select between multiple low-power modes without
user intervention, adapting to the runtime requirements.

Power Domain Hierarchy in Device Tree
=====================================

The power domain hierarchy in the device tree defines how different system components are grouped
and how their power states are coordinated. This hierarchical structure is fundamental in how Linux
sees the system's mapping of low power modes to individual power domains.

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

The domain grouping serves two critical purposes:

1. **Automatic Mode Selection**: The cpuidle framework uses the hierarchy to automatically select
   the deepest possible state. If any device in a power domain is active or has latency constraints,
   shallower states are automatically chosen.

2. **Race Condition Prevention**: The hierarchy ensures that the PSCI firmware can verify all
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
======================

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
      │   ├─> main_sleep_rtcddr (total latency: 300ms entry + 600ms exit = 900ms)
      │   └─> main_sleep_deep (total latency: 250ms entry + 100ms exit = 350ms)
      └─> Select deepest state that meets all constraints

   4. Last CPU issues composite CPU_SUSPEND with selected state
   5. PSCI firmware verifies and executes power-down

Idle State Definitions
======================

The Device Tree defines multiple idle states at each level of the hierarchy, each with different
power/latency trade-offs. The key states are:

**CPU-Level Idle States:**

* **cpu_sleep_1 (PowerDown)**: CPU is powered down with context loss

  * ``arm,psci-suspend-param = <0x012233>``
  * Entry latency: 10ms
  * Exit latency: 10ms
  * Min residency: 1000ms

**Cluster-Level Idle States:**

* **cluster_sleep_0 (Low-Latency Standby)**: Cluster enters low-power standby when all CPUs are idle

  * ``arm,psci-suspend-param = <0x01000021>``
  * Entry latency: 200μs
  * Exit latency: 300μs
  * Min residency: 10ms

**System-Level Idle States (Main Domain):**

* **main_sleep_deep (Deep Sleep)**: DDR in self-refresh, more peripherals remain powered for faster resume

  * ``arm,psci-suspend-param = <0x2012235>``
  * Entry latency: 250ms
  * Exit latency: 100ms
  * Min residency: 500ms
  * Use case: Short to moderate idle periods with faster resume requirements

* **main_sleep_rtcddr (RTC+DDR)**: DDR in self-refresh, minimal peripherals powered (RTC, I/O retention only)

  * ``arm,psci-suspend-param = <0x2012234>``
  * Entry latency: 300ms
  * Exit latency: 600ms
  * Min residency: 1000ms
  * Use case: Long idle periods requiring maximum power savings

  .. note::

     For complete Device Tree definitions including all latency parameters, refer to the platform's
     device tree source files (e.g., ``k3-am62l3-evm-idle-states.dtso``).

Understanding the Suspend Parameters
====================================

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
3. Only idle states with ``exit-latency-us + entry-latency-us`` ≤ constraint are considered
4. The deepest eligible state is selected

**Selecting Specific Low-Power Modes:**

To force selection of a specific mode, set the QoS constraint strategically based on the exit
latencies of the available states. The latency value must be provided as a **hex string**
(e.g., "0x7a120").

* **To force Deep Sleep mode**: Set constraint above Deep Sleep's total latency
  (250ms entry + 100ms exit = **350ms**) but below RTC+DDR's total latency
  (300ms entry + 600ms exit = **900ms**). For example, use **500,000 μs** (500ms):

  .. code-block:: c

     #define LATENCY_VAL "0x7a120"  /* 500,000 μs = 500ms in hex */

  **Calculation:**

  - Target latency: 500,000 μs (above Deep Sleep's total 350,000 μs; below RTC+DDR's total 900,000 μs)
  - Convert to hex: 500,000₁₀ = 0x7A120₁₆
  - Write as hex string: ``"0x7a120"``
  - This allows Deep Sleep (350,000 μs total latency) but blocks RTC+DDR (900,000 μs total latency)

* **To allow RTC+DDR mode**: Set constraint higher than 900ms (900,000 μs = 300ms entry + 600ms exit)
  or don't apply any constraint, allowing the cpuidle governor to select the deepest state (RTC+DDR)
  during long idle periods.


**Example: Deep Sleep Mode Selection:**

Consider a scenario where the QoS constraint is set to 500ms (500,000 μs):

.. code-block:: text

   Available Main Domain States (compared against entry + exit total latency):
   ├─> main_sleep_rtcddr: total = 300ms + 600ms = 900,000 μs → REJECTED (exceeds 500ms constraint)
   └─> main_sleep_deep:   total = 250ms + 100ms = 350,000 μs → SELECTED (meets 500ms constraint)

   Result: System enters Deep Sleep mode instead of RTC+DDR mode

In this example, even though RTC+DDR provides better power savings, the 500ms constraint is below
RTC+DDR's 900ms total latency, so the system uses Deep Sleep instead. The selection is between the
two main domain idle states defined for s2idle suspend.

**Setting CPU wakeup latency constraints from user space:**

Applications can constrain the system's low-power behavior by writing to the CPU wakeup latency entry.
Since this is a device file that needs to be held open for the constraint to be "active", it can
be used in two ways - a C program or a simple bash command.

Below is a C program that demonstrates this:

.. code-block:: c

   /* testqos.c - Set CPU wakeup latency constraint */
   #include <stdio.h>
   #include <fcntl.h>
   #include <unistd.h>
   #include <signal.h>

   #define QOS_DEV "/dev/cpu_wakeup_latency"
   #define LATENCY_VAL "0x7a120"  /* 500,000 μs = 500ms in hex */

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

Alternatively, you can also set it with this command:

.. code-block:: bash

   exec 4<>/dev/cpu_wakeup_latency; echo 0x3e8 >&4

Execute this in a subshell to avoid accidentally keeping it open indefinitely.

**How It Sets QoS Constraints:**

The program opens the special device file ``/dev/cpu_wakeup_latency``. Writing a
latency value (in microseconds) to this file:

1. Registers a global CPU wakeup latency constraint
2. Causes the cpuidle governor to filter out any idle states with exit latency exceeding this value
3. Remains active as long as the file descriptor is open
4. Automatically releases the constraint when the file descriptor is closed (on program exit)

Here's how it would look like:

.. code-block:: console

   root@am62lxx-evm:~# gcc testqos.c -o testqos
   root@am62lxx-evm:~# ./testqos
   QoS set to 0x7a120. Press Ctrl+C to exit.

   # In another terminal, observe the CPU idle state latencies (all in μs):
   root@am62lxx-evm:~# cat /sys/devices/system/cpu/cpu0/cpuidle/state*/latency
   0          # state0: WFI       (0 μs   < 500,000 μs constraint → allowed)
   100        # state1: Standby   (100 μs < 500,000 μs constraint → allowed)
   10000      # state2: PowerDown (10ms   < 500,000 μs constraint → allowed)

   # Press Ctrl+C in the first terminal
   Released.

The value ``0x7a120`` (500,000 μs = 500ms) allows all CPU-level idle states. At the system domain
level, Deep Sleep (350ms total: 250ms entry + 100ms exit) is allowed while RTC+DDR (900ms total:
300ms entry + 600ms exit) is blocked.

