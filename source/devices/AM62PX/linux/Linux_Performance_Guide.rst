
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

    "af_unix_sock_stream_latency (microsec)","26.04"
    "af_unix_socket_stream_bandwidth (MBs)","1242.15"
    "bw_file_rd-io-1mb (MB/s)","1340.03"
    "bw_file_rd-o2c-1mb (MB/s)","696.99"
    "bw_mem-bcopy-16mb (MB/s)","1978.97"
    "bw_mem-bcopy-1mb (MB/s)","2120.28"
    "bw_mem-bcopy-2mb (MB/s)","1874.41"
    "bw_mem-bcopy-4mb (MB/s)","1921.23"
    "bw_mem-bcopy-8mb (MB/s)","1953.60"
    "bw_mem-bzero-16mb (MB/s)","8112.22"
    "bw_mem-bzero-1mb (MB/s)","5117.85 (min 2120.28, max 8115.42)"
    "bw_mem-bzero-2mb (MB/s)","4990.07 (min 1874.41, max 8105.73)"
    "bw_mem-bzero-4mb (MB/s)","5015.36 (min 1921.23, max 8109.48)"
    "bw_mem-bzero-8mb (MB/s)","5029.49 (min 1953.60, max 8105.37)"
    "bw_mem-cp-16mb (MB/s)","987.78"
    "bw_mem-cp-1mb (MB/s)","4645.28 (min 963.39, max 8327.17)"
    "bw_mem-cp-2mb (MB/s)","4594.23 (min 944.73, max 8243.73)"
    "bw_mem-cp-4mb (MB/s)","4569.42 (min 965.83, max 8173.00)"
    "bw_mem-cp-8mb (MB/s)","4596.80 (min 1051.11, max 8142.49)"
    "bw_mem-fcp-16mb (MB/s)","1835.49"
    "bw_mem-fcp-1mb (MB/s)","4971.12 (min 1826.82, max 8115.42)"
    "bw_mem-fcp-2mb (MB/s)","4902.05 (min 1698.37, max 8105.73)"
    "bw_mem-fcp-4mb (MB/s)","4917.06 (min 1724.63, max 8109.48)"
    "bw_mem-fcp-8mb (MB/s)","4965.41 (min 1825.44, max 8105.37)"
    "bw_mem-frd-16mb (MB/s)","2013.85"
    "bw_mem-frd-1mb (MB/s)","1980.46 (min 1826.82, max 2134.09)"
    "bw_mem-frd-2mb (MB/s)","1782.55 (min 1698.37, max 1866.72)"
    "bw_mem-frd-4mb (MB/s)","1839.20 (min 1724.63, max 1953.76)"
    "bw_mem-frd-8mb (MB/s)","1884.66 (min 1825.44, max 1943.87)"
    "bw_mem-fwr-16mb (MB/s)","8138.35"
    "bw_mem-fwr-1mb (MB/s)","5230.63 (min 2134.09, max 8327.17)"
    "bw_mem-fwr-2mb (MB/s)","5055.23 (min 1866.72, max 8243.73)"
    "bw_mem-fwr-4mb (MB/s)","5063.38 (min 1953.76, max 8173.00)"
    "bw_mem-fwr-8mb (MB/s)","5043.18 (min 1943.87, max 8142.49)"
    "bw_mem-rd-16mb (MB/s)","2075.50"
    "bw_mem-rd-1mb (MB/s)","2173.92 (min 2036.31, max 2311.52)"
    "bw_mem-rd-2mb (MB/s)","1942.69 (min 1860.75, max 2024.63)"
    "bw_mem-rd-4mb (MB/s)","1988.88 (min 1912.35, max 2065.40)"
    "bw_mem-rd-8mb (MB/s)","2004.14 (min 1949.08, max 2059.20)"
    "bw_mem-rdwr-16mb (MB/s)","1988.57"
    "bw_mem-rdwr-1mb (MB/s)","1458.43 (min 963.39, max 1953.47)"
    "bw_mem-rdwr-2mb (MB/s)","1308.49 (min 944.73, max 1672.24)"
    "bw_mem-rdwr-4mb (MB/s)","1428.10 (min 965.83, max 1890.36)"
    "bw_mem-rdwr-8mb (MB/s)","1479.64 (min 1051.11, max 1908.17)"
    "bw_mem-wr-16mb (MB/s)","1982.16"
    "bw_mem-wr-1mb (MB/s)","1994.89 (min 1953.47, max 2036.31)"
    "bw_mem-wr-2mb (MB/s)","1766.50 (min 1672.24, max 1860.75)"
    "bw_mem-wr-4mb (MB/s)","1901.36 (min 1890.36, max 1912.35)"
    "bw_mem-wr-8mb (MB/s)","1928.63 (min 1908.17, max 1949.08)"
    "bw_mmap_rd-mo-1mb (MB/s)","2261.66"
    "bw_mmap_rd-o2c-1mb (MB/s)","611.90"
    "bw_pipe (MB/s)","816.85"
    "bw_unix (MB/s)","1242.15"
    "lat_connect (us)","56.89"
    "lat_ctx-2-128k (us)","5.52"
    "lat_ctx-2-256k (us)","4.50"
    "lat_ctx-4-128k (us)","5.61"
    "lat_ctx-4-256k (us)","4.42"
    "lat_fs-0k (num_files)","245.00"
    "lat_fs-10k (num_files)","127.00"
    "lat_fs-1k (num_files)","171.00"
    "lat_fs-4k (num_files)","170.00"
    "lat_mem_rd-stride128-sz1000k (ns)","29.40"
    "lat_mem_rd-stride128-sz125k (ns)","5.56"
    "lat_mem_rd-stride128-sz250k (ns)","5.85"
    "lat_mem_rd-stride128-sz31k (ns)","3.65"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","7.72"
    "lat_mem_rd-stride128-sz62k (ns)","5.21"
    "lat_mmap-1m (us)","59.00"
    "lat_ops-double-add (ns)","2.86"
    "lat_ops-double-div (ns)","15.75"
    "lat_ops-double-mul (ns)","2.86"
    "lat_ops-float-add (ns)","2.86"
    "lat_ops-float-div (ns)","9.30"
    "lat_ops-float-mul (ns)","2.86"
    "lat_ops-int-add (ns)","0.72"
    "lat_ops-int-bit (ns)","0.48"
    "lat_ops-int-div (ns)","4.29"
    "lat_ops-int-mod (ns)","4.54"
    "lat_ops-int-mul (ns)","3.07"
    "lat_ops-int64-add (ns)","0.72"
    "lat_ops-int64-bit (ns)","0.48"
    "lat_ops-int64-div (ns)","6.80"
    "lat_ops-int64-mod (ns)","5.25"
    "lat_ops-int64-mul (ns)","3.55"
    "lat_pagefault (us)","1.35"
    "lat_pipe (us)","23.15"
    "lat_proc-exec (us)","798.57"
    "lat_proc-fork (us)","622.44"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","35.08"
    "lat_sem (us)","2.34"
    "lat_sig-catch (us)","5.79"
    "lat_sig-install (us)","0.67"
    "lat_sig-prot (us)","1.17"
    "lat_syscall-fstat (us)","2.04"
    "lat_syscall-null (us)","0.46"
    "lat_syscall-open (us)","147.05"
    "lat_syscall-read (us)","0.83"
    "lat_syscall-stat (us)","5.13"
    "lat_syscall-write (us)","0.74"
    "lat_tcp (us)","0.94"
    "lat_unix (us)","26.04"
    "latency_for_0.50_mb_block_size (nanosec)","7.72"
    "latency_for_1.00_mb_block_size (nanosec)","14.70 (min 0.00, max 29.40)"
    "pipe_bandwidth (MBs)","816.85"
    "pipe_latency (microsec)","23.15"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","35.08"
    "semaphore_latency (microsec)","2.34"
    "signal_handler_latency (microsec)","0.67"
    "signal_handler_overhead (microsec)","5.79"
    "tcp_ip_connection_cost_to_localhost (microsec)","56.89"
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

    "whetstone (MIPS)","10000.00"

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "linpack (Kflops)","577468.00"

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
    "fourier (Iterations)","22832.00"
    "fp_emulation (Iterations)","215.66"
    "huffman (Iterations)","1184.10"
    "idea (Iterations)","3444.90"
    "lu_decomposition (Iterations)","527.85"
    "neural_net (Iterations)","8.65"
    "numeric_sort (Iterations)","623.80"
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

    "add (MB/s)","1876.80"
    "copy (MB/s)","3174.00"
    "scale (MB/s)","2366.10"
    "triad (MB/s)","1732.90"

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
    "coremark-pro ()","946.22"
    "linear_alg-mid-100x100-sp (workloads/)","14.68"
    "loops-all-mid-10k-sp (workloads/)","0.72"
    "nnet_test (workloads/)","1.09"
    "parser-125k (workloads/)","8.77"
    "radix2-big-64k (workloads/)","74.22"
    "sha-test (workloads/)","81.97"
    "zip-test (workloads/)","22.22"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62pxx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","47.62"
    "core (workloads/)","0.34"
    "coremark-pro ()","997.73"
    "linear_alg-mid-100x100-sp (workloads/)","16.74"
    "loops-all-mid-10k-sp (workloads/)","0.78"
    "nnet_test (workloads/)","1.24"
    "parser-125k (workloads/)","8.47"
    "radix2-big-64k (workloads/)","53.48"
    "sha-test (workloads/)","93.46"
    "zip-test (workloads/)","25.00"

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

    "4m-check (workloads/)","417.57"
    "4m-check-reassembly (workloads/)","120.92"
    "4m-check-reassembly-tcp (workloads/)","59.10"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","33.50"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.91"
    "4m-cmykw2 (workloads/)","247.22"
    "4m-cmykw2-rotatew2 (workloads/)","49.75"
    "4m-reassembly (workloads/)","81.37"
    "4m-rotatew2 (workloads/)","53.19"
    "4m-tcp-mixed (workloads/)","119.40"
    "4m-x264w2 (workloads/)","1.96"
    "idct-4m (workloads/)","19.25"
    "idct-4mw1 (workloads/)","19.26"
    "ippktcheck-4m (workloads/)","418.55"
    "ippktcheck-4mw1 (workloads/)","418.48"
    "ipres-4m (workloads/)","111.36"
    "ipres-4mw1 (workloads/)","110.78"
    "md5-4m (workloads/)","28.91"
    "md5-4mw1 (workloads/)","29.00"
    "rgbcmyk-4m (workloads/)","65.77"
    "rgbcmyk-4mw1 (workloads/)","65.81"
    "rotate-4ms1 (workloads/)","23.40"
    "rotate-4ms1w1 (workloads/)","23.44"
    "rotate-4ms64 (workloads/)","23.63"
    "rotate-4ms64w1 (workloads/)","23.65"
    "x264-4mq (workloads/)","0.58"
    "x264-4mqw1 (workloads/)","0.58"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62pxx_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","15.73 (min 15.10, max 16.07)"

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

    "8000","255997.00","0.10"
    "11025","352797.00","0.13"
    "16000","511996.00","0.09"
    "22050","705595.00","0.24"
    "24000","705594.00","0.24"
    "32000","1023990.00","0.14"
    "44100","1411186.00","0.38"
    "48000","1535986.00","0.19"
    "88200","2822372.00","0.82"
    "96000","3071969.00","1.99"

|

Graphics SGX/RGX Driver
-------------------------
 
GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62pxx_sk-fs: Score","am62pxx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","912.45","14.72"
    " GFXBench 3.x gl_trex_off","1585.91","28.32"
    " GFXBench 4.x gl_4_off","261.99","4.43"
    " GFXBench 5.x gl_5_high_off","113.71","1.77"

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

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1731.05","62.00"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1840.85","37.62"

.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62pxx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62pxx_sk-fs: THROUGHPUT (Mbits/sec)","am62pxx_sk-fs: Packets Per Second (kPPS)","am62pxx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","16.16","112.00","39.62"
    "128","82.00","72.51","111.00","39.64"
    "256","210.00","184.86","110.00","39.48"
    "1024","978.00","899.23","115.00","44.49"
    "1518","1472.00","956.71","81.00","31.44"

|

Linux OSPI Flash Driver
-------------------------

AM62PXX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Write UBIFS CPU Load (%)","am62pxx_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62pxx_sk-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.28)","13.09 (min 11.87, max 14.11)","28.67","6.90"
    "262144","0.15 (min 0.11, max 0.19)","12.87 (min 11.47, max 14.01)","28.65","10.00"
    "524288","0.15 (min 0.11, max 0.19)","13.33 (min 10.92, max 15.20)","28.61","12.50"
    "1048576","0.15 (min 0.11, max 0.19)","13.52 (min 11.60, max 15.26)","28.34","10.00"

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

    "1m","91.50","2.28","289.00","4.43"
    "4m","97.50","1.64","288.00","3.63"
    "4k","78.60","33.12","92.30","30.52"
    "256k","91.30","2.80","287.00","5.93"

EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "1m","91.40","1.46","293.00","2.84"
    "4m","97.70","1.03","150.00","1.27"
    "4k","73.20","10.75","74.50","10.06"
    "256k","91.30","1.67","293.00","4.09"

EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Write EXT4 CPU Load (%)","am62pxx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62pxx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","68.60 (min 50.94, max 73.14)","4.85 (min 4.72, max 4.90)","131.58","7.81"
    "262144","60.52 (min 42.63, max 73.77)","4.51 (min 2.94, max 6.97)","178.25","10.97"
    "524288","61.34 (min 42.90, max 73.64)","4.53 (min 2.77, max 7.10)","101.57","5.81"
    "1048576","61.38 (min 42.59, max 75.22)","4.48 (min 3.04, max 6.62)","127.76","6.13"
    "5242880","61.57 (min 42.50, max 73.83)","4.57 (min 2.74, max 7.04)","133.97","7.30"

EMMC VFAT
^^^^^^^^^

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Write VFAT CPU Load (%)","am62pxx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62pxx_sk-fs: Read VFAT CPU Load (%)"

    "102400","37.66 (min 11.58, max 47.12)","4.45 (min 3.35, max 4.95)","142.56","8.14"
    "262144","43.19 (min 11.44, max 60.84)","5.96 (min 4.35, max 7.06)","263.29","16.88"
    "524288","45.51 (min 12.51, max 64.59)","4.99 (min 3.85, max 6.03)","185.39","8.64"
    "1048576","45.58 (min 12.18, max 65.61)","4.50 (min 3.37, max 5.51)","186.57","9.05"
    "5242880","47.38 (min 12.30, max 69.10)","4.74 (min 3.33, max 6.00)","188.52","10.31"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62pxx_sk-fs: Write Throughput (Kbytes/sec)","am62pxx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","97523.81","248242.42"
    "4000000","100207.95","267493.88"

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

    "1m","40.80","1.02","85.10","1.21"
    "4m","39.80","0.68","84.70","1.01"
    "4k","2.81","1.40","13.70","4.53"
    "256k","37.80","1.11","84.30","1.49"

MMC RAW FIO 1G
^^^^^^^^^^^^^^

.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "1m","43.20","1.33","88.10","1.87"
    "4m","43.10","1.10","88.10","1.45"
    "4k","3.56","2.40","16.60","7.99"
    "256k","39.90","1.47","86.10","2.20"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62pxx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Write Raw CPU Load (%)","am62pxx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62pxx_sk-fs: Read Raw CPU Load (%)"

    "102400","9.88 (min 9.65, max 10.41)","0.77 (min 0.67, max 1.07)","11.09","0.69"
    "262144","10.40 (min 10.14, max 10.83)","0.90 (min 0.70, max 1.39)","11.15","0.69"
    "524288","10.60 (min 10.53, max 10.74)","0.81 (min 0.65, max 1.16)","11.25","0.54"
    "1048576","10.32 (min 10.11, max 10.63)","0.81 (min 0.68, max 1.04)","11.06","0.61"
    "5242880","11.00 (min 10.77, max 11.12)","0.83 (min 0.69, max 1.15)","12.01","0.57"

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

    "150","34.50"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62pxx_sk-fs: Throughput (MB/sec)"

    "150","28.10"

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62pxx_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","17659.22"
    "aes-128-cbc","16","294.87"
    "aes-128-cbc","16384","77081.26"
    "aes-128-cbc","256","5147.73"
    "aes-128-cbc","64","1305.37"
    "aes-128-cbc","8192","62117.21"
    "aes-128-ecb","1024","17919.66"
    "aes-128-ecb","16","300.60"
    "aes-128-ecb","16384","79205.72"
    "aes-128-ecb","256","5244.59"
    "aes-128-ecb","64","1334.36"
    "aes-128-ecb","8192","63589.03"
    "aes-192-cbc","1024","17438.72"
    "aes-192-cbc","16","295.00"
    "aes-192-cbc","16384","70429.35"
    "aes-192-cbc","256","5156.01"
    "aes-192-cbc","64","1305.26"
    "aes-192-cbc","8192","57969.32"
    "aes-192-ecb","1024","17724.07"
    "aes-192-ecb","16","299.00"
    "aes-192-ecb","16384","72045.91"
    "aes-192-ecb","256","5219.33"
    "aes-192-ecb","64","1328.51"
    "aes-192-ecb","8192","58829.48"
    "aes-256-cbc","1024","17347.24"
    "aes-256-cbc","16","294.71"
    "aes-256-cbc","16384","64481.96"
    "aes-256-cbc","256","5137.75"
    "aes-256-cbc","64","1301.85"
    "aes-256-cbc","8192","54061.74"
    "aes-256-ecb","1024","17631.57"
    "aes-256-ecb","16","299.74"
    "aes-256-ecb","16384","66027.52"
    "aes-256-ecb","256","5219.84"
    "aes-256-ecb","64","1331.84"
    "aes-256-ecb","8192","55323.31"
    "sha256","1024","19539.63"
    "sha256","16","325.38"
    "sha256","16384","157750.61"
    "sha256","256","5084.33"
    "sha256","64","1286.27"
    "sha256","8192","107025.75"
    "sha512","1024","13944.49"
    "sha512","16","319.83"
    "sha512","16384","38677.16"
    "sha512","256","4573.70"
    "sha512","64","1279.77"
    "sha512","8192","34559.32"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62pxx_sk-fs: CPU Load"

    "aes-128-cbc","38.00"
    "aes-128-ecb","39.00"
    "aes-192-cbc","38.00"
    "aes-192-ecb","39.00"
    "aes-256-cbc","37.00"
    "aes-256-ecb","38.00"
    "sha256","97.00"
    "sha512","97.00"

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
