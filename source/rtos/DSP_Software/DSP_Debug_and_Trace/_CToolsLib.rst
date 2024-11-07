.. http://processors.wiki.ti.com/index.php/CToolsLib

Introduction
------------

See `CToolsLib Article <http://processors.wiki.ti.com/index.php/CToolsLib_Article>`__ for a
comprehensive article on cToolsLibs and the hardware modules supported.

Overview
--------

-  CToolsLib is collection of embedded target APIs/library focused to
   enable easy programmatic access to `CTools <http://processors.wiki.ti.com/index.php/CTools>`__
   debug capabilities
-  CToolsLib purpose is provided in source code for easy integration
   into applications
-  CToolsLib consists of several libraries

AETLib
^^^^^^

-  The `AETLIB <http://processors.wiki.ti.com/index.php/AETLIB>`__ library provides programmatic
   access to the `Advanced Event
   Triggering <http://processors.wiki.ti.com/index.php/Advanced_Event_Triggering>`__ capability on
   64x and 64x+ processor cores.

ETBLib
^^^^^^

-  This library provides the ability to program and read trace data from
   an Embedded Trace Buffer (ETB). The ETB can be used with other
   libraries to setup and capture DSP core trace data, ARM core trace
   data, or STM data sources.
-  In some devices each core has a dedicated ETB, while others have a
   single ETB shared between trace sources.
-  After the ETB data is read into local memory, the user must transport
   the binary trace data back to a host where the binary trace data can
   be converted to text, csv or a .tdf file that can be imported into
   CCS for display. The GettingStarted.htm file (available at
   `[1] <http://downloads.ti.com/emulation/esd/ctoolslib/GettingStarted.htm>`__
   )provides instructions for generating these files from utilities
   provided with CCS.
-  The Examples projects are also a good source of information on using
   ETBLib for different cases.

-  Instructions for `STM EDMA Example <http://processors.wiki.ti.com/index.php/STM_EDMA_Example>`__
   to extend ETB using target memory
-  Instructions for `DSPTrace EDMA
   Example <http://processors.wiki.ti.com/index.php/DSPTrace_EDMA_Example>`__ to extend ETB using
   target memory

DSPTraceLib
^^^^^^^^^^^

-  This library provides the ability to programmaticly setup 64x+ DSP
   trace export.

ETMLib
^^^^^^

-  The ETM Library provides the interface to configure and control
   instruction and data tracing during program execution. A trace
   session is defined as the time frame from the trace system getting
   armed(enabled and waiting for a start trace condition), to the time
   when the trace completes, either from an end trace condition that has
   been configured or a manual call to stop tracing.
-  Developed and tested for the CortexA8 on TCI6614 and C6A816x devices.
-  The `ETMLib Examples <http://processors.wiki.ti.com/index.php/ETMLib_Examples>`__ page provides
   instructions on how to run the examples and display the results.

STMLib
^^^^^^

-  This library provides "C" printf and binary APIs for hardware
   assisted (System Trace software messages) instrumentation in your
   code. STM messages are captured via an ETB or with an external
   XDS560v2 System Trace receiver.
-  For instructions on setting up CCS to capture STM data see `Using
   System Trace(STM) <http://processors.wiki.ti.com/index.php/Using_System_Trace_(STM)>`__.

ITMLib
^^^^^^

-  The ITMLib provides "C" string amd binary value logging APIs for TI
   M3/M4 devices that includes an ITM module and supports SWD (Serial
   Wire Debug) with SWO (Serial Wire Output) Trace. ITM requires at a
   minimum CCSv5.5 and emupack 5.1.340.0 with an XDS2xx or XDS110 (Note:
   your XDS may need a firmware update to work with "SWD with SWO
   Trace". See your XDS vendor for firmware update instructions).

CPTLib
^^^^^^

-  The Common Platform Tracer modules provides profile information via
   STM messages for critical buses within the device. CPTLib provides
   low level CP Tracer module setup. The provided use case based helper
   file combined with CPTLib makes for an easy to use environment. For
   examples see `Common platform Tracer
   Examples <http://processors.wiki.ti.com/index.php/Common_Platform_Tracer_Examples>`__. For debug
   help see `Debugging with Common Platform
   Tracer <http://processors.wiki.ti.com/index.php/Debugging_With_Common_Platform_Tracer>`__.

cTools_UCLib
^^^^^^^^^^^^

-  The cTools_UCLib is a library for Keystone family devices (C66xx,
   TCI66xx, 66AK2Hxx, 66AK2Exx and TCI6630K2L) that consolidates the
   most common CP Tracer and AET/DSP Trace uses cases into a single
   library. The Library also consolidates ETB setup and operation into a
   few easy to use functions.

-  Use cases supported include:

   -  Exception tracking with DSP Trace
   -  Application Program Counter Trace
   -  Illegal Memory Access Watching with DSP Trace
   -  CP Tracer Strategic Bus Throughput and Latency profiling
   -  Function Statistical Profiling with DSP Trace

-  Keystone Ctools_UCLib examples (platform specific CCS projects) are
   available as a separate zip package in the file repository listed
   below.
-  Keystone Ctools_UCLib examples are also available as a part of
   Keystone MCSDK instrumentation. For more details please refer to
   `Keystone MCSDK instrumentation
   examples <http://processors.wiki.ti.com/index.php/BIOS_MCSDK_2.0_User_Guide#cToolsLibrary>`__
-  For more information about Ctools use-cases, please refer to
   Ctools_UCLib doxygen at Ctools_UCLib/doc/Ctools_UCLib.html/index.html

PMICMILib
^^^^^^^^^

-  The PMI and CMI units provide power and clock state profiling via STM
   messages. The PMICMILib provides a common programming and control API
   for both units. For more details see `OMAP4 Power and Clock
   management
   Profiling <http://processors.wiki.ti.com/index.php/OMAP4_Power_and_Clock_Management_Profiling>`__.

Linux Kernel Driver for STM printf
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Linux kernel module device driver enables applications to use MIPI
   STM as a standard character device driver. Users can redirect output
   (from printf) to a STM device, or directly write() to the STM device
   from their application. For details and examples see `STM Linux
   Device Driver <http://processors.wiki.ti.com/index.php/STM_Linux_Device_Driver>`__.

SCILib
^^^^^^

-  The OMAP44xx and OMAP54xx Statistic Collectors provides profile data
   for SDRAM load monitoring and Master load and Latency monitoring.
   Data is exported as STM messages. SCILib provides a use case based
   API for configuring and controlling bus profile data for all the
   statistic collectors on a device.

-  Use cases supported include:

   -  Average Throughput (for SDRAM and Master SC Modules)
   -  Link Occupancy (for SDRAM and Master SC Modules)
   -  Average Burst Length (for SDRAM and Master SC Modules)
   -  Average Latentcy (For Master SC Module only)

Examples
--------

-  The CToolsLib examples package contains device or platform specific
   CCSv5 examples, which portrays typical use case scenarios involving
   individual or multiple CTools libraries. These examples also show how
   to integrate various CTools libraries into one's application SW.

-  The following are the various supported devices or platforms:

   -  Keystone1 family of devices (C667x, C665x and TCI661x)
   -  Keystone2 family of devices (66AK2Hxx, 66AK2Exx and TCI6630K2L)
   -  TCI648x family of devices
   -  OMAP family of devices (OMAP44xx and OMAP54xx)
   -  C6A816x family of devices
   -  DRA7xx family of devices

Documentation
-------------

-  There is a generated Doxygen API description included with each
   CToolsLib.

Download
--------

All cToolsLib libraries and example source are available in the links
below. After downloading the zips you need, simply expand each zip under
the same top level directory. All library and example projects are
compatible with CCSv6.

+-----------------------+-----------------------+-----------------------+
| Library               | Purpose               | File Repository       |
+=======================+=======================+=======================+
| GettingStarted        | Provides processor    | `GettingStarted       |
|                       | specific notes for    | <http://downloads.ti  |
|                       | libraries and         | .com/emulation/esd/	|
|                       | examples              | ctoolslib/GettingStar |
|                       |                       | ted.htm>`__           |
+-----------------------+-----------------------+-----------------------+
| STMLib                | Software Message      | `STMLib_5.2 <http://d |
|                       | Library               | ownloads.ti.com/emula |
|                       |                       | tion/esd/ctoolslib/ST |
|                       |                       | MLib_5.2.zip>`__      |
+-----------------------+-----------------------+-----------------------+
| AETLib                | Software library for  | `aet_4.18 <http://dow |
|                       | programmatically      | nloads.ti.com/emulati |
|                       | using the 64x+ AET    | on/esd/ctoolslib/aet_ |
|                       | hardware breakpoint   | 4.18.zip>`__          |
|                       | and watchpoint units. |                       |
|                       | Also useful for       |                       |
|                       | triggering/halting    |                       |
|                       | trace.                |                       |
+-----------------------+-----------------------+-----------------------+
| ETBLib                | Software Library for  | `ETBLib_1.22 <http:// |
|                       | configuring and       | downloads.ti.com/emul |
|                       | retrieving the ETB    | ation/esd/ctoolslib/E |
|                       | contents.             | TBLib_1.22.zip>`__    |
+-----------------------+-----------------------+-----------------------+
| ETMLib                | Software Library for  | `ETMLib_0.6 <http://d |
|                       | configuring ARM       | ownloads.ti.com/emula |
|                       | CortexA8 Core Trace   | tion/esd/ctoolslib/ET |
|                       | triggering.           | MLib_0.6.zip>`__      |
+-----------------------+-----------------------+-----------------------+
| DSPTraceLib           | Software Library to   | `DSPTraceLib_1.14 <ht |
|                       | configure DSP Trace   | tp://downloads.ti.com |
|                       | export                | /emulation/esd/ctools |
|                       |                       | lib/DSPTraceLib_1.14. |
|                       |                       | zip>`__               |
+-----------------------+-----------------------+-----------------------+
| cTools_UCLib          | Library that          | `Ctools_UCLib_1.5 <ht |
|                       | configures key        | tp://downloads.ti.com |
|                       | Keystone CP Tracer    | /emulation/esd/ctools |
|                       | and DSP Trace Use     | lib/Ctools_UCLib_1.5. |
|                       | Case                  | zip>`__               |
+-----------------------+-----------------------+-----------------------+
| PMICMILib             | Power and Clock       | `PMICMILib_1.3 <http: |
|                       | management            | //downloads.ti.com/em |
|                       | Instrumentation       | ulation/esd/ctoolslib |
|                       | Library               | /PMICMILib_1.3.zip>`_ |
|                       |                       | _                     |
+-----------------------+-----------------------+-----------------------+
| SCILib                | Statistic Collector   | `SCILib_1.5 <http://d |
|                       | Instrumentation       | ownloads.ti.com/emula |
|                       | Library               | tion/esd/ctoolslib/SC |
|                       |                       | ILib_1.5.zip>`__      |
+-----------------------+-----------------------+-----------------------+
| CPTLib                | CP Tracer             | `CPTLib_0.15 <http:// |
|                       | Instrumentation       | downloads.ti.com/emul |
|                       | Library               | ation/esd/ctoolslib/C |
|                       |                       | PTLib_0.15.zip>`__    |
+-----------------------+-----------------------+-----------------------+
| ITMLib                | Instrumentation Trace | `ITMLib_1.1 <http://d |
|                       | Macrocell Library     | ownloads.ti.com/emula |
|                       |                       | tion/esd/ctoolslib/IT |
|                       |                       | MLib_1.1.zip>`__      |
+-----------------------+-----------------------+-----------------------+
| Examples              | CToolsLib Examples    | `Examples_5.9 <http:/ |
|                       |                       | /downloads.ti.com/emu |
|                       |                       | lation/esd/ctoolslib/ |
|                       |                       | Examples_5.9.zip>`__  |
+-----------------------+-----------------------+-----------------------+
| Ctools_UCLib_Examples | CTools Use-Case       | `Ctools_UCLib_	|
|                       | Library Examples      | Examples_1.3 <http://	|
|                       |                       | downloads.ti.com/	|
|                       |                       | emulation/esd/ctool	|
|                       |                       | slib/Ctools_UCLib_	|
|                       |                       | Examples_1.3.zip>`__	|
+-----------------------+-----------------------+-----------------------+

|

The latest release of all libraries now come with CCS projects. Please
refer GettingStarted.htm for more details.

Trace Decoding
--------------

To decoder trace from a binary dump of the ETB memory, two tools are
avaialble:

**Bin2TDF utility**

Refer here for the detail on using `BIN2TDF. <http://processors.wiki.ti.com/index.php/BIN2TDF>`__

**TD utility**

Refer here for the detail on using
`TD <http://processors.wiki.ti.com/index.php/TD>`__ .



Support
-------

-  `Support Forum - Please put CToolsLib in
   title <http://e2e.ti.com/support/development_tools/code_composer_studio/f/81.aspx>`__

.. rubric:: Frequent Asked Questions (FAQ)
   :name: frequent-asked-questions-faq

.. rubric:: Q: Can I get the source code?
   :name: q-can-i-get-the-source-code

-  A: The source code is included with each library.

.. rubric:: Q: How do I know if my device supports CTools?
   :name: q-how-do-i-know-if-my-device-supports-ctools

-  A: The datasheet or Technical Reference Manual (TRM) will usually
   contain details on the features support and avaialble on your device.
   If you are unsure, you may wish to ask in the support forum.

.. rubric:: Q: Do I have to use CToolsLib with `Code Composer
   Studio <http://processors.wiki.ti.com/index.php/Code_Composer_Studio>`__?
   :name: q-do-i-have-to-use-ctoolslib-with-code-composer-studio

-  A: No, other tools such as Lauterbach Trace32 can be used with the
   CToolsLib. Please contact your tools vendor regarding support.

.. rubric:: Q: Do you have approximate cycle counts for each library?
   :name: q-do-you-have-approximate-cycle-counts-for-each-library

-  A: For `AETlib <http://processors.wiki.ti.com/index.php/AETlib>`__ there is a file called
   "aetlib_profiling_stats.txt" that gives this information
-  A: For ETBLib, on the TI c6x compiler on a 64x+ device, it takes
   approximately 1000 cycles per call at the "-o2" optimization level.

.. rubric:: Q: Do you have the code size for each library?
   :name: q-do-you-have-the-code-size-for-each-library

-  A: For `AETlib <http://processors.wiki.ti.com/index.php/AETlib>`__ there is a file called
   "aetlib_size_stats.txt" that gives this information
-  A: For ETBLib, on the TI c6x compiler on a 64x+ device, it is
   approximately 4KB at the "-o2" optimization level.

.. rubric:: Q: What license is this code provided under? / Is the code
   GPL compatible?
   :name: q-what-license-is-this-code-provided-under-is-the-code-gpl-compatible

-  A: The header files in CToolsLib will have the relevant licenses.
   Generally, CToolsLib is licnesed under modified BSD license which is
   GPL compatible. Please see `this wikipedia
   article. <http://en.wikipedia.org/wiki/BSD_License#3-clause_license_.28.22New_BSD_License.22_or_.22Modified_BSD_License.22.29>`__

.. rubric:: Related
   :name: related

-  `TI.com XDS560 Product Page <http://www.ti.com/tool/TMDSEMU560V2STM-U>`__
-  `XDS560v2 System Trace <http://processors.wiki.ti.com/index.php/XDS560v2_System_Trace>`__
-  `CTools <http://processors.wiki.ti.com/index.php/CTools>`__
-  `How OMAP software developers use System Trace to boost
   performance <http://e2e.ti.com/blogs_/b/mobile_momentum/archive/2011/01/03/how-omap-software-developers-use-system-trace-to-boost-performance.aspx>`__
-  `Using System Trace (STM) <http://processors.wiki.ti.com/index.php/Using_System_Trace_(STM)>`__
-  Etblib Example
   `Here <http://processors.wiki.ti.com/index.php/Capturing_ETB_Trace_Data_With_ETBLib>`__

