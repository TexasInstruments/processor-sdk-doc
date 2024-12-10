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
| AM335x EVM     | AM335x Evaluation Module rev 1.5B with ARM running at 1000MHz, DDR3-400 (400MHz/800 MT/S), TMDXEVM3358         |
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
    :header: "Benchmarks","am335x-evm: perf"

    "af_unix_sock_stream_latency (microsec)","48.86"
    "af_unix_socket_stream_bandwidth (MBs)","136.57"
    "bw_file_rd-io-1mb (MB/s)","143.97"
    "bw_file_rd-o2c-1mb (MB/s)","124.29"
    "bw_mem-bcopy-16mb (MB/s)","180.87"
    "bw_mem-bcopy-1mb (MB/s)","177.24"
    "bw_mem-bcopy-2mb (MB/s)","172.79"
    "bw_mem-bcopy-4mb (MB/s)","171.25"
    "bw_mem-bcopy-8mb (MB/s)","174.71"
    "bw_mem-bzero-16mb (MB/s)","954.08"
    "bw_mem-bzero-1mb (MB/s)","567.78 (min 177.24, max 958.31)"
    "bw_mem-bzero-2mb (MB/s)","556.40 (min 172.79, max 940.00)"
    "bw_mem-bzero-4mb (MB/s)","561.36 (min 171.25, max 951.47)"
    "bw_mem-bzero-8mb (MB/s)","565.17 (min 174.71, max 955.62)"
    "bw_mem-cp-16mb (MB/s)","152.29"
    "bw_mem-cp-1mb (MB/s)","560.05 (min 165.02, max 955.08)"
    "bw_mem-cp-2mb (MB/s)","555.49 (min 164.76, max 946.22)"
    "bw_mem-cp-4mb (MB/s)","559.37 (min 164.91, max 953.82)"
    "bw_mem-cp-8mb (MB/s)","559.03 (min 165.68, max 952.38)"
    "bw_mem-fcp-16mb (MB/s)","157.10"
    "bw_mem-fcp-1mb (MB/s)","558.42 (min 158.53, max 958.31)"
    "bw_mem-fcp-2mb (MB/s)","548.77 (min 157.54, max 940.00)"
    "bw_mem-fcp-4mb (MB/s)","554.42 (min 157.36, max 951.47)"
    "bw_mem-fcp-8mb (MB/s)","557.35 (min 159.07, max 955.62)"
    "bw_mem-frd-16mb (MB/s)","212.62"
    "bw_mem-frd-1mb (MB/s)","187.03 (min 158.53, max 215.53)"
    "bw_mem-frd-2mb (MB/s)","185.05 (min 157.54, max 212.56)"
    "bw_mem-frd-4mb (MB/s)","185.08 (min 157.36, max 212.79)"
    "bw_mem-frd-8mb (MB/s)","185.95 (min 159.07, max 212.82)"
    "bw_mem-fwr-16mb (MB/s)","955.05"
    "bw_mem-fwr-1mb (MB/s)","585.31 (min 215.53, max 955.08)"
    "bw_mem-fwr-2mb (MB/s)","579.39 (min 212.56, max 946.22)"
    "bw_mem-fwr-4mb (MB/s)","583.31 (min 212.79, max 953.82)"
    "bw_mem-fwr-8mb (MB/s)","582.60 (min 212.82, max 952.38)"
    "bw_mem-rd-16mb (MB/s)","215.04"
    "bw_mem-rd-1mb (MB/s)","572.26 (min 188.61, max 955.90)"
    "bw_mem-rd-2mb (MB/s)","580.57 (min 215.22, max 945.92)"
    "bw_mem-rd-4mb (MB/s)","582.82 (min 215.30, max 950.34)"
    "bw_mem-rd-8mb (MB/s)","583.81 (min 214.01, max 953.60)"
    "bw_mem-rdwr-16mb (MB/s)","174.42"
    "bw_mem-rdwr-1mb (MB/s)","171.39 (min 165.02, max 177.75)"
    "bw_mem-rdwr-2mb (MB/s)","169.90 (min 164.76, max 175.04)"
    "bw_mem-rdwr-4mb (MB/s)","170.72 (min 164.91, max 176.53)"
    "bw_mem-rdwr-8mb (MB/s)","171.19 (min 165.68, max 176.69)"
    "bw_mem-wr-16mb (MB/s)","955.87"
    "bw_mem-wr-1mb (MB/s)","566.83 (min 177.75, max 955.90)"
    "bw_mem-wr-2mb (MB/s)","560.48 (min 175.04, max 945.92)"
    "bw_mem-wr-4mb (MB/s)","563.44 (min 176.53, max 950.34)"
    "bw_mem-wr-8mb (MB/s)","565.15 (min 176.69, max 953.60)"
    "bw_mmap_rd-mo-1mb (MB/s)","202.63"
    "bw_mmap_rd-o2c-1mb (MB/s)","144.38"
    "bw_pipe (MB/s)","236.43"
    "bw_unix (MB/s)","136.57"
    "lat_connect (us)","100.67"
    "lat_ctx-2-128k (us)","37.49"
    "lat_ctx-2-256k (us)","4.00"
    "lat_ctx-4-128k (us)","47.27"
    "lat_ctx-4-256k (us)","0.00"
    "lat_fs-0k (num_files)","168.00"
    "lat_fs-10k (num_files)","73.00"
    "lat_fs-1k (num_files)","107.00"
    "lat_fs-4k (num_files)","108.00"
    "lat_mem_rd-stride128-sz1000k (ns)","270.29"
    "lat_mem_rd-stride128-sz125k (ns)","14.61"
    "lat_mem_rd-stride128-sz250k (ns)","85.30"
    "lat_mem_rd-stride128-sz31k (ns)","3.19"
    "lat_mem_rd-stride128-sz50 (ns)","3.12"
    "lat_mem_rd-stride128-sz500k (ns)","222.51"
    "lat_mem_rd-stride128-sz62k (ns)","9.35"
    "lat_mmap-1m (us)","85.00"
    "lat_ops-double-add (ns)","9.32"
    "lat_ops-double-div (ns)","59.74"
    "lat_ops-double-mul (ns)","11.58"
    "lat_ops-float-add (ns)","9.32"
    "lat_ops-float-div (ns)","34.46"
    "lat_ops-float-mul (ns)","10.49"
    "lat_ops-int-add (ns)","1.05"
    "lat_ops-int-bit (ns)","0.70"
    "lat_ops-int-div (ns)","76.00"
    "lat_ops-int-mod (ns)","26.58"
    "lat_ops-int-mul (ns)","6.84"
    "lat_ops-int64-add (ns)","1.11"
    "lat_ops-int64-bit (ns)","0.70"
    "lat_ops-int64-div (ns)","198.23"
    "lat_ops-int64-mod (ns)","54.52"
    "lat_ops-int64-mul (ns)","6.34"
    "lat_pagefault (us)","1.82"
    "lat_pipe (us)","38.21"
    "lat_proc-exec (us)","1685.43"
    "lat_proc-fork (us)","1247.67"
    "lat_proc-proccall (us)","0.02"
    "lat_select (us)","42.91"
    "lat_sem (us)","5.47"
    "lat_sig-catch (us)","8.19"
    "lat_sig-install (us)","1.33"
    "lat_sig-prot (us)","0.76"
    "lat_syscall-fstat (us)","4.37"
    "lat_syscall-null (us)","0.51"
    "lat_syscall-open (us)","324.53"
    "lat_syscall-read (us)","0.90"
    "lat_syscall-stat (us)","6.26"
    "lat_syscall-write (us)","0.69"
    "lat_tcp (us)","1.10"
    "lat_unix (us)","48.86"
    "latency_for_0.50_mb_block_size (nanosec)","222.51"
    "latency_for_1.00_mb_block_size (nanosec)","135.15 (min 0.00, max 270.29)"
    "pipe_bandwidth (MBs)","236.43"
    "pipe_latency (microsec)","38.21"
    "procedure_call (microsec)","0.02"
    "select_on_200_tcp_fds (microsec)","42.91"
    "semaphore_latency (microsec)","5.47"
    "signal_handler_latency (microsec)","1.33"
    "signal_handler_overhead (microsec)","8.19"
    "tcp_ip_connection_cost_to_localhost (microsec)","100.67"
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
    :header: "Benchmarks","am335x-evm: perf"

    "cpu_clock (MHz)","1000.00"
    "dhrystone_per_mhz (DMIPS/MHz)","2.00"
    "dhrystone_per_second (DhrystoneP)","3571428.50"

Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am335x-evm: perf"

    "whetstone (MIPS)","833.30"

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am335x-evm: perf"

    "linpack (Kflops)","48400.00"

NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am335x-evm: perf"

    "assignment (Iterations)","7.58"
    "fourier (Iterations)","2842.00"
    "fp_emulation (Iterations)","68.81"
    "huffman (Iterations)","713.20"
    "idea (Iterations)","1678.40"
    "lu_decomposition (Iterations)","74.06"
    "neural_net (Iterations)","2.17"
    "numeric_sort (Iterations)","409.38"
    "string_sort (Iterations)","65.96"

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
    :header: "Benchmarks","am335x-evm: perf"

    "add (MB/s)","438.80"
    "copy (MB/s)","414.00"
    "scale (MB/s)","525.70"
    "triad (MB/s)","395.20"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am335x-evm: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","65.09 (min 44.03, max 107.79)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am335x-evm: Throughput (bits/sec)","am335x-evm: CPU Load (%)"

    "8000","255998.00","2.77"
    "11025","352796.00","3.01"
    "16000","511995.00","3.65"
    "22050","705593.00","3.86"
    "24000","705590.00","3.62"
    "32000","1023986.00","6.27"
    "44100","1411181.00","4.64"
    "48000","1535980.00","5.61"
    "88200","2822360.00","7.95"
    "96000","3071956.00","14.36"

.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am335x-evm: Throughput (bits/sec)","am335x-evm: CPU Load (%)"

    "8000","256101.00","13.75"
    "11025","352938.00","14.48"
    "16000","512201.00","20.07"
    "22050","705877.00","19.73"
    "24000","705874.00","19.20"
    "32000","1024395.00","16.14"
    "44100","1411748.00","24.15"
    "48000","1536596.00","26.89"
    "88200","2823477.00","33.59"
    "96000","3073162.00","44.89"

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
    :header: "Benchmark","am335x-evm: Test Number","am335x-evm: Fps"

    "GLB25_EgyptTestC24Z16FixedTime test","2500005.00","4.24 (min 2.11, max 10.32)"
    "GLB25_EgyptTestC24Z16_ETC1 test","2501001.00","4.92 (min 2.13, max 10.32)"
    "GLB25_EgyptTestC24Z16_ETC1to565 test","2501401.00","4.90 (min 2.13, max 10.32)"
    "GLB25_EgyptTestC24Z16_PVRTC4 test","2501101.00","4.77 (min 2.06, max 10.31)"
    "GLB25_EgyptTestC24Z24MS4 test","2500003.00","3.97 (min 1.26, max 8.84)"
    "GLB25_EgyptTestStandard_inherited test","2000000.00","13.39 (min 9.52, max 19.05)"

.. csv-table:: GLBenchmark 25 Offscreen Performance
    :header: "Benchmark","am335x-evm: Test Number","am335x-evm: Fps"

    "GLB25_EgyptTestC24Z16_ETC1_Offscreen test","2501011.00","2.00"
    "GLB25_EgyptTestStandardOffscreen_inherited test","2000010.00","6.00"

Vertex Throughput
"""""""""""""""""""""""""""

.. csv-table:: GLBenchmark 25 Vertex Throughput
    :header: "Benchmark","am335x-evm: Test Number","am335x-evm: Rate (triangles/sec)"

    "GLB25_TriangleTexFragmentLitTestC24Z16 test","2500511.00","2233982.25"
    "GLB25_TriangleTexTestC24Z16 test","2500301.00","10659006.00"
    "GLB25_TriangleTexVertexLitTestC24Z16 test","2500411.00","3086775.25"

Pixel Throughput
"""""""""""""""""""""""""""

.. csv-table:: GLBenchmark 25 Pixel Throughput
    :header: "Benchmark","am335x-evm: Test Number","am335x-evm: Rate (texel/sec)","am335x-evm: Fps"

    "GLB25_FillTestC24Z16 test","2500101.00","96879864.00","3.95 (min 3.87, max 4.13)"

Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am335x-evm: Score"

    "Glmark2-DRM","40.00"
    "Glmark2-Wayland","54.00"

|

NAND Driver
-------------------------

AM335X-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: NAND Performance
    :header: "Buffer size (bytes)","am335x-evm: Write UBIFS Throughput (Mbytes/sec)","am335x-evm: Write UBIFS CPU Load (%)","am335x-evm: Read UBIFS Throughput (Mbytes/sec)","am335x-evm: Read UBIFS CPU Load (%)"

    "102400","3.36 (min 3.30, max 3.49)","67.31 (min 66.82, max 68.01)","5.43","31.56"
    "262144","3.19 (min 3.16, max 3.27)","66.55 (min 65.25, max 67.14)","5.40","31.75"
    "524288","3.31 (min 3.29, max 3.32)","67.98 (min 67.62, max 68.60)","5.39","34.52"
    "1048576","3.31 (min 3.29, max 3.32)","67.85 (min 67.11, max 68.65)","5.44","32.43"
    "5242880","3.29 (min 3.27, max 3.31)","68.06 (min 67.61, max 68.67)","5.40","32.10"

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
    :header: "Buffer size (bytes)","am335x-evm: Write EXT4 Throughput (Mbytes/sec)","am335x-evm: Write EXT4 CPU Load (%)","am335x-evm: Read EXT4 Throughput (Mbytes/sec)","am335x-evm: Read EXT4 CPU Load (%)"

    "1m","19.80","7.75","21.30","9.50"
    "4m","19.90","5.77","21.50","9.14"
    "4k","2.97","32.43","8.71","68.07"
    "256k","19.10","11.43","20.90","12.32"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am335x-evm: Write Raw Throughput (Mbytes/sec)","am335x-evm: Write Raw CPU Load (%)","am335x-evm: Read Raw Throughput (Mbytes/sec)","am335x-evm: Read Raw CPU Load (%)"

    "102400","19.28 (min 18.32, max 19.64)","14.66 (min 12.55, max 20.18)","19.60","19.65"
    "262144","18.22 (min 17.94, max 18.39)","15.74 (min 13.37, max 23.63)","19.90","18.91"
    "524288","18.61 (min 18.17, max 18.76)","15.04 (min 13.16, max 21.24)","21.35","17.19"
    "1048576","18.18 (min 17.70, max 18.39)","15.87 (min 12.71, max 21.82)","20.65","15.01"
    "5242880","18.79 (min 18.49, max 18.93)","14.95 (min 12.68, max 21.96)","22.58","16.96"

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|

USB Driver
-------------------------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am335x-evm: Throughput (MB/sec)"

    "150","18.70"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am335x-evm: Throughput (MB/sec)"

    "150","7.90"

|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am335x-evm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","45160.45"
    "aes-128-cbc","16","29444.57"
    "aes-128-cbc","16384","45498.37"
    "aes-128-cbc","256","43996.25"
    "aes-128-cbc","64","39726.91"
    "aes-128-cbc","8192","45304.49"
    "aes-128-ecb","1024","46018.56"
    "aes-128-ecb","16","33617.70"
    "aes-128-ecb","16384","44176.73"
    "aes-128-ecb","256","45172.91"
    "aes-128-ecb","64","42119.19"
    "aes-128-ecb","8192","46454.10"
    "aes-192-cbc","1024","37128.19"
    "aes-192-cbc","16","25825.44"
    "aes-192-cbc","16384","37475.67"
    "aes-192-cbc","256","36298.07"
    "aes-192-cbc","64","33364.46"
    "aes-192-cbc","8192","37218.99"
    "aes-192-ecb","1024","39738.71"
    "aes-192-ecb","16","30087.25"
    "aes-192-ecb","16384","39955.11"
    "aes-192-ecb","256","39108.78"
    "aes-192-ecb","64","36687.68"
    "aes-192-ecb","8192","39903.23"
    "aes-256-cbc","1024","33224.02"
    "aes-256-cbc","16","23909.91"
    "aes-256-cbc","16384","33390.59"
    "aes-256-cbc","256","32509.70"
    "aes-256-cbc","64","30216.81"
    "aes-256-cbc","8192","33412.44"
    "aes-256-ecb","1024","34884.27"
    "aes-256-ecb","16","27224.88"
    "aes-256-ecb","16384","35045.38"
    "aes-256-ecb","256","34382.85"
    "aes-256-ecb","64","32453.78"
    "aes-256-ecb","8192","34941.61"
    "des3","1024","4116.82"
    "des3","16","3899.69"
    "des3","16384","4106.92"
    "des3","256","4101.55"
    "des3","64","4063.23"
    "des3","8192","4104.19"
    "md5","1024","124733.78"
    "md5","16","7509.55"
    "md5","16384","165494.78"
    "md5","256","69602.05"
    "md5","64","25231.81"
    "md5","8192","161778.35"
    "sha1","1024","103653.03"
    "sha1","16","7100.50"
    "sha1","16384","132027.73"
    "sha1","256","61524.74"
    "sha1","64","23449.05"
    "sha1","8192","129687.55"
    "sha224","1024","60944.04"
    "sha224","16","6003.48"
    "sha224","16384","71892.99"
    "sha224","256","40934.49"
    "sha224","64","17822.29"
    "sha224","8192","71087.45"
    "sha256","1024","60806.14"
    "sha256","16","5863.40"
    "sha256","16384","71876.61"
    "sha256","256","40605.35"
    "sha256","64","17548.67"
    "sha256","8192","70926.34"
    "sha512","1024","34268.16"
    "sha512","16","3219.22"
    "sha512","16384","43499.52"
    "sha512","256","23722.07"
    "sha512","64","12888.55"
    "sha512","8192","42816.85"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am335x-evm: CPU Load"

    "aes-128-cbc","99.00"
    "aes-128-ecb","98.00"
    "aes-192-cbc","99.00"
    "aes-192-ecb","99.00"
    "aes-256-cbc","99.00"
    "aes-256-ecb","99.00"
    "des3","99.00"
    "md5","99.00"
    "sha1","99.00"
    "sha224","99.00"
    "sha256","99.00"
    "sha386","84.00"
    "sha512","98.00"

Listed for each algorithm are the code snippets used to run each benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

IPSec Hardware Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note: queue\_len is set to 300 and software fallback threshold set to 9
to enable software support for optimal performance

.. csv-table:: IPSec Hardware Performance
    :header: "Algorithm","am335x-evm: Throughput (Mbps)","am335x-evm: Packets/Sec","am335x-evm: CPU Load"

    "3des","0.00","0.00","100.73"
    "aes128","0.00","0.00","99.63"
    "aes192","0.30","0.00","98.67"
    "aes256","0.50","0.00","100.18"

IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","am335x-evm: Throughput (Mbps)","am335x-evm: Packets/Sec","am335x-evm: CPU Load"

    "3des","36.00","3.00","100.31"
    "aes128","82.40","7.00","100.44"
    "aes192","64.20","5.00","99.60"
    "aes256","68.50","6.00","101.78"
