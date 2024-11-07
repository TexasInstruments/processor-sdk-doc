.. http://processors.wiki.ti.com/index.php/AM335x_Power_Management_User_Guide

AM335x Power Management User Guide
------------------------------------

.. rubric:: Overview
   :name: overview-am335x-pm

This article provides a description of the example applications under
the Power page of the Matrix application that comes with the Sitara
SDK.  This page is labled "Power" in the top-level Matrix GUI. The
location of the Power icon on the main Matrix app list may be different
than shown here, depending on screen size. (Screen shots from SDK 06.00)

|

.. Image:: /images/Matrix_app_launcher.png

|

| PLEASE NOTE: cpufreq may cause I2C lockups on AM335x EVM boards.
  Beaglebone is not affected. This is a known issue related to the CPLD
  firmware. If the CPLD firmware on your EVM is detected to be the wrong
  version, the Matrix application output will inform you of the version
  mismatch and continue.
| Once updated CPLD firmware is available, this documentation will be
  updated to teach users how to upgrade their CPLD if necessary/desired.
  This procedure will require an Altera programming pod.

.. rubric:: Power Examples
   :name: power-examples

Several power examples exist to provide users the ability to dynamically
switch the CPU clock frequency. The frequencies shown are those
available for your system. Upon making a selection, you will be
presented a confirmation page. The readout number "BogoMIPS" will
confirm the new clock frequency. Please note that the frequency will
read out with a slight margin compare to the intended frequency. For
example, if you select 1GHz, you may see a number like 998.84 (in MHz).
This is normal. After reviewing the confirmation page, press the Close
button to return to normal Matrix operation.

Other power examples are provided which may be useful for power
management developers and power users. These have been included in
Matrix in part to make users aware that these valuable debugging tools
exist, in addition to the convenience of executing each application from
the GUI. In depth descriptions for each application follow. Similar
descriptions are also given via description pages in Matrix, which will
be displayed when clicking the button. Where appropriate, the
documentation will point out the corresponding command line operation.

The Suspend/Resume button demonstrates the ability to put the machine
into a suspended state. See below for complete documentation of this
feature.

Please note that the order of applications which appear on your screen
may differ from the picture below, due to devices with different screen
sizes, and differences between different versions of Matrix. Screen shot
is from SDK 06.00.

|

.. Image:: /images/AM335x_Power_screen.png

|

.. rubric:: Set Frequency
   :name: set-frequency

This command opens up another screen from which you choose the frequency
based on the available frequencies on the board. Here is a picture of
the screen you will see:

|

.. Image:: /images/AM335x_matrix_set_frequency.png

|

The following are the Linux command line equivalents for selecting the
operating frequency. Please note that changing the frequency also
changes the MPU voltage accordingly. The commands are part of the
"cpufreq" kernel interface for selecting the OPP (operating performance
point). Cpufreq provides an opportunity to save power by
adjusting/scaling voltage and frequency based on the current cpu load.

::

     (command line equivalent)
    cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies
    (view options, select one for next step)
    echo <selected frequency, in KHz> > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed
    cat /proc/cpuinfo

.. rubric:: Suspend/Resume
   :name: suspendresume

::

     (command line equivalent)
    mkdir /debug
    mount -t debugfs debugfs /debug
    echo mem > /sys/power/state

| This command sequence will put the platform into suspend mode. The
  final command initiates the suspend.

| IMPORTANT NOTE: When running this from Matrix, the system will only
  properly resume if the user sends a keypress to the UART. If the user
  presses the touchscreen or a button on the EVM, resume will not
  complete normally. This issue will be fixed in a future release. If
  you run these commands from the terminal - all of the normal wakeup
  events (UART keypress, touchscreen press, EVM keypad press) will
  operate correctly.

.. rubric:: SmartReflex
   :name: smartreflex

SmartReflex is an active power management technique which optimizes
voltage based on silicon process ("hot" vs. "cold" silicon),
temperature, and silicon degradation effects. In most cases, SmartReflex
provides significant power savings by lowering operating voltage.

On AM335x, SmartReflex is enabled by default in Sitara SDK releases
since 05.05.00.00. Please note that the kernel configuration menu
presents two options: "AM33XX SmartReflex support" and "SmartReflex
support". For AM33XX SmartReflex, you must select "AM33XX SmartReflex
support", and ensure that the "SmartReflex support" option is disabled.
The latter option is intended for AM37x and OMAP3 class devices.

The SmartReflex driver requires the use of either the TPS65217 or
TPS65910 PMIC. Furthermore, SmartReflex is currently supported only on
the ZCZ package. Please note that SmartReflex may not operate on AM335x
sample devices which were not programmed with voltage targets. To
disable SmartReflex, type the following commands at the target terminal:

::

    mkdir /debug
    mount -t debugfs debugfs /debug
    cd /debug/smartreflex   ==> NOTE: You may not see 'smartreflex' node if you have early silicon.  In this case SmartReflex operation is not possible.
    echo 0 > autocomp
    (Performing "echo 1 > autocomp" will re-enable SmartReflex)

On AM335x, to compile SmartReflex support out of the kernel, follow this
procedure to modify the kernel configuration:

::

    cd <kernel source directory>
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- menuconfig
    <the menuconfig interface should appear>
    Select "System Type"
    Select "TI OMAP Common Features"
    Deselect "AM33xx SmartReflex Support"
    Select "Exit" until you are prompted to save the configuration changes, and save them.
    Rebuild the kernel.

.. rubric:: Dynamic Frequency Scaling
   :name: dynamic-frequency-scaling

This feature, which can be enabled via patch to the SDK, enables scaling
frequency INDEPENDENT of voltage. It is also referred to as DFS (as in
DVFS without the 'V').

`Media:0001-Introduce-dynamic-frequency-scaling.patch <http://processors.wiki.ti.com/images/f/f3/0001-Introduce-dynamic-frequency-scaling.patch>`__

.. rubric:: Discussion
   :name: discussion

Certain systems are unable to scale voltage, either because they employ
a fixed voltage regulator, or use the ZCE package of AM335x. Without
being able to scale voltage, the power savings enabled via DVFS are
lost. This is because the current version of the omap-cpufreq driver
requires a valid MPU voltage regulator in order to operate. The purpose
of this DFS feature is to enable additional power savings for systems
with these sort of limitations.

When using the ZCE package of AM335x, the CORE and MPU voltage domains
are tied together. Due to Advisory 1.0.22, you are not allowed to
dynamically modify the CORE frequency/voltage because the EMIF cannot
support it. However, to achieve maximum power savings, it may still be
desirable to use a PMIC which supports dynamic voltage scaling, in order
to use Adaptive Voltage Scaling (aka SmartReflex or AVS). This
implementation of DFS does not affect the ability of AVS to optimize the
voltage and save additional power.

.. rubric:: Using the patch
   :name: using-the-patch

The patch presented here has been developed for and tested on the SDK
05.07. It modifies the omap-cpufreq driver to operate without requiring
a valid MPU voltage regulator. From a user perspective, changing
frequency via cpufreq is accomplished with exactly the same commands as
typical DVFS. For example, switching to 300 MHz is accomplished with the
following command:

::

    echo 300000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed

After applying the patch, the user must modify the kernel defconfig in
order to enable the DFS feature. You should also configure the "Maximum
supported DFS voltage" (shown below) to whatever the fixed voltage level
is for your system, in microvolts. For example, use the value 1100000 to
signify 1.1V. The software will use the voltage level that you specify
to automatically disable any Operating Performance Points (OPPs) which
have voltages above that level.

On AM335x, first apply the patch, then follow this procedure to modify
the kernel configuration:

::

    cd <kernel source directory>
    make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- menuconfig
    <the menuconfig interface should appear>
    Select "System Type"
    Select "TI OMAP Common Features"
    Select "Dynamic Frequency Scaling"
    Configure "Maximum supported DFS voltage (in microvolts)" (default is 1100000, or 1.1V)
    Select "Exit" until you are prompted to save the configuration changes, and save them.
    Rebuild the kernel.

.. rubric:: Power Savings
   :name: power-savings

-  Tested on a rev 1.2 EVM, running Linux at idle.
-  The delta between power consumption at 300MHz and 600MHz, with
   voltage unchanged, is approximately 75mW.

.. rubric:: Static CORE OPP 50
   :name: static-core-opp-50

Configuring the AM335x system to CORE OPP50 frequency and voltage is an
advanced power savings method that can be used, provided that you
understand the tradeoffs involved.

This patch, which was developed against the u-boot source tree from the
SDK 05.07, configures the bootloader to statically program the system to
CORE OPP50 voltage (0.95V) and frequencies. It also configures the MPU
to OPP50 voltage (0.95V) and frequency (300MHz). DDR2 is configured with
optimized timings to run at 125MHz.

Apply the following patch to your u-boot source tree and rebuild both
MLO and u-boot.img. (Refer to
`AM335x\_U-Boot\_User's\_Guide#Building\_U-Boot <http://processors.wiki.ti.com/index.php/AM335x_U-Boot_User%27s_Guide#Building_U-Boot>`__)

`Media:0001-Static-CORE-OPP50-w-DDR2-125MHz-MPU-300MHz.patch <http://processors.wiki.ti.com/images/c/ce/0001-Static-CORE-OPP50-w-DDR2-125MHz-MPU-300MHz.patch>`__

.. rubric:: Caveats
   :name: caveats

-  According to section 5.5.1 of the AM335x datasheet, operation of the
   Ethernet MAC and switch (CPSW) is NOT supported for CORE OPP50.

-  Note that MPU OPP50 operation is not supported for the 1.0 silicon
   revision (silicon errata Advisory 1.0.15).

-  Also be aware of Advisory 1.0.24, which states that boot may not be
   reliable because OPP100 frequencies are used by ROM at OPP50
   voltages.

-  DDR2 memory must be used (as on the AM335x EVM up to rev 1.2). DDR2
   memory timings must be modified to operate at 125MHz.

.. rubric:: Power Savings
   :name: power-savings-1

-  On an EVM (rev 1.2), active power consumption when Linux is idle for
   CORE and MPU rails was measured at 150mW. Using the out-of-the-box
   SDK at OPP100 (MPU and CORE), the comparable figure is 334mW.
-  Further savings are possible by disabling Ethernet drivers in the
   Linux defconfig. Refer to
   `AM335x\_CPSW\_(Ethernet)\_Driver's\_Guide#Driver\_Configuration <http://processors.wiki.ti.com/index.php/AM335x_CPSW_(Ethernet)_Driver%27s_Guide#Driver_Configuration>`__
   and disable "Ethernet driver support" to acheive additional power
   savings.

.. rubric:: Power Management Reference
   :name: power-management-reference

-  `AM335x Linux Power Management User
   Guide <http://processors.wiki.ti.com/index.php/AM335x_Linux_Power_Management_User_Guide>`__

Refer to this page for Linux specific information on AM335x devices.

-  `AM335x Power Estimation
   Tool <http://processors.wiki.ti.com/index.php/AM335x_Power_Estimation_Tool>`__

The Power Estimation Tool (PET) provides users the ability to gain
insight in to the power consumption of select Sitara processors.

-  `AM335x Power Consumption
   Summary <http://processors.wiki.ti.com/index.php/AM335x_Power_Consumption_Summary>`__

This document discusses the power consumption for common system
application usage scenarios for the AM335x ARM® Cortex™-A8
Microprocessors (MPUs).

-  `AM335x Power Management Standby User's
   Guide <http://processors.wiki.ti.com/index.php/AM335x_Power_Management_Standby_User%27s_Guide>`__

Standby for AM335x is a inactive (system suspended) power saving mode in
which the power savings achieved would be lesser than that achieved
through DeepSleep0 mode but with lesser resume latency and additional
wake-up sources.
