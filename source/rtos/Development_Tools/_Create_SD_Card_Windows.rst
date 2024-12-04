.. _windows-sd-card-creation-guide:

Windows SD Card Creation Guide
===============================

.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_Creating_a_SD_Card_with_Windows

Overview
----------

This page details how to use an image file to create a bootable SD card
for the Processor SDK RTOS for AM3/AM4/AM5/K2G. This is only required
one time. After that, you can use Windows to delete the SD card contents
and replace it with whatever you would like to boot.

The contents of an bootable RTOS application will contain two files on
the SD card:

-  **app** - Application image
-  **MLO** - Boot loader image


.. tip::
   If you have the SD card that came in the EVM kit, you can skip the
   following steps to *create* a bootable SD card and simply copy your
   SD card image files directly to the SD card.

|

What is Needed
----------------

-  Access to a Windows PC
-  A valid Processor SDK RTOS for the appropriate processor installed
   (AM335x, AM437x, AM57xx, K2G)
-  Software to write an image file to a SD card
-  A SD card appropriate for the required hardware platform, must be 1GB
   or larger
-  A SD card reader/writer

|

Steps to Follow
-----------------

Here is the process to follow to create the SD card.

Create a bootable SD image file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For example purposes, you can use the one that is bundled in the SDK.
The file is located in

::

     [SDK Install Path]\processor_sdk_rtos_<platform>_<version>\prebuilt-sdcards\<evm>\sd_card_img\

For example, the default location of the image file for the GP AM57x EVM
is
``C:\processor_sdk_rtos_am57xx_2_00_00_00\prebuilt-sdcards\evmAM572x\sd_card_img\sd_card.img.gz``.
To save installer space, this file is compressed. Once uncompressed, the
file name will be ``boot.img``.

.. rubric:: Download a disk imager program to write the image file to
   the SD card
   :name: download-a-disk-imager-program-to-write-the-image-file-to-the-sd-card

The open source `Win32 Disk
Imager <http://sourceforge.net/projects/win32diskimager>`__ is a good
option.

.. note::
   This application needs to be installed with Administrative privilages.

Use the software for writing an image to disk to write the .img file to the SD card
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
-  Plug the SD card into the SD card reader/writer.
-  Insert the SD card reader/writer into the PC.
-  Launch the disk writer software. In the screenshots below, we are
   using *Win32 Disk Imager*.

.. Image:: /images/Win32_Disk_Imager_open.png

-  Choose the image file for the SDK that you want to write.

.. Image:: /images/Win32_disk_imager_select_a_disk_image.png

-  Choose the SD card as the "Device".
-  Write the image to the SD card by click "Write". You will likely get
   the below confirmation box. This command will overwrite whatever disk
   you point it to, please make sure and choose the correct disk.

.. Image:: /images/Win32_disk_imager_Confirm_overwrite.png

-  You should see the following status bar as the image is being written
   to the disk:

.. Image:: /images/Win32_Disk_Imager_writing_to_disk.png

-  When the write is complete, you will get the following notification:

.. Image:: /images/Win32_Disk_Imager_Complete.png

-  You can now close the image writing program by click "Exit".

Limitations to the WinDisk32 SD card utility and alternate options
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The WinDisk32 utility described in the sections above is used to format the SD card to FAT format and copy an 1GB SD card image to the SD card. While, this utility formats the SD card in FAT format recognized by all the ROM bootloader supported on Sitara and K2G devices, it limits the storage capacity of larger volume SD cards to 1 GB volume. The utility is designed to update the SD card volume information to match the size of the image copied to its volume. This can result in large portion of the volume being unused on the SD cards. You can restore the volume on the SD card using linux based SD formatting utilities. This section describes some options to the WinDisk32 utility that we have tested with the ROM bootloader on devices supported in Processor SDK.


**SDcard.org Formatter Utility**


K2G and AM437x users, can use the formatting utility provided by SDCard.org for booting an SD card on TI evaluation platforms. This utility formats the SD cards in a way by which it retains the original size and also in a format recognized by the ROM bootloader.

.. note:: This utility is not compatible with AM335x and AM57xx devices due the FAT format restrictions in the ROM bootloader on those devices.

You can follow the instructions provide below:

1. Download `SD Card Formatter 4.0 for SD/SDHC/SDXC <https://www.sdcard.org/downloads/formatter_4/>`_ from the internet.

2. Insert the SD card into a USB based or similar SD card reader/writer on the host Windows system.

3. Run the SD Card Formatter 4.0 for SD/SDHC/SDXC Portable executable. The executable should automatically detect the SD card plugged via reader as a new 'removable disk' and populate the drive corresponding to the removable disk. Else you will need to manually point it to the new disk.

.. Image:: /images/SDFormatter_screenshot.png

4. Choose default settings (as shown above)if it is new SD card and Click on 'Format'. For previously used SD cards, you can choose "FULL" by clicking on Options menu to erase and format the SD card.

5. You should see a pop up window that indicates progress of the formatting tool. The Quick format option usually takes a few seconds. The following message will be displayed when the formatting is completed.

.. Image:: /images/SDF_Format_complete.png

6. Copy the MLO (boot loader) to the formatted SD Card.

7. Rename application boot binary as "app" and copy it to SD Card.

8. You can now insert the SD card in the TI evaluation platform and boot the platform in SD boot.

.. Note:: Bootmode switches are set for MMC/SD boot. See the `Hardware User's Guide <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_release_specific.html#supported-platforms-and-versions/>`_ for the evaluation platform for details.


**HP USB Disk Storage Format Tool v2.0.6 (works with AM335x and AM437x devices)**


For AM335x and AM437x users, you can opt to use HP USB Disk Storage Format Tool v2.0.6. This allows users to format the SD cards without modifying its volume and also uses a FAT32 format that is recognized by the ROM bootloader. However this utility may use FAT12 format for smaller volume(<4GB) SD cards.

You can follow the instructions provide below:

1. Download `HP USB Disk Storage Format Tool v2.0.6 Portable <https://www.google.co.in/search?q=HP+USB+Disk+Storage+Format+Tool+v2.0.6&hl=en&source=hp&gbv=2&gs_sm=e&gs_upl=1235l14547l0l16813l14l12l1l0l0l0l297l2500l0.4.7l11l0&safe=active&oq=HP+USB+Disk+Storage+Format+Tool+v2.0.6&aq=f&aqi=g3&aql=&gws_rd=ssl/>`_ from the internet.

2. Choose a SD card and a USB based or similar SD card reader/writer. Plug it to a Windows host system.

3. Run the HP USB Disk Storage Format Tool v2.0.6 Portable executable. The executable should automatically detect the SD card plugged via reader as a new 'removable disk'. Else point it to the new disk.

4. Choose FAT32 if the SD card size is greater that 4GB. Else FAT should be good to go.

5. Click "Format."

6. Copy the MLO (boot loader) to the formatted SD Card.

7. Rename application binary as "app" and copy it to SD Card.

8. Make sure that TI evaluation platform bootmode switches are set for MMC/SD boot. See the `Hardware User's Guide <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_release_specific.html#supported-platforms-and-versions/>`_  for the evaluation platform for details.

9. Attach the SD card to IDK MMC/SD Card slot and switch on TI evaluation platform.


**Use the SD card creation script on Linux platform (works with all platforms)**


This method works with all the platforms. However, this method requires the PDK installation on Linux and using the SD card creation script provided in the installer. Please refer to the `Linux SD Card Creation Guide <http://software-dl.ti.com/processor-sdk-rtos/esd/docs/latest/rtos/index_overview.html#linux-sd-card-creation-guide>`_ for details.

|

.. rubric:: Safely eject the SD card from the computer
   :name: safely-eject-the-sd-card-from-the-computer

| Here's an example using Windows 7:

.. Image:: /images/Win7_eject_disk.png

.. Image:: /images/Win7_eject_disk_detail.png

.. Image:: /images/Win7_device_can_be_safely_removed.png

|

.. note::
   Once SD card is made bootable with Win32 disk imager, it contains sample
   “MLO” and “app” which can be used on the target platform.

|

Boot from SD Card
-------------------

To boot from SD card, simply plug in the SD card to the EVM and power on
the board. If you used the examples provided in the Processor SDK RTOS
installer, you will see

-  AM335x/AM437x:

.. Image:: /images/AM437x-SD-Card-Example.png

-  AM57x:

.. Image:: /images/AM57x-SD-Card-Example.png

