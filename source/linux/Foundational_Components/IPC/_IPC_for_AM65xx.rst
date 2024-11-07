.. rubric:: Introduction
   :name: introduction-linux-ipc-on-am65xx

The AM65xx device has an MCU subsystem in addition to the Cortex-A53 cores. The MCU subsystem consists of 2 Cortex-R5F cores which can work as seperate cores or in lock-step mode.

This article is geared toward AM65xx users that are running Linux on the
Cortex A53 core. The goal is to help users understand how to establish communication with the R5F cores.

There are many facets to this task: building, loading, debugging,
memory sharing, etc. This article intends to take incremental steps
toward understanding all of those pieces.

.. rubric:: Software Dependencies to Get Started
   :name: ipc-am65xx-software-dependencies-to-get-started

Prerequisites

-  `Processor SDK Linux for
   AM65xx <http://software-dl.ti.com/processor-sdk-linux/esd/AM65X/latest/index_FDS.html>`__
   (Version 5.1 or newer needed)
-  `Processor SDK RTOS for
   AM65xx <http://software-dl.ti.com/processor-sdk-rtos/esd/AM65X/latest/index_FDS.html>`__
-  `Code Composer
   Studio <http://processors.wiki.ti.com/index.php/Download_CCS>`__
   (choose version as specified on Proc SDK download page)

.. note::
   Please be sure that you have the same version number
   for both Processor SDK RTOS and Linux.

For reference within the context of this page, the Linux SDK is
installed at the following location:

::

    /mnt/data/user/ti-processor-sdk-linux-am65xx-evm-xx.xx.xx.xx
    ├── bin
    ├── board-support
    ├── docs
    ├── example-applications
    ├── filesystem
    ├── ipc-build.txt
    ├── linux-devkit
    ├── Makefile
    ├── Rules.make
    └── setup.sh

The RTOS SDK is installed at:

::

    /mnt/data/user/my_custom_install_sdk_rtos_am65xx_xx.xx
    ├── bios_6_xx_xx_xx
    ├── cg_xml
    ├── ctoolslib_x_x_x_x
    ├── framework_components_x_xx_xx_xx
    ├── gcc-linaro-<version>-x86_64_aarch64-elf
    ├── ipc_3_xx_xx_xx
    ├── ndk_3_xx_xx_xx
    ├── ns_2_xx_xx_xx
    ├── pdk_am65xx_x_x_x
    ├── processor_sdk_rtos_am65xx_x_xx_xx_xx
    ├── uia_2_xx_xx_xx
    ├── xdais_7_xx_xx_xx
    ├── xdctools_3_xx_xx_xx

|

.. rubric:: Typical Boot Flow on AM65xx for ARM Linux users
   :name: typical-boot-flow-on-am65xx-for-arm-linux-users

AM65xx SOC's have multiple processor cores - Cortex A53, ARM R5F cores. The A53 typically runs a HLOS like Linux/Android and the remote cores (R5Fs) run TI-RTOS. In the normal operation,
boot loader(U-Boot/SPL) boots and loads the A53 with the HLOS. The A53
boots the R5 cores.

.. Image:: /images/Normal-boot-a53.png

In this sequence, the interval between the Power on Reset and the
remote cores (i.e. the R5Fs) executing is dependent on the
HLOS initialization time.

|

.. rubric:: Getting Started with IPC Linux Examples
   :name: ipc-am65xx-getting-started-with-ipc-linux-examples

The figure below illustrates how remoteproc/rpmsg driver from ARM Linux
kernel communicates with IPC driver on slave processor (e.g. R5F) running RTOS.

.. Image:: /images/LinuxIPC_with_RTOS_Slave.png

In order to setup IPC on slave cores, we provide some pre-built examples
in IPC package that can be run from ARM Linux. The subsequent sections
describe how to build and run this examples and use that as a starting
point for this effort.

.. rubric:: Building the Bundled IPC Examples
   :name: ipc-am65xx-building-the-bundled-ipc-examples

The instructions to build IPC examples found under
ipc\_3\_xx\_xx\_xx/examples/AM65XX\_linux\_elf have been provided in the
`Processor SDK IPC Quick Start Guide <Foundational_Components_IPC.html#build-ipc-linux-examples>`__.

Let's focus on one example in particular, ex02\_messageq, which is
located at
**<rtos-sdk-install-dir>/ipc\_3\_xx\_xx\_xx/examples/AM65XX\_linux\_elf/ex02\_messageq**.
Here are the key files that you should see after a successful build:

::

    ├── r5f-0
    │   └── bin
    │       ├── debug
    │       │   └── server_r5f-0.xer5f
    │       └── release
    │       │   └── server_r5f-0.xer5f
    ├── r5f-1
    │   └── bin
    │       ├── debug
    │       │   └── server_r5f-1.xer5f
    │       └── release
    │       │   └── server_r5f-1.xer5f
    ├── host
    │       ├── debug
    │       │   └── app_host
    │       └── release
    │           └── app_host


|

.. rubric:: Running the Bundled IPC Examples
   :name: ipc-am65xx-running-the-bundled-ipc-examples

On the target, let's create a directory called ipc-starter:

::

    root@am65xx-evm:~# mkdir -p /home/root/ipc-starter
    root@am65xx-evm:~# cd /home/root/ipc-starter/

You will need to copy the ex02\_messageq directory of your host PC to
that directory on the target (through SD card, NFS export, SCP, etc.).
You can copy the entire directory, though we're primarily interested in
these files:

-  r5f-0/bin/debug/server_r5f-0.xer5f
-  r5f-1/bin/debug/server_r5f-1.xer5f
-  host/bin/debug/app\_host

The remoteproc driver is hard-coded to look for specific files when
loading the R5F cores. Here are the files it looks for:

-  /lib/firmware/am65x-mcu-r5f0_0-fw

These are generally a soft link to the intended executable. So for
example, let's update the r5f0 executable on the target:

::

    root@am65xx-evm:~# cd /lib/firmware/
    root@am65xx-evm:/lib/firmware# ln -sf /home/root/ipc-starter/ex02_messageq/r5f-0/bin/debug/server_r5f-0.xer5f am65x-mcu-r5f0_0-fw

To reload R5F0 with this new executable, we perform the following steps:

First identify the remotproc node associated with R5F0. This can be done by::

    root@am65xx-evm:/lib/firmware# grep -Isr r5f /sys/kernel/debug/remoteproc/

This will display for example::

    /sys/kernel/debug/remoteproc/remoteproc8/resource_table:  Name trace:r5f0
    /sys/kernel/debug/remoteproc/remoteproc8/name:41000000.r5f

then remoteproc8 is the node for the r5f core. ( Note the remoteprocx can change to for example remoteproc4)::

    root@am65xx-evm:~# echo stop > /sys/class/remoteproc/remoteproc4/state
    [ 6663.636529] remoteproc remoteproc4: stopped remote processor 41000000.r5f

    root@am65xx-evm:~# echo start > /sys/class/remoteproc/remoteproc4/state [ 6767.681165] remoteproc remoteproc4: powering up 41000000.r5f
    [ 6767.803683] remoteproc remoteproc4: Booting fw image am65x-mcu-r5f0_0-fw, size 3590160
    [ 6767.812558] platform 41000000.r5f: booting R5F core using boot addr = 0x0
    [ 6767.821345] virtio_rpmsg_bus virtio0: rpmsg host is online
    [ 6767.827147] remoteproc remoteproc4: registered virtio0 (type 7)
    [ 6767.834776] remoteproc remoteproc4: remote processor 41000000.r5f is now up
    root@am65xx-evm:~# [ 6767.848838] virtio_rpmsg_bus virtio0: creating channel rpmsg-proto addr 0x3d


More info related to loading firmware to the various cores can be found
`here <Foundational_Components_Multimedia_IVAHD.html#firmware-loading-and-unloading>`__.

Finally, we can run the example on R5 core::

    root@am65xx-evm:~# ./app_host R5F-0
    --> main:
    --> Main_main:
    --> App_create:
    App_create: Host is ready
    <-- App_create:
    --> App_exec:
    App_exec: sending message 1
    App_exec: sending message 2
    App_exec: sending message 3
    App_exec: message received, sending message 4
    App_exec: message received, sending message 5
    App_exec: message received, sending message 6
    App_exec: message received, sending message 7
    App_exec: message received, sending message 8
    App_exec: message received, sending message 9
    App_exec: message received, sending message 10
    App_exec: message received, sending message 11
    App_exec: message received, sending message 12
    App_exec: message received, sending message 13
    App_exec: message received, sending message 14
    App_exec: message received, sending message 15
    App_exec: message received
    App_exec: message received
    App_exec: message received
    <-- App_exec: 0
    --> App_delete:
    <-- App_delete:
    <-- Main_main:
    <-- main:
    root@am65xx-evm:~#

.. rubric:: Understanding the Memory Map
   :name: ipc-am65xx-understanding-the-memory-map

.. rubric:: Overall Linux Memory Map
   :name: ipc-am65xx-overall-linux-memory-map

::

    root@am65xx-evm:~# cat /proc/iomem
    [snip...]
	80000000-9affffff : System RAM
	80080000-80b2ffff : Kernel code
	80bb0000-80d9ffff : Kernel data
	9c800000-9e7fffff : System RAM
	a0000000-ffffffff : System RAM
	400000000-4ffffffff : /soc0/fss@47000000/ospi@47040000
	880000000-8ffffffff : System RAM


|

.. rubric:: DMA memory Carveouts
   :name: dma-memory-carveouts

::

	root@am65xx-evm:~# dmesg | grep  "Reserved memory"
	[    0.000000] Reserved memory: created DMA memory pool at 0x000000009b000000, size 16 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x000000009c000000, size 8 MiB

From the output above, we can derive the location and size of each DMA
carveout:

+------------------+--------------------+---------+
| Memory Section   | Physical Address   | Size    |
+==================+====================+=========+
| R5F-0 Pool       | 0x9c000000         | 8 MB    |
+------------------+--------------------+---------+
| R5F-1 Pool       | 0x9b000000         | 16 MB   |
+------------------+--------------------+---------+

For details on how to adjust the sizes and locations of the R5F Pool
carveouts, please see the corresponding section for changing the R5F memory map.


.. rubric:: Changing the R5F Memory Map
   :name: changing-the-r5f-memory-map

.. rubric:: Slave Physical Addresses
   :name: slave-physical-addresses

The physical location where the R5F code/data will actually reside is
defined by the DMA carveout. To change this location, you must change
the definition of the carveout. **The R5F carveouts are defined in the
Linux dts file.** For example for the AM65xx EVM:

|
| linux/arch/arm64/boot/dts/ti/k3-am654-base-board.dts

::

		reserved-memory {
				#address-cells = <2>;
				#size-cells = <2>;
				ranges;

				r5f1_memory_region: r5f1-memory@9b000000 {
					compatible = "shared-dma-pool";
					reg = <0 0x9b000000 0 0x1000000>;
					no-map;
				};

				r5f0_memory_region: r5f0-memory@9c000000 {
					compatible = "shared-dma-pool";
					reg = <0 0x9c000000 0 0x800000>;
					no-map;
				};

				secure_ddr: secure_ddr@9e800000 {
					reg = <0 0x9e800000 0 0x01800000>; /* for OP-TEE */
					alignment = <0x1000>;
					no-map;
				};
			};

You are able to change both the size and location. **Be careful not to
overlap any other carveouts!**

Additionally, when you change the carveout location, there is a
corresponding change that must be made to the resource table. For
starters, if you're making a memory change you will need a **custom**
resource table. The resource table is a large structure that is the
"bridge" between physical memory and virtual memory.
There is detailed information available in the article `IPC
Resource customTable <http://software-dl.ti.com/processor-sdk-rtos/esd/
docs/latest/rtos/index_Foundational_Components.html#resource-custom-table>`__.

Once you've created your custom resource table, you must update the
address of PHYS\_MEM\_IPC\_VRING to be the same base address as your
corresponding CMA.

.. code-block:: c

	#define R5F_MEM_TEXT            0x9C200000
	#define R5F_MEM_DATA            0x9C300000

	#define R5F_MEM_IPC_DATA        0x9C100000
	#define R5F_MEM_IPC_VRING       0x9C000000
	#define R5F_MEM_RPMSG_VRING0    0x9C000000
	#define R5F_MEM_RPMSG_VRING1    0x9C010000
	#define R5F_MEM_VRING_BUFS0     0x9C040000
	#define R5F_MEM_VRING_BUFS1     0x9C080000


.. note::
   The PHYS\_MEM\_IPC\_VRING definition from the resource
   table must match the address of the associated CMA carveout!

.. rubric:: R5 Virtual Addresses
   :name: R5-virtual-addresses

These addresses are the ones seen by the MCU subsystem, i.e. these will
be the addresses in your linker command files, etc.

You must ensure that the sizes of your sections are consistent with the
corresponding definitions in the resource table. You should create your
own resource table in order to modify the memory map. This is describe
in the page `IPC Resource
customTable <http://software-dl.ti.com/processor-sdk-rtos/esd/
docs/latest/rtos/index_Foundational_Components.html#resource-custom-table>`__.
You can look at an existing resource table inside IPC:

ipc/packages/ti/ipc/remoteproc/rsc\_table\_am65xx\_r5f.h

.. code:: c

   {
        TYPE_CARVEOUT,
        R5F_MEM_IPC_DATA, 0,
        R5F_MEM_IPC_DATA_SIZE, 0, 0, "R5F_MEM_IPC_DATA",
    },

    {
        TYPE_CARVEOUT,
        R5F_MEM_TEXT, 0,
        R5F_MEM_TEXT_SIZE, 0, 0, "R5F_MEM_TEXT",
    },

    {
        TYPE_CARVEOUT,
        R5F_MEM_DATA, 0,
        R5F_MEM_DATA_SIZE, 0, 0, "R5F_MEM_DATA",
    },

    {
        TYPE_TRACE, TRACEBUFADDR, TRACEBUFSIZE, 0, "trace:r5f0",
    },


Let's have a look at some of these to understand them better. For
example:

.. code-block:: c

        {
            TYPE_CARVEOUT,
            DSP_MEM_TEXT, 0,
            DSP_MEM_TEXT_SIZE, 0, 0, "DSP_MEM_TEXT",
        },

Key points to note are:

#. The "TYPE\_CARVEOUT" indicates that the physical memory backing this
   entry will come from the associated reserved pool.
#. DSP\_MEM\_TEXT is a #define earlier in the code providing the address
   for the code section. It is 0x9C200000 by default. **This must
   correspond to a section from your DSP linker command file, i.e.
   EXT\_CODE (or whatever name you choose to give it) must be linked to
   the same address.**
#. DSP\_MEM\_TEXT\_SIZE is the size of the text section.
   **The actual amount of
   linked code in the corresponding section of your executable must be
   less than or equal to this size.**

Let's take another:

.. code-block:: c

        {
            TYPE_TRACE, TRACEBUFADDR, TRACEBUFSIZE, 0, "trace:r5f0",
        },

|

Key points are:

#. The "TYPE\_TRACE" indicates this is for trace info.
#. The TRACEBUFADDR is defined earlier in the file as
   &ti\_trace\_SysMin\_Module\_State\_0\_outbuf\_\_A. That corresponds
   to the symbol used in TI-RTOS for the trace buffer.
#. The TRACEBUFSIZE is the size of the Trace section The corresponding size
   in the cfg file should be the same (or less). It looks like this:
   ``SysMin.bufSize  = 0x8000;``
