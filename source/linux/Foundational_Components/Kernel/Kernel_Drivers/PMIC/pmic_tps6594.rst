.. http://processors.wiki.ti.com/index.php/Linux_Core_PMIC_TPS6594_User%27s_Guide

TPS6594 PMIC
---------------------------------

Introduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TPS6594 is a Power Management IC which provides regulators (bucks and LDOs)
and others features like GPIOs, RTC, watchdog, ESMs (Error Signal Monitor),
and PFSM (Pre-configurable Finite State Machine). The SoC and the PMIC can
communicate through the I2C or SPI interfaces.
TPS6594 is the super-set device while TPS6593 and LP8764 are derivatives.

This guide covers TPS6594/TPS6593/LP8764 PMIC drivers.

At least one of the two interfaces should be selected : either I2C or SPI driver.
The others drivers are sub-modules and may be selected or not, depending on the
application.

.. rubric:: Supported boards (using I2C interface)
   :name: supported-boards

.. code-block:: text

    AM62A SK EVM -> 1 TPS6593
    J721E EVM    -> 2 TPS6594
    J721S2 EVM   -> 2 TPS6594 + 1 LP8764
    J7200 EVM    -> 1 TPS6594 + 1 LP8764
    J784S4 EVM   -> 1 TPS6594

Device tree configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See device tree binding:

.. code-block:: text

    Documentation/devicetree/bindings/mfd/ti,tps6594.yaml

TPS6594 I2C driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Driver source location:

.. code-block:: text

    drivers/mfd/tps6594-i2c.c

.. rubric:: Kernel configuration options
   :name: kernel-configuration-options-i2c

Configs to be enabled in kernel:

.. code-block:: text

    CONFIG_I2C
    CONFIG_MFD_TPS6594_I2C (TPS6594 I2C support)

::

   Device Drivers --->
      Multifunction device drivers --->
         <*> TI TPS6594 Power Management chip with I2C

.. rubric:: CRC feature
   :name: crc-feature-i2c

.. rubric:: - When drivers are built as ‘modules’
   :name: crc-feature-i2c-modules

For safety applications, a CRC feature can be enabled from userspace:

.. code-block:: bash

    echo "options tps6594_i2c enable_crc=true" > /etc/modprobe.d/tps6594.conf; sync;

Then, the board must be powered off/on with the mechanical switch to apply
the new setting.

CRC feature will be enabled at module loading. Example of kernel messages
for J721S2:

.. code-block:: text

    [    5.060454] tps6594 0-0048: CRC feature enabled on primary PMIC
    [    5.086440] tps6594 0-004c: CRC feature enabled on secondary PMIC
    [    5.115762] tps6594 0-0058: CRC feature enabled on secondary PMIC

To disable CRC feature, the modprobe conf file must be removed:

.. code-block:: bash

    rm /etc/modprobe.d/tps6594.conf; sync;

Then, the board must be powered off/on with the mechanical switch to apply
the new setting.

.. rubric:: - When drivers are built statically into the kernel (‘built-in’)
   :name: crc-feature-i2c-builtin

CRC feature can be enabled through the kernel command line parameter:

.. code-block:: bash

    tps6594_i2c.enable_crc=Y

If the kernel command line is edited from uboot, the new setting can be
saved to the persistent storage:

.. code-block:: bash

    saveenv

TPS6594 SPI driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Driver source location:

.. code-block:: text

    drivers/mfd/tps6594-spi.c

.. rubric:: Kernel configuration options
   :name: kernel-configuration-options-spi

Configs to be enabled in kernel:

.. code-block:: text

    CONFIG_SPI_MASTER
    CONFIG_MFD_TPS6594_SPI (TPS6594 SPI support)

::

   Device Drivers --->
      Multifunction device drivers --->
         <*> TI TPS6594 Power Management chip with SPI

.. rubric:: CRC feature
   :name: crc-feature-spi

For safety applications, a CRC feature can be enabled (see 'TPS6594 I2C
driver' chapter).

TPS6594 GPIO/pinctrl driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The TPS6594 device integrates 11 configurable general-purpose I/Os that are
multiplexed with alternative functions.

Driver source location:

.. code-block:: text

    drivers/pinctrl/pinctrl-tps6594.c

[WARNING] GPIO indexation is 0-based in linux, whereas it is 1-based in the
PMIC TRM. So GPIO5 in linux corresponds to GPIO6 in the TRM.

.. rubric:: Kernel configuration options
   :name: kernel-configuration-options-gpio-pinctrl

Configs to be enabled in kernel:

.. code-block:: text

    CONFIG_PINCTRL_TPS6594 (TPS6594 GPIO support)

::

   Device Drivers --->
      Pin controllers --->
         <*> Pinctrl and GPIO driver for TI TPS6594 PMIC

.. rubric:: Driver usage (inputs - outputs)
   :name: driver-usage-inputs-outputs

Examples given for AM62A.

List all gpiochips present on the system, their names, labels and number
of GPIO lines:

.. code-block:: bash

    gpiodetect

        [...]
        gpiochip4 [tps6594-gpio] (11 lines)

List all lines of specified gpiochips, their names, consumers, direction,
active state and additional flags:

.. code-block:: bash

    gpioinfo gpiochip4

        gpiochip4 - 11 lines:
            line   0:      unnamed       unused   input  active-high
            line   1:      unnamed       unused   input  active-high
            line   2:      unnamed       unused   input  active-high
            line   3:      unnamed       unused  output  active-high
            line   4:      unnamed       unused   input  active-high
            line   5:      unnamed       unused  output  active-high
            line   6:      unnamed       unused   input  active-high
            line   7:      unnamed       unused   input  active-high
            line   8:      unnamed       unused   input  active-high
            line   9:      unnamed       unused   input  active-high
            line  10:      unnamed       unused   input  active-high

Read values of specified GPIO lines:

.. code-block:: bash

    gpioget gpiochip4 5

        0

Set values of specified GPIO lines:

.. code-block:: bash

    gpioset gpiochip4 5=1

.. rubric:: Driver usage (pinctrl)
   :name: driver-usage-pinctrl

Examples given for AM62A.

Get functions available for each pin:

.. code-block:: bash

    cat /sys/kernel/debug/pinctrl/tps6594-pinctrl.1.auto/pinmux-functions

        function 0: gpio, groups = [ GPIO0 GPIO1 GPIO2 GPIO3 GPIO4 GPIO5 GPIO6 GPIO7 GPIO8 GPIO9 GPIO10 ]
        function 1: nsleep1, groups = [ GPIO0 GPIO1 GPIO2 GPIO3 GPIO4 GPIO5 GPIO6 GPIO7 GPIO8 GPIO9 GPIO10 ]
        function 2: nsleep2, groups = [ GPIO0 GPIO1 GPIO2 GPIO3 GPIO4 GPIO5 GPIO6 GPIO7 GPIO8 GPIO9 GPIO10 ]
        function 3: wkup1, groups = [ GPIO0 GPIO1 GPIO2 GPIO3 GPIO4 GPIO5 GPIO6 GPIO7 GPIO8 GPIO9 GPIO10 ]
        function 4: wkup2, groups = [ GPIO0 GPIO1 GPIO2 GPIO3 GPIO4 GPIO5 GPIO6 GPIO7 GPIO8 GPIO9 GPIO10 ]
        function 5: scl_i2c2-cs_spi, groups = [ GPIO0 GPIO1 ]
        function 6: nrstout_soc, groups = [ GPIO0 GPIO10 ]
        function 7: trig_wdog, groups = [ GPIO1 GPIO10 ]
        function 8: sda_i2c2-sdo_spi, groups = [ GPIO1 ]
        function 9: clk32kout, groups = [ GPIO2 GPIO3 GPIO7 ]
        function 10: nerr_soc, groups = [ GPIO2 ]
        function 11: sclk_spmi, groups = [ GPIO4 ]
        function 12: sdata_spmi, groups = [ GPIO5 ]
        function 13: nerr_mcu, groups = [ GPIO6 ]
        function 14: syncclkout, groups = [ GPIO7 GPIO9 ]
        function 15: disable_wdog, groups = [ GPIO7 GPIO8 ]
        function 16: pdog, groups = [ GPIO8 ]
        function 17: syncclkin, groups = [ GPIO9 ]

Modify the function for a pin:

.. code-block:: bash

    echo "<group> <function>" > /sys/kernel/debug/pinctrl/tps6594-pinctrl.1.auto/pinmux-select

    Examples:
    echo "GPIO7 gpio" > /sys/kernel/debug/pinctrl/tps6594-pinctrl.1.auto/pinmux-select
    echo "GPIO2 nerr_soc" > /sys/kernel/debug/pinctrl/tps6594-pinctrl.1.auto/pinmux-select

TPS6594 regulator driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The TPS6594 provides regulators (bucks and LDOs). The output voltages are
configurable and are meant to supply power to the main processor and other
components. Bucks can be used in single or multiphase mode, depending on
the PMIC part number.

Driver source location:

.. code-block:: text

    drivers/regulator/tps6594-regulator.c

.. rubric:: Kernel configuration options
   :name: kernel-configuration-options-regul

Configs to be enabled in kernel:

.. code-block:: text

    CONFIG_REGULATOR_TPS6594 (TPS6594 regulator support)

::

   Device Drivers --->
      Voltage and Current Regulator Support --->
         <*> TI TPS6594 Power regulators

.. rubric:: Driver usage
   :name: driver-usage-regul

Regulator summary can be displayed:

.. code-block:: bash

    cat /sys/kernel/debug/regulator/regulator_summary

Regulator events, if any, can be seen by running this command:

.. code-block:: bash

    cat /proc/interrupts

TPS6594 ESM driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This device monitors the SoC error output signal at its nERR_SOC input pin.
In error condition, ESM toggles its nRSTOUT_SOC pin to reset the SoC.

Typically, Error Signal Monitor (on PMIC side) can be set up along with
Error Signaling Module (on SoC side).

Driver source location:

.. code-block:: text

    drivers/misc/tps6594-esm.c

.. rubric:: Kernel configuration options
   :name: kernel-configuration-options-esm

Configs to be enabled in kernel:

.. code-block:: text

    CONFIG_TPS6594_ESM (TPS6594 ESM support)

::

   Device Drivers --->
      Misc devices --->
         <*> TI TPS6594 Error Signal Monitor support

.. rubric:: Driver usage
   :name: driver-usage-esm

PMIC ESM will be started at module loading.

ESM errors, if any, can be seen by running this command:

.. code-block:: bash

    cat /proc/interrupts

TPS6594 RTC driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Driver source location:

.. code-block:: text

    drivers/rtc/rtc-tps6594.c

.. rubric:: Kernel configuration options
   :name: kernel-configuration-options-rtc

Configs to be enabled in kernel:

.. code-block:: text

    CONFIG_RTC_DRV_TPS6594 (TPS6594 RTC support)

::

   Device Drivers --->
      Real Time Clock --->
         <*> TI TPS6594 RTC driver

.. rubric:: Driver usage
   :name: driver-usage-rtc

Once the module is loaded, each RTC is exposed as a character
device file by the kernel to be used by userspace:

.. code-block:: text

    /dev/rtcX		X - index (zero-based)

Read date/time as follow:

.. code-block:: bash

    cat /sys/class/rtc/rtc0/date
    cat /sys/class/rtc/rtc0/time

Alarms, if any, can be seen by running this command:

.. code-block:: bash

    cat /proc/interrupts

An example of how to use RTC from a userspace application is given
in PFSM driver chapter.

TPS6594 PFSM driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Strictly speaking, PFSM is not hardware. It is a piece of code.
PMIC integrates a state machine which manages operational modes.
Depending on the current operational mode, some voltage domains
remain energized while others can be off.

PFSM driver can be used to trigger transitions between configured
states.

Driver source location:

.. code-block:: text

    drivers/misc/tps6594-pfsm.c

.. rubric:: Kernel configuration options
   :name: kernel-configuration-options-pfsm

Configs to be enabled in kernel:

.. code-block:: text

    CONFIG_TPS6594_PFSM (TPS6594 PFSM support)

::

   Device Drivers --->
      Misc devices --->
         <*> TI TPS6594 Pre-configurable Finite State Machine support

.. rubric:: Driver usage
   :name: driver-usage-pfsm

Once the module is loaded, each PFSM is exposed as a character
device file by the kernel to be used by userspace:

.. code-block:: text

    /dev/pfsm-X-Y       X - chip ID
                            [0] = TPS6594
                            [1] = TPS6593
                            [2] = LP8764

                        Y - I2C address or SPI chip select

    Example: '/dev/pfsm-1-0x4c' is TPS6593 @ I2C address 0x4c

Dump the registers of pages 0 and 1 as follow:

.. code-block:: bash

    hexdump -C /dev/pfsm-1-0x4c

PFSM events, if any, can be seen by running this command:

.. code-block:: bash

    cat /proc/interrupts

For more information, see kernel documentation:

.. code-block:: text

    Documentation/misc-devices/tps6594-pfsm.rst

A userspace code example is also provided:

.. code-block:: text

    samples/pfsm
