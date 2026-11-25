.. include:: <isonum.txt>

#################################
 Linux 12.02.00 Performance Guide
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

*****************
System Benchmarks
*****************

LMBench
=======

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

   "af_unix_sock_stream_latency (microsec)","30.67 (min 27.18, max 37.00)","25.96 (min 22.81, max 32.60)","26.58 (min 22.63, max 33.38)"
   "af_unix_socket_stream_bandwidth (mb\s)","569.55 (min 558.38, max 595.69)","669.05 (min 625.62, max 769.20)","814.91 (min 713.16, max 878.56)"
   "bw_file_rd-io-1mb (mb/s)","828.47 (min 786.91, max 860.73)","979.01 (min 899.44, max 1114.62)","950.61 (min 846.88, max 1044.93)"
   "bw_file_rd-o2c-1mb (mb/s)","440.78 (min 416.67, max 461.25)","512.69 (min 477.18, max 582.84)","509.86 (min 441.63, max 576.70)"
   "bw_mem-bcopy-16mb (mb/s)","668.39 (min 654.69, max 697.56)","799.95 (min 756.79, max 919.22)","860.26 (min 744.50, max 936.71)"
   "bw_mem-bcopy-1mb (mb/s)","708.46 (min 682.13, max 752.45)","887.26 (min 804.89, max 1084.99)","910.00 (min 746.97, max 1007.22)"
   "bw_mem-bcopy-2mb (mb/s)","669.68 (min 636.44, max 705.84)","829.79 (min 751.60, max 978.79)","823.03 (min 702.25, max 914.63)"
   "bw_mem-bcopy-4mb (mb/s)","691.07 (min 677.28, max 727.27)","847.96 (min 786.78, max 997.51)","841.59 (min 737.19, max 942.95)"
   "bw_mem-bcopy-8mb (mb/s)","705.43 (min 681.72, max 746.69)","861.10 (min 794.68, max 1008.32)","833.82 (min 702.86, max 929.69)"
   "bw_mem-bzero-16mb (mb/s)","1709.69 (min 1667.88, max 1772.26)","1859.20 (min 1747.30, max 2126.25)","1984.77 (min 1739.70, max 2129.08)"
   "bw_mem-bzero-1mb (mb/s)","1203.37 (min 682.13, max 1772.74)","1365.48 (min 804.89, max 2125.78)","1444.09 (min 746.97, max 2131.82)"
   "bw_mem-bzero-2mb (mb/s)","1183.30 (min 636.44, max 1768.66)","1336.43 (min 751.60, max 2125.78)","1400.45 (min 702.25, max 2130.30)"
   "bw_mem-bzero-4mb (mb/s)","1195.43 (min 677.28, max 1769.39)","1348.47 (min 786.78, max 2126.15)","1411.05 (min 737.19, max 2130.68)"
   "bw_mem-bzero-8mb (mb/s)","1208.53 (min 681.72, max 1772.46)","1360.41 (min 794.68, max 2126.25)","1408.76 (min 702.86, max 2129.36)"
   "bw_mem-cp-16mb (mb/s)","387.08 (min 369.52, max 408.54)","482.67 (min 451.71, max 553.17)","483.61 (min 378.00, max 551.84)"
   "bw_mem-cp-1mb (mb/s)","1111.32 (min 364.10, max 1902.23)","1239.41 (min 443.59, max 2279.20)","1321.51 (min 413.91, max 2298.41)"
   "bw_mem-cp-2mb (mb/s)","1077.44 (min 363.24, max 1839.59)","1198.67 (min 430.94, max 2203.05)","1269.84 (min 384.02, max 2216.07)"
   "bw_mem-cp-4mb (mb/s)","1079.21 (min 398.37, max 1822.32)","1200.38 (min 434.64, max 2171.16)","1255.83 (min 430.94, max 2171.95)"
   "bw_mem-cp-8mb (mb/s)","1076.81 (min 396.22, max 1805.05)","1197.33 (min 478.90, max 2155.17)","1229.42 (min 384.23, max 2157.50)"
   "bw_mem-fcp-16mb (mb/s)","673.07 (min 663.02, max 688.76)","790.42 (min 727.80, max 923.15)","864.94 (min 711.68, max 996.76)"
   "bw_mem-fcp-1mb (mb/s)","1235.06 (min 729.53, max 1772.74)","1387.34 (min 861.92, max 2125.78)","1460.40 (min 799.62, max 2131.82)"
   "bw_mem-fcp-2mb (mb/s)","1226.13 (min 739.78, max 1768.66)","1383.93 (min 853.12, max 2125.78)","1433.91 (min 771.46, max 2130.30)"
   "bw_mem-fcp-4mb (mb/s)","1228.75 (min 728.46, max 1769.39)","1377.79 (min 779.73, max 2126.15)","1442.82 (min 763.36, max 2130.68)"
   "bw_mem-fcp-8mb (mb/s)","1238.47 (min 743.08, max 1772.46)","1413.61 (min 882.81, max 2126.25)","1445.51 (min 772.80, max 2129.36)"
   "bw_mem-frd-16mb (mb/s)","1017.51 (min 1005.85, max 1043.02)","1190.51 (min 1076.93, max 1445.74)","1236.60 (min 1057.85, max 1375.40)"
   "bw_mem-frd-1mb (mb/s)","948.06 (min 729.53, max 1169.40)","1145.55 (min 861.92, max 1592.08)","1175.19 (min 799.62, max 1525.42)"
   "bw_mem-frd-2mb (mb/s)","876.01 (min 739.78, max 1058.76)","1062.46 (min 853.12, max 1374.10)","1067.98 (min 771.46, max 1366.35)"
   "bw_mem-frd-4mb (mb/s)","877.16 (min 728.46, max 1049.04)","1047.26 (min 779.73, max 1457.19)","1080.89 (min 763.36, max 1368.93)"
   "bw_mem-frd-8mb (mb/s)","895.14 (min 743.08, max 1065.10)","1098.67 (min 882.81, max 1460.39)","1085.23 (min 772.80, max 1375.28)"
   "bw_mem-fwr-16mb (mb/s)","1723.99 (min 1686.16, max 1788.91)","1868.67 (min 1752.46, max 2138.75)","1995.08 (min 1738.19, max 2144.20)"
   "bw_mem-fwr-1mb (mb/s)","1477.19 (min 1073.54, max 1902.23)","1675.86 (min 1250.00, max 2279.20)","1779.54 (min 1227.64, max 2298.41)"
   "bw_mem-fwr-2mb (mb/s)","1380.57 (min 954.96, max 1839.59)","1562.67 (min 1110.08, max 2203.05)","1652.96 (min 1049.13, max 2216.07)"
   "bw_mem-fwr-4mb (mb/s)","1369.40 (min 914.18, max 1822.32)","1544.15 (min 1061.43, max 2171.16)","1640.28 (min 1043.71, max 2171.95)"
   "bw_mem-fwr-8mb (mb/s)","1379.79 (min 1003.01, max 1805.05)","1555.52 (min 1129.78, max 2155.17)","1635.01 (min 1092.45, max 2157.50)"
   "bw_mem-rd-16mb (mb/s)","1047.87 (min 1020.21, max 1088.81)","1251.39 (min 1153.24, max 1468.83)","1276.82 (min 1095.97, max 1382.53)"
   "bw_mem-rd-1mb (mb/s)","875.95 (min 543.97, max 1244.44)","1067.52 (min 644.75, max 1651.38)","1091.67 (min 601.50, max 1636.96)"
   "bw_mem-rd-2mb (mb/s)","770.17 (min 481.06, max 1091.90)","950.12 (min 568.59, max 1464.93)","944.58 (min 525.49, max 1384.56)"
   "bw_mem-rd-4mb (mb/s)","802.40 (min 546.45, max 1071.38)","975.79 (min 579.21, max 1459.06)","957.83 (min 544.74, max 1383.37)"
   "bw_mem-rd-8mb (mb/s)","833.11 (min 580.13, max 1085.78)","1036.43 (min 735.43, max 1459.59)","979.97 (min 584.45, max 1378.83)"
   "bw_mem-rdwr-16mb (mb/s)","652.77 (min 608.83, max 682.04)","844.58 (min 757.61, max 984.07)","695.85 (min 597.73, max 769.90)"
   "bw_mem-rdwr-1mb (mb/s)","465.87 (min 364.10, max 563.78)","587.04 (min 443.59, max 780.15)","580.16 (min 413.91, max 755.00)"
   "bw_mem-rdwr-2mb (mb/s)","440.37 (min 363.24, max 513.94)","543.02 (min 430.94, max 712.00)","543.27 (min 384.02, max 695.89)"
   "bw_mem-rdwr-4mb (mb/s)","489.22 (min 398.37, max 577.28)","610.77 (min 434.64, max 835.77)","559.23 (min 430.94, max 734.21)"
   "bw_mem-rdwr-8mb (mb/s)","520.11 (min 396.22, max 659.25)","651.71 (min 478.90, max 930.02)","564.44 (min 384.23, max 745.57)"
   "bw_mem-wr-16mb (mb/s)","681.95 (min 646.86, max 723.72)","880.60 (min 778.55, max 1049.87)","693.81 (min 605.85, max 757.15)"
   "bw_mem-wr-1mb (mb/s)","552.58 (min 523.65, max 611.06)","700.33 (min 619.67, max 825.63)","685.04 (min 560.75, max 774.23)"
   "bw_mem-wr-2mb (mb/s)","496.23 (min 468.99, max 536.62)","635.53 (min 560.62, max 886.13)","608.98 (min 498.32, max 707.34)"
   "bw_mem-wr-4mb (mb/s)","567.28 (min 544.22, max 619.29)","719.70 (min 579.21, max 868.72)","636.00 (min 544.74, max 734.21)"
   "bw_mem-wr-8mb (mb/s)","623.97 (min 580.13, max 659.25)","807.59 (min 726.48, max 992.19)","679.08 (min 579.50, max 759.09)"
   "bw_mmap_rd-mo-1mb (mb/s)","1127.17 (min 1071.81, max 1188.86)","1378.73 (min 1262.40, max 1630.43)","1447.04 (min 1257.64, max 1591.72)"
   "bw_mmap_rd-o2c-1mb (mb/s)","440.46 (min 411.02, max 467.73)","508.97 (min 475.13, max 580.21)","481.50 (min 407.28, max 537.44)"
   "bw_pipe (mb/s)","473.07 (min 458.83, max 487.33)","554.16 (min 517.63, max 623.64)","569.23 (min 507.77, max 614.58)"
   "bw_unix (mb/s)","569.55 (min 558.38, max 595.69)","669.05 (min 625.62, max 769.20)","814.91 (min 713.16, max 878.56)"
   "lat_connect (us)","87.20 (min 85.87, max 88.56)","76.22 (min 72.76, max 78.38)","74.59 (min 72.97, max 76.76)"
   "lat_ctx-2-128k (us)","11.62 (min 9.27, max 16.03)","8.86 (min 7.71, max 11.24)","7.94 (min 7.12, max 8.87)"
   "lat_ctx-2-256k (us)","62.76 (min 6.63, max 86.30)","57.50 (min 6.29, max 77.27)","56.88 (min 46.99, max 73.63)"
   "lat_ctx-4-128k (us)","39.79 (min 7.46, max 56.78)","41.85 (min 28.64, max 49.50)","37.70 (min 32.28, max 48.21)"
   "lat_ctx-4-256k (us)","136.79 (min 5.97, max 228.46)","125.30 (min 7.03, max 183.19)","143.67 (min 5.21, max 191.52)"
   "lat_fs-0k (num_files)","197.75 (min 178.00, max 225.00)","236.14 (min 205.00, max 259.00)","232.50 (min 204.00, max 262.00)"
   "lat_fs-10k (num_files)","91.50 (min 75.00, max 106.00)","102.00 (min 94.00, max 109.00)","108.38 (min 91.00, max 128.00)"
   "lat_fs-1k (num_files)","126.00 (min 111.00, max 154.00)","160.29 (min 136.00, max 176.00)","156.63 (min 133.00, max 177.00)"
   "lat_fs-4k (num_files)","127.75 (min 113.00, max 138.00)","146.43 (min 129.00, max 164.00)","149.75 (min 128.00, max 165.00)"
   "lat_mem_rd-stride128-sz1000k (ns)","56.98 (min 54.45, max 58.19)","48.34 (min 41.33, max 51.36)","46.67 (min 42.81, max 53.08)"
   "lat_mem_rd-stride128-sz125k (ns)","6.23 (min 6.20, max 6.26)","5.55 (min 5.52, max 5.58)","5.56 (min 5.53, max 5.59)"
   "lat_mem_rd-stride128-sz250k (ns)","6.55 (min 6.53, max 6.56)","5.85 (min 5.83, max 5.86)","5.84 (min 5.83, max 5.86)"
   "lat_mem_rd-stride128-sz31k (ns)","3.05 (min 2.41, max 4.09)","3.30 (min 2.15, max 4.19)","2.35 (min 2.15, max 3.65)"
   "lat_mem_rd-stride128-sz50 (ns)","2.40 (min 2.40, max 2.41)","2.15","2.15"
   "lat_mem_rd-stride128-sz500k (ns)","15.67 (min 8.98, max 21.81)","14.70 (min 10.94, max 18.41)","12.49 (min 9.12, max 16.87)"
   "lat_mem_rd-stride128-sz62k (ns)","5.69 (min 5.07, max 5.95)","5.25 (min 5.23, max 5.30)","5.16 (min 4.51, max 5.28)"
   "lat_mmap-1m (us)","64.00 (min 57.00, max 72.00)","60.29 (min 51.00, max 64.00)","51.88 (min 48.00, max 63.00)"
   "lat_ops-double-add (ns)","3.21","2.86","2.86"
   "lat_ops-double-div (ns)","17.64 (min 17.63, max 17.65)","15.74 (min 15.74, max 15.76)","15.74 (min 15.74, max 15.75)"
   "lat_ops-double-mul (ns)","3.21","2.86","2.86"
   "lat_ops-float-add (ns)","3.21","2.86","2.86 (min 2.86, max 2.87)"
   "lat_ops-float-div (ns)","10.43 (min 10.42, max 10.44)","9.30 (min 9.30, max 9.31)","9.30 (min 9.30, max 9.31)"
   "lat_ops-float-mul (ns)","3.21","2.86 (min 2.86, max 2.87)","2.86"
   "lat_ops-int-add (ns)","0.80","0.72","0.72"
   "lat_ops-int-bit (ns)","0.53","0.48","0.48"
   "lat_ops-int-div (ns)","4.81 (min 4.81, max 4.82)","4.29 (min 4.29, max 4.30)","4.29 (min 4.29, max 4.30)"
   "lat_ops-int-mod (ns)","5.08 (min 5.08, max 5.09)","4.53 (min 4.53, max 4.54)","4.53 (min 4.53, max 4.54)"
   "lat_ops-int-mul (ns)","3.44 (min 3.40, max 3.47)","3.07 (min 3.04, max 3.10)","3.06 (min 3.04, max 3.10)"
   "lat_ops-int64-add (ns)","0.80","0.72","0.72"
   "lat_ops-int64-bit (ns)","0.53 (min 0.53, max 0.54)","0.48","0.48"
   "lat_ops-int64-div (ns)","7.62 (min 7.61, max 7.62)","6.80 (min 6.80, max 6.81)","6.80 (min 6.80, max 6.81)"
   "lat_ops-int64-mod (ns)","5.88 (min 5.88, max 5.90)","5.25","5.25"
   "lat_ops-int64-mul (ns)","3.99 (min 3.97, max 4.07)","3.54 (min 3.54, max 3.55)","3.55 (min 3.54, max 3.55)"
   "lat_pagefault (us)","0.84 (min 0.60, max 1.98)","0.90 (min 0.52, max 1.73)","1.41 (min 0.94, max 1.86)"
   "lat_pipe (us)","20.34 (min 19.98, max 20.75)","18.16 (min 17.95, max 18.36)","18.27 (min 18.07, max 18.39)"
   "lat_proc-exec (us)","1123.65 (min 1102.20, max 1140.80)","971.09 (min 840.71, max 1054.20)","936.41 (min 837.71, max 1073.60)"
   "lat_proc-fork (us)","965.95 (min 936.17, max 999.83)","819.10 (min 714.63, max 875.67)","806.58 (min 700.88, max 970.50)"
   "lat_proc-proccall (us)","0.01","0.01","0.01"
   "lat_select (us)","35.89 (min 35.65, max 36.12)","31.97 (min 31.83, max 32.14)","31.99 (min 31.75, max 32.39)"
   "lat_sem (us)","2.91 (min 2.55, max 3.24)","2.56 (min 2.23, max 2.99)","2.53 (min 2.32, max 2.79)"
   "lat_sig-catch (us)","6.59 (min 6.40, max 7.57)","5.74 (min 5.67, max 5.85)","5.75 (min 5.67, max 5.84)"
   "lat_sig-install (us)","0.69 (min 0.68, max 0.70)","0.61 (min 0.60, max 0.63)","0.61 (min 0.60, max 0.63)"
   "lat_sig-prot (us)","0.88 (min 0.28, max 1.63)","0.74 (min 0.24, max 1.82)","0.62 (min 0.22, max 0.92)"
   "lat_syscall-fstat (us)","2.02 (min 1.89, max 2.06)","1.79 (min 1.68, max 1.84)","1.80 (min 1.70, max 1.85)"
   "lat_syscall-null (us)","0.42 (min 0.41, max 0.44)","0.38 (min 0.37, max 0.41)","0.38 (min 0.37, max 0.41)"
   "lat_syscall-open (us)","238.54 (min 178.28, max 329.64)","183.49 (min 152.22, max 220.25)","184.13 (min 150.46, max 235.48)"
   "lat_syscall-read (us)","0.80 (min 0.79, max 0.82)","0.72 (min 0.71, max 0.74)","0.72 (min 0.70, max 0.74)"
   "lat_syscall-stat (us)","4.96 (min 4.75, max 5.17)","4.42 (min 4.24, max 4.55)","4.42 (min 4.26, max 4.58)"
   "lat_syscall-write (us)","0.76 (min 0.75, max 0.77)","0.68 (min 0.67, max 0.69)","0.68 (min 0.67, max 0.69)"
   "lat_tcp (us)","0.85","0.76 (min 0.75, max 0.76)","0.75 (min 0.75, max 0.76)"
   "lat_unix (us)","30.67 (min 27.18, max 37.00)","25.96 (min 22.81, max 32.60)","26.58 (min 22.63, max 33.38)"
   "latency_for_0.50_mb_block_size (nanosec)","15.67 (min 8.98, max 21.81)","14.70 (min 10.94, max 18.41)","12.49 (min 9.12, max 16.87)"
   "latency_for_1.00_mb_block_size (nanosec)","28.49 (min 0.00, max 58.19)","24.17 (min 0.00, max 51.36)","23.34 (min 0.00, max 53.08)"
   "pipe_bandwidth (mb\s)","473.07 (min 458.83, max 487.33)","554.16 (min 517.63, max 623.64)","569.23 (min 507.77, max 614.58)"
   "pipe_latency (microsec)","20.34 (min 19.98, max 20.75)","18.16 (min 17.95, max 18.36)","18.27 (min 18.07, max 18.39)"
   "procedure_call (microsec)","0.01","0.01","0.01"
   "select_on_200_tcp_fds (microsec)","35.89 (min 35.65, max 36.12)","31.97 (min 31.83, max 32.14)","31.99 (min 31.75, max 32.39)"
   "semaphore_latency (microsec)","2.91 (min 2.55, max 3.24)","2.56 (min 2.23, max 2.99)","2.53 (min 2.32, max 2.79)"
   "signal_handler_latency (microsec)","0.69 (min 0.68, max 0.70)","0.61 (min 0.60, max 0.63)","0.61 (min 0.60, max 0.63)"
   "signal_handler_overhead (microsec)","6.59 (min 6.40, max 7.57)","5.74 (min 5.67, max 5.85)","5.75 (min 5.67, max 5.84)"
   "tcp_ip_connection_cost_to_localhost (microsec)","87.20 (min 85.87, max 88.56)","76.22 (min 72.76, max 78.38)","74.59 (min 72.97, max 76.76)"
   "tcp_latency_using_localhost (microsec)","0.85","0.76 (min 0.75, max 0.76)","0.75 (min 0.75, max 0.76)"

Dhrystone
=========

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
   "dhrystone_per_mhz (dmips/mhz)","2.80","2.79 (min 2.70, max 2.80)","2.77 (min 2.70, max 2.80)"
   "dhrystone_per_second (dhrystonep)","6141774.86 (min 6060606.00, max 6250000.00)","6863710.79 (min 6666666.50, max 6896551.50)","6830870.07 (min 6666666.50, max 6896551.50)"

Whetstone
=========

Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

.. code-block:: console

    runWhetstone

.. csv-table:: Whetstone Benchmarks
   :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

   "whetstone (mips)","4761.90 (min 3333.30, max 5000.00)","5000.00","5000.00"

Linpack
=======

Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
   :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

   "linpack (kflops)","517865.38 (min 514550.00, max 520320.00)","580734.88 (min 578538.00, max 581576.00)","580806.38 (min 576498.00, max 582761.00)"

NBench
======

NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
   :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

   "assignment (iterations)","12.64 (min 12.60, max 12.69)","14.14 (min 14.09, max 14.19)","14.16 (min 14.14, max 14.20)"
   "fourier (iterations)","17292.13 (min 17285.00, max 17294.00)","19368.57 (min 19367.00, max 19371.00)","19367.86 (min 19364.00, max 19370.00)"
   "fp_emulation (iterations)","182.48 (min 182.46, max 182.50)","204.37 (min 204.35, max 204.40)","204.38 (min 204.35, max 204.40)"
   "huffman (iterations)","1060.79 (min 1060.30, max 1061.00)","1188.30 (min 1188.20, max 1188.50)","1188.30 (min 1188.00, max 1188.50)"
   "idea (iterations)","2741.40 (min 2741.10, max 2741.60)","3070.24 (min 3069.90, max 3070.70)","3070.46 (min 3069.90, max 3070.70)"
   "lu_decomposition (iterations)","475.33 (min 474.42, max 476.79)","532.06 (min 529.78, max 534.66)","532.23 (min 530.58, max 533.03)"
   "neural_net (iterations)","8.64","9.68 (min 9.67, max 9.68)","9.68 (min 9.67, max 9.68)"
   "numeric_sort (iterations)","481.49 (min 474.08, max 484.33)","541.23 (min 537.88, max 544.71)","539.27 (min 529.26, max 542.85)"
   "string_sort (iterations)","146.05 (min 145.99, max 146.07)","163.58 (min 163.54, max 163.61)","163.59 (min 163.56, max 163.61)"

Stream
======

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

   "add (mb/s)","1383.03 (min 1362.70, max 1413.40)","1511.73 (min 1460.10, max 1811.70)"
   "copy (mb/s)","1476.20 (min 1448.10, max 1514.40)","1736.43 (min 1660.70, max 2193.00)"
   "scale (mb/s)","1593.09 (min 1563.10, max 1628.00)","1858.19 (min 1770.70, max 2259.30)"
   "triad (mb/s)","1358.20 (min 1341.00, max 1385.50)","1545.66 (min 1497.40, max 1852.60)"

CoreMarkPro
===========

CoreMark\ |reg|-Pro is a comprehensive, advanced processor benchmark that works
with and enhances the market-proven industry-standard EEMBC CoreMark\ |reg|
benchmark. While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the
entire processor, adding comprehensive support for multicore technology, a
combination of integer and floating-point workloads, and data sets for utilizing
larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
   :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

   "cjpeg-rose7-preset (workloads/)","37.11 (min 37.04, max 37.17)","41.59 (min 41.49, max 41.67)","41.78 (min 41.32, max 42.02)"
   "core (workloads/)","0.27","0.30","0.30"
   "coremark-pro ()","811.35 (min 807.24, max 816.16)","909.83 (min 905.76, max 913.32)","884.10 (min 876.18, max 895.97)"
   "linear_alg-mid-100x100-sp (workloads/)","13.09 (min 13.09, max 13.10)","14.67 (min 14.66, max 14.67)","14.67 (min 14.65, max 14.69)"
   "loops-all-mid-10k-sp (workloads/)","0.60 (min 0.59, max 0.60)","0.67","0.68 (min 0.66, max 0.70)"
   "nnet_test (workloads/)","0.96","1.08","1.08"
   "parser-125k (workloads/)","7.87 (min 7.81, max 7.94)","8.84 (min 8.77, max 8.85)","8.89 (min 8.62, max 9.01)"
   "radix2-big-64k (workloads/)","52.44 (min 51.00, max 54.07)","59.10 (min 58.09, max 60.53)","44.35 (min 42.40, max 47.43)"
   "sha-test (workloads/)","71.18 (min 70.92, max 71.43)","79.46 (min 78.74, max 80.00)","80.73 (min 80.00, max 81.30)"
   "zip-test (workloads/)","19.56 (min 19.23, max 19.61)","22.02 (min 21.74, max 22.22)","21.57 (min 21.28, max 21.74)"

.. csv-table:: CoreMarkProTwoCore Benchmarks
   :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

   "cjpeg-rose7-preset (workloads/)","72.54 (min 72.46, max 72.99)","81.40 (min 80.65, max 82.64)","82.99 (min 82.64, max 83.33)"
   "core (workloads/)","0.54","0.60","0.60"
   "coremark-pro ()","1347.31 (min 1337.78, max 1356.38)","1535.37 (min 1511.03, max 1592.13)","1549.74 (min 1473.40, max 1595.22)"
   "linear_alg-mid-100x100-sp (workloads/)","26.14 (min 26.14, max 26.15)","29.29 (min 29.27, max 29.31)","29.31 (min 29.22, max 29.36)"
   "loops-all-mid-10k-sp (workloads/)","1.03 (min 1.03, max 1.04)","1.18 (min 1.15, max 1.25)","1.20 (min 1.13, max 1.24)"
   "nnet_test (workloads/)","1.92","2.15 (min 2.15, max 2.16)","2.15 (min 2.14, max 2.15)"
   "parser-125k (workloads/)","13.00 (min 12.66, max 13.25)","15.02 (min 14.60, max 15.87)","13.71 (min 12.42, max 14.39)"
   "radix2-big-64k (workloads/)","31.72 (min 31.13, max 32.41)","38.75 (min 35.78, max 45.94)","43.88 (min 34.86, max 50.79)"
   "sha-test (workloads/)","137.27 (min 135.14, max 138.89)","154.53 (min 153.85, max 156.25)","160.33 (min 158.73, max 161.29)"
   "zip-test (workloads/)","36.00 (min 35.09, max 36.36)","41.31 (min 40.82, max 42.55)","40.57 (min 37.04, max 41.67)"

MultiBench
==========

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

   "4m-check (workloads/)","275.83 (min 273.79, max 283.35)","313.67 (min 311.95, max 316.58)","329.39 (min 304.62, max 369.33)"
   "4m-check-reassembly (workloads/)","75.74 (min 74.02, max 78.68)","85.41 (min 84.32, max 87.34)","85.95 (min 76.22, max 100.81)"
   "4m-check-reassembly-tcp (workloads/)","43.95 (min 43.71, max 44.96)","48.98 (min 48.73, max 49.21)","50.55 (min 46.21, max 57.21)"
   "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","22.05 (min 21.84, max 22.60)","24.72 (min 24.38, max 24.80)","25.78 (min 23.58, max 29.28)"
   "4m-check-reassembly-tcp-x264w2 (workloads/)","1.58 (min 1.56, max 1.60)","1.77 (min 1.75, max 1.78)","1.76 (min 1.67, max 1.83)"
   "4m-cmykw2 (workloads/)","176.85 (min 175.44, max 181.32)","199.48 (min 196.27, max 203.05)","211.37 (min 192.12, max 238.38)"
   "4m-cmykw2-rotatew2 (workloads/)","34.32 (min 33.58, max 35.23)","39.10 (min 38.61, max 39.53)","40.57 (min 37.57, max 45.45)"
   "4m-reassembly (workloads/)","73.39 (min 71.63, max 74.68)","84.27 (min 82.85, max 85.91)","84.97 (min 76.05, max 97.94)"
   "4m-rotatew2 (workloads/)","40.33 (min 40.05, max 41.12)","45.68 (min 45.25, max 46.06)","46.12 (min 43.27, max 52.16)"
   "4m-tcp-mixed (workloads/)","97.39 (min 96.97, max 98.16)","109.59 (min 108.84, max 110.35)","115.74 (min 110.35, max 124.03)"
   "4m-x264w2 (workloads/)","1.63 (min 1.62, max 1.65)","1.84 (min 1.82, max 1.86)","1.84 (min 1.80, max 1.90)"
   "empty-wld (workloads/)","1.00","1.00","1.00"
   "idct-4m (workloads/)","17.57 (min 17.57, max 17.58)","19.69 (min 19.67, max 19.70)","19.64 (min 19.62, max 19.68)"
   "idct-4mw1 (workloads/)","17.58 (min 17.56, max 17.59)","19.69 (min 19.69, max 19.70)","19.65 (min 19.61, max 19.69)"
   "ippktcheck-4m (workloads/)","277.45 (min 275.48, max 284.90)","315.35 (min 313.17, max 316.34)","329.27 (min 304.32, max 369.44)"
   "ippktcheck-4mw1 (workloads/)","277.43 (min 275.73, max 283.32)","315.56 (min 314.19, max 317.30)","329.59 (min 303.10, max 372.19)"
   "ipres-4m (workloads/)","58.38 (min 57.67, max 59.81)","65.79 (min 65.19, max 66.70)","67.98 (min 62.24, max 77.40)"
   "ipres-4mw1 (workloads/)","58.47 (min 58.07, max 59.74)","65.73 (min 65.05, max 66.37)","67.91 (min 61.73, max 77.48)"
   "md5-4m (workloads/)","22.40 (min 22.19, max 22.56)","25.19 (min 24.97, max 25.41)","25.24 (min 23.17, max 26.80)"
   "md5-4mw1 (workloads/)","22.34 (min 22.19, max 22.44)","25.15 (min 24.91, max 25.36)","25.53 (min 23.70, max 26.90)"
   "rgbcmyk-4m (workloads/)","57.12 (min 56.85, max 57.41)","64.16 (min 63.84, max 64.41)","63.91 (min 63.35, max 64.85)"
   "rgbcmyk-4mw1 (workloads/)","56.85 (min 56.71, max 57.11)","64.31 (min 64.02, max 64.43)","63.84 (min 62.52, max 64.87)"
   "rotate-4ms1 (workloads/)","17.73 (min 17.65, max 18.15)","19.95 (min 19.90, max 19.98)","19.48 (min 18.12, max 21.60)"
   "rotate-4ms1w1 (workloads/)","17.72 (min 17.59, max 18.16)","19.96 (min 19.90, max 20.00)","19.34 (min 18.00, max 21.50)"
   "rotate-4ms64 (workloads/)","17.84 (min 17.72, max 18.27)","20.10 (min 20.08, max 20.13)","19.65 (min 18.36, max 21.82)"
   "rotate-4ms64w1 (workloads/)","17.86 (min 17.76, max 18.32)","20.11 (min 20.09, max 20.13)","19.64 (min 18.27, max 21.85)"
   "x264-4mq (workloads/)","0.50","0.56","0.56 (min 0.56, max 0.57)"
   "x264-4mqw1 (workloads/)","0.50","0.56","0.56 (min 0.55, max 0.57)"

*********************
Boot-time Measurement
*********************

Boot media: MMCSD
=================

.. csv-table:: Linux boot time MMCSD
   :header: "Boot Configuration","am62xx_lp_sk-fs: Boot time in seconds: avg(min,max)","am62xx_sk-fs: Boot time in seconds: avg(min,max)","am62xxsip_sk-fs: Boot time in seconds: avg(min,max)"

   "Linux boot time from SD with default rootfs (20 boot cycles)","19.86 (min 18.49, max 24.91)","19.10 (min 17.79, max 22.37)","18.76 (min 17.65, max 21.66)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

*********************
ALSA SoC Audio Driver
*********************

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
   :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)","am62xxsip_sk-fs: Throughput (bits/sec)","am62xxsip_sk-fs: CPU Load (%)"

   "11025","352797.43 (min 352796.00, max 352798.00)","0.25 (min 0.17, max 0.44)","352797.00 (min 352790.00, max 352799.00)","0.21 (min 0.15, max 0.28)","352795.00 (min 352766.00, max 352808.00)","0.23 (min 0.18, max 0.28)"
   "16000","511997.57 (min 511997.00, max 511998.00)","0.17 (min 0.13, max 0.24)","511998.43 (min 511996.00, max 512000.00)","0.18 (min 0.13, max 0.23)","511995.71 (min 511977.00, max 512003.00)","0.17 (min 0.14, max 0.21)"
   "22050","705591.29 (min 705588.00, max 705593.00)","0.22 (min 0.19, max 0.28)","705595.71 (min 705593.00, max 705600.00)","0.22 (min 0.17, max 0.28)","705599.43 (min 705587.00, max 705629.00)","0.20 (min 0.17, max 0.24)"
   "24000","705594.29 (min 705592.00, max 705595.00)","0.24 (min 0.21, max 0.32)","705597.00 (min 705595.00, max 705600.00)","0.23 (min 0.19, max 0.28)","705598.71 (min 705595.00, max 705605.00)","0.21 (min 0.17, max 0.26)"
   "32000","1023992.86 (min 1023991.00, max 1023994.00)","0.17 (min 0.13, max 0.24)","1023995.71 (min 1023993.00, max 1023999.00)","0.17 (min 0.14, max 0.23)","1023996.86 (min 1023979.00, max 1024008.00)","0.33 (min 0.14, max 0.82)"
   "44100","1411189.71 (min 1411187.00, max 1411192.00)","0.33 (min 0.31, max 0.38)","1411193.86 (min 1411190.00, max 1411198.00)","0.33 (min 0.27, max 0.42)","1411194.71 (min 1411163.00, max 1411213.00)","0.30 (min 0.25, max 0.36)"
   "48000","1535989.29 (min 1535986.00, max 1535992.00)","0.28 (min 0.15, max 0.73)","1535993.00 (min 1535987.00, max 1535998.00)","0.53 (min 0.16, max 2.00)","1535993.71 (min 1535956.00, max 1536015.00)","0.28 (min 0.13, max 0.69)"
   "88200","2822374.43 (min 2822367.00, max 2822380.00)","0.50 (min 0.48, max 0.53)","2822383.00 (min 2822374.00, max 2822390.00)","0.47 (min 0.40, max 0.55)","2822383.71 (min 2822311.00, max 2822425.00)","0.45 (min 0.42, max 0.47)"
   "96000","3071948.86 (min 3071943.00, max 3071954.00)","0.36 (min 0.17, max 1.26)","3071953.14 (min 3071919.00, max 3071967.00)","0.23 (min 0.17, max 0.28)","3071956.71 (min 3071923.00, max 3072050.00)","0.43 (min 0.14, max 0.93)"

.. csv-table:: Audio Playback
   :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)","am62xxsip_sk-fs: Throughput (bits/sec)","am62xxsip_sk-fs: CPU Load (%)"

   "11025","352938.00 (min 352894.00, max 352947.00)","0.19 (min 0.16, max 0.23)","352946.50 (min 352944.00, max 352948.00)","0.20 (min 0.13, max 0.32)","352942.25 (min 352916.00, max 352947.00)","0.25 (min 0.13, max 0.41)"
   "16000","512207.14 (min 512181.00, max 512212.00)","0.22 (min 0.14, max 0.32)","512213.38 (min 512211.00, max 512215.00)","0.15 (min 0.13, max 0.16)","512210.88 (min 512191.00, max 512216.00)","0.20 (min 0.13, max 0.35)"
   "22050","705891.29 (min 705886.00, max 705918.00)","0.17 (min 0.15, max 0.19)","705888.63 (min 705886.00, max 705891.00)","0.16 (min 0.14, max 0.17)","705893.25 (min 705885.00, max 705928.00)","0.21 (min 0.14, max 0.36)"
   "24000","705888.00 (min 705876.00, max 705891.00)","0.19 (min 0.17, max 0.21)","705892.00 (min 705890.00, max 705894.00)","0.17 (min 0.16, max 0.19)","705892.50 (min 705890.00, max 705896.00)","0.23 (min 0.15, max 0.39)"
   "32000","1024415.71 (min 1024379.00, max 1024424.00)","0.35 (min 0.14, max 0.96)","1024424.63 (min 1024421.00, max 1024427.00)","0.19 (min 0.13, max 0.44)","1024423.25 (min 1024409.00, max 1024430.00)","0.21 (min 0.13, max 0.44)"
   "44100","1411771.71 (min 1411711.00, max 1411784.00)","0.26 (min 0.24, max 0.28)","1411785.50 (min 1411779.00, max 1411789.00)","0.23 (min 0.20, max 0.27)","1411782.38 (min 1411755.00, max 1411794.00)","0.29 (min 0.22, max 0.47)"
   "48000","1536621.29 (min 1536551.00, max 1536635.00)","0.35 (min 0.18, max 0.74)","1536637.38 (min 1536631.00, max 1536641.00)","0.20 (min 0.15, max 0.41)","1536633.25 (min 1536600.00, max 1536646.00)","0.23 (min 0.14, max 0.41)"
   "88200","2823536.29 (min 2823403.00, max 2823563.00)","0.35 (min 0.30, max 0.40)","2823566.63 (min 2823556.00, max 2823574.00)","0.30 (min 0.26, max 0.35)","2823559.75 (min 2823495.00, max 2823584.00)","0.36 (min 0.26, max 0.54)"
   "96000","3073285.43 (min 3073227.00, max 3073597.00)","0.30 (min 0.21, max 0.59)","3073259.38 (min 3073238.00, max 3073291.00)","0.21 (min 0.18, max 0.25)","3073255.50 (min 3073232.00, max 3073320.00)","0.38 (min 0.17, max 0.77)"

***************
Graphics Driver
***************

GFXBench
========

Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
   :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_lp_sk-fs: Fps","am62xx_sk-fs: Score","am62xx_sk-fs: Fps"

   " GFXBench 3.x gl_manhattan_off","81.84 (min 80.19, max 82.29)","1.32 (min 1.29, max 1.33)"
   " GFXBench 3.x gl_trex_off","124.63 (min 122.21, max 126.97)","2.23 (min 2.18, max 2.27)"
   " GFXBench 5.x gl_5_high_off","11.16 (min 11.10, max 11.26)","0.17 (min 0.17, max 0.18)","11.52 (min 11.42, max 11.89)","0.18"

Glmark2
=======

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
   :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_sk-fs: Score","am62xxsip_sk-fs: Score"

   "Glmark2-DRM","60.00 (min 51.00, max 69.00)","61.00","55.43 (min 54.00, max 56.00)"
   "Glmark2-Wayland","200.57 (min 198.00, max 201.00)","216.63 (min 214.00, max 224.00)","207.00"
   "Glmark2-Wayland 1920x1080","71.00 (min 62.00, max 78.00)","66.14 (min 66.00, max 67.00)"

***********************
Linux OSPI Flash Driver
***********************

.. rubric:: AM62XX-SK
   :name: am62xx-sk-ospi-flash-driver

.. rubric:: UBIFS
   :name: am62xx-sk-ospi-ubifs

.. csv-table:: OSPI Flash Driver
   :header: "Buffer size (bytes)","am62xx_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62xx_sk-fs: Write UBIFS CPU Load (%)","am62xx_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62xx_sk-fs: Read UBIFS CPU Load (%)"

   "102400","0.16 (min 0.11, max 0.27)","28.69 (min 24.88, max 33.46)","58.87 (min 54.43, max 63.53)","21.96 (min 13.33, max 29.41)"
   "262144","0.13 (min 0.10, max 0.18)","28.71 (min 25.06, max 32.15)","58.10 (min 53.78, max 62.19)","16.23 (min 7.69, max 25.00)"
   "524288","0.13 (min 0.10, max 0.18)","28.64 (min 25.52, max 33.15)","57.62 (min 54.48, max 60.89)","17.38 (min 7.69, max 21.43)"
   "1048576","0.14 (min 0.10, max 0.18)","29.04 (min 25.44, max 34.67)","56.32 (min 51.85, max 59.73)","18.39 (min 8.33, max 26.67)"

.. rubric:: UBIFS
   :name: am62xx-sk-lp-ospi-ubifs

.. csv-table:: OSPI Flash Driver
   :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write UBIFS CPU Load (%)","am62xx_lp_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read UBIFS CPU Load (%)"

   "102400","7.20 (min 6.77, max 7.61)","15.42 (min 12.17, max 19.66)","15.73 (min 15.14, max 16.46)","18.23 (min 13.73, max 23.21)"
   "262144","7.01 (min 6.66, max 7.60)","15.32 (min 12.93, max 18.02)","15.58 (min 15.03, max 16.20)","17.14 (min 12.50, max 21.82)"
   "524288","7.02 (min 6.48, max 7.56)","15.35 (min 11.61, max 17.89)","15.53 (min 15.05, max 16.07)","19.18 (min 15.38, max 25.00)"
   "1048576","7.05 (min 6.50, max 7.60)","15.34 (min 12.50, max 18.85)","15.40 (min 15.00, max 16.16)","18.58 (min 11.76, max 22.22)"

.. rubric:: UBIFS
   :name: am62xxsip-sk-ospi-ubifs

.. csv-table:: OSPI Flash Driver
   :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write UBIFS CPU Load (%)","am62xxsip_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read UBIFS CPU Load (%)"

   "102400","0.17 (min 0.12, max 0.30)","28.29 (min 24.92, max 32.78)","58.30 (min 54.19, max 62.49)","15.95 (min 8.33, max 23.53)"
   "262144","0.14 (min 0.10, max 0.19)","29.22 (min 26.01, max 33.58)","57.20 (min 53.52, max 61.49)","19.18 (min 7.69, max 21.43)"
   "524288","0.14 (min 0.10, max 0.19)","28.99 (min 26.01, max 32.50)","56.31 (min 51.61, max 60.72)","20.85 (min 18.75, max 25.00)"
   "1048576","0.14 (min 0.10, max 0.19)","28.80 (min 25.66, max 32.80)","55.22 (min 51.98, max 58.98)","20.33 (min 13.33, max 26.67)"

.. rubric:: RAW
   :name: am62xx-sk-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
   :header: "File size (Mbytes)","am62xx_sk-fs: Raw Read Throughput (Mbytes/sec)"

   "50","179.19 (min 161.29, max 192.31)"

.. rubric:: RAW
   :name: am62xx-sk-lp-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
   :header: "File size (Mbytes)","am62xx_lp_sk-fs: Raw Read Throughput (Mbytes/sec)"

   "50","30.91 (min 29.94, max 31.85)"

.. rubric:: RAW
   :name: am62xx-sk-sip-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
   :header: "File size (Mbytes)","am62xxsip_sk-fs: Raw Read Throughput (Mbytes/sec)"

   "50","115.85 (min 89.28, max 128.21)"

***********
EMMC Driver
***********

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

EMMC EXT4 FIO 1G
================

.. csv-table:: EMMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

   "1m","68.41 (min 44.60, max 91.90)","2.00 (min 1.43, max 2.65)","173.43 (min 171.00, max 175.00)","2.38 (min 2.08, max 2.61)"
   "4m","70.93 (min 44.90, max 97.60)","1.51 (min 1.08, max 1.98)","172.86 (min 169.00, max 175.00)","1.75 (min 1.53, max 1.98)"
   "4k","41.38 (min 5.33, max 62.00)","12.82 (min 2.10, max 19.45)","66.11 (min 36.30, max 93.00)","15.67 (min 9.08, max 21.49)"
   "256k","65.64 (min 35.40, max 92.00)","2.44 (min 1.70, max 3.27)","173.00 (min 171.00, max 174.00)","3.03 (min 2.80, max 3.12)"

.. csv-table:: EMMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

   "1m","53.58 (min 42.90, max 61.70)","1.79 (min 1.35, max 2.12)","174.75 (min 174.00, max 175.00)","2.63 (min 2.31, max 2.89)"
   "4m","53.60 (min 43.10, max 61.70)","1.33 (min 1.19, max 1.46)","174.75 (min 174.00, max 175.00)","1.96 (min 1.78, max 2.18)"
   "4k","33.65 (min 5.22, max 50.80)","11.31 (min 2.15, max 16.87)","48.91 (min 36.40, max 56.80)","13.46 (min 10.14, max 15.57)"
   "256k","50.25 (min 34.10, max 61.80)","2.12 (min 1.64, max 2.47)","174.00","3.27 (min 2.79, max 3.51)"

.. csv-table:: EMMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

   "1m","91.60 (min 90.00, max 92.60)","2.68 (min 2.36, max 3.11)","171.38 (min 171.00, max 172.00)","2.62 (min 2.18, max 3.06)"
   "4m","96.35 (min 92.40, max 97.80)","2.47 (min 2.06, max 2.76)","165.75 (min 140.00, max 173.00)","2.43 (min 2.06, max 2.66)"
   "4k","61.86 (min 61.50, max 62.20)","18.90 (min 17.77, max 19.29)","92.05 (min 91.80, max 92.30)","20.79 (min 20.43, max 21.34)"
   "256k","91.40 (min 89.90, max 92.60)","2.76 (min 2.46, max 2.99)","170.50 (min 170.00, max 171.00)","2.68 (min 2.44, max 2.83)"

EMMC EXT4
=========

.. csv-table:: EMMC EXT4
   :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

   "102400","69.52 (min 42.22, max 87.42)","4.76 (min 1.99, max 7.90)","179.45 (min 178.72, max 180.95)","8.53 (min 7.36, max 9.83)"
   "262144","65.08 (min 42.53, max 87.97)","3.59 (min 1.58, max 6.75)","181.38 (min 180.24, max 183.10)","9.12 (min 7.83, max 10.00)"
   "524288","63.06 (min 42.39, max 86.80)","3.54 (min 1.67, max 6.94)","181.60 (min 180.77, max 182.98)","10.07 (min 8.23, max 11.69)"
   "1048576","61.70 (min 42.25, max 87.06)","3.40 (min 1.67, max 6.05)","181.51 (min 180.29, max 183.01)","9.82 (min 8.77, max 10.82)"
   "5242880","60.59 (min 42.53, max 87.62)","3.43 (min 1.79, max 6.65)","181.62 (min 180.55, max 183.00)","10.43 (min 7.93, max 10.96)"

.. csv-table:: EMMC EXT4
   :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

   "102400","44.00 (min 40.28, max 55.58)","3.56 (min 2.65, max 5.68)","177.82 (min 165.20, max 180.67)","9.61 (min 8.37, max 10.39)"
   "262144","44.24 (min 40.39, max 57.18)","2.72 (min 2.07, max 4.14)","182.84 (min 182.57, max 183.03)","10.82 (min 9.73, max 11.84)"
   "524288","44.28 (min 40.67, max 57.08)","2.74 (min 2.07, max 4.50)","182.69 (min 182.27, max 182.91)","10.98 (min 10.09, max 12.00)"
   "1048576","44.36 (min 40.66, max 57.28)","2.93 (min 2.18, max 5.39)","182.57 (min 182.29, max 182.91)","11.31 (min 10.18, max 12.39)"
   "5242880","44.45 (min 40.54, max 57.48)","2.78 (min 2.18, max 4.59)","182.58 (min 182.22, max 182.76)","12.70 (min 11.89, max 13.22)"

.. csv-table:: EMMC EXT4
   :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

   "102400","92.94 (min 32.80, max 100.32)","9.43 (min 3.35, max 28.85)","169.30 (min 151.76, max 178.93)","19.19 (min 6.06, max 38.60)"
   "262144","78.55 (min 25.81, max 100.58)","5.51 (min 0.93, max 14.13)","176.07 (min 168.34, max 180.52)","16.03 (min 7.76, max 30.71)"
   "524288","76.82 (min 31.91, max 100.62)","6.59 (min 0.88, max 22.72)","178.88 (min 174.15, max 181.14)","16.03 (min 9.05, max 33.89)"
   "1048576","76.88 (min 30.85, max 100.45)","6.77 (min 1.13, max 28.57)","179.75 (min 176.11, max 181.05)","15.43 (min 7.83, max 30.77)"
   "5242880","72.13 (min 12.13, max 99.38)","7.78 (min 0.67, max 27.46)","180.09 (min 177.94, max 181.00)","16.59 (min 9.61, max 33.04)"

EMMC VFAT
=========

.. csv-table:: EMMC VFAT
   :header: "Buffer size (bytes)","am62xx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xx_sk-fs: Write VFAT CPU Load (%)","am62xx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xx_sk-fs: Read VFAT CPU Load (%)"

   "102400","48.19 (min 33.57, max 71.46)","6.46 (min 4.27, max 12.05)","168.71 (min 162.37, max 173.50)","12.38 (min 10.70, max 14.06)"
   "262144","46.92 (min 32.85, max 75.91)","6.36 (min 4.65, max 12.55)","169.32 (min 161.30, max 174.93)","13.17 (min 10.50, max 14.84)"
   "524288","47.68 (min 32.87, max 77.67)","6.53 (min 4.73, max 12.74)","165.37 (min 153.08, max 174.31)","13.31 (min 11.79, max 14.57)"
   "1048576","47.91 (min 32.99, max 77.93)","6.57 (min 4.67, max 13.04)","165.97 (min 155.50, max 173.80)","13.83 (min 10.93, max 15.50)"
   "5242880","47.71 (min 32.97, max 78.03)","6.37 (min 4.59, max 12.54)","164.85 (min 152.31, max 173.59)","14.36 (min 12.45, max 15.48)"

.. csv-table:: EMMC VFAT
   :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write VFAT CPU Load (%)","am62xx_lp_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read VFAT CPU Load (%)"

   "102400","40.43 (min 31.07, max 49.44)","6.43 (min 4.63, max 10.38)","168.86 (min 167.73, max 169.27)","14.25 (min 12.86, max 16.06)"
   "262144","41.59 (min 31.76, max 50.97)","6.58 (min 4.75, max 10.51)","169.86 (min 169.38, max 170.49)","15.60 (min 14.88, max 16.80)"
   "524288","41.14 (min 31.60, max 49.01)","6.61 (min 4.85, max 10.41)","167.28 (min 165.01, max 168.80)","15.56 (min 14.29, max 18.04)"
   "1048576","41.32 (min 31.68, max 50.75)","6.58 (min 4.64, max 10.91)","166.73 (min 163.49, max 168.54)","16.73 (min 15.20, max 18.07)"
   "5242880","41.49 (min 31.76, max 51.20)","6.52 (min 4.80, max 10.48)","165.78 (min 164.53, max 168.10)","16.96 (min 16.26, max 18.18)"

.. csv-table:: EMMC VFAT
   :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write VFAT CPU Load (%)","am62xxsip_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read VFAT CPU Load (%)"

   "102400","77.12 (min 41.04, max 99.54)","22.26 (min 4.96, max 41.84)","173.88 (min 170.57, max 175.07)","14.29 (min 10.55, max 18.99)"
   "262144","72.66 (min 51.99, max 98.21)","14.38 (min 3.59, max 29.62)","175.72 (min 174.83, max 176.13)","13.98 (min 10.64, max 15.81)"
   "524288","74.71 (min 54.67, max 98.82)","16.74 (min 4.74, max 35.41)","175.17 (min 174.66, max 175.47)","14.16 (min 10.64, max 17.30)"
   "1048576","74.87 (min 50.23, max 98.60)","16.02 (min 5.18, max 36.73)","174.19 (min 169.94, max 175.78)","15.91 (min 11.34, max 29.34)"
   "5242880","75.22 (min 52.18, max 98.40)","16.07 (min 4.82, max 28.51)","174.28 (min 173.04, max 175.08)","15.35 (min 12.66, max 16.81)"

*****************
UBoot EMMC Driver
*****************

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

   "2000000","73343.55 (min 57087.11, max 97814.93)","170123.18 (min 168041.03, max 172463.16)"
   "4000000","74605.63 (min 57588.75, max 101922.24)","174014.14 (min 172918.21, max 175229.95)"

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

   "2000000","58986.98 (min 57186.74, max 61826.42)","169415.05 (min 167183.67, max 170666.67)"
   "4000000","59433.56 (min 56888.89, max 62178.37)","173443.10 (min 172918.21, max 174297.87)"

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

   "2000000","87328.60 (min 9097.17, max 102721.00)","162042.96 (min 137680.67, max 172463.16)"
   "4000000","97752.51 (min 94979.71, max 99447.65)","172254.84 (min 159843.90, max 175229.95)"

*****
MMCSD
*****

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

MMC EXT4 FIO 1G
===============

.. csv-table:: MMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

   "1m","42.18 (min 41.20, max 43.30)","1.48 (min 1.35, max 1.70)","85.93 (min 85.30, max 86.30)","1.68 (min 1.47, max 1.85)"
   "4m","41.36 (min 40.40, max 42.50)","1.08 (min 0.87, max 1.19)","85.03 (min 84.60, max 85.60)","1.20 (min 1.04, max 1.32)"
   "4k","2.84 (min 2.81, max 2.89)","1.88 (min 1.68, max 1.95)","13.06 (min 13.00, max 13.30)","4.16 (min 4.04, max 4.39)"
   "256k","38.73 (min 37.50, max 40.30)","1.74 (min 1.46, max 1.97)","84.69 (min 84.30, max 85.10)","1.78 (min 1.56, max 2.02)"

.. csv-table:: MMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

   "1m","43.39 (min 42.20, max 46.10)","1.72 (min 1.59, max 1.82)","86.18 (min 85.50, max 87.40)","1.82 (min 1.58, max 1.95)"
   "4m","42.75 (min 40.80, max 44.60)","1.23 (min 1.11, max 1.32)","84.78 (min 82.00, max 87.30)","1.27 (min 1.19, max 1.45)"
   "4k","2.69 (min 2.30, max 2.85)","2.01 (min 1.79, max 2.15)","12.18 (min 9.36, max 13.50)","4.28 (min 3.39, max 4.62)"
   "256k","38.64 (min 37.50, max 40.20)","1.91 (min 1.78, max 2.06)","83.89 (min 81.80, max 85.00)","2.11 (min 2.00, max 2.30)"

.. csv-table:: MMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

   "1m","43.24 (min 41.80, max 45.80)","1.71 (min 1.48, max 1.86)","87.43 (min 85.80, max 88.20)","1.98 (min 1.49, max 2.21)"
   "4m","40.86 (min 37.80, max 42.40)","1.58 (min 1.24, max 1.87)","84.76 (min 82.20, max 87.30)","1.51 (min 1.34, max 1.63)"
   "4k","2.75 (min 2.36, max 2.87)","1.84 (min 1.45, max 2.00)","12.56 (min 9.94, max 13.10)","4.05 (min 3.40, max 4.35)"
   "256k","38.43 (min 37.00, max 39.90)","1.69 (min 1.41, max 1.87)","84.09 (min 81.90, max 85.00)","1.77 (min 1.50, max 1.96)"

MMC EXT4
========

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","am62xx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Write Raw CPU Load (%)","am62xx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Read Raw CPU Load (%)"

   "102400","10.82 (min 10.42, max 11.17)","0.82 (min 0.56, max 1.09)","11.09 (min 10.67, max 11.83)","0.77 (min 0.59, max 0.91)"
   "262144","10.71 (min 10.21, max 10.91)","0.70 (min 0.46, max 1.23)","11.06 (min 10.77, max 11.22)","0.79 (min 0.62, max 0.96)"
   "524288","10.72 (min 10.33, max 11.06)","0.65 (min 0.44, max 0.95)","11.15 (min 11.00, max 11.48)","0.75 (min 0.61, max 0.86)"
   "1048576","10.84 (min 10.22, max 11.26)","0.65 (min 0.45, max 0.89)","11.73 (min 11.05, max 12.03)","0.88 (min 0.72, max 1.07)"
   "5242880","10.86 (min 10.38, max 11.21)","0.65 (min 0.47, max 0.95)","11.98 (min 11.75, max 12.02)","0.94 (min 0.69, max 1.09)"

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write Raw CPU Load (%)","am62xx_lp_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read Raw CPU Load (%)"

   "102400","10.74 (min 10.00, max 11.16)","0.93 (min 0.72, max 1.39)","11.29 (min 10.76, max 11.82)","0.88 (min 0.82, max 1.01)"
   "262144","10.54 (min 9.47, max 11.00)","0.82 (min 0.65, max 1.43)","11.04 (min 10.74, max 11.23)","0.87 (min 0.77, max 1.08)"
   "524288","10.58 (min 9.90, max 10.98)","0.73 (min 0.63, max 0.96)","11.18 (min 11.01, max 11.52)","0.85 (min 0.71, max 0.96)"
   "1048576","10.76 (min 10.00, max 11.13)","0.73 (min 0.60, max 1.01)","11.47 (min 11.05, max 12.00)","1.15 (min 0.93, max 1.55)"
   "5242880","10.84 (min 10.34, max 11.19)","0.78 (min 0.59, max 1.05)","11.84 (min 10.85, max 12.02)","0.92 (min 0.80, max 1.03)"

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write Raw CPU Load (%)","am62xxsip_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read Raw CPU Load (%)"

   "102400","10.71 (min 10.15, max 11.03)","1.55 (min 0.47, max 3.35)","10.85 (min 10.67, max 11.08)","1.48 (min 1.27, max 1.76)"
   "262144","10.64 (min 10.43, max 10.89)","1.05 (min 0.36, max 2.38)","10.89 (min 10.74, max 11.20)","1.25 (min 0.65, max 1.87)"
   "524288","10.64 (min 10.39, max 10.94)","0.88 (min 0.34, max 1.70)","11.29 (min 10.87, max 11.51)","1.17 (min 0.75, max 1.67)"
   "1048576","11.06 (min 10.64, max 11.38)","1.12 (min 0.34, max 3.77)","11.69 (min 11.06, max 12.03)","1.35 (min 0.69, max 2.58)"
   "5242880","11.25 (min 10.91, max 11.38)","1.94 (min 0.35, max 5.63)","12.01 (min 12.00, max 12.03)","1.56 (min 0.83, max 2.50)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

***********
UBoot MMCSD
***********

UBOOT MMCSD FAT
===============

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

   "400000","33864.84 (min 27863.95, max 40960.00)","81920.00"
   "800000","42168.53 (min 34276.15, max 50257.67)","86630.19 (min 85333.33, max 87148.94)"
   "1000000","48028.45 (min 42010.26, max 54979.87)","89323.79 (min 88562.16, max 90021.98)"

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

   "400000","36916.06 (min 25440.99, max 41373.74)","79175.09 (min 57690.14, max 83591.84)"
   "800000","43862.16 (min 36900.90, max 49349.40)","87017.89 (min 86231.58, max 87148.94)"
   "1000000","47822.26 (min 42335.92, max 52512.82)","89671.37 (min 89043.48, max 90021.98)"

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

   "400000","38865.16 (min 33573.77, max 43574.47)","80500.79 (min 71859.65, max 83591.84)"
   "800000","43889.93 (min 38460.09, max 49951.22)","84657.45 (min 74472.73, max 88086.02)"
   "1000000","47067.68 (min 42445.60, max 51684.54)","87627.54 (min 81920.00, max 89530.05)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

**********
USB Driver
**********

USB Device Controller
=====================

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
   :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)","am62xxsip_sk-fs: Throughput (MB/sec)"

   "150","38.53 (min 35.00, max 44.10)","42.32 (min 42.00, max 42.60)","43.50 (min 42.60, max 44.20)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
   :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)","am62xxsip_sk-fs: Throughput (MB/sec)"

   "150","35.66 (min 30.60, max 43.10)","40.48 (min 40.00, max 41.00)","38.39 (min 37.10, max 39.50)"

*************
CRYPTO Driver
*************

OpenSSL Performance
===================

.. csv-table:: OpenSSL Performance
   :header: "Algorithm","Buffer Size (in bytes)","am62xx_lp_sk-fs: throughput (KBytes/Sec)","am62xx_sk-fs: throughput (KBytes/Sec)","am62xxsip_sk-fs: throughput (KBytes/Sec)"

   "aes-128-cbc","1024","21474.47 (min 20976.98, max 22031.70)","24501.19 (min 24296.79, max 24978.43)","24560.11 (min 24249.34, max 24810.50)"
   "aes-128-cbc","16","369.01 (min 360.01, max 377.97)","415.80 (min 387.19, max 471.78)","435.95 (min 386.77, max 461.96)"
   "aes-128-cbc","16384","121717.42 (min 120466.09, max 122601.47)","126638.31 (min 121896.96, max 135299.07)","131318.37 (min 125190.14, max 134671.02)"
   "aes-128-cbc","256","6275.68 (min 6193.49, max 6365.44)","7112.21 (min 6105.77, max 8061.27)","7502.24 (min 6557.01, max 7932.07)"
   "aes-128-cbc","64","1634.17 (min 1608.62, max 1670.74)","1879.43 (min 1781.97, max 2067.84)","1944.55 (min 1767.15, max 2040.60)"
   "aes-128-cbc","8192","92894.55 (min 91627.52, max 94169.77)","100387.95 (min 97667.75, max 104950.44)","102257.70 (min 98314.92, max 104742.91)"
   "aes-128-ecb","1024","22331.31 (min 21637.12, max 22930.43)","24755.03 (min 24329.22, max 25373.01)","24935.01 (min 24200.19, max 25385.30)"
   "aes-128-ecb","16","373.51 (min 364.43, max 380.78)","430.34 (min 405.36, max 478.88)","440.75 (min 380.00, max 478.63)"
   "aes-128-ecb","16384","122587.14 (min 121902.42, max 123251.37)","131678.21 (min 127391.06, max 139831.98)","136501.78 (min 131208.53, max 139416.92)"
   "aes-128-ecb","256","6598.63 (min 6449.41, max 6704.13)","7516.94 (min 7138.30, max 8204.80)","7801.21 (min 7075.75, max 8182.87)"
   "aes-128-ecb","64","1708.58 (min 1667.31, max 1736.47)","1955.81 (min 1864.26, max 2131.07)","1995.77 (min 1799.53, max 2113.17)"
   "aes-128-ecb","8192","94514.52 (min 92403.03, max 96692.91)","101629.50 (min 97959.94, max 108344.66)","104713.18 (min 98563.41, max 108366.51)"
   "aes-192-cbc","1024","21361.11 (min 20915.54, max 21960.70)","24568.72 (min 24250.71, max 25201.32)","24288.71 (min 23573.16, max 24570.54)"
   "aes-192-cbc","16","369.00 (min 360.76, max 377.71)","417.77 (min 390.05, max 471.24)","437.59 (min 386.68, max 463.81)"
   "aes-192-cbc","16384","114187.61 (min 113186.13, max 116189.87)","119969.11 (min 115627.35, max 127975.42)","123371.52 (min 117626.20, max 126877.70)"
   "aes-192-cbc","256","6227.97 (min 6151.42, max 6328.15)","7242.30 (min 6826.92, max 8057.69)","7459.02 (min 6671.02, max 7892.31)"
   "aes-192-cbc","64","1634.02 (min 1600.79, max 1668.20)","1888.55 (min 1790.06, max 2092.80)","1949.35 (min 1768.11, max 2047.55)"
   "aes-192-cbc","8192","90126.34 (min 87949.31, max 91581.10)","95513.26 (min 92069.89, max 101468.84)","97545.48 (min 93872.13, max 99999.74)"
   "aes-192-ecb","1024","22174.93 (min 21533.35, max 22818.47)","24731.08 (min 24388.61, max 25436.84)","24874.40 (min 24414.21, max 25299.29)"
   "aes-192-ecb","16","373.11 (min 364.65, max 380.65)","431.83 (min 403.18, max 482.22)","450.48 (min 400.90, max 477.46)"
   "aes-192-ecb","16384","119676.25 (min 118603.78, max 120777.39)","124434.66 (min 119625.05, max 131951.27)","128520.95 (min 122366.63, max 131760.13)"
   "aes-192-ecb","256","6546.98 (min 6436.52, max 6661.29)","7478.64 (min 7063.72, max 8184.83)","7749.33 (min 7027.20, max 8182.44)"
   "aes-192-ecb","64","1704.56 (min 1663.49, max 1731.90)","1952.39 (min 1838.74, max 2150.95)","2021.14 (min 1843.16, max 2128.04)"
   "aes-192-ecb","8192","92572.67 (min 92187.31, max 92992.85)","99959.69 (min 97236.31, max 104557.23)","101575.34 (min 97992.70, max 103620.61)"
   "aes-256-cbc","1024","21210.92 (min 20831.57, max 21823.15)","24415.00 (min 24275.29, max 24786.60)","24106.29 (min 23065.60, max 24443.90)"
   "aes-256-cbc","16","369.14 (min 359.97, max 378.02)","417.20 (min 390.58, max 468.61)","435.86 (min 388.01, max 463.51)"
   "aes-256-cbc","16384","106916.52 (min 105573.03, max 107921.41)","111707.93 (min 107692.03, max 118505.47)","113565.39 (min 107276.97, max 117648.04)"
   "aes-256-cbc","256","6192.68 (min 6086.66, max 6276.18)","7184.90 (min 6719.06, max 7964.59)","7355.76 (min 6598.83, max 7818.75)"
   "aes-256-cbc","64","1640.38 (min 1607.25, max 1661.38)","1886.95 (min 1786.75, max 2064.02)","1948.57 (min 1751.02, max 2050.03)"
   "aes-256-cbc","8192","84627.11 (min 84331.18, max 85267.80)","89980.02 (min 87203.84, max 95010.82)","91975.53 (min 86504.79, max 94625.79)"
   "aes-256-ecb","1024","22054.02 (min 21410.82, max 22849.54)","24748.89 (min 24334.34, max 25610.58)","24770.03 (min 24254.81, max 25092.44)"
   "aes-256-ecb","16","373.25 (min 363.88, max 380.30)","432.32 (min 404.86, max 484.92)","450.54 (min 401.62, max 476.13)"
   "aes-256-ecb","16384","111611.90 (min 110379.01, max 112552.62)","116719.62 (min 112705.54, max 124698.62)","119839.86 (min 114753.54, max 123191.30)"
   "aes-256-ecb","256","6515.43 (min 6428.33, max 6572.20)","7489.74 (min 7105.79, max 8192.17)","7695.60 (min 6989.82, max 8125.44)"
   "aes-256-ecb","64","1706.14 (min 1675.78, max 1729.79)","1954.80 (min 1851.41, max 2145.47)","2017.06 (min 1844.57, max 2115.95)"
   "aes-256-ecb","8192","89103.02 (min 87468.71, max 91458.22)","93897.61 (min 90617.17, max 99658.41)","96162.25 (min 92105.39, max 98314.92)"
   "sha256","1024","23975.81 (min 23270.74, max 24704.34)","28910.02 (min 27552.77, max 31705.77)","29720.05 (min 27393.37, max 31158.61)"
   "sha256","16","411.97 (min 406.08, max 416.66)","487.16 (min 470.18, max 524.41)","496.06 (min 465.23, max 515.29)"
   "sha256","16384","236539.90 (min 233046.02, max 244247.21)","266883.53 (min 261707.09, max 277659.65)","268367.49 (min 261657.94, max 273143.13)"
   "sha256","256","6343.17 (min 6239.49, max 6449.24)","7611.86 (min 7334.14, max 8184.83)","7776.71 (min 7321.69, max 8083.20)"
   "sha256","64","1619.61 (min 1595.41, max 1638.38)","1925.32 (min 1855.32, max 2069.16)","1961.30 (min 1845.70, max 2042.22)"
   "sha256","8192","152588.63 (min 148643.84, max 154462.89)","174880.54 (min 171081.73, max 180701.87)","175206.86 (min 170901.50, max 178713.94)"
   "sha512","1024","22781.31 (min 22459.05, max 22948.18)","25171.17 (min 24577.02, max 26655.40)","25478.79 (min 24591.36, max 26051.58)"
   "sha512","16","392.55 (min 382.39, max 401.65)","471.98 (min 449.21, max 511.33)","481.64 (min 451.50, max 498.54)"
   "sha512","16384","96527.02 (min 95944.70, max 97020.59)","108959.06 (min 107866.79, max 110318.93)","108985.76 (min 107795.80, max 109685.42)"
   "sha512","256","5947.11 (min 5801.22, max 6110.55)","6859.43 (min 6242.47, max 7740.16)","7103.90 (min 6250.92, max 7525.46)"
   "sha512","64","1568.17 (min 1523.69, max 1606.34)","1886.94 (min 1796.80, max 2043.61)","1925.42 (min 1806.70, max 1991.98)"
   "sha512","8192","78202.54 (min 77796.69, max 78845.27)","88692.05 (min 87239.34, max 91029.50)","89013.97 (min 87233.88, max 90125.65)"

.. csv-table:: OpenSSL CPU Load
   :header: "Algorithm","am62xx_lp_sk-fs: CPU Load","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: CPU Load"

   "aes-128-cbc","36.88 (min 36.00, max 37.00)","35.50 (min 35.00, max 36.00)","35.44 (min 35.00, max 36.00)"
   "aes-128-ecb","38.88 (min 37.00, max 40.00)","37.67 (min 37.00, max 38.00)","37.44 (min 36.00, max 39.00)"
   "aes-192-cbc","37.63 (min 37.00, max 38.00)","36.00 (min 35.00, max 37.00)","36.11 (min 35.00, max 37.00)"
   "aes-192-ecb","38.13 (min 37.00, max 39.00)","36.83 (min 36.00, max 37.00)","37.11 (min 36.00, max 38.00)"
   "aes-256-cbc","36.88 (min 36.00, max 37.00)","35.50 (min 35.00, max 36.00)","35.78 (min 35.00, max 36.00)"
   "aes-256-ecb","37.50 (min 37.00, max 38.00)","36.67 (min 35.00, max 37.00)","36.78 (min 36.00, max 38.00)"
   "sha256","96.63 (min 94.00, max 98.00)","97.17 (min 95.00, max 98.00)","97.00 (min 95.00, max 98.00)"
   "sha512","96.63 (min 94.00, max 98.00)","97.17 (min 95.00, max 98.00)","96.89 (min 94.00, max 98.00)"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc

IPSec Hardware Performance
==========================

Note: queue\_len is set to 300 and software fallback threshold set to 9
to enable software support for optimal performance

.. csv-table:: IPSec Hardware Performance
   :header: "Algorithm","am62xx_sk-fs: Throughput (Mbps)","am62xx_sk-fs: Packets/Sec","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: Throughput (Mbps)","am62xxsip_sk-fs: Packets/Sec","am62xxsip_sk-fs: CPU Load"

   "aes128","0.50 (min 0.00, max 2.00)","0.00","23.06 (min 22.43, max 23.62)","1.40 (min 0.00, max 2.40)","0.00","18.52 (min 14.06, max 23.54)"
   "aes192","33.82 (min 0.20, max 61.10)","2.67 (min 0.00, max 5.00)","51.42 (min 50.26, max 52.23)","45.87 (min 0.20, max 173.80)","3.86 (min 0.00, max 15.00)","72.39 (min 50.15, max 94.66)"
   "aes256","52.03 (min 0.20, max 206.10)","4.14 (min 0.00, max 18.00)","47.59 (min 28.01, max 52.18)","89.51 (min 37.30, max 202.80)","7.57 (min 3.00, max 18.00)","77.86 (min 50.86, max 102.36)"

IPSec Software Performance
==========================

.. csv-table:: IPSec Software Performance
   :header: "Algorithm","am62xx_sk-fs: Throughput (Mbps)","am62xx_sk-fs: Packets/Sec","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: Throughput (Mbps)","am62xxsip_sk-fs: Packets/Sec","am62xxsip_sk-fs: CPU Load"

   "aes128","421.81 (min 401.60, max 456.90)","37.14 (min 35.00, max 40.00)","38.11 (min 28.99, max 51.93)","400.42 (min 243.40, max 446.60)","35.00 (min 21.00, max 39.00)","50.04 (min 27.27, max 72.97)"
   "aes192","355.12 (min 6.20, max 450.30)","31.17 (min 0.00, max 40.00)","35.24 (min 23.64, max 70.44)","0.00","0.00","73.16"
   "aes256","408.16 (min 404.70, max 410.50)","36.00","31.31 (min 29.24, max 39.12)","426.63 (min 403.40, max 451.20)","37.63 (min 35.00, max 40.00)","48.86 (min 29.29, max 96.99)"

