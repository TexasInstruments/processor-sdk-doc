
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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","25.35"
    "af_unix_socket_stream_bandwidth (MBs)","1257.15"
    "bw_file_rd-io-1mb (MB/s)","1340.26"
    "bw_file_rd-o2c-1mb (MB/s)","792.08"
    "bw_mem-bcopy-16mb (MB/s)","1972.39"
    "bw_mem-bcopy-1mb (MB/s)","2141.74"
    "bw_mem-bcopy-2mb (MB/s)","1789.55"
    "bw_mem-bcopy-4mb (MB/s)","1689.43"
    "bw_mem-bcopy-8mb (MB/s)","1703.76"
    "bw_mem-bzero-16mb (MB/s)","8109.48"
    "bw_mem-bzero-1mb (MB/s)","5128.58 (min 2141.74, max 8115.42)"
    "bw_mem-bzero-2mb (MB/s)","4951.93 (min 1789.55, max 8114.31)"
    "bw_mem-bzero-4mb (MB/s)","4900.83 (min 1689.43, max 8112.22)"
    "bw_mem-bzero-8mb (MB/s)","4906.62 (min 1703.76, max 8109.48)"
    "bw_mem-cp-16mb (MB/s)","980.63"
    "bw_mem-cp-1mb (MB/s)","4667.98 (min 963.86, max 8372.09)"
    "bw_mem-cp-2mb (MB/s)","4618.37 (min 976.72, max 8260.01)"
    "bw_mem-cp-4mb (MB/s)","4589.77 (min 1007.94, max 8171.60)"
    "bw_mem-cp-8mb (MB/s)","4585.55 (min 1027.22, max 8143.88)"
    "bw_mem-fcp-16mb (MB/s)","1841.20"
    "bw_mem-fcp-1mb (MB/s)","4979.88 (min 1844.34, max 8115.42)"
    "bw_mem-fcp-2mb (MB/s)","4932.81 (min 1751.31, max 8114.31)"
    "bw_mem-fcp-4mb (MB/s)","4950.97 (min 1789.71, max 8112.22)"
    "bw_mem-fcp-8mb (MB/s)","4967.46 (min 1825.44, max 8109.48)"
    "bw_mem-frd-16mb (MB/s)","2015.37"
    "bw_mem-frd-1mb (MB/s)","1949.44 (min 1844.34, max 2054.54)"
    "bw_mem-frd-2mb (MB/s)","1801.58 (min 1751.31, max 1851.85)"
    "bw_mem-frd-4mb (MB/s)","1887.41 (min 1789.71, max 1985.11)"
    "bw_mem-frd-8mb (MB/s)","1909.11 (min 1825.44, max 1992.78)"
    "bw_mem-fwr-16mb (MB/s)","8127.33"
    "bw_mem-fwr-1mb (MB/s)","5213.32 (min 2054.54, max 8372.09)"
    "bw_mem-fwr-2mb (MB/s)","5055.93 (min 1851.85, max 8260.01)"
    "bw_mem-fwr-4mb (MB/s)","5078.36 (min 1985.11, max 8171.60)"
    "bw_mem-fwr-8mb (MB/s)","5068.33 (min 1992.78, max 8143.88)"
    "bw_mem-rd-16mb (MB/s)","2065.32"
    "bw_mem-rd-1mb (MB/s)","2133.24 (min 1956.60, max 2309.88)"
    "bw_mem-rd-2mb (MB/s)","1910.09 (min 1769.60, max 2050.58)"
    "bw_mem-rd-4mb (MB/s)","1968.89 (min 1872.37, max 2065.40)"
    "bw_mem-rd-8mb (MB/s)","1992.38 (min 1915.71, max 2069.05)"
    "bw_mem-rdwr-16mb (MB/s)","1992.78"
    "bw_mem-rdwr-1mb (MB/s)","1423.73 (min 963.86, max 1883.59)"
    "bw_mem-rdwr-2mb (MB/s)","1354.61 (min 976.72, max 1732.50)"
    "bw_mem-rdwr-4mb (MB/s)","1438.84 (min 1007.94, max 1869.74)"
    "bw_mem-rdwr-8mb (MB/s)","1480.03 (min 1027.22, max 1932.83)"
    "bw_mem-wr-16mb (MB/s)","1968.75"
    "bw_mem-wr-1mb (MB/s)","1920.10 (min 1883.59, max 1956.60)"
    "bw_mem-wr-2mb (MB/s)","1751.05 (min 1732.50, max 1769.60)"
    "bw_mem-wr-4mb (MB/s)","1871.06 (min 1869.74, max 1872.37)"
    "bw_mem-wr-8mb (MB/s)","1924.27 (min 1915.71, max 1932.83)"
    "bw_mmap_rd-mo-1mb (MB/s)","2253.81"
    "bw_mmap_rd-o2c-1mb (MB/s)","736.11"
    "bw_pipe (MB/s)","813.43"
    "bw_unix (MB/s)","1257.15"
    "lat_connect (us)","50.07"
    "lat_ctx-2-128k (us)","6.47"
    "lat_ctx-2-256k (us)","5.52"
    "lat_ctx-4-128k (us)","5.96"
    "lat_ctx-4-256k (us)","2.79"
    "lat_fs-0k (num_files)","313.00"
    "lat_fs-10k (num_files)","139.00"
    "lat_fs-1k (num_files)","202.00"
    "lat_fs-4k (num_files)","194.00"
    "lat_mem_rd-stride128-sz1000k (ns)","29.33"
    "lat_mem_rd-stride128-sz125k (ns)","5.57"
    "lat_mem_rd-stride128-sz250k (ns)","5.84"
    "lat_mem_rd-stride128-sz31k (ns)","4.19"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","11.26"
    "lat_mem_rd-stride128-sz62k (ns)","5.23"
    "lat_mmap-1m (us)","53.00"
    "lat_ops-double-add (ns)","2.86"
    "lat_ops-double-div (ns)","15.73"
    "lat_ops-double-mul (ns)","2.86"
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
    "lat_pagefault (us)","1.25"
    "lat_pipe (us)","21.96"
    "lat_proc-exec (us)","764.14"
    "lat_proc-fork (us)","593.33"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","35.81"
    "lat_sem (us)","1.80"
    "lat_sig-catch (us)","5.29"
    "lat_sig-install (us)","0.65"
    "lat_sig-prot (us)","0.98"
    "lat_syscall-fstat (us)","1.64"
    "lat_syscall-null (us)","0.46"
    "lat_syscall-open (us)","145.68"
    "lat_syscall-read (us)","0.77"
    "lat_syscall-stat (us)","4.16"
    "lat_syscall-write (us)","0.68"
    "lat_tcp (us)","0.94"
    "lat_unix (us)","25.35"
    "latency_for_0.50_mb_block_size (nanosec)","11.26"
    "latency_for_1.00_mb_block_size (nanosec)","14.66 (min 0.00, max 29.33)"
    "pipe_bandwidth (MBs)","813.43"
    "pipe_latency (microsec)","21.96"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","35.81"
    "semaphore_latency (microsec)","1.80"
    "signal_handler_latency (microsec)","0.65"
    "signal_handler_overhead (microsec)","5.29"
    "tcp_ip_connection_cost_to_localhost (microsec)","50.07"
    "tcp_latency_using_localhost (microsec)","0.94"




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

    "cpu_clock (MHz)","1400.00"
    "dhrystone_per_mhz (DMIPS/MHz)","2.90"
    "dhrystone_per_second (DhrystoneP)","7142857.00"




Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "whetstone (MIPS)","5000.00"




Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "linpack (Kflops)","577128.00"




NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "assignment (Iterations)","14.47"
    "fourier (Iterations)","22833.00"
    "fp_emulation (Iterations)","215.65"
    "huffman (Iterations)","1183.60"
    "idea (Iterations)","3444.70"
    "lu_decomposition (Iterations)","526.69"
    "neural_net (Iterations)","8.66"
    "numeric_sort (Iterations)","616.00"
    "string_sort (Iterations)","163.93"




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

    "add (MB/s)","2891.10"
    "copy (MB/s)","4048.10"
    "scale (MB/s)","3716.50"
    "triad (MB/s)","2541.40"




CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","42.02"
    "core (workloads/)","0.30"
    "coremark-pro ()","944.14"
    "linear_alg-mid-100x100-sp (workloads/)","14.68"
    "loops-all-mid-10k-sp (workloads/)","0.72"
    "nnet_test (workloads/)","1.09"
    "parser-125k (workloads/)","8.93"
    "radix2-big-64k (workloads/)","71.46"
    "sha-test (workloads/)","81.97"
    "zip-test (workloads/)","22.22"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","83.33"
    "core (workloads/)","0.60"
    "coremark-pro ()","1691.80"
    "linear_alg-mid-100x100-sp (workloads/)","29.34"
    "loops-all-mid-10k-sp (workloads/)","1.32"
    "nnet_test (workloads/)","2.17"
    "parser-125k (workloads/)","14.71"
    "radix2-big-64k (workloads/)","72.98"
    "sha-test (workloads/)","163.93"
    "zip-test (workloads/)","43.48"

 
 


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

    "4m-check (workloads/)","436.61"
    "4m-check-reassembly (workloads/)","127.55"
    "4m-check-reassembly-tcp (workloads/)","61.12"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","33.80"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.93"
    "4m-cmykw2 (workloads/)","243.61"
    "4m-cmykw2-rotatew2 (workloads/)","51.37"
    "4m-reassembly (workloads/)","86.88"
    "4m-rotatew2 (workloads/)","53.97"
    "4m-tcp-mixed (workloads/)","118.52"
    "4m-x264w2 (workloads/)","1.95"
    "idct-4m (workloads/)","19.30"
    "idct-4mw1 (workloads/)","19.30"
    "ippktcheck-4m (workloads/)","435.46"
    "ippktcheck-4mw1 (workloads/)","436.45"
    "ipres-4m (workloads/)","116.28"
    "ipres-4mw1 (workloads/)","116.55"
    "md5-4m (workloads/)","29.34"
    "md5-4mw1 (workloads/)","29.42"
    "rgbcmyk-4m (workloads/)","62.93"
    "rgbcmyk-4mw1 (workloads/)","62.81"
    "rotate-4ms1 (workloads/)","24.17"
    "rotate-4ms1w1 (workloads/)","24.08"
    "rotate-4ms64 (workloads/)","24.47"
    "rotate-4ms64w1 (workloads/)","24.41"
    "x264-4mq (workloads/)","0.58"
    "x264-4mqw1 (workloads/)","0.58"



 
 



|

Boot-time Measurement
-------------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Boot time MMCSD
    :header: "Boot Configuration","am62pxx_sk-fs: boot time (sec)"

    "Kernel boot time test when bootloader, kernel and sdk-rootfs are in mmc-sd","14.46 (min 14.10, max 14.85)"
    "Kernel boot time test when init is /bin/sh and bootloader, kernel and sdk-rootfs are in mmc-sd","4.43 (min 4.38, max 4.48)"
    "kernel boot time test when bootloader, kernel and sdk-rootfs are in mmc-sd","16.23 (min 16.08, max 16.43)"



 
 



|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62pxx_sk-fs: Throughput (bits/sec)","am62pxx_sk-fs: CPU Load (%)"

    "8000","255997.00","0.09"
    "11025","352797.00","0.14"
    "16000","511997.00","0.09"
    "22050","705595.00","0.25"
    "24000","705593.00","0.23"
    "32000","1023988.00","0.51"
    "44100","1411184.00","0.41"
    "48000","1535984.00","0.84"
    "88200","2822368.00","0.74"
    "96000","3071965.00","1.72"



 
 



 



|

Graphics SGX/RGX Driver
-------------------------
 


GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62pxx_sk-fs: Score","am62pxx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","918.13","14.81"
    " GFXBench 3.x gl_trex_off","1590.73","28.41"
    " GFXBench 4.x gl_4_off","263.52","4.46"
    " GFXBench 5.x gl_5_high_off","113.87","1.77"




Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62pxx_sk-fs: Score"

    "Glmark2-DRM","309.00"
    "Glmark2-Wayland","794.00"

 
 

 

 



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

- CPSW3g: AM62px


.. rubric::  TCP Bidirectional Throughput 
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1772.82","58.57"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1854.00","37.39"







 
 

 

 
 

 

 



|

Linux OSPI Flash Driver
-------------------------

 

 


AM62PXX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Write UBIFS CPU Load (%)","am62pxx_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.28)","14.12 (min 13.22, max 14.70)","28.63","6.67"
    "262144","0.16 (min 0.11, max 0.19)","13.98 (min 13.38, max 14.41)","28.56","12.50"
    "524288","0.15 (min 0.11, max 0.19)","12.19 (min 11.31, max 13.62)","28.33","3.45"
    "1048576","0.16 (min 0.11, max 0.19)","13.34 (min 11.79, max 14.39)","28.14","10.00"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62pxx_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","37.59"

 
 

 

 

 

 


 

 

 

 

 

 
 

 

 

 

 

 



|

EMMC Driver
-------------------------

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

 

 

 

 

 


 

 




AM62PXX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","90.20","1.46","285.00","2.24"
    "4m","96.40","1.03","287.00","2.10"
    "4k","78.90","23.50","91.20","19.73"
    "256k","90.30","1.77","288.00","3.76"



 
 

 











 
 



|

UBoot EMMC Driver
-------------------------

 




AM62PXX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","97814.93","270809.92"
    "4000000","96518.41","281270.39"


























 
 

 



|

MMC/SD Driver
-------------------------

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

 

 

 

 

 





 

 




AM62PXX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.60","0.96","84.90","0.87"
    "4m","42.30","0.70","85.00","0.87"
    "4k","2.82","1.49","13.60","4.19"
    "256k","37.50","1.08","84.10","1.35"





 

 

 

 

 

 

 

 















 

 

 





 

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option
 



|

UBoot MMC/SD Driver
-------------------------

  




AM62PXX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","37236.36","59362.32"
    "800000","45765.36","72495.58"
    "1000000","48617.21","81108.91"
































 
 



|

USB Driver
-------------------------
 


USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^










.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","37.60"




.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","32.40"





 
 
 



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62pxx_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","25761.79"
    "aes-128-cbc","16","468.65"
    "aes-128-cbc","16384","87577.94"
    "aes-128-cbc","256","7765.33"
    "aes-128-cbc","64","2058.18"
    "aes-128-cbc","8192","74989.57"
    "aes-128-ecb","1024","26237.95"
    "aes-128-ecb","16","475.15"
    "aes-128-ecb","16384","90248.53"
    "aes-128-ecb","256","8015.02"
    "aes-128-ecb","64","2108.48"
    "aes-128-ecb","8192","77111.30"
    "aes-192-cbc","1024","25433.43"
    "aes-192-cbc","16","461.86"
    "aes-192-cbc","16384","78566.74"
    "aes-192-cbc","256","7644.25"
    "aes-192-cbc","64","1945.69"
    "aes-192-cbc","8192","68698.11"
    "aes-192-ecb","1024","25913.34"
    "aes-192-ecb","16","474.18"
    "aes-192-ecb","16384","81264.64"
    "aes-192-ecb","256","7905.45"
    "aes-192-ecb","64","2107.88"
    "aes-192-ecb","8192","70653.27"
    "aes-256-cbc","1024","24602.28"
    "aes-256-cbc","16","467.03"
    "aes-256-cbc","16384","71696.38"
    "aes-256-cbc","256","7622.49"
    "aes-256-cbc","64","2066.65"
    "aes-256-cbc","8192","63457.96"
    "aes-256-ecb","1024","25231.70"
    "aes-256-ecb","16","476.09"
    "aes-256-ecb","16384","74011.99"
    "aes-256-ecb","256","7842.39"
    "aes-256-ecb","64","2098.94"
    "aes-256-ecb","8192","65126.40"
    "sha256","1024","34277.72"
    "sha256","16","573.53"
    "sha256","16384","273716.57"
    "sha256","256","8973.06"
    "sha256","64","2288.19"
    "sha256","8192","185611.61"
    "sha512","1024","24480.09"
    "sha512","16","564.82"
    "sha512","16384","67807.91"
    "sha512","256","8025.94"
    "sha512","64","2264.26"
    "sha512","8192","60511.57"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62pxx_sk-fs: CPU Load"

    "aes-128-cbc","34.00"
    "aes-128-ecb","35.00"
    "aes-192-cbc","33.00"
    "aes-192-ecb","34.00"
    "aes-256-cbc","33.00"
    "aes-256-ecb","34.00"
    "sha256","98.00"
    "sha512","98.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

|

Low Power Performance
-------------------------

Table:  **Deep sleep**

.. csv-table::
    :header: "Rail name","Rail voltage(V)","am62pxx_sk-fs"

    "vdd_core","0.85","10.06"
    "vddr_core","0.85","0.92"
    "soc_dvdd_3v3","3.30","6.63"
    "soc_dvdd_1v8","1.80","2.78"
    "vdda_1v8","1.80","72.19"
    "vdd_lpddr4/vdd_ddr4","1.10","4.40"
    "Total"," ","96.98"

Table:  **MCU only**

.. csv-table::
    :header: "Rail name","Rail voltage(V)","am62pxx_sk-fs"

    "vdd_core","0.85","207.60"
    "vddr_core","0.85","2.46"
    "soc_dvdd_3v3","3.30","6.56"
    "soc_dvdd_1v8","1.80","2.63"
    "vdda_1v8","1.80","80.23"
    "vdd_lpddr4/vdd_ddr4","1.10","4.05"
    "Total"," ","303.53"

Partial I/O Data
- All voltage rails were measured to be near 0V

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)
