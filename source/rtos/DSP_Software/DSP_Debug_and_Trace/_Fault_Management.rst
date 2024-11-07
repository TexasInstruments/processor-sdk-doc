.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_FM

Introduction
------------

This section describes the Fault Management APIs and provides
information on how to instrument a DSP image for exception. This library
is currently supported for K2x devices only.

FM DSP Exception APIs & Usage
-----------------------------

A DSP application can create and install an exception hook configured
with the following features using the APIs provided by FM:

-  Retrieve DSP register status for a core dump
-  Halt system IO, such as DMAs
-  Inform remote DSPs an exception has occurred
-  Inform ARM/Host a DSP exception has occurred

.. rubric:: Retrieving Last Register Status
   :name: retrieving-last-register-status

An exception hook function that intends to create a core dump must call
the following API:

``void Fault_Mgmt_getLastRegStatus(void);``

The API stores relevant DSP core register values into the memory region
mapped to the fault_mgmt_data data array for the core dump that is
provided to the ARM/Host.

.. rubric:: Halting System IO
   :name: halting-system-io

When a DSP exception is detected, invoking the FM instrumented exception
hook function, system IO that offload data transfers can be stopped
using the following API:

``Fault_Mgmt_haltIoProcessing(Fm_GlobalConfigParams *fmGblCfgParams, Fm_HaltCfg *haltCfg)``

The API provides the ability to disable all or subsets of the following
system IO:

-  AIF2 PE (Tx) and PD (Rx) channels
-  EDMA3 DMA, QDMA, and INT channels
-  CPDMA Tx/Rx channels
-  SGMII switch

The exception hook can invoke this function in order to stop DSP enabled
IO from continuing data transfers that may wipe out data important to
deciphering the source of the DSP exception. However, care must be taken
to not disable resources in use by the ARM/Host. If this occurs the
ARM/Host may experience unstable behavior preventing it from properly
receiving and handling the DSP core dump.

.. rubric:: IO Halt Configuration Parameters
   :name: io-halt-configuration-parameters

The Fm_HaltCfg structure is used to define which system IO will be
disabled upon invocation of the IO halt API. A user can specify that an
entire IO be disabled or a subset of an IO be disabled. The Fm_HaltCfg
structure has the following parameters:

-  ``int32_t haltAif`` If set to a non-zero value, will halt all AIF2 PE
   and PD channels except those specified within the
   Fm_ExcludedResource's list. All AIF2 PE and PD channels will be
   disabled if the Fm_ExcludedResource's list is NULL.
-  ``int32_t haltSGMII`` If set to a non-zero value, will halt the SGMII
   ethernet switch.
   **Note:** This will prevent ARM Linux ethernet from working properly.
-  ``int32_t haltEdma3`` If set to a non-zero value, will halt all EMDA3
   DMA, QDMA, and INT channels except those specified within the
   Fm_ExcludedResource's list. All EDMA3 DMA, QDMA, and INT channels
   will be disabled if the Fm_ExcludedResource's list is NULL.
   **Note:** Some EDMA3 channels are used by ARM Linux to access
   NAND in UBIFS. UBIFS will not work correctly if these channels are
   halted.
-  ``int32_t haltCpdma`` If set to a non-zero value, will halt all CPDMA
   channels except those specified within the Fm_ExcludedResource's
   list. All CPDMA channels will be disabled if the
   Fm_ExcludedResource's list is NULL.
   **Note:** Some CPDMA channels are used by ARM Linux which will exhibit
   unknown behavior if the relevant CPDMA channels are halted.
-  ``Fm_ExcludedResource *excludedResources;`` List of specific system
   IO values that should not be disabled.

A customized version of the Fm_ExcludedResource's list can be created.
However, a version has been created and supplied in
*pdk_#_##_##_##\\packages\\ti\\instrumentation\\fault_mgmt\\device\\k2x\\src\\fm_device.c*
which already accounts for all resources used the ARM Linux kernel
delivered with the latest PROCSDK release.

.. note::
   Following the IO halt configuration defined in the FM test source code
   will diable all IO except that used by ARM Linux UBIFS and NFS.

.. rubric:: Informing Remote DSP Core's of Exception
   :name: informing-remote-dsp-cores-of-exception

Remote DSP cores can be informed of a DSP exception and told to halt
functioning using the following API:

``void Fault_Mgmt_notify_remote_core(uint32_t core_id);``

The DSP local to the exception will interrupt remote cores via their NMI
causing them to enter their own exception handling routine. This allows
all DSPs to be brought down when a single DSP exception occurs. In
multi-core application this may help preserve information relevant to
deciphering the root cause of the original DSP exception.

.. rubric:: Informing ARM/Host of DSP Exception
   :name: informing-armhost-of-dsp-exception

A DSP core can inform the ARM/Host an exception has occurred via the
following API:

``void Fault_Mgmt_notify(void);``

This function will notify the ARM/Host an exception has occurred via
Remoteproc and should be the last FM API called within the instrumented
exception hook function.

Instrumenting a DSP Application with FM Exception APIs
------------------------------------------------------

Create and install an exception hook in the DSP application that
utilizes the DSP FM APIs.

-  In the .cfg (Configuro Script) file of the application add following
   commands to create a section

::

    var devType = "k2?";  /* Replace k2? with the k2 device in use k2e, k2h, k2k, or k2l */
    /* Load and use the Fault Management package */
    var Fault_mgmt = xdc.useModule('ti.instrumentation.fault_mgmt.Settings')
    Fault_mgmt.deviceType = devType;

    /*
     * The SysMin used here vs StdMin, as trace buffer address is required for
     * Linux trace debug driver, plus provides better performance.
     */
    Program.global.sysMinBufSize = 0x8000;
    var System = xdc.useModule('xdc.runtime.System');
    var SysMin = xdc.useModule('xdc.runtime.SysMin');
    System.SupportProxy = SysMin;
    SysMin.bufSize = Program.global.sysMinBufSize;

    /* Configure resource table for trace only.
       Note that traceOnly parameter should not
       be set if application is using MessageQ based IPC
       to communicate between cores.
     */
    var Resource = xdc.useModule('ti.ipc.remoteproc.Resource');
    Resource.loadSegment = Program.platform.dataMemory;
    Resource.traceOnly = true;

    /* Load the Exception and register a exception hook */
    var Exception = xdc.useModule('ti.sysbios.family.c64p.Exception');
    Exception.exceptionHook = '&myExceptionHook';
    Exception.enablePrint = true;

    /* Add note section for coredump */
    Program.sectMap[".note"] = new Program.SectionSpec();
    Program.sectMap[".note"] = Program.platform.dataMemory;
    Program.sectMap[".note"].loadAlign = 128;

-  In a source/header file, create a exception hook function as follows

.. code-block:: c

    /* Fault Management Include File */
    #include <ti/instrumentation/fault_mgmt/fault_mgmt.h>

    Void myExceptionHook(Void)
    {
        uint32_t   i;
        Fm_HaltCfg haltCfg;
        uint32_t   efr_val;

        /* Copy register status into fault management data region for ARM/Host */
        Fault_Mgmt_getLastRegStatus();

        memset(&haltCfg, 0, sizeof(haltCfg));
        efr_val = CSL_chipReadEFR();

        /* If triggered exception originates from another core through
         * NMI exception don't need to halt processing and notify other cores
         * since the parent core where the exception originally triggered via
         * event would notify them.  This eliminates recursive exceptions */
        if (!(efr_val & 0x80000000)) {
            /* Halt all processing - Only need to be done on one core */
            haltCfg.haltAif = 1;
            haltCfg.haltCpdma = 1;
    #if EXCLUDE_LINUX_RESOURCES_FROM_HALT
            haltCfg.haltSGMII = 0;
            /* EDMA used by kernel to copy data to/from NAND in UBIFS */
            haltCfg.haltEdma3 = 0;
            haltCfg.excludedResources = &linuxResources[0];
    #else
            haltCfg.haltSGMII = 1;
            haltCfg.haltEdma3 = 1;
            haltCfg.excludedResources = NULL;
    #endif

            Fault_Mgmt_haltIoProcessing(&fmGblCfgParams, &haltCfg);

            for (i = 0; i < fmGblCfgParams.maxNumCores; i++) {
                /* Notify remote DSP cores of exception - WARNING: This will generate NMI
                 * pulse to the remote DSP cores */
                if (i != CSL_chipReadDNUM()) {
                    Fault_Mgmt_notify_remote_core(i);
                }
            }
        }

        /* Notify ARM/Host of crash */
        Fault_Mgmt_notify();
    }

A sample test application is provided in
*pdk_#_##_##_##\\packages\\ti\\instrumentation\\fault_mgmt\\test\\k2x\\c66\\bios\\fmCoreDumpK2XC66TestProject*.
The test application uses the default resource exclusion list provided
with FM in
*pdk_#_##_##_##\\packages\\ti\\instrumentation\\fault_mgmt\\device\\k2x\\src*.
The default list has been configured to exclude all Linux owned IO from
the halting on exception. This allows the Linux kernel to remain
operational after DSP exception so that the core dump can be processed.

.. note::
   It is recommended that the IO halt configuration defined within #if
   EXCLUDE_LINUX_RESOURCES_FROM_HALT be used in addition to halting AIF and
   CPDMA if Linux must remain active after a DSP exception occurs. This IO
   halt configuration has been tested with both UBIFS and NFS. The
   documented configuration shuts down all IO except those needed by Linux
   to operate, such as EDMA3 (for access to NAND), the SGMII (for
   Ethernet), and Linux owned CPPI DMAs.


FM Global Configuration Parameters
----------------------------------

The Fm_GlobalConfigParams structure informs the IO halt and cleanup
features of the system peripheral resource ranges that could not be
pulled from CSL. The user should not create their own version of this
structure. Instead, the version of the structure provided within
*pdk_#_##_##_##\\packages\\ti\\instrumentation\\fault_mgmt\\device\\k2x\\src\\fm_device.c*
should be used. This structure has been statically created based on
device peripheral parameters.

FM Tests
--------

The Fault Management module comes with a single test application,
fmCoreDumpK2HC66TestProject. The fmCoreDumpK2HC66TestProject forces a
DSP exception which causes the FM core dump logic to execute. The
example can be run from CCS or downloaded from Linux via MPM. After
executing the application, from the Linux shell, check /var/log/syslog
for a message saying a crash event was detected on the DSP to which the
core dump test was loaded and run.

Additional References
---------------------

+-----------------------------------+-----------------------------------+
| **Document**                      | **Location**                      |
+-----------------------------------+-----------------------------------+
| Fault Management API Reference    | $(TI_PDK_INSTALL_DIR)\\packages\\ |
| Manual                            | ti\\instrumentation\\fault_mgmt\\ |
|                                   | docs\\doxygen\html\index.html     |
+-----------------------------------+-----------------------------------+
| Fault Management Release Notes    | $(TI_PDK_INSTALL_DIR)\\packages\\ |
|                                   | ti\\instrumentation\\fault_mgmt\\ |
|                                   | docs\\ReleaseNotes_fault_mgmt.pdf |
+-----------------------------------+-----------------------------------+

