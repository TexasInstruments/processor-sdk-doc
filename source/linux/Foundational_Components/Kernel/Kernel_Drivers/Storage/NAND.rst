.. http://processors.wiki.ti.com/index.php/Linux_Core_NAND_User%27s_Guide

NAND
---------------------------------

.. rubric:: **Introduction**
   :name: introduction-linux-core-nand

.. rubric::  **TI infrastructure for NAND Flash devices**
   :name: ti-infrastructure-for-nand-flash-devices

TI's SoC interface with NAND Flash devices via on-chip GPMC (General
Purpose Memory Controller) interface or via AEMIF depending on the SoC.

For devices that include GPMC: The ECC algorithms required by NAND
devices to protect their data, are managed by two independent hardware
engines:

-  GPMC ECC engine: used for calculating ECC checksum while writing and
   reading the NAND device.
-  ELM ECC engine: used for locating and decoding ECC errors while
   reading the NAND device.

Depending on the SoC, a different set of NAND IP and drivers might be in use. The
following table summarizes the NAND IP and drivers used for each SoC family.

+----------------------------------+----------------------------------+
| Soc Family                       | NAND IP (drivers)                |
+==================================+==================================+
| OMAP2420, OMAP3430               | GPMC (omap2.o)                   |
+----------------------------------+----------------------------------+
| OMAP4430, OMAP5430               | GPMC (omap2.o), ELM (omap_elm.o) |
+----------------------------------+----------------------------------+
| AM335x, AM437x, AM57x, AM65x     | GPMC (omap2.o), ELM (omap_elm.o) |
+----------------------------------+----------------------------------+
| DM814, DM816                     | GPMC (omap2.o), ELM (omap_elm.o) |
+----------------------------------+----------------------------------+
| J5 (DRA62x), J6 (DRA72x), J721e  | GPMC (omap2.o), ELM (omap_elm.o) |
+----------------------------------+----------------------------------+
| K2G                              | GPMC (omap2.o), ELM (omap_elm.o) |
+----------------------------------+----------------------------------+
| K2E, K2HK, K2L                   | AEMIF (davinci_nand.o)           |
+----------------------------------+----------------------------------+
| DA850                            | AEMIF (davinci_nand.o)           |
+----------------------------------+----------------------------------+

.. rubric:: **Supported Features**
   :name: supported-features-kernel-nand

GPMC NAND driver supports:

-  NAND devices having:

   -  bus-width = x8 \| x16
   -  page-size = 2048 \| 4096
   -  block-size = 128k \| 256k

-  1-bit Hamming, BCH4, BCH8 and BCH16 ECC schemes.
-  Various transfer modes for different use-cases and applications (like
   Polled, Polled Prefetch, IRQ and DMA).
-  NAND boot support for custom non-ONFI compatible NAND devices using
   NAND-I2C boot-mode (Refer Chapter on *Initialization* in processor's
   TRM).
-  Sub-page write

.. rubric:: Accessing NAND partitions
   :name: accessing-nand-partitions

.. rubric:: Linux
   :name: linux

In Linux, NAND partitions are accessed via mtd devices through the Linux
MTD subsystem. The mtd device names are named /dev/mtdX, where X is and integer.

    .. rubric:: Determine NAND Partition MTD Identifier
       :name: determine-nand-partition-mtd-identifier

    Within the kernel figuring out the mtd device number that is for a
    particular NAND partition is simple. A user simply needs to view the
    list of mtd devices along with its name. Below command will provide this
    information:

    ::

        cat /proc/mtd

    An example of this output performed on the DRA71x EVM can be seen below.

    ::

        dev:    size   erasesize  name
        mtd0: 00010000 00010000 "QSPI.SPL"
        mtd1: 00010000 00010000 "QSPI.SPL.backup1"
        mtd2: 00010000 00010000 "QSPI.SPL.backup2"
        mtd3: 00010000 00010000 "QSPI.SPL.backup3"
        mtd4: 00100000 00010000 "QSPI.u-boot"
        mtd5: 00080000 00010000 "QSPI.u-boot-spl-os"
        mtd6: 00010000 00010000 "QSPI.u-boot-env"
        mtd7: 00010000 00010000 "QSPI.u-boot-env.backup1"
        mtd8: 00800000 00010000 "QSPI.kernel"
        mtd9: 01620000 00010000 "QSPI.file-system"
        mtd10: 00020000 00020000 "NAND.SPL"
        mtd11: 00020000 00020000 "NAND.SPL.backup1"
        mtd12: 00020000 00020000 "NAND.SPL.backup2"
        mtd13: 00020000 00020000 "NAND.SPL.backup3"
        mtd14: 00040000 00020000 "NAND.u-boot-spl-os"
        mtd15: 00100000 00020000 "NAND.u-boot"
        mtd16: 00020000 00020000 "NAND.u-boot-env"
        mtd17: 00020000 00020000 "NAND.u-boot-env.backup1"
        mtd18: 00800000 00020000 "NAND.kernel"
        mtd19: 0f600000 00020000 "NAND.file-system"

    As you can see from the above list, mtd devices not only include NAND
    partitions but other MTD partitions as well (e.g. OSPI).
    e.g. if you want to access the NAND.file-system partition you need to use
    /dev/mtd19. Linux knows the partition names, offsets and sizes via the
    MTD partition entry specified in the boards device tree.

    .. rubric:: Erasing, Reading and Writing
       :name: erasing-reading-and-writing

    For the below sections it is important to remember to replace **mtdX**
    with the appropriate mtd device that is associated with the particular NAND
    partition that you want to use.

    | **Erasing**
    | Erasing a NAND partition can be performed by using the below command:

    ::

        flash_erase /dev/mtdX 0 0

    | **Writing**
    | Writing a NAND partition is usually a two step process. Writing to
      NAND at a bit level is only able to change a bit from 1 to 0. This is
      problematic since frequently when writing new data you will need to
      change many bits from 1 to 0 along with changing some bits from 0 to
      1. The only way to get around this is erasing the NAND partition
      before writing. This is because erasing sets all the bits in a
      partition to 1.

    | The command to write to a NAND partition is below:

    ::

        nandwrite -p /dev/mtdX <filename>

    | **Reading**
    | Reading NAND can be done by running the below command:

    ::

        nanddump /dev/mtdX -f <filename>

    **Note:** The above command by default will save the full partition
    contents to the file. If you are interested in only a certain
    amount of data, additional parameters can be passed to the nanddump
    utility.

.. rubric:: U-boot
   :name: nand-u-boot

Information regarding NAND booting and booting the kernel and file
system from NAND can be found in the U-boot User Guide NAND
section.

Refer :ref:`here <linux-ubifs>` for UBIFS.

.. rubric:: **Board specific configurations**
   :name: board-specific-configurations

| Following table gives details about NAND devices present on various
  EVM boards

+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| EVM      | NAND     | Size     | Bus-Widt | Block-Si | Page-Siz | OOB-Size | ECC      | Hardware |
|          | Part #   |          | h        | ze       | e        | (bytes)  | Scheme   |          |
|          |          |          |          | (KB)     | (KB)     |          |          |          |
+==========+==========+==========+==========+==========+==========+==========+==========+==========+
| AM335x   | MT29F2G0 | 256 MB   | 8        | 128      | 2        | 64       | BCH 8    | GPMC     |
| GP       | 8AB      |          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| AM437x   | MT29F4G0 | 512 MB   | 8        | 256      | 4        | 224      | BCH 16   | GPMC     |
| GP       | 8AB      |          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| AM437x   | MT29F4G0 | 512 MB   | 8        | 256      | 4        | 224      | BCH 16   | GPMC     |
| EPOS     | 8AB      |          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| DRA71x   | MT29F2G1 | 256 MB   | 16       | 128      | 2        | 64       | BCH 8    | GPMC     |
|          | 6AADWP:D |          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| K2G      | MT29F2G1 | 512 MB   | 16       | 128      | 2        | 64       | BCH 16   | GPMC     |
|          | 6ABAFAWP |          |          |          |          |          |          |          |
|          | :F       |          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| K2E      | MT29F4G0 | 1 GB     | 8        | 128      | 2        | 64       | TBD      | AEMIF    |
|          | 8ABBDAH4 |          |          |          |          |          |          |          |
|          | D        |          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| K2L      | MT29F16G | 512 MB   | 8        | 256      | 4        | 224      | TBD      | AEMIF    |
|          | 08ADBCAH |          |          |          |          |          |          | |        |
|          | 4:C      |          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| AM64     | MT29F8G0 | 1024 MB  | 8        | 256      | 4        | 256      | BCH 8    | GPMC     |
|          | 8ADAFAH4 |          |          |          |          |          |          |          |
|          | :F       |          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+
| AM62     | MT29F8G0 | 1024 MB  | 8        | 256      | 4        | 256      | BCH 8    | GPMC     |
|          | 8ADAFAH4 |          |          |          |          |          |          |          |
|          | :F       |          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+----------+----------+

Table:  NAND Flash Specification Summary

.. rubric:: AM43xx GP EVM
   :name: am43xx-gp-evm

On this board, NAND Flash data lines are muxed with eMMC, so either eMMC
or NAND can be used enabled at a time. By default NAND is enabled.

.. rubric:: AM43xx EPOS EVM
   :name: am43xx-epos-evm

On this board, NAND Flash control lines are muxed with QSPI, Thus either
NAND or QSPI-NOR can be used at a time. By default NAND is enabled.

.. rubric:: DRA71x EVM
   :name: dra74x-evm

On the board, NAND Flash signals are muxed between NAND, NOR and Video
Out signals. Therefore, to have the signals properly muxed for NAND to
work Pin 1 (first pin on the left) must be turned on and Pin 2 must be
turned off. Pin 1 and 2 must never be switched on at the same time.
Doing so may cause damage to the board or SoC.

.. rubric:: AM64 GP EVM

NAND flash is not present on the EVM but needs to be added via an Expansion
card (TDMS64DC02EVM) that plugs into the High Speed Expansion (HSE) port.

The NAND flash and SoC supports BCH16 ECC Scheme but the BootROM does not support
BCH16. So BCH8 ECC Scheme has been used on this board.

.. note::

	Aside from setting the correct bootmode (SYSBOOT[5:0]) for
	NAND boot, make sure that The Bus width (SYSBOOT[13]) and
	Muxed-device (SYSBOOT[12:11]) are set as given in the TRM.

.. rubric:: Configurations (GPMC Specific)
   :name: configurations-gpmc-specific

.. rubric:: **How to enable GPMC NAND driver in Linux Kernel ?**
   :name: how-to-enable-gpmc-nand-driver-in-linux-kernel

.. ifconfig:: CONFIG_part_family in ('AM62X_family')

    Apply GPMC NAND overlay at u-boot prompt in AM62x LP-SK board:

    ::

       =>  setenv name_overlays ti/k3-am62x-lp-sk-nand.dtbo

GPMC NAND driver can be enabled/disabled via *Linux Kernel
Configuration* tool. Enable below Configs to enable MTD Support along
with MTD NAND driver support

::

    $ make menuconfig  ARCH=arm


::

    Device Drivers  --->
      <*> Memory Technology Device (MTD) support  --->
        <*>   Caching block device access to MTD devices
        <*>   Enable UBI - Unsorted block images  --->
        NAND  --->
            <*> Raw/Parallel NAND Device Support  --->
                <*>   OMAP2, OMAP3, OMAP4 and Keystone NAND controller
                [*]     Support hardware based BCH error correction
        Partition parsers  --->
            [*]   Command line partition table parsing
            <*> OpenFirmware (device tree) partitioning parser

.. rubric:: Transfer Modes
   :name: transfer-modes

.. rubric:: **Choose correct bus transfer mode**
   :name: choose-correct-bus-transfer-mode

The GPMC NAND driver support following different modes of transfers data
to external NAND device.

-  "prefetch-polled" Prefetch polled mode (default)
-  "polled" Polled mode, without prefetch
-  "prefetch-dma" Prefetch enabled DMA mode
-  "prefetch-irq" Prefetch enabled IRQ mode

Transfer mode can be configured in linux-kernel via DT binding
**<ti,nand-xfer-type>**
Refer: Linux kernel\_docs @
$LINUX/Documentation/devicetree/bindings/mtd/ti,gpmc-nand.yaml

.. rubric:: **DMA vs Non DMA Mode (PIO Mode)**
   :name: dma-vs-non-dma-mode-pio-mode

| The NAND interface is a low speed interface when compared to the main
  CPU. This means for most CPU frequencies
| if the CPU is reading the NAND buffers via polling then its fully
  capable of reading the NAND at its maximum speed.
| Of course the trade off being that the CPU while polling the NAND is
  not capable of doing anything else thus significantly
| increasing the overall CPU load.

| DMA performs best when it can read large amount of data at a time.
  This is necessary since the overhead in setting up, executing and
  returning from a DMA request is not insignificant so to compensate its
  best for the DMA to read/write as much data as possible. This provides
  a dual purpose of significant reduction in CPU load for an operation
  and also high performance.

The current NAND subsystem within Linux currently deals with reading a
single page from the NAND at a time. Unfortunately, the page size is
small enough that the overhead for using the DMA (including Linux DMA
software stack) negatively impacts the performance. Based on nand
performance tests done in early 2016 using the DMA reduced NAND read and
write performance by 10-20% depending on SOC. However, cpu load when
using polling via the same NAND test were around 99%. When using DMA
mode the CPU load for reading was around 35%-54% and for writing was
around 15%-30% depending on SOC.

.. rubric:: **Performance optimizations on NAND**
   :name: performance-optimizations-on-nand

.. rubric:: **Tweak NAND device signal timings**
   :name: tweak-nand-device-signal-timings

Much of the NAND throughput can be improved by matching GPMC signal
timings with NAND device present on the board. Although GPMC signal
timing configurations are not same as those given in NAND device
datasheets, but they can be easily derived based on details given in
GPMC Controller functional specification.

-  Details of GPMC Signal Timing configurations and how to use them can
   be found in TI's Processor TRM

Chapter *General Purpose Memory Controller*
Section *Signal Control*

-  In Linux, GPMC signal timing configurations are specified via DTB.

Refer kernel\_docs
$LINUX/Documentation/devicetree/bindings/memory-controllers/ti,gpmc.yaml

Some timing configurations like <gpmc,rd-cycle-ns>, <gpmc,wr-cycle-ns>
have larger impact on NAND throughput than others.

.. rubric:: **Tweaking UBIFS**
   :name: tweaking-ubifs

-  Specify **-o bulk\_read** while mounting UBIFS `(read
   ahead) <http://www.linux-mtd.infradead.org/doc/ubifs.html#L_readahead>`__
-  Tweak Linux VM `(kernel knobs for
   VM) <http://www.linux-mtd.infradead.org/doc/ubifs.html#L_wb_knobs>`__

.. rubric:: Additional Resources
   :name: additional-resources

Following links should help you better understand NAND Flash as
technology.

http://www.linux-mtd.infradead.org/doc/nand.html
http://www.linux-mtd.infradead.org/doc/ubi.html
http://www.linux-mtd.infradead.org/doc/ubifs.html
https://wiki.linaro.org/Flash%20memory
https://lwn.net/Articles/428584/
