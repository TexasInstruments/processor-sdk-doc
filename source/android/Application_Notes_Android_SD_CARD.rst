##################
Android on SD Card
##################

This application note contains steps to use SD Card instead of eMMC.


******************************
Build U-Boot with this changes
******************************

Download sources
================

Follow this link to download the :ref:`android-download-bootloaders`.

Apply this patch in U-Boot source code:

    .. code-block:: diff

       diff --git a/configs/am62x_a53_android.config b/configs/am62x_a53_android.config
       index 55fa93b140f9..dd0d36069d74 100644
       --- a/configs/am62x_a53_android.config
       +++ b/configs/am62x_a53_android.config
       @@ -5,7 +5,7 @@ CONFIG_USB_FUNCTION_FASTBOOT=y
        CONFIG_FASTBOOT_BUF_ADDR=0xC0000000
        CONFIG_FASTBOOT_BUF_SIZE=0x2F000000
        CONFIG_FASTBOOT_FLASH=y
       -CONFIG_FASTBOOT_FLASH_MMC_DEV=0
       +CONFIG_FASTBOOT_FLASH_MMC_DEV=1
        CONFIG_CMD_GPT=y # Needed for FASTBOOT_CMD_OEM_FORMAT
        CONFIG_RANDOM_UUID=y # Needed for FASTBOOT_CMD_OEM_FORMAT
        CONFIG_FASTBOOT_CMD_OEM_FORMAT=y
       diff --git a/include/env/ti/android.env b/include/env/ti/android.env
       index a058beb7fc42..693806550853 100644
       --- a/include/env/ti/android.env
       +++ b/include/env/ti/android.env
       @@ -24,8 +24,8 @@ partitions+=name=userdata,size=-,uuid=${uuid_gpt_userdata}
        fastboot_raw_partition_bootenv=0x800 0x400 mmcpart 1
        fastboot.partition-type:metadata=f2fs

       -boot_targets=mmc0
       -mmcdev=0
       +boot_targets=mmc1
       +mmcdev=1
        bootmeths=android
        vendor_boot_comp_addr_r=0xd0000000
        bootcmd=bootflow scan -lb

Build U-Boot
============

Follow this link to build the :ref:`android-build-bootloaders`.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   Rebuild U-Boot then copy :file:`u-boot.img` in Android build system environment : :file:`vendor/ti/am62x/bootloader/am62-sk`

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   Rebuild U-Boot then copy :file:`u-boot.img` in Android build system environment : :file:`vendor/ti/am62x/bootloader/am62px-sk`

Build Android
=============

Follow this link to build :ref:`android-build-aosp`.
Go in your Android environment then rebuild with ``TARGET_SDCARD_BOOT=true`` build args:

.. code-block:: console

   $ cd ${YOUR_PATH}/ti-aosp-16
   $ source build/envsetup.sh
   $ lunch <BUILD_TARGET>
   $ m TARGET_SDCARD_BOOT=true


****************
Flashing SD Card
****************

.. warning::
    Minimal size for SD card is ``16GB``

- Change the boot mode DIP switches to SD card boot mode:

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. list-table::
      :widths: 16 16 16
      :header-rows: 1

      * - Switch Label
        - SW2: 12345678
        - SW3: 12345678

      * - SD
        - 01000000
        - 11000010

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. list-table::
      :widths: 16 16 16
      :header-rows: 1

      * - Switch Label
        - SW5: 12345678
        - SW4: 12345678

      * - SD
        - 01000000
        - 11000010

- Go in :file:`out` directory in android environment.

  .. code-block:: console

     $ cd out/target/product/am62p
     $ sudo ./flashall.sh --board="am62px-sk" --sdcard="/dev/sdX"

  .. note::

     To disable AVB, pass the ``--disable-avb`` argument to :file:`flashall.sh`:

     .. code-block:: console

        $ sudo ./flashall.sh --board="am62px-sk" --sdcard="/dev/sdX" --disable-avb

:file:`flashall.sh` **script print in your console instruction to do**

.. tip::
    Replace X in ``/dev/sdX/`` by letter corresponding to your SD card
