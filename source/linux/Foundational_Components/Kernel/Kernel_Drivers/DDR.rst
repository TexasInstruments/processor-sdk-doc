.. _K3-DDR-Driver:
.. _ddr-driver:

######
K3 DDR
######

************
Introduction
************

The K3 DDR driver provides management and monitoring capabilities for DDR memory
subsystems on Texas Instruments K3 SoCs.

The following is a list of supported K3 DDR driver features by device family:

.. list-table:: K3 DDR Driver Feature Support
   :header-rows: 1

   * - Device Family
     - Temperature Monitoring

   * - J7200
     - Yes

   * - AM62x LP SK/ AM62Ax / AM62Px
     - Yes

********************************
Building and Enabling the Driver
********************************

.. rubric:: Kernel Configuration

The following kernel configuration enables the K3 DDR driver:

.. code-block:: kconfig

   CONFIG_K3_DDR_TEMP=y
   CONFIG_HWMON=y

.. _ddr-temperature-monitoring-linux:

************************************
Using the DDR Temperature Monitoring
************************************

By default, the DDR subsystem keeps temperature polling turned off. For allowing
the kernel driver to monitor temperature, the user must enable polling during
DDR configuration and initialization at boot time.

See :ref:`ddr-temperature-monitoring-uboot` in U-Boot documentation.

The K3 DDR driver creates a hwmon device that provides temperature status
information through sysfs. The driver registers as ``k3_ddr`` in the hwmon
subsystem for temperature monitoring functionality.

The driver reports temperature status according to LPDDR4 specification:

.. list-table::
   :header-rows: 1
   :stub-columns: 1

   * - Value
     - Temperature Status
   * - 0
     - Low temperature
   * - 1
     - 4x refresh interval
   * - 2
     - 2x refresh interval
   * - 3
     - 1x refresh interval (nominal)
   * - 4
     - 0.5x refresh interval
   * - 5
     - 0.25x refresh interval
   * - 6
     - 0.25x refresh interval with derating
   * - 7
     - High temperature

The hwmon device should now show up in the filesystem.

.. code-block:: console

   root@evm:~# ls -l /sys/class/hwmon/
   hwmon0

Check the current DDR temperature status:

.. code-block:: console

   root@evm:~# cat /sys/class/hwmon/hwmon0/device/k3_ddr_temp_status
   1x refresh interval
