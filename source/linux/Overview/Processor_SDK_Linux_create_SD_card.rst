.. _processor-sdk-linux-create-sd-card:

Create SD Card
===============

Overview
--------

This section provides guides to create SD cards for the following use cases:

#. Create SD cards with default images:

   - :ref:`Create SD cards with default images using balenaEtcher <processor-sdk-linux-create-sd-card-using-balena>`

   - :ref:`Create SD cards with default images using bmap-tools <processor-sdk-linux-create-sd-card-using-bmap>`

   - :ref:`Create SD cards with default images using script packaged in installer <processor-sdk-linux-sd-card-with-default-images>`

#. Create SD cards with custom images:

   - :ref:`Create SD cards with custom images <processor-sdk-linux-create-sd-card-with-custom-images>`

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM64X')

   .. attention:: After flashing the wic image on the SD-Card, it will boot on **HS-FS** devices by default.

         To boot on **GP**, run the following command:

         .. code-block:: console

             host# sudo cp /media/$USER/boot/tiboot3-am6*-gp-evm.bin /media/$USER/boot/tiboot3.bin

         To boot on **HS-SE**, run the following command:

         .. code-block:: console

             host# sudo cp /media/$USER/boot/tiboot3-am6*-hs-evm.bin /media/$USER/boot/tiboot3.bin


.. ifconfig:: CONFIG_part_variant in ('AM65X')

   .. attention:: After flashing the wic image on the SD-Card, it will boot on **SR2 GP** devices by default.

         To boot on **SR2 HS-SE**, run the following command:

         .. code-block:: console

             host# sudo cp /media/$USER/boot/tiboot3-am65x_sr2-hs-evm.bin /media/$USER/boot/tiboot3.bin
             host# sudo cp /media/$USER/boot/sysfw-am65x_sr2-hs-evm.itb /media/$USER/boot/sysfw.itb

.. _processor-sdk-linux-create-sd-card-using-balena:

Create SD Card using balenaEtcher
----------------------------------

1.  Download the default bootable SD card image (WIC file) available on the release page as

    .. parsed-literal::

       tisdk-|__IMAGE_TYPE__|-image-<machine>-<version>.rootfs.wic.xz

2.  Download and install the balenaEtcher tool

      - Balena Etcher is an open-source utility that can be installed on both Linux and Windows. Download the tool from `this link <https://www.balena.io/etcher/>`__ and install it.

3.  Flash the WIC image to the SD card

      - Insert a micro SD card into the USB SD card reader and start Etcher.Choose the default WIC
        image to be flashed, choose the USB SD card reader as the target, and then click "Flash".
        Etcher will decompress the image and write it to the SD card, as shown below

    .. Image:: /images/balena_etcher.png
       :height: 400

    .. danger::

        This operation **WILL ERASE** the contents of your SD card.

.. ifconfig:: CONFIG_image_type in ('adas')

   .. note::

      We do not release WIC images for J7 platforms (J784S4, J742S2, J722S, J721E, J721S2).
      Please refer to :ref:`Create SD Card with custom images <processor-sdk-linux-sd-card-with-default-images>` for flashing image.

.. _processor-sdk-linux-create-sd-card-using-bmap:

Create SD Card using bmap-tools
----------------------------------


1.  Download the default bootable SD card image (WIC file) available on the release page as

    .. parsed-literal::

       tisdk-|__IMAGE_TYPE__|-image-<machine>-<version>.rootfs.wic.xz

2. Decompress the tisdk-|__IMAGE_TYPE__|-image-<machine>-<version>.rootfs.wic.xz to tisdk-|__IMAGE_TYPE__|-image-<machine>-<version>.rootfs.wic

    - For Linux:

    .. parsed-literal::

       cd <PSDK_PATH>/filesystem
       unxz tisdk-|__IMAGE_TYPE__|-image-<machine>-<version>.rootfs.wic.xz

3.  Flash the WIC image to SD card

      a) First, make sure that the SD card is unmounted. You can use lsblk to
         inspect whether the SD card partitions have a MOUNTPOINT. If the SD
         card is mounted, use umount to unmount the partitions.

         For example, if lsblk returned this:

         .. code-block:: console

             $ lsblk
             NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
             :
             :
             sdc      8:32   1    15G  0 disk
             ├─sdc1   8:33   1 131.8M  0 part /media/$USER/boot
             └─sdc2   8:34   1 765.9M  0 part /media/$USER/root

         Then we would want to unmount sdc1 and sdc2:

         .. code-block:: console

             $ sudo umount /media/$USER/boot
             $ sudo umount /media/$USER/root
             $ lsblk
             NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
             :
             :
             sdc      8:32   1    15G  0 disk
             ├─sdc1   8:33   1 131.8M  0 part
             └─sdc2   8:34   1 765.9M  0 part

      b) Next, install bmap-tools using the following command:

         .. code-block:: console

             sudo apt-get install bmap-tools

         Then generate a bmap file from the decompressed WIC image with the following command.
         This step can be skipped but the bmap file significantly reduces the time taken to flash the SD card.

         .. parsed-literal::

            bmaptool create -o tisdk-|__IMAGE_TYPE__|-image-<machine>-<version>.rootfs.bmap tisdk-|__IMAGE_TYPE__|-image-<machine>-<version>.rootfs.wic

      c) Then write the WIC image to the SD card with the following command:

         .. parsed-literal::

            sudo bmaptool copy --bmap tisdk-|__IMAGE_TYPE__|-image-<machine>-<version>.rootfs.bmap tisdk-|__IMAGE_TYPE__|-image-<machine>-<version>.rootfs.wic /dev/sdx


         .. danger::

             The above operation **WILL ERASE** the contents of your SD card.

         In the above example, the SD card is at /dev/sdc. In that case, the
         image write command would look like this:

         .. parsed-literal::

            sudo bmaptool copy --bmap tisdk-|__IMAGE_TYPE__|-image-<machine>-<version>.rootfs.bmap tisdk-|__IMAGE_TYPE__|-image-<machine>-<version>.rootfs.wic /dev/sdc

.. ifconfig:: CONFIG_image_type in ('adas')
   
   .. note::
   
      We do not release WIC images for J7 platforms (J784S4, J742S2, J722S, J721E, J721S2).
      Please refer to :ref:`Create SD Card with custom images <processor-sdk-linux-sd-card-with-default-images>` for flashing image.

.. _processor-sdk-linux-create-sd-card-with-custom-images:

Create SD Card with custom images
---------------------------------

Often times you will use TFTP and NFS during development to transfer your
kernel images and boot your root file systems respectively. Once you are
done with your development you may want to place these images onto an SD
card so that they can be used stand-alone without requiring a network
connection to a server.

For this purpose, the |__SDK_FULL_NAME__| package includes a script at
:file:`{PSDK_PATH}/bin/create-sdcard.sh`

The |__SDK_FULL_NAME__| can be installed either on Host or Inside a Docker Container that is hosted on `ghcr.io/texasinstruments <https://github.com/TexasInstruments/ti-docker-images/pkgs/container/ubuntu-distro>`__.

The script will give you information about each step, but the following
section will go over the details for the use cases above and walk you
through how to use the script as well.


.. rubric:: 1. Invoking the Script:
   :name: Invoking-the-script

The :file:`create-sdcard.sh` script can be run from any location but must be
run with **root** permissions. This usually means using the **sudo**
command to start execution of the script. For example:

.. code-block:: console

    sudo <PSDK_PATH>/bin/create-sdcard.sh

If you fail to execute the script without root permissions you will
receive a message that root permissions are required and the script will
exit.


.. rubric:: 2. Select the SD Card Device:
   :name: select-the-sd-card-device

The first step of the script will ask you to select the drive
representing the SD card that you want to format. In most cases your
host root file system drive has been masked off to prevent damage to the
host system. When prompted enter the device number corresponding to the
SD card. For example if the output looks like:

.. code-block:: text

    Availible Drives to write images to:

    #  major   minor    size   name
    1:   8       16    7761920 sdb

    Enter Device Number:

You would enter **1** to select the **sdb** device.

.. attention::

 For most common installations, this script works fine.
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


.. rubric:: 3. Partitioning the SD Card
   :name: partitioning-the-sd-card

Any partitions of the device that are already mounted will be un-mounted
so that the device is ready for partitioning.

If the SD Card already has partition you will see a prompt like the
following asking you if you would like to repartition the card. If the
card was not already partitioned then this step will be skipped and you
can move on to the next step.

.. code-block:: text

    Would you like to re-partition the drive anyways [y/n] :

-  Options:

   -  **n** - If the SD card already has the desired number of
      partitions then this will leave the partitioning alone. If you
      select **n** here skip on to step 4.

  -   **y** - This will allow you to change the partitioning of the SD
      card. For example if you have a 3 partition card and want to
      create a 2 partition card to give additional storage space to the
      root file system you would select **y** here.

.. danger::

    This operation **WILL ERASE** the contents of your SD card.


.. rubric:: 4. Select Number of Partitions
   :name: select-number-of-partitions

You should now see a prompt like the following which will ask you how
many partitions you want to create for the SD card.

.. code-block:: text

    Number of partitions needed [2/3] :

-  Options:

   -  **2** - This is the most common use case and will give the most
      space to the root file system.

After selecting the number of partitions, move on to the next section.


.. rubric:: 5. Installing Content onto the SD Card:
   :name: installing-content-onto-sd-card

After the SD card is partitioned, you will be prompted whether you want
to continue installing the file system or safely exit the script.

-  Options:

   -  **y** - Selecting yes here will begin the process of installing
      the SD card contents. This operation **WILL ERASE** any existing
      data on the SD card.

   -  **n** - Selecting no here will allow you to have partitioned your
      card but will leave the partitions empty.



.. rubric:: 6. Installing Custom Images
   :name: installing-custom-images

You should now see a prompt like:

.. code-block:: text

    ################################################################################

        Choose file path to install from

        1 ) Install pre-built images from SDK
        2 ) Enter in custom boot and rootfs file paths

    ################################################################################

    Choose now [1/2] :

- Options:

  - **1** - Refer to :ref:`this section <processor-sdk-linux-sd-card-with-default-images>` to install the default images.

  - **2** - Select option **2** to create an SD card with your custom images.

.. rubric:: 7. Select Boot Partition
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

.. rubric:: 8. Select Root Partition
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


.. _processor-sdk-linux-sd-card-with-default-images:

Create SD Card with Default Images using script
-----------------------------------------------

The purpose of this section is to cover how to use the
:file:`create-sdcard.sh` script to populate an SD card that can be used to
boot the device using the default images that ship with the |__SDK_FULL_NAME__| package.

The |__SDK_FULL_NAME__| can be installed either on host or inside a Docker container that is hosted on `ghcr.io/texasinstruments <https://github.com/TexasInstruments/ti-docker-images/pkgs/container/ubuntu-distro>`__.

**Steps to follow inside a Docker Container**

- The SD card you wish to create is inserted into the host system and has a size sufficiently large (16GB or larger) to hold at least the bootloaders, kernel and root file system.
- Refer `Steps to Run SDK Installer inside a Container <https://github.com/TexasInstruments/ti-docker-images?tab=readme-ov-file#steps-to-run-sdk-installer-inside-container>`__
- Start running the script as mentioned in steps 1-4 of :ref:`Create SD card with custom images <processor-sdk-linux-create-sd-card-with-custom-images>` section above.
- Refer :ref:`Install the Pre-built Images from SDK <choose-install-pre-built-images>`

**Steps to follow on Host**

.. rubric:: 1. Prerequisites
   :name: sd-default-image-prerequisites

#. The |__SDK_FULL_NAME__| package is installed on your host system.
#. The SD card you wish to create is inserted into the host system and
   has a size sufficiently large (16GB or larger) to hold at least the bootloaders,
   kernel, and root file system.
#. You have started running the script as detailed in steps 1-4 of
   :ref:`Create SD card with custom images <processor-sdk-linux-create-sd-card-with-custom-images>`
   section above.

.. rubric:: 2. Choose Install Pre-built Images
   :name: choose-install-pre-built-images

You should now see a prompt like:

.. code-block:: text

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

.. important::

    Option 1 will only work with the format of the default SDK
    directory name, which makes the Hands on with the SDK training easiest.
    If you have to change the directory name, use option 2 to enter the
    custom file paths.


.. rubric:: 3. Enter SDK Path
   :name: enter-sdk-path

In the case that the script was invoked from a directory without the SDK
installation in the path, i.e. the script was copied to your home
directory and executed there, you may see a prompt like:

.. code-block:: text

    no SDK PATH found
    Enter path to SDK :

Enter the path to the SDK installation directory here. For example, if
the SDK was installed into the home directory of "**USER**", the
path to enter would be **/home/USER/ti-processor-sdk-linux-<machine>-<version>**.
You will be prompted to confirm the installation directory. The SD card will then
be created using the default images and the script will exit when finished.

