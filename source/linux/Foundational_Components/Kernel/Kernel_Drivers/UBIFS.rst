UBIFS
-----

.. rubric:: Introduction
   :name: linux-ubifs

Unsorted Block Image File System is a file system specifically designed for
flash memory devices. It's built on top of the UBI layer, which handles
low-level flash management tasks like wear-leveling and bad block management by
dividing it into Logical Erase Blocks (LEBs).

.. rubric:: Using UBIFS on flash
   :name: using-ubifs-on-flash

Flash devices can be divided into multiple partitions, including a rootfs
partition dedicated for the root file system. The rootfs partition can be
formatted with the UBIFS and the volume can be mounted as the root file system
during boot.

.. rubric:: Required Software for UBI image creation
   :name: linux-required-software-ubifs

Building a UBI File System requires two applications, :command:`ubinize` and
:command:`mkfs.ubifs`. Both are both provided by ``mtd-utils`` package.

.. code-block:: console

   $ sudo apt-get install mtd-utils

.. rubric:: Building a UBI File System image
   :name: linux-building-ubi-file-system

.. rubric:: Step 1
   :name: linux-building-ubi-file-system-step1

Create a directory containing the root file system. It is important that the
directory size is smaller than the ``rootfs`` partition in the flash. Users can
download the default/tiny image for specific SoC.

.. note::

   Download and extract ``tisdk-default-image-*-evm.rootfs.tar.xz`` for
   QSPI/OSPI/GPMC NAND.

   Download and extract ``tisdk-tiny-image-*-evm.rootfs.tar.xz`` for QSPI/OSPI
   NOR.

The ``rootfs`` partition information

   OSPI NOR

   .. code-block:: console

      # EVM Linux

      $ mtdinfo /dev/mtd5
      mtd5
      Name:                           ospi.rootfs
      Type:                           nor
      Eraseblock size:                262144 bytes, 256.0 KiB
      Amount of eraseblocks:          223 (58458112 bytes, 55.7 MiB)
      Minimum input/output unit size: 16 bytes
      Sub-page size:                  16 bytes
      Character device major/minor:   90:10
      Bad blocks are allowed:         false
      Device is writable:             true

   OSPI NAND

   .. code-block:: console

      # EVM Linux

      $ mtdinfo /dev/mtd5
      mtd5
      Name:                           ospi_nand.rootfs
      Type:                           nand
      Eraseblock size:                262144 bytes, 256.0 KiB
      Amount of eraseblocks:          383 (100401152 bytes, 95.7 MiB)
      Minimum input/output unit size: 4096 bytes
      Sub-page size:                  4096 bytes
      OOB size:                       128 bytes
      Character device major/minor:   90:10
      Bad blocks are allowed:         true
      Device is writable:             true

   GPMC NAND

   .. code-block:: console

      # EVM Linux

      $ mtdinfo /dev/mtd7
      mtd7
      Name:                           NAND.file-system
      Type:                           nand
      Eraseblock size:                262144 bytes, 256.0 KiB
      Amount of eraseblocks:          4054 (1062731776 bytes, 1013.5 MiB)
      Minimum input/output unit size: 4096 bytes
      Sub-page size:                  1024 bytes
      OOB size:                       256 bytes
      Character device major/minor:   90:14
      Bad blocks are allowed:         true
      Device is writable:             true


.. rubric:: Step 2
   :name: linux-building-ubi-file-system-step2

Create a file named :file:`ubinize.cfg` and add the contents below. Note that
this configuration file can be outside the root directory.

.. code-block:: ini

   [ubifs]
   mode=ubi
   image=rootfs.ubifs
   vol_id=0
   vol_type=dynamic
   vol_name=rootfs
   vol_flags=autoresize

.. rubric:: Step 3
   :name: linux-building-ubi-file-system-step3

:command:`mkfs.ubifs` is used to create UBI File System image, which is
specifically generated for a flash memory device, like Serial NOR, NAND and
Parallel NAND.

Syntax

.. code-block:: console

   mkfs.ubifs -r <root_dir> -o <output_image> [options]

Some key options to use:

1. ``-m <min_io_size>``: specifies the minimum I/O size (in bytes) of the flash
   device.

   .. code-block:: text

      The 'Minimum input/output unit size' value in mtdinfo.

2. ``-e <leb_size>``: specifies the logical eraseblock (LEB) size, which is the
   usable portion of an eraseblock in UBI.

   .. code-block:: text

      Logical Erase Block size = Physical Erase block size - UBI overhead

         Here,
         a. Physical Erase block size is the 'Eraseblock size' value in mtdinfo.
         b. UBI overhead = ALIGN((VID Header offset + sizeof(struct ubi_vid_hdr)), Minimum input/output unit size)

            Here,
            -> ALIGN(x,a) expands to (((x) + ((a) - 1)) & ~((a) - 1))
            -> sizeof(struct ubi_vid_hdr) is 64
            -> Minimum input/output unit size is the 'Minimum input/output unit
            size' value in mtdinfo

   For VID Header offset, refer 4th option, :ref:`here <linux-building-ubi-file-system-step4>`.

3. ``-c <max_leb>``: specifies the maximum number of logical eraseblocks (LEBs)
   the filesystem can use.

   .. code-block:: text

      The 'Amount of eraseblocks' value in mtdinfo.

4. ``-x <compression>``: specifies the compression method to use. Default is
   'zlib'.

5. ``-F``: used to force the filesystem to "fixup" all the free space which it
   is going to use. Note, this flag makes the first mount very slow, because
   the "free space fixup" procedure takes time.

For more details:

.. code-block:: console

   mkfs.ubifs --help

.. rubric:: Step 4
   :name: linux-building-ubi-file-system-step4

:command:`ubinize` is used to create UBI image for one or more UBIFS images.

.. code-block:: console

   ubinize [options] -o <output_image> <configuration_file>

Some key options to use:

1. ``-m <min_io_size>``: specifies the minimum I/O size (in bytes) of the flash
   device.

   .. code-block:: text

      The 'Minimum input/output unit size' value in mtdinfo.

2. ``-p <peb_size>``: specifies the physical eraseblock size, which is the
   total size of an eraseblock in the flash device.

   .. code-block:: text

      The 'Eraseblock size' value in mtdinfo.

3. ``-s <sub_page_size>``: specifies the sub-page size. Usually equivalent to
   the minimum I/O size.

   .. code-block:: text

      The 'Sub-page size' value in mtdinfo.

4. ``-O <vid_hdr_offset>``: specifies the offset of the VID (Volume Identifier)
   header within the physical eraseblock.

   .. code-block:: text

      VID Header offset = ALIGN((sizeof(struct ubi_ec_hdr)), Headers Minimum input/output unit size)

         Here,
         a. ALIGN(x,a) expands to (((x) + ((a) - 1)) & ~((a) - 1))
         b. sizeof(struct ubi_ec_hdr) is 64
         c. Headers Minimum input/output unit size = Minimum input/output unit size >> Sub Page shift

            Here,
            -> Minimum input/output unit size is the 'Minimum input/output unit
            size' value in mtdinfo
            -> Sub Page shift is zero for Serial flashes and [0,2] for Parallel
            flashes

For more details:

.. code-block:: console

   ubinize --help

Example:

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   To generate .ubifs image

      .. code-block:: console

         $ mkfs.ubifs -r /path/to/directory -o rootfs.ubifs -m 16 -e 262016 -c 219

   To generate .ubi image

      .. code-block:: console

         $ ubinize -o rootfs.ubi -m 16 -p 262144 -s 16 -O 64 ubinize.cfg

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   For OSPI NOR:

      To generate .ubifs image

         .. code-block:: console

            $ mkfs.ubifs -r /path/to/directory -o rootfs.ubifs -m 16 -e 262016 -c 219

      To generate .ubi image

         .. code-block:: console

            $ ubinize -o rootfs.ubi -m 16 -p 262144 -s 16 -O 64 ubinize.cfg

   For OSPI NAND:

      To generate .ubifs image

         .. code-block:: console

            $ mkfs.ubifs -r /path/to/directory -o rootfs.ubifs -m 2048 -e 126976 -c 743

      To generate .ubi image

         .. code-block:: console

            $ ubinize -o rootfs.ubi -m 2048 -p 131072 -s 2048 -O 2048 ubinize.cfg

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   To generate .ubifs image

      .. code-block:: console

         $ mkfs.ubifs -r /path/to/directory -o rootfs.ubifs -m 2048 -e 126976 -c 743

   To generate .ubi image

      .. code-block:: console

         $ ubinize -o rootfs.ubi -m 2048 -p 131072 -s 2048 -O 2048 ubinize.cfg

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J7200')

   To generate .ubifs image

      .. code-block:: console

         $ mkfs.ubifs -r /path/to/directory -o rootfs.ubifs -m 16 -e 262016 -c 219

   To generate .ubi image

      .. code-block:: console

         $ ubinize -o rootfs.ubi -m 16 -p 262144 -s 16 -O 64 ubinize.cfg

.. ifconfig:: CONFIG_part_variant in ('J721E')

   To generate .ubifs image

      .. code-block:: console

         $ mkfs.ubifs -r /path/to/directory -o rootfs.ubifs <MKUBIFS ARGS>

   To generate .ubi image

      .. code-block:: console

         $ ubinize -o rootfs.ubi <UBINIZE ARGS> ubinize.cfg

.. ifconfig:: CONFIG_part_variant in ('J721S2', 'J784S4', 'J742S2', 'J722S')

   To generate .ubifs image

      For OSPI NOR:

         .. code-block:: console

            $ mkfs.ubifs -r /path/to/directory -o rootfs.ubifs -m 16 -e 262016 -c 219

      For OSPI NAND:

         .. code-block:: console

            $ mkfs.ubifs -r /path/to/directory -o rootfs.ubifs -m 4096 -e 253952 -c 369

   To generate .ubi image

      For OSPI NOR:

         .. code-block:: console

            $ ubinize -o rootfs.ubi -m 16 -p 262144 -s 16 -O 64 ubinize.cfg

      For OSPI NAND:

         .. code-block:: console

            $ ubinize -o rootfs.ubi -m 16 -p 262144 -s 4096 -O 4096 ubinize.cfg

For GPMC NAND:

   To generate .ubifs image

      .. code-block:: console

         $ mkfs.ubifs -r /path/to/directory -o rootfs.ubifs <MKUBIFS ARGS>

   To generate .ubi image

      .. code-block:: console

         $ ubinize -o rootfs.ubi <UBINIZE ARGS> ubinize.cfg

   +---------------+------------------------------+-----------------------------------+
   | Board Name    | MKUBIFS Args                 | UBINIZE Args                      |
   +===============+==============================+===================================+
   | AM335X GP EVM | -F -m 2048 -e 126976 -c 5600 | -m 2048 -p 128KiB -s 512 -O 2048  |
   +---------------+------------------------------+-----------------------------------+
   | AM437x GP EVM | -F -m 4096 -e 253952 -c 2650 | -m 4096 -p 256KiB -s 4096 -O 4096 |
   +---------------+------------------------------+-----------------------------------+
   | K2E EVM       | -F -m 2048 -e 126976 -c 3856 | -m 2048 -p 128KiB -s 2048 -O 2048 |
   +---------------+------------------------------+-----------------------------------+
   | K2L EVM       | -F -m 4096 -e 253952 -c 1926 | -m 4096 -p 256KiB -s 4096 -O 4096 |
   +---------------+------------------------------+-----------------------------------+
   | K2G EVM       | -F -m 4096 -e 253952 -c 1926 | -m 4096 -p 256KiB -s 4096 -O 4096 |
   +---------------+------------------------------+-----------------------------------+
   | DRA71x EVM    | -F -m 2048 -e 126976 -c 8192 | -m 2048 -p 128KiB -s 512 -O 2048  |
   +---------------+------------------------------+-----------------------------------+
   | AM64 GP EVM   | -F -m 4096 -e 258048 -c 3970 | -m 4096 -p 256KiB -s 1024 -O 1024 |
   +---------------+------------------------------+-----------------------------------+
   | AM62 LP SK    | -F -m 4096 -e 258048 -c 3970 | -m 4096 -p 256KiB -s 1024 -O 1024 |
   +---------------+------------------------------+-----------------------------------+

   Table:  Table of Parameters to use for Building UBI filesystem image

.. rubric:: Step 5
   :name: linux-building-ubi-file-system-step5

Flash :file:`rootfs.ubi` to ``rootfs`` partition

.. code-block:: console

   # EVM Linux

   $ ubiformat -f rootfs.ubi /dev/mtdX
