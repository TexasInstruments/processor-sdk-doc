.. _KERNEL-SATA:

UFS
---------------------------------

.. rubric:: Introduction
   :name: introduction-linux-ufs

Universal Flash Storage (UFS) is a high performance mass storage device
with a serial interface. It is primarily used as a high performance data
storage device for embedded applications. There are JEDEC standards
governing UFS device and host controller. UFS adapts MIPI MPHY and
MIPI UniPro standards.

This user guide applies to kernel v4.19 and higher.

.. rubric:: Supported Devices
   :name: supported-devices-ufs

-  J721E EVM
-  J742S2 EVM
-  J784S4 EVM

.. rubric:: Hardware features
   :name: hardware-features-ufs

Key Features:

- Supports Universal Flash Storage Host (UFS2.1, JESD220C)
- Supports Universal Flash Storage Host Controller Interface (UFSHCI, JESD223C)
- Supports UFS interconnect - MIPI UniPro and MIPI M-PHY
- Supports Gear 1: 1.46 Gbps, 2-lanes
- Supports Gear 2: 2.91 Gbps, 2-lanes
- Supports Gear 3: 5.83 Gbps, 2-lanes
- Supports 128-bit Advanced Encryption Standard (AES) encryption
- Supports аll UFS mandatory SCSI commands required by JEDEC specification

.. rubric:: Driver features
   :name: driver-features-ufs

.. rubric:: Supported Features
   :name: supported-features-ufs

- Linux as standard UFS Host Controller Interface (UFSHCI) driver at :file:`drivers/scsi/ufs/ufshcd.c` and platform/SoC specific glue layers are located in the same folder.
- Supports HS Gear3B, 2-lanes


.. rubric:: Unsupported Features
   :name: unsupported-features-ufs

- No support for UFS inline Encryption/Decryption using UFS Crypto Engine

.. rubric:: Hardware Architecture and Software Architecure
   :name: hardware-architecture-ufs

UFS follows SCSI Architecture Model (SAM) and hence falls unders Linux's
SCSI stack. User space programs can interact with UFS storage device in
the same way as any other SCSI devices.
Hardware architecture is explained in detail in UFS JEDEC specification
JESD220D
Host Controller Interface and programming sequence is explained in
UFSHCI JEDEC specification JESD223C

UFS storage devices are exposed in Linux as :file:`/dev/sd{X}`. Tools such as
fdisk can be used to format and store data onto them similar to
traditional Hard Disks.

Here is the typical enumeration log of UFS devices

.. code-block:: console

	[    4.727525] cdns-ufshcd 4e84000.ufs: ufshcd_print_pwr_info:[RX, TX]: gear=[1, 1], lane[1, 1], pwr[SLOWAUTO_MODE, SLOWAUTO_MODE], rate = 0
	[    4.763158] cdns-ufshcd 4e84000.ufs: ufshcd_print_pwr_info:[RX, TX]: gear=[3, 3], lane[2, 2], pwr[FAST MODE, FAST MODE], rate = 2
	[    4.776497] cdns-ufshcd 4e84000.ufs: ufshcd_find_max_sup_active_icc_level: Regulator capability was not set, actvIccLevel=0
	[    4.787805] scsi 0:0:0:49488: Well-known LUN    TOSHIBA  THGAF8G8T23BAILB 0300 PQ: 0 ANSI: 6
	[    4.807335] scsi 0:0:0:49476: Well-known LUN    TOSHIBA  THGAF8G8T23BAILB 0300 PQ: 0 ANSI: 6
	[    4.816015] cdns-ufshcd 4e84000.ufs: ufshcd_scsi_add_wlus: BOOT WLUN not found
	[    4.828531] scsi 0:0:0:0: Direct-Access     TOSHIBA  THGAF8G8T23BAILB 0300 PQ: 0 ANSI: 6
	[    4.836834] sd 0:0:0:0: Power-on or device reset occurred
	[    4.842379] sd 0:0:0:0: [sda] 8192 4096-byte logical blocks: (33.6 MB/32.0 MiB)
	[    4.842404] scsi 0:0:0:1: Direct-Access     TOSHIBA  THGAF8G8T23BAILB 0300 PQ: 0 ANSI: 6
	[    4.857817] sd 0:0:0:0: [sda] Write Protect is off
	[    4.862629] sd 0:0:0:1: Power-on or device reset occurred
	[    4.862715] sd 0:0:0:0: [sda] Mode Sense: 00 32 00 10
	[    4.868197] sd 0:0:0:1: [sdb] 7808000 4096-byte logical blocks: (32.0 GB/29.8 GiB)
	[    4.880653] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, supports DPO and FUA
	[    4.889170] sd 0:0:0:1: [sdb] Write Protect is off
	[    4.889204] sd 0:0:0:0: [sda] Optimal transfer size 65536 bytes
	[    4.893959] sd 0:0:0:1: [sdb] Mode Sense: 00 32 00 10
	[    4.904957] sd 0:0:0:1: [sdb] Write cache: enabled, read cache: enabled, supports DPO and FUA
	[    4.905701] sd 0:0:0:0: [sda] Attached SCSI disk
	[    4.918093] sd 0:0:0:1: [sdb] Optimal transfer size 65536 bytes
	[    4.924852] sd 0:0:0:1: [sdb] Attached SCSI disk


.. rubric:: UFS Logical Units
   :name: UFS Logical Units

A UFS flash device is composed of memory blocks that are mapped to
different Logical Units (LUs). UFS device address space is organized in
several memory areas configurable by the user. In particular, such
memory areas are denoted as logical units and characterized by the fact
that they have independent logical addressable spaces starting from the
logical address zero. Thus, a logical unit (LU) is an externally
addressable, independent, processing entity that processes SCSI tasks
(commands) and performs task management functions. Each logical unit is
independent of other logical units in a device

In addition to the logical units, the UFS device supports the following well known logical units for specific purposes: UFS Device, REPORT LUNS, Boot and RPMB. Logical units are addressed by the LUN (logical unit number), while well known logical unit are addressed by the W-LUN (well known logical unit number).
In particular, the UFS device shall support the number of logical units specified by bMaxNumberLU. Each of them can be configured as boot
The number of logical units specified by bMaxNumberLU.
One RPMB well known logical unit (W-LUN = 44h, LUN field in UPIU = C4h). RPMB well known
logical unit may be further configured into up to four separate RPMB
regions (RPMB region 0 - RPMB region 3). A maximum of two logical units can be
configured as Boot logical units, with only one of them active and
readable through the Boot well known logical unit (W-LUN = 30h) for the
execution of the system boot (see UFS Boot section of JEDEC Spec). The
RPMB well known logical unit is accessed by authenticated operations by
a well defined security algorithm. The other logical units will be used
to fulfill other use cases.

.. rubric:: Logical Block Provisioning
   :name: Logical Block Provisioning

Logical Block Provisioning is the concept that describes the relationship between the logical block address space and the physical memory resources that supports the logical address space.

.. note::

 By default, Device comes with no LUs provisioned therefore device must
 be provisioned to be able to store anything in the device.

.. rubric:: Interacting with UFS device from userspace
   :name: Interacting with UFS device from userspace

UFS and SCSI layer supports something called Block SCSI Generic (BSG)
Device which exposes SCSI device such as UFS as generic device to
Userspace. UFS flash can be accessed at :file:`/dev/bsg/ufs-bsg{x}` where
`x` varies across devices and UFS parts.

`ufs-utils <https://github.com/westerndigitalcorporation/ufs-utils>`_
(part of SDK) can be used to interact with UFS device from userspace.

.. rubric:: UFS descriptors

A Descriptor is a block or page of parameters that describe something about a Device. For example, there are Device Descriptors, Configuration Descriptors, Unit Descriptors, etc.
In general, all Descriptors are readable, some may be write once, others
may have a write protection mechanism. The Configuration Descriptor is
writeable and allows modification of the device configuration set by the
manufacturer. More details in JEDEC UFS specification.
ufs-utils can be used to read any of the descriptor. See tool help for
more details.

.. rubric:: Provisioning UFS device using ufs-utils

UFS device can be provisioned by writing configuration descriptor to the
flash. You can read current configuration of UFS device using:

.. code-block:: console

	root@j721e-evm:~# ufs-utils desc -t 1 -p /dev/bsg/ufs-bsg0
	Config Device Descriptor: [Byte offset 0x0]: bLength = 0x90
	Config Device Descriptor: [Byte offset 0x1]: bDescriptorType = 0x1
	Config Device Descriptor: [Byte offset 0x2]: bConfDescContinue = 0x0
	Config Device Descriptor: [Byte offset 0x3]: bBootEnable = 0x1
	Config Device Descriptor: [Byte offset 0x4]: bDescrAccessEn = 0x1
	Config Device Descriptor: [Byte offset 0x5]: bInitPowerMode = 0x1
	Config Device Descriptor: [Byte offset 0x6]: bHighPriorityLUN = 0x7f
	Config Device Descriptor: [Byte offset 0x7]: bSecureRemovalType = 0x0
	Config Device Descriptor: [Byte offset 0x8]: bInitActiveICCLevel = 0x0
	Config Device Descriptor: [Byte offset 0x9]: wPeriodicRTCUpdate = 0x0
	Config Device Descriptor: [Byte offset 0xc]: bRPMBRegionEnable = 0x0
	Config Device Descriptor: [Byte offset 0xd]: bRPMBRegion1Size = 0x0
	Config Device Descriptor: [Byte offset 0xe]: bRPMBRegion2Size = 0x0
	Config Device Descriptor: [Byte offset 0xf]: bRPMBRegion3Size = 0x0
	Config 0 Unit Descriptor:
	Config Descriptor: [Byte offset 0x0]: bLUEnable = 0x1
	Config Descriptor: [Byte offset 0x1]: bBootLunID = 0x0
	Config Descriptor: [Byte offset 0x2]: bLUWriteProtect = 0x0
	Config Descriptor: [Byte offset 0x3]: bMemoryType = 0x0
	Config Descriptor: [Byte offset 0x4]: dNumAllocUnits = 0x1900
	Config Descriptor: [Byte offset 0x8]: bDataReliability = 0x0
	Config Descriptor: [Byte offset 0x9]: bLogicalBlockSize = 0xc
	Config Descriptor: [Byte offset 0xa]: bProvisioningType = 0x0
	Config Descriptor: [Byte offset 0xb]: wContextCapabilities = 0x0
	Config 1 Unit Descriptor:
	Config Descriptor: [Byte offset 0x0]: bLUEnable = 0x1
	Config Descriptor: [Byte offset 0x1]: bBootLunID = 0x1
	Config Descriptor: [Byte offset 0x2]: bLUWriteProtect = 0x0
	Config Descriptor: [Byte offset 0x3]: bMemoryType = 0x0
	Config Descriptor: [Byte offset 0x4]: dNumAllocUnits = 0x9
	Config Descriptor: [Byte offset 0x8]: bDataReliability = 0x0
	Config Descriptor: [Byte offset 0x9]: bLogicalBlockSize = 0xc
	Config Descriptor: [Byte offset 0xa]: bProvisioningType = 0x0
	Config Descriptor: [Byte offset 0xb]: wContextCapabilities = 0x0
	Config 2 Unit Descriptor:
	Config Descriptor: [Byte offset 0x0]: bLUEnable = 0x1
	Config Descriptor: [Byte offset 0x1]: bBootLunID = 0x0
	Config Descriptor: [Byte offset 0x2]: bLUWriteProtect = 0x0
	Config Descriptor: [Byte offset 0x3]: bMemoryType = 0x0
	Config Descriptor: [Byte offset 0x4]: dNumAllocUnits = 0x1
	Config Descriptor: [Byte offset 0x8]: bDataReliability = 0x0
	Config Descriptor: [Byte offset 0x9]: bLogicalBlockSize = 0xc
	Config Descriptor: [Byte offset 0xa]: bProvisioningType = 0x0
	Config Descriptor: [Byte offset 0xb]: wContextCapabilities = 0x0
	Config 3 Unit Descriptor:
	Config Descriptor: [Byte offset 0x0]: bLUEnable = 0x0
	Config Descriptor: [Byte offset 0x1]: bBootLunID = 0x0
	Config Descriptor: [Byte offset 0x2]: bLUWriteProtect = 0x0
	Config Descriptor: [Byte offset 0x3]: bMemoryType = 0x0
	Config Descriptor: [Byte offset 0x4]: dNumAllocUnits = 0x0
	Config Descriptor: [Byte offset 0x8]: bDataReliability = 0x0
	Config Descriptor: [Byte offset 0x9]: bLogicalBlockSize = 0xc
	Config Descriptor: [Byte offset 0xa]: bProvisioningType = 0x0
	Config Descriptor: [Byte offset 0xb]: wContextCapabilities = 0x0
	Config 4 Unit Descriptor:
	Config Descriptor: [Byte offset 0x0]: bLUEnable = 0x0
	Config Descriptor: [Byte offset 0x1]: bBootLunID = 0x0
	Config Descriptor: [Byte offset 0x2]: bLUWriteProtect = 0x0
	Config Descriptor: [Byte offset 0x3]: bMemoryType = 0x0
	Config Descriptor: [Byte offset 0x4]: dNumAllocUnits = 0x0
	Config Descriptor: [Byte offset 0x8]: bDataReliability = 0x0
	Config Descriptor: [Byte offset 0x9]: bLogicalBlockSize = 0xc
	Config Descriptor: [Byte offset 0xa]: bProvisioningType = 0x0
	Config Descriptor: [Byte offset 0xb]: wContextCapabilities = 0x0
	Config 5 Unit Descriptor:
	Config Descriptor: [Byte offset 0x0]: bLUEnable = 0x0
	Config Descriptor: [Byte offset 0x1]: bBootLunID = 0x0
	Config Descriptor: [Byte offset 0x2]: bLUWriteProtect = 0x0
	Config Descriptor: [Byte offset 0x3]: bMemoryType = 0x0
	Config Descriptor: [Byte offset 0x4]: dNumAllocUnits = 0x0
	Config Descriptor: [Byte offset 0x8]: bDataReliability = 0x0
	Config Descriptor: [Byte offset 0x9]: bLogicalBlockSize = 0xc
	Config Descriptor: [Byte offset 0xa]: bProvisioningType = 0x0
	Config Descriptor: [Byte offset 0xb]: wContextCapabilities = 0x0
	Config 6 Unit Descriptor:
	Config Descriptor: [Byte offset 0x0]: bLUEnable = 0x0
	Config Descriptor: [Byte offset 0x1]: bBootLunID = 0x0
	Config Descriptor: [Byte offset 0x2]: bLUWriteProtect = 0x0
	Config Descriptor: [Byte offset 0x3]: bMemoryType = 0x0
	Config Descriptor: [Byte offset 0x4]: dNumAllocUnits = 0x0
	Config Descriptor: [Byte offset 0x8]: bDataReliability = 0x0
	Config Descriptor: [Byte offset 0x9]: bLogicalBlockSize = 0xc
	Config Descriptor: [Byte offset 0xa]: bProvisioningType = 0x0
	Config Descriptor: [Byte offset 0xb]: wContextCapabilities = 0x0
	Config 7 Unit Descriptor:
	Config Descriptor: [Byte offset 0x0]: bLUEnable = 0x0
	Config Descriptor: [Byte offset 0x1]: bBootLunID = 0x0
	Config Descriptor: [Byte offset 0x2]: bLUWriteProtect = 0x0
	Config Descriptor: [Byte offset 0x3]: bMemoryType = 0x0
	Config Descriptor: [Byte offset 0x4]: dNumAllocUnits = 0x0
	Config Descriptor: [Byte offset 0x8]: bDataReliability = 0x0
	Config Descriptor: [Byte offset 0x9]: bLogicalBlockSize = 0xc
	Config Descriptor: [Byte offset 0xa]: bProvisioningType = 0x0
	Config Descriptor: [Byte offset 0xb]: wContextCapabilities = 0x0
	Config Descriptor was written into config_desc_data_ind_0 file

This also dumps descriptor in binary format into file called
*config_desc_data_ind_0*. Edit file as necessary and write file back to
device using:

.. code-block:: console

	ufs-utils desc -t 1 -w config_desc_data_ind_0 -p /dev/bsg/ufs-bsg0

.. note::

 This erases all existing data on flash and creates new partition.
 There is a vendor specific limit on how many times device can be
 re-provisioned or re-partitioned. Also, this setup is non-volatile and
 persists across Power-On-Resets and needs to be done only once.

EVM users can find the pre-populated configuration descriptor binary
file at the following link. To provision UFS flash on EVM:

- Download the :download:`file </files/config_desc_data_ind_0>`
- Execute below command to flash descriptor and reboot the board to see
  new partitions

.. code-block:: console

	ufs-utils desc -t 1 -w config_desc_data_ind_0 -p /dev/bsg/ufs-bsg0

This creates two LUs on device. A Boot LUN of 32MB and rest of the
flash (~32GB) is formated as general data area (for filesystem etc)
These two partitions appear as two SCSI block devices eg :file:`/dev/sda` and
:file:`/dev/sdb` in Linux.

.. rubric:: Getting current speed gear and lane count:


User can dump all UFS UniPro attributes.

For Active Data lanes:

.. code-block:: console

	root@j721e-evm:~# ufs-utils uic -t 1 -i 0x1560 -p /dev/bsg/ufs-bsg0
	[0x1560]PA_ActiveTxDataLanes                          : local = 0x00000002, peer = 0x00000002
	root@j721e-evm:~# ufs-utils uic -t 1 -i 0x1580 -p /dev/bsg/ufs-bsg0
	[0x1580]PA_ActiveRxDataLanes                          : local = 0x00000002, peer = 0x00000002

Value of 2 indicates 2 lanes are active


For Gear Speed:

.. code-block:: console

	root@j721e-evm:~# ufs-utils uic -t 1 -i 0x1568 -p /dev/bsg/ufs-bsg0
	[0x1568]PA_TxGear                                     : local = 0x00000003, peer = 0x00000003
	root@j721e-evm:~# ufs-utils uic -t 1 -i 0x1583 -p /dev/bsg/ufs-bsg0
	[0x1583]PA_RxGear                                     : local = 0x00000003, peer = 0x00000003

Value of 3 indicates HS Gear3 is active

For HS Gear Series

.. code-block:: console

	root@j721e-evm:~# ufs-utils uic -t 1 -i 0x156a -p /dev/bsg/ufs-bsg0
	[0x156a]PA_HSSeries                                   : local = 0x00000002, peer = 0x00000002

A value of 2 indicates series B is active
