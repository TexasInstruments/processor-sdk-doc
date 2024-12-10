
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
| AM437x-gpevm   | AM437x-gpevm Evaluation Module rev 1.5A with ARM running at 1000MHz, DDR3-400 (400MHz/800 MT/S), TMDSEVM437X   |
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
-------------------

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
    :header: "Benchmarks","am43xx-gpevm: perf"

    "af_unix_sock_stream_latency (microsec)","34.17"
    "af_unix_socket_stream_bandwidth (MBs)","203.46"
    "bw_file_rd-io-1mb (MB/s)","202.92"
    "bw_file_rd-o2c-1mb (MB/s)","165.95"
    "bw_mem-bcopy-16mb (MB/s)","192.76"
    "bw_mem-bcopy-1mb (MB/s)","199.32"
    "bw_mem-bcopy-2mb (MB/s)","198.81"
    "bw_mem-bcopy-4mb (MB/s)","197.28"
    "bw_mem-bcopy-8mb (MB/s)","198.17"
    "bw_mem-bzero-16mb (MB/s)","672.41"
    "bw_mem-bzero-1mb (MB/s)","437.22 (min 199.32, max 675.11)"
    "bw_mem-bzero-2mb (MB/s)","436.45 (min 198.81, max 674.08)"
    "bw_mem-bzero-4mb (MB/s)","435.46 (min 197.28, max 673.63)"
    "bw_mem-bzero-8mb (MB/s)","435.67 (min 198.17, max 673.17)"
    "bw_mem-cp-16mb (MB/s)","195.36"
    "bw_mem-cp-1mb (MB/s)","437.54 (min 200.88, max 674.20)"
    "bw_mem-cp-2mb (MB/s)","436.92 (min 200.66, max 673.17)"
    "bw_mem-cp-4mb (MB/s)","436.83 (min 200.26, max 673.40)"
    "bw_mem-cp-8mb (MB/s)","437.68 (min 201.84, max 673.51)"
    "bw_mem-fcp-16mb (MB/s)","243.43"
    "bw_mem-fcp-1mb (MB/s)","460.82 (min 246.52, max 675.11)"
    "bw_mem-fcp-2mb (MB/s)","457.96 (min 241.84, max 674.08)"
    "bw_mem-fcp-4mb (MB/s)","455.72 (min 237.80, max 673.63)"
    "bw_mem-fcp-8mb (MB/s)","458.49 (min 243.80, max 673.17)"
    "bw_mem-frd-16mb (MB/s)","200.49"
    "bw_mem-frd-1mb (MB/s)","224.81 (min 203.09, max 246.52)"
    "bw_mem-frd-2mb (MB/s)","223.53 (min 205.21, max 241.84)"
    "bw_mem-frd-4mb (MB/s)","220.56 (min 203.31, max 237.80)"
    "bw_mem-frd-8mb (MB/s)","223.18 (min 202.55, max 243.80)"
    "bw_mem-fwr-16mb (MB/s)","673.00"
    "bw_mem-fwr-1mb (MB/s)","438.65 (min 203.09, max 674.20)"
    "bw_mem-fwr-2mb (MB/s)","439.19 (min 205.21, max 673.17)"
    "bw_mem-fwr-4mb (MB/s)","438.36 (min 203.31, max 673.40)"
    "bw_mem-fwr-8mb (MB/s)","438.03 (min 202.55, max 673.51)"
    "bw_mem-rd-16mb (MB/s)","313.99"
    "bw_mem-rd-1mb (MB/s)","294.96 (min 273.00, max 316.91)"
    "bw_mem-rd-2mb (MB/s)","291.29 (min 270.42, max 312.16)"
    "bw_mem-rd-4mb (MB/s)","292.52 (min 270.76, max 314.27)"
    "bw_mem-rd-8mb (MB/s)","292.48 (min 271.07, max 313.89)"
    "bw_mem-rdwr-16mb (MB/s)","246.34"
    "bw_mem-rdwr-1mb (MB/s)","225.26 (min 200.88, max 249.63)"
    "bw_mem-rdwr-2mb (MB/s)","223.38 (min 200.66, max 246.09)"
    "bw_mem-rdwr-4mb (MB/s)","223.40 (min 200.26, max 246.53)"
    "bw_mem-rdwr-8mb (MB/s)","224.14 (min 201.84, max 246.44)"
    "bw_mem-wr-16mb (MB/s)","270.97"
    "bw_mem-wr-1mb (MB/s)","261.32 (min 249.63, max 273.00)"
    "bw_mem-wr-2mb (MB/s)","258.26 (min 246.09, max 270.42)"
    "bw_mem-wr-4mb (MB/s)","258.65 (min 246.53, max 270.76)"
    "bw_mem-wr-8mb (MB/s)","258.76 (min 246.44, max 271.07)"
    "bw_mmap_rd-mo-1mb (MB/s)","209.14"
    "bw_mmap_rd-o2c-1mb (MB/s)","163.29"
    "bw_pipe (MB/s)","410.43"
    "bw_unix (MB/s)","203.46"
    "lat_connect (us)","71.88"
    "lat_ctx-2-128k (us)","0.00"
    "lat_ctx-2-256k (us)","0.00"
    "lat_ctx-4-128k (us)","0.00"
    "lat_ctx-4-256k (us)","0.00"
    "lat_fs-0k (num_files)","248.00"
    "lat_fs-10k (num_files)","85.00"
    "lat_fs-1k (num_files)","132.00"
    "lat_fs-4k (num_files)","138.00"
    "lat_mem_rd-stride128-sz1000k (ns)","98.64"
    "lat_mem_rd-stride128-sz125k (ns)","15.99"
    "lat_mem_rd-stride128-sz250k (ns)","36.50"
    "lat_mem_rd-stride128-sz31k (ns)","9.24"
    "lat_mem_rd-stride128-sz50 (ns)","4.01"
    "lat_mem_rd-stride128-sz500k (ns)","91.20"
    "lat_mem_rd-stride128-sz62k (ns)","17.05"
    "lat_mmap-1m (us)","75.00"
    "lat_ops-double-add (ns)","5.02"
    "lat_ops-double-div (ns)","25.07"
    "lat_ops-double-mul (ns)","7.03"
    "lat_ops-float-add (ns)","5.01"
    "lat_ops-float-div (ns)","15.05"
    "lat_ops-float-mul (ns)","6.02"
    "lat_ops-int-add (ns)","1.03"
    "lat_ops-int-bit (ns)","0.76"
    "lat_ops-int-div (ns)","96.04"
    "lat_ops-int-mod (ns)","23.90"
    "lat_ops-int-mul (ns)","4.14"
    "lat_ops-int64-add (ns)","1.12"
    "lat_ops-int64-bit (ns)","0.67"
    "lat_ops-int64-div (ns)","200.88"
    "lat_ops-int64-mod (ns)","42.63"
    "lat_ops-int64-mul (ns)","4.15"
    "lat_pagefault (us)","1.36"
    "lat_pipe (us)","26.45"
    "lat_proc-exec (us)","1271.80"
    "lat_proc-fork (us)","977.17"
    "lat_proc-proccall (us)","0.01"
    "lat_select (us)","33.05"
    "lat_sem (us)","6.32"
    "lat_sig-catch (us)","5.56"
    "lat_sig-install (us)","0.83"
    "lat_sig-prot (us)","0.40"
    "lat_syscall-fstat (us)","3.32"
    "lat_syscall-null (us)","0.38"
    "lat_syscall-open (us)","284.33"
    "lat_syscall-read (us)","0.67"
    "lat_syscall-stat (us)","4.65"
    "lat_syscall-write (us)","0.53"
    "lat_tcp (us)","0.84"
    "lat_unix (us)","34.17"
    "latency_for_0.50_mb_block_size (nanosec)","91.20"
    "latency_for_1.00_mb_block_size (nanosec)","49.32 (min 0.00, max 98.64)"
    "pipe_bandwidth (MBs)","410.43"
    "pipe_latency (microsec)","26.45"
    "procedure_call (microsec)","0.01"
    "select_on_200_tcp_fds (microsec)","33.05"
    "semaphore_latency (microsec)","6.32"
    "signal_handler_latency (microsec)","0.83"
    "signal_handler_overhead (microsec)","5.56"
    "tcp_ip_connection_cost_to_localhost (microsec)","71.88"
    "tcp_latency_using_localhost (microsec)","0.84"

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
    :header: "Benchmarks","am43xx-gpevm: perf"

    "cpu_clock (MHz)","1000.00"
    "dhrystone_per_mhz (DMIPS/MHz)","2.50"
    "dhrystone_per_second (DhrystoneP)","4444444.50"

Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am43xx-gpevm: perf"

    "whetstone (MIPS)","3333.30"

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am43xx-gpevm: perf"

    "linpack (Kflops)","191721.00"

NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am43xx-gpevm: perf"

    "assignment (Iterations)","7.20"
    "fourier (Iterations)","13057.00"
    "fp_emulation (Iterations)","75.15"
    "huffman (Iterations)","855.84"
    "idea (Iterations)","1831.60"
    "lu_decomposition (Iterations)","334.46"
    "neural_net (Iterations)","9.59"
    "numeric_sort (Iterations)","511.48"
    "string_sort (Iterations)","64.07"

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
    :header: "Benchmarks","am43xx-gpevm: perf"

    "add (MB/s)","326.90"
    "copy (MB/s)","433.20"
    "scale (MB/s)","652.30"
    "triad (MB/s)","380.80"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am43xx-gpevm: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","62.57 (min 61.34, max 64.23)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am43xx-gpevm: Throughput (bits/sec)","am43xx-gpevm: CPU Load (%)"

    "8000","255997.00","0.58"
    "11025","352795.00","0.62"
    "16000","511993.00","0.70"
    "22050","705591.00","1.33"
    "24000","705592.00","1.10"
    "32000","1023987.00","2.65"
    "44100","1411182.00","1.61"
    "48000","1535980.00","2.30"
    "88200","2822360.00","3.10"
    "96000","3071955.00","0.54"

.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am43xx-gpevm: Throughput (bits/sec)","am43xx-gpevm: CPU Load (%)"

    "8000","256100.00","0.62"
    "11025","352938.00","0.59"
    "16000","512201.00","0.76"
    "22050","705878.00","1.08"
    "24000","705875.00","0.84"
    "32000","1024400.00","0.26"
    "44100","1411751.00","1.51"
    "48000","1536600.00","1.96"
    "88200","2823499.00","2.86"
    "96000","3073197.00","0.54"

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

.. csv-table:: GLBenchmark 25 Performance
    :header: "Benchmark","am43xx-gpevm: Test Number","am43xx-gpevm: Fps"

    "GLB25_EgyptTestC24Z16FixedTime test","2500005.00","4.45 (min 2.20, max 11.34)"
    "GLB25_EgyptTestC24Z16_ETC1 test","2501001.00","5.20 (min 2.20, max 11.90)"
    "GLB25_EgyptTestC24Z16_ETC1to565 test","2501401.00","5.19 (min 2.20, max 11.71)"
    "GLB25_EgyptTestC24Z16_PVRTC4 test","2501101.00","5.00 (min 2.13, max 11.34)"
    "GLB25_EgyptTestC24Z24MS4 test","2500003.00","4.18 (min 1.24, max 9.92)"
    "GLB25_EgyptTestStandard_inherited test","2000000.00","15.21 (min 10.56, max 19.84)"

.. csv-table:: GLBenchmark 25 Offscreen Performance
    :header: "Benchmark","am43xx-gpevm: Test Number","am43xx-gpevm: Fps"

    "GLB25_EgyptTestC24Z16_ETC1_Offscreen test","2501011.00","3.00"
    "GLB25_EgyptTestStandardOffscreen_inherited test","2000010.00","6.00"

Vertex Throughput
"""""""""""""""""""""""""""

.. csv-table:: GLBenchmark 25 Vertex Throughput
    :header: "Benchmark","am43xx-gpevm: Test Number","am43xx-gpevm: Rate (triangles/sec)"

    "GLB25_TriangleTexFragmentLitTestC24Z16 test","2500511.00","2307343.50"
    "GLB25_TriangleTexTestC24Z16 test","2500301.00","11125243.00"
    "GLB25_TriangleTexVertexLitTestC24Z16 test","2500411.00","4215366.50"

Pixel Throughput
"""""""""""""""""""""""""""

.. csv-table:: GLBenchmark 25 Pixel Throughput
    :header: "Benchmark","am43xx-gpevm: Test Number","am43xx-gpevm: Rate (texel/sec)","am43xx-gpevm: Fps"

    "GLB25_FillTestC24Z16 test","2500101.00","102746568.00","4.17 (min 3.97, max 4.25)"

Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am43xx-gpevm: Score"

    "Glmark2-DRM","40.00"
    "Glmark2-Wayland","62.00"

|

NAND Driver
-------------------------

AM43XX-GPEVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: NAND Performance
    :header: "Buffer size (bytes)","am43xx-gpevm: Write UBIFS Throughput (Mbytes/sec)","am43xx-gpevm: Write UBIFS CPU Load (%)","am43xx-gpevm: Read UBIFS Throughput (Mbytes/sec)","am43xx-gpevm: Read UBIFS CPU Load (%)"

    "102400","5.03 (min 4.90, max 5.34)","79.16 (min 77.63, max 79.80)","10.70","35.59"
    "262144","4.87 (min 4.77, max 5.16)","77.48 (min 75.34, max 78.50)","10.60","35.53"
    "524288","4.96 (min 4.87, max 5.00)","78.72 (min 78.37, max 79.10)","10.67","36.05"
    "1048576","4.96 (min 4.90, max 5.00)","78.77 (min 78.58, max 79.05)","10.71","34.76"
    "5242880","4.96 (min 4.91, max 4.99)","78.70 (min 78.35, max 79.00)","10.70","34.02"

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
    :header: "Buffer size (bytes)","am43xx-gpevm: Write EXT4 Throughput (Mbytes/sec)","am43xx-gpevm: Write EXT4 CPU Load (%)","am43xx-gpevm: Read EXT4 Throughput (Mbytes/sec)","am43xx-gpevm: Read EXT4 CPU Load (%)"

    "1m","13.90","4.66","22.70","7.98"
    "4m","14.40","4.02","23.10","7.75"
    "4k","4.50","22.49","10.30","37.71"
    "256k","13.80","5.56","22.40","8.91"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am43xx-gpevm: Write Raw Throughput (Mbytes/sec)","am43xx-gpevm: Write Raw CPU Load (%)","am43xx-gpevm: Read Raw Throughput (Mbytes/sec)","am43xx-gpevm: Read Raw CPU Load (%)"

    "102400","14.70 (min 14.16, max 15.23)","10.43 (min 8.69, max 15.48)","20.55","17.69"
    "262144","14.71 (min 14.37, max 15.08)","11.44 (min 9.01, max 16.69)","20.21","15.75"
    "524288","14.62 (min 14.29, max 15.14)","11.22 (min 8.90, max 17.03)","20.18","15.12"
    "1048576","14.83 (min 14.46, max 15.14)","10.51 (min 8.35, max 15.50)","21.89","15.37"
    "5242880","14.74 (min 14.34, max 14.98)","11.30 (min 9.59, max 15.13)","20.82","15.17"

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am43xx-gpevm: Write Throughput (Kbytes/sec)","am43xx-gpevm: Read Throughput (Kbytes/sec)"

    "400000","11441.34","18204.44"
    "800000","13086.26","18919.17"
    "1000000","14160.76","19275.29"

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
 
|

USB Driver
-------------------------
 
USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am43xx-gpevm: Throughput (MB/sec)"

    "150","29.80"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am43xx-gpevm: Throughput (MB/sec)"

    "150","32.70"

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am43xx-gpevm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","35747.84"
    "aes-128-cbc","16","26446.95"
    "aes-128-cbc","16384","35984.73"
    "aes-128-cbc","256","34951.85"
    "aes-128-cbc","64","32576.13"
    "aes-128-cbc","8192","36020.22"
    "aes-128-ecb","1024","37481.13"
    "aes-128-ecb","16","29543.00"
    "aes-128-ecb","16384","36022.95"
    "aes-128-ecb","256","36898.99"
    "aes-128-ecb","64","34818.22"
    "aes-128-ecb","8192","37579.43"
    "aes-192-cbc","1024","31572.31"
    "aes-192-cbc","16","23711.11"
    "aes-192-cbc","16384","31724.89"
    "aes-192-cbc","256","30984.36"
    "aes-192-cbc","64","28734.70"
    "aes-192-cbc","8192","31719.42"
    "aes-192-ecb","1024","30806.70"
    "aes-192-ecb","16","26539.27"
    "aes-192-ecb","16384","30894.76"
    "aes-192-ecb","256","30396.59"
    "aes-192-ecb","64","29511.04"
    "aes-192-ecb","8192","30892.03"
    "aes-256-cbc","1024","27561.64"
    "aes-256-cbc","16","21345.31"
    "aes-256-cbc","16384","27694.42"
    "aes-256-cbc","256","27116.46"
    "aes-256-cbc","64","25273.13"
    "aes-256-cbc","8192","27648.00"
    "aes-256-ecb","1024","26888.19"
    "aes-256-ecb","16","23633.29"
    "aes-256-ecb","16384","27017.22"
    "aes-256-ecb","256","26694.49"
    "aes-256-ecb","64","25829.82"
    "aes-256-ecb","8192","26987.18"
    "des3","1024","3417.43"
    "des3","16","3324.10"
    "des3","16384","3435.18"
    "des3","256","3428.86"
    "des3","64","3410.35"
    "des3","8192","3429.72"
    "md5","1024","107671.55"
    "md5","16","7538.66"
    "md5","16384","137052.16"
    "md5","256","64438.95"
    "md5","64","24612.16"
    "md5","8192","134671.02"
    "sha1","1024","96461.82"
    "sha1","16","7475.67"
    "sha1","16384","118953.30"
    "sha1","256","59920.13"
    "sha1","64","23729.22"
    "sha1","8192","117260.29"
    "sha224","1024","53822.12"
    "sha224","16","6092.77"
    "sha224","16384","61882.37"
    "sha224","256","37944.83"
    "sha224","64","17359.49"
    "sha224","8192","61278.89"
    "sha256","1024","53979.82"
    "sha256","16","6181.99"
    "sha256","16384","61440.00"
    "sha256","256","38204.33"
    "sha256","64","17617.75"
    "sha256","8192","61169.66"
    "sha512","1024","33758.21"
    "sha512","16","3310.41"
    "sha512","16384","39747.58"
    "sha512","256","21815.98"
    "sha512","64","13270.23"
    "sha512","8192","39340.71"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am43xx-gpevm: CPU Load"

    "aes-128-cbc","99.00"
    "aes-128-ecb","99.00"
    "aes-192-cbc","99.00"
    "aes-192-ecb","99.00"
    "aes-256-cbc","99.00"
    "aes-256-ecb","99.00"
    "des3","99.00"
    "md5","99.00"
    "sha1","99.00"
    "sha224","99.00"
    "sha256","99.00"
    "sha386","87.00"
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
    :header: "Algorithm","am43xx-gpevm: Throughput (Mbps)","am43xx-gpevm: Packets/Sec","am43xx-gpevm: CPU Load"

    "aes128","0.00","0.00","97.91"

IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","am43xx-gpevm: Throughput (Mbps)","am43xx-gpevm: Packets/Sec","am43xx-gpevm: CPU Load"

    "3des","33.00","2.00","97.63"
    "aes128","86.00","7.00","98.64"
    "aes192","80.30","7.00","100.16"
    "aes256","70.00","6.00","100.18"
