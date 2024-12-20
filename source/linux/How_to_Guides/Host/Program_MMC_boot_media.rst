######################
Program MMC boot media
######################

********
Overview
********
.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   This documentation provide the steps for building flasher Image with initramfs-based boot support and programming
   the eMMC device via CPSW Ethernet connection to a Linux host PC. This solution will work with a completely blank
   board / SK and can be used as a base to create a custom production programming solution.

   To achieve this goal the following is required:

   * Use the SDK to build a separate "flasher" image which can be transferred
     from the host PC via Ethernet to program the eMMC device.

.. ifconfig:: CONFIG_part_variant in ('J721S2','AM64X')

   This documentation provides the steps for building flasher image with initramfs-based boot support and programming
   the MMC device via CPSW Ethernet connection to a Linux host PC. This solution will work with a completely blank
   board / SK and can be used as a base to create a custom production programming solution.

   To achieve this goal the following is required:

   * Use the SDK to build a separate "flasher" image which can be transferred
     from the host PC via Ethernet to program the MMC-SD device.

**************
What is Needed
**************

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   * The most current `Processor SDK for Linux <https://www.ti.com/tool/PROCESSOR-SDK-AM64X>`__ installed
     on the host Linux PC used for development

   * SK-AM64B or AM64-EVM board and an ethernet cable to connect the board to the host PC

   * A 12V and 5V power supply compatible with the AM64-EVM and SK-AM64B respectively.

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   * The most current `Processor SDK for Linux
   <https://www.ti.com/tool/PROCESSOR-SDK-AM69>`__ installed on the host Linux PC used for development

   * AM69-SK board and a ethernet cable to connect the AM69-SK to the host PC

   * A 12V power supply compatible with the AM69-SK

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   * The most current `Processor SDK for Linux
     <https://www.ti.com/tool/PROCESSOR-SDK-AM68>`__ installed on the host Linux
     PC used for development

   * AM68-SK board and a ethernet cable to connect the AM68-SK to the host PC

   * A 5V power supply compatible with the AM68-SK

* A Serial Debug Cable is recommended to monitor U-Boot outputs

* An image to flash. This can be derived from the SDK mentioned above

* A Linux Filesystem small enough to be peripheral booted, with the
  functionality needed to do the necessary flashing operation. This can be
  derived from the SDK mentioned above

* A Linux host PC to transfer the binary files

* A configured TFTP Server

* A SD card with pre-built U-Boot images from SDK

**************
Configure tftp
**************

Steps to configure a TFTP Server on host PC can be found in :ref:`TFTP Server <run-setup-scripts>`

***************************
Preparing the Flasher Image
***************************

First we need to create the flasher image with smaller filesystem on the host PC.

Prepare a rootfs
================

* Navigate to **<Processor-SDK>/filesystem**

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   * Create a directory called **tisdk-tiny-image-j784s4-evm** under
     **<Processsor-SDK>/filesystem/**

   * Extract SDK-provided "tiny" rootfs inside the tisdk-tiny-image-j784s4-evm directory

      .. code-block:: console

         tar -C tisdk-tiny-image-j784s4-evm -xvf tisdk-tiny-image-j784s4-evm.tar.xz

   * Create an :file:`/init` link pointing to :file:`/sbin/init`. The Kernel
     requires this to boot from the initramfs:

      .. code-block:: console

         ln -s sbin/init tisdk-tiny-image-j784s4-evm/init

   * Verify contents of initramfs root folder:

      .. code-block:: console

         ls -l tisdk-tiny-image-j784s4-evm/

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   * Create a directory called **tisdk-tiny-image-j721s2-evm** under
     **<Processsor-SDK>/filesystem/**

   * Extract SDK-provided "tiny" rootfs inside the tisdk-tiny-image-j721s2-evm directory

      .. code-block:: console

         tar -C tisdk-tiny-image-j721s2-evm -xvf tisdk-tiny-image-j721s2-evm.tar.xz

   * Create an :file:`/init` link pointing to :file:`/sbin/init`. The Kernel
     requires this to boot from the initramfs:

      .. code-block:: console

         ln -s sbin/init tisdk-tiny-image-j721s2-evm/init

   * Verify contents of initramfs root folder:

      .. code-block:: console

         ls -l tisdk-tiny-image-j721s2-evm/

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   * Refer to prerequisites and steps for Yocto build for an Ubuntu host: :ref:`Host Setup - ubuntu (Recommended)`.

   After the Yocto enviroment is setup, use the below step to build the Initramfs Image:

   .. code-block:: console

      MACHINE=<machine> bitbake -k tisdk-tiny-initramfs

   The bitbake command mentioned in the last line above builds the tisdk-tiny-initramfs
   cpio which can be located at :file:`deploy-ti/images/am64xx-evm`.

.. ifconfig:: CONFIG_part_variant not in ('AM64X')

   :file:`init` should now be linked to :file:`sbin/init`

Prepare Kernel with baked-in initramfs
======================================

* Navigate to your linux repository to build flasher Image

   .. code-block:: console

      cd <PSDK_PATH>/board-support/linux-[ver]/

* Build device defconfig file

   .. code-block:: console

     make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- defconfig ti_arm64_prune.config

* Make a backup copy of :file:`.config` called :file:`.config.orig`

* Edit the current Kernel config using menuconfig as follows:

   .. code-block:: console

      make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- menuconfig

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   * Set CONFIG_INITRAMFS_SOURCE = :file:`{Processor-SDK}/filesystem/tisdk-tiny-image-j784s4-evm`

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   * Set CONFIG_INITRAMFS_SOURCE = :file:`{Processor-SDK}/filesystem/tisdk-tiny-image-j721s2-evm`

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   * Set CONFIG_INITRAMFS_SOURCE = :file:`{path to cpio}/tisdk-tiny-initramfs-am64xx-evm.cpio`

Select General setup:

.. Image:: /images/Program_flash_image1.PNG
   :height: 300px
   :width: 400px

|

Scroll down to **Initial RAM Filesystem and RAM Disk (initramfs/initrd)
support** and Select it:

.. Image:: /images/Program_flash_image2.PNG
   :height: 300px
   :width: 400px

|

Move down a line to Initramfs source file(s). Select it and fill in the
location of the files:

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   .. Image:: /images/am69_Program_flash_image.png
      :height: 300px
      :width: 400px

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   .. Image:: /images/am68_Program_flash_image.png
      :height: 300px
      :width: 400px

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. Image:: /images/menuconfig.png
      :height: 300px
      :width: 400px

|

Exit menuconfig and save the new configuration.

Build the Kernel
================

* Compile the :file:`zImage`

   .. code-block:: console

      make ARCH=arm64 CROSS_COMPILE=aarch64-none-linux-gnu- Image

* Copy :file:`arch/arm64/boot/Image` to :file:`/tftpboot`

*************
Target Images
*************

* Populate pre-built U-Boot images from SDK into TFTP folder

   .. note::

      We can use the prebuilt U-Boot images as-is with no modifications needed

* Populate bootloaders into the TFTP home directory

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   * Copy :file:`tiboot3-j784s4-hs-fs-evm.bin`, :file:`tispl.bin` and
     :file:`u-boot.img` files from
     :file:`{Processor-SDK}/board-support/prebuilt-images/` to the
     :file:`~/tftpboot` directory

   * Rename tiboot3-j784s4-* as tiboot3.bin inside ~/tftpboot

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   * Copy :file:`tiboot3-j721s2-hs-fs-evm.bin`, :file:`tispl.bin` and
     :file:`u-boot.img` files from
     :file:`{Processor-SDK}/board-support/prebuilt-images/` to the
     :file:`~/tftpboot` directory

   * Rename tiboot3-j721s2-* as tiboot3.bin inside ~/tftpboot

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   * Copy :file:`tiboot3.bin`, :file:`tispl.bin` and :file:`u-boot.img` files
     from :file:`{Processor-SDK}/board-support/prebuilt-images/am64xx-evm/` to
     the :file:`~/tftpboot` directory

* Populating rootfs into the TFTP home directory.

   * Download the default bootable SD card image (WIC file) available on the
     release page as :file:`tisdk-default-image-{machine}.wic.xz`

   * Copy wic image to root directory :file:`/tftpboot`

*****************
Program the Flash
*****************

Now that the flash image has been created we can now flash the SK

.. note::

   In SK the TFTP server must be properly configured to transfer the flash image.

* Connect SK to Linux host machine via Serial Debugging Cable

* Open an active console window to monitor bootup messages

* Connect ethernet cable to board

* Boot the board in SD boot mode and "strike any key" to halt U-Boot at prompt

* Enter the following commands

   .. code-block:: text

      setenv serverip <SERVER_IP>
      dhcp

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   * For writing bootloaders into eMMC boot partition

      .. code-block:: text

         mmc dev 0 1
         tftp ${loadaddr} tiboot3.bin
         mmc write ${loadaddr} 0x0 0x400
         tftp ${loadaddr} tispl.bin
         mmc write ${loadaddr} 0x400 0x1000
         tftp ${loadaddr} u-boot.img
         mmc write ${loadaddr} 0x1400 0x2000

   * To give the ROM access to the boot partition, the following commands must
     be used for the first time:

      .. code-block:: text

         mmc partconf 0 1 1 1
         mmc bootbus 0 2 0 0

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   * For creating eMMC boot partiton refer :ref:`here <partitioning-eMMC-from-uboot>`

   * For writing bootloaders into eMMC boot partition

   .. code-block:: text

      mmc dev 0 1
      tftp ${loadaddr} tiboot3.bin
      mmc write ${loadaddr} 0x0 0x400
      tftp ${loadaddr} tispl.bin
      mmc write ${loadaddr} 0x800 0x1000
      tftp ${loadaddr} u-boot.img
      mmc write ${loadaddr} 0x1800 0x2000

   * To give the ROM access to the boot partition, the following commands must be used for the first time:

   .. code-block:: text

      mmc partconf 0 1 1 1
      mmc bootbus 0 2 0 0

* Enter command to boot Linux using initramfs image from TFTP server

   .. code-block:: text

      run findfdt
      tftp ${loadaddr} Image
      tftp ${fdtaddr} ${name_fdt}
      booti ${loadaddr} - ${fdtaddr}

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   * Enter the following command on Linux shell to transfer the wic image

      .. code-block:: console

         tftp -b 1468 -g -r tisdk-default-image-j784s4-evm.wic.xz <SERVER_IP>

   * unmount the eMMC and flash the image into eMMC device

      .. code-block:: console

         umount /dev/mmcblk0*
         dd if=tisdk-default-image-j784s4-evm.wic.xz of=/dev/mmcblk0

   * Now reboot the board with eMMC boot mode and "strike any key" to  halt U-Boot at prompt

   * Enter command to boot kernel from eMMC

      .. code-block:: text

         setenv mmcdev 0
         setenv bootpart 0:2
         boot

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   * Enter the following command on Linux shell to transfer the wic image

      .. code-block:: console

         tftp -b 1468 -g -r tisdk-default-image-j721s2-evm.wic.xz <SERVER_IP>

   * Flash the image into MMC-SD

      .. code-block:: console

         dd if=tisdk-default-image-j721s2-evm.wic.xz of=/dev/mmcblk1

   * Now reboot the board with SD boot mode and verify that it boots successfully

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   * Enter the following command on Host PC's Linux shell to transfer the wic image

      .. code-block:: console

         tftp -b 1468 -g -r tisdk-default-image-am64xx-evm.wic.xz <SERVER_IP>

* Flash the image into MMC-SD

   .. code-block:: console

      dd if=tisdk-default-image-am64xx-evm.wic.xz of=/dev/mmcblk1

* Now reboot the board with SD boot mode and verify that it boots successfully
