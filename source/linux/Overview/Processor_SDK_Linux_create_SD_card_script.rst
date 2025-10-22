.. http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_create_SD_card_script

.. _linux_sd_card_creation_guide:

Linux SD Card Creation Guide
======================================

Overview
--------

The |__SDK_FULL_NAME__| package includes a script in the **<SDK INSTALL DIR>/bin**
directory named **create-sdcard.sh**. The purpose of this script is to
create SD cards for the following high-level use cases:

#. Create the `SD Card using default images <Processor_SDK_Linux_create_SD_card_script.html#sd-card-using-default-images>`__ from the |__SDK_FULL_NAME__|
   package
#. Create the `SD card using custom images <Processor_SDK_Linux_create_SD_card_script.html#sd-card-using-custom-images>`__
#. Create the `SD card using partition tarballs <Processor_SDK_Linux_create_SD_card_script.html#sd-card-using-partition-tarballs>`__ (This is not common
   and is used most often by board vendors)

The script will give you information about each step, but the following
sections will go over the details for the use cases above and walk you
through how to use the script as well.

|

.. _processor-sdk-linux-sd-card-common-steps:

Common Steps
-------------

No matter which use case above that you are creating an SD card for the
following steps are the same.

|

.. rubric:: Invoking the Script
   :name: invoking-the-sdcard-script

The **create-sdcard.sh** script can be run from any location but must be
run with **root** permissions. This usually means using the **sudo**
command to start execution of the script. For example:

**sudo <SDK INSTALL DIR>/bin/create-sdcard.sh**
If you fail to execute the script without root permissions you will
receive a message that root permissions are required and the script will
exit.

|

.. rubric:: Select the SD Card Device
   :name: select-the-sd-card-device

The first step of the script will ask you to select the drive
representing the SD card that you want to format. In most cases your
host root file system drive has been masked off to prevent damage to the
host system. When prompted enter the device number corresponding to the
SD card. For example if the output looks like:

::

    Availible Drives to write images to:

    #  major   minor    size   name
    1:   8       16    7761920 sdb

    Enter Device Number:

You would enter **1** to select the **sdb** device.

**NOTE**: For most common installations, this script works fine.
However, if you are using more advanced disk slicing and volume
management, the presented list of device nodes are off by one; in the
best case (picking the last item) it will flag a range error, and in the
worst case (anything in the middle) the wrong DASD can be destroyed. The
problem originates when it attempts to determine the $ROOTDRIVE to
"mask" the volume where "/" is mounted from the selection list using a
"grep -v $ROOTDRIVE" For the naive partitioning case, its heuristic is
fine, yielding something like "sda" --- but for LVM, it grabs some chunk
of the device name, e.g. "mapp" (out of "/dev/mapper/kubuntu--vg-root on
/ type ...").

.. rubric:: Re-Partitioning the SD Card
   :name: re-partitioning-the-sd-card

Any partitions of the device that are already mounted will be un-mounted
so that the device is ready for partitioning.

If the SD Card already has partition you will see a prompt like the
following asking you if you would like to repartition the card. If the
card was not already partitioned then this step will be skipped and you
can move on to the next step.

::

    Would you like to re-partition the drive anyways [y/n] :

-  Options:

   -  **y** - This will allow you to change the partitioning of the SD
      card. For example if you have a 3 partition card and want to
      create a 2 partition card to give additional storage space to the
      root file system you would select **y** here.
      **NOTE:** This operation **WILL ERASE** the contents of your SD
      card.
   -  **n** - If the SD card already has the desired number of
      partitions then this will leave the partitioning alone. If you
      select **n** here skip on to the `Installing SD Card Content <Processor_SDK_Linux_create_SD_card_script.html#installing-sd-card-content>`__ section.

.. rubric:: Select Number of Partitions
   :name: select-number-of-partitions

You should now see a prompt like the following which will ask you how
many partitions you want to create for the SD card.

::

    Number of partitions needed [2/3] :

-  Options:

   -  **2** - This is the most common use case and will give the most
      space to the root file system.
   -  **3** - This case should only be used by board manufacturers
      making SD cards to go in the box with the EVM. This requires
      access to the partition tarballs used for Out-Of-Box SD cards.
      This option should be selected if you are going to follow the
      `SD card using partition tarballs`_ steps below.

After selecting the number of partitions, move on to the next section.

.. _processor-sdk-linux-installing-sd-card-content:

Installing SD Card Content
---------------------------

After the SD card is partitioned, you will be prompted whether you want
to continue installing the file system or safely exit the script.

-  Options:

   -  **y** - Selecting yes here will begin the process of installing
      the SD card contents. This operation **WILL ERASE** any existing
      data on the SD card. Refer to one of the following sections for
      additional instructions depending on which use case you are
      creating an SD card for:

      -  Create the `SD card using default images`_
      -  Create the `SD card using custom images`_
      -  Create the `SD card using partition tarballs`_

   -  **n** - Selecting no here will allow you to have partitioned your
      card but will leave the partitions empty.

|

.. _processor-sdk-linux-sd-card-using-default-images:

SD Card Using Default Images
-----------------------------

The purpose of this section is to cover how to use the
**create-sdcard.sh** script to populate an SD card that can be used to
boot the device using the default images that ship with the |__SDK_FULL_NAME__| package.

.. rubric:: Prerequisites
   :name: sd-default-image-prerequisites

#. The |__SDK_FULL_NAME__| package is installed on your host system.
#. The SD card you wish to create is inserted into the host system and
   has a size sufficiently large (16GB or larger) to hold at least the bootloaders,
   kernel, and root file system.
#. You have started running the script as detailed in the `SD Card Common Steps <Processor_SDK_Linux_create_SD_card_script.html#common-steps>`__ section above.

.. rubric:: Choose Install Pre-built Images
   :name: choose-install-pre-built-images

You should now see a prompt like:

::

    ################################################################################

        Choose file path to install from

        1 ) Install pre-built images from SDK
        2 ) Enter in custom boot and rootfs file paths

    ################################################################################

    Choose now [1/2] :

You should choose option **1** to create an SD card using the pre-built
images from the SDK.

If you executed this script from within the SDK then the script can
determine the SDK path automatically and will start copying the contents
to the SD card. Once the files are copied the script will exit.

If you executed the script from outside of the SDK (i.e. you copied it
to some other directory and executed it there) please see the next
section.

**NOTE:** option 1 will only work with the format of the default SDK
directory name, which makes the Hands on with the SDK training easiest.
If you have to change the directory name, use option 2 to enter the
custom file paths.

|

.. rubric:: Enter SDK Path
   :name: enter-sdk-path

In the case that the script was invoked from a directory without the SDK
installation in the path, i.e. the script was copied to your home
directory and executed there, you may see a prompt like:

::

    no SDK PATH found
    Enter path to SDK :

Enter the path to the SDK installation directory here. For example, if
the SDK was installed into the home directory of the **sitara** user, the
path to enter would be
**/home/sitara/ti-processor-sdk-linux-<machine>-<version>**. You will be
prompted to confirm the installation directory. The SD card will then be
created using the default images and the script will exit when finished.

|

.. _processor-sdk-linux-sd-card-using-custom-images:

SD Card Using Custom Images
----------------------------

Often times you will use TFTP and NFS during development to transfer you
kernel images and boot your root file systems respectively. Once you are
done with your development you may want place these images onto an SD
card so that they can be used stand-along without requiring a network
connection to a server.

.. rubric:: Prerequisites
   :name: sd-custom-image-prerequisites

#. The |__SDK_FULL_NAME__| package is installed on your host system.
#. The SD card you wish to create is inserted into the host system and
   has a size sufficiently large (16GB or larger) to hold at least the bootloaders,
   kernel, and root file system.
#. You have started running the script as detailed in the `SD Card Common Steps <Processor_SDK_Linux_create_SD_card_script.html#common-steps>`__ section above.

.. rubric:: Choose Custom Images
   :name: choose-custom-images

You should now see a prompt like:

::

    ################################################################################

        Choose file path to install from

        1 ) Install pre-built images from SDK
        2 ) Enter in custom boot and rootfs file paths

    ################################################################################

    Choose now [1/2] :

Select option **2** to create an SD card with your custom images.

.. rubric:: Select Boot Partition
   :name: select-boot-partition

You will now be prompted to provide a path to the location of the boot
partition files. The prompt will explain the requirements of the files
to be placed at the path, but the basic options are:

#. Point to a tarball containing all of the files you want placed on the
   boot partition. This would include the boot loaders and the kernel
   image as well as any optional files like uEnv.txt.
#. Point to a directory containing the files for the boot partition like
   those in the first option.

The script is intelligent enough to recognize whether you provided a
tarball or a directory path and will copy the files accordingly. You
will be given a list of the files that are going to be copied and given
the option to change the path if the list of files is not correct.

.. rubric:: Select Root Partition
   :name: select-root-partition

You will now be prompted to provide a path to the location of the root
file sysetm partition files. The prompt will explain the requirements of
the files to be placed at the path, but the basic options are:

#. Point to a tarball of the root file system you want to use.
#. Point to a directory containing the root file sysetm such as an NFS
   share directory.

The script is intelligent enough to recognize whether you provided a
tarball or a directory path and will copy the files accordingly. You
will be given a list of the files that are going to be copied and given
the option to change the path if the list of files is not correct.

|

.. _processor-sdk-linux-sd-card-using-partition-tarballs:

SD Card Using Partition Tarballs
--------------------------------

This option is meant for board vendors to create SD cards to go in the
box with the EVM. It requires access to the three tarballs representing
the the partitions of the SD card shipped with the EVM.

.. rubric:: Prerequisites
   :name: sd-parition-tarballs-prerequisites

#. The |__SDK_FULL_NAME__| package is installed on your host system.
#. The SD card you wish to create is inserted into the host system and
   has a size sufficiently large (16GB or larger) to hold at least the bootloaders,
   kernel, and root file system.
#. You have started running the script as detailed in the `SD Card Common
   Steps <Processor_SDK_Linux_create_SD_card_script.html#common-steps>`__ section above.

.. rubric:: Provide Tarball Location
   :name: provide-tarball-location

After the SD card has been partitioned you will be prompted to:

::

    Enter path where SD card tarballs were downloaded :

Point to the directory containing the following tarball files:

-  **boot\_partition.tar.gz**
-  **rootfs\_partition.tar.gz**
-  **start\_here\_partition.tar.gz**

The script will show you the contents of the directory given and ask you
to verify that the tarballs are present in that directory. The SD card
will then be populated with the contents of the tarballs and be ready
for inclusion in the box with the EVM.
