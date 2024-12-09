
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

    "af_unix_sock_stream_latency (microsec)","26.81"
    "af_unix_socket_stream_bandwidth (MBs)","1190.21"
    "bw_file_rd-io-1mb (MB/s)","1283.23"
    "bw_file_rd-o2c-1mb (MB/s)","729.93"
    "bw_mem-bcopy-16mb (MB/s)","1832.13"
    "bw_mem-bcopy-1mb (MB/s)","1941.75"
    "bw_mem-bcopy-2mb (MB/s)","1719.10"
    "bw_mem-bcopy-4mb (MB/s)","1632.65"
    "bw_mem-bcopy-8mb (MB/s)","1822.53"
    "bw_mem-bzero-16mb (MB/s)","7901.23"
    "bw_mem-bzero-1mb (MB/s)","4929.85 (min 1941.75, max 7917.94)"
    "bw_mem-bzero-2mb (MB/s)","4792.34 (min 1719.10, max 7865.57)"
    "bw_mem-bzero-4mb (MB/s)","4768.90 (min 1632.65, max 7905.14)"
    "bw_mem-bzero-8mb (MB/s)","4858.64 (min 1822.53, max 7894.74)"
    "bw_mem-cp-16mb (MB/s)","920.97"
    "bw_mem-cp-1mb (MB/s)","4536.64 (min 922.68, max 8150.59)"
    "bw_mem-cp-2mb (MB/s)","4463.19 (min 924.93, max 8001.45)"
    "bw_mem-cp-4mb (MB/s)","4444.81 (min 935.89, max 7953.72)"
    "bw_mem-cp-8mb (MB/s)","4451.94 (min 962.12, max 7941.76)"
    "bw_mem-fcp-16mb (MB/s)","1648.46"
    "bw_mem-fcp-1mb (MB/s)","4836.17 (min 1754.39, max 7917.94)"
    "bw_mem-fcp-2mb (MB/s)","4722.80 (min 1580.03, max 7865.57)"
    "bw_mem-fcp-4mb (MB/s)","4790.91 (min 1676.68, max 7905.14)"
    "bw_mem-fcp-8mb (MB/s)","4785.51 (min 1676.27, max 7894.74)"
    "bw_mem-frd-16mb (MB/s)","1886.35"
    "bw_mem-frd-1mb (MB/s)","1882.31 (min 1754.39, max 2010.23)"
    "bw_mem-frd-2mb (MB/s)","1641.81 (min 1580.03, max 1703.58)"
    "bw_mem-frd-4mb (MB/s)","1664.45 (min 1652.21, max 1676.68)"
    "bw_mem-frd-8mb (MB/s)","1780.42 (min 1676.27, max 1884.57)"
    "bw_mem-fwr-16mb (MB/s)","7944.39"
    "bw_mem-fwr-1mb (MB/s)","5080.41 (min 2010.23, max 8150.59)"
    "bw_mem-fwr-2mb (MB/s)","4852.52 (min 1703.58, max 8001.45)"
    "bw_mem-fwr-4mb (MB/s)","4802.97 (min 1652.21, max 7953.72)"
    "bw_mem-fwr-8mb (MB/s)","4913.17 (min 1884.57, max 7941.76)"
    "bw_mem-rd-16mb (MB/s)","1935.64"
    "bw_mem-rd-1mb (MB/s)","1939.10 (min 1680.39, max 2197.80)"
    "bw_mem-rd-2mb (MB/s)","1768.02 (min 1633.99, max 1902.04)"
    "bw_mem-rd-4mb (MB/s)","1818.85 (min 1722.90, max 1914.79)"
    "bw_mem-rd-8mb (MB/s)","1845.93 (min 1772.46, max 1919.39)"
    "bw_mem-rdwr-16mb (MB/s)","1814.26"
    "bw_mem-rdwr-1mb (MB/s)","1313.13 (min 922.68, max 1703.58)"
    "bw_mem-rdwr-2mb (MB/s)","1270.22 (min 924.93, max 1615.51)"
    "bw_mem-rdwr-4mb (MB/s)","1302.32 (min 935.89, max 1668.75)"
    "bw_mem-rdwr-8mb (MB/s)","1361.54 (min 962.12, max 1760.95)"
    "bw_mem-wr-16mb (MB/s)","1822.32"
    "bw_mem-wr-1mb (MB/s)","1691.99 (min 1680.39, max 1703.58)"
    "bw_mem-wr-2mb (MB/s)","1624.75 (min 1615.51, max 1633.99)"
    "bw_mem-wr-4mb (MB/s)","1695.83 (min 1668.75, max 1722.90)"
    "bw_mem-wr-8mb (MB/s)","1766.71 (min 1760.95, max 1772.46)"
    "bw_mmap_rd-mo-1mb (MB/s)","2134.85"
    "bw_mmap_rd-o2c-1mb (MB/s)","680.04"
    "bw_pipe (MB/s)","805.00"
    "bw_unix (MB/s)","1190.21"
    "lat_connect (us)","56.95"
    "lat_ctx-2-128k (us)","5.99"
    "lat_ctx-2-256k (us)","6.45"
    "lat_ctx-4-128k (us)","5.85"
    "lat_ctx-4-256k (us)","4.51"
    "lat_fs-0k (num_files)","248.00"
    "lat_fs-10k (num_files)","125.00"
    "lat_fs-1k (num_files)","172.00"
    "lat_fs-4k (num_files)","144.00"
    "lat_mem_rd-stride128-sz1000k (ns)","30.75"
    "lat_mem_rd-stride128-sz125k (ns)","5.53"
    "lat_mem_rd-stride128-sz250k (ns)","5.83"
    "lat_mem_rd-stride128-sz31k (ns)","3.65"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","11.61"
    "lat_mem_rd-stride128-sz62k (ns)","5.26"
    "lat_mmap-1m (us)","58.00"
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
    "lat_pagefault (us)","1.36"
    "lat_pipe (us)","23.35"
    "lat_proc-exec (us)","842.71"
    "lat_proc-fork (us)","651.13"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","35.07"
    "lat_sem (us)","2.15"
    "lat_sig-catch (us)","5.77"
    "lat_sig-install (us)","0.66"
    "lat_sig-prot (us)","1.21"
    "lat_syscall-fstat (us)","2.00"
    "lat_syscall-null (us)","0.46"
    "lat_syscall-open (us)","169.97"
    "lat_syscall-read (us)","0.83"
    "lat_syscall-stat (us)","4.97"
    "lat_syscall-write (us)","0.74"
    "lat_tcp (us)","0.94"
    "lat_unix (us)","26.81"
    "latency_for_0.50_mb_block_size (nanosec)","11.61"
    "latency_for_1.00_mb_block_size (nanosec)","15.38 (min 0.00, max 30.75)"
    "pipe_bandwidth (MBs)","805.00"
    "pipe_latency (microsec)","23.35"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","35.07"
    "semaphore_latency (microsec)","2.15"
    "signal_handler_latency (microsec)","0.66"
    "signal_handler_overhead (microsec)","5.77"
    "tcp_ip_connection_cost_to_localhost (microsec)","56.95"
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

    "linpack (Kflops)","578294.00"

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

    "add (MB/s)","2609.30"
    "copy (MB/s)","3771.70"
    "scale (MB/s)","3491.20"
    "triad (MB/s)","2399.70"

CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","42.19"
    "core (workloads/)","0.30"
    "coremark-pro ()","938.54"
    "linear_alg-mid-100x100-sp (workloads/)","14.68"
    "loops-all-mid-10k-sp (workloads/)","0.71"
    "nnet_test (workloads/)","1.09"
    "parser-125k (workloads/)","8.85"
    "radix2-big-64k (workloads/)","69.60"
    "sha-test (workloads/)","81.30"
    "zip-test (workloads/)","22.22"

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

    "4m-check (workloads/)","426.04"
    "4m-check-reassembly (workloads/)","124.69"
    "4m-check-reassembly-tcp (workloads/)","60.10"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","33.69"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.93"
    "4m-cmykw2 (workloads/)","246.31"
    "4m-cmykw2-rotatew2 (workloads/)","50.51"
    "4m-reassembly (workloads/)","83.47"
    "4m-rotatew2 (workloads/)","54.73"
    "4m-tcp-mixed (workloads/)","119.40"
    "4m-x264w2 (workloads/)","1.98"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","19.27"
    "idct-4mw1 (workloads/)","19.27"
    "ippktcheck-4m (workloads/)","424.45"
    "ippktcheck-4mw1 (workloads/)","424.09"
    "ipres-4m (workloads/)","112.87"
    "ipres-4mw1 (workloads/)","113.46"
    "md5-4m (workloads/)","29.29"
    "md5-4mw1 (workloads/)","29.03"
    "rgbcmyk-4m (workloads/)","65.75"
    "rgbcmyk-4mw1 (workloads/)","65.77"
    "rotate-4ms1 (workloads/)","23.66"
    "rotate-4ms1w1 (workloads/)","23.67"
    "rotate-4ms64 (workloads/)","23.92"
    "rotate-4ms64w1 (workloads/)","25.60"
    "x264-4mq (workloads/)","0.58"
    "x264-4mqw1 (workloads/)","0.58"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62axx_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","16.57 (min 15.67, max 17.24)"

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

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1856.34","63.35"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1877.64","36.58"

.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62axx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: Packets Per Second (kPPS)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","16.42","114.00","40.70"
    "128","82.00","73.46","112.00","40.31"
    "256","210.00","186.80","111.00","40.33"
    "1024","978.00","839.17","107.00","40.21"
    "1518","1472.00","955.68","81.00","33.86"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62axx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: Packets Per Second (kPPS)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","1.02","7.00","2.44"
    "128","82.00","4.85","7.00","5.70"
    "256","210.00","12.89","8.00","1.48"
    "1024","978.00","65.72","8.00","3.86"
    "1518","1472.00","98.92","8.00","5.28"

.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62axx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: Packets Per Second (kPPS)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62axx_sk-fs: Packet Loss %"

    "64","18.00","32.83","228.00","41.27","43.93"
    "128","82.00","98.72","150.00","40.41","0.28"
    "256","210.00","337.70","201.00","42.58","46.54"
    "1024","978.00","933.59","119.00","42.42","0.21"
    "1518","1472.00","947.84","80.00","41.41","0.15"

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

    "1m","90.40","1.46","172.00","1.86"
    "4m","95.90","1.14","172.00","1.42"
    "4k","63.80","20.08","94.20","23.04"
    "256k","90.10","1.67","171.00","2.39"

EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Write EXT4 CPU Load (%)","am62axx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","84.31 (min 81.57, max 85.86)","6.26 (min 5.61, max 8.19)","179.01","8.19"
    "262144","80.39 (min 53.59, max 90.44)","6.08 (min 3.70, max 8.56)","179.87","9.52"
    "524288","72.34 (min 49.21, max 89.48)","5.31 (min 3.06, max 8.43)","180.99","9.48"
    "1048576","72.06 (min 47.11, max 89.92)","5.19 (min 2.92, max 7.94)","181.20","8.66"
    "5242880","79.37 (min 55.35, max 88.16)","5.97 (min 4.47, max 8.33)","181.25","9.48"

EMMC VFAT
^^^^^^^^^

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62axx_sk-fs: Write VFAT CPU Load (%)","am62axx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62axx_sk-fs: Read VFAT CPU Load (%)"

    "102400","51.02 (min 45.02, max 52.67)","5.10 (min 4.15, max 7.76)","172.99","10.20"
    "262144","52.91 (min 45.76, max 54.80)","5.17 (min 4.32, max 7.96)","171.43","10.33"
    "524288","53.43 (min 46.13, max 55.33)","5.31 (min 4.35, max 8.23)","170.89","9.43"
    "1048576","53.11 (min 45.89, max 55.06)","5.06 (min 4.20, max 7.88)","170.78","10.84"
    "5242880","53.39 (min 45.78, max 55.49)","5.21 (min 4.35, max 7.89)","171.34","9.05"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62axx_sk-fs: Write Throughput (Kbytes/sec)","am62axx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","96376.47","171560.21"
    "4000000","98996.98","175229.95"

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

    "1m","41.20","1.00","85.50","1.27"
    "4m","40.90","0.68","84.20","1.07"
    "4k","2.81","1.45","13.00","4.13"
    "256k","38.20","1.17","84.40","1.51"

MMC RAW FIO 1G
^^^^^^^^^^^^^^

.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Write Raw CPU Load (%)","am62axx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Read Raw CPU Load (%)"

    "1m","44.80","1.00","88.30","1.27"
    "4m","44.60","0.74","88.30","0.85"
    "4k","4.16","1.36","17.00","5.00"
    "256k","42.90","1.07","86.30","1.40"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Write Raw CPU Load (%)","am62axx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.54 (min 10.31, max 10.94)","0.86 (min 0.72, max 1.21)","10.84","0.65"
    "262144","10.25 (min 10.03, max 10.50)","0.89 (min 0.69, max 1.37)","10.96","0.84"
    "524288","10.29 (min 10.19, max 10.42)","0.83 (min 0.63, max 1.20)","11.02","0.63"
    "1048576","10.31 (min 10.18, max 10.39)","0.89 (min 0.76, max 1.16)","12.01","0.72"
    "5242880","11.04 (min 10.91, max 11.11)","0.87 (min 0.72, max 1.20)","12.02","0.63"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62axx_sk-fs: Write Throughput (Kbytes/sec)","am62axx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","39009.52","50567.90"
    "800000","45765.36","65536.00"
    "1000000","46678.06","76560.75"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

USB Driver
-------------------------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62axx_sk-fs: Throughput (MB/sec)"

    "150","44.50"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62axx_sk-fs: Throughput (MB/sec)"

    "150","38.70"

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62axx_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","24957.27"
    "aes-128-cbc","16","455.88"
    "aes-128-cbc","16384","86857.05"
    "aes-128-cbc","256","7483.90"
    "aes-128-cbc","64","1996.46"
    "aes-128-cbc","8192","73760.77"
    "aes-128-ecb","1024","25503.40"
    "aes-128-ecb","16","465.99"
    "aes-128-ecb","16384","89822.55"
    "aes-128-ecb","256","7670.44"
    "aes-128-ecb","64","2051.39"
    "aes-128-ecb","8192","76229.29"
    "aes-192-cbc","1024","24464.38"
    "aes-192-cbc","16","457.74"
    "aes-192-cbc","16384","78528.51"
    "aes-192-cbc","256","7427.24"
    "aes-192-cbc","64","1993.73"
    "aes-192-cbc","8192","67876.18"
    "aes-192-ecb","1024","25041.24"
    "aes-192-ecb","16","464.68"
    "aes-192-ecb","16384","80909.65"
    "aes-192-ecb","256","7619.07"
    "aes-192-ecb","64","2042.90"
    "aes-192-ecb","8192","69348.01"
    "aes-256-cbc","1024","23916.20"
    "aes-256-cbc","16","455.50"
    "aes-256-cbc","16384","71647.23"
    "aes-256-cbc","256","7336.79"
    "aes-256-cbc","64","1995.58"
    "aes-256-cbc","8192","62608.73"
    "aes-256-ecb","1024","24311.81"
    "aes-256-ecb","16","467.63"
    "aes-256-ecb","16384","73449.47"
    "aes-256-ecb","256","7513.60"
    "aes-256-ecb","64","2043.61"
    "aes-256-ecb","8192","64208.90"
    "sha256","1024","32988.84"
    "sha256","16","554.30"
    "sha256","16384","273929.56"
    "sha256","256","8643.50"
    "sha256","64","2191.15"
    "sha256","8192","183552.68"
    "sha512","1024","23909.72"
    "sha512","16","539.73"
    "sha512","16384","67605.85"
    "sha512","256","7746.73"
    "sha512","64","2160.13"
    "sha512","8192","60159.32"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62axx_sk-fs: CPU Load"

    "aes-128-cbc","34.00"
    "aes-128-ecb","35.00"
    "aes-192-cbc","33.00"
    "aes-192-ecb","34.00"
    "aes-256-cbc","33.00"
    "aes-256-ecb","33.00"
    "sha256","98.00"
    "sha512","98.00"

Listed for each algorithm are the code snippets used to run each benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

|

Low Power Performance
-------------------------

Table:  **Deep sleep**

.. csv-table::
    :header: "Rail name","Rail voltage(V)","Power (mW)"

    "vdd_core","0.85","16.82"
    "vddr_core","0.85","1.96"
    "soc_dvdd_3v3","3.30","4.63"
    "soc_dvdd_1v8","1.80","1.44"
    "vdda_1v8","1.80","10.72"
    "vdd_lpddr4/vdd_ddr4","1.10","6.07"
    "Total"," ","41.64"

Table:  **MCU only**

.. csv-table::
    :header: "Rail name","Rail voltage(V)","Power (mW)"

    "vdd_core","0.85","112.87"
    "vddr_core","0.85","1.49"
    "soc_dvdd_3v3","3.30","9.58"
    "soc_dvdd_1v8","1.80","1.71"
    "vdda_1v8","1.80","19.37"
    "vdd_lpddr4/vdd_ddr4","1.10","5.79"
    "Total"," ","150.82"

Partial I/O Data
- All voltage rails were measured to be near 0V

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)
