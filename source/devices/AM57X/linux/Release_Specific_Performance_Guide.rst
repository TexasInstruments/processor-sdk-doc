
======================================
 Linux 09.03 Performance Guide
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

    "af_unix_sock_stream_latency (microsec)","29.73"
    "af_unix_socket_stream_bandwidth (MBs)","2730.37"
    "bw_file_rd-io-1mb (MB/s)","1337.00"
    "bw_file_rd-o2c-1mb (MB/s)","1063.93"
    "bw_mem-bcopy-16mb (MB/s)","1972.14"
    "bw_mem-bcopy-1mb (MB/s)","5111.28"
    "bw_mem-bcopy-2mb (MB/s)","2727.26"
    "bw_mem-bcopy-4mb (MB/s)","2087.14"
    "bw_mem-bcopy-8mb (MB/s)","1992.03"
    "bw_mem-bzero-16mb (MB/s)","5155.88"
    "bw_mem-bzero-1mb (MB/s)","5034.11 (min 4956.93, max 5111.28)"
    "bw_mem-bzero-2mb (MB/s)","4259.75 (min 2727.26, max 5792.23)"
    "bw_mem-bzero-4mb (MB/s)","3805.05 (min 2087.14, max 5522.95)"
    "bw_mem-bzero-8mb (MB/s)","3652.28 (min 1992.03, max 5312.53)"
    "bw_mem-cp-16mb (MB/s)","1059.74"
    "bw_mem-cp-1mb (MB/s)","7469.40 (min 3166.74, max 11772.05)"
    "bw_mem-cp-2mb (MB/s)","4440.05 (min 1233.81, max 7646.28)"
    "bw_mem-cp-4mb (MB/s)","1365.39 (min 990.73, max 1740.04)"
    "bw_mem-cp-8mb (MB/s)","1234.22 (min 990.75, max 1477.68)"
    "bw_mem-fcp-16mb (MB/s)","515.31"
    "bw_mem-fcp-1mb (MB/s)","3999.24 (min 3041.54, max 4956.93)"
    "bw_mem-fcp-2mb (MB/s)","3657.37 (min 1522.50, max 5792.23)"
    "bw_mem-fcp-4mb (MB/s)","3060.95 (min 598.94, max 5522.95)"
    "bw_mem-fcp-8mb (MB/s)","2916.48 (min 520.42, max 5312.53)"
    "bw_mem-frd-16mb (MB/s)","1604.65"
    "bw_mem-frd-1mb (MB/s)","2755.85 (min 2470.15, max 3041.54)"
    "bw_mem-frd-2mb (MB/s)","1744.98 (min 1522.50, max 1967.46)"
    "bw_mem-frd-4mb (MB/s)","1149.09 (min 598.94, max 1699.24)"
    "bw_mem-frd-8mb (MB/s)","1069.38 (min 520.42, max 1618.34)"
    "bw_mem-fwr-16mb (MB/s)","1456.75"
    "bw_mem-fwr-1mb (MB/s)","7121.10 (min 2470.15, max 11772.05)"
    "bw_mem-fwr-2mb (MB/s)","4806.87 (min 1967.46, max 7646.28)"
    "bw_mem-fwr-4mb (MB/s)","1719.64 (min 1699.24, max 1740.04)"
    "bw_mem-fwr-8mb (MB/s)","1548.01 (min 1477.68, max 1618.34)"
    "bw_mem-rd-16mb (MB/s)","2515.13"
    "bw_mem-rd-1mb (MB/s)","8568.15 (min 3697.63, max 13438.66)"
    "bw_mem-rd-2mb (MB/s)","5171.48 (min 1930.57, max 8412.39)"
    "bw_mem-rd-4mb (MB/s)","1998.20 (min 1635.83, max 2360.57)"
    "bw_mem-rd-8mb (MB/s)","1932.62 (min 1331.78, max 2533.45)"
    "bw_mem-rdwr-16mb (MB/s)","877.24"
    "bw_mem-rdwr-1mb (MB/s)","4872.24 (min 3166.74, max 6577.73)"
    "bw_mem-rdwr-2mb (MB/s)","1975.60 (min 1233.81, max 2717.39)"
    "bw_mem-rdwr-4mb (MB/s)","961.45 (min 932.17, max 990.73)"
    "bw_mem-rdwr-8mb (MB/s)","939.95 (min 889.14, max 990.75)"
    "bw_mem-wr-16mb (MB/s)","1302.08"
    "bw_mem-wr-1mb (MB/s)","10008.20 (min 6577.73, max 13438.66)"
    "bw_mem-wr-2mb (MB/s)","5564.89 (min 2717.39, max 8412.39)"
    "bw_mem-wr-4mb (MB/s)","1284.00 (min 932.17, max 1635.83)"
    "bw_mem-wr-8mb (MB/s)","1110.46 (min 889.14, max 1331.78)"
    "bw_mmap_rd-mo-1mb (MB/s)","2555.11"
    "bw_mmap_rd-o2c-1mb (MB/s)","1297.58"
    "bw_pipe (MB/s)","653.56"
    "bw_unix (MB/s)","2730.37"
    "lat_connect (us)","51.28"
    "lat_ctx-2-128k (us)","3.31"
    "lat_ctx-2-256k (us)","27.96"
    "lat_ctx-4-128k (us)","11.24"
    "lat_ctx-4-256k (us)","22.22"
    "lat_fs-0k (num_files)","3289.00"
    "lat_fs-10k (num_files)","1420.00"
    "lat_fs-1k (num_files)","1971.00"
    "lat_fs-4k (num_files)","2076.00"
    "lat_mem_rd-stride128-sz1000k (ns)","12.86"
    "lat_mem_rd-stride128-sz125k (ns)","12.70"
    "lat_mem_rd-stride128-sz250k (ns)","12.84"
    "lat_mem_rd-stride128-sz31k (ns)","6.49"
    "lat_mem_rd-stride128-sz50 (ns)","2.68"
    "lat_mem_rd-stride128-sz500k (ns)","12.85"
    "lat_mem_rd-stride128-sz62k (ns)","12.10"
    "lat_mmap-1m (us)","61.00"
    "lat_ops-double-add (ns)","5.01"
    "lat_ops-double-div (ns)","32.09"
    "lat_ops-double-mul (ns)","6.02"
    "lat_ops-float-add (ns)","5.01"
    "lat_ops-float-div (ns)","18.01"
    "lat_ops-float-mul (ns)","6.01"
    "lat_ops-int-add (ns)","0.67"
    "lat_ops-int-bit (ns)","0.45"
    "lat_ops-int-div (ns)","60.07"
    "lat_ops-int-mod (ns)","8.91"
    "lat_ops-int-mul (ns)","2.09"
    "lat_ops-int64-add (ns)","0.85"
    "lat_ops-int64-bit (ns)","0.57"
    "lat_ops-int64-div (ns)","175.26"
    "lat_ops-int64-mod (ns)","29.46"
    "lat_ops-int64-mul (ns)","2.68"
    "lat_pagefault (us)","0.87"
    "lat_pipe (us)","44.89"
    "lat_proc-exec (us)","694.13"
    "lat_proc-fork (us)","609.89"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","28.38"
    "lat_sem (us)","4.85"
    "lat_sig-catch (us)","5.12"
    "lat_sig-install (us)","1.45"
    "lat_sig-prot (us)","0.92"
    "lat_syscall-fstat (us)","2.86"
    "lat_syscall-null (us)","0.43"
    "lat_syscall-open (us)","151.17"
    "lat_syscall-read (us)","0.66"
    "lat_syscall-stat (us)","4.29"
    "lat_syscall-write (us)","0.52"
    "lat_tcp (us)","1.10"
    "lat_unix (us)","29.73"
    "latency_for_0.50_mb_block_size (nanosec)","12.85"
    "latency_for_1.00_mb_block_size (nanosec)","6.43 (min 0.00, max 12.86)"
    "pipe_bandwidth (MBs)","653.56"
    "pipe_latency (microsec)","44.89"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","28.38"
    "semaphore_latency (microsec)","4.85"
    "signal_handler_latency (microsec)","1.45"
    "signal_handler_overhead (microsec)","5.12"
    "tcp_ip_connection_cost_to_localhost (microsec)","51.28"
    "tcp_latency_using_localhost (microsec)","1.10"




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

    "cpu_clock (MHz)","1000.00"
    "dhrystone_per_mhz (DMIPS/MHz)","2.00"
    "dhrystone_per_second (DhrystoneP)","3508772.00"




Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am57xx-evm: perf"

    "whetstone (MIPS)","2500.00"




Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am57xx-evm: perf"

    "linpack (Kflops)","652105.00"




NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am57xx-evm: perf"

    "assignment (Iterations)","12.40"
    "fourier (Iterations)","20642.00"
    "fp_emulation (Iterations)","106.96"
    "huffman (Iterations)","1086.90"
    "idea (Iterations)","3433.60"
    "lu_decomposition (Iterations)","588.61"
    "neural_net (Iterations)","18.87"
    "numeric_sort (Iterations)","407.41"
    "string_sort (Iterations)","95.65"




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

    "add (MB/s)","3650.30"
    "copy (MB/s)","3988.00"
    "scale (MB/s)","4580.20"
    "triad (MB/s)","3785.50"



 



 
 

 



|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am57xx-evm: Throughput (bits/sec)","am57xx-evm: CPU Load (%)"

    "8000","255982.00","0.16"
    "11025","352748.00","0.18"
    "16000","511981.00","0.19"
    "22050","705505.00","0.24"
    "24000","705485.00","0.25"
    "32000","1023884.00","0.30"
    "44100","1411453.00","0.40"
    "48000","1536062.00","0.62"
    "88200","2822359.00","0.90"
    "96000","3071826.00","0.82"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am57xx-evm: Throughput (bits/sec)","am57xx-evm: CPU Load (%)"

    "8000","256092.00","0.16"
    "11025","352909.00","0.23"
    "16000","512200.00","0.23"
    "22050","705812.00","0.30"
    "24000","705793.00","0.26"
    "32000","1024354.00","0.33"
    "44100","1412080.00","0.52"
    "48000","1536752.00","0.56"
    "88200","2823630.00","0.87"
    "96000","3073213.00","0.09"

 
 



|

Sensor Capture
-------------------------

Capture video frames (MMAP buffers) with v4l2c-ctl and record the
reported fps

.. csv-table:: Sensor Capture
    :header: "Resolution","Format","am57xx-evm: Fps","am57xx-evm: Sensor"

    "1280x800","nv12","30.02 (min 30.02, max 30.03)","ov10635"
    "1280x800","rgb4","30.02","ov10635"
    "320x240","nv12","30.00","ov10635"
    "320x240","rgb4","30.03 (min 30.03, max 30.04)","ov10635"



 



|

Graphics SGX/RGX Driver
-------------------------
 




Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am57xx-evm: Score"

    "Glmark2-DRM","55.00"
    "Glmark2-Wayland","471.00"

 
 

 

 

 

 

 

 

 

 

 

 

 



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

    "102400","12.28 (min 12.26, max 12.30)","2.11 (min 1.59, max 3.68)","70.20","6.46"
    "262144","12.25 (min 12.12, max 12.29)","2.00 (min 1.53, max 3.26)","72.96","6.36"
    "524288","12.15 (min 11.78, max 12.28)","1.99 (min 1.47, max 3.50)","78.02","7.81"
    "1048576","12.26 (min 12.19, max 12.30)","1.96 (min 1.47, max 3.20)","79.69","7.25"
    "5242880","12.29 (min 12.16, max 12.35)","2.10 (min 1.66, max 3.31)","79.53","7.25"

 

 

 

 

 

 

 

 
 

 


EMMC EXT2
^^^^^^^^^

 

 

 

 

 

 

 

 


.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT2 Throughput (Mbytes/sec)","am57xx-evm: Write EXT2 CPU Load (%)","am57xx-evm: Read EXT2 Throughput (Mbytes/sec)","am57xx-evm: Read EXT2 CPU Load (%)"

    "102400","12.04 (min 11.84, max 12.11)","2.08 (min 1.39, max 3.91)","69.47","5.46"
    "262144","12.02 (min 11.77, max 12.10)","2.03 (min 1.33, max 4.16)","72.65","6.67"
    "524288","12.04 (min 11.84, max 12.11)","2.11 (min 1.68, max 3.52)","77.45","8.42"
    "1048576","12.04 (min 11.86, max 12.10)","2.14 (min 1.51, max 3.74)","78.90","7.52"
    "5242880","12.02 (min 11.76, max 12.10)","1.96 (min 1.28, max 3.60)","78.66","7.89"

 

 

 

 

 

 

 

 
 


EMMC VFAT
^^^^^^^^^

 

 

 

 

 

 

 

 


.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am57xx-evm: Write VFAT Throughput (Mbytes/sec)","am57xx-evm: Write VFAT CPU Load (%)","am57xx-evm: Read VFAT Throughput (Mbytes/sec)","am57xx-evm: Read VFAT CPU Load (%)"

    "102400","12.16 (min 11.60, max 12.31)","2.41 (min 1.83, max 4.22)","66.33","7.35"
    "262144","12.15 (min 11.61, max 12.30)","2.47 (min 1.83, max 4.11)","68.44","8.20"
    "524288","12.16 (min 11.60, max 12.32)","2.29 (min 1.72, max 3.66)","70.66","7.17"
    "1048576","12.16 (min 11.62, max 12.31)","2.40 (min 1.66, max 3.94)","74.92","7.53"
    "5242880","12.16 (min 11.61, max 12.32)","2.35 (min 1.78, max 3.67)","74.79","8.21"

 

 

 

 

 

 

 

 
 

 
 

 



|

SATA Driver
-------------------------


mSATA Driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^
 


.. rubric::  AM57XX-EVM
   :name: am57xx-evm-msata


.. csv-table:: mSATA VFAT SSD 1G
    :header: "Buffer size (bytes)","am57xx-evm: Write VFAT Throughput (Mbytes/sec)","am57xx-evm: Write VFAT CPU Load (%)","am57xx-evm: Read VFAT Throughput (Mbytes/sec)","am57xx-evm: Read VFAT CPU Load (%)"

    "102400","47.45 (min 32.60, max 54.09)","19.56 (min 4.50, max 74.52)","265.74","22.59"
    "262144","56.72 (min 48.87, max 61.95)","8.41 (min 6.55, max 13.75)","267.68","22.43"
    "524288","57.38 (min 52.21, max 63.05)","8.38 (min 5.67, max 14.99)","270.51","20.14"
    "1048576","59.05 (min 52.01, max 63.84)","8.64 (min 6.68, max 14.94)","271.57","21.00"
    "5242880","58.84 (min 50.44, max 65.41)","8.18 (min 5.64, max 14.61)","269.09","20.40"




.. csv-table:: mSATA EXT2 SSD 1G
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT2 Throughput (Mbytes/sec)","am57xx-evm: Write EXT2 CPU Load (%)","am57xx-evm: Read EXT2 Throughput (Mbytes/sec)","am57xx-evm: Read EXT2 CPU Load (%)"

    "102400","57.79 (min 50.41, max 68.72)","5.04 (min 3.25, max 10.83)","235.46","19.57"
    "262144","57.27 (min 51.64, max 64.41)","5.21 (min 3.28, max 12.21)","266.31","22.13"
    "524288","49.87 (min 45.82, max 54.31)","4.15 (min 2.38, max 7.94)","239.61","17.68"
    "1048576","50.07 (min 45.30, max 54.48)","3.74 (min 2.96, max 6.03)","238.16","18.32"
    "5242880","48.51 (min 45.66, max 50.85)","4.01 (min 2.98, max 7.00)","265.13","20.65"




.. csv-table:: mSATA EXT4 SSD 1G
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT4 Throughput (Mbytes/sec)","am57xx-evm: Write EXT4 CPU Load (%)","am57xx-evm: Read EXT4 Throughput (Mbytes/sec)","am57xx-evm: Read EXT4 CPU Load (%)"

    "102400","60.49 (min 55.29, max 66.53)","4.87 (min 3.53, max 8.93)","255.62","22.24"
    "262144","58.56 (min 55.73, max 60.58)","4.93 (min 3.92, max 8.37)","253.19","21.20"
    "524288","60.32 (min 55.69, max 66.48)","5.50 (min 3.97, max 10.20)","262.22","19.71"
    "1048576","55.50 (min 51.68, max 59.46)","4.91 (min 3.60, max 8.32)","281.45","21.97"
    "5242880","54.91 (min 51.15, max 58.39)","4.57 (min 3.63, max 7.42)","282.20","21.82"



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

    "1m","14.00","0.70","22.20","1.17"
    "4m","14.50","0.54","22.80","1.07"
    "4k","4.80","5.24","10.70","9.47"
    "256k","13.70","1.29","23.60","1.31"

 

 

 

 
 

 


MMC EXT4
^^^^^^^^

 

 

 

 

 

 

 

 

 

 

 

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am57xx-evm: Write Raw Throughput (Mbytes/sec)","am57xx-evm: Write Raw CPU Load (%)","am57xx-evm: Read Raw Throughput (Mbytes/sec)","am57xx-evm: Read Raw CPU Load (%)"

    "102400","15.41 (min 15.28, max 15.63)","2.19 (min 1.69, max 3.75)","19.87","2.00"
    "262144","15.11 (min 14.86, max 15.36)","2.09 (min 1.68, max 2.83)","21.24","1.93"
    "524288","15.27 (min 14.81, max 15.66)","2.35 (min 1.75, max 3.90)","21.51","1.65"
    "1048576","15.20 (min 14.83, max 15.52)","2.12 (min 1.69, max 3.09)","20.34","1.84"
    "5242880","15.04 (min 14.68, max 15.23)","2.16 (min 1.58, max 3.52)","22.94","2.19"

 

 

 

 

 

 

 

 
 


MMC EXT3
^^^^^^^^

 

 

 

 

 

 

 

 

 

 

 

 


.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am57xx-evm: Write Raw Throughput (Mbytes/sec)","am57xx-evm: Write Raw CPU Load (%)","am57xx-evm: Read Raw Throughput (Mbytes/sec)","am57xx-evm: Read Raw CPU Load (%)"

    "102400","15.26 (min 14.85, max 15.50)","2.69 (min 2.08, max 4.84)","22.13","1.81"
    "262144","15.30 (min 15.07, max 15.64)","2.80 (min 2.10, max 5.01)","21.88","1.69"
    "524288","15.46 (min 14.79, max 16.11)","2.73 (min 2.03, max 4.75)","22.23","2.34"
    "1048576","15.33 (min 14.88, max 15.72)","2.57 (min 1.86, max 4.84)","22.32","2.13"
    "5242880","15.39 (min 15.00, max 15.84)","2.84 (min 1.81, max 5.77)","22.80","2.29"

 

 

 

 

 

 

 

 
 


MMC EXT2
^^^^^^^^

 

 

 

 

 

 

 

 

 

 

 

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am57xx-evm: Write Raw Throughput (Mbytes/sec)","am57xx-evm: Write Raw CPU Load (%)","am57xx-evm: Read Raw Throughput (Mbytes/sec)","am57xx-evm: Read Raw CPU Load (%)"

    "102400","15.15 (min 14.79, max 15.49)","2.40 (min 1.71, max 4.53)","22.18","2.34"
    "262144","15.48 (min 14.88, max 15.90)","2.52 (min 1.58, max 4.25)","22.40","2.36"
    "524288","15.24 (min 14.56, max 15.66)","2.38 (min 1.72, max 3.99)","22.73","2.39"
    "1048576","15.28 (min 14.93, max 16.01)","2.39 (min 1.69, max 4.76)","22.36","2.45"
    "5242880","15.29 (min 14.95, max 15.58)","2.53 (min 1.86, max 4.55)","22.81","1.86"

 

 

 

 

 

 

 

 
 

 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 



UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am57xx-evm: Write Throughput (Kbytes/sec)","am57xx-evm: Read Throughput (Kbytes/sec)"

    "400000","19320.75","19051.16"
    "800000","21277.92","20686.87"
    "1000000","21389.03","21614.78"

 

 

 

 
 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 



|

USB Driver
-------------------------
 


USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^










.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am57xx-evm: Throughput (MB/sec)"

    "150","44.40"




.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am57xx-evm: Throughput (MB/sec)"

    "150","39.30"





 
 
 



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am57xx-evm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","71243.43"
    "aes-128-cbc","16","54257.05"
    "aes-128-cbc","16384","71701.85"
    "aes-128-cbc","256","69970.77"
    "aes-128-cbc","64","65082.33"
    "aes-128-cbc","8192","71655.42"
    "aes-128-ecb","1024","75778.39"
    "aes-128-ecb","16","62406.91"
    "aes-128-ecb","16384","76158.29"
    "aes-128-ecb","256","74767.62"
    "aes-128-ecb","64","70714.33"
    "aes-128-ecb","8192","76024.49"
    "aes-192-cbc","1024","61508.61"
    "aes-192-cbc","16","48512.16"
    "aes-192-cbc","16384","61855.06"
    "aes-192-cbc","256","60502.36"
    "aes-192-cbc","64","56866.84"
    "aes-192-cbc","8192","61606.57"
    "aes-192-ecb","1024","64331.43"
    "aes-192-ecb","16","51476.45"
    "aes-192-ecb","16384","64716.80"
    "aes-192-ecb","256","63234.05"
    "aes-192-ecb","64","59280.51"
    "aes-192-ecb","8192","64637.61"
    "aes-256-cbc","1024","53437.10"
    "aes-256-cbc","16","43606.70"
    "aes-256-cbc","16384","53794.13"
    "aes-256-cbc","256","52706.82"
    "aes-256-cbc","64","49939.41"
    "aes-256-cbc","8192","53652.14"
    "aes-256-ecb","1024","52660.57"
    "aes-256-ecb","16","46397.49"
    "aes-256-ecb","16384","52964.01"
    "aes-256-ecb","256","52202.24"
    "aes-256-ecb","64","50147.82"
    "aes-256-ecb","8192","52781.06"
    "des3","1024","10148.86"
    "des3","16","9582.22"
    "des3","16384","10152.62"
    "des3","256","10117.55"
    "des3","64","9995.33"
    "des3","8192","10152.62"
    "md5","1024","203046.91"
    "md5","16","16008.87"
    "md5","16384","249118.72"
    "md5","256","127807.91"
    "md5","64","51321.30"
    "md5","8192","244861.61"
    "sha1","1024","213876.05"
    "sha1","16","16418.28"
    "sha1","16384","266807.98"
    "sha1","256","132984.92"
    "sha1","64","51625.43"
    "sha1","8192","262042.97"
    "sha224","1024","106668.71"
    "sha224","16","11641.73"
    "sha224","16384","123371.52"
    "sha224","256","74484.14"
    "sha224","64","33706.15"
    "sha224","8192","122129.07"
    "sha256","1024","106542.42"
    "sha256","16","11639.07"
    "sha256","16384","123540.82"
    "sha256","256","73920.17"
    "sha256","64","33190.81"
    "sha256","8192","122262.87"
    "sha512","1024","78967.81"
    "sha512","16","6993.66"
    "sha512","16384","94863.36"
    "sha512","256","51738.54"
    "sha512","64","28019.39"
    "sha512","8192","93129.39"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am57xx-evm: CPU Load"

    "aes-128-cbc","99.00"
    "aes-128-ecb","100.00"
    "aes-192-cbc","99.00"
    "aes-192-ecb","99.00"
    "aes-256-cbc","99.00"
    "aes-256-ecb","99.00"
    "des3","99.00"
    "md5","100.00"
    "sha1","99.00"
    "sha224","99.00"
    "sha256","100.00"
    "sha386","78.00"
    "sha512","99.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

 


IPSec Hardware Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note: queue\_len is set to 300 and software fallback threshold set to 9
to enable software support for optimal performance

.. csv-table:: IPSec Hardware Performance
    :header: "Algorithm","am57xx-evm: Throughput (Mbps)","am57xx-evm: Packets/Sec","am57xx-evm: CPU Load"

    "3des","39.40","3.00","58.78"
    "aes128","0.20","0.00","49.51"
    "aes192","4.10","0.00","52.09"
    "aes256","39.10","3.00","66.81"




IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","am57xx-evm: Throughput (Mbps)","am57xx-evm: Packets/Sec","am57xx-evm: CPU Load"

    "aes128","173.50","15.00","54.59"
    "aes192","177.80","15.00","55.24"

 
 

 

Performance and Benchmarks not available in this release.




