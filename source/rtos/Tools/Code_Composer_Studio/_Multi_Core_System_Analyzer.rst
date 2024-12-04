.. http://processors.wiki.ti.com/index.php/Multicore_System_Analyzer

.. rubric:: Overview
   :name: overview

System Analyzer is a real-time tool for analyzing, visualizing and
profiling application running on single or multi core systems. Data is
collected using UIA (Unified Instrumentation Architecture) software
instrumentation on the target and transported via Ethernet, run-mode
JTAG, stop-mode JTAG, USB or UART to the host PC for analysis and
visualization in Code Composer Studio.

In a multi core system, data from all cores are correlated to a single
timeline.

.. Image:: /images/SA.png
.. rubric:: Unified Instrumentation Architecture (UIA)
   :name: unified-instrumentation-architecture-uia

UIA is the target-side package which defines the APIs, transports,
interfaces and guidelines that enable developers to instrument embedded
software in a way that is portable and flexible. It enables the creation
of advanced tooling that can be used both in the lab and in the field.
The framework includes:

-  a messaging infrastructure that allows instrumentation clients to
   interact with instrumentation endpoints on a target device while the
   target is running
-  an extensible set of commands and messages that can be sent over the
   messaging infrastructure
-  protocols to be used by the target-side instrumentation framework and
   the host-side instrumentation client
-  built-in instrumentation for DSP/BIOS for 'out of the box' real-time
   visibility into the operation of the O/S
-  guidelines on how to instrument other RTOSes

.. rubric:: Portable and Flexible
   :name: portable-and-flexible

System Analyzer and UIA are designed to be portable and flexible:

-  ISA independent: UIA can be re-used across a wide range of TI
   platforms, single-core devices and multi-core devices
-  O/S independent: UIA not tied to any specific operating system
-  Transport independent: can use a wide variety of different transports
   to upload software events from the target to the host, without having
   to change the source code
-  Platform independent: Host-side tooling works on both Windows and
   Linux platforms
-  IDE independent: Host-side tooling will support both tight
   integration with Code Composer Studio and stand-alone operation for
   use with other IDEs.

System Analyzer together with it's UIA packages define an
instrumentation framework that enables the development of
instrumentation client tools, instrumented target content,
infrastructure components, and instrumentation middleware components
that interoperate and can be re-used across TI platforms and devices.

.. rubric:: Available Analysis
   :name: available-analysis

-  RTOS Execution Graph
-  CPU Load
-  Task Load
-  Duration Analysis
-  Context-aware Function Profiler
-  Concurrency Analysis
-  Task Profiler
-  Count/Statistical Analysis

.. rubric:: Execution Graph
   :name: execution-graph

Graphical representation of RTOS context switches, events, semaphores,
HWIs and SWIs. Start/Stop events logged for Duration Analysis and
Enter/Exit events logged for Function Profiler are also shown in graph.
In a multi core system all cores are shown in the same graph on the same
timeline.

.. rubric:: CPU Load
   :name: cpu-load

Graphical representation and min, max, average statistics of CPU loading
data collected from RTOS.
In a multi core system loading and statistics for all cores are shown.

.. rubric:: Task Load
   :name: task-load

Graphical representation and min, max, average statistics of task
loading data collected from RTOS.
In a multi core system different instance of analysis can be opened for
each core.

.. rubric:: Duration Analysis
   :name: duration-analysis

Analyze time to perform operations. Start/Stop events logged for each
operation is used to calculate and graph the time for each instance of
each operation. Summary statistics (including count, min, max and
average) is also shown for each operation.

.. rubric:: Context Aware Function Profiler
   :name: context-aware-function-profiler

Min, max and average inclusive time (includes time spend in called
functions) and exclusive time (excludes time spent in called functions)
for functions. Functions to be profiled must have their entry and exit
instrumented. See FAQ below on how to leverage compiler entry/exit hook
functions. For context awareness, RTOS context switch logging must also
be enabled.

.. rubric:: Concurrency Analysis
   :name: concurrency-analysis

This is a multi-core tool to analyze parallel execution of application
across multiple cores. RTOS Idle task is use to determine when the core
is not in use. Task switch logging must be enabled for this analysis.

.. rubric:: Task Profiler
   :name: task-profiler

The task profiler analyzes what percent of time tasks are spending in
their different states. RTOS context switch events are required for this
analysis.

.. rubric:: Count/Statistical Analysis
   :name: countstatistical-analysis

Graphical representation of any counter/variable that is being logger.
Also calculates number of occurrences and min, max, average value for
each counter/variable.

**Note:** TIRTOS/SYSBIOS instrumentation is not enabled by default.
  See User Guide or Tutorials on how to enable this.

**Note:** More information on the analysis features is available in the
`System Analyzer User's Guide <http://www.ti.com/lit/pdf/spruh43>`__.

.. rubric:: Documents and Tutorials
   :name: documents-and-tutorials

`System Analyzer Getting Started
Guide </images/7/7b/MCSA1.1_Getting_Started_Guide.pdf>`__ - Get familar
with System Analyzer features using a data file shipped with CCStudio.

`System Analyzer User's Guide </images/b/bc/MCSA1.1_User_Guide.pdf>`__ -
Detail guide on configuring and using System Analyzer and UIA.

`System Analyzer Tutorials
(CCSv5) <http://processors.wiki.ti.com/index.php/System_Analyzer_Tutorials_(CCSv5)>`__ - Includes a
series of projects that can be built and use, along with step-by-step
walkthroughs of how to configure code, set up System Analyzer, work with
Analysis Features, etc.

.. rubric:: System Analyzer and the MCSDK Demo
   :name: system-analyzer-and-the-mcsdk-demo

System Analyzer provides visibility into the real-time behavior and
performance of the `BIOS MCSDK
2.0 <http://processors.wiki.ti.com/index.php/BIOS_MCSDK_2.0_User_Guide>`__
Image Processing Demo. The `System Analyzer and the MCSDK
Demo <http://processors.wiki.ti.com/index.php/MCSA_and_the_MCSDK_Demo>`__
page provides more information about how to use System Analyzer with the
MCSDK.

.. rubric:: Known Issues/Errata
   :name: known-issueserrata

.. rubric:: CCS Crash when opening Graph in System Analyzer
   :name: ccs-crash-when-opening-graph-in-system-analyzer

-  It appears that some graphics card drivers are not compatible with
   Eclipse support for text rotation. This may result in a CCS crash
   (inside the graphics driver) when opening graphs in System Analyzer
   (graphs use text rotation for y-axis label). If you encounter this
   problem, try updating the graphics card driver. This has resolved the
   occurrences of this problem we've seen so far.

.. rubric:: Multicore correlation not working
   :name: multicore-correlation-not-working

-  Multicore event correlation is not automatically supported for JTAG
   transports (it is supported for Ethernet). User can explicitly add
   synchronization logs to enable correlation. (See `Tutorial
   4B <http://processors.wiki.ti.com/index.php/System_Analyzer_Tutorial_4B>`__
   for details)
-  if the target is halted (either by explict halt or implicit halts
   such as Console I/O / CIO) while data is being collected via Ethernet
   then correlation will not work.
-  if some target is generating data very infrequently then correlation
   may timeout resulting in uncorrelated data. In this case the data can
   be saved to a binary file and post process for correlation to work.

.. rubric:: uia_1_00_04_35 : Tutorial 1 and Tutorial 2 do not build
   properly.
   :name: uia_1_00_04_35-tutorial-1-and-tutorial-2-do-not-build-properly.

-  The build fails with the error *"dc.services.global.XDCException:
   xdc.PACKAGE_NOT_FOUND: can't locate the package 'ti.sysbios.knl'"*
-  To overcome this, please unzip

.. Image:: /images/UIAMetaData.zip
   <uia_1_00_04_35 install folder>/packages/ti/uia/runtime/ to update
   the UIAMetaData.xs file. Then delete the <Debug> folder from your
   project and rebuild.

.. rubric:: uia_1_03_00_02 : JTAG Transport does not work properly on
   some devices.
   :name: uia_1_03_00_02-jtag-transport-does-not-work-properly-on-some-devices.

-  Project builds cleanly, System Analyzer starts normally, but no
   events are captured.
-  To overcome this, please use
   `uia_1_03_01_08 <http://downloads.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/uia/1_03_01_08/index_FDS.html>`__
   or later.

.. rubric:: FAQs
   :name: faqs

.. rubric:: Q: When can I use System Analyzer auto configuration
   :name: q-when-can-i-use-system-analyzer-auto-configuration

When launching a Live or Binary File session users can choose to let
System Analyzer auto configure itself. For this to work you must:

-  have a debug session running with the symbol/program file loaded
-  generated rta and uia xml file (*program*.rta.xml and
   *program*.uia.xml) files should be located where the project
   generated them or in the same folder as the .out file
-  if using Ethernet transport it is expected that IP address is output
   in the console

.. rubric:: Q: Configuring System Analyzer when auto configuration is
   not possible
   :name: q-configuring-system-analyzer-when-auto-configuration-is-not-possible

See **Configuring System Analyzer Transport and Endpoints** in Chapter 4
of the `System Analyzer User's
Guide <http://www.ti.com/lit/pdf/spruh43>`__.

.. rubric:: Q: Can I launch System Analyzer before the target if running
   :name: q-can-i-launch-system-analyzer-before-the-target-if-running

If using Ethernet transport, System Analyzer expects that the target is
up and running and the Ethernet connection is established before it is
started. For JTAG transport the target does not have to be running.

.. rubric:: Q: What happens if the target is halted while collecting
   data using Ethernet transport
   :name: q-what-happens-if-the-target-is-halted-while-collecting-data-using-ethernet-transport

Halting the target may result in the ethenet connection getting
disconnected. The connection can be re-established using the **connect**
button.

.. rubric:: Q: How to Profile functions using enter and exit hook
   functions
   :name: q-how-to-profile-functions-using-enter-and-exit-hook-functions

In order to do inclusive and exclusive profiling of functions(using
Context Aware Profiler of System Analyzer), a UIA log is needed at the
entry and exit point of functions. One can add entry and exit hook
functions to every function in the source by doing the following

Use the following compiler options when compiling the source

::

    --entry_hook=functionEntryHook
    --entry_parm=address
    --exit_hook=functionExitHook
    --exit_parm=address

To use the required UIA events, need this include

.. code-block:: c

    #include <ti/uia/events/UIABenchmark.h>

|
| Add entry and exit hook functions to the source (The below one is for
  Context aware function profiling)

.. code-block:: c

    void functionEntryHook( void (*addr)() ){
        Log_write3(UIABenchmark_startInstanceWithAdrs, (IArg)"context=0x%x, fnAdrs=0x%x:",(IArg)0, (IArg)addr);
    }

    void functionExitHook( void (*addr)() ){
        Log_write3(UIABenchmark_stopInstanceWithAdrs,  (IArg)"context=0x%x, fnAdrs=0x%x:",(IArg)0, (IArg)addr);
    }

For CCS 5.5 and later

.. code-block:: c

    void functionEntryHook( void (*addr)() ){
        Log_write2(UIAProfile_enterFunctionAdrs, (IArg)0, (IArg)addr);
    }

    void functionExitHook( void (*addr)() ){
        Log_write2(UIAProfile_exitFunctionAdrs,  (IArg)0, (IArg)addr);
    }

|
| The 1st parameter after the message string( 3rd parameter to
  Log_write3) is a context parameter (For CCS 5.5 and later is the 2nd
  parameter to Log_write2) and can be used to specify an additional
  level of qualification (e.g. Task Context). For our purpose out here
  we can ignore this and just set it to 0.

If task aware profiling is needed, the Task context has to be logged.
SYS/BIOS automatically logs events for task switches and SWI and HWI
Start and Stop events. See Enabling and Disabling logging Sec 5.2.2 in
the `System Analyzer User's
Guide <http://www.ti.com/lit/pdf/spruh43>`__. Context change can also be
explicitly logged by the application. For more on Profiling using system
analyzer refer to Section 3.5,4.12 of the user's guide.

**Profiling Results when using Libraries:** Hook functions will not be
added and hence called from functions in libraries that have been linked
in. This will cause the Exclusive counts of the functions making calls
to the Library, to include the Library functions duration.

.. rubric:: Trouble Shooting
   :name: trouble-shooting

.. rubric:: System Analyzer Events or Packets are being dropped
   :name: system-analyzer-events-or-packets-are-being-dropped

See **Troubleshooting System Analyzer Connections** section in the
`System Analyzer User's Guide <http://www.ti.com/lit/pdf/spruh43>`__.

.. rubric:: No Events showing up in System Analyzer Views
   :name: no-events-showing-up-in-system-analyzer-views

See **Troubleshooting System Analyzer Connections** section in the
System Analyzer User's Guide.

.. rubric:: System Analyzer cannot connect to the target to retrieve
   logs
   :name: system-analyzer-cannot-connect-to-the-target-to-retrieve-logs

See **Troubleshooting System Analyzer Connections** section in the
System Analyzer User's Guide.

.. rubric:: System Analyzer Events do not make sense
   :name: system-analyzer-events-do-not-make-sense

See **Troubleshooting System Analyzer Connections** section in the
System Analyzer User's Guide.

.. rubric:: Time values in the logs are too large
   :name: time-values-in-the-logs-are-too-large

See **Troubleshooting System Analyzer Connections** section in the
System Analyzer User's Guide.

.. rubric:: Technical Support and Product Updates
   :name: technical-support-and-product-updates

For technical discussions and issues, please visit

-  `E2E Processor Support:
   https://e2e.ti.com/support/processors/ <https://e2e.ti.com/support/processors/>`__
-  `BIOS Embedded Software forum:
   http://e2e.ti.com/support/embedded/f/355.aspx <http://e2e.ti.com/support/embedded/f/355.aspx>`__
-  `Embedded Processors wiki:
   http://processors.wiki.ti.com <http://processors.wiki.ti.com>`__

Note: When asking for help in the forum you should tag your posts in the
Subject with "System Analyzer", the part number (e.g. "C6678"), and
component (e.g. "UIA").

|
| For product updates,

-  Use the CCS/Eclipse Update Manager (see the Getting Started Guide
   above)

