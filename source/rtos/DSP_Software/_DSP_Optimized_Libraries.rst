************************
DSP Optimized Libraries
************************

.. http://processors.wiki.ti.com/index.php/Processor_SDK_Libraries


Available Libraries
===================

The table below lists currently available libraries and the
corresponding information - whether they are included in Proc-SDK Linux
or RTOS, supported devices, and documentation links.

+-------------+-------------+-------------+-------------+---------------+
| Library     | Proc-SDK    | Proc-SDK    | Supported   | Documentation |
|             | Linux       | RTOS        | Devices     |               |
+=============+=============+=============+=============+===============+
| MATHLIB     | No          | Yes         | K1/K2/AM57x | `MATHLIB      |
|             |             |             |             | Documentation |
|             |             |             |             | <http://      |
|             |             |             |             | processors.   |
|             |             |             |             | wiki.ti.com   |
|             |             |             |             | /index.php/   |
|             |             |             |             | Software_li   |
|             |             |             |             | braries#Mat   |
|             |             |             |             | hLIB>`__      |
+-------------+-------------+-------------+-------------+---------------+
| DSPLIB      | No          | Yes         | K1/K2/AM57x | `DSPLIB       |
|             |             |             |             | Documentation |
|             |             |             |             | <http://      |
|             |             |             |             | processors.   |
|             |             |             |             | wiki.ti.com   |
|             |             |             |             | /index.php/   |
|             |             |             |             | Software_li   |
|             |             |             |             | braries#DSP   |
|             |             |             |             | LIB>`__       |
+-------------+-------------+-------------+-------------+---------------+
| IMGLIB      | No          | Yes         | K1/K2/AM57x | `IMGLIB       |
|             |             |             |             | Documentation |
|             |             |             |             | <http://      |
|             |             |             |             | processors.   |
|             |             |             |             | wiki.ti.com   |
|             |             |             |             | /index.php/   |
|             |             |             |             | Software_li   |
|             |             |             |             | braries#IMG   |
|             |             |             |             | LIB>`__       |
+-------------+-------------+-------------+-------------+---------------+
| LibArch     | Yes         | Yes         | C6678(RTOS) | `LibArch      |
|             |             |             | /K2H(Linux) | User's        |
|             |             |             | /AM572x     | Guide <http   |
|             |             |             | (Linux)     | ://processo   |
|             |             |             |             | rs.wiki.ti.   |
|             |             |             |             | com/index.p   |
|             |             |             |             | hp/Processo   |
|             |             |             |             | r_SDK_Libra   |
|             |             |             |             | ry_Architec   |
|             |             |             |             | ture_and_Fr   |
|             |             |             |             | amework>`__   |
+-------------+-------------+-------------+-------------+---------------+
| FFTLIB      | Yes         | Yes         | C6678(RTOS) | `FFT User's   |
|             |             |             | /K2H(Linux) | Guide (Linux) |
|             |             |             | /AM572x     | <http://proce |
|             |             |             | (Linux)     | ssors.wiki.ti |
|             |             |             |             | .com/index.ph |
|             |             |             |             | p/MCSDK_HPC   |
|             |             |             |             | _3.x_FFTW_Lib |
|             |             |             |             | rary>`__      |
|             |             |             |             |               |
|             |             |             |             | FFT User's    |
|             |             |             |             | Guide (RTOS): |
|             |             |             |             | Refer to FFT  |
|             |             |             |             | LIB folder    |
+-------------+-------------+-------------+-------------+---------------+
| LINALG      | Yes         | Yes         | C6678(RTOS) | `LINALG       |
|             |             |             | /K2H(Linux) | User's        |
|             |             |             | /AM572x     | Guide <http   |
|             |             |             | (Linux)     | ://processo   |
|             |             |             |             | rs.wiki.ti.   |
|             |             |             |             | com/index.p   |
|             |             |             |             | hp/Processo   |
|             |             |             |             | r_SDK_Linea   |
|             |             |             |             | r_Algebra_L   |
|             |             |             |             | ibrary>`__    |
+-------------+-------------+-------------+-------------+---------------+

Processor SDK libraries can be categorized into two groups, general
purpose libraries and high performance or application specific
libraries.

General Purpose Libraries
-------------------------

-  MATHLIB:\ `Standalone download
   page <http://www.ti.com/tool/mathlib>`__
-  DSPLIB: `Standalone download page <http://www.ti.com/tool/sprc265>`__
-  IMGLIB: `Standalone download page <http://www.ti.com/tool/sprc264>`__

These libraries are delivered with TI C66x object code and included in
Processor-SDK ROTS. For development in Processor-SDK Linux, they can be
downloaded from the links listed above and used in any C66x DSP code.

|

High Performance or Application Specific Libraries
--------------------------------------------------

-  `LibArch <http://processors.wiki.ti.com/index.php/Processor_SDK_Library_Architecture_and_Framework>`__:
   Library Architecture and Framework, an abstraction layer for
   multi-core DSP library development.
-  `FFTLIB <http://processors.wiki.ti.com/index.php/MCSDK_HPC_3.x_FFTW_Library>`__:
   optimized library for performing fast Fourier transform.
-  `LINALG <http://processors.wiki.ti.com/index.php/Processor_SDK_Linear_Algebra_Library>`__:
   optimized library for performing dense linear algebra computations.

These libraries are available in both Processor-SDK RTOS and
Processor-SDK Linux.

Library Usage
=============

Libraries can be used in either Processor-SDK RTOS or Processor-SDK
Linux.

Using Libraries in Processor-SDK RTOS
-------------------------------------

The following diagram illustrates the software stack of various
components including libraries provided with the Processor-SDK RTOS.

.. Image:: /images/Lib_sw_stack_rtos.jpg

Using Libraries in Processor-SDK Linux
--------------------------------------

The following diagram illustrates the software stack in Processor-SDK
Linux environment, taking LINALG as an example. Applications access the
libraries on the host (ARM) side, and the actual computation may be
executed on ARM or DSP according to configuration and problem size. This
is explained in detail in each library's documentation page.

.. Image:: /images/Linalg.jpg

Delivery Format
===============

All libraries are delivered with both source code and object code. The
source code can be recompiled according to the instructions given in
each individual library's documentation.

Core benchmark comparison
=========================

Please refer to `Core Benchmarks
<http://www.ti.com/processors/digital-signal-processors/core-benchmarks/core-benchmarks.html>`__
for DSP vs A15 core benchmark comparison for computation intensive tasks.

