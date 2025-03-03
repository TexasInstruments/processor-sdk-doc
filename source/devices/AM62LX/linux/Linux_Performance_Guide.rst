
====================================
 Linux 11.00.00.00 Performance Guide
====================================

.. rubric::  **Read This First**
   :name: read-this-first-kernel-perf-guide

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
| AM62L EVM      | AM62L EVM rev E1-1 with ARM running at 400 MHz, DDR data rate 1100 MT/S                                        |
+----------------+----------------------------------------------------------------------------------------------------------------+

Table:  Evaluation Modules

.. rubric::  About This Manual
   :name: about-this-manual-kernel-perf-guide

This document provides performance data for each of the device drivers
which are part of the Linux SDK package. This document should be
used in conjunction with release notes and user guides provided with the
Linux SDK package for information on specific issues present
with drivers included in a particular release.

.. rubric::  If You Need Assistance
   :name: if-you-need-assistance-kernel-perf-guide

For further information or to report any problems, contact
https://e2e.ti.com/ or https://support.ti.com/

Linux QSPI/OSPI Driver
----------------------

.. csv-table::
    :header: "Flash","File Size","Read Throughput","Write Throughput"

    "OSPI NOR","50 MB","205 MB/s","403 KB/s"
    "QSPI NAND","50 MB","18.6 MB/s","4.9 MB/s"

U-Boot QSPI/OSPI Driver
-----------------------

.. csv-table::
    :header: "Flash","File Size","Read Throughput","Write Throughput"

    "OSPI NOR","50 MB","303 MB/s","167 KB/s"
    "QSPI NAND","50 MB","25.7 MB/s","5.5 MB/s"

Low Power Performance
---------------------

These are power measurements taken while the device is in various low power modes like
Deep Sleep and RTC Only + DDR.

Table:  **Deep sleep**

.. csv-table::
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.75", "4.88"
     "soc_dvdd_1v8", "1.80", "2.06"
     "soc_dvdd_3v3", "3.29", "2.50"
     "vdda_1v8", "1.80", "0.56"
     "vdd_lpddr4_pmic1", "1.10", "0.99"
     "vdd_rtc", "0.74", "0.01"
     "vdd_rtc_1v8", "1.80", "0.01"
     "Total"," ","~11.04"

Table:  **RTC Only + DDR**

.. csv-table::
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.00", "0.00"
     "soc_dvdd_1v8", "1.80", "1.23"
     "soc_dvdd_3v3", "3.29", "1.07"
     "vdda_1v8", "0.00", "0.00"
     "vdd_lpddr4_pmic1", "1.10", "1.00"
     "vdd_rtc", "0.75", "0.02"
     "vdd_rtc_1v8", "1.80", "0.02"
     "Total"," ","3.34"
