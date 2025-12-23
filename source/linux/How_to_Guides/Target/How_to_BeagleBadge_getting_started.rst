===========================
BeagleBadge Getting Started
===========================

Overview
========

The BeagleBadge is a compact development platform from BeagleBoard.org powered by the TI AM62L SoC.
Designed for portable and low-power applications, it features built-in Wi-Fi and Bluetooth, multiple
low power modes, and an integrated fuel gauge for precise battery power monitoring.

The board provides a rich interface including an e-paper connector, DSI connector, Grove expansion,
seven-segment displays, and an RGB LED. Fully supported in TI sources, the BeagleBadge offers flexible
boot options (OSPI, UART, SD, USB-DFU) and runs Zephyr or Linux OS with Debian or Arago distributions,
making it an ideal open source solution for modern IoT and HMI projects.

Supported Distributions
=======================

- Debian: https://github.com/TexasInstruments/armbian-build.git branch: 2025.12-beaglebadge
- Arago: https://github.com/TexasInstruments/meta-tisdk branch: scarthgap

Low level sources
=================

- TI Linux: :file:`arch/arm64/boot/dts/til3-am62l3-beaglebadge.dts` branch: ti-linux-6.12.y
- TI U-boot: :file:`configs/am62lx_beaglebadge_defconfig` branch ti-u-boot-2025.01

Building for BeagleBadge
========================

.. code-block:: console

   $ git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
   $ cd tisdk
   $ ./oe-layertool-setup.sh -f configs/arago-scarthgap-config.txt
   $ cd build
   $ . conf/setenv
   $ export MACHINE=beaglebadge-ti
   $ ARAGO_SYSVINIT=1 bitbake -k tisdk-tiny-image

For more information go :ref:`here <building-the-sdk-with-yocto>`

.. note::

   Yocto: Due to the limited 128MB size of LPDDR on BeagleBadge, only the *tisdk-tiny-image*
   can boot on BeagleBadge. Switching to SystemV for init system instead of SystemD will reduce
   the memory footprint since more system services will be enabled by default with SystemD.

Booting BeagleBadge
===================

In the following instructions, assume /dev/ttyUSB0 is the serial port enumerated
on host machine from BeagleBadge USB C connection.

SD boot:
   1. Flash SD card with Debian or Arago image
   2. Insert Micro SD card
   3. Press & hold Select until step 4
   4. Connect USB C cable
   5. Connect to /dev/ttyUSB0 on host machine

OSPI boot:
   1. Boot via SD boot and stop at u-boot prompt
   2. Flash OSPI

      .. code-block:: console

         => fatload mmc 1 ${loadaddr} tiboot3.bin
         221296 bytes read in 11 ms (19.2 MiB/s)
         => print filesize
         filesize=36070
         => sf probe
         SF: Detected is25wx256 with page size 256 Bytes, erase size 4 KiB, total 32 MiB
         => sf erase 0 40000
         SF: 262144 bytes @ 0x0 Erased: OK
         => sf write ${loadaddr} 0 36070
         device 0 offset 0x0, size 0x36070
         SF: 221296 bytes @ 0x0 Written: OK
         => fatload mmc 1 ${loadaddr} tispl.bin
         1464080 bytes read in 62 ms (22.5 MiB/s)
         => print filesize
         filesize=165710
         => sf probe
         SF: Detected is25wx256 with page size 256 Bytes, erase size 4 KiB, total 32 MiB
         => sf erase 0x80000 180000
         SF: 1572864 bytes @ 0x80000 Erased: OK
         => sf write ${loadaddr} 0x80000 165710
         device 0 offset 0x80000, size 0x165710
         SF: 1464080 bytes @ 0x80000 Written: OK
         => fatload mmc 1 ${loadaddr} u-boot.img
         1314747 bytes read in 57 ms (22 MiB/s)
         => print filesize
         filesize=140fbb
         =>  sf probe
         SF: Detected is25wx256 with page size 256 Bytes, erase size 4 KiB, total 32 MiB
         => sf erase 0x280000 180000
         SF: 1572864 bytes @ 0x280000 Erased: OK
         => sf write ${loadaddr} 0x280000 140fbb
         device 0 offset 0x280000, size 0x140fbb
         SF: 1314747 bytes @ 0x280000 Written: OK

   3. Reset the board (S1 RST)

UART boot:
   1. Connect USB C cable
   2. Connect to /dev/ttyUSB0 on host machine
   3. Run the following instructions on host machine:

      .. code-block:: console

         $ sb --xmodem tiboot3.bin > /dev/ttyUSB0 < /dev/ttyUSB0
         $ sb --xmodem tispl.bin > /dev/ttyUSB0 < /dev/ttyUSB0
         $ sb --ymodem u-boot.img > /dev/ttyUSB0 < /dev/ttyUSB0

USB-DFU boot:
   1. Press & hold Select until step 4
   2. Connect USB C cable
   3. Connect to /dev/ttyUSB0 on host machine
   4. Send bootloader binaries from host MACHINE

      .. code-block:: console

         $ sudo -E -S dfu-util -R -a bootloader -D  tiboot3.bin
         $ sudo -E -S dfu-util -R -a bootloader -D  tispl.bin
         $ sudo -E -S dfu-util -R -a u-boot.img -D u-boot.img

Any of the above boot methods can be used to boot to u-boot prompt,
from here, loading the rootfs is generic and can be loaded from SD
card, OSPI flash, or USB DFU as is discussed in other sections of this
documentation.
