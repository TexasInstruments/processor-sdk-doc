.. _foundational-components-ipc:

IPC for J721E
==============

The J721E processors have Cortex-R5F, C66x DSP and C71x subsystems in addition to
a dual core Cortex-A72 subsystem. Please refer to the J721E Technical Reference Manual for details.

This article is geared toward J721E users that are running Linux on the Cortex
A72 cores. The goal is to help users understand how to establish IPC communication
with the C66x ,C71x DSP and R5F cores.

There are many facets to this task: building, loading, debugging, memory
sharing, etc. This article intends to take incremental steps toward
understanding all of those pieces.

Typical Boot Flow on J721E for ARM Linux users
-----------------------------------------------

J721E SOC's have multiple processor cores - Cortex-A72, Cortex-R5F and DSP cores.

The MCU R5F firmware runs device manager software (SciServer).
The MCU R5F firmware (DM) is integrated as part of tispl.bin binary
and is started early in the boot process, right after DDR initialization,
by u-boot SPL running on MCU R5.

The A72 typically runs a HLOS like Linux/Android. The C66x, C71x and R5F remote cores
run No-OS or RTOS (FreeRTOS etc). In normal operation, the boot loader (U-Boot/SPL)
boots and loads the A72 with the HLOS. The A72 then boots the C66x, C71x and R5F cores.

Getting Started with IPC Linux Examples
---------------------------------------

The figure below illustrates how the Remoteproc/RPMsg driver from the ARM Linux
kernel communicates with the IPC driver on a remote processors (e.g. R5F)
running RTOS.

.. Image:: /images/LinuxIPC_with_RTOS_Slave.png

In order to setup IPC on remote cores, we provide some pre-built examples
in the SDK package that can be run from ARM Linux.

The remoteproc driver is hard-coded to look for specific files when
loading the R5F, C66x and C71x cores. Here are the files it looks for on an J721E device:

.. code-block:: text

	+------------------+-----------------+----------------------+-----------------------+
	| Core Name        | RemoteProc Name | Description          | Firmware File Name    |
	+==================+=================+======================+=======================+
	| C66x             | 4d80800000.dsp  | C66x core            | j7-c66_0-fw           |
	+------------------+-----------------+----------------------+-----------------------+
	| C66x             | 4d81800000.dsp  | C66x core            | j7-c66_1-fw           |
	+------------------+-----------------+----------------------+-----------------------+
	| C71x             | 64800000.c7x    | C71x core            | j7-c71_0-fw           |
	+------------------+-----------------+----------------------+-----------------------+
	| C71x             | 65800000.c7x    | C71x core            | j7-c71_1-fw           |
	+------------------+-----------------+----------------------+-----------------------+
	| R5F              | 41000000.r5f    | R5F core(MCU domain) | j7-mcu-r5f0_0-fw      |
	+------------------+-----------------+----------------------+-----------------------+
	| R5F              | 41400000.r5f    | R5F core(MCU domain) | j7-mcu-r5f0_1-fw      |
	+------------------+-----------------+----------------------+-----------------------+
	| R5F              | 5c00000.r5f     | R5F core(MAIN domain)| j7-main-r5f0_0-fw     |
	+------------------+-----------------+----------------------+-----------------------+
	| R5F              | 5d00000.r5f     | R5F core(MAIN domain)| j7-main-r5f0_1-fw     |
	+------------------+-----------------+----------------------+-----------------------+
	| R5F              | 5e00000.r5f     | R5F core(MAIN domain)| j7-main-r5f1_0-fw     |
	+------------------+-----------------+----------------------+-----------------------+
	| R5F              | 5f00000.r5f     | R5F core(MAIN domain)| j7-main-r5f1_1-fw     |
	+------------------+-----------------+----------------------+-----------------------+

Generally on a target file system the above files are soft linked to the
intended executable FW files:

.. code-block:: console

	root@j721e-evm:~# ls -l /lib/firmware/
	lrwxrwxrwx 1 root root      69 Mar  9  2018 j7-c66_0-fw -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_c66xdsp_1_release_strip.xe66
	lrwxrwxrwx 1 root root      76 Mar  9  2018 j7-c66_0-fw-sec -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_c66xdsp_1_release_strip.xe66.signed
	lrwxrwxrwx 1 root root      69 Mar  9  2018 j7-c66_1-fw -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_c66xdsp_2_release_strip.xe66
	lrwxrwxrwx 1 root root      76 Mar  9  2018 j7-c66_1-fw-sec -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_c66xdsp_2_release_strip.xe66.signed
	lrwxrwxrwx 1 root root      65 Mar  9  2018 j7-c71_0-fw -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_c7x_1_release_strip.xe71
	lrwxrwxrwx 1 root root      72 Mar  9  2018 j7-c71_0-fw-sec -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_c7x_1_release_strip.xe71.signed
	lrwxrwxrwx 1 root root      65 Mar  9  2018 j7-main-r5f0_0-fw -> /lib/firmware/ti-eth/j721e/app_remoteswitchcfg_server_strip.xer5f
	lrwxrwxrwx 1 root root      72 Mar  9  2018 j7-main-r5f0_0-fw-sec -> /lib/firmware/ti-eth/j721e/app_remoteswitchcfg_server_strip.xer5f.signed
	lrwxrwxrwx 1 root root      67 Mar  9  2018 j7-main-r5f0_1-fw -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_mcu2_1_release_strip.xer5f
	lrwxrwxrwx 1 root root      74 Mar  9  2018 j7-main-r5f0_1-fw-sec -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_mcu2_1_release_strip.xer5f.signed
	lrwxrwxrwx 1 root root      67 Mar  9  2018 j7-main-r5f1_0-fw -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_mcu3_0_release_strip.xer5f
	lrwxrwxrwx 1 root root      74 Mar  9  2018 j7-main-r5f1_0-fw-sec -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_mcu3_0_release_strip.xer5f.signed
	lrwxrwxrwx 1 root root      67 Mar  9  2018 j7-main-r5f1_1-fw -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_mcu3_1_release_strip.xer5f
	lrwxrwxrwx 1 root root      74 Mar  9  2018 j7-main-r5f1_1-fw-sec -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_mcu3_1_release_strip.xer5f.signed
	lrwxrwxrwx 1 root root      67 Mar  9  2018 j7-mcu-r5f0_0-fw -> /lib/firmware/ti-ipc/j721e/ipc_echo_testb_mcu1_0_release_strip.xer5f
	lrwxrwxrwx 1 root root      67 Mar  9  2018 j7-mcu-r5f0_1-fw -> /lib/firmware/ti-ipc/j721e/ipc_echo_test_mcu1_1_release_strip.xer5f

For updating MCU (DM) R5F firmware binary, tispl.bin needs to be recompiled with the new firmware binary as mentioned below :

#. Go to linux installer and replace the existing R5F MCU (DM) firmware binary with the new one

   .. code-block:: console

      host#  cp <path_to_new_fw_binary>/ipc_echo_testb_freertos_mcu1_0_release.xer5f <path_to_linux_installer>/board-support/prebuilt-images/ti-dm/j721e/ipc_echo_testb_mcu1_0_release_strip.xer5f

#. Recompile u-boot to regenerate tispl.bin using the top level makefile.

   .. code-block:: console

      host# make u-boot

   Please refer to :ref:`top-level-makefile` for more details on Top Level makefile.

#. Replace the updated tispl.bin containing new R5F firmware binary in the boot partition of sdcard and reboot

   .. code-block:: console

      host# sudo cp board-support/u-boot_build/A72/tispl.bin  /media/$USER/boot

.. _booting_remote_cores_from_Linux_console:

Booting Remote Cores from Linux console/User space
--------------------------------------------------

To reload a remote core with new executables, please follow the below steps.

First, identify the remotproc node associated with the remote core:

.. code-block:: console

	root@j721e-evm:~# head /sys/class/remoteproc/remoteproc*/name
	==> /sys/class/remoteproc/remoteproc0/name <==
	4d80800000.dsp

	==> /sys/class/remoteproc/remoteproc1/name <==
	4d81800000.dsp

	==> /sys/class/remoteproc/remoteproc10/name <==
	b00c000.txpru

	==> /sys/class/remoteproc/remoteproc11/name <==
	b134000.pru

	==> /sys/class/remoteproc/remoteproc12/name <==
	b104000.rtu

	==> /sys/class/remoteproc/remoteproc13/name <==
	5d00000.r5f

	==> /sys/class/remoteproc/remoteproc14/name <==
	b10a000.txpru

	==> /sys/class/remoteproc/remoteproc15/name <==
	b138000.pru

	==> /sys/class/remoteproc/remoteproc16/name <==
	b106000.rtu

	==> /sys/class/remoteproc/remoteproc17/name <==
	b10c000.txpru

	==> /sys/class/remoteproc/remoteproc18/name <==
	5e00000.r5f

	==> /sys/class/remoteproc/remoteproc19/name <==
	5f00000.r5f

	==> /sys/class/remoteproc/remoteproc2/name <==
	64800000.dsp

	==> /sys/class/remoteproc/remoteproc3/name <==
	41000000.r5f

	==> /sys/class/remoteproc/remoteproc4/name <==
	5c00000.r5f

	==> /sys/class/remoteproc/remoteproc5/name <==
	b034000.pru

	==> /sys/class/remoteproc/remoteproc6/name <==
	b004000.rtu

	==> /sys/class/remoteproc/remoteproc7/name <==
	b00a000.txpru

	==> /sys/class/remoteproc/remoteproc8/name <==
	b038000.pru

	==> /sys/class/remoteproc/remoteproc9/name <==
	b006000.rtu

Then, use the sysfs interface to stop the remote core. For example, to stop the Main R5F0

.. code-block:: console

	root@j721e-evm:~# echo stop > /sys/class/remoteproc/remoteproc4/state
	[  277.626160] remoteproc remoteproc4: stopped remote processor 5c00000.r5f

If needed, update the firmware symbolic link to point to a new firmware:

.. code-block:: console

	root@j721e-evm:/lib/firmware# ln -sf /lib/firmware/ti-ipc/j721e/ipc_echo_test_mcu2_1_release_strip.xer5f j7-main-r5f0_1-fw

Finally, use the sysfs interface to start the remote core:

.. code-block:: console

	root@j721e-evm:~# echo start > /sys/class/remoteproc/remoteproc4/state
	[  311.633427] remoteproc remoteproc4: powering up 5c00000.r5f
	[  311.639692] remoteproc remoteproc4: Booting fw image j7-main-r5f0_0-fw, size 691508
	[  311.655007] rproc-virtio rproc-virtio.16.auto: assigned reserved memory node r5f-dma-memory@a2000000
	[  311.664718] virtio_rpmsg_bus virtio4: rpmsg host is online
	[  311.672389] rproc-virtio rproc-virtio.16.auto: registered virtio4 (type 7)
	[  311.680397] remoteproc remoteproc4: remote processor 5c00000.r5f is now up

.. note::

   The above process is for the gracful remote core shutdown and start. In some cases, graceful
   shutdown may not work. In such cases, it is recommended to put new firmwares in /lib/firmware
   location and do a reboot.

DMA memory Carveouts
--------------------

System memory is carved out for each remote processor core for IPC and for the
remote processor's code/data section needs. The default
memory carveouts (DMA pools) are shown below.

See the devicetree bindings documentation for more details:
:ti-linux-kernel-binding:`remoteproc/ti,k3-r5f-rproc.yaml`

.. code-block:: text

	+------------------+--------------------+---------+----------------------------+
	| Memory Section   | Physical Address   | Size    | Description                |
	+==================+====================+=========+============================+
	| C6x Pool         | 0xa6000000         | 1MB     | IPC (Virtio/Vring buffers) |
	+------------------+--------------------+---------+----------------------------+
	| C6x Pool         | 0xa6100000         | 15MB    | C6x externel code/data mem |
	+------------------+--------------------+---------+----------------------------+
	| C6x Pool         | 0xa7000000         | 1MB     | IPC (Virtio/Vring buffers) |
	+------------------+--------------------+---------+----------------------------+
	| C6x Pool         | 0xa7100000         | 15MB    | C6x externel code/data mem |
	+------------------+--------------------+---------+----------------------------+
	| C7x Pool         | 0xa8000000         | 1MB     | IPC (Virtio/Vring buffers) |
	+------------------+--------------------+---------+----------------------------+
	| C7x Pool         | 0xa8100000         | 15MB    | C7x externel code/data mem |
	+------------------+--------------------+---------+----------------------------+
	| R5F(mcu) Pool    | 0xa0000000         | 1MB     | IPC (Virtio/Vring buffers) |
	+------------------+--------------------+---------+----------------------------+
	| R5F(mcu) Pool    | 0xa0100000         | 15MB    | R5F externel code/data mem |
	+------------------+--------------------+---------+----------------------------+
	| R5F(mcu) Pool    | 0xa1000000         | 1MB     | IPC (Virtio/Vring buffers) |
	+------------------+--------------------+---------+----------------------------+
	| R5F(mcu) Pool    | 0xa1100000         | 15MB    | R5F externel code/data mem |
	+------------------+--------------------+---------+----------------------------+
	| R5F(main) Pool   | 0xa2000000         | 1MB     | IPC (Virtio/Vring buffers) |
	+------------------+--------------------+---------+----------------------------+
	| R5F(main) Pool   | 0xa2100000         | 15MB    | R5F externel code/data mem |
	+------------------+--------------------+---------+----------------------------+
	| R5F(main) Pool   | 0xa3000000         | 1MB     | IPC (Virtio/Vring buffers) |
	+------------------+--------------------+---------+----------------------------+
	| R5F(main) Pool   | 0xa3100000         | 15MB    | R5F externel code/data mem |
	+------------------+--------------------+---------+----------------------------+
	| R5F(main) Pool   | 0xa4000000         | 1MB     | IPC (Virtio/Vring buffers) |
	+------------------+--------------------+---------+----------------------------+
	| R5F(main) Pool   | 0xa4100000         | 15MB    | R5F externel code/data mem |
	+------------------+--------------------+---------+----------------------------+
	| R5F(main) Pool   | 0xa5000000         | 1MB     | IPC (Virtio/Vring buffers) |
	+------------------+--------------------+---------+----------------------------+
	| R5F(main) Pool   | 0xa5100000         | 15MB    | R5F externel code/data mem |
	+------------------+--------------------+---------+----------------------------+

.. code-block:: console

	root@j721e-evm:~# dmesg | grep Reserved
	[    0.000000] Reserved memory: created CMA memory pool at 0x00000008e0000000, size 512 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a0000000, size 1 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a0100000, size 15 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a1000000, size 1 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a1100000, size 15 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a2000000, size 1 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a2100000, size 15 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a3000000, size 1 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a3100000, size 15 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a4000000, size 1 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a4100000, size 15 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a5000000, size 1 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a5100000, size 15 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a6000000, size 1 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a6100000, size 15 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a7000000, size 1 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a7100000, size 15 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a8000000, size 1 MiB
	[    0.000000] Reserved memory: created DMA memory pool at 0x00000000a8100000, size 15 MiB

.. note:: The reserved memory sizes listed above are provided as a reference only and subject to change between releases. For latest memory reservations, please refer to the kernel device tree repository :
          https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-j721e-som-p0.dtsi?h=ti-linux-6.6.y

By default the first 1MB of each pool is used for the Virtio and Vring buffers
used to communicate with the remote processor core. The remaining carveout is
used for the remote core external memory (program code, data, etc).

.. note::
    The resource table entity (which describes the system resources needed by
    the remote processor) needs to be at the beginning of the remote processor
    external memory section.


Sizes and locations for DMA memory carveouts might be updated, e.g. when custom
firmware are used. For details on how to adjust the sizes and locations of the
remote core pool carveouts, please see section :ref:`changing_the_memory_map`.

.. _changing_the_memory_map:

Changing the Memory Map
---------------------------

The address and size of the DMA memory carveouts needs to match with the MCU
M4F and R5F external memory section sizes in their respective linker mapfiles.

arch/arm64/boot/dts/ti/k3-j721e-som-p0.dtsi

.. code-block:: text

	reserved_memory: reserved-memory {
		#address-cells = <2>;
		#size-cells = <2>;
		ranges;

		 /* global cma region */
		linux,cma {
			compatible = "shared-dma-pool";
			reusable;
			size = <0x00 0x20000000>;
			linux,cma-default;
		};

		secure_ddr: optee@9e800000 {
			reg = <0x00 0x9e800000 0x00 0x01800000>;
			alignment = <0x1000>;
			no-map;
		};

		mcu_r5fss0_core0_dma_memory_region: r5f-dma-memory@a0000000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa0000000 0x00 0x100000>;
			no-map;
		};

		mcu_r5fss0_core0_memory_region: r5f-memory@a0100000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa0100000 0x00 0xf00000>;
			no-map;
		};

		mcu_r5fss0_core1_dma_memory_region: r5f-dma-memory@a1000000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa1000000 0x00 0x100000>;
			no-map;
		};

		mcu_r5fss0_core1_memory_region: r5f-memory@a1100000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa1100000 0x00 0xf00000>;
			no-map;
		};

		main_r5fss0_core0_dma_memory_region: r5f-dma-memory@a2000000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa2000000 0x00 0x100000>;
			no-map;
		};

		main_r5fss0_core0_memory_region: r5f-memory@a2100000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa2100000 0x00 0xf00000>;
			no-map;
		};

		main_r5fss0_core1_dma_memory_region: r5f-dma-memory@a3000000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa3000000 0x00 0x100000>;
			no-map;
		};

		main_r5fss0_core1_memory_region: r5f-memory@a3100000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa3100000 0x00 0xf00000>;
			no-map;
		};

		main_r5fss1_core0_dma_memory_region: r5f-dma-memory@a4000000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa4000000 0x00 0x100000>;
			no-map;
		};

		main_r5fss1_core0_memory_region: r5f-memory@a4100000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa4100000 0x00 0xf00000>;
			no-map;
		};

		main_r5fss1_core1_dma_memory_region: r5f-dma-memory@a5000000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa5000000 0x00 0x100000>;
			no-map;
		};

		main_r5fss1_core1_memory_region: r5f-memory@a5100000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa5100000 0x00 0xf00000>;
			no-map;
		};

		c66_1_dma_memory_region: c66-dma-memory@a6000000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa6000000 0x00 0x100000>;
			no-map;
		};

		c66_0_memory_region: c66-memory@a6100000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa6100000 0x00 0xf00000>;
			no-map;
		};

		c66_0_dma_memory_region: c66-dma-memory@a7000000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa7000000 0x00 0x100000>;
			no-map;
		};

		c66_1_memory_region: c66-memory@a7100000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa7100000 0x00 0xf00000>;
			no-map;
		};

		c71_0_dma_memory_region: c71-dma-memory@a8000000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa8000000 0x00 0x100000>;
			no-map;
		};

		c71_0_memory_region: c71-memory@a8100000 {
			compatible = "shared-dma-pool";
			reg = <0x00 0xa8100000 0x00 0xf00000>;
			no-map;
		};

		rtos_ipc_memory_region: ipc-memories@aa000000 {
			reg = <0x00 0xaa000000 0x00 0x01c00000>;
			alignment = <0x1000>;
			no-map;
		};
	};


.. warning:: Be careful not to overlap carveouts!

.. note:: The reserved memory sizes listed above are provided as a reference only and subject to change between releases. For latest memory reservations, please refer to the kernel device tree repository :
          https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-j721e-som-p0.dtsi?h=ti-linux-6.6.y

.. include:: Foundational_Components/IPC/_RPMsg_char_driver.rst
