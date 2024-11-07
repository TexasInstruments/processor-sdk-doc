.. http://processors.wiki.ti.com/index.php/MCSDK_to_Processor_SDK_Migration

MCSDK to Processor SDK Migration Guide
=======================================

.. rubric:: Introduction

For many years, the MCSDK has been a great way to get started with
Embedded Software development on TI's KeyStone architecture processors
(C66x, K2x). If you go by "what's in a name?", you can easily see the
connection. The "MC" of MCSDK stands for Multi-Core and The "SDK" refers
to Software Development Kit. The MCSDK encapsulated a collection of
software elements and tools and was designed to provide a great starting
point for developing embedded applications on ARM running Linux and C66x
cores running TI-RTOS, on KeyStone processors. One of the goals of the
MCSDK was to enable a developer to quickly explore and evaluate the
possibilities as well as start development on a customized Linux/TI-RTOS
software platform.

Like the Linux kernel itself, which evolves every 77 days or so with a
new release, it's time for the MCSDK to evolve, without departing from
it's heritage. TI has a rich offering of microprocessors from multicore
ARMs to tiny, power-efficient DSPs, and different combinations of ARM,
DSP, and specialized cores to provide the broad market a variety of
solutions. Since many developers will touch several of these devices
from project to project, it is beneficial to standardize the experience
to maximize the benefit of learning. The limited time developers have in
today's time-to-market driven environment is very important and
shouldn't be wasted.

To this end, the KeyStone devices will be actively supported in the
Processor SDK, the unified SDK for TI processors. This allows suport for
both C66x and K2x in the same SDK, as well as the other AMx processor.
Each developer that uses the Processor SDK from project to project can
leverage that experience and know with confidence what they can expect.
The Processor SDK is more than a collection of components, the aim is
that applications can switch processors with minimal modifications.

Further, we are seeing different use cases for Linux and RTOS:

-  A fully RTOS based solution with RTOS on Cortex-A cores in addition
   to the C66/M4 cores and
-  Linux based solutions that need acceleration, but doesn't really need
   to get into the programming details of the non Cortex-A cores, and
   would just need open programming paradigms such as OpenCL, OpenGL,
   GStreamer to accelerate the Linux applications, leveraging TI's
   optimized libraries or codecs
-  A heterogenous solution of Coretex-A cores running Linux and C66/M4
   cores running RTOS

To this end, the Processor SDK is split into Processor SDK for RTOS and
Processor SDK for Linux.

To further customize the experience for developers who typically work on
one device we split the SDK to be a separate installer per device, per
OS. In summary, the contents of MCSDK is now split into Processor SDK
(Linux, RTOS) for K2H/K2K, K2E, and K2L. The devices without ARM
processors, C665x and C667x, only support RTOS. With this background in
place, let's dig into more specifics.

Processor-SDK 2.0.1 adds support for KeyStone devices from previous SDKs
that are no longer being maintained:

-  **MCSDK**: K2H, K2K, K2E, K2L *(last release: MCSDK 3.1.4)*
-  **BIOS-MCSDK**: C665x, C667x *(last release: BIOS-MCSDK 2.1.2)*

If you are migrating from these SDKs, the notes below will highlight any
changes that are required.

|

.. rubric:: Installation
   :name: installation

As with MCSDK, Processor SDK is also available as an installer on ti.com
for download.

.. rubric:: Target Machine
   :name: target-machine-mcsdk-to-procsdk

The Processor SDK Linux installer is available only for host machines
running Linux, where as the Processor SDK RTOS installer is available
for both Windows and Linux host machines. Please note that the Processor
SDK Linux Installer can be installed only on 64-bit host machines and
the support for 32-bit machines is dropped, primarily due to the Linaro
toolchain not supporting 32-bit anymore.

.. rubric:: Install Packages
   :name: install-packages

As noted earlier, the installer is now available per device, per OS. If
you work on multiple devices or work on both RTOS and Linux, you'd have
to download multiple installers.

.. rubric:: Command Line Installation
   :name: command-line-installation

The tool to create the installer was changed from *InstallJammer*, which
was an unsupported open source project, to *InstallBuilder*. If
installing on the command line without any user interaction, the command
option changed from

::

     --prefix [INSTALL_PATH] --mode unattended

to

::

     --prefix [INSTALL_PATH] --mode silent

.. rubric:: Processor SDK Linux

This chapter describes what's changed from a Linux point of view, when
migrating from MCSDK to Processor SDK

.. rubric:: Directory Structure
   :name: directory-structure-mcsdk-to-procsdk

In addition to the pre-built images and the filesystem, the installer
now contains a copy of the Linux Kernel and U-Boot GIT repositories, and
the sources for Kernel Modules, which'll be quite handy for reference or
further development. There are additional helper/setup scripts to help
with getting started with the EVMs. For an overview of the directory
structure and a brief description of the contents of the folders, refer
to
`Processor\_SDK\_Linux\_Directory\_Structure
<Overview_Directory_Structure_Overview.html>`__.

.. rubric:: Getting Started
   :name: getting-started

The Getting Started Guide for Processor SDK Linux is
`here <Overview_Getting_Started_Guide.html>`__
Processor SDK Linux includes a set up script that scripts the necessary
steps to setup the development environment on the host machine. The
setup script verifies that the Linux host is the recommended Ubuntu LTS
version, installs any required host packages, sets up the target
FileSystem installation, NFS setup, TFTP setup, Minicom setup, uboot
setup, Load uboot script and boots the EVM to Linux Prompt. After
installation of the SDK on the Linux host, the setup script should be
run to prepare the host for software development. Some of the tasks
require administrator privileges. The script will prompt you when these
administrator privileges are required. For more details, see
`Processor\_SDK\_Linux\_Setup\_Script
<Overview_Getting_Started_Guide.html#run-setup-scripts>`__.

The procedure to flash the U-Boot, Kernel and filesystem into the flash
memory on EVM, also known-as program\_evm, is still available, and
documented
`here <Overview_Getting_Started_Guide.html#program-evm-user-guide>`__.

.. rubric:: U-Boot
   :name: u-boot-mcsdk-to-procsdk

U-Boot is upgraded to be based on 2015.07. Listed below are a few major
differences from MCSDK.

-  To Flash u-boot image onto NOR flash, u-boot upgrade command is
   changed from burn\_uboot to burn\_uboot\_spi (for SPI NOR boot) and
   burn\_uboot\_nand (for NAND boot)
-  U-Boot starting address is now at 0x0c00 0000 instead of 0x0c00 1000
   in MCSDK
-  bootz is enabled in u-boot. So use zImage instead of uImage
-  Following default env variable have been updated.

   -  **name\_mon** from skern-<soc>-evm.bin to skern-<soc>.bin
   -  **name\_fdt** from uImage-<soc>-evm.dtb to <soc>-evm.dtb
   -  **name\_kern** from keystone-evm.bin to zImage
   -  **debug\_options** to **ks2\_debug**. This is set to 1 as before
      to allow CCS to be connected to DSP core. When the device boots to
      Linux, the DSP needs to be loaded with the image and run using
      mpmcl command first before the CCS can be connected to DSP cores.
      The ks2\_debug is not needed in this case.

-  Following new env variables are introduced to allow use of a firmware
   initramfs image so that Linux drivers that requires firmware can get
   it from this before rootfs is mounted during the boot up. This is
   needed to support NFS for example.

   -  **name\_fw\_rd** is set to k2-fw-initrd.cpio.gz - This image is
      supplied in the release package and contains K2 SerDes and QMSS
      Accumulator firmwares that are required by NetCP and PCIe drivers
   -  init scripts are modified to include this firmware during boot and
      pass it to kernel using 2nd argument of bootz command.

-  A copy of Kernel GIT repo is included in the "board-support" folder
   of the Processor SDK Installation
-  For more details, refer to the :ref:`Processor SDK Linux U-Boot Release Notes
   <u-boot-release-notes>`

.. rubric:: Linux Kernel
   :name: linux-kernel-mcsdk-to-procsdk

The Linux Kernel is upgraded to 4.1 (2015 LTS). Listed below are a few
major differences from MCSDK (3.10 Kernel).

-  Firmware is now not built into the Kernel. Instead they are available
   in the k2-fw-initrd.cpio.gz initramfs which are passed from u-boot to
   kernel as part of the bootz command for drivers that requires them
   very early in the boot up before the final rootfs is available.
-  Other firmwares that are used by dynamic modules are available in
   lib/firmware folder of the supplied file system images (for ubifs,
   initramfs etc) so that they are loaded and used by the driver from
   the user space.
-  A copy of Kernel GIT repo is included in the "board-support" folder
   of the Processor SDK Installation
-  For more details, refer to the
   `Processor\_SDK\_Linux\_Kernel\_Release\_Notes <Foundational_Components_Kernel_Release_Notes.html>`__
   and
   `Processor\_SDK\_Linux\_Kernel\_Performance\_Guide <Release_Specific_Performance_Guide.html>`__

.. rubric:: Roadmap
   :name: roadmap

Following features supported in MCSDK are not supported in Processor SDK
02.00.02 Release, and will get added in future Processor SDK releases

-  Drivers: UDMA, 10G-KR firmware, IPSec inflow, kexec, network bonding

|

.. rubric:: Kernel Drivers
   :name: kernel-drivers

Listed below are a few major differences from MCSDK (3.10 Kernel).

.. rubric:: NetCP Drivers
   :name: netcp-drivers

-  Netcp qmss and pkt dma drivers at drivers/soc/ti
-  In older kernel, firmwares used to be built into the kernel as an
   ihex file which is not right thing to do due to licensing issues. Per
   community accepted practice, the right thing to do is to have the
   firmware images in a file system and use request\_firmware() API in
   kernel to load it from the file system and use. So with this kernel
   release, this is how firmware files are used in kernel drivers.
-  The Accumulator channels requires the QMSS Accumulator firmware
   (ks2\_qmss\_pdsp\_acc48.bin) that is located in the
   k2-fw-initrd.cpio.gz.
-  Netcp net driver at the same location as before at
   drivers/net/ethernet/ti/, but files are renamed with netcp\_ prefix
-  DT documentation for the above drivers is under
   Documentation/devicetree/bindings/ folder.
-  PA firmwares are now part of the k2-fw-initrd.cpio.g image that is
   used for early boot. PA firmwares in Linux includes a header +
   Firmware bloab from the PA LLD package. See kernel source directory
   Documentation/arm/keystone/netcp-pa.txt for details of the header
   format.
-  Sysfs command file name paths have changed in this release. Please
   refer the NetCP User Guide for details.
-  QoS firmware is part of k2-fw-initrd.cpio.gz.
-  QoS qmss driver is implemented in drivers/soc/ti/knav\_qmss\_qos.c.
-  Cpts driver for Keystone is implemented in
   drivers/net/ethernet/ti/netcp\_cpts.c, which corresponds to the
   cpts.c in MCSDK release.
-  Keystone sideband crypto driver uses the firmware file: sa\_mci.fw
   which is different from that on older kernels. In older kernel, there
   is an array named sa\_eng\_aes\_enc\_mci\_tbl, which contains a set
   of micro instructions per algorithm for the SA hardware. This is now
   captured in a firmware file called sa\_mci.fw and used in the driver.
-  Multicast filters for special handling of multicast packets to avoid
   duplication are now not enabled through DT as in MCSDK. Instead a
   sysfs entry is provided for the same. See
   Documentation/networking/keystone-netcp.txt for details.

.. rubric:: K2 SerDes drivers
   :name: k2-serdes-drivers

-  K2 SerDes driver is located at drivers/phy/phy-keystone-serdes.c. It
   supports 3 serdes modes. PCIe, 1G and 10G.
-  The following firmwares are required for proper functioning of the
   driver:

   -  ks2\_gbe\_serdes.bin - for 1G
   -  ks2\_xgbe\_serdes.bin - for 10G
   -  ks2\_pcie\_serdes.bin - for PCIe

-  These firmwares have configuration values which otherwise were
   embedded in the driver code in v3.10.x based kernel releases
-  These firmwares are available in the file systems and
   k2-fw-initrd.cpio.gz file supplied in the release package and
   referred in the u-boot section of this document

|

.. rubric:: PCIe driver
   :name: pcie-driver

-  PCIe RC mode was set in Kernel in MCSDK but moved to U-boot in
   ProcSDK for upstreaming reason. U-boot needs to be the same release
   version as Kernel. If not, PCIe mode initialization needs to be added
   in the older version of u-boot.


.. rubric:: Building the Linux SDK
   :name: building-the-linux-sdk-mcsdk-to-procsdk

As with MCSDK, the Processor SDK Linux can be fully assembled from
sources, via Yocto. This gives the ability for customers to easily add
or remove components from the default filesystem(s) provided in the
Processor SDK Linux Installer. The instructions on how to build the
Processor SDK Linux are available
`here <Overview_Building_the_SDK.html>`__

|

.. rubric:: Processor SDK RTOS

.. rubric:: Directory Structure
   :name: directory-structure-1

Information on the Processor-SDK RTOS directory structre is
`here <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_overview.html?highlight=directory%20structure#directory-structure>`__.
Some modifications were made to be consistent across all devices:

C66x

-  **SDK folder** is per device. So, there is one for C665x and one for
   C667x.
-  **IBL**, **POST**, and **boot utilities** moved from SDK folder
   ``tools`` to PDK folder ``packages/ti/boot``
-  **NDK examples** moved from SDK folder ``examples/ndk`` to PDK folder
   ``packages/ti/transport/ndk/nimu/example``
-  **program\_evm** flash utility moved from SDK folder
   ``tools/program_evm`` to SDK folder ``bin``

K2x

-  **SDK and PDK folders** are per device. So, there are separate ones
   for K2E, K2H/K2K, and K2L.
-  **NDK examples** moved from SDK folder ``examples/ndk`` to PDK folder
   ``packages/ti/transport/ndk/nimu/example``

.. rubric:: Getting Started
   :name: getting-started-1

The Processor-SDK RTOS Getting Started Guide is located
`here <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_overview.html>`__.
As in MCSDK, this is the page to quickly find links for software and
information on setting up hardware. Further information can be found in
the `Developer
Guide <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index.html>`__.
This will look different from the MCSDK documentation since we are now
focusing on how to use the SDK software to quickly create an embedded
application rather than the design of the software.

.. rubric:: Migration from MCSDK (K2x)
   :name: migration-from-mcsdk-k2x

.. rubric:: CSL
   :name: csl

-  Renamed “ti/csl/device” folder to “ti/csl/soc” – hence any include
   header files as “ti/csl/device/k2?/src/xxxx.h” needs to be changed to
   “ti/csl/soc/k2?/src/xxxx.h”
-  One top level include header files per IP replaces multiple CSL files
   per IP for the following :

   -  <ti/csl/cslr\_bcp.h>, <ti/csl/cslr\_iqn2.h>, <ti/csl/csl\_rac.h>,
      <ti/csl/csl\_tac2.h>, <ti/csl/cslr\_aif2.h> and
      <ti/csl/cslr\_pcie.h>

-  Deprecated top level cslr\_cpsw\_5gf.h files - applications including
   csl 5gf header files would need to migrate to include
   <ti/csl/csl\_cpsw.h> file.

.. rubric:: Migration from BIOS-MCSDK (C66x)
   :name: migration-from-bios-mcsdk-c66x

.. rubric:: CSL
   :name: csl-1

-  Following SoC defines are added to support C6657 and C6678 in the
   CSL.

   -  SOC\_C6657 SOC\_C6678

-  following files are not supported from the top level CSL folder
   (ti/csl)

   -  csl\_mpuAux.h, csl\_memprot.h, csl\_memprotAux.h, csl\_pllcAux.h,
      csl\_cp\_tracer.h

-  include file changes

   -  Instead of <ti/csl/csl\_cpsw\_3gfAux.h> , <ti/csl/csl\_cpswAux.h>
      should be included
   -  Instead of <ti/csl/csl\_cpsw\_3gfssAux.h>,
      <ti/csl/csl(r)\_cpsw\_ss\_s.h> should be included
   -  Instead of <ti/csl/cslr\_pcie\*.h> needs to be changed to include
      cslr\_pcie.h
   -  Instead of <ti/csl/cslr\_sgmii.h>, <ti/csl/csl\_sgmii.h> include
      <ti/csl/cslr\_cpsgmii.h> and <ti/csl/csl\_cpsgmii.h> respectively.
   -  Instead of <ti/csl/csl(r)\_cpsw\_3gf\*.h> include
      <ti/csl/csl(r)\_cpsw.h>

.. raw:: html

   <div
   style="margin: 5px; padding: 2px 10px; background-color: #ecffff; border-left: 5px solid #3399ff;">

**NOTE**
Please define appropriate SOC define in the applicatoin when using the
CSL. E.g., SOC\_C6678 or SOC\_C6657 for c6678 and c6657 devices.

.. raw:: html

   </div>

.. rubric:: CPPI
   :name: cppi

-  Interface with Resource Management (RM) LLD ( Optional )
-  Cppi\_GlobalConfigParams configuration structure is changed, however
   there is no change for the applications that include
   <ti/drv/cppi/device/<soc>/cppi\_device.c> file. Applications does not
   include this directly, need to align the configuration as
   demonstrated in the cppi\_device.c file:

.. rubric:: QMSS
   :name: qmss

-  Optional RM LLD interface is supported to enable customers to use
   Resource manangement.
-  Qmss\_GlobalConfigParams configuration structure is changed, however
   there is no change for the applications that include
   <ti/drv/qmss/device/<soc>/qmss\_device.c> file. For applications that
   does not include this directly, it needs to align the configuration
   as demonstrated in the qmss\_device.c file:

.. rubric:: PA/SA
   :name: pasa

-  Support for Resource management (RM LLD) is supported for PA LLD -
   Note that this is an optional feature, applications that do not
   enable RM would not need to bring in RM LLD.

.. rubric:: HUA Demonstration
   :name: hua-demonstration

The HUA Demo for C66x in BIOS-MCSDK is no longer supported in
Processor-SDK. Rather, the Image Processing Demo is the common RTOS
demonstration that is supported across all supported devices in the
Processor-SDK for RTOS. This demo will continue to be enhanced with more
capabilities.

.. rubric:: Common Migration for Both MCSDK and BIOS-MCSDK
   :name: common-migration-for-both-mcsdk-and-bios-mcsdk

.. rubric:: Platform Library
   :name: platform-library

The Platform Library is deprecated and functionality is provided by the
Board Library. For backwards compatibility, Platform Library is provided
in this initial release. But it is planned to be dropped in a future
release. The Board Library is a common API across all devices in the
Processor-SDK.


|

.. rubric:: MCSDK1.1 to Processor SDK Migration for OMAPL13x devices
   :name: mcsdk1.1-to-processor-sdk-migration-for-omapl13x-devices

For OMAPL13x devices, you can refer to the `MCSDK1.1 to Processor SDK
Migration <Release_Specific_Migration_Guide.html#mcsdk1-1-to-processor-sdk-linux-migration-guide-for-omapl13x-devices>`__
link
