
====================================
 Linux 11.02.08.02 Performance Guide
====================================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

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
    ./runltp -P j721e-idk-gw -f ddt/lmbench -s LMBENCH_L_PERF_0001

.. csv-table:: LMBench Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "af_unix_sock_stream_latency (microsec)","33.40 (min 32.86, max 34.65)","29.79 (min 28.64, max 30.84)","33.61 (min 33.07, max 34.90)"
    "af_unix_socket_stream_bandwidth (mb\s)","532.62 (min 513.45, max 555.88)","602.54 (min 576.79, max 715.30)","728.89 (min 632.89, max 809.03)"
    "bw_file_rd-io-1mb (mb/s)","844.54 (min 822.23, max 886.68)","985.59 (min 935.75, max 1129.31)","970.83 (min 868.06, max 1075.08)"
    "bw_file_rd-o2c-1mb (mb/s)","460.27 (min 433.28, max 488.60)","520.63 (min 488.28, max 589.88)","545.10 (min 484.50, max 608.46)"
    "bw_mem-bcopy-16mb (mb/s)","666.43 (min 656.63, max 698.69)","779.46 (min 755.22, max 916.43)","804.83 (min 710.04, max 926.57)"
    "bw_mem-bcopy-1mb (mb/s)","700.75 (min 675.45, max 741.70)","842.36 (min 785.55, max 1038.96)","888.53 (min 745.85, max 1009.08)"
    "bw_mem-bcopy-2mb (mb/s)","657.09 (min 645.27, max 687.52)","789.75 (min 751.88, max 965.41)","796.56 (min 719.55, max 885.48)"
    "bw_mem-bcopy-4mb (mb/s)","689.78 (min 669.68, max 728.73)","816.64 (min 783.70, max 999.25)","813.86 (min 710.98, max 940.96)"
    "bw_mem-bcopy-8mb (mb/s)","699.67 (min 684.46, max 732.80)","822.42 (min 799.44, max 920.70)","807.96 (min 708.84, max 914.81)"
    "bw_mem-bzero-16mb (mb/s)","1706.95 (min 1678.03, max 1776.99)","1798.84 (min 1743.30, max 2125.68)","1932.00 (min 1724.88, max 2128.79)"
    "bw_mem-bzero-1mb (mb/s)","1194.75 (min 675.45, max 1771.79)","1310.82 (min 785.55, max 2122.77)","1407.48 (min 745.85, max 2129.17)"
    "bw_mem-bzero-2mb (mb/s)","1172.66 (min 645.27, max 1768.35)","1285.64 (min 751.88, max 2123.14)","1361.57 (min 719.55, max 2130.30)"
    "bw_mem-bzero-4mb (mb/s)","1189.77 (min 669.68, max 1766.78)","1299.62 (min 783.70, max 2125.78)","1370.93 (min 710.98, max 2129.93)"
    "bw_mem-bzero-8mb (mb/s)","1202.52 (min 684.46, max 1767.37)","1310.44 (min 799.44, max 2125.12)","1372.21 (min 708.84, max 2128.79)"
    "bw_mem-cp-16mb (mb/s)","381.91 (min 356.51, max 400.99)","466.22 (min 438.89, max 574.16)","470.46 (min 411.22, max 525.11)"
    "bw_mem-cp-1mb (mb/s)","1107.67 (min 369.41, max 1907.67)","1193.34 (min 436.81, max 2264.58)","1276.71 (min 394.48, max 2281.80)"
    "bw_mem-cp-2mb (mb/s)","1071.32 (min 360.82, max 1842.30)","1160.88 (min 427.53, max 2201.03)","1231.90 (min 381.90, max 2205.48)"
    "bw_mem-cp-4mb (mb/s)","1072.77 (min 398.29, max 1814.61)","1162.44 (min 467.24, max 2159.05)","1218.76 (min 398.45, max 2171.16)"
    "bw_mem-cp-8mb (mb/s)","1071.48 (min 408.66, max 1804.85)","1164.03 (min 482.77, max 2152.85)","1203.39 (min 386.32, max 2174.80)"
    "bw_mem-fcp-16mb (mb/s)","669.23 (min 654.21, max 689.36)","757.23 (min 728.96, max 882.76)","867.40 (min 755.89, max 1002.82)"
    "bw_mem-fcp-1mb (mb/s)","1231.51 (min 756.43, max 1771.79)","1338.53 (min 855.29, max 2122.77)","1426.17 (min 823.32, max 2129.17)"
    "bw_mem-fcp-2mb (mb/s)","1211.46 (min 718.13, max 1768.35)","1330.64 (min 832.52, max 2123.14)","1411.18 (min 782.78, max 2130.30)"
    "bw_mem-fcp-4mb (mb/s)","1222.02 (min 729.13, max 1766.78)","1347.90 (min 869.28, max 2125.78)","1411.80 (min 780.03, max 2129.93)"
    "bw_mem-fcp-8mb (mb/s)","1236.32 (min 736.85, max 1767.37)","1366.49 (min 887.71, max 2125.12)","1415.27 (min 788.18, max 2128.79)"
    "bw_mem-frd-16mb (mb/s)","1022.55 (min 981.35, max 1076.35)","1188.74 (min 1132.50, max 1428.19)","1201.69 (min 1025.58, max 1350.67)"
    "bw_mem-frd-1mb (mb/s)","958.09 (min 756.43, max 1193.93)","1114.58 (min 855.29, max 1598.58)","1143.78 (min 823.32, max 1534.53)"
    "bw_mem-frd-2mb (mb/s)","871.89 (min 718.13, max 1081.28)","1010.04 (min 832.52, max 1378.12)","1048.22 (min 782.78, max 1358.00)"
    "bw_mem-frd-4mb (mb/s)","886.22 (min 729.13, max 1068.09)","1041.72 (min 869.28, max 1402.28)","1046.94 (min 780.03, max 1353.41)"
    "bw_mem-frd-8mb (mb/s)","895.53 (min 736.85, max 1082.98)","1056.14 (min 887.71, max 1422.22)","1050.26 (min 788.18, max 1356.62)"
    "bw_mem-fwr-16mb (mb/s)","1713.36 (min 1690.44, max 1779.76)","1809.72 (min 1752.08, max 2139.90)","1946.08 (min 1751.89, max 2145.35)"
    "bw_mem-fwr-1mb (mb/s)","1487.39 (min 1112.70, max 1907.67)","1624.29 (min 1263.54, max 2264.58)","1725.34 (min 1197.40, max 2281.80)"
    "bw_mem-fwr-2mb (mb/s)","1388.30 (min 974.34, max 1842.30)","1502.10 (min 1075.85, max 2201.03)","1601.94 (min 1076.57, max 2205.48)"
    "bw_mem-fwr-4mb (mb/s)","1378.25 (min 989.12, max 1814.61)","1502.80 (min 1074.98, max 2159.05)","1584.78 (min 1080.94, max 2171.16)"
    "bw_mem-fwr-8mb (mb/s)","1373.81 (min 975.73, max 1804.85)","1498.37 (min 1119.66, max 2152.85)","1582.44 (min 1073.39, max 2174.80)"
    "bw_mem-rd-16mb (mb/s)","1037.69 (min 1016.97, max 1083.72)","1187.07 (min 1098.90, max 1445.48)","1215.25 (min 1060.59, max 1351.12)"
    "bw_mem-rd-1mb (mb/s)","867.03 (min 533.14, max 1234.35)","1028.36 (min 648.40, max 1634.88)","1048.08 (min 572.63, max 1595.18)"
    "bw_mem-rd-2mb (mb/s)","767.51 (min 473.20, max 1085.19)","899.44 (min 569.48, max 1419.45)","923.31 (min 506.14, max 1376.70)"
    "bw_mem-rd-4mb (mb/s)","798.39 (min 530.01, max 1083.13)","946.09 (min 674.76, max 1435.49)","922.27 (min 522.94, max 1364.26)"
    "bw_mem-rd-8mb (mb/s)","831.83 (min 586.17, max 1084.60)","989.49 (min 743.43, max 1446.92)","937.43 (min 563.94, max 1356.62)"
    "bw_mem-rdwr-16mb (mb/s)","670.46 (min 629.00, max 718.55)","836.08 (min 773.47, max 1046.44)","662.35 (min 584.13, max 754.68)"
    "bw_mem-rdwr-1mb (mb/s)","463.26 (min 369.41, max 567.46)","576.99 (min 436.81, max 806.19)","571.73 (min 394.48, max 769.47)"
    "bw_mem-rdwr-2mb (mb/s)","429.34 (min 360.82, max 514.07)","532.83 (min 427.53, max 740.60)","529.48 (min 381.90, max 690.25)"
    "bw_mem-rdwr-4mb (mb/s)","480.32 (min 398.29, max 593.74)","588.73 (min 467.24, max 879.99)","548.02 (min 398.45, max 723.85)"
    "bw_mem-rdwr-8mb (mb/s)","525.75 (min 408.66, max 655.68)","644.03 (min 482.77, max 956.71)","545.57 (min 386.32, max 737.87)"
    "bw_mem-wr-16mb (mb/s)","667.31 (min 625.73, max 693.30)","844.62 (min 778.66, max 1039.37)","675.18 (min 587.59, max 771.12)"
    "bw_mem-wr-1mb (mb/s)","545.02 (min 524.48, max 572.66)","690.54 (min 638.47, max 819.94)","676.66 (min 572.63, max 781.40)"
    "bw_mem-wr-2mb (mb/s)","490.33 (min 468.06, max 525.97)","612.48 (min 567.54, max 740.60)","603.33 (min 506.14, max 707.21)"
    "bw_mem-wr-4mb (mb/s)","557.39 (min 494.56, max 593.74)","697.74 (min 605.05, max 879.99)","626.41 (min 522.94, max 725.16)"
    "bw_mem-wr-8mb (mb/s)","630.78 (min 586.17, max 671.76)","785.24 (min 709.66, max 1007.68)","648.27 (min 563.94, max 754.36)"
    "bw_mmap_rd-mo-1mb (mb/s)","1163.27 (min 1139.38, max 1219.09)","1324.21 (min 1260.35, max 1606.86)","1377.07 (min 1225.06, max 1541.36)"
    "bw_mmap_rd-o2c-1mb (mb/s)","455.11 (min 438.28, max 477.55)","500.79 (min 427.78, max 590.67)","519.99 (min 465.91, max 600.69)"
    "bw_pipe (mb/s)","443.15 (min 435.10, max 453.94)","515.70 (min 492.51, max 600.38)","498.69 (min 451.80, max 545.64)"
    "bw_unix (mb/s)","532.62 (min 513.45, max 555.88)","602.54 (min 576.79, max 715.30)","728.89 (min 632.89, max 809.03)"
    "lat_connect (us)","66.67 (min 66.20, max 67.85)","59.11 (min 58.18, max 59.76)","65.67 (min 63.87, max 69.00)"
    "lat_ctx-2-128k (us)","8.89 (min 8.32, max 9.14)","7.99 (min 7.63, max 8.34)","8.91 (min 8.50, max 9.59)"
    "lat_ctx-2-256k (us)","13.57 (min 9.14, max 16.40)","9.88 (min 6.84, max 10.92)","12.44 (min 8.10, max 15.04)"
    "lat_ctx-4-128k (us)","9.13 (min 8.33, max 9.61)","7.66 (min 7.17, max 8.17)","8.56 (min 8.09, max 8.88)"
    "lat_ctx-4-256k (us)","10.98 (min 7.76, max 13.14)","9.48 (min 7.36, max 12.90)","8.46 (min 0.00, max 12.65)"
    "lat_fs-0k (num_files)","198.86 (min 177.00, max 227.00)","213.63 (min 195.00, max 235.00)","198.88 (min 192.00, max 210.00)"
    "lat_fs-10k (num_files)","92.57 (min 86.00, max 103.00)","102.88 (min 92.00, max 128.00)","93.13 (min 82.00, max 104.00)"
    "lat_fs-1k (num_files)","124.29 (min 109.00, max 146.00)","145.63 (min 135.00, max 160.00)","134.75 (min 115.00, max 147.00)"
    "lat_fs-4k (num_files)","123.14 (min 107.00, max 130.00)","145.25 (min 128.00, max 159.00)","133.63 (min 123.00, max 158.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","56.96 (min 54.29, max 58.01)","50.45 (min 42.65, max 52.51)","48.81 (min 43.55, max 54.17)"
    "lat_mem_rd-stride128-sz125k (ns)","6.22 (min 6.20, max 6.26)","5.57 (min 5.54, max 5.58)","6.22 (min 6.20, max 6.26)"
    "lat_mem_rd-stride128-sz250k (ns)","6.54 (min 6.54, max 6.56)","5.84 (min 5.83, max 5.85)","6.54 (min 6.53, max 6.54)"
    "lat_mem_rd-stride128-sz31k (ns)","4.20 (min 2.42, max 4.70)","3.85 (min 3.65, max 4.19)","3.40 (min 2.41, max 4.70)"
    "lat_mem_rd-stride128-sz50 (ns)","2.40 (min 2.40, max 2.41)","2.15","2.40 (min 2.40, max 2.41)"
    "lat_mem_rd-stride128-sz500k (ns)","17.11 (min 11.46, max 21.66)","17.27 (min 13.44, max 20.26)","15.35 (min 10.09, max 21.82)"
    "lat_mem_rd-stride128-sz62k (ns)","5.77 (min 5.05, max 5.89)","5.24 (min 5.22, max 5.27)","5.87 (min 5.85, max 5.90)"
    "lat_mmap-1m (us)","66.14 (min 59.00, max 73.00)","55.13 (min 53.00, max 64.00)","64.75 (min 57.00, max 71.00)"
    "lat_ops-double-add (ns)","3.21","2.86 (min 2.86, max 2.87)","3.21"
    "lat_ops-double-div (ns)","17.63 (min 17.62, max 17.64)","15.74 (min 15.74, max 15.75)","17.63 (min 17.63, max 17.65)"
    "lat_ops-double-mul (ns)","3.21","2.86","3.21"
    "lat_ops-float-add (ns)","3.21","2.86 (min 2.86, max 2.87)","3.21"
    "lat_ops-float-div (ns)","10.43 (min 10.42, max 10.43)","9.30","10.42 (min 10.42, max 10.43)"
    "lat_ops-float-mul (ns)","3.21 (min 3.20, max 3.21)","2.86","3.21"
    "lat_ops-int-add (ns)","0.80","0.72","0.80"
    "lat_ops-int-bit (ns)","0.53","0.48","0.53 (min 0.53, max 0.54)"
    "lat_ops-int-div (ns)","4.81 (min 4.81, max 4.82)","4.29 (min 4.29, max 4.30)","4.81"
    "lat_ops-int-mod (ns)","5.08","4.53 (min 4.53, max 4.54)","5.08 (min 5.07, max 5.08)"
    "lat_ops-int-mul (ns)","3.45 (min 3.45, max 3.46)","3.08 (min 3.07, max 3.10)","3.45 (min 3.44, max 3.46)"
    "lat_ops-int64-add (ns)","0.80","0.72","0.80"
    "lat_ops-int64-bit (ns)","0.53","0.48","0.53 (min 0.53, max 0.54)"
    "lat_ops-int64-div (ns)","7.62 (min 7.61, max 7.62)","6.80","7.62 (min 7.61, max 7.62)"
    "lat_ops-int64-mod (ns)","5.88","5.25","5.88 (min 5.87, max 5.89)"
    "lat_ops-int64-mul (ns)","3.99 (min 3.98, max 4.04)","3.56 (min 3.55, max 3.61)","3.98"
    "lat_pagefault (us)","0.80 (min 0.76, max 0.82)","0.71 (min 0.60, max 0.73)","1.26 (min 0.65, max 1.74)"
    "lat_pipe (us)","28.82 (min 28.37, max 29.43)","25.77 (min 25.50, max 26.22)","28.93 (min 28.25, max 29.53)"
    "lat_proc-exec (us)","1108.66 (min 1066.20, max 1142.00)","979.70 (min 844.00, max 1031.50)","1006.99 (min 886.29, max 1144.60)"
    "lat_proc-fork (us)","940.39 (min 880.50, max 1009.50)","831.78 (min 684.14, max 873.14)","857.04 (min 765.86, max 954.67)"
    "lat_proc-proccall (us)","0.01","0.01","0.01"
    "lat_select (us)","38.12 (min 37.94, max 38.28)","34.11 (min 33.75, max 34.40)","38.13 (min 37.96, max 38.48)"
    "lat_sem (us)","3.53 (min 2.89, max 4.27)","3.09 (min 2.59, max 3.54)","3.36 (min 2.96, max 3.84)"
    "lat_sig-catch (us)","6.23 (min 6.03, max 6.45)","5.52 (min 5.27, max 5.68)","6.18 (min 5.95, max 6.37)"
    "lat_sig-install (us)","0.74 (min 0.72, max 0.79)","0.66 (min 0.65, max 0.70)","0.75 (min 0.72, max 0.79)"
    "lat_sig-prot (us)","0.71 (min 0.55, max 0.93)","0.65 (min 0.48, max 0.80)","0.83 (min 0.58, max 1.48)"
    "lat_syscall-fstat (us)","2.21 (min 2.14, max 2.32)","1.98 (min 1.89, max 2.10)","2.22 (min 2.12, max 2.32)"
    "lat_syscall-null (us)","0.51 (min 0.51, max 0.52)","0.46 (min 0.46, max 0.50)","0.52 (min 0.51, max 0.56)"
    "lat_syscall-open (us)","214.57 (min 153.03, max 305.39)","175.20 (min 155.95, max 202.88)","174.43 (min 153.94, max 210.15)"
    "lat_syscall-read (us)","0.92 (min 0.90, max 0.99)","0.82 (min 0.80, max 0.88)","0.92 (min 0.90, max 0.99)"
    "lat_syscall-stat (us)","5.37 (min 5.23, max 5.53)","4.80 (min 4.66, max 5.01)","5.39 (min 5.25, max 5.60)"
    "lat_syscall-write (us)","0.86 (min 0.84, max 0.89)","0.78 (min 0.75, max 0.84)","0.87 (min 0.84, max 0.94)"
    "lat_tcp (us)","1.02","0.92 (min 0.91, max 0.97)","1.03 (min 1.02, max 1.09)"
    "lat_unix (us)","33.40 (min 32.86, max 34.65)","29.79 (min 28.64, max 30.84)","33.61 (min 33.07, max 34.90)"
    "latency_for_0.50_mb_block_size (nanosec)","17.11 (min 11.46, max 21.66)","17.27 (min 13.44, max 20.26)","15.35 (min 10.09, max 21.82)"
    "latency_for_1.00_mb_block_size (nanosec)","28.48 (min 0.00, max 58.01)","25.22 (min 0.00, max 52.51)","24.41 (min 0.00, max 54.17)"
    "pipe_bandwidth (mb\s)","443.15 (min 435.10, max 453.94)","515.70 (min 492.51, max 600.38)","498.69 (min 451.80, max 545.64)"
    "pipe_latency (microsec)","28.82 (min 28.37, max 29.43)","25.77 (min 25.50, max 26.22)","28.93 (min 28.25, max 29.53)"
    "procedure_call (microsec)","0.01","0.01","0.01"
    "select_on_200_tcp_fds (microsec)","38.12 (min 37.94, max 38.28)","34.11 (min 33.75, max 34.40)","38.13 (min 37.96, max 38.48)"
    "semaphore_latency (microsec)","3.53 (min 2.89, max 4.27)","3.09 (min 2.59, max 3.54)","3.36 (min 2.96, max 3.84)"
    "signal_handler_latency (microsec)","0.74 (min 0.72, max 0.79)","0.66 (min 0.65, max 0.70)","0.75 (min 0.72, max 0.79)"
    "signal_handler_overhead (microsec)","6.23 (min 6.03, max 6.45)","5.52 (min 5.27, max 5.68)","6.18 (min 5.95, max 6.37)"
    "tcp_ip_connection_cost_to_localhost (microsec)","66.67 (min 66.20, max 67.85)","59.11 (min 58.18, max 59.76)","65.67 (min 63.87, max 69.00)"
    "tcp_latency_using_localhost (microsec)","1.02","0.92 (min 0.91, max 0.97)","1.03 (min 1.02, max 1.09)"

Dhrystone
^^^^^^^^^
Dhrystone is a core only benchmark that runs from warm L1 caches in all
modern processors. It scales linearly with clock speed.

Please take note, different run may produce different slightly results.
This is advised to run this test multiple times in order to get maximum 
performance numbers.

Execute the benchmark with the following:

::

    runDhrystone

.. csv-table:: Dhrystone Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cpu_clock (mhz)","1250.00","1400.00","1250.00"
    "dhrystone_per_mhz (dmips/mhz)","2.84 (min 2.80, max 2.90)","2.90","2.86 (min 2.80, max 2.90)"
    "dhrystone_per_second (dhrystonep)","6336405.57 (min 6250000.00, max 6451613.00)","7142857.00","6376008.13 (min 6250000.00, max 6451613.00)"

Whetstone
^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "whetstone (mips)","5000.00","5000.00","5000.00"

Linpack
^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "linpack (kflops)","513733.00 (min 511865.00, max 515438.00)","577158.63 (min 576063.00, max 577662.00)","515214.00 (min 513050.00, max 516718.00)"

NBench
^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "assignment (iterations)","12.92 (min 12.80, max 12.95)","14.49 (min 14.44, max 14.53)","12.93 (min 12.85, max 12.96)"
    "fourier (iterations)","20380.88 (min 20371.00, max 20385.00)","22828.75 (min 22827.00, max 22831.00)","20383.88 (min 20381.00, max 20385.00)"
    "fp_emulation (iterations)","192.50 (min 192.47, max 192.52)","215.61 (min 215.57, max 215.65)","192.52 (min 192.49, max 192.54)"
    "huffman (iterations)","1057.11 (min 1056.50, max 1057.40)","1183.90 (min 1183.30, max 1184.30)","1057.24 (min 1056.70, max 1057.40)"
    "idea (iterations)","3075.31 (min 3074.90, max 3075.60)","3444.45 (min 3444.20, max 3444.80)","3075.58 (min 3075.30, max 3075.70)"
    "lu_decomposition (iterations)","472.14 (min 469.83, max 473.70)","527.41 (min 522.26, max 529.95)","472.13 (min 469.78, max 473.74)"
    "neural_net (iterations)","7.73 (min 7.72, max 7.73)","8.65 (min 8.64, max 8.66)","7.72 (min 7.71, max 7.73)"
    "numeric_sort (iterations)","559.47 (min 553.45, max 562.47)","625.06 (min 616.37, max 629.09)","559.74 (min 550.44, max 561.86)"
    "string_sort (iterations)","146.35 (min 146.33, max 146.37)","163.92 (min 163.91, max 163.94)","146.36 (min 146.35, max 146.37)"

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
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "add (mb/s)","1403.63 (min 1363.30, max 1452.60)","1628.69 (min 1443.40, max 1805.40)","1690.80 (min 1688.10, max 1693.80)"
    "copy (mb/s)","1471.36 (min 1421.90, max 1537.40)","1877.63 (min 1635.60, max 2125.00)","1869.34 (min 1836.10, max 1926.50)"
    "scale (mb/s)","1605.57 (min 1561.70, max 1663.20)","2031.11 (min 1793.40, max 2270.80)","1937.30 (min 1923.80, max 1949.60)"
    "triad (mb/s)","1378.53 (min 1343.40, max 1423.00)","1676.24 (min 1479.30, max 1872.10)","1656.76 (min 1651.70, max 1662.10)"

CoreMarkPro
^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","37.30 (min 37.17, max 37.45)","41.84 (min 41.67, max 42.02)","37.38 (min 36.90, max 37.59)"
    "core (workloads/)","0.27","0.30","0.27"
    "coremark-pro ()","784.22 (min 761.93, max 799.55)","874.96 (min 849.21, max 918.16)","800.81 (min 770.03, max 828.46)"
    "linear_alg-mid-100x100-sp (workloads/)","13.10 (min 13.09, max 13.11)","14.68 (min 14.66, max 14.70)","13.10 (min 13.09, max 13.11)"
    "loops-all-mid-10k-sp (workloads/)","0.59 (min 0.59, max 0.60)","0.67 (min 0.66, max 0.70)","0.62 (min 0.60, max 0.63)"
    "nnet_test (workloads/)","0.97","1.09 (min 1.08, max 1.09)","0.97"
    "parser-125k (workloads/)","7.38 (min 7.30, max 7.46)","8.30 (min 8.20, max 8.62)","7.64 (min 7.41, max 7.75)"
    "radix2-big-64k (workloads/)","42.96 (min 33.97, max 51.13)","46.53 (min 35.36, max 63.36)","46.38 (min 36.20, max 60.27)"
    "sha-test (workloads/)","71.81 (min 70.92, max 71.94)","80.56 (min 80.00, max 80.65)","72.14 (min 71.43, max 72.46)"
    "zip-test (workloads/)","18.52","20.84 (min 20.41, max 21.28)","18.96 (min 18.52, max 19.23)"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","73.92 (min 73.53, max 74.07)","82.82 (min 81.97, max 83.33)","74.28 (min 73.53, max 74.63)"
    "core (workloads/)","0.54","0.60","0.54"
    "coremark-pro ()","1335.06 (min 1324.28, max 1347.82)","1527.89 (min 1465.32, max 1576.42)","1407.68 (min 1356.48, max 1438.96)"
    "linear_alg-mid-100x100-sp (workloads/)","26.18 (min 26.16, max 26.19)","29.33 (min 29.31, max 29.36)","26.19 (min 26.12, max 26.21)"
    "loops-all-mid-10k-sp (workloads/)","1.03 (min 1.02, max 1.05)","1.19 (min 1.14, max 1.24)","1.11 (min 1.04, max 1.13)"
    "nnet_test (workloads/)","1.94 (min 1.93, max 1.94)","2.17","1.94 (min 1.93, max 1.94)"
    "parser-125k (workloads/)","10.55 (min 10.26, max 10.93)","12.28 (min 11.05, max 13.42)","11.24 (min 10.00, max 12.12)"
    "radix2-big-64k (workloads/)","35.17 (min 33.06, max 38.93)","44.61 (min 36.64, max 51.47)","47.05 (min 40.80, max 50.65)"
    "sha-test (workloads/)","142.86","160.01 (min 158.73, max 161.29)","143.89 (min 142.86, max 144.93)"
    "zip-test (workloads/)","34.49 (min 33.90, max 35.09)","39.14 (min 37.74, max 40.00)","35.96 (min 35.09, max 36.36)"

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
Multi-Instance-Test Harness (MITH), compatible and portable with most any multicore
processors and operating systems. MITH uses a thread-based API (POSIX-compliant) to
establish a common programming model that communicates with the benchmark through an
abstraction layer and provides a flexible interface to allow a wide variety of
thread-enabled workloads to be tested.

.. csv-table:: Multibench Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "4m-check (workloads/)","274.66 (min 267.24, max 283.06)","342.64 (min 302.01, max 368.24)","302.78 (min 279.33, max 340.88)"
    "4m-check-reassembly (workloads/)","58.33 (min 56.63, max 60.42)","72.79 (min 62.42, max 80.13)","63.46 (min 56.21, max 74.35)"
    "4m-check-reassembly-tcp (workloads/)","37.86 (min 36.82, max 38.76)","46.33 (min 41.32, max 49.80)","41.02 (min 37.48, max 46.04)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","21.83 (min 21.34, max 22.42)","27.22 (min 23.86, max 29.30)","24.15 (min 22.35, max 27.04)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.59 (min 1.58, max 1.61)","1.80 (min 1.76, max 1.84)","1.62 (min 1.59, max 1.66)"
    "4m-cmykw2 (workloads/)","178.88 (min 173.61, max 184.50)","220.64 (min 194.55, max 242.13)","192.61 (min 172.86, max 216.45)"
    "4m-cmykw2-rotatew2 (workloads/)","35.01 (min 34.05, max 35.93)","44.14 (min 38.78, max 47.58)","37.56 (min 33.82, max 41.81)"
    "4m-reassembly (workloads/)","46.17 (min 43.86, max 51.57)","57.21 (min 49.58, max 61.27)","50.47 (min 45.79, max 57.44)"
    "4m-rotatew2 (workloads/)","40.02 (min 39.09, max 41.03)","49.21 (min 44.25, max 52.47)","43.68 (min 40.95, max 47.92)"
    "4m-tcp-mixed (workloads/)","93.04 (min 91.43, max 95.24)","110.80 (min 103.90, max 115.11)","97.63 (min 93.02, max 104.58)"
    "4m-x264w2 (workloads/)","1.63 (min 1.56, max 1.65)","1.87 (min 1.81, max 1.91)","1.65 (min 1.58, max 1.70)"
    "empty-wld (workloads/)","1.00","1.00","1.00"
    "idct-4m (workloads/)","16.71 (min 16.49, max 16.78)","18.89 (min 18.56, max 19.11)","16.89 (min 16.78, max 17.10)"
    "idct-4mw1 (workloads/)","16.71 (min 16.49, max 16.79)","18.89 (min 18.56, max 19.11)","16.91 (min 16.76, max 17.10)"
    "ippktcheck-4m (workloads/)","274.52 (min 265.53, max 283.67)","340.93 (min 303.62, max 364.38)","302.69 (min 280.36, max 339.58)"
    "ippktcheck-4mw1 (workloads/)","274.24 (min 267.87, max 282.61)","342.81 (min 303.21, max 368.08)","302.30 (min 278.27, max 338.89)"
    "ipres-4m (workloads/)","58.88 (min 56.58, max 61.63)","73.72 (min 63.94, max 79.79)","66.26 (min 60.61, max 74.85)"
    "ipres-4mw1 (workloads/)","58.64 (min 56.97, max 60.66)","73.94 (min 64.16, max 80.30)","66.06 (min 60.68, max 74.55)"
    "md5-4m (workloads/)","21.83 (min 21.29, max 22.23)","25.41 (min 24.13, max 26.17)","22.62 (min 21.41, max 23.98)"
    "md5-4mw1 (workloads/)","22.12 (min 21.82, max 22.44)","25.67 (min 24.51, max 26.52)","22.83 (min 22.00, max 24.08)"
    "rgbcmyk-4m (workloads/)","56.75 (min 56.35, max 57.18)","64.33 (min 63.35, max 65.02)","56.81 (min 56.58, max 57.05)"
    "rgbcmyk-4mw1 (workloads/)","56.65 (min 56.37, max 57.14)","64.40 (min 63.33, max 65.08)","56.79 (min 56.66, max 57.05)"
    "rotate-4ms1 (workloads/)","16.66 (min 16.20, max 17.15)","20.43 (min 18.28, max 21.82)","18.07 (min 16.78, max 20.02)"
    "rotate-4ms1w1 (workloads/)","16.68 (min 16.31, max 17.16)","20.58 (min 18.29, max 22.77)","18.09 (min 16.95, max 20.03)"
    "rotate-4ms64 (workloads/)","16.83 (min 16.47, max 17.25)","20.60 (min 18.40, max 22.02)","18.26 (min 17.09, max 20.15)"
    "rotate-4ms64w1 (workloads/)","16.82 (min 16.46, max 17.25)","20.76 (min 18.34, max 23.08)","18.28 (min 17.10, max 20.20)"
    "x264-4mq (workloads/)","0.50","0.57 (min 0.56, max 0.57)","0.50 (min 0.50, max 0.51)"
    "x264-4mqw1 (workloads/)","0.50","0.56 (min 0.56, max 0.57)","0.50 (min 0.50, max 0.51)"

Boot-time Measurement
---------------------

Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62xx_lp_sk-fs: Boot time in seconds: avg(min,max)","am62xx_sk-fs: Boot time in seconds: avg(min,max)","am62xxsip_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","17.36 (min 15.98, max 25.46)","16.20 (min 14.74, max 22.20)","15.91 (min 14.98, max 25.80)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

ALSA SoC Audio Driver
---------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)","am62xxsip_sk-fs: Throughput (bits/sec)","am62xxsip_sk-fs: CPU Load (%)"

    "11025","352792.79 (min 352756.00, max 352798.00)","0.19 (min 0.13, max 0.67)","352798.88 (min 352798.00, max 352801.00)","0.13 (min 0.11, max 0.19)","352798.25 (min 352797.00, max 352800.00)","0.14 (min 0.11, max 0.18)"
    "16000","511993.07 (min 511964.00, max 511998.00)","0.19 (min 0.11, max 0.55)","511999.38 (min 511997.00, max 512002.00)","0.11 (min 0.09, max 0.17)","511998.17 (min 511996.00, max 512002.00)","0.17 (min 0.08, max 0.33)"
    "22050","705595.14 (min 705591.00, max 705613.00)","0.19 (min 0.16, max 0.24)","705594.50 (min 705591.00, max 705597.00)","0.16 (min 0.15, max 0.21)","705594.42 (min 705589.00, max 705600.00)","0.17 (min 0.14, max 0.22)"
    "24000","705593.71 (min 705585.00, max 705596.00)","0.21 (min 0.18, max 0.28)","705596.75 (min 705595.00, max 705599.00)","0.19 (min 0.16, max 0.25)","705596.33 (min 705594.00, max 705600.00)","0.19 (min 0.14, max 0.25)"
    "32000","1023989.36 (min 1023960.00, max 1023994.00)","0.14 (min 0.10, max 0.26)","1023996.25 (min 1023993.00, max 1023999.00)","0.12 (min 0.10, max 0.17)","1023995.50 (min 1023992.00, max 1024002.00)","0.18 (min 0.09, max 0.75)"
    "44100","1411184.36 (min 1411137.00, max 1411193.00)","0.29 (min 0.26, max 0.35)","1411195.00 (min 1411191.00, max 1411199.00)","0.26 (min 0.23, max 0.31)","1411193.67 (min 1411188.00, max 1411203.00)","0.26 (min 0.23, max 0.32)"
    "48000","1535982.00 (min 1535927.00, max 1535992.00)","0.30 (min 0.11, max 1.33)","1535994.50 (min 1535990.00, max 1535999.00)","0.15 (min 0.10, max 0.26)","1535993.17 (min 1535987.00, max 1536003.00)","0.27 (min 0.10, max 0.92)"
    "88200","2822360.21 (min 2822256.00, max 2822378.00)","0.52 (min 0.45, max 0.59)","2822385.38 (min 2822376.00, max 2822395.00)","0.49 (min 0.44, max 0.59)","2822380.33 (min 2822369.00, max 2822401.00)","0.48 (min 0.38, max 0.56)"
    "96000","3071963.64 (min 3071875.00, max 3071978.00)","0.25 (min 0.17, max 0.50)","3071983.00 (min 3071971.00, max 3071992.00)","0.24 (min 0.19, max 0.39)","3071976.00 (min 3071954.00, max 3071998.00)","0.32 (min 0.16, max 1.26)"

.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)","am62xxsip_sk-fs: Throughput (bits/sec)","am62xxsip_sk-fs: CPU Load (%)"

    "11025","352945.43 (min 352945.00, max 352947.00)","0.13 (min 0.12, max 0.14)","352946.86 (min 352946.00, max 352949.00)","0.13 (min 0.09, max 0.17)","352946.13 (min 352945.00, max 352948.00)","0.19 (min 0.09, max 0.32)"
    "16000","512212.00 (min 512211.00, max 512213.00)","0.20 (min 0.11, max 0.54)","512213.29 (min 512211.00, max 512216.00)","0.13 (min 0.08, max 0.30)","512213.25 (min 512211.00, max 512216.00)","0.20 (min 0.10, max 0.31)"
    "22050","705887.71 (min 705885.00, max 705892.00)","0.16 (min 0.15, max 0.17)","705888.71 (min 705885.00, max 705891.00)","0.14 (min 0.11, max 0.21)","705888.88 (min 705888.00, max 705890.00)","0.21 (min 0.12, max 0.35)"
    "24000","705889.86 (min 705888.00, max 705892.00)","0.18 (min 0.17, max 0.19)","705891.57 (min 705890.00, max 705893.00)","0.17 (min 0.12, max 0.22)","705891.63 (min 705889.00, max 705894.00)","0.24 (min 0.14, max 0.37)"
    "32000","1024421.71 (min 1024419.00, max 1024423.00)","0.14 (min 0.13, max 0.15)","1024424.57 (min 1024422.00, max 1024426.00)","0.13 (min 0.09, max 0.21)","1024424.25 (min 1024420.00, max 1024429.00)","0.19 (min 0.10, max 0.30)"
    "44100","1411749.57 (min 1411554.00, max 1411783.00)","0.23 (min 0.21, max 0.25)","1411755.43 (min 1411579.00, max 1411787.00)","0.20 (min 0.16, max 0.26)","1411785.25 (min 1411779.00, max 1411793.00)","0.27 (min 0.18, max 0.38)"
    "48000","1536632.83 (min 1536629.00, max 1536635.00)","0.26 (min 0.11, max 0.69)","1536637.57 (min 1536633.00, max 1536640.00)","0.16 (min 0.09, max 0.21)","1536636.00 (min 1536630.00, max 1536640.00)","0.29 (min 0.11, max 0.45)"
    "88200","2823558.00 (min 2823550.00, max 2823562.00)","0.39 (min 0.38, max 0.42)","2823567.00 (min 2823558.00, max 2823572.00)","0.37 (min 0.32, max 0.41)","2823443.00 (min 2822703.00, max 2823573.00)","0.44 (min 0.34, max 0.58)"
    "96000","3073257.40 (min 3073251.00, max 3073262.00)","0.25 (min 0.20, max 0.28)","3073268.57 (min 3073258.00, max 3073274.00)","0.22 (min 0.17, max 0.28)","3073266.57 (min 3073255.00, max 3073276.00)","0.35 (min 0.20, max 0.63)"

|

Graphics SGX/RGX Driver
-----------------------

GFXBench
^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_lp_sk-fs: Fps","am62xx_sk-fs: Score","am62xx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","81.66 (min 80.20, max 82.31)","1.32 (min 1.29, max 1.33)"
    " GFXBench 3.x gl_trex_off","123.00 (min 120.86, max 125.32)","2.20 (min 2.16, max 2.24)"
    " GFXBench 5.x gl_5_high_off","11.20 (min 11.14, max 11.28)","0.17 (min 0.17, max 0.18)","11.76 (min 11.60, max 11.89)","0.18"

Glmark2
^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_sk-fs: Score","am62xxsip_sk-fs: Score"

    "Glmark2-DRM","59.00 (min 51.00, max 70.00)","61.00","54.00"
    "Glmark2-Wayland","199.00 (min 198.00, max 203.00)","216.00","208.75 (min 208.00, max 209.00)"
    "Glmark2-Wayland 1920x1080","62.57 (min 62.00, max 63.00)","66.29 (min 66.00, max 67.00)"

|


Ethernet
-----------------
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

- CPSW2g: AM65x, J7200, J721e, J721S2, J784S4, J742S2
- CPSW3g: AM64x, AM62x, AM62ax, AM62px

.. rubric::  TCP Bidirectional Throughput
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1698.44 (min 1628.06, max 1800.35)","67.30 (min 64.15, max 72.01)","1783.17 (min 1762.43, max 1798.15)","67.94 (min 65.84, max 69.35)","1658.66 (min 1180.00, max 1849.79)","66.19 (min 55.35, max 71.09)"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1630.25 (min 1484.82, max 1709.62)","59.65 (min 50.43, max 84.96)","1604.35 (min 301.65, max 1837.36)","47.99 (min 14.99, max 55.09)","1840.19 (min 1813.97, max 1870.78)","54.44 (min 50.41, max 57.84)"

.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","45.17 (min 42.87, max 45.99)","88.22 (min 84.00, max 90.00)","39.84 (min 25.15, max 63.81)","","42.93 (min 26.73, max 54.34)","83.86 (min 52.00, max 106.00)","30.70 (min 12.22, max 39.15)","","47.46 (min 45.64, max 48.58)","92.75 (min 89.00, max 95.00)","39.02 (min 38.09, max 39.68)"
    "128","82.00","87.45 (min 81.17, max 89.93)","85.25 (min 79.00, max 88.00)","44.32 (min 37.82, max 62.92)","","90.95 (min 17.31, max 102.75)","88.70 (min 17.00, max 100.00)","34.13 (min 9.70, max 38.73)","","95.20 (min 89.43, max 97.29)","93.00 (min 87.00, max 95.00)","39.06 (min 38.06, max 39.81)"
    "256","210.00","172.10 (min 156.28, max 178.99)","83.89 (min 76.00, max 87.00)","43.40 (min 37.59, max 62.50)","","200.58 (min 195.49, max 213.41)","97.71 (min 95.00, max 104.00)","38.57 (min 38.11, max 39.49)","","185.76 (min 178.48, max 190.50)","90.57 (min 87.00, max 93.00)","38.56 (min 38.29, max 38.82)"
    "1024","978.00","610.03 (min 286.71, max 692.59)","74.57 (min 35.00, max 85.00)","37.81 (min 15.50, max 61.34)","","627.48 (min 46.69, max 807.16)","76.78 (min 6.00, max 99.00)","30.94 (min 0.92, max 38.45)","","700.39 (min 683.61, max 736.41)","85.25 (min 83.00, max 90.00)","38.01 (min 37.61, max 38.45)"
    "1518","1472.00","530.95 (min 183.19, max 697.98)","43.63 (min 15.00, max 57.00)","35.51 (min 11.05, max 60.04)","","757.07 (min 611.07, max 823.49)","62.33 (min 50.00, max 68.00)","35.49 (min 32.74, max 36.36)","","692.69 (min 529.45, max 741.46)","57.13 (min 44.00, max 61.00)","35.56 (min 30.07, max 40.87)"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","2.27 (min 1.38, max 2.66)","4.33 (min 3.00, max 5.00)","1.77 (min 0.74, max 3.49)","","1.52 (min 1.38, max 1.54)","3.00","0.88 (min 0.62, max 1.82)","","1.92 (min 1.38, max 2.71)","3.89 (min 3.00, max 5.00)","1.18 (min 0.58, max 2.47)"
    "128","82.00","5.28 (min 5.12, max 5.43)","5.00","2.32 (min 1.08, max 4.15)","","4.51","4.00","1.19 (min 0.85, max 2.88)","","4.73 (min 4.10, max 5.32)","4.57 (min 4.00, max 5.00)","0.99 (min 0.76, max 1.18)"
    "256","210.00","10.38 (min 9.83, max 10.85)","5.00","2.01 (min 1.04, max 3.87)","","11.06 (min 9.83, max 16.18)","5.50 (min 5.00, max 8.00)","1.76 (min 1.05, max 3.74)","","10.32 (min 9.20, max 10.85)","4.80 (min 4.00, max 5.00)","1.06 (min 0.98, max 1.15)"
    "1024","978.00","43.15 (min 42.60, max 43.42)","5.00","3.05 (min 1.38, max 5.13)","","43.07 (min 42.60, max 44.23)","5.00","2.44 (min 1.48, max 3.70)","","189.01 (min 27.85, max 935.80)","22.83 (min 3.00, max 114.00)","8.78 (min 1.39, max 42.77)"
    "1518","1472.00","61.97 (min 61.23, max 62.41)","5.00","3.53 (min 1.95, max 4.71)","","62.18 (min 61.23, max 63.59)","5.00","3.07 (min 1.84, max 4.74)","","225.77 (min 28.26, max 941.32)","19.00 (min 2.00, max 80.00)","11.77 (min 1.97, max 42.15)"

.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_lp_sk-fs: Packet Loss %","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: Packet Loss %","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: Packet Loss %"

    "64","18.00","78.62 (min 69.58, max 88.72)","153.56 (min 136.00, max 173.00)","48.04 (min 39.65, max 69.17)","52.00 (min 0.03, max 80.01)","","96.29 (min 89.66, max 97.42)","188.13 (min 175.00, max 190.00)","42.55 (min 39.69, max 44.43)","47.53 (min 31.90, max 64.49)","","83.77 (min 61.91, max 91.66)","163.56 (min 121.00, max 179.00)","42.08 (min 40.20, max 43.92)","71.27 (min 65.75, max 77.58)"
    "128","82.00","166.41 (min 141.23, max 171.82)","162.57 (min 138.00, max 168.00)","43.50 (min 40.85, max 45.21)","45.31 (min 0.18, max 62.80)","","192.35 (min 182.52, max 194.35)","187.89 (min 178.00, max 190.00)","40.78 (min 33.34, max 46.88)","48.04 (min 28.69, max 70.54)","","170.66 (min 161.89, max 179.10)","166.71 (min 158.00, max 175.00)","43.01 (min 41.89, max 44.60)","66.48 (min 46.79, max 74.38)"
    "256","210.00","302.93 (min 274.45, max 334.43)","147.89 (min 134.00, max 163.00)","48.96 (min 40.52, max 69.72)","28.02 (min 0.35, max 61.23)","","365.04 (min 343.99, max 374.14)","178.33 (min 168.00, max 183.00)","43.26 (min 41.74, max 44.53)","47.95 (min 40.06, max 53.04)","","285.42 (min 148.67, max 331.95)","139.40 (min 73.00, max 162.00)","42.81 (min 39.40, max 44.21)","46.03 (min 16.49, max 58.26)"
    "1024","978.00","815.64 (min 461.33, max 935.09)","99.56 (min 56.00, max 114.00)","44.65 (min 38.28, max 68.37)","0.31 (min 0.07, max 0.81)","","889.38 (min 838.56, max 935.45)","108.43 (min 102.00, max 114.00)","42.69 (min 39.75, max 45.31)","0.43 (min 0.06, max 0.90)","","817.58 (min 732.19, max 908.97)","99.83 (min 89.00, max 111.00)","41.74 (min 40.22, max 43.02)","0.48 (min 0.09, max 0.89)"
    "1518","1472.00","847.13 (min 748.02, max 945.15)","72.00 (min 64.00, max 80.00)","43.54 (min 35.25, max 68.38)","0.43 (min 0.03, max 1.40)","","881.34 (min 797.89, max 922.82)","74.80 (min 68.00, max 78.00)","40.02 (min 35.44, max 42.18)","0.34 (min 0.16, max 0.49)","","922.03 (min 879.70, max 955.84)","78.29 (min 75.00, max 81.00)","41.81 (min 39.60, max 43.08)","0.41 (min 0.00, max 0.77)"

|

Linux OSPI Flash Driver
-----------------------

.. rubric:: AM62XX-SK
   :name: am62xx-sk-ospi-flash-driver

.. rubric:: RAW
   :name: am62xx-sk-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xx_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","170.77 (min 166.67, max 172.41)"

.. rubric:: RAW
   :name: am62xx-sk-lp-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xx_lp_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","29.24 (min 28.73, max 29.59)"

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

    "1m","55.21 (min 43.80, max 90.90)","1.48 (min 1.08, max 2.52)","174.00 (min 171.00, max 175.00)","2.05 (min 1.79, max 2.27)"
    "4m","56.05 (min 43.70, max 96.40)","1.11 (min 0.80, max 1.78)","174.00 (min 171.00, max 175.00)","1.65 (min 1.46, max 1.87)"
    "4k","29.97 (min 5.31, max 63.60)","10.46 (min 2.06, max 22.72)","50.86 (min 36.30, max 93.30)","13.38 (min 9.65, max 23.05)"
    "256k","50.74 (min 35.00, max 91.30)","1.69 (min 1.11, max 2.90)","173.63 (min 171.00, max 174.00)","2.68 (min 2.25, max 2.96)"

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","49.95 (min 42.90, max 58.90)","1.58 (min 1.28, max 1.85)","174.50 (min 174.00, max 175.00)","2.37 (min 1.96, max 2.55)"
    "4m","49.89 (min 43.10, max 58.90)","1.27 (min 0.98, max 1.86)","174.70 (min 174.00, max 175.00)","1.91 (min 1.63, max 2.35)"
    "4k","23.80 (min 5.24, max 51.70)","9.27 (min 2.38, max 19.72)","44.31 (min 36.40, max 56.30)","13.52 (min 11.10, max 16.93)"
    "256k","44.37 (min 34.20, max 58.80)","1.75 (min 1.31, max 2.31)","174.00","3.09 (min 2.66, max 3.23)"

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "1m","92.76 (min 91.00, max 95.90)","2.53 (min 2.25, max 2.94)","171.75 (min 171.00, max 174.00)","2.55 (min 2.22, max 2.87)"
    "4m","96.81 (min 92.20, max 98.00)","2.27 (min 2.05, max 2.53)","165.75 (min 141.00, max 173.00)","2.53 (min 2.11, max 2.84)"
    "4k","64.16 (min 63.70, max 64.50)","24.79 (min 24.52, max 25.21)","92.38 (min 91.60, max 92.80)","24.06 (min 23.88, max 24.22)"
    "256k","91.96 (min 91.00, max 92.80)","2.63 (min 2.38, max 2.93)","171.00 (min 170.00, max 173.00)","2.92 (min 2.64, max 3.14)"

EMMC EXT4
^^^^^^^^^

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","47.27 (min 39.38, max 68.59)","4.63 (min 3.08, max 8.55)","172.03 (min 142.58, max 179.51)","12.04 (min 10.43, max 14.23)"
    "262144","46.33 (min 39.08, max 69.36)","4.62 (min 3.09, max 8.92)","171.71 (min 98.67, max 183.00)","12.59 (min 5.84, max 14.54)"
    "524288","46.07 (min 39.39, max 69.29)","4.66 (min 3.27, max 8.86)","176.20 (min 132.59, max 182.99)","12.90 (min 9.65, max 14.54)"
    "1048576","45.97 (min 38.94, max 67.84)","4.48 (min 3.09, max 8.61)","177.23 (min 139.09, max 182.88)","13.66 (min 10.74, max 15.35)"
    "5242880","46.19 (min 39.09, max 68.52)","4.48 (min 2.89, max 8.63)","176.56 (min 136.16, max 182.81)","13.55 (min 11.04, max 15.65)"

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "102400","46.20 (min 39.42, max 53.63)","5.41 (min 3.80, max 7.72)","175.55 (min 167.93, max 177.22)","14.04 (min 13.30, max 14.77)"
    "262144","45.84 (min 39.01, max 52.84)","5.56 (min 4.45, max 7.78)","180.66 (min 180.04, max 181.28)","16.55 (min 15.93, max 17.83)"
    "524288","45.78 (min 39.45, max 52.65)","5.57 (min 4.50, max 7.95)","182.34 (min 181.72, max 182.77)","17.30 (min 16.67, max 18.26)"
    "1048576","45.98 (min 39.10, max 53.29)","5.48 (min 4.24, max 7.77)","181.96 (min 181.42, max 182.45)","17.45 (min 16.74, max 19.48)"
    "5242880","46.10 (min 39.39, max 52.97)","5.41 (min 4.42, max 7.81)","181.51 (min 180.56, max 182.12)","17.27 (min 16.37, max 18.26)"

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "102400","92.90 (min 35.38, max 100.03)","12.70 (min 5.91, max 26.68)","178.51 (min 178.00, max 178.87)","12.36 (min 10.82, max 14.41)"
    "262144","78.13 (min 30.00, max 97.55)","7.26 (min 2.26, max 17.43)","180.57 (min 180.08, max 181.05)","13.93 (min 12.66, max 15.42)"
    "524288","77.25 (min 32.87, max 96.72)","6.82 (min 2.00, max 12.76)","181.08 (min 179.75, max 181.56)","14.21 (min 12.61, max 16.81)"
    "1048576","75.27 (min 32.45, max 97.43)","6.62 (min 2.05, max 12.64)","181.08 (min 180.11, max 181.60)","13.54 (min 12.28, max 16.67)"
    "5242880","73.92 (min 28.97, max 96.92)","6.62 (min 2.03, max 13.75)","180.86 (min 179.21, max 181.48)","13.65 (min 12.55, max 15.95)"

EMMC VFAT
^^^^^^^^^

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xx_sk-fs: Write VFAT CPU Load (%)","am62xx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xx_sk-fs: Read VFAT CPU Load (%)"

    "102400","41.99 (min 33.56, max 50.47)","5.63 (min 3.71, max 8.96)","168.88 (min 167.46, max 171.01)","12.46 (min 11.43, max 13.47)"
    "262144","43.21 (min 34.82, max 51.89)","5.89 (min 4.06, max 8.84)","170.74 (min 170.03, max 172.53)","14.81 (min 12.50, max 15.98)"
    "524288","43.26 (min 34.68, max 51.97)","5.92 (min 3.98, max 9.32)","169.14 (min 168.50, max 170.91)","14.50 (min 12.65, max 15.66)"
    "1048576","43.40 (min 35.02, max 52.21)","5.83 (min 3.98, max 9.22)","168.62 (min 167.68, max 169.36)","14.54 (min 12.60, max 15.73)"
    "5242880","43.37 (min 34.99, max 52.13)","5.80 (min 3.91, max 9.17)","168.87 (min 168.10, max 170.34)","14.71 (min 11.93, max 16.06)"

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write VFAT CPU Load (%)","am62xx_lp_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read VFAT CPU Load (%)"

    "102400","40.98 (min 31.93, max 49.66)","6.24 (min 4.49, max 9.95)","167.36 (min 165.22, max 169.10)","14.86 (min 13.22, max 16.27)"
    "262144","42.56 (min 33.32, max 51.62)","6.69 (min 4.94, max 10.29)","169.22 (min 167.97, max 170.23)","17.21 (min 15.42, max 18.22)"
    "524288","42.57 (min 33.42, max 51.68)","6.73 (min 5.00, max 10.84)","167.98 (min 167.06, max 168.70)","16.59 (min 15.51, max 17.67)"
    "1048576","42.66 (min 33.48, max 51.79)","6.55 (min 4.89, max 9.98)","167.73 (min 167.03, max 168.46)","16.94 (min 15.85, max 17.74)"
    "5242880","42.78 (min 33.53, max 52.13)","6.57 (min 4.94, max 10.26)","167.31 (min 166.74, max 168.09)","16.85 (min 15.73, max 17.93)"

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write VFAT CPU Load (%)","am62xxsip_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read VFAT CPU Load (%)"

    "102400","80.24 (min 45.77, max 96.90)","16.11 (min 5.36, max 29.32)","174.50 (min 173.84, max 174.86)","12.42 (min 10.59, max 15.29)"
    "262144","73.99 (min 51.85, max 96.56)","7.98 (min 4.06, max 15.38)","175.43 (min 175.16, max 175.60)","13.91 (min 12.71, max 17.08)"
    "524288","72.90 (min 49.94, max 96.87)","7.76 (min 3.53, max 14.31)","174.89 (min 174.56, max 175.13)","13.82 (min 12.97, max 15.90)"
    "1048576","74.90 (min 49.90, max 96.59)","8.42 (min 4.81, max 15.75)","174.62 (min 174.19, max 174.99)","13.74 (min 12.66, max 16.60)"
    "5242880","75.79 (min 49.91, max 96.31)","8.88 (min 4.68, max 13.65)","174.76 (min 174.11, max 175.19)","13.69 (min 12.61, max 15.61)"

UBoot EMMC Driver
-----------------

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","53539.31 (min 13727.69, max 61134.33)","170336.22 (min 169782.38, max 171560.21)"
    "4000000","64033.22 (min 58514.29, max 95533.53)","172287.23 (min 164663.32, max 173835.54)"

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","60091.96 (min 57186.74, max 62178.37)","170371.91 (min 169782.38, max 170666.67)"
    "4000000","61147.19 (min 57893.99, max 62415.24)","165622.92 (min 100824.62, max 174297.87)"

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","86450.84 (min 13914.23, max 97523.81)","163230.55 (min 141852.81, max 172463.16)"
    "4000000","98727.53 (min 96234.95, max 101448.92)","173236.44 (min 158682.81, max 175229.95)"

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

    "1m","42.31 (min 40.80, max 43.60)","1.53 (min 1.24, max 1.69)","87.53 (min 87.30, max 88.20)","1.59 (min 1.34, max 1.72)"
    "4m","41.66 (min 40.40, max 42.40)","1.03 (min 0.92, max 1.11)","86.67 (min 82.60, max 87.50)","1.19 (min 0.94, max 1.27)"
    "4k","2.79 (min 2.76, max 2.83)","1.88 (min 1.71, max 1.99)","12.93 (min 12.80, max 13.00)","4.47 (min 4.27, max 4.71)"
    "256k","38.07 (min 36.30, max 39.10)","1.70 (min 1.40, max 1.85)","83.87 (min 83.60, max 84.30)","1.75 (min 1.60, max 1.87)"

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.51 (min 41.90, max 43.60)","1.66 (min 1.59, max 1.74)","87.04 (min 84.90, max 87.40)","1.74 (min 1.66, max 1.87)"
    "4m","42.10 (min 40.70, max 43.20)","1.16 (min 1.07, max 1.25)","86.80 (min 84.20, max 87.40)","1.27 (min 1.22, max 1.31)"
    "4k","2.79 (min 2.76, max 2.84)","2.12 (min 1.97, max 2.26)","12.90 (min 12.80, max 13.00)","4.96 (min 4.77, max 5.13)"
    "256k","37.40 (min 36.10, max 38.50)","1.83 (min 1.64, max 1.93)","83.70 (min 83.30, max 84.30)","1.99 (min 1.87, max 2.06)"

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "1m","39.39 (min 18.80, max 42.80)","1.61 (min 1.16, max 1.88)","87.29 (min 86.60, max 87.70)","1.91 (min 1.67, max 2.13)"
    "4m","38.44 (min 18.60, max 42.50)","1.34 (min 0.85, max 1.57)","87.00 (min 86.20, max 87.30)","1.78 (min 1.37, max 2.02)"
    "4k","2.96 (min 2.77, max 4.18)","2.17 (min 2.04, max 2.73)","13.00 (min 12.90, max 13.50)","4.93 (min 4.70, max 5.20)"
    "256k","35.65 (min 17.70, max 39.60)","1.69 (min 1.15, max 1.92)","83.46 (min 82.20, max 84.00)","1.91 (min 1.68, max 2.08)"

MMC EXT4
^^^^^^^^

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Write Raw CPU Load (%)","am62xx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.57 (min 10.18, max 10.82)","1.12 (min 0.89, max 1.52)","11.02 (min 10.86, max 11.09)","0.96 (min 0.85, max 1.08)"
    "262144","10.35 (min 10.13, max 10.84)","1.14 (min 0.84, max 1.65)","11.11 (min 11.00, max 11.22)","1.02 (min 0.80, max 1.22)"
    "524288","10.30 (min 10.10, max 10.73)","1.12 (min 0.85, max 1.59)","11.16 (min 10.82, max 11.45)","0.99 (min 0.85, max 1.18)"
    "1048576","10.35 (min 10.17, max 10.78)","1.16 (min 0.86, max 1.73)","11.14 (min 10.98, max 11.52)","0.97 (min 0.82, max 1.08)"
    "5242880","10.37 (min 10.13, max 10.71)","1.08 (min 0.84, max 1.58)","11.79 (min 11.23, max 12.02)","1.02 (min 0.80, max 1.20)"

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write Raw CPU Load (%)","am62xx_lp_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read Raw CPU Load (%)"

    "102400","10.53 (min 10.22, max 10.94)","1.33 (min 1.09, max 1.74)","10.99 (min 10.62, max 11.80)","1.05 (min 0.98, max 1.14)"
    "262144","10.33 (min 10.09, max 10.82)","1.37 (min 1.18, max 1.97)","11.06 (min 10.73, max 11.21)","1.22 (min 1.08, max 1.31)"
    "524288","10.31 (min 10.10, max 10.74)","1.34 (min 1.12, max 1.80)","11.16 (min 11.05, max 11.50)","1.15 (min 1.08, max 1.26)"
    "1048576","10.32 (min 10.08, max 10.72)","1.41 (min 1.15, max 1.81)","11.20 (min 10.84, max 11.50)","1.16 (min 1.09, max 1.25)"
    "5242880","10.41 (min 10.15, max 10.69)","1.31 (min 1.11, max 1.92)","11.88 (min 11.50, max 12.02)","1.20 (min 1.10, max 1.26)"

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write Raw CPU Load (%)","am62xxsip_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read Raw CPU Load (%)"

    "102400","10.42 (min 8.81, max 10.95)","1.34 (min 0.65, max 2.59)","11.17 (min 10.59, max 11.81)","1.26 (min 0.99, max 1.63)"
    "262144","10.46 (min 8.73, max 11.13)","0.97 (min 0.66, max 1.95)","11.14 (min 10.78, max 11.92)","1.14 (min 0.94, max 1.79)"
    "524288","10.48 (min 9.36, max 10.84)","0.94 (min 0.71, max 1.40)","11.23 (min 10.91, max 12.00)","1.00 (min 0.87, max 1.18)"
    "1048576","10.46 (min 9.35, max 10.92)","0.99 (min 0.74, max 1.31)","11.20 (min 10.83, max 12.01)","1.02 (min 0.85, max 1.19)"
    "5242880","10.69 (min 9.03, max 11.30)","0.91 (min 0.61, max 1.29)","11.57 (min 10.87, max 12.03)","1.07 (min 0.85, max 1.26)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","35466.05 (min 16318.73, max 40960.00)","82755.92 (min 81920.00, max 83591.84)"
    "800000","42607.92 (min 36735.43, max 46282.49)","87151.41 (min 86231.58, max 88086.02)"
    "1000000","46774.89 (min 42335.92, max 49201.20)","89653.03 (min 89530.05, max 90021.98)"

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","36399.32 (min 30567.16, max 39766.99)","82636.50 (min 81920.00, max 83591.84)"
    "800000","41351.40 (min 35008.55, max 46545.45)","87148.94"
    "1000000","48424.06 (min 44281.08, max 50103.98)","89670.60 (min 89530.05, max 90021.98)"

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","31694.74 (min 18875.58, max 39384.62)","81820.63 (min 78769.23, max 83591.84)"
    "800000","37983.33 (min 20897.96, max 45765.36)","86655.57 (min 85333.33, max 88086.02)"
    "1000000","41131.43 (min 21005.13, max 49053.89)","89444.00 (min 88562.16, max 90021.98)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

USB Driver
----------

USB Device Controller
^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)","am62xxsip_sk-fs: Throughput (MB/sec)"

    "150","33.11 (min 30.30, max 34.50)","43.23 (min 42.60, max 44.20)","44.00 (min 43.60, max 44.40)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)","am62xxsip_sk-fs: Throughput (MB/sec)"

    "150","29.70 (min 26.70, max 32.00)","41.21 (min 40.30, max 42.90)","40.01 (min 37.50, max 42.30)"

|

CRYPTO Driver
-------------

OpenSSL Performance
^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62xx_lp_sk-fs: throughput (KBytes/Sec)","am62xx_sk-fs: throughput (KBytes/Sec)","am62xxsip_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","20907.99 (min 19976.19, max 22306.47)","23639.08 (min 21773.65, max 24485.89)","22077.10 (min 21114.88, max 23049.56)"
    "aes-128-cbc","16","364.55 (min 352.28, max 374.50)","387.41 (min 379.85, max 419.58)","380.12 (min 370.18, max 392.97)"
    "aes-128-cbc","16384","116402.86 (min 113541.12, max 119870.81)","120229.89 (min 115938.65, max 131110.23)","122670.42 (min 117544.28, max 127505.75)"
    "aes-128-cbc","256","5982.09 (min 5769.30, max 6152.11)","6286.31 (min 6142.29, max 7050.92)","6368.79 (min 6144.85, max 6681.17)"
    "aes-128-cbc","64","1497.61 (min 1441.62, max 1537.66)","1584.44 (min 1541.50, max 1818.71)","1617.02 (min 1536.41, max 1708.99)"
    "aes-128-cbc","8192","88300.89 (min 85458.94, max 91952.47)","93108.22 (min 88402.60, max 100466.69)","92829.70 (min 89186.30, max 96419.84)"
    "aes-128-ecb","1024","21740.50 (min 20489.90, max 22819.16)","24123.86 (min 22792.87, max 25001.98)","22632.58 (min 21597.87, max 23622.31)"
    "aes-128-ecb","16","370.24 (min 357.28, max 381.93)","390.43 (min 383.62, max 431.56)","386.75 (min 377.13, max 398.98)"
    "aes-128-ecb","16384","120206.68 (min 117850.11, max 123016.53)","124764.84 (min 120045.57, max 136303.96)","126950.06 (min 121247.06, max 131765.59)"
    "aes-128-ecb","256","5999.26 (min 5773.74, max 6163.88)","6343.30 (min 6170.97, max 7289.86)","6470.59 (min 6142.12, max 6830.59)"
    "aes-128-ecb","64","1505.50 (min 1446.49, max 1541.23)","1624.92 (min 1547.71, max 1877.35)","1642.30 (min 1537.45, max 1747.48)"
    "aes-128-ecb","8192","90868.39 (min 88468.14, max 92310.19)","97160.87 (min 91930.62, max 103997.44)","95978.84 (min 92334.76, max 99461.80)"
    "aes-192-cbc","1024","20752.00 (min 19784.02, max 22273.71)","23517.06 (min 21488.64, max 24410.45)","21847.89 (min 20898.82, max 22822.57)"
    "aes-192-cbc","16","365.52 (min 353.82, max 376.50)","388.34 (min 381.74, max 421.03)","379.18 (min 369.00, max 387.85)"
    "aes-192-cbc","16384","110072.49 (min 107440.81, max 112295.94)","113373.87 (min 109625.34, max 124081.49)","116275.20 (min 112104.79, max 120176.64)"
    "aes-192-cbc","256","5979.54 (min 5767.85, max 6141.44)","6288.97 (min 6152.28, max 7104.60)","6333.77 (min 6110.21, max 6583.64)"
    "aes-192-cbc","64","1498.07 (min 1442.62, max 1538.50)","1588.33 (min 1542.44, max 1838.59)","1615.22 (min 1536.38, max 1698.15)"
    "aes-192-cbc","8192","84092.59 (min 81810.77, max 86608.55)","88387.58 (min 84429.48, max 96318.81)","89152.51 (min 85595.48, max 92646.06)"
    "aes-192-ecb","1024","21486.68 (min 20369.07, max 22924.63)","24089.77 (min 22578.52, max 25076.74)","22564.44 (min 21724.16, max 23545.86)"
    "aes-192-ecb","16","370.41 (min 358.32, max 382.93)","390.16 (min 383.19, max 431.48)","387.65 (min 379.52, max 398.96)"
    "aes-192-ecb","16384","114104.32 (min 112219.48, max 117456.90)","118111.57 (min 113617.58, max 129111.38)","120551.42 (min 114524.16, max 125572.44)"
    "aes-192-ecb","256","5993.78 (min 5765.89, max 6156.20)","6344.05 (min 6169.69, max 7315.54)","6475.15 (min 6148.18, max 6893.74)"
    "aes-192-ecb","64","1502.55 (min 1446.85, max 1541.78)","1627.19 (min 1546.43, max 1887.98)","1648.31 (min 1540.27, max 1742.19)"
    "aes-192-ecb","8192","87736.66 (min 85093.03, max 91247.96)","92213.59 (min 87569.75, max 99887.79)","92321.11 (min 88678.40, max 95783.59)"
    "aes-256-cbc","1024","20581.29 (min 19701.76, max 21914.28)","23211.82 (min 21145.26, max 24292.69)","21607.81 (min 20540.07, max 22718.46)"
    "aes-256-cbc","16","365.27 (min 351.82, max 377.43)","388.41 (min 383.25, max 419.81)","379.23 (min 368.19, max 389.95)"
    "aes-256-cbc","16384","102187.01 (min 99074.05, max 105633.11)","106252.97 (min 102176.09, max 115627.35)","107868.16 (min 102318.08, max 112678.23)"
    "aes-256-cbc","256","5974.42 (min 5769.22, max 6132.31)","6279.75 (min 6146.82, max 7036.33)","6326.14 (min 6087.85, max 6636.97)"
    "aes-256-cbc","64","1497.24 (min 1443.63, max 1538.05)","1587.18 (min 1540.95, max 1830.78)","1607.81 (min 1514.67, max 1704.75)"
    "aes-256-cbc","8192","80066.90 (min 78809.77, max 81939.11)","84246.19 (min 80595.63, max 91176.96)","84435.29 (min 80655.70, max 87881.05)"
    "aes-256-ecb","1024","21426.18 (min 20330.15, max 22955.35)","23968.47 (min 22278.83, max 24843.26)","22376.92 (min 21511.85, max 23244.80)"
    "aes-256-ecb","16","370.62 (min 359.25, max 381.87)","390.07 (min 382.78, max 431.39)","387.06 (min 379.45, max 397.67)"
    "aes-256-ecb","16384","107402.58 (min 105185.28, max 109685.42)","110622.72 (min 107080.36, max 120558.93)","112945.83 (min 108505.77, max 117036.37)"
    "aes-256-ecb","256","5992.09 (min 5767.00, max 6159.53)","6339.20 (min 6167.81, max 7293.70)","6456.95 (min 6145.62, max 6806.61)"
    "aes-256-ecb","64","1502.26 (min 1448.23, max 1542.25)","1624.00 (min 1546.86, max 1885.10)","1648.13 (min 1540.82, max 1750.91)"
    "aes-256-ecb","8192","83537.24 (min 81562.28, max 84948.31)","87660.54 (min 84374.87, max 95049.05)","87739.05 (min 84350.29, max 90947.58)"
    "sha256","1024","31667.97 (min 30793.05, max 32121.86)","36792.92 (min 36691.63, max 37363.03)","32547.50 (min 31477.76, max 33580.71)"
    "sha256","16","535.08 (min 517.10, max 544.56)","581.78 (min 574.87, max 626.29)","546.96 (min 528.06, max 563.91)"
    "sha256","16384","259375.10 (min 256791.89, max 261860.01)","294220.46 (min 292962.30, max 298920.62)","263269.72 (min 260674.90, max 268413.61)"
    "sha256","256","8403.27 (min 8144.30, max 8599.30)","9269.37 (min 9191.00, max 9772.97)","8519.69 (min 8210.35, max 8809.05)"
    "sha256","64","2118.85 (min 2050.79, max 2152.09)","2321.29 (min 2297.30, max 2466.28)","2161.82 (min 2093.80, max 2229.46)"
    "sha256","8192","175455.91 (min 172878.51, max 179773.44)","197163.69 (min 196318.55, max 202429.78)","176976.21 (min 172785.66, max 181379.07)"
    "sha512","1024","22679.64 (min 22215.00, max 23011.33)","24744.92 (min 24600.58, max 25694.21)","22754.13 (min 22400.00, max 23131.14)"
    "sha512","16","522.33 (min 501.00, max 537.31)","577.81 (min 573.24, max 601.51)","529.39 (min 512.75, max 543.56)"
    "sha512","16384","60596.22 (min 60304.04, max 60926.63)","67861.16 (min 67671.38, max 68299.43)","60706.82 (min 60342.27, max 61063.17)"
    "sha512","256","7290.51 (min 7085.40, max 7548.84)","8234.50 (min 8163.75, max 8537.43)","7490.46 (min 7222.87, max 7709.53)"
    "sha512","64","2095.92 (min 2021.93, max 2149.91)","2311.92 (min 2293.89, max 2405.40)","2119.25 (min 2058.05, max 2178.41)"
    "sha512","8192","54249.47 (min 53824.17, max 54613.33)","60518.40 (min 60325.89, max 61390.85)","54479.87 (min 53963.43, max 54910.98)"

.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62xx_lp_sk-fs: CPU Load","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: CPU Load"

    "aes-128-cbc","36.63 (min 34.00, max 38.00)","36.88 (min 35.00, max 38.00)","36.38 (min 35.00, max 37.00)"
    "aes-128-ecb","38.75 (min 36.00, max 40.00)","39.13 (min 37.00, max 40.00)","38.13 (min 36.00, max 39.00)"
    "aes-192-cbc","37.00 (min 35.00, max 39.00)","37.50 (min 36.00, max 39.00)","35.75 (min 32.00, max 38.00)"
    "aes-192-ecb","38.50 (min 36.00, max 40.00)","38.38 (min 37.00, max 40.00)","37.88 (min 36.00, max 39.00)"
    "aes-256-cbc","36.88 (min 35.00, max 38.00)","36.75 (min 35.00, max 38.00)","36.13 (min 34.00, max 38.00)"
    "aes-256-ecb","38.25 (min 36.00, max 40.00)","38.13 (min 37.00, max 39.00)","37.38 (min 35.00, max 39.00)"
    "sha256","93.75 (min 93.00, max 94.00)","94.38 (min 93.00, max 95.00)","94.50 (min 93.00, max 95.00)"
    "sha512","93.38 (min 92.00, max 94.00)","94.75 (min 94.00, max 95.00)","94.63 (min 94.00, max 95.00)"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","am62xx_sk-fs: Throughput (Mbps)","am62xx_sk-fs: Packets/Sec","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: Throughput (Mbps)","am62xxsip_sk-fs: Packets/Sec","am62xxsip_sk-fs: CPU Load"

    "aes128","121.71 (min 2.30, max 305.50)","10.57 (min 0.00, max 27.00)","48.76 (min 28.52, max 54.93)","135.97 (min 4.10, max 338.50)","11.71 (min 0.00, max 30.00)","52.73 (min 47.19, max 58.90)"
    "aes192","75.94 (min 0.20, max 228.80)","6.43 (min 0.00, max 20.00)","42.84 (min 28.19, max 50.88)","2.40 (min 2.20, max 2.60)","0.00","85.06 (min 83.00, max 87.11)"
    "aes256","188.42 (min 1.30, max 302.20)","16.33 (min 0.00, max 26.00)","48.78 (min 28.23, max 54.44)","164.90 (min 4.80, max 331.20)","14.33 (min 0.00, max 29.00)","53.12 (min 28.47, max 65.09)"
