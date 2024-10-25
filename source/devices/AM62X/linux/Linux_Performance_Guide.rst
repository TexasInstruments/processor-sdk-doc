
======================================
 Linux 10.00 Performance Guide
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
http://e2e.ti.com/ or http://support.ti.com/


System Benchmarks
-------------------


LMBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
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

    "af_unix_sock_stream_latency (microsec)","27.25","24.81","26.57"
    "af_unix_socket_stream_bandwidth (MBs)","572.01","633.32","1152.05"
    "bw_file_rd-io-1mb (MB/s)","770.30","876.42","1045.11"
    "bw_file_rd-o2c-1mb (MB/s)","436.94","525.03","612.56"
    "bw_mem-bcopy-16mb (MB/s)","655.71","756.89","859.01"
    "bw_mem-bcopy-1mb (MB/s)","685.17","794.91","981.93"
    "bw_mem-bcopy-2mb (MB/s)","675.90","765.21","890.87"
    "bw_mem-bcopy-4mb (MB/s)","685.52","766.58","849.98"
    "bw_mem-bcopy-8mb (MB/s)","686.75","799.92","921.66"
    "bw_mem-bzero-16mb (MB/s)","1691.87","1744.82","2129.36"
    "bw_mem-bzero-1mb (MB/s)","1175.78 (min 685.17, max 1666.39)","1263.86 (min 794.91, max 1732.80)","1556.12 (min 981.93, max 2130.30)"
    "bw_mem-bzero-2mb (MB/s)","1170.73 (min 675.90, max 1665.56)","1252.78 (min 765.21, max 1740.34)","1510.02 (min 890.87, max 2129.17)"
    "bw_mem-bzero-4mb (MB/s)","1175.52 (min 685.52, max 1665.51)","1250.72 (min 766.58, max 1734.86)","1489.77 (min 849.98, max 2129.55)"
    "bw_mem-bzero-8mb (MB/s)","1181.60 (min 686.75, max 1676.45)","1272.66 (min 799.92, max 1745.39)","1525.65 (min 921.66, max 2129.64)"
    "bw_mem-cp-16mb (MB/s)","383.29","447.15","510.43"
    "bw_mem-cp-1mb (MB/s)","1091.89 (min 378.12, max 1805.65)","1161.34 (min 446.50, max 1876.17)","1393.17 (min 501.50, max 2284.84)"
    "bw_mem-cp-2mb (MB/s)","1056.55 (min 366.37, max 1746.72)","1120.09 (min 424.63, max 1815.54)","1361.20 (min 506.33, max 2216.07)"
    "bw_mem-cp-4mb (MB/s)","1041.93 (min 367.11, max 1716.74)","1102.99 (min 420.79, max 1785.18)","1330.54 (min 491.10, max 2169.98)"
    "bw_mem-cp-8mb (MB/s)","1061.00 (min 421.50, max 1700.50)","1129.75 (min 483.88, max 1775.61)","1331.79 (min 505.78, max 2157.79)"
    "bw_mem-fcp-16mb (MB/s)","663.49","743.11","968.05"
    "bw_mem-fcp-1mb (MB/s)","1223.52 (min 780.64, max 1666.39)","1306.47 (min 880.13, max 1732.80)","1561.27 (min 992.23, max 2130.30)"
    "bw_mem-fcp-2mb (MB/s)","1193.86 (min 722.15, max 1665.56)","1259.08 (min 777.81, max 1740.34)","1531.88 (min 934.58, max 2129.17)"
    "bw_mem-fcp-4mb (MB/s)","1212.19 (min 758.87, max 1665.51)","1316.77 (min 898.67, max 1734.86)","1526.09 (min 922.62, max 2129.55)"
    "bw_mem-fcp-8mb (MB/s)","1221.96 (min 767.46, max 1676.45)","1293.57 (min 841.75, max 1745.39)","1553.52 (min 977.40, max 2129.64)"
    "bw_mem-frd-16mb (MB/s)","968.11","1105.35","1377.53"
    "bw_mem-frd-1mb (MB/s)","952.86 (min 780.64, max 1125.07)","1076.78 (min 880.13, max 1273.42)","1282.28 (min 992.23, max 1572.33)"
    "bw_mem-frd-2mb (MB/s)","859.83 (min 722.15, max 997.51)","947.15 (min 777.81, max 1116.49)","1127.03 (min 934.58, max 1319.48)"
    "bw_mem-frd-4mb (MB/s)","884.87 (min 758.87, max 1010.87)","1007.37 (min 898.67, max 1116.07)","1150.85 (min 922.62, max 1379.07)"
    "bw_mem-frd-8mb (MB/s)","891.73 (min 767.46, max 1016.00)","975.43 (min 841.75, max 1109.11)","1174.57 (min 977.40, max 1371.74)"
    "bw_mem-fwr-16mb (MB/s)","1698.51","1771.09","2139.90"
    "bw_mem-fwr-1mb (MB/s)","1465.36 (min 1125.07, max 1805.65)","1574.80 (min 1273.42, max 1876.17)","1928.59 (min 1572.33, max 2284.84)"
    "bw_mem-fwr-2mb (MB/s)","1372.12 (min 997.51, max 1746.72)","1466.02 (min 1116.49, max 1815.54)","1767.78 (min 1319.48, max 2216.07)"
    "bw_mem-fwr-4mb (MB/s)","1363.81 (min 1010.87, max 1716.74)","1450.63 (min 1116.07, max 1785.18)","1774.53 (min 1379.07, max 2169.98)"
    "bw_mem-fwr-8mb (MB/s)","1358.25 (min 1016.00, max 1700.50)","1442.36 (min 1109.11, max 1775.61)","1764.77 (min 1371.74, max 2157.79)"
    "bw_mem-rd-16mb (MB/s)","1032.52","1137.90","1381.57"
    "bw_mem-rd-1mb (MB/s)","855.42 (min 532.58, max 1178.25)","986.70 (min 672.27, max 1301.12)","1166.52 (min 751.31, max 1581.72)"
    "bw_mem-rd-2mb (MB/s)","754.43 (min 479.16, max 1029.69)","852.69 (min 576.70, max 1128.67)","1033.96 (min 678.54, max 1389.37)"
    "bw_mem-rd-4mb (MB/s)","786.05 (min 550.51, max 1021.58)","918.19 (min 707.71, max 1128.67)","1039.92 (min 700.53, max 1379.31)"
    "bw_mem-rd-8mb (MB/s)","828.69 (min 632.66, max 1024.72)","942.82 (min 755.22, max 1130.42)","1051.50 (min 724.64, max 1378.36)"
    "bw_mem-rdwr-16mb (MB/s)","675.62","744.67","746.27"
    "bw_mem-rdwr-1mb (MB/s)","463.99 (min 378.12, max 549.85)","538.56 (min 446.50, max 630.62)","616.99 (min 501.50, max 732.47)"
    "bw_mem-rdwr-2mb (MB/s)","422.77 (min 366.37, max 479.16)","491.49 (min 424.63, max 558.35)","590.78 (min 506.33, max 675.22)"
    "bw_mem-rdwr-4mb (MB/s)","463.75 (min 367.11, max 560.38)","529.94 (min 420.79, max 639.08)","594.59 (min 491.10, max 698.08)"
    "bw_mem-rdwr-8mb (MB/s)","526.41 (min 421.50, max 631.31)","614.00 (min 483.88, max 744.12)","612.90 (min 505.78, max 720.01)"
    "bw_mem-wr-16mb (MB/s)","658.27","838.53","743.53"
    "bw_mem-wr-1mb (MB/s)","541.22 (min 532.58, max 549.85)","651.45 (min 630.62, max 672.27)","741.89 (min 732.47, max 751.31)"
    "bw_mem-wr-2mb (MB/s)","479.16","567.53 (min 558.35, max 576.70)","676.88 (min 675.22, max 678.54)"
    "bw_mem-wr-4mb (MB/s)","555.45 (min 550.51, max 560.38)","673.40 (min 639.08, max 707.71)","699.31 (min 698.08, max 700.53)"
    "bw_mem-wr-8mb (MB/s)","631.99 (min 631.31, max 632.66)","749.67 (min 744.12, max 755.22)","722.33 (min 720.01, max 724.64)"
    "bw_mmap_rd-mo-1mb (MB/s)","1160.29","1280.18","1567.94"
    "bw_mmap_rd-o2c-1mb (MB/s)","421.23","486.78","505.39"
    "bw_pipe (MB/s)","462.85","506.12","693.65"
    "bw_unix (MB/s)","572.01","633.32","1152.05"
    "lat_connect (us)","59.88","52.95","51.47"
    "lat_ctx-2-128k (us)","7.18","6.48","6.51"
    "lat_ctx-2-256k (us)","6.10","7.26","6.18"
    "lat_ctx-4-128k (us)","7.38","5.62","6.18"
    "lat_ctx-4-256k (us)","6.99","7.33","4.23"
    "lat_fs-0k (num_files)","240.00","272.00","286.00"
    "lat_fs-10k (num_files)","103.00","108.00","125.00"
    "lat_fs-1k (num_files)","146.00","154.00","193.00"
    "lat_fs-4k (num_files)","124.00","184.00","166.00"
    "lat_mem_rd-stride128-sz1000k (ns)","57.65","52.61","43.16"
    "lat_mem_rd-stride128-sz125k (ns)","6.24","5.57","5.58"
    "lat_mem_rd-stride128-sz250k (ns)","6.53","5.83","5.84"
    "lat_mem_rd-stride128-sz31k (ns)","2.42","3.65","3.65"
    "lat_mem_rd-stride128-sz50 (ns)","2.40","2.15","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","20.63","15.30","15.55"
    "lat_mem_rd-stride128-sz62k (ns)","5.90","5.25","5.25"
    "lat_mmap-1m (us)","63.00","68.00","55.00"
    "lat_ops-double-add (ns)","3.21","2.86","2.86"
    "lat_ops-double-div (ns)","17.63","15.74","15.74"
    "lat_ops-double-mul (ns)","3.21","2.86","2.86"
    "lat_ops-float-add (ns)","3.21","2.86","2.86"
    "lat_ops-float-div (ns)","10.42","9.30","9.31"
    "lat_ops-float-mul (ns)","3.21","2.86","2.86"
    "lat_ops-int-add (ns)","0.80","0.72","0.72"
    "lat_ops-int-bit (ns)","0.53","0.48","0.48"
    "lat_ops-int-div (ns)","4.81","4.29","4.29"
    "lat_ops-int-mod (ns)","5.08","4.54","4.53"
    "lat_ops-int-mul (ns)","3.45","3.07","3.08"
    "lat_ops-int64-add (ns)","0.80","0.72","0.72"
    "lat_ops-int64-bit (ns)","0.53","0.48","0.48"
    "lat_ops-int64-div (ns)","7.61","6.80","6.80"
    "lat_ops-int64-mod (ns)","5.88","5.25","5.25"
    "lat_ops-int64-mul (ns)","4.09","3.56","3.55"
    "lat_pagefault (us)","1.70","1.49","1.36"
    "lat_pipe (us)","24.73","22.16","21.99"
    "lat_proc-exec (us)","1217.00","1103.00","910.00"
    "lat_proc-fork (us)","913.00","830.86","705.11"
    "lat_proc-proccall (us)","0.01","0.01","0.01"
    "lat_select (us)","40.10","36.07","36.05"
    "lat_sem (us)","2.23","1.64","1.84"
    "lat_sig-catch (us)","5.93","5.33","5.30"
    "lat_sig-install (us)","0.72","0.65","0.65"
    "lat_sig-prot (us)","1.09","0.95","0.96"
    "lat_syscall-fstat (us)","1.84","1.64","1.65"
    "lat_syscall-null (us)","0.52","0.46","0.46"
    "lat_syscall-open (us)","283.62","169.09","148.54"
    "lat_syscall-read (us)","0.86","0.77","0.77"
    "lat_syscall-stat (us)","4.59","4.12","4.13"
    "lat_syscall-write (us)","0.77","0.68","0.69"
    "lat_tcp (us)","1.06","0.94","0.95"
    "lat_unix (us)","27.25","24.81","26.57"
    "latency_for_0.50_mb_block_size (nanosec)","20.63","15.30","15.55"
    "latency_for_1.00_mb_block_size (nanosec)","28.82 (min 0.00, max 57.65)","26.30 (min 0.00, max 52.61)","21.58 (min 0.00, max 43.16)"
    "pipe_bandwidth (MBs)","462.85","506.12","693.65"
    "pipe_latency (microsec)","24.73","22.16","21.99"
    "procedure_call (microsec)","0.01","0.01","0.01"
    "select_on_200_tcp_fds (microsec)","40.10","36.07","36.05"
    "semaphore_latency (microsec)","2.23","1.64","1.84"
    "signal_handler_latency (microsec)","0.72","0.65","0.65"
    "signal_handler_overhead (microsec)","5.93","5.33","5.30"
    "tcp_ip_connection_cost_to_localhost (microsec)","59.88","52.95","51.47"
    "tcp_latency_using_localhost (microsec)","1.06","0.94","0.95"




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

    "whetstone (MIPS)","5000.00","10000.00","10000.00"




Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "linpack (Kflops)","515825.00","578100.00","574617.00"




NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "assignment (Iterations)","12.94","14.49","14.49"
    "fourier (Iterations)","20384.00","22833.00","22832.00"
    "fp_emulation (Iterations)","192.53","215.65","215.65"
    "huffman (Iterations)","1057.00","1184.40","1184.40"
    "idea (Iterations)","3075.60","3444.90","3444.90"
    "lu_decomposition (Iterations)","470.79","527.77","528.61"
    "neural_net (Iterations)","7.73","8.65","8.65"
    "numeric_sort (Iterations)","554.43","628.90","628.46"
    "string_sort (Iterations)","146.37","163.94","163.94"




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

    "add (MB/s)","1376.60","1442.50","1713.70"
    "copy (MB/s)","1452.20","1637.60","1852.50"
    "scale (MB/s)","1582.90","1830.50","1943.80"
    "triad (MB/s)","1349.10","1481.40","1681.70"




CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","37.17","42.02","41.84"
    "core (workloads/)","0.27","0.30","0.30"
    "coremark-pro ()","761.94","885.95","848.71"
    "linear_alg-mid-100x100-sp (workloads/)","13.11","14.69","14.68"
    "loops-all-mid-10k-sp (workloads/)","0.59","0.66","0.67"
    "nnet_test (workloads/)","0.97","1.09","1.09"
    "parser-125k (workloads/)","7.35","8.33","8.26"
    "radix2-big-64k (workloads/)","33.24","51.08","34.93"
    "sha-test (workloads/)","71.94","80.65","80.00"
    "zip-test (workloads/)","18.52","20.83","20.83"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","73.53","81.97","82.64"
    "core (workloads/)","0.54","0.60","0.60"
    "coremark-pro ()","1314.33","1498.39","1553.78"
    "linear_alg-mid-100x100-sp (workloads/)","26.21","29.34","29.38"
    "loops-all-mid-10k-sp (workloads/)","1.03","1.14","1.23"
    "nnet_test (workloads/)","1.94","2.17","2.17"
    "parser-125k (workloads/)","10.64","11.83","12.05"
    "radix2-big-64k (workloads/)","30.41","42.62","49.45"
    "sha-test (workloads/)","142.86","158.73","161.29"
    "zip-test (workloads/)","34.48","37.74","40.00"

 
 


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

    "4m-check (workloads/)","273.97","311.06","365.87"
    "4m-check-reassembly (workloads/)","56.21","66.84","76.22"
    "4m-check-reassembly-tcp (workloads/)","37.15","41.46","48.08"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","18.90","24.02","28.92"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.59","1.79","1.84"
    "4m-cmykw2 (workloads/)","118.91","199.60","236.41"
    "4m-cmykw2-rotatew2 (workloads/)","34.50","39.14","45.84"
    "4m-reassembly (workloads/)","44.56","49.16","58.72"
    "4m-rotatew2 (workloads/)","39.60","44.58","53.05"
    "4m-tcp-mixed (workloads/)","91.95","102.56","114.29"
    "4m-x264w2 (workloads/)","1.66","1.85","1.91"
    "empty-wld (workloads/)","1.00","1.00","1.00"
    "idct-4m (workloads/)","16.80","18.62","19.12"
    "idct-4mw1 (workloads/)","16.77","18.63","19.11"
    "ippktcheck-4m (workloads/)","273.58","307.77","365.93"
    "ippktcheck-4mw1 (workloads/)","273.05","307.47","363.43"
    "ipres-4m (workloads/)","58.23","65.56","77.84"
    "ipres-4mw1 (workloads/)","58.09","65.39","78.45"
    "md5-4m (workloads/)","23.42","26.32","27.74"
    "md5-4mw1 (workloads/)","23.26","26.33","27.83"
    "rgbcmyk-4m (workloads/)","55.88","63.94","64.77"
    "rgbcmyk-4mw1 (workloads/)","56.48","63.86","64.79"
    "rotate-4ms1 (workloads/)","16.47","18.25","21.61"
    "rotate-4ms1w1 (workloads/)","16.42","18.18","21.75"
    "rotate-4ms64 (workloads/)","16.54","19.28","21.86"
    "rotate-4ms64w1 (workloads/)","16.57","18.40","21.87"
    "x264-4mq (workloads/)","0.50","0.56","0.57"
    "x264-4mqw1 (workloads/)","0.50","0.56","0.57"



 
 



|

Boot-time Measurement
-------------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Boot time MMCSD
    :header: "Boot Configuration","am62xx_lp_sk-fs: boot time (sec)","am62xxsip_sk-fs: boot time (sec)"

    "Kernel boot time test when bootloader, kernel and sdk-rootfs are in mmc-sd","17.28 (min 17.19, max 17.39)","20.97 (min 19.77, max 21.38)"
    "Kernel boot time test when init is /bin/sh and bootloader, kernel and sdk-rootfs are in mmc-sd","4.42 (min 4.38, max 4.43)","3.95 (min 3.92, max 3.98)"
    "kernel boot time test when bootloader, kernel and sdk-rootfs are in mmc-sd","23.13 (min 19.50, max 25.68)","18.33 (min 17.52, max 19.48)"



 
 



|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)","am62xxsip_sk-fs: Throughput (bits/sec)","am62xxsip_sk-fs: CPU Load (%)"

    "8000","255998.00","0.27","255998.00","0.15","255999.00","0.28"
    "11025","352797.00","0.19","352797.00","0.21","352799.00","0.35"
    "16000","511996.00","0.13","511997.00","0.17","511999.00","0.30"
    "22050","705595.00","0.33","705596.00","0.34","705599.00","0.49"
    "24000","705595.00","0.32","705595.00","0.32","705596.00","0.45"
    "32000","1023991.00","0.92","1023990.00","0.21","1023992.00","1.05"
    "44100","1411188.00","0.50","1411187.00","0.50","1411191.00","0.64"
    "48000","1535987.00","0.25","1535987.00","1.23","1535991.00","0.45"
    "88200","2822371.00","0.95","2822372.00","0.92","2822381.00","1.01"
    "96000","3071968.00","0.41","3071969.00","2.50","3071979.00","1.25"



 
 



 



|

Graphics SGX/RGX Driver
-------------------------
 


GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_lp_sk-fs: Fps","am62xx_sk-fs: Score","am62xx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","82.32","1.33"
    " GFXBench 3.x gl_trex_off","122.97","2.20"
    " GFXBench 5.x gl_5_high_off","11.17","0.17","11.82","0.18"




Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_sk-fs: Score","am62xxsip_sk-fs: Score"

    "Glmark2-DRM","51.00","61.00"
    "Glmark2-Wayland","200.00","218.00","211.00"
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

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1811.14","68.36","1835.59","67.36","1820.77","62.08"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1707.56","48.86","1819.03","52.11","1838.83","45.74"




.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","15.01","104.00","40.02","18.00","16.92","118.00","40.59","18.00","17.98","125.00","41.45"
    "128","82.00","65.07","99.00","39.33","82.00","73.78","112.00","39.86","82.00","79.54","121.00","40.66"
    "256","210.00","164.03","98.00","39.04","210.00","188.16","112.00","39.80","210.00","187.01","111.00","39.70"
    "1024","978.00","603.42","77.00","62.39","978.00","148.66","19.00","13.25","978.00","909.21","116.00","43.63"
    "1518","1472.00","845.79","72.00","62.01","1472.00","956.84","81.00","38.64","1472.00","957.01","81.00","35.52"




.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","1.05","7.00","0.92","18.00","17.93","125.00","82.59"
    "128","82.00","3.94","6.00","1.04","82.00","5.44","8.00","2.44","82.00","4.72","7.00","1.18"
    "256","210.00","13.61","8.00","2.93","210.00","13.94","8.00","1.63","210.00","13.44","8.00","1.30"
    "1024","978.00","67.29","9.00","5.02","978.00","934.93","119.00","41.89","978.00","936.69","120.00","43.50"
    "1518","1472.00","98.92","8.00","5.91","1472.00","957.03","81.00","43.05"




.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_lp_sk-fs: Packet Loss %","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: Packet Loss %","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: Packet Loss %"

    "64","18.00","33.79","235.00","42.10","71.81","18.00","25.06","174.00","37.74","17.10"
    "128","82.00","125.99","192.00","44.62","63.57","82.00","139.74","213.00","43.66","47.43","82.00","152.20","232.00","43.43","68.57"
    "256","210.00","261.84","156.00","39.59","11.97","210.00","332.46","198.00","45.22","47.35","210.00","381.37","227.00","44.06","28.31"
    "1024","978.00","934.87","119.00","44.28","0.21","978.00","936.28","120.00","43.16","0.05","978.00","936.69","120.00","43.50","0.00"
    "1518","1472.00","956.11","81.00","43.28","0.10","1472.00","955.03","81.00","41.14","0.19"

 
 

 

 
 

 

 



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

EMMC Driver
-------------------------

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

 

 

 

 

 


 


AM62XX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","59.70","1.36","175.00","1.84"
    "4m","59.70","1.07","175.00","1.55"
    "4k","49.80","14.96","55.70","14.02"
    "256k","60.00","1.72","174.00","2.62"




.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","57.60","1.58","175.00","2.29"
    "4m","57.70","1.26","175.00","1.85"
    "4k","51.30","17.36","56.60","15.91"
    "256k","57.60","1.80","174.00","2.93"




.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "1m","91.60","1.91","172.00","1.81"
    "4m","97.90","1.74","171.00","1.77"
    "4k","62.90","19.46","93.30","21.89"
    "256k","91.70","1.98","171.00","2.17"

 
 





 
 

 











 
 



|

UBoot EMMC Driver
-------------------------


AM62XX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","59470.05","170666.67"
    "4000000","61134.33","173375.66"




.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","61478.42","170666.67"
    "4000000","62415.24","174297.87"




.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","98402.40","171560.21"
    "4000000","97523.81","174762.67"

 
 




























 
 

 



|

MMC/SD Driver
-------------------------

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

 

 

 

 

 





 


AM62XX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","18.10","0.72","83.80","1.42"
    "4m","18.20","0.66","82.50","1.09"
    "4k","4.28","2.26","13.80","5.72"
    "256k","17.60","0.84","78.70","1.20"




.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","13.20","0.76","103.00","1.73"
    "4m","14.00","0.59","104.00","1.50"
    "4k","4.41","2.56","12.50","4.38"
    "256k","12.90","0.85","95.60","1.86"




.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "1m","41.70","1.23","84.80","1.24"
    "4m","40.70","0.93","84.90","1.20"
    "4k","2.82","1.55","13.10","4.07"
    "256k","36.80","1.24","84.30","1.39"

 
 







 

 

 

 

 

 

 

 















 

 

 





 

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option
 



|

UBoot MMC/SD Driver
-------------------------


AM62XX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","39384.62","56888.89"
    "800000","12245.14","70017.09"
    "1000000","11033.00","79533.98"




.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","32000.00","56109.59"
    "800000","57286.71","70017.09"
    "1000000","18788.99","79149.76"




.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","15693.49","55351.35"
    "800000","45765.36","68840.34"
    "1000000","22692.52","78769.23"

  
  


































 
 

 



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62xxsip_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","24597.50"
    "aes-128-cbc","16","385.46"
    "aes-128-cbc","16384","124245.33"
    "aes-128-cbc","256","6635.18"
    "aes-128-cbc","64","1739.18"
    "aes-128-cbc","8192","98197.50"
    "aes-128-ecb","1024","24546.30"
    "aes-128-ecb","16","385.70"
    "aes-128-ecb","16384","130946.39"
    "aes-128-ecb","256","6978.82"
    "aes-128-ecb","64","1798.57"
    "aes-128-ecb","8192","98312.19"
    "aes-192-cbc","1024","24569.86"
    "aes-192-cbc","16","385.77"
    "aes-192-cbc","16384","117784.58"
    "aes-192-cbc","256","6603.78"
    "aes-192-cbc","64","1728.70"
    "aes-192-cbc","8192","93285.03"
    "aes-192-ecb","1024","24602.97"
    "aes-192-ecb","16","390.62"
    "aes-192-ecb","16384","121563.82"
    "aes-192-ecb","256","6844.93"
    "aes-192-ecb","64","1797.33"
    "aes-192-ecb","8192","98121.05"
    "aes-256-cbc","1024","24532.65"
    "aes-256-cbc","16","386.05"
    "aes-256-cbc","16384","108653.23"
    "aes-256-cbc","256","6415.62"
    "aes-256-cbc","64","1742.23"
    "aes-256-cbc","8192","87635.29"
    "aes-256-ecb","1024","24565.08"
    "aes-256-ecb","16","390.44"
    "aes-256-ecb","16384","114059.95"
    "aes-256-ecb","256","6796.46"
    "aes-256-ecb","64","1792.53"
    "aes-256-ecb","8192","91944.28"
    "sha256","1024","29849.94"
    "sha256","16","505.45"
    "sha256","16384","261352.11"
    "sha256","256","7697.32"
    "sha256","64","1954.41"
    "sha256","8192","173222.57"
    "sha512","1024","23266.99"
    "sha512","16","481.34"
    "sha512","16384","66218.67"
    "sha512","256","6858.58"
    "sha512","64","1925.91"
    "sha512","8192","58791.25"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62xxsip_sk-fs: CPU Load"

    "aes-128-cbc","39.00"
    "aes-128-ecb","40.00"
    "aes-192-cbc","38.00"
    "aes-192-ecb","40.00"
    "aes-256-cbc","38.00"
    "aes-256-ecb","39.00"
    "sha256","97.00"
    "sha512","97.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

|

Low Power Performance
-------------------------

Table:  **Deep sleep**

.. csv-table::
    :header: "Rail name","Rail voltage(V)","am62xx_sk-fs"

    "vdd_core","0.85","7.95"
    "vddr_core","0.85","n/a"
    "soc_dvdd_3v3","3.30","6.20"
    "soc_dvdd_1v8","1.80","1.98"
    "vdda_1v8","1.80","1.80"
    "vdd_lpddr4/vdd_ddr4","1.10","7.50"
    "Total"," ","25.43"

Table:  **MCU only**

.. csv-table::
    :header: "Rail name","Rail voltage(V)","am62xx_sk-fs"

    "vdd_core","0.85","121.81"
    "vddr_core","0.85","n/a"
    "soc_dvdd_3v3","3.30","12.72"
    "soc_dvdd_1v8","1.80","1.62"
    "vdda_1v8","1.80","10.71"
    "vdd_lpddr4/vdd_ddr4","1.10","7.74"
    "Total"," ","154.61"

Partial I/O Data
- All voltage rails were measured to be near 0V

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)
