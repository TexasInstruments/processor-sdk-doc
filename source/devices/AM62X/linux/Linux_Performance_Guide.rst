
======================================
 Linux 10.01 Performance Guide
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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","30.51","27.27","25.88"
    "af_unix_socket_stream_bandwidth (MBs)","566.44","627.75","1060.15"
    "bw_file_rd-io-1mb (MB/s)","751.09","870.47","1037.34"
    "bw_file_rd-o2c-1mb (MB/s)","442.94","497.27","541.32"
    "bw_mem-bcopy-16mb (MB/s)","654.34","763.10","919.86"
    "bw_mem-bcopy-1mb (MB/s)","688.82","783.24","980.97"
    "bw_mem-bcopy-2mb (MB/s)","645.89","758.63","917.01"
    "bw_mem-bcopy-4mb (MB/s)","672.49","799.68","893.85"
    "bw_mem-bcopy-8mb (MB/s)","693.18","801.52","930.12"
    "bw_mem-bzero-16mb (MB/s)","1693.30","1734.23","2129.36"
    "bw_mem-bzero-1mb (MB/s)","1178.44 (min 688.82, max 1668.06)","1259.38 (min 783.24, max 1735.51)","1556.21 (min 980.97, max 2131.44)"
    "bw_mem-bzero-2mb (MB/s)","1156.70 (min 645.89, max 1667.50)","1247.83 (min 758.63, max 1737.02)","1523.85 (min 917.01, max 2130.68)"
    "bw_mem-bzero-4mb (MB/s)","1171.20 (min 672.49, max 1669.91)","1267.02 (min 799.68, max 1734.35)","1512.46 (min 893.85, max 2131.06)"
    "bw_mem-bzero-8mb (MB/s)","1187.28 (min 693.18, max 1681.38)","1281.72 (min 801.52, max 1761.92)","1529.88 (min 930.12, max 2129.64)"
    "bw_mem-cp-16mb (MB/s)","378.01","455.46","518.94"
    "bw_mem-cp-1mb (MB/s)","1091.05 (min 367.87, max 1814.22)","1153.77 (min 444.64, max 1862.89)","1383.56 (min 501.25, max 2265.86)"
    "bw_mem-cp-2mb (MB/s)","1059.28 (min 367.85, max 1750.70)","1112.34 (min 420.92, max 1803.75)","1356.95 (min 506.39, max 2207.51)"
    "bw_mem-cp-4mb (MB/s)","1063.37 (min 401.36, max 1725.38)","1128.24 (min 471.03, max 1785.45)","1334.78 (min 496.83, max 2172.73)"
    "bw_mem-cp-8mb (MB/s)","1059.31 (min 417.21, max 1701.40)","1133.71 (min 493.77, max 1773.64)","1334.21 (min 514.40, max 2154.01)"
    "bw_mem-fcp-16mb (MB/s)","667.75","742.98","939.41"
    "bw_mem-fcp-1mb (MB/s)","1207.38 (min 746.69, max 1668.06)","1311.73 (min 887.94, max 1735.51)","1563.23 (min 995.02, max 2131.44)"
    "bw_mem-fcp-2mb (MB/s)","1199.32 (min 731.13, max 1667.50)","1304.62 (min 872.22, max 1737.02)","1546.81 (min 962.93, max 2130.68)"
    "bw_mem-fcp-4mb (MB/s)","1201.73 (min 733.54, max 1669.91)","1325.37 (min 916.38, max 1734.35)","1543.83 (min 956.59, max 2131.06)"
    "bw_mem-fcp-8mb (MB/s)","1213.48 (min 745.57, max 1681.38)","1342.06 (min 922.19, max 1761.92)","1552.15 (min 974.66, max 2129.64)"
    "bw_mem-frd-16mb (MB/s)","1012.27","1136.44","1377.65"
    "bw_mem-frd-1mb (MB/s)","920.09 (min 746.69, max 1093.49)","1075.97 (min 887.94, max 1263.99)","1273.24 (min 995.02, max 1551.46)"
    "bw_mem-frd-2mb (MB/s)","845.11 (min 731.13, max 959.08)","992.70 (min 872.22, max 1113.17)","1166.99 (min 962.93, max 1371.04)"
    "bw_mem-frd-4mb (MB/s)","864.10 (min 733.54, max 994.65)","1019.20 (min 916.38, max 1122.02)","1115.54 (min 956.59, max 1274.49)"
    "bw_mem-frd-8mb (MB/s)","845.27 (min 745.57, max 944.96)","1023.21 (min 922.19, max 1124.23)","1176.04 (min 974.66, max 1377.41)"
    "bw_mem-fwr-16mb (MB/s)","1699.60","1759.98","2143.34"
    "bw_mem-fwr-1mb (MB/s)","1453.86 (min 1093.49, max 1814.22)","1563.44 (min 1263.99, max 1862.89)","1908.66 (min 1551.46, max 2265.86)"
    "bw_mem-fwr-2mb (MB/s)","1354.89 (min 959.08, max 1750.70)","1458.46 (min 1113.17, max 1803.75)","1789.28 (min 1371.04, max 2207.51)"
    "bw_mem-fwr-4mb (MB/s)","1360.02 (min 994.65, max 1725.38)","1453.74 (min 1122.02, max 1785.45)","1723.61 (min 1274.49, max 2172.73)"
    "bw_mem-fwr-8mb (MB/s)","1323.18 (min 944.96, max 1701.40)","1448.94 (min 1124.23, max 1773.64)","1765.71 (min 1377.41, max 2154.01)"
    "bw_mem-rd-16mb (MB/s)","1004.33","1142.86","1376.11"
    "bw_mem-rd-1mb (MB/s)","860.81 (min 567.46, max 1154.16)","957.31 (min 652.21, max 1262.40)","1144.70 (min 722.54, max 1566.85)"
    "bw_mem-rd-2mb (MB/s)","778.51 (min 527.50, max 1029.51)","878.72 (min 631.31, max 1126.13)","1029.58 (min 664.45, max 1394.70)"
    "bw_mem-rd-4mb (MB/s)","803.54 (min 579.46, max 1027.62)","907.94 (min 697.47, max 1118.41)","1042.94 (min 702.99, max 1382.89)"
    "bw_mem-rd-8mb (MB/s)","806.22 (min 592.81, max 1019.63)","949.53 (min 774.52, max 1124.54)","1052.54 (min 725.76, max 1379.31)"
    "bw_mem-rdwr-16mb (MB/s)","677.65","851.43","740.12"
    "bw_mem-rdwr-1mb (MB/s)","464.48 (min 367.87, max 561.09)","559.42 (min 444.64, max 674.20)","615.26 (min 501.25, max 729.26)"
    "bw_mem-rdwr-2mb (MB/s)","434.84 (min 367.85, max 501.82)","523.55 (min 420.92, max 626.17)","586.25 (min 506.39, max 666.11)"
    "bw_mem-rdwr-4mb (MB/s)","481.66 (min 401.36, max 561.96)","582.50 (min 471.03, max 693.96)","600.28 (min 496.83, max 703.73)"
    "bw_mem-rdwr-8mb (MB/s)","515.99 (min 417.21, max 614.77)","644.50 (min 493.77, max 795.23)","614.66 (min 514.40, max 714.92)"
    "bw_mem-wr-16mb (MB/s)","680.65","806.61","739.06"
    "bw_mem-wr-1mb (MB/s)","564.28 (min 561.09, max 567.46)","663.21 (min 652.21, max 674.20)","725.90 (min 722.54, max 729.26)"
    "bw_mem-wr-2mb (MB/s)","514.66 (min 501.82, max 527.50)","628.74 (min 626.17, max 631.31)","665.28 (min 664.45, max 666.11)"
    "bw_mem-wr-4mb (MB/s)","570.71 (min 561.96, max 579.46)","695.72 (min 693.96, max 697.47)","703.36 (min 702.99, max 703.73)"
    "bw_mem-wr-8mb (MB/s)","603.79 (min 592.81, max 614.77)","784.88 (min 774.52, max 795.23)","720.34 (min 714.92, max 725.76)"
    "bw_mmap_rd-mo-1mb (MB/s)","1174.89","1263.99","1561.42"
    "bw_mmap_rd-o2c-1mb (MB/s)","411.81","455.86","506.33"
    "bw_pipe (MB/s)","443.26","512.65","682.97"
    "bw_unix (MB/s)","566.44","627.75","1060.15"
    "lat_connect (us)","68.27","61.15","57.80"
    "lat_ctx-2-128k (us)","6.69","6.38","6.15"
    "lat_ctx-2-256k (us)","7.99","5.79","6.88"
    "lat_ctx-4-128k (us)","6.37","5.80","5.74"
    "lat_ctx-4-256k (us)","9.96","6.32","5.86"
    "lat_fs-0k (num_files)","197.00","183.00","244.00"
    "lat_fs-10k (num_files)","95.00","103.00","98.00"
    "lat_fs-1k (num_files)","102.00","131.00","167.00"
    "lat_fs-4k (num_files)","132.00","146.00","160.00"
    "lat_mem_rd-stride128-sz1000k (ns)","57.34","52.54","43.16"
    "lat_mem_rd-stride128-sz125k (ns)","6.28","5.54","5.57"
    "lat_mem_rd-stride128-sz250k (ns)","6.53","5.85","5.84"
    "lat_mem_rd-stride128-sz31k (ns)","4.09","3.65","3.65"
    "lat_mem_rd-stride128-sz50 (ns)","2.40","2.15","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","19.22","11.17","12.31"
    "lat_mem_rd-stride128-sz62k (ns)","5.86","5.20","5.23"
    "lat_mmap-1m (us)","63.00","68.00","61.00"
    "lat_ops-double-add (ns)","3.21","2.86","2.86"
    "lat_ops-double-div (ns)","17.64","15.74","15.74"
    "lat_ops-double-mul (ns)","3.21","2.86","2.86"
    "lat_ops-float-add (ns)","3.21","2.86","2.86"
    "lat_ops-float-div (ns)","10.42","9.30","9.30"
    "lat_ops-float-mul (ns)","3.21","2.86","2.86"
    "lat_ops-int-add (ns)","0.80","0.72","0.72"
    "lat_ops-int-bit (ns)","0.53","0.48","0.48"
    "lat_ops-int-div (ns)","4.81","4.29","4.29"
    "lat_ops-int-mod (ns)","5.08","4.53","4.53"
    "lat_ops-int-mul (ns)","3.44","3.07","3.07"
    "lat_ops-int64-add (ns)","0.80","0.72","0.72"
    "lat_ops-int64-bit (ns)","0.53","0.48","0.48"
    "lat_ops-int64-div (ns)","7.62","6.79","6.79"
    "lat_ops-int64-mod (ns)","5.88","5.25","5.25"
    "lat_ops-int64-mul (ns)","3.98","3.55","3.55"
    "lat_pagefault (us)","1.82","1.59","1.45"
    "lat_pipe (us)","26.01","23.18","22.99"
    "lat_proc-exec (us)","1266.25","1141.80","976.20"
    "lat_proc-fork (us)","953.67","857.71","763.86"
    "lat_proc-proccall (us)","0.01","0.01","0.01"
    "lat_select (us)","39.29","35.05","35.07"
    "lat_sem (us)","2.30","2.44","1.94"
    "lat_sig-catch (us)","6.49","5.76","5.74"
    "lat_sig-install (us)","0.73","0.66","0.66"
    "lat_sig-prot (us)","1.31","1.10","1.11"
    "lat_syscall-fstat (us)","2.24","2.00","2.00"
    "lat_syscall-null (us)","0.52","0.46","0.46"
    "lat_syscall-open (us)","163.50","197.91","155.95"
    "lat_syscall-read (us)","0.93","0.83","0.83"
    "lat_syscall-stat (us)","5.55","5.02","4.97"
    "lat_syscall-write (us)","0.83","0.74","0.74"
    "lat_tcp (us)","1.05","0.94","0.94"
    "lat_unix (us)","30.51","27.27","25.88"
    "latency_for_0.50_mb_block_size (nanosec)","19.22","11.17","12.31"
    "latency_for_1.00_mb_block_size (nanosec)","28.67 (min 0.00, max 57.34)","26.27 (min 0.00, max 52.54)","21.58 (min 0.00, max 43.16)"
    "pipe_bandwidth (MBs)","443.26","512.65","682.97"
    "pipe_latency (microsec)","26.01","23.18","22.99"
    "procedure_call (microsec)","0.01","0.01","0.01"
    "select_on_200_tcp_fds (microsec)","39.29","35.05","35.07"
    "semaphore_latency (microsec)","2.30","2.44","1.94"
    "signal_handler_latency (microsec)","0.73","0.66","0.66"
    "signal_handler_overhead (microsec)","6.49","5.76","5.74"
    "tcp_ip_connection_cost_to_localhost (microsec)","68.27","61.15","57.80"
    "tcp_latency_using_localhost (microsec)","1.05","0.94","0.94"

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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cpu_clock (MHz)","1250.00","1400.00","1400.00"
    "dhrystone_per_mhz (DMIPS/MHz)","2.90","2.90","2.90"
    "dhrystone_per_second (DhrystoneP)","6451613.00","7142857.00","7142857.00"

Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "whetstone (MIPS)","5000.00","10000.00","5000.00"

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "linpack (Kflops)","515090.00","577370.00","576595.00"

NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "assignment (Iterations)","12.93","14.50","14.51"
    "fourier (Iterations)","20385.00","22831.00","22832.00"
    "fp_emulation (Iterations)","192.54","215.66","215.65"
    "huffman (Iterations)","1057.40","1184.50","1184.40"
    "idea (Iterations)","3075.70","3444.80","3444.70"
    "lu_decomposition (Iterations)","472.27","528.59","529.43"
    "neural_net (Iterations)","7.72","8.65","8.65"
    "numeric_sort (Iterations)","562.00","629.31","627.71"
    "string_sort (Iterations)","146.35","163.92","163.92"

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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "add (MB/s)","1367.60","1442.40","1715.30"
    "copy (MB/s)","1426.70","1633.70","1874.90"
    "scale (MB/s)","1576.40","1806.40","1926.80"
    "triad (MB/s)","1346.40","1488.60","1681.30"

CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","37.31","41.67","41.67"
    "core (workloads/)","0.27","0.30","0.30"
    "coremark-pro ()","767.20","885.25","849.58"
    "linear_alg-mid-100x100-sp (workloads/)","13.11","14.69","14.66"
    "loops-all-mid-10k-sp (workloads/)","0.59","0.67","0.67"
    "nnet_test (workloads/)","0.97","1.09","1.09"
    "parser-125k (workloads/)","7.35","8.33","8.26"
    "radix2-big-64k (workloads/)","35.23","50.38","35.16"
    "sha-test (workloads/)","71.94","80.65","80.65"
    "zip-test (workloads/)","18.52","20.83","20.83"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","73.53","83.33","82.64"
    "core (workloads/)","0.54","0.60","0.60"
    "coremark-pro ()","1302.46","1543.95","1495.06"
    "linear_alg-mid-100x100-sp (workloads/)","26.19","29.36","29.33"
    "loops-all-mid-10k-sp (workloads/)","1.03","1.23","1.15"
    "nnet_test (workloads/)","1.94","2.17","2.17"
    "parser-125k (workloads/)","9.71","12.20","11.76"
    "radix2-big-64k (workloads/)","31.26","44.86","40.56"
    "sha-test (workloads/)","142.86","161.29","158.73"
    "zip-test (workloads/)","33.90","40.82","38.46"

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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "4m-check (workloads/)","271.68","305.55","302.63"
    "4m-check-reassembly (workloads/)","57.21","63.94","63.01"
    "4m-check-reassembly-tcp (workloads/)","37.31","41.60","41.19"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","21.38","23.85","23.69"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.58","1.80","1.78"
    "4m-cmykw2 (workloads/)","176.52","198.41","196.08"
    "4m-cmykw2-rotatew2 (workloads/)","34.56","39.11","38.27"
    "4m-reassembly (workloads/)","44.29","49.07","49.12"
    "4m-rotatew2 (workloads/)","39.65","44.48","45.39"
    "4m-tcp-mixed (workloads/)","91.95","103.23","102.56"
    "4m-x264w2 (workloads/)","1.65","1.84","1.86"
    "empty-wld (workloads/)","1.00","1.00","1.00"
    "idct-4m (workloads/)","16.79","18.63","18.55"
    "idct-4mw1 (workloads/)","16.80","18.61","18.58"
    "ippktcheck-4m (workloads/)","272.69","305.06","304.99"
    "ippktcheck-4mw1 (workloads/)","271.62","310.37","303.25"
    "ipres-4m (workloads/)","57.54","65.19","63.10"
    "ipres-4mw1 (workloads/)","57.36","64.16","62.21"
    "md5-4m (workloads/)","23.29","25.94","26.13"
    "md5-4mw1 (workloads/)","23.18","25.90","26.00"
    "rgbcmyk-4m (workloads/)","56.82","63.61","63.33"
    "rgbcmyk-4mw1 (workloads/)","56.56","63.78","63.31"
    "rotate-4ms1 (workloads/)","16.36","18.18","18.20"
    "rotate-4ms1w1 (workloads/)","16.34","18.19","18.16"
    "rotate-4ms64 (workloads/)","16.48","18.36","18.38"
    "rotate-4ms64w1 (workloads/)","16.47","18.32","18.39"
    "x264-4mq (workloads/)","0.50","0.56","0.56"
    "x264-4mqw1 (workloads/)","0.50","0.56","0.56"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62xx_lp_sk-fs: Boot time in seconds: avg(min,max)","am62xx_sk-fs: Boot time in seconds: avg(min,max)","am62xxsip_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","17.17 (min 16.77, max 17.51)","17.14 (min 16.69, max 17.59)","16.61 (min 16.32, max 16.93)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)","am62xxsip_sk-fs: Throughput (bits/sec)","am62xxsip_sk-fs: CPU Load (%)"

    "8000","255998.00","0.36","255999.00","0.09","255999.00","0.07"
    "11025","352798.00","0.19","352797.00","0.16","352798.00","0.14"
    "16000","511997.00","0.13","511997.00","0.09","511998.00","0.10"
    "22050","705597.00","0.33","705596.00","0.30","705598.00","0.27"
    "24000","705594.00","0.34","705595.00","0.27","705596.00","0.25"
    "32000","1023988.00","0.19","1023990.00","0.72","1023992.00","0.73"
    "44100","1411185.00","0.51","1411187.00","0.45","1411190.00","0.42"
    "48000","1535985.00","0.26","1535986.00","0.21","1535990.00","0.20"
    "88200","2822370.00","1.04","2822371.00","0.93","2822378.00","0.83"
    "96000","3071967.00","0.38","3071967.00","2.32","3071978.00","0.30"

|

Graphics SGX/RGX Driver
-------------------------

GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_lp_sk-fs: Fps","am62xx_sk-fs: Score","am62xx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","82.22","1.33"
    " GFXBench 3.x gl_trex_off","122.93","2.20"
    " GFXBench 5.x gl_5_high_off","11.18","0.17","11.46","0.18"

Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_sk-fs: Score","am62xxsip_sk-fs: Score"

    "Glmark2-DRM","51.00","61.00"
    "Glmark2-Wayland","200.00","218.00","209.00"
    "Glmark2-Wayland 1920x1080","62.00","67.00"

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
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1579.73","89.05","1838.18","68.74","1827.76","69.40"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1756.62","57.06","1742.62","50.25","1828.24","44.80"

.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","11.71","81.00","36.80","18.00","1.89","13.00","3.79","18.00","16.27","113.00","39.85"
    "128","82.00","60.36","92.00","38.24","82.00","67.53","103.00","38.37","82.00","71.83","109.00","39.55"
    "256","210.00","152.77","91.00","38.11","210.00","79.97","48.00","16.58","210.00","184.10","110.00","39.45"
    "1024","978.00","183.53","23.00","10.10","978.00","143.17","18.00","7.43","978.00","827.54","106.00","38.94"
    "1518","1472.00","956.68","81.00","42.84","1472.00","954.15","81.00","36.52","1472.00","956.98","81.00","35.74"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","1.21","8.00","4.65","18.00","1.01","7.00","1.01","18.00","1.01","7.00","0.94"
    "128","82.00","5.25","8.00","3.43","82.00","5.12","8.00","1.50","82.00","5.18","8.00","1.17"
    "256","210.00","12.94","8.00","4.26","210.00","11.59","7.00","1.10","210.00","13.94","8.00","1.34"
    "1024","978.00","65.72","8.00","2.33","978.00","65.72","8.00","3.44","978.00","931.68","119.00","42.71"
    "1518","1472.00","98.91","8.00","4.39","1472.00","98.92","8.00","3.32"

.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_lp_sk-fs: Packet Loss %","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: Packet Loss %","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: Packet Loss %"

    "64","18.00","19.27","134.00","40.40","1.01","18.00","32.50","226.00","41.18","71.70","18.00","32.30","224.00","41.74","73.86"
    "128","82.00","111.55","170.00","42.47","10.50","82.00","132.14","201.00","41.36","62.99","82.00","131.22","200.00","42.03","50.74"
    "256","210.00","269.06","160.00","42.24","1.06","210.00","329.03","196.00","42.36","56.71","210.00","322.91","192.00","42.02","38.10"
    "1024","978.00","913.54","117.00","42.14","0.02","978.00","911.01","116.00","42.48","0.33","978.00","931.68","119.00","42.71","0.00"
    "1518","1472.00","940.47","80.00","41.86","0.38","1472.00","953.90","81.00","43.27","0.32"

|

Linux OSPI Flash Driver
-------------------------

AM62XX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xx_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","172.41"

|

UBoot QSPI/OSPI Driver
-------------------------

AM62XX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","356.08","204800.00"
    "800000","356.22","240941.18"
    "1000000","358.47","268590.16"
    "2000000","351.77","284939.13"

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","380.81","195047.62"
    "800000","382.54","240941.18"
    "1000000","387.24","268590.16"
    "2000000","391.75","284939.13"

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

    "1m","60.30","1.28","175.00","1.42"
    "4m","59.30","1.02","175.00","1.69"
    "4k","51.40","15.33","55.80","14.12"
    "256k","60.30","1.77","174.00","2.54"

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","58.40","1.77","175.00","2.34"
    "4m","58.60","1.26","175.00","1.91"
    "4k","51.40","18.03","56.60","16.15"
    "256k","58.50","1.86","174.00","2.86"

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "1m","90.60","2.45","171.00","2.08"
    "4m","95.90","1.96","172.00","2.08"
    "4k","62.80","20.49","93.10","22.27"
    "256k","90.10","2.35","170.00","2.45"

EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","54.44 (min 52.10, max 55.30)","4.52 (min 3.96, max 6.09)","180.77","10.48"
    "262144","53.45 (min 51.06, max 54.33)","4.80 (min 4.25, max 6.33)","178.76","11.69"
    "524288","53.27 (min 50.36, max 54.05)","4.83 (min 4.39, max 6.13)","182.72","13.16"
    "1048576","53.74 (min 51.16, max 54.70)","4.85 (min 4.30, max 6.46)","183.05","12.72"
    "5242880","54.01 (min 50.92, max 55.04)","4.67 (min 4.20, max 5.72)","182.97","13.48"

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "102400","52.51 (min 50.01, max 53.62)","6.13 (min 5.62, max 7.87)","180.19","15.02"
    "262144","51.72 (min 48.24, max 52.73)","6.24 (min 5.76, max 7.95)","164.96","15.26"
    "524288","51.97 (min 48.19, max 53.16)","6.38 (min 5.73, max 7.71)","170.21","17.74"
    "1048576","51.46 (min 48.19, max 52.49)","6.06 (min 5.25, max 7.94)","182.42","17.18"
    "5242880","51.96 (min 48.64, max 53.23)","6.25 (min 5.80, max 7.77)","182.16","17.47"

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "102400","96.50 (min 94.37, max 98.68)","10.36 (min 6.55, max 17.97)","178.27","9.87"
    "262144","76.93 (min 48.58, max 97.56)","6.26 (min 3.17, max 10.07)","179.62","13.30"
    "524288","77.11 (min 49.70, max 96.50)","6.17 (min 3.35, max 10.16)","180.72","12.61"
    "1048576","77.27 (min 48.97, max 96.76)","6.45 (min 3.42, max 10.81)","181.14","12.88"
    "5242880","80.07 (min 48.38, max 97.69)","6.59 (min 3.59, max 10.83)","181.09","12.12"

EMMC VFAT
^^^^^^^^^

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xx_sk-fs: Write VFAT CPU Load (%)","am62xx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xx_sk-fs: Read VFAT CPU Load (%)"

    "102400","48.56 (min 41.84, max 50.37)","6.56 (min 5.52, max 9.20)","171.91","13.22"
    "262144","49.22 (min 42.44, max 51.01)","6.93 (min 6.08, max 9.52)","157.56","15.15"
    "524288","49.34 (min 42.54, max 51.14)","6.90 (min 6.08, max 9.54)","160.17","14.94"
    "1048576","49.54 (min 42.58, max 51.39)","6.98 (min 6.34, max 9.27)","169.11","15.32"
    "5242880","49.87 (min 42.95, max 51.63)","6.97 (min 6.27, max 9.53)","167.80","14.86"

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write VFAT CPU Load (%)","am62xx_lp_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read VFAT CPU Load (%)"

    "102400","46.16 (min 39.51, max 48.04)","6.95 (min 6.18, max 9.54)","172.33","14.11"
    "262144","47.28 (min 40.23, max 49.19)","7.37 (min 6.53, max 9.90)","156.81","14.77"
    "524288","47.32 (min 40.34, max 49.22)","7.37 (min 6.41, max 9.83)","156.30","15.85"
    "1048576","47.58 (min 40.48, max 49.49)","7.14 (min 6.38, max 9.68)","167.94","15.85"
    "5242880","47.67 (min 40.69, max 49.57)","7.34 (min 6.61, max 9.91)","167.74","16.53"

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write VFAT CPU Load (%)","am62xxsip_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read VFAT CPU Load (%)"

    "102400","83.42 (min 66.69, max 97.45)","12.58 (min 8.65, max 19.18)","174.92","11.67"
    "262144","69.57 (min 59.40, max 97.47)","7.25 (min 4.31, max 13.44)","174.12","13.75"
    "524288","75.16 (min 56.74, max 96.66)","7.73 (min 4.30, max 13.28)","174.10","14.17"
    "1048576","74.99 (min 53.68, max 97.71)","8.26 (min 5.17, max 12.86)","174.76","12.61"
    "5242880","83.52 (min 60.53, max 97.85)","9.36 (min 5.57, max 13.11)","174.91","13.39"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","56987.83","168907.22"
    "4000000","57487.72","173375.66"

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","56888.89","169782.38"
    "4000000","58462.09","172918.21"

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","98107.78","171560.21"
    "4000000","97961.14","174762.67"

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

    "1m","42.60","1.20","88.20","1.21"
    "4m","40.90","0.89","81.30","1.00"
    "4k","2.81","1.57","12.90","4.01"
    "256k","37.20","1.17","84.90","1.37"

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.10","1.67","85.40","1.78"
    "4m","41.80","1.23","85.20","1.40"
    "4k","2.82","1.94","13.20","4.79"
    "256k","35.30","1.75","84.40","1.57"

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "1m","19.80","0.81","87.80","1.29"
    "4m","18.10","0.61","87.50","1.30"
    "4k","4.11","2.24","13.70","4.46"
    "256k","19.40","0.92","83.90","1.28"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Write Raw CPU Load (%)","am62xx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.23 (min 9.94, max 10.81)","1.13 (min 1.00, max 1.47)","10.76","0.95"
    "262144","10.46 (min 9.98, max 11.05)","1.19 (min 1.05, max 1.57)","10.93","0.89"
    "524288","10.56 (min 10.37, max 10.77)","1.24 (min 1.06, max 1.63)","11.20","1.07"
    "1048576","10.42 (min 10.34, max 10.53)","1.23 (min 1.11, max 1.54)","11.49","1.01"
    "5242880","10.45 (min 10.15, max 10.61)","1.14 (min 1.02, max 1.48)","12.00","0.97"

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write Raw CPU Load (%)","am62xx_lp_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read Raw CPU Load (%)"

    "102400","10.13 (min 9.86, max 10.54)","1.28 (min 1.11, max 1.65)","11.08","1.01"
    "262144","10.25 (min 9.98, max 10.76)","1.35 (min 1.21, max 1.70)","10.86","1.24"
    "524288","10.08 (min 9.89, max 10.17)","1.32 (min 1.20, max 1.70)","11.00","1.13"
    "1048576","10.32 (min 10.16, max 10.51)","1.41 (min 1.21, max 1.72)","10.93","1.07"
    "5242880","10.60 (min 10.51, max 10.73)","1.29 (min 1.13, max 1.73)","11.97","1.17"

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write Raw CPU Load (%)","am62xxsip_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read Raw CPU Load (%)"

    "102400","10.33 (min 10.27, max 10.37)","1.57 (min 1.23, max 2.37)","10.84","0.98"
    "262144","10.44 (min 10.28, max 10.54)","1.10 (min 0.84, max 1.31)","10.89","0.91"
    "524288","10.19 (min 10.13, max 10.35)","0.76 (min 0.66, max 0.88)","11.24","1.05"
    "1048576","10.42 (min 10.17, max 10.56)","0.86 (min 0.61, max 1.04)","11.26","1.02"
    "5242880","10.84 (min 10.53, max 11.24)","0.72 (min 0.54, max 0.86)","12.02","1.03"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 
UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","33032.26","56109.59"
    "800000","16855.97","70017.09"
    "1000000","13540.50","79149.76"

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","40960.00","60235.29"
    "800000","47906.43","73142.86"
    "1000000","47352.60","81108.91"

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","33032.26","57690.14"
    "800000","37751.15","71234.78"
    "1000000","47766.76","80709.36"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

USB Driver
-------------------------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)"

    "150","36.00","43.80"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)"

    "150","34.00","42.60"

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62xxsip_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","26023.25"
    "aes-128-cbc","16","441.59"
    "aes-128-cbc","16384","132983.47"
    "aes-128-cbc","256","7625.73"
    "aes-128-cbc","64","1963.05"
    "aes-128-cbc","8192","102845.10"
    "aes-128-ecb","1024","26712.41"
    "aes-128-ecb","16","452.78"
    "aes-128-ecb","16384","138040.66"
    "aes-128-ecb","256","7874.99"
    "aes-128-ecb","64","2030.57"
    "aes-128-ecb","8192","106356.74"
    "aes-192-cbc","1024","25901.74"
    "aes-192-cbc","16","443.53"
    "aes-192-cbc","16384","125539.67"
    "aes-192-cbc","256","7525.72"
    "aes-192-cbc","64","1961.39"
    "aes-192-cbc","8192","98268.50"
    "aes-192-ecb","1024","26521.26"
    "aes-192-ecb","16","455.63"
    "aes-192-ecb","16384","130864.47"
    "aes-192-ecb","256","7845.80"
    "aes-192-ecb","64","2021.14"
    "aes-192-ecb","8192","102156.97"
    "aes-256-cbc","1024","25711.27"
    "aes-256-cbc","16","443.25"
    "aes-256-cbc","16384","117118.29"
    "aes-256-cbc","256","7470.42"
    "aes-256-cbc","64","1974.08"
    "aes-256-cbc","8192","93077.50"
    "aes-256-ecb","1024","26374.49"
    "aes-256-ecb","16","455.40"
    "aes-256-ecb","16384","122115.41"
    "aes-256-ecb","256","7746.56"
    "aes-256-ecb","64","2024.85"
    "aes-256-ecb","8192","97113.43"
    "sha256","1024","31077.03"
    "sha256","16","517.50"
    "sha256","16384","265513.64"
    "sha256","256","8112.04"
    "sha256","64","2048.51"
    "sha256","8192","175890.43"
    "sha512","1024","23217.83"
    "sha512","16","520.82"
    "sha512","16384","67239.94"
    "sha512","256","7507.88"
    "sha512","64","2085.01"
    "sha512","8192","59643.22"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62xxsip_sk-fs: CPU Load"

    "aes-128-cbc","38.00"
    "aes-128-ecb","39.00"
    "aes-192-cbc","37.00"
    "aes-192-ecb","38.00"
    "aes-256-cbc","37.00"
    "aes-256-ecb","38.00"
    "sha256","98.00"
    "sha512","97.00"

Listed for each algorithm are the code snippets used to run each benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","am62xx_sk-fs: Throughput (Mbps)","am62xx_sk-fs: Packets/Sec","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: Throughput (Mbps)","am62xxsip_sk-fs: Packets/Sec","am62xxsip_sk-fs: CPU Load"

    "aes128","109.70","9.00","52.24","129.50","11.00","52.63"
    "aes192","103.40","9.00","52.10","258.70","23.00","27.59"
    "aes256","226.20","20.00","27.93"

|

Low Power Performance
-------------------------

Table:  **Deep sleep**

.. csv-table::
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","9.79"
   "vddr_core","0.85","n/a"
   "soc_dvdd_3v3","3.30","7.20"
   "soc_dvdd_1v8","1.80","1.98"
   "vdda_1v8","1.80","1.98"
   "vdd_lpddr4/vdd_ddr4","1.10","8.78"
   "Total"," ","29.75"

Table:  **MCU only**

.. csv-table::
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","110.46"
   "vddr_core","0.85","n/a"
   "soc_dvdd_3v3","3.30","13.98"
   "soc_dvdd_1v8","1.80","1.62"
   "vdda_1v8","1.80","11.30"
   "vdd_lpddr4/vdd_ddr4","1.10","8.16"
   "Total"," ","145.88"

Partial I/O Data
- All voltage rails were measured to be near 0V

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)
