
======================================
 Linux 10.01 Performance Guide
======================================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
| AM68 SK        | AM68 SK Evaluation Module  with ARM running at 2GHz, DDR data rate 2666 MT/S, L3 Cache size 3MB                |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM69 SK        | AM69 SK Evaluation Module  with ARM running at 2GHz, DDR data rate 2666 MT/S, L3 Cache size 3MB                |
+----------------+----------------------------------------------------------------------------------------------------------------+
| J721e EVM      | J721e Evaluation Module rev E2 with ARM running at 2GHz, DDR data rate 4266 MT/S, L3 Cache size 3MB            |
+----------------+----------------------------------------------------------------------------------------------------------------+
| J7200 EVM      | J7200 Evaluation Module rev E1 with ARM running at 2GHz, DDR data rate 2666 MT/S, L3 Cache size 3MB            |
+----------------+----------------------------------------------------------------------------------------------------------------+
| J721S2 EVM     | J721S2 Evaluation Module rev E2 with ARM running at 2GHz, DDR data rate 2666 MT/S, L3 Cache size 3MB           |
+----------------+----------------------------------------------------------------------------------------------------------------+
| J784S4 EVM     | J784S4 Evaluation Module Beta rev E1 with ARM running at 2GHz, DDR data rate 2666 MT/S, L3 Cache size 1MB      |
+----------------+----------------------------------------------------------------------------------------------------------------+
| J742S2 EVM     | J742S2 Evaluation Module with ARM running at 2GHz, DDR data rate 2666 MT/S, L3 Cache size 1MB                  |
+----------------+----------------------------------------------------------------------------------------------------------------+
| J722S EVM      | J722S Evaluation Module rev E1 with ARM running at 1.4GHz, DDR data rate 3200 MT/S                             |
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
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "af_unix_sock_stream_latency (microsec)","17.15","30.80","21.86","20.15","19.42","29.72","18.03","30.10"
    "af_unix_socket_stream_bandwidth (MBs)","2196.40","2405.12","1674.18","2059.63","1676.63","1115.52","3678.11","3563.63"
    "bw_file_rd-io-1mb (MB/s)","1818.51","3417.09","2487.56","2185.39","2126.15","1238.72","3572.07","3497.79"
    "bw_file_rd-o2c-1mb (MB/s)","1119.19","1476.29","1180.24","1139.60","1067.43","700.53","2213.61","1679.54"
    "bw_mem-bcopy-16mb (MB/s)","3822.72","2757.19","2371.42","2812.94","3384.45","1705.21","3767.81","2699.06"
    "bw_mem-bcopy-1mb (MB/s)","4830.92","10163.41","3381.99","4725.55","4752.85","1927.12","9730.97","9687.62"
    "bw_mem-bcopy-2mb (MB/s)","4049.33","3852.89","2420.05","3981.90","3205.13","1622.59","4954.88","3791.14"
    "bw_mem-bcopy-4mb (MB/s)","3879.10","3070.43","2326.93","3872.97","0.00","1544.20","4716.98","3070.43"
    "bw_mem-bcopy-8mb (MB/s)","3814.37","2874.08","2353.63","2902.23","3391.27","1779.56","3914.53","2801.12"
    "bw_mem-bzero-16mb (MB/s)","10960.78","10875.11","2337.47","9631.30","10479.78","6633.50","10583.76","10869.57"
    "bw_mem-bzero-1mb (MB/s)","8994.41 (min 4830.92, max 13157.89)","11958.29 (min 10163.41, max 13753.17)","4079.53 (min 3381.99, max 4777.07)","8670.44 (min 4725.55, max 12615.33)","8814.60 (min 4752.85, max 12876.35)","4273.64 (min 1927.12, max 6620.15)","11703.71 (min 9730.97, max 13676.44)","11715.42 (min 9687.62, max 13743.22)"
    "bw_mem-bzero-2mb (MB/s)","7920.45 (min 4049.33, max 11791.56)","8753.02 (min 3852.89, max 13653.14)","2665.10 (min 2420.05, max 2910.15)","8103.86 (min 3981.90, max 12225.82)","7211.85 (min 3205.13, max 11218.57)","4127.18 (min 1622.59, max 6631.76)","9181.56 (min 4954.88, max 13408.23)","8710.49 (min 3791.14, max 13629.84)"
    "bw_mem-bzero-4mb (MB/s)","7468.49 (min 3879.10, max 11057.87)","7676.84 (min 3070.43, max 12283.24)","2398.04 (min 2326.93, max 2469.14)","7908.87 (min 3872.97, max 11944.76)","5304.10 (min 0.00, max 10608.20)","4087.20 (min 1544.20, max 6630.20)","8291.14 (min 4716.98, max 11865.29)","7675.73 (min 3070.43, max 12281.02)"
    "bw_mem-bzero-8mb (MB/s)","7406.41 (min 3814.37, max 10998.45)","7132.01 (min 2874.08, max 11389.93)","2354.67 (min 2353.63, max 2355.71)","7290.53 (min 2902.23, max 11678.83)","6215.41 (min 3391.27, max 9039.55)","4205.43 (min 1779.56, max 6631.30)","7423.62 (min 3914.53, max 10932.70)","7035.36 (min 2801.12, max 11269.59)"
    "bw_mem-cp-16mb (MB/s)","2207.81","2130.78","984.37","1568.47","2128.51","899.84","2092.05","2174.21"
    "bw_mem-cp-1mb (MB/s)","7766.30 (min 2527.08, max 13005.52)","8508.60 (min 3288.87, max 13728.32)","3069.52 (min 1285.58, max 4853.46)","7160.22 (min 1732.77, max 12587.66)","7709.33 (min 2586.55, max 12832.10)","3890.74 (min 881.06, max 6900.41)","8855.85 (min 4020.47, max 13691.23)","8459.03 (min 3197.16, max 13720.89)"
    "bw_mem-cp-2mb (MB/s)","7030.38 (min 2233.21, max 11827.55)","8013.18 (min 2345.45, max 13680.90)","1976.77 (min 1008.57, max 2944.97)","6824.17 (min 1464.13, max 12184.20)","6653.40 (min 2144.01, max 11162.79)","3800.83 (min 864.06, max 6737.59)","7994.75 (min 2658.56, max 13330.93)","8002.36 (min 2377.31, max 13627.40)"
    "bw_mem-cp-4mb (MB/s)","6616.23 (min 2178.65, max 11053.80)","7312.04 (min 2334.18, max 12289.90)","1716.47 (min 958.08, max 2474.86)","6767.64 (min 1565.56, max 11969.72)","6358.90 (min 2096.44, max 10621.35)","3802.47 (min 919.33, max 6685.61)","7356.82 (min 2810.96, max 11902.68)","7334.27 (min 2383.08, max 12285.46)"
    "bw_mem-cp-8mb (MB/s)","6597.73 (min 2178.06, max 11017.39)","6743.08 (min 2172.73, max 11313.42)","1672.54 (min 984.49, max 2360.58)","6630.30 (min 1508.86, max 11751.74)","6182.07 (min 1871.35, max 10492.79)","3806.81 (min 944.73, max 6668.89)","6547.15 (min 2209.94, max 10884.35)","6744.20 (min 2210.86, max 11277.53)"
    "bw_mem-fcp-16mb (MB/s)","3785.64","2680.07","2401.68","2792.81","0.00","1663.55","3772.70","2650.76"
    "bw_mem-fcp-1mb (MB/s)","8666.06 (min 4174.23, max 13157.89)","10237.78 (min 6722.38, max 13753.17)","4058.13 (min 3339.19, max 4777.07)","8284.31 (min 3953.28, max 12615.33)","8514.04 (min 4151.73, max 12876.35)","4119.58 (min 1619.00, max 6620.15)","10127.08 (min 6577.71, max 13676.44)","10175.99 (min 6608.76, max 13743.22)"
    "bw_mem-fcp-2mb (MB/s)","7848.91 (min 3906.25, max 11791.56)","8503.17 (min 3353.20, max 13653.14)","2723.42 (min 2536.69, max 2910.15)","8121.68 (min 4017.53, max 12225.82)","6603.32 (min 1988.07, max 11218.57)","4091.80 (min 1551.83, max 6631.76)","8791.07 (min 4173.91, max 13408.23)","8551.70 (min 3473.56, max 13629.84)"
    "bw_mem-fcp-4mb (MB/s)","7451.64 (min 3845.41, max 11057.87)","7603.88 (min 2924.51, max 12283.24)","2443.40 (min 2417.65, max 2469.14)","7920.56 (min 3896.36, max 11944.76)","5304.10 (min 0.00, max 10608.20)","4095.13 (min 1560.06, max 6630.20)","8167.28 (min 4469.27, max 11865.29)","7596.91 (min 2912.80, max 12281.02)"
    "bw_mem-fcp-8mb (MB/s)","7396.76 (min 3795.07, max 10998.45)","7095.53 (min 2801.12, max 11389.93)","2385.04 (min 2355.71, max 2414.37)","7366.52 (min 3054.21, max 11678.83)","4519.78 (min 0.00, max 9039.55)","4130.98 (min 1630.66, max 6631.30)","7368.40 (min 3804.09, max 10932.70)","7002.09 (min 2734.58, max 11269.59)"
    "bw_mem-frd-16mb (MB/s)","4721.16","2988.98","6304.18","4790.42","4152.07","1836.97","4690.71","2928.26"
    "bw_mem-frd-1mb (MB/s)","4739.38 (min 4174.23, max 5304.52)","7260.36 (min 6722.38, max 7798.33)","4744.51 (min 3339.19, max 6149.83)","4748.37 (min 3953.28, max 5543.46)","4573.71 (min 4151.73, max 4995.69)","1759.35 (min 1619.00, max 1899.70)","7190.15 (min 6577.71, max 7802.58)","7130.44 (min 6608.76, max 7652.11)"
    "bw_mem-frd-2mb (MB/s)","4615.74 (min 3906.25, max 5325.22)","3530.17 (min 3353.20, max 3707.14)","4475.19 (min 2536.69, max 6413.68)","4905.22 (min 4017.53, max 5792.90)","3358.57 (min 1988.07, max 4729.06)","1616.11 (min 1551.83, max 1680.39)","4655.76 (min 4173.91, max 5137.61)","3687.14 (min 3473.56, max 3900.71)"
    "bw_mem-frd-4mb (MB/s)","4285.18 (min 3845.41, max 4724.94)","3025.25 (min 2924.51, max 3125.98)","4365.89 (min 2417.65, max 6314.13)","4767.35 (min 3896.36, max 5638.34)","2104.16 (min 0.00, max 4208.31)","1562.61 (min 1560.06, max 1565.15)","5010.49 (min 4469.27, max 5551.70)","3006.31 (min 2912.80, max 3099.81)"
    "bw_mem-frd-8mb (MB/s)","4257.77 (min 3795.07, max 4720.46)","2974.54 (min 2801.12, max 3147.95)","4362.26 (min 2414.37, max 6310.14)","4234.84 (min 3054.21, max 5415.47)","0.00","1736.46 (min 1630.66, max 1842.26)","4593.38 (min 3804.09, max 5382.67)","2926.34 (min 2734.58, max 3118.10)"
    "bw_mem-fwr-16mb (MB/s)","10947.66","10845.62","2343.29","9625.51","10483.21","6651.88","10601.29","10832.77"
    "bw_mem-fwr-1mb (MB/s)","9155.02 (min 5304.52, max 13005.52)","10763.33 (min 7798.33, max 13728.32)","5501.65 (min 4853.46, max 6149.83)","9065.56 (min 5543.46, max 12587.66)","8913.90 (min 4995.69, max 12832.10)","4400.06 (min 1899.70, max 6900.41)","10746.91 (min 7802.58, max 13691.23)","10686.50 (min 7652.11, max 13720.89)"
    "bw_mem-fwr-2mb (MB/s)","8576.39 (min 5325.22, max 11827.55)","8694.02 (min 3707.14, max 13680.90)","4679.33 (min 2944.97, max 6413.68)","8988.55 (min 5792.90, max 12184.20)","7945.93 (min 4729.06, max 11162.79)","4208.99 (min 1680.39, max 6737.59)","9234.27 (min 5137.61, max 13330.93)","8764.06 (min 3900.71, max 13627.40)"
    "bw_mem-fwr-4mb (MB/s)","7889.37 (min 4724.94, max 11053.80)","7707.94 (min 3125.98, max 12289.90)","4394.50 (min 2474.86, max 6314.13)","8804.03 (min 5638.34, max 11969.72)","7414.83 (min 4208.31, max 10621.35)","4125.38 (min 1565.15, max 6685.61)","8727.19 (min 5551.70, max 11902.68)","7692.64 (min 3099.81, max 12285.46)"
    "bw_mem-fwr-8mb (MB/s)","7868.93 (min 4720.46, max 11017.39)","7230.69 (min 3147.95, max 11313.42)","4335.36 (min 2360.58, max 6310.14)","8583.61 (min 5415.47, max 11751.74)","5246.40 (min 0.00, max 10492.79)","4255.58 (min 1842.26, max 6668.89)","8133.51 (min 5382.67, max 10884.35)","7197.82 (min 3118.10, max 11277.53)"
    "bw_mem-rd-16mb (MB/s)","5471.96","3542.96","6601.57","5106.93","4874.33","1889.91","5541.13","3673.09"
    "bw_mem-rd-1mb (MB/s)","9179.97 (min 8059.98, max 10299.96)","13129.50 (min 11157.34, max 15101.65)","7188.09 (min 3917.91, max 10458.26)","7968.57 (min 5527.82, max 10409.32)","7490.44 (min 5178.66, max 9802.21)","1976.40 (min 1795.69, max 2157.11)","15962.02 (min 14649.19, max 17274.84)","10779.21 (min 9780.91, max 11777.50)"
    "bw_mem-rd-2mb (MB/s)","4744.40 (min 3123.17, max 6365.63)","4799.73 (min 3804.45, max 5795.00)","4035.25 (min 977.04, max 7093.46)","3812.60 (min 1210.10, max 6415.09)","4393.68 (min 2974.53, max 5812.83)","1781.93 (min 1681.80, max 1882.06)","5810.24 (min 3754.91, max 7865.57)","4727.87 (min 3623.84, max 5831.90)"
    "bw_mem-rd-4mb (MB/s)","3994.83 (min 2411.82, max 5577.83)","3463.84 (min 3252.56, max 3675.12)","3731.87 (min 785.93, max 6677.80)","3740.87 (min 1223.05, max 6258.69)","3663.27 (min 2344.32, max 4982.21)","1796.98 (min 1710.13, max 1883.83)","4801.39 (min 2965.60, max 6637.17)","3721.52 (min 3512.47, max 3930.56)"
    "bw_mem-rd-8mb (MB/s)","3871.19 (min 2268.54, max 5473.83)","3521.76 (min 3312.17, max 3731.34)","3665.81 (min 752.66, max 6578.95)","3933.78 (min 1984.13, max 5883.43)","3507.48 (min 2150.25, max 4864.70)","1840.40 (min 1789.31, max 1891.48)","4895.78 (min 3272.65, max 6518.90)","3593.97 (min 3226.24, max 3961.70)"
    "bw_mem-rdwr-16mb (MB/s)","2235.57","2399.88","751.24","1888.13","2125.68","1828.78","2233.70","2396.29"
    "bw_mem-rdwr-1mb (MB/s)","4586.70 (min 2527.08, max 6646.31)","6426.10 (min 3288.87, max 9563.33)","3347.38 (min 1285.58, max 5409.18)","2429.70 (min 1732.77, max 3126.63)","4603.32 (min 2586.55, max 6620.08)","1327.37 (min 881.06, max 1773.68)","6817.93 (min 4020.47, max 9615.38)","6349.41 (min 3197.16, max 9501.65)"
    "bw_mem-rdwr-2mb (MB/s)","2699.83 (min 2233.21, max 3166.44)","3185.81 (min 2345.45, max 4026.17)","997.71 (min 986.84, max 1008.57)","1477.78 (min 1464.13, max 1491.42)","2473.41 (min 2144.01, max 2802.80)","1151.07 (min 864.06, max 1438.07)","3099.19 (min 2658.56, max 3539.82)","3015.81 (min 2377.31, max 3654.30)"
    "bw_mem-rdwr-4mb (MB/s)","2274.86 (min 2178.65, max 2371.07)","2600.27 (min 2334.18, max 2866.36)","876.50 (min 794.91, max 958.08)","1933.97 (min 1565.56, max 2302.38)","2133.41 (min 2096.44, max 2170.37)","1290.46 (min 919.33, max 1661.59)","2842.78 (min 2810.96, max 2874.60)","2595.30 (min 2383.08, max 2807.51)"
    "bw_mem-rdwr-8mb (MB/s)","2226.37 (min 2178.06, max 2274.67)","2469.49 (min 2172.73, max 2766.25)","870.28 (min 756.07, max 984.49)","1880.72 (min 1508.86, max 2252.57)","2018.22 (min 1871.35, max 2165.09)","1351.01 (min 944.73, max 1757.28)","2544.34 (min 2209.94, max 2878.73)","2473.66 (min 2210.86, max 2736.45)"
    "bw_mem-wr-16mb (MB/s)","2266.61","2734.58","743.05","1794.93","2197.50","1802.21","2200.52","2764.34"
    "bw_mem-wr-1mb (MB/s)","7353.15 (min 6646.31, max 8059.98)","10360.34 (min 9563.33, max 11157.34)","4663.55 (min 3917.91, max 5409.18)","4327.23 (min 3126.63, max 5527.82)","5899.37 (min 5178.66, max 6620.08)","1784.69 (min 1773.68, max 1795.69)","13445.11 (min 9615.38, max 17274.84)","9641.28 (min 9501.65, max 9780.91)"
    "bw_mem-wr-2mb (MB/s)","3144.81 (min 3123.17, max 3166.44)","3915.31 (min 3804.45, max 4026.17)","981.94 (min 977.04, max 986.84)","1350.76 (min 1210.10, max 1491.42)","2888.67 (min 2802.80, max 2974.53)","1559.94 (min 1438.07, max 1681.80)","3647.37 (min 3539.82, max 3754.91)","3639.07 (min 3623.84, max 3654.30)"
    "bw_mem-wr-4mb (MB/s)","2391.45 (min 2371.07, max 2411.82)","3059.46 (min 2866.36, max 3252.56)","790.42 (min 785.93, max 794.91)","1762.72 (min 1223.05, max 2302.38)","2257.35 (min 2170.37, max 2344.32)","1685.86 (min 1661.59, max 1710.13)","2920.10 (min 2874.60, max 2965.60)","3159.99 (min 2807.51, max 3512.47)"
    "bw_mem-wr-8mb (MB/s)","2271.61 (min 2268.54, max 2274.67)","3039.21 (min 2766.25, max 3312.17)","754.37 (min 752.66, max 756.07)","2118.35 (min 1984.13, max 2252.57)","2157.67 (min 2150.25, max 2165.09)","1773.30 (min 1757.28, max 1789.31)","3075.69 (min 2878.73, max 3272.65)","2981.35 (min 2736.45, max 3226.24)"
    "bw_mmap_rd-mo-1mb (MB/s)","6810.04","12660.55","8690.83","7236.96","6025.20","2085.51","10332.25","12916.14"
    "bw_mmap_rd-o2c-1mb (MB/s)","1323.25","1257.70","1407.71","1291.27","1165.95","661.49","2006.93","1748.56"
    "bw_pipe (MB/s)","955.39","894.72","733.36","906.22","1025.23","754.72","956.31","886.41"
    "bw_unix (MB/s)","2196.40","2405.12","1674.18","2059.63","1676.63","1115.52","3678.11","3563.63"
    "lat_connect (us)","37.52","37.53","37.36","36.66","38.04","64.17","37.49","37.37"
    "lat_ctx-2-128k (us)","3.93","3.91","3.75","3.92","3.86","6.41","4.04","6.87"
    "lat_ctx-2-256k (us)","3.20","2.95","3.21","3.21","3.26","7.49","3.20","3.03"
    "lat_ctx-4-128k (us)","3.79","4.83","3.69","3.69","3.90","6.54","3.66","4.53"
    "lat_ctx-4-256k (us)","2.62","2.02","2.61","2.63","1.58","5.59","2.31","4.60"
    "lat_fs-0k (num_files)","410.00","367.00","424.00","430.00","413.00","200.00","447.00","381.00"
    "lat_fs-10k (num_files)","142.00","180.00","158.00","153.00","150.00","97.00","178.00","179.00"
    "lat_fs-1k (num_files)","249.00","270.00","211.00","232.00","238.00","156.00","255.00","252.00"
    "lat_fs-4k (num_files)","243.00","274.00","224.00","259.00","240.00","134.00","261.00","258.00"
    "lat_mem_rd-stride128-sz1000k (ns)","11.42","5.83","9.69","11.50","13.07","31.82","5.79","5.84"
    "lat_mem_rd-stride128-sz125k (ns)","5.57","5.65","5.57","5.57","5.57","6.20","5.65","5.65"
    "lat_mem_rd-stride128-sz250k (ns)","5.57","5.65","5.57","5.57","5.57","6.54","5.65","5.65"
    "lat_mem_rd-stride128-sz31k (ns)","3.34","3.85","4.66","4.67","5.14","4.09","3.85","4.74"
    "lat_mem_rd-stride128-sz50 (ns)","2.00","2.00","2.00","2.00","2.00","2.40","2.00","2.00"
    "lat_mem_rd-stride128-sz500k (ns)","5.57","5.65","5.57","5.57","5.57","10.82","5.65","5.65"
    "lat_mem_rd-stride128-sz62k (ns)","5.57","5.20","5.12","5.57","4.67","5.84","5.19","5.65"
    "lat_mmap-1m (us)","29.00","29.00","39.00","35.00","29.00","57.00","34.00","29.00"
    "lat_ops-double-add (ns)","1.96","1.96","1.96","1.96","1.96","3.21","1.96","1.96"
    "lat_ops-double-div (ns)","9.01","9.01","9.01","9.01","9.01","17.62","9.00","9.01"
    "lat_ops-double-mul (ns)","2.00","2.00","2.00","2.00","2.00","3.21","2.00","2.00"
    "lat_ops-float-add (ns)","1.96","1.96","1.96","1.96","1.96","3.21","1.96","1.96"
    "lat_ops-float-div (ns)","5.51","5.51","5.50","5.51","5.51","10.41","5.50","5.51"
    "lat_ops-float-mul (ns)","2.00","2.00","2.00","2.00","2.00","3.20","2.00","2.00"
    "lat_ops-int-add (ns)","0.50","0.50","0.50","0.50","0.50","0.80","0.50","0.50"
    "lat_ops-int-bit (ns)","0.33","0.33","0.33","0.33","0.33","0.53","0.33","0.33"
    "lat_ops-int-div (ns)","4.00","4.00","4.00","4.01","4.00","4.81","4.00","4.00"
    "lat_ops-int-mod (ns)","4.67","4.67","4.67","4.67","4.67","5.08","4.67","4.67"
    "lat_ops-int-mul (ns)","1.52","1.52","1.52","1.52","1.52","3.44","1.52","1.52"
    "lat_ops-int64-add (ns)","0.50","0.50","0.50","0.50","0.50","0.80","0.50","0.50"
    "lat_ops-int64-bit (ns)","0.33","0.33","0.33","0.33","0.33","0.53","0.33","0.33"
    "lat_ops-int64-div (ns)","3.01","3.00","3.00","3.00","3.00","7.61","3.00","3.00"
    "lat_ops-int64-mod (ns)","5.67","5.67","5.67","5.67","5.67","5.88","5.67","5.67"
    "lat_ops-int64-mul (ns)","2.52","2.52","2.52","2.52","2.52","3.98","2.52","2.52"
    "lat_pagefault (us)","0.66","0.65","0.66","0.64","0.70","1.55","0.62","0.63"
    "lat_pipe (us)","13.89","19.57","13.92","13.82","13.91","25.98","14.38","19.23"
    "lat_proc-exec (us)","499.80","479.92","493.64","440.08","617.67","916.00","391.69","484.64"
    "lat_proc-fork (us)","387.57","416.25","392.93","354.73","392.57","726.25","332.59","356.43"
    "lat_proc-proccall (us)","0.00","0.00","0.00","0.00","0.00","0.01","0.00","0.00"
    "lat_select (us)","14.71","13.60","11.90","13.64","13.61","39.28","13.64","11.93"
    "lat_sem (us)","1.47","2.56","1.67","1.30","1.52","2.96","1.33","1.21"
    "lat_sig-catch (us)","3.59","3.54","3.58","3.47","3.57","6.67","3.58","3.62"
    "lat_sig-install (us)","0.54","0.53","0.53","0.53","0.53","0.72","0.54","0.54"
    "lat_sig-prot (us)","0.16","0.16","0.19","0.19","0.13","0.69","0.20","0.20"
    "lat_syscall-fstat (us)","0.90","0.87","0.90","0.92","0.91","2.09","0.87","0.91"
    "lat_syscall-null (us)","0.37","0.37","0.39","0.39","0.39","0.51","0.39","0.37"
    "lat_syscall-open (us)","140.05","111.22","137.18","140.70","125.48","152.66","153.84","230.68"
    "lat_syscall-read (us)","0.51","0.52","0.52","0.54","0.54","0.93","0.51","0.50"
    "lat_syscall-stat (us)","2.12","2.16","2.17","2.10","2.09","5.21","2.11","2.15"
    "lat_syscall-write (us)","0.47","0.46","0.46","0.48","0.49","0.84","0.47","0.46"
    "lat_tcp (us)","0.77","0.75","0.77","0.76","0.76","1.05","0.77","0.77"
    "lat_unix (us)","17.15","30.80","21.86","20.15","19.42","29.72","18.03","30.10"
    "latency_for_0.50_mb_block_size (nanosec)","5.57","5.65","5.57","5.57","5.57","10.82","5.65","5.65"
    "latency_for_1.00_mb_block_size (nanosec)","5.71 (min 0.00, max 11.42)","2.91 (min 0.00, max 5.83)","4.84 (min 0.00, max 9.69)","5.75 (min 0.00, max 11.50)","6.54 (min 0.00, max 13.07)","15.91 (min 0.00, max 31.82)","2.90 (min 0.00, max 5.79)","2.92 (min 0.00, max 5.84)"
    "pipe_bandwidth (MBs)","955.39","894.72","733.36","906.22","1025.23","754.72","956.31","886.41"
    "pipe_latency (microsec)","13.89","19.57","13.92","13.82","13.91","25.98","14.38","19.23"
    "procedure_call (microsec)","0.00","0.00","0.00","0.00","0.00","0.01","0.00","0.00"
    "select_on_200_tcp_fds (microsec)","14.71","13.60","11.90","13.64","13.61","39.28","13.64","11.93"
    "semaphore_latency (microsec)","1.47","2.56","1.67","1.30","1.52","2.96","1.33","1.21"
    "signal_handler_latency (microsec)","0.54","0.53","0.53","0.53","0.53","0.72","0.54","0.54"
    "signal_handler_overhead (microsec)","3.59","3.54","3.58","3.47","3.57","6.67","3.58","3.62"
    "tcp_ip_connection_cost_to_localhost (microsec)","37.52","37.53","37.36","36.66","38.04","64.17","37.49","37.37"
    "tcp_latency_using_localhost (microsec)","0.77","0.75","0.77","0.76","0.76","1.05","0.77","0.77"




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
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cpu_clock (MHz)","2000.00","2000.00","2000.00","2000.00","2000.00","1250.00","2000.00","2000.00"
    "dhrystone_per_mhz (DMIPS/MHz)","5.70","4.70","5.70","5.70","5.70","2.80","5.70","5.70"
    "dhrystone_per_second (DhrystoneP)","20000000.00","16666667.00","20000000.00","20000000.00","20000000.00","6250000.00","20000000.00","20000000.00"




Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "whetstone (MIPS)","10000.00","10000.00","10000.00","10000.00","10000.00","5000.00","10000.00","10000.00"




Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "linpack (Kflops)","2641026.00","2522656.00","2621865.00","2446266.00","2422106.00","515787.00","2596094.00","2560279.00"




NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "assignment (Iterations)","31.87","31.71","31.63","31.96","31.93","12.95","31.87","31.87"
    "fourier (Iterations)","60657.00","60051.00","60037.00","58877.00","65122.00","20386.00","64289.00","60049.00"
    "fp_emulation (Iterations)","388.00","387.97","388.00","388.01","381.06","192.55","387.97","387.94"
    "huffman (Iterations)","2487.70","2489.90","2494.90","2487.10","2476.30","1057.10","2497.20","2485.90"
    "idea (Iterations)","7996.60","7996.00","7996.90","7996.80","7899.40","3068.60","7996.80","7996.50"
    "lu_decomposition (Iterations)","1372.80","1353.30","1379.10","1369.70","1355.80","473.23","1352.30","1364.50"
    "neural_net (Iterations)","28.74","27.81","27.88","28.55","28.77","7.73","28.76","28.88"
    "numeric_sort (Iterations)","877.94","874.31","881.78","873.82","868.95","556.10","879.53","861.11"
    "string_sort (Iterations)","361.75","353.78","361.53","353.53","360.39","146.36","360.37","353.59"




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
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "add (MB/s)","6435.70","5755.80","5462.20","5279.50","6260.60","2304.60","6249.70","5797.80"
    "copy (MB/s)","6984.10","5709.80","4784.50","5522.20","6948.70","3431.00","6878.50","5853.30"
    "scale (MB/s)","7125.70","5669.70","4841.30","5414.20","7075.20","3019.40","7022.20","5806.40"
    "triad (MB/s)","6450.60","5754.30","5467.20","5264.20","6249.00","2107.00","6246.40","5795.60"




CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","80.65","82.64","82.64","82.64","82.64","37.59","82.64","81.97"
    "core (workloads/)","0.78","0.78","0.77","0.78","0.77","0.27","0.78","0.78"
    "coremark-pro ()","2507.36","2518.79","2489.11","2521.24","2454.68","840.47","2528.93","2485.62"
    "linear_alg-mid-100x100-sp (workloads/)","81.70","80.26","82.37","79.37","80.52","13.11","81.70","78.99"
    "loops-all-mid-10k-sp (workloads/)","2.47","2.47","2.46","2.46","2.46","0.64","2.47","2.46"
    "nnet_test (workloads/)","3.65","3.62","3.65","3.88","3.64","0.97","3.74","3.62"
    "parser-125k (workloads/)","10.99","10.87","10.87","11.24","10.99","7.81","10.99","10.87"
    "radix2-big-64k (workloads/)","288.18","304.04","268.60","280.98","263.30","64.65","296.47","277.55"
    "sha-test (workloads/)","158.73","158.73","158.73","158.73","158.73","72.46","158.73","158.73"
    "zip-test (workloads/)","47.62","47.62","47.62","47.62","43.48","19.61","47.62","47.62"



 
 


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

.. csv-table:: Multibench Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "4m-check (workloads/)","848.61","978.09","874.43","870.78","825.08","384.97","1117.07","987.75"
    "4m-check-reassembly (workloads/)","152.21","184.50","120.48","144.93","146.84","113.38","185.53","183.15"
    "4m-check-reassembly-tcp (workloads/)","96.90","108.23","92.59","98.43","94.70","54.95","112.11","106.84"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","42.58","37.76","41.12","45.01","40.43","29.94","56.02","39.06"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","2.68","4.84","2.66","2.69","2.69","1.74","4.79","4.86"
    "4m-cmykw2 (workloads/)","314.47","602.41","313.48","315.46","312.99","212.77","600.60","602.41"
    "4m-cmykw2-rotatew2 (workloads/)","59.94","47.02","60.00","63.49","60.24","44.74","72.29","48.15"
    "4m-reassembly (workloads/)","127.39","135.32","105.60","124.38","118.34","75.24","136.61","130.55"
    "4m-rotatew2 (workloads/)","70.18","49.60","69.88","73.53","70.22","48.69","78.06","48.29"
    "4m-tcp-mixed (workloads/)","262.30","246.15","275.86","275.86","262.30","108.84","271.19","250.00"
    "4m-x264w2 (workloads/)","2.75","5.09","2.72","2.78","2.76","1.78","4.95","5.07"
    "empty-wld (workloads/)","","","","","","1.00","",""
    "idct-4m (workloads/)","34.82","35.12","34.92","34.86","34.72","17.21","35.10","35.10"
    "idct-4mw1 (workloads/)","34.98","35.06","34.94","35.03","34.90","17.23","35.05","35.12"
    "ippktcheck-4m (workloads/)","830.01","991.67","870.47","871.69","836.96","383.02","1156.87","975.42"
    "ippktcheck-4mw1 (workloads/)","823.72","998.40","886.53","876.58","826.99","382.85","1131.22","1000.40"
    "ipres-4m (workloads/)","167.04","187.27","156.74","180.29","165.20","104.24","198.15","176.26"
    "ipres-4mw1 (workloads/)","169.30","183.37","157.07","176.26","165.93","104.24","196.34","177.31"
    "md5-4m (workloads/)","45.72","46.64","46.00","49.07","45.58","25.91","49.55","46.88"
    "md5-4mw1 (workloads/)","45.45","46.64","45.70","48.90","45.72","25.92","50.08","46.58"
    "rgbcmyk-4m (workloads/)","163.00","163.80","163.13","163.67","162.87","56.13","164.07","163.53"
    "rgbcmyk-4mw1 (workloads/)","163.00","163.53","163.40","163.67","162.73","56.15","163.93","163.80"
    "rotate-4ms1 (workloads/)","51.71","53.65","51.18","54.05","51.23","21.20","54.29","53.48"
    "rotate-4ms1w1 (workloads/)","50.81","53.65","51.39","54.05","51.18","21.21","54.29","53.76"
    "rotate-4ms64 (workloads/)","52.80","54.95","52.74","55.37","52.08","21.38","55.49","55.01"
    "rotate-4ms64w1 (workloads/)","52.52","55.01","52.58","55.19","52.91","21.40","55.56","54.88"
    "x264-4mq (workloads/)","1.42","1.42","1.42","1.43","1.43","0.52","1.41","1.44"
    "x264-4mqw1 (workloads/)","1.42","1.42","1.43","1.43","1.42","0.52","1.44","1.42"



 
 


Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am68_sk-fs: Boot time in seconds: avg(min,max)","am69_sk-fs: Boot time in seconds: avg(min,max)","j7200-evm: Boot time in seconds: avg(min,max)","j721e-idk-gw: Boot time in seconds: avg(min,max)","j721s2-evm: Boot time in seconds: avg(min,max)","j722s_evm-fs: Boot time in seconds: avg(min,max)","j742s2_evm-fs: Boot time in seconds: avg(min,max)","j784s4-evm: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","19.56 (min 19.19, max 19.94)","21.53 (min 21.02, max 22.14)","19.46 (min 19.18, max 20.42)","22.48 (min 21.90, max 23.51)","21.62 (min 21.42, max 22.27)","22.10 (min 21.65, max 22.97)","22.06 (min 21.00, max 37.39)","22.84 (min 22.36, max 24.33)"

 

 

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.
 



|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","j721e-idk-gw: Throughput (bits/sec)","j721e-idk-gw: CPU Load (%)","j721s2-evm: Throughput (bits/sec)","j721s2-evm: CPU Load (%)","j722s_evm-fs: Throughput (bits/sec)","j722s_evm-fs: CPU Load (%)"

    "8000","","","","","255988.00","0.35"
    "11025","352792.00","0.31","1023966.00","0.37","331808.00","0.35"
    "16000","511992.00","0.42","1023981.00","0.48","511976.00","0.41"
    "22050","705574.00","0.39","1023951.00","0.40","663630.00","0.47"
    "24000","705582.00","0.40","1023974.00","0.37","663610.00","0.44"
    "32000","1023979.00","0.28","1023976.00","0.43","1023924.00","0.56"
    "44100","1411173.00","0.60","","","1327223.00","0.64"
    "48000","1535972.00","0.79","","","1535905.00","0.80"
    "88200","2822348.00","1.05","","","2654466.00","1.01"
    "96000","3071938.00","0.52","","","3071822.00","1.10"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","j721e-idk-gw: Throughput (bits/sec)","j721e-idk-gw: CPU Load (%)"

    "11025","352937.00","0.15"
    "16000","512202.00","0.24"
    "22050","705865.00","0.27"
    "24000","705873.00","0.26"
    "32000","1024401.00","0.38"
    "44100","1411755.00","0.45"
    "48000","1536605.00","0.29"
    "88200","2823511.00","0.89"
    "96000","3073209.00","1.17"

 
 



 



|

Graphics SGX/RGX Driver
-------------------------
 


GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am68_sk-fs: Score","am68_sk-fs: Fps","am69_sk-fs: Score","am69_sk-fs: Fps","j721e-idk-gw: Score","j721e-idk-gw: Fps","j721s2-evm: Score","j721s2-evm: Fps","j742s2_evm-fs: Score","j742s2_evm-fs: Fps","j784s4-evm: Score","j784s4-evm: Fps"

    " GFXBench 3.x gl_manhattan_off","942.25","15.20","903.81","14.58","1228.17","19.81","950.12","15.32","941.93","15.19","917.29","14.80"
    " GFXBench 3.x gl_trex_off","1596.99","28.52","1465.23","26.16","1830.73","32.69","1599.63","28.56","1587.47","28.35","1516.07","27.07"
    " GFXBench 4.x gl_4_off","261.27","4.42","251.79","4.26","411.76","6.97","260.86","4.41","261.79","4.43","254.75","4.31"
    " GFXBench 5.x gl_5_high_off","113.83","1.77","109.82","1.71","179.78","2.80","113.82","1.77","113.50","1.77","110.98","1.73"




Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am68_sk-fs: Score","am69_sk-fs: Score","j721e-idk-gw: Score","j721s2-evm: Score","j722s_evm-fs: Score","j742s2_evm-fs: Score","j784s4-evm: Score"

    "Glmark2-DRM","523.00","167.00","48.00","112.00","286.00","142.00","160.00"
    "Glmark2-Wayland","1242.00","1323.00","1141.00","1082.00","708.00","1358.00","1354.00"
    "Glmark2-Wayland 4000x4000","77.00","82.00","72.00","82.00","83.00"

 
 

 

 



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
    :header: "Command Used","am68_sk-fs: THROUGHPUT (Mbits/sec)","am68_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","j7200-evm: THROUGHPUT (Mbits/sec)","j7200-evm: CPU Load % (LOCAL_CPU_UTIL)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j721s2-evm: THROUGHPUT (Mbits/sec)","j721s2-evm: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1850.79","78.97","1882.68","87.01","1878.23","81.60","1702.53","89.53","1849.38","65.91","1849.94","60.09","1816.81","28.75"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1869.49","43.22","1875.66","48.29","1871.06","20.18","1783.48","11.66"




.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: Packets Per Second (kPPS)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","26.65","185.00","81.41","18.00","14.31","99.00","39.29","18.00","22.93","159.00","43.40","18.00","25.26","175.00","20.94"
    "128","82.00","119.43","182.00","81.41","82.00","64.65","99.00","39.39","82.00","106.64","163.00","44.26","82.00","114.21","174.00","20.93"
    "256","210.00","304.53","181.00","82.50","210.00","164.83","98.00","39.05","210.00","262.75","156.00","43.65","210.00","267.12","159.00","22.03"
    "1024","978.00","956.61","122.00","56.74","978.00","726.25","93.00","38.43","978.00","901.73","115.00","30.32","978.00","935.29","120.00","15.89"
    "1518","1472.00","956.97","81.00","45.79","1472.00","957.00","81.00","38.96","1472.00","954.92","81.00","24.09","1472.00","954.30","81.00","10.89"




.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","3.28","23.00","9.32","18.00","1.04","7.00","0.76"
    "128","82.00","11.15","17.00","8.94","82.00","5.25","8.00","0.81","82.00","6.36","10.00","0.49"
    "256","210.00","18.98","11.00","5.32","210.00","13.78","8.00","0.49"
    "1024","978.00","66.50","8.00","3.47","978.00","303.33","39.00","14.02","978.00","72.76","9.00","1.20"
    "1518","1472.00","751.14","64.00","51.25","1472.00","937.24","80.00","30.28"




.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j721e-idk-gw: Packet Loss %","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: Packet Loss %","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: Packet Loss %"

    "64","18.00","51.37","357.00","84.72","10.08","18.00","66.59","462.00","44.00","45.13"
    "128","82.00","235.77","359.00","88.49","9.89","82.00","266.63","406.00","43.58","45.63","82.00","205.32","313.00","22.54","34.36"
    "256","210.00","588.37","350.00","89.85","11.86","210.00","600.31","357.00","22.45","14.26"
    "1024","978.00","905.44","116.00","82.40","1.02","978.00","930.76","119.00","40.25","0.09","978.00","871.00","111.00","19.28","0.03"
    "1518","1472.00","949.39","81.00","67.26","0.01","1472.00","937.24","80.00","30.28","0.00"

 
 

 

 
 



|

PCIe Driver
-------------------------

PCIe-ETH
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: PCIe Ethernet performance
    :header: "TCP Window Size(Kbytes)","am68-sk: Bandwidth (Mbits/sec)","am69-sk: Bandwidth (Mbits/sec)","j721e-idk-gw: Bandwidth (Mbits/sec)","j7200-evm: Bandwidth (Mbits/sec)","j721s2-evm: Bandwidth (Mbits/sec)","j784s4-evm: Bandwidth (Mbits/sec)","j722s-evm: Bandwidth (Mbits/sec)"

    "8","183","187","184","184","185","187","178"
    "16","437","440","438","439","439","440","414"
    "32","585","589","589","589","584","589","550"
    "64","929","937","935","935","928","937","914"
    "128","938","939","938","938","938","939","937"
    "256","938","940","939","939","938","940","938"

PCIe-NVMe-SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^
 

 


J721E-IDK-GW
"""""""""""""""""""""""""""




.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","753.00","14.30","745.00","3.92"
    "4m","756.00","13.27","1512.00","6.78"
    "4k","185.00","48.65","163.00","36.14"
    "256k","755.00","15.59","1508.00","14.30"



- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based 
- Platform: Speed 8GT/s, Width x2
- SSD being used: PLEXTOR PX-128M8PeY
 


J7200-EVM
"""""""""""""""""""""""""""




.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","j7200-evm: Write EXT4 Throughput (Mbytes/sec)","j7200-evm: Write EXT4 CPU Load (%)","j7200-evm: Read EXT4 Throughput (Mbytes/sec)","j7200-evm: Read EXT4 CPU Load (%)"

    "1m","813.00","18.13","1525.00","8.65"
    "4m","815.00","16.45","1524.00","6.78"
    "4k","186.00","48.71","164.00","35.91"
    "256k","815.00","16.88","1520.00","14.50"



- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based 
- Platform: Speed 8GT/s, Width x2
- SSD being used: PLEXTOR PX-128M8PeY
 


J721S2-EVM
"""""""""""""""""""""""""""




.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","743.00","19.04","780.00","6.68"
    "4m","743.00","17.05","781.00","6.42"
    "4k","186.00","52.26","281.00","52.57"
    "256k","743.00","17.84","779.00","9.95"



- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based 
- Platform: Speed 8GT/s, Width x2
- SSD being used: PLEXTOR PX-128M8PeY
 

 

 
 
 

 



|

Linux OSPI Flash Driver
-------------------------

 

 

 

 

 


J721E-IDK-GW
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j721e-idk-gw: Write UBIFS Throughput (Mbytes/sec)","j721e-idk-gw: Write UBIFS CPU Load (%)","j721e-idk-gw: Read UBIFS Throughput (Mbytes/sec)","j721e-idk-gw: Read UBIFS CPU Load (%)"

    "102400","0.61 (min 0.48, max 1.10)","24.40 (min 22.88, max 25.98)","31.51","0.00"
    "262144","0.47 (min 0.35, max 0.52)","23.72 (min 23.23, max 24.36)","31.32","14.29"
    "524288","0.46 (min 0.35, max 0.52)","24.45 (min 23.24, max 25.65)","31.00","20.00"
    "1048576","0.46 (min 0.35, max 0.52)","23.98 (min 21.86, max 25.26)","31.08","20.00"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j721e-idk-gw: Raw Read Throughput (Mbytes/sec)"

    "50","38.76"

 
 


J722S-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j722s_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Write UBIFS CPU Load (%)","j722s_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.12, max 0.28)","14.11 (min 13.24, max 14.71)","27.60","12.50"
    "262144","0.14 (min 0.11, max 0.18)","13.76 (min 12.85, max 14.83)","27.70","9.68"
    "524288","0.14 (min 0.10, max 0.17)","14.00 (min 12.72, max 14.83)","27.62","9.68"
    "1048576","0.14 (min 0.11, max 0.18)","14.23 (min 12.94, max 14.70)","27.19","6.45"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j722s_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","37.59"

 
 

 


 


J7200-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j7200-evm: Write UBIFS Throughput (Mbytes/sec)","j7200-evm: Write UBIFS CPU Load (%)","j7200-evm: Read UBIFS Throughput (Mbytes/sec)","j7200-evm: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.27)","25.81 (min 25.33, max 26.21)","79.00","25.00"
    "262144","0.13 (min 0.10, max 0.17)","26.09 (min 25.49, max 26.67)","78.47","20.00"
    "524288","0.13 (min 0.10, max 0.17)","25.94 (min 24.52, max 27.22)","76.87","42.86"
    "1048576","0.13 (min 0.10, max 0.17)","26.33 (min 26.05, max 26.76)","75.30","33.33"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j7200-evm: Raw Read Throughput (Mbytes/sec)"

    "50","238.09"

 
 

 


J784S4-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j784s4-evm: Write UBIFS Throughput (Mbytes/sec)","j784s4-evm: Write UBIFS CPU Load (%)","j784s4-evm: Read UBIFS Throughput (Mbytes/sec)","j784s4-evm: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.27)","6.12 (min 5.89, max 6.65)","78.38","9.09"
    "262144","0.13 (min 0.10, max 0.17)","6.10 (min 5.46, max 6.69)","73.45","4.35"
    "524288","0.14 (min 0.10, max 0.18)","6.31 (min 5.71, max 7.09)","71.84","8.70"
    "1048576","0.14 (min 0.10, max 0.19)","6.31 (min 6.17, max 6.52)","71.04","8.33"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j784s4-evm: Raw Read Throughput (Mbytes/sec)"

    "50","238.09"

 
 


 

 

 
 

 



|

UBoot QSPI/OSPI Driver
-------------------------

 










J721E-IDK-GW
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","1047.57","15814.67"
    "800000","1048.64","16062.75"
    "1000000","1048.64","16173.74"
    "2000000","1049.75","16221.78"









J721S2-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "400000","1000.73","15875.97"
    "800000","1001.59","16062.75"
    "1000000","1001.96","16173.74"
    "2000000","1002.48","16221.78"




J784S4-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","990.09","15814.67"
    "800000","991.17","16062.75"
    "1000000","991.71","16173.74"
    "2000000","991.74","16213.76"






AM68-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","am68_sk-fs: Write Throughput (Kbytes/sec)","am68_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","380.49","227555.56"
    "800000","381.25","282482.76"
    "1000000","381.64","334367.35"
    "2000000","380.26","360087.91"

















 
 

 

 



|

UBoot UFS Driver
-------------------------


J721E-IDK-GW
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","102400.00","341333.33"
    "800000","99902.44","512000.00"
    "1000000","102400.00","606814.81"








J784S4-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","102400.00","372363.64"
    "800000","99902.44","512000.00"
    "1000000","104356.69","630153.85"

 

 
 



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
    :header: "Buffer size (bytes)","j7200-evm: Write EXT4 Throughput (Mbytes/sec)","j7200-evm: Write EXT4 CPU Load (%)","j7200-evm: Read EXT4 Throughput (Mbytes/sec)","j7200-evm: Read EXT4 CPU Load (%)"

    "1m","60.50","1.58","314.00","1.87"
    "4m","60.60","1.43","314.00","1.41"
    "4k","53.40","21.00","56.00","19.07"
    "256k","60.50","1.89","316.00","3.49"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","60.50","1.45","175.00","1.19"
    "4m","60.60","1.24","175.00","0.89"
    "4k","50.80","19.88","56.40","18.81"
    "256k","60.40","1.71","174.00","2.14"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

    "1m","95.60","1.77","293.00","3.21"
    "4m","95.90","1.38","291.00","2.71"
    "4k","83.80","25.91","94.60","23.60"
    "256k","95.60","2.18","292.00","4.45"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","45.40","3.43","300.00","3.71"
    "4m","45.50","3.10","300.00","3.65"
    "4k","5.29","5.09","36.20","15.90"
    "256k","36.50","3.65","283.00","5.68"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

    "1m","95.00","0.46","292.00","0.54"
    "4m","95.60","0.50","164.00","0.20"
    "4k","83.30","10.94","92.80","9.33"
    "256k","95.00","0.48","292.00","1.02"

 

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Write EXT4 CPU Load (%)","am69_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Read EXT4 CPU Load (%)"

    "1m","89.40","0.46","288.00","0.67"
    "4m","95.90","0.50","284.00","0.40"
    "4k","77.30","9.79","89.80","8.71"
    "256k","89.90","0.51","288.00","0.82"

 

 

 

 

 

 

 
 


EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "1m","58.80","1.73","314.00","2.11"
    "4m","59.20","1.52","311.00","1.58"
    "4k","61.60","12.64","58.80","18.91"
    "256k","58.60","1.83","313.00","3.59"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "1m","59.80","1.65","175.00","1.39"
    "4m","59.70","1.21","175.00","0.94"
    "4k","54.40","16.19","54.30","14.13"
    "256k","59.70","1.85","174.00","2.38"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "1m","95.80","1.81","293.00","3.47"
    "4m","96.10","1.32","294.00","2.54"
    "4k","75.60","11.39","67.50","11.49"
    "256k","95.80","2.20","293.00","4.64"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "1m","61.10","1.95","314.00","2.06"
    "4m","61.10","1.45","314.00","1.64"
    "4k","62.70","12.85","59.50","15.62"
    "256k","61.10","2.04","313.00","3.94"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "1m","85.80","0.43","294.00","0.48"
    "4m","95.70","0.47","294.00","0.28"
    "4k","90.30","5.16","89.60","4.65"
    "256k","86.20","0.56","293.00","0.84"

 

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write Raw Throughput (Mbytes/sec)","am69_sk-fs: Write Raw CPU Load (%)","am69_sk-fs: Read Raw Throughput (Mbytes/sec)","am69_sk-fs: Read Raw CPU Load (%)"

    "1m","88.60","0.44","292.00","0.49"
    "4m","95.90","0.47","181.00","0.21"
    "4k","83.80","5.49","88.90","4.86"
    "256k","89.50","0.55","292.00","0.89"

 

 

 

 

 

 

 
 

 

 

 

 

 
 


UBoot EMMC Driver
-----------------

 

 

 

 

 

 

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

    "2000000","60346.22","312076.19"
    "4000000","61134.33","306242.99"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "2000000","60346.22","173375.66"
    "4000000","61191.41","177604.34"

 

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "2000000","60124.77","309132.08"
    "4000000","61191.41","322837.44"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "2000000","96376.47","277694.92"
    "4000000","97234.42","292571.43"

 

 


 

 

 

 

 

 

 
 

 


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

    "4m","21.60","2.33","85.20","2.93"
 

 

 

 

 

 

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write EXT4 Throughput (Mbytes/sec)","j7200-evm: Write EXT4 CPU Load (%)","j7200-evm: Read EXT4 Throughput (Mbytes/sec)","j7200-evm: Read EXT4 CPU Load (%)"

    "1m","20.80","0.74","87.40","0.95"
    "4m","20.50","0.78","84.40","0.89"
    "4k","4.67","3.15","13.60","6.46"
    "256k","20.60","0.95","83.80","1.34"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","21.90","3.15","87.10","2.99"
    "4k","4.83","5.20","13.50","8.78"
    "256k","21.60","3.17","83.30","3.01"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

    "1m","18.00","0.16","87.80","0.22"
    "4m","18.00","0.16","84.20","0.16"
    "4k","3.92","0.78","13.60","1.66"
    "256k","17.70","0.16","84.20","0.44"

 

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","32.70","1.01","42.30","0.60"
    "4m","33.00","0.90","42.30","0.52"
    "4k","2.79","1.88","11.30","4.87"
    "256k","31.90","1.17","41.90","0.79"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

    "1m","42.20","1.26","88.20","1.53"
    "4m","41.00","0.95","81.00","1.28"
    "4k","2.82","1.99","13.60","5.15"
    "256k","38.10","1.40","84.40","1.85"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am68_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am68_sk-fs: Write EXT4 CPU Load (%)","am68_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am68_sk-fs: Read EXT4 CPU Load (%)"

    "1m","17.70","0.95","83.40","0.97"
    "4m","17.50","0.76","83.60","0.87"
    "4k","3.83","2.96","13.10","6.68"
    "256k","16.80","0.90","78.90","1.43"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Write EXT4 CPU Load (%)","am69_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Read EXT4 CPU Load (%)"

    "1m","18.30","0.16","81.70","0.22"
    "4m","18.30","0.17","82.40","0.19"
    "4k","4.46","0.89","15.50","2.37"
    "256k","17.40","0.17","81.20","0.41"

 

 

 

 

 

 

 

 

 
 


MMC RAW FIO 1G
^^^^^^^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "1m","21.10","0.77","88.00","1.00"
    "4m","21.20","0.78","88.00","0.73"
    "4k","5.71","3.12","17.40","7.10"
    "256k","21.20","0.87","85.90","1.40"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "1m","20.90","3.06","87.20","2.84"
    "4m","20.70","2.96","87.00","2.92"
    "4k","5.96","5.83","17.80","9.83"
    "256k","21.20","2.87","85.30","3.61"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "1m","43.10","0.33","87.90","0.23"
    "4m","43.00","0.34","87.60","0.22"
    "4k","3.80","0.66","16.60","2.24"
    "256k","39.90","0.40","86.20","0.36"

 

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "1m","35.80","1.17","43.90","0.63"
    "4m","34.40","0.92","43.90","0.52"
    "4k","3.69","1.88","14.10","5.50"
    "256k","34.70","1.29","43.40","0.72"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "1m","45.10","1.24","88.30","1.55"
    "4m","45.20","1.02","88.30","1.16"
    "4k","3.84","1.92","16.70","5.76"
    "256k","43.00","1.53","86.30","1.77"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am68_sk-fs: Write Raw Throughput (Mbytes/sec)","am68_sk-fs: Write Raw CPU Load (%)","am68_sk-fs: Read Raw Throughput (Mbytes/sec)","am68_sk-fs: Read Raw CPU Load (%)"

    "1m","42.70","1.48","88.10","1.07"
    "4m","42.70","1.18","88.10","0.89"
    "4k","3.80","2.45","17.60","7.51"
    "256k","39.30","1.59","86.20","1.25"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write Raw Throughput (Mbytes/sec)","am69_sk-fs: Write Raw CPU Load (%)","am69_sk-fs: Read Raw Throughput (Mbytes/sec)","am69_sk-fs: Read Raw CPU Load (%)"

    "1m","19.40","0.15","88.00","0.28"
    "4m","19.10","0.17","87.90","0.15"
    "4k","5.42","0.79","16.80","2.28"
    "256k","19.50","0.13","85.90","0.48"

 

 

 
 


MMC EXT4
^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "102400","35.06 (min 33.45, max 38.70)","3.16 (min 2.72, max 4.54)","71.48","4.28"
    "262144","35.47 (min 33.92, max 37.29)","3.23 (min 2.59, max 4.71)","83.62","5.99"
    "524288","37.12 (min 36.62, max 37.70)","3.22 (min 2.88, max 4.31)","88.60","6.32"
    "1048576","37.73 (min 37.37, max 38.50)","3.26 (min 2.86, max 4.41)","90.60","5.43"
    "5242880","37.45 (min 36.70, max 38.04)","3.18 (min 2.67, max 4.70)","91.29","6.30"

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 


MMC EXT2
^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "102400","36.62 (min 34.74, max 37.79)","2.93 (min 2.46, max 4.23)","80.45","5.38"
    "262144","36.38 (min 35.14, max 37.67)","2.96 (min 2.36, max 4.28)","82.61","6.13"
    "524288","36.48 (min 34.92, max 37.33)","2.86 (min 2.32, max 4.25)","87.96","7.08"
    "1048576","36.42 (min 34.38, max 37.40)","2.99 (min 2.58, max 4.19)","89.96","5.59"
    "5242880","36.20 (min 35.00, max 37.50)","2.88 (min 2.34, max 4.40)","89.76","4.97"

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 



UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","28845.07","34133.33"
    "800000","33573.77","39384.62"
    "1000000","36088.11","43002.62"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

    "400000","46545.45","67147.54"
    "800000","73142.86","78769.23"
    "1000000","74472.73","85333.33"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "400000","37236.36","57690.14"
    "800000","49349.40","72495.58"
    "1000000","47352.60","81512.44"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","17579.40","46545.45"
    "800000","19692.31","62060.61"
    "1000000","16416.83","74472.73"

 

 

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am69_sk-fs: Write Throughput (Kbytes/sec)","am69_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","16189.72","47080.46"
    "800000","25761.01","63015.38"
    "1000000","43343.92","74812.79"

 

 

 

 

 

 

 

 

 
 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 



|

USB Driver
-------------------------
 


USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^










.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

    "150","22.60","30.10","44.90","44.30"




.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

    "150","26.90","28.60","39.80","39.90"





 
 
 



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am68_sk-fs: throughput (KBytes/Sec)","am69_sk-fs: throughput (KBytes/Sec)","j7200-evm: throughput (KBytes/Sec)","j721e-idk-gw: throughput (KBytes/Sec)","j721s2-evm: throughput (KBytes/Sec)","j722s_evm-fs: throughput (KBytes/Sec)","j742s2_evm-fs: throughput (KBytes/Sec)","j784s4-evm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","43735.38","34965.50","39232.85","45149.18","43742.21","23503.87","43034.28","41938.60"
    "aes-128-cbc","16","838.20","640.61","756.67","877.07","826.37","422.11","838.92","816.91"
    "aes-128-cbc","16384","184254.46","180458.84","187629.57","191561.73","182261.08","85224.11","182206.46","180966.74"
    "aes-128-cbc","256","13080.75","11235.75","11723.69","13565.70","12931.84","7185.15","12973.65","12560.21"
    "aes-128-cbc","64","3351.96","2554.33","3020.69","3477.40","3300.95","1848.19","3335.17","2756.48"
    "aes-128-cbc","8192","149763.41","144340.31","149367.47","156999.68","149684.22","71669.08","147761.83","147693.57"
    "aes-128-ecb","1024","43724.80","43631.62","39518.21","45972.48","43747.67","24460.29","43640.83","34652.16"
    "aes-128-ecb","16","853.96","737.29","761.68","865.14","844.53","437.37","845.13","815.01"
    "aes-128-ecb","16384","186679.30","184915.29","189267.97","198568.62","185821.87","87889.24","183309.65","178339.84"
    "aes-128-ecb","256","13103.62","13131.26","11901.44","13498.11","13106.60","7340.46","12921.94","11091.46"
    "aes-128-ecb","64","3384.73","3292.16","3050.88","3461.53","3342.74","1898.11","3352.55","2927.51"
    "aes-128-ecb","8192","151890.60","149910.87","149605.03","161508.01","152434.01","72518.31","149932.71","133240.15"
    "aes-192-cbc","1024","43713.19","34692.44","38708.22","45339.31","43379.03","23218.52","43597.82","42202.11"
    "aes-192-cbc","16","853.25","641.55","755.29","872.79","836.55","425.63","840.69","809.67"
    "aes-192-cbc","16384","174052.69","159257.94","184702.29","179950.93","175030.27","77245.10","174915.58","173632.17"
    "aes-192-cbc","256","13065.73","12784.21","11640.15","13562.28","12973.91","7113.73","12995.41","13079.04"
    "aes-192-cbc","64","3375.79","3196.74","3000.26","3501.29","3296.58","1846.68","3357.93","3107.69"
    "aes-192-cbc","8192","143381.85","126763.01","146699.61","150634.50","144911.02","65937.41","143510.19","141451.26"
    "aes-192-ecb","1024","43736.06","42400.09","39177.90","45080.58","43631.62","23909.03","43327.83","42341.72"
    "aes-192-ecb","16","851.83","635.71","759.76","873.54","848.19","432.67","843.48","634.56"
    "aes-192-ecb","16384","181556.57","177160.19","186116.78","184532.99","181534.72","79140.18","180518.91","175603.71"
    "aes-192-ecb","256","13131.09","12822.70","11838.12","13501.70","12975.27","7246.34","12973.65","12645.03"
    "aes-192-ecb","64","3433.79","2886.66","3035.20","3483.69","3344.83","1892.52","3347.95","2771.56"
    "aes-192-ecb","8192","148245.16","145137.66","148329.81","152513.19","147434.15","67938.99","147439.62","144864.60"
    "aes-256-cbc","1024","43373.91","38302.38","38924.97","44249.77","43233.62","22771.71","42738.69","42175.83"
    "aes-256-cbc","16","850.86","624.42","761.20","871.35","848.50","424.04","837.69","631.95"
    "aes-256-cbc","16384","164151.30","159612.93","176057.00","167002.11","163130.03","70429.35","162736.81","159662.08"
    "aes-256-cbc","256","13076.39","9783.21","11749.46","13569.02","13091.58","7002.28","12957.35","12922.79"
    "aes-256-cbc","64","3376.94","2492.97","3029.80","3476.93","3347.52","1846.85","3331.39","2997.16"
    "aes-256-cbc","8192","135132.50","133098.15","139963.05","140454.57","136667.14","61401.77","135735.98","132057.77"
    "aes-256-ecb","1024","43667.46","41742.68","39168.00","44711.25","43575.64","23380.31","42492.59","39909.38"
    "aes-256-ecb","16","850.02","626.10","763.32","864.48","850.25","433.85","836.57","634.99"
    "aes-256-ecb","16384","167810.39","164839.42","181278.04","171048.96","166319.45","72362.67","166991.19","155331.24"
    "aes-256-ecb","256","13103.62","12711.59","11820.54","13387.43","13097.30","7220.31","12905.98","12813.48"
    "aes-256-ecb","64","3380.16","3152.28","3056.23","3466.33","3400.49","1889.60","3358.46","3077.99"
    "aes-256-ecb","8192","139042.82","136811.86","144676.18","145498.11","139638.10","62870.87","139859.29","123092.99"
    "des3","1024","37889.37","31665.15","37546.33","38537.22","37535.06","","37524.14","30822.06"
    "des3","16","853.03","632.63","763.62","868.57","837.13","","838.04","623.82"
    "des3","16384","95709.87","91957.93","119308.29","96518.14","95655.25","","95797.25","91237.03"
    "des3","256","12496.38","9781.93","11351.13","12770.22","12215.98","","12368.55","9534.81"
    "des3","64","3386.79","2904.36","3044.80","3472.55","3354.01","","3345.45","2754.58"
    "des3","8192","86155.26","80300.71","102741.33","87621.63","86406.49","","86332.76","80322.56"
    "sha1","1024","52450.99","51176.11","52658.86","52432.55","52511.40","","53829.29","52264.96"
    "sha1","16","877.53","857.85","881.66","901.49","893.25","","897.03","863.24"
    "sha1","16384","445054.98","434296.15","445338.97","452618.92","445125.97","","446889.98","440636.76"
    "sha1","256","13742.51","13175.89","13847.13","14110.55","13982.89","","14086.31","13541.80"
    "sha1","64","3493.78","3401.56","3496.26","3576.23","3521.09","","3567.38","3440.90"
    "sha1","8192","299180.03","289647.27","296973.65","302312.11","299646.98","","299821.74","290635.78"
    "sha256","1024","52444.50","52465.66","51980.97","51972.78","53603.33","29473.45","54313.64","51661.14"
    "sha256","16","875.91","864.88","868.90","894.86","899.37","487.32","909.57","862.33"
    "sha256","16384","441892.86","438894.59","441581.57","442706.60","446371.16","241090.56","444519.77","432062.46"
    "sha256","256","13668.61","13590.87","13614.93","14018.47","14033.75","7510.19","14047.57","13345.96"
    "sha256","64","3469.27","3456.17","3478.14","3535.17","3544.49","1917.08","3578.45","3412.33"
    "sha256","8192","295600.13","291241.98","295026.69","295652.01","299565.06","161947.65","299518.63","290146.99"
    "sha512","1024","42425.69","41490.09","41954.65","43078.66","43663.36","21218.30","42553.69","41966.25"
    "sha512","16","876.59","857.95","863.40","892.59","895.37","475.95","878.37","861.62"
    "sha512","16384","145074.86","144113.66","144687.10","144992.94","146806.10","60243.97","144801.79","145675.61"
    "sha512","256","13051.99","12503.72","12793.09","12983.81","13112.15","6918.91","13099.35","12632.83"
    "sha512","64","3505.11","3415.51","3458.01","3556.50","3584.79","1901.65","3514.22","3451.33"
    "sha512","8192","124444.67","123595.43","124515.67","125419.52","126427.14","53654.87","125195.61","125116.42"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am68_sk-fs: CPU Load","am69_sk-fs: CPU Load","j7200-evm: CPU Load","j721e-idk-gw: CPU Load","j721s2-evm: CPU Load","j722s_evm-fs: CPU Load","j742s2_evm-fs: CPU Load","j784s4-evm: CPU Load"

    "aes-128-cbc","33.00","33.00","34.00","35.00","34.00","35.00","34.00","34.00"
    "aes-128-ecb","34.00","35.00","34.00","36.00","35.00","35.00","35.00","34.00"
    "aes-192-cbc","33.00","35.00","34.00","35.00","34.00","35.00","34.00","33.00"
    "aes-192-ecb","33.00","34.00","34.00","36.00","35.00","35.00","34.00","34.00"
    "aes-256-cbc","33.00","32.00","33.00","35.00","33.00","34.00","34.00","33.00"
    "aes-256-ecb","33.00","34.00","34.00","35.00","34.00","35.00","34.00","34.00"
    "des3","30.00","31.00","31.00","32.00","30.00","","30.00","31.00"
    "sha1","98.00","99.00","98.00","98.00","98.00","","98.00","99.00"
    "sha256","98.00","99.00","98.00","98.00","98.00","98.00","97.00","99.00"
    "sha512","98.00","99.00","98.00","98.00","98.00","98.00","98.00","99.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

 
