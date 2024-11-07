.. include:: <isonum.txt>

======================================
 RT-linux 10.00 Performance Guide
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
http://e2e.ti.com/ or http://support.ti.com/



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

Test command for running stress-ng and cyclictest together

``stress-ng --cpu-method=all -c 4 &``

``cyclictest -m -Sp98 -D6h -h400 -i200 -q``

.. csv-table::
    :header: "Latencies", "am64xx-hsevm:per-core"

    "Minimum (usec)","6,6"
    "Average (usec)","8,9"
    "Maximum (usec)","49,66"

|

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
    :header: "Benchmarks","am64xx-hsevm: perf"

    "af_unix_sock_stream_latency (microsec)","34.97"
    "af_unix_socket_stream_bandwidth (MBs)","565.33"
    "bw_file_rd-io-1mb (MB/s)","822.77"
    "bw_file_rd-o2c-1mb (MB/s)","492.61"
    "bw_mem-bcopy-16mb (MB/s)","870.94"
    "bw_mem-bcopy-1mb (MB/s)","931.79"
    "bw_mem-bcopy-2mb (MB/s)","905.25"
    "bw_mem-bcopy-4mb (MB/s)","896.16"
    "bw_mem-bcopy-8mb (MB/s)","1003.01"
    "bw_mem-bzero-16mb (MB/s)","2116.68"
    "bw_mem-bzero-1mb (MB/s)","1524.85 (min 931.79, max 2117.90)"
    "bw_mem-bzero-2mb (MB/s)","1510.83 (min 905.25, max 2116.40)"
    "bw_mem-bzero-4mb (MB/s)","1506.28 (min 896.16, max 2116.40)"
    "bw_mem-bzero-8mb (MB/s)","1560.69 (min 1003.01, max 2118.36)"
    "bw_mem-cp-16mb (MB/s)","516.98"
    "bw_mem-cp-1mb (MB/s)","1561.64 (min 530.69, max 2592.59)"
    "bw_mem-cp-2mb (MB/s)","1439.93 (min 528.75, max 2351.10)"
    "bw_mem-cp-4mb (MB/s)","1376.79 (min 521.85, max 2231.73)"
    "bw_mem-cp-8mb (MB/s)","1376.15 (min 591.89, max 2160.41)"
    "bw_mem-fcp-16mb (MB/s)","885.49"
    "bw_mem-fcp-1mb (MB/s)","1607.20 (min 1096.49, max 2117.90)"
    "bw_mem-fcp-2mb (MB/s)","1548.32 (min 980.23, max 2116.40)"
    "bw_mem-fcp-4mb (MB/s)","1557.27 (min 998.13, max 2116.40)"
    "bw_mem-fcp-8mb (MB/s)","1600.82 (min 1083.28, max 2118.36)"
    "bw_mem-frd-16mb (MB/s)","1293.14"
    "bw_mem-frd-1mb (MB/s)","1196.34 (min 1096.49, max 1296.18)"
    "bw_mem-frd-2mb (MB/s)","1137.58 (min 980.23, max 1294.92)"
    "bw_mem-frd-4mb (MB/s)","1146.53 (min 998.13, max 1294.92)"
    "bw_mem-frd-8mb (MB/s)","1190.78 (min 1083.28, max 1298.28)"
    "bw_mem-fwr-16mb (MB/s)","2114.16"
    "bw_mem-fwr-1mb (MB/s)","1944.39 (min 1296.18, max 2592.59)"
    "bw_mem-fwr-2mb (MB/s)","1823.01 (min 1294.92, max 2351.10)"
    "bw_mem-fwr-4mb (MB/s)","1763.33 (min 1294.92, max 2231.73)"
    "bw_mem-fwr-8mb (MB/s)","1729.35 (min 1298.28, max 2160.41)"
    "bw_mem-rd-16mb (MB/s)","1352.49"
    "bw_mem-rd-1mb (MB/s)","1104.06 (min 841.47, max 1366.65)"
    "bw_mem-rd-2mb (MB/s)","1098.91 (min 842.58, max 1355.24)"
    "bw_mem-rd-4mb (MB/s)","1100.89 (min 839.37, max 1362.40)"
    "bw_mem-rd-8mb (MB/s)","1110.39 (min 871.93, max 1348.85)"
    "bw_mem-rdwr-16mb (MB/s)","878.49"
    "bw_mem-rdwr-1mb (MB/s)","684.74 (min 530.69, max 838.79)"
    "bw_mem-rdwr-2mb (MB/s)","675.39 (min 528.75, max 822.03)"
    "bw_mem-rdwr-4mb (MB/s)","672.03 (min 521.85, max 822.20)"
    "bw_mem-rdwr-8mb (MB/s)","722.80 (min 591.89, max 853.70)"
    "bw_mem-wr-16mb (MB/s)","900.04"
    "bw_mem-wr-1mb (MB/s)","840.13 (min 838.79, max 841.47)"
    "bw_mem-wr-2mb (MB/s)","832.31 (min 822.03, max 842.58)"
    "bw_mem-wr-4mb (MB/s)","830.79 (min 822.20, max 839.37)"
    "bw_mem-wr-8mb (MB/s)","862.82 (min 853.70, max 871.93)"
    "bw_mmap_rd-mo-1mb (MB/s)","1244.44"
    "bw_mmap_rd-o2c-1mb (MB/s)","493.10"
    "bw_pipe (MB/s)","539.16"
    "bw_unix (MB/s)","565.33"
    "lat_connect (us)","74.47"
    "lat_ctx-2-128k (us)","6.35"
    "lat_ctx-2-256k (us)","19.78"
    "lat_ctx-4-128k (us)","6.93"
    "lat_ctx-4-256k (us)","3.52"
    "lat_fs-0k (num_files)","194.00"
    "lat_fs-10k (num_files)","92.00"
    "lat_fs-1k (num_files)","131.00"
    "lat_fs-4k (num_files)","124.00"
    "lat_mem_rd-stride128-sz1000k (ns)","48.11"
    "lat_mem_rd-stride128-sz125k (ns)","7.80"
    "lat_mem_rd-stride128-sz250k (ns)","13.79"
    "lat_mem_rd-stride128-sz31k (ns)","3.06"
    "lat_mem_rd-stride128-sz50 (ns)","3.02"
    "lat_mem_rd-stride128-sz500k (ns)","43.46"
    "lat_mem_rd-stride128-sz62k (ns)","7.36"
    "lat_mmap-1m (us)","77.00"
    "lat_ops-double-add (ns)","4.02"
    "lat_ops-double-div (ns)","22.11"
    "lat_ops-double-mul (ns)","4.02"
    "lat_ops-float-add (ns)","4.02"
    "lat_ops-float-div (ns)","13.06"
    "lat_ops-float-mul (ns)","4.02"
    "lat_ops-int-add (ns)","1.01"
    "lat_ops-int-bit (ns)","0.67"
    "lat_ops-int-div (ns)","6.03"
    "lat_ops-int-mod (ns)","6.37"
    "lat_ops-int-mul (ns)","4.37"
    "lat_ops-int64-add (ns)","1.01"
    "lat_ops-int64-bit (ns)","0.67"
    "lat_ops-int64-div (ns)","9.55"
    "lat_ops-int64-mod (ns)","7.37"
    "lat_ops-int64-mul (ns)","5.03"
    "lat_pagefault (us)","1.66"
    "lat_pipe (us)","22.51"
    "lat_proc-exec (us)","1308.40"
    "lat_proc-fork (us)","961.50"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","47.34"
    "lat_sem (us)","2.62"
    "lat_sig-catch (us)","6.10"
    "lat_sig-install (us)","0.96"
    "lat_sig-prot (us)","1.32"
    "lat_syscall-fstat (us)","2.26"
    "lat_syscall-null (us)","0.58"
    "lat_syscall-open (us)","372.33"
    "lat_syscall-read (us)","0.91"
    "lat_syscall-stat (us)","6.78"
    "lat_syscall-write (us)","0.77"
    "lat_tcp (us)","1.18"
    "lat_unix (us)","34.97"
    "latency_for_0.50_mb_block_size (nanosec)","43.46"
    "latency_for_1.00_mb_block_size (nanosec)","24.06 (min 0.00, max 48.11)"
    "pipe_bandwidth (MBs)","539.16"
    "pipe_latency (microsec)","22.51"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","47.34"
    "semaphore_latency (microsec)","2.62"
    "signal_handler_latency (microsec)","0.96"
    "signal_handler_overhead (microsec)","6.10"
    "tcp_ip_connection_cost_to_localhost (microsec)","74.47"
    "tcp_latency_using_localhost (microsec)","1.18"




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

    "whetstone (MIPS)","3333.30"




Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "linpack (Kflops)","408633.00"






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

    "add (MB/s)","1621.30"
    "copy (MB/s)","2089.50"
    "scale (MB/s)","2258.00"
    "triad (MB/s)","1620.00"




CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark\ |reg|\ -Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark\ |reg| benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "cjpeg-rose7-preset (workloads/)","29.50"
    "core (workloads/)","0.21"
    "coremark-pro ()","590.21"
    "linear_alg-mid-100x100-sp (workloads/)","10.43"
    "loops-all-mid-10k-sp (workloads/)","0.48"
    "nnet_test (workloads/)","0.77"
    "parser-125k (workloads/)","5.62"
    "radix2-big-64k (workloads/)","20.31"
    "sha-test (workloads/)","57.80"
    "zip-test (workloads/)","15.63"



 
 



 
 

 

 

 



 

 

 



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

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1132.27","99.03"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1243.94","79.58"




.. rubric::  UDP Throughput 
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","12.14","84.00","88.30"
    "128","82.00","54.18","83.00","89.33"
    "256","210.00","97.96","58.00","67.25"
    "1024","978.00","575.14","74.00","92.40"
    "1518","1472.00","828.30","70.00","89.95"




.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","1.12","8.00","0.16"
    "128","82.00","5.12","8.00","0.11"
    "256","210.00","13.44","8.00","4.66"
    "1024","978.00","67.28","9.00","0.21"
    "1518","1472.00","97.74","8.00","8.42"




.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)","am64xx-hsevm: Packet Loss %"

    "64","18.00","18.13","126.00","75.43","67.04"
    "128","82.00","80.59","123.00","77.11","76.52"
    "256","210.00","111.34","66.00","65.16","58.55"
    "1024","978.00","875.45","112.00","85.16","6.55"
    "1518","1472.00","911.43","77.00","82.74","4.77"

 
 


ICSSG Ethernet Driver 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric::  TCP Bidirectional Throughput 
   :name: tcp-bidirectional-throughput

.. csv-table:: ICSSG TCP Bidirectional Throughput
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_MAERTS","844.83","99.92"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: ICSSG-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: ICSSG TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_MAERTS","870.69","78.99"






.. csv-table:: ICSSG UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load %"

    "64","18.00","13.84","29.14","90.54"
    "128","82.00","61.76","64.58","91.48"
    "256","210.00","152.83","79.24","91.51"
    "1024","978.00","659.92","80.73","92.60"
    "1518","1472.00","951.78","78.37","92.78"

 
 
 



|

PCIe Driver
-------------------------

PCIe-ETH
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: PCIe Ethernet performance
    :header: "TCP Window Size(Kbytes)","am64xx-hsevm: Bandwidth (Mbits/sec)"

    "8","173"
    "16","383"
    "32","524"
    "64","930"
    "128","936"
    "256","939"

- Command: iperf3 -c $server_ip -w $window_size
- PCIe-Ethernet Card being used: Intel\ |reg| 82574L Gigabit Ethernet Controller

PCIe-NVMe-SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mibytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mibytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "4k","81.4","51.17","126","50.86"
    "256k","384.00","24.72","406.00","16.67"
    "1m","384.00","17.43","407.00","13.70"
    "4m","384.00","14.18","407.00","10.68"

- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based 
- Negotiated Link Speed and Link Width: Speed 5GT/s, Width x1
- SSD being used: Intel Optane NVMe SSD 900P

|

OSPI Flash Driver
-------------------------


AM64XX-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am64xx-hsevm: Raw Read Throughput (Mbytes/sec)"

    "50","138.89"

 
 

 

 

 
 

 





|

EMMC Driver
-------------------------

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

 

 

 

 


AM64XX-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "1m","61.10","3.52","175.00","6.79"
    "4m","61.20","2.66","175.00","4.96"
    "4k","50.90","46.06","55.70","40.65"
    "256k","61.00","5.45","174.00","7.66"






 

 


 

 

 

 
 

 



|

MMC/SD Driver
-------------------------

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

 

 

 

 

 


AM64XX-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "1m","19.30","1.75","87.20","4.46"
    "4m","18.60","1.40","85.60","3.23"
    "4k","4.24","8.79","13.60","13.00"
    "256k","18.30","2.49","82.70","4.52"



 



 

 

 

 

 

 

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

 

  



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am64xx-hsevm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","23334.23"
    "aes-128-cbc","16","356.12"
    "aes-128-cbc","16384","140585.64"
    "aes-128-cbc","256","6336.34"
    "aes-128-cbc","64","1579.33"
    "aes-128-cbc","8192","101840.21"
    "aes-128-ecb","1024","23933.61"
    "aes-128-ecb","16","338.18"
    "aes-128-ecb","16384","145620.99"
    "aes-128-ecb","256","6409.90"
    "aes-128-ecb","64","1583.30"
    "aes-128-ecb","8192","104958.63"
    "aes-192-cbc","1024","23362.22"
    "aes-192-cbc","16","354.55"
    "aes-192-cbc","16384","131104.77"
    "aes-192-cbc","256","6394.79"
    "aes-192-cbc","64","1586.30"
    "aes-192-cbc","8192","98713.60"
    "aes-192-ecb","1024","21278.38"
    "aes-192-ecb","16","363.35"
    "aes-192-ecb","16384","136009.05"
    "aes-192-ecb","256","6246.40"
    "aes-192-ecb","64","1589.70"
    "aes-192-ecb","8192","100027.05"
    "aes-256-cbc","1024","21395.11"
    "aes-256-cbc","16","355.57"
    "aes-256-cbc","16384","123677.35"
    "aes-256-cbc","256","5905.07"
    "aes-256-cbc","64","1506.39"
    "aes-256-cbc","8192","94658.56"
    "aes-256-ecb","1024","23214.76"
    "aes-256-ecb","16","338.69"
    "aes-256-ecb","16384","129504.60"
    "aes-256-ecb","256","5907.97"
    "aes-256-ecb","64","1475.67"
    "aes-256-ecb","8192","97487.53"
    "sha256","1024","24079.36"
    "sha256","16","403.53"
    "sha256","16384","193380.35"
    "sha256","256","6315.95"
    "sha256","64","1599.79"
    "sha256","8192","130351.10"
    "sha512","1024","17104.55"
    "sha512","16","388.51"
    "sha512","16384","48103.42"
    "sha512","256","5583.79"
    "sha512","64","1551.77"
    "sha512","8192","42786.82"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am64xx-hsevm: CPU Load"

    "aes-128-cbc","46.00"
    "aes-128-ecb","47.00"
    "aes-192-cbc","46.00"
    "aes-192-ecb","46.00"
    "aes-256-cbc","44.00"
    "aes-256-ecb","45.00"
    "sha256","97.00"
    "sha512","97.00"

 

Listed for each algorithm are the code snippets used to run each benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc
