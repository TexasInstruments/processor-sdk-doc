.. _foundational-components-ipc:

IPC for AM62x
=============

The AM62x processors have Cortex-M4F and Cortex-R5F subsystems in addition to
a Quad core Cortex-A53 subsystem. Please refer to the AM62x Technical Reference Manual for details.

This article is geared toward AM62x users that are running Linux on the Cortex
A53 cores. The goal is to help users understand how to establish IPC communication
with the M4F and R5F cores.

There are many facets to this task: building, loading, debugging, memory
sharing, etc. This article intends to take incremental steps toward
understanding all of those pieces.

Software Dependencies to Get Started
------------------------------------

Prerequisites

-  Processor SDK Linux for AM62x |__SDK_DOWNLOAD_URL__|.
-  `Processor SDK MCU+ for
   AM62x <https://www.ti.com/tool/download/MCU-PLUS-SDK-AM62X>`__

.. attention::

   Please be sure that you have the same version number
   for both Processor SDK RTOS and Linux.

Please refer to `Understanding inter-processor communication (IPC) <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62X/latest/exports/docs/api_guide_am62x/IPC_GUIDE.html>`__ section from MCU+ SDK documentation for M4F IPC architecture and builds.

Typical Boot Flow on AM62x for ARM Linux users
----------------------------------------------

AM62x SOC's have multiple processor cores - Cortex-A53, Cortex-R5F and Cortex-M4F ARM cores.
The A53 typically runs a HLOS like Linux/Android. The M4F and R5F remote cores run No-OS
or RTOS (FreeRTOS etc). In normal operation, the boot loader (U-Boot/SPL) boots
and loads the A53 with the HLOS. The A53 then boots the M4F core.

The R5F firmware runs device manager software (SciServer) along
with a demo IPC application.

Unlike M4F firmware, The R5F firmware is integrated as part of :file:`tispl.bin` binary
and is started early in the boot process by u-boot R5 SPL right after DDR initialization.


Getting Started with IPC Linux Examples
---------------------------------------

The figure below illustrates how the Remoteproc/RPMsg driver from the ARM Linux
kernel communicates with the IPC driver on a remote processor (e.g. M4F)
running RTOS.

.. Image:: /images/LinuxIPC_with_RTOS_Slave.png

In order to setup IPC on remote cores, we provide some pre-built examples
in the SDK package that can be run from ARM Linux.

The remoteproc driver is hard-coded to look for specific files when
loading the M4F core. Here are the files it looks for on an AM62x device:

   +------------------+-----------------+--------------------+----------------------+
   | Core Name        | RemoteProc Name | Description        | Firmware File Name   |
   +==================+=================+====================+======================+
   | M4F              | 5000000.m4f     | M4F core           | am62-mcu-m4f0_0-fw   |
   +------------------+-----------------+--------------------+----------------------+

Generally on a target file system the above files are soft linked to the
intended executable FW files:

.. code-block:: console

   root@am62xx-evm:/opt/ltp# ls -l /lib/firmware
   lrwxrwxrwx 1 root root      72 Mar  9  2018 am62-mcu-m4f0_0-fw -> /usr/lib/firmware/ti-ipc/am62xx/ipc_echo_test_mcu2_0_release_strip.xer5f

However, unlike M4F remoteproc driver which boots the M4F, the R5F remoteproc driver doesn't boot the R5F instead it late
attaches to already running R5F firmware binary which is started early in the boot process as mentinoed in previous section.

For updating R5F firmware binary, :file:`tispl.bin` needs to be recompiled with the new firmware binary as mentioned below :

#. Go to linux installer and replace the existing R5F firmware binary with the new one

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

   root@am62xx-evm:~# head /sys/class/remoteproc/remoteproc*/name
   ==> /sys/class/remoteproc/remoteproc0/name <==
   5000000.m4fss

   ==> /sys/class/remoteproc/remoteproc1/name <==
   78000000.r5f

   ==> /sys/class/remoteproc/remoteproc2/name <==
   30074000.pru

   ==> /sys/class/remoteproc/remoteproc3/name <==
   30078000.pru


Then, use the sysfs interface to stop the remote core. For example, to stop the M4F

.. code-block:: console

   root@am62xx-evm:~# echo stop > /sys/class/remoteproc/remoteproc0/state
   [  440.832317] remoteproc remoteproc0: stopped remote processor 5000000.m4fss

If needed, update the firmware symbolic link to point to a new firmware:

.. code-block:: console

   root@am62xx-evm:/lib/firmware# ln -sf /usr/lib/firmware/ti-ipc/am62xx/ipc_echo_test_mcu2_0_release_strip.xer5f am62-mcu-m4f0_0-fw

Finally, use the sysfs interface to start the remote core:

.. code-block:: console

   root@am62xx-evm:~# echo start > /sys/class/remoteproc/remoteproc0/state
   [  450.930070] remoteproc remoteproc0: powering up 5000000.m4fss
   [  450.936112] remoteproc remoteproc0: Booting fw image am62-mcu-m4f0_0-fw, size 78960
   [  450.960447]  remoteproc0#vdev0buffer: assigned reserved memory node m4f-dma-memory@9cb00000
   [  450.969408] virtio_rpmsg_bus virtio0: rpmsg host is online
   [  450.975089] virtio_rpmsg_bus virtio0: creating channel ti.ipc4.ping-pong addr 0xd
   [  450.975850]  remoteproc0#vdev0buffer: registered virtio0 (type 7)
   [  450.982840] virtio_rpmsg_bus virtio0: creating channel rpmsg_chrdev addr 0xe
   [  450.988824] remoteproc remoteproc0: remote processor 5000000.m4fss is now up

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
| M4F Pool         | 0x9cb00000         | 1MB     | IPC (Virtio/Vring buffers) |
+------------------+--------------------+---------+----------------------------+
| M4F Pool         | 0x9cc00000         | 14MB    | M4F externel code/data mem |
+------------------+--------------------+---------+----------------------------+
| R5F Pool         | 0x9da00000         | 1MB     | IPC (Virtio/Vring buffers) |
+------------------+--------------------+---------+----------------------------+
| R5F Pool         | 0x9db00000         | 12MB    | R5F externel code/data mem |
+------------------+--------------------+---------+----------------------------+

.. code-block:: console

   root@am62xx-evm:~# dmesg | grep Reserved
   [    0.000000] Reserved memory: created DMA memory pool at 0x000000009c800000, size 3 MiB
   [    0.000000] Reserved memory: created DMA memory pool at 0x000000009cb00000, size 1 MiB
   [    0.000000] Reserved memory: created DMA memory pool at 0x000000009cc00000, size 14 MiB
   [    0.000000] Reserved memory: created DMA memory pool at 0x000000009da00000, size 1 MiB
   [    0.000000] Reserved memory: created DMA memory pool at 0x000000009db00000, size 12 MiB
   [    0.000000] cma: Reserved 512 MiB at 0x00000000dd000000

.. note:: The reserved memory sizes listed above are provided as a reference only and subject to change between releases. For latest memory reservations, please refer to the kernel device tree repository :
          'https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-common.dtsi?h=ti-linux-6.6.y'

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

:file:`arch/arm64/boot/dts/ti/k3-am62x-sk-common.dtsi`

.. code-block:: dts

   reserved-memory {
      #address-cells = <2>;
      #size-cells = <2>;
      ranges;

      mcu_m4fss_dma_memory_region: m4f-dma-memory@9cb00000 {
         compatible = "shared-dma-pool";
         reg = <0x00 0x9cb00000 0x00 0x100000>;
         no-map;
      };

      mcu_m4fss_memory_region: m4f-memory@9cc00000 {
         compatible = "shared-dma-pool";
         reg = <0x00 0x9cc00000 0x00 0xe00000>;
         no-map;
      };

      wkup_r5fss0_core0_dma_memory_region: r5f-dma-memory@9da00000 {
         compatible = "shared-dma-pool";
         reg = <0x00 0x9da00000 0x00 0x00100000>;
         no-map;
      };

      wkup_r5fss0_core0_memory_region: r5f-memory@9db00000 {
         compatible = "shared-dma-pool";
         reg = <0x00 0x9db00000 0x00 0x00c00000>;
         no-map;
      };
   };

.. warning:: Be careful not to overlap carveouts!

.. note:: The DT fragments are provided as a reference and subject to change between releases. For latest memory reservations, please refer to the kernel device tree repository :
          'https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/arch/arm64/boot/dts/ti/k3-am62x-sk-common.dtsi?h=11.00.09'

.. include:: Foundational_Components/IPC/_RPMsg_char_driver.rst
