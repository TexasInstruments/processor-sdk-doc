.. include:: <isonum.txt>

.. http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_Kernel_Performance_Guide


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
| AM335x         | AM335x Evaluation Module rev 1.5B with ARM running at 1000MHz, DDR3-400 (400MHz/800 MT/S), TMDXEVM3358         |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM437x-gpevm   | AM437x-gpevm Evaluation Module rev 1.5A with ARM running at 1000MHz, DDR3-400 (400MHz/800 MT/S), TMDSEVM437X   |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM572x EVM     | AM57xx Evaluation Module rev A2 with ARM running at 1500MHz, DDR3L-533 (533 MHz/1066 MT/S), TMDSEVM572x        |
+----------------+----------------------------------------------------------------------------------------------------------------+
| K2HK EVM       | K2 Hawkings Evaluation Module rev 40 with ARM running at 1200MHz, DDR3-1600 (800 MHz/1600 MT/S), EVMK2H        |
+----------------+----------------------------------------------------------------------------------------------------------------+
| K2G EVM        | K2 Galileo Evaluation Module rev C, DDR3-1333 (666 MHz/1333 MT/S), EVMK2G                                      |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM65x EVM      | AM65x Evaluation Module rev 1.0 with ARM running at 800MHz, DDR4-2400 (1600 MT/S), TMDX654GPEVM                |
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
memory system performance.

**Latency**: lat_mem_rd-stride128-szN, where N is equal to or smaller than the cache
size at given level measures the cache miss penalty. N that is at least
double the size of last level cache is the latency to external memory.

**Bandwidth**: bw_mem_bcopy-N, where N is is equal to or smaller than the cache size at
a given level measures the achivable memory bandwidth from software doing
a memcpy() type operation. Typical use is for external memory bandwidth
calculation. The bandwidth is calculated as byte read and written counts
as 1 which should be roughly half of STREAM copy result.

.. csv-table::
    :header: "Benchmarks","am335x-evm: perf","am57xx-evm: perf","am654x-evm: perf","k2g-evm: perf","omapl138-lcdk: perf"

    "af_unix_sock_stream_latency (microsec)","43.64","28.84","46.50","47.52","736.29"
    "af_unix_socket_stream_bandwidth (MBs)","174.44","2054.91","1175.02","661.28","30.82"
    "bw_file_rd-io-1mb (MB/s)","182.75","1489.76","1163.47","727.80","43.92"
    "bw_file_rd-o2c-1mb (MB/s)","154.46","1086.17","734.35","526.04","40.10"
    "bw_mem-bcopy-16mb (MB/s)","208.64","1937.52","780.64","1237.72","40.10"
    "bw_mem-bcopy-1mb (MB/s)","197.90","4940.15","1472.48","1327.77","97.13"
    "bw_mem-bcopy-2mb (MB/s)","200.92","3273.92","882.22","1245.72","97.36"
    "bw_mem-bcopy-4mb (MB/s)","211.03","2046.73","789.42","1236.09","97.07"
    "bw_mem-bcopy-8mb (MB/s)","218.81","1972.39","781.40","1236.67","100.19"
    "bw_mem-bzero-16mb (MB/s)","995.02","4989.86","1979.71","3362.76","193.88"
    "bw_mem-bzero-1mb (MB/s)","591.00 (min 197.90, max 984.09)","5309.95 (min 4940.15, max 5679.74)","2888.59 (min 1472.48, max 4304.70)","2947.90 (min 1327.77, max 4568.02)","143.52 (min 97.13, max 189.90)"
    "bw_mem-bzero-2mb (MB/s)","592.59 (min 200.92, max 984.25)","4379.69 (min 3273.92, max 5485.46)","2566.31 (min 882.22, max 4250.39)","2586.34 (min 1245.72, max 3926.96)","144.86 (min 97.36, max 192.36)"
    "bw_mem-bzero-4mb (MB/s)","597.40 (min 211.03, max 983.77)","3660.15 (min 2046.73, max 5273.57)","1614.78 (min 789.42, max 2440.14)","2439.87 (min 1236.09, max 3643.65)","145.04 (min 97.07, max 193.00)"
    "bw_mem-bzero-8mb (MB/s)","601.84 (min 218.81, max 984.86)","3533.56 (min 1972.39, max 5094.73)","1399.78 (min 781.40, max 2018.16)","2336.30 (min 1236.67, max 3435.93)","146.77 (min 100.19, max 193.34)"
    "bw_mem-cp-16mb (MB/s)","195.55","1024.98","455.57","604.46","60.27"
    "bw_mem-cp-1mb (MB/s)","587.49 (min 191.20, max 983.77)","5163.28 (min 4576.24, max 5750.32)","2627.67 (min 818.60, max 4436.73)","2800.52 (min 609.94, max 4991.09)","52.85 (min 45.43, max 60.27)"
    "bw_mem-cp-2mb (MB/s)","589.18 (min 194.59, max 983.77)","3338.25 (min 1149.59, max 5526.90)","2409.98 (min 520.56, max 4299.39)","2307.50 (min 604.96, max 4010.03)","53.02 (min 39.57, max 66.46)"
    "bw_mem-cp-4mb (MB/s)","599.46 (min 197.54, max 1001.38)","3174.59 (min 1052.91, max 5296.26)","1455.02 (min 466.91, max 2443.12)","2113.61 (min 604.69, max 3622.53)","53.73 (min 37.98, max 69.48)"
    "bw_mem-cp-8mb (MB/s)","599.10 (min 202.56, max 995.64)","3071.72 (min 1043.84, max 5099.60)","1237.87 (min 460.11, max 2015.62)","2002.76 (min 610.41, max 3395.11)","93.97 (min 39.52, max 148.42)"
    "bw_mem-fcp-16mb (MB/s)","278.24","1125.65","776.28","618.50","189.90"
    "bw_mem-fcp-1mb (MB/s)","641.59 (min 299.09, max 984.09)","4477.64 (min 3275.53, max 5679.74)","2872.81 (min 1440.92, max 4304.70)","2593.80 (min 619.58, max 4568.02)","133.86 (min 77.82, max 189.90)"
    "bw_mem-fcp-2mb (MB/s)","639.90 (min 295.55, max 984.25)","3373.55 (min 1261.63, max 5485.46)","2563.22 (min 876.04, max 4250.39)","2271.46 (min 615.95, max 3926.96)","134.42 (min 76.48, max 192.36)"
    "bw_mem-fcp-4mb (MB/s)","642.43 (min 301.09, max 983.77)","3204.40 (min 1135.23, max 5273.57)","1613.39 (min 786.63, max 2440.14)","2126.75 (min 609.85, max 3643.65)","134.65 (min 76.30, max 193.00)"
    "bw_mem-fcp-8mb (MB/s)","643.30 (min 301.73, max 984.86)","3109.96 (min 1125.18, max 5094.73)","1396.42 (min 774.67, max 2018.16)","2028.99 (min 622.04, max 3435.93)","135.36 (min 77.37, max 193.34)"
    "bw_mem-frd-16mb (MB/s)","248.52","1054.09","1239.16","829.06","134.62"
    "bw_mem-frd-1mb (MB/s)","283.96 (min 268.82, max 299.09)","3182.10 (min 3088.66, max 3275.53)","1455.49 (min 1440.92, max 1470.05)","778.66 (min 619.58, max 937.73)","105.21 (min 77.82, max 132.59)"
    "bw_mem-frd-2mb (MB/s)","274.49 (min 253.42, max 295.55)","1735.99 (min 1261.63, max 2210.35)","1147.62 (min 876.04, max 1419.19)","726.04 (min 615.95, max 836.12)","105.02 (min 76.48, max 133.55)"
    "bw_mem-frd-4mb (MB/s)","275.34 (min 249.59, max 301.09)","1171.12 (min 1135.23, max 1207.00)","1058.43 (min 786.63, max 1330.23)","719.31 (min 609.85, max 828.76)","105.36 (min 76.30, max 134.41)"
    "bw_mem-frd-8mb (MB/s)","275.37 (min 249.01, max 301.73)","1086.63 (min 1048.08, max 1125.18)","1010.49 (min 774.67, max 1246.30)","725.10 (min 622.04, max 828.16)","106.00 (min 77.37, max 134.63)"
    "bw_mem-fwr-16mb (MB/s)","996.57","4982.87","1978.73","3324.68","193.15"
    "bw_mem-fwr-1mb (MB/s)","626.30 (min 268.82, max 983.77)","4419.49 (min 3088.66, max 5750.32)","2953.39 (min 1470.05, max 4436.73)","2964.41 (min 937.73, max 4991.09)","96.43 (min 60.27, max 132.59)"
    "bw_mem-fwr-2mb (MB/s)","618.60 (min 253.42, max 983.77)","3868.63 (min 2210.35, max 5526.90)","2859.29 (min 1419.19, max 4299.39)","2423.08 (min 836.12, max 4010.03)","100.01 (min 66.46, max 133.55)"
    "bw_mem-fwr-4mb (MB/s)","625.49 (min 249.59, max 1001.38)","3251.63 (min 1207.00, max 5296.26)","1886.68 (min 1330.23, max 2443.12)","2225.65 (min 828.76, max 3622.53)","101.95 (min 69.48, max 134.41)"
    "bw_mem-fwr-8mb (MB/s)","622.33 (min 249.01, max 995.64)","3073.84 (min 1048.08, max 5099.60)","1630.96 (min 1246.30, max 2015.62)","2111.64 (min 828.16, max 3395.11)","141.53 (min 134.63, max 148.42)"
    "bw_mem-rd-16mb (MB/s)","252.09","3039.51","1215.62","2433.09","50.21"
    "bw_mem-rd-1mb (MB/s)","628.92 (min 273.26, max 984.57)","12173.90 (min 10894.06, max 13453.74)","2007.45 (min 1940.99, max 2073.91)","1755.11 (min 871.69, max 2638.52)","126.14 (min 50.46, max 201.82)"
    "bw_mem-rd-2mb (MB/s)","618.50 (min 253.39, max 983.61)","8841.42 (min 8838.61, max 8844.22)","1739.25 (min 1691.19, max 1787.31)","1578.12 (min 702.25, max 2453.99)","137.93 (min 52.47, max 223.39)"
    "bw_mem-rd-4mb (MB/s)","617.57 (min 251.98, max 983.16)","2480.96 (min 1614.64, max 3347.28)","1155.85 (min 1015.10, max 1296.60)","1564.85 (min 704.72, max 2424.98)","78.88 (min 52.06, max 105.70)"
    "bw_mem-rd-8mb (MB/s)","617.46 (min 251.75, max 983.16)","2189.33 (min 1305.27, max 3073.38)","1053.18 (min 887.21, max 1219.14)","1561.99 (min 700.10, max 2423.88)","153.24 (min 52.66, max 253.82)"
    "bw_mem-rdwr-16mb (MB/s)","202.77","1182.56","846.29","670.52","42.17"
    "bw_mem-rdwr-1mb (MB/s)","199.02 (min 191.20, max 206.83)","6007.46 (min 4576.24, max 7438.68)","1311.34 (min 818.60, max 1804.08)","711.48 (min 609.94, max 813.01)","41.64 (min 37.84, max 45.43)"
    "bw_mem-rdwr-2mb (MB/s)","198.96 (min 194.59, max 203.33)","2847.96 (min 1149.59, max 4546.32)","1074.35 (min 520.56, max 1628.13)","640.49 (min 604.96, max 676.02)","37.80 (min 36.02, max 39.57)"
    "bw_mem-rdwr-4mb (MB/s)","199.92 (min 197.54, max 202.30)","1219.10 (min 1052.91, max 1385.28)","727.41 (min 466.91, max 987.90)","639.56 (min 604.69, max 674.42)","39.85 (min 37.98, max 41.72)"
    "bw_mem-rdwr-8mb (MB/s)","202.65 (min 202.56, max 202.74)","1124.88 (min 1043.84, max 1205.91)","659.75 (min 460.11, max 859.38)","641.54 (min 610.41, max 672.66)","41.36 (min 39.52, max 43.20)"
    "bw_mem-wr-16mb (MB/s)","995.83","1277.65","876.57","697.47","267.31"
    "bw_mem-wr-1mb (MB/s)","595.70 (min 206.83, max 984.57)","10446.21 (min 7438.68, max 13453.74)","1872.54 (min 1804.08, max 1940.99)","842.35 (min 813.01, max 871.69)","119.83 (min 37.84, max 201.82)"
    "bw_mem-wr-2mb (MB/s)","593.47 (min 203.33, max 983.61)","6692.47 (min 4546.32, max 8838.61)","1659.66 (min 1628.13, max 1691.19)","689.14 (min 676.02, max 702.25)","129.71 (min 36.02, max 223.39)"
    "bw_mem-wr-4mb (MB/s)","592.73 (min 202.30, max 983.16)","1499.96 (min 1385.28, max 1614.64)","1001.50 (min 987.90, max 1015.10)","689.57 (min 674.42, max 704.72)","73.71 (min 41.72, max 105.70)"
    "bw_mem-wr-8mb (MB/s)","592.95 (min 202.74, max 983.16)","1255.59 (min 1205.91, max 1305.27)","873.30 (min 859.38, max 887.21)","686.38 (min 672.66, max 700.10)","148.51 (min 43.20, max 253.82)"
    "bw_mmap_rd-mo-1mb (MB/s)","263.71","4124.82","1963.58","1553.33","133.24"
    "bw_mmap_rd-o2c-1mb (MB/s)","175.32","1414.68","912.74","600.60","85.00"
    "bw_pipe (MB/s)","284.46","601.67","966.41","420.76","27.79"
    "bw_unix (MB/s)","174.44","2054.91","1175.02","661.28","30.82"
    "lat_connect (us)","80.23","56.24","65.11","87.38","1059.50"
    "lat_ctx-2-128k (us)","37.06","4.08","8.93","6.29","180.00"
    "lat_ctx-2-256k (us)","4.00","4.00","10.62","4.00","166.25"
    "lat_ctx-4-128k (us)","64.82","6.11","10.73","3.50","209.03"
    "lat_ctx-4-256k (us)","0.00","0.00","18.50","0.00","246.58"
    "lat_fs-0k (num_files)","207.00","341.00","267.00","198.00","22.00"
    "lat_fs-10k (num_files)","71.00","139.00","71.00","89.00","8.00"
    "lat_fs-1k (num_files)","101.00","200.00","77.00","125.00","13.00"
    "lat_fs-4k (num_files)","117.00","182.00","77.00","128.00","12.00"
    "lat_mem_rd-stride128-sz1000k (ns)","221.43","12.82","31.32","123.82","230.81"
    "lat_mem_rd-stride128-sz125k (ns)","11.79","12.68","9.46","20.05","218.15"
    "lat_mem_rd-stride128-sz250k (ns)","55.01","12.82","10.11","20.18","217.58"
    "lat_mem_rd-stride128-sz31k (ns)","3.01","6.46","3.80","10.05","176.55"
    "lat_mem_rd-stride128-sz50 (ns)","3.01","2.67","3.76","4.00","5.07"
    "lat_mem_rd-stride128-sz500k (ns)","187.76","12.82","10.45","50.57","230.42"
    "lat_mem_rd-stride128-sz62k (ns)","9.14","12.68","8.02","18.06","217.40"
    "lat_mmap-1m (us)","69.00","48.00","22.00","85.00","662.00"
    "lat_ops-double-add (ns)","2.37","0.73","0.91","1.09","35.12"
    "lat_ops-double-mul (ns)","11.03","3.34","5.02","5.03","103.29"
    "lat_ops-float-add (ns)","2.29","0.73","0.91","1.10","21.44"
    "lat_ops-float-mul (ns)","10.02","3.34","5.01","5.00","65.95"
    "lat_ops-int-add (ns)","1.01","0.67","1.25","1.01","1.68"
    "lat_ops-int-bit (ns)","0.67","0.45","0.84","0.67","2.54"
    "lat_ops-int-div (ns)","58.42","58.46","7.52","87.74","198.32"
    "lat_ops-int-mod (ns)","23.49","10.26","7.94","15.48","87.76"
    "lat_ops-int-mul (ns)","6.05","2.09","3.80","3.14","6.60"
    "lat_ops-int64-add (ns)","1.21","0.74","1.26","1.10","5.32"
    "lat_ops-int64-bit (ns)","1.04","0.68","0.84","1.03","2.57"
    "lat_ops-int64-div (ns)","239.87","125.68","11.92","184.77","858.20"
    "lat_ops-int64-mod (ns)","71.22","22.75","9.19","34.10","256.30"
    "lat_pagefault (us)","1.69","0.99","2.96","1.73","7.68"
    "lat_pipe (us)","35.57","24.35","23.35","35.39","514.21"
    "lat_proc-exec (us)","1992.67","961.00","1377.75","1205.00","7483.00"
    "lat_proc-fork (us)","1700.00","924.33","1344.25","1103.40","6985.00"
    "lat_proc-proccall (us)","0.02","0.01","0.01","0.01","0.08"
    "lat_select (us)","45.88","28.78","58.37","49.34","239.18"
    "lat_sem (us)","5.20","2.58","3.61","6.84","106.73"
    "lat_sig-catch (us)","6.28","3.61","7.25","5.65","38.23"
    "lat_sig-install (us)","1.38","0.64","0.78","0.97","4.05"
    "lat_sig-prot (us)","0.44","0.34","0.57","0.45","2.02"
    "lat_syscall-fstat (us)","2.01","0.99","1.83","1.52","10.07"
    "lat_syscall-null (us)","0.56","0.32","0.44","0.46","2.56"
    "lat_syscall-open (us)","254.64","150.71","202.85","204.61","1544.75"
    "lat_syscall-read (us)","1.10","0.46","1.12","0.74","5.05"
    "lat_syscall-stat (us)","5.97","3.51","5.52","5.17","61.02"
    "lat_syscall-write (us)","0.74","0.38","0.76","0.57","3.78"
    "lat_tcp (us)","1.09","0.58","0.84","0.84","4.53"
    "lat_unix (us)","43.64","28.84","46.50","47.52","736.29"
    "latency_for_0.50_mb_block_size (nanosec)","187.76","12.82","10.45","50.57","230.42"
    "latency_for_1.00_mb_block_size (nanosec)","110.72 (min 0.00, max 221.43)","6.41 (min 0.00, max 12.82)","15.66 (min 0.00, max 31.32)","61.91 (min 0.00, max 123.82)","115.40 (min 0.00, max 230.81)"
    "pipe_bandwidth (MBs)","284.46","601.67","966.41","420.76","27.79"
    "pipe_latency (microsec)","35.57","24.35","23.35","35.39","514.21"
    "procedure_call (microsec)","0.02","0.01","0.01","0.01","0.08"
    "select_on_200_tcp_fds (microsec)","45.88","28.78","58.37","49.34","239.18"
    "semaphore_latency (microsec)","5.20","2.58","3.61","6.84","106.73"
    "signal_handler_latency (microsec)","1.38","0.64","0.78","0.97","4.05"
    "signal_handler_overhead (microsec)","6.28","3.61","7.25","5.65","38.23"
    "tcp_ip_connection_cost_to_localhost (microsec)","80.23","56.24","65.11","87.38","1059.50"
    "tcp_latency_using_localhost (microsec)","1.09","0.58","0.84","0.84","4.53"


Table:  **LM Bench Metrics**

Dhrystone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed. For standard ARM
cores the DMIPS/MHz score will be identical with the same compiler and flags.

.. csv-table::
    :header: "Benchmarks","am335x-evm: perf","am57xx-evm: perf","am654x-evm: perf","k2g-evm: perf","omapl138-lcdk: perf"

    "cpu_clock (MHz)","1000.00","1500.00","400.00","50.00","230.00"
    "dhrystone_per_mhz (DMIPS/MHz)","2.10","3.30","6.10","67.00","1.80"
    "dhrystone_per_second (DhrystoneP)","3636363.80","8695652.00","4255319.00","5882353.00","743494.40"


Table:  **Dhrystone Benchmark**

Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Benchmarks","am335x-evm: perf","am57xx-evm: perf","am654x-evm: perf","k2g-evm: perf","omapl138-lcdk: perf"

    "whetstone (MIPS)","833.30","5000.00","3333.30","2500.00","31.70"


Table:  **Whetstone Benchmark**

Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
sloving a dense linear system.

.. csv-table::
    :header: "Benchmarks","am335x-evm: perf","am57xx-evm: perf","am654x-evm: perf","k2g-evm: perf","omapl138-lcdk: perf"

    "linpack (Kflops)","52820.00","964826.00","336288.00","631012.00","7444.00"


Table:  **Linpack Benchmark**

NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Benchmarks","am335x-evm: perf","am57xx-evm: perf","am654x-evm: perf","k2g-evm: perf","omapl138-lcdk: perf"

    "assignment (Iterations)","7.59","16.53","7.71","11.05","0.98"
    "fourier (Iterations)","2381.90","18809.00","8265.50","12581.00","124.04"
    "fp_emulation (Iterations)","75.88","170.48","61.54","113.49","18.78"
    "huffman (Iterations)","723.32","1450.90","673.99","967.21","221.16"
    "idea (Iterations)","1323.60","3665.90","1920.70","2442.30","452.60"
    "lu_decomposition (Iterations)","75.69","823.37","323.47","553.09","5.85"
    "neural_net (Iterations)","2.06","22.79","4.22","15.29","0.19"
    "numeric_sort (Iterations)","378.10","658.53","299.17","444.86","96.92"
    "string_sort (Iterations)","66.89","141.11","94.72","93.98","7.46"


Table:  **NBench Benchmarks**

Stream
^^^^^^^^^^^^^^^^^^^^^^^^^^^
STREAM is a microbenchmarks for measuring data memory system performance without
any data reuse. It is designed to miss on caches and exercise data prefetcher and
apeculative accesseses. it uses double precision floating point (64bit) but in
most modern processors the memory access will be the bottleck. The four individual
scores are copy, scale as in multiply by constant, add two numbers, and triad for
multiply accumulate. For bandwidth a byte read counts as one and a byte written
counts as one resulting in a score that is double the bandwidth LMBench will show.

.. csv-table::
    :header: "Benchmarks","am335x-evm: perf","am57xx-evm: perf","am654x-evm: perf","k2g-evm: perf"

    "add (MB/s)","382.10","3985.00","1658.90","2422.90"
    "copy (MB/s)","434.90","4123.20","1849.80","2495.30"
    "scale (MB/s)","627.10","4644.40","1893.80","2399.80"
    "triad (MB/s)","386.70","4043.30","1558.30","2398.00"


Table:  **Stream**

CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark\ |reg|\ -Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark\ |reg| benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.



Table:  **CoreMarkPro**

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



Table:  **Multibench**

Spec2K6
^^^^^^^^^^^^^^^^^^^^^^^^^^^
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


Table:  **Spec2K6**

Speed (Single Core)


Table:  **Spec2K6 Speed**


Boot-time Measurement
-------------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Boot Configuration","am335x-evm: boot time (sec)","am57xx-evm: boot time (sec)","am654x-evm: boot time (sec)","k2g-evm: boot time (sec)","omapl138-lcdk: boot time (sec)"

    "Kernel boot time test when bootloader, kernel and sdk-rootfs are in mmc-sd","43.50 (min 43.00, max 44.25)","25.51 (min 20.91, max 28.74)","15.16 (min 14.70, max 15.79)","35.06 (min 34.94, max 35.24)","126.29 (min 124.00, max 129.00)"
    "Kernel boot time test when init is /bin/sh and bootloader, kernel and sdk-rootfs are in mmc-sd","6.35 (min 6.22, max 6.88)","7.12 (min 6.92, max 7.70)","5.51 (min 5.44, max 5.59)","7.54 (min 7.53, max 7.54)","9.47 (min 9.17, max 10.63)"

Table:  **Boot time MMC/SD**

Boot media: NAND
^^^^^^^^^^^^^^^^^^^^^^^^^^^


Table:  **Boot time MMC/SD**


ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table::
    :header: "Sampling Rate (Hz)","am335x-evm: Throughput (bits/sec)","am335x-evm: CPU Load (%)","am57xx-evm: Throughput (bits/sec)","am57xx-evm: CPU Load (%)","am654x-evm: Throughput (bits/sec)","am654x-evm: CPU Load (%)","k2g-evm: Throughput (bits/sec)","k2g-evm: CPU Load (%)","omapl138-lcdk: Throughput (bits/sec)","omapl138-lcdk: CPU Load (%)"

    "8000","255998.00","3.68","255992.00","0.10","255995.00","0.18","352799.00","0.56","256005.00","2.07"
    "11025","352797.00","3.69","352792.00","0.15","352794.00","0.19","352799.00","0.40","352810.00","3.05"
    "16000","511995.00","4.20","511984.00","0.21","511991.00","0.16","352799.00","0.40","512019.00","4.49"
    "22050","705593.00","7.67","705585.00","0.28","705587.00","0.32","705597.00","0.85","705635.00","6.01"
    "24000","705593.00","7.55","705585.00","0.25","705587.00","0.31","705597.00","0.75","705635.00","5.71"
    "32000","1023988.00","0.78","1023968.00","0.29","1023981.00","0.20","705597.00","0.75","1024072.00","9.72"
    "44100","1411182.00","14.27","1411169.00","0.45","1411173.00","0.55","1411194.00","1.33","1411335.00","11.45"
    "48000","1535979.00","23.00","1535952.00","0.44","1535970.00","0.85","1411194.00","1.45","1536160.00","12.54"
    "88200","2822349.00","28.76","2822338.00","0.97","2822340.00","1.02","2822384.00","2.87","2560997.00","23.41"
    "96000","3071941.00","1.22","3071903.00","0.82","3071935.00","0.53","2822384.00","2.76","2962684.00","28.99"

Table:  **Audio Capture**

|

.. csv-table::
    :header: "Sampling Rate (Hz)","am335x-evm: Throughput (bits/sec)","am335x-evm: CPU Load (%)","am57xx-evm: Throughput (bits/sec)","am57xx-evm: CPU Load (%)","k2g-evm: Throughput (bits/sec)","k2g-evm: CPU Load (%)","omapl138-lcdk: Throughput (bits/sec)","omapl138-lcdk: CPU Load (%)"

    "8000","256101.00","2.43","256093.00","0.09","352941.00","0.37","256108.00","2.42"
    "11025","352939.00","3.74","352931.00","0.12","352941.00","0.38","352952.00","2.99"
    "16000","512201.00","1.36","512185.00","0.21","352941.00","0.41","512225.00","4.32"
    "22050","705876.00","7.74","705862.00","0.25","705883.00","0.64","705919.00","5.46"
    "24000","705877.00","7.48","705862.00","0.26","705882.00","0.66","705919.00","5.46"
    "32000","1024400.00","1.05","1024371.00","0.41","705883.00","0.70","1024485.00","7.53"
    "44100","1411749.00","13.99","1411724.00","0.27","1411764.00","1.21","1411904.00","11.15"
    "48000","1536597.00","15.43","1536556.00","0.44","1411764.00","1.37","1536776.00","11.82"
    "88200","2823484.00","27.96","2823445.00","1.15","2823526.00","2.80","2731866.00","24.55"
    "96000","3073201.00","1.16","3073109.00","0.91","2823526.00","2.53","2863485.00","23.44"

Table:  **Audio Playback**

|

Sensor Capture
-------------------------

Capture video frames (MMAP buffers) with v4l2c-ctl and record the
reported fps

.. csv-table::
    :header: "Resolution","Format","am57xx-evm: Fps","am57xx-evm: Sensor"

    "1280x800","nv12","30.03","ov10635"
    "1280x800","rgb4","30.03","ov10635"
    "160x128","nv12","40.81 (min 40.60, max 40.91)","mt9t111"
    "160x128","rgb4","40.81 (min 40.60, max 40.91)","mt9t111"
    "2048x1536","nv12","6.64 (min 6.10, max 6.70)","mt9t111"
    "2048x1536","rgb4","6.64 (min 6.10, max 6.70)","mt9t111"
    "320x240","nv12","30.03","ov10635"
    "320x240","rgb4","30.03","ov10635"

Table:  **Sensor Capture**

|

Display Driver
-------------------------


.. csv-table::
    :header: "Mode","am335x-evm: Fps","am57xx-evm: Fps","am654x-evm: Fps","k2g-evm: Fps"

    "1280x800\@60","","","59.92 (min 50.70, max 60.01)",""
    "800x480\@60","","59.52 (min 59.50, max 59.56)","",""
    "800x480\@62","61.89 (min 61.86, max 61.92)","","",""

Table:  **Display performance (LCD)**


|



|


.. csv-table::
    :header: "Mode","am335x-evm: Fps","am57xx-evm: Fps","am654x-evm: Fps","k2g-evm: Fps"

    "1024x576\@60","59.97 (min 59.94, max 59.99)","59.97 (min 59.94, max 60.01)","","60.01 (min 60.00, max 60.01)"
    "1024x768\@60","","60.00 (min 59.98, max 60.04)","",""
    "1024x768\@70","","70.07 (min 70.03, max 70.13)","",""
    "1024x768\@75","","75.03 (min 74.86, max 75.19)","",""
    "1152x864\@75","","75.00 (min 74.82, max 75.18)","",""
    "1280x1024\@60","","60.02 (min 60.00, max 60.06)","",""
    "1280x1024\@75","","75.02 (min 75.00, max 75.06)","",""
    "1280x720\@60","60.00 (min 59.97, max 60.02)","60.00 (min 59.96, max 60.04)","","60.00"
    "1280x768\@60","","59.87 (min 59.84, max 59.90)","",""
    "1280x768\@75","","74.89 (min 74.86, max 74.94)","",""
    "1280x800\@60","","59.81 (min 59.77, max 59.86)","",""
    "1280x800\@75","","74.93 (min 74.90, max 74.99)","",""
    "1280x960\@60","","60.00 (min 59.88, max 60.12)","",""
    "1360x768\@60","","59.95 (min 59.91, max 59.98)","",""
    "1400x1050\@60","","59.98 (min 59.82, max 60.14)","",""
    "1400x1050\@75","","74.87 (min 74.84, max 74.91)","",""
    "1440x900\@60","","59.89 (min 59.85, max 59.93)","",""
    "1440x900\@75","","74.98 (min 74.88, max 75.09)","",""
    "1600x1200\@60","","60.00 (min 59.97, max 60.04)","",""
    "1600x1200\@65","","65.00 (min 64.98, max 65.05)","",""
    "1600x1200\@70","","70.00 (min 69.95, max 70.06)","",""
    "1600x900\@60","","60.00 (min 59.89, max 60.13)","",""
    "1680x1050\@60","","59.95 (min 59.93, max 59.99)","",""
    "1680x1050\@75","","74.89 (min 74.83, max 74.96)","",""
    "1680x945\@60","","60.02 (min 59.99, max 60.04)","",""
    "1920x1080\@60","","60.00 (min 59.97, max 60.03)","",""
    "2048x1152\@60","","60.00 (min 59.97, max 60.03)","",""
    "640x480\@60","60.00 (min 59.97, max 60.03)","60.00 (min 59.98, max 60.03)","",""
    "640x480\@73","72.81 (min 72.76, max 72.84)","72.81 (min 72.76, max 72.87)","",""
    "640x480\@75","75.00 (min 74.85, max 75.16)","75.00 (min 74.89, max 75.10)","",""
    "720x400\@70","70.08 (min 70.05, max 70.11)","70.08 (min 70.05, max 70.12)","",""
    "800x600\@56","56.25 (min 56.23, max 56.27)","56.25 (min 56.22, max 56.28)","",""
    "800x600\@60","60.32 (min 60.30, max 60.33)","60.32 (min 60.29, max 60.35)","",""
    "800x600\@72","72.19 (min 72.14, max 72.23)","72.19 (min 72.15, max 72.24)","","72.19 (min 72.18, max 72.19)"
    "800x600\@75","75.00 (min 74.95, max 75.05)","75.00 (min 74.97, max 75.04)","","75.00 (min 74.99, max 75.01)"
    "832x624\@75","74.55 (min 74.46, max 74.64)","74.55 (min 74.44, max 74.64)","","74.57 (min 74.57, max 74.58)"
    "848x480\@60","60.00 (min 59.97, max 60.04)","60.00 (min 59.97, max 60.03)","",""

Table:  **Display performance (HDMI)**


|


.. csv-table::
    :header: "Mode","am335x-evm: Fps","am57xx-evm: Fps","am654x-evm: Fps","k2g-evm: Fps"

    "800x480\@60","","59.52 (min 59.50, max 59.56)","",""

Table:  **Display performance (HDMI)**


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
    :header: "Benchmark","am335x-evm: Test Number","am335x-evm: Fps","am57xx-evm: Test Number","am57xx-evm: Fps"

    "GLB25_EgyptTestC24Z16FixedTime test","2500005.00","5.13 (min 1.35, max 13.75)","2500005.00","35.02 (min 19.52, max 59.52)"
    "GLB25_EgyptTestC24Z16_ETC1 test","2501001.00","6.26 (min 2.32, max 14.51)","2501001.00","43.07 (min 18.90, max 59.53)"
    "GLB25_EgyptTestC24Z16_ETC1to565 test","2501401.00","6.27 (min 2.32, max 14.51)","2501401.00","43.06 (min 19.20, max 59.53)"
    "GLB25_EgyptTestC24Z16_PVRTC4 test","2501101.00","6.09 (min 2.29, max 13.98)","2501101.00","43.03 (min 18.90, max 59.53)"
    "GLB25_EgyptTestC24Z24MS4 test","2500003.00","5.02 (min 0.66, max 11.60)","2500003.00","42.16 (min 18.54, max 59.53)"
    "GLB25_EgyptTestStandard_inherited test","2000000.00","22.98 (min 14.97, max 30.95)","2000000.00","59.49 (min 57.55, max 59.53)"


.. csv-table::
    :header: "Benchmark","am57xx-evm: Test Number","am57xx-evm: Fps"

    "GLB25_EgyptTestC24Z16_ETC1_Offscreen test","2501011.00","29.00"
    "GLB25_EgyptTestStandardOffscreen_inherited test","2000010.00","98.00"


Table:  **GLBenchmark 2.5 Performance**

Vertex Throughput
"""""""""""""""""""""""""""

.. csv-table::
    :header: "Benchmark","am335x-evm: Test Number","am335x-evm: Rate (triangles/sec)","am57xx-evm: Test Number","am57xx-evm: Rate (triangles/sec)"

    "GLB25_TriangleTexFragmentLitTestC24Z16 test","2500511.00","2205658.25","2500511.00","24907146.00"
    "GLB25_TriangleTexTestC24Z16 test","2500301.00","11388113.00","2500301.00","105226072.00"
    "GLB25_TriangleTexVertexLitTestC24Z16 test","2500411.00","3063717.50","2500411.00","39242812.00"


Table:  **GLBenchmark 2.5 Vertex Throughput**

Pixel Throughput
"""""""""""""""""""""""""""

.. csv-table::
    :header: "Benchmark","am335x-evm: Test Number","am335x-evm: Rate (texel/sec)","am335x-evm: Fps","am57xx-evm: Test Number","am57xx-evm: Rate (texel/sec)","am57xx-evm: Fps"

    "GLB25_FillTestC24Z16 test","2500101.00","108388880.00","4.54 (min 4.18, max 6.69)","2500101.00","1440019072.00","58.55 (min 55.56, max 59.53)"


Table:  **GLBenchmark 2.5 Pixel Throughput**

GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests



Table:  **GFXBench**

Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table::
    :header: "Benchmark","am335x-evm: Score","am57xx-evm: Score","am654x-evm: Score"

    "Glmark2-DRM","47.00","57.00"
    "Glmark2-Wayland","39.00","465.00","251.00"


Table:  **Glmark2**

|

Multimedia (Decode)
-------------------------

Run gstreamer pipeline "gst-launch-1.0 playbin uri=\ file://\ <Path to
stream> video-sink="kmssink sync=false connector=<connector id>"
audio-sink=fakesink" and calculate performance based on the execution
time reported. All display display outputs (HDMI and LCD) were connected
when running these tests, but playout was forced to LCD via the
connector=<connector id> option.

H264
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Resolution","am57xx-evm: Fps","am57xx-evm: IVA Freq (MHz)","am57xx-evm: IPU Freq (MHz)"

    "1080i","30300.00","532.00","1064.00"
    "1080p","60.00","532.00","1064.00"
    "720p","59940.00","532.00","1064.00"
    "720x480","24.17","532.00","1064.00"
    "800x480","30.00","532.00","1064.00"
    "CIF","90000.00","532.00","1064.00"

Table:  **Gstreamer H264 in AVI Container Decode Performance**

|

MPEG4
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Resolution","am57xx-evm: Fps","am57xx-evm: IVA Freq (MHz)","am57xx-evm: IPU Freq (MHz)"

    "CIF","30.00","532.00","1064.00"
    "QVGA","30.00","532.00",""
    "VGA","","532.00","1064.00"


Table:  **GStreamer MPEG4 in 3GP Container Decode Performance**

|

MPEG2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Resolution","am57xx-evm: Fps","am57xx-evm: IVA Freq (MHz)","am57xx-evm: IPU Freq (MHz)"

    "1080p","60.00","532.00","1064.00"
    "720p","29.97","532.00","1064.00"


Table:  **GStreamer MPEG2 in MP4 Container Decode Performance**

|

Machine Learning
-------------------------

TensorFlow Lite
^^^^^^^^^^^^^^^^^^^^^^^^^^^
TensorFlow Lite https://www.tensorflow.org/lite/ is open source deep
learning runtime for on-device inference. Processor SDK supports
TensorFlow Lite execution on Cortex A cores on all Sitara devices.

The table below lists TensorFlow Lite performance benchmarks when running
several well-known models on Sitara devices. The benchmarking data are
obtained with the benchmark_model binary, which is released in the
TensorFlow Lite source package and included in Processor SDK Linux filesystem.


Table:  **TensorFlow Lite Performance**

|

Ethernet Driver - CPSW CPSW2G NETCP
-------------------------------------

TCP Throughput
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "TCP Window Size (KBytes)","am335x-evm: Throughput (Mbits/sec)","am335x-evm: CPU Load ","am57xx-evm: Throughput (Mbits/sec)","am57xx-evm: CPU Load ","am654x-evm: Throughput (Mbits/sec)","am654x-evm: CPU Load ","k2g-evm: Throughput (Mbits/sec)","k2g-evm: CPU Load ","omapl138-lcdk: Throughput (Mbits/sec)","omapl138-lcdk: CPU Load "

    "8","243.52","","632.48","","614.80","","500.00","","34.48",""
    "16","295.20","","640.80","","660.80","","689.60","","41.92",""
    "32","325.60","","937.60","","1079.20","","747.20","","52.88",""
    "64","353.60","","1200.00","","1593.60","","832.80","","64.40",""
    "128","370.48","","1153.60","","1391.20","","824.00","","70.16",""
    "256","344.80","","1146.40","","1466.40","","902.40","","62.56",""

Table: **TCP Throughput**

.. rubric::  TCP Throughput Interrupt Pacing
   :name: tcp-throughput-interrupt-pacing

.. csv-table::
    :header: "TCP Window Size (KBytes)","am335x-evm: Throughput (Mbits/sec)","am335x-evm: CPU Load ","am57xx-evm: Throughput (Mbits/sec)","am57xx-evm: CPU Load "

    "8","240.00","","598.40",""
    "16","296.80","","672.80",""
    "32","327.20","","936.80",""
    "64","359.20","","1157.60",""
    "128","369.60","","1104.00",""
    "256","372.00","","1126.40",""

Table: **TCP Throughput Interrupt Pacing**


UDP Throughput
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric::  UDP Throughput Egress
   :name: udp-throughput-egress

.. csv-table::
    :header: "UDP Datagram Size(bytes)","am335x-evm: Throughput (Mbits/sec)","am335x-evm: CPU Load ","am335x-evm: Packets Per Second (kpps) ","am57xx-evm: Throughput (Mbits/sec)","am57xx-evm: CPU Load ","am57xx-evm: Packets Per Second (kpps) ","am654x-evm: Throughput (Mbits/sec)","am654x-evm: CPU Load ","am654x-evm: Packets Per Second (kpps) ","k2g-evm: Throughput (Mbits/sec)","k2g-evm: CPU Load ","k2g-evm: Packets Per Second (kpps) "

    "64","22.30","100.00","42.00","52.90","65.65","101.00","44.10","45.43","85.00","22.70","100.00","42.00"
    "128","43.70","100.00","41.00","106.40","61.67","103.00","85.70","46.13","83.00","45.20","100.00","43.00"
    "256","87.40","100.00","42.00","202.30","71.26","98.00","168.10","47.20","82.00","90.10","100.00","43.00"
    "512","167.40","100.00","40.00","376.70","64.04","91.00","319.40","49.64","77.00","175.00","100.00","42.00"
    "1024","313.40","100.00","38.00","786.30","67.30","95.00","591.60","48.13","72.00","343.60","100.00","41.00"
    "1470","432.00","100.00","36.00","949.00","50.07","80.00","798.70","46.87","67.00","486.40","100.00","41.00"
    "1500","313.20","100.00","26.00","655.20","59.29","54.00","90.40","11.70","7.00","380.30","100.00","31.00"
    "4000","507.10","100.00","15.00","945.60","46.42","29.00","956.40","44.97","29.00"
    "8000","552.70","100.00","8.00","935.50","54.15","14.00","79.10","4.80","1.00"

Table: **UDP Throughput Egress**

.. rubric::  UDP Throughput Ingress
   :name: udp-throughput-ingress

.. csv-table::
    :header: "UDP Datagram Size(bytes)","am335x-evm: Throughput (Mbits/sec)","am335x-evm: CPU Load ","am335x-evm: Packets Per Second (kpps) ","am57xx-evm: Throughput (Mbits/sec)","am57xx-evm: CPU Load ","am57xx-evm: Packets Per Second (kpps) ","am654x-evm: Throughput (Mbits/sec)","am654x-evm: CPU Load ","am654x-evm: Packets Per Second (kpps) ","k2g-evm: Throughput (Mbits/sec)","k2g-evm: CPU Load ","k2g-evm: Packets Per Second (kpps) "

    "64","13.60","100.09","25.00","56.40","84.22","109.00","33.90","43.10","64.00","17.00","99.97","33.00"
    "128","27.20","100.00","26.00","110.90","85.10","107.00","90.60","42.01","87.00","33.10","100.00","32.00"
    "256","52.10","100.34","25.00","220.90","85.12","107.00","189.70","42.47","92.00","68.20","100.33","33.00"
    "512","82.40","99.86","20.00","461.80","84.51","112.00","377.20","42.47","92.00","135.90","98.64","32.00"
    "1024","84.90","100.21","10.00","917.40","85.61","111.00","753.00","42.85","91.00","294.00","99.95","35.00"
    "1470","12.90","100.01","1.00","956.20","65.74","81.00","93.30","7.90","7.00","82.40","92.61","6.00"
    "1500","1.60","99.07","0.00","471.30","77.92","39.00","84.20","11.50","7.00","415.30","100.00","34.00"
    "4000","0.00","0.17","0.00","24.20","72.73","0.00"
    "8000","956.80","66.81","14.00","92.80","6.60","1.00","241.80","10.48","3.00"

Table: **UDP Throughput Ingress**

|

-  iperf version 2.0.5
-  For receive performance, on DUT, invoke iperf in server mode.

::

    iperf -s -u

-  For transmit performance, on DUT, invoke iperf in client mode.

::

    iperf -c <server ip> -b <bandwidth limit> -f M -t 60

|

PCIe Driver
-------------------------

PCIe-ETH
^^^^^^^^^^^^^^^^^^^^^^^^^^^


Table: **PCI Ethernet**

PCIe-NVMe-SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^

AM654x-EVM
"""""""""""""""""""""""""""



.. csv-table::
    :header: "Buffer size (bytes)","am654x-evm: Write VFAT Throughput (Mbytes/sec)","am654x-evm: Write VFAT CPU Load (%)","am654x-evm: Read VFAT Throughput (Mbytes/sec)","am654x-evm: Read VFAT CPU Load (%)"

    "102400","314.05 (min 140.43, max 358.12)","25.82 (min 22.74, max 26.69)","634.84","23.96"
    "262144","330.48 (min 147.83, max 376.66)","25.83 (min 22.25, max 26.84)","546.11","21.38"
    "524288","331.01 (min 148.52, max 377.16)","25.93 (min 22.43, max 26.89)","541.37","22.24"
    "1048576","331.80 (min 148.93, max 378.78)","25.91 (min 22.38, max 26.94)","530.97","23.00"
    "5242880","333.20 (min 149.37, max 380.48)","25.80 (min 22.37, max 26.84)","585.12","24.51"




.. csv-table::
    :header: "Buffer size (bytes)","am654x-evm: Write EXT4 Throughput (Mbytes/sec)","am654x-evm: Write EXT4 CPU Load (%)","am654x-evm: Read EXT4 Throughput (Mbytes/sec)","am654x-evm: Read EXT4 CPU Load (%)"

    "102400","271.09 (min 162.78, max 460.55)","15.62 (min 8.06, max 25.12)","607.71","21.33"
    "262144","153.84 (min 148.25, max 156.40)","7.49 (min 6.62, max 10.25)","574.43","20.97"
    "524288","454.68 (min 350.35, max 481.60)","24.54 (min 24.28, max 25.25)","573.24","21.56"
    "1048576","456.24 (min 351.59, max 483.18)","24.55 (min 24.31, max 25.29)","563.63","21.77"
    "5242880","461.55 (min 352.77, max 489.82)","24.59 (min 24.36, max 25.49)","632.16","25.04"




- Filesize used is: 1G
- Platform: Speed 8GT/s, Width x1
- SSD being used: SAMSUNG MZVLW128HEGR










NAND Driver
-------------------------



AM335X-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Buffer size (bytes)","am335x-evm: Write UBIFS Throughput (Mbytes/sec)","am335x-evm: Write UBIFS CPU Load (%)","am335x-evm: Read UBIFS Throughput (Mbytes/sec)","am335x-evm: Read UBIFS CPU Load (%)"

    "102400","3.79 (min 3.73, max 3.91)","62.57 (min 61.14, max 64.49)","5.22","33.85"
    "262144","3.75 (min 3.73, max 3.77)","62.65 (min 62.15, max 63.17)","5.24","34.45"
    "524288","3.75 (min 3.74, max 3.78)","62.67 (min 62.36, max 62.96)","5.25","33.02"
    "1048576","3.75 (min 3.73, max 3.77)","62.84 (min 62.48, max 63.00)","5.23","34.41"
    "5242880","3.75 (min 3.73, max 3.78)","62.87 (min 62.42, max 63.24)","5.24","33.74"










OMAPL138-LCDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Buffer size (bytes)","omapl138-lcdk: Write UBIFS Throughput (Mbytes/sec)","omapl138-lcdk: Write UBIFS CPU Load (%)","omapl138-lcdk: Read UBIFS Throughput (Mbytes/sec)","omapl138-lcdk: Read UBIFS CPU Load (%)"

    "102400","1.39 (min 1.38, max 1.40)","100.00","2.01","100.00"
    "262144","1.41 (min 1.39, max 1.43)","100.00","2.01","100.00"
    "524288","1.41 (min 1.38, max 1.45)","100.00","2.01","100.00"
    "1048576","1.41 (min 1.39, max 1.43)","100.00","2.00","100.00"
    "5242880","1.41 (min 1.40, max 1.43)","100.00","1.99","100.00"





QSPI Flash Driver
-------------------------












AM654x-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^
UBIFS
"""""""""""""""""""""""""""
.. csv-table::
    :header: "Buffer size (bytes)","am654x-evm: Write UBIFS Throughput (Mbytes/sec)","am654x-evm: Write UBIFS CPU Load (%)","am654x-evm: Read UBIFS Throughput (Mbytes/sec)","am654x-evm: Read UBIFS CPU Load (%)"

    "102400","0.63 (min 0.49, max 1.13)","35.54 (min 29.03, max 43.20)","40.97","23.81"
    "262144","0.47 (min 0.35, max 0.53)","38.66 (min 29.44, max 47.72)","41.02","15.79"
    "524288","0.47 (min 0.35, max 0.53)","49.51 (min 44.36, max 53.83)","40.76","20.00"
    "1048576","0.47 (min 0.35, max 0.53)","50.91 (min 47.90, max 53.10)","40.15","23.81"




RAW
"""""""""""""""""""""""""""
.. csv-table::
    :header: "File size (Mbytes)","am654x-evm: Raw Read Throughput (Mbytes/sec)"

    "50","208.33"













K2G-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Buffer size (bytes)","k2g-evm: Write UBIFS Throughput (Mbytes/sec)","k2g-evm: Write UBIFS CPU Load (%)","k2g-evm: Read UBIFS Throughput (Mbytes/sec)","k2g-evm: Read UBIFS CPU Load (%)"

    "102400","0.46 (min 0.30, max 0.80)","100.00","13.58","0.00"
    "262144","0.37 (min 0.25, max 0.47)","100.00","13.48","14.29"
    "524288","0.34 (min 0.23, max 0.47)","100.00","13.43","7.69"
    "1048576","0.37 (min 0.25, max 0.47)","100.00","13.33","25.00"





SPI Flash Driver
-------------------------



K2G-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
    :header: "Buffer size (bytes)","k2g-evm: Write UBIFS Throughput (Mbytes/sec)","k2g-evm: Write UBIFS CPU Load (%)","k2g-evm: Read UBIFS Throughput (Mbytes/sec)","k2g-evm: Read UBIFS CPU Load (%)"

    "102400","0.09 (min 0.08, max 0.13)","56.74 (min 36.34, max 64.21)","0.19","1.85"
    "262144","0.08 (min 0.08, max 0.09)","61.60 (min 58.45, max 63.51)","0.19","1.93"
    "524288","0.08 (min 0.08, max 0.09)","61.96 (min 58.77, max 63.86)","0.19","1.28"
    "1048576","0.08 (min 0.08, max 0.09)","62.65 (min 59.96, max 65.57)","0.19","2.89"





AM654X-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. csv-table::
    :header: "Buffer size (bytes)","am654x-evm: Write UBIFS Throughput (Mbytes/sec)","am654x-evm: Write UBIFS CPU Load (%)","am654x-evm: Read UBIFS Throughput (Mbytes/sec)","am654x-evm: Read UBIFS CPU Load (%)"

    "102400","0.33 (min 0.25, max 0.57)","24.07 (min 23.51, max 24.98)","2.63","1.91"
    "262144","0.26 (min 0.24, max 0.28)","25.19 (min 24.15, max 25.87)","2.65","2.86"
    "524288","0.26 (min 0.24, max 0.29)","24.80 (min 23.02, max 25.94)","2.64","2.85"
    "1048576","0.27 (min 0.24, max 0.31)","25.50 (min 25.11, max 25.88)","2.64","3.76"





UFS Driver
-------------------------

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

|









EMMC Driver
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
    :header: "Buffer size (bytes)","am57xx-evm: Write VFAT Throughput (Mbytes/sec)","am57xx-evm: Write VFAT CPU Load (%)","am57xx-evm: Read VFAT Throughput (Mbytes/sec)","am57xx-evm: Read VFAT CPU Load (%)"

    "102400","12.43 (min 11.78, max 12.64)","2.34 (min 1.51, max 4.73)","65.51","0.00"
    "262144","12.40 (min 11.66, max 12.61)","2.27 (min 1.52, max 4.78)","68.44","9.15"
    "524288","12.39 (min 11.65, max 12.61)","2.37 (min 1.57, max 4.52)","72.95","7.75"
    "1048576","12.24 (min 11.08, max 12.56)","2.25 (min 1.57, max 4.34)","75.14","8.27"
    "5242880","12.40 (min 11.70, max 12.58)","2.32 (min 1.51, max 4.54)","75.10","7.30"

|



.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT2 Throughput (Mbytes/sec)","am57xx-evm: Write EXT2 CPU Load (%)","am57xx-evm: Read EXT2 Throughput (Mbytes/sec)","am57xx-evm: Read EXT2 CPU Load (%)"

    "102400","12.40 (min 11.90, max 12.62)","1.75 (min 1.15, max 3.70)","69.31","7.64"
    "262144","12.53 (min 12.23, max 12.63)","1.90 (min 1.33, max 3.58)","72.94","6.74"
    "524288","12.54 (min 12.30, max 12.63)","1.93 (min 1.39, max 3.77)","77.35","6.04"
    "1048576","12.56 (min 12.27, max 12.64)","1.91 (min 1.28, max 3.48)","78.52","0.40"
    "5242880","12.38 (min 11.90, max 12.62)","1.87 (min 1.27, max 3.71)","78.54","3.54"

|



.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT4 Throughput (Mbytes/sec)","am57xx-evm: Write EXT4 CPU Load (%)","am57xx-evm: Read EXT4 Throughput (Mbytes/sec)","am57xx-evm: Read EXT4 CPU Load (%)"

    "102400","12.30 (min 12.17, max 12.37)","1.78 (min 1.36, max 2.92)","63.03","8.33"
    "262144","12.43 (min 11.88, max 12.63)","1.83 (min 1.43, max 3.10)","72.99","8.01"
    "524288","12.56 (min 12.42, max 12.60)","1.82 (min 1.39, max 2.98)","78.34","12.06"
    "1048576","12.41 (min 11.87, max 12.62)","1.88 (min 1.39, max 2.86)","79.67","7.58"
    "5242880","12.42 (min 12.02, max 12.59)","1.81 (min 1.38, max 2.85)","79.97","6.56"

|












AM654x-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^
|



.. csv-table::
    :header: "Buffer size (bytes)","am654x-evm: Write VFAT Throughput (Mbytes/sec)","am654x-evm: Write VFAT CPU Load (%)","am654x-evm: Read VFAT Throughput (Mbytes/sec)","am654x-evm: Read VFAT CPU Load (%)"

    "102400","20.20 (min 18.80, max 20.61)","2.02 (min 1.52, max 3.73)","128.16","8.56"
    "262144","20.41 (min 19.58, max 20.66)","1.86 (min 1.42, max 3.50)","136.32","7.52"
    "524288","20.39 (min 19.62, max 20.64)","1.81 (min 1.32, max 3.33)","153.15","7.04"
    "1048576","20.41 (min 19.67, max 20.63)","1.89 (min 1.42, max 3.48)","151.65","8.66"
    "5242880","20.43 (min 19.68, max 20.64)","1.87 (min 1.38, max 3.38)","149.49","8.30"

|



.. csv-table::
    :header: "Buffer size (bytes)","am654x-evm: Write EXT2 Throughput (Mbytes/sec)","am654x-evm: Write EXT2 CPU Load (%)","am654x-evm: Read EXT2 Throughput (Mbytes/sec)","am654x-evm: Read EXT2 CPU Load (%)"

    "102400","21.01 (min 20.72, max 21.75)","1.21 (min 0.99, max 1.79)","130.24","7.52"
    "262144","21.02 (min 20.55, max 21.84)","1.21 (min 1.05, max 1.62)","141.12","7.48"
    "524288","21.06 (min 20.46, max 21.70)","1.18 (min 0.95, max 1.71)","160.90","7.39"
    "1048576","20.95 (min 20.42, max 21.74)","1.15 (min 0.95, max 1.61)","168.76","7.38"
    "5242880","21.01 (min 20.26, max 21.55)","1.21 (min 0.95, max 1.69)","167.31","8.50"

|



.. csv-table::
    :header: "Buffer size (bytes)","am654x-evm: Write EXT4 Throughput (Mbytes/sec)","am654x-evm: Write EXT4 CPU Load (%)","am654x-evm: Read EXT4 Throughput (Mbytes/sec)","am654x-evm: Read EXT4 CPU Load (%)"

    "102400","20.69 (min 20.42, max 21.31)","1.24 (min 1.07, max 1.69)","119.83","5.80"
    "262144","20.40 (min 20.23, max 20.51)","1.20 (min 1.11, max 1.54)","142.52","6.92"
    "524288","21.28 (min 20.53, max 21.71)","1.22 (min 1.03, max 1.65)","165.49","7.26"
    "1048576","20.76 (min 20.50, max 20.85)","1.22 (min 1.05, max 1.56)","180.47","8.70"
    "5242880","20.82 (min 20.50, max 20.96)","1.21 (min 1.00, max 1.80)","180.54","9.09"

|














































K2G-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^
|



.. csv-table::
    :header: "Buffer size (bytes)","k2g-evm: Write VFAT Throughput (Mbytes/sec)","k2g-evm: Write VFAT CPU Load (%)","k2g-evm: Read VFAT Throughput (Mbytes/sec)","k2g-evm: Read VFAT CPU Load (%)"

    "102400","21.45 (min 18.86, max 22.36)","12.56 (min 9.76, max 21.58)","39.64","15.71"
    "262144","21.49 (min 18.86, max 22.29)","12.95 (min 10.26, max 21.76)","40.38","14.57"
    "524288","21.37 (min 18.84, max 22.08)","13.22 (min 10.55, max 22.04)","41.56","15.02"
    "1048576","21.50 (min 18.84, max 22.26)","12.84 (min 10.28, max 21.16)","42.61","15.66"
    "5242880","21.57 (min 18.83, max 22.31)","12.66 (min 10.04, max 21.76)","42.67","13.64"

|



.. csv-table::
    :header: "Buffer size (bytes)","k2g-evm: Write EXT2 Throughput (Mbytes/sec)","k2g-evm: Write EXT2 CPU Load (%)","k2g-evm: Read EXT2 Throughput (Mbytes/sec)","k2g-evm: Read EXT2 CPU Load (%)"

    "102400","22.13 (min 20.46, max 22.82)","11.54 (min 9.11, max 20.70)","40.32","16.15"
    "262144","21.98 (min 20.82, max 22.34)","11.31 (min 8.74, max 20.92)","41.20","16.67"
    "524288","22.19 (min 20.79, max 22.77)","11.83 (min 8.73, max 22.00)","42.67","13.17"
    "1048576","22.35 (min 20.68, max 22.82)","11.27 (min 7.91, max 20.79)","43.03","13.22"
    "5242880","22.04 (min 20.79, max 22.44)","11.21 (min 8.12, max 20.92)","43.00","14.63"

|



.. csv-table::
    :header: "Buffer size (bytes)","k2g-evm: Write EXT4 Throughput (Mbytes/sec)","k2g-evm: Write EXT4 CPU Load (%)","k2g-evm: Read EXT4 Throughput (Mbytes/sec)","k2g-evm: Read EXT4 CPU Load (%)"

    "102400","21.36 (min 20.78, max 21.61)","11.13 (min 8.88, max 17.13)","36.82","14.74"
    "262144","21.35 (min 20.49, max 21.72)","11.37 (min 9.47, max 16.70)","38.42","13.33"
    "524288","21.83 (min 20.78, max 22.22)","11.54 (min 9.34, max 17.43)","43.01","13.64"
    "1048576","21.82 (min 21.06, max 22.27)","11.10 (min 8.47, max 17.30)","43.45","13.64"
    "5242880","21.79 (min 20.90, max 22.13)","11.62 (min 9.92, max 17.03)","43.46","13.69"

|



SATA Driver
-------------------------



.. rubric::  AM57XX-EVM
   :name: am57xx-evm-sata

|





.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT2 Throughput (Mbytes/sec)","am57xx-evm: Write EXT2 CPU Load (%)","am57xx-evm: Read EXT2 Throughput (Mbytes/sec)","am57xx-evm: Read EXT2 CPU Load (%)"

    "102400","121.52 (min 108.74, max 127.01)","10.85 (min 5.84, max 30.32)","134.82","11.49"
    "262144","121.95 (min 107.79, max 125.98)","11.14 (min 5.65, max 32.40)","132.97","11.18"
    "524288","124.29 (min 120.66, max 127.09)","11.33 (min 5.42, max 31.82)","132.97","10.69"
    "1048576","124.71 (min 119.41, max 126.87)","11.56 (min 6.03, max 31.61)","132.97","9.67"
    "5242880","124.41 (min 120.61, max 126.87)","11.20 (min 6.07, max 31.40)","132.97","9.62"

|



.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT4 Throughput (Mbytes/sec)","am57xx-evm: Write EXT4 CPU Load (%)","am57xx-evm: Read EXT4 Throughput (Mbytes/sec)","am57xx-evm: Read EXT4 CPU Load (%)"

    "102400","121.23 (min 117.85, max 124.80)","10.13 (min 6.49, max 23.99)","131.73","10.75"
    "262144","120.58 (min 116.77, max 124.75)","10.24 (min 6.66, max 23.88)","129.48","10.40"
    "524288","118.08 (min 112.23, max 122.82)","9.85 (min 5.55, max 23.63)","129.28","10.29"
    "1048576","118.24 (min 115.36, max 120.68)","10.38 (min 6.32, max 24.50)","129.12","10.03"
    "5242880","121.03 (min 117.31, max 126.78)","10.21 (min 6.87, max 22.35)","131.76","10.41"

|


























|

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

    "102400","62.67 (min 53.15, max 66.31)","8.32 (min 5.36, max 19.44)","218.88","21.20"
    "262144","62.39 (min 52.98, max 65.21)","8.05 (min 5.16, max 19.03)","224.62","18.54"
    "524288","62.90 (min 53.20, max 65.65)","8.42 (min 5.46, max 19.10)","234.87","22.41"
    "1048576","63.58 (min 53.34, max 69.10)","8.42 (min 5.20, max 19.38)","238.56","21.31"
    "5242880","62.94 (min 52.96, max 66.08)","8.11 (min 5.14, max 18.87)","220.97","20.30"

|



.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT2 Throughput (Mbytes/sec)","am57xx-evm: Write EXT2 CPU Load (%)","am57xx-evm: Read EXT2 Throughput (Mbytes/sec)","am57xx-evm: Read EXT2 CPU Load (%)"

    "102400","64.19 (min 62.87, max 64.83)","4.99 (min 2.74, max 13.55)","225.00","19.78"
    "262144","64.27 (min 63.48, max 64.88)","4.53 (min 2.56, max 10.95)","234.34","20.76"
    "524288","64.63 (min 63.62, max 65.28)","3.59 (min 2.81, max 5.92)","249.01","19.58"
    "1048576","64.33 (min 63.27, max 65.02)","3.38 (min 2.79, max 5.09)","257.04","21.85"
    "5242880","64.55 (min 63.66, max 64.98)","3.52 (min 2.92, max 5.23)","257.70","21.17"

|



.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT4 Throughput (Mbytes/sec)","am57xx-evm: Write EXT4 CPU Load (%)","am57xx-evm: Read EXT4 Throughput (Mbytes/sec)","am57xx-evm: Read EXT4 CPU Load (%)"

    "102400","64.60 (min 64.14, max 64.94)","4.46 (min 3.69, max 6.53)","230.48","21.76"
    "262144","64.24 (min 63.74, max 64.89)","4.26 (min 3.48, max 6.80)","237.89","19.46"
    "524288","64.10 (min 63.69, max 64.51)","4.71 (min 3.56, max 8.82)","254.62","20.03"
    "1048576","64.35 (min 63.59, max 64.88)","4.21 (min 3.15, max 7.02)","265.81","21.83"
    "5242880","64.51 (min 63.88, max 64.99)","4.21 (min 3.53, max 6.44)","271.09","21.31"

|

|

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










|

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|



AM335x-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^
|



.. csv-table::
    :header: "Buffer size (bytes)","am335x-evm: Write VFAT Throughput (Mbytes/sec)","am335x-evm: Write VFAT CPU Load (%)","am335x-evm: Read VFAT Throughput (Mbytes/sec)","am335x-evm: Read VFAT CPU Load (%)"

    "102400","9.59 (min 9.13, max 9.82)","10.20 (min 8.69, max 15.13)","20.57","25.00"
    "262144","9.58 (min 8.72, max 9.83)","10.24 (min 8.72, max 15.05)","20.80","21.64"
    "524288","9.55 (min 8.86, max 9.85)","10.13 (min 8.53, max 15.07)","21.28","18.63"
    "1048576","9.52 (min 8.77, max 9.77)","10.12 (min 8.41, max 14.60)","21.22","18.16"
    "5242880","9.49 (min 8.73, max 9.74)","9.66 (min 8.05, max 14.08)","21.09","18.98"

|



.. csv-table::
    :header: "Buffer size (bytes)","am335x-evm: Write EXT2 Throughput (Mbytes/sec)","am335x-evm: Write EXT2 CPU Load (%)","am335x-evm: Read EXT2 Throughput (Mbytes/sec)","am335x-evm: Read EXT2 CPU Load (%)"

    "102400","8.57 (min 3.92, max 10.04)","7.09 (min 6.07, max 7.69)","21.16","23.73"
    "262144","9.76 (min 8.69, max 10.19)","8.73 (min 7.50, max 12.21)","21.58","23.00"
    "524288","10.11 (min 9.65, max 10.23)","9.18 (min 7.87, max 13.75)","22.18","20.22"
    "1048576","9.76 (min 8.88, max 10.20)","8.56 (min 7.28, max 12.18)","22.48","15.23"
    "5242880","10.11 (min 9.76, max 10.24)","8.92 (min 7.39, max 14.17)","22.49","17.93"

|



.. csv-table::
    :header: "Buffer size (bytes)","am335x-evm: Write EXT4 Throughput (Mbytes/sec)","am335x-evm: Write EXT4 CPU Load (%)","am335x-evm: Read EXT4 Throughput (Mbytes/sec)","am335x-evm: Read EXT4 CPU Load (%)"

    "102400","9.01 (min 6.51, max 10.54)","8.18 (min 5.21, max 13.26)","19.06","20.52"
    "262144","9.07 (min 5.84, max 9.90)","7.63 (min 7.36, max 7.80)","21.72","22.45"
    "524288","9.79 (min 9.12, max 10.23)","8.68 (min 7.83, max 11.19)","22.35","18.88"
    "1048576","9.24 (min 6.72, max 9.90)","8.25 (min 7.62, max 8.79)","22.63","16.63"
    "5242880","9.82 (min 9.61, max 9.88)","8.60 (min 7.55, max 12.00)","22.82","16.38"

|


|

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|









|

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|



AM57XX-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^
|



.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write VFAT Throughput (Mbytes/sec)","am57xx-evm: Write VFAT CPU Load (%)","am57xx-evm: Read VFAT Throughput (Mbytes/sec)","am57xx-evm: Read VFAT CPU Load (%)"

    "102400","7.99 (min 7.57, max 8.66)","1.43 (min 0.92, max 2.97)","21.49","2.38"
    "262144","8.51 (min 7.42, max 9.74)","1.50 (min 1.10, max 2.81)","21.45","2.97"
    "524288","7.42 (min 6.60, max 8.71)","1.28 (min 0.85, max 2.61)","22.14","2.65"
    "1048576","7.10 (min 6.33, max 7.61)","1.36 (min 0.81, max 2.87)","22.12","2.22"
    "5242880","8.28 (min 7.40, max 8.95)","1.38 (min 0.94, max 2.52)","22.11","3.15"

|



.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT2 Throughput (Mbytes/sec)","am57xx-evm: Write EXT2 CPU Load (%)","am57xx-evm: Read EXT2 Throughput (Mbytes/sec)","am57xx-evm: Read EXT2 CPU Load (%)"

    "102400","9.25 (min 7.77, max 10.09)","1.35 (min 1.06, max 2.27)","21.61","1.67"
    "262144","10.13 (min 9.60, max 10.64)","1.51 (min 1.06, max 2.72)","21.98","2.93"
    "524288","9.91 (min 9.60, max 10.24)","1.45 (min 0.97, max 2.87)","22.55","2.57"
    "1048576","10.06 (min 9.28, max 10.32)","1.59 (min 1.16, max 3.03)","22.74","2.38"
    "5242880","10.20 (min 10.11, max 10.28)","1.60 (min 1.13, max 2.91)","22.73","2.28"

|



.. csv-table::
    :header: "Buffer size (bytes)","am57xx-evm: Write EXT4 Throughput (Mbytes/sec)","am57xx-evm: Write EXT4 CPU Load (%)","am57xx-evm: Read EXT4 Throughput (Mbytes/sec)","am57xx-evm: Read EXT4 CPU Load (%)"

    "102400","8.87 (min 7.11, max 10.62)","1.49 (min 0.92, max 2.74)","21.69","1.47"
    "262144","9.05 (min 7.30, max 10.17)","1.49 (min 1.14, max 1.99)","22.07","2.22"
    "524288","9.90 (min 9.57, max 10.21)","1.57 (min 1.13, max 2.70)","22.59","2.27"
    "1048576","10.01 (min 9.79, max 10.18)","1.52 (min 1.12, max 2.65)","22.82","2.29"
    "5242880","9.28 (min 9.08, max 9.58)","1.45 (min 1.01, max 2.52)","22.82","2.18"

|


|

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|









|

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|









|

The performance numbers were captured using the following:

-  SanDisk 8GB SDHC UHS Memory Card
-  Partition was mounted with async option

|



AM654x-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^
|



.. csv-table::
    :header: "Buffer size (bytes)","am654x-evm: Write VFAT Throughput (Mbytes/sec)","am654x-evm: Write VFAT CPU Load (%)","am654x-evm: Read VFAT Throughput (Mbytes/sec)","am654x-evm: Read VFAT CPU Load (%)"

    "102400","18.78 (min 13.69, max 21.04)","1.84 (min 1.48, max 2.98)","22.60","1.62"
    "262144","18.94 (min 15.80, max 20.48)","1.83 (min 1.09, max 3.66)","22.66","1.62"
    "524288","19.13 (min 15.67, max 20.82)","1.88 (min 1.08, max 3.76)","22.92","1.26"
    "1048576","18.55 (min 15.95, max 20.32)","1.78 (min 1.14, max 3.60)","22.77","1.25"
    "5242880","18.68 (min 15.74, max 20.19)","1.81 (min 1.09, max 3.81)","22.72","1.47"

|



.. csv-table::
    :header: "Buffer size (bytes)","am654x-evm: Write EXT2 Throughput (Mbytes/sec)","am654x-evm: Write EXT2 CPU Load (%)","am654x-evm: Read EXT2 Throughput (Mbytes/sec)","am654x-evm: Read EXT2 CPU Load (%)"

    "102400","14.78 (min 12.23, max 16.04)","0.89 (min 0.70, max 1.34)","22.96","1.43"
    "262144","19.70 (min 17.66, max 20.63)","1.14 (min 0.84, max 1.68)","23.23","1.33"
    "524288","19.17 (min 15.34, max 20.99)","1.07 (min 0.80, max 1.58)","23.63","1.19"
    "1048576","19.18 (min 15.32, max 20.65)","1.12 (min 0.77, max 1.69)","23.70","1.30"
    "5242880","19.08 (min 15.21, max 20.57)","1.06 (min 0.76, max 1.60)","23.69","1.36"

|



.. csv-table::
    :header: "Buffer size (bytes)","am654x-evm: Write EXT4 Throughput (Mbytes/sec)","am654x-evm: Write EXT4 CPU Load (%)","am654x-evm: Read EXT4 Throughput (Mbytes/sec)","am654x-evm: Read EXT4 CPU Load (%)"

    "102400","20.12 (min 19.80, max 20.65)","1.20 (min 1.06, max 1.56)","20.77","1.29"
    "262144","19.01 (min 18.26, max 19.52)","1.15 (min 0.99, max 1.53)","23.27","1.22"
    "524288","20.24 (min 19.92, max 20.81)","1.22 (min 1.10, max 1.59)","23.75","1.14"
    "1048576","20.19 (min 19.07, max 20.82)","1.19 (min 0.99, max 1.64)","23.88","1.14"
    "5242880","20.09 (min 18.85, max 20.89)","1.19 (min 1.06, max 1.61)","23.87","1.14"

|


|

The performance numbers were captured using the following:

-  SanDisk 8GB SDHC UHS Memory Card
-  Partition was mounted with async option

|









|

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|









|

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|









|

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|









|

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|



K2G-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^
|



.. csv-table::
    :header: "Buffer size (bytes)","k2g-evm: Write VFAT Throughput (Mbytes/sec)","k2g-evm: Write VFAT CPU Load (%)","k2g-evm: Read VFAT Throughput (Mbytes/sec)","k2g-evm: Read VFAT CPU Load (%)"

    "102400","9.48 (min 8.40, max 9.93)","5.64 (min 4.38, max 10.00)","21.38","9.98"
    "262144","9.31 (min 8.44, max 9.76)","5.72 (min 4.38, max 10.12)","21.48","9.24"
    "524288","8.39 (min 6.37, max 9.39)","5.10 (min 3.85, max 7.64)","21.95","6.84"
    "1048576","9.39 (min 8.66, max 9.90)","5.89 (min 4.06, max 11.07)","22.37","7.34"
    "5242880","9.12 (min 8.39, max 9.74)","5.60 (min 3.88, max 10.70)","22.28","8.70"

|



.. csv-table::
    :header: "Buffer size (bytes)","k2g-evm: Write EXT2 Throughput (Mbytes/sec)","k2g-evm: Write EXT2 CPU Load (%)","k2g-evm: Read EXT2 Throughput (Mbytes/sec)","k2g-evm: Read EXT2 CPU Load (%)"

    "102400","8.85 (min 8.04, max 9.18)","4.11 (min 2.98, max 8.28)","21.70","7.16"
    "262144","9.77 (min 9.49, max 10.02)","5.34 (min 3.86, max 10.23)","21.88","7.98"
    "524288","8.97 (min 8.39, max 9.44)","4.82 (min 3.46, max 9.36)","21.41","6.00"
    "1048576","8.77 (min 7.46, max 9.75)","4.34 (min 3.16, max 7.54)","21.92","7.11"
    "5242880","8.86 (min 8.12, max 9.39)","4.44 (min 3.21, max 8.01)","22.53","6.49"

|



.. csv-table::
    :header: "Buffer size (bytes)","k2g-evm: Write EXT4 Throughput (Mbytes/sec)","k2g-evm: Write EXT4 CPU Load (%)","k2g-evm: Read EXT4 Throughput (Mbytes/sec)","k2g-evm: Read EXT4 CPU Load (%)"

    "102400","8.89 (min 8.41, max 10.04)","4.71 (min 3.67, max 7.99)","21.77","8.35"
    "262144","9.32 (min 8.53, max 9.84)","4.81 (min 3.36, max 7.12)","22.12","7.86"
    "524288","9.10 (min 8.75, max 9.62)","4.69 (min 3.77, max 7.08)","22.64","6.94"
    "1048576","9.45 (min 9.12, max 9.61)","4.80 (min 3.76, max 7.48)","22.83","6.99"
    "5242880","9.65 (min 9.33, max 10.06)","5.16 (min 4.32, max 7.51)","22.83","6.99"

|


|

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|



OMAPL138-LCDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^
|



.. csv-table::
    :header: "Buffer size (bytes)","omapl138-lcdk: Write VFAT Throughput (Mbytes/sec)","omapl138-lcdk: Write VFAT CPU Load (%)","omapl138-lcdk: Read VFAT Throughput (Mbytes/sec)","omapl138-lcdk: Read VFAT CPU Load (%)"

    "102400","6.98 (min 4.50, max 8.04)","89.19 (min 65.19, max 99.13)","14.92","68.50"
    "262144","6.76 (min 4.53, max 7.59)","69.98 (min 56.21, max 75.79)","14.51","63.78"
    "524288","7.55 (min 4.73, max 8.46)","78.23 (min 54.20, max 84.53)","15.01","62.78"
    "1048576","7.44 (min 4.60, max 8.40)","84.64 (min 55.77, max 95.23)","15.22","60.83"
    "5242880","7.30 (min 4.50, max 8.30)","80.83 (min 54.24, max 92.65)","13.47","56.23"

|



.. csv-table::
    :header: "Buffer size (bytes)","omapl138-lcdk: Write EXT2 Throughput (Mbytes/sec)","omapl138-lcdk: Write EXT2 CPU Load (%)","omapl138-lcdk: Read EXT2 Throughput (Mbytes/sec)","omapl138-lcdk: Read EXT2 CPU Load (%)"

    "102400","6.46 (min 3.53, max 7.38)","52.46 (min 48.79, max 55.60)","15.94","60.76"
    "262144","7.51 (min 7.00, max 7.80)","58.07 (min 50.97, max 69.22)","15.80","58.78"
    "524288","7.79 (min 7.52, max 7.99)","60.10 (min 54.52, max 73.41)","16.20","56.00"
    "1048576","7.51 (min 6.96, max 7.81)","57.49 (min 53.92, max 62.45)","16.34","56.00"
    "5242880","7.73 (min 7.58, max 7.89)","59.15 (min 54.87, max 68.00)","16.19","57.01"

|



.. csv-table::
    :header: "Buffer size (bytes)","omapl138-lcdk: Write EXT4 Throughput (Mbytes/sec)","omapl138-lcdk: Write EXT4 CPU Load (%)","omapl138-lcdk: Read EXT4 Throughput (Mbytes/sec)","omapl138-lcdk: Read EXT4 CPU Load (%)"

    "102400","6.98 (min 5.66, max 7.68)","87.88 (min 84.50, max 89.63)","15.89","62.79"
    "262144","8.25 (min 7.88, max 8.65)","77.26 (min 71.30, max 87.02)","15.35","61.16"
    "524288","8.05 (min 7.74, max 8.56)","74.33 (min 64.81, max 87.10)","16.17","57.28"
    "1048576","8.51 (min 8.26, max 8.69)","80.88 (min 74.47, max 94.69)","16.33","56.16"
    "5242880","8.34 (min 7.44, max 8.72)","79.69 (min 73.71, max 91.86)","16.55","58.60"

|


|

|

|

The performance numbers were captured using the following:

-  SanDisk 8GB MicroSDHC Class 10 Memory Card
-  Partition was mounted with async option

|

UART Driver
-------------------------

Performance and Benchmarks not available in this release.

|

I2C Driver
-------------------------

Performance and Benchmarks not available in this release.

|

EDMA Driver
-------------------------

Performance and Benchmarks not available in this release.

|

Touchscreen Driver
-------------------------

Performance and Benchmarks not available in this release.

|

USB Driver
-------------------------

MUSB/XHCI Host controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::

  **IMPORTANT**: For Mass-storage applications, the performance numbers can be severely
  affected if the media is mounted in sync mode. Hot plug scripts in the
  filesystem mount removable media in sync mode to ensure data
  integrity. For performance sensitive applications, umount the
  auto-mounted filesystem and re-mount in async mode.

|

**Setup** : Inateck ASM1153E USB hard disk is
connected to usb0 port. File read/write performance data on usb0 port is
captured.

|


USB Host VFAT
^^^^^^^^^^^^^
.. csv-table::
    :header: "Buffer size (bytes)","am335x-evm: Write VFAT Throughput (Mbytes/sec)","am335x-evm: Write VFAT CPU Load (%)","am335x-evm: Read VFAT Throughput (Mbytes/sec)","am335x-evm: Read VFAT CPU Load (%)","am57xx-evm: Write VFAT Throughput (Mbytes/sec)","am57xx-evm: Write VFAT CPU Load (%)","am57xx-evm: Read VFAT Throughput (Mbytes/sec)","am57xx-evm: Read VFAT CPU Load (%)","am654x-evm: Write VFAT Throughput (Mbytes/sec)","am654x-evm: Write VFAT CPU Load (%)","am654x-evm: Read VFAT Throughput (Mbytes/sec)","am654x-evm: Read VFAT CPU Load (%)"

    "102400","19.88 (min 18.41, max 20.41)","29.71 (min 26.53, max 37.91)","13.72","35.78","253.74 (min 130.55, max 289.07)","57.55 (min 49.37, max 62.32)","339.33","36.84","37.46 (min 33.00, max 38.61)","4.53 (min 3.96, max 6.57)","38.85","4.28"
    "262144","19.57 (min 18.25, max 19.94)","30.39 (min 27.88, max 38.66)","13.76","34.69","264.79 (min 135.32, max 297.99)","56.71 (min 48.99, max 62.32)","325.91","34.48","37.77 (min 34.15, max 38.69)","4.15 (min 3.62, max 5.91)","38.79","4.73"




USB Host EXT2
^^^^^^^^^^^^^
.. csv-table::
    :header: "Buffer size (bytes)","am335x-evm: Write EXT2 Throughput (Mbytes/sec)","am335x-evm: Write EXT2 CPU Load (%)","am335x-evm: Read EXT2 Throughput (Mbytes/sec)","am335x-evm: Read EXT2 CPU Load (%)","am57xx-evm: Write EXT2 Throughput (Mbytes/sec)","am57xx-evm: Write EXT2 CPU Load (%)","am57xx-evm: Read EXT2 Throughput (Mbytes/sec)","am57xx-evm: Read EXT2 CPU Load (%)","am654x-evm: Write EXT2 Throughput (Mbytes/sec)","am654x-evm: Write EXT2 CPU Load (%)","am654x-evm: Read EXT2 Throughput (Mbytes/sec)","am654x-evm: Read EXT2 CPU Load (%)"

    "102400","20.13 (min 18.79, max 20.60)","26.56 (min 23.28, max 35.93)","13.69","36.03","286.68 (min 152.68, max 320.47)","51.73 (min 48.33, max 54.69)","336.27","36.21","39.38 (min 37.63, max 39.85)","3.09 (min 2.50, max 4.07)","38.58","3.43"
    "1048576","20.03 (min 18.68, max 20.43)","27.40 (min 24.11, max 37.57)","13.72","32.89","287.23 (min 154.04, max 321.20)","52.70 (min 50.38, max 55.38)","367.65","37.04","39.49 (min 37.94, max 39.93)","3.01 (min 2.31, max 3.83)","38.86","3.10"
    "5242880","20.07 (min 18.79, max 20.47)","26.01 (min 22.53, max 35.53)","13.72","38.00","286.56 (min 155.86, max 319.94)","51.38 (min 49.18, max 53.23)","363.56","35.85","39.37 (min 37.86, max 39.77)","3.12 (min 2.76, max 3.90)","38.55","5.57"




|
|

|
|

|
|

|
|

|
|

USBDEVICE HIGHSPEED SLAVE READ THROUGHPUT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. csv-table::
    :header: "Number of Blocks","am335x-evm: Throughput (MB/sec)","am654x-evm: Throughput (MB/sec)","k2g-evm: Throughput (MB/sec)","omapl138-lcdk: Throughput (MB/sec)"

    "16","","","","6.30"
    "150","56.60","84.80","65.70","6.30"


|
|

USBDEVICE HIGHSPEED SLAVE WRITE THROUGHPUT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. csv-table::
    :header: "Number of Blocks","am335x-evm: Throughput (MB/sec)","am654x-evm: Throughput (MB/sec)","k2g-evm: Throughput (MB/sec)","omapl138-lcdk: Throughput (MB/sec)"

    "16","","","","4.10"
    "150","90.90","49.90","41.30","4.00"


|
|

USBDEVICE HIGHSPEED CDC IPERF TCP THROUGHPUT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. csv-table::
    :header: "Window Size (kbytes)","am335x-evm: TX Throughput (Mbits/sec)","am335x-evm: RX Throughput (Mbits/sec)","am57xx-evm: TX Throughput (Mbits/sec)","am57xx-evm: RX Throughput (Mbits/sec)","am654x-evm: TX Throughput (Mbits/sec)","am654x-evm: RX Throughput (Mbits/sec)","omapl138-lcdk: TX Throughput (Mbits/sec)","omapl138-lcdk: RX Throughput (Mbits/sec)"

    "8","50.24","51.09","227.90","251.00","227.60","234.00","26.02","20.01"
    "16","51.65","49.77","234.10","249.00","233.80","245.00","22.83","23.72"
    "32","50.24","50.10","248.50","245.00","235.40","254.00","30.70","26.70"
    "64","51.67","50.65","257.00","247.00","245.00","253.00","31.20","30.20"
    "128","51.05","51.99","271.10","262.30","257.90","258.90","29.70","29.80"


|
|

|
|

CRYPTO Driver
-------------------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. csv-table::
    :header: "Algorithm","Buffer Size (in bytes)","am335x-evm: throughput (KBytes/Sec)","am57xx-evm: throughput (KBytes/Sec)","am654x-evm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","12322.47","14267.39","20305.24"
    "aes-128-cbc","16","2627.96","4173.05","357.04"
    "aes-128-cbc","256","4806.83","5129.22","5630.29"
    "aes-128-cbc","64","8013.46","13888.75","1427.95"
    "aes-128-cbc","8192","18669.57","31173.29","103336.62"
    "aes-192-cbc","1024","12464.47","14202.88","20647.59"
    "aes-192-cbc","16","2716.71","4017.27","363.07"
    "aes-192-cbc","256","4635.31","5120.60","5675.69"
    "aes-192-cbc","64","7994.07","13228.27","1451.67"
    "aes-192-cbc","8192","19098.28","31203.33","99956.05"
    "aes-256-cbc","1024","12062.04","14267.73","20652.37"
    "aes-256-cbc","16","2592.06","4234.49","362.20"
    "aes-256-cbc","256","4538.79","5099.09","5677.23"
    "aes-256-cbc","64","7686.98","13470.87","1446.02"
    "aes-256-cbc","8192","17732.95","31200.60","95939.24"
    "des-cbc","1024","15265.79","9145.69","14665.05"
    "des-cbc","16","2704.53","309.95","3325.90"
    "des-cbc","256","12472.49","3901.18","12611.50"
    "des-cbc","64","7111.25","1177.69","8075.69"
    "des-cbc","8192","16179.20","15076.01","15406.42"
    "des3","1024","6004.39","9068.89","19632.13"
    "des3","16","2070.81","311.21","357.41"
    "des3","256","5564.59","3863.89","5671.77"
    "des3","64","4178.35","1178.84","1420.39"
    "des3","8192","6264.15","14794.75","68455.08"
    "md5","1024","9849.86","13926.40","31398.23"
    "md5","16","507.37","904.77","702.57"
    "md5","256","3597.48","4190.89","10112.43"
    "md5","64","2004.14","3641.66","2724.12"
    "md5","8192","39190.53","56224.43","81169.07"
    "sha1","1024","9832.45","13617.49","22668.97"
    "sha1","16","466.69","824.28","380.92"
    "sha1","256","3727.19","4589.23","5998.42"
    "sha1","64","1804.10","3274.71","1521.77"
    "sha1","8192","38131.03","55863.98","124054.19"
    "sha224","1024","9868.29","13839.02","38274.05"
    "sha224","16","454.87","836.90","670.41"
    "sha224","256","3722.58","4834.56","10387.80"
    "sha224","64","1767.66","3177.83","2658.07"
    "sha224","8192","38688.09","56410.11","174768.13"
    "sha256","1024","10135.55","13758.81","22595.24"
    "sha256","16","466.52","828.92","376.75"
    "sha256","256","3756.63","4192.51","5907.03"
    "sha256","64","1755.97","3153.64","1500.99"
    "sha256","8192","37926.23","55973.21","125610.67"
    "sha384","1024","17457.15","14147.58","21762.73"
    "sha384","16","461.17","768.70","636.22"
    "sha384","256","6393.60","4122.71","8364.03"
    "sha384","64","1856.66","3070.25","2544.04"
    "sha384","8192","36342.44","65672.53","40869.89"
    "sha512","1024","17756.84","14109.01","15704.06"
    "sha512","16","471.67","777.72","363.61"
    "sha512","256","6367.83","4133.46","5263.87"
    "sha512","64","1846.78","3081.15","1450.75"
    "sha512","8192","36055.72","65505.96","37462.02"


|
|

.. csv-table::
    :header: "Algorithm","am335x-evm: CPU Load","am57xx-evm: CPU Load","am654x-evm: CPU Load"

    "aes-128-cbc","51.00","52.00","45.00"
    "aes-192-cbc","51.00","52.00","45.00"
    "aes-256-cbc","50.00","51.00","44.00"
    "des-cbc","98.00","22.00","99.00"
    "des3","98.00","22.00","43.00"
    "md5","76.00","72.00","99.00"
    "sha1","76.00","74.00","99.00"
    "sha224","76.00","77.00","99.00"
    "sha256","77.00","72.00","99.00"
    "sha384","98.00","74.00","99.00"
    "sha512","98.00","74.00","99.00"



-

|
| Listed for each algorithm are the code snippets used to run each
  benchmark test.

|

::

    time -v openssl speed -elapsed -evp aes-128-cbc

-

IPSec Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note: queue\_len is set to 300 and software fallback threshold set to 9
to enable software support for optimal performance

.. csv-table::
    :header: "Algorithm","am335x-evm: Throughput (Mbps)","am335x-evm: Packets/Sec","am335x-evm: CPU Load","am57xx-evm: Throughput (Mbps)","am57xx-evm: Packets/Sec","am57xx-evm: CPU Load","am654x-evm: Throughput (Mbps)","am654x-evm: Packets/Sec","am654x-evm: CPU Load"

    "3des","17.40","1.00","76.10"
    "aes128","14.30","1.00","71.40","121.10","10.00","60.60","186.60","15.00","31.90"
    "aes192","29.10","2.00","81.10","146.40","13.00","62.30"
    "aes256","24.30","2.00","83.10","145.30","12.00","61.50"

-
