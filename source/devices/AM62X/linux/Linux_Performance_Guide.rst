
#################################
 Linux 12.00.00 Performance Guide
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

|

*****************
System Benchmarks
*****************

|

LMBench
=======

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

    "af_unix_sock_stream_latency (microsec)","29.86 (min 25.84, max 32.02)","25.62 (min 23.44, max 27.72)","27.27 (min 26.72, max 27.91)"
    "af_unix_socket_stream_bandwidth (mb\s)","550.16 (min 537.95, max 572.90)","656.18 (min 589.74, max 737.01)","726.70 (min 681.24, max 808.97)"
    "bw_file_rd-io-1mb (mb/s)","839.44 (min 808.93, max 863.71)","1022.11 (min 929.51, max 1115.86)","936.16 (min 877.35, max 1052.08)"
    "bw_file_rd-o2c-1mb (mb/s)","443.48 (min 412.09, max 462.11)","551.30 (min 478.85, max 640.82)","514.92 (min 467.58, max 584.88)"
    "bw_mem-bcopy-16mb (mb/s)","680.62 (min 656.28, max 700.77)","839.11 (min 760.85, max 924.59)","773.95 (min 704.44, max 876.66)"
    "bw_mem-bcopy-1mb (mb/s)","720.72 (min 682.83, max 770.18)","927.90 (min 789.89, max 1060.82)","860.74 (min 767.02, max 1018.50)"
    "bw_mem-bcopy-2mb (mb/s)","685.52 (min 657.14, max 733.41)","874.06 (min 757.86, max 992.56)","803.28 (min 735.74, max 919.68)"
    "bw_mem-bcopy-4mb (mb/s)","702.03 (min 684.93, max 721.11)","888.30 (min 791.14, max 993.05)","786.86 (min 715.44, max 901.51)"
    "bw_mem-bcopy-8mb (mb/s)","716.08 (min 691.20, max 740.33)","905.04 (min 794.20, max 1018.20)","770.79 (min 699.97, max 901.61)"
    "bw_mem-bzero-16mb (mb/s)","1734.34 (min 1684.21, max 1768.93)","1940.25 (min 1748.25, max 2126.25)","1869.45 (min 1731.98, max 2129.08)"
    "bw_mem-bzero-1mb (mb/s)","1223.03 (min 682.83, max 1767.41)","1427.89 (min 789.89, max 2127.28)","1360.25 (min 767.02, max 2129.55)"
    "bw_mem-bzero-2mb (mb/s)","1205.38 (min 657.14, max 1767.41)","1400.07 (min 757.86, max 2124.65)","1331.83 (min 735.74, max 2129.55)"
    "bw_mem-bzero-4mb (mb/s)","1215.14 (min 684.93, max 1771.22)","1409.99 (min 791.14, max 2126.91)","1323.07 (min 715.44, max 2130.30)"
    "bw_mem-bzero-8mb (mb/s)","1225.86 (min 691.20, max 1781.14)","1421.45 (min 794.20, max 2124.83)","1319.03 (min 699.97, max 2129.36)"
    "bw_mem-cp-16mb (mb/s)","395.42 (min 381.01, max 405.48)","508.67 (min 443.12, max 571.82)","439.42 (min 411.29, max 492.47)"
    "bw_mem-cp-1mb (mb/s)","1133.11 (min 381.10, max 1932.74)","1289.61 (min 438.08, max 2283.11)","1237.66 (min 411.47, max 2268.00)"
    "bw_mem-cp-2mb (mb/s)","1104.43 (min 374.60, max 1854.94)","1271.76 (min 439.13, max 2205.07)","1187.72 (min 401.53, max 2207.10)"
    "bw_mem-cp-4mb (mb/s)","1093.19 (min 398.96, max 1817.08)","1249.43 (min 434.40, max 2166.46)","1175.21 (min 410.47, max 2171.16)"
    "bw_mem-cp-8mb (mb/s)","1096.97 (min 413.05, max 1805.67)","1254.34 (min 479.82, max 2153.72)","1168.07 (min 416.45, max 2156.04)"
    "bw_mem-fcp-16mb (mb/s)","680.05 (min 662.11, max 693.36)","816.48 (min 729.13, max 905.80)","843.99 (min 759.88, max 965.43)"
    "bw_mem-fcp-1mb (mb/s)","1253.14 (min 754.72, max 1767.41)","1450.43 (min 856.60, max 2127.28)","1363.96 (min 784.81, max 2129.55)"
    "bw_mem-fcp-2mb (mb/s)","1239.40 (min 720.46, max 1767.41)","1443.63 (min 838.57, max 2124.65)","1367.84 (min 795.07, max 2129.55)"
    "bw_mem-fcp-4mb (mb/s)","1248.90 (min 737.60, max 1771.22)","1453.26 (min 858.65, max 2126.91)","1347.89 (min 756.86, max 2130.30)"
    "bw_mem-fcp-8mb (mb/s)","1261.19 (min 762.56, max 1781.14)","1473.56 (min 882.90, max 2124.83)","1360.30 (min 773.92, max 2129.36)"
    "bw_mem-frd-16mb (mb/s)","1044.45 (min 1007.81, max 1077.44)","1271.34 (min 1114.83, max 1446.00)","1170.00 (min 1098.75, max 1306.66)"
    "bw_mem-frd-1mb (mb/s)","968.42 (min 754.72, max 1179.84)","1192.10 (min 856.60, max 1573.25)","1100.20 (min 784.81, max 1542.61)"
    "bw_mem-frd-2mb (mb/s)","886.57 (min 720.46, max 1043.30)","1107.97 (min 838.57, max 1432.15)","1016.36 (min 795.07, max 1294.92)"
    "bw_mem-frd-4mb (mb/s)","902.01 (min 737.60, max 1070.38)","1098.26 (min 858.65, max 1435.49)","1011.59 (min 756.86, max 1366.12)"
    "bw_mem-frd-8mb (mb/s)","908.57 (min 762.56, max 1068.66)","1141.53 (min 882.90, max 1442.48)","1003.00 (min 773.92, max 1375.52)"
    "bw_mem-fwr-16mb (mb/s)","1744.19 (min 1697.07, max 1785.91)","1948.47 (min 1750.55, max 2147.65)","1878.33 (min 1745.39, max 2138.47)"
    "bw_mem-fwr-1mb (mb/s)","1510.52 (min 1125.91, max 1932.74)","1739.87 (min 1273.89, max 2283.11)","1668.01 (min 1199.86, max 2268.00)"
    "bw_mem-fwr-2mb (mb/s)","1411.88 (min 981.84, max 1854.94)","1648.53 (min 1105.58, max 2205.07)","1546.88 (min 1073.73, max 2207.10)"
    "bw_mem-fwr-4mb (mb/s)","1403.67 (min 968.05, max 1817.08)","1597.72 (min 1042.75, max 2166.46)","1544.82 (min 1092.60, max 2171.16)"
    "bw_mem-fwr-8mb (mb/s)","1397.79 (min 990.71, max 1805.67)","1616.90 (min 1130.26, max 2153.72)","1523.88 (min 985.95, max 2156.04)"
    "bw_mem-rd-16mb (mb/s)","1061.45 (min 1012.98, max 1092.75)","1296.52 (min 1154.57, max 1453.09)","1198.89 (min 1107.96, max 1370.68)"
    "bw_mem-rd-1mb (mb/s)","884.55 (min 556.79, max 1234.35)","1115.27 (min 648.09, max 1650.77)","1022.60 (min 579.37, max 1591.51)"
    "bw_mem-rd-2mb (mb/s)","783.16 (min 486.38, max 1073.92)","977.91 (min 568.99, max 1439.63)","892.41 (min 530.50, max 1389.61)"
    "bw_mem-rd-4mb (mb/s)","813.40 (min 502.07, max 1089.32)","1023.00 (min 653.17, max 1426.02)","912.16 (min 568.83, max 1383.13)"
    "bw_mem-rd-8mb (mb/s)","851.74 (min 577.95, max 1085.19)","1083.52 (min 764.31, max 1438.33)","921.44 (min 590.23, max 1383.13)"
    "bw_mem-rdwr-16mb (mb/s)","672.82 (min 659.06, max 688.62)","903.05 (min 789.77, max 1031.26)","653.37 (min 586.40, max 771.05)"
    "bw_mem-rdwr-1mb (mb/s)","480.16 (min 381.10, max 596.48)","615.93 (min 438.08, max 812.08)","547.06 (min 411.47, max 708.59)"
    "bw_mem-rdwr-2mb (mb/s)","448.92 (min 374.60, max 515.86)","580.74 (min 439.13, max 772.80)","515.12 (min 401.53, max 702.86)"
    "bw_mem-rdwr-4mb (mb/s)","489.55 (min 398.96, max 603.68)","640.10 (min 434.40, max 881.06)","520.62 (min 410.47, max 678.89)"
    "bw_mem-rdwr-8mb (mb/s)","527.31 (min 413.05, max 674.02)","680.65 (min 479.82, max 924.11)","531.07 (min 416.45, max 722.09)"
    "bw_mem-wr-16mb (mb/s)","694.95 (min 661.76, max 737.02)","927.61 (min 813.05, max 1038.89)","644.35 (min 583.58, max 753.15)"
    "bw_mem-wr-1mb (mb/s)","562.90 (min 544.86, max 596.48)","732.36 (min 626.37, max 848.61)","638.92 (min 560.01, max 764.29)"
    "bw_mem-wr-2mb (mb/s)","501.45 (min 476.53, max 547.20)","671.22 (min 559.91, max 772.80)","584.84 (min 518.87, max 702.86)"
    "bw_mem-wr-4mb (mb/s)","565.99 (min 502.07, max 616.71)","763.18 (min 653.06, max 887.51)","608.59 (min 534.90, max 728.07)"
    "bw_mem-wr-8mb (mb/s)","638.16 (min 577.87, max 679.69)","846.88 (min 708.97, max 1013.04)","632.04 (min 560.85, max 747.45)"
    "bw_mmap_rd-mo-1mb (mb/s)","1152.80 (min 1115.24, max 1190.27)","1410.30 (min 1246.88, max 1588.42)","1348.64 (min 1240.47, max 1557.90)"
    "bw_mmap_rd-o2c-1mb (mb/s)","445.75 (min 410.12, max 471.70)","553.69 (min 497.02, max 669.46)","506.34 (min 470.00, max 572.08)"
    "bw_pipe (mb/s)","463.99 (min 453.23, max 474.31)","567.38 (min 491.98, max 625.68)","511.98 (min 499.61, max 534.49)"
    "bw_unix (mb/s)","550.16 (min 537.95, max 572.90)","656.18 (min 589.74, max 737.01)","726.70 (min 681.24, max 808.97)"
    "lat_connect (us)","73.77 (min 59.56, max 87.60)","63.98 (min 51.45, max 76.63)","75.50 (min 71.71, max 77.82)"
    "lat_ctx-2-128k (us)","10.12 (min 8.90, max 12.47)","9.10 (min 8.05, max 13.66)","11.68 (min 8.45, max 16.33)"
    "lat_ctx-2-256k (us)","35.67 (min 9.10, max 85.73)","32.53 (min 7.09, max 79.24)","26.36 (min 8.58, max 58.00)"
    "lat_ctx-4-128k (us)","24.74 (min 9.55, max 55.08)","24.06 (min 8.02, max 57.28)","32.59 (min 9.40, max 49.60)"
    "lat_ctx-4-256k (us)","12.58 (min 10.84, max 15.20)","70.36 (min 7.41, max 195.04)","120.21 (min 15.56, max 197.58)"
    "lat_fs-0k (num_files)","230.17 (min 206.00, max 253.00)","259.67 (min 222.00, max 292.00)","247.67 (min 226.00, max 266.00)"
    "lat_fs-10k (num_files)","97.83 (min 89.00, max 115.00)","112.83 (min 101.00, max 150.00)","104.00 (min 100.00, max 111.00)"
    "lat_fs-1k (num_files)","145.00 (min 129.00, max 160.00)","166.83 (min 141.00, max 191.00)","156.67 (min 149.00, max 161.00)"
    "lat_fs-4k (num_files)","142.17 (min 126.00, max 155.00)","161.83 (min 130.00, max 190.00)","149.00 (min 142.00, max 159.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","56.02 (min 54.49, max 58.17)","46.44 (min 41.29, max 51.32)","49.54 (min 43.10, max 52.89)"
    "lat_mem_rd-stride128-sz125k (ns)","6.24 (min 6.20, max 6.29)","5.57 (min 5.55, max 5.59)","5.55 (min 5.54, max 5.56)"
    "lat_mem_rd-stride128-sz250k (ns)","6.56 (min 6.53, max 6.65)","5.84 (min 5.83, max 5.84)","5.83 (min 5.83, max 5.84)"
    "lat_mem_rd-stride128-sz31k (ns)","3.82 (min 2.42, max 5.23)","3.24 (min 2.16, max 4.19)","3.15 (min 2.16, max 3.65)"
    "lat_mem_rd-stride128-sz50 (ns)","2.40","2.15","2.15"
    "lat_mem_rd-stride128-sz500k (ns)","19.03 (min 17.22, max 21.61)","16.13 (min 12.75, max 18.51)","14.66 (min 13.14, max 16.84)"
    "lat_mem_rd-stride128-sz62k (ns)","5.78 (min 5.36, max 5.87)","5.24 (min 5.22, max 5.28)","5.01 (min 4.52, max 5.26)"
    "lat_mmap-1m (us)","64.33 (min 57.00, max 71.00)","57.00 (min 50.00, max 62.00)","56.33 (min 48.00, max 63.00)"
    "lat_ops-double-add (ns)","3.21","2.86","2.86"
    "lat_ops-double-div (ns)","17.65 (min 17.63, max 17.66)","15.75 (min 15.73, max 15.76)","15.74 (min 15.74, max 15.75)"
    "lat_ops-double-mul (ns)","3.21","2.86","2.86"
    "lat_ops-float-add (ns)","3.21","2.86","2.86"
    "lat_ops-float-div (ns)","10.42 (min 10.42, max 10.43)","9.30 (min 9.30, max 9.31)","9.30"
    "lat_ops-float-mul (ns)","3.21","2.86","2.86"
    "lat_ops-int-add (ns)","0.80","0.72","0.72"
    "lat_ops-int-bit (ns)","0.53","0.48","0.48"
    "lat_ops-int-div (ns)","4.81","4.29 (min 4.29, max 4.30)","4.30 (min 4.29, max 4.30)"
    "lat_ops-int-mod (ns)","5.08","4.53","4.54 (min 4.53, max 4.54)"
    "lat_ops-int-mul (ns)","3.46 (min 3.40, max 3.49)","3.09 (min 3.04, max 3.12)","3.12 (min 3.11, max 3.12)"
    "lat_ops-int64-add (ns)","0.80","0.72","0.72"
    "lat_ops-int64-bit (ns)","0.53 (min 0.53, max 0.54)","0.48","0.48"
    "lat_ops-int64-div (ns)","7.62 (min 7.61, max 7.63)","6.80 (min 6.79, max 6.80)","6.80"
    "lat_ops-int64-mod (ns)","5.88 (min 5.88, max 5.89)","5.25","5.25 (min 5.24, max 5.25)"
    "lat_ops-int64-mul (ns)","3.99 (min 3.97, max 4.07)","3.56 (min 3.54, max 3.64)","3.56 (min 3.54, max 3.59)"
    "lat_pagefault (us)","0.68 (min 0.66, max 0.70)","0.58 (min 0.52, max 0.63)","1.69 (min 1.53, max 1.78)"
    "lat_pipe (us)","24.07 (min 23.56, max 24.62)","21.52 (min 21.04, max 22.12)","21.79 (min 21.03, max 22.35)"
    "lat_proc-exec (us)","1130.37 (min 1095.20, max 1173.20)","936.72 (min 840.17, max 1059.33)","1003.69 (min 866.86, max 1074.80)"
    "lat_proc-fork (us)","1104.61 (min 926.33, max 1739.33)","818.28 (min 731.25, max 906.50)","855.18 (min 733.71, max 943.67)"
    "lat_proc-proccall (us)","0.01","0.01","0.01"
    "lat_select (us)","35.44 (min 35.10, max 35.63)","31.58 (min 31.34, max 32.00)","31.59 (min 31.47, max 31.79)"
    "lat_sem (us)","3.05 (min 2.72, max 3.89)","2.55 (min 2.34, max 2.82)","2.92 (min 2.87, max 2.97)"
    "lat_sig-catch (us)","6.27 (min 6.11, max 6.44)","5.60 (min 5.46, max 5.72)","5.55 (min 5.48, max 5.67)"
    "lat_sig-install (us)","0.73 (min 0.65, max 0.80)","0.65 (min 0.58, max 0.72)","0.60 (min 0.58, max 0.63)"
    "lat_sig-prot (us)","0.96 (min 0.83, max 1.10)","0.85 (min 0.75, max 0.92)","0.81 (min 0.76, max 0.86)"
    "lat_syscall-fstat (us)","2.04 (min 1.97, max 2.12)","1.81 (min 1.76, max 1.89)","1.80 (min 1.74, max 1.88)"
    "lat_syscall-null (us)","0.49 (min 0.41, max 0.57)","0.44 (min 0.37, max 0.51)","0.37"
    "lat_syscall-open (us)","222.13 (min 175.60, max 296.65)","181.80 (min 156.61, max 200.77)","169.27 (min 160.19, max 184.77)"
    "lat_syscall-read (us)","0.84 (min 0.82, max 0.89)","0.75 (min 0.73, max 0.79)","0.74 (min 0.73, max 0.74)"
    "lat_syscall-stat (us)","4.64 (min 4.46, max 4.76)","4.16 (min 3.99, max 4.28)","4.24 (min 4.23, max 4.25)"
    "lat_syscall-write (us)","0.79 (min 0.75, max 0.84)","0.70 (min 0.67, max 0.74)","0.67"
    "lat_tcp (us)","1.00 (min 0.85, max 1.14)","0.89 (min 0.76, max 1.02)","0.76"
    "lat_unix (us)","29.86 (min 25.84, max 32.02)","25.62 (min 23.44, max 27.72)","27.27 (min 26.72, max 27.91)"
    "latency_for_0.50_mb_block_size (nanosec)","19.03 (min 17.22, max 21.61)","16.13 (min 12.75, max 18.51)","14.66 (min 13.14, max 16.84)"
    "latency_for_1.00_mb_block_size (nanosec)","28.01 (min 0.00, max 58.17)","23.22 (min 0.00, max 51.32)","24.77 (min 0.00, max 52.89)"
    "pipe_bandwidth (mb\s)","463.99 (min 453.23, max 474.31)","567.38 (min 491.98, max 625.68)","511.98 (min 499.61, max 534.49)"
    "pipe_latency (microsec)","24.07 (min 23.56, max 24.62)","21.52 (min 21.04, max 22.12)","21.79 (min 21.03, max 22.35)"
    "procedure_call (microsec)","0.01","0.01","0.01"
    "select_on_200_tcp_fds (microsec)","35.44 (min 35.10, max 35.63)","31.58 (min 31.34, max 32.00)","31.59 (min 31.47, max 31.79)"
    "semaphore_latency (microsec)","3.05 (min 2.72, max 3.89)","2.55 (min 2.34, max 2.82)","2.92 (min 2.87, max 2.97)"
    "signal_handler_latency (microsec)","0.73 (min 0.65, max 0.80)","0.65 (min 0.58, max 0.72)","0.60 (min 0.58, max 0.63)"
    "signal_handler_overhead (microsec)","6.27 (min 6.11, max 6.44)","5.60 (min 5.46, max 5.72)","5.55 (min 5.48, max 5.67)"
    "tcp_ip_connection_cost_to_localhost (microsec)","73.77 (min 59.56, max 87.60)","63.98 (min 51.45, max 76.63)","75.50 (min 71.71, max 77.82)"
    "tcp_latency_using_localhost (microsec)","1.00 (min 0.85, max 1.14)","0.89 (min 0.76, max 1.02)","0.76"

Dhrystone
=========

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

    "cpu_clock (mhz)","1250.00","1400.00","1400.00"
    "dhrystone_per_mhz (dmips/mhz)","2.76 (min 2.70, max 2.80)","2.75 (min 2.60, max 2.90)","2.77 (min 2.70, max 2.80)"
    "dhrystone_per_second (dhrystonep)","6027183.60 (min 5882353.00, max 6250000.00)","6789289.58 (min 6451613.00, max 7142857.00)","6819923.17 (min 6666666.50, max 6896551.50)"

Whetstone
=========

Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "whetstone (mips)","4444.43 (min 3333.30, max 5000.00)","5000.00","5000.00"

Linpack
=======

Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "linpack (kflops)","515140.50 (min 508416.00, max 518513.00)","581699.00 (min 581477.00, max 581921.00)","578855.50 (min 578148.00, max 579563.00)"

NBench
======

NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "assignment (iterations)","12.63 (min 12.55, max 12.73)","14.16 (min 14.15, max 14.17)","14.14 (min 14.12, max 14.15)"
    "fourier (iterations)","18561.17 (min 18558.00, max 18567.00)","20791.00 (min 20785.00, max 20798.00)","20792.25 (min 20790.00, max 20796.00)"
    "fp_emulation (iterations)","182.44 (min 182.30, max 182.54)","204.36 (min 204.17, max 204.44)","204.39 (min 204.37, max 204.41)"
    "huffman (iterations)","1058.38 (min 1049.10, max 1063.20)","1187.26 (min 1174.70, max 1191.10)","1190.58 (min 1190.00, max 1190.90)"
    "idea (iterations)","2738.27 (min 2737.60, max 2738.60)","3066.96 (min 3066.60, max 3067.30)","3067.23 (min 3067.00, max 3067.40)"
    "lu_decomposition (iterations)","472.09 (min 469.76, max 474.80)","530.93 (min 526.72, max 532.68)","529.40 (min 526.80, max 532.45)"
    "neural_net (iterations)","8.60 (min 8.51, max 8.64)","9.65 (min 9.53, max 9.68)","9.68 (min 9.67, max 9.68)"
    "numeric_sort (iterations)","482.67 (min 477.04, max 484.80)","538.40 (min 533.26, max 542.91)","537.80 (min 527.29, max 542.82)"
    "string_sort (iterations)","150.20 (min 150.14, max 150.27)","168.20 (min 168.14, max 168.29)","168.19 (min 168.17, max 168.21)"

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

::

    stream_c

.. csv-table:: Stream Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "add (mb/s)","1376.20 (min 1329.10, max 1411.30)","1580.70 (min 1463.60, max 1811.00)","1704.70"
    "copy (mb/s)","1462.62 (min 1366.90, max 1515.60)","1838.92 (min 1650.20, max 2245.20)","1876.80"
    "scale (mb/s)","1565.95 (min 1474.00, max 1610.80)","1948.28 (min 1786.10, max 2285.60)","1921.20"
    "triad (mb/s)","1349.88 (min 1303.10, max 1385.40)","1615.13 (min 1494.30, max 1856.90)","1667.70"

CoreMarkPro
===========

CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","37.27 (min 37.04, max 37.59)","41.73 (min 41.49, max 41.84)","41.84 (min 41.67, max 42.02)"
    "core (workloads/)","0.27","0.30","0.30"
    "coremark-pro ()","793.57 (min 764.61, max 819.06)","888.50 (min 846.80, max 928.38)","879.40 (min 859.11, max 912.05)"
    "linear_alg-mid-100x100-sp (workloads/)","13.09 (min 13.08, max 13.11)","14.67 (min 14.66, max 14.70)","14.68 (min 14.68, max 14.69)"
    "loops-all-mid-10k-sp (workloads/)","0.60 (min 0.60, max 0.62)","0.67 (min 0.67, max 0.70)","0.68 (min 0.66, max 0.70)"
    "nnet_test (workloads/)","0.96 (min 0.95, max 0.96)","1.08","1.08 (min 1.07, max 1.08)"
    "parser-125k (workloads/)","7.65 (min 7.41, max 8.00)","8.52 (min 8.13, max 8.85)","8.68 (min 8.26, max 9.01)"
    "radix2-big-64k (workloads/)","44.85 (min 33.86, max 54.28)","51.45 (min 34.28, max 69.88)","44.89 (min 39.02, max 55.47)"
    "sha-test (workloads/)","71.77 (min 70.92, max 72.46)","80.12 (min 78.74, max 81.30)","80.86 (min 80.65, max 81.30)"
    "zip-test (workloads/)","19.07 (min 18.52, max 20.00)","21.37 (min 20.83, max 22.22)","21.28 (min 20.83, max 21.74)"

.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am62xx_lp_sk-fs: perf","am62xx_sk-fs: perf","am62xxsip_sk-fs: perf"

    "cjpeg-rose7-preset (workloads/)","73.38 (min 71.94, max 74.07)","82.31 (min 81.30, max 83.33)","83.10 (min 82.64, max 83.33)"
    "core (workloads/)","0.54","0.60","0.60"
    "coremark-pro ()","1356.04 (min 1322.58, max 1417.19)","1525.15 (min 1472.72, max 1594.34)","1560.33 (min 1506.68, max 1589.98)"
    "linear_alg-mid-100x100-sp (workloads/)","26.15 (min 26.12, max 26.18)","29.32 (min 29.29, max 29.34)","29.33 (min 29.33, max 29.34)"
    "loops-all-mid-10k-sp (workloads/)","1.05 (min 1.02, max 1.12)","1.18 (min 1.14, max 1.26)","1.21 (min 1.15, max 1.25)"
    "nnet_test (workloads/)","1.92","2.15","2.15"
    "parser-125k (workloads/)","12.19 (min 10.81, max 13.42)","13.68 (min 11.63, max 16.00)","14.12 (min 12.90, max 15.38)"
    "radix2-big-64k (workloads/)","35.34 (min 32.03, max 46.62)","40.11 (min 36.05, max 45.74)","44.46 (min 40.00, max 49.31)"
    "sha-test (workloads/)","140.33 (min 136.99, max 144.93)","156.69 (min 153.85, max 158.73)","160.44 (min 158.73, max 161.29)"
    "zip-test (workloads/)","35.29 (min 33.90, max 36.36)","40.31 (min 38.46, max 42.55)","40.60 (min 38.46, max 41.67)"

MultiBench
==========

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

    "4m-check (workloads/)","272.76 (min 272.01, max 273.58)","320.84 (min 305.89, max 373.86)","332.22 (min 303.95, max 360.49)"
    "4m-check-reassembly (workloads/)","56.07 (min 55.77, max 56.34)","72.48 (min 62.27, max 86.51)","75.46 (min 73.05, max 77.88)"
    "4m-check-reassembly-tcp (workloads/)","37.54 (min 37.43, max 37.65)","45.68 (min 41.81, max 50.00)","48.46 (min 47.89, max 49.02)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","21.53 (min 21.34, max 21.79)","25.33 (min 24.19, max 29.50)","26.49 (min 23.87, max 29.11)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","1.57 (min 1.57, max 1.58)","1.77 (min 1.74, max 1.83)","1.71 (min 1.71, max 1.72)"
    "4m-cmykw2 (workloads/)","176.42 (min 175.59, max 176.99)","205.20 (min 197.04, max 236.97)","217.95 (min 196.66, max 239.23)"
    "4m-cmykw2-rotatew2 (workloads/)","32.81 (min 32.66, max 33.09)","39.43 (min 37.11, max 45.21)","42.08 (min 38.12, max 46.05)"
    "4m-reassembly (workloads/)","43.05 (min 42.50, max 43.90)","61.98 (min 47.62, max 85.25)","68.29 (min 57.97, max 78.62)"
    "4m-rotatew2 (workloads/)","38.84 (min 38.55, max 39.03)","45.22 (min 42.18, max 51.87)","47.93 (min 44.39, max 51.47)"
    "4m-tcp-mixed (workloads/)","98.36 (min 97.56, max 98.77)","113.23 (min 111.11, max 123.08)","116.62 (min 111.11, max 122.14)"
    "4m-x264w2 (workloads/)","1.58 (min 1.52, max 1.63)","1.82 (min 1.72, max 1.91)","1.84 (min 1.82, max 1.86)"
    "empty-wld (workloads/)","1.00","1.00","1.00"
    "idct-4m (workloads/)","16.64 (min 16.60, max 16.66)","18.99 (min 18.49, max 19.69)","19.33 (min 19.05, max 19.61)"
    "idct-4mw1 (workloads/)","16.65 (min 16.64, max 16.66)","18.99 (min 18.49, max 19.69)","19.34 (min 19.05, max 19.62)"
    "ippktcheck-4m (workloads/)","270.95 (min 270.27, max 271.62)","320.65 (min 303.51, max 369.22)","334.19 (min 305.44, max 362.95)"
    "ippktcheck-4mw1 (workloads/)","273.45 (min 272.78, max 274.42)","321.05 (min 306.26, max 372.58)","334.33 (min 306.19, max 362.48)"
    "ipres-4m (workloads/)","53.57 (min 53.42, max 53.71)","64.68 (min 60.24, max 74.44)","67.79 (min 62.66, max 72.92)"
    "ipres-4mw1 (workloads/)","53.94 (min 53.51, max 54.27)","64.58 (min 60.44, max 74.93)","67.68 (min 62.55, max 72.82)"
    "md5-4m (workloads/)","22.10 (min 21.90, max 22.20)","25.32 (min 24.70, max 26.60)","26.04 (min 25.27, max 26.80)"
    "md5-4mw1 (workloads/)","22.29 (min 22.23, max 22.34)","25.25 (min 24.69, max 26.81)","25.90 (min 24.91, max 26.89)"
    "rgbcmyk-4m (workloads/)","56.14 (min 56.04, max 56.32)","63.75 (min 63.01, max 64.89)","63.24 (min 61.79, max 64.70)"
    "rgbcmyk-4mw1 (workloads/)","56.08 (min 55.96, max 56.29)","63.86 (min 63.07, max 64.91)","64.11 (min 63.47, max 64.75)"
    "rotate-4ms1 (workloads/)","16.34 (min 16.32, max 16.35)","19.50 (min 18.34, max 21.71)","19.82 (min 18.13, max 21.51)"
    "rotate-4ms1w1 (workloads/)","16.39 (min 16.37, max 16.41)","19.44 (min 18.23, max 21.62)","19.79 (min 18.18, max 21.40)"
    "rotate-4ms64 (workloads/)","16.53 (min 16.52, max 16.56)","19.61 (min 18.38, max 21.89)","20.05 (min 18.32, max 21.78)"
    "rotate-4ms64w1 (workloads/)","16.48 (min 16.46, max 16.50)","19.68 (min 18.38, max 22.23)","20.04 (min 18.34, max 21.75)"
    "x264-4mq (workloads/)","0.49 (min 0.48, max 0.50)","0.56 (min 0.55, max 0.57)","0.56 (min 0.56, max 0.57)"
    "x264-4mqw1 (workloads/)","0.49 (min 0.49, max 0.50)","0.56 (min 0.54, max 0.57)","0.56"

|

Boot-time Measurement
=====================

Boot media: MMCSD
-----------------

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am62xx_lp_sk-fs: Boot time in seconds: avg(min,max)","am62xx_sk-fs: Boot time in seconds: avg(min,max)","am62xxsip_sk-fs: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","18.28 (min 17.43, max 19.66)","18.15 (min 17.32, max 36.26)","18.15 (min 17.28, max 20.55)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

|

ALSA SoC Audio
==============

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)","am62xxsip_sk-fs: Throughput (bits/sec)","am62xxsip_sk-fs: CPU Load (%)"

    "11025","352797.40 (min 352797.00, max 352798.00)","0.20 (min 0.17, max 0.31)","352798.20 (min 352797.00, max 352799.00)","0.22 (min 0.13, max 0.32)","352799.67 (min 352799.00, max 352800.00)","0.30 (min 0.25, max 0.35)"
    "16000","511997.20 (min 511996.00, max 511998.00)","0.14 (min 0.12, max 0.15)","511998.00 (min 511997.00, max 512000.00)","0.15 (min 0.09, max 0.28)","512001.00 (min 511999.00, max 512002.00)","0.14 (min 0.13, max 0.14)"
    "22050","705591.80 (min 705591.00, max 705593.00)","0.18 (min 0.17, max 0.21)","705594.00 (min 705592.00, max 705596.00)","0.17 (min 0.15, max 0.22)","705593.67 (min 705593.00, max 705595.00)","0.19 (min 0.18, max 0.20)"
    "24000","705594.40 (min 705593.00, max 705595.00)","0.20 (min 0.19, max 0.23)","705596.00 (min 705594.00, max 705598.00)","0.19 (min 0.16, max 0.24)","705598.33 (min 705597.00, max 705599.00)","0.19 (min 0.18, max 0.20)"
    "32000","1023992.60 (min 1023991.00, max 1023994.00)","0.12 (min 0.11, max 0.13)","1023995.00 (min 1023992.00, max 1023998.00)","0.28 (min 0.09, max 0.97)","1024000.00 (min 1023997.00, max 1024002.00)","0.13 (min 0.12, max 0.14)"
    "44100","1411189.80 (min 1411188.00, max 1411192.00)","0.28 (min 0.27, max 0.30)","1411192.80 (min 1411189.00, max 1411197.00)","0.26 (min 0.23, max 0.30)","1411200.33 (min 1411196.00, max 1411203.00)","0.27"
    "48000","1535988.80 (min 1535986.00, max 1535991.00)","0.42 (min 0.10, max 1.23)","1535992.20 (min 1535988.00, max 1535997.00)","0.12 (min 0.10, max 0.19)","1536000.67 (min 1535996.00, max 1536003.00)","0.12 (min 0.11, max 0.12)"
    "88200","2822372.20 (min 2822363.00, max 2822378.00)","0.50 (min 0.45, max 0.56)","2822380.80 (min 2822374.00, max 2822389.00)","0.43 (min 0.40, max 0.46)","2822396.67 (min 2822387.00, max 2822403.00)","0.43 (min 0.41, max 0.45)"
    "96000","3071956.20 (min 3071939.00, max 3071969.00)","0.37 (min 0.16, max 1.00)","3071971.00 (min 3071963.00, max 3071983.00)","0.35 (min 0.14, max 0.99)","3071978.00 (min 3071960.00, max 3071992.00)","0.18 (min 0.15, max 0.21)"

.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","am62xx_lp_sk-fs: Throughput (bits/sec)","am62xx_lp_sk-fs: CPU Load (%)","am62xx_sk-fs: Throughput (bits/sec)","am62xx_sk-fs: CPU Load (%)","am62xxsip_sk-fs: Throughput (bits/sec)","am62xxsip_sk-fs: CPU Load (%)"

    "11025","352945.00 (min 352944.00, max 352946.00)","0.21 (min 0.15, max 0.29)","352946.60 (min 352945.00, max 352948.00)","0.19 (min 0.14, max 0.26)","352947.50 (min 352947.00, max 352948.00)","0.25 (min 0.21, max 0.28)"
    "16000","512211.67 (min 512210.00, max 512213.00)","0.16 (min 0.10, max 0.32)","512213.20 (min 512212.00, max 512214.00)","0.32 (min 0.12, max 0.90)","512215.00 (min 512214.00, max 512216.00)","0.17 (min 0.14, max 0.19)"
    "22050","705888.00 (min 705886.00, max 705890.00)","0.15 (min 0.13, max 0.17)","705890.20 (min 705888.00, max 705892.00)","0.13 (min 0.11, max 0.15)","705892.00 (min 705888.00, max 705896.00)","0.14 (min 0.13, max 0.14)"
    "24000","705881.00 (min 705832.00, max 705891.00)","0.16 (min 0.13, max 0.18)","705881.80 (min 705840.00, max 705893.00)","0.14 (min 0.13, max 0.16)","705895.00 (min 705894.00, max 705896.00)","0.14 (min 0.13, max 0.15)"
    "32000","1024422.50 (min 1024420.00, max 1024423.00)","0.12 (min 0.10, max 0.17)","1024425.20 (min 1024422.00, max 1024427.00)","0.12 (min 0.09, max 0.15)","1024429.50 (min 1024429.00, max 1024430.00)","0.12 (min 0.10, max 0.13)"
    "44100","1411782.00 (min 1411778.00, max 1411783.00)","0.21 (min 0.19, max 0.22)","1411786.00 (min 1411781.00, max 1411788.00)","0.18 (min 0.16, max 0.21)","1411791.50 (min 1411790.00, max 1411793.00)","0.21 (min 0.20, max 0.22)"
    "48000","1536632.80 (min 1536629.00, max 1536634.00)","0.13 (min 0.11, max 0.17)","1536637.75 (min 1536633.00, max 1536640.00)","0.11 (min 0.10, max 0.11)","1536644.50 (min 1536643.00, max 1536646.00)","0.63 (min 0.47, max 0.79)"
    "88200","2823553.20 (min 2823535.00, max 2823561.00)","0.32 (min 0.29, max 0.35)","2823566.75 (min 2823558.00, max 2823572.00)","0.29 (min 0.25, max 0.33)","2823576.50 (min 2823575.00, max 2823578.00)","0.31 (min 0.29, max 0.33)"
    "96000","3073248.50 (min 3073237.00, max 3073262.00)","0.29 (min 0.17, max 0.59)","3073254.67 (min 3073245.00, max 3073270.00)","0.17 (min 0.15, max 0.19)","3073253.00 (min 3073233.00, max 3073273.00)","0.39 (min 0.24, max 0.54)"

|

Graphics SGX/RGX
================

GFXBench
--------

Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_lp_sk-fs: Fps","am62xx_sk-fs: Score","am62xx_sk-fs: Fps"

    " GFXBench 3.x gl_manhattan_off","81.53 (min 81.16, max 82.23)","1.32 (min 1.31, max 1.33)"
    " GFXBench 3.x gl_trex_off","124.19 (min 122.95, max 124.90)","2.22 (min 2.20, max 2.23)"
    " GFXBench 5.x gl_5_high_off","11.08 (min 10.87, max 11.19)","0.17","11.79 (min 11.60, max 11.89)","0.18"

Glmark2
-------

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am62xx_lp_sk-fs: Score","am62xx_sk-fs: Score","am62xxsip_sk-fs: Score"

    "Glmark2-DRM","57.00 (min 51.00, max 69.00)","61.00","54.00"
    "Glmark2-Wayland","200.33 (min 199.00, max 203.00)","216.50 (min 216.00, max 217.00)","209.00"
    "Glmark2-Wayland 1920x1080","62.67 (min 62.00, max 63.00)","67.00"

|

Ethernet
========

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
---------------------------

- CPSW3g: AM62x

TCP Bidirectional Throughput
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1606.03 (min 1303.43, max 1816.77)","60.01 (min 39.33, max 71.84)","1540.48 (min 1283.30, max 1773.53)","52.49 (min 40.80, max 68.45)","1673.91 (min 1656.34, max 1691.48)","64.30 (min 62.64, max 65.95)"

TCP Bidirectional Throughput Interrupt Pacing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1641.49 (min 1549.80, max 1756.23)","51.62 (min 39.44, max 63.10)","1563.91 (min 1444.87, max 1707.72)","39.79 (min 33.68, max 47.59)","1731.44 (min 1694.58, max 1768.29)","50.23 (min 42.61, max 57.85)"

UDP Throughput
^^^^^^^^^^^^^^

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","46.06 (min 37.80, max 54.51)","90.00 (min 74.00, max 106.00)","39.08 (min 36.43, max 42.06)","","53.38 (min 42.81, max 62.88)","104.40 (min 84.00, max 123.00)","39.68 (min 36.73, max 42.59)","","44.24 (min 43.33, max 45.15)","86.50 (min 85.00, max 88.00)","37.12 (min 36.93, max 37.30)"
    "128","","85.61 (min 73.61, max 109.51)","83.67 (min 72.00, max 107.00)","38.00 (min 36.03, max 41.81)","","104.87 (min 82.30, max 121.26)","102.20 (min 80.00, max 118.00)","39.45 (min 36.24, max 41.89)","","90.28 (min 89.44, max 91.11)","88.00 (min 87.00, max 89.00)","37.38 (min 37.37, max 37.38)"
    "256","","179.15 (min 147.10, max 213.03)","87.50 (min 72.00, max 104.00)","38.96 (min 36.23, max 42.27)","","127.26 (min 53.04, max 239.91)","62.00 (min 26.00, max 117.00)","24.61 (min 8.86, max 41.07)","","174.19 (min 171.67, max 176.70)","85.00 (min 84.00, max 86.00)","36.85 (min 36.54, max 37.16)"
    "1024","","662.53 (min 586.81, max 812.44)","81.00 (min 72.00, max 99.00)","37.83 (min 35.95, max 40.50)","","395.91 (min 163.01, max 663.99)","48.40 (min 20.00, max 81.00)","20.92 (min 8.11, max 36.34)","","645.78 (min 634.74, max 656.81)","78.50 (min 77.00, max 80.00)","36.08 (min 35.77, max 36.38)"
    "1518","","700.49 (min 612.17, max 810.09)","57.75 (min 50.00, max 67.00)","36.31 (min 34.89, max 37.94)","","606.38 (min 537.43, max 675.32)","50.00 (min 44.00, max 56.00)","32.91 (min 30.89, max 34.93)","","699.12 (min 692.68, max 705.56)","57.50 (min 57.00, max 58.00)","35.18 (min 35.07, max 35.28)"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","1.82 (min 1.38, max 2.10)","3.75 (min 3.00, max 4.00)","2.15 (min 1.69, max 2.84)","","1.72 (min 1.43, max 2.10)","3.40 (min 3.00, max 4.00)","1.42 (min 0.53, max 2.65)","","2.18 (min 2.10, max 2.25)","4.00","1.24 (min 1.04, max 1.43)"
    "128","","4.07 (min 3.69, max 5.02)","4.25 (min 4.00, max 5.00)","2.53 (min 1.33, max 4.89)","","4.55 (min 4.10, max 5.22)","4.40 (min 4.00, max 5.00)","2.22 (min 0.81, max 4.32)","","4.86 (min 4.40, max 5.32)","4.50 (min 4.00, max 5.00)","1.28 (min 0.97, max 1.58)"
    "256","","9.73 (min 9.22, max 10.24)","5.00","3.26 (min 2.02, max 4.50)","","9.63 (min 9.01, max 10.24)","4.67 (min 4.00, max 5.00)","1.47 (min 1.21, max 1.89)","","10.04 (min 9.83, max 10.24)","5.00","1.66 (min 1.21, max 2.11)"
    "1024","","41.78","5.00","2.92 (min 2.18, max 4.20)","","41.78","5.00","1.58 (min 1.40, max 1.90)","","41.78","5.00","2.82"
    "1518","","61.23","5.00","3.88 (min 3.72, max 4.08)","","70.26 (min 60.06, max 89.50)","6.00 (min 5.00, max 8.00)","4.64 (min 4.27, max 5.26)"

.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","am62xx_lp_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_lp_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_lp_sk-fs: Packets Per Second (kPPS)","am62xx_lp_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_lp_sk-fs: Packet Loss %","am62xx_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xx_sk-fs: THROUGHPUT (Mbits/sec)","am62xx_sk-fs: Packets Per Second (kPPS)","am62xx_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xx_sk-fs: Packet Loss %","am62xxsip_sk-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","am62xxsip_sk-fs: THROUGHPUT (Mbits/sec)","am62xxsip_sk-fs: Packets Per Second (kPPS)","am62xxsip_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am62xxsip_sk-fs: Packet Loss %"

    "64","","69.11 (min 59.97, max 87.93)","135.00 (min 117.00, max 172.00)","36.72 (min 34.78, max 38.94)","26.42 (min 1.56, max 65.56)","","82.74 (min 67.76, max 97.96)","161.40 (min 132.00, max 191.00)","38.08 (min 34.78, max 42.57)","63.67 (min 43.77, max 74.38)","","69.59 (min 67.60, max 71.58)","136.00 (min 132.00, max 140.00)","34.70 (min 34.39, max 35.00)","74.32 (min 68.16, max 80.48)"
    "128","","141.22 (min 119.76, max 162.02)","137.75 (min 117.00, max 158.00)","38.88 (min 36.11, max 42.02)","52.69 (min 20.71, max 75.48)","","158.34 (min 132.52, max 176.61)","154.60 (min 129.00, max 172.00)","37.12 (min 35.20, max 39.85)","62.73 (min 53.38, max 72.34)","","138.96 (min 136.23, max 141.68)","135.50 (min 133.00, max 138.00)","35.06 (min 34.90, max 35.22)","76.84 (min 76.16, max 77.52)"
    "256","","258.83 (min 235.45, max 282.21)","126.50 (min 115.00, max 138.00)","37.83 (min 36.04, max 39.62)","11.20 (min 1.41, max 20.99)","","332.00 (min 263.81, max 384.23)","162.33 (min 129.00, max 188.00)","40.55 (min 35.77, max 46.01)","53.96 (min 50.78, max 58.00)","","255.67 (min 249.57, max 261.77)","125.00 (min 122.00, max 128.00)","35.55 (min 35.28, max 35.81)","57.33 (min 56.21, max 58.44)"
    "1024","","776.19 (min 642.99, max 892.17)","94.67 (min 78.00, max 109.00)","38.97 (min 36.84, max 41.48)","3.63 (min 1.35, max 5.01)","","929.77 (min 919.63, max 936.99)","113.25 (min 112.00, max 114.00)","39.72 (min 37.19, max 42.42)","0.70 (min 0.25, max 1.35)","","676.55","83.00","34.96","1.77"
    "1518","","875.44 (min 744.64, max 951.13)","74.33 (min 63.00, max 81.00)","40.26 (min 38.35, max 41.54)","0.78 (min 0.56, max 1.15)","","943.68 (min 942.65, max 945.04)","80.00","40.37 (min 39.53, max 40.82)","1.27 (min 0.89, max 1.50)"

|

OSPI
====

OSPI RAW
--------

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xx_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","151.67 (min 21.01, max 192.31)"

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xx_lp_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","30.49 (min 29.94, max 31.05)"

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am62xxsip_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","108.69"

|

EMMC
====

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

EMMC EXT4 FIO 1G
----------------

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","56.35 (min 44.40, max 75.60)","1.56 (min 1.16, max 2.04)","164.17 (min 111.00, max 175.00)","1.90 (min 1.59, max 2.12)"
    "4m","56.83 (min 44.50, max 80.10)","1.06 (min 0.71, max 1.42)","164.00 (min 110.00, max 175.00)","1.54 (min 1.18, max 1.84)"
    "4k","28.60 (min 5.36, max 52.00)","9.06 (min 1.93, max 15.76)","49.53 (min 36.40, max 56.10)","12.30 (min 9.51, max 14.25)"
    "256k","52.10 (min 35.10, max 67.00)","1.66 (min 1.12, max 2.17)","160.28 (min 91.70, max 174.00)","2.61 (min 1.70, max 2.93)"

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","55.60 (min 45.30, max 61.60)","1.78 (min 1.52, max 2.04)","174.75 (min 174.00, max 175.00)","2.37 (min 2.24, max 2.58)"
    "4m","55.50 (min 45.40, max 61.20)","1.29 (min 1.18, max 1.45)","174.75 (min 174.00, max 175.00)","1.92 (min 1.81, max 2.02)"
    "4k","39.94 (min 5.26, max 51.60)","14.36 (min 2.35, max 18.53)","51.20 (min 36.40, max 56.80)","14.69 (min 10.45, max 16.16)"
    "256k","53.20 (min 35.80, max 61.50)","2.10 (min 1.60, max 2.34)","174.00","3.19 (min 2.86, max 3.41)"

.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "1m","91.63 (min 91.30, max 92.00)","2.51 (min 2.23, max 2.67)","171.33 (min 170.00, max 173.00)","2.39 (min 2.14, max 2.57)"
    "4m","97.27 (min 96.90, max 97.70)","2.12 (min 1.89, max 2.31)","167.00 (min 158.00, max 172.00)","2.26 (min 1.93, max 2.48)"
    "4k","63.67 (min 63.20, max 64.00)","20.73 (min 19.98, max 21.12)","93.40 (min 92.90, max 94.10)","22.07 (min 21.76, max 22.27)"
    "256k","91.67 (min 91.00, max 92.50)","2.43 (min 2.08, max 2.63)","170.33 (min 170.00, max 171.00)","2.63 (min 2.35, max 2.79)"

EMMC EXT4
---------

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "102400","50.31 (min 41.84, max 56.05)","3.33 (min 2.60, max 4.79)","180.62 (min 180.33, max 181.00)","8.68 (min 7.83, max 9.52)"
    "262144","51.08 (min 42.48, max 56.58)","2.80 (min 2.15, max 4.33)","182.99 (min 182.78, max 183.18)","9.97 (min 8.41, max 10.96)"
    "524288","51.06 (min 41.99, max 56.65)","2.73 (min 2.06, max 4.58)","182.90 (min 182.74, max 183.04)","10.36 (min 8.77, max 11.74)"
    "1048576","50.98 (min 42.13, max 56.54)","2.65 (min 1.94, max 3.79)","182.93 (min 182.82, max 183.13)","9.78 (min 7.93, max 10.53)"
    "5242880","51.07 (min 42.13, max 56.54)","2.75 (min 2.01, max 4.09)","182.78 (min 182.36, max 183.06)","10.78 (min 8.77, max 11.40)"

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "102400","51.61 (min 43.30, max 56.17)","3.71 (min 2.43, max 5.02)","179.02 (min 172.26, max 180.85)","9.05 (min 8.23, max 9.57)"
    "262144","52.59 (min 43.98, max 57.20)","3.15 (min 1.80, max 4.78)","183.01 (min 182.93, max 183.06)","10.99 (min 9.65, max 12.33)"
    "524288","52.56 (min 43.72, max 57.24)","3.14 (min 2.01, max 4.45)","182.84 (min 182.51, max 183.01)","11.49 (min 10.04, max 13.54)"
    "1048576","52.58 (min 43.57, max 57.28)","3.06 (min 1.90, max 4.24)","182.79 (min 182.41, max 182.96)","11.33 (min 10.48, max 12.72)"
    "5242880","52.15 (min 43.78, max 55.83)","3.15 (min 2.01, max 4.62)","182.58 (min 181.98, max 182.86)","12.35 (min 10.87, max 13.16)"

.. csv-table:: EMMC EXT4
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "102400","95.17 (min 78.78, max 99.27)","10.85 (min 3.48, max 20.87)","162.54 (min 159.41, max 166.83)","23.53 (min 19.52, max 30.28)"
    "262144","74.93 (min 29.32, max 99.56)","5.48 (min 1.62, max 13.98)","174.98 (min 171.54, max 176.93)","22.29 (min 17.17, max 29.67)"
    "524288","75.89 (min 30.26, max 99.36)","7.44 (min 2.98, max 18.12)","178.63 (min 177.90, max 180.04)","22.39 (min 17.60, max 29.24)"
    "1048576","75.87 (min 33.26, max 97.92)","11.60 (min 1.61, max 23.10)","178.97 (min 178.01, max 180.14)","21.34 (min 18.70, max 24.68)"
    "5242880","73.34 (min 11.84, max 97.06)","13.62 (min 3.25, max 24.94)","179.63 (min 178.91, max 180.27)","22.32 (min 19.21, max 26.81)"

EMMC VFAT
---------

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xx_sk-fs: Write VFAT CPU Load (%)","am62xx_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xx_sk-fs: Read VFAT CPU Load (%)"

    "102400","52.56 (min 34.40, max 71.36)","6.92 (min 3.55, max 12.09)","162.41 (min 152.54, max 173.22)","11.50 (min 9.89, max 12.79)"
    "262144","55.10 (min 35.68, max 77.62)","7.45 (min 3.83, max 13.09)","163.45 (min 156.32, max 173.46)","13.60 (min 11.54, max 16.09)"
    "524288","54.75 (min 35.78, max 77.29)","7.34 (min 4.04, max 12.59)","165.21 (min 151.84, max 173.93)","13.71 (min 12.30, max 15.42)"
    "1048576","54.97 (min 35.68, max 78.17)","7.30 (min 3.98, max 12.78)","167.79 (min 155.51, max 173.76)","14.55 (min 13.36, max 15.83)"
    "5242880","54.86 (min 35.78, max 77.98)","7.34 (min 3.89, max 12.59)","165.91 (min 153.32, max 173.53)","14.65 (min 13.36, max 16.05)"

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write VFAT CPU Load (%)","am62xx_lp_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read VFAT CPU Load (%)"

    "102400","43.14 (min 31.28, max 48.03)","6.67 (min 4.77, max 9.79)","168.45 (min 168.10, max 168.97)","14.66 (min 13.88, max 15.38)"
    "262144","44.58 (min 32.66, max 49.74)","6.98 (min 4.81, max 10.22)","169.28 (min 167.93, max 170.55)","17.06 (min 16.26, max 17.55)"
    "524288","44.58 (min 32.73, max 49.63)","7.11 (min 4.99, max 12.17)","167.27 (min 166.39, max 168.76)","16.65 (min 15.73, max 17.67)"
    "1048576","44.59 (min 31.62, max 50.06)","6.88 (min 4.70, max 10.08)","166.64 (min 165.59, max 167.41)","15.93 (min 14.46, max 17.53)"
    "5242880","43.91 (min 31.57, max 50.45)","6.84 (min 4.60, max 10.32)","165.31 (min 164.67, max 166.08)","17.23 (min 16.21, max 17.79)"

.. csv-table:: EMMC VFAT
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write VFAT Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write VFAT CPU Load (%)","am62xxsip_sk-fs: Read VFAT Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read VFAT CPU Load (%)"

    "102400","83.18 (min 56.50, max 98.42)","12.41 (min 7.21, max 20.04)","174.58 (min 173.60, max 175.16)","10.94 (min 10.92, max 10.97)"
    "262144","76.86 (min 58.60, max 98.13)","7.57 (min 4.32, max 13.34)","175.43 (min 174.85, max 175.83)","12.22 (min 11.76, max 12.71)"
    "524288","71.89 (min 52.63, max 97.46)","6.91 (min 3.72, max 12.58)","175.03 (min 174.75, max 175.37)","12.41 (min 11.76, max 13.33)"
    "1048576","79.09 (min 59.19, max 96.71)","7.86 (min 3.77, max 12.68)","174.88 (min 174.20, max 175.33)","13.16 (min 11.76, max 15.48)"
    "5242880","78.00 (min 58.68, max 98.05)","8.31 (min 4.45, max 13.28)","174.56 (min 174.33, max 174.70)","13.21 (min 12.97, max 13.39)"

UBoot EMMC
----------


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","64931.38 (min 56205.83, max 98107.78)","169639.54 (min 168041.03, max 170666.67)"
    "4000000","65572.89 (min 58776.68, max 96376.47)","172398.70 (min 169343.67, max 173375.66)"

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","59176.51 (min 56399.31, max 61593.98)","170845.38 (min 170666.67, max 171560.21)"
    "4000000","60389.18 (min 58202.49, max 62178.37)","174297.87"

.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","97208.26 (min 93090.91, max 102721.00)","171861.19 (min 171560.21, max 172463.16)"
    "4000000","98611.89 (min 97234.42, max 99902.44)","175229.95"

MMCSD
=====

.. warning::

  **IMPORTANT**: The performance numbers can be severely affected if the media is
  mounted in sync mode. Hot plug scripts in the filesystem mount
  removable media in sync mode to ensure data integrity. For performance
  sensitive applications, umount the auto-mounted filesystem and
  re-mount in async mode.

MMC EXT4 FIO 1G
---------------

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Write EXT4 CPU Load (%)","am62xx_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.46 (min 41.90, max 43.50)","1.47 (min 1.10, max 1.67)","87.54 (min 87.30, max 88.10)","1.59 (min 1.47, max 1.75)"
    "4m","41.78 (min 40.20, max 43.20)","0.99 (min 0.81, max 1.13)","86.26 (min 82.50, max 87.30)","1.13 (min 1.04, max 1.24)"
    "4k","2.82 (min 2.78, max 2.87)","1.76 (min 1.63, max 1.88)","12.92 (min 12.80, max 13.00)","4.41 (min 4.30, max 4.51)"
    "256k","38.54 (min 37.40, max 40.00)","1.62 (min 1.20, max 1.79)","83.90 (min 83.50, max 84.60)","1.77 (min 1.66, max 1.90)"

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write EXT4 CPU Load (%)","am62xx_lp_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read EXT4 CPU Load (%)"

    "1m","43.30 (min 42.60, max 43.60)","1.68 (min 1.55, max 1.78)","87.23 (min 85.30, max 88.10)","1.73 (min 1.65, max 1.84)"
    "4m","41.55 (min 40.80, max 43.00)","1.10 (min 1.05, max 1.16)","84.75 (min 82.40, max 87.40)","1.31 (min 1.27, max 1.37)"
    "4k","2.85 (min 2.84, max 2.86)","1.97 (min 1.88, max 2.03)","13.03 (min 12.90, max 13.10)","4.71 (min 4.63, max 4.77)"
    "256k","38.03 (min 35.90, max 39.20)","1.76 (min 1.63, max 1.88)","84.18 (min 83.70, max 84.50)","2.03 (min 2.02, max 2.04)"

.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write EXT4 CPU Load (%)","am62xxsip_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read EXT4 CPU Load (%)"

    "1m","35.27 (min 19.60, max 43.90)","1.37 (min 1.08, max 1.62)","87.33 (min 87.20, max 87.50)","1.56 (min 1.53, max 1.60)"
    "4m","34.37 (min 19.10, max 42.90)","1.01 (min 0.73, max 1.16)","87.27 (min 87.20, max 87.40)","1.51 (min 1.38, max 1.75)"
    "4k","3.24 (min 2.79, max 4.10)","1.86 (min 1.57, max 2.38)","13.13 (min 12.90, max 13.60)","4.24 (min 4.10, max 4.48)"
    "256k","32.00 (min 18.90, max 39.70)","1.36 (min 1.21, max 1.47)","83.60 (min 83.20, max 83.90)","1.58 (min 1.40, max 1.80)"

MMC EXT4
--------

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xx_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Write Raw CPU Load (%)","am62xx_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_sk-fs: Read Raw CPU Load (%)"

    "102400","10.66 (min 10.15, max 10.97)","0.70 (min 0.54, max 0.99)","11.02 (min 10.66, max 11.11)","0.76 (min 0.64, max 0.86)"
    "262144","10.76 (min 10.52, max 11.00)","0.67 (min 0.45, max 1.02)","11.05 (min 10.81, max 11.20)","0.67 (min 0.62, max 0.74)"
    "524288","10.72 (min 10.27, max 11.02)","0.58 (min 0.41, max 0.85)","11.16 (min 10.91, max 11.50)","0.65 (min 0.56, max 0.78)"
    "1048576","10.80 (min 10.40, max 11.15)","0.64 (min 0.44, max 0.89)","11.34 (min 10.85, max 12.02)","0.64 (min 0.53, max 0.77)"
    "5242880","11.02 (min 10.68, max 11.26)","0.61 (min 0.44, max 0.98)","12.01 (min 11.98, max 12.03)","0.75 (min 0.60, max 0.86)"

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xx_lp_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Write Raw CPU Load (%)","am62xx_lp_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xx_lp_sk-fs: Read Raw CPU Load (%)"

    "102400","10.44 (min 10.00, max 10.84)","0.89 (min 0.73, max 1.16)","10.96 (min 10.64, max 11.81)","0.83 (min 0.66, max 0.99)"
    "262144","10.41 (min 9.72, max 10.96)","0.82 (min 0.60, max 1.44)","11.04 (min 10.91, max 11.19)","0.81 (min 0.42, max 1.02)"
    "524288","10.33 (min 9.37, max 10.79)","0.75 (min 0.60, max 0.97)","11.20 (min 10.99, max 11.50)","0.87 (min 0.75, max 0.97)"
    "1048576","10.60 (min 9.85, max 10.97)","0.79 (min 0.59, max 1.26)","11.44 (min 10.96, max 12.00)","0.89 (min 0.80, max 0.94)"
    "5242880","10.65 (min 10.25, max 11.15)","0.74 (min 0.59, max 1.04)","12.01 (min 11.99, max 12.02)","0.93 (min 0.86, max 0.98)"

.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am62xxsip_sk-fs: Write Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Write Raw CPU Load (%)","am62xxsip_sk-fs: Read Raw Throughput (Mbytes/sec)","am62xxsip_sk-fs: Read Raw CPU Load (%)"

    "102400","10.64 (min 9.97, max 10.88)","0.98 (min 0.54, max 1.67)","10.88 (min 10.86, max 10.91)","1.65 (min 1.56, max 1.74)"
    "262144","10.64 (min 10.39, max 10.86)","0.90 (min 0.59, max 1.70)","10.92 (min 10.81, max 11.00)","1.12 (min 0.93, max 1.23)"
    "524288","10.64 (min 10.41, max 10.90)","0.71 (min 0.46, max 1.37)","11.03 (min 10.94, max 11.08)","1.12 (min 0.93, max 1.27)"
    "1048576","11.01 (min 10.55, max 11.38)","1.11 (min 0.49, max 1.90)","11.99 (min 11.96, max 12.01)","1.17 (min 0.92, max 1.34)"
    "5242880","11.23 (min 10.86, max 11.33)","1.47 (min 0.51, max 2.99)","12.00 (min 11.99, max 12.02)","1.31 (min 1.00, max 1.57)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

UBoot MMCSD
-----------

UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_sk-fs: Write Throughput (Kbytes/sec)","am62xx_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","36246.41 (min 21787.23, max 40554.46)","82198.64 (min 81920.00, max 83591.84)"
    "800000","44588.63 (min 35310.34, max 56109.59)","86846.44 (min 86231.58, max 88086.02)"
    "1000000","48914.57 (min 44521.74, max 51684.54)","89369.63 (min 88562.16, max 90021.98)"


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xx_lp_sk-fs: Write Throughput (Kbytes/sec)","am62xx_lp_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","36781.47 (min 29049.65, max 40960.00)","81952.15 (min 78769.23, max 83591.84)"
    "800000","43935.80 (min 30228.78, max 50257.67)","86035.96 (min 79533.98, max 88086.02)"
    "1000000","47180.72 (min 42010.26, max 53368.08)","88994.57 (min 85333.33, max 90021.98)"

.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am62xxsip_sk-fs: Write Throughput (Kbytes/sec)","am62xxsip_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","27632.53 (min 16253.97, max 40554.46)","81427.02 (min 78769.23, max 83591.84)"
    "800000","37337.86 (min 20480.00, max 46022.47)","86543.74 (min 85333.33, max 87148.94)"
    "1000000","36834.85 (min 20152.52, max 47906.43)","89371.40 (min 88562.16, max 90021.98)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

|

USB
===

USB Device Controller
---------------------

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)","am62xxsip_sk-fs: Throughput (MB/sec)"

    "150","43.53 (min 43.30, max 43.70)","43.27 (min 42.70, max 43.60)","43.90 (min 43.80, max 44.00)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","am62xx_lp_sk-fs: Throughput (MB/sec)","am62xx_sk-fs: Throughput (MB/sec)","am62xxsip_sk-fs: Throughput (MB/sec)"

    "150","39.40 (min 39.10, max 39.80)","41.35 (min 40.90, max 41.90)","39.70 (min 38.70, max 40.70)"

|

CRYPTO
======

OpenSSL Performance
-------------------

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am62xx_lp_sk-fs: throughput (KBytes/Sec)","am62xx_sk-fs: throughput (KBytes/Sec)","am62xxsip_sk-fs: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","21742.25","24533.33","24039.08"
    "aes-128-cbc","16","378.80","385.16","383.05"
    "aes-128-cbc","16384","117959.34","120673.62","122934.61"
    "aes-128-cbc","256","6155.09","6233.26","6222.34"
    "aes-128-cbc","64","1538.09","1639.94","1591.89"
    "aes-128-cbc","8192","89830.74","94538.41","97886.21"
    "aes-128-ecb","1024","22719.15","24592.38","24507.05"
    "aes-128-ecb","16","383.20","386.55","386.23"
    "aes-128-ecb","16384","120640.85","125042.69","129351.68"
    "aes-128-ecb","256","6168.58","6537.22","6389.93"
    "aes-128-ecb","64","1545.64","1729.02","1667.37"
    "aes-128-ecb","8192","92547.75","98254.85","98358.61"
    "aes-192-cbc","1024","21413.89","24498.52","24373.93"
    "aes-192-cbc","16","381.31","384.91","385.23"
    "aes-192-cbc","16384","110351.70","115228.67","115769.34"
    "aes-192-cbc","256","6150.74","6228.48","6216.87"
    "aes-192-cbc","64","1540.44","1636.27","1615.96"
    "aes-192-cbc","8192","84582.40","90395.99","90745.51"
    "aes-192-ecb","1024","22448.47","24605.70","24558.59"
    "aes-192-ecb","16","380.79","386.39","386.22"
    "aes-192-ecb","16384","114098.18","118035.80","121055.91"
    "aes-192-ecb","256","6169.51","6392.92","6323.97"
    "aes-192-ecb","64","1546.37","1708.93","1698.71"
    "aes-192-ecb","8192","88380.76","92755.29","96624.64"
    "aes-256-cbc","1024","21324.46","24482.13","24067.75"
    "aes-256-cbc","16","381.35","385.14","384.90"
    "aes-256-cbc","16384","101111.13","106577.92","107533.65"
    "aes-256-cbc","256","6143.40","6218.84","6203.22"
    "aes-256-cbc","64","1539.43","1628.82","1567.98"
    "aes-256-cbc","8192","81002.50","84445.87","85393.41"
    "aes-256-ecb","1024","22270.63","24578.39","24514.56"
    "aes-256-ecb","16","382.64","386.23","386.61"
    "aes-256-ecb","16384","107457.19","110526.46","111771.65"
    "aes-256-ecb","256","6163.37","6369.54","6258.69"
    "aes-256-ecb","64","1543.34","1707.82","1700.89"
    "aes-256-ecb","8192","84467.71","88790.36","89587.71"
    "sha256","1024","24685.57","28421.80","28115.29"
    "sha256","16","387.77","478.60","478.12"
    "sha256","16384","237305.86","262215.00","261783.55"
    "sha256","256","6193.58","7474.60","7386.62"
    "sha256","64","1550.25","1890.03","1877.25"
    "sha256","8192","156396.20","173823.32","172504.41"
    "sha512","1024","22674.09","24628.57","24615.59"
    "sha512","16","386.84","468.11","462.11"
    "sha512","16384","97610.41","108729.69","108882.60"
    "sha512","256","6166.53","6850.47","6755.50"
    "sha512","64","1547.43","1872.62","1851.22"
    "sha512","8192","78539.43","89071.62","88926.89"


.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am62xx_lp_sk-fs: CPU Load","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: CPU Load"

    "aes-128-cbc","38.00","38.00","38.00"
    "aes-128-ecb","40.00","39.00","39.00"
    "aes-192-cbc","39.00","38.00","38.00"
    "aes-192-ecb","40.00","38.00","39.00"
    "aes-256-cbc","38.00","38.00","38.00"
    "aes-256-ecb","39.00","38.00","37.00"
    "sha256","95.00","95.00","94.00"
    "sha512","95.00","95.00","94.00"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

IPSec Software Performance
--------------------------

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","am62xx_sk-fs: Throughput (Mbps)","am62xx_sk-fs: Packets/Sec","am62xx_sk-fs: CPU Load","am62xxsip_sk-fs: Throughput (Mbps)","am62xxsip_sk-fs: Packets/Sec","am62xxsip_sk-fs: CPU Load"

    "aes128","77.65 (min 73.60, max 81.70)","6.50 (min 6.00, max 7.00)","51.08 (min 50.78, max 51.38)","80.50","7.00","51.43"
    "aes192","0.60","0.00","56.22"
    "aes256","130.00 (min 53.40, max 206.60)","11.00 (min 4.00, max 18.00)","39.11 (min 27.23, max 50.98)","88.60 (min 0.40, max 205.40)","7.67 (min 0.00, max 18.00)","43.07 (min 27.21, max 51.38)"

|
