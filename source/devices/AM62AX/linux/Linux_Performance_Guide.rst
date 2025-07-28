
==============================
 Linux 11.01 Performance Guide
==============================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+-----------------------------------------------------------------------------+
| Name           | Description                                                                 |
+================+=============================================================================+
| AM62Ax SK      | AM62Ax Starter Kit with ARM running at 1.2GHz, DDR data rate 3733 MT/S      |
+----------------+-----------------------------------------------------------------------------+

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
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","29.30"
    "af_unix_socket_stream_bandwidth (MBs)","1181.09"
    "bw_file_rd-io-1mb (MB/s)","1468.70"
    "bw_file_rd-o2c-1mb (MB/s)","783.09"
    "bw_mem-bcopy-16mb (MB/s)","1958.38"
    "bw_mem-bcopy-1mb (MB/s)","2113.05"
    "bw_mem-bcopy-2mb (MB/s)","1673.36"
    "bw_mem-bcopy-4mb (MB/s)","1873.54"
    "bw_mem-bcopy-8mb (MB/s)","1920.77"
    "bw_mem-bzero-16mb (MB/s)","8167.43"
    "bw_mem-bzero-1mb (MB/s)","5139.27 (min 2113.05, max 8165.49)"
    "bw_mem-bzero-2mb (MB/s)","4916.87 (min 1673.36, max 8160.37)"
    "bw_mem-bzero-4mb (MB/s)","5019.92 (min 1873.54, max 8166.30)"
    "bw_mem-bzero-8mb (MB/s)","5038.55 (min 1920.77, max 8156.33)"
    "bw_mem-cp-16mb (MB/s)","977.82"
    "bw_mem-cp-1mb (MB/s)","4675.13 (min 949.97, max 8400.29)"
    "bw_mem-cp-2mb (MB/s)","4616.41 (min 960.92, max 8271.89)"
    "bw_mem-cp-4mb (MB/s)","4630.00 (min 1021.06, max 8238.93)"
    "bw_mem-cp-8mb (MB/s)","4605.23 (min 1017.94, max 8192.52)"
    "bw_mem-fcp-16mb (MB/s)","1834.02"
    "bw_mem-fcp-1mb (MB/s)","4965.20 (min 1764.91, max 8165.49)"
    "bw_mem-fcp-2mb (MB/s)","4892.01 (min 1623.64, max 8160.37)"
    "bw_mem-fcp-4mb (MB/s)","4979.48 (min 1792.65, max 8166.30)"
    "bw_mem-fcp-8mb (MB/s)","4981.61 (min 1806.89, max 8156.33)"
    "bw_mem-frd-16mb (MB/s)","1977.02"
    "bw_mem-frd-1mb (MB/s)","1970.20 (min 1764.91, max 2175.49)"
    "bw_mem-frd-2mb (MB/s)","1749.21 (min 1623.64, max 1874.77)"
    "bw_mem-frd-4mb (MB/s)","1877.04 (min 1792.65, max 1961.43)"
    "bw_mem-frd-8mb (MB/s)","1845.73 (min 1806.89, max 1884.57)"
    "bw_mem-fwr-16mb (MB/s)","8185.54"
    "bw_mem-fwr-1mb (MB/s)","5287.89 (min 2175.49, max 8400.29)"
    "bw_mem-fwr-2mb (MB/s)","5073.33 (min 1874.77, max 8271.89)"
    "bw_mem-fwr-4mb (MB/s)","5100.18 (min 1961.43, max 8238.93)"
    "bw_mem-fwr-8mb (MB/s)","5038.55 (min 1884.57, max 8192.52)"
    "bw_mem-rd-16mb (MB/s)","2032.78"
    "bw_mem-rd-1mb (MB/s)","2084.95 (min 1862.89, max 2307.01)"
    "bw_mem-rd-2mb (MB/s)","1838.45 (min 1662.79, max 2014.10)"
    "bw_mem-rd-4mb (MB/s)","1908.75 (min 1812.14, max 2005.35)"
    "bw_mem-rd-8mb (MB/s)","1978.03 (min 1930.73, max 2025.32)"
    "bw_mem-rdwr-16mb (MB/s)","1946.00"
    "bw_mem-rdwr-1mb (MB/s)","1384.57 (min 949.97, max 1819.17)"
    "bw_mem-rdwr-2mb (MB/s)","1275.50 (min 960.92, max 1590.08)"
    "bw_mem-rdwr-4mb (MB/s)","1414.28 (min 1021.06, max 1807.50)"
    "bw_mem-rdwr-8mb (MB/s)","1411.81 (min 1017.94, max 1805.67)"
    "bw_mem-wr-16mb (MB/s)","1964.40"
    "bw_mem-wr-1mb (MB/s)","1841.03 (min 1819.17, max 1862.89)"
    "bw_mem-wr-2mb (MB/s)","1626.44 (min 1590.08, max 1662.79)"
    "bw_mem-wr-4mb (MB/s)","1809.82 (min 1807.50, max 1812.14)"
    "bw_mem-wr-8mb (MB/s)","1868.20 (min 1805.67, max 1930.73)"
    "bw_mmap_rd-mo-1mb (MB/s)","2215.41"
    "bw_mmap_rd-o2c-1mb (MB/s)","805.02"
    "bw_pipe (MB/s)","781.46"
    "bw_unix (MB/s)","1181.09"
    "lat_connect (us)","57.16"
    "lat_ctx-2-128k (us)","7.74"
    "lat_ctx-2-256k (us)","6.46"
    "lat_ctx-4-128k (us)","7.22"
    "lat_ctx-4-256k (us)","6.73"
    "lat_fs-0k (num_files)","221.00"
    "lat_fs-10k (num_files)","132.00"
    "lat_fs-1k (num_files)","165.00"
    "lat_fs-4k (num_files)","159.00"
    "lat_mem_rd-stride128-sz1000k (ns)","29.69"
    "lat_mem_rd-stride128-sz125k (ns)","5.57"
    "lat_mem_rd-stride128-sz250k (ns)","5.85"
    "lat_mem_rd-stride128-sz31k (ns)","3.65"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","9.88"
    "lat_mem_rd-stride128-sz62k (ns)","5.24"
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
    "lat_ops-int-mul (ns)","3.13"
    "lat_ops-int64-add (ns)","0.72"
    "lat_ops-int64-bit (ns)","0.48"
    "lat_ops-int64-div (ns)","6.80"
    "lat_ops-int64-mod (ns)","5.25"
    "lat_ops-int64-mul (ns)","3.55"
    "lat_pagefault (us)","0.52"
    "lat_pipe (us)","25.07"
    "lat_proc-exec (us)","705.75"
    "lat_proc-fork (us)","606.67"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","34.07"
    "lat_sem (us)","2.89"
    "lat_sig-catch (us)","5.26"
    "lat_sig-install (us)","0.65"
    "lat_sig-prot (us)","0.55"
    "lat_syscall-fstat (us)","1.94"
    "lat_syscall-null (us)","0.46"
    "lat_syscall-open (us)","173.66"
    "lat_syscall-read (us)","0.79"
    "lat_syscall-stat (us)","4.80"
    "lat_syscall-write (us)","0.80"
    "lat_tcp (us)","0.92"
    "lat_unix (us)","29.30"
    "latency_for_0.50_mb_block_size (nanosec)","9.88"
    "latency_for_1.00_mb_block_size (nanosec)","14.84 (min 0.00, max 29.69)"
    "pipe_bandwidth (MBs)","781.46"
    "pipe_latency (microsec)","25.07"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","34.07"
    "semaphore_latency (microsec)","2.89"
    "signal_handler_latency (microsec)","0.65"
    "signal_handler_overhead (microsec)","5.26"
    "tcp_ip_connection_cost_to_localhost (microsec)","57.16"
    "tcp_latency_using_localhost (microsec)","0.92"


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
    :header: "Benchmarks","am62axx_sk-fs: perf"

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
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "whetstone (MIPS)","5000.00"


Linpack
^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "linpack (Kflops)","576111.00"


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
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "add (MB/s)","2762.80"
    "copy (MB/s)","4006.30"
    "scale (MB/s)","3668.00"
    "triad (MB/s)","2483.50"


CoreMarkPro
^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","41.84"
    "core (workloads/)","0.30"
    "coremark-pro ()","928.27"
    "linear_alg-mid-100x100-sp (workloads/)","14.68"
    "loops-all-mid-10k-sp (workloads/)","0.72"
    "nnet_test (workloads/)","1.09"
    "parser-125k (workloads/)","8.77"
    "radix2-big-64k (workloads/)","62.74"
    "sha-test (workloads/)","81.97"
    "zip-test (workloads/)","22.22"

 


.. csv-table:: CoreMarkProFourCore Benchmarks
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","161.29"
    "core (workloads/)","1.20"
    "coremark-pro ()","2640.23"
    "linear_alg-mid-100x100-sp (workloads/)","56.24"
    "loops-all-mid-10k-sp (workloads/)","2.08"
    "nnet_test (workloads/)","3.62"
    "parser-125k (workloads/)","9.64"
    "radix2-big-64k (workloads/)","105.41"
    "sha-test (workloads/)","270.27"
    "zip-test (workloads/)","78.43"
 


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
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "4m-check (workloads/)","431.85"
    "4m-check-reassembly (workloads/)","128.87"
    "4m-check-reassembly-tcp (workloads/)","60.98"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","34.56"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.91"
    "4m-cmykw2 (workloads/)","240.39"
    "4m-cmykw2-rotatew2 (workloads/)","51.37"
    "4m-reassembly (workloads/)","87.26"
    "4m-rotatew2 (workloads/)","54.82"
    "4m-tcp-mixed (workloads/)","120.30"
    "4m-x264w2 (workloads/)","1.99"
    "idct-4m (workloads/)","19.28"
    "idct-4mw1 (workloads/)","19.30"
    "ippktcheck-4m (workloads/)","430.96"
    "ippktcheck-4mw1 (workloads/)","433.05"
    "ipres-4m (workloads/)","117.83"
    "ipres-4mw1 (workloads/)","117.28"
    "md5-4m (workloads/)","27.73"
    "md5-4mw1 (workloads/)","28.19"
    "rgbcmyk-4m (workloads/)","65.83"
    "rgbcmyk-4mw1 (workloads/)","65.81"
    "rotate-4ms1 (workloads/)","24.22"
    "rotate-4ms1w1 (workloads/)","23.99"
    "rotate-4ms64 (workloads/)","24.28"
    "rotate-4ms64w1 (workloads/)","24.26"
    "x264-4mq (workloads/)","0.58"
    "x264-4mqw1 (workloads/)","0.58" 
 


Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62axx_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","13.86 (min 13.64, max 14.26)"


Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.
 

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

- CPSW3g: AM62ax


.. rubric::  TCP Bidirectional Throughput 
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1851.88","66.20"



.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1842.82","37.96"



.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62axx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: Packets Per Second (kPPS)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","54.10","106.00","40.04"
    "128","82.00","106.34","104.00","39.83"
    "256","210.00","212.30","104.00","39.79"
    "1024","978.00","111.40","14.00","2.05"
    "1518","1472.00","846.30","70.00","37.86"




.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62axx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: Packets Per Second (kPPS)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","3.23","6.00","3.73"
    "128","82.00","6.35","6.00","2.53"
    "256","210.00","14.13","7.00","3.19"
    "1024","978.00","60.62","7.00","1.87"
    "1518","1472.00","88.32","8.00","5.01"




.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62axx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: Packets Per Second (kPPS)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62axx_sk-fs: Packet Loss %"

    "64","","103.23","202.00","42.49","3.77"
    "128","82.00","205.09","200.00","43.21","12.79"
    "256","210.00","401.30","196.00","42.80","11.33"
    "1024","978.00","938.10","115.00","41.75","0.11"
    "1518","1472.00","914.07","78.00","39.12","1.28"



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
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Write EXT4 CPU Load (%)","am62axx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","92.00","1.50","172.00","1.70"
    "4m","97.20","1.01","172.00","1.37"
    "4k","64.50","21.97","93.50","22.69"
    "256k","91.50","1.94","171.00","2.59"


EMMC RAW FIO 1G
^^^^^^^^^^^^^^^


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Write Raw CPU Load (%)","am62axx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Read Raw CPU Load (%)"

    "1m","89.80","1.48","174.00","1.92"
    "4m","96.10","0.98","171.00","1.42"
    "4k","66.10","16.26","93.00","20.93"
    "256k","89.80","1.85","173.00","2.53"

 

EMMC EXT4
^^^^^^^^^


.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Write EXT4 CPU Load (%)","am62axx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","72.76 (min 71.16, max 74.04)","5.23 (min 4.52, max 7.31)","136.00","6.21"
    "262144","65.25 (min 50.09, max 75.10)","4.64 (min 3.11, max 6.97)","99.58","5.24"
    "524288","65.09 (min 45.89, max 76.00)","4.86 (min 2.74, max 7.03)","126.76","4.59"
    "1048576","63.43 (min 45.49, max 74.33)","4.40 (min 2.82, max 6.25)","99.03","4.06"
    "5242880","69.85 (min 54.99, max 75.34)","4.83 (min 3.28, max 6.55)","129.97","6.23"



EMMC EXT2
^^^^^^^^^
 


.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write EXT2 Throughput (Mbytes/sec)","am62axx_sk-fs: Write EXT2 CPU Load (%)","am62axx_sk-fs: Read EXT2 Throughput (Mbytes/sec)","am62axx_sk-fs: Read EXT2 CPU Load (%)"

    "102400","45.14 (min 22.15, max 51.21)","5.60 (min 4.57, max 7.49)","175.49","8.44"
    "262144","55.47 (min 25.15, max 63.60)","6.90 (min 6.20, max 9.01)","178.61","9.83"
    "524288","63.52 (min 26.02, max 75.42)","6.43 (min 5.05, max 10.78)","179.02","8.19"
    "1048576","66.24 (min 26.39, max 78.56)","7.11 (min 6.17, max 9.75)","178.90","8.15"
    "5242880","71.16 (min 26.94, max 85.42)","6.37 (min 5.05, max 10.23)","178.63","9.28"



EMMC VFAT
^^^^^^^^^



.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62axx_sk-fs: Write VFAT CPU Load (%)","am62axx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62axx_sk-fs: Read VFAT CPU Load (%)"

    "102400","28.06 (min 3.67, max 34.32)","3.55 (min 2.43, max 4.23)","171.91","10.61"
    "262144","42.05 (min 11.98, max 61.10)","5.60 (min 4.66, max 6.80)","176.48","9.75"
    "524288","41.14 (min 3.95, max 50.87)","4.24 (min 2.18, max 5.16)","171.76","9.02"
    "1048576","42.12 (min 3.94, max 51.80)","3.98 (min 2.57, max 4.57)","171.55","9.05"
    "5242880","42.98 (min 3.97, max 53.17)","3.97 (min 2.48, max 4.68)","171.75","9.02"


UBoot EMMC Driver
-----------------


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62axx_sk-fs: Write Throughput (Kbytes/sec)","am62axx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","98402.40","172463.16"
    "4000000","98996.98","175229.95"


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
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Write EXT4 CPU Load (%)","am62axx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.30","0.91","87.30","1.14"
    "4m","41.40","0.61","87.40","0.96"
    "4k","2.76","1.73","13.00","4.19"
    "256k","38.30","1.22","83.80","1.54"


MMC RAW FIO 1G
^^^^^^^^^^^^^^


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Write Raw CPU Load (%)","am62axx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Read Raw CPU Load (%)"

    "1m","43.20","0.87","88.20","1.08"
    "4m","43.00","0.63","88.10","0.85"
    "4k","2.80","1.48","13.00","3.95"
    "256k","37.80","0.91","84.20","1.40"

MMC EXT4
^^^^^^^^


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Write Raw CPU Load (%)","am62axx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.73 (min 10.66, max 10.77)","0.89 (min 0.77, max 1.14)","10.92","1.02"
    "262144","10.72 (min 10.64, max 10.78)","1.01 (min 0.77, max 1.50)","11.03","0.76"
    "524288","10.43 (min 10.38, max 10.54)","0.92 (min 0.72, max 1.28)","11.52","0.58"
    "1048576","10.44 (min 10.36, max 10.54)","0.92 (min 0.74, max 1.16)","11.52","0.69"
    "5242880","10.47 (min 10.40, max 10.59)","0.80 (min 0.65, max 1.06)","11.76","0.59"

MMC EXT3
^^^^^^^^


.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Write Raw CPU Load (%)","am62axx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Read Raw CPU Load (%)"

    "102400","39.55 (min 33.68, max 41.47)","3.50 (min 2.86, max 5.63)","79.36","4.00"
    "262144","39.89 (min 34.99, max 41.55)","3.50 (min 2.77, max 5.75)","86.78","5.17"
    "524288","40.19 (min 35.62, max 41.63)","3.39 (min 2.69, max 5.62)","86.91","4.97"
    "1048576","36.73 (min 33.18, max 37.85)","3.07 (min 2.35, max 5.23)","90.56","5.35"
    "5242880","39.59 (min 35.86, max 41.21)","3.24 (min 2.40, max 5.74)","83.78","5.36"

MMC EXT2
^^^^^^^^


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Write Raw CPU Load (%)","am62axx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62axx_sk-fs: Read Raw CPU Load (%)"

    "102400","17.30 (min 3.49, max 20.99)","2.52 (min 2.17, max 2.86)","76.74","5.79"
    "262144","30.41 (min 3.85, max 37.37)","3.07 (min 1.96, max 3.90)","86.86","4.58"
    "524288","34.32 (min 3.94, max 42.42)","3.21 (min 2.09, max 3.74)","90.32","6.01"
    "1048576","34.33 (min 4.01, max 42.07)","3.02 (min 2.19, max 3.50)","84.19","4.80"
    "5242880","33.20 (min 4.02, max 40.86)","2.65 (min 2.39, max 2.91)","85.73","4.51"
 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 


UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62axx_sk-fs: Write Throughput (Kbytes/sec)","am62axx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","23405.71","81920.00"
    "800000","43115.79","87148.94"
    "1000000","48188.24","89530.05"



The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 

|

USB Driver
----------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^


.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62axx_sk-fs: Throughput (MB/sec)"

    "150","24.80"



.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62axx_sk-fs: Throughput (MB/sec)"

    "150","22.40"


|

CRYPTO Driver
-------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62axx_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","22460.07"
    "aes-128-cbc","16","404.44"
    "aes-128-cbc","16384","84290.22"
    "aes-128-cbc","256","6593.79"
    "aes-128-cbc","64","1757.46"
    "aes-128-cbc","8192","70806.19"
    "aes-128-ecb","1024","23219.54"
    "aes-128-ecb","16","415.56"
    "aes-128-ecb","16384","85759.32"
    "aes-128-ecb","256","6803.03"
    "aes-128-ecb","64","1805.29"
    "aes-128-ecb","8192","72764.07"
    "aes-192-cbc","1024","22142.98"
    "aes-192-cbc","16","405.20"
    "aes-192-cbc","16384","76726.27"
    "aes-192-cbc","256","6573.48"
    "aes-192-cbc","64","1758.04"
    "aes-192-cbc","8192","65301.16"
    "aes-192-ecb","1024","22728.36"
    "aes-192-ecb","16","412.53"
    "aes-192-ecb","16384","78222.68"
    "aes-192-ecb","256","6736.21"
    "aes-192-ecb","64","1797.67"
    "aes-192-ecb","8192","66418.01"
    "aes-256-cbc","1024","21632.34"
    "aes-256-cbc","16","402.21"
    "aes-256-cbc","16384","69888.68"
    "aes-256-cbc","256","6485.67"
    "aes-256-cbc","64","1728.77"
    "aes-256-cbc","8192","60334.08"
    "aes-256-ecb","1024","22175.06"
    "aes-256-ecb","16","414.45"
    "aes-256-ecb","16384","71800.15"
    "aes-256-ecb","256","6675.29"
    "aes-256-ecb","64","1792.19"
    "aes-256-ecb","8192","61904.21"
    "sha256","1024","36802.22"
    "sha256","16","613.02"
    "sha256","16384","296162.65"
    "sha256","256","9669.46"
    "sha256","64","2449.56"
    "sha256","8192","200488.28"
    "sha512","1024","26210.99"
    "sha512","16","614.23"
    "sha512","16384","68452.35"
    "sha512","256","8776.36"
    "sha512","64","2468.99"
    "sha512","8192","61546.50"



.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62axx_sk-fs: CPU Load"

    "aes-128-cbc","31.00"
    "aes-128-ecb","32.00"
    "aes-192-cbc","31.00"
    "aes-192-ecb","31.00"
    "aes-256-cbc","31.00"
    "aes-256-ecb","31.00"
    "sha256","96.00"
    "sha512","96.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc


Low Power Performance
---------------------

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

Resume Latency Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: LPM Resume Latency Performance
   :header: "Low Power Mode","Total Resume Latency (ms)"

   "Deep Sleep", "146.45"
   "MCU Only", "110.40"

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
