#######################
Enhanced capture (eCAP)
#######################

************
Introduction
************

eCAP is a dual-mode hardware module:

- **Auxiliary pulse-width modulator (APWM) Mode**: Generates pulse-width modulated (PWM) signals with configurable period and duty cycle
- **Capture Mode**: Records timestamp when input signal transitions occur, used for pulse measurement and event timing

*****************
Hardware overview
*****************

eCAP provides a 32-bit free-running counter with up to 4 capture event registers.
Key features include:

- Single PWM output channel (*APWM* mode)
- Up to 4 capture events per instance
- Counter overflow detection
- Configurable edge polarity (rising/falling)
- Programmable interrupt generation

****************
Device instances
****************

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX', 'AM62LX')

   |__PART_FAMILY_DEVICE_NAMES__| family provides 3 eCAP instances:

   - ecap0 @ 0x23100000
   - ecap1 @ 0x23110000
   - ecap2 @ 0x23120000

   Each instance is independently configurable for *APWM* or *Capture* mode.

.. ifconfig:: CONFIG_part_variant not in ('AM62X', 'AM62AX', 'AM62PX', 'AM62LX')

   Device instances documentation is pending for |__PART_FAMILY_DEVICE_NAMES__|,
   reach out to: `Help e2e <https://e2e.ti.com//>`__ for additional information.

*************
Linux drivers
*************

eCAP hardware module supports dual-mode operation. The DT compatible string determines
which driver loads for the eCAP instance. PWM compatible exposes the eCAP instance through
the PWM subsystem while capture compatible exposes the eCAP instance through the counter
subsystem. Both drivers are enabled by default in TI Linux kernel.

**APWM Mode:**

- Subsystem: `PWM <https://www.kernel.org/doc/html/latest/driver-api/pwm.html>`__
- DT Compatible: ``ti,am3352-ecap``
- Driver: :file:`drivers/pwm/pwm-tiecap.c`
- Menuconfig driver selection:

   .. code-block:: menuconfig

      Device Drivers --->
         <*> Pulse-Width Modulation (PWM) Support --->
            <*> ECAP PWM support

**Capture Mode:**

- Subsystem: `Counter <https://www.kernel.org/doc/html/latest/driver-api/generic-counter.html>`__
- DT Compatible: ``ti,am62-ecap-capture``
- Driver: :file:`drivers/counter/ti-ecap-capture.c`
- Menuconfig driver selection:

   .. code-block:: menuconfig

      Device Drivers --->
         <M> Counter support --->
            <M> TI eCAP capture driver

****************
Device tree node
****************

**APWM Mode:**

.. code-block:: dts

   ecap2: pwm@23120000 {
      compatible = "ti,am3352-ecap";
      #pwm-cells = <3>;
      reg = <0x00 0x23120000 0x00 0x100>;
      power-domains = <&k3_pds 53 TI_SCI_PD_EXCLUSIVE>;
      clocks = <&k3_clks 53 0>;
      clock-names = "fck";
      pinctrl-names = "default";
      pinctrl-0 = <&main_ecap2_pwm_pins_default>;
      status = "okay";
   };

**Capture Mode:**

.. code-block:: dts

   ecap2: pwm@23120000 {
      compatible = "ti,am62-ecap-capture";
      #pwm-cells = <3>;
      reg = <0x00 0x23120000 0x00 0x100>;
      power-domains = <&k3_pds 53 TI_SCI_PD_EXCLUSIVE>;
      clocks = <&k3_clks 53 0>;
      clock-names = "fck";
      interrupt-parent = <&gic500>;
      interrupts = <GIC_SPI 115 IRQ_TYPE_EDGE_RISING>;
      pinctrl-names = "default";
      pinctrl-0 = <&main_ecap2_capture_pins_default>;
      status = "okay";
   };

The ``pinctrl`` node is not included here. Refer to the TI device tree overlay for your
platform for an example of how to set ``pincltrl`` node for eCAP in *APWM* or *Capture* mode.

*****************
Pin configuration
*****************

TI Overlays set the following pin configuration for an eCAP instance in *APWM*
or *Capture* mode:

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX', 'AM62LX')

   **APWM Mode:**

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      PWM overlay: :file:`k3-am62x-sk-pwm.dtso`

         - eCAP0: J3 header : pin 26
         - eCAP1: J3 header : pin 38
         - eCAP2: J3 header : pin 11

   .. ifconfig:: CONFIG_part_variant in ('AM62AX')

      PWM overlay: :file:`k3-am62x-sk-pwm.dtso`

         - eCAP0: J3 header : pin 26
         - eCAP1: J3 header : pin 40
         - eCAP2: J3 header : pin 11

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      DTS: :file:`k3-am62p5-sk.dts` (no separate overlay)

         - eCAP1: J4 header : pin 36
         - eCAP2: J4 header : pin 11

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      PWM overlay: :file:`k3-am62l3-evm-pwm.dtso`

         - eCAP0: J2 header : pin 24
         - eCAP1: J2 header : pin 26
         - eCAP2: J3 header : pin 9

   **Capture Mode:**

   .. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX')

      Capture overlay: :file:`k3-am62x-ecap-capture.dtso`

         - eCAP2: J3 header : pin 11

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      Capture overlay: :file:`k3-am62p5-ecap-capture.dtso`

      - eCAP1: J4 header : pin 36
      - eCAP2: J4 header : pin 11

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      Capture overlay: :file:`k3-am62l3-ecap-capture.dtso`

      - eCAP2: J6 header : pin 2

   .. warning::

      Enabling eCAP pins may require disabling peripherals (UART, audio) that use the
      same pins as eCAP.

.. ifconfig:: CONFIG_part_variant not in ('AM62X', 'AM62AX', 'AM62PX', 'AM62L')

   eCAP pin configuration is not defined for this device variant. Please refer to the device
   datasheet for eCAP pin definitions and configure Linux device tree accordingly.

*********
APWM mode
*********

eCAP uses the standard PWM sysfs interface. See :ref:`PWM <Using_PWM_with_sysfs>` guide for
sysfs usage (export, period, duty cycle, polarity, enable).

**eCAP differences:**

- Single channel per instance (compared to 2 channels for ePWM)

************
Capture mode
************

*Capture* mode records input signal transitions. The module timestamps each edge and optionally
generates interrupts.

eCAP capture driver exposes counters through the generic counter sysfs interface at
:file:`/sys/bus/counter/devices/`.

**Verify counter device availability:**

.. code-block:: console

   $ ls /sys/bus/counter/devices/
   counter0  counter1  ...

**Identify eCAP device:**

.. code-block:: console

   $ cat /sys/bus/counter/devices/counter0/name
   ecap
   $ cat /sys/bus/counter/devices/counter0/uevent
   MAJOR=237
   MINOR=0
   DEVNAME=counter0
   DEVTYPE=counter_device
   OF_NAME=pwm
   OF_FULLNAME=/bus@f0000/pwm@23120000
   OF_COMPATIBLE_0=ti,am62-ecap-capture
   OF_COMPATIBLE_N=1

**Check counter0 attributes:**

.. code-block:: console

   $ ls /sys/bus/counter/devices/counter0/count0/
   capture0           function           signal0_action
   capture1           num_overflows      signal1_action
   capture2           ceiling            enable
   capture3           count              function_available

**Check function and signal actions:**

.. code-block:: console

   $ cat /sys/bus/counter/devices/counter0/count0/function
   increase
   $ cat /sys/bus/counter/devices/counter0/signal0/name
   Clock Signal
   $ cat /sys/bus/counter/devices/counter0/count0/signal0_action
   rising edge
   $ cat /sys/bus/counter/devices/counter0/signal1/name
   Input Signal
   $ cat /sys/bus/counter/devices/counter0/signal1/polarity0
   positive

- :file:`function`: Counter increments on clock signal
- :file:`signal0`: Clock signal driving counter with rising edge action
- :file:`signal1`: Action configurable input signal driving capture events
- :file:`polarity0`: Sets edge polarity for capture event on input signal

When the Input Signal :file:`signal1` edge detection occurs, eCAP automatically
captures the current :file:`count` (TSCNT) value to the next available capture
register. Configure capture event edge type through :file:`polarity0-3`.

**Check counter0 ceiling:**

.. code-block:: console

   $ cat /sys/bus/counter/devices/counter0/count0/ceiling
   4294967295

Note that 32 bit :file:`ceiling` is the maximum value of the counter.

**Enable capture:**

.. code-block:: console

   $ echo 1 > /sys/bus/counter/devices/counter0/count0/enable

**Read count:**

.. code-block:: console

   $ cat /sys/bus/counter/devices/counter0/count0/count
   1313052346

Note that :file:`count` (TSCNT) is a free-running timestamp counter that increments
from module clock according to clock signal action. Every rising increments the counter
by one.

**Read captured timestamps:**

.. code-block:: console

   $ cat /sys/bus/counter/devices/counter0/count0/capture[0-3]
   3008643764
   3008591266
   3008612306
   3008612768

On each edge, eCAP captures current counter value to circular buffer (4 registers):

   - :file:`capture0` (CEVT1): 1st edge timestamp
   - :file:`capture1` (CEVT2): 2nd edge timestamp
   - :file:`capture2` (CEVT3): 3rd edge timestamp
   - :file:`capture3` (CEVT4): 4th edge timestamp

On 5th edge, :file:`capture0` is overwritten with a new timestamp. On 6th edge,
:file:`capture1` is overwritten, and so on.

**Read overflow count:**

.. code-block:: console

   $ cat /sys/bus/counter/devices/counter0/count0/num_overflows
   2

Attribute :file:`num_overflows` increments when counter wraps around
(0xFFFFFFFF -> 0x00000000).

**Disable capture:**

.. code-block:: console

   $ echo 0 > /sys/bus/counter/devices/counter0/count0/enable

********************
Troubleshooting eCAP
********************

**Verify PWM functionality:**

See troubleshooting in :ref:`PWM <troubleshoot_the_pwm_setup>` guide and monitor eCAP PWM
through :file:`/sys/kernel/debug/pwm`.

**Verify Capture mode enumeration:**

.. code-block:: console

   $ cat /sys/bus/counter/devices/counterX/name

If not present, verify the overlay applied and check for pin conflicts reported in ``dmesg`` log.

**Verify capture interrupts are firing:**

.. code-block:: console

   $ cat /proc/interrupts | grep pwm
   409:      36506          0          0          0    GICv3 147 Edge      23120000.pwm

Interrupt count will increment on each capture event or overflow. A high count on
the active signal indicates interrupts are working correctly.
