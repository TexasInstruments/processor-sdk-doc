
#################################
 Linux 12.00.00 Performance Guide
#################################

***************
Read This First
***************

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM62Dx EVM     | AM62Dx Evaluation Module rev E1 with ARM running at 1.4GHz, DDR data rate 3733 MT/S                            |
+----------------+----------------------------------------------------------------------------------------------------------------+

Table:  Evaluation Modules

*****************
About This Manual
*****************

This document provides performance data for each of the device drivers
which are part of the Processor SDK Linux package. This document should be
used in conjunction with release notes and user guides provided with the
Processor SDK Linux package for information on specific issues present
with drivers included in a particular release.

For further information or to report any problems, contact
https://e2e.ti.com/ or https://support.ti.com/

|

*****************
System Benchmarks
*****************

|

LMBench
=======

LMBench is a collection of microbenchmarks of which the memory bandwidth 
and latency related ones are typically used to estimate processor 
memory system performance. More information about lmbench at
https://lmbench.sourceforge.net/whatis_lmbench.html and
https://lmbench.sourceforge.net/man/lmbench.8.html

**Latency**: lat_mem_rd-stride128-szN, where N is equal to or smaller than the cache
size at given level measures the cache miss penalty. N that is at least
double the size of last level cache is the latency to external memory.

**Bandwidth**: bw_mem_bcopy-N, where N is equal to or smaller than the cache size at
a given level measures the achievable memory bandwidth from software doing
a memcpy() type operation. Typical use is for external memory bandwidth
calculation. The bandwidth is calculated as byte read and written counts
as 1 which should be roughly half of STREAM copy result.

Execute the LMBench with the following:

::

    cd /opt/ltp
    ./runltp -P j721e-idk-gw -f ddt/lmbench -s LMBENCH_L_PERF_0001

.. csv-table:: LMBench Benchmarks
    :header: "Benchmarks","am62dxx_evm-fs: perf"

    "af_unix_sock_stream_latency (microsec)","26.25 (min 23.23, max 29.86)"
    "af_unix_socket_stream_bandwidth (mb\s)","1071.71 (min 1058.15, max 1084.28)"
    "bw_file_rd-io-1mb (mb/s)","1348.18 (min 1335.78, max 1359.22)"
    "bw_file_rd-o2c-1mb (mb/s)","696.88 (min 633.61, max 771.01)"
    "bw_mem-bcopy-16mb (mb/s)","1742.80 (min 1730.67, max 1760.18)"
    "bw_mem-bcopy-1mb (mb/s)","1865.40 (min 1833.37, max 1893.94)"
    "bw_mem-bcopy-2mb (mb/s)","1625.86 (min 1561.59, max 1675.32)"
    "bw_mem-bcopy-4mb (mb/s)","1648.95 (min 1618.78, max 1670.84)"
    "bw_mem-bcopy-8mb (mb/s)","1674.23 (min 1590.62, max 1730.10)"
    "bw_mem-bzero-16mb (mb/s)","7939.79 (min 7935.20, max 7947.02)"
    "bw_mem-bzero-1mb (mb/s)","4882.93 (min 1833.37, max 7950.36)"
    "bw_mem-bzero-2mb (mb/s)","4763.62 (min 1561.59, max 7916.52)"
    "bw_mem-bzero-4mb (mb/s)","4781.67 (min 1618.78, max 7926.50)"
    "bw_mem-bzero-8mb (mb/s)","4802.10 (min 1590.62, max 7943.07)"
    "bw_mem-cp-16mb (mb/s)","841.31 (min 833.20, max 851.06)"
    "bw_mem-cp-1mb (mb/s)","4496.61 (min 783.70, max 8222.18)"
    "bw_mem-cp-2mb (mb/s)","4414.12 (min 780.03, max 8041.96)"
    "bw_mem-cp-4mb (mb/s)","4417.08 (min 815.58, max 8002.91)"
    "bw_mem-cp-8mb (mb/s)","4429.55 (min 846.20, max 7980.05)"
    "bw_mem-fcp-16mb (mb/s)","1554.75 (min 1535.21, max 1576.04)"
    "bw_mem-fcp-1mb (mb/s)","4733.08 (min 1539.78, max 7950.36)"
    "bw_mem-fcp-2mb (mb/s)","4701.07 (min 1459.06, max 7916.52)"
    "bw_mem-fcp-4mb (mb/s)","4726.03 (min 1495.51, max 7926.50)"
    "bw_mem-fcp-8mb (mb/s)","4740.18 (min 1540.24, max 7943.07)"
    "bw_mem-frd-16mb (mb/s)","1841.28 (min 1782.13, max 1859.38)"
    "bw_mem-frd-1mb (mb/s)","1754.60 (min 1539.78, max 1975.57)"
    "bw_mem-frd-2mb (mb/s)","1618.86 (min 1459.06, max 1750.09)"
    "bw_mem-frd-4mb (mb/s)","1648.13 (min 1495.51, max 1827.32)"
    "bw_mem-frd-8mb (mb/s)","1658.91 (min 1540.24, max 1849.92)"
    "bw_mem-fwr-16mb (mb/s)","7957.56 (min 7949.65, max 7964.16)"
    "bw_mem-fwr-1mb (mb/s)","5064.88 (min 1899.83, max 8222.18)"
    "bw_mem-fwr-2mb (mb/s)","4873.22 (min 1723.84, max 8041.96)"
    "bw_mem-fwr-4mb (mb/s)","4873.01 (min 1684.21, max 8002.91)"
    "bw_mem-fwr-8mb (mb/s)","4869.76 (min 1689.72, max 7980.05)"
    "bw_mem-rd-16mb (mb/s)","1930.96 (min 1920.08, max 1941.51)"
    "bw_mem-rd-1mb (mb/s)","1704.69 (min 1174.50, max 2232.56)"
    "bw_mem-rd-2mb (mb/s)","1532.41 (min 1099.30, max 1964.96)"
    "bw_mem-rd-4mb (mb/s)","1624.88 (min 1203.55, max 1922.15)"
    "bw_mem-rd-8mb (mb/s)","1714.81 (min 1360.78, max 1945.05)"
    "bw_mem-rdwr-16mb (mb/s)","1609.39 (min 1560.52, max 1682.09)"
    "bw_mem-rdwr-1mb (mb/s)","1008.69 (min 783.70, max 1286.29)"
    "bw_mem-rdwr-2mb (mb/s)","970.31 (min 780.03, max 1168.68)"
    "bw_mem-rdwr-4mb (mb/s)","1109.24 (min 815.58, max 1465.74)"
    "bw_mem-rdwr-8mb (mb/s)","1224.13 (min 846.20, max 1571.40)"
    "bw_mem-wr-16mb (mb/s)","1620.26 (min 1557.03, max 1666.84)"
    "bw_mem-wr-1mb (mb/s)","1214.54 (min 1156.07, max 1286.29)"
    "bw_mem-wr-2mb (mb/s)","1139.75 (min 1096.49, max 1257.66)"
    "bw_mem-wr-4mb (mb/s)","1356.70 (min 1203.55, max 1465.74)"
    "bw_mem-wr-8mb (mb/s)","1534.69 (min 1360.78, max 1571.40)"
    "bw_mmap_rd-mo-1mb (mb/s)","2054.67 (min 2010.97, max 2106.47)"
    "bw_mmap_rd-o2c-1mb (mb/s)","721.65 (min 636.84, max 812.35)"
    "bw_pipe (mb/s)","712.68 (min 661.13, max 740.02)"
    "bw_unix (mb/s)","1071.71 (min 1058.15, max 1084.28)"
    "lat_connect (us)","61.57 (min 50.64, max 72.15)"
    "lat_ctx-2-128k (us)","8.53 (min 7.89, max 9.31)"
    "lat_ctx-2-256k (us)","18.50 (min 6.99, max 40.68)"
    "lat_ctx-4-128k (us)","14.98 (min 8.17, max 29.59)"
    "lat_ctx-4-256k (us)","22.67 (min 7.08, max 97.51)"
    "lat_fs-0k (num_files)","280.00 (min 256.00, max 311.00)"
    "lat_fs-10k (num_files)","123.50 (min 105.00, max 141.00)"
    "lat_fs-1k (num_files)","187.17 (min 173.00, max 203.00)"
    "lat_fs-4k (num_files)","180.67 (min 163.00, max 207.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","30.92 (min 30.56, max 31.60)"
    "lat_mem_rd-stride128-sz125k (ns)","5.57 (min 5.54, max 5.63)"
    "lat_mem_rd-stride128-sz250k (ns)","5.83 (min 5.82, max 5.84)"
    "lat_mem_rd-stride128-sz31k (ns)","3.49 (min 2.15, max 4.20)"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","11.53 (min 10.19, max 12.71)"
    "lat_mem_rd-stride128-sz62k (ns)","5.23 (min 5.19, max 5.25)"
    "lat_mmap-1m (us)","53.33 (min 49.00, max 58.00)"
    "lat_ops-double-add (ns)","2.86 (min 2.86, max 2.87)"
    "lat_ops-double-div (ns)","15.74"
    "lat_ops-double-mul (ns)","2.86"
    "lat_ops-float-add (ns)","2.86 (min 2.86, max 2.87)"
    "lat_ops-float-div (ns)","9.30 (min 9.30, max 9.31)"
    "lat_ops-float-mul (ns)","2.86"
    "lat_ops-int-add (ns)","0.72"
    "lat_ops-int-bit (ns)","0.48"
    "lat_ops-int-div (ns)","4.30 (min 4.29, max 4.30)"
    "lat_ops-int-mod (ns)","4.53 (min 4.53, max 4.54)"
    "lat_ops-int-mul (ns)","3.09 (min 3.04, max 3.12)"
    "lat_ops-int64-add (ns)","0.72"
    "lat_ops-int64-bit (ns)","0.48"
    "lat_ops-int64-div (ns)","6.80"
    "lat_ops-int64-mod (ns)","5.25"
    "lat_ops-int64-mul (ns)","3.57 (min 3.54, max 3.64)"
    "lat_pagefault (us)","0.44"
    "lat_pipe (us)","21.45 (min 20.89, max 21.91)"
    "lat_proc-exec (us)","714.75 (min 702.50, max 721.88)"
    "lat_proc-fork (us)","632.38 (min 613.13, max 654.78)"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","31.59 (min 31.34, max 31.76)"
    "lat_sem (us)","2.73 (min 2.22, max 3.05)"
    "lat_sig-catch (us)","5.60 (min 5.47, max 5.74)"
    "lat_sig-install (us)","0.65 (min 0.58, max 0.71)"
    "lat_sig-prot (us)","0.85 (min 0.71, max 0.92)"
    "lat_syscall-fstat (us)","1.81 (min 1.74, max 1.87)"
    "lat_syscall-null (us)","0.44 (min 0.37, max 0.51)"
    "lat_syscall-open (us)","206.84 (min 162.68, max 241.21)"
    "lat_syscall-read (us)","0.75 (min 0.73, max 0.79)"
    "lat_syscall-stat (us)","4.15 (min 3.99, max 4.26)"
    "lat_syscall-write (us)","0.70 (min 0.66, max 0.75)"
    "lat_tcp (us)","0.89 (min 0.76, max 1.02)"
    "lat_unix (us)","26.25 (min 23.23, max 29.86)"
    "latency_for_0.50_mb_block_size (nanosec)","11.53 (min 10.19, max 12.71)"
    "latency_for_1.00_mb_block_size (nanosec)","15.46 (min 0.00, max 31.60)"
    "pipe_bandwidth (mb\s)","712.68 (min 661.13, max 740.02)"
    "pipe_latency (microsec)","21.45 (min 20.89, max 21.91)"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","31.59 (min 31.34, max 31.76)"
    "semaphore_latency (microsec)","2.73 (min 2.22, max 3.05)"
    "signal_handler_latency (microsec)","0.65 (min 0.58, max 0.71)"
    "signal_handler_overhead (microsec)","5.60 (min 5.47, max 5.74)"
    "tcp_ip_connection_cost_to_localhost (microsec)","61.57 (min 50.64, max 72.15)"
    "tcp_latency_using_localhost (microsec)","0.89 (min 0.76, max 1.02)"

Dhrystone
=========

Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed.

Please take note, different run may produce different slightly results.
This is advised to run this test multiple times in order to get maximum 
performance numbers.

Execute the benchmark with the following:

::

    runDhrystone

.. csv-table:: Dhrystone Benchmarks
    :header: "Benchmarks","am62dxx_evm-fs: perf"

    "cpu_clock (mhz)","1400.00"
    "dhrystone_per_mhz (dmips/mhz)","2.75 (min 2.60, max 2.90)"
    "dhrystone_per_second (dhrystonep)","6789289.58 (min 6451613.00, max 7142857.00)"

Whetstone
=========

Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62dxx_evm-fs: perf"

    "whetstone (mips)","5833.33 (min 5000.00, max 10000.00)"

Linpack
=======

Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62dxx_evm-fs: perf"

    "linpack (kflops)","580360.75 (min 579515.00, max 581724.00)"

Stream
======

STREAM is a microbenchmark for measuring data memory system performance without
any data reuse. It is designed to miss on caches and exercise data prefetcher
and speculative accesses.
It uses double precision floating point (64bit) but in
most modern processors the memory access will be the bottleneck.
The four individual scores are copy, scale as in multiply by constant,
add two numbers, and triad for multiply accumulate.
For bandwidth, a byte read counts as one and a byte written counts as one,
resulting in a score that is double the bandwidth LMBench will show.

Execute the benchmark with the following:

::

    stream_c

.. csv-table:: Stream Benchmarks
    :header: "Benchmarks","am62dxx_evm-fs: perf"

    "add (mb/s)","2566.47 (min 2557.40, max 2582.90)"
    "copy (mb/s)","3540.12 (min 3515.30, max 3565.80)"
    "scale (mb/s)","3346.33 (min 3203.90, max 3405.60)"
    "triad (mb/s)","2384.27 (min 2377.90, max 2393.60)"

CoreMarkPro
===========

CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62dxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","41.99 (min 41.84, max 42.02)"
    "core (workloads/)","0.30"
    "coremark-pro ()","928.67 (min 892.10, max 957.91)"
    "linear_alg-mid-100x100-sp (workloads/)","14.68 (min 14.68, max 14.69)"
    "loops-all-mid-10k-sp (workloads/)","0.71"
    "nnet_test (workloads/)","1.08"
    "parser-125k (workloads/)","8.96 (min 8.77, max 9.26)"
    "radix2-big-64k (workloads/)","63.08 (min 44.67, max 75.93)"
    "sha-test (workloads/)","81.19 (min 80.65, max 81.97)"
    "zip-test (workloads/)","22.66 (min 22.22, max 23.81)"


.. csv-table:: CoreMarkProFourCore Benchmarks
    :header: "Benchmarks","am62dxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","159.05 (min 158.73, max 161.29)"
    "core (workloads/)","1.20"
    "coremark-pro ()","2592.85 (min 2558.16, max 2639.06)"
    "linear_alg-mid-100x100-sp (workloads/)","56.35 (min 56.24, max 56.43)"
    "loops-all-mid-10k-sp (workloads/)","2.05 (min 2.01, max 2.11)"
    "nnet_test (workloads/)","3.59"
    "parser-125k (workloads/)","11.93 (min 9.98, max 13.65)"
    "radix2-big-64k (workloads/)","76.45 (min 71.88, max 81.33)"
    "sha-test (workloads/)","266.71 (min 263.16, max 270.27)"
    "zip-test (workloads/)","78.74 (min 74.07, max 83.33)"

MultiBench
==========

MultiBench™ is a suite of benchmarks that allows processor and system designers to
analyze, test, and improve multicore processors. It uses three forms of concurrency:
Data decomposition: multiple threads cooperating on achieving a unified goal and
demonstrating a processor’s support for fine grain parallelism.
Processing multiple data streams: uses common code running over multiple threads and
demonstrating how well a processor scales over scalable data inputs.
Multiple workload processing: shows the scalability of general-purpose processing,
demonstrating concurrency over both code and data.
MultiBench combines a wide variety of application-specific workloads with the EEMBC
Multi-Instance-Test Harness (MITH), compatible and portable with most any multicore
processors and operating systems. MITH uses a thread-based API (POSIX-compliant) to
establish a common programming model that communicates with the benchmark through an
abstraction layer and provides a flexible interface to allow a wide variety of
thread-enabled workloads to be tested.

.. csv-table:: Multibench Benchmarks
    :header: "Benchmarks","am62dxx_evm-fs: perf"

    "4m-check (workloads/)","423.43 (min 421.30, max 428.08)"
    "4m-check-reassembly (workloads/)","122.51 (min 108.93, max 172.71)"
    "4m-check-reassembly-tcp (workloads/)","62.57 (min 59.52, max 73.75)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","34.10 (min 33.67, max 34.90)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.89 (min 1.88, max 1.89)"
    "4m-cmykw2 (workloads/)","245.65 (min 239.52, max 250.00)"
    "4m-cmykw2-rotatew2 (workloads/)","47.70 (min 46.77, max 49.75)"
    "4m-reassembly (workloads/)","91.00 (min 76.45, max 147.06)"
    "4m-rotatew2 (workloads/)","52.53 (min 51.79, max 54.11)"
    "4m-tcp-mixed (workloads/)","128.00 (min 126.98, max 129.03)"
    "4m-x264w2 (workloads/)","1.95 (min 1.93, max 1.98)"
    "idct-4m (workloads/)","19.28 (min 19.16, max 19.76)"
    "idct-4mw1 (workloads/)","19.28 (min 19.15, max 19.74)"
    "ippktcheck-4m (workloads/)","422.45 (min 418.62, max 428.52)"
    "ippktcheck-4mw1 (workloads/)","422.78 (min 419.96, max 426.40)"
    "ipres-4m (workloads/)","101.92 (min 99.60, max 107.84)"
    "ipres-4mw1 (workloads/)","102.01 (min 99.87, max 108.38)"
    "md5-4m (workloads/)","28.00 (min 27.77, max 28.14)"
    "md5-4mw1 (workloads/)","28.03 (min 27.97, max 28.12)"
    "rgbcmyk-4m (workloads/)","63.80 (min 63.41, max 64.54)"
    "rgbcmyk-4mw1 (workloads/)","63.80 (min 63.45, max 64.45)"
    "rotate-4ms1 (workloads/)","23.83 (min 23.29, max 25.80)"
    "rotate-4ms1w1 (workloads/)","23.84 (min 23.28, max 25.80)"
    "rotate-4ms64 (workloads/)","24.14 (min 23.56, max 26.11)"
    "rotate-4ms64w1 (workloads/)","24.14 (min 23.57, max 26.08)"
    "x264-4mq (workloads/)","0.58"
    "x264-4mqw1 (workloads/)","0.58"

|

Boot-time Measurement
=====================

Boot media: MMCSD
-----------------

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62dxx_evm-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","17.16 (min 16.40, max 18.33)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

Ethernet
========

Ethernet performance benchmarks were measured using :command:`netperf` 2.7.1 https://hewlettpackard.github.io/netperf/doc/netperf.html
Test procedures were modeled after those defined in RFC-2544:
https://tools.ietf.org/html/rfc2544, where the DUT is the TI device
and the "tester" used was a Linux PC. To produce consistent results,
it is recommended to carry out performance tests in a private network and to avoid
running NFS on the same interface used in the test. In these results,
CPU utilization was captured as the total percentage used across all cores on the device,
while running the performance test over one external interface.

UDP Throughput (0% loss) was measured by the procedure defined in RFC-2544 section 26.1: Throughput.
In this scenario, :command:`netperf` options burst_size (-b) and wait_time (-w) are used to limit bandwidth
during different trials of the test, with the goal of finding the highest rate at which
no loss is seen. For example, to limit bandwidth to 500Mbits/sec with 1472B datagram:

.. code-block:: console

   burst_size = <bandwidth (bits/sec)> / 8 (bits -> bytes) / <UDP datagram size> / 100 (seconds -> 10 ms)
   burst_size = 500000000 / 8 / 1472 / 100 = 425

   wait_time = 10 milliseconds (minimum supported by Linux PC used for testing)

UDP Throughput (possible loss) was measured by capturing throughput and packet loss statistics when
running the :command:`netperf` test with no bandwidth limit (remove -b/-w options).

In order to start a :command:`netperf` client on one device, the other device must have :command:`netserver` running.
To start :command:`netserver`:

.. code-block:: console

   netserver [-p <port_number>] [-4 (IPv4 addressing)] [-6 (IPv6 addressing)]

Running the following shell script from the DUT will trigger :command:`netperf` clients to measure
bidirectional TCP performance for 60 seconds and report CPU utilization. Parameter -k is used in
client commands to summarize selected statistics on their own line and -j is used to gain
additional timing measurements during the test.

.. code-block:: console

   #!/bin/bash
   for i in 1
   do
      netperf -H <tester ip> -j -c -l 60 -t TCP_STREAM --
         -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE &

      netperf -H <tester ip> -j -c -l 60 -t TCP_MAERTS --
         -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE &
   done

Running the following commands will trigger :command:`netperf` clients to measure UDP burst performance for
60 seconds at various burst/datagram sizes and report CPU utilization.

- For UDP egress tests, run :command:`netperf` client from DUT and start :command:`netserver` on tester.

.. code-block:: console

   netperf -H <tester ip> -j -c -l 60 -t UDP_STREAM -b <burst_size> -w <wait_time> -- -m <UDP datagram size>
      -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE

- For UDP ingress tests, run :command:`netperf` client from tester and start :command:`netserver` on DUT.

.. code-block:: console

   netperf -H <DUT ip> -j -C -l 60 -t UDP_STREAM -b <burst_size> -w <wait_time> -- -m <UDP datagram size>
      -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE

CPSW/CPSW2g/CPSW3g Ethernet
---------------------------

UDP Throughput
^^^^^^^^^^^^^^

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62dxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62dxx_evm-fs: THROUGHPUT (Mbits/sec)","am62dxx_evm-fs: Packets Per Second (kPPS)","am62dxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","45.45","89","37.6"
    "128","","90.47","88","37.6"
    "256","","181.31","89","37.7"
    "1024","","704.12","86","37.1"
    "1518","","716.61","61","29.8"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62dxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62dxx_evm-fs: THROUGHPUT (Mbits/sec)","am62dxx_evm-fs: Packets Per Second (kPPS)","am62dxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","33.69","66","11.8"
    "128","","80.87","79","20.9"
    "256","","154.01","75","14.0"
    "1024","","617.87","75","23.8"
    "1518","","726.36","62","29.2"

.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62dxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62dxx_evm-fs: THROUGHPUT (Mbits/sec)","am62dxx_evm-fs: Packets Per Second (kPPS)","am62dxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","am62dxx_evm-fs: Packet Loss %"

    "64","","75.95 (min 67.93, max 98.26)","148.50 (min 133.00, max 192.00)","36.17 (min 34.38, max 38.15)","17.56 (min 1.13, max 64.36)"
    "128","","134.40 (min 129.62, max 137.51)","131.33 (min 127.00, max 134.00)","36.01 (min 33.95, max 38.93)","2.45 (min 0.78, max 4.73)"
    "256","","304.24 (min 272.41, max 387.16)","148.50 (min 133.00, max 189.00)","37.26 (min 35.26, max 39.33)","29.49 (min 0.84, max 62.35)"
    "1024","","909.90 (min 871.42, max 937.29)","111.00 (min 106.00, max 114.00)","38.69 (min 35.09, max 41.03)","0.77 (min 0.22, max 1.35)"
    "1518","","909.09 (min 860.26, max 930.92)","77.20 (min 73.00, max 79.00)","38.12 (min 35.95, max 39.53)","0.39 (min 0.09, max 1.30)"

|

OSPI
====

.. rubric:: AM62DXX-EVM
   :name: am62dxx-evm-ospi


.. rubric:: UBIFS
   :name: am62dxx-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62dxx_evm-fs: Write UBIFS Throughput (Mbytes/sec)","am62dxx_evm-fs: Write UBIFS CPU Load (%)","am62dxx_evm-fs: Read UBIFS Throughput (Mbytes/sec)","am62dxx_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.29)","27.95 (min 24.67, max 32.81)","27.80 (min 27.52, max 27.95)","7.71 (min 3.45, max 12.90)"
    "262144","0.14 (min 0.11, max 0.19)","28.36 (min 26.09, max 31.33)","27.79 (min 27.70, max 27.86)","7.53 (min 0.00, max 12.50)"
    "524288","0.15 (min 0.11, max 0.19)","28.01 (min 25.70, max 32.28)","27.62 (min 27.52, max 27.76)","7.47 (min 0.00, max 12.50)"
    "1048576","0.14 (min 0.11, max 0.19)","28.57 (min 25.89, max 33.40)","27.53 (min 27.25, max 27.95)","9.30 (min 3.57, max 17.14)"

.. rubric:: RAW
   :name: am62dxx-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62dxx_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","37.65 (min 37.59, max 37.88)"

| 

EMMC
====

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

EMMC EXT4 FIO 1G
----------------

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62dxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62dxx_evm-fs: Write EXT4 CPU Load (%)","am62dxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62dxx_evm-fs: Read EXT4 CPU Load (%)"

    "1m","85.83 (min 75.60, max 91.50)","1.53 (min 1.22, max 1.75)","151.50 (min 111.00, max 172.00)","1.58 (min 1.12, max 1.92)"
    "4m","89.93 (min 79.90, max 96.70)","1.00 (min 0.85, max 1.06)","147.33 (min 110.00, max 172.00)","1.25 (min 0.91, max 1.53)"
    "4k","45.29 (min 8.07, max 64.20)","14.48 (min 2.77, max 20.43)","80.38 (min 56.40, max 93.90)","19.07 (min 14.20, max 22.42)"
    "256k","82.67 (min 66.30, max 91.10)","1.80 (min 1.45, max 2.06)","144.65 (min 91.70, max 171.00)","2.19 (min 1.55, max 2.71)"

EMMC RAW FIO 1G
---------------

.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62dxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Write Raw CPU Load (%)","am62dxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Read Raw CPU Load (%)"

    "1m","84.78 (min 73.10, max 91.10)","1.35 (min 1.09, max 1.46)","153.33 (min 111.00, max 174.00)","1.58 (min 1.31, max 1.73)"
    "4m","90.07 (min 78.50, max 96.60)","0.97 (min 0.81, max 1.08)","153.33 (min 111.00, max 174.00)","1.20 (min 0.96, max 1.56)"
    "4k","45.31 (min 7.91, max 64.20)","10.99 (min 2.21, max 15.58)","78.82 (min 57.30, max 90.40)","17.15 (min 13.32, max 19.33)"
    "256k","81.52 (min 64.30, max 90.80)","1.66 (min 1.30, max 1.88)","146.50 (min 93.20, max 173.00)","2.11 (min 1.37, max 2.53)"

EMMC EXT4
---------

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62dxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62dxx_evm-fs: Write EXT4 CPU Load (%)","am62dxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62dxx_evm-fs: Read EXT4 CPU Load (%)"

    "102400","86.89 (min 45.15, max 93.13)","3.48 (min 2.69, max 4.97)","168.56 (min 120.34, max 179.02)","5.60 (min 4.58, max 5.98)"
    "262144","82.72 (min 48.35, max 93.80)","2.64 (min 1.28, max 4.30)","167.28 (min 99.38, max 181.01)","5.64 (min 3.11, max 6.93)"
    "524288","75.51 (min 46.27, max 94.05)","2.28 (min 1.16, max 4.30)","170.57 (min 119.47, max 181.80)","5.71 (min 4.01, max 6.49)"
    "1048576","77.20 (min 48.04, max 94.18)","2.31 (min 1.25, max 3.99)","170.74 (min 119.45, max 181.86)","5.40 (min 4.26, max 6.87)"
    "5242880","73.57 (min 46.13, max 93.84)","2.33 (min 1.25, max 3.99)","171.26 (min 119.41, max 181.87)","5.95 (min 4.01, max 6.52)"

EMMC EXT2
---------

.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am62dxx_evm-fs: Write EXT2 Throughput (Mbytes/sec)","am62dxx_evm-fs: Write EXT2 CPU Load (%)","am62dxx_evm-fs: Read EXT2 Throughput (Mbytes/sec)","am62dxx_evm-fs: Read EXT2 CPU Load (%)"

    "102400","39.87 (min 6.34, max 52.65)","3.51 (min 2.16, max 7.82)","142.95 (min 111.81, max 168.91)","5.88 (min 4.46, max 7.14)"
    "262144","43.68 (min 6.11, max 67.03)","3.01 (min 1.59, max 8.06)","143.60 (min 113.67, max 173.63)","5.80 (min 4.21, max 7.44)"
    "524288","49.98 (min 6.55, max 79.96)","3.06 (min 1.50, max 9.01)","156.50 (min 137.82, max 177.19)","5.87 (min 4.68, max 6.29)"
    "1048576","51.82 (min 6.71, max 84.10)","2.80 (min 1.46, max 9.31)","157.26 (min 139.07, max 176.20)","6.01 (min 4.68, max 7.05)"
    "5242880","56.15 (min 7.17, max 90.93)","2.64 (min 1.27, max 8.54)","156.67 (min 141.85, max 174.06)","6.03 (min 5.44, max 6.75)"

EMMC VFAT
---------

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62dxx_evm-fs: Write VFAT Throughput (Mbytes/sec)","am62dxx_evm-fs: Write VFAT CPU Load (%)","am62dxx_evm-fs: Read VFAT Throughput (Mbytes/sec)","am62dxx_evm-fs: Read VFAT CPU Load (%)"

    "102400","35.64 (min 10.18, max 49.91)","4.32 (min 3.04, max 5.60)","153.77 (min 133.47, max 173.84)","8.39 (min 5.88, max 10.70)"
    "262144","42.52 (min 11.62, max 62.06)","5.27 (min 2.89, max 7.99)","167.42 (min 153.80, max 175.94)","9.50 (min 8.24, max 10.55)"
    "524288","46.89 (min 12.01, max 71.89)","4.97 (min 3.55, max 6.88)","169.57 (min 157.20, max 175.58)","9.16 (min 8.00, max 10.08)"
    "1048576","50.75 (min 11.73, max 74.45)","4.85 (min 3.49, max 6.50)","168.96 (min 159.05, max 175.61)","9.57 (min 8.78, max 11.34)"
    "5242880","51.49 (min 12.38, max 80.25)","4.80 (min 3.03, max 6.70)","171.56 (min 167.20, max 175.54)","9.64 (min 8.87, max 10.04)"

 
UBoot EMMC
----------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62dxx_evm-fs: Write Throughput (Kbytes/sec)","am62dxx_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","97103.80 (min 92827.20, max 102721.00)","165591.77 (min 142469.57, max 172463.16)"
    "4000000","97707.35 (min 95533.53, max 98847.66)","173050.47 (min 162620.35, max 175229.95)"

|

MMCSD
=====

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.


MMC EXT4 FIO 1G
---------------

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62dxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62dxx_evm-fs: Write EXT4 CPU Load (%)","am62dxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62dxx_evm-fs: Read EXT4 CPU Load (%)"

    "1m","42.35 (min 41.60, max 43.10)","1.01 (min 0.92, max 1.14)","86.77 (min 85.10, max 88.30)","1.21 (min 1.05, max 1.29)"
    "4m","41.02 (min 40.10, max 41.60)","0.68 (min 0.63, max 0.73)","85.60 (min 82.40, max 87.30)","0.90 (min 0.81, max 0.96)"
    "4k","2.80 (min 2.77, max 2.81)","1.60 (min 1.51, max 1.69)","12.87 (min 12.50, max 13.10)","4.08 (min 4.02, max 4.16)"
    "256k","38.12 (min 37.30, max 39.00)","1.19 (min 1.11, max 1.32)","83.88 (min 83.10, max 84.50)","1.51 (min 1.47, max 1.56)"

MMC RAW FIO 1G
--------------

.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62dxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Write Raw CPU Load (%)","am62dxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Read Raw CPU Load (%)"

    "1m","43.22 (min 42.00, max 44.20)","0.90 (min 0.81, max 0.99)","88.23 (min 88.20, max 88.30)","1.12 (min 1.05, max 1.21)"
    "4m","42.80 (min 41.90, max 44.00)","0.69 (min 0.64, max 0.73)","88.17 (min 88.00, max 88.30)","0.86 (min 0.84, max 0.88)"
    "4k","2.81 (min 2.80, max 2.84)","1.34 (min 1.29, max 1.38)","13.03 (min 13.00, max 13.10)","3.76 (min 3.66, max 3.86)"
    "256k","37.75 (min 36.00, max 40.70)","1.00 (min 0.92, max 1.16)","84.40 (min 84.30, max 84.50)","1.48 (min 1.34, max 1.56)"

MMC EXT4
--------

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62dxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Write Raw CPU Load (%)","am62dxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Read Raw CPU Load (%)"

    "102400","10.78 (min 10.49, max 11.05)","0.52 (min 0.39, max 0.82)","11.05 (min 10.68, max 11.83)","0.47 (min 0.36, max 0.55)"
    "262144","10.83 (min 10.54, max 11.15)","0.47 (min 0.29, max 0.88)","11.12 (min 10.81, max 11.24)","0.57 (min 0.46, max 0.71)"
    "524288","10.79 (min 10.53, max 11.17)","0.41 (min 0.29, max 0.58)","11.23 (min 11.06, max 11.49)","0.48 (min 0.43, max 0.56)"
    "1048576","10.91 (min 10.51, max 11.31)","0.43 (min 0.29, max 0.65)","11.25 (min 10.84, max 12.03)","0.57 (min 0.42, max 0.75)"
    "5242880","11.00 (min 10.56, max 11.31)","0.44 (min 0.31, max 0.95)","12.03 (min 12.01, max 12.03)","0.59 (min 0.46, max 0.83)"

MMC EXT3
--------

.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62dxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Write Raw CPU Load (%)","am62dxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Read Raw CPU Load (%)"

    "102400","32.80 (min 27.05, max 38.59)","1.93 (min 1.26, max 3.96)","71.22 (min 68.05, max 75.78)","3.30 (min 2.73, max 4.56)"
    "262144","32.68 (min 28.51, max 34.70)","1.62 (min 0.99, max 3.46)","76.95 (min 75.21, max 78.70)","3.61 (min 2.77, max 4.36)"
    "524288","32.65 (min 27.95, max 38.16)","1.64 (min 0.92, max 4.53)","82.90 (min 82.35, max 83.83)","3.68 (min 3.39, max 3.94)"
    "1048576","34.47 (min 29.54, max 38.43)","1.62 (min 0.94, max 3.52)","82.57 (min 78.49, max 86.37)","3.35 (min 2.95, max 3.74)"
    "5242880","35.41 (min 30.54, max 40.36)","1.56 (min 0.88, max 3.46)","84.97 (min 79.58, max 86.36)","3.52 (min 3.42, max 3.70)"

MMC EXT2
--------

.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62dxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Write Raw CPU Load (%)","am62dxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Read Raw CPU Load (%)"

    "102400","15.97 (min 3.16, max 20.55)","1.70 (min 1.43, max 1.92)","72.65 (min 68.58, max 75.06)","3.50 (min 3.06, max 3.88)"
    "262144","25.96 (min 3.22, max 39.58)","1.85 (min 1.40, max 2.26)","79.21 (min 75.06, max 87.04)","3.09 (min 2.73, max 3.43)"
    "524288","29.08 (min 3.46, max 37.38)","1.73 (min 1.32, max 2.09)","83.16 (min 80.48, max 85.19)","3.18 (min 2.85, max 3.65)"
    "1048576","29.86 (min 3.53, max 38.71)","1.61 (min 1.08, max 2.81)","82.67 (min 79.79, max 85.87)","3.39 (min 2.65, max 3.71)"
    "5242880","30.19 (min 3.79, max 38.77)","1.38 (min 1.03, max 1.84)","83.81 (min 80.31, max 86.32)","3.24 (min 3.08, max 3.51)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62dxx_evm-fs: Write Throughput (Kbytes/sec)","am62dxx_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","36678.90 (min 33851.24, max 39384.62)","82198.64 (min 81920.00, max 83591.84)"
    "800000","40659.22 (min 32899.60, max 45010.99)","87308.41 (min 86231.58, max 88086.02)"
    "1000000","43129.36 (min 36328.16, max 46811.43)","89613.83 (min 89043.48, max 90021.98)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 
|

USB
===

USB Device Controller
---------------------

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62dxx_evm-fs: Throughput (MB/sec)"

    "150","31.76 (min 26.90, max 40.40)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62dxx_evm-fs: Throughput (MB/sec)"

    "150","27.41 (min 22.40, max 33.30)"

|

CRYPTO
======

OpenSSL Performance
-------------------

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62dxx_evm-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","24568.83"
    "aes-128-cbc","16","446.98"
    "aes-128-cbc","16384","87168.34"
    "aes-128-cbc","256","7377.41"
    "aes-128-cbc","64","1969.19"
    "aes-128-cbc","8192","73949.18"
    "aes-128-ecb","1024","24998.57"
    "aes-128-ecb","16","453.88"
    "aes-128-ecb","16384","89085.27"
    "aes-128-ecb","256","7518.29"
    "aes-128-ecb","64","2004.20"
    "aes-128-ecb","8192","75653.12"
    "aes-192-cbc","1024","23895.38"
    "aes-192-cbc","16","446.65"
    "aes-192-cbc","16384","78091.61"
    "aes-192-cbc","256","7297.54"
    "aes-192-cbc","64","1949.01"
    "aes-192-cbc","8192","67155.29"
    "aes-192-ecb","1024","24523.09"
    "aes-192-ecb","16","457.21"
    "aes-192-ecb","16384","80439.98"
    "aes-192-ecb","256","7495.51"
    "aes-192-ecb","64","2025.96"
    "aes-192-ecb","8192","69457.24"
    "aes-256-cbc","1024","23421.95"
    "aes-256-cbc","16","447.55"
    "aes-256-cbc","16384","71516.16"
    "aes-256-cbc","256","7258.20"
    "aes-256-cbc","64","1949.67"
    "aes-256-cbc","8192","61909.67"
    "aes-256-ecb","1024","24072.53"
    "aes-256-ecb","16","458.01"
    "aes-256-ecb","16384","73820.84"
    "aes-256-ecb","256","7437.40"
    "aes-256-ecb","64","2014.89"
    "aes-256-ecb","8192","64184.32"
    "sha256","1024","32333.82"
    "sha256","16","535.81"
    "sha256","16384","277938.18"
    "sha256","256","8409.69"
    "sha256","64","2122.37"
    "sha256","8192","183263.23"
    "sha512","1024","26990.25"
    "sha512","16","520.24"
    "sha512","16384","110586.54"
    "sha512","256","7864.32"
    "sha512","64","2082.37"
    "sha512","8192","91439.10"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62dxx_evm-fs: CPU Load"

    "aes-128-cbc","32.00"
    "aes-128-ecb","34.00"
    "aes-192-cbc","32.00"
    "aes-192-ecb","33.00"
    "aes-256-cbc","32.00"
    "aes-256-ecb","32.00"
    "sha256","95.00"
    "sha512","96.00"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

|

Low Power Performance
---------------------

Power Performance
^^^^^^^^^^^^^^^^^

.. csv-table:: I/O Only + DDR Power Performance
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","0.00"
   "vddr_core","0.85","0.00"
   "soc_dvdd_3v3","3.30","2.61"
   "soc_dvdd_1v8","1.80","1.80"
   "vdda_1v8","1.80","0.00"
   "vdd_lpddr4","1.10","0.01"
   "Total"," ","4.42"

.. csv-table:: Deep Sleep Power Performance
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","29.45"
   "vddr_core","0.85","2.82"
   "soc_dvdd_3v3","3.30","2.19"
   "soc_dvdd_1v8","1.80","5.39"
   "vdda_1v8","1.80","2.62"
   "vdd_lpddr4","1.10","0.00"
   "Total"," ","42.47"

.. csv-table:: MCU Only Power Performance
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","208.77"
   "vddr_core","0.85","4.05"
   "soc_dvdd_3v3","3.30","10.22"
   "soc_dvdd_1v8","1.80","3.89"
   "vdda_1v8","1.80","11.59"
   "vdd_lpddr4","1.10","0.00"
   "Total"," ","238.53"

Partial I/O Data
- All voltage rails were measured to be near 0V

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)
