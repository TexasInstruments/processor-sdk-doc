.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_PROFILING

Overview
--------

Introduction
^^^^^^^^^^^^

The profiling library can be used to profile any of the Platform
Development Kit components at the runtime. Feature enables reporting of
cpu cycles measurement for PDK driver components in order to analyze and
meet constraint requirement for a real time application. Profiling
module uses hardware clock of PMU to measure length of each task in
processor cycles with minimal overhead. It use standard C programming
hooks that may be adapted for any platform and/or processor
architecture.

Integration
-----------

**Baremetal or No-OS Use case**

Reference Utils library path to be included in application build
environment.

::

    -l <ti/utils/profiling/lib/[cpu]/>

Reference lld library path to be included.(Replace profile suffix
library with original one)

::

    -l <ti/drv/uart/lib/[soc]/[cpu]/lld.profiling>

Example:

::

    -l "ti/utils/profiling/lib/armv7/ti.utils.profiling.aa15fg" -l "ti/drv/uart/lib/armv7/ti.drv.uart.profiling.aa15fg>

**SysBIOS based application**

Refer \*.cfg of Uart test application for sample implementation


1. Load utils package.

::

    var Utils = xdc.loadPackage('ti.utils.profiling');

2. Set the ‘enableProfiling’ attribute to ‘true’ into the .cfg file.
This will load library with profiling enabled

::

    var Uart = xdc.loadPackage('ti.drv.uart’);
    Uart.Settings.enableProfiling = true;

3. Enable DDR3 memory, if not already enabled in test/example
application

::

    Program.sectMap[".fardata:benchmarking"] = "DDR3";

4. Add following line in .cfg if it does not exist already. Enable the
Task hooks for Task switches.

::

    var Task = xdc.useModule('ti.sysbios.knl.Task');

    Task.addHookSet({
    registerFxn: '&TaskRegisterId',
    switchFxn: '&mySwitch',
    });

**Additional compiler flags**

1. For gcc compiler add

::

    -gdwarf-3 -finstrument-functions

2. For TI compiler add

::

    --entry_parm=address --exit_hook=ti_utils_exit --exit_parm=address --entry_hook=ti_utils_entry

Reference: \*project.txt inside UART test application

Rebuild the project
-------------------

.. rubric:: Profiling Processing
   :name: profiling-processing

All LLD Test/DMATest projects located under "LLD/test/" has profiling
configuration enabled by default.

Load compiled program onto desired target and platform. Run program to a
desired logical point where profiling data needs to be collected

1. While program is at the break, open the Memory Browser (View > Memory
Browser).

2. Save a memory snapshot by clicking "Save", setting the start address
to "elemlog" and length to "log_idx*4". (It is preferred to save it into
ti .dat format.)

|

.. rubric:: Profiling Post-processing
   :name: profiling-post-processing

**Host Environment:Windows or Ubuntu** **Tools dependencies:**

+------------+---------------------------------------------------+
| Tools      | Download                                          |
+============+===================================================+
| python 2.7 | https://www.python.org/downloads/                 |
+------------+---------------------------------------------------+
| pyelftools | https://github.com/eliben/pyelftools              |
+------------+---------------------------------------------------+
| tabulate   | https://pypi.python.org/pypi/tabulate             |
+------------+---------------------------------------------------+
| XlsxWriter | https://pypi.python.org/pypi/XlsxWriter#downloads |
+------------+---------------------------------------------------+

(Follow the standard instruction for installing the tools from their
websites.)

**Running the script**

Open a cmd/terminal & set to the directory of the "decodeProfileDump.py"
Python script (typically under utils/profiling/scripts)

::

    python decodeProfileDump.py -flags [log 1] [executable 1]

Example:

::

    python decodeProfileDump.py -v uart.dat UART_BasicExample_k2h_armTestproject.out

**Optional flags**

+-----------------------------------+-----------------------------------+
| Flags                             | Response                          |
+===================================+===================================+
| -v                                | Display verbose output            |
+-----------------------------------+-----------------------------------+
| –t                                | Breakdown function totals by      |
|                                   | their reference sites             |
+-----------------------------------+-----------------------------------+
| –x                                | Print the tabulated results into  |
|                                   | a report.xlsx Excel file          |
+-----------------------------------+-----------------------------------+
| -csv                              | Print the tabulated results into  |
|                                   | a report.csv file                 |
+-----------------------------------+-----------------------------------+
| -off N                            | Manual instrumentation offset of  |
|                                   | N cycles, subtracted from each    |
|                                   | function.                         |
+-----------------------------------+-----------------------------------+

(The instrumentation program already generates an offset from itself
that is subtracted from the function times. Use this flag only if there
is an additional offset you would like to subtract.)

**Report Fields**

+-----------------------------------+-----------------------------------+
| Term                              | Meaning                           |
+===================================+===================================+
| Function                          | Name of instrumented function     |
+-----------------------------------+-----------------------------------+
| Referenced_By                     | Call site of instrumented         |
|                                   | function                          |
+-----------------------------------+-----------------------------------+
| Total_Cycles                      | Inclusive/Exclusive processor     |
|                                   | cycles elapsed for instrumented   |
|                                   | function                          |
+-----------------------------------+-----------------------------------+
| Average_Cycles                    | Processor cycles elapsed for      |
|                                   | instrumented function per         |
|                                   | reference                         |
+-----------------------------------+-----------------------------------+
| Total_Calls                       | Number of times instrumented      |
|                                   | function is called                |
+-----------------------------------+-----------------------------------+
| Average_Calls                     | Number of times instrumented      |
|                                   | function is called per reference  |
+-----------------------------------+-----------------------------------+
| Iterations                        | Number of times instrumented      |
|                                   | function was referenced           |
+-----------------------------------+-----------------------------------+

(inclusive(inc): including the cycles of its child functions within,
exclusive(exc): excluding the cycles of its child functions.)

.. note::

   Remaining functions on the stack at last timestamp will be considered
   closed.

   BIOS functions are not accounted by instrumentation and will not appear
   in the report.

   Functions which are optimized out will not appear in the report eg.
   empty/single-line functions, ``ti_sysbios_*`` functions etc.

|
