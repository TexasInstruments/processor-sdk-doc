======================================
 RT-linux 10.01 Performance Guide
======================================

.. rubric::  **Read This First**

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
| AM62A SK       | AM62A Starter Kit rev E2 with ARM running at 1200MHz, LPDDR4 data rate is 3733 MT/s                            |
+----------------+----------------------------------------------------------------------------------------------------------------+

Table:  Evaluation Modules

|

.. rubric::  About This Manual

This document provides performance data for each of the device drivers
which are part of the Process SDK Linux package. This document should be
used in conjunction with release notes and user guides provided with the
Process SDK Linux package for information on specific issues present
with drivers included in a particular release.

.. rubric::  If You Need Assistance

For further information or to report any problems, contact
https://e2e.ti.com/ or https://support.ti.com/

|

System Benchmarks
-------------------------

Stress-ng and Cyclic Test

.. _RT-linux-performance:

stress-ng (next-generation) will stress test a embedded platform in various selectable ways.
It was designed to exercise various physical subsystems as well as the various
operating system kernel interfaces. stress-ng can also measure test throughput rates;
this can be useful to observe performance changes across different operating system or types of hardware.

Cyclictest is most commonly used for benchmarking RT systems.
It is one of the most frequently used tools for evaluating the relative performance of real-time systems.
Some performance tests which use Cyclictest are System benchmarking, Latency debugging with tracing and
approximating application performance.

Test commands used for running stress-ng and cyclictest together

.. code:: console

   stress-ng --cpu-method=all -c 4 &
   cyclictest -m -Sp80 -D6h -h400 -i200 -M -q

The latencies where observed with this SDK are summarized below:

.. csv-table::
   :header: "Latencies","CPU 0","CPU 1","CPU 2","CPU 3"

   "Minimum (us)","5","5","5","5"
   "Average (us)","5","6","6","5"
   "Maximum (us)","68","31","34","28"

.. image:: img/rt-cpu-method-all-latency-histogram.png

