
======================================
 Linux 11.02.01 Performance Guide
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
| AM437x-gpevm   | AM437x-gpevm Evaluation Module rev 1.5A with ARM running at 1000MHz, DDR3-400 (400MHz/800 MT/S), TMDSEVM437X   |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM572x EVM     | AM57xx Evaluation Module rev A2 with ARM running at 1500MHz, DDR3L-533 (533 MHz/1066 MT/S), TMDSEVM572x        |
+----------------+----------------------------------------------------------------------------------------------------------------+
| K2HK EVM       | K2 Hawkings Evaluation Module rev 40 with ARM running at 1200MHz, DDR3-1600 (800 MHz/1600 MT/S), EVMK2H        |
+----------------+----------------------------------------------------------------------------------------------------------------+
| K2G EVM        | K2 Galileo Evaluation Module rev C, DDR3-1333 (666 MHz/1333 MT/S), EVMK2G                                      |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM64x EVM      | AM64x Evaluation Module rev E1 with ARM running at 1GHz, DDR data rate 1600 MT/S                               |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM65x EVM      | AM65x Evaluation Module rev 1.0 with ARM running at 800MHz, DDR4-2400 (1600 MT/S), TMDX654GPEVM                |
+----------------+----------------------------------------------------------------------------------------------------------------+
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
| AM62x SK       | AM62x Starter Kit rev E2 and E3 with ARM running at 1.4GHz, DDR data rate 1600 MT/S                            |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM62x LP SK    | AM62x LP Starter Kit rev E1 with ARM running at 1.25GHz, LPDDR4 data rate 1600 MT/S                            |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM62SIP SK     | AM62SIP Starter Kit rev E1 with ARM running at 1.4GHz, 512MB LPDDR4 data rate 1600 MT/S                        |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM62Ax SK      | AM62Ax Starter Kit with ARM running at 1.2GHz, DDR data rate 3733 MT/S                                         |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM62Dx EVM     | AM62Dx Evaluation Module rev E2 with ARM running at 1.2GHz, DDR data rate 3733 MT/S                            |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM62Px SK      | AM62Px Starter Kit rev E1 with ARM running at 1.4GHz, DDR data rate 3200 MT/S                                  |
+----------------+----------------------------------------------------------------------------------------------------------------+
| AM62Lx EVM     | AM62Lx Evaluation Module rev E1 with ARM running at 1.4GHz, DDR data rate 1600 MT/S                            |
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
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "af_unix_sock_stream_latency (microsec)","20.11 (min 19.51, max 20.91)","20.92 (min 19.39, max 27.23)","20.28 (min 19.48, max 21.07)","20.73 (min 19.79, max 25.68)","23.65 (min 19.76, max 35.41)"
    "af_unix_socket_stream_bandwidth (mb\s)","1600.78 (min 1549.65, max 1692.82)","1909.59 (min 1796.88, max 1967.65)","1968.01 (min 1771.13, max 2088.48)","2880.92 (min 2676.18, max 3095.23)","2547.08 (min 1610.12, max 3148.32)"
    "bw_file_rd-io-1mb (mb/s)","3575.64 (min 3321.03, max 3685.28)","3527.50 (min 3290.68, max 3636.36)","3018.09 (min 0.00, max 3527.66)","4081.20 (min 3909.03, max 4393.19)","4084.84 (min 3905.52, max 4408.66)"
    "bw_file_rd-o2c-1mb (mb/s)","1343.17 (min 1165.50, max 1618.71)","1660.73 (min 1324.50, max 1843.47)","1408.46 (min 1194.13, max 1538.46)","2039.42 (min 1729.83, max 2330.17)","1935.73 (min 1622.79, max 2194.99)"
    "bw_mem-bcopy-16mb (mb/s)","2303.90 (min 2238.70, max 2369.32)","2776.48 (min 2616.52, max 2818.39)","3433.05 (min 2752.45, max 3787.88)","3063.04 (min 2501.95, max 3676.89)","2916.36 (min 2610.97, max 3428.33)"
    "bw_mem-bcopy-1mb (mb/s)","3242.81 (min 3097.67, max 3390.44)","4751.54 (min 4405.29, max 5214.89)","4439.54 (min 3597.12, max 4804.14)","9721.45 (min 8886.57, max 10054.14)","9634.83 (min 9102.73, max 10055.02)"
    "bw_mem-bcopy-2mb (mb/s)","2397.72 (min 2365.00, max 2478.75)","3837.26 (min 3462.00, max 3942.65)","3597.91 (min 2862.25, max 3985.65)","4399.84 (min 3795.72, max 5075.22)","4236.83 (min 3481.62, max 5156.54)"
    "bw_mem-bcopy-4mb (mb/s)","2293.98 (min 2205.88, max 2362.67)","3721.93 (min 3367.57, max 3883.50)","3460.16 (min 2753.40, max 3822.87)","3712.22 (min 3003.57, max 4682.93)","3467.90 (min 2694.51, max 4290.31)"
    "bw_mem-bcopy-8mb (mb/s)","2298.55 (min 2251.30, max 2367.21)","3014.27 (min 2767.21, max 3089.40)","3430.32 (min 2743.48, max 3788.48)","3151.39 (min 2577.32, max 3769.44)","3068.19 (min 2646.38, max 3645.20)"
    "bw_mem-bzero-16mb (mb/s)","2279.15 (min 2233.70, max 2345.70)","9514.78 (min 8950.21, max 9658.92)","10543.73 (min 9865.89, max 10884.35)","10026.42 (min 9501.19, max 10514.21)","10865.63 (min 10792.58, max 10912.19)"
    "bw_mem-bzero-1mb (mb/s)","3954.88 (min 3097.67, max 4877.10)","8572.39 (min 4405.29, max 12565.07)","8534.13 (min 3597.12, max 13105.92)","11587.93 (min 8886.57, max 13681.37)","11691.32 (min 9102.73, max 13768.12)"
    "bw_mem-bzero-2mb (mb/s)","2618.64 (min 2365.00, max 2929.87)","7946.80 (min 3462.00, max 12234.62)","7442.29 (min 2862.25, max 11729.10)","8655.10 (min 3795.72, max 13437.44)","8955.98 (min 3481.62, max 13715.94)"
    "bw_mem-bzero-4mb (mb/s)","2346.81 (min 2205.88, max 2471.04)","7754.88 (min 3367.57, max 11962.62)","7046.19 (min 2753.40, max 10972.93)","7489.39 (min 3003.57, max 11799.41)","7886.89 (min 2694.51, max 12642.67)"
    "bw_mem-bzero-8mb (mb/s)","2294.45 (min 2242.15, max 2367.21)","7250.17 (min 2767.21, max 11736.66)","6998.01 (min 2743.48, max 10926.83)","6721.38 (min 2577.32, max 10785.31)","7184.20 (min 2646.38, max 11339.48)"
    "bw_mem-cp-16mb (mb/s)","959.83 (min 940.35, max 988.94)","1515.96 (min 1380.50, max 1572.79)","2101.34 (min 1909.08, max 2186.69)","1953.87 (min 1832.34, max 2178.35)","2183.41 (min 2098.36, max 2305.48)"
    "bw_mem-cp-1mb (mb/s)","2967.77 (min 1181.63, max 4877.17)","7028.88 (min 1512.29, max 12614.89)","7496.96 (min 2064.18, max 13155.52)","8147.56 (min 2600.55, max 13678.91)","8400.76 (min 2701.73, max 13743.22)"
    "bw_mem-cp-2mb (mb/s)","1915.03 (min 960.15, max 2940.10)","6776.41 (min 1327.58, max 12219.23)","6676.95 (min 1897.23, max 11627.91)","7518.71 (min 1885.31, max 13306.96)","8057.87 (min 2241.79, max 13693.56)"
    "bw_mem-cp-4mb (mb/s)","1677.56 (min 930.45, max 2473.33)","6655.29 (min 1362.40, max 11964.85)","6349.68 (min 1859.60, max 10928.96)","6754.05 (min 2099.37, max 11795.32)","7417.25 (min 2295.77, max 12709.62)"
    "bw_mem-cp-8mb (mb/s)","1622.51 (min 927.75, max 2358.84)","6484.60 (min 1335.11, max 11734.51)","6326.13 (min 1883.24, max 10945.78)","6136.98 (min 1814.47, max 10788.94)","6763.79 (min 2141.04, max 11315.42)"
    "bw_mem-fcp-16mb (mb/s)","2363.52 (min 2323.89, max 2422.41)","2753.51 (min 2614.81, max 2789.40)","3400.07 (min 2696.78, max 3747.51)","3039.61 (min 2479.08, max 3665.52)","2861.98 (min 2572.35, max 3421.36)"
    "bw_mem-fcp-1mb (mb/s)","3957.97 (min 3106.16, max 4877.10)","8135.05 (min 3544.78, max 12565.07)","8206.62 (min 3182.18, max 13105.92)","10015.92 (min 6025.23, max 13681.37)","10192.21 (min 6339.43, max 13768.12)"
    "bw_mem-fcp-2mb (mb/s)","2655.81 (min 2406.26, max 2929.87)","7946.46 (min 3403.10, max 12234.62)","7218.36 (min 0.00, max 11729.10)","8309.26 (min 3167.69, max 13437.44)","8623.79 (min 3185.35, max 13715.94)"
    "bw_mem-fcp-4mb (mb/s)","2371.84 (min 2283.97, max 2471.04)","7765.87 (min 3393.86, max 11962.62)","7037.86 (min 2725.72, max 10972.93)","7406.95 (min 2853.58, max 11799.41)","7801.33 (min 2685.92, max 12642.67)"
    "bw_mem-fcp-8mb (mb/s)","2322.39 (min 2242.15, max 2411.82)","7247.52 (min 2783.09, max 11736.66)","6981.49 (min 2694.96, max 10926.83)","6694.23 (min 2519.69, max 10785.31)","7150.25 (min 2626.83, max 11339.48)"
    "bw_mem-frd-16mb (mb/s)","6064.97 (min 5884.52, max 6331.62)","4703.93 (min 4320.24, max 4795.44)","4161.47 (min 3177.12, max 4653.87)","3753.13 (min 3109.82, max 4422.94)","3357.09 (min 2664.89, max 4094.69)"
    "bw_mem-frd-1mb (mb/s)","4747.48 (min 3106.16, max 6896.55)","4607.98 (min 3544.78, max 5706.41)","4297.23 (min 3182.18, max 5082.59)","7141.34 (min 6025.23, max 7802.58)","7103.70 (min 6339.43, max 7799.44)"
    "bw_mem-frd-2mb (mb/s)","4316.62 (min 2406.26, max 6427.42)","4747.63 (min 3403.10, max 5818.18)","3895.01 (min 0.00, max 5311.08)","4137.41 (min 3167.69, max 5596.64)","3911.95 (min 3185.35, max 4940.15)"
    "bw_mem-frd-4mb (mb/s)","4200.94 (min 2283.97, max 6322.86)","4639.06 (min 3393.86, max 5680.81)","3830.56 (min 2725.72, max 4726.54)","3952.75 (min 2853.58, max 5161.29)","3489.19 (min 2661.79, max 4638.07)"
    "bw_mem-frd-8mb (mb/s)","4196.89 (min 2306.47, max 6313.13)","4148.40 (min 2783.09, max 5426.49)","3780.51 (min 2694.96, max 4665.40)","3667.44 (min 2519.69, max 5056.89)","3336.67 (min 2626.83, max 4581.90)"
    "bw_mem-fwr-16mb (mb/s)","2277.25 (min 2229.97, max 2345.01)","9509.92 (min 8951.88, max 9661.84)","10543.99 (min 9871.97, max 10871.41)","10021.43 (min 9543.69, max 10517.67)","10883.06 (min 10832.77, max 10921.50)"
    "bw_mem-fwr-1mb (mb/s)","5481.24 (min 4558.20, max 6896.55)","8866.50 (min 4830.92, max 12614.89)","8729.62 (min 4420.87, max 13155.52)","10448.43 (min 7499.54, max 13678.91)","10607.61 (min 6358.04, max 13743.22)"
    "bw_mem-fwr-2mb (mb/s)","4502.55 (min 2775.37, max 6427.42)","8841.49 (min 5166.18, max 12219.23)","7943.13 (min 3536.35, max 11627.91)","8736.18 (min 3850.60, max 13306.96)","8955.02 (min 3615.18, max 13693.56)"
    "bw_mem-fwr-4mb (mb/s)","4230.56 (min 2350.87, max 6322.86)","8666.53 (min 5017.92, max 11964.85)","7423.02 (min 3218.54, max 10928.96)","7792.43 (min 3567.61, max 11795.32)","7994.26 (min 2661.79, max 12709.62)"
    "bw_mem-fwr-8mb (mb/s)","4164.65 (min 2235.57, max 6313.13)","8398.91 (min 4783.26, max 11734.51)","7368.94 (min 3178.39, max 10945.78)","7264.87 (min 3496.50, max 10788.94)","7480.53 (min 2696.78, max 11315.42)"
    "bw_mem-rd-16mb (mb/s)","6301.80 (min 6117.77, max 6597.03)","5021.65 (min 4611.62, max 5155.47)","4862.14 (min 3721.80, max 5404.49)","4450.54 (min 3686.21, max 5211.73)","4022.68 (min 3242.81, max 4761.90)"
    "bw_mem-rd-1mb (mb/s)","9233.10 (min 3172.71, max 15393.39)","6297.72 (min 2132.61, max 10133.23)","5791.45 (min 2956.39, max 10137.58)","15655.52 (min 12228.80, max 17350.44)","15808.36 (min 11174.21, max 17322.27)"
    "bw_mem-rd-2mb (mb/s)","3857.92 (min 923.50, max 7072.14)","3944.39 (min 1045.66, max 6557.38)","4150.78 (min 2416.71, max 6380.86)","4703.32 (min 2515.27, max 7312.61)","4712.98 (min 2776.33, max 6802.72)"
    "bw_mem-rd-4mb (mb/s)","3561.09 (min 748.22, max 6666.67)","3727.96 (min 1087.25, max 6384.11)","3647.71 (min 2062.21, max 5547.85)","3895.91 (min 2030.97, max 6160.95)","3947.76 (min 3315.10, max 5417.30)"
    "bw_mem-rd-8mb (mb/s)","3514.69 (min 711.36, max 6591.96)","3637.77 (min 1136.53, max 5957.92)","3538.21 (min 1973.60, max 5428.33)","3885.71 (min 2016.64, max 6033.18)","3899.81 (min 3203.84, max 5316.50)"
    "bw_mem-rdwr-16mb (mb/s)","730.03 (min 715.34, max 752.34)","1839.46 (min 1695.99, max 1904.54)","2138.79 (min 1930.50, max 2259.89)","1939.69 (min 1632.82, max 2150.54)","2447.60 (min 2328.63, max 2646.82)"
    "bw_mem-rdwr-1mb (mb/s)","3443.25 (min 1181.63, max 8832.93)","2627.14 (min 1512.29, max 6301.32)","3321.11 (min 2064.18, max 5330.88)","6292.88 (min 2600.55, max 9604.93)","6254.40 (min 2701.73, max 9608.41)"
    "bw_mem-rdwr-2mb (mb/s)","972.91 (min 936.91, max 1016.26)","1691.11 (min 1217.47, max 2461.32)","2387.51 (min 1897.23, max 3109.21)","2802.34 (min 1885.31, max 3873.72)","3268.92 (min 2241.79, max 4698.23)"
    "bw_mem-rdwr-4mb (mb/s)","863.45 (min 758.87, max 986.31)","1815.72 (min 1239.73, max 2411.45)","2166.55 (min 1859.60, max 2389.84)","2311.39 (min 1741.91, max 2725.72)","2753.37 (min 2295.77, max 3423.49)"
    "bw_mem-rdwr-8mb (mb/s)","845.19 (min 720.46, max 987.05)","1814.93 (min 1335.11, max 2323.56)","2125.82 (min 1883.24, max 2300.50)","2210.99 (min 1777.58, max 2807.51)","2559.90 (min 2141.04, max 3275.56)"
    "bw_mem-wr-16mb (mb/s)","720.74 (min 694.47, max 743.39)","1740.92 (min 1589.83, max 1835.49)","2188.97 (min 1980.93, max 2273.70)","2018.34 (min 1903.86, max 2239.33)","2758.80 (min 2710.95, max 2818.89)"
    "bw_mem-wr-1mb (mb/s)","6556.45 (min 3172.71, max 15393.39)","3677.88 (min 2132.61, max 8189.73)","4259.94 (min 2956.39, max 9430.47)","13126.49 (min 9334.05, max 17350.44)","13237.13 (min 8131.58, max 17322.27)"
    "bw_mem-wr-2mb (mb/s)","955.37 (min 923.50, max 989.28)","1686.60 (min 1045.66, max 2461.32)","2729.47 (min 2296.65, max 3109.21)","3211.49 (min 2515.27, max 3873.72)","3828.13 (min 2776.33, max 4698.23)"
    "bw_mem-wr-4mb (mb/s)","770.11 (min 748.22, max 801.76)","1722.02 (min 1087.25, max 2411.45)","2297.65 (min 1994.35, max 2435.31)","2467.53 (min 1741.91, max 3150.60)","3211.71 (min 2642.88, max 3673.77)"
    "bw_mem-wr-8mb (mb/s)","730.85 (min 711.36, max 758.44)","1860.92 (min 1136.53, max 2323.56)","2193.40 (min 1912.50, max 2300.50)","2545.42 (min 1777.58, max 2981.74)","3120.49 (min 2645.50, max 3544.00)"
    "bw_mmap_rd-mo-1mb (mb/s)","11957.09 (min 10453.61, max 12278.05)","8662.55 (min 8233.53, max 8958.97)","8459.03 (min 7783.48, max 8805.51)","12890.95 (min 12834.42, max 12917.12)","12904.82 (min 12839.06, max 12916.14)"
    "bw_mmap_rd-o2c-1mb (mb/s)","1426.64 (min 1216.76, max 1646.90)","1463.77 (min 1186.24, max 1664.51)","1304.51 (min 1087.94, max 1498.13)","2562.90 (min 2331.84, max 2966.26)","2207.41 (min 1396.89, max 2808.46)"
    "bw_pipe (mb/s)","756.83 (min 732.59, max 777.56)","932.83 (min 856.51, max 973.20)","959.62 (min 851.11, max 1000.65)","966.46 (min 907.58, max 1020.56)","929.16 (min 796.46, max 1026.46)"
    "bw_unix (mb/s)","1600.78 (min 1549.65, max 1692.82)","1909.59 (min 1796.88, max 1967.65)","1968.01 (min 1771.13, max 2088.48)","2880.92 (min 2676.18, max 3095.23)","2547.08 (min 1610.12, max 3148.32)"
    "lat_connect (us)","37.62 (min 37.05, max 38.36)","37.33 (min 36.66, max 37.89)","37.93 (min 37.30, max 38.57)","37.92 (min 37.24, max 38.42)","37.89 (min 37.27, max 38.57)"
    "lat_ctx-2-128k (us)","5.39 (min 5.02, max 5.72)","5.36 (min 4.98, max 5.66)","5.38 (min 5.05, max 5.65)","5.52 (min 5.23, max 5.77)","7.19 (min 5.32, max 8.92)"
    "lat_ctx-2-256k (us)","4.65 (min 4.32, max 5.07)","4.96 (min 4.34, max 6.41)","4.73 (min 4.35, max 5.04)","4.67 (min 4.39, max 4.94)","5.54 (min 4.41, max 8.17)"
    "lat_ctx-4-128k (us)","5.27 (min 4.95, max 5.58)","5.25 (min 4.90, max 5.48)","5.32 (min 4.92, max 5.55)","5.22 (min 4.94, max 5.55)","6.79 (min 5.52, max 7.61)"
    "lat_ctx-4-256k (us)","4.23 (min 3.86, max 4.63)","4.21 (min 3.82, max 4.54)","4.36 (min 4.02, max 4.71)","3.81 (min 3.44, max 4.20)","5.74 (min 5.24, max 6.99)"
    "lat_fs-0k (num_files)","400.85 (min 371.00, max 421.00)","408.36 (min 395.00, max 421.00)","390.18 (min 350.00, max 414.00)","402.45 (min 381.00, max 417.00)","399.64 (min 361.00, max 426.00)"
    "lat_fs-10k (num_files)","154.54 (min 143.00, max 163.00)","167.82 (min 148.00, max 182.00)","164.36 (min 149.00, max 189.00)","183.91 (min 176.00, max 199.00)","190.64 (min 177.00, max 201.00)"
    "lat_fs-1k (num_files)","230.62 (min 206.00, max 236.00)","234.73 (min 201.00, max 261.00)","226.73 (min 211.00, max 243.00)","242.82 (min 216.00, max 261.00)","245.73 (min 233.00, max 264.00)"
    "lat_fs-4k (num_files)","236.92 (min 219.00, max 261.00)","251.91 (min 230.00, max 262.00)","238.82 (min 202.00, max 256.00)","260.91 (min 231.00, max 274.00)","267.36 (min 262.00, max 270.00)"
    "lat_mem_rd-stride128-sz1000k (ns)","11.99 (min 11.23, max 13.01)","11.97 (min 11.14, max 12.91)","13.54 (min 12.09, max 16.63)","5.81 (min 5.65, max 6.19)","5.99 (min 5.69, max 6.60)"
    "lat_mem_rd-stride128-sz125k (ns)","5.57","5.57","5.57","5.65","5.65"
    "lat_mem_rd-stride128-sz250k (ns)","5.57 (min 5.57, max 5.59)","5.57 (min 5.57, max 5.59)","5.57","5.65 (min 5.65, max 5.69)","5.65"
    "lat_mem_rd-stride128-sz31k (ns)","3.68 (min 2.00, max 4.67)","3.86 (min 3.34, max 4.67)","4.15 (min 3.34, max 5.12)","4.21 (min 3.35, max 5.20)","4.06 (min 3.39, max 4.75)"
    "lat_mem_rd-stride128-sz50 (ns)","2.00","2.00","2.00","2.00","2.00"
    "lat_mem_rd-stride128-sz500k (ns)","5.58 (min 5.57, max 5.62)","5.65 (min 5.57, max 5.83)","5.81 (min 5.57, max 7.14)","5.65","5.65"
    "lat_mem_rd-stride128-sz62k (ns)","5.31 (min 4.67, max 5.57)","5.26 (min 5.12, max 5.59)","5.32 (min 4.67, max 5.57)","5.30 (min 4.76, max 5.65)","5.34 (min 4.74, max 5.65)"
    "lat_mmap-1m (us)","33.08 (min 28.00, max 37.00)","30.55 (min 28.00, max 34.00)","32.45 (min 28.00, max 36.00)","30.64 (min 29.00, max 35.00)","31.18 (min 29.00, max 36.00)"
    "lat_ops-double-add (ns)","1.96","1.96","1.96","1.96","1.96"
    "lat_ops-double-div (ns)","9.01 (min 9.01, max 9.02)","9.01 (min 9.01, max 9.02)","9.01 (min 9.01, max 9.02)","9.01","9.01 (min 9.00, max 9.01)"
    "lat_ops-double-mul (ns)","2.00","2.00","2.00","2.00","2.00"
    "lat_ops-float-add (ns)","1.96","1.96","1.96","1.96","1.96"
    "lat_ops-float-div (ns)","5.51","5.51 (min 5.50, max 5.51)","5.51","5.50 (min 5.50, max 5.51)","5.51 (min 5.50, max 5.51)"
    "lat_ops-float-mul (ns)","2.00","2.00","2.00 (min 2.00, max 2.01)","2.00","2.00"
    "lat_ops-int-add (ns)","0.50","0.50","0.50","0.50","0.50"
    "lat_ops-int-bit (ns)","0.33","0.33","0.33","0.33","0.33"
    "lat_ops-int-div (ns)","4.01 (min 4.00, max 4.01)","4.01 (min 4.00, max 4.01)","4.01 (min 4.00, max 4.02)","4.00 (min 4.00, max 4.01)","4.00 (min 4.00, max 4.01)"
    "lat_ops-int-mod (ns)","4.67 (min 4.67, max 4.69)","4.67 (min 4.67, max 4.68)","4.67 (min 4.67, max 4.68)","4.67","4.67"
    "lat_ops-int-mul (ns)","1.52","1.52","1.52","1.52","1.52"
    "lat_ops-int64-add (ns)","0.50","0.50","0.50","0.50","0.50"
    "lat_ops-int64-bit (ns)","0.33","0.33","0.33","0.33","0.33"
    "lat_ops-int64-div (ns)","3.00 (min 3.00, max 3.01)","3.00","3.00 (min 3.00, max 3.01)","3.00","3.00"
    "lat_ops-int64-mod (ns)","5.67 (min 5.67, max 5.68)","5.67 (min 5.67, max 5.68)","5.67 (min 5.67, max 5.68)","5.67 (min 5.67, max 5.68)","5.67 (min 5.67, max 5.68)"
    "lat_ops-int64-mul (ns)","2.52","2.52","2.52 (min 2.52, max 2.53)","2.52","2.52"
    "lat_pagefault (us)","0.28 (min 0.25, max 0.45)","0.24 (min 0.23, max 0.24)","0.27 (min 0.24, max 0.46)","0.24 (min 0.23, max 0.25)","0.24 (min 0.24, max 0.25)"
    "lat_pipe (us)","14.88 (min 14.10, max 15.59)","14.63 (min 13.93, max 15.28)","14.98 (min 13.74, max 15.87)","16.65 (min 16.08, max 17.14)","20.08 (min 17.41, max 22.46)"
    "lat_proc-exec (us)","423.53 (min 402.46, max 439.75)","374.74 (min 354.69, max 389.50)","436.24 (min 407.08, max 461.08)","338.41 (min 328.18, max 346.94)","412.59 (min 346.80, max 435.85)"
    "lat_proc-fork (us)","388.18 (min 377.79, max 398.57)","345.83 (min 332.76, max 368.07)","394.22 (min 379.92, max 411.79)","316.10 (min 300.47, max 326.47)","383.79 (min 335.94, max 413.07)"
    "lat_proc-proccall (us)","0.00","0.00","0.00","0.00","0.00"
    "lat_select (us)","12.34 (min 11.45, max 13.36)","12.67 (min 11.44, max 13.64)","12.32 (min 11.43, max 13.34)","12.70 (min 11.43, max 13.69)","12.68 (min 11.46, max 13.35)"
    "lat_sem (us)","1.98 (min 1.50, max 2.32)","1.96 (min 1.66, max 2.17)","2.14 (min 1.81, max 2.56)","1.80 (min 1.39, max 2.09)","2.44 (min 1.73, max 2.94)"
    "lat_sig-catch (us)","3.17 (min 2.89, max 3.34)","3.21 (min 2.86, max 3.36)","3.19 (min 2.88, max 3.35)","3.22 (min 2.88, max 3.41)","3.23 (min 2.96, max 3.40)"
    "lat_sig-install (us)","0.54 (min 0.52, max 0.56)","0.55 (min 0.53, max 0.57)","0.55 (min 0.52, max 0.56)","0.55 (min 0.54, max 0.57)","0.55 (min 0.53, max 0.57)"
    "lat_sig-prot (us)","0.45 (min 0.26, max 0.64)","0.47 (min 0.33, max 0.62)","0.53 (min 0.30, max 1.06)","0.54 (min 0.35, max 1.27)","0.47 (min 0.35, max 0.62)"
    "lat_syscall-fstat (us)","1.00 (min 0.91, max 1.09)","1.03 (min 0.94, max 1.10)","1.02 (min 0.94, max 1.10)","1.02 (min 0.93, max 1.10)","1.04 (min 0.93, max 1.11)"
    "lat_syscall-null (us)","0.40 (min 0.39, max 0.42)","0.40 (min 0.39, max 0.42)","0.40 (min 0.39, max 0.41)","0.40 (min 0.39, max 0.42)","0.40 (min 0.39, max 0.42)"
    "lat_syscall-open (us)","163.24 (min 149.65, max 220.24)","162.85 (min 129.86, max 211.64)","156.62 (min 132.58, max 196.79)","180.26 (min 93.72, max 690.67)","192.89 (min 124.79, max 314.00)"
    "lat_syscall-read (us)","0.51 (min 0.50, max 0.53)","0.51 (min 0.50, max 0.56)","0.51 (min 0.49, max 0.52)","0.51 (min 0.50, max 0.53)","0.51 (min 0.49, max 0.54)"
    "lat_syscall-stat (us)","2.34 (min 2.22, max 2.48)","2.36 (min 2.25, max 2.47)","2.38 (min 2.22, max 2.49)","2.37 (min 2.25, max 2.50)","2.40 (min 2.28, max 2.55)"
    "lat_syscall-write (us)","0.49 (min 0.47, max 0.51)","0.50 (min 0.47, max 0.52)","0.50 (min 0.47, max 0.53)","0.49 (min 0.47, max 0.52)","0.50 (min 0.47, max 0.51)"
    "lat_tcp (us)","0.81 (min 0.79, max 0.83)","0.83 (min 0.81, max 0.86)","0.82 (min 0.79, max 0.85)","0.82 (min 0.79, max 0.84)","0.83 (min 0.80, max 0.86)"
    "lat_unix (us)","20.11 (min 19.51, max 20.91)","20.92 (min 19.39, max 27.23)","20.28 (min 19.48, max 21.07)","20.73 (min 19.79, max 25.68)","23.65 (min 19.76, max 35.41)"
    "latency_for_0.50_mb_block_size (nanosec)","5.58 (min 5.57, max 5.62)","5.65 (min 5.57, max 5.83)","5.81 (min 5.57, max 7.14)","5.65","5.65"
    "latency_for_1.00_mb_block_size (nanosec)","6.00 (min 0.00, max 13.01)","5.99 (min 0.00, max 12.91)","6.77 (min 0.00, max 16.63)","2.91 (min 0.00, max 6.19)","3.00 (min 0.00, max 6.60)"
    "pipe_bandwidth (mb\s)","756.83 (min 732.59, max 777.56)","932.83 (min 856.51, max 973.20)","959.62 (min 851.11, max 1000.65)","966.46 (min 907.58, max 1020.56)","929.16 (min 796.46, max 1026.46)"
    "pipe_latency (microsec)","14.88 (min 14.10, max 15.59)","14.63 (min 13.93, max 15.28)","14.98 (min 13.74, max 15.87)","16.65 (min 16.08, max 17.14)","20.08 (min 17.41, max 22.46)"
    "procedure_call (microsec)","0.00","0.00","0.00","0.00","0.00"
    "select_on_200_tcp_fds (microsec)","12.34 (min 11.45, max 13.36)","12.67 (min 11.44, max 13.64)","12.32 (min 11.43, max 13.34)","12.70 (min 11.43, max 13.69)","12.68 (min 11.46, max 13.35)"
    "semaphore_latency (microsec)","1.98 (min 1.50, max 2.32)","1.96 (min 1.66, max 2.17)","2.14 (min 1.81, max 2.56)","1.80 (min 1.39, max 2.09)","2.44 (min 1.73, max 2.94)"
    "signal_handler_latency (microsec)","0.54 (min 0.52, max 0.56)","0.55 (min 0.53, max 0.57)","0.55 (min 0.52, max 0.56)","0.55 (min 0.54, max 0.57)","0.55 (min 0.53, max 0.57)"
    "signal_handler_overhead (microsec)","3.17 (min 2.89, max 3.34)","3.21 (min 2.86, max 3.36)","3.19 (min 2.88, max 3.35)","3.22 (min 2.88, max 3.41)","3.23 (min 2.96, max 3.40)"
    "tcp_ip_connection_cost_to_localhost (microsec)","37.62 (min 37.05, max 38.36)","37.33 (min 36.66, max 37.89)","37.93 (min 37.30, max 38.57)","37.92 (min 37.24, max 38.42)","37.89 (min 37.27, max 38.57)"
    "tcp_latency_using_localhost (microsec)","0.81 (min 0.79, max 0.83)","0.83 (min 0.81, max 0.86)","0.82 (min 0.79, max 0.85)","0.82 (min 0.79, max 0.84)","0.83 (min 0.80, max 0.86)"




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
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cpu_clock (mhz)","2000.00","2000.00","2000.00","2000.00","2000.00"
    "dhrystone_per_mhz (dmips/mhz)","5.28 (min 4.70, max 5.70)","5.46 (min 4.40, max 5.70)","5.22 (min 4.40, max 5.70)","5.26 (min 4.40, max 5.70)","5.65 (min 5.20, max 5.70)"
    "dhrystone_per_second (dhrystonep)","18585858.67 (min 16666667.00, max 20000000.00)","19150080.62 (min 15384615.00, max 20000000.00)","18340750.18 (min 15384615.00, max 20000000.00)","18506039.45 (min 15384615.00, max 20000000.00)","19834710.73 (min 18181818.00, max 20000000.00)"




Whetstone
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Whetstone is a benchmark primarily measuring floating-point arithmetic performance.

Execute the benchmark with the following:

.. code-block:: console

    runWhetstone

.. csv-table:: Whetstone Benchmarks
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "whetstone (mips)","10000.00","10000.00","10000.00","10000.00","10000.00"




Linpack
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Linpack measures peak double precision (64 bit) floating point performance in
solving a dense linear system.

.. csv-table:: Linpack Benchmarks
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "linpack (kflops)","2474650.83 (min 2359680.00, max 2616870.00)","2485862.00 (min 2345173.00, max 2621866.00)","2527215.00 (min 2387575.00, max 2622867.00)","2497389.64 (min 2396742.00, max 2588265.00)","2468907.45 (min 2334013.00, max 2601997.00)"




NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "assignment (iterations)","31.87 (min 31.68, max 31.99)","31.86 (min 31.52, max 31.98)","31.93 (min 31.86, max 31.99)","31.79 (min 31.63, max 31.87)","31.77 (min 31.42, max 31.90)"
    "fourier (iterations)","60644.00 (min 59005.00, max 65633.00)","61890.09 (min 58899.00, max 65543.00)","61492.18 (min 59223.00, max 65637.00)","60215.64 (min 59116.00, max 61757.00)","61379.09 (min 59750.00, max 64969.00)"
    "fp_emulation (iterations)","387.98 (min 387.93, max 388.05)","387.98 (min 387.84, max 388.03)","387.98 (min 387.91, max 388.03)","387.98 (min 387.89, max 388.03)","388.00 (min 387.95, max 388.04)"
    "huffman (iterations)","2406.49 (min 2399.70, max 2413.10)","2407.97 (min 2404.30, max 2411.20)","2407.76 (min 2400.40, max 2416.10)","2407.68 (min 2398.60, max 2413.90)","2405.16 (min 2389.10, max 2413.40)"
    "idea (iterations)","7996.25 (min 7995.20, max 7996.60)","7996.36 (min 7995.20, max 7996.60)","7996.24 (min 7996.00, max 7996.50)","7996.40 (min 7995.50, max 7996.60)","7996.48 (min 7996.20, max 7997.00)"
    "lu_decomposition (iterations)","1371.95 (min 1345.70, max 1391.10)","1367.80 (min 1355.90, max 1374.20)","1372.87 (min 1356.60, max 1389.00)","1364.34 (min 1339.20, max 1377.70)","1359.86 (min 1331.90, max 1377.70)"
    "neural_net (iterations)","28.36 (min 26.96, max 29.03)","28.57 (min 27.57, max 29.03)","28.79 (min 27.06, max 29.04)","28.47 (min 26.31, max 29.03)","28.56 (min 27.52, max 29.04)"
    "numeric_sort (iterations)","873.80 (min 855.53, max 884.84)","874.58 (min 865.31, max 882.72)","879.55 (min 869.95, max 885.36)","876.41 (min 866.80, max 881.58)","876.15 (min 867.45, max 885.54)"
    "string_sort (iterations)","345.39 (min 312.60, max 361.51)","351.09 (min 341.26, max 358.43)","354.63 (min 350.53, max 361.36)","350.79 (min 342.34, max 356.86)","349.20 (min 311.66, max 355.42)"




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
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "add (mb/s)","5304.56 (min 5217.90, max 5457.70)","5191.84 (min 4785.60, max 5294.00)","6271.53 (min 5785.80, max 6497.20)","5863.01 (min 5625.70, max 6250.70)","5684.90 (min 5419.90, max 5789.80)"
    "copy (mb/s)","4661.35 (min 4598.40, max 4776.80)","5479.71 (min 5223.10, max 5544.00)","6969.18 (min 5199.90, max 7755.70)","6172.63 (min 5188.10, max 6874.30)","5601.92 (min 5285.90, max 6196.50)"
    "scale (mb/s)","4735.93 (min 4681.10, max 4843.10)","5346.54 (min 5105.10, max 5409.80)","7079.48 (min 5312.60, max 7859.70)","6288.05 (min 5274.60, max 7011.70)","5592.24 (min 5286.80, max 6220.30)"
    "triad (mb/s)","5311.15 (min 5229.50, max 5465.60)","5172.96 (min 4766.40, max 5277.20)","6270.01 (min 5787.50, max 6499.70)","5860.14 (min 5617.20, max 6249.20)","5678.53 (min 5421.30, max 5780.50)"




CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","82.42 (min 81.97, max 83.33)","82.28 (min 80.00, max 82.64)","82.51 (min 81.97, max 82.64)","82.65 (min 81.30, max 83.33)","82.83 (min 81.97, max 83.33)"
    "core (workloads/)","0.77 (min 0.77, max 0.78)","0.77 (min 0.77, max 0.78)","0.77 (min 0.77, max 0.78)","0.77 (min 0.77, max 0.78)","0.77 (min 0.77, max 0.78)"
    "coremark-pro ()","2462.93 (min 2446.52, max 2487.00)","2497.27 (min 2482.04, max 2519.86)","2481.01 (min 2450.48, max 2514.48)","2495.07 (min 2468.69, max 2517.57)","2505.05 (min 2472.84, max 2529.33)"
    "linear_alg-mid-100x100-sp (workloads/)","80.62 (min 78.62, max 82.51)","80.62 (min 79.37, max 82.10)","80.61 (min 79.62, max 81.83)","79.57 (min 78.13, max 81.30)","80.34 (min 79.11, max 81.97)"
    "loops-all-mid-10k-sp (workloads/)","2.47 (min 2.45, max 2.48)","2.47 (min 2.44, max 2.48)","2.48 (min 2.45, max 2.50)","2.46 (min 2.46, max 2.47)","2.46 (min 2.46, max 2.47)"
    "nnet_test (workloads/)","3.61 (min 3.41, max 3.83)","3.67 (min 3.52, max 3.87)","3.67 (min 3.38, max 3.86)","3.55 (min 3.34, max 3.80)","3.62 (min 3.42, max 3.81)"
    "parser-125k (workloads/)","10.99 (min 10.87, max 11.11)","11.09 (min 10.99, max 11.11)","11.05 (min 10.99, max 11.11)","10.87","10.86 (min 10.75, max 10.87)"
    "radix2-big-64k (workloads/)","256.20 (min 241.55, max 265.53)","275.62 (min 270.64, max 283.93)","264.22 (min 236.52, max 279.17)","293.95 (min 272.78, max 307.79)","295.18 (min 271.59, max 307.31)"
    "sha-test (workloads/)","157.49 (min 156.25, max 158.73)","158.50 (min 156.25, max 158.73)","157.24 (min 156.25, max 158.73)","158.73","158.50 (min 156.25, max 158.73)"
    "zip-test (workloads/)","46.54 (min 45.45, max 47.62)","47.62","47.19 (min 45.45, max 47.62)","47.23 (min 45.45, max 47.62)","47.23 (min 45.45, max 47.62)"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","163.23 (min 161.29, max 163.93)","163.28 (min 158.73, max 163.93)","162.88 (min 158.73, max 163.93)","163.95 (min 161.29, max 166.67)","164.93 (min 163.93, max 166.67)"
    "core (workloads/)","1.55 (min 1.54, max 1.55)","1.55 (min 1.54, max 1.56)","1.54 (min 1.53, max 1.55)","1.55 (min 1.54, max 1.56)","1.55 (min 1.54, max 1.55)"
    "coremark-pro ()","4264.54 (min 4113.16, max 4398.22)","4371.24 (min 4277.67, max 4469.69)","4410.16 (min 4354.11, max 4500.29)","4692.95 (min 4639.00, max 4720.56)","4895.17 (min 4726.41, max 5010.90)"
    "linear_alg-mid-100x100-sp (workloads/)","159.96 (min 158.23, max 162.87)","159.85 (min 156.74, max 163.40)","160.48 (min 158.23, max 163.40)","160.11 (min 158.73, max 161.81)","160.45 (min 158.73, max 162.34)"
    "loops-all-mid-10k-sp (workloads/)","3.95 (min 3.50, max 4.22)","3.96 (min 3.63, max 4.32)","4.00 (min 3.79, max 4.20)","4.05 (min 3.88, max 4.38)","4.41 (min 3.86, max 4.92)"
    "nnet_test (workloads/)","7.27 (min 7.04, max 7.63)","7.23 (min 6.69, max 7.70)","7.37 (min 7.07, max 7.69)","7.22 (min 7.11, max 7.29)","7.27 (min 7.18, max 7.66)"
    "parser-125k (workloads/)","20.65 (min 19.80, max 20.83)","21.22 (min 21.05, max 21.28)","20.60 (min 20.20, max 21.05)","21.10 (min 20.83, max 21.28)","21.24 (min 20.83, max 21.74)"
    "radix2-big-64k (workloads/)","224.23 (min 194.82, max 253.55)","266.96 (min 242.95, max 292.48)","282.78 (min 262.40, max 317.36)","418.64 (min 411.69, max 426.26)","552.41 (min 414.25, max 619.96)"
    "sha-test (workloads/)","305.21 (min 285.71, max 312.50)","302.28 (min 270.27, max 312.50)","306.24 (min 277.78, max 312.50)","318.55 (min 312.50, max 322.58)","319.83 (min 312.50, max 322.58)"
    "zip-test (workloads/)","81.39 (min 62.50, max 86.96)","83.88 (min 76.92, max 90.91)","84.57 (min 80.00, max 90.91)","93.51 (min 90.91, max 95.24)","94.45 (min 90.91, max 95.24)"

 


.. csv-table:: CoreMarkProFourCore Benchmarks
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","160.92 (min 156.25, max 163.93)","162.71 (min 161.29, max 163.93)","161.54 (min 158.73, max 163.93)","322.58"
    "core (workloads/)","1.55 (min 1.54, max 1.55)","1.54 (min 1.54, max 1.55)","1.54 (min 1.54, max 1.55)","3.09 (min 3.08, max 3.10)"
    "coremark-pro ()","4135.30 (min 4080.30, max 4234.65)","4329.63 (min 4265.20, max 4430.38)","4335.59 (min 4235.39, max 4405.19)","8758.07 (min 8659.92, max 8875.66)"
    "linear_alg-mid-100x100-sp (workloads/)","159.92 (min 155.76, max 161.81)","160.22 (min 158.23, max 161.81)","159.22 (min 153.85, max 162.34)","311.10 (min 304.88, max 314.47)"
    "loops-all-mid-10k-sp (workloads/)","4.04 (min 3.87, max 4.23)","4.02 (min 3.53, max 4.34)","4.10 (min 3.88, max 4.36)","7.45 (min 7.13, max 7.73)"
    "nnet_test (workloads/)","7.32 (min 7.07, max 7.62)","7.37 (min 7.19, max 7.67)","7.39 (min 7.09, max 7.58)","12.22 (min 11.98, max 12.80)"
    "parser-125k (workloads/)","19.33 (min 18.78, max 19.70)","20.36 (min 19.70, max 20.73)","18.83 (min 18.43, max 19.51)","39.84 (min 37.38, max 41.67)"
    "radix2-big-64k (workloads/)","182.48 (min 159.44, max 205.89)","241.24 (min 230.84, max 270.71)","273.22 (min 225.68, max 292.57)","808.84 (min 746.27, max 882.61)"
    "sha-test (workloads/)","301.91 (min 285.71, max 312.50)","304.86 (min 285.71, max 312.50)","301.94 (min 277.78, max 312.50)","526.32"
    "zip-test (workloads/)","80.34 (min 75.47, max 83.33)","85.24 (min 80.00, max 88.89)","82.62 (min 75.47, max 88.89)","179.66 (min 173.91, max 181.82)"

 


.. csv-table:: CoreMarkProEightCore Benchmarks
    :header: "Benchmarks","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","625.00"
    "core (workloads/)","6.18 (min 6.16, max 6.21)"
    "coremark-pro ()","14137.52 (min 13646.37, max 14294.03)"
    "linear_alg-mid-100x100-sp (workloads/)","577.16 (min 568.18, max 581.40)"
    "loops-all-mid-10k-sp (workloads/)","10.44 (min 10.10, max 10.69)"
    "nnet_test (workloads/)","18.79 (min 18.08, max 19.19)"
    "parser-125k (workloads/)","72.56 (min 70.80, max 73.39)"
    "radix2-big-64k (workloads/)","846.71 (min 824.40, max 866.55)"
    "sha-test (workloads/)","769.23"
    "zip-test (workloads/)","310.57 (min 228.57, max 320.00)"

 
 


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
    :header: "Benchmarks","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "4m-check (workloads/)","823.74 (min 802.05, max 865.35)","821.32 (min 788.64, max 847.75)","767.62 (min 692.71, max 804.38)","1119.59 (min 1099.38, max 1148.37)","993.45 (min 979.62, max 1003.21)"
    "4m-check-reassembly (workloads/)","114.89 (min 111.86, max 123.31)","138.67 (min 130.55, max 143.06)","136.56 (min 121.36, max 143.27)","175.19 (min 166.67, max 190.84)","185.55 (min 177.94, max 192.31)"
    "4m-check-reassembly-tcp (workloads/)","85.36 (min 83.61, max 87.41)","94.14 (min 89.29, max 98.81)","86.53 (min 76.92, max 93.28)","106.57 (min 102.04, max 113.12)","106.61 (min 99.60, max 110.13)"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","39.55 (min 38.78, max 40.57)","43.24 (min 41.12, max 44.28)","40.43 (min 38.73, max 41.58)","54.53 (min 53.33, max 56.50)","36.28 (min 33.30, max 39.47)"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","2.67 (min 2.62, max 2.69)","2.68 (min 2.50, max 2.75)","2.65 (min 2.60, max 2.70)","4.61 (min 3.87, max 4.83)","4.64 (min 3.29, max 4.88)"
    "4m-cmykw2 (workloads/)","309.23 (min 307.22, max 311.04)","313.09 (min 310.08, max 314.96)","309.17 (min 306.28, max 311.53)","590.02 (min 561.80, max 604.23)","596.36 (min 576.37, max 606.06)"
    "4m-cmykw2-rotatew2 (workloads/)","58.74 (min 57.20, max 59.76)","62.75 (min 61.92, max 63.63)","59.02 (min 57.53, max 59.64)","71.29 (min 67.64, max 72.29)","47.01 (min 41.49, max 54.60)"
    "4m-reassembly (workloads/)","102.72 (min 100.00, max 107.07)","125.75 (min 117.65, max 129.03)","120.30 (min 106.27, max 127.23)","128.33 (min 122.40, max 143.06)","132.28 (min 125.63, max 140.45)"
    "4m-rotatew2 (workloads/)","69.17 (min 68.68, max 69.83)","72.83 (min 71.63, max 73.64)","68.85 (min 67.89, max 69.44)","77.34 (min 76.57, max 77.94)","50.04 (min 40.68, max 61.05)"
    "4m-tcp-mixed (workloads/)","260.51 (min 250.00, max 271.19)","264.58 (min 242.42, max 275.86)","256.71 (min 246.15, max 266.67)","261.59 (min 258.07, max 271.19)","250.30 (min 238.81, max 262.30)"
    "4m-x264w2 (workloads/)","2.73 (min 2.71, max 2.74)","2.74 (min 2.64, max 2.80)","2.71 (min 2.69, max 2.74)","4.80 (min 3.99, max 5.07)","4.93 (min 4.14, max 5.07)"
    "idct-4m (workloads/)","34.87 (min 34.75, max 34.92)","35.03 (min 34.99, max 35.06)","34.85 (min 34.75, max 34.94)","35.05 (min 34.93, max 35.10)","35.08 (min 34.90, max 35.12)"
    "idct-4mw1 (workloads/)","34.89 (min 34.73, max 34.93)","35.03 (min 34.98, max 35.06)","34.90 (min 34.71, max 34.97)","35.06 (min 34.92, max 35.12)","35.08 (min 34.93, max 35.12)"
    "ippktcheck-4m (workloads/)","819.03 (min 799.49, max 854.41)","816.93 (min 769.47, max 850.92)","772.15 (min 709.02, max 815.40)","1106.41 (min 1013.79, max 1123.09)","991.76 (min 967.87, max 1003.61)"
    "ippktcheck-4mw1 (workloads/)","815.57 (min 796.94, max 848.03)","819.09 (min 783.21, max 851.79)","770.92 (min 696.38, max 825.08)","1119.12 (min 1114.58, max 1123.09)","990.57 (min 967.87, max 1000.80)"
    "ipres-4m (workloads/)","153.06 (min 150.00, max 158.40)","177.61 (min 164.84, max 181.60)","159.99 (min 140.85, max 170.26)","179.31 (min 165.93, max 196.85)","179.88 (min 173.21, max 187.27)"
    "ipres-4mw1 (workloads/)","152.31 (min 149.25, max 157.40)","178.40 (min 167.22, max 182.70)","159.65 (min 139.80, max 169.11)","179.78 (min 169.68, max 200.54)","179.18 (min 174.42, max 186.57)"
    "md5-4m (workloads/)","43.04 (min 42.37, max 43.59)","46.18 (min 45.21, max 46.66)","42.71 (min 41.44, max 43.29)","47.16 (min 46.58, max 47.69)","44.61 (min 44.42, max 44.88)"
    "md5-4mw1 (workloads/)","43.34 (min 42.99, max 43.78)","46.31 (min 45.62, max 46.82)","42.93 (min 41.36, max 43.50)","47.16 (min 46.79, max 47.64)","44.65 (min 44.29, max 45.05)"
    "rgbcmyk-4m (workloads/)","162.72 (min 160.26, max 163.27)","163.53 (min 163.27, max 163.80)","162.44 (min 159.87, max 162.87)","163.36 (min 160.00, max 164.07)","163.74 (min 163.27, max 163.93)"
    "rgbcmyk-4mw1 (workloads/)","162.57 (min 160.90, max 163.13)","162.92 (min 160.13, max 163.67)","162.63 (min 161.94, max 162.87)","163.65 (min 163.40, max 163.93)","163.13 (min 160.64, max 164.07)"
    "rotate-4ms1 (workloads/)","50.85 (min 50.10, max 51.28)","53.82 (min 53.08, max 54.53)","50.70 (min 49.31, max 51.28)","53.19 (min 52.74, max 54.11)","53.14 (min 52.47, max 53.48)"
    "rotate-4ms1w1 (workloads/)","50.90 (min 50.51, max 51.60)","53.79 (min 52.85, max 54.23)","50.53 (min 48.97, max 51.28)","53.26 (min 52.74, max 54.17)","53.22 (min 53.02, max 53.48)"
    "rotate-4ms64 (workloads/)","52.49 (min 51.92, max 53.02)","55.39 (min 54.82, max 55.80)","52.17 (min 50.61, max 52.91)","54.63 (min 53.71, max 55.49)","54.78 (min 54.64, max 55.49)"
    "rotate-4ms64w1 (workloads/)","52.56 (min 51.60, max 53.76)","55.13 (min 54.41, max 55.49)","51.95 (min 50.97, max 52.36)","54.66 (min 54.23, max 55.43)","54.68 (min 53.94, max 54.82)"
    "x264-4mq (workloads/)","1.42 (min 1.41, max 1.43)","1.42 (min 1.31, max 1.44)","1.42 (min 1.40, max 1.42)","1.40 (min 1.26, max 1.44)","1.37 (min 0.80, max 1.44)"
    "x264-4mqw1 (workloads/)","1.42 (min 1.42, max 1.43)","1.41 (min 1.29, max 1.44)","1.42 (min 1.39, max 1.43)","1.43 (min 1.40, max 1.45)","1.37 (min 0.96, max 1.43)"



 
 


Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","j7200-evm: Boot time in seconds: avg(min,max)","j721e-idk-gw: Boot time in seconds: avg(min,max)","j721s2-evm: Boot time in seconds: avg(min,max)","j742s2_evm-fs: Boot time in seconds: avg(min,max)","j784s4-evm: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","19.49 (min 18.86, max 23.17)","22.83 (min 21.82, max 25.00)","17.91 (min 15.52, max 20.80)","21.14 (min 18.68, max 56.68)","21.04 (min 19.16, max 38.53)"

 

 

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

    "11025","352791.82 (min 352790.00, max 352794.00)","0.24 (min 0.19, max 0.35)","1023977.89 (min 1023976.00, max 1023980.00)","0.56 (min 0.38, max 0.69)","1023977.73 (min 1023968.00, max 1023994.00)","0.13 (min 0.06, max 0.35)"
    "16000","511990.64 (min 511988.00, max 511992.00)","0.38 (min 0.31, max 0.49)","1023987.44 (min 1023986.00, max 1023989.00)","0.93 (min 0.83, max 1.07)","1023987.45 (min 1023982.00, max 1023998.00)","0.19 (min 0.06, max 0.25)"
    "22050","705574.36 (min 705572.00, max 705578.00)","0.35 (min 0.29, max 0.43)","1023973.44 (min 1023966.00, max 1023993.00)","0.53 (min 0.40, max 0.78)","1023964.36 (min 1023957.00, max 1023969.00)","0.14 (min 0.10, max 0.16)"
    "24000","705581.82 (min 705580.00, max 705584.00)","0.37 (min 0.32, max 0.45)","1023984.67 (min 1023982.00, max 1023993.00)","0.63 (min 0.39, max 0.76)","1023981.45 (min 1023978.00, max 1023985.00)","0.15 (min 0.13, max 0.17)"
    "32000","1023978.73 (min 1023976.00, max 1023981.00)","0.29 (min 0.21, max 0.48)","1023984.89 (min 1023983.00, max 1023989.00)","0.72 (min 0.45, max 0.84)","1023983.91 (min 1023978.00, max 1023989.00)","0.15 (min 0.11, max 0.17)"
    "44100","1411172.73 (min 1411169.00, max 1411176.00)","0.60 (min 0.53, max 0.70)","1417786.00 (min 1417761.00, max 1417795.00)","0.71 (min 0.61, max 0.75)","1417790.82 (min 1417784.00, max 1417801.00)","0.15 (min 0.14, max 0.17)"
    "48000","1535971.55 (min 1535968.00, max 1535975.00)","0.77 (min 0.68, max 0.92)","1535950.44 (min 1535934.00, max 1535956.00)","0.71 (min 0.61, max 0.78)","1535953.00 (min 1535948.00, max 1535963.00)","0.16 (min 0.13, max 0.18)"
    "88200","2822346.45 (min 2822340.00, max 2822352.00)","1.11 (min 1.03, max 1.25)","2835612.33 (min 2835593.00, max 2835619.00)","1.28 (min 1.20, max 1.31)","2835615.18 (min 2835607.00, max 2835632.00)","0.30 (min 0.27, max 0.34)"
    "96000","3071942.00 (min 3071936.00, max 3071949.00)","0.59 (min 0.50, max 0.67)","3071920.89 (min 3071905.00, max 3071926.00)","1.31 (min 1.14, max 1.40)","3071922.91 (min 3071914.00, max 3071941.00)","0.32 (min 0.27, max 0.38)"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","j721e-idk-gw: Throughput (bits/sec)","j721e-idk-gw: CPU Load (%)","j721s2-evm: Throughput (bits/sec)","j721s2-evm: CPU Load (%)","j784s4-evm: Throughput (bits/sec)","j784s4-evm: CPU Load (%)"

    "11025","352937.36 (min 352936.00, max 352938.00)","0.22 (min 0.18, max 0.27)","1024399.63 (min 1024389.00, max 1024404.00)","0.47 (min 0.34, max 0.60)","1024399.09 (min 1024395.00, max 1024403.00)","0.11 (min 0.07, max 0.22)"
    "16000","512202.45 (min 512201.00, max 512203.00)","0.31 (min 0.17, max 0.38)","1024409.38 (min 1024403.00, max 1024412.00)","0.64 (min 0.37, max 0.82)","1024408.82 (min 1024406.00, max 1024412.00)","0.13 (min 0.07, max 0.19)"
    "22050","705866.27 (min 705862.00, max 705869.00)","0.33 (min 0.30, max 0.40)","1024388.00 (min 1024370.00, max 1024393.00)","0.61 (min 0.45, max 0.79)","1024386.18 (min 1024381.00, max 1024392.00)","0.14 (min 0.10, max 0.17)"
    "24000","705873.45 (min 705871.00, max 705875.00)","0.34 (min 0.30, max 0.41)","1024404.00 (min 1024395.00, max 1024406.00)","0.49 (min 0.26, max 0.77)","1024403.09 (min 1024401.00, max 1024406.00)","0.14 (min 0.07, max 0.16)"
    "32000","1024401.82 (min 1024399.00, max 1024404.00)","0.46 (min 0.23, max 0.56)","1024405.50 (min 1024396.00, max 1024408.00)","0.58 (min 0.25, max 0.81)","1024405.73 (min 1024401.00, max 1024410.00)","0.13 (min 0.06, max 0.20)"
    "44100","1411755.64 (min 1411752.00, max 1411758.00)","0.56 (min 0.51, max 0.61)","1418375.13 (min 1418348.00, max 1418383.00)","0.62 (min 0.54, max 0.75)","1418373.64 (min 1418368.00, max 1418387.00)","0.15 (min 0.14, max 0.18)"
    "48000","1536605.73 (min 1536602.00, max 1536608.00)","0.66 (min 0.36, max 0.77)","1536586.25 (min 1536563.00, max 1536593.00)","0.67 (min 0.57, max 0.77)","1536585.18 (min 1536581.00, max 1536596.00)","0.17 (min 0.14, max 0.23)"
    "88200","2823511.73 (min 2823504.00, max 2823516.00)","1.07 (min 1.00, max 1.15)","2836784.25 (min 2836748.00, max 2836794.00)","1.19 (min 1.09, max 1.31)","2836783.00 (min 2836776.00, max 2836798.00)","0.29 (min 0.27, max 0.34)"
    "96000","3073210.36 (min 3073203.00, max 3073215.00)","1.14 (min 0.52, max 1.43)","3073189.38 (min 3073154.00, max 3073198.00)","1.23 (min 0.98, max 1.41)","3073187.82 (min 3073181.00, max 3073202.00)","0.30 (min 0.16, max 0.38)"

 
 



 



|

Graphics SGX/RGX Driver
-------------------------
 


GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","j721e-idk-gw: Score","j721e-idk-gw: Fps","j721s2-evm: Score","j721s2-evm: Fps","j742s2_evm-fs: Score","j742s2_evm-fs: Fps","j784s4-evm: Score","j784s4-evm: Fps"

    " GFXBench 3.x gl_manhattan_off","1186.13 (min 1130.10, max 1216.61)","19.13 (min 18.23, max 19.62)","932.62 (min 889.16, max 956.89)","15.04 (min 14.34, max 15.43)","915.19 (min 872.62, max 956.67)","14.76 (min 14.07, max 15.43)","894.13 (min 881.41, max 927.40)","14.42 (min 14.22, max 14.96)"
    " GFXBench 3.x gl_trex_off","1796.81 (min 1694.50, max 1851.00)","32.09 (min 30.26, max 33.05)","1591.65 (min 1546.11, max 1641.00)","28.42 (min 27.61, max 29.30)","1492.87 (min 1422.88, max 1587.93)","26.66 (min 25.41, max 28.36)","1484.62 (min 1436.41, max 1534.72)","26.51 (min 25.65, max 27.41)"
    " GFXBench 4.x gl_4_off","404.16 (min 389.01, max 412.86)","6.84 (min 6.58, max 6.99)","259.24 (min 251.06, max 263.93)","4.39 (min 4.25, max 4.47)","255.84 (min 250.12, max 262.40)","4.33 (min 4.23, max 4.44)","253.18 (min 251.00, max 255.97)","4.28 (min 4.25, max 4.33)"
    " GFXBench 5.x gl_5_high_off","177.46 (min 173.02, max 179.44)","2.76 (min 2.69, max 2.79)","114.17 (min 113.19, max 114.94)","1.78 (min 1.76, max 1.79)","112.47 (min 111.27, max 113.82)","1.75 (min 1.73, max 1.77)","111.16 (min 110.50, max 111.97)","1.73 (min 1.72, max 1.74)"




Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","j721e-idk-gw: Score","j721s2-evm: Score","j742s2_evm-fs: Score","j784s4-evm: Score"

    "Glmark2-DRM","46.38 (min 43.00, max 48.00)","121.50 (min 110.00, max 141.00)","127.46 (min 102.00, max 142.00)","164.77 (min 149.00, max 171.00)"
    "Glmark2-Wayland","1062.21 (min 763.00, max 1134.00)","1232.38 (min 1086.00, max 1415.00)","1278.57 (min 1206.00, max 1364.00)","1276.13 (min 1254.00, max 1319.00)"
    "Glmark2-Wayland 4000x4000","79.64 (min 69.00, max 85.00)","78.50 (min 77.00, max 83.00)","84.55 (min 83.00, max 88.00)"

 
 

 

 



|

Ethernet
-----------------
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- CPSW2g: AM65x, J7200, J721e, J721S2, J784S4, J742S2
- CPSW3g: AM64x, AM62x, AM62ax, AM62dx, AM62px


.. rubric::  TCP Bidirectional Throughput 
   :name: CPSW2g-tcp-bidirectional-throughput

.. csv-table:: CPSW2g TCP Bidirectional Throughput
    :header: "Command Used","j7200-evm: THROUGHPUT (Mbits/sec)","j7200-evm: CPU Load % (LOCAL_CPU_UTIL)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j721s2-evm: THROUGHPUT (Mbits/sec)","j721s2-evm: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1074.02 (min 0.00, max 1863.42)","91.65 (min 79.94, max 98.40)","1835.76 (min 1819.73, max 1854.28)","86.65 (min 79.11, max 91.76)","1425.98 (min 0.00, max 1863.91)","87.78 (min 75.63, max 99.23)","1824.95 (min 1812.01, max 1852.44)","59.02 (min 53.81, max 62.83)","1777.43 (min 1670.23, max 1852.12)","27.45 (min 25.24, max 29.09)"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1844.66 (min 1808.69, max 1871.44)","44.79 (min 32.62, max 50.47)","1788.32 (min 1691.27, max 1854.90)","49.05 (min 19.83, max 63.85)","1784.62 (min 1645.58, max 1876.06)","17.27 (min 11.98, max 27.89)"




.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","56.46 (min 0.00, max 93.69)","110.33 (min 0.00, max 183.00)","61.26 (min 15.03, max 84.28)","","79.79 (min 78.33, max 83.28)","155.86 (min 153.00, max 163.00)","43.69 (min 43.24, max 44.62)","","83.31 (min 76.53, max 91.75)","162.67 (min 149.00, max 179.00)","22.19 (min 21.07, max 23.24)"
    "128","","88.12 (min 0.00, max 190.73)","86.00 (min 0.00, max 186.00)","49.57 (min 7.30, max 85.10)","","162.64 (min 157.88, max 168.06)","158.86 (min 154.00, max 164.00)","44.43 (min 43.90, max 45.16)","","163.99 (min 155.27, max 179.60)","160.11 (min 152.00, max 175.00)","22.45 (min 21.27, max 23.09)"
    "256","","195.67 (min 19.25, max 378.61)","95.60 (min 9.00, max 185.00)","44.73 (min 1.91, max 85.39)","","323.22 (min 312.05, max 339.52)","157.86 (min 152.00, max 166.00)","44.18 (min 43.52, max 45.36)","","317.22 (min 303.77, max 341.23)","154.89 (min 148.00, max 167.00)","22.31 (min 21.23, max 22.90)"
    "1024","","750.17 (min 0.00, max 938.57)","91.70 (min 0.00, max 115.00)","62.77 (min 60.53, max 64.41)","","817.10 (min 521.23, max 936.51)","99.57 (min 64.00, max 114.00)","29.89 (min 18.81, max 35.64)","","936.23 (min 933.55, max 939.05)","114.22 (min 114.00, max 115.00)","17.11 (min 16.08, max 18.02)"
    "1518","","921.08 (min 918.51, max 923.68)","76.00","56.17 (min 54.25, max 58.04)","","893.93 (min 704.20, max 924.22)","73.75 (min 58.00, max 76.00)","30.84 (min 28.97, max 31.86)","","921.00 (min 911.09, max 924.32)","75.89 (min 75.00, max 76.00)","14.92 (min 13.31, max 16.28)"




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

 
 

 

 
 



|

PCIe Driver
-------------------------


 


PCIe-NVMe-SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^
 

 

 


.. rubric:: J721E-IDK-GW
   :name: j721e-idk-gw-pciessd




.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","725.36 (min 719.00, max 741.00)","14.26 (min 13.81, max 15.31)","1514.36 (min 1511.00, max 1519.00)","8.11 (min 7.75, max 8.34)"
    "4m","722.27 (min 718.00, max 732.00)","12.48 (min 12.07, max 13.66)","1389.82 (min 741.00, max 1515.00)","5.09 (min 2.70, max 5.60)"
    "4k","173.18 (min 172.00, max 176.00)","48.81 (min 48.42, max 49.02)","126.85 (min 44.80, max 158.00)","30.31 (min 12.89, max 37.23)"
    "256k","732.18 (min 720.00, max 754.00)","16.12 (min 15.48, max 17.02)","1394.36 (min 752.00, max 1515.00)","14.60 (min 7.12, max 15.66)"



- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based 
- Platform: Speed 8GT/s, Width x2
- SSD being used: PLEXTOR PX-128M8PeY
 



.. rubric:: J721S2-EVM
   :name: j721s2-evm-pciessd




.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","706.00 (min 665.00, max 731.00)","16.44 (min 15.55, max 17.25)","771.80 (min 770.00, max 774.00)","4.28 (min 3.82, max 4.82)"
    "4m","714.20 (min 687.00, max 732.00)","13.90 (min 13.77, max 14.08)","774.60 (min 771.00, max 779.00)","3.18 (min 2.43, max 3.83)"
    "4k","167.40 (min 158.00, max 174.00)","49.79 (min 48.52, max 50.56)","265.80 (min 259.00, max 272.00)","50.41 (min 50.27, max 50.50)"
    "256k","701.80 (min 631.00, max 749.00)","16.57 (min 15.38, max 17.59)","781.20 (min 774.00, max 786.00)","8.11 (min 7.58, max 8.48)"



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

    "102400","0.17 (min 0.12, max 0.29)","50.36 (min 49.55, max 51.29)","77.91 (min 76.59, max 78.73)","27.50 (min 0.00, max 40.00)"
    "262144","0.14 (min 0.10, max 0.19)","50.46 (min 49.90, max 51.23)","76.43 (min 75.68, max 77.18)","30.00 (min 25.00, max 40.00)"
    "524288","0.14 (min 0.10, max 0.19)","50.41 (min 49.82, max 51.26)","75.62 (min 74.84, max 76.62)","31.88 (min 20.00, max 40.00)"
    "1048576","0.14 (min 0.10, max 0.19)","50.50 (min 49.87, max 51.43)","73.88 (min 73.39, max 74.81)","31.98 (min 0.00, max 40.00)"




.. rubric:: RAW
   :name: j7200-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j7200-evm: Raw Read Throughput (Mbytes/sec)"

    "50","230.36 (min 227.27, max 238.09)"

 
 


.. rubric:: J721E-IDK-GW
   :name: j721e-idk-gw-ospi


.. rubric:: UBIFS
   :name: j721e-idk-gw-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j721e-idk-gw: Write UBIFS Throughput (Mbytes/sec)","j721e-idk-gw: Write UBIFS CPU Load (%)","j721e-idk-gw: Read UBIFS Throughput (Mbytes/sec)","j721e-idk-gw: Read UBIFS CPU Load (%)"

    "102400","0.69 (min 0.51, max 1.34)","53.81 (min 47.56, max 62.95)","77.37 (min 31.50, max 84.65)","34.88 (min 7.69, max 50.00)"
    "262144","0.50 (min 0.37, max 0.57)","53.98 (min 49.81, max 66.46)","76.41 (min 31.04, max 83.61)","31.67 (min 8.33, max 40.00)"
    "524288","0.50 (min 0.37, max 0.57)","53.06 (min 49.62, max 59.51)","75.63 (min 31.12, max 82.77)","35.53 (min 14.29, max 57.14)"
    "1048576","0.50 (min 0.37, max 0.57)","53.06 (min 49.12, max 60.39)","73.90 (min 30.96, max 79.92)","36.53 (min 14.29, max 50.00)"




.. rubric:: RAW
   :name: j721e-idk-gw-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j721e-idk-gw: Raw Read Throughput (Mbytes/sec)"

    "50","221.84 (min 38.46, max 263.16)"

 
 

 

 


.. rubric:: J742S2-EVM
   :name: j742s2-evm-ospi


.. rubric:: UBIFS
   :name: j742s2-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j742s2_evm-fs: Write UBIFS CPU Load (%)","j742s2_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j742s2_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.29)","27.31 (min 23.95, max 31.13)","73.90 (min 70.59, max 77.89)","18.67 (min 9.09, max 33.33)"
    "262144","0.14 (min 0.10, max 0.19)","27.47 (min 25.20, max 30.15)","74.22 (min 71.10, max 77.87)","17.59 (min 10.00, max 23.08)"
    "524288","0.14 (min 0.10, max 0.19)","27.74 (min 25.00, max 32.30)","73.19 (min 68.87, max 78.57)","22.29 (min 9.09, max 25.00)"
    "1048576","0.14 (min 0.10, max 0.19)","27.95 (min 25.74, max 31.37)","72.67 (min 70.21, max 76.58)","17.81 (min 3.23, max 25.00)"




.. rubric:: RAW
   :name: j742s2-evm-ospi-raw

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j742s2_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","249.00 (min 200.00, max 263.16)"

 
 


.. rubric:: J784S4-EVM
   :name: j784s4-evm-ospi


.. rubric:: UBIFS
   :name: j784s4-evm-ospi-ubifs

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j784s4-evm: Write UBIFS Throughput (Mbytes/sec)","j784s4-evm: Write UBIFS CPU Load (%)","j784s4-evm: Read UBIFS Throughput (Mbytes/sec)","j784s4-evm: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.12, max 0.29)","14.04 (min 12.31, max 17.10)","72.88 (min 69.78, max 77.96)","8.89 (min 4.17, max 15.38)"
    "262144","0.14 (min 0.10, max 0.19)","14.53 (min 12.69, max 17.19)","76.26 (min 71.36, max 80.06)","7.54 (min 4.35, max 13.04)"
    "524288","0.14 (min 0.10, max 0.19)","14.88 (min 12.78, max 17.29)","73.64 (min 70.05, max 79.02)","9.06 (min 4.35, max 13.04)"
    "1048576","0.15 (min 0.10, max 0.19)","14.74 (min 12.46, max 16.92)","73.57 (min 68.25, max 77.00)","7.99 (min 4.17, max 12.00)"




.. rubric:: RAW
   :name: j784s4-evm-ospi-raw


.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j784s4-evm: Raw Read Throughput (Mbytes/sec)"

    "50","246.56 (min 185.19, max 263.16)"

 
 

 

 
 

 



|

UBoot QSPI/OSPI Driver
-------------------------

 


















.. rubric:: J721E-IDK-GW
   :name: j721e-idk-gw-uboot-qspi

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","1030.65 (min 1018.15, max 1041.18)","15845.32 (min 15814.67, max 15875.97)"
    "800000","1031.52 (min 1019.03, max 1042.11)","16059.61 (min 16031.31, max 16062.75)"
    "1000000","1031.85 (min 1019.67, max 1042.37)","16167.36 (min 16157.79, max 16173.74)"
    "2000000","1031.89 (min 1019.83, max 1042.64)","16220.18 (min 16213.76, max 16221.78)"




.. rubric:: J721S2-EVM
   :name: j721s2-evm-uboot-qspi

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "400000","997.13 (min 981.55, max 1002.94)","15842.53 (min 15814.67, max 15875.97)"
    "800000","997.88 (min 982.73, max 1003.55)","16059.89 (min 16031.31, max 16062.75)"
    "1000000","998.08 (min 983.02, max 1003.74)","16163.59 (min 16157.79, max 16173.74)"
    "2000000","998.36 (min 982.99, max 1004.44)","16219.59 (min 16213.76, max 16221.78)"






.. rubric:: J742S2-EVM
   :name: j742s2-evm-uboot-qspi

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","982.87 (min 976.40, max 1000.49)","15848.11 (min 15814.67, max 15875.97)"
    "800000","983.36 (min 977.22, max 1001.47)","16057.03 (min 16031.31, max 16062.75)"
    "1000000","983.77 (min 977.51, max 1001.71)","16160.69 (min 16157.79, max 16173.74)"
    "2000000","984.02 (min 978.65, max 1002.17)","16219.59 (min 16213.76, max 16221.78)"




.. rubric:: J784S4-EVM
   :name: j784s4-evm-uboot-qspi

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","993.61 (min 982.73, max 1024.26)","15831.39 (min 15814.67, max 15875.97)"
    "800000","994.68 (min 983.08, max 1025.28)","16059.89 (min 16031.31, max 16062.75)"
    "1000000","994.94 (min 983.49, max 1025.22)","16163.59 (min 16157.79, max 16173.74)"
    "2000000","994.84 (min 983.32, max 1025.86)","16221.05 (min 16213.76, max 16221.78)"















 
 

 

 



|

UBoot UFS Driver
-------------------------




.. rubric:: J721E-IDK-GW
   :name: j721e-idk-gw-uboot-ufs-raw

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","105500.71 (min 73142.86, max 215578.95)","365468.02 (min 341333.33, max 372363.64)"
    "800000","109739.45 (min 88086.02, max 195047.62)","505307.19 (min 481882.35, max 512000.00)"
    "1000000","115178.24 (min 93622.86, max 234057.14)","619988.40 (min 606814.81, max 655360.00)"






.. rubric:: J742S2-EVM
   :name: j742s2-evm-uboot-ufs-raw

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","91654.27 (min 75851.85, max 97523.81)","359064.94 (min 341333.33, max 372363.64)"
    "800000","98571.17 (min 88086.02, max 102400.00)","512000.00"
    "1000000","102117.05 (min 95812.87, max 105025.64)","610148.96 (min 606814.81, max 630153.85)"

 


.. rubric:: J784S4-EVM
   :name: j784s4-evm-emmc-raw

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","92116.59 (min 87148.94, max 102400.00)","368915.83 (min 341333.33, max 372363.64)"
    "800000","98628.79 (min 88086.02, max 102400.00)","501960.78 (min 481882.35, max 512000.00)"
    "1000000","98832.53 (min 94160.92, max 103696.20)","619780.94 (min 606814.81, max 630153.85)"

 

 



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

    "1m","55.24 (min 44.90, max 60.80)","1.63 (min 1.28, max 1.92)","311.50 (min 306.00, max 315.00)","1.94 (min 1.81, max 2.10)"
    "4m","55.19 (min 44.90, max 61.00)","1.40 (min 1.12, max 1.63)","308.17 (min 301.00, max 314.00)","1.22 (min 1.05, max 1.40)"
    "4k","39.49 (min 5.26, max 58.10)","17.94 (min 2.61, max 27.12)","49.51 (min 36.10, max 56.40)","18.62 (min 13.68, max 21.29)"
    "256k","52.28 (min 36.10, max 60.80)","1.80 (min 1.22, max 2.26)","306.33 (min 288.00, max 317.00)","3.81 (min 3.59, max 4.00)"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","60.20 (min 58.40, max 61.00)","1.52 (min 1.40, max 1.65)","175.00","1.32 (min 1.22, max 1.53)"
    "4m","60.00 (min 57.80, max 61.20)","1.34 (min 1.16, max 1.61)","175.00","0.87 (min 0.72, max 1.08)"
    "4k","50.36 (min 50.00, max 50.60)","21.84 (min 21.53, max 22.07)","56.40 (min 56.00, max 56.90)","20.51 (min 19.98, max 20.72)"
    "256k","60.36 (min 58.70, max 61.20)","2.01 (min 1.89, max 2.22)","174.00","2.36 (min 2.17, max 2.59)"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","68.06 (min 45.00, max 96.70)","2.08 (min 1.44, max 2.93)","300.36 (min 282.00, max 315.00)","2.00 (min 1.76, max 2.09)"
    "4m","68.30 (min 45.30, max 97.10)","1.57 (min 1.19, max 2.34)","278.82 (min 165.00, max 314.00)","1.19 (min 0.93, max 1.44)"
    "4k","48.06 (min 5.22, max 82.60)","23.12 (min 2.76, max 40.21)","62.42 (min 36.20, max 93.50)","24.84 (min 14.71, max 36.95)"
    "256k","64.85 (min 36.20, max 96.70)","2.42 (min 1.50, max 3.53)","293.45 (min 276.00, max 315.00)","3.83 (min 3.59, max 4.03)"

 

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Write EXT4 CPU Load (%)","j742s2_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Read EXT4 CPU Load (%)"

    "1m","96.63 (min 95.90, max 98.00)","1.02 (min 0.94, max 1.08)","289.88 (min 280.00, max 293.00)","0.85 (min 0.80, max 0.89)"
    "4m","95.26 (min 86.80, max 98.50)","1.01 (min 0.92, max 1.11)","261.88 (min 156.00, max 293.00)","0.45 (min 0.30, max 0.51)"
    "4k","82.88 (min 82.50, max 84.30)","20.85 (min 20.12, max 21.93)","82.99 (min 77.00, max 87.50)","16.27 (min 14.86, max 17.86)"
    "256k","96.64 (min 95.90, max 98.10)","1.06 (min 1.00, max 1.17)","292.63 (min 292.00, max 294.00)","1.89 (min 1.81, max 2.03)"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

    "1m","93.41 (min 80.00, max 97.80)","0.48 (min 0.45, max 0.54)","259.18 (min 114.00, max 294.00)","0.41 (min 0.22, max 0.52)"
    "4m","93.91 (min 80.60, max 98.20)","0.45 (min 0.40, max 0.48)","229.97 (min 96.70, max 294.00)","0.21 (min 0.11, max 0.29)"
    "4k","69.48 (min 8.65, max 83.20)","9.74 (min 1.32, max 12.08)","85.85 (min 56.50, max 94.10)","9.26 (min 5.85, max 10.35)"
    "256k","91.75 (min 70.70, max 97.80)","0.59 (min 0.43, max 0.71)","257.42 (min 94.80, max 295.00)","0.92 (min 0.33, max 1.28)"

 

 

 

 

 

 

 
 


EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "1m","53.84 (min 45.00, max 61.00)","1.54 (min 1.24, max 1.93)","311.00 (min 305.00, max 315.00)","1.90 (min 1.64, max 2.07)"
    "4m","53.58 (min 44.90, max 61.00)","1.31 (min 1.08, max 1.59)","291.92 (min 245.00, max 314.00)","1.11 (min 1.00, max 1.31)"
    "4k","34.28 (min 5.30, max 56.10)","12.20 (min 2.05, max 19.86)","47.93 (min 36.00, max 56.40)","16.52 (min 12.56, max 19.50)"
    "256k","50.29 (min 36.10, max 60.90)","1.61 (min 1.22, max 2.10)","303.92 (min 288.00, max 317.00)","3.63 (min 3.32, max 3.92)"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "1m","59.05 (min 43.80, max 61.30)","1.44 (min 1.11, max 1.67)","175.00","1.24 (min 1.15, max 1.38)"
    "4m","59.15 (min 44.20, max 61.60)","1.22 (min 0.90, max 1.44)","175.00","0.79 (min 0.70, max 0.93)"
    "4k","48.31 (min 5.47, max 53.10)","16.74 (min 2.14, max 18.44)","54.60 (min 36.00, max 56.90)","18.19 (min 12.04, max 19.25)"
    "256k","58.24 (min 34.70, max 61.20)","1.73 (min 1.24, max 1.95)","174.00","2.18 (min 2.05, max 2.33)"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "1m","59.46 (min 45.10, max 96.60)","1.77 (min 1.35, max 2.93)","309.42 (min 294.00, max 316.00)","1.99 (min 1.81, max 2.16)"
    "4m","59.54 (min 45.20, max 96.90)","1.42 (min 1.04, max 2.16)","300.25 (min 258.00, max 314.00)","1.23 (min 1.09, max 1.40)"
    "4k","45.04 (min 5.22, max 83.50)","17.18 (min 2.33, max 31.60)","54.27 (min 36.20, max 93.60)","19.97 (min 13.37, max 33.85)"
    "256k","57.20 (min 36.30, max 96.60)","2.03 (min 1.40, max 3.27)","303.83 (min 284.00, max 317.00)","3.74 (min 3.52, max 3.86)"

 

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "1m","93.36 (min 77.60, max 97.50)","0.96 (min 0.73, max 1.28)","276.91 (min 112.00, max 295.00)","0.83 (min 0.38, max 1.01)"
    "4m","93.86 (min 79.40, max 97.80)","0.95 (min 0.76, max 1.03)","241.00 (min 112.00, max 295.00)","0.51 (min 0.23, max 1.00)"
    "4k","73.99 (min 7.73, max 83.40)","14.93 (min 1.67, max 17.12)","88.93 (min 59.00, max 94.20)","16.73 (min 11.69, max 17.70)"
    "256k","91.08 (min 68.60, max 97.60)","0.98 (min 0.75, max 1.19)","275.48 (min 94.30, max 295.00)","1.67 (min 0.66, max 1.88)"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "1m","92.10 (min 79.00, max 98.00)","0.45 (min 0.37, max 0.50)","261.18 (min 112.00, max 296.00)","0.41 (min 0.19, max 0.65)"
    "4m","92.44 (min 71.40, max 98.50)","0.43 (min 0.38, max 0.48)","244.82 (min 111.00, max 296.00)","0.22 (min 0.13, max 0.30)"
    "4k","68.57 (min 6.13, max 83.20)","6.90 (min 0.61, max 9.02)","86.45 (min 56.70, max 93.70)","8.36 (min 5.43, max 9.31)"
    "256k","90.90 (min 69.40, max 98.00)","0.50 (min 0.42, max 0.64)","258.64 (min 94.50, max 296.00)","0.86 (min 0.34, max 1.29)"

 

 

 

 

 

 

 
 

 

 

 

 

 
 



UBoot EMMC Driver
-----------------

 

 

 

 

 

 

 

 

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

    "2000000","60158.47 (min 59041.44, max 61248.60)","307003.10 (min 292571.43, max 312076.19)"
    "4000000","60776.36 (min 59959.74, max 61651.93)","314759.50 (min 304818.60, max 324435.64)"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "2000000","60302.61 (min 59254.97, max 60907.06)","173582.77 (min 172463.16, max 175229.95)"
    "4000000","61009.66 (min 59959.74, max 62060.61)","177446.35 (min 176172.04, max 178572.21)"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "2000000","59316.14 (min 57893.99, max 61478.42)","306695.38 (min 289982.30, max 312076.19)"
    "4000000","60086.70 (min 59308.60, max 61478.42)","308473.92 (min 245453.18, max 322837.44)"

 

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","98745.87 (min 96376.47, max 104025.40)","256895.31 (min 99598.78, max 284939.13)"
    "4000000","98341.17 (min 96518.41, max 100669.74)","267580.77 (min 145635.56, max 292571.43)"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "2000000","96465.70 (min 93356.13, max 101448.92)","276222.56 (min 248242.42, max 289982.30)"
    "4000000","98146.58 (min 95953.15, max 101763.98)","276513.68 (min 214872.13, max 295207.21)"

 

 

 

 

 

 

 
 

 


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

    "1m","34.03 (min 32.60, max 34.90)","1.17 (min 1.08, max 1.28)","43.26 (min 42.30, max 43.50)","0.68 (min 0.62, max 0.75)"
    "4m","33.41 (min 32.10, max 34.30)","0.91 (min 0.84, max 0.98)","43.15 (min 41.60, max 43.50)","0.55 (min 0.47, max 0.70)"
    "4k","2.77 (min 2.75, max 2.80)","2.13 (min 1.97, max 2.23)","11.24 (min 11.20, max 11.40)","5.28 (min 5.17, max 5.47)"
    "256k","31.69 (min 30.60, max 33.50)","1.38 (min 1.22, max 1.52)","42.56 (min 42.40, max 42.90)","0.91 (min 0.82, max 0.98)"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write EXT4 Throughput (Mbytes/sec)","j7200-evm: Write EXT4 CPU Load (%)","j7200-evm: Read EXT4 Throughput (Mbytes/sec)","j7200-evm: Read EXT4 CPU Load (%)"

    "1m","42.89 (min 41.20, max 45.20)","1.54 (min 1.46, max 1.63)","86.96 (min 85.10, max 87.50)","1.10 (min 0.94, max 1.25)"
    "4m","42.37 (min 40.80, max 43.80)","1.26 (min 1.18, max 1.33)","86.49 (min 82.30, max 87.40)","0.74 (min 0.67, max 0.82)"
    "4k","2.75 (min 2.35, max 2.82)","2.28 (min 1.94, max 2.41)","12.54 (min 9.35, max 13.00)","6.18 (min 4.66, max 6.54)"
    "256k","38.13 (min 36.70, max 40.00)","1.65 (min 1.55, max 1.90)","83.45 (min 81.20, max 84.30)","1.46 (min 1.39, max 1.53)"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","42.65 (min 42.00, max 43.70)","1.69 (min 1.56, max 1.92)","87.55 (min 87.20, max 88.20)","1.21 (min 1.05, max 1.41)"
    "4m","41.75 (min 40.20, max 42.80)","1.31 (min 1.17, max 1.53)","85.85 (min 82.10, max 87.30)","0.84 (min 0.72, max 1.14)"
    "4k","2.80 (min 2.79, max 2.83)","2.53 (min 2.39, max 2.65)","12.90 (min 12.80, max 13.00)","7.03 (min 6.78, max 7.26)"
    "256k","38.23 (min 37.00, max 40.50)","1.89 (min 1.72, max 2.17)","83.87 (min 83.20, max 84.50)","1.58 (min 1.45, max 1.85)"

 

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Write EXT4 CPU Load (%)","j742s2_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Read EXT4 CPU Load (%)"

    "1m","42.23 (min 41.50, max 42.80)","0.63 (min 0.47, max 0.69)","87.35 (min 87.30, max 87.50)","0.47 (min 0.39, max 0.55)"
    "4m","41.91 (min 40.90, max 42.70)","0.58 (min 0.51, max 0.64)","87.26 (min 87.10, max 87.40)","0.32 (min 0.29, max 0.35)"
    "4k","2.77 (min 2.75, max 2.79)","1.32 (min 1.11, max 1.44)","12.89 (min 12.80, max 13.00)","3.93 (min 3.27, max 4.24)"
    "256k","36.65 (min 35.90, max 37.80)","0.63 (min 0.57, max 0.67)","83.61 (min 83.40, max 84.00)","0.72 (min 0.67, max 0.77)"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

    "1m","42.82 (min 41.30, max 46.00)","0.31 (min 0.26, max 0.34)","87.23 (min 85.50, max 88.20)","0.26 (min 0.23, max 0.31)"
    "4m","42.66 (min 41.50, max 45.30)","0.28 (min 0.25, max 0.33)","86.70 (min 82.80, max 87.50)","0.17 (min 0.14, max 0.21)"
    "4k","2.75 (min 2.37, max 2.82)","0.61 (min 0.51, max 0.71)","12.58 (min 9.78, max 13.10)","1.72 (min 1.47, max 1.83)"
    "256k","37.57 (min 36.00, max 41.60)","0.32 (min 0.30, max 0.36)","83.38 (min 80.70, max 84.50)","0.35 (min 0.33, max 0.38)"

 

 

 

 

 

 

 

 

 
 


MMC RAW FIO 1G
^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 

 

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "1m","43.87 (min 42.40, max 47.30)","1.39 (min 1.31, max 1.52)","88.01 (min 86.40, max 88.30)","0.91 (min 0.87, max 0.96)"
    "4m","43.53 (min 41.30, max 46.70)","1.23 (min 1.08, max 1.32)","87.93 (min 86.20, max 88.30)","0.70 (min 0.61, max 0.77)"
    "4k","2.77 (min 2.25, max 2.83)","1.94 (min 1.64, max 2.03)","12.67 (min 9.38, max 13.00)","5.95 (min 4.48, max 6.28)"
    "256k","37.91 (min 36.30, max 41.40)","1.48 (min 1.34, max 1.58)","84.03 (min 81.10, max 84.50)","1.43 (min 1.38, max 1.52)"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "1m","34.47 (min 33.00, max 36.50)","1.03 (min 0.94, max 1.16)","43.86 (min 43.80, max 43.90)","0.65 (min 0.56, max 0.79)"
    "4m","33.82 (min 32.50, max 35.40)","0.92 (min 0.80, max 0.97)","43.82 (min 43.80, max 43.90)","0.52 (min 0.45, max 0.62)"
    "4k","2.79 (min 2.77, max 2.80)","1.88 (min 1.77, max 2.03)","11.30","4.98 (min 4.85, max 5.20)"
    "256k","32.02 (min 29.80, max 35.00)","1.24 (min 1.08, max 1.44)","42.90","0.88 (min 0.80, max 0.96)"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "1m","43.38 (min 42.40, max 45.00)","1.59 (min 1.46, max 1.80)","88.20 (min 88.10, max 88.30)","1.08 (min 1.01, max 1.14)"
    "4m","43.06 (min 41.60, max 45.00)","1.27 (min 1.17, max 1.38)","88.17 (min 88.00, max 88.30)","0.81 (min 0.75, max 0.87)"
    "4k","2.82 (min 2.81, max 2.82)","2.22 (min 2.07, max 2.42)","13.02 (min 13.00, max 13.10)","6.59 (min 6.38, max 6.78)"
    "256k","38.00 (min 36.00, max 41.40)","1.73 (min 1.67, max 1.82)","84.37 (min 84.20, max 84.50)","1.52 (min 1.45, max 1.58)"

 

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "1m","43.47 (min 42.00, max 45.10)","0.58 (min 0.54, max 0.64)","88.23 (min 88.10, max 88.30)","0.41 (min 0.36, max 0.45)"
    "4m","43.06 (min 42.00, max 44.50)","0.58 (min 0.54, max 0.61)","88.19 (min 88.00, max 88.30)","0.31 (min 0.26, max 0.35)"
    "4k","2.80 (min 2.79, max 2.83)","1.19 (min 0.98, max 1.31)","13.06 (min 13.00, max 13.10)","3.76 (min 3.26, max 4.08)"
    "256k","38.22 (min 36.00, max 41.50)","0.61 (min 0.52, max 0.67)","84.40 (min 84.20, max 84.50)","0.70 (min 0.63, max 0.75)"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "1m","43.85 (min 42.40, max 47.10)","0.28 (min 0.25, max 0.32)","88.09 (min 86.40, max 88.30)","0.21 (min 0.18, max 0.25)"
    "4m","43.80 (min 42.30, max 47.10)","0.28 (min 0.26, max 0.32)","88.05 (min 86.40, max 88.30)","0.17 (min 0.14, max 0.21)"
    "4k","2.77 (min 2.24, max 2.83)","0.53 (min 0.42, max 0.60)","12.72 (min 9.40, max 13.10)","1.65 (min 1.13, max 1.79)"
    "256k","38.30 (min 36.40, max 41.60)","0.30 (min 0.25, max 0.36)","84.16 (min 81.20, max 84.50)","0.33 (min 0.31, max 0.37)"

 

 

 
 


MMC EXT4
^^^^^^^^

 

 

 

 

 

 

 

 

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "102400","30.77 (min 27.44, max 35.13)","2.83 (min 2.16, max 4.12)","40.21 (min 39.22, max 43.16)","2.36 (min 1.86, max 3.38)"
    "262144","30.49 (min 27.95, max 34.09)","2.85 (min 2.17, max 4.10)","41.68 (min 39.84, max 42.62)","2.24 (min 1.91, max 2.82)"
    "524288","31.49 (min 29.12, max 35.37)","2.85 (min 2.20, max 4.17)","45.43 (min 42.37, max 45.86)","2.55 (min 2.19, max 2.84)"
    "1048576","31.95 (min 29.81, max 34.83)","2.77 (min 1.93, max 4.40)","45.78 (min 45.37, max 45.89)","2.72 (min 2.20, max 3.06)"
    "5242880","32.18 (min 29.27, max 35.59)","2.77 (min 2.06, max 4.17)","45.77 (min 45.65, max 45.89)","2.71 (min 2.21, max 3.06)"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "102400","38.44 (min 34.64, max 44.59)","3.64 (min 2.89, max 5.68)","77.78 (min 70.58, max 81.72)","4.63 (min 3.33, max 5.79)"
    "262144","38.59 (min 35.36, max 41.91)","3.73 (min 2.99, max 5.29)","83.80 (min 78.74, max 88.29)","4.98 (min 3.79, max 6.25)"
    "524288","38.95 (min 36.26, max 42.36)","3.72 (min 2.73, max 6.29)","89.57 (min 81.29, max 92.09)","5.48 (min 4.31, max 6.14)"
    "1048576","39.95 (min 36.84, max 42.72)","3.76 (min 2.76, max 5.57)","90.71 (min 82.14, max 92.05)","6.13 (min 5.29, max 6.93)"
    "5242880","39.41 (min 36.80, max 42.44)","3.70 (min 2.93, max 5.73)","91.63 (min 90.08, max 92.11)","6.43 (min 5.70, max 6.96)"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "102400","38.43 (min 34.70, max 44.04)","3.53 (min 2.69, max 5.94)","77.92 (min 71.25, max 81.68)","4.89 (min 3.54, max 6.02)"
    "262144","38.17 (min 36.19, max 41.90)","3.67 (min 2.61, max 5.52)","84.19 (min 80.79, max 88.28)","5.05 (min 4.28, max 5.86)"
    "524288","39.34 (min 36.57, max 43.37)","3.56 (min 2.42, max 5.34)","91.37 (min 90.63, max 91.73)","5.68 (min 4.80, max 6.96)"
    "1048576","40.00 (min 36.76, max 42.90)","3.57 (min 2.57, max 5.32)","91.18 (min 89.72, max 91.91)","5.51 (min 4.35, max 6.11)"
    "5242880","39.63 (min 36.81, max 43.79)","3.53 (min 2.57, max 5.36)","91.39 (min 89.62, max 91.90)","5.44 (min 4.82, max 6.55)"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "102400","39.04 (min 35.67, max 42.57)","0.93 (min 0.64, max 1.33)","76.54 (min 72.42, max 81.53)","1.25 (min 0.96, max 1.74)"
    "262144","37.96 (min 35.83, max 42.66)","0.88 (min 0.59, max 1.29)","83.00 (min 79.19, max 88.38)","1.08 (min 0.87, max 1.41)"
    "524288","39.89 (min 37.08, max 43.31)","0.92 (min 0.71, max 1.58)","91.86 (min 89.90, max 92.25)","1.18 (min 0.75, max 1.64)"
    "1048576","39.32 (min 36.46, max 43.38)","0.86 (min 0.59, max 1.42)","91.22 (min 89.94, max 92.18)","1.19 (min 0.98, max 1.53)"
    "5242880","39.42 (min 37.47, max 42.83)","0.88 (min 0.63, max 1.38)","91.67 (min 90.88, max 92.17)","1.22 (min 1.08, max 1.42)"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "102400","38.72 (min 35.74, max 43.37)","1.76 (min 1.32, max 2.72)","77.10 (min 72.91, max 81.73)","2.19 (min 0.91, max 2.87)"
    "262144","38.58 (min 36.55, max 41.49)","1.81 (min 1.40, max 2.66)","83.49 (min 78.60, max 88.36)","2.11 (min 1.74, max 2.43)"
    "524288","39.52 (min 37.35, max 42.47)","1.78 (min 1.36, max 3.06)","91.29 (min 89.67, max 92.14)","2.24 (min 1.74, max 2.40)"
    "1048576","39.50 (min 36.97, max 42.88)","1.74 (min 1.31, max 2.52)","91.43 (min 90.00, max 92.07)","2.40 (min 1.98, max 3.04)"
    "5242880","39.43 (min 37.54, max 42.57)","1.71 (min 1.21, max 2.53)","91.89 (min 91.23, max 92.18)","2.56 (min 2.18, max 3.03)"

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 


MMC EXT2
^^^^^^^^

 

 

 

 

 

 

 

 

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "102400","32.49 (min 28.11, max 35.02)","3.40 (min 2.37, max 6.20)","42.36 (min 41.71, max 43.01)","2.44 (min 2.00, max 3.06)"
    "262144","30.55 (min 28.49, max 34.31)","3.09 (min 2.07, max 6.02)","44.03 (min 43.35, max 44.81)","2.62 (min 2.14, max 3.39)"
    "524288","31.24 (min 28.27, max 34.34)","3.20 (min 2.33, max 5.85)","45.09 (min 44.34, max 45.73)","2.66 (min 2.33, max 3.05)"
    "1048576","30.25 (min 28.46, max 31.35)","3.00 (min 2.05, max 5.36)","45.07 (min 44.30, max 45.72)","2.89 (min 2.61, max 3.25)"
    "5242880","31.49 (min 27.53, max 34.79)","3.14 (min 2.08, max 5.96)","45.31 (min 44.28, max 45.72)","2.76 (min 2.34, max 3.27)"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "102400","41.83 (min 37.48, max 45.35)","4.52 (min 3.39, max 7.89)","78.66 (min 73.94, max 81.14)","4.47 (min 3.15, max 5.41)"
    "262144","30.98 (min 3.15, max 39.91)","4.17 (min 2.57, max 5.46)","86.13 (min 78.40, max 88.10)","4.95 (min 4.14, max 5.83)"
    "524288","39.24 (min 35.14, max 45.69)","4.13 (min 2.77, max 8.09)","89.71 (min 85.18, max 91.42)","5.87 (min 4.80, max 7.36)"
    "1048576","39.50 (min 35.27, max 43.38)","4.18 (min 2.99, max 7.22)","89.66 (min 82.47, max 91.45)","6.07 (min 5.16, max 6.97)"
    "5242880","38.78 (min 35.57, max 42.54)","4.04 (min 2.90, max 7.50)","89.44 (min 86.35, max 91.44)","6.47 (min 5.49, max 8.15)"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "102400","39.38 (min 34.64, max 43.91)","4.16 (min 2.87, max 7.52)","79.74 (min 77.22, max 81.18)","5.44 (min 3.92, max 6.84)"
    "262144","38.60 (min 35.14, max 42.21)","4.00 (min 2.58, max 7.63)","86.61 (min 82.93, max 87.87)","5.81 (min 4.82, max 7.09)"
    "524288","37.79 (min 35.13, max 39.91)","3.90 (min 2.75, max 6.90)","89.97 (min 86.23, max 91.23)","5.61 (min 3.96, max 7.76)"
    "1048576","38.10 (min 34.94, max 42.59)","4.03 (min 2.78, max 7.31)","89.97 (min 85.33, max 91.30)","5.81 (min 4.80, max 6.49)"
    "5242880","38.21 (min 34.50, max 42.98)","3.98 (min 2.63, max 6.75)","91.06 (min 90.30, max 91.33)","5.98 (min 4.82, max 6.90)"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "102400","41.82 (min 37.41, max 44.54)","1.14 (min 0.80, max 1.94)","79.20 (min 75.33, max 81.35)","1.26 (min 1.02, max 1.48)"
    "262144","38.49 (min 35.04, max 43.30)","0.97 (min 0.65, max 1.75)","86.08 (min 82.96, max 87.83)","1.17 (min 0.89, max 1.58)"
    "524288","39.11 (min 35.30, max 42.90)","0.98 (min 0.64, max 1.78)","89.46 (min 86.08, max 91.55)","1.22 (min 0.98, max 1.55)"
    "1048576","38.70 (min 34.58, max 42.69)","0.98 (min 0.65, max 1.79)","90.38 (min 86.55, max 91.60)","1.23 (min 0.98, max 1.41)"
    "5242880","39.35 (min 35.20, max 44.43)","0.99 (min 0.65, max 1.90)","90.88 (min 86.84, max 91.62)","1.27 (min 0.88, max 1.63)"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "102400","39.72 (min 34.31, max 43.04)","2.09 (min 1.38, max 3.74)","79.98 (min 77.61, max 80.97)","2.55 (min 1.93, max 3.26)"
    "262144","38.95 (min 35.05, max 42.09)","2.00 (min 1.29, max 3.59)","86.11 (min 83.36, max 87.84)","2.23 (min 1.68, max 2.71)"
    "524288","38.25 (min 35.02, max 42.90)","1.98 (min 1.29, max 3.83)","90.85 (min 86.80, max 91.56)","2.20 (min 1.75, max 2.62)"
    "1048576","38.95 (min 35.14, max 41.84)","1.92 (min 1.26, max 3.38)","89.37 (min 84.54, max 91.57)","2.42 (min 1.97, max 2.83)"
    "5242880","38.62 (min 35.29, max 42.54)","1.95 (min 1.31, max 3.55)","90.80 (min 86.86, max 91.58)","2.81 (min 2.19, max 3.26)"

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 



UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 

 

 

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

    "400000","37343.63 (min 25128.83, max 52512.82)","83609.25 (min 81920.00, max 85333.33)"
    "800000","48685.13 (min 41583.76, max 66064.52)","88330.48 (min 87148.94, max 89043.48)"
    "1000000","50084.13 (min 42118.25, max 73801.80)","90646.89 (min 89530.05, max 91022.22)"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","26475.33 (min 17138.08, max 32000.00)","44219.87 (min 43574.47, max 44521.74)"
    "800000","28932.75 (min 19006.96, max 35008.55)","45627.44 (min 45259.67, max 45765.36)"
    "1000000","31856.13 (min 17945.24, max 36328.16)","46259.12 (min 46022.47, max 46413.60)"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "400000","33188.04 (min 26597.40, max 39384.62)","82831.91 (min 81920.00, max 83591.84)"
    "800000","40014.81 (min 28444.44, max 47080.46)","88087.87 (min 87148.94, max 89043.48)"
    "1000000","46487.21 (min 41062.66, max 48330.38)","90519.34"

 

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","34200.15 (min 27675.68, max 38641.51)","83439.85 (min 81920.00, max 83591.84)"
    "800000","39034.00 (min 30340.74, max 45765.36)","88000.83 (min 87148.94, max 88086.02)"
    "1000000","46448.81 (min 40857.86, max 49799.39)","90565.06 (min 90519.34, max 91022.22)"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","30337.53 (min 17808.70, max 39009.52)","82141.47 (min 77283.02, max 83591.84)"
    "800000","36475.36 (min 19883.50, max 47627.91)","87337.03 (min 84453.61, max 89043.48)"
    "1000000","38434.92 (min 19095.57, max 48473.37)","90342.94 (min 89043.48, max 91022.22)"

 

 

 

 

 

 

 

 

 
 

 

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

    "150","9.50 (min 8.10, max 12.30)","39.30 (min 27.30, max 44.50)","24.06 (min 14.00, max 37.30)","43.96 (min 43.30, max 44.40)","42.44 (min 36.00, max 44.30)"




.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721e-idk-gw: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

    "150","9.32 (min 7.90, max 12.20)","38.20 (min 29.80, max 42.70)","22.20 (min 13.80, max 34.40)","37.23 (min 35.20, max 39.60)","36.12 (min 30.00, max 38.60)"





 
 
 



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","j7200-evm: throughput (KBytes/Sec)","j721e-idk-gw: throughput (KBytes/Sec)","j721s2-evm: throughput (KBytes/Sec)","j742s2_evm-fs: throughput (KBytes/Sec)","j784s4-evm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","35258.54 (min 33110.36, max 36992.68)","41609.35 (min 38766.25, max 42864.98)","39301.75 (min 35923.29, max 41106.77)","38726.66 (min 36403.88, max 40103.25)","37616.20 (min 34457.60, max 39562.92)"
    "aes-128-cbc","16","683.27 (min 665.77, max 700.82)","787.43 (min 771.32, max 807.01)","748.97 (min 720.97, max 766.07)","748.52 (min 727.26, max 769.47)","686.81 (min 582.42, max 751.85)"
    "aes-128-cbc","16384","177469.21 (min 173659.48, max 181638.49)","184173.38 (min 178263.38, max 188705.45)","178181.46 (min 172201.30, max 180677.29)","176162.75 (min 173408.26, max 178885.97)","173431.19 (min 168990.04, max 179044.35)"
    "aes-128-cbc","256","10510.34 (min 10330.20, max 10944.26)","12272.38 (min 11976.45, max 12568.32)","11655.35 (min 11315.37, max 12030.89)","11488.90 (min 11175.85, max 11806.12)","10965.88 (min 9775.45, max 11819.78)"
    "aes-128-cbc","64","2729.62 (min 2659.65, max 2798.12)","3150.72 (min 3088.87, max 3223.59)","2995.86 (min 2833.51, max 3081.56)","2985.31 (min 2935.49, max 3042.33)","2721.34 (min 2335.81, max 3000.64)"
    "aes-128-cbc","8192","140191.97 (min 138346.50, max 144351.23)","150016.95 (min 146953.56, max 152130.90)","143595.75 (min 140083.20, max 145468.07)","142781.10 (min 140222.46, max 144613.38)","137517.47 (min 129171.46, max 143461.03)"
    "aes-128-ecb","1024","35417.00 (min 33504.94, max 37184.17)","42188.69 (min 38969.00, max 43510.10)","39773.27 (min 36287.49, max 41387.69)","39112.21 (min 37168.47, max 40328.19)","37257.25 (min 33961.30, max 40123.05)"
    "aes-128-ecb","16","689.12 (min 668.42, max 704.96)","796.37 (min 780.22, max 811.95)","759.39 (min 726.41, max 781.89)","751.42 (min 738.51, max 769.52)","694.12 (min 629.43, max 743.30)"
    "aes-128-ecb","16384","180860.25 (min 177356.80, max 186428.07)","190752.19 (min 180633.60, max 195106.13)","180592.64 (min 177504.26, max 182998.36)","178846.75 (min 170759.51, max 181349.03)","175839.64 (min 166576.13, max 179879.94)"
    "aes-128-ecb","256","10618.67 (min 10386.43, max 10897.49)","12478.94 (min 12211.80, max 12750.93)","11779.65 (min 11356.93, max 12154.11)","11641.17 (min 11429.12, max 11901.44)","10877.76 (min 8829.35, max 11813.55)"
    "aes-128-ecb","64","2752.52 (min 2670.76, max 2832.51)","3191.37 (min 3087.57, max 3261.01)","3018.89 (min 2853.14, max 3105.37)","2993.82 (min 2946.24, max 3064.28)","2797.05 (min 2331.03, max 3029.14)"
    "aes-128-ecb","8192","141895.45 (min 140331.69, max 145855.83)","154138.15 (min 148357.12, max 157215.40)","145526.78 (min 143406.42, max 147939.33)","144578.87 (min 143253.50, max 146462.04)","139126.37 (min 127079.77, max 145640.11)"
    "aes-192-cbc","1024","35182.14 (min 33143.81, max 36777.64)","41220.88 (min 38410.58, max 42334.21)","39101.78 (min 35510.27, max 40497.15)","38244.57 (min 36091.90, max 40271.87)","37292.82 (min 31342.93, max 39482.03)"
    "aes-192-cbc","16","686.37 (min 671.39, max 702.90)","790.24 (min 771.33, max 809.09)","753.57 (min 718.10, max 772.33)","747.83 (min 728.18, max 760.97)","673.35 (min 564.79, max 754.39)"
    "aes-192-cbc","16384","172979.54 (min 169508.86, max 180071.08)","175179.83 (min 173244.42, max 177416.87)","169386.89 (min 166111.91, max 172365.14)","167078.57 (min 162316.29, max 170775.89)","164903.32 (min 156243.29, max 170153.30)"
    "aes-192-cbc","256","10530.76 (min 10381.23, max 10911.91)","12295.84 (min 12103.51, max 12551.59)","11654.35 (min 11072.09, max 12014.34)","11509.72 (min 11287.04, max 11818.24)","11149.43 (min 9846.61, max 11848.79)"
    "aes-192-cbc","64","2738.49 (min 2679.38, max 2809.92)","3152.70 (min 3097.71, max 3237.25)","3006.21 (min 2849.60, max 3095.02)","2973.00 (min 2897.32, max 3043.22)","2827.19 (min 2554.82, max 2983.38)"
    "aes-192-cbc","8192","137193.47 (min 134662.83, max 142527.15)","144205.88 (min 142811.14, max 145626.45)","138510.11 (min 135460.18, max 139616.26)","136748.56 (min 135113.39, max 138914.47)","133942.48 (min 123505.32, max 138188.12)"
    "aes-192-ecb","1024","35318.19 (min 33032.53, max 36727.47)","41787.58 (min 38889.81, max 43331.58)","39335.03 (min 35810.65, max 41065.81)","38561.61 (min 36379.99, max 40249.00)","37653.91 (min 31919.45, max 40219.31)"
    "aes-192-ecb","16","688.47 (min 671.40, max 702.75)","795.83 (min 779.24, max 812.66)","757.63 (min 734.57, max 774.58)","748.89 (min 726.26, max 771.50)","723.52 (min 630.84, max 761.67)"
    "aes-192-ecb","16384","175420.76 (min 170748.59, max 180360.53)","179919.01 (min 177821.01, max 182255.62)","174862.34 (min 172332.37, max 177389.57)","172843.26 (min 169989.46, max 175002.97)","172328.00 (min 167968.77, max 175041.19)"
    "aes-192-ecb","256","10605.91 (min 10402.39, max 10944.77)","12432.44 (min 12235.09, max 12749.74)","11736.76 (min 11272.96, max 12103.68)","11584.22 (min 11329.45, max 11916.80)","11556.92 (min 11182.42, max 11879.00)"
    "aes-192-ecb","64","2750.10 (min 2672.21, max 2819.01)","3183.95 (min 3127.83, max 3256.87)","3016.06 (min 2901.87, max 3110.34)","2982.14 (min 2858.75, max 3064.77)","2959.73 (min 2743.55, max 3046.95)"
    "aes-192-ecb","8192","138700.12 (min 135632.21, max 142950.40)","147630.34 (min 145582.76, max 149345.62)","141963.04 (min 139826.52, max 144588.80)","140374.14 (min 139569.83, max 141978.28)","138411.21 (min 131642.71, max 141486.76)"
    "aes-256-cbc","1024","34995.31 (min 32794.28, max 36508.33)","40895.75 (min 37819.39, max 42143.06)","38701.08 (min 35110.23, max 40275.97)","38261.64 (min 35912.02, max 39836.67)","37156.59 (min 30671.19, max 38445.06)"
    "aes-256-cbc","16","685.52 (min 668.87, max 705.27)","791.77 (min 772.42, max 810.83)","754.58 (min 724.95, max 774.37)","747.51 (min 727.32, max 771.93)","704.54 (min 578.46, max 759.69)"
    "aes-256-cbc","16384","170415.90 (min 167854.08, max 174243.84)","162643.13 (min 160885.42, max 164167.68)","157959.96 (min 153671.00, max 160437.59)","156250.24 (min 152300.20, max 158821.03)","155084.94 (min 145315.16, max 158127.45)"
    "aes-256-cbc","256","10500.57 (min 10293.93, max 10931.97)","12244.72 (min 12073.39, max 12524.89)","11588.63 (min 10936.06, max 11915.26)","11485.68 (min 11186.52, max 11859.97)","11062.08 (min 10062.93, max 11729.32)"
    "aes-256-cbc","64","2737.18 (min 2666.58, max 2825.81)","3160.41 (min 3105.58, max 3229.97)","2998.28 (min 2854.14, max 3082.26)","2983.99 (min 2905.00, max 3079.02)","2849.19 (min 2278.72, max 3032.21)"
    "aes-256-cbc","8192","135539.60 (min 134206.81, max 139026.43)","135822.10 (min 134886.74, max 136724.48)","130320.38 (min 127183.53, max 132096.00)","129685.32 (min 127896.23, max 132025.00)","126333.75 (min 119608.66, max 129922.39)"
    "aes-256-ecb","1024","35183.27 (min 33047.21, max 36583.77)","41374.40 (min 38304.09, max 42684.42)","39144.96 (min 35275.78, max 40973.99)","38510.53 (min 36133.21, max 40186.20)","37259.33 (min 35075.75, max 39460.52)"
    "aes-256-ecb","16","688.04 (min 673.86, max 705.91)","796.68 (min 778.37, max 815.21)","759.26 (min 733.28, max 780.14)","752.23 (min 732.42, max 770.92)","683.14 (min 558.11, max 761.83)"
    "aes-256-ecb","16384","171541.39 (min 168028.84, max 176084.31)","168814.01 (min 167291.56, max 170896.04)","162942.07 (min 160552.28, max 165292.71)","161840.16 (min 159094.10, max 164397.06)","159737.99 (min 152535.04, max 161884.84)"
    "aes-256-ecb","256","10547.98 (min 10340.10, max 10919.00)","12362.50 (min 12067.67, max 12651.43)","11694.17 (min 11002.79, max 12167.25)","11547.19 (min 11133.27, max 11939.24)","11088.31 (min 9803.09, max 11794.26)"
    "aes-256-ecb","64","2746.00 (min 2686.10, max 2812.93)","3189.71 (min 3113.24, max 3260.84)","3021.22 (min 2878.81, max 3125.76)","3006.09 (min 2917.38, max 3083.39)","2891.68 (min 2405.48, max 3048.06)"
    "aes-256-ecb","8192","137085.61 (min 134965.93, max 141301.08)","139521.73 (min 138158.08, max 140260.69)","134237.30 (min 131631.79, max 135905.28)","133247.10 (min 131866.62, max 135839.74)","131826.48 (min 124106.07, max 133944.66)"
    "des3","1024","33997.80 (min 32402.09, max 35328.00)","35672.01 (min 33504.94, max 36675.24)","34267.51 (min 31854.25, max 35393.19)","34070.87 (min 32717.82, max 34899.29)","33115.61 (min 28200.96, max 35017.39)"
    "des3","16","688.09 (min 666.89, max 703.85)","792.24 (min 778.47, max 814.60)","751.96 (min 728.50, max 769.32)","748.10 (min 732.91, max 765.69)","694.83 (min 562.50, max 753.63)"
    "des3","16384","116557.60 (min 115403.43, max 117342.21)","94812.11 (min 94333.61, max 95354.88)","93750.16 (min 92760.75, max 94868.82)","94071.47 (min 93082.97, max 94557.53)","93539.53 (min 92225.54, max 94382.76)"
    "des3","256","10329.16 (min 10096.13, max 10576.81)","11606.56 (min 11440.98, max 11923.03)","10978.13 (min 10591.57, max 11319.55)","10925.16 (min 10786.56, max 11116.63)","10565.60 (min 9644.63, max 11026.94)"
    "des3","64","2742.92 (min 2661.08, max 2820.42)","3157.30 (min 3104.17, max 3239.85)","3003.07 (min 2908.80, max 3071.57)","2971.77 (min 2894.78, max 3028.14)","2793.12 (min 2485.44, max 3003.99)"
    "des3","8192","99194.20 (min 97812.48, max 99915.09)","85846.70 (min 85445.29, max 86297.26)","83747.27 (min 82302.29, max 84161.88)","84612.19 (min 84022.61, max 85128.53)","83551.30 (min 79233.02, max 84639.74)"
    "sha1","1024","68636.96 (min 65616.90, max 71213.40)","68619.37 (min 62956.20, max 71213.06)","67985.18 (min 64463.53, max 70482.60)","67243.63 (min 65565.01, max 69621.08)","66840.75 (min 64685.40, max 68334.59)"
    "sha1","16","1151.60 (min 1103.37, max 1192.99)","1154.28 (min 1050.12, max 1200.49)","1139.20 (min 1087.91, max 1193.06)","1124.81 (min 1077.95, max 1169.72)","1122.06 (min 1091.29, max 1150.29)"
    "sha1","16384","497450.55 (min 487565.99, max 506380.29)","499435.57 (min 480843.09, max 511093.42)","497180.22 (min 488614.57, max 505140.57)","494081.37 (min 485321.39, max 504392.36)","493158.95 (min 486916.10, max 498614.27)"
    "sha1","256","18123.01 (min 17304.06, max 18733.31)","18122.35 (min 16475.56, max 18773.85)","17984.65 (min 17378.05, max 18694.06)","17719.75 (min 17213.01, max 18311.00)","17595.49 (min 17096.79, max 18012.67)"
    "sha1","64","4579.91 (min 4378.43, max 4748.48)","4591.64 (min 4181.93, max 4768.51)","4556.69 (min 4400.73, max 4698.79)","4480.39 (min 4345.22, max 4626.62)","4473.90 (min 4325.85, max 4561.26)"
    "sha1","8192","349260.00 (min 339916.12, max 360153.09)","348411.43 (min 331497.47, max 359328.43)","347996.16 (min 343911.08, max 357485.23)","345303.97 (min 339626.67, max 352018.43)","345509.61 (min 336235.18, max 350041.43)"
    "sha256","1024","67888.70 (min 62777.00, max 70057.30)","68020.09 (min 63336.79, max 70715.73)","67471.73 (min 64848.90, max 69846.02)","66229.37 (min 64284.67, max 69204.99)","65836.75 (min 63520.09, max 67617.11)"
    "sha256","16","1139.68 (min 1056.86, max 1176.56)","1152.26 (min 1070.15, max 1200.56)","1140.28 (min 1093.05, max 1168.89)","1121.90 (min 1087.47, max 1171.69)","1115.80 (min 1071.54, max 1146.79)"
    "sha256","16384","490626.16 (min 479532.37, max 503179.95)","495154.73 (min 482623.49, max 503491.24)","492105.73 (min 484223.66, max 499570.01)","486213.57 (min 479980.20, max 494146.90)","483068.59 (min 475496.45, max 489401.00)"
    "sha256","256","17937.54 (min 16430.76, max 18640.90)","17966.91 (min 16698.97, max 18705.92)","17881.76 (min 17058.82, max 18549.85)","17541.84 (min 17025.79, max 18345.47)","17479.17 (min 16819.88, max 17899.52)"
    "sha256","64","4546.32 (min 4206.36, max 4684.84)","4574.55 (min 4251.84, max 4757.97)","4544.79 (min 4352.49, max 4672.38)","4450.35 (min 4280.30, max 4656.45)","4449.25 (min 4276.80, max 4556.44)"
    "sha256","8192","344316.81 (min 330181.29, max 355923.29)","347217.08 (min 334995.46, max 355560.11)","344332.29 (min 338253.14, max 349323.26)","340139.78 (min 333441.71, max 350085.12)","338332.33 (min 331601.24, max 345817.09)"
    "sha512","1024","51610.97 (min 50094.42, max 52599.13)","51306.71 (min 49361.24, max 52463.96)","50903.64 (min 48561.49, max 52422.66)","50896.40 (min 47777.11, max 52441.77)","50505.25 (min 49252.01, max 51585.71)"
    "sha512","16","1129.24 (min 1088.44, max 1175.50)","1135.47 (min 1076.06, max 1182.29)","1122.56 (min 1022.35, max 1169.29)","1114.81 (min 1024.99, max 1165.53)","1100.99 (min 1065.39, max 1129.10)"
    "sha512","16384","150327.30 (min 149099.86, max 151306.24)","150094.66 (min 149034.33, max 151328.09)","149862.17 (min 148897.79, max 151109.63)","149778.56 (min 147789.14, max 151628.46)","149517.65 (min 148701.18, max 150487.04)"
    "sha512","256","16524.79 (min 15969.79, max 17169.75)","16451.12 (min 15655.59, max 17099.09)","16304.93 (min 15298.39, max 16899.24)","16194.89 (min 15175.59, max 16732.25)","16134.11 (min 15631.45, max 16408.49)"
    "sha512","64","4538.79 (min 4381.59, max 4704.38)","4549.32 (min 4312.09, max 4734.83)","4507.33 (min 4147.65, max 4667.71)","4482.78 (min 4103.98, max 4671.68)","4445.31 (min 4289.86, max 4597.95)"
    "sha512","8192","132748.63 (min 131710.98, max 133884.59)","132707.25 (min 131517.10, max 134026.58)","132448.71 (min 130722.47, max 134146.73)","132182.88 (min 129092.27, max 134111.23)","131850.24 (min 130916.35, max 133477.72)"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","j7200-evm: CPU Load","j721e-idk-gw: CPU Load","j721s2-evm: CPU Load","j742s2_evm-fs: CPU Load","j784s4-evm: CPU Load"

    "aes-128-cbc","32.33 (min 31.00, max 33.00)","33.23 (min 33.00, max 34.00)","32.17 (min 31.00, max 33.00)","32.64 (min 32.00, max 33.00)","32.10 (min 30.00, max 33.00)"
    "aes-128-ecb","32.58 (min 32.00, max 33.00)","33.92 (min 33.00, max 35.00)","32.75 (min 32.00, max 34.00)","32.91 (min 28.00, max 34.00)","33.10 (min 32.00, max 34.00)"
    "aes-192-cbc","32.42 (min 32.00, max 33.00)","33.23 (min 33.00, max 34.00)","32.17 (min 31.00, max 33.00)","32.64 (min 32.00, max 33.00)","32.80 (min 32.00, max 34.00)"
    "aes-192-ecb","32.50 (min 32.00, max 33.00)","33.54 (min 33.00, max 34.00)","32.75 (min 32.00, max 34.00)","32.91 (min 32.00, max 34.00)","32.50 (min 32.00, max 33.00)"
    "aes-256-cbc","32.33 (min 32.00, max 33.00)","32.85 (min 32.00, max 34.00)","31.92 (min 31.00, max 33.00)","32.36 (min 31.00, max 33.00)","32.20 (min 31.00, max 33.00)"
    "aes-256-ecb","32.42 (min 32.00, max 33.00)","33.15 (min 32.00, max 34.00)","32.25 (min 31.00, max 33.00)","32.73 (min 32.00, max 34.00)","32.20 (min 31.00, max 33.00)"
    "des3","30.42 (min 29.00, max 32.00)","29.85 (min 29.00, max 31.00)","28.75 (min 28.00, max 30.00)","29.55 (min 29.00, max 30.00)","29.30 (min 28.00, max 30.00)"
    "sha1","97.00","97.00","96.67 (min 96.00, max 97.00)","97.00 (min 95.00, max 98.00)","96.80 (min 96.00, max 97.00)"
    "sha256","97.00","97.00","96.67 (min 96.00, max 97.00)","97.09 (min 96.00, max 98.00)","96.80 (min 96.00, max 97.00)"
    "sha512","97.00","97.00","96.42 (min 96.00, max 97.00)","97.00 (min 94.00, max 98.00)","96.80 (min 96.00, max 97.00)"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

.. code-block:: console

    time -v openssl speed -elapsed -evp aes-128-cbc

 




IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","j721e-idk-gw: Throughput (Mbps)","j721e-idk-gw: Packets/Sec","j721e-idk-gw: CPU Load"

    "3des","183.85 (min 183.50, max 184.20)","16.00","39.65 (min 39.09, max 40.21)"
    "aes128","445.00 (min 0.20, max 693.30)","39.40 (min 0.00, max 61.00)","81.66 (min 58.66, max 99.82)"
    "aes192","676.30","60.00","59.36"
    "aes256","96.14 (min 0.10, max 309.80)","8.40 (min 0.00, max 27.00)","87.32 (min 64.27, max 98.15)"

 
 

 





