
===================================
Linux 12.00.00 Performance Guide
===================================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","27.25 (min 23.37, max 31.39)"
    "af_unix_socket_stream_bandwidth (mb\s)","1098.87 (min 1064.86, max 1145.16)"
    "bw_file_rd-io-1mb (mb/s)","1297.39 (min 1250.45, max 1353.70)"
    "bw_file_rd-o2c-1mb (mb/s)","698.21 (min 626.27, max 743.36)"
    "bw_mem-bcopy-16mb (mb/s)","1819.35 (min 1787.11, max 1858.30)"
    "bw_mem-bcopy-1mb (mb/s)","1968.82 (min 1926.11, max 2020.20)"
    "bw_mem-bcopy-2mb (mb/s)","1636.56 (min 1562.99, max 1757.47)"
    "bw_mem-bcopy-4mb (mb/s)","1760.75 (min 1715.76, max 1810.50)"
    "bw_mem-bcopy-8mb (mb/s)","1783.97 (min 1721.36, max 1831.92)"
    "bw_mem-bzero-16mb (mb/s)","7382.69 (min 7082.78, max 7846.98)"
    "bw_mem-bzero-1mb (mb/s)","4669.86 (min 1926.11, max 7834.89)"
    "bw_mem-bzero-2mb (mb/s)","4501.42 (min 1562.99, max 7834.76)"
    "bw_mem-bzero-4mb (mb/s)","4568.55 (min 1715.76, max 7836.15)"
    "bw_mem-bzero-8mb (mb/s)","4584.74 (min 1721.36, max 7857.26)"
    "bw_mem-cp-16mb (mb/s)","900.30 (min 885.79, max 917.43)"
    "bw_mem-cp-1mb (mb/s)","4257.87 (min 872.75, max 8091.21)"
    "bw_mem-cp-2mb (mb/s)","4187.65 (min 858.86, max 7981.14)"
    "bw_mem-cp-4mb (mb/s)","4183.31 (min 906.00, max 7906.56)"
    "bw_mem-cp-8mb (mb/s)","4182.61 (min 932.73, max 7880.48)"
    "bw_mem-fcp-16mb (mb/s)","1699.60 (min 1673.12, max 1742.16)"
    "bw_mem-fcp-1mb (mb/s)","4518.12 (min 1637.85, max 7834.89)"
    "bw_mem-fcp-2mb (mb/s)","4484.17 (min 1506.70, max 7834.76)"
    "bw_mem-fcp-4mb (mb/s)","4516.30 (min 1596.17, max 7836.15)"
    "bw_mem-fcp-8mb (mb/s)","4531.23 (min 1649.14, max 7857.26)"
    "bw_mem-frd-16mb (mb/s)","1782.34 (min 1669.45, max 1859.82)"
    "bw_mem-frd-1mb (mb/s)","1757.90 (min 1637.85, max 1979.84)"
    "bw_mem-frd-2mb (mb/s)","1652.86 (min 1506.70, max 1781.58)"
    "bw_mem-frd-4mb (mb/s)","1699.36 (min 1596.17, max 1833.74)"
    "bw_mem-frd-8mb (mb/s)","1717.18 (min 1624.20, max 1853.14)"
    "bw_mem-fwr-16mb (mb/s)","7398.31 (min 7099.54, max 7855.97)"
    "bw_mem-fwr-1mb (mb/s)","4739.74 (min 1767.92, max 8091.21)"
    "bw_mem-fwr-2mb (mb/s)","4599.47 (min 1652.07, max 7981.14)"
    "bw_mem-fwr-4mb (mb/s)","4594.96 (min 1597.02, max 7906.56)"
    "bw_mem-fwr-8mb (mb/s)","4588.07 (min 1624.20, max 7880.48)"
    "bw_mem-rd-16mb (mb/s)","1879.38 (min 1823.36, max 1934.00)"
    "bw_mem-rd-1mb (mb/s)","1948.25 (min 1650.77, max 2211.57)"
    "bw_mem-rd-2mb (mb/s)","1700.50 (min 1484.56, max 1916.32)"
    "bw_mem-rd-4mb (mb/s)","1771.38 (min 1632.43, max 1932.99)"
    "bw_mem-rd-8mb (mb/s)","1808.54 (min 1708.12, max 1918.93)"
    "bw_mem-rdwr-16mb (mb/s)","1812.20 (min 1768.15, max 1847.36)"
    "bw_mem-rdwr-1mb (mb/s)","1279.41 (min 872.75, max 1768.97)"
    "bw_mem-rdwr-2mb (mb/s)","1176.63 (min 858.86, max 1505.57)"
    "bw_mem-rdwr-4mb (mb/s)","1258.98 (min 906.00, max 1676.45)"
    "bw_mem-rdwr-8mb (mb/s)","1349.98 (min 932.73, max 1789.91)"
    "bw_mem-wr-16mb (mb/s)","1789.42 (min 1731.98, max 1835.07)"
    "bw_mem-wr-1mb (mb/s)","1704.44 (min 1634.58, max 1887.44)"
    "bw_mem-wr-2mb (mb/s)","1505.81 (min 1451.12, max 1630.99)"
    "bw_mem-wr-4mb (mb/s)","1634.87 (min 1510.95, max 1731.85)"
    "bw_mem-wr-8mb (mb/s)","1748.27 (min 1703.76, max 1789.91)"
    "bw_mmap_rd-mo-1mb (mb/s)","2006.64 (min 1947.10, max 2076.84)"
    "bw_mmap_rd-o2c-1mb (mb/s)","705.96 (min 677.62, max 734.75)"
    "bw_pipe (mb/s)","754.85 (min 721.80, max 814.87)"
    "bw_unix (mb/s)","1098.87 (min 1064.86, max 1145.16)"
    "lat_connect (us)","68.66 (min 51.27, max 81.66)"
    "lat_ctx-2-128k (us)","9.35 (min 8.02, max 10.68)"
    "lat_ctx-2-256k (us)","24.48 (min 8.17, max 45.71)"
    "lat_ctx-4-128k (us)","17.09 (min 8.06, max 30.58)"
    "lat_ctx-4-256k (us)","43.70 (min 7.31, max 102.29)"
    "lat_fs-0k (num_files)","259.00 (min 207.00, max 308.00)"
    "lat_fs-10k (num_files)","121.40 (min 101.00, max 154.00)"
    "lat_fs-1k (num_files)","175.80 (min 163.00, max 196.00)"
    "lat_fs-4k (num_files)","168.20 (min 150.00, max 183.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","31.90 (min 31.10, max 32.39)"
    "lat_mem_rd-stride128-sz125k (ns)","5.96 (min 5.53, max 6.23)"
    "lat_mem_rd-stride128-sz250k (ns)","6.26 (min 5.83, max 6.54)"
    "lat_mem_rd-stride128-sz31k (ns)","2.72 (min 2.16, max 4.19)"
    "lat_mem_rd-stride128-sz50 (ns)","2.30 (min 2.15, max 2.40)"
    "lat_mem_rd-stride128-sz500k (ns)","12.15 (min 11.18, max 12.90)"
    "lat_mem_rd-stride128-sz62k (ns)","5.61 (min 5.23, max 5.88)"
    "lat_mmap-1m (us)","57.20 (min 56.00, max 62.00)"
    "lat_ops-double-add (ns)","3.07 (min 2.86, max 3.21)"
    "lat_ops-double-div (ns)","16.88 (min 15.75, max 17.64)"
    "lat_ops-double-mul (ns)","3.07 (min 2.86, max 3.21)"
    "lat_ops-float-add (ns)","3.07 (min 2.86, max 3.21)"
    "lat_ops-float-div (ns)","10.02 (min 9.30, max 10.64)"
    "lat_ops-float-mul (ns)","3.07 (min 2.86, max 3.22)"
    "lat_ops-int-add (ns)","0.77 (min 0.72, max 0.80)"
    "lat_ops-int-bit (ns)","0.51 (min 0.48, max 0.53)"
    "lat_ops-int-div (ns)","4.60 (min 4.29, max 4.81)"
    "lat_ops-int-mod (ns)","4.86 (min 4.53, max 5.08)"
    "lat_ops-int-mul (ns)","3.33 (min 3.05, max 3.49)"
    "lat_ops-int64-add (ns)","0.77 (min 0.72, max 0.80)"
    "lat_ops-int64-bit (ns)","0.51 (min 0.48, max 0.53)"
    "lat_ops-int64-div (ns)","7.29 (min 6.80, max 7.62)"
    "lat_ops-int64-mod (ns)","5.63 (min 5.25, max 5.88)"
    "lat_ops-int64-mul (ns)","3.82 (min 3.54, max 4.07)"
    "lat_pagefault (us)","0.47 (min 0.45, max 0.48)"
    "lat_pipe (us)","22.97 (min 21.04, max 24.59)"
    "lat_proc-exec (us)","746.80 (min 706.88, max 781.00)"
    "lat_proc-fork (us)","652.35 (min 620.22, max 681.50)"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","33.85 (min 31.32, max 35.89)"
    "lat_sem (us)","2.83 (min 2.58, max 3.13)"
    "lat_sig-catch (us)","6.03 (min 5.51, max 6.37)"
    "lat_sig-install (us)","0.69 (min 0.58, max 0.80)"
    "lat_sig-prot (us)","0.90 (min 0.80, max 0.97)"
    "lat_syscall-fstat (us)","1.93 (min 1.74, max 2.10)"
    "lat_syscall-null (us)","0.45 (min 0.37, max 0.56)"
    "lat_syscall-open (us)","222.92 (min 145.19, max 448.21)"
    "lat_syscall-read (us)","0.80 (min 0.74, max 0.86)"
    "lat_syscall-stat (us)","4.42 (min 3.96, max 4.79)"
    "lat_syscall-write (us)","0.75 (min 0.67, max 0.82)"
    "lat_tcp (us)","0.92 (min 0.76, max 1.14)"
    "lat_unix (us)","27.25 (min 23.37, max 31.39)"
    "latency_for_0.50_mb_block_size (nanosec)","12.15 (min 11.18, max 12.90)"
    "latency_for_1.00_mb_block_size (nanosec)","15.95 (min 0.00, max 32.39)"
    "pipe_bandwidth (mb\s)","754.85 (min 721.80, max 814.87)"
    "pipe_latency (microsec)","22.97 (min 21.04, max 24.59)"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","33.85 (min 31.32, max 35.89)"
    "semaphore_latency (microsec)","2.83 (min 2.58, max 3.13)"
    "signal_handler_latency (microsec)","0.69 (min 0.58, max 0.80)"
    "signal_handler_overhead (microsec)","6.03 (min 5.51, max 6.37)"
    "tcp_ip_connection_cost_to_localhost (microsec)","68.66 (min 51.27, max 81.66)"
    "tcp_latency_using_localhost (microsec)","0.92 (min 0.76, max 1.14)"

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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cpu_clock (mhz)","1310.00 (min 1250.00, max 1400.00)"
    "dhrystone_per_mhz (dmips/mhz)","2.76 (min 2.70, max 2.80)"
    "dhrystone_per_second (dhrystonep)","6323683.00 (min 5882353.00, max 6896551.50)"

Whetstone
^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "whetstone (mips)","5000.00"

Linpack
^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "linpack (kflops)","559402.33 (min 518395.00, max 580053.00)"

NBench
^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "assignment (iterations)","13.25 (min 12.62, max 14.16)"
    "fourier (iterations)","19455.60 (min 18561.00, max 20791.00)"
    "fp_emulation (iterations)","191.26 (min 182.55, max 204.44)"
    "huffman (iterations)","1111.14 (min 1063.00, max 1190.80)"
    "idea (iterations)","2869.98 (min 2738.50, max 3067.40)"
    "lu_decomposition (iterations)","496.24 (min 469.90, max 532.70)"
    "neural_net (iterations)","9.03 (min 8.64, max 9.68)"
    "numeric_sort (iterations)","506.05 (min 479.67, max 542.75)"
    "string_sort (iterations)","157.42 (min 150.17, max 168.31)"

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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "add (mb/s)","2595.38 (min 2519.20, max 2715.50)"
    "copy (mb/s)","3692.72 (min 3632.10, max 3761.80)"
    "scale (mb/s)","3369.20 (min 3233.70, max 3519.80)"
    "triad (mb/s)","2328.48 (min 2274.80, max 2413.50)"

CoreMarkPro
^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","39.26 (min 37.31, max 42.19)"
    "core (workloads/)","0.28 (min 0.27, max 0.30)"
    "coremark-pro ()","878.42 (min 816.27, max 956.64)"
    "linear_alg-mid-100x100-sp (workloads/)","13.73 (min 13.10, max 14.68)"
    "loops-all-mid-10k-sp (workloads/)","0.67 (min 0.64, max 0.71)"
    "nnet_test (workloads/)","1.01 (min 0.96, max 1.08)"
    "parser-125k (workloads/)","8.48 (min 7.94, max 9.35)"
    "radix2-big-64k (workloads/)","63.41 (min 48.48, max 75.74)"
    "sha-test (workloads/)","76.21 (min 72.46, max 81.30)"
    "zip-test (workloads/)","21.17 (min 20.00, max 23.26)"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","78.14 (min 74.07, max 84.03)"
    "core (workloads/)","0.56 (min 0.54, max 0.60)"
    "coremark-pro ()","1582.94 (min 1487.40, max 1713.31)"
    "linear_alg-mid-100x100-sp (workloads/)","27.45 (min 26.19, max 29.36)"
    "loops-all-mid-10k-sp (workloads/)","1.24 (min 1.18, max 1.32)"
    "nnet_test (workloads/)","2.01 (min 1.92, max 2.15)"
    "parser-125k (workloads/)","14.04 (min 12.05, max 16.67)"
    "radix2-big-64k (workloads/)","66.02 (min 63.30, max 69.22)"
    "sha-test (workloads/)","151.47 (min 144.93, max 161.29)"
    "zip-test (workloads/)","41.87 (min 38.46, max 46.51)"

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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "4m-check (workloads/)","400.01 (min 389.29, max 419.89)"
    "4m-check-reassembly (workloads/)","113.31 (min 110.38, max 118.06)"
    "4m-check-reassembly-tcp (workloads/)","57.65 (min 55.93, max 60.83)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","32.13 (min 30.91, max 34.38)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.75 (min 1.66, max 1.90)"
    "4m-cmykw2 (workloads/)","230.97 (min 222.72, max 247.22)"
    "4m-cmykw2-rotatew2 (workloads/)","44.27 (min 42.64, max 46.69)"
    "4m-reassembly (workloads/)","75.98 (min 74.02, max 79.30)"
    "4m-rotatew2 (workloads/)","49.28 (min 47.37, max 52.49)"
    "4m-tcp-mixed (workloads/)","119.41 (min 115.11, max 128.00)"
    "4m-x264w2 (workloads/)","1.75 (min 1.75, max 1.76)"
    "idct-4m (workloads/)","17.85 (min 17.17, max 19.20)"
    "idct-4mw1 (workloads/)","17.86 (min 17.19, max 19.19)"
    "ippktcheck-4m (workloads/)","401.16 (min 390.44, max 420.95)"
    "ippktcheck-4mw1 (workloads/)","400.93 (min 390.26, max 419.96)"
    "ipres-4m (workloads/)","99.59 (min 97.78, max 103.02)"
    "ipres-4mw1 (workloads/)","99.17 (min 97.40, max 102.39)"
    "md5-4m (workloads/)","26.22 (min 25.27, max 28.03)"
    "md5-4mw1 (workloads/)","26.08 (min 25.09, max 27.90)"
    "rgbcmyk-4m (workloads/)","61.17 (min 58.82, max 65.83)"
    "rgbcmyk-4mw1 (workloads/)","61.16 (min 58.81, max 65.77)"
    "rotate-4ms1 (workloads/)","22.01 (min 21.25, max 23.46)"
    "rotate-4ms1w1 (workloads/)","22.03 (min 21.29, max 23.42)"
    "rotate-4ms64 (workloads/)","22.19 (min 21.35, max 23.67)"
    "rotate-4ms64w1 (workloads/)","22.24 (min 21.51, max 23.63)"
    "x264-4mq (workloads/)","0.54 (min 0.51, max 0.58)"
    "x264-4mqw1 (workloads/)","0.54 (min 0.52, max 0.58)"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62pxx_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","17.86 (min 16.83, max 19.02)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

ALSA SoC Audio Driver
---------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62pxx_sk-fs: Throughput (bits/sec)","am62pxx_sk-fs: CPU Load (%)"

    "11025","352798.20 (min 352797.00, max 352799.00)","0.12 (min 0.10, max 0.13)"
    "16000","511998.20 (min 511996.00, max 512000.00)","0.11 (min 0.10, max 0.11)"
    "22050","705595.60 (min 705594.00, max 705597.00)","0.14 (min 0.13, max 0.15)"
    "24000","705596.80 (min 705594.00, max 705599.00)","0.16 (min 0.14, max 0.18)"
    "32000","1023995.60 (min 1023991.00, max 1023999.00)","0.38 (min 0.09, max 1.50)"
    "44100","1411193.40 (min 1411187.00, max 1411199.00)","0.23 (min 0.20, max 0.24)"
    "48000","1535993.00 (min 1535986.00, max 1535999.00)","0.21 (min 0.09, max 0.65)"
    "88200","2822383.20 (min 2822371.00, max 2822395.00)","0.37 (min 0.35, max 0.40)"
    "96000","3071966.00 (min 3071934.00, max 3071992.00)","0.27 (min 0.12, max 0.71)"

.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62pxx_sk-fs: Throughput (bits/sec)","am62pxx_sk-fs: CPU Load (%)"

    "11025","352946.00 (min 352945.00, max 352947.00)","0.10 (min 0.09, max 0.11)"
    "16000","512213.40 (min 512212.00, max 512215.00)","0.11 (min 0.10, max 0.12)"
    "22050","705877.40 (min 705825.00, max 705892.00)","0.12"
    "24000","705892.80 (min 705891.00, max 705895.00)","0.13 (min 0.12, max 0.14)"
    "32000","835300.40 (min 78800.00, max 1024428.00)","0.09 (min 0.07, max 0.11)"
    "44100","1411741.00 (min 1411558.00, max 1411790.00)","0.17 (min 0.15, max 0.18)"
    "48000","1536638.50 (min 1536636.00, max 1536641.00)","0.10 (min 0.10, max 0.11)"
    "88200","2823571.00 (min 2823566.00, max 2823576.00)","0.28 (min 0.24, max 0.31)"
    "96000","3073263.00 (min 3073241.00, max 3073275.00)","0.14 (min 0.13, max 0.15)"

|

Graphics SGX/RGX Driver
-----------------------

GFXBench
^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62pxx_sk-fs: Score","am62pxx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","863.66 (min 842.62, max 903.54)","13.93 (min 13.59, max 14.57)"
    " GFXBench 3.x gl_trex_off","1591.39","28.42"
    " GFXBench 5.x gl_5_high_off","108.08 (min 104.61, max 115.03)","1.68 (min 1.63, max 1.79)"

Glmark2
^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62pxx_sk-fs: Score"

    "Glmark2-DRM","276.50 (min 157.00, max 353.00)"
    "Glmark2-Wayland","733.20 (min 718.00, max 782.00)"

|

Ethernet
--------
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

CPSW/CPSW2g/CPSW3g Ethernet Driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- CPSW3g: AM64x, AM62x, AM62ax, AM62px

.. rubric::  TCP Bidirectional Throughput
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1553.15 (min 1176.25, max 1811.29)","54.49 (min 39.05, max 70.68)"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1849.66 (min 1825.39, max 1875.16)","38.86 (min 32.01, max 45.30)"

.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62pxx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: Packets Per Second (kPPS)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","51.17 (min 41.42, max 63.85)","100.00 (min 81.00, max 125.00)","40.18 (min 37.30, max 43.08)"
    "128","","101.30 (min 81.62, max 127.24)","99.00 (min 80.00, max 124.00)","39.93 (min 37.23, max 42.60)"
    "256","","199.81 (min 162.14, max 250.72)","97.25 (min 79.00, max 122.00)","39.74 (min 36.74, max 42.59)"
    "1024","","768.11 (min 634.77, max 935.43)","93.50 (min 77.00, max 114.00)","40.08 (min 36.82, max 45.20)"
    "1518","","759.63 (min 622.71, max 917.85)","62.75 (min 51.00, max 76.00)","37.32 (min 34.57, max 41.16)"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62pxx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: Packets Per Second (kPPS)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "128","","4.37 (min 3.89, max 5.02)","4.33 (min 4.00, max 5.00)","1.36 (min 0.83, max 2.25)"

.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62pxx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: Packets Per Second (kPPS)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62pxx_sk-fs: Packet Loss %"

    "128","","145.25 (min 124.88, max 181.77)","142.00 (min 122.00, max 178.00)","36.41 (min 34.88, max 39.17)","76.69 (min 71.36, max 80.26)"

|

Linux OSPI Flash Driver
-----------------------

.. rubric:: AM62PXX-SK
   :name: am62pxx-sk-ospi

.. rubric:: UBIFS
   :name: am62pxx-sk-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Write UBIFS CPU Load (%)","am62pxx_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.11, max 0.28)","28.43 (min 24.61, max 34.68)","27.63 (min 27.23, max 28.20)","9.70 (min 6.45, max 12.90)"
    "262144","0.13 (min 0.10, max 0.18)","29.86 (min 25.97, max 34.50)","27.60 (min 27.18, max 28.27)","5.98 (min 3.45, max 6.67)"
    "524288","0.13 (min 0.10, max 0.18)","29.15 (min 25.26, max 32.64)","27.37 (min 27.03, max 27.85)","6.63 (min 3.45, max 9.68)"
    "1048576","0.13 (min 0.10, max 0.18)","30.02 (min 27.22, max 33.36)","27.16 (min 26.74, max 27.82)","9.50 (min 3.33, max 12.90)"

.. rubric:: RAW
   :name: am62pxx-sk-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62pxx_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","37.88"

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
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","91.50 (min 90.50, max 92.60)","1.68 (min 1.62, max 1.76)","265.60 (min 172.00, max 292.00)","2.75 (min 1.76, max 3.10)"
    "4m","96.74 (min 96.20, max 97.20)","1.06 (min 0.97, max 1.13)","259.00 (min 172.00, max 289.00)","2.00 (min 1.35, max 2.34)"
    "4k","75.68 (min 63.50, max 79.10)","24.68 (min 20.29, max 26.37)","91.88 (min 88.50, max 94.10)","21.96 (min 21.39, max 22.51)"
    "256k","91.10 (min 90.60, max 91.70)","2.08 (min 1.91, max 2.26)","267.80 (min 173.00, max 294.00)","4.07 (min 2.71, max 4.75)"

EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","91.67 (min 87.34, max 94.14)","3.71 (min 2.83, max 5.23)","177.06 (min 168.93, max 179.17)","6.08 (min 5.15, max 6.84)"
    "262144","81.61 (min 48.84, max 94.77)","2.36 (min 1.28, max 3.85)","179.77 (min 175.01, max 181.42)","5.75 (min 4.74, max 6.47)"
    "524288","78.37 (min 47.78, max 94.13)","2.30 (min 1.14, max 4.65)","181.00 (min 177.82, max 182.35)","5.77 (min 4.76, max 6.47)"
    "1048576","77.61 (min 48.31, max 94.36)","2.28 (min 1.14, max 3.87)","180.95 (min 178.16, max 182.00)","5.19 (min 4.78, max 6.03)"
    "5242880","75.53 (min 47.37, max 95.20)","2.43 (min 1.12, max 4.32)","181.68 (min 181.18, max 182.02)","5.64 (min 5.19, max 6.49)"

EMMC VFAT
^^^^^^^^^

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Write VFAT CPU Load (%)","am62pxx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Read VFAT CPU Load (%)"

    "102400","38.37 (min 11.31, max 52.60)","5.05 (min 3.66, max 7.13)","200.84 (min 174.06, max 210.23)","11.14 (min 8.40, max 13.24)"
    "262144","44.05 (min 11.91, max 62.82)","5.83 (min 4.00, max 8.71)","263.27 (min 176.35, max 288.62)","16.52 (min 9.70, max 22.92)"
    "524288","50.43 (min 12.09, max 73.37)","5.16 (min 3.42, max 6.98)","263.58 (min 176.08, max 288.67)","14.38 (min 8.90, max 16.44)"
    "1048576","52.85 (min 12.24, max 75.55)","5.12 (min 3.58, max 6.94)","262.95 (min 176.25, max 285.29)","14.56 (min 8.05, max 17.57)"
    "5242880","55.67 (min 12.34, max 82.40)","5.28 (min 3.61, max 7.06)","262.72 (min 175.95, max 284.89)","14.16 (min 9.62, max 16.44)"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","98095.04 (min 95255.81, max 101135.80)","196449.26 (min 155298.58, max 268590.16)"
    "4000000","97568.90 (min 95672.99, max 99598.78)","247676.85 (min 193893.49, max 302009.22)"

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
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","43.06 (min 42.00, max 43.70)","1.06 (min 0.97, max 1.13)","87.44 (min 87.10, max 88.20)","1.34 (min 1.23, max 1.42)"
    "4m","42.16 (min 40.90, max 43.30)","0.69 (min 0.61, max 0.75)","86.26 (min 82.30, max 87.40)","0.94 (min 0.83, max 1.06)"
    "4k","2.83 (min 2.79, max 2.88)","1.66 (min 1.51, max 1.76)","13.10 (min 12.90, max 13.50)","4.37 (min 3.98, max 4.93)"
    "256k","38.92 (min 38.50, max 39.50)","1.30 (min 1.13, max 1.44)","83.68 (min 83.30, max 84.40)","1.59 (min 1.47, max 1.72)"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.84 (min 10.58, max 11.28)","0.48 (min 0.36, max 0.69)","11.30 (min 10.87, max 11.81)","0.49 (min 0.45, max 0.61)"
    "262144","10.82 (min 10.65, max 11.18)","0.41 (min 0.29, max 0.73)","11.09 (min 10.97, max 11.24)","0.57 (min 0.50, max 0.68)"
    "524288","10.85 (min 10.31, max 11.10)","0.38 (min 0.26, max 0.55)","11.11 (min 10.88, max 11.52)","0.45 (min 0.39, max 0.53)"
    "1048576","10.83 (min 10.11, max 11.33)","0.43 (min 0.29, max 0.62)","11.67 (min 11.27, max 12.03)","0.49 (min 0.38, max 0.63)"
    "5242880","10.99 (min 10.47, max 11.35)","0.39 (min 0.26, max 0.59)","11.83 (min 11.06, max 12.03)","0.43 (min 0.40, max 0.49)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","36090.73 (min 33573.77, max 40960.00)","82588.74 (min 81920.00, max 83591.84)"
    "800000","41443.90 (min 34276.15, max 43807.49)","87148.94"
    "1000000","46962.65 (min 42226.80, max 49498.49)","89530.05"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

USB Driver
----------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","35.96 (min 27.00, max 38.60)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","30.72 (min 24.80, max 33.40)"

|

CRYPTO Driver
-------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62pxx_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","22662.57 (min 21330.94, max 24852.48)"
    "aes-128-cbc","16","419.93 (min 405.77, max 451.41)"
    "aes-128-cbc","16384","85168.13 (min 84497.75, max 86633.13)"
    "aes-128-cbc","256","6960.34 (min 6771.88, max 7385.94)"
    "aes-128-cbc","64","1841.70 (min 1769.47, max 1961.96)"
    "aes-128-cbc","8192","71877.29 (min 71005.53, max 73714.35)"
    "aes-128-ecb","1024","23194.71 (min 21783.55, max 25396.91)"
    "aes-128-ecb","16","429.13 (min 415.93, max 459.21)"
    "aes-128-ecb","16384","88210.09 (min 87332.18, max 89571.33)"
    "aes-128-ecb","256","7081.71 (min 6928.81, max 7419.65)"
    "aes-128-ecb","64","1889.19 (min 1835.82, max 2021.99)"
    "aes-128-ecb","8192","74016.09 (min 73064.45, max 76046.34)"
    "aes-192-cbc","1024","22294.78 (min 20896.77, max 24468.82)"
    "aes-192-cbc","16","421.20 (min 406.44, max 453.28)"
    "aes-192-cbc","16384","77471.74 (min 76819.11, max 78697.81)"
    "aes-192-cbc","256","6940.52 (min 6709.25, max 7392.43)"
    "aes-192-cbc","64","1848.60 (min 1800.21, max 1973.61)"
    "aes-192-cbc","8192","66239.83 (min 65129.13, max 68182.02)"
    "aes-192-ecb","1024","22754.90 (min 21388.97, max 24982.19)"
    "aes-192-ecb","16","429.45 (min 415.78, max 460.86)"
    "aes-192-ecb","16384","79107.41 (min 78129.83, max 80013.99)"
    "aes-192-ecb","256","7031.79 (min 6869.93, max 7419.90)"
    "aes-192-ecb","64","1887.06 (min 1827.56, max 2022.78)"
    "aes-192-ecb","8192","67811.33 (min 67212.63, max 68577.96)"
    "aes-256-cbc","1024","21804.80 (min 20580.35, max 23639.04)"
    "aes-256-cbc","16","421.40 (min 407.79, max 452.66)"
    "aes-256-cbc","16384","70429.35 (min 69533.70, max 71286.78)"
    "aes-256-cbc","256","6910.42 (min 6666.84, max 7359.06)"
    "aes-256-cbc","64","1847.16 (min 1798.85, max 1968.02)"
    "aes-256-cbc","8192","61151.91 (min 60593.49, max 61991.59)"
    "aes-256-ecb","1024","22310.49 (min 21001.90, max 24208.38)"
    "aes-256-ecb","16","429.48 (min 414.78, max 460.38)"
    "aes-256-ecb","16384","72333.99 (min 71374.17, max 73433.09)"
    "aes-256-ecb","256","7017.88 (min 6817.88, max 7410.43)"
    "aes-256-ecb","64","1884.53 (min 1836.84, max 2008.73)"
    "aes-256-ecb","8192","62623.74 (min 61491.88, max 63670.95)"
    "sha256","1024","29610.41 (min 28761.43, max 31727.96)"
    "sha256","16","483.89 (min 461.47, max 527.91)"
    "sha256","16384","258501.29 (min 250724.35, max 275256.66)"
    "sha256","256","7645.93 (min 7375.87, max 8255.57)"
    "sha256","64","1921.05 (min 1845.40, max 2081.13)"
    "sha256","8192","169372.33 (min 164525.40, max 180974.93)"
    "sha512","1024","24823.30 (min 23840.43, max 26991.96)"
    "sha512","16","475.94 (min 460.72, max 517.66)"
    "sha512","16384","101677.74 (min 98396.84, max 110455.47)"
    "sha512","256","7190.93 (min 6925.57, max 7765.50)"
    "sha512","64","1903.05 (min 1842.90, max 2071.62)"
    "sha512","8192","84061.53 (min 81250.99, max 91379.03)"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62pxx_sk-fs: CPU Load"

    "aes-128-cbc","34.25 (min 34.00, max 35.00)"
    "aes-128-ecb","35.50 (min 35.00, max 36.00)"
    "aes-192-cbc","34.25 (min 33.00, max 35.00)"
    "aes-192-ecb","34.75 (min 34.00, max 35.00)"
    "aes-256-cbc","33.50 (min 33.00, max 34.00)"
    "aes-256-ecb","34.50 (min 34.00, max 35.00)"
    "sha256","96.00"
    "sha512","96.00"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc
