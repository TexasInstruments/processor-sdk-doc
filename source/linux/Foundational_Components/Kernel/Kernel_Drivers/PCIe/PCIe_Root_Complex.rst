.. http://processors.wiki.ti.com/index.php/Linux_Core_PCIE_User%27s_Guide

PCIe Root Complex
---------------------------------

.. rubric:: Introduction
   :name: introduction-linux-pcie-rc

The PCI Express (PCIe) module is a multi-lane I/O interconnect providing
low pin count, high reliability, and high-speed data transfer at rates
of up to 8.0 Gbps per lane per direction. It is a 3rd Generation I/O Interconnect
technology succeeding ISA and PCI bus that is designed to be used as a
general-purpose serial I/O interconnect in multiple market segments,
including desktop, mobile, server, storage and embedded communications.

.. ifconfig:: CONFIG_part_family in ('General_family')

    .. rubric:: Keystone PCIe
       :name: keystone-pcie

    Keystone PCIe module is used on K2H/K2K, K2E, K2L and K2G SoCs. For more
    details on the module specification, please refers to sprugs6d.pdf
    documentation provided at ti.com. The K2G PCIe module spec is part of
    spruhy8d.pdf.

    .. rubric:: Supported platforms
       :name: supported-platforms

    SoCs: K2E, K2G

    Keystone PCIe driver may be used on K2L/K2HK and boards/EVMs using these
    SoCs, but is not validated since nothing is hooked to PCIe port on these
    EVMs.

    K2E EVM has a Marvel SATA controller (88se9182) hooked to PCIe port 1.
    The Driver is validated by connecting a SATA hard disk to the SATA port
    available on the EVM. K2G EVM has a single x1 PCIe slot which accepts
    standard PCIe cards. Following PCIe cards are validated for basic
    functionality on K2G EVM:-

    ::

        * Ethernet: Broadcom Corporation NetXtreme BCM5721 Gigabit (tg3 driver)
        * Intel Corporation 82572EI Gigabit Ethernet (e1000e driver)
        * USB: Texas Instruments TUSB73x0 SuperSpeed USB 3.0 xHCI Host
        * SATA: Marvell Technology Group Ltd. 88SE9120 SATA 6Gb/s

    K2G EVM: Make sure following jumper settings on the EVM:-

    ::

        * J44: put stub to short pin 1 & 2. This ensure proper reset to PCIe slot
        * J15: put stub to short pin 2 & 3. This ensures 100MHz clock to PCIe slot

    |

    .. rubric:: Introduction to PCIe on TI Keystone platforms
       :name: introduction-linux-pcie

    The TI Keystone platforms contain a PCI Express module which supports a
    multi-lane I/O interconnect providing low pin count, high reliability,
    and high-speed data transfer at rates of up to 5.0 Gbps per lane per
    direction, The module supports Root Complex and End Point operation
    modes.

    The PCIe driver implemented supports only the Root Complex (RC)
    operation mode on K2 platforms (K2HK, K2E). The PCIe driver is designed
    based on PCIE Designware Core driver. The Designware Core driver is
    enhanced to support Keystone PCIe driver in the mainline kernel. The
    diagram below shows the various drivers that Keystone PCI depends on to
    implement the RC driver. PCI Designware Core driver provides a set of
    function calls defined in drivers/pci/host/pcie-designware.h for
    platform drivers to implement the RC driver. Keystone PCI module
    required some enhancements to designware core because of the application
    register space which otherwise is part of the designware core. These
    keystone specific handling of the driver is re-factored into PCI
    Keystone DW Core Driver and used from PCI Keystone platform driver. This
    includes MSI/Legacy IRQ handling, Read/Write functions to write over the
    PCI bus etc which are unique for Keystone PCI driver.

    ::

                             Callbacks
         |------------------|       |--------------------|       |---------------------|       |---------------|
         | PCI Keystone     |<------| PCI Keystone DW    |<------| PCI Designware Core |       |               |
         | Platform Driver  |------>| Core Driver        |------>| Driver              |-------|  PCI Core     |
         | (pci-keystone.c) |       | pci-keystone-dw.c  |       | pcie-designware.c   |       |               |
         |------------------|       |--------------------|       |---------------------|       |---------------|
                            function calls              function calls

    |
    | PCIe has been verified on K2E EVM. K2E supports two PCI ports. Port 0
      is on Domain 0 and Port 1 is on Domain 1. On K2E EVM, a Marvel SATA
      controller, 0x9182 is connected to port 1 that supports interfacing
      with Hard disk drives (HDD). Following h/w setup is used to test SATA
      HDD interface with K2E. Western Digital 1.0 TB SATA / 64MB Cache hard
      disk drive, WD10EZEX is used for the test over PCI port 1.

    |

    ::

         -----------     SATA 6Gbps data cable    ------------
         | WD10EZEX | --------------------------> |  K2E EVM |
         -----------                              ------------
               ^
               |
        (External power supply)

    Connect HDD to an external power supply. Connect the HDD SATA port to
    K2E EVM SATA port using a 6Gbps data cable and power on the HDD. Power
    On K2E EVM. The K2E rev 1.0.2.0 requires a hardware modification to get
    the SATA detection on the PCI bus. Please check with EVM hardware vendor
    for the details.

    For K2G EVM, there is a PCIe slot available to work with standard PCIe
    cards. For example to test PCIe SATA as in K2E, connect the hard disk
    SATA cables to the PCIe SATA controller card and insert the card into
    the PCIe slot and Power on the EVM. Other PCIe cards can be tested in a
    similar way.

    .. rubric:: Driver Configuration
       :name: driver-configuration-pcierc

    Assume, you have default configuration set for kernel build. To enable
    PCI Keystone driver, traverse the following config tree from menuconfig

    ::

             Bus support  --->
                     [*] PCI support
                     [*] Message Signaled Interrupts (MSI and MSI-X)
                     [ ] PCI Debugging
                     [ ] Enable PCI resource re-allocation detection
                     ......
                     PCI host controller drivers  --->
                                 [ ] Generic PCI host controller
                                 [*] TI Keystone PCIe controller

    The RC driver can be built into the kernel as a static module.

    |

    .. rubric:: Device Tree bindings
       :name: device-tree-bindings

    DT documentation is at
    Documentation/devicetree/bindings/pci/pci-keystone.txt in the kernel
    source tree. The PCIE SerDes Phy related DT documentation is available
    at Documentation/devicetree/bindings/phy/ti-phy.txt

    |

    .. rubric:: Driver Source location
       :name: driver-source-location

    The driver code is located at drivers/pci/host

    ::

        Files: pci-keystone.c
               pci-keystone-dw.c
               pci-keystone.h

    |
    | The PCIe PHY (SerDes) contains the analog portion of the PHY, which is
      the transmission line channel that is used to transmit and receive
      data. It contains a phase locked loop, analog transceiver, phase
      interpolator-based clock/data recovery, parallel-to-serial converter,
      serial-to-parallel converter, scrambler, configuration, and test
      logic.

    PCI driver calls into Phy SerDes driver to initialize PCI Phy (SerDes).
    From PCI probe function, phy\_init() is called which results in SerDes
    initialization. The SerDes code is a common driver used across all sub
    systems such as SGMII, PCIe and 10G. The driver code for this located at
    drivers/phy/phy-keystone-serdes.c

    .. rubric:: Limitations
       :name: limitations

    -  PCIe is verified only on K2E and K2G EVMs
    -  AER error interrupt is not handled by PCIE AER driver for Keystone as
       this uses non standard platform interrupt
    -  ASPM interrupt is non standard on Keystone and the same is not
       handled by the PCIe ASPM driver.

    |

    .. rubric:: U-Boot environment/scripts
       :name: u-boot-environmentscripts

    The Keystone PCIe SerDes Phy hardware requires a firmware to configure
    the Phy to work as a PCIe phy. As Keystone PCIe is statically built into
    the kernel, this firmware is needed when Phy SerDes driver is probed.
    When initramfs is used as the final rootfs, this firmware can reside at
    /lib/firmware folder of the fs. For other boot modes (mmc, ubi, nfs),
    k2-fw-initrd.cpio.gz has this firmware and can be loaded to memory and
    the address is passed to kernel through second argument of bootm
    command. Following env scripts are used to customize the u-boot
    environment for various boot modes so that firmware is available to
    initialize the phy SerDes when Phy SerDes driver is probed.

    firmware file ks2\_pcie\_serdes.bin is available in
    ti-linux-firmware.git at ti-keystone folder or at /lib/firmware folder
    of the file system images shipped with the release or under /lib/firmare
    folder of the k2-fw-initrd.cpio.gz shipped with the release). If you are
    using your own file system, make sure ks2\_pcie\_serdes.bin resides at
    /lib/firmware folder.

    Setup u-boot env as follows. These are expected to be available in the
    default env variable, but check and update it if not present.

    |
    | Update init\_\* variables

    ::

        setenv init_fw_rd_mmc 'load mmc ${bootpart} ${rdaddr} ${bootdir}/${name_fw_rd}; run set_rd_spec'
        setenv init_fw_rd_net 'dhcp ${rdaddr} ${tftp_root}/${name_fw_rd}; run set_rd_spec'
        setenv init_fw_rd_ramfs 'setenv rd_spec - '
        setenv init_fw_rd_ubi 'ubifsload ${rdaddr} ${bootdir}/${name_fw_rd}; run set_rd_spec'
        setenv set_rd_spec 'setenv rd_spec ${rdaddr}:${filesize}'
        setenv name_fw_rd 'k2-fw-initrd.cpio.gz'

    Add init\_fw\_rd\_${boot} to bootcmd.

    ::

        setenv bootcmd 'run envboot; run set_name_pmmc init_${boot} init_fw_rd_${boot} get_pmmc_${boot} run_pmmc get_fdt_${boot} get_mon_${boot} get_kern_${boot} run_mon run_kern'

    |

    .. rubric:: Procedure to boot Linux with FS on hard disk
       :name: procedure-to-boot-linux-with-fs-on-hard-disk

    .. rubric:: Enable AHCI, ATA drivers
       :name: enable-ahci-ata-drivers

    Assume, you have default configuration set for kernel build. Both AHCI
    and ATA drivers are to be enabled to build statically into the kernel
    image if rootfs is mounted from the hard disk. Otherwise, if hard disk
    is used as a storage device, the below drivers can be built as dynamic
    modules and loaded from user space.

    From Kernel menuconfig, traverse the configuration tree as follows:-

    ::

         Device Drivers  --->
                      ---------
                 < > ATA/ATAPI/MFM/RLL support (DEPRECATED)  ----
                     SCSI device support  --->
                     <*> Serial ATA and Parallel ATA drivers (libata)  --->
                                           *** Controllers with non-SFF native interface ***
                                     <*>   AHCI SATA support
                                     <*>   Platform AHCI SATA support
                                     < >   CEVA AHCI SATA support
                                     -----------------
                                           *** Generic fallback / legacy drivers ***
                                     <*>   Generic ATA support
                                     < >   Legacy ISA PATA support (Experimental)
                     [ ] Multiple devices driver support (RAID and LVM)  ----


    Boot Linux kernel on K2E EVM using NFS file system or Ramfs and using
    rootfs provided in the SDK. Make sure SATA HDD is connected to EVM as
    explained above and SATA EP is detected during boot up. This example
    uses a 1TB HDD and create two partition. First partition is for
    filesystem and is 510GB and second is for swap and is 256MB.

    |

    .. rubric:: Create partition with fdisk
       :name: create-partition-with-fdisk

    First step is to create 2 partitions using fdisk command. At Linux
    console type the following commands

    ::

        root@keystone-evm:~# fdisk /dev/sda
        Welcome to fdisk (util-linux 2.21.2).

        Changes will remain in memory only, until you decide to write them.
        Be careful before using the write command.

    ::

        Device does not contain a recognized partition table
        Building a new DOS disklabel with disk identifier 0x9b51b66e.

        The device presents a logical sector size that is smaller than
        the physical sector size. Aligning to a physical sector (or optimal
        I/O) size boundary is recommended, or performance may be impacted.

        Command (m for help): m
        Command action
           a   toggle a bootable flag
           b   edit bsd disklabel
           c   toggle the dos compatibility flag
           d   delete a partition
           l   list known partition types
           m   print this menu
           n   add a new partition
           o   create a new empty DOS partition table
           p   print the partition table
           q   quit without saving changes
           s   create a new empty Sun disklabel
           t   change a partition's system id
           u   change display/entry units
           v   verify the partition table
           w   write table to disk and exit
           x   extra functionality (experts only)

        Command (m for help): n
        Partition type:
           p   primary (0 primary, 0 extended, 4 free)
           e   extended
        Select (default p): p
        Partition number (1-4, default 1): 1
        First sector (2048-1953525167, default 2048): 2048
        Last sector, +sectors or +size{K,M,G} (2048-1953525167, default 1953525167): +510G
        Partition 1 of type Linux and of size 510 GiB is set

    ::

        Command (m for help): n
        Partition type:
           p   primary (1 primary, 0 extended, 3 free)
           e   extended
        Select (default p): p
        Partition number (1-4, default 2): 2
        First sector (1069549568-1953525167, default 1069549568):
        Using default value 1069549568
        Last sector, +sectors or +size{K,M,G} (1069549568-1953525167, default 1953525167): +256M
        Partition 2 of type Linux and of size 256 MiB is set

    ::

        Command (m for help): p

    ::

        Disk /dev/sda: 1000.2 GB, 1000204886016 bytes
        255 heads, 63 sectors/track, 121601 cylinders, total 1953525168 sectors
        Units = sectors of 1 * 512 = 512 bytes
        Sector size (logical/physical): 512 bytes / 4096 bytes
        I/O size (minimum/optimal): 4096 bytes / 4096 bytes
        Disk identifier: 0x9b51b66e
           Device Boot      Start         End      Blocks   Id  System
        /dev/sda1            2048  1069549567   534773760   83  Linux
        /dev/sda2      1069549568  1070073855      262144   83  Linux

    ::

        Command (m for help): p

    ::

        Disk /dev/sda: 1000.2 GB, 1000204886016 bytes
        255 heads, 63 sectors/track, 121601 cylinders, total 1953525168 sectors
        Units = sectors of 1 * 512 = 512 bytes
        Sector size (logical/physical): 512 bytes / 4096 bytes
        I/O size (minimum/optimal): 4096 bytes / 4096 bytes
        Disk identifier: 0x9b51b66e

          Device Boot      Start         End      Blocks   Id  System
        /dev/sda1            2048  1069549567   534773760   83  Linux
        /dev/sda2      1069549568  1070073855      262144   83  Linux

        Command (m for help): t
        Partition number (1-4): 2
        Hex code (type L to list codes): L

         0  Empty           24  NEC DOS         81  Minix / old Lin bf  Solaris
         1  FAT12           27  Hidden NTFS Win 82  Linux swap / So c1  DRDOS/sec (FAT-
         2  XENIX root      39  Plan 9          83  Linux           c4  DRDOS/sec (FAT-
         3  XENIX usr       3c  PartitionMagic  84  OS/2 hidden C:  c6  DRDOS/sec (FAT-
         4  FAT16 <32M      40  Venix 80286     85  Linux extended  c7  Syrinx
         5  Extended        41  PPC PReP Boot   86  NTFS volume set da  Non-FS data
         6  FAT16           42  SFS             87  NTFS volume set db  CP/M / CTOS / .
         7  HPFS/NTFS/exFAT 4d  QNX4.x          88  Linux plaintext de  Dell Utility
         8  AIX             4e  QNX4.x 2nd part 8e  Linux LVM       df  BootIt
         9  AIX bootable    4f  QNX4.x 3rd part 93  Amoeba          e1  DOS access
         a  OS/2 Boot Manag 50  OnTrack DM      94  Amoeba BBT      e3  DOS R/O
         b  W95 FAT32       51  OnTrack DM6 Aux 9f  BSD/OS          e4  SpeedStor
         c  W95 FAT32 (LBA) 52  CP/M            a0  IBM Thinkpad hi eb  BeOS fs
         e  W95 FAT16 (LBA) 53  OnTrack DM6 Aux a5  FreeBSD         ee  GPT
         f  W95 Ext'd (LBA) 54  OnTrackDM6      a6  OpenBSD         ef  EFI (FAT-12/16/
        10  OPUS            55  EZ-Drive        a7  NeXTSTEP        f0  Linux/PA-RISC b
        11  Hidden FAT12    56  Golden Bow      a8  Darwin UFS      f1  SpeedStor
        12  Compaq diagnost 5c  Priam Edisk     a9  NetBSD          f4  SpeedStor
        14  Hidden FAT16 <3 61  SpeedStor       ab  Darwin boot     f2  DOS secondary
        16  Hidden FAT16    63  GNU HURD or Sys af  HFS / HFS+      fb  VMware VMFS
        17  Hidden HPFS/NTF 64  Novell Netware  b7  BSDI fs         fc  VMware VMKCORE
        18  AST SmartSleep  65  Novell Netware  b8  BSDI swap       fd  Linux raid auto
        1b  Hidden W95 FAT3 70  DiskSecure Mult bb  Boot Wizard hid fe  LANstep
        1c  Hidden W95 FAT3 75  PC/IX           be  Solaris boot    ff  BBT
        1e  Hidden W95 FAT1 80  Old Minix
        Hex code (type L to list codes): 82
        Changed system type of partition 2 to 82 (Linux swap / Solaris)

        Command (m for help): p

        Disk /dev/sda: 1000.2 GB, 1000204886016 bytes
        255 heads, 63 sectors/track, 121601 cylinders, total 1953525168 sectors
        Units = sectors of 1 * 512 = 512 bytes
        Sector size (logical/physical): 512 bytes / 4096 bytes
        I/O size (minimum/optimal): 4096 bytes / 4096 bytes
        Disk identifier: 0x9b51b66e

         Device Boot      Start         End      Blocks   Id  System
        /dev/sda1            2048  1069549567   534773760   83  Linux
        /dev/sda2      1069549568  1070073855      262144   82  Linux swap / Solaris

    |

    .. rubric:: Format partitions
       :name: format-partitions

    ::

        root@k2e-evm~# mkfs.ext4 /dev/sda1
        mke2fs 1.42.1 (17-Feb-2012)
        Filesystem label=
        OS type: Linux
        Block size=4096 (log=2)
        Fragment size=4096 (log=2)
        Stride=0 blocks, Stripe width=0 blocks
        33423360 inodes, 133693440 blocks
        6684672 blocks (5.00%) reserved for the super user
        First data block=0
        Maximum filesystem blocks=0
        4080 block groups
        32768 blocks per group, 32768 fragments per group
        8192 inodes per group
        Superblock backups stored on blocks:
               32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
               4096000, 7962624, 11239424, 20480000, 23887872, 71663616, 78675968,
               102400000

    ::

        Allocating group tables: done
        Writing inode tables: done
        Creating journal (32768 blocks): done
        Writing superblocks and filesystem accounting information: done

        root@k2e-evm:~# ls -ltr /dev/sda*
        brw-rw----    1 root     disk        8,   2 Sep 21 14:37 /dev/sda2
        brw-rw----    1 root     disk        8,   0 Sep 21 14:37 /dev/sda
        brw-rw----    1 root     disk        8,   1 Sep 21 14:40 /dev/sda1

    .. rubric:: Copy filesystem to rootfs
       :name: copy-filesystem-to-rootfs

    This procedure assumes the cpio file for SDK filesystem is available on
    the NFS or ramfs.

    ::

        >mkdir /mnt/test
        >mount -t ext4 /dev/sda1 /mnt/test
        >cd /mnt/test
        >cpio -i -v </<rootfs>.cpio
        >cd /
        >umount /mnt/test

    Where rootfs.cpio is the cpio file for the SDK fileystem.

    |

    .. rubric:: Booting with FS on harddisk
       :name: booting-with-fs-on-harddisk

    Once the harddisk is formatted and has a rootfs installed, following
    procedure can be used to boot Linux kernel using this rootfs.

    Boot EVM to u-boot prompt. Add following env variables to u-boot
    environment :-

    ::

        K2E EVM # setenv boot hdd
        K2E EVM # setenv get_fdt_hdd 'dhcp ${fdtaddr} ${tftp_root}/${name_fdt}'
        K2E EVM # setenv init_fw_rd_hdd 'dhcp ${rdaddr} ${tftp_root}/${name_fw_rd}; run set_rd_spec'
        K2E EVM # setenv get_kern_hdd 'dhcp ${loadaddr} ${tftp_root}/${name_kern}'
        K2E EVM # setenv get_mon_hdd 'dhcp ${addr_mon} ${tftp_root}/${name_mon}'
        K2E EVM # setenv init_hdd 'run args_all  args_hdd'
        K2E EVM # setenv args_hdd 'setenv bootargs ${bootargs} rw root=/dev/sda1'
        K2E EVM # saveenv

    Now type boot command and boot to Linux. The above steps can be skipped
    once u-boot implements these env variables by default which is expected
    to be supported in the future.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

    .. rubric:: **Features of AM64**
       :name: features-am64-linux-pcie-ep

    There is one instance of the PCIe subsystem. Following are some of the
    main features:

    - The instance can be configured to operate in Root Complex mode or
      End Point mode

    - One lane configuration, capable up to 5.0 Gbps/lane (Gen2)

    - Support for Legacy, MSI and MSI-X Interrupt

    - There can be 32 different address mappings in outbound address translation
      unit. The mappings can be from regions reserved for each PCIe instance.

      - For instance PCIE0, there are two regions in SoC Memory Map:

        - 128 MB region with address in lower 32 bits

        - 4 GB region with address above 32 bits

    .. rubric:: **Capabilities of AM64 EVM**
       :name: capabilities-am64-evm-pcie-rc

    Following are some of the details for PCIE0 instance:

    +------------------------+-------------------+------------------------------------+
    | Instance               | Supported lanes   | Supported Connector                |
    +========================+===================+====================================+
    | PCIE0                  | 1 lane            | Standard female connector          |
    +------------------------+-------------------+------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J721E')

    .. rubric:: **Features of J7ES**
       :name: features-j7es-linux-pcie-ep

    There are four instances of the PCIe subsystem. Following are some of the
    main features:

    - Each instance can be configured to operate in Root Complex mode or
      End Point mode

    - One or two lane configuration, capable up to 8.0 Gbps/lane (Gen3)

    - Support for Legacy, MSI and MSI-X Interrupt

    - There can be 32 different address mappings in outbound address translation
      unit. The mappings can be from regions reserved for each PCIe instance.

      - For instance PCIE0 and PCIE1, there are two regions in SoC Memory Map:

        - 128 MB region with address in lower 32 bits

        - 4 GB region with address above 32 bits

      - For instance PCIE2 and PCIE3, there are two regions in SoC Memory Map:

        - 128 MB region with address above 32 bits

        - 4 GB region with address above 32 bits

    .. rubric:: **Capabilities of J721E EVM**
       :name: capabilities-j721e-evm-pcie-rc

    There are three instances of the PCIe subsystem on the EVM. Following are
    some of the details for each instance:

    +------------------------+-------------------+------------------------------------+
    | Instance               | Supported lanes   | Supported Connector                |
    +========================+===================+====================================+
    | PCIE0                  | 1 lane            | Standard female connector          |
    +------------------------+-------------------+------------------------------------+
    | PCIE1                  | 2 lane            | Standard female connector          |
    +------------------------+-------------------+------------------------------------+
    | PCIE2                  | 2 lane            | m.2 connector keyed for SSD (M key)|
    +------------------------+-------------------+------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM64X','J721E')

    .. rubric:: **Hardware Setup Details**
       :name: hardware-setup-details

    |__PART_FAMILY_DEVICE_NAMES__| is, by default, intended to be operated in
    Root Complex mode.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

    Refer to the following image to toggle between Root Complex mode and End Point mode.

    .. Image:: /images/am64-pcie-rc-ep-sel.png


.. ifconfig:: CONFIG_part_variant in ('J721E')

    For End Point mode, PCIE_1L_MODE_SEL (switch 5) and PCIE_2L_MODE_SEL (switch 6)
    should be set to '0'.

    .. Image:: /images/dip-switch.png

.. rubric:: **RC Software Architecture**
   :name: rc-software-architecture

Following is the software architecture for Root Complex mode:

.. Image:: /images/Linux_PCIe_subsystem.png

Following is a brief explanation of layers shown in the diagram:

- There are different drivers for the connected PCIe devices like
  pci_endpoint_test, tg-3, r8169, xhci-pci, ahci, etc. It could be
  vendor-specific like most of the ethernet cards (tg3, r8169) or class-specific
  like xhci-pci and ahci. Each of these drivers will also interact with it's own
  domain-specific stack. For example, tg3 will interface with network stack, and
  xhci-pci will interface with USB stack.

- The PCI core layer scans the PCIe bus to identify and detect any PCIe devices.
  It also binds the driver from the layer above, for the PCIe device, based on
  vendorid, deviceid and class.

- The PCI BIOS layer handles resource management. For example, allocation of
  memory resources for BARs.

- The bottom-most layer consists of the PCIe platform drivers like pcie-cadence,
  pcie-designware, etc. pci-j721e and pci-dra7xx are TI's wrappers over these
  drivers. They configure platform-specific controllers and perform
  actual register writes.

.. ifconfig:: CONFIG_part_family in ('AM64X_family','J7_family')

    .. rubric:: **RC Device Configuration**
       :name: rc-device-configuration

    .. rubric:: *DTS Modification*
       :name: rc-dts-modification

    The default dts for |__PART_FAMILY_DEVICE_NAMES__| is configured to be used in
    root complex mode.

    .. rubric:: *Linux Driver Configuration*
       :name: linux-driver-configuration

    The following config options have to be enabled in order to configure the
    PCI controller to be used in Root Complex mode.

    ::

        CONFIG_SOCIONEXT_SYNQUACER_PREITS=y
        CONFIG_PCI=y
        CONFIG_PCI_MSI=y
        CONFIG_PCI_J721E=y
        CONFIG_PCIE_CADENCE=y
        CONFIG_PCIE_CADENCE_HOST=y

    .. rubric:: **Compliance Mode**
        :name: compliance-mode

    In RC mode of operation, the Endpoint device can be forced to enter
    Compliance Mode for PCIe compliance testing by setting the "EC" bit
    in the LINK_CTRL_STATUS_2 register of the respective PCIe RC instance.
    Setting "EC" to 1 initiates a hot reset thereby forcing the Endpoint
    device into Compliance mode. The "EC" bit can be set from command-line
    by using devmem2 utility as follows:

        devmem2 <address> w <value>

    where <address> is the address of LINK_CTRL_STATUS_2 register and
    <value> is the resulting value to be written with "EC" bit of the
    register set.

    .. rubric:: **Testing Details**
       :name: testing-details

    The RC should enumerate any off-the-shelf PCIe cards. It has been tested
    with Ethernet cards, NVMe cards, PCIe USB card, PCIe WiFi card, PCIe SATA
    card and also to |__PART_FAMILY_DEVICE_NAMES__| in loopback mode.

    In order to see if the connected card is detected, lspci utility should be
    used. Different utilities can be used depending on the cards.

    Following are the outputs for some of them:

    - Loopback mode (|__PART_FAMILY_DEVICE_NAMES__| EVM to |__PART_FAMILY_DEVICE_NAMES__| EVM)

      Two |__PART_FAMILY_DEVICE_NAMES__| EVMs can be connected in loopback mode by following
      the steps explained in
      `End Point (EP) Device Configuration <PCIe_End_Point.html#ep-device-configuration>`_
      section for End Point (EP) and
      `HOST Device Configuration <PCIe_End_Point.html#host-device-configuration>`_
      section for Root Complex (RC) in
      `PCIe End Point documentation. <PCIe_End_Point.html>`_ The pci-epf-test
      driver will be configured for End Point(EP) using those steps.

      The lspci output on the Root Complex (RC) device is as follows:

.. ifconfig:: CONFIG_part_family in ('AM64X_family')

      ::

          root@am64xx-evm:~# lspci
          0000:00:00.0 PCI bridge: Texas Instruments Device b010
          0000:01:00.0 Unassigned class [ff00]: Texas Instruments Device b010

    -  WiFi card

        - lspci output

        ::

            root@am64xx-evm:~# lspci
            0000:00:00.0 PCI bridge: Texas Instruments Device b010
            0000:01:00.0 Network controller: Intel Corporation Wireless 3160 (rev 6b)

        - Test using ping

        ::

            root@am64xx-evm:~# ping 192.168.10.1 -w 10|
            PING 192.168.10.1 (192.168.10.1): 56 data bytes
            64 bytes from 192.168.10.1: seq=0 ttl=64 time=176.985 ms
            64 bytes from 192.168.10.1: seq=1 ttl=64 time=49.840 ms
            64 bytes from 192.168.10.1: seq=2 ttl=64 time=32.125 ms
            64 bytes from 192.168.10.1: seq=3 ttl=64 time=4.652 ms
            64 bytes from 192.168.10.1: seq=4 ttl=64 time=70.805 ms
            64 bytes from 192.168.10.1: seq=6 ttl=64 time=195.564 ms
            64 bytes from 192.168.10.1: seq=7 ttl=64 time=9.321 ms
            64 bytes from 192.168.10.1: seq=8 ttl=64 time=5.784 ms
            64 bytes from 192.168.10.1: seq=9 ttl=64 time=18.015 ms

    -  NVMe SSD

        - lspci output

        ::

            root@am64xx-evm:~# lspci -vv
            00:00.0 PCI bridge: Texas Instruments Device b010 (prog-if 00 [Normal decode])
                Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
                Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
                Latency: 0
                Interrupt: pin A routed to IRQ 44
                Region 0: Memory at <unassigned> (64-bit, prefetchable)
                Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
                I/O behind bridge: [disabled]
                Memory behind bridge: 68100000-681fffff [size=1M]
                Prefetchable memory behind bridge: [disabled]
                Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
                BridgeCtl: Parity- SERR+ NoISA- VGA- VGA16- MAbort- >Reset- FastB2B-
                        PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
                Capabilities: [80] Power Management version 3
                        Flags: PMEClk- DSI- D1+ D2- AuxCurrent=0mA PME(D0+,D1+,D2-,D3hot+,D3cold-)
                        Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
                Capabilities: [90] MSI: Enable+ Count=1/1 Maskable+ 64bit+
                        Address: 0000000001000000  Data: 0000
                        Masking: 00000000  Pending: 00000000
                Capabilities: [b0] MSI-X: Enable- Count=1 Masked-
                        Vector table: BAR=0 offset=00000000
                        PBA: BAR=0 offset=00000008
                Capabilities: [c0] Express (v2) Root Port (Slot+), MSI 00
                        DevCap: MaxPayload 128 bytes, PhantFunc 0
                                ExtTag- RBE+
                        DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                                RlxdOrd+ ExtTag- PhantFunc- AuxPwr- NoSnoop+
                                MaxPayload 128 bytes, MaxReadReq 512 bytes
                        DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
                        LnkCap: Port #0, Speed 5GT/s, Width x1, ASPM L1, Exit Latency L1 <8us
                                ClockPM- Surprise- LLActRep- BwNot+ ASPMOptComp+
                        LnkCtl: ASPM Disabled; RCB 64 bytes Disabled- CommClk-
                                ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                        LnkSta: Speed 5GT/s (ok), Width x1 (ok)
                                TrErr- Train- SlotClk- DLActive- BWMgmt- ABWMgmt+
                        SltCap: AttnBtn- PwrCtrl- MRL- AttnInd- PwrInd- HotPlug- Surprise-
                                Slot #0, PowerLimit 0.000W; Interlock- NoCompl-
                        SltCtl: Enable: AttnBtn- PwrFlt- MRL- PresDet- CmdCplt- HPIrq- LinkChg-
                                Control: AttnInd Off, PwrInd Off, Power+ Interlock-
                        SltSta: Status: AttnBtn- PowerFlt- MRL+ CmdCplt- PresDet- Interlock-
                                Changed: MRL- PresDet- LinkState-
                        RootCap: CRSVisible-
                        RootCtl: ErrCorrectable- ErrNon-Fatal- ErrFatal- PMEIntEna+ CRSVisible-
                        RootSta: PME ReqID 0000, PMEStatus- PMEPending-
                        DevCap2: Completion Timeout: Range B, TimeoutDis+, NROPrPrP-, LTR+
                                 10BitTagComp-, 10BitTagReq-, OBFF Via message, ExtFmt+, EETLPPrefix+, MaxEETLPPrefixes 1
                                 EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                                 FRS-, LN System CLS Not Supported, TPHComp-, ExtTPHComp-, ARIFwd-
                                 AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                        DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR+, OBFF Disabled ARIFwd-
                                 AtomicOpsCtl: ReqEn- EgressBlck-
                        LnkCtl2: Target Link Speed: 5GT/s, EnterCompliance- SpeedDis-
                                 Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                                 Compliance De-emphasis: -6dB
                        LnkSta2: Current De-emphasis Level: -6dB, EqualizationComplete-, EqualizationPhase1-
                                 EqualizationPhase2-, EqualizationPhase3-, LinkEqualizationRequest-
                Capabilities: [100 v2] Advanced Error Reporting
                        UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                        UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                        UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                        CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
                        CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
                        AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                                MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
                        HeaderLog: 00000000 00000000 00000000 00000000
                        RootCmd: CERptEn- NFERptEn- FERptEn-
                        RootSta: CERcvd- MultCERcvd- UERcvd- MultUERcvd-
                                 FirstFatal- NonFatalMsg- FatalMsg- IntMsg 0
                        ErrorSrc: ERR_COR: 0000 ERR_FATAL/NONFATAL: 0000
                Capabilities: [150 v1] Device Serial Number 00-00-00-00-00-00-00-00
                Capabilities: [300 v1] Secondary PCI Express
                        LnkCtl3: LnkEquIntrruptEn-, PerformEqu-
                        LaneErrStat: 0
                Capabilities: [4c0 v1] Virtual Channel
                        Caps:   LPEVC=0 RefClk=100ns PATEntryBits=1
                        Arb:    Fixed- WRR32- WRR64- WRR128-
                        Ctrl:   ArbSelect=Fixed
                        Status: InProgress-
                        VC0:    Caps:   PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                                Arb:    Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                                Ctrl:   Enable+ ID=0 ArbSelect=Fixed TC/VC=ff
                                Status: NegoPending- InProgress-
                        VC1:    Caps:   PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                                Arb:    Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                                Ctrl:   Enable- ID=1 ArbSelect=Fixed TC/VC=00
                                Status: NegoPending- InProgress-
                        VC2:    Caps:   PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                                Arb:    Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                                Ctrl:   Enable- ID=2 ArbSelect=Fixed TC/VC=00
                                Status: NegoPending- InProgress-
                        VC3:    Caps:   PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                                Arb:    Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                                Ctrl:   Enable- ID=3 ArbSelect=Fixed TC/VC=00
                                Status: NegoPending- InProgress-
                Capabilities: [900 v1] L1 PM Substates
                        L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                                  PortCommonModeRestoreTime=255us PortTPowerOnTime=26us
                        L1SubCtl1: PCI-PM_L1.2- PCI-PM_L1.1- ASPM_L1.2- ASPM_L1.1-
                                   T_CommonMode=0us LTR1.2_Threshold=0ns
                        L1SubCtl2: T_PwrOn=10us
                Capabilities: [a20 v1] Precision Time Measurement
                        PTMCap: Requester:- Responder:+ Root:+
                        PTMClockGranularity: 4ns
                        PTMControl: Enabled:- RootSelected:-
                        PTMEffectiveGranularity: Unknown
                Kernel driver in use: pcieport
                Kernel modules: pci_endpoint_test

            01:00.0 Non-Volatile memory controller: Intel Corporation Optane SSD 900P Series (prog-if 02 [NVM Express])
                    Subsystem: Intel Corporation 900P Series [Add-in Card]
                    Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
                    Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
                    Latency: 0
                    Interrupt: pin A routed to IRQ 43
                    Region 0: Memory at 68110000 (64-bit, non-prefetchable) [size=16K]
                    Expansion ROM at 68100000 [virtual] [disabled] [size=64K]
                    Capabilities: [40] Power Management version 3
                            Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1-,D2-,D3hot-,D3cold-)
                            Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
                    Capabilities: [50] MSI-X: Enable+ Count=32 Masked-
                            Vector table: BAR=0 offset=00002000
                            PBA: BAR=0 offset=00003000
                    Capabilities: [60] Express (v2) Endpoint, MSI 00
                            DevCap: MaxPayload 256 bytes, PhantFunc 0, Latency L0s <4us, L1 <4us
                                    ExtTag+ AttnBtn- AttnInd- PwrInd- RBE+ FLReset+ SlotPowerLimit 0.000W
                            DevCtl: CorrErr- NonFatalErr- FatalErr- UnsupReq-
                                    RlxdOrd+ ExtTag+ PhantFunc- AuxPwr- NoSnoop+ FLReset-
                                    MaxPayload 128 bytes, MaxReadReq 512 bytes
                            DevSta: CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
                            LnkCap: Port #0, Speed 8GT/s, Width x4, ASPM L0s, Exit Latency L0s <4us
                                    ClockPM- Surprise- LLActRep- BwNot- ASPMOptComp+
                            LnkCtl: ASPM Disabled; RCB 64 bytes Disabled- CommClk-
                                    ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                            LnkSta: Speed 5GT/s (downgraded), Width x1 (downgraded)
                                    TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
                            DevCap2: Completion Timeout: Range ABCD, TimeoutDis+, NROPrPrP-, LTR-
                                     10BitTagComp-, 10BitTagReq-, OBFF Not Supported, ExtFmt-, EETLPPrefix-
                                     EmergencyPowerReduction Not Supported, EmergencyPowerReductionInit-
                                     FRS-, TPHComp-, ExtTPHComp-
                                     AtomicOpsCap: 32bit- 64bit- 128bitCAS-
                            DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
                                     AtomicOpsCtl: ReqEn-
                            LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                                     Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                                     Compliance De-emphasis: -6dB
                            LnkSta2: Current De-emphasis Level: -6dB, EqualizationComplete-, EqualizationPhase1-
                                     EqualizationPhase2-, EqualizationPhase3-, LinkEqualizationRequest-
                    Capabilities: [100 v1] Advanced Error Reporting
                            UESta:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                            UEMsk:  DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                            UESvrt: DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                            CESta:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
                            CEMsk:  RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
                            AERCap: First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                                    MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
                            HeaderLog: 00000000 00000000 00000000 00000000
                    Capabilities: [150 v1] Virtual Channel
                            Caps:   LPEVC=0 RefClk=100ns PATEntryBits=1
                            Arb:    Fixed- WRR32- WRR64- WRR128-
                            Ctrl:   ArbSelect=Fixed
                            Status: InProgress-
                            VC0:    Caps:   PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                                    Arb:    Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                                    Ctrl:   Enable+ ID=0 ArbSelect=Fixed TC/VC=ff
                                    Status: NegoPending- InProgress-
                    Capabilities: [180 v1] Power Budgeting <?>
                    Capabilities: [190 v1] Alternative Routing-ID Interpretation (ARI)
                            ARICap: MFVC- ACS-, Next Function: 0
                            ARICtl: MFVC- ACS-, Function Group: 0
                    Capabilities: [270 v1] Device Serial Number 55-cd-2e-41-4e-31-12-50
                    Capabilities: [2a0 v1] Secondary PCI Express
                            LnkCtl3: LnkEquIntrruptEn-, PerformEqu-
                            LaneErrStat: 0
                    Kernel driver in use: nvme
                    Kernel modules: nvme

        - Test using hdparm

        ::

            root@am64xx-evm:~# hdparm -tT /dev/nvme0n1

            /dev/nvme0n1:
            Timing cached reads: 1062 MB in  2.00 seconds = 530.42 MB/sec
            Timing buffered disk reads: 812 MB in  3.01 seconds = 270.03 MB/sec

        - Test using dd

        ::

            root@am64xx-evm:~# time dd if=/dev/urandom of=/home/root/srctest_file_pci_2199 bs=1M count=10
            10+0 records in
            10+0 records out
            real	0m 0.22s
            user	0m 0.00s
            sys	    0m 0.20s

.. ifconfig:: CONFIG_part_family in ('J7_family')

      ::

          root@j721e-evm:~# lspci
          0000:00:00.0 PCI bridge: Texas Instruments Device b00d
          0000:01:00.0 Unassigned class [ff00]: Texas Instruments Device b00d
          0000:01:00.1 Unassigned class [ff00]: Texas Instruments Device b00d
          0000:01:00.2 Unassigned class [ff00]: Texas Instruments Device b00d
          0000:01:00.3 Unassigned class [ff00]: Texas Instruments Device b00d
          0000:01:00.4 Unassigned class [ff00]: Texas Instruments Device b00d
          0000:01:00.5 Unassigned class [ff00]: Texas Instruments Device b00d
          0001:00:00.0 PCI bridge: Texas Instruments Device b00d
          0002:00:00.0 PCI bridge: Texas Instruments Device b00d

    -  WiFi card

        - lspci output

        ::

            root@j721e-evm:~# lspci
            0000:00:00.0 PCI bridge: Texas Instruments Device b00d
            0000:01:00.0 Network controller: Intel Corporation Wireless 3160 (rev 6b)
            0001:00:00.0 PCI bridge: Texas Instruments Device b00d
            0002:00:00.0 PCI bridge: Texas Instruments Device b00d

        - Test using ping

        ::

            root@j721e-evm:~# ping 192.168.10.1 -w 10|
            PING 192.168.10.1 (192.168.10.1): 56 data bytes
            64 bytes from 192.168.10.1: seq=0 ttl=64 time=176.985 ms
            64 bytes from 192.168.10.1: seq=1 ttl=64 time=49.840 ms
            64 bytes from 192.168.10.1: seq=2 ttl=64 time=32.125 ms
            64 bytes from 192.168.10.1: seq=3 ttl=64 time=4.652 ms
            64 bytes from 192.168.10.1: seq=4 ttl=64 time=70.805 ms
            64 bytes from 192.168.10.1: seq=6 ttl=64 time=195.564 ms
            64 bytes from 192.168.10.1: seq=7 ttl=64 time=9.321 ms
            64 bytes from 192.168.10.1: seq=8 ttl=64 time=5.784 ms
            64 bytes from 192.168.10.1: seq=9 ttl=64 time=18.015 ms

    -  NVMe SSD

        - lspci output

        ::

            root@j721e-evm:~# lspci -vv
            0000:00:00.0 PCI bridge: Texas Instruments Device b00d (prog-if 00 [Normal decode])
                Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
                Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
                Interrupt: pin A routed to IRQ 0
                Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
                I/O behind bridge: None
                Memory behind bridge: None
                Prefetchable memory behind bridge: None
                Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
                BridgeCtl: Parity- SERR- NoISA- VGA- VGA16- MAbort- >Reset- FastB2B-
                    PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
                Capabilities: [80] Power Management version 3
                    Flags: PMEClk- DSI- D1+ D2- AuxCurrent=0mA PME(D0+,D1+,D2-,D3hot+,D3cold-)
                    Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
                Capabilities: [90] MSI: Enable- Count=1/1 Maskable+ 64bit+
                    Address: 0000000000000000  Data: 0000
                    Masking: 00000000  Pending: 00000000
                Capabilities: [b0] MSI-X: Enable- Count=1 Masked-
                    Vector table: BAR=0 offset=00000000
                    PBA: BAR=0 offset=00000008
                Capabilities: [c0] Express (v2) Root Port (Slot+), MSI 00
                    DevCap:	MaxPayload 256 bytes, PhantFunc 0
                        ExtTag- RBE+
                    DevCtl:	CorrErr- NonFatalErr- FatalErr- UnsupReq-
                        RlxdOrd+ ExtTag- PhantFunc- AuxPwr- NoSnoop+
                        MaxPayload 128 bytes, MaxReadReq 512 bytes
                    DevSta:	CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
                    LnkCap:	Port #0, Speed 8GT/s, Width x1, ASPM L1, Exit Latency L1 <8us
                        ClockPM- Surprise- LLActRep- BwNot+ ASPMOptComp+
                    LnkCtl:	ASPM Disabled; RCB 64 bytes Disabled- CommClk-
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                    LnkSta:	Speed 2.5GT/s (downgraded), Width x2 (strange)
                        TrErr- Train- SlotClk- DLActive- BWMgmt- ABWMgmt-
                    SltCap:	AttnBtn- PwrCtrl- MRL- AttnInd- PwrInd- HotPlug- Surprise-
                        Slot #0, PowerLimit 0.000W; Interlock- NoCompl-
                    SltCtl:	Enable: AttnBtn- PwrFlt- MRL- PresDet- CmdCplt- HPIrq- LinkChg-
                        Control: AttnInd Off, PwrInd Off, Power+ Interlock-
                    SltSta:	Status: AttnBtn- PowerFlt- MRL+ CmdCplt- PresDet- Interlock-
                        Changed: MRL- PresDet- LinkState-
                    RootCtl: ErrCorrectable- ErrNon-Fatal- ErrFatal- PMEIntEna- CRSVisible-
                    RootCap: CRSVisible-
                    RootSta: PME ReqID 0000, PMEStatus- PMEPending-
                    DevCap2: Completion Timeout: Range B, TimeoutDis+, LTR+, OBFF Not Supported ARIFwd+
                        AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                    DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled ARIFwd-
                        AtomicOpsCtl: ReqEn- EgressBlck-
                    LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                        Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                        Compliance De-emphasis: -6dB
                    LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete-, EqualizationPhase1-
                        EqualizationPhase2-, EqualizationPhase3-, LinkEqualizationRequest-
                Capabilities: [100 v2] Advanced Error Reporting
                    UESta:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                    UEMsk:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                    UESvrt:	DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                    CESta:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
                    CEMsk:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
                    AERCap:	First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                        MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
                    HeaderLog: 00000000 00000000 00000000 00000000
                    RootCmd: CERptEn- NFERptEn- FERptEn-
                    RootSta: CERcvd- MultCERcvd- UERcvd- MultUERcvd-
                        FirstFatal- NonFatalMsg- FatalMsg- IntMsg 0
                    ErrorSrc: ERR_COR: 0000 ERR_FATAL/NONFATAL: 0000
                Capabilities: [150 v1] Device Serial Number 00-00-00-00-00-00-00-00
                Capabilities: [300 v1] Secondary PCI Express <?>
                Capabilities: [4c0 v1] Virtual Channel
                    Caps:	LPEVC=0 RefClk=100ns PATEntryBits=1
                    Arb:	Fixed- WRR32- WRR64- WRR128-
                    Ctrl:	ArbSelect=Fixed
                    Status:	InProgress-
                    VC0:	Caps:	PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                        Arb:	Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                        Ctrl:	Enable+ ID=0 ArbSelect=Fixed TC/VC=ff
                        Status:	NegoPending- InProgress-
                    VC1:	Caps:	PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                        Arb:	Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                        Ctrl:	Enable- ID=1 ArbSelect=Fixed TC/VC=00
                        Status:	NegoPending- InProgress-
                    VC2:	Caps:	PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                        Arb:	Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                        Ctrl:	Enable- ID=2 ArbSelect=Fixed TC/VC=00
                        Status:	NegoPending- InProgress-
                    VC3:	Caps:	PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                        Arb:	Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                        Ctrl:	Enable- ID=3 ArbSelect=Fixed TC/VC=00
                        Status:	NegoPending- InProgress-
                Capabilities: [5c0 v1] Address Translation Service (ATS)
                    ATSCap:	Invalidate Queue Depth: 01
                    ATSCtl:	Enable-, Smallest Translation Unit: 00
                Capabilities: [640 v1] Page Request Interface (PRI)
                    PRICtl: Enable- Reset-
                    PRISta: RF- UPRGI- Stopped+
                    Page Request Capacity: 00000001, Page Request Allocation: 00000000
                Capabilities: [900 v1] L1 PM Substates
                    L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                        PortCommonModeRestoreTime=255us PortTPowerOnTime=26us
                    L1SubCtl1: PCI-PM_L1.2- PCI-PM_L1.1- ASPM_L1.2- ASPM_L1.1-
                        T_CommonMode=0us LTR1.2_Threshold=0ns
                    L1SubCtl2: T_PwrOn=10us
                Kernel modules: pci_endpoint_test, ntb_hw_epf

            0001:00:00.0 PCI bridge: Texas Instruments Device b00d (prog-if 00 [Normal decode])
                Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
                Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
                Latency: 0
                Interrupt: pin A routed to IRQ 0
                Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
                I/O behind bridge: None
                Memory behind bridge: 18100000-181fffff [size=1M]
                Prefetchable memory behind bridge: None
                Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
                BridgeCtl: Parity- SERR- NoISA- VGA- VGA16- MAbort- >Reset- FastB2B-
                    PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
                Capabilities: [80] Power Management version 3
                    Flags: PMEClk- DSI- D1+ D2- AuxCurrent=0mA PME(D0+,D1+,D2-,D3hot+,D3cold-)
                    Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
                Capabilities: [90] MSI: Enable- Count=1/1 Maskable+ 64bit+
                    Address: 0000000000000000  Data: 0000
                    Masking: 00000000  Pending: 00000000
                Capabilities: [b0] MSI-X: Enable- Count=1 Masked-
                    Vector table: BAR=0 offset=00000000
                    PBA: BAR=0 offset=00000008
                Capabilities: [c0] Express (v2) Root Port (Slot+), MSI 00
                    DevCap:	MaxPayload 256 bytes, PhantFunc 0
                        ExtTag- RBE+
                    DevCtl:	CorrErr- NonFatalErr- FatalErr- UnsupReq-
                        RlxdOrd+ ExtTag- PhantFunc- AuxPwr- NoSnoop+
                        MaxPayload 128 bytes, MaxReadReq 512 bytes
                    DevSta:	CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
                    LnkCap:	Port #0, Speed 8GT/s, Width x2, ASPM L1, Exit Latency L1 <8us
                        ClockPM- Surprise- LLActRep- BwNot+ ASPMOptComp+
                    LnkCtl:	ASPM Disabled; RCB 64 bytes Disabled- CommClk-
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                    LnkSta:	Speed 8GT/s (ok), Width x2 (ok)
                        TrErr- Train- SlotClk- DLActive- BWMgmt- ABWMgmt+
                    SltCap:	AttnBtn- PwrCtrl- MRL- AttnInd- PwrInd- HotPlug- Surprise-
                        Slot #0, PowerLimit 0.000W; Interlock- NoCompl-
                    SltCtl:	Enable: AttnBtn- PwrFlt- MRL- PresDet- CmdCplt- HPIrq- LinkChg-
                        Control: AttnInd Off, PwrInd Off, Power+ Interlock-
                    SltSta:	Status: AttnBtn- PowerFlt- MRL+ CmdCplt- PresDet- Interlock-
                        Changed: MRL- PresDet- LinkState-
                    RootCtl: ErrCorrectable- ErrNon-Fatal- ErrFatal- PMEIntEna- CRSVisible-
                    RootCap: CRSVisible-
                    RootSta: PME ReqID 0000, PMEStatus- PMEPending-
                    DevCap2: Completion Timeout: Range B, TimeoutDis+, LTR+, OBFF Not Supported ARIFwd+
                        AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                    DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled ARIFwd+
                        AtomicOpsCtl: ReqEn- EgressBlck-
                    LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                        Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                        Compliance De-emphasis: -6dB
                    LnkSta2: Current De-emphasis Level: -6dB, EqualizationComplete+, EqualizationPhase1+
                        EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
                Capabilities: [100 v2] Advanced Error Reporting
                    UESta:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                    UEMsk:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                    UESvrt:	DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                    CESta:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
                    CEMsk:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
                    AERCap:	First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                        MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
                    HeaderLog: 00000000 00000000 00000000 00000000
                    RootCmd: CERptEn- NFERptEn- FERptEn-
                    RootSta: CERcvd- MultCERcvd- UERcvd- MultUERcvd-
                        FirstFatal- NonFatalMsg- FatalMsg- IntMsg 0
                    ErrorSrc: ERR_COR: 0000 ERR_FATAL/NONFATAL: 0000
                Capabilities: [150 v1] Device Serial Number 00-00-00-00-00-00-00-00
                Capabilities: [300 v1] Secondary PCI Express <?>
                Capabilities: [4c0 v1] Virtual Channel
                    Caps:	LPEVC=0 RefClk=100ns PATEntryBits=1
                    Arb:	Fixed- WRR32- WRR64- WRR128-
                    Ctrl:	ArbSelect=Fixed
                    Status:	InProgress-
                    VC0:	Caps:	PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                        Arb:	Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                        Ctrl:	Enable+ ID=0 ArbSelect=Fixed TC/VC=ff
                        Status:	NegoPending- InProgress-
                    VC1:	Caps:	PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                        Arb:	Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                        Ctrl:	Enable- ID=1 ArbSelect=Fixed TC/VC=00
                        Status:	NegoPending- InProgress-
                    VC2:	Caps:	PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                        Arb:	Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                        Ctrl:	Enable- ID=2 ArbSelect=Fixed TC/VC=00
                        Status:	NegoPending- InProgress-
                    VC3:	Caps:	PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                        Arb:	Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                        Ctrl:	Enable- ID=3 ArbSelect=Fixed TC/VC=00
                        Status:	NegoPending- InProgress-
                Capabilities: [5c0 v1] Address Translation Service (ATS)
                    ATSCap:	Invalidate Queue Depth: 01
                    ATSCtl:	Enable-, Smallest Translation Unit: 00
                Capabilities: [640 v1] Page Request Interface (PRI)
                    PRICtl: Enable- Reset-
                    PRISta: RF- UPRGI- Stopped+
                    Page Request Capacity: 00000001, Page Request Allocation: 00000000
                Capabilities: [900 v1] L1 PM Substates
                    L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                        PortCommonModeRestoreTime=255us PortTPowerOnTime=26us
                    L1SubCtl1: PCI-PM_L1.2- PCI-PM_L1.1- ASPM_L1.2- ASPM_L1.1-
                        T_CommonMode=0us LTR1.2_Threshold=0ns
                    L1SubCtl2: T_PwrOn=10us
                Kernel modules: pci_endpoint_test, ntb_hw_epf

            0001:01:00.0 Non-Volatile memory controller: Lite-On Technology Corporation M8Pe Series NVMe SSD (rev 01) (prog-if 02 [NVM Express])
                Subsystem: Marvell Technology Group Ltd. M8Pe Series NVMe SSD
                Control: I/O- Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
                Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
                Latency: 0
                Interrupt: pin A routed to IRQ 0
                Region 0: Memory at 18120000 (64-bit, non-prefetchable) [size=16K]
                Expansion ROM at 18100000 [size=128K]
                Capabilities: [40] Power Management version 3
                    Flags: PMEClk- DSI- D1- D2- AuxCurrent=0mA PME(D0-,D1-,D2-,D3hot-,D3cold-)
                    Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
                Capabilities: [50] MSI: Enable- Count=1/1 Maskable+ 64bit+
                    Address: 0000000000000000  Data: 0000
                    Masking: 00000000  Pending: 00000000
                Capabilities: [70] Express (v2) Endpoint, MSI 00
                    DevCap:	MaxPayload 128 bytes, PhantFunc 0, Latency L0s unlimited, L1 unlimited
                        ExtTag- AttnBtn- AttnInd- PwrInd- RBE+ FLReset+ SlotPowerLimit 0.000W
                    DevCtl:	CorrErr- NonFatalErr- FatalErr- UnsupReq-
                        RlxdOrd+ ExtTag- PhantFunc- AuxPwr- NoSnoop- FLReset-
                        MaxPayload 128 bytes, MaxReadReq 512 bytes
                    DevSta:	CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
                    LnkCap:	Port #0, Speed 8GT/s, Width x4, ASPM L1, Exit Latency L1 <64us
                        ClockPM+ Surprise- LLActRep- BwNot- ASPMOptComp+
                    LnkCtl:	ASPM Disabled; RCB 64 bytes Disabled- CommClk-
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                    LnkSta:	Speed 8GT/s (ok), Width x2 (downgraded)
                        TrErr- Train- SlotClk+ DLActive- BWMgmt- ABWMgmt-
                    DevCap2: Completion Timeout: Not Supported, TimeoutDis+, LTR+, OBFF Via message
                        AtomicOpsCap: 32bit- 64bit- 128bitCAS-
                    DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled
                        AtomicOpsCtl: ReqEn-
                    LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                        Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                        Compliance De-emphasis: -6dB
                    LnkSta2: Current De-emphasis Level: -6dB, EqualizationComplete+, EqualizationPhase1+
                        EqualizationPhase2+, EqualizationPhase3+, LinkEqualizationRequest-
                Capabilities: [b0] MSI-X: Enable+ Count=19 Masked-
                    Vector table: BAR=0 offset=00002000
                    PBA: BAR=0 offset=00003000
                Capabilities: [100 v2] Advanced Error Reporting
                    UESta:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                    UEMsk:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                    UESvrt:	DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                    CESta:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
                    CEMsk:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
                    AERCap:	First Error Pointer: 00, ECRCGenCap+ ECRCGenEn+ ECRCChkCap+ ECRCChkEn+
                        MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
                    HeaderLog: 00000000 00000000 00000000 00000000
                Capabilities: [148 v1] Device Serial Number 00-00-00-00-00-00-00-00
                Capabilities: [158 v1] Power Budgeting <?>
                Capabilities: [168 v1] Alternative Routing-ID Interpretation (ARI)
                    ARICap:	MFVC- ACS-, Next Function: 0
                    ARICtl:	MFVC- ACS-, Function Group: 0
                Capabilities: [178 v1] Secondary PCI Express <?>
                Capabilities: [2b8 v1] Latency Tolerance Reporting
                    Max snoop latency: 0ns
                    Max no snoop latency: 0ns
                Capabilities: [2c0 v1] L1 PM Substates
                    L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                        PortCommonModeRestoreTime=10us PortTPowerOnTime=10us
                    L1SubCtl1: PCI-PM_L1.2- PCI-PM_L1.1- ASPM_L1.2- ASPM_L1.1-
                        T_CommonMode=0us LTR1.2_Threshold=0ns
                    L1SubCtl2: T_PwrOn=10us
                Kernel driver in use: nvme
                Kernel modules: nvme

            0002:00:00.0 PCI bridge: Texas Instruments Device b00d (prog-if 00 [Normal decode])
                Control: I/O- Mem- BusMaster- SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx-
                Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
                Interrupt: pin A routed to IRQ 0
                Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
                I/O behind bridge: None
                Memory behind bridge: None
                Prefetchable memory behind bridge: None
                Secondary status: 66MHz- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- <SERR- <PERR-
                BridgeCtl: Parity- SERR- NoISA- VGA- VGA16- MAbort- >Reset- FastB2B-
                    PriDiscTmr- SecDiscTmr- DiscTmrStat- DiscTmrSERREn-
                Capabilities: [80] Power Management version 3
                    Flags: PMEClk- DSI- D1+ D2- AuxCurrent=0mA PME(D0+,D1+,D2-,D3hot+,D3cold-)
                    Status: D0 NoSoftRst+ PME-Enable- DSel=0 DScale=0 PME-
                Capabilities: [90] MSI: Enable- Count=1/1 Maskable+ 64bit+
                    Address: 0000000000000000  Data: 0000
                    Masking: 00000000  Pending: 00000000
                Capabilities: [b0] MSI-X: Enable- Count=1 Masked-
                    Vector table: BAR=0 offset=00000000
                    PBA: BAR=0 offset=00000008
                Capabilities: [c0] Express (v2) Root Port (Slot+), MSI 00
                    DevCap:	MaxPayload 256 bytes, PhantFunc 0
                        ExtTag- RBE+
                    DevCtl:	CorrErr- NonFatalErr- FatalErr- UnsupReq-
                        RlxdOrd+ ExtTag- PhantFunc- AuxPwr- NoSnoop+
                        MaxPayload 128 bytes, MaxReadReq 512 bytes
                    DevSta:	CorrErr- NonFatalErr- FatalErr- UnsupReq- AuxPwr- TransPend-
                    LnkCap:	Port #0, Speed 8GT/s, Width x2, ASPM L1, Exit Latency L1 <8us
                        ClockPM- Surprise- LLActRep- BwNot+ ASPMOptComp+
                    LnkCtl:	ASPM Disabled; RCB 64 bytes Disabled- CommClk-
                        ExtSynch- ClockPM- AutWidDis- BWInt- AutBWInt-
                    LnkSta:	Speed 2.5GT/s (downgraded), Width x2 (ok)
                        TrErr- Train- SlotClk- DLActive- BWMgmt- ABWMgmt-
                    SltCap:	AttnBtn- PwrCtrl- MRL- AttnInd- PwrInd- HotPlug- Surprise-
                        Slot #0, PowerLimit 0.000W; Interlock- NoCompl-
                    SltCtl:	Enable: AttnBtn- PwrFlt- MRL- PresDet- CmdCplt- HPIrq- LinkChg-
                        Control: AttnInd Off, PwrInd Off, Power+ Interlock-
                    SltSta:	Status: AttnBtn- PowerFlt- MRL+ CmdCplt- PresDet- Interlock-
                        Changed: MRL- PresDet- LinkState-
                    RootCtl: ErrCorrectable- ErrNon-Fatal- ErrFatal- PMEIntEna- CRSVisible-
                    RootCap: CRSVisible-
                    RootSta: PME ReqID 0000, PMEStatus- PMEPending-
                    DevCap2: Completion Timeout: Range B, TimeoutDis+, LTR+, OBFF Not Supported ARIFwd+
                        AtomicOpsCap: Routing- 32bit- 64bit- 128bitCAS-
                    DevCtl2: Completion Timeout: 50us to 50ms, TimeoutDis-, LTR-, OBFF Disabled ARIFwd-
                        AtomicOpsCtl: ReqEn- EgressBlck-
                    LnkCtl2: Target Link Speed: 8GT/s, EnterCompliance- SpeedDis-
                        Transmit Margin: Normal Operating Range, EnterModifiedCompliance- ComplianceSOS-
                        Compliance De-emphasis: -6dB
                    LnkSta2: Current De-emphasis Level: -3.5dB, EqualizationComplete-, EqualizationPhase1-
                        EqualizationPhase2-, EqualizationPhase3-, LinkEqualizationRequest-
                Capabilities: [100 v2] Advanced Error Reporting
                    UESta:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                    UEMsk:	DLP- SDES- TLP- FCP- CmpltTO- CmpltAbrt- UnxCmplt- RxOF- MalfTLP- ECRC- UnsupReq- ACSViol-
                    UESvrt:	DLP+ SDES+ TLP- FCP+ CmpltTO- CmpltAbrt- UnxCmplt- RxOF+ MalfTLP+ ECRC- UnsupReq- ACSViol-
                    CESta:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr-
                    CEMsk:	RxErr- BadTLP- BadDLLP- Rollover- Timeout- AdvNonFatalErr+
                    AERCap:	First Error Pointer: 00, ECRCGenCap+ ECRCGenEn- ECRCChkCap+ ECRCChkEn-
                        MultHdrRecCap- MultHdrRecEn- TLPPfxPres- HdrLogCap-
                    HeaderLog: 00000000 00000000 00000000 00000000
                    RootCmd: CERptEn- NFERptEn- FERptEn-
                    RootSta: CERcvd- MultCERcvd- UERcvd- MultUERcvd-
                        FirstFatal- NonFatalMsg- FatalMsg- IntMsg 0
                    ErrorSrc: ERR_COR: 0000 ERR_FATAL/NONFATAL: 0000
                Capabilities: [150 v1] Device Serial Number 00-00-00-00-00-00-00-00
                Capabilities: [300 v1] Secondary PCI Express <?>
                Capabilities: [4c0 v1] Virtual Channel
                    Caps:	LPEVC=0 RefClk=100ns PATEntryBits=1
                    Arb:	Fixed- WRR32- WRR64- WRR128-
                    Ctrl:	ArbSelect=Fixed
                    Status:	InProgress-
                    VC0:	Caps:	PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                        Arb:	Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                        Ctrl:	Enable+ ID=0 ArbSelect=Fixed TC/VC=ff
                        Status:	NegoPending- InProgress-
                    VC1:	Caps:	PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                        Arb:	Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                        Ctrl:	Enable- ID=1 ArbSelect=Fixed TC/VC=00
                        Status:	NegoPending- InProgress-
                    VC2:	Caps:	PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                        Arb:	Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                        Ctrl:	Enable- ID=2 ArbSelect=Fixed TC/VC=00
                        Status:	NegoPending- InProgress-
                    VC3:	Caps:	PATOffset=00 MaxTimeSlots=1 RejSnoopTrans-
                        Arb:	Fixed- WRR32- WRR64- WRR128- TWRR128- WRR256-
                        Ctrl:	Enable- ID=3 ArbSelect=Fixed TC/VC=00
                        Status:	NegoPending- InProgress-
                Capabilities: [5c0 v1] Address Translation Service (ATS)
                    ATSCap:	Invalidate Queue Depth: 01
                    ATSCtl:	Enable-, Smallest Translation Unit: 00
                Capabilities: [640 v1] Page Request Interface (PRI)
                    PRICtl: Enable- Reset-
                    PRISta: RF- UPRGI- Stopped+
                    Page Request Capacity: 00000001, Page Request Allocation: 00000000
                Capabilities: [900 v1] L1 PM Substates
                    L1SubCap: PCI-PM_L1.2+ PCI-PM_L1.1+ ASPM_L1.2+ ASPM_L1.1+ L1_PM_Substates+
                        PortCommonModeRestoreTime=255us PortTPowerOnTime=26us
                    L1SubCtl1: PCI-PM_L1.2- PCI-PM_L1.1- ASPM_L1.2- ASPM_L1.1-
                        T_CommonMode=0us LTR1.2_Threshold=0ns
                    L1SubCtl2: T_PwrOn=10us
                Kernel modules: pci_endpoint_test, ntb_hw_epf

        - Test using hdparm

        ::

            root@j721e-evm:~# hdparm -tT /dev/nvme0n1

            /dev/nvme0n1:
            Timing cached reads: 3678 MB in 2.00 seconds = 1840.32 MB/sec
            Timing buffered disk reads: 2252 MB in 3.00 seconds = 750.34 MB/sec

        - Test using dd

        ::

            root@j721e-evm:~# time dd if=/dev/urandom of=/home/root/srctest_file_pci_2199 bs=1M count=10|
            10+0 records in
            10+0 records out
            real	0m 0.17s
            user	0m 0.00s
            sys	    0m 0.08s

    .. rubric:: **J7200 Testing Details**

    PCIe and QSGMII uses the same SERDES in J7200. The default SDK is enabled for QSGMII. In order to
    test PCIe, Ethfw firmware shouldn't be loaded and PCIe overlay file should be applied.

    The simplest way to avoid ethfw from being loaded is to link j7200-main-r5f0_0-fw to IPC firmware.
    ::

        root@j7200-evm:~# rm /lib/firmware/j7200-main-r5f0_0-fw
        root@j7200-evm:~# ln -s /lib/firmware/pdk-ipc/ipc_echo_test_mcu2_0_release_strip.xer5f /lib/firmware/j7200-main-r5f0_0-fw

    The following Device Tree Overlay should be applied for testing J7200 RC.

    https://git.ti.com/cgit/ti-linux-kernel/ti-upstream-tools/tree/arch/arm64/boot/dts/ti/system_test/pcie/pcie_ep/k3-j7200-common-proc-board-pcie.dtso?h=ti-linux-5.4.y


    The following command should be given in u-boot to apply overlay

        ::

           => setenv name_overlays ti/k3-j7200-common-proc-board-pcie.dtbo
