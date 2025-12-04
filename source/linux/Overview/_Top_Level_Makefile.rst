.. _top-level-makefile:

Simplified SDK Build Using Top-Level Makefile
*********************************************

.. http://processors.wiki.ti.com/index.php/Processor_Linux_SDK_Top-Level_Makefile

Overview
========

Inside of the |__SDK_FULL_NAME__| package, there is a top-level Makefile that can
be used to build some of the sub-components found within the SDK. This
Makefile uses the Rules.make file and gives an example of how the
various components can be built and the parameters to use for |__PART_FAMILY_NAME__|.

.. note::

   You should not call this makefile with the `environment-setup
   script <Overview/GCC_ToolChain.html#environment-setup-script>`__
   sourced. The sub-component Makefiles will handle sourcing this script
   where appropriate, but some make targets such as the Linux kernel make
   target do not work properly when this script is already sourced.

.. rubric:: Required Host Packages
   :name: makefile-required-packages

Please run the top level setup.sh script to install all packages required by the
makefile targets.

.. rubric:: Components:
   :name: top-level-makefile-overview

The functionality of the Top Level Makefile is implemented by these components:

- makerules/Makefile\_*    : These have all of the makerules that are common for TI SDKs across various platforms
- Rules.make               : This defines variables to configure Makefile for |__SDK_FULL_NAME__|
- Makefile                 : Only pulls in these variable definitions and the make rules

Below sections will give a bottoms-up description of these components in some more detail

makerules
---------

.. rubric:: Target Types
   :name: target-types

For each of the targets discussed below, the following target types are
defined

-  **<target>** - This is the build target which will compile the
   release version of the component.
-  **<target>\_install** - This target will install the component to the
   location pointed to by DESTDIR/BOOTFS
-  **<target>\_clean** - This target will clean the component.


.. rubric:: Component Targets

The following is a list of the basic Makefile targets that are provided in the |__SDK_FULL_NAME__|
package as component Makefiles under makerules/ directory:

.. ifconfig:: CONFIG_part_variant not in ('J7200')

   -  **u-boot** - This target will build the u-boot binaries for the
      SOC and SOC_TYPE combination defined in Rules.make. The built binaries will include:

      .. ifconfig:: CONFIG_part_variant in ('J721E')

         - sysfw.itb,

      - tiboot3.bin,
      - tispl.bin,
      - u-boot.img

      Refer to :ref:`Build-U-Boot-label` section for more details on these binaries.

   -  **linux-dtbs** - Compiles and creates the device tree blobs. It uses the
      KERNEL_DEVICETREE_PREFIX variable defined in Rules.make to parse which dtb[o]s to build.
   -  **linux** - Configures the Linux kernel for TI SOCs and Compiles the following:

      - Image,
      - modules,
      - and dtbs.
      - For SOC_TYPE=hs, This also triggers a build for the linux-fitImage target.

      Refer to :ref:`linux_kernel_users_guide` section for more details on the TI Linux Kernel.

   -  **linux-fitImage** - Picks up images built by 'u-boot-a72' and 'linux' targets and generates
      a signed fitImage, u-boot-a72 combination. This is necessary to boot successfully on HS-SE devices
      (SOC_TYPE=hs), but the fitImage can optionally be authenticated on GP (gp), HS-FS (hs-fs) devices
      as well by manually setting boot_fit=1 in the u-boot prompt.

      Refer to :ref:`fitImage-for-HS` section for more information on the signed linux fitImage.

   -  **am-benchmarks** - Builds the ARM Benchmarks for the ARCH defined in Rules.make.

   -  **cryptodev** - Builds the kernel module for the crypto device driver

   -  **ti-img-rogue-driver** - Builds the Kernel drivers for the PowerVR Rogue GPU

.. ifconfig:: CONFIG_part_variant in ('J7200')

   -  **u-boot** - This target will build the u-boot binaries for the
      SOC and SOC_TYPE combination defined in Rules.make. The built binaries will include:

      .. ifconfig:: CONFIG_part_variant in ('J721E')

         - sysfw.itb,

      - tiboot3.bin,
      - tispl.bin,
      - u-boot.img

      Refer to :ref:`Build-U-Boot-label` section for more details on these binaries.

   -  **linux-dtbs** - Compiles and creates the device tree blobs. It uses the
      KERNEL_DEVICETREE_PREFIX variable defined in Rules.make to parse which dtb[o]s to build.
   -  **linux** - Configures the Linux kernel for TI SOCs and Compiles the Linux kernel:

      - Image,
      - modules,
      - and dtbs.
      - For SOC_TYPE=hs, This also triggers a build for the linux-fitImage target.

      Refer to :ref:`linux_kernel_users_guide` section for more details on the TI Linux Kernel.

   -  **linux-fitImage** - Picks up images built by 'u-boot-a72' and 'linux' targets and generates
      a signed fitImage, u-boot-a72 combination. This is necessary to boot successfully on HS-SE devices
      (SOC_TYPE=hs), but the fitImage can optionally be authenticated on GP (gp), HS-FS (hs-fs) devices
      as well by manually setting boot_fit=1 in the u-boot prompt.

      Refer to :ref:`fitImage-for-HS` section for more information on the signed linux fitImage.

   -  **am-benchmarks** - Builds the ARM Benchmarks for the ARCH defined in Rules.make.

   -  **cryptodev** - Builds the kernel module for the crypto device driver


For a full list of supported subcomponent targets, one can also simply run ``make list-targets`` at the SDK install location.

Rules.make
----------

Here, we cover the Rules.make file found in the top-level
of the |__SDK_FULL_NAME__| package. This file is used not only by the
top-level Makefile, but also by many of the sub-component Makefiles to
gain access to common shared variables and settings. The variables defined
in here are all of the required flags/parameters that will be required to
build/compile any of the sub-component makefile targets for |__PART_FAMILY_NAME__|.

.. rubric:: Key Variables Defined
   :name: variables-defined

Below we describe a subset of the variables defined in the Rules.make
that can be editted/overriden by the user as required. These can either
be editted into the Rules.make file itself (to reset new defaults)
OR can be specified over command line when calling the make command.

-  **SOC\_TYPE** - This describes the HS configuration to build for. It
   can be set to 'gp', 'hs', and 'hs-fs'. It is used when building
   u-boot and linux to use unsigned or signed images as required.
-  **KERNEL\_DEVICETREE\_PREFIX** - This is a regex filter to parse which dtb[o]s
   should be built for |__PART_FAMILY_NAME__| SOC, when building linux kernel.
-  **ROOTFS\_PART** - This points to the base installation directory that
   applications/drivers should be installed to. This is usually the root
   of a target file system but can be changed to point anywhere.
-  **BOOT\_PART** - This points to the base installation directory that
   u-boot binaries should be installed to. This is usually the boot partition
   of an SD card but can be changed to point anywhere.


Top Level Makefile
------------------

.. rubric:: Top-Level Targets
   :name: top-level-targets

The |__SDK_FULL_NAME__| package provides the following targets by default, which
will invoke the corresponding component targets:

-  **all** - This will call the build target for each component included
   in the Makefile.
-  **install** - This will call the install target for each component
   included in the Makefile.
-  **clean** - This will call the clean target for each component
   included in the Makefile.
-  **list-targets** - This only lists all the supported targets/components for the platform

Usage Examples
==============

The following example demonstrates how to use the top-level Makefile for
building and installing u-boot and linux images. All of the examples below
assume that you are calling the Makefile from the top-level of the SDK.

-  If using an SD card, edit below variables in the Rules.make to point to
   the boot and root partitions. Else, point them to directories where you
   want to install the boot and root-filesystem images respectively.
   ::

      BOOT_PART?=/path/to/sd-card/boot-partition
      ROOTFS_PART?=/path/to/sd-card/root-partition

-  Set the correct value for the SOC_TYPE variable in Rules.make according
   to the platform being used.
   ::

      SOC_TYPE?=<gp/hs-fs/hs>

-  Now build u-boot, linux kernel images.
   ::

      make u-boot
      make linux

-  Install to SD card (BOOT_PART & ROOTFS_PART).
   ::

      make u-boot_install
      make linux_install

Now you can eject the SD card and boot the devices using the newly built images!

.. rubric:: A Note about Out-of-tree Kernel Modules
   :name: a-note-about-out-of-tree-kernel-modules

Some drivers like the GPU drivers are delivered as modules outside of
the kernel tree. If you rebuild the kernel and install it using the
``make linux_install`` target you will also need to rebuild the out of
tree modules and install them as well. The modules\_install command used
by the linux\_install target will remove any existing drivers before
installing the new ones. This means those drivers are no longer
available until they have been rebuilt against the kernel and
re-installed.

.. _top-level-makefile-hs-devices:

.. rubric:: A Note about the SOC_TYPE variable

The SOC_TYPE variable serves 2 purposes:

1. The U-Boot build generates the bootloader images for all 3 SOC types, namely,
   GP, HS-FS, and HS-SE. These are not compatible with one another. So the SOC_TYPE
   variable picks up the correct binary accordingly when installing u-boot.
   For example, below command will install the u-boot images for HS-FS device.
   ::

      SOC_TYPE=hs-fs make u-boot
      SOC_TYPE=hs-fs make u-boot_install

2. HS-SE devices enforce fitImage based authentication when booting up. They will fail to boot if (u-boot.img + fitImage) authentication fails.
   To simplify fitImage generation and testing one can simply set SOC_TYPE=hs when building/installing linux for HS-SE devices.
   ::

      SOC_TYPE=hs make linux
      SOC_TYPE=hs make linux_install
