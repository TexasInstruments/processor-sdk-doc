.. _Flash-via-Fastboot:

##################
Flash via Fastboot
##################

This application note provides instructions on using Snagfactory tool for flashing.

The Snagfactory tool has two main operations:

* Snagrecover: Boots the board (recovery) using USB DFU.
* Snagflash: Flashes binaries to the on-board memory using the Fastboot protocol.

This tool supports flashing multiple boards simultaneously, enhancing efficiency in producion
enviroment.

**********************
Installing Snagfactory
**********************

Install using the SDK installer (recommended)
=============================================

The Linux SDK installer includes a setup script that installs Snagboot and
configures udev rules automatically.

.. code-block:: console

   $ cd <sdk_install_dir>
   $ ./bin/setup-snagboot.sh

To also install the optional Snagfactory GUI:

.. code-block:: console

   $ ./bin/setup-snagboot.sh --gui

The script installs Snagboot by using pip, sets up udev rules so USB access works
without root, and verifies the installation. If pip installs the tools to
:file:`~/.local/bin` but that directory is not on ``PATH``, add the following to :file:`~/.bashrc`:

.. code-block:: console

   $ export PATH="$HOME/.local/bin:$PATH"

Manual installation
===================

If the SDK installer is not available, install Snagboot directly by using pip:

* Snagfactory tool is hosted here `Snagfactory <https://github.com/bootlin/snagboot>`__.
* More info about installation can be found in `Snagfactory Readme <https://github.com/bootlin/snagboot/blob/main/README.md>`__.

.. code-block:: console

   $ python3 -m pip install --user snagboot
   $ python3 -m pip install --user snagboot[gui]

After installation, set up udev rules so USB access works without root:

.. code-block:: console

   $ python3 -m snagrecover --udev | sudo tee /etc/udev/rules.d/80-snagboot.rules
   $ sudo udevadm control --reload-rules && sudo udevadm trigger

***************************************
Build boot loader binaries for recovery
***************************************

For Snagrecover, boot loader images must support Device Firmware Upgrade (DFU) boot
and fastboot download. The u-boot build requires the USB DFU fragment config to enable
DFU boot. It also requires the additional fragment config
:file:`am6x_a53_snagfactory.config`, that enables fastboot support in U-Boot and other
required configs for :command:`snagfactory`.

Build using the SDK installer (recommended)
===========================================

The Linux SDK installer includes a dedicated Makefile target that builds
boot loader images with all the required DFU and Fastboot configuration
fragments applied automatically.

From the top level of the Linux SDK installer:

.. code-block:: console

   $ make u-boot-snagboot_clean
   $ make u-boot-snagboot
   $ make u-boot-snagboot_stage

The build places the staged boot loader images in
:file:`board-support/built-images/snagboot/`. The directory contains:

* :file:`tiboot3.bin` (R5 Secondary Program Loader (SPL), or A53 SPL for AM62L)
* :file:`tispl.bin` (A53 SPL with DFU and fastboot support)
* :file:`u-boot.img` (U-Boot with fastboot support)

.. note::

   For AM62L, only the A53 build is needed. The ``u-boot-snagboot`` target
   handles this automatically.

Manual build
============

If the SDK installer is not available, apply the required config fragments
manually by editing :file:`Rules.make` in the top level of the Linux SDK and
then running the standard u-boot build.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. code-block:: make

      UBOOT_MACHINE_R5=am62x_evm_r5_defconfig am62x_r5_usbdfu.config

      UBOOT_MACHINE=am62x_evm_a53_defconfig am62x_a53_usbdfu.config am6x_a53_snagfactory.config

      # For AM62X LP

      UBOOT_MACHINE_R5=am62x_lpsk_r5_defconfig am62x_r5_usbdfu.config

      UBOOT_MACHINE=am62x_lpsk_a53_defconfig am62x_a53_usbdfu.config am6x_a53_snagfactory.config

      # For AM62X SIP

      UBOOT_MACHINE_R5=am62xsip_evm_r5_defconfig am62x_r5_usbdfu.config

      UBOOT_MACHINE=am62xsip_evm_a53_defconfig am62x_a53_usbdfu.config am6x_a53_snagfactory.config

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. code-block:: make

      UBOOT_MACHINE_R5=am64x_evm_r5_defconfig

      UBOOT_MACHINE=am64x_evm_a53_defconfig am6x_a53_snagfactory.config

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   .. code-block:: make

      UBOOT_MACHINE_R5=am62ax_evm_r5_defconfig am62x_r5_usbdfu.config

      UBOOT_MACHINE=am62ax_evm_a53_defconfig am62x_a53_usbdfu.config am6x_a53_snagfactory.config

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. code-block:: make

      UBOOT_MACHINE_R5=am62px_evm_r5_defconfig am62x_r5_usbdfu.config

      UBOOT_MACHINE=am62px_evm_a53_defconfig am62x_a53_usbdfu.config am6x_a53_snagfactory.config

.. ifconfig:: CONFIG_part_variant in ('AM62DX')

   .. code-block:: make

      UBOOT_MACHINE_R5=am62dx_evm_r5_defconfig am62x_r5_usbdfu.config

      UBOOT_MACHINE=am62dx_evm_a53_defconfig am62x_a53_usbdfu.config am6x_a53_snagfactory.config

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. code-block:: make

      UBOOT_MACHINE=am62lx_evm_defconfig am62x_a53_usbdfu.config am6x_a53_snagfactory.config

Then build using the top-level makefile:

.. code-block:: console

   $ make u-boot_clean
   $ make u-boot
   $ make u-boot_stage

The boot loader images are placed in :file:`board-support/built-images`.

For more details regarding USB DFU refer :ref:`usb-device-firmware-upgrade-label`.

.. note::

   ``CONFIG_FASTBOOT_BUF_SIZE`` is defined in :file:`am6x_a53_snagfactory.config`
   and specifies the maximum buffer size for flashing files. Its value must be equal
   or greater than the largest file size being flashed. If smaller, non-sparse
   images will not flash correctly due to issues with chunked processing.

***********
Connections
***********

* Power off the EVM and set up the boot mode switches to boot from USB DFU.

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      AM62X (SK-AM62B-P1) - USB-DFU Boot

      .. code-block:: text

         SW2 - BOOTMODE[8:15]   = 00000000
         SW1 - BOOTMODE[0:7]    = 11001010

   .. ifconfig:: CONFIG_part_variant in ('AM62AX')

      AM62A (SK-AM62A-LP) - USB-DFU Boot

      .. code-block:: text

         SW3 - BOOTMODE[8:15]   = 00000000
         SW2 - BOOTMODE[0:7]    = 11001010

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      AM62P (SK-AM62P-LP) - USB-DFU Boot

      .. code-block:: text

         SW5 - BOOTMODE[8:15]   = 00000000
         SW4 - BOOTMODE[0:7]    = 11001010

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      AM62L (TMDS62LEVM) - USB-DFU Boot

      .. code-block:: text

         SW2 - BOOTMODE[8:11]    = 0000
         SW3 - BOOTMODE[12:15]   = 0000
         SW4 - BOOTMODE[0:7]     = 11001010

   .. ifconfig:: CONFIG_part_variant in ('AM64X')

      AM64X (TMDS64EVM) - USB-DFU Boot

      .. code-block:: text

         SW2 - BOOTMODE[0:7] = 11001010
         SW3 - BOOTMODE[8:15] = 00000000

* Power on the board.
* Optionally you can also connect host PC to board by using UART to read the console logs.

How to use Snagfactory
======================

Comprehensive instructions for installation of the Snagfactory tool are here:

* `Snagfactory doc <https://github.com/bootlin/snagboot/blob/main/docs/snagfactory.md>`__.
* `Snagfactory config doc <https://github.com/bootlin/snagboot/blob/main/docs/snagfactory_config.md>`__.

YAML configuration files
=========================

Ready-to-use YAML configuration files for all supported platforms are bundled
with the SDK installer under:

.. code-block:: text

   <sdk_install_dir>/bin/snagboot_flash/yaml/<board>/

The same configuration files are also available from the TI GitHub repository:

`snagfactory-configs <https://github.com/TexasInstruments/snagfactory-configs>`__

Before using a YAML file, replace the two path placeholders with actual paths
to your binaries:

* ``<path_to_snagboot_binaries>/`` — recovery boot loader images built with
  ``u-boot-snagboot`` (placed in :file:`board-support/built-images/snagboot/`)
* ``<path_to_flash_binaries>/`` — production images to be written to the
  target non-volatile memory

**SnagFactory GUI Tool Configuration and Device Flashing Procedure**

The tool currently supports MMC and MTD backends for flashing images.

.. note::

   SnagFactory GUI tool is a prerequisite for this procedure.

The following steps outline the process for configuring and flashing a device by using
the SnagFactory GUI tool.

.. figure:: /images/snagfactory.png
   :height: 500
   :width: 800

**Step 1: Launch SnagFactory GUI Tool**

* Launch the SnagFactory GUI tool to begin the configuration and device flashing process.

.. code-block:: console

   $ snagfactory

**Step 2: Select configuration file option**

* Upon launch, the SnagFactory GUI tool will present the option to add a configuration file.
  Select the conf option to proceed with loading the configuration file.

**Step 3: Load YAML configuration file**

* Load the YAML configuration file for the platform. This file has the necessary settings
  and parameters for the device flashing process.

**Step 4: Flash the device**

* Once you load the YAML configuration file, the SnagFactory GUI tool will flash the device with
  the specified configuration.

The following table outlines the board names for :command:`snagfactory` YAML configuration.

.. list-table::
   :header-rows: 1

   * - Evaluation Board
     - Family
     - board
   * - am62pxx-evm
     - am6x
     - am62p
   * - am62xx-evm
     - am6x
     - am625
   * - am62lxx-evm
     - am62lx
     - am62l3
   * - am62xx-lp-evm
     - am6x
     - am625
   * - am62sip-evm
     - am6x
     - am625
   * - am62dxx-evm
     - am6x
     - am62d2
   * - am62axx-evm
     - am6x
     - am62a7
   * - am64xx-evm
     - am6x
     - am6442

The example configuration files for **emmc** and **ospi-nand** and **ospi-nor** are as follows.

For reference, the :file:`ospi-nor.yaml` file for **am62p** platform can be as follows:

.. code-block:: yaml

   boards:
     0451:6165: am62p
   soc-models:
     am62p-firmware:
       tiboot3:
         path: "<path_to_snagboot_binaries>/tiboot3.bin"
       tispl:
         path: "<path_to_snagboot_binaries>/tispl.bin"
       u-boot:
         path: "<path_to_snagboot_binaries>/u-boot.img"
     am62p-tasks:
     - eraseblk-size: 0x40000
       fb-buffer-addr: 0x82000000
       fb-buffer-size: 0x7000000
       target-device: nor0
     - task: run
       args:
         - "oem_run:mtd list"
         - "oem_run:setenv mtdids nor0=nor0"
     - task: mtd-parts
       args:
         - name: ospi.tiboot3
           size: 0x80000
         - name: ospi.tispl
           size: 0x200000
         - name: ospi.u-boot
           size: 0x400000
     - task: flash
       args:
         - image: "<path_to_flash_binaries>/tiboot3.bin"
           part: ospi.tiboot3
         - image: "<path_to_flash_binaries>/tispl.bin"
           part: ospi.tispl
         - image: "<path_to_flash_binaries>/u-boot.img"
           part: ospi.u-boot

For reference, the :file:`ospi-nand.yaml` file for **am62xx-lp** platform can be as follows:

.. code-block:: yaml

   boards:
     0451:6165: am625
   soc-models:
     am625-firmware:
       tiboot3:
         path: "<path_to_snagboot_binaries>/tiboot3.bin"
       tispl:
         path: "<path_to_snagboot_binaries>/tispl.bin"
       u-boot:
         path: "<path_to_snagboot_binaries>/u-boot.img"
     am625-tasks:
     - eraseblk-size: 0x40000
       fb-buffer-addr: 0x82000000
       fb-buffer-size: 0x7000000
       target-device: spi-nand0
     - task: run
       args:
         - "oem_run:mtd list"
         - "oem_run:setenv mtdids spi-nand0=spi-nand0"
     - task: mtd-parts
       args:
         - name: ospi_nand.tiboot3
           size: 0x80000
         - name: ospi_nand.tispl
           size: 0x200000
         - name: ospi_nand.u-boot
           size: 0x400000
         - name: ospi_nand.env
           size: 0x40000
         - name: ospi_nand.env.backup
           size: 0x40000
         - name: ospi_nand.rootfs
           size: 0x5fc0000
           start: 0x2000000
         - name: ospi_nand.phypattern
           start: 0x7fc0000
           size: 0x40000
     - task: flash
       args:
         - image: "<path_to_flash_binaries>/tiboot3.bin"
           part: ospi_nand.tiboot3
         - image: "<path_to_flash_binaries>/tispl.bin"
           part: ospi_nand.tispl
         - image: "<path_to_flash_binaries>/u-boot.img"
           part: ospi_nand.u-boot

For reference, the :file:`emmc.yaml` file for **am62p** platform can be as follows:

.. code-block:: yaml

   boards:
     "0451:6165": "am62p"
   soc-models:
     am62p-firmware:
         tiboot3:
           path: "<path_to_snagboot_binaries>/tiboot3.bin"
         tispl:
           path: "<path_to_snagboot_binaries>/tispl.bin"
         u-boot:
           path: "<path_to_snagboot_binaries>/u-boot.img"
     am62p-tasks:
       - target-device: mmc0
         fb-buffer-addr: 0x82000000
         fb-buffer-size: 0x7000000
       - task: gpt
         args:
           - name: rootfs
             size: 1G
       - task: reset
       - task: flash
         args:
           - image: "<path_to_flash_binaries>/tiboot3.bin"
             image-offset: 0x0
             part: "hwpart 1"
           - image: "<path_to_flash_binaries>/tispl.bin"
             image-offset: 0x80000
             part: "hwpart 1"
           - image: "<path_to_flash_binaries>/u-boot.img"
             image-offset: 0x280000
             part: "hwpart 1"
           - image: "<path_to_flash_binaries>/rootfs.ext4"
             part: "rootfs"

For reference, the :file:`emmc.yaml` file for **am62l** platform can be as follows:

.. code-block:: yaml

   boards:
     "0451:6165": "am62l3"

   soc-models:
     am62l3-firmware:
         tiboot3:
           path: "<path_to_snagboot_binaries>/tiboot3.bin"
         tispl:
           path: "<path_to_snagboot_binaries>/tispl.bin"
         u-boot:
           path: "<path_to_snagboot_binaries>/u-boot.img"

     am62l3-tasks:
       - target-device: mmc0
         fb-buffer-addr: 0x82000000
         fb-buffer-size: 0x7000000

       - task: gpt
         args:
           - name: rootfs
             size: 15G

       - task: reset

       - task: flash
         args:
           - image: "<path_to_flash_binaries>/tiboot3.bin"
             image-offset: 0x0
             part: "hwpart 1"
           - image: "<path_to_flash_binaries>/tispl.bin"
             image-offset: 0x80000
             part: "hwpart 1"
           - image: "<path_to_flash_binaries>/u-boot.img"
             image-offset: 0x280000
             part: "hwpart 1"
           - image: "<path_to_flash_binaries>/rootfs.ext4"
             part: "rootfs"

For eMMC boot configuration, refer :ref:`emmc_boot_config`

**Snagboot command-line configuration and device flashing procedure**

Snagrecover uses vendor-specific ROM code mechanisms to initialize external RAM and run U-Boot, without modifying any non-volatile memories.

.. code-block:: console

   $ snagrecover -s am625 -F "{'tiboot3': {'path': 'tiboot3.bin'}}" -F "{'tispl': {'path': 'tispl.bin'}}" -F "{'u-boot': {'path': 'u-boot.img'}}"

* Comprehensive instructions for using :command:`snagrecover` command line are here:
  `Snagrecover command line <https://github.com/bootlin/snagboot/blob/main/docs/snagrecover.md>`__.

Snagflash communicates with U-Boot to flash system images to non-volatile memories, using either DFU, UMS or Fastboot.

.. code-block:: console

   $ snagflash -P fastboot-uboot -p 0451:6165 -i

* Comprehensive instructions for using :command:`snagflash` command line are here:
  `Snagflash command line <https://github.com/bootlin/snagboot/blob/main/docs/snagflash.md>`__.
