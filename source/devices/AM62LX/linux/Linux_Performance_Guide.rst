.. include:: <isonum.txt>

#################################
 Linux 12.02.00 Performance Guide
#################################

***************
Read This First
***************

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
| AM62Lx EVM     | AM62Lx Evaluation Module rev E1-1 with ARM running at 1.4GHz, DDR data rate 1600 MT/S                          |
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


*****************
System Benchmarks
*****************

LMBench
=======

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
   :header: "Benchmarks","am62lxx_evm-fs: perf"

   "af_unix_sock_stream_latency (microsec)","27.00 (min 26.45, max 27.87)"
   "af_unix_socket_stream_bandwidth (mb\s)","491.81 (min 434.42, max 544.44)"
   "bw_file_rd-io-1mb (mb/s)","981.38 (min 895.74, max 1059.51)"
   "bw_file_rd-o2c-1mb (mb/s)","500.93 (min 466.78, max 558.87)"
   "bw_mem-bcopy-16mb (mb/s)","781.08 (min 706.99, max 849.26)"
   "bw_mem-bcopy-1mb (mb/s)","811.17 (min 691.32, max 922.85)"
   "bw_mem-bcopy-2mb (mb/s)","817.78 (min 692.88, max 954.65)"
   "bw_mem-bcopy-4mb (mb/s)","844.41 (min 725.29, max 959.69)"
   "bw_mem-bcopy-8mb (mb/s)","863.30 (min 757.93, max 973.47)"
   "bw_mem-bzero-16mb (mb/s)","2429.95 (min 2103.33, max 2727.58)"
   "bw_mem-bzero-1mb (mb/s)","1619.18 (min 691.32, max 2724.80)"
   "bw_mem-bzero-2mb (mb/s)","1623.64 (min 692.88, max 2727.12)"
   "bw_mem-bzero-4mb (mb/s)","1635.49 (min 725.29, max 2725.26)"
   "bw_mem-bzero-8mb (mb/s)","1631.69 (min 757.93, max 2726.65)"
   "bw_mem-cp-16mb (mb/s)","455.40 (min 401.06, max 509.21)"
   "bw_mem-cp-1mb (mb/s)","1555.83 (min 393.96, max 2887.95)"
   "bw_mem-cp-2mb (mb/s)","1500.81 (min 393.16, max 2822.37)"
   "bw_mem-cp-4mb (mb/s)","1481.35 (min 401.08, max 2774.41)"
   "bw_mem-cp-8mb (mb/s)","1485.28 (min 450.27, max 2754.35)"
   "bw_mem-fcp-16mb (mb/s)","785.90 (min 717.01, max 863.32)"
   "bw_mem-fcp-1mb (mb/s)","1652.38 (min 771.96, max 2724.80)"
   "bw_mem-fcp-2mb (mb/s)","1645.73 (min 766.58, max 2727.12)"
   "bw_mem-fcp-4mb (mb/s)","1659.18 (min 786.70, max 2725.26)"
   "bw_mem-fcp-8mb (mb/s)","1655.68 (min 809.80, max 2726.65)"
   "bw_mem-frd-16mb (mb/s)","1401.03 (min 1237.43, max 1553.25)"
   "bw_mem-frd-1mb (mb/s)","1105.00 (min 771.96, max 1488.10)"
   "bw_mem-frd-2mb (mb/s)","1096.72 (min 766.58, max 1523.52)"
   "bw_mem-frd-4mb (mb/s)","1141.16 (min 786.70, max 1550.79)"
   "bw_mem-frd-8mb (mb/s)","1153.78 (min 809.80, max 1552.80)"
   "bw_mem-fwr-16mb (mb/s)","2440.67 (min 2123.42, max 2735.04)"
   "bw_mem-fwr-1mb (mb/s)","1983.54 (min 1193.85, max 2887.95)"
   "bw_mem-fwr-2mb (mb/s)","1933.31 (min 1164.31, max 2822.37)"
   "bw_mem-fwr-4mb (mb/s)","1933.56 (min 1223.24, max 2774.41)"
   "bw_mem-fwr-8mb (mb/s)","1927.24 (min 1240.12, max 2754.35)"
   "bw_mem-rd-16mb (mb/s)","1419.42 (min 1255.20, max 1579.78)"
   "bw_mem-rd-1mb (mb/s)","1038.45 (min 547.45, max 1568.76)"
   "bw_mem-rd-2mb (mb/s)","1019.09 (min 536.77, max 1551.11)"
   "bw_mem-rd-4mb (mb/s)","1059.71 (min 608.27, max 1568.42)"
   "bw_mem-rd-8mb (mb/s)","1089.35 (min 682.59, max 1569.55)"
   "bw_mem-rdwr-16mb (mb/s)","791.95 (min 664.67, max 885.30)"
   "bw_mem-rdwr-1mb (mb/s)","565.72 (min 393.96, max 746.83)"
   "bw_mem-rdwr-2mb (mb/s)","537.00 (min 393.16, max 693.60)"
   "bw_mem-rdwr-4mb (mb/s)","591.70 (min 401.08, max 789.42)"
   "bw_mem-rdwr-8mb (mb/s)","630.48 (min 450.27, max 861.42)"
   "bw_mem-wr-16mb (mb/s)","816.63 (min 697.35, max 935.78)"
   "bw_mem-wr-1mb (mb/s)","657.09 (min 523.38, max 777.91)"
   "bw_mem-wr-2mb (mb/s)","622.77 (min 515.40, max 726.08)"
   "bw_mem-wr-4mb (mb/s)","703.88 (min 600.69, max 809.55)"
   "bw_mem-wr-8mb (mb/s)","753.32 (min 642.21, max 877.77)"
   "bw_mmap_rd-mo-1mb (mb/s)","1166.88 (min 998.86, max 1351.58)"
   "bw_mmap_rd-o2c-1mb (mb/s)","506.77 (min 469.04, max 563.06)"
   "bw_pipe (mb/s)","440.02 (min 378.49, max 494.68)"
   "bw_unix (mb/s)","491.81 (min 434.42, max 544.44)"
   "lat_connect (us)","108.01 (min 95.53, max 117.50)"
   "lat_ctx-2-128k (us)","39.98 (min 31.47, max 49.18)"
   "lat_ctx-2-256k (us)","156.95 (min 132.39, max 190.48)"
   "lat_ctx-4-128k (us)","75.65 (min 15.64, max 107.41)"
   "lat_ctx-4-256k (us)","86.85 (min 0.00, max 180.82)"
   "lat_fs-0k (num_files)","199.83 (min 174.00, max 223.00)"
   "lat_fs-10k (num_files)","91.83 (min 81.00, max 99.00)"
   "lat_fs-1k (num_files)","139.17 (min 132.00, max 146.00)"
   "lat_fs-4k (num_files)","125.50 (min 108.00, max 147.00)"
   "lat_mem_rd-stride128-sz1000k (ns)","47.65 (min 42.95, max 52.47)"
   "lat_mem_rd-stride128-sz125k (ns)","6.20 (min 6.18, max 6.23)"
   "lat_mem_rd-stride128-sz250k (ns)","12.69 (min 7.79, max 17.76)"
   "lat_mem_rd-stride128-sz31k (ns)","3.59 (min 2.42, max 4.46)"
   "lat_mem_rd-stride128-sz50 (ns)","2.40 (min 2.40, max 2.41)"
   "lat_mem_rd-stride128-sz500k (ns)","43.43 (min 38.91, max 48.50)"
   "lat_mem_rd-stride128-sz62k (ns)","5.72 (min 5.70, max 5.74)"
   "lat_mmap-1m (us)","59.33 (min 56.00, max 65.00)"
   "lat_ops-double-add (ns)","3.21"
   "lat_ops-double-div (ns)","17.66 (min 17.64, max 17.68)"
   "lat_ops-double-mul (ns)","3.21"
   "lat_ops-float-add (ns)","3.21"
   "lat_ops-float-div (ns)","10.44 (min 10.42, max 10.45)"
   "lat_ops-float-mul (ns)","3.21"
   "lat_ops-int-add (ns)","0.80"
   "lat_ops-int-bit (ns)","0.53"
   "lat_ops-int-div (ns)","4.81 (min 4.81, max 4.82)"
   "lat_ops-int-mod (ns)","5.08 (min 5.08, max 5.09)"
   "lat_ops-int-mul (ns)","3.44 (min 3.41, max 3.47)"
   "lat_ops-int64-add (ns)","0.80"
   "lat_ops-int64-bit (ns)","0.54 (min 0.53, max 0.54)"
   "lat_ops-int64-div (ns)","7.62 (min 7.62, max 7.63)"
   "lat_ops-int64-mod (ns)","5.89 (min 5.88, max 5.89)"
   "lat_ops-int64-mul (ns)","3.97 (min 3.97, max 3.98)"
   "lat_pagefault (us)","0.83 (min 0.66, max 0.93)"
   "lat_pipe (us)","20.45 (min 19.62, max 21.33)"
   "lat_proc-exec (us)","1431.13 (min 1303.40, max 1561.50)"
   "lat_proc-fork (us)","1247.01 (min 1113.00, max 1382.80)"
   "lat_proc-proccall (us)","0.01"
   "lat_select (us)","35.93 (min 35.63, max 36.44)"
   "lat_sem (us)","3.28 (min 3.14, max 3.46)"
   "lat_sig-catch (us)","6.42 (min 6.36, max 6.47)"
   "lat_sig-install (us)","0.68 (min 0.67, max 0.69)"
   "lat_sig-prot (us)","0.75 (min 0.39, max 1.06)"
   "lat_syscall-fstat (us)","2.01 (min 1.90, max 2.07)"
   "lat_syscall-null (us)","0.42 (min 0.41, max 0.46)"
   "lat_syscall-open (us)","525.09 (min 449.92, max 603.00)"
   "lat_syscall-read (us)","0.80 (min 0.79, max 0.82)"
   "lat_syscall-stat (us)","4.99 (min 4.78, max 5.15)"
   "lat_syscall-write (us)","0.76 (min 0.75, max 0.77)"
   "lat_tcp (us)","0.85"
   "lat_unix (us)","27.00 (min 26.45, max 27.87)"
   "latency_for_0.50_mb_block_size (nanosec)","43.43 (min 38.91, max 48.50)"
   "latency_for_1.00_mb_block_size (nanosec)","23.83 (min 0.00, max 52.47)"
   "pipe_bandwidth (mb\s)","440.02 (min 378.49, max 494.68)"
   "pipe_latency (microsec)","20.45 (min 19.62, max 21.33)"
   "procedure_call (microsec)","0.01"
   "select_on_200_tcp_fds (microsec)","35.93 (min 35.63, max 36.44)"
   "semaphore_latency (microsec)","3.28 (min 3.14, max 3.46)"
   "signal_handler_latency (microsec)","0.68 (min 0.67, max 0.69)"
   "signal_handler_overhead (microsec)","6.42 (min 6.36, max 6.47)"
   "tcp_ip_connection_cost_to_localhost (microsec)","108.01 (min 95.53, max 117.50)"
   "tcp_latency_using_localhost (microsec)","0.85"

Dhrystone
=========

Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed.

Please take note, different run may produce different slightly results.
This is advised to run this test multiple times in order to get maximum
performance numbers.

Execute the benchmark with the following:

.. code-block:: console

    runDhrystone

.. csv-table:: Dhrystone Benchmarks
   :header: "Benchmarks","am62lxx_evm-fs: perf"

   "cpu_clock (mhz)","1250.00"
   "dhrystone_per_mhz (dmips/mhz)","2.80"
   "dhrystone_per_second (dhrystonep)","6087662.29 (min 6060606.00, max 6250000.00)"

Whetstone
=========

Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

.. code-block:: console

    runWhetstone

.. csv-table:: Whetstone Benchmarks
   :header: "Benchmarks","am62lxx_evm-fs: perf"

   "whetstone (mips)","5000.00"

Linpack
=======

Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
   :header: "Benchmarks","am62lxx_evm-fs: perf"

   "linpack (kflops)","518135.71 (min 515515.00, max 519219.00)"

NBench
======

NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
   :header: "Benchmarks","am62lxx_evm-fs: perf"

   "assignment (iterations)","12.64 (min 12.61, max 12.66)"
   "fourier (iterations)","17292.50 (min 17291.00, max 17294.00)"
   "fp_emulation (iterations)","182.37 (min 182.33, max 182.41)"
   "huffman (iterations)","1060.82 (min 1060.20, max 1061.00)"
   "idea (iterations)","2741.35 (min 2740.90, max 2741.50)"
   "lu_decomposition (iterations)","474.00 (min 471.56, max 476.14)"
   "neural_net (iterations)","8.64"
   "numeric_sort (iterations)","482.14 (min 473.92, max 484.91)"
   "string_sort (iterations)","146.07 (min 146.05, max 146.09)"

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

.. code-block:: console

    stream_c

.. csv-table:: Stream Benchmarks
   :header: "Benchmarks","am62lxx_evm-fs: perf"

   "add (mb/s)","1619.81 (min 1502.60, max 1861.00)"
   "copy (mb/s)","1722.66 (min 1604.70, max 1972.30)"
   "scale (mb/s)","1798.00 (min 1656.80, max 2082.50)"
   "triad (mb/s)","1602.17 (min 1488.50, max 1837.90)"

CoreMarkPro
===========

CoreMark\ |reg|-Pro is a comprehensive, advanced processor benchmark that works
with and enhances the market-proven industry-standard EEMBC CoreMark\ |reg|
benchmark. While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the
entire processor, adding comprehensive support for multicore technology, a
combination of integer and floating-point workloads, and data sets for utilizing
larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
   :header: "Benchmarks","am62lxx_evm-fs: perf"

   "cjpeg-rose7-preset (workloads/)","37.06 (min 36.76, max 37.31)"
   "core (workloads/)","0.27"
   "coremark-pro ()","716.56 (min 699.78, max 733.93)"
   "linear_alg-mid-100x100-sp (workloads/)","13.07 (min 13.05, max 13.09)"
   "loops-all-mid-10k-sp (workloads/)","0.58 (min 0.56, max 0.60)"
   "nnet_test (workloads/)","0.96"
   "parser-125k (workloads/)","7.78 (min 7.52, max 8.00)"
   "radix2-big-64k (workloads/)","17.82 (min 16.31, max 19.79)"
   "sha-test (workloads/)","70.59 (min 68.97, max 71.94)"
   "zip-test (workloads/)","19.95 (min 19.23, max 20.41)"

.. csv-table:: CoreMarkProTwoCore Benchmarks
   :header: "Benchmarks","am62lxx_evm-fs: perf"

   "cjpeg-rose7-preset (workloads/)","72.32 (min 71.43, max 72.99)"
   "core (workloads/)","0.53 (min 0.53, max 0.54)"
   "coremark-pro ()","1260.34 (min 1227.16, max 1295.85)"
   "linear_alg-mid-100x100-sp (workloads/)","25.93 (min 25.09, max 26.12)"
   "loops-all-mid-10k-sp (workloads/)","1.03 (min 0.97, max 1.08)"
   "nnet_test (workloads/)","1.92 (min 1.91, max 1.92)"
   "parser-125k (workloads/)","9.25 (min 8.89, max 9.66)"
   "radix2-big-64k (workloads/)","25.70 (min 23.07, max 28.78)"
   "sha-test (workloads/)","135.21 (min 129.87, max 138.89)"
   "zip-test (workloads/)","35.86 (min 33.90, max 37.74)"

MultiBench
==========

MultiBench\ |trade| is a suite of benchmarks that allows processor and system
designers to analyze, test, and improve multicore processors. It uses three
forms of concurrency: Data decomposition: multiple threads cooperating on
achieving a unified goal and demonstrating a processor's support for fine grain
parallelism.
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
   :header: "Benchmarks","am62lxx_evm-fs: perf"

   "4m-check (workloads/)","291.40 (min 269.92, max 319.33)"
   "4m-check-reassembly (workloads/)","75.19 (min 67.66, max 84.60)"
   "4m-check-reassembly-tcp (workloads/)","42.84 (min 36.50, max 47.17)"
   "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","17.30 (min 16.14, max 18.79)"
   "4m-check-reassembly-tcp-x264w2 (workloads/)","0.92 (min 0.91, max 0.95)"
   "4m-cmykw2 (workloads/)","106.97 (min 102.46, max 109.65)"
   "4m-cmykw2-rotatew2 (workloads/)","23.35 (min 21.10, max 26.21)"
   "4m-reassembly (workloads/)","87.86 (min 79.11, max 98.04)"
   "4m-rotatew2 (workloads/)","26.63 (min 24.80, max 28.87)"
   "4m-tcp-mixed (workloads/)","100.89 (min 95.81, max 108.84)"
   "4m-x264w2 (workloads/)","0.94 (min 0.92, max 0.97)"
   "empty-wld (workloads/)","1.00"
   "idct-4m (workloads/)","17.58 (min 17.57, max 17.60)"
   "idct-4mw1 (workloads/)","17.59 (min 17.57, max 17.62)"
   "ippktcheck-4m (workloads/)","290.81 (min 267.92, max 319.16)"
   "ippktcheck-4mw1 (workloads/)","290.53 (min 268.04, max 321.75)"
   "ipres-4m (workloads/)","70.35 (min 64.32, max 77.96)"
   "ipres-4mw1 (workloads/)","70.50 (min 64.85, max 78.41)"
   "md5-4m (workloads/)","19.33 (min 18.22, max 20.91)"
   "md5-4mw1 (workloads/)","18.95 (min 17.78, max 20.49)"
   "rgbcmyk-4m (workloads/)","57.40 (min 57.13, max 57.75)"
   "rgbcmyk-4mw1 (workloads/)","57.22 (min 56.59, max 57.70)"
   "rotate-4ms1 (workloads/)","21.29 (min 19.76, max 23.17)"
   "rotate-4ms1w1 (workloads/)","21.31 (min 19.67, max 23.22)"
   "rotate-4ms64 (workloads/)","21.36 (min 19.65, max 23.25)"
   "rotate-4ms64w1 (workloads/)","21.37 (min 19.72, max 23.25)"
   "x264-4mq (workloads/)","0.50 (min 0.50, max 0.51)"
   "x264-4mqw1 (workloads/)","0.51 (min 0.50, max 0.51)"

*********************
Boot-time Measurement
*********************

Boot media: MMCSD
=================

.. csv-table:: Linux boot time MMCSD
   :header: "Boot Configuration","am62lxx_evm-fs: Boot time in seconds: avg(min,max)"

   "Linux boot time from SD with default rootfs (20 boot cycles)","21.32 (min 19.69, max 29.06)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

***********************
Linux OSPI Flash Driver
***********************

.. rubric:: AM62XX-SK
   :name: am62xx-sk-ospi-flash-driver

.. rubric:: AM62LXX-EVM
   :name: am62lxx-evm-ospi

.. rubric:: RAW
   :name: am62lxx-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
   :header: "File size (Mbytes)","am62lxx_evm-fs: Raw Read Throughput (Mbytes/sec)"

   "50","167.19 (min 151.51, max 178.57)"

***********
EMMC Driver
***********

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

EMMC EXT4 FIO 1G
================

.. csv-table:: EMMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

   "1m","126.43 (min 115.00, max 129.00)","9.33 (min 8.69, max 9.83)","179.43 (min 179.00, max 180.00)","8.86 (min 8.08, max 9.35)"
   "4m","127.14 (min 120.00, max 129.00)","5.82 (min 5.65, max 5.97)","179.14 (min 179.00, max 180.00)","5.46 (min 5.20, max 5.66)"
   "4k","85.69 (min 81.00, max 88.10)","57.92 (min 54.42, max 59.93)","92.93 (min 90.00, max 94.80)","56.87 (min 56.10, max 58.26)"
   "256k","123.14 (min 123.00, max 124.00)","13.22 (min 13.00, max 13.75)","176.86 (min 175.00, max 179.00)","11.92 (min 11.62, max 12.46)"

EMMC RAW FIO 1G
===============

.. csv-table:: EMMC RAW FIO 1G
   :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

   "1m","129.14 (min 129.00, max 130.00)","8.32 (min 7.93, max 8.61)","180.00","8.83 (min 8.48, max 9.22)"
   "4m","127.71 (min 120.00, max 129.00)","5.52 (min 5.29, max 5.63)","180.00","5.22 (min 5.08, max 5.48)"
   "4k","95.07 (min 94.40, max 95.60)","46.70 (min 45.84, max 48.04)","98.34 (min 97.00, max 101.00)","52.18 (min 50.18, max 55.03)"
   "256k","123.57 (min 123.00, max 124.00)","11.10 (min 10.84, max 11.49)","178.71 (min 178.00, max 179.00)","10.90 (min 9.75, max 11.45)"

EMMC EXT4
=========

.. csv-table:: EMMC EXT4
   :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

   "102400","104.46 (min 96.12, max 107.87)","18.14 (min 14.72, max 22.84)","163.08 (min 153.58, max 175.71)","31.17 (min 28.95, max 33.33)"
   "262144","106.77 (min 100.58, max 110.82)","12.91 (min 10.64, max 18.66)","167.31 (min 156.54, max 182.41)","27.88 (min 24.77, max 30.47)"
   "524288","106.60 (min 98.84, max 110.30)","12.97 (min 10.66, max 17.07)","170.38 (min 165.22, max 174.24)","29.67 (min 26.50, max 33.07)"
   "1048576","107.02 (min 100.43, max 110.37)","13.56 (min 10.31, max 27.18)","179.77 (min 176.17, max 184.28)","28.05 (min 23.21, max 32.48)"
   "5242880","107.67 (min 100.25, max 112.70)","13.95 (min 11.34, max 18.13)","181.91 (min 180.00, max 184.65)","34.49 (min 31.86, max 36.52)"

EMMC VFAT
=========

.. csv-table:: EMMC VFAT
   :header: "Buffer size (bytes)","am62lxx_evm-fs: Write VFAT Throughput (Mbytes/sec)","am62lxx_evm-fs: Write VFAT CPU Load (%)","am62lxx_evm-fs: Read VFAT Throughput (Mbytes/sec)","am62lxx_evm-fs: Read VFAT CPU Load (%)"

   "102400","29.38 (min 15.51, max 34.04)","17.79 (min 15.69, max 20.63)","158.13 (min 149.51, max 165.96)","37.38 (min 33.90, max 39.53)"
   "262144","44.42 (min 19.06, max 57.04)","20.39 (min 17.06, max 23.08)","162.66 (min 146.04, max 175.99)","36.98 (min 34.51, max 38.89)"
   "524288","52.05 (min 20.65, max 64.14)","20.09 (min 16.80, max 26.04)","155.01 (min 142.41, max 165.93)","35.84 (min 33.61, max 37.93)"
   "1048576","59.50 (min 21.90, max 73.88)","21.17 (min 19.87, max 23.69)","152.54 (min 141.48, max 175.16)","36.69 (min 30.17, max 40.91)"
   "5242880","70.24 (min 22.21, max 84.62)","23.05 (min 21.12, max 27.17)","150.85 (min 143.06, max 173.52)","37.55 (min 30.70, max 40.14)"

*****************
UBoot EMMC Driver
*****************

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","am62lxx_evm-fs: Write Throughput (Kbytes/sec)","am62lxx_evm-fs: Read Throughput (Kbytes/sec)"

   "2000000","110345.39 (min 108145.21, max 116612.10)","174996.93 (min 174297.87, max 175229.95)"
   "4000000","125449.14 (min 123886.58, max 129262.33)","178086.96"

*****
MMCSD
*****

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

MMC EXT4 FIO 1G
===============

.. csv-table:: MMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

   "1m","42.53 (min 42.20, max 43.00)","4.24 (min 3.65, max 4.69)","86.53 (min 84.70, max 87.80)","5.81 (min 5.28, max 6.53)"
   "4m","41.60 (min 40.40, max 43.10)","2.96 (min 2.57, max 3.31)","85.52 (min 82.00, max 87.30)","3.42 (min 3.04, max 3.90)"
   "4k","2.78 (min 2.75, max 2.82)","7.48 (min 6.91, max 7.86)","12.93 (min 12.90, max 13.00)","11.75 (min 11.08, max 12.24)"
   "256k","38.67 (min 37.50, max 40.60)","6.42 (min 5.62, max 7.03)","83.37 (min 83.10, max 84.00)","6.92 (min 5.93, max 7.71)"

MMC RAW FIO 1G
==============

.. csv-table:: MMC RAW FIO 1G
   :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

   "1m","44.36 (min 41.80, max 45.70)","3.75 (min 3.19, max 4.18)","87.77 (min 87.60, max 87.90)","5.46 (min 4.52, max 6.18)"
   "4m","43.59 (min 41.00, max 45.40)","2.93 (min 2.51, max 3.30)","87.89 (min 87.80, max 88.00)","3.49 (min 3.02, max 4.04)"
   "4k","2.79 (min 2.77, max 2.81)","5.65 (min 4.76, max 6.67)","13.01 (min 12.90, max 13.10)","10.56 (min 9.22, max 12.01)"
   "256k","39.64 (min 35.80, max 41.50)","5.45 (min 4.43, max 6.38)","83.66 (min 83.40, max 83.90)","6.68 (min 5.40, max 7.50)"

MMC EXT4
========

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

   "102400","10.60 (min 10.46, max 10.92)","2.36 (min 1.49, max 3.29)","10.49 (min 10.28, max 10.83)","3.29 (min 2.66, max 3.82)"
   "262144","10.66 (min 10.19, max 10.97)","1.99 (min 1.23, max 2.83)","10.87 (min 10.79, max 10.98)","2.62 (min 2.06, max 3.71)"
   "524288","10.63 (min 10.12, max 11.05)","1.91 (min 1.11, max 2.68)","11.02 (min 10.85, max 11.38)","2.14 (min 1.68, max 3.04)"
   "1048576","10.98 (min 10.58, max 11.19)","2.01 (min 1.13, max 3.36)","11.74 (min 11.00, max 11.89)","2.40 (min 1.76, max 3.07)"
   "5242880","10.96 (min 10.42, max 11.16)","1.96 (min 1.23, max 2.92)","11.91 (min 11.86, max 11.93)","2.40 (min 1.71, max 3.06)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

***********
UBoot MMCSD
***********

UBOOT MMCSD FAT
===============

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","am62lxx_evm-fs: Write Throughput (Kbytes/sec)","am62lxx_evm-fs: Read Throughput (Kbytes/sec)"

   "400000","32341.56 (min 18875.58, max 39384.62)","82198.64 (min 81920.00, max 83591.84)"
   "800000","42188.82 (min 34276.15, max 46545.45)","87308.41 (min 86231.58, max 88086.02)"
   "1000000","43076.24 (min 40255.53, max 46811.43)","89530.94 (min 89043.48, max 90021.98)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

**********
USB Driver
**********

USB Device Controller
=====================

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
   :header: "Number of Blocks","am62lxx_evm-fs: Throughput (MB/sec)"

   "150","37.39 (min 31.20, max 41.90)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
   :header: "Number of Blocks","am62lxx_evm-fs: Throughput (MB/sec)"

   "150","34.06 (min 27.40, max 39.40)"

*************
CRYPTO Driver
*************

OpenSSL Performance
===================

.. csv-table:: OpenSSL Performance
   :header: "Algorithm","Buffer Size (in bytes)","am62lxx_evm-fs: throughput (KBytes/Sec)"

   "aes-128-cbc","1024","816378.03 (min 814629.55, max 817896.45)"
   "aes-128-cbc","16","87824.04 (min 86654.27, max 89015.29)"
   "aes-128-cbc","16384","938242.50 (min 936787.97, max 939529.56)"
   "aes-128-cbc","256","578595.16 (min 575426.99, max 581820.59)"
   "aes-128-cbc","64","275083.25 (min 272185.54, max 277948.29)"
   "aes-128-cbc","8192","930254.39 (min 929417.90, max 931015.34)"
   "aes-128-ecb","1024","896853.79 (min 894076.25, max 898568.87)"
   "aes-128-ecb","16","94466.41 (min 92570.83, max 95450.29)"
   "aes-128-ecb","16384","1067124.51 (min 1063381.67, max 1069498.37)"
   "aes-128-ecb","256","595149.10 (min 589436.84, max 598318.51)"
   "aes-128-ecb","64","259881.40 (min 256024.98, max 261730.09)"
   "aes-128-ecb","8192","1056312.43 (min 1055337.13, max 1057046.53)"
   "aes-192-cbc","1024","632689.55 (min 630571.35, max 634228.74)"
   "aes-192-cbc","16","84825.58 (min 83401.81, max 85565.78)"
   "aes-192-cbc","16384","704831.49 (min 697308.50, max 706658.30)"
   "aes-192-cbc","256","478630.20 (min 475369.22, max 481316.95)"
   "aes-192-cbc","64","249804.17 (min 246430.57, max 251667.97)"
   "aes-192-cbc","8192","701065.44 (min 700683.61, max 701333.50)"
   "aes-192-ecb","1024","796321.56 (min 796133.38, max 796556.63)"
   "aes-192-ecb","16","91392.11 (min 91178.70, max 91498.90)"
   "aes-192-ecb","16384","928700.64 (min 926706.35, max 929770.15)"
   "aes-192-ecb","256","546606.24 (min 545964.63, max 546986.24)"
   "aes-192-ecb","64","247006.95 (min 246791.49, max 247168.28)"
   "aes-192-ecb","8192","919587.95 (min 918978.56, max 919958.87)"
   "aes-256-cbc","1024","532843.98 (min 532625.75, max 533049.34)"
   "aes-256-cbc","16","83407.59 (min 83351.01, max 83443.17)"
   "aes-256-cbc","16384","582615.95 (min 582260.05, max 582849.88)"
   "aes-256-cbc","256","420241.74 (min 418515.37, max 420708.61)"
   "aes-256-cbc","64","233584.28 (min 232648.43, max 233902.14)"
   "aes-256-cbc","8192","579172.12 (min 578934.10, max 579491.16)"
   "aes-256-ecb","1024","702728.48 (min 699652.10, max 704730.11)"
   "aes-256-ecb","16","86654.84 (min 85879.63, max 88143.87)"
   "aes-256-ecb","16384","808444.81 (min 807834.97, max 808992.77)"
   "aes-256-ecb","256","486982.36 (min 484331.43, max 490064.55)"
   "aes-256-ecb","64","231141.85 (min 229839.70, max 233926.14)"
   "aes-256-ecb","8192","801233.58 (min 801016.49, max 801532.59)"
   "des3","1024","4559.76 (min 4557.48, max 4561.58)"
   "des3","16","4316.06 (min 4309.71, max 4319.09)"
   "des3","16384","4564.76 (min 4560.21, max 4565.67)"
   "des3","256","4546.86 (min 4545.71, max 4548.61)"
   "des3","64","4498.02 (min 4497.02, max 4499.54)"
   "des3","8192","4564.31 (min 4562.94, max 4565.67)"
   "md5","1024","142136.60 (min 141753.00, max 142520.66)"
   "md5","16","10086.57 (min 9970.07, max 10168.25)"
   "md5","16384","179477.62 (min 179257.34, max 179645.10)"
   "md5","256","85291.55 (min 83521.45, max 85973.76)"
   "md5","64","32994.58 (min 32676.27, max 33244.97)"
   "md5","8192","176296.39 (min 175538.18, max 176581.29)"
   "sha1","1024","324823.04 (min 324385.79, max 325552.81)"
   "sha1","16","11499.90 (min 11465.39, max 11560.74)"
   "sha1","16384","556979.54 (min 555892.74, max 557689.51)"
   "sha1","256","139494.27 (min 139028.39, max 139944.62)"
   "sha1","64","42429.95 (min 42292.54, max 42603.52)"
   "sha1","8192","532012.15 (min 531357.70, max 532534.61)"
   "sha224","1024","320532.08 (min 314424.32, max 323801.43)"
   "sha224","16","12026.96 (min 11445.43, max 12324.22)"
   "sha224","16384","528150.98 (min 527095.13, max 528848.21)"
   "sha224","256","143043.93 (min 137978.71, max 145343.74)"
   "sha224","64","44282.12 (min 42374.83, max 45217.81)"
   "sha224","8192","506436.27 (min 505055.91, max 508073.30)"
   "sha256","1024","320728.12 (min 314722.65, max 324295.34)"
   "sha256","16","12047.68 (min 11513.81, max 12361.39)"
   "sha256","16384","528697.12 (min 527406.42, max 529661.95)"
   "sha256","256","142709.66 (min 138010.20, max 145583.62)"
   "sha256","64","44283.56 (min 42402.88, max 45450.30)"
   "sha256","8192","506941.44 (min 505126.91, max 508048.73)"
   "sha512","1024","99816.56 (min 98935.13, max 100230.14)"
   "sha512","16","6963.13 (min 6828.02, max 7055.93)"
   "sha512","16384","126721.14 (min 126681.09, max 126790.31)"
   "sha512","256","59536.51 (min 58972.50, max 59897.26)"
   "sha512","64","27566.62 (min 27237.61, max 27812.52)"
   "sha512","8192","124410.08 (min 123770.20, max 124633.09)"

.. csv-table:: OpenSSL CPU Load
   :header: "Algorithm","am62lxx_evm-fs: CPU Load"

   "aes-128-cbc","99.00"
   "aes-128-ecb","99.00"
   "aes-192-cbc","99.00"
   "aes-192-ecb","99.00"
   "aes-256-cbc","99.00"
   "aes-256-ecb","99.00"
   "des3","99.00"
   "md5","99.00"
   "sha1","99.00"
   "sha224","99.00"
   "sha256","99.00"
   "sha386","80.83 (min 78.00, max 85.00)"
   "sha512","99.00"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc
