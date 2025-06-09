###########################################
Flash via USB Device Firmware Upgrade (DFU)
###########################################

Flash Writer is a tool used to flash binaries to the on-board memory. This application
note provides instructions on how to use flash writer tool for flashing. Flash
writer script will use USB DFU to boot the board and then flash the binaries to on-board
memory. This tool also supports flashing multiple boards via DFU simultaneously.

********
Get Tool
********

SDK installer
=============

Download and install Processer SDK Installer. For steps refer :ref:`download-and-install-sdk`.

Clone repository
================

The sources are publicly available at `git.ti.com/uboot-flash-writer <https://git.ti.com/cgit/processor-sdk/uboot-flash-writer/>`__.

You can clone the sources on your host by running the following commands,

.. code-block:: console

    git clone https://git.ti.com/git/processor-sdk/uboot-flash-writer.git
    git checkout master

***************
Important files
***************

* :file:`bin/` - Contains boot binaries used to boot the board via USB DFU, also config files
  for GP, HS and HS-SE.
* :file:`src/` - other python modules.
* :file:`dfu_flash.py` - main python script that is to be run.
* Python script for flashing via DFU is located at :file:`<TI_SDK_PATH>/bin/DFU_flash/dfu_flash.py`.
* Config files and example dfu boot binaries are located at :file:`<TI_SDK_PATH>/bin/DFU_flash/bin/<device>/`.

************
Requirements
************

* Linux or Windows Development PC that can access serial console.
* Type C USB cable
* dfu-util program needs to installed on your host.

For Ubuntu
==========

.. code-block:: console

    sudo apt-get install dfu-util

For Windows
===========

Download the dfu-util-0.9-win64.zip file from dfu-util site. Place executable files
in a directory ex. :file:`C:\\Program Files\\dfu-util` and then edit the environment
variables to add this path.

Download Zadig installer from `here <https://zadig.akeo.ie/>`__.

Put the device in DFU mode. Then run the :file:`Zadig_<version>.exe` file.

Select libusbK and then click the Install Driver button. For more information 
about libusbK, refer `wiki <https://github.com/libusb/libusb/wiki/Windows#How%5Fto%5Fuse%5Flibusb%5Fon%5FWindows>`__.

* Python (3.10+)
* dfu-util installed on host (0.11+)
* USB hub to connect multiple boards (Optional)
* UART to read the logs from the EVM (Optional)

****************
Flow of flashing
****************

* Host PC is connected to boards via USB Type C.
* After tool is run, it will detect the boards. Script will send the bootloader 
  binaries ( :file:`tiboot3.bin`, :file:`tispl.bin` and :file:`u-boot.img` ) from host PC to boards and
  boards will be booted.
* After the boards are booted, tool will send :file:`uEnv.txt` file from host PC to boards.
* Environment variables on boards is set using :file:`uEnv.txt` and boards are now ready
  for flashing. tool can now flash files from host PC to boards.

******************************************************
Building bootloader binaries for flashing and DFU boot
******************************************************

Override the bootcmd command to receive the environment variable text file after
DFU boot and flash the binaries/images. Following change needs to be done.

Pre-built DFU boot binaries for TI boards are already present in :file:`bin` directory. To
flash custom board(s) generate the boot binaries and place them in
:file:`<TI_SDK_PATH>/bin/DFU_flash/bin/<board>/<type>` folder.

Following change needs to be done in :file:`<platform>_a53_defconfig` file located at following path
inside the SDK :file:`/board-support/ti-u-boot-2024*/configs/`.

Add or update the CONFIG_BOOTCOMMAND

.. code-block:: text

    CONFIG_BOOTCOMMAND="setenv dfu_alt_info_flashenv uEnv.txt ram 0x82000000 0x10000000; setenv dfu_alt_info ${dfu_alt_info_flashenv}; dfu 0 ram 0; env import -t ${loadaddr} $filesize; run user_commands;"

It will enable script to send uEnv.txt file, import the environment variables
from the uEnv.txt file and run user_commands after DFU boot. The user_commands
variable is defined in the :file:`uEnv.txt` file and the value assigned will be based on
flashing memory and binaries/images to be flashed.

Additionallly, these changes can also be done:

.. code-block:: text

    To make sure board does not use saved environment variables after boot.

    Add below line.
    CONFIG_ENV_IS_NOWHERE=y

    Remove below line.
    CONFIG_ENV_IS_IN_MMC=y

    To decrease boot delay to 0
    CONFIG_BOOTDELAY=0

For DFU boot, build the bootloader images using below configs file. Following
change is needed in :file:`Rules.make` file present in the top level of Linux SDK Installer.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    .. code-block:: make

        UBOOT_MACHINE_R5=am62x_evm_r5_defconfig am62x_r5_usbdfu.config

        # For AM62X LP

        UBOOT_MACHINE_R5=am62x_lpsk_r5_defconfig am62x_r5_usbdfu.config

        # For AM62X SIP

        UBOOT_MACHINE_R5=am62xsip_evm_r5_defconfig am62x_r5_usbdfu.config

.. ifconfig:: CONFIG_part_variant in ('AM64X')

    .. code-block:: make

        UBOOT_MACHINE_R5=am64x_evm_r5_defconfig

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    .. code-block:: make

        UBOOT_MACHINE_R5=am62ax_evm_r5_defconfig am62x_r5_usbdfu.config

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    .. code-block:: make

        UBOOT_MACHINE_R5=am62px_evm_r5_defconfig am62x_r5_usbdfu.config

Generate the bootloader images for DFU boot using top-level makefile by running
following commands on the terminal from the top-level of the Linux SDK installer.

.. code-block:: console

    $ make u-boot_clean
    $ make u-boot

Save the bootloader binaries generated in a separate directory. These bootloader
images will be used for DFU boot and to start flashing the images. The bootloader
images after make will be generated in the following path.


* :file:`board-support/u-boot_build/r5/tiboot3.bin`
* :file:`board-support/u-boot_build/a53/tispl.bin`
* :file:`board-support/u-boot_build/a53/u-boot.img`

DFU boot binaries are required for flashing. These DFU binaries once booted on
the board listens for the images to be flashed over USB DFU. Go to the respective
directory :file:`bin/${device}/${type}` and copy paste the DFU boot binaries (:file:`tiboot3.bin`, :file:`tispl.bin`, :file:`u-boot.img`).

For more details regarding USB DFU refer :ref:`usb-device-firmware-upgrade-label`.

***********
Connections
***********

Power off the EVM and set up the boot mode switches to boot from USB DFU

.. code-block:: text

    SW2-11001100
    SW3-00000000

Power on the board.

Optionally you can also connect host PC to board via UART to read the console logs.

**************************************
Preparing the Flash Configuration file
**************************************

* Go to the directory :file:`bin/${device}/${type}` according to the device and the type.
* Edit the configuration file :file:`flash-files.cfg` to list the commands for each of the files to be flashed.
* For each config line, prepare the following three arguments separated by space.
* Edit the path of files to be flashed using :code:`-file=${path}`.
* Edit the operation using :code:`--operation=${flash-nor|flash-emmc|flash-nand|flash-gpmc_nand}`.
* The operation flash-nor is used to flash the SPI NOR.
* The operation flash-nand is used to flash the SPI NAND.
* The operation flash-emmc is used to flash the eMMC.
* The operation flash-gpmc_nand is used to flash the GPMC NAND.
* Edit the offset using :code:`--offset=${hex_address}`.

******************
Flashing the files
******************

Change the working directory in terminal to flash writer tool directory i.e.
:file:`<TI_SDK_PATH>/bin/DFU_flash/`

.. code-block:: console

    $ ${PYTHON} dfu_flash.py [ -d device ] [ -t type ] [ -c cfg ] [ -r reset]

    where ${PYTHON} evalutes to specific python command according to the OS.
    In most cases, this should be `python` for Windows while `python3` for Linux.

    Options

        - -d | --device : Argument to identify the device (Mandatory).
        - -t | --type   : Argument to identify the type of the device gp,hs,hsfs (Mandatory).
        - -c | --cfg    : Argument to get the path of the custom configuration file.
        - -r | --reset  : Argument to reset the board after flashing.

Flash to eMMC
=============

Flashing to eMMC needs and additional attributes named :code:`--attributes` in flash
configuration file. The key :code:`--attributes` is only valid for eMMC and has the
following value:

.. code-block:: text

    --attributes="<raw|part>,<hwpart>,<partid>"

- Use `raw` for raw flashing to any offset of any hardware partition in eMMC. If `raw`
  is used, only `hwpart` is required and the third parameter `partid` should be set to `-`.
- Use `part` for raw flashing to a partition defined in GPT or DOS partition table. If `part`
  is used, both `hwpart` & `partid` are required.
- It should be noted using `part` requires a partition table already in the respective
  hardware partition in eMMC. For steps refer :ref:`partitioning-eMMC-from-uboot`.

In the config file, specify operation as

.. code-block:: text

    --operation=flash-emmc

Run following command in Linux or Windows to start the flash tool.

.. code-block:: console

    $ ${PYTHON} dfu_flash.py -d <device> -t <type> -c <cfg file>


Flash to SPI NOR
================

In the config file, specify operation as

.. code-block:: text

    --operation=flash-nor

Run following command in Linux or Windows host to start the flash tool.

.. code-block:: console

    $ ${PYTHON} dfu_flash.py -d <device> -t <type> -c <cfg file>

Flash to SPI NAND
=================

In the config file, specify operation as

.. code-block:: text

    --operation=flash-nand

Run following command in Linux or Windows host to start the flash tool.

.. code-block:: console

    $ ${PYTHON} dfu_flash.py -d <device> -t <type> -c <cfg file>

Flash to GPMC NAND
==================

In the config file, specify operation as

.. code-block:: text

    --operation=flash-gpmc_nand

Run following command in Linux or Windows host to start the flash tool.

.. code-block:: console

    $ ${PYTHON} dfu_flash.py -d <device> -t <type> -c <cfg file>
