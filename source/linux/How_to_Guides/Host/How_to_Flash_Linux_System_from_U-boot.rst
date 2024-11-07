.. http://processors.wiki.ti.com/index.php/How_to_Flash_Linux_System_from_U-boot

How to Flash from U-boot Shell
================================================

.. ifconfig:: CONFIG_part_family in ('J7_family')

    The procedure is documented in the u-boot documentation. The most updated
    information can be found in the u-boot README file linked to below:

    ::

        https://git.ti.com/cgit/ti-u-boot/ti-u-boot/tree/doc/board/ti/j721e_evm.rst


.. ifconfig:: CONFIG_part_family in ('General_family')

    .. rubric:: Application
       :name: application

    This article applies to Sitara SDK 4.0.1 which uses the Platform Support
    Package (PSP) software version 03.01.00.06

    for AM35x and AM37x devices.   This information is obsolete as newer
    software has different NAND ECC requirements.

    .. rubric:: Introduction
       :name: introduction-flash-linux-system-from-uboot

    This guide will show how use u-boot to flash the NAND of an OMAP3 EVM
    (for AM37x, DM37x or OMAP35xx devices) or an AM3517EVM (for AM35x
    devices) with Linux system binaries.

    -  Assumptions:

    #. SD card with system binaries (x-loader, u-boot, Linux kernel) on
       **boot** partition
    #. Linux root filesystem in **rootfs** partition of SD card or root
       filesystem available via NFS

    .. rubric:: Caution
       :name: caution

    The procedures here will erase the NAND flash of the EVM.  This includes
    all u-boot environment variables.  Use the "**printenv**" command (or
    just "**pri**") in u-boot to print a complete list of environment
    variables.  Copy and paste these to a text file for safe keeping.

    .. rubric:: Boot EVM into SD/MMC card boot mode
       :name: bootevm-into-sdmmc-card-boot-mode

    The SD card must at least have the files MLO, u-boot.bin, and uImage.
    All of these files can also be found in the "./psp/prebuilt-images"
    directory in the Sitara SDK installation (with names that include the
    platform name and software revision info).  The MLO file is simply a
    re-named copy of the file x-load.bin.ift that is produced by rebuilding
    x-loader and signing the file.  When the board is booted in SD/MMC card
    boot mode, the ROM code looks specifically for the file with the name
    MLO as the primary bootloader.

    To boot from this SD card, the boot switches should be set to SD/MMC
    boot:

    **For Mistral OMAP EVM (AM37x, DM37x or OMAP35xx devices)**

    | Set SW4 switches #1, #2, #3 and #6 to the ON position and all others
      OFF (MMC1, UART3 boot order)
    | **For LogicPD AM3517EVM (AM35x device)**

    | Set SW7 switches #1 and #4 to the ON position and all others OFF.
      (USB, UART, MMC1, XIP boot order)

    Start the board and interrupt the boot process when prompted by hitting
    any key in the UART terminal application:

    ::

        Texas Instruments X-Loader 1.45 (Mar 19 2010 - 19:44:19)
        Starting X-loader on MMC
        Reading boot sector

        212504 Bytes Read from MMC
        Starting OS Bootloader from MMC...
        Starting OS Bootloader...
        U-Boot 2009.11 (May 06 2010 - 16:57:54)

        OMAP34xx/35xx-GP ES1.0, CPU-OPP2 L3-165MHz
        OMAP3 EVM board + LPDDR/NAND
        I2C: ready
        DRAM: 128 MB
        NAND: 256 MiB
        *** Warning - bad CRC or NAND, using default environment

        In: serial
        Out: serial
        Err: serial
        Read back SMSC id 0x92200000
        Die ID #731c0000000000000156087c0a023021
        Net: smc911x-0
        Hit any key to stop autoboot: 0
        OMAP3_EVM #
        OMAP3_EVM #

    All of the commands in this guide are performed at the u-boot prompt.

    .. rubric:: Run the u-boot commands to flash the NAND
       :name: run-the-u-boot-commands-to-flash-the-nand

    All of the following commands are performed at the u-boot prompt.

      These commands are actually a series of u-boot commands that are
    connected together with semicolons.  The individual commands can be
    entered separately or simple pasted from here.

    |

    -  Complete xloader write from MMC to NAND (only erases one block=128k).

    ::

        mw.b 0x81600000 0xff 0x20000;nand erase 0 20000;mmc init;fatload mmc 0 0x81600000 x-load.bin.ift;nandecc hw; nand write.i 0x81600000 0 20000

    -  Complete uboot write from MMC to NAND (only erases two blocks=256k)

    ::

        mw.b 0x81600000 0xff 0x40000;nand erase 80000 40000;mmc init;fatload mmc 0 0x81600000 u-boot.bin;nandecc sw; nand write.i 0x81600000 80000 40000

    -  Complete kernel write from MMC to NAND (erases 3M)

    ::

        mw.b 0x81600000 0xff 0x1400000;nand erase 280000 300000;mmc init;fatload mmc 0 0x81600000 uImage;nandecc sw; nand write.i 0x81600000 280000 300000

    .. rubric:: Put the EVM in NAND boot mode
       :name: put-the-evm-in-nandboot-mode

     With the EVM in NAND boot mode and the images flashed in NAND as
    detailed above, the SD card does not need to be in the EVM at boot up.
    X-loader and u-boot will run from NAND.  In order to also pull the Linux
    kernel (uImage) from NAND it will be necessary to halt the boot process
    and edit some u-boot environment variables.

    |

    **For Mistral OMAP EVM (AM37x, DM37x or OMAP35xx devices)**

    Set SW4 switches #2, #4 and #6 to the ON position and all others OFF
    (NAND, UART3 boot order)

    **For LogicPD AM3517EVM (AM35x device)**

    Set SW7 with switches #1 thru #8 all to the OFF position. (NAND, EMAC,
    USB, MMC1 boot order)

    -  Save off the original boot command

    ::

        setenv bootcmd_original ${bootcmd}
        saveenv

    |

    -  Create command for reading the kernel from NAND and then another
       command for doing the boot where the kernel is pulled from NAND and
       the root filesystem is from the SD/MMC card.

    ::

        setenv nand_kernel 'nand read.i ${loadaddr} 280000 300000'
        setenv nand_mmc_boot 'run nand_kernel;setenv bootargs ${mmcargs}; bootm'

    Run this last command to actually perform the boot.  And always save the
    environment after making changes.

    ::

        saveenv
        run nand_mmc_boot

    .. rubric:: Flashing the Root File System to NAND
       :name: flashing-the-root-file-system-to-nand

    A jffs2 file system can be copied into NAND flash.  Copy the file
    rootfs.tar.gz to the /home/root directory on the SD Card. Boot the EVM
    to Linux and enter the following commands:

    ::

        [prompt]$ flash_eraseall –j /dev/mtd4
        [prompt]$ mount /dev/mtdblock4 /media/nand –t jffs2
        [prompt]$ cd /media/nand
        [prompt]$ tar xzf /home/root/rootfs.tar.gz
        [prompt]$ reboot –f

    The bootargs under u-boot must be altered to use this new NAND file
    system.

    NOTE:After the reboot the board is now running in u-boot, remember to
    stop the autoboot sequence by typing any key. The following are u-boot
    commands:

    ::

        setenv bootargs 'mem=128M console=ttyS0,115200n8 noinitrd root=/dev/mtdblock4 rw rootfstype=jffs2 ip=dhcp'
        bootm

    .. rubric:: Mounting File System from NFS
       :name: mounting-file-system-from-nfs

    The file system can also be mounted as a Network File System (NFS).  The
    NFS is simply a sub-directory of the Linux host development system.

    Another command can be made to pull the root filesystem via NFS.  This
    command can be combine with the one to pull the bootloaders and kernel
    from NAND.  (The IP address and path to the NFS is an example and should
    be changed by the user).

    ::

        setenv serverip <ip address of nfs host>
        setenv nfsargs 'setenv bootargs mem=128M console=ttyS0,115200n8 noinitrd rw ip=dhcp root=/dev/nfs nfsroot=${serverip}:/home/user/ti-sdk-AM3715-evm-4.0.0.0/rfs,nolock,rsize=1024,wsize=1024'
        setenv nand_nfs_boot 'run nand_kernel;run nfsargs; bootm ${loadaddr}'
        saveenv
        run nand_nfs_boot

    .. rubric:: Default NAND partitioning (from x-loader)
       :name: default-nand-partitioning-from-x-loader

    | /\* NAND is partitioned:
    | \* 0x00000000 - 0x0007FFFF Booting Image (512k)
    | \* 0x00080000 - 0x0023FFFF U-Boot Image (1.6M)
    | \* 0x00240000 - 0x0027FFFF U-Boot Env Data (256k)
    | \* 0x00280000 - 0x0077FFFF Kernel Image (5M)
    | \* 0x00780000 - 0x08000000 File System

    -  Block size = 0x00020000 (128k)
       \* Page size = 0x00000800 (2k)
       \*/

    |



