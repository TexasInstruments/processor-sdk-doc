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

Usually in all the platforms there will be two MMC instances of which one
would be SD and the other would be eMMC. The index of them can vary from
one class of platforms to the other. For a given platform, the device
number: **mmcdev=[0:1]** can be found in the following way:

.. code-block:: console

   => mmc list
   sdhci@fa10000: 0 (eMMC)
   sdhci@fa00000: 1 (SD)

The device number "**0**" for eMMC will be needed when flashing to the eMMC device
in: :ref:`flash-and-boot-to-uboot-prompt`.

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

   => mmc dev 0 0 # select eMMC user HW partition (UDA)
   => mmc dev 0 1 # select eMMC boot0 HW partition
   => mmc dev 0 2 # select eMMC boot1 HW partition
   => mmc dev 1 1 # select SD "boot" partition
   => mmc dev 1 2 # select SD "root" partition

View MMC partition contents
===========================

This section assumes an SD card or eMMC was prepared previously to
boot the device.

.. note::

   For eMMC, typically, the device ships without a partition table If there is
   a need to create a partition in UDA (to flash the rootfs), please go to:
   :ref:`create-partitions-in-emmc-uda-from-linux` and format the partition:
   :ref:`formatting-mmc-partition-from-linux` before proceeding to look at the
   eMMC partition contents.

To verify partitions in any MMC device from u-boot prompt, use the
command: :command:`mmc part`.

.. code-block:: console

   => mmc dev 0
   switch to partitions #0, OK
   mmc0(part 0) is current device
   => mmc part

   Partition Map for MMC device 0  --   Partition Type: DOS

   Part   Start Sector    Num Sectors     UUID           Type
    1     2048            31078400        8ece5cfe-01    83

If the partitions are formatted with a file system type that is supported
by u-boot, you can view the contents of the MMC partition as show below:

.. code-block:: console

   => ls mmc 0:1
   <DIR>       4096 .
   <DIR>       4096 ..
   <SYM>          7 bin
   <DIR>       4096 boot
   <DIR>       4096 dev
   <DIR>       4096 etc
   <DIR>       4096 home
   <SYM>          7 lib
   <DIR>       4096 media
   <DIR>       4096 mnt
   <DIR>       4096 opt
   <DIR>       4096 proc
   <DIR>       4096 root
   <DIR>       4096 run
   <SYM>          8 sbin
   <DIR>       4096 srv
   <DIR>       4096 sys
   <DIR>       4096 tmp
   <DIR>       4096 usr
   <DIR>       4096 var
   => ls mmc 0:1 boot/dtb/ti
   <DIR>       4096 .
   <DIR>       4096 ..
              60319 k3-am625-sk.dtb

Where the general syntax is:

.. code-block:: console

   $ ls <interface> [<dev[:partition]> [directory]]

.. _flash-and-boot-to-uboot-prompt:

Flash and boot SPL from eMMC
============================

The K3 based processors supports and recommends booting from the eMMC
boot0/1 HW partitions. In the following example, we use the :command:`fatload`
and :command:`mmc write` commands to load binaries from an SD card and write
them to the eMMC boot0 HW partition:

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. code-block:: console

      => mmc dev 0 1
      => fatload mmc 1 ${loadaddr} tiboot3.bin
      => mmc write ${loadaddr} 0x0 0x800
      => fatload mmc 1 ${loadaddr} tispl.bin
      => mmc write ${loadaddr} 0x800 0x1000
      => fatload mmc 1 ${loadaddr} u-boot.img
      => mmc write ${loadaddr} 0x1800 0x2000

.. ifconfig:: CONFIG_part_variant in ('J7200')

   .. code-block:: console

      => mmc dev 0 1
      => fatload mmc 1 ${loadaddr} tiboot3.bin
      => mmc write ${loadaddr} 0x0 0x800
      => fatload mmc 1 ${loadaddr} tispl.bin
      => mmc write ${loadaddr} 0x800 0x1000
      => fatload mmc 1 ${loadaddr} u-boot.img
      => mmc write ${loadaddr} 0x1800 0x2000

.. ifconfig:: CONFIG_part_variant in ('J721S2', 'AM62X', 'J784S4','J742S2', 'J722S')

   .. code-block:: console

      => mmc dev 0 1
      => fatload mmc 1 ${loadaddr} tiboot3.bin
      => mmc write ${loadaddr} 0x0 0x400
      => fatload mmc 1 ${loadaddr} tispl.bin
      => mmc write ${loadaddr} 0x400 0x1000
      => fatload mmc 1 ${loadaddr} u-boot.img
      => mmc write ${loadaddr} 0x1400 0x2000

.. ifconfig:: CONFIG_part_variant not in ('AM64X', 'J7200', 'J721S2', 'AM62X', 'J784S4','J742S2', 'J722S')

   .. code-block:: console

      => mmc dev 0 1
      => fatload mmc 1 ${loadaddr} tiboot3.bin
      => mmc write ${loadaddr} 0x0 0x400
      => fatload mmc 1 ${loadaddr} tispl.bin
      => mmc write ${loadaddr} 0x400 0x1000
      => fatload mmc 1 ${loadaddr} u-boot.img
      => mmc write ${loadaddr} 0x1400 0x2000
      => fatload mmc 1 ${loadaddr} sysfw.itb
      => mmc write ${loadaddr} 0x3600 0x800

eMMC layout
-----------

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'J7200')

   .. code-block:: text

      +----------------------------------+0x0      +-------------------------+0x0
      |      tiboot3.bin (1 MB)          |         |                         |
      +----------------------------------+0x800    |                         |
      |       tispl.bin (2 MB)           |         |                         |
      +----------------------------------+0x1800   |        rootfs           |
      |       u-boot.img (4 MB)          |         |                         |
      +----------------------------------+0x3800   |                         |
      |      environment (128 KB)        |         |                         |
      +----------------------------------+0x3900   |                         |
      |   backup environment (128 KB)    |         |                         |
      +----------------------------------+0x3A00   +-------------------------+
            boot0 HW partition (8 MB)                     user partition

.. ifconfig:: CONFIG_part_variant in ('J721S2', 'AM62X')

   .. code-block:: text

      +----------------------------------+0x0      +-------------------------+0x0
      |      tiboot3.bin (1 MB)          |         |                         |
      +----------------------------------+0x400    |                         |
      |       tispl.bin (2 MB)           |         |                         |
      +----------------------------------+0x1400   |        rootfs           |
      |       u-boot.img (4 MB)          |         |                         |
      +----------------------------------+0x3400   |                         |
      |      environment (128 KB)        |         |                         |
      +----------------------------------+0x3500   |                         |
      |   backup environment (128 KB)    |         |                         |
      +----------------------------------+0x3600   +-------------------------+
            boot0 HW partition (8 MB)                     user partition

.. ifconfig:: CONFIG_part_variant not in ('AM64X', 'J7200', 'J721S2', 'AM62X')

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
            boot0 HW partition (8 MB)                     user partition

eMMC boot configuration
-----------------------

To boot from any eMMC, the master (ROM) will require some configuration which can be
set using the :command:`mmc bootbus` and :command:`mmc partconf` commands.

- The :command:`mmc bootbus` command sets the BOOT_BUS_WIDTH field where :command:`mmc bootbus 0 2 0 0`
  selects **x8 (sdr/ddr) buswidth in boot operation mode**.
- The :command:`mmc partconf` command can be used to configure what hardware partition
  to boot from. The general syntax is:

.. code-block:: console

   $ mmc partconf <dev> [[varname] | [<boot_ack> <boot_partition> <partition_access>]]

- For more information on these commands, please refer to: `MMC CMD <https://docs.u-boot.org/en/latest/usage/cmd/mmc.html//>`__.

**Boot from boot0 HW partition of eMMC:**

.. code-block:: console

   => mmc partconf 0 1 1 1
   => mmc bootbus 0 2 0 0

**Boot from boot1 HW hardware partition of eMMC:**

.. code-block:: console

   => mmc partconf 0 1 2 1
   => mmc bootbus 0 2 0 0

.. note::

   When booting from boot1 HW partition, make sure to flash the partition using:
   :samp:`mmc dev 0 2`.

**Boot from UDA HW partition of eMMC:**

.. code-block:: console

   => mmc partconf 0 1 7 1
   => mmc bootbus 0 2 0 0

**Enable warm reset**

On eMMC devices, warm reset will not work if EXT_CSD[162] bit is unset since the
reset input signal will be ignored. Warm reset is required to be enabled in order
for the eMMC to be in a "clean state" on power-on reset so that ROM can do a clean
enumeration. To set the EXT_CSD[162] bit, stop at u-boot prompt and execute the
following command:

.. code-block:: console

   => mmc rst-function 0 1

.. warning::

   This is a write-once field. For more information, please refer to the u-boot
   doc: `MMC CMD <https://docs.u-boot.org/en/latest/usage/cmd/mmc.html//>`__.

Boot Linux from eMMC
====================

To flash & boot the rootfs from eMMC UDA HW partition, first prepare UDA:
:ref:`create-partitions-in-emmc-uda-from-linux`. The new software partition then
needs to be formatted as a ext4 filesystem: :ref:`formatting-mmc-partition-from-linux`,
and then the rootfs has to be written. It is not possible to format a partition to ext4
in U-Boot. The Linux kernel image and DT are expected to be present in the /boot folder
of rootfs.

To boot Linux from eMMC, use the following commands after flashing rootfs to UDA:

.. code-block:: console

   => setenv mmcdev 0
   => setenv bootpart 0
   => boot

Flashing an MMC device using USB-DFU
====================================

To flash the eMMC device (boot0 HW partition) using USB-DFU, the device should
be booted to u-boot prompt and a USB cable connected from the host machine
to the device USB port configured to USB peripheral mode.

From u-boot prompt execute the following:

.. code-block:: console

   => setenv dfu_alt_info ${dfu_alt_info_emmc}
   => dfu 0 mmc 0

and on the host machine have the bootloader binaries ready to flash
to eMMC boot0 HW partition. Execute the :command:`dfu-util` to transfer
files to the device. The general syntax for dfu-util command is:

.. code-block:: console

   $ sudo dfu-util -R -a <dfu-target> -D <binary>

To see what are the dfu-targets, on the host machine run: :samp:`sudo dfu-util -l`

.. code-block:: console

   $ sudo dfu-util -l
   dfu-util 0.9
   Found DFU: [0451:6165] ver=0223, devnum=32, cfg=1, intf=0, path="1-10", alt=6, name="sysfw.itb.raw", serial="0000000000000591"
   Found DFU: [0451:6165] ver=0223, devnum=32, cfg=1, intf=0, path="1-10", alt=5, name="u-env.raw", serial="0000000000000591"
   Found DFU: [0451:6165] ver=0223, devnum=32, cfg=1, intf=0, path="1-10", alt=4, name="u-boot.img.raw", serial="0000000000000591"
   Found DFU: [0451:6165] ver=0223, devnum=32, cfg=1, intf=0, path="1-10", alt=3, name="tispl.bin.raw", serial="0000000000000591"
   Found DFU: [0451:6165] ver=0223, devnum=32, cfg=1, intf=0, path="1-10", alt=2, name="tiboot3.bin.raw", serial="0000000000000591"
   Found DFU: [0451:6165] ver=0223, devnum=32, cfg=1, intf=0, path="1-10", alt=1, name="rootfs", serial="0000000000000591"
   Found DFU: [0451:6165] ver=0223, devnum=32, cfg=1, intf=0, path="1-10", alt=0, name="rawemmc", serial="0000000000000591"

Then transfer each desired binary from the host to the device:

- Host:

   .. code-block:: console

      $ sudo dfu-util -R -a tiboot3.bin.raw -D tiboot3.bin

- Device:

   .. code-block:: console

      ##DOWNLOAD ... OK
      Ctrl+C to exit ...

Flashing an SD card from a host PC
==================================

This section assumes that you have flashed an SD card using the
script "create-sdcard.sh" packaged in the installer or have
made a compatible layout manually. In this case, you will need
to copy the boot images:

.. ifconfig:: CONFIG_part_variant in ('AM65X', 'J721E')

   - :file:`tiboot3.bin`
   - :file:`sysfw.itb`
   - :file:`tispl.bin`
   - :file:`u-boot.img`

.. ifconfig:: CONFIG_part_variant not in ('AM65X', 'J721E')

   - :file:`tiboot3.bin`
   - :file:`tispl.bin`
   - :file:`u-boot.img`

to the SD card *boot* partition. At this point, the device can boot to u-boot prompt.

USB
***

.. _uboot-configure-usb-in-host-mode:

Configuring USB in Host Mode
============================

.. ifconfig:: CONFIG_part_variant not in ('J721E', 'J7200', 'J721S2', 'AM64X', 'AM62X', 'AM65X')

   Configuring USB in host mode documentation is pending for |__PART_FAMILY_DEVICE_NAMES__|
   please reach out to:  `Help e2e <https://e2e.ti.com//>`__ for additional information.

.. ifconfig:: CONFIG_part_variant in ('J721E', 'J7200', 'J721S2')

   .. note::

      USB0 instance on J721e/J7200 base board is connected to TypeC port that
      can be used both as host port and device port. By default, USB0 is port
      is configured to be in **peripheral mode**. Since U-Boot does not support
      dynamic switching of USB roles, below DT fragment needs to be applied and
      U-Boot image needs to be rebuilt to make USB0 port to be USB 3.0 host port.

   .. code-block:: diff

      diff --git a/arch/arm/dts/k3-j721e-common-proc-board-u-boot.dtsi b/arch/arm/dts/k3-j721e-common-proc-board-u-boot.dtsi
      index 50effb4812b2..28986c4d2c2a 100644
      --- a/arch/arm/dts/k3-j721e-common-proc-board-u-boot.dtsi
      +++ b/arch/arm/dts/k3-j721e-common-proc-board-u-boot.dtsi
      @@ -184,11 +184,10 @@

       &usbss0 {
              u-boot,dm-spl;
      -       ti,usb2-only;
       };

       &usb0 {
      -       dr_mode = "peripheral";
      +       dr_mode = "host";
              u-boot,dm-spl;
       };


   .. code-block:: diff

      diff --git a/arch/arm/dts/k3-j7200-common-proc-board-u-boot.dtsi b/arch/arm/dts/k3-j7200-common-proc-board-u-boot.dtsi
      index 1b0f5658200f..daa05291b4cc 100644
      --- a/arch/arm/dts/k3-j7200-common-proc-board-u-boot.dtsi
      +++ b/arch/arm/dts/k3-j7200-common-proc-board-u-boot.dtsi
      @@ -155,11 +155,10 @@

       &usbss0 {
              u-boot,dm-spl;
      -       ti,usb2-only;
       };

       &usb0 {
      -       dr_mode = "peripheral";
      +       dr_mode = "host";
              u-boot,dm-spl;
       };

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. note::

      USB instance in AM64 SoC is brought out using a USB 2.0 micro-AB port on the GP
      EVM. This port can be used in both host and device modes. By default in U-Boot,
      peripheral mode is supported. For accessing USB storage devices in U-Boot, dr_mode
      should be set to **host** in the U-Boot dts. The following diff shows the required
      changes to be done. On Starter Kit, USB instance in AM64 SoC is brought out using
      a USB 3.0 Type A port, so the mode is set to **host** by default and the following
      diff would not be required.

   .. code-block:: diff

      diff --git a/arch/arm/dts/k3-am642-evm-u-boot.dtsi b/arch/arm/dts/k3-am642-evm-u-boot.dtsi
      index d066973f89f1..ff8afee09402 100644
      --- a/arch/arm/dts/k3-am642-evm-u-boot.dtsi
      +++ b/arch/arm/dts/k3-am642-evm-u-boot.dtsi
      @@ -55,7 +55,7 @@
      };

       &usb0 {
      -       dr_mode="peripheral";
      +       dr_mode="host";
              u-boot,dm-spl;
       };

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. note::

      There are two instances of USB on AM62 SoC. On the SK board, zeroth instance is
      brought out through a Type C port and the first instance is brought through a Type
      A port. By default, USB0 port is configured to be in **peripheral mode**. Since
      U-Boot does not support dynamic switching of USB roles, below DT fragment needs to
      be applied and U-Boot image needs to be rebuilt to make USB0 port to be USB 2.0
      host port.

   .. code-block:: diff

      diff --git a/arch/arm/dts/k3-am625-sk-u-boot.dtsi b/arch/arm/dts/k3-am625-sk-u-boot.dtsi
      index 20c24d2fa7a4..2b662653023f 100644
      --- a/arch/arm/dts/k3-am625-sk-u-boot.dtsi
      +++ b/arch/arm/dts/k3-am625-sk-u-boot.dtsi
      @@ -117,5 +117,5 @@
       };

       &usb0 {
      -       dr_mode = "peripheral";
      +       dr_mode = "host";
              u-boot,dm-spl;

.. ifconfig:: CONFIG_part_variant in ('AM65X')

   .. note::

      There are two instance of USB on AM654 SoC. The zero instance is not brought out on
      EVM and the first instance is brought using a USB 2.0 micro-AB port on the EVM. By
      default in U-Boot, peripheral mode is supported. For accessing USB storage devices in
      U-Boot, dr_mode should be set to "host" in the U-Boot device tree file. The following
      diff shows the required changes to be done.

   .. code-block:: diff

      diff --git a/arch/arm/dts/k3-am654-base-board-u-boot.dtsi b/arch/arm/dts/k3-am654-base-board-u-boot.dtsi
      index fd8f88bd3451..a754400ca122 100644
      --- a/arch/arm/dts/k3-am654-base-board-u-boot.dtsi
      +++ b/arch/arm/dts/k3-am654-base-board-u-boot.dtsi
      @@ -108,5 +108,9 @@
                     <&mcu_udmap 0x4303>; /* mgmnt rsp slice 1 */
       };

      +&usb1 {
      +       dr_mode = "host";
      +};
      +
       /* Disable ICSSG2 EMAC1 */
       /delete-node/ &icssg2_emac1;

.. ifconfig:: CONFIG_part_variant in ('J721E', 'J7200', 'J721S2', 'AM64X', 'AM62X', 'AM65X')

   Loading images from USB storage
   ===============================

   For loading images from a FAT partition on a different media than mmc, replace
   the :command:`mmc` command with the required media. For example, to load images
   from a FAT partition on a USB storage device connected to the zeroth instance
   of USB:

   .. code-block:: console

      => fatload usb 0 ${loadaddr} <file name>

.. _uboot-usb-msc-boot:

Flash and boot SPL from USB storage
===================================

.. ifconfig:: CONFIG_part_variant not in ('J7200', 'J721E', 'AM64X', 'AM65X', 'J722S')

   Boot SPL from USB storage documentation is pending for |__PART_FAMILY_DEVICE_NAMES__|
   please reach out to:  `Help e2e <https://e2e.ti.com//>`__ for additional information.

.. ifconfig:: CONFIG_part_variant in ('J7200', 'J721E')

   .. note::

      The SoC does not support booting from USB mass storage, but USB can still be
      accesed as storage device at U-Boot prompt.

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'AM65X', 'J722S')

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      Booting to U-Boot prompt from USB storage is supported. The following are the
      steps to be followed:

      - Build the bootloader images using default "am64x_evm_r5_defconfig" and
        "am64x_evm_a53_defconfig" configs files. For instructions to build the
        bootloader images please refer to :ref:`Build-U-Boot-label`.
      - Create a FAT32 partition with boot flag enabled on the USB storage device.
      - Copy the bootloader images(tiboot3.bin, tispl.bin, u-boot.img) into the
        above created partition.
      - Set the boot mode switches to usb host mode (For boot switch details refer to the
        **Initialization/Boot Mode Pins** chapter of TRM.)
      - Connect the USB Mass storage device with the bootloader images and boot up
        the board.
      - The board should now boot to u-boot prompt.

   .. ifconfig:: CONFIG_part_variant in ('AM65X')

      Booting to U-Boot prompt from USB storage is supported. The following are the
      steps to be followed:

      - Build the bootloader images using the "am65x_evm_r5_usbmsc_defconfig"
        and "am65x_evm_a53_defconfig" configs files. For instructions to build the
        bootloader images please refer to :ref:`Build-U-Boot-label`.
      - Create a FAT32 partition with boot flag enabled on the USB storage device.
      - Copy the bootloader images(tiboot3.bin, sysfw.itb, tispl.bin, u-boot.img)
        into the above created partition.
      - Set the boot mode switches to usb host mode (For boot switch details refer to the
        **Initialization/Boot Mode Pins** chapter of TRM.)
      - Connect the USB Mass storage device with the bootloader images and boot up
        the board.
      - The board should now boot to u-boot prompt.

   .. ifconfig:: CONFIG_part_variant in ('J722S')

      Booting to U-Boot prompt from USB storage is supported. The following are the
      steps to be followed:

      - In U-Boot the USB controller can be used in either host or peripheral mode.
        For booting to linux kernel from USB storage device, the USB port should be
        in host mode.
      - By default, USB0 is set to peripheral mode. Change this from peripheral to
        host mode.
      - Build the bootloader images using the default "j722s_evm_r5_defconfig" and
        the config fragment "j722s_evm_r5_usbmsc.config" and "j722s_evm_a53_defconfig"
        configs files. The configs required for USB MSC boot are already enabled. For
        instructions to build the bootloader images please refer to :ref:`Build-U-Boot-label`.
      - Create a FAT32 partition with boot flag enabled on the USB storage device.
      - Copy the bootloader images(tiboot3.bin, tispl.bin, u-boot.img) into the above
        created partition.
      - Set the boot mode switches to USB host boot mode (Refer to the **Initialization**
        chapter of TRM for boot switch details)
      - Make sure USB0 port in DRP mode: SW2[2:3] = 00
      - Connect the USB Mass storage device with the bootloader images and boot up
        the board.

   .. note::

      While using :samp:`usb reset` or :samp:`usb start` commands in U-Boot, or
      booting from a USB Mass storage device, some of the USB devices fail to get
      detected. This issue is seen because these USB devices are failing to follow the
      spec for power good delay. It can be resolved by overriding the **power good delay**
      using the environment variable **usb_pgood_delay**, setting it to 2000 should be
      good enough for all cases.

Boot Linux from USB storage
==============================

.. ifconfig:: CONFIG_part_family not in ('J7_family', 'AM62X_family', 'AM64X_family')

   Booting Linux from USB storage documentation is pending for |__PART_FAMILY_DEVICE_NAMES__|
   please reach out to:  `Help e2e <https://e2e.ti.com//>`__ for additional information.

.. ifconfig:: CONFIG_part_family in ('J7_family')

   .. ifconfig:: CONFIG_part_variant not in ('J722S')

      This feature is currently not supported.

   .. ifconfig:: CONFIG_part_variant in ('J722S')

      To load the Linux kernel, Device Tree and the root file system from USB
      mass storage device, the following changes are required to be done:

      - U-Boot

         - In U-Boot, the USB controller can be used in either host or peripheral
           mode. For booting to linux prompt. For USB storage device, the USB port has
           to be set as host. By default, USB0 is set to peripheral mode. Change this
           from peripheral to host mode in u-boot DT.

      - Linux

         - In Linux, by default the USB subsystem is built as modules. For booting
           from USB mass storage device, the USB subsytem is required to be built into
           the image. This can be done by making the following changes in the
           configuration used for building kernel:

         .. code-block:: Kconfig

            CONFIG_USB_COMMON=y
            CONFIG_USB=y
            CONFIG_USB_XHCI_HCD=y
            CONFIG_USB_XHCI_PCI=y
            CONFIG_USB_XHCI_PLATFORM=y
            CONFIG_USB_STORAGE=y
            CONFIG_USB_DWC3=y
            CONFIG_USB_DWC3_AM62=y
            CONFIG_USB_GADGET=y
            CONFIG_TYPEC=y
            CONFIG_TYPEC_TPS6598X=y
            CONFIG_USB_ROLE_SWITCH=y

      **Copying the images to USB storage device**

      - After making the required changes mentioned above, build the kernel,
        device tree file and modules. The USB Mass storage device should have the
        rootfs in the second partition with ext4 file system. The following images
        should be in /boot/ directory:

         - Linux kernel **Image**
         - Device tree (dtb) file

      **Run usb_boot**

      - During the boot, cancel the autoboot at U-Boot and run the following command
        at u-boot prompt:

         .. code-block:: console

            => run usb_boot

.. ifconfig:: CONFIG_part_family in ('AM62X_family')

   To load the Linux kernel, Device Tree and the Root file system from USB Mass storage
   device, the following changes are required to be done:

   - U-Boot

      - In U-Boot the USB controller can be used in either host or peripheral mode. For
        booting to linux kernel from USB storage device, the USB port is to be set as host.
      - By default, on AM625-SK board the zero instance of USB connected to the Type C
        port, is set to peripheral mode and the first instance of USB connected to the Type
        A port is set to host mode.
      - Therefore, USB controller needs to be set host mode and custom bootloader images
        are required to be built, if zeroth instance is used. Please refer to note in section
        :ref:`uboot-configure-usb-in-host-mode`

   - Linux

      - In Linux, by default the USB subsystem is built as modules. For booting from USB
        mass storage device, USB subsytem is required to be built into the image. This can be
        done by making the following changes in the configuration used for building kernel:

      .. code-block:: Kconfig

         CONFIG_USB_COMMON=y
         CONFIG_USB=y
         CONFIG_USB_XHCI_HCD=y
         CONFIG_USB_XHCI_PCI=y
         CONFIG_USB_XHCI_PLATFORM=y
         CONFIG_USB_STORAGE=y
         CONFIG_USB_DWC3=y
         CONFIG_USB_DWC3_AM62=y
         CONFIG_USB_GADGET=y
         CONFIG_TYPEC=y
         CONFIG_TYPEC_TPS6598X=y
         CONFIG_USB_ROLE_SWITCH=y

   **Copying the images to USB storage device**

      - After making the required changes mentioned above, build the kernel, device tree
        file and modules.
      - The USB Mass storage device should have the rootfs as the second
        partition with ext4 file system. The following images should be in /boot/ directory:

         #. Linux kernel **Image**
         #. Device tree (dtb) file

   **Run usbboot**

      - During boot, cancel the autoboot at U-Boot and run the following command at u-boot
        prompt:

         .. code-block:: console

            => run usbboot

.. ifconfig:: CONFIG_part_family in ('AM64X_family')

   To load the Linux kernel, Device Tree and the Root file system from USB Mass storage
   device, the following changes are required to be done:

   - U-Boot

      - In U-Boot the USB controller can be used in either host or peripheral mode. For
        booting to linux kernel from USB storage device, the USB port is to be set as host.
      - By default, the USB controller is set in peripheral mode.
      - If the boot media used to boot to U-Boot is USB Host mode(:ref:`uboot-usb-msc-boot`)
        then, the USB controller is set to host mode during runtime. Therefore, no changes
        would be required in this case.
      - If a boot media other than USB Host is used, the USB controller needs to be set
        host mode and custom bootloader images are required to be built. Please refer to note
        in section :ref:`uboot-configure-usb-in-host-mode`

   - Linux

      - In Linux, by default the USB subsystem is built as modules. For booting from USB
        mass storage device, USB subsytem is required to be built into the image. This can be
        done by making the following changes in the configuration used for building kernel:

      .. code-block:: Kconfig

         CONFIG_USB=y
         CONFIG_USB_XHCI_HCD=y
         CONFIG_USB_XHCI_PLATFORM=y
         CONFIG_USB_STORAGE=y
         CONFIG_USB_GADGET=y
         CONFIG_USB_CDNS3=y
         CONFIG_USB_CDNS3_GADGET=y
         CONFIG_USB_CDNS3_HOST=y
         CONFIG_USB_CDNS3_TI=y

      **Copying the images to USB storage device**

      - After making the required changes mentioned above, build the kernel, device tree
        file and modules. The USB Mass storage device should have two partitions:

      - boot
         - For creating this parition please refer :ref:`uboot-usb-msc-boot`
      - rootfs
         - A partition with ext4 filesystem and the following images in /boot/ directory
            - Linux kernel **Image**
            - Device tree (dtb) file

      **Run usbboot**

      - During boot, cancel the autoboot at U-Boot and run the following command at u-boot
        prompt:

         .. code-block:: console

            => run usbboot

Steps for working around SD card issues in u-boot
=================================================

In some cases, issues can be seen while using some SD cards, like:

- Error while trying to initialize:

   .. code-block:: console

      U-Boot SPL 2021.01-g74fc69c889 (May 19 2022 - 02:44:29 +0000)
      SYSFW ABI: 3.1 (firmware rev 0x0008 '8.3.2--v08.03.02 (Jolly Jellyfi')
      Trying to boot from MMC2
      spl: mmc init failed with error: -110
      SPL: failed to boot from all boot devices
      ### ERROR ### Please RESET the board ###

Given below are the list of various workarounds that can be done in the
device tree MMC node to get SD card working. The workarounds are ordered in
increasing order of reducing performance.

.. note::

   All the  mentioned below, are to be done in the MMC device tree node
   corresponding to the SD instance. This is usually the first (index starting
   from zero) instance.

#. Restricting to a given speed mode

   By default the U-Boot driver tries to enumerate a SD card in the highest
   supported speed mode. Given below is the order in which the driver tries
   to enumerate a SD card:

   - SDR104
   - SDR50
   - DDR50
   - SD HS
   - SD legacy

   The **sdhci-caps-mask** can be added to the DT node to cap at a specific mode:

   - Limit to DDR50: ``sdhci-caps-mask = <0x00000003 0x00000000>``
   - Limit to SD HS: ``sdhci-caps-mask = <0x00000007 0x00000000>``
   - Limit to SD legacy: ``sdhci-caps-mask = <0x00000007 0x00200000>``

   .. code-block:: dts

      &sdhci1 {
         /* SD/MMC */
         vmmc-supply = <&vdd_mmc1>;
         vqmmc-supply = <&vdd_sd_dv>;
         pinctrl-names = "default";
         pinctrl-0 = <&main_mmc1_pins_default>;
         ti,driver-strength-ohm = <50>;
         disable-wp;
         sdhci-caps-mask = <0x00000003 0x00000000>; /* Limiting to DDR50 speed mode */
      };

#. Increase power cycle period

   Increasing the delay while power cycling the SD card. This can be done
   by increasing the delay value in the diff indicated below,

   .. code-block:: diff

      diff --git a/drivers/mmc/mmc.c b/drivers/mmc/mmc.c
      index f486e2a2c364..38cc956b3d53 100644
      --- a/drivers/mmc/mmc.c
      +++ b/drivers/mmc/mmc.c
      @@ -2761,7 +2761,7 @@ static int mmc_power_cycle(struct mmc *mmc)
               * SD spec recommends at least 1ms of delay. Let's wait for 2ms
               * to be on the safer side.
               */
      -       udelay(2000);
      +       udelay(4000);
            return mmc_power_on(mmc);
      }

#. Reduce the bus width

   The SD interface supports a bus width of 4. It can be reduced to 1 by
   changing the **bus-width** device tree property from 4 to 1.

   .. code-block:: diff

      diff --git a/arch/arm/dts/k3-am62-main.dtsi b/arch/arm/dts/k3-am62-main.dtsi
      index c06ec7355035..4ab29b6aa4b7 100644
      --- a/arch/arm/dts/k3-am62-main.dtsi
      +++ b/arch/arm/dts/k3-am62-main.dtsi
      @@ -373,7 +373,7 @@
                     ti,itap-del-sel-sdr12 = <0x0>;
                     ti,itap-del-sel-sdr25 = <0x0>;
                     ti,clkbuf-sel = <0x7>;
      -               bus-width = <4>;
      +               bus-width = <1>;
      };

      sdhci2: mmc@fa20000 {
