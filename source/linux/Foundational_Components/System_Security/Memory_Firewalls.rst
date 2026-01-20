.. _memory-firewalls:

################
Memory Firewalls
################

********
Overview
********

TI System-on-Chips (SoCs) use hardware-backed firewalls to enforce
access control. Texas Instruments Foundational Security (TIFS)
configures these firewalls to restrict the components that can access
specific regions of device-mapped memory. Other components such as
Open Portable Trusted Execution Environment (OP-TEE), Arm Trusted
Firmware (ATF), Linux, U-Boot, and user-space programs can request TIFS
to configure firewalls on their behalf.

Firewalls can restrict access based on:

*  **Core**: A53, R5, M4
*  **Privilege level**: privileged or non-privileged
*  **Security state**: secure or insecure

For example, TIFS might configure a firewall to prevent Linux (running
on A53) from accessing a memory region reserved for the secure world.

For more information about firewalls, see the Technical Reference
Manual (TRM) for the specific SoC, the
`TISCI Firewall API <https://software-dl.ti.com/tisci/esd/latest/2_tisci_msgs/security/firewall_api.html>`__,
and the
`TIFS Firewall FAQ <https://software-dl.ti.com/tisci/esd/latest/6_topic_user_guides/firewall_faq.html>`__.

****************************************
What Happens During a Firewall Violation
****************************************

When software attempts an unauthorized access to a memory region that
a firewall protects, the firewall blocks the access and triggers an
exception. The outcome depends on the type of access:

*  **Read access**: The firewall blocks the read. The system continues
   running.
*  **Write access**: The firewall blocks the write and crashes the
   Linux kernel. The system halts.

The kernel crash on write violations stops the offending software
immediately, preventing further unauthorized access attempts.

TIFS logs information about every firewall exception. The rest of this
document explains how to trigger exceptions, enable TIFS logs, access
them, and interpret them.

*******************************
Triggering a Firewall Exception
*******************************

To test firewall behavior, use ``k3conf`` to read from or write to a
protected memory region.

Triggering a read exception:

.. code-block:: console

   k3conf read <addr> [<size>]

Triggering a write exception (this will crash the kernel):

.. code-block:: console

   k3conf write <addr> <value>

Replace ``<addr>`` with the address of a firewall-protected region,
``<size>`` with the number of bytes to read, and ``<value>`` with the
value to write.

******************
Enabling TIFS Logs
******************

TIFS does not output logs by default. Enabling TIFS logging requires
modifying U-Boot source code, recompiling it, and transferring the new
binaries to the boot partition.

Modify U-Boot Configuration
===========================

Open :file:`board/ti/<soc_name>/board-cfg.yaml` in the U-Boot source
tree. Locate ``trace_dst_enables`` and ``trace_src_enables``, which
U-Boot sets to ``0x0`` by default. Change these values as follows:

*  ``trace_dst_enables``: change from ``0x0`` to ``0xD``
*  ``trace_src_enables``: change from ``0x0`` to ``0x3F``

Build and Deploy U-Boot
=======================

After making these changes, compile U-Boot and transfer the resulting
binaries to the board's boot partition. See
:ref:`u-boot-build-guide-build-k3` for build instructions.

*******************
Accessing TIFS Logs
*******************

TIFS outputs logs to a separate serial port from the Linux console.
If the Linux command line is accessible through :file:`/dev/ttyUSB0`, TIFS logs
are typically accessible through :file:`/dev/ttyUSB1`. However, the exact device
assignment depends on the hardware setup and the order in which the
host enumerates USB devices.

Open the TIFS serial port with a terminal emulator to view the logs.

**********************
Interpreting TIFS Logs
**********************

For information about interpreting firewall exception logs, see the
`TIFS Firewall FAQ <https://software-dl.ti.com/tisci/esd/latest/6_topic_user_guides/firewall_faq.html#how-do-i-debug-firewall-issues>`__.
