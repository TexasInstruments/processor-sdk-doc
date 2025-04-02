======================================
RT-linux 11.00 Performance Guide
======================================

.. rubric::  **Read This First**
   :name: read-this-first-rt-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+---------------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                         |
+================+=====================================================================================================================+
| AM64x EVM      | AM64x Evaluation Module rev E1 with ARM running at 1GHz, DDR data rate 1600 MT/S                                    |
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

Stress-ng and Cyclic Test
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _RT-linux-performance:

stress-ng (next-generation) will stress test a embedded platform in various selectable ways.
It was designed to exercise various physical subsystems as well as the various
operating system kernel interfaces. stress-ng can also measure test throughput rates;
this can be useful to observe performance changes across different operating system or types of hardware.

Cyclictest is most commonly used for benchmarking RT systems.
It is one of the most frequently used tools for evaluating the relative performance of real-time systems.
Some performance tests which use Cyclictest are System benchmarking, Latency debugging with tracing and
approximating application performance.

Test commands used for running stress-ng and cyclictest together

.. code:: console

   stress-ng --cpu-method=all -c 4 &
   cyclictest -m -Sp80 -D6h -h400 -i200 -M -q

The latencies observed with this DK are summarized below:

.. csv-table::
   :header: "Latencies","CPU 0","CPU 1"

   "Minimum (usec)","6","6"
   "Average (usec)","8","8"
   "Maximum (usec)","77","105"

.. image:: img/rt-cpu-method-all-latency-histogram.png

|

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
    :header: "Benchmarks","am64xx-hsevm: perf"

    "af_unix_sock_stream_latency (microsec)","39.20"
    "af_unix_socket_stream_bandwidth (MBs)","535.26"
    "bw_file_rd-io-1mb (MB/s)","873.06"
    "bw_file_rd-o2c-1mb (MB/s)","500.58"
    "bw_mem-bcopy-16mb (MB/s)","976.92"
    "bw_mem-bcopy-1mb (MB/s)","995.36"
    "bw_mem-bcopy-2mb (MB/s)","987.65"
    "bw_mem-bcopy-4mb (MB/s)","912.30"
    "bw_mem-bcopy-8mb (MB/s)","987.41"
    "bw_mem-bzero-16mb (MB/s)","2117.24"
    "bw_mem-bzero-1mb (MB/s)","1556.44 (min 995.36, max 2117.52)"
    "bw_mem-bzero-2mb (MB/s)","1553.34 (min 987.65, max 2119.02)"
    "bw_mem-bzero-4mb (MB/s)","1513.23 (min 912.30, max 2114.16)"
    "bw_mem-bzero-8mb (MB/s)","1551.49 (min 987.41, max 2115.56)"
    "bw_mem-cp-16mb (MB/s)","533.72"
    "bw_mem-cp-1mb (MB/s)","1553.21 (min 542.79, max 2563.63)"
    "bw_mem-cp-2mb (MB/s)","1448.26 (min 557.34, max 2339.18)"
    "bw_mem-cp-4mb (MB/s)","1393.63 (min 562.98, max 2224.28)"
    "bw_mem-cp-8mb (MB/s)","1343.05 (min 539.30, max 2146.79)"
    "bw_mem-fcp-16mb (MB/s)","1084.82"
    "bw_mem-fcp-1mb (MB/s)","1600.87 (min 1084.21, max 2117.52)"
    "bw_mem-fcp-2mb (MB/s)","1579.89 (min 1040.76, max 2119.02)"
    "bw_mem-fcp-4mb (MB/s)","1586.67 (min 1059.18, max 2114.16)"
    "bw_mem-fcp-8mb (MB/s)","1565.07 (min 1014.58, max 2115.56)"
    "bw_mem-frd-16mb (MB/s)","1307.30"
    "bw_mem-frd-1mb (MB/s)","1174.33 (min 1084.21, max 1264.45)"
    "bw_mem-frd-2mb (MB/s)","1191.30 (min 1040.76, max 1341.83)"
    "bw_mem-frd-4mb (MB/s)","1177.79 (min 1059.18, max 1296.39)"
    "bw_mem-frd-8mb (MB/s)","1125.34 (min 1014.58, max 1236.09)"
    "bw_mem-fwr-16mb (MB/s)","2126.25"
    "bw_mem-fwr-1mb (MB/s)","1914.04 (min 1264.45, max 2563.63)"
    "bw_mem-fwr-2mb (MB/s)","1840.51 (min 1341.83, max 2339.18)"
    "bw_mem-fwr-4mb (MB/s)","1760.34 (min 1296.39, max 2224.28)"
    "bw_mem-fwr-8mb (MB/s)","1691.44 (min 1236.09, max 2146.79)"
    "bw_mem-rd-16mb (MB/s)","1339.70"
    "bw_mem-rd-1mb (MB/s)","1067.51 (min 833.89, max 1301.12)"
    "bw_mem-rd-2mb (MB/s)","1096.69 (min 826.56, max 1366.82)"
    "bw_mem-rd-4mb (MB/s)","1084.80 (min 834.03, max 1335.56)"
    "bw_mem-rd-8mb (MB/s)","1110.87 (min 876.52, max 1345.22)"
    "bw_mem-rdwr-16mb (MB/s)","870.23"
    "bw_mem-rdwr-1mb (MB/s)","677.24 (min 542.79, max 811.69)"
    "bw_mem-rdwr-2mb (MB/s)","706.14 (min 557.34, max 854.94)"
    "bw_mem-rdwr-4mb (MB/s)","697.94 (min 562.98, max 832.90)"
    "bw_mem-rdwr-8mb (MB/s)","697.96 (min 539.30, max 856.62)"
    "bw_mem-wr-16mb (MB/s)","886.23"
    "bw_mem-wr-1mb (MB/s)","822.79 (min 811.69, max 833.89)"
    "bw_mem-wr-2mb (MB/s)","840.75 (min 826.56, max 854.94)"
    "bw_mem-wr-4mb (MB/s)","833.47 (min 832.90, max 834.03)"
    "bw_mem-wr-8mb (MB/s)","866.57 (min 856.62, max 876.52)"
    "bw_mmap_rd-mo-1mb (MB/s)","1327.77"
    "bw_mmap_rd-o2c-1mb (MB/s)","466.78"
    "bw_pipe (MB/s)","543.51"
    "bw_unix (MB/s)","535.26"
    "lat_connect (us)","75.45"
    "lat_ctx-2-128k (us)","14.36"
    "lat_ctx-2-256k (us)","32.22"
    "lat_ctx-4-128k (us)","11.99"
    "lat_ctx-4-256k (us)","19.26"
    "lat_fs-0k (num_files)","180.00"
    "lat_fs-10k (num_files)","84.00"
    "lat_fs-1k (num_files)","120.00"
    "lat_fs-4k (num_files)","123.00"
    "lat_mem_rd-stride128-sz1000k (ns)","48.32"
    "lat_mem_rd-stride128-sz125k (ns)","7.85"
    "lat_mem_rd-stride128-sz250k (ns)","9.46"
    "lat_mem_rd-stride128-sz31k (ns)","3.06"
    "lat_mem_rd-stride128-sz50 (ns)","3.02"
    "lat_mem_rd-stride128-sz500k (ns)","44.34"
    "lat_mem_rd-stride128-sz62k (ns)","7.37"
    "lat_mmap-1m (us)","65.00"
    "lat_ops-double-add (ns)","4.02"
    "lat_ops-double-div (ns)","22.11"
    "lat_ops-double-mul (ns)","4.02"
    "lat_ops-float-add (ns)","4.02"
    "lat_ops-float-div (ns)","13.07"
    "lat_ops-float-mul (ns)","4.02"
    "lat_ops-int-add (ns)","1.01"
    "lat_ops-int-bit (ns)","0.67"
    "lat_ops-int-div (ns)","6.03"
    "lat_ops-int-mod (ns)","6.37"
    "lat_ops-int-mul (ns)","4.32"
    "lat_ops-int64-add (ns)","1.01"
    "lat_ops-int64-bit (ns)","0.67"
    "lat_ops-int64-div (ns)","9.55"
    "lat_ops-int64-mod (ns)","7.37"
    "lat_ops-int64-mul (ns)","5.00"
    "lat_pagefault (us)","1.82"
    "lat_pipe (us)","26.36"
    "lat_proc-exec (us)","1157.20"
    "lat_proc-fork (us)","1010.83"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","46.54"
    "lat_sem (us)","3.37"
    "lat_sig-catch (us)","5.98"
    "lat_sig-install (us)","0.91"
    "lat_sig-prot (us)","0.36"
    "lat_syscall-fstat (us)","2.33"
    "lat_syscall-null (us)","0.58"
    "lat_syscall-open (us)","406.36"
    "lat_syscall-read (us)","0.84"
    "lat_syscall-stat (us)","6.48"
    "lat_syscall-write (us)","0.77"
    "lat_tcp (us)","1.11"
    "lat_unix (us)","39.20"
    "latency_for_0.50_mb_block_size (nanosec)","44.34"
    "latency_for_1.00_mb_block_size (nanosec)","24.16 (min 0.00, max 48.32)"
    "pipe_bandwidth (MBs)","543.51"
    "pipe_latency (microsec)","26.36"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","46.54"
    "semaphore_latency (microsec)","3.37"
    "signal_handler_latency (microsec)","0.91"
    "signal_handler_overhead (microsec)","5.98"
    "tcp_ip_connection_cost_to_localhost (microsec)","75.45"
    "tcp_latency_using_localhost (microsec)","1.11"

Dhrystone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed. For standard ARM
cores the DMIPS/MHz score will be identical with the same compiler and flags.

.. csv-table:: Dhrystone Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "cpu_clock (MHz)","1000.00"
    "dhrystone_per_mhz (DMIPS/MHz)","2.90"
    "dhrystone_per_second (DhrystoneP)","5128205.00"

Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "whetstone (MIPS)","5000.00"

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "linpack (Kflops)","407227.00"

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
    :header: "Benchmarks","am64xx-hsevm: perf"

    "add (MB/s)","1619.70"
    "copy (MB/s)","2019.30"
    "scale (MB/s)","2250.40"
    "triad (MB/s)","1615.70"

CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "cjpeg-rose7-preset (workloads/)","29.41"
    "core (workloads/)","0.21"
    "coremark-pro ()","587.13"
    "linear_alg-mid-100x100-sp (workloads/)","10.42"
    "loops-all-mid-10k-sp (workloads/)","0.48"
    "nnet_test (workloads/)","0.77"
    "parser-125k (workloads/)","5.68"
    "radix2-big-64k (workloads/)","19.25"
    "sha-test (workloads/)","57.80"
    "zip-test (workloads/)","15.63"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "cjpeg-rose7-preset (workloads/)","58.82"
    "core (workloads/)","0.42"
    "coremark-pro ()","1034.74"
    "linear_alg-mid-100x100-sp (workloads/)","20.65"
    "loops-all-mid-10k-sp (workloads/)","0.86"
    "nnet_test (workloads/)","1.53"
    "parser-125k (workloads/)","5.43"
    "radix2-big-64k (workloads/)","32.63"
    "sha-test (workloads/)","114.94"
    "zip-test (workloads/)","28.17"

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
    :header: "Benchmarks","am64xx-hsevm: perf"

    "4m-check (workloads/)","281.69"
    "4m-check-reassembly (workloads/)","61.50"
    "4m-check-reassembly-tcp (workloads/)","36.28"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","14.43"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","0.75"
    "4m-cmykw2 (workloads/)","85.14"
    "4m-cmykw2-rotatew2 (workloads/)","18.51"
    "4m-reassembly (workloads/)","56.18"
    "4m-rotatew2 (workloads/)","19.53"
    "4m-tcp-mixed (workloads/)","81.63"
    "4m-x264w2 (workloads/)","0.76"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","13.62"
    "idct-4mw1 (workloads/)","13.62"
    "ippktcheck-4m (workloads/)","281.82"
    "ippktcheck-4mw1 (workloads/)","280.93"
    "ipres-4m (workloads/)","72.74"
    "ipres-4mw1 (workloads/)","72.18"
    "md5-4m (workloads/)","19.67"
    "md5-4mw1 (workloads/)","19.81"
    "rgbcmyk-4m (workloads/)","44.61"
    "rgbcmyk-4mw1 (workloads/)","44.71"
    "rotate-4ms1 (workloads/)","16.56"
    "rotate-4ms1w1 (workloads/)","16.52"
    "rotate-4ms64 (workloads/)","16.73"
    "rotate-4ms64w1 (workloads/)","16.77"
    "x264-4mq (workloads/)","0.41"
    "x264-4mqw1 (workloads/)","0.41"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am64xx-hsevm: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","21.36 (min 20.52, max 21.88)"

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

- CPSW3g: AM64x

.. rubric::  TCP Bidirectional Throughput 
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1095.34","98.12"

ICSSG Ethernet Driver 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric::  TCP Bidirectional Throughput 
   :name: tcp-bidirectional-throughput

.. csv-table:: ICSSG TCP Bidirectional Throughput
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_MAERTS","183.94","37.22"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: ICSSG-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: ICSSG TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_MAERTS","359.51","53.51"

.. csv-table:: ICSSG UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load %"

    "128","82.00","1.97","3.00","0.64"
    "256","210.00","7.39","4.00","0.71"
    "1024","978.00","40.68","5.00","6.72"
    "1518","1472.00","94.21","8.00","9.70"

|

OSPI Flash Driver
-------------------------

RAW
^^^

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am64xx-hsevm: Raw Read Throughput (Mbytes/sec)"

    "50","108.69"

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
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "1m","60.90","4.78","175.00","8.43"
    "4m","60.80","3.41","174.00","6.83"
    "4k","48.40","54.81","55.80","48.81"
    "256k","60.60","6.56","174.00","9.49"

EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "102400","53.73 (min 51.22, max 54.75)","11.69 (min 10.55, max 15.06)","176.86","31.48"
    "262144","53.21 (min 49.80, max 54.17)","11.37 (min 10.31, max 15.20)","181.69","30.56"
    "524288","53.20 (min 49.68, max 54.36)","12.17 (min 10.91, max 15.48)","182.95","28.57"
    "1048576","53.49 (min 49.83, max 54.53)","11.91 (min 10.76, max 15.31)","182.97","27.68"
    "5242880","53.50 (min 50.17, max 54.57)","10.88 (min 9.69, max 14.59)","182.94","27.68"

EMMC VFAT
^^^^^^^^^

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am64xx-hsevm: Write VFAT Throughput (Mbytes/sec)","am64xx-hsevm: Write VFAT CPU Load (%)","am64xx-hsevm: Read VFAT Throughput (Mbytes/sec)","am64xx-hsevm: Read VFAT CPU Load (%)"

    "102400","49.53 (min 41.41, max 51.76)","14.70 (min 12.69, max 20.76)","165.41","31.30"
    "262144","50.47 (min 41.92, max 52.82)","14.72 (min 12.98, max 20.97)","170.09","31.03"
    "524288","50.37 (min 41.84, max 52.80)","14.89 (min 13.10, max 20.72)","169.50","29.51"
    "1048576","50.62 (min 42.25, max 52.97)","14.22 (min 12.66, max 19.76)","169.28","27.27"
    "5242880","50.74 (min 42.19, max 53.16)","13.71 (min 11.90, max 19.84)","169.63","27.73"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am64xx-hsevm: Write Throughput (Kbytes/sec)","am64xx-hsevm: Read Throughput (Kbytes/sec)"

    "2000000","59041.44","168907.22"
    "4000000","59308.60","172463.16"

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
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "1m","41.50","3.23","87.00","5.01"
    "4m","41.80","2.57","87.20","3.57"
    "4k","2.81","8.28","12.80","14.46"
    "256k","35.90","4.53","83.10","6.21"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am64xx-hsevm: Write Raw Throughput (Mbytes/sec)","am64xx-hsevm: Write Raw CPU Load (%)","am64xx-hsevm: Read Raw Throughput (Mbytes/sec)","am64xx-hsevm: Read Raw CPU Load (%)"

    "102400","28.52 (min 27.85, max 29.34)","6.12 (min 5.46, max 8.49)","39.35","7.63"
    "262144","28.36 (min 27.89, max 29.10)","6.54 (min 5.35, max 8.79)","40.40","6.82"
    "524288","29.14 (min 28.88, max 29.71)","5.85 (min 4.99, max 8.69)","45.51","6.99"
    "1048576","29.44 (min 29.04, max 29.61)","5.75 (min 4.73, max 8.64)","45.37","6.77"
    "5242880","29.29 (min 28.70, max 30.30)","5.69 (min 4.86, max 8.71)","45.33","6.97"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am64xx-hsevm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","20972.89"
    "aes-128-cbc","16","308.04"
    "aes-128-cbc","16384","133207.38"
    "aes-128-cbc","256","5377.96"
    "aes-128-cbc","64","1348.82"
    "aes-128-cbc","8192","98050.05"
    "aes-128-ecb","1024","20139.01"
    "aes-128-ecb","16","311.34"
    "aes-128-ecb","16384","139935.74"
    "aes-128-ecb","256","5468.25"
    "aes-128-ecb","64","1381.89"
    "aes-128-ecb","8192","99188.74"
    "aes-192-cbc","1024","20745.56"
    "aes-192-cbc","16","313.45"
    "aes-192-cbc","16384","126697.47"
    "aes-192-cbc","256","5491.88"
    "aes-192-cbc","64","1363.61"
    "aes-192-cbc","8192","92886.36"
    "aes-192-ecb","1024","21486.93"
    "aes-192-ecb","16","311.40"
    "aes-192-ecb","16384","130913.62"
    "aes-192-ecb","256","5517.31"
    "aes-192-ecb","64","1386.69"
    "aes-192-ecb","8192","96488.11"
    "aes-256-cbc","1024","18767.87"
    "aes-256-cbc","16","293.50"
    "aes-256-cbc","16384","120034.65"
    "aes-256-cbc","256","5228.37"
    "aes-256-cbc","64","1313.64"
    "aes-256-cbc","8192","89967.27"
    "aes-256-ecb","1024","21326.85"
    "aes-256-ecb","16","311.80"
    "aes-256-ecb","16384","122404.86"
    "aes-256-ecb","256","5472.26"
    "aes-256-ecb","64","1403.71"
    "aes-256-ecb","8192","92056.23"
    "sha256","1024","25799.00"
    "sha256","16","429.11"
    "sha256","16384","208180.57"
    "sha256","256","6721.79"
    "sha256","64","1698.90"
    "sha256","8192","139889.32"
    "sha512","1024","17905.66"
    "sha512","16","415.45"
    "sha512","16384","47966.89"
    "sha512","256","5931.52"
    "sha512","64","1662.76"
    "sha512","8192","43048.96"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am64xx-hsevm: CPU Load"

    "aes-128-cbc","43.00"
    "aes-128-ecb","45.00"
    "aes-192-cbc","44.00"
    "aes-192-ecb","44.00"
    "aes-256-cbc","42.00"
    "aes-256-ecb","44.00"
    "sha256","93.00"
    "sha512","93.00"

Listed for each algorithm are the code snippets used to run each benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc
