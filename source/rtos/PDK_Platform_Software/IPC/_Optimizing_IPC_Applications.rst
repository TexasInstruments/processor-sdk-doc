.. http://processors.wiki.ti.com/index.php/IPC_Users_Guide/Optimizing_IPC_Applications

Compiler and Linker Optimization
----------------------------------

You can optimize your application for better performance and code size
or to give you more debugging information by selecting different ways of
compiling and linking your application. For example, you can do this by
linking with versions of the SYS/BIOS and IPC libraries that were
compiled differently.

The choices you can make related to compiler and linker optimization are
located in the following places:

-  **RTSC Build-Profile.** You see this field when you are creating a
   new CCS project or modifying the CCS Build settings. We recommend
   that you use the "release" setting. The "release" option is preferred
   even when you are creating and debugging an application; the "debug"
   option is mainly intended for internal use by Texas Instruments. The
   "release" option results in a somewhat smaller executable that can
   still be debugged. This build profile primarily affects how Codec
   Engine and some device drivers are built.

.. note::

   The "whole_program" and "whole_program_debug" options for the RTSC
   Build-Profile have been deprecated, and are no longer recommended.
   The option that provides the most similar result is to set the
   BIOS.libType configuration property to BIOS.LibType_Custom.


-  **CCS Build Configuration.** This setting in the CCS Build settings
   allows you to choose between and customize multiple build
   configurations. Each configuration can have the compiler and linker
   settings you choose.
-  **BIOS.libType configuration property.** You can set this property in
   XGCONF or by editing the .cfg file in your project. This property
   lets you select from two pre-compiled versions of the SYS/BIOS and
   IPC libraries or to have a custom version of the SYS/BIOS and IPC
   libraries compiled based on the needs of your application. See the
   table and discussion that follow for more information.

The options for the BIOS.libType configuration property are as follows:

+-------------+-------------+-------------+-------------+-------------+
| BIOS.libTyp | Compile     | Logging     | Code Size   | Run-Time    |
| e           | Time        |             |             | Performance |
+=============+=============+=============+=============+=============+
| Instrumente | Fast        | On          | Good        | Good        |
| d           |             |             |             |             |
| (BIOS.LibTy |             |             |             |             |
| pe_Instrume |             |             |             |             |
| nted)       |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Non-Instrum | Fast        | Off         | Better      | Better      |
| ented       |             |             |             |             |
| (BIOS.LibTy |             |             |             |             |
| pe_NonInstr |             |             |             |             |
| umented)    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Custom      | Fast (slow  | As          | Best        | Best        |
| (BIOS.LibTy | first time) | configured  |             |             |
| pe_Custom)  |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Debug       | Slower      | As          |             |             |
| (BIOS.LibTy |             | configured  |             |             |
| pe_Debug)   |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

-  **Instrumented.** (default) This option links with pre-built SYS/BIOS
   (and IPC) libraries that have instrumentation available. All Asserts
   and Diags settings are checked. Your configuration file can enable or
   disable various Diags and logging related settings. However, note
   that the checks to see if Diags are enabled before outputting a Log
   event are always performed, which has an impact on performance even
   if you use the ALWAYS_ON or ALWAYS_OFF setting. The resulting code
   size when using this option may be too large to fit on some targets,
   such as C28x and MSP430. This option is easy to use and debug and
   provides a fast build time.
-  **Non-Instrumented.** This option links with pre-built SYS/BIOS (and
   IPC) libraries that have instrumentation turned off. No Assert or
   Diag settings are checked, and logging information is not available
   at run-time. The checking for Asserts and Diags is compiled out of
   the libraries, so run-time performance and code size are optimized.
   Checking of Error_Blocks and handling errors in ways other than
   logging an event are still supported. This option is easy to use and
   provides a fast build time.
-  **Custom.** This option builds custom versions of the SYS/BIOS (and
   IPC) libraries that contain the modules and APIs that your
   application needs to access. If you have not used a particular module
   in your .cfg file or your C code (and it is not required internally
   by a SYS/BIOS module that is used), that module is not contained in
   the custom libraries compiled for your application. This option
   provides the best run-time performance and best code size given the
   needs of your application. Instrumentation is available to whatever
   extent your application configures it.

   The first time you build a project with the custom libType, the build
   will be longer. The custom libraries are stored in the "src"
   directory of your project. Subsequent builds may be faster; libraries
   do not need to be rebuilt unless you change one of the few
   configuration properties that affect the build settings, or you use
   an additional module that wasn't already used in the previous
   configuration.:

.. note::

   If you disable SYS/BIOS Task or Swi scheduling, you must use the
   "custom" option in order to successfully link your application.

   The custom option uses program optimization that removes many
   initialized constants and small code fragments (often "glue" code)
   from the final executable image. Such classic optimizations as
   constant folding and function inlining are used, including across
   module boundaries. The custom build preserves enough debug
   information to make it still possible to step through the optimized
   code in CCS and locate global variables.:

-  **Debug.** This option is not recommended; it is intended for
   internal use by Texas Instruments developers.

The following example statements set the BIOS.libType configuration
property:

::

    var BIOS = xdc.useModule('ti.sysbios.BIOS');
    BIOS.libType = BIOS.LibType_Custom;

If you use the custom option for the BIOS.libType, you can also set the
BIOS.customCCOpts property to customize the C compiler command-line
options used when compiling the SYS/BIOS libraries. If you want to
change this property, it is important to first examine and understand
the default command-line options used to compile the SYS/BIOS libraries
for your target. You can see the default in XGCONF or by placing the
following statement in your configuration script and building the
project:

::

    print("customCCOpts =", BIOS.customCCOpts);

Be careful not to cause problems for the SYS/BIOS compilation when you
modify this property. For example, the --program_level_compile option is
required. (Some --define and --include_path options are used on the
compiler command line but are not listed in the customCCOpts definition;
these also cannot be removed.)
For example, to create a debuggable custom library, you can remove the
-o3 option from the BIOS.customCCOpts definition by specifying it with
the following string for a C64x+ target:

::

    BIOS.customCCOpts = "-mv64p --abi=eabi -q -mi10 -mo -pdr -pden -pds=238 -pds=880
      -pds1110  --embed_inline_assembly --program_level_compile -g";


Optimizing Runtime Performance
--------------------------------

You can use one or more of the following techniques to improve the
runtime performance of IPC applications:

-  After you have finished debugging an application, you can disable
   asserts and logging with the following configuration statements:

::

       var Diags = xdc.useModule("xdc.runtime.Diags");
       var Defaults = xdc.useModule('xdc.runtime.Defaults');
       Defaults.common$.diags_ASSERT = Diags.ALWAYS_OFF;
       Defaults.common$.logger = null;

-  If shared memory has the same address on all processors, you can use
   the following configuration statement to set the
   SharedRegion.translate property to false. See `SharedRegion
   Module <index_Foundational_Components.html#shared-region-module>`__ for more
   about SharedRegion configuration.

::

       SharedRegion.translate = false;

-  Ensure that code, data, and shared data are all placed in cacheable
   memory. Refer to the SYS/BIOS documentation for information on how to
   configure a cache. See the *TI SYS/BIOS Real-time* *Operating System
   v6.x User's Guide* (`SPRUEX3 <http://www.ti.com/lit/pdf/SPRUEX3>`__)
   for details.
-  You can reduce contention between multiple processors and multiple
   threads by creating a new gate for use by a new IPC module instance.
   Leaving the params.gate property set to NULL causes the default
   system GateMP instance to be used for context protection. However, in
   some cases it may be optimal to create a new GateMP instance and
   supply it to the instance creation. See `GateMP
   Module <index_Foundational_Components.html#gatemp-module>`__ for more
   information. For example:

.. code-block:: c

       GateMP_Params gateParams;
       GateMP_Handle gateHandle;
       HeapBufMP_Params heapParams;

       GateMP_Params_init(&gateParams);
       gateHandle = GateMP_create(&gateParams);

       HeapBufMP_Params_init(&heapParams);
       heapParams.gate = gateHandle;


-  If a unicache is shared between two cores in shared memory and you
   expect to share certain IPC instances (such as a GateMP or ListMP)
   solely between those two cores, you may be able to improve
   performance by creating a SharedRegion with cache disabled for use
   between those two cores only. Since region 0 needs to be accessible
   by all cores on a system, region 1 can be created with a cache line
   size of 0 and a cacheEnable configuration of FALSE. Any IPC instance
   created within a SharedRegion inherits the cache settings (the
   cacheEnabled flag and the cacheLineSize) from this region. Therefore,
   unnecessary cache operations can be avoided by creating an instance
   in region 1.

   The following configuration statements create a SharedRegion with the
   cache disabled (on OMAP4430):

.. code-block:: c

       SharedRegion.setEntryMeta(1, /* Create shared region 1 */
           {   base: 0x86000000,
               len: 0x10000,
               ownerProcId: 0,
               isValid: true,
               cacheEnabled: false, /* Cache operations unneeded */
               cacheLineSize: 0, /* Cache padding unneeded */
               name: "DDR2",
           });


   The following C code creates a HeapBufMP instance in this
   SharedRegion::

.. code-block:: c

       HeapBufMP_Params heapParams;
       HeapBufMP_Handle heapHandle;

       HeapBufMP_Params_init(&heapParams);
       heapParams.regionId = 1;

       heapHandle = HeapBufMP_create(&heapParams);

   This heap can be used by either of the Cortex M3 cores on an
   OMAP4430, because they both share a unicache. Do not use this heap
   (or anything else belonging to a SharedRegion with caching disabled)
   from any other processor if the shared memory belonging to the
   SharedRegion is cacheable.

Optimizing Notify and MessageQ Latency
---------------------------------------

By default, IPC applications are configured to use the
ti.sdo.ipc.notifyDrivers.NotifyDriverShm Notify driver and the
ti.sdo.ipc.transports.TransportShm MessageQ transport. These modules are
used by default because they offer backward compatibility with older
IPC/SysLink releases. In addition, these modules may offer functionality
not supported by their newer, lower-latency counterparts.

If your application does not need functionality provided only by the
default Notify drivers or MessageQ transport, you can reduce the latency
by switching to alternative MessageQ transports and/or Notify drivers.

Choosing and Configuring Notify Drivers
----------------------------------------

To switch to a different Notify driver, set the Notify.SetupProxy
configuration to the family-specific Notify setup module. For example,
the following statements configure an application on the DM6446 to use
the NotifyDriverCirc driver for that device:

::

    var Notify = xdc.useModule('ti.sdo.ipc.Notify');
    Notify.SetupProxy = xdc.useModule('ti.sdo.ipc.family.dm6446.NotifyCircSetup');

|


IPC provides the following Notify drivers. Each has a corresponding
setup module that should be used as the Notify.SetupProxy module.

+-----------------------------------------------+-----------------------+-----------------------+
| Modules and                                   | Supports Disabling    | Latency               |
| Description                                   | and Enabling Events   |                       |
+===============================================+=======================+=======================+
| ti.sdo.ipc.notifyDrivers.NotifyDriverShm      | Yes                   | Default               |
| ti.sdo.ipc.family.<family>.NotifySetup        |                       |                       |
|                                               |                       |                       |
| |                                             |                       |                       |
|                                               |                       |                       |
| This shared-memory Notify driver offers       |                       |                       |
| room for a single pending notification        |                       |                       |
| in shared memory per event.                   |                       |                       |
|                                               |                       |                       |
+-----------------------------------------------+-----------------------+-----------------------+
| ti.sdo.ipc.notifyDrivers.NotifyDriverCirc     | No                    | Better than           |
| ti.sdo.ipc.family.<family>.NotifyCircSetup    |                       | NotifyDriverShm       |
|                                               |                       |                       |
| |                                             |                       |                       |
|                                               |                       |                       |
| This shared-memory                            |                       |                       |
| Notify driver uses a                          |                       |                       |
| circular buffer to                            |                       |                       |
| store notifications.                          |                       |                       |
| Unlike                                        |                       |                       |
| NotifyDriverShm, this                         |                       |                       |
| driver stores all                             |                       |                       |
| notifications in the                          |                       |                       |
| same circular buffer                          |                       |                       |
| (whose size is                                |                       |                       |
| configurable).                                |                       |                       |
+-----------------------------------------------+-----------------------+-----------------------+
| ti.sdo.ipc.family.ti8                         | No                    | Better than           |
| 1xx.\ **NotifyDriverM                         |                       | NotifyDriverCirc and  |
| bx**                                          |                       | NotifyDriverShm       |
| ti.sdo.ipc.family.ti8                         |                       |                       |
| 1xx.NotifyMbxSetup                            |                       |                       |
|                                               |                       |                       |
| |                                             |                       |                       |
|                                               |                       |                       |
| This TI81xx-only                              |                       |                       |
| Notify driver uses                            |                       |                       |
| the hardware mailbox.                         |                       |                       |
| This driver is not                            |                       |                       |
| usable by other                               |                       |                       |
| devices.                                      |                       |                       |
| Notifications are                             |                       |                       |
| stored in hardware                            |                       |                       |
| mailbox queues                                |                       |                       |
| present on TI81xx                             |                       |                       |
| devices.                                      |                       |                       |
+-----------------------------------------------+-----------------------+-----------------------+

Choosing and Configuring MessageQ Transports
---------------------------------------------

Similarly, to use an alternative MessageQ transport, configure the
MessageQ.SetupTransportProxy property to use the transport's
corresponding Transport Setup proxy. For example, to use the
TransportShmNotify module, use the following configuration:

::

    var MessageQ = xdc.module('ti.sdo.ipc.MessageQ');
    MessageQ.SetupTransportProxy =
          xdc.module('ti.sdo.ipc.transports.TransportShmNotifySetup');

Unlike the Notify setup modules, Transport setup modules are generally
not family-specific; most are located in the ti.sdo.ipc.transports
package.
IPC provides the following transports. Each has a corresponding setup
module for use as the MessageQ.SetupTransportProxy module.

+-----------------------------------+-----------------------------------+
| Modules and Description           | Transport Speed                   |
+===================================+===================================+
| ti.sdo.ipc.transports.\ **Transpo | Slowest                           |
| rtShm**                           |                                   |
| ti.sdo.ipc.transports.TransportSh |                                   |
| mSetup                            |                                   |
|                                   |                                   |
| |                                 |                                   |
|                                   |                                   |
| This shared-memory MessageQ       |                                   |
| transport uses ListMP to          |                                   |
| temporarily queue messages in     |                                   |
| shared memory before the messages |                                   |
| are moved to the destination      |                                   |
| queue. This transport is          |                                   |
| typically slowest because of the  |                                   |
| overhead of queuing messages      |                                   |
| using a linked list. This is the  |                                   |
| default MessageQ transport.       |                                   |
|                                   |                                   |
+-----------------------------------+-----------------------------------+
| ti.sdo.ipc.transports.\ **Transpo | Medium                            |
| rtShmCirc**                       |                                   |
| ti.sdo.ipc.transports.TransportSh |                                   |
| mCircSetup                        |                                   |
|                                   |                                   |
| |                                 |                                   |
|                                   |                                   |
| This shared-memory MessageQ       |                                   |
| transport uses a fixed-length     |                                   |
| circular buffer to temporarily    |                                   |
| queue messages in shared memory   |                                   |
| before the messages are moved to  |                                   |
| the destination queue. This       |                                   |
| transport is typically faster     |                                   |
| than TransportShm because of the  |                                   |
| efficiencies gained by using a    |                                   |
| circular buffer instead of a      |                                   |
| linked list.                      |                                   |
+-----------------------------------+-----------------------------------+
| ti.sdo.ipc.transports.\ **Transpo | Fastest, but depends on fast      |
| rtShmNotify**                     | processing of messages by         |
| ti.sdo.ipc.transports.TransportSh | receiver                          |
| mNotifySetup                      |                                   |
|                                   |                                   |
| |                                 |                                   |
|                                   |                                   |
| This shared-memory MessageQ       |                                   |
| transport does no buffering       |                                   |
| before the messages are moved to  |                                   |
| the destination queue. Because of |                                   |
| the lack of buffering, this       |                                   |
| transport tends to offer lower    |                                   |
| MessageQ latency than either      |                                   |
| TransportShm or TransportShm.     |                                   |
| However, If messages aren't       |                                   |
| received quickly enough by the    |                                   |
| receiver, the sender may spin     |                                   |
| while waiting for the receiver to |                                   |
| move the message to its local     |                                   |
| queue.                            |                                   |
+-----------------------------------+-----------------------------------+

Optimizing Shared Memory Usage
-------------------------------

You can use one or more of the following techniques to reduce the shared
memory footprint of IPC applications:

-  If some connections between processors are not needed, it is not
   necessary to attach to those cores. To selectively attach between
   cores, use pair-wise synchronization as described in `Ipc
   Module <index_Foundational_Components.html#ipc-module>`__. Your C code must
   call Ipc_attach() for processors you want to connect to if you are
   using pair-wise synchronization. The following configuration
   statement causes the Ipc module to expect pair-wise synchronization.

::

   Ipc.procSync = Ipc.ProcSync_PAIR;

|

At run-time, only call Ipc_attach() to a remote processor if one or
more of the following conditions is true::

   -  The remote processor is the owner of region 0.
   -  It is necessary to send Notifications between this processor and
      the remote processor.
   -  It is necessary to send MessageQ messages between this processor
      and the remote processor.
   -  It is necessary for either the local or remote processor to open a
      module instance using *MODULE*\ \_open() that has been created on
      the other processor.

-  Configure the Ipc.setEntryMeta property to disable components of IPC
   that are not required. For example, if an application uses Notify but
   not MessageQ, disabling MessageQ avoids the creation of MessageQ
   transports during Ipc_attach().

.. code-block:: c

           /* To avoid wasting shared mem for MessageQ transports */
           for (var i = 0; i < MultiProc.numProcessors; i++) {
               Ipc.setEntryMeta({
                   remoteProcId: 1,
                   setupMessageQ: false,
               });
           }

-  Configure Notify.numEvents to a lower number. The default value of 32
   is often significantly more than the total number of Notify events
   required on a system. See `Notify
   Module <index_Foundational_Components.html#notify-module>`__ for more
   information.

   For example, a simple MessageQ application may simply use two events
   (one for NameServer and one for the MessageQ transport). In this
   case, we can optimize memory use with the following configuration:

.. code-block:: javascript

    var Notify = xdc.useModule('ti.sdo.ipc.Notify');

    /* Reduce the total number of supported events from 32 to 2 */
    Notify.numEvents = 2;

    var NameServerRemoteNotify = xdc.useModule('ti.sdo.ipc.NameServerRemoteNotify');
    NameServerRemoteNotify.notifyEventId = 1;

    var TransportShm = xdc.useModule('ti.sdo.ipc.transports.TransportShm');
    TransportShm.notifyEventId = 0;

-  Reduce the cacheLineSize property of a SharedRegion to reflect the
   actual size of the cache line. IPC uses the cacheLineSize setting to
   pad data structures in shared memory. Padding is required so that
   cache write-back and invalidate operations on data in shared memory
   do not affect the cache status of adjacent data. The larger the
   cacheLineSize setting, the more shared memory is used for the sole
   purpose of padding. Therefore, the cacheLineSize setting should
   optimally be set to the actual size of the cache line. The default
   cacheLineSize for SharedRegion is 128. Using the correct size has
   both performance and size benefits.

   The following example (for C6472) sets the cacheLineSize property to
   64 because the shared L2 memory has this cache line size.

.. code-block:: c

           SharedRegion.setEntryMeta(0,
               { base: SHAREDMEM,
                 len: SHAREDMEMSIZE,
                 ownerProcId: 0,
                 isValid: true,
                 cacheLineSize: 64, /* SL2 cache line size = 64 */
                 name: "SL2_RAM",
               });

Optimizing Local Memory Usage
--------------------------------

If the Custom1 and Custom2 GateMP proxies will never be used, make sure
they are both plugged with the ti.sdo.ipc.gates.GateMPSupportNull GateMP
delegate. By default, GateMP plugs the Custom1 proxy with the
GatePeterson delegate. A considerable amount of local memory is reserved
for use by GatePeterson. You can plug the Custom1 proxy with the
GateMPSupportNull delegate by adding the following configuration
statements to your application:

.. code-block:: javascript

    var GateMP = xdc.useModule('ti.sdo.ipc.GateMP');
    GateMP.RemoteCustom1Proxy = xdc.useModule('ti.sdo.ipc.gates.GateMPSupportNull');

Optimizing Code Size
---------------------

This section provides tips and suggestions for minimizing the code size
of a SYS/BIOS-based application that uses IPC.

-  For a number of ways to configure SYS/BIOS that reduce code size by
   using custom built SYS/BIOS libraries and by disabling various
   features, see Section E.3 of the *TI SYS/BIOS Real-time Operating*
   *System v6.x User's Guide*
   (`SPRUEX3 <http://www.ti.com/lit/pdf/SPRUEX3>`__). In particular,
   after you have debugged your code, disabling Asserts as follows helps
   reduce the size of your code.

::
       var Defaults = xdc.useModule('xdc.runtime.Defaults');
       var Diags = xdc.useModule('xdc.runtimg.Diags');
       Defaults.common$.diags_ASSERT = Diags.ALWAYS_OFF;

-  The NotifyDriverCirc notification driver and the TransportShmNotify
   or TransportShmCirc MessageQ transports described in **Optimizing IPC
   Applications** use less code space than the default Notify driver and
   MessageQ transport.
-  You can reduce code size by not using the HeapBufMP Heap
   implementation. Since IPC uses the HeapMemMP implementation
   internally, using HeapMemMP in your application does not increase the
   code size. However, you should be aware that, depending on how your
   application uses heaps, HeapMemMP may lead to problems with heap
   fragmentation. See `Heap*MP
   Modules <index_Foundational_Components.html#heapmp-module>`__ for more about
   Heap implementations.

|


