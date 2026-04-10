#################################
 Linux 12.00.00 Performance Guide
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

*****************
About This Manual
*****************

This document provides performance data for each of the device drivers
which are part of the Processor SDK Linux package. This document should be
used in conjunction with release notes and user guides provided with the
Processor SDK Linux package for information on specific issues present
with drivers included in a particular release.

For further information or to report any problems, contact
https://e2e.ti.com/ or https://support.ti.com/

|

*****************
System Benchmarks
*****************

|

LMBench
=======

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

    "af_unix_sock_stream_latency (microsec)","28.47 (min 25.57, max 29.86)"
    "af_unix_socket_stream_bandwidth (mb\s)","473.68 (min 441.13, max 551.95)"
    "bw_file_rd-io-1mb (mb/s)","952.82 (min 909.92, max 1066.29)"
    "bw_file_rd-o2c-1mb (mb/s)","391.04 (min 55.18, max 547.95)"
    "bw_mem-bcopy-16mb (mb/s)","749.66 (min 705.87, max 858.60)"
    "bw_mem-bcopy-1mb (mb/s)","769.84 (min 694.44, max 909.09)"
    "bw_mem-bcopy-2mb (mb/s)","752.70 (min 690.49, max 913.94)"
    "bw_mem-bcopy-4mb (mb/s)","775.04 (min 704.72, max 954.65)"
    "bw_mem-bcopy-8mb (mb/s)","809.57 (min 727.14, max 971.23)"
    "bw_mem-bzero-16mb (mb/s)","2279.05 (min 2106.37, max 2725.72)"
    "bw_mem-bzero-1mb (mb/s)","1526.26 (min 694.44, max 2725.29)"
    "bw_mem-bzero-2mb (mb/s)","1515.47 (min 690.49, max 2727.45)"
    "bw_mem-bzero-4mb (mb/s)","1526.69 (min 704.72, max 2724.33)"
    "bw_mem-bzero-8mb (mb/s)","1546.56 (min 727.14, max 2725.72)"
    "bw_mem-cp-16mb (mb/s)","426.86 (min 395.35, max 500.74)"
    "bw_mem-cp-1mb (mb/s)","1439.36 (min 395.41, max 2878.53)"
    "bw_mem-cp-2mb (mb/s)","1400.78 (min 386.25, max 2819.38)"
    "bw_mem-cp-4mb (mb/s)","1398.29 (min 434.36, max 2764.34)"
    "bw_mem-cp-8mb (mb/s)","1393.47 (min 432.85, max 2750.09)"
    "bw_mem-fcp-16mb (mb/s)","751.74 (min 710.38, max 853.20)"
    "bw_mem-fcp-1mb (mb/s)","1557.43 (min 776.04, max 2725.29)"
    "bw_mem-fcp-2mb (mb/s)","1551.17 (min 764.33, max 2727.45)"
    "bw_mem-fcp-4mb (mb/s)","1563.30 (min 790.28, max 2724.33)"
    "bw_mem-fcp-8mb (mb/s)","1574.04 (min 798.08, max 2725.72)"
    "bw_mem-frd-16mb (mb/s)","1329.96 (min 1253.62, max 1537.28)"
    "bw_mem-frd-1mb (mb/s)","1049.23 (min 776.04, max 1494.21)"
    "bw_mem-frd-2mb (mb/s)","1043.79 (min 764.33, max 1423.99)"
    "bw_mem-frd-4mb (mb/s)","1062.05 (min 790.28, max 1526.14)"
    "bw_mem-frd-8mb (mb/s)","1092.66 (min 798.08, max 1551.89)"
    "bw_mem-fwr-16mb (mb/s)","2295.38 (min 2122.02, max 2738.79)"
    "bw_mem-fwr-1mb (mb/s)","1857.24 (min 1178.25, max 2878.53)"
    "bw_mem-fwr-2mb (mb/s)","1819.10 (min 1196.53, max 2819.38)"
    "bw_mem-fwr-4mb (mb/s)","1803.17 (min 1166.35, max 2764.34)"
    "bw_mem-fwr-8mb (mb/s)","1816.38 (min 1237.43, max 2750.09)"
    "bw_mem-rd-16mb (mb/s)","1348.11 (min 1269.04, max 1574.80)"
    "bw_mem-rd-1mb (mb/s)","973.75 (min 532.67, max 1533.45)"
    "bw_mem-rd-2mb (mb/s)","954.80 (min 508.78, max 1548.95)"
    "bw_mem-rd-4mb (mb/s)","965.06 (min 582.16, max 1563.11)"
    "bw_mem-rd-8mb (mb/s)","1028.38 (min 671.03, max 1574.49)"
    "bw_mem-rdwr-16mb (mb/s)","742.83 (min 671.11, max 871.98)"
    "bw_mem-rdwr-1mb (mb/s)","507.25 (min 395.41, max 758.58)"
    "bw_mem-rdwr-2mb (mb/s)","508.60 (min 386.25, max 742.12)"
    "bw_mem-rdwr-4mb (mb/s)","554.93 (min 434.36, max 758.58)"
    "bw_mem-rdwr-8mb (mb/s)","594.72 (min 432.85, max 831.51)"
    "bw_mem-wr-16mb (mb/s)","761.79 (min 696.29, max 875.47)"
    "bw_mem-wr-1mb (mb/s)","597.49 (min 503.36, max 758.58)"
    "bw_mem-wr-2mb (mb/s)","580.37 (min 508.78, max 742.12)"
    "bw_mem-wr-4mb (mb/s)","649.66 (min 582.16, max 809.88)"
    "bw_mem-wr-8mb (mb/s)","712.22 (min 660.23, max 831.51)"
    "bw_mmap_rd-mo-1mb (mb/s)","1186.31 (min 1095.29, max 1369.06)"
    "bw_mmap_rd-o2c-1mb (mb/s)","504.63 (min 466.13, max 534.00)"
    "bw_pipe (mb/s)","397.94 (min 332.79, max 502.07)"
    "bw_unix (mb/s)","473.68 (min 441.13, max 551.95)"
    "lat_connect (us)","110.85 (min 108.39, max 113.45)"
    "lat_ctx-2-128k (us)","40.79 (min 10.02, max 53.07)"
    "lat_ctx-2-256k (us)","122.00 (min 19.85, max 160.05)"
    "lat_ctx-4-128k (us)","79.14 (min 11.48, max 104.99)"
    "lat_ctx-4-256k (us)","95.97 (min 8.50, max 179.58)"
    "lat_fs-0k (num_files)","203.25 (min 195.00, max 212.00)"
    "lat_fs-10k (num_files)","89.00 (min 81.00, max 96.00)"
    "lat_fs-1k (num_files)","134.25 (min 118.00, max 146.00)"
    "lat_fs-4k (num_files)","128.25 (min 120.00, max 136.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","49.87 (min 42.84, max 52.35)"
    "lat_mem_rd-stride128-sz125k (ns)","6.18 (min 6.17, max 6.18)"
    "lat_mem_rd-stride128-sz250k (ns)","11.22 (min 7.65, max 14.89)"
    "lat_mem_rd-stride128-sz31k (ns)","3.16 (min 2.41, max 3.90)"
    "lat_mem_rd-stride128-sz50 (ns)","2.41"
    "lat_mem_rd-stride128-sz500k (ns)","45.38 (min 39.37, max 47.67)"
    "lat_mem_rd-stride128-sz62k (ns)","5.74 (min 5.72, max 5.77)"
    "lat_mmap-1m (us)","65.00 (min 57.00, max 68.00)"
    "lat_ops-double-add (ns)","3.21"
    "lat_ops-double-div (ns)","17.66 (min 17.65, max 17.66)"
    "lat_ops-double-mul (ns)","3.21"
    "lat_ops-float-add (ns)","3.21"
    "lat_ops-float-div (ns)","10.44 (min 10.43, max 10.45)"
    "lat_ops-float-mul (ns)","3.21 (min 3.21, max 3.22)"
    "lat_ops-int-add (ns)","0.80"
    "lat_ops-int-bit (ns)","0.53"
    "lat_ops-int-div (ns)","4.82 (min 4.81, max 4.82)"
    "lat_ops-int-mod (ns)","5.08 (min 5.08, max 5.09)"
    "lat_ops-int-mul (ns)","3.49"
    "lat_ops-int64-add (ns)","0.80"
    "lat_ops-int64-bit (ns)","0.54 (min 0.53, max 0.54)"
    "lat_ops-int64-div (ns)","7.63 (min 7.62, max 7.63)"
    "lat_ops-int64-mod (ns)","5.89 (min 5.88, max 5.92)"
    "lat_ops-int64-mul (ns)","3.98 (min 3.97, max 3.99)"
    "lat_pagefault (us)","0.87 (min 0.77, max 0.93)"
    "lat_pipe (us)","22.18 (min 20.56, max 23.06)"
    "lat_proc-exec (us)","1469.13 (min 1298.00, max 1543.25)"
    "lat_proc-fork (us)","1296.60 (min 1160.40, max 1372.00)"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","35.38 (min 35.29, max 35.56)"
    "lat_sem (us)","3.55 (min 3.33, max 3.84)"
    "lat_sig-catch (us)","6.24 (min 6.16, max 6.34)"
    "lat_sig-install (us)","0.66 (min 0.65, max 0.70)"
    "lat_sig-prot (us)","0.95 (min 0.88, max 1.01)"
    "lat_syscall-fstat (us)","2.02 (min 1.97, max 2.12)"
    "lat_syscall-null (us)","0.42 (min 0.41, max 0.42)"
    "lat_syscall-open (us)","485.80 (min 413.85, max 568.44)"
    "lat_syscall-read (us)","0.83 (min 0.82, max 0.83)"
    "lat_syscall-stat (us)","4.74 (min 4.69, max 4.79)"
    "lat_syscall-write (us)","0.75"
    "lat_tcp (us)","0.86"
    "lat_unix (us)","28.47 (min 25.57, max 29.86)"
    "latency_for_0.50_mb_block_size (nanosec)","45.38 (min 39.37, max 47.67)"
    "latency_for_1.00_mb_block_size (nanosec)","22.16 (min 0.00, max 52.35)"
    "pipe_bandwidth (mb\s)","397.94 (min 332.79, max 502.07)"
    "pipe_latency (microsec)","22.18 (min 20.56, max 23.06)"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","35.38 (min 35.29, max 35.56)"
    "semaphore_latency (microsec)","3.55 (min 3.33, max 3.84)"
    "signal_handler_latency (microsec)","0.66 (min 0.65, max 0.70)"
    "signal_handler_overhead (microsec)","6.24 (min 6.16, max 6.34)"
    "tcp_ip_connection_cost_to_localhost (microsec)","110.85 (min 108.39, max 113.45)"
    "tcp_latency_using_localhost (microsec)","0.86"

Dhrystone
=========

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

    "cpu_clock (mhz)","1250.00"
    "dhrystone_per_mhz (dmips/mhz)","2.80"
    "dhrystone_per_second (dhrystonep)","6250000.00"

Whetstone
=========

Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

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

    "linpack (kflops)","516120.50 (min 514627.00, max 517614.00)"

NBench
======

NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "assignment (iterations)","12.64 (min 12.62, max 12.67)"
    "fourier (iterations)","18560.75 (min 18556.00, max 18568.00)"
    "fp_emulation (iterations)","182.43 (min 182.35, max 182.50)"
    "huffman (iterations)","1063.13 (min 1063.00, max 1063.20)"
    "idea (iterations)","2738.40 (min 2738.10, max 2738.60)"
    "lu_decomposition (iterations)","473.09 (min 467.17, max 475.75)"
    "neural_net (iterations)","8.63 (min 8.59, max 8.64)"
    "numeric_sort (iterations)","483.39 (min 482.54, max 484.16)"
    "string_sort (iterations)","150.19 (min 150.17, max 150.21)"

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

::

    stream_c

.. csv-table:: Stream Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "add (mb/s)","1523.87 (min 1498.10, max 1538.30)"
    "copy (mb/s)","1629.27 (min 1610.40, max 1639.00)"
    "scale (mb/s)","1672.47 (min 1632.10, max 1713.80)"
    "triad (mb/s)","1512.27 (min 1488.30, max 1526.00)"

CoreMarkPro
===========

CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","37.22 (min 37.04, max 37.31)"
    "core (workloads/)","0.27"
    "coremark-pro ()","719.19 (min 697.16, max 733.93)"
    "linear_alg-mid-100x100-sp (workloads/)","13.08"
    "loops-all-mid-10k-sp (workloads/)","0.59 (min 0.56, max 0.60)"
    "nnet_test (workloads/)","0.96"
    "parser-125k (workloads/)","7.62 (min 7.04, max 8.06)"
    "radix2-big-64k (workloads/)","19.26 (min 16.30, max 21.85)"
    "sha-test (workloads/)","71.11 (min 69.44, max 72.46)"
    "zip-test (workloads/)","19.04 (min 17.86, max 20.41)"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","72.20 (min 71.94, max 72.46)"
    "core (workloads/)","0.53 (min 0.53, max 0.54)"
    "coremark-pro ()","1209.22 (min 1186.40, max 1232.04)"
    "linear_alg-mid-100x100-sp (workloads/)","26.04 (min 26.03, max 26.06)"
    "loops-all-mid-10k-sp (workloads/)","0.99 (min 0.98, max 1.00)"
    "nnet_test (workloads/)","1.91 (min 1.91, max 1.92)"
    "parser-125k (workloads/)","7.61 (min 5.97, max 9.26)"
    "radix2-big-64k (workloads/)","24.15 (min 23.08, max 25.21)"
    "sha-test (workloads/)","137.01 (min 135.14, max 138.89)"
    "zip-test (workloads/)","33.37 (min 32.26, max 34.48)"

MultiBench
==========

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

    "4m-check (workloads/)","287.19 (min 265.48, max 320.97)"
    "4m-check-reassembly (workloads/)","66.74 (min 51.05, max 83.26)"
    "4m-check-reassembly-tcp (workloads/)","41.39 (min 33.69, max 47.80)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","16.75 (min 15.29, max 18.62)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","0.87 (min 0.78, max 0.95)"
    "4m-cmykw2 (workloads/)","107.63 (min 106.10, max 110.01)"
    "4m-cmykw2-rotatew2 (workloads/)","22.14 (min 18.79, max 26.33)"
    "4m-reassembly (workloads/)","74.80 (min 47.60, max 98.62)"
    "4m-rotatew2 (workloads/)","24.65 (min 19.73, max 28.48)"
    "4m-tcp-mixed (workloads/)","102.76 (min 98.16, max 108.84)"
    "4m-x264w2 (workloads/)","0.93 (min 0.92, max 0.96)"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","17.23 (min 16.47, max 17.62)"
    "idct-4mw1 (workloads/)","17.23 (min 16.48, max 17.62)"
    "ippktcheck-4m (workloads/)","288.80 (min 267.09, max 323.63)"
    "ippktcheck-4mw1 (workloads/)","288.26 (min 265.73, max 323.71)"
    "ipres-4m (workloads/)","67.60 (min 60.10, max 78.25)"
    "ipres-4mw1 (workloads/)","67.64 (min 59.78, max 78.21)"
    "md5-4m (workloads/)","19.49 (min 18.37, max 20.95)"
    "md5-4mw1 (workloads/)","19.53 (min 18.49, max 21.01)"
    "rgbcmyk-4m (workloads/)","57.07 (min 56.69, max 57.47)"
    "rgbcmyk-4mw1 (workloads/)","57.04 (min 56.64, max 57.29)"
    "rotate-4ms1 (workloads/)","20.24 (min 17.49, max 23.21)"
    "rotate-4ms1w1 (workloads/)","20.27 (min 17.48, max 23.20)"
    "rotate-4ms64 (workloads/)","20.37 (min 17.64, max 23.22)"
    "rotate-4ms64w1 (workloads/)","20.36 (min 17.62, max 23.29)"
    "x264-4mq (workloads/)","0.50 (min 0.50, max 0.51)"
    "x264-4mqw1 (workloads/)","0.50 (min 0.49, max 0.51)"

|

Boot-time Measurement
=====================

Boot media: MMCSD
-----------------

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62lxx_evm-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","21.87 (min 19.45, max 24.14)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

ALSA SoC Audio Driver
=====================

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62lxx_evm-fs: Throughput (bits/sec)","am62lxx_evm-fs: CPU Load (%)"

    "11025","352795.00 (min 352794.00, max 352796.00)","0.36 (min 0.29, max 0.42)"
    "16000","511994.00","0.37 (min 0.31, max 0.42)"
    "22050","705588.00 (min 705587.00, max 705589.00)","0.36 (min 0.35, max 0.36)"
    "24000","705590.00 (min 705589.00, max 705591.00)","0.38 (min 0.36, max 0.40)"
    "32000","1023985.50 (min 1023984.00, max 1023987.00)","0.22 (min 0.21, max 0.23)"
    "44100","1411180.00 (min 1411179.00, max 1411181.00)","0.54 (min 0.53, max 0.54)"
    "48000","1535978.50 (min 1535977.00, max 1535980.00)","0.59 (min 0.19, max 0.99)"
    "88200","2822351.50 (min 2822349.00, max 2822354.00)","0.83 (min 0.81, max 0.84)"
    "96000","3071928.50 (min 3071926.00, max 3071931.00)","1.18 (min 0.39, max 1.96)"

.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62lxx_evm-fs: Throughput (bits/sec)","am62lxx_evm-fs: CPU Load (%)"

    "11025","352943.67 (min 352943.00, max 352944.00)","0.45 (min 0.31, max 0.63)"
    "16000","512209.00 (min 512208.00, max 512210.00)","0.33 (min 0.22, max 0.46)"
    "22050","705886.67 (min 705885.00, max 705890.00)","0.36 (min 0.30, max 0.48)"
    "24000","705888.00 (min 705887.00, max 705890.00)","0.42 (min 0.36, max 0.53)"
    "32000","1024417.67 (min 1024416.00, max 1024420.00)","0.54 (min 0.24, max 1.00)"
    "44100","1411774.67 (min 1411772.00, max 1411778.00)","0.52 (min 0.42, max 0.67)"
    "48000","1536624.67 (min 1536622.00, max 1536628.00)","0.48 (min 0.33, max 0.77)"
    "88200","2823538.00 (min 2823532.00, max 2823546.00)","0.74 (min 0.62, max 0.91)"
    "96000","3073210.00 (min 3073190.00, max 3073224.00)","0.48 (min 0.37, max 0.55)"

|

Ethernet
========

Ethernet performance benchmarks were measured using :command:`netperf` 2.7.1 https://hewlettpackard.github.io/netperf/doc/netperf.html
Test procedures were modeled after those defined in RFC-2544:
https://tools.ietf.org/html/rfc2544, where the DUT is the TI device
and the "tester" used was a Linux PC. To produce consistent results,
it is recommended to carry out performance tests in a private network and to avoid
running NFS on the same interface used in the test. In these results,
CPU utilization was captured as the total percentage used across all cores on the device,
while running the performance test over one external interface.

UDP Throughput (0% loss) was measured by the procedure defined in RFC-2544 section 26.1: Throughput.
In this scenario, :command:`netperf` options burst_size (-b) and wait_time (-w) are used to limit bandwidth
during different trials of the test, with the goal of finding the highest rate at which
no loss is seen. For example, to limit bandwidth to 500Mbits/sec with 1472B datagram:

.. code-block:: console

   burst_size = <bandwidth (bits/sec)> / 8 (bits -> bytes) / <UDP datagram size> / 100 (seconds -> 10 ms)
   burst_size = 500000000 / 8 / 1472 / 100 = 425

   wait_time = 10 milliseconds (minimum supported by Linux PC used for testing)

UDP Throughput (possible loss) was measured by capturing throughput and packet loss statistics when
running the :command:`netperf` test with no bandwidth limit (remove -b/-w options).

In order to start a :command:`netperf` client on one device, the other device must have :command:`netserver` running.
To start :command:`netserver`:

.. code-block:: console

   netserver [-p <port_number>] [-4 (IPv4 addressing)] [-6 (IPv6 addressing)]

Running the following shell script from the DUT will trigger :command:`netperf` clients to measure
bidirectional TCP performance for 60 seconds and report CPU utilization. Parameter -k is used in
client commands to summarize selected statistics on their own line and -j is used to gain
additional timing measurements during the test.

.. code-block:: console

   #!/bin/bash
   for i in 1
   do
      netperf -H <tester ip> -j -c -l 60 -t TCP_STREAM --
         -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE &

      netperf -H <tester ip> -j -c -l 60 -t TCP_MAERTS --
         -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE &
   done

Running the following commands will trigger :command:`netperf` clients to measure UDP burst performance for
60 seconds at various burst/datagram sizes and report CPU utilization.

- For UDP egress tests, run :command:`netperf` client from DUT and start :command:`netserver` on tester.

.. code-block:: console

   netperf -H <tester ip> -j -c -l 60 -t UDP_STREAM -b <burst_size> -w <wait_time> -- -m <UDP datagram size>
      -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE

- For UDP ingress tests, run :command:`netperf` client from tester and start :command:`netserver` on DUT.

.. code-block:: console

   netperf -H <DUT ip> -j -C -l 60 -t UDP_STREAM -b <burst_size> -w <wait_time> -- -m <UDP datagram size>
      -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE

CPSW/CPSW2g/CPSW3g Ethernet
---------------------------

TCP Bidirectional Throughput
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1048.02 (min 1035.65, max 1060.38)","99.10 (min 98.47, max 99.72)"

TCP Bidirectional Throughput Interrupt Pacing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1182.95 (min 1179.68, max 1186.21)","95.50 (min 95.39, max 95.60)"

UDP Throughput
^^^^^^^^^^^^^^

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62lxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: Packets Per Second (kPPS)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","36.89 (min 36.82, max 36.96)","72.00","75.48 (min 75.29, max 75.67)"
    "128","","80.20","78.00","77.85"
    "256","","145.24","71.00","75.58"
    "1024","","355.15 (min 137.62, max 572.68)","43.50 (min 17.00, max 70.00)","49.89 (min 24.19, max 75.58)"
    "1518","","623.50 (min 619.61, max 627.38)","51.50 (min 51.00, max 52.00)","72.61 (min 71.63, max 73.58)"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62lxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: Packets Per Second (kPPS)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","1.54 (min 1.48, max 1.59)","3.00","1.97 (min 1.84, max 2.10)"
    "128","","4.46 (min 4.40, max 4.51)","4.00","3.70 (min 2.67, max 4.73)"
    "256","","10.14 (min 10.04, max 10.24)","5.00","3.06 (min 3.00, max 3.11)"
    "1024","","42.19 (min 41.78, max 42.60)","5.00","3.49 (min 3.40, max 3.57)"
    "1518","","34.74 (min 8.24, max 61.23)","3.00 (min 1.00, max 5.00)","3.65 (min 1.02, max 6.27)"

.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62lxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: Packets Per Second (kPPS)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","am62lxx_evm-fs: Packet Loss %"

    "64","","47.26 (min 46.91, max 47.61)","92.50 (min 92.00, max 93.00)","65.65 (min 64.95, max 66.34)","79.50 (min 79.03, max 79.97)"
    "128","","89.46 (min 88.85, max 90.07)","87.50 (min 87.00, max 88.00)","67.22 (min 67.01, max 67.42)","83.49 (min 80.73, max 86.25)"
    "256","","187.89 (min 178.98, max 196.80)","91.50 (min 87.00, max 96.00)","67.38 (min 65.87, max 68.89)","55.23 (min 51.03, max 59.42)"
    "1024","","590.71 (min 544.95, max 636.47)","72.50 (min 67.00, max 78.00)","74.71 (min 70.00, max 79.41)","21.13 (min 16.49, max 25.77)"
    "1518","","784.17 (min 775.84, max 792.50)","66.50 (min 66.00, max 67.00)","76.55 (min 75.73, max 77.37)","14.76 (min 12.32, max 17.20)"

|

EMMC
====

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

EMMC EXT4 FIO 1G
----------------

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

    "1m","128.33 (min 128.00, max 129.00)","8.92 (min 8.60, max 9.20)","179.33 (min 179.00, max 180.00)","7.83 (min 7.36, max 8.35)"
    "4m","128.67 (min 128.00, max 129.00)","5.52 (min 5.34, max 5.80)","179.33 (min 179.00, max 180.00)","5.08 (min 4.98, max 5.22)"
    "4k","87.67 (min 86.30, max 88.60)","57.12 (min 56.47, max 57.84)","93.83 (min 90.80, max 97.50)","55.19 (min 54.00, max 57.17)"
    "256k","123.00","12.30 (min 11.83, max 13.08)","177.67 (min 175.00, max 179.00)","10.40 (min 9.43, max 11.55)"

EMMC EXT4
---------

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

    "102400","104.84 (min 95.48, max 108.41)","15.02 (min 13.33, max 20.00)","175.11 (min 158.41, max 183.74)","29.09 (min 25.19, max 33.64)"
    "262144","106.77 (min 100.69, max 110.53)","12.13 (min 10.05, max 16.93)","185.91 (min 185.64, max 186.39)","27.61 (min 25.00, max 31.48)"
    "524288","106.64 (min 99.47, max 110.24)","12.17 (min 9.74, max 15.57)","186.99 (min 186.68, max 187.16)","23.49 (min 20.91, max 25.00)"
    "1048576","106.92 (min 102.07, max 109.98)","11.92 (min 10.26, max 15.71)","187.10 (min 187.05, max 187.17)","23.32 (min 22.22, max 24.11)"
    "5242880","107.71 (min 100.42, max 111.86)","12.14 (min 10.47, max 15.05)","187.16 (min 187.07, max 187.23)","23.25 (min 22.73, max 24.07)"

EMMC VFAT
---------

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write VFAT Throughput (Mbytes/sec)","am62lxx_evm-fs: Write VFAT CPU Load (%)","am62lxx_evm-fs: Read VFAT Throughput (Mbytes/sec)","am62lxx_evm-fs: Read VFAT CPU Load (%)"

    "102400","32.78 (min 16.04, max 37.19)","15.45 (min 12.96, max 20.27)","174.45 (min 173.98, max 175.01)","39.26 (min 36.52, max 43.97)"
    "262144","47.10 (min 19.77, max 59.67)","18.04 (min 14.56, max 21.99)","175.94 (min 175.78, max 176.17)","36.81 (min 34.51, max 38.94)"
    "524288","55.87 (min 21.16, max 65.96)","18.69 (min 15.92, max 25.61)","177.09 (min 176.63, max 177.56)","32.66 (min 31.03, max 34.19)"
    "1048576","61.77 (min 22.07, max 76.62)","19.90 (min 18.12, max 22.93)","175.57 (min 174.58, max 177.21)","35.72 (min 33.04, max 40.52)"
    "5242880","71.75 (min 23.10, max 85.16)","21.11 (min 19.44, max 22.40)","176.47 (min 176.20, max 176.65)","33.14 (min 32.48, max 34.45)"

UBoot EMMC
----------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62lxx_evm-fs: Write Throughput (Kbytes/sec)","am62lxx_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","111077.97","175229.95"
    "4000000","124830.48","178086.96"

MMCSD
=====

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

MMC EXT4 FIO 1G
---------------

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

    "1m","42.60 (min 42.20, max 43.00)","4.13 (min 3.97, max 4.29)","86.40 (min 85.50, max 87.30)","5.47 (min 5.44, max 5.50)"
    "4m","41.50 (min 40.30, max 42.70)","2.71 (min 2.63, max 2.78)","86.10 (min 84.70, max 87.50)","3.13 (min 3.12, max 3.14)"
    "4k","2.86 (min 2.84, max 2.89)","7.03 (min 6.58, max 7.47)","12.95 (min 12.90, max 13.00)","12.01 (min 11.69, max 12.32)"
    "256k","39.40 (min 38.90, max 39.90)","5.83 (min 5.38, max 6.28)","83.85 (min 83.70, max 84.00)","6.30 (min 6.26, max 6.34)"

MMC EXT4
--------

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "102400","10.74 (min 10.57, max 10.92)","1.53 (min 1.20, max 2.08)","10.92 (min 10.64, max 11.08)","2.10 (min 1.85, max 2.37)"
    "262144","10.70 (min 10.25, max 11.01)","1.52 (min 1.11, max 2.42)","11.12 (min 10.99, max 11.19)","1.63 (min 1.34, max 1.83)"
    "524288","10.74 (min 10.42, max 10.96)","1.33 (min 1.04, max 1.80)","11.36 (min 11.06, max 11.52)","1.34 (min 1.32, max 1.38)"
    "1048576","10.83 (min 10.22, max 11.21)","1.42 (min 0.94, max 2.00)","11.50 (min 11.02, max 12.02)","1.36 (min 1.16, max 1.55)"
    "5242880","10.93 (min 10.69, max 11.19)","1.29 (min 0.92, max 2.16)","12.01 (min 11.99, max 12.02)","1.49 (min 1.32, max 1.61)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62lxx_evm-fs: Write Throughput (Kbytes/sec)","am62lxx_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","28068.99 (min 10422.39, max 39009.52)","63923.25 (min 11636.36, max 83591.84)"
    "800000","35679.64 (min 10908.12, max 49053.89)","67640.33 (min 11719.60, max 88086.02)"
    "1000000","36338.73 (min 11033.00, max 47489.86)","69037.04 (min 11744.80, max 90021.98)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

USB
===

USB Device Controller
---------------------

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62lxx_evm-fs: Throughput (MB/sec)"

    "150","37.55 (min 36.00, max 40.60)"


.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62lxx_evm-fs: Throughput (MB/sec)"

    "150","31.63 (min 31.20, max 32.20)"

|

CRYPTO
======

OpenSSL Performance
-------------------

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62lxx_evm-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","820153.17 (min 819911.34, max 820533.93)"
    "aes-128-cbc","16","88945.15 (min 88836.08, max 89002.73)"
    "aes-128-cbc","16384","939063.98 (min 937519.79, max 940032.00)"
    "aes-128-cbc","256","581491.09 (min 581083.82, max 581764.44)"
    "aes-128-cbc","64","277695.28 (min 277243.09, max 278112.00)"
    "aes-128-cbc","8192","930250.75 (min 929565.35, max 930660.35)"
    "aes-128-ecb","1024","899457.71 (min 896871.42, max 901688.66)"
    "aes-128-ecb","16","94404.48 (min 92735.88, max 95448.03)"
    "aes-128-ecb","16384","1068426.58 (min 1067881.81, max 1068979.54)"
    "aes-128-ecb","256","594218.41 (min 589874.01, max 597775.02)"
    "aes-128-ecb","64","259665.47 (min 256530.28, max 261640.53)"
    "aes-128-ecb","8192","1056195.93 (min 1055719.42, max 1057030.14)"
    "aes-192-cbc","1024","635496.19 (min 634212.01, max 636192.09)"
    "aes-192-cbc","16","84958.61 (min 83445.07, max 85605.02)"
    "aes-192-cbc","16384","704898.39 (min 702851.75, max 706418.01)"
    "aes-192-cbc","256","480254.10 (min 477063.59, max 481556.39)"
    "aes-192-cbc","64","250222.52 (min 246972.93, max 251633.17)"
    "aes-192-cbc","8192","701138.94 (min 700844.71, max 701322.58)"
    "aes-192-ecb","1024","796659.71 (min 794786.82, max 797450.58)"
    "aes-192-ecb","16","90855.18 (min 89027.61, max 91505.64)"
    "aes-192-ecb","16384","929252.69 (min 928235.52, max 929824.77)"
    "aes-192-ecb","256","544550.23 (min 540975.10, max 546148.27)"
    "aes-192-ecb","64","245857.87 (min 242240.04, max 247096.23)"
    "aes-192-ecb","8192","919371.09 (min 918964.91, max 919639.38)"
    "aes-256-cbc","1024","533614.59 (min 532546.56, max 534222.85)"
    "aes-256-cbc","16","82838.72 (min 81336.68, max 83377.88)"
    "aes-256-cbc","16384","582748.84 (min 582489.43, max 582909.95)"
    "aes-256-cbc","256","419748.05 (min 417439.23, max 420707.93)"
    "aes-256-cbc","64","232853.02 (min 229933.29, max 233899.99)"
    "aes-256-cbc","8192","579334.14 (min 579215.36, max 579499.35)"
    "aes-256-ecb","1024","709590.02 (min 708103.51, max 710752.26)"
    "aes-256-ecb","16","87171.66 (min 86051.96, max 88241.35)"
    "aes-256-ecb","16384","813151.57 (min 812346.03, max 814159.19)"
    "aes-256-ecb","256","488434.03 (min 485834.50, max 490525.18)"
    "aes-256-ecb","64","232332.60 (min 230068.37, max 234072.00)"
    "aes-256-ecb","8192","801607.00 (min 801270.44, max 802234.37)"
    "des3","1024","4550.06 (min 4524.03, max 4562.26)"
    "des3","16","4316.02 (min 4306.80, max 4319.40)"
    "des3","16384","4564.31 (min 4560.21, max 4565.67)"
    "des3","256","4548.33 (min 4545.19, max 4549.89)"
    "des3","64","4497.16 (min 4490.35, max 4499.69)"
    "des3","8192","4557.48 (min 4546.56, max 4565.67)"
    "md5","1024","144407.38 (min 144327.00, max 144474.79)"
    "md5","16","10784.95 (min 10761.82, max 10811.65)"
    "md5","16384","179810.30 (min 179754.33, max 179869.01)"
    "md5","256","88550.12 (min 88464.73, max 88638.55)"
    "md5","64","34590.38 (min 34213.35, max 34737.00)"
    "md5","8192","175732.74 (min 171794.43, max 177081.00)"
    "sha1","1024","332384.51 (min 329384.28, max 333542.74)"
    "sha1","16","12155.34 (min 12111.18, max 12188.26)"
    "sha1","16384","557408.26 (min 555111.77, max 558410.41)"
    "sha1","256","146047.32 (min 145553.07, max 146227.97)"
    "sha1","64","44891.43 (min 44686.68, max 44967.42)"
    "sha1","8192","534735.53 (min 533981.87, max 535374.51)"
    "sha224","1024","319523.93 (min 317158.06, max 320510.98)"
    "sha224","16","11875.43 (min 11692.84, max 11952.49)"
    "sha224","16384","528467.29 (min 527777.79, max 529017.51)"
    "sha224","256","141599.27 (min 139762.60, max 142371.58)"
    "sha224","64","43810.79 (min 43110.55, max 44092.07)"
    "sha224","8192","506508.63 (min 506161.83, max 507008.34)"
    "sha256","1024","316993.96 (min 315484.84, max 318002.86)"
    "sha256","16","11887.42 (min 11801.78, max 11934.95)"
    "sha256","16384","528214.70 (min 527750.49, max 528438.61)"
    "sha256","256","139981.29 (min 139145.39, max 140377.69)"
    "sha256","64","43094.56 (min 42625.62, max 43298.41)"
    "sha256","8192","505567.23 (min 504321.37, max 506585.09)"
    "sha512","1024","99841.62 (min 99679.91, max 99963.90)"
    "sha512","16","6977.87 (min 6945.17, max 7007.74)"
    "sha512","16384","126693.38 (min 126621.01, max 126795.78)"
    "sha512","256","59556.44 (min 59256.32, max 59719.51)"
    "sha512","64","27937.12 (min 27885.93, max 28021.01)"
    "sha512","8192","124555.95 (min 124523.86, max 124630.36)"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62lxx_evm-fs: CPU Load"

    "aes-128-cbc","98.75 (min 98.00, max 99.00)"
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
    "sha386","81.00 (min 78.00, max 85.00)"
    "sha512","96.75 (min 90.00, max 99.00)"

Listed for each algorithm are the code snippets used to run each
benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc

|
