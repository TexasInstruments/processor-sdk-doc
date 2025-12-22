
====================================
 Linux 11.02.08.02 Performance Guide
====================================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM62Dx EVM     | AM62Dx Evaluation Module rev E1 with ARM running at 1.4GHz, DDR data rate 3733 MT/S                            |
+----------------+----------------------------------------------------------------------------------------------------------------+

Table:  Evaluation Modules

.. rubric::  About This Manual
   :name: about-this-manual-kernel-perf-guide

This document provides performance data for each of the device drivers
which are part of the Processor SDK Linux package. This document should be
used in conjunction with release notes and user guides provided with the
Processor SDK Linux package for information on specific issues present
with drivers included in a particular release.

.. rubric::  If You Need Assistance
   :name: if-you-need-assistance-kernel-perf-guide

For further information or to report any problems, contact
https://e2e.ti.com/ or https://support.ti.com/

System Benchmarks
-----------------

LMBench
^^^^^^^
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

    "af_unix_sock_stream_latency (microsec)","30.12 (min 29.31, max 30.82)"
    "af_unix_socket_stream_bandwidth (mb\s)","1054.72 (min 1042.80, max 1065.78)"
    "bw_file_rd-io-1mb (mb/s)","1394.63 (min 1375.04, max 1403.65)"
    "bw_file_rd-o2c-1mb (mb/s)","749.43 (min 694.32, max 788.64)"
    "bw_mem-bcopy-16mb (mb/s)","1740.68 (min 1715.63, max 1750.16)"
    "bw_mem-bcopy-1mb (mb/s)","1863.03 (min 1842.75, max 1889.39)"
    "bw_mem-bcopy-2mb (mb/s)","1625.67 (min 1545.83, max 1692.05)"
    "bw_mem-bcopy-4mb (mb/s)","1647.32 (min 1548.79, max 1713.31)"
    "bw_mem-bcopy-8mb (mb/s)","1729.40 (min 1707.76, max 1746.34)"
    "bw_mem-bzero-16mb (mb/s)","7938.98 (min 7920.79, max 7952.29)"
    "bw_mem-bzero-1mb (mb/s)","4881.67 (min 1842.75, max 7925.07)"
    "bw_mem-bzero-2mb (mb/s)","4766.95 (min 1545.83, max 7952.29)"
    "bw_mem-bzero-4mb (mb/s)","4788.22 (min 1548.79, max 7945.11)"
    "bw_mem-bzero-8mb (mb/s)","4831.41 (min 1707.76, max 7947.02)"
    "bw_mem-cp-16mb (mb/s)","840.43 (min 834.03, max 852.65)"
    "bw_mem-cp-1mb (mb/s)","4506.74 (min 795.42, max 8218.15)"
    "bw_mem-cp-2mb (mb/s)","4415.13 (min 784.93, max 8064.52)"
    "bw_mem-cp-4mb (mb/s)","4431.16 (min 849.98, max 8001.45)"
    "bw_mem-cp-8mb (mb/s)","4434.57 (min 870.70, max 7984.03)"
    "bw_mem-fcp-16mb (mb/s)","1532.91 (min 1509.72, max 1557.94)"
    "bw_mem-fcp-1mb (mb/s)","4726.56 (min 1515.15, max 7925.07)"
    "bw_mem-fcp-2mb (mb/s)","4700.63 (min 1429.08, max 7952.29)"
    "bw_mem-fcp-4mb (mb/s)","4735.69 (min 1504.61, max 7945.11)"
    "bw_mem-fcp-8mb (mb/s)","4744.51 (min 1547.39, max 7947.02)"
    "bw_mem-frd-16mb (mb/s)","1887.64 (min 1876.61, max 1895.06)"
    "bw_mem-frd-1mb (mb/s)","1782.58 (min 1515.15, max 2047.08)"
    "bw_mem-frd-2mb (mb/s)","1605.52 (min 1429.08, max 1839.25)"
    "bw_mem-frd-4mb (mb/s)","1646.92 (min 1504.61, max 1855.86)"
    "bw_mem-frd-8mb (mb/s)","1665.51 (min 1547.39, max 1882.13)"
    "bw_mem-fwr-16mb (mb/s)","7962.52 (min 7943.07, max 7974.75)"
    "bw_mem-fwr-1mb (mb/s)","5099.94 (min 1932.20, max 8218.15)"
    "bw_mem-fwr-2mb (mb/s)","4869.22 (min 1611.08, max 8064.52)"
    "bw_mem-fwr-4mb (mb/s)","4872.60 (min 1653.58, max 8001.45)"
    "bw_mem-fwr-8mb (mb/s)","4875.39 (min 1660.27, max 7984.03)"
    "bw_mem-rd-16mb (mb/s)","1932.53 (min 1913.65, max 1942.22)"
    "bw_mem-rd-1mb (mb/s)","1725.48 (min 1225.28, max 2219.76)"
    "bw_mem-rd-2mb (mb/s)","1571.95 (min 1133.63, max 1943.32)"
    "bw_mem-rd-4mb (mb/s)","1665.97 (min 1365.65, max 1941.12)"
    "bw_mem-rd-8mb (mb/s)","1730.15 (min 1454.28, max 1948.61)"
    "bw_mem-rdwr-16mb (mb/s)","1672.28 (min 1600.32, max 1718.40)"
    "bw_mem-rdwr-1mb (mb/s)","1037.11 (min 795.42, max 1297.02)"
    "bw_mem-rdwr-2mb (mb/s)","986.71 (min 784.93, max 1238.39)"
    "bw_mem-rdwr-4mb (mb/s)","1135.79 (min 849.98, max 1446.39)"
    "bw_mem-rdwr-8mb (mb/s)","1211.02 (min 870.70, max 1599.04)"
    "bw_mem-wr-16mb (mb/s)","1619.91 (min 1548.29, max 1668.40)"
    "bw_mem-wr-1mb (mb/s)","1255.05 (min 1206.06, max 1308.90)"
    "bw_mem-wr-2mb (mb/s)","1195.30 (min 1057.64, max 1289.08)"
    "bw_mem-wr-4mb (mb/s)","1403.98 (min 1295.97, max 1454.55)"
    "bw_mem-wr-8mb (mb/s)","1525.80 (min 1389.37, max 1599.04)"
    "bw_mmap_rd-mo-1mb (mb/s)","2117.81 (min 2081.76, max 2139.04)"
    "bw_mmap_rd-o2c-1mb (mb/s)","750.19 (min 693.72, max 794.91)"
    "bw_pipe (mb/s)","702.59 (min 692.16, max 713.48)"
    "bw_unix (mb/s)","1054.72 (min 1042.80, max 1065.78)"
    "lat_connect (us)","57.00 (min 56.61, max 57.41)"
    "lat_ctx-2-128k (us)","7.85 (min 7.55, max 8.11)"
    "lat_ctx-2-256k (us)","7.33 (min 6.40, max 8.28)"
    "lat_ctx-4-128k (us)","7.44 (min 7.06, max 7.89)"
    "lat_ctx-4-256k (us)","7.12 (min 5.25, max 8.97)"
    "lat_fs-0k (num_files)","234.50 (min 215.00, max 251.00)"
    "lat_fs-10k (num_files)","113.25 (min 104.00, max 122.00)"
    "lat_fs-1k (num_files)","163.75 (min 144.00, max 178.00)"
    "lat_fs-4k (num_files)","159.75 (min 144.00, max 174.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","31.04 (min 30.78, max 31.41)"
    "lat_mem_rd-stride128-sz125k (ns)","5.56 (min 5.53, max 5.61)"
    "lat_mem_rd-stride128-sz250k (ns)","5.90 (min 5.83, max 6.36)"
    "lat_mem_rd-stride128-sz31k (ns)","3.67 (min 2.16, max 4.19)"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","11.25 (min 9.86, max 13.27)"
    "lat_mem_rd-stride128-sz62k (ns)","5.15 (min 4.51, max 5.27)"
    "lat_mmap-1m (us)","55.75 (min 51.00, max 58.00)"
    "lat_ops-double-add (ns)","2.86"
    "lat_ops-double-div (ns)","15.75 (min 15.74, max 15.76)"
    "lat_ops-double-mul (ns)","2.86"
    "lat_ops-float-add (ns)","2.86"
    "lat_ops-float-div (ns)","9.30 (min 9.30, max 9.31)"
    "lat_ops-float-mul (ns)","2.86"
    "lat_ops-int-add (ns)","0.72"
    "lat_ops-int-bit (ns)","0.48"
    "lat_ops-int-div (ns)","4.29"
    "lat_ops-int-mod (ns)","4.53 (min 4.53, max 4.54)"
    "lat_ops-int-mul (ns)","3.08 (min 3.07, max 3.09)"
    "lat_ops-int64-add (ns)","0.72"
    "lat_ops-int64-bit (ns)","0.48"
    "lat_ops-int64-div (ns)","6.80"
    "lat_ops-int64-mod (ns)","5.25 (min 5.25, max 5.26)"
    "lat_ops-int64-mul (ns)","3.55"
    "lat_pagefault (us)","0.65 (min 0.51, max 1.06)"
    "lat_pipe (us)","25.70 (min 25.35, max 26.22)"
    "lat_proc-exec (us)","712.79 (min 689.13, max 735.50)"
    "lat_proc-fork (us)","624.24 (min 601.00, max 643.00)"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","34.08 (min 33.89, max 34.33)"
    "lat_sem (us)","2.99 (min 2.61, max 3.63)"
    "lat_sig-catch (us)","5.51 (min 5.27, max 5.71)"
    "lat_sig-install (us)","0.67 (min 0.64, max 0.70)"
    "lat_sig-prot (us)","0.64 (min 0.46, max 0.80)"
    "lat_syscall-fstat (us)","1.98 (min 1.90, max 2.07)"
    "lat_syscall-null (us)","0.46 (min 0.46, max 0.50)"
    "lat_syscall-open (us)","166.27 (min 150.75, max 200.85)"
    "lat_syscall-read (us)","0.82 (min 0.80, max 0.88)"
    "lat_syscall-stat (us)","4.79 (min 4.64, max 4.97)"
    "lat_syscall-write (us)","0.78 (min 0.75, max 0.83)"
    "lat_tcp (us)","0.92 (min 0.91, max 0.97)"
    "lat_unix (us)","30.12 (min 29.31, max 30.82)"
    "latency_for_0.50_mb_block_size (nanosec)","11.25 (min 9.86, max 13.27)"
    "latency_for_1.00_mb_block_size (nanosec)","15.52 (min 0.00, max 31.41)"
    "pipe_bandwidth (mb\s)","702.59 (min 692.16, max 713.48)"
    "pipe_latency (microsec)","25.70 (min 25.35, max 26.22)"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","34.08 (min 33.89, max 34.33)"
    "semaphore_latency (microsec)","2.99 (min 2.61, max 3.63)"
    "signal_handler_latency (microsec)","0.67 (min 0.64, max 0.70)"
    "signal_handler_overhead (microsec)","5.51 (min 5.27, max 5.71)"
    "tcp_ip_connection_cost_to_localhost (microsec)","57.00 (min 56.61, max 57.41)"
    "tcp_latency_using_localhost (microsec)","0.92 (min 0.91, max 0.97)"

Dhrystone
^^^^^^^^^
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
    "dhrystone_per_mhz (dmips/mhz)","2.90"
    "dhrystone_per_second (dhrystonep)","7142857.00"

Whetstone
^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62dxx_evm-fs: perf"

    "whetstone (mips)","7500.00 (min 5000.00, max 10000.00)"

Linpack
^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62dxx_evm-fs: perf"

    "linpack (kflops)","576688.25 (min 574136.00, max 578099.00)"

Stream
^^^^^^
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

    "add (mb/s)","2565.85 (min 2558.60, max 2572.00)"
    "copy (mb/s)","3569.39 (min 3553.00, max 3582.00)"
    "scale (mb/s)","3338.13 (min 3282.60, max 3379.00)"
    "triad (mb/s)","2385.28 (min 2379.40, max 2389.10)"

CoreMarkPro
^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62dxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","42.00 (min 41.84, max 42.19)"
    "core (workloads/)","0.30"
    "coremark-pro ()","923.79 (min 903.66, max 936.49)"
    "linear_alg-mid-100x100-sp (workloads/)","14.68 (min 14.67, max 14.69)"
    "loops-all-mid-10k-sp (workloads/)","0.71"
    "nnet_test (workloads/)","1.09 (min 1.08, max 1.09)"
    "parser-125k (workloads/)","8.78 (min 8.70, max 8.85)"
    "radix2-big-64k (workloads/)","61.55 (min 51.68, max 69.15)"
    "sha-test (workloads/)","81.30 (min 80.65, max 81.97)"
    "zip-test (workloads/)","22.16 (min 21.74, max 22.22)"

.. csv-table:: CoreMarkProFourCore Benchmarks
    :header: "Benchmarks","am62dxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","160.97 (min 158.73, max 161.29)"
    "core (workloads/)","1.20"
    "coremark-pro ()","2540.92 (min 2504.79, max 2570.41)"
    "linear_alg-mid-100x100-sp (workloads/)","56.35 (min 56.31, max 56.37)"
    "loops-all-mid-10k-sp (workloads/)","2.07 (min 2.03, max 2.12)"
    "nnet_test (workloads/)","3.62"
    "parser-125k (workloads/)","9.29 (min 8.89, max 9.93)"
    "radix2-big-64k (workloads/)","81.13 (min 79.71, max 82.65)"
    "sha-test (workloads/)","269.38 (min 263.16, max 270.27)"
    "zip-test (workloads/)","75.50 (min 72.73, max 76.92)"

MultiBench
^^^^^^^^^^
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

    "4m-check (workloads/)","417.14 (min 415.49, max 418.62)"
    "4m-check-reassembly (workloads/)","113.35 (min 111.86, max 115.08)"
    "4m-check-reassembly-tcp (workloads/)","58.41 (min 58.14, max 58.69)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","33.11 (min 32.89, max 33.33)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.89 (min 1.87, max 1.91)"
    "4m-cmykw2 (workloads/)","240.20 (min 227.02, max 246.61)"
    "4m-cmykw2-rotatew2 (workloads/)","49.45 (min 49.14, max 49.75)"
    "4m-reassembly (workloads/)","79.96 (min 78.86, max 80.97)"
    "4m-rotatew2 (workloads/)","52.44 (min 51.84, max 52.83)"
    "4m-tcp-mixed (workloads/)","119.07 (min 118.52, max 120.30)"
    "4m-x264w2 (workloads/)","1.97 (min 1.94, max 2.00)"
    "idct-4m (workloads/)","19.16 (min 19.14, max 19.20)"
    "idct-4mw1 (workloads/)","19.17 (min 19.15, max 19.21)"
    "ippktcheck-4m (workloads/)","414.97 (min 413.43, max 417.08)"
    "ippktcheck-4mw1 (workloads/)","416.58 (min 413.22, max 418.76)"
    "ipres-4m (workloads/)","108.42 (min 107.30, max 109.49)"
    "ipres-4mw1 (workloads/)","107.73 (min 106.84, max 109.09)"
    "md5-4m (workloads/)","27.55 (min 27.30, max 27.87)"
    "md5-4mw1 (workloads/)","27.59 (min 27.32, max 27.78)"
    "rgbcmyk-4m (workloads/)","63.65 (min 63.57, max 63.78)"
    "rgbcmyk-4mw1 (workloads/)","63.67 (min 63.41, max 63.88)"
    "rotate-4ms1 (workloads/)","23.44 (min 23.33, max 23.55)"
    "rotate-4ms1w1 (workloads/)","23.47 (min 23.28, max 23.84)"
    "rotate-4ms64 (workloads/)","23.71 (min 23.61, max 23.79)"
    "rotate-4ms64w1 (workloads/)","23.70 (min 23.57, max 23.76)"
    "x264-4mq (workloads/)","0.58"
    "x264-4mqw1 (workloads/)","0.58"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62dxx_evm-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","14.31 (min 12.88, max 20.51)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

Ethernet
-----------------
Ethernet performance benchmarks were measured using Netperf 2.7.1 https://hewlettpackard.github.io/netperf/doc/netperf.html
Test procedures were modeled after those defined in RFC-2544:
https://tools.ietf.org/html/rfc2544, where the DUT is the TI device
and the "tester" used was a Linux PC. To produce consistent results,
it is recommended to carry out performance tests in a private network and to avoid
running NFS on the same interface used in the test. In these results,
CPU utilization was captured as the total percentage used across all cores on the device,
while running the performance test over one external interface.

UDP Throughput (0% loss) was measured by the procedure defined in RFC-2544 section 26.1: Throughput.
In this scenario, netperf options burst_size (-b) and wait_time (-w) are used to limit bandwidth
during different trials of the test, with the goal of finding the highest rate at which
no loss is seen. For example, to limit bandwidth to 500Mbits/sec with 1472B datagram:

::

   burst_size = <bandwidth (bits/sec)> / 8 (bits -> bytes) / <UDP datagram size> / 100 (seconds -> 10 ms)
   burst_size = 500000000 / 8 / 1472 / 100 = 425

   wait_time = 10 milliseconds (minimum supported by Linux PC used for testing)

UDP Throughput (possible loss) was measured by capturing throughput and packet loss statistics when
running the netperf test with no bandwidth limit (remove -b/-w options).

In order to start a netperf client on one device, the other device must have netserver running.
To start netserver:

::

   netserver [-p <port_number>] [-4 (IPv4 addressing)] [-6 (IPv6 addressing)]

Running the following shell script from the DUT will trigger netperf clients to measure
bidirectional TCP performance for 60 seconds and report CPU utilization. Parameter -k is used in
client commands to summarize selected statistics on their own line and -j is used to gain
additional timing measurements during the test.

::

   #!/bin/bash
   for i in 1
   do
      netperf -H <tester ip> -j -c -l 60 -t TCP_STREAM --
         -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE &

      netperf -H <tester ip> -j -c -l 60 -t TCP_MAERTS --
         -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE &
   done

Running the following commands will trigger netperf clients to measure UDP burst performance for
60 seconds at various burst/datagram sizes and report CPU utilization.

- For UDP egress tests, run netperf client from DUT and start netserver on tester.

::

   netperf -H <tester ip> -j -c -l 60 -t UDP_STREAM -b <burst_size> -w <wait_time> -- -m <UDP datagram size> 
      -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE 

- For UDP ingress tests, run netperf client from tester and start netserver on DUT. 

::

   netperf -H <DUT ip> -j -C -l 60 -t UDP_STREAM -b <burst_size> -w <wait_time> -- -m <UDP datagram size>
      -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE


CPSW/CPSW2g/CPSW3g Ethernet Driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- CPSW2g: AM65x, J7200, J721e, J721S2, J784S4, J742S2
- CPSW3g: AM64x, AM62x, AM62ax, AM62px, AM62dx


.. rubric::  TCP Bidirectional Throughput 
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62dxx_evm-fs: THROUGHPUT (Mbits/sec)","am62dxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","304.93 (min 301.56, max 307.77)","11.34 (min 11.00, max 11.84)"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62dxx_evm-fs: THROUGHPUT (Mbits/sec)","am62dxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","305.08 (min 301.65, max 308.15)","11.48 (min 11.33, max 11.63)"

.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62dxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62dxx_evm-fs: THROUGHPUT (Mbits/sec)","am62dxx_evm-fs: Packets Per Second (kPPS)","am62dxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","57.87 (min 55.77, max 59.88)","113.00 (min 109.00, max 117.00)","25.67 (min 25.08, max 26.03)"
    "128","82.00","113.83 (min 109.02, max 116.77)","111.13 (min 106.00, max 114.00)","25.77 (min 25.07, max 26.02)"
    "256","210.00","148.42 (min 63.90, max 160.50)","72.13 (min 31.00, max 78.00)","19.34 (min 6.07, max 21.69)"
    "1024","978.00","181.49 (min 181.48, max 181.50)","22.00","7.98 (min 7.88, max 8.14)"
    "1518","1472.00","179.37 (min 179.36, max 179.37)","15.00","7.84 (min 7.65, max 7.99)"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62dxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62dxx_evm-fs: THROUGHPUT (Mbits/sec)","am62dxx_evm-fs: Packets Per Second (kPPS)","am62dxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","1.86 (min 1.48, max 2.36)","3.63 (min 3.00, max 5.00)","1.53 (min 0.53, max 3.81)"
    "128","82.00","4.47 (min 4.40, max 4.71)","4.13 (min 4.00, max 5.00)","1.02 (min 0.76, max 1.65)"
    "256","210.00","10.41 (min 10.03, max 10.85)","5.00","2.42 (min 0.94, max 5.27)"
    "1024","978.00","43.19 (min 42.60, max 44.24)","5.00","2.08 (min 1.31, max 4.18)"
    "1518","1472.00","62.15 (min 61.23, max 64.77)","5.11 (min 5.00, max 6.00)","2.90 (min 1.80, max 4.28)"

.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62dxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62dxx_evm-fs: THROUGHPUT (Mbits/sec)","am62dxx_evm-fs: Packets Per Second (kPPS)","am62dxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","am62dxx_evm-fs: Packet Loss %"

    "64","18.00","82.68 (min 69.85, max 95.35)","161.50 (min 136.00, max 186.00)","40.23 (min 38.26, max 42.06)","31.04 (min 0.18, max 62.30)"
    "128","82.00","174.59 (min 130.93, max 188.67)","170.50 (min 128.00, max 184.00)","41.26 (min 39.46, max 42.34)","44.65 (min 0.39, max 61.31)"
    "256","210.00","320.34 (min 259.61, max 369.04)","156.50 (min 127.00, max 180.00)","40.94 (min 38.60, max 42.78)","24.24 (min 0.37, max 49.24)"
    "1024","978.00","876.98 (min 837.06, max 913.30)","106.86 (min 102.00, max 111.00)","40.28 (min 39.04, max 41.61)","0.61 (min 0.18, max 1.17)"
    "1518","1472.00","892.63 (min 786.50, max 934.06)","75.78 (min 67.00, max 79.00)","38.92 (min 34.39, max 40.76)","1.04 (min 0.25, max 2.13)"

|

Linux OSPI Flash Driver
-----------------------

RAW

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62dxx_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "10","227.27"
    "50","217.39"

|

USB Driver
----------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62dxx_evm-fs: Throughput (MB/sec)"

    "150","31.79 (min 20.00, max 34.80)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62dxx_evm-fs: Throughput (MB/sec)"

    "150","30.64 (min 24.70, max 32.80)"

|

CRYPTO Driver
-------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62dxx_evm-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","23511.81 (min 22199.30, max 24003.58)"
    "aes-128-cbc","16","424.58 (min 400.86, max 435.84)"
    "aes-128-cbc","16384","85633.71 (min 84454.06, max 86250.84)"
    "aes-128-cbc","256","7031.72 (min 6708.74, max 7234.22)"
    "aes-128-cbc","64","1847.05 (min 1762.45, max 1904.09)"
    "aes-128-cbc","8192","72108.37 (min 70328.32, max 72742.23)"
    "aes-128-ecb","1024","24118.53 (min 23312.38, max 24716.29)"
    "aes-128-ecb","16","436.57 (min 412.31, max 446.68)"
    "aes-128-ecb","16384","88354.13 (min 87086.42, max 89161.73)"
    "aes-128-ecb","256","7186.42 (min 6870.70, max 7333.55)"
    "aes-128-ecb","64","1899.44 (min 1787.95, max 1948.69)"
    "aes-128-ecb","8192","74231.47 (min 72373.59, max 74986.84)"
    "aes-192-cbc","1024","23054.25 (min 21801.64, max 23675.90)"
    "aes-192-cbc","16","426.41 (min 403.57, max 437.48)"
    "aes-192-cbc","16384","77032.11 (min 75956.22, max 77736.62)"
    "aes-192-cbc","256","6940.00 (min 6559.74, max 7117.23)"
    "aes-192-cbc","64","1855.78 (min 1761.34, max 1896.92)"
    "aes-192-cbc","8192","66243.58 (min 64476.50, max 67100.67)"
    "aes-192-ecb","1024","23512.23 (min 22242.65, max 24032.94)"
    "aes-192-ecb","16","435.23 (min 416.22, max 443.56)"
    "aes-192-ecb","16384","79489.02 (min 77490.86, max 80303.45)"
    "aes-192-ecb","256","7143.25 (min 6823.34, max 7303.17)"
    "aes-192-ecb","64","1892.40 (min 1786.77, max 1936.68)"
    "aes-192-ecb","8192","67959.13 (min 66158.59, max 68741.80)"
    "aes-256-cbc","1024","22439.42 (min 21377.71, max 22966.27)"
    "aes-256-cbc","16","427.52 (min 403.20, max 438.70)"
    "aes-256-cbc","16384","70787.07 (min 69331.63, max 71254.02)"
    "aes-256-cbc","256","6881.53 (min 6456.32, max 7109.89)"
    "aes-256-cbc","64","1843.97 (min 1729.77, max 1889.94)"
    "aes-256-cbc","8192","61376.17 (min 59588.61, max 62046.21)"
    "aes-256-ecb","1024","23099.73 (min 22211.93, max 23634.60)"
    "aes-256-ecb","16","435.45 (min 415.85, max 443.94)"
    "aes-256-ecb","16384","72642.56 (min 71390.55, max 73176.41)"
    "aes-256-ecb","256","7103.46 (min 6742.61, max 7271.85)"
    "aes-256-ecb","64","1893.37 (min 1771.86, max 1932.05)"
    "aes-256-ecb","8192","62965.42 (min 61532.84, max 63539.88)"
    "sha256","1024","38004.99 (min 37393.07, max 38651.90)"
    "sha256","16","632.01 (min 623.18, max 639.92)"
    "sha256","16384","300601.34 (min 296621.40, max 303781.21)"
    "sha256","256","9924.28 (min 9777.24, max 10089.73)"
    "sha256","64","2500.19 (min 2459.39, max 2530.41)"
    "sha256","8192","203442.52 (min 201657.00, max 204671.66)"
    "sha512","1024","26159.23 (min 25836.20, max 26417.49)"
    "sha512","16","614.39 (min 601.95, max 625.40)"
    "sha512","16384","68399.79 (min 68119.21, max 68577.96)"
    "sha512","256","8720.94 (min 8533.85, max 8851.97)"
    "sha512","64","2456.83 (min 2404.99, max 2503.42)"
    "sha512","8192","61606.57 (min 61311.66, max 61794.99)"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62dxx_evm-fs: CPU Load"

    "aes-128-cbc","31.50 (min 30.00, max 32.00)"
    "aes-128-ecb","32.75 (min 31.00, max 34.00)"
    "aes-192-cbc","31.50 (min 30.00, max 32.00)"
    "aes-192-ecb","32.13 (min 30.00, max 33.00)"
    "aes-256-cbc","31.00 (min 29.00, max 32.00)"
    "aes-256-ecb","31.63 (min 30.00, max 33.00)"
    "sha256","95.50 (min 94.00, max 96.00)"
    "sha512","95.63 (min 95.00, max 96.00)"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc
