
====================================
 Linux 11.02.08.02 Performance Guide
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
-----------------

LMBench
^^^^^^^
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
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "af_unix_sock_stream_latency (microsec)","33.14 (min 32.70, max 34.50)"
    "af_unix_socket_stream_bandwidth (mb\s)","458.31 (min 416.22, max 548.49)"
    "bw_file_rd-io-1mb (mb/s)","971.18 (min 906.62, max 1128.85)"
    "bw_file_rd-o2c-1mb (mb/s)","515.41 (min 508.13, max 525.95)"
    "bw_mem-bcopy-16mb (mb/s)","742.11 (min 704.91, max 849.57)"
    "bw_mem-bcopy-1mb (mb/s)","755.61 (min 687.76, max 942.68)"
    "bw_mem-bcopy-2mb (mb/s)","748.93 (min 681.43, max 958.47)"
    "bw_mem-bcopy-4mb (mb/s)","781.73 (min 727.40, max 944.73)"
    "bw_mem-bcopy-8mb (mb/s)","801.94 (min 738.69, max 994.53)"
    "bw_mem-bzero-16mb (mb/s)","2250.16 (min 2104.16, max 2805.54)"
    "bw_mem-bzero-1mb (mb/s)","1502.54 (min 687.76, max 2800.63)"
    "bw_mem-bzero-2mb (mb/s)","1499.05 (min 681.43, max 2807.02)"
    "bw_mem-bzero-4mb (mb/s)","1516.48 (min 727.40, max 2806.03)"
    "bw_mem-bzero-8mb (mb/s)","1526.92 (min 738.69, max 2807.02)"
    "bw_mem-cp-16mb (mb/s)","422.87 (min 397.28, max 517.95)"
    "bw_mem-cp-1mb (mb/s)","1450.86 (min 401.50, max 3062.20)"
    "bw_mem-cp-2mb (mb/s)","1387.71 (min 399.24, max 2898.03)"
    "bw_mem-cp-4mb (mb/s)","1383.65 (min 434.12, max 2868.93)"
    "bw_mem-cp-8mb (mb/s)","1376.95 (min 436.56, max 2827.85)"
    "bw_mem-fcp-16mb (mb/s)","751.75 (min 710.13, max 879.75)"
    "bw_mem-fcp-1mb (mb/s)","1538.99 (min 777.24, max 2800.63)"
    "bw_mem-fcp-2mb (mb/s)","1534.98 (min 762.92, max 2807.02)"
    "bw_mem-fcp-4mb (mb/s)","1547.58 (min 788.72, max 2806.03)"
    "bw_mem-fcp-8mb (mb/s)","1556.02 (min 804.67, max 2807.02)"
    "bw_mem-frd-16mb (mb/s)","1328.40 (min 1227.75, max 1609.50)"
    "bw_mem-frd-1mb (mb/s)","1057.89 (min 777.24, max 1525.94)"
    "bw_mem-frd-2mb (mb/s)","1063.22 (min 762.92, max 1550.87)"
    "bw_mem-frd-4mb (mb/s)","1080.32 (min 788.72, max 1555.81)"
    "bw_mem-frd-8mb (mb/s)","1093.89 (min 804.67, max 1611.60)"
    "bw_mem-fwr-16mb (mb/s)","2270.76 (min 2123.71, max 2819.38)"
    "bw_mem-fwr-1mb (mb/s)","1876.87 (min 1218.45, max 3062.20)"
    "bw_mem-fwr-2mb (mb/s)","1828.62 (min 1203.61, max 2898.03)"
    "bw_mem-fwr-4mb (mb/s)","1809.91 (min 1247.47, max 2868.93)"
    "bw_mem-fwr-8mb (mb/s)","1802.83 (min 1250.00, max 2827.85)"
    "bw_mem-rd-16mb (mb/s)","1345.30 (min 1264.92, max 1616.65)"
    "bw_mem-rd-1mb (mb/s)","953.97 (min 525.76, max 1599.43)"
    "bw_mem-rd-2mb (mb/s)","940.68 (min 511.31, max 1592.61)"
    "bw_mem-rd-4mb (mb/s)","978.01 (min 513.68, max 1601.71)"
    "bw_mem-rd-8mb (mb/s)","1032.26 (min 681.02, max 1605.14)"
    "bw_mem-rdwr-16mb (mb/s)","732.31 (min 663.63, max 858.23)"
    "bw_mem-rdwr-1mb (mb/s)","503.57 (min 401.50, max 680.27)"
    "bw_mem-rdwr-2mb (mb/s)","494.06 (min 399.24, max 692.28)"
    "bw_mem-rdwr-4mb (mb/s)","553.67 (min 434.12, max 778.21)"
    "bw_mem-rdwr-8mb (mb/s)","585.97 (min 436.56, max 857.72)"
    "bw_mem-wr-16mb (mb/s)","763.43 (min 702.83, max 927.75)"
    "bw_mem-wr-1mb (mb/s)","573.83 (min 525.76, max 686.34)"
    "bw_mem-wr-2mb (mb/s)","559.79 (min 507.29, max 692.28)"
    "bw_mem-wr-4mb (mb/s)","633.10 (min 513.68, max 800.24)"
    "bw_mem-wr-8mb (mb/s)","708.78 (min 627.60, max 871.93)"
    "bw_mmap_rd-mo-1mb (mb/s)","1245.57 (min 1156.29, max 1501.22)"
    "bw_mmap_rd-o2c-1mb (mb/s)","509.91 (min 505.22, max 519.21)"
    "bw_pipe (mb/s)","426.35 (min 382.91, max 518.60)"
    "bw_unix (mb/s)","458.31 (min 416.22, max 548.49)"
    "lat_connect (us)","72.81 (min 71.39, max 76.51)"
    "lat_ctx-2-128k (us)","17.46 (min 11.52, max 25.12)"
    "lat_ctx-2-256k (us)","31.42 (min 26.43, max 34.63)"
    "lat_ctx-4-128k (us)","15.70 (min 12.41, max 17.36)"
    "lat_ctx-4-256k (us)","8.13 (min 0.00, max 16.57)"
    "lat_fs-0k (num_files)","198.17 (min 189.00, max 213.00)"
    "lat_fs-10k (num_files)","84.33 (min 76.00, max 90.00)"
    "lat_fs-1k (num_files)","127.00 (min 113.00, max 140.00)"
    "lat_fs-4k (num_files)","128.17 (min 119.00, max 134.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","49.98 (min 41.71, max 52.46)"
    "lat_mem_rd-stride128-sz125k (ns)","6.19 (min 6.16, max 6.22)"
    "lat_mem_rd-stride128-sz250k (ns)","13.46 (min 6.99, max 21.17)"
    "lat_mem_rd-stride128-sz31k (ns)","3.59 (min 2.42, max 4.45)"
    "lat_mem_rd-stride128-sz50 (ns)","2.40 (min 2.40, max 2.41)"
    "lat_mem_rd-stride128-sz500k (ns)","45.07 (min 38.07, max 48.16)"
    "lat_mem_rd-stride128-sz62k (ns)","5.74 (min 5.72, max 5.75)"
    "lat_mmap-1m (us)","59.83 (min 57.00, max 70.00)"
    "lat_ops-double-add (ns)","3.21"
    "lat_ops-double-div (ns)","17.65 (min 17.64, max 17.66)"
    "lat_ops-double-mul (ns)","3.21 (min 3.21, max 3.22)"
    "lat_ops-float-add (ns)","3.21"
    "lat_ops-float-div (ns)","10.43 (min 10.42, max 10.43)"
    "lat_ops-float-mul (ns)","3.21"
    "lat_ops-int-add (ns)","0.80"
    "lat_ops-int-bit (ns)","0.53"
    "lat_ops-int-div (ns)","4.82 (min 4.81, max 4.82)"
    "lat_ops-int-mod (ns)","5.08 (min 5.08, max 5.09)"
    "lat_ops-int-mul (ns)","3.45 (min 3.44, max 3.46)"
    "lat_ops-int64-add (ns)","0.80"
    "lat_ops-int64-bit (ns)","0.53 (min 0.53, max 0.54)"
    "lat_ops-int64-div (ns)","7.62"
    "lat_ops-int64-mod (ns)","5.88 (min 5.88, max 5.89)"
    "lat_ops-int64-mul (ns)","3.99 (min 3.98, max 4.04)"
    "lat_pagefault (us)","0.93 (min 0.81, max 0.98)"
    "lat_pipe (us)","26.36 (min 24.71, max 27.33)"
    "lat_proc-exec (us)","1447.93 (min 1267.60, max 1563.25)"
    "lat_proc-fork (us)","1269.68 (min 1094.20, max 1328.60)"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","38.21 (min 38.12, max 38.41)"
    "lat_sem (us)","4.12 (min 3.74, max 4.31)"
    "lat_sig-catch (us)","6.22 (min 6.07, max 6.38)"
    "lat_sig-install (us)","0.74 (min 0.72, max 0.78)"
    "lat_sig-prot (us)","0.69 (min 0.49, max 0.88)"
    "lat_syscall-fstat (us)","2.20 (min 2.12, max 2.31)"
    "lat_syscall-null (us)","0.51 (min 0.51, max 0.52)"
    "lat_syscall-open (us)","403.50 (min 362.00, max 459.33)"
    "lat_syscall-read (us)","0.91 (min 0.90, max 0.91)"
    "lat_syscall-stat (us)","5.41 (min 5.23, max 5.60)"
    "lat_syscall-write (us)","0.86 (min 0.84, max 0.88)"
    "lat_tcp (us)","1.02"
    "lat_unix (us)","33.14 (min 32.70, max 34.50)"
    "latency_for_0.50_mb_block_size (nanosec)","45.07 (min 38.07, max 48.16)"
    "latency_for_1.00_mb_block_size (nanosec)","24.99 (min 0.00, max 52.46)"
    "pipe_bandwidth (mb\s)","426.35 (min 382.91, max 518.60)"
    "pipe_latency (microsec)","26.36 (min 24.71, max 27.33)"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","38.21 (min 38.12, max 38.41)"
    "semaphore_latency (microsec)","4.12 (min 3.74, max 4.31)"
    "signal_handler_latency (microsec)","0.74 (min 0.72, max 0.78)"
    "signal_handler_overhead (microsec)","6.22 (min 6.07, max 6.38)"
    "tcp_ip_connection_cost_to_localhost (microsec)","72.81 (min 71.39, max 76.51)"
    "tcp_latency_using_localhost (microsec)","1.02"

Dhrystone
^^^^^^^^^
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
    "dhrystone_per_mhz (dmips/mhz)","8.90"
    "dhrystone_per_second (dhrystonep)","6250000.00"

Whetstone
^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "whetstone (mips)","5833.33 (min 5000.00, max 10000.00)"

Linpack
^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "linpack (kflops)","515149.67 (min 514088.00, max 516563.00)"

NBench
^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "assignment (iterations)","12.95 (min 12.90, max 12.97)"
    "fourier (iterations)","20382.00 (min 20379.00, max 20384.00)"
    "fp_emulation (iterations)","192.40 (min 192.33, max 192.47)"
    "huffman (iterations)","1057.02 (min 1056.80, max 1057.20)"
    "idea (iterations)","3075.14 (min 3074.90, max 3075.50)"
    "lu_decomposition (iterations)","473.43 (min 470.10, max 479.32)"
    "neural_net (iterations)","7.73 (min 7.72, max 7.73)"
    "numeric_sort (iterations)","558.36 (min 555.56, max 562.43)"
    "string_sort (iterations)","146.38 (min 146.36, max 146.39)"

Stream
^^^^^^
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

    "add (mb/s)","1651.55 (min 1501.10, max 1914.10)"
    "copy (mb/s)","1735.32 (min 1565.10, max 2033.20)"
    "scale (mb/s)","1830.72 (min 1641.00, max 2134.40)"
    "triad (mb/s)","1632.43 (min 1491.50, max 1888.40)"

CoreMarkPro
^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","37.22 (min 37.04, max 37.31)"
    "core (workloads/)","0.27"
    "coremark-pro ()","705.20 (min 686.04, max 730.09)"
    "linear_alg-mid-100x100-sp (workloads/)","13.09 (min 13.06, max 13.11)"
    "loops-all-mid-10k-sp (workloads/)","0.57 (min 0.56, max 0.60)"
    "nnet_test (workloads/)","0.97"
    "parser-125k (workloads/)","6.35 (min 5.62, max 6.99)"
    "radix2-big-64k (workloads/)","19.56 (min 17.06, max 22.07)"
    "sha-test (workloads/)","71.11 (min 69.93, max 72.46)"
    "zip-test (workloads/)","18.99 (min 18.52, max 19.61)"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","72.89 (min 71.94, max 74.07)"
    "core (workloads/)","0.54 (min 0.53, max 0.54)"
    "coremark-pro ()","1226.57 (min 1185.87, max 1277.14)"
    "linear_alg-mid-100x100-sp (workloads/)","26.03 (min 25.97, max 26.11)"
    "loops-all-mid-10k-sp (workloads/)","1.03 (min 1.00, max 1.07)"
    "nnet_test (workloads/)","1.93 (min 1.93, max 1.94)"
    "parser-125k (workloads/)","6.48 (min 5.81, max 7.33)"
    "radix2-big-64k (workloads/)","28.39 (min 25.03, max 31.84)"
    "sha-test (workloads/)","140.47 (min 138.89, max 142.86)"
    "zip-test (workloads/)","34.17 (min 32.26, max 35.71)"

MultiBench
^^^^^^^^^^
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

    "4m-check (workloads/)","288.19 (min 268.24, max 314.90)"
    "4m-check-reassembly (workloads/)","57.34 (min 52.49, max 63.94)"
    "4m-check-reassembly-tcp (workloads/)","36.65 (min 34.01, max 40.39)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","16.34 (min 15.28, max 18.05)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","0.93 (min 0.91, max 0.95)"
    "4m-cmykw2 (workloads/)","109.44 (min 107.88, max 112.05)"
    "4m-cmykw2-rotatew2 (workloads/)","21.20 (min 19.46, max 23.21)"
    "4m-reassembly (workloads/)","52.91 (min 49.41, max 58.24)"
    "4m-rotatew2 (workloads/)","21.26 (min 19.25, max 23.63)"
    "4m-tcp-mixed (workloads/)","95.76 (min 93.02, max 98.16)"
    "4m-x264w2 (workloads/)","0.94 (min 0.93, max 0.96)"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","16.97 (min 16.90, max 17.08)"
    "idct-4mw1 (workloads/)","16.97 (min 16.89, max 17.09)"
    "ippktcheck-4m (workloads/)","288.16 (min 267.84, max 314.11)"
    "ippktcheck-4mw1 (workloads/)","287.54 (min 267.58, max 312.77)"
    "ipres-4m (workloads/)","68.41 (min 62.50, max 76.69)"
    "ipres-4mw1 (workloads/)","68.31 (min 62.47, max 76.18)"
    "md5-4m (workloads/)","18.99 (min 17.91, max 20.68)"
    "md5-4mw1 (workloads/)","19.11 (min 18.16, max 20.15)"
    "rgbcmyk-4m (workloads/)","56.70 (min 56.45, max 57.08)"
    "rgbcmyk-4mw1 (workloads/)","56.64 (min 56.32, max 57.01)"
    "rotate-4ms1 (workloads/)","19.37 (min 17.85, max 20.73)"
    "rotate-4ms1w1 (workloads/)","19.04 (min 17.85, max 20.74)"
    "rotate-4ms64 (workloads/)","19.51 (min 18.04, max 22.62)"
    "rotate-4ms64w1 (workloads/)","19.33 (min 18.01, max 21.44)"
    "x264-4mq (workloads/)","0.50 (min 0.50, max 0.51)"
    "x264-4mqw1 (workloads/)","0.50 (min 0.49, max 0.51)"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62lxx_evm-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","19.01 (min 17.68, max 27.66)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

ALSA SoC Audio Driver
---------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62lxx_evm-fs: Throughput (bits/sec)","am62lxx_evm-fs: CPU Load (%)"

    "11025","352795.83 (min 352795.00, max 352797.00)","0.38 (min 0.29, max 0.48)"
    "16000","511995.00 (min 511994.00, max 511996.00)","0.35 (min 0.20, max 0.79)"
    "22050","705589.67 (min 705586.00, max 705594.00)","0.40 (min 0.30, max 0.53)"
    "24000","705591.50 (min 705589.00, max 705595.00)","0.47 (min 0.37, max 0.60)"
    "32000","1023987.83 (min 1023985.00, max 1023991.00)","0.30 (min 0.21, max 0.40)"
    "44100","1411182.17 (min 1411179.00, max 1411186.00)","0.59 (min 0.50, max 0.72)"
    "48000","1535980.33 (min 1535976.00, max 1535985.00)","0.91 (min 0.23, max 1.56)"
    "88200","2822355.00 (min 2822349.00, max 2822363.00)","1.09 (min 0.93, max 1.20)"
    "96000","3071938.67 (min 3071934.00, max 3071943.00)","1.22 (min 0.39, max 3.19)"

.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62lxx_evm-fs: Throughput (bits/sec)","am62lxx_evm-fs: CPU Load (%)"

    "11025","352943.17 (min 352943.00, max 352944.00)","0.30 (min 0.19, max 0.42)"
    "16000","512208.83 (min 512208.00, max 512209.00)","0.26 (min 0.17, max 0.42)"
    "22050","705883.83 (min 705882.00, max 705888.00)","0.30 (min 0.25, max 0.41)"
    "24000","705886.17 (min 705886.00, max 705887.00)","0.33 (min 0.29, max 0.36)"
    "32000","1024415.50 (min 1024414.00, max 1024417.00)","0.30 (min 0.19, max 0.65)"
    "44100","1411772.17 (min 1411772.00, max 1411773.00)","0.41 (min 0.38, max 0.45)"
    "48000","1536622.00 (min 1536621.00, max 1536623.00)","0.50 (min 0.19, max 0.95)"
    "88200","2823534.17 (min 2823531.00, max 2823536.00)","0.77 (min 0.73, max 0.81)"
    "96000","3073226.00 (min 3073218.00, max 3073234.00)","0.56 (min 0.31, max 1.58)"

|

Linux OSPI Flash Driver
-----------------------

.. rubric:: UBIFS
   :name: am62lxx-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write UBIFS Throughput (Mbytes/sec)","am62lxx_evm-fs: Write UBIFS CPU Load (%)","am62lxx_evm-fs: Read UBIFS Throughput (Mbytes/sec)","am62lxx_evm-fs: Read UBIFS CPU Load (%)"

    "102400","3.84 (min 3.55, max 4.17)","29.68 (min 24.49, max 34.58)","11.32 (min 11.19, max 11.63)","33.47 (min 31.25, max 35.29)"
    "262144","3.77 (min 3.49, max 4.27)","28.92 (min 24.49, max 33.65)","11.31 (min 11.20, max 11.55)","33.93 (min 31.25, max 37.14)"
    "524288","3.76 (min 3.45, max 4.15)","28.78 (min 25.49, max 33.98)","11.28 (min 11.19, max 11.50)","33.96 (min 31.25, max 35.29)"
    "1048576","3.77 (min 3.44, max 4.13)","28.45 (min 24.72, max 32.20)","11.18 (min 11.05, max 11.31)","37.67 (min 35.29, max 38.89)"

.. rubric:: RAW
   :name: am62lxx-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62lxx_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","17.36 (min 16.95, max 17.67)"

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

    "1m","128.17 (min 128.00, max 129.00)","8.56 (min 8.30, max 8.86)","179.33 (min 179.00, max 180.00)","7.98 (min 7.62, max 8.22)"
    "4m","127.50 (min 125.00, max 128.00)","5.46 (min 5.28, max 5.63)","179.50 (min 179.00, max 180.00)","4.95 (min 4.74, max 5.08)"
    "4k","86.62 (min 86.40, max 86.90)","59.76 (min 59.27, max 60.23)","90.67 (min 88.60, max 93.50)","56.33 (min 55.48, max 56.62)"
    "256k","122.83 (min 122.00, max 123.00)","11.83 (min 11.60, max 12.02)","178.33 (min 178.00, max 179.00)","10.08 (min 9.65, max 10.27)"

EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "1m","127.83 (min 122.00, max 129.00)","7.85 (min 7.48, max 7.99)","180.00","7.63 (min 7.16, max 8.07)"
    "4m","129.00","5.33 (min 5.10, max 5.56)","180.00","4.67 (min 4.51, max 4.96)"
    "4k","95.57 (min 93.50, max 96.40)","47.29 (min 45.85, max 48.11)","94.90 (min 94.00, max 95.80)","53.35 (min 52.55, max 54.08)"
    "256k","122.67 (min 118.00, max 124.00)","9.76 (min 9.54, max 10.07)","178.17 (min 178.00, max 179.00)","9.31 (min 9.00, max 9.65)"

EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

    "102400","90.91 (min 83.00, max 97.71)","20.38 (min 17.87, max 25.90)","180.36 (min 177.78, max 181.30)","37.46 (min 36.45, max 39.09)"
    "262144","94.89 (min 83.93, max 100.22)","20.88 (min 18.72, max 25.51)","183.72 (min 177.40, max 185.29)","39.71 (min 36.70, max 50.88)"
    "524288","95.62 (min 84.98, max 101.40)","20.84 (min 18.31, max 26.53)","186.81 (min 186.21, max 187.09)","32.93 (min 31.82, max 34.26)"
    "1048576","95.42 (min 82.97, max 100.97)","21.14 (min 18.45, max 26.53)","186.89 (min 186.56, max 187.07)","32.73 (min 32.11, max 33.33)"
    "5242880","96.51 (min 85.25, max 101.40)","20.64 (min 17.87, max 25.82)","186.37 (min 185.98, max 186.68)","32.98 (min 32.43, max 33.64)"

EMMC VFAT
^^^^^^^^^

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write VFAT Throughput (Mbytes/sec)","am62lxx_evm-fs: Write VFAT CPU Load (%)","am62lxx_evm-fs: Read VFAT Throughput (Mbytes/sec)","am62lxx_evm-fs: Read VFAT CPU Load (%)"

    "102400","32.73 (min 16.59, max 37.40)","15.81 (min 14.03, max 18.56)","173.62 (min 172.15, max 174.70)","39.10 (min 37.72, max 40.52)"
    "262144","47.45 (min 20.52, max 63.09)","17.72 (min 13.82, max 23.74)","174.94 (min 164.63, max 177.64)","40.50 (min 36.61, max 55.74)"
    "524288","56.02 (min 22.44, max 71.58)","18.76 (min 12.94, max 22.48)","177.43 (min 177.03, max 177.74)","32.31 (min 30.97, max 34.19)"
    "1048576","61.76 (min 23.47, max 77.61)","19.71 (min 18.09, max 22.20)","177.54 (min 175.95, max 178.35)","34.28 (min 31.62, max 40.71)"
    "5242880","71.24 (min 24.09, max 85.03)","20.62 (min 18.65, max 23.67)","176.90 (min 176.63, max 177.31)","32.18 (min 30.70, max 33.90)"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62lxx_evm-fs: Write Throughput (Kbytes/sec)","am62lxx_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","112634.05 (min 110702.70, max 116198.58)","174765.56 (min 173375.66, max 175229.95)"
    "4000000","125497.58 (min 122268.66, max 127254.37)","178086.96"

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

    "1m","35.31 (min 18.70, max 42.30)","3.38 (min 2.18, max 4.24)","87.01 (min 86.40, max 87.50)","5.29 (min 4.42, max 5.60)"
    "4m","34.96 (min 18.70, max 42.40)","2.36 (min 1.75, max 2.97)","86.47 (min 83.20, max 87.40)","3.02 (min 2.66, max 3.38)"
    "4k","3.23 (min 2.74, max 4.29)","7.39 (min 5.78, max 9.52)","13.10 (min 12.90, max 13.50)","12.51 (min 11.54, max 13.83)"
    "256k","31.90 (min 18.00, max 38.20)","5.09 (min 3.67, max 6.32)","83.10 (min 82.00, max 83.90)","6.51 (min 5.61, max 6.78)"

MMC RAW FIO 1G
^^^^^^^^^^^^^^

.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "1m","31.02 (min 18.20, max 44.20)","2.80 (min 1.82, max 3.70)","87.63 (min 87.10, max 88.00)","4.61 (min 4.27, max 5.11)"
    "4m","30.72 (min 18.20, max 43.60)","2.09 (min 1.32, max 2.68)","87.67 (min 87.00, max 88.10)","3.00 (min 2.61, max 3.48)"
    "4k","3.45 (min 2.80, max 4.15)","5.24 (min 4.23, max 6.10)","13.32 (min 13.00, max 13.60)","11.41 (min 10.56, max 12.38)"
    "256k","27.70 (min 17.60, max 38.60)","3.72 (min 2.58, max 4.57)","83.30 (min 82.10, max 84.10)","5.72 (min 4.84, max 6.15)"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "102400","9.60 (min 8.52, max 10.57)","2.45 (min 1.99, max 3.24)","10.84 (min 10.64, max 11.16)","2.81 (min 2.45, max 3.08)"
    "262144","9.45 (min 8.73, max 10.75)","2.46 (min 1.98, max 3.38)","10.99 (min 10.74, max 11.20)","2.35 (min 2.06, max 2.67)"
    "524288","9.52 (min 8.75, max 10.56)","2.42 (min 1.92, max 3.28)","11.13 (min 10.90, max 11.49)","2.10 (min 1.94, max 2.18)"
    "1048576","9.46 (min 8.86, max 10.52)","2.50 (min 1.96, max 3.77)","11.20 (min 11.08, max 11.38)","2.23 (min 2.01, max 2.66)"
    "5242880","9.53 (min 8.79, max 10.77)","2.38 (min 1.91, max 3.95)","11.46 (min 11.05, max 12.02)","2.23 (min 1.96, max 2.49)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62lxx_evm-fs: Write Throughput (Kbytes/sec)","am62lxx_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","17604.61 (min 12962.03, max 19692.31)","22714.58 (min 22505.49, max 22882.68)"
    "800000","20272.80 (min 18004.40, max 21501.31)","23152.29 (min 23076.06, max 23206.80)"
    "1000000","19450.02 (min 16015.64, max 21250.32)","23311.43 (min 23239.72, max 23339.03)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

USB Driver
----------
 
USB Device Controller
^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62lxx_evm-fs: Throughput (MB/sec)"

    "150","41.14 (min 36.20, max 43.50)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62lxx_evm-fs: Throughput (MB/sec)"

    "150","37.43 (min 31.00, max 41.40)"
