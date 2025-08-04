.. _how-to-emmc-boot:

#########################################
How to flash eMMC and boot with eMMC Boot
#########################################

Overview
========

This how to guide allows to prepare and flash the embedded multimedia card (eMMC) device to
boot using *eMMC boot*, that is, to boot from Boot0 or Boot1 eMMC hardware partitions and
boot the root filesystem (rootfs) from eMMC user data area (UDA).

.. note::

   This process will require a working secure digital (SD) card that can boot the device to Linux kernel.

.. _how-to-emmc-layout:

eMMC layout
===========

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'J7200')

   .. code-block:: text

      +----------------------------------+0x0      +-------------------------+0x0
      |      tiboot3.bin (1 MB)          |         |                         |
      +----------------------------------+0x800    |                         |
      |       tispl.bin (2 MB)           |         |        rootfs           |
      +----------------------------------+0x1800   |                         |
      |       u-boot.img (4 MB)          |         |                         |
      +----------------------------------+0x3800   |                         |
      |      environment (128 KB)        |         |                         |
      +----------------------------------+0x3900   |                         |
      |   backup environment (128 KB)    |         |                         |
      +----------------------------------+0x3A00   +-------------------------+
                   Boot0 (8 MB)                              UDA

.. ifconfig:: CONFIG_part_variant in ('J721S2', 'AM62X', 'AM62PX', 'AM62AX', 'AM62DX', 'AM62LX')

   .. code-block:: text

      +----------------------------------+0x0      +-------------------------+0x0
      |      tiboot3.bin (1 MB)          |         |                         |
      +----------------------------------+0x400    |                         |
      |       tispl.bin (2 MB)           |         |        rootfs           |
      +----------------------------------+0x1400   |                         |
      |       u-boot.img (4 MB)          |         |                         |
      +----------------------------------+0x3400   |                         |
      |      environment (128 KB)        |         |                         |
      +----------------------------------+0x3500   |                         |
      |   backup environment (128 KB)    |         |                         |
      +----------------------------------+0x3600   +-------------------------+
                   Boot0 (8 MB)                              UDA

.. ifconfig:: CONFIG_part_variant not in ('AM64X', 'J7200', 'J721S2', 'AM62X', 'AM62PX', 'AM62AX', 'AM62DX', 'AM62LX')

   .. code-block:: text


      +----------------------------------+0x0      +-------------------------+0x0
      |      tiboot3.bin (512 KB)        |         |                         |
      +----------------------------------+0x400    |                         |
      |       tispl.bin (2 MB)           |         |                         |
      +----------------------------------+0x1400   |        rootfs           |
      |       u-boot.img (4 MB)          |         |                         |
      +----------------------------------+0x3400   |                         |
      |      environment (128 KB)        |         |                         |
      +----------------------------------+0x3500   |                         |
      |   backup environment (128 KB)    |         |                         |
      +----------------------------------+0x3600   |                         |
      |          sysfw (1 MB)            |         |                         |
      +----------------------------------+0x3E00   +-------------------------+
                   Boot0 (8 MB)                              UDA

Flash boot loader binaries to eMMC
==================================

To boot with *eMMC boot* the eMMC needs to be prepared before hand. The recommended process
is to flash an SD card with TI SDK image, copy the boot loader binaries that will be flashed to
eMMC in the SD card "boot" partition in emmc/ folder, boot the board with *MMCSD boot* from SD
filesystem (FS) mode, and proceed to flash the eMMC from either u-boot or Linux.

**Erase eMMC**

In u-boot we can optionally erase boot0 or boot1 with :command:`mmc erase` command, where the
general syntax is:

.. code-block:: console

   $ mmc erase blk# cnt

The following example, shows how to find the largest block number for boot0 and erase boot0.
To erase boot1, replace ``mmc dev 0 1`` with ``mmc dev 0 2``.

.. code-block:: console

   => mmc dev 0 1
   switch to partitions #1, OK
   mmc0(part 1) is current device
   => mmc read ${loadaddr} 0xfffffffff 1
   MMC read: dev # 0, block # -1, count 1 ... MMC: block number 0x100000000 exceeds max(0xfc00)
   0 blocks read: ERROR
   => mmc erase 0 0xfc00
   MMC erase: dev # 0, block # 0, count 64512 ... 64512 blocks erased: OK

**Flash from u-boot**

Stop at u-boot prompt and flash eMMC by using :command:`fatload` and :command:`mmc write` commands
to load binaries from SD card and flash them to eMMC Boot0.

In this example, eMMC device is ``dev 0``, to find which device is eMMC, refer to
:ref:`this <uboot-listing-mmc-devices>`. section. To flash to eMMC Boot1 instead, replace
``mmc dev 0 1`` with ``mmc dev 0 2``.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. note::

      For am62lx device there is an errata for booting with *eMMC boot* `here <https://www.ti.com/lit/pdf/sprz582//>`__,
      hence it is recommended to boot with *MMCSD boot*, as shown :ref:`here <how-to-mmcsd-boot-from-emmc-uda>`.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. code-block:: console

      => mmc dev 0 1
      => fatload mmc 1 ${loadaddr} emmc/tiboot3.bin
      => mmc write ${loadaddr} 0x0 0x800
      => fatload mmc 1 ${loadaddr} emmc/tispl.bin
      => mmc write ${loadaddr} 0x800 0x1000
      => fatload mmc 1 ${loadaddr} emmc/u-boot.img
      => mmc write ${loadaddr} 0x1800 0x2000

.. ifconfig:: CONFIG_part_variant in ('J7200')

   .. code-block:: console

      => mmc dev 0 1
      => fatload mmc 1 ${loadaddr} emmc/tiboot3.bin
      => mmc write ${loadaddr} 0x0 0x800
      => fatload mmc 1 ${loadaddr} emmc/tispl.bin
      => mmc write ${loadaddr} 0x800 0x1000
      => fatload mmc 1 ${loadaddr} emmc/u-boot.img
      => mmc write ${loadaddr} 0x1800 0x2000

.. ifconfig:: CONFIG_part_variant in ('J721S2', 'AM62X', 'J784S4','J742S2', 'J722S', 'AM62PX', 'AM62AX', 'AM62DX','AM62LX')

   .. code-block:: console

      => mmc dev 0 1
      => fatload mmc 1 ${loadaddr} emmc/tiboot3.bin
      => mmc write ${loadaddr} 0x0 0x400
      => fatload mmc 1 ${loadaddr} emmc/tispl.bin
      => mmc write ${loadaddr} 0x400 0x1000
      => fatload mmc 1 ${loadaddr} emmc/u-boot.img
      => mmc write ${loadaddr} 0x1400 0x2000

.. ifconfig:: CONFIG_part_variant not in ('AM64X', 'J7200', 'J721S2', 'AM62X', 'J784S4','J742S2', 'J722S', 'AM62PX', 'AM62AX', 'AM62DX', 'AM62LX')

   .. code-block:: console

      => mmc dev 0 1
      => fatload mmc 1 ${loadaddr} emmc/tiboot3.bin
      => mmc write ${loadaddr} 0x0 0x400
      => fatload mmc 1 ${loadaddr} emmc/tispl.bin
      => mmc write ${loadaddr} 0x400 0x1000
      => fatload mmc 1 ${loadaddr} emmc/u-boot.img
      => mmc write ${loadaddr} 0x1400 0x2000
      => fatload mmc 1 ${loadaddr} emmc/sysfw.itb
      => mmc write ${loadaddr} 0x3600 0x800

**Flash from Linux**

At Linux prompt, flash eMMC by using :command:`cp` and :command:`dd` commands to load binaries
from SD card and flash them to eMMC Boot0.

In this example, eMMC is :file:`/dev/mmcblk0*` and SD :file:`/dev/mmcblk1*` to find which
device is eMMC, refer to :ref:`this <mmc-listing-mmc-devices-linux>`. section. To flash to
eMMC Boot1 instead, replace ``mmcblk0boot0`` with ``mmcblk0boot1``.

.. code-block:: console

   # Enable write access to the Boot0 partition
   root@<machine>:~# echo 0 > /sys/block/mmcblk0boot0/force_ro
   root@<machine>:~# mkdir /mnt/sdboot && mount /dev/mmcblk1p1 /mnt/sdboot && cd /mnt/sdboot
   root@<machine>:~# dd if=emmc/tiboot3.bin of=/dev/mmcblk0boot0 seek=0 bs=512
   root@<machine>:~# dd if=emmc/tispl.bin of=/dev/mmcblk0boot0 seek=1024 bs=512
   root@<machine>:~# dd if=emmc/u-boot.img of=/dev/mmcblk0boot0 seek=5120 bs=512

Where seek is the eMMC offset converted to decimal type. For example, for seek=1024, we are
flashing to offset 0x400. Please refer :ref:`here <how-to-emmc-layout>` for the offsets in eMMC
when flashing boot loader files.

Flash rootfs to eMMC
====================

To boot the rootfs from eMMC UDA, the eMMC needs to be prepared before hand. It is not
possible to format a partition to ext4 in U-Boot, so the recommended process is to flash
an SD card with TI SDK image, boot the device with SD card boot to Linux kernel prompt,
and prepare eMMC UDA from Linux.

Note that in the following examples the "root" partition is the second disk partition, in our
case, "root" will be the first partition so replace :file:`/dev/mmcblk0p2` with :file:`/dev/mmcblk0p1`.
First create a "root" partition to flash the rootfs as shown :ref:`here <mmc-create-root-partition-emmc-linux>`.
The new disk partition should be formatted as ext4 type as shown :ref:`here <mmc-format-partition-ext4>`.
Mount the new partition and flash the rootfs as shown :ref:`here <mmc-flash-emmc-uda-root>`.
The Linux kernel :file:`Image` and DT file are expected to be in the /boot folder of the
"root" partition in order for u-boot to find and load them.

eMMC boot configuration
=======================

Now that we have flashed the eMMC device, reboot the board and stop at u-boot prompt to
set configuration for *eMMC boot*.

**Enable boot from HW partition**

After flashing binaries to eMMC flash, the eMMC device Extended CSD register fields:
BUS_WIDTH and PARTITION_CONFIG must be set so ROM will use the correct configuration
for *eMMC boot*. Set by using the :command:`mmc bootbus` and :command:`mmc partconf` commands.
Go to ``Boot from Boot0`` if booting for eMMC boot0. Alternatively, ``Boot from Boot1`` if
booting from eMMC boot1.

- The :command:`mmc bootbus` command sets the BOOT_BUS_WIDTH field where ``mmc bootbus 0 2 0 0``
  selects **x8 (sdr/ddr) buswidth in boot operation mode**.
- The :command:`mmc partconf` command can be used to configure what hardware partition
  to boot from. The general syntax is:

.. code-block:: console

   $ mmc partconf <dev> [[varname] | [<boot_ack> <boot_partition> <partition_access>]]

Where <dev> is mmc device index.

- For more information on these commands, go `here <https://docs.u-boot.org/en/latest/usage/cmd/mmc.html>`__.

**Boot from Boot0**

.. code-block:: console

   => mmc partconf 0 1 1 1
   => mmc bootbus 0 2 0 0

**Boot from Boot1**

.. code-block:: console

   => mmc partconf 0 1 2 1
   => mmc bootbus 0 2 0 0

**Enable warm reset**

   On eMMC devices, warm reset will not work if EXT_CSD[162] bit is unset since the
   reset input signal will be ignored. Warm reset is required to be enabled in order
   for the eMMC to be in a "clean state" on power-on reset so that ROM can do
   a clean enumeration. To set the EXT_CSD[162] bit, stop at u-boot prompt and enter
   the following command:

.. code-block:: console

   => mmc rst-function 0 1

.. warning::

   This is a write-once field. For more information, refer to the u-boot
   doc found `here <https://docs.u-boot.org/en/latest/usage/cmd/mmc.html>`__.

**U-boot environment**

The command :command:`saveenv` is no longer used in TI SDK, thus, the following
environment workarounds must be implemented to boot from eMMC.

At u-boot prompt, run the following commands to boot Linux from eMMC UDA:

.. code-block:: console

   => setenv mmcdev 0
   => setenv bootpart 0
   => boot

Or change the u-boot environment for *eMMC boot* to boot completely from eMMC.

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
   +bootpart=0:1
    bootdir=/boot
    rd_spec=-

Re-build boot loader binaries and copy build outputs to the SD card "boot" partition
and :file:`emmc/` folder. Proceed to flash eMMC with these binaries as shown in this
step-by-step guide.

Boot from eMMC boot partition
=============================

Finally we can proceed to change boot mode pins to *eMMC boot* according to TRM, under:
:file:`Initialization/Boot Mode Pins` and power cycle the board.
