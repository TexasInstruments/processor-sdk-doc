.. _index-faq:

############################
Frequently Asked Questions
############################

.. toctree::
   :maxdepth: 5

   index_faq

Processor SDK RTOS software is tested and validated on TI evaluation platforms that generally includes the superset part
in the device family however, the software components like CSL, LLD drivers and RTOS are applicable on reduced feature set
variant of the devices. Most of the code in the Processor SDK RTOS for multi-core devices is independent of how many cores
exists on the device as they provide baseline platform software that can be run from any core.

It is the users responsibility to modify components that deploy tasks/software on slave cores like OpenMP, OpenCL, IPC and MultiProc Manager
so that they use the feature set that is available on their device. In most cases software documentation will provide guidance on updating
the software package however this should not be considered a comprehensive list of software components to be updated
to run the software on a reduced feature set device variant.

Example: `Processor SDK RTOS porting guide for AM571x/AM570x Speed
Grades <http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Porting_Guide_for_AM571x/AM570x_Speed_Grades>`_

Features noted as “not supported,” in device datasheet must not be used. Their functionality is not supported by TI for this
family of devices. These features are subject to removal without notice on future device revisions. Any information regarding
the unsupported features has been retained in the documentation solely for the purpose of clarifying signal names or for consistency
with previous feature descriptions.

|

Training and Documentation
==========================

.. rubric:: Is there any training content available for Processor SDK
   RTOS?
   :name: is-there-any-training-content-available-for-processor-sdk-rtos

There are multiple Processor SDK RTOS training modules available online
as part of the `Processor SDK Training
Series <https://training.ti.com/processor-sdk-training-series>`__. Link
to the complete series or refer to the direct links below:

Training URLs:

-  `Processor SDK RTOS Overview Part
   I <https://training.ti.com/introduction-processor-sdk-rtos-part-1?cu=519268>`__
-  `Processor SDK RTOS Overview Part
   II <https://training.ti.com/introduction-processor-sdk-rtos-part-2?cu=519268>`__
-  `Application Development Using Processor SDK
   RTOS <https://training.ti.com/application-development-using-processor-sdk-rtos?cu=519268>`__

.. rubric:: What documentation exists for Processor SDK RTOS?
   :name: what-documentation-exists-for-processor-sdk-rtos

There are three main documents for Processor SDK RTOS:

-  :ref:`Getting Started Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>`
   Provides information on setting up software and running basic
   examples/demonstrations bundled within the Processor SDK.
-  :ref:`Software Developer
   Guide <rtos-index>`:
   Provides information on features, functions, delivery package, and
   compile tools for the Processor SDK RTOS release. This guide also
   provides detailed information regarding software elements and
   software infrastructure to allow developers to start creating
   applications.
-  :ref:`Migration Guide <RTOS-SDK-Migration-Guide-label>`: Provides
   migration information for applications built on top of the Processor
   SDK for RTOS.

|

Host and Target Setup
=====================

.. rubric:: How do I setup the build environment with custom Processor
   SDK RTOS and CCS Installation paths on the host machine?
   :name: how-do-i-setup-the-build-environment-with-custom-processor-sdk-rtos-and-ccs-installation-paths-on-the-host-machine

The steps to set up CCS and Processor SDK RTOS when the SDK or the IDE
is installed in a location other than the default location are described
below: `Processor SDK RTOS Setup with CCS <How_to_Guides.html#setup-ccs-for-evm-and-processor-sdk-rtos>`__.

A common gotcha while setting up the build environment is
compatibility with CCS version. Please refer to :ref:`Release
Notes <processor-sdk-rtos-release-notes>` for the
recommended version of CCS.

.. rubric:: Can I install multiple versions of the Processor SDK RTOS in
   the same folder?
   :name: can-i-install-multiple-versions-of-the-processor-sdk-rtos-in-the-same-folder

Typically, the version numbers of most components (PDK, Processor SDK,
BIOS, XDC, etc.) will be updated in the newer release. However there are
components like DSPLIB, IMGLIB, etc. and EDMA drivers that may remain
the same. The safe option would be to install the most current Processor
SDK in a custom location. You can have multiple versions of the SDK for
different devices on your machine and install all of them in custom
folders. For example, if you have a project with AM335x and AM437x that
requires you to download the Processor SDK RTOS for those device, we
recommend that you install them under different directories say
C:\\ti\\PRSDK_AM3x and C:\\ti\\PRSDK_AM4x

.. note::
   When you install the SDK in a custom location, there are few additional
   steps to follow:

   -  CCS auto-detects components only in C:\\ti path. So you will need to
      add the custom path to discovery as described in `Setup
      CCS <How_to_Guides.html#setup-ccs-for-evm-and-processor-sdk-rtos>`__.
   -  Assuming CCS is installed in the default path, the process to set the
      custom SDK path while building the SDK is provided in `Install in
      Custom Path <How_to_Guides.html#update-environment-when-installing-to-a-custom-path>`

.. rubric:: What are the typical flows for a new user to setup the
   Processor SDK RTOS development environment?
   :name: what-are-the-typical-flows-for-a-new-user-to-setup-the-processor-sdk-rtos-development-environment

The typical Processor SDK RTOS setup steps have been described below:

.. rubric:: Step 1: Basic Hardware, SDK, and IDE Setup
   :name: step-1-basic-hardware-sdk-and-ide-setup

Setup the software and hardware as described in the :ref:`Getting Started
Guide <Processor-SDK-RTOS-Getting-Started-Guide-label>`
At this stage, you should have the CCS IDE environment, the Processor
SDK RTOS installed and be able to connect to your target using an
emulator.

.. note::
   If you have installed CCS and/or the Processor SDK RTOS in a custom
   location, you need to manually add the SDK install path to CCS as
   described here
   `CCS_and_SDK_installed_in_different_directories <How_to_Guides.html#ccs-and-sdk-installed-in-different-directories>`__

.. rubric:: Step 2: Run the Out-of-Box Examples or Diagnostics
   :name: step-2-run-the-out-of-box-examples-or-diagnostics

The SDK and CCS ships with some pre-built out-of-box
demonstrations/examples that can be flashed on to the EVM, copied over
to an SD card, or loaded over emulator so that you can bring up and test
the EVM hardware. The steps to flash and run the out-of-box examples are
described here:

-  `Running_examples.2Fdemonstrations <Examples_and_Demonstrations.html#examples-and-demonstrations>`__

.. rubric:: Step 3: Build Environment Setup
   :name: step-3-build-environment-setup

Processor SDK RTOS provides a script to set up the Windows and Linux
environment with the component and compiler PATHs. Running the script
and rebuilding the Processor SDK from the root directory is described in
the wiki article `Setup build Environment <Overview.html#setup-environment>`.

.. note::

   -  The script assumes that CCS and Processor SDK RTOS are installed in
      the default location. If you have installed CCS and/or the Processor
      SDK RTOS in a custom location, then modify the setup file to the
      custom path. Please setup the environment using the steps described
      in the wiki article
      `Processor SDK RTOS Install in Custom Path <How_to_Guides.html#update-environment-when-installing-to-a-custom-path>`__
   -  After the script executes, it prints all the PATH macros set for the
      different variables. Be sure that the compiler and component paths
      have been setup correctly.


.. rubric:: Step 4: Rebuilding the SDK
   :name: step-4-rebuilding-the-sdk

The critical device-specific components of the Processor SDK RTOS can be
rebuilt from the top-level make file provided in the root directory
processor_sdk_rtos_x_xx_xx_xx. Invoking the build and available options
from top-level make files is described in the wiki article `Rebuilding
SDK
Components <Overview.html#top-level-makefile>`__.

.. note::
   The SDK offers command line build for all the components. CCS projects
   are only supported for DSP libraries and PDK driver examples.

.. rubric:: Step 5: Generate and Run Peripheral Driver Examples
   :name: step-5-generate-and-run-peripheral-driver-examples

The PDK component in Processor SDK RTOS provides drivers for different
IPs on the SOC and provides unit tests and examples for the drivers to
test them on a specific board/hardware. These examples do not ship with
pre-generated CCS projects and require users to generate a project
create script to generate the CCS project for the unit tests. The
procedure to generate the CCS projects for a given SOC is described in
this article
`PDK_Example_and_Test_Project_Creation <How_to_Guides.html#pdk-example-and-test-project-creation>`__.

.. rubric:: Step 6: Exploring Other Components in the SDK
   :name: step-6-exploring-other-components-in-the-sdk

The SDK package includes several other components that allow application
developers to develop software for multi-core devices. This includes an
inter-processor communication component known as (IPC). For SOCs that
contain an C66x DSP, the SDK provides several optimized DSP libraries
(DSPLIB, MATHLIB and IMGLIB). These components also ship with pre-built
examples that can be built using build steps described in their
documentation that is linked at the top level :ref:`Software Developer
Guide <rtos-index>`.

|

.. rubric:: How can I optimize the build time when rebuilding the
   Processor SDK RTOS ?
   :name: how-can-i-optimize-the-build-time-when-rebuilding-the-processor-sdk-rtos

Processor SDK RTOS top level build will rebuild IPC, all components
inside the PDK package for all supported cores and evaluation platforms.
Building all components can cause long build times. If you wish to only
rebuild a section of the package, the build times can be significantly
optimized if you invoke make for specific components in the SDK instead
of making all components. Also, for the PDK users can invoke the build
using the following syntax

::

    make LIMIT_BOARDS="<BOARD>" LIMIT_SOCS="<SOC>" LIMIT_CORES="<CORE>"

**SOC** can be am335x, am437x, am571x, am572x, k2g,k2h,k2e, etc.

**CORE** can be “a15_0”, “c66x”, or “ipu1_0”, for a15, c66, m4
respectively.

**BOARD** can be any evaluation hardware platform that your SOC
supports.

::

    For Example:
    make LIMIT_BOARDS="evmK2G iceK2G" LIMIT_SOCS="k2g" LIMIT_CORES="a15_0"
|

.. rubric:: Why am I not able to connect to the DSP core in CCS when
   Linux is booted on KeyStone II devices?
   :name: why-am-i-not-able-to-connect-to-the-dsp-core-in-ccs-when-linux-is-booted-on-keystone-ii-devices

The U-boot code that is booted before booting Linux puts the DSP core in
reset. In order to connect to the DSP, you need to run a GEL script in
CCS as described in this article
`Taking_the_C66x_Out_Of_Reset_with_Linux_Running_on_the_ARM_A15 <How_to_Guides.html#taking-the-c66x-out-of-reset-with-linux-running-on-the-arm-a15>`__.

.. rubric:: How can I create a SD card for Processor SDK RTOS?
   :name: how-can-i-create-a-sd-card-for-processor-sdk-rtos

Many of the TI-supported EVMs ship with an SD card with Linux Booting as
part of the EVM out-of-box experience. Users are required to create a
separate SD card if they want to boot their EVM with Processor SDK RTOS
out-of-box demonstrations or run board diagnostics. The procedure to
create an SD differs depending on whether you are doing this on a
Windows or Linux host machine, as described in the two articles shown
here:

-  `Create an SD card on Windows Host (AMx, K2G only) <Overview.html#windows-sd-card-creation-guide>`__

-  `Create an SD card on Linux Host (AMx, K2G only) <Overview.html#linux-sd-card-creation-guide>`__

.. rubric:: How can I restore the firmware on my EVM to factory
   settings?
   :name: how-can-i-restore-the-firmware-on-my-evm-to-factory-settings

Most of the Sitara EVMs ship with a bootable SD card that boots Linux.
To restore the EVM to factory settings, simply reflash the SD card with
the bootable image using the `SD Card Creation
Script <http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_create_SD_card_script>`__
provided in Processor SDK Linux.

For KeyStone Devices, the Processor SDK RTOS provides a `Program EVM
Script <How_to_Guides.html#default-binaries-and-setup>`__
with default binaries that reflash images on EEPROM, SPI, and/or NAND
(depending on the EVM platform used).

.. rubric:: Can I run Processor SDK RTOS on BeagleBone?
   :name: can-i-run-processor-sdk-rtos-on-beaglebone

Yes, Processor SDK RTOS software can be used to develop and run code on
BeagleBone platform. In order to test Processor SDK RTOS software on
BeagleBone, you will need to connect a JTAG to the BeagleBone. With the
default configuration of the board, we have observed that connecting a
JTAG causes a reset. Users need to follow the procedure provided here to
prevent a reset from occurring.

-  `Preventing a Reset When Connecting a JTAG on
   BeagleBone <http://elinux.org/Beagleboard:BeagleBone#Board_Reset_on_JTAG_Connect.28A3.2CA4.2CA5.29>`__

|

Device Drivers
==============

.. rubric:: How do I find out if a driver is supported in the package
   for my device?
   :name: how-do-i-find-out-if-a-driver-is-supported-in-the-package-for-my-device

For all SoC and board-specific driver support, we recommend that you
refer to the :ref:`Release Notes <RN-Supported-Platforms-label>`
corresponding to your release.

If you need further details for driver support on all cores on
heterogeneous multi-core devices, please reach out to the engineering
team using `E2E forums <http://e2e.ti.com/support/>`__.

.. rubric:: Where can I find example projects for device drivers?
   :name: where-can-i-find-example-projects-for-device-drivers

The PDK package in processor SDK RTOS does not contain pre-canned CCS
projects for driver examples. But it does provide scripts to set up the
development environment and create the example CCS projects based on
that setup. This allows the SDK the flexibility to create CCS projects
based on the user-specific host setup. In order to create the example
projects, users can follow the sequence provided below:

#. Users are required to setup their development environment using
   `Processor SDK RTOS Setup <Overview.html#setup-environment>`__
#. Setup the PDK build environment `PDK
   Setup <How_to_Guides.html#building-pdk-using-gmake-in-windows-environment>`__.
#. Execute the PdkProjectCreate script in ${PDK_INSTALL_PATH}/packages
   as described on the `PDK Example and Test Project Creation
   wiki <How_to_Guides.html#pdk-example-and-test-project-creation>`__

.. rubric:: What is the difference between SOC-specific driver library
   and the SOC-independent (Generic core-specific) driver library?
   :name: what-is-the-difference-between-soc-specific-driver-library-and-the-soc-independent-generic-core-specific-driver-library

Each low level driver (LLD) in the PDK package contains two versions of
the driver library. The naming conventions are as follows:

-  **Generic Core-specific Driver Library** :
   ti.drv.<module>.<core_specific_extension>

Example: ti.drv.gpio.aa15fg (A15 core-specific GPIO driver library)

-  **SOC-specific Driver Library**:
   ti.pdk.<module>.<soc>.<core_specific_extension>

Example: ti.drv.gpio.am572x.aa15fg (A15 GPIO driver library for AM572x)

When using the core-specific driver library, users are required to
provide SOC-specific driver initialization structures that provide
information regarding the module instance used, interrupt numbers,
configuration modes, etc.

The SOC-specific driver library contains a default configuration
(provided in <module>_soc.c file) built into the library that gets used
to initialize the driver on TI EVMs and to run sample applications
provided in driver package. It may need to be modified to suit for a
custom board and/or target application. The default configuration
includes a specific peripheral instance, interrupt configuration, etc.

.. rubric:: How to create ARM baremetal CCS project that link to PDK
   driver libraries using GNU Linker?
   :name: how-to-create-arm-baremetal-ccs-project-that-link-to-pdk-driver-libraries-using-gnu-linker

The static libraries in Platform development kit (PDK) drivers use the
convention ti.drv.<module>.a<ARM extension>. For example, the UART
driver library for A15 is named "ti.drv.uart.aa15fg". This is different
form the convention of naming the libraries with a suffix of "lib" and
extension ".a" which is generally the case for ARM compiler libraries
(e.g., librdimon.a, libgcc.a, libm.a). This is usually not an issue when
building applications using GCC compiler and make/gmake as libraries can
be linked using "-l" option. However, when building bare-metal (no-OS)
ARM projects in CCS, the IDE expects the libraries to have the name with
suffix "lib" and extension ".a". If developers try to link libraries
which does not follow this convention, they observe a linking error that
mentions that the library doesn`t exist. There are a couple of work
around options available to users when working with baremetal PDK driver
libraries:

**Option 1:** Add a colon in front of the library name when adding the
ARM driver library to "Build Settings"->"GNU Linker"->"Libraries" as
shown below:

.. Image:: ../images/Bare-metal_driver_link.png

**Option 2:** Add driver libraries using linker command file using the
INPUT syntax

::

    INPUT(
      "C:\ti\pdk_am335x_1_0_6\packages\ti\drv\gpio\lib\a8\release\ti.drv.gpio.profiling.aa8fg"
      "C:\ti\pdk_am335x_1_0_6\packages\ti\utils\profiling\lib\a8\release\ti.utils.profiling.aa8fg"
      "C:\ti\pdk_am335x_1_0_6\packages\ti\board\lib\icev2AM335x\a8\release\ti.board.aa8fg"
      "C:\ti\pdk_am335x_1_0_6\packages\ti\drv\i2c\lib\a8\release\ti.drv.i2c.aa8fg"
      "C:\ti\pdk_am335x_1_0_6\packages\ti\drv\uart\lib\a8\release\ti.drv.uart.aa8fg"
      "C:\ti\pdk_am335x_1_0_6\packages\ti\csl\lib\am335x\a8\release\ti.csl.aa8fg"
      "C:\ti\pdk_am335x_1_0_6\packages\ti\osal\lib\tirtos\a8\release\ti.osal.aa8fg"
    )

|

Chip Support Library (CSL)
==========================

.. rubric:: Are there any bare-metal examples in the PDK package?
   :name: are-there-any-bare-metal-examples-in-the-pdk-package

Customers who are wanting to start bare-metal code development can refer
to the diagnostics package which uses the PDK drivers and does not rely
on the TI RTOS. There are also CSL examples included in the package
under the path ${PDK_INSTALL_PATH}\\packages\\ti\\csl\\test.

In addition to CSL example, the PDK contains bare-metal diagnostic test
cases that help in testing EVM functionality. These can be located under
pdk_am57xx_x_x_x\\packages\\ti\\board\\diag

Some of the driver examples contain a flag for BARE METAL usage of the
driver. Example: GPIO/SPI already have these flags implemented.

.. rubric:: Can I read core-specific registers on multi-core devices
   supported in Processor SDK RTOS using CSL code?
   :name: can-i-read-core-specific-registers-on-multi-core-devices-supported-in-processor-sdk-rtos-using-csl-code

Yes, SDK provides CSL code to read core status and system configurations
using the CSL provided for specific core. For CSL code specific to cores
and peripherals present on your device, please refer to the header files
provided under ${PDK_INSTALL_PATH}\\packages\\ti\\csl\\src\\ip.

A good example of where you may need to access CSL code to read
core-specific information is on a multi-core device. You can have code
shared between multiple cores and would like to use a different code
path or internal buffer based on core ID. The CSL code helps you
implement this as follows:

For example, if you need to read the core ID on a multi-core DSP device:

::

     uint32_t coreNum;
     /* Get the core number. */
     coreNum = CSL_chipReadReg(CSL_CHIP_DNUM);

To do the same on the multi-core A15 device, you can use the following
code in the A15 CSL:

::

     unsigned int armNum;
     armNum = CSL_a15ReadCoreId(); //This gets the core ID using the MPIDR in the A15

.. rubric:: How do I find out which CSL header and source files apply to
   my device?
   :name: how-do-i-find-out-which-csl-header-and-source-files-apply-to-my-device

The CSL package that is part of the SDK is a unified CSL that covers all
devices supported by the Processor SDK RTOS. When you link to the CSL
library or include the header files for a specific IP, the CSL library
requires users to add a MACRO definition (-D SOC_XX####) to your build
to indicate which SOC you are using. In order to locate the IP files for
your device, always look at the header file at the top of the CSL
directory pdk_<device>_xx_xx_xx\\packages\\ti\\csl and the files that are
found under the SOC_XX#### corresponds to the SOC that you are using.

SOC-specific files can also be found under the
pdk_<device>_xx_xx_xx\\packages\\ti\\csl\\soc\\<device_name>

.. rubric:: What is the system memory map used by the SDK examples?
   :name: what-is-the-system-memory-map-used-by-the-sdk-examples

The TI RTOS-based examples included in the SDK rely on the platform
definitions provided inside bios_6_xx_xx_xx\\packages\\ti\\platforms for
partitioning the SOC memory between all the available cores on the SoC.
Please take a look at the snapshot below for AM572x:

::

    /*  Memory Map for ti.platforms.evmAM572X
     *
     *  Virtual     Physical        Size            Comment
     *  ------------------------------------------------------------------------
     *              8000_0000  1000_0000  ( 256 MB) External Memory
     *
     *  0000_0000 0 8000_0000        100  ( 256  B) --------
     *              8000_0100       FF00  ( ~64 KB) --------
     *  0000_0000   8001_0000        100  ( 256  B) --------
     *              8001_0100       FF00  ( ~64 KB) --------
     *  0000_0000   8002_0000        100  ( 256  B) --------
     *              8002_0100       FF00  ( ~64 KB) --------
     *  0000_0000   8003_0000        100  ( 256  B) --------
     *              8003_0100    FE_FF00  ( ~16 MB) --------
     *            1 8100_0000    40_0000  (   4 MB) --------
     *              8140_0000    C0_0000  (  12 MB) --------
     *            2 8200_0000    40_0000  (   4 MB) --------
     *              8240_0000    C0_0000  (  12 MB) --------
     *            3 8300_0000    40_0000  (   4 MB) --------
     *              8340_0000    C0_0000  (  12 MB) --------
     *            4 8400_0000    40_0000  (   4 MB) --------
     *              8440_0000    C0_0000  (  12 MB) --------
     *            5 8500_0000   100_0000  (  16 MB) --------
     *            6 8600_0000   100_0000  (  16 MB) --------
     *            7 8700_0000   100_0000  (  16 MB) --------
     *            8 8800_0000   100_0000  (  16 MB) --------
     *            9 8900_0000   100_0000  (  16 MB) --------
     *            A 8A00_0000    80_0000  (   8 MB) IPU1 (code, data), benelli
     *              8A80_0000    80_0000  (   8 MB) IPU2 (code, data), benelli
     *            B 8B00_0000   100_0000  (  16 MB) HOST (code, data)
     *            C 8C00_0000   100_0000  (  16 MB) DSP1 (code, data)
     *            D 8D00_0000   100_0000  (  16 MB) DSP2 (code, data)
     *            E 8E00_0000   100_0000  (  16 MB) SR_0 (ipc)
     *            F 8F00_0000   100_0000  (  16 MB) --------
     */

For bare-metal code, users are required to use a linker command file for
each of the cores and partition the memory manually so that there is no
memory overlap in the applications running on each of the cores. For
bare-metal linker command files, you can refer to the CCS templates for
`Hello World <Examples_and_Demonstrations.html#no-os-bare-metal-example>`__
or the linker command file used in the common folder of the the
diagnostics package.

|

Board Support
=============

.. rubric:: What steps are involved when creating a new custom board
   library?
   :name: what-steps-are-involved-when-creating-a-new-custom-board-library

The board library consolidates all the board-specific information so
that all the modifications made when moving to a new custom platform
using the SOC can be made in the source of this library. The following
steps are involved in creating custom board library:

-  **Modify SOC Clock Settings** The core clocks and module clocks used
   on the custom board library may vary based on the power requirements
   and external components used on the boards. TI provides `Clock Tree
   Tools <http://www.ti.com/tool/CLOCKTREETOOL>`__ to simulate the
   device clocks. We recommend that you test the settings in CCS by
   creating a GEL file with the modified settings before modifying the
   source in the board library.

-  **Modify SOC DDR:** The board library has the correct DDR
   initialization sequence to initialize the DDR memory on your board.
   You may need to make changes to the AC timings, hardware leveling,
   and DDR PHY configuration, some or all of which may be different than
   the TI supported platforms. We recommend that you test the settings
   in CCS by creating a GEL file with the modified settings before
   modifying the source in the board library.

Useful DDR Configuration Resources
-----------------------------------

+----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Sitara Resources:                                                                                                                | Keystone Resources:                                                  |
+==================================================================================================================================+======================================================================+
| `AM57x EMIF Tools <http://www.ti.com/lit/pdf/sprac36>`_                                                                          | `KeyStone II DDR Guide <http://www.ti.com/lit/pdf/sprabx7>`_         |
+----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| `AM437x DDR Configuration Guide <http://processors.wiki.ti.com/index.php/AM437x_DDR_Configuration_and_Programming_Guide>`_       | `KeyStone II DDR Debug Guide <http://www.ti.com/lit/pdf/sprac04>`_   |
+----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| `AM335x/AM11x EMIF ConfigurationTools <http://processors.wiki.ti.com/index.php/AM335x_EMIF_Configuration_tips>`_                 | `KeyStoneI DDR Initialization <http://www.ti.com/lit/pdf/sprabl2>`_  |
+----------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

-  **Modify SoC Pin Mux Settings.** The Pin Mux configuration for a
   particular platform is obtained by creating a .pinmux project for the
   device using the `TI Pin Mux
   Tools <http://www.ti.com/tool/PINMUXTOOL>`__ available on ti.com. The
   output of the tool can be plugged into the board library to modify
   the default configuration. The default baseline Pin Mux project
   (boardname.pinmux) is included in the board library for reference.

-  **Modify IO Instance and Configuration to Match Use Case:** If your
   custom board uses an IO instance different from the TI-supported
   board, the instance needs to be modified in the Pin Mux setup as well
   as in the board_cfg.h file in
   pdk_xx_Xx_xx_xx/packages/ti/board/src/<customBoardName>/

-  **Modify Files Corresponding to External Board Components:** The
   custom board may have external components (flash devices, Ethernet
   PHY, etc.) that are different from the components populated on the
   TI-supported EVM. These components and their support files need to be
   added to the
   pdk_xx_Xx_xx_xx/packages/ti/board/src/<customBoardName>/device path
   and linked as part of the board library build.

The above steps have been explained in detail in **Section 9** of the
**`Application Development Using Processor SDK RTOS
Training <http://training.ti.com/application-development-using-processor-sdk-rtos/index.html>`__**.
The slides talk about the different aspects of porting Processor SDK 3.0
to your custom platform, including incorporating custom Pin Mux,
clocking, peripheral instance, etc.

Adding custom board to the PDK directory structure and build setup is
described in the article
`Adding_Custom_Board_Library_Target_to_Processor_SDK_RTOS_makefiles <How_to_Guides.html#adding-custom-board-library-target-to-processor-sdk-rtos-makefiles>`__

.. note::
   TI evaluation platforms for Sitara Processors usually have board
   information stored in an EEPROM which checks for revision number and
   board name which is used to configure the board. When creating a custom
   platform if you don`t intend to use an EEPROM then we recommend removing
   code corresponding to Board_getIDInfo in your board library

.. rubric:: Do I need to do any post processing on PDK files generated
   by Pin Mux Utility?
   :name: do-i-need-to-do-any-post-processing-on-pdk-files-generated-by-pin-mux-utility

The Pin Mux utility is designed to automate the integration of a
custom-designed SOC pin map into the board library software. For AM335x,
AM437x, and K2G devices, the PDK files generated by the utility can be
integrated into the board library without any manual edits to the files.
For AM57x users, there are system design-level considerations that
require the user to manually select IO delay modes for specific
peripherals, which may require manual intervention before integrating
with the board library.

An example for modifying the Pin Mux in the board library to modify the
UART instance on AM335x is provided in the wiki article `Processor SDK
RTOS
Customization <http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Customization:_Modifying_Board_library_to_change_UART_instance_on_AM335x>`__.

**For More Information:** Refer to `Application Development Using
Processor SDK RTOS
Training <http://training.ti.com/application-development-using-processor-sdk-rtos/index.html>`__
and `Application Notes on AM57xx Pin Multiplexing
Utilities <http://www.ti.com/lit/pdf/sprac44>`__.

.. rubric:: How can I modify PLL settings in board libraries?
   :name: how-can-i-modify-pll-settings-in-board-libraries

The SOC board library in the PDK configures the SOC PLL and module clock
settings to the nominal settings required to be used with the TI
evaluation platform. If you want to use different clock settings due to
power consideration, or if you are using a variant of the device that
needs to be clocked differently, you can enter the PLL and clock
settings in the board library. All of the PLL and module clock settings
are consolidated in the following files:

-  <Board>.c: Contains calls related to all board-level initialization.
   <Board> refers to the evaluation platform (For example, evmam335x)
-  <EVM>_pll.c: Defines the Board_PLLInit() function that configures the
   dividers and multipliers for the clock tree.
-  <EVM>_clock.c: Defines clock dividers, scalars, and multipliers for
   individual board modules initialized using the board library.

.. rubric:: Can you provide an example of modifying a board library to
   use a different peripheral instance as compared to the EVM design?
   :name: can-you-provide-an-example-of-modifying-a-board-library-to-use-a-different-peripheral-instance-as-compared-to-the-evm-design

A good example of the steps involved in modifying a peripheral instance
is provided in the application note "`Processor SDK RTOS Customization:
Modifying UART
Instance <http://www.ti.com/lit/pdf/sprac32>`__"

|

Secondary Bootloader
====================

.. rubric:: What board initialization is required in the application
   after booting using the Secondary Boot Loader (SBL)?
   :name: what-board-initialization-is-required-in-the-application-after-booting-using-the-secondary-boot-loader-sbl

SBL calls the board library to set up the PLL clock, DDR, and Pin Mux,
and to power on target cores and the I/O peripheral from which it will
boot the application. Excluding those just mentioned, any other
configuration need to be done from the application code. As long as you
have added all of the device initialization to the board library, you
will not need to add any initialization code in the application.

.. note::
   For AM57xx devices, the AVS and ABB settings required for all core rails
   is added to the SBL code, as this initialization is required only in a
   production environment.


.. rubric:: Where do I locate flashing and boot utilities in the
   package?
   :name: where-do-i-locate-flashing-and-boot-utilities-in-the-package

The documentation for the booting and flashing of images to EVMs using
Processor SDK RTOS is provided from the wiki article :ref:`Processor SDK RTOS
Boot Documentation <FC-Boot-label>`

The :ref:`Boot and Flashing Utilities <FC-Boot-label>`
for all devices is located in the PDK package under the path
pdk_<device_name>_x_x_x\\packages\\ti\\boot\\sbl\\tools.

The SDK provides secondary bootloader code for all devices, which is
loaded by the ROM bootloader. The SBL is responsible for device
initialization, waking up secondary cores, and deployment of the
application code on different cores on multi-core devices. On single
core devices, the SBL is used to manage the device initialization, as
well as loading and running applications on the device.

Depending on the boot design you need to implement, the boot and
flashing tools that are used for formatting and booting the SBL can also
be leveraged to format and boot the application image directly. The
flash-writing utilities for different EVMs can be located under the path
pdk_<device_name>_x_x_x\\packages\\ti\\boot\\sbl\\tools\\flashWriter.

If the intent is to restore the KeyStone II EVM to factory settings,
then the `Program EVM Script <How_to_Guides.html#flash-bootable-images-c66x-k2h-k2e-k2l-only>`__
enables users to program the flash on the EVM using the pre-built
firmware images provided by TI/board manufacturer.

|

Diagnostics
===========

.. rubric:: How to I test my EVM functionality? Can I use the same tests
   on my custom platform?
   :name: how-to-i-test-my-evm-functionality-can-i-use-the-same-tests-on-my-custom-platform

The Processor SDK RTOS provides unit tests to test interfaces on the EVM
as part of diagnostics package that can be found in the package in the
path pdk_<device_namme>_x_x_x\\packages\\ti\\board\\diag. It also provides a
framework to run each of these tests through a command line serial
interface. Users can either load the tests using an emulator or they can
load them over an SD card to test the EVM functionality.

These tests, like all other examples in the SDK, rely on the board
library to perform the SOC and board initialization. So if you have
modified the board library to account for the components on your custom
hardware, then you should be able to re-use the diagnostic tests while
bringing up your custom hardware. Users will link to the new board
library and rebuild the diagnostics package to leverage these examples
on the custom hardware.

|

Filesystem Support
==================

.. rubric:: What filesystem support if provided by Processor SDK RTOS ?
   Can I use UBIFS, RAMFS, or FATFS with TI RTOS when using external
   non-volatile memory devices?
   :name: what-filesystem-support-if-provided-by-processor-sdk-rtos-can-i-use-ubifs-ramfs-or-fatfs-with-ti-rtos-when-using-external-non-volatile-memory-devices

Processor SDK RTOS only supports use of FATFS filesystem for some
devices. For availability of support for your devices check the :ref:`Release
Notes <processor-sdk-rtos-release-notes>`
There are numerous examples for using FATFS with USB driver and SD/MMC
driver in the SDK that you can use for reference. The FATFS-specific
documentation for Processor SDK RTOS is available in the `FATFS wiki
section of the Processor SDK RTOS <Device_Drivers.html#fatfs>`__.

|

TI RTOS
=======

Useful Resources
----------------

-  `SYSBIOS
   FAQ <http://processors.wiki.ti.com/index.php/SYS/BIOS_FAQs>`__
-  `Processor_SDK_RTOS:_TI_RTOS_Tips_And_Tricks <http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS:_TI_RTOS_Tips_And_Tricks>`__
-  `TI RTOS
   Worskshop <https://training.ti.com/ti-rtos-workshop-series>`__
-  `SYS/BIOS_with_GCC_(CortexA) <http://processors.wiki.ti.com/index.php/SYS/BIOS_with_GCC_(CortexA)>`__

|
.. rubric:: How do I start writing my TI RTOS application code? Is there
   any documentation that describes the process?
   :name: how-do-i-start-writing-my-ti-rtos-application-code-is-there-any-documentation-that-describes-the-process

The typical recommendation is to start a TI RTOS project using the
predefined templates provided as part of CCS installation and then add
custom configuration on top of it. CCS allows users to create a TI RTOS
project with Minimum, Typical, and a set of generic examples, as you can
see from wiki `Processor SDK RTOS TI RTOS Getting Started
Examples <index_overview.html#processor-sdk-rtos-getting-started-guide>`__.

Other than that, there is an TI RTOS workshop that addresses different
features and use cases of TI RTOS with CCS: `Introduction to the TI-RTOS
Kernel
Workshop <http://processors.wiki.ti.com/index.php/Introduction_to_the_TI-RTOS_Kernel_Workshop>`__

The TI RTOS component also ships with user documentation that provides
information on configuring TI RTOS through scripts APIs and also using
the graphical XGCONF tool. Full online API and module documentation is
available here: `TI RTOS API
Documentation <http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/sysbios/6_46_00_23/exports/bios_6_46_00_23/docs/cdoc/index.html>`__

.. rubric:: What interrupt latency, foot print, etc. can I expect while
   using TI RTOS?
   :name: what-interrupt-latency-foot-print-etc.-can-i-expect-while-using-ti-rtos

Performance and size benchmarks are available for every released
SYS/BIOS kernel in the TI RTOS package and are shipped as part of the
standard product documentation. In addition to the benchmark numbers
themselves, .pdf files provide a detailed description of how the
benchmarks were implemented. For example, whether they were implemented
in internal or external memory..

If you do not have access to a release, you can access the release notes
(and thereby the benchmarks) online by clicking on the following link
and going to the download link for the TI RTOS version that is part of
the SDK.

-  `SYS/BIOS
   Releases <http://software-dl.ti.com/dsps/dsps_public_sw/sdo_sb/targetcontent/bios/sysbios/index.html>`__

This link enables you to access any TI RTOS products and their
associated release notes. The release notes may be browsed directly.
There is no need to download the whole product. You will need to have a
my.ti login to access this site.

Within the SDK package, TI-RTOS Benchmark Documentation can be found
under directory path
*bios_6_xx_xx_xx\\packages\\ti\\sysbios\\benchmarks\\doc-files*

.. rubric:: How do I debug TI-RTOS and driver code?
   :name: how-do-i-debug-ti-rtos-and-driver-code

In order to single step through code, the driver libraries and the TI
RTOS libraries should be built with complete symbol definition.

For building a debug-able version of TI RTOS, please refer to the
following article:
`Making_a_debug-able_Custom_SYSBIOS_Library <http://processors.wiki.ti.com/index.php/SYS/BIOS_FAQs#1_Making_a_debug-able_Custom_SYS.2FBIOS_Library>`__

Processor SDK RTOS drivers are already built with full symbol
definition. So you should be able to single step into the drivers in the
CCS IDE environment. **Note**: You may need to add the source of the
SYS/BIOS and the drivers in the source search path in CCS.

Advanced debug of TI RTOS applications using system analyzer and ROV
object viewer is described in the `TI RTOS SYSTEM Anlayzer
wiki <http://processors.wiki.ti.com/index.php/How_is_SYS/BIOS_related_to_System_Analyzer%3F>`__.

|

.. rubric:: How can I run TI RTOS on secondary ARM cores on multi-core
   ARM devices
   :name: how-can-i-run-ti-rtos-on-secondary-arm-cores-on-multi-core-arm-devices

Processor SDK RTOS supports multiple device that have multi-core ARM
like AM572x and Keystone2 devices. In order to run TI RTOS application
on the secondary ARM core in non-SMP mode, application developers need
to add correct coreID to the configuration to their BIOS configuration
to allow the hardware interrupts to be routed to the secondary core.

For example on AM572x which has 2 A15 cores, to run the TI RTOS example
on secondary ARM core, application users need to add :

::

    var Core = xdc.useModule('ti.sysbios.family.arm.ducati.Core');
    Core.id = 1;

|

.. rubric:: Why do I get a "undefined reference to
   \`ti_sysbios_rts_gnu_ReentSupport_checkIfCorrectLibrary'" error when
   compiling my application?
   :name: why-do-i-get-a-undefined-reference-to-ti_sysbios_rts_gnu_reentsupport_checkifcorrectlibrary-error-when-compiling-my-application

You may have encountered this error when building an application for ARM
using makefile and not using CCS. You will need to link in the proper C
runtime library from SYS/BIOS. Double check the makefile(s) and make
sure that you are using libc, libgcc, libm, etc. from the SYS/BIOS
package and not from your toolchain (GCC Linaro).

For additional information, refer to: `What do I need to do to make the
C runtime library re-entrant when building SYS/BIOS applications for
Cortex-A GNU
targets <http://processors.wiki.ti.com/index.php/SYS/BIOS_with_GCC_(CortexA)#What_do_I_need_to_do_to_make_the_C_runtime_library_re-entrant_when_building_SYS.2FBIOS_applications_for_Cortex-A_GNU_targets.C2.A0.3F>`__

.. rubric:: Where do I post questions on generic TI RTOS?
   :name: where-do-i-post-questions-on-generic-ti-rtos

We recommend that all TI RTOS users review the list of TI RTOS
frequently asked questions on the `TI RTOS
FAQ <http://processors.wiki.ti.com/index.php/SYS/BIOS_FAQs>`__ page
prior to posting the questions on the E2E forum. If the question is not
specific to the Processor SDK RTOS drivers, but relates to configuration
of a specific module inside TI RTOS, then please post the questions on
the `TI RTOS E2E Forum <https://e2e.ti.com/support/embedded/tirtos/>`__.

.. rubric:: When load a RTOS example to DSP2, the code stuck at timer.c
   before go main(), but the same worked on DSP1?
   :name: when-load-a-rtos-example-to-dsp2-the-code-stuck-at-timer.c-before-go-main-but-the-same-worked-on-dsp1

By default, BIOS uses GPtimer5 to source the clock ticks in the BIOS
clock module. The GEL is created with the assumption that the DSP1
developers will use GPtimer5 and DSP2 users will use GPtimer6 to source
clock module. This means that DSP2 developers will need to add
configuration script to change the clock source to GPtimer6. Try to add
the following in your DSP2.cfg :

::

     var Clock = xdc.useModule('ti.sysbios.knl.Clock');
     Clock.timerId = 5; /* Change BIOS clock to GPTimer6 */

|

Networking Support
==================

.. rubric:: Can I use NDK software stack on all devices supported in
   Processor SDK RTOS?
   :name: can-i-use-ndk-software-stack-on-all-devices-supported-in-processor-sdk-rtos

The NDK software stack provided by TI typically requires a transport
layer called Network Interface Management Unit (NIMU) layer to interface
the underlying platform software elements and device drivers. Please
check the :ref:`Processor SDK RTOS Release Notes <processor-sdk-rtos-release-notes>`
for support of the NIMU transport driver to determine if NDK software
can be utilized on your device.

.. rubric:: Where do I find the documentation for the NDK stack?
   :name: where-do-i-find-the-documentation-for-the-ndk-stack

All the networking-related documentation for Processor SDK RTOS, along
with the NDK software stack, is linked from the wiki `NDK Documentation
and
References <http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_NDK#Additional_Documentation_References>`__.

|

Inter-processor Communication (IPC)
===================================

.. rubric:: How do I build and run IPC examples?
   :name: how-do-i-build-and-run-ipc-examples

IPC and corresponding examples are designed to be built from the top
level `Processor SDK RTOS IPC Make Target <Overview.html#additional-targets>`__.
Please ensure the `Processor SDK RTOS build <Overview.html#additional-targets>`__
environments have been set up before running the "make ipc_bios" or
[make ipc_examples] option.

The documentation to run the IPC examples is provided as part of
ReadMe.txt in the IPC examples or on a device-specific wiki article like
`How to Run AM57x IPC
Examples <How_to_Guides.html#run-ipc-examples-on-am572x>`__.

.. rubric:: Where can I locate IPC FAQ document?
   :name: where-can-i-locate-ipc-faq-document

For IPC-related questions, please refer to the `IPC FAQ wiki
article <http://processors.wiki.ti.com/index.php/IPC_3.x_FAQ>`__ that
consolidates the FAQ across all multi-core TI processors.

.. rubric:: How can I run TI RTOS IPC examples on AM57xx devices?
   :name: how-can-i-run-ti-rtos-ipc-examples-on-am57xx-devices

The instructions to run the IPC examples on AM57xx are provided in the
wiki article "`Running IPC Examples on
AM57xx/DRA7xx <How_to_Guides.html#run-ipc-examples-on-am572x>`__"

|

DSP-Optimized Libraries
=======================

.. rubric:: Why did I encounter a build issue while rebuilding DSPLIB,
   IMGLIB, or MATHLIB with C6000 CGT 8.x?
   :name: why-did-i-encounter-a-build-issue-while-rebuilding-dsplib-imglib-or-mathlib-with-c6000-cgt-8.x

This is a known issue. Please refer to the note provided on the
`Software Libraries
wiki <http://processors.wiki.ti.com/index.php/Software_libraries#Library_Object_File_Format>`__
to fix the issue.

.. rubric:: Why does the performance of the DSP Libraries not match with
   the performance in the documentation?
   :name: why-does-the-performance-of-the-dsp-libraries-not-match-with-the-performance-in-the-documentation

The performance documented in the optimized DSP libraries that are part
of the Processor SDK RTOS has been obtained using a C66x simulator
interface which only works with a flat memory model. In order to obtain
performance similar to the documentation, the user is expected to
perform the SOC-specific optimization. This includes placing the data
buffers in internal DSP memory, using optimized compiler settings in the
application code, enabling cache if buffers are in DDR memory, enabling
EDMA for moving data from external memory to L2, etc.

The CSL libraries for the SOC and TI RTOS provide APIs for cache
management of instruction memory as well as data memory. There are some
useful documents that enable benchmarking on the DSP and ARM cores.

-  `Introduction to DSP
   Optimization <http://www.ti.com/lit/pdf/sprabf2>`__
-  `TI portal for Core
   Benchmarking <http://www.ti.com/lsds/ti/processors/technology/benchmarks/core-benchmarks.page>`__
-  `TI DSP Benchmarking Application
   Report <http://www.ti.com/lit/pdf/sprac13>`__

|

EDMA Library
============

.. rubric:: How do I resolve EDMA instance usage conflict?
   :name: how-do-i-resolve-edma-instance-usage-conflict

There are several RTOS driver example projects using EDMA (e.g., PCIE,
SPI, UART, and MMCSD). These projects typically can run on A15, DSP, or
M4 cores. As a driver example, these projects use the first EDMA
instance (EDMA #0), assuming that no others are using it at the system
level.

There may be an issue if the EDMA instance #0 is already being used in
the system. For example, if the A15 core runs Linux and uses the EDMA #0
already, and a user wants to run a Processor SDK RTOS example on C66x
with default EDMA #0. To resolve such an issue, please choose an unused
instance. For example, EDMA #1 in the example.

.. rubric:: CCS 7.1 platform can't be verified warning
   :name: ccs-7.1-platform-cant-be-verified-warning

.. rubric:: When I use CCS 7.1 for Processor SDK RTOS 4.0 projects, I
   saw a warning "Platform name 'ti.platforms.xxxxxx' could not be
   verified. Your project may not build as expected."
   :name: when-i-use-ccs-7.1-for-processor-sdk-rtos-4.0-projects-i-saw-a-warning-platform-name-ti.platforms.xxxxxx-could-not-be-verified.-your-project-may-not-build-as-expected.

The warning shows in Properties---->General of a CCS project in CCS 7.1.
The warning is due to a change made in CCS 7.1, whereby the User
Interface tries to verify the project's target/platform name against a
list of known names and if it cannot be verified then it shows the
warning. The warning, in itself, does not necessarily mean that the
target-name is incorrect. Especially in this case where we are looking
at a known good project, it is likely showing up because the known
target-names list it is checking against is incomplete. Hence you can
treat the warning as harmless and ignore it. This causes some confusion
we have decided to remove the warning in the next release of CCS.

.. rubric:: Keystone I and II devices SGMII/MDIO/PHY
   :name: keystone-i-and-ii-devices-sgmiimdiophy

.. rubric:: How to setup SGMII interface to a PHY or to another SGMII
   port without using a PHY?
   :name: how-to-setup-sgmii-interface-to-a-phy-or-to-another-sgmii-port-without-using-a-phy

There are 3 SGMII connectivity modes: • SGMII port with PHY attached and
auto-negotiation enabled - for connecting to an external PHY • SGMII
master to SGMII device with auto-negotiation enabled - this is for
connecting two SGMII devices, one has to be set as master and the other
as device • SGMII port to SGMII port with forced link configuration –
generally this is used when one of the ports does not support
auto-negotiation

When a device having an SGMII MAC port is connected to a PHY device, the
SGMII MAC is the device in this link and the PHY is the master. The link
is established using auto-negotiation across the SGMII link that is
initiated by the master with an expected response by the device. If the
auto-negotiation is not initiated by the link master (PHY), the link
will remain down. In TI Keystone EVMs, the Processor with an SGMII MAC
port is connected to a PHY, which provides a copper interface to a
Gigabit RJ-45 connector. The Processor’s SGMII MAC port is configured as
a device with auto-negotiation enabled. This is done in the Init_SGMII().

When a SGMII MAC port is connected to another SGMII MAC port and
auto-negotiation is enabled, one must be configured to emulate a master
while the other is a device. The master port uses the MR_ADV_ABILITY
register to determine speed and duplex setting instead of the
MR_LP_ADV_ABILITY register.

Alternately, when an SGMII MAC port is connected to another SGMII MAC
port and auto-negotiation is not enabled, or not available, a “forced
link” can be established. Again, the MR_ADV_ABILITY register determines
the speed and duplex setting. Please refer to the TI KeyStone
Architecture Gigabit Ethernet (GbE) Switch Subsystem User Guide, section
3.3, SGMII_CONTROL, MR_ADV_ABILITY and MR_LP_ADV_ABILITY registers for
detail. The corresponding CSL code is implemented in
packages\\ti\\csl\\src\\ip\\sgmii\\Vx\\csl_cpsgmiiAux.h.

.. rubric:: In a TI SGMII to FPGA (PHY port) connection, data corruption
   is observed on egress direction, what could be the cause?
   :name: in-a-ti-sgmii-to-fpga-phy-port-connection-data-corruption-is-observed-on-egress-direction-what-could-be-the-cause

First to check if the FPGA side is a PHY port or 1000BASE-X media port.
There are many similarities but they are not identical. It is important
to recognize that from an electrical point of view, the SGMII interface
is very similar to the 1000BASE-X interface. Both use 8B/10B encoding, a
serial interface and an embedded clock. Systems can operate with SGMII
connected to a media port but they are not guaranteed to operate as they
are not consistent with the Ethernet standard.

Also, check Rx equalization. Some FPGA may have different choices of
robust mode (dynamic feedback equalization, aka DFE) or more basic mode
(linear equalizer). The DFE allows better compensation of transmission
channel losses by providing a closer adjustment of filter parameters
than when using a linear equalizer. However, a DFE cannot remove the
pre-cursor of a transmitted bit; it only compensates for the post
cursors. Try to use basic mode to see if it helps.

.. rubric:: How do I program the PHY through MDIO interface? I find that
   TI Init_MDIO() function is empty?
   :name: how-do-i-program-the-phy-through-mdio-interface-i-find-that-ti-init_mdio-function-is-empty

For some TI EVMs, Init_MDIO() is empty because that PHY is configured
using pin strapping and no MDIO control is needed to enable it to
operate through auto-negotiation in the optimum configuration. Sample
CSL code to access PHY via MDIO can be found under
packages\\ti\\csl\\src\\ip\\mdio\\Vx\\csl_mdioAux.h. The MDIO user access
register is used to communicate with the physical transceiver connected
to the MDIO bus, not to a register of the Keystone SOC MDIO itself. The
code must be customized for what you want to get or set within the PHY.
To do this you must set the correct PHY address and then identify PHY
register that you want to access. Those registers are defined in the PHY
datasheet, not TI Keystone documents.

After PHY is programmed, the MDIO controller will continue polling the
PHY periodically for status. The PHY Alive Status Register (ALIVE) and
PHY Link Status Register (LINK) can be read to monitor this status of
the PHY and link (please refer to the TI KeyStone Architecture Gigabit
Ethernet (GbE) Switch Subsystem User Guide, section 3.4).

DMSC/SYSFW
==========

Questions and answers found in this section expand on information found in the
`System Firmware Public Documentation
<http://software-dl.ti.com/tisci/esd/latest/1_intro/index.html>`__

.. rubric:: How do I configure the AM65x MMU to preemptively restrict write
   access to memory regions protected by SYSFW controlled firewalls?

Device Management & Security Controller (DMSC) uses device firewalls
to prevent applications from directly manipulating non-real-time registers.  The
MMU can optionally be used to mimic the firewall access restrictions enforced by
DMSC.  Programming the MMU in such a manner allows applications to be compatible
with firewall configurations whether or not DMSC firewall support is enabled.
Therefore, it is highly recommended that applications configure the MMU to
prevent write accesses to these regions as detailed below.

The recommendation to keep MMU configuration as restrictive (or more
restrictive) than the firewalls always stands as the MMU will give a
precise exception at the time the offending instruction is executed. The
firewall will give an imprecise data abort that will happen some time after
the offending memory access lands.

The following table describes all AM65x MMR regions which must be
configured for read only using the MMU.

+------------------------+------------+------------+------------+---------------+--------------+
| IP Block               | MMR Region | Start      | End        | MMU Page      | MMU Page     |
|                        | Name       | Address    | Address    | Start Address | End Address  |
+========================+============+============+============+===============+==============+
| MCU Navigator UDMASS   | cfg        | 0x283C0000 | 0x283C001F | 0x00283C0000  | 0x00283D0000 |
| Interrupt Aggregator   |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator UDMAP   | rflow      | 0x28400000 | 0x28401FFF | 0x0028400000  | 0x0028410000 |
+------------------------+------------+------------+------------+---------------+--------------+
| MCU Navigator Ring     | cfg        | 0x28440000 | 0x2847FFFF | 0x0028440000  | 0x0028450000 |
| Accelerator            |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+
| MCU Navigator UDMASS   | gcntcfg    | 0x28480000 | 0x28481FFF | 0x0028480000  | 0x0028490000 |
| Interrupt Aggregator   |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator UDMAP   | tchan      | 0x284A0000 | 0x284A3FFF | 0x00284A0000  | 0x00284B0000 |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator UDMAP   | rchan      | 0x284C0000 | 0x284C3FFF | 0x00284C0000  | 0x00284D0000 |
+------------------------+------------+------------+------------+---------------+--------------+
| MCU Navigator UDMASS   | imap       | 0x28560000 | 0x2856FFFF | 0x0028560000  | 0x0028570000 |
| Interrupt Aggregator   |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+
| MCU Navigator UDMASS   | l2g        | 0x28570000 | 0x2857007F | 0x0028570000  | 0x0028580000 |
| Interrupt Aggregator   |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+
| MCU Navigator UDMASS   | mcast      | 0x28580000 | 0x28580FFF | 0x0028580000  | 0x0028590000 |
| Interrupt Aggregator   |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator UDMAP   | gcfg       | 0x285C0000 | 0x285C00FF | 0x00285C0000  | 0x00285D0000 |
+------------------------+------------+------------+------------+---------------+--------------+
| MCU Navigator Ring     | gcfg       | 0x285D0000 | 0x285D03FF | 0x00285D0000  | 0x00285E0000 |
| Accelerator            |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator MODSS   | cfg        | 0x30800000 | 0x3080001F | 0x0030800000  | 0x0030810000 |
| Interrupt Aggregator 0 |            |            |            |               |              |
+------------------------+------------+------------+------------+               |              +
| Main Navigator MODSS   | cfg        | 0x30801000 | 0x3080101F |               |              |
| Interrupt Aggregator 1 |            |            |            |               |              |
+------------------------+------------+------------+------------+               |              +
| Main Navigator UDMASS  | cfg        | 0x30802000 | 0x3080201F |               |              |
| Interrupt Aggregator   |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator MODSS   | imap       | 0x30900000 | 0x30907FFF | 0x0030900000  | 0x0030910000 |
| Interrupt Aggregator 0 |            |            |            |               |              |
+------------------------+------------+------------+------------+               |              +
| Main Navigator MODSS   | imap       | 0x30908000 | 0x3090FFFF |               |              |
| Interrupt Aggregator 1 |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator UDMASS  | imap       | 0x30940000 | 0x3097FFFF | 0x0030940000  | 0x0030950000 |
| Interrupt Aggregator   |            |            |            |               |              |
+                        +            +            +            +---------------+--------------+
|                        |            |            |            | 0x0030950000  | 0x0030960000 |
+                        +            +            +            +---------------+--------------+
|                        |            |            |            | 0x0030960000  | 0x0030970000 |
+                        +            +            +            +---------------+--------------+
|                        |            |            |            | 0x0030970000  | 0x0030980000 |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator         | tchan      | 0x30B00000 | 0x30B0FFFF | 0x0030B00000  | 0x0030B10000 |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator         | rchan      | 0x30C00000 | 0x30C0FFFF | 0x0030C00000  | 0x0030C10000 |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator         | rflow      | 0x30D00000 | 0x30D07fff | 0x0030D00000  | 0x0030D10000 |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator UDMASS  | gcntcfg    | 0x31040000 | 0x31043FFF | 0x0031040000  | 0x0031050000 |
| Interrupt Aggregator   |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator Ring    | cfg        | 0x31080000 | 0x310BFFFF | 0x0031080000  | 0x0031090000 |
| Accelerator            |            |            |            |               |              |
+                        +            +            +            +---------------+--------------+
|                        |            |            |            | 0x0031090000  | 0x00310A0000 |
+                        +            +            +            +---------------+--------------+
|                        |            |            |            | 0x00310A0000  | 0x00310B0000 |
+                        +            +            +            +---------------+--------------+
|                        |            |            |            | 0x00310B0000  | 0x00310C0000 |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator UDMASS  | l2g        | 0x3110007F | 0x3110007F | 0x0031100000  | 0x0031110000 |
| Interrupt Aggregator   |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator UDMASS  | mcast      | 0x31110000 | 0x31113FFF | 0x0031110000  | 0x0031120000 |
| Interrupt Aggregator   |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator UDMAP   | gcfg       | 0x31150000 | 0x311500FF | 0x0031150000  | 0x0031160000 |
+------------------------+------------+------------+------------+---------------+--------------+
| Main Navigator Ring    | gcfg       | 0x31160000 | 0x311603FF | 0x0031160000  | 0x0031170000 |
| Accelerator            |            |            |            |               |              |
+------------------------+------------+------------+------------+---------------+--------------+

.. rubric:: What AM65x memory areas are reserved for use by DMSC?

DMSC reserves a portion of the AM65x MSMC memory for the communication path
between itself and the A53.  Applications must not use the reserved region of
MSMC or communication with DMSC will be compromised.

The size of the MSMC region used by DMSC is both configurable and discoverable.
The size of the region can be configured through the DMSC board configuration's
`msmc_cache_size parameter
<http://software-dl.ti.com/tisci/esd/latest/3_boardcfg/BOARDCFG.html#design-for-boardcfg-msmc>`__.
The useable MSMC memory after DMSC reservations can be discovered by sending
the `TISCI_MSG_QUERY_MSMC message
<http://software-dl.ti.com/tisci/esd/latest/2_tisci_msgs/general/core.html#tisci-msg-query-msmc>`__
to DMSC.  The message response contains the range of MSMC memory useable by the
application.

|

SMP Examples
============

.. rubric:: How do I load SMP enabled example into target through CCS ?
   :name: how-do-i-load-smp-enabled-example-into-target-through-ccs

Symmetric Multi Processing requires a different approach to load
the application into target board through CCS. The detailed documentation on loading
and debugging the SMP enabled example is linked `here
<http://software-dl.ti.com/ccs/esd/documents/ccs_smp-debug.html>`__.
