.. http://processors.wiki.ti.com/index.php/Processor_SDK_Big_Data_IPC_Examples

Introduction
============

High Performance Computing applications and other Data intensive
applications often require passing of Big data buffers between the
multi-core processors in an SOC.

The Big Data IPC examples are created mainly to show exchange of big
data buffers between cores and is part of the Processor SDK RTOS
package.

Currently the example named "simple_buffer_example", captures the
details of exchange of big buffers with both host A15 core and a DSP
cores.

Architecture Overview
=====================

The following block diagram shows the various functional blocks used in
the example on the cores running TI-RTOS/BIOS.

.. Image:: /images/Big_Data_IPC_RTOS_Software_blocks.png

For the small message IPC, sharedRegion and Heap, the modules in the
Standard TI IPC package are used.

The BigDataXlat module, which is part of the example code, provides a
high level abstraction to take care of Address translation and Cache
sync on the big data buffers.

Simple Buffer example: Program Sequence
=======================================

This section describes the program sequence captured in the example.

The main aim of the overall program is to show the exchange of big data
buffers. The sequence is described in words here to sort of walk through
the main application code.

Initially, the host sends first message with shared memory init
information followed by two more dummy messages to slave core ( all
three messages sent in sequence without waiting for reply).

The shared memory region init message conveys the details about the
shared memory expected to hold the big data buffers.

Independently, the slave processor receives messages and sends back
reply back for each of the messages to the host.

Then the host receives one message from the slave and sends a message
with Big data buffer allocated from the Big data heap and filled with an
incrementing pattern. (This process is repeated with 10 Big data Buffer
messages). Each of these Messages are received by slave and the values
in the buffers are updated with a modified incrementing pattern and sent
back to the host.

Note the Slave and Host processors checks the expected incrementing
pattern for errors.

At this point only 7 Big data buffer messages would have been received.
Then the host sends two dummy messages plus one shutdown message to the
slave core when receiving the remaining three Big data buffer messages.
Totally 10 Big data buffers are exchanged between the cores. The slave
core on receiving the shutdown message, shuts itself down and
reinitializes itself for future runs.

Then the host receives back the remaining returned messages before
shutting down.

.. note::
   The size of the big data buffer is configurable compile time by
   changing value of the define BIGDATA_SIZE in shared/AppCommon.h

Host Linux example
==================

.. note::
   Host linux example is only available starting from Processor SDK
   4.0.0 release for AM57xx platform

Under the host_linux directory the simple_buffer_example is implemented
for Host A15 running Linux and DSP core running TI-RTOS.

Architecture Updates for Linux
------------------------------

The following block diagram shows the various functional blocks used in
the example on the host running linux.

.. Image:: /images/Big_DATA_IPC_Linux_Software_blocks.png

The SharedRegion and HeapMem modules are not currently supported for
Linux in the TI Standard IPC package.

The example provides these modules with same/similar API implemented for
Linux with some limitations.

The CMEM APIs provide user space allocation of contiguous memory for the
Big data buffers.

How to Run the Example
----------------------

The Processor SDK Linux release includes the pre-built binaries for the
host_linux example as part of the tisdk-rootfs-image filesystem.

Step 1 : To run the demo, the first step is to make sure there is no
other default applications using the same resources. For example, the
following command is needed to disable the default OpenCL applications.

::

       systemctl stop ti-mct-daemon.service

Step 2: Switch the firmware running in the DSP. This can be done by
using the following steps. Unbind dsp

::

       echo 40800000.dsp > /sys/bus/platform/drivers/omap-rproc/unbind

.. note::
   May need to unbind all the other cores as well to avoid issues.

Update firmware symbolic link

::

       ln -sf /usr/bin/simple_buffer_example/release/server_dsp.xe66 /lib/firmware/dra7-dsp1-fw.xe66

Bind dsp

::

       echo 40800000.dsp > /sys/bus/platform/drivers/omap-rproc/bind

Step 3: Now the Host side application can be run using the following
command

::

       /usr/bin/simple_buffer_example/release/app_host

The DSP side log can be checked by typing the following command to dump
the trace.

::

       cat /sys/kernel/debug/remoteproc/remoteproc2/trace0

Here is a sample log.

::

    root@am57xx-evm:~# /usr/bin/simple_buffer_example/release/app_host DSP1
    --> main:
    [523682.897761] omap_hwmod: mmu0_dsp2: _wait_target_disable failed
    [523682.903751] omap-iommu 41501000.mmu: 41501000.mmu: version 3.0
    [523682.911797] omap-iommu 41502000.mmu: 41502000.mmu: version 3.0
    --> Main_main:
    --> App_create:
    App_create: Host is ready
    <-- App_create:
    --> App_exec:
    CMEM_init success
    CMEM_getPool success
    CMEM_allocPool success: Allocated buffer 0xaa641000
    SharedRegion_setup success
    App_taskFxn: SR_1, base 0xaa641000, len=1000000
    HeapMem_setup success
    HeapMem_create success
    App_taskFxn: SR_1 heap, totalSize=16777216,totalFreeSize=16777216,largestFreeSize=16777216
    App_taskFxn: SR_1 heap, buf=0x0xaa641080,size=16777216
    App_exec: sending message 1
    Shared memory phys Addr ffffffffa0000000
    App_exec: sending message 2
    App_exec: sending message 3
    App_exec: message received 1
    App_exec: Preparing message 4
    App_exec: Sending message 4
    App_exec: message received 2
    App_exec: Preparing message 5
    App_exec: Sending message 5
    App_exec: message received 3
    App_exec: Preparing message 6
    App_exec: Sending message 6
    App_exec: message received 4
    App_exec: Preparing message 7
    App_exec: Sending message 7
    App_exec: message received 5
    App_exec: Preparing message 8
    App_exec: Sending message 8
    App_exec: message received 6
    App_exec: Preparing message 9
    App_exec: Sending message 9
    App_exec: message received 7
    App_exec: Preparing message 10
    App_exec: Sending message 10
    App_exec: message received 8
    App_exec: Preparing message 11
    App_exec: Sending message 11
    App_exec: message received 9
    App_exec: Preparing message 12
    App_exec: Sending message 12
    App_exec: message received 10
    App_exec: Preparing message 13
    App_exec: Sending message 13
    App_exec: message received 11
    App_exec: Preparing message 14
    App_exec: Sending message 14
    App_exec: message received 12
    App_exec: Preparing message 15
    App_exec: Sending message 15
    App_exec: message received 13
    App_exec: Preparing message 16
    App_exec: Sending message 16
    App_exec: message received: 14
    App_exec: message received: 15
    App_exec: message received: 16
    App_exec: Data check clean
    <-- App_exec: 0
    --> App_delete:
    <-- App_delete:
    <-- Main_main:

     Host: Test Passed
    <-- main:
    root@am57xx-evm:~#

    root@am57xx-evm:~# cat /sys/kernel/debug/remoteproc/remoteproc2/trace0
    [      0.000] 18 Resource entries at 0x95000000
    [      0.000] [t=0x0002122e] xdc.runtime.Main: --> main:
    [      0.000] registering rpmsg-proto:rpmsg-proto service on 61 with HOST
    [      0.000] [t=0x003c5d7b] xdc.runtime.Main: NameMap_sendMessage: HOST 53, port=61
    [      0.000] [t=0x003d5186] xdc.runtime.Main: --> smain:
    [      0.000] [t=0x003e8259] Server: Server_create: server is ready
    [      0.000] [t=0x003ecc97] Server: <-- Server_create: 0
    [      0.000] [t=0x003f04a4] Server: --> Server_exec:
    [     51.571] [t=0x00000008:a56e6a9a] Server: Message received...1
    [     51.571] [t=0x00000008:a56f9b77] Server: Shared region entry configured...
    [     51.571] [t=0x00000008:a5700cb1] Server: Server_exec: processed id 1, cmd=0x1
    [     51.571] [t=0x00000008:a570aea5] Server: Message received...2
    [     51.571] [t=0x00000008:a57119fd] Server: Server_exec: processed id 2, cmd=0x0
    [     51.571] [t=0x00000008:a571b1e9] Server: Message received...3
    [     51.571] [t=0x00000008:a5721eac] Server: Server_exec: processed id 3, cmd=0x0
    [     51.571] [t=0x00000008:a5755f6b] Server: Message received...4
    [     51.573] [t=0x00000008:a583e61b] Server: Server_exec: processed id 4, cmd=0x2
    [     51.573] [t=0x00000008:a584a087] Server: Message received...5
    [     51.574] [t=0x00000008:a592c2cc] Server: Server_exec: processed id 5, cmd=0x2
    [     51.574] [t=0x00000008:a5937d8c] Server: Message received...6
    [     51.575] [t=0x00000008:a5a19aeb] Server: Server_exec: processed id 6, cmd=0x2
    [     51.575] [t=0x00000008:a5a2543d] Server: Message received...7
    [     51.577] [t=0x00000008:a5b07d15] Server: Server_exec: processed id 7, cmd=0x2
    [     51.577] [t=0x00000008:a5b137c0] Server: Message received...8
    [     51.578] [t=0x00000008:a5bf5d83] Server: Server_exec: processed id 8, cmd=0x2
    [     51.578] [t=0x00000008:a5c019cc] Server: Message received...9
    [     51.579] [t=0x00000008:a5ce3dca] Server: Server_exec: processed id 9, cmd=0x2
    [     51.579] [t=0x00000008:a5cef75e] Server: Message received...10
    [     51.581] [t=0x00000008:a5dd247a] Server: Server_exec: processed id 10, cmd=0x2
    [     51.581] [t=0x00000008:a5dde2d9] Server: Message received...11
    [     51.582] [t=0x00000008:a5ec04df] Server: Server_exec: processed id 11, cmd=0x2
    [     51.582] [t=0x00000008:a5ecc1a3] Server: Message received...12
    [     51.583] [t=0x00000008:a5fae91c] Server: Server_exec: processed id 12, cmd=0x2
    [     51.583] [t=0x00000008:a5fba4c6] Server: Message received...13
    [     51.585] [t=0x00000008:a609d1c1] Server: Server_exec: processed id 13, cmd=0x2
    [     51.585] [t=0x00000008:a60a8dd4] Server: Message received...14
    [     51.585] [t=0x00000008:a60af96e] Server: Server_exec: processed id 14, cmd=0x0
    [     51.585] [t=0x00000008:a60b9229] Server: Message received...15
    [     51.585] [t=0x00000008:a60bffd3] Server: Server_exec: processed id 15, cmd=0x0
    [     51.585] [t=0x00000008:a60e179b] Server: Message received...16
    [     51.585] [t=0x00000008:a60e9727] Server: Server_exec: processed id 16, cmd=0x2000000
    [     51.585] [t=0x00000008:a60f3fb7] Server: Server_exec: Data check clean
    [     51.585] [t=0x00000008:a60fb280] Server: <-- Server_exec: 0
    [     51.585] [t=0x00000008:a6101708] xdc.runtime.Main: DSP: Test Passed
    [     51.585] [t=0x00000008:a6109170] Server: --> Server_delete:
    [     51.585] [t=0x00000008:a6114fa2] Server: <-- Server_delete: 0
    [     51.586] [t=0x00000008:a6127d48] Server: Server_create: server is ready
    [     51.586] [t=0x00000008:a612ff93] Server: <-- Server_create: 0
    [     51.586] [t=0x00000008:a613620c] Server: --> Server_exec:
    root@am57xx-evm:~#

|


How to Re-Build the example
---------------------------

Also source code for the example is included in the Processor SDK Linux
release. Once installed the source files can be found in the directory
example-applications/big-data-ipc-demo-linux_<version>.

Prerequisites: Also need to have the Processor SDK RTOS release
installed to build the DSP side RTOS image. See the instruction in :ref:`RTOS
SDK Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>`

The example can be rebuilt by using the following commands.

::

       export TI_RTOS_PATH=<TI_RTOS_PROC_SDK_INSTALL_DIR>
       make big-data-ipc-demo

(e.g)

::

       export TI_RTOS_PATH=$HOME/ti
       make big-data-ipc-demo

The test binaries can be installed into the default filesystem using the
command.

::

       make big-data-ipc-demo_install

.. note::
   Rules.make file can be edited to change the DESTDIR where the
   binaries will be installed.

Source files
^^^^^^^^^^^^

The source files for the example are located at

::

       <processor-sdk_linux-<platform>-<version>/example-applications/big-data-ipc-demo-linux-<version>/host_linux/simple_buffer_example.

The host directory and dsp directory has the corresponding sources.
The shared folder contains some common sources.
The main sequence for big data IPC can be followed by looking at
host/App.c and dsp/Server.c.
|

Memory layout details
^^^^^^^^^^^^^^^^^^^^^

The DSP side memory layout can be found in the file
host_linux/simple_buffer_example/shared/<platform>/config.bld.
Also note the addition of the following section in
host_linux/simple_buffer_example/shared/<platform>/rsc_table_dsp.h.
Please note the reserved carve-out in the DSP resource table

.. note::
   Make sure this matches what is configured in the linux device tree

#. define DSP_CMEM_IOBUFS 0xA0000000
#. define PHYS_CMEM_IOBUFS 0xA0000000
#. define DSP_CMEM_IOBUFS_SIZE (SZ_1M \* 192)

The CMEM area allocated from this region is used for the big data
buffers.

Host RTOS example
=================

Under the host_bios directory the simple_buffer_example is implemented
for Host A15 and DSP both running TI RTOS/BIOS.

How to Run the Example
----------------------

The Processor SDK RTOS release include the pre-built binaries for the
host_bios example under:

::

       processor_sdk_<platform>_<version>/demos/bigdataipc/prebuilt-binaries/<board-name>/simple_buffer_example/release/

Also for the platforms that support boot through SDcard, pre-built boot
image or 'app' bootable through SBL is located under:

::

       processor_sdk_<platform>_<version>/demos/bigdataipc/prebuilt-binaries/bootimages/host_bios/simple_buffer_example/<board-name>/app

AM57xx & K2G boards
^^^^^^^^^^^^^^^^^^^

.. rubric:: Pre-requisites
   :name: pre-requisites

1. Create a bootable SDCard using the procedure here: :ref:`Creating SD card in Windows <Tools-Create-SD-Card-Windows-label>`
or
:ref:`Create SD card in Linux <Tools-Create-SD-Card-Linux-label>`

2. Connect the UART on the hardware to the Host.
( Configure the terminal/console to Baud Rate= 115200, Data Bits= 8 ,
Parity= None, Flow Control= Off )

.. rubric:: Procedure
   :name: procedure

-  Copy/overwrite the pre-built boot image 'app' corresponding to the
   board to a bootable SD Card
-  Insert the SD card into the board
-  Boot/Reboot the board

The application will be loaded and run automatically and the "Host: Test
Passed" message will be printed to the UART console.

.. Image:: /images/BigDataIPC_Rtos_Demo.png

K2H, K2K, K2L, K2E Boards
^^^^^^^^^^^^^^^^^^^^^^^^^

The prebuilt elf binaries of Host and DSP images can be loaded through
CCS to the appropriate cores and run.

How to Re-Build the Example
---------------------------

The bigdata ipc examples can be built from the Processor SDK top level
directory using the following steps

.. rubric:: 1. Build environment setup
   :name: build-environment-setup

.. rubric:: Linux host
   :name: linux-host

::

       cd  <processor_sdk_<platform>_<version>
       export SDK_INSTALL_PATH=<Base directory where Processor SDK is installed>
       source setupenv.sh

.. rubric:: Windows host
   :name: windows-host

::

       cd  <processor_sdk_<platform>_<version>
       set SDK_INSTALL_PATH=<Base directory where Processor SDK is installed>
       setupenv.bat

.. rubric:: 2. Build
   :name: build

::

       make bigdataipc_examples

This creates the elf binaries for both the host and DSP cores.
And the binaries can be installed using

::

       make bigdataipc_examples_install

(NOTE: The above command installs the elf binaries under the
prebuilt-binaries location mentioned above.
Need to convert the prebuilt elf binaries into bootable images refer
to :ref:`Processor SDK RTOS Boot <FC-Boot-label>`)

.. rubric:: Source files
   :name: source-files-1

The source files for the example are located at

::

       <processor_sdk_<platform>_<version>/demos/bigdataipc/host_bios/simple_buffer_example.

The host directory and dsp directory has the corresponding sources.
The shared folder contains some common sources.
The main sequence for big data IPC can be followed by looking at
host/App.c and dsp/Server.c.

