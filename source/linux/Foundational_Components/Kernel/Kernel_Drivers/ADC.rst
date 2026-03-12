.. http://processors.wiki.ti.com/index.php/Linux_Core_ADC_Users_Guide

ADC
---------------------------------

.. rubric:: **Introduction**
   :name: introduction-core-adc

An analog-to-digital converter (abbreviated ADC) is a device that uses
sampling to convert a continuous quantity to a discrete time
representation in digital form.

.. ifconfig:: CONFIG_part_variant not in ('AM64X', 'AM65X', 'J721E', 'J7200', 'J721S2', 'J784S4','J742S2')

   The TSC\_ADC\_SS (Touchscreen\_ADC\_subsystem) is an 8 channel general
   purpose ADC, with optional support for interleaving Touch Screen
   conversions. The TSC\_ADC\_SS can be used and configured in one of the
   following application options:

   -  8 general purpose ADC channels
   -  4 wire TS, with 4 general purpose ADC channels
   -  5 wire TS, with 3 general purpose ADC channels

   ADC used is 12 bit SAR ADC with a sample rate of 200 KSPS (Kilo Samples
   Per Second). The ADC samples the analog signal when "start of
   conversion" signal is high and continues sampling 1 clock cycle after
   the falling edge. It captures the signal at the end of sampling period
   and starts conversion. It uses 12 clock cycles to digitize the sampled
   input; then an "end of conversion" signal is enabled high indicating
   that the digital data ADCOUT<11:0> is ready for SW to consume. A new
   conversion cycle can be initiated after the previous data is read.
   Please note that the ADC output is positive binary weighted data.

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'AM65X', 'J721E', 'J7200', 'J721S2', 'J784S4','J742S2')

   The ADC is a 12-bit, 8-channel, general purpose ADC with a sample rate
   of 4 MSPS (Megasamples per second or millions of samples per second).
   The ADC sits idle until a Start of Conversion (SOC) pulse allows the
   it to start conversion. The ADC samples the analog signal when "start
   of conversion" signal is high and continues sampling 1 clock cycle after
   the falling edge. It captures the signal at the end of sampling period
   and starts conversion. It uses 13 clock cycles to digitize the sampled
   input; then an "end of conversion" signal is enabled high indicating
   that the digital data ADCOUT<11:0> is ready for SW to consume. A new
   conversion cycle can be initiated after the previous data is read.
   Please note that the ADC output is positive binary weighted data.

.. rubric:: **Convert Analog voltage to Digital**
   :name: convert-analog-voltage-to-digital

To cross verify the digital values read use,

::

    D = Vin * (2^n - 1) / Vref

::

    Where:
    D = Digital value
    Vin = Input voltage
    n = No of bits
    Vref = reference voltage

Ex: Read value on channel AIN4 for input voltage supplied 1.01:

Formula:

::

    D = 1.01 * (2^12 -1 )/ 1.8
    D = 2297.75

.. rubric:: **Accessing ADC Pins on TI EVMs**
   :name: accessing-adc-pins-on-ti-evms

.. ifconfig:: CONFIG_part_variant not in ('AM64X', 'AM65X')

   .. rubric:: **AM335x EVM**
      :name: am335x-evm-adc

   On top of EVM, on LCD daughter board, J8 connector can be used, where
   ADC channel input AIN0-AN7 pins are brought out. For further information
   of J8 connector layout please refer to EVM schematics
   `here <http://www.ti.com/tool/tmdxevm3358#technicaldocuments>`__

   .. rubric:: **Beaglebone/Beaglebone Black**
      :name: beaglebonebeaglebone-black

   On BeagleBone platform, P9 expansion header can be used. For further
   information on expansion header layout please refer to the Beaglebone
   schematics
   `here <http://circuitco.com/support/index.php?title=BeagleBone#Rev_A6>`__

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   On AM64x platform, there is a 20-pin connector (J3) of part number
   "TSW-110-07-S-D" for connecting ADC signals. The connector includes
   ADC0_AIN0-7, VDDA_ADC connections and ground connections.
   For ADC connector (J3) Pin-Out go to the "AM64x User Guide" found
   `here <https://dev.ti.com/tirex/content/tirex-product-tree/am64x-devtools/docs/am64x_gpevm_quick_start_guide.html>`__,
   or see the ADC schematic (PROC101A(001)_SCH) found
   `here <https://www.ti.com/lit/zip/swrr171>`__.

.. ifconfig:: CONFIG_part_variant in ('AM65X')

   On AM65x platform, there is a 20-pin connector (J10) of part number
   "TSW-110-07-S-D" for connecting ADC signals. The connector includes
   MCU_ADC0_CH0-7 for ADC0 and ground connections. The ADC connector
   schematic (PROC062E3(003)_SCH) can be found
   `here <https://www.ti.com/lit/zip/sprcah2>`__.

|

.. rubric:: **Driver Configuration**
   :name: driver-configuration-adc

You can enable ADC driver in the kernel as follows.

::

    Device Drivers  --->
             [*]  Industrial I/O support  --->
                      [*]  Enable buffer support within IIO
                           Analog to digital converters  --->
                                   <*> TI's AM335X ADC driver

Should the entry "TI's AM335X ADC driver" be missing the MFD component
--->

::

    Device Drivers  --->
        Multifunction device drivers  --->
            <M> TI ADC / Touch Screen chip support

.. rubric:: Building as Loadable Kernel Module

-  In-case if you want to build the driver as module, use <M> instead of
   <\*> during menuconfig while selecting the drivers (as shown below).
   For more information on compiling and installing kernel modules, refer
   to the `Kernel User's Guide <Foundational_Components_Kernel_Users_Guide.html>`__ .
   For more information on loadable modules refer to `Loadable Module
   HOWTO <http://tldp.org/HOWTO/Module-HOWTO/>`__ .

::

    Device Drivers  --->
             [M]  Industrial I/O support  --->
                      [*]  Enable buffer support within IIO
                           Analog to digital converters  --->
                                   <M> TI's AM335X ADC driver

#. Use "make modules" during kernel build to build the ADC driver as
   module. The module should be present in
   ``drivers/iio/adc/ti_am335x_adc.ko``.
#. The driver should autoload on filesystem boot. If not, load the
   driver using

::

    modprobe ti_am335x_adc

.. rubric:: **Device Tree**
   :name: device-tree

.. ifconfig:: CONFIG_part_variant not in ('AM64X', 'AM65X')

   ADC device tree data is added in
   file(\ ``arch/arm/boot/dts/am335x-evm.dts``) as shown below.

   ::

      &tscadc {
               status = "okay";
               adc {
                     ti,adc-channels = <4 5 6 7>;
               };
      };

   |

   The parameter "ti,adc-channels" needs to hold data related to which
   channels you want to use for ADC.

   -  This example is using channels AIN4, AIN5, AIN6, and AIN7 are used by
      ADC. The remaining channels (0 to 3) are used by TSC.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   ADC device tree data is added in
   file(\ ``arch/arm64/boot/dts/ti/am642-evm.dts``) as shown below.

   ::

      &tscadc0 {
               status = "okay";
               adc {
                     ti,adc-channels = <0 1 2 3 4 5 6 7>;
               };
      };

   |

   The parameter "ti,adc-channels" needs to hold data related to which
   channels you want to use for ADC; the example above is using channels
   CH0-CH7.

.. ifconfig:: CONFIG_part_variant in ('AM65X')

   ADC device tree data is added in
   file(\ ``arch/arm64/boot/dts/ti/am654-base-board.dts``) as shown below.

   ::

      &tscadc0 {
	      adc {
		      ti,adc-channels = <0 1 2 3 4 5 6 7>;
	      };
      };

   |

   The parameter "ti,adc-channels" needs to hold data related to which
   channels you want to use for ADC; the example above is using channels
   CH0-CH7.

You can find the source code for ADC in the kernel sources at
``drivers/iio/adc/ti_am335x_adc.c``.

.. rubric:: **Usage**
   :name: adc-usage

To test ADC, Connect a DC voltage supply to each of the AIN0 through
AIN7 pins (based on your channel configuration), and vary voltage
between 0 and 1.8v reference voltage.

.. caution::

   Make sure that the voltage supplied does not cross 1.8v

On loading the module you would see the IIO device created

.. ifconfig:: CONFIG_part_variant not in ('AM64X', 'AM65X')

   ::

      root@arago-armv7:~# ls -al /sys/bus/iio/devices/iio\:device0/
      drwxr-xr-x    5 root     root             0 Nov  1 22:06 .
      drwxr-xr-x    4 root     root             0 Nov  1 22:06 ..
      drwxr-xr-x    2 root     root             0 Nov  1 22:06 buffer
      -r--r--r--    1 root     root          4096 Nov  1 22:06 dev
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 in_voltage4_raw
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 in_voltage5_raw
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 in_voltage6_raw
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 in_voltage7_raw
      -r--r--r--    1 root     root          4096 Nov  1 22:06 name
      lrwxrwxrwx    1 root     root             0 Nov  1 22:06 of_node -> ../../../../../../firmware/devicetree/base/ocp/tscadc@44e0d000/adc
      drwxr-xr-x    2 root     root             0 Nov  1 22:06 power
      drwxr-xr-x    2 root     root             0 Nov  1 22:06 scan_elements
      lrwxrwxrwx    1 root     root             0 Nov  1 22:06 subsystem -> ../../../../../../bus/iio
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 uevent

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'AM65X')

   ::

      root@arago-armv7:~# ls -al /sys/bus/iio/devices/iio\:device0/
      drwxr-xr-x    5 root     root             0 Nov  1 22:06 .
      drwxr-xr-x    4 root     root             0 Nov  1 22:06 ..
      drwxr-xr-x    2 root     root             0 Nov  1 22:06 buffer
      -r--r--r--    1 root     root          4096 Nov  1 22:06 dev
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 in_voltage0_raw
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 in_voltage1_raw
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 in_voltage2_raw
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 in_voltage3_raw
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 in_voltage4_raw
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 in_voltage5_raw
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 in_voltage6_raw
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 in_voltage7_raw
      -r--r--r--    1 root     root          4096 Nov  1 22:06 name
      lrwxrwxrwx    1 root     root             0 Nov  1 22:06 of_node -> ../../../../../../firmware/devicetree/base/ocp/tscadc@44e0d000/adc
      drwxr-xr-x    2 root     root             0 Nov  1 22:06 power
      drwxr-xr-x    2 root     root             0 Nov  1 22:06 scan_elements
      lrwxrwxrwx    1 root     root             0 Nov  1 22:06 subsystem -> ../../../../../../bus/iio
      -rw-r--r--    1 root     root          4096 Nov  1 22:06 uevent

.. rubric:: **Modes of operation**
   :name: modes-of-operation

When the ADC sequencer finishes cycling through all the enabled
channels, the user can decide if the sequencer should stop (one-shot
mode), or loop back and schedule again (continuous mode). If one-shot
mode is enabled, then the sequencer will only be scheduled one time (the
sequencer HW will automatically disable the StepEnable bit after it is
scheduled which will guarantee only one sample is taken per channel).
When the user wants to continuously take samples, continuous mode needs
to be enabled. One cannot read ADC data from one channel operating in
One-shot mode and and other in continuous mode at the same time.

.. rubric:: **One-shot Mode**
   :name: one-shot-mode

To read a single ADC output from a particular channel this interface can
be used.

::

    root@arago-armv7:~# cat /sys/bus/iio/devices/iio\:device0/in_voltage4_raw
    645

This feature is exposed by IIO through the following files:

-  in\_voltageX\_raw: raw value of the channel X of the ADC

.. rubric:: **Continuous Mode**
   :name: continuous-mode

.. rubric:: **Overview**
   :name: overview

Important folders in the iio:deviceX directory are:

-  ``buffer``

   -  ``enable``: get and set the state of the buffer
   -  ``length``: get and set the length of the buffer.

::

    root@charlie:~# ls -l /sys/bus/iio/devices/iio\:device0/buffer/
    total 0
    -rw-r--r-- 1 root root 4096 Nov  3 22:53 enable
    -rw-r--r-- 1 root root 4096 Nov  3 22:53 length
    -rw-r--r-- 1 root root 4096 Nov  3 22:53 watermark

-  Scan\_elements directory contains interfaces for elements that will
   be captured for a single sample set in the buffer.

::

    root@arago-armv7:~# ls -al /sys/bus/iio/devices/iio\:device0/scan_elements/
    drwxr-xr-x    2 root     root            0 Jan  1 00:00 .
    drwxr-xr-x    5 root     root            0 Jan  1 00:00 ..
    -rw-r--r--    1 root     root         4096 Jan  1 00:02 in_voltage0_en
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage0_index
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage0_type
    -rw-r--r--    1 root     root         4096 Jan  1 00:02 in_voltage1_en
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage1_index
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage1_type
    -rw-r--r--    1 root     root         4096 Jan  1 00:02 in_voltage2_en
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage2_index
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage2_type
    -rw-r--r--    1 root     root         4096 Jan  1 00:02 in_voltage3_en
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage3_index
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage3_type
    -rw-r--r--    1 root     root         4096 Jan  1 00:02 in_voltage4_en
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage4_index
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage4_type
    -rw-r--r--    1 root     root         4096 Jan  1 00:02 in_voltage5_en
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage5_index
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage5_type
    -rw-r--r--    1 root     root         4096 Jan  1 00:02 in_voltage6_en
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage6_index
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage6_type
    -rw-r--r--    1 root     root         4096 Jan  1 00:02 in_voltage7_en
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage7_index
    -r--r--r--    1 root     root         4096 Jan  1 00:02 in_voltage7_type
    root@arago-armv7:~#

``scan_elements`` exposes 3 files per channel:

-  in\_voltageX\_en: is this channel enabled?
-  in\_voltageX\_index: index of this channel in the buffer's chunks
-  in\_voltageX\_type : How the ADC stores its data. Reading this file
   should return you a string something like below:

::

    root@arago-armv7:~# cat /sys/bus/iio/devices/iio\:device0/scan_elements/in_voltage1_type
    le:u12/16>>0

Where:

-  le represents the endianness, here little endian
-  u is the sign of the value returned. It could be either u (for
   unsigned) or s (for signed)
-  12 is the number of relevant bits of information
-  16 is the actual number of bits used to store the datum
-  0 is the number of right shifts needed.

|

.. rubric:: **How to set it up**
   :name: how-to-set-it-up

To read ADC data continuously we need to enable buffer and channels to
be used.

Set up the channels in use (you can enable any combination of the
channels you want)

::

    root@arago-armv7:~# echo 1 > /sys/bus/iio/devices/iio\:device0/scan_elements/in_voltage0_en
    root@arago-armv7:~# echo 1 > /sys/bus/iio/devices/iio\:device0/scan_elements/in_voltage5_en
    root@arago-armv7:~# echo 1 > /sys/bus/iio/devices/iio\:device0/scan_elements/in_voltage7_en

Set up the buffer length

::

    root@arago-armv7:~# echo 100 > /sys/bus/iio/devices/iio\:device0/buffer/length

Enable the capture

::

    root@arago-armv7:~# echo 1 > /sys/bus/iio/devices/iio\:device0/buffer/enable

| Now, all the captures are exposed in the character device
  ``/dev/iio:device0``

To stop the capture, just disable the buffer

::

    root@arago-armv7:~# echo 0 > /sys/bus/iio/devices/iio\:device0/buffer/enable

.. rubric:: **Userspace Sample Application**
   :name: userspace-sample-application

The source code is located under kernel sources at
``tools/iio/iio_generic_buffer.c``.

How to compile:

::

    $ make -C <kernel-src-dir>/tools/iio ARCH=arm

The ``iio_generic_buffer`` application does all the ADC channel "enable"
and "disable" actions for you. You will only need to specify the IIO
driver. Application takes *buffer length* to use (256 in this example)
and the *number of iterations* you want to run (3 in this example). By
just enabling the buffer ADC switches to continuous mode.

::

    root@charlie:~# ./iio_generic_buffer -?
    Usage: generic_buffer [options]...
    Capture, convert and output data from IIO device buffer
      -a         Auto-activate all available channels
      -A         Force-activate ALL channels
      -c <n>     Do n conversions
      -e         Disable wait for event (new data)
      -g         Use trigger-less mode
      -l <n>     Set buffer length to n samples
      --device-name -n <name>
      --device-num -N <num>
            Set device by name or number (mandatory)
      --trigger-name -t <name>
      --trigger-num -T <num>
            Set trigger by name or number
      -w <n>     Set delay between reads in us (event-less mode)

For example:-

::

    root@charlie:~# ./iio_generic_buffer -N 0 -g -a
    iio device number being used is 0
    trigger-less mode selected
    Enabling all channels
    Enabling: in_voltage7_en
    Enabling: in_voltage4_en
    Enabling: in_voltage6_en
    Enabling: in_voltage5_en
    525.000000 924.000000 988.000000 1039.000000
    754.000000 986.000000 1071.000000 1117.000000
    877.000000 1067.000000 1150.000000 1169.000000
    1003.000000 1143.000000 1230.000000 1226.000000
    1078.000000 1222.000000 1298.000000 1286.000000
    1139.000000 1286.000000 1372.000000 1343.000000
    ...
    ...
    1863.000000 1954.000000 2031.000000 2074.000000
    1858.000000 1959.000000 2023.000000 2083.000000
    1852.000000 1958.000000 2024.000000 2076.000000
    1866.000000 1964.000000 2029.000000 2083.000000
    1850.000000 1952.000000 2026.000000 2074.000000
    Disabling: in_voltage7_en
    Disabling: in_voltage4_en
    Disabling: in_voltage6_en
    Disabling: in_voltage5_en

.. rubric::  **ADC Driver Limitations**
   :name: adc-driver-limitations

This driver is based on the IIO (Industrial I/O subsystem), however this
driver has limited functionality:

#. "Out of Range" not supported by ADC driver.

