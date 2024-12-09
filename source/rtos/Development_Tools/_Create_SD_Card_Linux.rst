Linux SD Card Creation Guide
=============================

.. http://processors.wiki.ti.com/index.php/Processor_SDK_RTOS_create_SD_card_script

Overview
----------

The Processor SDK RTOS for AM3/AM4/AM5/K2G includes a script in the
directory

::

     [SDK Install Path]\processor_sdk_rtos_<platform>_<version>\bin\

named **create-sdcard.sh**. The purpose of this script is to create SD
cards to load with images for RTOS applications.

The contents of an bootable RTOS application will contain two files on
the SD card:

-  **app** - Application image
-  **MLO** - Boot loader image

The script will give you information about each step, but the following
sections will go over the details and walk you through how to use the
script as well.

|

What is Needed
----------------

-  Access to a Linux PC
-  A valid Processor SDK RTOS for the appropriate processor installed
   (AM335x, AM437x, AM57xx, K2G)
-  A SD card appropriate for the required hardware platform, must be 1GB
   or larger
-  A SD card reader/writer

|

Creating an SD card
---------------------

Invoking the Script
^^^^^^^^^^^^^^^^^^^^

The **create-sdcard.sh** script can be run from any location but must be
run with ``root`` permissions. This usually means using the ``sudo``
command to start execution of the script. For example:

::

     sudo [SDK INSTALL DIR]/bin/create-sdcard.sh [path/to/sdcard/files]

The SDK comes with pre-built images that can be directly loaded on an SD
card without having to do any builds. These are typically a
demonstration or a Power-On Self Test (POST) application. The path for
these files are:

::

     sudo [SDK INSTALL DIR]/bin/create-sdcard.sh [SDK INSTALL DIR]/prebuilt-sdcards/[EVM DIR]/sd_card_files/

If you fail to execute the script with root permissions you will receive
a message that root permissions are required and the script will exit.

Select the SD Card Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first step of the script will ask you to select the drive
representing the SD card that you want to format. In most cases your
host root file system drive has been masked off to prevent damage to the
host system. When prompted enter the device number corresponding to the
SD card. For example, if the output looks like:

::

    Availible Drives to write images to:

    #  major   minor    size   name
    1:   8       16    7761920 sdb

    Enter Device Number:

You would enter **1** to select the *sdb* device.

For most common installations, this script works fine. However, if you
are using more advanced disk slicing and volume management, the
presented list of device nodes are off by one; in the best case (picking
the last item) it will flag a range error, and in the worst case
(anything in the middle) the wrong DASD can be destroyed. The problem
originates when it attempts to determine the ``$ROOTDRIVE`` to "mask"
the volume where "/" is mounted from the selection list using a
``grep -v $ROOTDRIVE``.

For the naive partitioning case, its heuristic is fine, yielding
something like "sda" --- but for LVM, it grabs some chunk of the device
name, e.g. "mapp" (out of "/dev/mapper/kubuntu--vg-root on / type ...").

.. rubric:: Partition and Format the SD Card
   :name: partition-and-format-the-sd-card

Any partitions of the device that are already mounted will be un-mounted
so that the device is ready for partitioning. The SD Card will then be
partitioned and formatted into FAT32.

Installing SD Card Contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
After the SD card is partitioned and formatted, the files under the
path/to/sdcard/files will be installed onto the SD card, then safely
exit the script.

.. tip::
   Once SD card is made bootable, it contains sample “MLO” and “app”
   which can be used on the target platform.

|

Load Default Images to SD Card
-------------------------------
The purpose of this section is to cover how to use the
**create-sdcard.sh** script to populate an SD card that can be used to
boot the device using the default images that ship with the Processor
SDK for RTOS.

For example purposes, you can use the one that is bundled in the SDK.
The file is located in

::

     [SDK Install Path]/processor_sdk_rtos_<platform>_<version>/prebuilt-sdcards/<evm>/sd_card_files/

For example, the default location of the image file for the GP AM57x EVM
is

::

     ~/ti/processor_sdk_rtos_am57xx_2_00_00_00/prebuilt-sdcards/evmAM572x/sd_card_files/

The command to load the SD card is

::

     sudo [SDK Install Path]/bin/create-sdcard.sh ~/ti/processor_sdk_rtos_am57xx_2_00_00_00/prebuilt-sdcards/evmAM572x/sd_card_files

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

