.. _u-boot-build-guide-build-omap:

#####
Build
#####

.. _Build-U-Boot-label:

************
Build U-Boot
************

.. note::

   The following commands are intended to be run from the root of the
   U-Boot tree unless otherwise specified. The root of the U-Boot tree is
   the top-level directory and can be identified by looking for the
   "MAINTAINERS" file.

We strongly recommend the use of separate object directories when
building. This is done with O= parameter to make. We also recommend that
you use an output directory name that is identical to the configuration
target name. That way if you are working with multiple configuration
targets it is very easy to know which folder contains the u-boot
binaries that you are interested in.

.. rubric:: Setting the tool chain path

We strongly recommend using the toolchain that came with the Linux Core
release that corresponds to this U-Boot release. For e.g:

.. code-block:: console

   $ export PATH=$HOME/<TOOLCHAIN_PATH>/bin:$PATH

.. rubric:: Cleaning the Sources

If you did not use a separate object directory:

.. code-block:: console

   $ make CROSS_COMPILE=arm-none-linux-gnueabihf- distclean

.. ifconfig:: CONFIG_part_variant in ('AM335X')

   If you used ``O=am335x\_evm`` as your object directory:

   .. code-block:: console

      $ rm -rf ./am335x_evm

.. ifconfig:: CONFIG_part_variant in ('AM437X')

   If you used ``O=am43xx\_evm`` as your object directory:

   .. code-block:: console

      $ rm -rf ./am43xx_evm

.. ifconfig:: CONFIG_part_variant in ('AM57X')

   If you used ``O=am57xx\_evm`` as your object directory:

   .. code-block:: console

      $ rm -rf ./am57xx_evm

.. rubric:: Compiling MLO and u-boot

Building of both u-boot and SPL is done at the same time. You must
however first configure the build for the board you are working with.
Use the following table to determine what defconfig to use to configure
with:

+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| Board                      | SD Boot                     | eMMC Boot                | NAND Boot                                    | UART Boot                | Ethernet Boot            | USB Ethernet Boot        | USB Host Boot                           | SPI Boot                                 |
+============================+=============================+==========================+==============================================+==========================+==========================+==========================+=========================================+==========================================+
| AM335x GP EVM              | ``am335x_evm_defconfig``    |                          | ``am335x_evm_defconfig``                     | ``am335x_evm_defconfig`` | ``am335x_evm_defconfig`` | ``am335x_evm_defconfig`` |                                         |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| AM335x EVM-SK              | ``am335x_evm_defconfig``    |                          |                                              | ``am335x_evm_defconfig`` |                          | ``am335x_evm_defconfig`` |                                         |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| AM335x ICE                 | ``am335x_evm_defconfig``    |                          |                                              | ``am335x_evm_defconfig`` |                          |                          |                                         |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| BeagleBone Black           | ``am335x_evm_defconfig``    | ``am335x_evm_defconfig`` |                                              | ``am335x_evm_defconfig`` |                          |                          |                                         |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| BeagleBone White           | ``am335x_evm_defconfig``    |                          |                                              | ``am335x_evm_defconfig`` |                          |                          |                                         |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| AM437x GP EVM              | ``am43xx_evm_defconfig``    |                          | ``am43xx_evm_defconfig``                     | ``am43xx_evm_defconfig`` | ``am43xx_evm_defconfig`` | ``am43xx_evm_defconfig`` | ``am43xx_evm_usbhost_boot_defconfig``   |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| AM437x EVM-Sk              | ``am43xx_evm_defconfig``    |                          |                                              |                          |                          |                          | ``am43xx_evm_usbhost_boot_defconfig``   |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| AM437x IDK                 | ``am43xx_evm_defconfig``    |                          |                                              |                          |                          |                          |                                         | ``am43xx_evm_qspiboot_defconfig`` (XIP)  |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| AM437x ePOS EVM            | ``am43xx_evm_defconfig``    |                          | ``am43xx_evm_defconfig``                     |                          |                          |                          | ``am43xx_evm_usbhost_boot_defconfig``   |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| AM572x GP EVM              | ``am57xx_evm_defconfig``    |                          |                                              | ``am57xx_evm_defconfig`` |                          |                          |                                         |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| AM572x IDK                 | ``am57xx_evm_defconfig``    |                          |                                              |                          |                          |                          |                                         |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| AM571x IDK                 | ``am57xx_evm_defconfig``    |                          |                                              |                          |                          |                          |                                         |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| DRA74x/DRA72x/DRA71x EVM   | ``dra7xx_evm_defconfig``    | ``dra7xx_evm_defconfig`` | ``dra7xx_evm_defconfig``   (DRA71x EVM only) |                          |                          |                          |                                         | ``dra7xx_evm_defconfig``  (QSPI)         |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| K2HK EVM                   |                             |                          | ``k2hk_evm_defconfig``                       | ``k2hk_evm_defconfig``   | ``k2hk_evm_defconfig``   |                          |                                         | ``k2hk_evm_defconfig``                   |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| K2L EVM                    |                             |                          | ``k2l_evm_defconfig``                        | ``k2l_evm_defconfig``    |                          |                          |                                         | ``k2l_evm_defconfig``                    |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| K2E EVM                    |                             |                          | ``k2e_evm_defconfig``                        | ``k2e_evm_defconfig``    |                          |                          |                                         | ``k2e_evm_defconfig``                    |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| K2G GP EVM                 | ``k2g_evm_defconfig``       |                          |                                              | ``k2g_evm_defconfig``    | ``k2g_evm_defconfig``    |                          |                                         | ``k2g_evm_defconfig``                    |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| K2G ICE                    | ``k2g_evm_defconfig``       |                          |                                              |                          |                          |                          |                                         |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
| OMAP-L138 LCDK             | ``omapl138_lcdk_defconfig`` |                          | ``omapl138_lcdk_defconfig``                  |                          |                          |                          |                                         |                                          |
+----------------------------+-----------------------------+--------------------------+----------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM335X')

   Then (Use ``am335x_evm`` and 'AM335x GP EVM' in this example):

   .. code-block:: console

      $ make CROSS_COMPILE=arm-none-linux-gnueabihf- O=am335x_evm am335x_evm_defconfig
      $ make CROSS_COMPILE=arm-none-linux-gnueabihf- O=am335x_evm

.. ifconfig:: CONFIG_part_variant in ('AM437X')

   Then (Use ``am43xx_evm`` and 'AM437x GP EVM' in this example):

   .. code-block:: console

      $ make CROSS_COMPILE=arm-none-linux-gnueabihf- O=am43xx_evm am43xx_evm_defconfig
      $ make CROSS_COMPILE=arm-none-linux-gnueabihf- O=am43xx_evm

.. ifconfig:: CONFIG_part_variant in ('AM57X')

   Then (Use ``am57xx_evm`` and 'AM57x GP EVM' in this example):

   .. code-block:: console

      $ make CROSS_COMPILE=arm-none-linux-gnueabihf- O=am57xx_evm am57xx_evm_defconfig
      $ make CROSS_COMPILE=arm-none-linux-gnueabihf- O=am57xx_evm

.. note::

   Not all possible build targets for a given platform are listed
   here as the community has additional build targets that are not
   supported by TI. To find these read the :file:`boards.cfg` file and look for
   the build target listed above. And please note that the main config file
   will leverage other files under :file:`include/configs`, as seen by #include
   statements.
