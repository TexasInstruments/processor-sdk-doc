.. include:: <isonum.txt>

#################################
 Linux 12.01.00 Performance Guide
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

System Benchmarks
-------------------

LMBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "af_unix_sock_stream_latency (microsec)","29.13 (min 25.73, max 32.78)"
    "af_unix_socket_stream_bandwidth (mb\s)","497.81 (min 446.92, max 544.77)"
    "bw_file_rd-io-1mb (mb/s)","981.72 (min 885.74, max 1063.64)"
    "bw_file_rd-o2c-1mb (mb/s)","510.96 (min 480.23, max 581.56)"
    "bw_mem-bcopy-16mb (mb/s)","787.31 (min 709.72, max 858.42)"
    "bw_mem-bcopy-1mb (mb/s)","809.45 (min 707.84, max 922.17)"
    "bw_mem-bcopy-2mb (mb/s)","809.91 (min 686.93, max 923.79)"
    "bw_mem-bcopy-4mb (mb/s)","822.90 (min 731.53, max 915.86)"
    "bw_mem-bcopy-8mb (mb/s)","858.15 (min 754.01, max 977.28)"
    "bw_mem-bzero-16mb (mb/s)","2440.52 (min 2120.33, max 2726.65)"
    "bw_mem-bzero-1mb (mb/s)","1625.79 (min 707.84, max 2727.27)"
    "bw_mem-bzero-2mb (mb/s)","1577.63 (min 686.93, max 2725.26)"
    "bw_mem-bzero-4mb (mb/s)","1627.81 (min 731.53, max 2726.19)"
    "bw_mem-bzero-8mb (mb/s)","1647.43 (min 754.01, max 2725.72)"
    "bw_mem-cp-16mb (mb/s)","453.47 (min 397.69, max 505.03)"
    "bw_mem-cp-1mb (mb/s)","1534.09 (min 392.77, max 2938.48)"
    "bw_mem-cp-2mb (mb/s)","1503.22 (min 398.84, max 2858.67)"
    "bw_mem-cp-4mb (mb/s)","1488.86 (min 423.15, max 2791.83)"
    "bw_mem-cp-8mb (mb/s)","1482.08 (min 453.10, max 2746.78)"
    "bw_mem-fcp-16mb (mb/s)","789.51 (min 710.89, max 859.48)"
    "bw_mem-fcp-1mb (mb/s)","1657.73 (min 782.47, max 2727.27)"
    "bw_mem-fcp-2mb (mb/s)","1603.27 (min 779.93, max 2725.26)"
    "bw_mem-fcp-4mb (mb/s)","1664.75 (min 787.25, max 2726.19)"
    "bw_mem-fcp-8mb (mb/s)","1672.56 (min 813.34, max 2725.72)"
    "bw_mem-frd-16mb (mb/s)","1383.14 (min 1185.71, max 1554.30)"
    "bw_mem-frd-1mb (mb/s)","1109.00 (min 782.47, max 1463.86)"
    "bw_mem-frd-2mb (mb/s)","1086.97 (min 779.93, max 1459.06)"
    "bw_mem-frd-4mb (mb/s)","1135.18 (min 787.25, max 1535.21)"
    "bw_mem-frd-8mb (mb/s)","1152.31 (min 813.34, max 1555.21)"
    "bw_mem-fwr-16mb (mb/s)","2450.64 (min 2128.23, max 2741.60)"
    "bw_mem-fwr-1mb (mb/s)","1974.95 (min 1220.15, max 2938.48)"
    "bw_mem-fwr-2mb (mb/s)","1926.99 (min 1133.57, max 2858.67)"
    "bw_mem-fwr-4mb (mb/s)","1932.64 (min 1200.48, max 2791.83)"
    "bw_mem-fwr-8mb (mb/s)","1929.10 (min 1217.66, max 2746.78)"
    "bw_mem-rd-16mb (mb/s)","1417.48 (min 1261.73, max 1562.96)"
    "bw_mem-rd-1mb (mb/s)","1023.01 (min 540.83, max 1553.87)"
    "bw_mem-rd-2mb (mb/s)","1012.45 (min 515.26, max 1545.36)"
    "bw_mem-rd-4mb (mb/s)","1054.65 (min 597.01, max 1566.99)"
    "bw_mem-rd-8mb (mb/s)","1088.34 (min 681.55, max 1565.56)"
    "bw_mem-rdwr-16mb (mb/s)","766.54 (min 664.45, max 848.45)"
    "bw_mem-rdwr-1mb (mb/s)","549.09 (min 392.77, max 745.16)"
    "bw_mem-rdwr-2mb (mb/s)","526.30 (min 398.84, max 656.38)"
    "bw_mem-rdwr-4mb (mb/s)","586.70 (min 423.15, max 803.45)"
    "bw_mem-rdwr-8mb (mb/s)","617.32 (min 453.10, max 827.30)"
    "bw_mem-wr-16mb (mb/s)","798.46 (min 704.88, max 893.70)"
    "bw_mem-wr-1mb (mb/s)","636.29 (min 540.83, max 745.16)"
    "bw_mem-wr-2mb (mb/s)","602.83 (min 509.16, max 740.60)"
    "bw_mem-wr-4mb (mb/s)","688.53 (min 581.82, max 803.45)"
    "bw_mem-wr-8mb (mb/s)","746.81 (min 647.51, max 847.28)"
    "bw_mmap_rd-mo-1mb (mb/s)","1245.61 (min 1133.97, max 1362.93)"
    "bw_mmap_rd-o2c-1mb (mb/s)","512.52 (min 460.62, max 605.33)"
    "bw_pipe (mb/s)","438.29 (min 384.43, max 492.81)"
    "bw_unix (mb/s)","497.81 (min 446.92, max 544.77)"
    "lat_connect (us)","112.54 (min 102.66, max 121.48)"
    "lat_ctx-2-128k (us)","39.93 (min 34.45, max 48.61)"
    "lat_ctx-2-256k (us)","138.27 (min 124.17, max 156.80)"
    "lat_ctx-4-128k (us)","87.06 (min 76.12, max 99.20)"
    "lat_ctx-4-256k (us)","174.47 (min 146.56, max 197.22)"
    "lat_fs-0k (num_files)","211.75 (min 200.00, max 226.00)"
    "lat_fs-10k (num_files)","78.50 (min 74.00, max 85.00)"
    "lat_fs-1k (num_files)","138.25 (min 131.00, max 150.00)"
    "lat_fs-4k (num_files)","133.75 (min 124.00, max 143.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","47.59 (min 43.00, max 52.39)"
    "lat_mem_rd-stride128-sz125k (ns)","6.19 (min 6.18, max 6.20)"
    "lat_mem_rd-stride128-sz250k (ns)","14.32 (min 13.04, max 15.85)"
    "lat_mem_rd-stride128-sz31k (ns)","4.32 (min 3.90, max 5.03)"
    "lat_mem_rd-stride128-sz50 (ns)","2.40 (min 2.40, max 2.41)"
    "lat_mem_rd-stride128-sz500k (ns)","43.63 (min 39.14, max 48.08)"
    "lat_mem_rd-stride128-sz62k (ns)","5.54 (min 4.93, max 5.75)"
    "lat_mmap-1m (us)","59.25 (min 56.00, max 68.00)"
    "lat_ops-double-add (ns)","3.21 (min 3.21, max 3.22)"
    "lat_ops-double-div (ns)","17.65 (min 17.64, max 17.66)"
    "lat_ops-double-mul (ns)","3.21"
    "lat_ops-float-add (ns)","3.21"
    "lat_ops-float-div (ns)","10.44 (min 10.43, max 10.44)"
    "lat_ops-float-mul (ns)","3.21"
    "lat_ops-int-add (ns)","0.80 (min 0.80, max 0.81)"
    "lat_ops-int-bit (ns)","0.53 (min 0.53, max 0.54)"
    "lat_ops-int-div (ns)","4.82 (min 4.81, max 4.82)"
    "lat_ops-int-mod (ns)","5.08 (min 5.08, max 5.09)"
    "lat_ops-int-mul (ns)","3.46 (min 3.41, max 3.50)"
    "lat_ops-int64-add (ns)","0.80"
    "lat_ops-int64-bit (ns)","0.53"
    "lat_ops-int64-div (ns)","7.63 (min 7.62, max 7.64)"
    "lat_ops-int64-mod (ns)","5.89 (min 5.88, max 5.89)"
    "lat_ops-int64-mul (ns)","3.98 (min 3.97, max 3.98)"
    "lat_pagefault (us)","1.18 (min 0.75, max 2.30)"
    "lat_pipe (us)","20.93 (min 19.12, max 22.71)"
    "lat_proc-exec (us)","1409.70 (min 1292.00, max 1534.00)"
    "lat_proc-fork (us)","1237.11 (min 1157.00, max 1332.25)"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","37.14 (min 35.32, max 41.80)"
    "lat_sem (us)","3.42 (min 2.87, max 3.73)"
    "lat_sig-catch (us)","6.33 (min 6.21, max 6.44)"
    "lat_sig-install (us)","0.68 (min 0.68, max 0.69)"
    "lat_sig-prot (us)","0.94 (min 0.79, max 1.01)"
    "lat_syscall-fstat (us)","2.04 (min 1.98, max 2.14)"
    "lat_syscall-null (us)","0.43 (min 0.42, max 0.45)"
    "lat_syscall-open (us)","463.84 (min 422.08, max 547.45)"
    "lat_syscall-read (us)","0.80 (min 0.79, max 0.81)"
    "lat_syscall-stat (us)","4.80 (min 4.70, max 4.86)"
    "lat_syscall-write (us)","0.75 (min 0.75, max 0.76)"
    "lat_tcp (us)","0.86 (min 0.85, max 0.87)"
    "lat_unix (us)","29.13 (min 25.73, max 32.78)"
    "latency_for_0.50_mb_block_size (nanosec)","43.63 (min 39.14, max 48.08)"
    "latency_for_1.00_mb_block_size (nanosec)","21.15 (min 0.00, max 52.39)"
    "pipe_bandwidth (mb\s)","438.29 (min 384.43, max 492.81)"
    "pipe_latency (microsec)","20.93 (min 19.12, max 22.71)"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","37.14 (min 35.32, max 41.80)"
    "semaphore_latency (microsec)","3.42 (min 2.87, max 3.73)"
    "signal_handler_latency (microsec)","0.68 (min 0.68, max 0.69)"
    "signal_handler_overhead (microsec)","6.33 (min 6.21, max 6.44)"
    "tcp_ip_connection_cost_to_localhost (microsec)","112.54 (min 102.66, max 121.48)"
    "tcp_latency_using_localhost (microsec)","0.86 (min 0.85, max 0.87)"


Dhrystone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed.

Please take note, different run may produce different slightly results.
This is advised to run this test multiple times in order to get maximum 
performance numbers.


Execute the benchmark with the following:

.. code-block:: console

    runDhrystone

.. csv-table:: Dhrystone Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cpu_clock (mhz)","1250.00"
    "dhrystone_per_mhz (dmips/mhz)","2.80"
    "dhrystone_per_second (dhrystonep)","6060606.00"


Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

.. code-block:: console

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "whetstone (mips)","4583.33 (min 3333.30, max 5000.00)"


Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "linpack (kflops)","517528.50 (min 515825.00, max 518787.00)"


NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "assignment (iterations)","12.65 (min 12.64, max 12.66)"
    "fourier (iterations)","17306.75 (min 17291.00, max 17321.00)"
    "fp_emulation (iterations)","182.39 (min 182.29, max 182.48)"
    "huffman (iterations)","1062.05 (min 1060.60, max 1063.30)"
    "idea (iterations)","2739.90 (min 2738.60, max 2741.50)"
    "lu_decomposition (iterations)","475.73 (min 474.19, max 476.86)"
    "neural_net (iterations)","8.64 (min 8.63, max 8.64)"
    "numeric_sort (iterations)","481.47 (min 478.51, max 483.02)"
    "string_sort (iterations)","148.13 (min 146.05, max 150.19)"


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

.. code-block:: console

    stream_c

.. csv-table:: Stream Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "add (mb/s)","1594.58 (min 1504.00, max 1858.90)"
    "copy (mb/s)","1699.98 (min 1606.40, max 1973.80)"
    "scale (mb/s)","1758.88 (min 1646.40, max 2078.20)"
    "triad (mb/s)","1575.50 (min 1487.90, max 1835.00)"




CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark\ |reg|-Pro is a comprehensive, advanced processor benchmark that works
with and enhances the market-proven industry-standard EEMBC CoreMark\ |reg|
benchmark. While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the
entire processor, adding comprehensive support for multicore technology, a
combination of integer and floating-point workloads, and data sets for utilizing
larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","37.11 (min 37.04, max 37.17)"
    "core (workloads/)","0.27"
    "coremark-pro ()","717.45 (min 701.31, max 733.58)"
    "linear_alg-mid-100x100-sp (workloads/)","13.09 (min 13.08, max 13.09)"
    "loops-all-mid-10k-sp (workloads/)","0.58 (min 0.56, max 0.60)"
    "nnet_test (workloads/)","0.96"
    "parser-125k (workloads/)","7.82 (min 7.63, max 8.00)"
    "radix2-big-64k (workloads/)","17.96 (min 16.33, max 19.60)"
    "sha-test (workloads/)","70.45 (min 68.97, max 71.94)"
    "zip-test (workloads/)","19.82 (min 19.23, max 20.41)"


.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","72.08 (min 71.43, max 72.99)"
    "core (workloads/)","0.53 (min 0.53, max 0.54)"
    "coremark-pro ()","1268.79 (min 1235.84, max 1301.82)"
    "linear_alg-mid-100x100-sp (workloads/)","26.01 (min 25.77, max 26.12)"
    "loops-all-mid-10k-sp (workloads/)","1.04 (min 0.99, max 1.08)"
    "nnet_test (workloads/)","1.92"
    "parser-125k (workloads/)","9.48 (min 9.09, max 9.95)"
    "radix2-big-64k (workloads/)","26.00 (min 23.13, max 28.59)"
    "sha-test (workloads/)","137.96 (min 135.14, max 140.85)"
    "zip-test (workloads/)","35.59 (min 34.48, max 37.04)"

MultiBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
MultiBench\ |trade| is a suite of benchmarks that allows processor and system
designers to analyze, test, and improve multicore processors. It uses three
forms of concurrency: Data decomposition: multiple threads cooperating on
achieving a unified goal and demonstrating a processor's support for fine grain
parallelism.
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

    "4m-check (workloads/)","296.68 (min 270.83, max 321.25)"
    "4m-check-reassembly (workloads/)","76.38 (min 67.66, max 85.25)"
    "4m-check-reassembly-tcp (workloads/)","43.54 (min 39.87, max 46.38)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","17.47 (min 16.30, max 18.67)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","0.92 (min 0.88, max 0.94)"
    "4m-cmykw2 (workloads/)","108.48 (min 105.15, max 111.24)"
    "4m-cmykw2-rotatew2 (workloads/)","23.64 (min 20.93, max 26.92)"
    "4m-reassembly (workloads/)","89.49 (min 78.68, max 99.30)"
    "4m-rotatew2 (workloads/)","27.33 (min 24.27, max 29.83)"
    "4m-tcp-mixed (workloads/)","102.42 (min 96.97, max 112.68)"
    "4m-x264w2 (workloads/)","0.94 (min 0.87, max 0.97)"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","17.59 (min 17.56, max 17.63)"
    "idct-4mw1 (workloads/)","17.60 (min 17.57, max 17.62)"
    "ippktcheck-4m (workloads/)","296.56 (min 271.18, max 323.88)"
    "ippktcheck-4mw1 (workloads/)","297.52 (min 271.09, max 323.75)"
    "ipres-4m (workloads/)","71.71 (min 65.25, max 78.41)"
    "ipres-4mw1 (workloads/)","71.74 (min 65.25, max 78.04)"
    "md5-4m (workloads/)","19.34 (min 17.99, max 20.55)"
    "md5-4mw1 (workloads/)","19.48 (min 18.62, max 20.34)"
    "rgbcmyk-4m (workloads/)","57.28 (min 56.67, max 57.72)"
    "rgbcmyk-4mw1 (workloads/)","57.47 (min 57.06, max 57.85)"
    "rotate-4ms1 (workloads/)","21.61 (min 19.90, max 23.25)"
    "rotate-4ms1w1 (workloads/)","21.60 (min 19.88, max 23.21)"
    "rotate-4ms64 (workloads/)","21.62 (min 19.75, max 23.31)"
    "rotate-4ms64w1 (workloads/)","21.70 (min 19.98, max 23.33)"
    "x264-4mq (workloads/)","0.50 (min 0.49, max 0.51)"
    "x264-4mqw1 (workloads/)","0.50 (min 0.49, max 0.51)"


Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62lxx_evm-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","20.39 (min 19.59, max 21.85)"

 
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

    "11025","352795.00 (min 352794.00, max 352796.00)","0.45 (min 0.27, max 0.57)"
    "16000","511993.33 (min 511992.00, max 511994.00)","0.46 (min 0.17, max 0.71)"
    "22050","705588.33 (min 705586.00, max 705590.00)","0.43 (min 0.32, max 0.59)"
    "24000","705590.00 (min 705589.00, max 705591.00)","0.45 (min 0.35, max 0.61)"
    "32000","1023986.00 (min 1023985.00, max 1023987.00)","0.57 (min 0.20, max 1.05)"
    "44100","1411179.67 (min 1411178.00, max 1411181.00)","0.62 (min 0.50, max 0.79)"
    "48000","1535977.33 (min 1535975.00, max 1535979.00)","0.58 (min 0.25, max 1.16)"
    "88200","2822348.00 (min 2822345.00, max 2822353.00)","0.99 (min 0.79, max 1.28)"
    "96000","3071925.33 (min 3071918.00, max 3071939.00)","0.78 (min 0.30, max 1.44)"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62lxx_evm-fs: Throughput (bits/sec)","am62lxx_evm-fs: CPU Load (%)"

    "11025","352944.33 (min 352943.00, max 352946.00)","0.41 (min 0.32, max 0.54)"
    "16000","512210.33 (min 512209.00, max 512212.00)","0.31 (min 0.28, max 0.33)"
    "22050","705885.33 (min 705883.00, max 705887.00)","0.34 (min 0.29, max 0.38)"
    "24000","705888.00 (min 705885.00, max 705891.00)","0.35 (min 0.32, max 0.38)"
    "32000","1024418.67 (min 1024415.00, max 1024423.00)","0.28 (min 0.21, max 0.34)"
    "44100","1411776.33 (min 1411771.00, max 1411783.00)","0.50 (min 0.45, max 0.54)"
    "48000","1536627.33 (min 1536621.00, max 1536635.00)","0.35 (min 0.25, max 0.40)"
    "88200","2823542.67 (min 2823532.00, max 2823554.00)","0.66 (min 0.62, max 0.72)"
    "96000","3073222.00 (min 3073203.00, max 3073253.00)","0.57 (min 0.31, max 0.97)"


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

The following commands were used to tune the socket buffer sizes on the DUT before running the performance tests:

.. code-block:: console

   sysctl -w net.core.rmem_default=33554432
   sysctl -w net.core.rmem_max=67108864

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TCP Bidirectional Throughput
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1215.82","98.99"

TCP Bidirectional Throughput Interrupt Pacing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1266.92","99.09"

UDP Throughput
~~~~~~~~~~~~~~

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)", "am62lxx_evm-fs: THROUGHPUT (Mbits/sec)", "am62lxx_evm-fs: Packets Per Second (kPPS)", "am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","41.23","81","77.62"
    "128","80.45","79","77.20"
    "256","145.58","71","75.10"
    "1024","571.23","70","75.05"
    "1518","810.12","69","74.91"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)", "am62lxx_evm-fs: THROUGHPUT (Mbits/sec)", "am62lxx_evm-fs: Packets Per Second (kPPS)", "am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","48.36","94","77.82"
    "128","104.64","102","76.83"
    "256","205.60","100","75.71"
    "1024","651.14","79","73.67"
    "1518","810.12","69","74.91"

|

Linux OSPI Flash Driver
-------------------------


.. rubric:: AM62XX-SK
   :name: am62xx-sk-ospi-flash-driver


.. rubric:: AM62LXX-EVM
   :name: am62lxx-evm-ospi



.. rubric:: RAW
   :name: am62lxx-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62lxx_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","164.32 (min 151.51, max 172.41)"


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

    "1m","128.75 (min 128.00, max 129.00)","9.02 (min 8.26, max 9.60)","179.50 (min 179.00, max 180.00)","8.49 (min 7.60, max 9.38)"
    "4m","127.50 (min 126.00, max 129.00)","5.61 (min 5.35, max 5.87)","179.50 (min 179.00, max 180.00)","5.08 (min 4.90, max 5.32)"
    "4k","82.60 (min 80.80, max 86.80)","57.09 (min 56.39, max 57.72)","93.55 (min 91.20, max 95.50)","57.34 (min 56.40, max 58.79)"
    "256k","123.50 (min 123.00, max 124.00)","12.38 (min 11.70, max 13.58)","178.00 (min 175.00, max 179.00)","10.72 (min 10.06, max 12.00)"


EMMC RAW FIO 1G
^^^^^^^^^^^^^^^


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "1m","127.25 (min 122.00, max 129.00)","8.01 (min 7.62, max 8.36)","180.00","7.86 (min 7.61, max 8.48)"
    "4m","129.25 (min 129.00, max 130.00)","5.27 (min 5.05, max 5.67)","180.00","4.91 (min 4.59, max 5.11)"
    "4k","95.75 (min 95.10, max 96.30)","46.36 (min 45.24, max 47.31)","97.45 (min 96.80, max 98.50)","52.29 (min 48.95, max 55.01)"
    "256k","123.75 (min 123.00, max 124.00)","10.09 (min 9.59, max 11.18)","178.25 (min 178.00, max 179.00)","9.75 (min 8.99, max 11.03)"
 

EMMC EXT4
^^^^^^^^^


.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

    "102400","104.41 (min 95.42, max 108.94)","16.22 (min 13.09, max 21.11)","178.21 (min 160.96, max 184.00)","27.73 (min 25.93, max 32.28)"
    "262144","106.56 (min 101.98, max 110.99)","12.07 (min 10.20, max 17.24)","184.53 (min 180.00, max 186.29)","26.65 (min 24.78, max 30.91)"
    "524288","106.45 (min 99.93, max 110.63)","11.90 (min 9.90, max 15.31)","182.66 (min 169.19, max 187.25)","23.44 (min 19.81, max 30.65)"
    "1048576","106.93 (min 98.85, max 110.67)","12.71 (min 9.90, max 19.17)","184.30 (min 175.45, max 187.29)","25.06 (min 20.00, max 35.90)"
    "5242880","107.52 (min 101.18, max 111.58)","12.48 (min 10.00, max 16.75)","184.96 (min 178.93, max 187.07)","25.56 (min 22.02, max 34.78)"


EMMC EXT2
^^^^^^^^^


.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT2 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT2 CPU Load (%)","am62lxx_evm-fs: Read EXT2 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT2 CPU Load (%)"

    "102400","33.01 (min 16.79, max 38.97)","14.07 (min 10.42, max 21.27)","165.14 (min 147.82, max 174.71)","31.20 (min 28.21, max 33.09)"
    "262144","50.13 (min 21.20, max 69.19)","14.13 (min 9.23, max 21.36)","175.13 (min 169.44, max 178.31)","27.00 (min 25.22, max 28.45)"
    "524288","63.01 (min 23.13, max 80.51)","14.97 (min 9.29, max 26.10)","176.63 (min 168.27, max 179.77)","25.10 (min 22.61, max 27.42)"
    "1048576","73.38 (min 25.59, max 92.38)","13.76 (min 9.13, max 21.02)","174.74 (min 162.15, max 181.26)","26.87 (min 18.92, max 33.59)"
    "5242880","86.13 (min 28.33, max 102.60)","13.55 (min 10.24, max 20.40)","180.17 (min 176.80, max 182.12)","25.10 (min 24.35, max 26.50)"
 


EMMC VFAT
^^^^^^^^^


.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write VFAT Throughput (Mbytes/sec)","am62lxx_evm-fs: Write VFAT CPU Load (%)","am62lxx_evm-fs: Read VFAT Throughput (Mbytes/sec)","am62lxx_evm-fs: Read VFAT CPU Load (%)"

    "102400","32.19 (min 15.62, max 37.35)","15.92 (min 13.41, max 19.66)","169.69 (min 156.03, max 175.00)","36.10 (min 35.09, max 36.84)"
    "262144","47.11 (min 19.54, max 60.44)","18.60 (min 14.90, max 22.38)","170.65 (min 152.30, max 177.21)","35.36 (min 33.63, max 37.96)"
    "524288","55.89 (min 21.31, max 72.09)","19.59 (min 16.46, max 27.03)","176.38 (min 173.34, max 177.55)","30.30 (min 29.82, max 30.77)"
    "1048576","61.69 (min 22.49, max 76.68)","20.18 (min 18.12, max 22.81)","173.63 (min 160.73, max 178.20)","31.52 (min 28.95, max 37.21)"
    "5242880","71.13 (min 23.14, max 84.91)","21.38 (min 19.43, max 24.22)","170.34 (min 150.85, max 177.46)","34.09 (min 31.58, max 38.41)"


UBoot EMMC Driver
-----------------


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62lxx_evm-fs: Write Throughput (Kbytes/sec)","am62lxx_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","113456.08 (min 108863.79, max 116612.10)","174763.91 (min 174297.87, max 175229.95)"
    "4000000","124546.94 (min 123419.96, max 126517.37)","178086.96"

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

    "1m","43.03 (min 42.00, max 44.20)","3.87 (min 3.57, max 4.41)","87.08 (min 86.90, max 87.20)","5.48 (min 4.85, max 6.21)"
    "4m","42.20 (min 41.60, max 42.50)","2.59 (min 2.31, max 2.91)","86.98 (min 86.80, max 87.10)","2.94 (min 2.63, max 3.46)"
    "4k","2.79 (min 2.71, max 2.88)","6.87 (min 6.30, max 7.33)","12.85 (min 12.70, max 12.90)","12.00 (min 11.02, max 13.06)"
    "256k","38.33 (min 37.60, max 39.60)","5.71 (min 5.18, max 6.05)","83.25 (min 82.60, max 83.70)","6.54 (min 5.95, max 7.34)"


MMC RAW FIO 1G
^^^^^^^^^^^^^^
 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "1m","42.93 (min 41.90, max 43.50)","3.42 (min 2.82, max 3.77)","87.88 (min 87.60, max 88.10)","4.72 (min 4.27, max 5.35)"
    "4m","42.93 (min 41.90, max 43.40)","2.62 (min 2.23, max 3.12)","87.98 (min 87.70, max 88.20)","2.95 (min 2.40, max 3.35)"
    "4k","2.79 (min 2.77, max 2.82)","4.84 (min 4.09, max 6.00)","13.03 (min 13.00, max 13.10)","10.67 (min 9.67, max 12.23)"
    "256k","37.68 (min 35.90, max 39.80)","4.89 (min 3.95, max 6.26)","83.93 (min 83.40, max 84.30)","5.58 (min 5.05, max 6.22)"



MMC EXT4
^^^^^^^^



.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "102400","10.68 (min 10.46, max 10.91)","1.81 (min 1.20, max 3.48)","10.89 (min 10.73, max 11.07)","2.26 (min 1.76, max 2.92)"
    "262144","10.65 (min 10.01, max 10.91)","1.57 (min 1.12, max 2.19)","10.93 (min 10.81, max 11.02)","2.03 (min 1.63, max 3.04)"
    "524288","10.63 (min 9.99, max 10.84)","1.46 (min 1.08, max 2.54)","10.98 (min 10.87, max 11.07)","1.48 (min 1.25, max 1.75)"
    "1048576","11.04 (min 10.62, max 11.22)","1.58 (min 1.12, max 2.63)","11.76 (min 10.96, max 12.03)","2.01 (min 1.55, max 3.08)"
    "5242880","10.79 (min 10.67, max 11.08)","1.55 (min 1.03, max 2.60)","11.99 (min 11.90, max 12.02)","2.04 (min 1.32, max 3.50)"


MMC EXT3
^^^^^^^^
 


.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "102400","30.79 (min 26.16, max 34.13)","5.76 (min 3.66, max 10.23)","68.24 (min 62.14, max 72.13)","10.42 (min 8.42, max 12.38)"
    "262144","32.47 (min 27.92, max 38.54)","4.94 (min 3.13, max 10.31)","75.55 (min 71.84, max 79.90)","11.23 (min 10.04, max 11.90)"
    "524288","32.94 (min 28.88, max 35.72)","5.24 (min 3.47, max 10.30)","79.88 (min 76.69, max 83.00)","10.97 (min 9.24, max 12.75)"
    "1048576","34.42 (min 29.17, max 38.38)","4.91 (min 3.28, max 9.69)","81.91 (min 75.54, max 84.74)","10.63 (min 8.98, max 12.59)"
    "5242880","33.37 (min 29.91, max 37.56)","4.79 (min 2.76, max 9.12)","83.56 (min 81.99, max 84.87)","10.50 (min 9.88, max 11.16)"



MMC EXT2
^^^^^^^^
 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "102400","13.40 (min 2.61, max 19.00)","7.49 (min 5.46, max 11.02)","69.03 (min 62.17, max 73.17)","12.30 (min 9.60, max 13.83)"
    "262144","21.58 (min 2.71, max 31.85)","7.29 (min 4.90, max 11.47)","74.31 (min 67.06, max 79.15)","12.32 (min 10.57, max 15.21)"
    "524288","26.37 (min 2.81, max 36.37)","6.50 (min 4.40, max 11.09)","80.34 (min 73.49, max 82.81)","11.54 (min 9.84, max 14.39)"
    "1048576","27.12 (min 2.95, max 36.66)","5.90 (min 4.33, max 10.54)","82.07 (min 76.44, max 84.19)","10.71 (min 8.98, max 11.57)"
    "5242880","29.71 (min 3.07, max 39.12)","5.02 (min 3.63, max 9.85)","80.98 (min 68.17, max 87.18)","11.65 (min 9.62, max 13.65)"
 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 



UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^



.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62lxx_evm-fs: Write Throughput (Kbytes/sec)","am62lxx_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","33703.44 (min 25283.95, max 39384.62)","82337.96 (min 81920.00, max 83591.84)"
    "800000","43057.19 (min 36247.79, max 46545.45)","87383.21 (min 87148.94, max 88086.02)"
    "1000000","44251.69 (min 40857.86, max 47352.60)","89653.03 (min 89530.05, max 90021.98)"


The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 


|

USB Driver
-------------------------
 

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62lxx_evm-fs: Throughput (MB/sec)"

    "150","39.65 (min 37.70, max 42.00)"


.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62lxx_evm-fs: Throughput (MB/sec)"

    "150","33.55 (min 31.70, max 36.20)"



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62lxx_evm-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","816797.15 (min 815551.15, max 817668.44)"
    "aes-128-cbc","16","88977.37 (min 88930.89, max 89000.25)"
    "aes-128-cbc","16384","938088.86 (min 932484.44, max 939813.55)"
    "aes-128-cbc","256","581576.38 (min 580964.95, max 581908.99)"
    "aes-128-cbc","64","277979.64 (min 277940.86, max 278005.99)"
    "aes-128-cbc","8192","930446.81 (min 929335.98, max 930968.92)"
    "aes-128-ecb","1024","897718.75 (min 894838.44, max 898706.43)"
    "aes-128-ecb","16","94859.46 (min 92759.88, max 95423.67)"
    "aes-128-ecb","16384","1068374.43 (min 1066691.24, max 1069645.82)"
    "aes-128-ecb","256","596566.63 (min 591885.91, max 598013.95)"
    "aes-128-ecb","64","260405.44 (min 256349.65, max 261659.54)"
    "aes-128-ecb","8192","1056610.17 (min 1056347.48, max 1056967.34)"
    "aes-192-cbc","1024","634277.61 (min 632684.89, max 634923.01)"
    "aes-192-cbc","16","85048.25 (min 83429.37, max 85611.75)"
    "aes-192-cbc","16384","705898.09 (min 704102.40, max 706767.53)"
    "aes-192-cbc","256","480501.56 (min 477092.01, max 481657.77)"
    "aes-192-cbc","64","250379.53 (min 246146.90, max 251754.26)"
    "aes-192-cbc","8192","701144.00 (min 699233.62, max 701688.49)"
    "aes-192-ecb","1024","794620.86 (min 791610.03, max 796341.93)"
    "aes-192-ecb","16","91410.99 (min 91327.35, max 91459.85)"
    "aes-192-ecb","16384","926582.92 (min 918563.50, max 929513.47)"
    "aes-192-ecb","256","545679.68 (min 542937.60, max 547488.00)"
    "aes-192-ecb","64","246857.22 (min 246442.62, max 247097.30)"
    "aes-192-ecb","8192","917562.44 (min 914115.24, max 919609.34)"
    "aes-256-cbc","1024","531543.59 (min 528252.25, max 532763.65)"
    "aes-256-cbc","16","82494.01 (min 81360.11, max 83413.56)"
    "aes-256-cbc","16384","582500.35 (min 581872.30, max 582980.95)"
    "aes-256-cbc","256","419024.61 (min 417079.55, max 420504.75)"
    "aes-256-cbc","64","231986.61 (min 229821.27, max 233890.37)"
    "aes-256-cbc","8192","579124.70 (min 578898.60, max 579513.00)"
    "aes-256-ecb","1024","703716.28 (min 700410.88, max 705543.85)"
    "aes-256-ecb","16","88225.54 (min 88146.11, max 88279.13)"
    "aes-256-ecb","16384","808174.66 (min 806005.42, max 809260.37)"
    "aes-256-ecb","256","489753.05 (min 488617.90, max 490522.11)"
    "aes-256-ecb","64","233904.64 (min 233706.09, max 234050.56)"
    "aes-256-ecb","8192","799985.94 (min 797537.62, max 801958.57)"
    "des3","1024","4558.51 (min 4555.09, max 4560.55)"
    "des3","16","4309.59 (min 4297.71, max 4317.90)"
    "des3","16384","4565.67"
    "des3","256","4543.59 (min 4537.94, max 4546.39)"
    "des3","64","4491.39 (min 4483.82, max 4497.05)"
    "des3","8192","4561.31 (min 4557.48, max 4562.94)"
    "md5","1024","142736.04 (min 141895.68, max 143770.97)"
    "md5","16","10164.33 (min 9873.24, max 10546.44)"
    "md5","16384","179487.81 (min 179273.73, max 179776.17)"
    "md5","256","86155.95 (min 84983.55, max 87610.71)"
    "md5","64","33204.04 (min 32109.23, max 34182.38)"
    "md5","8192","176097.96 (min 174699.86, max 176859.82)"
    "sha1","1024","324866.46 (min 321817.94, max 329407.83)"
    "sha1","16","11502.62 (min 11294.16, max 11816.92)"
    "sha1","16384","555818.46 (min 550240.26, max 558071.81)"
    "sha1","256","139574.36 (min 137170.35, max 143157.16)"
    "sha1","64","42437.61 (min 41532.54, max 43725.87)"
    "sha1","8192","532018.52 (min 530243.58, max 533487.62)"
    "sha224","1024","306683.02 (min 303283.54, max 311584.77)"
    "sha224","16","10947.69 (min 10773.89, max 11196.84)"
    "sha224","16384","525943.88 (min 523758.25, max 527712.26)"
    "sha224","256","131822.30 (min 129201.83, max 135015.59)"
    "sha224","64","40186.41 (min 39269.42, max 41471.38)"
    "sha224","8192","502658.94 (min 501011.80, max 504681.81)"
    "sha256","1024","307426.03 (min 305723.05, max 310038.19)"
    "sha256","16","10990.68 (min 10860.63, max 11175.99)"
    "sha256","16384","526128.47 (min 525145.43, max 527237.12)"
    "sha256","256","132596.31 (min 131163.05, max 134198.02)"
    "sha256","64","40352.16 (min 39886.06, max 40831.34)"
    "sha256","8192","502832.06 (min 501896.53, max 503704.23)"
    "sha512","1024","99356.06 (min 99000.66, max 99706.88)"
    "sha512","16","6824.95 (min 6770.49, max 6906.27)"
    "sha512","16384","126616.64 (min 126511.79, max 126692.01)"
    "sha512","256","58869.85 (min 58252.63, max 59386.03)"
    "sha512","64","27197.10 (min 27005.18, max 27503.57)"
    "sha512","8192","124457.78 (min 124387.33, max 124556.63)"


.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62lxx_evm-fs: CPU Load"

    "aes-128-cbc","98.40 (min 96.00, max 99.00)"
    "aes-128-ecb","99.00"
    "aes-192-cbc","99.00"
    "aes-192-ecb","99.00"
    "aes-256-cbc","98.00 (min 94.00, max 99.00)"
    "aes-256-ecb","98.60 (min 97.00, max 99.00)"
    "des3","98.80 (min 98.00, max 99.00)"
    "md5","99.00"
    "sha1","98.40 (min 96.00, max 99.00)"
    "sha224","98.80 (min 98.00, max 99.00)"
    "sha256","99.00"
    "sha386","81.40 (min 78.00, max 85.00)"
    "sha512","99.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc

|

Low Power Performance
---------------------

Power Performance
^^^^^^^^^^^^^^^^^

These are power measurements taken while the device is in various low power modes like
DSS plus DeepSleep, DeepSleep, RTC + I/O + DDR, and RTC Only.

.. csv-table:: DSS plus DeepSleep Power Performance
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.75", "44.66"
     "soc_dvdd_1v8", "1.80", "1.77"
     "soc_dvdd_3v3", "3.30", "3.64"
     "vdda_1v8", "1.80", "18.82"
     "vdd_lpddr4_pmic2", "1.10", "1.06"
     "vdd_rtc", "0.75", "0.03"
     "vdd_rtc_1v8", "1.80", "0.01"
     "Total"," ","69.99"

.. csv-table:: DeepSleep Power Performance
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.75", "6.71"
     "soc_dvdd_1v8", "1.80", "1.46"
     "soc_dvdd_3v3", "3.30", "3.44"
     "vdda_1v8", "1.80", "1.05"
     "vdd_lpddr4_pmic2", "1.10", "0.97"
     "vdd_rtc", "0.75", "0.03"
     "vdd_rtc_1v8", "1.80", "0.02"
     "Total"," ","13.67"

.. csv-table:: RTC + I/O + DDR Power Performance
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.00", "0.00"
     "soc_dvdd_1v8", "1.80", "1.36"
     "soc_dvdd_3v3", "3.30", "0.98"
     "vdda_1v8", "0.00", "0.00"
     "vdd_lpddr4_pmic2", "1.10", "1.03"
     "vdd_rtc", "0.75", "0.03"
     "vdd_rtc_1v8", "1.80", "0.01"
     "Total"," ","3.41"

.. csv-table:: RTC Only Power Performance
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.00", "0.00"
     "soc_dvdd_1v8", "0.00", "0.00"
     "soc_dvdd_3v3", "0.00", "0.00"
     "vdda_1v8", "0.00", "0.00"
     "vdd_lpddr4_pmic2", "0.00", "0.00"
     "vdd_rtc", "0.75", "0.03"
     "vdd_rtc_1v8", "1.80", "0.01"
     "Total"," ","0.05"

.. note::

   For the most accurate power measurements, use the latest TIVA firmware.

Resume Latency Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: LPM Resume Latency Performance
   :header: "Low Power Mode","Total Resume Latency (ms)"

   "RTC Only", "Full normal boot time (~seconds)"
   "RTC + I/O + DDR", "388"
   "DeepSleep", "165"
   "DSS plus DeepSleep", "499"

The performance numbers are measured without the Linux printk logs. To remove the
Linux printk logs, run the following commands in the terminal:

.. code:: console

   # Detach kernel serial console
   consoles=$(find /sys/bus/platform/devices/*.serial/ -name console)
   for console in ${consoles}; do
        echo -n N > ${console}
   done

.. note::

   The measurements shown are from using the default SDK with no extra optimizations.

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)
