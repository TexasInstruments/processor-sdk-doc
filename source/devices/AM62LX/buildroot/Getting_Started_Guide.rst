##############################
Getting Started with Buildroot
##############################

The SD card Image sdcard.img provided on the |__SDK_DOWNLOAD_URL__| is all you
need to get started and explore Buildroot on TI microprocessors.

The Buildroot Image provided has all the basic packages required to boot with
Weston as default window manager. The user can install any new package and
customize the filesystem as required.

Follow the steps mentioned in this page to create an SD card Image.

**************
Hardware Setup
**************

In addition to the EVM itself, the following hardware is needed:

1. USB Type-C 5V - 15V and 3A power supply
2. Micro-SD card reader
3. Micro-SD card (16GB or larger recommended)
4. USB Micro-B cable for UART serial communication
5. HDMI display and HDMI cable
6. USB mouse and Keyboard (For controlling the UI)
7. Ethernet cable (For network access)

*********************************
Create SD Card using balenaEtcher
*********************************

1.  Download the default bootable SD card image available on the release page as
    :file:`tisdk-buildroot-sdcard-image-am62lxx-evm-<version>.img` for Linux image
    or :file:`tisdk-buildroot-sdcard-image-rt-am62lxx-evm-<version>.img` for RT-Linux
    image.

2.  Download and install the balenaEtcher tool:

        Balena Etcher is an open-source utility that can be installed on both Linux and Windows.
        Download the tool from `this link <https://www.balena.io/etcher/>`__ and install it.

3.  Flash the SD Card image to the SD card:

        Insert a micro SD card into the USB SD card reader and start Etcher. Choose the sdcard
        image to be flashed, choose the USB SD card reader as the target, and then click "Flash".
        Etcher will decompress the image and write it to the SD card, as shown below:

.. figure:: /images/balena_etcher.png
    :height: 600
    :width: 800

********************************
Set the EVM to SD card Boot mode
********************************

The simplest way to run Linux on the EVM is through an SD card. For that, the
EVM will need to be configured for SD card boot.
Refer to `AM62L EVM User's Guide <https://www.ti.com/tool/EVM-AM62L>`__ for
detailed information about boot mode configurations. For quick reference,
the figure below shows the boot mode switch setting for SD card boot.

.. figure:: /images/AM62x_SD_boot.jpg
    :height: 600
    :width: 800

***************************
Boot and Validate Buildroot
***************************

Make sure to connect the Ethernet cable, HDMI Display, Mouse and Keyboard to the EVM.
Insert the SD Card in the board and Power ON the EVM.

After few seconds the booting prompt will appear.

.. figure:: /images/buildroot_homescreen.png
    :height: 600
    :width: 800

You've successfully booted Buildroot on AM62L.
