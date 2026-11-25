
=================================
 Linux 12.02.00 Performance Guide
=================================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
| AM437x-gpevm   | AM437x-gpevm Evaluation Module rev 1.5A with ARM running at 1000MHz, DDR3-400 (400MHz/800 MT/S), TMDSEVM437X   |
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
   :header: "Benchmarks","am43xx-gpevm: perf"

   "af_unix_sock_stream_latency (microsec)","44.28 (min 42.93, max 45.49)"
   "af_unix_socket_stream_bandwidth (mb\s)","205.30 (min 176.76, max 213.66)"
   "bw_file_rd-io-1mb (mb/s)","196.92 (min 193.01, max 202.31)"
   "bw_file_rd-o2c-1mb (mb/s)","158.67 (min 156.81, max 162.07)"
   "bw_mem-bcopy-16mb (mb/s)","196.76 (min 195.44, max 197.94)"
   "bw_mem-bcopy-1mb (mb/s)","199.91 (min 198.33, max 200.96)"
   "bw_mem-bcopy-2mb (mb/s)","198.41 (min 196.46, max 199.22)"
   "bw_mem-bcopy-4mb (mb/s)","198.39 (min 197.01, max 199.26)"
   "bw_mem-bcopy-8mb (mb/s)","196.48 (min 193.33, max 197.83)"
   "bw_mem-bzero-16mb (mb/s)","671.99 (min 670.78, max 672.72)"
   "bw_mem-bzero-1mb (mb/s)","437.08 (min 198.33, max 674.76)"
   "bw_mem-bzero-2mb (mb/s)","435.59 (min 196.46, max 674.08)"
   "bw_mem-bzero-4mb (mb/s)","435.72 (min 197.01, max 673.40)"
   "bw_mem-bzero-8mb (mb/s)","434.59 (min 193.33, max 673.00)"
   "bw_mem-cp-16mb (mb/s)","199.33 (min 197.50, max 200.53)"
   "bw_mem-cp-1mb (mb/s)","437.62 (min 200.48, max 675.45)"
   "bw_mem-cp-2mb (mb/s)","436.99 (min 200.52, max 673.97)"
   "bw_mem-cp-4mb (mb/s)","436.79 (min 199.83, max 673.40)"
   "bw_mem-cp-8mb (mb/s)","435.74 (min 197.43, max 672.89)"
   "bw_mem-fcp-16mb (mb/s)","241.39 (min 240.44, max 242.83)"
   "bw_mem-fcp-1mb (mb/s)","459.51 (min 242.37, max 674.76)"
   "bw_mem-fcp-2mb (mb/s)","458.02 (min 241.93, max 674.08)"
   "bw_mem-fcp-4mb (mb/s)","457.40 (min 240.72, max 673.40)"
   "bw_mem-fcp-8mb (mb/s)","456.77 (min 239.94, max 673.00)"
   "bw_mem-frd-16mb (mb/s)","293.06 (min 276.76, max 305.01)"
   "bw_mem-frd-1mb (mb/s)","243.60 (min 230.02, max 246.67)"
   "bw_mem-frd-2mb (mb/s)","255.16 (min 241.93, max 272.18)"
   "bw_mem-frd-4mb (mb/s)","248.15 (min 240.72, max 258.53)"
   "bw_mem-frd-8mb (mb/s)","266.86 (min 239.94, max 305.40)"
   "bw_mem-fwr-16mb (mb/s)","672.36 (min 671.51, max 673.03)"
   "bw_mem-fwr-1mb (mb/s)","458.39 (min 230.02, max 675.45)"
   "bw_mem-fwr-2mb (mb/s)","470.07 (min 263.40, max 673.97)"
   "bw_mem-fwr-4mb (mb/s)","463.76 (min 250.41, max 673.40)"
   "bw_mem-fwr-8mb (mb/s)","482.43 (min 283.93, max 672.89)"
   "bw_mem-rd-16mb (mb/s)","409.64 (min 407.60, max 412.73)"
   "bw_mem-rd-1mb (mb/s)","335.99 (min 271.52, max 403.12)"
   "bw_mem-rd-2mb (mb/s)","339.72 (min 268.60, max 412.12)"
   "bw_mem-rd-4mb (mb/s)","339.75 (min 269.36, max 412.37)"
   "bw_mem-rd-8mb (mb/s)","339.14 (min 261.82, max 411.99)"
   "bw_mem-rdwr-16mb (mb/s)","247.80 (min 246.74, max 248.20)"
   "bw_mem-rdwr-1mb (mb/s)","226.07 (min 200.48, max 252.02)"
   "bw_mem-rdwr-2mb (mb/s)","224.41 (min 200.52, max 248.60)"
   "bw_mem-rdwr-4mb (mb/s)","224.13 (min 199.83, max 248.43)"
   "bw_mem-rdwr-8mb (mb/s)","223.83 (min 197.43, max 248.79)"
   "bw_mem-wr-16mb (mb/s)","270.15 (min 269.46, max 271.29)"
   "bw_mem-wr-1mb (mb/s)","261.74 (min 250.66, max 272.48)"
   "bw_mem-wr-2mb (mb/s)","258.77 (min 247.49, max 270.01)"
   "bw_mem-wr-4mb (mb/s)","258.83 (min 246.03, max 270.69)"
   "bw_mem-wr-8mb (mb/s)","258.67 (min 247.42, max 271.09)"
   "bw_mmap_rd-mo-1mb (mb/s)","197.30 (min 194.48, max 199.04)"
   "bw_mmap_rd-o2c-1mb (mb/s)","149.11 (min 147.32, max 150.65)"
   "bw_pipe (mb/s)","347.95 (min 317.37, max 382.82)"
   "bw_unix (mb/s)","205.30 (min 176.76, max 213.66)"
   "lat_connect (us)","81.07 (min 78.71, max 87.54)"
   "lat_ctx-2-128k (us)","5.54 (min 1.63, max 12.99)"
   "lat_ctx-2-256k (us)","24.04 (min 4.00, max 86.61)"
   "lat_ctx-4-128k (us)","13.09 (min 3.05, max 25.32)"
   "lat_ctx-4-256k (us)","0.00"
   "lat_fs-0k (num_files)","207.43 (min 186.00, max 240.00)"
   "lat_fs-10k (num_files)","77.00 (min 68.00, max 84.00)"
   "lat_fs-1k (num_files)","125.00 (min 122.00, max 129.00)"
   "lat_fs-4k (num_files)","121.14 (min 108.00, max 130.00)"
   "lat_mem_rd-stride128-sz1000k (ns)","99.61 (min 99.32, max 100.12)"
   "lat_mem_rd-stride128-sz125k (ns)","16.00 (min 15.89, max 16.12)"
   "lat_mem_rd-stride128-sz250k (ns)","38.23 (min 33.47, max 48.76)"
   "lat_mem_rd-stride128-sz31k (ns)","8.02 (min 4.01, max 12.81)"
   "lat_mem_rd-stride128-sz50 (ns)","4.00 (min 4.00, max 4.01)"
   "lat_mem_rd-stride128-sz500k (ns)","91.20 (min 86.60, max 92.84)"
   "lat_mem_rd-stride128-sz62k (ns)","16.40 (min 15.30, max 17.07)"
   "lat_mmap-1m (us)","75.14 (min 69.00, max 86.00)"
   "lat_ops-double-add (ns)","5.03 (min 5.02, max 5.04)"
   "lat_ops-double-div (ns)","25.15 (min 25.11, max 25.17)"
   "lat_ops-double-mul (ns)","7.04 (min 7.03, max 7.05)"
   "lat_ops-float-add (ns)","5.04 (min 5.03, max 5.05)"
   "lat_ops-float-div (ns)","15.12 (min 15.07, max 15.21)"
   "lat_ops-float-mul (ns)","6.04 (min 6.03, max 6.05)"
   "lat_ops-int-add (ns)","1.01"
   "lat_ops-int-bit (ns)","0.76"
   "lat_ops-int-div (ns)","96.09 (min 95.94, max 96.22)"
   "lat_ops-int-mod (ns)","21.89 (min 21.88, max 21.91)"
   "lat_ops-int-mul (ns)","4.15 (min 4.14, max 4.16)"
   "lat_ops-int64-add (ns)","1.11"
   "lat_ops-int64-bit (ns)","0.67 (min 0.67, max 0.68)"
   "lat_ops-int64-div (ns)","185.30 (min 183.90, max 186.14)"
   "lat_ops-int64-mod (ns)","45.28 (min 45.09, max 45.65)"
   "lat_ops-int64-mul (ns)","4.16 (min 4.15, max 4.17)"
   "lat_pagefault (us)","1.55 (min 1.51, max 1.63)"
   "lat_pipe (us)","29.21 (min 28.97, max 29.57)"
   "lat_proc-exec (us)","1351.32 (min 1315.75, max 1391.00)"
   "lat_proc-fork (us)","1178.77 (min 1123.80, max 1268.20)"
   "lat_proc-proccall (us)","0.01"
   "lat_select (us)","36.03 (min 35.71, max 36.23)"
   "lat_sem (us)","8.61 (min 8.41, max 9.33)"
   "lat_sig-catch (us)","6.16 (min 5.96, max 6.70)"
   "lat_sig-install (us)","0.99 (min 0.97, max 1.01)"
   "lat_sig-prot (us)","0.75 (min 0.63, max 0.96)"
   "lat_syscall-fstat (us)","2.21 (min 2.16, max 2.28)"
   "lat_syscall-null (us)","0.36 (min 0.34, max 0.43)"
   "lat_syscall-open (us)","425.07 (min 372.00, max 560.20)"
   "lat_syscall-read (us)","0.83 (min 0.81, max 0.86)"
   "lat_syscall-stat (us)","5.10 (min 4.92, max 5.59)"
   "lat_syscall-write (us)","0.68 (min 0.67, max 0.70)"
   "lat_tcp (us)","0.96 (min 0.95, max 0.99)"
   "lat_unix (us)","44.28 (min 42.93, max 45.49)"
   "latency_for_0.50_mb_block_size (nanosec)","91.20 (min 86.60, max 92.84)"
   "latency_for_1.00_mb_block_size (nanosec)","49.80 (min 0.00, max 100.12)"
   "pipe_bandwidth (mb\s)","347.95 (min 317.37, max 382.82)"
   "pipe_latency (microsec)","29.21 (min 28.97, max 29.57)"
   "procedure_call (microsec)","0.01"
   "select_on_200_tcp_fds (microsec)","36.03 (min 35.71, max 36.23)"
   "semaphore_latency (microsec)","8.61 (min 8.41, max 9.33)"
   "signal_handler_latency (microsec)","0.99 (min 0.97, max 1.01)"
   "signal_handler_overhead (microsec)","6.16 (min 5.96, max 6.70)"
   "tcp_ip_connection_cost_to_localhost (microsec)","81.07 (min 78.71, max 87.54)"
   "tcp_latency_using_localhost (microsec)","0.96 (min 0.95, max 0.99)"

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
   :header: "Benchmarks","am43xx-gpevm: perf"

   "cpu_clock (mhz)","1000.00"
   "dhrystone_per_mhz (dmips/mhz)","2.37 (min 2.30, max 2.40)"
   "dhrystone_per_second (dhrystonep)","4142371.37 (min 4081632.80, max 4166666.80)"

Whetstone
=========

Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

.. code-block:: console

    runWhetstone

.. csv-table:: Whetstone Benchmarks
   :header: "Benchmarks","am43xx-gpevm: perf"

   "whetstone (mips)","3333.30"

Linpack
=======

Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
   :header: "Benchmarks","am43xx-gpevm: perf"

   "linpack (kflops)","190968.43 (min 188743.00, max 191994.00)"

NBench
======

NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
   :header: "Benchmarks","am43xx-gpevm: perf"

   "assignment (iterations)","7.73 (min 7.71, max 7.75)"
   "fourier (iterations)","12375.13 (min 12357.00, max 12383.00)"
   "fp_emulation (iterations)","103.58 (min 103.46, max 103.71)"
   "huffman (iterations)","871.10 (min 869.65, max 871.90)"
   "idea (iterations)","1739.10 (min 1737.10, max 1739.80)"
   "lu_decomposition (iterations)","335.52 (min 329.57, max 337.09)"
   "neural_net (iterations)","9.05 (min 9.05, max 9.06)"
   "numeric_sort (iterations)","402.60 (min 397.66, max 405.08)"
   "string_sort (iterations)","65.08 (min 65.01, max 65.13)"

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
   :header: "Benchmarks","am43xx-gpevm: perf"

   "add (mb/s)","315.04 (min 314.40, max 316.00)"
   "copy (mb/s)","397.10 (min 396.20, max 398.20)"
   "scale (mb/s)","479.54 (min 477.40, max 481.90)"
   "triad (mb/s)","309.45 (min 302.40, max 311.30)"

*********************
Boot-time Measurement
*********************

Boot media: MMCSD
=================

.. csv-table:: Linux boot time MMCSD
   :header: "Boot Configuration","am43xx-gpevm: Boot time in seconds: avg(min,max)"

   "Linux boot time from SD with default rootfs (20 boot cycles)","65.70 (min 56.42, max 89.54)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

***************
Graphics Driver
***************

Glmark2
=======

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
   :header: "Benchmark","am43xx-gpevm: Score"

   "Glmark2-DRM","92.00"

***********
NAND Driver
***********

.. rubric:: AM43XX-GPEVM
   :name: am43xx-gpevm-nand-driver

.. csv-table:: NAND Performance
   :header: "Buffer size (bytes)","am43xx-gpevm: Write UBIFS Throughput (Mbytes/sec)","am43xx-gpevm: Write UBIFS CPU Load (%)","am43xx-gpevm: Read UBIFS Throughput (Mbytes/sec)","am43xx-gpevm: Read UBIFS CPU Load (%)"

   "102400","4.65 (min 4.47, max 4.93)","80.88 (min 79.58, max 81.52)","10.33 (min 10.19, max 10.46)","37.01 (min 34.42, max 41.04)"
   "262144","4.57 (min 4.45, max 4.68)","81.22 (min 80.35, max 82.10)","10.35 (min 10.25, max 10.45)","38.64 (min 36.31, max 42.96)"
   "524288","4.57 (min 4.46, max 4.69)","81.14 (min 80.23, max 81.91)","10.33 (min 10.23, max 10.52)","36.98 (min 29.43, max 40.21)"
   "1048576","4.58 (min 4.43, max 4.69)","81.17 (min 79.79, max 81.83)","10.40 (min 10.24, max 10.48)","36.94 (min 32.29, max 41.09)"
   "5242880","4.58 (min 4.45, max 4.71)","81.21 (min 80.32, max 81.97)","10.31 (min 10.10, max 10.47)","37.42 (min 33.25, max 42.93)"

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
   :header: "Buffer size (bytes)","am43xx-gpevm: Write EXT4 Throughput (Mbytes/sec)","am43xx-gpevm: Write EXT4 CPU Load (%)","am43xx-gpevm: Read EXT4 Throughput (Mbytes/sec)","am43xx-gpevm: Read EXT4 CPU Load (%)"

   "1m","19.97 (min 19.80, max 20.20)","7.81 (min 7.10, max 8.59)","21.34 (min 21.10, max 21.60)","8.87 (min 8.49, max 9.25)"
   "4m","19.86 (min 19.60, max 20.20)","6.41 (min 5.81, max 7.76)","21.33 (min 21.10, max 21.60)","7.93 (min 7.32, max 8.59)"
   "4k","2.54 (min 2.50, max 2.61)","20.03 (min 18.40, max 21.55)","8.50 (min 8.37, max 8.67)","34.44 (min 33.02, max 36.16)"
   "256k","19.14 (min 18.70, max 19.60)","9.76 (min 9.04, max 10.39)","20.94 (min 20.60, max 21.40)","10.03 (min 9.53, max 10.44)"

MMC EXT4
========

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","am43xx-gpevm: Write Raw Throughput (Mbytes/sec)","am43xx-gpevm: Write Raw CPU Load (%)","am43xx-gpevm: Read Raw Throughput (Mbytes/sec)","am43xx-gpevm: Read Raw CPU Load (%)"

   "102400","19.45 (min 18.04, max 20.16)","13.64 (min 11.90, max 18.84)","20.81 (min 19.70, max 21.94)","13.69 (min 9.46, max 18.38)"
   "262144","18.47 (min 17.94, max 19.03)","13.63 (min 11.31, max 19.18)","20.83 (min 20.41, max 21.40)","16.12 (min 14.74, max 17.68)"
   "524288","18.35 (min 17.91, max 18.84)","13.11 (min 11.25, max 18.21)","21.49 (min 20.38, max 22.69)","15.51 (min 14.40, max 16.34)"
   "1048576","18.58 (min 18.08, max 19.15)","13.56 (min 10.73, max 19.18)","22.46 (min 20.80, max 22.82)","15.85 (min 15.00, max 16.41)"
   "5242880","18.89 (min 17.86, max 19.84)","13.56 (min 11.45, max 17.61)","22.61 (min 21.75, max 22.80)","16.18 (min 15.72, max 16.63)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

***********
UBoot MMCSD
***********

UBOOT MMCSD FAT
===============

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","am43xx-gpevm: Write Throughput (Kbytes/sec)","am43xx-gpevm: Read Throughput (Kbytes/sec)"

   "400000","14211.97 (min 10666.67, max 15814.67)","19152.25 (min 18962.96, max 19320.75)"
   "800000","14495.63 (min 10908.12, max 16549.49)","19401.04 (min 19320.75, max 19458.43)"
   "1000000","15333.51 (min 12109.39, max 16978.24)","19551.36 (min 19504.76, max 19574.67)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

**********
USB Driver
**********

USB Device Controller
=====================

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
   :header: "Number of Blocks","am43xx-gpevm: Throughput (MB/sec)"

   "150","33.57 (min 32.80, max 34.10)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
   :header: "Number of Blocks","am43xx-gpevm: Throughput (MB/sec)"

   "150","32.35 (min 31.60, max 32.80)"

*************
CRYPTO Driver
*************

OpenSSL Performance
===================

.. csv-table:: OpenSSL Performance
   :header: "Algorithm","Buffer Size (in bytes)","am43xx-gpevm: throughput (KBytes/Sec)"

   "aes-128-cbc","1024","35633.54 (min 35414.70, max 35901.78)"
   "aes-128-cbc","16","25870.23 (min 24693.50, max 26474.09)"
   "aes-128-cbc","16384","35859.11 (min 35591.51, max 36126.72)"
   "aes-128-cbc","256","34805.43 (min 34512.30, max 35217.07)"
   "aes-128-cbc","64","32518.68 (min 32116.35, max 32750.68)"
   "aes-128-cbc","8192","35943.77 (min 35657.05, max 36181.33)"
   "aes-128-ecb","1024","38242.65 (min 37027.84, max 38904.49)"
   "aes-128-ecb","16","28720.98 (min 28436.75, max 28900.82)"
   "aes-128-ecb","16384","38468.85 (min 37563.05, max 39168.68)"
   "aes-128-ecb","256","37625.95 (min 36820.99, max 38044.25)"
   "aes-128-ecb","64","34947.04 (min 34676.39, max 35095.04)"
   "aes-128-ecb","8192","38487.97 (min 37475.67, max 39114.07)"
   "aes-192-cbc","1024","30993.55 (min 30958.25, max 31033.69)"
   "aes-192-cbc","16","23465.68 (min 23452.67, max 23485.83)"
   "aes-192-cbc","16384","31067.96 (min 30889.30, max 31156.91)"
   "aes-192-cbc","256","30499.11 (min 30427.05, max 30577.24)"
   "aes-192-cbc","64","28629.76 (min 28530.03, max 28724.61)"
   "aes-192-cbc","8192","31078.50 (min 31025.83, max 31126.87)"
   "aes-192-ecb","1024","30954.15 (min 30900.91, max 31007.74)"
   "aes-192-ecb","16","25752.47 (min 25724.65, max 25775.47)"
   "aes-192-ecb","16384","30846.39 (min 29873.49, max 31058.60)"
   "aes-192-ecb","256","30575.69 (min 30436.35, max 30635.18)"
   "aes-192-ecb","64","29209.87 (min 29033.30, max 29287.10)"
   "aes-192-ecb","8192","31023.88 (min 30870.19, max 31091.37)"
   "aes-256-cbc","1024","27049.55 (min 26983.77, max 27154.43)"
   "aes-256-cbc","16","21085.61 (min 21005.72, max 21146.65)"
   "aes-256-cbc","16384","27172.47 (min 27104.60, max 27273.90)"
   "aes-256-cbc","256","26606.56 (min 26289.75, max 26710.70)"
   "aes-256-cbc","64","25253.51 (min 25199.17, max 25296.02)"
   "aes-256-cbc","8192","27145.17 (min 27074.56, max 27208.36)"
   "aes-256-ecb","1024","26687.98 (min 25820.84, max 26981.72)"
   "aes-256-ecb","16","22758.32 (min 22681.06, max 22829.90)"
   "aes-256-ecb","16384","26829.97 (min 25892.18, max 27028.14)"
   "aes-256-ecb","256","26595.82 (min 26519.81, max 26621.78)"
   "aes-256-ecb","64","25553.91 (min 25506.52, max 25648.34)"
   "aes-256-ecb","8192","26783.94 (min 25277.78, max 27126.44)"
   "des3","1024","3450.93 (min 3349.50, max 3489.79)"
   "des3","16","3334.32 (min 3323.58, max 3346.72)"
   "des3","16384","3453.12 (min 3407.87, max 3484.33)"
   "des3","256","3435.42 (min 3311.45, max 3480.66)"
   "des3","64","3381.17 (min 3298.33, max 3453.31)"
   "des3","8192","3451.56 (min 3372.37, max 3476.14)"
   "md5","1024","107480.41 (min 103949.99, max 108329.64)"
   "md5","16","7684.44 (min 7123.94, max 7810.21)"
   "md5","16384","136466.24 (min 135692.29, max 136817.32)"
   "md5","256","65171.59 (min 64606.63, max 65479.94)"
   "md5","64","25232.57 (min 24961.86, max 25361.62)"
   "md5","8192","134168.97 (min 133761.71, max 134537.22)"
   "sha1","1024","94262.61 (min 92185.26, max 96202.75)"
   "sha1","16","7243.63 (min 7135.70, max 7497.46)"
   "sha1","16384","118812.87 (min 118347.09, max 119280.98)"
   "sha1","256","58645.54 (min 57999.36, max 59749.38)"
   "sha1","64","23050.11 (min 22558.12, max 23738.20)"
   "sha1","8192","117086.70 (min 116443.82, max 117320.36)"
   "sha224","1024","53717.38 (min 53229.23, max 54154.24)"
   "sha224","16","5883.87 (min 5799.74, max 6066.59)"
   "sha224","16384","62083.66 (min 61429.08, max 62499.50)"
   "sha224","256","37286.13 (min 36935.77, max 37816.06)"
   "sha224","64","16757.81 (min 16560.30, max 17109.99)"
   "sha224","8192","61559.37 (min 60822.87, max 61953.37)"
   "sha256","1024","53628.49 (min 53057.19, max 54170.62)"
   "sha256","16","5906.24 (min 5691.33, max 6065.81)"
   "sha256","16384","61615.54 (min 59392.00, max 62395.73)"
   "sha256","256","37399.36 (min 36973.91, max 37720.15)"
   "sha256","64","16521.58 (min 15395.07, max 17081.90)"
   "sha256","8192","60645.38 (min 56915.29, max 61939.71)"
   "sha512","1024","33319.64 (min 31191.72, max 33812.82)"
   "sha512","16","3278.12 (min 3226.56, max 3306.99)"
   "sha512","16384","39689.85 (min 39583.74, max 39758.51)"
   "sha512","256","22697.91 (min 22524.16, max 22790.14)"
   "sha512","64","12983.78 (min 12692.52, max 13114.77)"
   "sha512","8192","39261.53 (min 39097.69, max 39343.45)"

.. csv-table:: OpenSSL CPU Load
   :header: "Algorithm","am43xx-gpevm: CPU Load"

   "aes-128-cbc","98.57 (min 98.00, max 99.00)"
   "aes-128-ecb","99.00"
   "aes-192-cbc","99.00"
   "aes-192-ecb","99.00"
   "aes-256-cbc","99.00"
   "aes-256-ecb","98.86 (min 98.00, max 99.00)"
   "des3","98.57 (min 98.00, max 99.00)"
   "md5","98.86 (min 98.00, max 99.00)"
   "sha1","99.00"
   "sha224","99.00"
   "sha256","98.57 (min 98.00, max 99.00)"
   "sha386","86.57 (min 84.00, max 90.00)"
   "sha512","98.86 (min 98.00, max 99.00)"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc
