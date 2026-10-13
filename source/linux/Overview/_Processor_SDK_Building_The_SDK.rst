.. _building-the-sdk-with-yocto:

***************************
Building the SDK with Yocto
***************************

Introduction
============
This page provides the steps to build the Processor SDK and individual
components from source. The Processor SDK build is based on the `Arago
Project <https://git.yoctoproject.org/meta-arago>`__ which
provides a set of layers for `OpenEmbedded <https://www.openembedded.org/wiki/Main_Page>`__
and the `Yocto Project <https://yoctoproject.org/>`__ targeting TI
platforms.

This page will provide the basic steps required to recreate the Processor
SDK along with a reference of Processor SDK specific configurations,
build targets, and target devices. Also, tips and suggestions are
provided along with links for more in-depth information.

Steps to Run Yocto Builds inside Container
==========================================

TI provides a Ubuntu 22.04 based docker image with all the packages that are required to start a Yocto Build.

The Docker Image is hosted on `ghcr.io/texasinstruments <https://github.com/TexasInstruments/ti-docker-images/pkgs/container/ubuntu-distro>`__.

Refer `Steps to Run Yocto builds inside a Container <https://github.com/TexasInstruments/ti-docker-images?tab=readme-ov-file#steps-to-run-yocto-builds-inside-container>`__ for a comprehensive guide.

Follow :ref:`Processor SDK Build Reference <processor-sdk-build-reference>` for Layer Configuration and Build Options.

.. attention::

   Before starting the container, ensure that you have completed all the Pre-Requisites as mentioned `here <https://github.com/TexasInstruments/ti-docker-images?tab=readme-ov-file#pre-requisites>`__.

Steps to Run Yocto Builds on Host
=================================

Prerequisites (One-time setup)
------------------------------

.. rubric:: Host Setup - Ubuntu (Recommended)
   :name: Host Setup - ubuntu (Recommended)

.. ifconfig:: CONFIG_sdk in ('SITARA', 'JACINTO','j7_foundational')

   The recommended Linux distribution is Ubuntu 22.04.

The following build host packages are required for Ubuntu. The following
command will install the required tools on the Ubuntu Linux
distribution.

.. ifconfig:: CONFIG_sdk in ('SITARA', 'JACINTO','j7_foundational')

   For Ubuntu 22.04, please run the following:

.. code-block:: console

   $ sudo apt-get update
   $ # Install packages required for builds
   $ sudo apt-get -f -y install \
     git build-essential diffstat texinfo gawk chrpath socat doxygen \
     dos2unix python3 bison flex libssl-dev u-boot-tools mono-devel \
     mono-complete curl python3-distutils repo pseudo python3-sphinx \
     g++-multilib libc6-dev-i386 jq git-lfs pigz zstd liblz4-tool \
     cpio file lz4 debianutils iputils-ping python3-git python3-jinja2 \
     python3-subunit locales libacl1 unzip gcc python3-pip python3-pexpect \
     xz-utils wget \
   $ sudo locale-gen en_US.UTF-8

By default Ubuntu uses "dash" as the default shell for /bin/sh. You must
reconfigure to use bash by running the following command:

.. code-block:: console

   $ sudo dpkg-reconfigure dash

.. important::

   Be sure to select "No" when you are asked to use dash as the default system shell.

.. rubric:: Large Swap File

Building large packages, especially several at a time, requires a lot of
working memory for a computer. For computers with 32 GB of RAM or more, this
should not be a problem. For computers with less RAM, a swap file of ~16GB may
be needed to build large packages. Creating a large swap file, or resizing a
small swap file to be larger will help avoid build errors for large packages.

.. rubric:: Proxy Setup
   :name: Proxy Setup

If working behind a proxy, please see `Working Behind a Network
Proxy <https://wiki.yoctoproject.org/wiki/Working_Behind_a_Network_Proxy>`__.

Build Steps
-----------

Please refer to :ref:`here <yocto-layer-configuration>` for the
layer configuration ``oeconfig-file`` for a particular release of |__SDK_FULL_NAME__|.
The MACHINE can be set to |__SDK_BUILD_MACHINE__|, for example.

.. ifconfig:: CONFIG_sdk in ('SITARA')

   .. ifconfig:: CONFIG_part_variant in ('AM62AX')

      The final command below will build the **tisdk-edgeai-image**, which is the
      Processor SDK image with Arago + EdgeAI filesystem.  See `Build Options`_ for a list of
      additional targets.

      .. tabs::

         .. tab:: Build Linux SD card Image

            .. code-block:: console

               $ git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
               $ cd tisdk
               $ ./oe-layertool-setup.sh -f configs/processor-sdk-analytics/<oeconfig-file>
               $ cd build
               $ . conf/setenv
               $ MACHINE=am62axx-evm bitbake -k tisdk-edgeai-image

         .. tab:: Build RT-Linux SD card Image

            .. code-block:: console

               $ git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
               $ cd tisdk
               $ ./oe-layertool-setup.sh -f configs/processor-sdk-analytics/<oeconfig-file>
               $ cd build
               $ . conf/setenv
               $ MACHINE=am62axx-evm ARAGO_RT_ENABLE=1 bitbake -k tisdk-edgeai-image

   .. ifconfig:: CONFIG_part_variant not in ('AM62AX', 'AM335X', 'AM437X')

      The final command below will build the :file:`tisdk-default-image`, which is the
      Processor SDK image with arago filesystem.  See `Build Options`_ for a list of
      additional targets.

      .. tabs::

         .. tab:: Build Linux SD card Image

            .. code-block:: console

               $ git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
               $ cd tisdk
               $ ./oe-layertool-setup.sh -f configs/processor-sdk/<oeconfig-file>
               $ cd build
               $ . conf/setenv
               $ MACHINE=<machine> bitbake -k tisdk-default-image

         .. tab:: Build RT-Linux SD card Image

            .. code-block:: console

               $ git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
               $ cd tisdk
               $ ./oe-layertool-setup.sh -f configs/processor-sdk/<oeconfig-file>
               $ cd build
               $ . conf/setenv
               $ MACHINE=<machine> ARAGO_RT_ENABLE=1 bitbake -k tisdk-default-image

   .. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X')

      The final command below will build the :file:`tisdk-default-image`, which is the
      Processor SDK image with arago filesystem.  See `Build Options`_ for a list of
      additional targets.

      .. code-block:: console

         $ git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
         $ cd tisdk
         $ ./oe-layertool-setup.sh -f configs/processor-sdk/<oeconfig-file>
         $ cd build
         $ . conf/setenv
         $ MACHINE=<machine> bitbake -k tisdk-default-image

   .. ifconfig:: CONFIG_part_variant in ('AM62X','AM62PX','AM62LX')

      * The final command below will build the :file:`tisdk-jailhouse-image`, which is the
        Processor SDK image with arago filesystem and Jailhouse support.

      .. ifconfig:: CONFIG_part_variant in ('AM62X')

         * :file:`tisdk-jailhouse-image` is not applicable for am62xxsip-evm and beagleplay-ti.

      .. tabs::

         .. tab:: Build Jailhouse Linux SD card Image

            .. code-block:: console

               $ git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
               $ cd tisdk
               $ ./oe-layertool-setup.sh -f configs/processor-sdk/<oeconfig-file>
               $ cd build
               $ . conf/setenv
               $ echo 'TI_EXTRAS="tie-jailhouse"' >> conf/local.conf
               $ MACHINE=<machine> bitbake -k tisdk-jailhouse-image

         .. tab:: Build Jailhouse RT-Linux SD card Image

            .. code-block:: console

               $ git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
               $ cd tisdk
               $ ./oe-layertool-setup.sh -f configs/processor-sdk/<oeconfig-file>
               $ cd build
               $ . conf/setenv
               $ echo 'TI_EXTRAS="tie-jailhouse"' >> conf/local.conf
               $ MACHINE=<machine> ARAGO_RT_ENABLE=1 bitbake -k tisdk-jailhouse-image

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      * The command below will build the :file:`tisdk-evse-image`, which is the
        Processor SDK image with arago filesystem and `AM62L-EVSE-DEV-EVM <https://www.ti.com/lit/ug/slvudn0/slvudn0.pdf>`_ support (EV charging Use case support).

      .. code-block:: console

         $ git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
         $ cd tisdk
         $ ./oe-layertool-setup.sh -f configs/processor-sdk/<oeconfig-file>
         $ cd build
         $ . conf/setenv
         $ MACHINE=am62lxx-evm ARAGO_RT_ENABLE=1 bitbake -k tisdk-evse-image

      .. important::

         EVSE (EV Charging) image uses RT-Linux and is not supported on Linux.

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

   |__SDK_FULL_NAME__| uses the 'oe-layersetup' tool to configure the meta layers. If you do not have the Linux SDK package installed:

   .. code-block:: console

      git clone https://git.ti.com/git/arago-project/oe-layersetup.git yocto-build
      cd yocto-build

   The Linux SDK package also has the above tool cloned at the top level. If you have it installed:

   .. code-block:: console

      cd <SDK INSTALL DIR>/yocto-build

   Then run following commands to setup a yocto build for a specific release version and build the 'tisdk-|__IMAGE_TYPE__|-image' target.

   .. ifconfig:: CONFIG_image_type in ('default')

      .. code-block:: console

         ./oe-layertool-setup.sh -f configs/processor-sdk-linux/processor-sdk-linux-<version>.txt
         cd build
         . conf/setenv
         MACHINE=<machine> bitbake -k tisdk-default-image

   .. ifconfig:: CONFIG_image_type in ('edgeai', 'adas')

      .. parsed-literal::

         ./oe-layertool-setup.sh -f configs/processor-sdk-analytics/processor-sdk-analytics-<version>-config.txt
         cd build
         . conf/setenv
         echo 'ARAGO_BRAND = \"|__IMAGE_TYPE__|\"' >> conf/local.conf
         MACHINE="|__SDK_BUILD_MACHINE__|" bitbake -k tisdk-|__IMAGE_TYPE__|-image

Your newly built wic image will be generated in deploy-ti directory. Use :ref:`Linux SD Card Creation Guide <processor-sdk-linux-create-sd-card>` to flash this image on the SD-Card.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. note:: If trying to build tisdk-display-cluster image, add ``DISPLAY_CLUSTER_ENABLE="1"`` at the end of :file:`conf/local.conf` file before running bitbake.

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'AM62DX', 'AM65X', 'AM335X', 'AM437X')

   .. important::

      The Yocto build will need ~500GB of hard disk space for building the :file:`tisdk-default-image`

.. ifconfig:: CONFIG_sdk in ('j7_foundational') or CONFIG_part_variant in ('AM62X', 'AM62PX')

   .. important::

      The Yocto build will need ~750GB of hard disk space for building the :file:`tisdk-default-image` which includes Chromium.

   .. tip::

      The :file:`tisdk-default-image` now includes Chromium by default, which may increase the build
      time. If you prefer not to build Chromium, you can remove the **meta-browser** layer from
      the oeconfig-file before running :file:`oe-layertool-setup.sh`

      However, if you are building the :file:`tisdk-default-image` specifically to try out the TI Apps Launcher out-of-the-box (OOB),
      it is not recommended to remove the meta-browser layer. The TI Apps Launcher relies on
      Chromium and removing the layer may impact its functionality. Keep the meta-browser layer
      intact for the best OOB experience.


.. tip::

   If your computer is frequently crashing while running the bitbake command, edit the
   :file:`conf/local.conf` file under ``build`` directory and set the variables: ``BB_NUMBER_THREADS`` and ``PARALLEL_MAKE``
   to cap the number of threads bitbake can create at a time. By default bitbake tries to automatically figure out and
   set the maximum values for these variables on your system which may lead to errors.

.. caution:: While building images via Yocto, if you are facing **locale.Error: unsupported locale setting** error, it means your system is trying to use a locale setting which was not there. Run the following commands which will setup the locale and try building your target image again.

   .. code-block:: console

      export LC_ALL="en_US.UTF-8"
      export LC_CTYPE="en_US.UTF-8"
      export LC_NUMERIC="en_US.UTF-8"
      export LANG=en_US.UTF-8
      export LANGUAGE=en_US.UTF-8
      ulimit -n 4096

.. _processor-sdk-build-reference:

Processor SDK Build Reference
=============================

The following sections provide information for configuration, build
options, and supported platforms of the Processor SDK.

Layer Configuration
-------------------
Please refer to :ref:`here <yocto-layer-configuration>` for the layer configuration for a particular release of Processor SDK Linux.

.. _Build_Options:

Build Options
-------------

.. rubric:: Images
   :name: Images

In addition to individual components packages, the following table
provides a list of build targets supported. These are the <target> used
in the command:

.. code-block:: console

   MACHINE=<machine> bitbake <target>

The build system places the "Build Output" relative to :file:`deploy-ti`


.. ifconfig:: CONFIG_sdk in ('SITARA')

   .. ifconfig:: CONFIG_part_variant in ('AM62AX')

      +------------------------------+---------------------------------------------------------------+-------------------------------+
      | Target                       | Build Output                                                  | Description                   |
      +==============================+===============================================================+===============================+
      | tisdk-edgeai-image           | images/<machine>/tisdk-edgeai-image-<machine>.tar.xz          | Target Edge AI Filesystem     |
      +------------------------------+---------------------------------------------------------------+-------------------------------+
      | tisdk-default-image          | images/<machine>/tisdk-default-image-<machine>.tar.xz         | Target Filesystem w/o EdgeAI  |
      +------------------------------+---------------------------------------------------------------+-------------------------------+
      | tisdk-base-image             | images/<machine>/tisdk-base-image-<machine>.tar.xz            | Minimal Target Filesytem      |
      +------------------------------+---------------------------------------------------------------+-------------------------------+
      | meta-toolchain-arago-tisdk   | sdk/arago-<arago-version>-<architecture>.sh                   | Devkit                        |
      +------------------------------+---------------------------------------------------------------+-------------------------------+
      | mc:k3r5:meta-toolchain-arago | sdk/arago-<arago-version>-<architecture>.sh                   | K3R5 baremetal toolchain      |
      +------------------------------+---------------------------------------------------------------+-------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      +------------------------------+----------------------------------------------------------------------+----------------------------+
      | Target                       | Build Output                                                         | Description                |
      +==============================+======================================================================+============================+
      | tisdk-default-image          | images/<machine>/tisdk-default-image-<machine>.rootfs.tar.xz         | Target Filesystem          |
      +------------------------------+----------------------------------------------------------------------+----------------------------+
      | tisdk-display-cluster-image  | images/<machine>/tisdk-display-cluster-image-<machine>.rootfs.tar.xz | Display Cluster Filesystem |
      +------------------------------+----------------------------------------------------------------------+----------------------------+
      | tisdk-jailhouse-image        | images/<machine>/tisdk-jailhouse-image-<machine>.rootfs.tar.xz       | Jailhouse Filesystem       |
      +------------------------------+----------------------------------------------------------------------+----------------------------+
      | tisdk-base-image             | images/<machine>/tisdk-base-image-<machine>.rootfs.tar.xz            | Minimal Target Filesytem   |
      +------------------------------+----------------------------------------------------------------------+----------------------------+
      | tisdk-thinlinux-image        | images/<machine>/tisdk-thinlinux-image-<machine>.rootfs.tar.xz       | Minimal Target Filesytem   |
      |                              |                                                                      | with docker enabled        |
      +------------------------------+----------------------------------------------------------------------+----------------------------+
      | meta-toolchain-arago-tisdk   | sdk/arago-<arago-version>-<architecture>.sh                          | Devkit                     |
      +------------------------------+----------------------------------------------------------------------+----------------------------+
      | mc:k3r5:meta-toolchain-arago | sdk/arago-<arago-version>-<architecture>.sh                          | K3R5 baremetal toolchain   |
      +------------------------------+----------------------------------------------------------------------+----------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      +------------------------------+----------------------------------------------------------------+----------------------------+
      | Target                       | Build Output                                                   | Description                |
      +==============================+================================================================+============================+
      | tisdk-default-image          | images/<machine>/tisdk-default-image-<machine>.rootfs.tar.xz   | Target Filesystem          |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | tisdk-jailhouse-image        | images/<machine>/tisdk-jailhouse-image-<machine>.rootfs.tar.xz | Jailhouse Filesystem       |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | tisdk-base-image             | images/<machine>/tisdk-base-image-<machine>.rootfs.tar.xz      | Minimal Target Filesytem   |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | tisdk-thinlinux-image        | images/<machine>/tisdk-thinlinux-image-<machine>.rootfs.tar.xz | Minimal Target Filesytem   |
      |                              |                                                                | with docker enabled        |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | meta-toolchain-arago-tisdk   | sdk/arago-<arago-version>-<architecture>.sh                    | Devkit                     |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | mc:k3r5:meta-toolchain-arago | sdk/arago-<arago-version>-<architecture>.sh                    | K3R5 baremetal toolchain   |
      +------------------------------+----------------------------------------------------------------+----------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      +------------------------------+----------------------------------------------------------------+----------------------------+
      | Target                       | Build Output                                                   | Description                |
      +==============================+================================================================+============================+
      | tisdk-default-image          | images/<machine>/tisdk-default-image-<machine>.rootfs.tar.xz   | Target Filesystem          |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | tisdk-jailhouse-image        | images/<machine>/tisdk-jailhouse-image-<machine>.rootfs.tar.xz | Jailhouse Filesystem       |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | tisdk-evse-image             | images/<machine>/tisdk-evse-image-rt-<machine>.rootfs.tar.xz   | EV Charging Filesystem     |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | tisdk-base-image             | images/<machine>/tisdk-base-image-<machine>.rootfs.tar.xz      | Minimal Target Filesytem   |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | tisdk-thinlinux-image        | images/<machine>/tisdk-thinlinux-image-<machine>.rootfs.tar.xz | Minimal Target Filesytem   |
      |                              |                                                                | with docker enabled        |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | meta-toolchain-arago-tisdk   | sdk/arago-<arago-version>-<architecture>.sh                    | Devkit                     |
      +------------------------------+----------------------------------------------------------------+----------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      +------------------------------+----------------------------------------------------------------+----------------------------+
      | Target                       | Build Output                                                   | Description                |
      +==============================+================================================================+============================+
      | tisdk-default-image          | images/<machine>/tisdk-default-image-<machine>.rootfs.tar.xz   | Target Filesystem          |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | tisdk-base-image             | images/<machine>/tisdk-base-image-<machine>.rootfs.tar.xz      | Minimal Target Filesytem   |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | tisdk-thinlinux-image        | images/<machine>/tisdk-thinlinux-image-<machine>.rootfs.tar.xz | Minimal Target Filesytem   |
      |                              |                                                                | with docker enabled        |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | meta-toolchain-arago-tisdk   | sdk/arago-<arago-version>-<architecture>.sh                    | Devkit                     |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | mc:k3r5:meta-toolchain-arago | sdk/arago-<arago-version>-<architecture>.sh                    | K3R5 baremetal toolchain   |
      +------------------------------+----------------------------------------------------------------+----------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM65X')

      +------------------------------+----------------------------------------------------------------+----------------------------+
      | Target                       | Build Output                                                   | Description                |
      +==============================+================================================================+============================+
      | tisdk-default-image          | images/<machine>/tisdk-default-image-<machine>.tar.xz          | Target Filesystem          |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | tisdk-base-image             | images/<machine>/tisdk-base-image-<machine>.tar.xz             | Minimal Target Filesytem   |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | tisdk-thinlinux-image        | images/<machine>/tisdk-thinlinux-image-<machine>.tar.xz        | Minimal Target Filesytem   |
      |                              |                                                                | with docker enabled        |
      +------------------------------+----------------------------------------------------------------+----------------------------+
      | meta-toolchain-arago-tisdk   | sdk/arago-<arago-version>-<architecture>.sh                    | Devkit                     |
      +------------------------------+----------------------------------------------------------------+----------------------------+

.. ifconfig:: CONFIG_sdk in ('j7_foundational')

   +------------------------------+---------------------------------------------------------------+----------------------------+
   | Target                       | Build Output                                                  | Description                |
   +==============================+===============================================================+============================+
   | tisdk-core-bundle            | images/<machine>/tisdk-core-bundle-<machine>.tar.xz           | Full SDK                   |
   +------------------------------+---------------------------------------------------------------+----------------------------+
   | tisdk-default-image          | images/<machine>/tisdk-default-image-<machine>.tar.xz         | Target Filesystem          |
   +------------------------------+---------------------------------------------------------------+----------------------------+
   | tisdk-base-image             | images/<machine>/tisdk-base-image-<machine>.tar.xz            | Minimal Target Filesytem   |
   +------------------------------+---------------------------------------------------------------+----------------------------+
   | tisdk-thinlinux-image        | images/<machine>/tisdk-thinlinux-image-<machine>.tar.xz       | Minimal Target Filesytem   |
   |                              |                                                               | with docker enabled        |
   +------------------------------+---------------------------------------------------------------+----------------------------+
   | meta-toolchain-arago-tisdk   | sdk/arago-<arago-version>-<architecture>.sh                   | Linux glibc toolchain      |
   +------------------------------+---------------------------------------------------------------+----------------------------+
   | mc:k3r5:meta-toolchain-arago | sdk/arago-<arago-version>-<architecture>.sh                   | K3R5 baremetal toolchain   |
   +------------------------------+---------------------------------------------------------------+----------------------------+

.. ifconfig:: CONFIG_sdk in ('JACINTO')

   +------------------------------+---------------------------------------------------------------+----------------------------+
   | Target                       | Build Output                                                  | Description                |
   +==============================+===============================================================+============================+
   | tisdk-core-bundle            | images/<machine>/tisdk-core-bundle-<machine>.tar.xz           | Full SDK                   |
   +------------------------------+---------------------------------------------------------------+----------------------------+
   | tisdk-default-image          | images/<machine>/tisdk-default-image-<machine>.tar.xz         | Target Filesystem          |
   +------------------------------+---------------------------------------------------------------+----------------------------+
   | tisdk-edgeai-image           | images/<machine>/tisdk-edgeai-image-<machine>.tar.xz          | Target EdgeAI Filesystem   |
   +------------------------------+---------------------------------------------------------------+----------------------------+
   | tisdk-adas-image             | images/<machine>/tisdk-adas-image-<machine>.tar.xz            | Target Adas Filesystem     |
   +------------------------------+---------------------------------------------------------------+----------------------------+
   | tisdk-base-image             | images/<machine>/tisdk-base-image-<machine>.tar.xz            | Minimal Target Filesytem   |
   +------------------------------+---------------------------------------------------------------+----------------------------+
   | tisdk-thinlinux-image        | images/<machine>/tisdk-thinlinux-image-<machine>.tar.xz       | Minimal Target Filesytem   |
   |                              |                                                               | with docker enabled        |
   +------------------------------+---------------------------------------------------------------+----------------------------+
   | meta-toolchain-arago-tisdk   | sdk/arago-<arago-version>-<architecture>.sh                   | Linux glibc toolchain      |
   +------------------------------+---------------------------------------------------------------+----------------------------+
   | mc:k3r5:meta-toolchain-arago | sdk/arago-<arago-version>-<architecture>.sh                   | K3R5 baremetal toolchain   |
   +------------------------------+---------------------------------------------------------------+----------------------------+

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

   .. rubric:: Platforms

   Please refer to :ref:`here <yocto-layer-configuration>` for the yocto build platforms supported in |__SDK_FULL_NAME__|.
   These are the <machine> used in the command:

   ``MACHINE=<machine> bitbake <target>``

   .. ifconfig:: CONFIG_part_variant in ('J721E')

      +-------------------------------+-----------------------------------------------------------------------+
      | **MACHINE**                   | **Supported EVMs**                                                    |
      +-------------------------------+-----------------------------------------------------------------------+
      | |__SDK_BUILD_MACHINE__|       | J721E EVM, TDA4VM SK                                                  |
      +-------------------------------+-----------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('J721S2')

      .. ifconfig:: CONFIG_sdk in ('j7_foundational')

         +-------------------------------+-----------------------------------------------------------------------+
         | **MACHINE**                   | **Supported EVMs**                                                    |
         +-------------------------------+-----------------------------------------------------------------------+
         | |__SDK_BUILD_MACHINE__|       | AM68 SK                                                               |
         +-------------------------------+-----------------------------------------------------------------------+

      .. ifconfig:: CONFIG_sdk in ('JACINTO')

         +-------------------------------+-----------------------------------------------------------------------+
         | **MACHINE**                   | **Supported EVMs**                                                    |
         +-------------------------------+-----------------------------------------------------------------------+
         | j721s2-evm                    | J721S2 EVM                                                            |
         +-------------------------------+-----------------------------------------------------------------------+
         | am68-sk                       | AM68A SK                                                              |
         +-------------------------------+-----------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('J784S4')

      .. ifconfig:: CONFIG_sdk in ('j7_foundational')

         +-------------------------------+-----------------------------------------------------------------------+
         | **MACHINE**                   | **Supported EVMs**                                                    |
         +-------------------------------+-----------------------------------------------------------------------+
         | |__SDK_BUILD_MACHINE__|       | AM69 SK                                                               |
         +-------------------------------+-----------------------------------------------------------------------+

      .. ifconfig:: CONFIG_sdk in ('JACINTO')

         +-------------------------------+-----------------------------------------------------------------------+
         | **MACHINE**                   | **Supported EVMs**                                                    |
         +-------------------------------+-----------------------------------------------------------------------+
         | j784s4-evm                    | J784S4 EVM                                                            |
         +-------------------------------+-----------------------------------------------------------------------+
         | am69-sk                       | AM69A SK                                                              |
         +-------------------------------+-----------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('J742S2')

      +-------------------------------+-----------------------------------------------------------------------+
      | **MACHINE**                   | **Supported EVMs**                                                    |
      +-------------------------------+-----------------------------------------------------------------------+
      | |__SDK_BUILD_MACHINE__|       | J742S2 EVM                                                            |
      +-------------------------------+-----------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('J7200')

      +-------------------------------+-----------------------------------------------------------------------+
      | **MACHINE**                   | **Supported EVMs**                                                    |
      +-------------------------------+-----------------------------------------------------------------------+
      | |__SDK_BUILD_MACHINE__|       | J7200 EVM                                                             |
      +-------------------------------+-----------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('J722S')

      +-------------------------------+-----------------------------------------------------------------------+
      | **MACHINE**                   | **Supported EVMs**                                                    |
      +-------------------------------+-----------------------------------------------------------------------+
      | |__SDK_BUILD_MACHINE__|       | J722S EVM                                                             |
      +-------------------------------+-----------------------------------------------------------------------+

   .. ifconfig:: CONFIG_rt_linux_support in ('yes')

      .. rubric:: RT Support

      Run the command below, before the bitbake build command, to setup a yocto build with RT Linux Kernel:

      .. code-block:: console

         echo "ARAGO_RT_ENABLE = \"1\"" >> conf/local.conf

      This will tell the Arago yocto setup to pick up RT-Linux Kernel when building any images that depend on the Kernel.
      Alternatively, one can directly build the RT Kernel using below:

      ``MACHINE=<machine> bitbake linux-ti-staging-rt``

.. ifconfig:: CONFIG_sdk in ('SITARA')

   .. rubric:: Platforms
      :name: Platforms

   The following platforms are supported in Processor SDK. These are the
   <machine> in the command:

   ``MACHINE=<machine> bitbake <target>``

   .. ifconfig:: CONFIG_part_variant in ('AM335X')

      +---------------+---------------------------------------------------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                                                                    |
      +---------------+---------------------------------------------------------------------------------------+
      | am335x-evm    | AM335x EVM, AM335x Starter Kit, Beaglebone Black                                      |
      +---------------+---------------------------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM437X')

      +---------------+---------------------------------------------------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                                                                    |
      +---------------+---------------------------------------------------------------------------------------+
      | am437x-evm    | AM437x GP EVM, AM437x Starter Kit                                                     |
      +---------------+---------------------------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM57X')

      +---------------+---------------------------------------------------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                                                                    |
      +---------------+---------------------------------------------------------------------------------------+
      | am57xx-evm    | AM572x GP EVM, AM572x Industrial Development Kit, AM571x Industrial Development Kit   |
      +---------------+---------------------------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      +---------------+-----------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                            |
      +---------------+-----------------------------------------------+
      | am64xx-evm    | AM64x EVM - HS-FS, HS-SE                      |
      +---------------+-----------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      +---------------+-----------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                            |
      +---------------+-----------------------------------------------+
      | am62pxx-evm   | AM62Px EVM - HS-FS, HS-SE                     |
      +---------------+-----------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('J722S')

      +---------------+-----------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                            |
      +---------------+-----------------------------------------------+
      | j722s-evm     | J722S EVM - HS-FS, HS-SE                      |
      +---------------+-----------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      +------------------+--------------------------------------------+
      | **MACHINE**      | **Supported EVMs**                         |
      +------------------+--------------------------------------------+
      | am62xx-evm       | AM62x Starter Kit (SK) - GP, HS-FS, HS-SE  |
      +------------------+--------------------------------------------+
      | am62xx-lp-evm    | AM62x LP Starter Kit (SK) - HS-FS, HS-SE   |
      +------------------+--------------------------------------------+
      | beagleplay-ti    | BEAGL-PLAY-SBC - GP                        |
      +------------------+--------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62AX')

      +---------------+---------------------------------------------------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                                                                    |
      +---------------+---------------------------------------------------------------------------------------+
      | am62axx-evm   | AM62A Starter Kit (SK)                                                                |
      +---------------+---------------------------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM65X')

      +---------------+-----------------------------------------------------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                                                                      |
      +---------------+-----------------------------------------------------------------------------------------+
      | am65xx-evm    | AM65x Evaluation Module, AM65x Industrial Development Kit, DRA80xM Evaluation Module    |
      +---------------+-----------------------------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      +---------------+-----------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                            |
      +---------------+-----------------------------------------------+
      | am62lxx-evm   | AM62L EVM - HS-FS                             |
      +---------------+-----------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM335X')

      +--------------+---------------------------------------------------------------------------------------+
      | **MACHINE**  | **Supported EVMs**                                                                    |
      +--------------+---------------------------------------------------------------------------------------+
      | am335x-evm   | AM335x EVM, AM335x Industrial Communications Engine                                   |
      +--------------+---------------------------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM437X')

      +---------------+--------------------------------------------------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                                                                   |
      +---------------+--------------------------------------------------------------------------------------+
      | am437x-evm   | AM437x GP EVM, AM437x Industrial Development Kit                                      |
      +--------------+---------------------------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM57X')

      +---------------+--------------------------------------------------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                                                                   |
      +---------------+--------------------------------------------------------------------------------------+
      | am57xx-evm   | AM572x GP EVM, AM574x Industrial Development Kit,                                     |
      |              | AM572x Industrial Development Kit, AM571x Industrial Development Kit                  |
      +--------------+---------------------------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      +---------------+-----------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                            |
      +---------------+-----------------------------------------------+
      | am64xx-evm    | AM64x EVM - HS-FS, HS-SE                      |
      +---------------+-----------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      +---------------+-----------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                            |
      +---------------+-----------------------------------------------+
      | am62pxx-evm   | AM62Px EVM - HS-FS, HS-SE                     |
      +---------------+-----------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      +------------------+--------------------------------------------+
      | **MACHINE**      | **Supported EVMs**                         |
      +------------------+--------------------------------------------+
      | am62xx-evm       | AM62x Starter Kit (SK) - GP, HS-FS, HS-SE  |
      +------------------+--------------------------------------------+
      | am62xx-lp-evm    | AM62x LP Starter Kit (SK) - HS-FS, HS-SE   |
      +------------------+--------------------------------------------+
      | beagleplay-ti    | BEAGL-PLAY-SBC - GP                        |
      +------------------+--------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM65X')

      +---------------+-----------------------------------------------------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                                                                      |
      +---------------+-----------------------------------------------------------------------------------------+
      | am65xx-evm    | AM65x Evaluation Module, AM65x Industrial Development Kit, DRA80xM Evaluation Module    |
      +---------------+-----------------------------------------------------------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      +---------------+-----------------------------------------------+
      | **MACHINE**   | **Supported EVMs**                            |
      +---------------+-----------------------------------------------+
      | am62lxx-evm   | AM62L EVM - HS-FS                             |
      +---------------+-----------------------------------------------+

.. _building-the-sdk-recipes:

Recipes
-------

.. rubric:: Recipe Basics
   :name: Recipe Basics

One or more recipes can be specified for the <target> for greater
granularity of recipe development and debug. Specifying a recipe name,
minus the version (if the version is appended to the name), will build
the recipe and all its dependencies.

For example, the following command builds only the zlib recipe and all the
dependencies it defines.

.. code-block:: console

   MACHINE=<machine> bitbake zlib

After the preceding bitbake command completes successfully, the
:file:`arago-tmp-default-glibc/work/aarch64-oe-linux/zlib` directory gets created.
It has the original source code, shared objects (.so files) in the packages-split folder
and IPK packages in the deploy-ipks folder.

.. note::

   Please note that the output of a recipe can be in another folder under :file:`arago-tmp-[toolchain]/work` directory, depending on the defines of the recipe.
   You can call the following command from yocto's build directory to get the path to the workdir of your recipe.

   .. code-block:: console

      MACHINE=<machine> bitbake-getvar -r <recipe-name> WORKDIR --value

.. rubric:: Forced Re-compilation
   :name: Forced Re-compilation

When needed, source code under the work directory (e.g.,
:file:`arago-tmp-default-glibc/work/aarch64-oe-linux/zlib/<version>/zlib-<version>`) can
be modified. After the modification is done, run the following commands
to force recompilation with the new code and rebuilding of the recipe,
For example,

.. code-block:: console

   MACHINE=<machine> bitbake zlib --force -c compile
   MACHINE=<machine> bitbake zlib

.. rubric:: Installing Package
   :name: installing-package

To install a modified and rebuilt package, copy the new IPKs from the
deploy-ipks folder (e.g., :file:`arago-tmp-default-glibc/work/aarch64-oe-linux/zlib/<version>/deploy-ipks`)
to the target system and then run the following command to install the IPKs:

.. code-block:: console

   opkg install [package_ipk].ipk

.. rubric:: Cleaning a Built Recipe
   :name: cleaning-a-built-recipe

A built recipe can be entirely cleaned using:

.. code-block:: console

   MACHINE=<machine> bitbake <target> -c cleanall

The cleanall task removes all output files, shared state (sstate) cache and downloaded source files for a target (i.e. the contents of DL_DIR)

See also
========

General information on Yocto, OpenEmbedded and Arago projects can be found at:

-  `Yocto Project <https://yoctoproject.org/>`__
-  `OpenEmbedded <https://openembedded.org/>`__
-  `Arago Project <https://git.yoctoproject.org/meta-arago>`__

