.. include:: <isonum.txt>

======================================
 RT-linux 09.01.00 Performance Guide
======================================

.. rubric::  **Read This First**
   :name: read-this-first-rt-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+---------------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                         |
+================+=====================================================================================================================+
| AM64x SK       | AM64x Starter Kit rev A with ARM running at 1GHz, LPDDR4 data rate 1600 MT/S                                        |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| AM65x EVM      | AM65x Evaluation Module rev 2.0 with ARM running at 800MHz, DDR4-2400 (1600 MT/S), TMDX654IDKEVM                    |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| AM62x SK       | AM62x Starter Kit rev A with ARM running at 1400 MHz, DDR4 data rate 1600 MT/S                                      |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| AM62A SK       | AM62A Starter Kit rev E3 with ARM running at 1866MHz, LPDDR4 data rate 3733 MT/S                                    |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| AM62P SK       | AM62P Starter Kit rev E1 with ARM running at 1200MHz, LPDDR4 data rate 3200 MT/S                                    |
+----------------+---------------------------------------------------------------------------------------------------------------------+



Table:  Evaluation Modules

|

.. rubric::  About This Manual
   :name: about-this-manual-rt-kernel-perf-guide

This document provides performance data for each of the device drivers
which are part of the Processor SDK Linux package. This document should be
used in conjunction with release notes and user guides provided with the
Processor SDK Linux package for information on specific issues present
with drivers included in a particular release.

.. rubric::  If You Need Assistance
   :name: if-you-need-assistance-rt-kernel-perf-guide

For further information or to report any problems, contact
http://e2e.ti.com/ or http://support.ti.com/


System Benchmarks
-------------------------

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

.. csv-table::
    :header: "Benchmarks","am64xx-hsevm: perf","am654x-evm: perf"

    "af_unix_sock_stream_latency (microsec)","34.49","68.44"
    "af_unix_socket_stream_bandwidth (MBs)","578.92","986.93"
    "bw_file_rd-io-1mb (MB/s)","840.90","1091.70"
    "bw_file_rd-o2c-1mb (MB/s)","510.55","638.37"
    "bw_mem-bcopy-16mb (MB/s)","851.38","905.54"
    "bw_mem-bcopy-1mb (MB/s)","997.21","1233.92"
    "bw_mem-bcopy-2mb (MB/s)","941.62","970.72"
    "bw_mem-bcopy-4mb (MB/s)","956.71","910.75"
    "bw_mem-bcopy-8mb (MB/s)","976.80","904.47"
    "bw_mem-bzero-16mb (MB/s)","2119.77","2021.48"
    "bw_mem-bzero-1mb (MB/s)","1559.24 (min 997.21, max 2121.27)","2847.91 (min 1233.92, max 4461.90)"
    "bw_mem-bzero-2mb (MB/s)","1529.76 (min 941.62, max 2117.90)","2222.14 (min 970.72, max 3473.56)"
    "bw_mem-bzero-4mb (MB/s)","1537.31 (min 956.71, max 2117.90)","1608.12 (min 910.75, max 2305.48)"
    "bw_mem-bzero-8mb (MB/s)","1547.72 (min 976.80, max 2118.64)","1475.26 (min 904.47, max 2046.04)"
    "bw_mem-cp-16mb (MB/s)","520.16","582.98"
    "bw_mem-cp-1mb (MB/s)","659.86 (min 529.57, max 790.14)","1402.49 (min 775.34, max 2029.63)"
    "bw_mem-cp-2mb (MB/s)","686.72 (min 578.95, max 794.49)","849.54 (min 616.05, max 1083.03)"
    "bw_mem-cp-4mb (MB/s)","689.96 (min 556.95, max 822.96)","717.69 (min 587.46, max 847.91)"
    "bw_mem-cp-8mb (MB/s)","707.95 (min 576.70, max 839.19)","694.50 (min 593.60, max 795.39)"
    "bw_mem-fcp-16mb (MB/s)","891.81","892.26"
    "bw_mem-fcp-1mb (MB/s)","1615.27 (min 1109.26, max 2121.27)","2806.55 (min 1151.19, max 4461.90)"
    "bw_mem-fcp-2mb (MB/s)","1601.25 (min 1084.60, max 2117.90)","2219.80 (min 966.03, max 3473.56)"
    "bw_mem-fcp-4mb (MB/s)","1612.51 (min 1107.11, max 2117.90)","1599.92 (min 894.35, max 2305.48)"
    "bw_mem-fcp-8mb (MB/s)","1615.50 (min 1112.35, max 2118.64)","1477.26 (min 908.47, max 2046.04)"
    "bw_mem-frd-16mb (MB/s)","1261.23","1168.65"
    "bw_mem-frd-1mb (MB/s)","1187.09 (min 1109.26, max 1264.91)","1360.53 (min 1151.19, max 1569.86)"
    "bw_mem-frd-2mb (MB/s)","1208.97 (min 1084.60, max 1333.33)","1175.78 (min 966.03, max 1385.52)"
    "bw_mem-frd-4mb (MB/s)","1209.62 (min 1107.11, max 1312.12)","1058.05 (min 894.35, max 1221.75)"
    "bw_mem-frd-8mb (MB/s)","1197.41 (min 1112.35, max 1282.46)","1057.46 (min 908.47, max 1206.45)"
    "bw_mem-fwr-16mb (MB/s)","837.52","791.88"
    "bw_mem-fwr-1mb (MB/s)","1027.53 (min 790.14, max 1264.91)","1799.75 (min 1569.86, max 2029.63)"
    "bw_mem-fwr-2mb (MB/s)","1063.91 (min 794.49, max 1333.33)","1234.28 (min 1083.03, max 1385.52)"
    "bw_mem-fwr-4mb (MB/s)","1067.54 (min 822.96, max 1312.12)","1034.83 (min 847.91, max 1221.75)"
    "bw_mem-fwr-8mb (MB/s)","1060.83 (min 839.19, max 1282.46)","1000.92 (min 795.39, max 1206.45)"
    "bw_mem-rd-16mb (MB/s)","1353.75","1207.46"
    "bw_mem-rd-1mb (MB/s)","1108.24 (min 854.55, max 1361.93)","3248.89 (min 3232.76, max 3265.01)"
    "bw_mem-rd-2mb (MB/s)","1103.44 (min 847.94, max 1358.93)","1426.50 (min 1328.90, max 1524.10)"
    "bw_mem-rd-4mb (MB/s)","1110.83 (min 855.07, max 1366.59)","1121.45 (min 967.59, max 1275.31)"
    "bw_mem-rd-8mb (MB/s)","1120.03 (min 890.08, max 1349.98)","1059.94 (min 899.99, max 1219.88)"
    "bw_mem-rdwr-16mb (MB/s)","874.17","851.47"
    "bw_mem-rdwr-1mb (MB/s)","682.15 (min 529.57, max 834.72)","1660.58 (min 775.34, max 2545.82)"
    "bw_mem-rdwr-2mb (MB/s)","692.92 (min 578.95, max 806.89)","939.64 (min 616.05, max 1263.22)"
    "bw_mem-rdwr-4mb (MB/s)","697.85 (min 556.95, max 838.75)","758.85 (min 587.46, max 930.23)"
    "bw_mem-rdwr-8mb (MB/s)","714.84 (min 576.70, max 852.97)","729.61 (min 593.60, max 865.61)"
    "bw_mem-wr-16mb (MB/s)","891.91","892.16"
    "bw_mem-wr-1mb (MB/s)","844.64 (min 834.72, max 854.55)","2889.29 (min 2545.82, max 3232.76)"
    "bw_mem-wr-2mb (MB/s)","827.42 (min 806.89, max 847.94)","1296.06 (min 1263.22, max 1328.90)"
    "bw_mem-wr-4mb (MB/s)","846.91 (min 838.75, max 855.07)","948.91 (min 930.23, max 967.59)"
    "bw_mem-wr-8mb (MB/s)","871.53 (min 852.97, max 890.08)","882.80 (min 865.61, max 899.99)"
    "bw_mmap_rd-mo-1mb (MB/s)","1301.60","2721.62"
    "bw_mmap_rd-o2c-1mb (MB/s)","503.61","696.99"
    "bw_pipe (MB/s)","528.22","477.71"
    "bw_unix (MB/s)","578.92","986.93"
    "lat_connect (us)","77.65","91.85"
    "lat_ctx-2-128k (us)","6.01","12.01"
    "lat_ctx-2-256k (us)","15.74","9.65"
    "lat_ctx-4-128k (us)","7.02","7.85"
    "lat_ctx-4-256k (us)","10.76","3.97"
    "lat_fs-0k (num_files)","231.00","204.00"
    "lat_fs-10k (num_files)","91.00","90.00"
    "lat_fs-1k (num_files)","138.00","135.00"
    "lat_fs-4k (num_files)","138.00","134.00"
    "lat_mem_rd-stride128-sz1000k (ns)","48.10","23.73"
    "lat_mem_rd-stride128-sz125k (ns)","7.84","9.79"
    "lat_mem_rd-stride128-sz250k (ns)","10.53","10.28"
    "lat_mem_rd-stride128-sz31k (ns)","3.06","6.43"
    "lat_mem_rd-stride128-sz50 (ns)","3.01","3.77"
    "lat_mem_rd-stride128-sz500k (ns)","44.07","11.38"
    "lat_mem_rd-stride128-sz62k (ns)","7.37","9.25"
    "lat_mmap-1m (us)","75.00","80.00"
    "lat_ops-double-add (ns)","4.02","5.03"
    "lat_ops-double-div (ns)","22.11","27.79"
    "lat_ops-double-mul (ns)","4.02","5.03"
    "lat_ops-float-add (ns)","4.02","5.04"
    "lat_ops-float-div (ns)","13.06","16.37"
    "lat_ops-float-mul (ns)","4.02","5.05"
    "lat_ops-int-add (ns)","1.01","1.26"
    "lat_ops-int-bit (ns)","0.67","0.84"
    "lat_ops-int-div (ns)","6.03","7.57"
    "lat_ops-int-mod (ns)","6.37","7.97"
    "lat_ops-int-mul (ns)","4.33","5.42"
    "lat_ops-int64-add (ns)","1.01","1.26"
    "lat_ops-int64-bit (ns)","0.67","0.84"
    "lat_ops-int64-div (ns)","9.55","11.96"
    "lat_ops-int64-mod (ns)","7.37","9.23"
    "lat_ops-int64-mul (ns)","4.99","6.25"
    "lat_pagefault (us)","1.46","1.30"
    "lat_pipe (us)","21.32","35.18"
    "lat_proc-exec (us)","1189.20","909.67"
    "lat_proc-fork (us)","963.00","790.14"
    "lat_proc-proccall (us)","0.01","0.02"
    "lat_select (us)","43.00","54.96"
    "lat_sem (us)","2.74","5.89"
    "lat_sig-catch (us)","5.89","7.38"
    "lat_sig-install (us)","0.90","1.14"
    "lat_sig-prot (us)","0.67","0.84"
    "lat_syscall-fstat (us)","4.36","5.47"
    "lat_syscall-null (us)","0.58","0.71"
    "lat_syscall-open (us)","286.84","276.20"
    "lat_syscall-read (us)","0.97","1.21"
    "lat_syscall-stat (us)","5.62","6.96"
    "lat_syscall-write (us)","0.80","1.00"
    "lat_tcp (us)","1.13","1.41"
    "lat_unix (us)","34.49","68.44"
    "latency_for_0.50_mb_block_size (nanosec)","44.07","11.38"
    "latency_for_1.00_mb_block_size (nanosec)","24.05 (min 0.00, max 48.10)","11.87 (min 0.00, max 23.73)"
    "pipe_bandwidth (MBs)","528.22","477.71"
    "pipe_latency (microsec)","21.32","35.18"
    "procedure_call (microsec)","0.01","0.02"
    "select_on_200_tcp_fds (microsec)","43.00","54.96"
    "semaphore_latency (microsec)","2.74","5.89"
    "signal_handler_latency (microsec)","0.90","1.14"
    "signal_handler_overhead (microsec)","5.89","7.38"
    "tcp_ip_connection_cost_to_localhost (microsec)","77.65","91.85"
    "tcp_latency_using_localhost (microsec)","1.13","1.41"


Table:  **LM Bench Metrics**



Dhrystone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed. For standard ARM
cores the DMIPS/MHz score will be identical with the same compiler and flags.

.. csv-table::
    :header: "Benchmarks","am64xx-hsevm: perf"

    "cpu_clock (MHz)","1000.00"
    "dhrystone_per_mhz (DMIPS/MHz)","2.90"
    "dhrystone_per_second (DhrystoneP)","5128205.00"


Table:  **Dhrystone Benchmark**



Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Benchmarks","am64xx-hsevm: perf","am654x-evm: perf"

    "whetstone (MIPS)","5000.00","3333.30"


Table:  **Whetstone Benchmark**



Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table::
    :header: "Benchmarks","am64xx-hsevm: perf","am654x-evm: perf"

    "linpack (Kflops)","410097.00","326394.00"


Table:  **Linpack Benchmark**



NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks 
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html


.. csv-table::
    :header: "Benchmarks","am654x-evm: perf"

    "assignment (Iterations)","7.89"
    "fourier (Iterations)","12853.00"
    "fp_emulation (Iterations)","52.43"
    "huffman (Iterations)","663.45"
    "idea (Iterations)","1956.50"
    "lu_decomposition (Iterations)","302.85"
    "neural_net (Iterations)","5.01"
    "numeric_sort (Iterations)","339.11"
    "string_sort (Iterations)","93.56"


Table:  **NBench Benchmarks**



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

.. csv-table::
    :header: "Benchmarks","am654x-evm: perf"

    "add (MB/s)","1589.60"
    "copy (MB/s)","1838.30"
    "scale (MB/s)","1811.70"
    "triad (MB/s)","1495.20"


Table:  **Stream**



CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark\ |reg|\ -Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark\ |reg| benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table::
    :header: "Benchmarks","am64xx-hsevm: perf"

    "cjpeg-rose7-preset (workloads/)","29.85"
    "core (workloads/)","0.21"
    "coremark-pro ()","587.59"
    "linear_alg-mid-100x100-sp (workloads/)","10.43"
    "loops-all-mid-10k-sp (workloads/)","0.49"
    "nnet_test (workloads/)","0.77"
    "parser-125k (workloads/)","5.56"
    "radix2-big-64k (workloads/)","19.28"
    "sha-test (workloads/)","58.14"
    "zip-test (workloads/)","15.38"


Table:  **CoreMarkPro**


 
 


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

.. csv-table::
    :header: "Benchmarks","am654x-evm: perf"

    "4m-check (workloads/)","314.43"
    "4m-check-reassembly (workloads/)","79.05"
    "4m-check-reassembly-tcp (workloads/)","37.04"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","11.18"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.13"
    "4m-cmykw2 (workloads/)","139.28"
    "4m-cmykw2-rotatew2 (workloads/)","34.27"
    "4m-reassembly (workloads/)","58.04"
    "4m-rotatew2 (workloads/)","13.29"
    "4m-tcp-mixed (workloads/)","70.80"
    "4m-x264w2 (workloads/)","1.16"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","10.97"
    "idct-4mw1 (workloads/)","10.98"
    "ippktcheck-4m (workloads/)","314.74"
    "ippktcheck-4mw1 (workloads/)","315.30"
    "ipres-4m (workloads/)","67.78"
    "ipres-4mw1 (workloads/)","67.72"
    "md5-4m (workloads/)","17.05"
    "md5-4mw1 (workloads/)","17.00"
    "rgbcmyk-4m (workloads/)","36.43"
    "rgbcmyk-4mw1 (workloads/)","36.40"
    "rotate-4ms1 (workloads/)","14.25"
    "rotate-4ms1w1 (workloads/)","14.25"
    "rotate-4ms64 (workloads/)","14.39"
    "rotate-4ms64w1 (workloads/)","14.38"
    "x264-4mq (workloads/)","0.33"
    "x264-4mqw1 (workloads/)","0.33"


Table:  **Multibench**
 

Stress-ng and Cyclic Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^

stress-ng (next-generation) will stress test a embedded platform in various selectable ways.
It was designed to exercise various physical subsystems as well as the various
operating system kernel interfaces. stress-ng can also measure test throughput rates;
this can be useful to observe performance changes across different operating system or types of hardware.

Cyclictest is most commonly used for benchmarking RT systems.
It is one of the most frequently used tools for evaluating the relative performance of real-time systems.
Some performance tests which use Cyclictest are System benchmarking, Latency debugging with tracing and
approximating application performance.

Test command for running stress-ng and cyclictest together

``stress-ng --cpu-method=all -c 4 &``

``cyclictest -m -Sp98 -D6h -h400 -i200 -q``

.. csv-table::
    :header: "Latencies","am62xx_sk:per-core","am62pxx_sk-fs:per-core", "am64xx-hsevm:per-core", "am62axx_sk-fs:per-core"

    "Minimum (usec)","4,4,4,4","4,4,4,4","5,5","4,4,4,4"
    "Average (usec)","5,5,5,5","5,5,5,6","7,7","5,5,5,5"
    "Maximum (usec)","55,62,71,61","41,45,43,44","72,48","29,24,35,35"
 

Table:  **Stress-ng and Cyclic Test**



Boot-time Measurement
-------------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Boot Configuration","am654x-evm: boot time (sec)"

    "Kernel boot time test when bootloader, kernel and sdk-rootfs are in mmc-sd","20.50 (min 17.91, max 24.61)"
    "Kernel boot time test when init is /bin/sh and bootloader, kernel and sdk-rootfs are in mmc-sd","4.45 (min 4.42, max 4.47)"

Table:  **Boot time MMC/SD**

 

 


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

|


CPSW/CPSW2g/CPSW3g Ethernet Driver 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- CPSW2g: AM65x
- CPSW3g: AM64x


.. rubric::  TCP Bidirectional Throughput 
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table::
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1148.97","73.07"

Table: **CPSW TCP Bidirectional Throughput**

|



.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table::
    :header: "Command Used","am654x-evm: THROUGHPUT (Mbits/sec)","am654x-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1463.47","34.26"

Table: **CPSW TCP Bidirectional Throughput Interrupt Pacing**

|



.. rubric::  UDP Throughput 
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table::
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)","am654x-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am654x-evm: THROUGHPUT (Mbits/sec)","am654x-evm: Packets Per Second (kPPS)","am654x-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","12.62","88.00","89.72","18.00","10.34","72.00","45.70"
    "128","82.00","53.57","82.00","86.97","82.00","48.91","75.00","44.85"
    "256","210.00","130.25","78.00","89.70","210.00","120.14","72.00","45.76"
    "1024","978.00","108.73","14.00","18.98","978.00","517.07","66.00","46.38"
    "1518","1472.00","944.16","80.00","93.31","1472.00","625.72","53.00","37.07"

Table: **CPSW UDP Egress Throughput**

|



.. csv-table::
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)","am654x-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am654x-evm: THROUGHPUT (Mbits/sec)","am654x-evm: Packets Per Second (kPPS)","am654x-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","1.22","8.00","7.88","18.00","1.86","13.00","4.86"
    "128","82.00","5.58","9.00","8.38","82.00","9.58","15.00","4.84"
    "256","210.00","13.78","8.00","0.98","210.00","56.45","34.00","16.67"
    "1024","978.00","75.89","10.00","8.46"
    "1518","1472.00","115.40","10.00","8.97","1472.00","428.63","36.00","18.22"

Table: **CPSW UDP Ingress Throughput (0% loss)**

|



.. csv-table::
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)","am64xx-hsevm: Packet Loss %","am654x-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am654x-evm: THROUGHPUT (Mbits/sec)","am654x-evm: Packets Per Second (kPPS)","am654x-evm: CPU Load % (LOCAL_CPU_UTIL)","am654x-evm: Packet Loss %"

    "64","18.00","19.67","137.00","76.58","77.46","18.00","14.93","104.00","42.30","73.92"
    "128","82.00","88.72","135.00","79.04","75.23","82.00","68.49","104.00","42.84","74.73"
    "256","210.00","222.84","133.00","82.94","70.27","210.00","176.52","105.00","43.39","72.63"
    "1024","978.00","889.55","114.00","87.28","5.04"
    "1518","1472.00","902.13","77.00","81.60","4.88","1472.00","924.97","79.00","40.51","1.74"

Table: **CPSW UDP Ingress Throughput (possible loss)**

|
 
 


ICSSG Ethernet Driver 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric::  TCP Bidirectional Throughput 
   :name: tcp-bidirectional-throughput

.. csv-table::
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)","am654x-evm: THROUGHPUT (Mbits/sec)","am654x-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_MAERTS","235.83","77.11","1094.15","50.29"

Table: **ICSSG TCP Bidirectional Throughput**

|



.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: ICSSG-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table::
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_MAERTS","240.18","58.85"

Table: **ICSSG TCP Bidirectional Throughput Interrupt Pacing**

|





.. csv-table::
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load %","am654x-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am654x-evm: THROUGHPUT (Mbits/sec)","am654x-evm: Packets Per Second (kPPS)","am654x-evm: CPU Load %"

    "64","18.00","1.93","13.00","22.35"
    "128","82.00","13.71","21.00","22.53"
    "256","210.00","40.49","24.00","13.07"
    "1518","1472.00","314.02","27.00","63.21"

Table: **ICSSG UDP Ingress Throughput (0% loss)**

|
 
 
 


PCIe Driver
-------------------------

PCIe-ETH
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "TCP Window Size(Kbytes)","am64xx-hsevm: Bandwidth (Mbits/sec)"

    "8","197.60"
    "16","193.60"
    "32","339.20"
    "64","519.20"
    "128","688.80"
    "256","792.80"

Table: **PCI Ethernet**


 
 

 




EMMC Driver
-------------------------

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

|

 
 

 


AM64XX-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^
|

.. csv-table::
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "1m","60.90","3.32","175.00","5.85"
    "4m","61.10","2.51","175.00","4.71"
    "4k","48.50","51.42","55.50","52.60"
    "256k","60.80","5.05","174.00","7.20"

|



 

 


MMC/SD Driver
-------------------------

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

| 

 

 


AM64XX-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^
|

.. csv-table::
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "1m","18.10","1.39","86.50","3.71"
    "4m","17.60","1.07","86.40","2.72"
    "4k","4.51","9.00","16.20","18.19"
    "256k","17.20","1.99","84.00","4.77"

|


 

 

 

 

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|
 

  


CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. csv-table::
    :header: "Algorithm","Buffer Size (in bytes)","am64xx-hsevm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","22739.29"
    "aes-128-cbc","16","378.75"
    "aes-128-cbc","16384","143851.52"
    "aes-128-cbc","256","6019.33"
    "aes-128-cbc","64","1508.22"
    "aes-128-cbc","8192","104630.95"
    "aes-128-ecb","1024","24544.60"
    "aes-128-ecb","16","398.81"
    "aes-128-ecb","16384","147860.14"
    "aes-128-ecb","256","6688.51"
    "aes-128-ecb","64","1671.17"
    "aes-128-ecb","8192","107479.04"
    "aes-192-cbc","1024","23729.15"
    "aes-192-cbc","16","409.47"
    "aes-192-cbc","16384","134272.34"
    "aes-192-cbc","256","6536.36"
    "aes-192-cbc","64","1659.58"
    "aes-192-cbc","8192","100264.62"
    "aes-192-ecb","1024","23268.69"
    "aes-192-ecb","16","416.16"
    "aes-192-ecb","16384","138996.39"
    "aes-192-ecb","256","6693.55"
    "aes-192-ecb","64","1668.74"
    "aes-192-ecb","8192","103675.22"
    "aes-256-cbc","1024","21606.40"
    "aes-256-cbc","16","406.22"
    "aes-256-cbc","16384","126844.93"
    "aes-256-cbc","256","6054.23"
    "aes-256-cbc","64","1509.59"
    "aes-256-cbc","8192","96400.73"
    "aes-256-ecb","1024","24218.28"
    "aes-256-ecb","16","419.88"
    "aes-256-ecb","16384","130389.33"
    "aes-256-ecb","256","6658.39"
    "aes-256-ecb","64","1684.99"
    "aes-256-ecb","8192","98375.00"
    "sha256","1024","24721.07"
    "sha256","16","412.99"
    "sha256","16384","197940.57"
    "sha256","256","6479.53"
    "sha256","64","1634.05"
    "sha256","8192","133772.63"
    "sha512","1024","17315.84"
    "sha512","16","401.58"
    "sha512","16384","46945.62"
    "sha512","256","5716.57"
    "sha512","64","1604.86"
    "sha512","8192","42052.27"


|
|



.. csv-table::
    :header: "Algorithm","am64xx-hsevm: CPU Load"

    "aes-128-cbc","44.00"
    "aes-128-ecb","46.00"
    "aes-192-cbc","45.00"
    "aes-192-ecb","45.00"
    "aes-256-cbc","43.00"
    "aes-256-ecb","45.00"
    "sha256","97.00"
    "sha512","97.00"

 

|
| Listed for each algorithm are the code snippets used to run each
  benchmark test.

|





IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Algorithm","am64xx-hsevm: Throughput (Mbps)","am64xx-hsevm: Packets/Sec","am64xx-hsevm: CPU Load","am654x-evm: Throughput (Mbps)","am654x-evm: Packets/Sec","am654x-evm: CPU Load"

    "3des","53.00","4.00","51.59"
    "aes128","0.70","0.00","56.73"
    "aes256","3.00","0.00","42.79"

 


