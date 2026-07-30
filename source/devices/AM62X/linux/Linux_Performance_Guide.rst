.. include:: <isonum.txt>

#################################
 Linux 12.01.00 Performance Guide
#################################

***************
Read This First
***************

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
| AM62x SK       | AM62x Starter Kit rev E2 and E3 with ARM running at 1.4GHz, DDR data rate 1600 MT/S                            |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM62x LP SK    | AM62x LP Starter Kit rev E1 with ARM running at 1.25GHz, LPDDR4 data rate 1600 MT/S                            |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM62SIP SK     | AM62SIP Starter Kit rev E1 with ARM running at 1.4GHz, 512MB LPDDR4 data rate 1600 MT/S                        |
+----------------+----------------------------------------------------------------------------------------------------------------+

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

System Benchmarks
-------------------

LMBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
LMBench is a collection of microbenchmarks of which the memory bandwidth 
and latency related ones are typically used to estimate processor 
memory system performance. More information about lmbench at
https://lmbench.sourceforge.net/whatis_lmbench.html and
https://lmbench.sourceforge.net/man/lmbench.8.html

**Latency**: :command:`lat_mem_rd-stride128-szN`, where N is equal to or smaller than the cache
size at given level measures the cache miss penalty. N that is at least
double the size of last level cache is the latency to external memory.

**Bandwidth**: :command:`bw_mem_bcopy-N`, where N is equal to or smaller than the cache size at
a given level measures the achievable memory bandwidth from software doing
a memcpy() type operation. Typical use is for external memory bandwidth
calculation. The bandwidth is calculated as byte read and written counts
as 1 which should be roughly half of STREAM copy result.

Execute the LMBench with the following:

.. code-block:: console

    cd /opt/ltp
    ./runltp -P j721e-idk-gw -f ddt/lmbench -s LMBENCH_L_PERF_0001

.. csv-table:: LMBench Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","29.57 (min 24.20, max 38.93)","24.16 (min 21.71, max 28.22)","23.35 (min 21.55, max 25.90)"
    "af_unix_socket_stream_bandwidth (mb\s)","565.72 (min 559.87, max 573.08)","649.39 (min 607.00, max 773.16)","798.02 (min 728.51, max 880.43)"
    "bw_file_rd-io-1mb (mb/s)","838.59 (min 812.08, max 857.34)","973.29 (min 938.26, max 1094.09)","950.24 (min 866.55, max 1055.59)"
    "bw_file_rd-o2c-1mb (mb/s)","436.33 (min 417.36, max 457.11)","519.24 (min 490.76, max 599.52)","517.11 (min 465.48, max 585.05)"
    "bw_mem-bcopy-16mb (mb/s)","678.49 (min 659.33, max 698.45)","783.20 (min 756.97, max 874.41)","809.10 (min 719.78, max 913.09)"
    "bw_mem-bcopy-1mb (mb/s)","728.28 (min 696.26, max 773.04)","854.14 (min 796.94, max 1051.71)","888.95 (min 750.19, max 1019.37)"
    "bw_mem-bcopy-2mb (mb/s)","680.33 (min 659.52, max 697.47)","806.70 (min 764.53, max 961.69)","808.10 (min 707.09, max 915.47)"
    "bw_mem-bcopy-4mb (mb/s)","697.13 (min 660.94, max 721.63)","838.48 (min 792.94, max 994.65)","831.91 (min 730.73, max 937.54)"
    "bw_mem-bcopy-8mb (mb/s)","719.11 (min 702.49, max 747.31)","841.35 (min 794.91, max 1001.13)","797.23 (min 696.20, max 910.33)"
    "bw_mem-bzero-16mb (mb/s)","1731.19 (min 1691.51, max 1776.99)","1823.38 (min 1744.25, max 2125.96)","1938.45 (min 1747.68, max 2128.79)"
    "bw_mem-bzero-1mb (mb/s)","1223.12 (min 696.26, max 1770.54)","1332.59 (min 796.94, max 2121.27)","1408.47 (min 750.19, max 2131.82)"
    "bw_mem-bzero-2mb (mb/s)","1198.76 (min 659.52, max 1766.47)","1309.50 (min 764.53, max 2123.14)","1367.43 (min 707.09, max 2129.55)"
    "bw_mem-bzero-4mb (mb/s)","1208.10 (min 660.94, max 1772.79)","1326.06 (min 792.94, max 2125.78)","1379.47 (min 730.73, max 2130.68)"
    "bw_mem-bzero-8mb (mb/s)","1226.30 (min 702.49, max 1768.35)","1333.53 (min 794.91, max 2125.96)","1364.65 (min 696.20, max 2129.08)"
    "bw_mem-cp-16mb (mb/s)","389.82 (min 363.48, max 404.58)","478.65 (min 449.67, max 574.51)","467.99 (min 426.86, max 520.63)"
    "bw_mem-cp-1mb (mb/s)","1131.50 (min 375.66, max 1923.45)","1221.43 (min 443.59, max 2287.02)","1279.02 (min 391.44, max 2284.41)"
    "bw_mem-cp-2mb (mb/s)","1094.19 (min 378.36, max 1847.06)","1191.73 (min 459.14, max 2206.29)","1228.45 (min 383.88, max 2216.48)"
    "bw_mem-cp-4mb (mb/s)","1087.41 (min 395.73, max 1814.33)","1174.71 (min 445.63, max 2164.89)","1215.70 (min 394.91, max 2172.73)"
    "bw_mem-cp-8mb (mb/s)","1089.76 (min 419.82, max 1804.65)","1180.06 (min 471.84, max 2153.43)","1202.72 (min 382.01, max 2159.54)"
    "bw_mem-fcp-16mb (mb/s)","676.43 (min 654.64, max 692.73)","779.27 (min 741.98, max 906.36)","874.94 (min 780.98, max 964.84)"
    "bw_mem-fcp-1mb (mb/s)","1253.18 (min 768.94, max 1770.54)","1365.50 (min 854.85, max 2121.27)","1425.99 (min 831.39, max 2131.82)"
    "bw_mem-fcp-2mb (mb/s)","1232.01 (min 725.03, max 1766.47)","1348.55 (min 822.26, max 2123.14)","1396.21 (min 784.31, max 2129.55)"
    "bw_mem-fcp-4mb (mb/s)","1246.86 (min 757.00, max 1772.79)","1368.38 (min 856.35, max 2125.78)","1392.59 (min 762.05, max 2130.68)"
    "bw_mem-fcp-8mb (mb/s)","1256.38 (min 757.07, max 1768.35)","1383.76 (min 866.93, max 2125.96)","1409.08 (min 749.84, max 2129.08)"
    "bw_mem-frd-16mb (mb/s)","1019.01 (min 995.71, max 1048.77)","1194.27 (min 1116.15, max 1399.21)","1225.86 (min 1059.32, max 1372.80)"
    "bw_mem-frd-1mb (mb/s)","971.53 (min 768.94, max 1194.74)","1126.42 (min 854.85, max 1619.29)","1149.06 (min 831.39, max 1530.09)"
    "bw_mem-frd-2mb (mb/s)","887.52 (min 725.03, max 1074.11)","1024.84 (min 822.26, max 1315.14)","1042.67 (min 784.31, max 1364.49)"
    "bw_mem-frd-4mb (mb/s)","899.71 (min 757.00, max 1040.18)","1054.69 (min 856.35, max 1389.85)","1036.45 (min 762.05, max 1368.46)"
    "bw_mem-frd-8mb (mb/s)","901.40 (min 757.07, max 1071.52)","1070.59 (min 866.93, max 1400.81)","1057.69 (min 749.84, max 1362.86)"
    "bw_mem-fwr-16mb (mb/s)","1738.92 (min 1687.23, max 1786.91)","1838.42 (min 1753.23, max 2138.47)","1943.18 (min 1740.27, max 2144.48)"
    "bw_mem-fwr-1mb (mb/s)","1512.24 (min 1124.50, max 1923.45)","1646.09 (min 1249.11, max 2287.02)","1738.62 (min 1224.74, max 2284.41)"
    "bw_mem-fwr-2mb (mb/s)","1412.47 (min 974.98, max 1847.06)","1532.25 (min 1108.49, max 2206.29)","1614.24 (min 1103.55, max 2216.48)"
    "bw_mem-fwr-4mb (mb/s)","1396.73 (min 1004.39, max 1814.33)","1522.82 (min 1108.03, max 2164.89)","1594.80 (min 1062.56, max 2172.73)"
    "bw_mem-fwr-8mb (mb/s)","1387.99 (min 963.74, max 1804.65)","1522.89 (min 1136.85, max 2153.43)","1594.79 (min 1094.09, max 2159.54)"
    "bw_mem-rd-16mb (mb/s)","1060.15 (min 1029.47, max 1094.92)","1212.46 (min 1135.56, max 1414.93)","1237.74 (min 1098.07, max 1375.87)"
    "bw_mem-rd-1mb (mb/s)","879.07 (min 552.59, max 1236.31)","1048.17 (min 633.51, max 1643.54)","1061.14 (min 615.29, max 1596.88)"
    "bw_mem-rd-2mb (mb/s)","784.58 (min 479.39, max 1062.32)","924.68 (min 568.59, max 1406.22)","920.77 (min 522.26, max 1391.30)"
    "bw_mem-rd-4mb (mb/s)","806.28 (min 551.80, max 1063.26)","954.73 (min 663.35, max 1397.14)","930.64 (min 541.86, max 1371.27)"
    "bw_mem-rd-8mb (mb/s)","849.43 (min 581.18, max 1081.81)","1005.66 (min 746.48, max 1414.43)","948.84 (min 582.79, max 1375.28)"
    "bw_mem-rdwr-16mb (mb/s)","673.59 (min 644.41, max 691.50)","824.60 (min 741.26, max 983.22)","670.57 (min 585.42, max 757.07)"
    "bw_mem-rdwr-1mb (mb/s)","475.31 (min 375.66, max 571.51)","579.29 (min 443.59, max 806.84)","561.55 (min 391.44, max 760.31)"
    "bw_mem-rdwr-2mb (mb/s)","453.35 (min 378.36, max 569.72)","565.08 (min 459.14, max 842.82)","516.48 (min 383.88, max 625.59)"
    "bw_mem-rdwr-4mb (mb/s)","489.02 (min 395.73, max 596.57)","600.90 (min 445.63, max 855.61)","547.77 (min 394.91, max 729.13)"
    "bw_mem-rdwr-8mb (mb/s)","525.81 (min 419.82, max 641.08)","652.97 (min 471.84, max 957.28)","544.93 (min 382.01, max 711.49)"
    "bw_mem-wr-16mb (mb/s)","681.50 (min 665.03, max 695.50)","849.00 (min 793.85, max 997.07)","684.46 (min 604.69, max 770.27)"
    "bw_mem-wr-1mb (mb/s)","561.36 (min 544.37, max 586.34)","692.44 (min 622.37, max 806.84)","676.57 (min 591.10, max 775.67)"
    "bw_mem-wr-2mb (mb/s)","518.24 (min 468.11, max 591.54)","647.02 (min 557.10, max 842.82)","590.55 (min 522.26, max 664.67)"
    "bw_mem-wr-4mb (mb/s)","570.23 (min 528.40, max 596.57)","713.81 (min 643.81, max 877.67)","628.40 (min 541.86, max 729.13)"
    "bw_mem-wr-8mb (mb/s)","634.94 (min 581.18, max 675.22)","801.24 (min 732.60, max 995.02)","651.37 (min 580.13, max 745.09)"
    "bw_mmap_rd-mo-1mb (mb/s)","1168.52 (min 1097.49, max 1196.17)","1330.90 (min 1244.89, max 1590.11)","1410.40 (min 1243.34, max 1566.85)"
    "bw_mmap_rd-o2c-1mb (mb/s)","432.68 (min 412.54, max 453.93)","414.28 (min 86.08, max 509.34)","502.94 (min 465.19, max 533.33)"
    "bw_pipe (mb/s)","472.29 (min 455.78, max 485.39)","547.80 (min 519.83, max 643.11)","558.58 (min 515.54, max 600.98)"
    "bw_unix (mb/s)","565.72 (min 559.87, max 573.08)","649.39 (min 607.00, max 773.16)","798.02 (min 728.51, max 880.43)"
    "lat_connect (us)","87.53 (min 86.81, max 87.98)","77.15 (min 73.87, max 79.04)","75.23 (min 72.83, max 77.80)"
    "lat_ctx-2-128k (us)","10.80 (min 8.75, max 15.57)","9.19 (min 6.08, max 11.11)","8.83 (min 7.27, max 10.59)"
    "lat_ctx-2-256k (us)","67.64 (min 9.37, max 89.50)","65.35 (min 45.72, max 76.64)","32.90 (min 6.04, max 68.50)"
    "lat_ctx-4-128k (us)","44.19 (min 10.83, max 55.51)","45.31 (min 29.02, max 53.09)","30.76 (min 7.57, max 43.89)"
    "lat_ctx-4-256k (us)","129.12 (min 8.02, max 225.53)","106.55 (min 6.56, max 188.07)","89.46 (min 6.26, max 193.75)"
    "lat_fs-0k (num_files)","204.40 (min 176.00, max 237.00)","235.00 (min 202.00, max 269.00)","241.50 (min 225.00, max 252.00)"
    "lat_fs-10k (num_files)","91.00 (min 80.00, max 107.00)","105.40 (min 100.00, max 116.00)","110.50 (min 90.00, max 124.00)"
    "lat_fs-1k (num_files)","133.20 (min 129.00, max 139.00)","150.60 (min 131.00, max 165.00)","148.00 (min 135.00, max 160.00)"
    "lat_fs-4k (num_files)","130.40 (min 128.00, max 134.00)","159.60 (min 143.00, max 181.00)","152.00 (min 128.00, max 177.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","55.99 (min 54.43, max 57.48)","49.14 (min 41.49, max 51.38)","47.25 (min 42.86, max 52.83)"
    "lat_mem_rd-stride128-sz125k (ns)","6.23 (min 6.20, max 6.25)","5.56 (min 5.54, max 5.57)","5.55 (min 5.55, max 5.56)"
    "lat_mem_rd-stride128-sz250k (ns)","6.89 (min 6.53, max 8.26)","5.84 (min 5.83, max 5.85)","5.84 (min 5.84, max 5.85)"
    "lat_mem_rd-stride128-sz31k (ns)","3.21 (min 2.42, max 4.70)","2.87 (min 2.16, max 4.19)","3.04 (min 2.16, max 4.19)"
    "lat_mem_rd-stride128-sz50 (ns)","2.40","2.15","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","17.91 (min 8.76, max 23.11)","17.40 (min 15.25, max 21.36)","14.62 (min 10.63, max 16.61)"
    "lat_mem_rd-stride128-sz62k (ns)","5.87 (min 5.86, max 5.89)","5.24 (min 5.23, max 5.25)","5.26 (min 5.24, max 5.30)"
    "lat_mmap-1m (us)","70.00 (min 69.00, max 72.00)","56.40 (min 50.00, max 65.00)","52.25 (min 43.00, max 58.00)"
    "lat_ops-double-add (ns)","3.21 (min 3.21, max 3.23)","2.86 (min 2.86, max 2.87)","2.86 (min 2.86, max 2.87)"
    "lat_ops-double-div (ns)","17.64 (min 17.63, max 17.66)","15.74","15.74"
    "lat_ops-double-mul (ns)","3.21 (min 3.20, max 3.23)","2.86","2.86 (min 2.86, max 2.87)"
    "lat_ops-float-add (ns)","3.21","2.86","2.87 (min 2.86, max 2.89)"
    "lat_ops-float-div (ns)","10.42 (min 10.42, max 10.43)","9.31 (min 9.30, max 9.31)","9.31 (min 9.30, max 9.31)"
    "lat_ops-float-mul (ns)","3.21","2.86","2.86 (min 2.86, max 2.87)"
    "lat_ops-int-add (ns)","0.80","0.72","0.72"
    "lat_ops-int-bit (ns)","0.53","0.48","0.48"
    "lat_ops-int-div (ns)","4.81 (min 4.81, max 4.82)","4.30 (min 4.29, max 4.30)","4.30 (min 4.29, max 4.30)"
    "lat_ops-int-mod (ns)","5.08 (min 5.08, max 5.09)","4.53","4.54 (min 4.53, max 4.54)"
    "lat_ops-int-mul (ns)","3.44 (min 3.41, max 3.50)","3.08 (min 3.04, max 3.12)","3.07 (min 3.04, max 3.12)"
    "lat_ops-int64-add (ns)","0.80","0.72","0.72"
    "lat_ops-int64-bit (ns)","0.53 (min 0.53, max 0.54)","0.48","0.48"
    "lat_ops-int64-div (ns)","7.62 (min 7.61, max 7.62)","6.80 (min 6.80, max 6.81)","6.80"
    "lat_ops-int64-mod (ns)","5.88","5.25","5.25"
    "lat_ops-int64-mul (ns)","3.97 (min 3.97, max 3.98)","3.54","3.54 (min 3.54, max 3.55)"
    "lat_pagefault (us)","0.67 (min 0.60, max 0.69)","0.59 (min 0.52, max 0.62)","1.48 (min 1.00, max 1.82)"
    "lat_pipe (us)","21.78 (min 19.83, max 24.42)","19.51 (min 17.87, max 21.93)","18.82 (min 17.57, max 21.46)"
    "lat_proc-exec (us)","1123.52 (min 1074.00, max 1157.80)","975.70 (min 834.00, max 1034.00)","952.81 (min 862.86, max 1041.00)"
    "lat_proc-fork (us)","970.12 (min 929.17, max 999.60)","834.79 (min 718.88, max 890.71)","803.21 (min 728.29, max 901.83)"
    "lat_proc-proccall (us)","0.01","0.01","0.01"
    "lat_select (us)","36.82 (min 35.29, max 41.62)","32.96 (min 31.50, max 37.56)","33.12 (min 31.51, max 37.29)"
    "lat_sem (us)","2.82 (min 2.65, max 3.12)","2.39 (min 2.18, max 2.68)","2.48 (min 2.29, max 2.63)"
    "lat_sig-catch (us)","6.34 (min 6.20, max 6.47)","5.68 (min 5.55, max 5.76)","5.68 (min 5.55, max 5.76)"
    "lat_sig-install (us)","0.68 (min 0.68, max 0.69)","0.61 (min 0.61, max 0.62)","0.61 (min 0.61, max 0.62)"
    "lat_sig-prot (us)","0.91 (min 0.80, max 1.03)","1.01 (min 0.72, max 1.71)","0.82 (min 0.68, max 0.97)"
    "lat_syscall-fstat (us)","2.01 (min 1.97, max 2.10)","1.80 (min 1.75, max 1.87)","1.82 (min 1.79, max 1.88)"
    "lat_syscall-null (us)","0.43 (min 0.41, max 0.45)","0.39 (min 0.37, max 0.41)","0.38 (min 0.37, max 0.41)"
    "lat_syscall-open (us)","244.20 (min 167.97, max 345.41)","188.71 (min 165.50, max 201.89)","853.68 (min 169.52, max 2849.38)"
    "lat_syscall-read (us)","0.80 (min 0.80, max 0.81)","0.72 (min 0.71, max 0.72)","0.71 (min 0.71, max 0.72)"
    "lat_syscall-stat (us)","4.84 (min 4.72, max 4.92)","4.28 (min 4.16, max 4.34)","4.30 (min 4.18, max 4.38)"
    "lat_syscall-write (us)","0.75 (min 0.75, max 0.76)","0.67 (min 0.67, max 0.68)","0.67"
    "lat_tcp (us)","0.85","0.76","0.76"
    "lat_unix (us)","29.57 (min 24.20, max 38.93)","24.16 (min 21.71, max 28.22)","23.35 (min 21.55, max 25.90)"
    "latency_for_0.50_mb_block_size (nanosec)","17.91 (min 8.76, max 23.11)","17.40 (min 15.25, max 21.36)","14.62 (min 10.63, max 16.61)"
    "latency_for_1.00_mb_block_size (nanosec)","28.00 (min 0.00, max 57.48)","24.57 (min 0.00, max 51.38)","23.62 (min 0.00, max 52.83)"
    "pipe_bandwidth (mb\s)","472.29 (min 455.78, max 485.39)","547.80 (min 519.83, max 643.11)","558.58 (min 515.54, max 600.98)"
    "pipe_latency (microsec)","21.78 (min 19.83, max 24.42)","19.51 (min 17.87, max 21.93)","18.82 (min 17.57, max 21.46)"
    "procedure_call (microsec)","0.01","0.01","0.01"
    "select_on_200_tcp_fds (microsec)","36.82 (min 35.29, max 41.62)","32.96 (min 31.50, max 37.56)","33.12 (min 31.51, max 37.29)"
    "semaphore_latency (microsec)","2.82 (min 2.65, max 3.12)","2.39 (min 2.18, max 2.68)","2.48 (min 2.29, max 2.63)"
    "signal_handler_latency (microsec)","0.68 (min 0.68, max 0.69)","0.61 (min 0.61, max 0.62)","0.61 (min 0.61, max 0.62)"
    "signal_handler_overhead (microsec)","6.34 (min 6.20, max 6.47)","5.68 (min 5.55, max 5.76)","5.68 (min 5.55, max 5.76)"
    "tcp_ip_connection_cost_to_localhost (microsec)","87.53 (min 86.81, max 87.98)","77.15 (min 73.87, max 79.04)","75.23 (min 72.83, max 77.80)"
    "tcp_latency_using_localhost (microsec)","0.85","0.76","0.76"



Dhrystone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed.

Please take note, different run may produce different slightly results.
This is advised to run this test multiple times in order to get maximum 
performance numbers.


Execute the benchmark with the following:

.. code-block:: console

    runDhrystone

.. csv-table:: Dhrystone Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cpu_clock (mhz)","1250.00","1400.00","1400.00"
    "dhrystone_per_mhz (dmips/mhz)","2.80","2.78 (min 2.70, max 2.80)","2.76 (min 2.70, max 2.80)"
    "dhrystone_per_second (dhrystonep)","6174242.40 (min 6060606.00, max 6250000.00)","6850574.50 (min 6666666.50, max 6896551.50)","6804597.50 (min 6666666.50, max 6896551.50)"


Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

.. code-block:: console

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "whetstone (mips)","5000.00","5000.00","5000.00"


Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "linpack (kflops)","516580.00 (min 515013.00, max 517497.00)","581301.00 (min 580494.00, max 582513.00)","580159.75 (min 576304.00, max 582266.00)"


NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "assignment (iterations)","12.63 (min 12.62, max 12.67)","14.15 (min 14.13, max 14.16)","14.14 (min 14.12, max 14.15)"
    "fourier (iterations)","17304.20 (min 17291.00, max 17322.00)","19382.40 (min 19371.00, max 19400.00)","19378.00 (min 19371.00, max 19399.00)"
    "fp_emulation (iterations)","182.49 (min 182.46, max 182.52)","204.40 (min 204.39, max 204.43)","204.42 (min 204.40, max 204.44)"
    "huffman (iterations)","1061.68 (min 1060.70, max 1063.30)","1189.34 (min 1188.40, max 1190.90)","1188.88 (min 1187.80, max 1190.90)"
    "idea (iterations)","2740.28 (min 2738.50, max 2741.60)","3069.32 (min 3067.20, max 3070.70)","3069.83 (min 3067.30, max 3070.70)"
    "lu_decomposition (iterations)","475.31 (min 474.24, max 476.40)","531.00 (min 527.52, max 532.97)","532.77 (min 531.96, max 534.42)"
    "neural_net (iterations)","8.64 (min 8.63, max 8.64)","9.67 (min 9.67, max 9.68)","9.68 (min 9.67, max 9.68)"
    "numeric_sort (iterations)","483.77 (min 482.68, max 485.44)","540.92 (min 537.53, max 543.25)","540.68 (min 538.21, max 544.78)"
    "string_sort (iterations)","147.70 (min 146.05, max 150.16)","165.44 (min 163.60, max 168.19)","164.73 (min 163.51, max 168.19)"


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

.. code-block:: console

    stream_c

.. csv-table:: Stream Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf"

    "add (mb/s)","1393.88 (min 1367.60, max 1413.80)","1467.42 (min 1462.40, max 1472.40)"
    "copy (mb/s)","1492.60 (min 1467.10, max 1516.10)","1673.08 (min 1663.80, max 1679.80)"
    "scale (mb/s)","1598.40 (min 1559.60, max 1632.00)","1801.42 (min 1788.30, max 1812.00)"
    "triad (mb/s)","1368.36 (min 1343.50, max 1385.60)","1503.06 (min 1498.50, max 1507.30)"



CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark\ |reg|-Pro is a comprehensive, advanced processor benchmark that works
with and enhances the market-proven industry-standard EEMBC CoreMark\ |reg|
benchmark. While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the
entire processor, adding comprehensive support for multicore technology, a
combination of integer and floating-point workloads, and data sets for utilizing
larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","37.15 (min 37.04, max 37.17)","41.56 (min 41.49, max 41.67)","41.84 (min 41.67, max 42.02)"
    "core (workloads/)","0.27","0.30","0.30"
    "coremark-pro ()","809.71 (min 808.32, max 811.10)","908.96 (min 905.75, max 913.00)","906.04 (min 891.25, max 927.33)"
    "linear_alg-mid-100x100-sp (workloads/)","13.09 (min 13.09, max 13.10)","14.67 (min 14.66, max 14.67)","14.67 (min 14.67, max 14.68)"
    "loops-all-mid-10k-sp (workloads/)","0.60 (min 0.59, max 0.60)","0.67","0.68 (min 0.67, max 0.70)"
    "nnet_test (workloads/)","0.96","1.08","1.08"
    "parser-125k (workloads/)","7.86 (min 7.75, max 7.94)","8.82 (min 8.77, max 8.85)","8.87 (min 8.70, max 9.01)"
    "radix2-big-64k (workloads/)","51.83 (min 51.42, max 52.28)","59.31 (min 58.11, max 60.53)","55.57 (min 48.79, max 64.46)"
    "sha-test (workloads/)","70.82 (min 70.42, max 71.43)","79.37 (min 78.74, max 80.00)","80.65 (min 80.00, max 81.30)"
    "zip-test (workloads/)","19.61","21.84 (min 21.74, max 22.22)","21.63 (min 21.28, max 22.22)"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","72.57 (min 72.46, max 72.99)","81.57 (min 81.30, max 81.97)","82.82 (min 82.64, max 83.33)"
    "core (workloads/)","0.54","0.60","0.60"
    "coremark-pro ()","1356.24 (min 1344.91, max 1364.68)","1528.63 (min 1508.62, max 1591.34)","1573.34 (min 1520.26, max 1606.96)"
    "linear_alg-mid-100x100-sp (workloads/)","26.14 (min 26.12, max 26.15)","29.28 (min 29.27, max 29.29)","29.33 (min 29.33, max 29.36)"
    "loops-all-mid-10k-sp (workloads/)","1.04 (min 1.02, max 1.06)","1.17 (min 1.14, max 1.25)","1.22 (min 1.14, max 1.26)"
    "nnet_test (workloads/)","1.92","2.15","2.15 (min 2.14, max 2.15)"
    "parser-125k (workloads/)","13.26 (min 13.07, max 13.42)","14.94 (min 14.60, max 15.87)","14.08 (min 13.51, max 14.81)"
    "radix2-big-64k (workloads/)","32.39 (min 31.11, max 33.38)","37.81 (min 35.70, max 45.37)","47.12 (min 39.36, max 52.00)"
    "sha-test (workloads/)","138.13 (min 136.99, max 138.89)","154.33 (min 153.85, max 156.25)","160.65 (min 158.73, max 161.29)"
    "zip-test (workloads/)","36.24 (min 35.71, max 37.04)","41.16 (min 40.82, max 42.55)","41.25 (min 40.00, max 41.67)"

MultiBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
MultiBench\ |trade| is a suite of benchmarks that allows processor and system
designers to analyze, test, and improve multicore processors. It uses three
forms of concurrency: Data decomposition: multiple threads cooperating on
achieving a unified goal and demonstrating a processor's support for fine grain
parallelism.
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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "4m-check (workloads/)","278.63 (min 274.21, max 290.19)","315.60 (min 312.77, max 317.66)","326.47 (min 303.77, max 370.92)"
    "4m-check-reassembly (workloads/)","76.67 (min 75.02, max 80.06)","84.27 (min 83.61, max 84.60)","85.64 (min 76.86, max 101.94)"
    "4m-check-reassembly-tcp (workloads/)","44.40 (min 43.71, max 46.04)","49.38 (min 49.02, max 49.70)","50.38 (min 46.73, max 55.19)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","22.26 (min 21.94, max 23.18)","24.92 (min 24.79, max 25.08)","25.38 (min 23.72, max 28.42)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.56 (min 1.50, max 1.59)","1.76 (min 1.75, max 1.77)","1.70 (min 1.58, max 1.77)"
    "4m-cmykw2 (workloads/)","177.96 (min 174.67, max 184.16)","199.87 (min 199.60, max 200.40)","208.82 (min 195.89, max 233.92)"
    "4m-cmykw2-rotatew2 (workloads/)","34.54 (min 33.48, max 35.78)","39.04 (min 38.59, max 39.63)","40.05 (min 37.22, max 45.05)"
    "4m-reassembly (workloads/)","73.72 (min 72.73, max 76.39)","83.01 (min 82.92, max 83.13)","85.78 (min 78.62, max 99.60)"
    "4m-rotatew2 (workloads/)","40.41 (min 39.89, max 41.77)","45.48 (min 45.07, max 45.79)","46.18 (min 43.08, max 51.89)"
    "4m-tcp-mixed (workloads/)","97.11 (min 95.24, max 98.77)","108.62 (min 106.67, max 110.35)","113.43 (min 108.11, max 120.30)"
    "4m-x264w2 (workloads/)","1.63 (min 1.59, max 1.65)","1.82 (min 1.77, max 1.86)","1.81 (min 1.75, max 1.86)"
    "empty-wld (workloads/)","1.00","1.00","1.00"
    "idct-4m (workloads/)","17.58 (min 17.58, max 17.59)","19.68 (min 19.66, max 19.70)","19.64 (min 19.62, max 19.69)"
    "idct-4mw1 (workloads/)","17.58 (min 17.57, max 17.59)","19.70 (min 19.69, max 19.71)","19.63 (min 19.60, max 19.68)"
    "ippktcheck-4m (workloads/)","277.24 (min 273.49, max 290.23)","314.84 (min 313.05, max 316.42)","329.22 (min 307.58, max 372.41)"
    "ippktcheck-4mw1 (workloads/)","278.67 (min 274.64, max 290.70)","313.46 (min 311.49, max 315.98)","326.68 (min 304.80, max 370.21)"
    "ipres-4m (workloads/)","59.05 (min 58.05, max 61.53)","65.48 (min 64.99, max 66.08)","67.53 (min 62.68, max 77.08)"
    "ipres-4mw1 (workloads/)","59.02 (min 57.83, max 61.32)","65.26 (min 64.60, max 65.67)","68.06 (min 63.10, max 77.76)"
    "md5-4m (workloads/)","22.16 (min 21.94, max 22.30)","24.81 (min 24.68, max 24.98)","25.17 (min 24.67, max 26.16)"
    "md5-4mw1 (workloads/)","22.03 (min 21.97, max 22.09)","24.70 (min 24.57, max 24.92)","24.88 (min 24.37, max 25.90)"
    "rgbcmyk-4m (workloads/)","57.16 (min 56.83, max 57.64)","64.19 (min 64.02, max 64.45)","63.90 (min 63.41, max 64.81)"
    "rgbcmyk-4mw1 (workloads/)","57.04 (min 56.88, max 57.31)","64.10 (min 64.04, max 64.16)","63.91 (min 63.39, max 64.85)"
    "rotate-4ms1 (workloads/)","17.82 (min 17.64, max 18.46)","19.99 (min 19.97, max 20.02)","19.34 (min 18.18, max 21.66)"
    "rotate-4ms1w1 (workloads/)","17.80 (min 17.60, max 18.41)","20.01 (min 20.00, max 20.02)","19.34 (min 18.13, max 21.63)"
    "rotate-4ms64 (workloads/)","17.96 (min 17.78, max 18.62)","20.13 (min 20.12, max 20.15)","19.51 (min 18.29, max 21.78)"
    "rotate-4ms64w1 (workloads/)","17.94 (min 17.76, max 18.62)","20.12 (min 20.10, max 20.14)","19.50 (min 18.29, max 21.74)"
    "x264-4mq (workloads/)","0.49 (min 0.46, max 0.50)","0.56","0.56 (min 0.55, max 0.57)"
    "x264-4mqw1 (workloads/)","0.50 (min 0.49, max 0.50)","0.56","0.56 (min 0.55, max 0.57)"
 


Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62xx_lp_sk-fs: Boot time in seconds: avg(min,max)","am62xx_sk-fs: Boot time in seconds: avg(min,max)","am62xxsip_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","19.07 (min 18.25, max 20.87)","18.30 (min 17.61, max 19.35)","17.91 (min 17.37, max 18.54)"

 
Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.
 

|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)","am62xxsip_sk-fs: Throughput (bits/sec)","am62xxsip_sk-fs: CPU Load (%)"

    "11025","352798.20 (min 352797.00, max 352800.00)","0.23 (min 0.20, max 0.28)","352799.00 (min 352798.00, max 352800.00)","0.18 (min 0.15, max 0.21)","352798.00","0.31 (min 0.23, max 0.39)"
    "16000","511998.60 (min 511998.00, max 512001.00)","0.19 (min 0.14, max 0.36)","511999.60 (min 511997.00, max 512001.00)","0.14 (min 0.12, max 0.15)","511998.67 (min 511997.00, max 512000.00)","0.28 (min 0.18, max 0.34)"
    "22050","705589.80 (min 705582.00, max 705593.00)","0.20 (min 0.19, max 0.21)","705595.00 (min 705593.00, max 705596.00)","0.19 (min 0.17, max 0.22)","705593.00 (min 705592.00, max 705594.00)","0.31 (min 0.24, max 0.36)"
    "24000","705595.00 (min 705593.00, max 705596.00)","0.21 (min 0.20, max 0.23)","705597.80 (min 705595.00, max 705599.00)","0.19 (min 0.17, max 0.21)","705596.00 (min 705594.00, max 705597.00)","0.33 (min 0.23, max 0.41)"
    "32000","1023993.80 (min 1023993.00, max 1023994.00)","0.14 (min 0.11, max 0.17)","1023997.80 (min 1023994.00, max 1024000.00)","0.12 (min 0.08, max 0.15)","1023995.67 (min 1023993.00, max 1023997.00)","0.28 (min 0.20, max 0.32)"
    "44100","1411191.80 (min 1411191.00, max 1411193.00)","0.30 (min 0.28, max 0.33)","1411196.00 (min 1411190.00, max 1411200.00)","0.29 (min 0.27, max 0.31)","1411193.67 (min 1411189.00, max 1411196.00)","0.42 (min 0.32, max 0.47)"
    "48000","1535991.20 (min 1535990.00, max 1535992.00)","0.30 (min 0.16, max 0.81)","1535996.00 (min 1535990.00, max 1536000.00)","0.16 (min 0.12, max 0.21)","1535993.33 (min 1535989.00, max 1535996.00)","0.28 (min 0.19, max 0.33)"
    "88200","2822379.40 (min 2822377.00, max 2822382.00)","0.48 (min 0.45, max 0.51)","2822386.60 (min 2822369.00, max 2822394.00)","0.45 (min 0.40, max 0.51)","2822375.67 (min 2822364.00, max 2822388.00)","0.58 (min 0.51, max 0.67)"
    "96000","3071955.00 (min 3071946.00, max 3071975.00)","0.55 (min 0.15, max 1.33)","3071967.00 (min 3071960.00, max 3071975.00)","0.18 (min 0.14, max 0.22)","3071958.67 (min 3071955.00, max 3071963.00)","0.65 (min 0.24, max 1.35)"



.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)","am62xxsip_sk-fs: Throughput (bits/sec)","am62xxsip_sk-fs: CPU Load (%)"

    "11025","352944.80 (min 352944.00, max 352945.00)","0.21 (min 0.16, max 0.29)","352946.40 (min 352946.00, max 352947.00)","0.22 (min 0.09, max 0.54)","352946.00 (min 352945.00, max 352947.00)","0.18 (min 0.16, max 0.19)"
    "16000","512212.00 (min 512211.00, max 512213.00)","0.16 (min 0.14, max 0.18)","512213.20 (min 512212.00, max 512214.00)","0.13 (min 0.11, max 0.15)","512214.67 (min 512214.00, max 512215.00)","0.14"
    "22050","705887.20 (min 705886.00, max 705888.00)","0.17 (min 0.14, max 0.19)","705888.80 (min 705886.00, max 705892.00)","0.13 (min 0.11, max 0.15)","705889.33 (min 705885.00, max 705897.00)","0.15 (min 0.15, max 0.16)"
    "24000","705890.20 (min 705889.00, max 705891.00)","0.19 (min 0.16, max 0.21)","705892.00 (min 705890.00, max 705893.00)","0.15 (min 0.12, max 0.17)","705893.33 (min 705891.00, max 705897.00)","0.16 (min 0.14, max 0.17)"
    "32000","1024421.80 (min 1024420.00, max 1024423.00)","0.24 (min 0.12, max 0.63)","1024424.80 (min 1024422.00, max 1024426.00)","0.12 (min 0.09, max 0.14)","1024427.33 (min 1024424.00, max 1024431.00)","0.13 (min 0.11, max 0.15)"
    "44100","1411781.80 (min 1411779.00, max 1411783.00)","0.25 (min 0.23, max 0.27)","1411785.20 (min 1411781.00, max 1411787.00)","0.21 (min 0.18, max 0.24)","1411789.00 (min 1411785.00, max 1411793.00)","0.21 (min 0.19, max 0.22)"
    "48000","1536633.20 (min 1536630.00, max 1536635.00)","0.17 (min 0.10, max 0.21)","1536636.40 (min 1536633.00, max 1536640.00)","0.20 (min 0.11, max 0.47)","1536641.33 (min 1536637.00, max 1536645.00)","0.26 (min 0.13, max 0.50)"
    "88200","2823556.20 (min 2823550.00, max 2823563.00)","0.34 (min 0.33, max 0.35)","2823564.00 (min 2823552.00, max 2823571.00)","0.28 (min 0.22, max 0.33)","2823545.33 (min 2823493.00, max 2823575.00)","0.28 (min 0.24, max 0.32)"
    "96000","3073242.80 (min 3073236.00, max 3073253.00)","0.40 (min 0.16, max 0.73)","3073254.80 (min 3073244.00, max 3073271.00)","0.19 (min 0.16, max 0.25)","3073222.67 (min 3073199.00, max 3073236.00)","0.38 (min 0.21, max 0.51)"


|

Graphics SGX/RGX Driver
-------------------------
 


GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_lp_sk-fs: Fps","am62xx_sk-fs: Score","am62xx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","81.49 (min 80.21, max 82.24)","1.31 (min 1.29, max 1.33)"
    " GFXBench 3.x gl_trex_off","124.27 (min 123.06, max 126.55)","2.22 (min 2.20, max 2.26)"
    " GFXBench 5.x gl_5_high_off","11.27 (min 11.14, max 11.46)","0.18 (min 0.17, max 0.18)","11.57 (min 11.43, max 11.93)","0.18 (min 0.18, max 0.19)"


Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_sk-fs: Score","am62xxsip_sk-fs: Score"

    "Glmark2-DRM","60.00 (min 51.00, max 69.00)","61.00","54.00"
    "Glmark2-Wayland","202.60 (min 198.00, max 206.00)","215.20 (min 215.00, max 216.00)","208.00 (min 207.00, max 209.00)"
    "Glmark2-Wayland 1920x1080","64.00 (min 62.00, max 67.00)","66.60 (min 66.00, max 67.00)"



Ethernet
--------

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

The following commands were used to tune the socket buffer sizes on the DUT before running the performance tests:

.. code-block:: console

   sysctl -w net.core.rmem_default=33554432
   sysctl -w net.core.rmem_max=67108864

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- CPSW3g: AM62x

TCP Bidirectional Throughput
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1657.01","67.11","1822.62","66.72","1763.18","67.48"

TCP Bidirectional Throughput Interrupt Pacing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1794.07","63.53","1828.80","57.91","1543.11","49.30"

UDP Throughput
~~~~~~~~~~~~~~

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)", "am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)", "am62xx_lp_sk-fs: Packets Per Second (kPPS)", "am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)", "am62xx_sk-fs: THROUGHPUT (Mbits/sec)", "am62xx_sk-fs: Packets Per Second (kPPS)", "am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)", "am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)", "am62xxsip_sk-fs: Packets Per Second (kPPS)", "am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","38.61","75","36.53","44.13","86","37.14","45.71","89","37.74"
    "128","76.11","74","36.58","85.34","83","36.72","91.47","89","37.33"
    "256","148.89","73","36.41","169.41","83","36.51","170.76","83","36.89"
    "1024","592.94","72","36.75","659.08","80","36.45","704.41","86","37.13"
    "1518","846.54","72","36.56","208.42","18","11.87","916.55","78","39.59"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)", "am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)", "am62xx_lp_sk-fs: Packets Per Second (kPPS)", "am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)", "am62xx_sk-fs: THROUGHPUT (Mbits/sec)", "am62xx_sk-fs: Packets Per Second (kPPS)", "am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)", "am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)", "am62xxsip_sk-fs: Packets Per Second (kPPS)", "am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","33.53","65","15.91","41.16","80","19.91","30.41","59","12.23"
    "128","63.90","62","15.10","66.05","65","15.68","61.95","60","14.96"
    "256","170.41","83","26.12","148.27","72","18.20","142.13","69","13.55"
    "1024","611.97","75","26.40","754.92","92","31.48","681.07","83","41.67"
    "1518","954.54","81","39.92","956.88","81","38.55","710.47","60","31.15"

|

Linux OSPI Flash Driver
-------------------------


.. rubric:: AM62XX-SK
   :name: am62xx-sk-ospi-flash-driver


.. rubric:: UBIFS
   :name: am62xx-sk-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62xx_sk-fs: Write UBIFS CPU Load (%)","am62xx_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62xx_sk-fs: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.27)","27.87 (min 24.82, max 30.31)","63.18 (min 63.12, max 63.23)","25.00 (min 21.43, max 28.57)"
    "262144","0.13 (min 0.10, max 0.17)","29.15 (min 26.40, max 32.72)","61.33 (min 61.19, max 61.47)","15.38"
    "524288","0.13 (min 0.09, max 0.18)","28.75 (min 26.95, max 31.59)","60.81 (min 60.68, max 60.94)","11.86 (min 8.33, max 15.38)"
    "1048576","0.14 (min 0.10, max 0.18)","28.05 (min 25.85, max 29.86)","59.35 (min 59.01, max 59.69)","18.41 (min 15.38, max 21.43)"




.. rubric:: UBIFS
   :name: am62xx-sk-lp-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write UBIFS CPU Load (%)","am62xx_lp_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read UBIFS CPU Load (%)"

    "102400","7.09 (min 6.74, max 7.40)","15.52 (min 13.76, max 18.42)","16.29 (min 16.08, max 16.49)","16.29 (min 14.58, max 18.00)"
    "262144","7.07 (min 6.67, max 7.48)","14.92 (min 13.89, max 15.70)","16.22 (min 15.95, max 16.49)","15.45 (min 14.89, max 16.00)"
    "524288","7.08 (min 6.63, max 7.58)","14.56 (min 12.50, max 16.67)","16.10 (min 15.91, max 16.29)","17.83 (min 17.65, max 18.00)"
    "1048576","6.99 (min 6.34, max 7.56)","15.04 (min 12.28, max 17.12)","15.89 (min 15.75, max 16.03)","16.66 (min 16.00, max 17.31)"



.. rubric:: RAW
   :name: am62xx-sk-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xx_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","180.35 (min 166.67, max 192.31)"




.. rubric:: RAW
   :name: am62xx-sk-lp-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xx_lp_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","30.20 (min 27.47, max 31.85)"



.. rubric:: RAW
   :name: am62xx-sk-sip-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xxsip_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","120.95 (min 104.17, max 135.13)"



EMMC Driver
-----------
.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.



EMMC EXT4 FIO 1G
^^^^^^^^^^^^^^^^


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","62.80 (min 44.40, max 92.40)","1.64 (min 1.22, max 2.32)","174.40 (min 173.00, max 175.00)","2.06 (min 1.88, max 2.38)"
    "4m","62.44 (min 44.80, max 90.50)","1.25 (min 0.98, max 1.70)","174.20 (min 172.00, max 175.00)","1.69 (min 1.55, max 1.86)"
    "4k","43.13 (min 5.26, max 62.20)","13.39 (min 2.01, max 20.77)","59.52 (min 36.40, max 93.20)","14.50 (min 8.98, max 21.95)"
    "256k","60.60 (min 35.30, max 91.00)","2.08 (min 1.39, max 2.86)","173.80 (min 173.00, max 174.00)","2.86 (min 2.79, max 2.95)"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","59.16 (min 57.90, max 61.70)","1.91 (min 1.70, max 2.04)","175.00","2.50 (min 2.14, max 2.62)"
    "4m","58.96 (min 58.00, max 61.90)","1.36 (min 1.29, max 1.48)","175.00","1.87 (min 1.80, max 1.93)"
    "4k","51.16 (min 50.70, max 51.80)","17.46 (min 16.87, max 18.27)","56.22 (min 56.00, max 56.80)","15.65 (min 15.36, max 16.17)"
    "256k","59.04 (min 57.90, max 61.80)","2.30 (min 2.07, max 2.49)","174.00","3.24 (min 3.05, max 3.33)"



.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "1m","90.75 (min 89.20, max 91.90)","2.60 (min 2.44, max 2.82)","172.00 (min 171.00, max 173.00)","2.55 (min 2.37, max 2.89)"
    "4m","96.68 (min 95.80, max 97.80)","2.43 (min 2.25, max 2.66)","159.25 (min 148.00, max 172.00)","2.38 (min 2.04, max 2.57)"
    "4k","61.68 (min 59.30, max 63.40)","19.49 (min 18.56, max 20.94)","91.75 (min 89.40, max 93.10)","21.02 (min 20.15, max 22.35)"
    "256k","91.70 (min 90.60, max 92.90)","2.70 (min 2.58, max 2.77)","170.25 (min 170.00, max 171.00)","2.67 (min 2.63, max 2.71)"

 


EMMC EXT4
^^^^^^^^^


.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","65.94 (min 51.95, max 88.01)","4.53 (min 3.10, max 7.48)","177.81 (min 173.94, max 180.71)","8.94 (min 8.37, max 9.70)"
    "262144","61.26 (min 47.20, max 86.51)","3.34 (min 2.36, max 5.73)","182.03 (min 180.56, max 183.07)","9.52 (min 9.09, max 10.04)"
    "524288","62.23 (min 48.33, max 86.64)","3.50 (min 2.53, max 5.69)","182.22 (min 180.76, max 183.00)","9.81 (min 9.13, max 10.62)"
    "1048576","63.42 (min 48.76, max 87.45)","3.47 (min 2.33, max 6.42)","182.27 (min 181.03, max 183.07)","9.71 (min 8.85, max 10.53)"
    "5242880","60.51 (min 46.65, max 88.29)","3.31 (min 2.34, max 5.93)","181.58 (min 178.71, max 183.02)","10.96 (min 10.53, max 11.64)"

 


.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "102400","46.63 (min 40.28, max 53.71)","3.66 (min 2.75, max 5.76)","178.68 (min 171.41, max 180.59)","9.93 (min 9.13, max 11.11)"
    "262144","47.15 (min 40.60, max 54.89)","2.89 (min 2.07, max 4.16)","182.82 (min 182.62, max 183.02)","10.31 (min 8.89, max 10.96)"
    "524288","47.15 (min 40.81, max 54.55)","2.99 (min 2.27, max 4.53)","182.78 (min 182.62, max 183.02)","11.41 (min 10.13, max 12.72)"
    "1048576","47.29 (min 40.74, max 56.19)","2.91 (min 2.08, max 4.82)","182.80 (min 182.55, max 182.94)","10.99 (min 9.82, max 11.89)"
    "5242880","47.40 (min 40.94, max 56.18)","2.91 (min 2.18, max 4.29)","182.62 (min 182.13, max 183.12)","12.60 (min 11.89, max 13.60)"

 

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "102400","93.28 (min 24.51, max 99.44)","7.62 (min 3.50, max 19.48)","171.26 (min 165.13, max 178.47)","16.76 (min 10.36, max 23.97)"
    "262144","76.99 (min 27.28, max 99.83)","4.48 (min 1.25, max 12.68)","177.52 (min 170.96, max 180.49)","16.72 (min 8.62, max 30.42)"
    "524288","79.73 (min 34.07, max 100.43)","5.67 (min 1.33, max 17.10)","179.55 (min 178.18, max 180.81)","18.40 (min 10.43, max 30.34)"
    "1048576","79.10 (min 33.46, max 98.37)","7.35 (min 1.29, max 20.38)","178.45 (min 176.02, max 180.90)","16.57 (min 8.26, max 29.54)"
    "5242880","76.91 (min 32.42, max 98.19)","7.98 (min 1.38, max 21.61)","180.68 (min 180.05, max 181.07)","16.34 (min 9.52, max 25.33)"

 


EMMC EXT2
^^^^^^^^^


.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT2 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT2 CPU Load (%)","am62xx_sk-fs: Read EXT2 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT2 CPU Load (%)"

    "102400","60.69 (min 42.39, max 84.16)","5.24 (min 2.96, max 10.55)","167.37 (min 163.92, max 173.46)","8.61 (min 6.56, max 10.00)"
    "262144","59.48 (min 44.36, max 85.86)","4.12 (min 2.43, max 10.39)","172.78 (min 169.11, max 179.85)","9.89 (min 7.95, max 11.02)"
    "524288","58.89 (min 44.04, max 85.45)","4.24 (min 2.51, max 9.41)","175.19 (min 172.15, max 176.93)","10.48 (min 8.47, max 11.93)"
    "1048576","59.56 (min 44.64, max 86.45)","4.16 (min 2.46, max 8.73)","175.40 (min 172.22, max 177.77)","9.66 (min 8.66, max 11.06)"
    "5242880","60.06 (min 45.56, max 86.59)","3.90 (min 2.24, max 8.43)","175.87 (min 173.56, max 178.30)","10.52 (min 8.51, max 11.91)"

 


.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT2 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT2 CPU Load (%)","am62xx_lp_sk-fs: Read EXT2 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT2 CPU Load (%)"

    "102400","43.48 (min 35.48, max 49.38)","4.25 (min 2.94, max 6.86)","168.71 (min 159.08, max 174.58)","11.33 (min 10.73, max 12.30)"
    "262144","45.52 (min 35.33, max 53.07)","3.66 (min 2.25, max 7.33)","174.08 (min 167.68, max 179.57)","11.86 (min 11.30, max 12.76)"
    "524288","45.76 (min 35.60, max 53.66)","3.82 (min 2.45, max 6.86)","173.28 (min 172.03, max 176.16)","12.16 (min 11.25, max 13.11)"
    "1048576","46.40 (min 35.82, max 54.28)","3.93 (min 2.33, max 7.48)","176.06 (min 173.77, max 177.63)","11.95 (min 10.26, max 13.25)"
    "5242880","47.21 (min 36.65, max 56.25)","3.52 (min 2.31, max 6.18)","176.66 (min 172.16, max 178.86)","13.25 (min 12.07, max 14.41)"

 


.. csv-table:: EMMC EXT2
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT2 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT2 CPU Load (%)","am62xxsip_sk-fs: Read EXT2 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT2 CPU Load (%)"

    "102400","84.10 (min 34.98, max 96.31)","8.55 (min 1.98, max 27.86)","161.73 (min 156.39, max 170.85)","20.35 (min 15.06, max 27.38)"
    "262144","75.57 (min 13.00, max 97.16)","5.54 (min 0.69, max 16.87)","166.17 (min 163.25, max 168.92)","17.06 (min 10.84, max 24.90)"
    "524288","80.23 (min 46.20, max 97.58)","5.95 (min 1.80, max 17.27)","168.59 (min 165.67, max 172.89)","16.34 (min 10.92, max 24.70)"
    "1048576","78.15 (min 48.08, max 99.03)","7.32 (min 1.52, max 16.97)","171.91 (min 167.85, max 178.30)","14.94 (min 8.62, max 23.90)"
    "5242880","80.32 (min 54.47, max 97.26)","8.93 (min 1.80, max 23.98)","172.48 (min 169.42, max 176.19)","15.74 (min 9.13, max 24.80)"


EMMC VFAT
^^^^^^^^^


.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xx_sk-fs: Write VFAT CPU Load (%)","am62xx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xx_sk-fs: Read VFAT CPU Load (%)"

    "102400","44.55 (min 33.43, max 48.68)","6.26 (min 4.71, max 9.25)","167.93 (min 161.93, max 170.07)","13.19 (min 10.55, max 14.56)"
    "262144","45.10 (min 35.30, max 48.62)","6.40 (min 4.79, max 9.39)","168.62 (min 161.76, max 171.41)","13.79 (min 13.22, max 14.34)"
    "524288","46.11 (min 35.21, max 50.57)","6.43 (min 4.96, max 10.42)","165.11 (min 152.92, max 169.64)","13.61 (min 12.96, max 14.11)"
    "1048576","44.84 (min 33.24, max 49.15)","6.38 (min 4.50, max 9.33)","165.41 (min 156.74, max 168.30)","13.68 (min 12.55, max 14.46)"
    "5242880","45.81 (min 35.23, max 50.99)","6.35 (min 4.85, max 9.88)","164.83 (min 153.92, max 168.75)","15.19 (min 14.46, max 15.66)"



.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write VFAT CPU Load (%)","am62xx_lp_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read VFAT CPU Load (%)"

    "102400","44.58 (min 32.83, max 49.34)","6.86 (min 4.88, max 10.01)","168.97 (min 168.30, max 169.74)","14.45 (min 13.64, max 15.38)"
    "262144","44.99 (min 32.56, max 49.40)","7.09 (min 5.27, max 10.18)","169.30 (min 167.31, max 170.27)","15.90 (min 14.88, max 16.80)"
    "524288","44.49 (min 32.64, max 49.36)","7.14 (min 5.22, max 10.03)","167.25 (min 166.69, max 167.90)","15.37 (min 14.63, max 16.00)"
    "1048576","45.43 (min 34.25, max 49.51)","7.12 (min 5.41, max 10.33)","166.66 (min 163.93, max 167.67)","16.09 (min 14.57, max 17.41)"
    "5242880","44.83 (min 32.77, max 51.69)","6.98 (min 5.21, max 10.58)","165.87 (min 163.59, max 167.66)","17.72 (min 16.80, max 19.60)"



.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write VFAT CPU Load (%)","am62xxsip_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read VFAT CPU Load (%)"

    "102400","77.16 (min 47.97, max 96.24)","16.49 (min 4.32, max 30.40)","174.09 (min 172.88, max 175.03)","12.59 (min 10.50, max 14.05)"
    "262144","75.70 (min 56.81, max 96.63)","11.38 (min 4.45, max 26.37)","175.67 (min 174.43, max 176.12)","13.05 (min 11.02, max 15.00)"
    "524288","75.73 (min 56.09, max 97.19)","12.04 (min 4.83, max 24.29)","175.13 (min 174.03, max 175.55)","13.24 (min 11.02, max 15.55)"
    "1048576","75.41 (min 55.14, max 96.14)","11.90 (min 5.49, max 20.06)","174.50 (min 172.76, max 175.45)","15.04 (min 12.45, max 20.75)"
    "5242880","76.51 (min 57.28, max 97.55)","11.20 (min 5.64, max 26.11)","173.60 (min 171.43, max 175.10)","13.91 (min 12.29, max 15.29)"



UBoot EMMC Driver
-----------------


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","66548.10 (min 57996.46, max 96946.75)","170143.50 (min 168907.22, max 172463.16)"
    "4000000","66752.61 (min 58935.25, max 95533.53)","173745.52 (min 172918.21, max 174762.67)"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","58475.27 (min 56594.13, max 61134.33)","170668.52 (min 169782.38, max 171560.21)"
    "4000000","59231.47 (min 57740.97, max 62178.37)","174113.43 (min 173375.66, max 174297.87)"

 

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","97239.96 (min 96093.84, max 98107.78)","158060.71 (min 143091.70, max 171560.21)"
    "4000000","98799.87 (min 96234.95, max 100515.34)","172485.12 (min 164250.63, max 175229.95)"



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
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","43.60 (min 42.50, max 44.70)","1.49 (min 1.24, max 1.61)","87.60 (min 87.40, max 88.20)","1.68 (min 1.29, max 1.91)"
    "4m","42.84 (min 41.70, max 43.60)","1.06 (min 0.84, max 1.20)","86.54 (min 83.20, max 87.50)","1.13 (min 0.99, max 1.28)"
    "4k","2.84 (min 2.80, max 2.89)","1.84 (min 1.68, max 1.93)","12.94 (min 12.90, max 13.00)","4.15 (min 3.95, max 4.29)"
    "256k","39.24 (min 37.00, max 40.70)","1.68 (min 1.35, max 1.90)","84.10 (min 83.80, max 84.90)","1.71 (min 1.56, max 1.93)"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","43.64 (min 42.50, max 46.30)","1.68 (min 1.54, max 1.82)","85.96 (min 85.30, max 87.20)","1.82 (min 1.72, max 1.96)"
    "4m","42.58 (min 40.50, max 44.80)","1.25 (min 1.13, max 1.37)","85.24 (min 82.80, max 87.40)","1.25 (min 1.17, max 1.37)"
    "4k","2.74 (min 2.38, max 2.90)","2.03 (min 1.77, max 2.21)","12.28 (min 9.38, max 13.10)","4.39 (min 3.39, max 4.76)"
    "256k","39.18 (min 38.60, max 40.20)","1.88 (min 1.77, max 1.96)","83.94 (min 82.00, max 84.70)","1.98 (min 1.89, max 2.03)"



.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "1m","43.88 (min 42.50, max 46.10)","1.50 (min 1.32, max 1.74)","86.23 (min 84.30, max 87.40)","1.61 (min 1.52, max 1.82)"
    "4m","42.20 (min 40.30, max 44.10)","1.30 (min 1.20, max 1.52)","85.60 (min 83.60, max 86.90)","1.47 (min 1.19, max 1.73)"
    "4k","2.68 (min 2.31, max 2.82)","1.69 (min 1.54, max 1.78)","12.06 (min 9.32, max 13.00)","3.94 (min 3.78, max 4.16)"
    "256k","39.10 (min 37.90, max 40.10)","1.53 (min 1.37, max 1.79)","83.58 (min 82.00, max 84.30)","1.53 (min 1.43, max 1.64)"



MMC EXT4
^^^^^^^^


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Write Raw CPU Load (%)","am62xx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.76 (min 10.55, max 11.00)","0.79 (min 0.56, max 1.14)","10.86 (min 10.68, max 11.10)","0.71 (min 0.56, max 0.84)"
    "262144","10.73 (min 10.27, max 10.86)","0.70 (min 0.51, max 1.29)","11.09 (min 10.80, max 11.24)","0.74 (min 0.67, max 0.78)"
    "524288","10.73 (min 10.45, max 10.97)","0.62 (min 0.44, max 1.00)","11.20 (min 11.04, max 11.51)","0.72 (min 0.53, max 0.86)"
    "1048576","10.76 (min 10.48, max 11.19)","0.61 (min 0.40, max 0.90)","11.49 (min 11.04, max 12.03)","0.75 (min 0.55, max 1.06)"
    "5242880","10.97 (min 10.69, max 11.22)","0.64 (min 0.48, max 0.87)","12.01 (min 12.00, max 12.02)","0.92 (min 0.75, max 1.00)"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write Raw CPU Load (%)","am62xx_lp_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read Raw CPU Load (%)"

    "102400","10.62 (min 10.02, max 11.15)","0.96 (min 0.74, max 1.39)","10.94 (min 10.55, max 11.82)","0.85 (min 0.76, max 0.96)"
    "262144","10.34 (min 9.43, max 10.95)","0.84 (min 0.62, max 1.28)","10.96 (min 10.82, max 11.20)","0.83 (min 0.62, max 0.96)"
    "524288","10.34 (min 9.72, max 10.75)","0.74 (min 0.62, max 1.00)","11.21 (min 10.99, max 11.47)","0.88 (min 0.76, max 1.07)"
    "1048576","10.65 (min 10.08, max 11.20)","0.75 (min 0.63, max 0.99)","11.80 (min 11.49, max 12.02)","1.17 (min 1.00, max 1.40)"
    "5242880","10.67 (min 10.33, max 11.15)","0.80 (min 0.65, max 1.03)","11.62 (min 11.04, max 12.02)","0.87 (min 0.77, max 0.98)"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write Raw CPU Load (%)","am62xxsip_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read Raw CPU Load (%)"

    "102400","10.52 (min 9.99, max 10.81)","1.09 (min 0.36, max 2.37)","10.85 (min 10.76, max 10.90)","1.10 (min 0.67, max 1.51)"
    "262144","10.48 (min 9.85, max 10.89)","0.65 (min 0.37, max 1.06)","11.04 (min 10.82, max 11.21)","1.10 (min 0.75, max 1.58)"
    "524288","10.63 (min 10.02, max 10.90)","0.76 (min 0.44, max 1.72)","11.16 (min 11.00, max 11.52)","1.19 (min 0.89, max 1.48)"
    "1048576","10.75 (min 10.04, max 11.35)","0.93 (min 0.44, max 1.83)","11.88 (min 11.49, max 12.02)","1.33 (min 0.69, max 2.49)"
    "5242880","11.00 (min 10.53, max 11.32)","1.19 (min 0.33, max 3.31)","12.01 (min 12.00, max 12.02)","1.26 (min 0.74, max 2.13)"

 


MMC EXT3
^^^^^^^^


.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Write Raw CPU Load (%)","am62xx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Read Raw CPU Load (%)"

    "102400","31.76 (min 28.14, max 34.12)","2.65 (min 1.84, max 4.99)","72.76 (min 69.78, max 75.25)","4.25 (min 3.72, max 4.85)"
    "262144","31.79 (min 27.67, max 35.83)","2.19 (min 1.50, max 4.10)","78.04 (min 76.62, max 79.51)","4.99 (min 4.70, max 5.51)"
    "524288","32.45 (min 28.71, max 34.65)","2.31 (min 1.46, max 4.26)","80.08 (min 73.55, max 83.33)","4.88 (min 4.02, max 5.77)"
    "1048576","32.40 (min 27.80, max 34.65)","2.17 (min 1.48, max 4.32)","82.70 (min 80.02, max 84.56)","5.15 (min 4.79, max 5.56)"
    "5242880","34.18 (min 29.97, max 40.84)","2.21 (min 1.31, max 4.36)","84.57 (min 81.23, max 86.51)","5.45 (min 4.70, max 6.02)"

 


.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write Raw CPU Load (%)","am62xx_lp_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read Raw CPU Load (%)"

    "102400","31.43 (min 26.73, max 34.07)","3.07 (min 2.19, max 5.56)","69.42 (min 63.10, max 73.85)","4.82 (min 3.80, max 5.57)"
    "262144","30.16 (min 23.98, max 33.23)","2.56 (min 1.65, max 4.64)","72.76 (min 69.08, max 76.71)","5.36 (min 4.79, max 5.70)"
    "524288","32.95 (min 27.50, max 37.36)","2.76 (min 1.71, max 5.02)","79.71 (min 76.56, max 83.87)","5.65 (min 5.13, max 6.41)"
    "1048576","35.89 (min 27.05, max 42.41)","2.83 (min 1.80, max 5.27)","81.39 (min 73.87, max 89.78)","6.49 (min 5.85, max 7.10)"
    "5242880","35.14 (min 27.50, max 39.71)","2.70 (min 1.93, max 5.41)","82.98 (min 80.25, max 87.01)","6.55 (min 6.20, max 6.91)"

 


.. csv-table:: MMC EXT3
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write Raw CPU Load (%)","am62xxsip_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read Raw CPU Load (%)"

    "102400","29.80 (min 22.97, max 37.43)","3.81 (min 1.51, max 8.26)","70.82 (min 65.50, max 75.00)","9.29 (min 5.73, max 11.73)"
    "262144","35.31 (min 23.25, max 42.55)","2.49 (min 1.37, max 6.28)","78.08 (min 74.94, max 85.39)","8.26 (min 5.44, max 9.86)"
    "524288","35.73 (min 32.47, max 39.49)","3.37 (min 1.48, max 7.24)","83.23 (min 82.38, max 84.12)","9.00 (min 6.34, max 10.24)"
    "1048576","39.73 (min 34.47, max 44.80)","4.85 (min 1.49, max 10.28)","85.50 (min 83.35, max 88.87)","8.47 (min 5.76, max 10.28)"
    "5242880","36.53 (min 35.05, max 38.08)","7.01 (min 1.18, max 12.27)","83.92 (min 82.33, max 84.89)","9.59 (min 4.94, max 12.12)"

 


MMC EXT2
^^^^^^^^


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Write Raw CPU Load (%)","am62xx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Read Raw CPU Load (%)"

    "102400","32.44 (min 27.56, max 35.20)","2.54 (min 1.69, max 4.41)","73.01 (min 70.35, max 76.35)","4.26 (min 3.63, max 4.73)"
    "262144","31.31 (min 27.06, max 34.35)","2.18 (min 1.23, max 4.30)","75.14 (min 65.87, max 78.67)","4.95 (min 3.31, max 7.10)"
    "524288","33.07 (min 29.85, max 36.76)","2.27 (min 1.24, max 5.08)","81.65 (min 78.79, max 83.83)","5.40 (min 4.98, max 5.82)"
    "1048576","35.33 (min 30.45, max 40.00)","2.27 (min 1.53, max 4.12)","83.89 (min 82.07, max 84.83)","5.17 (min 4.51, max 6.25)"
    "5242880","34.72 (min 30.16, max 39.50)","2.18 (min 1.48, max 3.84)","84.90 (min 83.92, max 85.77)","5.20 (min 4.52, max 5.70)"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write Raw CPU Load (%)","am62xx_lp_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read Raw CPU Load (%)"

    "102400","32.85 (min 29.25, max 35.23)","3.06 (min 2.05, max 5.51)","73.27 (min 71.27, max 74.67)","5.16 (min 4.81, max 5.53)"
    "262144","33.13 (min 27.96, max 42.81)","2.66 (min 1.83, max 4.73)","77.68 (min 73.00, max 85.28)","5.70 (min 5.37, max 5.93)"
    "524288","33.08 (min 28.78, max 37.46)","2.72 (min 2.03, max 5.06)","80.70 (min 77.99, max 83.29)","6.33 (min 5.54, max 6.94)"
    "1048576","34.94 (min 28.45, max 42.09)","2.64 (min 1.92, max 4.70)","83.90 (min 79.49, max 89.82)","6.32 (min 5.61, max 7.39)"
    "5242880","33.68 (min 29.57, max 38.00)","2.65 (min 1.69, max 4.45)","83.46 (min 81.02, max 84.78)","6.60 (min 6.19, max 7.17)"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write Raw CPU Load (%)","am62xxsip_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read Raw CPU Load (%)"

    "102400","29.87 (min 23.30, max 35.23)","2.75 (min 1.14, max 7.42)","70.21 (min 63.61, max 75.59)","5.47 (min 3.99, max 8.78)"
    "262144","35.31 (min 32.62, max 40.58)","1.89 (min 0.94, max 5.16)","76.42 (min 73.50, max 80.91)","6.35 (min 3.55, max 11.66)"
    "524288","34.39 (min 30.32, max 36.34)","2.21 (min 1.03, max 6.07)","79.91 (min 76.44, max 83.52)","6.88 (min 4.28, max 12.40)"
    "1048576","36.15 (min 33.60, max 37.65)","2.75 (min 1.14, max 8.70)","83.38 (min 81.19, max 84.70)","5.95 (min 4.27, max 9.24)"
    "5242880","37.34 (min 35.23, max 39.34)","3.18 (min 1.00, max 9.34)","82.40 (min 78.52, max 85.19)","5.91 (min 4.17, max 9.81)"

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 



UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","35959.37 (min 25761.01, max 40554.46)","81803.04 (min 75851.85, max 83591.84)"
    "800000","41256.89 (min 28845.07, max 49349.40)","87151.13 (min 86231.58, max 88086.02)"
    "1000000","47501.89 (min 43690.67, max 49648.48)","89475.99 (min 89043.48, max 89530.05)"


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","38338.18 (min 35617.39, max 39766.99)","81933.11 (min 80313.73, max 83591.84)"
    "800000","44696.22 (min 39960.98, max 49349.40)","86782.00 (min 86231.58, max 87148.94)"
    "1000000","49885.70 (min 43574.47, max 54613.33)","89142.89 (min 88562.16, max 89530.05)"


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","36727.07 (min 32251.97, max 39766.99)","83173.88 (min 81920.00, max 83591.84)"
    "800000","42247.31 (min 37236.36, max 47080.46)","87148.94"
    "1000000","48627.22 (min 47627.91, max 49349.40)","89653.03 (min 89530.05, max 90021.98)"


The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 

|

USB Driver
-------------------------
 


USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)","am62xxsip_sk-fs: Throughput (MB/sec)"

    "150","39.06 (min 35.30, max 43.90)","42.88 (min 42.00, max 43.80)","44.08 (min 43.90, max 44.40)"



.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)","am62xxsip_sk-fs: Throughput (MB/sec)"

    "150","36.42 (min 33.40, max 39.70)","40.80 (min 40.10, max 41.80)","39.85 (min 38.00, max 41.60)"


|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62xx_lp_sk-fs: throughput (KBytes/Sec)","am62xx_sk-fs: throughput (KBytes/Sec)","am62xxsip_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","18977.85 (min 18394.45, max 20248.58)","21651.70 (min 20509.35, max 22688.09)","20736.94 (min 20347.90, max 21727.91)"
    "aes-128-cbc","16","378.79 (min 375.53, max 382.16)","408.84 (min 384.24, max 465.69)","385.79 (min 385.00, max 387.50)"
    "aes-128-cbc","16384","119413.87 (min 116648.62, max 121552.90)","125335.26 (min 120433.32, max 135981.74)","124717.74 (min 123125.76, max 125747.20)"
    "aes-128-cbc","256","6190.02 (min 6071.30, max 6284.54)","6998.06 (min 6219.09, max 7965.70)","6611.20 (min 6207.74, max 6761.81)"
    "aes-128-cbc","64","1572.14 (min 1528.94, max 1638.17)","1818.41 (min 1614.46, max 2043.22)","1728.69 (min 1593.41, max 1779.63)"
    "aes-128-cbc","8192","91341.71 (min 88451.75, max 93115.73)","99342.04 (min 94967.13, max 104953.17)","98206.38 (min 97804.29, max 98448.73)"
    "aes-128-ecb","1024","19317.48 (min 18519.38, max 20401.49)","22346.41 (min 21083.48, max 23313.41)","21503.91 (min 21052.76, max 22771.71)"
    "aes-128-ecb","16","380.50 (min 376.57, max 384.12)","420.65 (min 386.27, max 478.16)","396.44 (min 386.31, max 404.43)"
    "aes-128-ecb","16384","121612.97 (min 119373.82, max 122781.70)","130880.85 (min 124725.93, max 140432.73)","130669.23 (min 128843.78, max 131312.30)"
    "aes-128-ecb","256","6310.56 (min 6097.58, max 6605.57)","7218.63 (min 6298.20, max 8178.01)","6869.76 (min 6246.91, max 7153.92)"
    "aes-128-ecb","64","1609.79 (min 1542.49, max 1727.10)","1895.57 (min 1716.03, max 2121.15)","1790.79 (min 1682.69, max 1865.37)"
    "aes-128-ecb","8192","95180.12 (min 91430.91, max 96927.74)","101433.34 (min 98202.97, max 109030.06)","98494.46 (min 98402.30, max 98557.95)"
    "aes-192-cbc","1024","18814.58 (min 18410.50, max 20017.15)","21459.09 (min 20200.45, max 22637.23)","20646.49 (min 20291.93, max 21548.03)"
    "aes-192-cbc","16","379.34 (min 375.74, max 383.47)","409.27 (min 384.65, max 462.91)","387.86 (min 384.07, max 392.70)"
    "aes-192-cbc","16384","112595.40 (min 108522.15, max 114627.93)","118458.66 (min 113437.35, max 127866.20)","117362.69 (min 115927.72, max 117937.49)"
    "aes-192-cbc","256","6159.02 (min 6063.19, max 6204.59)","6947.96 (min 6208.51, max 7914.58)","6610.56 (min 6198.44, max 6845.35)"
    "aes-192-cbc","64","1571.22 (min 1523.75, max 1642.39)","1815.19 (min 1618.97, max 2043.63)","1714.43 (min 1550.51, max 1791.27)"
    "aes-192-cbc","8192","87137.85 (min 84361.22, max 88637.44)","93785.53 (min 89593.17, max 100335.62)","93470.04 (min 90311.34, max 95821.82)"
    "aes-192-ecb","1024","19242.21 (min 18541.91, max 20331.86)","22259.13 (min 21011.11, max 23232.51)","21466.45 (min 21001.56, max 22706.18)"
    "aes-192-ecb","16","380.99 (min 375.53, max 383.98)","420.35 (min 385.70, max 477.98)","398.01 (min 381.25, max 406.92)"
    "aes-192-ecb","16384","117005.43 (min 112672.77, max 120291.33)","122987.67 (min 118194.18, max 132978.01)","122395.31 (min 120919.38, max 122972.84)"
    "aes-192-ecb","256","6299.18 (min 6092.54, max 6586.37)","7184.54 (min 6283.61, max 8173.82)","6863.02 (min 6251.09, max 7155.80)"
    "aes-192-ecb","64","1605.30 (min 1541.44, max 1722.33)","1887.54 (min 1695.25, max 2117.12)","1808.19 (min 1674.84, max 1868.12)"
    "aes-192-ecb","8192","90469.26 (min 87414.10, max 92722.52)","98834.92 (min 93727.40, max 104581.80)","97595.39 (min 95931.05, max 98309.46)"
    "aes-256-cbc","1024","18711.55 (min 18308.78, max 19727.36)","21071.77 (min 20045.48, max 22235.82)","20295.51 (min 19700.39, max 21456.90)"
    "aes-256-cbc","16","379.59 (min 375.90, max 383.76)","409.21 (min 384.25, max 465.94)","387.68 (min 383.82, max 390.51)"
    "aes-256-cbc","16384","104694.67 (min 99276.12, max 107621.03)","109936.64 (min 106354.01, max 117964.80)","108130.30 (min 107326.12, max 109723.65)"
    "aes-256-cbc","256","6148.86 (min 6063.10, max 6181.38)","6917.50 (min 6205.70, max 7883.01)","6496.21 (min 6190.76, max 6641.66)"
    "aes-256-cbc","64","1572.02 (min 1527.83, max 1642.24)","1806.17 (min 1586.37, max 2046.70)","1719.51 (min 1585.88, max 1784.38)"
    "aes-256-cbc","8192","82831.59 (min 79798.27, max 84511.40)","88505.20 (min 84219.22, max 95150.08)","86915.07 (min 85297.83, max 88208.73)"
    "aes-256-ecb","1024","19278.73 (min 18512.90, max 20477.61)","21784.72 (min 20646.91, max 22739.63)","21193.73 (min 20683.78, max 22409.90)"
    "aes-256-ecb","16","381.19 (min 376.40, max 384.63)","420.47 (min 385.58, max 477.11)","398.34 (min 385.93, max 405.72)"
    "aes-256-ecb","16384","110105.94 (min 107113.13, max 113262.59)","114585.01 (min 107812.18, max 123207.68)","113975.30 (min 112612.69, max 114775.38)"
    "aes-256-ecb","256","6294.12 (min 6113.54, max 6607.96)","7143.86 (min 6236.33, max 8153.26)","6812.59 (min 6225.41, max 7101.87)"
    "aes-256-ecb","64","1615.34 (min 1542.21, max 1735.91)","1887.85 (min 1678.38, max 2133.01)","1814.69 (min 1692.76, max 1881.02)"
    "aes-256-ecb","8192","86476.12 (min 84140.03, max 88754.86)","92044.14 (min 87919.27, max 98394.11)","91720.36 (min 89191.77, max 93181.27)"
    "sha256","1024","24614.74 (min 24410.79, max 24789.33)","28566.19 (min 27299.16, max 31053.14)","26271.74 (min 25423.87, max 27493.72)"
    "sha256","16","397.46 (min 386.68, max 416.60)","481.84 (min 466.90, max 511.49)","459.56 (min 455.64, max 466.64)"
    "sha256","16384","233674.98 (min 232767.49, max 234602.50)","266009.84 (min 261969.24, max 276632.92)","261438.12 (min 261079.04, max 261849.09)"
    "sha256","256","6235.88 (min 6174.63, max 6420.14)","7546.33 (min 7233.54, max 8083.20)","7156.59 (min 7068.33, max 7347.88)"
    "sha256","64","1570.23 (min 1546.26, max 1631.83)","1907.52 (min 1839.57, max 2042.01)","1809.42 (min 1787.58, max 1845.35)"
    "sha256","8192","151538.80 (min 149099.86, max 154454.70)","174553.58 (min 170890.58, max 179683.33)","169099.26 (min 168037.03, max 171477.67)"
    "sha512","1024","22334.41 (min 21967.19, max 22827.35)","25018.03 (min 24584.87, max 26285.74)","24581.21 (min 24557.23, max 24623.79)"
    "sha512","16","388.87 (min 385.80, max 397.54)","466.91 (min 448.48, max 508.92)","442.16 (min 431.85, max 460.50)"
    "sha512","16384","97186.25 (min 96731.14, max 97801.56)","109388.17 (min 108462.08, max 110859.61)","107704.32 (min 107113.13, max 108953.60)"
    "sha512","256","6111.36 (min 6070.95, max 6147.24)","6699.26 (min 6204.67, max 7669.16)","6308.78 (min 6200.83, max 6631.17)"
    "sha512","64","1555.03 (min 1543.49, max 1586.73)","1867.67 (min 1795.97, max 2035.65)","1771.22 (min 1727.87, max 1843.26)"
    "sha512","8192","78165.79 (min 77832.19, max 78484.82)","88805.18 (min 87643.48, max 91209.73)","87623.68 (min 87124.65, max 89019.73)"



.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62xx_lp_sk-fs: CPU Load","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: CPU Load"

    "aes-128-cbc","37.00 (min 36.00, max 39.00)","35.86 (min 35.00, max 38.00)","36.00 (min 35.00, max 38.00)"
    "aes-128-ecb","39.67 (min 38.00, max 41.00)","37.29 (min 36.00, max 39.00)","38.50 (min 37.00, max 41.00)"
    "aes-192-cbc","38.17 (min 37.00, max 39.00)","36.57 (min 35.00, max 39.00)","36.50 (min 35.00, max 39.00)"
    "aes-192-ecb","39.17 (min 37.00, max 41.00)","36.57 (min 36.00, max 38.00)","37.50 (min 37.00, max 39.00)"
    "aes-256-cbc","38.00 (min 37.00, max 39.00)","36.14 (min 35.00, max 38.00)","36.25 (min 35.00, max 39.00)"
    "aes-256-ecb","38.50 (min 36.00, max 40.00)","35.71 (min 32.00, max 39.00)","37.50 (min 36.00, max 40.00)"
    "sha256","94.50 (min 94.00, max 95.00)","91.57 (min 69.00, max 96.00)","95.00"
    "sha512","94.33 (min 94.00, max 95.00)","95.29 (min 95.00, max 96.00)","95.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc

.. _crypto-performance:

Crypto Performance Comparison
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following table shows different AES/SHA algorithms throughput measured using
openssl speed across the SA3UL accelerator, ARM Cryptographic Extension (CE), and baseline ARM CPU.

.. csv-table:: Crypto Accelerator Performance
    :header: "Algorithm", "Size (bytes)", "Accelerator (MB/s)", "ARM CE (MB/s)", "ARM (MB/s)"
    :widths: 20, 25, 20, 20, 20

    "aes-128-cbc", "16", "0.45", "97.73", "31.20"
    "aes-128-cbc", "64", "1.99", "304.30", "39.79"
    "aes-128-cbc", "256", "7.72", "636.67", "42.94"
    "aes-128-cbc", "1024", "21.86", "895.64", "43.82"
    "aes-128-cbc", "8192", "102.05", "1018.99", "44.05"
    "aes-128-cbc", "16384", "131.01", "1028.67", "44.01"
    "aes-128-ecb", "16 bytes", "0.38", "101.97", "32.06"
    "aes-128-ecb", "64 bytes", "1.76", "279.44", "40.04"
    "aes-128-ecb", "256 bytes", "6.71", "639.87", "42.85"
    "aes-128-ecb", "1024 bytes", "19.99", "960.23", "43.61"
    "aes-128-ecb", "8192 bytes", "93.42", "1129.36", "43.83"
    "aes-128-ecb", "16384 bytes", "121.38", "1141.08", "43.84"
    "aes-192-cbc", "16 bytes", "0.32", "91.33", "27.08"
    "aes-192-cbc", "64 bytes", "1.65", "269.97", "34.19"
    "aes-192-cbc", "256 bytes", "6.62", "522.39", "36.72"
    "aes-192-cbc", "1024 bytes", "20.06", "692.84", "37.40"
    "aes-192-cbc", "8192 bytes", "90.84", "767.14", "37.61"
    "aes-192-cbc", "16384 bytes", "113.89", "773.14", "37.61"
    "aes-192-ecb", "16 bytes", "0.46", "100.13", "29.41"
    "aes-192-ecb", "64 bytes", "2.06", "270.43", "35.47"
    "aes-192-ecb", "256 bytes", "7.98", "599.16", "37.51"
    "aes-192-ecb", "1024 bytes", "22.31", "872.68", "38.05"
    "aes-192-ecb", "8192 bytes", "101.09", "1005.80", "38.21"
    "aes-192-ecb", "16384 bytes", "127.68", "1016.40", "38.21"
    "aes-256-cbc", "16 bytes", "0.37", "89.19", "24.67"
    "aes-256-cbc", "64 bytes", "1.68", "249.91", "29.71"
    "aes-256-cbc", "256 bytes", "6.37", "449.52", "31.44"
    "aes-256-cbc", "1024 bytes", "19.06", "569.64", "31.90"
    "aes-256-cbc", "8192 bytes", "82.56", "619.18", "32.04"
    "aes-256-cbc", "16384 bytes", "102.05", "622.82", "32.04"
    "aes-256-ecb", "16 bytes", "0.38", "94.26", "25.78"
    "aes-256-ecb", "64 bytes", "1.76", "249.85", "30.44"
    "aes-256-ecb", "256 bytes", "6.66", "523.62", "31.96"
    "aes-256-ecb", "1024 bytes", "19.66", "753.23", "32.36"
    "aes-256-ecb", "8192 bytes", "85.49", "856.40", "32.48"
    "aes-256-ecb", "16384 bytes", "106.41", "864.28", "32.47"
    "sha2-256", "16 bytes", "0.41", "11.63", "7.51"
    "sha2-256", "64 bytes", "1.45", "42.74", "22.16"
    "sha2-256", "256 bytes", "6.72", "140.62", "50.31"
    "sha2-256", "1024 bytes", "25.73", "327.24", "74.01"
    "sha2-256", "8192 bytes", "161.96", "537.28", "85.80"
    "sha2-256", "16384 bytes", "249.38", "562.66", "86.78"
    "sha2-512", "16 bytes", "0.43", "7.20", "7.21"
    "sha2-512", "64 bytes", "1.73", "28.73", "28.78"
    "sha2-512", "256 bytes", "6.06", "62.53", "62.64"
    "sha2-512", "1024 bytes", "23.45", "106.01", "105.97"
    "sha2-512", "8192 bytes", "84.48", "133.00", "132.99"
    "sha2-512", "16384 bytes", "103.98", "135.43", "135.40"

.. csv-table:: CPU Usage %
    :header: "Algorithm", "Accelerator (%)", "ARM CE (%)", "ARM (%)"
    :widths: 25, 25, 25, 25

    "aes-128-cbc", "35%", "99%", "99%"
    "aes-128-ecb", "36%", "99%", "99%"
    "aes-192-cbc", "23%", "99%", "99%"
    "aes-192-ecb", "36%", "99%", "99%"
    "aes-256-cbc", "35%", "99%", "99%"
    "aes-256-ecb", "35%", "99%", "99%"
    "sha2-256", "86%", "99%", "99%"
    "sha2-512", "93%", "99%", "99%"


IPSec Hardware Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note: queue\_len is set to 300 and software fallback threshold set to 9
to enable software support for optimal performance

.. csv-table:: IPSec Hardware Performance
    :header: "Algorithm","am62xx_sk-fs: Throughput (Mbps)","am62xx_sk-fs: Packets/Sec","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: Throughput (Mbps)","am62xxsip_sk-fs: Packets/Sec","am62xxsip_sk-fs: CPU Load"

    "aes128","1.90","0.00","22.31","2.50","0.00","16.46"
    "aes192","207.80","18.00","51.35","51.30","4.00","74.65"
    "aes256","50.60","4.00","50.99","34.70","3.00","50.40"


IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","am62xx_sk-fs: Throughput (Mbps)","am62xx_sk-fs: Packets/Sec","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: Throughput (Mbps)","am62xxsip_sk-fs: Packets/Sec","am62xxsip_sk-fs: CPU Load"

    "aes128","115.90 (min 0.20, max 414.10)","9.80 (min 0.00, max 36.00)","48.24 (min 29.08, max 59.28)","172.27 (min 0.20, max 416.10)","15.00 (min 0.00, max 37.00)","44.19 (min 30.68, max 51.63)"
    "aes192","162.16 (min 50.20, max 456.20)","14.00 (min 4.00, max 40.00)","44.00 (min 29.67, max 51.46)","0.70","0.00","36.21"
    "aes256","190.65 (min 45.70, max 459.10)","16.50 (min 4.00, max 40.00)","39.63 (min 26.98, max 51.15)","125.30 (min 0.40, max 409.10)","10.75 (min 0.00, max 36.00)","51.72 (min 49.72, max 54.04)"

|

Low Power Performance
-------------------------

Power Performance
^^^^^^^^^^^^^^^^^

.. csv-table:: DeepSleep Power Performance
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","9.01"
   "vddr_core","0.85","n/a"
   "soc_dvdd_3v3","3.30","5.86"
   "soc_dvdd_1v8","1.80","4.37"
   "vdda_1v8","1.80","1.80"
   "vdd_ddr4","1.10","8.07"
   "Total"," ","29.11"

.. csv-table:: MCU Only Power Performance
   :header: "Rail name","Rail voltage(V)","Power (mW)"

   "vdd_core","0.85","90.67"
   "vddr_core","0.85","n/a"
   "soc_dvdd_3v3","3.30","13.65"
   "soc_dvdd_1v8","1.80","4.95"
   "vdda_1v8","1.80","10.81"
   "vdd_ddr4","1.10","8.58"
   "Total"," ","128.66"

Partial I/O Data
- All voltage rails were measured to be near 0V

.. note::

   The measurements shown are from an SK-AM62B-P1. Results may vary based off of the board variant being used.
   For the most accurate power measurements, use the latest TIVA firmware.

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)

Resume Latency Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: LPM Resume Latency Performance
   :header: "Low Power Mode","Total Resume Latency (ms)"

   "DeepSleep", "124"
   "MCU Only", "76"

The performance numbers are measured without the Linux printk logs. To remove the
Linux printk logs, run the following commands in the terminal:

.. code:: console

   # Detach kernel serial console
   consoles=$(find /sys/bus/platform/devices/*.serial/ -name console)
   for console in ${consoles}; do
        echo -n N > ${console}
   done

.. note::

   The measurements shown are from using the default SDK with no extra optimizations.

Further optimizations are possible for these low power modes. Please refer to the AM62x Power Consumption App Note (https://www.ti.com/lit/pdf/spradg1)
