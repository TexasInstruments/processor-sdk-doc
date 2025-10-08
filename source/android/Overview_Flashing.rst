.. _android-flashing:

####################
Flashing Instruction
####################

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   These instructions are for the AM62x SK EVM.
   For flashing the Beagle Play, see the :ref:`beagleplay-app-note`.

.. ifconfig:: CONFIG_part_variant in ('AM67A')

   These instructions are for the AM67A EVM.
   For flashing the BeagleY-AI, see the :ref:`beagley-ai-app-note`.


************
DFU Recovery
************

It's possible to put the |__PART_FAMILY_NAME__| SK EVM in USB DFU mode, which allows
loading bootloaders over DFU. This is done via the ``snagboot`` tool.
This is useful for initial flashing or recovering boards which have broken
bootloaders.

Installation and setup
======================

Install snagboot 1.3.0 following the `official instructions <https://github.com/bootlin/snagboot>`_
Make sure to install the udev rules as documented:

.. code-block:: console

   $ snagrecover --udev > 50-snagboot.rules
   $ sudo cp 50-snagboot.rules /etc/udev/rules.d/
   $ sudo udevadm control --reload-rules
   $ sudo udevadm trigger

.. tip::

    If Snagboot cannot be installed, it's possible to boot the initial bootloaders from an SD card.
    Follow :ref:`android-bootloader-sdcard` if you encounter issues with Snagboot.


eMMC flashing
==============

Flashing instructions
---------------------

Once the build is complete, follow the steps below to flash the images to eMMC.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. Image:: ../images/am62x_sk_evm_setup.jpg

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. Image:: ../images/am62px_sk_evm_setup.png

.. ifconfig:: CONFIG_part_variant in ('AM67A')

   .. Image:: ../images/am67a_evm_setup.jpg

1. Change the boot mode DIP switches to DFU mode:

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      .. list-table::
         :widths: 16 16 16
         :header-rows: 1

         * - Switch Label
           - SW2: 12345678
           - SW3: 12345678

         * - USB DFU
           - 00000000
           - 11001010

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      .. list-table::
         :widths: 16 16 16
         :header-rows: 1

         * - Switch Label
           - SW5: 12345678
           - SW4: 12345678

         * - USB DFU
           - 00000000
           - 11001010

   .. ifconfig:: CONFIG_part_variant in ('AM67A')

      .. list-table::
         :widths: 16 16 16
         :header-rows: 1

         * - Switch Label
           - SW3: 12345678
           - SW4: 12345678

         * - USB DFU
           - 11001010
           - 00000000

2. Ensure the device is plugged in with USB host and debug UART/serial debug

3. Open a terminal debugger to view console output from the device:

   .. code-block:: console

      $ sudo picocom -b 115200 -r -l /dev/ttyUSB0

4. The following sequence assumes that 2 terminals are open:

   - On the left, a terminal to send commands from the PC to the device
   - On the right, the ``picocom`` console to run commands on the device

.. list-table::
   :header-rows: 1

   * - PC
     - Device
   * - run ``snagrecover``:

       .. ifconfig:: CONFIG_part_variant in ('AM62X')

          .. code-block:: console

             # If you are using binaries built locally
             $ cd out/target/product/am62x

             (OR)

             # If you are using pre-built binaries from SDK download page
             $ cd AM62x_11.00.00_emmc

             # for AM62x SK EVM (GP)
             $ snagrecover -s am625 -f ./am62x-sk-evm.yaml

             # for AM62x SK EVM (HS-FS)
             $ snagrecover -s am625 -f ./am62x-sk-evm-hsfs.yaml

             # for AM62x LP SK EVM (GP)
             $ snagrecover -s am625 -f ./am62x-lp-sk-evm.yaml

             # for AM62x LP SK EVM (HS-FS)
             $ snagrecover -s am625 -f ./am62x-lp-sk-evm-hsfs.yaml

       .. ifconfig:: CONFIG_part_variant in ('AM62PX')

         .. code-block:: console

             # If you are using binaries built locally
             $ cd out/target/product/am62p

             (OR)

             # If you are using pre-built binaries from SDK download page
             $ cd AM62Px_11.00.00_emmc

             $ snagrecover -s am625 -f ./am62px-sk-evm-hsfs.yaml

       .. ifconfig:: CONFIG_part_variant in ('AM67A')

         .. code-block:: console

             # If you are using binaries built locally
             $ cd out/target/product/am67a

             (OR)

             # If you are using pre-built binaries from SDK download page
             $ cd AM67A_11.00.00_emmc

             # for AM67A EVM (HS-FS only: by default)
             $ snagrecover -s am62p5 -f ./am67a-evm-hsfs.yaml

       produces::

          Starting recovery of am625 board
          Installing firmware tiboot3
          Searching for partition id...
          Downloading file...
          Could not read status after end of manifest phase
          Done
          Done installing firmware tiboot3
          Installing firmware tispl
          Searching for partition id...
          Downloading file...
          Done
          Done installing firmware tispl
          Installing firmware u-boot
          Searching for partition id...
          Downloading file...
          Done
          Sending detach command...
          Done installing firmware u-boot
          Installing firmware u-boot
          Searching for partition id...
          Downloading file...
          Done
          Sending detach command...
          Done installing firmware u-boot
          Done recovering am625 board

     - Halt the autoboot countdown by pressing any key::

          U-Boot SPL 2023.04-g83660642 (Jul 15 2024 - 11:30:29 +0000)
          SYSFW ABI: 4.0 (firmware rev 0x000a '10.0.6--v10.00.06 (Fiery Fox)')
          SPL initial stack usage: 17048 bytes
          Trying to boot from DFU
          ##########################################################DOWNLOAD ... OK
          Ctrl+C to exit ...
          ##############################################################DOWNLOAD ... OK
          Ctrl+C to exit ...
          Authentication passed
          Authentication passed
          Authentication passed
          init_env from device 10 not supported!
          Authentication passed
          Authentication passed
          Starting ATF on ARM64 core...

          NOTICE:  BL31: v2.10.0(release):09.02.00.009
          NOTICE:  BL31: Built : 11:30:24, Jul 15 2024

          U-Boot SPL 2023.04-g83660642 (Jul 15 2024 - 11:30:56 +0000)
          SYSFW ABI: 4.0 (firmware rev 0x000a '10.0.6--v10.00.06 (Fiery Fox)')
          SPL initial stack usage: 1904 bytes
          Trying to boot from DFU
          #####DOWNLOAD ... OK
          Ctrl+C to exit ...
          Authentication passed
          Authentication passed


          U-Boot 2023.04-g83660642 (Jul 15 2024 - 11:30:56 +0000)

          SoC:   AM62PX SR1.0 HS-FS
          Model: Texas Instruments AM62P5 SK
          DRAM:  2 GiB (effective 8 GiB)
          Core:  80 devices, 30 uclasses, devicetree: separate
          MMC:   mmc@fa10000: 0, mmc@fa00000: 1
          Loading Environment from MMC... OK
          In:    serial
          Out:   serial
          Err:   serial
          Net:   eth0: ethernet@8000000port@1, eth1: ethernet@8000000port@2
          Hit any key to stop autoboot:  0
          =>

   * -
     - .. _step_5_flashing_instructions:

       Ensure the default U-Boot environment is configured with:

       .. code-block:: console

          => env default -f -a; saveenv;
          ## Resetting to default environment
          Saving Environment to MMC... Writing to MMC(0)... OK

       .. tip::

          By default, no Device-Tree Overlays are selected.
          Follow this link to configure :ref:`android-dtbo`

   * -
     - Enable fastboot mode on the device by executing below command.

       Before running this, make sure USB-C cable is connected from the host PC to the EVM:

       .. code-block:: console

          => fastboot 0

   * - Run the the :file:`flashall.sh` script to start flashing the binaries to eMMC:

       .. ifconfig:: CONFIG_part_variant in ('AM62X')

          .. code-block:: console

             # If you are using binaries built locally
             $ cd out/target/product/am62x

             (OR)

             # If you are using pre-built binaries from SDK download page
             $ cd AM62x_11.00.00_emmc

             # for AM62x SK EVM (GP)
             $ sudo ./flashall.sh --board am62x-sk

             # for AM62x SK EVM (HS-FS)
             $ sudo ./flashall.sh --board am62x-sk --hsfs

             # for AM62x LP SK EVM (GP)
             $ sudo ./flashall.sh --board am62x-lp-sk

             # for AM62x LP SK EVM (HS-FS)
             $ sudo ./flashall.sh --board am62x-lp-sk --hsfs

             board: am62x-sk
             Fastboot: ./fastboot
             Generating bootloader-am62x-sk.img ...
             mkfs.fat 4.2 (2021-01-31)
             Generating bootloader-am62x-sk.img: DONE
             Create GPT partition table
             OKAY [  0.032s]

       .. ifconfig:: CONFIG_part_variant in ('AM62PX')

          .. code-block:: console

             # If you are using binaries built locally
             $ cd out/target/product/am62p

             (OR)

             # If you are using pre-built binaries from SDK download page
             $ cd AM62Px_11.00.00_emmc

             $ sudo ./flashall.sh --board am62px-sk
             board: am62px-sk
             Fastboot: ./fastboot
             Generating bootloader-am62px-sk.img ...
             mkfs.fat 4.2 (2021-01-31)
             Generating bootloader-am62px-sk.img: DONE
             Create GPT partition table
             OKAY [  0.032s]

       .. ifconfig:: CONFIG_part_variant in ('AM67A')

          .. code-block:: console

             # If you are using binaries built locally
             $ cd out/target/product/am67a

             (OR)

             # If you are using pre-built binaries from SDK download page
             $ cd AM67A_11.00.00_emmc

             # for AM67A EVM (HS-FS only: by default)
             $ sudo ./flashall.sh --board am67a-evm
             board: am67a-evm
             Fastboot: ./fastboot
             Generating bootloader-am67a-evm.img ...
             mkfs.fat 4.2 (2021-01-31)
             Generating bootloader-am67a-evm.img: DONE
             Create GPT partition table
             OKAY [  0.032s]

     - ::

          Writing GPT: success!
          dwc3-generic-peripheral usb@31000000: request 00000000f7ec4040 was not queued to ep1in-bulk
          ** Bad device specification mmc tiboot3_a **
          ** Bad device specification mmc tiboot3_a **
          Couldn't find partition mmc tiboot3_a
          dwc3-generic-peripheral usb@31000000: request 00000000f7ec4040 was not queued to ep1in-bulk



.. tip::

    If you get ``mcopy`` command not found error on Linux PC, install the ``mtools`` package:

    .. code-block:: console

      $ apt-get install mtools

.. warning::

    It's possible that the in-memory partition layout is still from an older system.

    In that case, we can observe flashing errors similar to::

      writing 'tiboot3'...
      FAILED (remote: invalid partition or device)

    When that happens:

    1. Reboot into the newly flashed bootloader with ``$ fastboot reboot bootloader``
    2. Restart the flashing from :ref:`U-Boot environment <step_5_flashing_instructions>`.


5. Once the flashing is complete, power off the board

6. Change boot mode DIP switches to boot from eMMC user partitions and power cycle the board:

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      .. list-table::
         :widths: 16 16 16
         :header-rows: 1

         * - Switch Label
           - SW2: 12345678
           - SW3: 12345678

         * - EMMC (with UDA)
           - 00000000
           - 11000010

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      .. list-table::
         :widths: 16 16 16
         :header-rows: 1

         * - Switch Label
           - SW5: 12345678
           - SW4: 12345678

         * - EMMC (with UDA)
           - 00000000
           - 11000010

   .. ifconfig:: CONFIG_part_variant in ('AM67A')

      .. list-table::
         :widths: 16 16 16
         :header-rows: 1

         * - Switch Label
           - SW3: 12345678
           - SW4: 12345678

         * - EMMC (with UDA)
           - 11010010
           - 00000000


7. Board should boot the Android images now.

