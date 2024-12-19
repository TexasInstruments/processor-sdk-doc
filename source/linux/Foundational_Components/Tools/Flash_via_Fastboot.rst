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

* Snagfactory tool is hosted here `Snagfactory <https://github.com/bootlin/snagboot>`__.
* More info about installation can be found in `Snagfactory Readme <https://github.com/bootlin/snagboot/blob/main/README.md>`__.
* Snagfactory also is available on pip.

 .. code-block:: console

    $ python3 -m pip install --user snagboot

.. note::

   At the time of 10.1 release, the corresponding Snagfactory version was v2.0.

*****************************************
Building bootloader binaries for Recovery
*****************************************

For Snagrecover, bootloader images must support DFU boot and fastboot download.
In addition to USB DFU fragment config (which enables DFU boot) for the u-boot
build, an additional fragment config :file:`am6x_a53_snagfactory.config` needs to be
used, which enables fastboot support in U-Boot and other required configs for
snagfactory.

To build bootloader images for recovery using SDK, following change is needed
in :file:`Rules.make` file present in the top level of Linux SDK Installer.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. code-block:: make

      UBOOT_MACHINE_R5=am62x_evm_r5_defconfig am62x_r5_usbdfu.config

      UBOOT_MACHINE_A53=am62x_evm_r5_defconfig am62x_a53_usbdfu.config am6x_a53_snagfactory.config

      # For AM62X LP

      UBOOT_MACHINE_R5=am62x_lpsk_r5_defconfig am62x_r5_usbdfu.config

      UBOOT_MACHINE_A53=am62x_lpsk_a53_defconfig am62x_a53_usbdfu.config am6x_a53_snagfactory.config

      # For AM62X SIP

      UBOOT_MACHINE_R5=am62xsip_evm_r5_defconfig am62x_r5_usbdfu.config

      UBOOT_MACHINE_A53=am62xsip_evm_a53_defconfig am62x_a53_usbdfu.config am6x_a53_snagfactory.config

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   .. code-block:: make

      UBOOT_MACHINE_R5=am64x_evm_r5_defconfig

      UBOOT_MACHINE_A53=am64x_evm_a53_defconfig am6x_a53_snagfactory.config

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   .. code-block:: make

      UBOOT_MACHINE_R5=am62ax_evm_r5_defconfig am62x_r5_usbdfu.config

      UBOOT_MACHINE_A53=am62ax_evm_a53_defconfig am62x_a53_usbdfu.config am6x_a53_snagfactory.config

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. code-block:: make

      UBOOT_MACHINE_R5=am62px_evm_r5_defconfig am62x_r5_usbdfu.config

      BOOT_MACHINE_A53=am62px_evm_a53_defconfig am62x_a53_usbdfu.config am6x_a53_snagfactory.config

Generate the bootloader images using top-level makefile by running following
commands on the terminal from the top-level of the Linux SDK installer.

.. code-block:: console

   $ make u-boot_clean
   $ make u-boot
   $ make u-boot_stage

Save the bootloader binaries generated in a separate directory. These bootloader
images will be used for recovery and to start flashing the images. The bootloader
images after make can be found in :file:`board-support/built-images`.

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

 .. code-block:: text

    SW2-11001100
    SW3-00000000

* Power on the board.
* Optionally you can also connect host PC to board via UART to read the console logs.

How to use Snagfactory
**********************

Comprehensive instructions for using the Snagfactory tool can be found here.

* `Snagfactory doc <https://github.com/bootlin/snagboot/blob/main/docs/snagfactory.md>`__.
* `Snagfactory config doc <https://github.com/bootlin/snagboot/blob/main/docs/snagfactory_config.md>`__.
