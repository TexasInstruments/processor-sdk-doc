
====================================
 Linux 11.00.15.05 Performance Guide
====================================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
| AM62Lx EVM     | AM62Lx Evaluation Module rev E1-1 with ARM running at 1.4GHz, DDR data rate 1600 MT/S                          |
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
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "af_unix_sock_stream_latency (microsec)","32.52"
    "af_unix_socket_stream_bandwidth (MBs)","432.01"
    "bw_file_rd-io-1mb (MB/s)","936.15"
    "bw_file_rd-o2c-1mb (MB/s)","462.32"
    "bw_mem-bcopy-16mb (MB/s)","704.35"
    "bw_mem-bcopy-1mb (MB/s)","739.92"
    "bw_mem-bcopy-2mb (MB/s)","715.95"
    "bw_mem-bcopy-4mb (MB/s)","694.93"
    "bw_mem-bcopy-8mb (MB/s)","734.08"
    "bw_mem-bzero-16mb (MB/s)","2113.33"
    "bw_mem-bzero-1mb (MB/s)","1429.47 (min 739.92, max 2119.02)"
    "bw_mem-bzero-2mb (MB/s)","1410.98 (min 715.95, max 2106.00)"
    "bw_mem-bzero-4mb (MB/s)","1400.28 (min 694.93, max 2105.63)"
    "bw_mem-bzero-8mb (MB/s)","1390.98 (min 734.08, max 2047.87)"
    "bw_mem-cp-16mb (MB/s)","400.91"
    "bw_mem-cp-1mb (MB/s)","1355.73 (min 399.31, max 2312.14)"
    "bw_mem-cp-2mb (MB/s)","1280.47 (min 393.31, max 2167.63)"
    "bw_mem-cp-4mb (MB/s)","1290.96 (min 423.64, max 2158.27)"
    "bw_mem-cp-8mb (MB/s)","1296.73 (min 446.10, max 2147.36)"
    "bw_mem-fcp-16mb (MB/s)","712.76"
    "bw_mem-fcp-1mb (MB/s)","1452.53 (min 786.04, max 2119.02)"
    "bw_mem-fcp-2mb (MB/s)","1434.10 (min 762.20, max 2106.00)"
    "bw_mem-fcp-4mb (MB/s)","1453.30 (min 800.96, max 2105.63)"
    "bw_mem-fcp-8mb (MB/s)","1430.32 (min 812.76, max 2047.87)"
    "bw_mem-frd-16mb (MB/s)","1277.75"
    "bw_mem-frd-1mb (MB/s)","1009.87 (min 786.04, max 1233.70)"
    "bw_mem-frd-2mb (MB/s)","983.24 (min 762.20, max 1204.28)"
    "bw_mem-frd-4mb (MB/s)","1023.15 (min 800.96, max 1245.33)"
    "bw_mem-frd-8mb (MB/s)","1039.49 (min 812.76, max 1266.22)"
    "bw_mem-fwr-16mb (MB/s)","2119.77"
    "bw_mem-fwr-1mb (MB/s)","1772.92 (min 1233.70, max 2312.14)"
    "bw_mem-fwr-2mb (MB/s)","1685.96 (min 1204.28, max 2167.63)"
    "bw_mem-fwr-4mb (MB/s)","1701.80 (min 1245.33, max 2158.27)"
    "bw_mem-fwr-8mb (MB/s)","1706.79 (min 1266.22, max 2147.36)"
    "bw_mem-rd-16mb (MB/s)","1273.78"
    "bw_mem-rd-1mb (MB/s)","928.42 (min 601.23, max 1255.61)"
    "bw_mem-rd-2mb (MB/s)","885.57 (min 520.36, max 1250.78)"
    "bw_mem-rd-4mb (MB/s)","885.23 (min 516.33, max 1254.12)"
    "bw_mem-rd-8mb (MB/s)","975.55 (min 681.66, max 1269.44)"
    "bw_mem-rdwr-16mb (MB/s)","689.74"
    "bw_mem-rdwr-1mb (MB/s)","461.90 (min 399.31, max 524.48)"
    "bw_mem-rdwr-2mb (MB/s)","466.16 (min 393.31, max 539.01)"
    "bw_mem-rdwr-4mb (MB/s)","512.76 (min 423.64, max 601.87)"
    "bw_mem-rdwr-8mb (MB/s)","566.43 (min 446.10, max 686.75)"
    "bw_mem-wr-16mb (MB/s)","717.49"
    "bw_mem-wr-1mb (MB/s)","562.86 (min 524.48, max 601.23)"
    "bw_mem-wr-2mb (MB/s)","529.69 (min 520.36, max 539.01)"
    "bw_mem-wr-4mb (MB/s)","559.10 (min 516.33, max 601.87)"
    "bw_mem-wr-8mb (MB/s)","684.21 (min 681.66, max 686.75)"
    "bw_mmap_rd-mo-1mb (MB/s)","1145.48"
    "bw_mmap_rd-o2c-1mb (MB/s)","478.93"
    "bw_pipe (MB/s)","438.63"
    "bw_unix (MB/s)","432.01"
    "lat_connect (us)","75.81"
    "lat_ctx-2-128k (us)","13.11"
    "lat_ctx-2-256k (us)","36.99"
    "lat_ctx-4-128k (us)","14.81"
    "lat_ctx-4-256k (us)","14.32"
    "lat_fs-0k (num_files)","195.00"
    "lat_fs-10k (num_files)","87.00"
    "lat_fs-1k (num_files)","131.00"
    "lat_fs-4k (num_files)","131.00"
    "lat_mem_rd-stride128-sz1000k (ns)","52.39"
    "lat_mem_rd-stride128-sz125k (ns)","6.18"
    "lat_mem_rd-stride128-sz250k (ns)","17.61"
    "lat_mem_rd-stride128-sz31k (ns)","2.42"
    "lat_mem_rd-stride128-sz50 (ns)","2.41"
    "lat_mem_rd-stride128-sz500k (ns)","46.57"
    "lat_mem_rd-stride128-sz62k (ns)","5.74"
    "lat_mmap-1m (us)","70.00"
    "lat_ops-double-add (ns)","3.21"
    "lat_ops-double-div (ns)","17.66"
    "lat_ops-double-mul (ns)","3.21"
    "lat_ops-float-add (ns)","3.21"
    "lat_ops-float-div (ns)","10.44"
    "lat_ops-float-mul (ns)","3.21"
    "lat_ops-int-add (ns)","0.80"
    "lat_ops-int-bit (ns)","0.53"
    "lat_ops-int-div (ns)","4.81"
    "lat_ops-int-mod (ns)","5.08"
    "lat_ops-int-mul (ns)","3.44"
    "lat_ops-int64-add (ns)","0.80"
    "lat_ops-int64-bit (ns)","0.53"
    "lat_ops-int64-div (ns)","7.62"
    "lat_ops-int64-mod (ns)","5.88"
    "lat_ops-int64-mul (ns)","3.98"
    "lat_pagefault (us)","1.80"
    "lat_pipe (us)","24.62"
    "lat_proc-exec (us)","1551.25"
    "lat_proc-fork (us)","1343.25"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","38.16"
    "lat_sem (us)","4.04"
    "lat_sig-catch (us)","5.97"
    "lat_sig-install (us)","0.75"
    "lat_sig-prot (us)","0.61"
    "lat_syscall-fstat (us)","2.09"
    "lat_syscall-null (us)","0.51"
    "lat_syscall-open (us)","418.36"
    "lat_syscall-read (us)","0.88"
    "lat_syscall-stat (us)","5.27"
    "lat_syscall-write (us)","0.85"
    "lat_tcp (us)","1.02"
    "lat_unix (us)","32.52"
    "latency_for_0.50_mb_block_size (nanosec)","46.57"
    "latency_for_1.00_mb_block_size (nanosec)","26.19 (min 0.00, max 52.39)"
    "pipe_bandwidth (MBs)","438.63"
    "pipe_latency (microsec)","24.62"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","38.16"
    "semaphore_latency (microsec)","4.04"
    "signal_handler_latency (microsec)","0.75"
    "signal_handler_overhead (microsec)","5.97"
    "tcp_ip_connection_cost_to_localhost (microsec)","75.81"
    "tcp_latency_using_localhost (microsec)","1.02"




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
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cpu_clock (MHz)","400.00"
    "dhrystone_per_mhz (DMIPS/MHz)","9.20"
    "dhrystone_per_second (DhrystoneP)","6451613.00"



Whetstone
^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "whetstone (MIPS)","5000.00"




Linpack
^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "linpack (Kflops)","511674.00"




NBench
^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "assignment (Iterations)","12.99"
    "fourier (Iterations)","20380.00"
    "fp_emulation (Iterations)","192.46"
    "huffman (Iterations)","1056.50"
    "idea (Iterations)","3074.50"
    "lu_decomposition (Iterations)","475.39"
    "neural_net (Iterations)","7.73"
    "numeric_sort (Iterations)","555.93"
    "string_sort (Iterations)","146.40"




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
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "add (MB/s)","1538.50"
    "copy (MB/s)","1605.30"
    "scale (MB/s)","1718.90"
    "triad (MB/s)","1526.50"




CoreMarkPro
^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","37.31"
    "core (workloads/)","0.27"
    "coremark-pro ()","688.91"
    "linear_alg-mid-100x100-sp (workloads/)","13.08"
    "loops-all-mid-10k-sp (workloads/)","0.56"
    "nnet_test (workloads/)","0.97"
    "parser-125k (workloads/)","5.88"
    "radix2-big-64k (workloads/)","18.16"
    "sha-test (workloads/)","69.93"
    "zip-test (workloads/)","18.52"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","70.92"
    "core (workloads/)","0.53"
    "coremark-pro ()","1170.45"
    "linear_alg-mid-100x100-sp (workloads/)","25.61"
    "loops-all-mid-10k-sp (workloads/)","0.99"
    "nnet_test (workloads/)","1.90"
    "parser-125k (workloads/)","5.48"
    "radix2-big-64k (workloads/)","26.26"
    "sha-test (workloads/)","138.89"
    "zip-test (workloads/)","32.26"

 
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
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "4m-check (workloads/)","314.35"
    "4m-check-reassembly (workloads/)","64.10"
    "4m-check-reassembly-tcp (workloads/)","39.75"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","17.39"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","0.94"
    "4m-cmykw2 (workloads/)","110.87"
    "4m-cmykw2-rotatew2 (workloads/)","23.34"
    "4m-reassembly (workloads/)","57.24"
    "4m-rotatew2 (workloads/)","23.21"
    "4m-tcp-mixed (workloads/)","105.96"
    "4m-x264w2 (workloads/)","0.95"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","17.08"
    "idct-4mw1 (workloads/)","17.09"
    "ippktcheck-4m (workloads/)","313.83"
    "ippktcheck-4mw1 (workloads/)","312.23"
    "ipres-4m (workloads/)","75.15"
    "ipres-4mw1 (workloads/)","75.23"
    "md5-4m (workloads/)","19.67"
    "md5-4mw1 (workloads/)","19.62"
    "rgbcmyk-4m (workloads/)","56.92"
    "rgbcmyk-4mw1 (workloads/)","56.96"
    "rotate-4ms1 (workloads/)","20.58"
    "rotate-4ms1w1 (workloads/)","20.55"
    "rotate-4ms64 (workloads/)","20.82"
    "rotate-4ms64w1 (workloads/)","20.89"
    "x264-4mq (workloads/)","0.51"
    "x264-4mqw1 (workloads/)","0.51"



Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62lxx_evm-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","19.37 (min 19.00, max 19.75)"

 

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.



|

ALSA SoC Audio Driver
---------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62lxx_evm-fs: Throughput (bits/sec)","am62lxx_evm-fs: CPU Load (%)"

    "8000","255998.00","1.04"
    "11025","352797.00","1.03"
    "16000","511995.00","0.98"
    "22050","705593.00","1.16"
    "24000","705593.00","1.18"
    "32000","1023991.00","1.01"
    "44100","1411186.00","1.25"
    "48000","1535985.00","1.19"
    "88200","2822365.00","1.76"
    "96000","3071960.00","1.05"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62lxx_evm-fs: Throughput (bits/sec)","am62lxx_evm-fs: CPU Load (%)"

    "8000","255334.00","0.99"
    "11025","352944.00","0.81"
    "16000","512208.00","0.78"
    "22050","705887.00","0.79"
    "24000","705883.00","0.87"
    "32000","1024414.00","0.79"
    "44100","1411770.00","1.08"
    "48000","1536621.00","1.43"
    "88200","2823533.00","1.32"
    "96000","3073232.00","0.87"

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


.. rubric::  TCP Bidirectional Throughput 
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1243.73","96.90"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1148.94","95.96"



.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62lxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: Packets Per Second (kPPS)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","11.89","83.00","85.06"
    "128","82.00","56.95","87.00","84.68"
    "256","210.00","142.75","85.00","51.47"
    "1024","978.00","606.16","77.00","81.25"
    "1518","1472.00","877.82","75.00","81.39"




.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62lxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: Packets Per Second (kPPS)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","1.21","8.00","8.87"
    "128","82.00","3.08","5.00","3.80"
    "256","210.00","13.61","8.00","5.80"
    "1024","978.00","65.72","8.00","8.75"
    "1518","1472.00","98.92","8.00","11.86"




.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62lxx_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: Packets Per Second (kPPS)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","am62lxx_evm-fs: Packet Loss %"

    "64","18.00","20.14","140.00","80.40","83.81"
    "128","82.00","66.92","102.00","73.67","79.35"
    "256","210.00","191.78","114.00","80.03","46.16"
    "1024","978.00","629.86","81.00","77.38","11.72"
    "1518","1472.00","721.91","61.00","84.22","6.20"


|

Linux OSPI Flash Driver
-----------------------


AM62LXX-EVM
^^^^^^^^^^^


UBIFS
"""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write UBIFS Throughput (Mbytes/sec)","am62lxx_evm-fs: Write UBIFS CPU Load (%)","am62lxx_evm-fs: Read UBIFS Throughput (Mbytes/sec)","am62lxx_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.28)","51.32 (min 50.77, max 51.89)","56.02","50.00"
    "262144","0.14 (min 0.11, max 0.19)","51.75 (min 50.99, max 53.37)","56.09","42.86"
    "524288","0.14 (min 0.11, max 0.19)","51.41 (min 50.80, max 52.05)","56.14","33.33"
    "1048576","0.14 (min 0.11, max 0.19)","51.64 (min 51.40, max 51.84)","53.84","37.50"



RAW
"""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62lxx_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","16.78"


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
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

    "1m","128.00","9.30","180.00","8.80"
    "4m","125.00","6.05","180.00","5.24"
    "4k","85.10","59.89","91.90","56.88"
    "256k","122.00","12.02","179.00","10.41"

 
EMMC RAW FIO 1G
^^^^^^^^^^^^^^^


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "1m","35.80","3.58","44.30","3.39"
    "4m","38.40","2.84","44.30","2.33"
    "4k","27.80","20.13","41.50","26.05"
    "256k","35.90","5.15","44.20","4.76"


EMMC EXT4
^^^^^^^^^


.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

    "102400","35.30 (min 34.37, max 35.63)","8.58 (min 7.78, max 10.89)","46.13","9.42"
    "262144","33.50 (min 28.29, max 36.51)","8.46 (min 6.57, max 10.40)","46.21","10.99"
    "524288","34.84 (min 30.34, max 36.49)","8.49 (min 6.82, max 10.91)","46.36","8.28"
    "1048576","33.58 (min 28.79, max 36.14)","7.98 (min 6.34, max 11.15)","46.34","9.07"
    "5242880","33.76 (min 28.50, max 36.40)","7.93 (min 5.88, max 10.95)","46.34","8.69"

 
EMMC VFAT
^^^^^^^^^


.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write VFAT Throughput (Mbytes/sec)","am62lxx_evm-fs: Write VFAT CPU Load (%)","am62lxx_evm-fs: Read VFAT Throughput (Mbytes/sec)","am62lxx_evm-fs: Read VFAT CPU Load (%)"

    "102400","22.07 (min 9.07, max 27.48)","11.72 (min 10.34, max 13.37)","45.80","12.22"
    "262144","25.90 (min 9.68, max 31.34)","6.65 (min 5.28, max 10.10)","45.90","10.55"
    "524288","25.86 (min 9.84, max 32.57)","9.64 (min 7.73, max 10.85)","45.88","9.43"
    "1048576","26.16 (min 9.97, max 33.33)","9.11 (min 7.40, max 10.77)","45.89","9.23"
    "5242880","28.22 (min 10.12, max 34.10)","9.96 (min 8.82, max 10.53)","45.86","9.25"


UBoot EMMC Driver
-----------------



.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62lxx_evm-fs: Write Throughput (Kbytes/sec)","am62lxx_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","114975.44","175229.95"
    "4000000","128000.00","178086.96"

 

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
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Write EXT4 CPU Load (%)","am62lxx_evm-fs: Read EXT4 Throughput (Mbytes/sec)","am62lxx_evm-fs: Read EXT4 CPU Load (%)"

    "1m","18.70","3.03","86.10","6.06"
    "4m","18.90","2.77","86.90","3.97"
    "4k","4.29","10.42","13.50","14.25"
    "256k","17.90","4.38","82.20","7.38"

 


MMC RAW FIO 1G
^^^^^^^^^^^^^^

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "1m","15.20","2.61","22.80","2.60"
    "4m","15.20","2.17","22.80","2.23"
    "4k","3.96","6.55","9.70","9.60"
    "256k","15.20","3.46","22.50","3.52"



MMC EXT4
^^^^^^^^



.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Write Raw CPU Load (%)","am62lxx_evm-fs: Read Raw Throughput (Mbytes/sec)","am62lxx_evm-fs: Read Raw CPU Load (%)"

    "102400","9.34 (min 9.21, max 9.44)","3.08 (min 2.75, max 3.57)","11.21","3.28"
    "262144","8.94 (min 8.73, max 9.11)","2.90 (min 2.58, max 3.43)","10.80","2.90"
    "524288","9.06 (min 8.83, max 9.15)","2.97 (min 2.68, max 3.50)","10.98","2.53"
    "1048576","9.09 (min 9.00, max 9.18)","2.78 (min 2.61, max 3.31)","11.22","2.58"
    "5242880","9.00 (min 8.60, max 9.26)","2.80 (min 2.58, max 3.45)","11.15","2.51"

 
 
The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 



UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^



.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62lxx_evm-fs: Write Throughput (Kbytes/sec)","am62lxx_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","19883.50","22505.49"
    "800000","16650.41","23011.24"
    "1000000","16855.97","23272.73"

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 

|

USB Driver
----------
 


USB Device Controller
^^^^^^^^^^^^^^^^^^^^^


.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62lxx_evm-fs: Throughput (MB/sec)"

    "150","37.10"




.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62lxx_evm-fs: Throughput (MB/sec)"

    "150","32.50"


Low Power Performance
---------------------

Power Performance
^^^^^^^^^^^^^^^^^

These are power measurements taken while the device is in various low power modes like
Deep Sleep and RTC Only + DDR.

.. csv-table:: Deep Sleep Power Performance
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.75", "4.88"
     "soc_dvdd_1v8", "1.80", "2.06"
     "soc_dvdd_3v3", "3.29", "2.50"
     "vdda_1v8", "1.80", "0.56"
     "vdd_lpddr4_pmic1", "1.10", "0.99"
     "vdd_rtc", "0.74", "0.01"
     "vdd_rtc_1v8", "1.80", "0.01"
     "Total"," ","~11.04"

.. csv-table:: RTC Only + DDR Power Performance
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.00", "0.00"
     "soc_dvdd_1v8", "1.80", "1.23"
     "soc_dvdd_3v3", "3.29", "1.07"
     "vdda_1v8", "0.00", "0.00"
     "vdd_lpddr4_pmic1", "1.10", "1.00"
     "vdd_rtc", "0.75", "0.02"
     "vdd_rtc_1v8", "1.80", "0.02"
     "Total"," ","3.34"
