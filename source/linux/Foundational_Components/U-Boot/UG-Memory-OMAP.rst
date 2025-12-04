SD, eMMC and USB
################

The following guide shows how to flash and boot from storage media like the
embedded multimedia card (eMMC), secure digital (SD) card, and USB storage
devices. While this is a step-by-step guide, it is in no way extensive and
does not cover all the per-platform corner-cases. For any  issues/questions
on this guide, please reach out to: `Help e2e <https://e2e.ti.com//>`__.

MMC
***

.. _uboot-listing-mmc-devices:

Listing MMC devices
===================

Usually in all the platforms there will be one or two MMC instances of which one
would be SD and the other would be eMMC. The index of them can vary from
one class of platforms to the other. For a given platform, the device
number: **mmcdev=[0:1]** can be found in the following way:

.. code-block:: console

   => mmc list
   OMAP SD/MMC: 0 (SD)

The device number "**0**" is for SD, here eMMC is not enumerated.

.. _uboot-selecting-mmc-device-and-partitions:

Selecting MMC device and paritions
==================================

To selct an MMC device in u-boot, the command: :command:`mmc dev` could be used.
The general syntax is:

.. code-block:: console

   => mmc dev [dev] [partition]

The following lists examples and their explanation for each MMC device
and partitions according to the example in: :ref:`uboot-listing-mmc-devices`.

.. code-block:: console

   => mmc dev 0 # select SD

View MMC partition contents
===========================

This section assumes an SD card or eMMC was prepared previously to
boot the device.

.. note::

   For eMMC, typically, the device ships without a partition table
   If there is a need to create a partition in UDA (to flash the rootfs),
   please go to: :ref:`create partition in UDA <create-partitions-in-emmc-uda-from-linux>`
   and format the partition: :ref:`formatting eMMC partition <formatting-mmc-partition-from-linux>`
   before proceeding to look at the eMMC partition contents.

To verify partitions in any MMC device from u-boot prompt, use the
command: :command:`mmc part`. If the partitions are formatted with a
file system type that is supported by u-boot, you can view the contents
of the MMC partition as show below:

.. code-block:: console

   => ls mmc 0:1
      7700992   zImage
         112421   am437x-idk-evm.dtb
         118979   am437x-sk-evm.dtb
         122333   am43x-epos-evm.dtb
                  extlinux/
         158859   MLO
         814184   u-boot.img
            717   uEnv.txt
         84299   am437x-gp-evm.dtb

      8 file(s), 1 dir(s)

   => ls mmc 0:2 boot
      <DIR>       4096 .
      <DIR>       4096 ..
      <DIR>       4096 dtb
               7700992 zImage

Where the general syntax is:

.. code-block:: console

   $ ls <interface> [<dev[:partition]> [directory]]

.. _flash-and-boot-to-uboot-prompt:

Flash and boot SPL from eMMC
============================

.. ifconfig:: CONFIG_part_variant in ('AM335X')

   .. note::

      Please note that am335 devices do not support eMMC boot from boot0/boot1,
      only boot from eMMC UDA.

In some cases it is desirable to write :file:`MLO` and :file:`u-boot.img`
as raw images to the MMC device rather than load them from a filesystem.
In that case, the command :command:`mmc write` can be used to flash
the MMC device.

In this example, :samp:`mmc dev 0` selects an eMMC device that was enumerated. In
the following example, flash the eMMC boot0 HW partition, loading the binaries from
SD and assuming the files: :file:`MLO` and :file:`u-boot.img` exist on the SD card
first (boot) partition:

.. code-block:: console

   => mmc dev 0
   => mmc rescan
   => mmc dev 1 1
   => fatload mmc 0 ${loadaddr} MLO
   => mmc write ${loadaddr} 0x0 0x300
   => fatload mmc 0 ${loadaddr} u-boot.img
   => mmc write ${loadaddr} 0x300 0x400

To flash the eMMC boot0 HW partition from network tftp:

.. code-block:: console

   => setenv autoload no
   => dhcp
   => mmc dev 1 1
   => tftp ${loadaddr} MLO
   => mmc write ${loadaddr} 0x0 0x300
   => tftp ${loadaddr} u-boot.img
   => mmc write ${loadaddr} 0x300 0x400

To flash the eMMC UDA HW partition from SD:
Flash each binary at specific offsets chosen to not overwrite the partition table
on the device. Assuming that the files exist on the SD card.

.. code-block:: console

   => mmc dev 0
   => mmc rescan
   => mmc dev 1
   => fatload mmc 0 ${loadaddr} MLO
   => mmc write ${loadaddr} 0x100 0x100
   => mmc write ${loadaddr} 0x200 0x100
   => fatload mmc 0 ${loadaddr} u-boot.img
   => mmc write ${loadaddr} 0x300 0x400
   => fatload mmc 0 ${loadaddr} rootfs.ext4
   => mmc write ${loadaddr} 0x1000 ...rootfs.ext4 size in bytes divided by 512, in hex...

eMMC boot configuration
-----------------------

We also need to configure the eMMC to boot from boot0 HW partition using the :command:`bootbus`
and :command:`partconf` commands. The :command:`bootbus` command sets the eMMC into
dual data rate mode with a bus width of 8 to match with the bus configuration supported
by the Boot ROM. The :command:`partconf` command gives access to the boot0 HW partition
during boot operation. Note that these configurations are limited to boot operation and
the eMMC can be set to its highest speed mode once boot operation is complete. All these
are non-volatile configurations that need to be done **once per eMMC/board** .

.. code-block:: console

   => mmc bootbus 1 2 0 2
   => mmc partconf 1 1 1 0
   => mmc rst-function 1 1

Flashing an MMC device using USB-DFU
====================================

To see the list of available places to write to (in DFU terms, altsettings) list the
MMC partitions with :command:`mmc part` command, run :samp:`printenv dfu_alt_info_mmc`
or :samp:`printenv dfu_alt_info_emmc` to see how they are mapped and exposed to
:command:`dfu-util`.

.. code-block:: console

   => mmc part

   Partition Map for MMC device 0  --   Partition Type: DOS

   Partition     Start Sector     Num Sectors     Type
      1                   63          144522       c Boot
      2               160650         1847475      83
      3              2024190         1815345      83
   => printenv dfu_alt_info_mmc
   dfu_alt_info=boot part 0 1;rootfs part 0 2;MLO fat 0 1;u-boot.img fat 0 1;uEnv.txt fat 0 1"

.. note::

   The above command: :command:`mmc part` lists the partitions in the current selected
   device. Switch to a different MMC device with :command:`mmc dev`, refer to
   :ref:`uboot-selecting-mmc-device-and-partitions`.

This means that you can tell dfu-util to write anything to any of:

-  boot
-  rootfs
-  MLO
-  u-boot.img
-  uEnv.txt

And that the :file:`MLO`, :file:`u-boot.img` and :file:`uEnv.txt` files are to be
written to a FAT filesystem.

To start DFU on the target on the first MMC device:

.. code-block:: console

   => setenv dfu_alt_info ${dfu_alt_info_mmc}
   => dfu 0 mmc 0

On boards like AM57x GP EVM or BeagleBoard x15, where the second USB
instance is used as USB client, the dfu command becomes:

.. code-block:: console

   => dfu 1 mmc 0

Then on the host PC to write :file:`MLO` to an existing boot partition:

.. code-block:: console

   $ sudo dfu-util -D MLO -a MLO

On the host PC to overwrite the current boot partition contents with a
new created on the host FAT filesystem image:

.. code-block:: console

   $ sudo dfu-util -D fat.img -a boot

Flashing an SD card from a host PC
==================================

This section assumes that you have flashed an SD card using the
script "create-sdcard.sh" packaged in the installer or have
made a compatible layout manually. In this case, you will need
to copy the boot images:

- :file:`MLO`
- :file:`u-boot.img`

to the SD card *boot* partition. At this point, the device can boot to u-boot prompt.

USB
***

.. _uboot-configure-usb-in-host-mode:

Configuring USB in Host Mode
============================

Configuring USB in host mode documentation is pending for |__PART_FAMILY_NAME__|,
please reach out to:  `Help e2e <https://e2e.ti.com//>`__ for additional information.

.. _uboot-usb-msc-boot:

Flash and boot SPL from USB storage
===================================

.. ifconfig:: CONFIG_part_variant not in ('AM437X')

   Boot SPL from USB storage documentation is pending for |__PART_FAMILY_NAME__|,
   please reach out to:  `Help e2e <https://e2e.ti.com//>`__ for additional information.

.. ifconfig:: CONFIG_part_variant in ('AM437X')

   Booting to U-Boot prompt from USB storage is supported. The following are the
   steps to be followed:

   - In U-Boot the USB controller can be used in either host or peripheral mode.
   - Build the bootloader images using the "am43xx_evm_usbhost_boot_defconfig". For
     instructions to build the bootloader images please refer to :ref:`Build-U-Boot-label`.
   - Create a FAT32 partition with boot flag enabled on the USB storage device.
   - Copy the bootloader images(MLO,  u-boot.img) into the above created partition.
   - Set the boot mode switches to USB host boot mode (For boot switch details refer to the
     **Initialization/Functional Description/Booting** chapter of TRM.)
   - Connect the USB Mass storage device with the bootloader images and boot up
     the board.
   - The board should now boot to u-boot prompt.

Boot Linux from USB storage
==============================

.. ifconfig:: CONFIG_part_family not in ('AM57X_family')

   Booting Linux from USB storage documentation is pending for |__PART_FAMILY_NAME__|,
   please reach out to:  `Help e2e <https://e2e.ti.com//>`__ for additional information.

.. ifconfig:: CONFIG_part_family in ('AM57X_family')

   To load the Linux Kernel and rootfs from USB rather than a MMC card on
   AMx/DRA7x EVMs, if we assume that the USB device is partitioned the same
   way as an SD/MMC card is, we can utilize the :command:`mmcboot` command
   to boot. To do this, perform the following steps:

   .. code-block:: console

      => usb start
      => setenv mmcroot /dev/sda2 ro
      => run mmcargs
      => run bootcmd_usb

   The USB drivers in Linux kernel need to be built-in (default modules). The
   configuration changes are:

   .. ifconfig:: CONFIG_part_family in ('AM437X_family', 'AM57X_family')

      .. code-block:: Kconfig

         CONFIG_USB=y
         CONFIG_USB_XHCI_HCD=y
         CONFIG_USB_XHCI_PCI=y
         CONFIG_USB_XHCI_PLATFORM=y
         CONFIG_USB_STORAGE=y
         CONFIG_USB_DWC3=y
         CONFIG_USB_DWC3_HOST=y
         CONFIG_USB_DWC3_KEYSTONE=y
         CONFIG_EXTCON=y
         CONFIG_EXTCON_USB_GPIO=y
         CONFIG_SCSI_MOD=y
         CONFIG_SCSI=y
         CONFIG_BLK_DEV_SD=y

   .. ifconfig:: CONFIG_part_family in ('AM35X_family')

      .. code-block:: Kconfig

         CONFIG_USB_MUSB_HDRC=Y
         CONFIG_USB_MUSB_HOST=y
         CONFIG_USB_MUSB_GADGET=n
         CONFIG_USB_MUSB_DUAL_ROLE=Y
         CONFIG_USB_MUSB_TUSB6010=n
         CONFIG_USB_MUSB_OMAP2PLUS=n
         CONFIG_USB_MUSB_AM35X=n
         CONFIG_USB_MUSB_DSPS=Y
         CONFIG_USB_MUSB_UX500=n
         CONFIG_AM335X_PHY_USB=y
         CONFIG_USB_TI_CPPI41_DMA=Y
         CONFIG_MUSB_PIO_ONLY=n

   The USB should have boot partition of FAT32 format, and rootfs partition
   of EXT4 format. The boot partition must contain the following files:

   - Device tree binary (.dtb)
   - Linux kernel image (zImage)

   The rootfs partition contains the filesystem from Processor SDK release package. Extracting
   files to the rootfs parititon should be done as a root user.

   .. code-block:: console

      $ mkdir /mnt/temp
      $ mount -t ext4 /dev/sdb2 /mnt/temp
      $ cd /mnt/temp
      $ tar xvf <Linux_Proc_SDK_Install_DIR>/filesystem/tisdk-default-image-<machine>-evm.tar.xz
      $ cd /mnt
      $ umount temp

   Set up the following u-boot environment variables:

   .. code-block:: console

      => setenv args_all 'setenv bootargs console=ttyS0,115200n8 rootwait'
      => setenv args_usb 'setenv bootargs ${bootargs} rootdelay=3 rootfstype=ext4 root=/dev/sda2 rw'
      => setenv get_fdt_usb 'fatload usb 0:1 ${fdtaddr} ${name_fdt}'
      => setenv get_kern_usb 'fatload usb 0:1 ${loadaddr} ${name_kern}'
      => setenv init_usb 'usb start; run args_all args_usb'
      => setenv boot usb
      => saveenv
      => boot

.. ifconfig:: CONFIG_part_family in ('AM57X_family')

   Booting from SD/eMMC from SPL (Single stage or Falcon mode)
   ===========================================================

   In this boot mode SPL (first stage bootloader) directly boots the Linux
   kernel. Optionally, in order to enter into U-Boot, reset the board while
   keeping 'c' key on the serial terminal pressed. When falcon mode is
   enabled in U-Boot build (usually enabled by default), :file:`MLO` checks if
   there is a valid :file:`uImage` present at a defined offset. If :file:`uImage`
   is present, it is booted directly. If valid :file:`uImage` is not found,
   :file:`MLO` falls back to checking if the :file:`uImage` exists in a FAT
   partition. If it fails, it falls back to booting :file:`u-boot.img`.

   Falcon boot uses :file:`uImage`. To build the kernel :file:`uImage`, you
   will need to keep the U-Boot tool **mkimage** in your **$PATH**.

   .. code-block:: console

      $ make uImage modules dtbs LOADADDR=80008000

   If kernel is not build with **CONFIG_CMDLINE** to set correct bootargs,
   then add the needed **bootargs** in **chosen** node in DTB file, using
   **fdtput** host utility. For example, for DRA74x EVM:

   .. code-block:: console

      => fdtput -v -t s arch/arm/boot/dts/dra7-evm.dtb "/chosen" bootargs "console=ttyO0,115200n8 root=<rootfs>"

   Files: :file:`MLO`, :file:`u-boot.img` (optional), DTB, :file:`uImage`
   are all stored on the same medium, either the SD or the eMMC. There are
   two ways to store the binaries in the SD (resp. eMMC):

   * raw: binaries are stored at fixed offset in the medium
   * fat: binaries are stored as file in a FAT partition

   To flash binaries to SD or eMMC, you can use DFU. For SD boot, from
   u-boot prompt

   .. code-block:: console

      => env default -a; setenv dfu_alt_info ${dfu_alt_info_mmc}; dfu 0 mmc 0

   For eMMC boot, from u-boot prompt

   .. code-block:: console

      => env default -a; setenv dfu_alt_info ${dfu_alt_info_emmc}; dfu 0 mmc 1

   Note: On boards like AM57x GP EVM or BeagleBoard x15, where the second
   USB instance is used as USB client, replace``dfu 0 mmc X`` with ``dfu 1
   mmc X``

   On the host side: binaries in FAT:

   .. code-block:: console

      $ sudo dfu-util -D MLO -a MLO
      $ sudo dfu-util -D u-boot.img -a u-boot.img
      $ sudo dfu-util -D dra7-evm.dtb -a spl-os-args
      $ sudo dfu-util -D uImage -a spl-os-image

   raw binaries:

   .. code-block:: console

      $ sudo dfu-util -D MLO -a MLO.raw
      $ sudo dfu-util -D u-boot.img -a u-boot.img.raw
      $ sudo dfu-util -D dra7-evm.dtb -a spl-os-args.raw
      $ sudo dfu-util -D uImage -a spl-os-image.raw

   If the binaries are files in a fat partition, you need to specify their
   name if they differ from the default values ("uImage" and "args"). Note
   that DFU uses the names "spl-os-image" and "spl-os-args", so this step
   is required in the case of DFU. From u-boot prompt

   .. code-block:: console

      => setenv falcon_image_file spl-os-image
      => setenv falcon_args_file spl-os-args
      => saveenv

   Set the environment variable "boot\_os" to 1. From u-boot prompt

   .. code-block:: console

      => setenv boot_os 1
      => saveenv

   Set the board boot from SD (or eMMC respectively) and reset the EVM. The
   SPL directly boots the kernel image from SD (or eMMC).
