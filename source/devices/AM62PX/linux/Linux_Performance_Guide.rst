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
| AM62Px SK      | AM62Px Starter Kit rev E1 with ARM running at 1.4GHz, DDR data rate 3200 MT/S                                  |
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
-----------------

LMBench
^^^^^^^
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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","26.29 (min 21.53, max 29.44)"
    "af_unix_socket_stream_bandwidth (mb\s)","1171.35 (min 1145.36, max 1187.19)"
    "bw_file_rd-io-1mb (mb/s)","1369.92 (min 1348.23, max 1405.73)"
    "bw_file_rd-o2c-1mb (mb/s)","734.43 (min 722.94, max 753.86)"
    "bw_mem-bcopy-16mb (mb/s)","1883.80 (min 1838.45, max 1953.36)"
    "bw_mem-bcopy-1mb (mb/s)","2013.26 (min 1957.33, max 2106.88)"
    "bw_mem-bcopy-2mb (mb/s)","1745.10 (min 1728.31, max 1761.18)"
    "bw_mem-bcopy-4mb (mb/s)","1753.02 (min 1688.48, max 1806.14)"
    "bw_mem-bcopy-8mb (mb/s)","1872.67 (min 1828.99, max 1951.22)"
    "bw_mem-bzero-16mb (mb/s)","7927.46 (min 7815.04, max 8119.08)"
    "bw_mem-bzero-1mb (mb/s)","4967.30 (min 1957.33, max 8118.35)"
    "bw_mem-bzero-2mb (mb/s)","4832.80 (min 1728.31, max 8110.01)"
    "bw_mem-bzero-4mb (mb/s)","4838.05 (min 1688.48, max 8113.59)"
    "bw_mem-bzero-8mb (mb/s)","4895.46 (min 1828.99, max 8106.74)"
    "bw_mem-cp-16mb (mb/s)","936.38 (min 911.21, max 974.36)"
    "bw_mem-cp-1mb (mb/s)","4576.25 (min 902.36, max 8428.00)"
    "bw_mem-cp-2mb (mb/s)","4485.27 (min 906.07, max 8237.82)"
    "bw_mem-cp-4mb (mb/s)","4475.95 (min 919.65, max 8185.54)"
    "bw_mem-cp-8mb (mb/s)","4463.85 (min 957.85, max 8139.73)"
    "bw_mem-fcp-16mb (mb/s)","1721.19 (min 1653.40, max 1827.74)"
    "bw_mem-fcp-1mb (mb/s)","4820.81 (min 1651.25, max 8118.35)"
    "bw_mem-fcp-2mb (mb/s)","4810.22 (min 1626.55, max 8110.01)"
    "bw_mem-fcp-4mb (mb/s)","4820.09 (min 1644.51, max 8113.59)"
    "bw_mem-fcp-8mb (mb/s)","4827.66 (min 1687.76, max 8106.74)"
    "bw_mem-frd-16mb (mb/s)","1879.68 (min 1832.76, max 1959.34)"
    "bw_mem-frd-1mb (mb/s)","1843.36 (min 1651.25, max 2031.14)"
    "bw_mem-frd-2mb (mb/s)","1761.34 (min 1626.55, max 1903.31)"
    "bw_mem-frd-4mb (mb/s)","1788.46 (min 1644.51, max 1943.63)"
    "bw_mem-frd-8mb (mb/s)","1809.37 (min 1687.76, max 1958.38)"
    "bw_mem-fwr-16mb (mb/s)","7941.45 (min 7825.24, max 8132.84)"
    "bw_mem-fwr-1mb (mb/s)","5081.79 (min 1914.04, max 8428.00)"
    "bw_mem-fwr-2mb (mb/s)","4933.68 (min 1769.29, max 8237.82)"
    "bw_mem-fwr-4mb (mb/s)","4924.74 (min 1812.69, max 8185.54)"
    "bw_mem-fwr-8mb (mb/s)","4918.49 (min 1840.14, max 8139.73)"
    "bw_mem-rd-16mb (mb/s)","1969.37 (min 1920.08, max 2060.79)"
    "bw_mem-rd-1mb (mb/s)","2071.71 (min 1804.73, max 2366.22)"
    "bw_mem-rd-2mb (mb/s)","1795.69 (min 1586.80, max 2011.40)"
    "bw_mem-rd-4mb (mb/s)","1858.30 (min 1694.68, max 2032.18)"
    "bw_mem-rd-8mb (mb/s)","1894.18 (min 1760.95, max 2056.56)"
    "bw_mem-rdwr-16mb (mb/s)","1895.06 (min 1825.03, max 1996.01)"
    "bw_mem-rdwr-1mb (mb/s)","1391.37 (min 902.36, max 1846.04)"
    "bw_mem-rdwr-2mb (mb/s)","1260.18 (min 906.07, max 1682.79)"
    "bw_mem-rdwr-4mb (mb/s)","1357.85 (min 919.65, max 1823.99)"
    "bw_mem-rdwr-8mb (mb/s)","1382.95 (min 957.85, max 1870.91)"
    "bw_mem-wr-16mb (mb/s)","1864.64 (min 1786.71, max 1951.70)"
    "bw_mem-wr-1mb (mb/s)","1855.47 (min 1799.53, max 1978.42)"
    "bw_mem-wr-2mb (mb/s)","1619.04 (min 1547.09, max 1698.08)"
    "bw_mem-wr-4mb (mb/s)","1757.92 (min 1694.68, max 1855.29)"
    "bw_mem-wr-8mb (mb/s)","1806.14 (min 1735.55, max 1907.26)"
    "bw_mmap_rd-mo-1mb (mb/s)","2101.00 (min 2064.95, max 2170.37)"
    "bw_mmap_rd-o2c-1mb (mb/s)","746.69 (min 729.66, max 765.81)"
    "bw_pipe (mb/s)","844.60 (min 834.23, max 858.88)"
    "bw_unix (mb/s)","1171.35 (min 1145.36, max 1187.19)"
    "lat_connect (us)","72.33 (min 71.78, max 72.64)"
    "lat_ctx-2-128k (us)","8.63 (min 7.31, max 9.40)"
    "lat_ctx-2-256k (us)","36.34 (min 34.15, max 40.18)"
    "lat_ctx-4-128k (us)","25.56 (min 24.45, max 26.16)"
    "lat_ctx-4-256k (us)","95.72 (min 89.56, max 102.35)"
    "lat_fs-0k (num_files)","261.33 (min 251.00, max 272.00)"
    "lat_fs-10k (num_files)","124.00 (min 110.00, max 135.00)"
    "lat_fs-1k (num_files)","180.33 (min 167.00, max 189.00)"
    "lat_fs-4k (num_files)","159.00 (min 142.00, max 168.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","30.63 (min 29.52, max 31.38)"
    "lat_mem_rd-stride128-sz125k (ns)","5.57 (min 5.55, max 5.59)"
    "lat_mem_rd-stride128-sz250k (ns)","5.84 (min 5.84, max 5.85)"
    "lat_mem_rd-stride128-sz31k (ns)","3.51 (min 2.15, max 4.19)"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","10.65 (min 9.53, max 12.90)"
    "lat_mem_rd-stride128-sz62k (ns)","5.25 (min 5.24, max 5.25)"
    "lat_mmap-1m (us)","52.00 (min 50.00, max 56.00)"
    "lat_ops-double-add (ns)","2.86 (min 2.86, max 2.87)"
    "lat_ops-double-div (ns)","15.74"
    "lat_ops-double-mul (ns)","2.86"
    "lat_ops-float-add (ns)","2.86"
    "lat_ops-float-div (ns)","9.30 (min 9.30, max 9.31)"
    "lat_ops-float-mul (ns)","2.86"
    "lat_ops-int-add (ns)","0.72"
    "lat_ops-int-bit (ns)","0.48"
    "lat_ops-int-div (ns)","4.30 (min 4.29, max 4.30)"
    "lat_ops-int-mod (ns)","4.53 (min 4.53, max 4.54)"
    "lat_ops-int-mul (ns)","3.09 (min 3.05, max 3.12)"
    "lat_ops-int64-add (ns)","0.72"
    "lat_ops-int64-bit (ns)","0.48"
    "lat_ops-int64-div (ns)","6.80"
    "lat_ops-int64-mod (ns)","5.26 (min 5.25, max 5.27)"
    "lat_ops-int64-mul (ns)","3.54"
    "lat_pagefault (us)","0.44 (min 0.44, max 0.45)"
    "lat_pipe (us)","20.44 (min 18.08, max 21.82)"
    "lat_proc-exec (us)","697.63 (min 678.88, max 708.50)"
    "lat_proc-fork (us)","611.65 (min 585.50, max 627.56)"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","31.61 (min 31.47, max 31.83)"
    "lat_sem (us)","2.62 (min 2.43, max 2.91)"
    "lat_sig-catch (us)","5.70 (min 5.66, max 5.76)"
    "lat_sig-install (us)","0.61 (min 0.61, max 0.62)"
    "lat_sig-prot (us)","0.80 (min 0.72, max 0.87)"
    "lat_syscall-fstat (us)","1.82 (min 1.77, max 1.89)"
    "lat_syscall-null (us)","0.39 (min 0.37, max 0.41)"
    "lat_syscall-open (us)","165.98 (min 155.17, max 179.14)"
    "lat_syscall-read (us)","0.71"
    "lat_syscall-stat (us)","4.28 (min 4.22, max 4.32)"
    "lat_syscall-write (us)","0.67"
    "lat_tcp (us)","0.76"
    "lat_unix (us)","26.29 (min 21.53, max 29.44)"
    "latency_for_0.50_mb_block_size (nanosec)","10.65 (min 9.53, max 12.90)"
    "latency_for_1.00_mb_block_size (nanosec)","15.31 (min 0.00, max 31.38)"
    "pipe_bandwidth (mb\s)","844.60 (min 834.23, max 858.88)"
    "pipe_latency (microsec)","20.44 (min 18.08, max 21.82)"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","31.61 (min 31.47, max 31.83)"
    "semaphore_latency (microsec)","2.62 (min 2.43, max 2.91)"
    "signal_handler_latency (microsec)","0.61 (min 0.61, max 0.62)"
    "signal_handler_overhead (microsec)","5.70 (min 5.66, max 5.76)"
    "tcp_ip_connection_cost_to_localhost (microsec)","72.33 (min 71.78, max 72.64)"
    "tcp_latency_using_localhost (microsec)","0.76"


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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cpu_clock (mhz)","1400.00"
    "dhrystone_per_mhz (dmips/mhz)","2.76 (min 2.70, max 2.80)"
    "dhrystone_per_second (dhrystonep)","6804597.50 (min 6666666.50, max 6896551.50)"


Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

.. code-block:: console

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "whetstone (mips)","5000.00"


Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "linpack (kflops)","580891.00 (min 579075.00, max 583058.00)"


NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "assignment (iterations)","14.13 (min 14.08, max 14.16)"
    "fourier (iterations)","19386.00 (min 19371.00, max 19401.00)"
    "fp_emulation (iterations)","204.44 (min 204.42, max 204.45)"
    "huffman (iterations)","1189.68 (min 1188.40, max 1191.00)"
    "idea (iterations)","3069.03 (min 3067.40, max 3070.70)"
    "lu_decomposition (iterations)","531.94 (min 531.30, max 533.32)"
    "neural_net (iterations)","9.68 (min 9.67, max 9.68)"
    "numeric_sort (iterations)","542.03 (min 539.04, max 543.78)"
    "string_sort (iterations)","165.90 (min 163.60, max 168.20)"


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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "add (mb/s)","2739.62 (min 2693.40, max 2872.40)"
    "copy (mb/s)","3784.96 (min 3717.50, max 3962.10)"
    "scale (mb/s)","3523.64 (min 3456.90, max 3702.70)"
    "triad (mb/s)","2428.74 (min 2395.30, max 2524.50)"



CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark\ |reg|-Pro is a comprehensive, advanced processor benchmark that works
with and enhances the market-proven industry-standard EEMBC CoreMark\ |reg|
benchmark. While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the
entire processor, adding comprehensive support for multicore technology, a
combination of integer and floating-point workloads, and data sets for utilizing
larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","41.89 (min 41.67, max 42.02)"
    "core (workloads/)","0.30"
    "coremark-pro ()","955.64 (min 954.10, max 956.91)"
    "linear_alg-mid-100x100-sp (workloads/)","14.68"
    "loops-all-mid-10k-sp (workloads/)","0.71"
    "nnet_test (workloads/)","1.08"
    "parser-125k (workloads/)","9.28 (min 9.26, max 9.35)"
    "radix2-big-64k (workloads/)","74.93 (min 73.55, max 75.90)"
    "sha-test (workloads/)","81.30"
    "zip-test (workloads/)","23.53 (min 23.26, max 23.81)"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","83.16 (min 82.64, max 83.33)"
    "core (workloads/)","0.60"
    "coremark-pro ()","1689.37 (min 1686.54, max 1692.03)"
    "linear_alg-mid-100x100-sp (workloads/)","29.35 (min 29.33, max 29.36)"
    "loops-all-mid-10k-sp (workloads/)","1.30 (min 1.30, max 1.31)"
    "nnet_test (workloads/)","2.15"
    "parser-125k (workloads/)","16.39"
    "radix2-big-64k (workloads/)","64.30 (min 63.95, max 64.87)"
    "sha-test (workloads/)","161.29"
    "zip-test (workloads/)","45.45"


Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62pxx_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","17.35 (min 16.78, max 19.03)"


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

    "11025","352798.40 (min 352797.00, max 352800.00)","0.11 (min 0.10, max 0.12)"
    "16000","511998.60 (min 511996.00, max 512000.00)","0.23 (min 0.09, max 0.71)"
    "22050","705594.80 (min 705593.00, max 705596.00)","0.14 (min 0.13, max 0.16)"
    "24000","705596.80 (min 705594.00, max 705599.00)","0.15 (min 0.14, max 0.18)"
    "32000","1023996.20 (min 1023991.00, max 1023999.00)","0.20 (min 0.10, max 0.56)"
    "44100","1411194.40 (min 1411188.00, max 1411199.00)","0.22 (min 0.21, max 0.23)"
    "48000","1535994.20 (min 1535987.00, max 1535999.00)","0.12 (min 0.09, max 0.16)"
    "88200","2822385.40 (min 2822372.00, max 2822394.00)","0.36 (min 0.33, max 0.38)"
    "96000","3071974.80 (min 3071963.00, max 3071995.00)","0.33 (min 0.13, max 1.01)"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62pxx_sk-fs: Throughput (bits/sec)","am62pxx_sk-fs: CPU Load (%)"

    "11025","352947.25 (min 352947.00, max 352948.00)","0.11 (min 0.09, max 0.13)"
    "16000","512214.25 (min 512213.00, max 512215.00)","0.12 (min 0.10, max 0.13)"
    "22050","705893.00 (min 705891.00, max 705896.00)","0.13 (min 0.11, max 0.15)"
    "24000","705894.50 (min 705893.00, max 705896.00)","0.14 (min 0.12, max 0.15)"
    "32000","1024427.50 (min 1024425.00, max 1024429.00)","0.13 (min 0.10, max 0.15)"
    "44100","1411789.25 (min 1411787.00, max 1411791.00)","0.19 (min 0.17, max 0.21)"
    "48000","1536641.25 (min 1536639.00, max 1536643.00)","0.13 (min 0.10, max 0.16)"
    "88200","2823575.00 (min 2823571.00, max 2823578.00)","0.29 (min 0.25, max 0.31)"
    "96000","3073262.00 (min 3073247.00, max 3073268.00)","0.17 (min 0.11, max 0.20)"


|

Graphics SGX/RGX Driver
-------------------------
 

GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62pxx_sk-fs: Score","am62pxx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","907.06 (min 904.67, max 910.18)","14.63 (min 14.59, max 14.68)"
    " GFXBench 3.x gl_trex_off","1583.29 (min 1581.08, max 1585.25)","28.27 (min 28.23, max 28.31)"
    " GFXBench 5.x gl_5_high_off","114.96 (min 114.84, max 115.06)","1.79"


Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62pxx_sk-fs: Score"

    "Glmark2-DRM","306.40 (min 306.00, max 307.00)"
    "Glmark2-Wayland","776.40 (min 765.00, max 786.00)"


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

- CPSW3g: AM62px

TCP Bidirectional Throughput
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1828.16","43.22"

TCP Bidirectional Throughput Interrupt Pacing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1789.37","41.18"

UDP Throughput
~~~~~~~~~~~~~~

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)", "am62pxx_sk-fs: THROUGHPUT (Mbits/sec)", "am62pxx_sk-fs: Packets Per Second (kPPS)", "am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","46.50","91","37.58"
    "128","90.35","88","37.33"
    "256","179.38","88","37.18"
    "1024","673.26","82","35.55"
    "1518","956.86","81","40.26"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)", "am62pxx_sk-fs: THROUGHPUT (Mbits/sec)", "am62pxx_sk-fs: Packets Per Second (kPPS)", "am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","30.46","59","9.72"
    "128","64.61","63","12.30"
    "256","156.26","76","16.65"
    "1024","939.47","115","36.24"
    "1518","908.82","77","36.28"

|

Linux OSPI Flash Driver
-------------------------


.. rubric:: AM62PXX-SK
   :name: am62pxx-sk-ospi


.. rubric:: UBIFS
   :name: am62pxx-sk-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Write UBIFS CPU Load (%)","am62pxx_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Read UBIFS CPU Load (%)"

    "102400","0.16 (min 0.11, max 0.27)","28.44 (min 24.76, max 32.16)","28.39 (min 28.16, max 28.59)","7.29 (min 3.45, max 10.00)"
    "262144","0.13 (min 0.10, max 0.17)","30.44 (min 26.91, max 33.00)","28.29 (min 28.00, max 28.51)","6.85 (min 6.67, max 6.90)"
    "524288","0.13 (min 0.10, max 0.18)","29.84 (min 24.90, max 35.23)","28.13 (min 27.77, max 28.30)","7.84 (min 3.45, max 12.50)"
    "1048576","0.13 (min 0.10, max 0.18)","30.87 (min 25.61, max 35.17)","27.93 (min 27.70, max 28.12)","5.98 (min 3.45, max 12.90)"


.. rubric:: RAW
   :name: am62pxx-sk-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62pxx_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","37.50 (min 35.97, max 37.88)"


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

    "1m","91.56 (min 91.00, max 93.00)","1.62 (min 1.57, max 1.68)","284.60 (min 274.00, max 289.00)","2.75 (min 2.27, max 3.03)"
    "4m","96.84 (min 96.70, max 97.00)","1.11 (min 1.02, max 1.18)","254.40 (min 187.00, max 288.00)","1.89 (min 1.60, max 2.07)"
    "4k","79.20 (min 78.70, max 79.70)","23.82 (min 23.13, max 24.69)","88.18 (min 81.40, max 93.40)","19.43 (min 17.01, max 21.58)"
    "256k","91.54 (min 90.80, max 92.70)","2.00 (min 1.74, max 2.15)","290.00 (min 288.00, max 293.00)","4.05 (min 4.00, max 4.11)"


EMMC RAW FIO 1G
^^^^^^^^^^^^^^^


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "1m","90.48 (min 89.60, max 91.30)","1.38 (min 1.26, max 1.52)","293.60 (min 293.00, max 294.00)","2.62 (min 2.27, max 2.83)"
    "4m","96.80 (min 96.30, max 97.20)","1.02 (min 0.96, max 1.09)","264.20 (min 182.00, max 294.00)","1.86 (min 1.41, max 2.04)"
    "4k","75.56 (min 74.30, max 76.60)","17.70 (min 17.40, max 18.04)","86.46 (min 77.30, max 90.20)","17.35 (min 14.42, max 19.03)"
    "256k","90.44 (min 89.80, max 91.20)","1.77 (min 1.57, max 1.92)","293.40 (min 293.00, max 294.00)","3.85 (min 3.50, max 4.11)"


EMMC EXT4
^^^^^^^^^


.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","91.94 (min 87.85, max 94.24)","3.67 (min 2.66, max 5.43)","178.75 (min 177.43, max 179.20)","5.40 (min 4.76, max 6.78)"
    "262144","84.25 (min 48.91, max 94.48)","2.46 (min 1.51, max 4.08)","180.88 (min 180.62, max 181.14)","4.58 (min 4.33, max 5.15)"
    "524288","80.67 (min 50.44, max 94.58)","2.36 (min 1.32, max 4.10)","180.68 (min 176.90, max 181.92)","5.17 (min 4.33, max 5.65)"
    "1048576","78.31 (min 50.01, max 94.61)","2.46 (min 1.21, max 6.71)","181.58 (min 181.25, max 181.87)","4.87 (min 4.35, max 5.70)"
    "5242880","78.19 (min 50.39, max 94.91)","2.46 (min 1.29, max 4.04)","180.96 (min 178.96, max 181.81)","5.38 (min 5.17, max 5.65)"


EMMC EXT2
^^^^^^^^^


.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT2 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT2 CPU Load (%)","am62pxx_sk-fs: Read EXT2 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT2 CPU Load (%)"

    "102400","46.25 (min 23.67, max 56.24)","4.43 (min 2.27, max 8.30)","193.46 (min 188.27, max 198.75)","6.98 (min 6.31, max 7.87)"
    "262144","47.52 (min 25.94, max 69.50)","3.66 (min 1.47, max 9.22)","267.41 (min 259.42, max 288.15)","8.66 (min 7.50, max 9.32)"
    "524288","56.34 (min 27.85, max 81.77)","3.91 (min 1.24, max 9.23)","263.76 (min 257.68, max 270.37)","8.34 (min 6.45, max 10.19)"
    "1048576","59.61 (min 28.56, max 84.85)","3.49 (min 1.30, max 9.38)","265.84 (min 261.64, max 270.01)","9.09 (min 6.96, max 11.66)"
    "5242880","64.00 (min 31.03, max 92.26)","3.33 (min 1.43, max 8.77)","269.22 (min 266.95, max 273.97)","9.38 (min 7.24, max 11.32)"


EMMC VFAT
^^^^^^^^^


.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Write VFAT CPU Load (%)","am62pxx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Read VFAT CPU Load (%)"

    "102400","39.50 (min 11.48, max 52.78)","4.96 (min 3.90, max 6.55)","210.15 (min 209.96, max 210.42)","11.00 (min 10.20, max 12.00)"
    "262144","44.48 (min 12.06, max 63.22)","5.77 (min 4.24, max 7.98)","287.82 (min 286.33, max 289.47)","13.80 (min 12.77, max 15.07)"
    "524288","51.05 (min 12.19, max 73.73)","5.23 (min 3.71, max 7.37)","286.77 (min 284.09, max 288.75)","13.91 (min 12.50, max 14.97)"
    "1048576","51.71 (min 12.35, max 75.40)","4.93 (min 3.53, max 6.49)","285.14 (min 282.47, max 286.71)","13.73 (min 12.50, max 14.38)"
    "5242880","55.89 (min 12.48, max 81.76)","5.26 (min 3.67, max 7.74)","285.90 (min 285.00, max 287.53)","15.52 (min 14.58, max 16.44)"


UBoot EMMC Driver
-----------------


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","97216.82 (min 94160.92, max 100207.95)","242610.29 (min 208713.38, max 287438.60)"
    "4000000","96964.20 (min 95533.53, max 99146.75)","259018.23 (min 226768.17, max 300623.85)"



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

    "1m","42.76 (min 42.00, max 43.70)","1.01 (min 0.96, max 1.08)","86.38 (min 85.10, max 87.50)","1.35 (min 1.31, max 1.41)"
    "4m","42.96 (min 42.30, max 43.90)","0.72 (min 0.70, max 0.75)","85.98 (min 85.00, max 87.30)","0.89 (min 0.82, max 0.94)"
    "4k","2.82 (min 2.79, max 2.87)","1.59 (min 1.57, max 1.62)","13.24 (min 12.90, max 14.10)","4.04 (min 3.72, max 4.44)"
    "256k","39.36 (min 38.50, max 40.30)","1.27 (min 1.14, max 1.40)","84.08 (min 83.30, max 84.50)","1.49 (min 1.37, max 1.53)"


MMC RAW FIO 1G
^^^^^^^^^^^^^^


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "1m","43.78 (min 42.20, max 45.50)","0.91 (min 0.87, max 0.98)","88.18 (min 88.00, max 88.30)","1.19 (min 1.08, max 1.28)"
    "4m","43.76 (min 42.20, max 45.50)","0.68 (min 0.66, max 0.70)","88.18 (min 88.10, max 88.30)","0.90 (min 0.78, max 0.97)"
    "4k","2.82 (min 2.82, max 2.83)","1.33 (min 1.27, max 1.43)","12.94 (min 12.60, max 13.10)","3.67 (min 3.58, max 3.74)"
    "256k","38.62 (min 36.20, max 41.80)","1.08 (min 0.98, max 1.22)","84.30 (min 84.10, max 84.50)","1.50 (min 1.47, max 1.53)"
 


MMC EXT4
^^^^^^^^


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.88 (min 10.58, max 11.14)","0.53 (min 0.39, max 0.71)","11.10 (min 10.89, max 11.83)","0.47 (min 0.39, max 0.57)"
    "262144","10.84 (min 10.14, max 11.15)","0.42 (min 0.23, max 0.64)","11.03 (min 11.01, max 11.04)","0.51 (min 0.34, max 0.89)"
    "524288","10.79 (min 10.54, max 11.11)","0.39 (min 0.25, max 0.75)","11.17 (min 11.08, max 11.30)","0.37 (min 0.32, max 0.45)"
    "1048576","10.95 (min 10.60, max 11.38)","0.38 (min 0.26, max 0.58)","11.57 (min 11.05, max 12.03)","0.43 (min 0.37, max 0.46)"
    "5242880","11.09 (min 10.84, max 11.34)","0.39 (min 0.29, max 0.61)","12.02 (min 12.01, max 12.03)","0.45 (min 0.40, max 0.49)"


MMC EXT3
^^^^^^^^



.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","33.33 (min 29.56, max 37.01)","2.02 (min 1.26, max 4.00)","71.78 (min 69.72, max 73.64)","2.82 (min 2.35, max 3.28)"
    "262144","35.43 (min 30.67, max 43.47)","1.60 (min 0.94, max 3.66)","79.52 (min 75.70, max 82.26)","3.05 (min 2.19, max 4.69)"
    "524288","34.89 (min 30.56, max 39.34)","1.67 (min 0.99, max 3.74)","80.20 (min 74.71, max 84.35)","2.96 (min 2.50, max 3.56)"
    "1048576","36.11 (min 30.69, max 39.71)","1.64 (min 0.86, max 3.85)","83.46 (min 81.92, max 86.05)","3.47 (min 3.12, max 3.75)"
    "5242880","36.53 (min 31.76, max 40.54)","1.61 (min 0.99, max 3.50)","85.86 (min 82.73, max 86.90)","3.40 (min 2.89, max 3.91)"



MMC EXT2
^^^^^^^^
 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","14.71 (min 3.24, max 20.60)","1.74 (min 1.55, max 1.94)","72.31 (min 66.07, max 75.54)","2.79 (min 2.35, max 3.27)"
    "262144","23.26 (min 3.30, max 33.41)","1.96 (min 1.46, max 2.77)","79.42 (min 78.37, max 80.81)","3.22 (min 2.65, max 3.90)"
    "524288","29.61 (min 3.44, max 44.72)","1.61 (min 1.22, max 2.07)","86.23 (min 80.19, max 90.77)","3.27 (min 2.60, max 4.00)"
    "1048576","28.26 (min 3.59, max 38.31)","1.45 (min 0.80, max 1.79)","84.14 (min 81.69, max 85.19)","3.10 (min 2.41, max 3.66)"
    "5242880","30.55 (min 3.74, max 41.95)","1.26 (min 0.48, max 1.96)","87.29 (min 85.64, max 89.15)","3.01 (min 2.73, max 3.27)"


 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 


UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","31156.51 (min 23272.73, max 39384.62)","82158.83 (min 81920.00, max 83591.84)"
    "800000","45106.57 (min 41795.92, max 48473.37)","87148.94"
    "1000000","46442.00 (min 37838.34, max 49799.39)","89530.82 (min 89043.48, max 90021.98)"


The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 

|

USB Driver
-------------------------


USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","38.30 (min 37.50, max 38.80)"


.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","32.28 (min 29.40, max 33.90)"


|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62pxx_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","22631.94 (min 22081.88, max 23320.58)"
    "aes-128-cbc","16","467.10 (min 448.62, max 481.11)"
    "aes-128-cbc","16384","87726.31 (min 87108.27, max 88451.75)"
    "aes-128-cbc","256","7726.65 (min 7375.79, max 8021.76)"
    "aes-128-cbc","64","2057.17 (min 1943.51, max 2133.48)"
    "aes-128-cbc","8192","74890.35 (min 73992.87, max 75737.77)"
    "aes-128-ecb","1024","22978.56 (min 22504.45, max 23572.82)"
    "aes-128-ecb","16","476.81 (min 455.95, max 496.05)"
    "aes-128-ecb","16384","89903.56 (min 89265.49, max 90488.83)"
    "aes-128-ecb","256","7840.37 (min 7391.40, max 8190.29)"
    "aes-128-ecb","64","2104.39 (min 1973.74, max 2204.10)"
    "aes-128-ecb","8192","76683.95 (min 75647.66, max 77635.58)"
    "aes-192-cbc","1024","22110.78 (min 21732.35, max 22834.18)"
    "aes-192-cbc","16","467.78 (min 450.28, max 485.47)"
    "aes-192-cbc","16384","78685.98 (min 78528.51, max 79096.49)"
    "aes-192-cbc","256","7648.55 (min 7307.52, max 7929.17)"
    "aes-192-cbc","64","2052.64 (min 1932.71, max 2148.35)"
    "aes-192-cbc","8192","68420.04 (min 67502.08, max 69069.48)"
    "aes-192-ecb","1024","22689.62 (min 22192.81, max 23397.72)"
    "aes-192-ecb","16","478.69 (min 458.64, max 498.08)"
    "aes-192-ecb","16384","81073.49 (min 80270.68, max 81570.47)"
    "aes-192-ecb","256","7822.41 (min 7405.14, max 8148.31)"
    "aes-192-ecb","64","2116.24 (min 1994.79, max 2202.30)"
    "aes-192-ecb","8192","70169.94 (min 68501.50, max 71193.94)"
    "aes-256-cbc","1024","21578.75 (min 21215.23, max 22174.38)"
    "aes-256-cbc","16","466.91 (min 447.21, max 482.93)"
    "aes-256-cbc","16384","71731.88 (min 71346.86, max 72171.52)"
    "aes-256-cbc","256","7575.15 (min 7258.28, max 7839.49)"
    "aes-256-cbc","64","2044.43 (min 1944.64, max 2116.65)"
    "aes-256-cbc","8192","63040.63 (min 61977.94, max 63733.76)"
    "aes-256-ecb","1024","22039.27 (min 21698.56, max 22506.15)"
    "aes-256-ecb","16","476.24 (min 454.86, max 498.13)"
    "aes-256-ecb","16384","73474.96 (min 72624.81, max 74350.59)"
    "aes-256-ecb","256","7790.11 (min 7389.18, max 8175.62)"
    "aes-256-ecb","64","2100.60 (min 1977.58, max 2205.50)"
    "aes-256-ecb","8192","64469.22 (min 62450.35, max 65230.17)"
    "sha256","1024","31300.72 (min 30609.07, max 31860.74)"
    "sha256","16","520.84 (min 514.59, max 527.77)"
    "sha256","16384","275873.79 (min 273683.80, max 281520.81)"
    "sha256","256","8161.62 (min 8053.67, max 8233.81)"
    "sha256","64","2060.27 (min 2031.27, max 2082.54)"
    "sha256","8192","180412.87 (min 177307.65, max 184205.31)"
    "sha512","1024","26502.71 (min 26117.80, max 26698.07)"
    "sha512","16","507.12 (min 498.42, max 511.47)"
    "sha512","16384","110221.54 (min 109750.95, max 111017.98)"
    "sha512","256","7512.97 (min 7395.84, max 7748.86)"
    "sha512","64","2029.75 (min 1995.65, max 2046.74)"
    "sha512","8192","90879.77 (min 90016.43, max 91772.25)"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62pxx_sk-fs: CPU Load"

    "aes-128-cbc","32.33 (min 32.00, max 33.00)"
    "aes-128-ecb","34.00 (min 33.00, max 36.00)"
    "aes-192-cbc","32.33 (min 32.00, max 33.00)"
    "aes-192-ecb","33.33 (min 32.00, max 35.00)"
    "aes-256-cbc","32.33 (min 32.00, max 33.00)"
    "aes-256-ecb","32.67 (min 32.00, max 34.00)"
    "sha256","96.00"
    "sha512","96.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc

.. _crypto-performance:

Crypto Performance Comparison
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows different AES/SHA algorithms throughput measured using openssl speed across the SA3UL accelerator, ARM Cryptographic Extension (CE), and baseline ARM CPU.

.. csv-table:: Crypto Accelerator Performance
   :header: "Algorithm", "Size (bytes)", "Accelerator (MB/s)", "ARM CE (MB/s)", "ARM (MB/s)"
   :widths: 20, 25, 20, 20, 20

   "aes-128-cbc", "16", "0.47", "97.47", "31.46"
   "aes-128-cbc", "64", "2.08", "304.38", "39.87"
   "aes-128-cbc", "256", "7.77", "636.65", "42.97"
   "aes-128-cbc", "1024", "21.90", "895.63", "43.82"
   "aes-128-cbc", "8192", "73.61", "1018.95", "44.05"
   "aes-128-cbc", "16384", "85.81", "1028.09", "44.00"
   "aes-128-ecb", "16 bytes", "0.46", "99.15", "32.46"
   "aes-128-ecb", "64 bytes", "2.02", "274.23", "40.20"
   "aes-128-ecb", "256 bytes", "7.56", "632.64", "42.90"
   "aes-128-ecb", "1024 bytes", "21.44", "956.29", "43.62"
   "aes-128-ecb", "8192 bytes", "73.88", "1128.84", "43.84"
   "aes-128-ecb", "16384 bytes", "86.22", "1142.84", "43.85"
   "aes-192-cbc", "16 bytes", "0.46", "93.63", "27.73"
   "aes-192-cbc", "64 bytes", "2.02", "275.39", "34.38"
   "aes-192-cbc", "256 bytes", "7.58", "526.58", "36.76"
   "aes-192-cbc", "1024 bytes", "21.35", "694.33", "37.41"
   "aes-192-cbc", "8192 bytes", "67.50", "766.00", "37.60"
   "aes-192-cbc", "16384 bytes", "77.46", "770.55", "37.59"
   "aes-192-ecb", "16 bytes", "0.48", "100.15", "29.42"
   "aes-192-ecb", "64 bytes", "2.11", "270.42", "35.47"
   "aes-192-ecb", "256 bytes", "7.87", "598.99", "37.51"
   "aes-192-ecb", "1024 bytes", "21.78", "872.68", "38.05"
   "aes-192-ecb", "8192 bytes", "69.06", "1005.89", "38.21"
   "aes-192-ecb", "16384 bytes", "78.82", "1016.48", "38.21"
   "aes-256-cbc", "16 bytes", "0.46", "91.27", "25.26"
   "aes-256-cbc", "64 bytes", "2.02", "256.04", "30.42"
   "aes-256-cbc", "256 bytes", "7.51", "460.32", "32.19"
   "aes-256-cbc", "1024 bytes", "20.91", "584.52", "32.66"
   "aes-256-cbc", "8192 bytes", "62.41", "633.94", "32.81"
   "aes-256-cbc", "16384 bytes", "70.57", "637.81", "32.80"
   "aes-256-ecb", "16 bytes", "0.43", "94.32", "25.78"
   "aes-256-ecb", "64 bytes", "1.96", "250.11", "30.44"
   "aes-256-ecb", "256 bytes", "7.63", "524.03", "31.96"
   "aes-256-ecb", "1024 bytes", "21.06", "753.56", "32.37"
   "aes-256-ecb", "8192 bytes", "62.42", "856.83", "32.49"
   "aes-256-ecb", "16384 bytes", "69.74", "862.89", "32.49"
   "sha2-256", "16 bytes", "0.49", "11.69", "7.52"
   "sha2-256", "64 bytes", "1.93", "42.92", "22.19"
   "sha2-256", "256 bytes", "7.67", "141.05", "50.35"
   "sha2-256", "1024 bytes", "29.16", "327.85", "74.04"
   "sha2-256", "8192 bytes", "170.04", "537.19", "85.80"
   "sha2-256", "16384 bytes", "260.84", "561.95", "86.76"
   "sha2-512", "16 bytes", "0.48", "7.15", "7.22"
   "sha2-512", "64 bytes", "1.95", "28.33", "28.69"
   "sha2-512", "256 bytes", "7.18", "61.82", "62.65"
   "sha2-512", "1024 bytes", "25.59", "105.46", "106.05"
   "sha2-512", "8192 bytes", "87.32", "132.92", "133.00"
   "sha2-512", "16384 bytes", "105.99", "135.39", "135.40"

.. csv-table:: CPU Usage %
   :header: "Algorithm", "Accelerator (%)", "ARM CE (%)", "ARM (%)"
   :widths: 25, 25, 25, 25

   "aes-128-cbc", "33%", "99%", "99%"
   "aes-128-ecb", "33%", "99%", "99%"
   "aes-192-cbc", "32%", "99%", "99%"
   "aes-192-ecb", "32%", "99%", "99%"
   "aes-256-cbc", "31%", "99%", "99%"
   "aes-256-ecb", "26%", "99%", "99%"
   "sha2-256", "95%", "99%", "99%"
   "sha2-512", "66%", "99%", "99%"

|

Low Power Performance
---------------------

Power Performance
^^^^^^^^^^^^^^^^^

.. csv-table:: I/O Only + DDR Power Performance
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","0.00"
   "vddr_core","0.85","0.00"
   "soc_dvdd_3v3","3.30","2.11"
   "soc_dvdd_1v8","1.80","8.42"
   "vdda_1v8","1.80","0.10"
   "vdd_lpddr4","1.10","4.21"
   "Total"," ","14.84"

.. csv-table:: DeepSleep Power Performance
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","16.70"
   "vddr_core","0.85","1.31"
   "soc_dvdd_3v3","3.30","5.68"
   "soc_dvdd_1v8","1.80","2.60"
   "vdda_1v8","1.80","2.15"
   "vdd_lpddr4","1.10","3.27"
   "Total"," ","31.71"

.. csv-table:: MCU Only Power Performance
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","154.64"
   "vddr_core","0.85","1.96"
   "soc_dvdd_3v3","3.30","5.67"
   "soc_dvdd_1v8","1.80","2.74"
   "vdda_1v8","1.80","10.63"
   "vdd_lpddr4","1.10","4.06"
   "Total"," ","179.69"

Partial I/O Data
- All voltage rails were measured to be near 0V

.. note::

   The power consumption on the vdda_1v8 rail does not include an
   oscillator on the rail that has significant current consumption.

.. note::

   The measurements shown are from an AM62Px SK rev E1-1. Results may vary based off of the board revision being used.
   For the most accurate power measurements, use the latest TIVA firmware.

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)

Resume Latency Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: LPM Resume Latency Performance
   :header: "Low Power Mode","Total Resume Latency (ms)"

   "I/O Only + DDR", "606"
   "DeepSleep", "145"
   "MCU Only", "92"

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
