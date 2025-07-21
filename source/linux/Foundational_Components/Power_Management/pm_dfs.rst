###
DFS
###

.. rubric:: Overview

Dynamic frequency scaling (DFS) is the ability of a part to modify
frequency it operates at based on need, user preference, or other
factors. MPU DFS is supported in the kernel by the cpufreq driver. All
supported SoCs use the generic cpufreq driver. The frequency at which
the MPU operates is selected by a driver called a governor. Each
governor has a different strategy for selecting the most appropriate
frequency. The following governors are available within the kernel:

-  **ondemand**: This governor samples the load of the cpu and scales it
   up aggressively in order to provide the proper amount of processing
   power.
-  **conservative**: This governor is similar to ondemand but uses a
   less aggressive method of increasing the the OPP of the MPU.
-  **performance**: This governor statically sets the OPP of the MPU to
   the highest possible frequency.
-  **powersave**: This governor statically sets the OPP of the MPU to
   the lowest possible frequency.
-  **userspace**: This governor allows the user to set the desired OPP
   using any value found within scaling\_available\_frequencies by
   echoing it into scaling\_setspeed.
-  **schedutil**: This governor uses the Linux kernel scheduler utilization
   data to set the frequency.

More in depth documentation about each governor can be found in the
linux kernel documentation here:
https://www.kernel.org/doc/Documentation/cpu-freq/governors.txt

The kernel enables to cpufreq driver, and the ondemand, performance, and
userspace governors by default. The kernel enables the conservative and
powersave governors as modules. To make changes, use the following
instructions.

.. rubric:: Source Location

:file:`drivers/cpufreq/cpufreq-dt.c`

The OPP data itself is used by the cpufreq DT driver to scale frequencies
based on the governors.

.. rubric:: Kernel Configuration Options

The driver can be built into the kernel as a static module, dynamic
module, or both.

.. code-block:: console

   $ make menuconfig

Select CPU Power Management from the main menu.

.. code-block:: text

   ...
   Boot options --->
   Power management options  --->
   CPU Power Management --->
   ACPI (Advanced Configuration and Power Interface) Support  ----
   ...

Select CPU Frequency Scaling as shown here:

.. code-block:: text

   CPU Idle  --->
   CPU Frequency scaling  --->

All relevant options are listed below:

.. code-block:: text

   [*] CPU Frequency scaling
   [*]   CPU frequency transition statistics
         Default CPUFreq governor (performance)  --->
   -*-   'performance' governor
   <M>   'powersave' governor
   <*>   'userspace' governor for userspace frequency scaling
   <*>   'ondemand' cpufreq policy governor
   <M>   'conservative' cpufreq governor
   [ ]   'schedutil' cpufreq policy governor
   *** CPU frequency scaling drivers ***
   <*>   Generic DT based cpufreq driver
   -*-   Generic DT based cpufreq platdev driver
   <*>   SCMI based CPUfreq driver
   [*]   Texas Instruments CPUFreq support
      ...

.. ifconfig:: CONFIG_part_variant in ('J7200')

   .. rubric:: DT Configuration

   The clock information and the operating-points table need to be added as
   given in the example below.

   .. code-block:: dts

      /* From arch/arm64/boot/dts/ti/k3-j7200.dtsi */

      cpus {
                #address-cells = <1>;
                #size-cells = <0>;
                cpu-map {
                        cluster0: cluster0 {
                                core0 {
                                        cpu = <&cpu0>;
                                };

                                core1 {
                                        cpu = <&cpu1>;
                                };
                        };

                };

                cpu0: cpu@0 {
                        compatible = "arm,cortex-a72";
                        reg = <0x000>;
                        device_type = "cpu";
                        enable-method = "psci";
                        i-cache-size = <0xc000>;
                        i-cache-line-size = <64>;
                        i-cache-sets = <256>;
                        d-cache-size = <0x8000>;
                        d-cache-line-size = <64>;
                        d-cache-sets = <256>;
                        next-level-cache = <&L2_0>;
                        clocks = <&k3_clks 202 2>;
                        clock-names = "cpu";
                        operating-points-v2 = <&cpu0_opp_table>;
                        #cooling-cells = <2>; /* min followed by max */
                };

                cpu1: cpu@1 {
                        compatible = "arm,cortex-a72";
                        reg = <0x001>;
                        device_type = "cpu";
                        enable-method = "psci";
                        i-cache-size = <0xc000>;
                        i-cache-line-size = <64>;
                        i-cache-sets = <256>;
                        d-cache-size = <0x8000>;
                        d-cache-line-size = <64>;
                        d-cache-sets = <256>;
                        next-level-cache = <&L2_0>;
                        operating-points-v2 = <&cpu0_opp_table>;
                        #cooling-cells = <2>; /* min followed by max */
                        clocks = <&k3_clks 203 0>;
                        clock-names = "cpu";
                };
      };

.. rubric:: Driver Usage

All of the standard governors are built-in to the kernel, and by default
the performance governor is selected. Performance governor sets the CPU
statically to the highest frequency within the borders of scaling_min_freq
and scaling_max_freq.

To view available governors,

.. code-block:: console

   $ cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors
   conservative userspace powersave ondemand performance

To view current governor,

.. code-block:: console

   $ cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
   ondemand

To set a governor,

.. code-block:: console

   $ echo userspace > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

To view current OPP (frequency in kHz)

.. code-block:: console

   $ cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
   2000000000

To view supported OPP's (frequency in kHz),

.. ifconfig:: CONFIG_part_variant in ('J7200')

   .. code-block:: console

      $ cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies
      750000000 1000000000 1500000000 2000000000

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX', 'J722S')

   .. code-block:: console

      $ cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies
      200000 400000 600000 800000 1000000 1250000 1400000

To change OPP (can be done only for userspace governor. If governors
like ondemand is used, OPP change happens automatically based on the
system load)

.. code-block:: console

   $ echo 1000000000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed

|

.. rubric:: Operating Points
   :name: operating-points

Design: OPP term is derived from the usage in DVFS where they are a
pair of voltage frequency value. To keep compatibility with the DVFS
system, DFS uses same OPP tables with the voltages removed from the
table.

.. ifconfig:: CONFIG_part_variant in ('J7200')

   .. code-block:: dts

      /* From arch/arm64/boot/dts/ti/k3-j7200.dtsi */

      cpu0_opp_table: opp-table {
              compatible = "operating-points-v2";

              opp4-2000000000 {
                      opp-hz = /bits/ 64 <2000000000>;
              };

              opp3-1500000000 {
                      opp-hz = /bits/ 64 <1500000000>;
              };

              opp2-1000000000 {
                      opp-hz = /bits/ 64 <1000000000>;
              };

              opp1-750000000 {
                      opp-hz = /bits/ 64 <750000000>;
              };
      };

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   The OPP table defined in the following files
   allows defining of a different set of OPPs for each different SoC:

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      :file:`arch/arm64/boot/dts/ti/k3-am625.dtsi`

   .. ifconfig:: CONFIG_part_variant in ('AM62AX')

      :file:`arch/arm64/boot/dts/ti/k3-am62a7.dtsi`

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      :file:`arch/arm64/boot/dts/ti/k3-am62p5.dtsi`

   .. code-block:: dts

      a53_opp_table: opp-table {
              compatible = "operating-points-v2-ti-cpu";
              opp-shared;
              syscon = <&wkup_conf>;

              opp-200000000 {
                      opp-hz = /bits/ 64 <200000000>;
                      opp-supported-hw = <0x01 0x0007>;
                      clock-latency-ns = <6000000>;
              };

              opp-400000000 {
                      opp-hz = /bits/ 64 <400000000>;
                      opp-supported-hw = <0x01 0x0007>;
                      clock-latency-ns = <6000000>;
              };

              opp-600000000 {
                      opp-hz = /bits/ 64 <600000000>;
                      opp-supported-hw = <0x01 0x0007>;
                      clock-latency-ns = <6000000>;
              };

              opp-800000000 {
                      opp-hz = /bits/ 64 <800000000>;
                      opp-supported-hw = <0x01 0x0007>;
                      clock-latency-ns = <6000000>;
              };

              opp-1000000000 {
                      opp-hz = /bits/ 64 <1000000000>;
                      opp-supported-hw = <0x01 0x0006>;
                      clock-latency-ns = <6000000>;
              };

              opp-1250000000 {
                      opp-hz = /bits/ 64 <1250000000>;
                      opp-supported-hw = <0x01 0x0004>;
                      clock-latency-ns = <6000000>;
                      opp-suspend;
              };
      };

   .. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX')

      The maximum OPP for A53 requires VDD_CORE to be at 0.85V.
      It is enabled in the board-specific dts file:

      .. ifconfig:: CONFIG_part_variant in ('AM62X')

         :file:`arch/arm64/boot/dts/ti/k3-am625-sk.dts`

      .. ifconfig:: CONFIG_part_variant in ('AM62PX')

         :file:`arch/arm64/boot/dts/ti/k3-am62p5-sk.dts`

      .. code-block:: dts

          opp-table {
                          opp-1400000000 {
                                  opp-hz = /bits/ 64 <1400000000>;
                                  opp-supported-hw = <0x01 0x0004>;
                                  clock-latency-ns = <6000000>;
                          };
                  };

   To disable any of the above OPP's one can simply add

   .. code-block:: dts

      status = "disabled";

   to the corresponding DT Node.

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   To enable maximum clock rates for A53 and C7x on AM62A7-SK Rev E3
   board, an overlay has to be used as shown below:

   .. code-block:: console

      setenv name_overlays ti/k3-am62a7-sk-e3-max-opp.dtbo

   This overlay adds the 1.4 GHz OPP for A53 cores and disables all
   the lower OPPs. It also overrides the clock rate for C7x to 1 GHz.

   **Please note: This overlay is meant only for AM62A7-SK Rev E3 boards
   that have VDD_CORE at 0.85V. Board Rev E1 and E2 do not meet this
   requirement.** Any other boards based on this design should verify
   that they have the right silicon variant and the right power tree
   before booting with this overlay.
