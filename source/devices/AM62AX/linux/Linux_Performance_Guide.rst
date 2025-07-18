
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
| AM62Ax SK      | AM62Ax Starter Kit with ARM running at 1.2GHz, DDR data rate 3733 MT/S                                         |
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
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","28.80"
    "af_unix_socket_stream_bandwidth (MBs)","1158.39"
    "bw_file_rd-io-1mb (MB/s)","1367.99"
    "bw_file_rd-o2c-1mb (MB/s)","771.72"
    "bw_mem-bcopy-16mb (MB/s)","1805.05"
    "bw_mem-bcopy-1mb (MB/s)","1992.39"
    "bw_mem-bcopy-2mb (MB/s)","1734.30"
    "bw_mem-bcopy-4mb (MB/s)","1786.78"
    "bw_mem-bcopy-8mb (MB/s)","1796.74"
    "bw_mem-bzero-16mb (MB/s)","7947.02"
    "bw_mem-bzero-1mb (MB/s)","4970.90 (min 1992.39, max 7949.41)"
    "bw_mem-bzero-2mb (MB/s)","4832.55 (min 1734.30, max 7930.79)"
    "bw_mem-bzero-4mb (MB/s)","4864.51 (min 1786.78, max 7942.24)"
    "bw_mem-bzero-8mb (MB/s)","4867.28 (min 1796.74, max 7937.82)"
    "bw_mem-cp-16mb (MB/s)","930.29"
    "bw_mem-cp-1mb (MB/s)","4563.39 (min 916.59, max 8210.18)"
    "bw_mem-cp-2mb (MB/s)","4473.88 (min 893.12, max 8054.63)"
    "bw_mem-cp-4mb (MB/s)","4472.48 (min 943.51, max 8001.45)"
    "bw_mem-cp-8mb (MB/s)","4465.06 (min 959.35, max 7970.77)"
    "bw_mem-fcp-16mb (MB/s)","1724.32"
    "bw_mem-fcp-1mb (MB/s)","4842.31 (min 1735.21, max 7949.41)"
    "bw_mem-fcp-2mb (MB/s)","4754.04 (min 1577.29, max 7930.79)"
    "bw_mem-fcp-4mb (MB/s)","4822.07 (min 1701.89, max 7942.24)"
    "bw_mem-fcp-8mb (MB/s)","4749.32 (min 1560.82, max 7937.82)"
    "bw_mem-frd-16mb (MB/s)","1904.31"
    "bw_mem-frd-1mb (MB/s)","1886.69 (min 1735.21, max 2038.17)"
    "bw_mem-frd-2mb (MB/s)","1663.69 (min 1577.29, max 1750.09)"
    "bw_mem-frd-4mb (MB/s)","1642.30 (min 1582.70, max 1701.89)"
    "bw_mem-frd-8mb (MB/s)","1637.86 (min 1560.82, max 1714.90)"
    "bw_mem-fwr-16mb (MB/s)","7964.16"
    "bw_mem-fwr-1mb (MB/s)","5124.18 (min 2038.17, max 8210.18)"
    "bw_mem-fwr-2mb (MB/s)","4902.36 (min 1750.09, max 8054.63)"
    "bw_mem-fwr-4mb (MB/s)","4792.08 (min 1582.70, max 8001.45)"
    "bw_mem-fwr-8mb (MB/s)","4842.84 (min 1714.90, max 7970.77)"
    "bw_mem-rd-16mb (MB/s)","1951.93"
    "bw_mem-rd-1mb (MB/s)","1994.86 (min 1764.60, max 2225.11)"
    "bw_mem-rd-2mb (MB/s)","1756.29 (min 1568.63, max 1943.95)"
    "bw_mem-rd-4mb (MB/s)","1841.36 (min 1734.35, max 1948.37)"
    "bw_mem-rd-8mb (MB/s)","1892.72 (min 1830.87, max 1954.56)"
    "bw_mem-rdwr-16mb (MB/s)","1863.50"
    "bw_mem-rdwr-1mb (MB/s)","1331.97 (min 916.59, max 1747.34)"
    "bw_mem-rdwr-2mb (MB/s)","1205.75 (min 893.12, max 1518.37)"
    "bw_mem-rdwr-4mb (MB/s)","1310.86 (min 943.51, max 1678.20)"
    "bw_mem-rdwr-8mb (MB/s)","1371.14 (min 959.35, max 1782.93)"
    "bw_mem-wr-16mb (MB/s)","1805.67"
    "bw_mem-wr-1mb (MB/s)","1755.97 (min 1747.34, max 1764.60)"
    "bw_mem-wr-2mb (MB/s)","1543.50 (min 1518.37, max 1568.63)"
    "bw_mem-wr-4mb (MB/s)","1706.28 (min 1678.20, max 1734.35)"
    "bw_mem-wr-8mb (MB/s)","1806.90 (min 1782.93, max 1830.87)"
    "bw_mmap_rd-mo-1mb (MB/s)","2130.68"
    "bw_mmap_rd-o2c-1mb (MB/s)","731.93"
    "bw_pipe (MB/s)","791.41"
    "bw_unix (MB/s)","1158.39"
    "lat_connect (us)","56.82"
    "lat_ctx-2-128k (us)","7.87"
    "lat_ctx-2-256k (us)","8.59"
    "lat_ctx-4-128k (us)","6.76"
    "lat_ctx-4-256k (us)","9.67"
    "lat_fs-0k (num_files)","249.00"
    "lat_fs-10k (num_files)","119.00"
    "lat_fs-1k (num_files)","153.00"
    "lat_fs-4k (num_files)","146.00"
    "lat_mem_rd-stride128-sz1000k (ns)","30.87"
    "lat_mem_rd-stride128-sz125k (ns)","5.59"
    "lat_mem_rd-stride128-sz250k (ns)","5.84"
    "lat_mem_rd-stride128-sz31k (ns)","4.19"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","11.18"
    "lat_mem_rd-stride128-sz62k (ns)","4.53"
    "lat_mmap-1m (us)","50.00"
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
    "lat_ops-int64-div (ns)","6.81"
    "lat_ops-int64-mod (ns)","5.25"
    "lat_ops-int64-mul (ns)","3.55"
    "lat_pagefault (us)","1.06"
    "lat_pipe (us)","25.31"
    "lat_proc-exec (us)","693.38"
    "lat_proc-fork (us)","585.00"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","34.04"
    "lat_sem (us)","2.90"
    "lat_sig-catch (us)","5.55"
    "lat_sig-install (us)","0.68"
    "lat_sig-prot (us)","0.85"
    "lat_syscall-fstat (us)","1.96"
    "lat_syscall-null (us)","0.46"
    "lat_syscall-open (us)","212.00"
    "lat_syscall-read (us)","0.80"
    "lat_syscall-stat (us)","4.80"
    "lat_syscall-write (us)","0.76"
    "lat_tcp (us)","0.91"
    "lat_unix (us)","28.80"
    "latency_for_0.50_mb_block_size (nanosec)","11.18"
    "latency_for_1.00_mb_block_size (nanosec)","15.44 (min 0.00, max 30.87)"
    "pipe_bandwidth (MBs)","791.41"
    "pipe_latency (microsec)","25.31"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","34.04"
    "semaphore_latency (microsec)","2.90"
    "signal_handler_latency (microsec)","0.68"
    "signal_handler_overhead (microsec)","5.55"
    "tcp_ip_connection_cost_to_localhost (microsec)","56.82"
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
    :header: "Benchmarks","am62axx_sk-fs: perf"

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
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "whetstone (MIPS)","5000.00"

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "linpack (Kflops)","577662.00"

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
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "add (MB/s)","2638.50"
    "copy (MB/s)","3791.10"
    "scale (MB/s)","3538.50"
    "triad (MB/s)","2426.20"

CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","41.67"
    "core (workloads/)","0.30"
    "coremark-pro ()","940.71"
    "linear_alg-mid-100x100-sp (workloads/)","14.68"
    "loops-all-mid-10k-sp (workloads/)","0.71"
    "nnet_test (workloads/)","1.09"
    "parser-125k (workloads/)","8.77"
    "radix2-big-64k (workloads/)","72.61"
    "sha-test (workloads/)","81.30"
    "zip-test (workloads/)","22.22"

.. csv-table:: CoreMarkProFourCore Benchmarks
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","161.29"
    "core (workloads/)","1.20"
    "coremark-pro ()","2630.14"
    "linear_alg-mid-100x100-sp (workloads/)","56.37"
    "loops-all-mid-10k-sp (workloads/)","2.07"
    "nnet_test (workloads/)","3.62"
    "parser-125k (workloads/)","9.76"
    "radix2-big-64k (workloads/)","100.84"
    "sha-test (workloads/)","270.27"
    "zip-test (workloads/)","78.43"

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
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "4m-check (workloads/)","418.20"
    "4m-check-reassembly (workloads/)","124.07"
    "4m-check-reassembly-tcp (workloads/)","60.24"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","34.25"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.89"
    "4m-cmykw2 (workloads/)","248.76"
    "4m-cmykw2-rotatew2 (workloads/)","50.76"
    "4m-reassembly (workloads/)","83.19"
    "4m-rotatew2 (workloads/)","56.50"
    "4m-tcp-mixed (workloads/)","117.65"
    "4m-x264w2 (workloads/)","1.97"
    "idct-4m (workloads/)","19.25"
    "idct-4mw1 (workloads/)","19.25"
    "ippktcheck-4m (workloads/)","423.44"
    "ippktcheck-4mw1 (workloads/)","421.30"
    "ipres-4m (workloads/)","112.02"
    "ipres-4mw1 (workloads/)","113.12"
    "md5-4m (workloads/)","28.39"
    "md5-4mw1 (workloads/)","28.29"
    "rgbcmyk-4m (workloads/)","65.66"
    "rgbcmyk-4mw1 (workloads/)","65.66"
    "rotate-4ms1 (workloads/)","23.60"
    "rotate-4ms1w1 (workloads/)","23.54"
    "rotate-4ms64 (workloads/)","23.80"
    "rotate-4ms64w1 (workloads/)","23.84"
    "x264-4mq (workloads/)","0.58"
    "x264-4mqw1 (workloads/)","0.58"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62axx_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","13.68 (min 13.50, max 13.97)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

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

- CPSW3g: AM62ax

.. rubric::  TCP Bidirectional Throughput 
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1855.56","65.98"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1876.44","38.25"

.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62axx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: Packets Per Second (kPPS)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","15.73","109.00","40.72"
    "128","82.00","69.74","106.00","40.24"
    "256","210.00","177.12","105.00","40.18"
    "1024","978.00","800.79","102.00","39.91"
    "1518","1472.00","955.95","81.00","35.45"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62axx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: Packets Per Second (kPPS)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","1.02","7.00","1.11"
    "128","82.00","5.25","8.00","3.50"
    "256","210.00","13.10","8.00","2.10"
    "1024","978.00","102.49","13.00","7.14"
    "1518","1472.00","100.09","8.00","3.16"

.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62axx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: Packets Per Second (kPPS)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62axx_sk-fs: Packet Loss %"

    "64","18.00","33.07","230.00","42.67","50.74"
    "128","82.00","134.23","205.00","45.22","52.22"
    "256","210.00","337.01","201.00","44.35","47.91"
    "1024","978.00","898.26","115.00","41.05","0.26"
    "1518","1472.00","931.76","79.00","40.01","2.10"

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
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Write EXT4 CPU Load (%)","am62axx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","91.70","1.48","172.00","1.54"
    "4m","97.50","1.07","171.00","1.38"
    "4k","64.00","21.81","93.00","22.36"
    "256k","92.20","1.68","171.00","2.20"

EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Write Raw CPU Load (%)","am62axx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Read Raw CPU Load (%)"

    "1m","91.00","1.42","174.00","1.83"
    "4m","97.60","1.02","174.00","1.35"
    "4k","64.10","16.11","92.70","20.72"
    "256k","90.90","1.77","173.00","2.43"

EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Write EXT4 CPU Load (%)","am62axx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","82.79 (min 80.86, max 84.20)","5.89 (min 5.33, max 7.53)","178.87","8.62"
    "262144","79.25 (min 56.62, max 88.47)","5.91 (min 3.91, max 8.43)","180.55","9.13"
    "524288","79.95 (min 57.79, max 88.21)","5.89 (min 3.99, max 8.38)","181.15","8.70"
    "1048576","74.08 (min 52.01, max 88.83)","5.40 (min 3.35, max 8.03)","181.22","8.26"
    "5242880","75.34 (min 53.85, max 87.76)","5.38 (min 3.47, max 8.02)","181.47","9.48"

EMMC VFAT
^^^^^^^^^

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62axx_sk-fs: Write VFAT CPU Load (%)","am62axx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62axx_sk-fs: Read VFAT CPU Load (%)"

    "102400","28.13 (min 3.67, max 34.37)","3.45 (min 2.27, max 3.95)","171.77","10.20"
    "262144","43.39 (min 11.54, max 60.99)","5.67 (min 4.16, max 6.97)","175.90","9.70"
    "524288","41.35 (min 3.90, max 51.60)","4.24 (min 2.41, max 4.93)","171.23","9.35"
    "1048576","42.74 (min 3.97, max 53.26)","4.21 (min 2.26, max 4.84)","171.45","9.47"
    "5242880","42.69 (min 4.00, max 52.77)","3.86 (min 2.30, max 4.35)","171.53","9.02"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62axx_sk-fs: Write Throughput (Kbytes/sec)","am62axx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","59362.32","168907.22"
    "4000000","59850.23","172918.21"

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
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Write EXT4 CPU Load (%)","am62axx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.20","1.02","87.40","1.26"
    "4m","43.20","0.75","87.20","1.06"
    "4k","2.84","1.67","12.90","4.27"
    "256k","39.20","1.31","83.60","1.57"

MMC RAW FIO 1G
^^^^^^^^^^^^^^

.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Write Raw CPU Load (%)","am62axx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Read Raw CPU Load (%)"

    "1m","43.00","0.84","88.10","1.14"
    "4m","43.00","0.64","88.00","0.89"
    "4k","2.81","1.40","13.00","3.90"
    "256k","36.80","0.94","84.20","1.38"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Write Raw CPU Load (%)","am62axx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.40 (min 10.24, max 10.69)","0.83 (min 0.72, max 1.12)","10.80","0.67"
    "262144","10.37 (min 10.24, max 10.50)","0.91 (min 0.64, max 1.48)","10.99","0.79"
    "524288","10.47 (min 10.29, max 10.56)","0.81 (min 0.71, max 1.13)","11.05","0.66"
    "1048576","10.38 (min 10.26, max 10.59)","0.92 (min 0.76, max 1.19)","10.79","0.77"
    "5242880","10.79 (min 10.66, max 10.92)","0.83 (min 0.73, max 1.04)","12.03","0.75"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62axx_sk-fs: Write Throughput (Kbytes/sec)","am62axx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","38641.51","81920.00"
    "800000","45765.36","87148.94"
    "1000000","48046.92","90021.98"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

USB Driver
-------------------------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62axx_sk-fs: Throughput (MB/sec)"

    "150","43.80"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62axx_sk-fs: Throughput (MB/sec)"

    "150","36.10"

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62axx_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","22690.82"
    "aes-128-cbc","16","407.87"
    "aes-128-cbc","16384","83771.39"
    "aes-128-cbc","256","6693.03"
    "aes-128-cbc","64","1769.71"
    "aes-128-cbc","8192","70991.87"
    "aes-128-ecb","1024","23238.66"
    "aes-128-ecb","16","415.95"
    "aes-128-ecb","16384","87064.58"
    "aes-128-ecb","256","6831.70"
    "aes-128-ecb","64","1811.97"
    "aes-128-ecb","8192","72884.22"
    "aes-192-cbc","1024","22330.03"
    "aes-192-cbc","16","412.24"
    "aes-192-cbc","16384","76540.59"
    "aes-192-cbc","256","6668.46"
    "aes-192-cbc","64","1779.07"
    "aes-192-cbc","8192","65191.94"
    "aes-192-ecb","1024","22708.57"
    "aes-192-ecb","16","415.37"
    "aes-192-ecb","16384","78255.45"
    "aes-192-ecb","256","6798.68"
    "aes-192-ecb","64","1813.08"
    "aes-192-ecb","8192","67029.67"
    "aes-256-cbc","1024","21670.23"
    "aes-256-cbc","16","405.98"
    "aes-256-cbc","16384","70068.91"
    "aes-256-cbc","256","6556.16"
    "aes-256-cbc","64","1761.22"
    "aes-256-cbc","8192","60661.76"
    "aes-256-ecb","1024","22268.25"
    "aes-256-ecb","16","415.66"
    "aes-256-ecb","16384","71734.61"
    "aes-256-ecb","256","6744.66"
    "aes-256-ecb","64","1808.04"
    "aes-256-ecb","8192","60866.56"
    "sha256","1024","34747.73"
    "sha256","16","571.94"
    "sha256","16384","286829.23"
    "sha256","256","9044.22"
    "sha256","64","2270.38"
    "sha256","8192","193448.62"
    "sha512","1024","24330.24"
    "sha512","16","566.06"
    "sha512","16384","67687.77"
    "sha512","256","8116.39"
    "sha512","64","2266.01"
    "sha512","8192","60424.19"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62axx_sk-fs: CPU Load"

    "aes-128-cbc","30.00"
    "aes-128-ecb","32.00"
    "aes-192-cbc","30.00"
    "aes-192-ecb","31.00"
    "aes-256-cbc","30.00"
    "aes-256-ecb","30.00"
    "sha256","96.00"
    "sha512","96.00"

Listed for each algorithm are the code snippets used to run each benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

|

Low Power Performance
-------------------------

Power Performance
^^^^^^^^^^^^^^^^^

.. csv-table:: Deep Sleep Power Performance
    :header: "Rail name","Rail voltage(V)","Power (mW)"

    "vdd_core","0.85","19.16"
    "vddr_core","0.85","2.34"
    "soc_dvdd_3v3","3.30","4.63"
    "soc_dvdd_1v8","1.80","2.03"
    "vdda_1v8","1.80","11.22"
    "vdd_lpddr4","1.10","3.59"
    "Total"," ","42.96"

.. csv-table:: MCU Only Power Performance
    :header: "Rail name","Rail voltage(V)","Power (mW)"

    "vdd_core","0.85","199.73"
    "vddr_core","0.85","3.28"
    "soc_dvdd_3v3","3.30","10.49"
    "soc_dvdd_1v8","1.80","1.80"
    "vdda_1v8","1.80","19.42"
    "vdd_lpddr4","1.10","4.41"
    "Total"," ","239.14"

Partial I/O Data
- All voltage rails were measured to be near 0V

.. note::

   The measurements shown are from an AM62Ax rev E3. Results may vary based off of the board revision being used.

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)
