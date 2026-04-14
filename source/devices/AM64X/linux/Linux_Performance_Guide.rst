#################################
 Linux 12.00.00 Performance Guide
#################################

***************
Read This First
***************

**All performance numbers provided in this document are gathered using
following Evaluation Modules unless otherwise specified.**

+----------------+----------------------------------------------------------------------------------------------------------------+
| Name           | Description                                                                                                    |
+================+================================================================================================================+
| AM64x EVM      |  AM64x Evaluation Module rev E1 with ARM running at 1GHz, DDR data rate 1600 MT/S                              |
+----------------+----------------------------------------------------------------------------------------------------------------+

Table:  Evaluation Modules

*****************
About This Manual
*****************

This document provides performance data for each of the device drivers
which are part of the Processor SDK Linux package. This document should be
used in conjunction with release notes and user guides provided with the
Processor SDK Linux package for information on specific issues present
with drivers included in a particular release.

For further information or to report any problems, contact
https://e2e.ti.com/ or https://support.ti.com/

|

*****************
System Benchmarks
*****************

|

|

CRYPTO
======

Crypto Performance Comparison
-----------------------------

The following table shows different AES/SHA algorithms throughput measured using openssl speed across the SA2UL accelerator, ARM Cryptographic Extension (CE), and baseline ARM CPU.

.. csv-table:: Crypto Accelerator Performance
   :header: "Algorithm", "Size (bytes)", "Accelerator (MB/s)", "ARM CE (MB/s)", "ARM (MB/s)"
   :widths: 20, 25, 20, 20, 20

   "aes-128-cbc", "16", "0.34", "69.43", "22.18"
   "aes-128-cbc", "64", "1.51", "217.04", "28.34"
   "aes-128-cbc", "256", "5.99", "454.25", "30.63"
   "aes-128-cbc", "1024", "21.92", "640.51", "31.25"
   "aes-128-cbc", "8192", "97.97", "726.61", "31.44"
   "aes-128-cbc", "16384", "134.93", "727.48", "31.44"
   "aes-128-ecb", "16 bytes", "0.34", "73.59", "23.41"
   "aes-128-ecb", "64 bytes", "1.50", "202.54", "29.24"
   "aes-128-ecb", "256 bytes", "5.99", "464.31", "31.29"
   "aes-128-ecb", "1024 bytes", "21.97", "702.67", "31.86"
   "aes-128-ecb", "8192 bytes", "100.92", "824.92", "32.02"
   "aes-128-ecb", "16384 bytes", "138.82", "834.02", "32.02"
   "aes-192-cbc", "16 bytes", "0.33", "66.81", "19.77"
   "aes-192-cbc", "64 bytes", "1.47", "196.53", "24.54"
   "aes-192-cbc", "256 bytes", "5.82", "376.00", "26.24"
   "aes-192-cbc", "1024 bytes", "21.32", "496.64", "26.69"
   "aes-192-cbc", "8192 bytes", "93.72", "547.69", "26.84"
   "aes-192-cbc", "16384 bytes", "127.00", "551.73", "26.85"
   "aes-192-ecb", "16 bytes", "0.34", "71.43", "21.00"
   "aes-192-ecb", "64 bytes", "1.52", "193.03", "25.32"
   "aes-192-ecb", "256 bytes", "5.97", "426.73", "26.77"
   "aes-192-ecb", "1024 bytes", "21.91", "623.05", "27.15"
   "aes-192-ecb", "8192 bytes", "96.57", "718.21", "27.27"
   "aes-192-ecb", "16384 bytes", "130.32", "726.05", "27.24"
   "aes-256-cbc", "16 bytes", "0.34", "65.08", "18.03"
   "aes-256-cbc", "64 bytes", "1.49", "182.49", "21.70"
   "aes-256-cbc", "256 bytes", "5.95", "328.41", "22.96"
   "aes-256-cbc", "1024 bytes", "21.62", "416.88", "23.29"
   "aes-256-cbc", "8192 bytes", "90.38", "452.23", "23.40"
   "aes-256-cbc", "16384 bytes", "120.37", "454.51", "23.40"
   "sha2-256", "16 bytes", "0.37", "9.30", "6.14"
   "sha2-256", "64 bytes", "1.45", "33.77", "17.48"
   "sha2-256", "256 bytes", "5.80", "109.48", "38.41"
   "sha2-256", "1024 bytes", "22.30", "248.15", "54.93"
   "sha2-256", "8192 bytes", "128.88", "395.37", "62.80"
   "sha2-256", "16384 bytes", "196.56", "412.43", "63.41"
   "sha2-512", "16 bytes", "0.35", "5.51", "5.52"
   "sha2-512", "64 bytes", "1.42", "22.00", "21.99"
   "sha2-512", "256 bytes", "5.35", "46.49", "46.48"
   "sha2-512", "1024 bytes", "18.47", "77.98", "77.85"
   "sha2-512", "8192 bytes", "63.28", "97.22", "97.25"
   "sha2-512", "16384 bytes", "76.56", "98.87", "98.93"

.. csv-table:: CPU Usage %
   :header: "Algorithm", "Accelerator (%)", "ARM CE (%)", "ARM (%)"
   :widths: 25, 25, 25, 25

   "aes-128-cbc", "39%", "99%", "99%"
   "aes-128-ecb", "41%", "99%", "99%"
   "aes-192-cbc", "39%", "99%", "99%"
   "aes-192-ecb", "40%", "99%", "99%"
   "aes-256-cbc", "38%", "99%", "99%"
   "sha2-256", "91%", "99%", "99%"
   "sha2-512", "91%", "99%", "99%"
