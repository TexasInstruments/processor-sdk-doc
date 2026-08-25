
################################
Linux 11.02.02 Performance Guide
################################

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
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
   :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

   "af_unix_sock_stream_latency (microsec)","20.02 (min 19.48, max 20.91)","20.59 (min 18.81, max 27.23)","20.25 (min 19.48, max 21.07)","30.14 (min 29.18, max 31.07)","20.75 (min 19.79, max 25.68)","23.85 (min 19.76, max 35.41)"
   "af_unix_socket_stream_bandwidth (mb\s)","1597.96 (min 1549.65, max 1692.82)","1883.71 (min 1783.01, max 1967.65)","1924.77 (min 1739.48, max 2088.48)","1083.90 (min 1046.92, max 1128.41)","2859.68 (min 2628.23, max 3095.23)","2457.51 (min 1610.12, max 3148.32)"
   "bw_file_rd-io-1mb (mb/s)","3579.94 (min 3321.03, max 3685.28)","3483.55 (min 3290.68, max 3636.36)","2967.94 (min 0.00, max 3527.66)","1361.63 (min 1303.36, max 1414.93)","4052.89 (min 3854.24, max 4393.19)","4059.62 (min 3844.04, max 4408.66)"
   "bw_file_rd-o2c-1mb (mb/s)","1350.26 (min 1165.50, max 1618.71)","1647.40 (min 1324.50, max 1843.47)","1365.80 (min 1081.67, max 1538.46)","742.38 (min 668.11, max 794.91)","2049.07 (min 1729.83, max 2330.17)","1865.36 (min 1485.61, max 2194.99)"
   "bw_mem-bcopy-16mb (mb/s)","2299.53 (min 2238.70, max 2369.32)","2742.51 (min 2613.52, max 2818.39)","3259.89 (min 2512.56, max 3787.88)","1753.52 (min 1587.93, max 1882.13)","3054.50 (min 2501.95, max 3676.89)","2923.40 (min 2610.97, max 3428.33)"
   "bw_mem-bcopy-1mb (mb/s)","3233.68 (min 3097.67, max 3390.44)","4617.75 (min 4052.15, max 5214.89)","4308.48 (min 3551.40, max 4804.14)","1925.44 (min 1835.24, max 2018.16)","9691.01 (min 8886.57, max 10054.14)","9642.98 (min 9102.73, max 10055.02)"
   "bw_mem-bcopy-2mb (mb/s)","2391.04 (min 2350.18, max 2478.75)","3759.58 (min 3462.00, max 3942.65)","3414.31 (min 2613.89, max 3985.65)","1658.95 (min 1592.99, max 1794.04)","4396.97 (min 3627.13, max 5076.14)","4221.81 (min 3481.62, max 5156.54)"
   "bw_mem-bcopy-4mb (mb/s)","2288.33 (min 2205.88, max 2362.67)","3642.24 (min 3258.92, max 3883.50)","3288.36 (min 2544.53, max 3822.87)","1680.66 (min 1475.47, max 1817.08)","3711.41 (min 3003.57, max 4682.93)","3445.72 (min 2694.51, max 4290.31)"
   "bw_mem-bcopy-8mb (mb/s)","2292.88 (min 2251.30, max 2367.21)","2966.74 (min 2767.21, max 3089.40)","3259.29 (min 2519.29, max 3788.48)","1721.51 (min 1478.74, max 1854.86)","3145.78 (min 2577.32, max 3769.44)","3068.94 (min 2646.38, max 3645.20)"
   "bw_mem-bzero-16mb (mb/s)","2271.49 (min 2233.70, max 2345.70)","9393.90 (min 8938.55, max 9658.92)","10379.47 (min 9632.75, max 10884.35)","7229.24 (min 7142.86, max 7323.77)","10016.49 (min 9501.19, max 10514.21)","10871.90 (min 10792.58, max 10912.19)"
   "bw_mem-bzero-1mb (mb/s)","3939.53 (min 3097.67, max 4877.10)","8446.62 (min 4052.15, max 12565.07)","8369.48 (min 3551.40, max 13105.92)","4573.50 (min 1835.24, max 7329.45)","11576.15 (min 8886.57, max 13681.37)","11695.91 (min 9102.73, max 13768.12)"
   "bw_mem-bzero-2mb (mb/s)","2610.59 (min 2350.18, max 2929.87)","7838.55 (min 3462.00, max 12234.62)","7252.56 (min 2613.89, max 11729.10)","4439.37 (min 1592.99, max 7318.35)","8660.05 (min 3627.13, max 13437.44)","8945.55 (min 3481.62, max 13715.94)"
   "bw_mem-bzero-4mb (mb/s)","2340.07 (min 2205.88, max 2471.04)","7641.42 (min 3258.92, max 11962.62)","6877.00 (min 2544.53, max 10972.93)","4451.07 (min 1475.47, max 7319.91)","7486.01 (min 3003.57, max 11799.41)","7873.72 (min 2694.51, max 12642.67)"
   "bw_mem-bzero-8mb (mb/s)","2287.54 (min 2241.84, max 2367.21)","7148.14 (min 2767.21, max 11736.66)","6828.35 (min 2519.29, max 10926.83)","4473.72 (min 1478.74, max 7326.01)","6718.45 (min 2577.32, max 10785.31)","7182.22 (min 2646.38, max 11339.48)"
   "bw_mem-cp-16mb (mb/s)","956.67 (min 940.35, max 988.94)","1489.59 (min 1380.50, max 1572.79)","2054.10 (min 1832.13, max 2186.69)","881.29 (min 843.57, max 918.38)","1942.74 (min 1832.34, max 2178.35)","2189.94 (min 2098.36, max 2305.48)"
   "bw_mem-cp-1mb (mb/s)","2952.46 (min 1181.63, max 4877.17)","6958.83 (min 1482.85, max 12614.89)","7358.81 (min 2051.09, max 13155.52)","4203.03 (min 833.75, max 7639.57)","8214.01 (min 2600.55, max 13678.91)","8401.02 (min 2701.73, max 13746.33)"
   "bw_mem-cp-2mb (mb/s)","1907.41 (min 960.15, max 2940.10)","6691.73 (min 1327.58, max 12219.23)","6558.05 (min 1857.01, max 11627.91)","4113.97 (min 818.55, max 7477.30)","7496.30 (min 1885.31, max 13306.96)","8059.82 (min 2241.79, max 13693.56)"
   "bw_mem-cp-4mb (mb/s)","1670.26 (min 918.17, max 2473.33)","6565.39 (min 1362.40, max 11964.85)","6243.66 (min 1804.24, max 10928.96)","4098.15 (min 850.07, max 7399.93)","6756.83 (min 2099.37, max 11795.32)","7413.35 (min 2295.77, max 12709.62)"
   "bw_mem-cp-8mb (mb/s)","1616.57 (min 927.75, max 2358.84)","6391.14 (min 1310.40, max 11734.51)","6219.45 (min 1825.86, max 10945.78)","4095.12 (min 868.34, max 7363.77)","6132.12 (min 1814.47, max 10788.94)","6771.26 (min 2141.04, max 11367.67)"
   "bw_mem-fcp-16mb (mb/s)","2358.32 (min 2323.89, max 2422.41)","2724.10 (min 2612.67, max 2789.40)","3225.69 (min 2480.62, max 3747.51)","1640.77 (min 1479.43, max 1748.44)","3033.91 (min 2479.08, max 3665.52)","2867.45 (min 2572.35, max 3421.36)"
   "bw_mem-fcp-1mb (mb/s)","3942.92 (min 3106.16, max 4877.10)","8046.68 (min 3493.29, max 12565.07)","8068.04 (min 3154.57, max 13105.92)","4439.68 (min 1587.02, max 7329.45)","10029.19 (min 6025.23, max 13681.37)","10175.02 (min 6253.55, max 13768.12)"
   "bw_mem-fcp-2mb (mb/s)","2648.48 (min 2406.26, max 2929.87)","7843.00 (min 3403.10, max 12234.62)","7068.79 (min 0.00, max 11729.10)","4391.89 (min 1448.44, max 7318.35)","8328.16 (min 3167.69, max 13437.44)","8610.90 (min 3185.35, max 13715.94)"
   "bw_mem-fcp-4mb (mb/s)","2364.45 (min 2277.04, max 2471.04)","7658.00 (min 3393.86, max 11962.62)","6865.92 (min 2505.09, max 10972.93)","4416.77 (min 1522.65, max 7319.91)","7398.88 (min 2853.58, max 11799.41)","7792.13 (min 2685.92, max 12642.67)"
   "bw_mem-fcp-8mb (mb/s)","2316.06 (min 2241.84, max 2411.82)","7148.56 (min 2783.09, max 11736.66)","6808.97 (min 2468.75, max 10926.83)","4432.04 (min 1587.30, max 7326.01)","6690.34 (min 2519.69, max 10785.31)","7146.13 (min 2626.83, max 11339.48)"
   "bw_mem-frd-16mb (mb/s)","6031.55 (min 5869.41, max 6331.62)","4624.24 (min 4307.44, max 4795.44)","3946.37 (min 3094.18, max 4653.87)","1830.43 (min 1743.68, max 1922.15)","3743.18 (min 3109.82, max 4422.94)","3330.44 (min 2664.89, max 4094.69)"
   "bw_mem-frd-1mb (mb/s)","4711.65 (min 3106.16, max 6896.55)","4552.12 (min 3493.29, max 5706.41)","4190.87 (min 3154.57, max 5082.59)","1793.17 (min 1587.02, max 2036.28)","7145.23 (min 6025.23, max 7802.58)","7082.68 (min 6253.55, max 7799.44)"
   "bw_mem-frd-2mb (mb/s)","4297.73 (min 2406.26, max 6427.42)","4658.07 (min 3403.10, max 5818.18)","3723.34 (min 0.00, max 5311.08)","1619.83 (min 1448.44, max 1900.78)","4165.63 (min 3167.69, max 5596.64)","3870.43 (min 3185.35, max 4940.15)"
   "bw_mem-frd-4mb (mb/s)","4180.44 (min 2277.04, max 6322.86)","4550.68 (min 3393.86, max 5680.81)","3633.05 (min 2505.09, max 4726.54)","1656.85 (min 1517.64, max 1913.27)","3935.55 (min 2853.58, max 5161.29)","3467.84 (min 2661.79, max 4638.07)"
   "bw_mem-frd-8mb (mb/s)","4179.82 (min 2306.47, max 6313.13)","4075.80 (min 2783.09, max 5426.49)","3584.75 (min 2468.75, max 4665.40)","1702.82 (min 1571.86, max 1919.16)","3655.61 (min 2519.69, max 5056.89)","3317.07 (min 2626.83, max 4581.90)"
   "bw_mem-fwr-16mb (mb/s)","2269.59 (min 2229.97, max 2345.01)","9393.70 (min 8940.21, max 9661.84)","10378.10 (min 9650.18, max 10871.41)","7252.79 (min 7169.53, max 7346.19)","10017.17 (min 9543.69, max 10517.67)","10878.85 (min 10832.77, max 10921.50)"
   "bw_mem-fwr-1mb (mb/s)","5435.93 (min 4460.82, max 6896.55)","8787.33 (min 4830.92, max 12614.89)","8552.41 (min 4120.88, max 13155.52)","4721.94 (min 1781.58, max 7639.57)","10469.16 (min 7414.10, max 13678.91)","10614.38 (min 6358.04, max 13746.33)"
   "bw_mem-fwr-2mb (mb/s)","4480.82 (min 2773.44, max 6427.42)","8717.13 (min 5110.42, max 12219.23)","7726.48 (min 3503.24, max 11627.91)","4519.96 (min 1544.88, max 7477.30)","8743.85 (min 3850.60, max 13306.96)","8924.38 (min 3503.24, max 13693.56)"
   "bw_mem-fwr-4mb (mb/s)","4208.58 (min 2333.72, max 6322.86)","8535.06 (min 5017.02, max 11964.85)","7232.30 (min 3138.73, max 10928.96)","4498.64 (min 1517.64, max 7399.93)","7786.65 (min 3567.61, max 11795.32)","7976.07 (min 2661.79, max 12709.62)"
   "bw_mem-fwr-8mb (mb/s)","4145.93 (min 2235.57, max 6313.13)","8267.04 (min 4761.20, max 11734.51)","7177.70 (min 3093.58, max 10945.78)","4516.15 (min 1571.86, max 7363.77)","7257.34 (min 3496.50, max 10788.94)","7467.65 (min 2696.78, max 11367.67)"
   "bw_mem-rd-16mb (mb/s)","6267.83 (min 6116.99, max 6597.03)","4934.31 (min 4602.99, max 5155.47)","4614.33 (min 3624.42, max 5404.49)","1866.95 (min 1784.72, max 1959.58)","4442.18 (min 3686.21, max 5211.73)","3964.06 (min 3192.98, max 4761.90)"
   "bw_mem-rd-1mb (mb/s)","9741.61 (min 3172.71, max 15474.28)","6054.63 (min 1966.39, max 10133.23)","5964.33 (min 2956.39, max 12145.06)","1901.76 (min 1519.76, max 2246.35)","15728.83 (min 12228.80, max 17350.44)","15673.82 (min 10353.23, max 17322.27)"
   "bw_mem-rd-2mb (mb/s)","3809.46 (min 2.00, max 7072.14)","3870.14 (min 1045.66, max 6557.38)","3974.96 (min 2416.71, max 6380.86)","1687.20 (min 1395.67, max 1955.99)","4682.82 (min 2512.56, max 7312.61)","4454.36 (min 2.00, max 6802.72)"
   "bw_mem-rd-4mb (mb/s)","3542.58 (min 748.22, max 6666.67)","3668.88 (min 1087.25, max 6384.11)","3495.32 (min 2035.97, max 5547.85)","1747.35 (min 1550.59, max 1949.95)","3882.49 (min 2030.97, max 6160.95)","3905.02 (min 3183.19, max 5417.30)"
   "bw_mem-rd-8mb (mb/s)","3495.59 (min 711.36, max 6591.96)","3606.75 (min 1136.53, max 5957.92)","3392.45 (min 1972.14, max 5428.33)","1791.32 (min 1584.47, max 1952.17)","3870.04 (min 2016.64, max 6033.18)","3855.19 (min 3162.06, max 5316.50)"
   "bw_mem-rdwr-16mb (mb/s)","727.97 (min 715.34, max 752.34)","1800.36 (min 1615.67, max 1904.54)","2082.76 (min 1822.53, max 2259.89)","1776.33 (min 1708.31, max 1900.91)","1919.86 (min 1632.82, max 2150.54)","2465.78 (min 2328.63, max 2646.82)"
   "bw_mem-rdwr-1mb (mb/s)","3398.38 (min 1181.63, max 8832.93)","2600.45 (min 1482.85, max 6301.32)","3293.72 (min 2051.09, max 5330.88)","1266.29 (min 833.75, max 1827.15)","6318.10 (min 2600.55, max 9604.93)","6255.12 (min 2701.73, max 9608.41)"
   "bw_mem-rdwr-2mb (mb/s)","939.76 (min 2.00, max 1016.26)","1612.32 (min 1114.05, max 2461.32)","2332.87 (min 1857.01, max 3109.21)","1156.76 (min 818.55, max 1595.15)","2781.76 (min 1885.31, max 3873.72)","3237.35 (min 2241.79, max 4698.23)"
   "bw_mem-rdwr-4mb (mb/s)","859.77 (min 758.29, max 986.31)","1744.75 (min 1239.73, max 2411.45)","2112.30 (min 1804.24, max 2389.84)","1254.80 (min 850.07, max 1718.71)","2295.63 (min 1730.10, max 2725.72)","2757.09 (min 2295.77, max 3423.49)"
   "bw_mem-rdwr-8mb (mb/s)","841.90 (min 720.46, max 987.05)","1761.11 (min 1310.40, max 2323.56)","2074.71 (min 1825.86, max 2300.50)","1323.11 (min 868.34, max 1856.79)","2183.21 (min 1777.58, max 2807.51)","2565.46 (min 2141.04, max 3275.56)"
   "bw_mem-wr-16mb (mb/s)","718.28 (min 694.47, max 743.39)","1701.96 (min 1489.62, max 1835.49)","2145.12 (min 1956.71, max 2273.70)","1769.34 (min 1687.41, max 1864.80)","2006.17 (min 1903.86, max 2239.33)","2763.52 (min 2710.95, max 2818.89)"
   "bw_mem-wr-1mb (mb/s)","6901.66 (min 3172.71, max 15474.28)","3548.45 (min 1966.39, max 8189.73)","4543.60 (min 2956.39, max 12145.06)","1659.51 (min 1502.35, max 1841.28)","13162.04 (min 8983.11, max 17350.44)","13211.63 (min 8131.58, max 17322.27)"
   "bw_mem-wr-2mb (mb/s)","893.60 (min 2.00, max 989.28)","1612.56 (min 1045.66, max 2461.32)","2669.44 (min 2267.15, max 3109.21)","1484.21 (min 1314.49, max 1671.68)","3206.78 (min 2512.56, max 3873.72)","3772.97 (min 2776.33, max 4698.23)"
   "bw_mem-wr-4mb (mb/s)","767.60 (min 748.22, max 801.76)","1659.62 (min 1087.25, max 2411.45)","2240.35 (min 1920.31, max 2435.31)","1627.24 (min 1527.69, max 1768.35)","2457.12 (min 1730.10, max 3150.60)","3213.73 (min 2642.88, max 3673.77)"
   "bw_mem-wr-8mb (mb/s)","728.37 (min 711.36, max 758.44)","1846.91 (min 1136.53, max 2323.56)","2142.46 (min 1847.15, max 2300.50)","1722.82 (min 1573.56, max 1856.79)","2525.44 (min 1777.58, max 2981.74)","3121.35 (min 2645.50, max 3544.00)"
   "bw_mmap_rd-mo-1mb (mb/s)","11970.51 (min 10453.61, max 12278.05)","8584.05 (min 8233.53, max 8958.97)","8315.68 (min 7440.48, max 8805.51)","2050.84 (min 1962.18, max 2150.15)","12895.34 (min 12834.42, max 12918.49)","12906.71 (min 12839.06, max 12916.91)"
   "bw_mmap_rd-o2c-1mb (mb/s)","1441.26 (min 1216.76, max 1646.90)","1448.29 (min 1186.24, max 1664.51)","1259.23 (min 969.93, max 1498.13)","735.10 (min 658.65, max 797.32)","2560.07 (min 2331.84, max 2966.26)","2138.61 (min 1396.89, max 2808.46)"
   "bw_pipe (mb/s)","752.66 (min 725.04, max 777.56)","927.94 (min 856.51, max 973.20)","942.67 (min 851.11, max 1000.65)","769.76 (min 723.11, max 814.07)","963.04 (min 887.75, max 1020.56)","929.63 (min 796.46, max 1026.46)"
   "bw_unix (mb/s)","1597.96 (min 1549.65, max 1692.82)","1883.71 (min 1783.01, max 1967.65)","1924.77 (min 1739.48, max 2088.48)","1083.90 (min 1046.92, max 1128.41)","2859.68 (min 2628.23, max 3095.23)","2457.51 (min 1610.12, max 3148.32)"
   "lat_connect (us)","37.74 (min 37.05, max 38.55)","37.47 (min 36.66, max 38.16)","38.10 (min 37.30, max 38.89)","56.92 (min 56.32, max 57.46)","38.00 (min 37.24, max 38.42)","38.02 (min 37.27, max 38.65)"
   "lat_ctx-2-128k (us)","5.38 (min 5.02, max 5.72)","5.35 (min 4.98, max 5.66)","5.38 (min 5.05, max 5.65)","7.99 (min 7.64, max 8.67)","5.51 (min 5.23, max 5.77)","7.04 (min 5.32, max 8.92)"
   "lat_ctx-2-256k (us)","4.64 (min 4.32, max 5.07)","4.91 (min 4.34, max 6.41)","4.73 (min 4.35, max 5.04)","8.77 (min 6.69, max 14.05)","4.64 (min 4.39, max 4.94)","5.79 (min 4.41, max 8.17)"
   "lat_ctx-4-128k (us)","5.27 (min 4.95, max 5.58)","5.26 (min 4.90, max 5.48)","5.32 (min 4.92, max 5.55)","7.73 (min 6.99, max 8.68)","5.22 (min 4.94, max 5.55)","6.81 (min 5.52, max 7.61)"
   "lat_ctx-4-256k (us)","4.22 (min 3.86, max 4.63)","4.18 (min 3.82, max 4.54)","4.35 (min 4.02, max 4.71)","7.06 (min 4.17, max 9.58)","3.79 (min 3.44, max 4.20)","5.79 (min 5.24, max 6.99)"
   "lat_fs-0k (num_files)","401.38 (min 371.00, max 421.00)","407.64 (min 395.00, max 421.00)","387.07 (min 350.00, max 414.00)","237.25 (min 216.00, max 266.00)","400.00 (min 377.00, max 417.00)","398.57 (min 361.00, max 426.00)"
   "lat_fs-10k (num_files)","153.00 (min 142.00, max 163.00)","168.43 (min 148.00, max 182.00)","163.36 (min 149.00, max 189.00)","115.25 (min 107.00, max 123.00)","182.79 (min 169.00, max 199.00)","189.43 (min 176.00, max 201.00)"
   "lat_fs-1k (num_files)","229.13 (min 206.00, max 236.00)","233.50 (min 201.00, max 261.00)","226.93 (min 211.00, max 243.00)","163.94 (min 144.00, max 178.00)","240.43 (min 216.00, max 261.00)","246.79 (min 233.00, max 264.00)"
   "lat_fs-4k (num_files)","233.25 (min 205.00, max 261.00)","249.86 (min 224.00, max 262.00)","237.43 (min 202.00, max 256.00)","157.56 (min 138.00, max 174.00)","258.71 (min 231.00, max 274.00)","264.79 (min 246.00, max 270.00)"
   "lat_mem_rd-stride128-sz1000k (ns)","12.02 (min 11.23, max 13.01)","12.08 (min 11.14, max 12.91)","14.05 (min 12.09, max 16.76)","32.25 (min 30.61, max 33.72)","5.85 (min 5.65, max 6.53)","5.92 (min 5.65, max 6.60)"
   "lat_mem_rd-stride128-sz125k (ns)","5.57","5.57","5.57","5.56 (min 5.53, max 5.59)","5.65","5.65"
   "lat_mem_rd-stride128-sz250k (ns)","5.57 (min 5.57, max 5.59)","5.57 (min 5.57, max 5.59)","5.57","5.84 (min 5.83, max 5.85)","5.65 (min 5.65, max 5.69)","5.65 (min 5.65, max 5.66)"
   "lat_mem_rd-stride128-sz31k (ns)","3.79 (min 2.00, max 5.12)","3.85 (min 3.34, max 4.67)","4.13 (min 3.34, max 5.12)","3.67 (min 2.15, max 4.20)","4.20 (min 3.35, max 5.20)","4.01 (min 3.35, max 4.75)"
   "lat_mem_rd-stride128-sz50 (ns)","2.00","2.00","2.00","2.15","2.00","2.00"
   "lat_mem_rd-stride128-sz500k (ns)","5.58 (min 5.57, max 5.62)","5.65 (min 5.57, max 5.83)","5.77 (min 5.57, max 7.14)","11.93 (min 9.83, max 15.73)","5.65","5.65"
   "lat_mem_rd-stride128-sz62k (ns)","5.30 (min 4.67, max 5.57)","5.26 (min 5.12, max 5.59)","5.29 (min 4.67, max 5.57)","5.20 (min 4.52, max 5.28)","5.33 (min 4.76, max 5.65)","5.28 (min 4.74, max 5.65)"
   "lat_mmap-1m (us)","33.13 (min 28.00, max 37.00)","30.14 (min 28.00, max 34.00)","32.29 (min 28.00, max 36.00)","54.13 (min 50.00, max 58.00)","31.50 (min 29.00, max 36.00)","32.00 (min 29.00, max 36.00)"
   "lat_ops-double-add (ns)","1.96","1.96","1.96","2.86","1.96","1.96"
   "lat_ops-double-div (ns)","9.01 (min 9.01, max 9.02)","9.01 (min 9.01, max 9.02)","9.01 (min 9.01, max 9.02)","15.74 (min 15.74, max 15.75)","9.01","9.01 (min 9.00, max 9.01)"
   "lat_ops-double-mul (ns)","2.00","2.00","2.00","2.86","2.00","2.00"
   "lat_ops-float-add (ns)","1.96","1.96","1.96","2.86","1.96","1.96"
   "lat_ops-float-div (ns)","5.51","5.51 (min 5.50, max 5.51)","5.51","9.30 (min 9.30, max 9.31)","5.50 (min 5.50, max 5.51)","5.51 (min 5.50, max 5.51)"
   "lat_ops-float-mul (ns)","2.00","2.00","2.00 (min 2.00, max 2.01)","2.86","2.00","2.00"
   "lat_ops-int-add (ns)","0.50","0.50","0.50","0.72","0.50","0.50"
   "lat_ops-int-bit (ns)","0.33","0.33","0.33","0.48","0.33","0.33"
   "lat_ops-int-div (ns)","4.01 (min 4.00, max 4.01)","4.01 (min 4.00, max 4.01)","4.01 (min 4.00, max 4.02)","4.29 (min 4.29, max 4.30)","4.00 (min 4.00, max 4.01)","4.00 (min 4.00, max 4.01)"
   "lat_ops-int-mod (ns)","4.67 (min 4.67, max 4.69)","4.67 (min 4.67, max 4.68)","4.67 (min 4.67, max 4.68)","4.53 (min 4.53, max 4.54)","4.67","4.67"
   "lat_ops-int-mul (ns)","1.52","1.52","1.52","3.08 (min 3.07, max 3.09)","1.52","1.52"
   "lat_ops-int64-add (ns)","0.50","0.50","0.50","0.72","0.50","0.50"
   "lat_ops-int64-bit (ns)","0.33","0.33","0.33","0.48","0.33","0.33"
   "lat_ops-int64-div (ns)","3.00 (min 3.00, max 3.01)","3.00","3.00 (min 3.00, max 3.01)","6.80 (min 6.79, max 6.80)","3.00","3.00"
   "lat_ops-int64-mod (ns)","5.67 (min 5.67, max 5.68)","5.67 (min 5.67, max 5.68)","5.67 (min 5.67, max 5.68)","5.25 (min 5.24, max 5.25)","5.67 (min 5.67, max 5.68)","5.67 (min 5.67, max 5.68)"
   "lat_ops-int64-mul (ns)","2.52","2.52","2.52 (min 2.52, max 2.53)","3.56 (min 3.55, max 3.57)","2.52","2.52"
   "lat_pagefault (us)","0.29 (min 0.25, max 0.45)","0.24 (min 0.23, max 0.25)","0.28 (min 0.24, max 0.46)","0.63 (min 0.52, max 1.11)","0.24 (min 0.23, max 0.25)","0.24 (min 0.24, max 0.25)"
   "lat_pipe (us)","14.93 (min 14.10, max 15.90)","14.66 (min 13.93, max 15.28)","15.00 (min 13.74, max 15.87)","25.87 (min 25.14, max 26.41)","16.63 (min 16.08, max 17.14)","19.84 (min 17.41, max 22.46)"
   "lat_proc-exec (us)","424.29 (min 402.46, max 439.75)","378.15 (min 354.69, max 393.07)","442.23 (min 407.08, max 478.00)","735.24 (min 697.63, max 780.00)","338.99 (min 328.18, max 346.94)","416.27 (min 346.80, max 439.69)"
   "lat_proc-fork (us)","389.21 (min 377.79, max 398.57)","349.91 (min 332.76, max 385.27)","398.65 (min 379.92, max 421.79)","646.86 (min 619.44, max 682.75)","318.01 (min 300.47, max 338.41)","388.26 (min 335.94, max 419.62)"
   "lat_proc-proccall (us)","0.00","0.00","0.00","0.01","0.00","0.00"
   "lat_select (us)","12.55 (min 11.45, max 13.80)","12.69 (min 11.44, max 13.64)","12.27 (min 11.43, max 13.34)","33.90 (min 32.82, max 34.35)","12.70 (min 11.43, max 13.69)","12.53 (min 11.45, max 13.35)"
   "lat_sem (us)","1.98 (min 1.50, max 2.32)","1.94 (min 1.66, max 2.17)","2.10 (min 1.81, max 2.56)","2.97 (min 2.48, max 3.95)","1.82 (min 1.39, max 2.09)","2.34 (min 1.42, max 2.94)"
   "lat_sig-catch (us)","3.19 (min 2.89, max 3.34)","3.22 (min 2.86, max 3.36)","3.20 (min 2.88, max 3.35)","5.57 (min 5.25, max 5.73)","3.23 (min 2.88, max 3.41)","3.24 (min 2.96, max 3.40)"
   "lat_sig-install (us)","0.54 (min 0.52, max 0.56)","0.55 (min 0.53, max 0.57)","0.55 (min 0.52, max 0.56)","0.67 (min 0.64, max 0.70)","0.55 (min 0.54, max 0.57)","0.55 (min 0.53, max 0.57)"
   "lat_sig-prot (us)","0.45 (min 0.26, max 0.64)","0.48 (min 0.33, max 0.62)","0.53 (min 0.30, max 1.06)","0.66 (min 0.47, max 1.38)","0.53 (min 0.35, max 1.27)","0.48 (min 0.35, max 0.62)"
   "lat_syscall-fstat (us)","1.00 (min 0.91, max 1.09)","1.02 (min 0.94, max 1.10)","1.02 (min 0.94, max 1.10)","2.00 (min 1.90, max 2.07)","1.02 (min 0.93, max 1.10)","1.03 (min 0.93, max 1.11)"
   "lat_syscall-null (us)","0.40 (min 0.39, max 0.42)","0.40 (min 0.39, max 0.42)","0.40 (min 0.39, max 0.41)","0.46 (min 0.46, max 0.50)","0.40 (min 0.39, max 0.42)","0.40 (min 0.39, max 0.42)"
   "lat_syscall-open (us)","162.44 (min 149.65, max 220.24)","167.17 (min 129.86, max 271.35)","155.18 (min 132.58, max 196.79)","164.31 (min 148.50, max 199.96)","170.07 (min 93.72, max 690.67)","205.79 (min 124.79, max 314.00)"
   "lat_syscall-read (us)","0.51 (min 0.50, max 0.54)","0.52 (min 0.50, max 0.56)","0.51 (min 0.49, max 0.53)","0.81 (min 0.79, max 0.89)","0.51 (min 0.50, max 0.53)","0.51 (min 0.49, max 0.54)"
   "lat_syscall-stat (us)","2.35 (min 2.22, max 2.53)","2.37 (min 2.25, max 2.47)","2.39 (min 2.22, max 2.50)","4.87 (min 4.63, max 5.05)","2.38 (min 2.25, max 2.50)","2.41 (min 2.28, max 2.55)"
   "lat_syscall-write (us)","0.49 (min 0.47, max 0.51)","0.49 (min 0.47, max 0.52)","0.49 (min 0.47, max 0.53)","0.77 (min 0.74, max 0.84)","0.49 (min 0.47, max 0.52)","0.49 (min 0.47, max 0.51)"
   "lat_tcp (us)","0.81 (min 0.79, max 0.83)","0.82 (min 0.79, max 0.86)","0.82 (min 0.79, max 0.85)","0.91 (min 0.91, max 0.97)","0.82 (min 0.79, max 0.84)","0.82 (min 0.80, max 0.86)"
   "lat_unix (us)","20.02 (min 19.48, max 20.91)","20.59 (min 18.81, max 27.23)","20.25 (min 19.48, max 21.07)","30.14 (min 29.18, max 31.07)","20.75 (min 19.79, max 25.68)","23.85 (min 19.76, max 35.41)"
   "latency_for_0.50_mb_block_size (nanosec)","5.58 (min 5.57, max 5.62)","5.65 (min 5.57, max 5.83)","5.77 (min 5.57, max 7.14)","11.93 (min 9.83, max 15.73)","5.65","5.65"
   "latency_for_1.00_mb_block_size (nanosec)","6.01 (min 0.00, max 13.01)","6.04 (min 0.00, max 12.91)","7.02 (min 0.00, max 16.76)","16.13 (min 0.00, max 33.72)","2.93 (min 0.00, max 6.53)","2.96 (min 0.00, max 6.60)"
   "pipe_bandwidth (mb\s)","752.66 (min 725.04, max 777.56)","927.94 (min 856.51, max 973.20)","942.67 (min 851.11, max 1000.65)","769.76 (min 723.11, max 814.07)","963.04 (min 887.75, max 1020.56)","929.63 (min 796.46, max 1026.46)"
   "pipe_latency (microsec)","14.93 (min 14.10, max 15.90)","14.66 (min 13.93, max 15.28)","15.00 (min 13.74, max 15.87)","25.87 (min 25.14, max 26.41)","16.63 (min 16.08, max 17.14)","19.84 (min 17.41, max 22.46)"
   "procedure_call (microsec)","0.00","0.00","0.00","0.01","0.00","0.00"
   "select_on_200_tcp_fds (microsec)","12.55 (min 11.45, max 13.80)","12.69 (min 11.44, max 13.64)","12.27 (min 11.43, max 13.34)","33.90 (min 32.82, max 34.35)","12.70 (min 11.43, max 13.69)","12.53 (min 11.45, max 13.35)"
   "semaphore_latency (microsec)","1.98 (min 1.50, max 2.32)","1.94 (min 1.66, max 2.17)","2.10 (min 1.81, max 2.56)","2.97 (min 2.48, max 3.95)","1.82 (min 1.39, max 2.09)","2.34 (min 1.42, max 2.94)"
   "signal_handler_latency (microsec)","0.54 (min 0.52, max 0.56)","0.55 (min 0.53, max 0.57)","0.55 (min 0.52, max 0.56)","0.67 (min 0.64, max 0.70)","0.55 (min 0.54, max 0.57)","0.55 (min 0.53, max 0.57)"
   "signal_handler_overhead (microsec)","3.19 (min 2.89, max 3.34)","3.22 (min 2.86, max 3.36)","3.20 (min 2.88, max 3.35)","5.57 (min 5.25, max 5.73)","3.23 (min 2.88, max 3.41)","3.24 (min 2.96, max 3.40)"
   "tcp_ip_connection_cost_to_localhost (microsec)","37.74 (min 37.05, max 38.55)","37.47 (min 36.66, max 38.16)","38.10 (min 37.30, max 38.89)","56.92 (min 56.32, max 57.46)","38.00 (min 37.24, max 38.42)","38.02 (min 37.27, max 38.65)"
   "tcp_latency_using_localhost (microsec)","0.81 (min 0.79, max 0.83)","0.82 (min 0.79, max 0.86)","0.82 (min 0.79, max 0.85)","0.91 (min 0.91, max 0.97)","0.82 (min 0.79, max 0.84)","0.82 (min 0.80, max 0.86)"

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
   :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

   "cpu_clock (mhz)","2000.00","2000.00","2000.00","1400.00","2000.00","2000.00"
   "dhrystone_per_mhz (dmips/mhz)","5.37 (min 4.70, max 5.70)","5.51 (min 4.40, max 5.70)","5.32 (min 4.40, max 5.70)","2.91 (min 2.90, max 3.00)","5.25 (min 4.40, max 5.70)","5.63 (min 5.20, max 5.70)"
   "dhrystone_per_second (dhrystonep)","18868686.93 (min 16666667.00, max 20000000.00)","19309440.50 (min 15384615.00, max 20000000.00)","18696303.71 (min 15384615.00, max 20000000.00)","7159391.41 (min 7142857.00, max 7407407.50)","18458208.50 (min 15384615.00, max 20000000.00)","19740259.71 (min 18181818.00, max 20000000.00)"

Whetstone
=========

Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

.. code-block:: console

    runWhetstone

.. csv-table:: Whetstone Benchmarks
   :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

   "whetstone (mips)","10000.00","10000.00","10000.00","7500.00 (min 5000.00, max 10000.00)","10000.00","10000.00"

Linpack
=======

Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
   :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

   "linpack (kflops)","2475799.87 (min 2359680.00, max 2616870.00)","2483644.57 (min 2345173.00, max 2621866.00)","2527265.43 (min 2387575.00, max 2622867.00)","575796.88 (min 572652.00, max 578392.00)","2492077.00 (min 2396742.00, max 2588265.00)","2475207.86 (min 2334013.00, max 2602983.00)"

NBench
======

NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
   :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

   "assignment (iterations)","31.88 (min 31.68, max 31.99)","31.87 (min 31.52, max 31.98)","31.91 (min 31.78, max 31.99)","14.49 (min 14.42, max 14.53)","31.79 (min 31.63, max 31.87)","31.76 (min 31.42, max 31.90)"
   "fourier (iterations)","60888.25 (min 59005.00, max 65633.00)","61891.71 (min 58899.00, max 65543.00)","61570.86 (min 59223.00, max 65637.00)","22585.88 (min 22050.00, max 22831.00)","60595.71 (min 59116.00, max 61995.00)","61467.36 (min 59750.00, max 64969.00)"
   "fp_emulation (iterations)","387.99 (min 387.93, max 388.05)","387.99 (min 387.84, max 388.03)","387.99 (min 387.91, max 388.06)","215.64 (min 215.62, max 215.65)","387.99 (min 387.89, max 388.05)","388.00 (min 387.92, max 388.04)"
   "huffman (iterations)","2407.24 (min 2399.70, max 2413.10)","2407.77 (min 2402.70, max 2411.80)","2407.53 (min 2400.40, max 2416.10)","1184.07 (min 1183.30, max 1184.30)","2407.47 (min 2398.60, max 2415.70)","2406.09 (min 2389.10, max 2413.40)"
   "idea (iterations)","7996.32 (min 7995.20, max 7996.70)","7996.34 (min 7995.20, max 7996.60)","7996.14 (min 7994.90, max 7996.50)","3444.76 (min 3444.60, max 3444.90)","7996.07 (min 7991.30, max 7996.70)","7996.49 (min 7996.20, max 7997.00)"
   "lu_decomposition (iterations)","1372.21 (min 1345.70, max 1391.10)","1368.75 (min 1355.90, max 1389.20)","1373.78 (min 1356.60, max 1389.00)","529.18 (min 526.26, max 531.90)","1360.52 (min 1329.90, max 1377.70)","1359.75 (min 1331.90, max 1377.70)"
   "neural_net (iterations)","28.40 (min 26.96, max 29.03)","28.65 (min 27.57, max 29.03)","28.83 (min 27.06, max 29.04)","8.65 (min 8.65, max 8.67)","28.40 (min 26.31, max 29.03)","28.37 (min 26.79, max 29.04)"
   "numeric_sort (iterations)","874.58 (min 855.53, max 884.84)","874.35 (min 865.31, max 882.72)","878.32 (min 864.73, max 885.36)","626.11 (min 616.42, max 629.72)","876.88 (min 866.80, max 882.60)","877.28 (min 867.45, max 885.54)"
   "string_sort (iterations)","347.06 (min 312.60, max 361.51)","351.52 (min 341.26, max 358.43)","353.48 (min 343.19, max 361.36)","163.94 (min 163.93, max 163.94)","350.37 (min 341.78, max 361.47)","349.35 (min 311.66, max 355.42)"

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
   :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

   "add (mb/s)","5290.63 (min 5217.90, max 5457.70)","5097.81 (min 4752.00, max 5294.00)","6174.44 (min 5737.20, max 6497.20)","2492.61 (min 2403.10, max 2620.50)","5832.73 (min 5618.80, max 6250.70)","5681.79 (min 5419.90, max 5789.80)"
   "copy (mb/s)","4649.63 (min 4598.40, max 4776.80)","5423.85 (min 5217.70, max 5544.00)","6863.24 (min 5199.90, max 7755.70)","3614.89 (min 3509.50, max 3818.80)","6095.19 (min 5188.10, max 6874.30)","5637.41 (min 5285.90, max 6196.50)"
   "scale (mb/s)","4725.77 (min 4679.70, max 4843.10)","5290.73 (min 5083.40, max 5409.80)","6979.81 (min 5312.60, max 7859.70)","3308.43 (min 3167.90, max 3474.80)","6209.16 (min 5274.60, max 7011.70)","5628.16 (min 5286.80, max 6220.30)"
   "triad (mb/s)","5296.63 (min 5222.90, max 5465.60)","5079.06 (min 4733.20, max 5277.20)","6174.08 (min 5737.20, max 6499.70)","2278.86 (min 2216.30, max 2373.80)","5828.83 (min 5609.20, max 6249.20)","5675.08 (min 5421.30, max 5780.50)"

CoreMarkPro
===========

CoreMark\ |reg|-Pro is a comprehensive, advanced processor benchmark that works
with and enhances the market-proven industry-standard EEMBC CoreMark\ |reg|
benchmark. While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the
entire processor, adding comprehensive support for multicore technology, a
combination of integer and floating-point workloads, and data sets for utilizing
larger memory subsystems.

.. csv-table:: CoreMarkPro Benchmarks
   :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

   "cjpeg-rose7-preset (workloads/)","82.37 (min 81.97, max 83.33)","82.41 (min 80.00, max 83.33)","82.54 (min 81.97, max 82.64)","41.96 (min 41.67, max 42.02)","82.60 (min 81.30, max 83.33)","82.81 (min 81.97, max 83.33)"
   "core (workloads/)","0.77 (min 0.77, max 0.78)","0.77 (min 0.77, max 0.78)","0.77 (min 0.77, max 0.78)","0.30","0.77 (min 0.77, max 0.78)","0.77 (min 0.77, max 0.78)"
   "coremark-pro ()","2460.77 (min 2434.80, max 2487.00)","2496.40 (min 2482.04, max 2519.86)","2479.12 (min 2450.48, max 2514.48)","922.92 (min 896.57, max 945.42)","2499.77 (min 2468.69, max 2526.97)","2507.91 (min 2472.84, max 2537.85)"
   "linear_alg-mid-100x100-sp (workloads/)","80.66 (min 78.62, max 82.51)","80.69 (min 79.37, max 82.10)","80.39 (min 78.62, max 81.83)","14.68 (min 14.66, max 14.70)","79.55 (min 78.13, max 81.30)","80.42 (min 79.11, max 81.97)"
   "loops-all-mid-10k-sp (workloads/)","2.47 (min 2.45, max 2.48)","2.47 (min 2.44, max 2.48)","2.47 (min 2.45, max 2.50)","0.71 (min 0.70, max 0.71)","2.46 (min 2.44, max 2.47)","2.46 (min 2.46, max 2.47)"
   "nnet_test (workloads/)","3.64 (min 3.41, max 3.83)","3.67 (min 3.52, max 3.87)","3.68 (min 3.38, max 3.86)","1.09 (min 1.08, max 1.09)","3.60 (min 3.34, max 3.87)","3.66 (min 3.42, max 3.84)"
   "parser-125k (workloads/)","11.00 (min 10.87, max 11.11)","11.09 (min 10.99, max 11.11)","11.02 (min 10.87, max 11.11)","8.73 (min 8.62, max 8.77)","10.85 (min 10.75, max 10.87)","10.86 (min 10.75, max 10.87)"
   "radix2-big-64k (workloads/)","251.82 (min 223.46, max 265.53)","274.60 (min 262.19, max 283.93)","264.32 (min 236.52, max 279.17)","62.28 (min 47.42, max 74.70)","295.56 (min 272.78, max 307.79)","295.15 (min 271.59, max 307.31)"
   "sha-test (workloads/)","157.74 (min 156.25, max 158.73)","158.20 (min 156.25, max 158.73)","157.20 (min 156.25, max 158.73)","81.30 (min 80.65, max 81.97)","158.73","158.54 (min 156.25, max 158.73)"
   "zip-test (workloads/)","46.61 (min 45.45, max 47.62)","47.62","47.12 (min 45.45, max 47.62)","22.13 (min 21.74, max 22.22)","47.31 (min 45.45, max 47.62)","47.29 (min 45.45, max 47.62)"

.. csv-table:: CoreMarkProTwoCore Benchmarks
   :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

   "cjpeg-rose7-preset (workloads/)","163.35 (min 161.29, max 163.93)","163.41 (min 158.73, max 163.93)","162.33 (min 156.25, max 163.93)","83.49 (min 82.64, max 84.03)","164.16 (min 161.29, max 166.67)","164.77 (min 163.93, max 166.67)"
   "core (workloads/)","1.55 (min 1.54, max 1.55)","1.55 (min 1.54, max 1.56)","1.54 (min 1.53, max 1.55)","0.60","1.55 (min 1.54, max 1.56)","1.55 (min 1.54, max 1.55)"
   "coremark-pro ()","4259.62 (min 4113.16, max 4398.22)","4376.02 (min 4277.67, max 4469.69)","4401.01 (min 4327.37, max 4500.29)","1639.15 (min 1620.08, max 1655.67)","4694.72 (min 4639.00, max 4720.56)","4868.75 (min 4709.49, max 5010.90)"
   "linear_alg-mid-100x100-sp (workloads/)","160.07 (min 158.23, max 162.87)","159.46 (min 156.74, max 163.40)","160.55 (min 158.23, max 163.40)","29.35 (min 29.33, max 29.38)","160.14 (min 158.73, max 161.81)","160.54 (min 158.73, max 162.34)"
   "loops-all-mid-10k-sp (workloads/)","3.92 (min 3.48, max 4.22)","3.98 (min 3.63, max 4.32)","4.01 (min 3.79, max 4.29)","1.28 (min 1.27, max 1.29)","4.06 (min 3.88, max 4.38)","4.34 (min 3.85, max 4.92)"
   "nnet_test (workloads/)","7.28 (min 7.04, max 7.63)","7.27 (min 6.69, max 7.70)","7.33 (min 7.01, max 7.69)","2.17 (min 2.16, max 2.17)","7.23 (min 7.11, max 7.30)","7.29 (min 7.18, max 7.66)"
   "parser-125k (workloads/)","20.67 (min 19.80, max 20.83)","21.20 (min 21.05, max 21.28)","20.51 (min 19.80, max 21.05)","13.24 (min 12.58, max 14.08)","21.09 (min 20.83, max 21.28)","21.21 (min 20.83, max 21.74)"
   "radix2-big-64k (workloads/)","222.49 (min 194.82, max 253.55)","266.82 (min 242.95, max 292.48)","281.51 (min 262.40, max 317.36)","65.44 (min 60.39, max 71.41)","420.82 (min 411.69, max 436.49)","533.91 (min 414.25, max 619.96)"
   "sha-test (workloads/)","306.43 (min 285.71, max 312.50)","301.51 (min 270.27, max 312.50)","302.34 (min 277.78, max 312.50)","161.11 (min 158.73, max 161.29)","317.15 (min 312.50, max 322.58)","319.48 (min 312.50, max 322.58)"
   "zip-test (workloads/)","81.20 (min 62.50, max 86.96)","84.36 (min 76.92, max 90.91)","85.43 (min 80.00, max 90.91)","42.49 (min 41.67, max 42.55)","93.24 (min 90.91, max 95.24)","94.57 (min 90.91, max 95.24)"

.. csv-table:: CoreMarkProFourCore Benchmarks
   :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j784s4-evm: perf"

   "cjpeg-rose7-preset (workloads/)","160.99 (min 156.25, max 163.93)","162.29 (min 158.73, max 163.93)","161.48 (min 158.73, max 163.93)","159.43 (min 153.85, max 161.29)","322.58"
   "core (workloads/)","1.55 (min 1.54, max 1.55)","1.54 (min 1.54, max 1.55)","1.54 (min 1.54, max 1.55)","1.19 (min 1.18, max 1.20)","3.09 (min 3.08, max 3.10)"
   "coremark-pro ()","4128.13 (min 3993.08, max 4234.65)","4324.66 (min 4265.20, max 4430.38)","4341.94 (min 4235.39, max 4412.72)","2553.00 (min 2513.56, max 2580.49)","8759.02 (min 8481.33, max 8904.81)"
   "linear_alg-mid-100x100-sp (workloads/)","160.01 (min 155.76, max 161.81)","160.14 (min 156.74, max 161.81)","159.78 (min 153.85, max 162.87)","56.27 (min 55.68, max 56.37)","311.27 (min 304.88, max 314.47)"
   "loops-all-mid-10k-sp (workloads/)","4.02 (min 3.84, max 4.23)","3.98 (min 3.53, max 4.34)","4.11 (min 3.88, max 4.40)","2.06 (min 2.00, max 2.12)","7.36 (min 5.58, max 8.07)"
   "nnet_test (workloads/)","7.34 (min 7.07, max 7.62)","7.41 (min 7.19, max 7.67)","7.40 (min 7.09, max 7.58)","3.62 (min 3.61, max 3.62)","12.34 (min 11.98, max 12.85)"
   "parser-125k (workloads/)","19.34 (min 18.78, max 19.70)","20.37 (min 19.70, max 20.73)","18.86 (min 18.43, max 19.51)","8.56 (min 7.77, max 9.24)","39.69 (min 37.38, max 41.67)"
   "radix2-big-64k (workloads/)","181.73 (min 154.49, max 205.89)","240.32 (min 230.84, max 270.71)","272.63 (min 225.68, max 292.57)","92.88 (min 87.57, max 98.36)","819.20 (min 746.27, max 882.61)"
   "sha-test (workloads/)","302.75 (min 285.71, max 312.50)","306.29 (min 285.71, max 312.50)","303.53 (min 277.78, max 312.50)","270.27","526.32"
   "zip-test (workloads/)","79.27 (min 72.73, max 83.33)","85.07 (min 76.92, max 90.91)","82.67 (min 75.47, max 88.89)","76.44 (min 66.67, max 78.43)","178.99 (min 173.91, max 181.82)"

.. csv-table:: CoreMarkProEightCore Benchmarks
   :header: "Benchmarks","j784s4-evm: perf"

   "cjpeg-rose7-preset (workloads/)","625.00"
   "core (workloads/)","6.18 (min 6.16, max 6.21)"
   "coremark-pro ()","14092.08 (min 13612.67, max 14294.03)"
   "linear_alg-mid-100x100-sp (workloads/)","577.81 (min 568.18, max 581.40)"
   "loops-all-mid-10k-sp (workloads/)","10.34 (min 9.56, max 10.69)"
   "nnet_test (workloads/)","18.86 (min 18.08, max 19.27)"
   "parser-125k (workloads/)","72.59 (min 70.80, max 73.39)"
   "radix2-big-64k (workloads/)","843.59 (min 824.40, max 866.55)"
   "sha-test (workloads/)","769.23"
   "zip-test (workloads/)","304.99 (min 228.57, max 320.00)"

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
   :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

   "4m-check (workloads/)","821.83 (min 802.05, max 865.35)","812.96 (min 774.71, max 847.75)","759.38 (min 692.71, max 804.38)","396.97 (min 379.08, max 410.85)","1119.91 (min 1099.38, max 1148.37)","994.22 (min 979.62, max 1003.21)"
   "4m-check-reassembly (workloads/)","114.29 (min 111.24, max 123.31)","136.70 (min 128.37, max 143.06)","134.40 (min 121.36, max 143.27)","116.34 (min 111.36, max 121.36)","173.71 (min 164.20, max 190.84)","185.03 (min 176.37, max 192.31)"
   "4m-check-reassembly-tcp (workloads/)","85.60 (min 83.61, max 88.34)","92.97 (min 88.34, max 98.81)","86.03 (min 76.92, max 93.28)","57.99 (min 56.18, max 59.52)","106.09 (min 102.04, max 113.12)","106.55 (min 99.60, max 110.13)"
   "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","39.55 (min 38.78, max 40.57)","42.99 (min 41.12, max 44.28)","40.19 (min 38.73, max 41.58)","32.38 (min 31.76, max 33.11)","54.40 (min 53.33, max 56.50)","36.51 (min 33.30, max 39.60)"
   "4m-check-reassembly-tcp-x264w2 (workloads/)","2.67 (min 2.62, max 2.69)","2.68 (min 2.50, max 2.75)","2.65 (min 2.60, max 2.70)","1.87 (min 1.69, max 1.92)","4.65 (min 3.87, max 4.84)","4.68 (min 3.29, max 4.88)"
   "4m-cmykw2 (workloads/)","309.18 (min 307.22, max 311.04)","312.75 (min 310.08, max 314.96)","308.59 (min 305.81, max 311.53)","242.86 (min 232.83, max 247.83)","591.40 (min 561.80, max 604.23)","597.43 (min 576.37, max 606.06)"
   "4m-cmykw2-rotatew2 (workloads/)","58.84 (min 57.20, max 59.76)","62.52 (min 61.54, max 63.63)","58.81 (min 57.53, max 59.64)","49.00 (min 47.77, max 50.04)","71.38 (min 67.64, max 72.29)","46.63 (min 41.49, max 54.60)"
   "4m-reassembly (workloads/)","102.30 (min 99.01, max 107.07)","124.23 (min 115.74, max 129.03)","117.79 (min 106.27, max 127.23)","80.63 (min 76.75, max 90.17)","127.69 (min 122.25, max 143.06)","132.99 (min 125.63, max 141.64)"
   "4m-rotatew2 (workloads/)","69.19 (min 68.68, max 69.83)","72.57 (min 70.97, max 73.64)","68.70 (min 67.84, max 69.44)","52.49 (min 51.63, max 53.68)","77.36 (min 76.57, max 77.94)","51.00 (min 40.68, max 64.43)"
   "4m-tcp-mixed (workloads/)","262.23 (min 250.00, max 271.19)","263.79 (min 242.42, max 275.86)","254.54 (min 231.88, max 266.67)","116.55 (min 114.29, max 118.52)","261.44 (min 258.07, max 271.19)","251.52 (min 238.81, max 262.30)"
   "4m-x264w2 (workloads/)","2.70 (min 2.27, max 2.75)","2.75 (min 2.64, max 2.80)","2.71 (min 2.69, max 2.74)","1.95 (min 1.89, max 1.98)","4.84 (min 3.99, max 5.07)","4.95 (min 4.14, max 5.07)"
   "idct-4m (workloads/)","34.88 (min 34.75, max 34.92)","35.03 (min 34.99, max 35.06)","34.85 (min 34.75, max 34.94)","19.15 (min 19.14, max 19.16)","35.05 (min 34.93, max 35.10)","35.07 (min 34.90, max 35.12)"
   "idct-4mw1 (workloads/)","34.87 (min 34.73, max 34.93)","35.03 (min 34.94, max 35.06)","34.90 (min 34.71, max 34.97)","19.15 (min 19.14, max 19.17)","35.06 (min 34.92, max 35.12)","35.09 (min 34.93, max 35.12)"
   "ippktcheck-4m (workloads/)","818.07 (min 799.49, max 854.41)","811.22 (min 769.47, max 850.92)","762.03 (min 709.02, max 815.40)","396.83 (min 381.04, max 412.68)","1108.77 (min 1013.79, max 1123.09)","992.28 (min 967.87, max 1003.61)"
   "ippktcheck-4mw1 (workloads/)","813.36 (min 796.94, max 848.03)","810.84 (min 777.12, max 851.79)","760.64 (min 696.38, max 825.08)","397.90 (min 378.90, max 413.84)","1118.30 (min 1105.22, max 1123.09)","993.48 (min 967.87, max 1003.21)"
   "ipres-4m (workloads/)","151.17 (min 123.25, max 158.40)","175.22 (min 164.84, max 181.60)","157.21 (min 140.85, max 170.26)","105.73 (min 98.62, max 110.70)","177.63 (min 165.93, max 196.85)","180.86 (min 173.21, max 190.36)"
   "ipres-4mw1 (workloads/)","151.69 (min 142.72, max 157.40)","175.83 (min 165.75, max 182.70)","156.94 (min 139.80, max 169.11)","105.94 (min 99.67, max 110.87)","178.66 (min 169.68, max 200.54)","180.36 (min 174.42, max 189.16)"
   "md5-4m (workloads/)","43.04 (min 42.37, max 43.59)","46.07 (min 45.05, max 46.66)","42.48 (min 41.37, max 43.29)","27.27 (min 26.75, max 27.87)","47.12 (min 46.58, max 47.69)","44.57 (min 44.35, max 44.88)"
   "md5-4mw1 (workloads/)","43.27 (min 42.83, max 43.78)","46.12 (min 45.07, max 46.82)","42.69 (min 41.36, max 43.50)","27.40 (min 26.92, max 27.82)","47.11 (min 46.71, max 47.64)","44.66 (min 44.13, max 45.05)"
   "rgbcmyk-4m (workloads/)","162.74 (min 160.26, max 163.27)","163.49 (min 163.27, max 163.80)","162.50 (min 159.87, max 162.87)","64.72 (min 62.32, max 65.53)","163.28 (min 160.00, max 164.07)","163.72 (min 163.27, max 163.93)"
   "rgbcmyk-4mw1 (workloads/)","162.64 (min 160.90, max 163.13)","163.03 (min 160.13, max 163.67)","162.60 (min 161.94, max 162.87)","64.72 (min 62.29, max 65.57)","163.44 (min 161.03, max 163.93)","163.29 (min 160.64, max 164.07)"
   "rotate-4ms1 (workloads/)","50.79 (min 50.10, max 51.28)","53.61 (min 52.74, max 54.53)","50.48 (min 49.31, max 51.28)","23.00 (min 22.17, max 23.72)","53.12 (min 52.58, max 54.11)","53.20 (min 52.47, max 53.53)"
   "rotate-4ms1w1 (workloads/)","50.62 (min 46.55, max 51.60)","53.60 (min 52.80, max 54.23)","50.29 (min 48.97, max 51.28)","23.02 (min 22.09, max 23.70)","53.20 (min 52.74, max 54.17)","53.24 (min 53.02, max 53.48)"
   "rotate-4ms64 (workloads/)","52.41 (min 51.92, max 53.02)","55.21 (min 54.47, max 55.80)","51.91 (min 50.61, max 52.91)","23.27 (min 22.36, max 23.93)","54.57 (min 53.71, max 55.49)","54.83 (min 54.64, max 55.49)"
   "rotate-4ms64w1 (workloads/)","52.49 (min 51.60, max 53.76)","54.96 (min 53.82, max 55.49)","51.71 (min 50.61, max 52.36)","23.20 (min 22.28, max 23.89)","54.56 (min 54.05, max 55.43)","54.65 (min 53.94, max 54.82)"
   "x264-4mq (workloads/)","1.42 (min 1.41, max 1.43)","1.42 (min 1.31, max 1.44)","1.41 (min 1.40, max 1.42)","0.58 (min 0.57, max 0.58)","1.41 (min 1.26, max 1.44)","1.38 (min 0.80, max 1.44)"
   "x264-4mqw1 (workloads/)","1.41 (min 1.32, max 1.43)","1.41 (min 1.29, max 1.44)","1.41 (min 1.39, max 1.43)","0.58 (min 0.55, max 0.58)","1.43 (min 1.40, max 1.45)","1.38 (min 0.96, max 1.44)"

*********************
Boot-time Measurement
*********************

Boot media: MMCSD
=================

.. csv-table:: Linux boot time MMCSD
   :header: "Boot Configuration","j7200-evm: Boot time in seconds: avg(min,max)","j721e-idk-gw: Boot time in seconds: avg(min,max)","j721s2-evm: Boot time in seconds: avg(min,max)","j722s_evm-fs: Boot time in seconds: avg(min,max)","j742s2_evm-fs: Boot time in seconds: avg(min,max)","j784s4-evm: Boot time in seconds: avg(min,max)"

   "Linux boot time from SD with default rootfs (20 boot cycles)","19.45 (min 18.86, max 23.17)","22.91 (min 21.82, max 25.82)","17.50 (min 15.52, max 20.80)","22.08 (min 20.09, max 47.31)","20.85 (min 18.68, max 56.68)","20.67 (min 19.16, max 38.53)"

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.

*********************
ALSA SoC Audio Driver
*********************

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64

.. csv-table:: Audio Capture
   :header: "Sampling Rate (Hz)","j721e-idk-gw: Throughput (bits/sec)","j721e-idk-gw: CPU Load (%)","j721s2-evm: Throughput (bits/sec)","j721s2-evm: CPU Load (%)","j722s_evm-fs: Throughput (bits/sec)","j722s_evm-fs: CPU Load (%)","j784s4-evm: Throughput (bits/sec)","j784s4-evm: CPU Load (%)"

   "11025","352791.71 (min 352790.00, max 352794.00)","0.24 (min 0.19, max 0.35)","1023977.89 (min 1023976.00, max 1023980.00)","0.56 (min 0.38, max 0.69)","179100.50 (min 75851.00, max 331813.00)","0.27 (min 0.21, max 0.32)","1023977.43 (min 1023968.00, max 1023994.00)","0.12 (min 0.06, max 0.35)"
   "16000","511990.79 (min 511988.00, max 511992.00)","0.37 (min 0.31, max 0.49)","1023987.44 (min 1023986.00, max 1023989.00)","0.93 (min 0.83, max 1.07)","422986.00 (min 244992.00, max 511983.00)","0.31 (min 0.29, max 0.34)","1023987.00 (min 1023982.00, max 1023998.00)","0.20 (min 0.06, max 0.25)"
   "22050","705574.50 (min 705572.00, max 705578.00)","0.35 (min 0.29, max 0.43)","1023973.44 (min 1023966.00, max 1023993.00)","0.53 (min 0.40, max 0.78)","564950.00 (min 367635.00, max 663609.00)","0.32 (min 0.29, max 0.34)","1023964.00 (min 1023957.00, max 1023969.00)","0.14 (min 0.10, max 0.16)"
   "24000","705581.93 (min 705580.00, max 705584.00)","0.36 (min 0.32, max 0.45)","1023984.67 (min 1023982.00, max 1023993.00)","0.63 (min 0.39, max 0.76)","564938.00 (min 367565.00, max 663625.00)","0.32 (min 0.30, max 0.35)","1023981.21 (min 1023978.00, max 1023985.00)","0.15 (min 0.13, max 0.17)"
   "32000","1023978.79 (min 1023976.00, max 1023981.00)","0.28 (min 0.21, max 0.48)","1023984.89 (min 1023983.00, max 1023989.00)","0.72 (min 0.45, max 0.84)","846154.00 (min 490544.00, max 1023960.00)","0.35 (min 0.30, max 0.38)","1023983.50 (min 1023978.00, max 1023989.00)","0.16 (min 0.11, max 0.18)"
   "44100","1411172.79 (min 1411169.00, max 1411176.00)","0.60 (min 0.53, max 0.70)","1417786.00 (min 1417761.00, max 1417795.00)","0.71 (min 0.61, max 0.75)","1129907.00 (min 735196.00, max 1327264.00)","0.38 (min 0.33, max 0.42)","1417790.21 (min 1417784.00, max 1417801.00)","0.15 (min 0.14, max 0.17)"
   "48000","1535971.50 (min 1535968.00, max 1535975.00)","0.76 (min 0.68, max 0.92)","1535950.44 (min 1535934.00, max 1535956.00)","0.71 (min 0.61, max 0.78)","1269208.33 (min 735738.00, max 1535945.00)","0.37 (min 0.33, max 0.40)","1535952.50 (min 1535948.00, max 1535963.00)","0.16 (min 0.13, max 0.18)"
   "88200","2822346.43 (min 2822340.00, max 2822352.00)","1.11 (min 1.03, max 1.25)","2835612.33 (min 2835593.00, max 2835619.00)","1.28 (min 1.20, max 1.31)","2260078.67 (min 1471209.00, max 2654516.00)","0.49 (min 0.36, max 0.56)","2835614.43 (min 2835607.00, max 2835632.00)","0.29 (min 0.26, max 0.34)"
   "96000","3071940.50 (min 3071921.00, max 3071949.00)","0.61 (min 0.50, max 0.90)","3071920.89 (min 3071905.00, max 3071926.00)","1.31 (min 1.14, max 1.40)","2538445.33 (min 1471875.00, max 3071735.00)","0.51 (min 0.38, max 0.58)","3071922.00 (min 3071914.00, max 3071941.00)","0.32 (min 0.27, max 0.38)"

.. csv-table:: Audio Playback
   :header: "Sampling Rate (Hz)","j721e-idk-gw: Throughput (bits/sec)","j721e-idk-gw: CPU Load (%)","j721s2-evm: Throughput (bits/sec)","j721s2-evm: CPU Load (%)","j722s_evm-fs: Throughput (bits/sec)","j722s_evm-fs: CPU Load (%)","j784s4-evm: Throughput (bits/sec)","j784s4-evm: CPU Load (%)"

   "11025","352937.43 (min 352936.00, max 352938.00)","0.22 (min 0.18, max 0.27)","1024399.63 (min 1024389.00, max 1024404.00)","0.47 (min 0.34, max 0.60)","154444.50 (min 75880.00, max 331951.00)","0.27 (min 0.25, max 0.31)","1024399.07 (min 1024394.00, max 1024403.00)","0.11 (min 0.06, max 0.22)"
   "16000","512202.50 (min 512201.00, max 512203.00)","0.31 (min 0.17, max 0.38)","1024409.38 (min 1024403.00, max 1024412.00)","0.64 (min 0.37, max 0.82)","334094.00 (min 244824.00, max 512198.00)","0.26 (min 0.25, max 0.27)","1024408.86 (min 1024406.00, max 1024412.00)","0.12 (min 0.06, max 0.19)"
   "22050","705866.14 (min 705862.00, max 705869.00)","0.33 (min 0.30, max 0.40)","1024388.00 (min 1024370.00, max 1024393.00)","0.61 (min 0.45, max 0.79)","466374.00 (min 367203.00, max 663886.00)","0.28 (min 0.26, max 0.32)","1024386.21 (min 1024381.00, max 1024392.00)","0.13 (min 0.09, max 0.17)"
   "24000","705873.43 (min 705871.00, max 705875.00)","0.34 (min 0.30, max 0.41)","1024404.00 (min 1024395.00, max 1024406.00)","0.49 (min 0.26, max 0.77)","466316.00 (min 366979.00, max 663903.00)","0.27 (min 0.25, max 0.30)","1024403.14 (min 1024401.00, max 1024406.00)","0.14 (min 0.07, max 0.16)"
   "32000","1024401.71 (min 1024399.00, max 1024404.00)","0.45 (min 0.22, max 0.56)","1024405.50 (min 1024396.00, max 1024408.00)","0.58 (min 0.25, max 0.81)","668315.67 (min 489566.00, max 1024388.00)","0.28 (min 0.26, max 0.31)","1024405.64 (min 1024401.00, max 1024410.00)","0.13 (min 0.06, max 0.20)"
   "44100","1411755.57 (min 1411752.00, max 1411758.00)","0.56 (min 0.51, max 0.61)","1418375.13 (min 1418348.00, max 1418383.00)","0.62 (min 0.54, max 0.75)","932652.00 (min 734279.00, max 1327819.00)","0.33 (min 0.29, max 0.37)","1418375.00 (min 1418368.00, max 1418390.00)","0.15 (min 0.14, max 0.18)"
   "48000","1536605.64 (min 1536602.00, max 1536608.00)","0.64 (min 0.31, max 0.77)","1536586.25 (min 1536563.00, max 1536593.00)","0.67 (min 0.57, max 0.77)","1002312.00 (min 733745.00, max 1536588.00)","0.30 (min 0.27, max 0.33)","1536586.14 (min 1536581.00, max 1536597.00)","0.17 (min 0.14, max 0.23)"
   "88200","2823511.64 (min 2823504.00, max 2823516.00)","1.07 (min 1.00, max 1.15)","2836784.25 (min 2836748.00, max 2836794.00)","1.19 (min 1.09, max 1.31)","1864908.00 (min 1467285.00, max 2655628.00)","0.39 (min 0.29, max 0.51)","2836784.36 (min 2836776.00, max 2836800.00)","0.29 (min 0.27, max 0.34)"
   "96000","3073210.14 (min 3073203.00, max 3073215.00)","1.08 (min 0.52, max 1.43)","3073189.38 (min 3073154.00, max 3073198.00)","1.23 (min 0.98, max 1.41)","2004372.00 (min 1467503.00, max 3073021.00)","0.36 (min 0.31, max 0.43)","3073189.07 (min 3073181.00, max 3073203.00)","0.30 (min 0.16, max 0.38)"

***************
Graphics Driver
***************

GFXBench
========

Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
   :header: "Benchmark","j721e-idk-gw: Score","j721e-idk-gw: Fps","j721s2-evm: Score","j721s2-evm: Fps","j742s2_evm-fs: Score","j742s2_evm-fs: Fps","j784s4-evm: Score","j784s4-evm: Fps"

   " GFXBench 3.x gl_manhattan_off","1175.18 (min 1129.16, max 1216.61)","18.95 (min 18.21, max 19.62)","928.24 (min 889.16, max 956.89)","14.97 (min 14.34, max 15.43)","912.99 (min 872.62, max 956.67)","14.73 (min 14.07, max 15.43)","895.80 (min 881.41, max 927.40)","14.45 (min 14.22, max 14.96)"
   " GFXBench 3.x gl_trex_off","1778.11 (min 1694.32, max 1851.00)","31.75 (min 30.26, max 33.05)","1566.37 (min 1451.82, max 1641.00)","27.97 (min 25.93, max 29.30)","1493.27 (min 1422.88, max 1587.93)","26.67 (min 25.41, max 28.36)","1485.27 (min 1436.41, max 1534.72)","26.52 (min 25.65, max 27.41)"
   " GFXBench 4.x gl_4_off","401.39 (min 388.60, max 412.86)","6.79 (min 6.58, max 6.99)","257.92 (min 250.98, max 263.93)","4.36 (min 4.25, max 4.47)","255.48 (min 250.12, max 262.40)","4.32 (min 4.23, max 4.44)","253.26 (min 250.71, max 255.97)","4.29 (min 4.24, max 4.33)"
   " GFXBench 5.x gl_5_high_off","176.72 (min 173.02, max 179.44)","2.75 (min 2.69, max 2.79)","113.99 (min 112.35, max 114.94)","1.77 (min 1.75, max 1.79)","112.55 (min 111.27, max 113.82)","1.75 (min 1.73, max 1.77)","111.22 (min 110.44, max 111.97)","1.73 (min 1.72, max 1.74)"

Glmark2
=======

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
   :header: "Benchmark","j721e-idk-gw: Score","j721s2-evm: Score","j722s_evm-fs: Score","j742s2_evm-fs: Score","j784s4-evm: Score"

   "Glmark2-DRM","45.59 (min 43.00, max 48.00)","121.55 (min 99.00, max 141.00)","291.67 (min 285.00, max 336.00)","129.19 (min 102.00, max 142.00)","164.94 (min 149.00, max 171.00)"
   "Glmark2-Wayland","1052.59 (min 763.00, max 1134.00)","1210.71 (min 1086.00, max 1415.00)","791.75 (min 740.00, max 811.00)","1273.82 (min 1206.00, max 1364.00)","1275.26 (min 1254.00, max 1319.00)"
   "Glmark2-Wayland 4000x4000","78.62 (min 69.00, max 85.00)","78.20 (min 77.00, max 83.00)","85.29 (min 83.00, max 88.00)"

********
Ethernet
********

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

CPSW/CPSW2g/CPSW3g Ethernet Driver
==================================

- CPSW2g: AM65x, J7200, J721e, J721S2, J784S4, J742S2

.. rubric::  TCP Bidirectional Throughput
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
   :header: "Command Used","j7200-evm: THROUGHPUT (Mbits/sec)","j7200-evm: CPU Load % (LOCAL_CPU_UTIL)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j721s2-evm: THROUGHPUT (Mbits/sec)","j721s2-evm: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

   "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1074.02 (min 0.00, max 1863.42)","91.65 (min 79.94, max 98.40)","1835.76 (min 1819.73, max 1854.28)","86.65 (min 79.11, max 91.76)","1425.98 (min 0.00, max 1863.91)","87.78 (min 75.63, max 99.23)","1400.96 (min 821.14, max 1858.02)","50.61 (min 34.00, max 66.05)","1824.95 (min 1812.01, max 1852.44)","59.02 (min 53.81, max 62.83)","1777.43 (min 1670.23, max 1852.12)","27.45 (min 25.24, max 29.09)"

.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
   :header: "Command Used","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

   "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1844.66 (min 1808.69, max 1871.44)","44.79 (min 32.62, max 50.47)","1249.26 (min 838.70, max 1858.49)","35.94 (min 31.92, max 40.01)","1788.32 (min 1691.27, max 1854.90)","49.05 (min 19.83, max 63.85)","1784.62 (min 1645.58, max 1876.06)","17.27 (min 11.98, max 27.89)"

.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
   :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: Packets Per Second (kPPS)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

   "64","","56.46 (min 0.00, max 93.69)","110.33 (min 0.00, max 183.00)","61.26 (min 15.03, max 84.28)","","56.39 (min 53.92, max 59.25)","110.11 (min 105.00, max 116.00)","32.81 (min 25.28, max 47.09)","","79.79 (min 78.33, max 83.28)","155.86 (min 153.00, max 163.00)","43.69 (min 43.24, max 44.62)","","83.31 (min 76.53, max 91.75)","162.67 (min 149.00, max 179.00)","22.19 (min 21.07, max 23.24)"
   "128","","88.12 (min 0.00, max 190.73)","86.00 (min 0.00, max 186.00)","49.57 (min 7.30, max 85.10)","","104.27 (min 49.66, max 116.67)","101.70 (min 48.00, max 114.00)","30.39 (min 17.06, max 39.64)","","162.64 (min 157.88, max 168.06)","158.86 (min 154.00, max 164.00)","44.43 (min 43.90, max 45.16)","","163.99 (min 155.27, max 179.60)","160.11 (min 152.00, max 175.00)","22.45 (min 21.27, max 23.09)"
   "256","","195.67 (min 19.25, max 378.61)","95.60 (min 9.00, max 185.00)","44.73 (min 1.91, max 85.39)","","222.26 (min 211.61, max 232.25)","108.33 (min 103.00, max 113.00)","25.87 (min 25.26, max 26.19)","","323.22 (min 312.05, max 339.52)","157.86 (min 152.00, max 166.00)","44.18 (min 43.52, max 45.36)","","317.22 (min 303.77, max 341.23)","154.89 (min 148.00, max 167.00)","22.31 (min 21.23, max 22.90)"
   "1024","","750.17 (min 0.00, max 938.57)","91.70 (min 0.00, max 115.00)","62.77 (min 60.53, max 64.41)","","676.85 (min 104.85, max 844.00)","82.73 (min 13.00, max 103.00)","28.89 (min 2.08, max 40.04)","","817.10 (min 521.23, max 936.51)","99.57 (min 64.00, max 114.00)","29.89 (min 18.81, max 35.64)","","936.23 (min 933.55, max 939.05)","114.22 (min 114.00, max 115.00)","17.11 (min 16.08, max 18.02)"
   "1518","","921.08 (min 918.51, max 923.68)","76.00","56.17 (min 54.25, max 58.04)","","772.00 (min 559.32, max 836.04)","63.70 (min 46.00, max 69.00)","28.08 (min 21.61, max 37.42)","","893.93 (min 704.20, max 924.22)","73.75 (min 58.00, max 76.00)","30.84 (min 28.97, max 31.86)","","921.00 (min 911.09, max 924.32)","75.89 (min 75.00, max 76.00)","14.92 (min 13.31, max 16.28)"

.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
   :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

   "64","","2.09 (min 2.00, max 2.25)","4.00","2.52 (min 1.57, max 3.58)","","2.12 (min 1.48, max 3.53)","4.25 (min 3.00, max 7.00)","0.57 (min 0.30, max 0.83)","","4.89 (min 1.43, max 12.75)","9.63 (min 3.00, max 25.00)","1.08 (min 0.13, max 3.36)"
   "128","","14.01 (min 5.12, max 50.36)","13.56 (min 5.00, max 49.00)","11.25 (min 2.21, max 41.46)","","5.94 (min 4.40, max 11.47)","5.89 (min 4.00, max 11.00)","0.99 (min 0.47, max 1.81)","","7.82 (min 4.71, max 11.88)","7.67 (min 5.00, max 12.00)","0.49 (min 0.29, max 0.77)"
   "256","","11.03 (min 10.04, max 12.29)","5.33 (min 5.00, max 6.00)","3.72 (min 2.33, max 6.05)","","16.49 (min 10.65, max 22.32)","8.00 (min 5.00, max 11.00)","0.73 (min 0.56, max 0.90)","","17.25 (min 9.62, max 46.49)","8.50 (min 5.00, max 23.00)","0.82 (min 0.32, max 2.36)"
   "1024","","47.10 (min 42.60, max 59.80)","5.75 (min 5.00, max 7.00)","5.28 (min 2.39, max 8.37)","","28.01 (min 11.28, max 43.42)","3.25 (min 1.00, max 5.00)","1.75 (min 0.38, max 3.26)","","235.68 (min 42.44, max 620.99)","28.67 (min 5.00, max 76.00)","5.73 (min 0.58, max 15.89)"
   "1518","","691.69 (min 280.25, max 956.63)","58.80 (min 24.00, max 81.00)","53.78 (min 21.17, max 77.55)","","596.91 (min 73.01, max 924.89)","50.75 (min 6.00, max 79.00)","22.66 (min 2.24, max 33.28)","","737.32 (min 560.95, max 910.42)","62.56 (min 48.00, max 77.00)","13.86 (min 10.24, max 16.81)"

.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
   :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j721e-idk-gw: Packet Loss %","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: Packet Loss %","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: Packet Loss %"

   "64","","66.19 (min 64.43, max 67.90)","129.29 (min 126.00, max 133.00)","80.93 (min 76.84, max 84.16)","2.90 (min 2.01, max 4.24)","","175.47 (min 150.06, max 197.41)","342.75 (min 293.00, max 386.00)","43.53 (min 40.30, max 44.95)","39.78 (min 6.41, max 61.49)","","166.07 (min 151.89, max 183.75)","324.50 (min 297.00, max 359.00)","22.70 (min 21.14, max 23.60)","24.37 (min 5.49, max 38.34)"
   "128","","132.37 (min 129.10, max 137.61)","129.11 (min 126.00, max 134.00)","79.27 (min 70.77, max 81.86)","2.58 (min 1.52, max 3.26)","","316.39 (min 289.57, max 386.60)","309.11 (min 283.00, max 378.00)","43.79 (min 42.58, max 45.07)","36.43 (min 10.24, max 49.78)","","331.90 (min 300.02, max 380.98)","324.11 (min 293.00, max 372.00)","22.88 (min 21.46, max 23.62)","23.67 (min 1.03, max 36.60)"
   "256","","264.63 (min 252.98, max 278.13)","129.33 (min 124.00, max 136.00)","80.96 (min 77.46, max 85.04)","2.66 (min 1.65, max 3.91)","","649.68 (min 588.86, max 710.50)","317.50 (min 288.00, max 347.00)","43.23 (min 42.62, max 43.84)","9.98 (min 3.43, max 16.53)","","522.54 (min 414.43, max 683.72)","255.00 (min 202.00, max 334.00)","19.55 (min 16.72, max 23.19)","4.38 (min 0.15, max 11.66)"
   "1024","","876.44 (min 847.74, max 907.63)","107.00 (min 103.00, max 111.00)","81.15 (min 79.01, max 83.50)","3.46 (min 2.21, max 5.04)","","785.54 (min 638.87, max 892.35)","96.00 (min 78.00, max 109.00)","34.19 (min 28.62, max 38.36)","0.31 (min 0.07, max 0.45)","","804.46 (min 615.56, max 933.25)","98.22 (min 75.00, max 114.00)","18.02 (min 15.51, max 20.08)","0.29 (min 0.00, max 0.68)"
   "1518","","946.52 (min 905.41, max 956.74)","80.30 (min 77.00, max 81.00)","76.16 (min 72.25, max 78.28)","0.04 (min 0.01, max 0.10)","","810.81 (min 575.93, max 924.89)","69.00 (min 49.00, max 79.00)","30.80 (min 21.31, max 36.42)","0.07 (min 0.00, max 0.18)","","773.14 (min 603.79, max 910.42)","65.56 (min 51.00, max 77.00)","14.57 (min 11.32, max 16.81)","0.00 (min 0.00, max 0.01)"

***********
PCIe Driver
***********

PCIe-NVMe-SSD
=============

.. rubric:: J721E-IDK-GW
   :name: j721e-idk-gw-pciessd

.. csv-table:: PCIE SSD EXT4 FIO 10G
   :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

   "1m","723.57 (min 710.00, max 741.00)","14.40 (min 13.81, max 15.31)","1478.14 (min 1007.00, max 1519.00)","8.13 (min 7.75, max 8.55)"
   "4m","721.07 (min 709.00, max 732.00)","12.68 (min 12.07, max 13.66)","1417.00 (min 741.00, max 1517.00)","5.23 (min 2.70, max 5.90)"
   "4k","173.07 (min 171.00, max 176.00)","48.81 (min 48.42, max 49.02)","127.40 (min 44.80, max 158.00)","30.18 (min 12.89, max 37.23)"
   "256k","730.86 (min 713.00, max 754.00)","16.19 (min 15.48, max 17.13)","1365.64 (min 752.00, max 1515.00)","14.20 (min 7.09, max 15.66)"

- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based
- Platform: Speed 8GT/s, Width x2
- SSD being used: PLEXTOR PX-128M8PeY

.. rubric:: J721S2-EVM
   :name: j721s2-evm-pciessd

.. csv-table:: PCIE SSD EXT4 FIO 10G
   :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

   "1m","699.75 (min 657.00, max 732.00)","16.61 (min 15.42, max 19.07)","772.00 (min 769.00, max 775.00)","4.26 (min 3.82, max 4.82)"
   "4m","709.88 (min 687.00, max 733.00)","14.07 (min 13.67, max 15.67)","775.38 (min 771.00, max 779.00)","3.05 (min 2.20, max 3.83)"
   "4k","166.00 (min 158.00, max 174.00)","49.57 (min 48.49, max 50.56)","265.50 (min 259.00, max 272.00)","50.32 (min 49.70, max 50.59)"
   "256k","689.00 (min 623.00, max 749.00)","16.57 (min 15.23, max 19.14)","779.88 (min 773.00, max 786.00)","8.03 (min 7.46, max 8.61)"

- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based
- Platform: Speed 8GT/s, Width x2
- SSD being used: PLEXTOR PX-128M8PeY

***********************
Linux OSPI Flash Driver
***********************

.. rubric:: J7200-EVM
   :name: j7200-evm-ospi

.. rubric:: UBIFS
   :name: j7200-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
   :header: "Buffer size (bytes)","j7200-evm: Write UBIFS Throughput (Mbytes/sec)","j7200-evm: Write UBIFS CPU Load (%)","j7200-evm: Read UBIFS Throughput (Mbytes/sec)","j7200-evm: Read UBIFS CPU Load (%)"

   "102400","0.17 (min 0.12, max 0.29)","50.34 (min 49.55, max 51.29)","78.03 (min 76.59, max 79.15)","29.55 (min 0.00, max 40.00)"
   "262144","0.14 (min 0.10, max 0.19)","50.49 (min 49.90, max 51.23)","76.46 (min 75.68, max 77.23)","28.48 (min 0.00, max 40.00)"
   "524288","0.14 (min 0.10, max 0.19)","50.44 (min 49.82, max 51.55)","75.51 (min 74.83, max 76.62)","31.17 (min 20.00, max 42.86)"
   "1048576","0.15 (min 0.10, max 0.19)","50.50 (min 49.87, max 51.43)","73.95 (min 73.39, max 74.81)","32.95 (min 0.00, max 40.00)"

.. rubric:: RAW
   :name: j7200-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
   :header: "File size (Mbytes)","j7200-evm: Raw Read Throughput (Mbytes/sec)"

   "50","228.45 (min 217.39, max 238.09)"

.. rubric:: J721E-IDK-GW
   :name: j721e-idk-gw-ospi

.. rubric:: UBIFS
   :name: j721e-idk-gw-ospi-ubifs

.. csv-table:: OSPI Flash Driver
   :header: "Buffer size (bytes)","j721e-idk-gw: Write UBIFS Throughput (Mbytes/sec)","j721e-idk-gw: Write UBIFS CPU Load (%)","j721e-idk-gw: Read UBIFS Throughput (Mbytes/sec)","j721e-idk-gw: Read UBIFS CPU Load (%)"

   "102400","0.69 (min 0.51, max 1.34)","53.60 (min 47.18, max 62.95)","78.54 (min 31.50, max 84.65)","35.74 (min 7.69, max 50.00)"
   "262144","0.50 (min 0.36, max 0.57)","54.40 (min 49.81, max 66.46)","77.71 (min 31.04, max 83.61)","34.23 (min 8.33, max 42.86)"
   "524288","0.50 (min 0.36, max 0.57)","52.97 (min 49.51, max 59.51)","76.81 (min 31.12, max 82.77)","34.15 (min 14.29, max 57.14)"
   "1048576","0.50 (min 0.36, max 0.57)","52.99 (min 49.12, max 60.39)","75.04 (min 30.96, max 79.92)","35.97 (min 14.29, max 50.00)"

.. rubric:: RAW
   :name: j721e-idk-gw-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
   :header: "File size (Mbytes)","j721e-idk-gw: Raw Read Throughput (Mbytes/sec)"

   "50","234.24 (min 38.46, max 263.16)"

.. rubric:: J722S-EVM
   :name: j722s-evm-ospi

.. rubric:: UBIFS
   :name: j722s-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
   :header: "Buffer size (bytes)","j722s_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Write UBIFS CPU Load (%)","j722s_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Read UBIFS CPU Load (%)"

   "102400","0.18 (min 0.11, max 0.29)","28.62 (min 24.84, max 37.67)","63.49 (min 55.35, max 65.07)","21.75 (min 8.33, max 53.85)"
   "262144","0.14 (min 0.10, max 0.19)","29.66 (min 25.37, max 35.93)","64.08 (min 61.78, max 65.47)","22.82 (min 8.33, max 28.57)"
   "524288","0.15 (min 0.09, max 0.19)","30.05 (min 26.04, max 37.28)","63.68 (min 61.76, max 65.39)","18.27 (min 0.00, max 26.67)"
   "1048576","0.15 (min 0.10, max 0.19)","29.69 (min 26.45, max 37.86)","62.59 (min 60.68, max 64.01)","21.39 (min 8.33, max 26.67)"

.. rubric:: RAW
   :name: j722s-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
   :header: "File size (Mbytes)","j722s_evm-fs: Raw Read Throughput (Mbytes/sec)"

   "50","221.56 (min 208.33, max 227.27)"

.. rubric:: J742S2-EVM
   :name: j742s2-evm-ospi

.. rubric:: UBIFS
   :name: j742s2-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
   :header: "Buffer size (bytes)","j742s2_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j742s2_evm-fs: Write UBIFS CPU Load (%)","j742s2_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j742s2_evm-fs: Read UBIFS CPU Load (%)"

   "102400","0.18 (min 0.12, max 0.31)","27.28 (min 23.95, max 31.13)","74.81 (min 70.59, max 77.89)","17.79 (min 9.09, max 33.33)"
   "262144","0.14 (min 0.10, max 0.20)","27.71 (min 25.20, max 31.34)","74.78 (min 71.10, max 77.87)","16.88 (min 10.00, max 25.00)"
   "524288","0.14 (min 0.10, max 0.20)","27.70 (min 25.00, max 32.30)","74.42 (min 68.87, max 79.27)","21.25 (min 9.09, max 27.27)"
   "1048576","0.14 (min 0.10, max 0.20)","27.99 (min 25.74, max 31.37)","73.57 (min 70.21, max 76.58)","17.91 (min 3.23, max 25.00)"

.. rubric:: RAW
   :name: j742s2-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
   :header: "File size (Mbytes)","j742s2_evm-fs: Raw Read Throughput (Mbytes/sec)"

   "50","252.86 (min 200.00, max 263.16)"

.. rubric:: J784S4-EVM
   :name: j784s4-evm-ospi

.. rubric:: UBIFS
   :name: j784s4-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
   :header: "Buffer size (bytes)","j784s4-evm: Write UBIFS Throughput (Mbytes/sec)","j784s4-evm: Write UBIFS CPU Load (%)","j784s4-evm: Read UBIFS Throughput (Mbytes/sec)","j784s4-evm: Read UBIFS CPU Load (%)"

   "102400","0.18 (min 0.12, max 0.29)","14.13 (min 12.29, max 17.17)","73.61 (min 69.78, max 77.98)","9.23 (min 4.17, max 15.38)"
   "262144","0.14 (min 0.10, max 0.19)","14.52 (min 12.48, max 17.19)","76.56 (min 71.21, max 80.73)","7.46 (min 4.35, max 13.04)"
   "524288","0.15 (min 0.10, max 0.19)","14.76 (min 12.78, max 17.29)","73.05 (min 70.05, max 79.02)","9.43 (min 4.35, max 15.38)"
   "1048576","0.15 (min 0.10, max 0.19)","14.66 (min 12.46, max 16.92)","72.38 (min 68.25, max 77.00)","8.70 (min 4.17, max 12.00)"

.. rubric:: RAW
   :name: j784s4-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
   :header: "File size (Mbytes)","j784s4-evm: Raw Read Throughput (Mbytes/sec)"

   "50","249.03 (min 185.19, max 263.16)"

**********************
UBoot QSPI/OSPI Driver
**********************

.. rubric:: J721E-IDK-GW
   :name: j721e-idk-gw-uboot-qspi

.. csv-table:: UBOOT QSPI or OSPI
   :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

   "400000","1031.02 (min 1018.15, max 1041.18)","15847.68 (min 15814.67, max 15875.97)"
   "800000","1031.91 (min 1019.03, max 1042.11)","16055.49 (min 16031.31, max 16062.75)"
   "1000000","1032.22 (min 1019.67, max 1042.37)","16167.61 (min 16157.79, max 16173.74)"
   "2000000","1032.32 (min 1019.83, max 1042.64)","16220.55 (min 16213.76, max 16221.78)"

.. rubric:: J721S2-EVM
   :name: j721s2-evm-uboot-qspi

.. csv-table:: UBOOT QSPI or OSPI
   :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

   "400000","996.83 (min 981.55, max 1002.94)","15845.32 (min 15814.67, max 15875.97)"
   "800000","997.67 (min 982.73, max 1003.55)","16060.50 (min 16031.31, max 16062.75)"
   "1000000","997.82 (min 983.02, max 1003.74)","16163.49 (min 16157.79, max 16173.74)"
   "2000000","998.15 (min 982.99, max 1004.44)","16220.06 (min 16213.76, max 16221.78)"

.. rubric:: J742S2-EVM
   :name: j742s2-evm-uboot-qspi

.. csv-table:: UBOOT QSPI or OSPI
   :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

   "400000","981.85 (min 976.40, max 1000.49)","15849.70 (min 15814.67, max 15875.97)"
   "800000","982.27 (min 976.17, max 1001.47)","16058.26 (min 16031.31, max 16062.75)"
   "1000000","982.65 (min 976.63, max 1001.71)","16161.21 (min 16157.79, max 16173.74)"
   "2000000","983.01 (min 978.50, max 1002.17)","16220.06 (min 16213.76, max 16221.78)"

.. rubric:: J784S4-EVM
   :name: j784s4-evm-uboot-qspi

.. csv-table:: UBOOT QSPI or OSPI
   :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

   "400000","997.14 (min 982.73, max 1026.57)","15832.18 (min 15814.67, max 15875.97)"
   "800000","998.17 (min 983.08, max 1027.85)","16058.26 (min 16031.31, max 16062.75)"
   "1000000","998.46 (min 983.49, max 1028.18)","16164.63 (min 16157.79, max 16173.74)"
   "2000000","998.44 (min 983.32, max 1028.60)","16221.21 (min 16213.76, max 16221.78)"

****************
UBoot UFS Driver
****************

.. rubric:: J721E-IDK-GW
   :name: j721e-idk-gw-uboot-ufs-raw

.. csv-table:: UBOOT UFS RAW
   :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

   "400000","103863.61 (min 73142.86, max 215578.95)","366721.77 (min 341333.33, max 372363.64)"
   "800000","108063.03 (min 88086.02, max 195047.62)","506524.06 (min 481882.35, max 512000.00)"
   "1000000","112801.43 (min 93622.86, max 234057.14)","617593.20 (min 606814.81, max 655360.00)"

.. rubric:: J742S2-EVM
   :name: j742s2-evm-uboot-ufs-raw

.. csv-table:: UBOOT UFS RAW
   :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

   "400000","91690.14 (min 75851.85, max 97523.81)","359951.52 (min 341333.33, max 372363.64)"
   "800000","98729.83 (min 88086.02, max 102400.00)","508988.24 (min 481882.35, max 512000.00)"
   "1000000","100609.80 (min 93622.86, max 105025.64)","609148.71 (min 606814.81, max 630153.85)"

.. rubric:: J784S4-EVM
   :name: j784s4-evm-emmc-raw

.. csv-table:: UBOOT UFS RAW
   :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

   "400000","93315.96 (min 87148.94, max 102400.00)","369542.70 (min 341333.33, max 372363.64)"
   "800000","99199.54 (min 88086.02, max 102400.00)","503786.10 (min 481882.35, max 512000.00)"
   "1000000","99604.93 (min 94160.92, max 105025.64)","619545.20 (min 606814.81, max 630153.85)"

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
   :header: "Buffer size (bytes)","j7200-evm: Write EXT4 Throughput (Mbytes/sec)","j7200-evm: Write EXT4 CPU Load (%)","j7200-evm: Read EXT4 Throughput (Mbytes/sec)","j7200-evm: Read EXT4 CPU Load (%)"

   "1m","56.32 (min 44.90, max 60.80)","1.66 (min 1.28, max 1.92)","312.00 (min 306.00, max 315.00)","1.95 (min 1.81, max 2.10)"
   "4m","56.30 (min 44.90, max 61.00)","1.41 (min 1.12, max 1.63)","308.00 (min 301.00, max 314.00)","1.22 (min 1.05, max 1.40)"
   "4k","42.83 (min 5.26, max 58.10)","19.40 (min 2.61, max 27.12)","50.81 (min 36.10, max 56.40)","19.04 (min 13.68, max 21.29)"
   "256k","53.93 (min 36.10, max 60.80)","1.86 (min 1.22, max 2.26)","308.27 (min 288.00, max 317.00)","3.81 (min 3.59, max 4.00)"

.. csv-table:: EMMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

   "1m","60.40 (min 58.40, max 61.50)","1.57 (min 1.40, max 1.83)","175.00","1.31 (min 1.21, max 1.53)"
   "4m","60.20 (min 57.80, max 61.40)","1.36 (min 1.16, max 1.61)","175.00","0.87 (min 0.72, max 1.08)"
   "4k","50.25 (min 49.40, max 50.60)","21.83 (min 21.53, max 22.07)","56.46 (min 56.00, max 56.90)","20.50 (min 19.98, max 20.75)"
   "256k","60.47 (min 58.70, max 61.20)","2.02 (min 1.84, max 2.22)","174.00","2.37 (min 2.17, max 2.59)"

.. csv-table:: EMMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

   "1m","71.59 (min 45.00, max 96.70)","2.24 (min 1.44, max 3.25)","300.36 (min 282.00, max 315.00)","2.01 (min 1.76, max 2.21)"
   "4m","71.86 (min 45.30, max 97.10)","1.64 (min 1.19, max 2.34)","276.29 (min 165.00, max 314.00)","1.20 (min 0.93, max 1.44)"
   "4k","53.77 (min 5.22, max 82.60)","25.94 (min 2.76, max 40.21)","66.45 (min 36.20, max 93.60)","26.36 (min 14.71, max 36.95)"
   "256k","69.08 (min 36.20, max 96.70)","2.57 (min 1.50, max 3.53)","295.07 (min 276.00, max 317.00)","3.84 (min 3.59, max 4.03)"

.. csv-table:: EMMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

   "1m","93.39 (min 78.00, max 97.60)","1.77 (min 1.41, max 1.97)","260.25 (min 113.00, max 296.00)","2.75 (min 1.36, max 3.32)"
   "4m","93.59 (min 78.40, max 98.10)","1.29 (min 1.05, max 1.41)","235.75 (min 112.00, max 295.00)","2.00 (min 1.15, max 2.43)"
   "4k","69.74 (min 8.57, max 83.90)","21.70 (min 3.20, max 26.13)","82.70 (min 56.60, max 90.90)","19.45 (min 14.50, max 21.33)"
   "256k","91.65 (min 68.70, max 97.60)","2.18 (min 1.69, max 2.46)","256.15 (min 94.80, max 296.00)","3.86 (min 1.51, max 4.50)"

.. csv-table:: EMMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","j742s2_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Write EXT4 CPU Load (%)","j742s2_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Read EXT4 CPU Load (%)"

   "1m","96.57 (min 95.90, max 98.00)","1.02 (min 0.94, max 1.12)","290.55 (min 280.00, max 294.00)","0.84 (min 0.76, max 0.91)"
   "4m","95.71 (min 86.80, max 98.50)","1.01 (min 0.92, max 1.11)","270.18 (min 156.00, max 294.00)","0.46 (min 0.30, max 0.52)"
   "4k","82.79 (min 82.50, max 84.30)","20.64 (min 20.05, max 21.93)","85.46 (min 77.00, max 92.40)","16.68 (min 14.86, max 17.89)"
   "256k","96.59 (min 95.90, max 98.10)","1.06 (min 1.00, max 1.17)","292.64 (min 292.00, max 294.00)","1.86 (min 1.76, max 2.03)"

.. csv-table:: EMMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

   "1m","93.01 (min 79.00, max 97.90)","0.48 (min 0.42, max 0.54)","253.79 (min 113.00, max 296.00)","0.40 (min 0.21, max 0.52)"
   "4m","93.46 (min 79.60, max 98.30)","0.45 (min 0.40, max 0.53)","229.75 (min 96.70, max 296.00)","0.22 (min 0.11, max 0.29)"
   "4k","67.03 (min 8.63, max 83.20)","9.27 (min 1.32, max 12.08)","84.82 (min 56.50, max 94.10)","9.06 (min 5.81, max 10.35)"
   "256k","91.10 (min 70.50, max 97.90)","0.57 (min 0.43, max 0.71)","251.26 (min 94.80, max 296.00)","0.88 (min 0.33, max 1.28)"

EMMC RAW FIO 1G
===============

.. csv-table:: EMMC RAW FIO 1G
   :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

   "1m","55.23 (min 45.00, max 61.00)","1.59 (min 1.24, max 1.93)","311.80 (min 305.00, max 315.00)","1.90 (min 1.64, max 2.07)"
   "4m","54.93 (min 44.90, max 61.00)","1.45 (min 1.08, max 3.15)","295.40 (min 245.00, max 314.00)","1.12 (min 1.00, max 1.31)"
   "4k","38.57 (min 5.30, max 56.50)","13.69 (min 2.05, max 19.88)","49.60 (min 36.00, max 56.40)","17.05 (min 12.56, max 19.50)"
   "256k","52.39 (min 36.10, max 61.00)","1.66 (min 1.22, max 2.10)","306.47 (min 288.00, max 317.00)","3.64 (min 3.32, max 3.92)"

.. csv-table:: EMMC RAW FIO 1G
   :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

   "1m","58.26 (min 43.80, max 61.30)","1.42 (min 1.11, max 1.67)","175.00","1.25 (min 1.15, max 1.38)"
   "4m","58.36 (min 44.20, max 61.60)","1.23 (min 0.90, max 1.44)","175.00","0.79 (min 0.70, max 0.93)"
   "4k","45.91 (min 5.44, max 53.10)","15.92 (min 2.14, max 18.44)","53.54 (min 36.00, max 56.90)","17.82 (min 12.04, max 19.25)"
   "256k","56.96 (min 34.70, max 61.40)","1.72 (min 1.23, max 1.96)","174.00","2.19 (min 2.05, max 2.33)"

.. csv-table:: EMMC RAW FIO 1G
   :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

   "1m","61.08 (min 44.90, max 96.60)","1.84 (min 1.35, max 2.93)","308.27 (min 294.00, max 316.00)","2.00 (min 1.81, max 2.23)"
   "4m","61.21 (min 45.20, max 97.10)","1.47 (min 1.04, max 2.26)","300.87 (min 258.00, max 315.00)","1.24 (min 1.09, max 1.44)"
   "4k","45.64 (min 5.22, max 83.60)","17.41 (min 2.33, max 31.65)","55.85 (min 36.20, max 93.60)","20.45 (min 13.37, max 33.85)"
   "256k","58.71 (min 36.20, max 96.70)","2.10 (min 1.40, max 3.27)","302.73 (min 284.00, max 317.00)","3.73 (min 3.52, max 3.86)"

.. csv-table:: EMMC RAW FIO 1G
   :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

   "1m","93.04 (min 78.00, max 97.80)","1.60 (min 1.28, max 1.76)","260.88 (min 112.00, max 296.00)","2.73 (min 1.43, max 3.31)"
   "4m","93.94 (min 78.20, max 98.30)","1.21 (min 1.01, max 1.36)","246.33 (min 95.20, max 296.00)","2.02 (min 1.05, max 2.41)"
   "4k","68.40 (min 8.58, max 82.70)","16.13 (min 2.45, max 19.51)","86.84 (min 56.60, max 94.30)","19.31 (min 13.48, max 20.97)"
   "256k","91.25 (min 68.50, max 97.80)","1.96 (min 1.30, max 2.19)","257.56 (min 94.30, max 296.00)","3.65 (min 1.66, max 4.34)"

.. csv-table:: EMMC RAW FIO 1G
   :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

   "1m","91.96 (min 67.80, max 97.60)","0.94 (min 0.72, max 1.28)","280.71 (min 112.00, max 295.00)","0.82 (min 0.38, max 1.01)"
   "4m","93.86 (min 79.40, max 97.90)","0.95 (min 0.76, max 1.03)","231.86 (min 112.00, max 295.00)","0.47 (min 0.23, max 1.00)"
   "4k","73.12 (min 7.73, max 83.40)","14.54 (min 1.67, max 17.12)","90.04 (min 59.00, max 94.20)","16.81 (min 11.69, max 17.70)"
   "256k","90.31 (min 68.50, max 97.60)","0.96 (min 0.73, max 1.19)","279.59 (min 94.30, max 295.00)","1.68 (min 0.66, max 1.88)"

.. csv-table:: EMMC RAW FIO 1G
   :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

   "1m","93.29 (min 79.00, max 98.00)","0.45 (min 0.37, max 0.50)","268.36 (min 112.00, max 296.00)","0.45 (min 0.19, max 0.66)"
   "4m","93.66 (min 71.40, max 98.50)","0.44 (min 0.38, max 0.48)","242.79 (min 111.00, max 296.00)","0.22 (min 0.13, max 0.30)"
   "4k","71.64 (min 6.13, max 83.20)","7.22 (min 0.61, max 9.02)","87.86 (min 56.70, max 93.70)","8.54 (min 5.43, max 9.39)"
   "256k","92.35 (min 69.40, max 98.00)","0.52 (min 0.42, max 0.69)","266.36 (min 94.50, max 296.00)","0.88 (min 0.34, max 1.29)"

*****************
UBoot EMMC Driver
*****************

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

   "2000000","60126.42 (min 59041.44, max 61248.60)","307054.04 (min 292571.43, max 312076.19)"
   "4000000","60741.40 (min 59148.01, max 61651.93)","313779.92 (min 299251.14, max 326049.75)"

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

   "2000000","60409.68 (min 59254.97, max 61593.98)","173607.84 (min 172463.16, max 175229.95)"
   "4000000","61225.70 (min 59959.74, max 62894.43)","177445.85 (min 176172.04, max 178572.21)"

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

   "2000000","59412.59 (min 57893.99, max 61593.98)","307406.06 (min 289982.30, max 312076.19)"
   "4000000","60182.10 (min 59308.60, max 61536.15)","308329.70 (min 245453.18, max 322837.44)"

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","j722s_evm-fs: Write Throughput (Kbytes/sec)","j722s_evm-fs: Read Throughput (Kbytes/sec)"

   "2000000","96671.07 (min 91275.77, max 103044.03)","162926.30 (min 95255.81, max 173375.66)"
   "4000000","97111.21 (min 90145.80, max 100669.74)","168712.69 (min 123886.58, max 175699.73)"

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

   "2000000","98707.38 (min 96093.84, max 104025.40)","262381.33 (min 99598.78, max 284939.13)"
   "4000000","98338.10 (min 96234.95, max 100669.74)","272751.81 (min 145635.56, max 293883.41)"

.. csv-table:: UBOOT EMMC RAW
   :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

   "2000000","96917.91 (min 93356.13, max 103369.09)","277208.04 (min 248242.42, max 315076.92)"
   "4000000","98357.70 (min 95953.15, max 101763.98)","278678.23 (min 214872.13, max 310597.16)"

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
   :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

   "1m","33.92 (min 32.60, max 34.90)","1.17 (min 1.08, max 1.28)","43.29 (min 42.30, max 43.50)","0.68 (min 0.62, max 0.75)"
   "4m","33.49 (min 32.10, max 34.40)","0.93 (min 0.84, max 1.03)","43.20 (min 41.60, max 43.50)","0.56 (min 0.47, max 0.70)"
   "4k","2.77 (min 2.75, max 2.80)","2.11 (min 1.97, max 2.23)","11.23 (min 11.20, max 11.40)","5.28 (min 5.17, max 5.47)"
   "256k","31.61 (min 30.60, max 33.50)","1.39 (min 1.22, max 1.52)","42.54 (min 42.40, max 42.90)","0.91 (min 0.82, max 0.98)"

.. csv-table:: MMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","j7200-evm: Write EXT4 Throughput (Mbytes/sec)","j7200-evm: Write EXT4 CPU Load (%)","j7200-evm: Read EXT4 Throughput (Mbytes/sec)","j7200-evm: Read EXT4 CPU Load (%)"

   "1m","43.37 (min 41.20, max 46.70)","1.55 (min 1.46, max 1.63)","86.81 (min 85.10, max 87.50)","1.10 (min 0.94, max 1.25)"
   "4m","42.86 (min 40.80, max 46.20)","1.27 (min 1.18, max 1.40)","86.41 (min 82.30, max 87.40)","0.73 (min 0.63, max 0.82)"
   "4k","2.69 (min 2.29, max 2.82)","2.26 (min 1.94, max 2.41)","12.07 (min 9.25, max 13.00)","6.00 (min 4.66, max 6.57)"
   "256k","38.02 (min 35.90, max 40.00)","1.64 (min 1.55, max 1.90)","83.02 (min 80.30, max 84.30)","1.47 (min 1.38, max 1.58)"

.. csv-table:: MMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

   "1m","42.54 (min 42.00, max 43.70)","1.73 (min 1.56, max 1.93)","87.50 (min 87.20, max 88.20)","1.22 (min 1.05, max 1.41)"
   "4m","41.91 (min 40.20, max 43.20)","1.36 (min 1.17, max 1.57)","86.14 (min 82.10, max 87.30)","0.86 (min 0.72, max 1.14)"
   "4k","2.80 (min 2.79, max 2.83)","2.55 (min 2.39, max 2.78)","12.89 (min 12.80, max 13.00)","7.02 (min 6.78, max 7.26)"
   "256k","38.17 (min 37.00, max 40.50)","1.93 (min 1.72, max 2.21)","83.84 (min 83.20, max 84.50)","1.60 (min 1.45, max 1.85)"

.. csv-table:: MMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

   "1m","42.30 (min 41.20, max 43.40)","1.31 (min 1.18, max 1.39)","87.06 (min 85.10, max 87.40)","1.55 (min 1.41, max 1.73)"
   "4m","42.21 (min 40.80, max 43.30)","0.94 (min 0.86, max 1.05)","86.98 (min 85.00, max 87.40)","1.15 (min 1.07, max 1.26)"
   "4k","2.78 (min 2.77, max 2.82)","1.92 (min 1.80, max 2.07)","12.98 (min 12.90, max 13.10)","4.54 (min 4.33, max 4.79)"
   "256k","38.09 (min 36.70, max 39.60)","1.51 (min 1.38, max 1.64)","83.73 (min 83.20, max 84.40)","1.77 (min 1.64, max 1.84)"

.. csv-table:: MMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","j742s2_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Write EXT4 CPU Load (%)","j742s2_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Read EXT4 CPU Load (%)"

   "1m","42.24 (min 41.50, max 42.80)","0.63 (min 0.47, max 0.69)","87.35 (min 87.20, max 87.60)","0.46 (min 0.39, max 0.55)"
   "4m","41.88 (min 40.90, max 42.70)","0.57 (min 0.51, max 0.64)","87.24 (min 86.80, max 87.40)","0.32 (min 0.26, max 0.35)"
   "4k","2.78 (min 2.75, max 2.84)","1.29 (min 1.11, max 1.44)","12.87 (min 12.70, max 13.00)","3.82 (min 3.27, max 4.24)"
   "256k","36.67 (min 35.20, max 38.00)","0.62 (min 0.56, max 0.67)","83.59 (min 83.30, max 84.00)","0.71 (min 0.65, max 0.77)"

.. csv-table:: MMC EXT4 FIO 1G
   :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

   "1m","43.03 (min 41.30, max 46.00)","0.30 (min 0.25, max 0.34)","87.12 (min 85.40, max 88.20)","0.26 (min 0.21, max 0.31)"
   "4m","42.82 (min 41.50, max 45.30)","0.28 (min 0.25, max 0.33)","86.69 (min 82.80, max 87.50)","0.17 (min 0.14, max 0.21)"
   "4k","2.73 (min 2.37, max 2.82)","0.62 (min 0.51, max 0.71)","12.40 (min 9.78, max 13.10)","1.70 (min 1.47, max 1.83)"
   "256k","37.59 (min 36.00, max 41.60)","0.32 (min 0.30, max 0.36)","83.23 (min 80.70, max 84.50)","0.35 (min 0.33, max 0.38)"

MMC RAW FIO 1G
==============

.. csv-table:: MMC RAW FIO 1G
   :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

   "1m","43.91 (min 42.20, max 47.30)","1.39 (min 1.22, max 1.52)","87.91 (min 86.40, max 88.30)","0.91 (min 0.87, max 0.96)"
   "4m","43.63 (min 41.30, max 47.10)","1.24 (min 1.08, max 1.32)","87.83 (min 86.10, max 88.30)","0.70 (min 0.61, max 0.77)"
   "4k","2.74 (min 2.25, max 2.83)","1.93 (min 1.61, max 2.09)","12.48 (min 9.38, max 13.00)","5.85 (min 4.45, max 6.28)"
   "256k","37.71 (min 36.10, max 41.40)","1.47 (min 1.31, max 1.58)","83.84 (min 80.80, max 84.50)","1.41 (min 1.32, max 1.52)"

.. csv-table:: MMC RAW FIO 1G
   :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

   "1m","34.56 (min 33.00, max 36.50)","1.03 (min 0.92, max 1.16)","43.87 (min 43.80, max 43.90)","0.65 (min 0.56, max 0.79)"
   "4m","33.96 (min 32.50, max 35.60)","0.93 (min 0.80, max 0.98)","43.83 (min 43.80, max 43.90)","0.52 (min 0.45, max 0.62)"
   "4k","2.79 (min 2.77, max 2.80)","1.89 (min 1.77, max 2.03)","11.29 (min 11.20, max 11.30)","4.97 (min 4.85, max 5.20)"
   "256k","32.12 (min 29.80, max 35.00)","1.23 (min 1.08, max 1.44)","42.90","0.88 (min 0.80, max 0.96)"

.. csv-table:: MMC RAW FIO 1G
   :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

   "1m","43.46 (min 42.40, max 45.10)","1.64 (min 1.46, max 1.80)","88.20 (min 88.10, max 88.30)","1.08 (min 1.01, max 1.14)"
   "4m","43.16 (min 41.60, max 45.00)","1.32 (min 1.17, max 1.52)","88.16 (min 88.00, max 88.30)","0.82 (min 0.75, max 0.89)"
   "4k","2.82 (min 2.81, max 2.82)","2.23 (min 2.07, max 2.42)","13.03 (min 13.00, max 13.10)","6.62 (min 6.38, max 6.78)"
   "256k","38.18 (min 36.00, max 41.60)","1.75 (min 1.67, max 1.93)","84.36 (min 84.20, max 84.50)","1.52 (min 1.45, max 1.67)"

.. csv-table:: MMC RAW FIO 1G
   :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

   "1m","43.28 (min 41.90, max 45.00)","1.15 (min 1.07, max 1.23)","88.16 (min 88.10, max 88.30)","1.43 (min 1.28, max 1.52)"
   "4m","43.08 (min 41.20, max 45.10)","0.90 (min 0.81, max 0.96)","88.13 (min 88.00, max 88.30)","1.11 (min 1.03, max 1.25)"
   "4k","2.81 (min 2.80, max 2.82)","1.59 (min 1.54, max 1.71)","13.03 (min 13.00, max 13.10)","4.18 (min 4.05, max 4.33)"
   "256k","37.65 (min 35.90, max 41.30)","1.27 (min 1.15, max 1.37)","84.35 (min 84.20, max 84.50)","1.72 (min 1.64, max 1.80)"

.. csv-table:: MMC RAW FIO 1G
   :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

   "1m","43.34 (min 42.00, max 45.10)","0.57 (min 0.51, max 0.64)","88.23 (min 88.10, max 88.30)","0.40 (min 0.36, max 0.45)"
   "4m","42.91 (min 42.00, max 44.50)","0.57 (min 0.52, max 0.61)","88.18 (min 88.00, max 88.30)","0.30 (min 0.24, max 0.35)"
   "4k","2.81 (min 2.79, max 2.83)","1.15 (min 0.95, max 1.31)","13.06 (min 13.00, max 13.10)","3.63 (min 3.14, max 4.08)"
   "256k","37.94 (min 36.00, max 41.50)","0.60 (min 0.52, max 0.67)","84.39 (min 84.20, max 84.50)","0.69 (min 0.62, max 0.75)"

.. csv-table:: MMC RAW FIO 1G
   :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

   "1m","43.90 (min 42.40, max 47.10)","0.28 (min 0.25, max 0.32)","88.12 (min 86.40, max 88.30)","0.21 (min 0.18, max 0.25)"
   "4m","43.80 (min 42.30, max 47.10)","0.28 (min 0.26, max 0.32)","88.09 (min 86.40, max 88.30)","0.16 (min 0.14, max 0.21)"
   "4k","2.78 (min 2.24, max 2.83)","0.53 (min 0.42, max 0.60)","12.79 (min 9.40, max 13.10)","1.66 (min 1.13, max 1.79)"
   "256k","38.34 (min 36.40, max 41.60)","0.30 (min 0.25, max 0.36)","84.21 (min 81.20, max 84.50)","0.33 (min 0.31, max 0.37)"

MMC EXT4
========

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

   "102400","37.53 (min 33.75, max 43.21)","3.13 (min 2.33, max 4.56)","76.83 (min 72.19, max 81.46)","4.69 (min 4.01, max 5.54)"
   "262144","38.25 (min 35.48, max 42.02)","3.29 (min 2.47, max 4.96)","84.55 (min 77.77, max 87.44)","4.99 (min 3.42, max 6.57)"
   "524288","38.91 (min 36.79, max 42.85)","3.13 (min 2.56, max 4.66)","90.91 (min 89.43, max 91.33)","5.20 (min 4.37, max 6.24)"
   "1048576","38.21 (min 36.81, max 41.43)","3.05 (min 2.34, max 4.61)","90.73 (min 88.86, max 91.33)","5.33 (min 4.81, max 5.86)"
   "5242880","38.89 (min 36.47, max 42.17)","3.07 (min 2.44, max 4.46)","91.05 (min 89.07, max 91.36)","5.08 (min 4.39, max 5.59)"

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

   "102400","30.84 (min 27.44, max 35.49)","2.86 (min 2.16, max 4.57)","40.56 (min 39.22, max 43.16)","2.37 (min 1.86, max 3.38)"
   "262144","30.75 (min 27.95, max 34.09)","2.88 (min 2.17, max 4.19)","41.74 (min 39.84, max 43.55)","2.28 (min 1.91, max 2.82)"
   "524288","31.21 (min 28.77, max 35.37)","2.86 (min 2.20, max 4.17)","45.25 (min 42.30, max 45.86)","2.59 (min 2.19, max 2.84)"
   "1048576","31.75 (min 29.81, max 34.83)","2.80 (min 1.93, max 4.40)","45.79 (min 45.37, max 45.90)","2.76 (min 2.20, max 3.06)"
   "5242880","32.06 (min 29.27, max 35.59)","2.81 (min 2.06, max 4.43)","45.73 (min 45.26, max 45.89)","2.76 (min 2.21, max 3.23)"

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

   "102400","38.38 (min 34.64, max 44.59)","3.67 (min 2.89, max 5.68)","76.45 (min 66.32, max 81.72)","4.71 (min 3.33, max 5.79)"
   "262144","38.69 (min 35.36, max 44.06)","3.74 (min 2.87, max 5.87)","83.69 (min 77.00, max 88.29)","4.85 (min 3.79, max 6.25)"
   "524288","39.21 (min 36.26, max 43.43)","3.75 (min 2.73, max 6.29)","89.84 (min 81.29, max 92.09)","5.31 (min 3.48, max 6.14)"
   "1048576","40.38 (min 36.84, max 44.20)","3.79 (min 2.76, max 5.57)","90.75 (min 82.14, max 92.05)","6.12 (min 5.29, max 6.93)"
   "5242880","39.49 (min 36.80, max 43.85)","3.71 (min 2.90, max 5.85)","91.51 (min 89.59, max 92.11)","6.33 (min 5.70, max 6.96)"

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

   "102400","38.67 (min 34.70, max 44.04)","3.61 (min 2.69, max 5.94)","77.90 (min 71.25, max 81.68)","5.01 (min 3.54, max 6.32)"
   "262144","38.02 (min 35.94, max 41.90)","3.68 (min 2.61, max 5.52)","84.68 (min 80.79, max 88.28)","5.09 (min 4.28, max 5.86)"
   "524288","39.44 (min 36.57, max 43.37)","3.58 (min 2.42, max 5.43)","91.32 (min 90.63, max 91.73)","5.55 (min 4.80, max 6.96)"
   "1048576","39.78 (min 36.76, max 42.90)","3.62 (min 2.57, max 5.41)","91.29 (min 89.72, max 91.91)","5.52 (min 4.35, max 6.14)"
   "5242880","39.58 (min 36.81, max 43.79)","3.55 (min 2.57, max 5.36)","91.24 (min 89.05, max 91.90)","5.45 (min 4.82, max 6.55)"

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

   "102400","39.16 (min 35.45, max 43.55)","0.94 (min 0.64, max 1.33)","76.00 (min 70.32, max 81.53)","1.22 (min 0.88, max 1.74)"
   "262144","38.17 (min 35.83, max 42.66)","0.90 (min 0.59, max 1.35)","83.38 (min 78.22, max 88.38)","1.08 (min 0.87, max 1.41)"
   "524288","40.15 (min 37.08, max 43.31)","0.93 (min 0.71, max 1.58)","91.72 (min 89.38, max 92.27)","1.18 (min 0.75, max 1.64)"
   "1048576","39.46 (min 36.46, max 43.38)","0.87 (min 0.59, max 1.42)","91.06 (min 89.74, max 92.18)","1.22 (min 0.98, max 1.53)"
   "5242880","39.80 (min 37.47, max 45.63)","0.89 (min 0.63, max 1.38)","91.60 (min 90.17, max 92.17)","1.23 (min 1.08, max 1.43)"

.. csv-table:: MMC EXT4
   :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

   "102400","38.68 (min 33.66, max 43.37)","1.76 (min 1.32, max 2.72)","77.04 (min 72.91, max 81.73)","2.29 (min 0.91, max 2.87)"
   "262144","38.43 (min 36.30, max 41.49)","1.81 (min 1.40, max 2.66)","82.85 (min 78.60, max 88.36)","2.10 (min 1.74, max 2.43)"
   "524288","39.43 (min 37.35, max 42.47)","1.81 (min 1.27, max 3.06)","91.28 (min 89.67, max 92.14)","2.26 (min 1.74, max 2.63)"
   "1048576","39.38 (min 36.97, max 42.88)","1.74 (min 1.31, max 2.52)","91.56 (min 90.00, max 92.21)","2.43 (min 1.98, max 3.04)"
   "5242880","39.28 (min 37.54, max 42.57)","1.72 (min 1.21, max 2.53)","91.73 (min 89.94, max 92.18)","2.55 (min 2.18, max 3.03)"

MMC EXT2
========

.. csv-table:: MMC EXT2
   :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

   "102400","39.71 (min 33.62, max 42.84)","3.72 (min 2.82, max 6.09)","79.02 (min 76.18, max 80.71)","5.10 (min 4.08, max 5.94)"
   "262144","37.93 (min 32.50, max 42.42)","3.48 (min 2.51, max 6.19)","84.76 (min 81.72, max 86.81)","5.52 (min 4.38, max 6.24)"
   "524288","37.13 (min 32.44, max 41.68)","3.41 (min 2.43, max 5.85)","89.27 (min 85.08, max 90.53)","5.43 (min 4.91, max 5.88)"
   "1048576","37.85 (min 32.65, max 41.90)","3.43 (min 2.51, max 6.11)","89.96 (min 84.98, max 90.43)","5.42 (min 4.76, max 5.83)"
   "5242880","37.81 (min 32.90, max 41.98)","3.39 (min 2.41, max 6.02)","89.99 (min 85.36, max 90.54)","5.38 (min 4.56, max 6.06)"

.. csv-table:: MMC EXT2
   :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

   "102400","32.73 (min 28.11, max 35.59)","3.45 (min 2.37, max 6.20)","42.32 (min 41.71, max 43.01)","2.50 (min 2.00, max 3.06)"
   "262144","30.62 (min 28.25, max 34.31)","3.11 (min 2.07, max 6.02)","43.91 (min 43.35, max 44.81)","2.61 (min 2.08, max 3.39)"
   "524288","31.02 (min 28.27, max 34.34)","3.17 (min 2.33, max 5.85)","45.02 (min 44.24, max 45.73)","2.67 (min 2.19, max 3.16)"
   "1048576","30.40 (min 28.46, max 33.20)","3.05 (min 2.05, max 5.75)","45.07 (min 43.87, max 45.72)","2.89 (min 2.61, max 3.25)"
   "5242880","31.47 (min 27.53, max 34.79)","3.15 (min 2.08, max 6.11)","45.07 (min 43.95, max 45.72)","2.74 (min 2.34, max 3.27)"

.. csv-table:: MMC EXT2
   :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

   "102400","41.88 (min 36.64, max 46.06)","4.53 (min 3.32, max 7.89)","77.89 (min 70.17, max 81.14)","4.76 (min 3.15, max 7.56)"
   "262144","30.90 (min 3.15, max 39.91)","4.16 (min 2.57, max 5.46)","86.46 (min 78.40, max 88.10)","5.02 (min 4.14, max 5.86)"
   "524288","39.62 (min 35.14, max 45.71)","4.17 (min 2.77, max 8.09)","88.89 (min 82.05, max 91.42)","5.84 (min 4.72, max 7.36)"
   "1048576","39.61 (min 35.27, max 43.38)","4.21 (min 2.99, max 7.22)","89.27 (min 82.47, max 91.45)","6.06 (min 5.00, max 6.97)"
   "5242880","39.36 (min 35.57, max 46.64)","4.11 (min 2.90, max 7.50)","89.05 (min 82.70, max 91.45)","6.48 (min 5.49, max 8.15)"

.. csv-table:: MMC EXT2
   :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

   "102400","39.54 (min 34.37, max 43.91)","4.23 (min 2.87, max 7.64)","80.06 (min 77.22, max 81.18)","5.72 (min 3.92, max 6.92)"
   "262144","38.64 (min 35.04, max 43.38)","4.09 (min 2.58, max 7.82)","86.51 (min 82.93, max 87.87)","5.80 (min 4.82, max 7.09)"
   "524288","38.19 (min 35.13, max 43.36)","3.98 (min 2.75, max 7.61)","90.29 (min 86.23, max 91.30)","5.63 (min 3.96, max 7.76)"
   "1048576","38.22 (min 34.86, max 42.59)","4.07 (min 2.78, max 7.47)","89.85 (min 85.33, max 91.30)","5.95 (min 4.80, max 6.87)"
   "5242880","38.07 (min 34.50, max 42.98)","3.99 (min 2.63, max 6.94)","90.65 (min 86.03, max 91.33)","6.15 (min 4.82, max 6.97)"

.. csv-table:: MMC EXT2
   :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

   "102400","42.06 (min 37.41, max 45.78)","1.14 (min 0.80, max 1.97)","78.90 (min 75.12, max 81.35)","1.30 (min 1.02, max 1.57)"
   "262144","38.89 (min 35.04, max 43.30)","0.98 (min 0.65, max 1.79)","85.44 (min 78.16, max 87.83)","1.16 (min 0.89, max 1.58)"
   "524288","39.64 (min 35.30, max 46.38)","1.00 (min 0.64, max 2.08)","89.72 (min 86.08, max 91.68)","1.24 (min 0.98, max 1.55)"
   "1048576","38.78 (min 34.58, max 42.69)","0.98 (min 0.65, max 1.79)","90.12 (min 86.55, max 91.60)","1.22 (min 0.98, max 1.41)"
   "5242880","39.52 (min 35.20, max 44.43)","0.99 (min 0.61, max 1.90)","90.88 (min 86.84, max 91.62)","1.26 (min 0.88, max 1.63)"

.. csv-table:: MMC EXT2
   :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

   "102400","40.31 (min 34.31, max 43.65)","2.13 (min 1.38, max 3.74)","80.27 (min 77.61, max 81.31)","2.54 (min 1.93, max 3.26)"
   "262144","38.63 (min 34.98, max 42.09)","1.97 (min 1.29, max 3.59)","85.78 (min 83.33, max 87.87)","2.32 (min 1.68, max 2.71)"
   "524288","38.54 (min 35.02, max 42.90)","2.02 (min 1.29, max 3.83)","90.61 (min 86.80, max 91.58)","2.24 (min 1.75, max 2.83)"
   "1048576","38.56 (min 35.14, max 41.84)","1.91 (min 1.26, max 3.38)","89.93 (min 84.54, max 91.60)","2.41 (min 1.97, max 2.83)"
   "5242880","38.84 (min 35.29, max 42.54)","1.95 (min 1.31, max 3.55)","90.97 (min 86.86, max 91.58)","2.75 (min 2.19, max 3.26)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option

***********
UBoot MMCSD
***********

UBOOT MMCSD FAT
===============

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

   "400000","38238.90 (min 25128.83, max 56109.59)","83382.86 (min 81920.00, max 85333.33)"
   "800000","49359.97 (min 41583.76, max 66064.52)","88220.47 (min 87148.94, max 89043.48)"
   "1000000","51332.90 (min 42118.25, max 73801.80)","90555.07 (min 89530.05, max 91022.22)"

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

   "400000","27409.62 (min 17138.08, max 35929.82)","44216.90 (min 43574.47, max 44521.74)"
   "800000","28955.34 (min 19006.96, max 35008.55)","45620.88 (min 45259.67, max 45765.36)"
   "1000000","31613.16 (min 17945.24, max 37067.87)","46254.92 (min 46022.47, max 46413.60)"

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

   "400000","33615.64 (min 26597.40, max 39384.62)","82994.75 (min 81920.00, max 83591.84)"
   "800000","40050.00 (min 28444.44, max 47080.46)","88087.48 (min 87148.94, max 89043.48)"
   "1000000","46743.82 (min 41062.66, max 49951.22)","90519.34"

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","j722s_evm-fs: Write Throughput (Kbytes/sec)","j722s_evm-fs: Read Throughput (Kbytes/sec)"

   "400000","34232.57 (min 17429.79, max 44043.01)","81279.75 (min 68266.67, max 83591.84)"
   "800000","41350.01 (min 18492.10, max 47906.43)","87269.73 (min 85333.33, max 88086.02)"
   "1000000","44651.42 (min 19006.96, max 50257.67)","89684.78 (min 88562.16, max 90021.98)"

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

   "400000","34545.09 (min 27675.68, max 38641.51)","83472.42 (min 81920.00, max 83591.84)"
   "800000","39644.36 (min 30340.74, max 46022.47)","88019.09 (min 87148.94, max 88086.02)"
   "1000000","46036.10 (min 40857.86, max 49799.39)","90555.26 (min 90519.34, max 91022.22)"

.. csv-table:: UBOOT MMCSD FAT
   :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

   "400000","28170.06 (min 17579.40, max 39009.52)","82332.85 (min 77283.02, max 83591.84)"
   "800000","35414.36 (min 19883.50, max 47627.91)","87634.31 (min 84453.61, max 89043.48)"
   "1000000","36882.19 (min 19095.57, max 48473.37)","90380.74 (min 89043.48, max 91022.22)"

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)

**********
USB Driver
**********

USB Device Controller
=====================

.. csv-table:: USBDEVICE SUPERSPEED SLAVE_READ_THROUGHPUT
   :header: "Number of Blocks","j742s2_evm-fs: Throughput (MB/sec)"

   "150","43.60"

.. csv-table:: USBDEVICE SUPERSPEED SLAVE_WRITE_THROUGHPUT
   :header: "Number of Blocks","j742s2_evm-fs: Throughput (MB/sec)"

   "150","39.00"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
   :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721e-idk-gw: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

   "150","9.96 (min 8.10, max 12.30)","40.38 (min 27.30, max 44.50)","24.22 (min 14.00, max 37.30)","43.95 (min 43.30, max 44.40)","42.55 (min 36.00, max 44.30)"

.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
   :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721e-idk-gw: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

   "150","9.71 (min 7.90, max 12.20)","38.86 (min 29.80, max 43.90)","22.18 (min 12.90, max 34.40)","37.44 (min 35.20, max 39.90)","35.92 (min 29.50, max 39.80)"

*************
CRYPTO Driver
*************

OpenSSL Performance
===================

.. csv-table:: OpenSSL Performance
   :header: "Algorithm","Buffer Size (in bytes)","j7200-evm: throughput (KBytes/Sec)","j721e-idk-gw: throughput (KBytes/Sec)","j721s2-evm: throughput (KBytes/Sec)","j722s_evm-fs: throughput (KBytes/Sec)","j742s2_evm-fs: throughput (KBytes/Sec)","j784s4-evm: throughput (KBytes/Sec)"

   "aes-128-cbc","1024","34782.91 (min 32799.74, max 36992.68)","41120.60 (min 38766.25, max 42864.98)","38766.91 (min 35923.29, max 41106.77)","22991.83 (min 21864.45, max 24363.69)","38268.42 (min 36186.11, max 40103.25)","36820.07 (min 33522.69, max 39562.92)"
   "aes-128-cbc","16","682.29 (min 665.77, max 700.82)","784.69 (min 770.87, max 807.01)","747.57 (min 720.97, max 766.07)","425.94 (min 403.10, max 439.23)","746.40 (min 727.26, max 769.47)","690.60 (min 582.42, max 751.85)"
   "aes-128-cbc","16384","176724.01 (min 172616.36, max 181638.49)","183084.03 (min 175658.33, max 188705.45)","177710.69 (min 172201.30, max 180677.29)","85599.23 (min 83197.95, max 86168.92)","176224.74 (min 173408.26, max 178885.97)","173619.57 (min 168990.04, max 179044.35)"
   "aes-128-cbc","256","10499.04 (min 10330.20, max 10944.26)","12244.33 (min 11976.45, max 12568.32)","11611.67 (min 11315.37, max 12030.89)","7025.14 (min 6523.65, max 7271.51)","11478.36 (min 11175.85, max 11806.12)","11030.82 (min 9775.45, max 11819.78)"
   "aes-128-cbc","64","2724.09 (min 2659.65, max 2798.12)","3143.21 (min 3088.87, max 3223.59)","2986.30 (min 2833.51, max 3081.56)","1844.61 (min 1697.60, max 1920.32)","2981.21 (min 2931.24, max 3042.33)","2777.76 (min 2335.81, max 3000.64)"
   "aes-128-cbc","8192","139559.64 (min 136456.87, max 144351.23)","149458.26 (min 146814.29, max 152130.90)","143530.03 (min 140083.20, max 145468.07)","72241.66 (min 69530.97, max 73400.32)","142653.73 (min 140222.46, max 144613.38)","138356.37 (min 129171.46, max 143461.03)"
   "aes-128-ecb","1024","34977.00 (min 33154.39, max 37184.17)","41680.06 (min 38969.00, max 43510.10)","39177.51 (min 36287.49, max 41387.69)","23515.46 (min 22396.93, max 24908.80)","38717.03 (min 37154.13, max 40328.19)","36574.65 (min 28992.51, max 40123.05)"
   "aes-128-ecb","16","687.85 (min 668.42, max 704.96)","794.64 (min 776.04, max 811.95)","756.82 (min 726.41, max 781.89)","437.41 (min 407.23, max 449.49)","749.84 (min 737.40, max 769.52)","695.79 (min 629.43, max 745.79)"
   "aes-128-ecb","16384","180431.17 (min 177356.80, max 186428.07)","189220.86 (min 180633.60, max 195106.13)","180166.47 (min 176701.44, max 182998.36)","88237.74 (min 86496.60, max 89139.88)","178719.40 (min 170759.51, max 181349.03)","176617.84 (min 166576.13, max 180852.05)"
   "aes-128-ecb","256","10610.38 (min 10386.43, max 10897.49)","12447.21 (min 12188.59, max 12750.93)","11755.02 (min 11356.93, max 12154.11)","7214.32 (min 6547.20, max 7430.74)","11649.38 (min 11429.12, max 11901.44)","10830.69 (min 8829.35, max 11813.55)"
   "aes-128-ecb","64","2747.40 (min 2670.76, max 2832.51)","3183.46 (min 3087.57, max 3261.01)","3012.06 (min 2853.14, max 3105.37)","1895.14 (min 1759.64, max 1970.97)","2989.08 (min 2939.35, max 3064.28)","2793.18 (min 2331.03, max 3029.14)"
   "aes-128-ecb","8192","141550.11 (min 139586.22, max 145855.83)","153179.31 (min 148357.12, max 157215.40)","145259.27 (min 142991.36, max 147939.33)","74427.39 (min 71783.77, max 75513.86)","144532.43 (min 143253.50, max 146462.04)","140003.59 (min 127079.77, max 145640.11)"
   "aes-192-cbc","1024","34721.34 (min 32787.80, max 36777.64)","40742.27 (min 38036.82, max 42334.21)","38523.43 (min 35510.27, max 40497.15)","22512.15 (min 21467.48, max 23803.56)","37812.08 (min 35508.91, max 40271.87)","36903.33 (min 31342.93, max 39482.03)"
   "aes-192-cbc","16","685.26 (min 671.39, max 702.90)","788.64 (min 771.33, max 809.09)","750.94 (min 718.10, max 772.33)","427.23 (min 403.40, max 438.95)","746.66 (min 728.18, max 760.97)","684.39 (min 564.79, max 754.39)"
   "aes-192-cbc","16384","172134.31 (min 167368.02, max 180071.08)","175002.28 (min 172135.77, max 177416.87)","169015.89 (min 166111.91, max 172365.14)","77484.71 (min 76283.90, max 78260.91)","166993.92 (min 162316.29, max 170775.89)","165351.11 (min 156243.29, max 170153.30)"
   "aes-192-cbc","256","10518.78 (min 10381.23, max 10911.91)","12268.44 (min 11989.50, max 12551.59)","11615.22 (min 11072.09, max 12014.34)","6983.54 (min 6517.93, max 7218.77)","11497.08 (min 11281.24, max 11818.24)","11228.21 (min 9846.61, max 11848.79)"
   "aes-192-cbc","64","2733.35 (min 2679.38, max 2809.92)","3146.32 (min 3088.32, max 3237.25)","2996.79 (min 2849.60, max 3095.02)","1840.69 (min 1695.85, max 1924.48)","2971.72 (min 2897.32, max 3043.22)","2858.15 (min 2554.82, max 2985.17)"
   "aes-192-cbc","8192","136572.29 (min 133758.98, max 142527.15)","144015.53 (min 142811.14, max 145626.45)","138071.06 (min 134520.83, max 139616.26)","66253.14 (min 64555.69, max 67267.24)","136838.97 (min 135113.39, max 138914.47)","134405.72 (min 123505.32, max 138188.12)"
   "aes-192-ecb","1024","34908.16 (min 33032.53, max 36727.47)","41316.99 (min 38889.81, max 43331.58)","38758.20 (min 35810.65, max 41065.81)","23136.09 (min 22098.94, max 24482.13)","38233.67 (min 36379.99, max 40249.00)","37298.15 (min 31919.45, max 40219.31)"
   "aes-192-ecb","16","687.49 (min 671.40, max 702.75)","794.95 (min 779.24, max 812.66)","754.59 (min 734.57, max 774.58)","436.81 (min 407.09, max 447.47)","748.64 (min 726.26, max 771.50)","714.55 (min 561.64, max 761.67)"
   "aes-192-ecb","16384","174453.92 (min 169820.16, max 180360.53)","179896.32 (min 177821.01, max 182255.62)","174474.67 (min 171873.62, max 177389.57)","79633.41 (min 77720.23, max 80745.81)","172995.54 (min 169989.46, max 175002.97)","172170.21 (min 167968.77, max 175041.19)"
   "aes-192-ecb","256","10601.73 (min 10402.39, max 10944.77)","12409.83 (min 12235.09, max 12749.74)","11729.16 (min 11272.96, max 12103.68)","7160.29 (min 6531.24, max 7358.72)","11600.37 (min 11329.45, max 11916.80)","11406.32 (min 10569.98, max 11879.00)"
   "aes-192-ecb","64","2745.97 (min 2672.21, max 2819.01)","3180.07 (min 3127.83, max 3256.87)","3005.97 (min 2901.87, max 3110.34)","1888.71 (min 1727.21, max 1957.40)","2980.94 (min 2858.75, max 3064.77)","2948.36 (min 2743.55, max 3046.95)"
   "aes-192-ecb","8192","138273.50 (min 135632.21, max 142950.40)","147507.71 (min 145582.76, max 149345.62)","141660.43 (min 139826.52, max 144588.80)","68399.45 (min 66385.24, max 69394.43)","140362.51 (min 139569.83, max 141978.28)","137580.65 (min 122852.69, max 141620.57)"
   "aes-256-cbc","1024","34558.91 (min 32677.55, max 36508.33)","40419.41 (min 37819.39, max 42143.06)","38116.92 (min 35012.27, max 40275.97)","21924.86 (min 21037.74, max 23027.37)","37826.32 (min 35723.95, max 39836.67)","36252.54 (min 30671.19, max 38445.06)"
   "aes-256-cbc","16","684.68 (min 668.87, max 705.27)","790.07 (min 772.42, max 810.83)","752.33 (min 724.95, max 774.37)","427.03 (min 402.01, max 437.66)","746.44 (min 727.32, max 771.93)","699.82 (min 554.25, max 759.69)"
   "aes-256-cbc","16384","170055.00 (min 167854.08, max 174243.84)","162601.98 (min 160885.42, max 164167.68)","157457.16 (min 153665.54, max 160437.59)","70309.55 (min 69058.56, max 71538.01)","156358.36 (min 152300.20, max 158821.03)","155256.04 (min 145315.16, max 158127.45)"
   "aes-256-cbc","256","10496.96 (min 10293.93, max 10931.97)","12225.52 (min 12073.39, max 12524.89)","11562.73 (min 10936.06, max 11915.26)","6915.76 (min 6486.10, max 7170.05)","11469.81 (min 11112.02, max 11859.97)","11087.16 (min 10062.93, max 11729.32)"
   "aes-256-cbc","64","2733.60 (min 2666.58, max 2825.81)","3153.97 (min 3105.58, max 3229.97)","2991.93 (min 2854.14, max 3082.26)","1839.16 (min 1679.91, max 1927.49)","2980.61 (min 2905.00, max 3079.02)","2837.58 (min 2278.72, max 3032.21)"
   "aes-256-cbc","8192","135173.83 (min 133384.87, max 139026.43)","135640.06 (min 134589.10, max 136724.48)","129930.04 (min 127183.53, max 132096.00)","61198.17 (min 59370.15, max 62180.01)","129611.87 (min 127896.23, max 132025.00)","126648.32 (min 119608.66, max 129922.39)"
   "aes-256-ecb","1024","34788.85 (min 33047.21, max 36583.77)","40837.06 (min 38304.09, max 42684.42)","38634.70 (min 35275.78, max 40973.99)","22550.40 (min 21661.01, max 23703.55)","38172.94 (min 36133.21, max 40186.20)","36611.28 (min 30323.03, max 39460.52)"
   "aes-256-ecb","16","686.89 (min 673.86, max 705.91)","793.91 (min 776.51, max 815.21)","757.06 (min 733.28, max 780.14)","436.34 (min 407.34, max 448.30)","751.59 (min 732.42, max 770.92)","680.82 (min 558.11, max 761.83)"
   "aes-256-ecb","16384","170973.59 (min 168028.84, max 176084.31)","168396.80 (min 165953.54, max 170896.04)","162587.17 (min 159498.24, max 165292.71)","72650.07 (min 70866.26, max 73536.85)","162079.89 (min 159094.10, max 164397.06)","160669.49 (min 152535.04, max 164954.11)"
   "aes-256-ecb","256","10549.72 (min 10340.10, max 10919.00)","12332.31 (min 12067.67, max 12651.43)","11677.47 (min 11002.79, max 12167.25)","7104.75 (min 6539.86, max 7290.97)","11569.69 (min 11133.27, max 11939.24)","11172.85 (min 9803.09, max 11794.26)"
   "aes-256-ecb","64","2741.81 (min 2686.10, max 2812.93)","3178.23 (min 3111.19, max 3260.84)","3013.77 (min 2878.81, max 3125.76)","1876.30 (min 1758.95, max 1940.03)","3000.34 (min 2917.38, max 3083.39)","2893.97 (min 2405.48, max 3048.06)"
   "aes-256-ecb","8192","136648.39 (min 134690.13, max 141301.08)","139381.59 (min 138158.08, max 140260.69)","133800.30 (min 131631.79, max 135905.28)","63013.38 (min 61115.05, max 63646.38)","133348.60 (min 131866.62, max 135839.74)","131428.67 (min 123131.22, max 133944.66)"
   "des3","1024","33631.89 (min 32057.69, max 35328.00)","35345.05 (min 33504.94, max 36675.24)","33966.88 (min 31854.25, max 35393.19)","","33788.61 (min 32605.18, max 34899.29)","33057.50 (min 28200.96, max 35017.39)"
   "des3","16","686.95 (min 666.89, max 703.85)","790.74 (min 778.47, max 814.60)","750.79 (min 728.50, max 769.32)","","747.75 (min 732.91, max 765.69)","692.00 (min 562.50, max 753.63)"
   "des3","16384","116400.31 (min 115403.43, max 117342.21)","94819.33 (min 94333.61, max 95354.88)","93728.49 (min 92760.75, max 94868.82)","","93947.42 (min 93082.97, max 94557.53)","93501.81 (min 92225.54, max 94382.76)"
   "des3","256","10319.04 (min 10096.13, max 10576.81)","11588.31 (min 11430.74, max 11923.03)","10972.64 (min 10591.57, max 11319.55)","","10921.98 (min 10786.56, max 11116.63)","10656.02 (min 9644.63, max 11026.94)"
   "des3","64","2738.55 (min 2661.08, max 2820.42)","3151.44 (min 3104.17, max 3239.85)","2996.71 (min 2908.80, max 3071.57)","","2973.84 (min 2894.78, max 3028.14)","2812.22 (min 2485.44, max 3003.99)"
   "des3","8192","99160.88 (min 97812.48, max 99915.09)","85841.75 (min 85445.29, max 86297.26)","83787.59 (min 82302.29, max 84161.88)","","84562.90 (min 83910.66, max 85128.53)","83617.00 (min 79233.02, max 84639.74)"
   "sha1","1024","68030.71 (min 65581.40, max 71213.40)","68472.66 (min 62956.20, max 71213.06)","67532.78 (min 64463.53, max 70482.60)","","66814.27 (min 64448.51, max 69621.08)","66540.52 (min 64685.40, max 68334.59)"
   "sha1","16","1144.70 (min 1103.37, max 1192.99)","1151.42 (min 1050.12, max 1200.49)","1136.18 (min 1087.91, max 1193.06)","","1119.66 (min 1075.22, max 1169.72)","1113.34 (min 1055.29, max 1150.29)"
   "sha1","16384","496795.65 (min 487565.99, max 506380.29)","499539.29 (min 480843.09, max 511093.42)","496846.62 (min 488614.57, max 505140.57)","","493696.34 (min 485321.39, max 504392.36)","492366.93 (min 485594.45, max 498614.27)"
   "sha1","256","17971.57 (min 17304.06, max 18733.31)","18074.60 (min 16475.56, max 18773.85)","17874.03 (min 17320.53, max 18694.06)","","17613.59 (min 16835.67, max 18311.00)","17458.16 (min 16477.61, max 18012.67)"
   "sha1","64","4545.15 (min 4378.43, max 4748.48)","4579.31 (min 4181.93, max 4768.51)","4534.20 (min 4400.73, max 4698.79)","","4453.60 (min 4284.48, max 4626.62)","4438.86 (min 4217.05, max 4561.26)"
   "sha1","8192","347990.88 (min 339916.12, max 360153.09)","348716.54 (min 331497.47, max 359328.43)","347590.02 (min 343823.70, max 357485.23)","","344691.27 (min 338954.92, max 352018.43)","344980.87 (min 336235.18, max 350041.43)"
   "sha256","1024","67406.21 (min 62777.00, max 70057.30)","67595.69 (min 63336.79, max 70715.73)","67113.16 (min 64679.94, max 69846.02)","37540.69 (min 37018.97, max 38389.76)","65767.25 (min 62208.34, max 69204.99)","65749.36 (min 63520.09, max 67617.11)"
   "sha256","16","1134.55 (min 1056.86, max 1176.56)","1145.94 (min 1070.15, max 1200.56)","1135.60 (min 1093.05, max 1168.89)","626.62 (min 619.02, max 634.84)","1113.05 (min 1054.13, max 1171.69)","1113.66 (min 1071.54, max 1146.79)"
   "sha256","16384","490105.88 (min 479532.37, max 503179.95)","494625.11 (min 482623.49, max 503491.24)","491571.70 (min 482235.73, max 499570.01)","299501.57 (min 297194.84, max 302661.63)","484164.75 (min 458713.77, max 494146.90)","483858.17 (min 475496.45, max 489401.00)"
   "sha256","256","17802.30 (min 16430.76, max 18640.90)","17856.78 (min 16698.97, max 18705.92)","17776.46 (min 17058.82, max 18549.85)","9802.49 (min 9667.41, max 10056.79)","17396.13 (min 16408.23, max 18345.47)","17419.09 (min 16819.88, max 17899.52)"
   "sha256","64","4517.70 (min 4206.36, max 4684.84)","4547.81 (min 4251.84, max 4757.97)","4523.45 (min 4352.49, max 4672.38)","2478.42 (min 2441.51, max 2533.16)","4416.83 (min 4169.41, max 4656.45)","4435.76 (min 4276.80, max 4556.44)"
   "sha256","8192","343354.75 (min 330181.29, max 355923.29)","346409.47 (min 334995.46, max 355560.11)","343857.93 (min 337726.12, max 349323.26)","201944.92 (min 200119.64, max 205138.60)","338477.64 (min 322909.53, max 350085.12)","338434.21 (min 331601.24, max 345817.09)"
   "sha512","1024","51293.14 (min 49911.13, max 52599.13)","51158.76 (min 49361.24, max 52463.96)","50889.23 (min 48561.49, max 52422.66)","25957.50 (min 25505.79, max 26348.20)","50592.33 (min 47777.11, max 52441.77)","50343.73 (min 49252.01, max 51585.71)"
   "sha512","16","1123.06 (min 1088.44, max 1175.50)","1132.83 (min 1076.06, max 1182.29)","1121.95 (min 1022.35, max 1169.29)","609.45 (min 597.36, max 621.75)","1107.72 (min 1024.99, max 1165.53)","1100.10 (min 1065.39, max 1129.10)"
   "sha512","16384","150121.86 (min 149007.02, max 151306.24)","150006.78 (min 149034.33, max 151328.09)","149819.67 (min 148897.79, max 151109.63)","68383.74 (min 68217.51, max 68556.12)","149609.72 (min 147789.14, max 151628.46)","149348.98 (min 148460.89, max 150487.04)"
   "sha512","256","16409.65 (min 15905.02, max 17169.75)","16400.77 (min 15655.59, max 17099.09)","16302.09 (min 15298.39, max 16899.24)","8657.16 (min 8456.70, max 8841.22)","16087.78 (min 15175.59, max 16732.25)","16074.20 (min 15631.45, max 16408.49)"
   "sha512","64","4510.49 (min 4374.02, max 4704.38)","4535.00 (min 4312.09, max 4734.83)","4502.68 (min 4147.65, max 4667.71)","2440.14 (min 2383.68, max 2504.26)","4449.73 (min 4103.98, max 4671.68)","4432.32 (min 4289.86, max 4597.95)"
   "sha512","8192","132509.97 (min 131334.14, max 133884.59)","132632.92 (min 131517.10, max 134026.58)","132409.84 (min 130722.47, max 134146.73)","61526.36 (min 61306.20, max 61707.61)","131963.76 (min 129092.27, max 134111.23)","131725.68 (min 130916.35, max 133477.72)"

.. csv-table:: OpenSSL CPU Load
   :header: "Algorithm","j7200-evm: CPU Load","j721e-idk-gw: CPU Load","j721s2-evm: CPU Load","j722s_evm-fs: CPU Load","j742s2_evm-fs: CPU Load","j784s4-evm: CPU Load"

   "aes-128-cbc","32.47 (min 31.00, max 33.00)","33.19 (min 33.00, max 34.00)","32.20 (min 31.00, max 33.00)","32.63 (min 31.00, max 34.00)","32.79 (min 32.00, max 34.00)","32.31 (min 30.00, max 33.00)"
   "aes-128-ecb","32.67 (min 32.00, max 33.00)","34.00 (min 33.00, max 35.00)","32.80 (min 32.00, max 34.00)","33.69 (min 32.00, max 35.00)","33.07 (min 28.00, max 34.00)","33.23 (min 32.00, max 34.00)"
   "aes-192-cbc","32.53 (min 32.00, max 33.00)","33.25 (min 33.00, max 34.00)","32.27 (min 31.00, max 33.00)","32.56 (min 30.00, max 33.00)","32.79 (min 32.00, max 34.00)","32.85 (min 32.00, max 34.00)"
   "aes-192-ecb","32.60 (min 32.00, max 33.00)","33.63 (min 33.00, max 34.00)","32.73 (min 32.00, max 34.00)","33.13 (min 31.00, max 34.00)","33.00 (min 32.00, max 34.00)","32.77 (min 32.00, max 34.00)"
   "aes-256-cbc","32.47 (min 32.00, max 33.00)","32.88 (min 32.00, max 34.00)","31.93 (min 31.00, max 33.00)","31.69 (min 29.00, max 33.00)","32.57 (min 31.00, max 34.00)","32.38 (min 31.00, max 33.00)"
   "aes-256-ecb","32.53 (min 32.00, max 33.00)","33.19 (min 32.00, max 34.00)","32.33 (min 31.00, max 33.00)","32.44 (min 31.00, max 33.00)","32.79 (min 32.00, max 34.00)","32.38 (min 31.00, max 33.00)"
   "des3","30.53 (min 29.00, max 32.00)","29.94 (min 29.00, max 31.00)","28.80 (min 28.00, max 30.00)","","29.64 (min 29.00, max 30.00)","29.38 (min 28.00, max 30.00)"
   "sha1","96.87 (min 96.00, max 97.00)","97.00","96.53 (min 96.00, max 97.00)","","97.00 (min 95.00, max 98.00)","96.85 (min 96.00, max 97.00)"
   "sha256","96.80 (min 96.00, max 97.00)","97.00","96.53 (min 96.00, max 97.00)","94.56 (min 84.00, max 96.00)","97.07 (min 96.00, max 98.00)","96.85 (min 96.00, max 97.00)"
   "sha512","96.87 (min 96.00, max 97.00)","97.00","96.40 (min 96.00, max 97.00)","95.00 (min 90.00, max 96.00)","97.00 (min 94.00, max 98.00)","96.85 (min 96.00, max 97.00)"

Listed for each algorithm are the code snippets used to run each
  benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc

IPSec Hardware Performance
==========================

Note: queue\_len is set to 300 and software fallback threshold set to 9
to enable software support for optimal performance

.. csv-table:: IPSec Hardware Performance
   :header: "Algorithm","j722s_evm-fs: Throughput (Mbps)","j722s_evm-fs: Packets/Sec","j722s_evm-fs: CPU Load"

   "aes192","323.07 (min 321.40, max 325.50)","28.33 (min 28.00, max 29.00)","53.80 (min 53.77, max 53.83)"

IPSec Software Performance
==========================

.. csv-table:: IPSec Software Performance
   :header: "Algorithm","j721e-idk-gw: Throughput (Mbps)","j721e-idk-gw: Packets/Sec","j721e-idk-gw: CPU Load"

   "3des","122.48 (min 0.00, max 184.20)","10.50 (min 0.00, max 16.00)","45.18 (min 39.09, max 51.28)"
   "aes128","448.90 (min 0.20, max 879.80)","39.71 (min 0.00, max 78.00)","74.24 (min 48.47, max 99.82)"
   "aes192","821.87 (min 676.30, max 909.70)","73.00 (min 60.00, max 81.00)","61.36 (min 59.36, max 62.96)"
   "aes256","379.81 (min 0.10, max 879.30)","33.50 (min 0.00, max 78.00)","77.33 (min 59.46, max 98.15)"

