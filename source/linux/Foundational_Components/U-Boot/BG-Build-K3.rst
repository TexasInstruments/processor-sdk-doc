.. _u-boot-build-guide-build-k3:

#####
Build
#####

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. rubric:: Build BL-1

   .. note::

      The following commands are intended to be run from the root of the
      TF-A tree unless otherwise specified. The root of the TF-A tree is
      the top-level directory and can be identified by looking for the
      "licenses" directory.

   .. rubric:: Setting up the toolchain paths

   .. include:: ../../Overview/GCC_ToolChain.rst
      :start-after: .. start_include_yocto_toolchain_host_setup
      :end-before: .. end_include_yocto_toolchain_host_setup

   .. code-block:: console

      $ cd <path to tf-a dir>

      $ make CROSS_COMPILE="$CROSS_COMPILE_64" ARCH=aarch64 PLAT=k3 TARGET_BOARD=am62l am62l_bl1

      <or to build bl-1 and bl-31 binaries from TF-A repo>

	   $ make CROSS_COMPILE="$CROSS_COMPILE_64" ARCH=aarch64 PLAT=k3 TARGET_BOARD=am62l

.. _Build-U-Boot-label:

************
Build U-Boot
************

.. note::

   The following commands are intended to be run from the root of the
   U-Boot tree unless otherwise specified. The root of the U-Boot tree is
   the top-level directory and can be identified by looking for the
   "MAINTAINERS" file.

.. ifconfig:: CONFIG_part_variant not in ('AM65X', 'AM64X', 'AM62LX')

   .. note:: Note about HSM Rearchitecture

      After HSM rearchitecture in bootloader, loading of remote cores with firmware
      will be supported at A72 SPL stage only and not at R5 SPL stage. Early loading
      of remote core firmware in R5 SPL requires core reset functionality. As part
      of HSM rearchitecture, this functionality has moved into the DM service which
      requires SPL to re-implement device and clock control. This support is not
      present in Uboot R5 SPL due to memory constraints on the existing 64-bit TI devices.

.. ifconfig:: CONFIG_part_variant not in ('AM65X', 'AM62LX')

   .. note::
      As of Processor SDK 9.0, compilation of bootloader images will no longer require
      different defconfigs for GP and HS devices. The same build commands will generate images
      for GP, HS-SE and HS-FS devices.

.. rubric:: Prebuilt Images

Several prebuilt images are required from the TI Processor SDK for building U-Boot on K3 based platforms.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   - TF-A (**BL-1** and **BL-31**): Refer to :ref:`foundational-components-atf`
     for more information
   - ti-linux-firmware (**BINMAN_INDIRS**): Prebuilt TIFS binaries are
     available in `ti-linux-firmware <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/?h=ti-linux-firmware>`__.

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   - TF-A (BL-31): Refer to :ref:`foundational-components-atf` for more information
   - OP-TEE (TEE): Refer to :ref:`foundational-components-optee` for more information
   - ti-linux-firmware (BINMAN_INDIRS): Prebuilt binaries for DM and SYSFW available `here
     <https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/log/?h=ti-linux-firmware>`__.

All of these are available in the SDK at :file:`<path to tisdk>/board-support/prebuilt-images>`

Go :ref:`here <download-and-install-sdk>` to download and install the SDK.

.. rubric:: Setting up the toolchain paths

.. include:: ../../Overview/GCC_ToolChain.rst
   :start-after: .. start_include_yocto_toolchain_host_setup
   :end-before: .. end_include_yocto_toolchain_host_setup

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   .. rubric:: Compiling R5 and ARM64 images

   Use the following table to determine what defconfig to use to configure with:

.. ifconfig:: CONFIG_part_variant in ('AM65X')

   +----------------------------+------------------------------------+--------------------------------+--------------------------------+
   |  Board                     |   SD / eMMC / UART / OSPI Boot     |         Hyper Flash            |           USB DFU              |
   +============================+====================================+================================+================================+
   |    AM65x EVM/IDK           |   ``am65x_evm_r5_defconfig``       |                                |                                |
   |                            |   ``am65x_evm_a53_defconfig``      |                                |                                |
   +----------------------------+------------------------------------+--------------------------------+--------------------------------+
   |    AM65x HS EVM/IDK        | ``am65x_hs_evm_r5_defconfig``      |                                |                                |
   |                            | ``am65x_hs_evm_a53_defconfig``     |                                |                                |
   +----------------------------+------------------------------------+--------------------------------+--------------------------------+

   *on GP*

   .. code-block:: console

      $ cd <path to u-boot dir>

      R5
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" am65x_evm_r5_defconfig O=<output directory>/r5
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" O=<output directory>/r5 BINMAN_INDIRS=<path to tisdk>/board-support/prebuilt-images

      A53
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am65x_evm_a53_defconfig O=<output directory>/a53
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=<path to tisdk>/board-support/prebuilt-images/bl31.bin TEE=<path to tisdk>/board-support/prebuilt-images/bl32.bin O=<output directory>/a53 BINMAN_INDIRS=<path to tisdk>/board-support/prebuilt-images



   *on HS*

   .. code-block:: console

      $ cd <path to u-boot dir>

      R5
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" am65x_hs_evm_r5_defconfig O=<output directory>/r5
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" O=<output directory>/r5 BINMAN_INDIRS=<path to tisdk>/board-support/prebuilt-images


      A53
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am65x_hs_evm_a53_defconfig O=<output directory>/a53
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=<path to tisdk>/board-support/prebuilt-images/bl31.bin TEE=<path to tisdk>/board-support/prebuilt-images/bl32.bin O=<output directory>/a53 BINMAN_INDIRS=<path to tisdk>/board-support/prebuilt-images



.. ifconfig:: CONFIG_part_variant in ('AM64X')

   +----------------------------+---------------------------------+---------------------------------+
   |  Board                     |     SD / UART / OSPI Boot       |      eMMC Boot                  |
   +============================+=================================+=================================+
   |    AM64X EVM               | ``am64x_evm_r5_defconfig``      |  ``am64x_evm_r5_defconfig``     |
   |                            | ``am64x_evm_a53_defconfig``     |  ``am64x_evm_a53_defconfig``    |
   +----------------------------+---------------------------------+---------------------------------+
   |    AM64X SK                | ``am64x_evm_r5_defconfig``      |                                 |
   |                            | ``am64x_evm_a53_defconfig``     |                                 |
   +----------------------------+---------------------------------+---------------------------------+

   .. note::

      Where to get the sources: :ref:`Getting the U-Boot Source Code-label`

   .. code-block:: console

      $ export UBOOT_DIR=<path-to-ti-u-boot>
      $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
      $ export TFA_DIR=<path-to-arm-trusted-firmware>
      $ export OPTEE_DIR=<path-to-ti-optee-os>

   .. note::

      The instructions below assume all binaries are built manually. For instructions to build :file:`bl31.bin` go to: :ref:`foundational-components-optee`.
      For instructions to build :file:`tee-pager_v2.bin` (:file:`bl32.bin`) go to: :ref:`foundational-components-atf`. BINMAN_INDIRS can point to
      :file:`<path-to-tisdk>/board-support/prebuilt-images/am64xx-evm` to use the pre-built binaries that come in the pre-built SDK (:file:`bl31.bin` for BL31, :file:`bl32.bin` for TEE).

   .. code-block:: console

      $ cd $UBOOT_DIR

      R5
      To build tiboot3.bin. Saved in $UBOOT_DIR/out/r5.
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" am64x_evm_r5_defconfig O=$UBOOT_DIR/out/r5
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" O=$UBOOT_DIR/out/r5 BINMAN_INDIRS=$TI_LINUX_FW_DIR

      A53
      To build tispl.bin and u-boot.img. Saved in $UBOOT_DIR/out/a53.
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am64x_evm_a53_defconfig O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/bl32.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR

.. ifconfig:: CONFIG_part_variant in ('J721E')

   +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
   |  Board                     |            SD/eMMC Boot         |           UART Boot            |           OSPI Boot            |         Hyper Flash            |           USB DFU              |
   +============================+=================================+================================+================================+================================+================================+
   |    J721E EVM               | ``j721e_evm_r5_defconfig``      | ``j721e_evm_r5_defconfig``     | ``j721e_evm_r5_defconfig``     | ``j721e_evm_r5_defconfig``     | ``j721e_evm_r5_defconfig``     |
   |                            | ``j721e_evm_a72_defconfig``     | ``j721e_evm_a72_defconfig``    | ``j721e_evm_a72_defconfig``    | ``j721e_evm_a72_defconfig``    | ``j721e_evm_a72_defconfig``    |
   +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
   |    J721E SK                | ``j721e_evm_r5_defconfig``      | ``j721e_evm_r5_defconfig``     | ``j721e_evm_r5_defconfig``     |                                |                                |
   |                            | ``j721e_evm_a72_defconfig``     | ``j721e_evm_a72_defconfig``    | ``j721e_evm_a72_defconfig``    |                                |                                |
   +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J7200')

   +----------------------------+---------------------------------+--------------------------------+
   |  Board                     |            SD/eMMC Boot         |           UART Boot            |
   +============================+=================================+================================+
   |    J7200 EVM               |  ``j7200_evm_r5_defconfig``     | ``j7200_evm_r5_defconfig``     |
   |                            |  ``j7200_evm_a72_defconfig``    | ``j7200_evm_a72_defconfig``    |
   +----------------------------+---------------------------------+--------------------------------+


.. ifconfig:: CONFIG_part_variant in ('J721S2')

   +----------------------------+---------------------------------+---------------------------------+---------------------------------+---------------------------------+
   |  Board                     |            SD/eMMC Boot         |           UART Boot             |           OSPI Boot             |           USB DFU               |
   +============================+=================================+=================================+=================================+=================================+
   |    J721S2 EVM              | ``j721s2_evm_r5_defconfig``     | ``j721s2_evm_r5_defconfig``     | ``j721s2_evm_r5_defconfig``     | ``j721s2_evm_r5_defconfig``     |
   |                            | ``j721s2_evm_a72_defconfig``    | ``j721s2_evm_a72_defconfig``    | ``j721s2_evm_a72_defconfig``    | ``j721s2_evm_a72_defconfig``    |
   +----------------------------+---------------------------------+---------------------------------+---------------------------------+---------------------------------+
   |    AM68 HS-FS SK           | ``j721s2_evm_r5_defconfig``     | ``j721s2_evm_r5_defconfig``     | ``j721s2_evm_r5_defconfig``     |                                 |
   |                            | ``j721s2_evm_a72_defconfig``    | ``j721s2_evm_a72_defconfig``    | ``j721s2_evm_a72_defconfig``    |                                 |
   +----------------------------+---------------------------------+---------------------------------+---------------------------------+---------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   +----------------------------+----------------------------------+---------------------------------+---------------------------------+---------------------------------+
   |  Board                     |            SD/eMMC Boot          |           UART Boot             |           OSPI Boot             |           USB DFU               |
   +============================+==================================+=================================+=================================+=================================+
   |    J784S4 EVM              | ``j784s4_evm_r5_defconfig``      | ``j784s4_evm_r5_defconfig``     | ``j784s4_evm_r5_defconfig``     | ``j784s4_evm_r5_defconfig``     |
   |                            | ``j784s4_evm_a72_defconfig``     | ``j784s4_evm_a72_defconfig``    | ``j784s4_evm_a72_defconfig``    | ``j784s4_evm_a72_defconfig``    |
   +----------------------------+----------------------------------+---------------------------------+---------------------------------+---------------------------------+
   |    AM69 HS-FS SK           |  ``j784s4_evm_r5_defconfig``     | ``j784s4_evm_r5_defconfig``     | ``j784s4_evm_r5_defconfig``     |                                 |
   |                            |  ``j784s4_evm_a72_defconfig``    | ``j784s4_evm_a72_defconfig``    | ``j784s4_evm_a72_defconfig``    |                                 |
   +----------------------------+----------------------------------+---------------------------------+---------------------------------+---------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J742S2')

   +----------------------------+---------------------------------+---------------------------------+---------------------------------+---------------------------------+
   |  Board                     |            SD/eMMC Boot         |           UART Boot             |           OSPI Boot             |           USB DFU               |
   +============================+=================================+=================================+=================================+=================================+
   |    J742S2 EVM              | ``j742s2_evm_r5_defconfig``     | ``j742s2_evm_r5_defconfig``     | ``j742s2_evm_r5_defconfig``     | ``j742s2_evm_r5_defconfig``     |
   |                            | ``j742s2_evm_a72_defconfig``    | ``j742s2_evm_a72_defconfig``    | ``j742s2_evm_a72_defconfig``    | ``j742s2_evm_a72_defconfig``    |
   +----------------------------+---------------------------------+---------------------------------+---------------------------------+---------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J722S')

   +----------------------------+---------------------------------+--------------------------------+--------------------------------+------------------------------------------------------+-------------------------------------------------------+
   |  Board                     |            SD/eMMC Boot         |           UART Boot            |           OSPI Boot            |                     USB DFU                          |           USB MSC                                     |
   +============================+=================================+================================+================================+======================================================+=======================================================+
   |    J722S EVM               | ``j722s_evm_r5_defconfig``      | ``j722s_evm_r5_defconfig``     | ``j722s_evm_r5_defconfig``     | ``j722s_evm_r5_defconfig am62x_r5_usbdfu.config``    | ``j722s_evm_r5_defconfig am62x_r5_usbmsc.config``     |
   |                            | ``j722s_evm_a53_defconfig``     | ``j722s_evm_a53_defconfig``    | ``j722s_evm_a53_defconfig``    | ``j722s_evm_a53_defconfig``                          | ``j722s_evm_a53_defconfig``                           |
   +----------------------------+---------------------------------+--------------------------------+--------------------------------+------------------------------------------------------+-------------------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J721E','J7200','J721S2','J784S4','J742S2')

   .. code-block:: console

      $ cd <path to u-boot dir>
      $ PREBUILT_IMAGES=<path to tisdk>/board-support/prebuilt-images

      R5
      $ make ARCH=arm O=<output directory>/r5 <soc>_evm_r5_defconfig
      $ make ARCH=arm O=<output directory>/r5 CROSS_COMPILE="$CROSS_COMPILE_32" BINMAN_INDIRS=${PREBUILT_IMAGES}


      A72
      $ make ARCH=arm O=<output directory>/a72 <soc>_evm_a72_defconfig
      $ make ARCH=arm O=<output directory>/a72 CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=${PREBUILT_IMAGES}/bl31.bin TEE=${PREBUILT_IMAGES}/bl32.bin BINMAN_INDIRS=${PREBUILT_IMAGES}

.. ifconfig:: CONFIG_part_variant in ('J722S')

   .. code-block:: console

      $ cd <path to u-boot dir>
      $ PREBUILT_IMAGES=<path to tisdk>/board-support/prebuilt-images

      R5
      $ make ARCH=arm O=<output directory>/r5 j722s_evm_r5_defconfig

      To build with config fragments
      $ make ARCH=arm O=<output directory>/r5 j722s_evm_r5_defconfig am62x_r5_usbdfu.config
      $ make ARCH=arm O=<output directory>/r5 j722s_evm_r5_defconfig am62x_r5_usbmsc.config

      $ make ARCH=arm O=<output directory>/r5 CROSS_COMPILE="$CROSS_COMPILE_32" BINMAN_INDIRS=${PREBUILT_IMAGES}


      A53
      $ make ARCH=arm O=<output directory>/a53 j722s_evm_a53_defconfig
      $ make ARCH=arm O=<output directory>/a53 CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=${PREBUILT_IMAGES}/bl31.bin TEE=${PREBUILT_IMAGES}/bl32.bin BINMAN_INDIRS=${PREBUILT_IMAGES}


.. ifconfig:: CONFIG_part_variant in ('AM62X')

   +---------------+------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
   |  Board        |     SD / eMMC / UART / OSPI Boot   |                         USB DFU                          |                            USB MSC                       |
   +===============+====================================+==========================================================+==========================================================+
   |  AM62X SK     | ``am62x_evm_r5_defconfig``         | ``am62x_evm_r5_defconfig am62x_r5_usbdfu.config``        | ``am62x_evm_r5_defconfig am62x_r5_usbmsc.config``        |
   |               | ``am62x_evm_a53_defconfig``        | ``am62x_evm_a53_defconfig``                              | ``am62x_evm_a53_defconfig``                              |
   +---------------+------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
   |  AM62X LP SK  | ``am62x_lpsk_r5_defconfig``        | ``am62x_lpsk_r5_defconfig am62x_r5_usbdfu.config``       | ``am62x_lpsk_r5_defconfig am62x_r5_usbmsc.config``       |
   |               | ``am62x_lpsk_a53_defconfig``       | ``am62x_lpsk_a53_defconfig``                             | ``am62x_lpsk_a53_defconfig``                             |
   +---------------+------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
   |  AM62SIP SK   | ``am62xsip_evm_r5_defconfig``      | ``am62xsip_evm_r5_defconfig am62x_r5_usbdfu.config``     | ``am62xsip_evm_r5_defconfig am62x_r5_usbmsc.config``     |
   |               | ``am62xsip_evm_a53_defconfig``     | ``am62xsip_evm_a53_defconfig``                           | ``am62xsip_evm_a53_defconfig``                           |
   +---------------+------------------------------------+----------------------------------------------------------+----------------------------------------------------------+

   .. note::

      Where to get the sources: :ref:`Getting the U-Boot Source Code-label`

   .. code-block:: console

      $ export UBOOT_DIR=<path-to-ti-u-boot>
      $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
      $ export TFA_DIR=<path-to-arm-trusted-firmware>
      $ export OPTEE_DIR=<path-to-ti-optee-os>

   .. note::

      The instructions below assume all binaries are built manually. For instructions to build :file:`bl31.bin` go to: :ref:`foundational-components-optee`.
      For instructions to build :file:`tee-pager_v2.bin` (:file:`bl32.bin`) go to: :ref:`foundational-components-atf`. BINMAN_INDIRS can point to
      :file:`<path-to-tisdk>/board-support/prebuilt-images/am62xx-evm` to use the pre-built binaries that come in the pre-built SDK (:file:`bl31.bin` for BL31, :file:`bl32.bin` for TEE).

   .. code-block:: console

      $ cd $UBOOT_DIR

      R5
      To build tiboot3.bin. Saved in $UBOOT_DIR/out/r5.

      For AM62X
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" am62x_evm_r5_defconfig O=$UBOOT_DIR/out/r5
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" O=$UBOOT_DIR/out/r5 BINMAN_INDIRS=$TI_LINUX_FW_DIR

      For AM62X LP
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" am62x_lpsk_r5_defconfig O=$UBOOT_DIR/out/r5
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" O=$UBOOT_DIR/out/r5 BINMAN_INDIRS=$TI_LINUX_FW_DIR

      For AM62SIP
      NOTE: AM62SIP Uses config fragment model.
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" am62x_evm_r5_defconfig am62xsip_sk_r5.config O=$UBOOT_DIR/out/r5
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" O=$UBOOT_DIR/out/r5 BINMAN_INDIRS=$TI_LINUX_FW_DIR

      A53
      To build tispl.bin and u-boot.img. Saved in $UBOOT_DIR/out/a53. Requires bl31.bin, tee-pager_v2.bin

      For AM62X or AM62SIP
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am62x_evm_a53_defconfig O=$UBOOT_DIR/out/a53
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR

      For AM62X LP
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am62x_lpsk_a53_defconfig O=$UBOOT_DIR/out/a53
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR


.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   +-------------+----------------------------------+--------------------------------------------------------+--------------------------------------------------------+
   |  Board      |            SD Boot               |                       USB DFU                          |                       USB MSC                          |
   +=============+==================================+========================================================+========================================================+
   |  AM62AX SK  | ``am62ax_evm_r5_defconfig``      | ``am62ax_evm_r5_defconfig am62x_r5_usbdfu.config``     | ``am62ax_evm_r5_defconfig am62x_r5_usbmsc.config``     |
   |             | ``am62ax_evm_a53_defconfig``     | ``am62ax_evm_a53_defconfig``                           | ``am62ax_evm_a53_defconfig``                           |
   +-------------+----------------------------------+--------------------------------------------------------+--------------------------------------------------------+

   .. note::

      Where to get the sources: :ref:`Getting the U-Boot Source Code-label`

   .. code-block:: console

      $ export UBOOT_DIR=<path-to-ti-u-boot>
      $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
      $ export TFA_DIR=<path-to-arm-trusted-firmware>
      $ export OPTEE_DIR=<path-to-ti-optee-os>
      $ export TI_DM=<path-to-ti-linux-firmware>/ti-dm

   .. note::

      The instructions below assume all binaries are built manually. For instructions to build :file:`bl31.bin` go to: :ref:`foundational-components-optee`.
      For instructions to build :file:`tee-pager_v2.bin` (:file:`bl32.bin`) go to: :ref:`foundational-components-atf`. BINMAN_INDIRS can point to
      :file:`<path-to-tisdk>/board-support/prebuilt-images` to use the pre-built binaries that come in the pre-built SDK (:file:`bl31.bin` for BL31, :file:`bl32.bin` for TEE).

   .. code-block:: console

      $ cd $UBOOT_DIR

      R5
      To build tiboot3.bin. Saved in $UBOOT_DIR/out/r5.
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" am62ax_evm_r5_defconfig O=$UBOOT_DIR/out/r5
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" O=$UBOOT_DIR/out/r5 BINMAN_INDIRS=$TI_LINUX_FW_DIR

      A53
      To build tispl.bin and u-boot.img. Saved in $UBOOT_DIR/out/a53. Requires bl31.bin, tee-pager_v2.bin.
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am62ax_evm_a53_defconfig O=$UBOOT_DIR/out/a53
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR TI_DM=$TI_DM/am62axx/dm_edgeai_mcu1_0_release_strip.out

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   +-------------+----------------------------------+----------------------------------------------------------+--------------------------------------------------------+
   |  Board      |            SD Boot               |                       USB DFU                            |                        USB MSC                         |
   +=============+==================================+==========================================================+========================================================+
   |  AM62PX SK  | ``am62px_evm_r5_defconfig``      | ``am62px_evm_r5_defconfig am62x_r5_usbdfu.config``       | ``am62px_evm_r5_defconfig am62x_r5_usbmsc.config``     |
   |             | ``am62px_evm_a53_defconfig``     | ``am62px_evm_a53_defconfig``                             | ``am62px_evm_a53_defconfig``                           |
   +-------------+----------------------------------+----------------------------------------------------------+--------------------------------------------------------+

   .. note::

      Where to get the sources: :ref:`Getting the U-Boot Source Code-label`

   .. code-block:: console

      $ export UBOOT_DIR=<path-to-ti-u-boot>
      $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
      $ export TFA_DIR=<path-to-arm-trusted-firmware>
      $ export OPTEE_DIR=<path-to-ti-optee-os>

   .. note::

      The instructions below assume all binaries are built manually. For instructions to build :file:`bl31.bin` go to: :ref:`foundational-components-optee`.
      For instructions to build :file:`tee-pager_v2.bin` (:file:`bl32.bin`) go to: :ref:`foundational-components-atf`. BINMAN_INDIRS can point to
      :file:`<path-to-tisdk>/board-support/prebuilt-images` to use the pre-built binaries that come in the pre-built SDK (:file:`bl31.bin` for BL31, :file:`bl32.bin` for TEE).

   .. code-block:: console

      $ cd $UBOOT_DIR

      R5
      To build tiboot3.bin. Saved in $UBOOT_DIR/out/r5.
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" am62px_evm_r5_defconfig O=$UBOOT_DIR/out/r5
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" O=$UBOOT_DIR/out/r5 BINMAN_INDIRS=$TI_LINUX_FW_DIR

      A53
      To build tispl.bin and u-boot.img. Saved in $UBOOT_DIR/out/a53. Requires bl31.bin, tee-pager_v2.bin.
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am62px_evm_a53_defconfig O=$UBOOT_DIR/out/a53
      $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. csv-table::
      :header: "Board","SD / eMMC / UART / OSPI / USB DFU / USB MSC"

      "AM62LX EVM", ``am62lx_evm_defconfig``

   .. note::

      Where to get the sources: :ref:`Getting the U-Boot Source Code-label`

   .. code-block:: console

      $ export UBOOT_DIR=<path-to-ti-u-boot>
      $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
      $ export TFA_DIR=<path-to-arm-trusted-firmware>
      $ export OPTEE_DIR=<path-to-ti-optee-os>

   .. note::

      The instructions below assume all binaries are built manually.
      For instructions to build :file:`bl1.bin` or :file:`bl31.bin` go
      to: :ref:`foundational-components-atf`.

      **BINMAN_INDIRS** can point to
      :file:`<path-to-tisdk>/board-support/prebuilt-images` to use
      the pre-built binaries that come in the pre-built SDK.

   .. code-block:: console

      $ cd $UBOOT_DIR
      $ make CROSS_COMPILE="$CROSS_COMPILE_64" am62lx_evm_defconfig
      $ make CROSS_COMPILE="$CROSS_COMPILE_64" \
         BL1=$TFA_DIR/build/k3/am62l/release/bl1.bin \
         BL31=$TFA_DIR/build/k3/am62l/release/bl31.bin \
         BINMAN_INDIRS=$TI_LINUX_FW_DIR \
         TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin

.. ifconfig:: CONFIG_part_variant not in ('AM64X', 'AM62X', 'AM62AX', 'AM62LX')

   .. note::

      BINMAN_INDIRS is used to fetch the DM binary from :file:`board-support/prebuilt-images/ti-dm/` and SYSFW binaries from :file:`board-support/prebuilt-images/ti-sysfw/`. If not using the SDK, BINMAN_INDIRS can point to either ti-linux-firmware or any folder where DM is located in :file:`<path to folder>/ti-dm/` and SYSFW binaries are present in :file:`<path to folder>/ti-sysfw/`. Please make sure to use the absolute path.

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'AM62X', 'AM62AX')

   .. note::

      BINMAN_INDIRS is used to fetch the DM binary from :file:`<path to ti-linux-firmware>/ti-dm/` and SYSFW binaries from :file:`<path to ti-linux-firmware>/ti-sysfw/`. If using the SDK, BINMAN_INDIRS can point to :file:`<path to SDK>/board-support/prebuilt-images`. Else any folder where DM is located in :file:`<path to folder>/ti-dm/` and SYSFW binaries are present in :file:`<path to folder>/ti-sysfw/` can be used. Please make sure to use the absolute path.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. note::

      BINMAN_INDIRS is used to fetch the TIFS binaries from
      :file:`<path to ti-linux-firmware>/ti-sysfw/`. If using the SDK,
      BINMAN_INDIRS can point to
      :file:`<path to SDK>/board-support/prebuilt-images`. Else any
      folder where SYSFW binaries are present in
      :file:`<path to folder>/ti-sysfw/` can be used. Please make sure
      to use the absolute path.

.. ifconfig:: CONFIG_part_variant in ('J721E', 'J7200', 'AM62X', 'AM62AX', 'AM62PX', 'J721S2', 'J784S4','J742S2', 'J722S')

   .. note::

      It is also possible to pick up a custom DM binary by adding TI_DM argument pointing to the file. If not provided, it defaults to picking up the DM binary from BINMAN_INDIRS. This is only applicable to devices that utilize split firmware.
