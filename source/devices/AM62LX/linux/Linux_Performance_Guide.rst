
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

Low Power Performance
---------------------

These are power measurements taken while the device is in various low power modes like
Deep Sleep and RTC Only + DDR.

Table:  **Deep sleep**

.. csv-table::
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.7514649630", "4.8868646622"
     "soc_dvdd_1v8", "1.8012107611", "2.0651760101"
     "soc_dvdd_3v3", "3.2925584316", "2.5013184547"
     "vdda_1v8", "1.8007422686", "0.5689254999"
     "vdd_lpddr4_pmic1", "1.1009571552", "0.9891174436"
     "vdd_rtc", "0.7499415278", "0.0171553455"
     "vdd_rtc_1v8", "1.8004883528", "0.0148546640"
     "Total"," ","11.04"

Table:  **RTC Only + DDR**

.. csv-table::
     :header: "Rail name","Rail voltage(V)","Power (mW)"

     "vdd_core", "0.0010742188", "0.0001037598"
     "soc_dvdd_1v8", "1.8008592129", "1.2375650406"
     "soc_dvdd_3v3", "3.2974414825", "1.0737464428"
     "vdda_1v8", "0.0024999999", "0.0000331421"
     "vdd_lpddr4_pmic1", "1.1013282537", "1.0006968975"
     "vdd_rtc", "0.7501758337", "0.0158234257"
     "vdd_rtc_1v8", "1.8011522293", "0.0151987495"
     "Total"," ","3.34"
