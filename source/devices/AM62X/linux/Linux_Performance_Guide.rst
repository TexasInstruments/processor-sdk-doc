
==============================
 Linux 11.01 Performance Guide
==============================

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
http://e2e.ti.com/ or http://support.ti.com/


System Benchmarks
-----------------


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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","33.72","29.04","33.12"
    "af_unix_socket_stream_bandwidth (MBs)","549.13","599.28","654.14"
    "bw_file_rd-io-1mb (MB/s)","886.84","947.27","882.30"
    "bw_file_rd-o2c-1mb (MB/s)","488.68","501.67","478.39"
    "bw_mem-bcopy-16mb (MB/s)","702.31","758.69","750.47"
    "bw_mem-bcopy-1mb (MB/s)","731.40","810.64","790.83"
    "bw_mem-bcopy-2mb (MB/s)","701.26","754.34","724.51"
    "bw_mem-bcopy-4mb (MB/s)","725.16","797.77","742.25"
    "bw_mem-bcopy-8mb (MB/s)","737.40","788.49","726.02"
    "bw_mem-bzero-16mb (MB/s)","1777.58","1757.08","1747.87"
    "bw_mem-bzero-1mb (MB/s)","1249.56 (min 731.40, max 1767.72)","1273.23 (min 810.64, max 1735.81)","1259.27 (min 790.83, max 1727.71)"
    "bw_mem-bzero-2mb (MB/s)","1234.34 (min 701.26, max 1767.41)","1244.32 (min 754.34, max 1734.30)","1223.29 (min 724.51, max 1722.06)"
    "bw_mem-bzero-4mb (MB/s)","1247.54 (min 725.16, max 1769.91)","1274.42 (min 797.77, max 1751.06)","1240.19 (min 742.25, max 1738.12)"
    "bw_mem-bzero-8mb (MB/s)","1251.41 (min 737.40, max 1765.42)","1266.66 (min 788.49, max 1744.82)","1237.62 (min 726.02, max 1749.21)"
    "bw_mem-cp-16mb (MB/s)","408.49","454.88","449.99"
    "bw_mem-cp-1mb (MB/s)","1146.98 (min 392.46, max 1901.50)","1153.53 (min 430.17, max 1876.88)","1156.08 (min 446.83, max 1865.32)"
    "bw_mem-cp-2mb (MB/s)","1126.54 (min 410.09, max 1842.98)","1128.29 (min 438.07, max 1818.51)","1103.62 (min 412.54, max 1794.69)"
    "bw_mem-cp-4mb (MB/s)","1103.66 (min 388.31, max 1819.01)","1136.35 (min 485.38, max 1787.31)","1104.23 (min 437.49, max 1770.96)"
    "bw_mem-cp-8mb (MB/s)","1122.78 (min 439.68, max 1805.87)","1125.20 (min 477.73, max 1772.66)","1079.77 (min 399.36, max 1760.18)"
    "bw_mem-fcp-16mb (MB/s)","696.89","736.95","808.28"
    "bw_mem-fcp-1mb (MB/s)","1292.16 (min 816.59, max 1767.72)","1310.31 (min 884.80, max 1735.81)","1264.43 (min 801.15, max 1727.71)"
    "bw_mem-fcp-2mb (MB/s)","1260.50 (min 753.58, max 1767.41)","1303.26 (min 872.22, max 1734.30)","1260.02 (min 797.98, max 1722.06)"
    "bw_mem-fcp-4mb (MB/s)","1282.65 (min 795.39, max 1769.91)","1316.69 (min 882.32, max 1751.06)","1256.21 (min 774.29, max 1738.12)"
    "bw_mem-fcp-8mb (MB/s)","1283.72 (min 802.01, max 1765.42)","1300.13 (min 855.43, max 1744.82)","1286.00 (min 822.79, max 1749.21)"
    "bw_mem-frd-16mb (MB/s)","1022.56","1132.74","1084.82"
    "bw_mem-frd-1mb (MB/s)","994.66 (min 816.59, max 1172.73)","1082.72 (min 884.80, max 1280.64)","1006.95 (min 801.15, max 1212.75)"
    "bw_mem-frd-2mb (MB/s)","879.12 (min 753.58, max 1004.65)","997.70 (min 872.22, max 1123.17)","937.88 (min 797.98, max 1077.78)"
    "bw_mem-frd-4mb (MB/s)","924.01 (min 795.39, max 1052.63)","1003.36 (min 882.32, max 1124.39)","900.76 (min 774.29, max 1027.22)"
    "bw_mem-frd-8mb (MB/s)","937.56 (min 802.01, max 1073.11)","988.33 (min 855.43, max 1121.23)","946.94 (min 822.79, max 1071.09)"
    "bw_mem-fwr-16mb (MB/s)","1780.94","1753.81","1753.81"
    "bw_mem-fwr-1mb (MB/s)","1537.12 (min 1172.73, max 1901.50)","1578.76 (min 1280.64, max 1876.88)","1539.04 (min 1212.75, max 1865.32)"
    "bw_mem-fwr-2mb (MB/s)","1423.82 (min 1004.65, max 1842.98)","1470.84 (min 1123.17, max 1818.51)","1436.24 (min 1077.78, max 1794.69)"
    "bw_mem-fwr-4mb (MB/s)","1435.82 (min 1052.63, max 1819.01)","1455.85 (min 1124.39, max 1787.31)","1399.09 (min 1027.22, max 1770.96)"
    "bw_mem-fwr-8mb (MB/s)","1439.49 (min 1073.11, max 1805.87)","1446.95 (min 1121.23, max 1772.66)","1415.64 (min 1071.09, max 1760.18)"
    "bw_mem-rd-16mb (MB/s)","1088.51","1135.96","1081.81"
    "bw_mem-rd-1mb (MB/s)","912.37 (min 579.63, max 1245.11)","976.13 (min 648.72, max 1303.54)","946.52 (min 620.54, max 1272.50)"
    "bw_mem-rd-2mb (MB/s)","791.99 (min 496.83, max 1087.15)","855.46 (min 573.48, max 1137.44)","828.62 (min 554.25, max 1102.99)"
    "bw_mem-rd-4mb (MB/s)","825.24 (min 586.08, max 1064.40)","899.80 (min 674.42, max 1125.18)","834.36 (min 572.08, max 1096.64)"
    "bw_mem-rd-8mb (MB/s)","883.75 (min 679.35, max 1088.14)","942.36 (min 754.93, max 1129.78)","830.91 (min 573.68, max 1088.14)"
    "bw_mem-rdwr-16mb (MB/s)","675.96","830.95","597.26"
    "bw_mem-rdwr-1mb (MB/s)","475.87 (min 392.46, max 559.28)","538.40 (min 430.17, max 646.62)","527.09 (min 446.83, max 607.35)"
    "bw_mem-rdwr-2mb (MB/s)","452.73 (min 410.09, max 495.36)","506.60 (min 438.07, max 575.13)","480.47 (min 412.54, max 548.40)"
    "bw_mem-rdwr-4mb (MB/s)","485.45 (min 388.31, max 582.58)","579.51 (min 485.38, max 673.63)","505.73 (min 437.49, max 573.97)"
    "bw_mem-rdwr-8mb (MB/s)","567.00 (min 439.68, max 694.32)","619.49 (min 477.73, max 761.25)","487.83 (min 399.36, max 576.29)"
    "bw_mem-wr-16mb (MB/s)","745.19","766.06","609.45"
    "bw_mem-wr-1mb (MB/s)","569.46 (min 559.28, max 579.63)","647.67 (min 646.62, max 648.72)","613.95 (min 607.35, max 620.54)"
    "bw_mem-wr-2mb (MB/s)","496.10 (min 495.36, max 496.83)","574.31 (min 573.48, max 575.13)","551.33 (min 548.40, max 554.25)"
    "bw_mem-wr-4mb (MB/s)","584.33 (min 582.58, max 586.08)","674.03 (min 673.63, max 674.42)","573.03 (min 572.08, max 573.97)"
    "bw_mem-wr-8mb (MB/s)","686.84 (min 679.35, max 694.32)","758.09 (min 754.93, max 761.25)","574.99 (min 573.68, max 576.29)"
    "bw_mmap_rd-mo-1mb (MB/s)","1219.51","1265.82","1244.22"
    "bw_mmap_rd-o2c-1mb (MB/s)","472.52","500.92","446.10"
    "bw_pipe (MB/s)","462.28","507.32","468.69"
    "bw_unix (MB/s)","549.13","599.28","654.14"
    "lat_connect (us)","66.58","59.62","66.43"
    "lat_ctx-2-128k (us)","8.57","7.38","9.05"
    "lat_ctx-2-256k (us)","10.84","10.58","12.25"
    "lat_ctx-4-128k (us)","8.82","7.32","8.58"
    "lat_ctx-4-256k (us)","9.82","9.93","10.74"
    "lat_fs-0k (num_files)","209.00","220.00","182.00"
    "lat_fs-10k (num_files)","87.00","96.00","93.00"
    "lat_fs-1k (num_files)","126.00","143.00","136.00"
    "lat_fs-4k (num_files)","131.00","130.00","123.00"
    "lat_mem_rd-stride128-sz1000k (ns)","54.80","51.88","53.94"
    "lat_mem_rd-stride128-sz125k (ns)","6.22","5.57","6.22"
    "lat_mem_rd-stride128-sz250k (ns)","6.55","5.84","6.55"
    "lat_mem_rd-stride128-sz31k (ns)","4.70","2.16","4.09"
    "lat_mem_rd-stride128-sz50 (ns)","2.40","2.15","2.41"
    "lat_mem_rd-stride128-sz500k (ns)","15.61","24.71","15.47"
    "lat_mem_rd-stride128-sz62k (ns)","5.89","5.25","5.86"
    "lat_mmap-1m (us)","60.00","64.00","61.00"
    "lat_ops-double-add (ns)","3.21","2.86","3.21"
    "lat_ops-double-div (ns)","17.63","15.75","17.63"
    "lat_ops-double-mul (ns)","3.21","2.86","3.20"
    "lat_ops-float-add (ns)","3.21","2.86","3.21"
    "lat_ops-float-div (ns)","10.43","9.31","10.42"
    "lat_ops-float-mul (ns)","3.21","2.86","3.21"
    "lat_ops-int-add (ns)","0.80","0.72","0.80"
    "lat_ops-int-bit (ns)","0.53","0.48","0.53"
    "lat_ops-int-div (ns)","4.81","4.29","4.81"
    "lat_ops-int-mod (ns)","5.08","4.53","5.08"
    "lat_ops-int-mul (ns)","3.51","3.13","3.51"
    "lat_ops-int64-add (ns)","0.80","0.72","0.80"
    "lat_ops-int64-bit (ns)","0.53","0.48","0.53"
    "lat_ops-int64-div (ns)","7.61","6.80","7.62"
    "lat_ops-int64-mod (ns)","5.88","5.25","5.88"
    "lat_ops-int64-mul (ns)","3.98","3.55","3.98"
    "lat_pagefault (us)","0.78","0.71","1.55"
    "lat_pipe (us)","27.48","25.15","28.22"
    "lat_proc-exec (us)","1071.80","1023.00","1042.80"
    "lat_proc-fork (us)","882.86","852.86","929.00"
    "lat_proc-proccall (us)","0.01","0.01","0.01"
    "lat_select (us)","38.14","34.07","37.98"
    "lat_sem (us)","4.37","2.98","3.22"
    "lat_sig-catch (us)","5.97","5.31","6.03"
    "lat_sig-install (us)","0.73","0.65","0.73"
    "lat_sig-prot (us)","0.78","0.58","0.74"
    "lat_syscall-fstat (us)","2.23","1.97","2.22"
    "lat_syscall-null (us)","0.52","0.46","0.52"
    "lat_syscall-open (us)","185.60","155.14","224.73"
    "lat_syscall-read (us)","0.90","0.80","0.90"
    "lat_syscall-stat (us)","5.44","4.87","5.44"
    "lat_syscall-write (us)","0.91","0.81","0.92"
    "lat_tcp (us)","1.04","0.93","1.04"
    "lat_unix (us)","33.72","29.04","33.12"
    "latency_for_0.50_mb_block_size (nanosec)","15.61","24.71","15.47"
    "latency_for_1.00_mb_block_size (nanosec)","27.40 (min 0.00, max 54.80)","25.94 (min 0.00, max 51.88)","26.97 (min 0.00, max 53.94)"
    "pipe_bandwidth (MBs)","462.28","507.32","468.69"
    "pipe_latency (microsec)","27.48","25.15","28.22"
    "procedure_call (microsec)","0.01","0.01","0.01"
    "select_on_200_tcp_fds (microsec)","38.14","34.07","37.98"
    "semaphore_latency (microsec)","4.37","2.98","3.22"
    "signal_handler_latency (microsec)","0.73","0.65","0.73"
    "signal_handler_overhead (microsec)","5.97","5.31","6.03"
    "tcp_ip_connection_cost_to_localhost (microsec)","66.58","59.62","66.43"
    "tcp_latency_using_localhost (microsec)","1.04","0.93","1.04"



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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cpu_clock (MHz)","1250.00","1400.00","1250.00"
    "dhrystone_per_mhz (DMIPS/MHz)","2.90","2.90","2.90"
    "dhrystone_per_second (DhrystoneP)","6451613.00","7142857.00","6451613.00"



Whetstone
^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "whetstone (MIPS)","5000.00","5000.00","5000.00"



Linpack
^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "linpack (Kflops)","515516.00","575242.00","515670.00"



NBench
^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "assignment (Iterations)","12.94","14.49","12.90"
    "fourier (Iterations)","20380.00","22832.00","20384.00"
    "fp_emulation (Iterations)","192.48","215.64","192.53"
    "huffman (Iterations)","1057.10","1184.20","1057.10"
    "idea (Iterations)","3075.10","3444.70","3075.50"
    "lu_decomposition (Iterations)","473.03","530.04","473.87"
    "neural_net (Iterations)","7.73","8.66","7.73"
    "numeric_sort (Iterations)","561.61","629.58","557.46"
    "string_sort (Iterations)","146.34","163.94","146.35"



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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "add (MB/s)","1415.00","1447.90","1692.60"
    "copy (MB/s)","1455.40","1638.00","1875.50"
    "scale (MB/s)","1595.70","1792.70","1938.40"
    "triad (MB/s)","1384.60","1477.10","1657.50"




CoreMarkPro
^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","37.17","41.84","37.59"
    "core (workloads/)","0.27","0.30","0.27"
    "coremark-pro ()","789.18","887.88","823.42"
    "linear_alg-mid-100x100-sp (workloads/)","13.10","14.68","13.11"
    "loops-all-mid-10k-sp (workloads/)","0.59","0.66","0.63"
    "nnet_test (workloads/)","0.97","1.09","0.97"
    "parser-125k (workloads/)","7.41","8.20","7.69"
    "radix2-big-64k (workloads/)","45.59","53.18","57.64"
    "sha-test (workloads/)","71.43","80.65","72.46"
    "zip-test (workloads/)","18.52","20.83","18.87"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","74.07","83.33","74.07"
    "core (workloads/)","0.54","0.60","0.54"
    "coremark-pro ()","1329.74","1487.25","1358.05"
    "linear_alg-mid-100x100-sp (workloads/)","26.21","29.36","26.18"
    "loops-all-mid-10k-sp (workloads/)","1.03","1.15","1.05"
    "nnet_test (workloads/)","1.94","2.17","1.94"
    "parser-125k (workloads/)","9.43","11.70","10.64"
    "radix2-big-64k (workloads/)","38.37","38.53","40.37"
    "sha-test (workloads/)","140.85","158.73","140.85"
    "zip-test (workloads/)","34.48","38.46","34.48"



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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "4m-check (workloads/)","281.25","301.64","283.22"
    "4m-check-reassembly (workloads/)","62.19","62.93","59.24"
    "4m-check-reassembly-tcp (workloads/)","38.88","40.98","38.76"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","22.26","23.69","22.50"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.61","1.75","1.59"
    "4m-cmykw2 (workloads/)","185.01","199.01","181.32"
    "4m-cmykw2-rotatew2 (workloads/)","36.17","39.14","35.38"
    "4m-reassembly (workloads/)","46.88","49.53","47.57"
    "4m-rotatew2 (workloads/)","41.34","44.29","41.08"
    "4m-tcp-mixed (workloads/)","94.67","102.56","94.12"
    "4m-x264w2 (workloads/)","1.67","1.83","1.64"
    "empty-wld (workloads/)","1.00","1.00","1.00"
    "idct-4m (workloads/)","16.83","18.59","16.84"
    "idct-4mw1 (workloads/)","16.82","18.59","16.84"
    "ippktcheck-4m (workloads/)","282.01","302.52","283.42"
    "ippktcheck-4mw1 (workloads/)","282.90","299.76","283.45"
    "ipres-4m (workloads/)","59.34","64.32","60.90"
    "ipres-4mw1 (workloads/)","60.98","64.91","61.37"
    "md5-4m (workloads/)","22.20","24.69","22.06"
    "md5-4mw1 (workloads/)","22.63","24.76","22.28"
    "rgbcmyk-4m (workloads/)","56.95","63.67","56.77"
    "rgbcmyk-4mw1 (workloads/)","57.16","63.55","56.71"
    "rotate-4ms1 (workloads/)","16.98","18.11","16.91"
    "rotate-4ms1w1 (workloads/)","17.00","18.12","16.89"
    "rotate-4ms64 (workloads/)","17.19","18.37","17.05"
    "rotate-4ms64w1 (workloads/)","17.18","18.27","16.95"
    "x264-4mq (workloads/)","0.50","0.56","0.50"
    "x264-4mqw1 (workloads/)","0.50","0.56","0.50"





Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62xx_sk-fs: Boot time in seconds: avg(min,max)","am62xxsip_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","16.24 (min 15.96, max 16.42)","15.09 (min 14.92, max 15.32)"



Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.



|

ALSA SoC Audio Driver
---------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)","am62xxsip_sk-fs: Throughput (bits/sec)","am62xxsip_sk-fs: CPU Load (%)"

    "11025","352798.00","0.12","352799.00","0.12","352799.00","0.28"
    "16000","511998.00","0.48","511999.00","0.10","512000.00","0.31"
    "22050","705593.00","0.16","705596.00","0.16","705594.00","0.31"
    "24000","705595.00","0.19","705598.00","0.19","705597.00","0.39"
    "32000","1023993.00","0.11","1023996.00","0.11","1023997.00","0.31"
    "44100","1411190.00","0.27","1411195.00","0.25","1411196.00","0.48"
    "48000","1535990.00","1.02","1535994.00","0.20","1535996.00","0.38"
    "88200","2822374.00","0.51","2822385.00","0.51","2822389.00","0.59"
    "96000","3071972.00","0.22","3071984.00","0.19","3071987.00","0.36"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)","am62xxsip_sk-fs: Throughput (bits/sec)","am62xxsip_sk-fs: CPU Load (%)"

    "11025","352945.00","0.13","352946.00","0.11","352948.00","0.10"
    "16000","512212.00","0.26","512213.00","0.11","512216.00","0.09"
    "22050","705888.00","0.14","705892.00","0.12","705887.00","0.12"
    "24000","705890.00","0.17","705893.00","0.14","705891.00","0.14"
    "32000","1024421.00","0.13","1024426.00","0.10","1024425.00","0.10"
    "44100","1411781.00","0.21","1411787.00","0.19","1411789.00","0.18"
    "48000","1536633.00","0.22","1536639.00","0.19","",""
    "88200","2823558.00","0.36","2823567.00","0.35","",""
    "96000","3073259.00","0.28","3073271.00","0.22","",""



|

Graphics SGX/RGX Driver
-----------------------



GFXBench
^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_lp_sk-fs: Fps","am62xx_sk-fs: Score","am62xx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","80.18","1.29"
    " GFXBench 3.x gl_trex_off","125.77","2.25"
    " GFXBench 5.x gl_5_high_off","11.41","0.18","11.48","0.18"




Glmark2
^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_sk-fs: Score","am62xxsip_sk-fs: Score"

    "Glmark2-DRM","51.00","61.00","54.00"
    "Glmark2-Wayland","199.00","217.00","210.00"
    "Glmark2-Wayland 1920x1080","63.00","66.00"



|

Ethernet
--------
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

- CPSW3g: AM64x, AM62x, AM62ax, AM62px


.. rubric::  TCP Bidirectional Throughput
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1685.26","64.99","1767.54","66.70","1647.55","62.58"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","326.74","11.98","1586.14","47.14","1807.73","48.75"




.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","40.95","80.00","37.35","18.00","18.74","37.00","10.12","","48.25","94.00","39.37"
    "128","82.00","89.57","87.00","38.47","82.00","99.23","97.00","38.69","","97.04","95.00","26.11"
    "256","210.00","175.06","85.00","38.18","210.00","198.56","97.00","38.59","","179.37","88.00","38.40"
    "1024","978.00","363.71","44.00","21.25","978.00","785.68","96.00","38.33","","708.67","87.00","38.11"
    "1518","1472.00","183.19","15.00","10.59","1472.00","770.81","63.00","36.09","","706.43","58.00","35.94"




.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","3.38","7.00","1.44","","3.07","6.00","3.06","","2.92","6.00","0.97"
    "128","82.00","6.76","7.00","1.28","82.00","7.58","7.00","2.11","","7.17","7.00","1.63"
    "256","210.00","15.77","8.00","4.60","210.00","15.36","8.00","2.22","","15.16","7.00","2.19"
    "1024","978.00","60.62","7.00","2.80","978.00","61.44","8.00","1.82","","61.44","8.00","4.89"
    "1518","1472.00","38.86","3.00","2.09","1472.00","2.43","0.00","0.59"




.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_lp_sk-fs: Packet Loss %","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: Packet Loss %","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: Packet Loss %"

    "64","","71.78","140.00","65.81","74.13","","97.99","191.00","40.57","61.06","","92.95","182.00","42.37","75.92"
    "128","82.00","173.15","169.00","45.12","65.86","82.00","193.99","189.00","41.95","67.47","","183.40","179.00","43.96","71.84"
    "256","210.00","271.82","133.00","41.55","0.42","210.00","357.95","175.00","41.46","52.51","","324.57","158.00","43.50","58.28"
    "1024","978.00","939.00","115.00","44.49","0.03","978.00","904.64","110.00","42.08","0.38","","738.20","90.00","41.83","0.55"
    "1518","1472.00","13.16","1.00","20.85","97.98","1472.00","3.90","0.00","24.85","99.58"



|

Linux OSPI Flash Driver
-----------------------


AM62XX-SK
^^^^^^^^^


RAW
"""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xx_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","172.41"


.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xx_lp_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","29.07"



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
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","44.60","1.43","174.00","2.30"
    "4m","44.90","1.06","174.00","1.70"
    "4k","5.32","2.19","36.40","10.09"
    "256k","35.40","1.49","173.00","2.84"



.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","61.50","1.99","175.00","2.30"
    "4m","61.70","1.33","175.00","1.97"
    "4k","51.40","19.45","56.80","16.71"
    "256k","61.60","2.33","174.00","3.23"



EMMC EXT4
^^^^^^^^^


.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","51.83 (min 49.52, max 52.61)","5.03 (min 4.49, max 6.52)","177.99","13.56"
    "262144","50.97 (min 48.59, max 51.96)","5.21 (min 4.57, max 6.73)","181.94","14.16"
    "524288","50.87 (min 48.19, max 51.68)","5.79 (min 4.94, max 7.10)","182.94","15.35"
    "1048576","51.33 (min 48.92, max 52.08)","5.32 (min 4.73, max 6.67)","182.83","15.72"
    "5242880","51.15 (min 49.02, max 51.80)","5.18 (min 4.59, max 6.56)","181.99","15.65"



.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "102400","51.16 (min 48.23, max 52.47)","5.88 (min 5.39, max 7.27)","176.55","13.73"
    "262144","49.96 (min 47.07, max 50.94)","5.98 (min 5.45, max 7.53)","180.51","15.04"
    "524288","49.88 (min 47.07, max 50.91)","6.06 (min 5.47, max 7.62)","182.72","17.03"
    "1048576","50.54 (min 47.88, max 51.64)","5.91 (min 5.45, max 7.31)","182.53","16.81"
    "5242880","50.27 (min 47.13, max 51.35)","5.73 (min 5.24, max 7.20)","181.68","17.11"




EMMC EXT2
^^^^^^^^^


.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT2 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT2 CPU Load (%)","am62xx_sk-fs: Read EXT2 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT2 CPU Load (%)"

    "102400","39.34 (min 35.40, max 40.46)","4.49 (min 3.94, max 6.48)","174.99","12.45"
    "262144","40.53 (min 36.16, max 41.74)","4.57 (min 3.80, max 6.57)","177.47","15.45"
    "524288","40.11 (min 35.88, max 41.23)","4.54 (min 3.93, max 6.59)","178.47","14.59"
    "1048576","40.30 (min 36.06, max 41.48)","4.49 (min 3.86, max 6.46)","177.97","14.66"
    "5242880","40.32 (min 35.99, max 41.47)","4.52 (min 3.85, max 6.69)","177.38","14.96"



.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT2 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT2 CPU Load (%)","am62xx_lp_sk-fs: Read EXT2 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT2 CPU Load (%)"

    "102400","50.92 (min 43.73, max 52.79)","6.83 (min 5.89, max 9.41)","173.27","13.56"
    "262144","50.82 (min 43.46, max 52.86)","6.61 (min 5.74, max 9.33)","177.56","16.88"
    "524288","50.63 (min 43.23, max 52.92)","6.74 (min 5.62, max 9.18)","176.84","16.74"
    "1048576","50.67 (min 43.58, max 52.56)","6.62 (min 5.64, max 9.44)","177.34","17.17"
    "5242880","50.70 (min 42.92, max 53.20)","6.46 (min 5.52, max 9.29)","177.49","17.45"




EMMC VFAT
^^^^^^^^^


.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xx_sk-fs: Write VFAT CPU Load (%)","am62xx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xx_sk-fs: Read VFAT CPU Load (%)"

    "102400","47.06 (min 41.03, max 48.78)","6.33 (min 5.66, max 8.51)","169.15","13.77"
    "262144","48.92 (min 42.39, max 50.79)","6.86 (min 6.18, max 9.11)","169.46","15.16"
    "524288","48.17 (min 41.79, max 49.95)","6.59 (min 5.95, max 8.88)","169.19","15.32"
    "1048576","48.61 (min 42.40, max 50.41)","6.61 (min 5.84, max 9.10)","168.56","14.29"
    "5242880","48.94 (min 42.48, max 50.83)","6.65 (min 5.99, max 8.93)","168.66","14.98"




.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write VFAT CPU Load (%)","am62xx_lp_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read VFAT CPU Load (%)"

    "102400","46.05 (min 39.74, max 47.77)","6.88 (min 5.82, max 9.39)","168.34","14.29"
    "262144","47.61 (min 40.82, max 49.71)","7.33 (min 6.35, max 10.21)","169.78","17.89"
    "524288","47.73 (min 40.99, max 49.58)","7.30 (min 6.47, max 9.78)","168.38","18.25"
    "1048576","47.70 (min 41.07, max 49.70)","7.31 (min 6.53, max 9.81)","168.33","17.67"
    "5242880","47.80 (min 40.93, max 49.80)","7.16 (min 6.26, max 9.67)","167.94","16.87"




UBoot EMMC Driver
-----------------


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","99296.97","171560.21"
    "4000000","97523.81","175229.95"




.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","57588.75","169782.38"
    "4000000","57893.99","173375.66"


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","47627.91","91275.77"
    "4000000","52261.56","92434.41"



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
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.70","1.44","87.30","1.53"
    "4m","41.60","1.07","87.20","1.24"
    "4k","2.77","1.78","13.00","4.45"
    "256k","37.60","1.72","83.70","1.79"




.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.60","1.57","87.20","1.56"
    "4m","42.20","1.07","87.30","1.13"
    "4k","2.77","1.99","12.90","5.04"
    "256k","38.60","1.70","84.00","1.88"




.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.40","1.97","87.30","1.86"
    "4m","40.70","1.40","87.00","1.79"
    "4k","2.77","2.14","13.20","4.98"
    "256k","37.80","1.90","83.40","1.90"


MMC EXT4
^^^^^^^^


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Write Raw CPU Load (%)","am62xx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.57 (min 10.49, max 10.60)","1.19 (min 1.06, max 1.45)","11.06","1.08"
    "262144","10.30 (min 9.97, max 10.61)","1.24 (min 1.10, max 1.54)","10.78","1.03"
    "524288","10.31 (min 10.18, max 10.46)","1.18 (min 1.02, max 1.55)","11.44","1.01"
    "1048576","10.35 (min 10.23, max 10.63)","1.22 (min 1.03, max 1.52)","11.44","1.12"
    "5242880","10.55 (min 10.41, max 10.77)","1.20 (min 1.09, max 1.54)","10.95","1.05"




.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write Raw CPU Load (%)","am62xx_lp_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read Raw CPU Load (%)"

    "102400","10.58 (min 10.19, max 10.92)","1.36 (min 1.22, max 1.63)","11.78","1.10"
    "262144","10.12 (min 10.10, max 10.15)","1.42 (min 1.23, max 1.76)","10.95","1.18"
    "524288","10.17 (min 10.10, max 10.23)","1.37 (min 1.17, max 1.66)","11.06","1.19"
    "1048576","10.20 (min 10.14, max 10.30)","1.38 (min 1.21, max 1.70)","11.05","1.21"
    "5242880","10.19 (min 10.16, max 10.28)","1.32 (min 1.14, max 1.81)","11.52","1.13"




.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write Raw CPU Load (%)","am62xxsip_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read Raw CPU Load (%)"

    "102400","10.51 (min 10.47, max 10.57)","1.40 (min 1.06, max 2.18)","10.87","1.19"
    "262144","10.59 (min 10.55, max 10.63)","1.13 (min 0.99, max 1.49)","11.19","1.15"
    "524288","10.71 (min 10.54, max 10.82)","1.02 (min 0.92, max 1.16)","11.01","1.08"
    "1048576","10.61 (min 10.25, max 10.81)","1.16 (min 1.11, max 1.33)","10.83","1.16"
    "5242880","11.04 (min 10.55, max 11.30)","1.11 (min 0.95, max 1.29)","12.02","1.12"


MMC EXT3
^^^^^^^^


.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Write Raw CPU Load (%)","am62xx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Read Raw CPU Load (%)"

    "102400","36.77 (min 32.06, max 38.32)","4.58 (min 3.89, max 6.66)","79.49","6.11"
    "262144","34.68 (min 31.54, max 35.94)","4.19 (min 3.63, max 6.25)","85.12","7.36"
    "524288","34.44 (min 29.06, max 36.66)","4.13 (min 3.68, max 5.76)","89.51","7.51"
    "1048576","34.73 (min 30.73, max 36.01)","4.02 (min 3.28, max 5.95)","89.59","7.73"
    "5242880","38.45 (min 34.26, max 40.01)","4.49 (min 3.77, max 6.55)","84.49","8.22"




.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write Raw CPU Load (%)","am62xx_lp_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read Raw CPU Load (%)"

    "102400","35.99 (min 31.77, max 37.53)","5.11 (min 4.33, max 7.44)","79.52","6.86"
    "262144","33.79 (min 30.12, max 34.90)","4.95 (min 3.92, max 7.10)","84.64","9.05"
    "524288","34.60 (min 30.25, max 35.84)","4.67 (min 3.92, max 7.00)","89.40","8.76"
    "1048576","34.20 (min 29.86, max 35.48)","4.64 (min 3.71, max 6.63)","84.61","8.69"
    "5242880","34.30 (min 30.30, max 35.96)","4.52 (min 3.81, max 6.73)","88.98","8.53"




.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write Raw CPU Load (%)","am62xxsip_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read Raw CPU Load (%)"

    "102400","35.61 (min 27.97, max 40.71)","5.54 (min 2.82, max 9.13)","79.32","6.99"
    "262144","41.13 (min 40.19, max 42.21)","5.30 (min 2.86, max 8.60)","85.39","7.99"
    "524288","42.68 (min 41.84, max 43.27)","4.09 (min 2.83, max 7.93)","84.63","7.74"
    "1048576","42.30 (min 40.04, max 43.70)","3.76 (min 2.77, max 7.16)","89.59","8.72"
    "5242880","42.01 (min 41.13, max 43.09)","3.97 (min 2.62, max 8.43)","89.58","8.33"



MMC EXT2
^^^^^^^^


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Write Raw CPU Load (%)","am62xx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Read Raw CPU Load (%)"

    "102400","38.68 (min 34.18, max 40.13)","4.40 (min 3.65, max 6.69)","80.23","6.53"
    "262144","35.29 (min 31.27, max 36.87)","4.22 (min 3.38, max 5.82)","85.76","7.80"
    "524288","35.20 (min 32.48, max 36.36)","4.16 (min 3.34, max 6.66)","89.26","7.68"
    "1048576","34.82 (min 31.53, max 37.17)","4.12 (min 3.34, max 6.15)","84.22","7.47"
    "5242880","39.27 (min 35.85, max 40.49)","4.39 (min 3.68, max 6.50)","89.89","7.73"




.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write Raw CPU Load (%)","am62xx_lp_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read Raw CPU Load (%)"

    "102400","38.00 (min 33.58, max 39.35)","4.74 (min 4.13, max 7.07)","75.79","6.22"
    "262144","35.16 (min 31.38, max 36.39)","4.55 (min 3.80, max 6.53)","85.71","8.59"
    "524288","35.08 (min 31.38, max 36.20)","4.61 (min 3.86, max 6.72)","89.64","8.37"
    "1048576","38.47 (min 34.47, max 39.93)","4.85 (min 4.14, max 7.38)","89.35","8.33"
    "5242880","35.09 (min 31.53, max 36.31)","4.41 (min 3.64, max 6.68)","89.43","9.15"




.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write Raw CPU Load (%)","am62xxsip_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read Raw CPU Load (%)"

    "102400","36.89 (min 27.05, max 39.82)","4.68 (min 2.56, max 7.97)","76.13","6.58"
    "262144","43.94 (min 43.06, max 44.49)","3.91 (min 2.71, max 7.56)","86.00","7.44"
    "524288","43.69 (min 41.15, max 45.18)","3.87 (min 3.04, max 6.82)","89.93","8.19"
    "1048576","44.00 (min 42.71, max 45.20)","3.85 (min 2.86, max 7.47)","89.56","7.96"
    "5242880","42.13 (min 40.07, max 44.07)","3.47 (min 2.70, max 5.73)","89.51","8.14"





The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option


UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","39009.52","83591.84"
    "800000","40554.46","88086.02"
    "1000000","44643.05","89530.05"




.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","35008.55","81920.00"
    "800000","32379.45","87148.94"
    "1000000","49799.39","90021.98"




.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","31507.69","81920.00"
    "800000","42890.05","87148.94"
    "1000000","49648.48","89530.05"



The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)


|

USB Driver
----------


USB Device Controller
^^^^^^^^^^^^^^^^^^^^^


.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)","am62xxsip_sk-fs: Throughput (MB/sec)"

    "150","33.00","42.50","43.50"



.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)","am62xxsip_sk-fs: Throughput (MB/sec)"

    "150","30.70","39.80","37.10"


|

CRYPTO Driver
-------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62xx_lp_sk-fs: throughput (KBytes/Sec)","am62xx_sk-fs: throughput (KBytes/Sec)","am62xxsip_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","19332.10","21814.61","21901.65"
    "aes-128-cbc","16","344.83","380.01","370.25"
    "aes-128-cbc","16384","112579.93","116370.09","124261.72"
    "aes-128-cbc","256","6121.81","6160.55","6302.89"
    "aes-128-cbc","64","1532.95","1542.44","1626.22"
    "aes-128-cbc","8192","84322.99","88956.93","93115.73"
    "aes-128-ecb","1024","20105.56","22847.49","22268.59"
    "aes-128-ecb","16","362.49","383.55","378.92"
    "aes-128-ecb","16384","114682.54","120569.86","127860.74"
    "aes-128-ecb","256","6092.37","6171.05","6463.66"
    "aes-128-ecb","64","1538.13","1548.27","1663.08"
    "aes-128-ecb","8192","87067.31","92536.83","95701.67"
    "aes-192-cbc","1024","19188.39","21499.22","21587.29"
    "aes-192-cbc","16","345.95","383.05","370.81"
    "aes-192-cbc","16384","105316.35","109843.80","116539.39"
    "aes-192-cbc","256","6100.82","6159.79","6238.46"
    "aes-192-cbc","64","1526.98","1543.04","1620.65"
    "aes-192-cbc","8192","80538.28","84535.98","89066.15"
    "aes-192-ecb","1024","19876.52","22543.70","22193.49"
    "aes-192-ecb","16","361.37","383.07","382.09"
    "aes-192-ecb","16384","111351.13","113628.50","121503.74"
    "aes-192-ecb","256","6097.66","6170.03","6481.15"
    "aes-192-ecb","64","1538.15","1546.99","1680.51"
    "aes-192-ecb","8192","84372.14","88003.93","92105.39"
    "aes-256-cbc","1024","18930.69","21275.65","21359.96"
    "aes-256-cbc","16","346.96","382.25","370.81"
    "aes-256-cbc","16384","98604.37","102520.15","109614.42"
    "aes-256-cbc","256","6085.97","6156.37","6247.08"
    "aes-256-cbc","64","1530.07","1540.33","1618.54"
    "aes-256-cbc","8192","77313.37","81087.15","84762.62"
    "aes-256-ecb","1024","19814.06","22423.21","22128.98"
    "aes-256-ecb","16","362.64","383.66","376.89"
    "aes-256-ecb","16384","103180.97","106779.99","114005.33"
    "aes-256-ecb","256","6135.13","6169.94","6384.81"
    "aes-256-ecb","64","1537.32","1547.33","1658.11"
    "aes-256-ecb","8192","79563.43","84475.90","87960.23"
    "sha256","1024","24798.21","29029.38","30274.56"
    "sha256","16","426.65","481.71","501.07"
    "sha256","16384","242909.18","261947.39","251062.95"
    "sha256","256","6633.39","7654.49","7859.88"
    "sha256","64","1676.12","1916.42","1985.81"
    "sha256","8192","156958.72","174140.07","168424.79"
    "sha512","1024","20430.17","23322.97","21332.99"
    "sha512","16","398.69","480.28","483.14"
    "sha512","16384","59561.30","65650.69","60030.98"
    "sha512","256","6163.97","6760.70","6936.66"
    "sha512","64","1589.91","1920.30","1929.90"
    "sha512","8192","52232.19","58804.91","53398.19"



.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62xx_lp_sk-fs: CPU Load","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: CPU Load"

    "aes-128-cbc","35.00","35.00","35.00"
    "aes-128-ecb","37.00","38.00","36.00"
    "aes-192-cbc","35.00","36.00","35.00"
    "aes-192-ecb","36.00","37.00","36.00"
    "aes-256-cbc","35.00","35.00","34.00"
    "aes-256-ecb","36.00","36.00","36.00"
    "sha256","94.00","94.00","95.00"
    "sha512","94.00","95.00","95.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc



IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","am62xx_sk-fs: Throughput (Mbps)","am62xx_sk-fs: Packets/Sec","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: Throughput (Mbps)","am62xxsip_sk-fs: Packets/Sec","am62xxsip_sk-fs: CPU Load"

    "aes128","1.20","0.00","51.32","4.20","0.00","70.26"
    "aes192","1.30","0.00","51.25","2.90","0.00","79.48"
    "aes256","1.20","0.00","51.52","216.40","19.00","28.32"

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
