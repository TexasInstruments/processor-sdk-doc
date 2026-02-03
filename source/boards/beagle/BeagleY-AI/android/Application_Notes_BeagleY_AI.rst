.. _beagley-ai-app-note:

###########################
BeagleY-AI Application Note
###########################

************
Introduction
************

Beagley AI is built around the Texas Instruments J722s SoC.
the J722s is Quad-Core Arm® Cortex®-A53 SoC.
It comes with 4Gb RAM, has no eMMC, and uses an SD card.

***********
Limitations
***********

Known Issues
============

* Audio is not functional
* Bluetooth is not functional

Untested Features
=================

The following features have not been validated in this release:

* Ethernet connectivity
* PCI Express (PCIe) interface
* Board identifier EEPROM
* LVDS display interface
* MIPI-DSI display interface
* DSP for AI acceleration
* Audio subsystem


******************
Building the image
******************

To build the image you need to build the image for the am67a-evm.
The kernel includes the appropriate device tree and the proper bootloaders are deployed.

   .. code-block:: console

      $ source build/envsetup.sh
      $ lunch am67a-bp2a-user/userdebug
      $ m TARGET_SDCARD_BOOT=true
      $ sudo flashall --board am67a-beagley-ai --sdcard=/dev/sdX

   TARGET_SDCARD_BOOT=true is required since the beagley-ai does not have an eMMC.

**************************
Initial flashing procedure
**************************

Flashing Android requires to use the sdcard.

1. Plug a 16Gb+ sdcard into your host computer

2. Run the flashall script with the following arguments:

   .. code-block:: console

      # Replace X with your sdcard endpoint
      $ sudo flashall --board am67a-beagley-ai --sdcard=/dev/sdX

   The script will only flash the bootloader and require you transfer
   the sdcard to the beagley-ai.
   The script will give the following instructions:

   .. code-block:: console

      Insert SD card on board, Power ON and interrupt U-Boot to go in console to do this command:
      Interrupt U-boot  to go in console:
      => fastboot 0
      When it's Done
      Press any key to continue...

   Keep this terminal open.

3. Open a terminal debugger to view console output from the device:

   .. code-block:: console

      $ sudo picocom -b 115200 -r -l /dev/ttyACM0

4. Start fastboot

   You must interrupt the bootloader when it gives the prompt:

   .. code-block:: console

      SoC:   J722S SR1.0 HS-FS
      Model: BeagleBoard.org BeagleY-AI
      DRAM:  2 GiB (total 4 GiB)
      Core:  89 devices, 30 uclasses, devicetree: separate
      MMC:   mmc@fa00000: 1
      Loading Environment from MMC... MMC Device 0 not found
      *** Warning - No MMC card found, using default environment

      In:    serial@2800000
      Out:   serial@2800000
      Err:   serial@2800000
      Net:   eth0: ethernet@8000000port@1
      Press SPACE to abort autoboot in 2 seconds


   Press space to get access to the prompt and then issue tho fastboot command:

   .. code-block:: console

      => fastboot 0

   This will put the bootloader in fastboot mode so the host can flash the android images.

5. Continue flashing

   In the previous terminal where the sdcard script was started, press enter to continue
   the flashing process.

   This will enable the fastboot flashing process that will format and flash the sdcard on the beagley-ai.

   .. code-block:: console

     Finished. Total time: 112.819s
     -------------------------------
     flashing done, you can issue the 'fastboot reboot' command

   At which point the board is flash and can reboot. It will boot to Android.
