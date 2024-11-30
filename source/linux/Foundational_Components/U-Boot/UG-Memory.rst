SD, eMMC and USB
----------------

The commands for using SD cards, eMMC flash and USB mass storage devices
(hard drives, flash drives, card readers, etc) are all very similar. The
biggest difference is that on some hardware we may not be able to run
U-Boot out of ROM from the storage device as it is unsupported. Once
U-Boot is running however, any of these may be used for the kernel and
the root filesystem.

Usually in all the platforms there will be two MMC instances of which one
would be SD and the other would be eMMC. The index of them can vary from
one class of platforms to the other. For a given platform, the device
number (device num) can be found in the following way,

.. code-block:: console

     U-Boot# mmc list
     sdhci@fa10000: 0 (eMMC)
     sdhci@fa00000: 1 (SD)

.. _partitioning-eMMC-from-uboot:

Partitioning eMMC from U-Boot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The eMMC device typically ships without any partition table. We make use
of the GPT support in U-Boot to write a GPT partition table to eMMC. In
this case we need to use the **uuidgen** program on the host to create
the UUIDs used for the disk and each partition.

.. code-block:: console

    $ uuidgen
    ...first uuid...
    $ uuidgen
    ...second uuid...

.. code-block:: console

    U-Boot # printenv partitions
    uuid_disk=${uuid_gpt_disk};name=rootfs,start=2MiB,size=-,uuid=${uuid_gpt_rootfs}
    U-Boot # setenv uuid_gpt_disk ...first uuid...
    U-Boot # setenv uuid_gpt_rootfs ...second uuid...
    U-Boot # gpt write mmc <device num> ${partitions} /* <device num> is device index obtained from mmc list for eMMC */

A reset is required for the partition table to be visible.

Updating an SD card from a host PC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section assume that you have created an SD card using the
script "create-sdcard.sh" packaged inside the installer or have
made a compatible layout by hand. In this case, you will need to copy
the all the boot images (**MLO** and **u-boot.img** for 32-bit platforms,
**tiboot3.bin**, **sysfw.itb**, **tispl.bin**, **u-boot.img** for K3 based platforms,
except AM64x and J7200 in which **sysfw.itb** is already combined with **tiboot3.bin**)
files to the *boot* partition. At this point, the card is now bootable in the SD card slot.
We default to using **/boot/${bootfile}** on the *rootfs* partition and the device tree file
loaded from **/boot** with the same name as in the kernel.

.. ifconfig:: CONFIG_part_family in ('GEN')

    However, if you are using OMAP-L138 based board (like the LCDK), then
    you need to write the generated ``u-boot.ais`` image to the SD card
    using ``dd`` command.

    .. code-block:: console

        $ sudo dd if=u-boot.ais of=/dev/sd<N> seek=117 bs=512 conv=fsync

Updating an SD card or eMMC using DFU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To see the list of available places to write to (in DFU terms,
altsettings) use the **mmc part** command to list the partitions on the
MMC device and **printenv dfu\_alt\_settings\_mmc** or
**dfu\_alt\_settings\_emmc** to see how they are mapped and exposed to
**dfu-util**.

.. code-block:: console

    U-Boot# mmc part

    Partition Map for MMC device 0  --   Partition Type: DOS

    Partition     Start Sector     Num Sectors     Type
        1                   63          144522       c Boot
        2               160650         1847475      83
        3              2024190         1815345      83
    U-Boot# printenv dfu_alt_info_mmc
    dfu_alt_info=boot part 0 1;rootfs part 0 2;MLO fat 0 1;u-boot.img fat 0 1;uEnv.txt fat 0 1"

.. note::
	The above command mmc part lists the partitions in the current
	selected device. So, to list the partitions in eMMC or SD one needs to
	switch to the required device by using the command ``mmc dev <device
	num>``.

This means that you can tell dfu-util to write anything to any of:

-  boot
-  rootfs
-  MLO
-  u-boot.img
-  uEnv.txt

And that the **MLO**, **u-boot.img** and **uEnv.txt** files are to be
written to a FAT filesystem.

To start DFU on the target on the first MMC device:

.. code-block:: console

    U-Boot # setenv dfu_alt_info ${dfu_alt_info_mmc}
    U-Boot # dfu 0 mmc 0

On boards like AM57x GP EVM or BeagleBoard x15, where the second USB
instance is used as USB client, the dfu command becomes:

.. code-block:: console

    U-Boot # dfu 1 mmc 0

Then on the host PC to write **MLO** to an existing boot partition:

.. code-block:: console

    $ sudo dfu-util -D MLO -a MLO

On the host PC to overwrite the current boot partition contents with a
new created on the host FAT filesystem image:

.. code-block:: console

    $ sudo dfu-util -D fat.img -a boot

.. ifconfig:: CONFIG_part_family not in ('AM64X')

    Updating an SD card or eMMC with RAW writes
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    In some cases it is desirable to write **MLO** and **u-boot.img** as raw
    images to the MMC device rather than in a filesystem. eMMC requires
    this, for example. In that case, the following is how to program these
    files and not overwrite the partition table on the device. We assume
    that the files exist on a SD card. In addition you may wish to write a
    filesystem image to the device, so an example is also provided.

    .. code-block:: console

        U-Boot # mmc dev 0
        U-Boot # mmc rescan
        U-Boot # mmc dev 1
        U-Boot # fatload mmc 0 ${loadaddr} MLO
        U-Boot # mmc write ${loadaddr} 0x100 0x100
        U-Boot # mmc write ${loadaddr} 0x200 0x100
        U-Boot # fatload mmc 0 ${loadaddr} u-boot.img
        U-Boot # mmc write ${loadaddr} 0x300 0x400
        U-Boot # fatload mmc 0 ${loadaddr} rootfs.ext4
        U-Boot # mmc write ${loadaddr} 0x1000 ...rootfs.ext4 size in bytes divided by 512, in hex...

.. _boot-linux-from-mmc:

Booting Linux from SD card or eMMC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Within the default environment for each board that supports SD/MMC there
is a boot command called **mmcboot** that will set the boot arguments
correctly and start the kernel. In this case however, you must first run
**loaduimagefat** or **loaduimage** to first load the kernel into
memory. For the exact details of each use **printenv** on the
**mmcboot**, **loaduimagefat** and **loaduimage** variables and then in
turn **printenv** other sub-sections of the command. The most important
variables here are **mmcroot** and **mmcrootfstype**.

.. ifconfig:: CONFIG_part_family in ('AM335X', 'AM437X', 'AM57X', 'GEN')

    Booting MLO and u-boot from eMMC boot partition (For non-K3 class of SoCs)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    The dra7xx and am57xx processors support booting from the eMMC boot
    partition. The following commands load the boot images from network and
    write them into the boot0 partition.

    .. code-block:: console

        U-boot # setenv autoload no
        U-boot # dhcp
        U-boot # mmc dev 1 1
        U-boot # tftp ${loadaddr} dra7xx/MLO
        U-boot # mmc write ${loadaddr} 0x0 0x300
        U-boot # tftp ${loadaddr} dra7xx/u-boot.img
        U-boot # mmc write ${loadaddr} 0x300 0x400

    We also need to configure the eMMC using the bootbus and partconf commands.
    The bootbus command sets the eMMC into dual data rate mode with a bus width
    of 8 to match with the bus configuration supported by the Boot ROM. The
    partconf command gives access to the boot0 partition during boot operation.
    Note that these configurations are limited to boot operation and the eMMC
    can be set to its highest speed mode once boot operation is complete. All
    these are non-volatile configurations that need to be done **once per
    eMMC/board** .

    .. code-block:: console

        U-boot # mmc bootbus 1 2 0 2
        U-boot # mmc partconf 1 1 1 0
        U-boot # mmc rst-function 1 1

.. _mmc-boot-label:

Booting tiboot3.bin, tispl.bin and u-boot.img from eMMC boot partition (For K3 class of SoCs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The K3 based processors support booting from the eMMC boot partition.
The following commands can be used to download tiboot3.bin, tispl.bin and
u-boot.img from an SD card and write them to the eMMC boot0 partition at
respective addresses.

.. note::
        By default, SDK chooses boot0 partition for eMMC boot (equivalently done
        using ``mmc partconf 0 1 1 1``). Boot partition can also be switched from
        boot0 to boot1 by using ``mmc partconf 0 1 2 1``. This enables booting from
        boot1 partition. Switch to boot1 partition using ``mmc dev 0 2`` and follow
        regular eMMC write commands (seen below). On rebooting with regular eMMC dip
        switch settings, boot1 partition will be used.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

  .. code-block:: console

    => mmc dev 0 1
    => fatload mmc 1 ${loadaddr} tiboot3.bin
    => mmc write ${loadaddr} 0x0 0x800
    => fatload mmc 1 ${loadaddr} tispl.bin
    => mmc write ${loadaddr} 0x800 0x1000
    => fatload mmc 1 ${loadaddr} u-boot.img
    => mmc write ${loadaddr} 0x1800 0x2000

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

For loading images from a FAT partition on a different media, replace mmc with the required
media. For example, to load images from a FAT partition on a USB Storage device connected to
the zeroth instance of usb,

.. code-block:: console

  => fatload usb 0 ${loadaddr} <file name>

.. ifconfig:: CONFIG_part_variant in ('J721E', 'J7200', 'J721S2')

  .. note::
      USB0 instance on J721e/J7200 base board is connected to TypeC port that can be
      used both as host port and device port. By default, USB0 is port is
      configured to be in **peripheral mode**. Since U-Boot does not support
      dynamic switching of USB roles, below DT fragment needs to be
      applied and U-Boot image needs to be rebuilt to make USB0 port to be
      USB 3.0 host port.

  .. code-block:: dts

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

  .. code-block:: dts

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

.. ifconfig:: CONFIG_part_family in ('AM64X_family')

  .. note::
      USB instance in AM64 SoC is brought out using a USB 2.0 micro-AB port on the GP EVM. This port can be
      used in both host and device modes. By default in U-Boot, peripheral mode is supported.
      For accessing USB storage devices in U-Boot, dr_mode should be set to "host" in the U-Boot
      device tree file. The following diff shows the required changes to be done. On Starter Kit,
      USB instance in AM64 SoC is brought out using a USB 3.0 Type A port, so the mode is set to
      host by default and the following diff would not be required.

.. ifconfig:: CONFIG_part_family in ('AM62X_family')

  .. note::
      There are two instances of USB on AM62 SoC. On the SK board, zeroth instance is brought out
      through a Type C port and the first instance is brought through a Type A port. By default,
      USB0 port is configured to be in **peripheral mode**. Since U-Boot does not support
      dynamic switching of USB roles, below DT fragment needs to be applied and U-Boot image
      needs to be rebuilt to make USB0 port to be USB 2.0 host port.


.. ifconfig:: CONFIG_part_variant in ('AM65X')

  .. note::
      There are two instance of USB on AM654 SoC. The zero instance is not brought out on EVM
      and the first instance is brought using a USB 2.0 micro-AB port on the EVM.
      By default in U-Boot, peripheral mode is supported. For accessing USB storage devices in U-Boot,
      dr_mode should be set to "host" in the U-Boot device tree file. The following diff shows the
      required changes to be done.

.. ifconfig:: CONFIG_part_family in ('AM64X_family')

    .. code-block:: dts

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

.. ifconfig:: CONFIG_part_family in ('AM62X_family')

    .. code-block:: dts

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

    .. code-block:: dts

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

To give the ROM access to the boot partition, the following commands must be
used for the first time:

.. code-block:: console

  => mmc partconf 0 1 1 1
  => mmc bootbus 0 2 0 0

- eMMC layout:

.. ifconfig:: CONFIG_part_variant in ('AM64X')

  .. code-block:: console

               boot0 partition (8 MB)                        user partition
       0x0+----------------------------------+      0x0+-------------------------+
          |     tiboot3.bin (1 MB)           |         |                         |
     0x800+----------------------------------+         |                         |
          |       tispl.bin (2 MB)           |         |                         |
    0x1800+----------------------------------+         |        rootfs           |
          |       u-boot.img (4 MB)          |         |                         |
    0x3800+----------------------------------+         |                         |
          |      environment (128 KB)        |         |                         |
    0x3900+----------------------------------+         |                         |
          |   backup environment (128 KB)    |         |                         |
    0x3A00+----------------------------------+         +-------------------------+

.. ifconfig:: CONFIG_part_variant not in ('AM64X', 'J7200', 'J721S2', 'AM62X')

    .. code-block:: console

                 boot0 partition (8 MB)                        user partition
         0x0+----------------------------------+      0x0+-------------------------+
            |     tiboot3.bin (512 KB)         |         |                         |
       0x400+----------------------------------+         |                         |
            |       tispl.bin (2 MB)           |         |                         |
      0x1400+----------------------------------+         |        rootfs           |
            |       u-boot.img (4 MB)          |         |                         |
      0x3400+----------------------------------+         |                         |
            |      environment (128 KB)        |         |                         |
      0x3500+----------------------------------+         |                         |
            |   backup environment (128 KB)    |         |                         |
      0x3600+----------------------------------+         |                         |
            |          sysfw (1 MB)            |         |                         |
      0x3E00+----------------------------------+         +-------------------------+


.. ifconfig:: CONFIG_part_variant in ('J7200')

  .. code-block:: console

                boot0 partition (8 MB)                        user partition
       0x0+----------------------------------+      0x0+-------------------------+
          |     tiboot3.bin (1 MB)           |         |                         |
     0x800+----------------------------------+         |                         |
          |       tispl.bin (2 MB)           |         |                         |
    0x1800+----------------------------------+         |        rootfs           |
          |       u-boot.img (4 MB)          |         |                         |
    0x3800+----------------------------------+         |                         |
          |      environment (128 KB)        |         |                         |
    0x3900+----------------------------------+         |                         |
          |   backup environment (128 KB)    |         |                         |
    0x3A00+----------------------------------+         +-------------------------+


.. ifconfig:: CONFIG_part_variant in ('J721S2', 'AM62X')

  .. code-block:: console

                boot0 partition (8 MB)                        user partition
       0x0+----------------------------------+      0x0+-------------------------+
          |     tiboot3.bin (1 MB)           |         |                         |
     0x400+----------------------------------+         |                         |
          |       tispl.bin (2 MB)           |         |                         |
    0x1400+----------------------------------+         |        rootfs           |
          |       u-boot.img (4 MB)          |         |                         |
    0x3400+----------------------------------+         |                         |
          |      environment (128 KB)        |         |                         |
    0x3500+----------------------------------+         |                         |
          |   backup environment (128 KB)    |         |                         |
    0x3600+----------------------------------+         +-------------------------+

To boot from UDA parition of eMMC. Please set following

.. code-block:: console

  => mmc partconf 0 1 7 1
  => mmc bootbus 0 2 0 0

**Enable warm reset**

On eMMC devices, warm reset will not work if EXT_CSD[162] bit is unset since the reset input signal
will be ignored. Warm reset is required to be enabled in order to the eMMC to be in a "clean state"
on power on reset so that ROM can do clean enumeration.

To set the EXT_CSD[162] bit, stop at U-boot prompt and execute the following command:

.. code-block:: console

  => mmc rst-function 0 1

.. warning::

  WARNING : This is a write-once field.

For more information, please refer to the latest U-boot documentation: https://docs.u-boot.org/en/latest/usage/cmd/mmc.html.

|

**Boot kernel from eMMC**

.. note::
	rootfs is written to the user partition. The user partition is
	first required to be formatted as a ext4 file system and then the rootfs
	has to be written. It is not possible to format a partition to ext4 in
	U-Boot. It is required to boot to kernel and write rootfs to user partition
	after formatting it to ext4. Kernel image and DT are expected to be present
	in the /boot folder of rootfs.

To boot kernel from eMMC, use the following commands after writing rootfs to user partition:

.. code-block:: console

    => setenv mmcdev 0
    => setenv bootpart 0
    => boot

.. _U-Boot-USB-MSC-boot-label:

Booting to U-Boot prompt from USB storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('J7200', 'J721E')

  |__PART_FAMILY_DEVICE_NAMES__| SoC does not support booting from USB mass storage devices.
  However, it can be used as storage device at U-Boot prompt.

.. ifconfig:: CONFIG_part_family in ('AM64X_family')

  Booting to U-Boot prompt from USB storage is supported. The following are the steps to be followed,

  #. Build the bootloader images using default "am64x_evm_r5_defconfig"
     and "am64x_evm_a53_defconfig" configs files. The configs required for
     USB MSC boot are already enabled. For instructions to build the bootloader
     images please refer to :ref:`Build-U-Boot-label`.

  #. Create a FAT32 partition with boot flag enabled on the USB storage device.

  #. Copy the bootloader images(tiboot3.bin, tispl.bin, u-boot.img) into the above created partition.

  #. Set the boot mode switches to usb host mode by referring to the Technical Reference manual.

  #. Connect the USB Mass storage device with the bootloader images and boot up the board.

.. ifconfig:: CONFIG_part_variant in ('AM65X')

  Booting to U-Boot prompt from USB storage is supported. The following are the steps to be followed,

  #. Build the bootloader images using default "am65x_evm_r5_usbmsc_defconfig"
     and "am65x_evm_a53_defconfig" configs files. The configs required for
     USB MSC boot are already enabled. For instructions to build the bootloader
     images please refer to :ref:`Build-U-Boot-label`.

  #. Create a FAT32 partition with boot flag enabled on the USB storage device.

  #. Copy the bootloader images(tiboot3.bin, sysfw.itb, tispl.bin, u-boot.img) into the above created partition.

  #. Set the boot mode switches to usb host mode by referring to the Technical Reference manual.

  #. Connect the USB Mass storage device with the bootloader images and boot up the board.

.. ifconfig:: CONFIG_part_variant in ('J722S')

  Booting to U-Boot prompt from USB storage is supported. The following are the steps to be followed,
  #. In U-Boot the USB controller can be used in either host or peripheral mode. For booting to linux kernel from USB storage device, the USB port is to be set as host.

  #. By default, USB0 is set to peripheral mode. Change this from peripheral to host mode.

  #. Build the bootloader images using the default "j722s_evm_r5_defconfig"
     and the config fragment "j722s_evm_r5_usbmsc.config" and "j722s_evm_a53_defconfig"
     configs files. The configs required for
     USB MSC boot are already enabled. For instructions to build the bootloader
     images please refer to :ref:`Build-U-Boot-label`.

  #. Create a FAT32 partition with boot flag enabled on the USB storage device.

  #. Copy the bootloader images(tiboot3.bin, tispl.bin, u-boot.img) into the above created partition.

  #. Set the boot mode switches to USB host boot mode (Refer to  **Initialization** chapter of TRM for boot switch details)

  #. Make sure USB0 port in DRP mode: SW2[2:3] = 00

  #. Connect the USB Mass storage device with the bootloader images and boot up the board.

.. note::
  While using ``usb reset`` or ``usb start`` command in U-Boot, or booting from a USB Mass storage device, some of the USB
  devices fail to get detected. This issue is seen because these USB
  devices are failing to follow the spec for power good delay. It can be
  resolved by overriding the power good delay using the environment variable
  ``usb_pgood_delay``. Setting it to 2000 should be good enough for all cases.


Booting Linux from USB storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_family in ('J7_family')

  .. ifconfig:: CONFIG_part_variant not in ('J722S')

     This feature is currently not supported.

.. ifconfig:: CONFIG_part_variant in ('J722S')

    To load the Linux kernel, Device Tree and the Root file system from USB Mass storage device,
    the following changes are required to be done,

    - U-Boot

      #. In U-Boot the USB controller can be used in either host or peripheral mode. For booting to linux kernel
         from USB storage device, the USB port is to be set as host.
      #. By default, USB0 is set to peripheral mode. Change this from peripheral to host mode

    - Kernel

      #. In kernel, by default the USB subsystem is built as modules. For booting from USB mass storage device,
         USB subsytem is required to be built into the image. This can be done by making the following changes
         in the configuration used for building kernel,

      .. code-block:: text

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

    - Copying the images to USB storage device

      #. After making the required changes mentioned above, build the kernel, device tree file and modules
      #. The USB Mass storage device should have the rootfs as the second partition with ext4 file system,

          - The following images should be in /boot/ directory

            - Kernel image
            - device tree file

    - During the boot, cancel the autoboot at U-Boot and run the following command on U-Boot
      prompt

      .. code-block:: console

         => run usb_boot

.. ifconfig:: CONFIG_part_family in ('AM62X_family')

    To load the Linux kernel, Device Tree and the Root file system from USB Mass storage device,
    the following changes are required to be done,

    - U-Boot

      #. In U-Boot the USB controller can be used in either host or peripheral mode. For booting to linux kernel
         from USB storage device, the USB port is to be set as host.
      #. By default, on AM625-SK board the zero instance of USB connected to the Type C port, is set to peripheral mode
         and the first instance of USB connected to the Type A port is set to host mode.
      #. Therefore, USB controller needs to be set host mode and custom bootloader images are required to be built, if zeroth
         instance is used. Please refer to note in section :ref:`mmc-boot-label`

    - Kernel

      #. In kernel, by default the USB subsystem is built as modules. For booting from USB mass storage device,
         USB subsytem is required to be built into the image. This can be done by making the following changes
         in the configuration used for building kernel,

      .. code-block:: text

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

    - Copying the images to USB storage device

      #. After making the required changes mentioned above, build the kernel, device tree file and modules
      #. The USB Mass storage device should have the rootfs as the second partition with ext4 file system,

          - The following images should be in /boot/ directory

            - Kernel image
            - device tree file

    - During the boot, cancel the autoboot at U-Boot and run the following command on U-Boot
      prompt

      .. code-block:: console

        => run usbboot

.. ifconfig:: CONFIG_part_family in ('AM64X_family')

    To load the Linux kernel, Device Tree and the Root file system from USB Mass storage device,
    the following changes are required to be done,

    - U-Boot

      #. In U-Boot the USB controller can be used in either host or peripheral mode. For booting to linux kernel
         from USB storage device, the USB port is to be set as host.
      #. By default, the USB controller is set in peripheral mode.
      #. If the boot media used to boot to U-Boot is USB Host mode(:ref:`U-Boot-USB-MSC-boot-label`) then,
         the USB controller is set to host mode during runtime. Therefore, no changes would be required in this case.
      #. If a boot media other than USB Host is used, the USB controller needs to be set host mode and custom
         bootloader images are required to be built. Please refer to note in section :ref:`mmc-boot-label`

    - Kernel

      #. In kernel, by default the USB subsystem is built as modules. For booting from USB mass storage device,
         USB subsytem is required to be built into the image. This can be done by making the following changes
         in the configuration used for building kernel,

      .. code-block:: text

          CONFIG_USB=y
          CONFIG_USB_XHCI_HCD=y
          CONFIG_USB_XHCI_PLATFORM=y
          CONFIG_USB_STORAGE=y
          CONFIG_USB_GADGET=y
          CONFIG_USB_CDNS3=y
          CONFIG_USB_CDNS3_GADGET=y
          CONFIG_USB_CDNS3_HOST=y
          CONFIG_USB_CDNS3_TI=y

    - Copying the images to USB storage device

      #. After making the required changes mentioned above, build the kernel, device tree file and modules
      #. The USB Mass storage device should have two partitions,

        - boot

          - For creating this parition please refer :ref:`U-Boot-USB-MSC-boot-label`
        - rootfs

          - A partition with ext4 filesystem and the following images in /boot/ directory

            - Kernel image
            - device tree file

    - During the boot, cancel the autoboot at U-Boot and run the following command on U-Boot
      prompt

      .. code-block:: console

        => run usbboot

.. ifconfig:: CONFIG_part_family not in ('AM64X_family', 'J7_family')

    Booting Linux from USB storage
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    To load the Linux Kernel and rootfs from USB rather than SD/MMC card on
    AMx/DRA7x EVMs, if we assume that the USB device is partitioned the same
    way as an SD/MMC card is, we can utilize the **mmcboot** command to
    boot. To do this, perform the following steps:

    .. code-block:: console

        U-Boot # usb start
        U-Boot # setenv mmcroot /dev/sda2 ro
        U-Boot # run mmcargs
        U-Boot # run bootcmd_usb

    On K2H/K/E/L EVMs, the USB drivers in Kernel needs to be built-in
    (default modules). The configuration changes are:

    .. code-block:: text

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

    The USB should have boot partition of FAT32 format, and rootfs partition
    of EXT4 format. The boot partition must contain the following images:

    .. code-block:: text

        keystone-<platform>-evm.dtb
        skern-<platform>.bin
        k2-fw-initrd.cpio.gz
        zImage

        where <platform>=k2hk, k2e, k2l

    The rootfs partition contains the filesystem from ProcSDK release
    package.

    .. code-block:: console

        # mkdir /mnt/temp
        # mount -t ext4 /dev/sdb2 /mnt/temp
        # cd /mnt/temp
        # tar xvf <Linux_Proc_Sdk_Install_DIR>/filesyste/tisdk-server-rootfs-image-k2hk-evm.tar.xz
        # cd /mnt
        # umount temp

    Set up the following u-boot environment variables:

    .. code-block:: console

        setenv args_all 'setenv bootargs console=ttyS0,115200n8 rootwait'
        setenv args_usb 'setenv bootargs ${bootargs} rootdelay=3 rootfstype=ext4 root=/dev/sda2 rw'
        setenv get_fdt_usb 'fatload usb 0:1 ${fdtaddr} ${name_fdt}'
        setenv get_kern_usb 'fatload usb 0:1 ${loadaddr} ${name_kern}'
        setenv get_mon_usb 'fatload usb 0:1 ${addr_mon} ${name_mon}'
        setenv init_fw_rd_usb 'fatload usb 0:1 ${rdaddr} ${name_fw_rd}; setenv filesize <hex_len>; run set_rd_spec'
        setenv init_usb 'usb start; run args_all args_usb'
        setenv boot usb
        saveenv
        boot

    **Note:**: <hex\_len> must be at least the hex size of the k2-fw-initrd.cpio.gz file size.


    Booting from SD/eMMC from SPL (Single stage or Falcon mode)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    .. note::
        Falcon mode is not supported on K3 family of devices.

    In this boot mode SPL (first stage bootloader) directly boots the Linux
    kernel. Optionally, in order to enter into U-Boot, reset the board while
    keeping 'c' key on the serial terminal pressed. When falcon mode is
    enabled in U-Boot build (usually enabled by default), ``MLO`` checks if
    there is a valid ``uImage`` present at a defined offset. If ``uImage``
    is present, it is booted directly. If valid ``uImage`` is not found,
    ``MLO`` falls back to checking if the ``uImage`` exists in a FAT
    partition. If it fails, it falls back to booting ``u-boot.img``.

    The falcon boot uses ``uImage``. To build the kernel ``uImage``, you
    will need to keep the U-Boot tool ``mkimage`` in your ``$PATH``

    .. code-block:: console

        # make uImage modules dtbs LOADADDR=80008000

    If kernel is not build with ``CONFIG_CMDLINE`` to set correct bootargs,
    then add the needed ``bootargs`` in ``chosen`` node in DTB file, using
    ``fdtput`` host utility. For example, for DRA74x EVM:

    .. code-block:: console

        # fdtput -v -t s arch/arm/boot/dts/dra7-evm.dtb "/chosen" bootargs "console=ttyO0,115200n8 root=<rootfs>"

    ``MLO``, ``u-boot.img`` (optional), DTB, ``uImage`` are all stored on
    the same medium, either the SD or the eMMC. There are two ways to store
    the binaries in the SD (resp. eMMC):

    .. code-block:: text

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
    USB instance is used as USB client, replace "dfu 0 mmc X" with "dfu 1
    mmc X"

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

Steps for working around SD card issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In some cases issue can be seen while using some SD cards, like

#. Error while trying to initialize,

    .. code-block:: console

        U-Boot SPL 2021.01-g74fc69c889 (May 19 2022 - 02:44:29 +0000)
        SYSFW ABI: 3.1 (firmware rev 0x0008 '8.3.2--v08.03.02 (Jolly Jellyfi')
        Trying to boot from MMC2
        spl: mmc init failed with error: -110
        SPL: failed to boot from all boot devices
        ### ERROR ### Please RESET the board ###

Given below are the list of various workarounds that can be done in the
device tree node to get SD card working. The workarounds are ordered in
increasing order of reducing performance.

All the  mentioned below, are to be done in the MMCSD device tree node
corresponding to the SD instance. This is usually the first(index starting
from zero) instance.

#. Restricting to a given speed mode

   - By default the U-Boot driver tries to enumerate a SD card in the highest
     supported speed mode. Given below is the order in which the driver
     tries to enumerate a SD card

       - SDR104
       - SDR50
       - DDR50
       - SD HS
       - SD legacy

   - These speed capabilites can be masked using device tree property
     sdhci-caps-mask.

       - Limit to SDR50: ``sdhci-caps-mask = <0x00000004 0x00000000>``
       - Limit to DDR50: ``sdhci-caps-mask = <0x00000006 0x00000000>``
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
                 sdhci-caps-mask = <0x00000006 0x00000000>; /* Limiting to DDR50 speed mode */
              };

#. Increase power cycle period

    - Increasing the delay while power cycling the SD card. This can be done
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

    - The SD interface supports a bus width of 4. It can be reduced to 1 by
      changing the ``bus-width`` device tree property from 4 to 1.

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
