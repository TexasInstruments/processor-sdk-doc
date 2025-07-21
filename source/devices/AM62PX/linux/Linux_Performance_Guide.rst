
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

    "af_unix_sock_stream_latency (microsec)","30.16"
    "af_unix_socket_stream_bandwidth (MBs)","1195.29"
    "bw_file_rd-io-1mb (MB/s)","1441.44"
    "bw_file_rd-o2c-1mb (MB/s)","802.95"
    "bw_mem-bcopy-16mb (MB/s)","1962.71"
    "bw_mem-bcopy-1mb (MB/s)","2096.88"
    "bw_mem-bcopy-2mb (MB/s)","1846.15"
    "bw_mem-bcopy-4mb (MB/s)","1671.54"
    "bw_mem-bcopy-8mb (MB/s)","1938.45"
    "bw_mem-bzero-16mb (MB/s)","8114.96"
    "bw_mem-bzero-1mb (MB/s)","5095.88 (min 2096.88, max 8094.88)"
    "bw_mem-bzero-2mb (MB/s)","4970.95 (min 1846.15, max 8095.74)"
    "bw_mem-bzero-4mb (MB/s)","4891.20 (min 1671.54, max 8110.85)"
    "bw_mem-bzero-8mb (MB/s)","5023.97 (min 1938.45, max 8109.48)"
    "bw_mem-cp-16mb (MB/s)","981.17"
    "bw_mem-cp-1mb (MB/s)","4660.98 (min 968.52, max 8353.44)"
    "bw_mem-cp-2mb (MB/s)","4599.50 (min 955.26, max 8243.73)"
    "bw_mem-cp-4mb (MB/s)","4596.81 (min 1006.67, max 8186.94)"
    "bw_mem-cp-8mb (MB/s)","4586.70 (min 1025.38, max 8148.02)"
    "bw_mem-fcp-16mb (MB/s)","1831.08"
    "bw_mem-fcp-1mb (MB/s)","4939.98 (min 1785.08, max 8094.88)"
    "bw_mem-fcp-2mb (MB/s)","4916.98 (min 1738.22, max 8095.74)"
    "bw_mem-fcp-4mb (MB/s)","4926.51 (min 1742.16, max 8110.85)"
    "bw_mem-fcp-8mb (MB/s)","4962.49 (min 1815.50, max 8109.48)"
    "bw_mem-frd-16mb (MB/s)","1847.79"
    "bw_mem-frd-1mb (MB/s)","1909.49 (min 1785.08, max 2033.90)"
    "bw_mem-frd-2mb (MB/s)","1869.31 (min 1738.22, max 2000.40)"
    "bw_mem-frd-4mb (MB/s)","1831.85 (min 1742.16, max 1921.54)"
    "bw_mem-frd-8mb (MB/s)","1872.19 (min 1815.50, max 1928.87)"
    "bw_mem-fwr-16mb (MB/s)","8128.70"
    "bw_mem-fwr-1mb (MB/s)","5193.67 (min 2033.90, max 8353.44)"
    "bw_mem-fwr-2mb (MB/s)","5122.07 (min 2000.40, max 8243.73)"
    "bw_mem-fwr-4mb (MB/s)","5054.24 (min 1921.54, max 8186.94)"
    "bw_mem-fwr-8mb (MB/s)","5038.45 (min 1928.87, max 8148.02)"
    "bw_mem-rd-16mb (MB/s)","2065.05"
    "bw_mem-rd-1mb (MB/s)","2124.95 (min 1916.38, max 2333.51)"
    "bw_mem-rd-2mb (MB/s)","1874.93 (min 1704.16, max 2045.69)"
    "bw_mem-rd-4mb (MB/s)","1944.50 (min 1829.27, max 2059.73)"
    "bw_mem-rd-8mb (MB/s)","2000.01 (min 1930.97, max 2069.05)"
    "bw_mem-rdwr-16mb (MB/s)","1983.88"
    "bw_mem-rdwr-1mb (MB/s)","1404.23 (min 968.52, max 1839.93)"
    "bw_mem-rdwr-2mb (MB/s)","1272.39 (min 955.26, max 1589.51)"
    "bw_mem-rdwr-4mb (MB/s)","1417.41 (min 1006.67, max 1828.15)"
    "bw_mem-rdwr-8mb (MB/s)","1493.08 (min 1025.38, max 1960.78)"
    "bw_mem-wr-16mb (MB/s)","1972.87"
    "bw_mem-wr-1mb (MB/s)","1878.16 (min 1839.93, max 1916.38)"
    "bw_mem-wr-2mb (MB/s)","1646.84 (min 1589.51, max 1704.16)"
    "bw_mem-wr-4mb (MB/s)","1828.71 (min 1828.15, max 1829.27)"
    "bw_mem-wr-8mb (MB/s)","1945.88 (min 1930.97, max 1960.78)"
    "bw_mmap_rd-mo-1mb (MB/s)","2246.03"
    "bw_mmap_rd-o2c-1mb (MB/s)","796.31"
    "bw_pipe (MB/s)","780.02"
    "bw_unix (MB/s)","1195.29"
    "lat_connect (us)","56.93"
    "lat_ctx-2-128k (us)","7.60"
    "lat_ctx-2-256k (us)","7.56"
    "lat_ctx-4-128k (us)","7.18"
    "lat_ctx-4-256k (us)","6.51"
    "lat_fs-0k (num_files)","248.00"
    "lat_fs-10k (num_files)","108.00"
    "lat_fs-1k (num_files)","178.00"
    "lat_fs-4k (num_files)","175.00"
    "lat_mem_rd-stride128-sz1000k (ns)","29.18"
    "lat_mem_rd-stride128-sz125k (ns)","5.62"
    "lat_mem_rd-stride128-sz250k (ns)","5.83"
    "lat_mem_rd-stride128-sz31k (ns)","3.65"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","12.89"
    "lat_mem_rd-stride128-sz62k (ns)","5.22"
    "lat_mmap-1m (us)","56.00"
    "lat_ops-double-add (ns)","2.86"
    "lat_ops-double-div (ns)","15.74"
    "lat_ops-double-mul (ns)","2.86"
    "lat_ops-float-add (ns)","2.86"
    "lat_ops-float-div (ns)","9.30"
    "lat_ops-float-mul (ns)","2.86"
    "lat_ops-int-add (ns)","0.72"
    "lat_ops-int-bit (ns)","0.48"
    "lat_ops-int-div (ns)","4.29"
    "lat_ops-int-mod (ns)","4.53"
    "lat_ops-int-mul (ns)","3.08"
    "lat_ops-int64-add (ns)","0.72"
    "lat_ops-int64-bit (ns)","0.48"
    "lat_ops-int64-div (ns)","6.79"
    "lat_ops-int64-mod (ns)","5.25"
    "lat_ops-int64-mul (ns)","3.55"
    "lat_pagefault (us)","0.50"
    "lat_pipe (us)","24.46"
    "lat_proc-exec (us)","682.50"
    "lat_proc-fork (us)","590.20"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","34.04"
    "lat_sem (us)","3.53"
    "lat_sig-catch (us)","5.30"
    "lat_sig-install (us)","0.65"
    "lat_sig-prot (us)","0.64"
    "lat_syscall-fstat (us)","1.99"
    "lat_syscall-null (us)","0.46"
    "lat_syscall-open (us)","147.43"
    "lat_syscall-read (us)","0.80"
    "lat_syscall-stat (us)","4.85"
    "lat_syscall-write (us)","0.82"
    "lat_tcp (us)","0.93"
    "lat_unix (us)","30.16"
    "latency_for_0.50_mb_block_size (nanosec)","12.89"
    "latency_for_1.00_mb_block_size (nanosec)","14.59 (min 0.00, max 29.18)"
    "pipe_bandwidth (MBs)","780.02"
    "pipe_latency (microsec)","24.46"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","34.04"
    "semaphore_latency (microsec)","3.53"
    "signal_handler_latency (microsec)","0.65"
    "signal_handler_overhead (microsec)","5.30"
    "tcp_ip_connection_cost_to_localhost (microsec)","56.93"
    "tcp_latency_using_localhost (microsec)","0.93"



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

    "cpu_clock (MHz)","1400.00"
    "dhrystone_per_mhz (DMIPS/MHz)","2.90"
    "dhrystone_per_second (DhrystoneP)","7142857.00"



Whetstone
^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "whetstone (MIPS)","10000.00"



Linpack
^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "linpack (Kflops)","329621.00"



NBench
^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "assignment (Iterations)","8.26"
    "fourier (Iterations)","13044.00"
    "fp_emulation (Iterations)","123.21"
    "huffman (Iterations)","676.56"
    "idea (Iterations)","1968.20"
    "lu_decomposition (Iterations)","302.85"
    "neural_net (Iterations)","4.95"
    "numeric_sort (Iterations)","358.59"
    "string_sort (Iterations)","93.66"



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

    "add (MB/s)","2719.00"
    "copy (MB/s)","3791.20"
    "scale (MB/s)","3426.70"
    "triad (MB/s)","2418.50"



CoreMarkPro
^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","41.84"
    "core (workloads/)","0.30"
    "coremark-pro ()","918.00"
    "linear_alg-mid-100x100-sp (workloads/)","14.67"
    "loops-all-mid-10k-sp (workloads/)","0.71"
    "nnet_test (workloads/)","1.09"
    "parser-125k (workloads/)","8.77"
    "radix2-big-64k (workloads/)","59.36"
    "sha-test (workloads/)","81.30"
    "zip-test (workloads/)","21.74"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","84.03"
    "core (workloads/)","0.60"
    "coremark-pro ()","1676.82"
    "linear_alg-mid-100x100-sp (workloads/)","29.36"
    "loops-all-mid-10k-sp (workloads/)","1.30"
    "nnet_test (workloads/)","2.17"
    "parser-125k (workloads/)","14.08"
    "radix2-big-64k (workloads/)","71.98"
    "sha-test (workloads/)","161.29"
    "zip-test (workloads/)","43.48"

 


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

    "4m-check (workloads/)","428.45"
    "4m-check-reassembly (workloads/)","126.90"
    "4m-check-reassembly-tcp (workloads/)","61.12"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","34.48"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.91"
    "4m-cmykw2 (workloads/)","243.90"
    "4m-cmykw2-rotatew2 (workloads/)","51.64"
    "4m-reassembly (workloads/)","87.11"
    "4m-rotatew2 (workloads/)","54.23"
    "4m-tcp-mixed (workloads/)","120.30"
    "4m-x264w2 (workloads/)","1.94"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","19.28"
    "idct-4mw1 (workloads/)","19.29"
    "ippktcheck-4m (workloads/)","431.93"
    "ippktcheck-4mw1 (workloads/)","430.66"
    "ipres-4m (workloads/)","118.02"
    "ipres-4mw1 (workloads/)","117.46"
    "md5-4m (workloads/)","27.98"
    "md5-4mw1 (workloads/)","28.02"
    "rgbcmyk-4m (workloads/)","62.75"
    "rgbcmyk-4mw1 (workloads/)","62.72"
    "rotate-4ms1 (workloads/)","24.08"
    "rotate-4ms1w1 (workloads/)","24.15"
    "rotate-4ms64 (workloads/)","24.35"
    "rotate-4ms64w1 (workloads/)","24.32"
    "x264-4mq (workloads/)","0.58"
    "x264-4mqw1 (workloads/)","0.58"

 


Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62pxx_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","13.63 (min 13.22, max 14.01)"

 

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

    "11025","352798.00","0.10"
    "16000","511998.00","0.09"
    "22050","705597.00","0.13"
    "24000","705597.00","0.13"
    "32000","1023995.00","0.10"
    "44100","1411193.00","0.21"
    "48000","1535992.00","0.16"
    "88200","2822382.00","0.35"
    "96000","3071979.00","0.18"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62pxx_sk-fs: Throughput (bits/sec)","am62pxx_sk-fs: CPU Load (%)"

    "11025","352944.00","0.14"
    "16000","512210.00","0.26"
    "22050","705885.00","0.17"
    "24000","705887.00","0.19"
    "32000","1024418.00","0.16"
    "44100","1411775.00","0.28"
    "48000","1536626.00","0.23"
    "88200","2823541.00","0.46"
    "96000","3073248.00","0.31"


|

Graphics SGX/RGX Driver
-----------------------
 

GFXBench
^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62pxx_sk-fs: Score","am62pxx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","907.99","14.65"
    " GFXBench 3.x gl_trex_off","1595.80","28.50"
    " GFXBench 4.x gl_4_off","260.27","4.40"
    " GFXBench 5.x gl_5_high_off","113.55","1.77"


Glmark2
^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62pxx_sk-fs: Score"

    "Glmark2-DRM","355.00"
    "Glmark2-Wayland","734.00"


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
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1818.42","64.41"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1812.61","29.43"




.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62pxx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: Packets Per Second (kPPS)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","55.07","108.00","39.97"
    "128","82.00","108.69","106.00","39.97"
    "256","210.00","218.80","107.00","39.98"
    "1024","978.00","839.58","102.00","39.48"
    "1518","1472.00","856.67","71.00","37.44"
 



|

Linux OSPI Flash Driver
-----------------------




AM62PXX-SK
^^^^^^^^^^


UBIFS
"""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Write UBIFS CPU Load (%)","am62pxx_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.29)","27.43 (min 24.77, max 30.04)","28.58","12.90"
    "262144","0.15 (min 0.11, max 0.19)","28.31 (min 26.75, max 30.10)","28.55","6.90"
    "524288","0.15 (min 0.11, max 0.19)","28.51 (min 27.57, max 30.32)","28.26","12.90"
    "1048576","0.15 (min 0.11, max 0.19)","28.08 (min 25.48, max 30.41)","28.21","9.68"



RAW
"""

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

    "1m","90.50","1.61","171.00","1.83"
    "4m","95.60","0.99","172.00","1.41"
    "4k","64.30","21.67","93.40","22.26"
    "256k","90.50","2.01","171.00","2.62"




EMMC RAW FIO 1G
^^^^^^^^^^^^^^^



.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "1m","90.10","1.38","174.00","1.76"
    "4m","97.00","1.01","138.00","1.20"
    "4k","64.70","16.10","92.40","20.30"
    "256k","90.20","1.85","173.00","2.45"

 


EMMC EXT4
^^^^^^^^^
 


.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","83.74 (min 81.64, max 85.23)","5.78 (min 4.97, max 7.62)","178.99","8.97"
    "262144","82.29 (min 61.99, max 90.58)","5.84 (min 3.99, max 8.08)","181.07","9.48"
    "524288","79.81 (min 51.54, max 89.29)","5.46 (min 3.20, max 8.02)","181.88","9.52"
    "1048576","73.44 (min 49.22, max 89.90)","5.08 (min 2.94, max 8.17)","181.74","8.66"
    "5242880","74.59 (min 50.87, max 87.83)","5.30 (min 3.27, max 8.33)","181.91","8.30"



EMMC EXT2
^^^^^^^^^



.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT2 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT2 CPU Load (%)","am62pxx_sk-fs: Read EXT2 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT2 CPU Load (%)"

    "102400","36.82 (min 7.02, max 46.19)","4.08 (min 2.94, max 4.65)","140.53","8.00"
    "262144","50.11 (min 20.89, max 59.79)","5.67 (min 2.87, max 11.52)","177.12","14.41"
    "524288","51.44 (min 7.44, max 67.81)","4.78 (min 2.24, max 6.37)","137.86","7.79"
    "1048576","52.32 (min 7.48, max 68.81)","4.22 (min 2.35, max 5.42)","152.16","7.97"
    "5242880","54.76 (min 7.50, max 70.98)","4.21 (min 2.39, max 4.92)","152.90","6.32"


EMMC VFAT
^^^^^^^^^
 


.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Write VFAT CPU Load (%)","am62pxx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Read VFAT CPU Load (%)"

    "102400","35.84 (min 11.13, max 50.42)","4.93 (min 3.85, max 6.36)","173.89","8.40"
    "262144","45.10 (min 11.46, max 58.09)","6.41 (min 4.90, max 7.20)","175.12","14.23"
    "524288","50.40 (min 12.70, max 72.57)","4.73 (min 3.83, max 5.93)","176.19","8.82"
    "1048576","57.99 (min 12.88, max 75.35)","5.09 (min 4.03, max 5.97)","176.20","9.21"
    "5242880","56.58 (min 13.07, max 82.67)","5.09 (min 3.91, max 6.71)","176.26","9.62"

 

UBoot EMMC Driver
-----------------

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","98402.40","172463.16"
    "4000000","96946.75","174762.67"

 



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

    "1m","42.10","1.04","87.20","1.28"
    "4m","42.90","0.79","87.30","0.97"
    "4k","2.78","1.69","12.80","4.25"
    "256k","38.10","1.22","83.70","1.55"


 


MMC RAW FIO 1G
^^^^^^^^^^^^^^




.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "1m","43.10","1.40","88.00","1.87"
    "4m","43.60","1.02","88.00","1.40"
    "4k","2.77","2.21","13.00","6.68"
    "256k","36.80","1.56","84.00","2.38"




MMC EXT4
^^^^^^^^



.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.37 (min 10.30, max 10.63)","0.80 (min 0.69, max 1.12)","10.68","0.76"
    "262144","10.36 (min 10.28, max 10.49)","0.85 (min 0.63, max 1.32)","11.22","0.67"
    "524288","10.40 (min 10.33, max 10.47)","0.83 (min 0.72, max 1.05)","11.50","0.63"
    "1048576","10.45 (min 10.40, max 10.55)","0.86 (min 0.80, max 1.03)","11.05","0.66"
    "5242880","10.65 (min 10.31, max 10.87)","0.83 (min 0.70, max 1.08)","12.03","0.66"



MMC EXT3
^^^^^^^^



.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","40.74 (min 35.43, max 45.16)","3.67 (min 2.97, max 6.09)","80.08","4.23"
    "262144","40.14 (min 35.43, max 41.78)","3.57 (min 2.82, max 5.91)","82.32","5.14"
    "524288","36.55 (min 32.31, max 38.14)","3.16 (min 2.55, max 5.39)","90.35","4.75"
    "1048576","36.11 (min 31.85, max 37.76)","3.26 (min 2.62, max 5.39)","90.20","4.95"
    "5242880","39.66 (min 34.22, max 42.15)","3.30 (min 2.58, max 5.32)","90.47","4.98"

 


MMC EXT2
^^^^^^^^

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","17.47 (min 3.49, max 21.09)","2.33 (min 2.14, max 2.47)","76.97","4.41"
    "262144","31.21 (min 3.88, max 38.66)","3.17 (min 2.06, max 3.75)","81.53","4.50"
    "524288","34.84 (min 3.99, max 42.82)","3.34 (min 2.05, max 4.00)","90.76","4.76"
    "1048576","33.57 (min 4.02, max 41.12)","2.83 (min 2.09, max 3.23)","90.54","4.35"
    "5242880","32.54 (min 4.03, max 39.87)","2.62 (min 2.03, max 2.86)","90.56","4.55"



 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 

UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","38280.37","81920.00"
    "800000","40554.46","87148.94"
    "1000000","42666.67","90021.98"

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 


|

USB Driver
----------
 


USB Device Controller
^^^^^^^^^^^^^^^^^^^^^



.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","44.00"



.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","37.30"



|

CRYPTO Driver
-------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62pxx_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","23455.06"
    "aes-128-cbc","16","421.01"
    "aes-128-cbc","16384","85224.11"
    "aes-128-cbc","256","6907.22"
    "aes-128-cbc","64","1825.54"
    "aes-128-cbc","8192","71923.03"
    "aes-128-ecb","1024","23801.51"
    "aes-128-ecb","16","430.91"
    "aes-128-ecb","16384","87780.01"
    "aes-128-ecb","256","7053.99"
    "aes-128-ecb","64","1870.70"
    "aes-128-ecb","8192","73659.73"
    "aes-192-cbc","1024","22887.42"
    "aes-192-cbc","16","423.09"
    "aes-192-cbc","16384","76808.19"
    "aes-192-cbc","256","6910.29"
    "aes-192-cbc","64","1825.79"
    "aes-192-cbc","8192","65912.83"
    "aes-192-ecb","1024","23310.34"
    "aes-192-ecb","16","429.07"
    "aes-192-ecb","16384","79123.80"
    "aes-192-ecb","256","6940.50"
    "aes-192-ecb","64","1837.50"
    "aes-192-ecb","8192","67548.50"
    "aes-256-cbc","1024","22148.10"
    "aes-256-cbc","16","421.00"
    "aes-256-cbc","16384","69435.39"
    "aes-256-cbc","256","6811.73"
    "aes-256-cbc","64","1828.39"
    "aes-256-cbc","8192","60792.83"
    "aes-256-ecb","1024","22760.45"
    "aes-256-ecb","16","432.77"
    "aes-256-ecb","16384","72286.21"
    "aes-256-ecb","256","6953.05"
    "aes-256-ecb","64","1869.91"
    "aes-256-ecb","8192","62401.19"
    "sha256","1024","34637.82"
    "sha256","16","574.17"
    "sha256","16384","284317.01"
    "sha256","256","8920.66"
    "sha256","64","2263.98"
    "sha256","8192","190515.88"
    "sha512","1024","24553.81"
    "sha512","16","560.17"
    "sha512","16384","67567.62"
    "sha512","256","8053.59"
    "sha512","64","2252.35"
    "sha512","8192","60293.12"



.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62pxx_sk-fs: CPU Load"

    "aes-128-cbc","31.00"
    "aes-128-ecb","32.00"
    "aes-192-cbc","31.00"
    "aes-192-ecb","32.00"
    "aes-256-cbc","30.00"
    "aes-256-ecb","31.00"
    "sha256","96.00"
    "sha512","96.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

 
Low Power Performance
---------------------

Table:  **Deep sleep**

.. csv-table::
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","8.95"
   "vddr_core","0.85","0.84"
   "soc_dvdd_3v3","3.30","7.16"
   "soc_dvdd_1v8","1.80","2.59"
   "vdda_1v8","1.80","68.66"
   "vdd_lpddr4","1.10","0.46"
   "Total"," ","88.66"

Table:  **MCU only**

.. csv-table::
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","211.34"
   "vddr_core","0.85","2.51"
   "soc_dvdd_3v3","3.30","6.81"
   "soc_dvdd_1v8","1.80","2.63"
   "vdda_1v8","1.80","77.43"
   "vdd_lpddr4","1.10","0.42"
   "Total"," ","301.14"

Partial I/O Data
- All voltage rails were measured to be near 0V

.. note::

   The power consumption on the vdda_1v8 rail is not indicitive of the SoC's power consumption due to an oscillator on the rail
   that has significant current consumption.

.. note::

   The measurements shown are from an AM62Px SK rev E1-1. Results may vary based off of the board revision being used.

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)
