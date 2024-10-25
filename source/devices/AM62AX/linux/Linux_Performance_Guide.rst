
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
    :header: "Benchmarks","am62axx_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","25.30"
    "af_unix_socket_stream_bandwidth (MBs)","1212.25"
    "bw_file_rd-io-1mb (MB/s)","1263.54"
    "bw_file_rd-o2c-1mb (MB/s)","734.35"
    "bw_mem-bcopy-16mb (MB/s)","1827.11"
    "bw_mem-bcopy-1mb (MB/s)","1975.11"
    "bw_mem-bcopy-2mb (MB/s)","1761.80"
    "bw_mem-bcopy-4mb (MB/s)","1790.78"
    "bw_mem-bcopy-8mb (MB/s)","1798.76"
    "bw_mem-bzero-16mb (MB/s)","7779.58"
    "bw_mem-bzero-1mb (MB/s)","4864.92 (min 1975.11, max 7754.73)"
    "bw_mem-bzero-2mb (MB/s)","4753.46 (min 1761.80, max 7745.12)"
    "bw_mem-bzero-4mb (MB/s)","4773.62 (min 1790.78, max 7756.45)"
    "bw_mem-bzero-8mb (MB/s)","4784.76 (min 1798.76, max 7770.76)"
    "bw_mem-cp-16mb (MB/s)","913.03"
    "bw_mem-cp-1mb (MB/s)","4467.69 (min 904.00, max 8031.38)"
    "bw_mem-cp-2mb (MB/s)","4405.03 (min 887.84, max 7922.22)"
    "bw_mem-cp-4mb (MB/s)","4386.41 (min 936.66, max 7836.15)"
    "bw_mem-cp-8mb (MB/s)","4391.31 (min 965.02, max 7817.59)"
    "bw_mem-fcp-16mb (MB/s)","1714.71"
    "bw_mem-fcp-1mb (MB/s)","4750.48 (min 1746.22, max 7754.73)"
    "bw_mem-fcp-2mb (MB/s)","4710.08 (min 1675.04, max 7745.12)"
    "bw_mem-fcp-4mb (MB/s)","4725.92 (min 1695.39, max 7756.45)"
    "bw_mem-fcp-8mb (MB/s)","4728.02 (min 1685.27, max 7770.76)"
    "bw_mem-frd-16mb (MB/s)","1886.79"
    "bw_mem-frd-1mb (MB/s)","1837.12 (min 1746.22, max 1928.02)"
    "bw_mem-frd-2mb (MB/s)","1690.33 (min 1675.04, max 1705.61)"
    "bw_mem-frd-4mb (MB/s)","1766.25 (min 1695.39, max 1837.11)"
    "bw_mem-frd-8mb (MB/s)","1753.49 (min 1685.27, max 1821.70)"
    "bw_mem-fwr-16mb (MB/s)","7792.21"
    "bw_mem-fwr-1mb (MB/s)","4979.70 (min 1928.02, max 8031.38)"
    "bw_mem-fwr-2mb (MB/s)","4813.92 (min 1705.61, max 7922.22)"
    "bw_mem-fwr-4mb (MB/s)","4836.63 (min 1837.11, max 7836.15)"
    "bw_mem-fwr-8mb (MB/s)","4819.65 (min 1821.70, max 7817.59)"
    "bw_mem-rd-16mb (MB/s)","1937.98"
    "bw_mem-rd-1mb (MB/s)","1927.74 (min 1688.62, max 2166.85)"
    "bw_mem-rd-2mb (MB/s)","1784.64 (min 1645.28, max 1924.00)"
    "bw_mem-rd-4mb (MB/s)","1782.14 (min 1649.48, max 1914.79)"
    "bw_mem-rd-8mb (MB/s)","1857.86 (min 1784.52, max 1931.20)"
    "bw_mem-rdwr-16mb (MB/s)","1833.39"
    "bw_mem-rdwr-1mb (MB/s)","1282.41 (min 904.00, max 1660.82)"
    "bw_mem-rdwr-2mb (MB/s)","1164.38 (min 887.84, max 1440.92)"
    "bw_mem-rdwr-4mb (MB/s)","1338.91 (min 936.66, max 1741.15)"
    "bw_mem-rdwr-8mb (MB/s)","1371.30 (min 965.02, max 1777.58)"
    "bw_mem-wr-16mb (MB/s)","1828.99"
    "bw_mem-wr-1mb (MB/s)","1674.72 (min 1660.82, max 1688.62)"
    "bw_mem-wr-2mb (MB/s)","1543.10 (min 1440.92, max 1645.28)"
    "bw_mem-wr-4mb (MB/s)","1695.32 (min 1649.48, max 1741.15)"
    "bw_mem-wr-8mb (MB/s)","1781.05 (min 1777.58, max 1784.52)"
    "bw_mmap_rd-mo-1mb (MB/s)","2180.23"
    "bw_mmap_rd-o2c-1mb (MB/s)","661.05"
    "bw_pipe (MB/s)","793.38"
    "bw_unix (MB/s)","1212.25"
    "lat_connect (us)","51.39"
    "lat_ctx-2-128k (us)","6.19"
    "lat_ctx-2-256k (us)","5.93"
    "lat_ctx-4-128k (us)","5.69"
    "lat_ctx-4-256k (us)","4.47"
    "lat_fs-0k (num_files)","306.00"
    "lat_fs-10k (num_files)","120.00"
    "lat_fs-1k (num_files)","192.00"
    "lat_fs-4k (num_files)","202.00"
    "lat_mem_rd-stride128-sz1000k (ns)","30.96"
    "lat_mem_rd-stride128-sz125k (ns)","5.56"
    "lat_mem_rd-stride128-sz250k (ns)","5.82"
    "lat_mem_rd-stride128-sz31k (ns)","2.16"
    "lat_mem_rd-stride128-sz50 (ns)","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","10.73"
    "lat_mem_rd-stride128-sz62k (ns)","5.23"
    "lat_mmap-1m (us)","53.00"
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
    "lat_pagefault (us)","1.33"
    "lat_pipe (us)","21.95"
    "lat_proc-exec (us)","803.86"
    "lat_proc-fork (us)","612.60"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","35.75"
    "lat_sem (us)","1.55"
    "lat_sig-catch (us)","5.31"
    "lat_sig-install (us)","0.65"
    "lat_sig-prot (us)","0.97"
    "lat_syscall-fstat (us)","1.64"
    "lat_syscall-null (us)","0.46"
    "lat_syscall-open (us)","276.05"
    "lat_syscall-read (us)","0.77"
    "lat_syscall-stat (us)","4.09"
    "lat_syscall-write (us)","0.69"
    "lat_tcp (us)","0.94"
    "lat_unix (us)","25.30"
    "latency_for_0.50_mb_block_size (nanosec)","10.73"
    "latency_for_1.00_mb_block_size (nanosec)","15.48 (min 0.00, max 30.96)"
    "pipe_bandwidth (MBs)","793.38"
    "pipe_latency (microsec)","21.95"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","35.75"
    "semaphore_latency (microsec)","1.55"
    "signal_handler_latency (microsec)","0.65"
    "signal_handler_overhead (microsec)","5.31"
    "tcp_ip_connection_cost_to_localhost (microsec)","51.39"
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

    "linpack (Kflops)","573944.00"






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

    "add (MB/s)","2826.80"
    "copy (MB/s)","3967.20"
    "scale (MB/s)","3770.40"
    "triad (MB/s)","2564.10"




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
    "coremark-pro ()","932.87"
    "linear_alg-mid-100x100-sp (workloads/)","14.68"
    "loops-all-mid-10k-sp (workloads/)","0.72"
    "nnet_test (workloads/)","1.09"
    "parser-125k (workloads/)","8.93"
    "radix2-big-64k (workloads/)","64.41"
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

    "4m-check (workloads/)","426.69"
    "4m-check-reassembly (workloads/)","122.25"
    "4m-check-reassembly-tcp (workloads/)","60.10"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","33.59"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.92"
    "4m-cmykw2 (workloads/)","251.26"
    "4m-cmykw2-rotatew2 (workloads/)","50.59"
    "4m-reassembly (workloads/)","83.19"
    "4m-rotatew2 (workloads/)","54.73"
    "4m-tcp-mixed (workloads/)","119.40"
    "4m-x264w2 (workloads/)","1.98"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","19.28"
    "idct-4mw1 (workloads/)","19.29"
    "ippktcheck-4m (workloads/)","426.19"
    "ippktcheck-4mw1 (workloads/)","426.26"
    "ipres-4m (workloads/)","113.04"
    "ipres-4mw1 (workloads/)","112.44"
    "md5-4m (workloads/)","29.39"
    "md5-4mw1 (workloads/)","29.12"
    "rgbcmyk-4m (workloads/)","65.72"
    "rgbcmyk-4mw1 (workloads/)","65.83"
    "rotate-4ms1 (workloads/)","23.76"
    "rotate-4ms1w1 (workloads/)","23.74"
    "rotate-4ms64 (workloads/)","24.10"
    "rotate-4ms64w1 (workloads/)","24.07"
    "x264-4mq (workloads/)","0.58"
    "x264-4mqw1 (workloads/)","0.58"



 
 



|

Boot-time Measurement
-------------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Boot time MMCSD
    :header: "Boot Configuration","am62axx_sk-fs: boot time (sec)"

    "Kernel boot time test when init is /bin/sh and bootloader, kernel and sdk-rootfs are in mmc-sd","4.25 (min 4.22, max 4.28)"



 
 

 



 

 

 

 



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

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1856.93","66.28"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62axx_sk-fs: THROUGHPUT (Mbits/sec)","am62axx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1792.48","31.15"







 
 

 

 
 

 

 

 

 

 

 

 

 



|

EMMC Driver
-------------------------

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

 

 

 

 

 


 

 


AM62AXX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Write EXT4 CPU Load (%)","am62axx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","58.70","1.05","175.00","1.76"
    "4m","58.20","0.85","175.00","1.49"
    "4k","50.90","14.84","56.50","14.33"
    "256k","58.60","1.42","174.00","2.18"





 
 

 











 
 



|

UBoot EMMC Driver
-------------------------

 


AM62AXX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62axx_sk-fs: Write Throughput (Kbytes/sec)","am62axx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","61593.98","170666.67"
    "4000000","62296.58","173835.54"




























 
 

 



|

MMC/SD Driver
-------------------------

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

 

 

 

 

 





 

 


AM62AXX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62axx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Write EXT4 CPU Load (%)","am62axx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62axx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","14.40","0.59","25.30","0.60"
    "4m","14.30","0.48","24.40","0.53"
    "4k","4.07","2.22","10.40","3.41"
    "256k","14.70","0.60","24.90","0.65"







 

 

 

 

 

 

 

 















 

 

 





 

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option
 



|

UBoot MMC/SD Driver
-------------------------

  


AM62AXX-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62axx_sk-fs: Write Throughput (Kbytes/sec)","am62axx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","13044.59","47627.91"
    "800000","21389.03","63015.38"
    "1000000","18724.57","74812.79"


































 
 

 



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62axx_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","25424.21"
    "aes-128-cbc","16","463.89"
    "aes-128-cbc","16384","87184.73"
    "aes-128-cbc","256","7661.74"
    "aes-128-cbc","64","2040.15"
    "aes-128-cbc","8192","74315.09"
    "aes-128-ecb","1024","25885.35"
    "aes-128-ecb","16","472.89"
    "aes-128-ecb","16384","89828.01"
    "aes-128-ecb","256","7816.53"
    "aes-128-ecb","64","2083.58"
    "aes-128-ecb","8192","76647.08"
    "aes-192-cbc","1024","24936.11"
    "aes-192-cbc","16","464.92"
    "aes-192-cbc","16384","78888.96"
    "aes-192-cbc","256","7620.95"
    "aes-192-cbc","64","2044.27"
    "aes-192-cbc","8192","68247.55"
    "aes-192-ecb","1024","25520.81"
    "aes-192-ecb","16","479.59"
    "aes-192-ecb","16384","81073.49"
    "aes-192-ecb","256","7835.48"
    "aes-192-ecb","64","2096.21"
    "aes-192-ecb","8192","70309.21"
    "aes-256-cbc","1024","24279.72"
    "aes-256-cbc","16","465.84"
    "aes-256-cbc","16384","71756.46"
    "aes-256-cbc","256","7542.10"
    "aes-256-cbc","64","2029.14"
    "aes-256-cbc","8192","63048.36"
    "aes-256-ecb","1024","24907.78"
    "aes-256-ecb","16","474.14"
    "aes-256-ecb","16384","73657.00"
    "aes-256-ecb","256","7709.53"
    "aes-256-ecb","64","2083.50"
    "aes-256-ecb","8192","64965.29"
    "sha256","1024","34098.52"
    "sha256","16","573.46"
    "sha256","16384","274912.60"
    "sha256","256","8941.40"
    "sha256","64","2268.39"
    "sha256","8192","186168.66"
    "sha512","1024","24584.19"
    "sha512","16","562.22"
    "sha512","16384","67988.14"
    "sha512","256","8026.03"
    "sha512","64","2249.41"
    "sha512","8192","60650.84"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62axx_sk-fs: CPU Load"

    "aes-128-cbc","33.00"
    "aes-128-ecb","34.00"
    "aes-192-cbc","33.00"
    "aes-192-ecb","34.00"
    "aes-256-cbc","32.00"
    "aes-256-ecb","33.00"
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
    :header: "Rail name","Rail voltage(V)","am62axx_sk-fs"

    "vdd_core","0.85","16.82"
    "vddr_core","0.85","1.96"
    "soc_dvdd_3v3","3.30","4.63"
    "soc_dvdd_1v8","1.80","1.44"
    "vdda_1v8","1.80","10.72"
    "vdd_lpddr4/vdd_ddr4","1.10","6.07"
    "Total"," ","41.64"

Table:  **MCU only**

.. csv-table::
    :header: "Rail name","Rail voltage(V)","am62axx_sk-fs"

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
