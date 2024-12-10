
======================================
 RT-linux 09.03 Performance Guide
======================================

.. rubric::  **Read This First**
   :name: read-this-first-rt-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+---------------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                         |
+================+=====================================================================================================================+
| AM65x EVM      | AM65x Evaluation Module rev 1.0 with ARM running at 800MHz, DDR4-2400 (1600 MT/S), TMDX654GPEVM                     |
+----------------+---------------------------------------------------------------------------------------------------------------------+

Table:  Evaluation Modules

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
https://e2e.ti.com/ or https://support.ti.com/

|

System Benchmarks
-------------------------

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
    :header: "Benchmarks","am654x-evm: perf"

    "af_unix_sock_stream_latency (microsec)","76.85"
    "af_unix_socket_stream_bandwidth (MBs)","961.20"
    "bw_file_rd-io-1mb (MB/s)","1090.12"
    "bw_file_rd-o2c-1mb (MB/s)","656.17"
    "bw_mem-bcopy-16mb (MB/s)","899.63"
    "bw_mem-bcopy-1mb (MB/s)","1236.75"
    "bw_mem-bcopy-2mb (MB/s)","954.65"
    "bw_mem-bcopy-4mb (MB/s)","903.85"
    "bw_mem-bcopy-8mb (MB/s)","906.00"
    "bw_mem-bzero-16mb (MB/s)","2020.71"
    "bw_mem-bzero-1mb (MB/s)","2849.72 (min 1236.75, max 4462.69)"
    "bw_mem-bzero-2mb (MB/s)","2188.68 (min 954.65, max 3422.70)"
    "bw_mem-bzero-4mb (MB/s)","1606.22 (min 903.85, max 2308.58)"
    "bw_mem-bzero-8mb (MB/s)","1477.46 (min 906.00, max 2048.92)"
    "bw_mem-cp-16mb (MB/s)","583.03"
    "bw_mem-cp-1mb (MB/s)","1361.31 (min 759.73, max 1962.88)"
    "bw_mem-cp-2mb (MB/s)","841.95 (min 612.65, max 1071.24)"
    "bw_mem-cp-4mb (MB/s)","714.13 (min 584.11, max 844.15)"
    "bw_mem-cp-8mb (MB/s)","692.07 (min 596.04, max 788.10)"
    "bw_mem-fcp-16mb (MB/s)","901.26"
    "bw_mem-fcp-1mb (MB/s)","2798.88 (min 1135.07, max 4462.69)"
    "bw_mem-fcp-2mb (MB/s)","2188.22 (min 953.74, max 3422.70)"
    "bw_mem-fcp-4mb (MB/s)","1602.37 (min 896.16, max 2308.58)"
    "bw_mem-fcp-8mb (MB/s)","1471.04 (min 893.16, max 2048.92)"
    "bw_mem-frd-16mb (MB/s)","1179.85"
    "bw_mem-frd-1mb (MB/s)","1346.89 (min 1135.07, max 1558.71)"
    "bw_mem-frd-2mb (MB/s)","1158.42 (min 953.74, max 1363.09)"
    "bw_mem-frd-4mb (MB/s)","1068.81 (min 896.16, max 1241.46)"
    "bw_mem-frd-8mb (MB/s)","1027.39 (min 893.16, max 1161.61)"
    "bw_mem-fwr-16mb (MB/s)","783.93"
    "bw_mem-fwr-1mb (MB/s)","1760.80 (min 1558.71, max 1962.88)"
    "bw_mem-fwr-2mb (MB/s)","1217.17 (min 1071.24, max 1363.09)"
    "bw_mem-fwr-4mb (MB/s)","1042.81 (min 844.15, max 1241.46)"
    "bw_mem-fwr-8mb (MB/s)","974.86 (min 788.10, max 1161.61)"
    "bw_mem-rd-16mb (MB/s)","1213.78"
    "bw_mem-rd-1mb (MB/s)","3375.84 (min 3297.13, max 3454.55)"
    "bw_mem-rd-2mb (MB/s)","1441.25 (min 1335.11, max 1547.39)"
    "bw_mem-rd-4mb (MB/s)","1125.80 (min 973.24, max 1278.36)"
    "bw_mem-rd-8mb (MB/s)","1055.49 (min 901.41, max 1209.56)"
    "bw_mem-rdwr-16mb (MB/s)","854.38"
    "bw_mem-rdwr-1mb (MB/s)","1796.80 (min 759.73, max 2833.86)"
    "bw_mem-rdwr-2mb (MB/s)","916.27 (min 612.65, max 1219.88)"
    "bw_mem-rdwr-4mb (MB/s)","760.61 (min 584.11, max 937.10)"
    "bw_mem-rdwr-8mb (MB/s)","729.85 (min 596.04, max 863.65)"
    "bw_mem-wr-16mb (MB/s)","894.75"
    "bw_mem-wr-1mb (MB/s)","3144.21 (min 2833.86, max 3454.55)"
    "bw_mem-wr-2mb (MB/s)","1277.50 (min 1219.88, max 1335.11)"
    "bw_mem-wr-4mb (MB/s)","955.17 (min 937.10, max 973.24)"
    "bw_mem-wr-8mb (MB/s)","882.53 (min 863.65, max 901.41)"
    "bw_mmap_rd-mo-1mb (MB/s)","2692.83"
    "bw_mmap_rd-o2c-1mb (MB/s)","721.63"
    "bw_pipe (MB/s)","463.04"
    "bw_unix (MB/s)","961.20"
    "lat_connect (us)","91.54"
    "lat_ctx-2-128k (us)","11.69"
    "lat_ctx-2-256k (us)","10.23"
    "lat_ctx-4-128k (us)","5.15"
    "lat_ctx-4-256k (us)","4.32"
    "lat_fs-0k (num_files)","200.00"
    "lat_fs-10k (num_files)","88.00"
    "lat_fs-1k (num_files)","120.00"
    "lat_fs-4k (num_files)","118.00"
    "lat_mem_rd-stride128-sz1000k (ns)","22.67"
    "lat_mem_rd-stride128-sz125k (ns)","9.78"
    "lat_mem_rd-stride128-sz250k (ns)","10.29"
    "lat_mem_rd-stride128-sz31k (ns)","6.42"
    "lat_mem_rd-stride128-sz50 (ns)","3.77"
    "lat_mem_rd-stride128-sz500k (ns)","11.18"
    "lat_mem_rd-stride128-sz62k (ns)","9.19"
    "lat_mmap-1m (us)","94.00"
    "lat_ops-double-add (ns)","5.04"
    "lat_ops-double-div (ns)","27.70"
    "lat_ops-double-mul (ns)","5.03"
    "lat_ops-float-add (ns)","5.03"
    "lat_ops-float-div (ns)","16.40"
    "lat_ops-float-mul (ns)","5.04"
    "lat_ops-int-add (ns)","1.26"
    "lat_ops-int-bit (ns)","0.84"
    "lat_ops-int-div (ns)","7.55"
    "lat_ops-int-mod (ns)","7.98"
    "lat_ops-int-mul (ns)","5.41"
    "lat_ops-int64-add (ns)","1.26"
    "lat_ops-int64-bit (ns)","0.84"
    "lat_ops-int64-div (ns)","12.00"
    "lat_ops-int64-mod (ns)","9.22"
    "lat_ops-int64-mul (ns)","6.41"
    "lat_pagefault (us)","1.30"
    "lat_pipe (us)","37.35"
    "lat_proc-exec (us)","934.67"
    "lat_proc-fork (us)","790.00"
    "lat_proc-proccall (us)","0.02"
    "lat_select (us)","55.17"
    "lat_sem (us)","4.97"
    "lat_sig-catch (us)","7.14"
    "lat_sig-install (us)","1.21"
    "lat_sig-prot (us)","0.46"
    "lat_syscall-fstat (us)","5.82"
    "lat_syscall-null (us)","0.71"
    "lat_syscall-open (us)","223.26"
    "lat_syscall-read (us)","1.20"
    "lat_syscall-stat (us)","7.52"
    "lat_syscall-write (us)","1.05"
    "lat_tcp (us)","1.45"
    "lat_unix (us)","76.85"
    "latency_for_0.50_mb_block_size (nanosec)","11.18"
    "latency_for_1.00_mb_block_size (nanosec)","11.33 (min 0.00, max 22.67)"
    "pipe_bandwidth (MBs)","463.04"
    "pipe_latency (microsec)","37.35"
    "procedure_call (microsec)","0.02"
    "select_on_200_tcp_fds (microsec)","55.17"
    "semaphore_latency (microsec)","4.97"
    "signal_handler_latency (microsec)","1.21"
    "signal_handler_overhead (microsec)","7.14"
    "tcp_ip_connection_cost_to_localhost (microsec)","91.54"
    "tcp_latency_using_localhost (microsec)","1.45"

Dhrystone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed. For standard ARM
cores the DMIPS/MHz score will be identical with the same compiler and flags.

.. csv-table:: Dhrystone Benchmarks
    :header: "Benchmarks","am654x-evm: perf"

    "cpu_clock (MHz)","800.00"
    "dhrystone_per_mhz (DMIPS/MHz)","2.90"
    "dhrystone_per_second (DhrystoneP)","4081632.80"

Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am654x-evm: perf"

    "whetstone (MIPS)","3333.30"

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am654x-evm: perf"

    "linpack (Kflops)","326161.00"

NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks 
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am654x-evm: perf"

    "assignment (Iterations)","7.89"
    "fourier (Iterations)","12739.00"
    "fp_emulation (Iterations)","52.31"
    "huffman (Iterations)","657.98"
    "idea (Iterations)","1882.20"
    "lu_decomposition (Iterations)","306.17"
    "neural_net (Iterations)","5.01"
    "numeric_sort (Iterations)","339.56"
    "string_sort (Iterations)","88.18"

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

.. csv-table:: Stream Benchmarks
    :header: "Benchmarks","am654x-evm: perf"

    "add (MB/s)","1590.20"
    "copy (MB/s)","1835.60"
    "scale (MB/s)","1816.80"
    "triad (MB/s)","1497.60"

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
    :header: "Benchmarks","am654x-evm: perf"

    "4m-check (workloads/)","314.62"
    "4m-check-reassembly (workloads/)","77.88"
    "4m-check-reassembly-tcp (workloads/)","36.87"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","12.05"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.14"
    "4m-cmykw2 (workloads/)","139.37"
    "4m-cmykw2-rotatew2 (workloads/)","15.74"
    "4m-reassembly (workloads/)","57.64"
    "4m-rotatew2 (workloads/)","12.44"
    "4m-tcp-mixed (workloads/)","69.87"
    "4m-x264w2 (workloads/)","1.16"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","10.98"
    "idct-4mw1 (workloads/)","10.99"
    "ippktcheck-4m (workloads/)","314.23"
    "ippktcheck-4mw1 (workloads/)","313.21"
    "ipres-4m (workloads/)","68.40"
    "ipres-4mw1 (workloads/)","68.37"
    "md5-4m (workloads/)","17.06"
    "md5-4mw1 (workloads/)","17.02"
    "rgbcmyk-4m (workloads/)","36.39"
    "rgbcmyk-4mw1 (workloads/)","36.39"
    "rotate-4ms1 (workloads/)","14.24"
    "rotate-4ms1w1 (workloads/)","14.24"
    "rotate-4ms64 (workloads/)","14.38"
    "rotate-4ms64w1 (workloads/)","14.38"
    "x264-4mq (workloads/)","0.33"
    "x264-4mqw1 (workloads/)","0.33"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am654x-evm: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","16.45 (min 16.01, max 16.77)"

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

ICSSG Ethernet Driver 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric::  TCP Bidirectional Throughput 
   :name: tcp-bidirectional-throughput

.. csv-table:: ICSSG TCP Bidirectional Throughput
    :header: "Command Used","am654x-evm: THROUGHPUT (Mbits/sec)","am654x-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_MAERTS","1021.47","45.64"

.. csv-table:: ICSSG UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am654x-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am654x-evm: THROUGHPUT (Mbits/sec)","am654x-evm: Packets Per Second (kPPS)","am654x-evm: CPU Load %"

    "256","210.00","21.34","13.00","7.80"

|

PCIe Driver
-------------------------

PCIe-ETH
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: PCIe Ethernet performance
    :header: "TCP Window Size(Kbytes)","am654x-evm: Bandwidth (Mbits/sec)"

    "8","0.00"
    "16","0.00"
    "32","0.00"
    "64","0.00"
    "128","0.00"
    "256","0.00"

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
    :header: "Buffer size (bytes)","am654x-evm: Write EXT4 Throughput (Mbytes/sec)","am654x-evm: Write EXT4 CPU Load (%)","am654x-evm: Read EXT4 Throughput (Mbytes/sec)","am654x-evm: Read EXT4 CPU Load (%)"

    "1m","60.70","1.11","175.00","1.48"
    "4m","60.80","1.06","175.00","1.25"
    "4k","49.40","28.86","55.80","32.01"
    "256k","60.60","1.34","174.00","2.75"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am654x-evm: Write Throughput (Kbytes/sec)","am654x-evm: Read Throughput (Kbytes/sec)"

    "2000000","61248.60","173375.66"
    "4000000","61077.35","177604.34"

MMCSD
-----

.. important::

 The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am654x-evm: Write Raw Throughput (Mbytes/sec)","am654x-evm: Write Raw CPU Load (%)","am654x-evm: Read Raw Throughput (Mbytes/sec)","am654x-evm: Read Raw CPU Load (%)"

    "102400","15.03 (min 14.47, max 15.44)","2.07 (min 1.64, max 3.53)","21.22","1.73"
    "262144","15.05 (min 14.67, max 15.41)","2.03 (min 1.65, max 3.43)","23.27","1.78"
    "524288","15.14 (min 14.32, max 15.50)","2.05 (min 1.61, max 3.28)","23.65","1.70"
    "1048576","15.37 (min 14.60, max 16.08)","1.97 (min 1.65, max 3.07)","23.84","1.71"
    "5242880","15.25 (min 14.55, max 15.63)","2.01 (min 1.64, max 3.03)","23.83","1.88"

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am654x-evm: Write Throughput (Kbytes/sec)","am654x-evm: Read Throughput (Kbytes/sec)"

    "400000","18123.89","19980.49"
    "800000","21167.96","21729.44"
    "1000000","20634.76","22598.62"

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am654x-evm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","15611.90"
    "aes-128-cbc","16","245.21"
    "aes-128-cbc","16384","113410.05"
    "aes-128-cbc","256","4169.73"
    "aes-128-cbc","64","1085.46"
    "aes-128-cbc","8192","83722.24"
    "aes-128-ecb","1024","15945.73"
    "aes-128-ecb","16","259.56"
    "aes-128-ecb","16384","121727.66"
    "aes-128-ecb","256","3999.74"
    "aes-128-ecb","64","1063.10"
    "aes-128-ecb","8192","81619.63"
    "aes-192-cbc","1024","15231.66"
    "aes-192-cbc","16","256.90"
    "aes-192-cbc","16384","114726.23"
    "aes-192-cbc","256","3811.50"
    "aes-192-cbc","64","1027.16"
    "aes-192-cbc","8192","78921.73"
    "aes-192-ecb","1024","14815.23"
    "aes-192-ecb","16","271.24"
    "aes-192-ecb","16384","117265.75"
    "aes-192-ecb","256","4113.58"
    "aes-192-ecb","64","1052.39"
    "aes-192-ecb","8192","75014.14"
    "aes-256-cbc","1024","14758.23"
    "aes-256-cbc","16","275.32"
    "aes-256-cbc","16384","111700.65"
    "aes-256-cbc","256","4344.15"
    "aes-256-cbc","64","1029.80"
    "aes-256-cbc","8192","79162.03"
    "aes-256-ecb","1024","15332.01"
    "aes-256-ecb","16","264.85"
    "aes-256-ecb","16384","113410.05"
    "aes-256-ecb","256","4039.51"
    "aes-256-ecb","64","1057.26"
    "aes-256-ecb","8192","81207.30"
    "des3","1024","14565.03"
    "des3","16","258.01"
    "des3","16384","74208.60"
    "des3","256","4291.58"
    "des3","64","1006.95"
    "des3","8192","58821.29"
    "sha1","1024","20338.69"
    "sha1","16","341.55"
    "sha1","16384","154910.72"
    "sha1","256","5345.19"
    "sha1","64","1354.24"
    "sha1","8192","106455.04"
    "sha256","1024","20236.63"
    "sha256","16","337.02"
    "sha256","16384","156942.34"
    "sha256","256","5294.42"
    "sha256","64","1339.54"
    "sha256","8192","107151.36"
    "sha512","1024","14032.90"
    "sha512","16","327.79"
    "sha512","16384","37120.68"
    "sha512","256","4670.12"
    "sha512","64","1313.79"
    "sha512","8192","33385.13"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am654x-evm: CPU Load"

    "aes-128-cbc","41.00"
    "aes-128-ecb","43.00"
    "aes-192-cbc","41.00"
    "aes-192-ecb","42.00"
    "aes-256-cbc","41.00"
    "aes-256-ecb","41.00"
    "des3","38.00"
    "sha1","98.00"
    "sha256","98.00"
    "sha512","98.00"

Listed for each algorithm are the code snippets used to run each benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","am654x-evm: Throughput (Mbps)","am654x-evm: Packets/Sec","am654x-evm: CPU Load"

    "aes128","91.30","8.00","24.09"
