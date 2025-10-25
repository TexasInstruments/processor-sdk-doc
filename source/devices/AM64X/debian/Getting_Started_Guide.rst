.. _overview-getting-started:

***************************
Getting Started with Debian
***************************

The SD card Debian Image provided on the |__SDK_DOWNLOAD_URL__| is all you need to get started and explore
Debian on TI microprocessors.

The Debian Image provided has all the basic packages required to boot with weston as default window manager.
The user can install any new package using Debian's default ``apt`` package manager and customize the
filesystem as desired.

Follow the steps mentioned in this page to flash an SD Card.

Hardware Setup
--------------

In addition to the Evaluation Module (EVM) or the Starter Kit (SK) itself, the following hardware is needed:

-  Barrel jack power supply
-  Micro-SD card reader
-  Micro-SD card (16GB or larger recommended)
-  USB Micro-B cable for UART serial communication
-  Ethernet cable (For network access)

.. _processor-sdk-debian-create-sd-card:

Flash SD Card using balenaEtcher
--------------------------------

#. Download the default bootable SD card image (IMG file) available on the release page:

   ``tisdk-debian-<debian version>-<TI EVM board>-<TI PSDK version>-Armbian-<armbian version>.img``

#. Download and install the balenaEtcher tool:

   Balena Etcher is an open-source utility that can be installed on both Linux and Windows.
   Download the tool from `this link <https://www.balena.io/etcher/>`__ and install it.

#. Flash the IMG image to the SD card:

   Insert a micro SD card into the USB SD card reader and start Etcher. Choose the debian img
   image to be flashed, choose the USB SD card reader as the target, and then click "Flash".
   Etcher will decompress the image and write it to the SD card, as shown below:

   .. image:: /images/balena_etcher.png

Set the EVM to SD card Boot mode
--------------------------------
The simplest way to run Linux on the EVM or SK is through an SD card. For that, configure the EVM or SK for SD card boot mode. Refer to
`AM64x EVM User's Guide <https://www.ti.com/tool/TMDS64EVM>`__ or `AM64x SK User's Guide <https://www.ti.com/tool/SK-AM64B>`__ (depending on the device)
for detailed information about boot mode configurations. For quick reference, the figure below shows the boot mode switch setting for SD card boot.

.. image:: /images/AM64x_SD_boot.jpg

Boot and Validate Debian
------------------------
Make sure to connect the UART and Ethernet cable to the EVM. Insert the SD Card in the board and Power ON the EVM.

After approximately 20 seconds, the board should boot and you should see the on-board LED glowing.

During first bootup, a setup script will run. This script guides the user through setting up user account, root password, date and so on.
Once the setup ends, reboot the board.

To verify the distro, connect via the UART console and try running ``neofetch`` on the terminal. The output of the command can be observed on the screen as shown below.

.. image:: /images/debian_neofetch.png

You've successfully booted Debian on |__PART_FAMILY_DEVICE_NAMES__|.

If the board is connected to a private network, setup the proxy to be able to access the Internet.
For more info, refer to `apt.conf(5) man page <https://manpages.debian.org/trixie/apt/apt.conf.5.en.html>`__

Also export ``http_proxy``, ``https_proxy``, ``ftp_proxy`` and ``no_proxy`` with appropriate values if needed.

Do an ``apt update`` to make sure that the proxy is properly set and apt recognizes it. The sample output of the command is as shown below:.

.. image:: /images/debian_apt_update.png

To install any package available on Debian Standard Package Archive and TI Package Archive use ``apt install``.

As an example to install and run ``fortune`` package.

.. image:: /images/debian_apt_install.png

More packages can be installed at runtime following the instructions provided to help with the development work flow.

