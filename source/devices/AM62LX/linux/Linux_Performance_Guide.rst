
====================================
 Linux 11.00.00.00 Performance Guide
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
    ./runltp -P am62lxx_evm-fs -f ddt/lmbench -s LMBENCH_L_PERF_0001

.. csv-table:: LMBench Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "af_unix_sock_stream_latency (microsec)","27.34"
    "af_unix_socket_stream_bandwidth (MBs)","458.06"
    "bw_file_rd-io-1mb (MB/s)","966.34"
    "bw_file_rd-o2c-1mb (MB/s)","500.17"
    "bw_mem-bcopy-16mb (MB/s)","741.63"
    "bw_mem-bcopy-1mb (MB/s)","743.63"
    "bw_mem-bcopy-2mb (MB/s)","720.85"
    "bw_mem-bcopy-4mb (MB/s)","767.17"
    "bw_mem-bcopy-8mb (MB/s)","798.88"
    "bw_mem-bzero-16mb (MB/s)","2186.69"
    "bw_mem-bzero-1mb (MB/s)","1464.71 (min 743.63, max 2185.79)"
    "bw_mem-bzero-2mb (MB/s)","1454.12 (min 720.85, max 2187.39)"
    "bw_mem-bzero-4mb (MB/s)","1477.28 (min 767.17, max 2187.39)"
    "bw_mem-bzero-8mb (MB/s)","1491.74 (min 798.88, max 2184.60)"
    "bw_mem-cp-16mb (MB/s)","419.34"
    "bw_mem-cp-1mb (MB/s)","1430.43 (min 452.56, max 2408.30)"
    "bw_mem-cp-2mb (MB/s)","1359.89 (min 428.45, max 2291.33)"
    "bw_mem-cp-4mb (MB/s)","1332.46 (min 441.45, max 2223.46)"
    "bw_mem-cp-8mb (MB/s)","1346.78 (min 466.39, max 2227.17)"
    "bw_mem-fcp-16mb (MB/s)","737.12"
    "bw_mem-fcp-1mb (MB/s)","1502.80 (min 819.81, max 2185.79)"
    "bw_mem-fcp-2mb (MB/s)","1489.95 (min 792.50, max 2187.39)"
    "bw_mem-fcp-4mb (MB/s)","1511.50 (min 835.60, max 2187.39)"
    "bw_mem-fcp-8mb (MB/s)","1513.84 (min 843.08, max 2184.60)"
    "bw_mem-frd-16mb (MB/s)","1283.49"
    "bw_mem-frd-1mb (MB/s)","1038.16 (min 819.81, max 1256.51)"
    "bw_mem-frd-2mb (MB/s)","1024.00 (min 792.50, max 1255.49)"
    "bw_mem-frd-4mb (MB/s)","1068.31 (min 835.60, max 1301.02)"
    "bw_mem-frd-8mb (MB/s)","1073.22 (min 843.08, max 1303.36)"
    "bw_mem-fwr-16mb (MB/s)","2209.03"
    "bw_mem-fwr-1mb (MB/s)","1832.41 (min 1256.51, max 2408.30)"
    "bw_mem-fwr-2mb (MB/s)","1773.41 (min 1255.49, max 2291.33)"
    "bw_mem-fwr-4mb (MB/s)","1762.24 (min 1301.02, max 2223.46)"
    "bw_mem-fwr-8mb (MB/s)","1765.27 (min 1303.36, max 2227.17)"
    "bw_mem-rd-16mb (MB/s)","1327.36"
    "bw_mem-rd-1mb (MB/s)","962.76 (min 610.22, max 1315.30)"
    "bw_mem-rd-2mb (MB/s)","932.32 (min 565.93, max 1298.70)"
    "bw_mem-rd-4mb (MB/s)","959.33 (min 625.20, max 1293.45)"
    "bw_mem-rd-8mb (MB/s)","1010.60 (min 711.87, max 1309.33)"
    "bw_mem-rdwr-16mb (MB/s)","712.28"
    "bw_mem-rdwr-1mb (MB/s)","504.42 (min 452.56, max 556.28)"
    "bw_mem-rdwr-2mb (MB/s)","498.08 (min 428.45, max 567.70)"
    "bw_mem-rdwr-4mb (MB/s)","504.86 (min 441.45, max 568.26)"
    "bw_mem-rdwr-8mb (MB/s)","594.44 (min 466.39, max 722.48)"
    "bw_mem-wr-16mb (MB/s)","757.86"
    "bw_mem-wr-1mb (MB/s)","583.25 (min 556.28, max 610.22)"
    "bw_mem-wr-2mb (MB/s)","566.82 (min 565.93, max 567.70)"
    "bw_mem-wr-4mb (MB/s)","596.73 (min 568.26, max 625.20)"
    "bw_mem-wr-8mb (MB/s)","717.18 (min 711.87, max 722.48)"
    "bw_mmap_rd-mo-1mb (MB/s)","1237.62"
    "bw_mmap_rd-o2c-1mb (MB/s)","495.38"
    "bw_pipe (MB/s)","399.08"
    "bw_unix (MB/s)","458.06"
    "lat_connect (us)","59.62"
    "lat_ctx-2-128k (us)","14.58"
    "lat_ctx-2-256k (us)","31.29"
    "lat_ctx-4-128k (us)","13.82"
    "lat_ctx-4-256k (us)","19.00"
    "lat_fs-0k (num_files)","217.00"
    "lat_fs-10k (num_files)","105.00"
    "lat_fs-1k (num_files)","152.00"
    "lat_fs-4k (num_files)","134.00"
    "lat_mem_rd-stride128-sz1000k (ns)","50.64"
    "lat_mem_rd-stride128-sz125k (ns)","6.21"
    "lat_mem_rd-stride128-sz250k (ns)","13.20"
    "lat_mem_rd-stride128-sz31k (ns)","3.90"
    "lat_mem_rd-stride128-sz50 (ns)","2.41"
    "lat_mem_rd-stride128-sz500k (ns)","44.90"
    "lat_mem_rd-stride128-sz62k (ns)","4.92"
    "lat_mmap-1m (us)","57.00"
    "lat_ops-double-add (ns)","3.21"
    "lat_ops-double-div (ns)","17.65"
    "lat_ops-double-mul (ns)","3.21"
    "lat_ops-float-add (ns)","3.21"
    "lat_ops-float-div (ns)","10.43"
    "lat_ops-float-mul (ns)","3.21"
    "lat_ops-int-add (ns)","0.80"
    "lat_ops-int-bit (ns)","0.54"
    "lat_ops-int-div (ns)","4.81"
    "lat_ops-int-mod (ns)","5.08"
    "lat_ops-int-mul (ns)","3.45"
    "lat_ops-int64-add (ns)","0.80"
    "lat_ops-int64-bit (ns)","0.54"
    "lat_ops-int64-div (ns)","7.62"
    "lat_ops-int64-mod (ns)","5.88"
    "lat_ops-int64-mul (ns)","3.98"
    "lat_pagefault (us)","0.95"
    "lat_pipe (us)","22.06"
    "lat_proc-exec (us)","1411.25"
    "lat_proc-fork (us)","1221.80"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","37.59"
    "lat_sem (us)","3.63"
    "lat_sig-catch (us)","5.82"
    "lat_sig-install (us)","0.79"
    "lat_sig-prot (us)","0.95"
    "lat_syscall-fstat (us)","2.00"
    "lat_syscall-null (us)","0.51"
    "lat_syscall-open (us)","555.70"
    "lat_syscall-read (us)","0.78"
    "lat_syscall-stat (us)","5.07"
    "lat_syscall-write (us)","0.75"
    "lat_tcp (us)","1.02"
    "lat_unix (us)","27.34"
    "latency_for_0.50_mb_block_size (nanosec)","44.90"
    "latency_for_1.00_mb_block_size (nanosec)","25.32 (min 0.00, max 50.64)"
    "pipe_bandwidth (MBs)","399.08"
    "pipe_latency (microsec)","22.06"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","37.59"
    "semaphore_latency (microsec)","3.63"
    "signal_handler_latency (microsec)","0.79"
    "signal_handler_overhead (microsec)","5.82"
    "tcp_ip_connection_cost_to_localhost (microsec)","59.62"
    "tcp_latency_using_localhost (microsec)","1.02"

Dhrystone
^^^^^^^^^
Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed.

Please take note, different runs may produce slightly different results.
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

    "linpack (Kflops)","514473.00"

NBench
^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "assignment (Iterations)","12.90"
    "fourier (Iterations)","20382.00"
    "fp_emulation (Iterations)","192.47"
    "huffman (Iterations)","1057.00"
    "idea (Iterations)","3075.00"
    "lu_decomposition (Iterations)","473.07"
    "neural_net (Iterations)","7.73"
    "numeric_sort (Iterations)","558.90"
    "string_sort (Iterations)","146.37"

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

    "add (MB/s)","1914.10"
    "copy (MB/s)","1993.60"
    "scale (MB/s)","2136.40"
    "triad (MB/s)","1890.70"

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
    "coremark-pro ()","725.83"
    "linear_alg-mid-100x100-sp (workloads/)","13.09"
    "loops-all-mid-10k-sp (workloads/)","0.60"
    "nnet_test (workloads/)","0.97"
    "parser-125k (workloads/)","7.09"
    "radix2-big-64k (workloads/)","20.48"
    "sha-test (workloads/)","72.46"
    "zip-test (workloads/)","19.61"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "cjpeg-rose7-preset (workloads/)","70.92"
    "core (workloads/)","0.53"
    "coremark-pro ()","1172.58"
    "linear_alg-mid-100x100-sp (workloads/)","25.85"
    "loops-all-mid-10k-sp (workloads/)","1.01"
    "nnet_test (workloads/)","1.90"
    "parser-125k (workloads/)","5.04"
    "radix2-big-64k (workloads/)","26.82"
    "sha-test (workloads/)","138.89"
    "zip-test (workloads/)","33.90"

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
Multi-Instance-Test Harness (MITH), compatible and portable with most multicore
processors and operating systems. MITH uses a thread-based API (POSIX-compliant) to
establish a common programming model that communicates with the benchmark through an
abstraction layer and provides a flexible interface to allow a wide variety of
thread-enabled workloads to be tested.

.. csv-table:: Multibench Benchmarks
    :header: "Benchmarks","am62lxx_evm-fs: perf"

    "4m-check (workloads/)","278.86"
    "4m-check-reassembly (workloads/)","54.26"
    "4m-check-reassembly-tcp (workloads/)","34.97"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","15.24"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","0.91"
    "4m-cmykw2 (workloads/)","108.11"
    "4m-cmykw2-rotatew2 (workloads/)","19.24"
    "4m-reassembly (workloads/)","49.75"
    "4m-rotatew2 (workloads/)","20.15"
    "4m-tcp-mixed (workloads/)","98.77"
    "4m-x264w2 (workloads/)","0.93"
    "empty-wld (workloads/)","1.00"
    "idct-4m (workloads/)","16.95"
    "idct-4mw1 (workloads/)","16.98"
    "ippktcheck-4m (workloads/)","278.68"
    "ippktcheck-4mw1 (workloads/)","278.46"
    "ipres-4m (workloads/)","65.56"
    "ipres-4mw1 (workloads/)","65.10"
    "md5-4m (workloads/)","19.24"
    "md5-4mw1 (workloads/)","19.94"
    "rgbcmyk-4m (workloads/)","56.37"
    "rgbcmyk-4mw1 (workloads/)","56.88"
    "rotate-4ms1 (workloads/)","18.33"
    "rotate-4ms1w1 (workloads/)","18.66"
    "rotate-4ms64 (workloads/)","18.49"
    "rotate-4ms64w1 (workloads/)","18.64"
    "x264-4mq (workloads/)","0.50"
    "x264-4mqw1 (workloads/)","0.50"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62lxx_evm-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","19.08 (min 18.56, max 19.56)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

ALSA SoC Audio Driver
---------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62lxx_evm-fs: Throughput (bits/sec)","am62lxx_evm-fs: CPU Load (%)"

    "8000","255999.00","0.86"
    "11025","352782.00","0.95"
    "16000","511974.00","0.82"
    "22050","705568.00","1.21"
    "24000","705570.00","1.18"

.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62lxx_evm-fs: Throughput (bits/sec)","am62lxx_evm-fs: CPU Load (%)"

    "8000","255336.00","0.78"
    "11025","352931.00","0.90"

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

.. rubric::  TCP Bidirectional Throughput
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1110.66","97.65"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62lxx_evm-fs: THROUGHPUT (Mbits/sec)","am62lxx_evm-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","317.24","32.85"

Linux OSPI Flash Driver
-----------------------

RAW
^^^

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62lxx_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","172.41"

UBIFS
^^^^^

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62lxx_evm-fs: Write UBIFS Throughput (Mbytes/sec)","am62lxx_evm-fs: Write UBIFS CPU Load (%)","am62lxx_evm-fs: Read UBIFS Throughput (Mbytes/sec)","am62lxx_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.28)","51.32 (min 50.77, max 51.89)","56.02","50.00"
    "262144","0.14 (min 0.11, max 0.19)","51.75 (min 50.99, max 53.37)","56.09","42.86"
    "524288","0.14 (min 0.11, max 0.19)","51.41 (min 50.80, max 52.05)","56.14","33.33"
    "1048576","0.14 (min 0.11, max 0.19)","51.64 (min 51.40, max 51.84)","53.84","37.50"

Linux QSPI/OSPI Driver
----------------------

.. csv-table::
    :header: "Flash","File Size","Read Throughput","Write Throughput"

    "OSPI NOR","50 MB","205 MB/s","403 KB/s"
    "QSPI NAND","50 MB","18.6 MB/s","4.9 MB/s"

U-Boot QSPI/OSPI Driver
-----------------------

.. csv-table::
    :header: "Flash","File Size","Read Throughput","Write Throughput"

    "OSPI NOR","50 MB","303 MB/s","167 KB/s"
    "QSPI NAND","50 MB","25.7 MB/s","5.5 MB/s"

Low Power Performance
---------------------

These are power measurements taken while the device is in various low power modes like
Deep Sleep and RTC Only + DDR.

Table:  **Deep sleep**

.. csv-table::
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.75", "4.88"
     "soc_dvdd_1v8", "1.80", "2.06"
     "soc_dvdd_3v3", "3.29", "2.50"
     "vdda_1v8", "1.80", "0.56"
     "vdd_lpddr4_pmic1", "1.10", "0.99"
     "vdd_rtc", "0.74", "0.01"
     "vdd_rtc_1v8", "1.80", "0.01"
     "Total"," ","~11.04"

Table:  **RTC Only + DDR**

.. csv-table::
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.00", "0.00"
     "soc_dvdd_1v8", "1.80", "1.23"
     "soc_dvdd_3v3", "3.29", "1.07"
     "vdda_1v8", "0.00", "0.00"
     "vdd_lpddr4_pmic1", "1.10", "1.00"
     "vdd_rtc", "0.75", "0.02"
     "vdd_rtc_1v8", "1.80", "0.02"
     "Total"," ","3.34"
