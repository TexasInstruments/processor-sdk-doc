
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

    "af_unix_sock_stream_latency (microsec)","19.64","27.49","19.95","19.13","19.92","29.64","20.24","20.31"
    "af_unix_socket_stream_bandwidth (MBs)","2017.35","2989.67","1675.68","1973.31","2073.44","1046.24","3064.03","1845.20"
    "bw_file_rd-io-1mb (MB/s)","3306.65","3849.68","3679.18","3459.58","3610.11","1344.09","4403.73","3997.82"
    "bw_file_rd-o2c-1mb (MB/s)","1427.04","1413.23","1184.63","1729.21","1435.49","724.64","2288.77","2148.02"
    "bw_mem-bcopy-16mb (MB/s)","3387.32","2674.24","2366.86","2810.96","3792.82","1720.06","3379.45","3136.64"
    "bw_mem-bcopy-1mb (MB/s)","4298.26","9689.92","3265.01","5206.40","5083.79","1858.42","9554.75","9389.67"
    "bw_mem-bcopy-2mb (MB/s)","3592.60","3949.02","2462.62","3854.92","3941.66","1602.56","4858.00","5042.32"
    "bw_mem-bcopy-4mb (MB/s)","3424.07","3206.16","2343.29","3860.26","3864.11","1662.28","4185.56","3675.12"
    "bw_mem-bcopy-8mb (MB/s)","3404.26","2833.86","2341.58","3050.52","3786.09","1694.02","3508.77","3264.42"
    "bw_mem-bzero-16mb (MB/s)","10484.93","10841.94","2335.43","9621.17","10904.75","7156.70","10381.18","10904.75"
    "bw_mem-bzero-1mb (MB/s)","8434.54 (min 4298.26, max 12570.82)","11715.33 (min 9689.92, max 13740.73)","3991.46 (min 3265.01, max 4717.91)","8828.50 (min 5206.40, max 12450.59)","9114.29 (min 5083.79, max 13144.79)","4495.55 (min 1858.42, max 7132.67)","11581.95 (min 9554.75, max 13609.15)","11563.96 (min 9389.67, max 13738.25)"
    "bw_mem-bzero-2mb (MB/s)","7436.30 (min 3592.60, max 11279.99)","8743.30 (min 3949.02, max 13537.58)","2678.75 (min 2462.62, max 2894.88)","8038.17 (min 3854.92, max 12221.42)","7773.90 (min 3941.66, max 11606.14)","4366.98 (min 1602.56, max 7131.40)","9046.78 (min 4858.00, max 13235.56)","9352.01 (min 5042.32, max 13661.69)"
    "bw_mem-bzero-4mb (MB/s)","7034.02 (min 3424.07, max 10643.96)","7738.05 (min 3206.16, max 12269.94)","2400.71 (min 2343.29, max 2458.13)","7902.38 (min 3860.26, max 11944.49)","7425.56 (min 3864.11, max 10987.00)","4403.85 (min 1662.28, max 7145.41)","7930.07 (min 4185.56, max 11674.57)","7979.18 (min 3675.12, max 12283.24)"
    "bw_mem-bzero-8mb (MB/s)","6967.02 (min 3404.26, max 10529.78)","7034.91 (min 2833.86, max 11235.96)","2347.96 (min 2341.58, max 2354.33)","7378.56 (min 3050.52, max 11706.60)","7366.88 (min 3786.09, max 10947.66)","4414.62 (min 1694.02, max 7135.21)","7059.43 (min 3508.77, max 10610.08)","7285.92 (min 3264.42, max 11307.42)"
    "bw_mem-cp-16mb (MB/s)","2120.05","2133.62","985.22","1556.72","2144.77","846.43","2108.59","2295.55"
    "bw_mem-cp-1mb (MB/s)","7391.56 (min 2376.17, max 12406.95)","8290.64 (min 2865.33, max 13715.94)","3076.29 (min 1266.28, max 4886.30)","7068.65 (min 1704.87, max 12432.43)","7789.56 (min 2491.99, max 13087.13)","4154.77 (min 835.70, max 7473.84)","8523.75 (min 3560.72, max 13486.78)","8544.89 (min 3366.41, max 13723.37)"
    "bw_mem-cp-2mb (MB/s)","6688.88 (min 2129.17, max 11248.59)","8062.39 (min 2453.99, max 13670.79)","1968.27 (min 1010.95, max 2925.58)","6818.14 (min 1517.22, max 12119.05)","6932.63 (min 2171.55, max 11693.70)","4052.86 (min 832.99, max 7272.73)","7802.75 (min 2350.97, max 13254.52)","8182.91 (min 2725.26, max 13640.55)"
    "bw_mem-cp-4mb (MB/s)","6383.93 (min 2091.69, max 10676.16)","7590.18 (min 2504.30, max 12676.06)","1725.21 (min 978.23, max 2472.19)","6747.70 (min 1541.72, max 11953.68)","5913.58 (min 2153.63, max 9673.52)","3993.40 (min 779.58, max 7207.21)","7088.27 (min 2634.61, max 11541.93)","7478.00 (min 2692.70, max 12263.30)"
    "bw_mem-cp-8mb (MB/s)","6338.22 (min 2106.65, max 10569.78)","6711.63 (min 2187.29, max 11235.96)","1662.09 (min 975.37, max 2348.80)","6602.37 (min 1498.13, max 11706.60)","6518.73 (min 2158.66, max 10878.80)","4042.01 (min 892.36, max 7191.66)","6372.16 (min 2144.77, max 10599.54)","6820.00 (min 2358.49, max 11281.51)"
    "bw_mem-fcp-16mb (MB/s)","3371.62","2613.95","2414.37","2788.91","3774.92","1614.53","3376.24","3075.74"
    "bw_mem-fcp-1mb (MB/s)","8266.17 (min 3961.52, max 12570.82)","10212.37 (min 6684.00, max 13740.73)","4032.97 (min 3348.02, max 4717.91)","8232.60 (min 4014.60, max 12450.59)","8607.44 (min 4070.08, max 13144.79)","4369.05 (min 1605.42, max 7132.67)","10046.52 (min 6483.88, max 13609.15)","10117.12 (min 6495.99, max 13738.25)"
    "bw_mem-fcp-2mb (MB/s)","7383.17 (min 3486.35, max 11279.99)","8487.01 (min 3436.43, max 13537.58)","2694.55 (min 2494.21, max 2894.88)","8051.43 (min 3881.44, max 12221.42)","7728.74 (min 3851.34, max 11606.14)","4304.58 (min 1477.76, max 7131.40)","8700.39 (min 4165.22, max 13235.56)","8806.35 (min 3951.01, max 13661.69)"
    "bw_mem-fcp-4mb (MB/s)","7036.07 (min 3428.18, max 10643.96)","7655.31 (min 3040.67, max 12269.94)","2430.51 (min 2402.88, max 2458.13)","7878.10 (min 3811.70, max 11944.49)","7412.89 (min 3838.77, max 10987.00)","4359.49 (min 1573.56, max 7145.41)","7872.91 (min 4071.25, max 11674.57)","7915.62 (min 3547.99, max 12283.24)"
    "bw_mem-fcp-8mb (MB/s)","6948.39 (min 3367.00, max 10529.78)","7003.26 (min 2770.56, max 11235.96)","2382.17 (min 2354.33, max 2410.00)","7383.52 (min 3060.44, max 11706.60)","7327.11 (min 3706.56, max 10947.66)","4351.31 (min 1567.40, max 7135.21)","7005.48 (min 3400.88, max 10610.08)","7239.13 (min 3170.83, max 11307.42)"
    "bw_mem-frd-16mb (MB/s)","4167.75","3135.41","6308.32","4791.85","4680.42","1754.39","4189.03","3496.89"
    "bw_mem-frd-1mb (MB/s)","4304.54 (min 3961.52, max 4647.56)","7161.64 (min 6684.00, max 7639.28)","4563.07 (min 3348.02, max 5778.12)","4736.97 (min 4014.60, max 5459.34)","4666.98 (min 4070.08, max 5263.88)","1714.97 (min 1605.42, max 1824.51)","7031.87 (min 6483.88, max 7579.86)","7124.67 (min 6495.99, max 7753.34)"
    "bw_mem-frd-2mb (MB/s)","4052.20 (min 3486.35, max 4618.05)","3659.62 (min 3436.43, max 3882.81)","4461.39 (min 2494.21, max 6428.57)","4829.85 (min 3881.44, max 5778.26)","4540.05 (min 3851.34, max 5228.76)","1544.81 (min 1477.76, max 1611.86)","4602.97 (min 4165.22, max 5040.71)","3992.38 (min 3951.01, max 4033.74)"
    "bw_mem-frd-4mb (MB/s)","3824.17 (min 3428.18, max 4220.15)","3307.33 (min 3040.67, max 3573.98)","4354.15 (min 2402.88, max 6305.42)","4739.72 (min 3811.70, max 5667.73)","4288.12 (min 3838.77, max 4737.47)","1584.87 (min 1573.56, max 1596.17)","4512.63 (min 4071.25, max 4954.00)","3737.03 (min 3547.99, max 3926.06)"
    "bw_mem-frd-8mb (MB/s)","3769.37 (min 3367.00, max 4171.74)","3133.79 (min 2770.56, max 3497.01)","4362.07 (min 2410.00, max 6314.13)","4212.54 (min 3060.44, max 5364.63)","4192.81 (min 3706.56, max 4679.05)","1607.68 (min 1567.40, max 1647.96)","4151.80 (min 3400.88, max 4902.71)","3531.89 (min 3170.83, max 3892.94)"
    "bw_mem-fwr-16mb (MB/s)","10552.35","10834.60","2343.64","9628.40","10875.11","7168.46","10398.05","10895.47"
    "bw_mem-fwr-1mb (MB/s)","8527.26 (min 4647.56, max 12406.95)","10677.61 (min 7639.28, max 13715.94)","5332.21 (min 4886.30, max 5778.12)","8945.89 (min 5459.34, max 12432.43)","9175.51 (min 5263.88, max 13087.13)","4649.18 (min 1824.51, max 7473.84)","10533.32 (min 7579.86, max 13486.78)","10738.36 (min 7753.34, max 13723.37)"
    "bw_mem-fwr-2mb (MB/s)","7933.32 (min 4618.05, max 11248.59)","8776.80 (min 3882.81, max 13670.79)","4677.08 (min 2925.58, max 6428.57)","8948.66 (min 5778.26, max 12119.05)","8461.23 (min 5228.76, max 11693.70)","4442.30 (min 1611.86, max 7272.73)","9147.62 (min 5040.71, max 13254.52)","8837.15 (min 4033.74, max 13640.55)"
    "bw_mem-fwr-4mb (MB/s)","7448.16 (min 4220.15, max 10676.16)","8125.02 (min 3573.98, max 12676.06)","4388.81 (min 2472.19, max 6305.42)","8810.71 (min 5667.73, max 11953.68)","7205.50 (min 4737.47, max 9673.52)","4401.69 (min 1596.17, max 7207.21)","8247.97 (min 4954.00, max 11541.93)","8094.68 (min 3926.06, max 12263.30)"
    "bw_mem-fwr-8mb (MB/s)","7370.76 (min 4171.74, max 10569.78)","7366.49 (min 3497.01, max 11235.96)","4331.47 (min 2348.80, max 6314.13)","8535.62 (min 5364.63, max 11706.60)","7778.93 (min 4679.05, max 10878.80)","4419.81 (min 1647.96, max 7191.66)","7751.13 (min 4902.71, max 10599.54)","7587.23 (min 3892.94, max 11281.51)"
    "bw_mem-rd-16mb (MB/s)","4881.03","3782.06","6572.64","5102.04","5459.82","1795.94","4975.90","4083.72"
    "bw_mem-rd-1mb (MB/s)","5127.19 (min 3495.15, max 6759.23)","16161.82 (min 15085.42, max 17238.22)","6830.78 (min 3785.01, max 9876.54)","5188.82 (min 3069.25, max 7308.38)","5556.31 (min 3245.64, max 7866.98)","1795.51 (min 1556.02, max 2035.00)","16080.86 (min 15084.97, max 17076.75)","14583.30 (min 13793.10, max 15373.49)"
    "bw_mem-rd-2mb (MB/s)","4185.42 (min 2858.16, max 5512.68)","3958.12 (min 2618.23, max 5298.01)","4016.21 (min 982.32, max 7050.09)","4298.71 (min 2090.23, max 6507.18)","4526.04 (min 2934.70, max 6117.38)","1659.27 (min 1533.45, max 1785.08)","5152.73 (min 3279.29, max 7026.17)","4528.69 (min 3247.92, max 5809.45)"
    "bw_mem-rd-4mb (MB/s)","3676.82 (min 2371.42, max 4982.21)","3766.31 (min 3381.81, max 4150.81)","3715.74 (min 788.18, max 6643.29)","4057.21 (min 1825.10, max 6289.31)","3971.65 (min 2403.12, max 5540.17)","1663.95 (min 1570.68, max 1757.21)","4434.90 (min 2967.91, max 5901.88)","4130.17 (min 3559.99, max 4700.35)"
    "bw_mem-rd-8mb (MB/s)","3559.61 (min 2237.45, max 4881.77)","3689.97 (min 3249.83, max 4130.10)","3660.90 (min 747.17, max 6574.62)","3879.03 (min 1944.11, max 5813.95)","3849.71 (min 2286.69, max 5412.72)","1721.30 (min 1661.65, max 1780.94)","4343.77 (min 2955.85, max 5731.69)","4079.07 (min 3488.88, max 4669.26)"
    "bw_mem-rdwr-16mb (MB/s)","2119.21","2304.15","752.27","1795.53","2257.34","1733.67","2118.08","2570.69"
    "bw_mem-rdwr-1mb (MB/s)","2977.00 (min 2376.17, max 3577.82)","6058.10 (min 2865.33, max 9250.86)","3148.41 (min 1266.28, max 5030.54)","3608.78 (min 1704.87, max 5512.68)","3727.16 (min 2491.99, max 4962.32)","1203.60 (min 835.70, max 1571.50)","6574.14 (min 3560.72, max 9587.55)","5683.92 (min 3366.41, max 8001.42)"
    "bw_mem-rdwr-2mb (MB/s)","2406.87 (min 2129.17, max 2684.56)","3163.48 (min 2453.99, max 3872.97)","996.72 (min 982.48, max 1010.95)","1900.38 (min 1517.22, max 2283.54)","2517.67 (min 2171.55, max 2863.79)","1124.09 (min 832.99, max 1415.18)","3221.17 (min 2350.97, max 4091.37)","3283.02 (min 2725.26, max 3840.78)"
    "bw_mem-rdwr-4mb (MB/s)","2203.25 (min 2091.69, max 2314.81)","2691.78 (min 2504.30, max 2879.25)","888.40 (min 798.56, max 978.23)","1993.54 (min 1541.72, max 2445.36)","2295.03 (min 2153.63, max 2436.42)","1197.71 (min 779.58, max 1615.84)","2655.10 (min 2634.61, max 2675.59)","2972.90 (min 2692.70, max 3253.09)"
    "bw_mem-rdwr-8mb (MB/s)","2127.73 (min 2106.65, max 2148.80)","2471.30 (min 2187.29, max 2755.30)","865.40 (min 755.43, max 975.37)","1951.71 (min 1498.13, max 2405.29)","2232.07 (min 2158.66, max 2305.48)","1259.93 (min 892.36, max 1627.50)","2425.34 (min 2144.77, max 2705.90)","2740.22 (min 2358.49, max 3121.95)"
    "bw_mem-wr-16mb (MB/s)","2216.68","2674.69","743.01","1817.56","2249.72","1661.82","2206.59","2836.88"
    "bw_mem-wr-1mb (MB/s)","3536.49 (min 3495.15, max 3577.82)","13244.54 (min 9250.86, max 17238.22)","4407.78 (min 3785.01, max 5030.54)","4290.97 (min 3069.25, max 5512.68)","4103.98 (min 3245.64, max 4962.32)","1563.76 (min 1556.02, max 1571.50)","13332.15 (min 9587.55, max 17076.75)","10897.26 (min 8001.42, max 13793.10)"
    "bw_mem-wr-2mb (MB/s)","2771.36 (min 2684.56, max 2858.16)","3245.60 (min 2618.23, max 3872.97)","982.40 (min 982.32, max 982.48)","2186.89 (min 2090.23, max 2283.54)","2899.25 (min 2863.79, max 2934.70)","1474.32 (min 1415.18, max 1533.45)","3685.33 (min 3279.29, max 4091.37)","3544.35 (min 3247.92, max 3840.78)"
    "bw_mem-wr-4mb (MB/s)","2343.12 (min 2314.81, max 2371.42)","3130.53 (min 2879.25, max 3381.81)","793.37 (min 788.18, max 798.56)","2135.23 (min 1825.10, max 2445.36)","2419.77 (min 2403.12, max 2436.42)","1593.26 (min 1570.68, max 1615.84)","2821.75 (min 2675.59, max 2967.91)","3406.54 (min 3253.09, max 3559.99)"
    "bw_mem-wr-8mb (MB/s)","2193.13 (min 2148.80, max 2237.45)","3002.57 (min 2755.30, max 3249.83)","751.30 (min 747.17, max 755.43)","2174.70 (min 1944.11, max 2405.29)","2296.09 (min 2286.69, max 2305.48)","1644.58 (min 1627.50, max 1661.65)","2830.88 (min 2705.90, max 2955.85)","3305.42 (min 3121.95, max 3488.88)"
    "bw_mmap_rd-mo-1mb (MB/s)","8484.85","12920.84","12035.01","8775.07","8901.55","1994.56","12913.32","12916.91"
    "bw_mmap_rd-o2c-1mb (MB/s)","1321.00","2563.16","1235.66","1612.61","1337.66","731.53","2790.70","2429.71"
    "bw_pipe (MB/s)","1007.95","787.24","776.73","936.71","1022.19","764.41","1026.60","874.84"
    "bw_unix (MB/s)","2017.35","2989.67","1675.68","1973.31","2073.44","1046.24","3064.03","1845.20"
    "lat_connect (us)","37.08","37.41","37.08","36.57","37.45","57.91","37.42","37.55"
    "lat_ctx-2-128k (us)","4.98","7.98","5.11","4.98","5.09","7.76","5.13","8.02"
    "lat_ctx-2-256k (us)","4.32","6.93","4.36","4.24","4.52","7.06","4.47","7.25"
    "lat_ctx-4-128k (us)","4.94","6.57","5.09","5.02","4.94","7.83","5.06","7.65"
    "lat_ctx-4-256k (us)","3.95","6.71","3.94","3.99","4.48","6.64","3.68","5.14"
    "lat_fs-0k (num_files)","403.00","391.00","406.00","414.00","408.00","215.00","403.00","397.00"
    "lat_fs-10k (num_files)","154.00","178.00","141.00","175.00","175.00","112.00","193.00","177.00"
    "lat_fs-1k (num_files)","233.00","255.00","213.00","240.00","237.00","163.00","238.00","242.00"
    "lat_fs-4k (num_files)","246.00","252.00","251.00","264.00","253.00","145.00","266.00","264.00"
    "lat_mem_rd-stride128-sz1000k (ns)","13.71","5.65","12.25","12.47","11.90","33.46","6.37","5.71"
    "lat_mem_rd-stride128-sz125k (ns)","5.57","5.65","5.57","5.57","5.57","5.57","5.65","5.65"
    "lat_mem_rd-stride128-sz250k (ns)","5.57","5.65","5.57","5.57","5.57","5.83","5.65","5.65"
    "lat_mem_rd-stride128-sz31k (ns)","3.32","3.43","4.67","3.34","4.67","2.16","4.77","4.74"
    "lat_mem_rd-stride128-sz50 (ns)","2.00","2.00","2.00","2.00","2.00","2.15","2.00","2.00"
    "lat_mem_rd-stride128-sz500k (ns)","9.09","5.65","5.58","5.57","6.16","11.62","5.65","5.65"
    "lat_mem_rd-stride128-sz62k (ns)","5.57","5.21","5.57","5.12","5.12","4.78","4.76","4.74"
    "lat_mmap-1m (us)","29.00","35.00","36.00","33.00","35.00","50.00","29.00","29.00"
    "lat_ops-double-add (ns)","1.96","1.96","1.96","1.96","1.96","2.86","1.96","1.96"
    "lat_ops-double-div (ns)","9.01","9.01","9.02","9.01","9.01","15.74","9.01","9.01"
    "lat_ops-double-mul (ns)","2.00","2.00","2.00","2.00","2.00","2.86","2.00","2.00"
    "lat_ops-float-add (ns)","1.96","1.96","1.96","1.96","1.96","2.86","1.96","1.96"
    "lat_ops-float-div (ns)","5.50","5.51","5.51","5.51","5.51","9.30","5.51","5.50"
    "lat_ops-float-mul (ns)","2.00","2.00","2.00","2.00","2.00","2.86","2.00","2.00"
    "lat_ops-int-add (ns)","0.50","0.50","0.50","0.50","0.50","0.72","0.50","0.50"
    "lat_ops-int-bit (ns)","0.33","0.33","0.33","0.33","0.33","0.48","0.33","0.33"
    "lat_ops-int-div (ns)","4.00","4.00","4.01","4.01","4.00","4.30","4.00","4.00"
    "lat_ops-int-mod (ns)","4.67","4.67","4.67","4.67","4.68","4.53","4.67","4.67"
    "lat_ops-int-mul (ns)","1.52","1.52","1.52","1.52","1.52","3.07","1.52","1.52"
    "lat_ops-int64-add (ns)","0.50","0.50","0.50","0.50","0.50","0.72","0.50","0.50"
    "lat_ops-int64-bit (ns)","0.33","0.33","0.33","0.33","0.33","0.48","0.33","0.33"
    "lat_ops-int64-div (ns)","3.00","3.00","3.00","3.00","3.00","6.79","3.00","3.00"
    "lat_ops-int64-mod (ns)","5.67","5.67","5.67","5.67","5.67","5.26","5.67","5.67"
    "lat_ops-int64-mul (ns)","2.52","2.52","2.52","2.52","2.52","3.65","2.52","2.52"
    "lat_pagefault (us)","0.25","0.24","0.25","0.23","0.25","0.54","0.23","0.24"
    "lat_pipe (us)","12.88","16.35","14.19","14.08","14.80","25.21","15.99","19.13"
    "lat_proc-exec (us)","408.77","398.67","404.23","359.13","421.07","711.25","321.35","401.93"
    "lat_proc-fork (us)","371.67","387.60","380.15","325.41","361.53","603.00","300.32","377.67"
    "lat_proc-proccall (us)","0.00","0.00","0.00","0.00","0.00","0.01","0.00","0.00"
    "lat_select (us)","11.45","11.46","13.28","13.29","13.30","33.99","11.45","11.43"
    "lat_sem (us)","1.62","2.33","2.13","1.89","1.82","3.43","1.72","2.44"
    "lat_sig-catch (us)","2.98","3.02","3.02","2.99","3.04","5.57","3.06","3.10"
    "lat_sig-install (us)","0.54","0.54","0.55","0.53","0.53","0.68","0.54","0.55"
    "lat_sig-prot (us)","0.73","0.67","0.58","0.73","0.72","1.57","0.69","0.73"
    "lat_syscall-fstat (us)","0.94","0.95","0.96","0.92","0.97","1.97","0.94","1.00"
    "lat_syscall-null (us)","0.39","0.38","0.39","0.40","0.39","0.46","0.39","0.39"
    "lat_syscall-open (us)","153.54","172.65","153.94","142.68","181.10","180.19","115.08","205.22"
    "lat_syscall-read (us)","0.51","0.51","0.53","0.56","0.51","0.79","0.51","0.50"
    "lat_syscall-stat (us)","2.34","2.36","2.32","2.35","2.30","4.76","2.31","2.29"
    "lat_syscall-write (us)","0.47","0.48","0.49","0.47","0.49","0.75","0.49","0.49"
    "lat_tcp (us)","0.83","0.83","0.82","0.83","0.84","0.91","0.81","0.82"
    "lat_unix (us)","19.64","27.49","19.95","19.13","19.92","29.64","20.24","20.31"
    "latency_for_0.50_mb_block_size (nanosec)","9.09","5.65","5.58","5.57","6.16","11.62","5.65","5.65"
    "latency_for_1.00_mb_block_size (nanosec)","6.86 (min 0.00, max 13.71)","2.82 (min 0.00, max 5.65)","6.12 (min 0.00, max 12.25)","6.24 (min 0.00, max 12.47)","5.95 (min 0.00, max 11.90)","16.73 (min 0.00, max 33.46)","3.18 (min 0.00, max 6.37)","2.85 (min 0.00, max 5.71)"
    "pipe_bandwidth (MBs)","1007.95","787.24","776.73","936.71","1022.19","764.41","1026.60","874.84"
    "pipe_latency (microsec)","12.88","16.35","14.19","14.08","14.80","25.21","15.99","19.13"
    "procedure_call (microsec)","0.00","0.00","0.00","0.00","0.00","0.01","0.00","0.00"
    "select_on_200_tcp_fds (microsec)","11.45","11.46","13.28","13.29","13.30","33.99","11.45","11.43"
    "semaphore_latency (microsec)","1.62","2.33","2.13","1.89","1.82","3.43","1.72","2.44"
    "signal_handler_latency (microsec)","0.54","0.54","0.55","0.53","0.53","0.68","0.54","0.55"
    "signal_handler_overhead (microsec)","2.98","3.02","3.02","2.99","3.04","5.57","3.06","3.10"
    "tcp_ip_connection_cost_to_localhost (microsec)","37.08","37.41","37.08","36.57","37.45","57.91","37.42","37.55"
    "tcp_latency_using_localhost (microsec)","0.83","0.83","0.82","0.83","0.84","0.91","0.81","0.82"




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
    "dhrystone_per_mhz (DMIPS/MHz)","5.70","5.70","5.70","5.70","5.70","2.90","5.20","5.70"
    "dhrystone_per_second (DhrystoneP)","20000000.00","20000000.00","20000000.00","20000000.00","20000000.00","7142857.00","18181818.00","20000000.00"




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

    "linpack (Kflops)","2638997.00","2435852.00","2568900.00","2466475.00","2444523.00","578294.00","2519877.00","2350793.00"




NBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
NBench which stands for Native Benchmark is used to measure macro benchmarks
for commonly used operations such as sorting and analysis algorithms.
More information about NBench at
https://en.wikipedia.org/wiki/NBench and
https://nbench.io/articles/index.html

.. csv-table:: NBench Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "assignment (Iterations)","31.39","31.74","31.97","31.91","31.98","14.47","31.89","31.87"
    "fourier (Iterations)","60509.00","58786.00","59941.00","65647.00","59869.00","22830.00","63922.00","64039.00"
    "fp_emulation (Iterations)","387.97","388.02","387.99","387.99","387.90","215.64","387.97","387.91"
    "huffman (Iterations)","2489.60","2484.50","2489.90","2485.50","2482.80","1184.40","2485.30","2489.30"
    "idea (Iterations)","7996.10","7996.30","7996.50","7996.40","7989.50","3444.80","7995.70","7995.70"
    "lu_decomposition (Iterations)","1358.90","1366.40","1377.60","1375.40","1384.60","530.03","1366.10","1377.50"
    "neural_net (Iterations)","29.00","29.01","28.46","28.99","28.99","8.65","28.99","28.50"
    "numeric_sort (Iterations)","879.76","877.41","870.84","883.51","874.67","629.07","867.43","867.04"
    "string_sort (Iterations)","361.81","353.98","353.93","353.81","346.98","163.92","361.73","362.51"




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

    "add (MB/s)","6354.40","5703.20","5433.70","5288.80","6231.80","2449.90","6394.50","5858.10"
    "copy (MB/s)","6936.30","5543.80","4771.00","5536.90","6986.00","3488.40","7654.70","5362.10"
    "scale (MB/s)","7065.90","5518.40","4829.20","5406.00","7108.00","3234.80","7784.80","5349.40"
    "triad (MB/s)","6361.10","5692.60","5438.80","5270.00","6236.70","2236.00","6382.80","5854.80"




CoreMarkPro
^^^^^^^^^^^^^^^^^^^^^^^^^^^
CoreMark®-Pro is a comprehensive, advanced processor benchmark that works with
and enhances the market-proven industry-standard EEMBC CoreMark® benchmark.
While CoreMark stresses the CPU pipeline, CoreMark-Pro tests the entire processor,
adding comprehensive support for multicore technology, a combination of integer
and floating-point workloads, and data sets for utilizing larger memory subsystems.


.. csv-table:: CoreMarkPro Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","81.97","81.97","82.64","82.64","81.30","42.02","81.97","82.64"
    "core (workloads/)","0.78","0.78","0.78","0.78","0.78","0.30","0.77","0.78"
    "coremark-pro ()","2488.15","2516.12","2493.72","2499.57","2476.08","906.76","2513.41","2503.18"
    "linear_alg-mid-100x100-sp (workloads/)","81.57","80.65","80.65","80.39","80.52","14.67","80.65","80.00"
    "loops-all-mid-10k-sp (workloads/)","2.46","2.46","2.43","2.47","2.47","0.71","2.46","2.46"
    "nnet_test (workloads/)","3.65","3.60","3.86","3.66","3.65","1.08","3.65","3.60"
    "parser-125k (workloads/)","11.11","10.87","11.11","11.24","11.11","8.77","10.87","10.75"
    "radix2-big-64k (workloads/)","267.38","305.06","261.99","271.00","256.28","53.39","301.84","294.46"
    "sha-test (workloads/)","156.25","158.73","156.25","158.73","158.73","81.30","158.73","158.73"
    "zip-test (workloads/)","47.62","47.62","47.62","47.62","47.62","21.74","47.62","47.62"




.. csv-table:: CoreMarkProTwoCore Benchmarks
    :header: "Benchmarks","am68_sk-fs: perf","am69_sk-fs: perf","j7200-evm: perf","j721e-idk-gw: perf","j721s2-evm: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","163.93","163.93","163.93","163.93","163.93","83.33","166.67","163.93"
    "core (workloads/)","1.55","1.56","1.56","1.55","1.55","0.60","1.56","1.56"
    "coremark-pro ()","4461.18","4793.56","4338.81","4475.35","4433.83","1652.38","4765.49","4932.99"
    "linear_alg-mid-100x100-sp (workloads/)","159.24","159.24","163.40","158.23","158.73","29.38","161.29","162.34"
    "loops-all-mid-10k-sp (workloads/)","3.76","4.91","4.14","4.14","3.87","1.28","4.06","4.29"
    "nnet_test (workloads/)","7.32","6.86","7.25","7.70","7.33","2.17","7.72","7.17"
    "parser-125k (workloads/)","21.05","21.05","20.41","21.28","20.20","14.29","21.28","21.74"
    "radix2-big-64k (workloads/)","297.62","426.62","221.83","271.44","285.63","64.99","417.71","601.69"
    "sha-test (workloads/)","312.50","322.58","312.50","303.03","312.50","161.29","322.58","322.58"
    "zip-test (workloads/)","90.91","95.24","86.96","90.91","90.91","42.55","95.24","90.91"

 


.. csv-table:: CoreMarkProFourCore Benchmarks
    :header: "Benchmarks","am69_sk-fs: perf","j722s_evm-fs: perf","j742s2_evm-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","322.58","161.29","322.58","322.58"
    "core (workloads/)","3.11","1.19","3.11","2.99"
    "coremark-pro ()","8690.37","2544.35","7851.44","8662.99"
    "linear_alg-mid-100x100-sp (workloads/)","310.56","56.43","308.64","312.50"
    "loops-all-mid-10k-sp (workloads/)","7.66","2.06","5.75","7.51"
    "nnet_test (workloads/)","12.25","3.62","12.25","12.15"
    "parser-125k (workloads/)","40.00","8.39","37.04","40.00"
    "radix2-big-64k (workloads/)","747.94","89.83","434.22","772.80"
    "sha-test (workloads/)","526.32","270.27","526.32","526.32"
    "zip-test (workloads/)","173.91","76.92","173.91","173.91"

 


.. csv-table:: CoreMarkProEightCore Benchmarks
    :header: "Benchmarks","am69_sk-fs: perf","j784s4-evm: perf"

    "cjpeg-rose7-preset (workloads/)","625.00","625.00"
    "core (workloads/)","6.19","6.20"
    "coremark-pro ()","14127.78","14143.59"
    "linear_alg-mid-100x100-sp (workloads/)","581.40","581.40"
    "loops-all-mid-10k-sp (workloads/)","10.02","10.31"
    "nnet_test (workloads/)","18.38","19.16"
    "parser-125k (workloads/)","72.73","72.07"
    "radix2-big-64k (workloads/)","856.16","812.35"
    "sha-test (workloads/)","769.23","769.23"
    "zip-test (workloads/)","320.00","320.00"

 
 


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

    "4m-check (workloads/)","830.84","1007.66","870.17","865.65","800.51","396.64","1154.73","1019.16"
    "4m-check-reassembly (workloads/)","144.51","188.32","118.06","144.72","144.30","115.21","185.53","191.94"
    "4m-check-reassembly-tcp (workloads/)","88.65","111.61","87.11","95.79","88.97","57.74","111.11","107.76"
    "4m-check-reassembly-tcp-cmykw2-rotatew2 (workloads/)","41.35","37.06","40.49","44.35","40.32","32.57","56.13","38.36"
    "4m-check-reassembly-tcp-x264w2 (workloads/)","2.62","4.88","2.67","2.71","2.67","1.73","4.84","4.84"
    "4m-cmykw2 (workloads/)","307.22","586.51","311.53","314.47","294.55","241.26","606.06","588.24"
    "4m-cmykw2-rotatew2 (workloads/)","60.00","44.48","58.82","62.89","58.94","49.34","72.29","46.88"
    "4m-reassembly (workloads/)","116.96","136.61","104.93","127.39","113.90","79.43","135.69","138.89"
    "4m-rotatew2 (workloads/)","69.20","61.27","69.93","73.58","69.98","52.47","77.28","55.46"
    "4m-tcp-mixed (workloads/)","266.67","250.00","253.97","275.86","258.07","116.79","271.19","250.00"
    "4m-x264w2 (workloads/)","2.73","5.07","2.71","2.77","2.71","1.93","4.75","5.07"
    "idct-4m (workloads/)","34.77","35.06","34.86","35.05","34.89","19.16","34.76","35.11"
    "idct-4mw1 (workloads/)","34.94","35.05","34.76","34.81","34.94","19.15","34.94","34.95"
    "ippktcheck-4m (workloads/)","818.33","1007.25","862.37","866.55","813.27","392.90","1181.47","1011.74"
    "ippktcheck-4mw1 (workloads/)","819.94","1010.10","868.96","871.08","827.54","394.95","1177.58","1015.43"
    "ipres-4m (workloads/)","164.11","192.06","155.60","178.15","163.93","106.31","193.30","187.03"
    "ipres-4mw1 (workloads/)","163.40","193.30","156.74","179.64","158.73","105.12","193.55","189.16"
    "md5-4m (workloads/)","43.23","45.66","44.23","46.90","43.16","28.23","48.40","45.62"
    "md5-4mw1 (workloads/)","43.84","45.60","44.21","47.10","43.65","28.18","48.24","45.93"
    "rgbcmyk-4m (workloads/)","162.73","163.67","162.73","163.40","162.34","65.60","163.80","163.80"
    "rgbcmyk-4mw1 (workloads/)","162.73","163.53","162.73","163.40","162.47","65.49","160.51","163.67"
    "rotate-4ms1 (workloads/)","50.45","53.48","51.49","54.00","50.81","22.83","54.00","53.42"
    "rotate-4ms1w1 (workloads/)","50.35","53.59","50.97","54.00","50.61","22.81","53.42","53.48"
    "rotate-4ms64 (workloads/)","52.30","54.95","52.63","55.31","51.87","23.03","54.64","54.88"
    "rotate-4ms64w1 (workloads/)","52.52","54.95","52.36","55.37","52.63","23.03","55.31","54.95"
    "x264-4mq (workloads/)","1.42","1.44","1.42","1.43","1.43","0.58","1.44","1.42"
    "x264-4mqw1 (workloads/)","1.43","1.45","1.43","1.43","1.42","0.58","1.43","1.43"



 
 


Boot-time Measurement
---------------------


Boot media: MMCSD
^^^^^^^^^^^^^^^^^

.. csv-table:: Linux boot time MMCSD
    :header: "Boot Configuration","am68_sk-fs: Boot time in seconds: avg(min,max)","am69_sk-fs: Boot time in seconds: avg(min,max)","j7200-evm: Boot time in seconds: avg(min,max)","j721e-idk-gw: Boot time in seconds: avg(min,max)","j721s2-evm: Boot time in seconds: avg(min,max)","j722s_evm-fs: Boot time in seconds: avg(min,max)","j742s2_evm-fs: Boot time in seconds: avg(min,max)","j784s4-evm: Boot time in seconds: avg(min,max)"

    "Linux boot time from SD with default rootfs (20 boot cycles)","19.98 (min 19.29, max 21.49)","19.58 (min 18.71, max 23.48)","18.95 (min 18.51, max 22.78)","21.87 (min 21.53, max 22.25)","21.03 (min 20.52, max 21.49)","20.85 (min 20.47, max 21.05)","20.05 (min 19.68, max 23.71)","19.79 (min 19.51, max 20.21)"

 

 

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

    "8000","","","","","255988.00","0.32","1023979.00","0.74"
    "11025","352791.00","0.19","1023979.00","0.72","331809.00","0.36","1023988.00","0.27"
    "16000","511990.00","0.33","1023988.00","1.21","511977.00","0.36","1023966.00","0.16"
    "22050","705573.00","0.31","1023965.00","0.95","663631.00","0.45","1023982.00","0.21"
    "24000","705581.00","0.35","1023982.00","0.93","663611.00","0.45","1023985.00","0.22"
    "32000","1023977.00","0.22","1023984.00","1.04","1023926.00","0.54","1023966.00","0.15"
    "44100","1411171.00","0.54","1417793.00","0.96","1327227.00","0.63","1417810.00","0.18"
    "48000","1535969.00","0.75","1535955.00","0.97","1535909.00","0.66","1535967.00","0.14"
    "88200","2822343.00","0.93","2835618.00","1.44","2654473.00","1.00","2835634.00","0.32"
    "96000","3071938.00","0.50","3071926.00","1.52","3071829.00","1.05","3071939.00","0.20"




.. csv-table:: Audio Playback
    :header: "Sampling Rate (Hz)","j721e-idk-gw: Throughput (bits/sec)","j721e-idk-gw: CPU Load (%)","j721s2-evm: Throughput (bits/sec)","j721s2-evm: CPU Load (%)","j784s4-evm: Throughput (bits/sec)","j784s4-evm: CPU Load (%)"

    "8000","","","","","1024398.00","0.11"
    "11025","352938.00","0.35","352953.00","2.55","1024394.00","0.14"
    "16000","512203.00","0.49","512243.00","2.55","1024401.00","0.19"
    "22050","705866.00","0.43","705945.00","2.63","1024407.00","0.21"
    "24000","705874.00","0.47","768392.00","2.63","1024390.00","0.14"
    "32000","1024402.00","0.56","1024610.00","3.19","1024392.00","0.16"
    "44100","1411756.00","0.67","1412035.00","2.83","1418397.00","0.20"
    "48000","1536607.00","0.54","1536896.00","2.70","1536601.00","0.26"
    "88200","2823513.00","1.11","1536900.00","3.09","2836804.00","0.33"
    "96000","3073212.00","0.67","1536890.00","3.04","3073206.00","0.39"

 
 



 



|

Graphics SGX/RGX Driver
-------------------------
 


GFXBench
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Run GFXBench and capture performance reported (Score and Display rate in fps). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: GFXBench Performance
    :header: "Benchmark","am68_sk-fs: Score","am68_sk-fs: Fps","am69_sk-fs: Score","am69_sk-fs: Fps","j721e-idk-gw: Score","j721e-idk-gw: Fps","j721s2-evm: Score","j721s2-evm: Fps","j742s2_evm-fs: Score","j742s2_evm-fs: Fps","j784s4-evm: Score","j784s4-evm: Fps"

    " GFXBench 3.x gl_manhattan_off","964.56","15.56","887.59","14.32","1210.70","19.53","947.57","15.28","962.22","15.52","906.08","14.61"
    " GFXBench 3.x gl_trex_off","1596.91","28.52","1470.83","26.26","1837.06","32.80","1652.76","29.51","1593.90","28.46","1457.13","26.02"
    " GFXBench 4.x gl_4_off","260.95","4.42","254.29","4.30","410.48","6.95","260.17","4.40","260.97","4.42","254.27","4.30"
    " GFXBench 5.x gl_5_high_off","114.75","1.78","111.24","1.73","179.42","2.79","113.83","1.77","113.24","1.76","110.80","1.72"




Glmark2
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run Glmark2 and capture performance reported (Score). All display outputs (HDMI, Displayport and/or LCD) are connected when running these tests

.. csv-table:: Glmark2 Performance
    :header: "Benchmark","am68_sk-fs: Score","am69_sk-fs: Score","j721e-idk-gw: Score","j721s2-evm: Score","j722s_evm-fs: Score","j742s2_evm-fs: Score","j784s4-evm: Score"

    "Glmark2-DRM","517.00","165.00","48.00","112.00","287.00","142.00","169.00"
    "Glmark2-Wayland","1257.00","1282.00","1125.00","1244.00","695.00","1350.00","1343.00"
    "Glmark2-Wayland 4000x4000","85.00","88.00","","82.00","84.00"

 
 

 

 



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

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","0.02","82.75","0.02","28.54","1743.22","79.05","1830.17","86.82","1851.81","80.63","1818.90","65.86","1824.67","56.17","1682.56","26.69"




.. rubric::  TCP Bidirectional Throughput Interrupt Pacing
   :name: CPSW2g-tcp-bidirectional-throughput-interrupt-pacing

.. csv-table:: CPSW2g TCP Bidirectional Throughput Interrupt Pacing
    :header: "Command Used","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_STREAM; netperf -H 192.168.0.1 -j -c -C -l 60 -t TCP_MAERTS","1809.18","48.73","1698.08","35.51","1822.60","61.48","1751.43","12.82"




.. rubric::  UDP Throughput
   :name: CPSW2g-udp-throughput-0-loss

.. csv-table:: CPSW2g UDP Egress Throughput 0 loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j722s_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j722s_evm-fs: THROUGHPUT (Mbits/sec)","j722s_evm-fs: Packets Per Second (kPPS)","j722s_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","13.09","91.00","38.04","18.00","15.63","109.00","39.95","18.00","23.08","160.00","43.75","18.00","22.40","156.00","22.40"
    "128","82.00","66.40","101.00","47.34","82.00","79.91","122.00","26.41","82.00","105.72","161.00","44.25","82.00","105.77","161.00","22.40"
    "256","210.00","36.29","22.00","10.41","210.00","50.40","30.00","13.52","210.00","268.59","160.00","44.11","210.00","269.95","161.00","22.02"
    "1024","978.00","104.06","13.00","2.93","978.00","811.59","104.00","39.55","978.00","936.10","120.00","34.47","978.00","934.46","119.00","17.95"
    "1518","1472.00","289.67","25.00","19.03","1472.00","956.39","81.00","34.79","1472.00","956.86","81.00","24.13","1472.00","954.64","81.00","12.17"




.. csv-table:: CPSW2g UDP Ingress Throughput 0 loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)"

    "64","18.00","1.68","12.00","7.21"
    "128","82.00","5.31","8.00","4.62","82.00","4.59","7.00","0.97","82.00","125.79","192.00","11.82"
    "256","210.00","14.45","9.00","2.69","210.00","30.74","18.00","2.04","210.00","29.74","18.00","1.19"
    "1024","978.00","65.72","8.00","6.12","978.00","71.20","9.00","1.20"
    "1518","1472.00","754.65","64.00","56.22","1472.00","955.30","81.00","32.38"




.. csv-table:: CPSW2g UDP Ingress Throughput possible loss
    :header: "Frame Size(bytes)","j721e-idk-gw: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j721e-idk-gw: THROUGHPUT (Mbits/sec)","j721e-idk-gw: Packets Per Second (kPPS)","j721e-idk-gw: CPU Load % (LOCAL_CPU_UTIL)","j721e-idk-gw: Packet Loss %","j742s2_evm-fs: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j742s2_evm-fs: THROUGHPUT (Mbits/sec)","j742s2_evm-fs: Packets Per Second (kPPS)","j742s2_evm-fs: CPU Load % (LOCAL_CPU_UTIL)","j742s2_evm-fs: Packet Loss %","j784s4-evm: UDP Datagram Size(bytes) (LOCAL_SEND_SIZE)","j784s4-evm: THROUGHPUT (Mbits/sec)","j784s4-evm: Packets Per Second (kPPS)","j784s4-evm: CPU Load % (LOCAL_CPU_UTIL)","j784s4-evm: Packet Loss %"

    "64","18.00","53.83","374.00","91.85","6.89"
    "128","82.00","224.93","343.00","91.66","20.34","82.00","194.80","297.00","43.67","58.01","82.00","221.60","338.00","22.28","17.39"
    "256","210.00","566.73","337.00","92.00","21.44","210.00","490.25","292.00","43.93","32.09","210.00","577.26","344.00","23.59","21.05"
    "1024","978.00","894.65","114.00","79.79","1.27","978.00","932.88","119.00","19.41","0.02"
    "1518","1472.00","946.19","80.00","72.83","0.05","1472.00","955.30","81.00","32.38","0.00"

 
 

 

 
 



|

PCIe Driver
-------------------------


 


PCIe-NVMe-SSD
^^^^^^^^^^^^^^^^^^^^^^^^^^^
 

 


J721E-IDK-GW
"""""""""""""""""""""""""""




.. csv-table:: PCIE SSD EXT4 FIO 10G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","754.00","14.35","1514.00","8.14"
    "4m","754.00","12.74","1511.00","5.40"
    "4k","180.00","48.78","159.00","36.28"
    "256k","757.00","16.11","718.00","6.61"



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

    "102400","0.69 (min 0.52, max 1.34)","53.09 (min 47.90, max 55.41)","83.86","25.00"
    "262144","0.50 (min 0.37, max 0.57)","54.33 (min 51.39, max 56.75)","83.53","40.00"
    "524288","0.50 (min 0.37, max 0.57)","55.56 (min 52.45, max 59.70)","82.50","33.33"
    "1048576","0.50 (min 0.37, max 0.56)","54.24 (min 52.13, max 57.11)","80.20","40.00"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j721e-idk-gw: Raw Read Throughput (Mbytes/sec)"

    "50","263.16"

 
 


J722S-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j722s_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Write UBIFS CPU Load (%)","j722s_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j722s_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.18 (min 0.13, max 0.28)","28.69 (min 25.00, max 31.92)","64.64","21.43"
    "262144","0.14 (min 0.11, max 0.18)","31.24 (min 28.19, max 34.36)","65.26","16.67"
    "524288","0.14 (min 0.11, max 0.19)","31.91 (min 30.37, max 35.03)","65.03","20.00"
    "1048576","0.14 (min 0.11, max 0.19)","31.16 (min 29.82, max 32.49)","62.67","15.38"




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

    "102400","0.17 (min 0.12, max 0.28)","15.76 (min 12.38, max 18.60)","76.59","4.55"
    "262144","0.13 (min 0.10, max 0.18)","14.90 (min 13.44, max 16.10)","71.63","0.00"
    "524288","0.14 (min 0.11, max 0.18)","15.77 (min 13.89, max 17.11)","71.44","8.33"
    "1048576","0.13 (min 0.10, max 0.18)","16.71 (min 15.61, max 17.96)","71.96","4.35"




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

    "102400","0.17 (min 0.12, max 0.27)","50.25 (min 49.77, max 51.06)","80.64","33.33"
    "262144","0.13 (min 0.10, max 0.18)","50.68 (min 50.05, max 51.01)","78.57","40.00"
    "524288","0.13 (min 0.11, max 0.18)","50.63 (min 50.09, max 51.14)","77.76","0.00"
    "1048576","0.14 (min 0.10, max 0.18)","50.68 (min 50.28, max 51.32)","75.66","42.86"




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

    "102400","0.17 (min 0.12, max 0.28)","14.95 (min 12.50, max 16.61)","81.58","9.52"
    "262144","0.13 (min 0.10, max 0.18)","14.77 (min 13.53, max 16.65)","73.27","4.55"
    "524288","0.14 (min 0.10, max 0.18)","15.21 (min 13.36, max 16.75)","77.75","4.76"
    "1048576","0.14 (min 0.10, max 0.18)","15.66 (min 13.78, max 17.33)","77.90","9.09"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j784s4-evm: Raw Read Throughput (Mbytes/sec)"

    "50","263.16"

 
 



J742S2-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^


UBIFS
"""""""""""""""""""""""""""

.. csv-table:: OSPI Flash Driver
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write UBIFS Throughput (Mbytes/sec)","j742s2_evm-fs: Write UBIFS CPU Load (%)","j742s2_evm-fs: Read UBIFS Throughput (Mbytes/sec)","j742s2_evm-fs: Read UBIFS CPU Load (%)"

    "102400","0.17 (min 0.12, max 0.28)","28.79 (min 25.02, max 31.29)","68.69","18.18"
    "262144","0.13 (min 0.10, max 0.18)","30.86 (min 28.91, max 32.29)","74.46","18.18"
    "524288","0.14 (min 0.11, max 0.18)","30.62 (min 26.24, max 34.23)","73.14","9.09"
    "1048576","0.14 (min 0.11, max 0.18)","30.43 (min 27.81, max 33.06)","73.57","9.09"




RAW
"""""""""""""""""""""""""""

.. csv-table:: OSPI Raw Flash Driver
    :header: "File size (Mbytes)","j742s2_evm-fs: Raw Read Throughput (Mbytes/sec)"

    "50","172.41"

 
 

 

 
 

 



|

UBoot QSPI/OSPI Driver
-------------------------

 










J721E-IDK-GW
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","1047.57","15875.97"
    "800000","1048.11","16062.75"
    "1000000","1048.58","16157.79"
    "2000000","1047.17","16221.78"








J721S2-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "400000","1000.00","15814.67"
    "800000","1001.47","16062.75"
    "1000000","1001.53","16173.74"
    "2000000","1001.96","16213.76"




J784S4-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","989.85","15875.97"
    "800000","990.57","16062.75"
    "1000000","991.17","16157.79"
    "2000000","991.11","16221.78"




J742S2-EVM
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: UBOOT QSPI or OSPI
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","1004.17","15814.67"
    "800000","1005.15","16062.75"
    "1000000","1005.34","16157.79"
    "2000000","1005.77","16221.78"



















 
 

 

 



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

    "400000","204800.00","372363.64"
    "800000","248242.42","512000.00"
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
    :header: "Buffer size (bytes)","j7200-evm: Write EXT4 Throughput (Mbytes/sec)","j7200-evm: Write EXT4 CPU Load (%)","j7200-evm: Read EXT4 Throughput (Mbytes/sec)","j7200-evm: Read EXT4 CPU Load (%)"

    "1m","60.90","1.71","315.00","1.89"
    "4m","61.10","1.34","314.00","1.05"
    "4k","55.50","24.14","56.30","20.34"
    "256k","60.80","1.84","316.00","3.81"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","59.40","1.53","175.00","1.32"
    "4m","59.50","1.28","175.00","0.79"
    "4k","51.00","21.53","56.70","20.01"
    "256k","59.50","1.99","174.00","2.26"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

    "1m","94.80","1.78","174.00","2.04"
    "4m","95.30","1.19","174.00","1.59"
    "4k","67.80","21.89","94.10","22.70"
    "256k","94.80","1.96","173.00","2.87"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","60.60","2.01","314.00","2.06"
    "4m","60.00","1.47","311.00","1.37"
    "4k","59.20","28.11","56.10","21.78"
    "256k","60.60","2.32","312.00","4.64"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

    "1m","95.20","0.48","292.00","0.44"
    "4m","95.60","0.49","155.00","0.18"
    "4k","83.20","11.89","94.00","9.55"
    "256k","95.20","0.64","292.00","1.10"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Write EXT4 CPU Load (%)","j742s2_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Read EXT4 CPU Load (%)"

    "1m","97.90","1.11","294.00","0.96"
    "4m","97.50","1.04","293.00","0.57"
    "4k","82.80","20.66","81.40","15.89"
    "256k","97.90","1.22","292.00","1.97"

 


.. csv-table:: EMMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Write EXT4 CPU Load (%)","am69_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Read EXT4 CPU Load (%)"

    "1m","91.40","0.53","288.00","0.63"
    "4m","90.60","0.47","285.00","0.21"
    "4k","78.80","11.86","93.10","9.71"
    "256k","91.50","0.69","286.00","0.99"

 

 

 

 

 

 

 
 


EMMC RAW FIO 1G
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "1m","60.90","1.61","315.00","1.96"
    "4m","61.20","1.36","307.00","1.22"
    "4k","56.90","19.30","56.40","18.62"
    "256k","60.80","1.84","317.00","3.74"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "1m","62.10","1.47","175.00","1.27"
    "4m","61.50","1.27","175.00","0.79"
    "4k","53.00","17.36","56.50","17.81"
    "256k","61.60","1.70","174.00","2.35"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "1m","95.30","1.66","174.00","1.98"
    "4m","95.10","1.17","174.00","1.46"
    "4k","68.30","16.51","93.60","20.64"
    "256k","95.30","1.98","173.00","2.72"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "1m","59.80","3.83","313.00","3.78"
    "4m","60.10","3.45","300.00","3.40"
    "4k","55.70","22.62","56.00","22.14"
    "256k","59.90","4.13","309.00","5.79"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "1m","79.70","0.40","113.00","0.26"
    "4m","79.80","0.43","114.00","0.15"
    "4k","8.63","0.96","56.70","5.21"
    "256k","69.80","0.47","94.30","0.37"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Write Raw CPU Load (%)","j742s2_evm-fs: Read Raw Throughput (Mbytes/sec)","j742s2_evm-fs: Read Raw CPU Load (%)"

    "1m","96.90","1.05","294.00","1.06"
    "4m","98.40","0.99","197.00","0.47"
    "4k","83.30","16.47","93.60","17.65"
    "256k","96.40","1.07","294.00","1.91"

 


.. csv-table:: EMMC RAW FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write Raw Throughput (Mbytes/sec)","am69_sk-fs: Write Raw CPU Load (%)","am69_sk-fs: Read Raw Throughput (Mbytes/sec)","am69_sk-fs: Read Raw CPU Load (%)"

    "1m","90.40","0.51","293.00","0.40"
    "4m","97.30","0.47","151.00","0.13"
    "4k","76.90","7.98","91.40","7.92"
    "256k","91.20","0.59","293.00","0.80"

 

 

 

 

 

 

 
 

 

 

 

 

 
 



UBoot EMMC Driver
-----------------

 

 

 

 

 

 

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

    "2000000","57286.71","312076.19"
    "4000000","58462.09","315076.92"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "2000000","60794.06","173375.66"
    "4000000","61420.81","177604.34"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j722s_evm-fs: Write Throughput (Kbytes/sec)","j722s_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","95533.53","141852.81"
    "4000000","93891.12","170666.67"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "2000000","59795.62","312076.19"
    "4000000","60907.06","318135.92"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "2000000","99296.97","282482.76"
    "4000000","99750.38","293883.41"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "2000000","97814.93","282482.76"
    "4000000","100979.97","293883.41"

 


.. csv-table:: UBOOT EMMC RAW
    :header: "File size (bytes in hex)","am69_sk-fs: Write Throughput (Kbytes/sec)","am69_sk-fs: Read Throughput (Kbytes/sec)"

    "2000000","96946.75","214169.93"
    "4000000","95394.47","257003.92"

 

 

 

 

 

 

 
 

 


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

    "1m","42.50","1.46","87.30","1.05"
    "4m","41.10","1.09","87.30","0.68"
    "4k","2.80","2.19","13.00","6.36"
    "256k","38.90","1.70","84.00","1.40"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write EXT4 Throughput (Mbytes/sec)","j721s2-evm: Write EXT4 CPU Load (%)","j721s2-evm: Read EXT4 Throughput (Mbytes/sec)","j721s2-evm: Read EXT4 CPU Load (%)"

    "1m","42.10","2.05","87.90","1.41"
    "4m","40.10","1.50","82.30","1.23"
    "4k","2.81","2.78","13.10","7.12"
    "256k","38.70","2.26","84.40","1.76"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write EXT4 Throughput (Mbytes/sec)","j784s4-evm: Write EXT4 CPU Load (%)","j784s4-evm: Read EXT4 Throughput (Mbytes/sec)","j784s4-evm: Read EXT4 CPU Load (%)"

    "1m","43.20","0.32","87.30","0.27"
    "4m","41.30","0.31","87.40","0.20"
    "4k","2.79","0.64","13.00","1.78"
    "256k","38.20","0.35","83.30","0.40"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j742s2_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Write EXT4 CPU Load (%)","j742s2_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j742s2_evm-fs: Read EXT4 CPU Load (%)"

    "1m","43.30","0.66","87.40","0.72"
    "4m","42.20","0.65","87.10","0.44"
    "4k","2.77","1.47","12.90","4.27"
    "256k","36.30","0.73","83.70","0.85"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Write EXT4 CPU Load (%)","j721e-idk-gw: Read EXT4 Throughput (Mbytes/sec)","j721e-idk-gw: Read EXT4 CPU Load (%)"

    "1m","33.00","1.14","41.90","0.64"
    "4m","31.00","0.91","41.50","0.63"
    "4k","2.80","2.09","11.30","5.07"
    "256k","30.80","1.21","42.90","0.98"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Write EXT4 CPU Load (%)","j722s_evm-fs: Read EXT4 Throughput (Mbytes/sec)","j722s_evm-fs: Read EXT4 CPU Load (%)"

    "1m","42.30","1.14","87.10","1.57"
    "4m","41.60","0.93","87.50","1.14"
    "4k","2.79","1.85","13.00","4.49"
    "256k","38.90","1.42","83.90","1.64"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am68_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am68_sk-fs: Write EXT4 CPU Load (%)","am68_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am68_sk-fs: Read EXT4 CPU Load (%)"

    "1m","18.20","1.14","86.80","1.15"
    "4m","18.30","0.84","86.60","0.78"
    "4k","4.22","3.25","13.70","7.19"
    "256k","17.40","1.12","82.60","1.43"

 


.. csv-table:: MMC EXT4 FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Write EXT4 CPU Load (%)","am69_sk-fs: Read EXT4 Throughput (Mbytes/sec)","am69_sk-fs: Read EXT4 CPU Load (%)"

    "1m","18.50","0.19","86.80","0.27"
    "4m","18.80","0.19","86.50","0.17"
    "4k","4.65","0.89","14.30","1.92"
    "256k","17.90","0.15","82.60","0.34"

 

 

 

 

 

 

 

 

 
 


MMC RAW FIO 1G
^^^^^^^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j7200-evm: Write Raw Throughput (Mbytes/sec)","j7200-evm: Write Raw CPU Load (%)","j7200-evm: Read Raw Throughput (Mbytes/sec)","j7200-evm: Read Raw CPU Load (%)"

    "1m","45.30","1.46","88.20","0.94"
    "4m","44.10","1.27","88.10","0.67"
    "4k","2.82","1.88","13.00","5.76"
    "256k","41.40","1.40","84.40","1.36"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721s2-evm: Write Raw Throughput (Mbytes/sec)","j721s2-evm: Write Raw CPU Load (%)","j721s2-evm: Read Raw Throughput (Mbytes/sec)","j721s2-evm: Read Raw CPU Load (%)"

    "1m","45.00","1.70","88.30","1.21"
    "4m","45.00","1.50","88.10","0.97"
    "4k","2.82","2.39","13.00","6.65"
    "256k","41.40","1.86","84.50","1.67"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j784s4-evm: Write Raw Throughput (Mbytes/sec)","j784s4-evm: Write Raw CPU Load (%)","j784s4-evm: Read Raw Throughput (Mbytes/sec)","j784s4-evm: Read Raw CPU Load (%)"

    "1m","45.10","0.33","88.30","0.26"
    "4m","45.20","0.33","87.70","0.20"
    "4k","2.83","0.58","13.10","1.63"
    "256k","41.20","0.36","84.50","0.40"

 

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j721e-idk-gw: Write Raw Throughput (Mbytes/sec)","j721e-idk-gw: Write Raw CPU Load (%)","j721e-idk-gw: Read Raw Throughput (Mbytes/sec)","j721e-idk-gw: Read Raw CPU Load (%)"

    "1m","33.10","0.92","43.90","0.68"
    "4m","32.40","0.93","43.90","0.58"
    "4k","2.79","1.81","11.40","4.80"
    "256k","29.80","1.10","42.90","0.91"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "1m","42.60","1.10","88.30","1.46"
    "4m","41.60","0.90","88.10","1.00"
    "4k","2.82","1.61","13.00","4.13"
    "256k","36.50","1.18","84.50","1.63"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am68_sk-fs: Write Raw Throughput (Mbytes/sec)","am68_sk-fs: Write Raw CPU Load (%)","am68_sk-fs: Read Raw Throughput (Mbytes/sec)","am68_sk-fs: Read Raw CPU Load (%)"

    "1m","18.10","0.84","87.20","1.11"
    "4m","18.20","0.82","87.20","0.75"
    "4k","4.10","3.02","13.60","6.71"
    "256k","17.40","0.89","82.60","1.48"

 


.. csv-table:: MMC RAW FIO 1G
    :header: "Buffer size (bytes)","am69_sk-fs: Write Raw Throughput (Mbytes/sec)","am69_sk-fs: Write Raw CPU Load (%)","am69_sk-fs: Read Raw Throughput (Mbytes/sec)","am69_sk-fs: Read Raw CPU Load (%)"

    "1m","44.60","0.28","88.30","0.21"
    "4m","43.10","0.25","88.30","0.14"
    "4k","2.81","0.53","13.10","1.55"
    "256k","41.20","0.30","84.50","0.32"

 

 

 
 


MMC EXT4
^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC EXT4
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "102400","36.64 (min 35.08, max 38.97)","3.05 (min 2.64, max 4.28)","74.98","4.48"
    "262144","36.75 (min 35.92, max 38.81)","3.21 (min 2.75, max 4.74)","86.68","3.59"
    "524288","38.30 (min 37.56, max 38.75)","2.97 (min 2.52, max 4.07)","91.44","5.42"
    "1048576","38.47 (min 37.85, max 40.29)","3.03 (min 2.36, max 4.32)","90.54","5.59"
    "5242880","40.75 (min 38.47, max 41.44)","3.21 (min 2.67, max 4.31)","91.30","5.22"

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 


MMC EXT2
^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: MMC EXT2
    :header: "Buffer size (bytes)","j722s_evm-fs: Write Raw Throughput (Mbytes/sec)","j722s_evm-fs: Write Raw CPU Load (%)","j722s_evm-fs: Read Raw Throughput (Mbytes/sec)","j722s_evm-fs: Read Raw CPU Load (%)"

    "102400","36.58 (min 33.29, max 37.87)","3.28 (min 2.63, max 5.41)","76.25","4.93"
    "262144","37.12 (min 33.20, max 38.77)","3.26 (min 2.70, max 5.39)","86.25","7.69"
    "524288","40.12 (min 37.17, max 41.34)","3.57 (min 2.92, max 5.77)","85.65","4.93"
    "1048576","41.28 (min 37.00, max 42.84)","3.66 (min 3.04, max 5.91)","90.17","4.98"
    "5242880","38.06 (min 34.88, max 39.21)","3.25 (min 2.49, max 5.41)","90.39","5.17"

 

 

 

 

 

 

 

 

 

 

 

 

 
 

 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
-  Partition was mounted with async option
 



UBoot MMCSD
-----------


UBOOT MMCSD FAT
^^^^^^^^^^^^^^^

 

 

 

 

 

 

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j722s_evm-fs: Write Throughput (Kbytes/sec)","j722s_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","31030.30","83591.84"
    "800000","45765.36","87148.94"
    "1000000","48907.46","90021.98"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j721e-idk-gw: Write Throughput (Kbytes/sec)","j721e-idk-gw: Read Throughput (Kbytes/sec)"

    "400000","31751.94","44521.74"
    "800000","35772.93","45765.36"
    "1000000","32251.97","46282.49"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j7200-evm: Write Throughput (Kbytes/sec)","j7200-evm: Read Throughput (Kbytes/sec)"

    "400000","39384.62","83591.84"
    "800000","43574.47","89043.48"
    "1000000","45893.56","90519.34"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j721s2-evm: Write Throughput (Kbytes/sec)","j721s2-evm: Read Throughput (Kbytes/sec)"

    "400000","37577.98","83591.84"
    "800000","44765.03","88086.02"
    "1000000","43924.93","90519.34"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j784s4-evm: Write Throughput (Kbytes/sec)","j784s4-evm: Read Throughput (Kbytes/sec)"

    "400000","38641.51","83591.84"
    "800000","37577.98","88086.02"
    "1000000","47080.46","90519.34"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","j742s2_evm-fs: Write Throughput (Kbytes/sec)","j742s2_evm-fs: Read Throughput (Kbytes/sec)"

    "400000","39384.62","83591.84"
    "800000","42226.80","88086.02"
    "1000000","47352.60","90519.34"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am68_sk-fs: Write Throughput (Kbytes/sec)","am68_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","18618.18","80313.73"
    "800000","18204.44","85333.33"
    "1000000","18984.94","89530.05"

 


.. csv-table:: UBOOT MMCSD FAT
    :header: "File size (bytes in hex)","am69_sk-fs: Write Throughput (Kbytes/sec)","am69_sk-fs: Read Throughput (Kbytes/sec)"

    "400000","14222.22","78769.23"
    "800000","17429.79","85333.33"
    "1000000","18004.40","89530.05"

 

 

 

 

 

 

 

 

 
 

 

The performance numbers were captured using the following:

-  SanDisk Max Endurance SD card (SDSQQVR-032G-GN6IA)
 



|

USB Driver
-------------------------
 


USB Device Controller
^^^^^^^^^^^^^^^^^^^^^^^^^^^










.. csv-table:: USBDEVICE HIGHSPEED SLAVE_READ_THROUGHPUT
    :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721e-idk-gw: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j722s_evm-fs: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

    "150","40.40","42.30","32.90","44.20","43.80","43.30"




.. csv-table:: USBDEVICE HIGHSPEED SLAVE_WRITE_THROUGHPUT
    :header: "Number of Blocks","j7200-evm: Throughput (MB/sec)","j721e-idk-gw: Throughput (MB/sec)","j721s2-evm: Throughput (MB/sec)","j722s_evm-fs: Throughput (MB/sec)","j742s2_evm-fs: Throughput (MB/sec)","j784s4-evm: Throughput (MB/sec)"

    "150","37.10","40.30","30.40","39.70","37.20","34.60"





 
 
 



|

CRYPTO Driver
-------------------------


OpenSSL Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: OpenSSL Performance
    :header: "Algorithm","Buffer Size (in bytes)","am68_sk-fs: throughput (KBytes/Sec)","am69_sk-fs: throughput (KBytes/Sec)","j7200-evm: throughput (KBytes/Sec)","j721e-idk-gw: throughput (KBytes/Sec)","j721s2-evm: throughput (KBytes/Sec)","j722s_evm-fs: throughput (KBytes/Sec)","j742s2_evm-fs: throughput (KBytes/Sec)","j784s4-evm: throughput (KBytes/Sec)"

    "aes-128-cbc","1024","39776.60","37876.05","35652.61","41832.11","39509.33","22700.71","38864.90","38312.28"
    "aes-128-cbc","16","757.38","759.78","700.72","806.16","770.10","410.41","756.66","586.88"
    "aes-128-cbc","16384","174451.37","161983.15","181294.42","182829.06","176171.69","83432.79","178372.61","171562.33"
    "aes-128-cbc","256","11545.77","10588.84","10623.32","12217.94","11588.95","6710.61","11346.52","11240.19"
    "aes-128-cbc","64","3000.11","2343.27","2815.42","3224.94","3067.58","1796.97","3018.35","2858.75"
    "aes-128-cbc","8192","141926.40","136314.88","141770.75","149670.57","142267.73","70707.88","141910.02","139902.98"
    "aes-128-ecb","1024","40072.19","33729.88","35654.31","42456.06","40214.19","23350.95","39293.61","38010.54"
    "aes-128-ecb","16","782.96","620.01","708.05","821.63","782.52","415.09","769.32","753.73"
    "aes-128-ecb","16384","180977.66","178296.15","183681.02","192927.06","177717.25","87725.40","179208.19","166734.51"
    "aes-128-ecb","256","11917.91","11651.33","10662.57","12424.79","11830.53","6854.23","11512.92","11416.32"
    "aes-128-ecb","64","3094.76","3042.71","2811.11","3263.70","3068.03","1835.22","3047.06","2989.63"
    "aes-128-ecb","8192","145118.55","142327.81","143332.69","153985.02","144637.95","72996.18","144509.61","128062.81"
    "aes-192-cbc","1024","39583.06","37878.44","35623.59","41588.74","39249.92","22237.87","38562.82","37961.05"
    "aes-192-cbc","16","769.24","751.60","703.73","809.16","768.23","409.10","766.63","752.44"
    "aes-192-cbc","16384","170508.29","163020.80","176553.98","175762.09","169213.95","76868.27","166499.67","164828.50"
    "aes-192-cbc","256","11557.46","11375.53","10487.98","12095.57","11555.93","6682.45","11242.07","11201.62"
    "aes-192-cbc","64","3047.53","3019.41","2815.47","3221.57","3084.50","1798.04","3028.50","2986.56"
    "aes-192-cbc","8192","139818.33","133589.67","140053.16","142707.37","138240.00","65200.13","135932.59","135239.00"
    "aes-192-ecb","1024","39788.20","37189.97","35806.55","41913.00","39945.90","22708.91","38859.43","38752.60"
    "aes-192-ecb","16","764.43","746.76","705.13","820.05","776.37","416.60","767.78","752.43"
    "aes-192-ecb","16384","174271.15","165675.01","179563.18","179650.56","171977.39","78495.74","172589.06","163599.70"
    "aes-192-ecb","256","11662.17","9747.54","10657.62","12400.21","11611.73","6807.30","11413.67","11541.08"
    "aes-192-ecb","64","3037.87","2957.57","2824.21","3268.22","3103.89","1833.05","3052.54","3007.55"
    "aes-192-ecb","8192","141639.68","138592.26","141219.16","147322.20","141096.28","66945.02","139799.21","132109.65"
    "aes-256-cbc","1024","38649.86","37586.94","35459.75","40549.38","38962.18","21729.96","38346.41","37408.09"
    "aes-256-cbc","16","760.05","602.83","701.84","808.87","772.21","408.51","765.50","746.93"
    "aes-256-cbc","16384","159328.94","151027.71","169558.02","157832.53","154806.95","69670.23","158078.29","154178.90"
    "aes-256-cbc","256","11378.09","9635.07","10454.87","11990.87","11427.41","6644.05","11403.18","11131.73"
    "aes-256-cbc","64","3026.75","2704.28","2812.46","3214.85","3047.66","1789.27","3023.23","2979.65"
    "aes-256-cbc","8192","130304.68","128117.42","136151.04","134621.87","129622.02","60336.81","131082.92","126672.90"
    "aes-256-ecb","1024","39416.49","38501.72","35591.51","41498.28","39168.34","22258.01","38595.24","38117.38"
    "aes-256-ecb","16","767.51","752.31","710.40","814.93","779.77","417.71","763.57","744.68"
    "aes-256-ecb","16384","164397.06","163026.26","174030.85","166040.92","160606.89","71314.09","160415.74","159023.10"
    "aes-256-ecb","256","11545.51","11231.32","10506.50","12227.16","11516.16","6770.69","11296.77","11198.89"
    "aes-256-ecb","64","3041.96","2409.77","2820.95","3249.02","3091.95","1834.05","3041.39","2391.36"
    "aes-256-ecb","8192","133996.54","132262.57","139313.15","138521.26","133510.49","61521.92","132497.41","131380.57"
    "des3","1024","34736.47","29522.60","34081.11","35848.19","34514.94","","34194.77","30356.48"
    "des3","16","774.04","580.82","705.02","811.50","768.67","","766.19","749.16"
    "des3","16384","94213.46","94153.39","115692.89","94983.51","93645.48","","93984.09","93508.95"
    "des3","256","11072.60","10817.19","10171.39","11630.34","10956.12","","10926.42","10675.71"
    "des3","64","3028.86","2515.78","2776.45","3231.17","3049.81","","2966.55","2925.29"
    "des3","8192","83195.22","81453.06","98994.86","85590.02","83550.21","","84036.27","83481.94"
    "sha1","1024","52414.12","50368.51","52431.53","52711.42","52450.65","","50341.89","51912.02"
    "sha1","16","865.50","820.21","875.66","897.21","864.35","","819.59","827.27"
    "sha1","16384","436426.07","430085.46","440341.85","441696.26","441587.03","","432455.68","429872.47"
    "sha1","256","13464.23","13119.91","13759.40","14018.56","13614.59","","12989.53","13117.35"
    "sha1","64","3448.77","3280.94","3493.42","3550.95","3408.90","","3266.79","3280.26"
    "sha1","8192","296203.61","280221.01","294393.17","295084.03","296140.80","","285248.17","283942.91"
    "sha256","1024","52380.33","49182.04","52400.81","52484.10","52420.95","34304.68","50351.45","49931.95"
    "sha256","16","853.53","818.91","854.53","892.62","856.90","566.98","852.75","820.74"
    "sha256","16384","431904.09","419960.15","435115.35","433706.33","423553.71","285693.27","422625.28","420113.07"
    "sha256","256","13279.66","13072.38","13620.91","13992.96","13224.96","8921.86","13023.66","13114.88"
    "sha256","64","3388.57","3276.25","3416.92","3538.41","3347.20","2230.85","3349.70","3288.38"
    "sha256","8192","289600.85","279762.26","287820.46","291659.78","289027.41","188757.33","282187.09","280671.57"
    "sha512","1024","41631.74","40379.73","41217.37","42820.27","42228.74","24479.40","41311.23","40368.81"
    "sha512","16","819.32","818.45","836.67","866.29","848.40","549.18","842.67","819.94"
    "sha512","16384","143769.60","143687.68","144162.82","144894.63","142813.87","67381.93","143698.60","142972.25"
    "sha512","256","12734.21","11931.99","12516.78","12945.32","13018.20","7885.23","12685.57","12137.64"
    "sha512","64","3295.47","3274.67","3344.70","3488.98","3438.19","2196.25","3380.07","3279.98"
    "sha512","8192","123390.63","121907.88","123024.73","124592.13","123420.67","60052.82","123387.90","121263.45"




.. csv-table:: OpenSSL CPU Load
    :header: "Algorithm","am68_sk-fs: CPU Load","am69_sk-fs: CPU Load","j7200-evm: CPU Load","j721e-idk-gw: CPU Load","j721s2-evm: CPU Load","j722s_evm-fs: CPU Load","j742s2_evm-fs: CPU Load","j784s4-evm: CPU Load"

    "aes-128-cbc","32.00","32.00","32.00","33.00","32.00","30.00","33.00","31.00"
    "aes-128-ecb","33.00","33.00","33.00","34.00","33.00","32.00","34.00","33.00"
    "aes-192-cbc","32.00","32.00","32.00","33.00","32.00","30.00","33.00","32.00"
    "aes-192-ecb","33.00","32.00","32.00","33.00","32.00","30.00","33.00","33.00"
    "aes-256-cbc","32.00","31.00","32.00","32.00","32.00","30.00","33.00","32.00"
    "aes-256-ecb","32.00","32.00","32.00","33.00","32.00","18.00","33.00","32.00"
    "des3","29.00","29.00","30.00","30.00","29.00","","30.00","29.00"
    "sha1","96.00","97.00","97.00","97.00","96.00","","97.00","97.00"
    "sha256","96.00","97.00","97.00","97.00","96.00","88.00","97.00","97.00"
    "sha512","96.00","97.00","97.00","97.00","96.00","94.00","97.00","97.00"



Listed for each algorithm are the code snippets used to run each
  benchmark test.

::

    time -v openssl speed -elapsed -evp aes-128-cbc

 




IPSec Software Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: IPSec Software Performance
    :header: "Algorithm","j721e-idk-gw: Throughput (Mbps)","j721e-idk-gw: Packets/Sec","j721e-idk-gw: CPU Load"

    "aes128","695.20","62.00","59.59"
    "aes192","698.70","62.00","59.00"
    "aes256","725.60","64.00","97.84"


 





