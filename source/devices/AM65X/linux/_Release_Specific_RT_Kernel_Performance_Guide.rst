
=================================
 RT-linux 11.02 Performance Guide
=================================

.. rubric::  **Read This First**
   :name: read-this-first-rt-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+---------------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                         |
+================+=====================================================================================================================+
| AM65x EVM      | AM65x Evaluation Module rev 1.0 with ARM running at 800MHz, DDR4-2400 (1600 MT/S), TMDX654GPEVM                     |
+----------------+---------------------------------------------------------------------------------------------------------------------+

Table:  Evaluation Modules

.. rubric::  About This Manual
   :name: about-this-manual-rt-kernel-perf-guide

This document provides performance data for each of the device drivers
which are part of the Processor SDK Linux package. This document should be
used in conjunction with release notes and user guides provided with the
Processor SDK Linux package for information on specific issues present
with drivers included in a particular release.

.. rubric::  If You Need Assistance
   :name: if-you-need-assistance-rt-kernel-perf-guide

For further information or to report any problems, contact
https://e2e.ti.com/ or https://support.ti.com/

|

System Benchmarks
-------------------------

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
   :header: "Benchmarks","am654x-evm: perf"

   "af_unix_sock_stream_latency (microsec)","101.55 (min 90.19, max 116.04)"
   "af_unix_socket_stream_bandwidth (mb\s)","921.34 (min 899.58, max 966.53)"
   "bw_file_rd-io-1mb (mb/s)","1100.23 (min 1085.78, max 1115.03)"
   "bw_file_rd-o2c-1mb (mb/s)","618.02 (min 581.99, max 640.51)"
   "bw_mem-bcopy-16mb (mb/s)","889.57 (min 881.83, max 893.46)"
   "bw_mem-bcopy-1mb (mb/s)","1243.78 (min 1226.24, max 1258.54)"
   "bw_mem-bcopy-2mb (mb/s)","954.30 (min 937.79, max 968.84)"
   "bw_mem-bcopy-4mb (mb/s)","894.27 (min 888.40, max 898.78)"
   "bw_mem-bcopy-8mb (mb/s)","883.79 (min 875.27, max 889.09)"
   "bw_mem-bzero-16mb (mb/s)","2005.42 (min 2001.50, max 2008.79)"
   "bw_mem-bzero-1mb (mb/s)","2850.93 (min 1226.24, max 4481.89)"
   "bw_mem-bzero-2mb (mb/s)","2206.38 (min 937.79, max 3537.74)"
   "bw_mem-bzero-4mb (mb/s)","1591.13 (min 888.40, max 2294.46)"
   "bw_mem-bzero-8mb (mb/s)","1458.45 (min 875.27, max 2037.96)"
   "bw_mem-cp-16mb (mb/s)","585.43 (min 576.27, max 592.42)"
   "bw_mem-cp-1mb (mb/s)","2785.23 (min 753.30, max 4927.91)"
   "bw_mem-cp-2mb (mb/s)","2029.25 (min 615.20, max 3481.62)"
   "bw_mem-cp-4mb (mb/s)","1440.54 (min 574.14, max 2300.17)"
   "bw_mem-cp-8mb (mb/s)","1305.77 (min 575.71, max 2036.14)"
   "bw_mem-fcp-16mb (mb/s)","886.51 (min 875.90, max 893.80)"
   "bw_mem-fcp-1mb (mb/s)","2806.75 (min 1134.43, max 4481.89)"
   "bw_mem-fcp-2mb (mb/s)","2205.24 (min 935.31, max 3537.74)"
   "bw_mem-fcp-4mb (mb/s)","1590.17 (min 886.43, max 2294.46)"
   "bw_mem-fcp-8mb (mb/s)","1459.06 (min 881.06, max 2037.96)"
   "bw_mem-frd-16mb (mb/s)","1141.57 (min 1108.03, max 1168.57)"
   "bw_mem-frd-1mb (mb/s)","1529.78 (min 1134.43, max 1946.28)"
   "bw_mem-frd-2mb (mb/s)","1222.79 (min 935.31, max 1523.81)"
   "bw_mem-frd-4mb (mb/s)","1072.54 (min 886.43, max 1269.64)"
   "bw_mem-frd-8mb (mb/s)","1037.88 (min 881.06, max 1210.10)"
   "bw_mem-fwr-16mb (mb/s)","2001.83 (min 1987.33, max 2007.53)"
   "bw_mem-fwr-1mb (mb/s)","3356.49 (min 1875.82, max 4927.91)"
   "bw_mem-fwr-2mb (mb/s)","2466.01 (min 1461.19, max 3481.62)"
   "bw_mem-fwr-4mb (mb/s)","1774.37 (min 1240.31, max 2300.17)"
   "bw_mem-fwr-8mb (mb/s)","1612.12 (min 1154.73, max 2036.14)"
   "bw_mem-rd-16mb (mb/s)","1205.75 (min 1203.37, max 1209.83)"
   "bw_mem-rd-1mb (mb/s)","3264.82 (min 2912.06, max 3591.31)"
   "bw_mem-rd-2mb (mb/s)","1414.81 (min 1273.89, max 1534.33)"
   "bw_mem-rd-4mb (mb/s)","1114.69 (min 950.80, max 1271.05)"
   "bw_mem-rd-8mb (mb/s)","1053.52 (min 889.09, max 1219.51)"
   "bw_mem-rdwr-16mb (mb/s)","837.89 (min 828.03, max 849.75)"
   "bw_mem-rdwr-1mb (mb/s)","1795.42 (min 753.30, max 3013.18)"
   "bw_mem-rdwr-2mb (mb/s)","931.44 (min 615.20, max 1266.02)"
   "bw_mem-rdwr-4mb (mb/s)","751.66 (min 574.14, max 929.80)"
   "bw_mem-rdwr-8mb (mb/s)","716.18 (min 575.71, max 859.38)"
   "bw_mem-wr-16mb (mb/s)","888.32 (min 887.56, max 889.23)"
   "bw_mem-wr-1mb (mb/s)","3114.82 (min 2689.62, max 3591.31)"
   "bw_mem-wr-2mb (mb/s)","1273.62 (min 1219.33, max 1331.56)"
   "bw_mem-wr-4mb (mb/s)","941.16 (min 912.30, max 973.95)"
   "bw_mem-wr-8mb (mb/s)","874.69 (min 846.92, max 899.48)"
   "bw_mmap_rd-mo-1mb (mb/s)","2713.24 (min 2581.60, max 2828.59)"
   "bw_mmap_rd-o2c-1mb (mb/s)","659.73 (min 617.76, max 689.18)"
   "bw_pipe (mb/s)","547.03 (min 464.85, max 582.13)"
   "bw_unix (mb/s)","921.34 (min 899.58, max 966.53)"
   "lat_connect (us)","88.16 (min 87.63, max 88.68)"
   "lat_ctx-2-128k (us)","14.61 (min 9.31, max 18.62)"
   "lat_ctx-2-256k (us)","12.70 (min 6.93, max 17.64)"
   "lat_ctx-4-128k (us)","15.17 (min 12.88, max 17.59)"
   "lat_ctx-4-256k (us)","9.70 (min 4.94, max 14.11)"
   "lat_fs-0k (num_files)","169.20 (min 162.00, max 175.00)"
   "lat_fs-10k (num_files)","88.40 (min 81.00, max 98.00)"
   "lat_fs-1k (num_files)","115.40 (min 109.00, max 123.00)"
   "lat_fs-4k (num_files)","119.80 (min 116.00, max 130.00)"
   "lat_mem_rd-stride128-sz1000k (ns)","23.86 (min 22.80, max 24.66)"
   "lat_mem_rd-stride128-sz125k (ns)","9.81 (min 9.76, max 9.88)"
   "lat_mem_rd-stride128-sz250k (ns)","10.29 (min 10.28, max 10.30)"
   "lat_mem_rd-stride128-sz31k (ns)","5.39 (min 3.84, max 6.43)"
   "lat_mem_rd-stride128-sz50 (ns)","3.78"
   "lat_mem_rd-stride128-sz500k (ns)","11.87 (min 11.53, max 12.18)"
   "lat_mem_rd-stride128-sz62k (ns)","9.00 (min 8.04, max 9.28)"
   "lat_mmap-1m (us)","88.80 (min 81.00, max 93.00)"
   "lat_ops-double-add (ns)","5.06 (min 5.04, max 5.09)"
   "lat_ops-double-div (ns)","27.81 (min 27.71, max 27.88)"
   "lat_ops-double-mul (ns)","5.05 (min 5.04, max 5.07)"
   "lat_ops-float-add (ns)","5.05 (min 5.04, max 5.06)"
   "lat_ops-float-div (ns)","16.40 (min 16.37, max 16.46)"
   "lat_ops-float-mul (ns)","5.06 (min 5.04, max 5.08)"
   "lat_ops-int-add (ns)","1.27 (min 1.26, max 1.27)"
   "lat_ops-int-bit (ns)","0.84"
   "lat_ops-int-div (ns)","7.57 (min 7.55, max 7.59)"
   "lat_ops-int-mod (ns)","7.99 (min 7.97, max 8.03)"
   "lat_ops-int-mul (ns)","5.45 (min 5.43, max 5.51)"
   "lat_ops-int64-add (ns)","1.27 (min 1.26, max 1.27)"
   "lat_ops-int64-bit (ns)","0.84"
   "lat_ops-int64-div (ns)","12.01 (min 11.97, max 12.04)"
   "lat_ops-int64-mod (ns)","9.25 (min 9.23, max 9.29)"
   "lat_ops-int64-mul (ns)","6.28 (min 6.26, max 6.32)"
   "lat_pagefault (us)","1.50 (min 1.48, max 1.52)"
   "lat_pipe (us)","45.10 (min 43.38, max 46.25)"
   "lat_proc-exec (us)","932.70 (min 925.17, max 952.67)"
   "lat_proc-fork (us)","839.70 (min 820.57, max 855.83)"
   "lat_proc-proccall (us)","0.02"
   "lat_select (us)","58.53 (min 57.76, max 58.97)"
   "lat_sem (us)","6.31 (min 5.29, max 7.50)"
   "lat_sig-catch (us)","7.30 (min 7.12, max 7.48)"
   "lat_sig-install (us)","1.15 (min 1.14, max 1.16)"
   "lat_sig-prot (us)","0.92 (min 0.83, max 1.00)"
   "lat_syscall-fstat (us)","3.20 (min 3.12, max 3.37)"
   "lat_syscall-null (us)","0.75 (min 0.74, max 0.75)"
   "lat_syscall-open (us)","275.28 (min 250.22, max 322.44)"
   "lat_syscall-read (us)","1.02"
   "lat_syscall-stat (us)","8.84 (min 8.67, max 9.09)"
   "lat_syscall-write (us)","0.95 (min 0.95, max 0.96)"
   "lat_tcp (us)","1.38 (min 1.37, max 1.39)"
   "lat_unix (us)","101.55 (min 90.19, max 116.04)"
   "latency_for_0.50_mb_block_size (nanosec)","11.87 (min 11.53, max 12.18)"
   "latency_for_1.00_mb_block_size (nanosec)","11.93 (min 0.00, max 24.66)"
   "pipe_bandwidth (mb\s)","547.03 (min 464.85, max 582.13)"
   "pipe_latency (microsec)","45.10 (min 43.38, max 46.25)"
   "procedure_call (microsec)","0.02"
   "select_on_200_tcp_fds (microsec)","58.53 (min 57.76, max 58.97)"
   "semaphore_latency (microsec)","6.31 (min 5.29, max 7.50)"
   "signal_handler_latency (microsec)","1.15 (min 1.14, max 1.16)"
   "signal_handler_overhead (microsec)","7.30 (min 7.12, max 7.48)"
   "tcp_ip_connection_cost_to_localhost (microsec)","88.16 (min 87.63, max 88.68)"
   "tcp_latency_using_localhost (microsec)","1.38 (min 1.37, max 1.39)"

Dhrystone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed. For standard ARM
cores the DMIPS/MHz score will be identical with the same compiler and flags.

.. csv-table:: Dhrystone Benchmarks
   :header: "Benchmarks","am654x-evm: perf"

   "cpu_clock (mhz)","800.00"
   "dhrystone_per_mhz (dmips/mhz)","2.88 (min 2.80, max 2.90)"
   "dhrystone_per_second (dhrystonep)","4065306.24 (min 4000000.00, max 4081632.80)"

Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Whetstone Benchmarks
   :header: "Benchmarks","am654x-evm: perf"

   "whetstone (mips)","3333.30"

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
   :header: "Benchmarks","am654x-evm: perf"

   "linpack (kflops)","325321.80 (min 323487.00, max 327046.00)"

NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks 
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
   :header: "Benchmarks","am654x-evm: perf"

   "assignment (iterations)","8.19 (min 8.15, max 8.21)"
   "fourier (iterations)","12950.40 (min 12949.00, max 12951.00)"
   "fp_emulation (iterations)","122.24 (min 122.23, max 122.25)"
   "huffman (iterations)","671.51 (min 671.41, max 671.57)"
   "idea (iterations)","1954.82 (min 1954.50, max 1955.10)"
   "lu_decomposition (iterations)","299.24 (min 298.06, max 300.60)"
   "neural_net (iterations)","4.91 (min 4.91, max 4.92)"
   "numeric_sort (iterations)","355.67 (min 355.11, max 355.89)"
   "string_sort (iterations)","92.97 (min 92.96, max 92.98)"

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

.. csv-table:: Stream Benchmarks
   :header: "Benchmarks","am43xx-gpevm: perf"

   "add (mb/s)","324.98 (min 324.00, max 325.90)"
   "copy (mb/s)","433.06 (min 432.40, max 434.00)"
   "scale (mb/s)","649.78 (min 649.00, max 651.60)"
   "triad (mb/s)","378.94 (min 378.60, max 379.50)"

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
   :header: "Benchmarks","am654x-evm: perf"

   "4m-check (workloads/)","321.86 (min 320.80, max 322.58)"
   "4m-check-reassembly (workloads/)","77.20 (min 76.98, max 77.58)"
   "4m-check-reassembly-tcp (workloads/)","36.46 (min 36.34, max 36.60)"
   "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","9.84 (min 9.43, max 10.30)"
   "4m-check-reassembly-tcp-x264w2 (workloads/)","1.14"
   "4m-cmykw2 (workloads/)","137.43 (min 136.71, max 138.60)"
   "4m-cmykw2-rotatew2 (workloads/)","11.28 (min 9.53, max 12.52)"
   "4m-reassembly (workloads/)","56.12 (min 56.02, max 56.21)"
   "4m-rotatew2 (workloads/)","13.00 (min 10.34, max 15.99)"
   "4m-tcp-mixed (workloads/)","68.90 (min 66.67, max 70.18)"
   "4m-x264w2 (workloads/)","1.16 (min 1.15, max 1.17)"
   "empty-wld (workloads/)","1.00"
   "idct-4m (workloads/)","10.95 (min 10.94, max 10.96)"
   "idct-4mw1 (workloads/)","10.96 (min 10.93, max 10.97)"
   "ippktcheck-4m (workloads/)","321.15 (min 320.43, max 321.75)"
   "ippktcheck-4mw1 (workloads/)","321.56 (min 320.80, max 322.87)"
   "ipres-4m (workloads/)","67.16 (min 67.02, max 67.33)"
   "ipres-4mw1 (workloads/)","66.97 (min 66.58, max 67.33)"
   "md5-4m (workloads/)","16.66 (min 16.63, max 16.70)"
   "md5-4mw1 (workloads/)","16.70 (min 16.61, max 16.76)"
   "rgbcmyk-4m (workloads/)","36.19 (min 36.18, max 36.21)"
   "rgbcmyk-4mw1 (workloads/)","36.20 (min 36.17, max 36.21)"
   "rotate-4ms1 (workloads/)","14.15 (min 14.14, max 14.16)"
   "rotate-4ms1w1 (workloads/)","14.15 (min 14.14, max 14.16)"
   "rotate-4ms64 (workloads/)","14.29 (min 14.29, max 14.30)"
   "rotate-4ms64w1 (workloads/)","14.30 (min 14.29, max 14.30)"
   "x264-4mq (workloads/)","0.33"
   "x264-4mqw1 (workloads/)","0.33"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
   :header: "Boot Configuration","am654x-evm: Boot time in seconds: avg(min,max)"

   "Linux boot time from SD with default rootfs (20 boot cycles)","17.15 (min 16.76, max 17.93)"

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

PCIe Driver
-------------------------

PCIe-ETH
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: PCIe Ethernet performance
   :header: "TCP Window Size(Kbytes)","am654x-evm: Bandwidth (Mbits/sec)"

   "128","0.00"
   "256","0.00"

|

NAND Driver
-------------------------

.. rubric:: AM43XX-GPEVM
   :name: am43xx-gpevm-nand

.. csv-table:: NAND Performance
   :header: "Buffer size (bytes)","am43xx-gpevm: Write UBIFS Throughput (Mbytes/sec)","am43xx-gpevm: Write UBIFS CPU Load (%)","am43xx-gpevm: Read UBIFS Throughput (Mbytes/sec)","am43xx-gpevm: Read UBIFS CPU Load (%)"

   "102400","4.39 (min 4.28, max 4.66)","84.59 (min 83.73, max 85.20)","9.78 (min 9.75, max 9.80)","45.00 (min 43.98, max 46.67)"
   "262144","4.32 (min 4.23, max 4.39)","84.92 (min 84.54, max 85.42)","9.76 (min 9.74, max 9.80)","46.03 (min 45.08, max 47.19)"
   "524288","4.33 (min 4.26, max 4.38)","84.77 (min 84.07, max 85.20)","9.75 (min 9.73, max 9.78)","46.07 (min 44.55, max 47.09)"
   "1048576","4.31 (min 4.25, max 4.37)","84.87 (min 84.27, max 85.58)","9.79 (min 9.77, max 9.80)","44.28 (min 43.13, max 46.28)"
   "5242880","4.33 (min 4.26, max 4.39)","84.84 (min 84.44, max 85.52)","9.77 (min 9.73, max 9.81)","44.97 (min 42.98, max 47.50)"

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
   :header: "Buffer size (bytes)","am654x-evm: Write EXT4 Throughput (Mbytes/sec)","am654x-evm: Write EXT4 CPU Load (%)","am654x-evm: Read EXT4 Throughput (Mbytes/sec)","am654x-evm: Read EXT4 CPU Load (%)"

   "1m","55.50 (min 45.00, max 60.80)","1.39 (min 1.11, max 1.59)","174.67 (min 174.00, max 175.00)","2.47 (min 2.17, max 2.91)"
   "4m","55.60 (min 45.30, max 60.90)","1.13 (min 0.92, max 1.25)","174.67 (min 174.00, max 175.00)","2.01 (min 1.87, max 2.18)"
   "4k","33.60 (min 5.30, max 48.30)","20.04 (min 3.54, max 28.61)","49.40 (min 36.40, max 56.00)","26.39 (min 20.60, max 29.31)"
   "256k","52.50 (min 35.80, max 61.00)","1.56 (min 1.12, max 1.84)","174.00","3.46 (min 3.22, max 3.64)"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","am654x-evm: Write Throughput (Kbytes/sec)","am654x-evm: Read Throughput (Kbytes/sec)"

   "2000000","61393.80 (min 61020.48, max 61826.42)","174067.32 (min 173375.66, max 174297.87)"
   "4000000","61827.27 (min 61478.42, max 62119.43)","177845.65 (min 177604.34, max 178086.96)"

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
   :header: "Buffer size (bytes)","am654x-evm: Write EXT4 Throughput (Mbytes/sec)","am654x-evm: Write EXT4 CPU Load (%)","am654x-evm: Read EXT4 Throughput (Mbytes/sec)","am654x-evm: Read EXT4 CPU Load (%)"

   "1m","15.32 (min 15.00, max 15.60)","0.65 (min 0.62, max 0.68)","24.42 (min 24.30, max 24.60)","0.66 (min 0.62, max 0.70)"
   "4m","15.02 (min 14.90, max 15.20)","0.57 (min 0.55, max 0.58)","23.80 (min 23.50, max 24.40)","0.60 (min 0.59, max 0.61)"
   "4k","3.87 (min 3.73, max 3.92)","3.88 (min 3.73, max 4.03)","9.42 (min 9.38, max 9.50)","5.50 (min 5.30, max 5.62)"
   "256k","15.24 (min 14.70, max 15.60)","0.68 (min 0.64, max 0.70)","24.14 (min 24.00, max 24.30)","0.75 (min 0.71, max 0.80)"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","am654x-evm: Write Raw Throughput (Mbytes/sec)","am654x-evm: Write Raw CPU Load (%)","am654x-evm: Read Raw Throughput (Mbytes/sec)","am654x-evm: Read Raw CPU Load (%)"

   "102400","14.74 (min 14.01, max 15.44)","1.86 (min 1.56, max 2.63)","21.06 (min 20.64, max 21.53)","1.49 (min 1.39, max 1.62)"
   "262144","15.34 (min 14.71, max 15.90)","1.93 (min 1.43, max 2.47)","23.49 (min 23.37, max 23.55)","1.52 (min 1.51, max 1.52)"
   "524288","15.43 (min 14.78, max 16.09)","1.71 (min 1.41, max 2.39)","23.80 (min 23.75, max 23.83)","1.61 (min 1.48, max 1.76)"
   "1048576","15.44 (min 14.74, max 15.99)","1.74 (min 1.48, max 2.36)","23.80 (min 23.75, max 23.85)","1.60 (min 1.53, max 1.71)"
   "5242880","15.41 (min 14.76, max 16.21)","1.71 (min 1.44, max 2.52)","23.80 (min 23.77, max 23.85)","1.71 (min 1.65, max 1.77)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 
UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","am654x-evm: Write Throughput (Kbytes/sec)","am654x-evm: Read Throughput (Kbytes/sec)"

   "400000","17601.94 (min 15937.74, max 18703.20)","22738.19 (min 22505.49, max 22882.68)"
   "800000","19452.04 (min 14733.81, max 20951.41)","23197.75 (min 23011.24, max 23272.73)"
   "1000000","19428.52 (min 16499.50, max 21222.80)","23381.92 (min 23305.83, max 23405.71)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
   :header: "Algorithm","Buffer Size (in bytes)","am654x-evm: throughput (KBytes/Sec)"

   "aes-128-cbc","1024","13790.00 (min 12601.00, max 14640.13)"
   "aes-128-cbc","16","225.28 (min 212.71, max 237.80)"
   "aes-128-cbc","16384","110756.93 (min 108653.23, max 113186.13)"
   "aes-128-cbc","256","3552.02 (min 3438.51, max 3764.57)"
   "aes-128-cbc","64","908.54 (min 879.13, max 940.93)"
   "aes-128-cbc","8192","74448.90 (min 70959.10, max 77124.95)"
   "aes-128-ecb","1024","14162.74 (min 13721.60, max 14453.42)"
   "aes-128-ecb","16","224.70 (min 216.01, max 232.66)"
   "aes-128-ecb","16384","113643.79 (min 110029.48, max 116594.01)"
   "aes-128-ecb","256","3715.28 (min 3595.95, max 3830.95)"
   "aes-128-ecb","64","898.51 (min 862.70, max 949.76)"
   "aes-128-ecb","8192","78102.53 (min 75942.57, max 80827.73)"
   "aes-192-cbc","1024","13960.94 (min 13073.07, max 14519.98)"
   "aes-192-cbc","16","227.73 (min 209.87, max 236.91)"
   "aes-192-cbc","16384","106742.85 (min 104939.52, max 108363.78)"
   "aes-192-cbc","256","3575.19 (min 3467.78, max 3641.94)"
   "aes-192-cbc","64","926.70 (min 899.73, max 952.11)"
   "aes-192-cbc","8192","71924.67 (min 67264.51, max 75939.84)"
   "aes-192-ecb","1024","14151.41 (min 13632.51, max 14506.33)"
   "aes-192-ecb","16","223.97 (min 212.51, max 236.43)"
   "aes-192-ecb","16384","110458.74 (min 107763.03, max 112044.71)"
   "aes-192-ecb","256","3607.06 (min 3510.78, max 3717.63)"
   "aes-192-ecb","64","898.06 (min 855.51, max 971.86)"
   "aes-192-ecb","8192","73383.94 (min 71707.31, max 74377.90)"
   "aes-256-cbc","1024","13225.23 (min 12530.01, max 14188.54)"
   "aes-256-cbc","16","229.51 (min 223.70, max 236.77)"
   "aes-256-cbc","16384","103131.82 (min 99740.33, max 105900.71)"
   "aes-256-cbc","256","3479.84 (min 3316.74, max 3601.66)"
   "aes-256-cbc","64","890.31 (min 857.19, max 933.55)"
   "aes-256-cbc","8192","71637.40 (min 69536.43, max 74227.71)"
   "aes-256-ecb","1024","13513.66 (min 12838.57, max 14158.51)"
   "aes-256-ecb","16","223.22 (min 217.10, max 231.71)"
   "aes-256-ecb","16384","103479.16 (min 99008.51, max 108331.01)"
   "aes-256-ecb","256","3575.81 (min 3423.15, max 3669.42)"
   "aes-256-ecb","64","915.71 (min 883.71, max 946.24)"
   "aes-256-ecb","8192","71194.49 (min 68304.90, max 73998.34)"
   "des3","1024","13361.49 (min 12914.01, max 13898.07)"
   "des3","16","229.76 (min 221.77, max 238.33)"
   "des3","16384","71768.47 (min 70800.73, max 72739.50)"
   "des3","256","3574.34 (min 3348.39, max 3745.79)"
   "des3","64","908.89 (min 870.06, max 953.26)"
   "des3","8192","55066.62 (min 54744.41, max 55784.79)"
   "sha1","1024","22420.21 (min 22218.75, max 22690.13)"
   "sha1","16","376.29 (min 372.82, max 380.45)"
   "sha1","16384","169449.88 (min 168673.28, max 170595.67)"
   "sha1","256","5886.86 (min 5835.35, max 5955.16)"
   "sha1","64","1490.79 (min 1476.91, max 1508.74)"
   "sha1","8192","116964.83 (min 116274.52, max 118054.91)"
   "sha256","1024","22263.19 (min 22034.43, max 22410.92)"
   "sha256","16","372.87 (min 369.80, max 377.10)"
   "sha256","16384","172687.36 (min 171212.80, max 173823.32)"
   "sha256","256","5832.55 (min 5772.63, max 5888.09)"
   "sha256","64","1474.52 (min 1459.99, max 1489.86)"
   "sha256","8192","117898.17 (min 116957.18, max 118407.17)"
   "sha512","1024","14960.37 (min 14798.51, max 15063.04)"
   "sha512","16","355.99 (min 350.77, max 360.12)"
   "sha512","16384","38636.75 (min 38595.24, max 38699.01)"
   "sha512","256","5034.51 (min 4966.40, max 5091.84)"
   "sha512","64","1424.48 (min 1402.71, max 1441.75)"
   "sha512","8192","34831.84 (min 34758.66, max 34887.00)"

.. csv-table:: OpenSSL CPU Load
   :header: "Algorithm","am654x-evm: CPU Load"

   "aes-128-cbc","41.20 (min 40.00, max 43.00)"
   "aes-128-ecb","42.80 (min 42.00, max 43.00)"
   "aes-192-cbc","42.80 (min 42.00, max 43.00)"
   "aes-192-ecb","42.60 (min 42.00, max 43.00)"
   "aes-256-cbc","41.80 (min 41.00, max 42.00)"
   "aes-256-ecb","42.40 (min 42.00, max 43.00)"
   "des3","39.00"
   "sha1","93.40 (min 87.00, max 95.00)"
   "sha256","95.00"
   "sha512","94.60 (min 93.00, max 95.00)"

Listed for each algorithm are the code snippets used to run each benchmark test.

::

   time -v openssl speed -elapsed -evp aes-128-cbc
