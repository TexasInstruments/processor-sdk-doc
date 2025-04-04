
======================================
 Linux 11.00 Performance Guide
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

    "af_unix_sock_stream_latency (microsec)","19.41","20.06","19.59","19.11","19.31","30.00","19.65","26.32"
    "af_unix_socket_stream_bandwidth (MBs)","2040.52","3010.53","1660.98","1937.14","2041.79","1062.60","2815.01","1658.61"
    "bw_file_rd-io-1mb (MB/s)","3294.89","4320.06","3648.97","3568.08","3492.65","1354.78","4093.98","3911.81"
    "bw_file_rd-o2c-1mb (MB/s)","1524.39","2168.81","1530.87","1706.81","1401.54","669.34","2074.33","2034.78"
    "bw_mem-bcopy-16mb (MB/s)","3403.17","2797.69","2374.59","2816.90","3786.53","1746.34","3355.35","2759.57"
    "bw_mem-bcopy-1mb (MB/s)","4314.99","9941.85","3388.62","4966.89","4538.03","1875.78","9964.83","9825.55"
    "bw_mem-bcopy-2mb (MB/s)","3572.70","4110.61","2475.25","3893.81","4006.56","1654.53","4950.50","4047.09"
    "bw_mem-bcopy-4mb (MB/s)","3446.49","3247.81","2337.81","3888.78","3752.35","1590.46","4162.33","2954.21"
    "bw_mem-bcopy-8mb (MB/s)","3412.97","2950.40","2368.97","3078.11","3792.67","1617.14","3461.70","2864.30"
    "bw_mem-bzero-16mb (MB/s)","10557.57","10864.03","2347.07","9628.40","10925.23","7163.11","10289.39","10825.44"
    "bw_mem-bzero-1mb (MB/s)","8478.61 (min 4314.99, max 12642.23)","11847.51 (min 9941.85, max 13753.17)","4119.23 (min 3388.62, max 4849.84)","8788.74 (min 4966.89, max 12610.58)","8865.56 (min 4538.03, max 13193.08)","4514.43 (min 1875.78, max 7153.08)","11781.28 (min 9964.83, max 13597.73)","11787.04 (min 9825.55, max 13748.52)"
    "bw_mem-bzero-2mb (MB/s)","7411.70 (min 3572.70, max 11250.70)","8847.09 (min 4110.61, max 13583.56)","2701.22 (min 2475.25, max 2927.19)","7985.98 (min 3893.81, max 12078.15)","7854.55 (min 4006.56, max 11702.53)","4395.51 (min 1654.53, max 7136.49)","9037.41 (min 4950.50, max 13124.32)","8867.79 (min 4047.09, max 13688.49)"
    "bw_mem-bzero-4mb (MB/s)","7062.28 (min 3446.49, max 10678.06)","7735.72 (min 3247.81, max 12223.62)","2402.71 (min 2337.81, max 2467.61)","7922.94 (min 3888.78, max 11957.10)","7395.96 (min 3752.35, max 11039.56)","4370.49 (min 1590.46, max 7150.52)","7832.43 (min 4162.33, max 11502.52)","7606.55 (min 2954.21, max 12258.88)"
    "bw_mem-bzero-8mb (MB/s)","7002.50 (min 3412.97, max 10592.02)","7105.04 (min 2950.40, max 11259.68)","2361.65 (min 2354.33, max 2368.97)","7384.87 (min 3078.11, max 11691.63)","7382.37 (min 3792.67, max 10972.06)","4386.39 (min 1617.14, max 7155.64)","7029.87 (min 3461.70, max 10598.03)","7074.90 (min 2864.30, max 11285.49)"
    "bw_mem-cp-16mb (MB/s)","2128.79","2184.60","984.86","1558.54","2106.37","855.94","2081.98","2187.88"
    "bw_mem-cp-1mb (MB/s)","7527.08 (min 2446.70, max 12607.45)","8277.83 (min 2824.86, max 13730.80)","3056.76 (min 1261.03, max 4852.48)","7098.05 (min 1678.70, max 12517.39)","7777.06 (min 2599.81, max 12954.30)","4129.10 (min 832.92, max 7425.28)","7803.66 (min 3188.30, max 12419.01)","8509.42 (min 3270.65, max 13748.19)"
    "bw_mem-cp-2mb (MB/s)","6689.72 (min 2132.95, max 11246.49)","8049.29 (min 2446.70, max 13651.88)","1961.07 (min 991.74, max 2930.40)","6831.68 (min 1452.43, max 12210.92)","6953.92 (min 2182.21, max 11725.62)","4040.58 (min 826.90, max 7254.26)","7620.12 (min 2139.80, max 13100.44)","8021.64 (min 2415.88, max 13627.40)"
    "bw_mem-cp-4mb (MB/s)","6386.89 (min 2107.11, max 10666.67)","7375.64 (min 2507.84, max 12243.43)","1728.22 (min 984.62, max 2471.81)","6734.19 (min 1467.62, max 12000.75)","4249.00 (min 2176.67, max 6321.33)","4042.92 (min 866.93, max 7218.91)","6919.05 (min 2321.08, max 11517.01)","7362.75 (min 2471.04, max 12254.46)"
    "bw_mem-cp-8mb (MB/s)","6354.67 (min 2108.04, max 10601.29)","6739.71 (min 2235.57, max 11243.85)","1672.27 (min 982.92, max 2361.62)","6494.29 (min 1440.40, max 11548.18)","6541.07 (min 2179.24, max 10902.90)","4043.65 (min 904.67, max 7182.62)","6360.36 (min 2114.16, max 10606.56)","6720.94 (min 2225.62, max 11216.26)"
    "bw_mem-fcp-16mb (MB/s)","3361.34","2676.93","2415.46","2786.97","3764.71","1629.83","3343.78","2663.12"
    "bw_mem-fcp-1mb (MB/s)","8280.80 (min 3919.37, max 12642.23)","10152.75 (min 6552.32, max 13753.17)","4105.28 (min 3360.72, max 4849.84)","8252.98 (min 3895.38, max 12610.58)","8887.93 (min 4582.78, max 13193.08)","4352.34 (min 1551.59, max 7153.08)","10098.56 (min 6599.38, max 13597.73)","10201.89 (min 6655.26, max 13748.52)"
    "bw_mem-fcp-2mb (MB/s)","7327.64 (min 3404.58, max 11250.70)","8598.29 (min 3613.01, max 13583.56)","2676.70 (min 2426.20, max 2927.19)","7986.67 (min 3895.18, max 12078.15)","7805.54 (min 3908.54, max 11702.53)","4355.49 (min 1574.49, max 7136.49)","8650.21 (min 4176.09, max 13124.32)","8619.75 (min 3551.00, max 13688.49)"
    "bw_mem-fcp-4mb (MB/s)","7043.77 (min 3409.48, max 10678.06)","7669.75 (min 3115.87, max 12223.62)","2416.07 (min 2364.53, max 2467.61)","7896.83 (min 3836.56, max 11957.10)","7442.49 (min 3845.41, max 11039.56)","4365.93 (min 1581.34, max 7150.52)","7715.51 (min 3928.50, max 11502.52)","7503.30 (min 2747.72, max 12258.88)"
    "bw_mem-fcp-8mb (MB/s)","6970.35 (min 3348.68, max 10592.02)","7058.16 (min 2856.63, max 11259.68)","2375.49 (min 2354.33, max 2396.64)","7379.76 (min 3067.88, max 11691.63)","7347.94 (min 3723.82, max 10972.06)","4376.39 (min 1597.13, max 7155.64)","7012.32 (min 3426.61, max 10598.03)","7017.32 (min 2749.14, max 11285.49)"
    "bw_mem-frd-16mb (MB/s)","4195.07","3235.92","6333.29","4791.14","4600.35","1785.12","4171.56","2943.34"
    "bw_mem-frd-1mb (MB/s)","4641.13 (min 3919.37, max 5362.89)","7038.39 (min 6552.32, max 7524.45)","4825.02 (min 3360.72, max 6289.31)","4598.91 (min 3895.38, max 5302.44)","4917.68 (min 4582.78, max 5252.57)","1716.29 (min 1551.59, max 1880.98)","7107.49 (min 6599.38, max 7615.59)","7176.61 (min 6655.26, max 7697.95)"
    "bw_mem-frd-2mb (MB/s)","4077.16 (min 3404.58, max 4749.73)","3805.78 (min 3613.01, max 3998.55)","4431.99 (min 2426.20, max 6437.77)","4836.20 (min 3895.18, max 5777.22)","4524.97 (min 3908.54, max 5141.39)","1592.14 (min 1574.49, max 1609.79)","4487.46 (min 4176.09, max 4798.82)","3829.27 (min 3551.00, max 4107.54)"
    "bw_mem-frd-4mb (MB/s)","3814.45 (min 3409.48, max 4219.41)","3382.76 (min 3115.87, max 3649.64)","4344.32 (min 2364.53, max 6324.11)","4716.95 (min 3836.56, max 5597.34)","4249.06 (min 3845.41, max 4652.71)","1588.01 (min 1581.34, max 1594.68)","4433.39 (min 3928.50, max 4938.27)","2831.06 (min 2747.72, max 2914.39)"
    "bw_mem-frd-8mb (MB/s)","3757.68 (min 3348.68, max 4166.67)","3212.97 (min 2856.63, max 3569.30)","4336.56 (min 2396.64, max 6276.48)","4227.09 (min 3067.88, max 5386.30)","4168.39 (min 3723.82, max 4612.95)","1637.49 (min 1597.13, max 1677.85)","4095.68 (min 3426.61, max 4764.74)","2858.44 (min 2749.14, max 2967.73)"
    "bw_mem-fwr-16mb (MB/s)","10571.52","10858.50","2343.64","9619.72","10934.56","7185.63","10297.67","10840.11"
    "bw_mem-fwr-1mb (MB/s)","8985.17 (min 5362.89, max 12607.45)","10627.63 (min 7524.45, max 13730.80)","5570.90 (min 4852.48, max 6289.31)","8909.92 (min 5302.44, max 12517.39)","9103.44 (min 5252.57, max 12954.30)","4653.13 (min 1880.98, max 7425.28)","10017.30 (min 7615.59, max 12419.01)","10723.07 (min 7697.95, max 13748.19)"
    "bw_mem-fwr-2mb (MB/s)","7998.11 (min 4749.73, max 11246.49)","8825.22 (min 3998.55, max 13651.88)","4684.09 (min 2930.40, max 6437.77)","8994.07 (min 5777.22, max 12210.92)","8433.51 (min 5141.39, max 11725.62)","4432.03 (min 1609.79, max 7254.26)","8949.63 (min 4798.82, max 13100.44)","8867.47 (min 4107.54, max 13627.40)"
    "bw_mem-fwr-4mb (MB/s)","7443.04 (min 4219.41, max 10666.67)","7946.54 (min 3649.64, max 12243.43)","4397.96 (min 2471.81, max 6324.11)","8799.05 (min 5597.34, max 12000.75)","5487.02 (min 4652.71, max 6321.33)","4406.80 (min 1594.68, max 7218.91)","8227.64 (min 4938.27, max 11517.01)","7584.43 (min 2914.39, max 12254.46)"
    "bw_mem-fwr-8mb (MB/s)","7383.98 (min 4166.67, max 10601.29)","7406.58 (min 3569.30, max 11243.85)","4319.05 (min 2361.62, max 6276.48)","8467.24 (min 5386.30, max 11548.18)","7757.93 (min 4612.95, max 10902.90)","4430.24 (min 1677.85, max 7182.62)","7685.65 (min 4764.74, max 10606.56)","7092.00 (min 2967.73, max 11216.26)"
    "bw_mem-rd-16mb (MB/s)","4896.71","3941.37","6597.03","5166.29","5351.17","1824.19","4958.17","3252.69"
    "bw_mem-rd-1mb (MB/s)","10138.54 (min 7076.35, max 13200.72)","15364.38 (min 13447.21, max 17281.55)","7424.58 (min 3925.42, max 10923.73)","6750.28 (min 5394.99, max 8105.56)","6299.83 (min 4100.55, max 8499.10)","1813.71 (min 1596.03, max 2031.39)","13655.38 (min 11954.26, max 15356.49)","14417.70 (min 13505.91, max 15329.48)"
    "bw_mem-rd-2mb (MB/s)","4273.15 (min 3014.89, max 5531.41)","4372.97 (min 2732.71, max 6013.23)","4030.53 (min 975.13, max 7085.92)","4026.04 (min 1599.23, max 6452.84)","4554.47 (min 3016.02, max 6092.92)","1667.59 (min 1516.99, max 1818.18)","5180.71 (min 3126.83, max 7234.58)","4190.28 (min 3081.14, max 5299.42)"
    "bw_mem-rd-4mb (MB/s)","3666.49 (min 2367.56, max 4965.42)","4000.42 (min 3501.40, max 4499.44)","3727.74 (min 788.80, max 6666.67)","3999.81 (min 1775.15, max 6224.47)","3906.79 (min 2411.82, max 5401.76)","1711.36 (min 1611.39, max 1811.32)","4376.13 (min 2907.50, max 5844.75)","3420.90 (min 3408.32, max 3433.48)"
    "bw_mem-rd-8mb (MB/s)","3550.57 (min 2247.51, max 4853.63)","3908.95 (min 3378.38, max 4439.51)","3671.77 (min 749.41, max 6594.13)","3983.64 (min 2053.39, max 5913.88)","3840.07 (min 2292.92, max 5387.21)","1721.16 (min 1618.12, max 1824.19)","4241.18 (min 2711.40, max 5770.96)","3391.94 (min 3336.58, max 3447.29)"
    "bw_mem-rdwr-16mb (MB/s)","2124.27","2453.61","750.47","1795.13","2229.97","1763.67","1836.97","2363.72"
    "bw_mem-rdwr-1mb (MB/s)","3292.44 (min 2446.70, max 4138.18)","6201.01 (min 2824.86, max 9577.16)","3313.88 (min 1261.03, max 5366.73)","2586.32 (min 1678.70, max 3493.93)","3643.09 (min 2599.81, max 4686.37)","1216.04 (min 832.92, max 1599.15)","6009.16 (min 3188.30, max 8830.02)","6297.12 (min 3270.65, max 9323.58)"
    "bw_mem-rdwr-2mb (MB/s)","2422.28 (min 2132.95, max 2711.60)","3166.47 (min 2446.70, max 3886.24)","989.86 (min 987.98, max 991.74)","1458.55 (min 1452.43, max 1464.66)","2527.89 (min 2182.21, max 2873.56)","1101.33 (min 826.90, max 1375.75)","2742.14 (min 2139.80, max 3344.48)","3209.76 (min 2415.88, max 4003.64)"
    "bw_mem-rdwr-4mb (MB/s)","2185.58 (min 2107.11, max 2264.04)","2740.64 (min 2507.84, max 2973.43)","890.24 (min 795.86, max 984.62)","1953.32 (min 1467.62, max 2439.02)","2301.01 (min 2176.67, max 2425.34)","1212.18 (min 866.93, max 1557.43)","2130.79 (min 1940.49, max 2321.08)","2608.21 (min 2471.04, max 2745.37)"
    "bw_mem-rdwr-8mb (MB/s)","2134.37 (min 2108.04, max 2160.70)","2523.02 (min 2235.57, max 2810.47)","871.65 (min 760.38, max 982.92)","1884.69 (min 1440.40, max 2328.97)","2224.21 (min 2179.24, max 2269.18)","1300.69 (min 904.67, max 1696.71)","2070.13 (min 2026.09, max 2114.16)","2491.17 (min 2225.62, max 2756.72)"
    "bw_mem-wr-16mb (MB/s)","2221.30","2777.78","742.77","1675.22","2257.65","1721.36","2160.41","2759.57"
    "bw_mem-wr-1mb (MB/s)","8669.45 (min 4138.18, max 13200.72)","13429.36 (min 9577.16, max 17281.55)","4646.08 (min 3925.42, max 5366.73)","4444.46 (min 3493.93, max 5394.99)","4393.46 (min 4100.55, max 4686.37)","1597.59 (min 1596.03, max 1599.15)","10392.14 (min 8830.02, max 11954.26)","11414.75 (min 9323.58, max 13505.91)"
    "bw_mem-wr-2mb (MB/s)","2863.25 (min 2711.60, max 3014.89)","3309.48 (min 2732.71, max 3886.24)","981.56 (min 975.13, max 987.98)","1531.95 (min 1464.66, max 1599.23)","2944.79 (min 2873.56, max 3016.02)","1446.37 (min 1375.75, max 1516.99)","3235.66 (min 3126.83, max 3344.48)","3542.39 (min 3081.14, max 4003.64)"
    "bw_mem-wr-4mb (MB/s)","2315.80 (min 2264.04, max 2367.56)","3237.42 (min 2973.43, max 3501.40)","792.33 (min 788.80, max 795.86)","2107.09 (min 1775.15, max 2439.02)","2418.58 (min 2411.82, max 2425.34)","1584.41 (min 1557.43, max 1611.39)","2424.00 (min 1940.49, max 2907.50)","3089.43 (min 2745.37, max 3433.48)"
    "bw_mem-wr-8mb (MB/s)","2204.11 (min 2160.70, max 2247.51)","3094.43 (min 2810.47, max 3378.38)","754.90 (min 749.41, max 760.38)","2191.18 (min 2053.39, max 2328.97)","2281.05 (min 2269.18, max 2292.92)","1657.42 (min 1618.12, max 1696.71)","2368.75 (min 2026.09, max 2711.40)","3046.65 (min 2756.72, max 3336.58)"
    "bw_mmap_rd-mo-1mb (MB/s)","8418.52","12825.65","12159.71","8773.50","8830.02","2017.24","12911.44","12913.79"
    "bw_mmap_rd-o2c-1mb (MB/s)","1410.93","2654.87","1645.64","1497.29","1459.59","676.82","2470.88","2496.88"
    "bw_pipe (MB/s)","1024.12","980.03","788.71","972.95","1021.29","763.33","1053.91","888.29"
    "bw_unix (MB/s)","2040.52","3010.53","1660.98","1937.14","2041.79","1062.60","2815.01","1658.61"
    "lat_connect (us)","37.59","37.44","37.00","36.85","37.47","57.08","37.41","37.60"
    "lat_ctx-2-128k (us)","5.21","5.24","4.97","5.02","5.10","7.73","5.13","5.19"
    "lat_ctx-2-256k (us)","4.50","4.43","4.62","4.38","4.47","9.46","4.22","7.36"
    "lat_ctx-4-128k (us)","5.01","6.56","5.03","4.93","5.05","7.35","4.99","7.81"
    "lat_ctx-4-256k (us)","4.36","5.17","4.09","4.19","3.98","6.04","3.70","4.94"
    "lat_fs-0k (num_files)","413.00","381.00","371.00","411.00","403.00","219.00","406.00","407.00"
    "lat_fs-10k (num_files)","170.00","194.00","148.00","163.00","161.00","116.00","179.00","197.00"
    "lat_fs-1k (num_files)","237.00","235.00","216.00","242.00","227.00","171.00","240.00","241.00"
    "lat_fs-4k (num_files)","261.00","262.00","238.00","257.00","246.00","167.00","245.00","253.00"
    "lat_mem_rd-stride128-sz1000k (ns)","12.45","6.08","10.44","11.48","11.67","33.21","5.76","8.10"
    "lat_mem_rd-stride128-sz125k (ns)","5.57","5.65","5.57","5.57","5.57","5.61","5.65","5.65"
    "lat_mem_rd-stride128-sz250k (ns)","5.57","5.65","5.57","5.57","5.57","5.83","5.65","5.65"
    "lat_mem_rd-stride128-sz31k (ns)","3.77","3.35","3.80","5.12","3.35","4.19","4.75","3.39"
    "lat_mem_rd-stride128-sz50 (ns)","2.00","2.00","2.00","2.00","2.00","2.15","2.00","2.00"
    "lat_mem_rd-stride128-sz500k (ns)","6.85","5.65","5.57","5.73","5.63","10.30","5.65","5.65"
    "lat_mem_rd-stride128-sz62k (ns)","5.12","5.20","5.12","5.34","5.57","5.27","4.76","5.42"
    "lat_mmap-1m (us)","29.00","35.00","34.00","32.00","29.00","50.00","29.00","29.00"
    "lat_ops-double-add (ns)","1.96","1.96","1.96","1.96","1.96","2.86","1.96","1.96"
    "lat_ops-double-div (ns)","9.01","9.01","9.01","9.01","9.01","15.74","9.01","9.01"
    "lat_ops-double-mul (ns)","2.00","2.00","2.00","2.00","2.00","2.86","2.00","2.00"
    "lat_ops-float-add (ns)","1.96","1.96","1.96","1.96","1.96","2.86","1.96","1.96"
    "lat_ops-float-div (ns)","5.53","5.51","5.51","5.51","5.51","9.30","5.51","5.50"
    "lat_ops-float-mul (ns)","2.00","2.00","2.00","2.00","2.00","2.86","2.00","2.00"
    "lat_ops-int-add (ns)","0.50","0.50","0.50","0.50","0.50","0.72","0.50","0.50"
    "lat_ops-int-bit (ns)","0.33","0.33","0.33","0.33","0.33","0.48","0.33","0.33"
    "lat_ops-int-div (ns)","4.01","4.00","4.00","4.01","4.01","4.30","4.01","4.01"
    "lat_ops-int-mod (ns)","4.67","4.67","4.67","4.67","4.68","4.53","4.67","4.67"
    "lat_ops-int-mul (ns)","1.52","1.52","1.52","1.52","1.52","3.07","1.52","1.52"
    "lat_ops-int64-add (ns)","0.50","0.50","0.50","0.50","0.50","0.72","0.50","0.50"
    "lat_ops-int64-bit (ns)","0.33","0.33","0.33","0.33","0.33","0.48","0.33","0.33"
    "lat_ops-int64-div (ns)","3.00","3.00","3.00","3.00","3.01","6.80","3.01","3.00"
    "lat_ops-int64-mod (ns)","5.68","5.67","5.67","5.67","5.67","5.24","5.68","5.67"
    "lat_ops-int64-mul (ns)","2.52","2.52","2.52","2.52","2.52","3.55","2.52","2.52"
    "lat_pagefault (us)","0.25","0.24","0.25","0.23","0.25","0.54","0.23","0.24"
    "lat_pipe (us)","14.29","19.76","14.60","15.09","14.90","24.84","15.94","19.58"
    "lat_proc-exec (us)","416.08","351.13","409.00","377.29","397.69","724.25","333.24","405.79"
    "lat_proc-fork (us)","368.13","388.47","362.87","331.00","363.87","618.44","297.78","381.21"
    "lat_proc-proccall (us)","0.00","0.00","0.00","0.00","0.00","0.01","0.00","0.00"
    "lat_select (us)","11.47","13.31","11.48","13.27","13.29","34.29","11.46","13.29"
    "lat_sem (us)","2.09","2.78","2.13","1.73","1.86","2.78","2.20","3.05"
    "lat_sig-catch (us)","3.01","3.08","2.97","2.99","3.11","5.54","2.98","2.99"
    "lat_sig-install (us)","0.55","0.54","0.54","0.54","0.53","0.68","0.53","0.54"
    "lat_sig-prot (us)","0.70","0.76","0.66","0.64","0.73","0.77","0.66","0.71"
    "lat_syscall-fstat (us)","0.94","0.94","0.96","0.95","0.97","1.96","0.91","0.95"
    "lat_syscall-null (us)","0.39","0.40","0.39","0.38","0.39","0.46","0.39","0.39"
    "lat_syscall-open (us)","144.71","214.31","149.54","149.00","178.17","183.57","106.63","199.07"
    "lat_syscall-read (us)","0.52","0.50","0.51","0.50","0.51","0.79","0.51","0.51"
    "lat_syscall-stat (us)","2.35","2.38","2.32","2.31","2.33","4.76","2.32","2.35"
    "lat_syscall-write (us)","0.48","0.54","0.49","0.47","0.49","0.76","0.47","0.49"
    "lat_tcp (us)","0.81","0.81","0.81","0.82","0.84","0.91","0.81","0.82"
    "lat_unix (us)","19.41","20.06","19.59","19.11","19.31","30.00","19.65","26.32"
    "latency_for_0.50_mb_block_size (nanosec)","6.85","5.65","5.57","5.73","5.63","10.30","5.65","5.65"
    "latency_for_1.00_mb_block_size (nanosec)","6.23 (min 0.00, max 12.45)","3.04 (min 0.00, max 6.08)","5.22 (min 0.00, max 10.44)","5.74 (min 0.00, max 11.48)","5.83 (min 0.00, max 11.67)","16.61 (min 0.00, max 33.21)","2.88 (min 0.00, max 5.76)","4.05 (min 0.00, max 8.10)"
    "pipe_bandwidth (MBs)","1024.12","980.03","788.71","972.95","1021.29","763.33","1053.91","888.29"
    "pipe_latency (microsec)","14.29","19.76","14.60","15.09","14.90","24.84","15.94","19.58"
    "procedure_call (microsec)","0.00","0.00","0.00","0.00","0.00","0.01","0.00","0.00"
    "select_on_200_tcp_fds (microsec)","11.47","13.31","11.48","13.27","13.29","34.29","11.46","13.29"
    "semaphore_latency (microsec)","2.09","2.78","2.13","1.73","1.86","2.78","2.20","3.05"
    "signal_handler_latency (microsec)","0.55","0.54","0.54","0.54","0.53","0.68","0.53","0.54"
    "signal_handler_overhead (microsec)","3.01","3.08","2.97","2.99","3.11","5.54","2.98","2.99"
    "tcp_ip_connection_cost_to_localhost (microsec)","37.59","37.44","37.00","36.85","37.47","57.08","37.41","37.60"
    "tcp_latency_using_localhost (microsec)","0.81","0.81","0.81","0.82","0.84","0.91","0.81","0.82"




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
    "dhrystone_per_mhz (DMIPS/MHz)","5.70","5.70","5.70","5.70","5.20","2.90","5.20","5.70"
    "dhrystone_per_second (DhrystoneP)","20000000.00","20000000.00","20000000.00","20000000.00","18181818.00","7142857.00","18181818.00","20000000.00"




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

    "linpack (Kflops)","2616870.00","2549820.00","2614877.00","2432401.00","2548875.00","576643.00","2436716.00","2394235.00"




NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "assignment (Iterations)","31.88","31.91","31.94","31.87","31.91","14.43","31.84","31.85"
    "fourier (Iterations)","59956.00","59729.00","56778.00","60193.00","59950.00","22831.00","59982.00","65337.00"
    "fp_emulation (Iterations)","388.00","387.99","387.97","388.04","387.88","215.64","387.95","387.96"
    "huffman (Iterations)","2492.20","2486.10","2494.30","2491.20","2494.70","1184.50","2489.20","2496.60"
    "idea (Iterations)","7996.00","7996.50","7990.10","7996.40","7994.50","3444.70","7990.80","7996.40"
    "lu_decomposition (Iterations)","1375.30","1348.10","1362.90","1372.90","1389.40","532.33","1354.30","1362.60"
    "neural_net (Iterations)","28.67","26.77","28.99","28.98","28.98","8.66","28.99","28.97"
    "numeric_sort (Iterations)","884.26","881.83","877.69","881.67","885.45","627.99","879.92","883.68"
    "string_sort (Iterations)","344.56","353.90","345.54","361.94","353.61","163.94","359.43","361.87"




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

    "add (MB/s)","6295.40","5775.10","5455.20","5259.40","6521.20","2427.30","6420.20","5709.80"
    "copy (MB/s)","6913.60","5475.30","4779.00","5526.40","7801.00","3542.90","7450.50","5298.90"
    "scale (MB/s)","7052.20","5485.70","4841.10","5381.00","7922.00","3239.10","7587.60","5281.60"
    "triad (MB/s)","6298.60","5759.70","5462.10","5232.80","6521.00","2230.00","6422.10","5699.80"




CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","82.64","81.97","80.00","82.64","81.97","42.02","82.64","80.00"
    "core (workloads/)","0.78","0.78","0.78","0.78","0.77","0.30","0.78","0.78"
    "coremark-pro ()","2510.69","2510.20","2464.63","2504.44","2494.95","920.51","2530.19","2507.07"
    "linear_alg-mid-100x100-sp (workloads/)","79.87","79.37","80.26","80.39","81.70","14.68","80.39","78.00"
    "loops-all-mid-10k-sp (workloads/)","2.48","2.47","2.44","2.46","2.46","0.70","2.46","2.46"
    "nnet_test (workloads/)","3.73","3.62","3.68","3.64","3.66","1.09","3.80","3.86"
    "parser-125k (workloads/)","11.11","10.87","11.11","11.11","10.87","8.77","10.87","10.87"
    "radix2-big-64k (workloads/)","285.14","300.57","263.64","281.69","282.49","60.07","302.39","291.80"
    "sha-test (workloads/)","156.25","158.73","158.73","158.73","156.25","81.30","158.73","158.73"
    "zip-test (workloads/)","47.62","47.62","45.45","47.62","47.62","22.22","47.62","47.62"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","161.29","166.67","163.93","163.93","163.93","83.33","163.93","161.29"
    "core (workloads/)","1.55","1.55","1.56","1.55","1.55","0.60","1.55","1.56"
    "coremark-pro ()","4437.96","4972.89","4424.55","4453.79","4493.92","1644.93","4716.60","4779.47"
    "linear_alg-mid-100x100-sp (workloads/)","160.77","159.74","161.81","159.24","161.81","29.34","159.74","160.77"
    "loops-all-mid-10k-sp (workloads/)","3.96","4.35","4.17","3.86","3.85","1.28","3.90","4.84"
    "nnet_test (workloads/)","7.26","7.27","7.35","7.65","7.25","2.17","7.35","7.23"
    "parser-125k (workloads/)","21.05","21.74","20.83","21.28","21.05","13.25","20.83","21.05"
    "radix2-big-64k (workloads/)","273.67","604.23","256.35","270.34","308.45","67.39","439.37","421.76"
    "sha-test (workloads/)","312.50","322.58","312.50","312.50","312.50","161.29","322.58","322.58"
    "zip-test (workloads/)","90.91","95.24","86.96","90.91","90.91","42.55","95.24","90.91"

 


.. csv-table:: CoreMarkProFourCore Benchmarks
    :header: "Benchmarks","am69_sk-fs: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","322.58","158.73","312.50","322.58"
    "core (workloads/)","3.11","1.20","3.09","3.11"
    "coremark-pro ()","8840.76","2557.45","7823.27","8867.06"
    "linear_alg-mid-100x100-sp (workloads/)","310.56","56.37","308.64","308.64"
    "loops-all-mid-10k-sp (workloads/)","7.64","2.07","5.72","7.51"
    "nnet_test (workloads/)","12.24","3.62","12.21","12.77"
    "parser-125k (workloads/)","42.11","8.71","37.38","40.00"
    "radix2-big-64k (workloads/)","831.95","89.22","436.49","882.61"
    "sha-test (workloads/)","526.32","270.27","526.32","526.32"
    "zip-test (workloads/)","173.91","78.43","173.91","173.91"

 


.. csv-table:: CoreMarkProEightCore Benchmarks
    :header: "Benchmarks","am69_sk-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","625.00","625.00"
    "core (workloads/)","6.20","6.20"
    "coremark-pro ()","14045.95","14111.66"
    "linear_alg-mid-100x100-sp (workloads/)","581.40","581.40"
    "loops-all-mid-10k-sp (workloads/)","10.30","9.98"
    "nnet_test (workloads/)","19.19","19.08"
    "parser-125k (workloads/)","72.73","72.07"
    "radix2-big-64k (workloads/)","816.33","825.76"
    "sha-test (workloads/)","769.23","769.23"
    "zip-test (workloads/)","296.30","320.00"

 
 


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

    "4m-check (workloads/)","828.64","1018.33","871.99","852.66","830.01","408.43","1173.71","1012.56"
    "4m-check-reassembly (workloads/)","151.75","188.32","119.76","141.24","152.91","121.66","189.39","187.97"
    "4m-check-reassembly-tcp (workloads/)","92.59","109.17","88.65","97.28","93.99","59.52","110.62","107.76"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","39.55","35.11","40.76","41.49","41.90","32.93","56.23","38.36"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","2.68","4.88","2.68","2.66","2.67","1.90","4.83","4.85"
    "4m-cmykw2 (workloads/)","312.50","589.97","313.48","314.96","289.86","245.40","597.02","604.23"
    "4m-cmykw2-rotatew2 (workloads/)","59.88","43.42","59.46","62.83","60.12","50.34","72.12","50.34"
    "4m-reassembly (workloads/)","124.38","134.23","104.49","126.26","124.84","104.28","140.65","131.23"
    "4m-rotatew2 (workloads/)","69.35","47.46","69.74","73.37","69.30","55.40","77.58","62.54"
    "4m-tcp-mixed (workloads/)","262.30","242.42","275.86","266.67","262.30","118.52","271.19","262.30"
    "4m-x264w2 (workloads/)","2.73","5.05","2.75","2.79","2.73","1.96","4.78","5.02"
    "idct-4m (workloads/)","34.76","35.11","34.90","35.06","34.48","19.17","35.05","35.10"
    "idct-4mw1 (workloads/)","34.95","35.04","34.90","34.98","34.54","19.17","34.99","35.12"
    "ippktcheck-4m (workloads/)","825.36","1006.85","870.78","850.63","811.43","412.47","1180.36","1009.29"
    "ippktcheck-4mw1 (workloads/)","831.39","1010.51","873.21","866.55","831.67","410.51","1180.92","1018.33"
    "ipres-4m (workloads/)","166.48","187.27","157.07","179.43","170.07","111.03","194.81","184.05"
    "ipres-4mw1 (workloads/)","163.04","186.80","158.40","179.43","165.93","110.46","195.57","182.70"
    "md5-4m (workloads/)","43.52","45.72","43.86","46.95","43.98","28.58","48.76","45.75"
    "md5-4mw1 (workloads/)","44.17","45.66","44.19","47.42","43.73","28.13","48.54","45.45"
    "rgbcmyk-4m (workloads/)","162.47","163.40","162.47","163.27","162.87","62.40","163.80","163.53"
    "rgbcmyk-4mw1 (workloads/)","162.73","160.13","162.47","163.27","160.00","62.36","163.67","163.13"
    "rotate-4ms1 (workloads/)","51.39","53.36","51.33","54.11","51.39","23.65","53.88","53.30"
    "rotate-4ms1w1 (workloads/)","51.07","53.48","50.97","53.65","50.66","23.64","53.65","53.25"
    "rotate-4ms64 (workloads/)","52.52","54.88","53.08","55.19","52.19","23.84","55.13","55.49"
    "rotate-4ms64w1 (workloads/)","52.08","54.64","52.47","55.19","52.63","23.84","54.41","55.93"
    "x264-4mq (workloads/)","1.37","1.42","1.42","1.43","1.41","0.58","1.42","1.42"
    "x264-4mqw1 (workloads/)","1.43","1.42","1.42","1.43","1.42","0.58","1.43","1.42"



 
 


Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am68_sk-fs: Boot time in seconds: avg(min,max)","am69_sk-fs: Boot time in seconds: avg(min,max)","j7200-evm: Boot time in seconds: avg(min,max)","j721e-idk-gw: Boot time in seconds: avg(min,max)","j721s2-evm: Boot time in seconds: avg(min,max)","j722s_evm-fs: Boot time in seconds: avg(min,max)","j742s2_evm-fs: Boot time in seconds: avg(min,max)","j784s4-evm: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","19.98 (min 19.29, max 21.49)","20.51 (min 20.03, max 23.56)","18.69 (min 18.54, max 19.15)","22.84 (min 22.62, max 23.23)","21.76 (min 21.11, max 22.59)","20.73 (min 20.47, max 20.88)","19.97 (min 19.68, max 20.42)","18.99 (min 18.73, max 19.27)"

 

 

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

    "8000","","","","","255988.00","0.36","1023972.00","0.21"
    "11025","352792.00","0.22","1023969.00","0.68","331809.00","0.35","1023986.00","0.23"
    "16000","511991.00","0.34","1023981.00","0.73","511977.00","0.41","1023962.00","0.20"
    "22050","705576.00","0.30","1023971.00","0.68","663631.00","0.50","1023980.00","0.18"
    "24000","705583.00","0.32","1023981.00","0.72","663613.00","0.44","1023984.00","0.19"
    "32000","1023980.00","0.23","1023982.00","0.85","1023928.00","0.55","1023959.00","0.18"
    "44100","1411175.00","0.55","1417797.00","0.77","1327230.00","0.67","1417803.00","0.19"
    "48000","1535973.00","0.79","1535957.00","0.76","1535911.00","0.69","1535961.00","0.22"
    "88200","2822350.00","1.03","2835619.00","1.21","2654476.00","1.02","2835624.00","0.30"
    "96000","3071946.00","0.52","3071925.00","1.39","3071832.00","1.11","3071929.00","0.37"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","j721e-idk-gw: Throughput (bits/sec)","j721e-idk-gw: CPU Load (%)","j784s4-evm: Throughput (bits/sec)","j784s4-evm: CPU Load (%)"

    "8000","","","1024384.00","0.19"
    "11025","352937.00","0.33","1024401.00","0.16"
    "16000","512203.00","0.29","1024409.00","0.22"
    "22050","705866.00","0.45","1024410.00","0.22"
    "24000","705874.00","0.42","1024408.00","0.22"
    "32000","1024402.00","0.57","1024379.00","0.17"
    "44100","1411756.00","0.67","1418387.00","0.21"
    "48000","1536606.00","0.83","1536594.00","0.21"
    "88200","2823511.00","1.08","2836793.00","0.33"
    "96000","3073210.00","1.43","3073197.00","0.42"

 
 



 



|

Graphics SGX/RGX Driver
-------------------------
 


GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am68_sk-fs: Score","am68_sk-fs: Fps","am69_sk-fs: Score","am69_sk-fs: Fps","j721e-idk-gw: Score","j721e-idk-gw: Fps","j721s2-evm: Score","j721s2-evm: Fps","j742s2_evm-fs: Score","j742s2_evm-fs: Fps","j784s4-evm: Score","j784s4-evm: Fps"

    " GFXBench 3.x gl_manhattan_off","963.05","15.53","920.62","14.85","1212.52","19.56","945.27","15.25","937.66","15.12","898.98","14.50"
    " GFXBench 3.x gl_trex_off","1596.65","28.51","1483.08","26.48","1833.75","32.75","1637.43","29.24","1633.93","29.18","1461.97","26.11"
    " GFXBench 4.x gl_4_off","264.06","4.47","253.73","4.29","411.95","6.97","258.89","4.38","260.87","4.41","252.93","4.28"
    " GFXBench 5.x gl_5_high_off","113.36","1.76","111.19","1.73","179.00","2.78","113.87","1.77","113.79","1.77","111.94","1.74"



 
 

 

 



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

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","0.02","95.81","0.02","29.68","1769.03","81.30","1857.66","89.03","1861.43","79.74","1519.66","50.47","1856.72","43.52","1688.73","27.40"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1861.64","44.72","1876.90","40.13","1617.82","23.20","1877.04","12.65"




.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: Packets Per Second (kPPS)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","4.72","33.00","15.89","18.00","5.83","40.00","15.47","18.00","22.73","158.00","43.81","18.00","22.85","159.00","21.79"
    "128","82.00","117.90","180.00","81.21","82.00","76.47","117.00","26.11","82.00","106.25","162.00","44.45","82.00","107.89","164.00","22.09"
    "256","210.00","111.72","67.00","31.44","210.00","179.09","107.00","39.79","210.00","272.79","162.00","44.23","210.00","269.83","161.00","22.26"
    "1024","978.00","109.53","14.00","4.39","978.00","787.45","101.00","27.33","978.00","662.10","85.00","23.93","978.00","936.42","120.00","18.81"
    "1518","1472.00","304.98","26.00","16.24","1472.00","954.98","81.00","36.20","1472.00","669.95","57.00","16.32","1472.00","955.00","81.00","11.59"




.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","1.68","12.00","7.21"
    "128","82.00","5.12","8.00","7.01","82.00","3.94","6.00","0.95","82.00","45.06","69.00","6.79"
    "256","210.00","14.28","9.00","2.68","210.00","30.74","18.00","2.04","210.00","70.90","42.00","7.19"
    "1024","978.00","64.16","8.00","5.87","978.00","236.28","30.00","5.17"
    "1518","1472.00","949.76","81.00","73.73","1472.00","954.39","81.00","32.57"




.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j721e-idk-gw: Packet Loss %","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: Packet Loss %","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: Packet Loss %"

    "64","18.00","53.83","374.00","91.85","6.89"
    "128","82.00","225.25","343.00","90.62","19.90","82.00","248.97","380.00","44.15","49.33","82.00","220.43","336.00","22.86","14.04"
    "256","210.00","552.35","329.00","90.82","24.67","210.00","490.25","292.00","43.93","32.09","210.00","398.12","237.00","17.79","0.01"
    "1024","978.00","915.21","117.00","81.85","1.50","978.00","704.10","90.00","17.29","0.01"
    "1518","1472.00","949.76","81.00","73.73","0.00","1472.00","954.39","81.00","32.57","0.00"

 
 

 

 
 



|

PCIe Driver
-------------------------


 


PCIe-NVMe-SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^
 

 


J721E-IDK-GW
"""""""""""""""""""""""""""




.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","709.00","13.27","1514.00","8.10"
    "4m","708.00","12.08","1514.00","5.26"
    "4k","183.00","48.65","103.00","34.86"
    "256k","733.00","15.27","1510.00","14.91"



- Filesize used is: 10G
- FIO command options: --ioengine=libaio --iodepth=4 --numjobs=1 --direct=1 --runtime=60 --time_based 
- Platform: Speed 8GT/s, Width x2
- SSD being used: PLEXTOR PX-128M8PeY
 

 


J721S2-EVM
"""""""""""""""""""""""""""




.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","730.00","18.61","771.00","6.92"
    "4m","731.00","15.96","771.00","5.64"
    "4k","185.00","52.60","280.00","51.60"
    "256k","749.00","20.36","786.00","10.63"



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

    "102400","0.71 (min 0.54, max 1.35)","53.93 (min 47.51, max 59.36)","83.33","20.00"
    "262144","0.48 (min 0.33, max 0.59)","53.97 (min 51.41, max 55.81)","84.56","40.00"
    "524288","0.48 (min 0.38, max 0.54)","52.82 (min 50.19, max 53.76)","84.38","42.86"
    "1048576","0.50 (min 0.38, max 0.54)","53.83 (min 52.14, max 55.46)","83.59","40.00"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j721e-idk-gw: Raw Read Throughput (Mbytes/sec)"

    "50","250.00"

 
 


J722S-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j722s_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Write UBIFS CPU Load (%)","j722s_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.28)","28.65 (min 24.90, max 32.82)","63.82","15.38"
    "262144","0.14 (min 0.10, max 0.19)","29.25 (min 27.18, max 31.73)","66.01","16.67"
    "524288","0.15 (min 0.11, max 0.19)","29.77 (min 27.77, max 32.93)","63.02","21.43"
    "1048576","0.15 (min 0.11, max 0.19)","30.59 (min 28.69, max 31.77)","63.72","15.38"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j722s_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","227.27"

 
 


AM68-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am68_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","238.09"

 
 



AM69-SK
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","am69_sk-fs: Write UBIFS Throughput (Mbytes/sec)","am69_sk-fs: Write UBIFS CPU Load (%)","am69_sk-fs: Read UBIFS Throughput (Mbytes/sec)","am69_sk-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.30)","15.25 (min 12.35, max 16.23)","79.17","4.76"
    "262144","0.13 (min 0.10, max 0.17)","15.02 (min 12.54, max 16.89)","72.59","8.33"
    "524288","0.14 (min 0.11, max 0.19)","14.96 (min 13.82, max 15.90)","77.98","4.76"
    "1048576","0.13 (min 0.10, max 0.18)","14.63 (min 13.01, max 16.02)","75.46","4.35"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","am69_sk-fs: Raw Read Throughput (Mbytes/sec)"

    "50","263.16"

 
 


J7200-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j7200-evm: Write UBIFS Throughput (Mbytes/sec)","j7200-evm: Write UBIFS CPU Load (%)","j7200-evm: Read UBIFS Throughput (Mbytes/sec)","j7200-evm: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.30)","50.03 (min 49.61, max 50.27)","78.71","40.00"
    "262144","0.15 (min 0.11, max 0.19)","50.22 (min 50.09, max 50.41)","77.84","25.00"
    "524288","0.15 (min 0.11, max 0.19)","50.21 (min 50.02, max 50.71)","76.13","20.00"
    "1048576","0.16 (min 0.11, max 0.19)","50.14 (min 49.98, max 50.44)","74.78","33.33"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j7200-evm: Raw Read Throughput (Mbytes/sec)"

    "50","227.27"

 
 

 


J784S4-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j784s4-evm: Write UBIFS Throughput (Mbytes/sec)","j784s4-evm: Write UBIFS CPU Load (%)","j784s4-evm: Read UBIFS Throughput (Mbytes/sec)","j784s4-evm: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.28)","14.54 (min 12.50, max 16.11)","80.11","13.04"
    "262144","0.13 (min 0.10, max 0.18)","14.81 (min 13.79, max 15.81)","80.19","13.04"
    "524288","0.13 (min 0.10, max 0.18)","15.92 (min 14.82, max 17.09)","73.03","8.70"
    "1048576","0.13 (min 0.10, max 0.18)","15.11 (min 13.25, max 16.62)","77.14","8.70"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j784s4-evm: Raw Read Throughput (Mbytes/sec)"

    "50","227.27"

 
 



J742S2-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j742s2_evm-fs: Write UBIFS CPU Load (%)","j742s2_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j742s2_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.27)","28.22 (min 24.82, max 31.90)","73.62","9.09"
    "262144","0.14 (min 0.10, max 0.18)","28.24 (min 26.62, max 31.13)","74.01","10.00"
    "524288","0.14 (min 0.11, max 0.18)","29.16 (min 27.90, max 30.30)","74.54","16.67"
    "1048576","0.14 (min 0.10, max 0.18)","28.06 (min 26.88, max 30.19)","72.76","9.09"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j742s2_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","250.00"

 
 

 

 
 

 



|

UBoot QSPI/OSPI Driver
-------------------------

 










J721E-IDK-GW
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","1026.82","15875.97"
    "800000","1027.85","16062.75"
    "1000000","1027.98","16173.74"
    "2000000","1028.34","16213.76"








J721S2-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "400000","1000.49","15875.97"
    "800000","1001.47","16062.75"
    "1000000","1001.83","16157.79"
    "2000000","1001.96","16221.78"




J784S4-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","990.09","15814.67"
    "800000","992.01","16062.75"
    "1000000","991.23","16157.79"
    "2000000","990.36","16213.76"




J742S2-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","981.55","15875.97"
    "800000","982.49","16062.75"
    "1000000","982.78","16157.79"
    "2000000","983.37","16221.78"



















 
 

 

 



|

UBoot UFS Driver
-------------------------


J721E-IDK-GW
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","80313.73","372363.64"
    "800000","97523.81","512000.00"
    "1000000","102400.00","630153.85"








J784S4-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","71859.65","372363.64"
    "800000","102400.00","512000.00"
    "1000000","105025.64","630153.85"

 


J742S2-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT UFS RAW
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","215578.95","372363.64"
    "800000","240941.18","512000.00"
    "1000000","230760.56","630153.85"

 
 



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

    "1m","59.10","1.79","313.00","2.04"
    "4m","59.20","1.43","291.00","1.31"
    "4k","53.70","23.64","56.30","20.28"
    "256k","60.40","2.19","312.00","3.86"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","59.20","1.65","175.00","1.23"
    "4m","58.10","1.27","175.00","0.70"
    "4k","51.00","21.55","56.70","20.01"
    "256k","59.80","1.90","174.00","2.16"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

    "1m","94.90","1.71","174.00","2.04"
    "4m","95.20","1.21","174.00","1.59"
    "4k","67.80","21.97","94.30","22.62"
    "256k","94.80","2.20","173.00","2.77"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","59.80","4.17","315.00","4.19"
    "4m","60.30","3.49","314.00","3.60"
    "4k","58.00","28.91","56.50","24.50"
    "256k","60.10","4.34","316.00","5.73"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

    "1m","98.10","0.50","281.00","0.66"
    "4m","98.50","0.47","263.00","0.25"
    "4k","83.00","11.00","94.20","9.43"
    "256k","98.10","0.64","295.00","0.92"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Write EXT4 CPU Load (%)","j742s2_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Read EXT4 CPU Load (%)"

    "1m","97.50","1.07","294.00","0.99"
    "4m","97.00","1.06","216.00","0.55"
    "4k","83.30","21.12","86.60","17.13"
    "256k","97.50","1.13","294.00","2.04"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Write EXT4 CPU Load (%)","am69_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Read EXT4 CPU Load (%)"

    "1m","90.00","0.49","287.00","0.55"
    "4m","89.20","0.44","250.00","0.24"
    "4k","78.10","10.11","92.90","9.47"
    "256k","90.30","0.67","287.00","0.92"

 

 

 

 

 

 

 
 


EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "1m","59.10","1.75","314.00","1.93"
    "4m","59.00","1.52","309.00","1.29"
    "4k","55.50","18.75","56.30","18.93"
    "256k","59.00","2.03","312.00","3.63"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "1m","59.40","1.50","175.00","1.27"
    "4m","58.60","1.24","175.00","0.73"
    "4k","53.10","17.00","56.70","18.08"
    "256k","59.50","1.61","174.00","2.19"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "1m","95.60","1.67","174.00","2.04"
    "4m","96.20","1.28","174.00","1.55"
    "4k","69.00","16.73","93.40","20.54"
    "256k","95.60","2.08","173.00","2.68"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "1m","61.10","1.93","314.00","2.32"
    "4m","60.40","1.62","310.00","1.54"
    "4k","55.40","20.40","56.10","20.32"
    "256k","61.10","2.25","311.00","4.13"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "1m","80.10","0.40","112.00","0.24"
    "4m","80.50","0.44","95.10","0.22"
    "4k","8.68","0.92","56.60","5.20"
    "256k","70.20","0.46","94.20","0.53"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "1m","78.60","0.90","111.00","0.55"
    "4m","78.70","0.90","95.00","0.38"
    "4k","8.60","1.96","56.50","11.19"
    "256k","69.00","0.89","94.20","0.77"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write Raw Throughput (Mbytes/sec)","am69_sk-fs: Write Raw CPU Load (%)","am69_sk-fs: Read Raw Throughput (Mbytes/sec)","am69_sk-fs: Read Raw CPU Load (%)"

    "1m","89.00","0.52","292.00","0.41"
    "4m","96.10","0.44","292.00","0.28"
    "4k","77.10","7.71","88.30","8.01"
    "256k","89.20","0.60","292.00","0.89"

 

 

 

 

 

 

 
 

 

 

 

 

 
 



UBoot EMMC Driver
-----------------

 

 

 

 

 

 

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

    "2000000","58829.44","306242.99"
    "4000000","60069.66","307680.75"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "2000000","58099.29","173375.66"
    "4000000","59148.01","177604.34"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j722s_evm-fs: Write Throughput (Kbytes/sec)","j722s_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","98107.78","172463.16"
    "4000000","96093.84","175699.73"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "2000000","58935.25","309132.08"
    "4000000","59904.94","312076.19"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "2000000","98107.78","282482.76"
    "4000000","96234.95","293883.41"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","99296.97","284939.13"
    "4000000","97378.90","293883.41"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am69_sk-fs: Write Throughput (Kbytes/sec)","am69_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","100824.62","284939.13"
    "4000000","98698.80","292571.43"

 

 

 

 

 

 

 
 

 


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
    :header: "Buffer size (bytes)","j7200-evm: Write EXT4 Throughput (Mbytes/sec)","j7200-evm: Write EXT4 CPU Load (%)","j7200-evm: Read EXT4 Throughput (Mbytes/sec)","j7200-evm: Read EXT4 CPU Load (%)"

    "1m","41.90","1.37","87.40","1.13"
    "4m","41.40","1.19","87.30","0.71"
    "4k","2.79","2.20","12.90","6.22"
    "256k","37.10","1.61","83.30","1.51"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","42.50","1.81","87.20","1.19"
    "4m","41.60","1.47","87.10","0.99"
    "4k","2.78","2.55","12.90","7.01"
    "256k","37.70","1.98","83.40","1.73"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

    "1m","41.90","0.33","87.10","0.38"
    "4m","41.60","0.30","86.90","0.23"
    "4k","2.78","0.67","12.80","1.70"
    "256k","35.60","0.34","83.30","0.38"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Write EXT4 CPU Load (%)","j742s2_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Read EXT4 CPU Load (%)"

    "1m","17.90","0.51","86.80","0.62"
    "4m","18.00","0.47","86.80","0.46"
    "4k","4.13","2.04","14.30","4.75"
    "256k","17.40","0.49","82.90","0.82"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","32.60","1.12","43.40","0.66"
    "4m","34.30","0.92","43.40","0.65"
    "4k","2.82","2.01","11.20","5.07"
    "256k","33.00","1.40","42.40","0.92"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

    "1m","41.80","1.33","87.20","1.58"
    "4m","42.50","0.91","87.50","1.20"
    "4k","2.80","1.88","12.90","4.48"
    "256k","37.20","1.51","83.70","1.83"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am68_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am68_sk-fs: Write EXT4 CPU Load (%)","am68_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am68_sk-fs: Read EXT4 CPU Load (%)"

    "1m","18.50","1.10","86.80","1.12"
    "4m","18.40","0.79","85.70","0.84"
    "4k","4.41","3.55","13.50","6.97"
    "256k","17.50","1.13","81.50","1.62"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Write EXT4 CPU Load (%)","am69_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Read EXT4 CPU Load (%)"

    "1m","18.70","0.16","86.40","0.28"
    "4m","18.70","0.16","86.20","0.16"
    "4k","4.64","1.01","14.40","2.11"
    "256k","17.80","0.15","83.30","0.40"

 

 

 

 

 

 

 

 

 
 


MMC RAW FIO 1G
^^^^^^^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "1m","44.10","1.34","88.10","0.92"
    "4m","43.90","1.20","88.00","0.70"
    "4k","2.82","1.92","13.00","5.87"
    "256k","38.40","1.52","84.20","1.34"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "1m","45.00","1.71","88.30","1.32"
    "4m","44.90","1.45","88.20","1.03"
    "4k","2.82","2.43","13.00","6.35"
    "256k","41.20","2.17","84.50","1.71"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "1m","45.30","0.33","88.20","0.23"
    "4m","43.70","0.34","87.90","0.21"
    "4k","2.83","0.59","13.10","1.67"
    "256k","41.50","0.34","84.20","0.35"

 

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "1m","33.80","0.96","43.80","0.55"
    "4m","33.40","0.81","43.80","0.54"
    "4k","2.80","1.81","11.30","4.78"
    "256k","30.90","1.17","42.90","0.89"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "1m","42.60","1.12","88.20","1.38"
    "4m","42.00","0.83","88.30","1.02"
    "4k","2.82","1.57","13.00","4.09"
    "256k","36.60","1.09","84.50","1.75"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am68_sk-fs: Write Raw Throughput (Mbytes/sec)","am68_sk-fs: Write Raw CPU Load (%)","am68_sk-fs: Read Raw Throughput (Mbytes/sec)","am68_sk-fs: Read Raw CPU Load (%)"

    "1m","18.20","0.89","87.50","1.05"
    "4m","18.20","0.74","87.40","0.77"
    "4k","3.98","2.81","13.60","6.55"
    "256k","17.60","0.94","83.90","1.48"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write Raw Throughput (Mbytes/sec)","am69_sk-fs: Write Raw CPU Load (%)","am69_sk-fs: Read Raw Throughput (Mbytes/sec)","am69_sk-fs: Read Raw CPU Load (%)"

    "1m","44.90","0.24","88.30","0.19"
    "4m","44.90","0.26","88.20","0.15"
    "4k","2.82","0.53","13.00","1.55"
    "256k","41.30","0.29","84.50","0.33"

 

 

 
 


MMC EXT4
^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "102400","36.12 (min 34.37, max 38.06)","3.08 (min 2.78, max 4.18)","75.74","4.52"
    "262144","37.01 (min 35.73, max 37.91)","3.19 (min 2.79, max 4.39)","87.10","3.18"
    "524288","38.75 (min 38.34, max 40.05)","3.14 (min 2.75, max 4.03)","91.34","5.22"
    "1048576","38.02 (min 37.75, max 38.59)","3.03 (min 2.53, max 4.22)","90.70","4.77"
    "5242880","40.93 (min 39.23, max 41.86)","3.14 (min 2.90, max 3.85)","91.43","4.82"

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 


MMC EXT2
^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "102400","39.16 (min 34.56, max 40.58)","3.71 (min 2.98, max 5.93)","80.55","4.63"
    "262144","37.00 (min 33.63, max 38.47)","3.42 (min 2.82, max 5.37)","86.39","5.76"
    "524288","39.82 (min 35.27, max 41.59)","3.50 (min 2.81, max 5.56)","90.30","4.57"
    "1048576","36.80 (min 32.63, max 38.55)","3.27 (min 2.77, max 5.07)","90.44","5.39"
    "5242880","36.71 (min 33.54, max 37.85)","3.34 (min 2.61, max 5.51)","90.60","5.41"

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 



UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j722s_evm-fs: Write Throughput (Kbytes/sec)","j722s_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","40554.46","81920.00"
    "800000","43574.47","87148.94"
    "1000000","44765.03","89530.05"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","13170.42","44521.74"
    "800000","20177.34","45765.36"
    "1000000","22914.69","46413.60"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

    "400000","40554.46","83591.84"
    "800000","48761.90","88086.02"
    "1000000","47627.91","90519.34"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "400000","33573.77","83591.84"
    "800000","35310.34","88086.02"
    "1000000","47352.60","90519.34"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","27675.68","78769.23"
    "800000","20428.93","86231.58"
    "1000000","17847.49","89530.05"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","39384.62","83591.84"
    "800000","40960.00","88086.02"
    "1000000","41478.48","90519.34"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am68_sk-fs: Write Throughput (Kbytes/sec)","am68_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","27863.95","83591.84"
    "800000","15753.85","88086.02"
    "1000000","25520.25","90519.34"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am69_sk-fs: Write Throughput (Kbytes/sec)","am69_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","31751.94","83591.84"
    "800000","33436.73","88086.02"
    "1000000","50103.98","91022.22"

 

 

 

 

 

 

 

 

 
 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 



|

USB Driver
-------------------------
 


USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^










.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721e-idk-gw: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j722s_evm-fs: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

    "150","9.90","41.50","32.90","45.10","44.00","43.60"




.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721e-idk-gw: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j722s_evm-fs: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

    "150","9.80","39.50","30.40","43.10","36.10","34.70"





 
 
 



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am68_sk-fs: throughput (KBytes/Sec)","am69_sk-fs: throughput (KBytes/Sec)","j7200-evm: throughput (KBytes/Sec)","j721e-idk-gw: throughput (KBytes/Sec)","j721s2-evm: throughput (KBytes/Sec)","j722s_evm-fs: throughput (KBytes/Sec)","j742s2_evm-fs: throughput (KBytes/Sec)","j784s4-evm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","39577.26","37756.93","35465.22","41165.48","38415.36","22804.82","39581.01","38581.59"
    "aes-128-cbc","16","772.60","573.48","702.10","788.68","753.57","404.47","765.72","746.83"
    "aes-128-cbc","16384","178317.99","172632.75","180251.31","185810.94","174882.82","84251.99","178094.08","175789.40"
    "aes-128-cbc","256","11705.86","10046.81","10512.64","11962.28","11557.97","6732.03","11368.45","11237.38"
    "aes-128-cbc","64","3049.71","2549.82","2804.54","3150.21","3021.44","1793.81","3035.09","2973.42"
    "aes-128-cbc","8192","143469.23","139100.16","141489.49","150238.55","142087.51","70724.27","143338.15","141552.30"
    "aes-128-ecb","1024","39976.96","37954.56","35474.09","41910.95","40124.07","23211.69","39631.87","38865.58"
    "aes-128-ecb","16","775.07","696.48","707.04","800.92","757.19","411.97","774.06","717.35"
    "aes-128-ecb","16384","181103.27","175712.94","182419.46","190644.22","178438.14","86491.14","179284.65","164342.44"
    "aes-128-ecb","256","11874.99","11585.28","10587.14","12223.91","11787.86","6775.47","11720.28","9956.69"
    "aes-128-ecb","64","3093.08","2994.99","2798.23","3172.44","3045.08","1817.64","3044.48","3010.13"
    "aes-128-ecb","8192","144902.83","139586.22","142262.27","153534.46","141806.25","73042.60","143471.96","137423.53"
    "aes-192-cbc","1024","39500.12","37800.96","35468.29","40907.09","39056.73","22249.13","38611.29","34795.86"
    "aes-192-cbc","16","772.37","750.47","698.71","792.86","764.69","407.21","764.43","762.01"
    "aes-192-cbc","16384","168585.90","164446.21","177924.78","173151.57","168312.83","76371.29","168902.66","161251.33"
    "aes-192-cbc","256","11590.57","11127.21","10451.11","11908.86","11484.07","6631.68","11379.29","11413.59"
    "aes-192-cbc","64","3076.33","2988.76","2796.86","3156.61","2916.35","1794.07","3002.73","3000.77"
    "aes-192-cbc","8192","138941.78","134938.62","140004.01","143704.06","137958.74","65252.01","136645.29","134632.79"
    "aes-192-ecb","1024","39972.86","37972.31","35485.70","41554.26","39469.40","22659.75","39291.90","37597.53"
    "aes-192-ecb","16","779.47","755.48","704.32","805.65","770.30","414.37","771.95","589.23"
    "aes-192-ecb","16384","176903.51","168793.43","178388.99","179011.58","174347.61","78894.42","174369.45","169656.32"
    "aes-192-ecb","256","11844.78","11276.20","10526.04","12088.23","10757.80","6784.51","11521.11","9258.84"
    "aes-192-ecb","64","3112.28","2810.65","2805.01","3204.61","3052.27","1830.91","3057.47","2331.63"
    "aes-192-ecb","8192","142819.33","136249.34","140842.33","146164.39","140227.93","67360.09","140323.50","137756.67"
    "aes-256-cbc","1024","39119.53","37200.90","35290.11","40916.65","37615.27","21748.74","38695.25","37766.83"
    "aes-256-cbc","16","770.37","727.41","699.24","801.46","767.78","407.19","756.48","753.77"
    "aes-256-cbc","16384","158455.13","153763.84","171327.49","162338.13","157646.85","67922.60","156155.90","148695.72"
    "aes-256-cbc","256","11556.27","11194.37","10434.30","11997.70","11439.62","6609.15","11378.86","11077.63"
    "aes-256-cbc","64","3087.25","2989.67","2785.77","3172.59","3048.11","1800.04","3028.86","2973.16"
    "aes-256-cbc","8192","130798.93","126623.74","135342.76","134766.59","130192.73","59594.07","130476.71","127186.26"
    "aes-256-ecb","1024","39460.18","32424.28","35421.87","41271.98","39105.88","22302.38","39045.46","35389.44"
    "aes-256-ecb","16","776.01","584.14","708.60","803.89","725.49","412.45","768.43","754.99"
    "aes-256-ecb","16384","163528.70","149340.16","174500.52","165178.03","161562.62","70341.97","163747.16","149269.16"
    "aes-256-ecb","256","11591.34","10910.89","10516.99","12002.56","11530.50","6747.73","11381.08","11005.44"
    "aes-256-ecb","64","3059.75","2329.45","2820.63","3216.83","3064.47","1815.08","3049.39","2996.50"
    "aes-256-ecb","8192","133428.57","117099.18","139168.43","139304.96","132808.70","60347.73","134640.98","116746.92"
    "des3","1024","34775.38","29966.68","34153.47","35568.30","34453.85","","34291.03","33467.39"
    "des3","16","774.52","683.67","700.10","804.05","766.89","","765.24","755.99"
    "des3","16384","94486.53","92673.37","115763.88","94481.07","92400.30","","93891.24","93956.78"
    "des3","256","10990.76","10747.65","10205.01","11494.06","10697.73","","10945.54","8846.08"
    "des3","64","3045.82","2968.28","2778.37","3172.59","2922.18","","2992.98","2711.06"
    "des3","8192","83099.65","79981.23","97424.73","85756.59","83785.05","","84224.68","83970.73"
    "sha1","1024","52462.93","51189.42","52908.37","51969.71","47213.91","","52443.82","52165.63"
    "sha1","16","884.75","846.89","876.89","874.77","867.90","","840.58","836.29"
    "sha1","16384","445601.11","432504.83","444164.78","443498.50","441477.80","","435404.80","432062.46"
    "sha1","256","13987.16","13332.99","13901.23","13852.25","13667.24","","13364.48","13501.44"
    "sha1","64","3515.73","3375.91","3485.82","3459.88","3489.62","","3397.78","3337.34"
    "sha1","8192","299728.90","287323.48","294248.45","292659.20","298068.65","","287036.76","290870.61"
    "sha256","1024","52018.86","50610.52","52348.59","51968.68","52416.51","34361.34","52448.60","50779.14"
    "sha256","16","864.78","819.88","854.02","884.79","824.20","574.03","855.64","825.23"
    "sha256","16384","440964.44","423400.79","429419.18","433984.85","392391.34","283508.74","429806.93","425798.31"
    "sha256","256","13750.53","13118.21","13437.44","13745.07","13469.53","8928.17","13477.55","13021.44"
    "sha256","64","3466.11","3279.94","3386.50","3483.33","3008.79","2262.06","3361.43","3284.42"
    "sha256","8192","293475.67","281758.38","286487.89","290758.66","287135.06","189852.33","285496.66","284778.50"
    "sha512","1024","42193.24","40928.26","41565.53","42538.33","41812.99","24174.59","41947.82","40819.71"
    "sha512","16","843.32","824.97","839.31","853.61","818.50","546.33","840.05","820.78"
    "sha512","16384","143458.30","142770.18","143021.40","144457.73","144610.65","67403.78","144288.43","143846.06"
    "sha512","256","13069.14","12430.76","12484.35","12950.36","12371.80","7826.69","12772.10","12309.42"
    "sha512","64","3406.87","3332.01","3363.20","3425.66","3274.11","2189.23","3391.25","3300.67"
    "sha512","8192","123106.65","121714.01","122576.90","123726.51","123442.52","59984.55","123480.75","122893.65"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am68_sk-fs: CPU Load","am69_sk-fs: CPU Load","j7200-evm: CPU Load","j721e-idk-gw: CPU Load","j721s2-evm: CPU Load","j722s_evm-fs: CPU Load","j742s2_evm-fs: CPU Load","j784s4-evm: CPU Load"

    "aes-128-cbc","32.00","32.00","32.00","34.00","31.00","30.00","33.00","33.00"
    "aes-128-ecb","33.00","33.00","33.00","34.00","32.00","32.00","33.00","33.00"
    "aes-192-cbc","32.00","32.00","33.00","33.00","32.00","27.00","33.00","33.00"
    "aes-192-ecb","33.00","33.00","33.00","34.00","32.00","31.00","32.00","33.00"
    "aes-256-cbc","32.00","32.00","33.00","33.00","31.00","27.00","32.00","32.00"
    "aes-256-ecb","33.00","33.00","32.00","33.00","32.00","30.00","32.00","33.00"
    "des3","29.00","29.00","30.00","30.00","29.00","","29.00","30.00"
    "sha1","97.00","97.00","97.00","97.00","95.00","","97.00","97.00"
    "sha256","97.00","97.00","97.00","97.00","95.00","96.00","97.00","97.00"
    "sha512","97.00","97.00","96.00","97.00","96.00","96.00","98.00","97.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

 




IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","j721e-idk-gw: Throughput (Mbps)","j721e-idk-gw: Packets/Sec","j721e-idk-gw: CPU Load"

    "aes128","290.70","25.00","96.51"
    "aes192","698.70","62.00","59.00"
    "aes256","725.60","64.00","97.84"

 
 

 





