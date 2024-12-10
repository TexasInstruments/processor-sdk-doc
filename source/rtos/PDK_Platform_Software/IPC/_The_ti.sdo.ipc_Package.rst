.. http://processors.wiki.ti.com/index.php/IPC_Users_Guide/The_ti.sdo.ipc_Package

.. |ipcSdoRun_Img1| Image:: /images/Book_run.png
                 :target: http://downloads.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/ipc/latest/docs/doxygen/html/files.html

Introduction
-----------------
This page introduces the modules in the ti.sdo.ipc package.

.. note::
  This package is not used on HLOS-based cores. Although this is a BIOS-only package,
  note that the BIOS-side of a HLOS<->BIOS IPC-using application will need to bring in a subset of these packages into the BIOS-side configuration scripts.

The ``ti.sdo.ipc`` package contains the following modules that you may use in your applications:

   +----------------------------+------------------------------------+----------------------------------+
   |         Module             |      Module Path                   |         Description              |
   +============================+====================================+==================================+
   |`GateMP Module <index_      | GateMP                             | Manages gates for mutual         |
   |Foundational_Compon         |                                    | exclusion of shared resources    |
   |ents.html#gatemp-           |                                    | by multiple processors and       |
   |module>`__                  |                                    | threads.                         |
   |                            |                                    | See `GateMP Module <index_       |
   |                            |                                    | Foundational_Compon              |
   |                            |                                    | ents.html#gatemp-                |
   |                            |                                    | module>`__                       |
   +----------------------------+------------------------------------+----------------------------------+
   |`HeapBufMP Module <index_   | ti.sdo.ipc.heaps.HeapBufMP         | Fixed-sized shared memory        |
   |Foundational_               |                                    | Heaps. Similar to SYS/BIOS's     |
   |Components.html#heapmp-     |                                    | ti.sysbios.heaps.HeapBuf         |
   |module>`__                  |                                    | module, but with some            |
   |                            |                                    | configuration differences.       |
   |                            |                                    | See `HeapMP Module <index_       |
   |                            |                                    | Foundational_                    |
   |                            |                                    | Components.html#heapmp-          |
   |                            |                                    | module>`__                       |
   +----------------------------+------------------------------------+----------------------------------+
   |`HeapMemMP Module <index_   | ti.sdo.ipc.heaps.HeapMemMP         | Variable-sized shared memory     |
   |Foundational_               |                                    | Heaps.                           |
   |Components.html#heapmp-     |                                    | See `HeapMP Module <index_       |
   |module>`__                  |                                    | Foundational_                    |
   |                            |                                    | Components.html#heapmp-          |
   |                            |                                    | module>`__                       |
   +----------------------------+------------------------------------+----------------------------------+
   |`HeapMultiBufMP Module      | ti.sdo.ipc.heaps.HeapMultiBufMP    | Multiple fixed-sized shared      |
   |<index_Foundational_        |                                    | memory Heaps.                    |
   |Components.html#heapmp-     |                                    | See `HeapMP Module <index_       |
   |module>`__                  |                                    | Foundational_                    |
   |                            |                                    | Components.html#heapmp-          |
   |                            |                                    | module>`__                       |
   +----------------------------+------------------------------------+----------------------------------+
   |`Ipc Module <index_         | ti.sdo.ipc.Ipc                     | Provides Ipc_start() function    |
   |Foundational_               |                                    | and allows startup sequence      |
   |Components.html#ipc-        |                                    | configuration.                   |
   |module>`__                  |                                    | See `IPC Module <index_          |
   |                            |                                    | Foundational_                    |
   |                            |                                    | Components.html#ipc-             |
   |                            |                                    | module>`__                       |
   +----------------------------+------------------------------------+----------------------------------+
   |`ListMP Module <index_      | ti.sdo.ipc.ListMP                  | Doubly-linked list for           |
   |Foundational_               |                                    | shared-memory, multi-processor   |
   |Components.html#listmp-     |                                    | applications. Very similar to    |
   |module>`__                  |                                    | the ti.sdo.utils.List module.    |
   |                            |                                    | See `ListMP Module <index_       |
   |                            |                                    | Foundational_                    |
   |                            |                                    | Components.html#listmp-          |
   |                            |                                    | module>`__                       |
   +----------------------------+------------------------------------+----------------------------------+
   |`MessageQ Module <index_    | ti.sdo.ipc.MessageQ                | Variable size messaging          |
   |Foundational_               |                                    | module.                          |
   |Components.html#messageq-   |                                    | See `MessageQ Module <index_     |
   |module>`__                  |                                    | Foundational_                    |
   |                            |                                    | Components.html#messageq-        |
   |                            |                                    | module>`__                       |
   +----------------------------+------------------------------------+----------------------------------+
   | TransportShm               | ti.sdo.ipc.transports.TransportShm | Transport used by MessageQ       |
   |                            |                                    | for remote communication with    |
   |                            |                                    | other processors via shared      |
   |                            |                                    | memory.                          |
   |                            |                                    | See `MessageQ Module <index_     |
   |                            |                                    | Foundational_                    |
   |                            |                                    | Components.html#messageq-        |
   |                            |                                    | module>`__                       |
   +----------------------------+------------------------------------+----------------------------------+
   |`Notify Module <index_      | ti.sdo.ipc.Notify                  | Low-level interrupt              |
   |Foundational_               |                                    | mux/demuxer module.              |
   |Components.html#notify-     |                                    | See `Notify Module <index_       |
   |module>`__                  |                                    | Foundational_                    |
   |                            |                                    | Components.html#notify-          |
   |                            |                                    | module>`__                       |
   +----------------------------+------------------------------------+----------------------------------+
   | NotifyDriverShm            | ti.sdo.ipc.notifyDrivers.          | Shared memory notification       |
   |                            | NotifyDriverShm                    | driver used by the Notify        |
   |                            |                                    | module to communicate between    |
   |                            |                                    | a pair of processors.            |
   |                            |                                    | See `Notify Module <index_       |
   |                            |                                    | Foundational_                    |
   |                            |                                    | Components.html#notify-          |
   |                            |                                    | module>`__                       |
   +----------------------------+------------------------------------+----------------------------------+
   |`SharedRegion Module <index_| ti.sdo.ipc.SharedRegion            | Maintains shared memory for      |
   |Foundational_               |                                    | multiple shared regions.         |
   |Components.html#shared-     |                                    | See `SharedRegion Module <index_ |
   |region-module>`__           |                                    | Foundational_                    |
   |                            |                                    | Components.html#shared-region-   |
   |                            |                                    | module>`__                       |
   +----------------------------+------------------------------------+----------------------------------+

Additional modules in the subfolders of the ti.sdo.ipc package contain specific implementations of gates,
heaps, notify drivers, transports, and various device family-specific modules.

In addition, the ti.sdo.ipc package defines the following interfaces that you may implement as your own custom modules:

   +----------------------------+------------------------------------------+
   |         Module             |      Module Path                         |
   +============================+==========================================+
   |IGateMPSupport              | ti.sdo.ipc.interfaces.IGateMPSupport     |
   +----------------------------+------------------------------------------+
   |IInterrupt                  | ti.sdo.ipc.notifyDrivers.IInterrupt      |
   +----------------------------+------------------------------------------+
   |IMessageQTransport          | ti.sdo.ipc.interfaces.IMessageQTransport |
   +----------------------------+------------------------------------------+
   |INotifyDriver               | ti.sdo.ipc.interfaces.INotifyDriver      |
   +----------------------------+------------------------------------------+
   |INotifySetup                | ti.sdo.ipc.interfaces.INotifySetup       |
   +----------------------------+------------------------------------------+

The ``<ipc_install_dir>/packages/ti/sdo/ipc`` directory contains the following packages that you may need to know about:

 - **examples.** Contains examples.
 - **family.** Contains device-specific support modules (used internally).
 - **gates.** Contains GateMP implementations (used internally).
 - **heaps.** Contains multiprocessor heaps.
 - **interfaces.** Contains interfaces.
 - **notifyDrivers.** Contains NotifyDriver implementations (used internally).
 - **transports.** Contains MessageQ transport implementations that are used internally.

Including Header Files
^^^^^^^^^^^^^^^^^^^^^^^^

BIOS applications that use modules in the ti.sdo.ipc or ti.sdo.utils
package should include the common header files provided in
``<ipc_install_dir>/packages/ti/ipc/``. These header files offer a
common API for both SYS/BIOS and HLOS users of IPC.

The following example C code includes header files applications may need
to use. Depending on the APIs used in your application code, you may
need to include different XDC, IPC, and SYS/BIOS header files.

::

    #include <xdc/std.h>
    #include <string.h>

    /* ---- XDC.RUNTIME module Headers   */
    #include <xdc/runtime/Memory.h>
    #include <xdc/runtime/System.h>
    #include <xdc/runtime/IHeap.h>

    /* ----- IPC module Headers          */
    #include <ti/ipc/GateMP.h>
    #include <ti/ipc/Ipc.h>
    #include <ti/ipc/MessageQ.h>
    #include <ti/ipc/HeapBufMP.h>
    #include <ti/ipc/MultiProc.h>

    /* ---- BIOS6 module Headers         */
    #include <ti/sysbios/BIOS.h>
    #include <ti/sysbios/knl/Task.h>

    /* ---- Get globals from .cfg Header */
    #include <xdc/cfg/global.h>

Note that the appropriate include file location has changed from
previous versions of IPC. The XDCtools-generated header files are still
available in ``<ipc_install_dir>/packages/ti/sdo/ipc/``, but these
should not directly be included in runtime .c code.
You should search your applications for "ti/sdo/ipc" and "ti/sdo/utils"
and change the header file references found as needed. Additional
changes to API calls will be needed.

|ipcSdoRun_Img1| Documentation for all common-header APIs is provided in Doxygen format
in your IPC installation at
``<ipc_install_dir>/docs/doxygen/html/index.html``. The latest version
of that documentation is available
`online <http://downloads.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/ipc/latest/docs/doxygen/html/files.html>`__.


Standard IPC Function Call Sequence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For instance-based modules in IPC, the standard IPC methodology when
creating object dynamically (that is, in C code) is to have the creator
thread first initialize a *MODULE*\ \_Params structure to its default
values via a *MODULE*\ \_Params_init() function. The creator thread can
then set individual parameter fields in this structure as needed. After
setting up the *MODULE*\ \_Params structure, the creator thread calls
the *MODULE*\ \_create() function to creates the instance and
initializes any shared memory used by the instance. If the instance is
to be opened remotely, a unique name must be supplied in the parameters.

Other threads can access this instance via the *MODULE\_*\ open()
function, which returns a handle with access to the instance. The name
that was used for instance creation must be used in the
*MODULE*\ \_open() function.

In most cases, MODULE_open() functions must be called in the context of
a Task. This is because the thread running the MODULE_open() function
needs to be able to block (to pend on a Semaphore in this case) while
waiting for the remote processor to respond. The response from the
remote processor triggers a hardware interrupt, which then posts a
Semaphore to allow to Task to resume execution. The exception to this
rule is that MODULE_open() functions do not need to be able to block
when opening an instance on the local processor.

When the threads have finished using an instance, all threads that
called *MODULE\_*\ open() must call *MODULE*\ \_close(). Then, the
thread that called *MODULE*\ \_create() can call *MODULE*\ \_delete() to
free the memory used by the instance.

Note that *all* threads that opened an instance must close that instance
before the thread that created it can delete it. Also, a thread that
calls *MODULE*\ \_create() cannot call *MODULE*\ \_close(). Likewise, a
thread that calls *MODULE\_*\ open() cannot call *MODULE*\ \_delete().

Error Handling in IPC
^^^^^^^^^^^^^^^^^^^^^^^

Many of the APIs provided by IPC return an integer as a status code.
Your application can test the status value returned against any of the
provided status constants. For example:

::

    MessageQ_Msg     msg;
    MessageQ_Handle  messageQ;
    Int              status;

    ...
    status = MessageQ_get(messageQ, &msg, MessageQ_FOREVER);
        if (status < 0) {
            System_abort("Should not happen\n");
        }

Status constants have the following format: ``MODULE_[S|E]_CONDITION``.
For example, Ipc_S_SUCCESS, MessageQ_E_FAIL, and SharedRegion_E_MEMORY
are status codes that may be returned by functions in the corresponding
modules.
Success codes always have values greater or equal to zero. For example,
Ipc_S_SUCCESS=0 and Ipc_S_ALREADYSETUP=1; both are success codes.
Failure codes always have values less than zero. Therefore, the presence
of an error can be detected by simply checking whether the return value
is negative.

Other APIs provided by IPC return a handle to a created object. If the
handle is NULL, an error occurred when creating the object. For example:

::

    messageQ = MessageQ_create(DSP_MESSAGEQNAME, NULL);
    if (messageQ == NULL) {
        System_abort("MessageQ_create failed\n");
    }

Refer to the Doxygen documentation for status codes returned by IPC
functions.

