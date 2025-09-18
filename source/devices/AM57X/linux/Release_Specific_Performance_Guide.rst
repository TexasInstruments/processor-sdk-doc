
======================================
 Linux 11.01 Performance Guide
======================================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
| AM572x EVM     | AM57xx Evaluation Module rev A2 with ARM running at 1500MHz, DDR3L-533 (533 MHz/1066 MT/S), TMDSEVM572x        |
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
    :header: "Benchmarks","am57xx-evm: perf"

    "af_unix_sock_stream_latency (microsec)","35.52"
    "af_unix_socket_stream_bandwidth (MBs)","1828.56"
    "bw_file_rd-io-1mb (MB/s)","1338.28"
    "bw_file_rd-o2c-1mb (MB/s)","921.06"
    "bw_mem-bcopy-16mb (MB/s)","2033.81"
    "bw_mem-bcopy-1mb (MB/s)","5083.93"
    "bw_mem-bcopy-2mb (MB/s)","3878.91"
    "bw_mem-bcopy-4mb (MB/s)","2229.86"
    "bw_mem-bcopy-8mb (MB/s)","2077.02"
    "bw_mem-bzero-16mb (MB/s)","5426.03"
    "bw_mem-bzero-1mb (MB/s)","5933.57 (min 5083.93, max 6783.21)"
    "bw_mem-bzero-2mb (MB/s)","5177.93 (min 3878.91, max 6476.94)"
    "bw_mem-bzero-4mb (MB/s)","4048.29 (min 2229.86, max 5866.72)"
    "bw_mem-bzero-8mb (MB/s)","3809.08 (min 2077.02, max 5541.13)"
    "bw_mem-cp-16mb (MB/s)","1066.03"
    "bw_mem-cp-1mb (MB/s)","6116.37 (min 5750.06, max 6482.68)"
    "bw_mem-cp-2mb (MB/s)","3643.18 (min 1208.44, max 6077.91)"
    "bw_mem-cp-4mb (MB/s)","3435.75 (min 1108.32, max 5763.17)"
    "bw_mem-cp-8mb (MB/s)","3307.13 (min 1050.01, max 5564.25)"
    "bw_mem-fcp-16mb (MB/s)","516.63"
    "bw_mem-fcp-1mb (MB/s)","4921.87 (min 3060.52, max 6783.21)"
    "bw_mem-fcp-2mb (MB/s)","4424.31 (min 2371.68, max 6476.94)"
    "bw_mem-fcp-4mb (MB/s)","3241.15 (min 615.57, max 5866.72)"
    "bw_mem-fcp-8mb (MB/s)","3033.29 (min 525.45, max 5541.13)"
    "bw_mem-frd-16mb (MB/s)","1618.53"
    "bw_mem-frd-1mb (MB/s)","3187.87 (min 3060.52, max 3315.22)"
    "bw_mem-frd-2mb (MB/s)","2701.71 (min 2371.68, max 3031.74)"
    "bw_mem-frd-4mb (MB/s)","1152.60 (min 615.57, max 1689.62)"
    "bw_mem-frd-8mb (MB/s)","1080.44 (min 525.45, max 1635.43)"
    "bw_mem-fwr-16mb (MB/s)","5434.32"
    "bw_mem-fwr-1mb (MB/s)","4898.95 (min 3315.22, max 6482.68)"
    "bw_mem-fwr-2mb (MB/s)","4554.83 (min 3031.74, max 6077.91)"
    "bw_mem-fwr-4mb (MB/s)","3726.40 (min 1689.62, max 5763.17)"
    "bw_mem-fwr-8mb (MB/s)","3599.84 (min 1635.43, max 5564.25)"
    "bw_mem-rd-16mb (MB/s)","2595.93"
    "bw_mem-rd-1mb (MB/s)","12470.23 (min 11514.53, max 13425.93)"
    "bw_mem-rd-2mb (MB/s)","11030.21 (min 9251.97, max 12808.44)"
    "bw_mem-rd-4mb (MB/s)","2268.65 (min 1702.42, max 2834.87)"
    "bw_mem-rd-8mb (MB/s)","1997.73 (min 1379.79, max 2615.66)"
    "bw_mem-rdwr-16mb (MB/s)","903.44"
    "bw_mem-rdwr-1mb (MB/s)","6165.74 (min 5750.06, max 6581.42)"
    "bw_mem-rdwr-2mb (MB/s)","3278.29 (min 1208.44, max 5348.14)"
    "bw_mem-rdwr-4mb (MB/s)","1087.54 (min 1066.76, max 1108.32)"
    "bw_mem-rdwr-8mb (MB/s)","982.96 (min 915.91, max 1050.01)"
    "bw_mem-wr-16mb (MB/s)","1348.05"
    "bw_mem-wr-1mb (MB/s)","10003.68 (min 6581.42, max 13425.93)"
    "bw_mem-wr-2mb (MB/s)","9078.29 (min 5348.14, max 12808.44)"
    "bw_mem-wr-4mb (MB/s)","1384.59 (min 1066.76, max 1702.42)"
    "bw_mem-wr-8mb (MB/s)","1147.85 (min 915.91, max 1379.79)"
    "bw_mmap_rd-mo-1mb (MB/s)","3269.75"
    "bw_mmap_rd-o2c-1mb (MB/s)","1090.95"
    "bw_pipe (MB/s)","570.61"
    "bw_unix (MB/s)","1828.56"
    "lat_connect (us)","49.37"
    "lat_ctx-2-128k (us)","6.19"
    "lat_ctx-2-256k (us)","0.62"
    "lat_ctx-4-128k (us)","8.40"
    "lat_ctx-4-256k (us)","0.00"
    "lat_fs-0k (num_files)","3500.00"
    "lat_fs-10k (num_files)","1442.00"
    "lat_fs-1k (num_files)","2066.00"
    "lat_fs-4k (num_files)","2110.00"
    "lat_mem_rd-stride128-sz1000k (ns)","12.83"
    "lat_mem_rd-stride128-sz125k (ns)","12.69"
    "lat_mem_rd-stride128-sz250k (ns)","12.83"
    "lat_mem_rd-stride128-sz31k (ns)","10.22"
    "lat_mem_rd-stride128-sz50 (ns)","2.67"
    "lat_mem_rd-stride128-sz500k (ns)","12.83"
    "lat_mem_rd-stride128-sz62k (ns)","12.69"
    "lat_mmap-1m (us)","64.00"
    "lat_ops-double-add (ns)","3.35"
    "lat_ops-double-div (ns)","21.40"
    "lat_ops-double-mul (ns)","4.02"
    "lat_ops-float-add (ns)","3.34"
    "lat_ops-float-div (ns)","12.04"
    "lat_ops-float-mul (ns)","4.01"
    "lat_ops-int-add (ns)","0.67"
    "lat_ops-int-bit (ns)","0.45"
    "lat_ops-int-div (ns)","60.21"
    "lat_ops-int-mod (ns)","8.92"
    "lat_ops-int-mul (ns)","2.09"
    "lat_ops-int64-add (ns)","0.67"
    "lat_ops-int64-bit (ns)","0.45"
    "lat_ops-int64-div (ns)","121.10"
    "lat_ops-int64-mod (ns)","19.60"
    "lat_ops-int64-mul (ns)","2.09"
    "lat_pagefault (us)","0.99"
    "lat_pipe (us)","39.81"
    "lat_proc-exec (us)","730.30"
    "lat_proc-fork (us)","651.24"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","28.48"
    "lat_sem (us)","5.00"
    "lat_sig-catch (us)","5.80"
    "lat_sig-install (us)","0.98"
    "lat_sig-prot (us)","0.67"
    "lat_syscall-fstat (us)","1.72"
    "lat_syscall-null (us)","0.43"
    "lat_syscall-open (us)","250.23"
    "lat_syscall-read (us)","0.66"
    "lat_syscall-stat (us)","4.41"
    "lat_syscall-write (us)","0.53"
    "lat_tcp (us)","0.96"
    "lat_unix (us)","35.52"
    "latency_for_0.50_mb_block_size (nanosec)","12.83"
    "latency_for_1.00_mb_block_size (nanosec)","6.42 (min 0.00, max 12.83)"
    "pipe_bandwidth (MBs)","570.61"
    "pipe_latency (microsec)","39.81"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","28.48"
    "semaphore_latency (microsec)","5.00"
    "signal_handler_latency (microsec)","0.98"
    "signal_handler_overhead (microsec)","5.80"
    "tcp_ip_connection_cost_to_localhost (microsec)","49.37"
    "tcp_latency_using_localhost (microsec)","0.96"




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
    :header: "Benchmarks","am57xx-evm: perf"

    "cpu_clock (MHz)","1500.00"
    "dhrystone_per_mhz (DMIPS/MHz)","3.30"
    "dhrystone_per_second (DhrystoneP)","8695652.00"




Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am57xx-evm: perf"

    "whetstone (MIPS)","5000.00"




Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am57xx-evm: perf"

    "linpack (Kflops)","982496.00"




NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am57xx-evm: perf"

    "assignment (Iterations)","16.48"
    "fourier (Iterations)","25805.00"
    "fp_emulation (Iterations)","283.28"
    "huffman (Iterations)","1447.80"
    "idea (Iterations)","4712.00"
    "lu_decomposition (Iterations)","857.32"
    "neural_net (Iterations)","24.96"
    "numeric_sort (Iterations)","542.04"
    "string_sort (Iterations)","145.88"




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
    :header: "Benchmarks","am57xx-evm: perf"

    "add (MB/s)","3762.50"
    "copy (MB/s)","4149.40"
    "scale (MB/s)","4755.10"
    "triad (MB/s)","3924.00"
















|

Sensor Capture
-------------------------

Capture video frames (MMAP buffers) with v4l2c-ctl and record the
reported fps

.. csv-table:: Sensor Capture
    :header: "Resolution","Format","am57xx-evm: Fps","am57xx-evm: Sensor"

    "1280x800","nv12","30.03 (min 30.03, max 30.04)","ov10635"
    "1280x800","rgb4","30.02","ov10635"
    "320x240","nv12","30.00","ov10635"
    "320x240","rgb4","30.00","ov10635"







|

Graphics SGX/RGX Driver
-------------------------





Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am57xx-evm: Score"

    "Glmark2-DRM","608.00"
    "Glmark2-Wayland","488.00"




























EMMC Driver
-----------
.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.






EMMC EXT4
^^^^^^^^^


















.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT4 Throughput (Mbytes/sec)","am57xx-evm: Write EXT4 CPU Load (%)","am57xx-evm: Read EXT4 Throughput (Mbytes/sec)","am57xx-evm: Read EXT4 CPU Load (%)"

    "102400","12.41 (min 12.30, max 12.47)","1.71 (min 1.49, max 2.12)","69.10","7.87"
    "262144","12.47 (min 12.36, max 12.60)","1.66 (min 1.38, max 2.02)","75.94","5.88"
    "524288","12.43 (min 12.32, max 12.54)","1.56 (min 1.43, max 1.89)","79.56","6.87"
    "1048576","12.42 (min 12.28, max 12.49)","1.63 (min 1.44, max 2.06)","79.39","6.87"
    "5242880","12.33 (min 11.92, max 12.44)","1.60 (min 1.49, max 1.76)","79.66","7.60"





















EMMC EXT2
^^^^^^^^^


















.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT2 Throughput (Mbytes/sec)","am57xx-evm: Write EXT2 CPU Load (%)","am57xx-evm: Read EXT2 Throughput (Mbytes/sec)","am57xx-evm: Read EXT2 CPU Load (%)"

    "102400","11.81 (min 11.62, max 11.88)","1.90 (min 1.36, max 3.35)","69.75","7.02"
    "262144","11.83 (min 11.65, max 11.89)","1.85 (min 1.31, max 3.35)","75.00","8.93"
    "524288","11.87 (min 11.67, max 11.95)","1.78 (min 1.25, max 3.14)","78.66","5.36"
    "1048576","11.83 (min 11.63, max 11.90)","1.81 (min 1.20, max 3.24)","78.28","8.49"
    "5242880","11.70 (min 11.22, max 11.90)","1.74 (min 1.29, max 2.95)","78.60","4.28"



















EMMC VFAT
^^^^^^^^^


















.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am57xx-evm: Write VFAT Throughput (Mbytes/sec)","am57xx-evm: Write VFAT CPU Load (%)","am57xx-evm: Read VFAT Throughput (Mbytes/sec)","am57xx-evm: Read VFAT CPU Load (%)"

    "102400","12.35 (min 11.78, max 12.54)","2.59 (min 1.99, max 4.00)","64.85","6.31"
    "262144","12.36 (min 11.79, max 12.55)","2.33 (min 1.51, max 3.79)","70.97","8.14"
    "524288","12.20 (min 11.78, max 12.49)","2.68 (min 2.16, max 4.06)","74.41","6.83"
    "1048576","12.21 (min 11.75, max 12.51)","2.59 (min 1.98, max 4.12)","74.31","7.22"
    "5242880","12.35 (min 11.79, max 12.52)","2.91 (min 2.33, max 4.39)","74.47","7.86"


























|

SATA Driver
-------------------------



.. rubric::  AM57XX-EVM
   :name: am57xx-evm-sata




.. csv-table:: SATA EXT2 1G
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT2 Throughput (Mbytes/sec)","am57xx-evm: Write EXT2 CPU Load (%)","am57xx-evm: Read EXT2 Throughput (Mbytes/sec)","am57xx-evm: Read EXT2 CPU Load (%)"

    "102400","140.13 (min 115.83, max 170.46)","16.52 (min 10.16, max 29.76)","42.51","3.20"
    "262144","163.19 (min 124.76, max 173.79)","19.58 (min 15.00, max 33.37)","38.53","3.46"
    "524288","170.81 (min 159.32, max 174.15)","20.86 (min 13.95, max 43.20)","38.58","3.43"
    "1048576","171.44 (min 163.86, max 174.77)","21.99 (min 15.60, max 44.15)","37.84","3.25"
    "5242880","171.07 (min 162.34, max 175.72)","21.59 (min 14.71, max 44.30)","38.20","2.96"




.. csv-table:: SATA EXT4 1G
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT4 Throughput (Mbytes/sec)","am57xx-evm: Write EXT4 CPU Load (%)","am57xx-evm: Read EXT4 Throughput (Mbytes/sec)","am57xx-evm: Read EXT4 CPU Load (%)"

    "102400","167.70 (min 160.30, max 170.16)","18.03 (min 15.95, max 24.87)","126.35","10.32"
    "262144","165.64 (min 162.45, max 170.48)","18.19 (min 15.11, max 25.44)","130.87","10.79"
    "524288","165.80 (min 163.47, max 168.67)","18.20 (min 15.56, max 27.47)","128.37","10.28"
    "1048576","165.37 (min 164.18, max 167.73)","18.52 (min 15.50, max 27.88)","129.19","10.39"
    "5242880","165.84 (min 165.21, max 166.93)","18.42 (min 14.85, max 28.33)","128.76","9.99"










-  Filesize used is : 1G
-  SATA II Harddisk used is: Seagate ST3500514NS 500G


mSATA Driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. rubric::  AM57XX-EVM
   :name: am57xx-evm-msata


.. csv-table:: mSATA VFAT SSD 1G
    :header: "Buffer size (bytes)","am57xx-evm: Write VFAT Throughput (Mbytes/sec)","am57xx-evm: Write VFAT CPU Load (%)","am57xx-evm: Read VFAT Throughput (Mbytes/sec)","am57xx-evm: Read VFAT CPU Load (%)"

    "102400","56.59 (min 48.97, max 60.48)","10.30 (min 8.77, max 14.23)","265.53","23.59"
    "262144","58.33 (min 50.73, max 66.51)","10.56 (min 8.41, max 14.40)","270.40","22.65"
    "524288","59.52 (min 51.36, max 68.96)","11.11 (min 9.50, max 14.72)","274.26","20.30"
    "1048576","58.71 (min 51.24, max 65.05)","10.96 (min 9.48, max 14.68)","271.95","21.73"
    "5242880","59.63 (min 49.53, max 64.04)","10.97 (min 9.13, max 14.00)","270.05","21.07"




.. csv-table:: mSATA EXT2 SSD 1G
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT2 Throughput (Mbytes/sec)","am57xx-evm: Write EXT2 CPU Load (%)","am57xx-evm: Read EXT2 Throughput (Mbytes/sec)","am57xx-evm: Read EXT2 CPU Load (%)"

    "102400","59.25 (min 51.03, max 68.93)","6.50 (min 4.21, max 13.61)","263.24","22.31"
    "262144","58.89 (min 52.22, max 65.82)","7.23 (min 4.60, max 15.43)","269.18","22.19"
    "524288","51.30 (min 47.13, max 54.91)","5.66 (min 3.65, max 10.60)","270.18","20.19"
    "1048576","51.31 (min 46.63, max 54.45)","5.77 (min 4.30, max 10.86)","268.23","21.07"
    "5242880","52.69 (min 46.07, max 57.99)","5.84 (min 4.65, max 9.64)","267.89","20.77"




.. csv-table:: mSATA EXT4 SSD 1G
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT4 Throughput (Mbytes/sec)","am57xx-evm: Write EXT4 CPU Load (%)","am57xx-evm: Read EXT4 Throughput (Mbytes/sec)","am57xx-evm: Read EXT4 CPU Load (%)"

    "102400","63.22 (min 57.04, max 67.61)","6.45 (min 5.14, max 8.93)","255.04","20.39"
    "262144","58.99 (min 53.14, max 67.92)","6.10 (min 4.79, max 9.77)","205.95","14.76"
    "524288","59.36 (min 52.85, max 67.73)","6.26 (min 4.74, max 9.13)","213.49","16.02"
    "1048576","52.04 (min 49.26, max 55.64)","5.56 (min 4.70, max 8.63)","256.40","19.44"
    "5242880","54.28 (min 51.70, max 55.94)","5.76 (min 4.79, max 7.77)","283.18","21.67"



-  Filesize used is : 1G
-  MSATA Harddisk used is: SMS200S3/30G Kingston mSATA SSD drive




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
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT4 Throughput (Mbytes/sec)","am57xx-evm: Write EXT4 CPU Load (%)","am57xx-evm: Read EXT4 Throughput (Mbytes/sec)","am57xx-evm: Read EXT4 CPU Load (%)"

    "1m","20.20","1.12","21.70","1.23"
    "4m","19.70","1.05","21.70","1.19"
    "4k","2.65","2.54","9.11","6.69"
    "256k","19.20","1.28","21.50","1.32"













MMC EXT4
^^^^^^^^








































.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am57xx-evm: Write Raw Throughput (Mbytes/sec)","am57xx-evm: Write Raw CPU Load (%)","am57xx-evm: Read Raw Throughput (Mbytes/sec)","am57xx-evm: Read Raw CPU Load (%)"

    "102400","20.40 (min 19.84, max 20.77)","2.59 (min 2.31, max 2.97)","20.68","2.08"
    "262144","19.32 (min 18.92, max 20.22)","2.57 (min 1.93, max 3.60)","20.86","1.11"
    "524288","19.70 (min 19.54, max 19.91)","2.69 (min 2.06, max 4.21)","21.08","1.81"
    "1048576","19.17 (min 18.65, max 19.55)","2.67 (min 2.21, max 3.29)","22.96","2.19"
    "5242880","19.74 (min 19.45, max 20.49)","2.63 (min 2.07, max 4.13)","22.82","2.18"



















MMC EXT3
^^^^^^^^


























.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am57xx-evm: Write Raw Throughput (Mbytes/sec)","am57xx-evm: Write Raw CPU Load (%)","am57xx-evm: Read Raw Throughput (Mbytes/sec)","am57xx-evm: Read Raw CPU Load (%)"

    "102400","20.54 (min 19.22, max 21.15)","3.19 (min 2.31, max 5.63)","22.18","2.44"
    "262144","19.22 (min 18.61, max 19.48)","3.30 (min 2.61, max 5.20)","22.62","1.74"
    "524288","19.15 (min 18.50, max 19.73)","3.06 (min 2.31, max 4.94)","22.24","2.54"
    "1048576","20.17 (min 19.34, max 20.58)","3.16 (min 2.24, max 5.40)","22.38","2.04"
    "5242880","20.29 (min 19.49, max 20.80)","3.37 (min 2.69, max 5.26)","22.86","2.19"



















MMC EXT2
^^^^^^^^








































.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am57xx-evm: Write Raw Throughput (Mbytes/sec)","am57xx-evm: Write Raw CPU Load (%)","am57xx-evm: Read Raw Throughput (Mbytes/sec)","am57xx-evm: Read Raw CPU Load (%)"

    "102400","20.67 (min 20.06, max 20.94)","2.96 (min 2.30, max 4.84)","22.12","2.53"
    "262144","19.79 (min 19.28, max 20.03)","2.87 (min 2.21, max 4.65)","22.65","2.27"
    "524288","19.22 (min 18.59, max 19.45)","2.79 (min 2.23, max 4.48)","22.88","1.86"
    "1048576","19.36 (min 19.03, max 19.51)","2.75 (min 2.23, max 4.50)","22.88","2.29"
    "5242880","20.44 (min 19.88, max 20.64)","3.43 (min 2.65, max 5.06)","22.89","2.19"






















The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option




UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^








































.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am57xx-evm: Write Throughput (Kbytes/sec)","am57xx-evm: Read Throughput (Kbytes/sec)"

    "400000","18123.89","21903.74"
    "800000","19504.76","22260.87"
    "1000000","21113.40","22474.62"












The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)




|

USB Driver
-------------------------



USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^










.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am57xx-evm: Throughput (MB/sec)"

    "150","43.80"




.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am57xx-evm: Throughput (MB/sec)"

    "150","37.90"











|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am57xx-evm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","71209.64"
    "aes-128-cbc","16","54462.65"
    "aes-128-cbc","16384","71625.39"
    "aes-128-cbc","256","69442.73"
    "aes-128-cbc","64","64984.15"
    "aes-128-cbc","8192","71609.00"
    "aes-128-ecb","1024","75841.54"
    "aes-128-ecb","16","62518.99"
    "aes-128-ecb","16384","76054.53"
    "aes-128-ecb","256","74816.43"
    "aes-128-ecb","64","70779.20"
    "aes-128-ecb","8192","76125.53"
    "aes-192-cbc","1024","61555.37"
    "aes-192-cbc","16","48677.77"
    "aes-192-cbc","16384","61844.14"
    "aes-192-cbc","256","60566.87"
    "aes-192-cbc","64","56886.34"
    "aes-192-cbc","8192","61838.68"
    "aes-192-ecb","1024","64490.84"
    "aes-192-ecb","16","52108.36"
    "aes-192-ecb","16384","64826.03"
    "aes-192-ecb","256","63379.54"
    "aes-192-ecb","64","58961.73"
    "aes-192-ecb","8192","64801.45"
    "aes-256-cbc","1024","53803.01"
    "aes-256-cbc","16","43623.72"
    "aes-256-cbc","16384","54012.59"
    "aes-256-cbc","256","53057.11"
    "aes-256-cbc","64","50207.96"
    "aes-256-cbc","8192","54031.70"
    "aes-256-ecb","1024","52781.74"
    "aes-256-ecb","16","46544.11"
    "aes-256-ecb","16384","52909.40"
    "aes-256-ecb","256","52322.90"
    "aes-256-ecb","64","49855.25"
    "aes-256-ecb","8192","52928.51"
    "des3","1024","10205.53"
    "des3","16","9722.10"
    "des3","16384","10207.23"
    "des3","256","10186.84"
    "des3","64","10087.13"
    "des3","8192","10193.58"
    "md5","1024","199990.61"
    "md5","16","15559.15"
    "md5","16384","248452.44"
    "md5","256","124547.84"
    "md5","64","49533.61"
    "md5","8192","244228.10"
    "sha1","1024","211035.14"
    "sha1","16","15236.97"
    "sha1","16384","266704.21"
    "sha1","256","127757.91"
    "sha1","64","48907.46"
    "sha1","8192","262329.69"
    "sha224","1024","106972.84"
    "sha224","16","11751.70"
    "sha224","16384","123589.97"
    "sha224","256","74829.57"
    "sha224","64","34072.26"
    "sha224","8192","122317.48"
    "sha256","1024","106204.50"
    "sha256","16","11693.79"
    "sha256","16384","123426.13"
    "sha256","256","74427.48"
    "sha256","64","33660.46"
    "sha256","8192","122221.91"
    "sha512","1024","78953.47"
    "sha512","16","6912.48"
    "sha512","16384","94901.59"
    "sha512","256","51365.12"
    "sha512","64","26578.43"
    "sha512","8192","93675.52"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am57xx-evm: CPU Load"

    "aes-128-cbc","99.00"
    "aes-128-ecb","99.00"
    "aes-192-cbc","100.00"
    "aes-192-ecb","99.00"
    "aes-256-cbc","99.00"
    "aes-256-ecb","99.00"
    "des3","99.00"
    "md5","99.00"
    "sha1","99.00"
    "sha224","100.00"
    "sha256","99.00"
    "sha384","84.00"
    "sha512","100.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc










Performance and Benchmarks not available in this release.



