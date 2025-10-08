
====================================
 Linux 11.01.16.03 Performance Guide
====================================

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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","30.00 (min 29.99, max 30.01)"
    "af_unix_socket_stream_bandwidth (mb\s)","1140.42 (min 1129.11, max 1151.73)"
    "bw_file_rd-io-1mb (mb/s)","1430.38 (min 1396.89, max 1463.86)"
    "bw_file_rd-o2c-1mb (mb/s)","704.15 (min 657.68, max 750.61)"
    "bw_mem-bcopy-16mb (mb/s)","1732.51 (min 1616.16, max 1848.86)"
    "bw_mem-bcopy-1mb (mb/s)","2079.23 (min 2003.28, max 2155.17)"
    "bw_mem-bcopy-2mb (mb/s)","1725.21 (min 1723.54, max 1726.87)"
    "bw_mem-bcopy-4mb (mb/s)","1671.07 (min 1634.43, max 1707.70)"
    "bw_mem-bcopy-8mb (mb/s)","1887.75 (min 1808.93, max 1966.57)"
    "bw_mem-bzero-16mb (mb/s)","7962.36 (min 7812.50, max 8112.22)"
    "bw_mem-bzero-1mb (mb/s)","5015.40 (min 2003.28, max 8108.62)"
    "bw_mem-bzero-2mb (mb/s)","4834.47 (min 1723.54, max 8094.32)"
    "bw_mem-bzero-4mb (mb/s)","4812.58 (min 1634.43, max 8104.00)"
    "bw_mem-bzero-8mb (mb/s)","4923.05 (min 1808.93, max 8106.74)"
    "bw_mem-cp-16mb (mb/s)","951.23 (min 913.71, max 988.75)"
    "bw_mem-cp-1mb (mb/s)","4570.21 (min 898.63, max 8395.16)"
    "bw_mem-cp-2mb (mb/s)","4506.43 (min 885.74, max 8248.16)"
    "bw_mem-cp-4mb (mb/s)","4505.73 (min 943.95, max 8181.35)"
    "bw_mem-cp-8mb (mb/s)","4499.51 (min 962.35, max 8150.79)"
    "bw_mem-fcp-16mb (mb/s)","1780.36 (min 1722.47, max 1838.24)"
    "bw_mem-fcp-1mb (mb/s)","4854.96 (min 1695.23, max 8108.62)"
    "bw_mem-fcp-2mb (mb/s)","4835.00 (min 1680.11, max 8094.32)"
    "bw_mem-fcp-4mb (mb/s)","4839.75 (min 1664.82, max 8104.00)"
    "bw_mem-fcp-8mb (mb/s)","4861.43 (min 1716.00, max 8106.74)"
    "bw_mem-frd-16mb (mb/s)","1949.05 (min 1886.79, max 2011.31)"
    "bw_mem-frd-1mb (mb/s)","1903.28 (min 1695.23, max 2066.89)"
    "bw_mem-frd-2mb (mb/s)","1757.28 (min 1680.11, max 1842.30)"
    "bw_mem-frd-4mb (mb/s)","1816.81 (min 1664.82, max 2002.67)"
    "bw_mem-frd-8mb (mb/s)","1792.14 (min 1716.00, max 1844.38)"
    "bw_mem-fwr-16mb (mb/s)","7986.11 (min 7838.01, max 8134.21)"
    "bw_mem-fwr-1mb (mb/s)","5128.73 (min 2029.52, max 8395.16)"
    "bw_mem-fwr-2mb (mb/s)","4938.53 (min 1734.30, max 8248.16)"
    "bw_mem-fwr-4mb (mb/s)","4968.66 (min 1813.78, max 8181.35)"
    "bw_mem-fwr-8mb (mb/s)","4909.96 (min 1795.13, max 8150.79)"
    "bw_mem-rd-16mb (mb/s)","2002.61 (min 1928.64, max 2076.57)"
    "bw_mem-rd-1mb (mb/s)","2071.05 (min 1728.91, max 2346.15)"
    "bw_mem-rd-2mb (mb/s)","1814.74 (min 1529.75, max 2051.98)"
    "bw_mem-rd-4mb (mb/s)","1865.48 (min 1684.92, max 2033.55)"
    "bw_mem-rd-8mb (mb/s)","1926.46 (min 1779.56, max 2073.08)"
    "bw_mem-rdwr-16mb (mb/s)","1940.59 (min 1860.47, max 2020.71)"
    "bw_mem-rdwr-1mb (mb/s)","1328.43 (min 898.63, max 1780.06)"
    "bw_mem-rdwr-2mb (mb/s)","1238.26 (min 885.74, max 1610.05)"
    "bw_mem-rdwr-4mb (mb/s)","1365.79 (min 943.95, max 1780.68)"
    "bw_mem-rdwr-8mb (mb/s)","1418.89 (min 962.35, max 1931.90)"
    "bw_mem-wr-16mb (mb/s)","1910.82 (min 1841.20, max 1980.44)"
    "bw_mem-wr-1mb (mb/s)","1803.48 (min 1671.31, max 2033.65)"
    "bw_mem-wr-2mb (mb/s)","1602.93 (min 1494.77, max 1777.15)"
    "bw_mem-wr-4mb (mb/s)","1751.00 (min 1684.92, max 1820.66)"
    "bw_mem-wr-8mb (mb/s)","1848.44 (min 1745.96, max 1936.34)"
    "bw_mmap_rd-mo-1mb (mb/s)","2206.82 (min 2128.79, max 2284.84)"
    "bw_mmap_rd-o2c-1mb (mb/s)","761.68 (min 727.93, max 795.42)"
    "bw_pipe (mb/s)","787.85 (min 749.46, max 826.24)"
    "bw_unix (mb/s)","1140.42 (min 1129.11, max 1151.73)"
    "lat_connect (us)","56.68 (min 56.35, max 57.00)"
    "lat_ctx-2-128k (us)","7.80 (min 7.57, max 8.02)"
    "lat_ctx-2-256k (us)","7.17 (min 6.74, max 7.59)"
    "lat_ctx-4-128k (us)","7.25 (min 7.22, max 7.27)"
    "lat_ctx-4-256k (us)","6.43 (min 6.06, max 6.80)"
    "lat_fs-0k (num_files)","233.50 (min 231.00, max 236.00)"
    "lat_fs-10k (num_files)","119.50 (min 116.00, max 123.00)"
    "lat_fs-1k (num_files)","167.50 (min 163.00, max 172.00)"
    "lat_fs-4k (num_files)","160.50 (min 146.00, max 175.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","30.43 (min 29.44, max 31.43)"
    "lat_mem_rd-stride128-sz125k (ns)","5.58 (min 5.55, max 5.61)"
    "lat_mem_rd-stride128-sz250k (ns)","5.83 (min 5.83, max 5.84)"
    "lat_mem_rd-stride128-sz31k (ns)","2.90 (min 2.15, max 3.65)"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","12.11 (min 10.58, max 13.64)"
    "lat_mem_rd-stride128-sz62k (ns)","4.90 (min 4.54, max 5.25)"
    "lat_mmap-1m (us)","51.00"
    "lat_ops-double-add (ns)","2.86"
    "lat_ops-double-div (ns)","15.74 (min 15.73, max 15.74)"
    "lat_ops-double-mul (ns)","2.87 (min 2.86, max 2.87)"
    "lat_ops-float-add (ns)","2.86"
    "lat_ops-float-div (ns)","9.30"
    "lat_ops-float-mul (ns)","2.86"
    "lat_ops-int-add (ns)","0.72"
    "lat_ops-int-bit (ns)","0.48"
    "lat_ops-int-div (ns)","4.29"
    "lat_ops-int-mod (ns)","4.53"
    "lat_ops-int-mul (ns)","3.07"
    "lat_ops-int64-add (ns)","0.72"
    "lat_ops-int64-bit (ns)","0.48"
    "lat_ops-int64-div (ns)","6.80"
    "lat_ops-int64-mod (ns)","5.25"
    "lat_ops-int64-mul (ns)","3.55"
    "lat_pagefault (us)","0.51 (min 0.50, max 0.52)"
    "lat_pipe (us)","25.78 (min 25.77, max 25.79)"
    "lat_proc-exec (us)","706.31 (min 685.11, max 727.50)"
    "lat_proc-fork (us)","615.95 (min 598.78, max 633.13)"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","33.79 (min 33.79, max 33.80)"
    "lat_sem (us)","2.68 (min 2.48, max 2.89)"
    "lat_sig-catch (us)","5.45 (min 5.43, max 5.48)"
    "lat_sig-install (us)","0.67"
    "lat_sig-prot (us)","0.52 (min 0.51, max 0.54)"
    "lat_syscall-fstat (us)","1.98"
    "lat_syscall-null (us)","0.47"
    "lat_syscall-open (us)","147.83 (min 133.40, max 162.26)"
    "lat_syscall-read (us)","0.82 (min 0.81, max 0.82)"
    "lat_syscall-stat (us)","4.67 (min 4.64, max 4.71)"
    "lat_syscall-write (us)","0.76 (min 0.75, max 0.77)"
    "lat_tcp (us)","1.00 (min 0.98, max 1.02)"
    "lat_unix (us)","30.00 (min 29.99, max 30.01)"
    "latency_for_0.50_mb_block_size (nanosec)","12.11 (min 10.58, max 13.64)"
    "latency_for_1.00_mb_block_size (nanosec)","15.22 (min 0.00, max 31.43)"
    "pipe_bandwidth (mb\s)","787.85 (min 749.46, max 826.24)"
    "pipe_latency (microsec)","25.78 (min 25.77, max 25.79)"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","33.79 (min 33.79, max 33.80)"
    "semaphore_latency (microsec)","2.68 (min 2.48, max 2.89)"
    "signal_handler_latency (microsec)","0.67"
    "signal_handler_overhead (microsec)","5.45 (min 5.43, max 5.48)"
    "tcp_ip_connection_cost_to_localhost (microsec)","56.68 (min 56.35, max 57.00)"
    "tcp_latency_using_localhost (microsec)","1.00 (min 0.98, max 1.02)"



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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cpu_clock (mhz)","1400.00"
    "dhrystone_per_mhz (dmips/mhz)","2.95 (min 2.90, max 3.00)"
    "dhrystone_per_second (dhrystonep)","7275132.25 (min 7142857.00, max 7407407.50)"


Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "whetstone (mips)","7500.00 (min 5000.00, max 10000.00)"


Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "linpack (kflops)","575872.00 (min 574616.00, max 577128.00)"


NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "assignment (iterations)","14.47 (min 14.46, max 14.48)"
    "fourier (iterations)","22831.50 (min 22831.00, max 22832.00)"
    "fp_emulation (iterations)","215.64"
    "huffman (iterations)","1184.10 (min 1183.90, max 1184.30)"
    "idea (iterations)","3444.85 (min 3444.80, max 3444.90)"
    "lu_decomposition (iterations)","530.01 (min 529.95, max 530.06)"
    "neural_net (iterations)","8.65"
    "numeric_sort (iterations)","628.51 (min 628.05, max 628.96)"
    "string_sort (iterations)","163.94"


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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "add (mb/s)","2693.95 (min 2693.70, max 2694.20)"
    "copy (mb/s)","3756.90 (min 3756.30, max 3757.50)"
    "scale (mb/s)","3484.05 (min 3482.60, max 3485.50)"
    "triad (mb/s)","2400.10 (min 2397.20, max 2403.00)"


CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","42.19"
    "core (workloads/)","0.30"
    "coremark-pro ()","915.19 (min 905.27, max 925.11)"
    "linear_alg-mid-100x100-sp (workloads/)","14.68 (min 14.67, max 14.68)"
    "loops-all-mid-10k-sp (workloads/)","0.71"
    "nnet_test (workloads/)","1.09"
    "parser-125k (workloads/)","8.81 (min 8.77, max 8.85)"
    "radix2-big-64k (workloads/)","57.20 (min 51.86, max 62.54)"
    "sha-test (workloads/)","81.31 (min 80.65, max 81.97)"
    "zip-test (workloads/)","21.74"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","82.99 (min 82.64, max 83.33)"
    "core (workloads/)","0.60"
    "coremark-pro ()","1673.63 (min 1669.43, max 1677.83)"
    "linear_alg-mid-100x100-sp (workloads/)","29.37 (min 29.34, max 29.39)"
    "loops-all-mid-10k-sp (workloads/)","1.31 (min 1.30, max 1.32)"
    "nnet_test (workloads/)","2.17"
    "parser-125k (workloads/)","13.95 (min 13.51, max 14.39)"
    "radix2-big-64k (workloads/)","72.78 (min 71.34, max 74.21)"
    "sha-test (workloads/)","162.61 (min 161.29, max 163.93)"
    "zip-test (workloads/)","42.55"



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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "4m-check (workloads/)","411.93"
    "4m-check-reassembly (workloads/)","119.76"
    "4m-check-reassembly-tcp (workloads/)","59.24"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","33.15"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.87"
    "4m-cmykw2 (workloads/)","246.31"
    "4m-cmykw2-rotatew2 (workloads/)","49.75"
    "4m-reassembly (workloads/)","83.13"
    "4m-rotatew2 (workloads/)","52.66"
    "4m-tcp-mixed (workloads/)","118.52"
    "4m-x264w2 (workloads/)","1.95"
    "idct-4m (workloads/)","19.24"
    "idct-4mw1 (workloads/)","19.22"
    "ippktcheck-4m (workloads/)","415.01"
    "ippktcheck-4mw1 (workloads/)","413.98"
    "ipres-4m (workloads/)","112.11"
    "ipres-4mw1 (workloads/)","110.78"
    "md5-4m (workloads/)","27.67"
    "md5-4mw1 (workloads/)","27.21"
    "rgbcmyk-4m (workloads/)","65.88"
    "rgbcmyk-4mw1 (workloads/)","65.81"
    "rotate-4ms1 (workloads/)","23.44"
    "rotate-4ms1w1 (workloads/)","23.42"
    "rotate-4ms64 (workloads/)","23.71"
    "rotate-4ms64w1 (workloads/)","23.71"
    "x264-4mq (workloads/)","0.58"
    "x264-4mqw1 (workloads/)","0.58"



Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62pxx_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","13.40 (min 13.11, max 13.80)"

 

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.



|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62pxx_sk-fs: Throughput (bits/sec)","am62pxx_sk-fs: CPU Load (%)"

    "11025","352799.00 (min 352798.00, max 352800.00)","0.10 (min 0.09, max 0.10)"
    "16000","511999.00 (min 511998.00, max 512000.00)","0.08 (min 0.06, max 0.09)"
    "22050","705590.00 (min 705587.00, max 705593.00)","0.12 (min 0.11, max 0.13)"
    "24000","705594.00 (min 705593.00, max 705595.00)","0.14 (min 0.12, max 0.16)"
    "32000","1023994.50 (min 1023994.00, max 1023995.00)","0.10 (min 0.09, max 0.11)"
    "44100","1411192.50 (min 1411192.00, max 1411193.00)","0.21 (min 0.20, max 0.21)"
    "48000","1535993.00","0.16 (min 0.14, max 0.17)"
    "88200","2822383.50 (min 2822383.00, max 2822384.00)","0.36 (min 0.34, max 0.38)"
    "96000","3071979.00 (min 3071976.00, max 3071982.00)","0.15 (min 0.13, max 0.17)"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62pxx_sk-fs: Throughput (bits/sec)","am62pxx_sk-fs: CPU Load (%)"

    "11025","352945.00 (min 352944.00, max 352946.00)","0.09"
    "16000","512211.50 (min 512210.00, max 512213.00)","0.08"
    "22050","705861.00 (min 705832.00, max 705890.00)","0.12"
    "24000","705890.00 (min 705888.00, max 705892.00)","0.12"
    "32000","551611.50 (min 78799.00, max 1024424.00)","0.08 (min 0.07, max 0.09)"
    "44100","1411538.00 (min 1411523.00, max 1411553.00)","0.17 (min 0.16, max 0.17)"
    "48000","1536631.50 (min 1536627.00, max 1536636.00)","0.13 (min 0.11, max 0.14)"
    "88200","2823566.00","0.31"



|

Graphics SGX/RGX Driver
-------------------------
 


GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62pxx_sk-fs: Score","am62pxx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","907.49 (min 904.94, max 910.05)","14.64 (min 14.60, max 14.68)"
    " GFXBench 3.x gl_trex_off","1587.44 (min 1586.08, max 1588.81)","28.35 (min 28.32, max 28.37)"
    " GFXBench 4.x gl_4_off","260.73 (min 260.25, max 261.21)","4.41 (min 4.40, max 4.42)"
    " GFXBench 5.x gl_5_high_off","114.18 (min 113.75, max 114.61)","1.78 (min 1.77, max 1.78)"




Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62pxx_sk-fs: Score"

    "Glmark2-DRM","331.50 (min 308.00, max 355.00)"
    "Glmark2-Wayland","738.00 (min 737.00, max 739.00)"


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
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1797.44 (min 1756.87, max 1838.01)","63.06 (min 62.52, max 63.60)"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1785.70 (min 1694.75, max 1876.65)","37.27 (min 35.52, max 39.01)"




.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62pxx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: Packets Per Second (kPPS)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","56.49 (min 56.42, max 56.55)","110.00","40.52 (min 40.38, max 40.65)"
    "128","","110.21 (min 110.19, max 110.22)","108.00","40.07 (min 40.03, max 40.10)"
    "256","","220.01 (min 219.29, max 220.73)","107.50 (min 107.00, max 108.00)","39.97 (min 39.60, max 40.33)"
    "1024","","861.68 (min 859.04, max 864.32)","105.50 (min 105.00, max 106.00)","40.73 (min 40.59, max 40.87)"
    "1518","","846.42 (min 840.54, max 852.30)","69.50 (min 69.00, max 70.00)","37.22 (min 37.16, max 37.28)"


|

Linux OSPI Flash Driver
-------------------------


AM62PXX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Write UBIFS CPU Load (%)","am62pxx_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.28)","29.48 (min 24.79, max 33.84)","28.51 (min 28.45, max 28.57)","9.90 (min 6.90, max 12.90)"
    "262144","0.14 (min 0.10, max 0.18)","29.48 (min 27.27, max 31.62)","28.46 (min 28.38, max 28.54)","6.73 (min 3.45, max 10.00)"
    "524288","0.14 (min 0.10, max 0.19)","29.39 (min 26.96, max 31.81)","28.23 (min 28.10, max 28.36)","8.34 (min 6.67, max 10.00)"
    "1048576","0.14 (min 0.10, max 0.18)","29.92 (min 26.75, max 34.88)","28.09 (min 28.07, max 28.11)","9.68"

RAW
"""""""""""""""""""""""""""

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

    "1m","91.85 (min 90.70, max 93.00)","1.62 (min 1.60, max 1.63)","287.00 (min 285.00, max 289.00)","2.73 (min 2.65, max 2.81)"
    "4m","97.50 (min 96.30, max 98.70)","1.12 (min 1.07, max 1.16)","288.00 (min 287.00, max 289.00)","2.14 (min 2.04, max 2.24)"
    "4k","79.35 (min 79.20, max 79.50)","25.76 (min 25.60, max 25.92)","89.90 (min 89.20, max 90.60)","20.93 (min 20.67, max 21.18)"
    "256k","91.85 (min 90.50, max 93.20)","2.08 (min 1.97, max 2.18)","290.50 (min 287.00, max 294.00)","4.03 (min 3.96, max 4.09)"



EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "1m","90.00 (min 89.90, max 90.10)","1.36 (min 1.33, max 1.38)","293.00 (min 292.00, max 294.00)","2.61 (min 2.52, max 2.69)"
    "4m","97.10 (min 97.00, max 97.20)","1.03 (min 1.01, max 1.05)","293.00 (min 292.00, max 294.00)","2.07 (min 2.05, max 2.08)"
    "4k","77.15 (min 76.80, max 77.50)","19.09 (min 19.07, max 19.11)","93.05 (min 93.00, max 93.10)","20.30 (min 19.97, max 20.62)"
    "256k","90.25 (min 90.10, max 90.40)","1.76 (min 1.74, max 1.77)","293.00 (min 292.00, max 294.00)","3.80 (min 3.70, max 3.89)"



EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","84.05 (min 80.55, max 87.86)","5.95 (min 4.96, max 8.05)","178.95 (min 178.88, max 179.02)","8.77 (min 6.99, max 10.55)"
    "262144","82.22 (min 55.62, max 88.94)","5.71 (min 3.58, max 7.89)","181.33 (min 181.30, max 181.36)","8.53 (min 8.33, max 8.73)"
    "524288","76.21 (min 48.83, max 88.87)","5.38 (min 3.31, max 8.06)","182.11 (min 182.06, max 182.16)","10.34 (min 6.70, max 13.97)"
    "1048576","74.12 (min 49.72, max 89.67)","4.95 (min 2.92, max 7.84)","177.80 (min 173.33, max 182.26)","8.91 (min 6.75, max 11.06)"
    "5242880","68.44 (min 48.58, max 88.72)","4.75 (min 2.96, max 7.38)","182.00 (min 181.88, max 182.12)","8.88 (min 7.49, max 10.26)"


EMMC EXT2
^^^^^^^^^


.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT2 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT2 CPU Load (%)","am62pxx_sk-fs: Read EXT2 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT2 CPU Load (%)"

    "102400","46.66 (min 23.83, max 53.41)","6.19 (min 4.83, max 10.22)","206.14 (min 200.43, max 211.85)","10.42 (min 10.26, max 10.58)"
    "262144","54.96 (min 26.84, max 64.68)","6.91 (min 5.78, max 10.03)","291.88 (min 291.15, max 292.60)","15.85 (min 15.49, max 16.20)"
    "524288","64.23 (min 28.34, max 76.47)","6.02 (min 4.83, max 9.01)","296.85 (min 296.22, max 297.48)","14.93 (min 13.77, max 16.08)"
    "1048576","65.71 (min 28.66, max 78.49)","6.38 (min 4.49, max 8.85)","294.03 (min 293.85, max 294.20)","16.03 (min 15.97, max 16.08)"
    "5242880","70.98 (min 28.72, max 85.64)","6.08 (min 4.55, max 8.90)","295.09 (min 295.08, max 295.10)","14.73 (min 14.18, max 15.28)"


EMMC VFAT
^^^^^^^^^
 

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Write VFAT CPU Load (%)","am62pxx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Read VFAT CPU Load (%)"

    "102400","40.66 (min 11.88, max 52.29)","5.07 (min 3.58, max 6.10)","208.81 (min 208.70, max 208.92)","10.36 (min 10.10, max 10.61)"
    "262144","44.56 (min 12.48, max 62.93)","5.60 (min 4.40, max 7.81)","286.09 (min 284.98, max 287.19)","15.45 (min 14.56, max 16.33)"
    "524288","50.91 (min 12.75, max 73.51)","5.09 (min 3.68, max 7.64)","287.77 (min 287.04, max 288.49)","14.77 (min 13.89, max 15.65)"
    "1048576","55.28 (min 12.88, max 75.16)","5.00 (min 3.83, max 6.45)","287.39 (min 286.35, max 288.43)","14.48 (min 14.38, max 14.58)"
    "5242880","56.43 (min 13.03, max 81.90)","5.02 (min 3.73, max 6.68)","287.22 (min 287.00, max 287.43)","14.78 (min 14.48, max 15.07)"


UBoot EMMC Driver
-----------------
 

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","99571.30 (min 97523.81, max 103044.03)","234574.66 (min 172463.16, max 277694.92)"
    "4000000","97976.11 (min 96946.75, max 100054.96)","260546.71 (min 172918.21, max 300623.85)"

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

    "1m","41.80 (min 41.60, max 42.00)","1.01","87.30","1.38 (min 1.32, max 1.44)"
    "4m","41.95 (min 41.20, max 42.70)","0.75 (min 0.74, max 0.76)","87.15 (min 87.10, max 87.20)","0.97 (min 0.96, max 0.97)"
    "4k","2.80 (min 2.78, max 2.83)","1.70 (min 1.66, max 1.73)","12.95 (min 12.90, max 13.00)","4.24 (min 4.17, max 4.30)"
    "256k","37.85 (min 37.20, max 38.50)","1.26 (min 1.22, max 1.30)","83.85 (min 83.80, max 83.90)","1.63 (min 1.60, max 1.65)"



MMC RAW FIO 1G
^^^^^^^^^^^^^^


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "1m","44.20 (min 43.70, max 44.70)","0.96 (min 0.93, max 0.98)","88.20","1.18 (min 1.15, max 1.20)"
    "4m","43.90 (min 43.70, max 44.10)","0.75 (min 0.72, max 0.77)","88.20","0.92 (min 0.88, max 0.96)"
    "4k","2.81","1.35 (min 1.33, max 1.36)","13.05 (min 13.00, max 13.10)","3.95 (min 3.87, max 4.03)"
    "256k","39.70 (min 38.30, max 41.10)","1.09 (min 1.05, max 1.12)","84.40 (min 84.30, max 84.50)","1.48 (min 1.47, max 1.49)"

MMC EXT4
^^^^^^^^


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.86 (min 10.44, max 11.24)","0.84 (min 0.72, max 1.12)","11.82","0.71"
    "262144","10.63 (min 10.46, max 10.79)","0.86 (min 0.67, max 1.15)","11.08 (min 11.00, max 11.16)","0.78 (min 0.71, max 0.85)"
    "524288","10.41 (min 10.31, max 10.54)","0.79 (min 0.63, max 1.08)","11.29 (min 11.05, max 11.52)","0.69 (min 0.63, max 0.74)"
    "1048576","10.54 (min 10.25, max 10.84)","0.85 (min 0.70, max 1.13)","11.05 (min 11.02, max 11.07)","0.66"
    "5242880","10.52 (min 10.28, max 10.72)","0.84 (min 0.69, max 1.16)","11.30 (min 11.08, max 11.52)","0.67 (min 0.63, max 0.71)"

 


MMC EXT3
^^^^^^^^


.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","39.34 (min 33.29, max 41.31)","3.58 (min 2.85, max 6.03)","78.75 (min 77.10, max 80.39)","5.35 (min 4.42, max 6.27)"
    "262144","38.50 (min 33.14, max 41.93)","3.38 (min 2.42, max 6.09)","84.29 (min 82.02, max 86.55)","5.69 (min 5.36, max 6.02)"
    "524288","36.83 (min 32.58, max 38.61)","3.34 (min 2.45, max 5.43)","90.39 (min 90.30, max 90.48)","5.26 (min 5.16, max 5.36)"
    "1048576","38.74 (min 32.47, max 41.44)","3.34 (min 2.37, max 5.98)","90.10 (min 89.80, max 90.39)","5.04 (min 4.93, max 5.15)"
    "5242880","38.13 (min 33.25, max 41.45)","3.28 (min 2.33, max 5.60)","90.13 (min 89.93, max 90.33)","5.04 (min 4.73, max 5.34)"



MMC EXT2
^^^^^^^^


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","17.50 (min 3.49, max 21.20)","2.52 (min 2.13, max 2.86)","80.73 (min 80.69, max 80.77)","4.44 (min 4.26, max 4.62)"
    "262144","30.77 (min 3.87, max 39.22)","3.32 (min 2.15, max 3.89)","86.89 (min 86.64, max 87.13)","5.18 (min 4.96, max 5.39)"
    "524288","35.27 (min 3.96, max 44.35)","3.26 (min 2.12, max 4.01)","90.33 (min 90.28, max 90.37)","4.95 (min 4.74, max 5.16)"
    "1048576","34.26 (min 4.01, max 43.23)","2.82 (min 1.88, max 3.57)","90.69 (min 90.61, max 90.76)","4.97 (min 4.55, max 5.39)"
    "5242880","33.95 (min 4.03, max 42.47)","2.61 (min 1.97, max 3.23)","87.86 (min 85.16, max 90.55)","5.11 (min 4.75, max 5.47)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","36597.69 (min 35617.39, max 37577.98)","82755.92 (min 81920.00, max 83591.84)"
    "800000","38524.54 (min 32768.00, max 44281.08)","86690.26 (min 86231.58, max 87148.94)"
    "1000000","45309.46 (min 41269.52, max 49349.40)","89530.05"

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)



|

USB Driver
-------------------------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","38.95 (min 33.90, max 44.00)"




.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","32.50 (min 27.90, max 37.10)"

|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62pxx_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","22944.60 (min 22896.64, max 22992.55)"
    "aes-128-cbc","16","411.11 (min 409.66, max 412.57)"
    "aes-128-cbc","16384","84309.33 (min 83656.70, max 84961.96)"
    "aes-128-cbc","256","6772.78 (min 6760.02, max 6785.54)"
    "aes-128-cbc","64","1800.77 (min 1799.74, max 1801.79)"
    "aes-128-cbc","8192","70837.59 (min 70579.54, max 71095.64)"
    "aes-128-ecb","1024","23454.04 (min 23428.44, max 23479.64)"
    "aes-128-ecb","16","419.04 (min 418.92, max 419.16)"
    "aes-128-ecb","16384","87053.65 (min 86736.90, max 87370.41)"
    "aes-128-ecb","256","6953.86 (min 6949.72, max 6957.99)"
    "aes-128-ecb","64","1843.58 (min 1842.69, max 1844.48)"
    "aes-128-ecb","8192","73486.34 (min 73394.86, max 73577.81)"
    "aes-192-cbc","1024","22431.23 (min 22398.63, max 22463.83)"
    "aes-192-cbc","16","412.38 (min 411.57, max 413.18)"
    "aes-192-cbc","16384","76283.90 (min 75776.00, max 76791.81)"
    "aes-192-cbc","256","6698.28 (min 6681.17, max 6715.39)"
    "aes-192-cbc","64","1806.75 (min 1803.65, max 1809.86)"
    "aes-192-cbc","8192","65279.32 (min 65077.25, max 65481.39)"
    "aes-192-ecb","1024","22946.13 (min 22890.50, max 23001.77)"
    "aes-192-ecb","16","418.73 (min 417.76, max 419.71)"
    "aes-192-ecb","16384","78452.05 (min 78386.52, max 78517.59)"
    "aes-192-ecb","256","6863.70 (min 6831.53, max 6895.87)"
    "aes-192-ecb","64","1837.65 (min 1836.99, max 1838.31)"
    "aes-192-ecb","8192","67362.82 (min 67193.51, max 67532.12)"
    "aes-256-cbc","1024","21829.12 (min 21806.08, max 21852.16)"
    "aes-256-cbc","16","413.87 (min 412.79, max 414.94)"
    "aes-256-cbc","16384","69869.57 (min 69637.46, max 70101.67)"
    "aes-256-cbc","256","6656.51 (min 6655.06, max 6657.96)"
    "aes-256-cbc","64","1801.61 (min 1798.98, max 1804.25)"
    "aes-256-cbc","8192","60593.49 (min 60481.54, max 60705.45)"
    "aes-256-ecb","1024","22341.97 (min 22245.72, max 22438.23)"
    "aes-256-ecb","16","419.94 (min 419.53, max 420.34)"
    "aes-256-ecb","16384","71841.11 (min 71483.39, max 72198.83)"
    "aes-256-ecb","256","6813.27 (min 6799.96, max 6826.58)"
    "aes-256-ecb","64","1831.33 (min 1828.18, max 1834.47)"
    "aes-256-ecb","8192","61456.38 (min 61265.24, max 61647.53)"
    "sha256","1024","38186.15 (min 38049.11, max 38323.20)"
    "sha256","16","631.57 (min 630.11, max 633.04)"
    "sha256","16384","298710.36 (min 298647.55, max 298773.16)"
    "sha256","256","9972.44 (min 9929.05, max 10015.83)"
    "sha256","64","2497.73 (min 2488.73, max 2506.73)"
    "sha256","8192","202798.42 (min 202312.36, max 203284.48)"
    "sha512","1024","26188.97 (min 26184.36, max 26193.58)"
    "sha512","16","612.37 (min 610.09, max 614.65)"
    "sha512","16384","68296.70 (min 68277.59, max 68315.82)"
    "sha512","256","8686.17 (min 8669.53, max 8702.81)"
    "sha512","64","2451.79 (min 2442.45, max 2461.12)"
    "sha512","8192","61581.99 (min 61562.88, max 61601.11)"



.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62pxx_sk-fs: CPU Load"

    "aes-128-cbc","30.50 (min 30.00, max 31.00)"
    "aes-128-ecb","32.00"
    "aes-192-cbc","30.50 (min 30.00, max 31.00)"
    "aes-192-ecb","31.00"
    "aes-256-cbc","30.00"
    "aes-256-ecb","30.50 (min 30.00, max 31.00)"
    "sha256","95.00"
    "sha512","94.50 (min 93.00, max 96.00)"


 
Low Power Performance
---------------------

Power Performance
^^^^^^^^^^^^^^^^^

.. csv-table:: Deep Sleep Power Performance
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","14.36"
   "vddr_core","0.85","1.03"
   "soc_dvdd_3v3","3.30","6.02"
   "soc_dvdd_1v8","1.80","2.78"
   "vdda_1v8","1.80","67.41"
   "vdd_lpddr4","1.10","4.92"
   "Total"," ","96.52"

.. csv-table:: MCU Only Power Performance
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","213.68"
   "vddr_core","0.85","2.79"
   "soc_dvdd_3v3","3.30","7.52"
   "soc_dvdd_1v8","1.80","2.85"
   "vdda_1v8","1.80","75.91"
   "vdd_lpddr4","1.10","5.12"
   "Total"," ","307.88"

Partial I/O Data
- All voltage rails were measured to be near 0V

.. note::

   The power consumption on the vdda_1v8 rail is not indicitive of the SoC's power consumption due to an oscillator on the rail
   that has significant current consumption.

.. note::

   The measurements shown are from an AM62Px SK rev E1-1. Results may vary based off of the board revision being used.

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)

Resume Latency Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: LPM Resume Latency Performance
   :header: "Low Power Mode","Total Resume Latency (ms)"

   "I/O Only + DDR", "716.68"
   "Deep Sleep", "150.50"
   "MCU Only", "94.06"

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
