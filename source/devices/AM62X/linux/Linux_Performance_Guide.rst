
======================================
 Linux 11.00 Performance Guide
======================================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
| AM62x SK       | AM62x Starter Kit rev E2 and E3 with ARM running at 1.4GHz, DDR data rate 1600 MT/S                            |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM62x LP SK    | AM62x LP Starter Kit rev E1 with ARM running at 1.25GHz, LPDDR4 data rate 1600 MT/S                            |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM62SIP SK     | AM62SIP Starter Kit rev E1 with ARM running at 1.4GHz, 512MB LPDDR4 data rate 1600 MT/S                        |
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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","32.14","29.59"
    "af_unix_socket_stream_bandwidth (MBs)","540.61","600.15"
    "bw_file_rd-io-1mb (MB/s)","880.13","954.50"
    "bw_file_rd-o2c-1mb (MB/s)","455.10","532.86"
    "bw_mem-bcopy-16mb (MB/s)","672.10","758.26"
    "bw_mem-bcopy-1mb (MB/s)","700.89","801.03"
    "bw_mem-bcopy-2mb (MB/s)","669.01","769.97"
    "bw_mem-bcopy-4mb (MB/s)","695.05","799.28"
    "bw_mem-bcopy-8mb (MB/s)","719.62","803.29"
    "bw_mem-bzero-16mb (MB/s)","1730.10","1760.56"
    "bw_mem-bzero-1mb (MB/s)","1208.67 (min 700.89, max 1716.44)","1265.57 (min 801.03, max 1730.10)"
    "bw_mem-bzero-2mb (MB/s)","1194.20 (min 669.01, max 1719.39)","1251.84 (min 769.97, max 1733.70)"
    "bw_mem-bzero-4mb (MB/s)","1206.88 (min 695.05, max 1718.71)","1268.33 (min 799.28, max 1737.37)"
    "bw_mem-bzero-8mb (MB/s)","1218.00 (min 719.62, max 1716.37)","1276.44 (min 803.29, max 1749.59)"
    "bw_mem-cp-16mb (MB/s)","393.28","455.17"
    "bw_mem-cp-1mb (MB/s)","1124.57 (min 396.25, max 1852.88)","1161.67 (min 452.08, max 1871.26)"
    "bw_mem-cp-2mb (MB/s)","1090.58 (min 391.93, max 1789.23)","1138.54 (min 459.56, max 1817.52)"
    "bw_mem-cp-4mb (MB/s)","1091.43 (min 414.25, max 1768.61)","1133.29 (min 474.72, max 1791.85)"
    "bw_mem-cp-8mb (MB/s)","1096.93 (min 433.67, max 1760.18)","1138.86 (min 501.13, max 1776.59)"
    "bw_mem-fcp-16mb (MB/s)","689.03","740.02"
    "bw_mem-fcp-1mb (MB/s)","1254.23 (min 792.02, max 1716.44)","1322.59 (min 915.08, max 1730.10)"
    "bw_mem-fcp-2mb (MB/s)","1247.97 (min 776.55, max 1719.39)","1288.20 (min 842.70, max 1733.70)"
    "bw_mem-fcp-4mb (MB/s)","1249.53 (min 780.34, max 1718.71)","1304.09 (min 870.80, max 1737.37)"
    "bw_mem-fcp-8mb (MB/s)","1254.82 (min 793.26, max 1716.37)","1297.68 (min 845.76, max 1749.59)"
    "bw_mem-frd-16mb (MB/s)","1056.11","1142.29"
    "bw_mem-frd-1mb (MB/s)","991.15 (min 792.02, max 1190.27)","1100.11 (min 915.08, max 1285.14)"
    "bw_mem-frd-2mb (MB/s)","901.98 (min 776.55, max 1027.40)","982.20 (min 842.70, max 1121.70)"
    "bw_mem-frd-4mb (MB/s)","915.04 (min 780.34, max 1049.73)","986.06 (min 870.80, max 1101.32)"
    "bw_mem-frd-8mb (MB/s)","925.87 (min 793.26, max 1058.48)","981.23 (min 845.76, max 1116.69)"
    "bw_mem-fwr-16mb (MB/s)","1737.05","1767.96"
    "bw_mem-fwr-1mb (MB/s)","1521.58 (min 1190.27, max 1852.88)","1578.20 (min 1285.14, max 1871.26)"
    "bw_mem-fwr-2mb (MB/s)","1408.32 (min 1027.40, max 1789.23)","1469.61 (min 1121.70, max 1817.52)"
    "bw_mem-fwr-4mb (MB/s)","1409.17 (min 1049.73, max 1768.61)","1446.59 (min 1101.32, max 1791.85)"
    "bw_mem-fwr-8mb (MB/s)","1409.33 (min 1058.48, max 1760.18)","1446.64 (min 1116.69, max 1776.59)"
    "bw_mem-rd-16mb (MB/s)","1055.27","1136.44"
    "bw_mem-rd-1mb (MB/s)","890.15 (min 569.88, max 1210.41)","992.58 (min 663.90, max 1321.25)"
    "bw_mem-rd-2mb (MB/s)","790.99 (min 522.47, max 1059.51)","873.95 (min 619.87, max 1128.03)"
    "bw_mem-rd-4mb (MB/s)","822.28 (min 584.11, max 1060.45)","909.27 (min 687.64, max 1130.90)"
    "bw_mem-rd-8mb (MB/s)","856.77 (min 657.57, max 1055.97)","941.08 (min 764.53, max 1117.63)"
    "bw_mem-rdwr-16mb (MB/s)","657.14","757.00"
    "bw_mem-rdwr-1mb (MB/s)","489.72 (min 396.25, max 583.18)","551.56 (min 452.08, max 651.04)"
    "bw_mem-rdwr-2mb (MB/s)","450.81 (min 391.93, max 509.68)","534.94 (min 459.56, max 610.31)"
    "bw_mem-rdwr-4mb (MB/s)","490.09 (min 414.25, max 565.93)","585.55 (min 474.72, max 696.38)"
    "bw_mem-rdwr-8mb (MB/s)","517.41 (min 433.67, max 601.14)","623.01 (min 501.13, max 744.88)"
    "bw_mem-wr-16mb (MB/s)","678.94","838.62"
    "bw_mem-wr-1mb (MB/s)","576.53 (min 569.88, max 583.18)","657.47 (min 651.04, max 663.90)"
    "bw_mem-wr-2mb (MB/s)","516.08 (min 509.68, max 522.47)","615.09 (min 610.31, max 619.87)"
    "bw_mem-wr-4mb (MB/s)","575.02 (min 565.93, max 584.11)","692.01 (min 687.64, max 696.38)"
    "bw_mem-wr-8mb (MB/s)","629.36 (min 601.14, max 657.57)","754.71 (min 744.88, max 764.53)"
    "bw_mmap_rd-mo-1mb (MB/s)","1179.25","1290.80"
    "bw_mmap_rd-o2c-1mb (MB/s)","452.42","518.76"
    "bw_pipe (MB/s)","453.11","499.59"
    "bw_unix (MB/s)","540.61","600.15"
    "lat_connect (us)","67.32","58.96"
    "lat_ctx-2-128k (us)","8.35","7.77"
    "lat_ctx-2-256k (us)","14.15","10.21"
    "lat_ctx-4-128k (us)","8.01","7.30"
    "lat_ctx-4-256k (us)","12.53","11.14"
    "lat_fs-0k (num_files)","209.00","212.00"
    "lat_fs-10k (num_files)","91.00","95.00"
    "lat_fs-1k (num_files)","126.00","144.00"
    "lat_fs-4k (num_files)","144.00","137.00"
    "lat_mem_rd-stride128-sz1000k (ns)","56.29","51.97"
    "lat_mem_rd-stride128-sz125k (ns)","6.26","5.58"
    "lat_mem_rd-stride128-sz250k (ns)","6.53","5.83"
    "lat_mem_rd-stride128-sz31k (ns)","4.69","2.16"
    "lat_mem_rd-stride128-sz50 (ns)","2.40","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","21.81","16.52"
    "lat_mem_rd-stride128-sz62k (ns)","5.85","5.24"
    "lat_mmap-1m (us)","69.00","61.00"
    "lat_ops-double-add (ns)","3.21","2.86"
    "lat_ops-double-div (ns)","17.63","15.80"
    "lat_ops-double-mul (ns)","3.21","2.86"
    "lat_ops-float-add (ns)","3.21","2.86"
    "lat_ops-float-div (ns)","10.44","9.30"
    "lat_ops-float-mul (ns)","3.21","2.86"
    "lat_ops-int-add (ns)","0.80","0.72"
    "lat_ops-int-bit (ns)","0.53","0.48"
    "lat_ops-int-div (ns)","4.81","4.30"
    "lat_ops-int-mod (ns)","5.08","4.53"
    "lat_ops-int-mul (ns)","3.45","3.08"
    "lat_ops-int64-add (ns)","0.80","0.72"
    "lat_ops-int64-bit (ns)","0.53","0.48"
    "lat_ops-int64-div (ns)","7.63","6.80"
    "lat_ops-int64-mod (ns)","5.88","5.25"
    "lat_ops-int64-mul (ns)","3.99","3.55"
    "lat_pagefault (us)","0.78","0.72"
    "lat_pipe (us)","28.50","25.19"
    "lat_proc-exec (us)","1022.40","950.00"
    "lat_proc-fork (us)","897.00","822.57"
    "lat_proc-proccall (us)","0.01","0.01"
    "lat_select (us)","38.10","33.92"
    "lat_sem (us)","3.22","2.80"
    "lat_sig-catch (us)","6.22","5.54"
    "lat_sig-install (us)","0.76","0.68"
    "lat_sig-prot (us)","1.75","0.89"
    "lat_syscall-fstat (us)","2.22","1.97"
    "lat_syscall-null (us)","0.51","0.46"
    "lat_syscall-open (us)","205.22","153.76"
    "lat_syscall-read (us)","0.88","0.79"
    "lat_syscall-stat (us)","5.35","4.82"
    "lat_syscall-write (us)","0.85","0.76"
    "lat_tcp (us)","1.02","0.91"
    "lat_unix (us)","32.14","29.59"
    "latency_for_0.50_mb_block_size (nanosec)","21.81","16.52"
    "latency_for_1.00_mb_block_size (nanosec)","28.15 (min 0.00, max 56.29)","25.98 (min 0.00, max 51.97)"
    "pipe_bandwidth (MBs)","453.11","499.59"
    "pipe_latency (microsec)","28.50","25.19"
    "procedure_call (microsec)","0.01","0.01"
    "select_on_200_tcp_fds (microsec)","38.10","33.92"
    "semaphore_latency (microsec)","3.22","2.80"
    "signal_handler_latency (microsec)","0.76","0.68"
    "signal_handler_overhead (microsec)","6.22","5.54"
    "tcp_ip_connection_cost_to_localhost (microsec)","67.32","58.96"
    "tcp_latency_using_localhost (microsec)","1.02","0.91"

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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf"

    "cpu_clock (MHz)","1250.00","1400.00"
    "dhrystone_per_mhz (DMIPS/MHz)","2.90","2.90"
    "dhrystone_per_second (DhrystoneP)","6451613.00","7142857.00"

Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf"

    "whetstone (MIPS)","5000.00","5000.00"

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf"

    "linpack (Kflops)","515361.00","576740.00"

NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf"

    "assignment (Iterations)","12.93","14.52"
    "fourier (Iterations)","20384.00","22831.00"
    "fp_emulation (Iterations)","192.52","215.63"
    "huffman (Iterations)","1057.30","1184.20"
    "idea (Iterations)","3075.50","3444.70"
    "lu_decomposition (Iterations)","473.04","530.53"
    "neural_net (Iterations)","7.73","8.66"
    "numeric_sort (Iterations)","557.39","628.41"
    "string_sort (Iterations)","146.35","163.93"

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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf"

    "add (MB/s)","1366.70","1450.00"
    "copy (MB/s)","1423.40","1637.80"
    "scale (MB/s)","1567.90","1792.50"
    "triad (MB/s)","1345.00","1478.40"

CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","37.17","41.49"
    "core (workloads/)","0.27","0.30"
    "coremark-pro ()","781.81","863.81"
    "linear_alg-mid-100x100-sp (workloads/)","13.10","14.68"
    "loops-all-mid-10k-sp (workloads/)","0.60","0.66"
    "nnet_test (workloads/)","0.97","1.09"
    "parser-125k (workloads/)","7.35","8.26"
    "radix2-big-64k (workloads/)","41.24","41.57"
    "sha-test (workloads/)","71.94","80.65"
    "zip-test (workloads/)","18.52","20.83"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","74.07","82.64"
    "core (workloads/)","0.54","0.60"
    "coremark-pro ()","1352.68","1503.32"
    "linear_alg-mid-100x100-sp (workloads/)","26.19","29.31"
    "loops-all-mid-10k-sp (workloads/)","1.03","1.15"
    "nnet_test (workloads/)","1.93","2.17"
    "parser-125k (workloads/)","11.05","11.56"
    "radix2-big-64k (workloads/)","37.88","43.39"
    "sha-test (workloads/)","142.86","158.73"
    "zip-test (workloads/)","34.48","38.46"

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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf"

    "4m-check (workloads/)","277.78","300.52"
    "4m-check-reassembly (workloads/)","58.41","63.41"
    "4m-check-reassembly-tcp (workloads/)","37.88","41.19"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","21.83","23.79"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.60","1.77"
    "4m-cmykw2 (workloads/)","180.67","199.01"
    "4m-cmykw2-rotatew2 (workloads/)","35.40","38.96"
    "4m-reassembly (workloads/)","45.45","49.38"
    "4m-rotatew2 (workloads/)","41.02","43.92"
    "4m-tcp-mixed (workloads/)","93.57","102.56"
    "4m-x264w2 (workloads/)","1.61","1.86"
    "empty-wld (workloads/)","1.00","1.00"
    "idct-4m (workloads/)","16.47","18.59"
    "idct-4mw1 (workloads/)","16.49","18.58"
    "ippktcheck-4m (workloads/)","278.15","304.77"
    "ippktcheck-4mw1 (workloads/)","274.54","304.84"
    "ipres-4m (workloads/)","59.43","64.05"
    "ipres-4mw1 (workloads/)","58.92","64.29"
    "md5-4m (workloads/)","22.84","25.21"
    "md5-4mw1 (workloads/)","22.78","25.43"
    "rgbcmyk-4m (workloads/)","56.92","63.51"
    "rgbcmyk-4mw1 (workloads/)","56.67","63.67"
    "rotate-4ms1 (workloads/)","16.71","18.14"
    "rotate-4ms1w1 (workloads/)","17.68","18.16"
    "rotate-4ms64 (workloads/)","16.86","18.29"
    "rotate-4ms64w1 (workloads/)","16.89","18.31"
    "x264-4mq (workloads/)","0.50","0.56"
    "x264-4mqw1 (workloads/)","0.50","0.56"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62xx_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","16.20 (min 15.97, max 16.41)"

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62xx_lp_sk-fs: Boot time in seconds: avg(min,max)","am62xx_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","20.38 (min 20.27, max 20.48)","16.20 (min 15.97, max 16.41)"


Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)"

    "8000","255998.00","0.23","256001.00","0.10"
    "11025","352797.00","0.21","352801.00","0.19"
    "16000","511996.00","0.15","512002.00","0.12"
    "22050","705595.00","0.37","705602.00","0.33"
    "24000","705593.00","0.34","705596.00","0.31"
    "32000","1023988.00","0.23","1023987.00","0.57"
    "44100","1411184.00","0.55","1411186.00","0.49"
    "48000","1535983.00","0.29","1535988.00","0.24"
    "88200","2822364.00","1.07","2822378.00","0.97"
    "96000","3071961.00","2.29","3071976.00","0.42"

|

Graphics SGX/RGX Driver
-------------------------

GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_lp_sk-fs: Fps","am62xx_sk-fs: Score","am62xx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","81.16","1.31"
    " GFXBench 3.x gl_trex_off","123.21","2.20"
    " GFXBench 5.x gl_5_high_off","11.20","0.17","11.66","0.18"

Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_sk-fs: Score"

    "Glmark2-DRM","51.00","61.00"
    "Glmark2-Wayland","203.00","216.00"
    "Glmark2-Wayland 1920x1080","63.00","67.00"

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

- CPSW3g: AM62x

.. rubric::  TCP Bidirectional Throughput 
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1808.53","71.31","1830.85","70.45"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1423.79","39.02","1824.36","56.36"

.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","11.19","78.00","36.85","18.00","14.71","102.00","39.11"
    "128","82.00","58.84","90.00","25.07","82.00","19.72","30.00","19.16"
    "256","210.00","147.65","88.00","30.25","210.00","162.53","97.00","38.66"
    "1024","978.00","183.54","23.00","10.13","978.00","122.05","16.00","7.09"
    "1518","1472.00","956.37","81.00","43.48","1472.00","299.10","25.00","9.72"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","1.04","7.00","0.94"
    "128","82.00","5.25","8.00","1.46","82.00","3.94","6.00","2.87"
    "256","210.00","13.94","8.00","1.68","210.00","13.61","8.00","1.80"
    "1024","978.00","936.44","120.00","42.20","978.00","65.72","8.00","2.08"
    "1518","1472.00","98.92","8.00","5.88","1472.00","98.92","8.00","2.97"

.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_lp_sk-fs: Packet Loss %","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: Packet Loss %"

    "64","18.00","33.17","230.00","45.90","73.39"
    "128","82.00","113.43","173.00","45.16","66.03","82.00","125.24","191.00","44.79","37.76"
    "256","210.00","277.06","165.00","44.13","60.85","210.00","317.12","189.00","43.41","39.20"
    "1024","978.00","936.44","120.00","42.20","0.00","978.00","932.18","119.00","41.73","0.09"
    "1518","1472.00","916.84","78.00","42.74","0.53","1472.00","922.97","78.00","41.03","0.34"

|

Linux OSPI Flash Driver
-------------------------

AM62XX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xx_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","192.31"

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xx_lp_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","29.24"

|

UBoot QSPI/OSPI Driver
-------------------------

AM62XX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"
 
    "400000","391.66","195047.62"
    "800000","391.27","248242.42"
    "1000000","392.73","273066.67"
    "2000000","390.59","284939.13"


EMMC Driver
-----------
.. important::

  The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

EMMC EXT4 FIO 1G
^^^^^^^^^^^^^^^^

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","59.80","0.08","175.00","0.08"
    "4m","60.00","0.10","175.00","0.06"
    "4k","53.00","0.06","56.40","0.05"
    "256k","60.30","0.05","174.00","0.05"

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","61.60","2.01","175.00","2.53"
    "4m","61.60","1.43","175.00","1.97"
    "4k","51.40","19.40","56.80","16.84"
    "256k","61.60","2.34","174.00","3.36"

EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","54.37 (min 51.87, max 55.19)","4.84 (min 4.31, max 5.84)","179.35","10.78"
    "262144","53.97 (min 51.33, max 54.81)","4.82 (min 4.31, max 5.77)","182.78","12.39"
    "524288","53.43 (min 50.44, max 54.44)","4.74 (min 4.38, max 5.90)","182.99","14.47"
    "1048576","53.56 (min 51.51, max 54.38)","4.71 (min 4.02, max 6.14)","182.93","12.33"
    "5242880","53.84 (min 50.47, max 54.90)","4.55 (min 4.05, max 5.55)","182.73","12.72"

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "102400","50.36 (min 47.80, max 51.29)","5.49 (min 4.78, max 6.86)","177.03","13.68"
    "262144","49.57 (min 47.01, max 50.44)","5.60 (min 5.19, max 6.88)","180.97","16.23"
    "524288","49.52 (min 46.68, max 50.44)","5.76 (min 5.29, max 7.23)","182.44","17.11"
    "1048576","49.57 (min 47.05, max 50.43)","5.87 (min 5.39, max 7.29)","182.30","17.03"
    "5242880","49.85 (min 47.38, max 50.51)","5.64 (min 5.07, max 6.91)","181.88","17.39"

EMMC VFAT
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","54.37 (min 51.87, max 55.19)","4.84 (min 4.31, max 5.84)","179.35","10.78"
    "262144","53.97 (min 51.33, max 54.81)","4.82 (min 4.31, max 5.77)","182.78","12.39"
    "524288","53.43 (min 50.44, max 54.44)","4.74 (min 4.38, max 5.90)","182.99","14.47"
    "1048576","53.56 (min 51.51, max 54.38)","4.71 (min 4.02, max 6.14)","182.93","12.33"
    "5242880","53.84 (min 50.47, max 54.90)","4.55 (min 4.05, max 5.55)","182.73","12.72"

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "102400","50.36 (min 47.80, max 51.29)","5.49 (min 4.78, max 6.86)","177.03","13.68"
    "262144","49.57 (min 47.01, max 50.44)","5.60 (min 5.19, max 6.88)","180.97","16.23"
    "524288","49.52 (min 46.68, max 50.44)","5.76 (min 5.29, max 7.23)","182.44","17.11"
    "1048576","49.57 (min 47.05, max 50.43)","5.87 (min 5.39, max 7.29)","182.30","17.03"
    "5242880","49.85 (min 47.38, max 50.51)","5.64 (min 5.07, max 6.91)","181.88","17.39"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","59254.97","170666.67"
    "4000000","59201.45","174297.87"

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","60457.56","171560.21"
    "4000000","61536.15","174297.87"

MMCSD
-----

.. important::

  The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

MMC EXT4 FIO 1G
^^^^^^^^^^^^^^^

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","43.60","1.21","87.30","1.22"
    "4m","42.30","0.79","87.10","0.93"
    "4k","2.83","1.64","12.90","4.19"
    "256k","39.70","1.44","83.60","1.65"

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.00","1.55","87.20","1.89"
    "4m","43.00","1.14","87.30","1.18"
    "4k","2.78","2.00","13.00","4.94"
    "256k","38.40","1.82","83.50","2.02"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Write Raw CPU Load (%)","am62xx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.63 (min 10.54, max 10.67)","0.98 (min 0.91, max 1.18)","10.71","0.95"
    "262144","10.31 (min 10.23, max 10.42)","1.05 (min 0.91, max 1.37)","11.22","0.96"
    "524288","10.35 (min 10.22, max 10.49)","0.99 (min 0.86, max 1.25)","11.39","0.90"
    "1048576","10.36 (min 10.29, max 10.51)","1.04 (min 0.84, max 1.40)","11.07","0.77"
    "5242880","10.77 (min 10.21, max 11.15)","1.00 (min 0.85, max 1.31)","11.97","0.83"

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write Raw CPU Load (%)","am62xx_lp_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read Raw CPU Load (%)"

    "102400","10.55 (min 10.43, max 10.61)","1.43 (min 1.28, max 1.84)","10.89","1.22"
    "262144","10.26 (min 10.15, max 10.57)","1.44 (min 1.24, max 1.79)","10.80","1.24"
    "524288","10.24 (min 10.00, max 10.50)","1.41 (min 1.17, max 1.85)","11.03","1.26"
    "1048576","10.28 (min 10.09, max 10.45)","1.48 (min 1.28, max 1.60)","11.28","1.35"
    "5242880","10.52 (min 10.32, max 10.75)","1.40 (min 1.22, max 1.94)","11.97","1.28"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 
UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","37577.98","81920.00"
    "800000","42010.26","87148.94"
    "1000000","49498.49","89530.05"

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","37577.98","83591.84"
    "800000","32899.60","87148.94"
    "1000000","49201.20","89530.05"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

USB Driver
-------------------------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)"

    "150","31.40","42.20"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)"

    "150","27.40","40.60"

|

CRYPTO Driver
-------------------------

IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","am62xx_sk-fs: Throughput (Mbps)","am62xx_sk-fs: Packets/Sec","am62xx_sk-fs: CPU Load"

    "aes128","1.20","0.00","51.33"
    "aes192","2.30","0.00","75.29"

|

Low Power Performance
-------------------------

Table:  **Deep sleep**

.. csv-table::
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","9.61"
   "vddr_core","0.85","n/a"
   "soc_dvdd_3v3","3.30","7.03"
   "soc_dvdd_1v8","1.80","2.43"
   "vdda_1v8","1.80","1.80"
   "vdd_ddr4","1.10","8.73"
   "Total"," ","29.60"

Table:  **MCU only**

.. csv-table::
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","109.78"
   "vddr_core","0.85","n/a"
   "soc_dvdd_3v3","3.30","14.48"
   "soc_dvdd_1v8","1.80","1.94"
   "vdda_1v8","1.80","10.94"
   "vdd_ddr4","1.10","8.76"
   "Total"," ","145.90"

Partial I/O Data
- All voltage rails were measured to be near 0V

.. note::

   The measurements shown are from an SK-AM62B-P1. Results may vary based off of the board variant being used.

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)
