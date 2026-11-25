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
| AM335x EVM     | AM335x Evaluation Module rev 1.5B with ARM running at 1000MHz, DDR3-400 (400MHz/800 MT/S), TMDXEVM3358         |
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
   :header: "Benchmarks","am335x-evm: perf"

   "af_unix_sock_stream_latency (microsec)","62.03 (min 58.72, max 64.70)"
   "af_unix_socket_stream_bandwidth (mb\s)","196.89 (min 159.89, max 209.80)"
   "bw_file_rd-io-1mb (mb/s)","188.22 (min 182.48, max 192.09)"
   "bw_file_rd-o2c-1mb (mb/s)","146.31 (min 144.20, max 148.37)"
   "bw_mem-bcopy-16mb (mb/s)","184.37 (min 168.25, max 197.87)"
   "bw_mem-bcopy-1mb (mb/s)","216.76 (min 202.72, max 224.27)"
   "bw_mem-bcopy-2mb (mb/s)","211.26 (min 184.23, max 219.25)"
   "bw_mem-bcopy-4mb (mb/s)","203.09 (min 171.36, max 215.18)"
   "bw_mem-bcopy-8mb (mb/s)","200.71 (min 180.04, max 215.21)"
   "bw_mem-bzero-16mb (mb/s)","991.02 (min 984.01, max 995.95)"
   "bw_mem-bzero-1mb (mb/s)","599.25 (min 202.72, max 984.74)"
   "bw_mem-bzero-2mb (mb/s)","597.81 (min 184.23, max 986.52)"
   "bw_mem-bzero-4mb (mb/s)","595.80 (min 171.36, max 996.64)"
   "bw_mem-bzero-8mb (mb/s)","594.03 (min 180.04, max 1002.00)"
   "bw_mem-cp-16mb (mb/s)","176.88 (min 168.73, max 185.81)"
   "bw_mem-cp-1mb (mb/s)","595.05 (min 193.61, max 989.77)"
   "bw_mem-cp-2mb (mb/s)","591.89 (min 194.82, max 993.87)"
   "bw_mem-cp-4mb (mb/s)","595.44 (min 197.17, max 1008.57)"
   "bw_mem-cp-8mb (mb/s)","589.39 (min 176.27, max 1009.21)"
   "bw_mem-fcp-16mb (mb/s)","175.12 (min 170.81, max 181.42)"
   "bw_mem-fcp-1mb (mb/s)","589.96 (min 189.86, max 984.74)"
   "bw_mem-fcp-2mb (mb/s)","586.53 (min 175.87, max 986.52)"
   "bw_mem-fcp-4mb (mb/s)","589.41 (min 188.30, max 996.64)"
   "bw_mem-fcp-8mb (mb/s)","584.99 (min 170.75, max 1002.00)"
   "bw_mem-frd-16mb (mb/s)","246.14 (min 243.92, max 248.63)"
   "bw_mem-frd-1mb (mb/s)","232.58 (min 189.86, max 269.65)"
   "bw_mem-frd-2mb (mb/s)","218.87 (min 175.87, max 251.60)"
   "bw_mem-frd-4mb (mb/s)","217.19 (min 188.30, max 248.14)"
   "bw_mem-frd-8mb (mb/s)","214.18 (min 170.75, max 248.15)"
   "bw_mem-fwr-16mb (mb/s)","990.77 (min 979.97, max 995.89)"
   "bw_mem-fwr-1mb (mb/s)","626.57 (min 264.24, max 989.77)"
   "bw_mem-fwr-2mb (mb/s)","617.41 (min 246.37, max 993.87)"
   "bw_mem-fwr-4mb (mb/s)","617.81 (min 239.51, max 1008.57)"
   "bw_mem-fwr-8mb (mb/s)","617.61 (min 243.00, max 1009.21)"
   "bw_mem-rd-16mb (mb/s)","249.70 (min 247.12, max 251.67)"
   "bw_mem-rd-1mb (mb/s)","625.82 (min 260.28, max 985.71)"
   "bw_mem-rd-2mb (mb/s)","619.23 (min 249.81, max 996.68)"
   "bw_mem-rd-4mb (mb/s)","618.95 (min 244.16, max 1009.08)"
   "bw_mem-rd-8mb (mb/s)","620.26 (min 247.87, max 1007.43)"
   "bw_mem-rdwr-16mb (mb/s)","203.87 (min 201.39, max 206.11)"
   "bw_mem-rdwr-1mb (mb/s)","206.27 (min 193.61, max 209.01)"
   "bw_mem-rdwr-2mb (mb/s)","201.72 (min 194.82, max 205.87)"
   "bw_mem-rdwr-4mb (mb/s)","201.62 (min 197.17, max 205.67)"
   "bw_mem-rdwr-8mb (mb/s)","196.58 (min 176.27, max 205.57)"
   "bw_mem-wr-16mb (mb/s)","992.56 (min 987.78, max 995.71)"
   "bw_mem-wr-1mb (mb/s)","596.53 (min 207.84, max 985.71)"
   "bw_mem-wr-2mb (mb/s)","595.53 (min 205.19, max 996.68)"
   "bw_mem-wr-4mb (mb/s)","596.09 (min 200.66, max 1009.08)"
   "bw_mem-wr-8mb (mb/s)","597.36 (min 202.26, max 1007.43)"
   "bw_mmap_rd-mo-1mb (mb/s)","261.62 (min 257.86, max 266.42)"
   "bw_mmap_rd-o2c-1mb (mb/s)","160.32 (min 156.40, max 163.91)"
   "bw_pipe (mb/s)","297.42 (min 247.94, max 371.22)"
   "bw_unix (mb/s)","196.89 (min 159.89, max 209.80)"
   "lat_connect (us)","99.10 (min 97.31, max 103.49)"
   "lat_ctx-2-128k (us)","40.19 (min 35.05, max 44.65)"
   "lat_ctx-2-256k (us)","44.27 (min 5.36, max 74.38)"
   "lat_ctx-4-128k (us)","64.82 (min 40.92, max 77.28)"
   "lat_ctx-4-256k (us)","3.65 (min 0.00, max 25.53)"
   "lat_fs-0k (num_files)","161.00 (min 134.00, max 185.00)"
   "lat_fs-10k (num_files)","72.57 (min 57.00, max 80.00)"
   "lat_fs-1k (num_files)","103.71 (min 96.00, max 107.00)"
   "lat_fs-4k (num_files)","99.71 (min 86.00, max 110.00)"
   "lat_mem_rd-stride128-sz1000k (ns)","224.39 (min 222.15, max 227.99)"
   "lat_mem_rd-stride128-sz125k (ns)","16.16 (min 11.67, max 26.78)"
   "lat_mem_rd-stride128-sz250k (ns)","67.03 (min 37.57, max 81.62)"
   "lat_mem_rd-stride128-sz31k (ns)","3.05 (min 3.04, max 3.07)"
   "lat_mem_rd-stride128-sz50 (ns)","3.01 (min 3.01, max 3.02)"
   "lat_mem_rd-stride128-sz500k (ns)","188.16 (min 185.87, max 190.74)"
   "lat_mem_rd-stride128-sz62k (ns)","8.90 (min 8.84, max 8.95)"
   "lat_mmap-1m (us)","103.00 (min 82.00, max 124.00)"
   "lat_ops-double-add (ns)","8.99 (min 8.95, max 9.07)"
   "lat_ops-double-div (ns)","57.45 (min 57.32, max 57.61)"
   "lat_ops-double-mul (ns)","11.13 (min 11.07, max 11.24)"
   "lat_ops-float-add (ns)","8.97 (min 8.94, max 9.01)"
   "lat_ops-float-div (ns)","33.24 (min 33.16, max 33.32)"
   "lat_ops-float-mul (ns)","10.08 (min 10.05, max 10.11)"
   "lat_ops-int-add (ns)","1.01 (min 1.01, max 1.02)"
   "lat_ops-int-bit (ns)","0.67"
   "lat_ops-int-div (ns)","72.08 (min 71.72, max 72.28)"
   "lat_ops-int-mod (ns)","25.57 (min 25.50, max 25.69)"
   "lat_ops-int-mul (ns)","6.08 (min 6.07, max 6.09)"
   "lat_ops-int64-add (ns)","1.11"
   "lat_ops-int64-bit (ns)","0.68"
   "lat_ops-int64-div (ns)","211.46 (min 211.00, max 212.24)"
   "lat_ops-int64-mod (ns)","52.80 (min 52.72, max 52.88)"
   "lat_ops-int64-mul (ns)","6.61 (min 6.59, max 6.63)"
   "lat_pagefault (us)","2.06 (min 1.98, max 2.15)"
   "lat_pipe (us)","38.45 (min 36.89, max 42.58)"
   "lat_proc-exec (us)","1459.96 (min 1364.25, max 1506.75)"
   "lat_proc-fork (us)","1342.60 (min 1292.40, max 1401.75)"
   "lat_proc-proccall (us)","0.01"
   "lat_select (us)","59.76 (min 56.58, max 77.03)"
   "lat_sem (us)","12.73 (min 12.08, max 13.80)"
   "lat_sig-catch (us)","9.26 (min 9.01, max 9.80)"
   "lat_sig-install (us)","1.50 (min 1.47, max 1.58)"
   "lat_sig-prot (us)","1.02 (min 0.88, max 1.16)"
   "lat_syscall-fstat (us)","2.85 (min 2.72, max 3.22)"
   "lat_syscall-null (us)","0.46 (min 0.45, max 0.50)"
   "lat_syscall-open (us)","538.82 (min 408.31, max 777.67)"
   "lat_syscall-read (us)","1.05 (min 1.04, max 1.07)"
   "lat_syscall-stat (us)","7.30 (min 6.59, max 8.04)"
   "lat_syscall-write (us)","0.82 (min 0.81, max 0.82)"
   "lat_tcp (us)","1.31 (min 1.28, max 1.41)"
   "lat_unix (us)","62.03 (min 58.72, max 64.70)"
   "latency_for_0.50_mb_block_size (nanosec)","188.16 (min 185.87, max 190.74)"
   "latency_for_1.00_mb_block_size (nanosec)","112.20 (min 0.00, max 227.99)"
   "pipe_bandwidth (mb\s)","297.42 (min 247.94, max 371.22)"
   "pipe_latency (microsec)","38.45 (min 36.89, max 42.58)"
   "procedure_call (microsec)","0.01"
   "select_on_200_tcp_fds (microsec)","59.76 (min 56.58, max 77.03)"
   "semaphore_latency (microsec)","12.73 (min 12.08, max 13.80)"
   "signal_handler_latency (microsec)","1.50 (min 1.47, max 1.58)"
   "signal_handler_overhead (microsec)","9.26 (min 9.01, max 9.80)"
   "tcp_ip_connection_cost_to_localhost (microsec)","99.10 (min 97.31, max 103.49)"
   "tcp_latency_using_localhost (microsec)","1.31 (min 1.28, max 1.41)"

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
   :header: "Benchmarks","am335x-evm: perf"

   "cpu_clock (mhz)","1000.00"
   "dhrystone_per_mhz (dmips/mhz)","2.00"
   "dhrystone_per_second (dhrystonep)","3456918.11 (min 3448275.80, max 3508772.00)"

Whetstone
=========

Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

.. code-block:: console

    runWhetstone

.. csv-table:: Whetstone Benchmarks
   :header: "Benchmarks","am335x-evm: perf"

   "whetstone (mips)","880.93 (min 833.30, max 1000.00)"

Linpack
=======

Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
   :header: "Benchmarks","am335x-evm: perf"

   "linpack (kflops)","52117.86 (min 51772.00, max 52447.00)"

NBench
======

NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
   :header: "Benchmarks","am335x-evm: perf"

   "assignment (iterations)","7.96 (min 7.94, max 7.97)"
   "fourier (iterations)","2760.17 (min 2756.40, max 2762.20)"
   "fp_emulation (iterations)","72.10 (min 71.67, max 72.32)"
   "huffman (iterations)","714.76 (min 713.62, max 715.33)"
   "idea (iterations)","1721.34 (min 1719.20, max 1722.50)"
   "lu_decomposition (iterations)","77.15 (min 76.77, max 77.39)"
   "neural_net (iterations)","2.17"
   "numeric_sort (iterations)","348.71 (min 348.12, max 349.00)"
   "string_sort (iterations)","69.45 (min 69.34, max 69.51)"

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
   :header: "Benchmarks","am335x-evm: perf"

   "add (mb/s)","382.63 (min 379.60, max 386.40)"
   "copy (mb/s)","439.66 (min 436.20, max 442.10)"
   "scale (mb/s)","413.21 (min 410.40, max 416.50)"
   "triad (mb/s)","346.67 (min 343.00, max 350.10)"

*********************
Boot-time Measurement
*********************

Boot media: MMCSD
=================

.. csv-table:: Linux boot time MMCSD
   :header: "Boot Configuration","am335x-evm: Boot time in seconds: avg(min,max)"

   "Linux boot time from SD with default rootfs (20 boot cycles)","89.23 (min 77.47, max 110.57)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

***************
Graphics Driver
***************

Glmark2
=======

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
   :header: "Benchmark","am335x-evm: Score"

   "Glmark2-DRM","73.00"

***********
NAND Driver
***********

.. rubric:: AM335X-EVM
   :name: am335x-evm-nand-driver

.. csv-table:: NAND Performance
   :header: "Buffer size (bytes)","am335x-evm: Write UBIFS Throughput (Mbytes/sec)","am335x-evm: Write UBIFS CPU Load (%)","am335x-evm: Read UBIFS Throughput (Mbytes/sec)","am335x-evm: Read UBIFS CPU Load (%)"

   "102400","3.30 (min 3.20, max 3.43)","70.99 (min 69.57, max 72.45)","6.05 (min 5.93, max 6.21)","38.34 (min 30.57, max 41.43)"
   "262144","3.29 (min 3.18, max 3.45)","68.56 (min 66.75, max 70.33)","6.09 (min 6.00, max 6.22)","38.67 (min 36.09, max 40.95)"
   "524288","3.27 (min 3.21, max 3.34)","70.86 (min 69.91, max 71.94)","6.12 (min 6.04, max 6.21)","38.32 (min 29.86, max 41.25)"
   "1048576","3.27 (min 3.21, max 3.34)","70.86 (min 69.99, max 71.99)","6.08 (min 5.97, max 6.21)","37.91 (min 31.12, max 40.25)"
   "5242880","3.27 (min 3.22, max 3.33)","71.07 (min 69.96, max 72.43)","6.10 (min 6.01, max 6.22)","38.55 (min 34.09, max 40.57)"

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
   :header: "Buffer size (bytes)","am335x-evm: Write EXT4 Throughput (Mbytes/sec)","am335x-evm: Write EXT4 CPU Load (%)","am335x-evm: Read EXT4 Throughput (Mbytes/sec)","am335x-evm: Read EXT4 CPU Load (%)"

   "1m","19.69 (min 19.40, max 19.90)","8.20 (min 4.77, max 9.33)","20.93 (min 20.50, max 21.30)","9.04 (min 6.18, max 9.93)"
   "4m","19.56 (min 19.00, max 20.10)","6.58 (min 3.91, max 7.77)","20.93 (min 20.50, max 21.40)","7.92 (min 5.92, max 8.55)"
   "4k","2.33 (min 2.24, max 2.50)","32.73 (min 19.87, max 36.43)","8.06 (min 7.94, max 8.48)","47.63 (min 37.23, max 51.15)"
   "256k","18.34 (min 17.60, max 19.10)","11.92 (min 7.56, max 13.44)","20.53 (min 19.90, max 20.90)","12.09 (min 8.44, max 13.25)"

MMC EXT4
========

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","am335x-evm: Write Raw Throughput (Mbytes/sec)","am335x-evm: Write Raw CPU Load (%)","am335x-evm: Read Raw Throughput (Mbytes/sec)","am335x-evm: Read Raw CPU Load (%)"

   "102400","19.07 (min 18.32, max 20.02)","15.78 (min 12.69, max 21.35)","20.43 (min 19.27, max 21.86)","21.19 (min 10.85, max 24.95)"
   "262144","18.01 (min 17.37, max 19.11)","16.26 (min 14.39, max 19.83)","20.21 (min 20.13, max 20.54)","17.82 (min 17.33, max 18.36)"
   "524288","17.98 (min 17.31, max 19.16)","16.11 (min 13.92, max 20.43)","21.21 (min 20.43, max 22.37)","16.52 (min 15.61, max 17.25)"
   "1048576","18.20 (min 17.58, max 19.32)","16.48 (min 14.01, max 20.73)","21.98 (min 20.87, max 22.42)","16.39 (min 15.67, max 16.92)"
   "5242880","18.33 (min 17.89, max 19.59)","16.11 (min 13.78, max 20.96)","22.43 (min 22.30, max 22.80)","17.42 (min 16.37, max 18.84)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

**********
USB Driver
**********

USB Device Controller
=====================

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
   :header: "Number of Blocks","am335x-evm: Throughput (MB/sec)"

   "150","16.20"

*************
CRYPTO Driver
*************

OpenSSL Performance
===================

.. csv-table:: OpenSSL Performance
   :header: "Algorithm","Buffer Size (in bytes)","am335x-evm: throughput (KBytes/Sec)"

   "aes-128-cbc","1024","45366.04 (min 45195.61, max 45490.52)"
   "aes-128-cbc","16","28588.29 (min 27196.26, max 28815.95)"
   "aes-128-cbc","16384","45747.77 (min 45569.37, max 45875.20)"
   "aes-128-cbc","256","44076.67 (min 43909.97, max 44184.83)"
   "aes-128-cbc","64","39513.17 (min 39308.42, max 39608.43)"
   "aes-128-cbc","8192","45729.56 (min 45430.10, max 45891.58)"
   "aes-128-ecb","1024","45942.84 (min 43752.79, max 46258.86)"
   "aes-128-ecb","16","31838.27 (min 30922.68, max 32053.13)"
   "aes-128-ecb","16384","46398.12 (min 46252.03, max 46541.48)"
   "aes-128-ecb","256","44796.64 (min 43231.74, max 45194.24)"
   "aes-128-ecb","64","41286.62 (min 40924.99, max 41518.08)"
   "aes-128-ecb","8192","46238.83 (min 43797.16, max 46576.98)"
   "aes-192-cbc","1024","37225.13 (min 36823.38, max 37435.39)"
   "aes-192-cbc","16","25116.66 (min 23840.61, max 25356.99)"
   "aes-192-cbc","16384","37417.87 (min 36842.15, max 37683.20)"
   "aes-192-cbc","256","36339.95 (min 36003.84, max 36517.63)"
   "aes-192-cbc","64","33129.56 (min 32283.52, max 33383.23)"
   "aes-192-cbc","8192","37427.88 (min 37164.37, max 37743.27)"
   "aes-192-ecb","1024","39472.87 (min 37751.47, max 39783.77)"
   "aes-192-ecb","16","28733.40 (min 28593.25, max 28808.06)"
   "aes-192-ecb","16384","39793.10 (min 38770.01, max 40020.65)"
   "aes-192-ecb","256","38929.49 (min 38800.64, max 39019.69)"
   "aes-192-ecb","64","36105.41 (min 35854.70, max 36208.00)"
   "aes-192-ecb","8192","39851.80 (min 39403.52, max 40012.46)"
   "aes-256-cbc","1024","33288.45 (min 33109.67, max 33383.42)"
   "aes-256-cbc","16","23363.57 (min 23208.18, max 23432.13)"
   "aes-256-cbc","16384","33507.10 (min 33346.90, max 33609.05)"
   "aes-256-cbc","256","32601.69 (min 32467.71, max 32683.78)"
   "aes-256-cbc","64","30026.84 (min 29920.43, max 30112.30)"
   "aes-256-cbc","8192","33491.63 (min 33357.82, max 33600.85)"
   "aes-256-ecb","1024","34702.73 (min 33780.39, max 34912.60)"
   "aes-256-ecb","16","25963.01 (min 24767.22, max 26135.13)"
   "aes-256-ecb","16384","34698.58 (min 33035.61, max 35072.68)"
   "aes-256-ecb","256","33841.37 (min 32348.59, max 34324.82)"
   "aes-256-ecb","64","31802.72 (min 30798.14, max 32120.30)"
   "aes-256-ecb","8192","34416.18 (min 33008.30, max 35083.61)"
   "des3","1024","3996.59 (min 3739.65, max 4061.53)"
   "des3","16","3725.51 (min 3359.05, max 3828.49)"
   "des3","16384","3997.70 (min 3741.01, max 4063.23)"
   "des3","256","3981.85 (min 3725.65, max 4046.85)"
   "des3","64","3934.46 (min 3683.93, max 4001.73)"
   "des3","8192","3974.03 (min 3730.09, max 4057.77)"
   "md5","1024","122987.41 (min 120309.76, max 124262.74)"
   "md5","16","7275.29 (min 6906.11, max 7411.23)"
   "md5","16384","161771.06 (min 156871.34, max 162796.89)"
   "md5","256","68709.34 (min 66182.66, max 69899.52)"
   "md5","64","24889.61 (min 23673.24, max 25392.32)"
   "md5","8192","158561.62 (min 147259.39, max 161218.56)"
   "sha1","1024","102179.84 (min 101504.00, max 103297.37)"
   "sha1","16","6871.88 (min 6645.29, max 7133.53)"
   "sha1","16384","130134.93 (min 129193.30, max 130531.33)"
   "sha1","256","59858.01 (min 58953.39, max 61170.77)"
   "sha1","64","22515.71 (min 21911.25, max 23184.28)"
   "sha1","8192","127947.66 (min 126394.37, max 129496.41)"
   "sha224","1024","60254.46 (min 60014.59, max 60458.67)"
   "sha224","16","5661.87 (min 5400.54, max 5778.01)"
   "sha224","16384","71178.92 (min 70871.72, max 71417.86)"
   "sha224","256","39892.20 (min 39427.93, max 40147.29)"
   "sha224","64","17107.70 (min 16783.47, max 17286.14)"
   "sha224","8192","69836.80 (min 63728.30, max 70920.87)"
   "sha256","1024","60132.69 (min 59791.02, max 60353.88)"
   "sha256","16","5609.66 (min 5018.20, max 5743.65)"
   "sha256","16384","70345.61 (min 63919.45, max 71434.24)"
   "sha256","256","39724.69 (min 39308.54, max 39981.06)"
   "sha256","64","16806.62 (min 15509.35, max 17090.54)"
   "sha256","8192","69759.20 (min 63343.27, max 70866.26)"
   "sha512","1024","35813.43 (min 32678.91, max 36269.40)"
   "sha512","16","3197.90 (min 2891.39, max 3279.18)"
   "sha512","16384","43175.48 (min 42964.31, max 43313.83)"
   "sha512","256","23462.66 (min 22244.52, max 23829.59)"
   "sha512","64","12644.84 (min 11827.31, max 13039.10)"
   "sha512","8192","42645.73 (min 42388.14, max 42874.20)"

.. csv-table:: OpenSSL CPU Load
   :header: "Algorithm","am335x-evm: CPU Load"

   "aes-128-cbc","98.92 (min 98.00, max 99.00)"
   "aes-128-ecb","98.75 (min 97.00, max 99.00)"
   "aes-192-cbc","99.00"
   "aes-192-ecb","98.92 (min 98.00, max 99.00)"
   "aes-256-cbc","99.00"
   "aes-256-ecb","98.50 (min 98.00, max 99.00)"
   "des3","98.75 (min 98.00, max 99.00)"
   "md5","98.67 (min 98.00, max 99.00)"
   "sha1","99.00"
   "sha224","98.92 (min 98.00, max 99.00)"
   "sha256","98.42 (min 97.00, max 99.00)"
   "sha386","84.58 (min 73.00, max 89.00)"
   "sha512","98.58 (min 98.00, max 99.00)"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc
