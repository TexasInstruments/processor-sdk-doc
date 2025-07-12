.. _usb-device-firmware-upgrade-label:

USB Device Firmware Upgrade (DFU)
-----------------------------------

When working with USB Device Firmware Upgrade (DFU), regardless of the
medium to be written to and of the board being used, there are some
general things to keep in mind. First of all, you will need to get a
copy of the **dfu-util** program installed on your host. If your
distribution does not provide this package you will need to build it
from source. Second, the examples that follow assume a single board is
plugged into the host PC. If you have more than one device plugged in
you will need to use the options that **dfu-util** provides for
specifying a single device to work with. Finally, to program via DFU for
a given storage device see the section for the storage device you are
working with.

USB Peripheral boot mode (SPL-DFU support)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The USB Peripheral boot mode is used to boot using USB
interface using SPL-DFU feature. Steps outlined here can be used on
platform that support USB Peripheral boot mode.

.. ifconfig:: CONFIG_part_family in ('General_family')

  #. Enable the SPL-DFU feature in u-boot and build MLO/u-boot binaries.
  #. Load the MLO and u-boot.img using the dfu-util from host PC.
  #. Once the u-boot is up, use DFU command from u-boot to flash the
     binary images from Host PC (using dfu-utils tool) to the eMMC, or
     QSPI to fresh/factory boards.

  -  Example provided here is for dra7xx platform.

  -  Use default "dra7xx\_evm\_defconfig" to build spl/u-boot-spl.bin,
     u-boot.img.

  ::

       host$ make dra7xx_evm_defconfig
       host$ make menuconfig

       select SPL/DFU support
       menuconfig->SPL/TPL--->
          ..
          [*] Support booting from RAM
          [*] Support USB Gadget drivers
          [ ]    Support USB Ethernet drivers
          [*]    Support DFU (Device Firmware Upgrade)
                    DFU device selection (RAM device) -->

  ::

       Unselect CONFIG_HUSH_PARSER
       menuconfig--->Command Line interface
          [*] Support U-boot commands
          [ ]   Use hush shell


  -  Build spl/u-boot-spl.bin and u-boot.img

  ::

       host$ make

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM57X_family')

   -  Set SYSBOOT SW2 switch to USB Peripheral boot mode

   ::

        SW2[7..0] = 00010000 (refer to TRM for various booting order)

   -  Connect EVM Superspeed port (USB1 port) to PC (Ubuntu) through USB
      cable.
   -  From Ubuntu (or the host) PC, fetch and build usbboot application.
      usbboot pre-built binaries for particular distributions may be
      available in :ref:`Processor SDK Linux <linux-index>`
      already. Here are the steps to build usbboot application.

   ::

       host$ git clone git://git.omapzoom.org/repo/omapboot.git
       host$ cd omapboot
       host$ checkout 609ac271d9f89b51c133fd829dc77e8af4e7b67e
       host$ make -C host/tools

   This results in host side tool called ``usbboot-stand-alone``

   For loading spl/u-boot-spl.bin to EVM, issue the command below and reset
   the board.

   ::

       host$ sudo usbboot-stand-alone -S spl/u-boot-spl.bin

   -  Load the u-boot.img to RAM.

   ::

       host$ sudo dfu-util -l

   ::

       Found DFU: [0451:d022] devnum=0, cfg=1, intf=0, alt=0, name="kernel"
       Found DFU: [0451:d022] devnum=0, cfg=1, intf=0, alt=1, name="fdt"
       Found DFU: [0451:d022] devnum=0, cfg=1, intf=0, alt=2, name="ramdisk"

   ::

       host$ sudo dfu-util c 1 -i 0 -a 0 -D "u-boot.img" -R

   -  Now EVM will boot to u-boot prompt.

.. ifconfig:: CONFIG_part_family in ('AM64X_family')

  #. Build the bootloader images using default "am64x_evm_r5_defconfig"
     and "am64x_evm_a53_defconfig" configs files. The configs required for
     DFU boot as well as DFU in U-Boot are already enabled. For instructions
     to build the bootloader images please refer to :ref:`Build-U-Boot-label`.
  #. Load the bootloader images tiboot3.bin, tispl.bin and u-boot.img using
     the dfu-util from host PC.
  #. Once the U-Boot is up, use DFU command from u-boot to flash the
     binary images from Host PC (using dfu-utils tool) to the eMMC, or
     QSPI to fresh/factory boards.

.. ifconfig:: CONFIG_part_family in ('AM62X_family')

  .. note::

     Please refer to :ref:`workarounds` to fix the USB Device Firmware Upgrade (DFU) Boot
     failure in AM62x.

  #. Build :program:`tiboot3.bin` using :file:`am62x_evm_r5_defconfig` along
     with :file:`am62x_r5_usbdfu.config` fragment. Build :program:`tispl.bin`
     and :program:`u-boot.img` using :file:`am62x_evm_a53_defconfig`.
     For instructions to build the bootloader images please refer to
     :ref:`Build-U-Boot-label`.
  #. Load the bootloader images :program:`tiboot3.bin`, :program:`tispl.bin`
     and :program:`u-boot.img` using the dfu-util tool on the Host PC.
  #. Once U-Boot is up, use the DFU command at U-Boot prompt to flash the
     binary images from the Host PC (using dfu-utils tool) to the eMMC, or
     QSPI to fresh/factory boards.


.. ifconfig:: CONFIG_part_family in ('AM62AX_family')

  #. Build :program:`tiboot3.bin` using :file:`am62ax_evm_r5_defconfig` along
     with :file:`am62x_r5_usbdfu.config` fragment. Build :program:`tispl.bin`
     and :program:`u-boot.img` using :file:`am62ax_evm_a53_defconfig`.
     For instructions to build the bootloader images please refer to
     :ref:`Build-U-Boot-label`.
  #. Load the bootloader images :program:`tiboot3.bin`, :program:`tispl.bin`
     and :program:`u-boot.img` using the dfu-util tool on the Host PC.
  #. Once U-Boot is up, use the DFU command at U-Boot prompt to flash the
     binary images from the Host PC (using dfu-utils tool) to the eMMC, QSPI
     or OSPI to fresh/factory boards.

.. ifconfig:: CONFIG_part_family in ('AM62LX_family')

  #. Build :program:`tiboot3.bin`, :program:`tispl.bin` and :program:`u-boot.img`
     using :file:`am62lx_evm_defconfig`. For instructions to build the bootloader
     images please refer to :ref:`Build-U-Boot-label`.
  #. Load the bootloader images :program:`tiboot3.bin`, :program:`tispl.bin`
     and :program:`u-boot.img` using the dfu-util tool on the Host PC.
  #. Once U-Boot is up, use the DFU command at U-Boot prompt to flash the
     binary images from the Host PC (using dfu-utils tool) to the eMMC, QSPI
     or OSPI to fresh/factory boards.


.. ifconfig:: CONFIG_part_family in ('AM62PX_family')

  #. Build :program:`tiboot3.bin` using :file:`am62px_evm_r5_defconfig` along
     with :file:`am62x_r5_usbdfu.config` fragment. Build :program:`tispl.bin`
     and :program:`u-boot.img` using :file:`am62px_evm_a53_defconfig`.
     For instructions to build the bootloader images please refer to
     :ref:`Build-U-Boot-label`.
  #. Load the bootloader images :program:`tiboot3.bin`, :program:`tispl.bin`
     and :program:`u-boot.img` using the dfu-util tool on the Host PC.
  #. Once U-Boot is up, use the DFU command at U-Boot prompt to flash the
     binary images from the Host PC (using dfu-utils tool) to the eMMC, QSPI
     or OSPI to fresh/factory boards.


.. ifconfig:: CONFIG_part_variant in ('J722S')

  #. Build :program:`tiboot3.bin` using :file:`j722s_evm_r5_defconfig` along
     with :file:`am62x_r5_usbdfu.config` fragment. Build :program:`tispl.bin`
     and :program:`u-boot.img` using :file:`j722s_evm_a53_defconfig`.
     For instructions to build the bootloader images please refer to
     :ref:`Build-U-Boot-label`.
  #. Load the bootloader images tiboot3.bin, tispl.bin and u-boot.img using
     the dfu-util from host PC.
  #. Once the U-Boot is up, use DFU command from u-boot to flash the
     binary images from Host PC (using dfu-utils tool) to the eMMC, QSPI
     or OPSI to fresh/factory boards.

.. ifconfig:: CONFIG_part_family not in ('AM62X_family', 'AM62AX_family', 'AM62PX_family', 'AM57X_family')

    .. rubric:: USB Peripheral boot mode on |__PART_FAMILY_DEVICE_NAMES__| EVM (SPL-DFU boot mode)

.. ifconfig:: CONFIG_part_family in ('AM62X_family', 'AM62AX_family', 'AM62PX_family')

    .. rubric:: USB Peripheral boot mode on |__PART_FAMILY_DEVICE_NAMES__| SK (SPL-DFU boot mode)

.. ifconfig:: CONFIG_part_variant in ('J721E')

    -  Set SYSBOOT switches to USB Peripheral boot mode (Refer to **Initialization** chapter of J721E TRM for boot switch details)
    -  Make sure USB0 port in UFP/DRP mode: SW3[3:4] = 01 or 1x
    -  Connect EVM's TypeC port (USB0 port) to PC through USB cable
    -  Power on the board

.. ifconfig:: CONFIG_part_variant in ('J7200', 'J721S2', 'J784S4','J742S2')

    -  Set SYSBOOT switches to USB Peripheral boot mode (Refer to **Initialization** chapter of TRM for boot switch details)
    -  Make sure USB0 port in UFP/DRP mode: SW3[3:4] = 01 or 1x
    -  Connect EVM's TypeC port (USB0 port) to PC through USB cable
    -  Power on the board


.. ifconfig:: CONFIG_part_variant in ('J722S')

    -  Set SYSBOOT switches to USB Peripheral boot mode (Refer to **Initialization** chapter of TRM for boot switch details)
    -  Make sure USB0 port in UFP/DRP mode: SW2[2:3] = 01 or 00
    -  Connect EVM's TypeC port (USB0 port) to PC through USB cable
    -  Power on the board

.. ifconfig:: CONFIG_part_family in ('AM64X_family')

    - Set SYSBOOT switches to USB Peripheral boot mode (Refer to **Initialization** chapter of AM64 TRM for boot switch details)
    - For AM64X GP EVM, SYSBOOT switch settings are SW2[1:8] = 11001010 and  SW3[1:8] = 00000000. Also, the jumper on pin header J23 has to be removed.
    - Connect USB 2.0 Port on EVM to PC through USB cable
    - Power on the board

.. ifconfig:: CONFIG_part_family in ('AM62X_family')

    - Set SYSBOOT switches to USB DFU boot mode (Refer to **Initialization** chapter of AM62 TRM for boot switch details)
    - Connect USB Type C DRD Port (J13) on SK board to PC through USB cable
    - Power on the board


.. ifconfig:: CONFIG_part_family in ('AM62AX_family')

    - Set SYSBOOT switches to USB DFU boot mode (Refer to **Initialization** chapter of AM62A TRM for boot switch details)
    - Connect USB Type C DRD Port (J15) on SK board to PC through USB cable
    - Power on the board

.. ifconfig:: CONFIG_part_family in ('AM62LX_family')

    - Set SYSBOOT switches to USB DFU boot mode (Refer to **Initialization** chapter of AM62L TRM for boot switch details)
    - Connect USB Type C DRD Port (J19) on EVM board to PC through USB cable
    - Power on the board

.. ifconfig:: CONFIG_part_family in ('AM62PX_family')

    - Set SYSBOOT switches to USB DFU boot mode (Refer to **Initialization** chapter of AM62P TRM for boot switch details)
    - Connect USB Type C DRD Port (J19) on SK board to PC through USB cable
    - Power on the board

.. ifconfig:: CONFIG_part_family in ('AM64X_family', 'J7_family', 'AM62X_family', 'AM62AX_family', 'AM62PX_family', 'AM62LX_family')

    .. rubric:: On Linux host

    .. code-block:: text

        host$ sudo dfu-util -l

    .. rubric:: On Windows host

    Download dfu-util from *Releases* section of `dfu-util Homepage <http://dfu-util.sourceforge.net/>`_ and extract the zip file.

    .. code-block:: text

        host> dfu-util.exe -l

    This will show the following DFU entities:

.. ifconfig:: CONFIG_part_variant in ('J7200')

    .. code-block:: text

		Found DFU: [0451:6164] ver=0200, devnum=99, cfg=1, intf=0, path="3-3", alt=1, name="SocId", serial="01.00.00.00"
		Found DFU: [0451:6164] ver=0200, devnum=99, cfg=1, intf=0, path="3-3", alt=0, name="bootloader", serial="01.00.00.00"

    Send boot images in this order: tiboot3.bin -> tispl.bin -> u-boot.img.

.. ifconfig:: CONFIG_part_variant in ('J721S2')

    .. code-block:: text

		Found DFU: [0451:6168] ver=0200, devnum=99, cfg=1, intf=0, path="3-3", alt=1, name="SocId", serial="01.00.00.00"
		Found DFU: [0451:6168] ver=0200, devnum=99, cfg=1, intf=0, path="3-3", alt=0, name="bootloader", serial="01.00.00.00"

    Send boot images in this order: tiboot3.bin -> tispl.bin -> u-boot.img.

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

    .. code-block:: text

		Found DFU: [0451:6167] ver=0200, devnum=44, cfg=1, intf=0, path="1-10", alt=1, name="SocId", serial="01.00.00.00"
		Found DFU: [0451:6167] ver=0200, devnum=44, cfg=1, intf=0, path="1-10", alt=0, name="bootloader", serial="01.00.00.00"

    Send boot images in this order: tiboot3.bin -> tispl.bin -> u-boot.img.

.. ifconfig:: CONFIG_part_variant in ('J721E')

    .. code-block:: text

		Found DFU: [0451:6163] ver=0200, devnum=50, cfg=1, intf=0, path="3-2", alt=1, name="SocId", serial="01.00.00.00"
		Found DFU: [0451:6163] ver=0200, devnum=50, cfg=1, intf=0, path="3-2", alt=0, name="bootloader", serial="01.00.00.00"

    Send boot images in this order: tiboot3.bin -> sysfw.itb -> tispl.bin -> u-boot.img.


.. ifconfig:: CONFIG_part_variant in ('J722S')

    .. code-block:: text

		Found DFU: [0451:6165] ver=0200, devnum=9, cfg=1, intf=0, path="1-2.2", alt=1, name="SocId", serial="01.00.00.00"
		Found DFU: [0451:6165] ver=0200, devnum=9, cfg=1, intf=0, path="1-2.2", alt=0, name="bootloader", serial="01.00.00.00"

    Send boot images in this order: tiboot3.bin -> tispl.bin -> u-boot.img

.. ifconfig:: CONFIG_part_family in ('AM64X_family', 'AM62X_family', 'AM62AX_family', 'AM62PX_family', 'AM62LX_family')

    .. code-block:: text

		Found DFU: [0451:6165] ver=0200, devnum=9, cfg=1, intf=0, path="1-2.2", alt=1, name="SocId", serial="01.00.00.00"
		Found DFU: [0451:6165] ver=0200, devnum=9, cfg=1, intf=0, path="1-2.2", alt=0, name="bootloader", serial="01.00.00.00"

    Send boot images in this order: tiboot3.bin -> tispl.bin -> u-boot.img

    .. note:: On Windows, if you face any issues while listing the available DFU Interfaces, try installing/updating the Generic USB DFU Drivers using `Zadig <https://zadig.akeo.ie/>`_.

.. ifconfig:: CONFIG_part_family in ('AM64X_family', 'J7_family', 'AM62X_family', 'AM62AX_family', 'AM62PX_family', 'AM62LX_family')

    Move to directory containing the images and give the following commands

.. ifconfig:: CONFIG_part_variant in ('J7200')

    .. code-block:: text

		host$ sudo dfu-util -R -a bootloader -D tiboot3.bin
		host$ sudo dfu-util -l
		  Found DFU: [0451:6164] ver=0224, devnum=100, cfg=1, intf=0, path="3-3", alt=1, name="u-boot.img", serial="UNKNOWN"
		  Found DFU: [0451:6164] ver=0224, devnum=100, cfg=1, intf=0, path="3-3", alt=0, name="tispl.bin", serial="UNKNOWN"

		host$ sudo dfu-util -R -a tispl.bin -D tispl.bin
		host$ sudo dfu-util -R  -a u-boot.img -D u-boot.img

.. ifconfig:: CONFIG_part_variant in ('J721S2')

    .. code-block:: text

		host$ sudo dfu-util -R -a bootloader -D tiboot3.bin
		host$ sudo dfu-util -l
		  Found DFU: [0451:6168] ver=0224, devnum=100, cfg=1, intf=0, path="3-3", alt=1, name="u-boot.img", serial="UNKNOWN"
		  Found DFU: [0451:6168] ver=0224, devnum=100, cfg=1, intf=0, path="3-3", alt=0, name="tispl.bin", serial="UNKNOWN"

		host$ sudo dfu-util -R -a tispl.bin -D tispl.bin
		host$ sudo dfu-util -R  -a u-boot.img -D u-boot.img

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

     .. code-block:: text

		host$ sudo dfu-util -R -a bootloader -D tiboot3.bin
		host$ sudo dfu-util -l
		  Found DFU: [0451:6168] ver=0224, devnum=47, cfg=1, intf=0, path="1-10", alt=1, name="u-boot.img", serial="UNKNOWN"
		  Found DFU: [0451:6168] ver=0224, devnum=47, cfg=1, intf=0, path="1-10", alt=0, name="tispl.bin", serial="UNKNOWN"

		host$ sudo dfu-util -R -a tispl.bin -D tispl.bin
		host$ sudo dfu-util -R  -a u-boot.img -D u-boot.img

.. ifconfig:: CONFIG_part_variant in ('J721E')

    .. code-block:: text

		host$ sudo dfu-util -R -a bootloader -D tiboot3.bin
		host$ sudo dfu-util -l
		  Found DFU: [0451:6163] ver=0224, devnum=51, cfg=1, intf=0, path="3-2", alt=0, name="sysfw.itb", serial="UNKNOWN"

		host$ sudo dfu-util -R -a sysfw.itb -D sysfw.itb
		host$ sudo dfu-util -l
		  Found DFU: [0451:6163] ver=0224, devnum=52, cfg=1, intf=0, path="3-2", alt=1, name="u-boot.img", serial="UNKNOWN"
		  Found DFU: [0451:6163] ver=0224, devnum=52, cfg=1, intf=0, path="3-2", alt=0, name="tispl.bin", serial="UNKNOWN"

		host$ sudo dfu-util -R -a tispl.bin -D tispl.bin
		host$ sudo dfu-util -R  -a u-boot.img -D u-boot.img


.. ifconfig:: CONFIG_part_variant in ('J722S')

    .. rubric:: On Linux host

    .. code-block:: text

		host$ sudo dfu-util -R -a bootloader -D tiboot3.bin
		host$ sudo dfu-util -l
		  Found DFU: [0451:6165] ver=0224, devnum=11, cfg=1, intf=0, path="1-2.2", alt=1, name="u-boot.img", serial="UNKNOWN"
		  Found DFU: [0451:6165] ver=0224, devnum=11, cfg=1, intf=0, path="1-2.2", alt=0, name="tispl.bin", serial="UNKNOWN"

		host$ sudo dfu-util -R -a tispl.bin -D tispl.bin
		host$ sudo dfu-util -R -a u-boot.img -D u-boot.img

.. ifconfig:: CONFIG_part_family in ('AM64X_family', 'AM62X_family', 'AM62AX_family', 'AM62PX_family')

    .. rubric:: On Linux host

    .. code-block:: text

		host$ sudo dfu-util -R -a bootloader -D tiboot3.bin
		host$ sudo dfu-util -l
		  Found DFU: [0451:6165] ver=0224, devnum=11, cfg=1, intf=0, path="1-2.2", alt=1, name="u-boot.img", serial="UNKNOWN"
		  Found DFU: [0451:6165] ver=0224, devnum=11, cfg=1, intf=0, path="1-2.2", alt=0, name="tispl.bin", serial="UNKNOWN"

		host$ sudo dfu-util -R -a tispl.bin -D tispl.bin
		host$ sudo dfu-util -R -a u-boot.img -D u-boot.img

    .. rubric:: On Windows host

    .. code-block:: text

        host> dfu-util.exe -R -a 0 -D tiboot3.bin
        host> dfu-util.exe -l
          Found DFU: [0451:6165] devnum=0, cfg=1, intf=0, alt=0, name="tispl.bin"
          Found DFU: [0451:6165] devnum=0, cfg=1, intf=0, alt=1, name="u-boot.img"

        host> dfu-util.exe -R -a 0 -D tispl.bin
        host> dfu-util.exe -R -a 1 -D u-boot.img

    .. note:: On Windows host, if `name` of the DFU Interface doesn't work, use `alt` number instead.

.. ifconfig:: CONFIG_part_family in ('AM62LX_family')

    .. rubric:: On Linux host

    .. code-block:: text

		host$ sudo dfu-util -R -a bootloader -D tiboot3.bin
		host$ sudo dfu-util -l
		  Found DFU: [0451:6165] ver=0200, devnum=45, cfg=1, intf=0, path="1-4.2", alt=1, name="SocId", serial="01.00.00.00"
		  Found DFU: [0451:6165] ver=0200, devnum=45, cfg=1, intf=0, path="1-4.2", alt=0, name="bootloader", serial="01.00.00.00"

		host$ sudo dfu-util -R -a bootloader -D tispl.bin
		host$ sudo dfu-util -R -a u-boot.img -D u-boot.img

    .. rubric:: On Windows host

    .. code-block:: text

        host> dfu-util.exe -R -a 0 -D tiboot3.bin
        host> dfu-util.exe -l
          Found DFU: [0451:6165] devnum=0, cfg=1, intf=0, alt=0, name="bootloader"
          Found DFU: [0451:6165] devnum=0, cfg=1, intf=0, alt=1, name="SocId"

        host> dfu-util.exe -R -a 0 -D tispl.bin
        host> dfu-util.exe -R -a 1 -D u-boot.img

    .. note:: On Windows host, if `name` of the DFU Interface doesn't work, use `alt` number instead.

.. ifconfig:: CONFIG_part_family in ('AM64X_family', 'J7_family', 'AM62X_family', 'AM62AX_family', 'AM62PX_family', 'AM62LX_family')

    At this point, the board should boot to the U-Boot prompt.

.. ifconfig:: CONFIG_part_variant in ('J721E')

    .. note::
        This mode is not supported on J721E Rev E2 and earlier boards.
