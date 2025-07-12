SPI
------------------------------------

.. ifconfig:: CONFIG_part_family in ('J7_family')

    .. note::
        SPI is not supported on J721E platform (not be confused with QSPI/OSPI).

This section documents how to write files to the SPI device and use it
to load and then boot the Linux Kernel using a root filesystem also
found on SPI. At this time, no special builds of U-Boot are required to
perform these operations on the supported hardware. The table below
however, lists builds that will also use the SPI flash for the
environment instead of the default, which typically is NAND in AM57x and
DRA7x EVMs, but in Keystone-2 EVMs, it is only NOR. Finally, for
simplicity we assume the files are being loaded from an SD card. Using
the network interface (if applicable) is documented above.

Writing to SPI from U-Boot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note for AM57x and DRA7x platforms:

-  From the U-Boot build, the **MLO.byteswap** and **u-boot.img** files
   are the ones to be written.
-  We load all files from an SD card in this example but they can just
   as easily be loaded via network (documented above) or other interface
   that exists.
-  At this time the SPI mtd partition map has not yet been updated to
   include an example location for the device tree.

::

    U-Boot # mmc rescan
    U-Boot # sf probe 0
    U-Boot # sf erase 0 +80000
    U-Boot # fatload mmc 0 ${loadaddr} MLO.byteswap
    U-Boot # sf write ${loadaddr} 0 ${filesize}
    U-Boot # fatload mmc 0 ${loadaddr} u-boot.img
    U-Boot # sf write ${loadaddr} 0x20000 ${filesize}
    U-Boot # sf erase 80000 +${spiimgsize}
    U-Boot # fatload mmc 0 ${loadaddr} zImage
    U-Boot # sf write ${loadaddr} ${spisrcaddr} ${filesize}


.. ifconfig:: CONFIG_part_family not in ('AM57X_family')

   Note for Keystone-2 (K2H/K/E/L/G) platforms:

   -  From the U-Boot build, the **u-boot-spi.gph** file is the one to be
      written.
   -  We load the file from a tftp server via netowrk in this example.
   -  The series commands burns the u-boot image to the SPI NOR flash

   ::

      U-Boot # env default -f -a
      U-Boot # setenv serverip <ip address of tftp server>
      U-Boot # setenv tftp_root <tftp root directory>
      U-Boot # setenv name_uboot u-boot-spi.gph
      U-Boot # run get_uboot_net
      U-Boot # run burn_uboot_spi

|

Booting from SPI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Within the default environment for each board that supports SPI there is
a boot command called **spiboot** that will automatically load the
kernel and boot. For the exact details of each use **printenv** on the
**spiboot** variable and then in turn **printenv** other sub-sections of
the command. The most important variables here are **spiroot** and
**spirootfstype**. For Keystone-2 platforms, it is configured to be
**ARM SPI** boot mode using SW1 dip switch setting. Please refer to the
Hardware Setup of each Keystone-2 EVM.
