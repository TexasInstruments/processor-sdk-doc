
======================================
 Linux 11.02 Performance Guide
======================================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
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
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "af_unix_sock_stream_latency (microsec)","19.98 (min 19.51, max 20.42)","20.26 (min 19.39, max 21.11)","20.13 (min 19.48, max 21.07)","30.29 (min 29.18, max 31.07)","20.20 (min 19.79, max 20.60)","22.99 (min 19.76, max 28.54)"
    "af_unix_socket_stream_bandwidth (mb\s)","1607.04 (min 1549.65, max 1692.82)","1936.06 (min 1893.35, max 1967.65)","1991.06 (min 1869.53, max 2088.48)","1075.13 (min 1053.08, max 1122.04)","2887.72 (min 2676.18, max 3095.23)","2387.82 (min 1610.12, max 3148.32)"
    "bw_file_rd-io-1mb (mb/s)","3602.36 (min 3434.46, max 3685.28)","3564.31 (min 3469.81, max 3625.82)","2955.57 (min 0.00, max 3527.66)","1346.40 (min 1313.63, max 1397.87)","4042.79 (min 3909.03, max 4163.65)","4099.75 (min 3905.52, max 4408.66)"
    "bw_file_rd-o2c-1mb (mb/s)","1356.15 (min 1192.91, max 1618.71)","1729.35 (min 1376.33, max 1843.47)","1431.21 (min 1359.22, max 1538.46)","743.06 (min 714.03, max 794.91)","2003.37 (min 1729.83, max 2330.17)","1867.61 (min 1622.79, max 2168.81)"
    "bw_mem-bcopy-16mb (mb/s)","2314.36 (min 2238.70, max 2369.32)","2811.34 (min 2802.59, max 2818.39)","3494.28 (min 3385.89, max 3787.88)","1760.23 (min 1706.85, max 1876.17)","3103.56 (min 2535.26, max 3676.89)","2900.58 (min 2610.97, max 3428.33)"
    "bw_mem-bcopy-1mb (mb/s)","3262.21 (min 3153.99, max 3390.44)","4868.49 (min 4520.80, max 5214.89)","4556.63 (min 4245.11, max 4804.14)","1905.41 (min 1835.24, max 2010.45)","9740.12 (min 8886.57, max 10054.14)","9728.29 (min 9303.21, max 10055.02)"
    "bw_mem-bcopy-2mb (mb/s)","2400.80 (min 2365.00, max 2478.75)","3915.70 (min 3861.00, max 3942.65)","3663.49 (min 3533.57, max 3985.65)","1633.60 (min 1592.99, max 1698.08)","4437.53 (min 3905.56, max 5075.22)","4263.84 (min 3481.62, max 5156.54)"
    "bw_mem-bcopy-4mb (mb/s)","2301.25 (min 2205.88, max 2362.67)","3806.83 (min 3730.65, max 3883.50)","3518.88 (min 3414.13, max 3790.87)","1666.83 (min 1475.47, max 1811.87)","3771.82 (min 3021.72, max 4682.93)","3446.82 (min 2694.51, max 4290.31)"
    "bw_mem-bcopy-8mb (mb/s)","2308.40 (min 2251.30, max 2367.21)","3068.07 (min 3051.49, max 3089.40)","3495.89 (min 3370.31, max 3788.48)","1715.64 (min 1599.04, max 1854.86)","3194.06 (min 2606.29, max 3769.44)","3050.50 (min 2646.38, max 3645.20)"
    "bw_mem-bzero-16mb (mb/s)","2290.03 (min 2233.70, max 2345.70)","9638.93 (min 9621.17, max 9658.92)","10619.00 (min 10486.65, max 10884.35)","7203.37 (min 7142.86, max 7318.19)","10080.90 (min 9567.95, max 10514.21)","10861.82 (min 10792.58, max 10897.33)"
    "bw_mem-bzero-1mb (mb/s)","3967.62 (min 3153.99, max 4877.10)","8689.67 (min 4520.80, max 12565.07)","8652.05 (min 4245.11, max 13105.92)","4546.98 (min 1835.24, max 7301.87)","11600.67 (min 8886.57, max 13681.37)","11739.79 (min 9303.21, max 13768.12)"
    "bw_mem-bzero-2mb (mb/s)","2628.10 (min 2365.00, max 2929.87)","8058.17 (min 3861.00, max 12234.62)","7520.19 (min 3533.57, max 11695.91)","4413.67 (min 1592.99, max 7318.35)","8695.15 (min 3905.56, max 13437.44)","8974.79 (min 3481.62, max 13715.94)"
    "bw_mem-bzero-4mb (mb/s)","2356.50 (min 2205.88, max 2471.04)","7876.35 (min 3730.65, max 11962.62)","7118.16 (min 3414.13, max 10972.93)","4429.40 (min 1475.47, max 7319.91)","7551.39 (min 3021.72, max 11799.41)","7884.33 (min 2694.51, max 12642.67)"
    "bw_mem-bzero-8mb (mb/s)","2304.94 (min 2242.15, max 2367.21)","7364.76 (min 3051.49, max 11736.66)","7075.99 (min 3370.31, max 10915.91)","4456.46 (min 1599.04, max 7320.64)","6773.39 (min 2606.29, max 10785.31)","7176.12 (min 2646.38, max 11339.48)"
    "bw_mem-cp-16mb (mb/s)","964.64 (min 940.35, max 988.94)","1538.92 (min 1505.88, max 1565.25)","2139.33 (min 2109.98, max 2186.69)","873.51 (min 849.98, max 917.22)","1978.68 (min 1852.71, max 2178.35)","2181.75 (min 2098.36, max 2305.48)"
    "bw_mem-cp-1mb (mb/s)","2978.41 (min 1181.63, max 4877.17)","7110.93 (min 1670.69, max 12614.89)","7564.33 (min 2326.83, max 13155.52)","4178.82 (min 833.75, max 7635.04)","8323.30 (min 2933.70, max 13678.91)","8368.31 (min 2701.73, max 13743.22)"
    "bw_mem-cp-2mb (mb/s)","1924.53 (min 960.15, max 2940.10)","6861.92 (min 1417.18, max 12219.23)","6746.85 (min 2110.08, max 11627.91)","4094.71 (min 819.22, max 7473.31)","7547.18 (min 1885.31, max 13306.96)","8057.41 (min 2241.79, max 13693.56)"
    "bw_mem-cp-4mb (mb/s)","1686.17 (min 932.51, max 2473.33)","6740.10 (min 1492.82, max 11964.85)","6407.74 (min 2056.56, max 10895.22)","4077.81 (min 850.07, max 7399.93)","6786.96 (min 2099.37, max 11795.32)","7433.94 (min 2295.77, max 12709.62)"
    "bw_mem-cp-8mb (mb/s)","1631.59 (min 927.75, max 2358.84)","6583.92 (min 1461.45, max 11734.51)","6393.28 (min 2083.06, max 10945.78)","4077.78 (min 870.61, max 7355.65)","6179.82 (min 1814.47, max 10788.94)","6767.14 (min 2141.04, max 11315.42)"
    "bw_mem-fcp-16mb (mb/s)","2373.37 (min 2327.61, max 2422.41)","2783.90 (min 2769.12, max 2789.40)","3461.34 (min 3356.06, max 3747.51)","1622.40 (min 1479.43, max 1727.49)","3083.53 (min 2498.05, max 3665.52)","2845.51 (min 2572.35, max 3421.36)"
    "bw_mem-fcp-1mb (mb/s)","3970.17 (min 3106.16, max 4877.10)","8235.06 (min 3836.32, max 12565.07)","8306.41 (min 3630.71, max 13105.92)","4417.25 (min 1593.20, max 7301.87)","10017.52 (min 6025.23, max 13681.37)","10185.50 (min 6339.43, max 13768.12)"
    "bw_mem-fcp-2mb (mb/s)","2668.91 (min 2415.95, max 2929.87)","8061.00 (min 3852.08, max 12234.62)","7230.48 (min 0.00, max 11695.91)","4374.14 (min 1469.08, max 7318.35)","8375.55 (min 3219.96, max 13437.44)","8629.23 (min 3185.35, max 13715.94)"
    "bw_mem-fcp-4mb (mb/s)","2380.90 (min 2283.97, max 2471.04)","7883.60 (min 3775.72, max 11962.62)","7111.14 (min 3323.36, max 10972.93)","4407.53 (min 1564.54, max 7319.91)","7471.20 (min 2892.79, max 11799.41)","7798.28 (min 2685.92, max 12642.67)"
    "bw_mem-fcp-8mb (mb/s)","2333.86 (min 2242.15, max 2411.82)","7358.68 (min 3030.88, max 11736.66)","7058.25 (min 3363.23, max 10915.91)","4416.81 (min 1587.30, max 7320.64)","6744.67 (min 2560.41, max 10785.31)","7142.26 (min 2626.83, max 11339.48)"
    "bw_mem-frd-16mb (mb/s)","6114.99 (min 5884.52, max 6331.62)","4789.08 (min 4780.40, max 4795.44)","4249.94 (min 4147.23, max 4653.87)","1805.26 (min 1743.68, max 1915.71)","3821.16 (min 3109.82, max 4422.94)","3331.93 (min 2664.89, max 4094.69)"
    "bw_mem-frd-1mb (mb/s)","4771.33 (min 3106.16, max 6896.55)","4708.76 (min 3836.32, max 5706.41)","4355.83 (min 3630.71, max 5017.65)","1773.66 (min 1593.20, max 2027.28)","7135.29 (min 6025.23, max 7802.58)","7077.05 (min 6339.43, max 7769.15)"
    "bw_mem-frd-2mb (mb/s)","4346.25 (min 2415.95, max 6427.42)","4840.79 (min 3852.08, max 5813.95)","3914.79 (min 0.00, max 5311.08)","1604.27 (min 1469.08, max 1900.78)","4207.69 (min 3219.96, max 5596.64)","3906.09 (min 3185.35, max 4940.15)"
    "bw_mem-frd-4mb (mb/s)","4228.07 (min 2283.97, max 6322.86)","4734.80 (min 3775.72, max 5680.81)","3906.78 (min 3323.36, max 4726.54)","1647.27 (min 1517.64, max 1903.55)","4026.84 (min 2892.79, max 5161.29)","3463.66 (min 2661.79, max 4638.07)"
    "bw_mem-frd-8mb (mb/s)","4224.67 (min 2306.47, max 6313.13)","4225.78 (min 3030.88, max 5426.49)","3855.86 (min 3363.23, max 4665.40)","1691.31 (min 1571.86, max 1919.16)","3725.72 (min 2560.41, max 5056.89)","3312.77 (min 2626.83, max 4581.90)"
    "bw_mem-fwr-16mb (mb/s)","2289.13 (min 2229.97, max 2345.01)","9630.44 (min 9599.52, max 9658.92)","10622.40 (min 10507.31, max 10862.19)","7227.96 (min 7173.82, max 7339.45)","10065.53 (min 9547.96, max 10517.67)","10883.69 (min 10843.78, max 10899.18)"
    "bw_mem-fwr-1mb (mb/s)","5503.33 (min 4558.20, max 6896.55)","8991.87 (min 5162.24, max 12614.89)","8794.05 (min 4587.16, max 13155.52)","4692.29 (min 1781.58, max 7635.04)","10554.73 (min 7499.54, max 13678.91)","10573.07 (min 6358.04, max 13743.22)"
    "bw_mem-fwr-2mb (mb/s)","4534.88 (min 2775.37, max 6427.42)","8964.32 (min 5719.39, max 12219.23)","8046.14 (min 4584.53, max 11627.91)","4495.00 (min 1544.88, max 7473.31)","8779.11 (min 3850.60, max 13306.96)","8947.21 (min 3615.18, max 13693.56)"
    "bw_mem-fwr-4mb (mb/s)","4260.71 (min 2350.87, max 6322.86)","8797.69 (min 5612.07, max 11964.85)","7507.67 (min 4204.63, max 10895.22)","4470.78 (min 1517.64, max 7399.93)","7860.93 (min 3567.61, max 11795.32)","7989.03 (min 2661.79, max 12709.62)"
    "bw_mem-fwr-8mb (mb/s)","4193.08 (min 2244.35, max 6313.13)","8538.76 (min 5370.03, max 11734.51)","7460.66 (min 4134.37, max 10945.78)","4491.73 (min 1571.86, max 7355.65)","7335.66 (min 3515.97, max 10788.94)","7468.59 (min 2696.78, max 11315.42)"
    "bw_mem-rd-16mb (mb/s)","6352.39 (min 6117.77, max 6597.03)","5107.56 (min 5085.82, max 5155.47)","4965.22 (min 4820.00, max 5404.49)","1841.87 (min 1787.91, max 1959.10)","4531.65 (min 3686.21, max 5211.73)","4011.95 (min 3242.81, max 4761.90)"
    "bw_mem-rd-1mb (mb/s)","9449.73 (min 3172.71, max 15393.39)","6538.03 (min 2132.61, max 10133.23)","5961.23 (min 3004.06, max 10137.58)","1883.30 (min 1569.86, max 2246.35)","15510.22 (min 12228.80, max 17350.44)","15695.54 (min 11174.21, max 17322.27)"
    "bw_mem-rd-2mb (mb/s)","3887.39 (min 928.79, max 7072.14)","4057.89 (min 1157.41, max 6557.38)","4232.63 (min 2783.09, max 6380.86)","1675.66 (min 1395.67, max 1955.99)","4795.28 (min 2515.27, max 7312.61)","4658.99 (min 2776.33, max 6802.72)"
    "bw_mem-rd-4mb (mb/s)","3593.41 (min 748.22, max 6666.67)","3815.40 (min 1194.56, max 6363.80)","3725.76 (min 2360.58, max 5547.85)","1727.35 (min 1550.59, max 1911.44)","3942.50 (min 2030.97, max 6160.95)","3946.06 (min 3315.10, max 5417.30)"
    "bw_mem-rd-8mb (mb/s)","3542.89 (min 711.36, max 6591.96)","3690.90 (min 1271.05, max 5957.92)","3613.61 (min 2240.58, max 5428.33)","1773.06 (min 1585.41, max 1951.70)","3932.59 (min 2016.64, max 6033.18)","3900.21 (min 3252.03, max 5316.50)"
    "bw_mem-rdwr-16mb (mb/s)","733.99 (min 715.34, max 752.34)","1866.44 (min 1774.23, max 1904.54)","2169.33 (min 2073.34, max 2258.93)","1745.80 (min 1708.31, max 1808.11)","1974.74 (min 1860.47, max 2150.54)","2453.56 (min 2351.56, max 2646.82)"
    "bw_mem-rdwr-1mb (mb/s)","3319.10 (min 1181.63, max 8832.93)","2763.77 (min 1670.69, max 6301.32)","3311.28 (min 2326.83, max 5330.88)","1252.81 (min 833.75, max 1827.15)","6375.38 (min 2933.70, max 9604.93)","6218.21 (min 2701.73, max 9608.41)"
    "bw_mem-rdwr-2mb (mb/s)","977.21 (min 936.91, max 1016.26)","1713.93 (min 1217.47, max 2461.32)","2439.19 (min 2110.08, max 3109.21)","1158.44 (min 819.22, max 1595.15)","2831.11 (min 1885.31, max 3873.72)","3277.41 (min 2241.79, max 4698.23)"
    "bw_mem-rdwr-4mb (mb/s)","868.21 (min 758.87, max 986.31)","1868.16 (min 1239.73, max 2411.45)","2209.98 (min 2056.56, max 2389.84)","1235.24 (min 850.07, max 1645.08)","2344.43 (min 2062.56, max 2725.72)","2773.62 (min 2295.77, max 3423.49)"
    "bw_mem-rdwr-8mb (mb/s)","849.71 (min 720.66, max 987.05)","1839.82 (min 1446.65, max 2323.56)","2168.05 (min 2083.06, max 2300.50)","1305.98 (min 870.61, max 1817.77)","2247.97 (min 1814.47, max 2807.51)","2561.96 (min 2141.04, max 3275.56)"
    "bw_mem-wr-16mb (mb/s)","724.24 (min 694.47, max 743.39)","1776.73 (min 1679.44, max 1835.49)","2231.11 (min 2216.37, max 2273.70)","1750.27 (min 1687.41, max 1838.24)","2051.47 (min 1937.75, max 2239.33)","2754.65 (min 2710.95, max 2813.93)"
    "bw_mem-wr-1mb (mb/s)","6524.35 (min 3172.71, max 15393.39)","3992.52 (min 2132.61, max 8189.73)","4294.28 (min 3004.06, max 9430.47)","1651.76 (min 1515.92, max 1827.15)","13060.53 (min 9403.19, max 17350.44)","13230.25 (min 8131.58, max 17322.27)"
    "bw_mem-wr-2mb (mb/s)","960.58 (min 928.79, max 989.28)","1751.06 (min 1157.41, max 2461.32)","2787.59 (min 2547.31, max 3109.21)","1492.24 (min 1388.89, max 1671.68)","3218.74 (min 2515.27, max 3873.72)","3769.99 (min 2776.33, max 4698.23)"
    "bw_mem-wr-4mb (mb/s)","774.28 (min 748.22, max 801.76)","1796.03 (min 1194.56, max 2411.45)","2347.75 (min 2216.48, max 2435.31)","1610.29 (min 1527.69, max 1756.18)","2489.52 (min 2030.97, max 3150.60)","3221.34 (min 2642.88, max 3673.77)"
    "bw_mem-wr-8mb (mb/s)","734.87 (min 711.36, max 758.44)","1869.85 (min 1271.05, max 2323.56)","2239.72 (min 2112.77, max 2300.50)","1703.23 (min 1585.41, max 1825.44)","2565.83 (min 2016.64, max 2981.74)","3125.89 (min 2645.50, max 3544.00)"
    "bw_mmap_rd-mo-1mb (mb/s)","11919.07 (min 10453.61, max 12278.05)","8752.77 (min 8494.07, max 8958.97)","8559.04 (min 8169.93, max 8805.51)","2026.97 (min 1962.18, max 2149.77)","12901.81 (min 12834.42, max 12916.14)","12902.33 (min 12839.06, max 12916.14)"
    "bw_mmap_rd-o2c-1mb (mb/s)","1447.52 (min 1361.07, max 1646.90)","1532.57 (min 1285.11, max 1664.51)","1328.22 (min 1172.14, max 1498.13)","727.37 (min 658.65, max 794.91)","2532.79 (min 2331.84, max 2966.26)","2193.41 (min 1846.26, max 2641.78)"
    "bw_pipe (mb/s)","758.58 (min 732.59, max 777.56)","947.73 (min 900.50, max 973.20)","976.30 (min 952.00, max 1000.65)","772.90 (min 750.93, max 809.54)","971.64 (min 907.58, max 1020.56)","912.68 (min 796.46, max 1012.75)"
    "bw_unix (mb/s)","1607.04 (min 1549.65, max 1692.82)","1936.06 (min 1893.35, max 1967.65)","1991.06 (min 1869.53, max 2088.48)","1075.13 (min 1053.08, max 1122.04)","2887.72 (min 2676.18, max 3095.23)","2387.82 (min 1610.12, max 3148.32)"
    "lat_connect (us)","37.46 (min 37.05, max 38.24)","37.20 (min 36.66, max 37.88)","37.82 (min 37.30, max 38.57)","57.06 (min 56.43, max 57.46)","37.84 (min 37.24, max 38.42)","37.77 (min 37.27, max 38.57)"
    "lat_ctx-2-128k (us)","5.33 (min 5.02, max 5.55)","5.26 (min 4.98, max 5.58)","5.31 (min 5.05, max 5.55)","7.87 (min 7.64, max 8.20)","5.48 (min 5.23, max 5.77)","6.97 (min 5.32, max 8.63)"
    "lat_ctx-2-256k (us)","4.60 (min 4.32, max 5.07)","4.98 (min 4.34, max 6.41)","4.67 (min 4.35, max 5.04)","8.50 (min 6.74, max 10.64)","4.59 (min 4.39, max 4.92)","4.99 (min 4.41, max 7.59)"
    "lat_ctx-4-128k (us)","5.22 (min 4.95, max 5.58)","5.19 (min 4.90, max 5.40)","5.25 (min 4.92, max 5.47)","7.64 (min 6.99, max 8.57)","5.16 (min 4.94, max 5.43)","6.73 (min 5.52, max 7.61)"
    "lat_ctx-4-256k (us)","4.17 (min 3.86, max 4.63)","4.16 (min 3.82, max 4.54)","4.36 (min 4.02, max 4.71)","7.39 (min 5.49, max 9.58)","3.70 (min 3.44, max 3.97)","5.79 (min 5.24, max 6.99)"
    "lat_fs-0k (num_files)","404.40 (min 371.00, max 421.00)","410.88 (min 401.00, max 421.00)","396.13 (min 350.00, max 414.00)","240.50 (min 218.00, max 266.00)","404.50 (min 381.00, max 417.00)","399.88 (min 376.00, max 412.00)"
    "lat_fs-10k (num_files)","156.10 (min 143.00, max 163.00)","166.13 (min 148.00, max 182.00)","166.38 (min 149.00, max 189.00)","115.00 (min 107.00, max 123.00)","183.75 (min 176.00, max 199.00)","189.50 (min 177.00, max 201.00)"
    "lat_fs-1k (num_files)","231.20 (min 206.00, max 236.00)","244.13 (min 233.00, max 261.00)","228.88 (min 211.00, max 243.00)","166.13 (min 150.00, max 177.00)","245.75 (min 216.00, max 261.00)","247.38 (min 233.00, max 264.00)"
    "lat_fs-4k (num_files)","237.20 (min 219.00, max 261.00)","257.13 (min 240.00, max 262.00)","238.25 (min 202.00, max 256.00)","156.38 (min 138.00, max 174.00)","265.50 (min 251.00, max 274.00)","267.75 (min 264.00, max 270.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","11.98 (min 11.23, max 13.01)","11.88 (min 11.14, max 12.71)","13.11 (min 12.09, max 13.70)","32.66 (min 30.66, max 33.44)","5.83 (min 5.65, max 6.19)","5.98 (min 5.69, max 6.29)"
    "lat_mem_rd-stride128-sz125k (ns)","5.57","5.57","5.57","5.57 (min 5.53, max 5.59)","5.65","5.65"
    "lat_mem_rd-stride128-sz250k (ns)","5.57 (min 5.57, max 5.59)","5.57 (min 5.57, max 5.59)","5.57","5.84 (min 5.83, max 5.85)","5.65 (min 5.65, max 5.69)","5.65"
    "lat_mem_rd-stride128-sz31k (ns)","3.70 (min 2.00, max 4.67)","3.89 (min 3.34, max 4.67)","4.17 (min 3.34, max 5.12)","3.92 (min 3.65, max 4.20)","4.12 (min 3.35, max 5.20)","4.13 (min 3.39, max 4.74)"
    "lat_mem_rd-stride128-sz50 (ns)","2.00","2.00","2.00","2.15","2.00","2.00"
    "lat_mem_rd-stride128-sz500k (ns)","5.58 (min 5.57, max 5.62)","5.66 (min 5.57, max 5.83)","5.90 (min 5.57, max 7.14)","12.36 (min 9.83, max 15.73)","5.65","5.65"
    "lat_mem_rd-stride128-sz62k (ns)","5.34 (min 4.67, max 5.57)","5.29 (min 5.12, max 5.59)","5.40 (min 5.12, max 5.57)","5.24 (min 5.22, max 5.26)","5.40 (min 4.78, max 5.65)","5.39 (min 4.74, max 5.65)"
    "lat_mmap-1m (us)","32.80 (min 28.00, max 36.00)","31.13 (min 28.00, max 34.00)","33.00 (min 28.00, max 36.00)","53.75 (min 50.00, max 58.00)","31.25 (min 29.00, max 35.00)","31.13 (min 29.00, max 36.00)"
    "lat_ops-double-add (ns)","1.96","1.96","1.96","2.86","1.96","1.96"
    "lat_ops-double-div (ns)","9.01 (min 9.01, max 9.02)","9.01 (min 9.01, max 9.02)","9.01 (min 9.01, max 9.02)","15.74 (min 15.74, max 15.75)","9.01","9.01"
    "lat_ops-double-mul (ns)","2.00","2.00","2.00","2.86","2.00","2.00"
    "lat_ops-float-add (ns)","1.96","1.96","1.96","2.86","1.96","1.96"
    "lat_ops-float-div (ns)","5.51","5.51 (min 5.50, max 5.51)","5.51","9.30 (min 9.30, max 9.31)","5.50 (min 5.50, max 5.51)","5.51 (min 5.50, max 5.51)"
    "lat_ops-float-mul (ns)","2.00","2.00","2.00 (min 2.00, max 2.01)","2.86","2.00","2.00"
    "lat_ops-int-add (ns)","0.50","0.50","0.50","0.72","0.50","0.50"
    "lat_ops-int-bit (ns)","0.33","0.33","0.33","0.48","0.33","0.33"
    "lat_ops-int-div (ns)","4.01 (min 4.00, max 4.01)","4.01 (min 4.00, max 4.01)","4.01 (min 4.00, max 4.02)","4.29 (min 4.29, max 4.30)","4.00 (min 4.00, max 4.01)","4.00 (min 4.00, max 4.01)"
    "lat_ops-int-mod (ns)","4.67 (min 4.67, max 4.68)","4.67 (min 4.67, max 4.68)","4.67 (min 4.67, max 4.68)","4.54 (min 4.53, max 4.54)","4.67","4.67"
    "lat_ops-int-mul (ns)","1.52","1.52","1.52","3.08 (min 3.07, max 3.09)","1.52","1.52"
    "lat_ops-int64-add (ns)","0.50","0.50","0.50","0.72","0.50","0.50"
    "lat_ops-int64-bit (ns)","0.33","0.33","0.33","0.48","0.33","0.33"
    "lat_ops-int64-div (ns)","3.00 (min 3.00, max 3.01)","3.00","3.00 (min 3.00, max 3.01)","6.80 (min 6.79, max 6.80)","3.00","3.00"
    "lat_ops-int64-mod (ns)","5.68 (min 5.67, max 5.68)","5.67 (min 5.67, max 5.68)","5.67 (min 5.67, max 5.68)","5.25","5.67 (min 5.67, max 5.68)","5.67 (min 5.67, max 5.68)"
    "lat_ops-int64-mul (ns)","2.52","2.52","2.52 (min 2.52, max 2.53)","3.56 (min 3.55, max 3.57)","2.52","2.52"
    "lat_pagefault (us)","0.27 (min 0.25, max 0.45)","0.24 (min 0.23, max 0.24)","0.25 (min 0.24, max 0.26)","0.74 (min 0.53, max 1.11)","0.24 (min 0.23, max 0.25)","0.24 (min 0.24, max 0.25)"
    "lat_pipe (us)","14.80 (min 14.10, max 15.59)","14.54 (min 13.93, max 15.28)","14.76 (min 13.74, max 15.27)","25.75 (min 25.14, max 26.41)","16.54 (min 16.08, max 17.14)","20.40 (min 18.01, max 22.46)"
    "lat_proc-exec (us)","421.84 (min 402.46, max 434.25)","370.33 (min 354.69, max 382.43)","432.45 (min 407.08, max 444.00)","733.11 (min 697.63, max 762.86)","337.27 (min 328.18, max 346.94)","405.26 (min 346.80, max 434.62)"
    "lat_proc-fork (us)","386.32 (min 377.79, max 395.15)","341.41 (min 332.76, max 352.80)","388.67 (min 379.92, max 402.54)","646.59 (min 619.44, max 677.38)","312.95 (min 300.47, max 324.94)","386.13 (min 335.94, max 413.07)"
    "lat_proc-proccall (us)","0.00","0.00","0.00","0.01","0.00","0.00"
    "lat_select (us)","12.04 (min 11.45, max 13.30)","12.64 (min 11.44, max 13.64)","12.16 (min 11.43, max 13.34)","34.17 (min 33.91, max 34.35)","12.41 (min 11.43, max 13.47)","12.44 (min 11.46, max 13.31)"
    "lat_sem (us)","1.99 (min 1.50, max 2.32)","1.99 (min 1.68, max 2.17)","2.11 (min 1.81, max 2.56)","3.11 (min 2.48, max 3.95)","1.78 (min 1.39, max 2.09)","2.47 (min 1.89, max 2.94)"
    "lat_sig-catch (us)","3.13 (min 2.89, max 3.34)","3.16 (min 2.86, max 3.35)","3.14 (min 2.88, max 3.32)","5.52 (min 5.25, max 5.73)","3.17 (min 2.88, max 3.41)","3.17 (min 2.96, max 3.39)"
    "lat_sig-install (us)","0.54 (min 0.52, max 0.56)","0.55 (min 0.53, max 0.57)","0.55 (min 0.53, max 0.56)","0.66 (min 0.64, max 0.70)","0.55 (min 0.54, max 0.57)","0.55 (min 0.54, max 0.57)"
    "lat_sig-prot (us)","0.46 (min 0.26, max 0.64)","0.48 (min 0.33, max 0.62)","0.58 (min 0.30, max 1.06)","0.77 (min 0.57, max 1.38)","0.59 (min 0.45, max 1.27)","0.50 (min 0.35, max 0.62)"
    "lat_syscall-fstat (us)","0.98 (min 0.91, max 1.08)","1.00 (min 0.94, max 1.08)","0.99 (min 0.94, max 1.07)","1.98 (min 1.90, max 2.07)","0.99 (min 0.93, max 1.08)","1.01 (min 0.93, max 1.11)"
    "lat_syscall-null (us)","0.40 (min 0.39, max 0.42)","0.40 (min 0.39, max 0.42)","0.40 (min 0.39, max 0.41)","0.46 (min 0.46, max 0.50)","0.40 (min 0.39, max 0.42)","0.40 (min 0.39, max 0.42)"
    "lat_syscall-open (us)","166.00 (min 149.65, max 220.24)","157.35 (min 129.86, max 211.64)","161.05 (min 132.58, max 196.79)","173.89 (min 150.84, max 199.96)","201.65 (min 93.72, max 690.67)","212.77 (min 124.79, max 314.00)"
    "lat_syscall-read (us)","0.51 (min 0.50, max 0.53)","0.52 (min 0.50, max 0.56)","0.51 (min 0.50, max 0.52)","0.82 (min 0.80, max 0.89)","0.51 (min 0.50, max 0.53)","0.51 (min 0.49, max 0.52)"
    "lat_syscall-stat (us)","2.31 (min 2.22, max 2.47)","2.34 (min 2.25, max 2.46)","2.35 (min 2.22, max 2.49)","4.79 (min 4.63, max 4.98)","2.33 (min 2.25, max 2.47)","2.36 (min 2.28, max 2.55)"
    "lat_syscall-write (us)","0.49 (min 0.47, max 0.51)","0.50 (min 0.47, max 0.52)","0.50 (min 0.47, max 0.53)","0.78 (min 0.75, max 0.84)","0.49 (min 0.47, max 0.51)","0.50 (min 0.47, max 0.51)"
    "lat_tcp (us)","0.81 (min 0.79, max 0.83)","0.83 (min 0.81, max 0.86)","0.82 (min 0.80, max 0.85)","0.92 (min 0.91, max 0.97)","0.82 (min 0.79, max 0.84)","0.83 (min 0.81, max 0.86)"
    "lat_unix (us)","19.98 (min 19.51, max 20.42)","20.26 (min 19.39, max 21.11)","20.13 (min 19.48, max 21.07)","30.29 (min 29.18, max 31.07)","20.20 (min 19.79, max 20.60)","22.99 (min 19.76, max 28.54)"
    "latency_for_0.50_mb_block_size (nanosec)","5.58 (min 5.57, max 5.62)","5.66 (min 5.57, max 5.83)","5.90 (min 5.57, max 7.14)","12.36 (min 9.83, max 15.73)","5.65","5.65"
    "latency_for_1.00_mb_block_size (nanosec)","5.99 (min 0.00, max 13.01)","5.94 (min 0.00, max 12.71)","6.56 (min 0.00, max 13.70)","16.33 (min 0.00, max 33.44)","2.92 (min 0.00, max 6.19)","2.99 (min 0.00, max 6.29)"
    "pipe_bandwidth (mb\s)","758.58 (min 732.59, max 777.56)","947.73 (min 900.50, max 973.20)","976.30 (min 952.00, max 1000.65)","772.90 (min 750.93, max 809.54)","971.64 (min 907.58, max 1020.56)","912.68 (min 796.46, max 1012.75)"
    "pipe_latency (microsec)","14.80 (min 14.10, max 15.59)","14.54 (min 13.93, max 15.28)","14.76 (min 13.74, max 15.27)","25.75 (min 25.14, max 26.41)","16.54 (min 16.08, max 17.14)","20.40 (min 18.01, max 22.46)"
    "procedure_call (microsec)","0.00","0.00","0.00","0.01","0.00","0.00"
    "select_on_200_tcp_fds (microsec)","12.04 (min 11.45, max 13.30)","12.64 (min 11.44, max 13.64)","12.16 (min 11.43, max 13.34)","34.17 (min 33.91, max 34.35)","12.41 (min 11.43, max 13.47)","12.44 (min 11.46, max 13.31)"
    "semaphore_latency (microsec)","1.99 (min 1.50, max 2.32)","1.99 (min 1.68, max 2.17)","2.11 (min 1.81, max 2.56)","3.11 (min 2.48, max 3.95)","1.78 (min 1.39, max 2.09)","2.47 (min 1.89, max 2.94)"
    "signal_handler_latency (microsec)","0.54 (min 0.52, max 0.56)","0.55 (min 0.53, max 0.57)","0.55 (min 0.53, max 0.56)","0.66 (min 0.64, max 0.70)","0.55 (min 0.54, max 0.57)","0.55 (min 0.54, max 0.57)"
    "signal_handler_overhead (microsec)","3.13 (min 2.89, max 3.34)","3.16 (min 2.86, max 3.35)","3.14 (min 2.88, max 3.32)","5.52 (min 5.25, max 5.73)","3.17 (min 2.88, max 3.41)","3.17 (min 2.96, max 3.39)"
    "tcp_ip_connection_cost_to_localhost (microsec)","37.46 (min 37.05, max 38.24)","37.20 (min 36.66, max 37.88)","37.82 (min 37.30, max 38.57)","57.06 (min 56.43, max 57.46)","37.84 (min 37.24, max 38.42)","37.77 (min 37.27, max 38.57)"
    "tcp_latency_using_localhost (microsec)","0.81 (min 0.79, max 0.83)","0.83 (min 0.81, max 0.86)","0.82 (min 0.80, max 0.85)","0.92 (min 0.91, max 0.97)","0.82 (min 0.79, max 0.84)","0.83 (min 0.81, max 0.86)"




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
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cpu_clock (mhz)","2000.00","2000.00","2000.00","1400.00","2000.00","2000.00"
    "dhrystone_per_mhz (dmips/mhz)","5.26 (min 4.70, max 5.70)","5.57 (min 4.40, max 5.70)","5.10 (min 4.40, max 5.70)","2.91 (min 2.90, max 3.00)","5.10 (min 4.40, max 5.70)","5.70"
    "dhrystone_per_second (dhrystonep)","18484848.56 (min 16666667.00, max 20000000.00)","19538461.50 (min 15384615.00, max 20000000.00)","17945804.25 (min 15384615.00, max 20000000.00)","7175925.81 (min 7142857.00, max 7407407.50)","17945804.25 (min 15384615.00, max 20000000.00)","20000000.00"




Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

::

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "whetstone (mips)","10000.00","10000.00","10000.00","8125.00 (min 5000.00, max 10000.00)","10000.00","10000.00"




Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "linpack (kflops)","2446304.22 (min 2359680.00, max 2513422.00)","2476130.13 (min 2345173.00, max 2600026.00)","2537165.75 (min 2387575.00, max 2622867.00)","575723.88 (min 573082.00, max 578392.00)","2498958.63 (min 2396742.00, max 2588265.00)","2448299.13 (min 2334013.00, max 2549820.00)"




NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "assignment (iterations)","31.86 (min 31.68, max 31.99)","31.85 (min 31.52, max 31.95)","31.92 (min 31.86, max 31.99)","14.50 (min 14.45, max 14.52)","31.77 (min 31.63, max 31.85)","31.74 (min 31.42, max 31.90)"
    "fourier (iterations)","60439.60 (min 59005.00, max 65633.00)","61431.00 (min 58899.00, max 65354.00)","61461.63 (min 59223.00, max 65637.00)","22829.88 (min 22822.00, max 22831.00)","59890.25 (min 59116.00, max 60492.00)","61332.00 (min 59750.00, max 64969.00)"
    "fp_emulation (iterations)","387.98 (min 387.93, max 388.05)","387.97 (min 387.84, max 388.03)","387.99 (min 387.93, max 388.03)","215.64 (min 215.62, max 215.65)","387.97 (min 387.89, max 388.03)","388.00 (min 387.95, max 388.04)"
    "huffman (iterations)","2406.61 (min 2403.20, max 2413.10)","2408.65 (min 2405.90, max 2411.20)","2406.84 (min 2400.40, max 2416.10)","1184.05 (min 1183.60, max 1184.30)","2406.41 (min 2398.60, max 2412.80)","2403.26 (min 2389.10, max 2409.90)"
    "idea (iterations)","7996.17 (min 7995.20, max 7996.50)","7996.33 (min 7995.20, max 7996.60)","7996.25 (min 7996.00, max 7996.50)","3444.76 (min 3444.60, max 3444.90)","7996.41 (min 7995.50, max 7996.60)","7996.46 (min 7996.20, max 7997.00)"
    "lu_decomposition (iterations)","1369.87 (min 1345.70, max 1391.10)","1367.31 (min 1355.90, max 1374.20)","1373.66 (min 1356.60, max 1389.00)","529.84 (min 527.92, max 531.90)","1362.08 (min 1339.20, max 1376.50)","1361.83 (min 1331.90, max 1377.70)"
    "neural_net (iterations)","28.16 (min 26.96, max 29.03)","28.51 (min 27.57, max 29.03)","28.75 (min 27.06, max 29.03)","8.65 (min 8.65, max 8.66)","28.33 (min 26.31, max 29.03)","28.41 (min 27.52, max 29.01)"
    "numeric_sort (iterations)","873.07 (min 855.53, max 884.84)","875.87 (min 869.15, max 882.72)","881.12 (min 875.38, max 885.36)","626.86 (min 619.59, max 629.11)","875.90 (min 866.80, max 880.73)","875.68 (min 867.45, max 881.62)"
    "string_sort (iterations)","341.65 (min 312.60, max 361.15)","350.80 (min 341.26, max 358.43)","355.09 (min 350.91, max 361.36)","163.94 (min 163.93, max 163.94)","350.73 (min 342.34, max 356.86)","347.82 (min 311.66, max 355.42)"




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
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "add (mb/s)","5330.16 (min 5217.90, max 5457.70)","5280.50 (min 5259.60, max 5294.00)","6371.04 (min 6212.00, max 6497.20)","2477.46 (min 2403.10, max 2614.00)","5878.95 (min 5625.70, max 6250.70)","5659.85 (min 5419.90, max 5789.80)"
    "copy (mb/s)","4680.62 (min 4598.40, max 4776.80)","5536.96 (min 5526.40, max 5544.00)","7221.28 (min 6943.90, max 7755.70)","3603.89 (min 3523.00, max 3810.40)","6066.85 (min 5188.10, max 6874.30)","5644.11 (min 5285.90, max 6196.50)"
    "scale (mb/s)","4753.30 (min 4682.50, max 4843.10)","5398.83 (min 5384.70, max 5409.80)","7338.84 (min 7060.00, max 7859.70)","3292.09 (min 3167.90, max 3465.20)","6173.41 (min 5274.60, max 7011.70)","5633.58 (min 5286.80, max 6220.30)"
    "triad (mb/s)","5338.12 (min 5231.10, max 5465.60)","5261.99 (min 5238.10, max 5277.20)","6376.19 (min 6218.40, max 6499.70)","2268.64 (min 2220.20, max 2372.80)","5876.20 (min 5617.20, max 6249.20)","5653.89 (min 5421.30, max 5780.50)"




CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","82.57 (min 81.97, max 83.33)","82.14 (min 80.00, max 82.64)","82.45 (min 81.97, max 82.64)","41.95 (min 41.67, max 42.02)","82.73 (min 82.64, max 83.33)","82.82 (min 81.97, max 83.33)"
    "core (workloads/)","0.77 (min 0.77, max 0.78)","0.77 (min 0.77, max 0.78)","0.77 (min 0.77, max 0.78)","0.30","0.78 (min 0.77, max 0.78)","0.77 (min 0.77, max 0.78)"
    "coremark-pro ()","2465.09 (min 2447.25, max 2487.00)","2495.29 (min 2482.04, max 2519.86)","2478.91 (min 2450.48, max 2514.48)","917.83 (min 896.57, max 933.54)","2496.36 (min 2468.69, max 2515.06)","2503.75 (min 2472.84, max 2517.13)"
    "linear_alg-mid-100x100-sp (workloads/)","80.80 (min 79.49, max 82.51)","80.98 (min 80.26, max 82.10)","80.67 (min 79.87, max 81.83)","14.68 (min 14.67, max 14.68)","79.44 (min 78.13, max 81.30)","80.39 (min 79.11, max 81.97)"
    "loops-all-mid-10k-sp (workloads/)","2.47 (min 2.47, max 2.48)","2.47 (min 2.46, max 2.48)","2.48 (min 2.45, max 2.48)","0.70 (min 0.70, max 0.71)","2.46 (min 2.46, max 2.47)","2.46 (min 2.46, max 2.47)"
    "nnet_test (workloads/)","3.58 (min 3.41, max 3.67)","3.62 (min 3.52, max 3.84)","3.63 (min 3.38, max 3.86)","1.09","3.50 (min 3.34, max 3.66)","3.63 (min 3.60, max 3.66)"
    "parser-125k (workloads/)","10.99 (min 10.87, max 11.11)","11.08 (min 10.99, max 11.11)","11.06 (min 10.99, max 11.11)","8.73 (min 8.62, max 8.77)","10.87","10.85 (min 10.75, max 10.87)"
    "radix2-big-64k (workloads/)","258.56 (min 242.37, max 265.53)","275.23 (min 270.64, max 283.05)","264.48 (min 236.52, max 279.17)","59.49 (min 47.42, max 69.16)","296.29 (min 272.78, max 307.79)","294.07 (min 271.59, max 307.31)"
    "sha-test (workloads/)","157.08 (min 156.25, max 158.73)","158.73","157.31 (min 156.25, max 158.73)","81.22 (min 80.65, max 81.30)","158.73","158.42 (min 156.25, max 158.73)"
    "zip-test (workloads/)","46.66 (min 45.45, max 47.62)","47.62","47.31 (min 45.45, max 47.62)","22.10 (min 21.74, max 22.22)","47.62","47.08 (min 45.45, max 47.62)"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","163.41 (min 161.29, max 163.93)","163.64 (min 161.29, max 163.93)","162.81 (min 158.73, max 163.93)","83.54 (min 82.64, max 84.03)","163.96 (min 161.29, max 166.67)","164.96 (min 163.93, max 166.67)"
    "core (workloads/)","1.55 (min 1.54, max 1.55)","1.55 (min 1.54, max 1.56)","1.54 (min 1.53, max 1.55)","0.60","1.55 (min 1.54, max 1.56)","1.55"
    "coremark-pro ()","4254.37 (min 4113.16, max 4363.75)","4353.82 (min 4277.67, max 4413.16)","4403.11 (min 4355.51, max 4500.29)","1634.39 (min 1620.08, max 1655.03)","4693.73 (min 4639.00, max 4720.56)","4906.76 (min 4726.41, max 5010.90)"
    "linear_alg-mid-100x100-sp (workloads/)","160.22 (min 158.23, max 162.87)","159.54 (min 156.74, max 163.40)","160.13 (min 158.23, max 162.87)","29.34 (min 29.33, max 29.34)","159.81 (min 158.73, max 160.77)","160.78 (min 158.73, max 162.34)"
    "loops-all-mid-10k-sp (workloads/)","3.96 (min 3.50, max 4.19)","3.97 (min 3.63, max 4.32)","3.99 (min 3.84, max 4.19)","1.28 (min 1.27, max 1.29)","4.06 (min 3.88, max 4.38)","4.47 (min 3.90, max 4.92)"
    "nnet_test (workloads/)","7.23 (min 7.04, max 7.60)","7.19 (min 6.69, max 7.70)","7.31 (min 7.07, max 7.67)","2.17","7.22 (min 7.11, max 7.29)","7.22 (min 7.18, max 7.31)"
    "parser-125k (workloads/)","20.68 (min 20.41, max 20.83)","21.23 (min 21.05, max 21.28)","20.44 (min 20.20, max 20.83)","13.10 (min 12.58, max 13.89)","21.08 (min 20.83, max 21.28)","21.17 (min 20.83, max 21.51)"
    "radix2-big-64k (workloads/)","223.92 (min 194.82, max 253.55)","263.32 (min 242.95, max 286.62)","281.70 (min 262.40, max 317.36)","64.34 (min 60.39, max 67.36)","418.78 (min 411.69, max 426.26)","556.42 (min 414.25, max 619.96)"
    "sha-test (workloads/)","302.52 (min 285.71, max 312.50)","298.87 (min 270.27, max 312.50)","304.91 (min 277.78, max 312.50)","161.29","320.06 (min 312.50, max 322.58)","320.06 (min 312.50, max 322.58)"
    "zip-test (workloads/)","80.36 (min 62.50, max 86.96)","83.19 (min 76.92, max 90.91)","86.06 (min 80.00, max 90.91)","42.55","93.07 (min 90.91, max 95.24)","94.70 (min 90.91, max 95.24)"

 


.. csv-table:: CoreMarkProFourCore Benchmarks
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","160.80 (min 156.25, max 163.93)","162.94 (min 161.29, max 163.93)","161.63 (min 158.73, max 163.93)","159.08 (min 153.85, max 161.29)","322.58"
    "core (workloads/)","1.55 (min 1.54, max 1.55)","1.54 (min 1.54, max 1.55)","1.54 (min 1.54, max 1.55)","1.19 (min 1.18, max 1.20)","3.09 (min 3.08, max 3.10)"
    "coremark-pro ()","4137.59 (min 4080.30, max 4234.65)","4321.76 (min 4265.20, max 4363.64)","4343.83 (min 4235.39, max 4405.19)","2564.87 (min 2531.35, max 2580.49)","8776.25 (min 8664.83, max 8875.66)"
    "linear_alg-mid-100x100-sp (workloads/)","159.92 (min 155.76, max 161.81)","160.14 (min 158.23, max 161.81)","158.83 (min 153.85, max 162.34)","56.25 (min 55.68, max 56.37)","311.07 (min 304.88, max 314.47)"
    "loops-all-mid-10k-sp (workloads/)","4.04 (min 3.88, max 4.23)","4.03 (min 3.53, max 4.23)","4.08 (min 3.88, max 4.28)","2.07 (min 2.00, max 2.12)","7.49 (min 7.19, max 7.73)"
    "nnet_test (workloads/)","7.29 (min 7.07, max 7.62)","7.32 (min 7.24, max 7.41)","7.35 (min 7.09, max 7.57)","3.62 (min 3.61, max 3.62)","12.09 (min 11.98, max 12.27)"
    "parser-125k (workloads/)","19.32 (min 18.78, max 19.70)","20.37 (min 20.10, max 20.73)","18.94 (min 18.43, max 19.51)","8.76 (min 8.26, max 9.24)","39.73 (min 37.38, max 41.67)"
    "radix2-big-64k (workloads/)","185.14 (min 169.15, max 205.89)","239.89 (min 231.05, max 251.26)","274.90 (min 225.68, max 292.57)","93.19 (min 87.57, max 98.36)","828.82 (min 761.62, max 882.61)"
    "sha-test (workloads/)","302.36 (min 285.71, max 312.50)","303.44 (min 285.71, max 312.50)","304.62 (min 285.71, max 312.50)","270.27","526.32"
    "zip-test (workloads/)","79.62 (min 75.47, max 83.33)","85.04 (min 80.00, max 88.89)","83.16 (min 75.47, max 88.89)","77.12 (min 75.47, max 78.43)","179.84 (min 173.91, max 181.82)"

 


.. csv-table:: CoreMarkProEightCore Benchmarks
    :header: "Benchmarks","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","625.00"
    "core (workloads/)","6.18 (min 6.16, max 6.21)"
    "coremark-pro ()","14093.90 (min 13646.37, max 14258.78)"
    "linear_alg-mid-100x100-sp (workloads/)","576.40 (min 568.18, max 581.40)"
    "loops-all-mid-10k-sp (workloads/)","10.43 (min 10.10, max 10.69)"
    "nnet_test (workloads/)","18.65 (min 18.08, max 19.12)"
    "parser-125k (workloads/)","72.41 (min 70.80, max 73.39)"
    "radix2-big-64k (workloads/)","843.23 (min 824.40, max 866.55)"
    "sha-test (workloads/)","769.23"
    "zip-test (workloads/)","307.03 (min 228.57, max 320.00)"

 
 


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
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "4m-check (workloads/)","826.34 (min 802.05, max 865.35)","827.56 (min 808.02, max 847.75)","780.53 (min 763.59, max 804.38)","398.07 (min 391.85, max 410.64)","1120.79 (min 1099.38, max 1148.37)","991.66 (min 979.62, max 998.40)"
    "4m-check-reassembly (workloads/)","115.54 (min 111.86, max 123.31)","140.00 (min 137.74, max 143.06)","139.23 (min 124.07, max 143.27)","116.38 (min 114.16, max 120.63)","177.38 (min 167.50, max 190.84)","185.77 (min 179.21, max 192.31)"
    "4m-check-reassembly-tcp (workloads/)","85.40 (min 83.61, max 87.41)","94.36 (min 92.25, max 96.15)","86.90 (min 76.92, max 89.93)","58.03 (min 57.21, max 59.38)","107.63 (min 102.88, max 113.12)","107.43 (min 104.60, max 110.13)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","39.68 (min 39.11, max 40.57)","43.38 (min 41.12, max 44.28)","40.76 (min 39.68, max 41.58)","32.44 (min 31.90, max 32.93)","54.74 (min 53.33, max 56.50)","36.15 (min 33.30, max 39.47)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","2.67 (min 2.62, max 2.69)","2.70 (min 2.66, max 2.75)","2.66 (min 2.64, max 2.67)","1.86 (min 1.69, max 1.92)","4.55 (min 3.87, max 4.83)","4.74 (min 4.39, max 4.88)"
    "4m-cmykw2 (workloads/)","309.51 (min 308.17, max 311.04)","313.24 (min 310.08, max 314.96)","309.61 (min 306.28, max 311.53)","241.60 (min 232.83, max 247.83)","593.12 (min 584.80, max 604.23)","593.94 (min 576.37, max 600.60)"
    "4m-cmykw2-rotatew2 (workloads/)","58.71 (min 57.20, max 59.76)","62.90 (min 62.44, max 63.63)","59.30 (min 59.11, max 59.46)","49.00 (min 48.39, max 49.71)","71.23 (min 67.64, max 72.29)","47.88 (min 42.40, max 54.60)"
    "4m-reassembly (workloads/)","103.14 (min 100.60, max 107.07)","126.59 (min 122.55, max 129.03)","122.81 (min 120.77, max 125.31)","81.45 (min 78.80, max 90.17)","129.73 (min 122.40, max 143.06)","130.75 (min 125.63, max 138.70)"
    "4m-rotatew2 (workloads/)","69.24 (min 68.68, max 69.83)","73.01 (min 72.57, max 73.64)","69.07 (min 68.59, max 69.44)","52.63 (min 52.22, max 53.68)","77.38 (min 76.57, max 77.94)","52.74 (min 47.73, max 61.05)"
    "4m-tcp-mixed (workloads/)","259.07 (min 250.00, max 266.67)","266.81 (min 253.97, max 275.86)","257.67 (min 246.15, max 266.67)","116.37 (min 115.11, max 117.65)","262.91 (min 258.07, max 271.19)","251.17 (min 238.81, max 262.30)"
    "4m-x264w2 (workloads/)","2.73 (min 2.71, max 2.74)","2.75 (min 2.66, max 2.80)","2.71 (min 2.69, max 2.74)","1.96 (min 1.93, max 1.98)","4.86 (min 3.99, max 5.07)","4.91 (min 4.14, max 5.07)"
    "idct-4m (workloads/)","34.89 (min 34.79, max 34.92)","35.03 (min 34.99, max 35.06)","34.87 (min 34.75, max 34.94)","19.15 (min 19.14, max 19.16)","35.04 (min 34.93, max 35.10)","35.08 (min 34.90, max 35.12)"
    "idct-4mw1 (workloads/)","34.88 (min 34.73, max 34.93)","35.04 (min 35.00, max 35.06)","34.92 (min 34.89, max 34.97)","19.15 (min 19.14, max 19.17)","35.06 (min 34.92, max 35.12)","35.08 (min 34.93, max 35.12)"
    "ippktcheck-4m (workloads/)","821.00 (min 799.49, max 854.41)","824.59 (min 815.40, max 850.92)","786.35 (min 768.52, max 815.40)","398.44 (min 390.56, max 412.68)","1114.25 (min 1097.45, max 1122.59)","988.74 (min 967.87, max 1000.80)"
    "ippktcheck-4mw1 (workloads/)","818.36 (min 796.94, max 848.03)","828.79 (min 814.07, max 851.79)","784.47 (min 766.87, max 825.08)","399.14 (min 393.70, max 413.84)","1119.39 (min 1115.08, max 1123.09)","988.83 (min 967.87, max 997.21)"
    "ipres-4m (workloads/)","153.34 (min 150.00, max 158.40)","179.46 (min 177.73, max 181.38)","163.38 (min 159.92, max 170.07)","106.08 (min 103.95, max 110.70)","182.55 (min 170.46, max 196.85)","179.01 (min 173.21, max 183.37)"
    "ipres-4mw1 (workloads/)","152.88 (min 149.25, max 157.40)","180.17 (min 177.73, max 182.70)","163.11 (min 160.77, max 168.16)","106.26 (min 104.02, max 110.54)","181.52 (min 169.68, max 200.54)","178.72 (min 174.42, max 182.04)"
    "md5-4m (workloads/)","43.18 (min 42.50, max 43.59)","46.31 (min 45.66, max 46.66)","42.96 (min 42.50, max 43.29)","27.33 (min 26.93, max 27.87)","47.23 (min 46.58, max 47.69)","44.63 (min 44.44, max 44.88)"
    "md5-4mw1 (workloads/)","43.41 (min 43.05, max 43.78)","46.47 (min 45.83, max 46.82)","43.21 (min 42.92, max 43.50)","27.44 (min 26.98, max 27.82)","47.18 (min 46.79, max 47.64)","44.67 (min 44.29, max 45.05)"
    "rgbcmyk-4m (workloads/)","162.67 (min 160.26, max 163.27)","163.57 (min 163.40, max 163.80)","162.39 (min 159.87, max 162.87)","64.72 (min 62.38, max 65.53)","163.72 (min 163.40, max 164.07)","163.70 (min 163.27, max 163.93)"
    "rgbcmyk-4mw1 (workloads/)","162.68 (min 161.42, max 163.13)","162.70 (min 160.13, max 163.67)","162.75 (min 162.60, max 162.87)","64.67 (min 62.29, max 65.49)","163.67 (min 163.40, max 163.93)","162.95 (min 160.64, max 164.07)"
    "rotate-4ms1 (workloads/)","50.89 (min 50.10, max 51.28)","54.05 (min 53.76, max 54.53)","50.91 (min 50.20, max 51.18)","23.06 (min 22.76, max 23.70)","53.29 (min 52.74, max 54.11)","53.11 (min 52.47, max 53.42)"
    "rotate-4ms1w1 (workloads/)","50.95 (min 50.51, max 51.60)","54.02 (min 53.76, max 54.23)","50.75 (min 50.15, max 51.12)","23.07 (min 22.80, max 23.70)","53.40 (min 52.85, max 54.17)","53.25 (min 53.02, max 53.48)"
    "rotate-4ms64 (workloads/)","52.58 (min 52.03, max 53.02)","55.48 (min 55.19, max 55.80)","52.43 (min 52.14, max 52.74)","23.34 (min 22.98, max 23.93)","54.70 (min 53.71, max 55.49)","54.79 (min 54.64, max 55.49)"
    "rotate-4ms64w1 (workloads/)","52.75 (min 51.76, max 53.76)","55.27 (min 55.13, max 55.49)","52.13 (min 51.98, max 52.30)","23.27 (min 23.00, max 23.89)","54.75 (min 54.23, max 55.43)","54.65 (min 53.94, max 54.82)"
    "x264-4mq (workloads/)","1.42 (min 1.41, max 1.43)","1.43 (min 1.43, max 1.44)","1.42 (min 1.41, max 1.42)","0.58 (min 0.57, max 0.58)","1.41 (min 1.26, max 1.44)","1.42 (min 1.38, max 1.44)"
    "x264-4mqw1 (workloads/)","1.42 (min 1.42, max 1.43)","1.42 (min 1.30, max 1.44)","1.42 (min 1.41, max 1.43)","0.58 (min 0.57, max 0.58)","1.43 (min 1.40, max 1.45)","1.40 (min 1.27, max 1.43)"



 
 


Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","j7200-evm: Boot time in seconds: avg(min,max)","j721e-idk-gw: Boot time in seconds: avg(min,max)","j721s2-evm: Boot time in seconds: avg(min,max)","j722s_evm-fs: Boot time in seconds: avg(min,max)","j742s2_evm-fs: Boot time in seconds: avg(min,max)","j784s4-evm: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","19.45 (min 18.86, max 23.17)","22.68 (min 21.82, max 25.00)","19.03 (min 16.76, max 20.80)","22.25 (min 20.63, max 35.01)","19.66 (min 18.68, max 23.96)","20.40 (min 19.16, max 31.50)"

 

 

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.
 



|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","j721e-idk-gw: Throughput (bits/sec)","j721e-idk-gw: CPU Load (%)","j721s2-evm: Throughput (bits/sec)","j721s2-evm: CPU Load (%)","j784s4-evm: Throughput (bits/sec)","j784s4-evm: CPU Load (%)"

    "11025","352792.13 (min 352791.00, max 352794.00)","0.24 (min 0.19, max 0.35)","1023977.75 (min 1023976.00, max 1023980.00)","0.58 (min 0.40, max 0.69)","1023977.25 (min 1023968.00, max 1023994.00)","0.13 (min 0.06, max 0.35)"
    "16000","511990.75 (min 511988.00, max 511992.00)","0.37 (min 0.31, max 0.47)","1023987.38 (min 1023986.00, max 1023989.00)","0.92 (min 0.83, max 1.07)","1023987.25 (min 1023982.00, max 1023998.00)","0.18 (min 0.06, max 0.25)"
    "22050","705574.38 (min 705572.00, max 705577.00)","0.35 (min 0.29, max 0.43)","1023974.13 (min 1023966.00, max 1023993.00)","0.53 (min 0.40, max 0.78)","1023963.75 (min 1023957.00, max 1023969.00)","0.14 (min 0.11, max 0.16)"
    "24000","705581.88 (min 705580.00, max 705583.00)","0.36 (min 0.32, max 0.45)","1023984.88 (min 1023982.00, max 1023993.00)","0.63 (min 0.39, max 0.76)","1023981.13 (min 1023978.00, max 1023985.00)","0.14 (min 0.13, max 0.17)"
    "32000","1023978.88 (min 1023976.00, max 1023981.00)","0.26 (min 0.21, max 0.36)","1023985.00 (min 1023983.00, max 1023989.00)","0.71 (min 0.45, max 0.84)","1023983.25 (min 1023978.00, max 1023989.00)","0.15 (min 0.11, max 0.17)"
    "44100","1411173.00 (min 1411169.00, max 1411176.00)","0.59 (min 0.53, max 0.70)","1417785.25 (min 1417761.00, max 1417795.00)","0.71 (min 0.61, max 0.74)","1417790.50 (min 1417784.00, max 1417801.00)","0.15 (min 0.14, max 0.17)"
    "48000","1535972.00 (min 1535968.00, max 1535975.00)","0.77 (min 0.69, max 0.92)","1535950.00 (min 1535934.00, max 1535956.00)","0.71 (min 0.61, max 0.78)","1535953.00 (min 1535948.00, max 1535963.00)","0.16 (min 0.13, max 0.18)"
    "88200","2822347.00 (min 2822340.00, max 2822352.00)","1.11 (min 1.03, max 1.25)","2835611.75 (min 2835593.00, max 2835619.00)","1.27 (min 1.20, max 1.31)","2835615.13 (min 2835607.00, max 2835632.00)","0.30 (min 0.27, max 0.34)"
    "96000","3071943.00 (min 3071936.00, max 3071949.00)","0.57 (min 0.50, max 0.67)","3071920.38 (min 3071905.00, max 3071926.00)","1.30 (min 1.14, max 1.40)","3071922.75 (min 3071914.00, max 3071941.00)","0.31 (min 0.27, max 0.37)"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","j721e-idk-gw: Throughput (bits/sec)","j721e-idk-gw: CPU Load (%)","j721s2-evm: Throughput (bits/sec)","j721s2-evm: CPU Load (%)","j784s4-evm: Throughput (bits/sec)","j784s4-evm: CPU Load (%)"

    "11025","352937.25 (min 352936.00, max 352938.00)","0.22 (min 0.18, max 0.27)","1024399.29 (min 1024389.00, max 1024404.00)","0.47 (min 0.34, max 0.60)","1024399.50 (min 1024396.00, max 1024403.00)","0.12 (min 0.07, max 0.22)"
    "16000","512202.38 (min 512201.00, max 512203.00)","0.32 (min 0.18, max 0.38)","1024409.14 (min 1024403.00, max 1024412.00)","0.62 (min 0.37, max 0.76)","1024409.00 (min 1024406.00, max 1024411.00)","0.12 (min 0.07, max 0.19)"
    "22050","705866.13 (min 705862.00, max 705869.00)","0.33 (min 0.30, max 0.40)","1024388.00 (min 1024370.00, max 1024393.00)","0.59 (min 0.45, max 0.79)","1024386.00 (min 1024381.00, max 1024392.00)","0.13 (min 0.10, max 0.17)"
    "24000","705873.25 (min 705871.00, max 705875.00)","0.34 (min 0.30, max 0.41)","1024403.86 (min 1024395.00, max 1024406.00)","0.50 (min 0.26, max 0.77)","1024403.00 (min 1024401.00, max 1024406.00)","0.13 (min 0.07, max 0.16)"
    "32000","1024401.50 (min 1024399.00, max 1024404.00)","0.45 (min 0.23, max 0.56)","1024405.29 (min 1024396.00, max 1024408.00)","0.55 (min 0.25, max 0.81)","1024406.25 (min 1024401.00, max 1024410.00)","0.13 (min 0.06, max 0.19)"
    "44100","1411755.38 (min 1411752.00, max 1411758.00)","0.56 (min 0.51, max 0.61)","1418375.00 (min 1418348.00, max 1418383.00)","0.60 (min 0.54, max 0.72)","1418372.75 (min 1418368.00, max 1418382.00)","0.15 (min 0.14, max 0.18)"
    "48000","1536605.50 (min 1536602.00, max 1536608.00)","0.63 (min 0.36, max 0.77)","1536586.00 (min 1536563.00, max 1536593.00)","0.66 (min 0.57, max 0.77)","1536584.63 (min 1536581.00, max 1536593.00)","0.17 (min 0.14, max 0.23)"
    "88200","2823511.25 (min 2823504.00, max 2823516.00)","1.07 (min 1.00, max 1.15)","2836784.00 (min 2836748.00, max 2836794.00)","1.17 (min 1.09, max 1.31)","2836782.25 (min 2836776.00, max 2836795.00)","0.29 (min 0.27, max 0.34)"
    "96000","3073210.00 (min 3073203.00, max 3073215.00)","1.26 (min 0.52, max 1.43)","3073189.00 (min 3073154.00, max 3073198.00)","1.20 (min 0.98, max 1.38)","3073187.25 (min 3073181.00, max 3073200.00)","0.29 (min 0.16, max 0.38)"

 
 



 



|

Graphics SGX/RGX Driver
-------------------------
 


GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","j721e-idk-gw: Score","j721e-idk-gw: Fps","j721s2-evm: Score","j721s2-evm: Fps","j742s2_evm-fs: Score","j742s2_evm-fs: Fps","j784s4-evm: Score","j784s4-evm: Fps"

    " GFXBench 3.x gl_manhattan_off","1205.06 (min 1195.13, max 1216.61)","19.44 (min 19.28, max 19.62)","946.11 (min 941.45, max 956.89)","15.26 (min 15.18, max 15.43)","923.01 (min 872.62, max 956.67)","14.89 (min 14.07, max 15.43)","895.57 (min 881.47, max 927.40)","14.44 (min 14.22, max 14.96)"
    " GFXBench 3.x gl_trex_off","1839.33 (min 1829.10, max 1851.00)","32.85 (min 32.66, max 33.05)","1607.29 (min 1589.89, max 1641.00)","28.70 (min 28.39, max 29.30)","1504.12 (min 1422.88, max 1587.93)","26.86 (min 25.41, max 28.36)","1487.15 (min 1436.41, max 1534.72)","26.56 (min 25.65, max 27.41)"
    " GFXBench 4.x gl_4_off","410.57 (min 408.75, max 412.86)","6.95 (min 6.92, max 6.99)","260.88 (min 259.76, max 263.93)","4.41 (min 4.40, max 4.47)","256.97 (min 250.94, max 262.40)","4.35 (min 4.25, max 4.44)","253.25 (min 251.00, max 255.97)","4.29 (min 4.25, max 4.33)"
    " GFXBench 5.x gl_5_high_off","178.46 (min 177.63, max 179.44)","2.78 (min 2.76, max 2.79)","114.14 (min 113.66, max 114.94)","1.78 (min 1.77, max 1.79)","112.72 (min 111.27, max 113.82)","1.75 (min 1.73, max 1.77)","111.13 (min 110.50, max 111.97)","1.73 (min 1.72, max 1.74)"




Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","j721e-idk-gw: Score","j721s2-evm: Score","j722s_evm-fs: Score","j742s2_evm-fs: Score","j784s4-evm: Score"

    "Glmark2-DRM","47.88 (min 47.00, max 48.00)","116.50 (min 110.00, max 141.00)","286.25 (min 285.00, max 287.00)","124.80 (min 102.00, max 142.00)","166.50 (min 163.00, max 171.00)"
    "Glmark2-Wayland","1121.25 (min 1112.00, max 1134.00)","1258.11 (min 1207.00, max 1415.00)","787.00 (min 740.00, max 802.00)","1289.11 (min 1213.00, max 1364.00)","1274.90 (min 1257.00, max 1306.00)"
    "Glmark2-Wayland 4000x4000","81.63 (min 75.00, max 85.00)","79.00 (min 77.00, max 83.00)","83.88 (min 83.00, max 88.00)"

 
 

 

 



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
    :header: "Command Used","j7200-evm: THROUGHPUT (Mbits/sec)","j7200-evm: CPU Load % (LOCAL_CPU_UTIL)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j721s2-evm: THROUGHPUT (Mbits/sec)","j721s2-evm: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","998.00 (min 0.00, max 1863.42)","91.51 (min 79.94, max 98.40)","1838.18 (min 1819.73, max 1854.28)","85.99 (min 79.11, max 91.76)","1391.04 (min 0.00, max 1863.91)","87.20 (min 75.63, max 99.23)","1349.43 (min 821.14, max 1858.02)","49.37 (min 34.00, max 66.05)","1825.53 (min 1812.01, max 1852.44)","59.77 (min 55.30, max 62.83)","1772.83 (min 1670.23, max 1852.12)","27.59 (min 25.24, max 29.09)"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1843.80 (min 1808.69, max 1871.44)","44.86 (min 32.62, max 50.47)","1293.42 (min 838.70, max 1858.49)","35.97 (min 31.92, max 40.01)","1788.32 (min 1691.27, max 1854.90)","49.05 (min 19.83, max 63.85)","1773.21 (min 1645.58, max 1876.06)","17.87 (min 11.98, max 27.89)"




.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: Packets Per Second (kPPS)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","60.09 (min 0.00, max 93.69)","117.38 (min 0.00, max 183.00)","65.43 (min 15.03, max 84.28)","","56.70 (min 54.36, max 59.25)","110.75 (min 106.00, max 116.00)","31.03 (min 25.28, max 40.20)","","79.79 (min 78.33, max 83.28)","155.86 (min 153.00, max 163.00)","43.69 (min 43.24, max 44.62)","","82.80 (min 76.53, max 91.75)","161.63 (min 149.00, max 179.00)","22.29 (min 21.07, max 23.24)"
    "128","","96.18 (min 0.00, max 190.73)","93.88 (min 0.00, max 186.00)","54.12 (min 7.30, max 85.10)","","103.69 (min 49.66, max 116.67)","101.11 (min 48.00, max 114.00)","30.96 (min 17.06, max 39.64)","","162.64 (min 157.88, max 168.06)","158.86 (min 154.00, max 164.00)","44.43 (min 43.90, max 45.16)","","164.67 (min 155.27, max 179.60)","160.75 (min 152.00, max 175.00)","22.40 (min 21.27, max 23.09)"
    "256","","215.25 (min 19.25, max 378.61)","105.11 (min 9.00, max 185.00)","49.14 (min 1.91, max 85.39)","","222.26 (min 211.61, max 232.25)","108.33 (min 103.00, max 113.00)","25.87 (min 25.26, max 26.19)","","323.22 (min 312.05, max 339.52)","157.86 (min 152.00, max 166.00)","44.18 (min 43.52, max 45.36)","","317.27 (min 303.77, max 341.23)","154.88 (min 148.00, max 167.00)","22.24 (min 21.23, max 22.75)"
    "1024","","703.17 (min 0.00, max 938.57)","86.00 (min 0.00, max 115.00)","62.62 (min 60.53, max 64.41)","","608.41 (min 104.85, max 844.00)","74.43 (min 13.00, max 103.00)","28.09 (min 2.08, max 40.04)","","817.10 (min 521.23, max 936.51)","99.57 (min 64.00, max 114.00)","29.89 (min 18.81, max 35.64)","","936.46 (min 933.55, max 939.05)","114.25 (min 114.00, max 115.00)","17.14 (min 16.08, max 18.02)"
    "1518","","920.79 (min 918.51, max 923.68)","76.00","56.15 (min 54.25, max 58.04)","","764.91 (min 559.32, max 836.04)","63.11 (min 46.00, max 69.00)","27.04 (min 21.61, max 36.67)","","893.93 (min 704.20, max 924.22)","73.75 (min 58.00, max 76.00)","30.84 (min 28.97, max 31.86)","","922.24 (min 920.21, max 924.32)","76.00","15.04 (min 13.31, max 16.28)"




.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","2.11 (min 2.00, max 2.25)","4.00","2.41 (min 1.57, max 3.39)","","2.12 (min 1.48, max 3.53)","4.25 (min 3.00, max 7.00)","0.57 (min 0.30, max 0.83)","","5.00 (min 1.43, max 12.75)","9.86 (min 3.00, max 25.00)","1.17 (min 0.13, max 3.36)"
    "128","","15.00 (min 5.12, max 50.36)","14.50 (min 5.00, max 49.00)","12.11 (min 2.21, max 41.46)","","5.25 (min 4.40, max 9.32)","5.25 (min 4.00, max 9.00)","0.98 (min 0.47, max 1.81)","","8.12 (min 4.71, max 11.88)","8.00 (min 5.00, max 12.00)","0.52 (min 0.32, max 0.77)"
    "256","","11.00 (min 10.24, max 12.08)","5.29 (min 5.00, max 6.00)","3.33 (min 2.33, max 4.70)","","16.49 (min 10.65, max 22.32)","8.00 (min 5.00, max 11.00)","0.73 (min 0.56, max 0.90)","","17.25 (min 9.62, max 46.49)","8.50 (min 5.00, max 23.00)","0.82 (min 0.32, max 2.36)"
    "1024","","47.28 (min 42.60, max 59.80)","5.71 (min 5.00, max 7.00)","5.08 (min 2.39, max 8.37)","","28.01 (min 11.28, max 43.42)","3.25 (min 1.00, max 5.00)","1.75 (min 0.38, max 3.26)","","259.83 (min 42.60, max 620.99)","31.63 (min 5.00, max 76.00)","6.36 (min 0.58, max 15.89)"
    "1518","","667.79 (min 280.25, max 956.63)","56.78 (min 24.00, max 81.00)","51.86 (min 21.17, max 77.55)","","566.25 (min 73.01, max 924.89)","48.17 (min 6.00, max 79.00)","20.70 (min 2.24, max 33.28)","","734.95 (min 560.95, max 910.42)","62.38 (min 48.00, max 77.00)","13.76 (min 10.24, max 16.81)"




.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j721e-idk-gw: Packet Loss %","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: Packet Loss %","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: Packet Loss %"

    "64","","66.40 (min 64.43, max 67.90)","129.80 (min 126.00, max 133.00)","81.10 (min 79.73, max 83.94)","2.91 (min 2.01, max 4.24)","","175.47 (min 150.06, max 197.41)","342.75 (min 293.00, max 386.00)","43.53 (min 40.30, max 44.95)","39.78 (min 6.41, max 61.49)","","167.87 (min 151.89, max 183.75)","328.00 (min 297.00, max 359.00)","22.80 (min 21.14, max 23.60)","23.39 (min 5.49, max 38.34)"
    "128","","132.68 (min 129.10, max 137.61)","129.38 (min 126.00, max 134.00)","80.34 (min 78.95, max 81.86)","2.72 (min 2.13, max 3.26)","","318.32 (min 289.57, max 386.60)","311.00 (min 283.00, max 378.00)","43.94 (min 42.84, max 45.07)","39.70 (min 22.05, max 49.78)","","335.42 (min 300.02, max 380.98)","327.50 (min 293.00, max 372.00)","22.83 (min 21.46, max 23.62)","22.41 (min 1.03, max 36.60)"
    "256","","265.30 (min 252.98, max 278.13)","129.71 (min 124.00, max 136.00)","80.31 (min 77.46, max 82.07)","2.79 (min 1.65, max 3.91)","","649.68 (min 588.86, max 710.50)","317.50 (min 288.00, max 347.00)","43.23 (min 42.62, max 43.84)","9.98 (min 3.43, max 16.53)","","522.54 (min 414.43, max 683.72)","255.00 (min 202.00, max 334.00)","19.55 (min 16.72, max 23.19)","4.38 (min 0.15, max 11.66)"
    "1024","","879.78 (min 847.74, max 907.63)","107.43 (min 103.00, max 111.00)","81.45 (min 79.01, max 83.50)","3.45 (min 2.21, max 5.04)","","785.54 (min 638.87, max 892.35)","96.00 (min 78.00, max 109.00)","34.19 (min 28.62, max 38.36)","0.31 (min 0.07, max 0.45)","","795.18 (min 615.56, max 933.25)","97.13 (min 75.00, max 114.00)","17.90 (min 15.51, max 20.08)","0.30 (min 0.00, max 0.68)"
    "1518","","945.93 (min 905.41, max 956.74)","80.22 (min 77.00, max 81.00)","76.29 (min 72.25, max 78.28)","0.04 (min 0.01, max 0.10)","","832.55 (min 584.30, max 924.89)","70.83 (min 50.00, max 79.00)","31.04 (min 21.31, max 35.50)","0.05 (min 0.00, max 0.18)","","775.25 (min 603.79, max 910.42)","65.75 (min 51.00, max 77.00)","14.55 (min 11.32, max 16.81)","0.00 (min 0.00, max 0.01)"

 
 

 

 
 



|

PCIe Driver
-------------------------


 


PCIe-NVMe-SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^
 

 

 


.. rubric:: J721E-IDK-GW
   :name: j721e-idk-gw-pciessd




.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","721.88 (min 719.00, max 727.00)","14.00 (min 13.81, max 14.20)","1513.88 (min 1512.00, max 1516.00)","8.12 (min 7.75, max 8.34)"
    "4m","721.38 (min 718.00, max 724.00)","12.28 (min 12.07, max 12.42)","1417.13 (min 741.00, max 1515.00)","5.03 (min 2.70, max 5.57)"
    "4k","173.13 (min 172.00, max 176.00)","48.76 (min 48.42, max 48.99)","123.25 (min 44.80, max 158.00)","28.72 (min 12.89, max 37.04)"
    "256k","728.63 (min 720.00, max 746.00)","15.88 (min 15.48, max 16.36)","1349.88 (min 752.00, max 1512.00)","14.32 (min 7.12, max 15.66)"



- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based 
- Platform: Speed 8GT/s, Width x2
- SSD being used: PLEXTOR PX-128M8PeY
 



.. rubric:: J721S2-EVM
   :name: j721s2-evm-pciessd




.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","731.00","17.03 (min 16.83, max 17.25)","770.33 (min 770.00, max 771.00)","4.55 (min 4.24, max 4.82)"
    "4m","732.00","13.96 (min 13.87, max 14.08)","771.67 (min 771.00, max 772.00)","3.67 (min 3.55, max 3.83)"
    "4k","173.00 (min 171.00, max 174.00)","50.53 (min 50.50, max 50.56)","269.00 (min 264.00, max 272.00)","50.49 (min 50.47, max 50.50)"
    "256k","749.00","17.26 (min 16.93, max 17.59)","786.00","8.43 (min 8.38, max 8.48)"



- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based 
- Platform: Speed 8GT/s, Width x2
- SSD being used: PLEXTOR PX-128M8PeY
 

 

 

 
 

 



|

Linux OSPI Flash Driver
-------------------------

 

 

 

 

 


 


 


.. rubric:: J7200-EVM
   :name: j7200-evm-ospi


.. rubric:: UBIFS
   :name: j7200-evm-ospi-ubifs


.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j7200-evm: Write UBIFS Throughput (Mbytes/sec)","j7200-evm: Write UBIFS CPU Load (%)","j7200-evm: Read UBIFS Throughput (Mbytes/sec)","j7200-evm: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.29)","50.37 (min 49.55, max 51.29)","77.72 (min 76.59, max 78.73)","34.00 (min 25.00, max 40.00)"
    "262144","0.14 (min 0.10, max 0.19)","50.41 (min 49.90, max 50.81)","76.32 (min 75.68, max 77.17)","29.67 (min 25.00, max 40.00)"
    "524288","0.14 (min 0.10, max 0.19)","50.39 (min 50.02, max 51.26)","75.53 (min 74.84, max 76.62)","31.00 (min 25.00, max 40.00)"
    "1048576","0.14 (min 0.10, max 0.19)","50.49 (min 49.87, max 51.42)","73.97 (min 73.43, max 74.81)","35.17 (min 25.00, max 40.00)"




.. rubric:: RAW
   :name: j7200-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j7200-evm: Raw Read Throughput (Mbytes/sec)"

    "50","232.68 (min 227.27, max 238.09)"

 
 


.. rubric:: J721E-IDK-GW
   :name: j721e-idk-gw-ospi


.. rubric:: UBIFS
   :name: j721e-idk-gw-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j721e-idk-gw: Write UBIFS Throughput (Mbytes/sec)","j721e-idk-gw: Write UBIFS CPU Load (%)","j721e-idk-gw: Read UBIFS Throughput (Mbytes/sec)","j721e-idk-gw: Read UBIFS CPU Load (%)"

    "102400","0.69 (min 0.52, max 1.34)","54.54 (min 48.04, max 62.95)","74.82 (min 31.50, max 84.65)","31.84 (min 7.69, max 50.00)"
    "262144","0.50 (min 0.37, max 0.57)","54.64 (min 49.81, max 66.46)","73.98 (min 31.04, max 83.61)","27.50 (min 8.33, max 40.00)"
    "524288","0.50 (min 0.37, max 0.57)","53.13 (min 49.62, max 59.51)","73.16 (min 31.12, max 82.77)","36.91 (min 14.29, max 57.14)"
    "1048576","0.50 (min 0.37, max 0.57)","53.12 (min 49.87, max 60.39)","71.55 (min 30.96, max 79.92)","35.44 (min 14.29, max 50.00)"




.. rubric:: RAW
   :name: j721e-idk-gw-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j721e-idk-gw: Raw Read Throughput (Mbytes/sec)"

    "50","197.43 (min 38.46, max 263.16)"

 
 

 


.. rubric:: J722S-EVM
   :name: j722s-evm-ospi


.. rubric:: UBIFS
   :name: j722s-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j722s_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Write UBIFS CPU Load (%)","j722s_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.28)","29.40 (min 24.89, max 37.67)","63.17 (min 55.35, max 64.95)","24.25 (min 8.33, max 53.85)"
    "262144","0.14 (min 0.10, max 0.19)","29.85 (min 26.26, max 33.57)","64.30 (min 62.76, max 65.47)","21.60 (min 8.33, max 28.57)"
    "524288","0.15 (min 0.11, max 0.19)","30.54 (min 26.04, max 37.28)","64.08 (min 62.63, max 65.20)","19.19 (min 9.09, max 26.67)"
    "1048576","0.15 (min 0.11, max 0.19)","29.99 (min 26.60, max 37.86)","62.55 (min 62.12, max 62.99)","22.64 (min 15.38, max 26.67)"




.. rubric:: RAW
   :name: j722s-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j722s_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","227.27"

 
 


.. rubric:: J742S2-EVM
   :name: j742s2-evm-ospi


.. rubric:: UBIFS
   :name: j742s2-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j742s2_evm-fs: Write UBIFS CPU Load (%)","j742s2_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j742s2_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.29)","27.59 (min 23.95, max 31.13)","71.98 (min 70.59, max 73.05)","22.19 (min 18.18, max 33.33)"
    "262144","0.14 (min 0.10, max 0.19)","27.42 (min 25.56, max 30.15)","72.23 (min 71.10, max 73.20)","15.89 (min 10.00, max 23.08)"
    "524288","0.14 (min 0.10, max 0.19)","27.87 (min 25.35, max 32.30)","70.69 (min 68.87, max 72.23)","20.67 (min 9.09, max 25.00)"
    "1048576","0.14 (min 0.10, max 0.19)","28.12 (min 25.74, max 31.37)","71.05 (min 70.21, max 73.09)","20.87 (min 16.67, max 25.00)"




.. rubric:: RAW
   :name: j742s2-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j742s2_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","240.50 (min 200.00, max 263.16)"

 
 


.. rubric:: J784S4-EVM
   :name: j784s4-evm-ospi


.. rubric:: UBIFS
   :name: j784s4-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j784s4-evm: Write UBIFS Throughput (Mbytes/sec)","j784s4-evm: Write UBIFS CPU Load (%)","j784s4-evm: Read UBIFS Throughput (Mbytes/sec)","j784s4-evm: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.12, max 0.29)","14.16 (min 12.31, max 17.10)","73.84 (min 69.78, max 77.96)","9.98 (min 4.35, max 15.38)"
    "262144","0.15 (min 0.10, max 0.19)","14.41 (min 13.09, max 17.06)","75.90 (min 71.36, max 79.25)","6.84 (min 4.35, max 12.00)"
    "524288","0.15 (min 0.10, max 0.19)","15.02 (min 12.78, max 17.29)","72.30 (min 70.05, max 78.65)","9.19 (min 4.35, max 13.04)"
    "1048576","0.15 (min 0.10, max 0.19)","14.76 (min 12.46, max 16.92)","73.31 (min 68.25, max 77.00)","7.65 (min 4.17, max 11.54)"




.. rubric:: RAW
   :name: j784s4-evm-ospi-raw


.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j784s4-evm: Raw Read Throughput (Mbytes/sec)"

    "50","234.11 (min 185.19, max 263.16)"

 
 

 

 
 

 



|

UBoot QSPI/OSPI Driver
-------------------------

 
















.. rubric:: J721E-IDK-GW
   :name: j721e-idk-gw-uboot-qspi

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","1029.58 (min 1018.15, max 1041.18)","15852.98 (min 15814.67, max 15875.97)"
    "800000","1030.49 (min 1019.03, max 1041.84)","16058.82 (min 16031.31, max 16062.75)"
    "1000000","1030.84 (min 1019.67, max 1042.37)","16167.76 (min 16157.79, max 16173.74)"
    "2000000","1030.82 (min 1019.83, max 1042.64)","16219.78 (min 16213.76, max 16221.78)"




.. rubric:: J721S2-EVM
   :name: j721s2-evm-uboot-qspi

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "400000","1000.03 (min 997.32, max 1002.69)","15852.98 (min 15814.67, max 15875.97)"
    "800000","1000.77 (min 998.17, max 1003.43)","16058.82 (min 16031.31, max 16062.75)"
    "1000000","1001.14 (min 998.72, max 1003.74)","16165.77 (min 16157.79, max 16173.74)"
    "2000000","1001.40 (min 999.79, max 1003.61)","16219.78 (min 16213.76, max 16221.78)"






.. rubric:: J742S2-EVM
   :name: j742s2-evm-uboot-qspi

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","982.25 (min 977.80, max 1000.49)","15845.32 (min 15814.67, max 15875.97)"
    "800000","982.72 (min 977.92, max 1001.47)","16054.89 (min 16031.31, max 16062.75)"
    "1000000","983.06 (min 978.38, max 1001.71)","16159.78 (min 16157.79, max 16173.74)"
    "2000000","983.26 (min 978.65, max 1002.17)","16219.78 (min 16213.76, max 16221.78)"




.. rubric:: J784S4-EVM
   :name: j784s4-evm-uboot-qspi

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","991.19 (min 982.73, max 1003.18)","15822.33 (min 15814.67, max 15875.97)"
    "800000","992.17 (min 983.08, max 1004.17)","16058.82 (min 16031.31, max 16062.75)"
    "1000000","992.50 (min 983.49, max 1004.29)","16165.77 (min 16157.79, max 16173.74)"
    "2000000","992.47 (min 983.32, max 1003.92)","16220.78 (min 16213.76, max 16221.78)"















 
 

 

 



|

UBoot UFS Driver
-------------------------




.. rubric:: J721E-IDK-GW
   :name: j721e-idk-gw-uboot-ufs-raw

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","109624.57 (min 73142.86, max 215578.95)","363497.84 (min 341333.33, max 372363.64)"
    "800000","113881.29 (min 97523.81, max 195047.62)","507697.48 (min 481882.35, max 512000.00)"
    "1000000","118730.24 (min 93622.86, max 234057.14)","623752.28 (min 606814.81, max 655360.00)"






.. rubric:: J742S2-EVM
   :name: j742s2-evm-uboot-ufs-raw

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","91493.35 (min 75851.85, max 97523.81)","366157.58 (min 341333.33, max 372363.64)"
    "800000","98038.67 (min 88086.02, max 102400.00)","512000.00"
    "1000000","101478.74 (min 95812.87, max 104356.69)","611482.62 (min 606814.81, max 630153.85)"

 


.. rubric:: J784S4-EVM
   :name: j784s4-evm-emmc-raw

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","90391.67 (min 87148.94, max 93090.91)","367191.92 (min 341333.33, max 372363.64)"
    "800000","98172.76 (min 88086.02, max 102400.00)","501960.78 (min 481882.35, max 512000.00)"
    "1000000","98645.38 (min 94160.92, max 103696.20)","622374.17 (min 606814.81, max 630153.85)"

 

 



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

    "1m","55.16 (min 45.00, max 60.80)","1.65 (min 1.28, max 1.92)","311.44 (min 306.00, max 315.00)","1.95 (min 1.81, max 2.10)"
    "4m","55.08 (min 44.90, max 61.00)","1.41 (min 1.21, max 1.63)","309.00 (min 303.00, max 314.00)","1.23 (min 1.05, max 1.40)"
    "4k","39.34 (min 5.31, max 58.10)","17.80 (min 2.74, max 26.71)","49.51 (min 36.10, max 56.40)","18.57 (min 13.68, max 21.18)"
    "256k","52.21 (min 36.10, max 60.80)","1.84 (min 1.22, max 2.26)","306.11 (min 288.00, max 317.00)","3.81 (min 3.59, max 4.00)"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","60.01 (min 58.40, max 61.00)","1.49 (min 1.40, max 1.65)","175.00","1.30 (min 1.22, max 1.53)"
    "4m","59.81 (min 57.80, max 61.20)","1.31 (min 1.16, max 1.61)","175.00","0.85 (min 0.72, max 1.08)"
    "4k","50.40 (min 50.10, max 50.60)","21.84 (min 21.53, max 22.07)","56.34 (min 56.00, max 56.90)","20.47 (min 19.98, max 20.72)"
    "256k","60.19 (min 58.70, max 61.20)","2.01 (min 1.89, max 2.22)","174.00","2.35 (min 2.17, max 2.59)"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","68.40 (min 45.00, max 96.70)","2.06 (min 1.44, max 2.75)","300.38 (min 287.00, max 313.00)","2.02 (min 1.92, max 2.06)"
    "4m","68.63 (min 45.30, max 97.10)","1.54 (min 1.19, max 2.07)","271.13 (min 165.00, max 313.00)","1.20 (min 0.93, max 1.44)"
    "4k","47.68 (min 5.22, max 82.60)","22.69 (min 2.76, max 39.71)","62.68 (min 36.20, max 93.50)","24.85 (min 14.71, max 36.58)"
    "256k","65.11 (min 36.20, max 96.70)","2.36 (min 1.50, max 3.28)","293.88 (min 283.00, max 311.00)","3.84 (min 3.64, max 4.03)"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

    "1m","92.44 (min 78.00, max 97.60)","1.77 (min 1.41, max 1.97)","249.25 (min 113.00, max 295.00)","2.63 (min 1.36, max 3.19)"
    "4m","92.78 (min 78.40, max 98.10)","1.27 (min 1.05, max 1.41)","244.75 (min 112.00, max 295.00)","2.05 (min 1.15, max 2.43)"
    "4k","65.04 (min 8.57, max 83.90)","20.27 (min 3.20, max 26.11)","81.38 (min 56.60, max 90.90)","19.27 (min 14.57, max 21.33)"
    "256k","90.13 (min 68.70, max 97.60)","2.13 (min 1.69, max 2.35)","243.33 (min 94.80, max 295.00)","3.71 (min 1.51, max 4.50)"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Write EXT4 CPU Load (%)","j742s2_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Read EXT4 CPU Load (%)"

    "1m","96.92 (min 95.90, max 98.00)","0.99 (min 0.94, max 1.05)","288.40 (min 280.00, max 293.00)","0.84 (min 0.80, max 0.89)"
    "4m","96.46 (min 93.10, max 98.50)","0.99 (min 0.92, max 1.10)","292.20 (min 290.00, max 293.00)","0.49 (min 0.44, max 0.51)"
    "4k","83.06 (min 82.70, max 84.30)","21.28 (min 20.90, max 21.93)","81.32 (min 77.00, max 87.30)","16.17 (min 14.86, max 17.86)"
    "256k","96.92 (min 95.90, max 98.10)","1.07 (min 1.01, max 1.17)","292.80 (min 292.00, max 294.00)","1.89 (min 1.81, max 2.03)"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

    "1m","94.23 (min 80.00, max 97.20)","0.48 (min 0.45, max 0.50)","268.75 (min 114.00, max 294.00)","0.43 (min 0.22, max 0.52)"
    "4m","94.74 (min 80.60, max 97.70)","0.45 (min 0.40, max 0.48)","232.34 (min 96.70, max 294.00)","0.22 (min 0.15, max 0.29)"
    "4k","73.72 (min 8.65, max 83.20)","10.37 (min 1.32, max 12.08)","87.91 (min 56.60, max 94.10)","9.43 (min 5.85, max 10.35)"
    "256k","93.10 (min 71.00, max 97.20)","0.59 (min 0.43, max 0.71)","268.48 (min 94.80, max 294.00)","0.99 (min 0.33, max 1.28)"

 

 

 

 

 

 

 
 


EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "1m","53.26 (min 45.00, max 60.50)","1.51 (min 1.24, max 1.93)","310.67 (min 305.00, max 315.00)","1.90 (min 1.64, max 2.07)"
    "4m","52.88 (min 44.90, max 60.60)","1.31 (min 1.08, max 1.59)","286.78 (min 245.00, max 314.00)","1.12 (min 1.00, max 1.31)"
    "4k","32.83 (min 5.30, max 55.10)","11.65 (min 2.05, max 19.52)","47.34 (min 36.00, max 56.30)","16.29 (min 12.56, max 19.50)"
    "256k","49.50 (min 36.10, max 60.60)","1.61 (min 1.22, max 2.10)","302.89 (min 288.00, max 316.00)","3.63 (min 3.36, max 3.92)"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "1m","58.30 (min 43.80, max 61.30)","1.42 (min 1.11, max 1.58)","175.00","1.24 (min 1.15, max 1.38)"
    "4m","58.39 (min 44.20, max 61.60)","1.19 (min 0.90, max 1.44)","175.00","0.80 (min 0.70, max 0.93)"
    "4k","46.86 (min 5.47, max 53.10)","16.27 (min 2.14, max 18.44)","53.91 (min 36.00, max 56.90)","17.90 (min 12.04, max 19.25)"
    "256k","57.20 (min 34.70, max 61.10)","1.71 (min 1.24, max 1.95)","174.00","2.19 (min 2.05, max 2.33)"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "1m","55.07 (min 45.10, max 61.10)","1.63 (min 1.35, max 1.78)","309.89 (min 301.00, max 314.00)","1.95 (min 1.81, max 2.13)"
    "4m","55.12 (min 45.20, max 61.20)","1.31 (min 1.04, max 1.48)","303.33 (min 281.00, max 314.00)","1.21 (min 1.09, max 1.29)"
    "4k","38.61 (min 5.22, max 55.70)","14.76 (min 2.33, max 21.55)","49.42 (min 36.20, max 56.20)","18.17 (min 13.37, max 21.01)"
    "256k","52.00 (min 36.30, max 60.90)","1.88 (min 1.40, max 2.19)","302.67 (min 284.00, max 314.00)","3.72 (min 3.52, max 3.82)"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "1m","92.61 (min 78.00, max 97.80)","1.59 (min 1.28, max 1.76)","249.63 (min 112.00, max 296.00)","2.68 (min 1.43, max 3.31)"
    "4m","92.95 (min 78.20, max 98.30)","1.20 (min 1.01, max 1.36)","243.03 (min 95.20, max 296.00)","2.00 (min 1.05, max 2.41)"
    "4k","63.92 (min 8.58, max 82.70)","15.11 (min 2.45, max 19.51)","84.58 (min 56.60, max 94.30)","18.90 (min 13.54, max 20.92)"
    "256k","89.08 (min 68.60, max 97.80)","1.92 (min 1.30, max 2.17)","245.33 (min 94.30, max 296.00)","3.53 (min 1.67, max 4.34)"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "1m","92.45 (min 77.60, max 97.50)","0.91 (min 0.73, max 1.02)","271.63 (min 112.00, max 295.00)","0.79 (min 0.38, max 0.87)"
    "4m","93.88 (min 79.40, max 97.80)","0.94 (min 0.76, max 1.03)","243.75 (min 112.00, max 295.00)","0.44 (min 0.23, max 0.54)"
    "4k","70.47 (min 7.73, max 83.40)","14.40 (min 1.67, max 17.12)","87.04 (min 59.00, max 93.10)","16.53 (min 11.69, max 17.70)"
    "256k","88.93 (min 68.60, max 97.60)","0.92 (min 0.75, max 1.01)","269.29 (min 94.30, max 295.00)","1.63 (min 0.66, max 1.81)"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "1m","92.71 (min 79.00, max 98.00)","0.45 (min 0.37, max 0.50)","271.38 (min 112.00, max 296.00)","0.41 (min 0.19, max 0.56)"
    "4m","94.26 (min 71.40, max 98.50)","0.43 (min 0.38, max 0.48)","249.00 (min 111.00, max 296.00)","0.24 (min 0.13, max 0.30)"
    "4k","72.47 (min 6.13, max 83.20)","7.33 (min 0.61, max 9.02)","89.00 (min 66.80, max 93.70)","8.63 (min 6.89, max 9.31)"
    "256k","92.29 (min 69.50, max 98.00)","0.49 (min 0.45, max 0.53)","270.19 (min 94.50, max 296.00)","0.87 (min 0.34, max 1.09)"

 

 

 

 

 

 

 
 

 

 

 

 

 
 



UBoot EMMC Driver
-----------------

 

 

 

 

 

 

 

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

    "2000000","59999.37 (min 59041.44, max 61248.60)","306102.84 (min 292571.43, max 312076.19)"
    "4000000","60700.91 (min 59959.74, max 61651.93)","312540.24 (min 304818.60, max 321254.90)"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "2000000","60320.39 (min 59254.97, max 60907.06)","173772.30 (min 173375.66, max 175229.95)"
    "4000000","60971.47 (min 59959.74, max 62060.61)","177674.40 (min 177124.32, max 178572.21)"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "2000000","59628.83 (min 57893.99, max 61478.42)","308668.65 (min 303407.41, max 312076.19)"
    "4000000","60385.87 (min 59362.32, max 61478.42)","317192.67 (min 310597.16, max 322837.44)"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j722s_evm-fs: Write Throughput (Kbytes/sec)","j722s_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","97386.23 (min 93622.86, max 103044.03)","162812.24 (min 95255.81, max 172463.16)"
    "4000000","98138.10 (min 95812.87, max 100669.74)","169164.36 (min 123886.58, max 175699.73)"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","99089.53 (min 96376.47, max 104025.40)","248190.19 (min 99598.78, max 284939.13)"
    "4000000","98434.29 (min 96803.55, max 100361.41)","259806.28 (min 145635.56, max 292571.43)"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "2000000","95710.54 (min 93356.13, max 98698.80)","278630.50 (min 258015.75, max 289982.30)"
    "4000000","97951.00 (min 95953.15, max 100979.97)","281882.18 (min 235741.01, max 295207.21)"

 

 

 

 

 

 

 
 

 


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
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","33.84 (min 32.60, max 34.60)","1.16 (min 1.08, max 1.22)","43.31 (min 42.30, max 43.50)","0.67 (min 0.62, max 0.75)"
    "4m","33.31 (min 32.10, max 34.20)","0.90 (min 0.84, max 0.98)","43.28 (min 42.20, max 43.50)","0.55 (min 0.49, max 0.70)"
    "4k","2.77 (min 2.75, max 2.80)","2.10 (min 1.97, max 2.23)","11.23 (min 11.20, max 11.30)","5.30 (min 5.18, max 5.47)"
    "256k","31.59 (min 30.60, max 32.60)","1.37 (min 1.22, max 1.51)","42.55 (min 42.40, max 42.90)","0.90 (min 0.82, max 0.97)"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write EXT4 Throughput (Mbytes/sec)","j7200-evm: Write EXT4 CPU Load (%)","j7200-evm: Read EXT4 Throughput (Mbytes/sec)","j7200-evm: Read EXT4 CPU Load (%)"

    "1m","42.74 (min 41.20, max 43.40)","1.52 (min 1.46, max 1.61)","87.04 (min 85.10, max 87.50)","1.07 (min 0.94, max 1.20)"
    "4m","42.10 (min 40.80, max 43.10)","1.25 (min 1.18, max 1.33)","86.89 (min 84.90, max 87.40)","0.74 (min 0.67, max 0.82)"
    "4k","2.80 (min 2.77, max 2.82)","2.31 (min 2.19, max 2.41)","12.89 (min 12.80, max 13.00)","6.33 (min 6.15, max 6.54)"
    "256k","38.34 (min 36.80, max 40.00)","1.67 (min 1.59, max 1.90)","83.69 (min 83.40, max 84.30)","1.45 (min 1.39, max 1.53)"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","42.63 (min 42.00, max 43.10)","1.65 (min 1.56, max 1.74)","87.64 (min 87.20, max 88.20)","1.20 (min 1.05, max 1.41)"
    "4m","41.63 (min 40.20, max 42.80)","1.26 (min 1.17, max 1.50)","85.33 (min 82.10, max 87.30)","0.81 (min 0.72, max 0.96)"
    "4k","2.80 (min 2.79, max 2.83)","2.51 (min 2.39, max 2.63)","12.90 (min 12.80, max 13.00)","7.02 (min 6.78, max 7.18)"
    "256k","38.48 (min 37.20, max 40.50)","1.84 (min 1.72, max 1.93)","83.94 (min 83.20, max 84.50)","1.56 (min 1.45, max 1.85)"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

    "1m","41.85 (min 41.20, max 42.60)","1.30 (min 1.24, max 1.38)","87.03 (min 85.10, max 87.40)","1.55 (min 1.45, max 1.62)"
    "4m","42.14 (min 40.80, max 43.10)","0.92 (min 0.86, max 1.01)","86.95 (min 85.00, max 87.40)","1.15 (min 1.11, max 1.25)"
    "4k","2.78 (min 2.77, max 2.80)","1.94 (min 1.88, max 2.07)","12.96 (min 12.90, max 13.10)","4.53 (min 4.35, max 4.79)"
    "256k","37.63 (min 36.70, max 38.90)","1.50 (min 1.38, max 1.60)","83.68 (min 83.40, max 84.30)","1.76 (min 1.70, max 1.84)"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Write EXT4 CPU Load (%)","j742s2_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Read EXT4 CPU Load (%)"

    "1m","42.40 (min 41.50, max 42.80)","0.64 (min 0.58, max 0.69)","87.35 (min 87.30, max 87.50)","0.49 (min 0.44, max 0.55)"
    "4m","41.98 (min 41.30, max 42.70)","0.58 (min 0.51, max 0.64)","87.26 (min 87.10, max 87.40)","0.33 (min 0.30, max 0.35)"
    "4k","2.77 (min 2.75, max 2.78)","1.38 (min 1.31, max 1.44)","12.89 (min 12.80, max 13.00)","4.14 (min 4.03, max 4.24)"
    "256k","36.51 (min 35.90, max 37.20)","0.63 (min 0.60, max 0.67)","83.63 (min 83.40, max 84.00)","0.74 (min 0.71, max 0.77)"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

    "1m","42.36 (min 41.30, max 43.60)","0.31 (min 0.26, max 0.34)","87.40 (min 87.10, max 88.20)","0.26 (min 0.23, max 0.31)"
    "4m","42.44 (min 41.50, max 43.00)","0.28 (min 0.25, max 0.33)","86.68 (min 82.80, max 87.50)","0.17 (min 0.14, max 0.21)"
    "4k","2.79 (min 2.77, max 2.82)","0.62 (min 0.57, max 0.71)","12.93 (min 12.80, max 13.10)","1.74 (min 1.65, max 1.83)"
    "256k","37.73 (min 36.00, max 41.60)","0.32 (min 0.30, max 0.36)","83.60 (min 83.30, max 84.50)","0.35 (min 0.33, max 0.38)"

 

 

 

 

 

 

 

 

 
 


MMC RAW FIO 1G
^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "1m","43.55 (min 42.40, max 45.30)","1.36 (min 1.31, max 1.40)","88.18 (min 88.10, max 88.30)","0.92 (min 0.87, max 0.96)"
    "4m","43.26 (min 41.30, max 45.30)","1.21 (min 1.08, max 1.32)","88.11 (min 88.00, max 88.30)","0.70 (min 0.61, max 0.77)"
    "4k","2.82 (min 2.82, max 2.83)","1.98 (min 1.93, max 2.03)","13.00","6.10 (min 5.93, max 6.28)"
    "256k","37.94 (min 36.30, max 41.40)","1.49 (min 1.39, max 1.57)","84.35 (min 84.20, max 84.50)","1.41 (min 1.38, max 1.46)"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "1m","34.64 (min 33.00, max 36.50)","1.04 (min 0.96, max 1.16)","43.85 (min 43.80, max 43.90)","0.65 (min 0.56, max 0.79)"
    "4m","33.90 (min 32.50, max 35.40)","0.91 (min 0.80, max 0.97)","43.81 (min 43.80, max 43.90)","0.51 (min 0.46, max 0.62)"
    "4k","2.79 (min 2.77, max 2.80)","1.89 (min 1.77, max 2.03)","11.30","5.00 (min 4.85, max 5.20)"
    "256k","32.28 (min 29.80, max 35.00)","1.22 (min 1.08, max 1.33)","42.90","0.87 (min 0.80, max 0.96)"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "1m","43.57 (min 42.40, max 45.00)","1.62 (min 1.47, max 1.80)","88.21 (min 88.10, max 88.30)","1.08 (min 1.06, max 1.14)"
    "4m","43.16 (min 41.60, max 45.00)","1.26 (min 1.17, max 1.38)","88.20 (min 88.00, max 88.30)","0.81 (min 0.75, max 0.87)"
    "4k","2.82 (min 2.81, max 2.82)","2.25 (min 2.10, max 2.42)","13.03 (min 13.00, max 13.10)","6.62 (min 6.38, max 6.78)"
    "256k","38.49 (min 36.20, max 41.40)","1.72 (min 1.67, max 1.82)","84.39 (min 84.20, max 84.50)","1.52 (min 1.45, max 1.58)"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "1m","43.44 (min 42.00, max 45.00)","1.13 (min 1.07, max 1.23)","88.18 (min 88.10, max 88.30)","1.44 (min 1.37, max 1.52)"
    "4m","43.23 (min 41.20, max 45.10)","0.92 (min 0.81, max 0.96)","88.14 (min 88.00, max 88.30)","1.13 (min 1.03, max 1.25)"
    "4k","2.81 (min 2.80, max 2.82)","1.61 (min 1.54, max 1.71)","13.03 (min 13.00, max 13.10)","4.23 (min 4.08, max 4.33)"
    "256k","38.09 (min 36.10, max 41.30)","1.27 (min 1.15, max 1.37)","84.39 (min 84.30, max 84.50)","1.74 (min 1.67, max 1.80)"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "1m","43.34 (min 42.60, max 44.70)","0.58 (min 0.54, max 0.64)","88.20 (min 88.10, max 88.30)","0.42 (min 0.36, max 0.45)"
    "4m","42.97 (min 42.00, max 44.50)","0.58 (min 0.54, max 0.61)","88.16 (min 88.00, max 88.30)","0.32 (min 0.30, max 0.35)"
    "4k","2.80 (min 2.79, max 2.80)","1.26 (min 1.18, max 1.31)","13.04 (min 13.00, max 13.10)","3.96 (min 3.80, max 4.08)"
    "256k","37.73 (min 36.40, max 41.20)","0.60 (min 0.52, max 0.66)","84.36 (min 84.20, max 84.50)","0.72 (min 0.68, max 0.75)"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "1m","43.76 (min 42.60, max 45.30)","0.28 (min 0.25, max 0.32)","88.26 (min 88.20, max 88.30)","0.22 (min 0.18, max 0.25)"
    "4m","43.69 (min 42.50, max 45.30)","0.28 (min 0.26, max 0.32)","88.21 (min 88.00, max 88.30)","0.17 (min 0.14, max 0.21)"
    "4k","2.82 (min 2.81, max 2.83)","0.54 (min 0.49, max 0.60)","13.05 (min 13.00, max 13.10)","1.72 (min 1.62, max 1.79)"
    "256k","38.71 (min 36.40, max 41.60)","0.31 (min 0.25, max 0.36)","84.45 (min 84.30, max 84.50)","0.33 (min 0.31, max 0.35)"

 

 

 
 


MMC EXT4
^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "102400","37.09 (min 33.75, max 41.38)","3.07 (min 2.33, max 4.56)","75.87 (min 72.19, max 81.41)","4.89 (min 4.61, max 5.54)"
    "262144","38.23 (min 35.48, max 42.02)","3.29 (min 2.47, max 4.96)","82.90 (min 77.77, max 87.12)","4.92 (min 3.42, max 6.57)"
    "524288","39.52 (min 37.42, max 42.85)","3.17 (min 2.57, max 4.66)","90.87 (min 89.43, max 91.30)","5.16 (min 4.37, max 5.66)"
    "1048576","38.12 (min 36.81, max 40.88)","3.07 (min 2.34, max 4.36)","90.89 (min 89.06, max 91.32)","5.33 (min 4.81, max 5.86)"
    "5242880","38.59 (min 36.47, max 41.60)","3.02 (min 2.44, max 4.46)","90.94 (min 89.07, max 91.36)","5.10 (min 4.81, max 5.43)"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "102400","31.14 (min 27.78, max 35.13)","2.86 (min 2.26, max 4.12)","40.29 (min 39.22, max 43.16)","2.30 (min 1.86, max 2.65)"
    "262144","30.71 (min 27.95, max 34.09)","2.89 (min 2.26, max 4.10)","41.76 (min 39.84, max 42.62)","2.22 (min 1.91, max 2.63)"
    "524288","31.34 (min 29.12, max 35.00)","2.88 (min 2.20, max 4.17)","45.32 (min 42.37, max 45.84)","2.52 (min 2.19, max 2.84)"
    "1048576","31.96 (min 30.01, max 34.83)","2.78 (min 2.17, max 4.40)","45.82 (min 45.73, max 45.87)","2.71 (min 2.20, max 3.06)"
    "5242880","31.78 (min 29.27, max 34.68)","2.76 (min 2.06, max 4.17)","45.79 (min 45.65, max 45.89)","2.71 (min 2.21, max 3.06)"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "102400","38.87 (min 35.91, max 44.59)","3.62 (min 2.89, max 5.62)","77.50 (min 70.58, max 81.72)","4.54 (min 3.40, max 5.38)"
    "262144","38.65 (min 35.36, max 41.91)","3.74 (min 3.01, max 5.13)","83.01 (min 78.74, max 88.29)","4.90 (min 3.79, max 5.46)"
    "524288","38.96 (min 36.26, max 42.36)","3.72 (min 2.73, max 6.29)","89.02 (min 81.29, max 92.09)","5.52 (min 4.31, max 6.09)"
    "1048576","40.14 (min 36.84, max 42.72)","3.77 (min 2.76, max 5.57)","90.27 (min 82.14, max 92.05)","6.07 (min 5.29, max 6.93)"
    "5242880","39.59 (min 37.79, max 42.44)","3.72 (min 2.93, max 5.54)","91.49 (min 90.08, max 92.01)","6.33 (min 5.70, max 6.96)"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "102400","38.35 (min 34.70, max 44.04)","3.52 (min 2.69, max 4.94)","76.63 (min 71.25, max 81.41)","4.72 (min 3.54, max 6.02)"
    "262144","38.52 (min 36.19, max 41.90)","3.68 (min 2.61, max 5.44)","83.69 (min 80.79, max 88.28)","5.00 (min 4.58, max 5.46)"
    "524288","39.33 (min 36.94, max 43.37)","3.50 (min 2.42, max 5.34)","91.27 (min 90.63, max 91.73)","5.62 (min 4.80, max 6.96)"
    "1048576","40.17 (min 36.76, max 42.90)","3.55 (min 2.57, max 5.31)","91.43 (min 90.12, max 91.91)","5.41 (min 4.35, max 6.11)"
    "5242880","39.63 (min 36.81, max 43.79)","3.47 (min 2.57, max 5.36)","91.61 (min 91.13, max 91.90)","5.36 (min 4.82, max 6.55)"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "102400","38.86 (min 35.67, max 42.47)","0.95 (min 0.64, max 1.33)","76.18 (min 72.42, max 81.38)","1.18 (min 0.96, max 1.45)"
    "262144","37.80 (min 35.83, max 41.50)","0.88 (min 0.59, max 1.29)","83.03 (min 80.55, max 87.89)","1.05 (min 0.87, max 1.26)"
    "524288","40.07 (min 37.38, max 43.31)","0.93 (min 0.71, max 1.58)","91.74 (min 89.90, max 92.25)","1.16 (min 0.75, max 1.64)"
    "1048576","39.51 (min 36.46, max 43.38)","0.88 (min 0.63, max 1.42)","90.99 (min 89.94, max 92.18)","1.17 (min 0.98, max 1.52)"
    "5242880","39.21 (min 37.47, max 42.22)","0.88 (min 0.63, max 1.37)","91.52 (min 90.88, max 92.14)","1.21 (min 1.08, max 1.32)"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "102400","38.51 (min 35.74, max 41.30)","1.75 (min 1.37, max 2.56)","76.18 (min 72.91, max 81.09)","2.33 (min 1.82, max 2.87)"
    "262144","38.24 (min 36.55, max 41.14)","1.82 (min 1.40, max 2.66)","83.73 (min 78.60, max 88.36)","2.19 (min 1.74, max 2.43)"
    "524288","39.62 (min 37.35, max 42.47)","1.81 (min 1.36, max 3.06)","91.20 (min 89.67, max 92.11)","2.30 (min 2.19, max 2.40)"
    "1048576","39.83 (min 36.97, max 42.88)","1.75 (min 1.31, max 2.52)","91.72 (min 90.95, max 92.07)","2.43 (min 1.98, max 3.04)"
    "5242880","39.20 (min 37.54, max 42.41)","1.70 (min 1.21, max 2.53)","91.77 (min 91.23, max 92.15)","2.53 (min 2.18, max 3.03)"

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 


MMC EXT2
^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "102400","39.86 (min 33.62, max 42.80)","3.74 (min 2.90, max 6.09)","79.10 (min 76.26, max 80.71)","5.21 (min 4.09, max 5.94)"
    "262144","38.20 (min 33.20, max 42.42)","3.53 (min 2.51, max 6.19)","84.73 (min 81.72, max 86.66)","5.64 (min 4.38, max 6.24)"
    "524288","36.81 (min 32.68, max 38.94)","3.33 (min 2.43, max 5.69)","88.37 (min 85.08, max 90.50)","5.41 (min 4.91, max 5.88)"
    "1048576","38.22 (min 32.93, max 41.90)","3.48 (min 2.63, max 6.11)","89.69 (min 84.98, max 90.43)","5.41 (min 4.97, max 5.62)"
    "5242880","37.86 (min 32.90, max 41.33)","3.40 (min 2.41, max 5.67)","89.65 (min 85.36, max 90.42)","5.44 (min 4.56, max 6.06)"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "102400","32.30 (min 28.11, max 35.02)","3.38 (min 2.37, max 6.06)","42.30 (min 41.71, max 43.00)","2.42 (min 2.00, max 3.06)"
    "262144","30.59 (min 28.64, max 34.31)","3.07 (min 2.21, max 6.02)","43.76 (min 43.35, max 44.81)","2.56 (min 2.28, max 2.99)"
    "524288","31.54 (min 28.27, max 34.34)","3.22 (min 2.36, max 5.85)","45.37 (min 44.35, max 45.73)","2.71 (min 2.54, max 3.05)"
    "1048576","30.21 (min 28.46, max 31.16)","2.98 (min 2.05, max 5.36)","45.01 (min 44.30, max 45.72)","2.84 (min 2.61, max 3.05)"
    "5242880","31.49 (min 27.53, max 34.74)","3.12 (min 2.20, max 5.96)","45.18 (min 44.28, max 45.72)","2.78 (min 2.34, max 3.27)"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "102400","41.41 (min 37.48, max 43.97)","4.48 (min 3.39, max 7.54)","79.93 (min 76.25, max 81.14)","4.52 (min 3.15, max 5.41)"
    "262144","31.20 (min 3.93, max 39.91)","4.25 (min 2.94, max 5.46)","86.60 (min 81.79, max 88.10)","5.10 (min 4.42, max 5.83)"
    "524288","38.49 (min 35.14, max 43.70)","4.02 (min 2.77, max 7.29)","89.75 (min 85.18, max 91.38)","5.89 (min 4.80, max 7.36)"
    "1048576","39.25 (min 35.27, max 43.38)","4.18 (min 3.09, max 7.12)","90.57 (min 86.34, max 91.36)","6.20 (min 5.65, max 6.97)"
    "5242880","38.58 (min 35.82, max 42.54)","4.02 (min 2.90, max 7.43)","89.38 (min 86.35, max 91.44)","6.70 (min 6.01, max 8.15)"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "102400","39.14 (min 34.64, max 43.91)","4.15 (min 2.87, max 7.52)","79.77 (min 77.28, max 81.18)","5.66 (min 3.92, max 6.84)"
    "262144","38.37 (min 35.14, max 42.21)","3.94 (min 2.58, max 7.36)","87.59 (min 87.08, max 87.87)","5.70 (min 5.04, max 6.22)"
    "524288","37.97 (min 35.21, max 39.91)","3.84 (min 2.75, max 6.89)","90.36 (min 86.28, max 91.23)","5.24 (min 3.96, max 5.65)"
    "1048576","38.39 (min 34.94, max 42.59)","3.99 (min 2.78, max 7.31)","90.38 (min 86.24, max 91.30)","5.60 (min 4.80, max 6.03)"
    "5242880","38.59 (min 35.40, max 42.98)","4.01 (min 2.63, max 6.72)","91.21 (min 91.13, max 91.33)","5.73 (min 4.82, max 6.11)"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "102400","41.68 (min 37.59, max 43.88)","1.11 (min 0.80, max 1.91)","79.23 (min 76.52, max 81.19)","1.28 (min 1.02, max 1.48)"
    "262144","38.19 (min 35.04, max 41.23)","0.95 (min 0.65, max 1.75)","86.68 (min 83.19, max 87.83)","1.19 (min 1.04, max 1.36)"
    "524288","39.27 (min 35.30, max 42.90)","0.98 (min 0.64, max 1.76)","89.11 (min 86.08, max 91.55)","1.23 (min 0.98, max 1.55)"
    "1048576","38.70 (min 34.58, max 42.69)","0.97 (min 0.65, max 1.77)","90.32 (min 86.55, max 91.60)","1.24 (min 0.98, max 1.41)"
    "5242880","38.76 (min 35.20, max 43.10)","0.97 (min 0.65, max 1.90)","91.48 (min 90.99, max 91.62)","1.20 (min 0.88, max 1.41)"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "102400","39.49 (min 34.31, max 43.04)","2.08 (min 1.38, max 3.74)","80.22 (min 77.84, max 80.86)","2.59 (min 1.93, max 3.26)"
    "262144","38.94 (min 35.05, max 42.09)","2.01 (min 1.29, max 3.59)","86.32 (min 83.47, max 87.84)","2.13 (min 1.68, max 2.59)"
    "524288","38.50 (min 35.22, max 42.90)","1.99 (min 1.29, max 3.83)","90.69 (min 86.80, max 91.56)","2.17 (min 1.75, max 2.62)"
    "1048576","39.40 (min 35.14, max 41.84)","1.96 (min 1.38, max 3.38)","89.42 (min 84.54, max 91.54)","2.51 (min 1.97, max 2.83)"
    "5242880","39.03 (min 35.29, max 42.54)","1.97 (min 1.31, max 3.55)","91.36 (min 90.99, max 91.58)","2.76 (min 2.19, max 3.26)"

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 



UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

    "400000","38506.35 (min 33851.24, max 52512.82)","83986.58 (min 81920.00, max 85333.33)"
    "800000","47895.80 (min 43574.47, max 62534.35)","88620.21 (min 87148.94, max 89043.48)"
    "1000000","48225.22 (min 42118.25, max 72176.21)","90799.33 (min 90021.98, max 91022.22)"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","25212.35 (min 17138.08, max 32000.00)","44166.51 (min 43574.47, max 44521.74)"
    "800000","27405.98 (min 19006.96, max 34565.40)","45575.73 (min 45259.67, max 45765.36)"
    "1000000","30465.63 (min 17945.24, max 36247.79)","46250.35 (min 46022.47, max 46413.60)"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "400000","32776.82 (min 26597.40, max 39384.62)","82755.92 (min 81920.00, max 83591.84)"
    "800000","38906.19 (min 28444.44, max 46282.49)","88086.02"
    "1000000","46602.38 (min 41062.66, max 48330.38)","90519.34"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j722s_evm-fs: Write Throughput (Kbytes/sec)","j722s_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","34065.44 (min 17429.79, max 39766.99)","82137.18 (min 80313.73, max 83591.84)"
    "800000","40119.81 (min 18492.10, max 47080.46)","87156.26 (min 85333.33, max 88086.02)"
    "1000000","43049.66 (min 19006.96, max 49951.22)","89655.03 (min 88562.16, max 90021.98)"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","34098.54 (min 27675.68, max 38641.51)","83591.84"
    "800000","39279.84 (min 30340.74, max 45765.36)","88086.02"
    "1000000","46020.87 (min 40857.86, max 49799.39)","90582.20 (min 90519.34, max 91022.22)"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","32525.83 (min 17808.70, max 39009.52)","82989.01 (min 78769.23, max 83591.84)"
    "800000","38362.25 (min 19883.50, max 45259.67)","87517.38 (min 84453.61, max 89043.48)"
    "1000000","41281.77 (min 21032.09, max 48473.37)","90460.58 (min 89043.48, max 91022.22)"

 

 

 

 

 

 

 

 

 
 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 



|

USB Driver
-------------------------
 


USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. csv-table:: USBDEVICE SUPERSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","j742s2_evm-fs: Throughput (MB/sec)"

    "150","43.60"





.. csv-table:: USBDEVICE SUPERSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","j742s2_evm-fs: Throughput (MB/sec)"

    "150","39.00"








.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721e-idk-gw: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

    "150","8.35 (min 8.10, max 8.60)","39.53 (min 27.30, max 44.50)","21.25 (min 14.00, max 35.40)","43.96 (min 43.30, max 44.40)","42.99 (min 39.80, max 44.30)"




.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721e-idk-gw: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

    "150","8.20 (min 7.90, max 8.70)","38.59 (min 29.80, max 42.60)","19.75 (min 13.80, max 31.80)","37.12 (min 35.20, max 39.60)","36.87 (min 34.90, max 38.60)"





 
 
 



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","j7200-evm: throughput (KBytes/Sec)","j721e-idk-gw: throughput (KBytes/Sec)","j721s2-evm: throughput (KBytes/Sec)","j722s_evm-fs: throughput (KBytes/Sec)","j742s2_evm-fs: throughput (KBytes/Sec)","j784s4-evm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","35727.51 (min 35073.37, max 36992.68)","42114.90 (min 41506.82, max 42864.98)","39992.96 (min 39447.21, max 41106.77)","23611.73 (min 22308.52, max 24363.69)","39296.77 (min 38829.74, max 40103.25)","37677.20 (min 34457.60, max 39562.92)"
    "aes-128-cbc","16","686.97 (min 671.97, max 700.82)","790.69 (min 777.45, max 807.01)","754.35 (min 738.54, max 766.07)","423.61 (min 403.10, max 433.58)","752.48 (min 738.50, max 769.47)","700.40 (min 632.01, max 751.85)"
    "aes-128-cbc","16384","178017.62 (min 173659.48, max 181638.49)","184707.07 (min 182015.32, max 186881.37)","178764.46 (min 176674.13, max 180202.15)","85368.83 (min 83197.95, max 86168.92)","176406.53 (min 173495.64, max 178820.44)","172770.06 (min 169077.42, max 179044.35)"
    "aes-128-cbc","256","10550.16 (min 10366.04, max 10944.26)","12276.20 (min 11976.45, max 12568.32)","11710.98 (min 11519.06, max 12030.89)","7015.48 (min 6523.65, max 7271.51)","11531.09 (min 11339.95, max 11806.12)","11164.18 (min 9981.78, max 11819.78)"
    "aes-128-cbc","64","2742.87 (min 2684.27, max 2798.12)","3165.00 (min 3101.74, max 3223.59)","3021.87 (min 2949.85, max 3081.56)","1835.98 (min 1697.60, max 1920.32)","2999.32 (min 2955.11, max 3042.33)","2691.39 (min 2335.81, max 3000.64)"
    "aes-128-cbc","8192","140595.35 (min 138720.60, max 144351.23)","150348.80 (min 149389.31, max 150872.06)","144029.35 (min 142188.54, max 145468.07)","71909.38 (min 69530.97, max 72764.07)","143014.91 (min 141765.29, max 144613.38)","136755.30 (min 129171.46, max 143461.03)"
    "aes-128-ecb","1024","35836.47 (min 35304.79, max 37184.17)","42752.77 (min 41944.75, max 43510.10)","40486.53 (min 39797.42, max 41387.69)","24146.35 (min 22734.85, max 24908.80)","39638.61 (min 39095.98, max 40328.19)","36998.34 (min 33961.30, max 40123.05)"
    "aes-128-ecb","16","693.14 (min 677.30, max 704.96)","800.57 (min 783.38, max 811.95)","766.51 (min 747.64, max 781.89)","435.16 (min 407.23, max 446.23)","753.95 (min 742.68, max 769.52)","689.09 (min 629.43, max 743.30)"
    "aes-128-ecb","16384","181100.24 (min 177356.80, max 186428.07)","192075.09 (min 189393.58, max 194144.94)","180625.41 (min 177504.26, max 182998.36)","87890.60 (min 86496.60, max 89112.58)","179684.01 (min 177586.18, max 181174.27)","175648.18 (min 166576.13, max 179847.17)"
    "aes-128-ecb","256","10660.34 (min 10408.45, max 10897.49)","12539.74 (min 12226.13, max 12750.93)","11866.76 (min 11708.33, max 12154.11)","7168.44 (min 6547.20, max 7422.46)","11695.66 (min 11456.77, max 11901.44)","10682.42 (min 8829.35, max 11813.55)"
    "aes-128-ecb","64","2768.82 (min 2697.86, max 2832.51)","3220.39 (min 3145.11, max 3261.01)","3050.55 (min 2965.27, max 3105.37)","1887.18 (min 1759.64, max 1970.97)","3004.47 (min 2949.08, max 3064.28)","2781.56 (min 2331.03, max 3029.14)"
    "aes-128-ecb","8192","142187.63 (min 140331.69, max 145855.83)","155060.91 (min 153624.58, max 156013.91)","146125.82 (min 144837.29, max 147939.33)","74279.25 (min 71783.77, max 75213.48)","144691.88 (min 143253.50, max 146462.04)","137479.31 (min 127079.77, max 144957.44)"
    "aes-192-cbc","1024","35597.35 (min 35112.62, max 36777.64)","41726.12 (min 41251.84, max 42334.21)","39779.03 (min 39279.27, max 40497.15)","23029.38 (min 21753.17, max 23803.56)","38854.06 (min 37802.33, max 40271.87)","38178.43 (min 36314.45, max 39482.03)"
    "aes-192-cbc","16","689.16 (min 679.02, max 702.90)","795.60 (min 781.25, max 809.09)","759.58 (min 744.14, max 772.33)","425.58 (min 403.40, max 438.95)","751.43 (min 744.68, max 760.97)","660.63 (min 564.79, max 754.39)"
    "aes-192-cbc","16384","173865.19 (min 169508.86, max 180071.08)","175461.72 (min 173670.40, max 177416.87)","170071.38 (min 167717.55, max 172365.14)","77385.05 (min 76283.90, max 78222.68)","167165.95 (min 162316.29, max 170775.89)","165573.58 (min 156336.13, max 170153.30)"
    "aes-192-cbc","256","10545.70 (min 10381.23, max 10911.91)","12333.48 (min 12103.51, max 12551.59)","11734.62 (min 11476.31, max 12014.34)","6970.19 (min 6517.93, max 7218.77)","11558.60 (min 11365.12, max 11818.24)","11011.82 (min 9846.61, max 11848.79)"
    "aes-192-cbc","64","2748.56 (min 2708.95, max 2809.92)","3174.57 (min 3101.74, max 3237.25)","3034.13 (min 2957.33, max 3095.02)","1833.43 (min 1695.85, max 1924.48)","2990.55 (min 2955.67, max 3043.22)","2771.58 (min 2554.82, max 2972.05)"
    "aes-192-cbc","8192","137890.78 (min 134662.83, max 142527.15)","144084.99 (min 142811.14, max 145626.45)","139079.34 (min 138346.50, max 139616.26)","66052.10 (min 64555.69, max 66898.60)","136897.54 (min 135113.39, max 138914.47)","133327.92 (min 123505.32, max 137663.83)"
    "aes-192-ecb","1024","35767.64 (min 35320.83, max 36727.47)","42346.97 (min 41308.84, max 43331.58)","40041.39 (min 39343.45, max 41065.81)","23671.25 (min 22367.57, max 24482.13)","39214.17 (min 38498.99, max 40249.00)","37586.99 (min 31919.45, max 40219.31)"
    "aes-192-ecb","16","691.89 (min 682.59, max 702.75)","800.74 (min 783.14, max 812.66)","762.73 (min 747.02, max 774.58)","433.96 (min 407.09, max 445.81)","752.96 (min 726.26, max 771.50)","731.67 (min 678.70, max 761.67)"
    "aes-192-ecb","16384","176097.66 (min 170748.59, max 180360.53)","180303.87 (min 177821.01, max 182255.62)","175385.94 (min 173533.87, max 177389.57)","79504.73 (min 77720.23, max 80336.21)","172735.15 (min 169989.46, max 175002.97)","172539.90 (min 170218.84, max 175041.19)"
    "aes-192-ecb","256","10642.27 (min 10476.20, max 10944.77)","12474.63 (min 12237.31, max 12749.74)","11823.67 (min 11592.02, max 12103.68)","7125.41 (min 6531.24, max 7358.72)","11629.64 (min 11329.45, max 11916.80)","11550.24 (min 11182.42, max 11879.00)"
    "aes-192-ecb","64","2766.32 (min 2701.76, max 2819.01)","3207.58 (min 3140.37, max 3256.87)","3037.70 (min 2967.08, max 3110.34)","1873.26 (min 1727.21, max 1941.65)","3005.23 (min 2912.00, max 3064.77)","2956.46 (min 2743.55, max 3046.95)"
    "aes-192-ecb","8192","139402.96 (min 137606.49, max 142950.40)","147585.37 (min 145582.76, max 149162.67)","142576.30 (min 140984.32, max 144588.80)","68180.31 (min 66385.24, max 68919.30)","140336.47 (min 139569.83, max 141978.28)","137560.06 (min 131642.71, max 140421.80)"
    "aes-256-cbc","1024","35435.52 (min 34948.10, max 36508.33)","41544.19 (min 40927.57, max 42143.06)","39405.74 (min 38410.24, max 40275.97)","22435.03 (min 21141.50, max 23027.37)","38908.50 (min 38364.50, max 39836.67)","38070.76 (min 37558.61, max 38445.06)"
    "aes-256-cbc","16","688.69 (min 674.54, max 705.27)","798.78 (min 785.02, max 810.83)","761.07 (min 746.78, max 774.37)","425.56 (min 402.01, max 436.08)","751.45 (min 737.77, max 771.93)","710.26 (min 578.46, max 759.69)"
    "aes-256-cbc","16384","170376.00 (min 168394.75, max 174243.84)","162663.77 (min 161437.01, max 163616.09)","158856.53 (min 157319.17, max 160437.59)","69935.10 (min 69058.56, max 71095.64)","156255.57 (min 152300.20, max 158821.03)","154323.24 (min 145315.16, max 158127.45)"
    "aes-256-cbc","256","10519.32 (min 10343.17, max 10931.97)","12286.81 (min 12073.39, max 12524.89)","11676.47 (min 11296.68, max 11915.26)","6909.42 (min 6486.10, max 7170.05)","11533.82 (min 11186.52, max 11859.97)","11127.16 (min 10543.70, max 11729.32)"
    "aes-256-cbc","64","2750.42 (min 2687.91, max 2825.81)","3183.13 (min 3136.21, max 3229.97)","3023.71 (min 2967.96, max 3082.26)","1830.20 (min 1679.91, max 1927.49)","3001.95 (min 2958.04, max 3079.02)","2937.82 (min 2709.72, max 3032.21)"
    "aes-256-cbc","8192","135707.46 (min 134575.45, max 139026.43)","135923.71 (min 134886.74, max 136724.48)","130899.29 (min 129826.82, max 132096.00)","60955.65 (min 59370.15, max 61906.94)","130092.71 (min 128535.21, max 132025.00)","125666.84 (min 119608.66, max 129348.95)"
    "aes-256-ecb","1024","35598.03 (min 34873.69, max 36583.77)","41961.26 (min 41353.22, max 42684.42)","39838.34 (min 39267.67, max 40973.99)","23055.32 (min 21734.06, max 23703.55)","39080.87 (min 38042.28, max 40186.20)","37473.57 (min 35075.75, max 39460.52)"
    "aes-256-ecb","16","690.74 (min 680.42, max 705.91)","802.37 (min 787.19, max 815.21)","766.07 (min 745.81, max 780.14)","433.76 (min 407.34, max 444.44)","756.82 (min 741.42, max 770.92)","670.05 (min 558.11, max 761.83)"
    "aes-256-ecb","16384","171765.00 (min 168028.84, max 176084.31)","168734.04 (min 167291.56, max 169579.86)","163293.18 (min 160552.28, max 165292.71)","72430.93 (min 70866.26, max 73045.33)","161574.23 (min 159094.10, max 164397.06)","160315.88 (min 156783.96, max 161884.84)"
    "aes-256-ecb","256","10562.24 (min 10340.10, max 10919.00)","12399.64 (min 12067.67, max 12651.43)","11793.44 (min 11458.39, max 12167.25)","7069.53 (min 6539.86, max 7290.97)","11582.84 (min 11133.27, max 11939.24)","11105.26 (min 9803.09, max 11794.26)"
    "aes-256-ecb","64","2756.40 (min 2725.16, max 2812.93)","3216.47 (min 3142.61, max 3260.84)","3051.03 (min 2965.63, max 3125.76)","1865.29 (min 1758.95, max 1940.03)","3026.50 (min 2952.96, max 3083.39)","2873.16 (min 2405.48, max 3048.06)"
    "aes-256-ecb","8192","137672.02 (min 135547.56, max 141301.08)","139441.83 (min 138158.08, max 139935.74)","134742.02 (min 133098.15, max 135905.28)","62757.89 (min 61115.05, max 63485.27)","133507.41 (min 131964.93, max 135839.74)","131084.09 (min 124106.07, max 133281.11)"
    "des3","1024","34389.98 (min 33894.40, max 35328.00)","36049.54 (min 35549.87, max 36675.24)","34722.99 (min 34237.78, max 35393.19)","","34389.76 (min 33932.63, max 34899.29)","33766.01 (min 30561.62, max 35017.39)"
    "des3","16","692.05 (min 682.38, max 703.85)","797.86 (min 780.10, max 814.60)","757.19 (min 737.33, max 769.32)","","752.37 (min 739.75, max 765.69)","703.88 (min 576.14, max 753.63)"
    "des3","16384","116578.23 (min 115403.43, max 117342.21)","94782.12 (min 94333.61, max 95240.19)","94033.92 (min 93164.89, max 94868.82)","","94044.16 (min 93082.97, max 94557.53)","93516.75 (min 92225.54, max 94382.76)"
    "des3","256","10328.30 (min 10125.06, max 10576.81)","11646.68 (min 11440.98, max 11923.03)","11045.12 (min 10853.03, max 11319.55)","","10947.98 (min 10873.69, max 11116.63)","10467.06 (min 9644.63, max 11026.94)"
    "des3","64","2757.13 (min 2706.45, max 2820.42)","3178.77 (min 3113.05, max 3239.85)","3024.04 (min 2945.13, max 3071.57)","","2991.21 (min 2950.83, max 3028.14)","2780.99 (min 2485.44, max 3003.99)"
    "des3","8192","99163.86 (min 97812.48, max 99745.79)","85861.72 (min 85445.29, max 86278.14)","83707.90 (min 82302.29, max 84161.88)","","84693.33 (min 84257.45, max 85128.53)","83594.68 (min 79233.02, max 84639.74)"
    "sha1","1024","69005.16 (min 66851.50, max 71213.40)","68041.30 (min 62956.20, max 71213.06)","68285.91 (min 64463.53, max 70482.60)","","67348.22 (min 65565.01, max 69054.81)","67106.38 (min 65459.54, max 68316.50)"
    "sha1","16","1153.89 (min 1103.37, max 1192.99)","1139.86 (min 1050.12, max 1197.12)","1140.58 (min 1087.91, max 1193.06)","","1125.20 (min 1077.95, max 1152.60)","1122.83 (min 1097.77, max 1147.10)"
    "sha1","16384","498890.98 (min 494944.26, max 506380.29)","497767.77 (min 480843.09, max 511093.42)","497000.45 (min 490897.41, max 504616.28)","","494477.99 (min 487582.38, max 500225.37)","493387.78 (min 487489.54, max 498614.27)"
    "sha1","256","18218.53 (min 17668.18, max 18733.31)","17948.64 (min 16475.56, max 18773.85)","18060.64 (min 17497.86, max 18694.06)","","17740.26 (min 17213.01, max 18151.85)","17626.92 (min 17220.18, max 18012.67)"
    "sha1","64","4597.50 (min 4378.47, max 4748.48)","4538.36 (min 4181.93, max 4768.51)","4572.32 (min 4402.03, max 4698.79)","","4488.39 (min 4345.22, max 4575.96)","4487.12 (min 4373.82, max 4561.11)"
    "sha1","8192","350964.09 (min 345961.81, max 360153.09)","346092.20 (min 331497.47, max 359328.43)","348478.12 (min 343911.08, max 357485.23)","","345389.06 (min 339626.67, max 348992.85)","346039.05 (min 338886.66, max 349989.55)"
    "sha256","1024","68645.28 (min 66090.67, max 70057.30)","67727.45 (min 63336.79, max 69632.68)","67941.42 (min 66660.01, max 69846.02)","37798.83 (min 37391.70, max 38389.76)","66286.17 (min 64538.62, max 67730.09)","66193.55 (min 65267.03, max 67617.11)"
    "sha256","16","1151.65 (min 1116.79, max 1176.56)","1142.17 (min 1070.15, max 1182.84)","1146.48 (min 1129.63, max 1168.89)","628.96 (min 622.82, max 634.84)","1122.80 (min 1087.47, max 1133.96)","1121.11 (min 1091.77, max 1144.18)"
    "sha256","16384","491281.52 (min 485064.70, max 497374.55)","492731.05 (min 482623.49, max 498363.05)","491547.31 (min 484223.66, max 498554.20)","299754.84 (min 297194.84, max 302661.63)","486320.81 (min 480231.42, max 494146.90)","483063.52 (min 475889.66, max 487800.83)"
    "sha256","256","18156.70 (min 17514.24, max 18640.90)","17877.27 (min 16698.97, max 18416.30)","18032.48 (min 17649.41, max 18549.85)","9891.39 (min 9715.71, max 10056.79)","17567.96 (min 17084.59, max 17872.98)","17604.80 (min 17219.93, max 17899.52)"
    "sha256","64","4595.42 (min 4421.82, max 4684.84)","4542.38 (min 4251.84, max 4686.70)","4577.52 (min 4487.98, max 4672.38)","2497.22 (min 2457.56, max 2533.16)","4451.73 (min 4280.30, max 4535.45)","4476.27 (min 4372.27, max 4552.51)"
    "sha256","8192","345888.69 (min 339326.29, max 355923.29)","345651.54 (min 334995.46, max 353689.60)","344452.78 (min 340639.74, max 348506.79)","202784.77 (min 200428.20, max 205138.60)","339995.31 (min 333441.71, max 343717.21)","338560.54 (min 333960.53, max 344298.84)"
    "sha512","1024","51820.28 (min 51040.60, max 52599.13)","51170.39 (min 49361.24, max 52461.91)","51176.75 (min 48561.49, max 52422.66)","26179.20 (min 25885.35, max 26348.20)","51297.32 (min 49816.58, max 52441.77)","50732.32 (min 49362.60, max 51585.71)"
    "sha512","16","1130.16 (min 1088.44, max 1175.50)","1128.65 (min 1076.06, max 1182.29)","1128.29 (min 1022.35, max 1169.29)","614.29 (min 608.94, max 621.75)","1124.88 (min 1066.50, max 1165.53)","1101.72 (min 1065.39, max 1129.10)"
    "sha512","16384","150462.16 (min 149099.86, max 151306.24)","150308.86 (min 149034.33, max 151328.09)","150155.26 (min 149045.25, max 151109.63)","68401.15 (min 68217.51, max 68556.12)","150100.65 (min 149083.48, max 151628.46)","149734.16 (min 148723.03, max 150487.04)"
    "sha512","256","16596.05 (min 16004.69, max 17169.75)","16403.77 (min 15655.59, max 17051.39)","16431.00 (min 15298.39, max 16899.24)","8744.11 (min 8657.75, max 8841.22)","16343.95 (min 15637.93, max 16732.25)","16215.16 (min 15814.06, max 16408.49)"
    "sha512","64","4553.02 (min 4405.10, max 4704.38)","4531.55 (min 4312.09, max 4712.85)","4537.90 (min 4147.65, max 4667.71)","2463.45 (min 2434.22, max 2504.26)","4532.33 (min 4264.92, max 4671.68)","4474.14 (min 4301.23, max 4597.95)"
    "sha512","8192","132883.04 (min 132180.65, max 133884.59)","132629.16 (min 131517.10, max 134026.58)","132714.15 (min 130722.47, max 134146.73)","61589.16 (min 61464.58, max 61707.61)","132666.37 (min 130902.70, max 134111.23)","132143.20 (min 131246.76, max 133477.72)"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","j7200-evm: CPU Load","j721e-idk-gw: CPU Load","j721s2-evm: CPU Load","j722s_evm-fs: CPU Load","j742s2_evm-fs: CPU Load","j784s4-evm: CPU Load"

    "aes-128-cbc","32.11 (min 31.00, max 33.00)","33.13 (min 33.00, max 34.00)","32.00 (min 31.00, max 33.00)","32.13 (min 31.00, max 33.00)","32.50 (min 32.00, max 33.00)","32.14 (min 31.00, max 33.00)"
    "aes-128-ecb","32.44 (min 32.00, max 33.00)","33.88 (min 33.00, max 35.00)","32.38 (min 32.00, max 33.00)","33.25 (min 32.00, max 34.00)","33.25 (min 32.00, max 34.00)","32.86 (min 32.00, max 34.00)"
    "aes-192-cbc","32.22 (min 32.00, max 33.00)","33.13 (min 33.00, max 34.00)","32.00 (min 31.00, max 33.00)","32.13 (min 30.00, max 33.00)","32.50 (min 32.00, max 33.00)","32.57 (min 32.00, max 33.00)"
    "aes-192-ecb","32.33 (min 32.00, max 33.00)","33.50 (min 33.00, max 34.00)","32.63 (min 32.00, max 33.00)","32.75 (min 31.00, max 34.00)","32.75 (min 32.00, max 33.00)","32.43 (min 32.00, max 33.00)"
    "aes-256-cbc","32.22 (min 32.00, max 33.00)","32.75 (min 32.00, max 34.00)","31.75 (min 31.00, max 32.00)","31.13 (min 29.00, max 32.00)","32.13 (min 31.00, max 33.00)","32.14 (min 31.00, max 33.00)"
    "aes-256-ecb","32.22 (min 32.00, max 33.00)","33.00 (min 32.00, max 34.00)","32.00 (min 31.00, max 33.00)","32.13 (min 31.00, max 33.00)","32.50 (min 32.00, max 33.00)","32.00 (min 31.00, max 33.00)"
    "des3","30.11 (min 29.00, max 31.00)","29.75 (min 29.00, max 31.00)","28.50 (min 28.00, max 29.00)","","29.38 (min 29.00, max 30.00)","29.14 (min 28.00, max 30.00)"
    "sha1","97.00","97.00","96.75 (min 96.00, max 97.00)","","97.00 (min 95.00, max 98.00)","96.86 (min 96.00, max 97.00)"
    "sha256","97.00","97.00","96.75 (min 96.00, max 97.00)","95.50 (min 94.00, max 96.00)","97.13 (min 97.00, max 98.00)","96.86 (min 96.00, max 97.00)"
    "sha512","97.00","97.00","96.38 (min 96.00, max 97.00)","94.88 (min 90.00, max 96.00)","96.88 (min 94.00, max 98.00)","96.86 (min 96.00, max 97.00)"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

 




IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","j721e-idk-gw: Throughput (Mbps)","j721e-idk-gw: Packets/Sec","j721e-idk-gw: CPU Load"

    "3des","183.85 (min 183.50, max 184.20)","16.00","39.65 (min 39.09, max 40.21)"
    "aes128","556.20 (min 192.90, max 693.30)","49.25 (min 17.00, max 61.00)","77.98 (min 58.66, max 99.82)"
    "aes192","676.30","60.00","59.36"
    "aes256","120.13 (min 0.10, max 309.80)","10.50 (min 0.00, max 27.00)","84.63 (min 64.27, max 98.15)"

