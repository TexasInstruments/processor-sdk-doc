======================================
 RT-linux 10.01 Performance Guide
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

    "af_unix_sock_stream_latency (microsec)","37.24"
    "af_unix_socket_stream_bandwidth (MBs)","560.42"
    "bw_file_rd-io-1mb (MB/s)","852.66"
    "bw_file_rd-o2c-1mb (MB/s)","491.72"
    "bw_mem-bcopy-16mb (MB/s)","844.28"
    "bw_mem-bcopy-1mb (MB/s)","963.70"
    "bw_mem-bcopy-2mb (MB/s)","939.70"
    "bw_mem-bcopy-4mb (MB/s)","993.42"
    "bw_mem-bcopy-8mb (MB/s)","1038.56"
    "bw_mem-bzero-16mb (MB/s)","2120.33"
    "bw_mem-bzero-1mb (MB/s)","1537.82 (min 963.70, max 2111.93)"
    "bw_mem-bzero-2mb (MB/s)","1529.74 (min 939.70, max 2119.77)"
    "bw_mem-bzero-4mb (MB/s)","1556.78 (min 993.42, max 2120.14)"
    "bw_mem-bzero-8mb (MB/s)","1578.89 (min 1038.56, max 2119.21)"
    "bw_mem-cp-16mb (MB/s)","519.83"
    "bw_mem-cp-1mb (MB/s)","1595.51 (min 531.44, max 2659.57)"
    "bw_mem-cp-2mb (MB/s)","1453.00 (min 528.82, max 2377.18)"
    "bw_mem-cp-4mb (MB/s)","1388.31 (min 548.62, max 2228.00)"
    "bw_mem-cp-8mb (MB/s)","1380.94 (min 597.95, max 2163.92)"
    "bw_mem-fcp-16mb (MB/s)","895.10"
    "bw_mem-fcp-1mb (MB/s)","1609.47 (min 1107.01, max 2111.93)"
    "bw_mem-fcp-2mb (MB/s)","1599.46 (min 1079.14, max 2119.77)"
    "bw_mem-fcp-4mb (MB/s)","1573.62 (min 1027.09, max 2120.14)"
    "bw_mem-fcp-8mb (MB/s)","1592.66 (min 1066.10, max 2119.21)"
    "bw_mem-frd-16mb (MB/s)","1274.39"
    "bw_mem-frd-1mb (MB/s)","1200.22 (min 1107.01, max 1293.42)"
    "bw_mem-frd-2mb (MB/s)","1207.35 (min 1079.14, max 1335.56)"
    "bw_mem-frd-4mb (MB/s)","1194.63 (min 1027.09, max 1362.17)"
    "bw_mem-frd-8mb (MB/s)","1210.10 (min 1066.10, max 1354.10)"
    "bw_mem-fwr-16mb (MB/s)","2130.49"
    "bw_mem-fwr-1mb (MB/s)","1976.50 (min 1293.42, max 2659.57)"
    "bw_mem-fwr-2mb (MB/s)","1856.37 (min 1335.56, max 2377.18)"
    "bw_mem-fwr-4mb (MB/s)","1795.09 (min 1362.17, max 2228.00)"
    "bw_mem-fwr-8mb (MB/s)","1759.01 (min 1354.10, max 2163.92)"
    "bw_mem-rd-16mb (MB/s)","1361.01"
    "bw_mem-rd-1mb (MB/s)","1105.38 (min 859.40, max 1351.35)"
    "bw_mem-rd-2mb (MB/s)","1107.70 (min 843.41, max 1371.98)"
    "bw_mem-rd-4mb (MB/s)","1104.06 (min 856.07, max 1352.04)"
    "bw_mem-rd-8mb (MB/s)","1121.62 (min 890.97, max 1352.27)"
    "bw_mem-rdwr-16mb (MB/s)","876.71"
    "bw_mem-rdwr-1mb (MB/s)","672.03 (min 531.44, max 812.61)"
    "bw_mem-rdwr-2mb (MB/s)","664.04 (min 528.82, max 799.25)"
    "bw_mem-rdwr-4mb (MB/s)","677.29 (min 548.62, max 805.96)"
    "bw_mem-rdwr-8mb (MB/s)","713.49 (min 597.95, max 829.02)"
    "bw_mem-wr-16mb (MB/s)","895.26"
    "bw_mem-wr-1mb (MB/s)","836.01 (min 812.61, max 859.40)"
    "bw_mem-wr-2mb (MB/s)","821.33 (min 799.25, max 843.41)"
    "bw_mem-wr-4mb (MB/s)","831.02 (min 805.96, max 856.07)"
    "bw_mem-wr-8mb (MB/s)","860.00 (min 829.02, max 890.97)"
    "bw_mmap_rd-mo-1mb (MB/s)","1297.98"
    "bw_mmap_rd-o2c-1mb (MB/s)","489.96"
    "bw_pipe (MB/s)","540.92"
    "bw_unix (MB/s)","560.42"
    "lat_connect (us)","86.38"
    "lat_ctx-2-128k (us)","5.52"
    "lat_ctx-2-256k (us)","19.77"
    "lat_ctx-4-128k (us)","6.16"
    "lat_ctx-4-256k (us)","0.00"
    "lat_fs-0k (num_files)","147.00"
    "lat_fs-10k (num_files)","77.00"
    "lat_fs-1k (num_files)","112.00"
    "lat_fs-4k (num_files)","105.00"
    "lat_mem_rd-stride128-sz1000k (ns)","48.17"
    "lat_mem_rd-stride128-sz125k (ns)","7.85"
    "lat_mem_rd-stride128-sz250k (ns)","14.06"
    "lat_mem_rd-stride128-sz31k (ns)","5.13"
    "lat_mem_rd-stride128-sz50 (ns)","3.01"
    "lat_mem_rd-stride128-sz500k (ns)","43.77"
    "lat_mem_rd-stride128-sz62k (ns)","7.38"
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
    "lat_ops-int-mul (ns)","4.32"
    "lat_ops-int64-add (ns)","1.01"
    "lat_ops-int64-bit (ns)","0.67"
    "lat_ops-int64-div (ns)","9.54"
    "lat_ops-int64-mod (ns)","7.37"
    "lat_ops-int64-mul (ns)","4.99"
    "lat_pagefault (us)","1.55"
    "lat_pipe (us)","23.89"
    "lat_proc-exec (us)","1316.80"
    "lat_proc-fork (us)","993.00"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","48.89"
    "lat_sem (us)","2.09"
    "lat_sig-catch (us)","5.86"
    "lat_sig-install (us)","0.90"
    "lat_sig-prot (us)","1.38"
    "lat_syscall-fstat (us)","2.71"
    "lat_syscall-null (us)","0.58"
    "lat_syscall-open (us)","400.53"
    "lat_syscall-read (us)","1.01"
    "lat_syscall-stat (us)","6.89"
    "lat_syscall-write (us)","1.02"
    "lat_tcp (us)","1.21"
    "lat_unix (us)","37.24"
    "latency_for_0.50_mb_block_size (nanosec)","43.77"
    "latency_for_1.00_mb_block_size (nanosec)","24.09 (min 0.00, max 48.17)"
    "pipe_bandwidth (MBs)","540.92"
    "pipe_latency (microsec)","23.89"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","48.89"
    "semaphore_latency (microsec)","2.09"
    "signal_handler_latency (microsec)","0.90"
    "signal_handler_overhead (microsec)","5.86"
    "tcp_ip_connection_cost_to_localhost (microsec)","86.38"
    "tcp_latency_using_localhost (microsec)","1.21"

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

    "linpack (Kflops)","408074.00"

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

    "add (MB/s)","1626.90"
    "copy (MB/s)","2112.60"
    "scale (MB/s)","2263.80"
    "triad (MB/s)","1625.90"

CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "cjpeg-rose7-preset (workloads/)","29.76"
    "core (workloads/)","0.21"
    "coremark-pro ()","589.26"
    "linear_alg-mid-100x100-sp (workloads/)","10.41"
    "loops-all-mid-10k-sp (workloads/)","0.48"
    "nnet_test (workloads/)","0.77"
    "parser-125k (workloads/)","5.65"
    "radix2-big-64k (workloads/)","19.66"
    "sha-test (workloads/)","58.14"
    "zip-test (workloads/)","15.63"

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

    "4m-check (workloads/)","285.16"
    "4m-check-reassembly (workloads/)","64.06"
    "4m-check-reassembly-tcp (workloads/)","37.15"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","14.70"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","0.75"
    "4m-cmykw2 (workloads/)","86.39"
    "4m-cmykw2-rotatew2 (workloads/)","18.43"
    "4m-reassembly (workloads/)","57.08"
    "4m-rotatew2 (workloads/)","19.74"
    "4m-tcp-mixed (workloads/)","86.02"
    "4m-x264w2 (workloads/)","0.77"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","13.71"
    "idct-4mw1 (workloads/)","13.71"
    "ippktcheck-4m (workloads/)","285.36"
    "ippktcheck-4mw1 (workloads/)","285.52"
    "ipres-4m (workloads/)","73.10"
    "ipres-4mw1 (workloads/)","72.67"
    "md5-4m (workloads/)","20.81"
    "md5-4mw1 (workloads/)","21.35"
    "rgbcmyk-4m (workloads/)","44.85"
    "rgbcmyk-4mw1 (workloads/)","44.88"
    "rotate-4ms1 (workloads/)","16.82"
    "rotate-4ms1w1 (workloads/)","16.80"
    "rotate-4ms64 (workloads/)","16.97"
    "rotate-4ms64w1 (workloads/)","16.98"
    "x264-4mq (workloads/)","0.41"
    "x264-4mqw1 (workloads/)","0.41"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am64xx-hsevm: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","21.64 (min 20.54, max 22.65)"

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

    "64","18.00","3.27","23.00","18.94"
    "128","82.00","15.28","23.00","18.93"
    "256","210.00","32.93","20.00","17.54"
    "1024","978.00","213.50","27.00","40.65"
    "1518","1472.00","374.91","32.00","44.99"

|

PCIe Driver
-------------------------

PCIe-ETH
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: PCIe Ethernet performance
    :header: "TCP Window Size(Kbytes)","am64xx-hsevm: Bandwidth (Mbits/sec)"

    "8","0.00"
    "16","0.00"

PCIe-NVMe-SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^

AM64xx-EVM
"""""""""""""""""""""""""""

.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "1m","373.00","19.47","398.00","13.84"
    "4m","364.00","16.00","398.00","12.77"
    "4k","78.30","51.37","90.40","46.75"
    "256k","375.00","21.93","397.00","15.57"

- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based 
- Platform: Speed 8GT/s, Width x1
- SSD being used: Lite-On Technology Corporation M8Pe Series NVMe SSD [14a4:22f1] (rev 01)

|

OSPI Flash Driver
-------------------------

AM64XX-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am64xx-hsevm: Raw Read Throughput (Mbytes/sec)"

    "50","116.28"

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

    "1m","61.60","3.59","175.00","5.84"
    "4m","61.70","2.65","175.00","5.02"
    "4k","51.50","47.69","56.10","42.24"
    "256k","61.50","5.13","174.00","8.18"

EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "102400","54.39 (min 51.41, max 55.34)","11.14 (min 9.84, max 15.23)","180.51","30.91"
    "262144","53.42 (min 50.09, max 54.97)","10.55 (min 9.51, max 14.18)","173.07","31.03"
    "524288","54.12 (min 51.22, max 55.43)","10.58 (min 9.42, max 14.25)","182.13","28.18"
    "1048576","54.35 (min 51.25, max 55.19)","10.38 (min 9.21, max 14.22)","182.97","26.13"
    "5242880","54.45 (min 51.44, max 55.48)","10.48 (min 9.26, max 14.07)","182.94","27.03"

EMMC VFAT
^^^^^^^^^

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am64xx-hsevm: Write VFAT Throughput (Mbytes/sec)","am64xx-hsevm: Write VFAT CPU Load (%)","am64xx-hsevm: Read VFAT Throughput (Mbytes/sec)","am64xx-hsevm: Read VFAT CPU Load (%)"

    "102400","48.82 (min 40.94, max 50.98)","13.12 (min 11.49, max 19.09)","170.67","30.70"
    "262144","50.98 (min 42.47, max 53.58)","13.51 (min 11.70, max 19.72)","158.23","29.03"
    "524288","51.26 (min 42.72, max 53.89)","13.95 (min 11.83, max 19.47)","166.34","28.10"
    "1048576","51.61 (min 42.95, max 53.97)","13.31 (min 11.54, max 19.55)","170.29","26.45"
    "5242880","52.03 (min 43.35, max 54.33)","13.36 (min 11.66, max 19.54)","170.69","26.45"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am64xx-hsevm: Write Throughput (Kbytes/sec)","am64xx-hsevm: Read Throughput (Kbytes/sec)"

    "2000000","59795.62","168907.22"
    "4000000","60346.22","172463.16"

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

    "1m","42.60","3.21","87.30","4.34"
    "4m","42.00","2.43","82.30","3.11"
    "4k","2.77","7.10","12.90","13.10"
    "256k","38.40","4.29","84.00","5.09"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am64xx-hsevm: Write Raw Throughput (Mbytes/sec)","am64xx-hsevm: Write Raw CPU Load (%)","am64xx-hsevm: Read Raw Throughput (Mbytes/sec)","am64xx-hsevm: Read Raw CPU Load (%)"

    "102400","31.90 (min 30.56, max 33.46)","6.36 (min 5.54, max 8.81)","39.10","9.11"
    "262144","29.00 (min 28.17, max 30.62)","6.17 (min 5.28, max 8.68)","40.23","7.20"
    "524288","29.93 (min 29.14, max 30.39)","5.93 (min 4.99, max 8.46)","44.83","6.49"
    "1048576","32.19 (min 31.35, max 32.45)","6.33 (min 5.27, max 9.45)","45.45","6.36"
    "5242880","31.67 (min 30.97, max 32.28)","6.11 (min 5.41, max 8.61)","45.46","6.35"

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

    "aes-128-cbc","1024","22478.85"
    "aes-128-cbc","16","342.87"
    "aes-128-cbc","16384","138341.03"
    "aes-128-cbc","256","6090.67"
    "aes-128-cbc","64","1529.79"
    "aes-128-cbc","8192","100971.86"
    "aes-128-ecb","1024","22976.17"
    "aes-128-ecb","16","327.34"
    "aes-128-ecb","16384","143545.69"
    "aes-128-ecb","256","6251.69"
    "aes-128-ecb","64","1488.15"
    "aes-128-ecb","8192","104114.86"
    "aes-192-cbc","1024","22419.80"
    "aes-192-cbc","16","321.81"
    "aes-192-cbc","16384","130542.25"
    "aes-192-cbc","256","5873.41"
    "aes-192-cbc","64","1418.67"
    "aes-192-cbc","8192","96829.44"
    "aes-192-ecb","1024","22828.71"
    "aes-192-ecb","16","350.46"
    "aes-192-ecb","16384","135375.53"
    "aes-192-ecb","256","6228.05"
    "aes-192-ecb","64","1539.82"
    "aes-192-ecb","8192","98645.33"
    "aes-256-cbc","1024","20705.62"
    "aes-256-cbc","16","343.20"
    "aes-256-cbc","16384","121896.96"
    "aes-256-cbc","256","6080.17"
    "aes-256-cbc","64","1531.48"
    "aes-256-cbc","8192","91545.60"
    "aes-256-ecb","1024","22881.96"
    "aes-256-ecb","16","349.42"
    "aes-256-ecb","16384","126686.55"
    "aes-256-ecb","256","6222.85"
    "aes-256-ecb","64","1507.82"
    "aes-256-ecb","8192","95764.48"
    "sha256","1024","23239.68"
    "sha256","16","386.25"
    "sha256","16384","191376.04"
    "sha256","256","6049.37"
    "sha256","64","1530.39"
    "sha256","8192","127737.86"
    "sha512","1024","16603.82"
    "sha512","16","372.24"
    "sha512","16384","47824.90"
    "sha512","256","5363.71"
    "sha512","64","1488.15"
    "sha512","8192","42374.49"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am64xx-hsevm: CPU Load"

    "aes-128-cbc","46.00"
    "aes-128-ecb","47.00"
    "aes-192-cbc","45.00"
    "aes-192-ecb","47.00"
    "aes-256-cbc","45.00"
    "aes-256-ecb","47.00"
    "sha256","97.00"
    "sha512","97.00"

Listed for each algorithm are the code snippets used to run each benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","am64xx-hsevm: Throughput (Mbps)","am64xx-hsevm: Packets/Sec","am64xx-hsevm: CPU Load"

    "3des","52.80","4.00","52.54"
    "aes128","0.00","0.00","51.14"
