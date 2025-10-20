.. http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_Creating_a_SD_Card_with_Windows

Windows SD Card Creation Guide
======================================
.. rubric:: Introduction
   :name: introduction-linux-sd-card

This page details how to use an image file to create a SD Card
containing the embedded Linux system provided with the Linux SDK. This
allows a user to evaluate the embedded system on a supported hardware
platform.

.. rubric:: What is Needed
   :name: what-is-needed

-  Access to a Windows PC
-  A valid Linux SDK image for the appropriate processor (AM335x, for
   example)
-  Software to decompress a zip file (ex. 7-zip)
-  Software to write an image file to a SD card
-  A SD card appropriate for the required hardware platform, must be 16GB
   or larger
-  A SD card reader/writer

.. rubric:: Steps to Follow
   :name: steps-to-follow

Here is the process to follow to create the SD card.

#. Download the Processor SDK for Linux image file that you want to use.
#. On a Windows PC, you'll need software to decompress a zip file.
   Windows 7 can do this natively. If you don't already have something
   that works, the open source software `7-zip <http://www.7-zip.org>`__
   is a great choice. Since this image is created with lots of empty
   space, this step saves about 700 MB of download time.
#. Use the decompression software to decompress the zipped file to an
   image file. Here's how to do it with 7-zip:

   .. Image:: /images/7zip_to_extract_image.png

   You should see a status bar as the image is decompressed:

   .. Image:: /images/Win32_Disk_Imager_Extracting.png

   And this is what you should have when it is finished:

   .. Image:: /images/7zip_image_file_extracted.png

#. If you don't have it already, download a program to write the image
   file to the SD card. The open source `Win32 Disk
   Imager <http://sourceforge.net/projects/win32diskimager>`__ is a good
   option.
#. Use the software for writing an image to disk to write the
   decompressed .img file to the SD card.

   #. Plug the SD card into the SD card reader/writer.
   #. Insert the SD card reader/writer into the PC.
   #. Launch the disk writer software, if needed.
   #. Choose the image file for the SDK that you want to write.

      .. Image:: /images/Win32_Disk_Imager_open.png

      And select the appropriate SDK Image file:

      .. Image:: /images/Win32_disk_imager_select_a_disk_image.png

   #. Choose the SD card as the destination.

      .. Image:: /images/Win32_Disk_Imager_select_disk.png

   #. Write the image to the SD card.

      .. Image:: /images/Win32_Disk_Imager_write_disk.png

      .. note::
          You'll likely get the below confirmation box. This command will
          overwrite whatever disk you point it to, please make sure and choose
          the correct disk:

      .. Image:: /images/Win32_disk_imager_Confirm_overwrite.png

      You should see the following status bar as the image is being
      written to the disk:

      .. Image:: /images/Win32_Disk_Imager_writing_to_disk.png

      And when the write is complete, you should get a notification:

      .. Image:: /images/Win32_Disk_Imager_Complete.png

      You can now close the image writing program:

      .. Image:: /images/Win32_Disk_Imager_exit.png

#. Safely eject the SD card from the computer. Here's an example using
   Windows 7:

.. Image:: /images/Win7_eject_disk.png

.. Image:: /images/Win7_eject_disk_detail.png

.. Image:: /images/Win7_device_can_be_safely_removed.png

#. Plug it into a supported hardware platform and boot the platform from
   the SD card.
#. If the platform has a display (Starterkit, for example), you should
   see the landing application from the SDK. You can also connect to the board
   using a terminal emulator (ex. Tera Term) in order to view the serial console
   and interact with the embedded Linux system.

|

