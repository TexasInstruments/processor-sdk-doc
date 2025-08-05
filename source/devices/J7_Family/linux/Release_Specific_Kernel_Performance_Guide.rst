
======================================
 Linux 11.01 Performance Guide
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

    "af_unix_sock_stream_latency (microsec)","19.49","26.99","19.54","19.64","19.45","30.57","20.38","20.61"
    "af_unix_socket_stream_bandwidth (MBs)","2118.33","3054.86","1646.55","1963.24","2028.55","1056.55","2988.58","2000.93"
    "bw_file_rd-io-1mb (MB/s)","3328.08","4094.55","3805.18","3428.37","3235.08","1342.28","4006.41","3814.50"
    "bw_file_rd-o2c-1mb (MB/s)","1443.26","2017.61","1518.03","1851.85","1470.59","717.75","2063.27","1855.29"
    "bw_mem-bcopy-16mb (MB/s)","3768.25","2744.90","2358.14","2813.43","3412.24","1725.63","3378.74","2728.98"
    "bw_mem-bcopy-1mb (MB/s)","4656.16","9864.82","3342.00","4677.27","4431.31","1863.46","9826.15","9692.76"
    "bw_mem-bcopy-2mb (MB/s)","3928.50","4201.68","2457.87","3857.62","3597.77","1659.20","4823.75","3780.72"
    "bw_mem-bcopy-4mb (MB/s)","3737.74","3318.95","2349.72","3863.99","3451.25","1608.36","4169.56","3226.33"
    "bw_mem-bcopy-8mb (MB/s)","3752.93","2895.93","2337.81","3055.77","3403.77","1695.09","3495.48","2888.09"
    "bw_mem-bzero-16mb (MB/s)","10841.94","10862.19","2339.87","9667.67","10585.51","7126.95","10362.69","10865.87"
    "bw_mem-bzero-1mb (MB/s)","8747.36 (min 4656.16, max 12838.55)","11793.81 (min 9864.82, max 13722.80)","4096.30 (min 3342.00, max 4850.60)","8632.47 (min 4677.27, max 12587.66)","8481.32 (min 4431.31, max 12531.33)","4495.52 (min 1863.46, max 7127.58)","11706.56 (min 9826.15, max 13586.96)","11725.46 (min 9692.76, max 13758.15)"
    "bw_mem-bzero-2mb (MB/s)","7688.03 (min 3928.50, max 11447.56)","8923.10 (min 4201.68, max 13644.52)","2694.41 (min 2457.87, max 2930.94)","8032.94 (min 3857.62, max 12208.26)","7445.30 (min 3597.77, max 11292.83)","4391.49 (min 1659.20, max 7123.78)","9026.11 (min 4823.75, max 13228.46)","8725.76 (min 3780.72, max 13670.79)"
    "bw_mem-bzero-4mb (MB/s)","7369.42 (min 3737.74, max 11001.10)","7814.44 (min 3318.95, max 12309.92)","2412.29 (min 2349.72, max 2474.86)","7904.38 (min 3863.99, max 11944.76)","7074.17 (min 3451.25, max 10697.09)","4373.06 (min 1608.36, max 7137.76)","7902.12 (min 4169.56, max 11634.67)","7741.50 (min 3226.33, max 12256.67)"
    "bw_mem-bzero-8mb (MB/s)","7349.36 (min 3752.93, max 10945.78)","7096.69 (min 2895.93, max 11297.44)","2346.07 (min 2337.81, max 2354.33)","7330.24 (min 3055.77, max 11604.71)","7014.85 (min 3403.77, max 10625.93)","4417.06 (min 1695.09, max 7139.03)","7080.06 (min 3495.48, max 10664.64)","7074.88 (min 2888.09, max 11261.66)"
    "bw_mem-cp-16mb (MB/s)","2182.81","2150.54","983.41","1545.89","2129.93","850.16","2109.15","2168.32"
    "bw_mem-cp-1mb (MB/s)","7748.72 (min 2453.13, max 13044.31)","8426.00 (min 3105.02, max 13746.98)","3056.28 (min 1269.04, max 4843.52)","7101.47 (min 1702.93, max 12500.00)","7521.44 (min 2628.12, max 12414.76)","4177.88 (min 876.73, max 7479.02)","8745.61 (min 3953.31, max 13537.91)","8367.72 (min 2997.18, max 13738.25)"
    "bw_mem-cp-2mb (MB/s)","6947.43 (min 2181.82, max 11713.03)","7991.99 (min 2504.02, max 13479.96)","1971.90 (min 1022.49, max 2921.31)","6875.20 (min 1618.38, max 12132.02)","6725.36 (min 2142.47, max 11308.25)","4024.78 (min 822.82, max 7226.74)","7280.57 (min 2339.57, max 12221.57)","8056.53 (min 2466.09, max 13646.97)"
    "bw_mem-cp-4mb (MB/s)","6556.81 (min 2146.69, max 10966.92)","7384.34 (min 2489.88, max 12278.80)","1722.38 (min 977.52, max 2467.23)","6767.25 (min 1587.51, max 11946.99)","6389.05 (min 2101.94, max 10676.16)","4042.65 (min 872.89, max 7212.41)","7078.59 (min 2558.77, max 11598.41)","7380.13 (min 2510.20, max 12250.05)"
    "bw_mem-cp-8mb (MB/s)","6532.72 (min 2166.26, max 10899.18)","6718.39 (min 2204.77, max 11232.01)","1673.26 (min 985.59, max 2360.93)","6599.61 (min 1473.30, max 11725.91)","6348.92 (min 2094.79, max 10603.05)","4040.86 (min 900.39, max 7181.33)","6386.90 (min 2139.04, max 10634.76)","6775.63 (min 2211.78, max 11339.48)"
    "bw_mem-fcp-16mb (MB/s)","3728.73","2661.79","2389.13","2787.94","3368.07","1616.81","3376.60","2644.19"
    "bw_mem-fcp-1mb (MB/s)","8384.30 (min 3930.05, max 12838.55)","10065.93 (min 6409.05, max 13722.80)","4105.83 (min 3361.05, max 4850.60)","8276.89 (min 3966.11, max 12587.66)","8247.29 (min 3963.25, max 12531.33)","4369.96 (min 1612.33, max 7127.58)","10072.80 (min 6558.64, max 13586.96)","10197.24 (min 6636.33, max 13758.15)"
    "bw_mem-fcp-2mb (MB/s)","7669.69 (min 3891.81, max 11447.56)","8499.18 (min 3353.83, max 13644.52)","2737.51 (min 2544.07, max 2930.94)","8057.95 (min 3907.64, max 12208.26)","7400.46 (min 3508.09, max 11292.83)","4295.97 (min 1468.16, max 7123.78)","8705.92 (min 4183.37, max 13228.46)","8498.98 (min 3327.17, max 13670.79)"
    "bw_mem-fcp-4mb (MB/s)","7408.59 (min 3816.07, max 11001.10)","7706.85 (min 3103.78, max 12309.92)","2438.87 (min 2402.88, max 2474.86)","7876.06 (min 3807.35, max 11944.76)","7057.36 (min 3417.63, max 10697.09)","4362.22 (min 1586.67, max 7137.76)","7816.94 (min 3999.20, max 11634.67)","7667.39 (min 3078.11, max 12256.67)"
    "bw_mem-fcp-8mb (MB/s)","7351.12 (min 3756.46, max 10945.78)","7052.72 (min 2808.00, max 11297.44)","2364.99 (min 2354.33, max 2375.65)","7328.69 (min 3052.66, max 11604.71)","7002.87 (min 3379.81, max 10625.93)","4371.92 (min 1604.81, max 7139.03)","7040.02 (min 3415.40, max 10664.64)","7035.08 (min 2808.50, max 11261.66)"
    "bw_mem-frd-16mb (MB/s)","4581.90","3208.99","6327.45","4794.73","4175.37","1754.00","4208.86","3202.56"
    "bw_mem-frd-1mb (MB/s)","4512.05 (min 3930.05, max 5094.04)","7077.01 (min 6409.05, max 7744.96)","4655.64 (min 3361.05, max 5950.23)","4730.31 (min 3966.11, max 5494.51)","4500.97 (min 3963.25, max 5038.69)","1796.98 (min 1612.33, max 1981.62)","6960.91 (min 6558.64, max 7363.18)","7218.47 (min 6636.33, max 7800.61)"
    "bw_mem-frd-2mb (MB/s)","4456.53 (min 3891.81, max 5021.24)","3809.11 (min 3353.83, max 4264.39)","4469.20 (min 2544.07, max 6394.32)","4849.75 (min 3907.64, max 5791.86)","4088.22 (min 3508.09, max 4668.35)","1489.48 (min 1468.16, max 1510.80)","4693.92 (min 4183.37, max 5204.46)","3766.84 (min 3327.17, max 4206.50)"
    "bw_mem-frd-4mb (MB/s)","4221.70 (min 3816.07, max 4627.33)","3375.71 (min 3103.78, max 3647.64)","4359.75 (min 2402.88, max 6316.62)","4728.04 (min 3807.35, max 5648.72)","3824.85 (min 3417.63, max 4232.06)","1615.26 (min 1586.67, max 1643.84)","4480.99 (min 3999.20, max 4962.78)","3261.41 (min 3078.11, max 3444.71)"
    "bw_mem-frd-8mb (MB/s)","4166.56 (min 3756.46, max 4576.66)","3218.06 (min 2808.00, max 3628.12)","4347.39 (min 2375.65, max 6319.12)","4228.58 (min 3052.66, max 5404.49)","3780.14 (min 3379.81, max 4180.46)","1678.35 (min 1604.81, max 1751.89)","4114.44 (min 3415.40, max 4813.48)","3125.18 (min 2808.50, max 3441.85)"
    "bw_mem-fwr-16mb (MB/s)","10873.26","10827.27","2336.45","9637.10","10557.57","7187.78","10389.61","10889.91"
    "bw_mem-fwr-1mb (MB/s)","9069.18 (min 5094.04, max 13044.31)","10745.97 (min 7744.96, max 13746.98)","5396.88 (min 4843.52, max 5950.23)","8997.26 (min 5494.51, max 12500.00)","8726.73 (min 5038.69, max 12414.76)","4730.32 (min 1981.62, max 7479.02)","10450.55 (min 7363.18, max 13537.91)","10769.43 (min 7800.61, max 13738.25)"
    "bw_mem-fwr-2mb (MB/s)","8367.14 (min 5021.24, max 11713.03)","8872.18 (min 4264.39, max 13479.96)","4657.82 (min 2921.31, max 6394.32)","8961.94 (min 5791.86, max 12132.02)","7988.30 (min 4668.35, max 11308.25)","4368.77 (min 1510.80, max 7226.74)","8713.02 (min 5204.46, max 12221.57)","8926.74 (min 4206.50, max 13646.97)"
    "bw_mem-fwr-4mb (MB/s)","7797.13 (min 4627.33, max 10966.92)","7963.22 (min 3647.64, max 12278.80)","4391.93 (min 2467.23, max 6316.62)","8797.86 (min 5648.72, max 11946.99)","7454.11 (min 4232.06, max 10676.16)","4428.13 (min 1643.84, max 7212.41)","8280.60 (min 4962.78, max 11598.41)","7847.38 (min 3444.71, max 12250.05)"
    "bw_mem-fwr-8mb (MB/s)","7737.92 (min 4576.66, max 10899.18)","7430.07 (min 3628.12, max 11232.01)","4340.03 (min 2360.93, max 6319.12)","8565.20 (min 5404.49, max 11725.91)","7391.76 (min 4180.46, max 10603.05)","4466.61 (min 1751.89, max 7181.33)","7724.12 (min 4813.48, max 10634.76)","7390.67 (min 3441.85, max 11339.48)"
    "bw_mem-rd-16mb (MB/s)","5320.92","3954.03","6586.17","5105.30","4887.73","1796.54","4996.88","3789.67"
    "bw_mem-rd-1mb (MB/s)","6102.56 (min 3893.81, max 8311.30)","16303.55 (min 15309.80, max 17297.30)","7240.87 (min 4511.28, max 9970.46)","5502.57 (min 3504.67, max 7500.47)","7741.53 (min 6793.98, max 8689.08)","1792.57 (min 1535.57, max 2049.56)","16462.29 (min 15599.19, max 17325.39)","15215.08 (min 13132.85, max 17297.30)"
    "bw_mem-rd-2mb (MB/s)","4425.53 (min 2839.40, max 6011.65)","4515.42 (min 3360.09, max 5670.74)","4006.14 (min 977.84, max 7034.43)","3810.90 (min 1161.61, max 6460.19)","4282.56 (min 3099.57, max 5465.55)","1593.31 (min 1408.20, max 1778.41)","6288.66 (min 4897.67, max 7679.65)","4186.10 (min 2722.48, max 5649.72)"
    "bw_mem-rd-4mb (MB/s)","3918.83 (min 2402.88, max 5434.78)","3933.67 (min 3427.00, max 4440.33)","3710.90 (min 784.62, max 6637.17)","3706.83 (min 1206.09, max 6207.57)","3660.61 (min 2365.46, max 4955.75)","1676.57 (min 1571.92, max 1781.21)","4521.06 (min 3107.40, max 5934.72)","3798.41 (min 3405.41, max 4191.41)"
    "bw_mem-rd-8mb (MB/s)","3797.59 (min 2269.83, max 5325.35)","3868.56 (min 3331.02, max 4406.10)","3656.34 (min 746.69, max 6565.99)","3852.32 (min 1888.57, max 5816.07)","3564.33 (min 2246.88, max 4881.77)","1674.90 (min 1576.35, max 1773.44)","4393.02 (min 2909.09, max 5876.95)","3750.89 (min 3326.40, max 4175.37)"
    "bw_mem-rdwr-16mb (MB/s)","2229.03","2392.70","750.43","1796.95","2139.32","1682.09","2149.38","2342.95"
    "bw_mem-rdwr-1mb (MB/s)","3295.13 (min 2453.13, max 4137.12)","6359.33 (min 3105.02, max 9613.64)","2601.86 (min 1269.04, max 3934.68)","2235.07 (min 1702.93, max 2767.21)","3294.26 (min 2628.12, max 3960.40)","1292.63 (min 876.73, max 1708.53)","6783.48 (min 3953.31, max 9613.64)","6275.37 (min 2997.18, max 9553.56)"
    "bw_mem-rdwr-2mb (MB/s)","2441.74 (min 2181.82, max 2701.66)","3369.84 (min 2504.02, max 4235.66)","1003.70 (min 984.90, max 1022.49)","1415.16 (min 1211.94, max 1618.38)","2359.90 (min 2142.47, max 2577.32)","1095.64 (min 822.82, max 1368.46)","3380.84 (min 2339.57, max 4422.11)","3054.54 (min 2466.09, max 3642.99)"
    "bw_mem-rdwr-4mb (MB/s)","2256.60 (min 2146.69, max 2366.51)","2704.26 (min 2489.88, max 2918.64)","885.19 (min 792.86, max 977.52)","1967.98 (min 1587.51, max 2348.45)","2194.65 (min 2101.94, max 2287.35)","1223.07 (min 872.89, max 1573.25)","2711.28 (min 2558.77, max 2863.79)","2690.60 (min 2510.20, max 2870.99)"
    "bw_mem-rdwr-8mb (MB/s)","2219.17 (min 2166.26, max 2272.08)","2507.87 (min 2204.77, max 2810.96)","870.94 (min 756.29, max 985.59)","1840.71 (min 1473.30, max 2208.11)","2137.32 (min 2094.79, max 2179.84)","1237.44 (min 900.39, max 1574.49)","2462.04 (min 2139.04, max 2785.03)","2494.78 (min 2211.78, max 2777.78)"
    "bw_mem-wr-16mb (MB/s)","2233.08","2710.03","745.16","1757.66","2224.38","1698.51","2198.41","2743.95"
    "bw_mem-wr-1mb (MB/s)","4015.47 (min 3893.81, max 4137.12)","13455.47 (min 9613.64, max 17297.30)","4222.98 (min 3934.68, max 4511.28)","3135.94 (min 2767.21, max 3504.67)","6324.74 (min 3960.40, max 8689.08)","1622.05 (min 1535.57, max 1708.53)","13469.52 (min 9613.64, max 17325.39)","13425.43 (min 9553.56, max 17297.30)"
    "bw_mem-wr-2mb (MB/s)","2770.53 (min 2701.66, max 2839.40)","3797.88 (min 3360.09, max 4235.66)","981.37 (min 977.84, max 984.90)","1186.78 (min 1161.61, max 1211.94)","2838.45 (min 2577.32, max 3099.57)","1388.33 (min 1368.46, max 1408.20)","4659.89 (min 4422.11, max 4897.67)","3182.74 (min 2722.48, max 3642.99)"
    "bw_mem-wr-4mb (MB/s)","2384.70 (min 2366.51, max 2402.88)","3172.82 (min 2918.64, max 3427.00)","788.74 (min 784.62, max 792.86)","1777.27 (min 1206.09, max 2348.45)","2326.41 (min 2287.35, max 2365.46)","1572.59 (min 1571.92, max 1573.25)","2985.60 (min 2863.79, max 3107.40)","3138.20 (min 2870.99, max 3405.41)"
    "bw_mem-wr-8mb (MB/s)","2270.96 (min 2269.83, max 2272.08)","3070.99 (min 2810.96, max 3331.02)","751.49 (min 746.69, max 756.29)","2048.34 (min 1888.57, max 2208.11)","2213.36 (min 2179.84, max 2246.88)","1575.42 (min 1574.49, max 1576.35)","2847.06 (min 2785.03, max 2909.09)","3052.09 (min 2777.78, max 3326.40)"
    "bw_mmap_rd-mo-1mb (MB/s)","8788.33","12897.37","12239.90","8744.76","8594.35","1985.56","12909.09","12909.09"
    "bw_mmap_rd-o2c-1mb (MB/s)","1517.96","2441.31","1475.74","1583.67","1383.13","716.08","2385.76","2416.29"
    "bw_pipe (MB/s)","1009.47","785.53","772.07","981.03","1004.81","759.30","1025.32","846.56"
    "bw_unix (MB/s)","2118.33","3054.86","1646.55","1963.24","2028.55","1056.55","2988.58","2000.93"
    "lat_connect (us)","37.52","37.11","37.25","36.70","37.27","57.40","37.26","37.19"
    "lat_ctx-2-128k (us)","4.88","5.01","5.03","4.83","4.96","7.41","5.22","8.12"
    "lat_ctx-2-256k (us)","4.12","4.34","4.22","4.71","4.18","7.76","4.18","4.37"
    "lat_ctx-4-128k (us)","5.26","6.60","4.80","4.75","4.80","7.16","4.65","4.84"
    "lat_ctx-4-256k (us)","3.69","4.89","4.09","4.38","4.63","6.60","3.25","6.82"
    "lat_fs-0k (num_files)","402.00","409.00","361.00","423.00","406.00","214.00","392.00","400.00"
    "lat_fs-10k (num_files)","170.00","177.00","163.00","155.00","173.00","99.00","183.00","194.00"
    "lat_fs-1k (num_files)","236.00","255.00","233.00","240.00","239.00","151.00","256.00","245.00"
    "lat_fs-4k (num_files)","249.00","261.00","237.00","255.00","218.00","171.00","260.00","259.00"
    "lat_mem_rd-stride128-sz1000k (ns)","13.00","5.72","12.46","12.08","13.29","33.35","5.90","5.65"
    "lat_mem_rd-stride128-sz125k (ns)","5.57","5.65","5.57","5.57","5.57","5.56","5.65","5.65"
    "lat_mem_rd-stride128-sz250k (ns)","5.57","5.65","5.57","5.57","5.57","5.82","5.65","5.65"
    "lat_mem_rd-stride128-sz31k (ns)","3.35","4.28","4.66","3.77","3.32","2.17","4.74","3.39"
    "lat_mem_rd-stride128-sz50 (ns)","2.00","2.00","2.00","2.00","2.00","2.15","2.00","2.00"
    "lat_mem_rd-stride128-sz500k (ns)","6.41","5.65","5.57","5.57","5.57","13.14","5.65","5.65"
    "lat_mem_rd-stride128-sz62k (ns)","5.12","5.20","5.12","5.57","5.12","5.26","5.65","5.65"
    "lat_mmap-1m (us)","28.00","29.00","35.00","28.00","29.00","57.00","28.00","34.00"
    "lat_ops-double-add (ns)","1.96","1.96","1.96","1.96","1.96","2.86","1.96","1.96"
    "lat_ops-double-div (ns)","9.02","9.01","9.01","9.01","9.01","15.75","9.01","9.01"
    "lat_ops-double-mul (ns)","2.00","2.00","2.00","2.00","2.00","2.86","2.00","2.00"
    "lat_ops-float-add (ns)","1.96","1.96","1.96","1.96","1.96","2.86","1.96","1.96"
    "lat_ops-float-div (ns)","5.51","5.51","5.51","5.51","5.51","9.30","5.51","5.51"
    "lat_ops-float-mul (ns)","2.00","2.00","2.00","2.00","2.00","2.86","2.00","2.00"
    "lat_ops-int-add (ns)","0.50","0.50","0.50","0.50","0.50","0.72","0.50","0.50"
    "lat_ops-int-bit (ns)","0.33","0.33","0.33","0.33","0.33","0.48","0.33","0.33"
    "lat_ops-int-div (ns)","4.00","4.00","4.01","4.01","4.01","4.29","4.00","4.00"
    "lat_ops-int-mod (ns)","4.68","4.67","4.67","4.67","4.68","4.54","4.67","4.67"
    "lat_ops-int-mul (ns)","1.52","1.52","1.52","1.52","1.52","3.13","1.52","1.52"
    "lat_ops-int64-add (ns)","0.50","0.50","0.50","0.50","0.50","0.72","0.50","0.50"
    "lat_ops-int64-bit (ns)","0.33","0.33","0.33","0.33","0.33","0.48","0.33","0.33"
    "lat_ops-int64-div (ns)","3.00","3.00","3.00","3.00","3.00","6.80","3.00","3.00"
    "lat_ops-int64-mod (ns)","5.67","5.68","5.67","5.68","5.68","5.26","5.67","5.67"
    "lat_ops-int64-mul (ns)","2.52","2.52","2.52","2.52","2.52","3.56","2.52","2.52"
    "lat_pagefault (us)","0.45","0.43","0.25","0.24","0.26","0.54","0.24","0.24"
    "lat_pipe (us)","14.30","20.23","13.79","14.77","14.34","25.49","16.00","21.33"
    "lat_proc-exec (us)","419.54","411.00","405.38","379.43","426.85","728.00","329.24","423.85"
    "lat_proc-fork (us)","380.13","394.23","381.27","340.38","388.87","655.25","299.94","360.06"
    "lat_proc-proccall (us)","0.00","0.00","0.00","0.00","0.00","0.01","0.00","0.00"
    "lat_select (us)","11.47","11.44","11.46","11.46","11.48","33.96","11.50","11.50"
    "lat_sem (us)","2.30","2.71","2.33","1.99","2.26","3.11","2.00","2.96"
    "lat_sig-catch (us)","2.75","2.66","2.70","2.69","2.75","5.30","2.73","2.71"
    "lat_sig-install (us)","0.56","0.55","0.55","0.54","0.55","0.65","0.56","0.55"
    "lat_sig-prot (us)","0.54","0.47","0.48","0.54","0.48","0.56","0.39","0.59"
    "lat_syscall-fstat (us)","1.02","0.99","0.96","0.99","0.97","1.95","0.98","1.01"
    "lat_syscall-null (us)","0.43","0.44","0.43","0.41","0.43","0.46","0.42","0.39"
    "lat_syscall-open (us)","146.38","204.16","152.38","115.95","129.05","174.87","137.22","425.86"
    "lat_syscall-read (us)","0.51","0.52","0.50","0.49","0.51","0.79","0.51","0.52"
    "lat_syscall-stat (us)","2.14","2.17","2.18","2.15","2.10","4.82","2.14","2.15"
    "lat_syscall-write (us)","0.48","0.48","0.48","0.48","0.46","0.80","0.48","0.48"
    "lat_tcp (us)","0.82","0.84","0.81","0.81","0.80","0.92","0.83","0.82"
    "lat_unix (us)","19.49","26.99","19.54","19.64","19.45","30.57","20.38","20.61"
    "latency_for_0.50_mb_block_size (nanosec)","6.41","5.65","5.57","5.57","5.57","13.14","5.65","5.65"
    "latency_for_1.00_mb_block_size (nanosec)","6.50 (min 0.00, max 13.00)","2.86 (min 0.00, max 5.72)","6.23 (min 0.00, max 12.46)","6.04 (min 0.00, max 12.08)","6.64 (min 0.00, max 13.29)","16.68 (min 0.00, max 33.35)","2.95 (min 0.00, max 5.90)","2.82 (min 0.00, max 5.65)"
    "pipe_bandwidth (MBs)","1009.47","785.53","772.07","981.03","1004.81","759.30","1025.32","846.56"
    "pipe_latency (microsec)","14.30","20.23","13.79","14.77","14.34","25.49","16.00","21.33"
    "procedure_call (microsec)","0.00","0.00","0.00","0.00","0.00","0.01","0.00","0.00"
    "select_on_200_tcp_fds (microsec)","11.47","11.44","11.46","11.46","11.48","33.96","11.50","11.50"
    "semaphore_latency (microsec)","2.30","2.71","2.33","1.99","2.26","3.11","2.00","2.96"
    "signal_handler_latency (microsec)","0.56","0.55","0.55","0.54","0.55","0.65","0.56","0.55"
    "signal_handler_overhead (microsec)","2.75","2.66","2.70","2.69","2.75","5.30","2.73","2.71"
    "tcp_ip_connection_cost_to_localhost (microsec)","37.52","37.11","37.25","36.70","37.27","57.40","37.26","37.19"
    "tcp_latency_using_localhost (microsec)","0.82","0.84","0.81","0.81","0.80","0.92","0.83","0.82"




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

    "cpu_clock (MHz)","2000.00","2000.00","2000.00","2000.00","2000.00","1400.00","2000.00","2000.00"
    "dhrystone_per_mhz (DMIPS/MHz)","5.70","5.70","5.70","5.70","5.20","2.90","5.70","5.70"
    "dhrystone_per_second (DhrystoneP)","20000000.00","20000000.00","20000000.00","20000000.00","18181818.00","7142857.00","20000000.00","20000000.00"




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

    "linpack (Kflops)","2546985.00","2479837.00","2475366.00","2459409.00","2598057.00","577565.00","2501518.00","2382605.00"




NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "assignment (Iterations)","31.96","31.88","31.87","31.73","31.87","14.46","31.86","31.86"
    "fourier (Iterations)","60069.00","59866.00","59966.00","60053.00","65718.00","22831.00","65695.00","60104.00"
    "fp_emulation (Iterations)","387.96","387.98","388.00","387.93","387.91","215.65","387.95","387.84"
    "huffman (Iterations)","2411.00","2406.50","2410.90","2415.20","2413.90","1183.90","2406.20","2407.30"
    "idea (Iterations)","7996.20","7996.50","7996.30","7996.80","7996.30","3444.70","7996.20","7996.90"
    "lu_decomposition (Iterations)","1365.90","1366.00","1360.00","1362.70","1372.30","529.33","1377.30","1379.40"
    "neural_net (Iterations)","29.02","28.76","27.71","29.02","28.79","8.66","28.76","29.02"
    "numeric_sort (Iterations)","881.70","881.12","883.39","880.28","882.85","621.99","871.09","883.31"
    "string_sort (Iterations)","349.95","361.94","350.71","358.01","360.87","163.93","348.62","350.53"




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

    "add (MB/s)","6357.50","5752.50","5455.20","5263.20","6434.00","2435.70","6435.40","5574.70"
    "copy (MB/s)","6955.90","5708.80","4771.00","5533.10","6965.60","3541.90","7690.10","5841.50"
    "scale (MB/s)","7079.70","5678.40","4829.20","5386.10","7106.70","3165.20","7833.60","5805.30"
    "triad (MB/s)","6353.30","5741.90","5459.10","5243.80","6437.90","2232.90","6426.60","5554.30"




CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","80.00","82.64","82.64","83.33","82.64","42.02","83.33","81.30"
    "core (workloads/)","0.78","0.78","0.78","0.78","0.78","0.30","0.78","0.78"
    "coremark-pro ()","2477.08","2488.68","2467.07","2529.15","2459.73","905.84","2504.92","2522.22"
    "linear_alg-mid-100x100-sp (workloads/)","81.70","81.57","79.62","80.91","81.04","14.68","79.24","81.17"
    "loops-all-mid-10k-sp (workloads/)","2.47","2.43","2.45","2.48","2.48","0.70","2.45","2.46"
    "nnet_test (workloads/)","3.67","3.65","3.67","3.87","3.44","1.09","3.63","3.63"
    "parser-125k (workloads/)","10.99","10.87","10.99","11.11","11.11","8.77","10.75","10.99"
    "radix2-big-64k (workloads/)","271.37","270.64","254.07","282.89","253.36","53.56","295.42","306.37"
    "sha-test (workloads/)","158.73","158.73","156.25","158.73","156.25","80.65","158.73","158.73"
    "zip-test (workloads/)","45.45","47.62","47.62","47.62","47.62","21.74","47.62","47.62"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","163.93","163.93","163.93","161.29","163.93","82.64","163.93","166.67"
    "core (workloads/)","1.56","1.55","1.55","1.56","1.55","0.60","1.56","1.55"
    "coremark-pro ()","4453.86","4926.18","4303.47","4495.33","4390.38","1643.12","4742.81","4965.38"
    "linear_alg-mid-100x100-sp (workloads/)","160.77","161.29","162.87","161.81","159.74","29.38","156.74","160.77"
    "loops-all-mid-10k-sp (workloads/)","3.98","4.05","3.60","4.12","4.20","1.28","4.18","4.27"
    "nnet_test (workloads/)","7.27","7.56","7.29","7.26","7.30","2.17","7.28","7.60"
    "parser-125k (workloads/)","20.41","21.51","20.62","21.28","19.80","14.29","21.05","21.28"
    "radix2-big-64k (workloads/)","283.13","583.43","235.57","288.35","289.77","62.30","435.92","589.62"
    "sha-test (workloads/)","312.50","322.58","312.50","312.50","312.50","161.29","322.58","322.58"
    "zip-test (workloads/)","90.91","95.24","86.96","90.91","76.92","42.55","95.24","95.24"

 


.. csv-table:: CoreMarkProFourCore Benchmarks
    :header: "Benchmarks","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","322.58","163.93","163.93","161.29","158.73","322.58"
    "core (workloads/)","3.11","1.55","1.55","1.55","1.20","3.11"
    "coremark-pro ()","8760.74","4145.92","4377.92","4362.78","2546.80","8835.06"
    "linear_alg-mid-100x100-sp (workloads/)","310.56","160.77","159.24","160.77","56.43","312.50"
    "loops-all-mid-10k-sp (workloads/)","7.70","3.66","4.10","4.02","2.07","7.57"
    "nnet_test (workloads/)","12.14","7.42","7.60","7.42","3.62","12.21"
    "parser-125k (workloads/)","40.00","19.80","20.62","18.69","8.91","41.67"
    "radix2-big-64k (workloads/)","772.20","194.33","244.20","266.31","85.56","803.86"
    "sha-test (workloads/)","526.32","294.12","303.03","312.50","270.27","526.32"
    "zip-test (workloads/)","181.82","81.63","86.96","86.96","76.92","181.82"

 


.. csv-table:: CoreMarkProEightCore Benchmarks
    :header: "Benchmarks","am69_sk-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","625.00","625.00"
    "core (workloads/)","6.18","6.21"
    "coremark-pro ()","14216.83","14141.56"
    "linear_alg-mid-100x100-sp (workloads/)","581.40","574.71"
    "loops-all-mid-10k-sp (workloads/)","10.42","10.17"
    "nnet_test (workloads/)","19.23","19.23"
    "parser-125k (workloads/)","72.73","73.39"
    "radix2-big-64k (workloads/)","834.03","845.31"
    "sha-test (workloads/)","769.23","769.23"
    "zip-test (workloads/)","320.00","307.69"

 
 


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

    "4m-check (workloads/)","811.16","979.24","844.02","864.16","809.32","380.17","1091.23","981.16"
    "4m-check-reassembly (workloads/)","146.63","188.32","116.41","142.05","145.14","111.73","186.57","176.37"
    "4m-check-reassembly-tcp (workloads/)","91.91","104.17","84.75","92.94","91.58","56.05","110.62","105.93"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","41.96","36.72","40.82","44.05","41.15","31.20","55.87","34.31"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","2.69","4.88","2.68","2.71","2.68","1.87","4.71","4.87"
    "4m-cmykw2 (workloads/)","289.86","588.24","312.50","314.96","312.99","244.20","604.23","600.60"
    "4m-cmykw2-rotatew2 (workloads/)","60.18","45.42","59.70","62.70","59.46","48.66","72.38","50.63"
    "4m-reassembly (workloads/)","124.53","132.45","104.93","132.98","130.21","77.10","143.27","134.77"
    "4m-rotatew2 (workloads/)","68.54","52.14","70.03","73.48","69.54","51.63","77.76","50.89"
    "4m-tcp-mixed (workloads/)","253.97","242.42","266.67","258.07","258.07","115.11","266.67","242.42"
    "4m-x264w2 (workloads/)","2.75","5.06","2.72","2.79","2.74","1.84","5.02","5.06"
    "idct-4m (workloads/)","34.93","35.12","34.78","35.06","34.95","19.15","35.11","35.12"
    "idct-4mw1 (workloads/)","34.94","35.08","34.92","35.06","34.92","19.14","35.10","35.10"
    "ippktcheck-4m (workloads/)","823.72","969.37","844.60","833.33","805.67","380.69","1122.59","980.39"
    "ippktcheck-4mw1 (workloads/)","814.86","988.14","855.29","868.06","807.75","379.02","1114.08","964.88"
    "ipres-4m (workloads/)","166.30","177.94","156.58","178.57","167.41","100.40","192.56","183.82"
    "ipres-4mw1 (workloads/)","169.11","174.42","156.09","179.00","167.41","99.60","196.34","185.41"
    "md5-4m (workloads/)","43.48","44.78","43.76","47.04","43.98","27.08","47.94","44.50"
    "md5-4mw1 (workloads/)","43.67","44.76","43.61","47.06","44.07","27.54","47.92","44.60"
    "rgbcmyk-4m (workloads/)","163.00","163.67","162.87","163.67","162.87","65.49","163.93","163.80"
    "rgbcmyk-4mw1 (workloads/)","162.60","163.53","163.00","163.67","163.13","65.32","160.64","163.93"
    "rotate-4ms1 (workloads/)","51.18","52.91","51.28","54.35","50.66","22.48","53.94","53.82"
    "rotate-4ms1w1 (workloads/)","51.07","53.36","51.55","54.23","50.40","22.04","54.05","53.53"
    "rotate-4ms64 (workloads/)","52.69","54.76","52.69","55.19","52.19","22.32","55.31","54.88"
    "rotate-4ms64w1 (workloads/)","52.41","54.59","52.80","55.74","51.92","22.31","55.37","54.76"
    "x264-4mq (workloads/)","1.42","1.42","1.42","1.43","1.41","0.57","1.42","1.42"
    "x264-4mqw1 (workloads/)","1.43","1.42","1.42","1.44","1.42","0.57","1.43","1.42"



 
 


Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","j721e-idk-gw: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","22.11 (min 21.89, max 22.38)"

 

 

Boot time numbers [avg, min, max] are measured from "Starting kernel" to Linux prompt across 20 boot cycles.
 



|

ALSA SoC Audio Driver
-------------------------

#. Access type - RW\_INTERLEAVED
#. Channels - 2
#. Format - S16\_LE
#. Period size - 64


.. csv-table:: Audio Capture
    :header: "Sampling Rate (Hz)","j721e-idk-gw: Throughput (bits/sec)","j721e-idk-gw: CPU Load (%)","j721s2-evm: Throughput (bits/sec)","j721s2-evm: CPU Load (%)","j722s_evm-fs: Throughput (bits/sec)","j722s_evm-fs: CPU Load (%)","j784s4-evm: Throughput (bits/sec)","j784s4-evm: CPU Load (%)"

    "11025","352792.00","0.29","1023977.00","0.53","331812.00","0.34","1023971.00","0.10"
    "16000","511991.00","0.43","1023987.00","0.93","511982.00","0.37","1023983.00","0.18"
    "22050","705576.00","0.40","1023968.00","0.55","663605.00","0.38","1023966.00","0.10"
    "24000","705583.00","0.41","1023983.00","0.73","663623.00","0.39","1023981.00","0.14"
    "32000","1023975.00","0.32","1023985.00","0.77","1023957.00","0.40","1023979.00","0.14"
    "44100","1411174.00","0.62","1417793.00","0.71","1327261.00","0.49","1417788.00","0.13"
    "48000","1535973.00","0.84","1535955.00","0.75","1535941.00","0.51","1535951.00","0.16"
    "88200","2822349.00","1.13","2835618.00","1.26","2654523.00","0.62","2835611.00","0.27"
    "96000","3071945.00","0.63","3071925.00","1.38","3071726.00","0.61","3071919.00","0.29"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","j721e-idk-gw: Throughput (bits/sec)","j721e-idk-gw: CPU Load (%)","j721s2-evm: Throughput (bits/sec)","j721s2-evm: CPU Load (%)","j722s_evm-fs: Throughput (bits/sec)","j722s_evm-fs: CPU Load (%)","j784s4-evm: Throughput (bits/sec)","j784s4-evm: CPU Load (%)"

    "11025","352937.00","0.22","1024404.00","0.41","191937.00","0.32","1024381.00","0.67"
    "16000","512203.00","0.37","1024413.00","0.98","255987.00","0.34","1024399.00","0.10"
    "22050","705866.00","0.31","1024387.00","0.54","383919.00","0.35","1024394.00","0.10"
    "24000","705873.00","0.33","1024404.00","0.63","383972.00","0.35","1024403.00","0.06"
    "32000","1024401.00","0.43","1024407.00","0.73","512100.00","0.33","1024401.00","0.13"
    "44100","1411755.00","0.52","1418376.00","0.68","768093.00","0.37","1418387.00","0.15"
    "48000","1536605.00","0.32","1536588.00","0.71","768187.00","0.37","1536593.00","0.14"
    "88200","2823512.00","1.05","2836787.00","1.22","1535024.00","0.41","2836791.00","0.29"
    "96000","3073210.00","0.54","3073192.00","1.25","1535645.00","0.41","3073193.00","0.36"

 
 



 



|

Graphics SGX/RGX Driver
-------------------------
 


GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am68_sk-fs: Score","am68_sk-fs: Fps","am69_sk-fs: Score","am69_sk-fs: Fps","j721e-idk-gw: Score","j721e-idk-gw: Fps","j721s2-evm: Score","j721s2-evm: Fps","j742s2_evm-fs: Score","j742s2_evm-fs: Fps","j784s4-evm: Score","j784s4-evm: Fps"

    " GFXBench 3.x gl_manhattan_off","941.34","15.18","904.19","14.58","1215.12","19.60","957.81","15.45","956.69","15.43","938.20","15.13"
    " GFXBench 3.x gl_trex_off","1603.75","28.64","1455.77","26.00","1839.18","32.84","1645.01","29.38","1642.73","29.33","1464.47","26.15"
    " GFXBench 4.x gl_4_off","260.83","4.41","254.11","4.30","411.79","6.97","263.28","4.45","260.79","4.41","250.88","4.24"
    " GFXBench 5.x gl_5_high_off","113.83","1.77","110.71","1.72","179.43","2.79","113.91","1.77","113.82","1.77","111.83","1.74"




Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am68_sk-fs: Score","am69_sk-fs: Score","j721e-idk-gw: Score","j721s2-evm: Score","j722s_evm-fs: Score","j742s2_evm-fs: Score","j784s4-evm: Score"

    "Glmark2-DRM","522.00","158.00","48.00","141.00","287.00","113.00","166.00"
    "Glmark2-Wayland","1232.00","1303.00","1126.00","1238.00","795.00","1368.00","1291.00"
    "Glmark2-Wayland 4000x4000","83.00","73.00","85.00","83.00","88.00"

 
 

 

 



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
    :header: "Command Used","am68_sk-fs: THROUGHPUT (Mbits/sec)","am68_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","am69_sk-fs: THROUGHPUT (Mbits/sec)","am69_sk-fs: CPU Load % (LOCAL_CPU_UTIL)","j7200-evm: THROUGHPUT (Mbits/sec)","j7200-evm: CPU Load % (LOCAL_CPU_UTIL)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j721s2-evm: THROUGHPUT (Mbits/sec)","j721s2-evm: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","0.02","80.67","0.02","29.50","1774.79","74.86","1812.15","82.41","0.02","80.25","907.42","35.21","1817.27","57.56","1851.66","27.82"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1842.31","48.70","1870.65","40.00","1810.25","55.34","1677.91","26.78"




.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: Packets Per Second (kPPS)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","20.84","41.00","17.20","18.00","53.56","105.00","39.35","18.00","77.42","151.00","43.10","18.00","84.43","165.00","20.48"
    "128","82.00","23.45","23.00","9.00","82.00","105.84","103.00","39.64","82.00","156.44","153.00","43.43","82.00","146.76","143.00","22.01"
    "256","210.00","19.05","9.00","1.79","210.00","211.01","103.00","39.64","210.00","312.75","153.00","43.50","210.00","325.76","159.00","20.62"
    "1024","978.00","0.01","0.00","59.66","978.00","728.69","89.00","25.23","978.00","938.76","115.00","34.15","978.00","937.30","114.00","18.11"
    "1518","1472.00","0.01","0.00","50.52","1472.00","855.88","70.00","38.52","1472.00","922.38","76.00","27.86","1472.00","842.24","69.00","10.43"




.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","","3.64","7.00","4.84","","3.58","7.00","0.71","18.00","2.76","5.00","1.04"
    "128","82.00","10.03","10.00","6.56","82.00","17.92","18.00","2.39","82.00","6.86","7.00","0.52"
    "256","210.00","23.96","12.00","9.01","","24.17","12.00","1.17","210.00","17.41","9.00","0.49"
    "1024","978.00","145.82","18.00","13.80","","30.19","4.00","1.88","978.00","877.68","107.00","19.03"
    "1518","1472.00","571.43","49.00","42.41","1472.00","906.30","77.00","31.50","1472.00","953.57","81.00","17.22"




.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j721e-idk-gw: Packet Loss %","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: Packet Loss %","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: Packet Loss %"

    "64","","77.40","151.00","84.53","4.00","","153.23","299.00","44.38","59.69","18.00","197.00","385.00","23.23","26.10"
    "128","82.00","154.42","151.00","84.65","2.49","82.00","386.25","377.00","43.48","39.61","82.00","348.15","340.00","23.26","27.41"
    "256","210.00","305.82","149.00","82.08","3.51","","776.10","379.00","44.28","2.00","210.00","612.53","299.00","23.18","22.86"
    "1024","978.00","923.64","113.00","82.67","1.63","","891.13","109.00","39.33","0.38","978.00","934.78","114.00","20.07","0.04"
    "1518","1472.00","929.27","79.00","71.74","0.01","1472.00","906.30","77.00","31.50","0.00","1472.00","953.57","81.00","17.22","0.00"

 
 

 

 
 



|

PCIe Driver
-------------------------


 


PCIe-NVMe-SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^
 

 

 


J721E-IDK-GW
"""""""""""""""""""""""""""




.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","720.00","13.73","1514.00","8.10"
    "4m","722.00","12.46","1514.00","5.27"
    "4k","173.00","48.45","159.00","36.67"
    "256k","718.00","15.41","1507.00","14.50"



- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based 
- Platform: Speed 8GT/s, Width x2
- SSD being used: PLEXTOR PX-128M8PeY
 



J721S2-EVM
"""""""""""""""""""""""""""




.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","731.00","17.18","771.00","4.49"
    "4m","731.00","13.97","772.00","3.56"
    "4k","175.00","50.45","285.00","50.48"
    "256k","749.00","17.68","786.00","8.13"



- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based 
- Platform: Speed 8GT/s, Width x2
- SSD being used: PLEXTOR PX-128M8PeY
 

 

 

 
 

 



|

Linux OSPI Flash Driver
-------------------------

 

 

 

 

 


 


 


J7200-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j7200-evm: Write UBIFS Throughput (Mbytes/sec)","j7200-evm: Write UBIFS CPU Load (%)","j7200-evm: Read UBIFS Throughput (Mbytes/sec)","j7200-evm: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.28)","50.63 (min 49.63, max 51.72)","78.21","0.00"
    "262144","0.13 (min 0.10, max 0.18)","50.50 (min 49.98, max 51.08)","79.66","40.00"
    "524288","0.14 (min 0.11, max 0.18)","50.51 (min 49.98, max 51.33)","76.54","33.33"
    "1048576","0.14 (min 0.11, max 0.18)","50.57 (min 50.00, max 51.29)","74.97","25.00"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j7200-evm: Raw Read Throughput (Mbytes/sec)"

    "50","238.09"

 
 


J721E-IDK-GW
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j721e-idk-gw: Write UBIFS Throughput (Mbytes/sec)","j721e-idk-gw: Write UBIFS CPU Load (%)","j721e-idk-gw: Read UBIFS Throughput (Mbytes/sec)","j721e-idk-gw: Read UBIFS CPU Load (%)"

    "102400","0.70 (min 0.53, max 1.34)","54.46 (min 50.57, max 61.19)","31.55","7.69"
    "262144","0.51 (min 0.38, max 0.58)","53.80 (min 49.86, max 62.66)","31.58","20.00"
    "524288","0.51 (min 0.37, max 0.57)","52.70 (min 50.95, max 56.26)","31.20","0.00"
    "1048576","0.51 (min 0.37, max 0.57)","54.19 (min 51.72, max 59.34)","31.09","14.29"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j721e-idk-gw: Raw Read Throughput (Mbytes/sec)"

    "50","38.76"

 
 
    "400000","988.42","15875.97"

 


J722S-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j722s_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Write UBIFS CPU Load (%)","j722s_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.29)","28.63 (min 24.95, max 31.39)","64.21","28.57"
    "262144","0.14 (min 0.11, max 0.19)","29.46 (min 28.09, max 31.52)","64.80","15.38"
    "524288","0.14 (min 0.11, max 0.19)","28.79 (min 27.27, max 30.04)","66.06","28.57"
    "1048576","0.14 (min 0.11, max 0.19)","31.27 (min 28.03, max 32.99)","62.26","26.67"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j722s_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","227.27"

 
 


J742S2-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j742s2_evm-fs: Write UBIFS CPU Load (%)","j742s2_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j742s2_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.28)","28.80 (min 25.00, max 33.37)","74.73","18.18"
    "262144","0.14 (min 0.11, max 0.18)","30.07 (min 27.35, max 32.13)","75.22","18.18"
    "524288","0.14 (min 0.11, max 0.18)","30.04 (min 28.09, max 33.34)","72.49","16.67"
    "1048576","0.14 (min 0.11, max 0.18)","30.26 (min 28.21, max 32.33)","73.02","23.08"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j742s2_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","238.09"

 
 


J784S4-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j784s4-evm: Write UBIFS Throughput (Mbytes/sec)","j784s4-evm: Write UBIFS CPU Load (%)","j784s4-evm: Read UBIFS Throughput (Mbytes/sec)","j784s4-evm: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.28)","14.98 (min 12.37, max 17.06)","72.30","4.35"
    "262144","0.13 (min 0.10, max 0.18)","14.55 (min 13.20, max 15.68)","74.58","8.70"
    "524288","0.13 (min 0.10, max 0.18)","15.83 (min 14.37, max 18.38)","74.26","4.55"
    "1048576","0.14 (min 0.10, max 0.18)","15.35 (min 13.72, max 16.31)","69.79","4.17"




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

    "400000","1026.82","15875.97"
    "800000","1027.47","16062.75"
    "1000000","1027.60","16157.79"
    "2000000","1028.18","16213.76"




J721S2-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "400000","999.27","15875.97"
    "800000","999.76","16062.75"
    "1000000","999.82","16157.79"
    "2000000","999.51","16221.78"






J742S2-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","979.67","15875.97"
    "800000","979.67","16062.75"
    "1000000","979.96","16173.74"
    "2000000","980.52","16221.78"




J784S4-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "800000","989.13","16062.75"
    "1000000","989.55","16157.79"
    "2000000","989.76","16221.78"















 
 

 

 



|

UBoot UFS Driver
-------------------------




J721E-IDK-GW
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","215578.95","372363.64"
    "800000","190511.63","512000.00"
    "1000000","234057.14","630153.85"






J742S2-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","204800.00","372363.64"
    "800000","190511.63","512000.00"
    "1000000","230760.56","655360.00"

 


J784S4-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","215578.95","372363.64"
    "800000","195047.62","512000.00"
    "1000000","230760.56","655360.00"

 

 



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
    :header: "Buffer size (bytes)","am69_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Write EXT4 CPU Load (%)","am69_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Read EXT4 CPU Load (%)"

    "1m","91.80","0.46","289.00","0.45"
    "4m","90.80","0.46","286.00","0.29"
    "4k","78.30","11.70","92.90","9.34"
    "256k","91.80","0.51","287.00","0.88"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write EXT4 Throughput (Mbytes/sec)","j7200-evm: Write EXT4 CPU Load (%)","j7200-evm: Read EXT4 Throughput (Mbytes/sec)","j7200-evm: Read EXT4 CPU Load (%)"

    "1m","44.20","1.39","300.00","1.81"
    "4m","44.30","1.28","300.00","0.90"
    "4k","5.22","2.60","36.20","13.44"
    "256k","35.50","1.28","283.00","3.44"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","60.40","1.60","175.00","1.21"
    "4m","59.80","1.27","175.00","0.78"
    "4k","50.30","21.85","56.40","20.24"
    "256k","60.10","2.03","174.00","2.33"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","45.30","1.50","300.00","1.96"
    "4m","45.50","1.07","300.00","1.26"
    "4k","5.25","2.63","36.20","14.35"
    "256k","36.50","1.49","283.00","3.42"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

    "1m","97.40","1.89","175.00","2.12"
    "4m","97.70","1.32","168.00","1.58"
    "4k","68.20","22.10","94.90","22.84"
    "256k","97.30","2.34","174.00","2.84"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Write EXT4 CPU Load (%)","j742s2_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Read EXT4 CPU Load (%)"

    "1m","97.00","0.95","292.00","0.86"
    "4m","97.60","0.89","292.00","0.50"
    "4k","83.00","21.08","84.10","16.51"
    "256k","97.10","0.99","292.00","1.84"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

    "1m","97.20","0.54","293.00","0.56"
    "4m","97.70","0.46","292.00","0.27"
    "4k","82.70","10.17","93.90","9.75"
    "256k","97.20","0.59","293.00","1.00"

 

 

 

 

 

 

 
 


EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write Raw Throughput (Mbytes/sec)","am69_sk-fs: Write Raw CPU Load (%)","am69_sk-fs: Read Raw Throughput (Mbytes/sec)","am69_sk-fs: Read Raw CPU Load (%)"

    "1m","90.60","0.43","293.00","0.42"
    "4m","97.50","0.45","293.00","0.20"
    "4k","76.00","8.63","86.80","7.86"
    "256k","90.70","0.50","293.00","0.87"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "1m","44.30","1.31","306.00","1.63"
    "4m","44.40","0.99","303.00","1.06"
    "4k","5.20","2.02","36.10","12.04"
    "256k","35.50","1.14","288.00","3.30"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "1m","60.60","1.34","175.00","1.21"
    "4m","60.50","1.25","175.00","0.75"
    "4k","53.00","17.78","56.40","18.25"
    "256k","60.30","1.76","174.00","2.09"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "1m","45.30","1.55","301.00","1.97"
    "4m","45.50","1.05","298.00","1.13"
    "4k","5.24","2.16","36.30","12.96"
    "256k","36.50","1.40","284.00","3.29"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "1m","77.80","1.40","112.00","1.48"
    "4m","78.00","1.01","112.00","1.06"
    "4k","8.48","2.59","56.70","13.63"
    "256k","68.20","1.67","94.20","1.46"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "1m","98.50","0.86","294.00","0.86"
    "4m","98.60","0.92","294.00","0.49"
    "4k","84.70","16.69","93.70","17.34"
    "256k","98.50","0.93","294.00","1.77"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "1m","98.40","0.45","296.00","0.40"
    "4m","98.80","0.46","296.00","0.21"
    "4k","82.60","7.90","93.30","8.66"
    "256k","98.30","0.48","296.00","0.81"

 

 

 

 

 

 

 
 

 

 

 

 

 
 



UBoot EMMC Driver
-----------------

 

 

 

 

 

 

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am69_sk-fs: Write Throughput (Kbytes/sec)","am69_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","96946.75","280068.38"
    "4000000","95255.81","291271.11"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

    "2000000","59904.94","312076.19"
    "4000000","61248.60","319687.80"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "2000000","60124.77","174297.87"
    "4000000","60235.29","178086.96"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "2000000","60569.32","309132.08"
    "4000000","61420.81","318135.92"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j722s_evm-fs: Write Throughput (Kbytes/sec)","j722s_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","96946.75","172463.16"
    "4000000","96660.77","175699.73"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","97234.42","258015.75"
    "4000000","98996.98","292571.43"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "2000000","103696.20","284939.13"
    "4000000","97961.14","295207.21"

 

 

 

 

 

 

 
 

 


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
    :header: "Buffer size (bytes)","am68_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am68_sk-fs: Write EXT4 CPU Load (%)","am68_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am68_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.80","1.56","88.10","1.19"
    "4m","41.60","1.26","83.20","0.84"
    "4k","2.82","2.35","13.00","6.57"
    "256k","42.50","2.08","84.00","1.55"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Write EXT4 CPU Load (%)","am69_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Read EXT4 CPU Load (%)"

    "1m","42.10","0.28","87.30","0.28"
    "4m","42.70","0.29","87.40","0.18"
    "4k","2.78","0.60","12.90","1.74"
    "256k","36.80","0.27","83.40","0.34"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","33.50","1.12","43.40","0.82"
    "4m","33.50","0.94","43.40","0.52"
    "4k","2.76","2.08","11.20","4.97"
    "256k","33.20","1.30","42.50","0.81"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write EXT4 Throughput (Mbytes/sec)","j7200-evm: Write EXT4 CPU Load (%)","j7200-evm: Read EXT4 Throughput (Mbytes/sec)","j7200-evm: Read EXT4 CPU Load (%)"

    "1m","42.30","1.64","87.40","1.21"
    "4m","42.10","1.22","87.20","0.84"
    "4k","2.81","2.19","12.90","6.34"
    "256k","38.20","1.56","84.00","1.52"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","42.40","1.52","87.60","1.12"
    "4m","41.80","1.15","87.50","0.78"
    "4k","2.80","2.51","13.00","6.39"
    "256k","36.60","1.65","83.90","1.57"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

    "1m","42.60","1.36","87.30","1.59"
    "4m","41.70","0.92","87.20","1.22"
    "4k","2.83","2.03","13.20","4.80"
    "256k","39.70","1.69","83.40","1.70"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Write EXT4 CPU Load (%)","j742s2_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Read EXT4 CPU Load (%)"

    "1m","42.30","0.62","87.10","0.49"
    "4m","41.50","0.51","87.00","0.31"
    "4k","2.77","1.34","12.90","4.12"
    "256k","36.20","0.57","83.40","0.73"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

    "1m","41.80","0.28","87.30","0.32"
    "4m","42.70","0.25","87.20","0.20"
    "4k","2.78","0.60","12.90","1.66"
    "256k","37.80","0.30","83.50","0.33"

 

 

 

 

 

 

 

 

 
 


MMC RAW FIO 1G
^^^^^^^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am68_sk-fs: Write Raw Throughput (Mbytes/sec)","am68_sk-fs: Write Raw CPU Load (%)","am68_sk-fs: Read Raw Throughput (Mbytes/sec)","am68_sk-fs: Read Raw CPU Load (%)"

    "1m","44.90","1.48","88.20","0.94"
    "4m","44.10","1.13","88.20","0.60"
    "4k","2.82","2.03","13.00","6.34"
    "256k","41.40","1.55","84.50","1.42"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write Raw Throughput (Mbytes/sec)","am69_sk-fs: Write Raw CPU Load (%)","am69_sk-fs: Read Raw Throughput (Mbytes/sec)","am69_sk-fs: Read Raw CPU Load (%)"

    "1m","42.80","0.26","88.20","0.20"
    "4m","42.90","0.27","88.00","0.13"
    "4k","2.82","0.49","13.00","1.55"
    "256k","36.70","0.26","84.20","0.34"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "1m","42.40","1.30","88.10","0.96"
    "4m","42.40","1.17","88.10","0.68"
    "4k","2.82","1.81","13.00","5.82"
    "256k","36.10","1.23","84.40","1.33"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "1m","33.60","1.03","43.80","0.63"
    "4m","33.50","0.85","43.80","0.48"
    "4k","2.78","1.86","11.30","4.80"
    "256k","30.60","1.09","42.80","0.84"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "1m","44.00","1.48","88.10","0.97"
    "4m","44.00","1.27","88.20","0.76"
    "4k","2.82","2.15","13.00","6.39"
    "256k","38.40","1.67","84.30","1.38"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "1m","44.60","1.22","88.30","1.40"
    "4m","43.10","0.91","88.10","1.09"
    "4k","2.80","1.61","13.00","4.11"
    "256k","41.10","1.30","84.50","1.75"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "1m","42.70","0.57","88.20","0.45"
    "4m","42.20","0.54","88.00","0.36"
    "4k","2.80","1.24","13.10","3.98"
    "256k","36.40","0.49","84.30","0.75"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "1m","42.40","0.28","88.30","0.18"
    "4m","42.40","0.26","88.30","0.15"
    "4k","2.81","0.54","13.00","1.49"
    "256k","36.20","0.26","84.50","0.36"

 

 

 
 


MMC EXT4
^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "102400","38.55 (min 37.26, max 39.25)","3.13 (min 2.70, max 4.01)","75.20","4.14"
    "262144","36.59 (min 35.69, max 37.03)","3.08 (min 2.65, max 4.52)","86.91","5.00"
    "524288","37.97 (min 37.18, max 38.49)","3.08 (min 2.71, max 4.04)","89.37","4.50"
    "1048576","37.60 (min 36.74, max 38.15)","2.96 (min 2.54, max 4.00)","91.31","5.42"
    "5242880","38.47 (min 37.70, max 39.60)","2.96 (min 2.61, max 4.06)","91.32","5.45"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "102400","30.10 (min 29.43, max 30.70)","2.75 (min 2.34, max 3.53)","43.15","2.26"
    "262144","29.26 (min 28.59, max 30.52)","2.74 (min 2.05, max 3.36)","41.44","2.18"
    "524288","29.63 (min 28.83, max 31.22)","2.73 (min 2.34, max 3.58)","45.86","2.63"
    "1048576","30.67 (min 29.89, max 32.82)","2.65 (min 2.18, max 3.90)","45.85","2.41"
    "5242880","30.51 (min 29.65, max 32.40)","2.58 (min 2.12, max 3.55)","45.74","3.04"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "102400","38.99 (min 38.08, max 39.99)","3.52 (min 2.87, max 4.89)","81.19","4.65"
    "262144","37.31 (min 36.11, max 40.03)","3.54 (min 3.16, max 4.61)","81.42","5.06"
    "524288","41.63 (min 39.49, max 42.57)","3.67 (min 2.84, max 4.68)","92.04","5.26"
    "1048576","38.85 (min 37.96, max 40.15)","3.60 (min 3.26, max 4.77)","92.07","5.29"
    "5242880","41.59 (min 40.70, max 42.26)","3.82 (min 3.11, max 5.24)","91.95","6.55"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "102400","37.52 (min 36.44, max 39.53)","3.49 (min 2.96, max 5.08)","75.75","5.09"
    "262144","37.85 (min 36.41, max 40.12)","3.55 (min 2.96, max 5.15)","84.59","6.00"
    "524288","40.83 (min 39.63, max 41.42)","3.62 (min 2.85, max 5.21)","91.33","4.80"
    "1048576","38.52 (min 37.59, max 40.19)","3.28 (min 2.76, max 4.24)","91.72","4.82"
    "5242880","39.34 (min 38.41, max 40.90)","3.18 (min 2.57, max 4.68)","91.86","5.26"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "102400","39.56 (min 38.67, max 40.88)","0.97 (min 0.88, max 1.17)","74.68","1.07"
    "262144","37.71 (min 36.96, max 39.41)","0.87 (min 0.71, max 1.22)","88.28","1.26"
    "524288","39.46 (min 38.61, max 41.74)","0.95 (min 0.65, max 1.69)","91.54","0.98"
    "1048576","39.22 (min 38.59, max 39.88)","0.79 (min 0.65, max 1.09)","91.94","1.20"
    "5242880","38.71 (min 37.32, max 40.67)","0.82 (min 0.73, max 1.07)","91.00","1.19"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "102400","37.32 (min 35.11, max 40.43)","1.63 (min 1.34, max 2.22)","74.74","2.49"
    "262144","37.41 (min 36.82, max 38.27)","1.64 (min 1.41, max 2.01)","87.80","2.10"
    "524288","38.94 (min 38.03, max 41.18)","1.71 (min 1.37, max 2.35)","92.18","1.98"
    "1048576","38.38 (min 37.95, max 39.36)","1.61 (min 1.37, max 2.07)","92.13","2.19"
    "5242880","39.03 (min 38.45, max 40.42)","1.63 (min 1.30, max 2.12)","92.05","2.63"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am68_sk-fs: Write Raw Throughput (Mbytes/sec)","am68_sk-fs: Write Raw CPU Load (%)","am68_sk-fs: Read Raw Throughput (Mbytes/sec)","am68_sk-fs: Read Raw CPU Load (%)"

    "102400","40.38 (min 39.67, max 41.27)","3.48 (min 3.04, max 4.61)","76.23","4.73"
    "262144","37.74 (min 37.05, max 39.11)","3.36 (min 2.53, max 4.85)","87.99","5.42"
    "524288","39.25 (min 38.02, max 41.40)","3.42 (min 2.44, max 4.74)","91.57","4.39"
    "1048576","39.08 (min 38.32, max 41.14)","3.33 (min 2.57, max 4.88)","91.83","5.26"
    "5242880","39.58 (min 38.55, max 40.57)","3.11 (min 2.44, max 4.26)","91.31","6.06"

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","am69_sk-fs: Write Raw Throughput (Mbytes/sec)","am69_sk-fs: Write Raw CPU Load (%)","am69_sk-fs: Read Raw Throughput (Mbytes/sec)","am69_sk-fs: Read Raw CPU Load (%)"

    "102400","38.96 (min 38.25, max 39.33)","0.86 (min 0.75, max 1.14)","81.71","0.98"
    "262144","37.35 (min 36.24, max 39.46)","0.82 (min 0.66, max 1.18)","88.17","1.26"
    "524288","37.27 (min 36.35, max 37.75)","0.80 (min 0.67, max 1.13)","91.97","1.10"
    "1048576","38.69 (min 37.29, max 40.82)","0.83 (min 0.71, max 1.12)","91.46","1.31"
    "5242880","39.70 (min 38.41, max 42.68)","0.88 (min 0.65, max 1.47)","91.97","1.42"

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 


MMC EXT2
^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "102400","41.05 (min 36.88, max 42.42)","3.87 (min 3.27, max 5.99)","77.63","4.83"
    "262144","37.02 (min 33.77, max 38.27)","3.33 (min 2.64, max 5.47)","82.79","5.36"
    "524288","37.55 (min 34.11, max 38.69)","3.31 (min 2.73, max 5.37)","90.65","5.40"
    "1048576","36.87 (min 33.35, max 38.04)","3.16 (min 2.37, max 5.33)","85.80","4.35"
    "5242880","37.28 (min 33.58, max 39.07)","3.33 (min 2.72, max 5.36)","85.76","4.92"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "102400","34.35 (min 32.38, max 35.24)","3.34 (min 2.66, max 5.72)","41.15","2.17"
    "262144","29.76 (min 28.53, max 30.47)","2.88 (min 2.11, max 4.77)","43.46","2.69"
    "524288","29.93 (min 28.95, max 30.42)","2.87 (min 2.19, max 4.84)","44.37","2.75"
    "1048576","29.95 (min 28.62, max 30.36)","2.98 (min 2.17, max 4.78)","44.62","2.98"
    "5242880","30.18 (min 28.91, max 30.91)","2.86 (min 2.30, max 4.70)","44.32","3.37"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "102400","42.32 (min 40.08, max 43.17)","4.41 (min 3.52, max 7.10)","81.10","5.38"
    "262144","42.18 (min 39.46, max 43.37)","4.54 (min 3.44, max 7.17)","87.28","5.42"
    "524288","38.07 (min 36.28, max 38.84)","3.99 (min 2.90, max 6.74)","91.32","6.52"
    "1048576","37.79 (min 35.11, max 38.64)","3.74 (min 2.95, max 6.22)","86.44","6.20"
    "5242880","40.87 (min 38.75, max 42.05)","4.14 (min 3.22, max 6.49)","91.36","6.11"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "102400","42.05 (min 38.34, max 43.62)","4.58 (min 3.68, max 7.14)","77.48","6.59"
    "262144","38.06 (min 35.86, max 39.33)","3.82 (min 2.58, max 6.50)","87.37","5.42"
    "524288","37.72 (min 34.96, max 38.84)","4.05 (min 2.91, max 6.34)","86.27","4.22"
    "1048576","37.99 (min 36.09, max 39.13)","4.05 (min 3.17, max 7.04)","91.18","5.22"
    "5242880","37.95 (min 36.61, max 38.70)","4.07 (min 3.07, max 7.01)","91.36","5.26"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "102400","40.99 (min 37.86, max 41.94)","1.10 (min 0.85, max 1.81)","80.78","1.35"
    "262144","37.64 (min 35.35, max 38.79)","0.99 (min 0.74, max 1.60)","87.66","1.36"
    "524288","37.62 (min 35.51, max 38.79)","0.97 (min 0.76, max 1.69)","91.65","1.31"
    "1048576","38.33 (min 36.05, max 39.13)","0.98 (min 0.75, max 1.67)","91.50","1.31"
    "5242880","41.16 (min 37.40, max 42.66)","1.01 (min 0.80, max 1.69)","86.31","1.34"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "102400","37.79 (min 34.82, max 38.78)","1.95 (min 1.56, max 3.24)","80.86","3.07"
    "262144","41.91 (min 39.50, max 43.60)","2.17 (min 1.74, max 3.67)","82.55","2.36"
    "524288","38.02 (min 35.72, max 38.74)","1.88 (min 1.30, max 3.23)","91.48","1.97"
    "1048576","37.89 (min 35.52, max 38.87)","1.82 (min 1.35, max 3.21)","86.74","1.67"
    "5242880","38.37 (min 35.72, max 39.87)","1.84 (min 1.46, max 3.06)","91.42","2.18"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am68_sk-fs: Write Raw Throughput (Mbytes/sec)","am68_sk-fs: Write Raw CPU Load (%)","am68_sk-fs: Read Raw Throughput (Mbytes/sec)","am68_sk-fs: Read Raw CPU Load (%)"

    "102400","41.15 (min 38.64, max 42.99)","4.27 (min 3.37, max 7.00)","80.79","3.53"
    "262144","38.73 (min 36.04, max 39.54)","3.79 (min 2.84, max 6.52)","87.73","5.46"
    "524288","38.05 (min 35.82, max 39.10)","3.77 (min 2.96, max 6.50)","91.13","6.52"
    "1048576","37.95 (min 35.90, max 38.80)","3.87 (min 2.88, max 6.50)","91.33","5.68"
    "5242880","41.20 (min 38.91, max 42.17)","4.16 (min 3.35, max 7.06)","90.65","5.63"

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","am69_sk-fs: Write Raw Throughput (Mbytes/sec)","am69_sk-fs: Write Raw CPU Load (%)","am69_sk-fs: Read Raw Throughput (Mbytes/sec)","am69_sk-fs: Read Raw CPU Load (%)"

    "102400","40.48 (min 37.14, max 42.83)","1.10 (min 0.91, max 1.73)","81.05","1.45"
    "262144","38.19 (min 36.33, max 39.23)","0.93 (min 0.69, max 1.52)","87.84","1.15"
    "524288","41.38 (min 38.80, max 42.15)","0.97 (min 0.75, max 1.62)","91.64","1.53"
    "1048576","37.78 (min 34.75, max 39.19)","0.94 (min 0.73, max 1.53)","91.51","1.20"
    "5242880","38.19 (min 36.39, max 39.26)","0.88 (min 0.66, max 1.52)","90.79","1.19"

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 



UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am68_sk-fs: Write Throughput (Kbytes/sec)","am68_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","17355.93","78769.23"
    "800000","18044.05","86231.58"
    "1000000","18832.18","89043.48"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am69_sk-fs: Write Throughput (Kbytes/sec)","am69_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","16000.00","78769.23"
    "800000","18660.59","86231.58"
    "1000000","19883.50","89530.05"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

    "400000","53194.81","81920.00"
    "800000","73142.86","87148.94"
    "1000000","75155.96","90021.98"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","14840.58","43115.79"
    "800000","28845.07","45259.67"
    "1000000","16786.89","45893.56"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "400000","33851.24","81920.00"
    "800000","35617.39","87148.94"
    "1000000","48188.24","91022.22"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j722s_evm-fs: Write Throughput (Kbytes/sec)","j722s_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","39009.52","81920.00"
    "800000","43807.49","88086.02"
    "1000000","48473.37","89530.05"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","36571.43","83591.84"
    "800000","45765.36","88086.02"
    "1000000","47080.46","91022.22"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","23813.95","83591.84"
    "800000","38460.09","88086.02"
    "1000000","48473.37","90519.34"

 

 

 

 

 

 

 

 

 
 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 



|

USB Driver
-------------------------
 


USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^










.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721e-idk-gw: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j722s_evm-fs: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

    "150","35.40","43.30","29.80","44.50","44.10","43.20"




.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721e-idk-gw: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j722s_evm-fs: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

    "150","29.70","41.70","25.60","39.10","37.70","36.60"





 
 
 



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am68_sk-fs: throughput (KBytes/Sec)","am69_sk-fs: throughput (KBytes/Sec)","j7200-evm: throughput (KBytes/Sec)","j721e-idk-gw: throughput (KBytes/Sec)","j721s2-evm: throughput (KBytes/Sec)","j722s_evm-fs: throughput (KBytes/Sec)","j742s2_evm-fs: throughput (KBytes/Sec)","j784s4-evm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","39560.53","31139.84","35848.19","42525.35","40297.13","22416.38","39476.91","39505.92"
    "aes-128-cbc","16","779.17","733.96","701.19","815.24","775.88","399.48","775.87","780.55"
    "aes-128-cbc","16384","179240.96","176690.52","179710.63","185412.27","181310.81","82624.51","176264.53","172277.76"
    "aes-128-cbc","256","11811.50","9223.59","10695.51","12382.98","11884.12","6604.89","11795.37","11492.18"
    "aes-128-cbc","64","3095.27","2623.02","2808.15","3241.11","3148.76","1784.04","3079.81","2884.18"
    "aes-128-cbc","8192","143720.45","128062.81","141230.08","150047.40","144793.60","70322.86","143414.61","144083.63"
    "aes-128-ecb","1024","40338.09","37960.02","35778.90","43217.58","40572.25","23074.13","40057.17","39840.09"
    "aes-128-ecb","16","785.95","607.72","708.82","824.45","787.01","413.53","767.71","780.44"
    "aes-128-ecb","16384","179213.65","167930.54","181387.26","192075.09","182173.70","85524.48","182599.68","180873.90"
    "aes-128-ecb","256","11929.34","10732.37","10928.21","12763.39","12045.14","6811.65","11666.52","11819.61"
    "aes-128-ecb","64","3107.16","2331.09","2817.39","3291.93","3165.25","1818.39","3085.42","3099.46"
    "aes-128-ecb","8192","145451.69","132724.05","143458.30","155181.06","145877.67","72512.85","144733.53","144878.25"
    "aes-192-cbc","1024","39511.04","38153.90","35596.29","42172.42","40254.46","22086.66","39876.27","38610.94"
    "aes-192-cbc","16","777.10","701.60","703.35","821.55","783.90","407.18","782.92","776.17"
    "aes-192-cbc","16384","170868.74","168203.61","178978.82","176182.61","168389.29","76218.37","167723.01","165281.79"
    "aes-192-cbc","256","11698.60","11279.70","10479.79","12316.50","11714.90","6607.87","11598.08","11509.93"
    "aes-192-cbc","64","3096.92","2989.82","2817.43","3257.90","3135.42","1788.22","3089.26","3090.13"
    "aes-192-cbc","8192","139976.70","135760.55","140763.14","144001.71","138188.12","64907.95","137087.66","135648.60"
    "aes-192-ecb","1024","40263.34","38609.24","35696.98","42253.99","40414.89","22566.91","39626.75","39514.45"
    "aes-192-ecb","16","783.92","697.68","699.39","825.01","798.59","413.64","772.65","781.06"
    "aes-192-ecb","16384","174216.53","171769.86","180054.70","179437.57","173533.87","76972.03","174789.97","170115.07"
    "aes-192-ecb","256","11880.62","11693.82","10673.49","12490.75","12010.41","6767.87","11706.97","11551.32"
    "aes-192-ecb","64","3126.34","3046.49","2789.74","3294.68","3152.53","1818.20","3090.39","3115.41"
    "aes-192-ecb","8192","141565.95","139916.63","139864.75","147854.68","142737.41","66407.08","140484.61","139635.37"
    "aes-256-cbc","1024","39180.29","37601.28","35516.42","41942.36","39751.34","21625.86","39193.26","38305.45"
    "aes-256-cbc","16","780.18","720.99","703.89","818.86","786.60","408.30","776.52","770.14"
    "aes-256-cbc","16384","159640.23","157002.41","170382.68","162802.35","159558.31","69561.00","159754.92","157854.38"
    "aes-256-cbc","256","11575.55","11137.37","10496.26","12256.26","11765.76","6555.56","11459.41","11279.53"
    "aes-256-cbc","64","3089.49","2998.70","2825.47","3264.60","3159.62","1789.65","3093.46","3052.89"
    "aes-256-cbc","8192","130842.62","129078.61","135397.38","135110.66","130878.12","59768.83","131148.46","129163.26"
    "aes-256-ecb","1024","39918.25","37796.86","35552.26","41972.74","40195.41","22110.21","39584.77","38990.51"
    "aes-256-ecb","16","785.90","750.45","698.88","829.22","792.18","412.14","783.04","782.79"
    "aes-256-ecb","16384","161988.61","162867.88","173244.42","169443.33","163386.71","70948.18","164571.82","161371.48"
    "aes-256-ecb","256","11724.03","11577.51","10764.29","12474.97","11796.39","6716.93","11626.33","11592.62"
    "aes-256-ecb","64","3125.53","3040.28","2786.54","3286.06","3155.80","1803.80","3106.24","3135.13"
    "aes-256-ecb","8192","134490.79","132207.96","138824.36","139848.36","135053.31","60402.35","134482.60","132931.58"
    "des3","1024","34818.39","34503.34","34110.81","36261.89","35073.37","","34882.56","28594.18"
    "des3","16","779.47","580.07","700.69","815.32","785.61","","779.77","623.14"
    "des3","16384","94011.39","94044.16","115621.89","94109.70","94366.38","","94535.68","90079.23"
    "des3","256","11051.95","10859.09","10264.83","11737.09","11218.26","","11099.22","9121.79"
    "des3","64","3098.03","2956.07","2797.72","3245.40","3105.28","","3097.77","2969.05"
    "des3","8192","83208.87","83752.28","98729.98","86163.46","83664.90","","84759.89","81504.94"
    "sha1","1024","67628.71","65168.04","67606.53","67789.82","67656.70","","65804.63","66771.63"
    "sha1","16","1131.38","1088.04","1115.58","1132.37","1135.65","","1116.01","1120.08"
    "sha1","16384","492797.95","484054.36","496588.12","491645.61","495785.30","","487593.30","494179.67"
    "sha1","256","17921.96","17101.48","17943.89","17861.97","18020.69","","17519.79","17760.51"
    "sha1","64","4547.03","4348.16","4473.39","4485.44","4485.74","","4439.81","4482.94"
    "sha1","8192","341516.29","336355.33","348160.00","344219.65","345625.94","","337259.18","345464.83"
    "sha256","1024","65538.73","65235.97","65530.88","65188.86","67369.30","37527.21","65574.57","65648.64"
    "sha256","16","1105.70","1089.43","1100.25","1090.65","1125.59","625.83","1104.57","1107.87"
    "sha256","16384","486763.18","479936.51","489193.47","477517.14","486866.94","298003.11","479303.00","488925.87"
    "sha256","256","17471.23","17112.83","17358.17","16993.45","17560.58","9770.24","17357.82","17469.87"
    "sha256","64","4388.61","4346.05","4391.42","4316.67","4440.60","2471.13","4384.77","4375.04"
    "sha256","8192","334872.58","334831.62","341661.01","334446.59","339307.18","201252.86","336841.39","337630.55"
    "sha512","1024","50309.46","49938.09","50606.08","49729.54","51168.60","26195.29","50053.80","50124.80"
    "sha512","16","1099.16","1079.35","1111.71","1077.71","1135.89","620.30","1074.63","1093.37"
    "sha512","16384","149869.91","149564.07","150596.27","148821.33","150011.90","68375.89","149738.84","149476.69"
    "sha512","256","15945.39","15849.47","16279.64","15644.07","16371.54","8762.97","15939.24","15905.79"
    "sha512","64","4357.63","4332.03","4495.38","4298.37","4521.64","2480.15","4328.51","4336.30"
    "sha512","8192","131833.86","131315.03","132167.00","130662.40","132268.03","61576.53","131754.67","131279.53"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am68_sk-fs: CPU Load","am69_sk-fs: CPU Load","j7200-evm: CPU Load","j721e-idk-gw: CPU Load","j721s2-evm: CPU Load","j722s_evm-fs: CPU Load","j742s2_evm-fs: CPU Load","j784s4-evm: CPU Load"

    "aes-128-cbc","32.00","32.00","32.00","33.00","32.00","30.00","32.00","31.00"
    "aes-128-ecb","33.00","24.00","32.00","34.00","33.00","31.00","33.00","33.00"
    "aes-192-cbc","32.00","32.00","32.00","33.00","32.00","30.00","32.00","32.00"
    "aes-192-ecb","32.00","32.00","33.00","33.00","32.00","31.00","33.00","32.00"
    "aes-256-cbc","32.00","31.00","32.00","32.00","31.00","30.00","32.00","32.00"
    "aes-256-ecb","32.00","32.00","32.00","33.00","32.00","31.00","32.00","31.00"
    "des3","28.00","29.00","30.00","29.00","29.00","","29.00","28.00"
    "sha1","97.00","97.00","97.00","97.00","97.00","","97.00","96.00"
    "sha256","97.00","97.00","97.00","97.00","97.00","96.00","97.00","96.00"
    "sha512","97.00","97.00","97.00","97.00","97.00","96.00","97.00","96.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

 




IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","j721e-idk-gw: Throughput (Mbps)","j721e-idk-gw: Packets/Sec","j721e-idk-gw: CPU Load"

    "3des","229.30","20.00","44.02"
    "aes128","700.70","62.00","60.08"
    "aes192","635.40","56.00","98.58"
    "aes256","715.20","63.00","97.33"

 
 

 



