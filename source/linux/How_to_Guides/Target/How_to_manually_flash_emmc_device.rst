####################################################
How to flash eMMC device and boot from UDA partition
####################################################

********
Overview
********

- Requires a bootable SD card with linux Kernel images. Boot the target EVM to
  linux prompt and check for mmc devices

  .. code-block:: console

     root@j7200-evm:~# lsblk | grep mmc
     mmcblk0      179:0    0 14.8G  0 disk
     |-mmcblk0p1  179:1    0  128M  0 part /run/media/boot-mmcblk0p1
     `-mmcblk0p2  179:2    0 14.7G  0 part /run/media/root-mmcblk0p2
     mmcblk0boot0 179:32   0 31.5M  1 disk
     mmcblk0boot1 179:64   0 31.5M  1 disk
     mmcblk1      179:96   0 29.7G  0 disk
     |-mmcblk1p1  179:97   0  128M  0 part /run/media/boot-mmcblk1p1
     `-mmcblk1p2  179:98   0  8.5G  0 part /

  Here, SD card is mmcblk1 and eMMC (UDA partition) is mmcblk0. SD card rootfs
  partition (mmcblk1p2) is mounted at root.

- To flash eMMC using a partitioned wic image from the SDK, jump to :ref:`flash-emmc-from-wic`

- To flash eMMC manually, jump to :ref:`flash-emmc-manually`

- To Boot the board from a flashed eMMC device, jump to :ref:`flash-emmc-boot`

.. _flash-emmc-from-wic:

************************************
Flash eMMC device using a disk image
************************************

Copy the .wic formatted disk image from the SDK installer to target filesystem.
Then the eMMC device can be flashed using following commands

.. code-block:: console

   root@j7200-evm:~# ls
   tisdk-base-image-j7200-evm.rootfs.wic.xz
   root@j7200-evm:~# xz -d -k tisdk-base-image-j7200-evm.rootfs.wic.xz
   root@j7200-evm:~# ls
   tisdk-base-image-j7200-evm.rootfs.wic tisdk-base-image-j7200-evm.rootfs.wic.xz
   root@j7200-evm:~# umount /dev/mmcblk0*
   root@j7200-evm:~# dd if=tisdk-base-image-j7200-evm.rootfs.wic of=/dev/mmcblk0
   root@j7200-evm:~#

To Boot the board from a flashed eMMC device, jump to :ref:`flash-emmc-boot`

.. _flash-emmc-manually:

**************************
Manually flash eMMC device
**************************

Partition and format eMMC device
================================

Following commands will partition the eMMC device from linux using fdisk, mkfs
utilities:

.. code-block:: console

   root@j7200-evm:~# umount /dev/mmcblk0*
   root@j7200-evm:~# dd if=/dev/zero of=/dev/mmcblk0 bs=1024 count=1024
   root@j7200-evm:~# fdisk /dev/mmcblk0

   Welcome to fdisk (util-linux 2.39.3).
   Changes will remain in memory only, until you decide to write them.
   Be careful before using the write command.

   Device does not contain a recognized partition table.
   Created a new DOS (MBR) disklabel with disk identifier 0x85204c5d.

   Command (m for help): n
   Partition type
      p   primary (0 primary, 0 extended, 4 free)
      e   extended (container for logical partitions)
   Select (default p): p
   Partition number (1-4, default 1): 1
   First sector (2048-31080447, default 2048): 
   Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-31080447, default 31080447): +128M

   Created a new partition 1 of type 'Linux' and of size 128 MiB.
   Partition #1 contains a vfat signature.

   Do you want to remove the signature? [Y]es/[N]o: Y

   The signature will be removed by a write command.

   Command (m for help): n
   Partition type
      p   primary (1 primary, 0 extended, 3 free)
      e   extended (container for logical partitions)
   Select (default p): p
   Partition number (2-4, default 2): 2
   First sector (264192-31080447, default 264192):
   Last sector, +/-sectors or +/-size{K,M,G,T,P} (264192-31080447, default 31080447): 

   Created a new partition 2 of type 'Linux' and of size 14.7 GiB.
   Partition #2 contains a ext4 signature.

   Do you want to remove the signature? [Y]es/[N]o: Y

   The signature will be removed by a write command.

   Command (m for help): t
   Partition number (1,2, default 2): 1
   Hex code or alias (type L to list all): c

   Changed type of partition 'Linux' to 'W95 FAT32 (LBA)'.

   Command (m for help): a
   Partition number (1,2, default 2): 1

   The bootable flag on partition 1 is enabled now.

   Command (m for help): w
   The partition table has been altered.
   Calling ioctl() to re-read partition table.
   Syncing disks.

   root@j7200-evm:~#
   root@j7200-evm:~# umount /dev/mmcblk0p*
   root@j7200-evm:~#
   root@j7200-evm:~# mkfs.vfat -F 32 -n "boot" /dev/mmcblk0p1
   mkfs.fat 4.2 (2021-01-31)
   mkfs.fat: Warning: lowercase labels might not work properly on some systems
   root@j7200-evm:~#
   root@j7200-evm:~# mkfs.ext4 -L "root" /dev/mmcblk0p2
   mke2fs 1.47.0 (5-Feb-2023)
   Discarding device blocks: done
   Creating filesystem with 3852032 4k blocks and 964768 inodes
   Filesystem UUID: 877458c6-bf40-46dd-87a1-062a948bc138
   Superblock backups stored on blocks: 
         32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208

   Allocating group tables: done
   Writing inode tables: done
   Creating journal (16384 blocks): done
   Writing superblocks and filesystem accounting information: done
   root@j7200-evm:~#


Populate eMMC device
====================

- Boot partition

  Populate Boot partition on eMMC device with a copy of SD card Boot partition.

  .. code-block:: console

     root@j7200-evm:~# umount /run/media/*
     root@j7200-evm:~# mkdir /mnt/sd-boot /mnt/emmc-boot
     root@j7200-evm:~# mount /dev/mmcblk1p1 /mnt/sd-boot
     root@j7200-evm:~# mount /dev/mmcblk0p1 /mnt/emmc-boot
     root@j7200-evm:~# cp -r /mnt/sd-boot/* /mnt/emmc-boot
     root@j7200-evm:~# sync
     root@j7200-evm:~# umount /mnt/*

  Alternatively, the boot files can be copied from any source manually.

- Rootfs partition

  Populate rootfs partition on eMMC device with a copy of SD card rootfs
  partition.

  .. code-block:: console

     root@j7200-evm:~# umount /run/media/*
     root@j7200-evm:~# mkdir /mnt/sd-rootfs /mnt/emmc-rootfs
     root@j7200-evm:~# mount /dev/mmcblk1p2 /mnt/sd-rootfs
     root@j7200-evm:~# mount /dev/mmcblk0p2 /mnt/emmc-rootfs
     root@j7200-evm:~# cp -r /mnt/sd-rootfs/* /mnt/emmc-rootfs
     root@j7200-evm:~# sync
     root@j7200-evm:~# umount /mnt/*

  Alternatively, the rootfs can be flashed from a tarball:

  .. code-block:: console

     root@j7200-evm:~# ls
     tisdk-base-image-j7200-evm.rootfs.tar.xz
     root@j7200-evm:~# umount /run/media/*
     root@j7200-evm:~# mkdir /mnt/emmc-rootfs
     root@j7200-evm:~# mount /dev/mmcblk0p2 /mnt/emmc-rootfs
     root@j7200-evm:~# tar -xf tisdk-base-image-j7200-evm.rootfs.tar.xz -C /mnt/emmc-rootfs
     root@j7200-evm:~# sync
     root@j7200-evm:~# umount /mnt/emmc-rootfs

To Boot the board from a flashed eMMC device, jump to :ref:`flash-emmc-boot`


.. _flash-emmc-boot:

*****************************************
Boot through UDA partition of emmc device
*****************************************

Following are the steps to boot the target through eMMC device.
For more information refer to :ref:`boot-linux-from-mmc`

- To give the ROM access to the boot partition, the following commands must be
  run from the u-boot prompt for the first time.
  To boot from UDA partition of eMMC:

  .. code-block:: console

     => mmc partconf 0 1 7 1
     => mmc bootbus 0 2 0 0

- Now we can reboot the board with eMMC bootmode selected.

- Even with eMMC bootmode selected u-boot defaults to use SD card (mmcdev=1)
  for Kernel and filesystem. To boot kernel and filesystem from eMMC, use the
  following commands at the u-boot prompt:

  .. code-block:: console

     => setenv mmcdev 0
     => setenv bootpart 0:2
     => boot


