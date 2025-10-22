####
DVFS
####

.. rubric:: Overview

Dynamic voltage and frequency scaling, or DVFS as it is commonly known,
is the ability of a part to modify both the voltage and frequency it
operates at based on need, user preference, or other factors. MPU DVFS
is supported in the kernel by the cpufreq driver. All supported SoCs use
the generic cpufreq-cpu0 driver. The frequency at which the MPU operates
is selected by a driver called a governor. Each governor has a different
strategy for selecting the most appropriate frequency. The following
governors are available within the kernel:

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

More in depth documentation about each governor can be found in the
linux kernel documentation here:
https://www.kernel.org/doc/Documentation/cpu-freq/governors.txt

By default, cpufreq, the cpufreq-cpu0 driver, and all of the standard
governors are enabled with the ondemand governor selected as the default
governor. To make changes, follow the instructions below.

.. rubric:: Source Location

drivers/cpufreq/ti-cpufreq.c drivers/cpufreq/cpufreq-dt.c

TI cpufreq driver uses efuse information to scale the OPP data based on
silicon characteristics. The OPP data itself is used by the cpufreq DT
driver to scale voltages based on frequency changes for the CPU.

.. rubric:: Kernel Configuration Options

The driver can be built into the kernel as a static module, dynamic
module, or both.

$ make menuconfig

Select CPU Power Management from the main menu.

.. code-block:: menuconfig

   ...
   ...
   Boot options --->
   CPU Power Management --->
   Floating point emulation --->
   ...

Select CPU Frequency Scaling as shown here:

.. code-block:: menuconfig

   ...
   ...
       CPU Frequency Scaling --->
   [*] CPU idle PM support
   ...

All relevant options are listed below:

.. code-block:: menuconfig

   [*] CPU Frequency scaling
   <*>   CPU frequency translation statistics
   [*]     CPU frequency translation statistics details
         Default CPUFreq governor (userspace)  --->
   <*>   'performance' governor
   <*>   'powersave' governor
   -*-   'userspace' governor for userspace frequency scaling
   <*>   'ondemand' cpufreq policy governor
   <*>   'conservative' cpufreq governor
         *** CPU frequency scaling drivers ***
   <M>   Generic DT based cpufreq driver
   <M>   Generic DT based cpufreq driver using clk notifiers
   <*>    Texas Instruments CPUFreq support
   ...

.. rubric:: DT Configuration

The clock information and the operating-points table need to be added as
given in the example below. The voltage source needs to be hooked to the
cpu0 node. As given below cpu0-supply needs to be mapped to the right
regulator node by looking at the schematics.

.. code-block:: dts

   /* From arch/arm/boot/dts/am4372.dtsi */

   cpus {
      #address-cells = <1>;
      #size-cells = <0>;
      cpu: cpu@0 {
         compatible = "arm,cortex-a9";
         enable-method = "ti,am4372";
         device_type = "cpu";
         reg = <0>;

         clocks = <&dpll_mpu_ck>;
         clock-names = "cpu";

         operating-points-v2 = <&cpu0_opp_table>;
         ti,syscon-efuse = <&scm_conf 0x610 0x3f 0>;
         ti,syscon-rev = <&scm_conf 0x600>;

         clock-latency = <300000>; /* From omap-cpufreq driver */
      };
   };

   /* From arch/arm/boot/dts/am437x-gp-evm.dts */

   &cpu {
      cpu0-supply = <&dcdc2>;
   };

The ``operating-points`` table has been introduced instead of
arch/arm/mach-omap2/oppXXXX\_data.c files for each platform that define
OPPs for each silicon revision. More information can be found in the
`Operating Points <#operating-points>`__ section.

.. rubric:: Driver Usage

All of the standard governors are built-in to the kernel, and by default
the ondemand governor is selected.

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
   720000

To view supported OPP's (frequency in kHz),

.. code-block:: console

   $ cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies
   275000 500000 600000 720000

To change OPP (can be done only for userspace governor. If governors
like ondemand is used, OPP change happens automatically based on the
system load)

.. code-block:: console

   $ echo 275000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed

|

.. rubric:: Operating Points
   :name: operating-points

Design: OPP is a pair of voltage frequency value. When scaling from High
OPP to Low OPP Frequency is reduced first and then the voltage. When
scaling from a lower OPP to Higher OPP we scale the voltage first and
then the frequency.

The OPP platform data defined in arch/arm/mach-omap2/oppXXXX\_data.c has
been replaced by the TI cpufreq driver OPP modification code and the OPP
tables in the DT files. These files allow defining of a different set of
OPPs for each different SoC, and also selective, automatic enabling
based on what is detected to be supported by the specific SoC in use.

.. code-block:: dts

   /* From arch/arm/boot/dts/am4372.dtsi */

   cpu0_opp_table: opp_table0 {
      compatible = "operating-points-v2";

      opp50@300000000 {
         opp-hz = /bits/ 64 <300000000>;
         opp-microvolt = <950000 931000 969000>;
         opp-supported-hw = <0xFF 0x01>;
         opp-suspend;
      };

      opp100@600000000 {
         opp-hz = /bits/ 64 <600000000>;
         opp-microvolt = <1100000 1078000 1122000>;
         opp-supported-hw = <0xFF 0x04>;
      };

      opp120@720000000 {
         opp-hz = /bits/ 64 <720000000>;
         opp-microvolt = <1200000 1176000 1224000>;
         opp-supported-hw = <0xFF 0x08>;
      };

      oppturbo@800000000 {
         opp-hz = /bits/ 64 <800000000>;
         opp-microvolt = <1260000 1234800 1285200>;
         opp-supported-hw = <0xFF 0x10>;
      };

      oppnitro@1000000000 {
         opp-hz = /bits/ 64 <1000000000>;
         opp-microvolt = <1325000 1298500 1351500>;
         opp-supported-hw = <0xFF 0x20>;
      };
   };

To implement Dynamic Frequency Scaling (DFS), the voltages in the table
can be changed to the same fixed value to avoid any voltage scaling from
taking place if the system has been designed to use a single voltage.
