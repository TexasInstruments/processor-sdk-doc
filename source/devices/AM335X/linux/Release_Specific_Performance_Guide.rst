==============================
 Linux 11.02 Performance Guide
==============================

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

System Benchmarks
-------------------

LMBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
   :header: "Benchmarks","am335x-evm: perf","beaglebone_green_eco-gp: perf"

   "af_unix_sock_stream_latency (microsec)","57.32 (min 56.70, max 57.65)","61.82 (min 56.24, max 71.97)"
   "af_unix_socket_stream_bandwidth (mb\s)","166.51 (min 159.23, max 173.50)","181.18 (min 174.29, max 191.62)"
   "bw_file_rd-io-1mb (mb/s)","180.13 (min 174.49, max 182.82)","207.41 (min 198.99, max 211.69)"
   "bw_file_rd-o2c-1mb (mb/s)","141.57 (min 139.47, max 144.89)","162.80 (min 154.01, max 168.15)"
   "bw_mem-bcopy-16mb (mb/s)","194.15 (min 178.65, max 199.37)","225.02 (min 218.00, max 230.28)"
   "bw_mem-bcopy-1mb (mb/s)","223.15 (min 220.39, max 224.19)","254.95 (min 247.04, max 260.59)"
   "bw_mem-bcopy-2mb (mb/s)","219.04 (min 216.17, max 220.22)","246.12 (min 242.69, max 252.81)"
   "bw_mem-bcopy-4mb (mb/s)","196.30 (min 187.81, max 199.48)","243.71 (min 238.01, max 246.73)"
   "bw_mem-bcopy-8mb (mb/s)","201.09 (min 185.15, max 213.04)","233.01 (min 226.33, max 238.00)"
   "bw_mem-bzero-16mb (mb/s)","991.85 (min 988.39, max 994.47)","1508.91 (min 1508.15, max 1509.72)"
   "bw_mem-bzero-1mb (mb/s)","604.18 (min 220.39, max 993.54)","880.46 (min 247.04, max 1509.05)"
   "bw_mem-bzero-2mb (mb/s)","601.62 (min 216.17, max 985.38)","877.67 (min 242.69, max 1509.89)"
   "bw_mem-bzero-4mb (mb/s)","591.61 (min 187.81, max 998.88)","874.01 (min 238.01, max 1508.86)"
   "bw_mem-bzero-8mb (mb/s)","593.62 (min 185.15, max 997.88)","869.66 (min 226.33, max 1508.30)"
   "bw_mem-cp-16mb (mb/s)","185.60 (min 174.74, max 194.82)","217.47 (min 216.44, max 219.29)"
   "bw_mem-cp-1mb (mb/s)","592.38 (min 182.05, max 985.71)","874.92 (min 237.56, max 1509.56)"
   "bw_mem-cp-2mb (mb/s)","593.34 (min 198.41, max 993.21)","872.85 (min 233.62, max 1510.12)"
   "bw_mem-cp-4mb (mb/s)","586.67 (min 183.87, max 1002.76)","871.49 (min 230.97, max 1508.49)"
   "bw_mem-cp-8mb (mb/s)","588.58 (min 182.61, max 1000.50)","866.06 (min 218.64, max 1508.86)"
   "bw_mem-fcp-16mb (mb/s)","178.38 (min 167.36, max 185.65)","207.75 (min 200.60, max 213.03)"
   "bw_mem-fcp-1mb (mb/s)","589.93 (min 186.78, max 993.54)","864.68 (min 216.26, max 1509.05)"
   "bw_mem-fcp-2mb (mb/s)","587.36 (min 184.11, max 985.38)","863.67 (min 213.70, max 1509.89)"
   "bw_mem-fcp-4mb (mb/s)","584.40 (min 180.12, max 998.88)","857.88 (min 207.95, max 1508.86)"
   "bw_mem-fcp-8mb (mb/s)","585.32 (min 182.56, max 997.88)","857.71 (min 205.33, max 1508.30)"
   "bw_mem-frd-16mb (mb/s)","247.67 (min 245.87, max 248.55)","278.49 (min 269.33, max 283.27)"
   "bw_mem-frd-1mb (mb/s)","230.80 (min 186.78, max 271.33)","261.97 (min 216.26, max 308.64)"
   "bw_mem-frd-2mb (mb/s)","220.13 (min 184.11, max 251.07)","250.34 (min 213.70, max 286.86)"
   "bw_mem-frd-4mb (mb/s)","214.60 (min 180.12, max 248.83)","245.55 (min 207.95, max 284.64)"
   "bw_mem-frd-8mb (mb/s)","216.02 (min 182.56, max 248.59)","243.65 (min 205.33, max 282.91)"
   "bw_mem-fwr-16mb (mb/s)","991.96 (min 985.59, max 994.28)","1507.45 (min 1504.04, max 1509.29)"
   "bw_mem-fwr-1mb (mb/s)","625.41 (min 261.51, max 985.71)","904.43 (min 286.08, max 1509.56)"
   "bw_mem-fwr-2mb (mb/s)","617.42 (min 248.88, max 993.21)","895.02 (min 274.57, max 1510.12)"
   "bw_mem-fwr-4mb (mb/s)","616.96 (min 244.14, max 1002.76)","893.30 (min 271.17, max 1508.49)"
   "bw_mem-fwr-8mb (mb/s)","618.33 (min 245.59, max 1000.50)","893.10 (min 269.74, max 1508.86)"
   "bw_mem-rd-16mb (mb/s)","250.44 (min 248.64, max 251.98)","284.97 (min 274.03, max 290.47)"
   "bw_mem-rd-1mb (mb/s)","625.37 (min 263.89, max 986.19)","906.56 (min 296.74, max 1509.43)"
   "bw_mem-rd-2mb (mb/s)","617.63 (min 246.91, max 985.06)","900.01 (min 277.89, max 1513.15)"
   "bw_mem-rd-4mb (mb/s)","617.89 (min 248.15, max 997.13)","893.00 (min 274.80, max 1507.16)"
   "bw_mem-rd-8mb (mb/s)","618.45 (min 248.22, max 994.65)","896.60 (min 274.25, max 1509.15)"
   "bw_mem-rdwr-16mb (mb/s)","201.31 (min 199.90, max 202.67)","234.29 (min 228.82, max 237.35)"
   "bw_mem-rdwr-1mb (mb/s)","203.67 (min 182.05, max 207.88)","240.35 (min 232.86, max 244.08)"
   "bw_mem-rdwr-2mb (mb/s)","202.18 (min 198.41, max 203.77)","236.29 (min 228.18, max 240.67)"
   "bw_mem-rdwr-4mb (mb/s)","194.39 (min 183.87, max 202.21)","235.69 (min 228.83, max 239.46)"
   "bw_mem-rdwr-8mb (mb/s)","195.35 (min 182.61, max 203.21)","229.72 (min 218.64, max 238.89)"
   "bw_mem-wr-16mb (mb/s)","992.61 (min 991.14, max 994.41)","1505.84 (min 1504.04, max 1508.72)"
   "bw_mem-wr-1mb (mb/s)","595.03 (min 206.27, max 986.19)","871.65 (min 232.86, max 1509.43)"
   "bw_mem-wr-2mb (mb/s)","593.12 (min 200.58, max 985.06)","872.46 (min 228.18, max 1513.15)"
   "bw_mem-wr-4mb (mb/s)","593.65 (min 201.89, max 997.13)","868.02 (min 228.83, max 1507.16)"
   "bw_mem-wr-8mb (mb/s)","594.74 (min 201.64, max 994.65)","871.96 (min 228.66, max 1509.15)"
   "bw_mmap_rd-mo-1mb (mb/s)","249.61 (min 247.99, max 252.56)","290.27 (min 273.45, max 301.11)"
   "bw_mmap_rd-o2c-1mb (mb/s)","154.94 (min 151.54, max 158.25)","173.10 (min 162.07, max 180.25)"
   "bw_pipe (mb/s)","302.55 (min 286.94, max 328.87)","392.73 (min 337.23, max 424.16)"
   "bw_unix (mb/s)","166.51 (min 159.23, max 173.50)","181.18 (min 174.29, max 191.62)"
   "lat_connect (us)","100.21 (min 98.59, max 101.91)","104.26 (min 95.27, max 119.61)"
   "lat_ctx-2-128k (us)","45.64 (min 37.59, max 64.00)","36.78 (min 18.72, max 62.95)"
   "lat_ctx-2-256k (us)","8.60 (min 4.00, max 27.00)","11.67 (min 3.22, max 27.80)"
   "lat_ctx-4-128k (us)","53.62 (min 41.81, max 62.86)","59.60 (min 47.57, max 70.42)"
   "lat_ctx-4-256k (us)","0.00","0.00"
   "lat_fs-0k (num_files)","151.60 (min 137.00, max 173.00)","156.67 (min 138.00, max 175.00)"
   "lat_fs-10k (num_files)","68.80 (min 62.00, max 72.00)","70.00 (min 65.00, max 73.00)"
   "lat_fs-1k (num_files)","99.20 (min 97.00, max 102.00)","97.67 (min 79.00, max 108.00)"
   "lat_fs-4k (num_files)","95.00 (min 88.00, max 101.00)","100.00 (min 83.00, max 111.00)"
   "lat_mem_rd-stride128-sz1000k (ns)","227.09 (min 221.99, max 234.53)","204.00 (min 198.76, max 207.01)"
   "lat_mem_rd-stride128-sz125k (ns)","14.68 (min 11.63, max 26.38)","12.62 (min 11.64, max 14.55)"
   "lat_mem_rd-stride128-sz250k (ns)","72.76 (min 56.79, max 84.33)","52.09 (min 37.95, max 72.45)"
   "lat_mem_rd-stride128-sz31k (ns)","3.04 (min 3.03, max 3.06)","3.29 (min 3.03, max 3.80)"
   "lat_mem_rd-stride128-sz50 (ns)","3.01 (min 3.00, max 3.02)","3.26 (min 3.01, max 3.76)"
   "lat_mem_rd-stride128-sz500k (ns)","184.98 (min 183.31, max 186.85)","170.38 (min 169.34, max 171.91)"
   "lat_mem_rd-stride128-sz62k (ns)","8.85 (min 8.71, max 8.96)","9.62 (min 8.82, max 11.16)"
   "lat_mmap-1m (us)","128.00 (min 104.00, max 141.00)","115.00 (min 90.00, max 144.00)"
   "lat_ops-double-add (ns)","8.98 (min 8.95, max 9.00)","9.70 (min 8.91, max 11.20)"
   "lat_ops-double-div (ns)","57.41 (min 57.30, max 57.49)","62.23 (min 57.31, max 71.88)"
   "lat_ops-double-mul (ns)","11.09 (min 11.05, max 11.12)","11.99 (min 11.05, max 13.84)"
   "lat_ops-float-add (ns)","8.99 (min 8.94, max 9.07)","9.73 (min 8.99, max 11.21)"
   "lat_ops-float-div (ns)","33.33 (min 33.19, max 33.57)","36.06 (min 33.26, max 41.50)"
   "lat_ops-float-mul (ns)","10.08 (min 10.05, max 10.12)","10.91 (min 10.05, max 12.59)"
   "lat_ops-int-add (ns)","1.01","1.10 (min 1.01, max 1.27)"
   "lat_ops-int-bit (ns)","0.67","0.73 (min 0.67, max 0.84)"
   "lat_ops-int-div (ns)","73.02 (min 72.67, max 73.19)","79.26 (min 72.82, max 91.57)"
   "lat_ops-int-mod (ns)","25.51 (min 25.44, max 25.58)","27.61 (min 25.47, max 31.84)"
   "lat_ops-int-mul (ns)","6.58 (min 6.56, max 6.60)","7.14 (min 6.59, max 8.25)"
   "lat_ops-int64-add (ns)","1.06 (min 1.05, max 1.07)","1.15 (min 1.06, max 1.32)"
   "lat_ops-int64-bit (ns)","0.68","0.74 (min 0.68, max 0.85)"
   "lat_ops-int64-div (ns)","189.07 (min 188.55, max 189.45)","205.66 (min 189.59, max 236.27)"
   "lat_ops-int64-mod (ns)","52.22 (min 52.12, max 52.40)","56.77 (min 52.12, max 66.00)"
   "lat_ops-int64-mul (ns)","6.51 (min 6.49, max 6.55)","7.04 (min 6.49, max 8.13)"
   "lat_pagefault (us)","2.37 (min 2.32, max 2.41)","2.21 (min 2.04, max 2.51)"
   "lat_pipe (us)","45.68 (min 45.20, max 46.26)","43.48 (min 39.75, max 50.40)"
   "lat_proc-exec (us)","1629.35 (min 1534.25, max 1722.25)","1556.50 (min 1418.50, max 1739.50)"
   "lat_proc-fork (us)","1447.40 (min 1374.50, max 1542.75)","1349.83 (min 1286.00, max 1475.25)"
   "lat_proc-proccall (us)","0.02","0.02"
   "lat_select (us)","58.91 (min 57.90, max 59.85)","63.80 (min 58.52, max 73.56)"
   "lat_sem (us)","13.65 (min 13.54, max 13.76)","14.78 (min 13.39, max 17.27)"
   "lat_sig-catch (us)","9.30 (min 9.26, max 9.37)","10.04 (min 9.19, max 11.72)"
   "lat_sig-install (us)","1.47 (min 1.45, max 1.50)","1.60 (min 1.47, max 1.84)"
   "lat_sig-prot (us)","0.94 (min 0.86, max 1.11)","1.06 (min 0.94, max 1.18)"
   "lat_syscall-fstat (us)","2.91 (min 2.84, max 3.04)","3.13 (min 2.84, max 3.65)"
   "lat_syscall-null (us)","0.50","0.54 (min 0.50, max 0.62)"
   "lat_syscall-open (us)","483.61 (min 398.93, max 591.10)","467.73 (min 411.46, max 526.73)"
   "lat_syscall-read (us)","0.97 (min 0.94, max 1.05)","1.03 (min 0.94, max 1.18)"
   "lat_syscall-stat (us)","7.09 (min 7.04, max 7.17)","7.66 (min 7.06, max 8.79)"
   "lat_syscall-write (us)","0.75 (min 0.74, max 0.75)","0.81 (min 0.74, max 0.93)"
   "lat_tcp (us)","1.16","1.26 (min 1.16, max 1.45)"
   "lat_unix (us)","57.32 (min 56.70, max 57.65)","61.82 (min 56.24, max 71.97)"
   "latency_for_0.50_mb_block_size (nanosec)","184.98 (min 183.31, max 186.85)","170.38 (min 169.34, max 171.91)"
   "latency_for_1.00_mb_block_size (nanosec)","113.55 (min 0.00, max 234.53)","102.00 (min 0.00, max 207.01)"
   "pipe_bandwidth (mb\s)","302.55 (min 286.94, max 328.87)","392.73 (min 337.23, max 424.16)"
   "pipe_latency (microsec)","45.68 (min 45.20, max 46.26)","43.48 (min 39.75, max 50.40)"
   "procedure_call (microsec)","0.02","0.02"
   "select_on_200_tcp_fds (microsec)","58.91 (min 57.90, max 59.85)","63.80 (min 58.52, max 73.56)"
   "semaphore_latency (microsec)","13.65 (min 13.54, max 13.76)","14.78 (min 13.39, max 17.27)"
   "signal_handler_latency (microsec)","1.47 (min 1.45, max 1.50)","1.60 (min 1.47, max 1.84)"
   "signal_handler_overhead (microsec)","9.30 (min 9.26, max 9.37)","10.04 (min 9.19, max 11.72)"
   "tcp_ip_connection_cost_to_localhost (microsec)","100.21 (min 98.59, max 101.91)","104.26 (min 95.27, max 119.61)"
   "tcp_latency_using_localhost (microsec)","1.16","1.26 (min 1.16, max 1.45)"

Dhrystone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed.

Please take note, different run may produce different slightly results.
This is advised to run this test multiple times in order to get maximum 
performance numbers.

Execute the benchmark with the following:

::

   runDhrystone

.. csv-table:: Dhrystone Benchmarks
   :header: "Benchmarks","am335x-evm: perf","beaglebone_green_eco-gp: perf"

   "cpu_clock (mhz)","1000.00","900.00 (min 800.00, max 1000.00)"
   "dhrystone_per_mhz (dmips/mhz)","1.94 (min 1.90, max 2.00)","1.90"
   "dhrystone_per_second (dhrystonep)","3413208.62 (min 3389830.50, max 3448275.80)","3064778.25 (min 2739726.00, max 3389830.50)"

Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

   runWhetstone

.. csv-table:: Whetstone Benchmarks
   :header: "Benchmarks","am335x-evm: perf","beaglebone_green_eco-gp: perf"

   "whetstone (mips)","866.64 (min 833.30, max 1000.00)","773.80 (min 714.30, max 833.30)"

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
   :header: "Benchmarks","am335x-evm: perf","beaglebone_green_eco-gp: perf"

   "linpack (kflops)","49734.67 (min 49519.00, max 50099.00)","44991.50 (min 39832.00, max 50118.00)"

NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
   :header: "Benchmarks","am335x-evm: perf","beaglebone_green_eco-gp: perf"

   "assignment (iterations)","7.89 (min 7.86, max 7.91)","6.86 (min 6.33, max 7.91)"
   "fourier (iterations)","2897.06 (min 2894.40, max 2899.40)","2512.30 (min 2316.80, max 2900.40)"
   "fp_emulation (iterations)","73.21 (min 72.99, max 73.43)","63.66 (min 58.78, max 73.40)"
   "huffman (iterations)","731.14 (min 730.34, max 731.93)","634.63 (min 585.67, max 732.40)"
   "idea (iterations)","1703.00 (min 1701.50, max 1704.10)","1477.13 (min 1363.40, max 1704.60)"
   "lu_decomposition (iterations)","76.03 (min 75.76, max 76.32)","66.23 (min 61.13, max 76.38)"
   "neural_net (iterations)","2.07","1.80 (min 1.66, max 2.07)"
   "numeric_sort (iterations)","346.51 (min 346.05, max 346.93)","300.72 (min 277.57, max 346.98)"
   "string_sort (iterations)","69.45 (min 69.39, max 69.53)","60.24 (min 55.59, max 69.53)"

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

::

   stream_c

.. csv-table:: Stream Benchmarks
   :header: "Benchmarks","am335x-evm: perf","beaglebone_green_eco-gp: perf"

   "add (mb/s)","526.28 (min 521.30, max 531.90)","599.05 (min 578.10, max 619.20)"
   "copy (mb/s)","476.98 (min 471.70, max 483.50)","567.28 (min 541.00, max 590.60)"
   "scale (mb/s)","614.24 (min 610.60, max 619.00)","776.88 (min 719.10, max 832.90)"
   "triad (mb/s)","445.32 (min 439.90, max 454.20)","509.23 (min 482.90, max 536.50)"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
   :header: "Boot Configuration","am335x-evm: Boot time in seconds: avg(min,max)","beaglebone_green_eco-gp: Boot time in seconds: avg(min,max)"

   "Linux boot time from SD with default rootfs (20 boot cycles)","55.37 (min 54.87, max 55.77)","48.46 (min 47.18, max 48.93)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

Graphics SGX/RGX Driver
-------------------------

Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
   :header: "Benchmark","am335x-evm: Score"

   "Glmark2-DRM","73.00"
   "Glmark2-Wayland","54.00"

|

NAND Driver
-------------------------

.. rubric:: AM335X-EVM
   :name: am335x-evm-nand-driver

.. csv-table:: NAND Performance
   :header: "Buffer size (bytes)","am335x-evm: Write UBIFS Throughput (Mbytes/sec)","am335x-evm: Write UBIFS CPU Load (%)","am335x-evm: Read UBIFS Throughput (Mbytes/sec)","am335x-evm: Read UBIFS CPU Load (%)"

   "102400","3.21 (min 3.13, max 3.33)","73.78 (min 72.37, max 74.86)","5.93 (min 5.90, max 5.96)","39.32 (min 38.01, max 41.15)"
   "262144","3.21 (min 3.16, max 3.32)","70.88 (min 69.25, max 71.85)","5.90 (min 5.88, max 5.92)","39.25 (min 38.56, max 39.91)"
   "524288","3.14 (min 3.09, max 3.18)","74.65 (min 73.91, max 75.45)","5.88 (min 5.86, max 5.89)","40.08 (min 39.49, max 40.82)"
   "1048576","3.16 (min 3.12, max 3.18)","74.45 (min 73.88, max 74.98)","5.94 (min 5.90, max 5.96)","39.00 (min 38.04, max 40.08)"
   "5242880","3.16 (min 3.14, max 3.18)","74.33 (min 73.69, max 74.96)","5.95 (min 5.93, max 5.97)","38.60 (min 37.94, max 39.54)"

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
   :header: "Buffer size (bytes)","am335x-evm: Write EXT4 Throughput (Mbytes/sec)","am335x-evm: Write EXT4 CPU Load (%)","am335x-evm: Read EXT4 Throughput (Mbytes/sec)","am335x-evm: Read EXT4 CPU Load (%)"

   "1m","19.26 (min 18.80, max 19.60)","9.57 (min 8.93, max 10.05)","20.72 (min 20.20, max 21.20)","11.55 (min 11.07, max 12.31)"
   "4m","19.46 (min 18.90, max 19.80)","8.14 (min 7.67, max 8.91)","20.92 (min 20.40, max 21.40)","10.12 (min 9.21, max 10.79)"
   "4k","2.30 (min 2.29, max 2.31)","33.02 (min 31.64, max 34.45)","8.35 (min 8.30, max 8.40)","41.29 (min 36.91, max 42.92)"
   "256k","18.18 (min 17.50, max 18.50)","13.31 (min 12.56, max 13.90)","20.20 (min 19.60, max 20.50)","14.98 (min 14.30, max 15.76)"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","am335x-evm: Write Raw Throughput (Mbytes/sec)","am335x-evm: Write Raw CPU Load (%)","am335x-evm: Read Raw Throughput (Mbytes/sec)","am335x-evm: Read Raw CPU Load (%)"

   "102400","18.35 (min 17.30, max 20.02)","16.77 (min 14.06, max 23.34)","19.16 (min 19.04, max 19.35)","23.14 (min 21.43, max 25.60)"
   "262144","17.93 (min 17.37, max 19.28)","16.67 (min 14.68, max 21.40)","20.22 (min 19.67, max 20.65)","18.58 (min 17.77, max 19.57)"
   "524288","18.20 (min 17.34, max 19.46)","16.95 (min 14.89, max 22.04)","21.02 (min 20.64, max 21.42)","16.68 (min 16.02, max 17.12)"
   "1048576","18.25 (min 17.67, max 19.68)","17.46 (min 14.83, max 23.26)","22.40 (min 22.35, max 22.46)","18.10 (min 17.33, max 19.21)"
   "5242880","18.66 (min 17.90, max 19.87)","16.92 (min 14.16, max 21.45)","22.43 (min 22.29, max 22.50)","18.30 (min 17.66, max 19.04)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

|

USB Driver
-------------------------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
   :header: "Number of Blocks","am335x-evm: Throughput (MB/sec)"

   "150","63.85 (min 56.70, max 71.00)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
   :header: "Number of Blocks","am335x-evm: Throughput (MB/sec)"

   "150","39.70 (min 14.20, max 65.20)"

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
   :header: "Algorithm","Buffer Size (in bytes)","am335x-evm: throughput (KBytes/Sec)","beaglebone_green_eco-gp: throughput (KBytes/Sec)"

   "aes-128-cbc","1024","44867.72 (min 44698.97, max 45007.19)","40543.66 (min 36034.90, max 45085.01)"
   "aes-128-cbc","16","29336.34 (min 28146.99, max 29690.50)","26273.19 (min 22176.13, max 29744.81)"
   "aes-128-cbc","16384","44968.62 (min 44711.94, max 45443.75)","40843.95 (min 36328.79, max 45394.60)"
   "aes-128-cbc","256","43805.47 (min 43729.32, max 43922.69)","39504.87 (min 35104.60, max 43905.02)"
   "aes-128-cbc","64","39670.89 (min 39525.21, max 39778.84)","34768.81 (min 30877.21, max 39806.78)"
   "aes-128-cbc","8192","45247.15 (min 45042.35, max 45424.64)","40870.57 (min 36306.94, max 45430.10)"
   "aes-128-ecb","1024","45828.64 (min 45761.19, max 45975.21)","40213.59 (min 32413.35, max 45956.10)"
   "aes-128-ecb","16","33491.15 (min 33372.82, max 33574.76)","29274.30 (min 26860.44, max 33648.54)"
   "aes-128-ecb","16384","45982.24 (min 45809.66, max 46191.96)","41413.29 (min 36279.64, max 46235.65)"
   "aes-128-ecb","256","44920.10 (min 44784.64, max 45075.37)","40451.97 (min 36071.94, max 45065.81)"
   "aes-128-ecb","64","41845.05 (min 41695.83, max 41997.59)","37356.46 (min 33494.23, max 41998.89)"
   "aes-128-ecb","8192","46124.24 (min 46014.46, max 46271.15)","41251.50 (min 35556.01, max 46254.76)"
   "aes-192-cbc","1024","36906.80 (min 36759.21, max 37142.19)","33314.13 (min 29543.77, max 37066.07)"
   "aes-192-cbc","16","25842.75 (min 25644.13, max 25987.24)","23373.78 (min 20733.91, max 25991.41)"
   "aes-192-cbc","16384","37083.55 (min 36907.69, max 37218.99)","33581.74 (min 29840.73, max 37350.06)"
   "aes-192-cbc","256","36124.07 (min 35959.04, max 36243.46)","32572.86 (min 28911.70, max 36224.43)"
   "aes-192-cbc","64","33293.88 (min 33239.21, max 33384.75)","29900.48 (min 25979.31, max 33413.57)"
   "aes-192-cbc","8192","37181.30 (min 37027.84, max 37470.21)","33598.81 (min 29799.77, max 37440.17)"
   "aes-192-ecb","1024","39483.12 (min 39440.38, max 39547.90)","35608.23 (min 31605.76, max 39602.86)"
   "aes-192-ecb","16","30049.00 (min 29978.45, max 30128.36)","26481.94 (min 21620.30, max 30104.27)"
   "aes-192-ecb","16384","39583.74 (min 39343.45, max 39774.89)","35785.39 (min 31828.65, max 39758.51)"
   "aes-192-ecb","256","38803.30 (min 38734.68, max 38894.85)","34930.52 (min 30859.86, max 38938.97)"
   "aes-192-ecb","64","36472.74 (min 36409.64, max 36580.57)","32651.67 (min 28241.30, max 36572.67)"
   "aes-192-ecb","8192","39610.50 (min 39428.10, max 39774.89)","35765.59 (min 31776.77, max 39753.05)"
   "aes-256-cbc","1024","33042.30 (min 32937.64, max 33148.25)","29809.92 (min 26489.17, max 33154.73)"
   "aes-256-cbc","16","23951.28 (min 23914.03, max 24043.51)","21604.21 (min 19188.28, max 24054.00)"
   "aes-256-cbc","16384","33157.94 (min 32713.39, max 33346.90)","30003.20 (min 26662.23, max 33341.44)"
   "aes-256-cbc","256","32448.87 (min 32383.91, max 32539.90)","29264.90 (min 26027.01, max 32505.43)"
   "aes-256-cbc","64","30097.08 (min 30023.66, max 30150.17)","27145.66 (min 24085.46, max 30213.76)"
   "aes-256-cbc","8192","33194.53 (min 33024.68, max 33325.06)","29971.80 (min 26648.58, max 33335.98)"
   "aes-256-ecb","1024","34616.25 (min 34555.22, max 34653.18)","31241.56 (min 27767.81, max 34754.56)"
   "aes-256-ecb","16","27148.98 (min 27091.19, max 27222.23)","24499.54 (min 21769.09, max 27239.27)"
   "aes-256-ecb","16384","34754.83 (min 34657.62, max 34870.61)","30956.20 (min 26198.02, max 34865.15)"
   "aes-256-ecb","256","34175.27 (min 34110.89, max 34273.54)","30823.62 (min 27367.94, max 34275.24)"
   "aes-256-ecb","64","32304.96 (min 32254.91, max 32401.56)","29129.81 (min 25858.28, max 32376.26)"
   "aes-256-ecb","8192","34798.52 (min 34736.81, max 34892.46)","31401.30 (min 27915.61, max 34908.84)"
   "des3","1024","4021.18 (min 3851.95, max 4080.64)","3618.05 (min 3255.30, max 4073.47)"
   "des3","16","3786.75 (min 3653.41, max 3869.72)","3473.70 (min 3103.46, max 3879.10)"
   "des3","16384","4066.51 (min 4057.77, max 4079.62)","3611.31 (min 3249.49, max 4079.62)"
   "des3","256","4004.42 (min 3832.32, max 4056.23)","3658.30 (min 3252.05, max 4068.01)"
   "des3","64","3949.63 (min 3712.70, max 4025.07)","3622.76 (min 3226.26, max 4027.37)"
   "des3","8192","4020.09 (min 3852.97, max 4076.89)","3609.94 (min 3063.81, max 4079.62)"
   "md5","1024","118451.95 (min 117416.28, max 118936.92)","107242.50 (min 95363.07, max 119226.37)"
   "md5","16","6339.70 (min 6266.33, max 6379.15)","5755.89 (min 5112.16, max 6395.94)"
   "md5","16384","162885.36 (min 162512.90, max 163474.09)","147004.07 (min 130624.17, max 163561.47)"
   "md5","256","63196.48 (min 62180.86, max 63712.43)","57189.74 (min 50839.47, max 63521.71)"
   "md5","64","22078.11 (min 21832.32, max 22201.79)","19964.42 (min 17763.33, max 22179.41)"
   "md5","8192","158970.68 (min 158504.28, max 159435.43)","143465.13 (min 127344.64, max 159602.01)"
   "sha1","1024","99903.90 (min 97011.71, max 100954.11)","90590.38 (min 80547.16, max 100657.83)"
   "sha1","16","6380.82 (min 6145.69, max 6510.23)","5804.14 (min 5119.14, max 6486.83)"
   "sha1","16384","127800.66 (min 122650.62, max 130165.42)","116594.01 (min 101924.86, max 130170.88)"
   "sha1","256","56994.18 (min 55117.99, max 58188.03)","51933.08 (min 45230.34, max 58224.81)"
   "sha1","64","20973.81 (min 19979.63, max 21547.84)","19283.66 (min 17055.62, max 21573.59)"
   "sha1","8192","126776.66 (min 123098.45, max 128704.51)","115866.28 (min 103030.78, max 128780.97)"
   "sha224","1024","59564.92 (min 59410.77, max 59874.65)","53707.69 (min 47753.56, max 59685.21)"
   "sha224","16","5325.87 (min 5253.98, max 5402.44)","4768.37 (min 4244.29, max 5304.11)"
   "sha224","16384","70976.58 (min 70871.72, max 71232.17)","64050.52 (min 56912.55, max 71166.63)"
   "sha224","256","38894.27 (min 38675.37, max 39190.27)","34535.38 (min 30139.31, max 38894.76)"
   "sha224","64","16309.64 (min 16136.73, max 16513.47)","14652.87 (min 13028.59, max 16281.96)"
   "sha224","8192","70484.51 (min 70249.13, max 70776.15)","63563.09 (min 56497.49, max 70694.23)"
   "sha256","1024","59347.15 (min 59060.57, max 59581.10)","53368.66 (min 47663.10, max 59646.63)"
   "sha256","16","5242.32 (min 5106.42, max 5321.37)","4707.52 (min 4188.81, max 5294.98)"
   "sha256","16384","71047.58 (min 70931.80, max 71330.47)","64154.28 (min 57005.40, max 71308.63)"
   "sha256","256","38497.02 (min 38064.81, max 38718.81)","33938.84 (min 30851.24, max 37366.19)"
   "sha256","64","16116.93 (min 15817.02, max 16270.42)","14417.05 (min 12791.40, max 16257.88)"
   "sha256","8192","70364.91 (min 70175.40, max 70516.74)","63223.81 (min 56418.30, max 70593.19)"
   "sha512","1024","35821.50 (min 35697.32, max 35953.66)","32361.64 (min 28662.10, max 35977.56)"
   "sha512","16","3144.34 (min 3126.37, max 3158.76)","2819.52 (min 2455.91, max 3162.56)"
   "sha512","16384","43062.61 (min 42882.39, max 43215.53)","38886.06 (min 34532.01, max 43215.53)"
   "sha512","256","23309.24 (min 23240.02, max 23392.26)","20995.93 (min 18459.05, max 23385.86)"
   "sha512","64","12444.62 (min 12369.94, max 12479.10)","11160.48 (min 9683.50, max 12515.97)"
   "sha512","8192","42435.65 (min 42319.87, max 42598.40)","38321.49 (min 34051.41, max 42603.86)"

.. csv-table:: OpenSSL CPU Load
   :header: "Algorithm","am335x-evm: CPU Load","beaglebone_green_eco-gp: CPU Load"

   "aes-128-cbc","98.80 (min 98.00, max 99.00)","98.50 (min 98.00, max 99.00)"
   "aes-128-ecb","99.00","99.00"
   "aes-192-cbc","99.00","99.00"
   "aes-192-ecb","99.00","99.00"
   "aes-256-cbc","99.00","99.00"
   "aes-256-ecb","99.00","98.75 (min 98.00, max 99.00)"
   "des3","98.00","98.25 (min 98.00, max 99.00)"
   "md5","99.00","99.00"
   "sha1","98.20 (min 98.00, max 99.00)","99.00"
   "sha224","99.00","99.00"
   "sha256","99.00","98.50 (min 98.00, max 99.00)"
   "sha386","83.20 (min 82.00, max 85.00)","85.75 (min 81.00, max 88.00)"
   "sha512","99.00","99.00"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

   time -v openssl speed -elapsed -evp aes-128-cbc
