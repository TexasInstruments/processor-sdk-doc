
====================================
 Linux 11.01.16.13 Performance Guide
====================================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

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

System Benchmarks
-------------------


LMBench
^^^^^^^
LMBench is a collection of microbenchmarks of which the memory bandwidth 
and latency related ones are typically used to estimate processor 
memory system performance. More information about lmbench at
http://lmbench.sourceforge.net/whatis_lmbench.html and
http://lmbench.sourceforge.net/man/lmbench.8.html

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
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "af_unix_sock_stream_latency (microsec)","33.32 (min 32.78, max 34.30)"
    "af_unix_socket_stream_bandwidth (mb\s)","477.67 (min 424.53, max 533.19)"
    "bw_file_rd-io-1mb (mb/s)","1017.86 (min 930.23, max 1103.75)"
    "bw_file_rd-o2c-1mb (mb/s)","498.42 (min 476.87, max 515.11)"
    "bw_mem-bcopy-16mb (mb/s)","785.15 (min 707.87, max 861.19)"
    "bw_mem-bcopy-1mb (mb/s)","808.29 (min 696.74, max 916.42)"
    "bw_mem-bcopy-2mb (mb/s)","811.05 (min 686.58, max 932.84)"
    "bw_mem-bcopy-4mb (mb/s)","835.91 (min 713.78, max 944.51)"
    "bw_mem-bcopy-8mb (mb/s)","860.43 (min 743.43, max 972.05)"
    "bw_mem-bzero-16mb (mb/s)","2426.00 (min 2106.09, max 2726.19)"
    "bw_mem-bzero-1mb (mb/s)","1616.51 (min 696.74, max 2726.28)"
    "bw_mem-bzero-2mb (mb/s)","1618.34 (min 686.58, max 2725.72)"
    "bw_mem-bzero-4mb (mb/s)","1630.79 (min 713.78, max 2725.26)"
    "bw_mem-bzero-8mb (mb/s)","1643.18 (min 743.43, max 2726.19)"
    "bw_mem-cp-16mb (mb/s)","454.69 (min 396.23, max 512.71)"
    "bw_mem-cp-1mb (mb/s)","1541.45 (min 397.93, max 2954.21)"
    "bw_mem-cp-2mb (mb/s)","1490.05 (min 396.47, max 2828.85)"
    "bw_mem-cp-4mb (mb/s)","1483.53 (min 419.77, max 2781.64)"
    "bw_mem-cp-8mb (mb/s)","1481.96 (min 440.72, max 2755.77)"
    "bw_mem-fcp-16mb (mb/s)","788.37 (min 712.79, max 865.71)"
    "bw_mem-fcp-1mb (mb/s)","1646.16 (min 767.75, max 2726.28)"
    "bw_mem-fcp-2mb (mb/s)","1647.26 (min 767.46, max 2725.72)"
    "bw_mem-fcp-4mb (mb/s)","1659.77 (min 742.67, max 2725.26)"
    "bw_mem-fcp-8mb (mb/s)","1668.94 (min 800.48, max 2726.19)"
    "bw_mem-frd-16mb (mb/s)","1412.28 (min 1254.12, max 1571.86)"
    "bw_mem-frd-1mb (mb/s)","1117.35 (min 767.75, max 1527.01)"
    "bw_mem-frd-2mb (mb/s)","1119.11 (min 767.46, max 1539.94)"
    "bw_mem-frd-4mb (mb/s)","1144.37 (min 742.67, max 1557.33)"
    "bw_mem-frd-8mb (mb/s)","1161.00 (min 800.48, max 1572.02)"
    "bw_mem-fwr-16mb (mb/s)","2441.13 (min 2120.89, max 2737.85)"
    "bw_mem-fwr-1mb (mb/s)","1993.66 (min 1208.77, max 2954.21)"
    "bw_mem-fwr-2mb (mb/s)","1947.01 (min 1216.92, max 2828.85)"
    "bw_mem-fwr-4mb (mb/s)","1937.10 (min 1219.70, max 2781.64)"
    "bw_mem-fwr-8mb (mb/s)","1934.21 (min 1245.91, max 2755.77)"
    "bw_mem-rd-16mb (mb/s)","1425.70 (min 1267.63, max 1576.67)"
    "bw_mem-rd-1mb (mb/s)","1017.79 (min 520.56, max 1563.04)"
    "bw_mem-rd-2mb (mb/s)","1013.96 (min 514.87, max 1562.26)"
    "bw_mem-rd-4mb (mb/s)","1054.25 (min 594.71, max 1573.56)"
    "bw_mem-rd-8mb (mb/s)","1097.67 (min 678.20, max 1575.11)"
    "bw_mem-rdwr-16mb (mb/s)","795.82 (min 678.22, max 938.80)"
    "bw_mem-rdwr-1mb (mb/s)","548.03 (min 397.93, max 769.82)"
    "bw_mem-rdwr-2mb (mb/s)","533.22 (min 396.47, max 744.32)"
    "bw_mem-rdwr-4mb (mb/s)","585.02 (min 419.77, max 796.89)"
    "bw_mem-rdwr-8mb (mb/s)","621.08 (min 440.72, max 865.33)"
    "bw_mem-wr-16mb (mb/s)","815.25 (min 709.75, max 917.80)"
    "bw_mem-wr-1mb (mb/s)","630.18 (min 520.56, max 769.82)"
    "bw_mem-wr-2mb (mb/s)","617.21 (min 505.50, max 744.32)"
    "bw_mem-wr-4mb (mb/s)","689.76 (min 592.33, max 827.22)"
    "bw_mem-wr-8mb (mb/s)","753.35 (min 623.59, max 876.71)"
    "bw_mmap_rd-mo-1mb (mb/s)","1316.12 (min 1163.76, max 1486.16)"
    "bw_mmap_rd-o2c-1mb (mb/s)","501.44 (min 449.51, max 560.70)"
    "bw_pipe (mb/s)","451.18 (min 373.01, max 509.56)"
    "bw_unix (mb/s)","477.67 (min 424.53, max 533.19)"
    "lat_connect (us)","70.44 (min 66.29, max 74.05)"
    "lat_ctx-2-128k (us)","14.18 (min 10.78, max 18.24)"
    "lat_ctx-2-256k (us)","25.92 (min 17.18, max 33.03)"
    "lat_ctx-4-128k (us)","15.49 (min 11.20, max 18.76)"
    "lat_ctx-4-256k (us)","11.87 (min 2.03, max 17.07)"
    "lat_fs-0k (num_files)","196.75 (min 184.00, max 207.00)"
    "lat_fs-10k (num_files)","88.13 (min 80.00, max 95.00)"
    "lat_fs-1k (num_files)","131.13 (min 117.00, max 140.00)"
    "lat_fs-4k (num_files)","131.50 (min 116.00, max 140.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","47.61 (min 42.75, max 52.39)"
    "lat_mem_rd-stride128-sz125k (ns)","6.19 (min 6.17, max 6.24)"
    "lat_mem_rd-stride128-sz250k (ns)","11.95 (min 9.14, max 16.02)"
    "lat_mem_rd-stride128-sz31k (ns)","3.78 (min 2.42, max 4.44)"
    "lat_mem_rd-stride128-sz50 (ns)","2.40 (min 2.40, max 2.41)"
    "lat_mem_rd-stride128-sz500k (ns)","43.36 (min 37.83, max 47.82)"
    "lat_mem_rd-stride128-sz62k (ns)","5.64 (min 4.95, max 5.76)"
    "lat_mmap-1m (us)","60.38 (min 57.00, max 68.00)"
    "lat_ops-double-add (ns)","3.21"
    "lat_ops-double-div (ns)","17.65 (min 17.64, max 17.66)"
    "lat_ops-double-mul (ns)","3.21"
    "lat_ops-float-add (ns)","3.21"
    "lat_ops-float-div (ns)","10.43 (min 10.43, max 10.44)"
    "lat_ops-float-mul (ns)","3.21"
    "lat_ops-int-add (ns)","0.80"
    "lat_ops-int-bit (ns)","0.53"
    "lat_ops-int-div (ns)","4.82 (min 4.81, max 4.82)"
    "lat_ops-int-mod (ns)","5.08 (min 5.08, max 5.09)"
    "lat_ops-int-mul (ns)","3.48 (min 3.44, max 3.51)"
    "lat_ops-int64-add (ns)","0.80"
    "lat_ops-int64-bit (ns)","0.53 (min 0.53, max 0.54)"
    "lat_ops-int64-div (ns)","7.62 (min 7.62, max 7.63)"
    "lat_ops-int64-mod (ns)","5.88 (min 5.88, max 5.89)"
    "lat_ops-int64-mul (ns)","3.99 (min 3.98, max 3.99)"
    "lat_pagefault (us)","0.90 (min 0.83, max 0.99)"
    "lat_pipe (us)","26.34 (min 25.59, max 27.41)"
    "lat_proc-exec (us)","1394.59 (min 1262.00, max 1528.25)"
    "lat_proc-fork (us)","1229.03 (min 1120.80, max 1349.80)"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","38.25 (min 38.05, max 38.51)"
    "lat_sem (us)","3.97 (min 3.64, max 4.35)"
    "lat_sig-catch (us)","6.05 (min 5.87, max 6.26)"
    "lat_sig-install (us)","0.72 (min 0.72, max 0.74)"
    "lat_sig-prot (us)","0.62 (min 0.57, max 0.67)"
    "lat_syscall-fstat (us)","2.25 (min 2.18, max 2.38)"
    "lat_syscall-null (us)","0.52 (min 0.51, max 0.53)"
    "lat_syscall-open (us)","493.24 (min 374.64, max 590.10)"
    "lat_syscall-read (us)","0.91 (min 0.88, max 0.92)"
    "lat_syscall-stat (us)","5.40 (min 5.27, max 5.67)"
    "lat_syscall-write (us)","0.87 (min 0.83, max 0.91)"
    "lat_tcp (us)","1.05 (min 1.02, max 1.10)"
    "lat_unix (us)","33.32 (min 32.78, max 34.30)"
    "latency_for_0.50_mb_block_size (nanosec)","43.36 (min 37.83, max 47.82)"
    "latency_for_1.00_mb_block_size (nanosec)","23.80 (min 0.00, max 52.39)"
    "pipe_bandwidth (mb\s)","451.18 (min 373.01, max 509.56)"
    "pipe_latency (microsec)","26.34 (min 25.59, max 27.41)"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","38.25 (min 38.05, max 38.51)"
    "semaphore_latency (microsec)","3.97 (min 3.64, max 4.35)"
    "signal_handler_latency (microsec)","0.72 (min 0.72, max 0.74)"
    "signal_handler_overhead (microsec)","6.05 (min 5.87, max 6.26)"
    "tcp_ip_connection_cost_to_localhost (microsec)","70.44 (min 66.29, max 74.05)"
    "tcp_latency_using_localhost (microsec)","1.05 (min 1.02, max 1.10)"



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
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cpu_clock (mhz)","400.00"
    "dhrystone_per_mhz (dmips/mhz)","9.03 (min 8.90, max 9.20)"
    "dhrystone_per_second (dhrystonep)","6339605.78 (min 6250000.00, max 6451613.00)"



Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "whetstone (mips)","5625.00 (min 5000.00, max 10000.00)"



Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "linpack (kflops)","513526.67 (min 511598.00, max 515322.00)"



NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "assignment (iterations)","12.93 (min 12.89, max 12.97)"
    "fourier (iterations)","20382.13 (min 20379.00, max 20384.00)"
    "fp_emulation (iterations)","192.44 (min 192.37, max 192.47)"
    "huffman (iterations)","1057.10 (min 1056.70, max 1057.30)"
    "idea (iterations)","3075.39 (min 3075.10, max 3075.60)"
    "lu_decomposition (iterations)","472.38 (min 471.18, max 473.82)"
    "neural_net (iterations)","7.72 (min 7.69, max 7.73)"
    "numeric_sort (iterations)","559.37 (min 555.24, max 561.74)"
    "string_sort (iterations)","146.37 (min 146.34, max 146.39)"



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
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "add (mb/s)","1814.33 (min 1507.90, max 1859.50)"
    "copy (mb/s)","1907.35 (min 1562.40, max 1976.20)"
    "scale (mb/s)","2009.28 (min 1651.30, max 2080.60)"
    "triad (mb/s)","1792.49 (min 1490.60, max 1837.30)"




CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","37.24 (min 37.04, max 37.45)"
    "core (workloads/)","0.27"
    "coremark-pro ()","714.25 (min 680.43, max 728.34)"
    "linear_alg-mid-100x100-sp (workloads/)","13.09 (min 13.07, max 13.10)"
    "loops-all-mid-10k-sp (workloads/)","0.58 (min 0.56, max 0.59)"
    "nnet_test (workloads/)","0.97"
    "parser-125k (workloads/)","6.42 (min 5.24, max 7.04)"
    "radix2-big-64k (workloads/)","20.92 (min 18.16, max 22.04)"
    "sha-test (workloads/)","71.77 (min 69.44, max 72.46)"
    "zip-test (workloads/)","19.19 (min 18.87, max 19.61)"



.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","73.00 (min 71.94, max 73.53)"
    "core (workloads/)","0.54"
    "coremark-pro ()","1227.03 (min 1186.04, max 1267.74)"
    "linear_alg-mid-100x100-sp (workloads/)","26.06 (min 25.92, max 26.14)"
    "loops-all-mid-10k-sp (workloads/)","1.03 (min 0.99, max 1.08)"
    "nnet_test (workloads/)","1.93 (min 1.93, max 1.94)"
    "parser-125k (workloads/)","6.48 (min 5.78, max 7.22)"
    "radix2-big-64k (workloads/)","28.01 (min 24.43, max 32.16)"
    "sha-test (workloads/)","140.88 (min 136.99, max 142.86)"
    "zip-test (workloads/)","34.23 (min 32.79, max 36.36)"



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
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "4m-check (workloads/)","280.25 (min 263.49, max 314.58)"
    "4m-check-reassembly (workloads/)","56.17 (min 52.44, max 64.10)"
    "4m-check-reassembly-tcp (workloads/)","36.29 (min 34.34, max 40.92)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","15.99 (min 15.14, max 17.81)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","0.92 (min 0.89, max 0.95)"
    "4m-cmykw2 (workloads/)","109.32 (min 107.64, max 111.79)"
    "4m-cmykw2-rotatew2 (workloads/)","20.95 (min 19.16, max 24.17)"
    "4m-reassembly (workloads/)","51.98 (min 48.40, max 60.06)"
    "4m-rotatew2 (workloads/)","20.48 (min 18.58, max 22.06)"
    "4m-tcp-mixed (workloads/)","99.60 (min 98.16, max 104.58)"
    "4m-x264w2 (workloads/)","0.94 (min 0.93, max 0.96)"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","16.93 (min 16.59, max 17.09)"
    "idct-4mw1 (workloads/)","16.93 (min 16.61, max 17.10)"
    "ippktcheck-4m (workloads/)","280.55 (min 264.63, max 314.55)"
    "ippktcheck-4mw1 (workloads/)","279.72 (min 264.05, max 312.77)"
    "ipres-4m (workloads/)","66.59 (min 62.32, max 76.26)"
    "ipres-4mw1 (workloads/)","66.74 (min 62.21, max 77.16)"
    "md5-4m (workloads/)","18.51 (min 17.80, max 20.26)"
    "md5-4mw1 (workloads/)","18.76 (min 18.18, max 19.69)"
    "rgbcmyk-4m (workloads/)","56.72 (min 56.23, max 57.41)"
    "rgbcmyk-4mw1 (workloads/)","56.78 (min 56.32, max 57.29)"
    "rotate-4ms1 (workloads/)","18.75 (min 17.48, max 21.19)"
    "rotate-4ms1w1 (workloads/)","18.66 (min 17.66, max 20.72)"
    "rotate-4ms64 (workloads/)","18.80 (min 17.77, max 20.95)"
    "rotate-4ms64w1 (workloads/)","19.06 (min 17.84, max 22.76)"
    "x264-4mq (workloads/)","0.50 (min 0.50, max 0.51)"
    "x264-4mqw1 (workloads/)","0.50 (min 0.50, max 0.51)"



Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62lxx_evm-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","19.88 (min 17.98, max 25.20)"

 

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.


|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62lxx_evm-fs: Throughput (bits/sec)","am62lxx_evm-fs: CPU Load (%)"

    "11025","352796.09 (min 352795.00, max 352799.00)","0.30 (min 0.23, max 0.48)"
    "16000","511995.18 (min 511993.00, max 511999.00)","0.32 (min 0.20, max 0.55)"
    "22050","705582.36 (min 705523.00, max 705596.00)","0.33 (min 0.28, max 0.37)"
    "24000","705590.73 (min 705588.00, max 705596.00)","0.38 (min 0.34, max 0.43)"
    "32000","1023987.82 (min 1023985.00, max 1023995.00)","0.40 (min 0.21, max 1.18)"
    "44100","1411159.45 (min 1410927.00, max 1411193.00)","0.50 (min 0.43, max 0.56)"
    "48000","1535980.91 (min 1535976.00, max 1535992.00)","0.75 (min 0.42, max 2.97)"
    "88200","2822264.91 (min 2821350.00, max 2822376.00)","0.98 (min 0.86, max 1.08)"
    "96000","3071944.73 (min 3071933.00, max 3071967.00)","0.66 (min 0.30, max 3.07)"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62lxx_evm-fs: Throughput (bits/sec)","am62lxx_evm-fs: CPU Load (%)"

    "11025","352943.67 (min 352942.00, max 352947.00)","0.31 (min 0.21, max 0.44)"
    "16000","512209.17 (min 512205.00, max 512214.00)","0.26 (min 0.17, max 0.37)"
    "22050","705876.08 (min 705834.00, max 705889.00)","0.30 (min 0.24, max 0.39)"
    "24000","705886.42 (min 705884.00, max 705891.00)","0.35 (min 0.29, max 0.43)"
    "32000","1024416.42 (min 1024413.00, max 1024424.00)","0.31 (min 0.21, max 0.69)"
    "44100","1411742.25 (min 1411579.00, max 1411784.00)","0.43 (min 0.38, max 0.51)"
    "48000","1536623.92 (min 1536619.00, max 1536636.00)","0.60 (min 0.41, max 0.92)"
    "88200","2823412.83 (min 2822773.00, max 2823559.00)","0.80 (min 0.73, max 0.91)"
    "96000","3073230.64 (min 3073221.00, max 3073254.00)","0.73 (min 0.29, max 2.03)"


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


.. rubric::  TCP Bidirectional Throughput 
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","932.42 (min 315.68, max 1272.81)","85.10 (min 47.92, max 100.00)"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1224.89 (min 1089.90, max 1387.62)","97.80 (min 92.06, max 99.99)"




.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62lxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: Packets Per Second (kPPS)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","41.92 (min 12.23, max 49.53)","91.38 (min 85.00, max 97.00)","81.74 (min 79.77, max 84.67)"
    "128","82.00","86.33 (min 50.77, max 97.64)","89.45 (min 77.00, max 95.00)","75.62 (min 50.37, max 83.33)"
    "256","210.00","171.57 (min 139.16, max 189.82)","86.25 (min 78.00, max 93.00)","75.94 (min 50.62, max 82.88)"
    "1024","978.00","488.10 (min 181.00, max 683.63)","60.10 (min 22.00, max 83.00)","62.42 (min 26.04, max 79.88)"
    "1518","1472.00","712.23 (min 653.18, max 870.48)","59.00 (min 54.00, max 74.00)","74.48 (min 72.13, max 80.78)"




.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62lxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: Packets Per Second (kPPS)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","2.55 (min 2.15, max 3.33)","5.00 (min 4.00, max 7.00)","4.77 (min 3.83, max 6.57)"
    "128","82.00","5.99 (min 4.10, max 7.68)","6.33 (min 4.00, max 8.00)","3.40 (min 1.92, max 6.28)"
    "256","210.00","12.24 (min 1.02, max 15.36)","6.09 (min 0.00, max 8.00)","4.60 (min 0.54, max 7.52)"
    "1024","978.00","55.74 (min 39.32, max 65.72)","6.83 (min 5.00, max 8.00)","6.64 (min 3.03, max 10.09)"
    "1518","1472.00","63.39 (min 8.24, max 98.92)","5.50 (min 1.00, max 8.00)","5.70 (min 0.89, max 10.58)"




.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62lxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: Packets Per Second (kPPS)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","am62lxx_evm-fs: Packet Loss %"

    "64","","72.74 (min 68.22, max 80.12)","142.00 (min 133.00, max 156.00)","83.20 (min 81.93, max 85.28)","74.92 (min 61.45, max 82.42)"
    "128","82.00","133.35 (min 64.37, max 165.54)","136.25 (min 98.00, max 162.00)","84.18 (min 72.40, max 88.93)","70.62 (min 52.05, max 85.34)"
    "256","210.00","262.08 (min 170.59, max 311.88)","131.45 (min 102.00, max 152.00)","83.40 (min 75.15, max 87.02)","51.76 (min 28.30, max 76.63)"
    "1024","978.00","740.76 (min 558.42, max 876.07)","91.08 (min 68.00, max 107.00)","85.63 (min 77.24, max 92.38)","9.14 (min 4.33, max 17.50)"
    "1518","1472.00","753.68 (min 444.48, max 895.93)","64.00 (min 38.00, max 76.00)","81.54 (min 60.50, max 90.29)","6.15 (min 0.64, max 9.91)"


|

Linux OSPI Flash Driver
-------------------------


AM62XX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^


RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62lxx_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","17.29 (min 16.89, max 17.67)"

 

AM62LXX-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write UBIFS Throughput (Mbytes/sec)","am62lxx_evm-fs: Write UBIFS CPU Load (%)","am62lxx_evm-fs: Read UBIFS Throughput (Mbytes/sec)","am62lxx_evm-fs: Read UBIFS CPU Load (%)"

    "102400","3.83 (min 3.45, max 4.17)","28.48 (min 24.75, max 32.35)","11.35 (min 11.20, max 11.52)","32.57 (min 27.59, max 37.14)"
    "262144","3.76 (min 3.33, max 4.18)","28.21 (min 23.76, max 36.11)","11.33 (min 11.04, max 11.56)","35.23 (min 30.00, max 40.00)"
    "524288","3.73 (min 3.34, max 4.19)","28.86 (min 23.81, max 45.61)","11.32 (min 11.14, max 11.58)","33.91 (min 29.03, max 38.89)"
    "1048576","3.77 (min 3.33, max 4.22)","28.69 (min 22.55, max 33.65)","11.26 (min 11.09, max 11.46)","35.56 (min 29.03, max 40.54)"


RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62lxx_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","17.29 (min 16.89, max 17.67)"


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
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

    "1m","128.09 (min 128.00, max 129.00)","8.78 (min 8.62, max 9.02)","179.55 (min 179.00, max 180.00)","8.10 (min 7.36, max 8.35)"
    "4m","127.64 (min 125.00, max 129.00)","5.47 (min 5.09, max 5.69)","179.18 (min 179.00, max 180.00)","4.94 (min 4.69, max 5.20)"
    "4k","82.85 (min 75.50, max 86.90)","60.78 (min 59.59, max 62.96)","88.41 (min 85.50, max 91.00)","56.55 (min 55.14, max 58.55)"
    "256k","122.82 (min 122.00, max 123.00)","11.89 (min 11.32, max 12.14)","178.18 (min 177.00, max 179.00)","10.21 (min 9.89, max 10.55)"


EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "1m","127.08 (min 122.00, max 129.00)","7.88 (min 7.24, max 8.20)","180.00","7.61 (min 6.21, max 8.13)"
    "4m","128.54 (min 128.00, max 129.00)","5.29 (min 4.90, max 5.68)","180.00","4.71 (min 4.39, max 5.05)"
    "4k","94.25 (min 90.40, max 96.50)","47.94 (min 46.23, max 49.73)","93.92 (min 91.80, max 96.30)","54.26 (min 52.60, max 57.08)"
    "256k","122.77 (min 118.00, max 125.00)","9.94 (min 9.03, max 10.37)","178.54 (min 178.00, max 179.00)","9.33 (min 7.73, max 10.01)"


EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

    "102400","89.95 (min 81.91, max 99.06)","20.14 (min 16.67, max 26.53)","180.24 (min 178.28, max 181.35)","38.95 (min 36.11, max 41.59)"
    "262144","94.39 (min 82.96, max 99.33)","21.11 (min 18.57, max 26.64)","184.25 (min 183.09, max 185.21)","38.34 (min 35.51, max 48.18)"
    "524288","95.44 (min 84.33, max 100.71)","21.19 (min 18.69, max 26.21)","186.73 (min 186.35, max 187.13)","33.40 (min 30.84, max 35.14)"
    "1048576","95.63 (min 84.01, max 101.22)","20.93 (min 17.84, max 26.61)","186.55 (min 186.13, max 186.94)","32.91 (min 31.78, max 34.55)"
    "5242880","95.84 (min 85.17, max 100.83)","20.72 (min 18.31, max 26.10)","186.14 (min 185.24, max 186.78)","33.33 (min 31.48, max 34.82)"


EMMC EXT2
^^^^^^^^^


.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT2 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT2 CPU Load (%)","am62lxx_evm-fs: Read EXT2 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT2 CPU Load (%)"

    "102400","33.22 (min 16.63, max 37.66)","15.99 (min 12.80, max 23.97)","174.78 (min 168.57, max 176.68)","39.40 (min 36.70, max 41.59)"
    "262144","48.63 (min 20.43, max 63.88)","17.72 (min 12.16, max 25.76)","179.48 (min 175.01, max 181.23)","38.53 (min 36.94, max 40.87)"
    "524288","59.55 (min 22.13, max 76.08)","18.73 (min 15.46, max 26.62)","181.73 (min 177.71, max 182.42)","33.12 (min 31.82, max 35.34)"
    "1048576","66.02 (min 22.84, max 84.31)","18.83 (min 14.96, max 26.95)","181.17 (min 176.66, max 181.82)","33.17 (min 31.53, max 35.40)"
    "5242880","76.28 (min 23.43, max 91.74)","20.31 (min 17.17, max 29.32)","180.86 (min 177.57, max 181.84)","32.91 (min 31.53, max 34.75)"


EMMC VFAT
^^^^^^^^^


.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write VFAT Throughput (Mbytes/sec)","am62lxx_evm-fs: Write VFAT CPU Load (%)","am62lxx_evm-fs: Read VFAT Throughput (Mbytes/sec)","am62lxx_evm-fs: Read VFAT CPU Load (%)"

    "102400","32.51 (min 16.29, max 36.85)","15.82 (min 13.44, max 19.58)","172.29 (min 169.56, max 173.89)","39.02 (min 36.94, max 40.52)"
    "262144","47.09 (min 20.19, max 62.79)","17.59 (min 13.14, max 21.52)","177.08 (min 175.97, max 177.69)","38.17 (min 37.17, max 39.13)"
    "524288","56.02 (min 21.98, max 70.61)","18.85 (min 15.85, max 22.42)","177.08 (min 176.50, max 177.67)","32.90 (min 31.30, max 35.04)"
    "1048576","61.25 (min 22.84, max 75.98)","19.85 (min 17.81, max 23.49)","177.32 (min 176.61, max 177.85)","32.79 (min 30.97, max 34.19)"
    "5242880","70.86 (min 23.63, max 85.00)","20.74 (min 19.31, max 23.77)","176.55 (min 176.03, max 177.18)","32.28 (min 30.97, max 33.90)"


UBoot EMMC Driver
-----------------


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62lxx_evm-fs: Write Throughput (Kbytes/sec)","am62lxx_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","111773.53 (min 105703.23, max 117870.50)","175229.95"
    "4000000","125710.23 (min 123886.58, max 128000.00)","178198.94 (min 178086.96, max 178572.21)"


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
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

    "1m","18.77 (min 17.90, max 19.80)","2.36 (min 1.91, max 2.69)","85.09 (min 79.70, max 87.30)","5.35 (min 4.63, max 5.70)"
    "4m","18.70 (min 17.70, max 19.50)","1.68 (min 1.50, max 1.96)","84.56 (min 76.30, max 86.90)","3.13 (min 2.75, max 3.43)"
    "4k","4.47 (min 4.25, max 4.74)","10.39 (min 8.49, max 11.72)","13.52 (min 13.40, max 13.60)","14.22 (min 12.04, max 17.18)"
    "256k","18.38 (min 17.30, max 19.20)","3.59 (min 3.08, max 3.96)","82.45 (min 79.50, max 83.60)","6.72 (min 5.94, max 7.40)"


MMC RAW FIO 1G
^^^^^^^^^^^^^^

.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "1m","22.89 (min 18.50, max 43.30)","2.23 (min 1.61, max 2.99)","87.52 (min 86.80, max 88.10)","4.48 (min 3.90, max 4.78)"
    "4m","22.47 (min 18.50, max 42.50)","1.75 (min 1.35, max 2.22)","87.58 (min 86.90, max 88.20)","2.96 (min 2.51, max 3.36)"
    "4k","3.98 (min 2.80, max 4.47)","5.92 (min 4.35, max 7.08)","13.52 (min 13.10, max 13.60)","11.51 (min 9.36, max 13.34)"
    "256k","21.43 (min 17.40, max 37.70)","3.21 (min 2.65, max 4.31)","83.23 (min 82.20, max 84.30)","5.82 (min 4.84, max 6.32)"


MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "102400","9.42 (min 8.48, max 10.75)","2.28 (min 1.67, max 3.26)","11.03 (min 10.62, max 11.78)","2.69 (min 2.31, max 2.99)"
    "262144","9.41 (min 8.66, max 10.66)","2.29 (min 1.74, max 3.45)","11.06 (min 10.59, max 11.92)","2.39 (min 2.12, max 2.78)"
    "524288","9.43 (min 8.71, max 10.85)","2.24 (min 1.71, max 3.47)","11.00 (min 10.74, max 11.26)","2.02 (min 1.76, max 2.24)"
    "1048576","9.38 (min 8.86, max 10.52)","2.34 (min 1.62, max 3.95)","11.11 (min 10.82, max 11.48)","2.04 (min 1.79, max 2.26)"
    "5242880","9.43 (min 8.83, max 10.68)","2.20 (min 1.62, max 3.92)","11.35 (min 10.84, max 12.01)","2.10 (min 1.71, max 2.35)"

MMC EXT3
^^^^^^^^

.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "102400","23.20 (min 15.57, max 40.38)","6.01 (min 3.41, max 14.56)","76.27 (min 71.64, max 78.41)","17.37 (min 14.67, max 20.80)"
    "262144","22.76 (min 15.81, max 39.78)","5.79 (min 3.29, max 13.83)","81.99 (min 79.01, max 85.25)","16.70 (min 15.33, max 18.15)"
    "524288","23.16 (min 16.44, max 39.82)","5.72 (min 3.30, max 14.22)","86.75 (min 83.12, max 89.74)","15.42 (min 13.25, max 17.32)"
    "1048576","22.52 (min 16.11, max 36.71)","5.54 (min 3.17, max 13.11)","88.33 (min 82.79, max 89.91)","15.29 (min 13.55, max 17.99)"
    "5242880","22.91 (min 16.00, max 39.33)","5.69 (min 3.34, max 13.42)","87.07 (min 82.59, max 89.42)","15.07 (min 12.80, max 17.15)"
 

MMC EXT2
^^^^^^^^

.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "102400","13.52 (min 2.68, max 19.90)","6.03 (min 4.38, max 8.77)","75.44 (min 71.95, max 78.17)","18.59 (min 15.56, max 24.91)"
    "262144","16.84 (min 2.63, max 36.72)","5.59 (min 3.62, max 11.25)","83.89 (min 79.18, max 85.49)","17.55 (min 15.16, max 19.23)"
    "524288","17.78 (min 2.61, max 40.70)","5.27 (min 3.51, max 10.25)","88.26 (min 83.81, max 90.12)","15.92 (min 14.10, max 17.72)"
    "1048576","18.10 (min 2.91, max 40.66)","5.19 (min 3.61, max 12.89)","86.83 (min 83.40, max 90.09)","15.72 (min 13.10, max 17.20)"
    "5242880","18.08 (min 2.91, max 39.87)","5.04 (min 3.29, max 9.56)","88.72 (min 84.09, max 90.20)","15.76 (min 13.10, max 17.30)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 


UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62lxx_evm-fs: Write Throughput (Kbytes/sec)","am62lxx_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","16887.87 (min 13170.42, max 20078.43)","22546.94 (min 22505.49, max 22629.83)"
    "800000","17033.13 (min 12681.11, max 19366.43)","23025.64 (min 23011.24, max 23076.06)"
    "1000000","15915.67 (min 14499.12, max 17808.70)","23254.39 (min 23239.72, max 23272.73)"
 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)


|

USB Driver
----------
 

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62lxx_evm-fs: Throughput (MB/sec)"

    "150","40.81 (min 37.30, max 43.40)"




.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62lxx_evm-fs: Throughput (MB/sec)"

    "150","37.14 (min 30.70, max 41.70)"


Low Power Performance
---------------------

Power Performance
^^^^^^^^^^^^^^^^^

These are power measurements taken while the device is in various low power modes like
Deep Sleep and RTC Only + DDR.

.. csv-table:: Deep Sleep Power Performance
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.75", "5.41"
     "soc_dvdd_1v8", "1.80", "0.30"
     "soc_dvdd_3v3", "3.29", "3.45"
     "vdda_1v8", "1.80", "1.26"
     "vdd_lpddr4_pmic2", "1.10", "1.00"
     "vdd_rtc", "0.74", "0.02"
     "vdd_rtc_1v8", "1.80", "0.02"
     "Total"," ","11.47"

.. csv-table:: RTC Only + DDR Power Performance
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.00", "0.00"
     "soc_dvdd_1v8", "1.80", "0.36"
     "soc_dvdd_3v3", "3.29", "0.93"
     "vdda_1v8", "0.00", "0.00"
     "vdd_lpddr4_pmic2", "1.10", "1.08"
     "vdd_rtc", "0.75", "0.02"
     "vdd_rtc_1v8", "1.80", "0.02"
     "Total"," ","2.41"
