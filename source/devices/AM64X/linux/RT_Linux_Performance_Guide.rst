###################################
RT-linux 12.00.00 Performance Guide
###################################

***************
Read This First
***************

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+---------------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                         |
+================+=====================================================================================================================+
| AM64x EVM      | AM64x Evaluation Module rev E1 with ARM running at 1GHz, DDR data rate 1600 MT/S                                    |
+----------------+---------------------------------------------------------------------------------------------------------------------+

Table:  Evaluation Modules

*****************
About This Manual
*****************

This document provides performance data for each of the device drivers
which are part of the Processor SDK Linux package. This document should be
used in conjunction with release notes and user guides provided with the
Processor SDK Linux package for information on specific issues present
with drivers included in a particular release.

For further information or to report any problems, contact
https://e2e.ti.com/ or https://support.ti.com/

|

*****************
System Benchmarks
*****************

|

LMBench
=======

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

    "af_unix_sock_stream_latency (microsec)","29.27 (min 24.87, max 39.15)"
    "af_unix_socket_stream_bandwidth (mb\s)","558.67 (min 544.62, max 577.21)"
    "bw_file_rd-io-1mb (mb/s)","842.86 (min 820.61, max 860.44)"
    "bw_file_rd-o2c-1mb (mb/s)","494.65 (min 478.77, max 505.56)"
    "bw_mem-bcopy-16mb (mb/s)","949.99 (min 921.34, max 973.47)"
    "bw_mem-bcopy-1mb (mb/s)","943.11 (min 906.76, max 975.93)"
    "bw_mem-bcopy-2mb (mb/s)","933.38 (min 918.70, max 958.47)"
    "bw_mem-bcopy-4mb (mb/s)","960.36 (min 924.21, max 978.47)"
    "bw_mem-bcopy-8mb (mb/s)","954.73 (min 901.51, max 986.19)"
    "bw_mem-bzero-16mb (mb/s)","2117.57 (min 2115.56, max 2118.36)"
    "bw_mem-bzero-1mb (mb/s)","1530.94 (min 906.76, max 2120.52)"
    "bw_mem-bzero-2mb (mb/s)","1525.61 (min 918.70, max 2118.64)"
    "bw_mem-bzero-4mb (mb/s)","1538.69 (min 924.21, max 2117.90)"
    "bw_mem-bzero-8mb (mb/s)","1536.19 (min 901.51, max 2118.92)"
    "bw_mem-cp-16mb (mb/s)","561.34 (min 542.93, max 581.71)"
    "bw_mem-cp-1mb (mb/s)","1606.01 (min 557.72, max 2718.38)"
    "bw_mem-cp-2mb (mb/s)","1439.68 (min 534.62, max 2352.94)"
    "bw_mem-cp-4mb (mb/s)","1383.16 (min 524.25, max 2227.17)"
    "bw_mem-cp-8mb (mb/s)","1359.16 (min 537.42, max 2167.43)"
    "bw_mem-fcp-16mb (mb/s)","1043.67 (min 1008.64, max 1082.84)"
    "bw_mem-fcp-1mb (mb/s)","1605.66 (min 1081.08, max 2120.52)"
    "bw_mem-fcp-2mb (mb/s)","1568.44 (min 966.81, max 2118.64)"
    "bw_mem-fcp-4mb (mb/s)","1582.47 (min 951.70, max 2117.90)"
    "bw_mem-fcp-8mb (mb/s)","1571.60 (min 959.23, max 2118.92)"
    "bw_mem-frd-16mb (mb/s)","1311.63 (min 1279.49, max 1329.57)"
    "bw_mem-frd-1mb (mb/s)","1200.07 (min 1081.08, max 1331.78)"
    "bw_mem-frd-2mb (mb/s)","1168.93 (min 966.81, max 1370.33)"
    "bw_mem-frd-4mb (mb/s)","1181.54 (min 951.70, max 1369.63)"
    "bw_mem-frd-8mb (mb/s)","1170.23 (min 959.23, max 1367.05)"
    "bw_mem-fwr-16mb (mb/s)","2128.04 (min 2125.96, max 2129.93)"
    "bw_mem-fwr-1mb (mb/s)","1965.95 (min 1273.19, max 2718.38)"
    "bw_mem-fwr-2mb (mb/s)","1819.17 (min 1265.22, max 2352.94)"
    "bw_mem-fwr-4mb (mb/s)","1760.80 (min 1275.31, max 2227.17)"
    "bw_mem-fwr-8mb (mb/s)","1737.99 (min 1241.85, max 2167.43)"
    "bw_mem-rd-16mb (mb/s)","1332.85 (min 1270.14, max 1382.89)"
    "bw_mem-rd-1mb (mb/s)","1102.66 (min 850.77, max 1419.88)"
    "bw_mem-rd-2mb (mb/s)","1086.05 (min 821.81, max 1365.89)"
    "bw_mem-rd-4mb (mb/s)","1104.47 (min 856.62, max 1380.74)"
    "bw_mem-rd-8mb (mb/s)","1116.97 (min 863.84, max 1397.38)"
    "bw_mem-rdwr-16mb (mb/s)","878.96 (min 870.37, max 884.08)"
    "bw_mem-rdwr-1mb (mb/s)","698.17 (min 557.72, max 847.46)"
    "bw_mem-rdwr-2mb (mb/s)","684.70 (min 534.62, max 828.16)"
    "bw_mem-rdwr-4mb (mb/s)","697.23 (min 524.25, max 855.25)"
    "bw_mem-rdwr-8mb (mb/s)","713.67 (min 537.42, max 878.54)"
    "bw_mem-wr-16mb (mb/s)","898.11 (min 890.57, max 901.46)"
    "bw_mem-wr-1mb (mb/s)","835.61 (min 768.34, max 890.31)"
    "bw_mem-wr-2mb (mb/s)","823.57 (min 790.62, max 852.64)"
    "bw_mem-wr-4mb (mb/s)","850.08 (min 805.07, max 878.64)"
    "bw_mem-wr-8mb (mb/s)","875.81 (min 858.74, max 897.87)"
    "bw_mmap_rd-mo-1mb (mb/s)","1288.67 (min 1251.79, max 1327.27)"
    "bw_mmap_rd-o2c-1mb (mb/s)","503.15 (min 477.40, max 532.86)"
    "bw_pipe (mb/s)","559.24 (min 519.56, max 584.19)"
    "bw_unix (mb/s)","558.67 (min 544.62, max 577.21)"
    "lat_connect (us)","69.65 (min 68.59, max 71.76)"
    "lat_ctx-2-128k (us)","17.41 (min 8.52, max 35.96)"
    "lat_ctx-2-256k (us)","59.43 (min 18.26, max 137.82)"
    "lat_ctx-4-128k (us)","33.39 (min 10.30, max 79.35)"
    "lat_ctx-4-256k (us)","57.09 (min 5.26, max 145.73)"
    "lat_fs-0k (num_files)","222.33 (min 204.00, max 253.00)"
    "lat_fs-10k (num_files)","97.33 (min 88.00, max 117.00)"
    "lat_fs-1k (num_files)","138.83 (min 128.00, max 152.00)"
    "lat_fs-4k (num_files)","129.17 (min 126.00, max 135.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","46.99 (min 46.70, max 48.08)"
    "lat_mem_rd-stride128-sz125k (ns)","7.81 (min 7.80, max 7.85)"
    "lat_mem_rd-stride128-sz250k (ns)","13.11 (min 10.29, max 17.26)"
    "lat_mem_rd-stride128-sz31k (ns)","4.69 (min 3.06, max 5.89)"
    "lat_mem_rd-stride128-sz50 (ns)","3.02"
    "lat_mem_rd-stride128-sz500k (ns)","42.92 (min 42.10, max 44.04)"
    "lat_mem_rd-stride128-sz62k (ns)","7.37 (min 7.35, max 7.39)"
    "lat_mmap-1m (us)","61.50 (min 58.00, max 71.00)"
    "lat_ops-double-add (ns)","4.02"
    "lat_ops-double-div (ns)","22.13 (min 22.12, max 22.14)"
    "lat_ops-double-mul (ns)","4.02"
    "lat_ops-float-add (ns)","4.02"
    "lat_ops-float-div (ns)","13.08 (min 13.06, max 13.11)"
    "lat_ops-float-mul (ns)","4.02"
    "lat_ops-int-add (ns)","1.01"
    "lat_ops-int-bit (ns)","0.67"
    "lat_ops-int-div (ns)","6.04 (min 6.03, max 6.05)"
    "lat_ops-int-mod (ns)","6.38 (min 6.37, max 6.40)"
    "lat_ops-int-mul (ns)","4.34 (min 4.27, max 4.38)"
    "lat_ops-int64-add (ns)","1.01"
    "lat_ops-int64-bit (ns)","0.67"
    "lat_ops-int64-div (ns)","9.55"
    "lat_ops-int64-mod (ns)","7.38 (min 7.37, max 7.38)"
    "lat_ops-int64-mul (ns)","5.05 (min 4.98, max 5.11)"
    "lat_pagefault (us)","1.66 (min 1.57, max 1.75)"
    "lat_pipe (us)","21.07 (min 20.07, max 21.69)"
    "lat_proc-exec (us)","1192.27 (min 1137.20, max 1275.60)"
    "lat_proc-fork (us)","1074.68 (min 1031.00, max 1137.60)"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","42.85 (min 42.28, max 43.92)"
    "lat_sem (us)","2.57 (min 1.71, max 3.19)"
    "lat_sig-catch (us)","6.09 (min 5.83, max 6.30)"
    "lat_sig-install (us)","0.94 (min 0.87, max 1.10)"
    "lat_sig-prot (us)","0.81 (min 0.66, max 0.94)"
    "lat_syscall-fstat (us)","2.31 (min 2.13, max 2.49)"
    "lat_syscall-null (us)","0.52 (min 0.44, max 0.65)"
    "lat_syscall-open (us)","345.64 (min 311.94, max 360.53)"
    "lat_syscall-read (us)","0.80 (min 0.69, max 0.89)"
    "lat_syscall-stat (us)","5.88 (min 5.61, max 6.20)"
    "lat_syscall-write (us)","0.76 (min 0.66, max 0.87)"
    "lat_tcp (us)","0.97 (min 0.75, max 1.22)"
    "lat_unix (us)","29.27 (min 24.87, max 39.15)"
    "latency_for_0.50_mb_block_size (nanosec)","42.92 (min 42.10, max 44.04)"
    "latency_for_1.00_mb_block_size (nanosec)","23.50 (min 0.00, max 48.08)"
    "pipe_bandwidth (mb\s)","559.24 (min 519.56, max 584.19)"
    "pipe_latency (microsec)","21.07 (min 20.07, max 21.69)"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","42.85 (min 42.28, max 43.92)"
    "semaphore_latency (microsec)","2.57 (min 1.71, max 3.19)"
    "signal_handler_latency (microsec)","0.94 (min 0.87, max 1.10)"
    "signal_handler_overhead (microsec)","6.09 (min 5.83, max 6.30)"
    "tcp_ip_connection_cost_to_localhost (microsec)","69.65 (min 68.59, max 71.76)"
    "tcp_latency_using_localhost (microsec)","0.97 (min 0.75, max 1.22)"

Dhrystone
=========

Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed. For standard ARM
cores the DMIPS/MHz score will be identical with the same compiler and flags.

.. csv-table:: Dhrystone Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "cpu_clock (mhz)","1000.00"
    "dhrystone_per_mhz (dmips/mhz)","2.76 (min 2.70, max 2.80)"
    "dhrystone_per_second (dhrystonep)","4855981.60 (min 4761905.00, max 5000000.00)"

Whetstone
=========

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "whetstone (mips)","3611.08 (min 3333.30, max 5000.00)"

Linpack
=======

Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "linpack (kflops)","411621.33 (min 411424.00, max 411819.00)"

CoreMarkPro
===========

CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "cjpeg-rose7-preset (workloads/)","29.60 (min 29.41, max 29.85)"
    "core (workloads/)","0.21"
    "coremark-pro ()","592.17 (min 585.01, max 602.59)"
    "linear_alg-mid-100x100-sp (workloads/)","10.41 (min 10.38, max 10.43)"
    "loops-all-mid-10k-sp (workloads/)","0.48 (min 0.48, max 0.49)"
    "nnet_test (workloads/)","0.76 (min 0.76, max 0.77)"
    "parser-125k (workloads/)","5.61 (min 5.29, max 6.17)"
    "radix2-big-64k (workloads/)","20.77 (min 20.27, max 21.14)"
    "sha-test (workloads/)","57.80"
    "zip-test (workloads/)","15.75 (min 15.63, max 16.13)"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am64xx-hsevm: perf"

    "cjpeg-rose7-preset (workloads/)","58.09 (min 57.47, max 58.82)"
    "core (workloads/)","0.43"
    "coremark-pro ()","1037.34 (min 981.69, max 1065.66)"
    "linear_alg-mid-100x100-sp (workloads/)","20.81 (min 20.78, max 20.83)"
    "loops-all-mid-10k-sp (workloads/)","0.88"
    "nnet_test (workloads/)","1.53"
    "parser-125k (workloads/)","5.99 (min 4.91, max 6.99)"
    "radix2-big-64k (workloads/)","32.45 (min 31.58, max 33.23)"
    "sha-test (workloads/)","114.94"
    "zip-test (workloads/)","26.01 (min 14.39, max 28.57)"

|

Boot-time Measurement
=====================

Boot media: MMCSD
-----------------

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am64xx-hsevm: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","28.67 (min 22.45, max 36.73)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

Ethernet
========

Ethernet performance benchmarks were measured using :command:`netperf` 2.7.1 https://hewlettpackard.github.io/netperf/doc/netperf.html
Test procedures were modeled after those defined in RFC-2544:
https://tools.ietf.org/html/rfc2544, where the DUT is the TI device
and the "tester" used was a Linux PC. To produce consistent results,
it is recommended to carry out performance tests in a private network and to avoid
running NFS on the same interface used in the test. In these results,
CPU utilization was captured as the total percentage used across all cores on the device,
while running the performance test over one external interface.

UDP Throughput (0% loss) was measured by the procedure defined in RFC-2544 section 26.1: Throughput.
In this scenario, :command:`netperf` options burst_size (-b) and wait_time (-w) are used to limit bandwidth
during different trials of the test, with the goal of finding the highest rate at which
no loss is seen. For example, to limit bandwidth to 500Mbits/sec with 1472B datagram:

.. code-block:: console

   burst_size = <bandwidth (bits/sec)> / 8 (bits -> bytes) / <UDP datagram size> / 100 (seconds -> 10 ms)
   burst_size = 500000000 / 8 / 1472 / 100 = 425

   wait_time = 10 milliseconds (minimum supported by Linux PC used for testing)

UDP Throughput (possible loss) was measured by capturing throughput and packet loss statistics when
running the :command:`netperf` test with no bandwidth limit (remove -b/-w options).

In order to start a :command:`netperf` client on one device, the other device must have :command:`netserver` running.
To start :command:`netserver`:

.. code-block:: console

   netserver [-p <port_number>] [-4 (IPv4 addressing)] [-6 (IPv6 addressing)]

Running the following shell script from the DUT will trigger :command:`netperf` clients to measure
bidirectional TCP performance for 60 seconds and report CPU utilization. Parameter -k is used in
client commands to summarize selected statistics on their own line and -j is used to gain
additional timing measurements during the test.

.. code-block:: console

   #!/bin/bash
   for i in 1
   do
      netperf -H <tester ip> -j -c -l 60 -t TCP_STREAM --
         -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE &

      netperf -H <tester ip> -j -c -l 60 -t TCP_MAERTS --
         -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE &
   done

Running the following commands will trigger :command:`netperf` clients to measure UDP burst performance for
60 seconds at various burst/datagram sizes and report CPU utilization.

- For UDP egress tests, run :command:`netperf` client from DUT and start :command:`netserver` on tester.

.. code-block:: console

   netperf -H <tester ip> -j -c -l 60 -t UDP_STREAM -b <burst_size> -w <wait_time> -- -m <UDP datagram size>
      -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE

- For UDP ingress tests, run :command:`netperf` client from tester and start :command:`netserver` on DUT.

.. code-block:: console

   netperf -H <DUT ip> -j -C -l 60 -t UDP_STREAM -b <burst_size> -w <wait_time> -- -m <UDP datagram size>
      -k DIRECTION,THROUGHPUT,MEAN_LATENCY,LOCAL_CPU_UTIL,REMOTE_CPU_UTIL,LOCAL_BYTES_SENT,REMOTE_BYTES_RECVD,LOCAL_SEND_SIZE

CPSW/CPSW2g/CPSW3g Ethernet
---------------------------

- CPSW3g: AM64x

TCP Bidirectional Throughput
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1100.48 (min 1064.93, max 1125.49)","99.80 (min 99.68, max 99.87)"

TCP Bidirectional Throughput Interrupt Pacing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1129.68 (min 1104.10, max 1180.26)","92.57 (min 77.95, max 98.21)"

UDP Throughput
^^^^^^^^^^^^^^

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","31.91 (min 16.92, max 46.99)","62.25 (min 33.00, max 92.00)","71.14 (min 54.01, max 87.52)"
    "128","","62.77 (min 33.94, max 92.73)","61.50 (min 33.00, max 91.00)","69.80 (min 52.96, max 86.37)"
    "256","","91.10 (min 53.10, max 171.91)","44.50 (min 26.00, max 84.00)","56.55 (min 31.44, max 87.70)"
    "1024","","420.23 (min 273.76, max 655.96)","51.00 (min 33.00, max 80.00)","66.26 (min 53.48, max 89.14)"
    "1518","","443.96 (min 254.51, max 628.95)","36.50 (min 21.00, max 52.00)","71.19 (min 53.13, max 89.29)"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "128","","4.89 (min 4.40, max 5.43)","4.50 (min 4.00, max 5.00)","2.05 (min 0.20, max 7.47)"
    "256","","10.60 (min 10.24, max 11.06)","5.00","1.86 (min 0.13, max 6.88)"
    "1024","","42.05 (min 41.78, max 42.60)","5.00","3.74 (min 0.94, max 7.58)"
    "1518","","63.29 (min 62.41, max 64.76)","5.00","7.24 (min 7.04, max 7.31)"

.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)","am64xx-hsevm: Packet Loss %"

    "128","","92.68 (min 84.84, max 97.29)","90.50 (min 83.00, max 95.00)","66.28 (min 64.69, max 67.86)","72.37 (min 68.17, max 79.35)"
    "256","","190.43 (min 175.08, max 202.24)","93.00 (min 85.00, max 99.00)","67.43 (min 65.94, max 68.79)","69.29 (min 67.47, max 71.90)"
    "1024","","586.35 (min 540.95, max 621.28)","71.67 (min 66.00, max 76.00)","66.59 (min 65.50, max 68.59)","30.88 (min 27.41, max 35.21)"
    "1518","","634.14 (min 592.61, max 686.45)","53.75 (min 50.00, max 58.00)","65.50 (min 64.50, max 66.73)","32.49 (min 28.27, max 35.88)"

ICSSG Ethernet
--------------

TCP Bidirectional Throughput
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: ICSSG TCP Bidirectional Throughput
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_MAERTS","812.01 (min 355.31, max 1121.74)","83.12 (min 74.78, max 99.72)"

TCP Bidirectional Throughput Interrupt Pacing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: ICSSG TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.2.1 -j -c -C -l 60 -t TCP_MAERTS","528.47 (min 363.92, max 1021.70)","50.15 (min 38.53, max 84.08)"

UDP Egress Throughput
^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: ICSSG UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","18.70 (min 16.63, max 19.65)","36.25 (min 32.00, max 38.00)","53.66 (min 53.49, max 53.81)"
    "128","","37.99 (min 35.64, max 39.58)","37.25 (min 35.00, max 39.00)","53.92 (min 53.64, max 54.23)"
    "256","","122.26 (min 70.86, max 173.65)","59.75 (min 35.00, max 85.00)","71.04 (min 53.56, max 89.45)"
    "1024","","421.89 (min 20.48, max 646.48)","51.67 (min 3.00, max 79.00)","59.85 (min 0.95, max 89.47)"
    "1472","","225.95 (min 9.42, max 866.11)","19.25 (min 1.00, max 74.00)","23.84 (min 0.19, max 88.88)"

UDP Ingress Throughput
^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: ICSSG UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am64xx-hsevm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am64xx-hsevm: THROUGHPUT (Mbits/sec)","am64xx-hsevm: Packets Per Second (kPPS)","am64xx-hsevm: CPU Load %"

    "64","","1.55 (min 1.43, max 1.64)","3.00","2.63 (min 0.19, max 6.18)"
    "128","","4.43 (min 4.30, max 4.71)","4.25 (min 4.00, max 5.00)","1.16 (min 0.22, max 2.30)"
    "256","","10.14 (min 9.63, max 10.65)","5.00","4.54 (min 0.32, max 6.49)"
    "1024","","43.22 (min 42.60, max 43.42)","5.00","6.99 (min 5.41, max 9.72)"
    "1472","","99.50 (min 61.23, max 181.34)","8.25 (min 5.00, max 15.00)","11.03 (min 6.91, max 20.94)"

|

OSPI
====

OSPI RAW
--------

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am64xx-hsevm: Raw Read Throughput (Mbytes/sec)"

    "50","120.03 (min 34.72, max 142.86)"

|

EMMC
====

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

EMMC EXT4 FIO 1G
----------------

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "1m","60.85 (min 59.80, max 61.40)","4.01 (min 3.82, max 4.19)","175.00","7.54 (min 6.84, max 8.58)"
    "4m","60.92 (min 60.10, max 61.70)","3.00 (min 2.94, max 3.09)","175.00","6.21 (min 6.08, max 6.67)"
    "4k","51.03 (min 50.40, max 51.40)","47.71 (min 47.11, max 48.21)","56.20 (min 55.90, max 56.50)","43.39 (min 42.04, max 44.59)"
    "256k","60.88 (min 59.70, max 61.40)","5.90 (min 5.76, max 6.02)","174.00","8.94 (min 8.35, max 9.48)"

EMMC EXT4
---------

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "102400","53.52 (min 50.76, max 55.23)","10.85 (min 9.02, max 15.05)","177.10 (min 170.77, max 178.65)","29.75 (min 26.36, max 31.19)"
    "262144","53.44 (min 49.12, max 55.01)","11.09 (min 9.71, max 14.70)","180.91 (min 177.95, max 182.21)","30.50 (min 27.93, max 33.04)"
    "524288","53.65 (min 49.96, max 55.45)","10.94 (min 9.33, max 14.80)","182.81 (min 182.59, max 182.93)","27.26 (min 24.55, max 28.83)"
    "1048576","53.88 (min 49.84, max 55.29)","10.68 (min 9.47, max 14.43)","182.82 (min 182.64, max 182.99)","28.13 (min 25.89, max 29.46)"
    "5242880","54.16 (min 49.90, max 55.64)","10.63 (min 9.14, max 14.63)","182.84 (min 182.76, max 182.90)","27.89 (min 27.03, max 28.57)"

EMMC VFAT
---------

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am64xx-hsevm: Write VFAT Throughput (Mbytes/sec)","am64xx-hsevm: Write VFAT CPU Load (%)","am64xx-hsevm: Read VFAT Throughput (Mbytes/sec)","am64xx-hsevm: Read VFAT CPU Load (%)"

    "102400","48.54 (min 40.00, max 51.49)","12.98 (min 10.62, max 19.53)","168.22 (min 167.35, max 168.71)","31.87 (min 28.81, max 34.48)"
    "262144","50.03 (min 40.70, max 53.63)","13.61 (min 11.41, max 19.72)","169.22 (min 167.80, max 170.47)","30.98 (min 27.27, max 37.82)"
    "524288","49.42 (min 39.94, max 52.77)","13.40 (min 11.16, max 19.84)","168.08 (min 166.94, max 169.46)","27.37 (min 25.20, max 28.69)"
    "1048576","48.91 (min 40.22, max 51.96)","13.10 (min 10.95, max 19.49)","166.64 (min 165.06, max 168.68)","27.83 (min 25.62, max 28.80)"
    "5242880","49.84 (min 40.55, max 54.04)","13.15 (min 11.19, max 19.67)","166.79 (min 165.93, max 167.42)","28.51 (min 27.87, max 29.03)"

UBoot EMMC
----------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am64xx-hsevm: Write Throughput (Kbytes/sec)","am64xx-hsevm: Read Throughput (Kbytes/sec)"

    "2000000","59848.32 (min 58724.01, max 61134.33)","169053.08 (min 168907.22, max 169782.38)"
    "4000000","60759.37 (min 59308.60, max 61651.93)","172614.84 (min 172463.16, max 172918.21)"

MMCSD
=====

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

MMC EXT4 FIO 1G
---------------

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am64xx-hsevm: Write EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Write EXT4 CPU Load (%)","am64xx-hsevm: Read EXT4 Throughput (Mbytes/sec)","am64xx-hsevm: Read EXT4 CPU Load (%)"

    "1m","42.42 (min 41.30, max 44.00)","3.46 (min 3.11, max 3.71)","86.77 (min 84.80, max 87.90)","5.25 (min 5.00, max 5.40)"
    "4m","41.77 (min 40.30, max 42.70)","2.57 (min 2.51, max 2.68)","85.97 (min 82.60, max 87.30)","3.78 (min 3.35, max 4.18)"
    "4k","2.77 (min 2.72, max 2.81)","6.96 (min 6.71, max 7.31)","12.82 (min 12.70, max 12.90)","12.76 (min 12.13, max 13.58)"
    "256k","38.15 (min 37.80, max 38.70)","4.64 (min 4.50, max 4.76)","83.47 (min 83.10, max 83.90)","6.51 (min 6.19, max 7.09)"

MMC EXT4
--------

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am64xx-hsevm: Write Raw Throughput (Mbytes/sec)","am64xx-hsevm: Write Raw CPU Load (%)","am64xx-hsevm: Read Raw Throughput (Mbytes/sec)","am64xx-hsevm: Read Raw CPU Load (%)"

    "102400","28.91 (min 27.03, max 32.81)","5.91 (min 4.58, max 8.99)","39.25 (min 37.68, max 40.92)","7.04 (min 6.25, max 7.95)"
    "262144","28.72 (min 27.22, max 32.30)","6.29 (min 4.81, max 8.97)","41.56 (min 39.87, max 42.87)","6.69 (min 6.28, max 7.44)"
    "524288","29.68 (min 28.38, max 32.45)","6.11 (min 4.99, max 9.66)","45.38 (min 45.00, max 45.57)","6.76 (min 6.05, max 7.38)"
    "1048576","30.06 (min 28.89, max 32.57)","6.01 (min 4.93, max 8.69)","45.34 (min 45.16, max 45.45)","6.75 (min 6.33, max 7.17)"
    "5242880","31.13 (min 28.88, max 33.47)","6.14 (min 4.65, max 9.08)","45.36 (min 45.00, max 45.55)","6.87 (min 6.37, max 7.21)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

|

CRYPTO
======

OpenSSL Performance
-------------------

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am64xx-hsevm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","23012.35"
    "aes-128-cbc","16","345.75"
    "aes-128-cbc","16384","138062.51"
    "aes-128-cbc","256","5988.95"
    "aes-128-cbc","64","1506.60"
    "aes-128-cbc","8192","100433.92"
    "aes-128-ecb","1024","22891.52"
    "aes-128-ecb","16","345.72"
    "aes-128-ecb","16384","144796.33"
    "aes-128-ecb","256","5978.97"
    "aes-128-ecb","64","1483.33"
    "aes-128-ecb","8192","105411.93"
    "aes-192-cbc","1024","22946.13"
    "aes-192-cbc","16","322.59"
    "aes-192-cbc","16384","130547.71"
    "aes-192-cbc","256","5987.33"
    "aes-192-cbc","64","1483.73"
    "aes-192-cbc","8192","96985.09"
    "aes-192-ecb","1024","23038.29"
    "aes-192-ecb","16","323.43"
    "aes-192-ecb","16384","132852.39"
    "aes-192-ecb","256","5995.86"
    "aes-192-ecb","64","1401.62"
    "aes-192-ecb","8192","100335.62"
    "aes-256-cbc","1024","20581.72"
    "aes-256-cbc","16","320.95"
    "aes-256-cbc","16384","122339.33"
    "aes-256-cbc","256","5605.12"
    "aes-256-cbc","64","1392.06"
    "aes-256-cbc","8192","92940.97"
    "aes-256-ecb","1024","21534.04"
    "aes-256-ecb","16","326.69"
    "aes-256-ecb","16384","127320.06"
    "aes-256-ecb","256","5676.46"
    "aes-256-ecb","64","1498.28"
    "aes-256-ecb","8192","97176.23"
    "sha256","1024","24602.62"
    "sha256","16","407.77"
    "sha256","16384","206176.26"
    "sha256","256","6433.96"
    "sha256","64","1622.78"
    "sha256","8192","137366.19"
    "sha512","1024","20061.53"
    "sha512","16","393.69"
    "sha512","16384","79216.64"
    "sha512","256","5904.04"
    "sha512","64","1574.76"
    "sha512","8192","65959.25"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am64xx-hsevm: CPU Load"

    "aes-128-cbc","44.00"
    "aes-128-ecb","45.00"
    "aes-192-cbc","43.00"
    "aes-192-ecb","44.00"
    "aes-256-cbc","42.00"
    "aes-256-ecb","43.00"
    "sha256","94.00"
    "sha512","94.00"

Listed for each algorithm are the code snippets used to run each benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

|
