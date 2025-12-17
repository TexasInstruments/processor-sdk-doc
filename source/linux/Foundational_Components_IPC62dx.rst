.. _foundational-components-ipc:

##############
IPC for AM62Dx
##############

The AM62Dx processors have Cortex-R5F and C7x DSP subsystems in addition to
a Quad core Cortex-A53 subsystem. Please refer to the `AM62Dx Technical
Reference Manual <https://www.ti.com/lit/pdf/sprujd4>`__ for
details.

This article is geared toward AM62Dx users that are running Linux on the Cortex
A53 cores. The goal is to help users understand how to establish IPC communication
with the C7x DSP and R5F cores.

There are many facets to this task: building, loading, debugging, memory
sharing, etc. This article intends to take incremental steps toward
understanding all of those pieces.

************************************
Software Dependencies to Get Started
************************************

Prerequisites

-  Processor SDK Linux for AM62Dx |__SDK_DOWNLOAD_URL__|.
-  Processor SDK MCU+ for AM62D refer `doc <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/11_02_00_20/exports/docs/api_guide_am62dx/index.html>`__

.. note::

   Please be sure that you have the same version number
   for both Processor SDK RTOS and Linux.

Please refer to the MCU+SDK documentation, section "Developer Guides" -> "Understanding
inter-processor communication (IPC)" for IPC architecture and builds.

***********************************************
Typical Boot Flow on AM62Dx for ARM Linux users
***********************************************

AM62Dx SOC's have multiple processor cores - Cortex-A53, Cortex-R5F and DSP cores.
The A53 typically runs a HLOS like Linux/Android. The C7x and R5F remote cores run No-OS
or RTOS (FreeRTOS etc). In normal operation, the boot loader (U-Boot/SPL) boots
and loads the A53 with the HLOS. The A53 then boots the C7x and R5F cores.

The wakeup R5F firmware runs device manager software (SciServer) along
with vision apps application.

The wakeup R5F firmware is integrated as part of :file:`tispl.bin` binary
and is started early in the boot process by u-boot R5 SPL right after DDR initialization.

***************************************
Getting Started with IPC Linux Examples
***************************************

The figure below illustrates how the Remoteproc/RPMsg driver from the ARM Linux
kernel communicates with the IPC driver on a remote processors (e.g. R5F)
running RTOS.

.. Image:: /images/LinuxIPC_with_RTOS_Slave.png

In order to setup IPC on remote cores, we provide some pre-built examples
in the SDK package that can be run from ARM Linux.

The remoteproc driver is hard-coded to look for specific files when
loading the R5F and C7x cores. Here are the files it looks for on an AM62dx device:

+------------------+-----------------+----------------------+----------------------+
| Core Name        | RemoteProc Name | Description          | Firmware File Name   |
+==================+=================+======================+======================+
| C7x              | 7e000000.c7x    | C7x core             | am62d-c71_0-fw       |
+------------------+-----------------+----------------------+----------------------+
| R5F	           | 79000000.r5f    | R5F core(MCU domain) | am62d-mcu-r5f0_0-fw  |
+------------------+-----------------+----------------------+----------------------+

Generally on a target file system the above files are soft linked to the
intended executable FW files:

.. code-block:: console

   root@am62dxx-evm:~# ls -l /lib/firmware/
   lrwxrwxrwx 1 root root      71 Mar  9  2018 am62d-c71_0-fw -> /usr/lib/firmware/ti-ipc/am62dxx/ipc_echo_test_c7x_1_release_strip.xe71
   lrwxrwxrwx 1 root root      73 Mar  9  2018 am62d-mcu-r5f0_0-fw -> /usr/lib/firmware/ti-ipc/am62dxx/ipc_echo_test_mcu2_0_release_strip.xer5f

For updating wakeup (DM) R5F firmware binary, :file:`tispl.bin` needs to be recompiled with the new firmware binary as mentioned below :

#. Go to linux installer and replace the existing R5F wakeup (DM) firmware binary with the new one

.. code-block:: console

   host#  cp <path_to_new_fw_binary>/ipc_echo_testb_freertos_mcu1_0_release.xer5f <path_to_linux_installer>/board-support/prebuilt-images/am62dxx-evm/ti-dm/am62dxx/ipc_echo_testb_mcu1_0_release_strip.xer5f

#. Recompile u-boot to regenerate :file:`tispl.bin` using the top level makefile.

.. code-block:: console

   host# make u-boot

Please refer to :ref:`Top-Level Makefile <top-level-makefile>` for more details on Top Level makefile.

#. Replace the updated :file:`tispl.bin` containing new R5F firmware binary in the boot partition of sdcard and reboot

.. code-block:: console

   host# sudo cp board-support/u-boot_build/a53/tispl.bin /media/$USER/boot

.. _booting_remote_cores_from_Linux_console:

**************************************************
Booting Remote Cores from Linux console/User space
**************************************************

To reload a remote core with new executables, please follow the below steps.

First, identify the remotproc node associated with the remote core:

.. code-block:: console

   root@am62dxx-evm:~# head /sys/class/remoteproc/remoteproc*/name
   ==> /sys/class/remoteproc/remoteproc0/name <==
   7e000000.dsp

   ==> /sys/class/remoteproc/remoteproc1/name <==
   79000000.r5f

   ==> /sys/class/remoteproc/remoteproc2/name <==
   78000000.r5f

Then, use the sysfs interface to stop the remote core. For example, to stop the C7x

.. code-block:: console

   root@am62dxx-evm:~# echo stop > /sys/class/remoteproc/remoteproc0/state
   [   61.497327] remoteproc remoteproc0: stopped remote processor 7e000000.dsp

If needed, update the firmware symbolic link to point to a new firmware:

.. code-block:: console

   root@am62dxx-evm:/lib/firmware# ln -sf /lib/firmware/ti-ipc/am62dxx/ipc_echo_test_c7x_1_release_strip.xe71 am62d-c71_0-fw

Finally, use the sysfs interface to start the remote core:

.. code-block:: console

   root@am62axx-evm:~# echo start > /sys/class/remoteproc/remoteproc0/state
   [ 1917.868689] remoteproc remoteproc0: powering up 7e000000.dsp
   [ 1917.879917] remoteproc remoteproc0: Booting fw image am62d-c71_0-fw, size 8392040
   [ 1917.887904] rproc-virtio rproc-virtio.5.auto: assigned reserved memory node c7x-dma-memory@99800000
   [ 1917.889728] virtio_rpmsg_bus virtio0: rpmsg host is online
   [ 1917.889772] rproc-virtio rproc-virtio.5.auto: registered virtio0 (type 7)
   [ 1917.889779] remoteproc remoteproc0: remote processor 7e000000.dsp is now up
   [ 1917.902247] virtio_rpmsg_bus virtio0: creating channel rpmsg-client-sample addr 0xd
   [ 1917.902541] virtio_rpmsg_bus virtio0: creating channel rpmsg_chrdev addr 0xe

.. note::

   The RemoteProc driver does not support a graceful shutdown of R5 and DSP cores
   in the current Linux Processor SDK. For now, it is recommended to reboot the
   board when loading new binaries into an R5F or DSP core.

********************
DMA memory Carveouts
********************

System memory is carved out for each remote processor core for IPC and for the
remote processor's code/data section needs. The default
memory carveouts (DMA pools) are shown below.

See the devicetree bindings documentation for more details: `Documentation/devicetree/bindings/remoteproc/ti,k3-r5f-rproc.yaml <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/Documentation/devicetree/bindings/remoteproc/ti,k3-r5f-rproc.yaml?h=ti-linux-6.12.y>`__

+------------------+--------------------+---------+----------------------------+
| Memory Section   | Physical Address   | Size    | Description                |
+==================+====================+=========+============================+
| C7x Pool         | 0x99800000         | 1MB     | IPC (Virtio/Vring buffers) |
+------------------+--------------------+---------+----------------------------+
| C7x Pool         | 0x99900000         | 15MB    | C7x externel code/data mem |
+------------------+--------------------+---------+----------------------------+
| R5F(MCU) Pool    | 0x9b800000         | 1MB     | IPC (Virtio/Vring buffers) |
+------------------+--------------------+---------+----------------------------+
| R5F(MCU) Pool    | 0x9b900000         | 15MB    | R5F externel code/data mem |
+------------------+--------------------+---------+----------------------------+
| R5F(WKUP) Pool   | 0x9c800000         | 1MB     | IPC (Virtio/Vring buffers) |
+------------------+--------------------+---------+----------------------------+
| R5F(WKUP) Pool   | 0x9c900000         | 15MB    | R5F externel code/data mem |
+------------------+--------------------+---------+----------------------------+

.. code-block:: console

   root@am62dxx-evm:/lib/firmware# dmesg | grep Reserved
   [    0.000000] Reserved memory: created CMA memory pool at 0x00000000c0000000, size 32 MiB
   [    0.000000] Reserved memory: created DMA memory pool at 0x0000000099800000, size 1 MiB
   [    0.000000] Reserved memory: created DMA memory pool at 0x0000000099900000, size 15 MiB
   [    0.000000] Reserved memory: created DMA memory pool at 0x000000009b800000, size 1 MiB
   [    0.000000] Reserved memory: created DMA memory pool at 0x000000009b900000, size 15 MiB
   [    0.000000] Reserved memory: created DMA memory pool at 0x000000009c800000, size 1 MiB
   [    0.000000] Reserved memory: created DMA memory pool at 0x000000009c900000, size 15 MiB
   [    0.000000] Reserved memory: created DMA memory pool at 0x00000000a0000000, size 16 MiB

.. note::

   The reserved memory sizes listed above are provided as a reference only
   and subject to change between releases. For latest memory reservations,
   please refer to the kernel `device tree repository
   <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62d2-evm.dts?h=ti-linux-6.12.y>`__.

By default the first 1MB of each pool is used for the Virtio and Vring buffers
used to communicate with the remote processor core. The remaining carveout is
used for the remote core external memory (program code, data, etc).

.. note::

   The resource table entity (which describes the system resources needed by
   the remote processor) needs to be at the beginning of the remote processor
   external memory section.

For details on how to adjust the sizes and locations of the remote core pool
carveouts, please see section :ref:`changing_the_memory_map`.

.. _changing_the_memory_map:

***********************
Changing the Memory Map
***********************

The address and size of the DMA memory carveouts needs to match with the MCU
M4F and R5F external memory section sizes in their respective linker mapfiles.

:file:`arch/arm64/boot/dts/ti/k3-am62d2-evm.dts`

.. code-block:: text

   reserved-memory {
       #address-cells = <2>;
       #size-cells = <2>;
       ranges;

       c7x_0_dma_memory_region: c7x-dma-memory@99800000 {
           compatible = "shared-dma-pool";
           reg = <0x00 0x99800000 0x00 0x100000>;
           no-map;
       };

       c7x_0_memory_region: c7x-memory@99900000 {
           compatible = "shared-dma-pool";
           reg = <0x00 0x99900000 0x00 0xf00000>;
           no-map;
       };

       mcu_r5fss0_core0_dma_memory_region: r5f-dma-memory@9b800000 {
           compatible = "shared-dma-pool";
           reg = <0x00 0x9b800000 0x00 0x100000>;
           no-map;
       };

       mcu_r5fss0_core0_memory_region: r5f-dma-memory@9b900000 {
           compatible = "shared-dma-pool";
           reg = <0x00 0x9b900000 0x00 0xf00000>;
           no-map;
       };

       wkup_r5fss0_core0_dma_memory_region: r5f-dma-memory@9c800000 {
           compatible = "shared-dma-pool";
           reg = <0x00 0x9c800000 0x00 0x100000>;
           no-map;
       };

       wkup_r5fss0_core0_memory_region: r5f-dma-memory@9c900000 {
           compatible = "shared-dma-pool";
           reg = <0x00 0x9c900000 0x00 0xf00000>;
           no-map;
           bootph-pre-ram;
       };
   };

.. warning::

   Be careful not to overlap carveouts!

.. note::

   The reserved memory sizes listed above are provided as a reference only
   and subject to change between releases. For latest memory reservations,
   please refer to the kernel `device tree repository
   <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62d2-evm.dts?h=ti-linux-6.12.y>`__.

.. include:: Foundational_Components/IPC/_RPMsg_char_driver.rst
