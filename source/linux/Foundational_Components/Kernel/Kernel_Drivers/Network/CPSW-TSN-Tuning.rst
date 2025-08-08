.. _tsn_tuning:

=======================
TSN Switch Tuning Guide
=======================

.. contents:: :local:
   :depth: 2

The size of each FIFO TX queue in CPSW is 2K Bytes by default and packets
might have to be queued in the switch temporarily depending on the TSN
feature being used. Tuning the TSN feature appropriately ensures that there
is no packet loss.

The following TSN features in switch mode can be tuned for optimizing the
performance:

   1. EST (Enhanced Scheduler for Traffic)
   2. CBS (Credit Based Shaper)
   3. IET (Interspersing Express Traffic)


Background
==========

The total memory pool available for each port for TX and RX queues is 20K
Bytes on both J7xxx and AM6xx devices. This memory of 20K Bytes has to be
shared between the 8 TX and 1 RX queues in the form of 1K or 4K Byte blocks.
The existing allocation is in the form of 17 - 1K Byte blocks to be shared
between the 8 TX queues and 3 - 1K Byte blocks for the RX queue. This implies
that the memory available per TX queue is roughly 2K Bytes. Thus, if the packet
size is 1K Bytes, then at most 2 packets can be in a queue before the queue is
full and the incoming packets get dropped.
The impact of the queue size on various TSN features in switch mode is
described in detail in the following sections. This serves the purpose of
providing suggestions for tuning the performance.


EST (Enhanced Scheduler for Traffic)
====================================

EST involves stopping and releasing packets only at specific time intervals as
specified by the schedule. Thus, if the cycle-time is not low enough, or if the
packet transmission rate is high, in both these cases, the queue will overflow
resulting in packet drops.
Consider an EST schedule where the maximum wait time for one of the priorities
is X microseconds, with the packets arriving at Y Bytes per second for this
priority which has the longest wait time of X microseconds. Also, the TX queue
size is 2K Bytes = 2048 Bytes.
The EST schedule would be as follows:

.. code:: text

   Priority 0          X0 microseconds
   Priority 1          X1 microseconds
   Priority 2          X2 microseconds
   Priority .          .  microseconds
   Priority .          .  microseconds
   Priority n-1        Xn-1 microseconds

Here, the Cycle-Time is X0+X1+...+Xn-1
And, X is the maximum of (Cycle-Time - Xj) over all j from 0 to n-1,
which corresponds to the maximum time that one of all the n priorities has to
wait for its turn.
Then, to prevent packet drops, we require:

.. code:: text

   (Maximum-Wait-Time)*(Throughput) < Queue-Size

   Or,
      (X microseconds)*(Y Bytes/Second) < 2048 Bytes
      (X*10^-6 Seconds)*(Y Bytes/Second) < 2048 Bytes
   Thus, numerically,
      X*Y < 2048000000

Using the above condition, we can find out the maximum wait-time for different
throughput as follows:

.. code:: text

   1. Throughput of 10 Mbps (Y = 10*1024*1024/8 Bytes/Second)
      => X*(10*1024*1024/8) < 2048000000
      => X < 2048000000*8/(10*1024*1024)
      Thus, X < 1562.5 microseconds
      If X is greater than this value, then there will be packet drops
      for 10 Mbps throughput.
   2. Similarly, for 100 Mbps throughput,
      => X < 156.25 microseconds
   3. And for 1000 Mbps throughput,
      => X < 15.625 microseconds.

We can also use the condition to derive the maximum throughput allowed for a
given EST as follows:
For example, consider an EST schedule as follows:

.. code:: text

   Priority-0 200 microseconds
   Priority-1 300 microseconds
   Here, Cycle-Time is 500 microseconds and X = 300
   Thus,
      300*Y < 2048000000
   Or,
      => Y < 6826666 Bytes per second
      => Y < 52 Mbps is the throughput limit to prevent packet drops.

Also, if Y has to increase, then X, and therefore Cycle-Time have
to decrease for preventing packet drops.

CBS (Credit Based Shaper)
=========================

CBS involves rate-limiting the throughput on different queues. Thus, when the
traffic on a queue exceeds the allotted throughput, then the queue gate is
closed, preventing packet flow from that queue. This will result in the queue
being filled quickly, again resulting in packet drops.
For a CBS schedule where there are N priorities with the rate-limiting on each
of these priorities being:

.. code::text

   X0, X1, .... XN-1 Bytes per second.

If the actual throughput of each of these priorities is:

.. code::text

   Y0, Y1, .... YN-1 Bytes per second,

and they are all greater than the rate-limits, then, the queues will fill up in:

.. code::text

   2048/(Y0-X0), 2048/(Y1-X1), .... seconds.

In general, queue 'i' will fill up in:

.. code:: text

   2048/(Yi-Xi) seconds

For example, consider N=2, with X0=300 Mbps, X1=400 Mbps, Y0=301 Mbps and Y1=410
Mbps. Y0 and Y1 are higher than X0 and X1 , thereby causing the switch to
implement rate-limiting.
Thus, traffic accumulates at a rate of (Y0-X0) and (Y1-X1) on queues 0 and 1 and
starts filling them up.
For the example above, it would take:

.. code:: text

   15.625 milliseconds to fill up queue 0, and
   1.5625 milliseconds to fill up queue 1,

resulting in packet drops after that time on those queues if the existing
throughput continues on those queues.

IET (Interspersing Express Traffic)
===================================

IET involves frame preemption whereby high priority traffic overrides the low
priority traffic. Thus, when packets being sent on a low priority queue are
preempted for allowing packets on higher priority queue to pass, first the frame
being transmitted on low priority queue is fragmented. Then, the high priority
traffic is allowed to pass. In the meanwhile, traffic on the low priority queue
starts filling up the queue, resulting in packet drops.
If the low priority traffic is arriving at Y Bytes per second, it would fill up
the queue in:

.. code:: text

   2048/Y seconds.

For example, if low priority traffic is arriving at 100 Mbps, it would fill up
the queue in:

.. code:: text

   156.25 microseconds.
