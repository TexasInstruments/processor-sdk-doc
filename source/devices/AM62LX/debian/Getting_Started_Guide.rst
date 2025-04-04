.. _overview-getting-started:

***************************
Getting Started with Debian
***************************

The SD card Image tisdk-debian-trixie-<machine>-<version>.wic.xz provided on the |__SDK_DOWNLOAD_URL__| is all you need to get started and explore Debian on TI microprocessors.

The Debian Image provided has all the basic packages required to boot with weston as default window manager. The user can install any new package using inbuilt 'apt' utility
and customize the filesystem as required.

Follow the steps mentioned in this page to create an SD Card.

Hardware Setup
--------------

In addition to the EVM itself, the following hardware is needed:

1. USB Type-C 5V - 15V and 3A power supply
2. Micro-SD card reader
3. Micro-SD card (16GB or larger recommended)
4. USB Micro-B cable for UART serial communication
5. HDMI display and HDMI cable
6. USB mouse and Keyboard (For controlling the UI)
7. Ethernet cable (For network access)

.. _processor-sdk-debian-create-sd-card:

Create SD Card using balenaEtcher
---------------------------------

1.  Download the default bootable SD card image (WIC file) available on the release page as
    tisdk-debian-trixie-<machine>-<version>.wic.xz

|

2.  Download and install the balenaEtcher tool:

        Balena Etcher is an open-source utility that can be installed on both Linux and Windows.
        Download the tool from `this link <https://www.balena.io/etcher/>`__ and install it.

|

3.  Flash the WIC image to the SD card:

        Insert a micro SD card into the USB SD card reader and start Etcher. Choose the debian wic
        image to be flashed, choose the USB SD card reader as the target, and then click "Flash".
        Etcher will decompress the image and write it to the SD card, as shown below:

    .. Image:: /images/balena_etcher.png

|

Set the EVM to SD card Boot mode
--------------------------------
The simplest way to run Linux on the EVM is through an SD card. For that, the EVM will need to be configured for SD card boot. Refer to `AM62L EVM User's Guide <https://www.ti.com/tool/EVM-AM62L>`__ for detailed information about boot mode configurations. For quick reference, the figure below shows the boot mode switch setting for SD card boot.

.. Image:: /images/AM62LX_SD_boot.jpg

Boot and Validate Debian
------------------------
Make sure to connect the Ethernet cable, HDMI Display, Mouse and Keyboard to the EVM. Insert the SD Card in the board and Power ON the EVM.

After a few seconds, the boot prompt will appear. After boot, the weston homescreen will appear.

.. Image:: /images/debian_homescreen.png

You've successfully booted Debian on AM62L.

If the board is connected to a private network, setup the proxy to be able to access the Internet.
For more info, refer to `apt.conf(5) man page <https://manpages.debian.org/bookworm/apt/apt.conf.5.en.html>`__

Also export ``http_proxy``, ``https_proxy``, ``ftp_proxy`` and ``no_proxy`` with appropriate values if needed.

Do an ``apt update`` to make sure that the proxy is properly set and apt recognizes it. The sample output of the command is as shown below:.

.. Image:: /images/debian_am62l_apt_update.png

To install any package available on Debian Standard Package Archive and TI Package Archive use ``apt install``.

As an example to install and run ``fortune`` package.

.. Image:: /images/debian_am62l_apt_install.png

More packages can be installed at runtime following the instructions provided to help with the development work flow.

