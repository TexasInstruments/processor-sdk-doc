.. http://processors.wiki.ti.com/index.php/Processor_SDK_IPC_Quick_Start_Guide
.. rubric:: Overview
   :name: overview-ipc

This page is meant to be a Quick Start Guide for applications using
IPC (Inter Processor Communication) in Processor SDK.

It begins with details about the out-of-box demo provided in the
Processor SDK Linux filesystem, followed by rebuilding the demo code and
running the built images. ( This covers the use case with the Host
running linux OS and the slave cores running RTOS).

Also details about building and running the IPC examples are covered.

The goal is to provides information for users to get familiar with IPC
and its build environment, in turn, to help users in developing their
projects quickly.

|

.. rubric:: Linux out of box demos
   :name: linux-out-of-box-demos

The out of box demo is only available on Keystone-2 EVMs.

.. note::

    This assumes the release images are loaded in the
    flash/SD Card. If needed to update to latest release follow the
    `Linux Getting Started Guide <Overview_Getting_Started_Guide.html>`__
    to update the release images on flash memory/SD card on the EVM using
    Program-evm or using the procedures for SD Card.

1. Connect the EVM Ethernet port 0 to a corporate or local network
   with DHCP server running, when the Linux kernel boots up, the rootfs
   start up scripts will get an IP address from the DHCP server and print
   the IP address to the EVM on-board LCD.
2. Open an Internet browser (e.g. Mozilla Firefox) on a remote
   computer that connects with the same network as the EVM.
3. Type the IP address displayed on EVM LCD to the browser and click
   cancel button to launch the Matrix launcher in the remote access mode
   instead of on the on-board display device.
4. Click the Multi-core Demonstrations, then Multi-core IPC Demo to
   start the IPC demonstration.

   .. Image:: /images/MatrixAppLauncher.jpg
      :scale: 60


   The result from running IPC Demo

   .. Image:: /images/IPC_Demo_Result.jpg
      :scale: 60


.. note::

    To view the out-of-box demo source code, please
    install Linux and RTOS Processor SDKs from `SDK download
    page <http://www.ti.com/lsds/ti/tools-software/processor_sw.page>`__

The source code are located in:

::

      Linux side application: <RTOS_SDK_INSTALL_DIR>/ipc_x_xx_xx_xx/linux/src/tests/MessageQBench.c
      DSP side application:   <RTOS_SDK_INSTALL_DIR>/ipc_x_xx_xx_xx/packages/ti/ipc/tests/messageq_single.c

**Rebuilding the demo:**

|
| **ARM Linux:**

**1.** Install Linux Proc SDK at the default location

**2.** Include cross-compiler directory in the $PATH

::

    export PATH=<sdk path>/linux-devkit/sysroots/x86_64-arago-linux/usr/bin:$PATH

**3.** Setup TI RTOS PATH using

::

    export TI_RTOS_PATH=<RTOS_SDK_INSTALL_DIR>
    export IPC_INSTALL_PATH=<RTOS_SDK_IPC_DIR>

**4.** In Linux Proc SDK, start the top level build:

::

    $ make ti-ipc-linux

**5.** The ARM binary will be located under the directory where the
       source code is <RTOS\_SDK\_INSTALL\_DIR>/ipc\_x\_xx\_xx\_xx/linux/src/tests/

.. note::

    Please follow the build instruction in `Linux Kernel User Guide
    <Foundational_Components_Kernel_Users_Guide.html>`__
    to set up the build environment.

|
| **DSP RTOS :**

**1.** Install RTOS Proc SDK at the default location

**2.** If RTOS Proc SDK and tools are not installed at its default
       location, then the environment variables, SDK\_INSTALL\_PATH and
       TOOLS\_INSTALL\_PATH need to be exported with their installed locations.

::

    export SDK_INSTALL_PATH=<RTOS_SDK_INSTALL_DIR>
    export TOOLS_INSTALL_PATH=<RTOS_SDK_INSTALL_DIR>

.. note::

    For ProcSDK 3.2 or older releases, tools are not included in RTOS SDK,
    so point to CCS:

::

    export TOOLS_INSTALL_PATH=<TI_CCS_INSTALL_DIR>

**3.** Configure the build environment in
       <RTOS\_SDK\_INSTALL\_DIR>/processor\_sdk\_rtos\_<platform>\_x\_xx\_xx\_xx
       directory

::

    $ cd <RTOS_SDK_INSTALL_DIR>/processor_sdk_rtos_<platform>_x_xx_xx_xx
    $ source ./setupenv.sh

**4.** Start the top level build:

::

    $ make ipc_bios

**5.** The DSP binary will be located under the directory where the
       source code is

::

    <RTOS_SDK_INSTALL_DIR>/ipc_x_xx_xx_xx/packages/ti/ipc/tests

|

.. rubric:: Build IPC Linux examples
   :name: build-ipc-linux-examples

IPC package and its examples are delivered in RTOS Processor SDK, but
can be built from Linux Proc SDK. To build IPC examples, both Linux and
RTOS processor SDKs need to be installed. They can be downloaded from
`SDK download
page <http://www.ti.com/lsds/ti/tools-software/processor_sw.page>`__

To install Linux Proc SDK, please follow the instruction in `Download
and Install the SDK
<Overview/Download_and_Install_the_SDK.html>`__

To Install RTOS Proc SDK, please see `Processor SDK for RTOS
<http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/
index_overview.html#processor-sdk-for-rtos>`__

Once the Linux and RTOS Processor SDKs are installed at their default
locations, the IPC Linux library, not included in the Linux Proc SDK,
can be built on Linux host machine with the following commands:

::

      $ cd <TI_LINUX_PROC_SDK_INSTALL_DIR>
      $ make ti-ipc-linux

The IPC examples in RTOS Proc SDK including out-of-box demo can be built
with the following commands:

::

      $ cd <TI_LINUX_PROC_SDK_INSTALL_DIR>
      $ make ti-ipc-linux-examples

.. note::

    Please follow the build instruction in `Linux Kernel User Guide
    <Foundational_Components_Kernel_Users_Guide.html>`__
    to set up the build environment.

.. note::

    If RTOS Proc SDK is not installed at its default
    location, then the environment variables, TI\_RTOS\_PATH
    needs to be exported with their installed locations.

::

      export TI_RTOS_PATH=<TI_RTOS_PROC_SDK_INSTALL_DIR>

Also if using Processor SDK 3.2 or older release, need to also set TI_CCS_PATH to CCSV6 location

::

      export TI_CCS_PATH=<TI_CCS_INSTALL_DIR>/ccsv6

.. rubric:: Run IPC Linux examples
   :name: run-ipc-linux-examples

1. The executables are in RTOS Proc SDK under the
   ipc\_xx\_xx\_xx\_xx/examples directory.

::

      <device>_<OS>_elf/ex<xx_yyyy>/host/bin/debug/app_host
      <device>_<OS>_elf/ex<xx_yyyyyy/<processor_or_component>/bin/debug/<ServerCore_or_component.xe66 for DSP
      <device>_<OS>_elf/ex<xx_yyyyyy/<processor_or_component>/bin/debug/<sServerCore_or_component.xem4 for IPU

2. Copy the executables to the target filesystem. It can also be done by
   running "make ti-ipc-linux-examples\_install" to install the binaries to
   DESTDIR if using NFS filesystem. ( See
   `Moving\_Files\_to\_the\_Target\_System <How_to_Guides/Host/Moving_Files_to_the_Target_System.html>`__
   for details of moving files to filesystem)

3. Load and start the executable on the target DSP/IPU.

For AM57x platforms, Modify the symbolic links in /lib/firmware of the
default image names to the built binaries. The images pointed by the
symbolic links will be downloaded to and started execution on the
corresponding processors by remoteproc during Linux Kernel boots.

::

      DSP image files: dra7-dsp1-fw.xe66  dra7-dsp2-fw.xe66
      IPU image files:  dra7-ipu1-fw.xem4  dra7-ipu2-fw.xem4

For OMAP-L138 platform, Modify the symblic link in /lib/firmware of the
default image names to the build binary

::

      DSP image files: rproc-dsp-fw

For Keystone-2 platforms, use the Multi-Processor Manager (MPM) Command
Line utilities to download and start the DSP executibles. Please refer
to /usr/bin/mc\_demo\_ipc.sh for examples

::

      The available commands are:
         mpmcl reset <dsp core>
         mpmcl status <dsp core>
         mpmcl load <dsp core>
         mpmcl run <dsp core>

4. Run the example
   From the Linux kernel prompt, run the host executable, app\_host.
   An example from running ex02\_messageq:

::

      root@am57xx-evm:~# ./app_host DSP1

The console output:

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
      App_exec  : message received
      App_exec: message received
      App_exec: message received
      <-- App_exec: 0
      --> App_delete:
      <-- App_delete:
      <-- Main_main:
      <-- main:
      root@am57xx-evm:~#

|

.. rubric:: Build IPC RTOS examples
   :name: build-ipc-rtos-examples

The IPC package also includes examples for the use case with Host and
the slave cores running RTOS/BIOS. They can be built from the Processor
SDK RTOS package.

.. note::

    To Install RTOS Proc SDK, please follow the
    instructions in `RTOS SDK Getting Started Guide
    <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_overview.html>`__
    In the RTOS Processor SDK, the ipc examples are located under
    <RTOS\_SDK\_INSTALL\_DIR>/processor\_sdk\_rtos\_<platform>\_x\_xx\_xx\_xx/ipc\_<version>/examples/<platform>\_bios\_elf.

NOTE: The platform in the directory name may be slightly different from
the top level platform name. For example, platform name DRA7XX refer to
common examples for DRA7XX & AM57x family of processors.

Once the RTOS Processor SDKs is installed at the default location, the
IPC examples can be built with the following commands:

::

       1. Configure the build environment in
          <RTOS_SDK_INSTALL_DIR>/processor_sdk_rtos_<platform>_x_xx_xx_xx directory
            $ cd <RTOS_SDK_INSTALL_DIR>/processor_sdk_rtos_<platform>_x_xx_xx_xx
            $ source ./setupenv.sh
       2. Start the top level build:
            $ make ipc_examples

.. note::

    If RTOS Proc SDK and tools are not installed at its
    default location, then the environment variables, SDK\_INSTALL\_PATH and
    TOOLS\_INSTALL\_PATH need to be exported with their installed locations.

|

.. rubric:: Run IPC RTOS examples
   :name: run-ipc-rtos-examples

The binary images for the examples are located in the corresponding
directories for host and the individual cores. The examples can be run
by loading and running the binaries using CCS through JTAG.

.. rubric:: Build your own project
   :name: build-your-own-project

After exercising the IPC build and running examples, users can take
further look at the source code of the examples as references for their
own project.

The sources for examples are under
ipc\_xx\_xx\_xx\_xx/examples/<device>\_<OS>\_elf directories. Once
modified the same build process described above can be used to rebuild
the examples.

