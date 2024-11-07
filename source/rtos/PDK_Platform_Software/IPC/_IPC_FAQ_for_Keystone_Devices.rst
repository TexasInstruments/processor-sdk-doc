.. http://processors.wiki.ti.com/index.php/IPC_FAQ_for_Keystone_Devices

Overview
^^^^^^^^^^

This wiki article is a collection of frequently asked questions (FAQ) on
IPC on Keystone family of devices , along with some useful collateral
and software reference links.

|

Guide on building and running the IPC examples of Processor SDK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| This guide will give step by step instruction on how to bring up the
  target EVMs and how to run the run the IPC examples of processor SDK
  on target EVM.

| Download the guide from :download:`Keystone II IPC Examples </files/Guide_Keystone_II_IPC_examples_.zip>`

| This guide will have steps on
| 1. Flashing the u-boot and boot u-boot.
| 2. Flashing the UBIFS image ( Linux and root filesystem ) into NAND
  and boot Linux.
| 3. Building the IPC package.
| 4. Building and running the IPC examples ( ex02_MessageQ,
  ex44_compute, ex45_host and ex46_graph ) on target EVM.
| 5. Real-time debugging on the DSP side programs using CCS.

|

Keystone IPC Frequently Asked Questions (FAQ)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Q: Where do I look for the list of IPC API reference
   document?
   :name: q-where-do-i-look-for-the-list-of-ipc-api-reference-document

**Ans:**

Please visit :
http://downloads.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/ipc/latest/docs/doxygen/html/index.html

The IPC product contains the following APIs:

::

    •GateMP (BIOS, Linux, QNX)
    •HeapBufMP (BIOS)
    •HeapMemMP (BIOS)
    •HeapMultiBufMP (BIOS)
    •Ipc (BIOS, Linux, QNX)
    •ListMP (BIOS)
    •MessageQ (BIOS, Linux, QNX)
    •MultiProc (BIOS, Linux, QNX)
    •NameServer (BIOS, Linux, QNX)
    •Notify (BIOS)
    •SharedRegion (BIOS)
    •IpcPower (BIOS)

Some environments also provide a "Multimedia RPC" interface. Currently
this is limited to OMAP5 and DRA7XX devices running an HLOS.

::

    •MmRpc (Linux, QNX)
    •MmServiceMgr (BIOS)

.. rubric:: Q: How to re-build the IPC package and its libraries?
   :name: q-how-to-re-build-the-ipc-package-and-its-libraries

**Ans:**

Actually, the user guide which comes along with the IPC package ( under
docs folder) is sufficient to build the IPC package. However, we have
extracted below steps from user guide. For building IPC package, you can
use either Cygwin/Command-line utility in windows machine or Linux
machine. This cannot be built through CCS.

| 1. Install the mcsdk_bios_3_xx_xx_xx which will install the IPC
  package version, ipc_3_xx_xx_xx
| 2. Go to the directory where the IPC package is installed.
| 3. Open the products.mak file and make sure the following parameters
  are set appropriately.

| For example:- ( For ipc-linux build )

::

           PLATFORM = TCI6638
           DESTDIR = /opt/ti/ipc_3_xx_xx_xx/ipc_3_xx_xx_xx_lib

::

           XDC_INSTALL_DIR = /opt/ti/xdctools_3_xx_xx_xx
           BIOS_INSTALL_DIR = /opt/ti/bios_6_xx_xx_xx
           ti.targets.elf.C66 = /opt/ti/ccsv5/tools/compiler/C6000_7.4.5

| 4. $cd /opt/ti/ ipc_3_xx_xx_xx
| 5. $make distclean
| 6. $make –f ipc-linux.mak config
| 7. $make
| 8. $make install

|

.. rubric:: Q: Is there any simple example to demonstrate IPC methods
   like message Q or notify for Keystone-II ?
   :name: q-is-there-any-simple-example-to-demonstrate-ipc-methods-like-message-q-or-notify-for-keystone-ii

**Ans:**

| Please look at the ex44_compute.zip
  in :~/ti/ipc_3_3x_xx_xx/examples/TCI6638_linux_elf

::

          ~/ti/ipc_3_3x_xx_xx/examples$ ls
          C6472_bios_elf C6A8149_bios_elf DRA7XX_android_elf DRA7XX_linux_elf makefile TCI6638_linux_elf
          TI814X_bios_elf C6678_bios_elf dosrc.bat DRA7XX_bios_elf DRA7XX_qnx_elf OMAPL138_linux_elf TDA3XX_bios_elf

Please refer the readme.txt to run and build the example according to
the target used. For K2, use the cluster ID as 0 instead of 18.

#. perl patchExec.pl 0 compute_dspN.xe66 compute_dspN_patched.xe66
#. lad_tci6638 -r 8 -n 9 -b 0 -l log.txt

|

.. rubric:: Q: For Keystone II, is there any CCS based examples to
   demonstrate a simple communication between ARM-DSP?
   :name: q-for-keystone-ii-is-there-any-ccs-based-examples-to-demonstrate-a-simple-communication-between-arm-dsp

**Ans:**

No. We have only Image Processing Demo.

In MCSDK 3.x, the ARM core only runs Linux kernel and User Space
applications. There isn't any Linux application example using CCS and if
any, it will be using Linux commands.

.. rubric:: Q: In IPC packages, there are lot of test example(sample.c)
   code given in the path: "~\ipc_3_3x_xx_xx\packages\ti\ipc\tests". But
   there is only command line option to build the whole IPC package. No
   option available to build the test examples individually. This is
   time consuming to build the whole IPC package. Customers were asking
   for CCS based environment to build and test as individual example for
   both DSP and ARM side.
   :name: q-in-ipc-packages-there-are-lot-of-test-examplesample.c-code-given-in-the-path-ipc_3_3x_xx_xxpackagestiipctests.-but-there-is-only-command-line-option-to-build-the-whole-ipc-package.-no-option-available-to-build-the-test-examples-individually.-this-is-time-consuming-to-build-the-whole-ipc-package.-customers-were-asking-for-ccs-based-environment-to-build-and-test-as-individual-example-for-both-dsp-and-arm-side.

**Ans:**

The IPC package has been developed to work on multiple platforms like
Linux, Android, QNX and TI-RTOS(SYS/BIOS) so the command line build is
selected which is common across all these platforms and we do not have
CCS based projects for these examples.

|

.. rubric:: Q: For keystone-II devices, where do I find the source code
   of the image processing demo and how to I re-build them? Using ARM
   core as a master, DSP cores as slaves.
   :name: q-for-keystone-ii-devices-where-do-i-find-the-source-code-of-the-image-processing-demo-and-how-to-i-re-build-them-using-arm-core-as-a-master-dsp-cores-as-slaves.

**Ans:**

Tested version : "mcsdk_bios_3_00_03_15". The Image processing demo was
tested multiple times with this version and it works fine.

The image processing demo source code can be found in below path.

**PATH:** C:\ti\mcsdk_bios_3_0x_0x_0x\demos\image_processing\ipc (master,
slave and common directories)

**Building Slave Code:**
The project can be imported into CCS and can be rebuilt.

*For K2E:*
“~\mcsdk_bios_3_0x_0x_0x\demos\image_processing\ipc\evm66ak2e\slave”

*For K2K:*
“~\mcsdk_bios_3_0x_0x_0x\demos\image_processing\ipc\evmtci6638k2k\slave”

*For K2L:*
“~\mcsdk_bios_3_0x_0x_0x\demos\image_processing\ipc\evmtci6630k2l\slave”

**Building Master Code:**

This can be built in the linux environment using the makefile provided
at

(~\mcsdk_bios_3_0x_0x_0x\demos\image_processing\ipc\evm66ak2x\master\make
) which in turn uses the makefile located at
~\mcsdk_bios_3_0x_0x_0x\demos\image_processing\ipc\master\src

|

.. rubric:: Q: How to import the slave code of Image processing demo and
   how do I build it?
   :name: qhow-to-import-the-slave-code-of-image-processing-demo-and-how-do-i-build-it

**Ans:**

Refer the screenshot below in which the correct path should be provided
to pick up the project and its sources. Note that the option for “Copy
projects into work space" should be unchecked.

.. Image:: /images/ImportPjt.jpg

|

In the project explorer screen, check whether you are able to see the
folders, slave --> src --> \*.c files.... Right click on the project and
give build.

.. Image:: /images/Sourcefilepjt.jpg

.. rubric:: Q: After building the slave code of the Image processing
   demo using CCS, where it needs to be replaced in the linux file
   system?
   :name: q-after-building-the-slave-code-of-the-image-processing-demo-using-ccs-where-it-needs-to-be-replaced-in-the-linux-file-system

**Ans:**

Take the binary file, image_processing_evmtci66xxk2x_slave.out and
replace it in the path target Linux filesystem,
“/usr/share/matrix-gui-2.0/apps/demo_imageproc/bin/"

.. rubric:: Q:  While building the ARM(master) side code of Image
   processing demo, I see a compilation error message about Std.h as
   below when I make it with or without BUILD_LOCAL=true.
   :name: q-while-building-the-armmaster-side-code-of-image-processing-demo-i-see-a-compilation-error-message-about-std.h-as-below-when-i-make-it-with-or-without-build_localtrue.

| *Error:*
| ***user@ubuntu:~/ti/mcsdk_bios_3_0x_0x_0x/demos/image_processing/ipc/evm66ak2x/master$***
  make

| *make[1]: Entering directory
  \`/home/user/ti/mcsdk_bios_3_0x_0x_0x/demos/image_processing/ipc/master/src'
  mcip_mem_mgmt.c:53:24: fatal error: ti/ipc/Std.h: No such file or
  directory #include <ti/ipc/Std.h> Compilation terminated.*

| **Ans:**
| There is an error in the Makefile. Make file needs to be updated for
  including the appropriate search path for "Std.h". You will find it at
  "../ti/ipc_3_3x_0x_0x/linux/include

Update the Makefile located at
"mcsdk_bios_3_0x_0x_0x\demos\image_processing\ipc\master\src\makefile"
as below,

| *For example:*

::

         IPC_INSTALL_DIR := /opt/ti/ipc_3_xx_0x_0x
         CFLAGS  := -Wall -I$(COMMON_INC) -I$(MASTER_INC) -I$(IPC_INSTALL_DIR)/linux/include -I$(IPC_INSTALL_DIR)/packages -D_GNU_SOURCE

.. rubric:: Q: While building the ARM(master) side code of Image
   processing demo, I see a linker error message like below.
   :name: q-while-building-the-armmaster-side-code-of-image-processing-demo-i-see-a-linker-error-message-like-below.

| *Error:*
| */usr/bin/ld: skipping incompatible
  /opt/ti/ipc_3_35_01_07/examples/TCI6638_linux_elf
  /ex44_compute_bkp/lib//libtitransportrpmsg.a when searching for
  -ltitransportrpmsg
  /usr/bin/ld: cannot find –ltitransportrpmsg*
| usr/bin/ld: cannot find -ltiipcutils
| collect2: error: ld returned 1 exit status
| make: \**\* [../../master/image_processing_master.out] Error 1
| root@e2e:/opt/ti/mcsdk_bios_3_0x_xx_xx/demos/image_processing/ipc/master/src#\ *
  *

| **Ans:**
| For these errors, please make sure you already built the Whole IPC
  package and installed the libraries such as transportrpmsg in a
  destination directory. This destination directory should be given in
  the makefile to find those libraries.

| For example, in the makefile located at
  mcsdk_bios_3_0x_xx_xx\demos\image_processing\ipc\master\src\makefile

::

        IPC_INSTALL_DIR := /opt/ti/ipc_3_3x_xx_xx

        #The location where the libraries are installed after building the IPC package
        SIPC_LINUX_DIR := /opt/ti/ipc_3_3x_xx_xx/IPC_Linux_libraries

::

        CROSS_COMPILE ?= arm-linux-gnueabihf-
        CC            := $(CROSS_COMPILE)gcc
        CFLAGS        := -Wall -I$(COMMON_INC) -I$(MASTER_INC) -I$(IPC_INSTALL_DIR)/linux/include -I$(IPC_INSTALL_DIR)/packages -D_GNU_SOURCE
        LFLAGS        := -lpthread -L$(SIPC_LINUX_DIR)/ -ltitransportrpmsg -L$(SIPC_LINUX_DIR)/ -ltiipc -L$(SIPC_LINUX_DIR)/ -ltiipcutils

|

.. rubric:: Q: The Image processing demo does not work on the version of
   MCSDK, V3.0x.xx.x on both the K2H and K2E EVMs. The earlier version
   of MCSDK works on both the EVMs. Will it be fixed on next version?
   :name: q-the-image-processing-demo-does-not-work-on-the-version-of-mcsdk-v3.0x.xx.x-on-both-the-k2h-and-k2e-evms.-the-earlier-version-of-mcsdk-works-on-both-the-evms.-will-it-be-fixed-on-next-version

**Ans:**

| Make sure the u-boot environments is set as below to work on MCSDK
  3.x.

::

             u-boot# env default –f –a
             u-boot# setenv mem_reserve 1536M
             u-boot# saveenv

|

.. rubric:: Q: How to build and run the qmssIpcBenchmark on C6678 EVM?
   :name: q-how-to-build-and-run-the-qmssipcbenchmark-on-c6678-evm

**Ans:**

**Hardware set up:**

::

      Set the boot mode dip switch to no boot/EMIF16 mode, Connect power and emulator to C6678 EVM.

**Software setup:**
1. After power ON the EVM, create and launch the target configuration
file(.ccxml) for CCS debugging.

2. Group Core 0 and Core 1 in CCS.

3. Connect to both cores via the group.

4. Load the evmc66xxl.gel to initialize the DDR. The GEL can be found in
the "CCS install
dir"\ccsv5\ccs_base_x.x.x.xxxxx\emulation\boards\evmc66xxl\gel
directory. Once loaded execute the default setup script on each core. In
the CCS menu go to Scripts->EVMC6678L Init
Functions->Global_Default_Setup.

5. Highlighting the Group in the CCS Debug window, load
transport\ipc\examples\qmssIpcBenchmark\Debug\qmssIpcBenchmark_c66xx.out
on each core

6. Highlighting the Group in CCS Debug window, run the program in CCS on
both cores simultaneously, qmssIpcBenchmark_c66xx will send messageQ
messages between the cores via the QMSS transport. The messages will be
used to measure the transport's performance. The test will be complete
after the throughput (msg/s) has been calculated.

.. Image:: /images/Qmss_IPC.png

.. rubric:: Q: How can I build the qmssIpcbenchmark of pdk_C6678_1_1_2_x
   pdk_C6678_1_1_2_x with release build configuration ?
   :name: q-how-can-i-build-the-qmssipcbenchmark-of-pdk_c6678_1_1_2_x-pdk_c6678_1_1_2_x-with-release-build-configuration

**Ans:**

| Actually the option, "-mo -o3 -q -k -eo.o" works for building the
  IPC-QMSS transport library in release mode and the option "-mo -g -q -k -eo.o"
  works for building the IPC-QMSS transport library in debug mode.
| But the common.bld script of IPC doesnot create a "release" folder. By
  default it always creates the "debug" folder and dumps all the
  binaries.
| By tweaking the common.bld, release folder can be made and hence the
  the IPC - qmssIpcBenchmark project can be built in release mode.
| **How to change the Common.bld:**
| 1. Go to C:\ti\ipc_3_00_xx_xx\packages\ti\sdo\ipc\build\Common.bld (
  Note: Go to the IPC version you use for building the transport
  library. Here, it refers to IPC version : 3.00.4.29)
| 2. Modify
| Line No:88 profiles[0] = "release";
| Line No: 99 var libPath = "lib/ipc/release/";
| 3. Build with option : -mo -o3 -q -k -eo.o in config.bld of transport
  library located at
  "..\ti\pdk_C6678_1_1_2_x\packages\ti\transport\ipc\qmss\transports"
| 4. Now build qmssIpcBenchmark project.
| Screenshot of the successful release build of qmssIpcBenchmark
  project.
.. Image:: /images/QMSSIPC_project1.png

|

.. rubric:: Q: How to re-build the IPC - QMSS transport library and
   generate “ti.transport.ipc.qmss.transports.ae66” ?
   :name: q-how-to-re-build-the-ipc---qmss-transport-library-and-generate-ti.transport.ipc.qmss.transports.ae66

**Ans:**

After installing PDK, go to path
“~\ti\pdk_C6678_1_1_2_x\packages\ti\transport\ipc\qmss\transports”

1. [Optional - Required for debug single stepping] Modify the transports
config.bld file C66LE/BE.ccOpts.prefix to remove optimization and add
symbolic debug

::

      From: "-mo -o3 -q -k -eo.o"
      To: "-mo -g -q -k -eo.o"

2. From a command prompt navigate to the
pdk\packages\ti\transport\ipc\(qmss or srio) directory 3 Configure the
XDCPATH environment variable with the BIOS and IPC install locations:

::

      set XDCPATH=c:\ti\bios_w_xx_yy_zz\packages\
      set XDCPATH=%XDCPATH%;c:\ti\ipc_w_xx_yy_zz\packages\

4 Configure the XDCCGROOT environment variable with the compiler install
path (Using CGT 7.2.4 installed as part of CCS as an example)

::

      set XDCCGROOT=c:\ti\ccsv5\tools\compiler\c6000_7.2.4

5 Add the XDC Tools to your system PATH

::

      set PATH=%PATH%;c:\ti\xdctools_w_xx_yy_zz\

6 Clean the transport

::

      >xdc clean -PR .

7 Build the transport

::

      >xdc -PR .

If we try this option, we should be able to build in releasemode. Note:
To allow single-step debug of the IPC and BIOS source rebuild the
example projects with the following command added to the example's .cfg
file BIOS.libType = BIOS.LibType_Debug; <--- here.

.. Image:: /images/Qmss_transports.png


