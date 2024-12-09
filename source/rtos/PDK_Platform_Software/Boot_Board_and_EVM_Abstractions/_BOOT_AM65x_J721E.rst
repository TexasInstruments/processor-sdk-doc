.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_BOOT_AM65x_J721E

Overview
^^^^^^^^^

The Secondary Bootloader (SBL) for AM65xx/J721E device initializes the execution
environment for multi-core applications and this can be used to demonstrate
a real world product experience. This section covers additional details
including execution sequence, tools and additional flashing instructions.

The SBL is essentially a baremetal application, and it uses many components
from the Processor SDK

- <PDK>/packages/ti/build : For  build infrastructure
- <PDK>/packages/ti/csl : For initialization and SoC addresses
- <PDK>/packages/ti/board : For board and usecase specific initialization
- <PDK>/packages/ti/drv/spi :  For reading applications from OSPI flashes
- <PDK>/packages/ti/drv/udma :  For reading data from boot media using DMA
- <PDK>/packages/ti/drv/mmcsd : For reading applications from MMC/SD/eMMC
- <PDK>/packages/ti/fs/fatfs : For reading files from MMC/SD/eMMC
- <PDK>/packages/ti/drv/sciclient : For communicating with DMSC sub-system
- <PDK>/packages/ti/drv/uart : For log messages
- <PDK>/packages/ti/osal : Primitives required by ti/drv components

The SBL is in turn used by the board framework to load and start diagnostics


.. rubric:: Bootloader Execution Sequence
   :name: bootloader-execution-sequence

-  **Power On Reset**
-  **ROM Bootloader (RBL)**

   -  Software pre-programmed in AM65xx/J721E ROM memory starts executing
   -  The RBL performs platform configuration and initialization.
   -  It then checks sysboot pins and chooses booting device
   -  The RBL then configures PLL and clock settings for R5, and
      boot media like eMMC, SD/MMC, OSPI, UART, PCIe, Ethernet etc for reliable
      boot.
   -  If no valid bootloader found on booting device, the RBL checks for next
      booting device, based on sysboot pins
   -  It then gets image size and load address by checking the X.509 certificate that
      is part of the bootloader image.
   -  The RBL then verifies, optionally decrypts and loads the binary to internal
      memory at the load address specified in the X.509 certificate.
   -  Finally it resets the R5 and passes control to Secondary Bootloader(SBL) running on the R5.

-  **Secondary bootloader(SBL)**

   -  User level secondary bootloader(SBL) begins execution from internal memory.
      It enables ATCM, starts PMU timers for profiling, initializes the MCU,
      and sets up the stack, heap and globals. It then jumps to main().
   -  Board Initialization is done by calls to **Board_init()** API.For additional
      details refer `Processor SDK Board Support
      <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/Board_EVM_Abstration.html>`__.
   -  The RAT is setup. Pin MUX and UART console are setup by calling **Board_init()** API. The
      system firmware (SYSFW) is then loaded from the boot media into the DMSC subsystem.
   -  Once the SYSFW is up and running, the rest of the initialization can be done.
   -  This includes optionally using **Board_init()** to configure PLLs, LPSCs and DDR.
   -  The SBL then loads the application from the boot media. If the image is signed, the
      application will be copied into a user specified reserved memory, and the SBL will attempt
      to verify the image by calling system firmware APIs. On HS devices, the boot proceeds
      only if image verification passes.
   -  The SBL parses application image(s) for each of the core(s) from boot
      media and scatter loads it to memory.
   -  Once the application is loaded, the SBL communicates with the system firmware
      to setup the clocks for the core(s) and release it from reset.
   -  The core then starts executing from application entry point.

.. raw:: html

   <div
   style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

**NOTE**

-  RBL requires boot loader (SBL) to be in a special format with the binary image
   appended to a X.509 certificate. The certificate contains the load address, size
   and SHA of the bootloader image.
-  For a detailed description of ROM bootloader and more information on the image
   format expected by the RBL refer the initialization chapter in the `AM65xx Technical
   Reference Manual <http://www.ti.com/lit/pdf/spruid7>`__ and the `J721E Technical
   Reference Manual <http://www.ti.com/lit/pdf/spruil1>`__
-  In addition to the bootloader and application, the DMSC firmware binary is also needed
   for the SoC to complete the system boot flow.
-  The first 256 bytes of the ATCM are reserved by SBL for its use. The SBL initializes
   the ATCM with 0xFF before it uses it.
-  If the multicore application image is signed using the TI Dummy Key, instead of a
   degenerate key (default setting) the same binary can be used on GP and HS devices.
   For information on the application's X.509 certificate format, please refer
   `Security X509 Certificate Documentation <http://downloads.ti.com/tisci/esd/latest/
   2_tisci_msgs/security/sec_cert_format.html#security-x509-certificate-documentation>`__
-  When the R5 is released from reset, it will always fetch and execute the first
   intruction from address 0x0.

.. raw:: html

   </div>

.. _am655x-sbl-high-level-arch:

Block Diagram
^^^^^^^^^^^^^^^^

.. Image:: /images/k3_sbl_arch_block_diag.png

.. _am655x-sbl-memory-usage:

Memory Map
^^^^^^^^^^^

.. Image:: /images/k3_sbl_mem_usage.png


.. _am655x-sbl-directory-structure:

Directory structure
^^^^^^^^^^^^^^^^^^^^

::

    sbl
    │
    ├── board
    │   └── k3
    │       └── sbl_main.c					<= define main() for SBL, board specific init
    │
    ├── build
    │   ├── makefile						<= makefile for the SBL component
    │   ├── sbl_am65xx.sh					<= For legacy, called by Yocto build
    │   ├── sbl_boot_test.mk					<= Builds SBL single core tests
    │   ├── sbl_smp_test.mk					<= Builds example app for using SBL lib
    │   ├── sbl_mcu0_boot_perf_test.mk				<= Builds example app for SBL performance tuning
    │   ├── sbl_mcu0_boot_xip_entry.mk				<= Builds example trampoline app to demonstrate transitioning to a XIP app from SBL
    │   ├── sbl_mcu0_boot_xip_test.mk				<= Builds example app to demonstrate XIP execution from XIP capable boot media
    │   ├── sbl_img.mk						<= builds SBL image that is loaded and executed by ROM code
    │   ├── sbl_lib.mk						<= Builds sbl library that other apps can link into
    │   ├── sbl_multicore_smp.mk				<= Builds multi-core image from SBL lib eg. test to demonstrate symmetric multiprocessor boot (SMP)
    │   └── sbl_multicore_amp.mk				<= Builds multi-core image from single core tests to demonstrate asymmetric multiprocessor boot (AMP)
    │
    ├── example
    │   └── k3MulticoreApp
    │       ├── binary
    │       │   └── [soc]
    │       │       ├── sbl_baremetal_*.appimage 		<= SBL loadable board specific sample apps for testing SBL boot flow on GP devices
    │       │       ├── sbl_baremetal_*.appimage.signed		<= SBL loadable board specific signed sample apps for testing SBL boot flow on HS devices
    │       │       └── sbl_baremetal_*_release.x*.bin		<= Binary image that can be eXecuted In Place on XIP capable boot media
    │       ├── mcuAmplinker.lds 				<= Linker comamnd file when TI CGT is used for Asym. Multiproc. boot
    │       ├── mpuAmplinker.lds 				<= GCC linker command file (for Cortex Axx cores) for Asym. Multiproc. boot
    │       ├── mcuBootPerfLinker.lds 				<= TI CGT Linker comamnd file for SBL performance tuning example.
    │       ├── mcuLockStepLinker.lds 				<= Linker comamnd file when TI CGT is used for R5 lock-step boot
    │       ├── mpuSmplinker.lds 				<= GCC linker command file (for Cortex Axx cores) for SMP boot
    │       ├── mcuXiplinker.lds 				<= Linker command file for XIP trampoline app
    │       ├── xip_entry.lds 					<= Linker comamnd file for XIP test case
    │       ├── xip_entry.asm 					<= Entry point of XIP trampoline app
    │       ├── xip_stub.c 					<= Simple SBL test app that demonstrates transitioning to a XIP app
    │       ├── sbl_amp_multicore.c 				<= Simple SBL test that displays UART message
    │       ├── sbl_amp_multicore_sections.h 			<= Allows same source to be loaded to different sections for different cores.
    │       ├── sbl_mcu_0_boot_perf_benchmark.c			<= SBL Test to tune boot performance.
    │       ├── sbl_multicore_a53.asm 				<= Test case entry point  for Cortex-Axx cores
    │       ├── sbl_multicore_r5.asm 				<= Test case entry point for Cortex-R5 cores
    │       ├── sbl_multicore_r5_sections.inc 			<= Allows same source to be loaded to different sections for different MCUs.
    │       ├── sbl_printf.c 					<= Lightweight UART printf function for SBL testing
    │       ├── sbl_smp_multicore.c 				<= Simple SBL SMP test that uses SBL lib to reset MPUs
    │       └── sbl_smp_r5.asm 					<= Provides dummy override function for __mpu_init for SMP testcase.
    │
    ├── binary							<= ROM bootable SBL images for each board/boot media
    │   ├── [board]
    │       └── [bootmedia]
    │           └── bin
    │               └── sbl_[bootmedia]_img_mcu1_0_release.tiimage
    │
    ├── lib							<= SBL lib for each boot media/board supported
    │   ├── [bootmedia]
    │   │   └── [board]
    │   │       └── r5f
    │   │           └── release
    │   │               └── sbl_lib_[bootmedia].aer5f
    │   └── cust
    │       └── [board]
    │           └── r5f
    │               └── release
    │                   └── sbl_lib_cust.aer5f
    │
    ├── soc							<= SOC specific SBL code
    │   └── k3
    │       ├── linker.cmd					<= Linker file used for generating ROM loadable SBL image.
    │       ├── sbl_err_trap.h					<= Error loops for SBL
    │       ├── sbl_init.asm					<= SBL Entry point
    │       ├── sbl_misc.asm					<= SBL Assembly utility functions
    │       ├── sbl_log.h					<= SBL logging framework
    │       ├── sbl_sci_client.c				<= Calls SYSFW on DMSC
    │       ├── sbl_sci_client.h
    │       ├── sbl_slave_core_boot.c				<= Code that contains the sequence to release a core from reset
    │       ├── sbl_slave_core_boot.h
    │       ├── sbl_soc.c					<= Cache Ops, PMU init, image verfication, etc & SoC specific code like RAT Init..
    │       ├── sbl_soc_cfg.h					<= Abstraction layer for hiding SoC level changes from SBL
    │       └── sbl_profile.h					<= SBL profiling framework
    │
    ├── src							<= Common drivers used across SOCs
    │   ├── mmcsd
    │   ├── hyperflash
    │   ├── ospi
    │   ├── qspi
    │   ├── uart
    │   ├── rprc						<= RPRC image parser used by SBL
    │   └── spi
    │
    └── tools
        ├── btoccs
        ├── byteswap
        ├── ccsutil
        ├── flashWriter						<= Unused for AM65xx/J721E. AM65xx/J721E uses Uniflash to program flashes.
        ├── multicoreImageGen					<= Stitches multiple RPRC images for different cores into a single image
        ├── omapl13x_boot_utils					<= Unused for AM65xx/J721E
        ├── omapl13x_sd_card_format				<= Unused for AM65xx/J721E
        ├── out2rprc						<= Converts .out into .rprc files, so that SBL can load non-continuous memory sections
        ├── scripts						<= Scripts used by .out  generated by CCS projects into SBL loadable images
        │   ├── K3ImageGen.bat
        │   └── K3ImageGen.sh
        └── tiImageGen						<= Unused for AM65xx/J721E. Image generation is handled by PDK build framework (<prsdk_install_path>/pdk_*/packages/ti/build/)


.. _am655x-image-formats:

Image Formats
^^^^^^^^^^^^^^

**SBL format:**

To generate the a bootable image, the SBL build uses the x509CertificateGen script to
sign the sbl binary with so that the ROM Boot Loader (RBL) can parse it. The image
format expected by the RBL has been described in detail in the Image Format Section
of the `AM65xx Technical Reference Manual <http://www.ti.com/lit/pdf/spruid7>`__ and
the `J721E Technical Reference Manual <http://www.ti.com/lit/pdf/spruil1>`__

.. note::  For HS devices, the SBL and system firmware have to be signed with the MPK.
           For an easy out-of-box experience, the Processor SDK for HS devices signs the
           SBL and system firmware with a TI Dummy Key. Images signed with a TI dummy
           key will boot on both GP and HS boards from TI. The build system invokes the script
           <PDK>/packages/ti/build/makerules/x509CertificateGen* which inturn calls OpenSSL
           to create the X509 certificate.

.. warning::  The TI Dummy Key(s) *MUST* be replaced by customers during production
              with their own Private Keys. If the TI Dummy Keys are used in a production
              system, the system will be open to security attacks. The path of the default
              (dummy) key used by the signing script for HS devices is
              <PDK>/packages/ti/build/makerules/k3_dev_mpk.pem

.. warning::  While SBL and system firmware images signed with the TI Dummy Keys will work
              on both GP and HS devices, the boot time will be significantly impacted on GP
              devices. Using SBL signed by TI Dummy Keys on GP devices is only recommended
              during the prototyping phase - when porting code developed on GP to HS devices.

**Application image format:**

Two utilities - out2rprc and multicoreImageGen are used to convert an application elf
image(s) into an image loadable by the SBL. The structure of a multicore application
image is provided below:

.. Image:: /images/Multicore_app_image.png

**RPRC File Header Format**

+------------+----------------------------+
| Offset     | Binary value               |
+============+============================+
| 0x00000000 | **Magic Word(43525052)**   |
+------------+----------------------------+
| 0x00000004 | **Entry Point (Location)** |
+------------+----------------------------+
| 0x00000008 | **Reserved Addr**          |
+------------+----------------------------+
| 0x0000000C | **Section Count**          |
+------------+----------------------------+
| 0x00000010 | **Version**                |
+------------+----------------------------+

**RPRC Section Header Format**

+------------+---------------------------+
| Offset     | Binary value              |
+============+===========================+
| 0x00000000 | **Section start Address** |
+------------+---------------------------+
| 0x00000004 | **Reserved Addr**         |
+------------+---------------------------+
| 0x00000008 | **Size**                  |
+------------+---------------------------+
| 0x0000000C | **Reserved CRC**          |
+------------+---------------------------+
| 0x00000010 | **Reserved**              |
+------------+---------------------------+

**Multicore boot image format**

**Meta Header Start**

+------------+-------------------------------+
| Offset     | Binary value                  |
+============+===============================+
| 0x00000000 | **Magic String (0x5254534D)** |
+------------+-------------------------------+
| 0x00000004 | **Number of Files**           |
+------------+-------------------------------+
| 0x00000008 | **Device ID**                 |
+------------+-------------------------------+
| 0x0000000C | **Reserved**                  |
+------------+-------------------------------+

**Meta Header per Core**

+------------+------------------+
| Offset     | Binary value     |
+============+==================+
| 0x00000000 | **Core ID**      |
+------------+------------------+
| 0x00000004 | **Image Offset** |
+------------+------------------+


**Signed application image format:**

To convert the multicore application image into a format that can be verified,  the build flow uses
the x509CertificateGen script to create a x509 certificate for the app image. Images that have a
x509 certificate are called signed images. Signed applications images are mandatory for HS devices,
but will work also work on GP devices.

Signed images are automatically detected by the SBL and loaded into a scratch memory area specified during
SBL build. The scratch memory area used by default is specified in `sbl_lib.mk <https://git.ti.
com/keystone-rtos/sbl/blobs/master/build/sbl_lib.mk>`__ via the flags SBL_SCRATCH_MEM_START and
SBL_SCRATCH_MEM_SIZE. The SBL_SCRATCH_MEM* options can also be specified for custom builds to override
the defaults.

The SBL scratch memory is unavailable to applications during app load time, as the SBL is
still active. Once the SBL transfers control to the application, this memory is available for app
use - in other words SBL_SCRATCH_MEM* is available during app runtime.

For information on the application's X.509 certificate format, please refer
`Security X509 Certificate Documentation <http://downloads.ti.com/tisci/esd/latest/
2_tisci_msgs/security/sec_cert_format.html#security-x509-certificate-documentation>`__

Building the SBL and its components
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Pre-requisites to Building**

-  Set your environment using pdksetupenv.bat or pdksetupenv.sh. Refer to
   `Processor SDK RTOS Building <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_overview.html#setup-environment>`__ for information on setting up your build environment

.. raw:: html

   <div
   style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

**NOTE**

-  SBL needs openssl to build. To check if openssl is present, type the
   following at the linux or windows prompt.
::

    openssl version


-  To build on Linux, you need to have `mono <http://www.mono-project.com>`__ installed.

-  Refer `Build Dependencies <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/Overview.html#command>`__ for instructions on how to install these tools,
   if they are not already present on your system.


.. raw:: html

   </div>

**Compiling the SBL**

To build all the SBL components:
::

    cd <PDK>/packages/ti/boot/sbl/build
    gmake clean all (for windows)
    make clean all  (for Linux)

-  SBL image files are be located at: **<PDK>/packages/ti/boot/sbl/binary/**
-  SBL examples are located at **<PDK>/packages/ti/boot/sbl/examples/k3MulticoreApp/binary**
-  SBL lib are located at **<PDK>/packages/ti/boot/sbl/lib/**

**Compile time options for the SBL**

The SBL supports several compile time options to tweak the SBL to satisfy requirements of
ease of use, boot time and size. These can be enabled or disabled by editing `sbl/sbl_component.mk
<http://git.ti.com/cgit/processor-sdk/pdk/tree/packages/ti/boot/sbl/sbl_component.mk>`__

-  SBL_LOG_LEVEL : Controls amount of SBL logs (on the MCU UART) and system firmware logs(on WAKEUP UART).
   Varies from 0(no logs) to  3 (all logs)
-  SBL_USE_DMA : Valid values are 0 (use CPU to access boot media) or 1 (use DMA to
   access boot media).
-  SBL_DISPLAY_PROFILE_INFO : At the end of the boot process, displays a log of timestamps
   at which different SBL profile points are hit. This is useful to see how much
   time the SBL spends in different functions. SBL_LOG_LEVEL can significantly
   affect performance numbers.
-  SBL_ENABLE_PLL : Dials up all the PLLs calling Board_init(). Makes it easier for
   applications as they no longer have to initialize the PLLs. However, enabling this
   significantly increases boot time and power consumption. Requires system firmware to
   be loaded.
-  SBL_ENABLE_CLOCKS : Enables all the module clocks by calling Board_init(). Makes
   it easier for applications as they no longer have to enable clocks.
-  SBL_ENABLE_DDR : Initializes the DDR. At the cost of boot time, this enables
   applications to run from and use DDR. SBL_ENABLE_CLOCKS and SBL_ENABLE_PLL must
   also be enabed for this to work. Enabling this option increases the boot time.
-  SBL_SKIP_MCU_RESET : Jumps to the MCU0 application entry point
   without resetting the core. Enables faster boot time. Will not change the MCU's
   mode (lock-step/split). Application also inherits the MCU state as the SBL
   left it in.
-  SBL_ENABLE_DEV_GRP_MCU : Will cause the system firmware to only use MCU domain
   resources during system firmware initialization. This can be dont either to support
   boot when the main power domain is off, or to save boot time.

The SBL also supports a "custom" build, in addition to standard out-of-box builds.
A custom build is a useful way of testing out the effect of different build options -
like when optimizing for boot time, or enabling custom usecases like eXecute In Place (XIP)
to reduce memory usage.

For an example of how to use such custom builds, please refer to `sbl/sbl_component.mk
<https://git.ti.com/cgit/processor-sdk/pdk/tree/packages/ti/boot/sbl/sbl_component.mk#n526>`__. It shows
how to specify a select list of build options while building SBL images and libs.


**SBL Startup**

The SBL can specify the R5 configuration (lockstep or split) that ROM needs to use when it
starts up the SBL. This info is passed to ROM as a field in the X509 certificate. The value
in this field can be controlled by editing the build flag R5_STARTUP_MODE  in `sbl/build/sbl_img.mk
<https://git.ti.com/cgit/processor-sdk/pdk/tree/packages/ti/boot/sbl/build/sbl_img.mk#n91>`__

-  EFUSE_DEFAULT : SBL will run with the same R5 configuration the boot rom ran in.
-  SPLIT_MODE  : ROM will switch the R5 to split mode before starting the SBL (default).


**Enabling/Disabling JTAG on secure devices**

JTAG access is controlled using a field in the X509 certificate.

By default, for an easy out of box experience, the Processor SDK enables debug via JTAG
on High Secure devices. Leaving JTAG enabled, while making it easy for software development,
creates a major security hole in production devices.

To disable/change the level of JTAG access on HS devices, update the value of the debugType field in the
signing scripts `build/makerules/x509template.txt <http://git.ti.com/cgit/processor-sdk/pdk/tree/packages/ti/build/makerules/x509template.txt#n74>`__
(when building from windows) and `build/makerules/x509CertificateGen.sh
<http://git.ti.com/cgit/processor-sdk/pdk/tree/packages/ti/build/makerules/x509CertificateGen.sh#n513>`__ (when building from linux).


Valid values are

-  0 : Disable all JTAG access (most secure and most restrictive)
-  1 : Use device defaults (most secure and most restrictive)
-  2 : Allow debug of non-secure code, when the CPU is running in secure mode, JTAG connectivity will be lost
-  4 : Allow debug of both secure and non-secure code (least secure and least restrictive). This is the default.


.. raw:: html

   </div>

.. _am655x-compiling-apps-for-sbl:

**Compiling apps that can be loaded by SBL:**

**Memory Map Considerations**

Applications that the SBL loads must comply with the am655x-sbl-memory-usage_.
In the application's linker command file, care must be taken to not use the first
0x100 bytes of any R5 MCU's ATCM memory and SBL reserved memory from 0x41C00100
to 0x41C3E000. If the applications are signed, no loadable sections must be placed
in the SBL scratch memory area. The scratch memory can be used at application runtime
for stacks, heaps, etc.

.. raw:: html

   <div
   style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

**NOTE**

-  The local address 0x0 of the MPU is not accessible from the MCU, so any MPU linker
   command file must not specify any loadable sections in that memory region. The SBL
   will not be able to access that memory to load code or data.


.. raw:: html

   </div>

**Converting ELF executables to SBL loadable image**

Depending on the usecase, an ELF application executable can be converted into an
image that can be loaded by SBL in many ways.

-  **Using CCS**: Any project created using the pdkProjectCreate scripts will
   automatically generate a SBL loadable app, as part of a post-build step.

-  **Using makefiles**: Add the following lines to the component's .mk file
::

    app_name_SBL_APPIMAGEGEN = yes
    export app_name_SBL_APPIMAGEGEN

-  **Existing ELF executable**: By calling the K3ImageGen script.
::

    Linux Syntax: K3ImageGen.sh <CoreID> <.out>

    Example:
    cd  <prsdk_install_path>/pdk_*/packages/ti/boot/sbl/example/ampMulticoreApp/binary/am65xx_evm/
    K3ImageGen.sh 4 sbl_baremetal_boot_test_am65xx_evm_mcu1_0TestApp_release.xer5f
::

    Windows Syntax: K3ImageGen.bat "<CoreID> <.out>"

    Example:
    cd  <prsdk_install_path>\pdk_*\packages\ti\boot\sbl\example\ampMulticoreApp\binary\am65xx_evm\
    K3ImageGen.bat "4 sbl_baremetal_boot_test_am65xx_evm_mcu1_0TestApp_release.xer5f"

-  **Multicore Images**: Multicore images, as the name suggests, allows the SBL
   to load applications for multiple cores from a single image. Creating such images
   invloves three steps.
#. Generate the ELF application executables for individual cores
#. Convert the ELF executables into intermediate .rprc images
#. Combine the .rprc images of individual cores to create a single multicore image

To covert any .out into the intermediate .rprc format, execute the following commands
::

    For Linux:
    mono <PDK>/packages/ti/boot/sbl/tools/out2rprc/bin/out2rprc.exe input.out output.rprc
::

    For Windows:
    <PDK>\packages\ti\boot\sbl\tools\out2rprc\bin\out2rprc.exe input.out output.rprc

To stitch multiple .rprc images into a multicore image, execute the following command
::

    For Linux:
    <PDK>/packages/ti/boot/sbl/tools/multicoreImageGen/bin/MulticoreImageGen LE 55 output.appimage  <core_id_1> core_1.rprc <core_id_2> core_2.rprc

::

    For Windows:
    <PDK>/packages/ti/boot/sbl/tools/multicoreImageGen/bin/MulticoreImageGen.exe LE 55 output.appimage  <core_id_1> core_1.rprc <core_id_2> core_2.rprc

.. raw:: html

   <div
   style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

**NOTE**

-  The linux host environment needs to have `mono <http://www.mono-project.com>`__ installed.
-  The values used for the Core ID and Device ID can be found in `sbl/soc/k3/
   sbl_slave_core_boot.h <https://git.ti.com/cgit/processor-sdk/pdk/tree/packages/ti/boot/sbl/soc/k3/sbl_slave_core_boot.h#n51>`__
-  To simply load an ELF without executing it, use CoreID value ONLY_LOAD_ID
-  If an image for MCU_1 core is provided, the SBL will attempt to switch to
   split mode.
-  If only an image for MCU_0 is provided, the SBL will not change the mode of the
   MCU subsystem.
-  To enable SMP on the MPU, ie, to get multiple MPUs execute from a single binary
   from the same address, use one of the following core_ids

   -  MPU1_SMP_ID: The same app binary runs on both cores in MPU cluster 1
   -  MPU2_SMP_ID: The same app binary runs on both cores in MPU cluster 2
   -  MPU_SMP_ID:  The same app binary runs all the MPUs

.. raw:: html

   </div>


**Converting ELF executables to executable binary images**

Sometimes, for exteremely constrained and specialized usecases like ultra-low-latency boot
or DDR-less systems, an ELF application executable can be converted into a binary
image that can executed directly from the boot media, without loading into internal
memory.

As internal memory is always accessible, this mode of execution allows some otherwise
mandatory steps steps like DDR initlization or clock initialization  to be done
later or skipped altogether.

Working with such highly contrained systems require some special steps..

-  Make sure that the boot media supports eXecuting In Place (XIP).

-  Use the custom SBL build to select the build options to build a SBL
   that meets the usecase requirements.

-  In the linker command file for the application, make sure that all the data
   sections, stacks, heaps and globals are in internal read/write memory

-  In the linker command file for the application, make sure that there are no
   holes in the loadable sections. Such non-contiguous sections can drastically
   blow up the binary image size, when comapred to the ELF executable size.

-  To generate an executable binary image from the applications ELF file,
   add the following lines to the component's .mk file
::

    app_name_SBL_APP_BINIMAGEGEN = yes
    export app_name_SBL_APP_BINIMAGEGEN


Testing the SBL
^^^^^^^^^^^^^^^^^

SBL provides test applications to demonstrate booting the A53 and R5 cores in
both symmetric/lock step & asymmetric/split-mode and other features. The multicore
sample application prints a message on the UART for each core. The functionality
the different tests exercises are listed below.

-  sbl_*_boot_test_*_all_coresTestApp_release: A single multicore boot test case
   that boots each core in the SoC with a separate app. Also tests DDR loading
-  sbl_*_boot_test_*_xxxx_xTestApp_release.appimage: A simple testcase for booting
   core xxxx_x (eg. MCU1_0, MPU2_0 etc.)
-  sbl_*_smp_test_*_all_coresTestApp_release.appimage: A single SMP boot test case
   that boots MCUs in lock step. The MCU app then uses the SBL lib to boot all the
   MPUs in SMP mode, ie, all the MPUs execute a single binary from the same address.
-  sbl_baremetal_boot_perf_*_mcu1_0TestApp_release.appimage: A single MCU1_0 test
   case that can be used to measure the effect of enabling/disabling the perf.
   tuning knobs in the SBL for OSPI boot. The size of the test case can be easily
   modified by changing the values of .space directives in `sbl/example/k3MulticoreApp/
   sbl_boot_perf_r5.asm <http://git.ti.com/cgit/processor-sdk/pdk/tree/packages/ti/boot/sbl/example/k3MulticoreApp/sbl_boot_perf_r5.asm#n42>`__
   to profile for different app image sizes.
-  sbl_baremetal_boot_xip_test_*_mcu1_0TestApp_release.xer5f.bin: A testcase
   demonstrating booting an XIP application from OSPI flash. Please refer `sbl/build/
   sbl_mcu0_boot_xip_test.mk <https://git.ti.com/cgit/processor-sdk/pdk/tree/packages/ti/boot/sbl/build/
   sbl_mcu0_boot_xip_test.mk>`__ and `sbl/example/k3MulticoreApp/mcuXiplinker.lds
   <https://git.ti.com/cgit/processor-sdk/pdk/tree/packages/ti/boot/sbl/example/k3MulticoreApp/mcuXiplinker.lds>`__
   to see how to convert an existing application into an XIP application. The
   sbl_*_xip_entry_*.appimage works in tandem with sbl_*xip_test_*.xer5f.bin to transition
   the system from non-xip to xip boot, as the ROM, by default, does not support XIP from
   boot media. After programming the sbl and syfw, to program  both sbl_*_xip_entry_*.appimage
   and  sbl_*xip_test_*.xer5f.bin into OSPI flash, use the following uniflash commands

::

    For Windows:
    .\dslite.bat --mode processors -c COM9 -f <PDK>\packages\ti\boot\sbl\example\k3MulticoreApp\binary\am65xx\sbl_baremetal_boot_xip_entry_am65xx_evm_mcu1_0TestApp_release.appimage -d 3 -o A0000
    .\dslite.bat --mode processors -c COM9 -f <PDK>\packages\ti\boot\sbl\example\k3MulticoreApp\binary\am65xx\sbl_baremetal_boot_xip_test_am65xx_evm_mcu1_0TestApp_release.xer5f.bin -d 3 -o E0000


::

    For Linux:
    sudo ./dslite.sh --mode processors -c /dev/ttyUSB1 -f <PDK>/packages/ti/boot/sbl/example/k3MulticoreApp/binary/am65xx/sbl_baremetal_boot_xip_entry_am65xx_evm_mcu1_0TestApp_release.appimage -d 3 -o A0000
    sudo ./dslite.sh --mode processors -c /dev/ttyUSB1 -f <PDK>/packages/ti/boot/sbl/example/k3MulticoreApp/binary/am65xx/sbl_baremetal_boot_xip_test_am65xx_evm_mcu1_0TestApp_release.xer5f.bin -d 3 -o E0000



An example test log for sbl_*_boot_test_*_all_coresTestApp_release is
::

    SYSFW  ver xx.x.x-v20xx.xx (xxx xxx) running
    SBL Revision: xx.xx.xx.xx (MMM  DD YYYY - HH:MM:SS)
    MPU1_0 running
    MPU1_1 running
    MPU2_0 running
    MPU2_1 running
    MCU1_1 running
    MCU1_0 running
    MCU1_0 reports: All tests have passed

An example log for sbl_*_smp_test_*_all_coresTestApp_release.appimage is
::

    SYSFW  ver xx.x.x-v20xx.xx (xxx xxx) running
    SBL Revision: xx.xx.xx.xx (MMM  DD YYYY - HH:MM:SS)
    MPU SMP boot test
    Cores 0 & 1 will boot from 0x801007a0
    Cores 2 & 3 will boot from 0x803007a0
    Resetting all ARM cores now...
    No of Cortex-A core(s) running: 1
    No of Cortex-A core(s) running: 2
    No of Cortex-A core(s) running: 3
    No of Cortex-A core(s) running: 4
    All tests have passed

An example log for sbl_baremetal_boot_perf_*_mcu1_0TestApp_release.appimage, when the best boot time is reached is
::

    Time elapsed since start of SBL:     36665us
    fxn:boot_perf_test_main	cycles:  14666041

    Attempting board config ...BOARD_INIT_PLL ...passed
    BOARD_INIT_MODULE_CLOCK...passed
    BOARD_INIT_DDR...passed

    Analyzing run results ....
    Boot time is now optimized....
    All tests have passed

    Profiling info ....
    MCU @ 400000000Hz.
    cycles per usec  = 400
      fxn:                            main	line:  75	cycle:  xxx	timestamp:       432us
  					.
  					.
  					.
      fxn:               SBL_SlaveCoreBoot	line: 231	cycle:  xxx	timestamp:     36149us

The test log for sbl_*_xip_test_*.xer5f.bin is
::

    MCU1_0 running

Boot Modes
^^^^^^^^^^


The SBL supports MMCSD, OSPI, UART and Hyperflash Boot modes. The different boot modes
supported for all the boards is tabulated below.

+-----------------------+--------+------+------+------+------+------------+
|                       | MMCSD  | OSPI | UART | PCIe | ETH  | HYPERFLASH |
+-----------------------+--------+------+------+------+------+------------+
| AM65xx EVM            |  YES   | YES  | YES  |  NO  |  NO  |     NO     |
+-----------------------+--------+------+------+------+------+------------+
| AM65xx IDK            |  YES   | YES  | YES  |  NO  |  NO  |     NO     |
+-----------------------+--------+------+------+------+------+------------+
| J721E EVM             |  YES   | YES  | YES  |  NO  |  NO  |     YES    |
+-----------------------+--------+------+------+------+------+------------+

**Booting Via SD Card**

#. Preparing the SD card.
#. Booting the testcase from SD card.

**Preparing the SD card**

#. To boot the target the SD card should be bootable. Follow the steps
   at `Creating bootable SD card in
   windows <http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Creating_a_SD_Card_with_Windows>`__
   or `Creating bootable SD card in
   Linux <http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_create_SD_card_script>`__.
#. To update the SBL with a newer version, copy the sbl image (sbl_mmcsd_img_mcu1_0_release.tiimage) to the SD card.
   Rename it to **tiboot3.bin**
#. To update the SYSFW with a newer version, copy the system firmware image (sysfw.bin) to the SD card.
#. Copy the generated application image(\*.appimage) to the SD card. Rename it to
   **app**

**Booting the testcase  from SD card**

#. Insert SD card into the SD card slot of the board.
#. Refer Boot Modes section in the `AM6x EVM Hardware Users Guide
   <http://www.ti.com/lit/pdf/spruim7>`__  to setup EVM to boot from MMCSD.
#. Open a serial communication terminal like TeraTerm, MiniCom on host
   PC and connect to the MCU UART console port
#. Power cycle the board to boot the application from the SD card.
#. The test logs will be displayed on the MCU UART

**Booting Via OSPI flash**

#. `Programming the OSPI flash <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_board.html#uniflash>`__
#. Booting the testcase from OSPI flash


**Booting the testcase from OSPI flash**

#. Refer Boot Modes section in the `AM6x EVM Hardware Users Guide
   <http://www.ti.com/lit/pdf/spruim7>`__  to setup EVM to boot from OSPI.
#. Open a serial communication terminal like TeraTerm, MiniCom on host
   PC and connect to the MCU UART console port
#. Power cycle  the board to boot the application from the OSPI flash.
#. The test logs will be displayed on the MCU UART


**Booting the testcase from UART**

#. Refer Boot Modes section in the `AM6x EVM Hardware Users Guide
   <http://www.ti.com/lit/pdf/spruim7>`__  to setup EVM to boot from UART.
#. Open a serial communication terminal like TeraTerm, MiniCom on host
   PC and connect to the MCU UART console port
#. Power cycle the board, the console should show a sequence of CCC being printed
#. Choose the X-Modem interface and send the SBL that was built for UART. After the transfer is completed,
   repeat the same step for sysfw.bin and the application. You will see notifications to perform these
   actions.

.. warning::   If sysfw.bin is not present in the boot media, the boot will fail without displaying any
               logs on the MCU UART. SBL enables UART logging only after successfully starting the system
               firmware image. If the system firmware load fails, the RBL will eventually reset the system.


**Booting Via Hyperflash**

#. `Programming the Hyperflash <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_board.html#uniflash>`__
#. Booting the testcase from Hyperflashflash


**Booting the testcase from Hyperflash**

#. Refer Boot Modes section in the `J721E EVM Hardware Users Guide
   <https://cdds.ext.ti.com/ematrix/common/emxNavigator.jsp?objectId=28670.42872.4850.38306>`__
   to setup EVM to boot from Hyperflash.
#. Open a serial communication terminal like TeraTerm, MiniCom on host
   PC and connect to the MCU UART console port
#. Power cycle  the board to boot the application from the Hyperflash.
#. The test logs will be displayed on the MCU UART


EVM Setup for testing SBL
^^^^^^^^^^^^^^^^^^^^^^^^^^

For information on board specific requirements like power supply, UART console port
connections refer the Hardware User guide of the respective boards.

The configurations needed to setup UART console through a serial terminal 
application on host PC are listed in the next section.

**UART Console Setup**

PDK SBL prints messages on the UART Serial Console running on the host. Hence, a
serial terminal application (like Tera Term/HyperTerminal/minicom) should be
running on the host.

-  The host serial port must be configured at 115200 baud, no parity, 1  stop bit
   and no flow control.
-  Please ensure that the local echo setting for the terminal is turned  off.
-  All SBL prints are routed to the `MCU UART <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_how_to_guides.html#uart-connection>`__
-  To verify setup is correct, setup the EVM to boot from UART  as the Primary Boot
   Device(refer `AM6x EVM Hardware Users Guide <http://www.ti.com/lit/pdf/spruim7>`__.
   Power cycle the EVM, and look for the string CCCCCCC on the UART.

