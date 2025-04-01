
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
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","29.90"
    "af_unix_socket_stream_bandwidth (MBs)","1187.22"
    "bw_file_rd-io-1mb (MB/s)","1467.89"
    "bw_file_rd-o2c-1mb (MB/s)","724.77"
    "bw_mem-bcopy-16mb (MB/s)","1973.60"
    "bw_mem-bcopy-1mb (MB/s)","2179.08"
    "bw_mem-bcopy-2mb (MB/s)","1655.63"
    "bw_mem-bcopy-4mb (MB/s)","1828.71"
    "bw_mem-bcopy-8mb (MB/s)","1966.09"
    "bw_mem-bzero-16mb (MB/s)","8108.11"
    "bw_mem-bzero-1mb (MB/s)","5143.60 (min 2179.08, max 8108.11)"
    "bw_mem-bzero-2mb (MB/s)","4875.69 (min 1655.63, max 8095.74)"
    "bw_mem-bzero-4mb (MB/s)","4965.67 (min 1828.71, max 8102.63)"
    "bw_mem-bzero-8mb (MB/s)","5036.42 (min 1966.09, max 8106.74)"
    "bw_mem-cp-16mb (MB/s)","989.73"
    "bw_mem-cp-1mb (MB/s)","4676.66 (min 960.92, max 8392.39)"
    "bw_mem-cp-2mb (MB/s)","4599.93 (min 954.65, max 8245.21)"
    "bw_mem-cp-4mb (MB/s)","4589.01 (min 1006.42, max 8171.60)"
    "bw_mem-cp-8mb (MB/s)","4589.65 (min 1032.66, max 8146.64)"
    "bw_mem-fcp-16mb (MB/s)","1835.92"
    "bw_mem-fcp-1mb (MB/s)","4934.80 (min 1761.49, max 8108.11)"
    "bw_mem-fcp-2mb (MB/s)","4899.95 (min 1704.16, max 8095.74)"
    "bw_mem-fcp-4mb (MB/s)","4942.98 (min 1783.33, max 8102.63)"
    "bw_mem-fcp-8mb (MB/s)","4963.91 (min 1821.08, max 8106.74)"
    "bw_mem-frd-16mb (MB/s)","2015.11"
    "bw_mem-frd-1mb (MB/s)","1890.85 (min 1761.49, max 2020.20)"
    "bw_mem-frd-2mb (MB/s)","1766.66 (min 1704.16, max 1829.16)"
    "bw_mem-frd-4mb (MB/s)","1880.62 (min 1783.33, max 1977.91)"
    "bw_mem-frd-8mb (MB/s)","1910.54 (min 1821.08, max 2000.00)"
    "bw_mem-fwr-16mb (MB/s)","8123.20"
    "bw_mem-fwr-1mb (MB/s)","5206.30 (min 2020.20, max 8392.39)"
    "bw_mem-fwr-2mb (MB/s)","5037.19 (min 1829.16, max 8245.21)"
    "bw_mem-fwr-4mb (MB/s)","5074.76 (min 1977.91, max 8171.60)"
    "bw_mem-fwr-8mb (MB/s)","5073.32 (min 2000.00, max 8146.64)"
    "bw_mem-rd-16mb (MB/s)","2074.69"
    "bw_mem-rd-1mb (MB/s)","2086.73 (min 1837.01, max 2336.45)"
    "bw_mem-rd-2mb (MB/s)","1844.74 (min 1649.35, max 2040.12)"
    "bw_mem-rd-4mb (MB/s)","1931.26 (min 1805.60, max 2056.91)"
    "bw_mem-rd-8mb (MB/s)","1950.34 (min 1834.02, max 2066.65)"
    "bw_mem-rdwr-16mb (MB/s)","1982.65"
    "bw_mem-rdwr-1mb (MB/s)","1365.42 (min 960.92, max 1769.91)"
    "bw_mem-rdwr-2mb (MB/s)","1249.89 (min 954.65, max 1545.12)"
    "bw_mem-rdwr-4mb (MB/s)","1447.05 (min 1006.42, max 1887.68)"
    "bw_mem-rdwr-8mb (MB/s)","1478.10 (min 1032.66, max 1923.54)"
    "bw_mem-wr-16mb (MB/s)","1977.51"
    "bw_mem-wr-1mb (MB/s)","1803.46 (min 1769.91, max 1837.01)"
    "bw_mem-wr-2mb (MB/s)","1597.24 (min 1545.12, max 1649.35)"
    "bw_mem-wr-4mb (MB/s)","1846.64 (min 1805.60, max 1887.68)"
    "bw_mem-wr-8mb (MB/s)","1878.78 (min 1834.02, max 1923.54)"
    "bw_mmap_rd-mo-1mb (MB/s)","2253.42"
    "bw_mmap_rd-o2c-1mb (MB/s)","760.31"
    "bw_pipe (MB/s)","793.54"
    "bw_unix (MB/s)","1187.22"
    "lat_connect (us)","56.55"
    "lat_ctx-2-128k (us)","7.66"
    "lat_ctx-2-256k (us)","6.67"
    "lat_ctx-4-128k (us)","7.18"
    "lat_ctx-4-256k (us)","6.67"
    "lat_fs-0k (num_files)","220.00"
    "lat_fs-10k (num_files)","115.00"
    "lat_fs-1k (num_files)","168.00"
    "lat_fs-4k (num_files)","161.00"
    "lat_mem_rd-stride128-sz1000k (ns)","29.37"
    "lat_mem_rd-stride128-sz125k (ns)","5.55"
    "lat_mem_rd-stride128-sz250k (ns)","5.84"
    "lat_mem_rd-stride128-sz31k (ns)","3.65"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","11.25"
    "lat_mem_rd-stride128-sz62k (ns)","5.24"
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
    "lat_ops-int-mul (ns)","3.07"
    "lat_ops-int64-add (ns)","0.72"
    "lat_ops-int64-bit (ns)","0.48"
    "lat_ops-int64-div (ns)","6.80"
    "lat_ops-int64-mod (ns)","5.25"
    "lat_ops-int64-mul (ns)","3.55"
    "lat_pagefault (us)","0.51"
    "lat_pipe (us)","25.28"
    "lat_proc-exec (us)","687.71"
    "lat_proc-fork (us)","577.30"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","33.98"
    "lat_sem (us)","2.72"
    "lat_sig-catch (us)","5.57"
    "lat_sig-install (us)","0.68"
    "lat_sig-prot (us)","0.86"
    "lat_syscall-fstat (us)","1.96"
    "lat_syscall-null (us)","0.46"
    "lat_syscall-open (us)","151.08"
    "lat_syscall-read (us)","0.79"
    "lat_syscall-stat (us)","4.76"
    "lat_syscall-write (us)","0.76"
    "lat_tcp (us)","0.91"
    "lat_unix (us)","29.90"
    "latency_for_0.50_mb_block_size (nanosec)","11.25"
    "latency_for_1.00_mb_block_size (nanosec)","14.68 (min 0.00, max 29.37)"
    "pipe_bandwidth (MBs)","793.54"
    "pipe_latency (microsec)","25.28"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","33.98"
    "semaphore_latency (microsec)","2.72"
    "signal_handler_latency (microsec)","0.68"
    "signal_handler_overhead (microsec)","5.57"
    "tcp_ip_connection_cost_to_localhost (microsec)","56.55"
    "tcp_latency_using_localhost (microsec)","0.91"

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

    "whetstone (MIPS)","10000.00"

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "linpack (Kflops)","577371.00"

NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "assignment (Iterations)","14.49"
    "fourier (Iterations)","22828.00"
    "fp_emulation (Iterations)","215.61"
    "huffman (Iterations)","1184.20"
    "idea (Iterations)","3444.20"
    "lu_decomposition (Iterations)","526.96"
    "neural_net (Iterations)","8.66"
    "numeric_sort (Iterations)","628.16"
    "string_sort (Iterations)","163.90"

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

    "add (MB/s)","2887.70"
    "copy (MB/s)","4034.70"
    "scale (MB/s)","3712.80"
    "triad (MB/s)","2539.20"

CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","23.98"
    "core (workloads/)","0.17"
    "coremark-pro ()","544.04"
    "linear_alg-mid-100x100-sp (workloads/)","8.37"
    "loops-all-mid-10k-sp (workloads/)","0.42"
    "nnet_test (workloads/)","0.62"
    "parser-125k (workloads/)","5.13"
    "radix2-big-64k (workloads/)","43.30"
    "sha-test (workloads/)","46.73"
    "zip-test (workloads/)","12.82"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","84.03"
    "core (workloads/)","0.60"
    "coremark-pro ()","1667.13"
    "linear_alg-mid-100x100-sp (workloads/)","29.34"
    "loops-all-mid-10k-sp (workloads/)","1.30"
    "nnet_test (workloads/)","2.17"
    "parser-125k (workloads/)","13.70"
    "radix2-big-64k (workloads/)","71.80"
    "sha-test (workloads/)","161.29"
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

    "4m-check (workloads/)","431.11"
    "4m-check-reassembly (workloads/)","134.59"
    "4m-check-reassembly-tcp (workloads/)","61.12"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","34.56"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.90"
    "4m-cmykw2 (workloads/)","244.80"
    "4m-cmykw2-rotatew2 (workloads/)","51.64"
    "4m-reassembly (workloads/)","86.81"
    "4m-rotatew2 (workloads/)","53.91"
    "4m-tcp-mixed (workloads/)","120.30"
    "4m-x264w2 (workloads/)","2.00"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","19.26"
    "idct-4mw1 (workloads/)","19.28"
    "ippktcheck-4m (workloads/)","432.45"
    "ippktcheck-4mw1 (workloads/)","432.30"
    "ipres-4m (workloads/)","117.93"
    "ipres-4mw1 (workloads/)","116.91"
    "md5-4m (workloads/)","28.52"
    "md5-4mw1 (workloads/)","28.42"
    "rgbcmyk-4m (workloads/)","62.75"
    "rgbcmyk-4mw1 (workloads/)","62.89"
    "rotate-4ms1 (workloads/)","24.06"
    "rotate-4ms1w1 (workloads/)","24.10"
    "rotate-4ms64 (workloads/)","24.34"
    "rotate-4ms64w1 (workloads/)","24.38"
    "x264-4mq (workloads/)","0.58"
    "x264-4mqw1 (workloads/)","0.58"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62pxx_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","41.19 (min 13.87, max 122.38)"

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

    "8000","255998.00","0.22"
    "11025","352798.00","0.17"
    "16000","511997.00","0.11"
    "22050","705596.00","0.28"
    "24000","705594.00","0.28"
    "32000","1023987.00","0.18"
    "44100","1411184.00","0.46"
    "48000","1535984.00","0.24"
    "88200","2822369.00","0.86"
    "96000","3071967.00","0.40"

|

Graphics SGX/RGX Driver
-------------------------
 
GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62pxx_sk-fs: Score","am62pxx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","912.50","14.72"
    " GFXBench 3.x gl_trex_off","1596.34","28.51"
    " GFXBench 4.x gl_4_off","260.30","4.40"
    " GFXBench 5.x gl_5_high_off","114.48","1.78"

Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62pxx_sk-fs: Score"

    "Glmark2-DRM","309.00"
    "Glmark2-Wayland","782.00"

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

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1580.77","62.51"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1645.43","33.49"

.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62pxx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: Packets Per Second (kPPS)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","15.72","109.00","40.18"
    "128","82.00","69.74","106.00","39.87"
    "256","210.00","178.63","106.00","39.75"
    "1024","978.00","804.42","103.00","39.63"
    "1518","1472.00","956.34","81.00","35.64"

|

Linux OSPI Flash Driver
-------------------------

AM62PXX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Write UBIFS CPU Load (%)","am62pxx_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.28)","28.87 (min 24.74, max 31.69)","28.60","9.68"
    "262144","0.14 (min 0.11, max 0.18)","28.98 (min 25.40, max 31.51)","28.45","6.67"
    "524288","0.14 (min 0.11, max 0.18)","29.47 (min 27.53, max 31.76)","28.47","3.45"
    "1048576","0.14 (min 0.11, max 0.18)","27.99 (min 26.58, max 28.91)","28.00","3.45"

RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62pxx_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","37.88"

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
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","91.50","2.05","172.00","3.03"
    "4m","97.10","1.57","169.00","2.17"
    "4k","64.50","31.80","88.50","30.07"
    "256k","91.30","3.13","171.00","4.34"

EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "1m","91.20","1.35","174.00","1.77"
    "4m","97.60","0.93","171.00","1.27"
    "4k","64.90","15.82","92.70","20.34"
    "256k","91.20","1.63","173.00","2.40"

EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","85.52 (min 79.45, max 87.92)","6.24 (min 5.36, max 8.32)","178.28","9.32"
    "262144","78.27 (min 52.51, max 87.84)","5.68 (min 3.75, max 7.72)","181.22","10.73"
    "524288","74.00 (min 51.70, max 86.90)","5.55 (min 3.33, max 7.84)","181.93","9.52"
    "1048576","73.58 (min 54.96, max 88.20)","5.39 (min 3.79, max 7.49)","181.98","9.17"
    "5242880","74.34 (min 58.42, max 86.76)","5.39 (min 3.82, max 7.92)","181.95","8.33"

EMMC VFAT
^^^^^^^^^

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Write VFAT CPU Load (%)","am62pxx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Read VFAT CPU Load (%)"

    "102400","36.69 (min 11.54, max 45.34)","4.74 (min 3.72, max 5.55)","137.56","7.82"
    "262144","43.58 (min 10.99, max 61.71)","4.96 (min 4.07, max 6.86)","176.50","10.08"
    "524288","50.97 (min 12.62, max 65.36)","5.65 (min 4.45, max 6.49)","167.18","8.84"
    "1048576","46.55 (min 12.36, max 66.45)","4.51 (min 3.14, max 5.96)","166.91","8.76"
    "5242880","48.35 (min 12.52, max 69.13)","4.40 (min 3.32, max 5.51)","167.83","8.80"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","97234.42","143719.30"
    "4000000","98550.38","174762.67"

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
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.40","0.95","87.40","1.26"
    "4m","42.00","0.62","87.40","0.87"
    "4k","2.80","1.59","12.90","4.33"
    "256k","37.10","1.09","83.90","1.49"

MMC RAW FIO 1G
^^^^^^^^^^^^^^

.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "1m","42.70","0.81","88.30","1.10"
    "4m","42.70","0.66","88.30","0.81"
    "4k","2.83","1.33","13.10","3.82"
    "256k","36.50","0.94","84.50","1.41"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.62 (min 10.41, max 10.73)","0.82 (min 0.72, max 1.04)","10.71","0.68"
    "262144","10.52 (min 10.30, max 10.84)","0.85 (min 0.73, max 1.26)","11.14","0.69"
    "524288","10.63 (min 10.60, max 10.67)","0.85 (min 0.76, max 1.09)","11.08","0.63"
    "1048576","10.43 (min 10.36, max 10.57)","0.86 (min 0.72, max 1.06)","10.87","0.62"
    "5242880","11.13 (min 11.06, max 11.17)","0.84 (min 0.72, max 1.21)","12.01","0.69"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","37236.36","71859.65"
    "800000","46022.47","81108.91"
    "1000000","47216.14","86231.58"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

USB Driver
-------------------------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","31.60"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","27.70"

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62pxx_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","23437.31"
    "aes-128-cbc","16","418.09"
    "aes-128-cbc","16384","85475.33"
    "aes-128-cbc","256","6860.89"
    "aes-128-cbc","64","1826.92"
    "aes-128-cbc","8192","71669.08"
    "aes-128-ecb","1024","23842.13"
    "aes-128-ecb","16","431.57"
    "aes-128-ecb","16384","87714.47"
    "aes-128-ecb","256","7033.69"
    "aes-128-ecb","64","1867.22"
    "aes-128-ecb","8192","73673.39"
    "aes-192-cbc","1024","22849.19"
    "aes-192-cbc","16","419.90"
    "aes-192-cbc","16384","77130.41"
    "aes-192-cbc","256","6825.47"
    "aes-192-cbc","64","1823.79"
    "aes-192-cbc","8192","65653.42"
    "aes-192-ecb","1024","23388.50"
    "aes-192-ecb","16","430.66"
    "aes-192-ecb","16384","79205.72"
    "aes-192-ecb","256","6999.81"
    "aes-192-ecb","64","1872.60"
    "aes-192-ecb","8192","67548.50"
    "aes-256-cbc","1024","22113.62"
    "aes-256-cbc","16","418.55"
    "aes-256-cbc","16384","70593.19"
    "aes-256-cbc","256","6764.97"
    "aes-256-cbc","64","1822.06"
    "aes-256-cbc","8192","61227.01"
    "aes-256-ecb","1024","22848.51"
    "aes-256-ecb","16","429.44"
    "aes-256-ecb","16384","72406.36"
    "aes-256-ecb","256","6989.06"
    "aes-256-ecb","64","1867.35"
    "aes-256-ecb","8192","62788.95"
    "sha256","1024","35276.46"
    "sha256","16","584.42"
    "sha256","16384","290111.49"
    "sha256","256","9243.48"
    "sha256","64","2319.10"
    "sha256","8192","191660.03"
    "sha512","1024","24752.81"
    "sha512","16","563.81"
    "sha512","16384","67693.23"
    "sha512","256","8133.46"
    "sha512","64","2253.44"
    "sha512","8192","60473.34"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62pxx_sk-fs: CPU Load"

    "aes-128-cbc","31.00"
    "aes-128-ecb","32.00"
    "aes-192-cbc","31.00"
    "aes-192-ecb","31.00"
    "aes-256-cbc","30.00"
    "aes-256-ecb","31.00"
    "sha256","96.00"
    "sha512","96.00"

Listed for each algorithm are the code snippets used to run each benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

|

Low Power Performance
-------------------------

Table:  **Deep sleep**

.. csv-table::
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","12.98"
   "vddr_core","0.85","1.01"
   "soc_dvdd_3v3","3.30","5.65"
   "soc_dvdd_1v8","1.80","2.76"
   "vdda_1v8","1.80","72.23"
   "vdd_lpddr4/vdd_ddr4","1.10","3.75"
   "Total"," ","98.37"

Table:  **MCU only**

.. csv-table::
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","203.98"
   "vddr_core","0.85","2.44"
   "soc_dvdd_3v3","3.30","5.55"
   "soc_dvdd_1v8","1.80","2.68"
   "vdda_1v8","1.80","81.25"
   "vdd_lpddr4/vdd_ddr4","1.10","4.33"
   "Total"," ","300.24"

Partial I/O Data
- All voltage rails were measured to be near 0V

.. note::

   The power consumption on the vdda_1v8 rail is not indicitive of the SoC's power consumption due to an oscillator on the rail
   that has significant current consumption.

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)
