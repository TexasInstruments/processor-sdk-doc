.. _foundational-components-ipc:

IPC for J722S
==============

The J722S processors have Cortex-R5F and C7x DSP subsystems in addition to
a dual core Cortex-A53 subsystem.
Please refer to the J722S Technical Reference Manual for details.

This article is geared toward J722S users that are running Linux on the Cortex
A53 cores. The goal is to help users understand how to establish IPC communication
with the C7x DSP and R5F cores.

There are many facets to this task: building, loading, debugging, memory
sharing, etc. This article intends to take incremental steps toward
understanding all of those pieces.

Typical Boot Flow on J722S for ARM Linux users
-----------------------------------------------

J722S SOC's have multiple processor cores - Cortex-A53, Cortex-R5F and DSP cores.

The WKUP R5F firmware runs device manager software (SciServer).
The WKUP R5F firmware (DM) is integrated as part of tispl.bin binary
and is started early in the boot process, right after DDR initialization,
by u-boot SPL running on WKUP R5.

The A53 typically runs a HLOS like Linux/Android. The C7x and R5F remote cores run No-OS
or RTOS (FreeRTOS etc). In normal operation, the boot loader (U-Boot/SPL) boots
and loads the A53 with the HLOS. The A53 then boots the C7x and R5F cores.

Getting Started with IPC Linux Examples
---------------------------------------

The figure below illustrates how the Remoteproc/RPMsg driver from the ARM Linux
kernel communicates with the IPC driver on a remote processors (e.g. R5F)
running RTOS.

.. Image:: /images/LinuxIPC_with_RTOS_Slave.png

In order to setup IPC on remote cores, we provide some pre-built examples
in the SDK package that can be run from ARM Linux.

The remoteproc driver is hard-coded to look for specific files when
loading the R5F and C7x cores. Here are the files it looks for on an J722S device:

.. code-block:: text

   +------------------+-----------------+----------------------+-----------------------+
   | Core Name        | RemoteProc Name | Description          | Firmware File Name    |
   +==================+=================+======================+=======================+
   | C7x              | 7e000000.c7x    | C7x core             | j722s-c71_0-fw        |
   +------------------+-----------------+----------------------+-----------------------+
   | C7x              | 7e200000.c7x    | C7x core             | j722s-c71_1-fw        |
   +------------------+-----------------+----------------------+-----------------------+
   | R5F              | 79000000.r5f    | R5F core(MCU domain) | j722s-mcu-r5f0_0-fw   |
   +------------------+-----------------+----------------------+-----------------------+
   | R5F              | 78400000.r5f    | R5F core(MAIN domain)| j722s-main-r5f0_0-fw  |
   +------------------+-----------------+----------------------+-----------------------+

Generally on a target file system the above files are soft linked to the
intended executable FW files:

.. code-block:: console

   root@j722s-evm::~# ls -l /lib/firmware/
   lrwxrwxrwx  1 root root      72 Dec  7 15:36 j722s-main-r5f0_0-fw -> /lib/firmware/ti-ipc/j722s/ipc_echo_test_mcu3_0_release_strip.xer5f
   lrwxrwxrwx  1 root root      67 Dec  7 15:37 j722s-mcu-r5f0_0-fw -> /lib/firmware/ti-ipc/j722s/ipc_echo_test_mcu2_0_release_strip.xer5f
   lrwxrwxrwx  1 root root      65 Dec  7 15:39 j722s-c71_0-fw -> /lib/firmware/ti-ipc/j722s/ipc_echo_test_c7x_1_release_strip.xe71
   lrwxrwxrwx  1 root root      65 Dec  7 15:40 j722s-c71_1-fw -> /lib/firmware/ti-ipc/j722s/ipc_echo_test_c7x_2_release_strip.xe71

For updating MCU (DM) R5F firmware binary, tispl.bin needs to be recompiled with the new firmware binary as mentioned below :

#. Go to linux installer and replace the existing R5F MCU (DM) firmware binary with the new one

   .. code-block:: console

      host#  cp <path_to_new_fw_binary>/ipc_echo_testb_freertos_mcu1_0_release.xer5f <path_to_linux_installer>/board-support/prebuilt-images/ti-dm/j722s/ipc_echo_testb_mcu1_0_release_strip.xer5f

#. Recompile u-boot to regenerate tispl.bin using the top level makefile.

   .. code-block:: console

      host# make u-boot

   Please refer to :ref:`top-level-makefile` for more details on Top Level makefile.

#. Replace the updated tispl.bin containing new R5F firmware binary in the boot partition of sdcard and reboot

   .. code-block:: console

      host# sudo cp board-support/u-boot_build/A53/tispl.bin  /media/$USER/boot

.. _booting_remote_cores_from_Linux_console:

Booting Remote Cores from Linux console/User space
--------------------------------------------------

To reload a remote core with new executables, please follow the below steps.

First, identify the remotproc node associated with the remote core:

.. code-block:: console

   root@j722s-evm:~# head /sys/class/remoteproc/remoteproc*/name
   ==> /sys/class/remoteproc/remoteproc0/name <==
   7e000000.dsp

   ==> /sys/class/remoteproc/remoteproc1/name <==
   7e200000.dsp

   ==> /sys/class/remoteproc/remoteproc2/name <==
   79000000.r5f

   ==> /sys/class/remoteproc/remoteproc3/name <==
   78000000.r5f

   ==> /sys/class/remoteproc/remoteproc4/name <==
   78400000.r5f

Then, use the sysfs interface to stop the remote core. For example, to stop the R5F

.. code-block:: console

   root@j722s-evm:~# echo stop > /sys/class/remoteproc/remoteproc4/state
   [ 1920.592397] remoteproc remoteproc4: stopped remote processor 78400000.r5f

If needed, update the firmware symbolic link to point to a new firmware:

.. code-block:: console

   root@j722s-evm:/lib/firmware# ln -sf /lib/firmware/ti-ipc/j722s/ipc_echo_test_mcu3_0_release_strip.xer5f j722s-main-r5f0_0-fw

Finally, use the sysfs interface to start the remote core:

.. code-block:: console

   root@j722s-evm:~# echo start > /sys/class/remoteproc/remoteproc4/state
   [ 1928.127331] remoteproc remoteproc4: powering up 78400000.r5f
   [ 1928.133194] remoteproc remoteproc4: Booting fw image j722s-main-r5f0_0-fw, size 45492
   [ 1928.142021] rproc-virtio rproc-virtio.6.auto: assigned reserved memory node main-r5fss-dma-memory-region@a2000000
   [ 1928.153114] virtio_rpmsg_bus virtio4: rpmsg host is online
   [ 1928.153776] virtio_rpmsg_bus virtio4: creating channel ti.ipc4.ping-pong addr 0xd
   [ 1928.158835] rproc-virtio rproc-virtio.6.auto: registered virtio4 (type 7)
   [ 1928.166410] virtio_rpmsg_bus virtio4: creating channel rpmsg_chrdev addr 0xe
   [ 1928.173034] remoteproc remoteproc4: remote processor 78400000.r5f is now up

.. note::

   The above process is for the graceful remote core shutdown and start. In some cases, graceful
   shutdown may not work. In such cases, it is **recommended** to put new firmwares in /lib/firmware
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
   | C7x Pool         | 0xa3000000         | 1MB     | IPC (Virtio/Vring buffers) |
   +------------------+--------------------+---------+----------------------------+
   | C7x Pool         | 0xa3100000         | 15MB    | C7x externel code/data mem |
   +------------------+--------------------+---------+----------------------------+
   | C7x Pool         | 0xa4000000         | 1MB     | IPC (Virtio/Vring buffers) |
   +------------------+--------------------+---------+----------------------------+
   | C7x Pool         | 0xa4100000         | 15MB    | C7x externel code/data mem |
   +------------------+--------------------+---------+----------------------------+


   root@J722S-evm:~# dmesg | grep Reserved
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

.. note:: The reserved memory sizes listed above are provided as a reference only and subject to change between releases. For latest memory reservations, please refer to the kernel device tree repository :
          https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-j722s-evm.dts?h=ti-linux-6.6.y

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

arch/arm64/boot/dts/ti/k3-j722s-evm.dts

.. code-block:: dts

   reserved_memory: reserved-memory {
           #address-cells = <2>;
           #size-cells = <2>;
           ranges;
   
           /* global cma region */
           linux,cma {
                   compatible = "shared-dma-pool";
                   reusable;
                   size = <0x00 0x38000000>;
                   linux,cma-default;
           };
   
           secure_tfa_ddr: tfa@9e780000 {
                   reg = <0x00 0x9e780000 0x00 0x80000>;
                   no-map;
           };
   
           secure_ddr: optee@9e800000 {
                   reg = <0x00 0x9e800000 0x00 0x01800000>;
                   no-map;
           };
   
           wkup_r5fss0_core0_dma_memory_region: r5f-dma-memory@a0000000 {
                   compatible = "shared-dma-pool";
                   reg = <0x00 0xa0000000 0x00 0x100000>;
                   no-map;
           };
   
           wkup_r5fss0_core0_memory_region: r5f-memory@a0100000 {
                   compatible = "shared-dma-pool";
                   reg = <0x00 0xa0100000 0x00 0xf00000>;
                   no-map;
           };
   
           mcu_r5fss0_core0_dma_memory_region: mcu-r5fss-dma-memory-region@a1000000 {
                   compatible = "shared-dma-pool";
                   reg = <0x00 0xa1000000 0x00 0x100000>;
                   no-map;
           };
   
           mcu_r5fss0_core0_memory_region: mcu-r5fss-memory-region@a1100000 {
                   compatible = "shared-dma-pool";
                   reg = <0x00 0xa1100000 0x00 0xf00000>;
                   no-map;
           };
   
           main_r5fss0_core0_dma_memory_region: main-r5fss-dma-memory-region@a2000000 {
                   compatible = "shared-dma-pool";
                   reg = <0x00 0xa2000000 0x00 0x100000>;
                   no-map;
           };
   
           main_r5fss0_core0_memory_region: main-r5fss-memory-region@a2100000 {
                   compatible = "shared-dma-pool";
                   reg = <0x00 0xa2100000 0x00 0xf00000>;
                   no-map;
           };
   
           c7x_0_dma_memory_region: c7x-dma-memory@a3000000 {
                   compatible = "shared-dma-pool";
                   reg = <0x00 0xa3000000 0x00 0x100000>;
                   no-map;
           };
   
           c7x_0_memory_region: c7x-memory@a3100000 {
                   compatible = "shared-dma-pool";
                   reg = <0x00 0xa3100000 0x00 0xf00000>;
                   no-map;
           };
   
           c7x_1_dma_memory_region: c7x-dma-memory@a4000000 {
                   compatible = "shared-dma-pool";
                   reg = <0x00 0xa4000000 0x00 0x100000>;
                   no-map;
           };
   
           c7x_1_memory_region: c7x-memory@a4100000 {
                   compatible = "shared-dma-pool";
                   reg = <0x00 0xa4100000 0x00 0xf00000>;
                   no-map;
           };
   
           rtos_ipc_memory_region: ipc-memories@a5000000 {
                   reg = <0x00 0xa5000000 0x00 0x1c00000>;
                   alignment = <0x1000>;
                   no-map;
           };
   };

.. warning:: Be careful not to overlap carveouts!

.. note:: The reserved memory sizes listed above are provided as a reference only and subject to change between releases. For latest memory reservations, please refer to the kernel device tree repository :
          https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-j722s-evm.dts?h=ti-linux-6.6.y

.. include:: Foundational_Components/IPC/_RPMsg_char_driver.rst
