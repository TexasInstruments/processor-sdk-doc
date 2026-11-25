
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
   :header: "Benchmarks","am62dxx_evm-fs: perf"

   "af_unix_sock_stream_latency (microsec)","28.78 (min 22.90, max 34.62)"
   "af_unix_socket_stream_bandwidth (mb\s)","1114.82 (min 945.99, max 1203.24)"
   "bw_file_rd-io-1mb (mb/s)","1353.10 (min 1163.18, max 1448.75)"
   "bw_file_rd-o2c-1mb (mb/s)","654.81 (min 515.73, max 732.20)"
   "bw_mem-bcopy-16mb (mb/s)","1825.91 (min 1407.09, max 2060.79)"
   "bw_mem-bcopy-1mb (mb/s)","1914.72 (min 1468.97, max 2202.24)"
   "bw_mem-bcopy-2mb (mb/s)","1685.55 (min 1345.67, max 1878.29)"
   "bw_mem-bcopy-4mb (mb/s)","1747.79 (min 1391.06, max 1991.70)"
   "bw_mem-bcopy-8mb (mb/s)","1759.11 (min 1381.45, max 2028.65)"
   "bw_mem-bzero-16mb (mb/s)","7824.12 (min 7162.04, max 8128.70)"
   "bw_mem-bzero-1mb (mb/s)","4864.48 (min 1468.97, max 8134.49)"
   "bw_mem-bzero-2mb (mb/s)","4743.16 (min 1345.67, max 8128.64)"
   "bw_mem-bzero-4mb (mb/s)","4774.47 (min 1391.06, max 8127.33)"
   "bw_mem-bzero-8mb (mb/s)","4790.11 (min 1381.45, max 8127.33)"
   "bw_mem-cp-16mb (mb/s)","844.19 (min 675.08, max 927.86)"
   "bw_mem-cp-1mb (mb/s)","4447.41 (min 670.35, max 8416.22)"
   "bw_mem-cp-2mb (mb/s)","4380.83 (min 638.26, max 8251.12)"
   "bw_mem-cp-4mb (mb/s)","4368.15 (min 690.61, max 8199.52)"
   "bw_mem-cp-8mb (mb/s)","4374.23 (min 705.84, max 8167.43)"
   "bw_mem-fcp-16mb (mb/s)","1610.03 (min 1287.52, max 1812.42)"
   "bw_mem-fcp-1mb (mb/s)","4694.62 (min 1288.66, max 8134.49)"
   "bw_mem-fcp-2mb (mb/s)","4652.04 (min 1214.51, max 8128.64)"
   "bw_mem-fcp-4mb (mb/s)","4684.16 (min 1294.29, max 8127.33)"
   "bw_mem-fcp-8mb (mb/s)","4718.73 (min 1267.63, max 8127.33)"
   "bw_mem-frd-16mb (mb/s)","1870.88 (min 1513.86, max 2076.03)"
   "bw_mem-frd-1mb (mb/s)","1755.99 (min 1288.66, max 2102.04)"
   "bw_mem-frd-2mb (mb/s)","1643.37 (min 1214.51, max 1954.27)"
   "bw_mem-frd-4mb (mb/s)","1686.88 (min 1294.29, max 2039.78)"
   "bw_mem-frd-8mb (mb/s)","1721.58 (min 1267.63, max 2062.39)"
   "bw_mem-fwr-16mb (mb/s)","7837.47 (min 7168.46, max 8148.02)"
   "bw_mem-fwr-1mb (mb/s)","5010.66 (min 1606.43, max 8416.22)"
   "bw_mem-fwr-2mb (mb/s)","4860.65 (min 1489.48, max 8251.12)"
   "bw_mem-fwr-4mb (mb/s)","4840.14 (min 1475.20, max 8199.52)"
   "bw_mem-fwr-8mb (mb/s)","4840.69 (min 1536.98, max 8167.43)"
   "bw_mem-rd-16mb (mb/s)","1905.30 (min 1575.27, max 2143.62)"
   "bw_mem-rd-1mb (mb/s)","1730.84 (min 1070.85, max 2445.45)"
   "bw_mem-rd-2mb (mb/s)","1561.68 (min 1004.69, max 2132.58)"
   "bw_mem-rd-4mb (mb/s)","1682.37 (min 1195.28, max 2135.61)"
   "bw_mem-rd-8mb (mb/s)","1734.65 (min 1266.83, max 2140.75)"
   "bw_mem-rdwr-16mb (mb/s)","1721.17 (min 1376.70, max 1921.92)"
   "bw_mem-rdwr-1mb (mb/s)","1020.95 (min 670.35, max 1367.05)"
   "bw_mem-rdwr-2mb (mb/s)","988.03 (min 638.26, max 1293.45)"
   "bw_mem-rdwr-4mb (mb/s)","1108.64 (min 690.61, max 1609.98)"
   "bw_mem-rdwr-8mb (mb/s)","1228.24 (min 705.84, max 1830.66)"
   "bw_mem-wr-16mb (mb/s)","1679.16 (min 1395.43, max 1863.50)"
   "bw_mem-wr-1mb (mb/s)","1240.90 (min 1070.85, max 1399.83)"
   "bw_mem-wr-2mb (mb/s)","1173.31 (min 1000.50, max 1331.78)"
   "bw_mem-wr-4mb (mb/s)","1392.45 (min 1033.32, max 1609.98)"
   "bw_mem-wr-8mb (mb/s)","1561.57 (min 1266.83, max 1830.66)"
   "bw_mmap_rd-mo-1mb (mb/s)","2063.00 (min 1640.54, max 2323.33)"
   "bw_mmap_rd-o2c-1mb (mb/s)","689.20 (min 547.45, max 841.89)"
   "bw_pipe (mb/s)","723.11 (min 685.63, max 753.72)"
   "bw_unix (mb/s)","1114.82 (min 945.99, max 1203.24)"
   "lat_connect (us)","72.12 (min 70.99, max 73.11)"
   "lat_ctx-2-128k (us)","7.92 (min 7.30, max 9.60)"
   "lat_ctx-2-256k (us)","28.07 (min 5.34, max 46.31)"
   "lat_ctx-4-128k (us)","24.34 (min 19.90, max 33.86)"
   "lat_ctx-4-256k (us)","68.60 (min 5.63, max 128.66)"
   "lat_fs-0k (num_files)","247.86 (min 221.00, max 262.00)"
   "lat_fs-10k (num_files)","119.29 (min 109.00, max 132.00)"
   "lat_fs-1k (num_files)","176.71 (min 156.00, max 185.00)"
   "lat_fs-4k (num_files)","170.57 (min 160.00, max 185.00)"
   "lat_mem_rd-stride128-sz1000k (ns)","31.45 (min 28.17, max 38.25)"
   "lat_mem_rd-stride128-sz125k (ns)","5.58 (min 5.55, max 5.63)"
   "lat_mem_rd-stride128-sz250k (ns)","5.84 (min 5.83, max 5.85)"
   "lat_mem_rd-stride128-sz31k (ns)","2.94 (min 2.16, max 4.66)"
   "lat_mem_rd-stride128-sz50 (ns)","2.15"
   "lat_mem_rd-stride128-sz500k (ns)","11.68 (min 9.89, max 14.17)"
   "lat_mem_rd-stride128-sz62k (ns)","5.14 (min 4.54, max 5.26)"
   "lat_mmap-1m (us)","52.86 (min 49.00, max 58.00)"
   "lat_ops-double-add (ns)","2.86"
   "lat_ops-double-div (ns)","15.74 (min 15.74, max 15.75)"
   "lat_ops-double-mul (ns)","2.86 (min 2.86, max 2.87)"
   "lat_ops-float-add (ns)","2.86"
   "lat_ops-float-div (ns)","9.30"
   "lat_ops-float-mul (ns)","2.86"
   "lat_ops-int-add (ns)","0.72"
   "lat_ops-int-bit (ns)","0.48"
   "lat_ops-int-div (ns)","4.29 (min 4.29, max 4.30)"
   "lat_ops-int-mod (ns)","4.53 (min 4.53, max 4.54)"
   "lat_ops-int-mul (ns)","3.05 (min 3.04, max 3.10)"
   "lat_ops-int64-add (ns)","0.72"
   "lat_ops-int64-bit (ns)","0.48"
   "lat_ops-int64-div (ns)","6.80"
   "lat_ops-int64-mod (ns)","5.25"
   "lat_ops-int64-mul (ns)","3.54 (min 3.54, max 3.55)"
   "lat_pagefault (us)","0.46 (min 0.42, max 0.58)"
   "lat_pipe (us)","18.18 (min 17.96, max 18.38)"
   "lat_proc-exec (us)","710.04 (min 668.38, max 777.86)"
   "lat_proc-fork (us)","617.34 (min 577.44, max 675.13)"
   "lat_proc-proccall (us)","0.01"
   "lat_select (us)","32.03 (min 31.81, max 32.27)"
   "lat_sem (us)","2.45 (min 2.13, max 2.78)"
   "lat_sig-catch (us)","5.74 (min 5.66, max 5.86)"
   "lat_sig-install (us)","0.61 (min 0.60, max 0.63)"
   "lat_sig-prot (us)","0.63 (min 0.30, max 0.90)"
   "lat_syscall-fstat (us)","1.80 (min 1.69, max 1.83)"
   "lat_syscall-null (us)","0.38 (min 0.37, max 0.40)"
   "lat_syscall-open (us)","867.56 (min 156.65, max 4787.35)"
   "lat_syscall-read (us)","0.72 (min 0.71, max 0.74)"
   "lat_syscall-stat (us)","4.42 (min 4.23, max 4.62)"
   "lat_syscall-write (us)","0.68 (min 0.67, max 0.69)"
   "lat_tcp (us)","0.76"
   "lat_unix (us)","28.78 (min 22.90, max 34.62)"
   "latency_for_0.50_mb_block_size (nanosec)","11.68 (min 9.89, max 14.17)"
   "latency_for_1.00_mb_block_size (nanosec)","15.72 (min 0.00, max 38.25)"
   "pipe_bandwidth (mb\s)","723.11 (min 685.63, max 753.72)"
   "pipe_latency (microsec)","18.18 (min 17.96, max 18.38)"
   "procedure_call (microsec)","0.01"
   "select_on_200_tcp_fds (microsec)","32.03 (min 31.81, max 32.27)"
   "semaphore_latency (microsec)","2.45 (min 2.13, max 2.78)"
   "signal_handler_latency (microsec)","0.61 (min 0.60, max 0.63)"
   "signal_handler_overhead (microsec)","5.74 (min 5.66, max 5.86)"
   "tcp_ip_connection_cost_to_localhost (microsec)","72.12 (min 70.99, max 73.11)"
   "tcp_latency_using_localhost (microsec)","0.76"

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
   :header: "Benchmarks","am62dxx_evm-fs: perf"

   "cpu_clock (mhz)","1400.00"
   "dhrystone_per_mhz (dmips/mhz)","2.76 (min 2.70, max 2.80)"
   "dhrystone_per_second (dhrystonep)","6810344.63 (min 6666666.50, max 6896551.50)"

Whetstone
=========

Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

.. code-block:: console

    runWhetstone

.. csv-table:: Whetstone Benchmarks
   :header: "Benchmarks","am62dxx_evm-fs: perf"

   "whetstone (mips)","5625.00 (min 5000.00, max 10000.00)"

Linpack
=======

Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
   :header: "Benchmarks","am62dxx_evm-fs: perf"

   "linpack (kflops)","579843.13 (min 577176.00, max 582266.00)"

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
   :header: "Benchmarks","am62dxx_evm-fs: perf"

   "add (mb/s)","2568.74 (min 2112.20, max 2913.00)"
   "copy (mb/s)","3514.59 (min 2781.40, max 4052.20)"
   "scale (mb/s)","3323.38 (min 2712.50, max 3749.40)"
   "triad (mb/s)","2343.86 (min 2014.60, max 2581.30)"

CoreMarkPro
===========

CoreMark\ |reg|-Pro is a comprehensive, advanced processor benchmark that works
with and enhances the market-proven industry-standard EEMBC CoreMark\ |reg|
benchmark. While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the
entire processor, adding comprehensive support for multicore technology, a
combination of integer and floating-point workloads, and data sets for utilizing
larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
   :header: "Benchmarks","am62dxx_evm-fs: perf"

   "cjpeg-rose7-preset (workloads/)","41.93 (min 41.84, max 42.02)"
   "core (workloads/)","0.30"
   "coremark-pro ()","953.80 (min 941.41, max 959.42)"
   "linear_alg-mid-100x100-sp (workloads/)","14.68 (min 14.67, max 14.68)"
   "loops-all-mid-10k-sp (workloads/)","0.71 (min 0.70, max 0.72)"
   "nnet_test (workloads/)","1.08"
   "parser-125k (workloads/)","9.27 (min 9.17, max 9.35)"
   "radix2-big-64k (workloads/)","73.68 (min 68.63, max 77.00)"
   "sha-test (workloads/)","81.14 (min 80.65, max 81.30)"
   "zip-test (workloads/)","23.46 (min 23.26, max 23.81)"

.. csv-table:: CoreMarkProFourCore Benchmarks
   :header: "Benchmarks","am62dxx_evm-fs: perf"

   "cjpeg-rose7-preset (workloads/)","157.19 (min 153.85, max 158.73)"
   "core (workloads/)","1.17 (min 1.10, max 1.20)"
   "coremark-pro ()","2592.74 (min 2512.28, max 2660.24)"
   "linear_alg-mid-100x100-sp (workloads/)","56.27 (min 56.18, max 56.31)"
   "loops-all-mid-10k-sp (workloads/)","2.06 (min 1.95, max 2.18)"
   "nnet_test (workloads/)","3.59 (min 3.58, max 3.59)"
   "parser-125k (workloads/)","13.72 (min 13.47, max 13.89)"
   "radix2-big-64k (workloads/)","69.96 (min 59.64, max 76.96)"
   "sha-test (workloads/)","257.44 (min 217.39, max 263.16)"
   "zip-test (workloads/)","79.57 (min 74.07, max 83.33)"

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
   :header: "Benchmarks","am62dxx_evm-fs: perf"

   "4m-check (workloads/)","425.47 (min 387.90, max 450.94)"
   "4m-check-reassembly (workloads/)","167.56 (min 144.09, max 185.87)"
   "4m-check-reassembly-tcp (workloads/)","73.12 (min 67.20, max 77.16)"
   "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","34.31 (min 32.21, max 35.91)"
   "4m-check-reassembly-tcp-x264w2 (workloads/)","1.89 (min 1.86, max 1.92)"
   "4m-cmykw2 (workloads/)","246.86 (min 244.50, max 249.38)"
   "4m-cmykw2-rotatew2 (workloads/)","48.64 (min 46.30, max 50.76)"
   "4m-reassembly (workloads/)","146.02 (min 123.92, max 163.13)"
   "4m-rotatew2 (workloads/)","54.20 (min 51.65, max 55.74)"
   "4m-tcp-mixed (workloads/)","127.05 (min 123.08, max 130.08)"
   "4m-x264w2 (workloads/)","1.96 (min 1.93, max 1.99)"
   "empty-wld (workloads/)","1.00"
   "idct-4m (workloads/)","19.76 (min 19.75, max 19.77)"
   "idct-4mw1 (workloads/)","19.76 (min 19.74, max 19.77)"
   "ippktcheck-4m (workloads/)","425.72 (min 389.77, max 451.59)"
   "ippktcheck-4mw1 (workloads/)","426.46 (min 389.41, max 451.26)"
   "ipres-4m (workloads/)","107.09 (min 92.36, max 118.11)"
   "ipres-4mw1 (workloads/)","106.95 (min 92.25, max 117.83)"
   "md5-4m (workloads/)","28.25 (min 27.82, max 28.63)"
   "md5-4mw1 (workloads/)","28.15 (min 27.34, max 28.79)"
   "rgbcmyk-4m (workloads/)","64.25 (min 63.07, max 65.66)"
   "rgbcmyk-4mw1 (workloads/)","64.25 (min 63.11, max 65.66)"
   "rotate-4ms1 (workloads/)","25.59 (min 23.75, max 26.85)"
   "rotate-4ms1w1 (workloads/)","25.62 (min 23.83, max 26.88)"
   "rotate-4ms64 (workloads/)","25.88 (min 23.95, max 27.20)"
   "rotate-4ms64w1 (workloads/)","25.87 (min 23.89, max 27.20)"
   "x264-4mq (workloads/)","0.58 (min 0.57, max 0.58)"
   "x264-4mqw1 (workloads/)","0.58"

*********************
Boot-time Measurement
*********************

Boot media: MMCSD
=================

.. csv-table:: Linux boot time MMCSD
   :header: "Boot Configuration","am62dxx_evm-fs: Boot time in seconds: avg(min,max)"

   "Linux boot time from SD with default rootfs (20 boot cycles)","17.78 (min 16.97, max 19.20)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

***********************
Linux OSPI Flash Driver
***********************

.. rubric:: AM62DXX-EVM
   :name: am62dxx-evm-ospi

.. rubric:: UBIFS
   :name: am62dxx-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
   :header: "Buffer size (bytes)","am62dxx_evm-fs: Write UBIFS Throughput (Mbytes/sec)","am62dxx_evm-fs: Write UBIFS CPU Load (%)","am62dxx_evm-fs: Read UBIFS Throughput (Mbytes/sec)","am62dxx_evm-fs: Read UBIFS CPU Load (%)"

   "102400","0.18 (min 0.13, max 0.29)","28.20 (min 24.78, max 31.92)","28.20 (min 27.83, max 28.47)","7.10 (min 3.45, max 12.90)"
   "262144","0.14 (min 0.11, max 0.19)","28.69 (min 25.96, max 34.26)","28.06 (min 27.63, max 28.41)","9.62 (min 6.67, max 17.65)"
   "524288","0.14 (min 0.11, max 0.19)","28.83 (min 25.68, max 32.74)","27.87 (min 27.41, max 28.21)","8.71 (min 0.00, max 15.62)"
   "1048576","0.14 (min 0.11, max 0.19)","29.29 (min 26.31, max 33.00)","27.61 (min 27.24, max 27.96)","8.43 (min 3.45, max 12.50)"

.. rubric:: RAW
   :name: am62dxx-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
   :header: "File size (Mbytes)","am62dxx_evm-fs: Raw Read Throughput (Mbytes/sec)"

   "50","37.72 (min 37.31, max 37.88)"

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
   :header: "Buffer size (bytes)","am62dxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62dxx_evm-fs: Write EXT4 CPU Load (%)","am62dxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62dxx_evm-fs: Read EXT4 CPU Load (%)"

   "1m","79.41 (min 73.00, max 91.20)","1.47 (min 1.26, max 1.68)","128.14 (min 109.00, max 172.00)","1.45 (min 1.17, max 1.89)"
   "4m","84.07 (min 77.80, max 96.50)","1.76 (min 0.88, max 2.98)","124.99 (min 91.90, max 172.00)","1.12 (min 0.90, max 1.43)"
   "4k","23.37 (min 7.87, max 62.10)","7.21 (min 2.65, max 18.88)","66.36 (min 56.30, max 91.80)","15.81 (min 13.45, max 20.51)"
   "256k","72.91 (min 64.00, max 90.80)","1.71 (min 1.51, max 2.06)","114.74 (min 91.70, max 171.00)","1.90 (min 1.37, max 2.68)"

EMMC RAW FIO 1G
===============

.. csv-table:: EMMC RAW FIO 1G
   :header: "Buffer size (bytes)","am62dxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Write Raw CPU Load (%)","am62dxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Read Raw CPU Load (%)"

   "1m","84.29 (min 73.70, max 90.90)","1.39 (min 1.19, max 1.76)","150.88 (min 111.00, max 174.00)","1.67 (min 1.18, max 2.00)"
   "4m","90.13 (min 78.70, max 96.90)","1.44 (min 0.79, max 2.82)","148.53 (min 94.20, max 174.00)","1.24 (min 1.03, max 1.39)"
   "4k","43.01 (min 7.88, max 64.20)","10.11 (min 2.18, max 15.03)","78.34 (min 57.30, max 93.40)","16.31 (min 12.44, max 19.21)"
   "256k","80.59 (min 64.10, max 90.50)","1.72 (min 1.35, max 2.15)","143.30 (min 93.80, max 173.00)","2.17 (min 1.63, max 2.68)"

EMMC EXT4
=========

.. csv-table:: EMMC EXT4
   :header: "Buffer size (bytes)","am62dxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62dxx_evm-fs: Write EXT4 CPU Load (%)","am62dxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62dxx_evm-fs: Read EXT4 CPU Load (%)"

   "102400","79.95 (min 57.42, max 93.95)","3.90 (min 2.43, max 19.78)","142.30 (min 121.41, max 179.12)","4.91 (min 3.40, max 7.17)"
   "262144","74.21 (min 46.84, max 94.88)","2.27 (min 1.12, max 3.66)","122.36 (min 98.80, max 180.75)","3.42 (min 1.91, max 5.15)"
   "524288","72.09 (min 47.89, max 94.90)","2.27 (min 1.03, max 3.83)","134.82 (min 110.70, max 181.38)","3.91 (min 2.92, max 5.49)"
   "1048576","72.60 (min 49.28, max 93.80)","2.47 (min 1.17, max 5.70)","133.53 (min 95.63, max 182.00)","4.26 (min 3.20, max 5.63)"
   "5242880","72.55 (min 50.66, max 94.19)","2.36 (min 1.29, max 4.06)","136.13 (min 114.19, max 180.86)","4.99 (min 3.46, max 6.49)"

EMMC VFAT
=========

.. csv-table:: EMMC VFAT
   :header: "Buffer size (bytes)","am62dxx_evm-fs: Write VFAT Throughput (Mbytes/sec)","am62dxx_evm-fs: Write VFAT CPU Load (%)","am62dxx_evm-fs: Read VFAT Throughput (Mbytes/sec)","am62dxx_evm-fs: Read VFAT CPU Load (%)"

   "102400","35.39 (min 10.35, max 50.63)","5.99 (min 2.97, max 16.76)","147.11 (min 132.69, max 173.96)","7.69 (min 6.07, max 10.00)"
   "262144","43.51 (min 12.13, max 63.07)","4.57 (min 1.99, max 7.29)","168.62 (min 162.36, max 176.05)","8.93 (min 7.60, max 11.24)"
   "524288","47.72 (min 12.48, max 72.81)","5.19 (min 3.17, max 7.33)","170.50 (min 167.08, max 175.74)","8.25 (min 7.29, max 9.60)"
   "1048576","47.83 (min 11.84, max 75.35)","4.79 (min 3.47, max 7.08)","167.82 (min 158.36, max 175.53)","9.19 (min 8.02, max 10.44)"
   "5242880","51.27 (min 12.04, max 81.83)","4.94 (min 3.54, max 7.48)","169.33 (min 161.55, max 175.28)","9.67 (min 8.53, max 10.97)"

*****************
UBoot EMMC Driver
*****************

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","am62dxx_evm-fs: Write Throughput (Kbytes/sec)","am62dxx_evm-fs: Read Throughput (Kbytes/sec)"

   "2000000","98404.52 (min 96093.84, max 101448.92)","169588.77 (min 157538.46, max 172463.16)"
   "4000000","97468.94 (min 95533.53, max 99598.78)","170201.31 (min 148607.71, max 175229.95)"

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
   :header: "Buffer size (bytes)","am62dxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62dxx_evm-fs: Write EXT4 CPU Load (%)","am62dxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62dxx_evm-fs: Read EXT4 CPU Load (%)"

   "1m","42.70 (min 41.70, max 43.50)","1.08 (min 0.98, max 1.18)","86.91 (min 85.60, max 88.20)","1.32 (min 1.15, max 1.50)"
   "4m","42.07 (min 41.60, max 42.90)","0.75 (min 0.69, max 0.82)","85.13 (min 82.80, max 87.50)","0.96 (min 0.87, max 1.13)"
   "4k","2.83 (min 2.79, max 2.88)","1.68 (min 1.58, max 1.76)","13.20 (min 13.00, max 14.10)","4.09 (min 3.88, max 4.63)"
   "256k","39.16 (min 37.50, max 40.60)","1.38 (min 1.29, max 1.54)","84.44 (min 83.80, max 85.10)","1.57 (min 1.45, max 1.73)"

MMC RAW FIO 1G
==============

.. csv-table:: MMC RAW FIO 1G
   :header: "Buffer size (bytes)","am62dxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Write Raw CPU Load (%)","am62dxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Read Raw CPU Load (%)"

   "1m","43.01 (min 42.20, max 44.20)","0.99 (min 0.87, max 1.15)","88.20 (min 88.10, max 88.30)","1.23 (min 1.18, max 1.32)"
   "4m","42.87 (min 42.20, max 43.60)","0.77 (min 0.70, max 0.85)","88.16 (min 88.00, max 88.30)","0.95 (min 0.87, max 1.03)"
   "4k","2.82 (min 2.80, max 2.84)","1.41 (min 1.33, max 1.55)","13.03 (min 13.00, max 13.10)","3.70 (min 3.58, max 3.82)"
   "256k","37.06 (min 36.30, max 38.60)","1.12 (min 0.95, max 1.26)","84.34 (min 84.30, max 84.50)","1.56 (min 1.41, max 1.68)"

MMC EXT4
========

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","am62dxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Write Raw CPU Load (%)","am62dxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62dxx_evm-fs: Read Raw CPU Load (%)"

   "102400","10.83 (min 10.66, max 11.18)","0.57 (min 0.40, max 0.82)","10.98 (min 10.67, max 11.56)","0.50 (min 0.42, max 0.58)"
   "262144","10.78 (min 10.11, max 11.09)","0.46 (min 0.25, max 0.88)","11.17 (min 11.02, max 11.34)","0.49 (min 0.40, max 0.63)"
   "524288","10.77 (min 10.16, max 11.07)","0.46 (min 0.28, max 0.97)","11.36 (min 11.06, max 11.52)","0.45 (min 0.35, max 0.58)"
   "1048576","10.93 (min 10.61, max 11.29)","0.41 (min 0.28, max 0.64)","11.39 (min 11.07, max 12.03)","0.53 (min 0.40, max 0.90)"
   "5242880","10.98 (min 10.27, max 11.28)","0.42 (min 0.30, max 0.67)","12.02 (min 12.01, max 12.03)","0.58 (min 0.49, max 0.86)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

***********
UBoot MMCSD
***********

UBOOT MMCSD FAT
===============

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","am62dxx_evm-fs: Write Throughput (Kbytes/sec)","am62dxx_evm-fs: Read Throughput (Kbytes/sec)"

   "400000","37212.90 (min 33851.24, max 39009.52)","82158.83 (min 81920.00, max 83591.84)"
   "800000","43904.79 (min 42666.67, max 45765.36)","87282.81 (min 87148.94, max 88086.02)"
   "1000000","45395.58 (min 41478.48, max 47489.86)","89601.09 (min 89043.48, max 90021.98)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

**********
USB Driver
**********

USB Device Controller
=====================

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
   :header: "Number of Blocks","am62dxx_evm-fs: Throughput (MB/sec)"

   "150","39.97 (min 38.30, max 42.10)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
   :header: "Number of Blocks","am62dxx_evm-fs: Throughput (MB/sec)"

   "150","37.03 (min 32.10, max 41.60)"

*************
CRYPTO Driver
*************

OpenSSL Performance
===================

.. csv-table:: OpenSSL Performance
   :header: "Algorithm","Buffer Size (in bytes)","am62dxx_evm-fs: throughput (KBytes/Sec)"

   "aes-128-cbc","1024","23808.46 (min 22987.78, max 24523.78)"
   "aes-128-cbc","16","468.63 (min 445.33, max 483.83)"
   "aes-128-cbc","16384","87050.62 (min 86043.31, max 88402.60)"
   "aes-128-cbc","256","7693.26 (min 7320.66, max 7983.45)"
   "aes-128-cbc","64","2063.46 (min 1952.32, max 2141.67)"
   "aes-128-cbc","8192","74428.26 (min 73476.78, max 75483.82)"
   "aes-128-ecb","1024","24387.05 (min 23629.14, max 25023.15)"
   "aes-128-ecb","16","480.66 (min 458.92, max 498.21)"
   "aes-128-ecb","16384","89872.31 (min 88195.07, max 91242.50)"
   "aes-128-ecb","256","7941.63 (min 7584.68, max 8189.78)"
   "aes-128-ecb","64","2117.79 (min 2039.25, max 2186.52)"
   "aes-128-ecb","8192","76546.05 (min 75330.90, max 77755.73)"
   "aes-192-cbc","1024","23292.17 (min 22416.38, max 24275.63)"
   "aes-192-cbc","16","468.74 (min 445.98, max 486.83)"
   "aes-192-cbc","16384","78311.88 (min 77392.55, max 79899.31)"
   "aes-192-cbc","256","7633.20 (min 7278.68, max 7979.52)"
   "aes-192-cbc","64","2066.09 (min 1956.29, max 2148.67)"
   "aes-192-cbc","8192","67912.89 (min 66704.73, max 69637.46)"
   "aes-192-ecb","1024","23823.93 (min 22954.33, max 24535.04)"
   "aes-192-ecb","16","479.76 (min 457.38, max 496.51)"
   "aes-192-ecb","16384","80981.26 (min 79822.85, max 81799.85)"
   "aes-192-ecb","256","7866.48 (min 7479.55, max 8165.97)"
   "aes-192-ecb","64","2119.03 (min 2029.25, max 2184.64)"
   "aes-192-ecb","8192","70268.55 (min 69468.16, max 71035.56)"
   "aes-256-cbc","1024","22759.20 (min 21817.34, max 23763.97)"
   "aes-256-cbc","16","468.09 (min 448.43, max 487.14)"
   "aes-256-cbc","16384","71610.82 (min 70352.90, max 72570.20)"
   "aes-256-cbc","256","7594.56 (min 7278.93, max 7896.23)"
   "aes-256-cbc","64","2063.05 (min 1967.47, max 2151.85)"
   "aes-256-cbc","8192","62850.24 (min 62199.13, max 63971.33)"
   "aes-256-ecb","1024","23341.74 (min 22609.92, max 23826.43)"
   "aes-256-ecb","16","479.23 (min 459.42, max 492.28)"
   "aes-256-ecb","16384","73690.98 (min 73154.56, max 74181.29)"
   "aes-256-ecb","256","7777.00 (min 7453.44, max 8035.75)"
   "aes-256-ecb","64","2110.04 (min 2033.32, max 2167.70)"
   "aes-256-ecb","8192","64524.44 (min 63668.22, max 65385.81)"
   "sha256","1024","31631.21 (min 29681.66, max 32247.47)"
   "sha256","16","523.59 (min 490.75, max 533.66)"
   "sha256","16384","275324.02 (min 266272.77, max 277768.87)"
   "sha256","256","8211.89 (min 7701.76, max 8369.07)"
   "sha256","64","2071.99 (min 1938.92, max 2112.85)"
   "sha256","8192","180429.10 (min 172400.64, max 182523.22)"
   "sha512","1024","26615.05 (min 25200.30, max 27062.61)"
   "sha512","16","513.29 (min 481.13, max 522.82)"
   "sha512","16384","110775.86 (min 108789.76, max 111558.66)"
   "sha512","256","7749.43 (min 7271.34, max 7902.55)"
   "sha512","64","2052.83 (min 1923.29, max 2092.93)"
   "sha512","8192","91277.08 (min 88850.43, max 92222.81)"

.. csv-table:: OpenSSL CPU Load
   :header: "Algorithm","am62dxx_evm-fs: CPU Load"

   "aes-128-cbc","31.67 (min 31.00, max 32.00)"
   "aes-128-ecb","33.00"
   "aes-192-cbc","31.67 (min 31.00, max 32.00)"
   "aes-192-ecb","32.33 (min 31.00, max 33.00)"
   "aes-256-cbc","31.11 (min 31.00, max 32.00)"
   "aes-256-ecb","31.89 (min 31.00, max 32.00)"
   "sha256","97.33 (min 96.00, max 98.00)"
   "sha512","97.33 (min 96.00, max 98.00)"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc