
======================================
 Linux 11.02.01 Performance Guide
======================================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
| J722S EVM      | J722S Evaluation Module rev E1 with ARM running at 1.4GHz, DDR data rate 3200 MT/S                             |
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
-------------------


LMBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
LMBench is a collection of microbenchmarks of which the memory bandwidth 
and latency related ones are typically used to estimate processor 
memory system performance. More information about lmbench at
https://lmbench.sourceforge.net/whatis_lmbench.html and
https://lmbench.sourceforge.net/man/lmbench.8.html

**Latency**: :command:`lat_mem_rd-stride128-szN`, where N is equal to or smaller than the cache
size at given level measures the cache miss penalty. N that is at least
double the size of last level cache is the latency to external memory.

**Bandwidth**: :command:`bw_mem_bcopy-N`, where N is equal to or smaller than the cache size at
a given level measures the achievable memory bandwidth from software doing
a memcpy() type operation. Typical use is for external memory bandwidth
calculation. The bandwidth is calculated as byte read and written counts
as 1 which should be roughly half of STREAM copy result.

Execute the LMBench with the following:

.. code-block:: console

    cd /opt/ltp
    ./runltp -P j721e-idk-gw -f ddt/lmbench -s LMBENCH_L_PERF_0001

.. csv-table:: LMBench Benchmarks
    :header: "Benchmarks","j722s_evm-fs: perf"

    "af_unix_sock_stream_latency (microsec)","30.22 (min 29.18, max 31.07)"
    "af_unix_socket_stream_bandwidth (mb\s)","1080.92 (min 1053.08, max 1122.04)"
    "bw_file_rd-io-1mb (mb/s)","1356.31 (min 1303.36, max 1414.93)"
    "bw_file_rd-o2c-1mb (mb/s)","741.25 (min 668.11, max 794.91)"
    "bw_mem-bcopy-16mb (mb/s)","1748.23 (min 1587.93, max 1876.17)"
    "bw_mem-bcopy-1mb (mb/s)","1919.28 (min 1835.24, max 2010.45)"
    "bw_mem-bcopy-2mb (mb/s)","1654.71 (min 1592.99, max 1794.04)"
    "bw_mem-bcopy-4mb (mb/s)","1661.58 (min 1475.47, max 1811.87)"
    "bw_mem-bcopy-8mb (mb/s)","1733.80 (min 1599.04, max 1854.86)"
    "bw_mem-bzero-16mb (mb/s)","7222.88 (min 7142.86, max 7323.77)"
    "bw_mem-bzero-1mb (mb/s)","4566.11 (min 1835.24, max 7329.45)"
    "bw_mem-bzero-2mb (mb/s)","4433.81 (min 1592.99, max 7318.35)"
    "bw_mem-bzero-4mb (mb/s)","4438.00 (min 1475.47, max 7319.91)"
    "bw_mem-bzero-8mb (mb/s)","4476.23 (min 1599.04, max 7326.01)"
    "bw_mem-cp-16mb (mb/s)","879.12 (min 847.46, max 917.22)"
    "bw_mem-cp-1mb (mb/s)","4201.30 (min 833.75, max 7639.57)"
    "bw_mem-cp-2mb (mb/s)","4108.07 (min 818.55, max 7477.30)"
    "bw_mem-cp-4mb (mb/s)","4092.93 (min 850.07, max 7399.93)"
    "bw_mem-cp-8mb (mb/s)","4091.36 (min 870.61, max 7363.77)"
    "bw_mem-fcp-16mb (mb/s)","1642.72 (min 1479.43, max 1748.44)"
    "bw_mem-fcp-1mb (mb/s)","4435.38 (min 1587.02, max 7329.45)"
    "bw_mem-fcp-2mb (mb/s)","4382.84 (min 1448.44, max 7318.35)"
    "bw_mem-fcp-4mb (mb/s)","4417.33 (min 1542.22, max 7319.91)"
    "bw_mem-fcp-8mb (mb/s)","4425.14 (min 1587.30, max 7326.01)"
    "bw_mem-frd-16mb (mb/s)","1823.32 (min 1743.68, max 1917.78)"
    "bw_mem-frd-1mb (mb/s)","1788.13 (min 1587.02, max 2036.28)"
    "bw_mem-frd-2mb (mb/s)","1610.91 (min 1448.44, max 1900.78)"
    "bw_mem-frd-4mb (mb/s)","1655.15 (min 1517.64, max 1913.27)"
    "bw_mem-frd-8mb (mb/s)","1691.26 (min 1571.86, max 1919.16)"
    "bw_mem-fwr-16mb (mb/s)","7245.95 (min 7172.74, max 7346.19)"
    "bw_mem-fwr-1mb (mb/s)","4712.43 (min 1781.58, max 7639.57)"
    "bw_mem-fwr-2mb (mb/s)","4513.41 (min 1544.88, max 7477.30)"
    "bw_mem-fwr-4mb (mb/s)","4489.27 (min 1517.64, max 7399.93)"
    "bw_mem-fwr-8mb (mb/s)","4504.66 (min 1571.86, max 7363.77)"
    "bw_mem-rd-16mb (mb/s)","1859.13 (min 1787.91, max 1959.10)"
    "bw_mem-rd-1mb (mb/s)","1898.03 (min 1569.86, max 2246.35)"
    "bw_mem-rd-2mb (mb/s)","1687.52 (min 1395.67, max 1955.99)"
    "bw_mem-rd-4mb (mb/s)","1742.52 (min 1550.59, max 1930.19)"
    "bw_mem-rd-8mb (mb/s)","1787.08 (min 1585.41, max 1951.70)"
    "bw_mem-rdwr-16mb (mb/s)","1769.85 (min 1708.31, max 1887.01)"
    "bw_mem-rdwr-1mb (mb/s)","1273.75 (min 833.75, max 1827.15)"
    "bw_mem-rdwr-2mb (mb/s)","1159.06 (min 818.55, max 1595.15)"
    "bw_mem-rdwr-4mb (mb/s)","1252.15 (min 850.07, max 1718.71)"
    "bw_mem-rdwr-8mb (mb/s)","1323.01 (min 870.61, max 1856.79)"
    "bw_mem-wr-16mb (mb/s)","1762.77 (min 1687.41, max 1856.15)"
    "bw_mem-wr-1mb (mb/s)","1663.97 (min 1515.92, max 1827.15)"
    "bw_mem-wr-2mb (mb/s)","1492.93 (min 1370.10, max 1671.68)"
    "bw_mem-wr-4mb (mb/s)","1626.08 (min 1527.69, max 1768.35)"
    "bw_mem-wr-8mb (mb/s)","1723.04 (min 1585.41, max 1856.79)"
    "bw_mmap_rd-mo-1mb (mb/s)","2044.06 (min 1962.18, max 2150.15)"
    "bw_mmap_rd-o2c-1mb (mb/s)","738.25 (min 658.65, max 794.91)"
    "bw_pipe (mb/s)","769.14 (min 723.11, max 811.97)"
    "bw_unix (mb/s)","1080.92 (min 1053.08, max 1122.04)"
    "lat_connect (us)","56.95 (min 56.32, max 57.46)"
    "lat_ctx-2-128k (us)","8.03 (min 7.64, max 8.67)"
    "lat_ctx-2-256k (us)","9.12 (min 6.69, max 14.05)"
    "lat_ctx-4-128k (us)","7.73 (min 6.99, max 8.68)"
    "lat_ctx-4-256k (us)","7.11 (min 4.17, max 9.58)"
    "lat_fs-0k (num_files)","236.23 (min 216.00, max 266.00)"
    "lat_fs-10k (num_files)","115.08 (min 107.00, max 123.00)"
    "lat_fs-1k (num_files)","163.31 (min 144.00, max 177.00)"
    "lat_fs-4k (num_files)","155.15 (min 138.00, max 174.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","32.36 (min 30.61, max 33.53)"
    "lat_mem_rd-stride128-sz125k (ns)","5.56 (min 5.53, max 5.59)"
    "lat_mem_rd-stride128-sz250k (ns)","5.84 (min 5.83, max 5.85)"
    "lat_mem_rd-stride128-sz31k (ns)","3.74 (min 2.16, max 4.20)"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","11.92 (min 9.83, max 15.73)"
    "lat_mem_rd-stride128-sz62k (ns)","5.18 (min 4.52, max 5.28)"
    "lat_mmap-1m (us)","54.62 (min 50.00, max 58.00)"
    "lat_ops-double-add (ns)","2.86"
    "lat_ops-double-div (ns)","15.74 (min 15.74, max 15.75)"
    "lat_ops-double-mul (ns)","2.86"
    "lat_ops-float-add (ns)","2.86"
    "lat_ops-float-div (ns)","9.30 (min 9.30, max 9.31)"
    "lat_ops-float-mul (ns)","2.86"
    "lat_ops-int-add (ns)","0.72"
    "lat_ops-int-bit (ns)","0.48"
    "lat_ops-int-div (ns)","4.29 (min 4.29, max 4.30)"
    "lat_ops-int-mod (ns)","4.53 (min 4.53, max 4.54)"
    "lat_ops-int-mul (ns)","3.08 (min 3.07, max 3.09)"
    "lat_ops-int64-add (ns)","0.72"
    "lat_ops-int64-bit (ns)","0.48"
    "lat_ops-int64-div (ns)","6.80 (min 6.79, max 6.80)"
    "lat_ops-int64-mod (ns)","5.25 (min 5.24, max 5.25)"
    "lat_ops-int64-mul (ns)","3.55 (min 3.55, max 3.57)"
    "lat_pagefault (us)","0.66 (min 0.52, max 1.11)"
    "lat_pipe (us)","25.86 (min 25.14, max 26.41)"
    "lat_proc-exec (us)","737.29 (min 697.63, max 780.00)"
    "lat_proc-fork (us)","647.08 (min 619.44, max 682.75)"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","34.01 (min 32.98, max 34.35)"
    "lat_sem (us)","3.03 (min 2.48, max 3.95)"
    "lat_sig-catch (us)","5.59 (min 5.25, max 5.73)"
    "lat_sig-install (us)","0.67 (min 0.64, max 0.70)"
    "lat_sig-prot (us)","0.70 (min 0.55, max 1.38)"
    "lat_syscall-fstat (us)","2.01 (min 1.90, max 2.07)"
    "lat_syscall-null (us)","0.46 (min 0.46, max 0.50)"
    "lat_syscall-open (us)","165.38 (min 148.50, max 199.96)"
    "lat_syscall-read (us)","0.82 (min 0.80, max 0.89)"
    "lat_syscall-stat (us)","4.86 (min 4.63, max 5.05)"
    "lat_syscall-write (us)","0.77 (min 0.75, max 0.84)"
    "lat_tcp (us)","0.92 (min 0.91, max 0.97)"
    "lat_unix (us)","30.22 (min 29.18, max 31.07)"
    "latency_for_0.50_mb_block_size (nanosec)","11.92 (min 9.83, max 15.73)"
    "latency_for_1.00_mb_block_size (nanosec)","16.18 (min 0.00, max 33.53)"
    "pipe_bandwidth (mb\s)","769.14 (min 723.11, max 811.97)"
    "pipe_latency (microsec)","25.86 (min 25.14, max 26.41)"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","34.01 (min 32.98, max 34.35)"
    "semaphore_latency (microsec)","3.03 (min 2.48, max 3.95)"
    "signal_handler_latency (microsec)","0.67 (min 0.64, max 0.70)"
    "signal_handler_overhead (microsec)","5.59 (min 5.25, max 5.73)"
    "tcp_ip_connection_cost_to_localhost (microsec)","56.95 (min 56.32, max 57.46)"
    "tcp_latency_using_localhost (microsec)","0.92 (min 0.91, max 0.97)"




Dhrystone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed.

Please take note, different run may produce different slightly results.
This is advised to run this test multiple times in order to get maximum 
performance numbers.


Execute the benchmark with the following:

.. code-block:: console

    runDhrystone

.. csv-table:: Dhrystone Benchmarks
    :header: "Benchmarks","j722s_evm-fs: perf"

    "cpu_clock (mhz)","1400.00"
    "dhrystone_per_mhz (dmips/mhz)","2.91 (min 2.90, max 3.00)"
    "dhrystone_per_second (dhrystonep)","7163207.04 (min 7142857.00, max 7407407.50)"




Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

.. code-block:: console

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","j722s_evm-fs: perf"

    "whetstone (mips)","7692.31 (min 5000.00, max 10000.00)"




Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","j722s_evm-fs: perf"

    "linpack (kflops)","575941.54 (min 573034.00, max 578392.00)"




NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","j722s_evm-fs: perf"

    "assignment (iterations)","14.48 (min 14.42, max 14.52)"
    "fourier (iterations)","22709.38 (min 22050.00, max 22831.00)"
    "fp_emulation (iterations)","215.64 (min 215.62, max 215.65)"
    "huffman (iterations)","1184.02 (min 1183.30, max 1184.30)"
    "idea (iterations)","3444.75 (min 3444.60, max 3444.90)"
    "lu_decomposition (iterations)","529.67 (min 527.92, max 531.90)"
    "neural_net (iterations)","8.65 (min 8.65, max 8.66)"
    "numeric_sort (iterations)","625.57 (min 616.42, max 629.11)"
    "string_sort (iterations)","163.94 (min 163.93, max 163.94)"




Stream
^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

.. code-block:: console

    stream_c

.. csv-table:: Stream Benchmarks
    :header: "Benchmarks","j722s_evm-fs: perf"

    "add (mb/s)","2475.39 (min 2403.10, max 2620.50)"
    "copy (mb/s)","3600.07 (min 3509.50, max 3818.80)"
    "scale (mb/s)","3287.07 (min 3167.90, max 3474.80)"
    "triad (mb/s)","2266.46 (min 2216.30, max 2373.80)"




CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","j722s_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","41.96 (min 41.67, max 42.02)"
    "core (workloads/)","0.30"
    "coremark-pro ()","923.13 (min 896.57, max 945.42)"
    "linear_alg-mid-100x100-sp (workloads/)","14.68 (min 14.67, max 14.70)"
    "loops-all-mid-10k-sp (workloads/)","0.71 (min 0.70, max 0.71)"
    "nnet_test (workloads/)","1.09 (min 1.08, max 1.09)"
    "parser-125k (workloads/)","8.73 (min 8.62, max 8.77)"
    "radix2-big-64k (workloads/)","62.58 (min 47.42, max 74.70)"
    "sha-test (workloads/)","81.30 (min 80.65, max 81.97)"
    "zip-test (workloads/)","22.11 (min 21.74, max 22.22)"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","j722s_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","83.40 (min 82.64, max 84.03)"
    "core (workloads/)","0.60"
    "coremark-pro ()","1636.24 (min 1620.08, max 1655.03)"
    "linear_alg-mid-100x100-sp (workloads/)","29.35 (min 29.33, max 29.38)"
    "loops-all-mid-10k-sp (workloads/)","1.28 (min 1.27, max 1.29)"
    "nnet_test (workloads/)","2.17 (min 2.16, max 2.17)"
    "parser-125k (workloads/)","13.29 (min 12.58, max 14.08)"
    "radix2-big-64k (workloads/)","64.29 (min 60.39, max 67.36)"
    "sha-test (workloads/)","161.06 (min 158.73, max 161.29)"
    "zip-test (workloads/)","42.47 (min 41.67, max 42.55)"

 


.. csv-table:: CoreMarkProFourCore Benchmarks
    :header: "Benchmarks","j722s_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","159.18 (min 153.85, max 161.29)"
    "core (workloads/)","1.19 (min 1.18, max 1.20)"
    "coremark-pro ()","2556.34 (min 2515.96, max 2580.49)"
    "linear_alg-mid-100x100-sp (workloads/)","56.25 (min 55.68, max 56.37)"
    "loops-all-mid-10k-sp (workloads/)","2.06 (min 2.00, max 2.12)"
    "nnet_test (workloads/)","3.62 (min 3.61, max 3.62)"
    "parser-125k (workloads/)","8.69 (min 8.26, max 9.24)"
    "radix2-big-64k (workloads/)","92.75 (min 87.57, max 98.36)"
    "sha-test (workloads/)","270.27"
    "zip-test (workloads/)","76.20 (min 66.67, max 78.43)"

 

 
 


MultiBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
    :header: "Benchmarks","j722s_evm-fs: perf"

    "4m-check (workloads/)","397.66 (min 379.08, max 410.85)"
    "4m-check-reassembly (workloads/)","116.49 (min 111.36, max 121.36)"
    "4m-check-reassembly-tcp (workloads/)","58.05 (min 56.18, max 59.52)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","32.41 (min 31.76, max 33.11)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.87 (min 1.69, max 1.92)"
    "4m-cmykw2 (workloads/)","242.24 (min 232.83, max 247.83)"
    "4m-cmykw2-rotatew2 (workloads/)","49.03 (min 47.77, max 50.04)"
    "4m-reassembly (workloads/)","80.78 (min 76.75, max 90.17)"
    "4m-rotatew2 (workloads/)","52.59 (min 51.71, max 53.68)"
    "4m-tcp-mixed (workloads/)","116.56 (min 114.29, max 118.52)"
    "4m-x264w2 (workloads/)","1.95 (min 1.89, max 1.98)"
    "idct-4m (workloads/)","19.15 (min 19.14, max 19.16)"
    "idct-4mw1 (workloads/)","19.15 (min 19.14, max 19.17)"
    "ippktcheck-4m (workloads/)","397.48 (min 381.04, max 412.68)"
    "ippktcheck-4mw1 (workloads/)","398.40 (min 378.90, max 413.84)"
    "ipres-4m (workloads/)","105.91 (min 98.62, max 110.70)"
    "ipres-4mw1 (workloads/)","106.10 (min 99.67, max 110.87)"
    "md5-4m (workloads/)","27.24 (min 26.75, max 27.87)"
    "md5-4mw1 (workloads/)","27.39 (min 26.92, max 27.82)"
    "rgbcmyk-4m (workloads/)","64.56 (min 62.32, max 65.53)"
    "rgbcmyk-4mw1 (workloads/)","64.54 (min 62.29, max 65.49)"
    "rotate-4ms1 (workloads/)","23.03 (min 22.17, max 23.72)"
    "rotate-4ms1w1 (workloads/)","23.04 (min 22.09, max 23.70)"
    "rotate-4ms64 (workloads/)","23.29 (min 22.36, max 23.93)"
    "rotate-4ms64w1 (workloads/)","23.22 (min 22.28, max 23.89)"
    "x264-4mq (workloads/)","0.58 (min 0.57, max 0.58)"
    "x264-4mqw1 (workloads/)","0.58 (min 0.55, max 0.58)"



 
 


Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","j722s_evm-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","22.26 (min 20.09, max 47.31)"

 

 

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.
 



|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","j722s_evm-fs: Throughput (bits/sec)","j722s_evm-fs: CPU Load (%)"

    "11025","282350.00 (min 183425.00, max 331813.00)","0.29 (min 0.27, max 0.31)"
    "16000","422986.00 (min 244992.00, max 511983.00)","0.31 (min 0.29, max 0.34)"
    "22050","564950.00 (min 367635.00, max 663609.00)","0.32 (min 0.29, max 0.34)"
    "24000","564938.00 (min 367565.00, max 663625.00)","0.32 (min 0.30, max 0.35)"
    "32000","846154.00 (min 490544.00, max 1023960.00)","0.35 (min 0.30, max 0.38)"
    "44100","1129907.00 (min 735196.00, max 1327264.00)","0.38 (min 0.33, max 0.42)"
    "48000","1269208.33 (min 735738.00, max 1535945.00)","0.37 (min 0.33, max 0.40)"
    "88200","2260078.67 (min 1471209.00, max 2654516.00)","0.49 (min 0.36, max 0.56)"
    "96000","2538445.33 (min 1471875.00, max 3071735.00)","0.51 (min 0.38, max 0.58)"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","j722s_evm-fs: Throughput (bits/sec)","j722s_evm-fs: CPU Load (%)"

    "11025","233008.33 (min 183250.00, max 331951.00)","0.26 (min 0.25, max 0.28)"
    "16000","334094.00 (min 244824.00, max 512198.00)","0.26 (min 0.25, max 0.27)"
    "22050","466374.00 (min 367203.00, max 663886.00)","0.28 (min 0.26, max 0.32)"
    "24000","466316.00 (min 366979.00, max 663903.00)","0.27 (min 0.25, max 0.30)"
    "32000","668315.67 (min 489566.00, max 1024388.00)","0.28 (min 0.26, max 0.31)"
    "44100","932652.00 (min 734279.00, max 1327819.00)","0.33 (min 0.29, max 0.37)"
    "48000","1002312.00 (min 733745.00, max 1536588.00)","0.30 (min 0.27, max 0.33)"
    "88200","1864908.00 (min 1467285.00, max 2655628.00)","0.39 (min 0.29, max 0.51)"
    "96000","2004372.00 (min 1467503.00, max 3073021.00)","0.36 (min 0.31, max 0.43)"

 
 



 



|

Graphics SGX/RGX Driver
-------------------------
 




Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","j722s_evm-fs: Score"

    "Glmark2-DRM","286.15 (min 285.00, max 287.00)"
    "Glmark2-Wayland","791.23 (min 740.00, max 811.00)"

 
 

 

 



|

Ethernet
-----------------
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

The following commands were used to tune the socket buffer sizes on the DUT before running the performance tests:

.. code-block:: console

   sysctl -w net.core.rmem_default=33554432
   sysctl -w net.core.rmem_max=67108864

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


CPSW/CPSW2g/CPSW3g Ethernet Driver 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- CPSW2g: AM65x, J7200, J721e, J721S2, J784S4, J742S2
- CPSW3g: AM64x, AM62x, AM62ax, AM62dx, AM62px


.. rubric::  TCP Bidirectional Throughput 
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1400.96 (min 821.14, max 1858.02)","50.61 (min 34.00, max 66.05)"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1249.26 (min 838.70, max 1858.49)","35.94 (min 31.92, max 40.01)"




.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","j722s_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: Packets Per Second (kPPS)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","56.39 (min 53.92, max 59.25)","110.11 (min 105.00, max 116.00)","32.81 (min 25.28, max 47.09)"
    "128","","104.27 (min 49.66, max 116.67)","101.70 (min 48.00, max 114.00)","30.39 (min 17.06, max 39.64)"
    "256","","222.26 (min 211.61, max 232.25)","108.33 (min 103.00, max 113.00)","25.87 (min 25.26, max 26.19)"
    "1024","","676.85 (min 104.85, max 844.00)","82.73 (min 13.00, max 103.00)","28.89 (min 2.08, max 40.04)"
    "1518","","772.00 (min 559.32, max 836.04)","63.70 (min 46.00, max 69.00)","28.08 (min 21.61, max 37.42)"





 
 

 

 
 

 

 



|

Linux OSPI Flash Driver
-------------------------

 

 

 

 

 

 


 


 

 

 

 


.. rubric:: J722S-EVM
   :name: j722s-evm-ospi


.. rubric:: UBIFS
   :name: j722s-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j722s_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Write UBIFS CPU Load (%)","j722s_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.12, max 0.29)","29.04 (min 24.84, max 37.67)","63.67 (min 55.35, max 65.07)","22.35 (min 8.33, max 53.85)"
    "262144","0.14 (min 0.10, max 0.19)","29.95 (min 25.37, max 35.93)","64.44 (min 62.76, max 65.47)","21.92 (min 8.33, max 28.57)"
    "524288","0.15 (min 0.10, max 0.19)","30.21 (min 26.04, max 37.28)","64.01 (min 62.63, max 65.39)","17.60 (min 0.00, max 26.67)"
    "1048576","0.15 (min 0.10, max 0.19)","29.97 (min 26.60, max 37.86)","62.80 (min 62.12, max 64.01)","22.58 (min 15.38, max 26.67)"




.. rubric:: RAW
   :name: j722s-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j722s_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","222.54 (min 208.33, max 227.27)"

 
 

 

 

 

 
 

 

 

 

 

 



EMMC Driver
-----------
.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.



EMMC EXT4 FIO 1G
^^^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 

 

 

 

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

    "1m","94.03 (min 78.00, max 97.60)","1.78 (min 1.41, max 1.97)","266.46 (min 113.00, max 296.00)","2.80 (min 1.36, max 3.32)"
    "4m","94.27 (min 78.40, max 98.10)","1.29 (min 1.05, max 1.41)","236.31 (min 112.00, max 295.00)","2.01 (min 1.15, max 2.43)"
    "4k","72.29 (min 8.57, max 83.90)","22.48 (min 3.20, max 26.13)","83.91 (min 56.60, max 90.90)","19.66 (min 14.57, max 21.33)"
    "256k","92.61 (min 68.70, max 97.60)","2.21 (min 1.69, max 2.46)","262.82 (min 94.80, max 296.00)","3.98 (min 1.51, max 4.50)"

 

 

 

 

 

 

 

 

 
 


EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 

 

 

 

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "1m","92.82 (min 78.00, max 97.80)","1.59 (min 1.28, max 1.76)","252.92 (min 112.00, max 296.00)","2.65 (min 1.43, max 3.31)"
    "4m","93.13 (min 78.20, max 98.30)","1.20 (min 1.01, max 1.36)","248.94 (min 95.20, max 296.00)","2.01 (min 1.05, max 2.41)"
    "4k","65.30 (min 8.58, max 82.70)","15.42 (min 2.45, max 19.51)","85.29 (min 56.60, max 94.30)","19.05 (min 13.48, max 20.97)"
    "256k","89.90 (min 68.50, max 97.80)","1.92 (min 1.30, max 2.17)","248.92 (min 94.30, max 296.00)","3.55 (min 1.66, max 4.34)"

 

 

 

 

 

 

 

 

 
 

 

 

 

 

 
 



UBoot EMMC Driver
-----------------

 

 

 

 

 

 

 

 

 

 

 

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j722s_evm-fs: Write Throughput (Kbytes/sec)","j722s_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","97131.28 (min 93622.86, max 103044.03)","160585.11 (min 95255.81, max 172463.16)"
    "4000000","97710.85 (min 94842.26, max 100669.74)","167100.30 (min 123886.58, max 175699.73)"

 

 

 

 

 

 

 

 

 
 

 


MMCSD
-----

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.


MMC EXT4 FIO 1G
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 

 

 

 

 

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

    "1m","42.20 (min 41.20, max 43.40)","1.31 (min 1.18, max 1.39)","86.98 (min 85.10, max 87.40)","1.53 (min 1.41, max 1.62)"
    "4m","42.18 (min 40.80, max 43.30)","0.93 (min 0.86, max 1.02)","86.89 (min 85.00, max 87.40)","1.14 (min 1.08, max 1.25)"
    "4k","2.78 (min 2.77, max 2.82)","1.92 (min 1.80, max 2.07)","12.98 (min 12.90, max 13.10)","4.52 (min 4.33, max 4.79)"
    "256k","38.01 (min 36.70, max 39.60)","1.51 (min 1.38, max 1.60)","83.72 (min 83.20, max 84.40)","1.76 (min 1.64, max 1.84)"

 

 

 

 

 

 

 

 

 

 

 
 


MMC RAW FIO 1G
^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 

 

 

 

 

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "1m","43.42 (min 42.00, max 45.00)","1.15 (min 1.07, max 1.23)","88.16 (min 88.10, max 88.30)","1.42 (min 1.28, max 1.52)"
    "4m","43.17 (min 41.20, max 45.10)","0.92 (min 0.81, max 0.96)","88.12 (min 88.00, max 88.30)","1.12 (min 1.03, max 1.25)"
    "4k","2.81 (min 2.80, max 2.82)","1.60 (min 1.54, max 1.71)","13.03 (min 13.00, max 13.10)","4.19 (min 4.05, max 4.33)"
    "256k","37.85 (min 36.10, max 41.30)","1.27 (min 1.15, max 1.37)","84.35 (min 84.20, max 84.50)","1.71 (min 1.64, max 1.80)"

 

 

 

 

 
 


MMC EXT4
^^^^^^^^

 

 

 

 

 

 

 

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "102400","37.72 (min 33.75, max 43.21)","3.13 (min 2.33, max 4.56)","76.99 (min 72.19, max 81.46)","4.74 (min 4.01, max 5.54)"
    "262144","38.17 (min 35.48, max 42.02)","3.28 (min 2.47, max 4.96)","83.96 (min 77.77, max 87.12)","5.08 (min 3.42, max 6.57)"
    "524288","39.17 (min 36.79, max 42.85)","3.15 (min 2.56, max 4.66)","90.92 (min 89.43, max 91.33)","5.21 (min 4.37, max 6.24)"
    "1048576","38.30 (min 36.81, max 41.43)","3.05 (min 2.34, max 4.61)","90.98 (min 89.06, max 91.33)","5.30 (min 4.81, max 5.86)"
    "5242880","38.95 (min 36.47, max 42.17)","3.05 (min 2.44, max 4.46)","91.08 (min 89.07, max 91.36)","5.05 (min 4.39, max 5.43)"

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 


MMC EXT2
^^^^^^^^

 

 

 

 

 

 

 

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "102400","39.81 (min 33.62, max 42.84)","3.73 (min 2.83, max 6.09)","79.03 (min 76.26, max 80.71)","5.09 (min 4.08, max 5.94)"
    "262144","38.26 (min 33.11, max 42.42)","3.51 (min 2.51, max 6.19)","85.02 (min 81.72, max 86.81)","5.54 (min 4.38, max 6.24)"
    "524288","37.28 (min 32.44, max 41.68)","3.42 (min 2.43, max 5.85)","89.09 (min 85.08, max 90.53)","5.42 (min 4.91, max 5.88)"
    "1048576","37.96 (min 32.93, max 41.90)","3.44 (min 2.51, max 6.11)","89.92 (min 84.98, max 90.43)","5.37 (min 4.76, max 5.79)"
    "5242880","37.83 (min 32.90, max 41.98)","3.40 (min 2.41, max 6.02)","89.93 (min 85.36, max 90.54)","5.33 (min 4.56, max 6.06)"

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 



UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 

 

 

 

 

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j722s_evm-fs: Write Throughput (Kbytes/sec)","j722s_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","34521.95 (min 17429.79, max 39766.99)","82182.25 (min 80313.73, max 83591.84)"
    "800000","41174.43 (min 18492.10, max 47080.46)","87297.61 (min 85333.33, max 88086.02)"
    "1000000","44044.35 (min 19006.96, max 49951.22)","89644.80 (min 88562.16, max 90021.98)"

 

 

 

 

 

 

 

 

 

 

 
 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 

 



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","j722s_evm-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","23215.63 (min 22151.17, max 24363.69)"
    "aes-128-cbc","16","426.77 (min 403.10, max 439.23)"
    "aes-128-cbc","16384","85577.41 (min 83197.95, max 86168.92)"
    "aes-128-cbc","256","7045.98 (min 6523.65, max 7271.51)"
    "aes-128-cbc","64","1847.27 (min 1697.60, max 1920.32)"
    "aes-128-cbc","8192","72273.81 (min 69530.97, max 73400.32)"
    "aes-128-ecb","1024","23739.18 (min 22653.27, max 24908.80)"
    "aes-128-ecb","16","438.44 (min 407.23, max 449.49)"
    "aes-128-ecb","16384","88213.56 (min 86496.60, max 89139.88)"
    "aes-128-ecb","256","7230.48 (min 6547.20, max 7430.74)"
    "aes-128-ecb","64","1897.64 (min 1759.64, max 1970.97)"
    "aes-128-ecb","8192","74464.02 (min 71783.77, max 75513.86)"
    "aes-192-cbc","1024","22706.78 (min 21753.17, max 23803.56)"
    "aes-192-cbc","16","428.00 (min 403.40, max 438.95)"
    "aes-192-cbc","16384","77491.28 (min 76283.90, max 78260.91)"
    "aes-192-cbc","256","7001.63 (min 6517.93, max 7218.77)"
    "aes-192-cbc","64","1842.60 (min 1695.85, max 1924.48)"
    "aes-192-cbc","8192","66317.18 (min 64555.69, max 67267.24)"
    "aes-192-ecb","1024","23328.93 (min 22204.07, max 24482.13)"
    "aes-192-ecb","16","437.39 (min 407.09, max 447.47)"
    "aes-192-ecb","16384","79527.10 (min 77720.23, max 80745.81)"
    "aes-192-ecb","256","7166.92 (min 6531.24, max 7358.72)"
    "aes-192-ecb","64","1887.81 (min 1727.21, max 1957.40)"
    "aes-192-ecb","8192","68371.48 (min 66385.24, max 69394.43)"
    "aes-256-cbc","1024","22090.07 (min 21141.50, max 23027.37)"
    "aes-256-cbc","16","427.91 (min 402.01, max 437.66)"
    "aes-256-cbc","16384","70236.95 (min 69058.56, max 71538.01)"
    "aes-256-cbc","256","6931.76 (min 6486.10, max 7170.05)"
    "aes-256-cbc","64","1840.06 (min 1679.91, max 1927.49)"
    "aes-256-cbc","8192","61121.77 (min 59370.15, max 62180.01)"
    "aes-256-ecb","1024","22728.18 (min 21734.06, max 23703.55)"
    "aes-256-ecb","16","436.99 (min 407.34, max 448.30)"
    "aes-256-ecb","16384","72624.39 (min 70866.26, max 73536.85)"
    "aes-256-ecb","256","7115.89 (min 6539.86, max 7290.97)"
    "aes-256-ecb","64","1875.32 (min 1758.95, max 1940.03)"
    "aes-256-ecb","8192","62975.47 (min 61115.05, max 63646.38)"
    "sha256","1024","37580.17 (min 37018.97, max 38389.76)"
    "sha256","16","626.79 (min 619.02, max 634.84)"
    "sha256","16384","299604.97 (min 297194.84, max 302661.63)"
    "sha256","256","9821.24 (min 9667.41, max 10056.79)"
    "sha256","64","2481.63 (min 2441.51, max 2533.16)"
    "sha256","8192","202097.48 (min 200119.64, max 205138.60)"
    "sha512","1024","25996.34 (min 25505.79, max 26348.20)"
    "sha512","16","610.48 (min 597.36, max 621.75)"
    "sha512","16384","68385.56 (min 68217.51, max 68556.12)"
    "sha512","256","8673.35 (min 8456.70, max 8841.22)"
    "sha512","64","2444.75 (min 2383.68, max 2504.26)"
    "sha512","8192","61534.94 (min 61306.20, max 61707.61)"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","j722s_evm-fs: CPU Load"

    "aes-128-cbc","32.54 (min 31.00, max 34.00)"
    "aes-128-ecb","33.62 (min 32.00, max 35.00)"
    "aes-192-cbc","32.46 (min 30.00, max 33.00)"
    "aes-192-ecb","33.00 (min 31.00, max 34.00)"
    "aes-256-cbc","31.54 (min 29.00, max 33.00)"
    "aes-256-ecb","32.31 (min 31.00, max 33.00)"
    "sha256","94.31 (min 84.00, max 96.00)"
    "sha512","94.85 (min 90.00, max 96.00)"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc

 



 
 

 




