.. http://processors.wiki.ti.com/index.php/Linux_Core_PWM_User%27s_Guide

PWM
---------------------------------

.. rubric:: Introduction
   :name: introduction-linux-core-pwm-ug

Linux has support for Enhanced Pulse Width Modulator (ePWM) and
Auxiliary Pulse Width Modulator (APWM) modules. APWM is Enhanced
Capture (eCAP) module configured in PWM mode. These devices are part
of the Pulse-Width Modulation Subsystem (PWMSS).

.. rubric:: PWMSS software architecture
   :name: pwmss-software-architecture

.. Image:: /images/AM335X_PWM-SS_arch.JPG

.. rubric:: Kernel Configuration
   :name: driver-configuration-pwm

.. rubric:: Enable the eHRPWM driver
   :name: enable-the-ehrpwm-driver

::

   Device Drivers --->
      <*> Pulse Width Modulation(PWM) Support --->
         <*> eHRPWM PWM support

.. rubric:: Enable the eCAP driver
   :name: enable-the-ecap-driver

::

   Device Drivers --->
      <*> Pulse Width Modulation(PWM) Support --->
         <*> eCAP PWM support

.. note::
   -  eHRPWM modules provide two PWM output channels per instance.

   -  eCAP modules provide a single PWM output channel pre instance when configured in APWM mode.


.. rubric:: Driver Usage
   :name: driver-usage-pwm

.. _Using-PWM-with-sysfs:

.. rubric:: Using PWM with the sysfs interface
   :name: using-pwm-with-sysfs-interface

The PWMs can be used from the userspace with a simple sysfs interface exposed at ``/sys/class/pwm/``. Each probed PWM controller/chip will be exported as pwmchipN, where N is the base of the PWM chip. The following attributes are available for each pwmchipN:

-  **npwm**

  The number of PWM channels this chip supports.

-  **export**

  Exports a PWM channel for use with sysfs.

-  **unexport**

  Unexports a PWM channel from sysfs.

The PWM channels are numbered per-chip from 0 to npwm-1.
When a PWM channel is exported a pwmX directory will be created in the pwmchipN directory, where X is the number of the channel that was exported. The following attributes will then be available in the pwmX directory:

-  **period**

  The total period of the PWM signal in nanoseconds.

-  **duty_cycle**

  The active time of the PWM signal in nanoseconds. Must be less than the period.

-  **polarity**

  Changes the polarity of the PWM signal. The value written is the string “normal” or “inversed”.

-  **enable**

  Enable/disable the PWM signal.

  -  0 - disabled
  -  1 - enabled

**Example**

List the available PWM controllers.

.. code-block:: console

   $ ls /sys/class/pwm/
   pwmchip0  pwmchip1  pwmchip2  pwmchip3  pwmchip5  pwmchip7

The number of channels per controller is reported in the ``npwm`` attribute.

.. code-block:: console

   $ cat /sys/class/pwm/pwmchip5/npwm
   2

The ``pwmchip5`` controller is a 2 channel ePWM. Export the second channel (EPWM_B, channel 1).

.. code-block:: console

   $ echo 1 > /sys/class/pwm/pwmchip5/export

Verify ``pwm1`` directory exists in the ``pwmchip5`` directory.

.. code-block:: console

   $ ls /sys/class/pwm/pwmchip5/
   device  export  npwm  power  pwm1  subsystem  uevent unexport

.. note::
    The PWM period and duty cycle must be configured before enabling any channel.

Set a period of 100 milliseconds with 30% duty cycle. The values are in nanoseconds.

.. code-block:: console

    $ echo 100000000 > /sys/class/pwm/pwmchip5/pwm1/period
    $ echo 30000000 > /sys/class/pwm/pwmchip5/pwm1/duty_cycle

Set the PWM signal polarity to "inversed" (or "normal") if required.

.. code-block:: console

    $ echo "inversed" > /sys/class/pwm/pwmchip5/pwm1/polarity
    $ cat /sys/class/pwm/pwmchip5/pwm1/polarity
    inversed

Enable the PWM channel.

.. code-block:: console

    $ echo 1 > /sys/class/pwm/pwmchip5/pwm1/enable

.. rubric:: Using PWM with kernel PWM API
   :name: using-pwm-with-kernel-pwm-api

A few examples of kernel drivers using the kernel PWM API:

- pwm-backlight: `drivers/video/backligt/pwm_bl.c <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/drivers/video/backlight/pwm_bl.c?h=ti-linux-5.10.y>`_

- pwm-beeper: `drivers/input/misc/pwm-beeper.c <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/drivers/input/misc/pwm-beeper.c?h=ti-linux-5.10.y>`_

- pwm-vibrator: `drivers/input/misc/pwm-vibra.c <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/drivers/input/misc/pwm-vibra.c?h=ti-linux-5.10.y>`_

.. rubric:: Troubleshooting the PWM setup
   :name: troubleshoot-the-pwm-setup

The current PWM settings for ePWM and eCAP(APWM) can be monitored from the debugfs ``pwm`` entry.

.. code-block:: console

    $ cat /sys/kernel/debug/pwm
    platform/23020000.pwm, 2 PWM devices
     pwm-0   ((null)              ): period: 0 ns duty: 0 ns polarity: normal
     pwm-1   ((null)              ): period: 0 ns duty: 0 ns polarity: normal

    platform/23010000.pwm, 2 PWM devices
     pwm-0   ((null)              ): period: 0 ns duty: 0 ns polarity: normal
     pwm-1   (sysfs               ): requested enabled period: 100000000 ns duty: 50000000 ns polarity: inverse

    platform/23000000.pwm, 2 PWM devices
     pwm-0   ((null)              ): period: 0 ns duty: 0 ns polarity: normal
     pwm-1   ((null)              ): period: 0 ns duty: 0 ns polarity: normal

    platform/23120000.pwm, 1 PWM device
     pwm-0   ((null)              ): period: 0 ns duty: 0 ns polarity: normal

    platform/23110000.pwm, 1 PWM device
     pwm-0   ((null)              ): period: 0 ns duty: 0 ns polarity: normal

    platform/23100000.pwm, 1 PWM device
     pwm-0   ((null)              ): period: 0 ns duty: 0 ns polarity: normal

|

.. rubric:: Testing eHRPWM in TI PSDK
   :name: testing-ehrpwm

EHRPWM can be tested using the following overlays for each of the following devices:

#. AM62X SK: k3-am625-sk-rpi-hdr-ehrpwm.dtso
#. AM62AX SK and AM62DX EVM: k3-am62a7-sk-rpi-hdr-ehrpwm.dtso
#. AM62PX SK: k3-am62p5-sk-rpi-hdr-ehrpwm.dtso
