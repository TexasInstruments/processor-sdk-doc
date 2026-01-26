#########
Boot Flow
#########

BeagleBadge has a `TI AM62L SoC <https://www.ti.com/product/AM62L/>`__, refer to :ref:`AM62Lx Boot Flow <Boot-Flow-label>`
for more details on AM62L boot flow.

############
Applications
############

- Deep Sleep Low Power mode as low as 350mW power draw
- RTC only mode with 3-5mW power draw
- E-Paper display support with tinyDRM
- Battery-powered with fuel gauge monitoring

#################
Low level sources
#################

.. list-table::
   :header-rows: 1
   :widths: 15, 15, 15

   * - Component
     - Branch
     - Source File
   * - U-Boot
     - `ti-u-boot-2025.01 <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/log/?h=ti-u-boot-2025.01>`__
     - :file:`configs/am62lx_beaglebadge_defconfig`
   * - Linux Kernel
     - `ti-linux-6.12.y <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.12.y>`__
     - :file:`arch/arm64/boot/dts/ti/k3-am62l3-beaglebadge.dts`

########################
Building for BeagleBadge
########################

.. code-block:: console

   $ git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
   $ cd tisdk
   $ ./oe-layertool-setup.sh -f configs/arago-scarthgap-config.txt
   $ cd build
   $ . conf/setenv
   $ export MACHINE=beaglebadge-ti
   $ ARAGO_SYSVINIT=1 bitbake -k tisdk-tiny-image

For more information on building Arago for BeagleBadge, go :ref:`here <building-the-sdk-with-yocto>`.

.. note::

   Yocto: Due to the 256MB size of LPDDR on BeagleBadge, there may be limited free memory (about 17-20MB)
   for developing applications with the **default**, TI-provided Arago distribution image. Switching to
   sysVinit for init system instead of systemd can help reduce the memory footprint further. Please go
   `here <https://www.linuxjournal.com/content/embracing-future-transition-sysvinit-systemd-linux>`__
   for a comparison of both init systems.

To build Armbian for BeagleBadge, refer to **Debian SDK user manual** found `here <https://www.ti.com/tool/download/AM62L-LINUX-SDK>`__.

###################
Booting BeagleBadge
###################

BeagleBadge supports four boot modes with the following configuration:

+-------------------------+-------------------+------------------+
| Button *Select* Pressed | Primary boot mode | Backup boot mode |
+=========================+===================+==================+
| Yes                     | SD boot           | USB-DFU boot     |
+-------------------------+-------------------+------------------+
| No                      | OSPI boot         | UART boot        |
+-------------------------+-------------------+------------------+

In the following instructions, assume /dev/ttyUSB0 is the serial port enumerated
on host machine from BeagleBadge USB C connection.

*******
SD boot
*******

   1. Flash SD card with Debian or Arago image
   2. Insert Micro SD card
   3. Press & hold **Select** until step 5
   4. Connect USB C cable
   5. Connect to /dev/ttyUSB0 on host machine

*********
OSPI boot
*********

   1. Boot via SD boot and stop at u-boot prompt
   2. Flash OSPI

      .. code-block:: console

         => sf probe
         SF: Detected is25wx256 with page size 256 Bytes, erase size 4 KiB, total 32 MiB
         => fatload mmc 1 ${loadaddr} tiboot3.bin
         221296 bytes read in 11 ms (19.2 MiB/s)
         => sf update ${loadaddr} 0 ${filesize}
         device 0 offset 0x0, size 0x36070
         SF: 221296 bytes @ 0x0 Written: OK
         => fatload mmc 1 ${loadaddr} tispl.bin
         1464080 bytes read in 62 ms (22.5 MiB/s)
         => sf update ${loadaddr} 0x80000 ${filesize}
         device 0 offset 0x80000, size 0x165710
         SF: 1464080 bytes @ 0x80000 Written: OK
         => fatload mmc 1 ${loadaddr} u-boot.img
         1314747 bytes read in 57 ms (22 MiB/s)
         => sf update ${loadaddr} 0x280000 ${filesize}
         device 0 offset 0x280000, size 0x140fbb
         SF: 1314747 bytes @ 0x280000 Written: OK

   3. Cold reset the board by disconnecting and reconnecting USB C cable.
   4. Reconnect to /dev/ttyUSB0 on host machine

*********
UART boot
*********

   1. Connect USB C cable
   2. Connect to /dev/ttyUSB0 on host machine
   3. Run the following instructions on host machine:

      .. code-block:: console

         $ sb --xmodem tiboot3.bin > /dev/ttyUSB0 < /dev/ttyUSB0
         $ sb --xmodem tispl.bin > /dev/ttyUSB0 < /dev/ttyUSB0
         $ sb --ymodem u-boot.img > /dev/ttyUSB0 < /dev/ttyUSB0

************
USB-DFU boot
************

   1. Press & hold **Select** until step 4
   2. Connect USB C cable
   3. Connect to /dev/ttyUSB0 on host machine
   4. Send boot loader binaries from host MACHINE

      .. code-block:: console

         $ sudo -E -S dfu-util -R -a bootloader -D  tiboot3.bin
         $ sudo -E -S dfu-util -R -a bootloader -D  tispl.bin
         $ sudo -E -S dfu-util -R -a u-boot.img -D u-boot.img

Any of the above boot methods can be used to boot to u-boot prompt,
from here, loading the rootfs is generic and can be loaded from SD
card, OSPI flash, or USB DFU as is discussed in other sections of this
documentation.
