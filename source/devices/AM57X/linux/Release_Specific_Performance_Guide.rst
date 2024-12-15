======================================
 Linux Performance Guide
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

|

.. rubric::  About This Manual
   :name: about-this-manual-kernel-perf-guide

This document provides performance data for each of the device drivers
which are part of the Process SDK Linux package. This document should be
used in conjunction with release notes and user guides provided with the
Process SDK Linux package for information on specific issues present
with drivers included in a particular release.

.. rubric::  If You Need Assistance
   :name: if-you-need-assistance-kernel-perf-guide

For further information or to report any problems, contact
http://community.ti.com/ or http://support.ti.com/


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

**Bandwidth**: bw_mem_bcopy-N, where N is is equal to or smaller than the cache size at
a given level measures the achievable memory bandwidth from software doing
a memcpy() type operation. Typical use is for external memory bandwidth
calculation. The bandwidth is calculated as byte read and written counts
as 1 which should be roughly half of STREAM copy result.

.. csv-table::
    :header: "Benchmarks","am57xx-evm: perf"

    "af_unix_sock_stream_latency (microsec)","34.31"
    "af_unix_socket_stream_bandwidth (MBs)","1643.24"
    "bw_file_rd-io-1mb (MB/s)","1634.14"
    "bw_file_rd-o2c-1mb (MB/s)","948.77"
    "bw_mem-bcopy-16mb (MB/s)","1960.06"
    "bw_mem-bcopy-1mb (MB/s)","4991.05"
    "bw_mem-bcopy-2mb (MB/s)","2955.49"
    "bw_mem-bcopy-4mb (MB/s)","2075.05"
    "bw_mem-bcopy-8mb (MB/s)","1986.10"
    "bw_mem-bzero-16mb (MB/s)","5140.15"
    "bw_mem-bzero-1mb (MB/s)","5524.33 (min 4991.05, max 6057.60)"
    "bw_mem-bzero-2mb (MB/s)","4388.55 (min 2955.49, max 5821.60)"
    "bw_mem-bzero-4mb (MB/s)","3783.52 (min 2075.05, max 5491.99)"
    "bw_mem-bzero-8mb (MB/s)","3621.17 (min 1986.10, max 5256.24)"
    "bw_mem-cp-16mb (MB/s)","1048.63"
    "bw_mem-cp-1mb (MB/s)","4775.13 (min 3540.31, max 6009.95)"
    "bw_mem-cp-2mb (MB/s)","3457.07 (min 1223.46, max 5690.68)"
    "bw_mem-cp-4mb (MB/s)","3288.05 (min 1068.47, max 5507.62)"
    "bw_mem-cp-8mb (MB/s)","3148.87 (min 1028.08, max 5269.66)"
    "bw_mem-fcp-16mb (MB/s)","1147.28"
    "bw_mem-fcp-1mb (MB/s)","4563.51 (min 3069.42, max 6057.60)"
    "bw_mem-fcp-2mb (MB/s)","3535.80 (min 1250.00, max 5821.60)"
    "bw_mem-fcp-4mb (MB/s)","3320.88 (min 1149.76, max 5491.99)"
    "bw_mem-fcp-8mb (MB/s)","3205.57 (min 1154.90, max 5256.24)"
    "bw_mem-frd-16mb (MB/s)","1057.08"
    "bw_mem-frd-1mb (MB/s)","3077.92 (min 3069.42, max 3086.42)"
    "bw_mem-frd-2mb (MB/s)","1767.06 (min 1250.00, max 2284.11)"
    "bw_mem-frd-4mb (MB/s)","1178.98 (min 1149.76, max 1208.19)"
    "bw_mem-frd-8mb (MB/s)","1113.57 (min 1072.24, max 1154.90)"
    "bw_mem-fwr-16mb (MB/s)","5115.09"
    "bw_mem-fwr-1mb (MB/s)","4548.19 (min 3086.42, max 6009.95)"
    "bw_mem-fwr-2mb (MB/s)","3987.40 (min 2284.11, max 5690.68)"
    "bw_mem-fwr-4mb (MB/s)","3357.91 (min 1208.19, max 5507.62)"
    "bw_mem-fwr-8mb (MB/s)","3170.95 (min 1072.24, max 5269.66)"
    "bw_mem-rd-16mb (MB/s)","3048.20"
    "bw_mem-rd-1mb (MB/s)","12158.45 (min 10893.45, max 13423.44)"
    "bw_mem-rd-2mb (MB/s)","7872.41 (min 6918.53, max 8826.29)"
    "bw_mem-rd-4mb (MB/s)","2492.86 (min 1634.39, max 3351.33)"
    "bw_mem-rd-8mb (MB/s)","2202.48 (min 1320.68, max 3084.28)"
    "bw_mem-rdwr-16mb (MB/s)","1188.97"
    "bw_mem-rdwr-1mb (MB/s)","5551.32 (min 3540.31, max 7562.32)"
    "bw_mem-rdwr-2mb (MB/s)","2346.10 (min 1223.46, max 3468.74)"
    "bw_mem-rdwr-4mb (MB/s)","1225.98 (min 1068.47, max 1383.48)"
    "bw_mem-rdwr-8mb (MB/s)","1120.84 (min 1028.08, max 1213.59)"
    "bw_mem-wr-16mb (MB/s)","1288.24"
    "bw_mem-wr-1mb (MB/s)","10492.88 (min 7562.32, max 13423.44)"
    "bw_mem-wr-2mb (MB/s)","5193.64 (min 3468.74, max 6918.53)"
    "bw_mem-wr-4mb (MB/s)","1508.94 (min 1383.48, max 1634.39)"
    "bw_mem-wr-8mb (MB/s)","1267.14 (min 1213.59, max 1320.68)"
    "bw_mmap_rd-mo-1mb (MB/s)","4119.85"
    "bw_mmap_rd-o2c-1mb (MB/s)","1234.92"
    "bw_pipe (MB/s)","434.29"
    "bw_unix (MB/s)","1643.24"
    "lat_connect (us)","48.80"
    "lat_ctx-2-128k (us)","19.15"
    "lat_ctx-2-256k (us)","35.35"
    "lat_ctx-4-128k (us)","21.62"
    "lat_ctx-4-256k (us)","34.18"
    "lat_fs-0k (num_files)","679.00"
    "lat_fs-10k (num_files)","211.00"
    "lat_fs-1k (num_files)","294.00"
    "lat_fs-4k (num_files)","308.00"
    "lat_mem_rd-stride128-sz1000k (ns)","19.27"
    "lat_mem_rd-stride128-sz125k (ns)","19.04"
    "lat_mem_rd-stride128-sz250k (ns)","12.83"
    "lat_mem_rd-stride128-sz31k (ns)","6.47"
    "lat_mem_rd-stride128-sz50 (ns)","2.67"
    "lat_mem_rd-stride128-sz500k (ns)","12.84"
    "lat_mem_rd-stride128-sz62k (ns)","17.19"
    "lat_mmap-1m (us)","49.00"
    "lat_ops-double-add (ns)","1.09"
    "lat_ops-double-mul (ns)","5.01"
    "lat_ops-float-add (ns)","1.09"
    "lat_ops-float-mul (ns)","5.01"
    "lat_ops-int-add (ns)","0.72"
    "lat_ops-int-bit (ns)","0.45"
    "lat_ops-int-div (ns)","76.97"
    "lat_ops-int-mod (ns)","13.79"
    "lat_ops-int-mul (ns)","2.69"
    "lat_ops-int64-add (ns)","1.25"
    "lat_ops-int64-bit (ns)","1.01"
    "lat_ops-int64-div (ns)","163.00"
    "lat_ops-int64-mod (ns)","33.79"
    "lat_pagefault (us)","1.09"
    "lat_pipe (us)","36.82"
    "lat_proc-exec (us)","925.67"
    "lat_proc-fork (us)","845.00"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","22.20"
    "lat_sem (us)","4.60"
    "lat_sig-catch (us)","2.96"
    "lat_sig-install (us)","0.61"
    "lat_sig-prot (us)","0.35"
    "lat_syscall-fstat (us)","0.98"
    "lat_syscall-null (us)","0.27"
    "lat_syscall-open (us)","246.23"
    "lat_syscall-read (us)","0.52"
    "lat_syscall-stat (us)","2.86"
    "lat_syscall-write (us)","0.33"
    "lat_tcp (us)","0.69"
    "lat_unix (us)","34.31"
    "latency_for_0.50_mb_block_size (nanosec)","12.84"
    "latency_for_1.00_mb_block_size (nanosec)","9.63 (min 0.00, max 19.27)"
    "pipe_bandwidth (MBs)","434.29"
    "pipe_latency (microsec)","36.82"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","22.20"
    "semaphore_latency (microsec)","4.60"
    "signal_handler_latency (microsec)","0.61"
    "signal_handler_overhead (microsec)","2.96"
    "tcp_ip_connection_cost_to_localhost (microsec)","48.80"
    "tcp_latency_using_localhost (microsec)","0.69"


Table:  **LM Bench Metrics**



Dhrystone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed. For standard ARM
cores the DMIPS/MHz score will be identical with the same compiler and flags.

.. csv-table::
    :header: "Benchmarks","am57xx-evm: perf"

    "cpu_clock (MHz)","1500.00"
    "dhrystone_per_mhz (DMIPS/MHz)","3.40"
    "dhrystone_per_second (DhrystoneP)","9090909.00"


Table:  **Dhrystone Benchmark**



Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Benchmarks","am57xx-evm: perf"

    "whetstone (MIPS)","5000.00"


Table:  **Whetstone Benchmark**



Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table::
    :header: "Benchmarks","am57xx-evm: perf"

    "linpack (Kflops)","907329.00"


Table:  **Linpack Benchmark**



NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html


.. csv-table::
    :header: "Benchmarks","am57xx-evm: perf"

    "assignment (Iterations)","16.49"
    "fourier (Iterations)","26342.00"
    "fp_emulation (Iterations)","169.17"
    "huffman (Iterations)","1358.80"
    "idea (Iterations)","3608.50"
    "lu_decomposition (Iterations)","693.97"
    "neural_net (Iterations)","22.14"
    "numeric_sort (Iterations)","632.83"
    "string_sort (Iterations)","118.08"


Table:  **NBench Benchmarks**



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

.. csv-table::
    :header: "Benchmarks","am57xx-evm: perf"

    "add (MB/s)","3676.60"
    "copy (MB/s)","3959.90"
    "scale (MB/s)","4450.80"
    "triad (MB/s)","3651.00"


Table:  **Stream**


Boot-time Measurement
-------------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Boot Configuration","am57xx-evm: boot time (sec)"

    "Kernel boot time test when bootloader, kernel and sdk-rootfs are in mmc-sd","37.40 (min 34.53, max 41.28)"
    "Kernel boot time test when init is /bin/sh and bootloader, kernel and sdk-rootfs are in mmc-sd","14.01 (min 13.40, max 16.44)"

Table:  **Boot time MMC/SD**




ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table::
    :header: "Sampling Rate (Hz)","am57xx-evm: Throughput (bits/sec)","am57xx-evm: CPU Load (%)"

    "8000","255833.00","0.09"
    "11025","352573.00","0.14"
    "16000","511666.00","0.22"
    "22050","705146.00","0.25"
    "24000","705146.00","0.26"
    "32000","1023331.00","0.36"
    "44100","1410291.00","0.38"
    "48000","1534995.00","0.45"
    "88200","2820580.00","0.83"
    "96000","3069989.00","1.06"

Table:  **Audio Capture**


|


.. csv-table::
    :header: "Sampling Rate (Hz)","am57xx-evm: Throughput (bits/sec)","am57xx-evm: CPU Load (%)"

    "8000","255936.00","0.07"
    "11025","352715.00","0.13"
    "16000","511872.00","0.10"
    "22050","705430.00","0.15"
    "24000","705430.00","0.13"
    "32000","1023744.00","0.21"
    "44100","1410860.00","0.31"
    "48000","1535615.00","0.26"
    "88200","2821718.00","0.49"
    "96000","3071227.00","0.61"

Table:  **Audio Playback**


|

Sensor Capture
-------------------------

Capture video frames (MMAP buffers) with v4l2c-ctl and record the
reported fps

.. csv-table::
    :header: "Resolution","Format","am57xx-evm: Fps","am57xx-evm: Sensor"

    "1280x800","nv12","30.01","ov10635"
    "1280x800","rgb4","30.01","ov10635"
    "320x240","nv12","30.01","ov10635"
    "320x240","rgb4","30.01","ov10635"

Table:  **Sensor Capture**

|


Graphics SGX/RGX Driver
-------------------------

GLBenchmark
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run GLBenchmark and capture performance reported Display rate (Fps),
Fill rate, Vertex Throughput, etc. All display outputs (HDMI, Displayport and/or LCD)
are connected when running these tests


Performance (Fps)
"""""""""""""""""""""""""""

.. csv-table::
    :header: "Benchmark","am57xx-evm: Test Number","am57xx-evm: Fps"

    "GLB25_EgyptTestC24Z16FixedTime test","2500005.00","25.17 (min 14.63, max 51.56)"
    "GLB25_EgyptTestC24Z16_ETC1 test","2501001.00","31.65 (min 14.87, max 59.49)"
    "GLB25_EgyptTestC24Z16_ETC1to565 test","2501401.00","32.48 (min 14.87, max 59.49)"
    "GLB25_EgyptTestC24Z16_PVRTC4 test","2501101.00","31.66 (min 14.87, max 59.49)"
    "GLB25_EgyptTestC24Z24MS4 test","2500003.00","27.65 (min 14.87, max 59.49)"
    "GLB25_EgyptTestStandard_inherited test","2000000.00","59.32 (min 51.56, max 59.49)"




Table:  **GLBenchmark 2.5 Performance**



Vertex Throughput
"""""""""""""""""""""""""""

.. csv-table::
    :header: "Benchmark","am57xx-evm: Test Number","am57xx-evm: Rate (triangles/sec)"

    "GLB25_TriangleTexFragmentLitTestC24Z16 test","2500511.00","32937770.00"
    "GLB25_TriangleTexTestC24Z16 test","2500301.00","99030688.00"
    "GLB25_TriangleTexVertexLitTestC24Z16 test","2500411.00","39563644.00"


Table:  **GLBenchmark 2.5 Vertex Throughput**



Pixel Throughput
"""""""""""""""""""""""""""

.. csv-table::
    :header: "Benchmark","am57xx-evm: Test Number","am57xx-evm: Rate (texel/sec)","am57xx-evm: Fps"

    "GLB25_FillTestC24Z16 test","2500101.00","731048896.00","29.74 (min 29.74, max 29.75)"


Table:  **GLBenchmark 2.5 Pixel Throughput**



Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table::
    :header: "Benchmark","am57xx-evm: Score"

    "Glmark2-DRM","56.00"
    "Glmark2-Wayland","375.00"


Table:  **Glmark2**


|


SATA Driver
-------------------------



.. rubric::  AM57XX-EVM
   :name: am57xx-evm-sata

|

.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT2 Throughput (Mbytes/sec)","am57xx-evm: Write EXT2 CPU Load (%)","am57xx-evm: Read EXT2 Throughput (Mbytes/sec)","am57xx-evm: Read EXT2 CPU Load (%)"

    "102400","121.86 (min 89.84, max 130.44)","9.90 (min 5.82, max 24.17)","133.60","11.54"
    "262144","126.69 (min 118.46, max 129.38)","11.61 (min 6.09, max 32.19)","134.17","11.71"
    "524288","126.32 (min 116.93, max 130.24)","11.40 (min 6.05, max 30.93)","134.03","10.75"
    "1048576","126.67 (min 119.65, max 129.25)","11.60 (min 6.31, max 31.77)","133.74","10.80"
    "5242880","127.08 (min 117.61, max 129.64)","11.24 (min 6.08, max 30.33)","133.89","10.34"

|



.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT4 Throughput (Mbytes/sec)","am57xx-evm: Write EXT4 CPU Load (%)","am57xx-evm: Read EXT4 Throughput (Mbytes/sec)","am57xx-evm: Read EXT4 CPU Load (%)"

    "102400","125.87 (min 124.12, max 129.29)","11.49 (min 7.17, max 27.08)","133.20","10.65"
    "262144","127.07 (min 125.81, max 128.05)","11.55 (min 7.02, max 27.32)","130.24","10.13"
    "524288","124.11 (min 122.95, max 124.97)","11.55 (min 7.57, max 26.44)","129.19","9.79"
    "1048576","124.08 (min 123.55, max 124.79)","10.57 (min 7.17, max 23.22)","129.12","10.04"
    "5242880","123.92 (min 121.87, max 125.60)","11.02 (min 7.41, max 24.51)","128.88","8.61"

|
|

-  Filesize used is : 1G
-  SATA II Harddisk used is: Seagate ST3500514NS 500G


mSATA Driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^



.. rubric::  AM57XX-EVM
   :name: am57xx-evm-msata

|

.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write VFAT Throughput (Mbytes/sec)","am57xx-evm: Write VFAT CPU Load (%)","am57xx-evm: Read VFAT Throughput (Mbytes/sec)","am57xx-evm: Read VFAT CPU Load (%)"

    "102400","62.41 (min 52.31, max 65.06)","10.21 (min 7.08, max 21.30)","220.29","20.50"
    "262144","62.23 (min 51.78, max 65.05)","10.52 (min 7.50, max 20.89)","228.85","21.31"
    "524288","62.34 (min 51.82, max 65.20)","10.58 (min 7.85, max 20.92)","241.67","21.89"
    "1048576","62.92 (min 51.74, max 66.16)","10.70 (min 7.37, max 20.88)","246.65","21.92"
    "5242880","62.65 (min 51.64, max 65.75)","10.57 (min 7.61, max 20.87)","243.72","21.22"

|



.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT2 Throughput (Mbytes/sec)","am57xx-evm: Write EXT2 CPU Load (%)","am57xx-evm: Read EXT2 Throughput (Mbytes/sec)","am57xx-evm: Read EXT2 CPU Load (%)"

    "102400","64.55 (min 63.06, max 65.61)","4.86 (min 2.64, max 12.28)","225.78","18.32"
    "262144","64.89 (min 63.89, max 66.03)","4.61 (min 3.00, max 10.64)","234.40","19.67"
    "524288","64.79 (min 64.32, max 65.50)","4.84 (min 3.16, max 10.79)","249.80","22.06"
    "1048576","65.93 (min 62.13, max 68.10)","4.99 (min 3.18, max 11.42)","260.06","21.05"
    "5242880","65.39 (min 64.03, max 67.35)","4.60 (min 3.14, max 9.33)","265.28","20.40"

|



.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT4 Throughput (Mbytes/sec)","am57xx-evm: Write EXT4 CPU Load (%)","am57xx-evm: Read EXT4 Throughput (Mbytes/sec)","am57xx-evm: Read EXT4 CPU Load (%)"

    "102400","64.78 (min 63.95, max 65.67)","4.85 (min 3.45, max 9.40)","230.42","17.37"
    "262144","65.69 (min 63.86, max 66.93)","4.64 (min 3.89, max 7.45)","237.43","19.20"
    "524288","67.24 (min 63.78, max 73.80)","5.20 (min 3.60, max 10.60)","254.59","20.58"
    "1048576","64.05 (min 63.17, max 64.99)","4.74 (min 3.49, max 9.34)","264.88","16.99"
    "5242880","64.37 (min 63.46, max 65.15)","4.60 (min 3.31, max 8.95)","271.15","22.86"


|

-  Filesize used is : 1G
-  MSATA Harddisk used is: SMS200S3/30G Kingston mSATA SSD drive

|



MMC/SD Driver
-------------------------

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

|


AM57XX-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^
|

.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT4 Throughput (Mbytes/sec)","am57xx-evm: Write EXT4 CPU Load (%)","am57xx-evm: Read EXT4 Throughput (Mbytes/sec)","am57xx-evm: Read EXT4 CPU Load (%)"

    "1m","16.40","0.70","22.30","0.67"
    "4m","16.10","0.76","22.50","0.59"
    "4k","2.31","2.24","10.70","7.81"
    "256k","15.40","0.48","22.10","0.89"

|


The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|

UBoot MMC/SD Driver
-------------------------
|


AM57XX-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "File size (bytes in hex)","am57xx-evm: Write Throughput (Kbytes/sec)","am57xx-evm: Read Throughput (Kbytes/sec)"

    "400000","6159.40","21222.80"
    "800000","12172.36","21962.47"
    "1000000","19574.67","22321.53"


The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card


|



USB Driver
-------------------------



USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Number of Blocks","am57xx-evm: Throughput (MB/sec)"

    "150","34.80"

Table: **USBDEVICE HIGHSPEED SLAVE READ THROUGHPUT**

|



.. csv-table::
    :header: "Number of Blocks","am57xx-evm: Throughput (MB/sec)"

    "150","32.20"

Table: **USBDEVICE HIGHSPEED SLAVE WRITE THROUGHPUT**

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Algorithm","Buffer Size (in bytes)","am57xx-evm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","14360.23"
    "aes-128-cbc","16","4890.10"
    "aes-128-cbc","16384","35296.60"
    "aes-128-cbc","256","5314.39"
    "aes-128-cbc","64","15177.24"
    "aes-128-cbc","8192","32033.45"
    "aes-192-cbc","1024","15467.52"
    "aes-192-cbc","16","4827.38"
    "aes-192-cbc","16384","35749.89"
    "aes-192-cbc","256","5331.46"
    "aes-192-cbc","64","14566.68"
    "aes-192-cbc","8192","32721.58"
    "aes-256-cbc","1024","14389.59"
    "aes-256-cbc","16","4753.24"
    "aes-256-cbc","16384","33581.74"
    "aes-256-cbc","256","5111.89"
    "aes-256-cbc","64","14157.76"
    "aes-256-cbc","8192","30580.74"
    "des-cbc","1024","8903.68"
    "des-cbc","16","312.33"
    "des-cbc","16384","16149.16"
    "des-cbc","256","3708.93"
    "des-cbc","64","1172.52"
    "des-cbc","8192","15226.20"
    "des3","1024","8768.85"
    "des3","16","319.39"
    "des3","16384","15805.10"
    "des3","256","3824.21"
    "des3","64","1215.30"
    "des3","8192","14158.51"
    "md5","1024","10163.20"
    "md5","16","1023.37"
    "md5","16384","66174.98"
    "md5","256","2971.31"
    "md5","64","3957.12"
    "md5","8192","48283.65"
    "sha1","1024","10249.90"
    "sha1","16","999.31"
    "sha1","16384","66306.05"
    "sha1","256","2899.29"
    "sha1","64","3911.55"
    "sha1","8192","48493.91"
    "sha224","1024","9752.23"
    "sha224","16","894.64"
    "sha224","16384","63673.69"
    "sha224","256","2841.17"
    "sha224","64","3409.17"
    "sha224","8192","47325.18"
    "sha256","1024","10128.38"
    "sha256","16","905.81"
    "sha256","16384","66060.29"
    "sha256","256","2868.22"
    "sha256","64","3447.30"
    "sha256","8192","48209.92"
    "sha384","1024","10723.33"
    "sha384","16","826.69"
    "sha384","16384","76797.27"
    "sha384","256","2832.98"
    "sha384","64","3320.41"
    "sha384","8192","52450.65"
    "sha512","1024","10304.17"
    "sha512","16","841.09"
    "sha512","16384","76693.50"
    "sha512","256","2855.00"
    "sha512","64","3370.90"
    "sha512","8192","53545.64"


|
|

.. csv-table::
    :header: "Algorithm","am57xx-evm: CPU Load"

    "aes-128-cbc","42.00"
    "aes-192-cbc","40.00"
    "aes-256-cbc","42.00"
    "des-cbc","20.00"
    "des3","15.00"
    "md5","50.00"
    "sha1","50.00"
    "sha224","57.00"
    "sha256","51.00"
    "sha384","56.00"
    "sha512","54.00"


|
| Listed for each algorithm are the code snippets used to run each
  benchmark test.

|

::

    time -v openssl speed -elapsed -evp aes-128-cbc



IPSec Hardware Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note: queue\_len is set to 300 and software fallback threshold set to 9
to enable software support for optimal performance

.. csv-table::
    :header: "Algorithm","am57xx-evm: Throughput (Mbps)","am57xx-evm: Packets/Sec","am57xx-evm: CPU Load"

    "3des","68.80","6.00","41.16"
    "aes128","88.70","7.00","61.72"
    "aes192","89.80","7.00","47.42"
    "aes256","91.10","8.00","48.63"




IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Algorithm","am57xx-evm: Throughput (Mbps)","am57xx-evm: Packets/Sec","am57xx-evm: CPU Load"

    "aes128","91.20","8.00","31.45"
    "aes192","91.30","8.00","33.67"
    "aes256","5.40","0.00","50.36"

|
