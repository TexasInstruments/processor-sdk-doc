NAND
----

.. ifconfig:: CONFIG_part_family in ('J7_family')

    .. note::
        NAND is not supported on J721E platform.

.. ifconfig:: CONFIG_part_family in ('AM62X_family')

    .. note::
        Use **am62x_lpsk_r5_gpmc_defconfig** as reference to enable GPMC NAND
        boot with AM62x SoC.

This section documents how to write files to the NAND device and use it
to load and then boot the Linux Kernel using a root filesystem also
found on NAND.

Erasing, Reading and Writing to/from NAND partitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Listing NAND partitions
   :name: listing-nand-partitions

Below command is used to see the list of mtd devices enabled in U-boot

::

    mtdparts

Example output on DRA71x EVM:

::

    device nand0 <nand.0>, # parts = 10
     #: name                size            offset          mask_flags
     0: NAND.SPL            0x00020000      0x00000000      0
     1: NAND.SPL.backup1    0x00020000      0x00020000      0
     2: NAND.SPL.backup2    0x00020000      0x00040000      0
     3: NAND.SPL.backup3    0x00020000      0x00060000      0
     4: NAND.u-boot-spl-os  0x00040000      0x00080000      0
     5: NAND.u-boot         0x00100000      0x000c0000      0
     6: NAND.u-boot-env     0x00020000      0x001c0000      0
     7: NAND.u-boot-env.backup10x00020000   0x001e0000      0
     8: NAND.kernel         0x00800000      0x00200000      0
     9: NAND.file-system    0x0f600000      0x00a00000      0

Note: In later sections the <partition name> symbol should be replaced
with the partition name seen when executing the mtdparts command.

.. rubric:: Erasing Partition
   :name: erasing-partition

::

    nand erase.part <partition name>

.. rubric:: Writing to Partition
   :name: writing-to-partition

When writing to NAND partition the file to be written must have
previously been copied to memory.

::

    nand write <ddr address> <partition name> <file size>

The symbol <ddr address> refers to the location in memory that a file
was read into DDR memory. The symbol <file size> represents the amount
of bytes (in hex) of the file to write into the NAND partition. Note:
When reading a file into DDR, U-boot by default sets the value of
environment variable "filesize" to the number of bytes (in hex) that was
read via the last read/load command.

|
| As an example below shows the process of writing a kernel (zImage)
  into the NAND's kernel partition. The zImage to be written is loaded
  from the SD card's rootfs (2nd) partition. Loading zImage from MMC to
  DDR memory

::

    U-Boot # mmc dev 0;
    U-Boot # setenv devnum 0
    U-Boot # setenv devtype mmc
    U-Boot # mmc rescan
    U-Boot # load ${devtype} 1:2 ${loadaddr} /boot/zImage

Now that zImage is loaded into memory time to write it into the NAND
partition

::

    U-Boot # nand erase.part NAND.kernel
    U-Boot # nand write ${loadaddr} NAND.kernel ${filesize}

.. rubric:: Reading from Partition
   :name: reading-from-partition

::

    nand read <ddr address> <partition name>

The symbol <ddr address> should be replaced with the location in DDR
that you want the contents of the NAND partition to be copied to. The
symbol <partition name> contains the NAND partition name you want to
read from.

|

Writing to NAND via DFU
^^^^^^^^^^^^^^^^^^^^^^^

If the board supports NAND and USB then flashing NAND via DFU is
most likely supported (Not supported in AM64 on 8.2).

Before dfu commands can be used, **mtdparts** and **dfu_alt_info**
must be correctly set.

Check if NAND partitions are visible in **mtdparts** command

::

    U-Boot # mtdparts

    device nand0 <omap2-nand.0>, # parts = 7
     #: name                size            offset          mask_flags
     0: NAND.tiboot3        0x00200000      0x00000000      0
     1: NAND.tispl          0x00200000      0x00200000      0
     2: NAND.tiboot3.backup 0x00200000      0x00400000      0
     3: NAND.u-boot         0x00400000      0x00600000      0
     4: NAND.u-boot-env     0x00040000      0x00a00000      0
     5: NAND.u-boot-env.backup0x00040000    0x00a40000      0
     6: NAND.filesystem     0x3f580000      0x00a80000      0

    active partition: nand0,0 - (NAND.tiboot3) 0x00200000 @ 0x00000000

Check that DFU can correctly see the NAND partition layout

::

    dfu 0 nand list

    DFU alt settings list:
    dev: NAND alt: 0 name: NAND.tiboot3 layout: RAW_ADDR
    dev: NAND alt: 1 name: NAND.tispl layout: RAW_ADDR
    dev: NAND alt: 2 name: NAND.tiboot3.backup layout: RAW_ADDR
    dev: NAND alt: 3 name: NAND.u-boot layout: RAW_ADDR
    dev: NAND alt: 4 name: NAND.u-boot-env layout: RAW_ADDR
    dev: NAND alt: 5 name: NAND.u-boot-env.backup layout: RAW_ADDR
    dev: NAND alt: 6 name: NAND.file-system layout: RAW_ADDR

In case you see an error like 'Device nor0 not found!' then you need to
ensure that all mtd devices specified in mtdids variable are available.

e.g. To probe nor device you will have to do

::

    sf probe

Before writing we must erase at least the area to be written to.

::

    U-Boot # nand erase.part NAND.file-system
    --OR erase entire chip--
    U-Boot # nand erase.chip

Start DFU on the EVM. Plug the EVM to a PC via USB cable. At uboot prompt,
run the following commands:

::

    U-Boot # env default -a -f

Set the **dfu_alt_info** environment variable for DFU to NAND.

.. ifconfig:: CONFIG_part_family in ('AM62X_family')

        ::

                U-Boot # setenv dfu_alt_info ${dfu_alt_info_gpmc_nand}

.. ifconfig:: CONFIG_part_family in ('AM64X_family')

        ::

                U-Boot # setenv dfu_alt_info ${dfu_alt_info_nand}

::

    U-Boot # dfu 0 nand 0

Use the the correct DFU USB port on the EVM. On the PC, check that you can see the DFU USB interface

::

    $ sudo dfu-util -l

    Found DFU: [0451:6165] ver=0224, devnum=8, cfg=1, intf=0, path="3-13.1", alt=6, name="NAND.file-system", serial="0000000000000280"
    Found DFU: [0451:6165] ver=0224, devnum=8, cfg=1, intf=0, path="3-13.1", alt=5, name="NAND.u-boot-env.backup", serial="0000000000000280"
    Found DFU: [0451:6165] ver=0224, devnum=8, cfg=1, intf=0, path="3-13.1", alt=4, name="NAND.u-boot-env", serial="0000000000000280"
    Found DFU: [0451:6165] ver=0224, devnum=8, cfg=1, intf=0, path="3-13.1", alt=3, name="NAND.u-boot", serial="0000000000000280"
    Found DFU: [0451:6165] ver=0224, devnum=8, cfg=1, intf=0, path="3-13.1", alt=2, name="NAND.tiboot3.backup", serial="0000000000000280"
    Found DFU: [0451:6165] ver=0224, devnum=8, cfg=1, intf=0, path="3-13.1", alt=1, name="NAND.tispl", serial="0000000000000280"
    Found DFU: [0451:6165] ver=0224, devnum=8, cfg=1, intf=0, path="3-13.1", alt=0, name="NAND.tiboot3", serial="0000000000000280"


On the PC, write the bootloader to the first NAND partition:

::

    $ sudo dfu-util -D tiboot3.bin -a NAND.tiboot3

Similarly for Other bootloader binaries:

::

    $ sudo dfu-util -D tispl.bin -a NAND.tispl

::

    $ sudo dfu-util -D u-boot.img -a NAND.u-boot

NAND Boot
^^^^^^^^^

If you want to load and run U-Boot from NAND, you need to ensure
that the appropriate U-boot files are loaded in the correct partition.
For AM335x, AM437x, DRA7x devices this means writing the file MLO to the
NAND's SPL partition. For OMAP-L138 device, write the .ais image to the
NAND's partition. For K3 devices you need to write tiboot3.bin to the
NAND.tiboot3 and tispl.bin to the NAND.tispl partition.

For all devices you will have to write u-boot.img to the NAND.u-boot partition.

Example of flashing u-boot over network (tftp)

::

    => setenv ipaddr <EVM_IPADDR>
    => setenv serverip <TFTP_SERVER_IPADDR>
    => tftpboot ${loadaddr} tiboot3.bin
    => print filesize
        filesize=8b3fa
    => nand erase.part NAND.tiboot3
    => nand write ${loadaddr} NAND.tiboot3 8b3fa

Repeat the process for all files required for u-boot. (e.g. tispl.bin and u-boot.img)

Once the file(s) have been written to NAND the board should then be
powered off. Next evm's boot switches need to be configured for NAND
booting. To understand the appropriate boot switches settings please see
the EVM's hardware setup guide.

|

Booting Kernel and Filesystem from NAND
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If a user wants to use NAND as their primary storage then the NAND flash
must have individual partitions for all the critical software needed to
boot the kernel. At a minimum this includes kernel, dtb, file system.
Some SoCs require additional files and firmware which also need to be
stored in different NAND partitions.

Similar to booting the kernel from any interface the user must ensure
that all required files needed for booting are loaded in DDR memory. The
only exception is the filesystem which will be loaded by the kernel via
the bootargs parameters. Bootargs contains information passed to the
kernel including where and how to mount the file system.

The below contains example bootargs used by DRA7x evm for using a ubifs
filesystem

::

    setenv bootargs console=${console} ${optargs} root=ubi0:rootfs rw ubi.mtd=NAND.file-system,2048 rootfstype=ubifs rootwait=1

In the above example bootargs, "rootfs" stands for the value specified
by in the "vol\_name" parameter defined in the ubinize.cfg file. In
ubi.mtd "NAND.file-system" represents the name of the partition that
contains the UBI volumes and "2048" is page size. Rootfstype simply tells
the kernel what type of file system to use.

By default for our evms properly loading, setting bootargs and booting
the kernel is handled by running "run nandboot" in U-boot.

Below is an example of u-boot environment settings for NAND booting on K3
platforms. The kernel, device tree blobs and root filesystem are fetched from
the rootfs UBIFS volume.

::

    bootdir=/boot

    ubi_init=ubi part NAND.file-system; ubifsmount ubi0:rootfs;
    args_nand=setenv bootargs console=${console} ${mtdparts} ubi.mtd=NAND.file-system root=ubi0:rootfs rootfstype=ubifs rootwait=1
    init_nand=run args_all args_nand ubi_init findfdt

    overlayaddr=0x89000000

    get_fdt_nand=ubifsload ${fdtaddr} ${bootdir}/${fdtfile}; fdt address ${fdtaddr}; fdt resize 0x100000; echo "loading overlays"; for overlay in $name_overlays; do; echo ${overlay}; ubifsload ${overlayaddr} ${bootdir}/${overlay}; fdt apply ${overlayaddr}; done;
    get_kern_nand=ubifsload ${loadaddr} ${bootdir}/${name_kern}

    boot=nand

U-Boot Environment in NAND
^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, U-Boot environment is saved in a FAT partition on the SD-card.
For saving/restoring U-Boot environment from a NAND partition, the following
changes need to be done to U-Boot configuation at build time.

Run menuconfig and set the U-Boot configuration as below

::

        Environment  --->
            [ ] Environment in an MMC device
            [*] Environment in a NAND device
            [*] Enable redundant environment support
            (0x00a00000) Environment offset
            (0x00a40000) Redundant environment offset
            (0x40000) Environment Size

The 'Environment offset', 'Redundant environment offset' and 'Environment Size'
represent the 'NAND.u-boot' and 'NAND.u-boot-env' partition offsets and size
respectively. They can be obtained from the NAND device node specification in
the board's device tree file.

Information on creating a UBIFS image and NAND flashing can be found
Refer :ref:`here <linux-ubifs>` for UBIFS
