#########################
Building Buildroot Images
#########################

This document provides a step-by-step guide to build a Buildroot image using
the buildroot-external-TI tree.

*************
Prerequisites
*************

    1.  A Linux-based development environment.
    2.  Required packages `Required Packages <https://buildroot.org/downloads/manual/manual.html#requirement>`__.

For Debian/Ubuntu distributions, the necessary packages can be installed with
the following command:

.. code-block:: console

   $ sudo apt install debianutils sed make binutils build-essential gcc g++ bash patch gzip bzip2 perl tar cpio unzip rsync file bc git

************************
Steps to Build the Image
************************

.. _set-up-the-external-tree:

Setting up the External Tree
============================

To set up and use the `buildroot-external-ti` external tree, follow these steps:

1. Clone the Buildroot and external tree repositories:

Buildroot tags for Platforms supported are as follws:

.. list-table::

   * - Repo
     - AM62LX
     - AM62X
   * - https://github.com/buildroot/buildroot
     - 2025.02.x
     - 2025.02.x
   * - https://github.com/TexasInstruments/buildroot-external-TI.git
     - 11.01.16.13
     - 11.01.05.03

You can fetch the repos with an explicit tag using:

.. code-block:: console

   $ git clone -b <tag> https://github.com/buildroot/buildroot
   $ git clone -b <tag> https://github.com/TexasInstruments/buildroot-external-TI.git

2. Configure Buildroot to use the external tree and choose a configuration file

.. code-block:: console

   $ cd buildroot
   During configuration
   $ make BR2_EXTERNAL=<path to external tree>/buildroot-external-TI <configuration file>
   OR
   export BR2_EXTERNAL=<path to external tree>/buildroot-external-TI

Select the Build Configuration
==============================

Buildroot uses a configuration file to determine which packages and settings to
use for the build. The buildroot-external-TI repository should provide one or more
configuration files tailored to a specific board. Select the appropriate
configuration file for your target device.

   Use the following table to determine what defconfig to use to configure with:

      +----------------------------+---------------------------------------------+
      |  Board                     |            Configuration file               |
      +============================+=============================================+
      |    AM62X-SK evm            |   ti\_release\_am62x\_sk\_defconfig         |
      +----------------------------+---------------------------------------------+
      |    AM62LX-evm              |   ti\_release\_am62lx\_evm\_defconfig       |
      +----------------------------+---------------------------------------------+


   .. code-block:: console

         $ cd buildroot
         $ make <defconfig>
         For example,
         $ make ti_release_am62x_sk_defconfig


Customize the Configuration
===========================

If necessary, you can customize the configuration further using the menuconfig
interface. This step is optional but useful if you need to make specific adjustments.

.. code-block:: console

   $ make menuconfig

Build the Image
===============

With the configuration set, you can now build the image. This process compiles
the necessary components and creates the root filesystem, kernel, and bootloader.

TI_K3_BOOT_FIRMWARE_VERSION will be as follows:

.. list-table::

   * - Platform
     - version_tag
   * - AM62X
     - 11.01.05
   * - AM62LX
     - 11.01.16


.. code-block:: console

   $ make TI_K3_BOOT_FIRMWARE_VERSION=<version_tag>

   For Example, version_tag will be 11.01.05 or 10.01.10
   $ make TI_K3_BOOT_FIRMWARE_VERSION=11.01.05

The build process can take some time, depending on your system's resources and
the complexity of the configuration.

Locate the Output Files
=======================

Once the build is complete, the generated files will be located in the :file:`output/images`
directory. These files typically include the root filesystem image, the kernel
image, and the bootloader.

You will find files ex. flashable SD card image :file:`sdcard.img`, root filesytems
:file:`rootfs.ext4` along with other build output files.

Flash the Image to SD Card
==========================

The final step is to flash the generated images to your target device. The specific
steps for flashing will depend on your hardware. Common methods include using dd
to write the image to an SD card or using a tool like
`Balena Etcher <https://etcher.balena.io/>`__. for USB flashing.

Example for SD card:

.. code-block:: console

   $ sudo dd if=output/images/sdcard.img of=/dev/sdX
   $ sync
   Replace /dev/sdX with the appropriate device identifier for your SD card.

Booting the SD Card Image
=========================

After the image is flashed to SD Card. Change the boot mode pins in
|__PART_FAMILY_NAME__| board for SD Card boot.

.. code-block:: console

   SW1[1:8] = 11000010 and SW2[1:8] = 01000000

Insert the SD Card in SD Card slot in |__PART_FAMILY_NAME__| board. Use a
USB Micro-B cable to connect the host PC to the USB Micro-B interface for UART
on the EVM then power on the board, the following logs can be observed on the
terminal window:

.. code-block:: console

   Trying to boot from MMC2
   ...
   ...
   ...
   Starting network: [    2.823578] am65-cpsw-nuss 8000000.ethernet eth0: PHY [8000f00.mdio:00] driver [TI DP83867] (irq=POLL)
   [    2.823635] am65-cpsw-nuss 8000000.ethernet eth0: configuring for phy/rgmii-rxid link mode
   udhcpc: started, v1.36.1
   udhcpc: broadcasting discover
   udhcpc: no lease, forking to background
   [    5.944022] am65-cpsw-nuss 8000000.ethernet eth1: PHY [8000f00.mdio:01] driver [TI DP83867] (irq=POLL)
   [    5.944130] am65-cpsw-nuss 8000000.ethernet eth1: configuring for phy/rgmii-rxid link mode
   udhcpc: started, v1.36.1
   udhcpc: broadcasting discover
   udhcpc: no lease, forking to background
   OK

   Welcome to Buildroot
   buildroot login: root
   #

*************
Going further
*************

For more detailed information, refer to the `Buildroot manual <https://buildroot.org/downloads/manual/manual.html>`__.
