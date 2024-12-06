PRU-ICSSG PWM
-------------

.. rubric:: Introduction

The PRU_ICSSG subsystem integrates one PWM module, which uses IEP0 and IEP1
compare events to generates PWM outputs.

The PRU_ICSSG PWM module is supported as of in Processor SDK Linux v6.2 for
AM65x.  The linux PRU PWM driver models the PWM module as two pwmchips, each
supports up to 12 PWMs through PRU-ICSSG GPIO pins. The PWM function is
implemented in PRU firmware.


.. rubric:: PRU PWM Features

Up to 24 PWMs are supported per PRU-ICSSG with the following features:

  - Each pwmchip (IEP) supports up to 12 PWMs
  - support Single-Ended mode
  - PWM period range: 40us ~ 2sec
  - PWM duty-cycle range: 400ns ~ (period - 400ns)


.. rubric:: PRU PWM Unsupported Features

The following features are not supported in PRU PWM:

  - Complementary mode
  - Invert polarity (Active Low)


.. rubric:: PRU PWM driver Kernel Config

The PRU PWM Linux kernel driver depends on the PRU-ICSS kernel driver. So
the following kernel Kconfig options should be enabled to use the PRU PWM
module.

.. code-block:: menuconfig

   Device Drivers  --->
      SOC (System On Chip) specific Drivers  --->
         [*] TI SOC drivers support  --->
            <M> TI PRU-ICSS Subsystem Platform drivers

   Device Drivers  --->
      Pulse-Width Modulation (PWM) Support  --->
         PRU-ICSS PWM support


.. rubric:: PRU PWM Sysfs Usage

The PRU PWM Linux kernel driver is integrated in the kernel PWM framework, so
user space application can access the PWMs via the Linux sysfs entries. For
details of the usage, please refer to :ref:`PWM Driver Usage <driver-usage-pwm>`.


.. rubric:: Notes

The 12 PWMs within a pwmchip (IEP) share the common PWM period setting. So only
the PWM which first sets the PWM period (period ownner) has the permission to
modify the PWM period setting. Other PWMs within the same pwmchip cannot modify
the PWM period until the application deallocated the "period owner" PWM.


