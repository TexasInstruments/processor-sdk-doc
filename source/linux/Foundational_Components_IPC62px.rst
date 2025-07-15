.. _foundational-components-ipc:

IPC for AM62Px
==============

The AM62Px processors have Cortex-R5F subsystems in addition to a Quad core
Cortex-A53 subsystem. Please refer to the AM62Px Technical Reference Manual for details.

This article is geared toward AM62Px users that are running Linux on the Cortex
A53 cores. The goal is to help users understand how to establish IPC communication
with R5F cores.

There are many facets to this task: building, loading, debugging, memory
sharing, etc. This article intends to take incremental steps toward
understanding all of those pieces.

Software Dependencies to Get Started
------------------------------------

Prerequisites

   - Processor SDK Linux for AM62Px |__SDK_DOWNLOAD_URL__|.
   - `Processor SDK MCU+ for AM62Px
     <https://www.ti.com/tool/download/MCU-PLUS-SDK-AM62P>`__

.. note::

   Please be sure that you have the same version number
   for both Processor SDK RTOS and Linux.

Please refer to the MCU+SDK documentation, section "Developer Guides" -> "Understanding
inter-processor communication (IPC)" for IPC architecture and builds.

Typical Boot Flow on AM62Px for ARM Linux users
-----------------------------------------------

AM62Px SOC's have multiple processor cores - Cortex-A53, Cortex-R5F.
The A53 typically runs a HLOS like Linux/Android. The R5F remote cores run No-OS
or RTOS (FreeRTOS etc). In normal operation, the boot loader (U-Boot/SPL) boots
and loads the A53 with the HLOS. The A53 then boots the R5F core.

The wakeup R5F firmware runs device manager software (SciServer) along
with user application.

The wakeup R5F firmware is integrated as part of :file:`tispl.bin` binary
and is started early in the boot process by u-boot R5 SPL right after DDR initialization.


Getting Started with IPC Linux Examples
---------------------------------------

The figure below illustrates how the Remoteproc/RPMsg driver from the ARM Linux
kernel communicates with the IPC driver on a remote processors (e.g. R5F)
running RTOS.

.. Image:: /images/LinuxIPC_with_RTOS_Slave.png

In order to setup IPC on remote cores, we provide some pre-built examples
in the SDK package that can be run from ARM Linux.

The remoteproc driver is hard-coded to look for specific files when
loading the R5F core. Here are the files it looks for on an AM62Px device:

   +-----------+-----------------+----------------------+-----------------------------+
   | Core Name | RemoteProc Name | Description          | Firmware File Name          |
   +===========+=================+======================+=============================+
   | R5F       | 79000000.r5f    | R5F core(MCU domain) | :file:`am62p-mcu-r5f0_0-fw` |
   +-----------+-----------------+----------------------+-----------------------------+

Generally on a target file system the above files are soft linked to the
intended executable FW files:

.. code-block:: console

   root@am62pxx-evm:~# ls -l /lib/firmware/
   lrwxrwxrwx 1 root root      41 Dec  2  2023 am62p-mcu-r5f0_0-fw -> /usr/lib/firmware/ti-ipc/am62xx/ipc_echo_test_mcu2_0_release_strip.xer5f

For updating wakeup (DM) R5F firmware binary, tispl.bin needs to be recompiled with the new firmware binary as mentioned below :

   #. Go to linux installer and replace the existing R5F wakeup (DM) firmware binary with the new one

      .. code-block:: console

         host#  cp <path_to_new_fw_binary>/ipc_echo_testb_freertos_mcu1_0_release.xer5f <path_to_linux_installer>/board-support/prebuilt-images/ipc_echo_testb_mcu1_0_release_strip.xer5f

   #. Recompile u-boot to regenerate tispl.bin using the top level makefile.

      .. code-block:: console

         host# make u-boot

      Please refer to :ref:`Top-Level Makefile <top-level-makefile>` for more details on Top Level makefile.

   #. Replace the updated tispl.bin containing new R5F firmware binary in the boot partition of sdcard and reboot

      .. code-block:: console

         host# sudo cp board-support/u-boot_build/a53/tispl.bin  /media/$USER/boot

.. _booting_remote_cores_from_Linux_console:

Booting Remote Cores from Linux console/User space
--------------------------------------------------

To reload a remote core with new executables, please follow the below steps.

First, identify the remotproc node associated with the remote core:

.. code-block:: console

   root@am62pxx-evm:~# head /sys/class/remoteproc/remoteproc*/name
   ==> /sys/class/remoteproc/remoteproc0/name <==
   79000000.r5f

   ==> /sys/class/remoteproc/remoteproc1/name <==
   78000000.r5f

Then, use the sysfs interface to stop the remote core. For example, to stop the R5F

.. code-block:: console

   root@am62pxx-evm:~# echo stop > /sys/class/remoteproc/remoteproc0/state
   [   61.497327] remoteproc remoteproc0: stopped remote processor 79000000.r5f

If needed, update the firmware symbolic link to point to a new firmware:

.. code-block:: console

   root@am62pxx-evm:/lib/firmware# ln -sf /lib/firmware/ti-ipc/am62pxx/ipc_echo_test_mcu2_0_release_strip.xer5f am62p-mcu-r5f0_0-fw

Finally, use the sysfs interface to start the remote core:

.. code-block:: console

   root@am62pxx-evm:~# echo start > /sys/class/remoteproc/remoteproc0/state
   [ 1406.013847] remoteproc remoteproc0: powering up 79000000.r5f
   [ 1406.020167] remoteproc remoteproc0: Booting fw image am62p-mcu-r5f0_0-fw, size 55272
   [ 1406.031012] rproc-virtio rproc-virtio.0.auto: assigned reserved memory node mcu-r5fss-dma-memory-region@9b800000
   [ 1406.042534] virtio_rpmsg_bus virtio0: rpmsg host is online
   [ 1406.048152] virtio_rpmsg_bus virtio0: creating channel ti.ipc4.ping-pong addr 0xd
   [ 1406.048836] rproc-virtio rproc-virtio.0.auto: registered virtio0 (type 7)
   [ 1406.055857] virtio_rpmsg_bus virtio0: creating channel rpmsg_chrdev addr 0xe
   [ 1406.063759] remoteproc remoteproc0: remote processor 79000000.r5f is now up

.. note::

   The RemoteProc driver does not support a graceful shutdown of R5 and DSP cores
   in the current Linux Processor SDK. For now, it is recommended to reboot the
   board when loading new binaries into an R5F or DSP core.

DMA memory Carveouts
--------------------

System memory is carved out for each remote processor core for IPC and for the
remote processor's code/data section needs. The default
memory carveouts (DMA pools) are shown below.

See the devicetree bindings documentation for more details:
:ti-linux-kernel-binding:`remoteproc/ti,k3-r5f-rproc.yaml`

   +------------------+--------------------+---------+----------------------------+
   | Memory Section   | Physical Address   | Size    | Description                |
   +==================+====================+=========+============================+
   | R5F(mcu) Pool    | 0x9b800000         | 1MB     | IPC (Virtio/Vring buffers) |
   +------------------+--------------------+---------+----------------------------+
   | R5F(mcu) Pool    | 0x9b900000         | 15MB    | R5F externel code/data mem |
   +------------------+--------------------+---------+----------------------------+
   | R5F(wkup) Pool   | 0x9c800000         | 1MB     | IPC (Virtio/Vring buffers) |
   +------------------+--------------------+---------+----------------------------+
   | R5F(wkup) Pool   | 0x9c900000         | 30MB    | R5F externel code/data mem |
   +------------------+--------------------+---------+----------------------------+

.. code-block:: console

   root@am62pxx-evm:~# dmesg | grep reserved
   [    0.000000] OF: reserved mem: initialized node linux,cma, compatible id shared-dma-pool
   [    0.000000] OF: reserved mem: initialized node rtos-ipc-memory@9b500000, compatible id shared-dma-pool
   [    0.000000] OF: reserved mem: initialized node mcu-r5fss-dma-memory-region@9b 800000, compatible id shared-dma-pool
   [    0.000000] OF: reserved mem: initialized node mcu-r5fss-memory-region@9b900000, compatible id shared-dma-pool
   [    0.000000] OF: reserved mem: initialized node r5f-dma-memory@9c800000, compatible id shared-dma-pool
   [    0.000000] OF: reserved mem: initialized node r5f-memory@9c900000, compatible id shared-dma-pool

.. note::

   The reserved memory sizes listed above are provided as a reference only and
   subject to change between releases. For latest memory reservations, please
   refer to the kernel device tree repository :
   'https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62p5-sk.dts?h=ti-linux-6.12.y'

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

Changing the Memory Map
---------------------------

The address and size of the DMA memory carveouts needs to match with the MCU
M4F and R5F external memory section sizes in their respective linker mapfiles.

:file:`arch/arm64/boot/dts/ti/k3-am62p5-sk.dts`

.. code-block:: dts

   reserved-memory {
      #address-cells = <2>;
      #size-cells = <2>;
      ranges;

      wkup_r5fss0_core0_dma_memory_region: r5f-dma-memory@9c800000 {
         compatible = "shared-dma-pool";
         reg = <0x00 0x9c800000 0x00 0x100000>;
         no-map;
      };

      wkup_r5fss0_core0_memory_region: r5f-dma-memory@9c900000 {
         compatible = "shared-dma-pool";
         reg = <0x00 0x9c900000 0x00 0x01e00000>;
         no-map;
      };

      mcu_r5fss0_core0_dma_memory_region: r5f-dma-memory@9b800000 {
         compatible = "shared-dma-pool";
         reg = <0x00 0x9b800000 0x00 0x100000>;
         no-map;
      };

      mcu_r5fss0_core0_memory_region: r5f-dma-memory@9b900000 {
         compatible = "shared-dma-pool";
         reg = <0x00 0x9b900000 0x00 0x0f00000>;
         no-map;
      };
   };


.. warning::

   Be careful not to overlap carveouts!

.. note::

   The reserved memory sizes listed above are provided as a reference only and
   subject to change between releases. For latest memory reservations, please
   refer to the kernel device tree repository :
   'https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62p5-sk.dts?h=11.00.09'

.. include:: Foundational_Components/IPC/_RPMsg_char_driver.rst
