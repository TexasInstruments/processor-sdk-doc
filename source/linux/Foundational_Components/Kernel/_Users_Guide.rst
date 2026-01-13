.. contents:: Linux Kernel User's Guide

Overview
--------

This document will cover the basic steps for building the Linux kernel.

.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family')

   .. rubric:: Install host dependencies

   To install host dependencies for building TI Linux kernel source (standalone)
   on Ubuntu 22.04+, run the following command in the terminal prompt:

   .. code-block:: console

      sudo apt install git xz-utils build-essential flex bison bc libssl-dev libncurses-dev

Getting the Kernel Source Code
------------------------------

The easiest way to get access to the kernel source code is by
downloading and installing the |__SDK_FULL_NAME__|. You can download the
latest |__SDK_FULL_NAME__| installer from |__SDK_DOWNLOAD_URL__|. Once
installed, the kernel source code is included in the SDK's board-support
directory. For your convenience the sources also includes the kernel's
git repository including commit history.
Alternatively, Kernel sources can directly be fetched from GIT.

.. ifconfig:: CONFIG_sdk in ('SITARA')

    You can find the details about the git repository, branch and commit id in
    the :ref:`release-specific-build-information-kernel` section of the release notes.

.. _preparing-to-build:

Preparing to Build
------------------

.. note::
    The following commands are intended to be run from the root of the
    kernel tree unless otherwise specified. The root of the kernel tree is
    the top-level directory and can be identified by looking for the
    "MAINTAINERS" file.

.. _kernel-compiler:

Setup Cross Compile Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::

   When using the GCC toolchain provided with the SDK or stand alone from TI that you do
   **NOT** source the :file:`environment-setup` file included with the toolchain when
   building the kernel. Doing so will cause the compilation of host side components within
   the kernel tree to fail.

.. include:: Overview/GCC_ToolChain.rst
   :start-after: .. start_include_yocto_toolchain_host_setup
   :end-before: .. end_include_yocto_toolchain_host_setup

Cleaning the Kernel Sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prior to compiling the Linux kernel it is often a good idea to make sure
that the kernel sources are clean and that there are no remnants left
over from a previous build.

.. note::
    The next step will delete any saved .config file in the kernel tree as
    well as the generated object files. If you have done a previous
    configuration and do not wish to lose your configuration file you should
    save a copy of the configuration file (.config) before proceeding.

The command to clean the kernel is:

..
  [comment] instructions for 32 bit processors
.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    .. code-block:: console

        make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" distclean

..
  [comment] instructions for 64 bit processors
.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    .. code-block:: console

        make ARCH=arm64 CROSS_COMPILE="$CROSS_COMPILE_64" distclean

|

.. _users-guide-kernel-config:

Configuring the Kernel
----------------------

Before compiling the Linux kernel it needs to be configured to select
what components will become part of the kernel image, which components
will be build as dynamic modules, and which components will be left out
all together. This is done using the Linux kernel configuration system.


It is often easiest to start with a base default configuration and then
customize it for your use case if needed. Apply Linux kernel configurations with
a command of the form:

..
  [comment] instructions for 32 bit processors
.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    .. code-block:: console

        make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" <defconfig>

..
  [comment] instructions for 64 bit processors
.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    .. code-block:: console

        make ARCH=arm64 CROSS_COMPILE="$CROSS_COMPILE_64" <defconfig>

Using Default Configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^



..
  [comment] instructions for 32 bit processors
.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    For this sdk, the defconfig found in :file:`arch/arm/configs` is used to create the prebuilt
    files. We recommend users to use this kernel configuration (or at least use it
    as a starting point).

    For example, to apply the default AM335x kernel configuration, use:

    For Linux,

    .. code-block:: console

        make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" multi_v7_defconfig ti_multi_v7_prune.config no_smp.config

    For RT-Linux,

    .. code-block:: console

        make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" multi_v7_defconfig ti_multi_v7_prune.config no_smp.config ti_rt.config


..
  [comment] instructions for 64 bit processors
.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    For this sdk, the defconfig found in :file:`arch/arm64/configs` is used to create the prebuilt
    files. We recommend users to use this kernel configuration (or at least use it
    as a starting point).

    For example, to apply the recommended kernel configuration for K3 devices, use:

    For Linux,

    .. code-block:: console

        make ARCH=arm64 CROSS_COMPILE="$CROSS_COMPILE_64" defconfig ti_arm64_prune.config

    For RT-Linux,

    .. code-block:: console

        make ARCH=arm64 CROSS_COMPILE="$CROSS_COMPILE_64" defconfig ti_arm64_prune.config ti_rt.config

The config fragments found in <path-to-ti-linux-kernel>/kernel/configs can be used to trim/add
features when building a kernel that targets only TI EVMs. Append a config fragment to the end
of "make" command like above to add/remove features.

After the configuration step has run the full configuration file is
saved to the root of the kernel tree as .config. Any further
configuration changes are based on this file until it is cleaned up by
doing a kernel clean as mentioned above.

Customizing the Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you want to customize the kernel configuration the easiest way is
to use the built in kernel configuration systems. One popular configuration
system is menuconfig. menuconfig is an ncurses based configuration utility.

To invoke the kernel configuration you simply use a command like:

..
  [comment] instructions for 32 bit processors
.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    .. code-block:: console

        make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" <config type>

    i.e. for menuconfig the command would look like

    .. code-block:: console

        make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" menuconfig

..
  [comment] instructions for 64 bit processors
.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    .. code-block:: console

        make ARCH=arm64 CROSS_COMPILE="$CROSS_COMPILE_64" <config type>

    i.e. for menuconfig the command would look like

    .. code-block:: console

        make ARCH=arm64 CROSS_COMPILE="$CROSS_COMPILE_64" menuconfig

Once the configuration window is open you can then select which kernel
components should be included in the build. Exiting the configuration
will save your selections to a file in the root of the kernel tree
called .config.

|

Compiling the Sources
---------------------

Compiling the Kernel
^^^^^^^^^^^^^^^^^^^^

..
  [comment] instructions for 32 bit processors
.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    Once the kernel has been configured it must be compiled to generate the
    bootable kernel image as well as any dynamic kernel modules that were
    selected.

    By default U-boot expects a compressed, self-extracting kernel image called
    :file:`zImage` as the type of kernel image used.

    To build, use this command:

    .. code-block:: console

        make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" zImage

    This will result in a kernel image file being created in the
    :file:`arch/arm/boot/` directory called :file:`zImage`.

..
  [comment] instructions for 64 bit processors
.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    By default U-boot expects to boot kernel :file:`Image`, DTB, and DTOs found in :file:`root/boot` of the
    SD card if using SD/MMC boot. The exception is for HS-SE (High Security - Security Enforced)
    devices where the FIT image (Flattened Image Tree) named :file:`fitImage` will boot by default.

    The FIT image includes the kernel :file:`Image`, DTB, and DTOs. Booting with the FIT image could be
    enabled/disabled by setting/resetting u-boot environment variable `boot_fit`. If `boot_fit` is set
    to `1`, then u-boot will boot the FIT image found in :file:`root/boot` of the SD card.

    Once the kernel has been configured it must be compiled to generate the bootable kernel :file:`Image`
    as well as any dynamic kernel modules that were selected. To rebuild kernel :file:`Image` to boot as
    is or for FIT image boot, use this command:

    .. code-block:: console

        make ARCH=arm64 CROSS_COMPILE="$CROSS_COMPILE_64" Image

    This will result in a kernel image file being created in the
    :file:`arch/arm64/boot/` directory called :file:`Image`.

.. _kernel_users_guide_compiling_the_device_tree_binaries:

Compiling the Device Tree Binaries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..
  [comment] instructions for 32 bit processors
.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    Starting with the 3.8 kernel each TI evm has an unique device tree
    binary file required by the kernel. Therefore, you will need to build
    and install the correct dtb for the target device. All device tree files
    are located at :file:`arch/arm/boot/dts/ti/omap`. Below list various TI evms and the
    matching device tree file.

    +-------------------------------------------+--------------------------------------+
    | Boards                                    | Device Tree File                     |
    +===========================================+======================================+
    | Beaglebone Black                          | am335x-boneblack.dts                 |
    +-------------------------------------------+--------------------------------------+
    | Beaglebone Green ECO                      | am335x-bonegreen-eco.dts             |
    +-------------------------------------------+--------------------------------------+
    | AM335x General Purpose EVM                | am335x-evm.dts                       |
    +-------------------------------------------+--------------------------------------+
    | AM335x Starter Kit                        | am335x-evmsk.dts                     |
    +-------------------------------------------+--------------------------------------+
    | AM335x Industrial Communications Engine   | am335x-icev2.dts                     |
    +-------------------------------------------+--------------------------------------+
    | AM437x General Purpose EVM                | am437x-gp-evm.dts,                   |
    |                                           | am437x-gp-evm-hdmi.dts (HDMI)        |
    +-------------------------------------------+--------------------------------------+
    | AM437x Starter Kit                        | am437x-sk-evm.dts                    |
    +-------------------------------------------+--------------------------------------+
    | AM437x Industrial Development Kit         | am437x-idk-evm.dts                   |
    +-------------------------------------------+--------------------------------------+
    | AM57xx EVM                                | am57xx-evm.dts,                      |
    |                                           | am57xx-evm-reva3.dts (revA3 EVMs )   |
    +-------------------------------------------+--------------------------------------+
    | AM572x IDK                                | am572x-idk.dts                       |
    +-------------------------------------------+--------------------------------------+
    | AM571x IDK                                | am571x-idk.dts                       |
    +-------------------------------------------+--------------------------------------+
    | AM574x IDK                                | am574x-idk.dts                       |
    +-------------------------------------------+--------------------------------------+
    | K2H/K2K EVM                               | keystone-k2hk-evm.dts                |
    +-------------------------------------------+--------------------------------------+
    | K2E EVM                                   | keystone-k2e-evm.dts                 |
    +-------------------------------------------+--------------------------------------+
    | K2L EVM                                   | keystone-k2l-evm.dts                 |
    +-------------------------------------------+--------------------------------------+
    | K2G EVM                                   | keystone-k2g-evm.dts                 |
    +-------------------------------------------+--------------------------------------+
    | K2G ICE EVM                               | keystone-k2g-ice.dts                 |
    +-------------------------------------------+--------------------------------------+
    | OMAP-L138 LCDK                            | da850-lcdk.dts                       |
    +-------------------------------------------+--------------------------------------+

    To build an individual device tree file find the name of the dts file
    for the board you are using and replace the .dts extension with .dtb.
    Then run the following command:

    .. code-block:: console

        make DTC_FLAGS=-@ ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" <dt filename>.dtb

    The compiled device tree file with be located in :file:`arch/arm/boot/dts/ti/omap`.

    For example, the Beaglebone Black device tree file is named
    :file:`am335x-boneblack.dts`. To build the device tree binary you would run:

    .. code-block:: console

        make DTC_FLAGS=-@ ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" am335x-boneblack.dtb

    Alternatively, you can build every device tree binary with command

    .. code-block:: console

        make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" dtbs

..
  [comment] instructions for 64 bit processors
.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    Each TI evm has an unique device tree
    binary file required by the kernel. Therefore, you will need to build
    and install the correct dtb for the target device. TI device tree files
    are located in :file:`arch/arm64/boot/dts/ti`. Below list various TI evms and the
    matching device tree file.

    +-------------------------------------------+--------------------------------------+
    | Boards                                    | Device Tree File                     |
    +===========================================+======================================+
    | AM62Lx EVM                                | k3-am62l3-evm.dts                    |
    +-------------------------------------------+--------------------------------------+
    | AM62Px SK                                 | k3-am62p5-sk.dts                     |
    +-------------------------------------------+--------------------------------------+
    | AM62Ax SK                                 | k3-am62a7-sk.dts                     |
    +-------------------------------------------+--------------------------------------+
    | AM62Dx EVM                                | k3-am62d2-evm.dts                    |
    +-------------------------------------------+--------------------------------------+
    | AM62x LP SK                               | k3-am62-lp-sk.dts                    |
    +-------------------------------------------+--------------------------------------+
    | Beagle Play                               | k3-am625-beagleplay.dts              |
    +-------------------------------------------+--------------------------------------+
    | AM62SIP SK / AM62x SK                     | k3-am625-sk.dts                      |
    +-------------------------------------------+--------------------------------------+
    | AM64x EVM                                 | k3-am642-evm.dts                     |
    +-------------------------------------------+--------------------------------------+
    | AM64x SK                                  | k3-am642-sk.dts                      |
    +-------------------------------------------+--------------------------------------+
    | AM65x EVM / AM65x IDK                     | k3-am654-base-board.dts,             |
    |                                           | daughter cards use .dtso files       |
    +-------------------------------------------+--------------------------------------+
    | J721e EVM                                 | k3-j721e-common-proc-board.dts       |
    +-------------------------------------------+--------------------------------------+
    | J721e SK                                  | k3-j721e-sk.dts                      |
    +-------------------------------------------+--------------------------------------+
    | J7200 EVM                                 | k3-j7200-common-proc-board.dts       |
    +-------------------------------------------+--------------------------------------+
    | J721S2 EVM                                | k3-j721s2-common-proc-board.dts      |
    +-------------------------------------------+--------------------------------------+
    | AM68 SK                                   | k3-am68-sk-base-board.dts            |
    +-------------------------------------------+--------------------------------------+
    | J784S4 EVM                                | k3-j784s4-evm.dts                    |
    +-------------------------------------------+--------------------------------------+
    | AM69 SK                                   | k3-am69-sk.dts                       |
    +-------------------------------------------+--------------------------------------+
    | J722S EVM                                 | k3-j722s-evm.dts                     |
    +-------------------------------------------+--------------------------------------+

    To build an individual device tree file find the name of the dts file
    for the board you are using and replace the .dts extension with .dtb.
    Then run the following command:

    .. code-block:: console

        make DTC_FLAGS=-@ ARCH=arm64 CROSS_COMPILE="$CROSS_COMPILE_64" ti/<dt filename>.dtb

    The compiled device tree file with be located in :file:`arch/arm64/boot/dts/ti`.

    For example, the AM64x EVM device tree file is named
    :file:`k3-am642-evm.dts`. To build the device tree binary you would run:

    .. code-block:: console

        make DTC_FLAGS=-@ ARCH=arm64 CROSS_COMPILE="$CROSS_COMPILE_64" ti/k3-am642-evm.dtb

    Alternatively, you can build every device tree binary with command

    .. code-block:: console

        make ARCH=arm64 CROSS_COMPILE="$CROSS_COMPILE_64" dtbs

Compiling the Kernel Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..
  [comment] instructions for 32 bit processors
.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    By default the majority of the Linux drivers used in the sdk are not
    integrated into the kernel image file :file:`zImage`. These drivers are built as
    dynamic modules. The command to build these modules is:

    .. code-block:: console

        make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" modules

..
  [comment] instructions for 64 bit processors
.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    By default the majority of the Linux drivers used in the sdk are not
    integrated into the kernel image file :file:`Image`. These drivers are built as
    dynamic modules. The command to build these modules is:

    .. code-block:: console

        make ARCH=arm64 CROSS_COMPILE="$CROSS_COMPILE_64" modules


This will result in .ko (kernel object) files being placed in the kernel
tree. These .ko files are the dynamic kernel modules.

.. note::
    If you make a change to the kernel which requires you to recompile
    the kernel, then you should also recompile the kernel modules and
    reinstall the kernel modules. Otherwise your kernel modules may refuse to
    load, which will result in a loss of functionality.

|

FIT Image
---------

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family')

   FIT Image documentation is pending for |__PART_FAMILY_DEVICE_NAMES__|
   reach out to:  `Help e2e <https://e2e.ti.com//>`__ for additional information.

.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family')

   .. include:: /linux/Foundational_Components/Kernel/_Fit_Image_Guide.rst

|

Installing the Kernel
---------------------

Once the Linux kernel, dtb files and modules have been compiled they
must be installed. In the case of the kernel image this can be installed
by copying the kernel image file to the location where it is going to be read
from. The device tree binaries should also be copied to the same
directory that the kernel image was copied to.

Installing the Kernel Image and Device Tree Binaries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..
  [comment] instructions for 32 bit processors
.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    .. code-block:: console

        cd <kernel sources dir>
        sudo cp arch/arm/boot/zImage $boot
        sudo cp arch/arm/boot/dts/ti/omap/<dt file>.dtb $boot

    For example, if you wanted to copy the kernel image and BeagleBone
    Black device tree file to the SD card partition, you would
    enter the below commands:

    .. code-block:: console

         cd <kernel sources dir>
         sudo cp arch/arm/boot/zImage $boot
         sudo cp arch/arm/boot/dts/ti/omap/am335x-boneblack.dtb $boot

    Where ``$boot`` is the mount point for the boot partition of the SD card.

..
  [comment] instructions for 64 bit processors
.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    .. code-block:: console

        cd <kernel sources dir>
        sudo cp arch/arm64/boot/Image <rootfs path>/boot
        sudo cp arch/arm64/boot/dts/ti/<dt file>.dtb <rootfs path>/boot/dtb/ti

    For example, if you wanted to copy the kernel image and AM64x EVM
    device tree file to the rootfs partition of a SD card you would
    enter the below commands:

    .. code-block:: console

         cd <kernel sources dir>
         sudo cp arch/arm64/boot/Image /media/rootfs/boot
         sudo cp arch/arm64/boot/dts/ti/k3-am642-evm.dtb /media/rootfs/boot/dtb/ti

Starting with U-boot 2013.10, the kernel and device tree binaries are read from
the root file system's boot directory when booting from MMC/EMMC. (NOT from the
/boot/ partition on the MMC). This would mean you copy the kernel image and device
tree binaries to :file:`/media/rootfs/boot` instead of :file:`/media/boot`.

Installing the Kernel Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install the kernel modules you use another make command similar to
the others, but with an additional parameter which give the base
location where the modules should be installed. This command will create
a directory tree from that location like lib/modules/<kernel version>
which will contain the dynamic modules corresponding to this version of
the kernel. The base location should usually be the root of your target
file system. The general format of the command is:

..
  [comment] instructions for 32 bit processors
.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    .. code-block:: console

        sudo make ARCH=arm  INSTALL_MOD_PATH=<path to root of file system> modules_install

    For example if you are installing the modules on the rootfs partition of
    the SD card you would do:

    .. code-block:: console

        sudo make ARCH=arm INSTALL_MOD_PATH=/media/rootfs modules_install

..
  [comment] instructions for 64 bit processors
.. ifconfig:: CONFIG_part_family not in ('AM335X_family', 'AM437X_family', 'AM57X_family')

    .. code-block:: console

        sudo make ARCH=arm64  INSTALL_MOD_PATH=<path to root of file system> modules_install

    For example if you are installing the modules on the rootfs partition of
    the SD card you would do:

    .. code-block:: console

        sudo make ARCH=arm64 INSTALL_MOD_PATH=/media/rootfs modules_install

.. note::

  Append **INSTALL\_MOD\_STRIP=1** to the make modules\_install command to
  reduce the size of the resulting installation
