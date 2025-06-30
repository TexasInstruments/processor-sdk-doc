.. _auth_boot_guide:

#############################
Authenticated Boot User Guide
#############################

************
Introduction
************

As we head into a new world of security requirements and regulations, secure boot is the first and most essential step. Secure boot is a process that ensures only authenticated software is selected and loaded, protecting systems from unauthorized or malicious code trying to load a unknown bootloader or OS on your device.

Secure boot is achieved by verifying digital signatures of each software layer involved during boot before executing that code. This requires that the design of hardware and software is prepared and developed with security in mind.

********
Learning
********

Root of Trust (RoT)
===================

The Root of Trust is the foundation of authenticated boot. It is the first component in the system that is inherently trusted and is responsible for verifying all subsequent components in the boot process. The RoT is usually implemented in hardware, firmware, or a combination of both.

There are two main types of RoT:

   - *Hardware Root of Trust*: Typically embedded in a secure element (such as a Trusted Platform Module [TPM], Hardware Security Module [HSM], or Secure Boot ROM). It is immutable and performs the first-stage verification.

   - *Firmware/Software Root of Trust*: This is the first code that runs on the system, typically stored in Read-Only Memory (ROM) or write-protected storage.

Chain of Trust (CoT)
====================

The Chain of Trust extends the RoT by ensuring that every stage of the boot process verifies the next stage before executing it. Each stage is cryptographically signed, and verification is performed using public key cryptography.

Process:

   1. Boot ROM - Verifies the Primary Bootloader using a cryptographic signature.

   2. Primary Bootloader - Verifies the Secondary Bootloader (U-Boot, GRUB, etc.) before executing it.

   3. Secondary Bootloader - Verifies the Kernel before booting the operating system.

   4. Kernel - Verifies the Initramfs and Root Filesystem using mechanisms like dm-verity or signatures.

Each step in the chain must be verified to maintain system integrity. If any stage fails verification, the system will refuse to boot or attempt recovery.

Device Mapper
=============

Device Mapper (dm) is a Linux kernel subsystem that provides an abstraction layer for managing block devices. It enables advanced features like encryption (dm-crypt) and integrity verification (dm-verity) at the block device level.

dm-verity
---------

dm-verity is a kernel feature designed to ensure that a block device remains read-only and has not been tampered with. It is commonly used in Android Verified Boot (AVB) and Linux-based secure boot systems.

The root filesystem is hashed block by block, creating a hash tree (Merkle tree). The root hash of the hash tree is signed by a trusted key. During boot, the kernel verifies the hash tree before mounting the root filesystem. If any block is modified, the hash verification will fail, preventing tampered data from being used.

While dm-verity guarantees data integrity, it does not promise confidentiality and works only on read-only filesystems.

dm-crypt
--------

dm-crypt is a device-mapper target used for transparent disk encryption. It ensures data confidentiality by encrypting the entire partition or block device.

A user provides an encryption key (stored securely in a TPM or entered manually). dm-crypt encrypts each block before writing it to disk. When reading data, dm-crypt decrypts blocks on the fly. Only authorized users with the correct key can access the decrypted data.

Before encrypting a drive, it is recommended to perform a secure erase by overwriting the entire device with random data. This can be done by following this `guide <https://wiki.archlinux.org/title/Dm-crypt/Drive_preparation>`_.

*****
Setup
*****

.. Image:: /images/Auth_default_bootflow.png
     :align: center

.. note::

   A new Yocto layer is in the works to automate all of the below steps

The following steps describe how to build user-space tools and configuration on Yocto. Please use :ref:`Processor SDK - Building the SDK with Yocto <building-the-sdk-with-yocto>` as reference.

#. Use the latest :ref:`oe-config file <yocto-layer-configuration>`. Build the default image and flash onto a 32GB+ SD card:

   .. code-block:: console

      MACHINE=<machine> bitbake -k tisdk-default-image

#. For this demo, the root filesystem is copied from the default rootfs into the encrypted partition on a 32GB+ SD card. Hence, the SD card needs to be partitioned accordingly. It is recommended to create 2 additional ext4 partitions bringing the total to 4 partitions:

   +-----------------+----------------+-------+--------------+
   | Partition Label | /dev partition | Size  |   Comments   |
   +=================+================+=======+==============+
   |      boot       | /dev/mmcblk1p1 | 128MB |   Default    |
   +-----------------+----------------+-------+--------------+
   |      root       | /dev/mmcblk1p2 |  10GB |   Default    |
   +-----------------+----------------+-------+--------------+
   |      crypt      | /dev/mmcblk1p3 |  10GB | Same as root |
   +-----------------+----------------+-------+--------------+
   |     verity      | /dev/mmcblk1p4 |  1GB  | 10% of crypt |
   +-----------------+----------------+-------+--------------+

#. On the host machine, build the Linux Kernel with support for these configs:

   .. code-block:: kconfig

      CONFIG_BLK_DEV_DM=y
      CONFIG_DM_CRYPT=y
      CONFIG_DM_VERITY=y

   These configs can be added using a separate .cfg file or the kernel can be edited using

   .. code-block:: console

      MACHINE=<machine> bitbake -c menuconfig linux-ti-staging

#. Edit :file:`sources/meta-arago/meta-arago-distro/recipes-core/images/tisdk-tiny-initramfs.bb` to add *dm-crypt* and *dm-verity* support:

   .. code-block:: console

      PACKAGE_INSTALL += " cryptsetup lvm2 e2fsprogs-mke2fs"

#. Build the initramfs image:

   .. code-block:: console

      MACHINE=<machine> bitbake -k tisdk-tiny-initramfs

#. Extract the initramfs .cpio file and add a :file:`pass_key` file

   .. code-block:: console

      # Extract command
      cpio -iv < <path to .cpio>

      # Create a random pass key
      tr -dc '[:alnum:]' </dev/urandom | head -c64 > <initramfs_root>/home/pass_key

      # Create cpio from initramfs folder
      cd <initramfs_root>
      find . | sort | cpio --reproducible -o -H newc -R root:root > ../<name>.cpio

#. Package the initramfs into the kernel by using the :code:`menuconfig` and build the kernel.

   .. code-block:: kconfig

        General setup ->
            Initial RAM filesystem and RAM disk (initramfs/initrd) support ->
                Initramfs source file(s)
                    /path/to/initramfs.cpio

#. Replace the :file:`root/boot/Image` with the updated Image and boot.

#. Run the following commands in initramfs to setup the crypt and verity partitions

   .. code-block:: console

      # Unmount encrypted partitions if already mounted
      umount /dev/mmcblk1p3
      umount /dev/mmcblk1p4

      # Create the mount paths
      mkdir /old_mnt
      mkdir /mnt

      # Mount default root
      mount /dev/mmcblk1p2 /old_mnt

      # Setup the encrypted partition
      # The default cipher at the time of writing this guide is aes-xts-plain64
      # Hardware acceleration for dm-crypt is not tested

      cryptsetup luksFormat /dev/mmcblk1p3 --key-file=/home/pass_key --batch-mode
      cryptsetup luksOpen /dev/mmcblk1p3 crypt_root --key-file=/home/pass_key

      # Use following commands to verify the status of the LUKS device
      cryptsetup -v status crypt_root    #Status Check
      cryptsetup luksDump /dev/mmcblk1p3 #Dump Headers

      # Format and copy rootfs inside encrypted partition
      mkfs.ext4 /dev/mapper/crypt_root

      # If command is successful you should see below output
      root@am62xx-evm:~# mkfs.ext4 /dev/mapper/crypt_root
      mkfs.ext4 /dev/mapper/crypt_root
      mke2fs 1.47.0 (5-Feb-2023)
      Creating filesystem with 2952704 4k blocks and 738192 inodes
      Filesystem UUID: 8cc1c02e-7b0a-4d57-82f0-f3a4c35e0f00
      Superblock backups stored on blocks:
          32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208

      Allocating group tables: done
      Writing inode tables: done
      Creating journal (16384 blocks): done
      Writing superblocks and filesystem accounting information: done

      # Mount the encrypted partition
      mount /dev/mapper/crypt_root /mnt
      cp -ar /old_mnt/. /mnt
      umount /mnt

      # Setup verity
      veritysetup format /dev/mapper/crypt_root /dev/mmcblk1p4

      # Output will have a Root hash, copy that hash as it will be used in next step
      ...
      Root hash: 4392712ba01368efdf14b05c76f9e4df0d53664630b5d48632ed17a137f39076

#. Back on the host machine, add this init file at the root of the initramfs:

   .. code-block:: bash

      #!/bin/sh

      sleep 5 # For mmcblk1 to populate
      chown root:root /bin/mount.util-linux  # Provide correct ownership

      # Mount dev, procfs and sysfs
      /bin/mount -t devtmpfs none /dev
      /bin/mount -t proc none /proc
      /bin/mount -t sysfs none /sys

      # Decrypt
      # If the cipher was previously changed, add --cipher aes-cbc-plain
      /sbin/cryptsetup luksOpen --key-file=/home/pass_key /dev/mmcblk1p3 crypt_root

      # Verify (use the root hash from the previous ``veritysetup format`` command)
      /sbin/veritysetup open /dev/mapper/crypt_root verity_root /dev/mmcblk1p4 4392712ba01368efdf14b05c76f9e4df0d53664630b5d48632ed17a137f39076

      mount -o ro /dev/mapper/verity_root /mnt

      # Jump to secure root FS
      exec switch_root /mnt/ /sbin/init

   and give it the appropriate permissions to run:

   .. code-block:: console

      chmod +x init

#. Repackage the initramfs into the kernel, build and replace the :file:`root/boot/Image` and boot.

.. Image:: /images/Auth_secure_bootflow.png
     :align: center

**********
Next steps
**********

This guide showcases the authenticated boot flow on TI devices and is not meant to be directly used in production. The demo utilizes a pass_key to secure the encrypted partition and is placed in the initramfs in a non-secure manner.

********
See Also
********

- `dm-crypt <https://wiki.archlinux.org/title/Dm-crypt>`__
- `dm-verity <https://wiki.archlinux.org/title/Dm-verity>`__
