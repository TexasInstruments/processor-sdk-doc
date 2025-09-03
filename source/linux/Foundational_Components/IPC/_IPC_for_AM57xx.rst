.. http://processors.wiki.ti.com/index.php/Linux_IPC_on_AM57xx
.. rubric:: Introduction
   :name: introduction-linux-ipc-on-am57xx

This article is geared toward AM57xx users that are running Linux on the
Cortex A15. The goal is to help users understand how to gain entitlement
to the DSP (c66x) and IPU (Cortex M4) subsystems of the AM57xx.

AM572x device has two IPU subsystems (IPUSS), each of which has 2 cores.
IPU2 is used as a controller in multi-media applications, so if you have
Processor SDK Linux running, chances are that IPU2 already has firmware
loaded. However, IPU1 is open for general purpose programming to offload
the ARM tasks.

There are many facets to this task: building, loading, debugging, MMUs,
memory sharing, etc. This article intends to take incremental steps
toward understanding all of those pieces.

.. rubric:: Software Dependencies to Get Started
   :name: ipc-am57xx-software-dependencies-to-get-started

Prerequisites

-  `Processor SDK Linux for
   AM57xx <http://software-dl.ti.com/processor-sdk-linux/esd/AM57X/latest/index_FDS.html>`__
   (Version 3.01 or newer needed)
-  `Processor SDK RTOS for
   AM57xx <http://software-dl.ti.com/processor-sdk-rtos/esd/AM57X/latest/index_FDS.html>`__
-  `Code Composer
   Studio <http://processors.wiki.ti.com/index.php/Download_CCS>`__
   (choose version as specified on Proc SDK download page)

.. note::
   Please be sure that you have the same version number
   for both Processor SDK RTOS and Linux.

For reference within the context of this page, the Linux SDK is
installed at the following location:

::

    /mnt/data/user/ti-processor-sdk-linux-am57xx-evm-xx.xx.xx.xx
    ├── bin
    ├── board-support
    ├── docs
    ├── example-applications
    ├── filesystem
    ├── linux-devkit
    ├── Makefile
    ├── Rules.make
    └── setup.sh

The RTOS SDK is installed at:

::

    /mnt/data/user/my_custom_install_sdk_rtos_am57xx_xx.xx
    ├── bios_6_xx_xx_xx
    ├── cg_xml
    ├── ctoolslib_x_x_x_x
    ├── dsplib_c66x_x_x_x_x
    ├── edma3_lld_2_xx_xx_xx
    ├── framework_components_x_xx_xx_xx
    ├── imglib_c66x_x_x_x_x
    ├── ipc_3_xx_xx_xx
    ├── mathlib_c66x_3_x_x_x
    ├── ndk_2_xx_xx_xx
    ├── opencl_rtos_am57xx_01_01_xx_xx
    ├── openmp_dsp_am57xx_2_04_xx_xx
    ├── pdk_am57xx_x_x_x
    ├── processor_sdk_rtos_am57xx_x_xx_xx_xx
    ├── uia_2_xx_xx_xx
    ├── xdais_7_xx_xx_xx

CCS is installed at:

::

    /mnt/data/user/ti/my_custom_ccs_x.x.x_install
    ├── ccsvX
    │   ├── ccs_base
    │   ├── doc
    │   ├── eclipse
    │   ├── install_info
    │   ├── install_logs
    │   ├── install_scripts
    │   ├── tools
    │   ├── uninstall_ccs
    │   ├── uninstall_ccs.dat
    │   ├── uninstallers
    │   └── utils
    ├── Code Composer Studio x.x.x.desktop
    └── xdctools_x_xx_xx_xx_core
        ├── bin
        ├── config.jar
        ├── docs
        ├── eclipse
        ├── etc
        ├── gmake
        ├── include
        ├── package
        ├── packages
        ├── package.xdc
        ├── tconfini.tcf
        ├── xdc
        ├── xdctools_3_xx_xx_xx_manifest.html
        ├── xdctools_3_xx_xx_xx_release_notes.html
        ├── xs
        └── xs.x86U

|

.. rubric:: Typical Boot Flow on AM572x for ARM Linux users
   :name: typical-boot-flow-on-am572x-for-arm-linux-users

AM57xx SOC's have multiple processor cores - Cortex A15, C66x DSP's and
ARM M4 cores. The A15 typically runs a HLOS like Linux/QNX/Android and
the remotecores(DSP's and M4's) run a RTOS. In the normal operation,
boot loader(U-Boot/SPL) boots and loads the A15 with the HLOS. The A15
boots the DSP and the M4 cores.

.. Image:: /images/Normal-boot.png

In this sequence, the interval between the Power on Reset and the
remotecores (i.e. the DSP's and the M4's) executing is dependent on the
HLOS initialization time.

|

.. rubric:: Getting Started with IPC Linux Examples
   :name: ipc-am57xx-getting-started-with-ipc-linux-examples

The figure below illustrates how remoteproc/rpmsg driver from ARM Linux
kernel communicates with IPC driver on slave processor (e.g. DSP, IPU,
etc) running RTOS.

.. Image:: /images/LinuxIPC_with_RTOS_Slave.png

In order to setup IPC on slave cores, we provide some pre-built examples
in IPC package that can be run from ARM Linux. The subsequent sections
describe how to build and run this examples and use that as a starting
point for this effort.

.. rubric:: Building the Bundled IPC Examples
   :name: ipc-am57xx-building-the-bundled-ipc-examples

The instructions to build IPC examples found under
ipc\_3\_xx\_xx\_xx/examples/DRA7XX\_linux\_elf have been provided in the
**`Processor\_SDK IPC Quick Start
Guide <Foundational_Components_IPC.html#ipc-quick-start-guide>`__.**

Let's focus on one example in particular, ex02\_messageq, which is
located at
**<rtos-sdk-install-dir>/ipc\_3\_xx\_xx\_xx/examples/DRA7XX\_linux\_elf/ex02\_messageq**.
Here are the key files that you should see after a successful build:

::

    ├── dsp1
    │   └── bin
    │       ├── debug
    │       │   └── server_dsp1.xe66
    │       └── release
    │           └── server_dsp1.xe66
    ├── dsp2
    │   └── bin
    │       ├── debug
    │       │   └── server_dsp2.xe66
    │       └── release
    │           └── server_dsp2.xe66
    ├── host
    │       ├── debug
    │       │   └── app_host
    │       └── release
    │           └── app_host
    ├── ipu1
    │   └── bin
    │       ├── debug
    │       │   └── server_ipu1.xem4
    │       └── release
    │           └── server_ipu1.xem4
    └── ipu2
        └── bin
            ├── debug
            │   └── server_ipu2.xem4
            └── release
                └── server_ipu2.xem4

|

|

.. rubric:: Running the Bundled IPC Examples
   :name: ipc-am57xx-running-the-bundled-ipc-examples

On the target, let's create a directory called ipc-starter:

::

    root@am57xx-evm:~# mkdir -p /home/root/ipc-starter
    root@am57xx-evm:~# cd /home/root/ipc-starter/

You will need to copy the ex02\_messageq directory of your host PC to
that directory on the target (through SD card, NFS export, SCP, etc.).
You can copy the entire directory, though we're primarily interested in
these files:

-  dsp1/bin/debug/server\_dsp1.xe66
-  dsp2/bin/debug/server\_dsp2.xe66
-  host/bin/debug/app\_host
-  ipu1/bin/debug/server\_ipu1.xem4
-  ipu2/bin/debug/server\_ipu2.xem4

The remoteproc driver is hard-coded to look for specific files when
loading the DSP/M4. Here are the files it looks for:

-  /lib/firmware/dra7-dsp1-fw.xe66
-  /lib/firmware/dra7-dsp2-fw.xe66
-  /lib/firmware/dra7-ipu1-fw.xem4
-  /lib/firmware/dra7-ipu2-fw.xem4

These are generally a soft link to the intended executable. So for
example, let's update the DSP1 executable on the target:

::

    root@am57xx-evm:~# cd /lib/firmware/
    root@am57xx-evm:/lib/firmware# rm dra7-dsp1-fw.xe66
    root@am57xx-evm:/lib/firmware# ln -s /home/root/ipc-starter/ex02_messageq/dsp1/bin/debug/server_dsp1.xe66 dra7-dsp1-fw.xe66

To reload DSP1 with this new executable, we perform the following steps:

::

    root@am57xx-evm:/lib/firmware# cd /sys/bus/platform/drivers/omap-rproc/
    root@am57xx-evm:/sys/bus/platform/drivers/omap-rproc# echo 40800000.dsp > unbind
    [27639.985631] omap_hwmod: mmu0_dsp1: _wait_target_disable failed
    [27639.991534] omap-iommu 40d01000.mmu: 40d01000.mmu: version 3.0
    [27639.997610] omap-iommu 40d02000.mmu: 40d02000.mmu: version 3.0
    [27640.017557] omap_hwmod: mmu1_dsp1: _wait_target_disable failed
    [27640.030571] omap_hwmod: mmu0_dsp1: _wait_target_disable failed
    [27640.036605]  remoteproc2: stopped remote processor 40800000.dsp
    [27640.042805]  remoteproc2: releasing 40800000.dsp
    root@am57xx-evm:/sys/bus/platform/drivers/omap-rproc# echo 40800000.dsp > bind
    [27645.958613] omap-rproc 40800000.dsp: assigned reserved memory node dsp1_cma@99000000
    [27645.966452]  remoteproc2: 40800000.dsp is available
    [27645.971410]  remoteproc2: Note: remoteproc is still under development and considered experimental.
    [27645.980536]  remoteproc2: THE BINARY FORMAT IS NOT YET FINALIZED, and backward compatibility isn't yet guaranteed.
    root@am57xx-evm:/sys/bus/platform/drivers/omap-rproc# [27646.008171]  remoteproc2: powering up 40800000.dsp
    [27646.013038]  remoteproc2: Booting fw image dra7-dsp1-fw.xe66, size 4706800
    [27646.028920] omap_hwmod: mmu0_dsp1: _wait_target_disable failed
    [27646.034819] omap-iommu 40d01000.mmu: 40d01000.mmu: version 3.0
    [27646.040772] omap-iommu 40d02000.mmu: 40d02000.mmu: version 3.0
    [27646.058323]  remoteproc2: remote processor 40800000.dsp is now up
    [27646.064772] virtio_rpmsg_bus virtio2: rpmsg host is online
    [27646.072271]  remoteproc2: registered virtio2 (type 7)
    [27646.078026] virtio_rpmsg_bus virtio2: creating channel rpmsg-proto addr 0x3d

More info related to loading firmware to the various cores can be found
`here <Foundational_Components_Multimedia_IVAHD.html#firmware-loading-and-unloading>`__.

Finally, we can run the example on DSP1:

::

    root@am57xx-evm:/sys/bus/platform/drivers/omap-rproc# cd /home/root/ipc-starter/ex02_messageq/host/bin/debug
    root@am57xx-evm:~/ipc-starter/ex02_messageq/host/bin/debug# ./app_host DSP1
    --> main:
    [33590.700700] omap_hwmod: mmu0_dsp2: _wait_target_disable failed
    [33590.706609] omap-iommu 41501000.mmu: 41501000.mmu: version 3.0
    [33590.718798] omap-iommu 41502000.mmu: 41502000.mmu: version 3.0
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

| The similar procedure can be used for DSP2/IPU1/IPU2 also to update
  the soft link of the firmware, reload the firmware at run-time, and
  run the host binary from A15.

.. rubric:: Understanding the Memory Map
   :name: ipc-am57xx-understanding-the-memory-map

.. rubric:: Overall Linux Memory Map
   :name: overall-linux-memory-map

::

    root@am57xx-evm:~# cat /proc/iomem
    [snip...]
    58060000-58078fff : core
    58820000-5882ffff : l2ram
    58882000-588820ff : /ocp/mmu@58882000
    80000000-9fffffff : System RAM
      80008000-808d204b : Kernel code
      80926000-809c96bf : Kernel data
    a0000000-abffffff : CMEM
    ac000000-ffcfffff : System RAM

|

.. rubric:: CMA Carveouts
   :name: cma-carveouts

::

    root@am57xx-evm:~# dmesg | grep -i cma
    [    0.000000] Reserved memory: created CMA memory pool at 0x0000000095800000, size 56 MiB
    [    0.000000] Reserved memory: initialized node ipu2_cma@95800000, compatible id shared-dma-pool
    [    0.000000] Reserved memory: created CMA memory pool at 0x0000000099000000, size 64 MiB
    [    0.000000] Reserved memory: initialized node dsp1_cma@99000000, compatible id shared-dma-pool
    [    0.000000] Reserved memory: created CMA memory pool at 0x000000009d000000, size 32 MiB
    [    0.000000] Reserved memory: initialized node ipu1_cma@9d000000, compatible id shared-dma-pool
    [    0.000000] Reserved memory: created CMA memory pool at 0x000000009f000000, size 8 MiB
    [    0.000000] Reserved memory: initialized node dsp2_cma@9f000000, compatible id shared-dma-pool
    [    0.000000] cma: Reserved 24 MiB at 0x00000000fe400000
    [    0.000000] Memory: 1713468K/1897472K available (6535K kernel code, 358K rwdata, 2464K rodata, 332K init, 289K bss, 28356K reserved, 155648K  cma-reserved, 1283072K highmem)
    [    5.492945] omap-rproc 58820000.ipu: assigned reserved memory node ipu1_cma@9d000000
    [    5.603289] omap-rproc 55020000.ipu: assigned reserved memory node ipu2_cma@95800000
    [    5.713411] omap-rproc 40800000.dsp: assigned reserved memory node dsp1_cma@9b000000
    [    5.771990] omap-rproc 41000000.dsp: assigned reserved memory node dsp2_cma@9f000000

From the output above, we can derive the location and size of each CMA
carveout:

+------------------+--------------------+---------+
| Memory Section   | Physical Address   | Size    |
+==================+====================+=========+
| IPU2 CMA         | 0x95800000         | 56 MB   |
+------------------+--------------------+---------+
| DSP1 CMA         | 0x99000000         | 64 MB   |
+------------------+--------------------+---------+
| IPU1 CMA         | 0x9d000000         | 32 MB   |
+------------------+--------------------+---------+
| DSP2 CMA         | 0x9f000000         | 8 MB    |
+------------------+--------------------+---------+
| Default CMA      | 0xfe400000         | 24 MB   |
+------------------+--------------------+---------+

For details on how to adjust the sizes and locations of the DSP/IPU CMA
carveouts, please see the corresponding section for changing the DSP or
IPU memory map.

To adjust the size of the "Default CMA" section, this is done as part of
the Linux config:

linux/arch/arm/configs/tisdk\_am57xx-evm\_defconfig

.. code-block:: c

    #
    # Default contiguous memory area size:
    #
    CONFIG_CMA_SIZE_MBYTES=24
    CONFIG_CMA_SIZE_SEL_MBYTES=y

|

.. rubric:: CMEM
   :name: cmem

To view the allocation at run-time:

::

    root@am57xx-evm:~# cat /proc/cmem

    Block 0: Pool 0: 1 bufs size 0xc000000 (0xc000000 requested)

    Pool 0 busy bufs:

    Pool 0 free bufs:
    id 0: phys addr 0xa0000000

This shows that we have defined a CMEM block at physical base address of
0xA0000000 with total size 0xc000000 (192 MB). This block contains a
buffer pool consisting of 1 buffer. Each buffer in the pool (only one in
this case) is defined to have a size of 0xc000000 (192 MB).

Here is where those sizes/addresses were defined for the AM57xx EVM:

linux/arch/arm/boot/dts/am57xx-evm-cmem.dtsi

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

|

.. rubric:: Changing the DSP Memory Map
   :name: changing-the-dsp-memory-map

First, it is important to understand that there are a pair of Memory
Management Units (MMUs) that sit between the DSP subsystems and the L3
interconnect. One of these MMUs is for the DSP core and the other is for
its local EDMA. They both serve the same purpose of translating virtual
addresses (i.e. the addresses as viewed by the DSP subsystem) into
physical addresses (i.e. addresses as viewed from the L3 interconnect).

.. Image:: /images/LinuxIpcDspMmu.png

.. rubric:: DSP Physical Addresses
   :name: dsp-physical-addresses

The physical location where the DSP code/data will actually reside is
defined by the CMA carveout. To change this location, you must change
the definition of the carveout. **The DSP carveouts are defined in the
Linux dts file.** For example for the AM57xx EVM:

|
| linux/arch/arm/boot/dts/am57xx-beagle-x15-common.dtsi

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
           };

You are able to change both the size and location. **Be careful not to
overlap any other carveouts!**

.. note::
   The **two** location entries for a given DSP must be identical!

Additionally, when you change the carveout location, there is a
corresponding change that must be made to the resource table. For
starters, if you're making a memory change you will need a **custom**
resource table. The resource table is a large structure that is the
"bridge" between physical memory and virtual memory. This structure is
utilized for configuring the MMUs that sit in front of the DSP
subsystem. There is detailed information available in the article `IPC
Resource customTable <http://software-dl.ti.com/processor-sdk-rtos/esd/
docs/latest/rtos/index_Foundational_Components.html#resource-custom-table>`__.

Once you've created your custom resource table, you must update the
address of PHYS\_MEM\_IPC\_VRING to be the same base address as your
corresponding CMA.

.. code-block:: c

    #if defined (VAYU_DSP_1)
    #define PHYS_MEM_IPC_VRING      0x99000000
    #elif defined (VAYU_DSP_2)
    #define PHYS_MEM_IPC_VRING      0x9F000000
    #endif

.. note::
   The PHYS\_MEM\_IPC\_VRING definition from the resource
   table must match the address of the associated CMA carveout!

.. rubric:: DSP Virtual Addresses
   :name: dsp-virtual-addresses

These addresses are the ones seen by the DSP subsystem, i.e. these will
be the addresses in your linker command files, etc.

You must ensure that the sizes of your sections are consistent with the
corresponding definitions in the resource table. You should create your
own resource table in order to modify the memory map. This is describe
in the page `IPC Resource
customTable <http://software-dl.ti.com/processor-sdk-rtos/esd/
docs/latest/rtos/index_Foundational_Components.html#resource-custom-table>`__.
You can look at an
existing resource table inside IPC:

ipc/packages/ti/ipc/remoteproc/rsc\_table\_vayu\_dsp.h

.. code:: c

        {
            TYPE_CARVEOUT,
            DSP_MEM_TEXT, 0,
            DSP_MEM_TEXT_SIZE, 0, 0, "DSP_MEM_TEXT",
        },
        {
            TYPE_CARVEOUT,
            DSP_MEM_DATA, 0,
            DSP_MEM_DATA_SIZE, 0, 0, "DSP_MEM_DATA",
        },
        {
            TYPE_CARVEOUT,
            DSP_MEM_HEAP, 0,
            DSP_MEM_HEAP_SIZE, 0, 0, "DSP_MEM_HEAP",
        },
        {
            TYPE_CARVEOUT,
            DSP_MEM_IPC_DATA, 0,
            DSP_MEM_IPC_DATA_SIZE, 0, 0, "DSP_MEM_IPC_DATA",
        },
        {
            TYPE_TRACE, TRACEBUFADDR, 0x8000, 0, "trace:dsp",
        },
        {
            TYPE_DEVMEM,
            DSP_MEM_IPC_VRING, PHYS_MEM_IPC_VRING,
            DSP_MEM_IPC_VRING_SIZE, 0, 0, "DSP_MEM_IPC_VRING",
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
   entry will come from the associated CMA pool.
#. DSP\_MEM\_TEXT is a #define earlier in the code providing the address
   for the code section. It is 0x95000000 by default. **This must
   correspond to a section from your DSP linker command file, i.e.
   EXT\_CODE (or whatever name you choose to give it) must be linked to
   the same address.**
#. DSP\_MEM\_TEXT\_SIZE is the size of the MMU pagetable entry being
   created (1MB in this particular instance). **The actual amount of
   linked code in the corresponding section of your executable must be
   less than or equal to this size.**

Let's take another:

.. code-block:: c

        {
            TYPE_TRACE, TRACEBUFADDR, 0x8000, 0, "trace:dsp",
        },

|

Key points are:

#. The "TYPE\_TRACE" indicates this is for trace info.
#. The TRACEBUFADDR is defined earlier in the file as
   &ti\_trace\_SysMin\_Module\_State\_0\_outbuf\_\_A. That corresponds
   to the symbol used in TI-RTOS for the trace buffer.
#. The "0x8000" is the size of the MMU mapping. The corresponding size
   in the cfg file should be the same (or less). It looks like this:
   ``SysMin.bufSize  = 0x8000;``

Finally, let's look at a TYPE\_DEVMEM example:

.. code-block:: c

        {
            TYPE_DEVMEM,
            DSP_PERIPHERAL_L4CFG, L4_PERIPHERAL_L4CFG,
            SZ_16M, 0, 0, "DSP_PERIPHERAL_L4CFG",
        },

|

Key points:

#. The "TYPE\_DEVMEM" indicates that we are making an MMU mapping, but
   this **does not come from the CMA pool**. This is intended for mapping
   peripherals, etc. that already exist in the device memory map.
#. DSP\_PERIPHERAL\_L4CFG (0x4A000000) is the virtual address while
   L4\_PERIPHERAL\_L4CFG (0x4A000000) is the physical address. **This is
   an identity mapping, meaning that peripherals can be referenced by
   the DSP using their physical address.**

.. rubric:: DSP Access to Peripherals
   :name: dsp-access-to-peripherals

The default resource table creates the following mappings:

+-------------------+--------------------+---------+-----------------------+
| Virtual Address   | Physical Address   | Size    | Comment               |
+===================+====================+=========+=======================+
| 0x4A000000        | 0x4A000000         | 16 MB   | L4CFG + L4WKUP        |
+-------------------+--------------------+---------+-----------------------+
| 0x48000000        | 0x48000000         | 2 MB    | L4PER1                |
+-------------------+--------------------+---------+-----------------------+
| 0x48400000        | 0x48400000         | 4 MB    | L4PER2                |
+-------------------+--------------------+---------+-----------------------+
| 0x48800000        | 0x48800000         | 8 MB    | L4PER3                |
+-------------------+--------------------+---------+-----------------------+
| 0x54000000        | 0x54000000         | 16 MB   | L3\_INSTR + CT\_TBR   |
+-------------------+--------------------+---------+-----------------------+
| 0x4E000000        | 0x4E000000         | 1 MB    | DMM config            |
+-------------------+--------------------+---------+-----------------------+

In other words, the peripherals can be accessed at their physical
addresses since we use an identity mapping.

.. rubric:: Inspecting the DSP IOMMU Page Tables at Run-Time
   :name: inspecting-the-dsp-iommu-page-tables-at-run-time

You can dump the DSP IOMMU page tables with the following commands:

+--------+--------+------------------------------------------------------------+
| DSP    | MMU    | Command                                                    |
+========+========+============================================================+
| DSP1   | MMU0   | cat /sys/kernel/debug/omap\_iommu/40d01000.mmu/pagetable   |
+--------+--------+------------------------------------------------------------+
| DSP1   | MMU1   | cat /sys/kernel/debug/omap\_iommu/40d02000.mmu/pagetable   |
+--------+--------+------------------------------------------------------------+
| DSP2   | MMU0   | cat /sys/kernel/debug/omap\_iommu/41501000.mmu/pagetable   |
+--------+--------+------------------------------------------------------------+
| DSP2   | MMU1   | cat /sys/kernel/debug/omap\_iommu/41502000.mmu/pagetable   |
+--------+--------+------------------------------------------------------------+

In general, MMU0 and MMU1 are being programmed identically so you really
only need to take a look at one or the other to understand the mapping
for a given DSP.

For example:

::

    root@am57xx-evm:~# cat /sys/kernel/debug/omap_iommu/40d01000.mmu/pagetable
    L:      da:     pte:
    --------------------------
    1: 0x48000000 0x48000002
    1: 0x48100000 0x48100002
    1: 0x48400000 0x48400002
    1: 0x48500000 0x48500002
    1: 0x48600000 0x48600002
    1: 0x48700000 0x48700002
    1: 0x48800000 0x48800002
    1: 0x48900000 0x48900002
    1: 0x48a00000 0x48a00002
    1: 0x48b00000 0x48b00002
    1: 0x48c00000 0x48c00002
    1: 0x48d00000 0x48d00002
    1: 0x48e00000 0x48e00002
    1: 0x48f00000 0x48f00002
    1: 0x4a000000 0x4a040002
    1: 0x4a100000 0x4a040002
    1: 0x4a200000 0x4a040002
    1: 0x4a300000 0x4a040002
    1: 0x4a400000 0x4a040002
    1: 0x4a500000 0x4a040002
    1: 0x4a600000 0x4a040002
    1: 0x4a700000 0x4a040002
    1: 0x4a800000 0x4a040002
    1: 0x4a900000 0x4a040002
    1: 0x4aa00000 0x4a040002
    1: 0x4ab00000 0x4a040002
    1: 0x4ac00000 0x4a040002
    1: 0x4ad00000 0x4a040002
    1: 0x4ae00000 0x4a040002
    1: 0x4af00000 0x4a040002

The first column tells us whether the mapping is a Level 1 or Level 2
descriptor. All the lines above are a first level descriptor, so we look
at the associated format from the TRM:

.. Image:: /images/LinuxIpcPageTableDescriptor1.png

The "da" ("device address") column reflects the virtual address. It is
**derived** from the index into the table, i.e. there does not exist a
"da" register or field in the page table. Each MB of the address space
maps to an entry in the table. The "da" column is displayed to make it
easy to find the virtual address of interest.

The "pte" ("page table entry") column can be decoded according to Table
20-4 shown above. For example:

::

    1: 0x4a000000 0x4a040002

The 0x4a040002 shows us that it is a Supersection with base address
0x4A000000. This gives us a 16 MB memory page. Note the repeated entries
afterward. That's a requirement of the MMU. Here's an excerpt from the
TRM:

.. note::
   Supersection descriptors must be repeated 16 times,
   because each descriptor in the first level translation table describes 1
   MiB of memory. If an access points to a descriptor that is not
   initialized, the MMU will behave in an unpredictable way.

|

.. rubric:: Changing Cortex M4 IPU Memory Map
   :name: changing-cortex-m4-ipu-memory-map

In order to fully understand the memory mapping of the Cortex M4 IPU
Subsystems, it's helpful to recognize that there are two
distinct/independent levels of memory translation. Here's a snippet from
the TRM to illustrate:

.. Image:: /images/LinuxIpcIpuMmu.png

.. rubric:: Cortex M4 IPU Physical Addresses
   :name: cortex-m4-ipu-physical-addresses

The physical location where the M4 code/data will actually reside is
defined by the CMA carveout. To change this location, you must change
the definition of the carveout. **The M4 carveouts are defined in the
Linux dts file.** For example for the AM57xx EVM:

|
| linux/arch/arm/boot/dts/am57xx-beagle-x15-common.dtsi

::

                   ipu2_cma_pool: ipu2_cma@95800000 {
                           compatible = "shared-dma-pool";
                           reg = <0x0 95800000 0x0 0x3800000>;
                           reusable;
                           status = "okay";
                   };

                   ipu1_cma_pool: ipu1_cma@9d000000 {
                           compatible = "shared-dma-pool";
                           reg = <0x0 9d000000 0x0 0x2000000>;
                           reusable;
                           status = "okay";
                   };
           };

| You are able to change both the size and location. **Be careful not to
  overlap any other carveouts!**

.. note::
   The **two** location entries for a given carveout
   must be identical!

| Additionally, when you change the carveout location, there is a
  corresponding change that must be made to the resource table. For
  starters, if you're making a memory change you will need a **custom**
  resource table. The resource table is a large structure that is the
  "bridge" between physical memory and virtual memory. This structure is
  utilized for configuring the IPUx\_MMU (not the Unicache MMU). There
  is detailed information available in the article `IPC Resource
  customTable <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/
  latest/rtos/index_Foundational_Components.html#resource-custom-table>`__.

Once you've created your custom resource table, you must update the
address of PHYS\_MEM\_IPC\_VRING to be the same base address as your
corresponding CMA.

.. code-block:: c

    #if defined(VAYU_IPU_1)
    #define PHYS_MEM_IPC_VRING      0x9D000000
    #elif defined (VAYU_IPU_2)
    #define PHYS_MEM_IPC_VRING      0x95800000
    #endif


.. note::
   The PHYS\_MEM\_IPC\_VRING definition from the resource
   table must match the address of the associated CMA carveout!

.. rubric:: Cortex M4 IPU Virtual Addresses
   :name: cortex-m4-ipu-virtual-addresses

.. rubric:: Unicache MMU
   :name: unicache-mmu

The Unicache MMU sits closest to the Cortex M4. It provides the first
level of address translation. The Unicache MMU is actually "self
programmed" by the Cortex M4. The Unicache MMU is also referred to as
the Attribute MMU (AMMU). There are a fixed number of small, medium and
large pages. Here's a snippet showing some of the key mappings:

ipc\_3\_43\_02\_04/examples/DRA7XX\_linux\_elf/ex02\_messageq/ipu1/IpuAmmu.cfg

.. code-block:: javascript

    /*********************** Large Pages *************************/
    /* Instruction Code: Large page  (512M); cacheable */
    /* config large page[0] to map 512MB VA 0x0 to L3 0x0 */
    AMMU.largePages[0].pageEnabled = AMMU.Enable_YES;
    AMMU.largePages[0].logicalAddress = 0x0;
    AMMU.largePages[0].translationEnabled = AMMU.Enable_NO;
    AMMU.largePages[0].size = AMMU.Large_512M;
    AMMU.largePages[0].L1_cacheable = AMMU.CachePolicy_CACHEABLE;
    AMMU.largePages[0].L1_posted = AMMU.PostedPolicy_POSTED;

    /* Peripheral regions: Large Page (512M); non-cacheable */
    /* config large page[1] to map 512MB VA 0x60000000 to L3 0x60000000 */
    AMMU.largePages[1].pageEnabled = AMMU.Enable_YES;
    AMMU.largePages[1].logicalAddress = 0x60000000;
    AMMU.largePages[1].translationEnabled = AMMU.Enable_NO;
    AMMU.largePages[1].size = AMMU.Large_512M;
    AMMU.largePages[1].L1_cacheable = AMMU.CachePolicy_NON_CACHEABLE;
    AMMU.largePages[1].L1_posted = AMMU.PostedPolicy_POSTED;

    /* Private, Shared and IPC Data regions: Large page (512M); cacheable */
    /* config large page[2] to map 512MB VA 0x80000000 to L3 0x80000000 */
    AMMU.largePages[2].pageEnabled = AMMU.Enable_YES;
    AMMU.largePages[2].logicalAddress = 0x80000000;
    AMMU.largePages[2].translationEnabled = AMMU.Enable_NO;
    AMMU.largePages[2].size = AMMU.Large_512M;
    AMMU.largePages[2].L1_cacheable = AMMU.CachePolicy_CACHEABLE;
    AMMU.largePages[2].L1_posted = AMMU.PostedPolicy_POSTED;

|

+----------------+-------------------------+-------------------------+----------+---------------+
| Page           | Cortex M4 Address       | Intermediate Address    | Size     | Comment       |
+================+=========================+=========================+==========+===============+
| Large Page 0   | 0x00000000-0x1fffffff   | 0x00000000-0x1fffffff   | 512 MB   | Code          |
+----------------+-------------------------+-------------------------+----------+---------------+
| Large Page 1   | 0x60000000-0x7fffffff   | 0x60000000-0x7fffffff   | 512 MB   | Peripherals   |
+----------------+-------------------------+-------------------------+----------+---------------+
| Large Page 2   | 0x80000000-0x9fffffff   | 0x80000000-0x9fffffff   | 512 MB   | Data          |
+----------------+-------------------------+-------------------------+----------+---------------+

These 3 pages are "identity" mappings, performing a passthrough of
requests to the associated address ranges. These intermediate addresses
get mapped to their physical addresses in the next level of translation
(IOMMU).

The AMMU ranges for code and data **need** to be identity mappings because
otherwise the remoteproc loader wouldn't be able to match up the
sections from the ELF file with the associated IOMMU mapping. These
mappings should suffice for any application, i.e. no need to adjust
these. The more likely area for modification is the resource table in
the next section. The AMMU mappings are needed mainly to understand the
full picture with respect to the Cortex M4 memory map.

|

.. rubric:: IOMMU
   :name: iommu

The IOMMU sits closest to the L3 interconnect. It takes the intermediate
address output from the AMMU and translates it to the physical address
used by the L3 interconnect. The IOMMU is programmed by the ARM based on
the associated resource table. If you're planning any memory changes
then you'll want to make a custom resource table as described in the
page `IPC Resource
customTable <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/
latest/rtos/index_Foundational_Components.html#resource-custom-table>`__.

The default resource table (which can be adapted to make a custom table)
can be found at this location:

ipc/packages/ti/ipc/remoteproc/rsc\_table\_vayu\_ipu.h

.. code-block:: c

    #define IPU_MEM_TEXT            0x0
    #define IPU_MEM_DATA            0x80000000

    #define IPU_MEM_IOBUFS          0x90000000

    #define IPU_MEM_IPC_DATA        0x9F000000
    #define IPU_MEM_IPC_VRING       0x60000000
    #define IPU_MEM_RPMSG_VRING0    0x60000000
    #define IPU_MEM_RPMSG_VRING1    0x60004000
    #define IPU_MEM_VRING_BUFS0     0x60040000
    #define IPU_MEM_VRING_BUFS1     0x60080000

    #define IPU_MEM_IPC_VRING_SIZE  SZ_1M
    #define IPU_MEM_IPC_DATA_SIZE   SZ_1M

    #if defined(VAYU_IPU_1)
    #define IPU_MEM_TEXT_SIZE       (SZ_1M)
    #elif defined(VAYU_IPU_2)
    #define IPU_MEM_TEXT_SIZE       (SZ_1M * 6)
    #endif

    #if defined(VAYU_IPU_1)
    #define IPU_MEM_DATA_SIZE       (SZ_1M * 5)
    #elif defined(VAYU_IPU_2)
    #define IPU_MEM_DATA_SIZE       (SZ_1M * 48)
    #endif

|

<snip...>

|

.. code-block:: c

        {
            TYPE_CARVEOUT,
            IPU_MEM_TEXT, 0,
            IPU_MEM_TEXT_SIZE, 0, 0, "IPU_MEM_TEXT",
        },
        {
            TYPE_CARVEOUT,
            IPU_MEM_DATA, 0,
            IPU_MEM_DATA_SIZE, 0, 0, "IPU_MEM_DATA",
        },
        {
            TYPE_CARVEOUT,
            IPU_MEM_IPC_DATA, 0,
            IPU_MEM_IPC_DATA_SIZE, 0, 0, "IPU_MEM_IPC_DATA",
        },


The 3 entries above from the resource table all come from the associated
IPU CMA pool (i.e. as dictated by the TYPE\_CARVEOUT). The second
parameter represents the virtual address (i.e. input address to the
IOMMU). **These addresses must be consistent with both the AMMU mapping
as well as the linker command file.** The ex02\_messageq example from
ipc defines these memory sections in the file
examples/DRA7XX\_linux\_elf/ex02\_messageq/shared/config.bld.

You can dump the IPU IOMMU page tables with the following commands:

+--------+------------------------------------------------------------+
| IPU    | Command                                                    |
+========+============================================================+
| IPU1   | cat /sys/kernel/debug/omap\_iommu/58882000.mmu/pagetable   |
+--------+------------------------------------------------------------+
| IPU2   | cat /sys/kernel/debug/omap\_iommu/55082000.mmu/pagetable   |
+--------+------------------------------------------------------------+

Please see the `corresponding DSP
documentation <Foundational_Components_IPC.html#inspecting-the-dsp-iommu-page-tables-at-run-time>`__
for more details on interpreting the output.

|

.. rubric:: Cortex M4 IPU Access to Peripherals
   :name: cortex-m4-ipu-access-to-peripherals

The default resource table creates the following mappings:

+-------------------------------------+-------------------------------------+------------------------------+---------+-----------------------+
| Virtual Address used by Cortex M4   | Address at output of Unicache MMU   | Address at output of IOMMU   | Size    | Comment               |
+=====================================+=====================================+==============================+=========+=======================+
| 0x6A000000                          | 0x6A000000                          | 0x4A000000                   | 16 MB   | L4CFG + L4WKUP        |
+-------------------------------------+-------------------------------------+------------------------------+---------+-----------------------+
| 0x68000000                          | 0x68000000                          | 0x48000000                   | 2 MB    | L4PER1                |
+-------------------------------------+-------------------------------------+------------------------------+---------+-----------------------+
| 0x68400000                          | 0x68400000                          | 0x48400000                   | 4 MB    | L4PER2                |
+-------------------------------------+-------------------------------------+------------------------------+---------+-----------------------+
| 0x68800000                          | 0x68800000                          | 0x48800000                   | 8 MB    | L4PER3                |
+-------------------------------------+-------------------------------------+------------------------------+---------+-----------------------+
| 0x74000000                          | 0x74000000                          | 0x54000000                   | 16 MB   | L3\_INSTR + CT\_TBR   |
+-------------------------------------+-------------------------------------+------------------------------+---------+-----------------------+

Example: Accessing UART5 from IPU

#. For this example, it's assumed the pin-muxing was already setup in
   the bootloader. If that's not the case, you would need to do that
   here.
#. The UART5 module needs to be enabled via the
   CM\_L4PER\_UART5\_CLKCTRL register. This is located at physical
   address 0x4A009870. So from the M4 we would program this register at
   virtual address 0x6A009870. Writing a value of 2 to this register
   will enable the peripheral.
#. After completing the previous step, the UART5 registers will become
   accessible. Normally UART5 is accessible at physical base address
   0x48066000. This would correspondingly be accessed from the IPU at
   0x68066000.

.. rubric:: Power Management
   :name: power-management

The IPUs and DSPs auto-idle by default. This can prevent you from being
able to connect to the device using JTAG or from accessing local memory
via devmem2. There are some options sprinkled throughout sysfs that are
needed in order to force these subsystems on, as is sometimes needed for
development and debug purposes.

There are some hard-coded device names that originate in the device tree
(dra7.dtsi) that are needed for these operations:

+---------------+---------------------------+------------------+
| Remote Core   | Definition in dra7.dtsi   | System FS Name   |
+===============+===========================+==================+
| IPU1          | ipu@58820000              | 58820000.ipu     |
+---------------+---------------------------+------------------+
| IPU2          | ipu@55020000              | 55020000.ipu     |
+---------------+---------------------------+------------------+
| DSP1          | dsp@40800000              | 40800000.dsp     |
+---------------+---------------------------+------------------+
| DSP2          | dsp@41000000              | 41000000.dsp     |
+---------------+---------------------------+------------------+
| ICSS1-PRU0    | pru@4b234000              | 4b234000.pru0    |
+---------------+---------------------------+------------------+
| ICSS1-PRU1    | pru@4b238000              | 4b238000.pru1    |
+---------------+---------------------------+------------------+
| ICSS2-PRU0    | pru@4b2b4000              | 4b2b4000.pru0    |
+---------------+---------------------------+------------------+
| ICSS2-PRU1    | pru@4b2b8000              | 4b2b8000.pru1    |
+---------------+---------------------------+------------------+

To map these System FS names to the associated remoteproc entry, you can
run the following commands:

::

    root@am57xx-evm:~# ls -l /sys/kernel/debug/remoteproc/
    root@am57xx-evm:~# cat /sys/kernel/debug/remoteproc/remoteproc*/name

The results of the commands will be a one-to-one mapping. For example,
58820000.ipu corresponds with remoteproc0.

Similarly, to see the power state of each of the cores:

::

    root@am57xx-evm:~# cat /sys/class/remoteproc/remoteproc*/state

The state can be suspended, running, offline, etc. You can only attach
JTAG if the state is "running". If it shows as "suspended" then you must
force it to run. For example, let's say DSP0 is "suspended". You can run
the following command to force it on:

::

    root@am57xx-evm:~# echo on > /sys/bus/platform/devices/40800000.dsp/power/control

The same is true for any of the cores, but replace 40800000.dsp with the
associated System FS name from the chart above.

.. rubric:: Adding IPC to an Existing TI-RTOS Application on slave cores
   :name: adding-ipc-to-an-existing-ti-rtos-application-on-slave-cores

.. rubric:: Adding IPC to an existing TI RTOS application on the DSP
   :name: adding-ipc-to-an-existing-ti-rtos-application-on-the-dsp

A common thing people want to do is take an existing DSP application
and add IPC to it. This is common when migrating from a DSP only
solution to a heterogeneous SoC with an Arm plus a DSP. This is the
focus of this section.

In order to describe this process, we need an example test case to
work with. For this purpose, we'll be using the
GPIO\_LedBlink\_evmAM572x\_c66xExampleProject example that's part of
the PDK (installed as part of the Processor SDK RTOS). You can find it
at
c:\\ti\\pdk\_am57xx\_1\_0\_4\\packages\\MyExampleProjects\\GPIO\_LedBlink\_evmAM572x\_c66xExampleProject.
This example uses SYS/BIOS and blinks the USER0 LED on the AM572x GP
EVM, it's labeled D4 on the EVM silkscreen just to the right of the
blue reset button.

|

There were several steps taken to make this whole process work, each of
which will be described in following sections

#. Build and run the out-of-box LED blink example on the EVM using Code
   Composer Studio (CCS)
#. Take the ex02\_message example from the IPC software bundle and turn
   it into a CCS project. Build it and modify the Linux startup code to
   use this new image. This is just a sanity check step to make sure we
   can build the IPC examples in CCS and have them run at boot up on the
   EVM.
#. In CCS, make a clone of the out-of-box LED example and rename it to
   denote it's the IPC version of the example. Then using the
   ex02\_messageq example as a reference, add in the IPC pieces to the
   LED example. Build from CCS then add it to the Linux firmware folder.

|

.. rubric:: Add IPC to the LED Blink Example
   :name: add-ipc-to-the-led-blink-example

The first step is to clone our out-of-box LED blink CCS project and
rename it to denote it's using IPC. The easiest way to do this is using
CCS. Here are the steps...

-  In the **Edit** perspective, go into your **Project Explorer** window and
   right click on your GPIO\_LedBlink\_evmAM572x+c66xExampleProject
   project and select **copy** from the pop-up menu. Maske sure the
   project is not is a closed state.
-  Rick click in and empty area of the project explorer window and
   select past.
-  A dialog box pops up, modify the name to denote it's using IPC. A
   good name is GPIO\_LedBlink\_evmAM572x+c66xExampleProjec\_with\_ipc.

|

This is the project we'll be working with from here on. The next thing
we want to do is select the proper RTSC platform and other components.
To do this, follow these steps.

-  Right click on the
   GPIO\_LedBlink\_evmAM572x+c66xExampleProjec\_with\_ipc project and
   select **Properties**
-  In the left hand pane, click on **CCS General**.
-  On the right hand side, click on the **RTSC** tab
-  For **XDCtools version:** select 3.32.0.06\_core
-  In the list of **Products and Repositories**, **check** the following...

   -  IPC 3.43.2.04
   -  SYS/BIOS 6.45.1.29
   -  am57xx PDK 1.0.4

-  For **Target**, select ti.targets.elf.C66
-  For **Platform**, select ti.platforms.evmDRA7XX
-  Once the platform is selected, edit its name buy hand and
   append :dsp1 to the end. After this it should be
   ti.platforms.evmDRA7XX:dsp1
-  Go ahead and leave the **Build-profile** set to debug.
-  Hit the OK button.

|

Now we want to copy configuration and source files from the
ex02\_messageq IPC example into our project. The IPC example is
located at
**C:\\ti\\ipc\_3\_43\_02\_04\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq**.
To copy files into your CCS project, you can simply select the files
you want in Windows explorer then drag and drop them into your project
in CCS.

Copy these files into your CCS project...

-  C:\\ti\\ipc\_3\_43\_02\_04\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\shared\\AppCommon.h
-  C:\\ti\\ipc\_3\_43\_02\_04\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\shared\\config.bld
-  C:\\ti\\ipc\_3\_43\_02\_04\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\shared\\ipc.cfg.xs

|

Now copy these files into your CCS project...

-  C:\\ti\\ipc\_3\_43\_02\_04\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\dsp1\\Dsp1.cfg
-  C:\\ti\\ipc\_3\_43\_02\_04\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\dsp1\\MainDsp1.c
-  C:\\ti\\ipc\_3\_43\_02\_04\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\dsp1\\Server.c
-  C:\\ti\\ipc\_3\_43\_02\_04\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\dsp1\\Server.h

|

.. note::
   When you copy Dsp1.cfg into your CCS project, it
   should show up greyed out. This is because the LED blink example
   already has a cfg file (gpio\_test\_evmAM572x.cfg). The Dsp1.cfg will
   be used for copying and pasting. When it's all done, you can delete it
   from your project.

Finally, you will likely want to use a custom resource table so copy
these files into your CCS project...

-  C:\\ti\\ipc\_3\_43\_02\_04\\packages\\ti\\ipc\\remoteproc\\rsc\_table\_vayu\_dsp.h
-  C:\\ti\\ipc\_3\_43\_02\_04\\packages\\ti\\ipc\\remoteproc\\rsc\_types.h

The rsc\_table\_vayu\_dsp.h file defines an initialized structure so
let's make a **.c** source file.

-  In your CCS project, rename rsc\_table\_vayu\_dsp.h to
   rsc\_table\_vayu\_dsp.c

|

Now we want to **merge** the IPC example configuration file with the LED
blink example configuration file. Follow these steps...

-  Open up **Dsp1.cfg** using a text editor (don't open it using the GUI).
   Right click on it and select **Open With -> XDCscript Editor**
-  We want to copy the entire contents into the clipboard. Select all
   and copy.
-  Now just like above, open the gpio\_test\_evmAM572x.cfg config file
   in the text editor. Go to the very bottom and **paste** in the contents
   from the Dsp1.cfg file. Basically we've appended the contents of
   Dsp1.cfg into gpio\_test\_evmAM572x.cfg.

|

We've now added in all the necessary configuration and source files
into our project. Don't expect it to build at this point, we have to
make edits first. These edits are listed below.

::

    NOTE, you can download the full CCS project with source files to use as a reference.
    See link towards the end of this section.

|

-  Edit **gpio\_test\_evmAM572x.cfg**

|

Add the following to the beginning of your configuration file

.. code-block:: javascript

    var Program = xdc.useModule('xdc.cfg.Program');

|

Comment out the Memory sections configuration as shown below

.. code-block:: javascript

    /* ================ Memory sections configuration ================ */
    //Program.sectMap[".text"] = "EXT_RAM";
    //Program.sectMap[".const"] = "EXT_RAM";
    //Program.sectMap[".plt"] = "EXT_RAM";
    /* Program.sectMap["BOARD_IO_DELAY_DATA"] = "OCMC_RAM1"; */
    /* Program.sectMap["BOARD_IO_DELAY_CODE"] = "OCMC_RAM1"; */

|

Since we are no longer using a shared folder, make the following change

.. code-block:: javascript

    //var ipc_cfg = xdc.loadCapsule("../shared/ipc.cfg.xs");
    var ipc_cfg = xdc.loadCapsule("../ipc.cfg.xs");


|

Comment out the following. We'll be calling this function directly from
main.

.. code-block:: c

    //BIOS.addUserStartupFunction('&IpcMgr_ipcStartup');

|

Increase the system stack size

.. code-block:: javascript

    //Program.stack = 0x1000;
    Program.stack = 0x8000;

|

Comment out the entire TICK section

.. code-block:: javascript

    /* --------------------------- TICK --------------------------------------*/
    // var Clock = xdc.useModule('ti.sysbios.knl.Clock');
    // Clock.tickSource = Clock.TickSource_NULL;
    // //Clock.tickSource = Clock.TickSource_USER;
    // /* Configure BIOS clock source as GPTimer5 */
    // //Clock.timerId = 0;
    //
    // var Timer = xdc.useModule('ti.sysbios.timers.dmtimer.Timer');
    //
    // /* Skip the Timer frequency verification check. Need to remove this later */
    // Timer.checkFrequency = false;
    //
    // /* Match this to the SYS_CLK frequency sourcing the dmTimers.
    //  * Not needed once the SYS/BIOS family settings is updated. */
    // Timer.intFreq.hi = 0;
    // Timer.intFreq.lo = 19200000;
    //
    // //var timerParams = new Timer.Params();
    // //timerParams.period = Clock.tickPeriod;
    // //timerParams.periodType = Timer.PeriodType_MICROSECS;
    // /* Switch off Software Reset to make the below settings effective */
    // //timerParams.tiocpCfg.softreset = 0x0;
    // /* Smart-idle wake-up-capable mode */
    // //timerParams.tiocpCfg.idlemode = 0x3;
    // /* Wake-up generation for Overflow */
    // //timerParams.twer.ovf_wup_ena = 0x1;
    // //Timer.create(Clock.timerId, Clock.doTick, timerParams);
    //
    // var Idle = xdc.useModule('ti.sysbios.knl.Idle');
    // var Deh = xdc.useModule('ti.deh.Deh');
    //
    // /* Must be placed before pwr mgmt */
    // Idle.addFunc('&ti_deh_Deh_idleBegin');


|

Make configuration change to use custom resource table. Add to the end
of the file.

.. code-block:: javascript

    /* Override the default resource table with my own */
    var Resource = xdc.useModule('ti.ipc.remoteproc.Resource');
    Resource.customTable = true;

|

-  Edit **main\_led\_blink.c**

|

Add the following external declarations

.. code-block:: c

    extern Int ipc_main();
    extern Void IpcMgr_ipcStartup(Void);

|

In main(), add a call to ipc\_main() and IpcMgr\_ipcStartup() just
before BIOS\_start()

.. code-block:: c

        ipc_main();

        if (callIpcStartup) {
            IpcMgr_ipcStartup();
        }

        /* Start BIOS */
        BIOS_start();
        return (0);

|

Comment out the line that calls Board\_init(boardCfg). This call is in
the original example because it assumes TI-RTOS is running on the Arm
but in our case here, we are running Linux and this call is
destructive so we comment it out.

.. code-block:: c

    #if defined(EVM_K2E) || defined(EVM_C6678)
        boardCfg = BOARD_INIT_MODULE_CLOCK |
        BOARD_INIT_UART_STDIO;
    #else
        boardCfg = BOARD_INIT_PINMUX_CONFIG |
        BOARD_INIT_MODULE_CLOCK |
        BOARD_INIT_UART_STDIO;
    #endif
        //Board_init(boardCfg);

|

-  Edit **MainDsp1.c**

|

The app now has it's own main(), so rename this one and get rid of args

.. code-block:: c

    //Int main(Int argc, Char* argv[])
    Int ipc_main()
    {

|

No longer using args so comment these lines

.. code-block:: c

        //taskParams.arg0 = (UArg)argc;
        //taskParams.arg1 = (UArg)argv;

|

BIOS\_start() is done in the app main() so comment it out here

.. code-block:: c

        /* start scheduler, this never returns */
        //BIOS_start();

|

Comment this out

.. code-block:: c

        //Log_print0(Diags_EXIT, "<-- main:");

|

-  Edit **rsc\_table\_vayu\_dsp.c**

|

Set this #define before it's used to select PHYS\_MEM\_IPC\_VRING value

.. code-block:: c

    #define VAYU_DSP_1

|

Add this extern declaration prior to the symbol being used

.. code-block:: c

    extern char ti_trace_SysMin_Module_State_0_outbuf__A;

|

-  Edit **Server.c**

|

No longer have shared folder so change include path

.. code-block:: c

    /* local header files */
    //#include "../shared/AppCommon.h"
    #include "../AppCommon.h"

|

.. rubric:: Download the Full CCS Project
   :name: download-the-full-ccs-project

:download:`GPIO\_LedBlink\_evmAM572x\_c66xExampleProject\_with\_ipc.zip <../files/GPIO_LedBlink_evmAM572x_c66xExampleProject_with_ipc.zip>`


.. rubric:: Adding IPC to an existing TI RTOS application on the IPU
   :name: adding-ipc-to-an-existing-ti-rtos-application-on-the-ipu

A common thing people want to do is take an existing IPU application
that may be controlling serial or control interfaces and add IPC to it
so that the firmware can be loaded from the ARM. This is common when
migrating from a IPU only solution to a heterogeneous SoC with an
MPUSS (ARM) and IPUSS. This is the focus of this section.

In order to describe this process, we need an example TI RTOS test
case to work with. For this purpose, we'll be using the
UART\_BasicExample\_evmAM572x\_m4ExampleProject example that's part of
the PDK (installed as part of the Processor SDK RTOS). This example
uses TI RTOS and does serial IO using UART3 port on the AM572x GP EVM,
it's labeled Serial Debug on the EVM silkscreen.

|

There were several steps taken to make this whole process work, each of
which will be described in following sections

#. Build and run the out-of-box UART M4 example on the EVM using Code
   Composer Studio (CCS)
#. Build and run the ex02\_messageQ example from the IPC software bundle
   and turn it into a CCS project. Build it and modify the Linux startup
   code to use this new image. This is just a sanity check step to make
   sure we can build the IPC examples in CCS and have them run at boot
   up on the EVM.
#. In CCS, make a clone of the out-of-box UART M4 example and rename it
   to denote it's the IPC version of the example. Then using the
   ex02\_messageq example as a reference, add in the IPC pieces to the
   UART example code. Build from CCS then add it to the Linux firmware
   folder.

.. rubric:: Running UART Read/Write PDK Example from CCS
   :name: running-uart-readwrite-pdk-example-from-ccs

Developers are required to run pdkProjectCreate script to generate this
example as described in the `Processor SDK RTOS
article <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/
latest/rtos/index_overview.html#rebuilding-components>`__.

For the UART M4 example run the script with the following arguments:

::

    pdkProjectCreate.bat AM572x evmAM572x little uart m4

|

After you run the script, you can find the UART M4 example project at
<SDK\_INSTALL\_PATH>\\pdk\_am57xx\_1\_0\_4\\packages\\MyExampleProjects\\UART\_BasicExample\_evmAM572x\_m4ExampleProject.

Import the project in CCS and build the example. You can now connect to
the EVM using an emulator and CCS using the instructions provided in `AM572x GP EVM Hardware Setup
<How_to_Guides_Hardware_Setup_with_CCS.html#am572x-gp-evm-hardware-setup>`__

Connect to the ARM core and make sure GEL runs multicore initialization
and brings the IPUSS out of reset. Connect to IPU2 core0 and load and
run the M4 UART example. When you run the code you should see the
following log on the serial IO console:

::

    uart driver and utils example test cases :
    Enter 16 characters or press Esc
    1234567890123456  <- user input
    Data received is
    1234567890123456  <- loopback from user input
    uart driver and utils example test cases :
    Enter 16 characters or press Esc

|

.. rubric:: Build and Run ex02\_messageq IPC example
   :name: build-and-run-ex02_messageq-ipc-example

Follow instructions described in Article `Run IPC Linux
Examples <Foundational_Components_IPC.html#ipc-quick-start-guide>`__

.. rubric:: Update Linux Kernel device tree to remove UART that will be
   controlled by M4
   :name: update-linux-kernel-device-tree-to-remove-uart-that-will-be-controlled-by-m4

Linux kernel enables all SOC HW modules which are required for its
configuration. Appropriate drivers configure required clocks and
initialize HW registers. For all unused IPs clocks are not configured.

The uart3 node is disabled in kernel using device tree. Also this
restricts kernel to put those IPs to sleep mode.

::

    &uart3 {
        status = "disabled";
        ti,no-idle;
    };

.. rubric:: Add IPC to the UART Example
   :name: add-ipc-to-the-uart-example

The first step is to clone our out-of-box UART example CCS project and
rename it to denote it's using IPC. The easiest way to do this is using
CCS. Here are the steps...

-  In the **Edit** perspective, go into your **Project Explorer** window and
   right click on your UART\_BasicExample\_evmAM572x\_m4ExampleProject
   project and select **copy** from the pop-up menu. Maske sure the
   project is not is a closed state.
-  Rick click in and empty area of the project explorer window and
   select past.
-  A dialog box pops up, modify the name to denote it's using IPC. A
   good name is
   UART\_BasicExample\_evmAM572x\_m4ExampleProject\_with\_ipc.

|

This is the project we'll be working with from here on. The next thing
we want to do is select the proper RTSC platform and other components.
To do this, follow these steps.

-  Right click on the
   UART\_BasicExample\_evmAM572x\_m4ExampleProject\_with\_ipc project
   and select **Properties**
-  In the left hand pane, click on **CCS General**.
-  On the right hand side, click on the **RTSC** tab
-  For **XDCtools version:** select 3.xx.x.xx\_core
-  In the list of **Products and Repositories**, **check** the following...

   -  IPC 3.xx.x.xx
   -  SYS/BIOS 6.4x.x.xx
   -  am57xx PDK x.x.x

-  For **Target**, select **ti.targets.arm.elf.M4**
-  For **Platform**, select **ti.platforms.evmDRA7XX**
-  Once the platform is selected, edit its name buy hand and
   append :ipu2 to the end. After this it should be
   ti.platforms.evmDRA7XX:ipu2
-  Go ahead and leave the **Build-profile** set to debug.
-  Hit the OK button.

|

Now we want to copy configuration and source files from the
ex02\_messageq IPC example into our project. The IPC example is
located at
**C:\\ti\\ipc\_3\_xx\_xx\_xx\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq**.
To copy files into your CCS project, you can simply select the files
you want in Windows explorer then drag and drop them into your project
in CCS.

Copy these files into your CCS project...

-  C:\\ti\\ipc\_3\_xx\_xx\_xx\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\shared\\AppCommon.h
-  C:\\ti\\ipc\_3\_xx\_xx\_xx\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\shared\\config.bld
-  C:\\ti\\ipc\_3\_xx\_xx\_xx\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\shared\\ipc.cfg.xs

|

Now copy these files into your CCS project...

-  C:\\ti\\ipc\_3\_xx\_xx\_xx\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\ipu2\\Ipu2.cfg
-  C:\\ti\\ipc\_3\_xx\_xx\_xx\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\ipu2\\MainIpu2.c
-  C:\\ti\\ipc\_3\_xx\_xx\_xx\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\ipu2\\Server.c
-  C:\\ti\\ipc\_3\_xx\_xx\_xx\\examples\\DRA7XX\_linux\_elf\\ex02\_messageq\\ipu2\\Server.h

|

.. note::
   When you copy Ipu2.cfg into your CCS project, it
   should show up greyed out. If not, right click and exclude it from
   build. This is because the UART example already has a cfg file
   (uart\_m4\_evmAM572x.cfg). The Ipu2.cfg will be used for copying and
   pasting. When it's all done, you can delete it from your project.

Finally, you will likely want to use a custom resource table so copy
these files into your CCS project...

-  C:\\ti\\ipc\_3\_xx\_xx\_xx\\packages\\ti\\ipc\\remoteproc\\rsc\_table\_vayu\_ipu.h
-  C:\\ti\\ipc\_3\_xx\_xx\_xx\\packages\\ti\\ipc\\remoteproc\\rsc\_types.h

The rsc\_table\_vayu\_dsp.h file defines an initialized structure so
let's make a **.c** source file.

-  In your CCS project, rename rsc\_table\_vayu\_ipu.h to
   rsc\_table\_vayu\_ipu.c

|

Now we want to **merge** the IPC example configuration file with the LED
blink example configuration file. Follow these steps...

-  Open up **Ipu2.cfg** using a text editor (don't open it using the GUI).
   Right click on it and select **Open With -> XDCscript Editor**
-  We want to copy the entire contents into the clipboard. Select all
   and copy.
-  Now just like above, open the uart\_m4\_evmAM572x.cfg config file in
   the text editor. Go to the very bottom and **paste** in the contents
   from the Ipu2.cfg file. Basically we've appended the contents of
   Ipu2.cfg into uart\_m4\_evmAM572x.cfg.

|

We've now added in all the necessary configuration and source files
into our project. Don't expect it to build at this point, we have to
make edits first. These edits are listed below.

::

    NOTE, you can download the full CCS project with source files to use as a reference.
    See link towards the end of this section.

-  Edit **uart\_m4\_evmAM572x.cfg**

|

Add the following to the beginning(at the top) of your configuration file

.. code-block:: javascript

    var Program = xdc.useModule('xdc.cfg.Program');

Since we are no longer using a shared folder, make the following
change

.. code-block:: javascript

    //var ipc_cfg = xdc.loadCapsule("../shared/ipc.cfg.xs");
    var ipc_cfg = xdc.loadCapsule("../ipc.cfg.xs");

|

Comment out the following. We'll be calling this function directly from
main.

.. code-block:: javascript

    //BIOS.addUserStartupFunction('&IpcMgr_ipcStartup');

|

Increase the system stack size

.. code-block:: javascript

    //Program.stack = 0x1000;
    Program.stack = 0x8000;

|

Comment out the entire TICK section

.. code-block:: javascript

    /* --------------------------- TICK --------------------------------------*/
    // var Clock = xdc.useModule('ti.sysbios.knl.Clock');
    // Clock.tickSource = Clock.TickSource_NULL;
    // //Clock.tickSource = Clock.TickSource_USER;
    // /* Configure BIOS clock source as GPTimer5 */
    // //Clock.timerId = 0;
    //
    // var Timer = xdc.useModule('ti.sysbios.timers.dmtimer.Timer');
    //
    // /* Skip the Timer frequency verification check. Need to remove this later */
    // Timer.checkFrequency = false;
    //
    // /* Match this to the SYS_CLK frequency sourcing the dmTimers.
    //  * Not needed once the SYS/BIOS family settings is updated. */
    // Timer.intFreq.hi = 0;
    // Timer.intFreq.lo = 19200000;
    //
    // //var timerParams = new Timer.Params();
    // //timerParams.period = Clock.tickPeriod;
    // //timerParams.periodType = Timer.PeriodType_MICROSECS;
    // /* Switch off Software Reset to make the below settings effective */
    // //timerParams.tiocpCfg.softreset = 0x0;
    // /* Smart-idle wake-up-capable mode */
    // //timerParams.tiocpCfg.idlemode = 0x3;
    // /* Wake-up generation for Overflow */
    // //timerParams.twer.ovf_wup_ena = 0x1;
    // //Timer.create(Clock.timerId, Clock.doTick, timerParams);
    //
    // var Idle = xdc.useModule('ti.sysbios.knl.Idle');
    // var Deh = xdc.useModule('ti.deh.Deh');
    //
    // /* Must be placed before pwr mgmt */
    // Idle.addFunc('&ti_deh_Deh_idleBegin');

|

Make configuration change to use custom resource table. Add to the end
of the file.

.. code-block:: javascript

    /* Override the default resource table with my own */
    var Resource = xdc.useModule('ti.ipc.remoteproc.Resource');
    Resource.customTable = true;

-  Edit **main\_uart\_example.c**

|

Add the following external declarations

.. code-block:: c

    extern Int ipc_main();
    extern Void IpcMgr_ipcStartup(Void);

|

In main(), add a call to ipc\_main() and IpcMgr\_ipcStartup() just
before BIOS\_start()

.. code-block:: c

    ipc_main();
    if (callIpcStartup) {
       IpcMgr_ipcStartup();
     }
     /* Start BIOS */
     BIOS_start();
     return (0);

|

Comment out the line that calls Board\_init(boardCfg). This call is in
the original example because it assumes TI-RTOS is running on the Arm
but in our case here, we are running Linux and this call is destructive
so we comment it out. The board init call does all pinmux configuration,
module clock and UART peripheral initialization.

In order to run the UART Example on M4, you need to disable the UART in
the Linux DTB file and interact with the Linux kernel using Telnet (This
will be described later in the article). Since Linux will be running
uboot performs the pinmux configuration but clock and UART Stdio setup
needs to be performed by the M4.

**Original code**

.. code-block:: c

    #if defined(EVM_K2E) || defined(EVM_C6678)
        boardCfg = BOARD_INIT_MODULE_CLOCK | BOARD_INIT_UART_STDIO;
    #else
        boardCfg = BOARD_INIT_PINMUX_CONFIG | BOARD_INIT_MODULE_CLOCK | BOARD_INIT_UART_STDIO;
    #endif
        Board_init(boardCfg);

|

**Modified Code :**

::

       boardCfg = BOARD_INIT_UART_STDIO;
       Board\_init(boardCfg);

We are not done yet as we still need to configure turn the clock control
on for the UART without impacting the other clocks. We can do that by
adding the following code before Board\_init API call:

::

       CSL_l4per_cm_core_componentRegs *l4PerCmReg =
           (CSL_l4per_cm_core_componentRegs *)CSL_MPU_L4PER_CM_CORE_REGS;
       CSL_FINST(l4PerCmReg->CM_L4PER_UART3_CLKCTRL_REG,
           L4PER_CM_CORE_COMPONENT_CM_L4PER_UART3_CLKCTRL_REG_MODULEMODE, ENABLE);
       while(CSL_L4PER_CM_CORE_COMPONENT_CM_L4PER_UART3_CLKCTRL_REG_IDLEST_FUNC !=
          CSL_FEXT(l4PerCmReg->CM_L4PER_UART3_CLKCTRL_REG,
           L4PER_CM_CORE_COMPONENT_CM_L4PER_UART3_CLKCTRL_REG_IDLEST));

-  Edit **MainIpu2.c**

|

The app now has it's own main(), so rename this one and get rid of args

.. code-block:: c

    //Int main(Int argc, Char* argv[])
    Int ipc_main()
    {

No longer using args so comment these lines

::

       //taskParams.arg0 = (UArg)argc;
       //taskParams.arg1 = (UArg)argv;

BIOS\_start() is done in the app main() so comment it out here

::

    /* start scheduler, this never returns */
    //BIOS_start();

|

Comment this out

::

       //Log_print0(Diags_EXIT, "<-- main:");

|

-  Edit **rsc\_table\_vayu\_ipu.c**

|

Set this #define before it's used to select PHYS\_MEM\_IPC\_VRING value

::

    #define VAYU_IPU_2

|

Add this extern declaration prior to the symbol being used

::

    extern char ti_trace_SysMin_Module_State_0_outbuf__A;

|

-  Edit **Server.c**

|

No longer have shared folder so change include path

.. code-block:: c

    /* local header files */
    //#include "../shared/AppCommon.h"
    #include "../AppCommon.h"

.. rubric:: Handling AMMU (L1 Unicache MMU) and L2 MMU
   :name: handling-ammu-l1-unicache-mmu-and-l2-mmu

There are two MMUs inside each of the IPU1, and IPU2 subsystems. The L1
MMU is referred to as IPU\_UNICACHE\_MMU or AMMU and L2 MMU. The
description of how this is configured in IPC-remoteproc has been
described in section
`Changing\_Cortex\_M4\_IPU\_Memory\_Map <Foundational_Components_IPC.html#ipc-for-am57xx>`__.
IPC handling of L1 and L2 MMU is different from how the PDK driver
examples setup the memory access using these MMUs which the users need
to manage when integrating the components. This difference is
highlighted below:

.. Image:: /images/IPU_MMU_Peripheral_access.png

-  PDK examples use addresses (0x4X000000) to peripheral registers and
   use following MMU setting

   -  L2 MMU uses default 1:1 Mapping
   -  AMMU configuration translates physical 0x4X000000 access to
      logical 0x4X000000

-  IPC+ Remote Proc ARM+M4 requires IPU to use logical address
   (0x6X000000) and uses following MMU setting

   -  L2 MMU is configured such that MMU translates 0x6X000000 access to
      addresss 0x4X000000
   -  AMMU is configured for 1:1 mapping 0x6X000000 and 0x6X000000

Therefore after integrating IPC with PDK drivers, it is recommended that
the alias addresses are used to access peripherals and PRCM registers.
This requires changes to the addresses used by PDK drivers and in
application code.

The following changes were then made to the IPU application source code:

Add UART\_soc.c file to the project and modify the base addresses for
all IPU UART register instance in the UART\_HwAttrs to use alias
addresses:

.. code-block:: c

    #ifdef _TMS320C6X
        CSL_DSP_UART3_REGS,
        OSAL_REGINT_INTVEC_EVENT_COMBINER,
    #elif defined(__ARM_ARCH_7A__)
        CSL_MPU_UART3_REGS,
        106,
    #else
        (CSL_IPU_UART3_REGS + 0x20000000),    //Base Addr = 0x48000000 + 0x20000000 = 0x68000000
        45,
    #endif

Adding custom SOC configuration also means that you should use the
generic UART driver instead of driver with built in SOC setup. To do
this comment the following line in .cfg:

::

    var Uart              = xdc.loadPackage('ti.drv.uart');
    //Uart.Settings.socType = socType;

There is also an instance in the application code where we added pointer
to PRCM registers that need to be changed as follows.

::

       CSL_l4per_cm_core_componentRegs *l4PerCmReg =
      (CSL_l4per_cm_core_componentRegs \*) 0x6a009700; //CSL_MPU_L4PER_CM_CORE_REGS;

Now, you are ready to build the firmware. After the .out is built,
change the extension to .xem4 and copy it over to the location in the
filesystem that is used to load M4 firmware.

.. rubric:: Download the Full CCS Project
   :name: download-the-full-ccs-project-1

:download:`UART\_BasicExample\_evmAM572x\_m4ExampleProject\_with\_ipc.zip <../files/UART_BasicExample_evmAM572x_m4ExampleProject_with_ipc.zip>`

