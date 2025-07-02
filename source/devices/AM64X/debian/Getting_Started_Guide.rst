.. _overview-getting-started:

***************************
Getting Started with Debian
***************************

The SD card Image tisdk-debian-bookworm-<machine> provided on the |__SDK_DOWNLOAD_URL__| is all you need to get started and explore Debian on TI microprocessors.

The user can install any new package by using inbuilt 'apt' utility and customize the filesystem as required.

Follow the steps mentioned in this page to create an SD Card.

Hardware Setup
--------------

In addition to the Evaluation Module (EVM) or the Starter Kit itself, use the following hardware:

1. Barrel jack power supply
2. Micro-SD card reader
3. Micro-SD card (16GB or larger recommended)
4. USB Micro-B cable for UART serial communication
5. Ethernet cable (For network access)

Create SD Card using balenaEtcher
---------------------------------

1.  Download the default bootable SD card image (WIC file) available on the release page as
    tisdk-debian-bookworm-<machine>.wic.xz

|

2.  Download and install the balenaEtcher tool:

        Balena Etcher is an open-source utility that can be installed on both Linux and Windows.
        Download the tool from `this link <https://www.balena.io/etcher/>`__ and install it.

|

3.  Flash the WIC image to the SD card:

        Insert a micro SD card into the USB SD card reader and start Etcher. Choose the debian wic
        image to be flashed, choose the USB SD card reader as the target, and then click "Flash".
        Etcher will decompress the image and write it to the SD card, as shown in the following:

    .. Image:: /images/balena_etcher.png

|

Set the EVM to SD card Boot mode
--------------------------------
The simplest way to run Linux on the SK EVM is through an SD card. For that, configure the EVM in SD card boot mode. Refer to `AM64x SK EVM User's Guide <https://www.ti.com/tool/SK-AM64B>`__ or the `TMDS64EVM User's Guide <https://www.ti.com/tool/TMDS64EVM>`__ (depending on the device) for detailed information about boot mode configurations. For quick reference, the following figure shows the boot mode switch setting for SD card boot.

.. Image:: /images/AM64x_SD_boot.jpg

Boot and Validate Debian
------------------------
Make sure to connect the UART and Ethernet cable to the EVM. Insert the SD Card in the board and Power ON the EVM.

After approximately 20 seconds, the board should boot and you should see the on-board LED glowing.

You've successfully booted Debian on AM64x.

To verify the distro, connect via the UART console and try running ``neofetch`` on the terminal. The output of the command can be observed on the screen as shown below.

.. Image:: /images/debian_neofetch.png

If the board is connected to a private network, setup the proxy to be able to access the Internet.
For more info, refer to `apt.conf(5) man page <https://manpages.debian.org/bookworm/apt/apt.conf.5.en.html>`__

Also export ``http_proxy``, ``https_proxy``, ``ftp_proxy`` and ``no_proxy`` with appropriate values if needed.

Do an ``apt update`` to make sure that the proxy is properly set and apt recognizes it. The sample output of the command is as shown below:.

.. Image:: /images/debian_apt_update.png

To install any package available on Debian Standard Package Archive and TI Package Archive use ``apt install``.

As an example to install and run ``fortune`` package.

.. Image:: /images/debian_apt_install.png

More packages can be installed at runtime following the instructions provided to help with the development work flow.

