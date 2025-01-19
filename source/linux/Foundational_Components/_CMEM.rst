.. http://processors.wiki.ti.com/index.php/CMEM_Overview

*******************
CMEM
*******************

.. rubric:: Introduction
   :name: introduction-linux-cmem

CMEM is an API (`Reference
Guide <http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/linuxutils/latest/docs/html/cmem_8h.html>`__)
and library for managing one or more blocks of physically contiguous
memory. It also provides address translation services (e.g. virtual to
physical translation) and user-mode cache management APIs. This
physically contiguous memory is useful as data buffers that will be
shared with another processor (e.g. for the DSP on an
`OMAP3 <http://processors.wiki.ti.com/index.php/OMAP3_Overview>`__) or a hardware accelerator/DMA
(e.g. used by codecs on a `DM365 <http://processors.wiki.ti.com/index.php/DM365>`__)

Using its pool-based configuration, CMEM enables users to avoid memory
fragmentation, and ensures large physically contiguous memory blocks are
available even after a system has been running for very long periods of
time.

It was originally developed for the
`DM644x <http://processors.wiki.ti.com/index.php/Category:DM644x>`__, and has been ported to several
Operating Systems (e.g. Linux, WinCE, QNX, Nucleus, Green Hills
Integrity, and others). Although generally associated with `Codec
Engine <http://processors.wiki.ti.com/index.php/Category:Codec_Engine>`__, it has no dependency on
Codec Engine and can be used on its own.

It's currently distributed as a component in the `Linux
Utils <http://processors.wiki.ti.com/index.php/Linux_Utils_Roadmap>`__ and `WinCE
Utils <http://processors.wiki.ti.com/index.php/Category:WinCE_Utils>`__ products, which may be
included in various Linux and WinCE based SDKs.

.. rubric:: Development
   :name: development

CMEM is a component of `Linux Utils <http://processors.wiki.ti.com/index.php/Linux_Utils_Roadmap>`__,
and is actively being developed in the publicly maintained, TI-hosted
'ludev' git repository - http://git.ti.com/ipc/ludev. The `Linux Utils
development process is documented
here <http://git.ti.com/ipc/pages/Home>`__, patches are welcome!

.. rubric:: Configuration
   :name: configuration

.. rubric:: Linux Configuration
   :name: linux-configuration

CMEM configuration can be done in 2 ways either through device tree soruce file (DTS) or command line when installing cmemk.ko driver using insmod command.

.. rubric:: DTS Configuration
   :name: DTS Configuration

The CMEM configuration can be defined in the DTS file. Take AM57xx CMEM configuration as an example which is defined in arch/arm/boot/dts/am57xx-evm-cmem.dtsi.

::

	/ {
		reserved-memory {
			#address-cells = <2>;
			#size-cells = <2>;
			ranges;

			cmem_block_mem_0: cmem_block_mem@a0000000 {
				reg = <0x0 0xa0000000 0x0 0x0c000000>;
				no-map;
				status = "okay";
			};

			cmem_block_mem_1_ocmc3: cmem_block_mem@40500000 {
				reg = <0x0 0x40500000 0x0 0x100000>;
				no-map;
				status = "okay";
			};
		};

		cmem {
			compatible = "ti,cmem";
			#address-cells = <1>;
			#size-cells = <0>;

			#pool-size-cells = <2>;

			status = "okay";

			cmem_block_0: cmem_block@0 {
				reg = <0>;
				memory-region = <&cmem_block_mem_0>;
				cmem-buf-pools = <1 0x0 0x0c000000>;
			};

			cmem_block_1: cmem_block@1 {
				reg = <1>;
				memory-region = <&cmem_block_mem_1_ocmc3>;
			};
		};
	};


There are 2 memory blocks reserved, one in DDR starting at 0xa0000000 of size 0x0c000000. The other reserved memory block is in MSMC at 0x40500000 of size 0x100000. There are 2 CMEM blocks configuration. The first CMEM block is from DDR area and has 1 buffer  in the pool of size 0x0c000000. The 2nd CMEM block is from OCMC area.

The CMEM buffer pool allocation can be viewed at run time

::

	root@am57xx-evm:~# cat /proc/cmem

	Block 0: Pool 0: 1 bufs size 0xc000000 (0xc000000 requested)

	Pool 0 busy bufs:

	Pool 0 free bufs:
	id 0: phys addr 0xa0000000


.. rubric:: Command Line Configuration
   :name: Command Line Configuration

CMEM Linux configuration through command line is done when installing the cmemk.ko driver,
typically done using the insmod command. The cmemk.ko driver accepts
command line parameters for configuring the physical memory to reserve
and how to carve it up.

The following is an example of installing the cmem kernel module:

::

    /sbin/insmod cmemk.ko pools=4x30000,2x500000 phys_start=0x0 phys_end=0x3000000

-  phys\_start and phys\_end must be specified in hexadecimal format
-  pools must be specified using decimal format (for both number and
   size), since using hexadecimal format would visually clutter the
   specification due to the use of "x" as a token separator

This particular command creates 2 pools. The first pool is created with
4 buffers of size 30000 bytes and the second pool is created with 2
buffers of size 500000 bytes. The CMEM pool buffers start at 0x0 and end
at 0x3000000 (max).

Pool buffers are aligned on a module-dependent boundary, and their sizes
are rounded up to this same boundary. This applies to each buffer within
a pool. The total space used by an individual pool will therefore be
greater than (or equal to) the exact amount requested in the
installation of the module.

The poolid used in the driver calls would be 0 for the first pool and 1
for the second pool.

Pool allocations can be requested explicitly by pool number, or more
generally by just a size. For size-based allocations, the pool which
best fits the requested size is automatically chosen.

For more details on CMEM configuration, please find info in [Linux ProcSDK]/board_support/extra-drivers/cmem-mod-(version+commit_ID)/include/ti/cmem.h which documents CMEM user interface, or refer to the device tree binding document in board-support/extra-drivers/cmem-mod-[version]+[git-commit-id]/src/cmem/module/kernel/Documentation/device-tree/bindings/cmem/ti,cmem.txt

.. rubric:: WinCE Configuration
   :name: wince-configuration

Configuration of CMEM in WinCE-based environments is typically done via
the registry and/or statically built into the driver (for closed
systems). Here is an example for a line to be added to the MEMORY
section of 'config.bib' of your BSP:

::

       CMEM_DSP     89000000    02800000    RESERVED ; 40 MB

That reserves 40MB of memory for CMEM, DSPLINK, DSP code as well as DSP
heap usage starting at virtual address 0x89000000. There is no
distinction here between the different modules memory usage. Obviously
all of them need to be configured accordingly. Registry settings for
CMEM use physical start and end addresses for any defined block of
pools.

Here is an example CMEM configuration registry entry in platform.reg for
TI EVM3530:

::

    ;-- CMEM --------------------------------------------------------------------
    IF SYSGEN_CMEM
    [HKEY_LOCAL_MACHINE\Drivers\BuiltIn\CMEMK]
        "Prefix"="CMK"
        "Dll"="cmemk.dll"
        "Index"=dword:1
        ; Make 7 pools available for allocation for block 0
        ; Make 1 pool available for allocation for block 1
        "NumPools0"=dword:7
        "NumPools1"=dword:0

        "Block0_NumBuffers_Pool0"=dword:20
        "Block0_PoolSize_Pool0"=dword:1000 ; size in bytes (hex)
        "Block0_NumBuffers_Pool1"=dword:8
        "Block0_PoolSize_Pool1"=dword:20000 ; size in bytes (hex)
        "Block0_NumBuffers_Pool2"=dword:5
        "Block0_PoolSize_Pool2"=dword:100000 ; size in bytes (hex)

        "Block0_NumBuffers_Pool3"=dword:1
        "Block0_PoolSize_Pool3"=dword:15cfc0 ; size in bytes (hex)
        "Block0_NumBuffers_Pool4"=dword:1
        "Block0_PoolSize_Pool4"=dword:3e800 ; size in bytes (hex)
        "Block0_NumBuffers_Pool5"=dword:1
        "Block0_PoolSize_Pool5"=dword:36ee80 ; size in bytes (hex)

        "Block0_NumBuffers_Pool6"=dword:3
        "Block0_PoolSize_Pool6"=dword:96000 ; size in bytes (hex)

        ;; "Block1_NumBuffers_Pool1"=dword:2
        ;; "Block1_PoolSize_Pool1"=dword:4000 ; size in bytes (hex)


        ; Physical start + physical end can be use to ask CMEM to map a specific
        ; range of physical addresses.
        ; This is a potential security risk.  If physical start == 0 then the code
        ; hits a special case.
        ; physical end - physical start == length of allocation.  In the special
        ; case, memory is allocated via a call to AllocPhysMem() (as shown in
        ; this example).  MmMapIoSpace() is used to map the normal case where
        ; physical start != 0.
        ;
        ; physical start and end for block 0
        "PhysicalStart0"=dword:85000000
        "PhysicalEnd0"=dword:86000000
        ; physical start and end for block 1
        "PhysicalStart1"=dword:0
        "PhysicalEnd1"=dword:0
    ENDIF SYSGEN_CMEM
    ;------------------------------------------------------------------------------

The CMEM driver information must also be added to the platform.bib file
(or some other .bib file that gets put into ce.bib). Here is an example
of the CMEM driver entry in platform.bib:

::

    ;-- CMEM ----------------------------------------------------------------------
    IF SYSGEN_CMEM
    cmemk.dll  $(_FLATRELEASEDIR)\cmemk.dll               NK SHK
    ENDIF BSP_CMEM
    ;------------------------------------------------------------------------------

.. rubric:: Debugging Techniques
   :name: debugging-techniques

Linux users can execute "``cat /proc/cmem``" to get status on the
buffers and pools managed by CMEM.

There is also a debug library provided that provides tracing diagnostics
during execution. XDC Config users can link in this library by adding
the following to their application's config script:

.. code-block:: javascript

    var CMEM = xdc.useModule('ti.sdo.linuxutils.cmem.CMEM');
    CMEM.debug = true;

.. rubric:: General Purpose Heaps
   :name: general-purpose-heaps

In CMEM 2.00, CMEM added support for a general purpose heap. Using the
example above, in addition to the 2 pools, a general purpose heap block
is created from which allocations of any size can be requested.
Internally, allocation sizes are rounded up to a module-dependent
boundary and allocation addresses are aligned either to this same
boundary or to the requested alignment (whichever is greater).

The size of the heap block is the amount of CMEM memory remaining after
all pool allocations. If more heap space is needed than is available
after pool allocations, you must reduce the amount of CMEM memory
granted to the pools.

The main disadvantage to using heap(s) over pools is fragmentation.
After several sequences of codec creation/deletion, in different orders,
with possibly different create() params, you may end up fragmenting your
heap and being unable to acquire a requested memory block - possibly
resulting in a codec creation failure.

Typically, during development, users will use CMEM with heap-based
memory, as heap usage requires very little configuration, and users
don't know how to configure pool memory(!). In a production system,
however, it's strongly recommended that pool configuration be used to
avoid memory fragmentation and confusing end user errors.

.. rubric:: Application Cleanup
   :name: application-cleanup

CMEM 2.23 introduced a facility to clean up unfreed buffers when an
application exits, either prematurely or in a normal fashion. This
facility is achieved by maintaining an "ownership" list for each
allocated buffer that is inspected upon closing a device driver
instance. During this inspection all allocated buffers are checked, and
when it is determined that the closing process is on the ownership list
of an allocated buffer, the process is removed from the list. If this
causes the list to become empty the associated buffer is actually freed,
otherwise it is maintained in the allocated state on behalf of other
owners. A side-effect of this model is that only a buffer "owner" is
allowed to free the buffer.

In order to facilitate multiple owners of an allocated buffer, a new set
of APIs was introduced:

.. code-block:: c

    void *CMEM_registerAlloc(unsigned long physp);
    int CMEM_unregister(void *ptr, CMEM_AllocParams *params);

``CMEM_registerAlloc()`` takes a buffer physical address as input
(achieved through ``CMEM_getPhys()``) and returns a fresh virtual
address that is mapped to that buffer, while also adding the calling
process to the ownership list. ``CMEM_unregister()`` is equivalent to
``CMEM_free()`` and releases ownership of the buffer (as well as freeing
it if all owners have released the buffer).

In CMEM 2.24, ownership is established on a per-process (and per-thread)
basis. This detail becomes important when using CMEM in multiple threads
of a given process - if one thread allocates a CMEM buffer and a
separate thread of the same process is responsible for freeing that
buffer, the "freeing" thread will not be allowed to free the buffer
since it is not on the ownership list.

CMEM 2.24.01 changes the ownership policy to be based on the calling
process' file descriptor instead of the calling process' process
descriptor. This facilitates thread-based sharing of buffers, allowing
any thread within a process to free a buffer that was allocated by a
different thread within the same process, since threads within a process
all use the same file descriptor.

.. rubric:: Linux CMA Support
   :name: linux-cma-support

CMEM 4.00 added the ability to leverage the `Linux kernel's CMA
feature <http://lwn.net/Articles/396657/>`__. CMA supports a "global"
memory pool, as well as device-specific memory - CMEM provides the
facilities to allocate from either type of CMA pool.

CMA also defines the carveout area of the physical location where the DSP code/data will actually reside. The DSP carveouts are defined in the dts file. For example the AM57xx EVM, it is linux/arch/arm/boot/dts/am57xx-beagle-x15-common.dtsi.

::

	dsp1_cma_pool: dsp1_cma@99000000 {
		compatible = "shared-dma-pool";
		reg = <0x0 0x99000000 0x0 0x4000000>;
		reusable;
		status = "okay";
	};

	dsp2_cma_pool: dsp2_cma@9f000000 {
		compatible = "shared-dma-pool";
		reg = <0x0 0x9f000000 0x0 0x800000>;
		reusable;
		status = "okay";
	};


Note that using CMEM to allocate from CMA-based memory is an additional
feature. You can continue to use CMEM to manage memory carveouts as
well.

.. rubric:: Android CMA Support
   :name: android-cma-support

.. rubric:: Build Environment Setup
   :name: build-environment-setup

First download an unzip the latest Linux utils(4.00.01.08) zip file. The
file products.mak (at the top level of this tree) contains two
definitions used by the build subsystem:

::

           KERNEL_INSTALL_DIR - The base directory of your Linux kernel source tree
           TOOLCHAIN_PREFIX - the 'prefix' for the GNU ARM codegen tools

The TOOLCHAIN\_PREFIX can contain the full path of the codegen tools,
ending with the tool prefix, i.e.:

::

           TOOLCHAIN_PREFIX=/db/toolsrc/library/vendors2005/cs/arm/arm-2008q1-126/bin/arm-none-linux-gnueabi-

or it can be just the tool prefix if your shell's $PATH contains your
codegen's 'bin' directory:

::

           TOOLCHAIN_PREFIX=arm-none-linux-gnueabi-

where your $PATH contains:

::

           /db/toolsrc/library/vendors2005/cs/arm/arm-2008q1-126/bin

For example, below is the setup environment which is validated

::

           TOOLCHAIN_LONGNAME = arm-eabi
           TOOLCHAIN_INSTALL_DIR = /home/(user)/mydroid/prebuilts/gcc/linux-x86/arm/arm-eabi-4.7
           KERNEL_INSTALL_DIR =/home/(user)/kernel/android-3.8

Now move to the src/cmem/module directory to run "make clean" and then
"make".

.. rubric:: Building Test Binaries
   :name: building-test-binaries

From the downloaded and installed linux utils base directory run the
below commands,

Note: Any non-android toolchain should work and don't forget to export
the toolchain path(until the bin folder) to PATH environment variable.

::

           export ARCH=arm
           export CROSS_COMPILE=arm-linux-gnueabihf
           ./configure --disable-shared  --host=arm-linux-gnueabihf --prefix=$PWD CFLAGS='--static'

Now run "make clean" and "make" to build the test binaries for android

.. rubric:: Test Setup and Validation Process
   :name: test-setup-and-validation-process

For testing purpose we built the android kernel for mem=1200M.

Boot the system with android and then do **adb push** on the below
mentioned files,

::

           (linux utils base directory)/src/cmem/module/cmemk.ko to /system/lib/modules
           (linux utils base directory)/src/cmem/tests/apitest to /system/bin
           (linux utils base directory)/src/cmem/tests/multi_process to /system/bin
           (linux utils base directory)/src/cmem/tests/translate to /system/bin

The loadable kernel module '**cmemk.ko'** can be installed into any
running system. Out of the 3 tests mentioned below Multi\_Process &
Translate tests have been used to validate the CMEM module's usage of
OCMC1 ram. OCMC1 ram range is 0x40300000 ~ 0x4033FFFF.

.. rubric:: Multi Process Test
   :name: multi-process-test

This app tries to use CMEM from multiple processes. It takes the number
of processes to start as a parameter. Now load the kernel module
'cmemk.ko' with the below command:

::

           % insmod cmemk.ko phys_start=0xcaf01000 phys_end=0xCB601000 pools=4x1000 phys_start_1=0xCB601000 phys_end_1=0xCB701000 pools_1=4x1000

(Uses DDR)

::

           % insmod cmemk.ko phys_start=0x40300000 phys_end=0x4033FFFF pools=4x500 phys_start_1=0x4033FFFF phys_end_1=0x4037ffff pools_1=4x500 allowOverlap=1

(Uses OCMC1, for this rebuild the Translate Test app with macro
BUFFER\_SIZE = 500 at line #49 in file
(linuxutils)/src/cmem/tests/multi\_process.c) Now run the Multi Process
test,

::

           % multi_process 3

where 3 is the number of processes to be spawned.

.. rubric:: Translate Test
   :name: translate-test

This app tests the address translation. Now load the kernel module
'cmemk.ko' with the below command:

::

           % insmod cmemk.ko phys_start=0xcaf01000 phys_end=0xCB601000 pools=1x3145728

(Uses DDR)

::

           % insmod cmemk.ko phys_start=0x40300000 phys_end=0x4037ffff pools=1x20000 allowOverlap=1

(Uses OCMC1, for this rebuild the Translate Test app with macro BUFSIZE
= 20000 at line #48 in file (linuxutils)/src/cmem/tests/translate.c) Now
run the Translate test,

::

           % translate

.. rubric:: API Test
   :name: api-test

Tests basic API usage and memory allocation. This particular test has a
limitation as it runs successfully only on kernel built with mem=120M.
Now load the kernel module 'cmemk.ko' with the below command:

::

           % insmod cmemk.ko phys_start=0x87800000 phys_end=0x87F00000 pools=4xBUFSIZE phys_start_1=0x87F00000 phys_end_1=0x88000000 pools_1=4xBUFSIZE

where BUFSIZE is the number of bytes you plan on passing as command line
parameter to apitest. If in doubt, use a larger number as BUFSIZE
denotes the maximum buffer you can allocate.Now run the Translate test,
Now run the API test,

::

           % apitest <BUFSIZE>

(e.g) With BUFSIZE=10240

::

           % apitest 10240

.. rubric:: CMEM FAQ
   :name: cmem-faq

**Q:** Why am I'm getting this error when loading the CMEM (or other!)
driver: "insmod: error inserting 'cmemk.ko': -1 Invalid module format"?

**A:** This error indicates the CMEM kernel module was built with a
different Linux kernel version than the version running on the target.
You need to rebuild CMEM against the kernel running on your target.
**Q:** Can ``CMEM_getPhys()`` be used to translate **any** virtual
address to its physical address?

**A:** In theory, "yes". However, sometime after Linux version 2.6.10
the CMEM kernel module ``get_phys()`` function stopped working for
kernel addresses. A new ``get_phys()`` was provided to work with newer
kernels, but it was discovered that this new one didn't correctly
translate non-direct-mapped kernel addresses, so code was added to CMEM
to save the lower/upper bounds of the CMEM blocks' kernel addresses, and
manually look for those in ``get_phys()`` before trying more general
methods of translation.
So, in short, CMEM's ``get_phys()`` doesn't handle non-direct-mapped
kernel addresses except the ones that correspond to CMEM's managed
memory block(s).
**Q:** How does CMEM relate to `DSPLink's
POOL <http://processors.wiki.ti.com/index.php/DSPLink_POOL_Module_Overview>`__ feature?

**A:** Though they provide overlapping features, they are independent,
and each has unique features.

-  CMEM

   -  CMEM can be used on systems without a remote DSP slave (e.g. DM365
      codecs require physically contiguous memory when using HW
      accelerators)
   -  CMEM buffers can be cached
   -  CMEM blocks support fixed size pools (no fragmentation) as well as
      heaps (easier to use)
   -  CMEM configuration doesn't require a rebuild (they're provided as
      insmod params)

-  POOL

   -  POOL buffers can be allocated on one processor and freed on
      another

**Q:** In Linux, how do I set aside the memory carveout that CMEM uses?

**A:** The memory carveout used by CMEM must not be in use by Linux else
an error will occur during module loading (i.e., insmod/modprobe). There
are two simple methods for defining CMEM's memory carveout:

-  1) kernel command line

This method involves the kernel command line issued from u-boot. When
booting Linux, one may restrict the memory available to Linux by
specifying physical memory blocks for Linux to use:
"mem=#[KMG]@0xXXXXXXXX"
e.g.:
mem=128M@0x80000000 mem=256M@0x90000000
which grants the memory at 0x80000000 -> 0x88000000 and 0x90000000 ->
0xa0000000 to Linux, leaving the CMEM memory carveout as 128MB at
0x88000000 (0x88000000 -> 0x90000000). Without a "mem=" entry on the
command line, Linux will use all available memory.

-  2) removal via machine's "``.reserve``" function

This method involves modifying a machine's ``.reserve`` function to
remove a block of memory from Linux. For example, for the Vayu
architecture, the file arch/arm/mach-omap2/common.c contains a function
named ``dra7_reserve()`` which is assigned to the machine ``.reserve``
function in arch/arm/mach-omap2/board-generic.c. Adding the following C
statement to ``dra7_reserve()`` accomplishes the same memory carveout as
specified in 1) above:
``memory_remove(0x88000000, 0x08000000);``
The CMEM memory carveout can either precede, overlap, or succeed the
Linux memory. For the case where it precedes or overlaps, don't forget
to specify "allowOverlap=1" on the cmemk.ko insmod/modprobe command,
else the module loading will fail.
For both cases above, you would load cmemk.ko as follows:
% modprobe cmemk.ko phys\_start=0x88000000 phys\_end=0x90000000
allowOverlap=1 pools=...
The advantage for method 1) is that the CMEM memory carveout can be
specified to be anywhere by the system integrator without changing the
kernel, with a disadvantage of having to document this carveout
specification along with potential error in doing so. The advantage of
method 2) is that a given kernel image will always properly create the
carveout for CMEM without any intervention by the system integrator,
with a disadvantage of not being moveable without changing/rebuilding
the kernel.
**Q:** Why CMEM failed in physical address > 32bits?

**A:** The user space application need to be compiled with
“–D\_FILE\_OFFSET\_BITS=64" to allow physical addresses > 32 bits.
|

.. rubric:: Licensing
   :name: licensing

In CMEM 2.00, the CMEM Linux release is LGPL v2 for the user mode lib
and GPL v2 for the kernel mode driver.

In CMEM 2.21, the Linux user mode library licensing changed from LGPL to
BSD. The Linux kernel mode driver continued to be GPL v2.

