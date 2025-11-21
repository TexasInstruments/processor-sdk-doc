
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
   :header: "Benchmarks","am43xx-gpevm: perf"

   "af_unix_sock_stream_latency (microsec)","41.33 (min 40.89, max 42.10)"
   "af_unix_socket_stream_bandwidth (mb\s)","180.59 (min 175.47, max 184.87)"
   "bw_file_rd-io-1mb (mb/s)","200.11 (min 196.93, max 203.40)"
   "bw_file_rd-o2c-1mb (mb/s)","160.55 (min 157.90, max 162.60)"
   "bw_mem-bcopy-16mb (mb/s)","196.36 (min 195.77, max 197.05)"
   "bw_mem-bcopy-1mb (mb/s)","199.82 (min 198.29, max 200.70)"
   "bw_mem-bcopy-2mb (mb/s)","198.00 (min 197.10, max 199.00)"
   "bw_mem-bcopy-4mb (mb/s)","198.03 (min 197.37, max 199.03)"
   "bw_mem-bcopy-8mb (mb/s)","196.32 (min 195.54, max 196.71)"
   "bw_mem-bzero-16mb (mb/s)","670.50 (min 668.20, max 672.41)"
   "bw_mem-bzero-1mb (mb/s)","436.65 (min 198.29, max 673.85)"
   "bw_mem-bzero-2mb (mb/s)","435.31 (min 197.10, max 673.29)"
   "bw_mem-bzero-4mb (mb/s)","435.47 (min 197.37, max 673.06)"
   "bw_mem-bzero-8mb (mb/s)","434.28 (min 195.54, max 672.95)"
   "bw_mem-cp-16mb (mb/s)","198.16 (min 197.18, max 199.23)"
   "bw_mem-cp-1mb (mb/s)","437.06 (min 200.20, max 674.08)"
   "bw_mem-cp-2mb (mb/s)","436.59 (min 198.26, max 673.63)"
   "bw_mem-cp-4mb (mb/s)","436.14 (min 197.88, max 673.17)"
   "bw_mem-cp-8mb (mb/s)","435.63 (min 197.25, max 672.95)"
   "bw_mem-fcp-16mb (mb/s)","240.09 (min 238.79, max 240.88)"
   "bw_mem-fcp-1mb (mb/s)","458.71 (min 243.25, max 673.85)"
   "bw_mem-fcp-2mb (mb/s)","457.83 (min 242.48, max 673.29)"
   "bw_mem-fcp-4mb (mb/s)","456.71 (min 239.38, max 673.06)"
   "bw_mem-fcp-8mb (mb/s)","456.36 (min 239.16, max 672.95)"
   "bw_mem-frd-16mb (mb/s)","200.45 (min 198.47, max 202.74)"
   "bw_mem-frd-1mb (mb/s)","225.55 (min 205.23, max 244.56)"
   "bw_mem-frd-2mb (mb/s)","224.09 (min 202.63, max 243.64)"
   "bw_mem-frd-4mb (mb/s)","220.10 (min 198.48, max 241.43)"
   "bw_mem-frd-8mb (mb/s)","221.05 (min 200.01, max 241.77)"
   "bw_mem-fwr-16mb (mb/s)","671.17 (min 670.58, max 672.01)"
   "bw_mem-fwr-1mb (mb/s)","440.43 (min 205.23, max 674.08)"
   "bw_mem-fwr-2mb (mb/s)","439.21 (min 202.63, max 673.63)"
   "bw_mem-fwr-4mb (mb/s)","436.14 (min 198.48, max 673.17)"
   "bw_mem-fwr-8mb (mb/s)","436.88 (min 200.01, max 672.95)"
   "bw_mem-rd-16mb (mb/s)","312.70 (min 311.82, max 313.40)"
   "bw_mem-rd-1mb (mb/s)","293.51 (min 270.82, max 316.26)"
   "bw_mem-rd-2mb (mb/s)","290.28 (min 266.42, max 312.99)"
   "bw_mem-rd-4mb (mb/s)","290.97 (min 267.76, max 313.77)"
   "bw_mem-rd-8mb (mb/s)","291.13 (min 269.09, max 313.01)"
   "bw_mem-rdwr-16mb (mb/s)","244.57 (min 242.33, max 245.66)"
   "bw_mem-rdwr-1mb (mb/s)","224.05 (min 200.20, max 249.16)"
   "bw_mem-rdwr-2mb (mb/s)","222.66 (min 198.26, max 245.64)"
   "bw_mem-rdwr-4mb (mb/s)","222.03 (min 197.88, max 245.55)"
   "bw_mem-rdwr-8mb (mb/s)","222.20 (min 197.25, max 245.60)"
   "bw_mem-wr-16mb (mb/s)","269.57 (min 268.33, max 270.24)"
   "bw_mem-wr-1mb (mb/s)","259.75 (min 245.19, max 272.26)"
   "bw_mem-wr-2mb (mb/s)","257.18 (min 245.19, max 269.94)"
   "bw_mem-wr-4mb (mb/s)","256.92 (min 243.41, max 270.43)"
   "bw_mem-wr-8mb (mb/s)","257.49 (min 244.77, max 270.26)"
   "bw_mmap_rd-mo-1mb (mb/s)","206.82 (min 205.99, max 207.60)"
   "bw_mmap_rd-o2c-1mb (mb/s)","152.96 (min 151.08, max 155.52)"
   "bw_pipe (mb/s)","341.01 (min 296.40, max 356.89)"
   "bw_unix (mb/s)","180.59 (min 175.47, max 184.87)"
   "lat_connect (us)","80.12 (min 78.59, max 81.01)"
   "lat_ctx-2-128k (us)","3.59 (min 0.00, max 10.83)"
   "lat_ctx-2-256k (us)","12.95 (min 0.00, max 33.69)"
   "lat_ctx-4-128k (us)","7.15 (min 0.00, max 12.55)"
   "lat_ctx-4-256k (us)","0.00"
   "lat_fs-0k (num_files)","203.20 (min 180.00, max 223.00)"
   "lat_fs-10k (num_files)","73.60 (min 69.00, max 80.00)"
   "lat_fs-1k (num_files)","117.80 (min 112.00, max 124.00)"
   "lat_fs-4k (num_files)","114.00 (min 105.00, max 120.00)"
   "lat_mem_rd-stride128-sz1000k (ns)","99.08 (min 98.47, max 99.85)"
   "lat_mem_rd-stride128-sz125k (ns)","15.97 (min 15.87, max 16.06)"
   "lat_mem_rd-stride128-sz250k (ns)","37.66 (min 31.64, max 44.45)"
   "lat_mem_rd-stride128-sz31k (ns)","7.16 (min 4.01, max 9.26)"
   "lat_mem_rd-stride128-sz50 (ns)","4.01"
   "lat_mem_rd-stride128-sz500k (ns)","91.64 (min 88.08, max 93.55)"
   "lat_mem_rd-stride128-sz62k (ns)","16.75 (min 16.40, max 17.02)"
   "lat_mmap-1m (us)","84.20 (min 76.00, max 92.00)"
   "lat_ops-double-add (ns)","5.03 (min 5.02, max 5.04)"
   "lat_ops-double-div (ns)","25.16 (min 25.10, max 25.24)"
   "lat_ops-double-mul (ns)","7.05 (min 7.02, max 7.11)"
   "lat_ops-float-add (ns)","5.03 (min 5.02, max 5.05)"
   "lat_ops-float-div (ns)","15.12 (min 15.06, max 15.18)"
   "lat_ops-float-mul (ns)","6.03 (min 6.00, max 6.05)"
   "lat_ops-int-add (ns)","1.03 (min 1.03, max 1.04)"
   "lat_ops-int-bit (ns)","0.76"
   "lat_ops-int-div (ns)","96.21 (min 95.97, max 96.63)"
   "lat_ops-int-mod (ns)","24.48 (min 24.45, max 24.53)"
   "lat_ops-int-mul (ns)","4.15 (min 4.15, max 4.17)"
   "lat_ops-int64-add (ns)","1.12 (min 1.12, max 1.13)"
   "lat_ops-int64-bit (ns)","0.67 (min 0.67, max 0.68)"
   "lat_ops-int64-div (ns)","200.54 (min 200.07, max 200.96)"
   "lat_ops-int64-mod (ns)","42.54 (min 42.43, max 42.63)"
   "lat_ops-int64-mul (ns)","4.15 (min 4.14, max 4.16)"
   "lat_pagefault (us)","1.69 (min 1.67, max 1.72)"
   "lat_pipe (us)","31.82 (min 31.66, max 32.03)"
   "lat_proc-exec (us)","1432.25 (min 1348.00, max 1499.75)"
   "lat_proc-fork (us)","1266.08 (min 1218.20, max 1308.60)"
   "lat_proc-proccall (us)","0.01"
   "lat_select (us)","38.32 (min 38.25, max 38.40)"
   "lat_sem (us)","9.92 (min 9.75, max 10.08)"
   "lat_sig-catch (us)","6.51 (min 6.43, max 6.54)"
   "lat_sig-install (us)","0.93 (min 0.92, max 0.95)"
   "lat_sig-prot (us)","0.35 (min 0.25, max 0.48)"
   "lat_syscall-fstat (us)","2.17 (min 2.13, max 2.19)"
   "lat_syscall-null (us)","0.40 (min 0.39, max 0.41)"
   "lat_syscall-open (us)","464.44 (min 403.00, max 586.00)"
   "lat_syscall-read (us)","0.73 (min 0.72, max 0.73)"
   "lat_syscall-stat (us)","5.14 (min 4.96, max 5.28)"
   "lat_syscall-write (us)","0.61 (min 0.60, max 0.62)"
   "lat_tcp (us)","0.88 (min 0.87, max 0.88)"
   "lat_unix (us)","41.33 (min 40.89, max 42.10)"
   "latency_for_0.50_mb_block_size (nanosec)","91.64 (min 88.08, max 93.55)"
   "latency_for_1.00_mb_block_size (nanosec)","49.54 (min 0.00, max 99.85)"
   "pipe_bandwidth (mb\s)","341.01 (min 296.40, max 356.89)"
   "pipe_latency (microsec)","31.82 (min 31.66, max 32.03)"
   "procedure_call (microsec)","0.01"
   "select_on_200_tcp_fds (microsec)","38.32 (min 38.25, max 38.40)"
   "semaphore_latency (microsec)","9.92 (min 9.75, max 10.08)"
   "signal_handler_latency (microsec)","0.93 (min 0.92, max 0.95)"
   "signal_handler_overhead (microsec)","6.51 (min 6.43, max 6.54)"
   "tcp_ip_connection_cost_to_localhost (microsec)","80.12 (min 78.59, max 81.01)"
   "tcp_latency_using_localhost (microsec)","0.88 (min 0.87, max 0.88)"

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
   :header: "Benchmarks","am43xx-gpevm: perf"

   "cpu_clock (mhz)","1000.00"
   "dhrystone_per_mhz (dmips/mhz)","2.24 (min 2.20, max 2.30)"
   "dhrystone_per_second (dhrystonep)","3952941.28 (min 3921568.80, max 4000000.00)"

Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

   runWhetstone

.. csv-table:: Whetstone Benchmarks
   :header: "Benchmarks","am43xx-gpevm: perf"

   "whetstone (mips)","3333.30"

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
   :header: "Benchmarks","am43xx-gpevm: perf"

   "linpack (kflops)","190177.00 (min 189881.00, max 190688.00)"

NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
   :header: "Benchmarks","am43xx-gpevm: perf"

   "assignment (iterations)","8.11 (min 8.08, max 8.16)"
   "fourier (iterations)","13079.40 (min 13073.00, max 13086.00)"
   "fp_emulation (iterations)","104.37 (min 104.19, max 104.52)"
   "huffman (iterations)","836.44 (min 835.95, max 837.19)"
   "idea (iterations)","1862.18 (min 1861.80, max 1862.60)"
   "lu_decomposition (iterations)","336.98 (min 335.31, max 338.35)"
   "neural_net (iterations)","9.34 (min 9.33, max 9.34)"
   "numeric_sort (iterations)","428.13 (min 420.75, max 435.24)"
   "string_sort (iterations)","65.07 (min 64.98, max 65.10)"

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
   :header: "Benchmarks","am43xx-gpevm: perf"

   "add (mb/s)","324.98 (min 324.00, max 325.90)"
   "copy (mb/s)","433.06 (min 432.40, max 434.00)"
   "scale (mb/s)","649.78 (min 649.00, max 651.60)"
   "triad (mb/s)","378.94 (min 378.60, max 379.50)"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
   :header: "Boot Configuration","am43xx-gpevm: Boot time in seconds: avg(min,max)"

   "Linux boot time from SD with default rootfs (20 boot cycles)","50.96 (min 41.96, max 67.61)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

Graphics SGX/RGX Driver
-------------------------

Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
   :header: "Benchmark","am43xx-gpevm: Score"

   "Glmark2-DRM","83.00"
   "Glmark2-Wayland","62.00"

|

NAND Driver
-------------------------

.. rubric:: AM43XX-GPEVM
   :name: am43xx-gpevm-nand-driver

.. csv-table:: NAND Performance
   :header: "Buffer size (bytes)","am43xx-gpevm: Write UBIFS Throughput (Mbytes/sec)","am43xx-gpevm: Write UBIFS CPU Load (%)","am43xx-gpevm: Read UBIFS Throughput (Mbytes/sec)","am43xx-gpevm: Read UBIFS CPU Load (%)"

   "102400","4.39 (min 4.28, max 4.66)","84.59 (min 83.73, max 85.20)","9.78 (min 9.75, max 9.80)","45.00 (min 43.98, max 46.67)"
   "262144","4.32 (min 4.23, max 4.39)","84.92 (min 84.54, max 85.42)","9.76 (min 9.74, max 9.80)","46.03 (min 45.08, max 47.19)"
   "524288","4.33 (min 4.26, max 4.38)","84.77 (min 84.07, max 85.20)","9.75 (min 9.73, max 9.78)","46.07 (min 44.55, max 47.09)"
   "1048576","4.31 (min 4.25, max 4.37)","84.87 (min 84.27, max 85.58)","9.79 (min 9.77, max 9.80)","44.28 (min 43.13, max 46.28)"
   "5242880","4.33 (min 4.26, max 4.39)","84.84 (min 84.44, max 85.52)","9.77 (min 9.73, max 9.81)","44.97 (min 42.98, max 47.50)"

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
   :header: "Buffer size (bytes)","am43xx-gpevm: Write EXT4 Throughput (Mbytes/sec)","am43xx-gpevm: Write EXT4 CPU Load (%)","am43xx-gpevm: Read EXT4 Throughput (Mbytes/sec)","am43xx-gpevm: Read EXT4 CPU Load (%)"

   "1m","19.94 (min 19.90, max 20.00)","7.46 (min 6.73, max 8.24)","21.66 (min 21.60, max 21.70)","8.81 (min 8.58, max 9.02)"
   "4m","19.92 (min 19.90, max 20.00)","6.47 (min 6.07, max 6.61)","21.66 (min 21.60, max 21.70)","8.28 (min 7.99, max 8.96)"
   "4k","2.53","19.67 (min 18.85, max 20.81)","8.43 (min 8.40, max 8.46)","35.89 (min 33.69, max 38.46)"
   "256k","19.12 (min 19.00, max 19.30)","9.85 (min 9.59, max 10.32)","21.32 (min 21.30, max 21.40)","9.98 (min 9.78, max 10.33)"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","am43xx-gpevm: Write Raw Throughput (Mbytes/sec)","am43xx-gpevm: Write Raw CPU Load (%)","am43xx-gpevm: Read Raw Throughput (Mbytes/sec)","am43xx-gpevm: Read Raw CPU Load (%)"

   "102400","19.14 (min 18.28, max 19.49)","13.97 (min 12.01, max 20.55)","20.21 (min 19.95, max 20.49)","11.98 (min 10.00, max 14.82)"
   "262144","18.66 (min 17.79, max 19.56)","14.06 (min 11.87, max 18.30)","20.47 (min 20.22, max 21.04)","15.89 (min 14.88, max 16.73)"
   "524288","18.62 (min 17.83, max 19.31)","13.80 (min 11.66, max 18.71)","21.34 (min 20.77, max 21.77)","15.92 (min 14.72, max 18.95)"
   "1048576","18.69 (min 17.96, max 19.38)","13.81 (min 11.82, max 18.81)","22.75 (min 22.62, max 22.81)","16.25 (min 15.93, max 16.74)"
   "5242880","18.99 (min 18.32, max 19.79)","13.58 (min 11.41, max 18.03)","22.77 (min 22.73, max 22.80)","16.96 (min 16.74, max 17.25)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","am43xx-gpevm: Write Throughput (Kbytes/sec)","am43xx-gpevm: Read Throughput (Kbytes/sec)"

   "400000","14236.33 (min 11314.92, max 16062.75)","19022.86 (min 18875.58, max 19230.05)"
   "800000","14039.31 (min 11457.34, max 16650.41)","19359.07 (min 19275.29, max 19458.43)"
   "1000000","14257.06 (min 11855.28, max 16804.10)","19508.72 (min 19458.43, max 19574.67)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

USB Driver
-------------------------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
   :header: "Number of Blocks","am43xx-gpevm: Throughput (MB/sec)"

   "150","28.80 (min 27.90, max 29.70)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
   :header: "Number of Blocks","am43xx-gpevm: Throughput (MB/sec)"

   "150","26.80 (min 26.40, max 27.20)"

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
   :header: "Algorithm","Buffer Size (in bytes)","am43xx-gpevm: throughput (KBytes/Sec)"

   "aes-128-cbc","1024","34505.86 (min 34406.74, max 34727.25)"
   "aes-128-cbc","16","26333.93 (min 26323.71, max 26344.71)"
   "aes-128-cbc","16384","34652.16 (min 34564.78, max 34892.46)"
   "aes-128-cbc","256","34062.95 (min 33977.00, max 34158.08)"
   "aes-128-cbc","64","31898.01 (min 30934.44, max 32178.69)"
   "aes-128-cbc","8192","34648.88 (min 34564.78, max 34794.15)"
   "aes-128-ecb","1024","37456.83 (min 37369.51, max 37588.65)"
   "aes-128-ecb","16","29551.18 (min 29508.43, max 29687.25)"
   "aes-128-ecb","16384","37534.65 (min 37355.52, max 37612.20)"
   "aes-128-ecb","256","36774.64 (min 36414.81, max 36914.60)"
   "aes-128-ecb","64","34660.42 (min 34155.46, max 34817.58)"
   "aes-128-ecb","8192","37622.03 (min 37582.17, max 37653.16)"
   "aes-192-cbc","1024","31420.35 (min 31396.52, max 31433.73)"
   "aes-192-cbc","16","23529.75 (min 23417.57, max 23612.85)"
   "aes-192-cbc","16384","31530.46 (min 31468.20, max 31577.43)"
   "aes-192-cbc","256","30856.98 (min 30802.94, max 30898.26)"
   "aes-192-cbc","64","28874.03 (min 28857.71, max 28891.18)"
   "aes-192-cbc","8192","31537.56 (min 31416.32, max 31585.62)"
   "aes-192-ecb","1024","30785.13 (min 30664.70, max 30868.48)"
   "aes-192-ecb","16","26480.62 (min 26399.84, max 26670.78)"
   "aes-192-ecb","16384","30837.96 (min 30730.92, max 30889.30)"
   "aes-192-ecb","256","30250.75 (min 29250.99, max 30554.11)"
   "aes-192-ecb","64","29421.89 (min 29356.14, max 29465.47)"
   "aes-192-ecb","8192","30863.63 (min 30788.27, max 30954.84)"
   "aes-256-cbc","1024","27443.06 (min 27415.89, max 27479.04)"
   "aes-256-cbc","16","21231.74 (min 21133.02, max 21294.58)"
   "aes-256-cbc","16384","27541.50 (min 27514.20, max 27568.81)"
   "aes-256-cbc","256","26976.41 (min 26946.82, max 27037.70)"
   "aes-256-cbc","64","25265.56 (min 25204.74, max 25325.40)"
   "aes-256-cbc","8192","27539.87 (min 27465.05, max 27571.54)"
   "aes-256-ecb","1024","26866.01 (min 26708.65, max 26954.41)"
   "aes-256-ecb","16","23472.67 (min 23380.09, max 23621.89)"
   "aes-256-ecb","16384","26678.61 (min 25843.03, max 27011.75)"
   "aes-256-ecb","256","26622.57 (min 26564.35, max 26685.53)"
   "aes-256-ecb","64","25720.31 (min 25660.93, max 25781.67)"
   "aes-256-ecb","8192","26927.10 (min 26921.64, max 26929.83)"
   "des3","1024","3508.29 (min 3503.10, max 3513.69)"
   "des3","16","3337.37 (min 3326.59, max 3346.34)"
   "des3","16384","3470.13 (min 3364.18, max 3506.18)"
   "des3","256","3496.60 (min 3491.84, max 3504.73)"
   "des3","64","3459.82 (min 3454.19, max 3469.46)"
   "des3","8192","3476.14 (min 3361.45, max 3511.64)"
   "md5","1024","106935.91 (min 106472.45, max 107164.67)"
   "md5","16","7497.29 (min 7260.15, max 7568.81)"
   "md5","16384","135707.58 (min 135162.54, max 136276.65)"
   "md5","256","63798.68 (min 63623.94, max 63892.31)"
   "md5","64","24487.06 (min 24471.87, max 24510.81)"
   "md5","8192","133518.68 (min 132915.20, max 133936.47)"
   "sha1","1024","96055.36 (min 95783.25, max 96261.80)"
   "sha1","16","7446.45 (min 7442.52, max 7449.89)"
   "sha1","16384","119047.24 (min 118904.15, max 119379.29)"
   "sha1","256","59529.90 (min 59369.64, max 59609.94)"
   "sha1","64","23543.21 (min 23495.15, max 23573.55)"
   "sha1","8192","117141.78 (min 116771.50, max 117410.47)"
   "sha224","1024","52889.46 (min 51005.44, max 53563.05)"
   "sha224","16","5821.87 (min 5810.07, max 5834.09)"
   "sha224","16384","61624.59 (min 61259.78, max 62084.44)"
   "sha224","256","36937.88 (min 36014.51, max 37350.57)"
   "sha224","64","16773.27 (min 16722.20, max 16806.81)"
   "sha224","8192","60973.06 (min 60071.94, max 61483.69)"
   "sha256","1024","52599.53 (min 51373.40, max 53322.07)"
   "sha256","16","5677.37 (min 5671.95, max 5684.00)"
   "sha256","16384","61576.53 (min 61205.16, max 61942.44)"
   "sha256","256","36804.35 (min 36558.76, max 36922.28)"
   "sha256","64","16400.87 (min 15912.02, max 16557.08)"
   "sha256","8192","60388.15 (min 58810.37, max 61169.66)"
   "sha512","1024","33702.64 (min 33636.69, max 33766.74)"
   "sha512","16","3282.83 (min 3236.74, max 3297.05)"
   "sha512","16384","39661.29 (min 39578.28, max 39714.82)"
   "sha512","256","22739.06 (min 22712.66, max 22767.87)"
   "sha512","64","12987.01 (min 12977.94, max 12992.47)"
   "sha512","8192","39234.22 (min 39144.11, max 39316.14)"

.. csv-table:: OpenSSL CPU Load
   :header: "Algorithm","am43xx-gpevm: CPU Load"

   "aes-128-cbc","99.00"
   "aes-128-ecb","99.00"
   "aes-192-cbc","99.00"
   "aes-192-ecb","99.00"
   "aes-256-cbc","99.00"
   "aes-256-ecb","99.00"
   "des3","99.00"
   "md5","98.80 (min 98.00, max 99.00)"
   "sha1","99.00"
   "sha224","98.80 (min 98.00, max 99.00)"
   "sha256","98.60 (min 98.00, max 99.00)"
   "sha386","78.00 (min 49.00, max 88.00)"
   "sha512","99.00"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

   time -v openssl speed -elapsed -evp aes-128-cbc
