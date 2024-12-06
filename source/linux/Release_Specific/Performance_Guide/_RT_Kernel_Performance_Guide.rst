.. include:: <isonum.txt>

..  http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_RT_Kernel_Performance_Guide

.. rubric::  **Read This First**
   :name: read-this-first-rt-kernel-perf-guide

All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.

+----------------+---------------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                         |
+================+=====================================================================================================================+
| AM335x         | AM335x Evaluation Module rev 1.5B with ARM running at 1000MHz, DDR3-400 (400MHz/800 MT/S), TMDXEVM3358              |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| AM437x-gpevm   | AM437x-gpevm Evaluation Module rev 1.5A with ARM running at 1000MHz, DDR3-400 (400MHz/800 MT/S), TMDSEVM437X        |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| AM572x IDK     | AM57xx Evaluation Module rev A2 with ARM running at 1500MHz, DDR3L-533 (533 MHz/1066 MT/S), TMDXIDK5278             |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| AM574x IDK     | AM57xx Industrial Development Kit rev 1.0A  with ARM running at 1500MHz, DDR3L-533 (533 MHz/1066 MT/S), TMDXIDK5278 |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| K2HK EVM       | K2 Hawkings Evaluation Module rev 40 with ARM running at 1200MHz, DDR3-1600 (800 MHz/1600 MT/S), EVMK2H             |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| K2G EVM        | K2 Galileo Evaluation Module rev C, DDR3-1333 (666 MHz/1333 MT/S), EVMK2G                                           |
+----------------+---------------------------------------------------------------------------------------------------------------------+
| AM65x EVM      | AM65x Evaluation Module rev 1.0 with ARM running at 800MHz, DDR4-2400 (1333 MT/S), TMDX654GPEVM                     |
+----------------+---------------------------------------------------------------------------------------------------------------------+

Table:  Evaluation Modules

|

.. rubric::  About This Manual
   :name: about-this-manual-rt-kernel-perf-guide

This document provides performance data for each of the device drivers
which are part of the Process SDK Linux package. This document should be
used in conjunction with release notes and user guides provided with the
Process SDK Linux package for information on specific issues present
with drivers included in a particular release.

.. rubric::  If You Need Assistance
   :name: if-you-need-assistance-rt-kernel-perf-guide

For further information or to report any problems, contact
http://community.ti.com/ or http://support.ti.com/

|

.. rubric::  System Benchmarks

**LMBench**

LMBench is a collection of microbenchmarks of which the memory bandwidth
and latency related ones are typically used to estimate processor
memory system performance.

*Latency*: lat_mem_rd-stride128-szN, where N is equal to or smaller than the cache
size at given level measures the cache miss penalty. N that is at least
double the size of last level cache is the latency to external memory.

*Bandwidth*: bw_mem_bcopy-N, where N is is equal to or smaller than the cache size at
a given level measures the achivable memory bandwidth from software doing
a memcpy() type operation. Typical use is for external memory bandwidth
calculation. The bandwidth is calculated as byte read and written counts
as 1 which should be roughly half of STREAM copy result.

.. csv-table::
    :header: "Benchmarks","am574x-idk: perf","am654x-idk: perf"

    "af_unix_sock_stream_latency (microsec)","63.17","50.64"
     "af_unix_socket_stream_bandwidth (MBs)","867.06","1213.27"
    "bw_file_rd-io-1mb (MB/s)","681.66","964.69"
    "bw_file_rd-o2c-1mb (MB/s)","534.28","650.09"
    "bw_mem-bcopy-16mb (MB/s)","1542.61","904.47"
    "bw_mem-bcopy-1mb (MB/s)","3532.91","1467.35"
    "bw_mem-bcopy-2mb (MB/s)","2525.25","977.04"
    "bw_mem-bcopy-4mb (MB/s)","1655.63","915.96"
    "bw_mem-bcopy-8mb (MB/s)","1568.01","913.76"
    "bw_mem-bzero-16mb (MB/s)","3947.21","2014.35"
    "bw_mem-bzero-1mb (MB/s)","3921.24 (min 3532.91, max 4309.57)","2914.31 (min 1467.35, max 4361.26)"
    "bw_mem-bzero-2mb (MB/s)","3411.62 (min 2525.25, max 4297.99)","2548.06 (min 977.04, max 4119.08)"
    "bw_mem-bzero-4mb (MB/s)","2906.10 (min 1655.63, max 4156.56)","1676.57 (min 915.96, max 2437.17)"
    "bw_mem-bzero-8mb (MB/s)","2798.44 (min 1568.01, max 4028.87)","1487.28 (min 913.76, max 2060.79)"
    "bw_mem-cp-16mb (MB/s)","847.05","582.41"
    "bw_mem-cp-1mb (MB/s)","3838.26 (min 3354.52, max 4321.99)","2691.39 (min 850.20, max 4532.58)"
    "bw_mem-cp-2mb (MB/s)","2608.28 (min 979.27, max 4237.29)","2403.64 (min 631.11, max 4176.16)"
    "bw_mem-cp-4mb (MB/s)","2467.70 (min 775.95, max 4159.45)","1517.19 (min 580.38, max 2453.99)"
    "bw_mem-cp-8mb (MB/s)","2431.67 (min 851.97, max 4011.37)","1328.00 (min 599.43, max 2056.56)"
    "bw_mem-fcp-16mb (MB/s)","864.91","865.61"
    "bw_mem-fcp-1mb (MB/s)","3243.72 (min 2177.86, max 4309.57)","2893.17 (min 1425.08, max 4361.26)"
    "bw_mem-fcp-2mb (MB/s)","2630.31 (min 962.62, max 4297.99)","2526.18 (min 933.27, max 4119.08)"
    "bw_mem-fcp-4mb (MB/s)","2509.88 (min 863.19, max 4156.56)","1658.29 (min 879.41, max 2437.17)"
    "bw_mem-fcp-8mb (MB/s)","2446.68 (min 864.49, max 4028.87)","1460.04 (min 859.29, max 2060.79)"
    "bw_mem-frd-16mb (MB/s)","875.90","1188.27"
    "bw_mem-frd-1mb (MB/s)","2120.63 (min 2063.40, max 2177.86)","1434.43 (min 1425.08, max 1443.78)"
    "bw_mem-frd-2mb (MB/s)","1289.59 (min 962.62, max 1616.55)","1134.31 (min 933.27, max 1335.34)"
    "bw_mem-frd-4mb (MB/s)","937.29 (min 863.19, max 1011.38)","1075.44 (min 879.41, max 1271.46)"
    "bw_mem-frd-8mb (MB/s)","880.43 (min 864.49, max 896.36)","1027.47 (min 859.29, max 1195.64)"
    "bw_mem-fwr-16mb (MB/s)","3943.31","2024.80"
    "bw_mem-fwr-1mb (MB/s)","3192.70 (min 2063.40, max 4321.99)","2988.18 (min 1443.78, max 4532.58)"
    "bw_mem-fwr-2mb (MB/s)","2926.92 (min 1616.55, max 4237.29)","2755.75 (min 1335.34, max 4176.16)"
    "bw_mem-fwr-4mb (MB/s)","2585.42 (min 1011.38, max 4159.45)","1862.73 (min 1271.46, max 2453.99)"
    "bw_mem-fwr-8mb (MB/s)","2453.87 (min 896.36, max 4011.37)","1626.10 (min 1195.64, max 2056.56)"
    "bw_mem-rd-16mb (MB/s)","2640.26","1204.18"
    "bw_mem-rd-1mb (MB/s)","8067.78 (min 7203.79, max 8931.76)","1928.16 (min 1855.98, max 2000.33)"
    "bw_mem-rd-2mb (MB/s)","6208.78 (min 5997.00, max 6420.55)","1645.92 (min 1594.90, max 1696.93)"
    "bw_mem-rd-4mb (MB/s)","2058.83 (min 1195.28, max 2922.37)","1157.18 (min 1027.35, max 1287.00)"
    "bw_mem-rd-8mb (MB/s)","1807.88 (min 948.20, max 2667.56)","1056.88 (min 904.57, max 1209.19)"
    "bw_mem-rdwr-16mb (MB/s)","897.16","854.34"
    "bw_mem-rdwr-1mb (MB/s)","4189.83 (min 3354.52, max 5025.13)","1323.74 (min 850.20, max 1797.27)"
    "bw_mem-rdwr-2mb (MB/s)","1959.92 (min 979.27, max 2940.56)","1084.64 (min 631.11, max 1538.17)"
    "bw_mem-rdwr-4mb (MB/s)","924.17 (min 775.95, max 1072.39)","781.41 (min 580.38, max 982.44)"
    "bw_mem-rdwr-8mb (MB/s)","883.65 (min 851.97, max 915.33)","734.45 (min 599.43, max 869.47)"
    "bw_mem-wr-16mb (MB/s)","925.44","891.17"
    "bw_mem-wr-1mb (MB/s)","6978.45 (min 5025.13, max 8931.76)","1826.63 (min 1797.27, max 1855.98)"
    "bw_mem-wr-2mb (MB/s)","4680.56 (min 2940.56, max 6420.55)","1566.54 (min 1538.17, max 1594.90)"
    "bw_mem-wr-4mb (MB/s)","1133.84 (min 1072.39, max 1195.28)","1004.90 (min 982.44, max 1027.35)"
    "bw_mem-wr-8mb (MB/s)","931.77 (min 915.33, max 948.20)","887.02 (min 869.47, max 904.57)"
    "bw_mmap_rd-mo-1mb (MB/s)","2752.29","1958.10"
    "bw_mmap_rd-o2c-1mb (MB/s)","776.55","672.04"
    "bw_pipe (MB/s)","210.63","395.28"
    "bw_unix (MB/s)","867.06","1213.27"
    "lat_connect (us)","148.24","82.78"
    "lat_ctx-2-128k (us)","1.69","3.40"
    "lat_ctx-2-256k (us)","4.00","1.35"
    "lat_ctx-4-128k (us)","8.40","2.98"
    "lat_ctx-4-256k (us)","0.00","0.00"
    "lat_fs-0k (num_files)","108.00","179.00"
    "lat_fs-10k (num_files)","45.00","79.00"
    "lat_fs-1k (num_files)","66.00","125.00"
    "lat_fs-4k (num_files)","68.00","128.00"
    "lat_mem_rd-stride128-sz1000k (ns)","19.29","35.18"
    "lat_mem_rd-stride128-sz125k (ns)","19.06","9.78"
    "lat_mem_rd-stride128-sz250k (ns)","19.28","10.26"
    "lat_mem_rd-stride128-sz31k (ns)","13.47","6.41"
    "lat_mem_rd-stride128-sz50 (ns)","4.01","3.78"
    "lat_mem_rd-stride128-sz500k (ns)","19.28","16.13"
    "lat_mem_rd-stride128-sz62k (ns)","17.21","9.20"
    "lat_mmap-1m (us)","158.00","77.00"
    "lat_ops-double-add (ns)","1.10","0.92"
    "lat_ops-double-mul (ns)","5.05","5.03"
    "lat_ops-float-add (ns)","1.10","0.91"
    "lat_ops-float-mul (ns)","5.04","5.05"
    "lat_ops-int-add (ns)","1.01","1.26"
    "lat_ops-int-bit (ns)","0.67","0.84"
    "lat_ops-int-div (ns)","88.18","7.59"
    "lat_ops-int-mod (ns)","15.52","7.99"
    "lat_ops-int-mul (ns)","3.16","3.82"
    "lat_ops-int64-add (ns)","1.11","1.26"
    "lat_ops-int64-bit (ns)","1.03","0.84"
    "lat_ops-int64-div (ns)","183.22","11.98"
    "lat_ops-int64-mod (ns)","34.36","9.23"
    "lat_pagefault (us)","1.89","1.57"
    "lat_pipe (us)","43.04","25.12"
    "lat_proc-exec (us)","2079.00","1286.40"
    "lat_proc-fork (us)","1903.33","1187.60"
    "lat_proc-proccall (us)","0.01","0.01"
    "lat_select (us)","41.64","52.71"
    "lat_sem (us)","3.16","6.90"
    "lat_sig-catch (us)","11.72","9.19"
    "lat_sig-install (us)","2.34","1.09"
    "lat_sig-prot (us)","0.23","0.83"
    "lat_syscall-fstat (us)","4.80","2.47"
    "lat_syscall-null (us)","0.49","0.44"
    "lat_syscall-open (us)","326.35","206.68"
    "lat_syscall-read (us)","0.69","1.16"
    "lat_syscall-stat (us)","12.27","6.90"
    "lat_syscall-write (us)","0.57","0.77"
    "lat_tcp (us)","0.87","0.86"
    "lat_unix (us)","63.17","50.64"
    "latency_for_0.50_mb_block_size (nanosec)","19.28","16.13"
    "latency_for_1.00_mb_block_size (nanosec)","9.64 (min 0.00, max 19.29)","17.59 (min 0.00, max 35.18)"
    "pipe_bandwidth (MBs)","210.63","395.28"
    "pipe_latency (microsec)","43.04","25.12"
    "procedure_call (microsec)","0.01","0.01"
    "select_on_200_tcp_fds (microsec)","41.64","52.71"
    "semaphore_latency (microsec)","3.16","6.90"
    "signal_handler_latency (microsec)","2.34","1.09"
    "signal_handler_overhead (microsec)","11.72","9.19"
    "tcp_ip_connection_cost_to_localhost (microsec)","148.24","82.78"
    "tcp_latency_using_localhost (microsec)","0.87","0.86"

Table:  *LM Bench Metrics*

**Dhrystone**

Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed. For standard ARM
cores the DMIPS/MHz score will be identical with the same compiler and flags.

.. csv-table::
    :header: "Benchmarks","am574x-idk: perf","am654x-idk: perf"

    "cpu_clock (MHz)","10.00","400.00"
    "dhrystone_per_mhz (DMIPS/MHz)","344.90","6.10"
    "dhrystone_per_second (DhrystoneP)","6060606.00","4255319.00"

Table:  *Dhrystone Benchmark*

**Whetstone**

.. csv-table::
    :header: "Benchmarks","am574x-idk: perf","am654x-idk: perf"

    "whetstone (MIPS)","3333.30","3333.30"

Table:  *Whetstone Benchmark*

**Linpack**

Linpack measures peak double precision (64 bit) floating point performance in
sloving a dense linear system.

.. csv-table::
    :header: "Benchmarks","am574x-idk: perf","am654x-idk: perf"

    "linpack (Kflops)","666667.00","326300.00"

Table:  *Linpack Benchmark*

**NBench**

.. csv-table::
    :header: "Benchmarks","am574x-idk: perf","am654x-idk: perf"

    "assignment (Iterations)","10.98","7.68"
    "fourier (Iterations)","12533.00","8242.30"
    "fp_emulation (Iterations)","113.56","61.40"
    "huffman (Iterations)","967.62","671.65"
    "idea (Iterations)","2442.00","1915.50"
    "lu_decomposition (Iterations)","551.76","313.92"
    "neural_net (Iterations)","15.33","4.21"
    "numeric_sort (Iterations)","439.40","296.85"
    "string_sort (Iterations)","93.97","94.51"

Table:  *NBench Benchmarks*

**Stream**

STREAM is a microbenchmarks for measuring data memory system performance without
any data reuse. It is designed to miss on caches and exercise data prefetcher and
apeculative accesseses. it uses double precision floating point (64bit) but in
most modern processors the memory access will be the bottleck. The four individual
scores are copy, scale as in multiply by constant, add two numbers, and triad for
multiply accumulate. For bandwidth a byte read counts as one and a byte written
counts as one resulting in a score that is double the bandwidth LMBench will show.

.. csv-table::
    :header: "Benchmarks","am574x-idk: perf","am654x-idk: perf"

    "add (MB/s)","2934.20","1588.80"
    "copy (MB/s)","3127.10","1845.10"
    "scale (MB/s)","3116.80","1823.80"
    "triad (MB/s)","2901.30","1497.40"

Table:  *Stream*

**CoreMarkPro**

CoreMark\ |reg|\ -Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark\ |reg| benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

Table:  *CoreMarkPro*

**MultiBench**

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

Table:  *Multibench*

**Spec2K6**

CPU2006 is a set of benchmarks designed to test the CPU performance of a modern server
computer system. It is split into two components, the first being CINT2006,
the other being CFP2006 (SPECfp), for floating point testing.

SPEC defines a base runtime for each of the 12 benchmark programs.
For SPECint2006, that number ranges from 1000 to 3000 seconds. The timed test is run on
the system, and the time of the test system is compared to the reference time, and a ratio
is computed. That ratio becomes the SPECint score for that test. (This differs from the rating
in SPECINT2000, which multiplies the ratio by 100.)

As an example for SPECint2006, consider a processor which can run 400.perlbench in 2000 seconds.
The time it takes the reference machine to run the benchmark is 9770 seconds. Thus the ratio is 4.885.
Each ratio is computed, and then the geometric mean of those ratios is computed to produce an overall value.

Rate (Multiple Cores)
Speed (Single Core)

|

.. rubric::  Maximum Latency under different use cases


**Shield (dedicated core) Case**

| The following tests measure worst-case latency under different
  scenarios or use cases.
| Cyclictest application was used to measured latency. Each test ran for
  4 hours.
| Two cgroups were used using shield\_shell procedure shown below.
| The application running the use case and cyclictest ran on a dedicated
  cpu (rt) while the rest of threads ran on nonrt cpu.

::

    shield_shell()
    {
    create_cgroup nonrt 0
    create_cgroup rt 1
    for pid in $(cat /sys/fs/cgroup/tasks); do /bin/echo $pid > /sys/fs/cgroup/nonrt/tasks; done
    /bin/echo $$ > /sys/fs/cgroup/rt/tasks
    }

.. csv-table::
    :header: "Use Case","am574x-idk: Latency","am654x-idk: Latency"

    "L_PERF_SHIELD_SMP_1080ENC","41.00"
    "L_PERF_SHIELD_SMP_GRAPHICS","49.00"
    "L_PERF_SHIELD_SMP_HACKBENCH","53.00","70.00"
    "L_PERF_SHIELD_SMP_MEM","42.00","77.00"
    "L_PERF_SHIELD_SMP_NET","51.00","29.00"
    "L_PERF_SHIELD_SMP_NO_LOAD","34.00","31.00"
    "L_PERF_SHIELD_SMP_STRESS_LOAD","51.00","74.00"
    "L_PERF_SHIELD_SMP_UART","41.00","31.00"
    "L_PERF_SHIELD_SMP_USB","68.00","56.00"
    "L_PERF_SHIELD_SMP_USB_NET","77.00"

|

.. rubric::  ALSA SoC Audio Driver

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


Table:  *Audio Capture*

.. csv-table::
    :header: "Sampling Rate (Hz)","am574x-idk: Throughput (bits/sec)","am574x-idk: CPU Load (%)"

    "8000","1024417.00","0.10"
    "11025","1024418.00","0.05"
    "16000","1024418.00","0.02"
    "22050","1024418.00","0.04"
    "24000","1024418.00","0.08"
    "32000","1024418.00","0.07"
    "44100","1411775.00","1.65"
    "48000","1536626.00","0.04"
    "88200","2823548.00","3.25"
    "96000","3073248.00","0.08"

Table:  *Audio Playback*

|

.. rubric::  Sensor Capture

Capture video frames (MMAP buffers) with v4l2c-ctl and record the
reported fps

|

.. rubric::  Display Driver

.. csv-table::
    :header: "Mode","am574x-idk: Fps"

    "1024x576\@60","59.97 (min 59.79, max 60.09)"
    "1024x768\@60","60.00 (min 59.89, max 60.12)"
    "1024x768\@70","70.07 (min 69.53, max 70.61)"
    "1024x768\@75","75.03 (min 74.38, max 75.56)"
    "1152x864\@75","75.00 (min 74.81, max 75.19)"
    "1280x1024\@60","60.01 (min 59.04, max 60.28)"
    "1280x1024\@75","75.03 (min 74.89, max 75.19)"
    "1280x720\@60","60.00 (min 59.83, max 60.23)"
    "1280x768\@60","59.86 (min 58.88, max 60.15)"
    "1280x768\@75","74.89 (min 73.49, max 75.07)"
    "1280x800\@60","59.81 (min 59.70, max 59.92)"
    "1280x800\@75","74.93 (min 74.33, max 75.55)"
    "1280x960\@60","59.99 (min 59.08, max 60.13)"
    "1360x768\@60","59.94 (min 58.98, max 60.08)"
    "1400x1050\@60","59.98 (min 59.90, max 60.10)"
    "1400x1050\@75","74.87 (min 74.74, max 74.99)"
    "1440x900\@60","59.89 (min 59.76, max 60.01)"
    "1440x900\@75","74.98 (min 73.83, max 75.18)"
    "1600x1200\@60","60.00 (min 59.93, max 60.12)"
    "1600x1200\@65","65.00 (min 64.80, max 65.15)"
    "1600x1200\@70","70.00 (min 69.71, max 70.39)"
    "1600x900\@60","60.00 (min 59.88, max 60.12)"
    "1680x1050\@60","59.95 (min 59.88, max 60.02)"
    "1680x1050\@75","74.89 (min 74.60, max 75.19)"
    "1680x945\@60","60.02 (min 59.84, max 60.11)"
    "1920x1080\@60","60.00 (min 59.92, max 60.09)"
    "2048x1152\@60","60.00 (min 59.90, max 60.12)"
    "640x480\@60","60.00 (min 59.87, max 60.11)"
    "640x480\@73","72.79 (min 71.60, max 72.97)"
    "640x480\@75","75.00 (min 74.55, max 75.38)"
    "720x400\@70","70.08 (min 69.96, max 70.23)"
    "800x600\@56","56.25 (min 56.13, max 56.35)"
    "800x600\@60","60.32 (min 60.24, max 60.39)"
    "800x600\@72","72.18 (min 71.05, max 72.50)"
    "800x600\@75","74.99 (min 73.70, max 75.15)"
    "832x624\@75","74.55 (min 74.38, max 74.73)"
    "848x480\@60","60.00 (min 59.91, max 60.09)"

Table:  *Display performance (HDMI)*

.. rubric::  Graphics SGX/RGX Driver

**GLBenchmark**

Run GLBenchmark and capture performance reported Display rate (Fps),
Fill rate, Vertex Throughput, etc. All display outputs (HDMI, Displayport and/or LCD)
are connected when running these tests

**Performance (Fps)**

.. csv-table::
    :header: "Benchmark","am574x-idk: Test Number","am574x-idk: Fps"

    "GLB25_EgyptTestC24Z16FixedTime test","2500005.00","29.46 (min 16.00, max 59.00)"
    "GLB25_EgyptTestC24Z16_ETC1 test","2501001.00","35.69 (min 15.48, max 60.00)"
    "GLB25_EgyptTestC24Z16_ETC1to565 test","2501401.00","35.69 (min 15.74, max 60.00)"
    "GLB25_EgyptTestC24Z16_PVRTC4 test","2501101.00","35.42 (min 15.74, max 60.00)"
    "GLB25_EgyptTestC24Z24MS4 test","2500003.00","32.24 (min 15.00, max 60.00)"
    "GLB25_EgyptTestStandard_inherited test","2000000.00","59.94 (min 58.00, max 60.00)"


.. csv-table::
    :header: "Benchmark","am574x-idk: Test Number","am574x-idk: Fps"

    "GLB25_EgyptTestC24Z16_ETC1_Offscreen test","2501011.00","24.00"
    "GLB25_EgyptTestStandardOffscreen_inherited test","2000010.00","83.00"

Table:  *GLBenchmark 2.5 Performance*

**Vertex Throughput**

.. csv-table::
    :header: "Benchmark","am574x-idk: Test Number","am574x-idk: Rate (triangles/sec)"

    "GLB25_TriangleTexFragmentLitTestC24Z16 test","2500511.00","17609242.00"
    "GLB25_TriangleTexTestC24Z16 test","2500301.00","85245192.00"
    "GLB25_TriangleTexVertexLitTestC24Z16 test","2500411.00","20607806.00"


Table:  *GLBenchmark 2.5 Vertex Throughput*

**Pixel Throughput**

.. csv-table::
    :header: "Benchmark","am574x-idk: Test Number","am574x-idk: Rate (texel/sec)","am574x-idk: Fps"

    "GLB25_FillTestC24Z16 test","2500101.00","1073744384.00","43.74 (min 42.29, max 44.26)"

Table:  *GLBenchmark 2.5 Pixel Throughput*

**GFXBench**

Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

**Glmark2**

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

|

.. rubric::  Multimedia (Decode)

Run gstreamer pipeline "gst-launch-1.0 playbin uri=\ file://\ <Path to
stream> video-sink="kmssink sync=false connector=<connector id>"
audio-sink=fakesink" and calculate performance based on the execution
time reported. All display display outputs (HDMI and LCD) were connected
when running these tests, but playout was forced to LCD via the
connector=<connector id> option.

*H264*

.. csv-table::
    :header: "Resolution","am574x-idk: Fps","am574x-idk: IVA Freq (MHz)","am574x-idk: IPU Freq (MHz)"

    "1080p","59.00","532.00","1064.00"
    "720p","59940.00","532.00",""
    "CIF","","532.00",""

Table:  *Gstreamer H264 in AVI Container Decode Performance*

**MPEG4**

.. csv-table::
    :header: "Resolution","am574x-idk: Fps","am574x-idk: IVA Freq (MHz)","am574x-idk: IPU Freq (MHz)"

    "CIF","30.00","532.00",""
    "QVGA","30.00","532.00","1064.00"

Table:  *GStreamer MPEG4 in 3GP Container Decode Performance*

**MPEG2**

.. csv-table::
    :header: "Resolution","am574x-idk: Fps","am574x-idk: IVA Freq (MHz)","am574x-idk: IPU Freq (MHz)"

    "720p","29.97","532.00",""

Table:  *GStreamer MPEG2 in MP4 Container Decode Performance*

|

.. rubric::  Ethernet Driver - CPSW CPSW2G NETCP

**TCP Throughput**

.. csv-table::
    :header: "TCP Window Size (KBytes)","am574x-idk: Throughput (Mbits/sec)","am574x-idk: CPU Load ","am654x-idk: Throughput (Mbits/sec)","am654x-idk: CPU Load "

    "8","494.96","","682.40",""
    "16","573.60","","888.00",""
    "32","652.80","","1150.40",""
    "64","793.60","","1268.00",""
    "128","606.40","","1282.40",""
    "256","415.20","","1332.00",""

Table: *TCP Throughput No Interrupt Pacing*

.. csv-table::
    :header: "TCP Window Size (KBytes)","am574x-idk: Throughput (Mbits/sec)","am574x-idk: CPU Load "

    "8","0.00",""
    "16","592.00",""
    "32","616.80",""
    "64","444.00",""
    "128","672.00",""
    "256","588.80",""

Table: *TCP Throughput Interrupt Pacing*


**UDP Throughput**

.. csv-table::
    :header: "UDP Datagram Size(bytes)","am574x-idk: Throughput (Mbits/sec)","am574x-idk: CPU Load ","am574x-idk: Packets Per Second (kpps) ","am654x-idk: Throughput (Mbits/sec)","am654x-idk: CPU Load ","am654x-idk: Packets Per Second (kpps) "

    "64","24.10","97.60","46.00","31.00","57.90","60.00"
    "128","44.80","96.46","42.00","75.40","48.92","73.00"
    "256","94.00","95.62","45.00","147.90","47.69","71.00"
    "512","215.60","97.56","52.00","280.30","47.79","68.00"
    "1024","350.70","90.32","42.00","496.30","49.75","60.00"
    "1470","465.80","88.63","39.00","706.10","49.97","60.00"
    "1500","308.40","90.46","25.00","495.40","48.11","41.00"
    "4000","827.50","44.06","25.00"
    "8000","957.30","47.07","14.00"

Table: *UDP Throughput Egress*

.. csv-table::
    :header: "UDP Datagram Size(bytes)","am574x-idk: Throughput (Mbits/sec)","am574x-idk: CPU Load ","am574x-idk: Packets Per Second (kpps) ","am654x-idk: Throughput (Mbits/sec)","am654x-idk: CPU Load ","am654x-idk: Packets Per Second (kpps) "

    "64","37.30","93.74","72.00","26.20","43.00","50.00"
    "128","78.40","94.94","76.00","89.60","42.27","86.00"
    "256","154.70","94.56","75.00","180.70","43.44","87.00"
    "512","313.90","95.44","76.00","367.70","43.52","89.00"
    "1024","657.00","96.04","80.00","715.90","43.64","87.00"
    "1470","928.30","96.13","78.00","93.30","11.40","7.00"
    "4000","0.00","0.03","0.00"
    "8000","0.00","0.07","0.00"

Table: *UDP Throughput Ingress*

-  iperf version 2.0.5
-  For receive performance, on DUT, invoke iperf in server mode.

::

    iperf -s -u

-  For transmit performance, on DUT, invoke iperf in client mode.

::

    iperf -c <server ip> -b <bandwidth limit> -f M -t 60

|

.. rubric::  PCIe Driver

|

.. rubric::  NAND Driver

|

.. rubric::  QSPI Flash Driver

**AM574x-IDK**

.. csv-table::
    :header: "Buffer size (bytes)","am574x-idk: Write UBIFS Throughput (Mbytes/sec)","am574x-idk: Write UBIFS CPU Load (%)","am574x-idk: Read UBIFS Throughput (Mbytes/sec)","am574x-idk: Read UBIFS CPU Load (%)"

    "102400","0.29 (min 0.25, max 0.43)","59.51 (min 57.70, max 61.04)","15.95","13.64"
    "262144","0.25 (min 0.23, max 0.27)","59.53 (min 58.11, max 60.48)","15.28","25.93"
    "524288","0.25 (min 0.23, max 0.27)","59.62 (min 59.18, max 60.21)","15.69","24.00"
    "1048576","0.25 (min 0.23, max 0.27)","59.47 (min 58.13, max 60.77)","15.58","25.93"

**AM654X-IDK**

.. csv-table::
    :header: "Buffer size (bytes)","am654x-idk: Write UBIFS Throughput (Mbytes/sec)","am654x-idk: Write UBIFS CPU Load (%)","am654x-idk: Read UBIFS Throughput (Mbytes/sec)","am654x-idk: Read UBIFS CPU Load (%)"

    "102400","0.62 (min 0.49, max 1.12)","25.11 (min 25.04, max 25.19)","33.78","28.00"
    "262144","0.47 (min 0.35, max 0.52)","25.19 (min 25.09, max 25.33)","31.14","22.22"
    "524288","0.46 (min 0.35, max 0.53)","25.13 (min 25.09, max 25.16)","29.53","22.22"
    "1048576","0.47 (min 0.35, max 0.52)","25.15 (min 25.12, max 25.19)","32.10","23.08"

|

.. rubric::  SPI Flash Driver

|

.. rubric::  EMMC Driver

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

**AM574x-IDK**

.. csv-table::
    :header: "Buffer size (bytes)","am574x-idk: Write EXT2 Throughput (Mbytes/sec)","am574x-idk: Write EXT2 CPU Load (%)","am574x-idk: Read EXT2 Throughput (Mbytes/sec)","am574x-idk: Read EXT2 CPU Load (%)"

    "102400","32.55 (min 27.11, max 34.37)","15.07 (min 10.76, max 28.96)","64.83","19.94"
    "262144","32.83 (min 27.27, max 34.47)","14.91 (min 10.79, max 27.99)","67.56","20.86"
    "524288","32.71 (min 27.49, max 34.33)","14.71 (min 11.26, max 26.79)","74.03","20.07"
    "1048576","32.77 (min 27.51, max 34.46)","14.94 (min 10.88, max 27.51)","75.30","21.90"
    "5242880","32.71 (min 27.48, max 34.42)","13.94 (min 9.80, max 27.67)","75.28","23.38"

.. csv-table::
    :header: "Buffer size (bytes)","am574x-idk: Write EXT4 Throughput (Mbytes/sec)","am574x-idk: Write EXT4 CPU Load (%)","am574x-idk: Read EXT4 Throughput (Mbytes/sec)","am574x-idk: Read EXT4 CPU Load (%)"

    "102400","31.87 (min 28.53, max 33.23)","15.75 (min 12.42, max 24.04)","64.23","22.39"
    "262144","31.59 (min 28.34, max 32.79)","14.74 (min 11.73, max 23.36)","62.67","19.51"
    "524288","32.24 (min 29.08, max 33.16)","16.07 (min 13.18, max 25.66)","75.08","22.02"
    "1048576","32.20 (min 29.05, max 33.18)","15.70 (min 12.82, max 24.72)","77.58","23.25"
    "5242880","32.26 (min 29.01, max 33.40)","15.87 (min 13.43, max 24.27)","77.56","24.07"

**AM654x-IDK**

.. csv-table::
    :header: "Buffer size (bytes)","am654x-idk: Write VFAT Throughput (Mbytes/sec)","am654x-idk: Write VFAT CPU Load (%)","am654x-idk: Read VFAT Throughput (Mbytes/sec)","am654x-idk: Read VFAT CPU Load (%)"

    "102400","33.78 (min 25.58, max 35.93)","6.84 (min 5.41, max 11.38)","130.13","14.05"
    "262144","33.68 (min 25.42, max 35.82)","6.84 (min 5.47, max 11.31)","130.28","22.94"
    "524288","33.71 (min 25.53, max 35.82)","6.72 (min 5.48, max 11.25)","131.78","22.26"
    "1048576","33.78 (min 25.61, max 35.86)","6.82 (min 5.57, max 11.07)","147.52","15.07"
    "5242880","33.80 (min 25.54, max 36.09)","6.74 (min 5.44, max 11.15)","145.30","15.38"

.. csv-table::
    :header: "Buffer size (bytes)","am654x-idk: Write EXT2 Throughput (Mbytes/sec)","am654x-idk: Write EXT2 CPU Load (%)","am654x-idk: Read EXT2 Throughput (Mbytes/sec)","am654x-idk: Read EXT2 CPU Load (%)"

    "102400","34.87 (min 31.19, max 35.99)","4.85 (min 4.03, max 7.71)","134.43","15.36"
    "262144","34.72 (min 30.51, max 35.86)","5.11 (min 4.29, max 7.52)","142.35","16.96"
    "524288","34.85 (min 31.08, max 36.01)","4.93 (min 4.12, max 7.94)","155.98","17.74"
    "1048576","34.78 (min 30.81, max 35.98)","4.90 (min 3.96, max 7.58)","163.90","17.86"
    "5242880","34.79 (min 30.76, max 35.88)","4.99 (min 4.17, max 7.79)","163.61","18.58"

.. csv-table::
    :header: "Buffer size (bytes)","am654x-idk: Write EXT4 Throughput (Mbytes/sec)","am654x-idk: Write EXT4 CPU Load (%)","am654x-idk: Read EXT4 Throughput (Mbytes/sec)","am654x-idk: Read EXT4 CPU Load (%)"

    "102400","35.48 (min 29.78, max 38.73)","6.64 (min 5.56, max 9.14)","139.16","15.15"
    "262144","34.50 (min 29.45, max 35.86)","6.54 (min 5.31, max 8.95)","135.61","15.84"
    "524288","34.79 (min 29.57, max 36.42)","6.43 (min 5.48, max 9.12)","162.33","17.97"
    "1048576","34.94 (min 29.88, max 36.38)","6.27 (min 5.41, max 8.89)","177.00","18.10"
    "5242880","35.09 (min 29.93, max 36.47)","6.38 (min 5.42, max 9.25)","176.11","18.53"

|

.. rubric::  SATA Driver

-  Filesize used is : 1G
-  SATA II Harddisk used is: Seagate ST3500514NS 500G


**mSATA Driver**

-  Filesize used is : 1G
-  MSATA Harddisk used is: SMS200S3/30G Kingston mSATA SSD drive

|

.. rubric::  MMC/SD Driver

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

**AM574x-IDK**

.. csv-table::
    :header: "Buffer size (bytes)","am574x-idk: Write VFAT Throughput (Mbytes/sec)","am574x-idk: Write VFAT CPU Load (%)","am574x-idk: Read VFAT Throughput (Mbytes/sec)","am574x-idk: Read VFAT CPU Load (%)"

    "102400","16.36 (min 9.71, max 18.93)","8.19 (min 6.18, max 11.50)","21.24","9.15"
    "262144","16.69 (min 11.22, max 18.83)","8.57 (min 6.56, max 13.47)","21.10","8.12"
    "524288","16.26 (min 11.55, max 19.04)","8.21 (min 5.48, max 14.00)","21.42","8.27"
    "1048576","16.67 (min 10.85, max 18.85)","8.10 (min 6.31, max 12.84)","21.81","6.86"
    "5242880","16.74 (min 10.84, max 18.89)","8.90 (min 6.62, max 12.97)","21.82","7.96"

.. csv-table::
    :header: "Buffer size (bytes)","am574x-idk: Write EXT2 Throughput (Mbytes/sec)","am574x-idk: Write EXT2 CPU Load (%)","am574x-idk: Read EXT2 Throughput (Mbytes/sec)","am574x-idk: Read EXT2 CPU Load (%)"

    "102400","16.58 (min 9.92, max 18.99)","6.86 (min 5.01, max 9.89)","21.75","7.41"
    "262144","18.27 (min 16.77, max 18.96)","8.34 (min 4.41, max 16.60)","21.94","7.46"
    "524288","16.84 (min 12.58, max 18.68)","8.64 (min 4.08, max 16.95)","22.42","6.97"
    "1048576","18.10 (min 16.43, max 19.02)","8.41 (min 6.03, max 16.38)","22.58","6.70"
    "5242880","18.65 (min 16.90, max 19.22)","8.60 (min 5.86, max 17.10)","22.60","6.82"

.. csv-table::
    :header: "Buffer size (bytes)","am574x-idk: Write EXT4 Throughput (Mbytes/sec)","am574x-idk: Write EXT4 CPU Load (%)","am574x-idk: Read EXT4 Throughput (Mbytes/sec)","am574x-idk: Read EXT4 CPU Load (%)"

    "102400","18.33 (min 17.56, max 18.62)","9.28 (min 7.24, max 14.95)","19.60","6.59"
    "262144","16.79 (min 16.39, max 17.24)","7.70 (min 5.65, max 12.76)","21.39","7.63"
    "524288","18.16 (min 16.90, max 18.74)","8.89 (min 6.71, max 13.67)","22.62","6.82"
    "1048576","18.42 (min 17.41, max 18.79)","10.27 (min 7.69, max 16.17)","22.77","6.44"
    "5242880","17.96 (min 17.30, max 18.73)","8.44 (min 6.34, max 14.20)","22.79","6.87"

**AM654x-IDK**

.. csv-table::
    :header: "Buffer size (bytes)","am654x-idk: Write VFAT Throughput (Mbytes/sec)","am654x-idk: Write VFAT CPU Load (%)","am654x-idk: Read VFAT Throughput (Mbytes/sec)","am654x-idk: Read VFAT CPU Load (%)"

    "102400","15.91 (min 13.38, max 16.63)","3.37 (min 2.51, max 6.28)","22.02","2.86"
    "262144","15.49 (min 11.33, max 16.68)","3.21 (min 2.55, max 5.45)","21.91","3.41"
    "524288","15.19 (min 13.39, max 16.57)","3.26 (min 2.07, max 6.43)","22.33","3.00"
    "1048576","15.29 (min 13.40, max 16.60)","3.28 (min 2.13, max 6.53)","22.39","2.90"
    "5242880","15.57 (min 13.36, max 16.45)","3.35 (min 2.43, max 6.51)","22.38","2.79"

.. csv-table::
    :header: "Buffer size (bytes)","am654x-idk: Write EXT2 Throughput (Mbytes/sec)","am654x-idk: Write EXT2 CPU Load (%)","am654x-idk: Read EXT2 Throughput (Mbytes/sec)","am654x-idk: Read EXT2 CPU Load (%)"

    "102400","16.88 (min 15.77, max 17.20)","2.47 (min 2.04, max 3.92)","22.50","2.49"
    "262144","15.53 (min 13.25, max 16.91)","2.27 (min 1.65, max 3.35)","22.85","2.79"
    "524288","16.08 (min 13.89, max 17.03)","2.42 (min 1.72, max 3.97)","23.37","2.30"
    "1048576","16.55 (min 15.58, max 17.00)","2.37 (min 1.91, max 3.83)","23.46","2.31"
    "5242880","15.59 (min 13.38, max 17.04)","2.27 (min 1.68, max 3.35)","23.47","2.47"

.. csv-table::
    :header: "Buffer size (bytes)","am654x-idk: Write EXT4 Throughput (Mbytes/sec)","am654x-idk: Write EXT4 CPU Load (%)","am654x-idk: Read EXT4 Throughput (Mbytes/sec)","am654x-idk: Read EXT4 CPU Load (%)"

    "102400","17.96 (min 16.21, max 19.15)","3.30 (min 2.47, max 4.99)","22.67","2.50"
    "262144","17.69 (min 15.30, max 19.17)","3.54 (min 2.45, max 5.23)","22.97","2.27"
    "524288","18.04 (min 17.02, max 19.00)","3.38 (min 2.78, max 5.30)","23.52","2.31"
    "1048576","17.41 (min 16.44, max 18.28)","3.33 (min 2.53, max 5.18)","23.73","2.44"
    "5242880","17.64 (min 16.38, max 18.20)","3.26 (min 2.49, max 5.24)","23.72","2.44"

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|

.. rubric::  UART Driver

Performance and Benchmarks not available in this release.

|

.. rubric::  I2C Driver

Performance and Benchmarks not available in this release.

|

.. rubric::  EDMA Driver

Performance and Benchmarks not available in this release.

|

.. rubric::  Touchscreen Driver

Performance and Benchmarks not available in this release.

|

.. rubric::  USB Driver

**MUSB/XHCI Host controller**

.. warning::

  **IMPORTANT**: For Mass-storage applications, the performance numbers can be severely
  affected if the media is mounted in sync mode. Hot plug scripts in the
  filesystem mount removable media in sync mode to ensure data
  integrity. For performance sensitive applications, umount the
  auto-mounted filesystem and re-mount in async mode.

*Setup* : SAMSUNG 850 PRO 2.5" 128GB SATA III Internal Solid State Drive (SSD) used with Inateck ASM1153E enclosure is
connected to usb port under test. File read/write performance data is captured.

**USB Host VFAT**

.. csv-table::
    :header: "Buffer size (bytes)","am654x-idk: Write VFAT Throughput (Mbytes/sec)","am654x-idk: Write VFAT CPU Load (%)","am654x-idk: Read VFAT Throughput (Mbytes/sec)","am654x-idk: Read VFAT CPU Load (%)"

    "102400","33.59 (min 25.46, max 35.84)","8.41 (min 6.36, max 11.97)","37.23","6.85"
    "262144","33.51 (min 25.42, max 35.61)","8.63 (min 6.99, max 12.62)","37.96","6.86"

**USB Host EXT2**

.. csv-table::
    :header: "Buffer size (bytes)","am654x-idk: Write EXT2 Throughput (Mbytes/sec)","am654x-idk: Write EXT2 CPU Load (%)","am654x-idk: Read EXT2 Throughput (Mbytes/sec)","am654x-idk: Read EXT2 CPU Load (%)"

    "102400","35.42 (min 30.65, max 36.79)","5.43 (min 3.60, max 8.04)","37.60","6.05"
    "1048576","35.59 (min 31.04, max 36.87)","5.95 (min 4.71, max 8.66)","37.11","6.60"
    "5242880","35.63 (min 30.79, max 36.95)","5.61 (min 4.38, max 8.41)","37.00","7.05"

|

.. rubric::  CRYPTO Driver

**OpenSSL Performance**

.. csv-table::
    :header: "Algorithm","Buffer Size (in bytes)","am574x-idk: throughput (KBytes/Sec)","am654x-idk: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","7819.95","13928.11"
    "aes-128-cbc","16","1561.91","241.15"
    "aes-128-cbc","256","2294.53","3632.55"
    "aes-128-cbc","64","5757.99","1082.07"
    "aes-128-cbc","8192","24461.31","73572.35"
    "aes-192-cbc","1024","7842.47","18339.16"
    "aes-192-cbc","16","1543.84","309.75"
    "aes-192-cbc","256","2255.27","4894.46"
    "aes-192-cbc","64","5599.40","1237.25"
    "aes-192-cbc","8192","24586.92","87026.35"
    "aes-256-cbc","1024","6730.75","13613.06"
    "aes-256-cbc","16","1547.00","231.65"
    "aes-256-cbc","256","1934.76","3592.87"
    "aes-256-cbc","64","5236.18","901.27"
    "aes-256-cbc","8192","23115.09","68730.88"
    "des-cbc","1024","5789.35","14491.99"
    "des-cbc","16","137.58","2932.50"
    "des-cbc","256","1960.02","12201.39"
    "des-cbc","64","537.58","7470.02"
    "des-cbc","8192","13200.04","15261.70"
    "des3","1024","5727.23","17277.61"
    "des3","16","137.54","310.20"
    "des3","256","1949.70","4831.32"
    "des3","64","535.96","1246.78"
    "des3","8192","12926.98","58949.63"
    "md5","1024","6029.99","30797.14"
    "md5","16","410.14","684.47"
    "md5","256","1951.57","9894.06"
    "md5","64","1605.59","2655.83"
    "md5","8192","32063.49","77933.23"
    "sha1","1024","6033.41","19233.11"
    "sha1","16","402.91","384.53"
    "sha1","256","1947.05","5743.87"
    "sha1","64","1589.40","1506.15"
    "sha1","8192","32339.29","59659.61"
    "sha224","1024","6012.25","17584.81"
    "sha224","16","385.74","606.95"
    "sha224","256","1945.43","7402.67"
    "sha224","64","1477.03","2236.39"
    "sha224","8192","31935.15","29016.06"
    "sha256","1024","6062.42","13561.51"
    "sha256","16","378.86","367.75"
    "sha256","256","1939.63","4953.09"
    "sha256","64","1462.44","1401.77"
    "sha256","8192","31992.49","27295.74"
    "sha384","1024","6077.78","21478.74"
    "sha384","16","353.69","620.04"
    "sha384","256","1929.39","8200.53"
    "sha384","64","1414.25","2475.39"
    "sha384","8192","35072.68","39949.65"
    "sha512","1024","6142.63","15635.46"
    "sha512","16","361.24","367.46"
    "sha512","256","1940.74","5233.58"
    "sha512","64","1439.08","1472.02"
    "sha512","8192","35149.14","36610.05"

.. csv-table::
    :header: "Algorithm","am574x-idk: CPU Load","am654x-idk: CPU Load"

    "aes-128-cbc","50.00","46.00"
    "aes-192-cbc","50.00","41.00"
    "aes-256-cbc","53.00","46.00"
    "des-cbc","16.00","99.00"
    "des3","16.00","39.00"
    "md5","73.00","99.00"
    "sha1","73.00","98.00"
    "sha224","73.00","98.00"
    "sha256","73.00","98.00"
    "sha384","74.00","98.00"
    "sha512","74.00","98.00"

| Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc


**IPSec Performance**

Note: queue\_len is set to 300 and software fallback threshold set to 9
to enable software support for optimal performance

.. csv-table::
    :header: "Algorithm","am654x-idk: Throughput (Mbps)","am654x-idk: Packets/Sec","am654x-idk: CPU Load"

    "aes128","88.00","7.00","27.20"

|

.. rubric::  PRU Ethernet

Table: **PRU UDP Throughput Egress**

Table: **PRU UDP Throughput Ingress**
