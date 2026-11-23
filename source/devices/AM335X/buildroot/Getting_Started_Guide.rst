##########################
Get started with Buildroot
##########################

The SD card image sdcard.img provided on the |__SDK_DOWNLOAD_URL__| is all you
need to get started and explore Buildroot on TI microprocessors.

The Buildroot image provided has all the basic packages required to boot with
Weston as default window manager. You can install any new package and
customize the filesystem as required.

Follow the steps on this page to create an SD card image.

**************
Hardware setup
**************

In addition to the SK Evaluation Module (EVM) itself, you need the following hardware:

1. USB Type-C 5V - 15V and 3A power supply
2. Micro-SD card reader
3. Micro-SD card (16GB or larger recommended)
4. USB Micro-B cable for Universal Asynchronous Receiver/Transmitter (UART) serial communication
5. High-Definition Multimedia Interface (HDMI) display and HDMI cable
6. USB mouse and keyboard (for controlling the UI)
7. Ethernet cable (for network access)

*********************************
Create SD card using balenaEtcher
*********************************

1.  Download the default bootable SD card image available on the release page as
    :file:`tisdk-buildroot-sdcard-image-am335xx-evm-<version>.img` for Linux image
    or :file:`tisdk-buildroot-sdcard-image-rt-am335xx-evm-<version>.img` for RT-Linux
    image.

2.  Download and install the balenaEtcher tool:

        Balena Etcher is an open-source utility that can be installed on both Linux and Windows.
        Download the tool from `this link <https://www.balena.io/etcher/>`__ and install it.

3.  Flash the SD Card image to the SD card:

        Insert a micro SD card into the USB SD card reader and start Etcher. Choose the sdcard
        image to flash, choose the USB SD card reader as the target, and then click "Flash".
        Etcher will decompress the image and write it to the SD card, as shown in the following figure:

.. figure:: /images/balena_etcher.png
    :height: 600
    :width: 800

********************************
Set the EVM to SD card Boot mode
********************************

The simplest way to run Linux on the SK EVM is through an SD card. For that, you must
configure the EVM for SD card boot.
Refer to `AM335x SK EVM User's Guide <https://www.ti.com/tool/BEAGL-BONE-GRN-ECO>`__ for
detailed information about boot mode configurations.

***************************
Boot and Validate Buildroot
***************************

Make sure to connect the Ethernet cable, HDMI Display, Mouse and Keyboard to the EVM.
Insert the SD Card in the board and Power ON the EVM.

Booting to prompt will take around 12 seconds.


You've successfully booted Buildroot on AM335x(BEAGL-BONE-GRN-ECO).
