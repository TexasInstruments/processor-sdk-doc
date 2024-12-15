Introduction
============

This article is geared toward 66AK2x users that are running Linux on the Cortex A15. The goal is to help users understand how to gain access to the DSP (c66x) subsystem of the 66AK2x. While the examples used in this guide are specific to K2G, the information provided here applies to all K2x platforms.

Software Dependencies to Get Started
====================================

Prerequisites

-  `Processor SDK Linux for
   K2G <http://software-dl.ti.com/processor-sdk-linux/esd/K2G/latest/index_FDS.html>`__
-  `Processor SDK RTOS for
   K2G <http://software-dl.ti.com/processor-sdk-rtos/esd/K2G/latest/index_FDS.html>`__
-  `Code Composer
   Studio <http://processors.wiki.ti.com/index.php/Download_CCS>`__
   (choose version as specified on Proc SDK download page)

.. note::
   Please be sure that you have the same version number
   for both Processor SDK RTOS and Linux.

For reference within the context of this page, the Linux SDK is
installed at the following location:

::

    /mnt/data/user/ti-processor-sdk-linux-k2g-evm-xx.xx.xx.xx
	├── bin
	├── board-support
	├── docs
	├── example-applications
	├── filesystem
	├── linux-devkit
	├── linux-devkit.sh
	├── Makefile
	├── Rules.make
	└── setup.sh


The RTOS SDK is installed at the following location:

::

    /mnt/data/user/my_custom_install_sdk_rtos_k2g_xx_xx.xx
	├── bios_6_xx_xx_xx
	├── cg_xml
	├── ctoolslib_x_x_x_x
	├── dsplib_c66x_x_x_x_x
	├── edma3_lld_x_xx_x_xxx
	├── framework_components_x_xx_xx_xx
	├── gcc-arm-none-eabi-6-2017-q1-update
	├── imglib_c66x_x_x_x_x
	├── ipc_3_xx_xx_xx
	├── mathlib_c66x_x_x_x_x
	├── multiprocmgr_x_x_x_x
	├── ndk_3_xx_xx_xx
	├── openmp_dsp_k2g_2_xx_xx_xx
	├── pdk_k2g_x_x_xx
	├── processor_sdk_rtos_k2g_x_xx_xx_xx
	├── uia_2_xx_xx_xx
	├── xdais_7_xx_xx_xx
	├── xdctools_3_xx_xx_xx


|

Multiple Processor Manager
==========================

The Multiple Processor Manager (MPM) module is used to load and run DSP images from the ARM. The following section provides some more detail on the MPM.


-	The MPM has the two following major components:

	- 	MPM server (mpmsrv): It runs as a daemon and runs automatically in the default filesystem supplied in Processor SDK. It parses the MPM configuration file from /etc/mpm/mpm_config.json, and then waits on a UNIX domain socket. The MPM server runs and maintains a state machine for each slave core.
	-	MPM command line/client utility (mpmcl): It is installed in the filesystem and provides command line access to the server.

-	The following are the different methods that can be used by MPM to load and run slave images:

	-	Using mpmcl utility.
	-	From the config file, to load at bootup.
	-	Writing an application to use mpmclient header file and library.

-	The location of the mpm server/daemon logs is based on the "outputif" configuration in the JSON config file. By default, this is /var/log/syslog.

-	The load command writes the slave image segments to memory using UIO interface. The run command runs the slave images.

-	All events from the state transition diagram are available as options of mpmcl command, except for the crash event.

-	The reset state powers down the slave nodes.

**Software Flow Diagram Slave States in MPM**

.. Image:: /images/MPM_Structure.png

Methods to load and run ELF images using MPM
--------------------------------------------

**Using mpmcl utility to manage slave processors**

Use mpmcl --help for details on the supported commands. The following is the output of mpmcl help:

::

	Usage: mpmcl <command> [slave name] [options]
	Multiproc manager CLI to manage slave processors
	<command>    Commands for the slave processor
                     Supported commands: ping, load, run, reset, status, coredump, transport
                     load_withpreload, run_withpreload
	[slave name] Name of the slave processor as specified in MPM config file
	[options]    In case of load, the option field need to have image file name


The following is a sample set of mpmcl commands for managing slave processors:


+-------------------------------------------------------------+------------------------------------------------+
| Command                                                     | Description                                    |
+=============================================================+================================================+
| mpmcl ping                                                  | Ping daemon if it is alive                     |
+-------------------------------------------------------------+------------------------------------------------+
| mpmcl status dsp0                                           | Check status of dsp core 0                     |
+-------------------------------------------------------------+------------------------------------------------+
| mpmcl load dsp0 dsp-core0.out                               | Load dsp core 0 with an image                  |
+-------------------------------------------------------------+------------------------------------------------+
| mpmcl run dsp0                                              | Run dsp core 0                                 |
+-------------------------------------------------------------+------------------------------------------------+
| mpmcl reset dsp0                                            | Reset dsp core 0                               |
+-------------------------------------------------------------+------------------------------------------------+
| mpmcl load_withpreload dsp0 preload_image.out dsp-core0.out | Load dsp core 0 image with a preload image     |
+-------------------------------------------------------------+------------------------------------------------+
| mpmcl run_withpreload dsp0                                  | Run dsp core 0 with preload                    |
+-------------------------------------------------------------+------------------------------------------------+


.. note:: In the case of an error, the mpm server takes the slave to error state. You need to run the reset command to change back to idle state so that the slave can be loaded and run again.

.. note:: The idle status of the slave core means the slave core is not loaded as far as MPM is concerned. It does NOT mean the slave core is running idle instructions.

|

**Loading and running slave images at bootup**

The config file can load a command script to load and run slave cores at bootup. The path of the script is to be added in "cmdfile": "/etc/mpm/slave_cmds.txt" in the config file. The following is a sample command to load and run DSP images:

::

	dsp0 load ./dsp-core0.out
	dsp1 load ./dsp-core0.out
	dsp0 run
	dsp1 run

**Managing slave processors from application program**

An application can include mpmclient.h from the MPM package and link to libmpmclient.a to load/run/reset slave cores. The mpmcl essentially is a wrapper around this library to provide command line access for the functions from mpmclient.h.

**DSP Image Requirements**

For MPM to properly load and manage a DSP image, the following is required:

-	The DSP image should be in ELF format.

-	The MPM ELF loader loads those segments to DSP memory, whose PT_LOAD field is set. In order to skip loading of a particular section, set the type to NOLOAD in the command/cfg file.

.. code:: c

	/* Section not to be loaded by remoteproc loader */
	Program.sectMap[".noload_section"].type = "NOLOAD";

-	The default allowed memory ranges for DSP segments are as follows:

+---------------+----------------------+---------+
|               | Start Address        |  Length |
+===============+======================+=========+
| L2 Local      | 0x00800000           |  1MB    |
+---------------+----------------------+---------+
| L2 Global     | 0x[1-4]0800000       |   1MB   |
+---------------+----------------------+---------+
| MSMC          | 0x0C000000           |  6MB    |
+---------------+----------------------+---------+
| DDR3          | 0xA0000000           | 512MB   |
+---------------+----------------------+---------+


The segment mapping can be changed using the mpm_config.json and Linux kernel device tree.

|

Getting Started with IPC Linux Examples
=======================================

The figure below illustrates how remoteproc/rpmsg driver from ARM Linux
kernel communicates with IPC driver on slave processor (e.g. DSP) running RTOS.

.. Image:: /images/LinuxIPC_with_RTOS_Slave.png

In order to setup IPC on slave cores, we provide some pre-built examples
in IPC package that can be run from ARM Linux. The subsequent sections
describe how to build and run this examples and use that as a starting
point for this effort.

|

Building the Bundled IPC Examples
---------------------------------

The instructions to build IPC examples found under ipc_3_xx_xx_xx/examples/66AK2G_linux_elf have been provided in the
`Processor SDK IPC Quick Start Guide <Foundational_Components_IPC.html#build-ipc-linux-examples>`__.

Let's focus on one example in particular, ex02\_messageq, which is located at **<rtos-sdk-install-dir>/ipc\_3\_xx\_xx\_xx/examples/66AK2G\_linux\_elf/ex02\_messageq**.

Here are the key files that you should see after a successful build:

::

	├── core0
	│   └── bin
	│       ├── debug
	│       │   └── server_core0.xe66
	│       └── release
	│           └── server_core0.xe66
	├── host
	│   └── bin
	│       ├── debug
	│       │   └── app_host
	│       └── release
	│       │   └── app_host



|

Running the Bundled IPC Examples
--------------------------------

**NOTE 1**: Before running the IPC examples, any other application already running and using the DSP cores, need to be stopped and disabled.
In addition, the EVM need to be rebooted so that the cache configuration of the previous firmware downloaded does not affect the execution of the example.
In the Linux Filesystem distributed part of the Processor SDK, OpenCL examples are configured to run by default. So use the following procedure to shutdown the openCL under section before running the IPC example: `Disable OpenCL Application`_.

**NOTE 2**: If the application really needs to dynamically download different DSP images, especially with different cache configuration, then a dummy image which resets the cache configuration in the DSP, need to be downloaded and run before downloading the actual example images.

You will need to copy the ex02\_messageq executable binaries onto the target (through SD card, NFS export, SCP, etc.).
You can copy the entire ex02\_messageq directory, though we're primarily interested in
these executable binaries:

-   Core0/bin/debug/ server_core0.xe66
-   host/bin/debug/app_host

The Multi-Processor Manager (MPM) Command Line utilities are used to download and start the DSP executables.

Let’s load the example and run the DSP:

::

    root@k2g-evm:~# mpmcl reset dsp0
    root@k2g-evm:~# mpmcl status dsp0
    root@k2g-evm:~# mpmcl load dsp0 server_core0.xe66
    root@k2g-evm:~# mpmcl run dsp0

You should see the following output:

::

	[  919.637071] remoteproc remoteproc0: powering up 10800000.dsp
	[  919.650495] remoteproc remoteproc0: Booting unspecified pre-loaded fw image
	[  919.683836] virtio_rpmsg_bus virtio0: rpmsg host is online
	[  919.689355] virtio_rpmsg_bus virtio0: creating channel rpmsg-proto addr 0x3d
	[  919.712755] remoteproc remoteproc0: registered virtio0 (type 7)
	[  919.718671] remoteproc remoteproc0: remote processor 10800000.dsp is now up


Now, we can run the IPC example:

::

	root@k2g-evm:~# ./app_host CORE0


The following is the expected output:

::

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

|

Understanding the Memory Map
============================

Overall Linux Memory Map
------------------------

::

	root@k2g-evm:~# cat /proc/iomem
	[snip...]
	80000000-8fffffff : System RAM (boot alias)
	92800000-97ffffff : System RAM (boot alias)
	9d000000-ffffffff : System RAM (boot alias)
	800000000-80fffffff : System RAM
		800008000-800dfffff : Kernel code
		801000000-80109433b : Kernel data
	812800000-817ffffff : System RAM
	818000000-81cffffff : CMEM
	81d000000-87fffffff : System RAM

**CMA Carveouts**

To view the allocation at run-time:

::

	root@k2g-evm:~# dmesg | grep "Reserved memory"
	[    0.000000] Reserved memory: created CMA memory pool at 0x000000081f800000, size 8 MiB

The CMA block is defined in the following file for the K2G EVM:

linux/arch/arm/boot/dts/keystone-k2g-evm.dts

**CMEM**

To view the allocation at run-time:

::

	root@k2g-evm:~# cat /proc/cmem
	Block 0: Pool 0: 1 bufs size 0x5000000 (0x5000000 requested)
	Pool 0 busy bufs:
	Pool 0 free bufs:
	id 0: phys addr 0x818000000

This shows that we have defined a CMEM block at physical address 0x818000000 with total size 0x5000000. This block contains a buffer pool consisting of 1 buffer. Each buffer in the pool (only one in this case) is defined to have a size of 0x5000000.

The CMEM block is defined in the following file for the K2G EVM:

linux/arch/arm/boot/dts/k2g-evm-cmem.dtsi

|

Changing the DSP Memory Map
===========================

Linux Device Tree
-----------------

The carveouts for the DSP are defined in the Linux dts file. For the K2G EVM, these definitions are located in linux/arch/arm/boot/dts/keystone-k2g-evm.dts

::

	reserved-memory {
		#address-cells = <2>;
		#size-cells = <2>;
		ranges;

		dsp_common_mpm_memory: dsp-common-mpm-memory@81d000000 {
			compatible = "ti,keystone-dsp-mem-pool";
			reg = <0x00000008 0x1d000000 0x00000000 0x2800000>;
			no-map;
			status = "okay";
		};
		dsp_common_memory: dsp-common-memory@81f800000 {
			compatible = "shared-dma-pool";
			reg = <0x00000008 0x1f800000 0x00000000 0x800000>;
			reusable;
			status = "okay";
		};
	};

The memory region "dsp_common_mpm_memory" starts at address 0x9d000000 and has a size of 0x2800000 bytes. This region is where the DSP code/data needs to reside. If they are not in this region, you will see the error "load failed (error: -104)" when trying to load.

The memory region "dsp_common_memory” starts at address 0x9f800000 and has a size of 0x800000. This is a CMA pool, as indicated by the line “compatible = "shared-dma-pool";”, and is reserved for
Virtque region and Rpmsg vring buffers.

As of Processor SDK 5.2, the Virtque and vring buffers are allocated by the remoteproc driver from this region and communicated to the slave by update to the resource table.


Resource Table
--------------

The default resource table for K2G is located at ipc_3_xx_xx_xx/packages/ti/ipc/remoteproc/rsc_table_tci6638.h

The resource table contains the definitions of the CMA carveout for the Rpmsg vring buffers.

MPM Config File
---------------

The MPM configuration file is a JSON format configuration file and is located in the default root file system release as part of Processor SDK Linux. It is labeled “mpm_config.json” and is located in /etc/mpm.

The following are some details regarding the MPM configuration file:

-	The MPM parser ignores any JSON elements which it does not recognize. This can be used to put comments in the config file.

-	The tag cmdfile (which is commented as _cmdfile by default) loads and runs MPM commands at bootup.

-	The tag outputif can be syslog, stderr or filename if it does not match any predefined string.

-	By default, the config file allows loading of DSP images to L2, MSMC and DDR. It can be changed to add more restrictions on loading, or to load to L1 sections.

-	In current form, MPM does not do MPAX mapping for local to global addresses and the default MPAX mapping is used.

-	By default, the MPM configuration file configures the MSMC region with start address at 0x0c000000 and size of 0x600000 bytes, and the DDR region with start address of 0xa0000000 and size of 0x10000000 bytes, as seen in the snippet below.

.. code-block:: javascript

		{
			"name": "local-msmc",
			"globaladdr": "0x0c000000",
			"length": "0x600000",
			"devicename": "/dev/dspmem"
		},
		{
			"name": "local-ddr",
			"globaladdr": "0xa0000000",
			"length": "0x10000000",
			"devicename": "/dev/dspmem"
		},

Config.bld
----------

The config.bld file is used by the IPC examples to configure the external memory map at the application level. It is located in /ipc_3_x_x_x/examples/66AK2G_linux_elf/ex02_messageq/shared/. A linker command file can be used as well, in place of a config.bld file, to place sections into memory.

By default, the ex02_messageq runs from MSMC memory so the config.bld file is not used. In the next section, we will show how to modify the config.bld to place the DSP code in DDR.


Modifying ex02_messageQ example to run from DDR
===============================================

As an example, the following section shows how to modify the IPC memory map to run the ex02_messageq example from DDR instead of MSMC.


**Changes to Config.bld**

We want to place the DSP application in DDR instead of MSMC, so we need to make the following changes to the config.bld file.

Remove the following lines:

.. code-block:: javascript

	Build.platformTable["ti.platforms.evmTCI66AK2G02:core0"] = {
    externalMemoryMap: [ ]
	};

and add the following:

.. code-block:: javascript

	var evmTCI66AK2G02_ExtMemMapDsp = {
		EXT_DDR: {
			name: "EXT_DDR",
			base: 0x9d000000,
			len:  0x00100000,
			space: "code/data",
			access: "RWX"
		},
	};

	Build.platformTable["ti.platforms.evmTCI66AK2G02:core0"] = {
		externalMemoryMap: [
			[ "EXT_DDR", evmTCI66AK2G02_ExtMemMapDsp.EXT_DDR ],
		],
		codeMemory: "EXT_DDR",
		dataMemory: "EXT_DDR",
		stackMemory: "EXT_DDR",
	};

This will place the DSP code, data, and stack memory at address 0x9d000000. We have chosen address 0x9d000000 because that is what is defined in the Linux device tree by default. Refer to the “dsp_common_mpm_memory” block in the previous section “Linux Device Tree.” Note, the length specified here is 0x00100000; this must be less than the size of the dsp_common_mpm_memory pool.

**Changes to the MPM Config File**

By default, mpm_config.json defines the DDR region to start at 0xa0000000 with a length of 0x10000000. We need to change this to include the region where our application resides so we will change it to span from 0x90000000 to 0xc0000000. This can be increased as needed by the application.

To do this, change the following block from:

.. code-block:: javascript

		{
			"name": "local-ddr",
			"globaladdr": "0xa0000000",
			"length": "0x10000000",
			"devicename": "/dev/dsp0"
		},

To:

.. code-block:: javascript

		{
			"name": "local-ddr",
			"globaladdr": "0x90000000",
			"length": "0x30000000",
			"devicename": "/dev/dsp0"
		},


**Changes to Core0.cfg**

Remove the following lines:

.. code-block:: javascript

	Program.sectMap[".text:_c_int00"] = new Program.SectionSpec();
	Program.sectMap[".text:_c_int00"].loadSegment = "L2SRAM";
	Program.sectMap[".text:_c_int00"].loadAlign = 0x400;

These lines above place the .text section into L2SRAM. We want it to be in DDR so it needs to be removed.

Remove the following lines:

::

	var Resource = xdc.useModule('ti.ipc.remoteproc.Resource');
	Resource.loadSegment = Program.platform.dataMemory;

These lines place the resource table into the dataMemory section, which in our case is in DDR memory.

The Remoteproc driver requires the trace buffers and resource table to be placed into L2SRAM. If they are not, you will see the following error when loading:

::

	keystone-rproc 10800000.dsp: error in ioctl call: cmd 0x40044902
	(2), ret -22
	load failed (error: -107)

So we will need to add the following lines to place the trace buffer and resource table into L2SRAM:

::

	Program.sectMap[".far"] = new Program.SectionSpec();
	Program.sectMap[".far"].loadSegment = "L2SRAM";
	Program.sectMap[".resource_table"] = new Program.SectionSpec();
	Program.sectMap[".resource_table"].loadSegment = "L2SRAM";
	var Resource = xdc.useModule('ti.ipc.remoteproc.Resource');
	Resource.loadSegment = "L2SRAM"

Now follow the steps in `Running the Bundled IPC Examples`_.


Loading DSP images from CCS (without using MPM)
===============================================

By default, the DSP cores are powered down by u-boot at the time of EVM boot. After kernel is running, MPM can be used to load and run DSP images from Linux command-line/utility.

Rather than using MPM, if you want to use CCS to load and run DSP images, then set the following setting in u-boot prompt:

::

	setenv debug_options 1
	saveenv
	reset

This will not power down DSPs at startup and CCS/JTAG can connect to the DSP for loading and debugging. This option is useful if you want to boot Linux on ARM and then use JTAG to manually load and run the DSPs. Otherwise you may see "held in reset" errors in CCS.

.. note:: The above step is not needed if you want to load DSP cores using MPM and subsequently use CCS to connect to DSP.

MPM Debugging
=============

The following are some pointers for MPM debugging.

**MPM Error Codes**

-	If MPM server crashed/exited/not running in the system, mpmcl ping will return failure

-	If there is any load/run/reset failure MPM client provides error codes. The major error codes are given below.

+------------+------------------------------------+
| error code |	error type                        |
+============+====================================+
| -100       |	error_ssm_unexpected_event        |
+------------+------------------------------------+
| -101       |	error_ssm_invalid_event           |
+------------+------------------------------------+
| -102       |	error_invalid_name_length         |
+------------+------------------------------------+
| -103       |	error_file_open	                  |
+------------+------------------------------------+
| -104       |	error_image_load                  |
+------------+------------------------------------+
| -105       |	error_uio                         |
+------------+------------------------------------+
| -106       |	error_image_invalid_entry_address |
+------------+------------------------------------+
| -107       |	error_resource_table_setting      |
+------------+------------------------------------+
| -108       |	error_error_no_entry_point        |
+------------+------------------------------------+
| -109       |	error_invalid_command             |
+------------+------------------------------------+

-	The MPM daemon logs goes to /var/log/syslog by default. This file can provide more information on the errors.

**DSP trace/print messages from Linux**

The DSP log messages can be read from following debugfs locations:

::

	DSP log entry for core #: /sys/kernel/debug/remoteproc/remoteproc#/trace0

Where # is the core id starting from 0.

::

  root@keystone-evm:~# cat /sys/kernel/debug/remoteproc/remoteproc0/trace0
  Main started on core 1
  ....
  root@keystone-evm:~#

Detecting crash event in MPM
----------------------------

In the case of a DSP exception, the MPM calls the script provided in JSON config file. The Processor SDK Linux filesystem has a sample script /etc/mpm/crash_callback.sh that sends message to syslog indicating which core crashed. This script can be customized to suit notification needs.

**Generating DSP coredump**

The DSP exceptions can be any of the following:

-	Software-generated exceptions
-	Internal/external exceptions
-	Watchdog timer expiration

The MPM creates an ELF formatted core dump.

::

	root@keystone-evm:~# mpmcl coredump dsp0 coredump.out

The above command will generate a coredump file with name coredump.out for the DSP core 0.

.. note:: The coredump can be captured from a running system that is not crashed, in this case the register information won't be available in the coredump.


Disable OpenCL Application
==========================

The OpenCL application needs to be disabled since it interferes with the caching properties of the memory region used by our modified example. If it is not disabled, the application will hang at App_create(). It can be disabled by issuing the following command:

::

	root@k2g-evm:~# systemctl disable ti-mct-daemon.service

|

After power-cycling the EVM, we can now load and run the example.


Frequently Asked Questions
==========================

Q: How to maintain cache coherency

A: In the first 2GB of DDR, region 00 8000 0000 - 00 FFFF FFFF (alias of 08 0000 0000 - 08 7FFF FFFF), no IO coherency is supported. Cache coherency will need to be maintained by software. The cache coherence API descriptions for the A15 can be found in the `TI-RTOS Cache Module cdocs. <http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/sysbios/6_52_00_12/exports/bios_6_52_00_12/docs/cdoc/ti/sysbios/family/arm/a15/Cache.html#xdoc-desc>`__

Q: MPM does not load and run the DSP image

A: There can be several scenarios, the following are a few of them:

-	The MPM server may not be running. The command mpmcl ping will timeout in this case. The mpm server is expected to be running in the background to service the requests from mpm client. The log file /var/log/mpmsrv.log can provide more information.

-	An issue can be the devices relevant to MPM /dev/dsp0, ... , /dev/dsp7, /dev/dspmem are not created. You need to check if these devices are present. If they are not present then check if the kernel and device tree have right patches for these devices.

-	The log can print error codes provided in MPM error codes section.

-	Another way to debug loading issues is, to run mpm server in non-daemon mode from one shell using command mpmsrv -n, before this you need to kill the server if it is running. (The command to kill is mpmsrv -k or you can choose to kill the process). Then from other shell run the client operations.

Q: MPM fails to load the segments


A: The MPM fundamentally copies segments from DSP image to memory using a custom UIO mmap interface. Each local or remote node (DSPs) is allocated some amount of resources using the config file. The segments in the config file needs to be subset of memory resources present in kernel dts file. The system integrator can choose to add or change memory configurations as needed by application. In order to change the default behavior user need to change in JSON config file and kernel device tree. In JSON configuration file, the segments section need to be updated. You need to make sure it does not overlap the scratch memory section. You might have to move the scratch section if the allocated DDR size is increased. And, in the kernel device tree the mem sections of dsp0, .. , dsp7, dspmem need to be updated.

-	Sometimes few segments used by DSP may not accessible by ARM at the time of loading. These segment can cause load failure. So it is useful to understand the memory layout of your own application and if there are any such sections, you can skip loading those segments to memory using NOLOAD method described above.

-	The MPM does not have MPAX support yet. So the MPAX support needs to be handled by application.

-	If the linker adds a hole in the resource table section right before the actual resource_table due to the alignment restriction, then MPM as of now won't be able to skip the hole and might get stuck. In this case if you hex-dump resource table (method given below) size will be quite large (normally for a non-IPC case it is around 0xac). The workaround is to align the .resource_table section to 0x1000 using linker command file or some other method so that linker does not add any hole in the resource_table section. In future, MPM will take care of this offset.

Q: MPM fails to run the image

A: MPM takes DSP out of reset to run the image. So, the fails to run normally attributed to DSP is crashing before main or some other issue in the image. But, to debug such issue, after mpmcl run, use CCS to connect to the target and then do load symbols of the images. Then the DSP can be debugged using CCS. Another way to debug the run issue, is to aff a infinite while loop in the reset function so that the DSP stops at the very beginning. Then load and run the DSP using MPM and connect thru CCS, do load symbols and come out of while loop and debug.

Q: I don't see DSP prints from debugfs

A: Make sure you followed the procedure described above to include the resource table in the image. Care should be taken for the resource table not being compiled out by linker. To check if the resource table present in the image using command readelf --hex-dump=.resource_table <image name>. It should have some non-zero data.
Another point is, if you are loading same image in multiple cores and if the resource table and trace buffer segments overlap with each other in memory, then there can be undesirable effect.

Q: I see the DSP state in /sys/kernel/debug/remoteproc/remoteproc0/state as crashed

A: The file /sys/kernel/debug/remoteproc/remoteproc#/state does not indicate state of DSP when MPM is used for loading. The state of the DSP can be seen using MPM client. See the description of the command in Methods to load and run ELF images using MPM sections.

