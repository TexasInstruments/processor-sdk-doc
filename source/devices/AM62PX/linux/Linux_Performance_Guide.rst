
===================================
Linux 11.02.08.02 Performance Guide
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

    "af_unix_sock_stream_latency (microsec)","30.38 (min 29.49, max 31.11)"
    "af_unix_socket_stream_bandwidth (mb\s)","1141.99 (min 1114.62, max 1178.85)"
    "bw_file_rd-io-1mb (mb/s)","1420.50 (min 1397.38, max 1467.89)"
    "bw_file_rd-o2c-1mb (mb/s)","756.14 (min 707.71, max 787.56)"
    "bw_mem-bcopy-16mb (mb/s)","1893.33 (min 1820.46, max 1973.12)"
    "bw_mem-bcopy-1mb (mb/s)","2039.91 (min 1948.56, max 2126.53)"
    "bw_mem-bcopy-2mb (mb/s)","1763.70 (min 1689.19, max 1838.80)"
    "bw_mem-bcopy-4mb (mb/s)","1778.31 (min 1643.39, max 1932.06)"
    "bw_mem-bcopy-8mb (mb/s)","1862.34 (min 1802.61, max 1939.39)"
    "bw_mem-bzero-16mb (mb/s)","7941.37 (min 7807.42, max 8116.33)"
    "bw_mem-bzero-1mb (mb/s)","4983.96 (min 1948.56, max 8117.51)"
    "bw_mem-bzero-2mb (mb/s)","4846.65 (min 1689.19, max 8105.73)"
    "bw_mem-bzero-4mb (mb/s)","4858.50 (min 1643.39, max 8110.85)"
    "bw_mem-bzero-8mb (mb/s)","4901.14 (min 1802.61, max 8110.85)"
    "bw_mem-cp-16mb (mb/s)","936.73 (min 894.15, max 985.16)"
    "bw_mem-cp-1mb (mb/s)","4594.51 (min 890.31, max 8403.36)"
    "bw_mem-cp-2mb (mb/s)","4486.54 (min 865.05, max 8255.56)"
    "bw_mem-cp-4mb (mb/s)","4485.96 (min 926.14, max 8185.54)"
    "bw_mem-cp-8mb (mb/s)","4481.34 (min 948.77, max 8154.94)"
    "bw_mem-fcp-16mb (mb/s)","1764.54 (min 1699.96, max 1837.60)"
    "bw_mem-fcp-1mb (mb/s)","4843.70 (min 1689.51, max 8117.51)"
    "bw_mem-fcp-2mb (mb/s)","4796.57 (min 1575.05, max 8105.73)"
    "bw_mem-fcp-4mb (mb/s)","4826.26 (min 1609.87, max 8110.85)"
    "bw_mem-fcp-8mb (mb/s)","4831.18 (min 1631.82, max 8110.85)"
    "bw_mem-frd-16mb (mb/s)","1908.07 (min 1837.18, max 2011.06)"
    "bw_mem-frd-1mb (mb/s)","1907.50 (min 1689.51, max 2142.09)"
    "bw_mem-frd-2mb (mb/s)","1705.84 (min 1575.05, max 1836.88)"
    "bw_mem-frd-4mb (mb/s)","1764.63 (min 1609.87, max 1909.31)"
    "bw_mem-frd-8mb (mb/s)","1789.25 (min 1631.82, max 1998.75)"
    "bw_mem-fwr-16mb (mb/s)","7958.93 (min 7822.69, max 8134.21)"
    "bw_mem-fwr-1mb (mb/s)","5153.95 (min 1974.16, max 8403.36)"
    "bw_mem-fwr-2mb (mb/s)","4904.86 (min 1597.44, max 8255.56)"
    "bw_mem-fwr-4mb (mb/s)","4913.69 (min 1659.06, max 8185.54)"
    "bw_mem-fwr-8mb (mb/s)","4917.48 (min 1674.52, max 8154.94)"
    "bw_mem-rd-16mb (mb/s)","1983.53 (min 1918.24, max 2065.32)"
    "bw_mem-rd-1mb (mb/s)","2035.54 (min 1708.82, max 2331.46)"
    "bw_mem-rd-2mb (mb/s)","1794.96 (min 1510.00, max 2037.35)"
    "bw_mem-rd-4mb (mb/s)","1864.28 (min 1662.05, max 2055.85)"
    "bw_mem-rd-8mb (mb/s)","1901.83 (min 1763.28, max 2069.05)"
    "bw_mem-rdwr-16mb (mb/s)","1853.51 (min 1684.21, max 1942.45)"
    "bw_mem-rdwr-1mb (mb/s)","1329.35 (min 890.31, max 1855.29)"
    "bw_mem-rdwr-2mb (mb/s)","1231.50 (min 865.05, max 1661.96)"
    "bw_mem-rdwr-4mb (mb/s)","1342.24 (min 926.14, max 1834.58)"
    "bw_mem-rdwr-8mb (mb/s)","1405.93 (min 948.77, max 1942.22)"
    "bw_mem-wr-16mb (mb/s)","1883.72 (min 1802.41, max 1975.55)"
    "bw_mem-wr-1mb (mb/s)","1779.17 (min 1614.06, max 2043.60)"
    "bw_mem-wr-2mb (mb/s)","1589.31 (min 1490.59, max 1853.57)"
    "bw_mem-wr-4mb (mb/s)","1739.42 (min 1631.10, max 1869.45)"
    "bw_mem-wr-8mb (mb/s)","1824.68 (min 1672.24, max 1942.22)"
    "bw_mmap_rd-mo-1mb (mb/s)","2177.27 (min 2111.56, max 2271.54)"
    "bw_mmap_rd-o2c-1mb (mb/s)","772.38 (min 680.85, max 826.72)"
    "bw_pipe (mb/s)","783.15 (min 729.29, max 819.18)"
    "bw_unix (mb/s)","1141.99 (min 1114.62, max 1178.85)"
    "lat_connect (us)","56.81 (min 56.67, max 57.00)"
    "lat_ctx-2-128k (us)","7.83 (min 7.60, max 8.13)"
    "lat_ctx-2-256k (us)","7.72 (min 6.67, max 11.90)"
    "lat_ctx-4-128k (us)","7.42 (min 6.78, max 7.96)"
    "lat_ctx-4-256k (us)","6.99 (min 6.18, max 8.04)"
    "lat_fs-0k (num_files)","239.71 (min 221.00, max 253.00)"
    "lat_fs-10k (num_files)","117.29 (min 106.00, max 136.00)"
    "lat_fs-1k (num_files)","160.43 (min 145.00, max 179.00)"
    "lat_fs-4k (num_files)","159.43 (min 142.00, max 176.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","30.55 (min 29.36, max 31.41)"
    "lat_mem_rd-stride128-sz125k (ns)","5.57 (min 5.54, max 5.64)"
    "lat_mem_rd-stride128-sz250k (ns)","5.84 (min 5.83, max 5.85)"
    "lat_mem_rd-stride128-sz31k (ns)","3.15 (min 2.16, max 4.66)"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","10.88 (min 9.02, max 12.76)"
    "lat_mem_rd-stride128-sz62k (ns)","5.24 (min 5.20, max 5.26)"
    "lat_mmap-1m (us)","52.57 (min 50.00, max 57.00)"
    "lat_ops-double-add (ns)","2.86"
    "lat_ops-double-div (ns)","15.74 (min 15.74, max 15.75)"
    "lat_ops-double-mul (ns)","2.86"
    "lat_ops-float-add (ns)","2.86"
    "lat_ops-float-div (ns)","9.30 (min 9.30, max 9.31)"
    "lat_ops-float-mul (ns)","2.86"
    "lat_ops-int-add (ns)","0.72"
    "lat_ops-int-bit (ns)","0.48"
    "lat_ops-int-div (ns)","4.29"
    "lat_ops-int-mod (ns)","4.53 (min 4.53, max 4.54)"
    "lat_ops-int-mul (ns)","3.08 (min 3.07, max 3.09)"
    "lat_ops-int64-add (ns)","0.72"
    "lat_ops-int64-bit (ns)","0.48"
    "lat_ops-int64-div (ns)","6.80"
    "lat_ops-int64-mod (ns)","5.25"
    "lat_ops-int64-mul (ns)","3.56 (min 3.55, max 3.57)"
    "lat_pagefault (us)","0.52 (min 0.50, max 0.54)"
    "lat_pipe (us)","25.74 (min 25.17, max 26.44)"
    "lat_proc-exec (us)","709.41 (min 689.88, max 728.75)"
    "lat_proc-fork (us)","616.86 (min 602.89, max 633.11)"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","33.97 (min 33.79, max 34.06)"
    "lat_sem (us)","3.04 (min 2.65, max 3.79)"
    "lat_sig-catch (us)","5.54 (min 5.27, max 5.77)"
    "lat_sig-install (us)","0.67 (min 0.65, max 0.71)"
    "lat_sig-prot (us)","0.65 (min 0.50, max 0.76)"
    "lat_syscall-fstat (us)","1.99 (min 1.90, max 2.07)"
    "lat_syscall-null (us)","0.46 (min 0.46, max 0.50)"
    "lat_syscall-open (us)","188.47 (min 153.56, max 251.41)"
    "lat_syscall-read (us)","0.83 (min 0.80, max 0.88)"
    "lat_syscall-stat (us)","4.79 (min 4.67, max 4.97)"
    "lat_syscall-write (us)","0.78 (min 0.75, max 0.84)"
    "lat_tcp (us)","0.92 (min 0.91, max 0.97)"
    "lat_unix (us)","30.38 (min 29.49, max 31.11)"
    "latency_for_0.50_mb_block_size (nanosec)","10.88 (min 9.02, max 12.76)"
    "latency_for_1.00_mb_block_size (nanosec)","15.28 (min 0.00, max 31.41)"
    "pipe_bandwidth (mb\s)","783.15 (min 729.29, max 819.18)"
    "pipe_latency (microsec)","25.74 (min 25.17, max 26.44)"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","33.97 (min 33.79, max 34.06)"
    "semaphore_latency (microsec)","3.04 (min 2.65, max 3.79)"
    "signal_handler_latency (microsec)","0.67 (min 0.65, max 0.71)"
    "signal_handler_overhead (microsec)","5.54 (min 5.27, max 5.77)"
    "tcp_ip_connection_cost_to_localhost (microsec)","56.81 (min 56.67, max 57.00)"
    "tcp_latency_using_localhost (microsec)","0.92 (min 0.91, max 0.97)"

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

    "cpu_clock (mhz)","1400.00"
    "dhrystone_per_mhz (dmips/mhz)","2.91 (min 2.90, max 3.00)"
    "dhrystone_per_second (dhrystonep)","7180649.93 (min 7142857.00, max 7407407.50)"

Whetstone
^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "whetstone (mips)","6428.57 (min 5000.00, max 10000.00)"

Linpack
^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "linpack (kflops)","575572.00 (min 571460.00, max 577031.00)"

NBench
^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "assignment (iterations)","14.48 (min 14.45, max 14.50)"
    "fourier (iterations)","22831.29 (min 22831.00, max 22832.00)"
    "fp_emulation (iterations)","215.64 (min 215.64, max 215.65)"
    "huffman (iterations)","1184.13 (min 1183.30, max 1184.40)"
    "idea (iterations)","3444.83 (min 3444.70, max 3444.90)"
    "lu_decomposition (iterations)","529.08 (min 526.35, max 533.03)"
    "neural_net (iterations)","8.65 (min 8.65, max 8.66)"
    "numeric_sort (iterations)","625.73 (min 617.87, max 629.99)"
    "string_sort (iterations)","163.94 (min 163.93, max 163.94)"

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

    "add (mb/s)","2825.76 (min 2698.10, max 2879.00)"
    "copy (mb/s)","3941.66 (min 3718.70, max 4027.40)"
    "scale (mb/s)","3624.44 (min 3481.60, max 3704.10)"
    "triad (mb/s)","2492.96 (min 2403.50, max 2530.10)"

CoreMarkPro
^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","41.97 (min 41.84, max 42.02)"
    "core (workloads/)","0.30"
    "coremark-pro ()","927.45 (min 906.93, max 947.60)"
    "linear_alg-mid-100x100-sp (workloads/)","14.68 (min 14.68, max 14.70)"
    "loops-all-mid-10k-sp (workloads/)","0.71 (min 0.71, max 0.72)"
    "nnet_test (workloads/)","1.09"
    "parser-125k (workloads/)","8.83 (min 8.77, max 8.85)"
    "radix2-big-64k (workloads/)","62.81 (min 53.18, max 74.52)"
    "sha-test (workloads/)","81.68 (min 81.30, max 81.97)"
    "zip-test (workloads/)","22.15 (min 21.74, max 22.22)"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","83.45 (min 82.64, max 84.03)"
    "core (workloads/)","0.60"
    "coremark-pro ()","1670.65 (min 1656.51, max 1691.47)"
    "linear_alg-mid-100x100-sp (workloads/)","29.34 (min 29.31, max 29.36)"
    "loops-all-mid-10k-sp (workloads/)","1.31 (min 1.30, max 1.31)"
    "nnet_test (workloads/)","2.17 (min 2.16, max 2.17)"
    "parser-125k (workloads/)","13.95 (min 13.51, max 14.49)"
    "radix2-big-64k (workloads/)","71.62 (min 68.31, max 76.15)"
    "sha-test (workloads/)","162.61 (min 161.29, max 163.93)"
    "zip-test (workloads/)","42.55"

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

    "4m-check (workloads/)","419.94 (min 412.34, max 431.18)"
    "4m-check-reassembly (workloads/)","123.93 (min 120.34, max 128.54)"
    "4m-check-reassembly-tcp (workloads/)","59.99 (min 59.10, max 61.27)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","33.80 (min 33.24, max 34.68)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.89 (min 1.87, max 1.91)"
    "4m-cmykw2 (workloads/)","243.33 (min 238.66, max 246.61)"
    "4m-cmykw2-rotatew2 (workloads/)","50.36 (min 49.71, max 51.37)"
    "4m-reassembly (workloads/)","83.96 (min 82.30, max 86.28)"
    "4m-rotatew2 (workloads/)","53.30 (min 52.63, max 54.26)"
    "4m-tcp-mixed (workloads/)","118.90 (min 118.52, max 119.40)"
    "4m-x264w2 (workloads/)","1.95 (min 1.80, max 2.00)"
    "idct-4m (workloads/)","19.21 (min 19.18, max 19.23)"
    "idct-4mw1 (workloads/)","19.21 (min 19.18, max 19.23)"
    "ippktcheck-4m (workloads/)","421.59 (min 413.22, max 431.63)"
    "ippktcheck-4mw1 (workloads/)","421.60 (min 412.61, max 431.33)"
    "ipres-4m (workloads/)","113.14 (min 110.54, max 116.73)"
    "ipres-4mw1 (workloads/)","113.31 (min 110.13, max 116.64)"
    "md5-4m (workloads/)","27.53 (min 27.10, max 27.88)"
    "md5-4mw1 (workloads/)","27.73 (min 27.45, max 27.98)"
    "rgbcmyk-4m (workloads/)","64.48 (min 62.70, max 65.81)"
    "rgbcmyk-4mw1 (workloads/)","64.46 (min 62.68, max 65.77)"
    "rotate-4ms1 (workloads/)","23.74 (min 23.38, max 24.15)"
    "rotate-4ms1w1 (workloads/)","23.76 (min 23.41, max 24.21)"
    "rotate-4ms64 (workloads/)","24.00 (min 23.66, max 24.49)"
    "rotate-4ms64w1 (workloads/)","24.34 (min 23.64, max 26.53)"
    "x264-4mq (workloads/)","0.58 (min 0.57, max 0.58)"
    "x264-4mqw1 (workloads/)","0.57 (min 0.53, max 0.58)"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62pxx_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","13.59 (min 13.10, max 18.72)"

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

    "11025","352798.33 (min 352797.00, max 352800.00)","0.10 (min 0.08, max 0.10)"
    "16000","511998.83 (min 511997.00, max 512002.00)","0.23 (min 0.08, max 0.48)"
    "22050","705594.83 (min 705589.00, max 705599.00)","0.13 (min 0.11, max 0.15)"
    "24000","705597.17 (min 705595.00, max 705599.00)","0.14 (min 0.13, max 0.15)"
    "32000","1023996.67 (min 1023994.00, max 1023998.00)","0.23 (min 0.08, max 0.87)"
    "44100","1411195.33 (min 1411192.00, max 1411197.00)","0.21 (min 0.20, max 0.23)"
    "48000","1535995.17 (min 1535991.00, max 1535998.00)","0.26 (min 0.09, max 0.92)"
    "88200","2822388.00 (min 2822381.00, max 2822394.00)","0.38 (min 0.35, max 0.40)"
    "96000","3071985.50 (min 3071973.00, max 3071993.00)","0.19 (min 0.17, max 0.21)"

.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62pxx_sk-fs: Throughput (bits/sec)","am62pxx_sk-fs: CPU Load (%)"

    "11025","352946.33 (min 352945.00, max 352947.00)","0.09 (min 0.07, max 0.10)"
    "16000","512213.17 (min 512210.00, max 512215.00)","0.08 (min 0.05, max 0.10)"
    "22050","705849.17 (min 705824.00, max 705896.00)","0.11 (min 0.09, max 0.12)"
    "24000","705891.33 (min 705888.00, max 705896.00)","0.13 (min 0.11, max 0.15)"
    "32000","551612.00 (min 78800.00, max 1024427.00)","0.21 (min 0.05, max 0.84)"
    "44100","1411628.17 (min 1411540.00, max 1411789.00)","0.18 (min 0.16, max 0.19)"
    "48000","1536632.67 (min 1536629.00, max 1536635.00)","0.26 (min 0.12, max 0.51)"
    "88200","2823553.00","0.34"
    "96000","3073255.00","0.94"

|

Graphics SGX/RGX Driver
-----------------------

GFXBench
^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62pxx_sk-fs: Score","am62pxx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","906.46 (min 902.42, max 910.12)","14.62 (min 14.56, max 14.68)"
    " GFXBench 3.x gl_trex_off","1582.33 (min 1576.54, max 1589.72)","28.26 (min 28.15, max 28.39)"
    " GFXBench 4.x gl_4_off","260.66 (min 259.90, max 261.32)","4.41 (min 4.40, max 4.42)"
    " GFXBench 5.x gl_5_high_off","114.64 (min 113.73, max 115.05)","1.78 (min 1.77, max 1.79)"

Glmark2
^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62pxx_sk-fs: Score"

    "Glmark2-DRM","314.14 (min 307.00, max 354.00)"
    "Glmark2-Wayland","730.75 (min 717.00, max 746.00)"

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

- CPSW2g: AM65x, J7200, J721e, J721S2, J784S4, J742S2
- CPSW3g: AM64x, AM62x, AM62ax, AM62px

.. rubric::  TCP Bidirectional Throughput
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1778.39 (min 1503.06, max 1857.97)","63.69 (min 60.80, max 65.40)"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1789.08 (min 1612.03, max 1873.08)","35.80 (min 27.35, max 38.76)"

.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62pxx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: Packets Per Second (kPPS)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","54.23 (min 53.64, max 55.42)","105.88 (min 105.00, max 108.00)","39.59 (min 39.25, max 40.20)"
    "128","82.00","107.70 (min 106.76, max 110.02)","105.00 (min 104.00, max 107.00)","39.41 (min 39.06, max 39.88)"
    "256","210.00","214.09 (min 211.33, max 217.17)","104.50 (min 103.00, max 106.00)","39.31 (min 39.08, max 39.69)"
    "1024","978.00","836.06 (min 813.57, max 847.48)","101.88 (min 99.00, max 103.00)","39.65 (min 38.57, max 40.42)"
    "1518","1472.00","838.69 (min 826.64, max 852.20)","69.13 (min 68.00, max 70.00)","37.17 (min 36.51, max 38.15)"

|

Linux OSPI Flash Driver
-----------------------

.. rubric:: AM62PXX-SK
   :name: am62pxx-sk-ospi

.. rubric:: UBIFS
   :name: am62pxx-sk-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Write UBIFS CPU Load (%)","am62pxx_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.28)","28.77 (min 24.69, max 33.84)","28.45 (min 28.34, max 28.64)","7.08 (min 3.57, max 12.50)"
    "262144","0.14 (min 0.10, max 0.18)","29.70 (min 25.14, max 35.52)","28.38 (min 28.03, max 28.59)","8.42 (min 3.45, max 12.90)"
    "524288","0.14 (min 0.10, max 0.18)","29.68 (min 26.42, max 33.97)","28.23 (min 27.97, max 28.56)","7.52 (min 3.45, max 12.50)"
    "1048576","0.14 (min 0.10, max 0.18)","29.89 (min 26.72, max 33.36)","27.96 (min 27.72, max 28.27)","7.96 (min 6.67, max 9.68)"

.. rubric:: RAW
   :name: am62pxx-sk-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62pxx_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","37.79 (min 37.31, max 37.88)"

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

    "1m","91.41 (min 90.40, max 92.50)","1.55 (min 1.48, max 1.61)","284.00 (min 276.00, max 289.00)","2.61 (min 2.33, max 2.79)"
    "4m","95.41 (min 90.40, max 97.50)","1.06 (min 1.00, max 1.13)","230.14 (min 153.00, max 288.00)","1.72 (min 1.26, max 2.10)"
    "4k","79.04 (min 78.90, max 79.30)","25.61 (min 25.54, max 25.65)","91.77 (min 89.20, max 93.10)","21.42 (min 20.63, max 21.94)"
    "256k","91.33 (min 90.70, max 91.80)","1.97 (min 1.84, max 2.09)","288.43 (min 280.00, max 291.00)","4.00 (min 3.76, max 4.15)"

EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "1m","90.53 (min 89.80, max 91.30)","1.37 (min 1.21, max 1.54)","293.29 (min 292.00, max 294.00)","2.64 (min 2.37, max 2.89)"
    "4m","96.93 (min 96.50, max 97.50)","0.97 (min 0.86, max 1.03)","277.00 (min 182.00, max 294.00)","1.90 (min 1.48, max 2.09)"
    "4k","76.76 (min 76.40, max 77.10)","18.94 (min 18.79, max 19.25)","92.90 (min 92.50, max 93.10)","20.21 (min 19.71, max 20.64)"
    "256k","90.53 (min 89.70, max 91.40)","1.73 (min 1.53, max 1.95)","293.57 (min 293.00, max 294.00)","3.83 (min 3.73, max 3.91)"

EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","83.27 (min 52.29, max 89.46)","5.94 (min 4.97, max 8.11)","178.78 (min 178.64, max 178.91)","8.44 (min 6.58, max 10.13)"
    "262144","80.06 (min 49.05, max 89.23)","5.71 (min 3.40, max 8.43)","179.72 (min 172.91, max 181.11)","9.36 (min 8.77, max 9.91)"
    "524288","75.36 (min 49.32, max 89.16)","5.33 (min 3.06, max 8.14)","180.13 (min 176.40, max 181.89)","8.74 (min 8.26, max 9.87)"
    "1048576","75.65 (min 47.53, max 88.93)","5.37 (min 2.72, max 8.45)","181.47 (min 180.95, max 181.87)","8.62 (min 7.86, max 9.44)"
    "5242880","76.21 (min 49.34, max 89.86)","5.37 (min 3.02, max 7.98)","180.45 (min 174.59, max 181.97)","8.71 (min 8.30, max 9.52)"

EMMC VFAT
^^^^^^^^^

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Write VFAT CPU Load (%)","am62pxx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Read VFAT CPU Load (%)"

    "102400","39.61 (min 11.80, max 52.28)","5.21 (min 3.66, max 6.47)","208.97 (min 208.62, max 209.38)","11.07 (min 9.23, max 12.81)"
    "262144","44.50 (min 12.47, max 62.38)","6.00 (min 4.12, max 9.12)","287.77 (min 285.96, max 289.30)","15.04 (min 12.77, max 16.55)"
    "524288","50.98 (min 12.69, max 73.49)","5.12 (min 3.75, max 7.69)","287.10 (min 285.81, max 288.26)","15.14 (min 14.58, max 16.11)"
    "1048576","53.77 (min 12.83, max 75.68)","5.03 (min 3.49, max 6.69)","287.01 (min 285.60, max 288.35)","14.66 (min 13.29, max 15.75)"
    "5242880","55.67 (min 13.01, max 81.71)","5.12 (min 3.81, max 6.94)","286.37 (min 280.42, max 288.38)","13.94 (min 12.77, max 15.75)"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","96461.77 (min 93891.12, max 100515.34)","215037.67 (min 146285.71, max 282482.76)"
    "4000000","97228.73 (min 95812.87, max 99447.65)","259335.04 (min 229950.88, max 296542.99)"

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

    "1m","42.59 (min 41.40, max 43.40)","1.06 (min 1.01, max 1.16)","87.31 (min 87.20, max 87.40)","1.29 (min 1.15, max 1.39)"
    "4m","42.17 (min 41.40, max 43.30)","0.71 (min 0.64, max 0.76)","87.24 (min 87.10, max 87.30)","0.92 (min 0.87, max 0.98)"
    "4k","2.80 (min 2.78, max 2.83)","1.67 (min 1.60, max 1.75)","12.94 (min 12.80, max 13.20)","4.31 (min 4.01, max 4.52)"
    "256k","38.44 (min 36.60, max 39.10)","1.25 (min 1.20, max 1.31)","83.47 (min 83.20, max 83.80)","1.52 (min 1.44, max 1.61)"

MMC RAW FIO 1G
^^^^^^^^^^^^^^

.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "1m","43.59 (min 42.40, max 45.10)","0.91 (min 0.86, max 1.01)","88.19 (min 88.10, max 88.30)","1.14 (min 1.09, max 1.22)"
    "4m","43.20 (min 42.10, max 45.00)","0.70 (min 0.63, max 0.76)","88.14 (min 88.00, max 88.30)","0.90 (min 0.84, max 0.96)"
    "4k","2.81 (min 2.80, max 2.83)","1.38 (min 1.33, max 1.43)","13.06 (min 13.00, max 13.10)","3.91 (min 3.82, max 4.06)"
    "256k","38.00 (min 36.20, max 41.40)","1.02 (min 0.96, max 1.08)","84.33 (min 84.20, max 84.50)","1.44 (min 1.38, max 1.50)"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.75 (min 10.41, max 11.18)","0.83 (min 0.67, max 1.20)","11.19 (min 10.89, max 11.82)","0.75 (min 0.68, max 0.90)"
    "262144","10.43 (min 10.25, max 10.62)","0.90 (min 0.68, max 1.46)","11.14 (min 10.99, max 11.22)","0.73 (min 0.63, max 0.78)"
    "524288","10.46 (min 10.29, max 10.86)","0.81 (min 0.65, max 1.20)","11.10 (min 10.85, max 11.50)","0.68 (min 0.61, max 0.88)"
    "1048576","10.49 (min 10.27, max 10.76)","0.88 (min 0.68, max 1.18)","11.06 (min 10.85, max 11.50)","0.66 (min 0.58, max 0.74)"
    "5242880","10.64 (min 10.27, max 11.12)","0.83 (min 0.64, max 1.20)","11.59 (min 10.97, max 12.03)","0.66 (min 0.58, max 0.73)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","36689.07 (min 28054.79, max 43574.47)","82875.34 (min 81920.00, max 83591.84)"
    "800000","40145.70 (min 33032.26, max 47627.91)","87148.94"
    "1000000","48396.32 (min 42555.84, max 51360.50)","89670.60 (min 89530.05, max 90021.98)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

USB Driver
----------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","30.13 (min 26.60, max 43.90)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","25.53 (min 21.90, max 37.10)"

|

CRYPTO Driver
-------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62pxx_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","23874.22 (min 22797.65, max 24305.66)"
    "aes-128-cbc","16","433.40 (min 414.08, max 439.83)"
    "aes-128-cbc","16384","86033.94 (min 84885.50, max 86523.90)"
    "aes-128-cbc","256","7133.66 (min 6779.65, max 7281.83)"
    "aes-128-cbc","64","1854.41 (min 1809.17, max 1895.91)"
    "aes-128-cbc","8192","72677.86 (min 71183.02, max 73187.33)"
    "aes-128-ecb","1024","24521.24 (min 23560.19, max 24830.98)"
    "aes-128-ecb","16","444.84 (min 423.89, max 450.61)"
    "aes-128-ecb","16384","88832.49 (min 87801.86, max 89511.25)"
    "aes-128-ecb","256","7297.62 (min 6986.33, max 7385.43)"
    "aes-128-ecb","64","1921.89 (min 1846.42, max 1959.10)"
    "aes-128-ecb","8192","74998.15 (min 72996.18, max 75606.70)"
    "aes-192-cbc","1024","23428.24 (min 22448.13, max 23803.22)"
    "aes-192-cbc","16","433.98 (min 413.37, max 440.67)"
    "aes-192-cbc","16384","77998.76 (min 76961.11, max 78419.29)"
    "aes-192-cbc","256","7084.75 (min 6741.16, max 7235.16)"
    "aes-192-cbc","64","1858.29 (min 1806.49, max 1907.71)"
    "aes-192-cbc","8192","66915.77 (min 65544.19, max 67439.27)"
    "aes-192-ecb","1024","24060.10 (min 23176.19, max 24450.05)"
    "aes-192-ecb","16","444.52 (min 424.39, max 449.94)"
    "aes-192-ecb","16384","80076.41 (min 78779.73, max 80767.66)"
    "aes-192-ecb","256","7282.65 (min 6920.45, max 7394.73)"
    "aes-192-ecb","64","1914.58 (min 1845.12, max 1949.12)"
    "aes-192-ecb","8192","68555.34 (min 67365.55, max 69383.51)"
    "aes-256-cbc","1024","22864.60 (min 21938.52, max 23255.72)"
    "aes-256-cbc","16","435.49 (min 413.74, max 442.78)"
    "aes-256-cbc","16384","70860.02 (min 69817.69, max 71636.31)"
    "aes-256-cbc","256","7052.84 (min 6704.38, max 7207.94)"
    "aes-256-cbc","64","1867.00 (min 1805.76, max 1916.16)"
    "aes-256-cbc","8192","61503.98 (min 60598.95, max 62406.66)"
    "aes-256-ecb","1024","23521.77 (min 22587.39, max 23857.15)"
    "aes-256-ecb","16","444.28 (min 425.70, max 450.73)"
    "aes-256-ecb","16384","72667.72 (min 72176.98, max 73558.70)"
    "aes-256-ecb","256","7234.73 (min 6907.56, max 7374.17)"
    "aes-256-ecb","64","1913.51 (min 1846.23, max 1957.03)"
    "aes-256-ecb","8192","63232.10 (min 62390.27, max 63744.68)"
    "sha256","1024","37936.08 (min 37196.12, max 38420.14)"
    "sha256","16","632.25 (min 614.09, max 639.77)"
    "sha256","16384","299548.67 (min 296605.01, max 302246.57)"
    "sha256","256","9906.47 (min 9659.73, max 10023.59)"
    "sha256","64","2505.28 (min 2431.06, max 2528.36)"
    "sha256","8192","203446.37 (min 199546.20, max 205512.70)"
    "sha512","1024","26078.79 (min 25618.77, max 26265.94)"
    "sha512","16","612.27 (min 590.90, max 623.37)"
    "sha512","16384","68343.91 (min 67993.60, max 68517.89)"
    "sha512","256","8707.43 (min 8436.31, max 8843.78)"
    "sha512","64","2455.43 (min 2363.48, max 2505.77)"
    "sha512","8192","61529.72 (min 61104.13, max 61680.30)"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62pxx_sk-fs: CPU Load"

    "aes-128-cbc","32.71 (min 31.00, max 33.00)"
    "aes-128-ecb","33.86 (min 32.00, max 35.00)"
    "aes-192-cbc","32.71 (min 31.00, max 33.00)"
    "aes-192-ecb","33.29 (min 32.00, max 34.00)"
    "aes-256-cbc","31.57 (min 30.00, max 32.00)"
    "aes-256-ecb","32.43 (min 31.00, max 33.00)"
    "sha256","95.57 (min 94.00, max 96.00)"
    "sha512","95.86 (min 95.00, max 96.00)"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc
