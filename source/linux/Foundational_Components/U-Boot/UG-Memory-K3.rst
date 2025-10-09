SD, eMMC and USB
################

.. ifconfig:: CONFIG_part_family in ('AM62X_family', 'AM62PX_family')

   .. warning::

      There is important information on multimedia card (MMC) support for |__PART_FAMILY_DEVICE_NAMES__| device, go
      :ref:`here <uboot-mmc-support>` for more information.

Overview
********

The following guide shows how to flash and boot from storage media such as the embedded multimedia
card (eMMC), secure digital (SD) card, and USB storage devices. While this is a step-by-step guide,
it is in no way extensive and does not cover all the per-platform corner-cases.
For any  issues or questions on this guide, reach out to: `Help e2e <https://e2e.ti.com//>`__.

MMC
***

.. _uboot-listing-mmc-devices:

Listing MMC devices
===================

Usually in all the platforms there will be two multimedia card (MMC) instances of which one
would be SD and the other would be eMMC. The device index of them can vary from
one class of platforms to the other. For a given platform, the device index
can be found in the following way:

.. code-block:: console

   => mmc list
   sdhci@fa10000: 0 (eMMC)
   sdhci@fa00000: 1 (SD)

The device index "**0**" for eMMC will be used when flashing to the eMMC device
:ref:`here <how-to-emmc-boot>` using :command:`mmc dev` command.

In u-boot environment, usually **mmcdev=n** is used to select which MMC device to boot
Linux from, where **n** is the device index.

MMC HW partitions
=================

This sections includes a summary of MMC hardware partitions.

**eMMC**

   Normally eMMC is divided into 4 areas (also known as HW partitions):

   - User data area (UDA): Used to store user data such as a file system. This partition can divided into disk partitions
   - Boot0/1: Used to store firmware and data needed during boot
   - Replay protected memory block (RPMB) : Used to store secure data

**SD**

   SD card memory is not divided into sections such as eMMC, but acts like UDA in eMMC where user can
   create disk partitions in software allowing to divide the storage space into multiple sections.

.. _uboot-selecting-mmc-device-and-partitions:

Selecting MMC device and partitions
===================================

To select an MMC device in u-boot, the command: :command:`mmc dev` could be used.
The general syntax is:

.. code-block:: console

   => mmc dev [dev] [partition]

Where [dev] is the MMC device index.

The following lists examples and their explanation for each MMC device
and partitions according to the example :ref:`here <uboot-listing-mmc-devices>`.

.. code-block:: console

   => mmc dev 0 0 # select eMMC UDA
   => mmc dev 0 1 # select eMMC Boot0
   => mmc dev 0 2 # select eMMC Boot1
   => mmc dev 1 # select SD

View MMC partition contents
===========================

This section assumes an SD card or eMMC was prepared previously to
boot the device.

.. note::

   For eMMC, typically, the device ships without a partition table If there is a need to
   create a partition in UDA, go :ref:`here <mmc-create-partitions-in-emmc-linux>`
   and to format the partition go :ref:`here <mmc-format-partition-linux>` before
   proceeding.

To list disk partitions for any MMC device from u-boot prompt, use the
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

MMC supported boot modes
========================

The K3 based processors support and recommends using *eMMC boot* from Boot0 or Boot1. For complete
information on the MMC boot modes supported by ROM, refer to the device specific TRM,
under: :file:`Initialization/Boot Mode Pins`. ROM supports the following two MMC boot modes:

**eMMC boot**

   This boot mode is a special boot mode specific to eMMC device. In this boot mode, ROM cannot
   boot from SD and can only boot from Boot0 or Boot1 in eMMC. Go :ref:`here <how-to-emmc-boot>`
   for a step-by-step guide to boot with this boot mode.

**MMCSD boot**

   This boot mode allows to boot from either eMMC or SD device. With this boot mode, ROM can
   only boot from SD card or UDA in eMMC. ROM allows to boot in raw or filesystem (FS) mode, FS mode being
   the recommended option and therefore will have a subsequent guide to boot using this mode. Configuration
   for selecting MMC device and raw/FS mode, is done with boot mode pins, refer to TRM for this
   setup. To boot from eMMC UDA in FS mode, go :ref:`here <how-to-mmcsd-boot-from-emmc-uda>`.

Flashing an MMC device using USB-DFU
====================================

To flash the eMMC device (Boot0) using USB-DFU, the device should
be booted to u-boot prompt and a USB cable connected from the host machine
to the device USB port configured to USB peripheral mode.

From u-boot prompt enter the following:

.. code-block:: console

   => setenv dfu_alt_info ${dfu_alt_info_emmc}
   => dfu 0 mmc 0

This command assumes eMMC device exists and is MMC device 0.

On the host machine have the boot loader binaries ready to flash
to eMMC Boot0. Run the :command:`dfu-util` to transfer
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

Then transfer each binary from the host to the device:

- Host:

   .. code-block:: console

      $ sudo dfu-util -R -a tiboot3.bin.raw -D tiboot3.bin
      $ sudo dfu-util -R -a tispl.bin.raw -D tispl.bin
      $ sudo dfu-util -R -a u-boot.img.raw -D u-boot.img

- Device:

   .. code-block:: console

      ##DOWNLOAD ... OK
      Ctrl+C to exit ...
      ##DOWNLOAD ... OK
      Ctrl+C to exit ...
      ##DOWNLOAD ... OK
      Ctrl+C to exit ...

Flashing an SD card from a host PC
==================================

This section assumes that you have flashed an SD card by using the
script "create-sdcard.sh" packaged in the installation program or have
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
   reach out to:  `Help e2e <https://e2e.ti.com//>`__ for additional information.

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

   For loading images from a FAT partition on a different media than MMC, replace
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
   reach out to:  `Help e2e <https://e2e.ti.com//>`__ for additional information.

.. ifconfig:: CONFIG_part_variant in ('J7200', 'J721E')

   .. note::

      The SoC does not support booting from USB mass storage, but USB can still be
      accessed as storage device at U-Boot prompt.

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'AM65X', 'J722S')

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      Booting to U-Boot prompt from USB storage is supported. The following are the
      steps to be followed:

      - Build the boot loader images using default "am64x_evm_r5_defconfig" and
        "am64x_evm_a53_defconfig" configs files. For instructions to build the
        boot loader images, refer to :ref:`Build-U-Boot-label`.
      - Create a FAT32 partition with boot flag enabled on the USB storage device.
      - Copy the boot loader images(tiboot3.bin, tispl.bin, u-boot.img) into the
        above created partition.
      - Set the boot mode switches to usb host mode (For boot switch details refer to the
        **Initialization/Boot Mode Pins** chapter of TRM.)
      - Connect the USB Mass storage device with the boot loader images and boot up
        the board.
      - The board should now boot to u-boot prompt.

   .. ifconfig:: CONFIG_part_variant in ('AM65X')

      Booting to U-Boot prompt from USB storage is supported. The following are the
      steps to be followed:

      - Build the boot loader images using the "am65x_evm_r5_usbmsc_defconfig"
        and "am65x_evm_a53_defconfig" configs files. For instructions to build the
        boot loader images, refer to :ref:`Build-U-Boot-label`.
      - Create a FAT32 partition with boot flag enabled on the USB storage device.
      - Copy the boot loader images(tiboot3.bin, sysfw.itb, tispl.bin, u-boot.img)
        into the above created partition.
      - Set the boot mode switches to usb host mode (For boot switch details refer to the
        **Initialization/Boot Mode Pins** chapter of TRM.)
      - Connect the USB Mass storage device with the boot loader images and boot up
        the board.
      - The board should now boot to u-boot prompt.

   .. ifconfig:: CONFIG_part_variant in ('J722S')

      Booting to U-Boot prompt from USB storage is supported. The following are the
      steps to be followed:

      - In U-Boot the USB controller can be used in either host or peripheral mode.
        For booting to Linux kernel from USB storage device, the USB port should be
        in host mode.
      - By default, USB0 is set to peripheral mode. Change this from peripheral to
        host mode.
      - Build the boot loader images using the default "j722s_evm_r5_defconfig" and
        the config fragment "j722s_evm_r5_usbmsc.config" and "j722s_evm_a53_defconfig"
        configs files. The configs required for USB MSC boot are already enabled. For
        instructions to build the boot loader images, refer to :ref:`Build-U-Boot-label`.
      - Create a FAT32 partition with boot flag enabled on the USB storage device.
      - Copy the boot loader images(tiboot3.bin, tispl.bin, u-boot.img) into the above
        created partition.
      - Set the boot mode switches to USB host boot mode (Refer to the **Initialization**
        chapter of TRM for boot switch details)
      - Make sure USB0 port in DRP mode: SW2[2:3] = 00
      - Connect the USB Mass storage device with the boot loader images and boot up
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

   Booting Linux from USB storage documentation is pending for |__PART_FAMILY_DEVICE_NAMES__|,
   reach out to:  `Help e2e <https://e2e.ti.com//>`__ for additional information.

.. ifconfig:: CONFIG_part_family in ('J7_family')

   .. ifconfig:: CONFIG_part_variant not in ('J722S')

      This feature is currently not supported.

   .. ifconfig:: CONFIG_part_variant in ('J722S')

      To load the Linux kernel, Device Tree and the root file system from USB
      mass storage device, the following changes are required to be done:

      - U-Boot

         - In U-Boot, the USB controller can be used in either host or peripheral
           mode. For booting to Linux prompt. For USB storage device, the USB port has
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
        booting to Linux kernel from USB storage device, the USB port is to be set as host.
      - By default, on AM625-SK board the zero instance of USB connected to the Type C
        port, is set to peripheral mode and the first instance of USB connected to the Type
        A port is set to host mode.
      - Therefore, USB controller needs to be set host mode and custom boot loader images
        are required to be built, if zeroth instance is used. Refer to note in section
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
        booting to Linux kernel from USB storage device, the USB port is to be set as host.
      - By default, the USB controller is set in peripheral mode.
      - If the boot media used to boot to U-Boot is USB Host mode(:ref:`uboot-usb-msc-boot`)
        then, the USB controller is set to host mode during runtime. Therefore, no changes
        would be required in this case.
      - If a boot media other than USB Host is used, the USB controller needs to be set
        host mode and custom boot loader images are required to be built. Refer to note
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
         - For creating this parition, refer to :ref:`uboot-usb-msc-boot`
      - rootfs
         - A partition with ext4 filesystem and the following images in /boot/ directory
            - Linux kernel **Image**
            - Device tree (dtb) file

      **Run usbboot**

      - During boot, cancel the autoboot at U-Boot and run the following command at u-boot
        prompt:

         .. code-block:: console

            => run usbboot

|

.. _uboot-mmc-support:

MMC support in u-boot
=====================

.. ifconfig:: CONFIG_part_family in ('AM62PX_family')

   **eMMC HS400 support**

   - For 11.1.1 SDK, only am62px SR1.2 supports eMMC HS400 mode, all earlier silicon revisions
     only support up to eMMC HS200 mode. Logic to determine eMMC mode is abstracted away in host
     driver and depends on silicon revision parsing.

   - For 11.0 and 11.1 SDK, am62px device does not support eMMC HS400 mode due to errata `i2458 <https://www.ti.com/lit/pdf/sprz574>`__.
     If support for HS400 is required, add the following to k3-am62p-j722s-common-main.dtsi:

      .. code-block:: diff

         diff --git a/dts/upstream/src/arm64/ti/k3-am62p-j722s-common-main.dtsi b/dts/upstream/src/arm64/ti/k3-am62p-j722s-common-main.dtsi
         index 8bfc6539b2a..8a536b081e1 100644
         --- a/dts/upstream/src/arm64/ti/k3-am62p-j722s-common-main.dtsi
         +++ b/dts/upstream/src/arm64/ti/k3-am62p-j722s-common-main.dtsi
         @@ -593,12 +593,16 @@
                        bus-width = <8>;
                        mmc-ddr-1_8v;
                        mmc-hs200-1_8v;
         +               mmc-hs400-1_8v;
                        ti,clkbuf-sel = <0x7>;
         +               ti,strobe-sel = <0x55>;
                        ti,trm-icp = <0x8>;
                        ti,otap-del-sel-legacy = <0x1>;
                        ti,otap-del-sel-mmc-hs = <0x1>;
                        ti,otap-del-sel-ddr52 = <0x6>;
                        ti,otap-del-sel-hs200 = <0x8>;
         +               ti,otap-del-sel-hs400 = <0x5>; // at 0.85V VDD_CORE
         +               //ti,otap-del-sel-hs400 = <0x7>; // at 0.75V VDD_CORE
                        ti,itap-del-sel-legacy = <0x10>;
                        ti,itap-del-sel-mmc-hs = <0xa>;
                        ti,itap-del-sel-ddr52 = <0x3>;

      and enable the following config options:

      .. code-block:: diff

         diff --git a/configs/am62px_evm_a53_defconfig b/configs/am62px_evm_a53_defconfig
         index 09a91248ce6..f95879f41c9 100644
         --- a/configs/am62px_evm_a53_defconfig
         +++ b/configs/am62px_evm_a53_defconfig
         @@ -114,8 +114,8 @@ CONFIG_MMC_IO_VOLTAGE=y
         CONFIG_SPL_MMC_IO_VOLTAGE=y
         CONFIG_MMC_UHS_SUPPORT=y
         CONFIG_SPL_MMC_UHS_SUPPORT=y
         -CONFIG_MMC_HS200_SUPPORT=y
         -CONFIG_SPL_MMC_HS200_SUPPORT=y
         +CONFIG_MMC_HS400_SUPPORT=y
         +CONFIG_SPL_MMC_HS400_SUPPORT=y
         CONFIG_MMC_SDHCI=y
         CONFIG_MMC_SDHCI_ADMA=y
         CONFIG_SPL_MMC_SDHCI_ADMA=y

.. ifconfig:: CONFIG_part_family in ('AM62X_family')

   **Missing eMMC support**

   Support for eMMC is missing for AM62SIP SK in Processor SDK 11.01. Therefore, eMMC boot, reading/writting/accessing the eMMC
   will not work on AM62SIP SK. If eMMC support is required, apply the following diff to k3-am6254xxl-sk.dts:

   .. code-block:: diff

      diff --git a/dts/upstream/src/arm64/ti/k3-am6254xxl-sk.dts b/dts/upstream/src/arm64/ti/k3-am6254xxl-sk.dts
      index 060df318b3f..d2c9f226b73 100644
      --- a/dts/upstream/src/arm64/ti/k3-am6254xxl-sk.dts
      +++ b/dts/upstream/src/arm64/ti/k3-am6254xxl-sk.dts
      @@ -42,6 +42,22 @@
      };

      &main_pmx0 {
      +       main_mmc0_pins_default: main-mmc0-default-pins {
      +               bootph-all;
      +               pinctrl-single,pins = <
      +                       AM62X_IOPAD(0x220, PIN_INPUT, 0) /* (Y3) MMC0_CMD */
      +                       AM62X_IOPAD(0x218, PIN_INPUT, 0) /* (AB1) MMC0_CLK */
      +                       AM62X_IOPAD(0x214, PIN_INPUT, 0) /* (AA2) MMC0_DAT0 */
      +                       AM62X_IOPAD(0x210, PIN_INPUT_PULLUP, 0) /* (AA1) MMC0_DAT1 */
      +                       AM62X_IOPAD(0x20c, PIN_INPUT_PULLUP, 0) /* (AA3) MMC0_DAT2 */
      +                       AM62X_IOPAD(0x208, PIN_INPUT_PULLUP, 0) /* (Y4) MMC0_DAT3 */
      +                       AM62X_IOPAD(0x204, PIN_INPUT_PULLUP, 0) /* (AB2) MMC0_DAT4 */
      +                       AM62X_IOPAD(0x200, PIN_INPUT_PULLUP, 0) /* (AC1) MMC0_DAT5 */
      +                       AM62X_IOPAD(0x1fc, PIN_INPUT_PULLUP, 0) /* (AD2) MMC0_DAT6 */
      +                       AM62X_IOPAD(0x1f8, PIN_INPUT_PULLUP, 0) /* (AC2) MMC0_DAT7 */
      +               >;
      +       };
      +
            main_rgmii2_pins_default: main-rgmii2-default-pins {
                     bootph-all;
                     pinctrl-single,pins = <
      @@ -147,6 +163,14 @@
            };
      };

      +&sdhci0 {
      +       bootph-all;
      +       status = "okay";
      +       pinctrl-names = "default";
      +       pinctrl-0 = <&main_mmc0_pins_default>;
      +};
      +
      &sdhci1 {
            vmmc-supply = <&vdd_mmc1>;
            vqmmc-supply = <&vdd_sd_dv>;

.. ifconfig:: CONFIG_part_family not in ('AM62X_family', 'AM62PX_family')

   There is no missing MMC support for |__PART_FAMILY_DEVICE_NAMES__| device.

|

Steps for working around SD card issues in u-boot
=================================================

In some cases, issues can be seen while using some SD cards, such as:

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
