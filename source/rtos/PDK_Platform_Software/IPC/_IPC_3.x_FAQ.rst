.. http://processors.wiki.ti.com/index.php/IPC_3.x_FAQ


I have a question that's not answered here, what now?
-----------------------------------------------------

-  There are lots of knowledgeable experts on the `TI E2E Support Forums <http://e2e.ti.com/>`__ - posts
   welcome!
-  Have you tried `Google <http://www.google.com>`__? IPC's been around
   a while, and Google has lots of details about it.

Does IPC 3.x support SMP BIOS?
--------------------------------

`SMP BIOS is described here <http://processors.wiki.ti.com/index.php/SMP/BIOS>`__. It is currently
only available for dual-core ARM M-class devices, sometimes called
"Benelli" or "Ducati".

Specifically where IPC 3.x is concerned, SMP BIOS is only applicable to
the following cores/devices:

-  IPU on OMAP54XX
-  IPU1 (and IPU2, if present) on DRA7XX (e.g. Vayu)

The answer to this question depends on whether you are developing an
HLOS-based or BIOS-based system.

+-----------------------------------+-----------------------------------+
| HLOS-Based                        | BIOS-Based                        |
| (e.g. Linux, QNX, Android on the  | (i.e. BIOS on the Cortex-A)       |
| Cortex-A)                         |                                   |
+===================================+===================================+
| IPC 3.x **only** supports SMP     | IPC 3.x supports either SMP BIOS  |
| BIOS on the IPU(s).               | or non-SMP BIOS. Note that        |
| In an HLOS-based system, the      | specifically on DRA7XX's          |
| IPU(s) are loaded and managed as  | **IPU2**, IPC 3.x only supports   |
| slaves (not peers).               | SMP BIOS (to reduce the number of |
|                                   | core-to-core permutations and     |
| When managing the IPU as a slave, | thus reduce the number of         |
| issues like power management,     | mailboxes required).              |
| loading/resetting, and error      | In a BIOS-based environment, the  |
| recovery are key features.        | IPU(s) are treated as peers (not  |
| Because the 2 cores in a single   | slaves), and as such some of the  |
| IPU can't easily be seen as truly | concerns about power management,  |
| independent (e.g. they share a    | loading, error recovery are no    |
| power domain), treating them as   | longer an issue.                  |
| one slave (running SMP BIOS) is   |                                   |
| simpler and more natural.         | Note that the MultiProc           |
|                                   | configuration used on all cores   |
|                                   | reflects your SMP-or-not-SMP      |
|                                   | decision. When using non-SMP      |
|                                   | BIOS, you must include "IPU1-0"   |
|                                   | and "IPU1-1" (rather than "IPU1"  |
|                                   | used when running SMP BIOS) in    |
|                                   | your MultiProc configuration. See |
|                                   | the ex11_ping example provided    |
|                                   | with the IPC product for an       |
|                                   | example that supports either      |
|                                   | "IPU1" or "IPU1-0 and IPU1-1".    |
+-----------------------------------+-----------------------------------+

Finally, there are a few notable benefits to using SMP BIOS. Many are
described in the `SMP/BIOS <http://processors.wiki.ti.com/index.php/SMP/BIOS>`__ article, but two are
highlighted here:

-  **Free load balancing** - SMP BIOS schedules tasks to run on the
   less-loaded core to balance IPU usage. Without SMP BIOS, when one of
   the cores became heavily loaded, users had to repartition the
   resources; often this meant moving tasks/code from one core to the
   other, which can affect memory maps, build/config scripts, etc.
-  **Simpler system integration** - there's one fewer core to manage the
   memory map and resource allocation for. Without SMP BIOS, the single
   unicache needed to understand AMMU and cache needs for both cores,
   and often confusing and error-prone integration issue.

Build Questions
-----------------

BIOS-side Build
^^^^^^^^^^^^^^^^

How do I change the Memory Map?
""""""""""""""""""""""""""""""""""

Standard techniques for changing the memory map of any BIOS executable
generally apply (e.g. `creating your own custom
platform <http://rtsc.eclipse.org/docs-tip/Demo_of_the_RTSC_Platform_Wizard_in_CCSv4>`__,
`creating an instance of an existing
platform <http://rtsc.eclipse.org/docs-tip/Using_Targets_and_Platforms>`__,
etc). However when building an executable which is loaded by an HLOS,
you also need to ensure the resource table is aligned with the memory
map. The `IPC Resource
customTable <index_Foundational_Components.html#resource-custom-table>`__ article describes
how to override the default resource table, which among other things,
includes the memory map.

Obviously be sure to also ensure changes to the memory map don't collide
with memory usage on other cores.

Why are the peripherals mapped to 0x6XXX:XXXX virtual memory for IPU (Cortex-M4) test images?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The ARM Cortex-M4 memory map includes a bit-banding region of memory
from 0x4000:0000 to 0x400F:FFFF and 0x4200:0000 to 0x43FF:FFFF. Here is
a Cortex-M4 memory map picture from ARM:

::

      http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0553a/CHDBIJJE.html

Many Vayu components running on the IPUs, including IPC, must access
peripherals physically located in this bit-banding region. As a result,
these accesses must be performed indirectly using a virtual memory
address, mapped using the IPU's AMMU.

Many of the components aligned on mapping this memory using one Large
AMMU page that maps 512M of physical memory beginning at 0x4000:0000 to
virtual memory beginning at 0x6000:0000. Then the components (by
default) access the peripherals using the 0x6XXX:XXXX address space.

-  IPC specifics:

IPC follows the convention of, by default, accessing memory physically
located at 0x4XXX:XXXX using virtual memory at 0x6XXX:XXXX. You can see
an example of this here - note the mailbox addresses configured here are
in the 06XXX:XXXX range:

::

       http://git.ti.com/cgit/cgit.cgi/ipc/ipcdev.git/tree/packages/ti/sdo/ipc/family/vayu/InterruptIpu.xs

In that same file, you can see that these addresses are configurable,
and the default 0x6XXX:XXXX addresses are only used if other addresses
haven't already been configured by the system integrator (e.g. in a .cfg
script). Users can override these default mailbox addresses using the
ti.sdo.ipc.family.vayu.InterruptIpu module's mailboxBaseAddr[] array,
documented here:

http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/ipc/latest/docs/cdoc/ti/sdo/ipc/family/vayu/InterruptIpu.html#metamailbox.Base.Addr

Linux Build
^^^^^^^^^^^^^

For details on the Linux build process see the `IPC Install Guide for
Linux <index_Foundational_Components.html#linux-install-guide>`__.

Try Cleaning First
"""""""""""""""""""

Sometimes the generated autotools makefiles can get confused, especially
if your often switching from one platform to another, between static and
dynamic libraries, etc. And sometimes simply cleaning and retrying can
help.

"make clean" does a 'light' cleaning, leaving the autotools-generated
config files so you can just retry 'make':

::

    # make clean
    #
    # make

"make distclean" does a more aggressive clean, requiring you to re-run
the config before running 'make':

::

    # make distclean
    #
    # make -f ipc-linux.mak
    # make

QNX Build
^^^^^^^^^^^

For details on the QNX build process see the `IPC Install Guide for
QNX <index_Foundational_Components.html#qnx-install-guide>`__.

How do I change the Memory Map?
""""""""""""""""""""""""""""""""

For the standpoint of the QNX OS, it owns all external memory by
default. When the 'ipc' resource manager is launched and the slave cores
are loaded, the resource table in each slave executable is read and
interpreted. All resource entries of type CARVEOUT are automatically
allocated from QNX-owned memory. Similarly, the first DEVMEM entry
always corresponds to the vring memory used by MessageQ and rpmsg_rpc,
and is also automatically allocated from QNX-owned memory, regardless of
which physical memory address is specified in the resource table entry.
If any other DEVMEM resource entry resides in external memory, QNX would
need to be told to not use that particular range. This is usually done
using the '-r' flag in the startup command in the 'build' file of the
QNX IFS (refer to your QNX BSP documentation for more details):

::

      startup-dra74x-vayu-evm -r0xBA300000,0x5A00000 -v -n852,668 -W -G

For example, the above '-r' flag would reserve 0x5A00000 bytes starting
at physical address 0xBA300000 from being used by the QNX OS on the
DRA74x. This technique is often used for the memory range used by
shmemallocator (resource table entry PHYS_MEM_IOBUFS) and/or by
SharedRegions. After modifying the startup flags, rebuild the QNX IFS
and use the new one to boot your board.

How do I configure the memory used by shmemallocator?
""""""""""""""""""""""""""""""""""""""""""""""""""""""

shmemallocator stands for "Shared Memory Allocator". It is a utility
that is built alongside the core IPC driver whenever the IPC product is
built. The user can optionally use this utility to allocate contiguous
shared memory for exchanging data between the host and the slave cores.
The memory it allocates from is defined in
<IPC_INSTALL_DIR>\qnx\src\ipc3x_dev\sharedmemallocator\resmgr\SharedMemoryAllocator.c
thru some #define statements:

::

    #define SH_MEM_BLOCK1_START 0xBA300000
    #define SH_MEM_BLOCK1_SIZE  0x5A00000

Typically, even though the code base (as of IPC 3.35) supports up to two
blocks, only block 1 is used when allocating memory using the function
SHM_alloc(), as shown in the IPC examples. When adjusting this block, It
is important that the memory matches a corresponding DEVMEM entry
(PHYS_MEM_IOBUFS) in the resource table so that this memory is mapped to
the slave core's MMU, and that the memory is reserved in the QNX IFS
startup command as per `"How do I change the Memory
Map?" <index_Foundational_Components.html#how-do-i-change-the-memory-map>`__.

Runtime Troubleshooting
^^^^^^^^^^^^^^^^^^^^^^^^^

Linux spurious "msg received with no recepient"
""""""""""""""""""""""""""""""""""""""""""""""""

When a Linux-loaded slave communicates to the Linux host, it sends a msg
using an rpmsg "channel". Sometimes there's no one listening on that
channel, for example if there are no host-side IPC applications running.
When a host-side application calls Ipc_start(), these channels start to
be monitored, but until then, no one's listening.

When, for example, a slave does a NameServer lookup, this query is often
sent to all cores in the system. If there's no host-side application
running, there's no one listening for these msgs, and when the
underlying rpmsg driver detects an arriving msg that no one's listening
for, it issues a dev_warn() call to report this, drops the message, and
moves along.

These warnings are often benign, and sometimes just reflect chatter
between the various slaves. Perhaps the dev_warn() should be changed to
a dev_dbg().

And yes, that's a typo - 'recepient' is really spelled 'recipient'.
Submit a patch and get your initials into the Linux kernel.  :)

Disabling auto-recovery
""""""""""""""""""""""""

When the HLOS detects a fault on a slave (e.g. an MMU fault), it reloads
and restarts the slave. Sometimes, especially when debugging slave-side
errors, it's useful to disable this feature so the state of the crashed
slave isn't reset and can be examined.

Linux
''''''

You can disable recovery of a given remote processor using remoteproc's
debugfs features. First, find the slave you want to disable (e.g.
``cat /debug/remoteproc/remoteproc0/name``) and then echo "disabled" to
the "recovery" file.

For example, if "remoteproc0" is the core you want to disable:

::

    target# echo "disabled" > /debug/remoteproc/remoteproc0/recovery

QNX
''''

Starting in IPC 3.22, you can simply throw the '-d' option when
launching the ipc resource manager to disable the recovery mechanism.

If you are using IPC 3.21 or older, there are a couple of tricks to
prevent the slaves from being automatically reloaded and restarted:

-  If you have the QNX Momentics IDE installed, you can set a breakpoint
   on the entry of ipc_recover() in
   <IPC_INSTALL_DIR>/qnx/src/ipc3x_dev/ti/syslink/build/Qnx/resmgr/syslink_main.c.
   This function is the callback that is invoked when an MMU fault
   occurs to perform the reload. Halting the host at that point would
   prevent it from reloading the DSP, and gives you time to inspect the
   DSP memory. This is nice because it does not necessitate a rebuild of
   IPC.

-  If you do not have access to the QNX debugger, you can rebuild IPC
   after commenting out the lines in ipc_recover(), and use the modified
   IPC resource manager binary for debugging. That would prevent it from
   reloading the DSP.

When should Ipc_start() be called?
------------------------------------

On a slave core, Ipc_start() should be called only if there is a need to
initialize the SharedRegion module and/or to perform slave-to-slave IPC
communication. In other words, if communication strictly happens between
host and slave(s), and SharedRegions are not defined, then there is no
need to call Ipc_start() on the slave. In fact, if SR0 (SharedRegion 0)
is not defined on a slave core, do not call Ipc_start() on that slave
core. The call would fail when it tries to look for SR0.

For an example that shows a call to Ipc_start() on the slave cores,
refer to the ex41_forwardmsg example, which showcases both host-to-slave
and slave-to-slave communication paths. Specifically, this line in
Dsp1.cfg and Ipu1.cfg adds a call to Ipc_start() within BIOS_start():

::

    BIOS.addUserStartupFunction('&IpcMgr_callIpcStart');

On the host core, Ipc_start() always needs to be called to initialize
IPC. Given host-side IPC code does not use SharedRegion, the function is
strictly used to perform initialization for other IPC modules.

Linux Ipc_start() Failures
----------------------------

LAD reports NameServer_setup: connect failed: 22, Invalid argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Internally, LAD tries to connect to sockets created by the rpmsg_proto
kernel driver. This connection can fail for several reasons, so this is
a common "general" error code. Some examples that generate this error
condition are below.

-  Failure to load the slave image. If the a slave executable fails to
   load, the sockets to communicate with it are not created. Make sure
   the slaves you need to communicate with are already loaded.
-  Failure to provide the correct KERNEL_INSTALL_DIR when building the
   user-side IPC libraries. Some customers reported this error when
   using Linux 3.9+ kernels (where the AF_MAX value in socket.h has
   increased). This created a mismatch in what AF_RPMSG was set to in
   user libs and the kernel, and the connect call failed. The solution
   was to require users set KERNEL_INSTALL_DIR when building the
   user-space libraries so IPC can interrogate the kernel version and
   set AF_RPMSG appropriately.
-  Failure to configure the slave image correctly. Internally, the
   slave-side MessageQ transport (TransportRpmsg) broadcasts its
   availability to the Linux host. If this broadcast doesn't occur
   (e.g., b/c the slave wasn't configured with TransportRpmsg), the
   socket connection will fail with error 22.
-  General slave-to-host interrupt failure. Some devices (e.g. DRA7XX)
   have interrupt crossbars that must be configured correctly as part of
   system boot (e.g. uboot). If these crossbars aren't initialized
   correctly, the slave-side broadcast that TransportRpmsg is available
   won't be received, the underlying socket connection won't be
   available, and the first sign of failure will be LAD trying to
   connect to the socket.

LAD reports LAD_connect() failed: 4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is a LAD_IOFAILURE = 4. The HOST OS-side application was unable to
communicate with LAD due to an OS_level I/O failure.

This is typically caused by LAD directory permissions.

-  In Linux **/tmp/LAD**
-  In Android **/data/lad/LAD**

The application was attempting to create or read from LAD's response
FIFO but was unable to by the application.

LAD must be started as root(su). IPC user applications communicating
with LAD, can be executed in **user** mode but need to ensure LAD is
stared with the correct permission.

-  **%** lad_dra7xx -l log.txt -p 777

You can also run both LAD and user application as root(su), thus not
requiring permission to be properly set when starting LAD.

LAD reports \_GateMP_TI_dGate not found
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the -g option is thrown, the LAD log may show an error about not
finding the symbol \_GateMP_TI_dGate:

::

    [22.583839] NameServer_getRemote: value for GateMP:_GateMP_TI_dGate not found.
    [22.583852] GateMP_attach: failed to open default gate on procId 4
    [22.583862]     status = -5
    [22.583871] DONE

This is because LAD is looking for the default GateMP instance, and did
not find it. On the DRA7xx, verify

#. SharedRegion 0 is defined on DSP1. GateMP implementation on the host
   requires use of SharedRegion
#. DSP1 is the owner of SharedRegion 0
#. Ipc_start() is called on DSP1. This ensures the default GateMP
   instance is created.

|

HLOS loading failures
-----------------------

BIOS-side VirtQueue assertions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The slave loads ok, but communication fails, and in the slave trace
output you find the following assert (line number and timestamp may
vary):

::

    [      0.000] [t=0x00d090ce] ti.ipc.family.vayu.VirtQueue: ERROR: "VirtQueue.c", line 296:
    [      0.000] ti.ipc.family.vayu.VirtQueue: "VirtQueue.c", line 296:
    [      0.000] xdc.runtime.Error.raise: terminating execution

This error often indicates a mismatch in VRING addresses between the
HLOS side and the slave. Often this is because a `custom resource
table <index_Foundational_Components.html#resource-custom-table>`__ was provided and the
VRING addresses specified don't match the HLOS-side addresses.

QNX IPC driver takes a long time to load the slave executable(s) when '-g' is thrown
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The '-g' option to the IPC driver is used to enable optional support for
GateMP on the host processor. During the setup of GateMP module, it
polls the slave processors for the default gate instance, which is
created by the owner of SharedRegion 0. If none of the cores loaded has
created the default gate, the driver will continue polling and
eventually timeout after 2 seconds, which means the loading procedure
may be delayed by 2 seconds as a consequence. To better suit a given
application, one can adjust the polling interval and the timeout
duration in the file
<IPC_INSTALL_DIR>/qnx/src/ipc3x_dev/ti/syslink/ipc/hlos/knl/GateMP_daemon.c
(this code excerpt may look slightly different depending on the version
of IPC you are looking at, but the idea is the same):

.. code-block:: c

    // Timeout duration is SETUP_TIMEOUT * polling interval
    #define SETUP_TIMEOUT         2

    Int GateMP_setup(Int32 * sr0ProcId)
    {
    ...
       UInt              timeout = SETUP_TIMEOUT;
    ...
       if (status == GateMP_S_SUCCESS) {
           /* The default gate creator is the owner of SR0 */
           while (((status = GateMP_openDefaultGate(&GateMP_module->defaultGate,
               &procId)) == GateMP_E_NOTFOUND) && (timeout > 0)) {
               sleep(1);  // polling interval
               timeout--;
           }
    ...
    }

In the case where the owner of SharedRegion 0 is not being loaded by the
IPC driver, reducing the timeout duration (SETUP_TIMEOUT) may be useful
to reduce the delay that results when the driver cannot find the default
gate.

In the case where the owner of SharedRegion 0 is indeed loaded by the
IPC driver, using usleep() instead of sleep() to reduce the polling
interval can be beneficial in cases where the initial poll happens
before the slave core (owner of SR0) has even got to the point in its
initialization to create the default gate. A faster polling rate would
ensure that a second or a third poll is performed more quickly thereby
giving a chance for the driver to move on. On the other hand, reducing
the polling interval too much may cause the driver to swamp the slave
cores with gate lookup requests, counterproductively slowing down the
loading process. As a rule of thumb, it is recommended to keep the
polling interval above 1 ms in modern platforms at the time of writing.

|

Disabling runtime auto-suspend
--------------------------------

When the HLOS detects that there has been no communication with the
slave for a defined amount of time and the slave is idled and in standby
state, then it can initiate suspend of the slave. Sometimes, the slave
may be performing some tasks that don't require communication with the
HLOS and does not wish to enter suspend. Or, it may be useful to
temporarily disable auto-suspend while debugging some errors.

Linux
^^^^^^^

The runtime suspend feature can be enabled or disabled by writing 'auto'
or 'on' to the device's 'control' power field. The default is enabled.
First, find the slave you want to disable (e.g.
``cat /debug/remoteproc/remoteproc0/name``) and then echo "on" to the
device's "control" power field.

For example, if "remoteproc0" is the core you want to disable:

::

    target# echo "on" > /sys/bus/platform/devices/58820000.ipu/power/control

SYS/BIOS
^^^^^^^^^

Alternatively, the slave can choose to deny the runtime suspend request,
preventing suspend. To prevent the slave from suspending, add the
`IpcPower_hibernateLock() <http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/ipc/latest/docs/doxygen/html/_ipc_power_8h.html#aef7ede8453ad5a6a52623188c412f2fc>`__
call to the slave software. When you wish to allow suspend again, call
`IpcPower_hibernateUnlock() <http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/ipc/latest/docs/doxygen/html/_ipc_power_8h.html#a2aa7348faba4bccb24da503fed3274f9>`__.
As long as the lock is held, the slave will deny all suspend requests
from the HLOS.

::

    IpcPower_hibernateLock();
    ...
    // Perform tasks
    ...
    IpcPower_hibernateUnlock();

In this case, it is not necessary to also disable auto-suspend from the
HLOS.

QNX
^^^^

Runtime auto-suspend is not supported in QNX.

|


