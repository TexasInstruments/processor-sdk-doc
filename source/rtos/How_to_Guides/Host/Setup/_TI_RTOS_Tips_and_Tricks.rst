TI RTOS Tips & Tricks
----------------------------

.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS:_TI_RTOS_Tips_And_Tricks

Description
^^^^^^^^^^^

The intent of this article is to address common issues that TI RTOS users may run into while configuring SYSBIOS, XDCTools or working with RTSC packages in general on DSP and ARM devices. This is meant to provide insight into build and configuration issue nd must be used as an addendum document by Processor  SDK USer to the `SYSBIOS FAQs <http://processors.wiki.ti.com/index.php/SYS/BIOS_FAQs>`__ and `XDCtools/RTSC documentation <http://rtsc.eclipse.org/docs-tip/XDCtools_User's_Guide>`__ and `TI RTOS Training <https://training.ti.com/ti-rtos-workshop-series>`__

RTSC Diagnostics: Understanding XDC build errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Some of the commonly observed XDC errors have been shown below. We try to explain how to understand and take corrective action.


xdc.tools.configuro:  can't locate the package 'Package Name' along the path: ...
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This indicates that one of the packages that you linked in your BIOS configuration, can`t be located under XDCPATH. The XDC tools uses XDC paths like library search path, so if you run into this issue check that all the component packages have been added to XDCPATH and there is no typo or non-existent paths that you have added to this variable. TI RTSC packages usually have the name ti.<package name>. The packages are named to also sometimes helps locate the package inside the component. For example '''ti.platforms.evmAM335x''' is located under BIOS_INSTALL_PATH/packages/'''ti/platforms/evmAM335x'''

For example if you are using packages from PDK (SOC driver packages)and BIOS (TI RTOS kernel), IPC (Interprocessor Communication) and NDK (Network development kit) then your XDCPATH needs to have following:

* BIOS_INSTALL_PATH/packages

* PDK_INSTALL_PATH/packages

* IPC_INSTALL_PATH/packages

* NDK_INSTALL_PATH/packages

xdc.cfg.SourceDir : Build of generated source libraries failed: exit status = 2:
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

A couple of different reasons could trigger this type of error

* Make sure there are no whitespaces or non-ASCII characters in any paths referenced by the build tools. In other words, make sure all software packages are installed in paths without spaces, and workspace and project names also do not have spaces or non-ASCII characters. We use gmake to build makefiles, and gmake doesn't deal well with spaces in directory and file names.

* Take a close look at the CCS build console and ensure that the sh.exe used for the build is the one from the CCS directory. Also check your system PATH variable and see if there is another sh.exe (or gmake.exe) in your system PATH earlier than the one from the CCS installation. If there is one, then that will be used for the build and could cause build errors such as this. Some toolchains that are known to include sh.exe and could cause a conflict are Cygwin, WinAVR, Yagarto.  In this case, remove those conflicting tools from the system PATH or modify the PATH so that the sh.exe and gmake.exe from CCS are seen first.

* Another source of problems related to sh.exe runnig Windows 10 may be Windows Defender. In "Windows Defender Security Centre", "App and browser control", "Exploit protection settings" one can add exceptions under "Program settings". Adding a rule for "sh.exe" to disable/override "Force randomisation for images (Mandatory ASLR)", "Randomise memory allocations (Bottom-up ASLR)",  "Validate stack integrity (StackPivot)".



xdc.tools.configuro: missing input config script
"""""""""""""""""""""""""""""""""""""""""""""""""

The XDCtools build command should normally have the configuration script (.cfg file) passed at the end of the command. If the .cfg is not getting passed correctly, then this message will appear in the CCS build console. This error will then result in other compiler errors further down in the build.

You can confirm if the root cause is the .cfg file not getting passed correctly by looking at the subdir_rules.mk file in the directory Debug (or Release) in your project. The command line that runs configuro usually looks like this: <br>

.. code:: console

    "C:/ti/xdctools_3_xx_xx_xx/xs" --xdcpath="..." xdc.tools.configuro -o configPkg -t ti.targets.elf.C674 -p ti.platforms.evm6747
    -r release -c "C:/ti/ccsv5/tools/compiler/c6000_x.x.x" --compileOptions "-g --optimize_with_debug" "$<"

Schema files not found
""""""""""""""""""""""""

Usually after creating a RTSC package, developers are supposed to run xdc release to generate the package that contains the .sch files but if you accidentally delete the package or the developers requires xdc release to be run in user environment, you can run into this issue. This issue can be resolved by adding XDCtools to your environment PATH variable and running the command xdc release

.. code:: console

    set PATH=$PATH;<XDC_INSTALL_PATH>
    xdc release

Detailed list of '''XDC Error codes''' and Troubleshoot can be found here:

* `XDCtools Error Codes <http://rtsc.eclipse.org/docs-tip/XDCtools_Error_Codes>`__
* `Trouble Shooting <http://rtsc.eclipse.org/docs-tip/Trouble_Shooting>`__


TI RTOS Platform configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Where does TI RTOS application get the Platform definition and memory sections on the SOC
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

When creating a TI RTOS project, the user is required to specify the Platform and target core as part of their RTSC setup as shown below. This shows an example that is created for evmAM335x platform.

.. Image:: /images/Platfrom_configuration.png
    :scale: 50 %

Selection of the platform essentially tell the build tools that the platform defintion should be picked up from the platform for evmAM335x from the directory path bios_x_xx_xx_xx\packages\ti\platforms\evmAM3359. If you open the Platform.xdc file under the folder path, you can see the default settings provided for this platform. This file combines the baseline AM335x SOC definition under bios_x_xx_xx_xx\packages\ti\catalog\arm\cortexa with the board specific setting like clockrate, DDR memory range.

How to create custom platform like DDRless platforms to use with TI RTOS projects
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

At some point in the application development process, most customers build their own boards, choosing a TI device and adding custom external memory.
You will also need to create your own platform if any of the following items are true:
* You want to customize cache sizes.
* You want to manually override the default section placement.
* You want application to run from on chip device memory.

For such custom boards you will need to create a platform using the platform wizard. The platform wizard is a GUI tool that allows you to easily create a custom platform. Creating a custom platform gives you a lot of flexibility in terms of defining the memory map and selecting default memory segments for section placement. This has been described in detail in following User guides and training links:

* `Section 7.2.2 in the TI RTOS User guide <http://www.ti.com/lit/ug/spruex3q/spruex3q.pdf>`__
* `Section 10.9 of  Application development with Processor SDK RTOS <http://software-dl.ti.com/public/hpmp/software/app_dev_procsdk_rtos/index.html>`__

How to place code and data sections in different memory location than set by default TI RTOS platform configuration
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

User can place specific code and data sections in desired location by using the following syntax in the configuration (.cfg)

.. code:: txt

    Program.sectMap[".data"] = new Program.SectionSpec();
    /* Set the load address for .data section */
    Program.sectMap[".data"].loadAddress = 0x82000000;
    /* Set the run address for .data section */
    Program.sectMap[".data"].runAddress = 0x82010000;

Generic TI RTOS questions
^^^^^^^^^^^^^^^^^^^^^^^^^^

What is relationship between TI RTOS and XDCtools and RTSC
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

`SYSBIOS <http://processors.wiki.ti.com/index.php?title=Category:SYSBIOS>`__ uses underlying technology provided by Real Time Software Components (RTSC).
* RTSC is an open-source specification within the Eclipse.org ecosystem for providing reusable software components (called "packages") for use in embedded systems.
* XDCtools is the actual product that contains all the tools necessary for you to use the SYS/BIOS components and configure your application. XDCtools is installed as part of Code Composer Studio (CCS). XDCtools is a separate software component provided by Texas Instruments that provides the underlying
tooling needed for configuring and building SYS/BIOS, NDK, and UIA.

RTSC and XDCtools are important to SYS/BIOS users because:

* `SYS/BIOS_as_a_set_of_RTSC_packages <http://dev.ti.com/tirex/content/simplelink_cc2640r2_sdk_2_40_00_32/docs/tirtos/sysbios/docs/cdoc/ti/sysbios/package.html>`__ containing the modules that make up the RTOS.

* `XDCtools provides configuration tools <http://rtsc.eclipse.org/docs-tip/XDCtools_User's_Guide>`__ you use to create and build a static configuration as part of your application. This \*.cfg configuration file specifies:

	* Which modules from XDCtools, SYS/BIOS, and other components to include in the run-time image.
	* What static instances of RTOS objects to create. For example, these include tasks and semaphores.
	* Settings for parameter values for modules and objects.

* `XDCtools provides critical APIs <http://rtsc.eclipse.org/docs-tip/Overview_of_xdc.runtime#Using_This_Package>`__ that are used by SYS/BIOS and other related software components. These include memory allocation, logging, and system control.

The `RTSC-pedia web site <http://rtsc.eclipse.org/docs-tip/Main_Page>`__ describes RTSC and XDCtools in more detail. In particular, it provides information for developers planning to create RTSC packages. It is also useful if you plan to edit configuration scripts with a text editor rather than using the XGCONF graphical editor provided withing CCS.


Can you use any SYSBIOS version with any version of XDCTools when creating create or migrating to TI RTOS based application development environment
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This is a frequent issue for new user of TI RTOS. SYSBIOS releases are usually validated with a specific version of XDCTools that is described in the Release notes. It is generally not recommended to mix and match SYSBIOS versions with older or newer than the versions described as you may run into incompatibility issues. TI simplifies this build environments by packaging the TI RTOS package with XDCtools or by providing SDKs with the compatible versions of SYSBIOS kernel and XDCtools.

For customers using TI DSP and ARM Processors, it is recommended to use Processor SDK RTOS for TI RTOS development and to setup the CCS environment such its Preferences are set to use the versions included in the SDK. This process has been described:
`Processor_SDK_RTOS_Setup_CCS <index_how_to_guides.html#setup-ccs-for-evm-and-processor-sdk-rtos>`__

Using SYSBIOS with GNU GCC (for ARM devices only)
""""""""""""""""""""""""""""""""""""""""""""""""""
The key care about of using SYSBIOS kernel on ARM based devices with GNU GCC compiler have been described in the article `SYS/BIOS_with_GCC_(CortexA) <http://processors.wiki.ti.com/index.php/SYS/BIOS_with_GCC_(CortexA)>`__

This wiki answers important questions about using SYSBIOS kernel with GNU GCC compiler like:
* `Changing entry point to an application <http://processors.wiki.ti.com/index.php/SYS/BIOS_with_GCC_(CortexA)#How_do_I_change_the_address_where_the_entry_point_function_.28_c_int00.29_gets_placed_.3F>`__

* `Recommended compiler and linker settings <http://processors.wiki.ti.com/index.php/SYS/BIOS_with_GCC_(CortexA)#Configure_SYS.2FBIOS>`__

* `Getting System_printf/printf (adding Semihosting support) <http://processors.wiki.ti.com/index.php/SYS/BIOS_with_GCC_(CortexA)#Why_is_System_printf.28.29.2Fprintf.28.29_not_working_.3F>`__

* `Creating make based TI RTOS application build using GNU GCC compiler and XDCtools <http://processors.wiki.ti.com/index.php/SYS/BIOS_with_GCC_(CortexA)#Build_Application_with_Configuration>`__

* `Configuring ARM MMU and cache settings <http://processors.wiki.ti.com/index.php/SYS/BIOS_with_GCC_(CortexA)#How_do_I_add_a_4KB_granularity_MMU_pages_on_Cortex-A8.2C_Cortex-A9_and_Cortex-A15_devices_.3F>`__

How do I port existing application developed on SYSBIOS application to SMP/BIOS
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

SYSBIOS supports SMP mode of operation on multi-core ARM and few dual core M3/M4 (IPU) subsytem present in Keystone and Sitara processors.

**Training Slides**: `SMP SYSBIOS Overview presentation <http://processors.wiki.ti.com/index.php/File:Public_SmpBiosSlides.pdf>`__.

To Porting existing SYS/BIOS applications to SMP/BIOS, you can use the follow steps described below:
* Merge existing separate applications into a single application.
* Merge separate platform memory definitions as necessary.
* Add this to your existing application’s config script:

.. code:: txt

    BIOS.smpEnabled = true;

* Use these SMP-aware clone modules in place of their xdc.runtime equivalents for SysMin, SysStd, LoggerBuf (in ti.sybios.smp package)

.. note::
    The existing Load module has been tweaked to provide minimal support for SMP.

* For initial sanity testing, force all tasks to run on core 0:

.. code:: txt

    Task.defaultAffinity = 0;

* Once basic functionality of the merged applications has been demonstrated, either remove Task.defaultAffinity setting or replace it with

.. code:: txt

    Task.defaultAffinity = Task.AFFINITY_NONE;

The above statement will guide RTOS kernel to deploy tasks based on availability in the cluster of compute cores processing in SMP mode.

Are there any Graphical tools to configure SYSBIOS configuration
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The easiest way for new users to add/configure new modules in the TI RTOS BIOS configuration is to use `XGCONF based graphical tool <http://rtsc.eclipse.org/docs-tip/RTSC%2BCCStudio_v4_QuickStart>`__


Thread Types
^^^^^^^^^^^^

What is the difference between SWIs and Tasks
"""""""""""""""""""""""""""""""""""""""""""""""

* A Swi is a non-blocking thread that runs to completion and can only be pre-empted by a higher priority Swi or a Hwi (interrupt). Swi's can pre-empt a Task thread when posted and run on the ISR (system) stack (i.e. they do not have their own stack).

* A Task thread on the other hand is a blocking thread and can be pre-empted by a higher priority Task or by Swi/Hwi. A task usually has a while loop that keeps the task executing continuously in the system as long as it is required in the application. Also, Tasks run on their own independent stack.

How to add house keeping functions in the idle Task
""""""""""""""""""""""""""""""""""""""""""""""""""""

If you want to use the idle time of the system to do some "housekeeping" jobs in the background, when the system is not active on interrupts or tasks, TI RTOS provides option to provide a task list or point to a housekeeping function which will run when no other thread is active in the system. The simplest syntax to add this to your code is shown below:

::

    Task.enableIdleTask = true;
    var Idle = xdc.useModule('ti.sysbios.knl.Idle');
    Idle.addFunc('&osTaskIdleFunc');

If you open the BIOS configuration in XGCONF, you will notice that user are allowed to enter upto 8 function in the function list.

Syntax to add idle functions is provided below

::

    var Idle = xdc.useModule('ti.sysbios.knl.Idle');
    Idle.idleFxns[0] = "&myIdle1";


Hardware Interrupts (HWI)
^^^^^^^^^^^^^^^^^^^^^^^^^^

How to configure Crossbar when setting up interrupts on DRA7xx/TDA2xx/AM57xx
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Some socs like AM571x and AM572x have a large number of interrupts requests to service the needs of its many peripherals and subsystems. All of the interrupt lines from the subsystems are not needed at the same time, so they have to be muxed to the irq-controller appropriately. In such places a interrupt controllers are preceded by an CROSSBAR that provides flexibility in muxing the device requests to the controller inputs.

Application developers have two options to setup interrupts on AM57xx/TDA2xx/DRA7xx devices which provide a crossbar mechanism to connect a given IRQ source to an IRQ line on the target cpu's interrupt controller. The device level chip support library provides functional APIs to map interrupt events to target core interrupt controller line.

For example SPI3_IRQ to the CROSSBAR input on DSP and M4, you can use the following:

DSP Core1 configuration of SPI3_IRQ to crossbar input 60:

::

    /* Configure xbar connect for MCSPI3: DSP_IRQ_43 (reserved) mapped to MCSPI3 intr */
       CSL_xbarIrqConfigure (CSL_XBAR_IRQ_CPU_ID_DSP1,
                             CSL_XBAR_INST_DSP1_IRQ_43, /* should match with C66 intc eventId used for event combiner that maps to DSP interrupts*/
                             CSL_XBAR_MCSPI3_IRQ);

IPU core1 configuration of SPI3_IRQ to crossbar input 43:

::

    /* Configure xbar connect for MCSPI3: IPU1_IRQ_60 (reserved) mapped to MCSPI3 intr */
       CSL_xbarIrqConfigure (CSL_XBAR_IRQ_CPU_ID_IPU1,
                             CSL_XBAR_INST_IPU1_IRQ_60, /* should match with M4 intNum used for HWI_create */
                             CSL_XBAR_MCSPI3_IRQ);

Here is how you would define the same interrupt handler for IPU statically in a configuration script:

::

    var Hwi = xdc.useModule('ti.sysbios.family.arm.m3.Hwi');
    var IntXbar = xdc.useModule('ti.sysbios.family.shared.vayu.IntXbar');
    // Connect IRQ 23 to Interrupt source index 86 (SPI3_IRQ)
    IntXbar.connectIRQMeta(60, 86);
    // Alternately, the connectIRQMeta API can be used. This
    // API expects XBAR instance number as an argument.
    //
    // Connect Xbar Instance 1 (IRQ 60) to Interrupt
    // source index 86 (MCSPI3_IRQ)
    //
    // IntXbar.connectMeta(1, 60);
    var hwiParams = new Hwi.Params();
    hwiParams.arg = 60;


Clocks and Timers
^^^^^^^^^^^^^^^^^^

What are the different clock and timer modules in TI RTOS that you should be aware of?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


* Timer Module
	* Manages timer peripherals
	* Provides target/device abstraction

* Clock Module
	* Manages BIOS “heartbeat”
	* Can schedule functions to fire in the future (one-shot or periodically)
	* Input can be configured to use Timer module “tick” or application “tick”

* Timestamp Module
	* Provides simple time stamping services for benchmarking code
	* Allows time stamping RTA logs

**BIOS Timer Architecture**

.. Image:: /images/BIOS_Timer_Architecture.png
   :scale: 50 %

**BIOS Clock Architecture**

.. Image:: /images/BIOS_Clock_Architecture.png
   :scale: 50 %


How to get accurate clock ticks from the clock module?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

The clock module uses the CPU clock setting that is provided by the default platform setting. For example, if the platform is set to AM335x, then the clock is assumed to be 550 MHz, so the clock ticks will be generated with period of 1.8 nanoseconds. '''TI RTOS doesn`t setup the device clocks, the device clock initiation is the responsibility of the initialization code''' (GEL file in debug environment and bootloader in production environment)

After, the clocks are configured, it is the responsibility of the application developer to inform BIOS of the CPU frequency so that accurate system ticks can be generated.

**Note:** For example if the core clock on AM335x is set to 720 MHz instead of default 550 Mhz, then users are required to add the following like the .cfg to inform BIOS kernel of the actual CPU setting.

::

   BIOS.cpuFreq.lo = 720000000;

We reiterate that this doesn`t change the actual frequency but only informs the OS of the change from default CPU freq setting.

How to set input frequency in SYSBIOS configuration and change timer used by clock module
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Timer.intFreq[index] determines the input clock that drivers the timer. In most cases the input clock is assumed to be the input clock used in TI EVM  (Example: 24 Mhz used on AM335x EVM). If you have a different input on your custom board users are required to change the input Freqency setting in their configuration. To change the dmtimer frequency in SYS/BIOS you need to add the following to your config file:

::

   var Timer = xdc.useModule('ti.sysbios.timers.dmtimer.Timer');
   Timer.intFreqs[index] = {hi: 0, lo: 19200000};

Where index is the SYS/BIOS timer ID.  Please remember that timer IDs do not necessarily match the number in the peripheral name.  For example on AM335x SYS/BIOS Timer 0 actually corresponds to DMTimer2 on the device.  Use the `Timer Mapping Table <http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/bios/sysbios/6_40_01_15/exports/bios_6_40_01_15/docs/cdoc/ti/sysbios/timers/dmtimer/doc-files/TimerTables.html>`__ to determine which timer corresponds to each Timer ID.

The Clock module uses a Timer internally.  By default, the Clock module calls Timer_create() with "ANY" which will return one of the available timers.  You can specify the exact timer using the following (the default value for Clock.timerId is ANY).


To set it to a specic timer Id, you can use the following syntax.

::

   Clock= xdc.useModule('ti.sysbios.knl.Clock');
   Clock.timerId = 3;


SemiHosting
^^^^^^^^^^^^^

Why can`t I see output of System_printf on CCS console?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

When getting started with TI RTOS, you may notice that the printf from your code goes to CCS console but using non-intrusive System_printf doesn`t. If you want to have System_printf output go to the same place as printf, add the following three lines to your .cfg file and re-build:

::

   var System = xdc.useModule('xdc.runtime.System');
   var SysStd = xdc.useModule('xdc.runtime.SysStd');
   System.SupportProxy = SysStd;

If you don't do this, the output will go to a circular buffer in memory. You can examine that buffer using the ROV tool (use the menu: Tools->ROV while in the debugger).

How to enable printf/System_printf to go to CCS IO console on ARM devices
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Application developers need to add the SemiHosting module to the .cfg manually by editing the config script. Add the following line:

::

   var SemiHostSupport = xdc.useModule('ti.sysbios.rts.gnu.SemiHostSupport');

This module does the required setup (install SVC_Handler and do the required file handle init) to support SemiHosting.

GNU GCC users on ARM platforms need to link to  "rdimon" library to the "GNU Linker" -> "Libraries" view. If the "nosys" library is already listed in the "Libraries" view then replace it with "rdimon". This will cause the application to link with librdimon.a library which is a Semi-Hosting enabled BSP library.


Exception Handling
^^^^^^^^^^^^^^^^^^

How can I get dump of registers when an exception occurs ?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

If you add this to your .cfg file:

::

   var Exception = xdc.useModule('ti.sysbios.family.c64p.Exception');
   Exception.enablePrint = true;

SYS/BIOS provides several target unique exception handlers:
* ti.sysbios.family.arm.exc.Exception - used by all Arm9 and A8 targets
* ti.sysbios.family.arm.m3.Hwi - used by all cortex-M3 targets
* ti.sysbios.family.c64p.Exception - used by all C6x targets

a complete exception register context should be dumped to the console in addition to the Error raised by the exception handler when an exception occurs.

If you set a breakpoint at "ti_sysbios_family_c64p_Hwi_int1", this is the function vectored to on all exceptions. No exception processing will have been performed at this point. Using CCS' register dump, you can see the complete state of the processor. The NRP register should contain the PC at the time the exception occurred.


How do I determine the call stack at the time of crash
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

A detailed view of analyzing the call stack using CCS tools when your TI RTOS application throws an exception has been described in the article:

* `Exception_Dump_Decoding_Using_the_CCS_Register_View <http://processors.wiki.ti.com/index.php/SYS/BIOS_FAQs#Exception_Dump_Decoding_Using_the_CCS_Register_View>`__



How can you route exception print to UART
""""""""""""""""""""""""""""""""""""""""""

The console I/O prints from TI-RTOS can be re-routed to UART. The console I/O messages are printed using the System module which can configured to call callback functions. These callback functions should be configured to write to UART. For example, in your .cfg add a configuration similar to the one below:

::

   /* ================ System configuration ================ */
   var System = xdc.useModule('xdc.runtime.System');
   var SysCallback = xdc.useModule('xdc.runtime.SysCallback');
   SysCallback.abortFxn = "&myUARTAbort";
   SysCallback.putchFxn = "&myUARTPutch";
   SysCallback.readyFxn = "&myUARTReady";
   System.SupportProxy = SysCallback;

And define the functions myUARTAbort, myUARTPutch and myUARTReady in your application. For details about the SysCallback module's callback function signature, please see this link.

For more details refer to the E2E discussion here: `Redirecting Exception logs to UART <https://e2e.ti.com/support/embedded/tirtos/f/355/t/459864>`__

Logging and Trace
^^^^^^^^^^^^^^^^^^

How get UIA logging working with TI RTOS application?
""""""""""""""""""""""""""""""""""""""""""""""""""""""

In order to get the UIA loggging enabled, you need to include the UIA module and indicate the modules on which you would like obtain the logging information in your application. For example the following configuration will enable Load, Task, Swi and Hwi logging and will enable Task profiler so that you gain visual insight into the execution of the TI RTOS application using System analyzer tools in CCS:

::

   var LoggingSetup = xdc.useModule('ti.uia.sysbios.LoggingSetup');
   LoggingSetup.loadLogging = true;
   LoggingSetup.loadLoggerSize = 1024;
   LoggingSetup.mainLoggerSize = 32768;
   LoggingSetup.sysbiosLoggerSize = 32768;
   LoggingSetup.sysbiosSwiLogging = true;
   LoggingSetup.sysbiosHwiLogging = true;
   LoggingSetup.sysbiosSemaphoreLogging = true;
   LoggingSetup.loadTaskLogging = true;
   LoggingSetup.loadSwiLogging = true;
   LoggingSetup.loadHwiLogging = true;
   LoggingSetup.enableTaskProfiler = true;
   LoggingSetup.sysbiosHwiLoggingRuntimeControl = true;
   LoggingSetup.sysbiosSwiLoggingRuntimeControl = true;
   LoggingSetup.eventUploadMode = LoggingSetup.UploadMode_JTAGSTOPMODE;


**System analyzer view :**

.. Image:: /images/System_Analyzer_Execution_log.png

**For more information refer to :**
`System Analyzer wiki <http://processors.wiki.ti.com/index.php/Multicore_System_Analyzer>`__

To see how XGCONF graphical tool can be used to add Logging setup, refer to `TI RTOS User Section 2.2 <http://www.ti.com/lit/ug/spruhd4m/spruhd4m.pdf>`__

What SYS/BIOS Debugging Tools do we have in CCS ?
""""""""""""""""""""""""""""""""""""""""""""""""""

* Real Time analysis(RTA) agent

* RTOS Object View(ROV)


Real Time analysis(RTA) agent
""""""""""""""""""""""""""""""

**Note:** Before Debugging the SYSBIOS Debugging options. It is recommended to set the Preferences under the Windows Tab in CCS to select the version of SYSBIOS, XDCTOOLS in Windows->Preferences->General->RTSC Options. Additionally set IPC and XDAIS if your application uses the components.

#. Real time analysis can easily be turned on in a SYSBIOS based CCS project using the Grace tools. Select the configuration file (.cfg) in your project this will open an available Resources view inside SYSBIOS. Under diagnostics, select the RTA agent and enable it and save the configuration. Rebuild the project with the new settings.
#. To run your project, choose **Target Debug Active Project** from the CCS menus. If this is the first time you are debugging a project for your target, you may need to set up a CCS Target Configuration. See the CCS help for details.
#. In the Debug perspective, open the Runtime Object Viewer (ROV) tool by choosing **Tools ROV**. Also open the Raw Logs view by choosing **Tools RTA Raw Logs**. These tools allow you to see the activity of RTSC and SYS/BIOS modules.
#. Set some breakpoints in the log.c source file. (You can do this by right-clicking on a line and choosing **New Breakpoint &gt; Breakpoint**.) For example, set a breakpoint on the last line of each function in log.c.
#. Run the application.
#. In the Raw Logs window, you can see the informational, warning, and error messages sent by the calls to Log module APIs in log.c. The messages that begin with **LM** are diagnostics provided by XDCtools. Messages that begin with “WARNING” come from calls to Log_warning2. Messages that begin with “ERROR” come from calls to Log_error2. Messages that begin with “../log.c” come from calls to Log_info0 and Log_info2 (depending on the number of arguments).</li>

.. Image:: /images/SYSBIOS_Diag.jpg
   :scale: 50 %

.. Image:: /images/SYSBIOS_Rawlog.jpg
   :scale: 50 %

.. Image:: /images/Rta_exec2.png

.. Image:: /images/SYSBIOS_CPUload.jpg
   :scale: 50 %

For advanced debugging options we recommend following the instructions on the `BIOS_6_Real-Time_Analysis_(RTA)_in_CCSv4 <http://processors.wiki.ti.com/index.php/BIOS_6_Real-Time_Analysis_(RTA)_in_CCSv4>`__ wiki


RTOS Object View(ROV)
"""""""""""""""""""""

#. Load your application for debugging. Select the device you want to debug before opening ROV.
#. In the ROV window, expand the tree to see the ti.sysbios.knl.Task module. The right pane shows a list of the Task threads in the application. As you advance from breakpoint to breakpoint, you see the run mode of the threads change.</li></ol>

.. Image:: /images/1.7.6_Image.png
   :scale: 50 %

For more details on ROV tools, refer to the `Runtime Object Viewer(ROV) <http://rtsc.eclipse.org/docs-tip/Runtime_Object_Viewer>`__ article on RTSC website.

Memory and Heap
^^^^^^^^^^^^^^^^

What kind of heap should I use in SYSBIOS application and how do I allocate Heap in my configuration
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
SYSBIOS Supports five different type of Heap implementation:

* HeapMin. Very small code footprint implementation. Supports non blocking memory allocation, but does not support freeing memory.
* HeapMem. Allocate variable-size blocks and uses Gate module to protect allocation and freeing of memory. typically Slower and non-deterministic
* HeapBuf. Allocate fixed-size blocks. Fast deterministic and non-blocking as allocation uses same size.
* HeapMultiBuf. Specify variable-size allocation, but internally allocate from a variety of fixed-size blocks. Good tradeoff for HeapMem and HeapBuf
* HeapTrack. Used to detect memory allocation and deallocation problems. Good for debugging as it detects memory leaks and buffer overflows.

Typical allocation of static heap within the SYSBIOS \*.cfg file is shown below:

::

   var HeapMem = xdc.useModule('ti.sysbios.heaps.HeapMem');
   /* Create a Heap. */
   var heapMemParams = new HeapMem.Params();
   heapMemParams.size = 0x8000000;                             // <-- edit this value to tune the size of the heap
   heapMemParams.sectionName = "systemHeapMaster";
   Program.global.heap0 = HeapMem.create(heapMemParams);
   Memory.defaultHeapInstance = Program.global.heap0;


Benchmarks
^^^^^^^^^^^

Where can I find Memory foot print, Interrupt latency and performance numbers of the TI RTOS when designing my system
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The Memory footprint and Interrupt latency for different processor architectures is provided in the SYSBIOS package. It can be located at
 bios_6_xx_xx_xx/packages/ti/sysbios/benchmarks/doc-files

The Foot print of the OS depends on number of BIOS kernel modules used by the application but an estimate of the foot print can be computed by adding up the module footprint numbers to the base kernel footprint. The interrupt latency is mostly deterministic in the system but OS response may depend on priority of the interrupt setup. If the 2 or more interrupts occur simultaneously, the premptive BIOS scheduler will let the higher HWI to run before letting the one with lower priority so it may seem as the the lower priority interrupt response is slightly slower.

Debugging
^^^^^^^^^^

How to debug common application issues like stack overflow, exception and memory leaks
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Common Application debug scenarios like exception management, memory leak and stack issues have been described in the following training video:
`Debugging Common Application Issues TI RTOS <https://training.ti.com/debugging-common-application-issues-ti-rtos>`__

The training covers stack over flow, exception handling and memory management issues in detail with a Lab for TI MCU devices but the same concepts and features also apply for TI ARM and DSP processors.


How to add Custom compiler options  and build custom BIOS library
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Users are allowed to change the libType and specify the compiler options from their BIOS configuration using the following

::

   BIOS.libType = BIOS.LibType_Custom;
   // For Cortex A8 device like AM335x
   BIOS.customCCOpts = "--endian=little -mv7A8 --abi=eabi --neon --float_support=vfpv3 -q -ms --program_level_compile -o3 --opt_for_speed=3"
   // For Cortex A9 device like AM437x
   BIOS.customCCOpts ="-mcpu=cortex-a9 -mfpu=neon -mfloat-abi=hard -mabi=aapcs -O3 -Wunused -Wunknown-pragmas -ffunction-sections -fdata-sections -g "

To remove a given compiler setting, you can use:

::

   BIOS.customCCOpts = BIOS.customCCOpts.replace(" -g ","");

