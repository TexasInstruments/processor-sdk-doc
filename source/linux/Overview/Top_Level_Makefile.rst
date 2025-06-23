.. _top-level-makefile:

SDK Build using Makefile
========================

.. http://processors.wiki.ti.com/index.php/Processor_Linux_SDK_Top-Level_Makefile
.. rubric:: Overview
   :name: top-level-makefile-overview

Inside of the |__SDK_FULL_NAME__| package, there is a top-level Makefile that can
be used to build some of the sub-components found within the SDK. This
Makefile uses the Rules.make file and gives an example of how the
various components can be built and the parameters to use.

The source code is available at `TexasInstruments/ti-tisdk-makefile <https://github.com/TexasInstruments/ti-tisdk-makefile>`__

.. caution::

   You should not call this makefile with the "environment-setup" script sourced.
   The sub-component Makefiles will handle sourcing this script where appropriate,
   but some make targets such as the Linux kernel make target do not work properly when this script is already sourced.

.. rubric:: Rules.make
   :name: rules.make

The following sections cover the Rules.make file found in the top-level
of the |__SDK_FULL_NAME__| package.

.. rubric:: Purpose
   :name: top-level-makefile-purpose

The **Rules.make** file in the top-level of the |__SDK_FULL_NAME__| package is
used not only by the top-level Makefile, but also by many of the
sub-component Makefiles to gain access to common shared variables and
settings. The next section covers the main variables defined in the
Rules.make file.

.. rubric:: Variables Defined
   :name: variables-defined

-  **PLATFORM** - This represents the machine name of the device
   supported by the SDK. This machine name has a direct correlation to
   the machine definition in the `Arago
   project <https://git.yoctoproject.org/meta-arago>`__ build system. The PLATFORM
   variable can be used by component Makefiles to make decisions on a
   per-machine basis.
-  **ARCH** - This represents the architecture family of the machine.
   This can be used by component Makefiles to change settings such as
   mtune values in CFLAGS based on the architecture of the PLATFORM.
-  **UBOOT\_MACHINE** - This us used when building u-boot to configure
   the u-boot sources for the correct device.
-  **TI\_SDK\_PATH** - This points to the top-level of the SDK. This is
   the same directory where the Rules.make file itself is located.
-  **DESTDIR** - This points to the base installation directory that
   applications/drivers should be installed to. This is usually the root
   of a target file system but can be changed to point anywhere.
-  **LINUX\_DEVKIT\_PATH** - This points to the linux-devkit directory.
   This directory is the base directory containing the cross-compiler
   and cross-libraries as well as the
   `environment-setup <GCC_ToolChain.html#environment-setup-script>`__
   script used by many component Makefiles to source additional variable
   settings.
-  **CROSS\_COMPILE** - This setting represents the CROSS\_COMPILE
   prefix to be used when invoking the cross-compiler. Many components
   such as the Linux kernel use the variable CROSS\_COMPILE to prepend
   the proper prefix to commands such as *gcc* to invoke the ARM
   cross-compiler.
-  **ENV\_SETUP** - This points to the
   `environment-setup <GCC_ToolChain.html#environment-setup-script>`__
   script in the linux-devkit directory used by many components to
   configure for a cross-compilation build.
-  **LINUXKERNEL\_INSTALL\_DIR** - This points to the location of the
   Linux kernel sources, which is used by components such as out-of-tree
   kernel drivers to find the Linux kernel Makefiles and headers.


.. rubric:: Makefile
   :name: makefile

The following sections cover the Makefile found in the top-level of the |__SDK_FULL_NAME__| package. The |__SDK_FULL_NAME__| can be installed either on a Linux host or inside a docker container that is hosted on `ghcr.io/texasinstruments <https://github.com/TexasInstruments/ti-docker-images/pkgs/container/ubuntu-distro>`__.

Steps to follow inside a Docker Container
-----------------------------------------

- The SD card you wish to create is inserted into the host system and has a size sufficiently large (16GB or larger) to hold at least the bootloaders, kernel and root file system.
- Refer `Steps to Run SDK Installer inside a Container <https://github.com/TexasInstruments/ti-docker-images?tab=readme-ov-file#steps-to-run-sdk-installer-inside-container>`__.
- Follow :ref:`this <usage-examples>` to understand the Makefile usage.

Steps to follow on Linux Host
-----------------------------

.. rubric:: Required Host Packages
   :name: makefile-required-packages

Please run the following command to install all packages required by the
makefile targets.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. important::

        * AM62x installer supports ``am62xx-evm`` and ``am62xx-lp-evm`` platforms. ``am62xx-evm`` is the default platform for the Toplevel Makefile. To build for ``am62xx-lp-evm``, pass ``PLATFORM=am62xx-lp-evm`` and ``YOCTO_MACHINE=am62xx-lp-evm`` as arguments to make.
        * No special arguments are needed to build for ``am62xxsip-evm`` in AM62xSIP Installer.

.. ifconfig:: CONFIG_part_variant not in ('AM62X', 'AM64X', 'AM62PX', 'AM335X', 'AM437X', 'AM65X', 'AM57X')

    .. code-block:: console

        host# sudo apt-get install build-essential autoconf automake bison flex libssl-dev bc u-boot-tools swig

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'AM62X', 'AM64X', 'AM335X', 'AM437X', 'AM65X', 'AM57X')

    .. code-block:: console

        host# sudo apt-get install build-essential autoconf automake bison flex libgnutls28-dev libmpc-dev libmpcdec6 libmpc3 libmpcdec-dev libssl-dev bc u-boot-tools swig python3 python3-pip

    Following pip packages are also needed for jailhouse & binman in u-boot targets

    .. code-block:: console

        host# pip3 install jsonschema pyelftools PyYAML Mako yamllint

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

    .. rubric:: Compiler toolchain
       :name: compiler-toolchain

    On the download page, you will find links to the recommended compiler toolchains.
    Download and extract them into your home directory. Note that you have to download
    both the toolchains for ARMv8 and ARMv7. Make sure to update your PATH to
    include the path to toolchain.

    .. code-block:: console

        GCC92PATH=$HOME/gcc-arm-9.2-2019.12-x86_64-aarch64-none-linux-gnu/bin:$HOME/gcc-arm-9.2-2019.12-x86_64-arm-none-linux-gnueabihf/bin
        export PATH=$GCC92PATH:$PATH

.. rubric:: Target Types
   :name: target-types

For each of the targets discussed below the following target type are
defined

-  **<target>** - This is the build target which will compile the
   release version of the component.

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'AM62X', 'AM64X')

    -  **<target>_stage** - This target will copy the component to
       <TISDK_path>/board-support/built-images folder.

-  **<target>_install** - This target will install the component to the
   location pointed to by DESTDIR.
-  **<target>_clean** - This target will clean the component.

.. rubric:: Top-Level Targets
   :name: top-level-targets

The |__SDK_FULL_NAME__| package provides the following targets by default, which
will invoke the corresponding component targets:

-  ``all`` - This will call the build target for each component defined
   in the Makefile.
-  ``install`` - This will call the install target for each component
   defined in the Makefile.
-  ``clean`` - This will call the clean target for each component
   defined in the Makefile.

.. rubric:: Common Targets
   :name: common-targets

The following targets are common to all platforms in |__SDK_FULL_NAME__|
package:

- ``linux`` - Compiles the Linux kernel using the default tisdk\_<PLATFORM>\_defconfig
  configuration.
- ``linux-dtbs`` - Compiles and creates the device tree blobs.
- ``u-boot`` - This target will build both u-boot and the u-boot SPL (MLO) binaries used in newer
  versions of u-boot. This actually provides a u-boot and u-boot-spl target in the Makefile.

.. ifconfig:: CONFIG_sdk not in ('SITARA')

   -  ``arm-benchmarks`` - Builds the ARM Benchmarks for the ARCH defined in
     Rules.make.
   -  ``am-sysinfo`` - Build the helper applications used by the system
     settings demos in Matrix.


.. rubric:: Additional Targets
   :name: additional-targets

Depending on the capabilities and software available for a given device
additional targets may also be defined. You can find the list of all the
targets by looking at the **all** target as described in the
`**Top-Level Targets** <#top-level-targets>`__ section above. Some
devices will have following additional targets:

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

  -  ``sysfw-image`` - Builds the system firmware itb file, which is a single
     binary for the system firmware release along with the different board
     configs.
  -  ``jailhouse`` - Builds the required kernel module, hypervisor firmware,
     jailhouse tools and cell configs. Applicable for only platforms with
     Hypervisor support enabled.

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'AM62X', 'AM62PX')

    - ``arm-benchmarks`` - Build the ARM Benchmarks

    - ``cryptodev`` - Build module for cryptographic hardware accelerators.

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'AM62X')

    - ``ti-img-rogue-driver`` - Build GPU Kernel module.

    - ``jailhouse`` - Builds the required kernel module, hypervisor firmware, jailhouse tools and cell configs. Applicable for only platforms with Hypervisor support enabled.

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM65X')

   ``ti-sgx-ddk-km`` - Build GPU Kernel module.

Along with these targets, there might be additional targets for different
external kernel modules. This list is different for each platform.


.. rubric:: Usage Examples
   :name: usage-examples

The following examples demonstrate how to use the top-level Makefile for
some common tasks. All of the examples below assume that you are calling
the Makefile from the top-level of the SDK.

-  Build Everything

   .. code-block:: console

       host# make all

-  Clean Everything

   .. code-block:: console

       host# make clean

-  Install Everything

   .. code-block:: console

       host# make install


.. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X')

    -  Build Linux kernel and Fitimage

       .. code-block:: console

           host# make linux

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X')

    -  Build Linux kernel

       .. code-block:: console

           host# make linux

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'AM62X', 'AM64X')

   - Copy FitImage, Linux Kernel Image and boot-binaries to built-images folder

     .. code-block:: console

         host# make linux_stage


.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X')

    -  Install Linux kernel image and kernel modules to SD card

       .. code-block:: console

           host# make linux_install

           To install in SD card directly:
           host# sudo DESTDIR=/media/$USER/boot make linux_install
           host# sudo DESTDIR=/media/$USER/rootfs make linux_modules_install

.. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X')

    -  Install Linux kernel modules and Fitimage to SD card rootfs

       .. code-block:: console

           host# make linux_install

           To install in SD card directly:
           host# sudo DESTDIR=/media/$USER/rootfs make linux_install

-  Clean Linux

   .. code-block:: console

       host# make linux_clean

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    - To build Linux kernel and FitImage for ``am62xx-lp-evm``, pass ``PLATFORM=am62xx-lp-evm``
      and ``YOCTO_MACHINE=am62xx-lp-evm`` arguments to make.

      .. code-block:: console

          host# PLATFORM=am62xx-lp-evm YOCTO_MACHINE=am62xx-lp-evm make linux

    - make linux_install for ``am62xx-lp-evm``

      .. code-block:: console

          host# sudo DESTDIR=/media/$USER/rootfs PLATFORM=am62xx-lp-evm YOCTO_MACHINE=am62xx-lp-evm make linux_install

    - To Build GPU kernel module

      .. code-block:: console

          host# make ti-img-rogue-driver

      .. code-block:: console

          Install GPU Kernel Modules
          host# make ti-img-rogue-driver_install

          To install in SD card directly:
          host# sudo DESTDIR=/media/$USER/rootfs make ti-img-rogue-driver_install


.. ifconfig:: CONFIG_sdk not in ('SITARA')

 -  Build the ARM Benchmarks

 .. code-block:: console

    host# make am-benchmarks

 -  Clean the ARM Benchmarks

 .. code-block:: console

    host# make am-benchmarks_clean

 -  Install the ARM Benchmarks

 .. code-block:: console

    host# make am-benchmarks_install

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'AM62X', 'AM64X' )

    -  Build the ARM Benchmarks

       .. code-block:: console

           host# make arm-benchmarks

    -  Clean the ARM Benchmarks

       .. code-block:: console

           host# make arm-benchmarks_clean

    -  Install the ARM Benchmarks

       .. code-block:: console

           host# sudo make arm-benchmarks_install

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational') or CONFIG_part_variant in ('AM65X')

  -  Build the sysfw.

  .. ifconfig:: CONFIG_part_variant in ('AM65X')

    -  By default, this builds the sysfw for AM65xx PG2.0 GP. To build sysfw for other variants,
       run the following commands

    .. code-block:: console

        host# cd <installer>/board-support/prebuilt-binaries/

    -  To build for AM65xx PG2.0 HS,

    .. code-block:: console

        host# wget https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/plain/ti-sysfw/ti-sci-firmware-am65x_sr2-hs-cert.bin?h=cicd.dunfell.202303090400 -o ti-sci-firmware-am65x_sr2-hs-cert.bin
        host# wget https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/plain/ti-sysfw/ti-sci-firmware-am65x_sr2-hs-enc.bin?h=cicd.dunfell.202303090400 -o ti-sci-firmware-am65x_sr2-hs-enc.bin

    -  To build for AM65xx PG1.0 HS,

    .. code-block:: console

        host# wget https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/plain/ti-sysfw/ti-sci-firmware-am65x-hs-cert.bin?h=cicd.dunfell.202303090400 -o ti-sci-firmware-am65x-hs-cert.bin
        host# wget https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/plain/ti-sysfw/ti-sci-firmware-am65x-hs-enc.bin?h=cicd.dunfell.202303090400 -o ti-sci-firmware-am65x-hs-enc.bin

    -  To build for AM65xx PG1.0 GP,

    .. code-block:: console

        host# wget https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/plain/ti-sysfw/ti-sci-firmware-am65x-gp.bin?h=cicd.dunfell.202303090400 -o ti-sci-firmware-am65x-gp.bin

    -  And modify the SYSFW_SOC_am65xx-evm variable in the Makefile to equal am65x or am65x_sr2 based on the device your are building for (AM65xx PG1.0 or AM65xx PG2.0 respectively).

    -  To Build for HS, add `SOC_TYPE=hs` in Rules.make file

  .. code-block:: console

      host# make sysfw-image

  -  Clean the sysfw

  .. code-block:: console

      host# make sysfw-image_clean

  -  Install the sysfw

  .. code-block:: console

      host# make sysfw-image_install

.. ifconfig:: CONFIG_part_variant not in ('AM62PX', 'AM64X', 'AM62X')

    -  Build u-boot

    .. code-block:: console

        host# make u-boot

    -  Clean u-boot

    .. code-block:: console

        host# make u-boot_clean

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'AM64X', 'AM62X')

    -  Build u-boot

       .. code-block:: console

           host# make u-boot

    - Build A53

      .. code-block:: console

          host# make u-boot-a53

    - Build R5

      .. code-block:: console

          host# make u-boot-r5

    - Copy boot-binaries to built-images folder

      .. code-block:: console

          host# make u-boot_stage

    - Install boot-binaries to SD card boot partition

      .. code-block:: console

          host# sudo DESTDIR=/media/$USER/boot make u-boot_install

    - Clean u-boot

      .. code-block:: console

          host# make u-boot_clean

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    To build u-boot binaries for ``am62xx-lp-evm``, pass ``PLATFORM=am62xx-lp-evm``
    and ``YOCTO_MACHINE=am62xx-lp-evm`` arguments to make.

    - Build u-boot for ``am62xx-lp-evm``

      .. code-block:: console

          host# make u-boot PLATFORM=am62xx-lp-evm YOCTO_MACHINE=am62xx-lp-evm

    - Install boot-binaries to SD card boot partition for ``am62xx-lp-evm``

      .. code-block:: console

          host# sudo DESTDIR=/media/$USER/boot PLATFORM=am62xx-lp-evm YOCTO_MACHINE=am62xx-lp-evm make u-boot_install

    Similar argument can be added to all u-boot targets discussed above.

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    -  Build the combined boot image (tiboot3.bin)

    This requires first building the R5 boot image. This will generate the u-boot-spl.bin. Then build sysfw-image to generate combined boot image.

    **For GP**

    .. code-block:: console

        host# make u-boot
        host# make sysfw-image DEVICE_TYPE=gp

    The combined boot image will be at <TI_SDK_PATH>/board-support/k3-image-gen*/tiboot3-am6*-gp-evm.bin

    **For HS-FS**

    .. code-block:: console

        host# make u-boot
        host# export TI_SECURE_DEV_PKG=<path-to-board-support>/core-secdev-k3
        host# make sysfw-image DEVICE_TYPE=hs-fs

    The combined boot image will be at <TI_SDK_PATH>/board-support/k3-image-gen*/tiboot3-am6*-hs-fs-evm.bin

    **For HS-SE**

    .. code-block:: console

        host# make u-boot
        host# export TI_SECURE_DEV_PKG=<path-to-board-support>/core-secdev-k3
        host# make sysfw-image DEVICE_TYPE=hs

    The combined boot image will be at <TI_SDK_PATH>/board-support/k3-image-gen*/tiboot3-am6*-hs-evm.bin

    .. note:: If TI_SECURE_DEV_PKG environment variable is not defined, tiboot3.bin can still be built for GP devices. The following errors will occur in K3-Image-Gen build logs when building for HS-FS or HS-SE devices without the TI_SECURE_DEV_PKG environment variable defined and K3-Image-Gen build may fail:

    .. code-block:: console

       TI_SECURE_DEV_PKG must be set for HS, defaults will not work.  Stop.

    To fix the above issue, do the following and rebuild the `sysfw-image`.

    .. code-block:: console

       host# export TI_SECURE_DEV_PKG=<path-to-board-support>/core-secdev-k3

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

  .. ifconfig:: CONFIG_part_variant in ('J7200')

      -  Build the combined boot image.  This requires first building the R5 boot image.
         This will generate the u-boot-spl.bin.  This file must be copied to the k3-image-gen* folder.
         The tiboot3.bin can then be built from the k3-image-gen* folder.

    .. code-block:: console

        host# make u-boot-r5
        host# cp board-support/u-boot_build/r5/spl/u-boot-spl.bin board-support/k3-image-gen*/.
        host# cd board-support/k3-image-gen*/
        host# make SOC=j7200 ROM_COMBINED_IMAGE=1 SBL=u-boot-spl.bin

.. ifconfig:: CONFIG_sdk not in ('SITARA')

   .. rubric:: Installing to SD card rootfs
   :name: installing-to-sd-card

    All the install targets copy the files in the rootfs pointed by the DESTDIR variable.
    By default, Rules.make points the DESTDIR to the NFS path for filesystem.
    If you want to install the files to the SD card, you should be able to specify
    different path to DESTDIR on commandline. e.g. run following for installing
    everything in the SD card rootfs.

    .. code-block:: console

        host# sudo DESTDIR=/media/$USER/rootfs make install
        #Replace the path to SD card rootfs partition as appropriate

.. rubric:: Installing boot binaries
   :name: installing-boot-binaries

.. ifconfig:: CONFIG_part_variant not in ('AM62PX', 'AM62X', 'AM64X')

    All the install targets copy the files in the rootfs pointed by the DESTDIR variable.
    *make install* command only copies the files in rootfs. If you have built either of
    system firmware or u-boot, you should copy these binaries in the boot partition of
    the SD card. e.g. run following to copy boot binaries in SD card boot partition.

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'AM62X', 'AM64X')

   All the install targets copy the files in the rootfs pointed by the DESTDIR variable.
   Run following commands to copy boot binaries in SD card boot partition.

.. ifconfig:: CONFIG_part_variant in ('AM65X')

    .. code-block:: console

        host# sudo cp board-support/u-boot_build/a53/u-boot.img board-support/u-boot_build/a53/tispl.bin board-support/u-boot_build/r5/tiboot3.bin /media/$USER/boot
        #Replace the path to SD card boot partition as appropriate

        # For AM65xx-EVM PG1.0, copy the following sysfw file
        host# cp board-support/k3-image-gen*/sysfw-am65x-evm.itb /media/$USER/boot/sysfw.itb
        #Replace the path to SD card boot partition as appropriate

        # For AM65xx-EVM PG2.0, copy the following sysfw file
        host# cp board-support/k3-image-gen*/sysfw-am65x_sr2-evm.itb /media/$USER/boot/sysfw.itb
        #Replace the path to SD card boot partition as appropriate

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    **For GP**

    .. code-block:: console

        host# sudo cp board-support/k3-image-gen*/tiboot3-am62*-gp-evm.bin /media/$USER/boot/tiboot3.bin
        host# sudo cp board-support/u-boot_build/a53/u-boot.img board-support/u-boot_build/a53/tispl.bin /media/$USER/boot

    **For HS-FS**

    .. code-block:: console

        host# sudo cp board-support/k3-image-gen*/tiboot3-am62*-hs-fs-evm.bin /media/$USER/boot/tiboot3.bin
        host# sudo cp board-support/u-boot_build/a53/u-boot.img board-support/u-boot_build/a53/tispl.bin /media/$USER/boot

    **For HS-SE**

    .. code-block:: console

        host# sudo cp board-support/k3-image-gen*/tiboot3-am62*-hs-evm.bin /media/$USER/boot/tiboot3.bin
        host# sudo cp board-support/u-boot_build/a53/tispl.bin_HS /media/$USER/boot/tispl.bin
        host# sudo cp board-support/u-boot_build/a53/u-boot.img_HS /media/$USER/boot/u-boot.img

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    **For GP**

    .. code-block:: console

        host# sudo cp board-support/built-images/tiboot3-am62*-gp-evm.bin /media/$USER/boot/tiboot3.bin
        host# sudo cp board-support/built-images/u-boot.img board-support/built-images/tispl.bin /media/$USER/boot

    **For HS-FS**

    .. code-block:: console

        host# sudo cp board-support/built-images/tiboot3-am62*-hs-fs-evm.bin /media/$USER/boot/tiboot3.bin
        host# sudo cp board-support/built-images/u-boot.img board-support/built-images/tispl.bin /media/$USER/boot

    **For HS-SE**

    .. code-block:: console

        host# sudo cp board-support/built-images/tiboot3-am62*-hs-evm.bin /media/$USER/boot/tiboot3.bin
        host# sudo cp board-support/built-images/tispl.bin board-support/built-images/u-boot.img /media/$USER/boot

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    **For HS-FS**

    .. code-block:: console

        host# sudo cp board-support/built-images/tiboot3-am62p*-hs-fs-evm.bin /media/$USER/boot/tiboot3.bin
        host# sudo cp board-support/built-images/u-boot.img board-support/built-images/tispl.bin /media/$USER/boot

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X')

    .. code-block:: console

        host# sudo cp board-support/u-boot_build/u-boot.img board-support/u-boot_build/MLO /media/$USER/boot


.. ifconfig:: CONFIG_part_variant in ('AM64X')

    **For GP**

    .. code-block:: console

        #Replace the path to SD card boot partition as appropriate
        host# sudo cp board-support/built-images/u-boot.img /media/$USER/boot/u-boot.img
        host# sudo cp board-support/built-images/tispl.bin /media/$USER/boot/tispl.bin
        host# sudo cp board-support/built-images/tiboot3-am64x-gp-evm.bin /media/$USER/boot/tiboot3.bin

    **For HS-FS**

    .. code-block:: console

        #Replace the path to SD card boot partition as appropriate
        host# sudo cp board-support/built-images/u-boot.img /media/$USER/boot/u-boot.img
        host# sudo cp board-support/built-images/tispl.bin /media/$USER/boot/tispl.bin
        host# sudo cp board-support/built-images/tiboot3-am64x_sr2-hs-fs-evm.bin /media/$USER/boot/tiboot3.bin

    **For HS-SE**

    .. code-block:: console

        #Replace the path to SD card boot partition as appropriate
        host# sudo cp board-support/built-images/u-boot.img /media/$USER/boot/u-boot.img
        host# sudo cp board-support/built-images/tispl.bin /media/$USER/boot/tispl.bin
        host# sudo cp board-support/built-images/tiboot3-am64x_sr2-hs-evm.bin /media/$USER/boot/tiboot3.bin

.. rubric:: A Note about Out-of-tree Kernel Modules
   :name: a-note-about-out-of-tree-kernel-modules

Some drivers like the GPU drivers are delivered as modules outside of
the kernel tree. If you rebuild the kernel and install it using the
"make linux\_install" target you will also need to rebuild the out of
tree modules and install them as well. The modules\_install command used
by the linux\_install target will remove any existing drivers before
installing the new ones. This means those drivers are no longer
available until they have been rebuilt against the kernel and
re-installed.

.. rubric:: A Note about the Linux Kernel Version
   :name: a-note-about-the-linux-kernel-version

To simplify and accelerate rebuilding and installing the linux kernel,
the file *.scmversion* is included in the kernel source tree to pin down
the version of the kernel provided in the SDK. If upgrading the kernel
sources or adding new commits, this file should be removed so that the
appropriate version is built into the kernel image.

