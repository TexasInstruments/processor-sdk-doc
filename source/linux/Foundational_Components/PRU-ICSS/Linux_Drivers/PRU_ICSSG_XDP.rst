.. _pru_icssg_xdp:

#############
PRU_ICSSG XDP
#############

.. contents:: :local:
    :depth: 3

************
Introduction
************

XDP (eXpress Data Path) provides a framework for BPF that enables high-performance programmable packet processing in the Linux kernel. It runs the BPF program at the earliest possible point in software, namely at the moment the network driver receives the packet.

XDP allows running a BPF program just before the skbs are allocated in the driver, the BPF program can look at the packet and return the following things.

- XDP_DROP :- The packet is dropped right away, without wasting any resources. Useful for firewall etc.
- XDP_ABORTED :- Similar to drop, an exception is generated.
- XDP_PASS :- Pass the packet to kernel stack, i.e. the skbs are allocated and it works normally.
- XDP_TX :- Send the packet back to same NIC with modification(if done by the program).
- XDP_REDIRECT :- Send the packet to another NIC or to the user space through AF_XDP Socket(discussed below).

.. Image:: /images/XDP-packet-processing.png

As explained before, the XDP_REDIRECT sends packets directly to the user space.
This works by using the AF_XDP socket type which was introduced specifically for this usecase.

In this process, the packet is directly sent to the user space without going through the kernel network stack.

.. Image:: /images/xdp-packet.png

Use cases for XDP
=================

XDP is particularly useful for these common networking scenarios:

1. **DDoS Mitigation**: High-speed packet filtering and dropping malicious traffic
2. **Load Balancing**: Efficient traffic distribution across multiple servers
3. **Packet Capture**: High-performance network monitoring without performance penalties
4. **Firewalls**: Wire-speed packet filtering based on flexible rule sets
5. **Network Analytics**: Real-time traffic analysis and monitoring
6. **Custom Network Functions**: Specialized packet handling for unique requirements

How to run XDP with PRU_ICSSG
=============================

The kernel configuration requires the following changes to use XDP with PRU_ICSSG:

.. code-block:: console

   CONFIG_DEBUG_INFO_BTF=y
   CONFIG_BPF_PRELOAD=y
   CONFIG_BPF_PRELOAD_UMD=y
   CONFIG_BPF_EVENTS=y
   CONFIG_BPF_LSM=y
   CONFIG_DEBUG_INFO_REDUCED=n
   CONFIG_FTRACE=y
   CONFIG_XDP_SOCKETS=y

Tools for debugging XDP Applications
====================================

Debugging tools for XDP development:

- bpftool - For loading and managing BPF programs
- xdpdump - For capturing XDP packet data
- perf - For performance monitoring and analysis
- bpftrace - For tracing BPF program execution

**************
AF_XDP Sockets
**************

AF_XDP is a socket address family specifically designed to work with the XDP framework.
These sockets provide a high-performance interface for user space applications to receive
and transmit network packets directly from the XDP layer, bypassing the traditional kernel networking stack.

Key characteristics of AF_XDP sockets include:

- Direct path from network driver to user space applications
- Shared memory rings for efficient packet transfer
- Minimal overhead compared to traditional socket interfaces
- Optimized for high-throughput, low-latency applications

How AF_XDP Works
================

AF_XDP sockets operate through a shared memory mechanism:

1. XDP program intercepts packets at driver level
2. XDP_REDIRECT action sends packets to the socket
3. Shared memory rings (RX/TX/FILL/COMPLETION) manage packet data
4. Userspace application directly accesses the packet data
5. Zero or minimal copying depending on the mode used

The AF_XDP architecture uses several ring buffers:

- **RX Ring**: Received packets ready for consumption
- **TX Ring**: Packets to be transmitted
- **FILL Ring**: Pre-allocated buffers for incoming packets
- **COMPLETION Ring**: Tracks completed TX operations

For more details on AF_XDP please refer to the official documentation: `AF_XDP <https://www.kernel.org/doc/html/latest/networking/af_xdp.html>`_.

Current Support Status in PRU_ICSSG
===================================

The PRU_ICSSG Ethernet driver currently supports:

- Native XDP mode
- Generic XDP mode (SKB-based)
- Zero-copy mode

**************************
XDP Zero-Copy in PRU_ICSSG
**************************

Introduction to Zero-Copy Mode
==============================

Zero-copy mode is an optimization in AF_XDP that eliminates packet data copying between the kernel and user space. This results in significantly improved performance for high-throughput network applications.

How Zero-Copy Works
===================

In standard XDP operation (copy mode), packet data is copied from kernel memory to user space memory when processed. Zero-copy mode eliminates this copy operation by:

1. Using memory-mapped regions shared between the kernel and user space
2. Allowing direct DMA from network hardware into memory accessible by user space applications
3. Managing memory ownership through descriptor rings rather than data movement

This approach provides several benefits:
- Reduced CPU utilization
- Lower memory bandwidth consumption
- Decreased latency for packet processing
- Improved overall throughput

Requirements for Zero-Copy
==========================

For zero-copy to function properly with PRU_ICSSG, ensure:

1. **Driver Support**: Verify the PRU_ICSSG driver is loaded with zero-copy support enabled
2. **Memory Alignment**: Buffer addresses must be properly aligned to page boundaries
3. **UMEM Configuration**: The UMEM area must be correctly configured:
   - Properly aligned memory allocation
   - Sufficient number of packet buffers
   - Appropriate buffer sizes
4. **Hugepages**: Using hugepages for UMEM allocation is recommended for optimal performance

Performance Comparison
======================

Performance testing shows that zero-copy mode can provide substantial throughput improvements compared to copy mode:

`xdpsock <https://github.com/xdp-project/bpf-examples/tree/main/AF_XDP-example>`_ opensource tool was used for testing XDP zero copy.
AF_XDP performance while using 64 byte packets in Kpps:

.. list-table::
   :header-rows: 1

   * - Benchmark
     - XDP-SKB
     - XDP-Native
     - XDP-Native(ZeroCopy)
   * - rxdrop
     - 253
     - 473
     - 656
   * - txonly
     - 350
     - 354
     - 855

Performance Considerations
==========================

When implementing XDP applications, consider these performance factors:

1. **Memory Alignment**: Buffers should be aligned to page boundaries for optimal performance
2. **Batch Processing**: Process multiple packets in batches when possible
3. **Poll Mode**: Use poll() or similar mechanisms to avoid blocking on socket operations
4. **Core Affinity**: Bind application threads to specific CPU cores to reduce cache contention
5. **NUMA Awareness**: Consider NUMA topology when allocating memory for packet buffers
