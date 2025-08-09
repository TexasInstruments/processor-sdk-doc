.. _how-to-mmcsd-boot-from-emmc-uda:

########################################
How to flash eMMC and boot from eMMC UDA
########################################

Overview
========

This how to guide allows to prepare and flash the embedded multimedia card (eMMC) device to boot using
*MMCSD boot*, from eMMC UDA in filesystem (FS) mode.

.. note::

   This process will require a working (secure digital) SD card that can boot the device to Linux kernel.

- To flash eMMC using a partitioned SD card image from the SDK, go :ref:`here <how-to-flash-emmc-wic>`
- To flash eMMC manually, go :ref:`here <how-to-flash-emmc-manual>`

.. _how-to-flash-emmc-wic:

Flash eMMC with disk image
==========================

Copy the .wic formatted disk image from the SDK installer to target filesystem, boot the
device via SD card boot and at Linux prompt, find the eMMC block device as shown
:ref:`here <mmc-listing-mmc-devices-linux>` and flash the eMMC as shown below:

.. code-block:: console

   root@<machine>:~# ls
   tisdk-base-image-<soc>-evm.rootfs.wic.xz
   root@<machine>:~# xz -d -k tisdk-base-image-<soc>-evm.rootfs.wic.xz
   root@<machine>:~# ls
   tisdk-base-image-<soc>-evm.rootfs.wic tisdk-base-image-<soc>-evm.rootfs.wic.xz
   root@<machine>:~# umount /dev/mmcblk0*
   root@<machine>:~# dd if=tisdk-base-image-<soc>-evm.rootfs.wic of=/dev/mmcblk0

.. _how-to-flash-emmc-manual:

Manually flash eMMC device
==========================

To boot with *MMCSD boot* from eMMC UDA in FS mode, the eMMC needs to be prepared before hand.
The recommended process is to flash an SD card with TI SDK image, copy the boot loader binaries
that will be flashed to eMMC in the SD card "boot" partition in :file:`emmc/` folder, boot the
board with *MMCSD boot* from SD (FS mode), and proceed to create disk partitions and flash the
eMMC from Linux.

**Create disk partitions**

In Linux, create a "boot" partition to store boot loader binaries as shown
:ref:`here <mmc-create-boot-partition-emmc-linux>` and
a "root" partition for the foot filesystem (rootfs): as shown
:ref:`here <mmc-create-root-partition-emmc-linux>`.

**Format partitions**

For the "boot" partition, format as *vfat* type as shown :ref:`here <mmc-format-partition-vfat>`
and for the "root" partition, format as *ext4* type as shown :ref:`here <mmc-format-partition-ext4>`.

**Flash eMMC UDA**

Mount the new "boot" partition and copy the boot loader binaries to the new partition
as shown :ref:`here <mmc-flash-emmc-uda-boot>`. Mount the new "root" partition
and copy the rootfs to the partition as shown :ref:`here <mmc-flash-emmc-uda-root>`

MMCSD boot configuration from eMMC UDA
======================================

Now that we have flashed the eMMC device, reboot the board and stop at u-boot prompt to
set configuration for *MMCSD boot* from UDA.

**Enable boot from eMMC UDA**

After flashing binaries to eMMC flash, the eMMC device Extended CSD register fields:
BUS_WIDTH and PARTITION_CONFIG must be set so ROM will use the correct configuration
for *MMCSD boot* from UDA.

Set by using the :command:`mmc bootbus` and :command:`mmc partconf` commands. Go to
``Boot from UDA``.

- The :command:`mmc bootbus` command sets the BOOT_BUS_WIDTH field where ``mmc bootbus 0 2 0 0``
  selects **x8 (sdr/ddr) buswidth in boot operation mode**.
- The :command:`mmc partconf` command can be used to configure what hardware partition
  to boot from. The general syntax is:

.. code-block:: console

   $ mmc partconf <dev> [[varname] | [<boot_ack> <boot_partition> <partition_access>]]

Where <dev> is MMC device index.

- For more information on these commands, go `here <https://docs.u-boot.org/en/latest/usage/cmd/mmc.html>`__.

**Boot from UDA**

.. code-block:: console

   => mmc partconf 0 1 7 1
   => mmc bootbus 0 2 0 0

**Enable warm reset**

   On eMMC devices, warm reset will not work if EXT_CSD[162] bit is unset since the
   reset input signal will be ignored. Warm reset is required to be enabled in order
   for the eMMC to be in a "clean state" on power-on reset so that ROM can do
   a clean enumeration. To set the EXT_CSD[162] bit, stop at u-boot prompt and run
   the following command:

.. code-block:: console

   => mmc rst-function 0 1

.. warning::

   This is a write-once field. For more information, refer to the u-boot
   doc found `here <https://docs.u-boot.org/en/latest/usage/cmd/mmc.html>`__.

**U-boot environment**

The command :command:`saveenv` is no longer used in TI SDK, thus, the following
environment workarounds must be implemented to boot from eMMC UDA.

At u-boot prompt, run the following commands to boot Linux from UDA:

.. code-block:: console

   => setenv mmcdev 0
   => setenv bootpart 0:2
   => boot

Or change the u-boot environment for *MMCSD boot* to boot completely from eMMC.

First apply the following change in u-boot for any SoC.

.. code-block:: diff

   diff --git a/board/ti/<soc>/<soc>.env b/board/ti/<soc>/<soc>.env
   index 82b9f0741bb..73d59ac425c 100644
   --- a/board/ti/<soc>/<soc>.env
   +++ b/board/ti/<soc>/<soc>.env
   @@ -17,8 +17,8 @@ run_kern=booti ${loadaddr} ${rd_spec} ${fdtaddr}

    boot_targets=mmc1 mmc0 usb pxe dhcp
    boot=mmc
   -mmcdev=1
   -bootpart=1:2
   +mmcdev=0
   +bootpart=0:2
    bootdir=/boot
    rd_spec=-

Re-build boot loader binaries and copy build outputs to the SD card "boot" partition
and :file:`emmc/` folder. Proceed to flash eMMC with these binaries as shown in this
step-by-step guide.

Boot from eMMC UDA
==================

Finally we can proceed to change boot mode pins to *MMCSD boot* from eMMC (port 0) in FS
mode according to TRM, under: :file:`Initialization/Boot Mode Pins` and power cycle the
board.
