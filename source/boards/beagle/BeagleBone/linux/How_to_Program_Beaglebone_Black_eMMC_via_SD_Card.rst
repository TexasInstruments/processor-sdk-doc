Flashing eMMC on BeagleBone Black via SD Card
=============================================

Overview
--------
This documentation provides the flow and script for programming the eMMC on a
BeagleBone Black solely via micro SD Card. This solution will work with a
completely blank board / EVM. This solution can be used as a base to create a
custom production programming solution. A host Linux PC with the most current
Processor SDK will be needed to create a bootable SD card.

In order to accomplish this goal, two main objectives need to happen:

   #. Create a bootable USB using the SDK's SD Card Creation script with our
      Linux PC.
   #. Use the included sd-card-flasher script on the EVM to repartition and
      reformat the eMMC.

What is Needed
--------------
*  The most current `Processor SDK for Linux
   <http://www.ti.com/tool/PROCESSOR-SDK-AM335X>`__ installed on an appropriate
   development system
*  A `BeagleBone Black <https://www.ti.com/tool/BEAGLEBK>`__
*  A 5V power supply compatible with the BeagleBone Black
*  A Serial Debug Cable is recommended to monitor U-Boot outputs
*  The flasher script: :download:`sd-card-flasher.sh <files/sd-card-flasher.sh>`

Preparing the SD Card
---------------------
* Follow the steps outlined in the :ref:`Linux SD Card Creation Guide
  <processor-sdk-linux-sd-card-with-default-images>`.
* For this guide, it is recommended to follow the steps to create an "SD Card
  Using Default Images."
* Once the SD Card has been created with default
  images, copy the included **sd-card-flasher.sh** to the **/home/root/**
  directory in the **rootfs** partition of the SD Card:

  ::

   sudo cp <PATH-TO-FLASHER>/flasher.sh <PATH-TO-SD-CARD>/rootfs/home/root/

* Verify flasher script has been copied to SD card:

  ::

   sudo ls <PATH-TO-SD-CARD>/rootfs/home/root/

* Copy rootfs from SDK to SD card:

  ::

   sudo cp <PROCESSOR-SDK>/filesystem/tisdk-default-image-am335x-evm.tar.xz
   <PATH-TO-SD-CARD>/rootfs/home/root/

* Verify rootfs tarball has been copied to SD card:

  ::

   sudo ls <PATH-TO-SD-CARD>/rootfs/home/root/

Booting EVM and Running Partition Script
----------------------------------------
* Connect EVM to UART console via Serial Debug Cable
* Insert SD Card into EVM
* Boot and power on EVM from SD Card.

  .. note:: The BeagleBone Black can be booted from an SD Card by simply
     holding down the **USER/BOOT** button on the board before powering it on.

* Once the EVM has booted, login with root permissions.
* Invoke **sd-card-flasher.sh** script. It will be located in the **/home/root/**
  directory:

  ::

   ./sd-card-flasher.sh

* If the eMMC has successfully been programmed, the script will output a
  successful flash message.
* Power off EVM, and remove SD Card
* Power EVM back on to ensure eMMC has been flashed
