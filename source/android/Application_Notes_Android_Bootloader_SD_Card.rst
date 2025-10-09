.. _android-bootloader-sdcard:

#############################
Android Bootloader on SD Card
#############################

This application note contains steps to flash initial bootloaders
from SD Card instead of using snagboot.

****************
SD Card Creation
****************

In order to flash the AM62x board's eMMC the fist time, a SD card containing the required bootloaders will have to be used
to boot into U-Boot and use fastboot.

.. warning::

   Make sure to use the same bootloaders as the release you are flashing.
   The latest release is ``11.00.00``.

Identify the SD Card
====================

To start, identify your SD card with:

.. code-block:: console

   $ sudo fdisk -l

In this example, the SD card will be: ``/dev/mmcblk0``.

Prepare the SD Card
===================

The preparation of the SD Card is done via the :file:`flashall.sh` script.
Make sure to identify the board model, and the SD card path.

Then, run:

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. code-block:: console

      # If you are using binaries built locally
      $ cd out/target/product/am62x

      (OR)

      # If you are using pre-built binaries from SDK download page
      $ cd AM62x_11.00.00_emmc

      # for AM62x SK EVM (GP)
      $ sudo ./flashall.sh --board am62x-sk --bootloader --sdcard /dev/mmcblk0

      # for AM62x SK EVM (HS-FS)
      $ sudo ./flashall.sh --board am62x-sk --hsfs --bootloader --sdcard /dev/mmcblk0

      # for AM62x LP SK EVM (GP)
      $ sudo ./flashall.sh --board am62x-lp-sk --bootloader --sdcard /dev/mmcblk0

      # for AM62x LP SK EVM (HS-FS)
      $ sudo ./flashall.sh --board am62x-lp-sk --bootloader --hsfs --sdcard /dev/mmcblk0

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. code-block:: console

      # If you are using binaries built locally
      $ cd out/target/product/am62p

      (OR)

      # If you are using pre-built binaries from SDK download page
      $ cd AM62Px_11.00.00_emmc

      $ sudo ./flashall.sh --board am62px-sk --bootloader --sdcard /dev/mmcblk0

.. ifconfig:: CONFIG_part_variant in ('AM67A')

   .. code-block:: console

      # If you are using binaries built locally
      $ cd out/target/product/am67a

      (OR)

      # If you are using pre-built binaries from SDK download page
      $ cd AM67A_11.00.00_emmc

      # for AM67a EVM (HS-FS only)
      $ sudo ./flashall.sh --board am67a-evm --bootloader --sdcard /dev/mmcblk0

*************
eMMC flashing
*************

Flashing instructions
=====================

Once the build is complete, follow the steps below to flash the images to eMMC.
Use the SD card created in previous step to get started.

Procedure is same whether the pre-built images from SDK download page is used or
the images are built from source.

1. Change the Boot Mode DIP switches to SD card boot mode:

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

2. Insert the SD card into the |__PART_FAMILY_NAME__| SK EVM.

3. Ensure the device is plugged in with USB host and debug UART/serial debug

4. Open a terminal debugger to view console output from the device:

   .. ifconfig:: CONFIG_part_variant in ('AM62X','AM62PX')

      .. code-block:: console

         $ sudo picocom -b 115200 -r -l /dev/ttyUSB0

5. Boot the board with SD card.

6. Stop at U-Boot console (interrupt the auto-boot countdown) and do below commands to setup Android
   partition table:

   .. code-block:: console

      => env default -f -a; saveenv

Then, continue following the default :ref:`flashing instructions from step 5<step_5_flashing_instructions>`.
