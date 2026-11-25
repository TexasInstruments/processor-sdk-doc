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
| AM62Px SK      | AM62Px Starter Kit rev E1 with ARM running at 1.4GHz, DDR data rate 3200 MT/S                                  |
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
   :header: "Benchmarks","am62pxx_sk-fs: perf"

   "af_unix_sock_stream_latency (microsec)","26.80 (min 22.34, max 33.96)"
   "af_unix_socket_stream_bandwidth (mb\s)","1225.33 (min 1171.98, max 1254.71)"
   "bw_file_rd-io-1mb (mb/s)","1382.11 (min 1345.44, max 1405.90)"
   "bw_file_rd-o2c-1mb (mb/s)","747.06 (min 685.64, max 818.73)"
   "bw_mem-bcopy-16mb (mb/s)","1880.55 (min 1574.49, max 1980.69)"
   "bw_mem-bcopy-1mb (mb/s)","2093.54 (min 2001.82, max 2145.92)"
   "bw_mem-bcopy-2mb (mb/s)","1745.69 (min 1592.36, max 1847.75)"
   "bw_mem-bcopy-4mb (mb/s)","1810.43 (min 1632.43, max 1942.06)"
   "bw_mem-bcopy-8mb (mb/s)","1816.85 (min 1582.59, max 1953.84)"
   "bw_mem-bzero-16mb (mb/s)","8030.89 (min 7807.42, max 8119.08)"
   "bw_mem-bzero-1mb (mb/s)","5058.56 (min 2001.82, max 8113.96)"
   "bw_mem-bzero-2mb (mb/s)","4882.73 (min 1592.36, max 8118.60)"
   "bw_mem-bzero-4mb (mb/s)","4918.22 (min 1632.43, max 8116.33)"
   "bw_mem-bzero-8mb (mb/s)","4924.21 (min 1582.59, max 8116.33)"
   "bw_mem-cp-16mb (mb/s)","959.88 (min 911.47, max 987.35)"
   "bw_mem-cp-1mb (mb/s)","4640.34 (min 884.80, max 8461.54)"
   "bw_mem-cp-2mb (mb/s)","4558.29 (min 887.05, max 8254.08)"
   "bw_mem-cp-4mb (mb/s)","4543.63 (min 935.34, max 8182.75)"
   "bw_mem-cp-8mb (mb/s)","4535.33 (min 929.48, max 8161.88)"
   "bw_mem-fcp-16mb (mb/s)","1800.27 (min 1718.95, max 1840.56)"
   "bw_mem-fcp-1mb (mb/s)","4898.50 (min 1698.43, max 8113.96)"
   "bw_mem-fcp-2mb (mb/s)","4848.89 (min 1604.88, max 8118.60)"
   "bw_mem-fcp-4mb (mb/s)","4893.16 (min 1672.01, max 8116.33)"
   "bw_mem-fcp-8mb (mb/s)","4904.67 (min 1665.45, max 8116.33)"
   "bw_mem-frd-16mb (mb/s)","1909.24 (min 1833.39, max 1963.43)"
   "bw_mem-frd-1mb (mb/s)","1881.98 (min 1698.43, max 2030.27)"
   "bw_mem-frd-2mb (mb/s)","1772.72 (min 1604.88, max 1950.84)"
   "bw_mem-frd-4mb (mb/s)","1823.17 (min 1672.01, max 1947.42)"
   "bw_mem-frd-8mb (mb/s)","1835.32 (min 1665.45, max 1955.27)"
   "bw_mem-fwr-16mb (mb/s)","8048.13 (min 7827.79, max 8135.59)"
   "bw_mem-fwr-1mb (mb/s)","5146.30 (min 1920.73, max 8461.54)"
   "bw_mem-fwr-2mb (mb/s)","5013.18 (min 1775.88, max 8254.08)"
   "bw_mem-fwr-4mb (mb/s)","4992.29 (min 1788.38, max 8182.75)"
   "bw_mem-fwr-8mb (mb/s)","4982.99 (min 1801.60, max 8161.88)"
   "bw_mem-rd-16mb (mb/s)","2022.08 (min 1882.80, max 2075.23)"
   "bw_mem-rd-1mb (mb/s)","2069.72 (min 1709.99, max 2355.07)"
   "bw_mem-rd-2mb (mb/s)","1866.02 (min 1520.68, max 2111.19)"
   "bw_mem-rd-4mb (mb/s)","1887.79 (min 1658.37, max 2057.61)"
   "bw_mem-rd-8mb (mb/s)","1953.28 (min 1786.91, max 2069.86)"
   "bw_mem-rdwr-16mb (mb/s)","1921.49 (min 1784.72, max 1996.26)"
   "bw_mem-rdwr-1mb (mb/s)","1419.14 (min 884.80, max 1969.56)"
   "bw_mem-rdwr-2mb (mb/s)","1310.68 (min 887.05, max 1735.21)"
   "bw_mem-rdwr-4mb (mb/s)","1379.62 (min 935.34, max 1882.06)"
   "bw_mem-rdwr-8mb (mb/s)","1441.08 (min 929.48, max 1947.18)"
   "bw_mem-wr-16mb (mb/s)","1922.37 (min 1832.76, max 1996.01)"
   "bw_mem-wr-1mb (mb/s)","1854.25 (min 1646.54, max 2049.18)"
   "bw_mem-wr-2mb (mb/s)","1694.08 (min 1520.68, max 1923.08)"
   "bw_mem-wr-4mb (mb/s)","1771.78 (min 1639.01, max 1900.54)"
   "bw_mem-wr-8mb (mb/s)","1884.80 (min 1764.64, max 1960.78)"
   "bw_mmap_rd-mo-1mb (mb/s)","2114.78 (min 2029.52, max 2201.43)"
   "bw_mmap_rd-o2c-1mb (mb/s)","753.97 (min 677.39, max 803.08)"
   "bw_pipe (mb/s)","821.50 (min 802.62, max 858.50)"
   "bw_unix (mb/s)","1225.33 (min 1171.98, max 1254.71)"
   "lat_connect (us)","72.22 (min 71.89, max 73.15)"
   "lat_ctx-2-128k (us)","7.06 (min 6.01, max 7.72)"
   "lat_ctx-2-256k (us)","20.66 (min 5.27, max 35.07)"
   "lat_ctx-4-128k (us)","21.23 (min 6.01, max 25.92)"
   "lat_ctx-4-256k (us)","54.07 (min 5.69, max 94.55)"
   "lat_fs-0k (num_files)","251.00 (min 226.00, max 274.00)"
   "lat_fs-10k (num_files)","121.57 (min 119.00, max 125.00)"
   "lat_fs-1k (num_files)","179.57 (min 171.00, max 189.00)"
   "lat_fs-4k (num_files)","166.00 (min 147.00, max 184.00)"
   "lat_mem_rd-stride128-sz1000k (ns)","30.12 (min 29.46, max 31.48)"
   "lat_mem_rd-stride128-sz125k (ns)","5.56 (min 5.55, max 5.58)"
   "lat_mem_rd-stride128-sz250k (ns)","5.83 (min 5.82, max 5.84)"
   "lat_mem_rd-stride128-sz31k (ns)","3.59 (min 2.15, max 4.19)"
   "lat_mem_rd-stride128-sz50 (ns)","2.15"
   "lat_mem_rd-stride128-sz500k (ns)","10.99 (min 8.61, max 13.06)"
   "lat_mem_rd-stride128-sz62k (ns)","5.03 (min 4.50, max 5.26)"
   "lat_mmap-1m (us)","55.14 (min 50.00, max 57.00)"
   "lat_ops-double-add (ns)","2.86"
   "lat_ops-double-div (ns)","15.75 (min 15.74, max 15.76)"
   "lat_ops-double-mul (ns)","2.86"
   "lat_ops-float-add (ns)","2.86"
   "lat_ops-float-div (ns)","9.30 (min 9.30, max 9.31)"
   "lat_ops-float-mul (ns)","2.86"
   "lat_ops-int-add (ns)","0.72"
   "lat_ops-int-bit (ns)","0.48"
   "lat_ops-int-div (ns)","4.29 (min 4.29, max 4.30)"
   "lat_ops-int-mod (ns)","4.54 (min 4.53, max 4.54)"
   "lat_ops-int-mul (ns)","3.07 (min 3.04, max 3.10)"
   "lat_ops-int64-add (ns)","0.72"
   "lat_ops-int64-bit (ns)","0.48"
   "lat_ops-int64-div (ns)","6.80"
   "lat_ops-int64-mod (ns)","5.25"
   "lat_ops-int64-mul (ns)","3.54 (min 3.54, max 3.55)"
   "lat_pagefault (us)","0.43 (min 0.38, max 0.44)"
   "lat_pipe (us)","18.18 (min 17.86, max 18.37)"
   "lat_proc-exec (us)","696.84 (min 674.75, max 739.50)"
   "lat_proc-fork (us)","601.98 (min 588.56, max 620.78)"
   "lat_proc-proccall (us)","0.01"
   "lat_select (us)","31.99 (min 31.82, max 32.25)"
   "lat_sem (us)","2.48 (min 2.30, max 2.66)"
   "lat_sig-catch (us)","5.74 (min 5.69, max 5.84)"
   "lat_sig-install (us)","0.61 (min 0.61, max 0.63)"
   "lat_sig-prot (us)","0.61 (min 0.28, max 0.92)"
   "lat_syscall-fstat (us)","1.80 (min 1.74, max 1.83)"
   "lat_syscall-null (us)","0.38 (min 0.37, max 0.40)"
   "lat_syscall-open (us)","170.07 (min 152.32, max 215.88)"
   "lat_syscall-read (us)","0.72 (min 0.71, max 0.74)"
   "lat_syscall-stat (us)","4.43 (min 4.30, max 4.56)"
   "lat_syscall-write (us)","0.68 (min 0.67, max 0.69)"
   "lat_tcp (us)","0.76 (min 0.75, max 0.76)"
   "lat_unix (us)","26.80 (min 22.34, max 33.96)"
   "latency_for_0.50_mb_block_size (nanosec)","10.99 (min 8.61, max 13.06)"
   "latency_for_1.00_mb_block_size (nanosec)","15.06 (min 0.00, max 31.48)"
   "pipe_bandwidth (mb\s)","821.50 (min 802.62, max 858.50)"
   "pipe_latency (microsec)","18.18 (min 17.86, max 18.37)"
   "procedure_call (microsec)","0.01"
   "select_on_200_tcp_fds (microsec)","31.99 (min 31.82, max 32.25)"
   "semaphore_latency (microsec)","2.48 (min 2.30, max 2.66)"
   "signal_handler_latency (microsec)","0.61 (min 0.61, max 0.63)"
   "signal_handler_overhead (microsec)","5.74 (min 5.69, max 5.84)"
   "tcp_ip_connection_cost_to_localhost (microsec)","72.22 (min 71.89, max 73.15)"
   "tcp_latency_using_localhost (microsec)","0.76 (min 0.75, max 0.76)"

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
   :header: "Benchmarks","am62pxx_sk-fs: perf"

   "cpu_clock (mhz)","1400.00"
   "dhrystone_per_mhz (dmips/mhz)","2.79 (min 2.70, max 2.80)"
   "dhrystone_per_second (dhrystonep)","6863710.79 (min 6666666.50, max 6896551.50)"

Whetstone
=========

Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

.. code-block:: console

    runWhetstone

.. csv-table:: Whetstone Benchmarks
   :header: "Benchmarks","am62pxx_sk-fs: perf"

   "whetstone (mips)","5000.00"

Linpack
=======

Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
   :header: "Benchmarks","am62pxx_sk-fs: perf"

   "linpack (kflops)","580341.29 (min 579319.00, max 581921.00)"

NBench
======

NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
   :header: "Benchmarks","am62pxx_sk-fs: perf"

   "assignment (iterations)","14.16 (min 14.11, max 14.21)"
   "fourier (iterations)","19369.57 (min 19361.00, max 19372.00)"
   "fp_emulation (iterations)","204.42 (min 204.42, max 204.43)"
   "huffman (iterations)","1188.33 (min 1188.00, max 1188.60)"
   "idea (iterations)","3070.63 (min 3070.50, max 3070.80)"
   "lu_decomposition (iterations)","532.76 (min 530.20, max 535.54)"
   "neural_net (iterations)","9.68 (min 9.67, max 9.68)"
   "numeric_sort (iterations)","540.56 (min 538.67, max 542.82)"
   "string_sort (iterations)","163.60 (min 163.59, max 163.61)"

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
   :header: "Benchmarks","am62pxx_sk-fs: perf"

   "add (mb/s)","2805.30 (min 2696.80, max 2881.70)"
   "copy (mb/s)","3871.04 (min 3712.00, max 3979.80)"
   "scale (mb/s)","3612.40 (min 3475.20, max 3706.50)"
   "triad (mb/s)","2476.64 (min 2396.00, max 2531.50)"

CoreMarkPro
===========

CoreMark\ |reg|-Pro is a comprehensive, advanced processor benchmark that works
with and enhances the market-proven industry-standard EEMBC CoreMark\ |reg|
benchmark. While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the
entire processor, adding comprehensive support for multicore technology, a
combination of integer and floating-point workloads, and data sets for utilizing
larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
   :header: "Benchmarks","am62pxx_sk-fs: perf"

   "cjpeg-rose7-preset (workloads/)","41.92 (min 41.84, max 42.02)"
   "core (workloads/)","0.30"
   "coremark-pro ()","952.93 (min 951.13, max 956.03)"
   "linear_alg-mid-100x100-sp (workloads/)","14.68"
   "loops-all-mid-10k-sp (workloads/)","0.71 (min 0.71, max 0.72)"
   "nnet_test (workloads/)","1.08"
   "parser-125k (workloads/)","9.26"
   "radix2-big-64k (workloads/)","73.18 (min 72.53, max 74.15)"
   "sha-test (workloads/)","81.21 (min 80.65, max 81.30)"
   "zip-test (workloads/)","23.41 (min 23.26, max 23.81)"

.. csv-table:: CoreMarkProTwoCore Benchmarks
   :header: "Benchmarks","am62pxx_sk-fs: perf"

   "cjpeg-rose7-preset (workloads/)","83.23 (min 82.64, max 83.33)"
   "core (workloads/)","0.60"
   "coremark-pro ()","1693.40 (min 1687.32, max 1708.45)"
   "linear_alg-mid-100x100-sp (workloads/)","29.33 (min 29.31, max 29.36)"
   "loops-all-mid-10k-sp (workloads/)","1.30 (min 1.30, max 1.32)"
   "nnet_test (workloads/)","2.15 (min 2.15, max 2.16)"
   "parser-125k (workloads/)","16.32 (min 16.13, max 16.53)"
   "radix2-big-64k (workloads/)","65.31 (min 63.75, max 68.02)"
   "sha-test (workloads/)","161.29"
   "zip-test (workloads/)","45.91 (min 45.45, max 46.51)"

*********************
Boot-time Measurement
*********************

Boot media: MMCSD
=================

.. csv-table:: Linux boot time MMCSD
   :header: "Boot Configuration","am62pxx_sk-fs: Boot time in seconds: avg(min,max)"

   "Linux boot time from SD with default rootfs (20 boot cycles)","18.09 (min 16.90, max 20.70)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

*********************
ALSA SoC Audio Driver
*********************

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
   :header: "Sampling Rate (Hz)","am62pxx_sk-fs: Throughput (bits/sec)","am62pxx_sk-fs: CPU Load (%)"

   "11025","352799.14 (min 352797.00, max 352801.00)","0.12 (min 0.11, max 0.13)"
   "16000","511999.29 (min 511996.00, max 512002.00)","0.15 (min 0.11, max 0.32)"
   "22050","705595.14 (min 705593.00, max 705597.00)","0.16 (min 0.14, max 0.17)"
   "24000","705597.57 (min 705594.00, max 705600.00)","0.17 (min 0.15, max 0.19)"
   "32000","1023997.29 (min 1023991.00, max 1024001.00)","0.14 (min 0.11, max 0.18)"
   "44100","1411196.29 (min 1411188.00, max 1411201.00)","0.24 (min 0.23, max 0.25)"
   "48000","1535996.14 (min 1535987.00, max 1536001.00)","0.13 (min 0.11, max 0.15)"
   "88200","2822390.00 (min 2822373.00, max 2822400.00)","0.39 (min 0.36, max 0.41)"
   "96000","3071978.57 (min 3071966.00, max 3072000.00)","0.19 (min 0.17, max 0.20)"

.. csv-table:: Audio Playback
   :header: "Sampling Rate (Hz)","am62pxx_sk-fs: Throughput (bits/sec)","am62pxx_sk-fs: CPU Load (%)"

   "11025","352954.43 (min 352935.00, max 353013.00)","0.12 (min 0.10, max 0.12)"
   "16000","512218.29 (min 512192.00, max 512269.00)","0.14 (min 0.11, max 0.16)"
   "22050","705853.57 (min 705614.00, max 705898.00)","0.14 (min 0.13, max 0.16)"
   "24000","705878.14 (min 705789.00, max 705896.00)","0.15 (min 0.13, max 0.16)"
   "32000","1024421.43 (min 1024404.00, max 1024429.00)","0.29 (min 0.12, max 1.19)"
   "44100","1411785.00 (min 1411772.00, max 1411791.00)","0.21 (min 0.19, max 0.22)"
   "48000","1536634.57 (min 1536621.00, max 1536643.00)","0.20 (min 0.14, max 0.38)"
   "88200","2823560.57 (min 2823537.00, max 2823579.00)","0.33 (min 0.29, max 0.36)"
   "96000","3073256.57 (min 3073232.00, max 3073281.00)","0.22 (min 0.17, max 0.47)"

***************
Graphics Driver
***************

GFXBench
========

Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
   :header: "Benchmark","am62pxx_sk-fs: Score","am62pxx_sk-fs: Fps"

   " GFXBench 3.x gl_manhattan_off","916.69 (min 902.89, max 933.58)","14.79 (min 14.56, max 15.06)"
   " GFXBench 3.x gl_trex_off","1613.55 (min 1580.03, max 1637.54)","28.81 (min 28.21, max 29.24)"
   " GFXBench 5.x gl_5_high_off","115.24 (min 114.75, max 116.13)","1.79 (min 1.78, max 1.81)"

Glmark2
=======

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
   :header: "Benchmark","am62pxx_sk-fs: Score"

   "Glmark2-DRM","319.43 (min 306.00, max 353.00)"
   "Glmark2-Wayland","775.14 (min 766.00, max 785.00)"

***********************
Linux OSPI Flash Driver
***********************

.. rubric:: AM62PXX-SK
   :name: am62pxx-sk-ospi

.. rubric:: UBIFS
   :name: am62pxx-sk-ospi-ubifs

.. csv-table:: OSPI Flash Driver
   :header: "Buffer size (bytes)","am62pxx_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Write UBIFS CPU Load (%)","am62pxx_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Read UBIFS CPU Load (%)"

   "102400","0.16 (min 0.11, max 0.27)","29.08 (min 24.84, max 35.33)","28.31 (min 27.99, max 28.64)","6.14 (min 0.00, max 12.90)"
   "262144","0.13 (min 0.10, max 0.18)","30.30 (min 25.96, max 33.72)","28.20 (min 27.99, max 28.59)","9.45 (min 6.90, max 12.90)"
   "524288","0.13 (min 0.10, max 0.18)","30.14 (min 27.55, max 33.92)","28.17 (min 27.87, max 28.40)","8.05 (min 3.57, max 15.62)"
   "1048576","0.13 (min 0.10, max 0.18)","30.21 (min 26.68, max 32.81)","27.88 (min 27.61, max 28.29)","8.46 (min 3.45, max 12.90)"

.. rubric:: RAW
   :name: am62pxx-sk-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
   :header: "File size (Mbytes)","am62pxx_sk-fs: Raw Read Throughput (Mbytes/sec)"

   "50","37.84 (min 37.59, max 37.88)"

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
   :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

   "1m","91.07 (min 90.30, max 91.80)","1.58 (min 1.43, max 1.69)","283.71 (min 272.00, max 290.00)","2.77 (min 2.69, max 2.95)"
   "4m","96.79 (min 96.20, max 97.40)","1.11 (min 0.99, max 1.20)","273.14 (min 186.00, max 289.00)","1.96 (min 1.50, max 2.21)"
   "4k","79.06 (min 78.60, max 79.50)","23.30 (min 23.06, max 23.54)","88.36 (min 80.60, max 92.10)","19.01 (min 16.83, max 20.13)"
   "256k","91.33 (min 90.60, max 92.10)","2.15 (min 1.94, max 2.28)","288.43 (min 279.00, max 293.00)","4.00 (min 3.81, max 4.19)"

EMMC RAW FIO 1G
===============

.. csv-table:: EMMC RAW FIO 1G
   :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

   "1m","90.46 (min 89.70, max 91.30)","1.42 (min 1.27, max 1.57)","293.57 (min 292.00, max 294.00)","2.77 (min 2.56, max 2.95)"
   "4m","96.41 (min 93.60, max 97.50)","0.98 (min 0.92, max 1.09)","233.29 (min 179.00, max 293.00)","1.68 (min 1.37, max 2.07)"
   "4k","76.81 (min 76.30, max 77.40)","17.54 (min 17.28, max 17.78)","84.89 (min 78.50, max 89.80)","16.56 (min 14.54, max 18.02)"
   "256k","90.50 (min 89.90, max 91.40)","1.79 (min 1.68, max 1.93)","293.29 (min 292.00, max 294.00)","3.90 (min 3.64, max 4.03)"

EMMC EXT4
=========

.. csv-table:: EMMC EXT4
   :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

   "102400","91.49 (min 87.96, max 93.77)","3.60 (min 2.82, max 5.14)","178.60 (min 177.03, max 179.16)","5.80 (min 5.13, max 6.38)"
   "262144","84.78 (min 50.64, max 94.96)","2.49 (min 1.33, max 3.90)","180.78 (min 180.44, max 181.14)","4.62 (min 3.51, max 5.15)"
   "524288","79.01 (min 50.72, max 94.56)","2.30 (min 1.19, max 4.95)","180.28 (min 172.27, max 182.33)","5.08 (min 4.37, max 6.10)"
   "1048576","78.06 (min 47.78, max 94.56)","2.28 (min 1.14, max 4.05)","176.66 (min 153.32, max 181.84)","5.28 (min 4.35, max 6.90)"
   "5242880","77.05 (min 50.18, max 95.38)","2.29 (min 1.20, max 4.16)","179.73 (min 175.09, max 182.35)","4.86 (min 1.81, max 6.25)"

EMMC VFAT
=========

.. csv-table:: EMMC VFAT
   :header: "Buffer size (bytes)","am62pxx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Write VFAT CPU Load (%)","am62pxx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Read VFAT CPU Load (%)"

   "102400","39.37 (min 10.73, max 52.73)","4.93 (min 3.48, max 7.12)","208.63 (min 203.39, max 210.68)","10.24 (min 8.72, max 11.94)"
   "262144","44.91 (min 12.03, max 62.84)","5.73 (min 3.19, max 8.45)","288.50 (min 286.66, max 290.08)","14.01 (min 12.14, max 15.38)"
   "524288","51.31 (min 12.28, max 73.89)","5.02 (min 3.63, max 7.12)","287.38 (min 283.93, max 289.23)","13.68 (min 13.19, max 14.48)"
   "1048576","52.87 (min 12.43, max 75.86)","4.95 (min 3.24, max 6.65)","286.33 (min 284.39, max 288.82)","13.95 (min 12.50, max 15.65)"
   "5242880","55.47 (min 12.61, max 81.88)","5.09 (min 3.56, max 6.90)","287.17 (min 283.95, max 289.30)","15.18 (min 14.69, max 16.33)"

*****************
UBoot EMMC Driver
*****************

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

   "2000000","96696.35 (min 92564.97, max 98996.98)","217971.96 (min 166335.03, max 284939.13)"
   "4000000","96970.13 (min 94568.54, max 98996.98)","279814.51 (min 181038.67, max 302009.22)"

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
   :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

   "1m","43.14 (min 42.00, max 44.20)","1.04 (min 1.00, max 1.08)","87.19 (min 85.60, max 88.20)","1.30 (min 1.19, max 1.37)"
   "4m","42.04 (min 40.10, max 43.70)","0.72 (min 0.67, max 0.77)","85.59 (min 82.60, max 87.40)","0.91 (min 0.84, max 0.98)"
   "4k","2.81 (min 2.79, max 2.83)","1.63 (min 1.61, max 1.67)","12.94 (min 12.80, max 13.00)","3.99 (min 3.92, max 4.15)"
   "256k","39.83 (min 38.70, max 41.00)","1.34 (min 1.29, max 1.38)","84.23 (min 83.90, max 84.40)","1.52 (min 1.44, max 1.60)"

MMC RAW FIO 1G
==============

.. csv-table:: MMC RAW FIO 1G
   :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

   "1m","44.06 (min 42.70, max 45.90)","0.91 (min 0.84, max 1.00)","88.24 (min 88.20, max 88.30)","1.23 (min 1.18, max 1.32)"
   "4m","43.97 (min 42.20, max 45.90)","0.73 (min 0.71, max 0.76)","88.14 (min 88.10, max 88.30)","0.93 (min 0.85, max 1.00)"
   "4k","2.82 (min 2.81, max 2.84)","1.33 (min 1.20, max 1.44)","13.03 (min 13.00, max 13.10)","3.67 (min 3.52, max 3.76)"
   "256k","38.84 (min 36.70, max 41.90)","1.10 (min 1.05, max 1.20)","84.40 (min 84.30, max 84.50)","1.50 (min 1.39, max 1.57)"

MMC EXT4
========

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

   "102400","10.88 (min 10.32, max 11.30)","0.52 (min 0.35, max 0.74)","11.03 (min 10.68, max 11.83)","0.47 (min 0.37, max 0.55)"
   "262144","10.85 (min 10.22, max 11.10)","0.42 (min 0.24, max 0.62)","11.26 (min 11.01, max 11.46)","0.58 (min 0.43, max 0.98)"
   "524288","10.82 (min 10.40, max 11.09)","0.39 (min 0.28, max 0.73)","11.03 (min 10.79, max 11.31)","0.40 (min 0.32, max 0.49)"
   "1048576","10.91 (min 10.20, max 11.36)","0.38 (min 0.26, max 0.66)","11.65 (min 11.08, max 12.04)","0.43 (min 0.37, max 0.49)"
   "5242880","10.99 (min 10.46, max 11.32)","0.39 (min 0.29, max 0.62)","11.96 (min 11.53, max 12.03)","0.47 (min 0.39, max 0.54)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

***********
UBoot MMCSD
***********

UBOOT MMCSD FAT
===============

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

   "400000","30628.91 (min 22382.51, max 37236.36)","82636.50 (min 81920.00, max 83591.84)"
   "800000","42390.85 (min 34276.15, max 47906.43)","87020.71 (min 86231.58, max 88086.02)"
   "1000000","47710.97 (min 43690.67, max 49498.49)","89530.05"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

**********
USB Driver
**********

USB Device Controller
=====================

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
   :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

   "150","42.11 (min 38.50, max 44.50)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
   :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

   "150","37.60 (min 32.70, max 40.20)"

*************
CRYPTO Driver
*************

OpenSSL Performance
===================

.. csv-table:: OpenSSL Performance
   :header: "Algorithm","Buffer Size (in bytes)","am62pxx_sk-fs: throughput (KBytes/Sec)"

   "aes-128-cbc","1024","24429.62 (min 24108.37, max 24905.05)"
   "aes-128-cbc","16","477.79 (min 470.96, max 489.35)"
   "aes-128-cbc","16384","87933.71 (min 87610.71, max 88741.21)"
   "aes-128-cbc","256","7933.95 (min 7806.21, max 8099.50)"
   "aes-128-cbc","64","2116.10 (min 2074.41, max 2152.30)"
   "aes-128-cbc","8192","75273.56 (min 74746.54, max 76019.03)"
   "aes-128-ecb","1024","24986.87 (min 24752.81, max 25312.60)"
   "aes-128-ecb","16","489.40 (min 480.10, max 498.33)"
   "aes-128-ecb","16384","90466.99 (min 89096.19, max 91362.65)"
   "aes-128-ecb","256","8130.02 (min 8048.98, max 8207.79)"
   "aes-128-ecb","64","2177.44 (min 2146.58, max 2203.01)"
   "aes-128-ecb","8192","77265.77 (min 75617.62, max 77851.31)"
   "aes-192-cbc","1024","23969.74 (min 23711.74, max 24290.65)"
   "aes-192-cbc","16","479.11 (min 468.73, max 487.31)"
   "aes-192-cbc","16384","78909.24 (min 77807.62, max 79577.09)"
   "aes-192-cbc","256","7865.37 (min 7738.54, max 8036.69)"
   "aes-192-cbc","64","2122.50 (min 2087.15, max 2145.17)"
   "aes-192-cbc","8192","68549.88 (min 67422.89, max 69413.55)"
   "aes-192-ecb","1024","24422.89 (min 24150.70, max 24782.51)"
   "aes-192-ecb","16","490.05 (min 482.17, max 496.91)"
   "aes-192-ecb","16384","81241.23 (min 80145.07, max 82007.38)"
   "aes-192-ecb","256","8075.08 (min 7954.01, max 8184.58)"
   "aes-192-ecb","64","2169.85 (min 2142.51, max 2193.39)"
   "aes-192-ecb","8192","70734.02 (min 69490.01, max 71458.82)"
   "aes-256-cbc","1024","23320.14 (min 23097.00, max 23473.83)"
   "aes-256-cbc","16","478.85 (min 472.94, max 488.99)"
   "aes-256-cbc","16384","72152.02 (min 71319.55, max 72668.50)"
   "aes-256-cbc","256","7788.89 (min 7685.80, max 7903.57)"
   "aes-256-cbc","64","2118.88 (min 2089.11, max 2146.03)"
   "aes-256-cbc","8192","63632.34 (min 63285.93, max 63867.56)"
   "aes-256-ecb","1024","23828.24 (min 23729.15, max 23972.18)"
   "aes-256-ecb","16","489.08 (min 483.34, max 497.58)"
   "aes-256-ecb","16384","73770.13 (min 72717.65, max 74274.13)"
   "aes-256-ecb","256","8020.00 (min 7911.68, max 8156.16)"
   "aes-256-ecb","64","2165.64 (min 2134.91, max 2192.94)"
   "aes-256-ecb","8192","65016.00 (min 63621.80, max 65505.96)"
   "sha256","1024","31644.87 (min 30971.90, max 32175.10)"
   "sha256","16","525.95 (min 517.11, max 533.00)"
   "sha256","16384","277328.07 (min 274158.93, max 282858.84)"
   "sha256","256","8229.42 (min 8113.75, max 8353.79)"
   "sha256","64","2079.99 (min 2051.41, max 2108.12)"
   "sha256","8192","181620.54 (min 179268.27, max 184939.86)"
   "sha512","1024","26627.75 (min 26322.60, max 27056.47)"
   "sha512","16","510.67 (min 503.91, max 522.75)"
   "sha512","16384","110312.69 (min 109974.87, max 111078.06)"
   "sha512","256","7598.18 (min 7388.07, max 7866.20)"
   "sha512","64","2041.49 (min 2015.64, max 2087.00)"
   "sha512","8192","90946.80 (min 90477.91, max 91594.75)"

.. csv-table:: OpenSSL CPU Load
   :header: "Algorithm","am62pxx_sk-fs: CPU Load"

   "aes-128-cbc","32.43 (min 32.00, max 33.00)"
   "aes-128-ecb","33.57 (min 33.00, max 34.00)"
   "aes-192-cbc","32.29 (min 32.00, max 33.00)"
   "aes-192-ecb","33.00"
   "aes-256-cbc","32.00"
   "aes-256-ecb","32.43 (min 32.00, max 33.00)"
   "sha256","97.43 (min 96.00, max 98.00)"
   "sha512","97.43 (min 96.00, max 98.00)"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc
