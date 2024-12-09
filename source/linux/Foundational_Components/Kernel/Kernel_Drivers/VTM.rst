Voltage & Thermal Management (VTM)
----------------------------------

Introduction
^^^^^^^^^^^^

.. rubric:: VTM Driver Overview

The Voltage and Thermal Management (VTM) system provides the control,
status and interrupt generation for the various independent temperature
sensors located at different hotspots on the SoC. This allows the kernel
to take actions based on thermal events configured via the kernel's
device tree.

Driver Features
^^^^^^^^^^^^^^^

.. rubric:: Sysfs Monitoring

One of the most basic roles the VTM system can give the kernel is
temperature readings (in milliCelcius) in the sysfs filesystem.

.. code-block:: bash

   cat /sys/class/thermal/thermal_zone*/temp

Running this command on your SoC will print each temperature in
milliCelcius for that region on the SoC.

.. rubric:: Thresholds, Triggers and Cooling

We can also program up to 3 threshold temperatures, 2 for greater than
thresholds and 1 for a less than threshold, to allow the VTM to alert
the kernel to take action. For example when the 1\ :sup:`st` threshold is
exceeded the kernel can be alerted to begin reducing the voltage and
clocks speed of CPUs, allowing the SoC's overall temperature to
stabilize.  If the SoC temperature continues to increase we can then use
the 2\ :sup:`nd` threshold to take more aggressive action.  For example
we could issue a poweroff command to turn the device off completely once
the 2\ :sup:`nd` threshold is exceeded.

Threshold temperatures can be set in the kernel with the values we
define inside the device tree. This can be used for:

#. To set a 'critical' temperature, where the kernel will poweroff the SoC

#. To signal a 'passive' alert in kernel in event of overheating

#. To lower the MPU frequency by registering cpufreq driver as a cooling
   device. cpufreq does DFS on the MPU to set the frequency specified in
   OPP table in the device tree. For more details, see
   `DFS <Power_Management/pm_dfs.html>`__.

::

    /* From arch/arm64/boot/dts/ti/k3-j7200-thermal.dtsi */

	mpu_thermal: mpu-thermal {
		polling-delay-passive = <250>; /* milliseconds */
		polling-delay = <500>; /* milliseconds */
		thermal-sensors = <&wkup_vtm0 1>;

		trips {
			mpu_crit: mpu-crit {
				temperature = <125000>; /* milliCelsius */
				hysteresis = <2000>; /* milliCelsius */
				type = "critical";
			};

			mpu_alert0: mpu_alert {
				temperature = <55000>; /* millicelsius */
				hysteresis = <5000>; /* millicelsius */
				type = "passive";
			};
		};

		cpu_cooling_maps: cooling-maps {
			map0 {
				trip = <&mpu_alert0>;
				cooling-device =
				<&cpu0 THERMAL_NO_LIMIT THERMAL_NO_LIMIT>;
			};
		};
	};

This node will instruct the kernel to periodically poll this temperature
sensor and to shutdown the SoC once it has exceeded 125 degrees Celsius.
And will enable cooling using DFS by cpufreq-dt driver on the MPU at 55
degrees Celsius.

Finding More Information
^^^^^^^^^^^^^^^^^^^^^^^^

More information can be found for this VTM device inside the Technical
Reference Manual for your device or the `device tree binding
documentation`_ in the kernel's source.

.. _`device tree binding documentation`: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/devicetree/bindings/thermal

