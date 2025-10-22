.. _toolchains:

GCC ToolChain Setup
===================

.. start_include_yocto_toolchain_host_setup

Before compiling any of the sources referenced in this document, set the cross compiler paths to the toolchains packaged in the Processor SDK [Recommended] as shown below. Refer to :ref:`yocto-toolchain` section for more details on usage.

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM57X')

   .. code-block:: console

      host# export CROSS_COMPILE_32="${SDK_INSTALL_DIR}/linux-devkit/sysroots/x86_64-arago-linux/usr/bin/arm-oe-linux-gnueabi/arm-oe-linux-gnueabi-"
      host# export SYSROOT_32="${SDK_INSTALL_DIR}/linux-devkit/sysroots/armv7at2hf-neon-oe-linux-gnueabi"
      host# export CFLAGS="-march=armv7-a -mthumb -mfpu=neon -mfloat-abi=hard"
      host# export CC_32="${CROSS_COMPILE_32}gcc ${CFLAGS} --sysroot=${SYSROOT_32}"

.. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X', 'AM57X')

   .. code-block:: console

      host# export CROSS_COMPILE_64="${SDK_INSTALL_DIR}/linux-devkit/sysroots/x86_64-arago-linux/usr/bin/aarch64-oe-linux/aarch64-oe-linux-"
      host# export SYSROOT_64="${SDK_INSTALL_DIR}/linux-devkit/sysroots/aarch64-oe-linux"
      host# export CC_64="${CROSS_COMPILE_64}gcc --sysroot=${SYSROOT_64}"
      host# export CROSS_COMPILE_32="${SDK_INSTALL_DIR}/k3r5-devkit/sysroots/x86_64-arago-linux/usr/bin/arm-oe-eabi/arm-oe-eabi-"

If the Processor SDK is not installed, the Arm GNU toolchains can be downloaded and setup. Refer to :ref:`external-arm-toolchain` section for more details on usage.

.. end_include_yocto_toolchain_host_setup

.. _yocto-toolchain:

Yocto-built SDK Toolchains
--------------------------

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM57X')

   The |__SDK_FULL_NAME__| package contains cross compile toolchain for the ARMv7
   (:ref:`linux-devkit`) architecture.

.. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X', 'AM57X')

   The |__SDK_FULL_NAME__| package contains cross compile toolchains for the ARMv8
   (:ref:`linux-devkit`) and ARMv7 (:ref:`k3r5-devkit`) architectures.

These toolchains are used by the :ref:`top level makefile <top-level-makefile>` when
compiling the binaries for the target. These also package an environment setup
script that, when sourced, sets all the right variables to compile binaries for
the target architecture. The toolchain installers are built through the yocto
build system, same as the target filesystem images themselves.

Below sections give some more details about the contents of these SDK Toolchains.

.. _linux-devkit:

linux-devkit
^^^^^^^^^^^^

.. rubric:: Overview

The |__SDK_FULL_NAME__| package comes with this toolchain preinstalled at linux-devkit/
directory within the SDK. Below paths are relative to the <SDK_INSTALL_DIR> and will be
referred to using the first column in the following sections.

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM57X')

   .. list-table:: Linux Devkit Contents
      :widths: 20 30 50
      :header-rows: 1

      * - Variable
        - Location
        - Description
      * - CROSS_COMPILE_32
        - linux-devkit/sysroots/x86_64-arago-linux/usr/bin/arm-oe-linux-gnueabi/arm-oe-linux-gnueabi-
        - Cross compiler toolchain for the ARMv7 architecture
      * - SYSROOT_32
        - linux-devkit/sysroots/armv7at2hf-neon-oe-linux-gnueabi/
        - Sysroot with the cross compiled libraries and headers for the ARMv7 architecture with Linux OS
      * - ENV_SETUP_32
        - linux-devkit/environment-setup-armv7at2hf-neon-oe-linux-gnueabi
        - Shell script that sets environment variables to compile binaries for the ARMv7 linux target

.. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X', 'AM57X')

   .. list-table:: Linux Devkit Contents
      :widths: 20 30 50
      :header-rows: 1

      * - Variable
        - Location
        - Description
      * - CROSS_COMPILE_64
        - linux-devkit/sysroots/x86_64-arago-linux/usr/bin/aarch64-oe-linux/aarch64-oe-linux-
        - Cross compiler toolchain for the ARMv8 architecture
      * - SYSROOT_64
        - linux-devkit/sysroots/aarch64-oe-linux/
        - Sysroot with the cross compiled libraries and headers for the ARMv8 architecture with Linux OS
      * - ENV_SETUP_64
        - linux-devkit/environment-setup-aarch64-oe-linux
        - Shell script that sets environment variables to compile binaries for the ARMv8 linux target

.. rubric:: Target Sysroot
   :name: cross-compiled-libraries

The toolchain within the Linux SDK contains more than just the
cross-compiler, it also contains pre-built libraries that can be used
in your applications without requiring you to cross-compile them
yourself.

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM57X')

   These libraries include packages from ALSA to zlib, for a list of the
   libraries you can refer to the software manifest found in the **<SDK
   INSTALL DIR>/manifest** directory or look at the list of libraries
   available in the **<SYSROOT_32>/usr/lib** directory. You will
   also find the header files corresponding to these libraries in the
   **<SYSROOT_32>/usr/include** directory. As
   an example if your application wants access to the alsa asound library
   then you can now do the following command:

   .. code-block:: console

      host# ${CROSS_COMPILE_32}gcc -lasound app.c -o app.out

.. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X', 'AM57X')

   These libraries include packages from ALSA to zlib, for a list of the
   libraries you can refer to the software manifest found in the **<SDK
   INSTALL DIR>/manifest** directory or look at the list of libraries
   available in the **<SYSROOT_64>/usr/lib** directory. You will
   also find the header files corresponding to these libraries in the
   **<SYSROOT_64>/usr/include** directory. As
   an example if your application wants access to the alsa asound library
   then you can now do the following command:

   .. code-block:: console

      host# ${CROSS_COMPILE_64}gcc -lasound app.c -o app.out

.. rubric:: Environment-setup script
   :name: environment-setup-script

When cross-compiling packages that use configuration tools and autotools
there are many settings that are required to make sure that the proper
cross-compile libraries are used. The **environment-setup** script
located in the **<SDK_INSTALL_DIR>/linux-devkit** directory handles this
for you. This script exports variables to perform actions such as:

-  Adding the toolchain to the PATH
-  Setting up CPATH
-  Setting up PKG\_CONFIG\_\* paths
-  Setting standard variable such as CC, CPP, AR to the cross-compile
   values

To **use** the environment-setup script you only need to source it. This
is as simple as:

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM57X')

   .. code-block:: console

      host# source ${ENV_SETUP_32}

.. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X', 'AM57X')

   .. code-block:: console

      host# source ${ENV_SETUP_64}

.. note::
   :name: when-compiling-the-linux-kernel

   Because environment-setup changes standard variables such as CC you
   should not use this script when compiler projects that build host-side
   as well as target-side tools. A prime example of this is the Linux
   kernel, which builds some host side tools to help during the kernel
   build. If the environment-setup script has been sourced then the CC
   value will specify the cross-compiler for the host-side tool build. This
   means that the tools compiled and used during the kernel build will be
   compiled for the ARM platform while the kernel build tries to run these
   tools on an Intel platform. This will cause the tools to fail to run and
   the kernel to fail to compile.


.. rubric:: Example usage
   :name: linux-devkit-usage

In the simplest case the cross-compiler can be used to compile simple
applications that just need access to standard libraries. The
example below covers an application that uses only the standard libgcc
libraries.

1. First, create a **helloworld.c** file

   .. code-block:: c

      #include <stdio.h>

      int main() {
          printf ("Hello World from TI!!!\n");
          return 0;
      }

2. Compile the c file to generate an executable for the target architecture,
   using one of the below 2 methods:

   - **Compile Directly** : Cross-compile the **helloworld.c** file using the
     cross-compile toolchain directly

     .. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM57X')

        .. code-block:: console

           host# ${CROSS_COMPILE_32}gcc -march=armv7-a -mthumb -mfpu=neon -mfloat-abi=hard --sysroot=${SYSROOT_32} helloworld.c -o helloworld

     .. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X', 'AM57X')

        .. code-block:: console

           host# ${CROSS_COMPILE_64}gcc --sysroot=${SYSROOT_64} helloworld.c -o helloworld

     Be sure to give the correct path to the gcc cross compiler and target
     sysroot as listed earlier.

   - **Using the environement setup script** : Cross-compile after sourcing
     the setup script

     .. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM57X')

        .. code-block:: console

           host# source ${ENV_SETUP_32}
           host# ${CC_32} helloworld.c -o helloworld

     .. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X', 'AM57X')

        .. code-block:: console

           host# source ${ENV_SETUP_64}
           host# ${CC} helloworld.c -o helloworld

3. After the above steps are run you should now have a **helloworld**
   executable in your directory that has been compiled for the ARM. A
   simple way to check this is to run the "file" command. It should
   return an output similar to below:

   .. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM57X')

      .. code-block:: console

         host# file helloworld
         helloworld: ELF 32-bit LSB executable, ARM, EABI5 version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-armhf.so.3, BuildID[sha1]=f163acd736f827b9743b27d9a94e431d63990711, for GNU/Linux 3.2.0, with debug_info, not stripped

   .. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X', 'AM57X')

      .. code-block:: console

         host# file helloworld
         helloworld: ELF 64-bit LSB executable, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-aarch64.so.1, BuildID[sha1]=bb96180ad71bd44e07fc148015a55c844134f30d, for GNU/Linux 3.14.0, with debug_info, not stripped

|


.. _k3r5-devkit:

k3r5-devkit
^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM57X', 'AM62LX')

   .. attention::

      The Processor SDK LINUX package for |__PART_FAMILY_NAME__| devices do not support k3r5-devkit toolchain.

.. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X', 'AM57X', 'AM62LX')

   .. rubric:: Overview

   The |__SDK_FULL_NAME__| package comes with an ARMv7 toolchain preinstalled at k3r5-devkit/
   directory within the SDK. Below paths are relative to the <SDK_INSTALL_DIR>.

   .. list-table:: k3r5 Devkit Contents
      :widths: 20 30 50
      :header-rows: 1

      * - Variable
        - Location
        - Description
      * - CROSS_COMPILE_32
        - k3r5-devkit/sysroots/x86_64-arago-linux/usr/bin/arm-oe-eabi/arm-oe-eabi-
        - Cross compiler toolchain for the ARMv7 architecture
      * - SYSROOT_32
        - k3r5-devkit/sysroots/armv7at2hf-vfp-oe-eabi/
        - Sysroot with the cross compiled libraries and headers for the ARMv7 architecture
      * - ENV_SETUP_32
        - k3r5-devkit/environment-setup-armv7at2hf-vfp-oe-eabi
        - Shell script that sets environment variables to compile binaries for the target


.. _external-arm-toolchain:

ARM toolchains
--------------

It is strongly recommended to use the toolchain in the Processor SDK which
is the version tested for TI platforms. In case the Processor SDK is not
used, the toolchain can be downloaded and the toolchain path can be set as
follows.

.. rubric:: Arm Toolchain setup

Download the toolchain from `here <https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads>`__,
and the version can be found in the :ref:`release notes <release-specific-build-information>`.
The following example shows how to download and set toolchain paths
into a ``<COMPILER_PATH>`` directory in Linux Host using x86_64 architecture.
The environment variables defined here will be referenced in the build
commands of the Foundational Components in this document.

.. code-block:: console

   host# COMPILER_PATH=/opt/arm-toolchain
   host# mkdir -p $COMPILER_PATH
   host# wget -c https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-linux-gnueabihf.tar.xz -O - | tar -xv -J -C $COMPILER_PATH
   host# wget -c https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-x86_64-aarch64-none-linux-gnu.tar.xz -O - | tar -xv -J -C $COMPILER_PATH
   host# export CROSS_COMPILE_64=$COMPILER_PATH/arm-gnu-toolchain-13.3.rel1-x86_64-aarch64-none-linux-gnu/bin/aarch64-none-linux-gnu-
   host# export CROSS_COMPILE_32=$COMPILER_PATH/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-linux-gnueabihf/bin/arm-none-linux-gnueabihf-
   host# export CC_64="${CROSS_COMPILE_64}gcc"
   host# export CC_32="${CROSS_COMPILE_32}gcc"

