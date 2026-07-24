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
the last active CPU (Last Man) will call `CPU_SUSPEND` with this parameter. The PSCI firmware then
coordinates the final steps to suspend the system (e.g., placing DDR in self-refresh and powering down the SoC).

******************************
S2Idle versus DeepSleep (mem)
******************************

Linux provides two distinct system sleep states accessible via :file:`/sys/power/mem_sleep`:
**s2idle (freeze)** and **deep (mem)**. While both can achieve similar power savings by suspending devices
and putting DDR into self-refresh, they differ fundamentally in their implementation approach and
system behavior.

Design Philosophy
=================

**s2idle (Suspend-to-Idle):**

The kernel's ``cpuidle`` framework retains full ownership of power state selection. After freezing
user space and suspending devices, the cpuidle governor walks the power domain hierarchy, evaluates
QoS latency constraints at each level, and selects the deepest eligible idle state - then encodes
that choice into a ``CPU_SUSPEND`` call. The OS decides; firmware executes.

**deep (Suspend-to-RAM):**

The OS hands off power state selection entirely to the platform firmware. After suspending devices
and hot-unplugging non-boot CPUs, the kernel issues a single ``SYSTEM_SUSPEND`` call and yields
control. The firmware then determines which Low Power Mode (LPM) to enter based on its own
evaluation of system constraints and QoS requirements.

Key Differences
===============

.. list-table:: S2Idle versus Deep [mem] Comparison
   :widths: 25 35 40
   :header-rows: 1

   * - Aspect
     - s2idle (freeze)
     - deep (mem)

   * - **CPU Management**
     - All CPUs stay online, enter idle states via cpuidle governor
     - Non-boot CPUs hot-unplugged before suspend

   * - **Entry mechanism**
     - Select ``[s2idle]`` in ``/sys/power/mem_sleep``
     - Select ``[deep]`` in ``/sys/power/mem_sleep``

   * - **PSCI Call**
     - ``CPU_SUSPEND`` (per-CPU, coordinated via OSI mode)
     - ``SYSTEM_SUSPEND`` (system-wide firmware call)

   * - **Context Save/Restore**
     - Linux assumes that there's no context loss and skips any core system restore operations
     - Full system context: GIC distributor, ITS tables, timekeeping, generic IRQ chips

   * - **System Hooks**
     - ``syscore_suspend/resume()`` **NOT called**
     - ``syscore_suspend/resume()`` **called** (saves critical platform state)

Context loss considerations
===========================

On TI K3 platforms with OSI mode enabled, s2idle can dynamically enter deep power states
(standby, DeepSleep, RTC + I/O + DDR) that power down the MAIN domain. This creates a hybrid scenario:

- **s2idle behavior**: no CPU hot plug, interrupt-driven wakeup
- **Hardware reality**: GIC and system peripherals lose power and context

This requires firmware (TF-A/TIFS) to handle context save/restore for these states even during
``CPU_SUSPEND`` calls, not just ``SYSTEM_SUSPEND``. The kernel's ``syscore_suspend()`` path
that normally saves GIC ITS tables, timekeeping state, and interrupt controller configuration
is bypassed in s2idle, making firmware-managed context preservation critical.

**********************************************************
Components Involved in Mode Selection in S2Idle (OSI Mode)
**********************************************************

S2Idle with OSI mode enables sophisticated low-power mode selection based on system constraints and
power domain hierarchy. The system can automatically select between multiple low-power modes without
user intervention, adapting to the runtime requirements.

The following describes the components involved in this selection process:

Power Domain Hierarchy in Device Tree
=====================================

The power domain hierarchy in the device tree defines the grouping of different system components
and their power states. This hierarchical structure is fundamental in how Linux sees the system's
mapping of low power modes to individual power domains.

**Hierarchical Structure:**

.. code-block:: text

   SOC_PD  [idle: RTC + I/O + DDR]
   |- MAIN_PD  [idle: DeepSleep]
   |   |- SYSTEM_PD  [idle: DSS DeepSleep]
   |   |   |-> CLUSTER_PD  [idle: Cluster Standby]
   |   |       |-> CPU_PD  [idle: CPU Standby, CPU PowerDown]
   |   |           |-> CPU0
   |   |           |-> CPU1
   |   |-> DISPLAY_PD
   |       |-> DSS0, DSS_DSI0, DPHY_TX0
   |-> WKUP_PD
       |-> USB0, USB1
       |-> WKUP Timers, GPIO, UART, I2C


The idle state associated with each domain is the state that domain enters when all
of its sub-nodes are off. This determines the deepest low power mode the
system can reach depending on which devices remain active.

**Device Tree Implementation:**

In the Device Tree, the psci node defines the power domain hierarchy and the idle states:

.. code-block:: dts

   &psci {
       CPU_PD: power-controller-cpu {
           #power-domain-cells = <0>;
           power-domains = <&CLUSTER_PD>;
           domain-idle-states = <&cpu_sleep_stby>, <&cpu_sleep_pwrdwn>;
       };

       CLUSTER_PD: power-controller-cluster {
           #power-domain-cells = <0>;
           power-domains = <&SYSTEM_PD>;
           domain-idle-states = <&cluster_sleep_stby>;
       };

       SYSTEM_PD: power-controller-system {
           #power-domain-cells = <0>;
           power-domains = <&MAIN_PD>;
           domain-idle-states = <&main_sleep_dss>;
       };
      /* Intermediate power domains */
       SOC_PD: power-controller-soc {
           #power-domain-cells = <0>;
           domain-idle-states = <&main_sleep_rtcddr>;
       };
   };

The ``power-domain-map`` property then assigns each peripheral to its domain:

.. code-block:: dts

   &scmi_pds {
       power-domain-map =
           <38 &DISPLAY_PD>,  /* DSS_DSI0  */
           <39 &DISPLAY_PD>,  /* DSS0      */
           <86 &DISPLAY_PD>,  /* DPHY_TX0  */
           <15 &SYSTEM_PD>,   /* TIMER0    */
           <16 &SYSTEM_PD>,   /* TIMER1    */
           /* ... UART, I2C, SPI, SDHCI, GPIO -> SYSTEM_PD ... */
           <57 &WKUP_PD>,     /* WKUP_I2C0 */
           <83 &WKUP_PD>,     /* WKUP_UART */
           <95 &WKUP_PD>,     /* USBSS0    */
           <96 &WKUP_PD>;     /* USBSS1    */
   };

This mapping lets the kernel decide at runtime when to turn off a power domain.
If any device assigned to a domain is still active, that domain stays on, which
blocks all of its parent domains from powering off too.

QoS Latency Constraints
=======================

The Linux kernel's PM QoS (Quality of Service) framework allows drivers and applications to
specify maximum acceptable wakeup latency. These constraints directly influence what idle
state are eligible for entry during s2idle.

**How QoS Constraints Work:**

#. Each device or CPU can register a latency constraint (in nanoseconds)
#. The cpuidle governor queries these constraints before selecting an idle state
#. Only idle states with ``exit-latency-us + entry-latency-us <= constraint`` are considered
#. The cpuidle governor selects the deepest eligible mode.

**How to set QoS Constraints**

- To create a global CPU wakeup latency constraint, write the latency value (in microseconds) to the device file ``/dev/cpu_wakeup_latency``.
- The constraint is "active" provided that the file descriptor is open. Closing the file descriptor releases the constraint.
- Refer :ref:`setting-cpu-wakeup-latency` to see how to set a QoS constraint from userspace.

Here's how it would look like: (The set_qos.c program in :ref:`setting-cpu-wakeup-latency` helps set the
``/dev/cpu_wakeup_latency`` QoS constraint.)

.. code-block:: console

   root@am62lxx-evm:~# gcc set_qos.c -o set_qos
   root@am62lxx-evm:~# ./set_qos
   QoS set to 0x7a120. Press Ctrl+C to exit.

   # In another terminal, observe the CPU idle state latencies (all in us):
   root@am62lxx-evm:~# cat /sys/devices/system/cpu/cpu0/cpuidle/state*/latency
   0          # state0: WFI       (0 us   < 500,000 us constraint -> allowed)
   100        # state1: Standby   (100 us < 500,000 us constraint -> allowed)
   10000      # state2: PowerDown (10ms   < 500,000 us constraint -> allowed)

   # Press Ctrl+C in the first terminal
   Released.

The value ``0x7a120`` (500,000 us = 500ms) allows all CPU-level idle states. At the system domain
level, the cpuidle governor allows DeepSleep (350ms total: 250ms entry + 100ms exit) and blocks RTC + I/O + DDR (900ms total:
300ms entry + 600ms exit).

Idle State Definitions
======================

The device tree defines multiple idle states at each level of the hierarchy, each with different
power/latency trade-offs. The key states are:

.. list-table:: Idle States by Power Domain Level
   :widths: 18 20 15 15 15 17
   :header-rows: 1

   * - Idle State
     - Domain
     - Entry latency
     - Exit latency
     - Min residency
     - Low Power Mode
   * - ``cpu_sleep_stby``
     - CPU_PD
     - 25 us
     - 100 us
     - 1 ms
     - CPU Standby
   * - ``cpu_sleep_pwrdwn``
     - CPU_PD
     - 150 ms
     - 100 ms
     - 1000 ms
     - CPU PowerDown
   * - ``cluster_sleep_stby``
     - CLUSTER_PD
     - 200 us
     - 300 us
     - 10 ms
     - Cluster Standby
   * - ``main_sleep_dss``
     - SYSTEM_PD
     - 150 ms
     - 100 ms
     - 250 ms
     - DSS DeepSleep
   * - ``main_sleep_deep``
     - MAIN_PD
     - 250 ms
     - 100 ms
     - 500 ms
     - DeepSleep
   * - ``main_sleep_rtcddr``
     - SOC_PD
     - 300 ms
     - 600 ms
     - 1000 ms
     - RTC + I/0 + DDR

The entry and exit latencies are what the cpuidle governor compares against the
active QoS constraint. The min residency is the minimum time the system must
expect to remain idle before it is worth entering that state.

Understanding the Suspend Parameters
====================================

The ``arm,psci-suspend-param`` values encode the target power state using the PSCI standard format
described earlier. Let's decode the key parameters for the main domain states:

Parameter: ``0x2012235`` and ``0x2012234``

.. code-block:: text

   Binary:     0000 0010 0000 0001 0010 0010 0011 0101
   Hex:        0x02012235

   [31:26] = 0  -> Reserved
   [25:24] = 2  -> Power Level = System (0x2)
   [23:17] = 0  -> Reserved
   [16]    = 1  -> State Type = Power Down
   [15:0]  = 0x2235 / 0x2234 -> State ID (platform-specific)

**Interpretation:**

- **Power Level = 2 (System)**: The entire system, including the SoC, enters a low-power state
- **State Type = 1 (Power Down)**: System loses context; firmware must restore state on resume
- **State ID = 0x2235**: Platform-specific identifier that the PSCI firmware (TF-A) recognizes
  as "DeepSleep" mode where DDR is in Self-Refresh and more peripherals in the Main domain
  remain powered compared to RTC + I/O + DDR mode, providing faster resume at the cost of higher power
- **State ID = 0x2234**: Platform-specific identifier for "RTC + I/O + DDR" mode where DDR is in
  Self-Refresh and only minimal peripherals (RTC, I/O retention) remain powered in the Main
  domain, providing maximum power savings at the cost of longer resume latency

The cpuidle governor uses these latency and residency values to automatically select the appropriate
mode. If predicted idle time is short and latency constraints are tight, the governor will choose
DeepSleep mode (the shallower state) for faster resume. For longer predicted idle periods with relaxed
latency requirements, the preferred state is RTC + I/O + DDR mode (the deeper state) for maximum power savings.

************************
How Mode Selection Works
************************

During s2idle entry, the cpuidle framework drives each CPU into its idle path. As
each CPU idles, the Generic Power Domain (genpd) layer performs a bottom-up traversal
of the power domain hierarchy - from ``CPU_PD`` up through ``CLUSTER_PD``,
``SYSTEM_PD``, then ``SOC_PD`` - attempting to power off each domain in turn. At
every level the genpd and cpuidle governor asks two questions:

1. **Can this domain power off?** - Are all devices mapped to it via
   ``power-domain-map`` runtime-suspended, and are all child domains already in
   their deepest idle state?
2. **Which idle state can the system enter?** - Of the states available for this domain,
   which is the deepest one whose total latency (entry + exit) fits within the
   current QoS constraint?

Only after the system satisfies both conditions at a given level does the traversal
continue up to the parent domain. The last active CPU makes a ``CPU_SUSPEND`` PSCI call
with the deepest eligible state found in the power domain hierarchy.

.. note::

   The wakeup sources affect the selection of low power modes, due to how genpd treats the associated devices.

   On suspend, genpd keeps a device ON if it is in the wakeup path and is an in-band wakeup source, otherwise genpd will suspend it.
   Thus enabling/disabling a wakeup source can affect the eligibility of the corresponding power domain to power off,
   and thus the selection of low power modes.

Step-by-step traversal
======================

#. **CPU_PD - first CPU goes idle**

   When the first CPU enters the idle path, the cpuidle framework walks the
   available CPU-level idle states and filters out any whose total latency exceeds
   the active QoS constraint. The governor selects the deepest state that passes for that
   CPU.

   The kernel then attempts to propagate the power-off up the hierarchy to
   ``CLUSTER_PD``. However, since the second CPU is still active, genpd
   cannot power off the cluster yet - the traversal stops at ``CPU_PD``.

   The first CPU makes the ``CPU_SUSPEND`` PSCI call for the deepest possible cpu-idle-state.

#. **CPU_PD - second (last) CPU goes idle**

   When the second CPU enters its idle path, the same QoS-filtered search is
   repeated for ``CPU_PD``. Now that both CPUs are idle, the kernel is free to
   continue the traversal upward.

#. **CLUSTER_PD - can it power off?**

   At ``CLUSTER_PD``, the kernel checks:

   - All devices assigned to ``CLUSTER_PD`` are runtime-suspended.
   - Both ``CPU_PD`` instances are in their deepest idle state.
   - The QoS latency constraint is long enough to justify the cluster's entry and
     exit latency.

   If all checks pass, governor selects ``cluster_sleep_stby`` and the traversal
   continues up to ``SYSTEM_PD``.

#. **SYSTEM_PD, MAIN_PD, SOC_PD - selecting the system-level low power mode**

   The same two checks repeat at each remaining level: are all devices in this
   domain suspended, and does the deepest available idle state fit the QoS
   constraint?

   If a domain cannot power off at any level, the traversal stops there and the
   deepest state reached so far becomes the final selection.

#. **Composite state and PSCI call**

   Once the traversal completes, the last active CPU encodes the deepest eligible
   idle state into a ``CPU_SUSPEND`` PSCI call and issues it to TF-A, which carries
   out the actual hardware power-down sequence.

Examples
========

**Example 1: Latency constraint forces DeepSleep instead of RTC + I/O + DDR**

A QoS constraint of 500 ms is active. Genpd suspends all eligible devices and ``WKUP_PD``
is idle.

.. code-block:: text

   SOC_PD idle state evaluation (QoS constraint = 500 ms):
   |-> main_sleep_rtcddr: entry 300 ms + exit 600 ms = 900 ms -> REJECTED
   |-> MAIN_PD falls back to main_sleep_deep:
       entry 250 ms + exit 100 ms = 350 ms -> SELECTED

   Result: System enters DeepSleep

Even though RTC + I/O + DDR offers lower power, its 900 ms total latency exceeds the
500 ms constraint, so DeepSleep is the deepest permitted state.

**Example 2: Active USB blocks RTC + I/O + DDR but DeepSleep still possible**

For this example we consider no QoS latency constraint, but USB0 is active.
``WKUP_PD`` has USBs as mapped devices, and is a direct child of ``SOC_PD``.

.. code-block:: text

   MAIN_PD: DISPLAY_PD inactive, all SYSTEM_PD devices suspended
   |-> main_sleep_deep (DeepSleep): SELECTED

   SOC_PD: WKUP_PD cannot power off (USB0 active)
   |-> main_sleep_rtcddr (RTC + I/O + DDR): REJECTED

   Result: System enters DeepSleep

The active USB device only blocks ``SOC_PD`` from powering off. Since
``WKUP_PD`` is a sibling of ``MAIN_PD`` (not a child), ``MAIN_PD`` can still
enter DeepSleep. This is why the RTC + I/O + DDR section in :ref:`lpm_modes` requires
disabling USB wakeup sources - DeepSleep works regardless, but RTC + I/O + DDR requires
``WKUP_PD`` to be idle too.

.. warning::

   When disabling **serial MAIN UART** as a wakeup source, do not disable ``console_suspend`` in the kernel command line.

   The MAIN UART has out-of-band wakeup capability, thus genpd disables it on suspend. However, when UART is not a wakeup source,
   disabling ``console_suspend`` kernel parameter prevents genpd from suspending the MAIN UART(UART0), keeping it active.
   Because the power domain maps UART0 to ``SYSTEM_PD``, this prevents the system from entering any of the suspend
   to RAM modes, leaving the system in a partially suspended state from which it cannot resume.

   Use the ``[deep]`` path in ``/sys/power/mem_sleep`` when using the mentioned configuration.

*****************************************
Controlling Mode Selection from Userspace
*****************************************

.. _setting-cpu-wakeup-latency:

Setting CPU wakeup latency constraints
=======================================

Applications can constrain the system's low-power behavior by writing to the CPU wakeup latency entry.
Since constraints are "active" only while a file descriptor to this device remains open, there are two
ways to set the constraints - a C program or a simple bash command.

Below is a C program that demonstrates this:

.. code-block:: c

   /* set_qos.c - Set CPU wakeup latency constraint */
   #include <stdio.h>
   #include <fcntl.h>
   #include <unistd.h>
   #include <signal.h>

   #define QOS_DEV "/dev/cpu_wakeup_latency"
   #define LATENCY_VAL "0x7a120"  /* 500,000 us = 500ms in hex */

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

Alternatively, the userspace can set CPU wakeup latency constraint with the following bash command:

.. code-block:: bash

   exec 4<>/dev/cpu_wakeup_latency; echo 0x7a120 >&4

Execute this in a subshell to avoid accidentally keeping it open indefinitely.
