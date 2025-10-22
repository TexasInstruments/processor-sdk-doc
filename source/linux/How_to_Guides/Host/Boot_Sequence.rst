
Boot Sequence
====================================

.. ifconfig:: CONFIG_part_family in ('J7_family')

    The J721E boot sequence is shown in the U-boot documentation file for J721E (doc/board/ti/j721e_evm.rst).

    Please refer back to the particular U-boot component branch and version information for this release:
    :ref:`release-specific-build-information`

.. ifconfig:: CONFIG_part_family in ('AM57X_family')

    .. rubric:: Introduction
       :name: introduction-boot-sequence

    This page describes the boot sequence of an OMAP3 and AM57X EVM. In this page, OMAP3 EVM is used for OMAP3 and AM57 EVM.

    .. rubric:: General Boot Sequence (Linux system)
       :name: general-boot-sequence-linux-system

    Boot sequence (in order)

    -  Boot ROM
    -  X-loader
    -  U-boot
    -  Linux

    |

    At power-up an OMAP3 device begins booting from internal Boot ROM.  This
    code is fixed during the manufacturing process and cannot be altered.
    The Boot ROM reads boot configuration pins (SW4 on the OMAP3 EVM) which
    tell the Boot ROM where to look for the first external bootloader.  The
    choices include NAND, UART, and SD/MMC Card.  Control is then passed to
    this first external bootloader called x-loader.  The x-loader
    application is included in the Linux PSP provided by TI and can be
    modified by the end user.  The x-loader application passes control to
    u-boot.  U-boot is also a bootloader and is considered the second
    external bootloader in this case.

    |

    U-boot is the application which passes control to the Linux system.  The
    main goal of u-boot is to retrieve the Linux kernel and provide the
    kernel with information about the location of the Linux filesystem.
    U-boot can be configured to retrieve the kernel from NAND, SD/MMC Card,
    UART or Ethernet (via TFTP).  U-boot can also specify a root filesystem
    that is located in NAND (jffs2), SRAM (ramdisk), SD/MMC card (ext3
    partition) or mounted over IP (NFS).

    |

    U-boot then boots the Linux kernel.  The Linux kernel mounts the Linux
    root filesystem.

    .. rubric::
       Booting TI SDK
       :name: booting-ti-sdk

    The OMAP3 EVM which includes the TI SDK will come with an SD card.  This
    card has been formatted and partition in such a way that the entire
    system comes from this card.  There is a bootable FAT partition which
    contains x-loader (MLO), u-boot (u-boot.bin )and the Linux kernel
    (uImage).  There is a separate ext3 partition which contains the Linux
    root filesystem.

    A tutorial for making this SD card can be found
    `here <http://processors.wiki.ti.com/index.php/How_to_Make_3_Partition_SD_Card>`__:

    The actual file names of the binaries on the FAT partition will be as
    follows:

    +-------------------------+------------------------------+
    | Application or Script   | Actual Filename on SD card   |
    +=========================+==============================+
    | X-loader                | MLO                          |
    +-------------------------+------------------------------+
    | U-boot                  | u-boot.bin                   |
    +-------------------------+------------------------------+
    | Linux kernel            | uImage                       |
    +-------------------------+------------------------------+
    | boot script             | boot.scr                     |
    +-------------------------+------------------------------+

    Table:  Files on boot (FAT) partition of SD card

    |

    When booting from an SD card, the OMAP3 Boot ROM code will search the SD
    card for the filename "MLO" when looking for x-loader.

    To boot from this SD card, the switches on SW4 should be set to SD/MMC
    boot.

    -  **SW4 = 00100111 (high to low, i.e. SW4.1 = 1)**
    -  **1 = "On" position on the switch**

    | A UART terminal application connect to UART 1/2 of the EVM will
      display output as the board boots up.  The first section shows output
      from x-loader as it boots from the SD/MMC card.

    ::

        Texas Instruments X-Loader 1.45 (Mar 19 2010 - 19:44:19)
        Starting X-loader on MMC
        Reading boot sector

        212504 Bytes Read from MMC
        Starting OS Bootloader from MMC...
        Starting OS Bootloader...

    X-loader then passes control to u-boot.  U-boot expects to find
    "environment variables" in NAND flash.  When a board is booted for the
    first time or if the NAND has been erased, u-boot will indicate a
    Warning about bad NAND.  U-boot will write a default environment that it
    will then use to continue the boot process.

    ::

        U-Boot 2023.04-gc1c2bdf272 (Nov 30 2023 - 18:17:44 +0000)

        CPU  : DRA752-GP ES2.0
        Model: TI AM5728 BeagleBoard-X15
        Board: AM572x EVM REV A.3A
        DRAM:  2 GiB
        Core:  65 devices, 21 uclasses, devicetree: separate
        MMC:   OMAP SD/MMC: 0, OMAP SD/MMC: 1
        *** Warning - bad env area, using default environment

        Net:   eth2: ethernet@48484000
        Hit any key to stop autoboot:  0

    The default environment is designed to boot the Linux system from the SD
    card, so it is not necessary to stop the boot process.  And the next
    time that the EVM is booted the default environment will exist in NAND
    so the "bad NAND" warning will not be displayed.

    U-boot allows the user a 2-3 seconds window to stop the boot process.
    Hit any key in the UART terminal application and the u-boot prompt will
    be displayed as shown below:

    ::

        OMAP3_EVM #

    There are several useful commands to remember here.  To display the
    environment variables, type "**printenv**" or just "**pri**".

    ::

        OMAP3_EVM #
        OMAP3_EVM # printenv
        bootcmd=if mmc init; then if run loadbootscript; then run bootscript; else if run loaduimage; then run mmcboot; else run nandboot; f
        i; fi; else run nandboot; fi
        bootdelay=2
        baudrate=115200
        bootfile=uImage
        loadaddr=0x82000000
        usbtty=cdc_acm
        console=ttyS0,115200n8
        mmcargs=setenv bootargs console=${console} root=/dev/mmcblk0p2 rw rootfstype=ext3 rootwait
        nandargs=setenv bootargs console=${console} root=/dev/mtdblock4 rw rootfstype=jffs2
        loadbootscript=fatload mmc 0 ${loadaddr} boot.scr
        bootscript=echo Running bootscript from mmc ...; source ${loadaddr}
        loaduimage=fatload mmc 0 ${loadaddr} uImage
        mmcboot=echo Booting from mmc ...; run mmcargs; bootm ${loadaddr}
        nandboot=echo Booting from nand ...; run nandargs; onenand read ${loadaddr} 280000 400000; bootm ${loadaddr}
        stdin=serial
        stdout=serial
        stderr=serial
        dieid#=731c0000000000000156087c0a023021
        ethact=smc911x-0

        Environment size: 873/131068 bytes
        OMAP3_EVM #

    | The environment variables shown above are the default variables that
      are included with u-boot from the TI SDK.  These will be re-written
      any time that the NAND is erased, but otherwise these variables stay
      in NAND and can be modified to change how Linux is booted.

    | To continue the boot from u-boot, simply type "**boot**" and the
      process will continue as if you did not stop the boot by hitting a
      key.  This is also equivalent to typing "**run bootcmd**".  The
      **bootcmd** environment variable is actually a sequence of conditional
      statements (separated by semicolons) which perform checks on the
      hardware and software to complete the boot process.

    ::

        OMAP3_EVM # boot
        ## Booting kernel from Legacy Image at 80000000 ...
        Image Name: Linux-2.6.32
        Image Type: ARM Linux Kernel Image (uncompressed)
        Data Size: 2396212 Bytes = 2.3 MB
        Load Address: 80008000
        Entry Point: 80008000
        Verifying Checksum ... OK
        Loading Kernel Image ... OK
        OK

        Starting kernel ...

        Uncompressing Linux.....................................................................................................
        .................................................. done, booting the kernel.

    | Then there will be a lot of messages from the kernel before getting to
      the Linux login prompt.  Just type "root" at the login prompt

    ::

        dm3730-am3715-evm login:

    |

    .. rubric:: Closer Look At bootcmd
       :name: closer-look-at-bootcmd

    The bootcmd environment variable is a set of nested conditional
    statements.

    |

    ::

        bootcmd=if mmc init; then if run loadbootscript; then run bootscript; else if run loaduimage; then run mmcboot; else run nandboot; f
        i; fi; else run nandboot; fi

    | The first conditional "**if mmc init**" checks to see if the SD/MMC
      card exists.  If the card exists, the next conditional "**if run
      loadbootscript**" checks to see if the bootscript boot.scr exists on
      the SD card.  If the boot script exists, then it is executed.  The
      boot script contains the boot arguments and the command to actually
      boot the Linux kernel.  So if the bootscript exists and is executed,
      it should not return to rest of the bootcmd.

