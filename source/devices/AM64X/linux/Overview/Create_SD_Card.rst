
.. _am64x-create-sd-card:

Create SD Card
==============

.. note::
  You will need a micro-SD Card (16GB or larger) and an SD Card Reader.

.. _am64x-create-sd-card-with-default-images:

Create SD Card with Default Images
----------------------------------

1.  Install the AM64x Processor SDK on a Linux or a Windows machine at <PSDK\_PATH>

|

2.  The default bootable SD card image (WIC file) is available
    at <PSDK\_PATH>/filesystem/tisdk-default-image-am64xx-evm.wic.xz

|

3.  Decompress the tisdk-default-image-am64xx-evm.wic.xz to tisdk-default-image-am64xx-evm.wic

    - For Linux:

    ::

        cd <PSDK_PATH>/filesystem
        unxz tisdk-default-image-am64xx-evm.wic.xz

    - For Windows, decompress the WIC image with a file archiver like 7-zip or
      winzip.

|

4.  Flash the WIC image to SD card


    - For Linux:
        a) First, make sure that the SD card is unmounted. You can use lsblk to
           inspect whether the SD card partitions have a MOUNTPOINT. If the SD
           card is mounted, use umount to unmount the partitions.

           For example, if lsblk returned this:

           ::

               $ lsblk
               NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
               :
               :
               sdc      8:32   1    15G  0 disk
               ├─sdc1   8:33   1 131.8M  0 part /media/localUser/boot
               └─sdc2   8:34   1 765.9M  0 part /media/localUser/root

           Then we would want to unmount sdc1 and sdc2:

           ::

               $ sudo umount /media/localUser/boot
               $ sudo umount /media/localUser/root
               $ lsblk
               NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
               :
               :
               sdc      8:32   1    15G  0 disk
               ├─sdc1   8:33   1 131.8M  0 part
               └─sdc2   8:34   1 765.9M  0 part

        b) Next, install bmap-tools using the following command:

           ::

               sudo apt-get install bmap-tools

           Then generate a bmap file from the decompressed WIC image with the following command.
           This step can be skipped but the bmap file significantly reduces the time taken to flash the SD card.

           ::

               bmaptool create -o tisdk-default-image.bmap tisdk-default-image-am64xx-evm.wic

        c) Then write the WIC image to the SD card with the following command:

           ::

               sudo bmaptool copy --bmap tisdk-default-image.bmap tisdk-default-image-am64xx-evm.wic /dev/sdx

           In the above example, the SD card is at /dev/sdc. In that case, the
           image write command would look like this:

           ::

               sudo bmaptool copy --bmap tisdk-default-image.bmap tisdk-default-image-am64xx-evm.wic /dev/sdc

    - For Windows:
        Write the WIC image to the SD card with Win32DiskImager.exe
        (https://sourceforge.net/projects/win32diskimager/files/latest/download)

|

.. _am64x-create-sd-card-with-custom-images:

Create SD Card with Custom Images
---------------------------------

.. note::
  The TI script used to generate custom SD card images should be run on a Linux
  computer.

For a Linux + RTOS/NO-RTOS application to boot from a SD card, two partitions need to
be created on the SD card:

   - boot partition
   - rootfs partition

create-sdcard-image.sh is provided in the Processor SDK to simplify this card
creation process. Here are the steps on how to use the script to create a custom
WIC image to place on an SD card.

1.  Install the AM64x Processor SDK on a Linux machine at <PSDK\_PATH> .

|

2.  Create a rootfs folder. create-sdcard-image.sh will use the rootfs folder
    to populate the rootfs partition on the WIC image.

    Let's use the prebuilt rootfs as an example. It is located at
    <PSDK\_PATH>/filesystem/tisdk-default-image-am64xx-evm.tar.xz

    ::

        cd <PSDK_PATH>/filesystem
        mkdir rootfs

    Un-tar the tisdk-default-image-am64xx-evm.tar.xz to
    <PSDK\_PATH>/filesystem/rootfs

    ::

        tar -xvf tisdk-default-image-am64xx-evm.tar.xz -C rootfs

|

3.  Create a boot folder. create-sdcard-image.sh will use the boot folder to
    populate the boot partition on the WIC image.

    Let's use the prebuilt images as an example. They are located at
    <PSDK\_PATH>/board-support/prebuilt-images

    ::

        mkdir boot
        cp ../board-support/prebuilt-images/tispl.bin boot
        cp ../board-support/prebuilt-images/tiboot3.bin boot
        cp ../board-support/prebuilt-images/u-boot-am64xx-evm.img boot/u-boot.img
        cp ../board-support/prebuilt-images/uEnv.txt boot

|

4.  Use create-sdcard-image.sh to generate a custom WIC file.

    You can give the WIC image any name. In this example, we will name it
    custom-image.wic.

    ::

        ../bin/scripts/create-sdcard-image.sh boot rootfs custom-image.wic

|

5.  If you want make changes to the custom WIC image, simply make changes to the
    boot and/or rootfs folders. Then use step 4 to re-create the WIC image.

|

6.  See section :ref:`am64x-create-sd-card-with-default-images` for steps to
    write your custom WIC image to an SD card.

|


