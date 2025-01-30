########
DM TIMER
########

- This guide covers a general overview on DM Timer, it supports DM Timers found on TI's
  |__PART_FAMILY_NAME__| SoC.

- Each timer comes with dedicated pins that can be used as timer capture inputs or as timer
  PWM outputs, please check the device TRM for more information.

- Each timer contains a free-running upward counter with autoreload capability on overflow.
  Each timer includes compare logic to allow an interrupt event on a programmable counter
  matching value. A dedicated output signal can be pulsed/toggled on an overflow or a match
  event. This offers time-stamp trigger signaling or PWM signal sources. A dedicated input
  signal can be used to trigger an automatic timer counter capture or an interrupt event on a
  programmable input signal transition.

- For more detailed information on timers, please refer to the: ``Peripherals/Timer Modules/Timers``
  section of the device specific TRM.

**************
Driver Sources
**************

- Driver source location: :file:`drivers/clocksource/ti,timer-dm.c`
- Binding source location: :file:`Documentation/device-tree/bindings/timer/ti,timer-dm.yaml`

*Enabling PWM output signals:*

- Driver source location: :file:`drivers/pwm/pwm-omap-dmtimer.c`
- Binding source location: :file:`Documentation/devicetree/bindings/pwm/pwm-omap-dmtimer.txt`

********************
Kernel Configuration
********************

Configs to be enabled in Linux Kernel:

.. code-block:: menuconfig

   Device Drivers --->
      -> Clock Source drivers
         -> OMAP dual-mode timer driver (OMAP_DM_TIMER [=y])

*Enabling PWM output signals:*

.. code-block:: menuconfig

   Device Drivers --->
      Pulse-Width Modulation (PWM) Support (PWM [=y])
         -> OMAP Dual-Mode Timer PWM support (PWM_OMAP_DMTIMER [=m])

.. rubric:: DTS node for DM Timer

In this example, we take am62x SK DT node as an example. In general all the timer nodes
should be described in its appropriate voltage domain .dtsi file, for example the following
node can be found in k3-am62-main.dtsi:

.. code-block:: dts

   main_timer3: timer@2430000 {
      compatible = "ti,am654-timer";
      reg = <0x00 0x2430000 0x00 0x400>;
      interrupts = <GIC_SPI 123 IRQ_TYPE_LEVEL_HIGH>;
      clocks = <&k3_clks 39 2>;
      clock-names = "fck";
      assigned-clocks = <&k3_clks 39 2>;
      assigned-clock-parents = <&k3_clks 39 3>;
      power-domains = <&k3_pds 39 TI_SCI_PD_EXCLUSIVE>;
      ti,timer-pwm;
   };

*Enabling PWM output signals:*

- The "ti,timer-pwm" DT attribute is required in the DM Timer node in order to enable PWM output
  signals.

An additional DT node is required in order to enable PWM output signals as shown below. The
``main_timer3_pins_default`` is also required and not listed here, use sysconfig tool to get
pinumux configuration.

.. code-block:: dts

   main_pwm3: dmtimer-main-pwm-3 {
      compatible = "ti,omap-dmtimer-pwm";
      #pwm-cells = <3>;
      ti,timers = <&main_timer3>;
      pinctrl-names = "default";
      pinctrl-0 = <&main_timer3_pins_default>;
   };

************
Driver Usage
************

For information on using DM timer as a counter, please refer to the detailed descriptions
in the TRM ``Timers Functional Description`` and ``Low-Level Programming Models`` under
``Peripherals/Timers Modules/Timers``.

   .. note::

      Currently there is no sysfs interface to interact with the DM Timer as a counter via userspace.

- Timers in "Timer" mode should be enabled by default in Linux DT.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX')

   In MAIN domain:
      - 8 DM timers in MAIN domain

   In MCU domain:
      - 4 DM timers in MCU domain

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   In MAIN domain:
      - 12 DM timers in MAIN domain

   In MCU domain:
      - 4 DM timers in MCU domain

*Enabling PWM output signals:*

If the PWM node exists in DT using a DM TIMER, the PWM device is probed and exposed as a
PWM device by Linux Kernel to be used by userspace in :file:`/sys/class/pwm`.

For controlling the PWM chip via sysfs interface please refer to the official Linux
documentation: `here <https://docs.kernel.org/driver-api/pwm.html#using-pwms-with-the-sysfs-interface>`__
or go to :ref:`Using-PWM-with-sysfs`.

********
Examples
********

To enable DM timer PWM output signals, there is an example DT overlay found in
:file:`arch/arm64/boot/dts/ti/k3-am62x-sk-dmtimer-pwm.dtso` that applies for am62x
family devices and can be referenced for other K3 devices.
