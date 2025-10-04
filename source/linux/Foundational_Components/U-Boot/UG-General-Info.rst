General Information
-------------------

.. ifconfig:: CONFIG_part_family not in ('General_family', 'AM335X_family', 'AM437X_family')

   .. rubric:: Install host dependencies

   To install host dependencies for building TI U-boot source (standalone)
   on Ubuntu 22.04+, run the following command in the terminal prompt:

   .. code-block:: console

      sudo apt install git xz-utils build-essential autoconf flex bison libssl-dev bc libncurses-dev \
      python3 python3-setuptools python3-dev python3-yaml python3-jsonschema python3-pyelftools \
      swig yamllint libgnutls28-dev

.. note::

   The recommended host machine for building U-Boot is Ubuntu 22.04.
   Users of Ubuntu 18.04 might need to install Python 3.7 or later. If using the default Python 3.6
   that is in Ubuntu 18.04, users might need to install these additional dependencies:

   .. code-block:: console

      pip install dataclasses pyelftools jsonschema yamllint importlib-resources

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   Getting the BL-1 Source Code
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   AM62L devices use TF-A BL-1 boot loader to configure LPDDR4 to
   enable secondary program loader.
   The easiest way to get access to the BL-1 source code is by
   downloading and installing the Processor SDK Linux. Once installed,
   the BL-1 source code is in the SDK at the path ``<path to tisdk>/board-support``.
   For your convenience the sources also includes the BL-1's
   git repository including commit history.

   Alternatively, BL-1 sources can directly be fetched from GIThub. The GIT
   repo URL, branch and commit id can be found at :ref:`release-specific-build-information`.
   section of the release notes.

   .. _Build-BL1-label:

   Build BL-1
   ^^^^^^^^^^
   .. note::
    The following commands needs to run from the root of the
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

.. _Getting the U-Boot Source Code-label:

Getting the U-Boot Source Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The easiest way to get access to the U-boot source code is by
downloading and installing the Processor SDK Linux. Once installed,
the U-Boot source code is in the SDK at the path ``<path to tisdk>/board-support``.
For your convenience the sources also includes the U-Boot's
git repository including commit history.

Alternatively, U-Boot sources can directly be fetched from Git.
The Git repo URL, branch and commit id can be found in the :ref:`u-boot-release-notes` :ref:`release-specific-build-information`
section of the release notes.


.. _Build-U-Boot-label:

Build U-Boot
^^^^^^^^^^^^
.. note::
    The following commands are intended to be run from the root of the
    U-Boot tree unless otherwise specified. The root of the U-Boot tree is
    the top-level directory and can be identified by looking for the
    "MAINTAINERS" file.

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family', 'AM57X_family')

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

        export PATH=$HOME/<TOOLCHAIN_PATH>/bin:$PATH

    .. rubric:: Cleaning the Sources

    If you did not use a separate object directory:

    .. code-block:: console

        $ make CROSS_COMPILE=arm-none-linux-gnueabihf- distclean

    If you used 'O=am335x\_evm' as your object directory:

    .. code-block:: console

        $ rm -rf ./am335x_evm

    .. rubric:: Compiling MLO and u-boot

    Building of both u-boot and SPL is done at the same time. You must
    however first configure the build for the board you are working with.
    Use the following table to determine what defconfig to use to configure
    with:

    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | Board                      | SD Boot                     | eMMC Boot                | NAND Boot                                  | UART Boot                | Ethernet Boot            | USB Ethernet Boot        | USB Host Boot                           | SPI Boot                                 |
    +============================+=============================+==========================+============================================+==========================+==========================+==========================+=========================================+==========================================+
    | AM335x GP EVM              | am335x\_evm\_defconfig      |                          | am335x\_evm\_defconfig                     | am335x\_evm\_defconfig   | am335x\_evm\_defconfig   | am335x\_evm\_defconfig   |                                         |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | AM335x EVM-SK              | am335x\_evm\_defconfig      |                          |                                            | am335x\_evm\_defconfig   |                          | am335x\_evm\_defconfig   |                                         |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | AM335x ICE                 | am335x\_evm\_defconfig      |                          |                                            | am335x\_evm\_defconfig   |                          |                          |                                         |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | BeagleBone Black           | am335x\_evm\_defconfig      | am335x\_evm\_defconfig   |                                            | am335x\_evm\_defconfig   |                          |                          |                                         |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | BeagleBone White           | am335x\_evm\_defconfig      |                          |                                            | am335x\_evm\_defconfig   |                          |                          |                                         |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | AM437x GP EVM              | am43xx\_evm\_defconfig      |                          | am43xx\_evm\_defconfig                     | am43xx\_evm\_defconfig   | am43xx\_evm\_defconfig   | am43xx\_evm\_defconfig   | am43xx\_evm\_usbhost\_boot\_defconfig   |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | AM437x EVM-Sk              | am43xx\_evm\_defconfig      |                          |                                            |                          |                          |                          | am43xx\_evm\_usbhost\_boot\_defconfig   |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | AM437x IDK                 | am43xx\_evm\_defconfig      |                          |                                            |                          |                          |                          |                                         | am43xx\_evm\_qspiboot\_defconfig (XIP)   |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | AM437x ePOS EVM            | am43xx\_evm\_defconfig      |                          | am43xx\_evm\_defconfig                     |                          |                          |                          | am43xx\_evm\_usbhost\_boot\_defconfig   |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | AM572x GP EVM              | am57xx\_evm\_defconfig      |                          |                                            | am57xx\_evm\_defconfig   |                          |                          |                                         |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | AM572x IDK                 | am57xx\_evm\_defconfig      |                          |                                            |                          |                          |                          |                                         |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | AM571x IDK                 | am57xx\_evm\_defconfig      |                          |                                            |                          |                          |                          |                                         |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | DRA74x/DRA72x/DRA71x EVM   | dra7xx\_evm\_defconfig      | dra7xx\_evm\_defconfig   | dra7xx\_evm\_defconfig (DRA71x EVM only)   |                          |                          |                          |                                         | dra7xx\_evm\_defconfig(QSPI)             |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | K2HK EVM                   |                             |                          | k2hk\_evm\_defconfig                       | k2hk\_evm\_defconfig     | k2hk\_evm\_defconfig     |                          |                                         | k2hk\_evm\_defconfig                     |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | K2L EVM                    |                             |                          | k2l\_evm\_defconfig                        | k2l\_evm\_defconfig      |                          |                          |                                         | k2l\_evm\_defconfig                      |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | K2E EVM                    |                             |                          | k2e\_evm\_defconfig                        | k2e\_evm\_defconfig      |                          |                          |                                         | k2e\_evm\_defconfig                      |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | K2G GP EVM                 | k2g\_evm\_defconfig         |                          |                                            | k2g\_evm\_defconfig      | k2g\_evm\_defconfig      |                          |                                         | k2g\_evm\_defconfig                      |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | K2G ICE                    | k2g\_evm\_defconfig         |                          |                                            |                          |                          |                          |                                         |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+
    | OMAP-L138 LCDK             | omapl138\_lcdk\_defconfig   |                          | omapl138\_lcdk\_defconfig                  |                          |                          |                          |                                         |                                          |
    +----------------------------+-----------------------------+--------------------------+--------------------------------------------+--------------------------+--------------------------+--------------------------+-----------------------------------------+------------------------------------------+

    Then (Use 'am335x_evm' and 'AM335x GP EVM' in this example):

    .. code-block:: console

        $ make CROSS_COMPILE=arm-none-linux-gnueabihf- O=am335x_evm am335x_evm_defconfig
        $ make CROSS_COMPILE=arm-none-linux-gnueabihf- O=am335x_evm

    .. note::
        Not all possible build targets for a given platform are listed
        here as the community has additional build targets that are not
        supported by TI. To find these read the 'boards.cfg' file and look for
        the build target listed above. And please note that the main config file
        will leverage other files under include/configs, as seen by #include
        statements.


.. ifconfig:: CONFIG_part_family not in ('General_family', 'AM335X_family', 'AM437X_family', 'AM57X_family')

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

   All of these are available in the SDK at ``<path to tisdk>/board-support/prebuilt-images>``

   Go :ref:`here <download-and-install-sdk>` to download and install the SDK.

   .. rubric:: Setting up the toolchain paths

   .. include:: ../../Overview/GCC_ToolChain.rst
      :start-after: .. start_include_yocto_toolchain_host_setup
      :end-before: .. end_include_yocto_toolchain_host_setup

   .. ifconfig:: CONFIG_part_variant not in ('AM62LX')

      .. rubric:: Compiling R5 and ARM64 images

      Use the following table to determine what defconfig to use to configure with:

   .. ifconfig:: CONFIG_part_variant in ('AM65X')

      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
      |  Board                     |            SD/eMMC Boot         |           UART boot            |           OSPI boot            |         Hyper Flash            |           USB DFU              |
      +============================+=================================+================================+================================+================================+================================+
      |    AM65x EVM/IDK           |    am65x\_evm\_r5\_defconfig    |   am65x\_evm\_r5\_defconfig    |   am65x\_evm\_r5_defconfig     |                                |                                |
      |                            |    am65x\_evm\_a53\_defconfig   |   am65x\_evm\_a53\_defconfig   |   am65x\_evm\_a53\_defconfig   |                                |                                |
      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
      |    AM65x HS EVM/IDK        | am65x\_hs\_evm\_r5\_defconfig   | am65x\_hs\_evm\_r5\_defconfig  | am65x\_hs\_evm\_r5_defconfig   |                                |                                |
      |                            | am65x\_hs\_evm\_a53\_defconfig  | am65x\_hs\_evm\_a53\_defconfig | am65x\_hs\_evm\_a53\_defconfig |                                |                                |
      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+

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

      +----------------------------+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
      |  Board                     |            SD Boot              |            eMMC Boot            |           UART boot            |           OSPI boot            |
      +============================+=================================+=================================+================================+================================+
      |    AM64X EVM               |    am64x\_evm\_r5\_defconfig    |    am64x\_evm\_r5\_defconfig    |   am64x\_evm\_r5\_defconfig    |   am64x\_evm\_r5\_defconfig    |
      |                            |    am64x\_evm\_a53\_defconfig   |    am64x\_evm\_a53\_defconfig   |   am64x\_evm\_a53\_defconfig   |   am64x\_evm\_a53\_defconfig   |
      +----------------------------+---------------------------------+---------------------------------+--------------------------------+--------------------------------+
      |    AM64X SK                |    am64x\_evm\_r5\_defconfig    |                                 |   am64x\_evm\_r5\_defconfig    |   am64x\_evm\_r5\_defconfig    |
      |                            |    am64x\_evm\_a53\_defconfig   |                                 |   am64x\_evm\_a53\_defconfig   |   am64x\_evm\_a53\_defconfig   |
      +----------------------------+---------------------------------+---------------------------------+--------------------------------+--------------------------------+

      .. note::

         Where to get the sources:

         - ti-u-boot version: :ref:`u-boot-release-notes`
         - ti-linux-firmware version: :ref:`ti-linux-fw-release-notes`
         - TF-A version: :ref:`tf-a-release-notes`
         - OP-TEE version: :ref:`optee-release-notes`

      .. code-block:: console

         $ export UBOOT_DIR=<path-to-ti-u-boot>
         $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
         $ export TFA_DIR=<path-to-arm-trusted-firmware>
         $ export OPTEE_DIR=<path-to-ti-optee-os>

      .. note::

         The instructions below assume all binaries are built manually. For instructions to build bl31.bin go to: :ref:`foundational-components-optee`.
         For instructions to build tee-pager_v2.bin (bl32.bin) go to: :ref:`foundational-components-atf`. BINMAN_INDIRS can point to
         <path-to-tisdk>/board-support/prebuilt-images/am64xx-evm to use the pre-built binaries that come in the pre-built SDK (bl31.bin for BL31, bl32.bin for TEE).

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
      |  Board                     |            SD/eMMC Boot         |           UART boot            |           OSPI boot            |         Hyper Flash            |           USB DFU              |
      +============================+=================================+================================+================================+================================+================================+
      |    J721E EVM               |    j721e\_evm\_r5\_defconfig    |   j721e\_evm\_r5\_defconfig    |   j721e\_evm\_r5\_defconfig    |   j721e\_evm\_r5\_defconfig    |   j721e\_evm\_r5\_defconfig    |
      |                            |    j721e\_evm\_a72\_defconfig   |   j721e\_evm\_a72\_defconfig   |   j721e\_evm\_a72\_defconfig   |   j721e\_evm\_a72\_defconfig   |   j721e\_evm\_a72\_defconfig   |
      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+
      |    J721E SK                |    j721e\_evm\_r5\_defconfig    |   j721e\_evm\_r5\_defconfig    |   j721e\_evm\_r5\_defconfig    |                                |                                |
      |                            |    j721e\_evm\_a72\_defconfig   |   j721e\_evm\_a72\_defconfig   |   j721e\_evm\_a72\_defconfig   |                                |                                |
      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('J7200')

      +----------------------------+---------------------------------+--------------------------------+
      |  Board                     |            SD/eMMC Boot         |           UART boot            |
      +============================+=================================+================================+
      |    J7200 EVM               |    j7200\_evm\_r5\_defconfig    |   j7200\_evm\_r5\_defconfig    |
      |                            |    j7200\_evm\_a72\_defconfig   |   j7200\_evm\_a72\_defconfig   |
      +----------------------------+---------------------------------+--------------------------------+


   .. ifconfig:: CONFIG_part_variant in ('J721S2')

      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------------+
      |  Board                     |            SD/eMMC Boot         |           UART boot            |           OSPI boot            |           USB DFU              |           Ethernet Boot              |
      +============================+=================================+================================+================================+================================+======================================+
      |    J721S2 EVM              |    j721s2\_evm\_r5\_defconfig   |   j721s2\_evm\_r5\_defconfig   |   j721s2\_evm\_r5\_defconfig   |   j721s2\_evm\_r5\_defconfig   |                                      |
      |                            |    j721s2\_evm\_a72\_defconfig  |   j721s2\_evm\_a72\_defconfig  |   j721s2\_evm\_a72\_defconfig  |   j721s2\_evm\_a72\_defconfig  |                                      |
      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------------+
      |    AM68 HS-FS SK           |    j721s2\_evm\_r5\_defconfig   |   j721s2\_evm\_r5\_defconfig   |   j721s2\_evm\_r5\_defconfig   |                                |   am68\_sk\_r5\_ethboot\_defconfig   |
      |                            |    j721s2\_evm\_a72\_defconfig  |   j721s2\_evm\_a72\_defconfig  |   j721s2\_evm\_a72\_defconfig  |                                |   am68\_sk\_a72\_ethboot\_defconfig  |
      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('J784S4')

      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------------+
      |  Board                     |            SD/eMMC Boot         |           UART boot            |           OSPI boot            |           USB DFU              |           Ethernet boot              |
      +============================+=================================+================================+================================+================================+======================================+
      |    J784S4 EVM              |    j784s4\_evm\_r5\_defconfig   |   j784s4\_evm\_r5\_defconfig   |   j784s4\_evm\_r5\_defconfig   |   j784s4\_evm\_r5\_defconfig   |                                      |
      |                            |    j784s4\_evm\_a72\_defconfig  |   j784s4\_evm\_a72\_defconfig  |   j784s4\_evm\_a72\_defconfig  |   j784s4\_evm\_a72\_defconfig  |                                      |
      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------------+
      |    AM69 HS-FS SK           |    j784s4\_evm\_r5\_defconfig   |   j784s4\_evm\_r5\_defconfig   |   j784s4\_evm\_r5\_defconfig   |                                |   am69\_sk\_r5\_ethboot\_defconfig   |
      |                            |    j784s4\_evm\_a72\_defconfig  |   j784s4\_evm\_a72\_defconfig  |   j784s4\_evm\_a72\_defconfig  |                                |   am69\_sk\_a72\_ethboot\_defconfig  |
      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('J742S2')

      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+
      |  Board                     |            SD/eMMC Boot         |           UART boot            |           OSPI boot            |           USB DFU              |
      +============================+=================================+================================+================================+================================+
      |    J742S2 EVM              |    j742s2\_evm\_r5\_defconfig   |   j742s2\_evm\_r5\_defconfig   |   j742s2\_evm\_r5\_defconfig   |   j742s2\_evm\_r5\_defconfig   |
      |                            |    j742s2\_evm\_a72\_defconfig  |   j742s2\_evm\_a72\_defconfig  |   j742s2\_evm\_a72\_defconfig  |   j742s2\_evm\_a72\_defconfig  |
      +----------------------------+---------------------------------+--------------------------------+--------------------------------+--------------------------------+

   .. ifconfig:: CONFIG_part_variant in ('J722S')

      +----------------------------+---------------------------------+--------------------------------+--------------------------------+------------------------------------------------------+-------------------------------------------------------+------------------------------------------+
      |  Board                     |            SD/eMMC Boot         |           UART boot            |           OSPI boot            |                     USB DFU                          |           USB MSC                                     |            Ethernet boot                 |
      +============================+=================================+================================+================================+======================================================+=======================================================+==========================================+
      |    J722S EVM               |  | ``j722s_evm_r5_defconfig``   |  | ``j722s_evm_r5_defconfig``  |  | ``j722s_evm_r5_defconfig``  |  | ``j722s_evm_r5_defconfig am62x_r5_usbdfu.config`` |  | ``j722s_evm_r5_defconfig am62x_r5_usbmsc.config``  |   j722s\_evm\_r5\_ethboot\_defconfig     |
      |                            |  | ``j722s_evm_a53_defconfig``  |  | ``j722s_evm_a53_defconfig`` |  | ``j722s_evm_a53_defconfig`` |  | ``j722s_evm_a53_defconfig``                       |  | ``j722s_evm_a53_defconfig``                        |   j722s\_evm\_a53\_ethboot\_defconfig    |
      +----------------------------+---------------------------------+--------------------------------+--------------------------------+------------------------------------------------------+-------------------------------------------------------+------------------------------------------+

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
      |  AM62X SK     |  | ``am62x_evm_r5_defconfig``      |  | ``am62x_evm_r5_defconfig am62x_r5_usbdfu.config``     |  | ``am62x_evm_r5_defconfig am62x_r5_usbmsc.config``     |
      |               |  | ``am62x_evm_a53_defconfig``     |  | ``am62x_evm_a53_defconfig``                           |  | ``am62x_evm_a53_defconfig``                           |
      +---------------+------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
      |  AM62X LP SK  |  | ``am62x_lpsk_r5_defconfig``     |  | ``am62x_lpsk_r5_defconfig am62x_r5_usbdfu.config``    |  | ``am62x_lpsk_r5_defconfig am62x_r5_usbmsc.config``    |
      |               |  | ``am62x_lpsk_a53_defconfig``    |  | ``am62x_lpsk_a53_defconfig``                          |  | ``am62x_lpsk_a53_defconfig``                          |
      +---------------+------------------------------------+----------------------------------------------------------+----------------------------------------------------------+
      |  AM62SIP SK   |  | ``am62xsip_evm_r5_defconfig``   |  | ``am62xsip_evm_r5_defconfig am62x_r5_usbdfu.config``  |  | ``am62xsip_evm_r5_defconfig am62x_r5_usbmsc.config``  |
      |               |  | ``am62xsip_evm_a53_defconfig``  |  | ``am62xsip_evm_a53_defconfig``                        |  | ``am62xsip_evm_a53_defconfig``                        |
      +---------------+------------------------------------+----------------------------------------------------------+----------------------------------------------------------+

      .. note::

         Where to get the sources:

         - ti-u-boot version: :ref:`u-boot-release-notes`
         - ti-linux-firmware version: :ref:`ti-linux-fw-release-notes`
         - TF-A version: :ref:`tf-a-release-notes`
         - OP-TEE version: :ref:`optee-release-notes`

      .. code-block:: console

         $ export UBOOT_DIR=<path-to-ti-u-boot>
         $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
         $ export TFA_DIR=<path-to-arm-trusted-firmware>
         $ export OPTEE_DIR=<path-to-ti-optee-os>

      .. note::

         The instructions below assume all binaries are built manually. For instructions to build bl31.bin go to: :ref:`foundational-components-optee`.
         For instructions to build tee-pager_v2.bin (bl32.bin) go to: :ref:`foundational-components-atf`. BINMAN_INDIRS can point to
         <path-to-tisdk>/board-support/prebuilt-images/am62xx-evm to use the pre-built binaries that come in the pre-built SDK (bl31.bin for BL31, bl32.bin for TEE).

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
      |  AM62AX SK  |  | ``am62ax_evm_r5_defconfig``   |  | ``am62ax_evm_r5_defconfig am62x_r5_usbdfu.config``  |  | ``am62ax_evm_r5_defconfig am62x_r5_usbmsc.config``  |
      |             |  | ``am62ax_evm_a53_defconfig``  |  | ``am62ax_evm_a53_defconfig``                        |  | ``am62ax_evm_a53_defconfig``                        |
      +-------------+----------------------------------+--------------------------------------------------------+--------------------------------------------------------+

      .. note::

         Where to get the sources:

         - ti-u-boot version: :ref:`u-boot-release-notes`
         - ti-linux-firmware version: :ref:`ti-linux-fw-release-notes`
         - TF-A version: :ref:`tf-a-release-notes`
         - OP-TEE version: :ref:`optee-release-notes`

      .. code-block:: console

         $ export UBOOT_DIR=<path-to-ti-u-boot>
         $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
         $ export TFA_DIR=<path-to-arm-trusted-firmware>
         $ export OPTEE_DIR=<path-to-ti-optee-os>

      .. note::

         The instructions below assume all binaries are built manually. For instructions to build bl31.bin go to: :ref:`foundational-components-optee`.
         For instructions to build tee-pager_v2.bin (bl32.bin) go to: :ref:`foundational-components-atf`. BINMAN_INDIRS can point to
         <path-to-tisdk>/board-support/prebuilt-images to use the pre-built binaries that come in the pre-built SDK (bl31.bin for BL31, bl32.bin for TEE).

      .. code-block:: console

         $ cd $UBOOT_DIR

         R5
         To build tiboot3.bin. Saved in $UBOOT_DIR/out/r5.
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" am62ax_evm_r5_defconfig O=$UBOOT_DIR/out/r5
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" O=$UBOOT_DIR/out/r5 BINMAN_INDIRS=$TI_LINUX_FW_DIR

         A53
         To build tispl.bin and u-boot.img. Saved in $UBOOT_DIR/out/a53. Requires bl31.bin, tee-pager_v2.bin.
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am62ax_evm_a53_defconfig O=$UBOOT_DIR/out/a53
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR

   .. ifconfig:: CONFIG_part_variant in ('AM62DX')

      +-------------+----------------------------------+--------------------------------------------------------+--------------------------------------------------------+
      |  Board      |            SD Boot               |                       USB DFU                          |                       USB MSC                          |
      +=============+==================================+========================================================+========================================================+
      |  AM62DX EVM |  | ``am62dx_evm_r5_defconfig``   |  | ``am62dx_evm_r5_defconfig am62x_r5_usbdfu.config``  |  | ``am62dx_evm_r5_defconfig am62x_r5_usbmsc.config``  |
      |             |  | ``am62dx_evm_a53_defconfig``  |  | ``am62dx_evm_a53_defconfig``                        |  | ``am62dx_evm_a53_defconfig``                        |
      +-------------+----------------------------------+--------------------------------------------------------+--------------------------------------------------------+

      .. note::

         Where to get the sources:

         - ti-u-boot version: :ref:`u-boot-release-notes`
         - ti-linux-firmware version: :ref:`ti-linux-fw-release-notes`
         - TF-A version: :ref:`tf-a-release-notes`
         - OP-TEE version: :ref:`optee-release-notes`

      .. code-block:: console

         $ export UBOOT_DIR=<path-to-ti-u-boot>
         $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
         $ export TFA_DIR=<path-to-arm-trusted-firmware>
         $ export OPTEE_DIR=<path-to-ti-optee-os>

      .. note::

         The instructions below assume all binaries are built manually. For instructions to build bl31.bin go to: :ref:`foundational-components-optee`.
         For instructions to build tee-pager_v2.bin (bl32.bin) go to: :ref:`foundational-components-atf`. BINMAN_INDIRS can point to
         :file:`<path-to-tisdk>/board-support/prebuilt-images` to use the pre-built binaries that come in the pre-built SDK (bl31.bin for BL31, bl32.bin for TEE).

      .. code-block:: console

         $ cd $UBOOT_DIR

         R5
         To build tiboot3.bin. Saved in $UBOOT_DIR/out/r5.
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" am62dx_evm_r5_defconfig O=$UBOOT_DIR/out/r5
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" O=$UBOOT_DIR/out/r5 BINMAN_INDIRS=$TI_LINUX_FW_DIR

         A53
         To build tispl.bin and u-boot.img. Saved in $UBOOT_DIR/out/a53. Requires bl31.bin, tee-pager_v2.bin.
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am62dx_evm_a53_defconfig O=$UBOOT_DIR/out/a53
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR



   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      +-------------+----------------------------------+----------------------------------------------------------+--------------------------------------------------------+-----------------------------------------+
      |  Board      |            SD Boot               |                       USB DFU                            |                        USB MSC                         |                 Ethernet Boot           |
      +=============+==================================+==========================================================+========================================================+=========================================+
      |  AM62PX SK  |  | ``am62px_evm_r5_defconfig``   |  | ``am62px_evm_r5_defconfig am62x_r5_usbdfu.config``    |  | ``am62px_evm_r5_defconfig am62x_r5_usbmsc.config``  |  | ``am62px_evm_r5_ethboot_defconfig``  |
      |             |  | ``am62px_evm_a53_defconfig``  |  | ``am62px_evm_a53_defconfig``                          |  | ``am62px_evm_a53_defconfig``                        |  | ``am62px_evm_a53_ethboot_defconfig`` |
      +-------------+----------------------------------+----------------------------------------------------------+--------------------------------------------------------+-----------------------------------------+

      .. note::

         Where to get the sources: :ref:`release-specific-build-information`.

      .. code-block:: console

         $ export UBOOT_DIR=<path-to-ti-u-boot>
         $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
         $ export TFA_DIR=<path-to-arm-trusted-firmware>
         $ export OPTEE_DIR=<path-to-ti-optee-os>

      .. note::

         The instructions below assume all binaries are built manually. For instructions to build bl31.bin go to: :ref:`foundational-components-optee`.
         For instructions to build tee-pager_v2.bin (bl32.bin) go to: :ref:`foundational-components-atf`. BINMAN_INDIRS can point to
         <path-to-tisdk>/board-support/prebuilt-images to use the pre-built binaries that come in the pre-built SDK (bl31.bin for BL31, bl32.bin for TEE).

      .. code-block:: console

         R5
         To build tiboot3.bin. Saved in $UBOOT_DIR/out/r5.
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" am62px_evm_r5_defconfig O=$UBOOT_DIR/out/r5
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_32" O=$UBOOT_DIR/out/r5 BINMAN_INDIRS=$TI_LINUX_FW_DIR

         A53
         To build tispl.bin and u-boot.img. Saved in $UBOOT_DIR/out/a53. Requires bl31.bin, tee-pager_v2.bin.
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" am62px_evm_a53_defconfig O=$UBOOT_DIR/out/a53
         $ make ARCH=arm CROSS_COMPILE="$CROSS_COMPILE_64" CC="$CC_64" BL31=$TFA_DIR/build/k3/lite/release/bl31.bin TEE=$OPTEE_DIR/out/arm-plat-k3/core/tee-pager_v2.bin O=$UBOOT_DIR/out/a53 BINMAN_INDIRS=$TI_LINUX_FW_DIR

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      .. csv-table::
         :header: "Board","SD/eMMC UART OSPI USB-DFU USB-MSC"

         "AM62LX EVM", "am62lx_evm_defconfig"

      .. note::

         Where to get the sources: :ref:`release-specific-build-information`.

      .. code-block:: console

         $ export UBOOT_DIR=<path-to-ti-u-boot>
         $ export TI_LINUX_FW_DIR=<path-to-ti-linux-firmware>
         $ export TFA_DIR=<path-to-arm-trusted-firmware>

      .. note::

         The instructions below assume all binaries are built manually.
         For instructions to build :file:bl1.bin or :file:bl31.bin go
         to: :ref:`foundational-components-atf`.

         **BINMAN_INDIRS** can point to
         :file:`<path-to-tisdk>/board-support/prebuilt-images` to use
         the pre-built binaries that come in the pre-built SDK.

      .. code-block:: console

         $ make CROSS_COMPILE="$CROSS_COMPILE_64" am62lx_evm_defconfig O=$UBOOT_DIR/out
         $ make CROSS_COMPILE="$CROSS_COMPILE_64" O=$UBOOT_DIR/out \
            BL1=$TFA_DIR/build/k3/am62l/release/bl1.bin \
            BL31=$TFA_DIR/build/k3/am62l/release/bl31.bin \
            BINMAN_INDIRS=$TI_LINUX_FW_DIR

.. ifconfig:: CONFIG_part_variant not in ('AM64X', 'AM62X', 'AM62AX', 'AM62LX')

     .. note::

       BINMAN_INDIRS is used to fetch the DM binary from board-support/prebuilt-images/ti-dm/ and SYSFW binaries from board-support/prebuilt-images/ti-sysfw/. If not using the SDK, BINMAN_INDIRS can point to either ti-linux-firmware or any folder where DM is located in <path to folder>/ti-dm/ and SYSFW binaries are present in <path to folder>/ti-sysfw/. Please make sure to use the absolute path.

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'AM62X', 'AM62AX')

     .. note::

      BINMAN_INDIRS is used to fetch the DM binary from <path to ti-linux-firmware>/ti-dm/ and SYSFW binaries from <path to ti-linux-firmware>/ti-sysfw/. If using the SDK, BINMAN_INDIRS can point to <path to SDK>/board-support/prebuilt-images. Else any folder where DM is located in <path to folder>/ti-dm/ and SYSFW binaries are present in <path to folder>/ti-sysfw/ can be used. Please make sure to use the absolute path.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

     .. note::

      BINMAN_INDIRS is used to fetch the TIFS binaries from
      :file:`<path to ti-linux-firmware>/ti-sysfw/`. If using the SDK,
      BINMAN_INDIRS can point to
      :file:`<path to SDK>/board-support/prebuilt-images`. Else any
      folder where SYSFW binaries are present in
      :file:`<path to folder>/ti-sysfw/` can be used. Please make sure
      to use the absolute path.

.. ifconfig:: CONFIG_part_variant in ('J721E', 'J7200', 'AM62X', 'AM62AX', 'AM62DX', 'AM62PX', 'J721S2', 'J784S4','J742S2', 'J722S')

   .. note::

      It is also possible to pick up a custom DM binary by adding TI_DM argument pointing to the file. If not provided, it defaults to picking up the DM binary from BINMAN_INDIRS. This is only applicable to devices that use split firmware.

.. ifconfig:: CONFIG_part_variant in ('AM65X', 'J721E', 'J7200', 'AM64X', 'AM62X', 'AM62AX', 'AM62DX', 'AM62LX', 'AM62PX', 'J721S2', 'J784S4','J742S2', 'J722S')

   .. rubric:: Target Images
      :name: target-images

   Copy the below images to the boot partition of an SD card and boot.
   Instructions to format the SD card can be found :ref:`here <processor-sdk-linux-create-sd-card>`.

.. ifconfig:: CONFIG_part_variant in ('AM65X')

       * GP

         * tiboot3-am65x_sr2-gp-evm.bin, sysfw-am65x_sr2-gp-evm.itb from <output directory>/r5
         * tispl.bin_unsigned, u-boot.img_unsigned from <output directory>/a53

       * HS

         * tiboot3-am65x_sr2-hs-evm.bin, sysfw-am65x_sr2-hs-evm.itb from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a53

.. ifconfig:: CONFIG_part_variant in ('J721E')

       * GP

         * tiboot3-j721e-gp-evm.bin, sysfw-j721e-gp-evm.itb from <output directory>/r5
         * tispl.bin_unsigned, u-boot.img_unsigned from <output directory>/a72

       * HS-FS

         * tiboot3-j721e_sr2-hs-fs-evm.bin, sysfw-j721e_sr2-hs-fs-evm.itb from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a72

       * HS-SE

         * tiboot3-j721e_sr2-hs-evm.bin, sysfw-j721e_sr2-hs-evm.itb from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a72

.. ifconfig:: CONFIG_part_variant in ('J7200')

       * GP

         * tiboot3-j7200-gp-evm.bin from <output directory>/r5
         * tispl.bin_unsigned, u-boot.img_unsigned from <output directory>/a72

       * HS-FS

         * tiboot3-j7200_sr2-hs-fs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a72

       * HS-SE

         * tiboot3-j7200_sr2-hs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a72

.. ifconfig:: CONFIG_part_variant in ('J721S2')

       * GP

         * tiboot3-j721s2-gp-evm.bin from <output directory>/r5
         * tispl.bin_unsigned, u-boot.img_unsigned from <output directory>/a72

       * HS-FS

         * tiboot3-j721s2-hs-fs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a72

       * HS-SE

         * tiboot3-j721s2-hs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a72

.. ifconfig:: CONFIG_part_variant in ('J784S4')

       * GP

         * tiboot3-j784s4-gp-evm.bin from <output directory>/r5
         * tispl.bin_unsigned, u-boot.img_unsigned from <output directory>/a72

       * HS-FS

         * tiboot3-j784s4-hs-fs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a72

       * HS-SE

         * tiboot3-j784s4-hs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a72

.. ifconfig:: CONFIG_part_variant in ('J742S2')

       * GP

         * tiboot3-j742s2-gp-evm.bin from <output directory>/r5
         * tispl.bin_unsigned, u-boot.img_unsigned from <output directory>/a72

       * HS-FS

         * tiboot3-j742s2-hs-fs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a72

       * HS-SE

         * tiboot3-j742s2-hs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a72

.. ifconfig:: CONFIG_part_variant in ('AM64X')

       * GP

         * tiboot3-am64x-gp-evm.bin from <output directory>/r5
         * tispl.bin_unsigned, u-boot.img_unsigned from <output directory>/a53

       * HS-FS

         * tiboot3-am64x_sr2-hs-fs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a53

       * HS-SE

         * tiboot3-am64x_sr2-hs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a53

.. ifconfig:: CONFIG_part_variant in ('AM62X')

       * GP

         * tiboot3-am62x-gp-evm.bin from <output directory>/r5
         * tispl.bin_unsigned, u-boot.img_unsigned from <output directory>/a53

       * HS-FS

         * tiboot3-am62x-hs-fs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a53

       * HS-SE

         * tiboot3-am62x-hs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a53

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

       * GP

         * tiboot3-am62ax-gp-evm.bin from <output directory>/r5
         * tispl.bin_unsigned, u-boot.img_unsigned from <output directory>/a53

       * HS-FS

         * tiboot3-am62ax-hs-fs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a53

       * HS-SE

         * tiboot3-am62ax-hs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a53

.. ifconfig:: CONFIG_part_variant in ('AM62DX')

   * HS-FS

     * :file:`tiboot3-am62dx-hs-fs-evm.bin` from :file:`<output directory>/r5`
     * :file:`tispl.bin, u-boot.img` from :file:`<output directory>/a53`

   * HS-SE

     * :file:`tiboot3-am62dx-hs-evm.bin` from :file:`<output directory>/r5`
     * :file:`tispl.bin, u-boot.img` from :file:`<output directory>/a53`

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

       * HS-FS

         * tiboot3-am62px-hs-fs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a53

       * HS-SE

         * tiboot3-am62px-hs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a53

.. ifconfig:: CONFIG_part_variant in ('J722S')

       * HS-FS

         * tiboot3-j722s-hs-fs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a53

       * HS-SE

         * tiboot3-j722s-hs-evm.bin from <output directory>/r5
         * tispl.bin, u-boot.img from <output directory>/a53

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

       * **HS-FS**

         * tiboot3-am62lx-hs-fs-evm.bin
         * tispl.bin
         * u-boot.img

.. ifconfig:: CONFIG_part_variant in ('AM65X', 'J721E', 'J7200', 'AM64X', 'AM62X', 'AM62AX', 'AM62DX', 'AM62PX', 'J721S2', 'J784S4','J742S2', 'J722S', 'AM62LX')

   .. warning::

      Rename :file:`tiboot3-<board>-evm.bin` to :file:`tiboot3.bin` in order for the device to load this binary from the SD card boot partition.
      Also, (For GP devices only) rename :file:`tispl.bin_unsigned` to :file:`tispl.bin` and :file:`u-boot.img_unsigned` to :file:`u-boot.img` as well.

Image Formats
^^^^^^^^^^^^^

    .. ifconfig:: CONFIG_part_variant not in ('J7200', 'AM64X', 'J721S2', 'J721E', 'AM62X', 'AM62AX', 'AM62LX', 'J784S4','J742S2', 'J722S', 'AM57X')

       - tiboot3.bin

       .. code-block:: text

            +-----------------------+
            |        X.509          |
            |      Certificate      |
            | +-------------------+ |
            | |                   | |
            | |        R5         | |
            | |   u-boot-spl.bin  | |
            | |                   | |
            | +-------------------+ |
            | |                   | |
            | |     FIT header    | |
            | | +---------------+ | |
            | | |               | | |
            | | |   DTB 1...N   | | |
            | | +---------------+ | |
            | +-------------------+ |
            +-----------------------+

       - tispl.bin

       .. code-block:: text

            +-----------------------+
            |                       |
            |       FIT HEADER      |
            | +-------------------+ |
            | |                   | |
            | |      ARM64 ATF    | |
            | +-------------------+ |
            | |                   | |
            | |     ARM64 OPTEE   | |
            | +-------------------+ |
            | |                   | |
            | |      ARM64 SPL    | |
            | +-------------------+ |
            | |                   | |
            | |   SPL DTB 1...N   | |
            | +-------------------+ |
            +-----------------------+

       - sysfw.itb

       .. code-block:: text

            +-----------------------+
            |                       |
            |       FIT HEADER      |
            | +-------------------+ |
            | |                   | |
            | |     sysfw.bin     | |
            | +-------------------+ |
            | |                   | |
            | |    board config   | |
            | +-------------------+ |
            | |                   | |
            | |     PM config     | |
            | +-------------------+ |
            | |                   | |
            | |     RM config     | |
            | +-------------------+ |
            | |                   | |
            | |    Secure config  | |
            | +-------------------+ |
            +-----------------------+

    .. ifconfig:: CONFIG_part_variant in ('J721E')

       - tiboot3.bin

       .. code-block:: text

            +-----------------------+
            |        X.509          |
            |      Certificate      |
            | +-------------------+ |
            | |                   | |
            | |        R5         | |
            | |   u-boot-spl.bin  | |
            | |                   | |
            | +-------------------+ |
            | |                   | |
            | |     FIT header    | |
            | | +---------------+ | |
            | | |               | | |
            | | |   DTB 1...N   | | |
            | | +---------------+ | |
            | +-------------------+ |
            +-----------------------+

       - tispl.bin

       .. code-block:: text

            +-----------------------+
            |                       |
            |       FIT HEADER      |
            | +-------------------+ |
            | |                   | |
            | |      A72 ATF      | |
            | +-------------------+ |
            | |                   | |
            | |     A72 OPTEE     | |
            | +-------------------+ |
            | |                   | |
            | |      R5 DM FW     | |
            | +-------------------+ |
            | |                   | |
            | |      A72 SPL      | |
            | +-------------------+ |
            | |                   | |
            | |   SPL DTB 1...N   | |
            | +-------------------+ |
            +-----------------------+

       - sysfw.itb

       .. code-block:: text

            +-----------------------+
            |                       |
            |       FIT HEADER      |
            | +-------------------+ |
            | |                   | |
            | |     sysfw.bin     | |
            | +-------------------+ |
            | |                   | |
            | |    board config   | |
            | +-------------------+ |
            | |                   | |
            | |     PM config     | |
            | +-------------------+ |
            | |                   | |
            | |     RM config     | |
            | +-------------------+ |
            | |                   | |
            | |    Secure config  | |
            | +-------------------+ |
            +-----------------------+

    .. ifconfig:: CONFIG_part_variant in ('J7200', 'J721S2', 'J784S4','J742S2')

        - tiboot3.bin:

           .. code-block:: text

                    +-----------------------+
                    |        X.509          |
                    |      Certificate      |
                    | +-------------------+ |
                    | |                   | |
                    | |        R5         | |
                    | |   u-boot-spl.bin  | |
                    | |                   | |
                    | +-------------------+ |
                    | |                   | |
                    | |     FIT header    | |
                    | | +---------------+ | |
                    | | |               | | |
                    | | |   DTB 1...N   | | |
                    | | +---------------+ | |
                    | +-------------------+ |
                    | |                   | |
                    | |      FIT HEADER   | |
                    | | +---------------+ | |
                    | | |               | | |
                    | | |   sysfw.bin   | | |
                    | | +---------------+ | |
                    | | |               | | |
                    | | |  board config | | |
                    | | +---------------+ | |
                    | | |               | | |
                    | | |   PM config   | | |
                    | | +---------------+ | |
                    | | |               | | |
                    | | |   RM config   | | |
                    | | +---------------+ | |
                    | | |               | | |
                    | | | Secure config | | |
                    | | +---------------+ | |
                    | +-------------------+ |
                    +-----------------------+

        - tispl.bin

           .. code-block:: text

                    +-----------------------+
                    |                       |
                    |       FIT HEADER      |
                    | +-------------------+ |
                    | |                   | |
                    | |      A72 ATF      | |
                    | +-------------------+ |
                    | |                   | |
                    | |     A72 OPTEE     | |
                    | +-------------------+ |
                    | |                   | |
                    | |      R5 DM FW     | |
                    | +-------------------+ |
                    | |                   | |
                    | |      A72 SPL      | |
                    | +-------------------+ |
                    | |                   | |
                    | |   SPL DTB 1...N   | |
                    | +-------------------+ |
                    +-----------------------+

    .. ifconfig:: CONFIG_part_variant in ('AM64X')

        - tiboot3.bin:

           .. code-block:: text

                    +-----------------------+
                    |        X.509          |
                    |      Certificate      |
                    | +-------------------+ |
                    | |                   | |
                    | |        R5         | |
                    | |   u-boot-spl.bin  | |
                    | |                   | |
                    | +-------------------+ |
                    | |                   | |
                    | |     FIT header    | |
                    | | +---------------+ | |
                    | | |               | | |
                    | | |   DTB 1...N   | | |
                    | | +---------------+ | |
                    | +-------------------+ |
                    | |                   | |
                    | |      FIT HEADER   | |
                    | | +---------------+ | |
                    | | |               | | |
                    | | |   sysfw.bin   | | |
                    | | +---------------+ | |
                    | | |               | | |
                    | | |  board config | | |
                    | | +---------------+ | |
                    | | |               | | |
                    | | |   PM config   | | |
                    | | +---------------+ | |
                    | | |               | | |
                    | | |   RM config   | | |
                    | | +---------------+ | |
                    | | |               | | |
                    | | | Secure config | | |
                    | | +---------------+ | |
                    | +-------------------+ |
                    +-----------------------+

        - tispl.bin

           .. code-block:: text

                    +-----------------------+
                    |                       |
                    |       FIT HEADER      |
                    | +-------------------+ |
                    | |                   | |
                    | |      A53 ATF      | |
                    | +-------------------+ |
                    | |                   | |
                    | |     A53 OPTEE     | |
                    | +-------------------+ |
                    | |                   | |
                    | |      A53 SPL      | |
                    | +-------------------+ |
                    | |                   | |
                    | |   SPL DTB 1...N   | |
                    | +-------------------+ |
                    +-----------------------+

    .. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX', 'J722S')

       - tiboot3.bin:

       .. code-block:: text

            +-----------------------+
            |        X.509          |
            |      Certificate      |
            | +-------------------+ |
            | |                   | |
            | |        R5         | |
            | |   u-boot-spl.bin  | |
            | |                   | |
            | +-------------------+ |
            | |                   | |
            | |TIFS with board cfg| |
            | |                   | |
            | +-------------------+ |
            | |                   | |
            | |                   | |
            | |     FIT header    | |
            | | +---------------+ | |
            | | |               | | |
            | | |   DTB 1...N   | | |
            | | +---------------+ | |
            | +-------------------+ |
            +-----------------------+

       - tispl.bin

       .. code-block:: text

            +-----------------------+
            |                       |
            |       FIT HEADER      |
            | +-------------------+ |
            | |                   | |
            | |      A53 ATF      | |
            | +-------------------+ |
            | |                   | |
            | |     A53 OPTEE     | |
            | +-------------------+ |
            | |                   | |
            | |      R5 DM FW     | |
            | +-------------------+ |
            | |                   | |
            | |      A53 SPL      | |
            | +-------------------+ |
            | |                   | |
            | |   SPL DTB 1...N   | |
            | +-------------------+ |
            +-----------------------+

    .. ifconfig:: CONFIG_part_variant in ('AM62LX')

       - tiboot3.bin

       .. code-block:: text

              TIBOOT3
          ┌─────────────┐
          │    X.509    │
          │ Certificate │
          │┌───────────┐│
          ││   BL-1    ││
          │├───────────┤│
          ││   TIFS    ││
          │├───────────┤│
          ││ TIFS CERT ││
          │└───────────┘│
          └─────────────┘

       - tispl.bin

       .. code-block:: text

               TISPL
          ┌─────────────┐
          │    X.509    │
          │ Certificate │
          │┌───────────┐│
          ││   BL-31   ││
          │├───────────┤│
          ││   TIFS    ││
          │├───────────┤│
          ││ TIFS CERT ││
          │├───────────┤│
          ││ BRD + SEC ││
          ││  CONFIGS  ││
          │├───────────┤│
          ││  U-BOOT   ││
          ││    SPL    ││
          │└───────────┘│
          └─────────────┘

.. _Boot-Flow-label:

Boot Flow
^^^^^^^^^
.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family', 'AM57X_family')

    Booting the Linux kernel on an embedded platform is not as simple as simply
    pointing a program counter to the kernel location and letting the processor
    run. This section will review the four bootloader software stages that must
    be run before the kernel can be booted and run on the device.

    Application processors such as the the AM335x are complex pieces of hardware,
    but have limited internal RAM (e.g., 128KB). Because of this limited amount
    of RAM, multiple bootloader stages are needed. These bootloader stages
    systematically unlock the full functionality of the device so that all
    complexities of the device are available to the kernel.

    There are four distinct bootloader stages:

    .. Image:: /images/U-Boot_Boot_Order_32bit.png

    1. ROM Code

    The first stage bootloader is housed in ROM on the device. The ROM code is
    the first block of code that is automatically run on device start-up or
    after power-on reset (POR). The ROM bootloader code is hardcoded into the
    device and cannot be changed by the user. Because of this, it is important
    to get an understanding of what exactly the ROM code is doing.

    The ROM code has two main functions:

    * Configuration of the device and initialization of primary peripherals
      such as stack setup, configuring the Watchdog Timer (see TRM for details)
      as well as the PLL and system clocks configuration
    * Readies the device for next bootloader by checking boot sources for next
      stage of bootloader (SPL) as well as loading the actual next stage
      bootloader code into memory and starting it

    The list of booting devices that the ROM code will search through for the
    second stage bootloader is configured by the voltage levels set on the
    devices SYSBOOT pins on startup. These pins also set other boot parameters
    (i.e. expected crystal frequency, bus width of external memory). For more
    information on the SYSBOOT pins and associated boot parameters see the
    device TRM.

    2. SPL or MLO

    The second stage bootloader is known as the SPL (Secondary Program Loader),
    but is sometimes referred to as the MLO (MMC Card Loader). The SPL is the
    first stage of U-Boot, and must be loaded from one of the boot sources into
    internal RAM. The SPL has very limited configuration or user interaction,
    and mainly serves to initialize the external DDR memory and set-up the boot
    process for the next bootloader stage: U-Boot.

    3. U-Boot

    U-Boot allows for powerful command-based control over the kernel boot
    environment via a serial terminal. The user has control over a number of
    parameters such as boot arguments and the kernel boot command. In addition,
    U-Boot environment variables can be configured. These environment variables
    are stored in the **uEnv.txt** file on your storage medium or directly in
    a Flash-based memory if configured such. These environment variables can be
    viewed, modified, and saved using the **env print**, **env set**, and
    **env save** commands, respectively. U-Boot is also a very useful tool to
    program and manipulate a wide range of external memory devices as well as
    a helpful aid during custom board bringup.

    4. Linux Kernel

    **zImage** is the compressed kernel image wrapped with header info that
    describes the kernel. This header includes the target architecture, the
    operating system, kernel size, entry points, etc. The loading of the kernel
    image is typically performed through the use of scripts stored in the U-Boot
    environment (all starting with the **bootcmd** ENV variable that gets
    executed after the autoboot countdown expires or manually by entering the
    **boot** command at the U-Boot prompt). This also involves passing a board-
    specific device tree blob (DTB) as an argument to U-Boot's **bootz**
    command that will extract and start the actual kernel.

.. ifconfig:: CONFIG_part_family not in ('General_family', 'AM335X_family', 'AM437X_family', 'AM62LX_family', 'AM57X_family')

    On K3 architecture based devices, ROM supports boot only via MCU(R5). This means that
    bootloader has to run on R5 core. In order to meet this constraint, keeping
    safety in picture and to have faster boot time, the software boot architecture
    is designed as below:

    .. ifconfig:: CONFIG_part_family not in ('J7_family', 'AM64X_family', 'AM62X_family', 'AM62AX_family')

         .. code-block:: text

             +------------------------------------------------------------------------+
             |        DMSC            |         R5            |        ARM64          |
             +------------------------------------------------------------------------+
             |    +--------+          |                       |                       |
             |    |  Reset |          |                       |                       |
             |    +--------+          |                       |                       |
             |         :              |                       |                       |
             |    +--------+          |   +-----------+       |                       |
             |    | *ROM*  |----------|-->| Reset rls |       |                       |
             |    +--------+          |   +-----------+       |                       |
             |    |        |          |         :             |                       |
             |    |  ROM   |          |         :             |                       |
             |    |services|          |         :             |                       |
             |    |        |          |   +-------------+     |                       |
             |    |        |          |   |  *R5 ROM*   |     |                       |
             |    |        |          |   +-------------+     |                       |
             |    |        |<---------|---|Load and auth|     |                       |
             |    |        |          |   | tiboot3.bin |     |                       |
             |    |        |          |   +-------------+     |                       |
             |    |        |          |         :             |                       |
             |    |        |          |         :             |                       |
             |    |        |          |         :             |                       |
             |    |        |          |   +-------------+     |                       |
             |    |        |          |   |  *R5 SPL*   |     |                       |
             |    |        |          |   +-------------+     |                       |
             |    |        |          |   |    Load     |     |                       |
             |    |        |          |   |  sysfw.itb  |     |                       |
             |    | Start  |          |   +-------------+     |                       |
             |    | System |<---------|---|    Start    |     |                       |
             |    |Firmware|          |   |    SYSFW    |     |                       |
             |    +--------+          |   +-------------+     |                       |
             |        :               |   |             |     |                       |
             |    +---------+         |   |   Load      |     |                       |
             |    | *SYSFW* |         |   |   system    |     |                       |
             |    +---------+         |   | Config data |     |                       |
             |    |         |<--------|---|             |     |                       |
             |    |         |         |   +-------------+     |                       |
             |    |         |         |   |             |     |                       |
             |    |         |         |   |    DDR      |     |                       |
             |    |         |         |   |   config    |     |                       |
             |    |         |         |   +-------------+     |                       |
             |    |         |         |   |             |     |                       |
             |    |         |<--------|---| Start A53   |     |                       |
             |    |         |         |   |  and Reset  |     |                       |
             |    |         |         |   +-------------+     |                       |
             |    |         |         |                       |     +-----------+     |
             |    |         |---------|-----------------------|---->| Reset rls |     |
             |    |         |         |                       |     +-----------+     |
             |    |  DMSC   |         |                       |          :            |
             |    |Services |         |                       |     +-----------+     |
             |    |         |<--------|-----------------------|---->|*ATF/OPTEE*|     |
             |    |         |         |                       |     +-----------+     |
             |    |         |         |                       |          :            |
             |    |         |         |                       |     +-----------+     |
             |    |         |<--------|-----------------------|---->| *A53 SPL* |     |
             |    |         |         |                       |     +-----------+     |
             |    |         |         |                       |     |   Load    |     |
             |    |         |         |                       |     | u-boot.img|     |
             |    |         |         |                       |     +-----------+     |
             |    |         |         |                       |          :            |
             |    |         |         |                       |     +-----------+     |
             |    |         |<--------|-----------------------|---->| *U-Boot*  |     |
             |    |         |         |                       |     +-----------+     |
             |    |         |         |                       |     |  prompt   |     |
             |    |         |         |                       |     +-----------+     |
             |    +---------+         |                       |                       |
             |                        |                       |                       |
             +------------------------------------------------------------------------+

    .. ifconfig:: CONFIG_part_variant in ('J721E')

        .. code-block:: text

            +------------------------------------------------------------------------+-----------------------+
            |        DMSC            |      MCU R5           |        A72            |  MAIN R5/C66x/C7x     |
            +------------------------------------------------------------------------+-----------------------+
            |    +--------+          |                       |                       |                       |
            |    |  Reset |          |                       |                       |                       |
            |    +--------+          |                       |                       |                       |
            |         :              |                       |                       |                       |
            |    +--------+          |   +-----------+       |                       |                       |
            |    | *ROM*  |----------|-->| Reset rls |       |                       |                       |
            |    +--------+          |   +-----------+       |                       |                       |
            |    |        |          |         :             |                       |                       |
            |    |  ROM   |          |         :             |                       |                       |
            |    |services|          |         :             |                       |                       |
            |    |        |          |   +-------------+     |                       |                       |
            |    |        |          |   |  *R5 ROM*   |     |                       |                       |
            |    |        |          |   +-------------+     |                       |                       |
            |    |        |<---------|---|Load and auth|     |                       |                       |
            |    |        |          |   | tiboot3.bin |     |                       |                       |
            |    |        |          |   +-------------+     |                       |                       |
            |    |        |          |         :             |                       |                       |
            |    |        |          |         :             |                       |                       |
            |    |        |          |         :             |                       |                       |
            |    |        |          |   +-------------+     |                       |                       |
            |    |        |          |   |  *R5 SPL*   |     |                       |                       |
            |    |        |          |   +-------------+     |                       |                       |
            |    |        |          |   |    Load     |     |                       |                       |
            |    |        |          |   |  sysfw.itb  |     |                       |                       |
            |    | Start  |          |   +-------------+     |                       |                       |
            |    | System |<---------|---|    Start    |     |                       |                       |
            |    |Firmware|          |   |    SYSFW    |     |                       |                       |
            |    +--------+          |   +-------------+     |                       |                       |
            |        :               |   |             |     |                       |                       |
            |    +---------+         |   |   Load      |     |                       |                       |
            |    | *SYSFW* |         |   |   system    |     |                       |                       |
            |    +---------+         |   | Config data |     |                       |                       |
            |    |         |<--------|---|             |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |   |    DDR      |     |                       |                       |
            |    |         |         |   |   config    |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |   |    Load     |     |                       |                       |
            |    |         |         |   |  tispl.bin  |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |   |   Load R5   |     |                       |                       |
            |    |         |         |   |   firmware  |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |<--------|---| Start A72   |     |                       |                       |
            |    |         |         |   | and jump to |     |                       |                       |
            |    |         |         |   | DM fw image |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |---------|-----------------------|---->| Reset rls |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |  TIFS   |         |                       |          :            |                       |
            |    |Services |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|---->|*ATF/OPTEE*|     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |          :            |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|---->| *A72 SPL* |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |     |   Load    |     |                       |
            |    |         |         |                       |     | u-boot.img|     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |          :            |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|---->| *U-Boot*  |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |     |  prompt   |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |     |  Load R5  |     |                       |
            |    |         |         |                       |     |  Firmware |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|-----|  Start R5 |     |      +-----------+    |
            |    |         |---------|-----------------------|-----+-----------+-----|----->| R5 starts |    |
            |    |         |         |                       |     |  Load C6  |     |      +-----------+    |
            |    |         |         |                       |     |  Firmware |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|-----|  Start C6 |     |      +-----------+    |
            |    |         |---------|-----------------------|-----+-----------+-----|----->| C6 starts |    |
            |    |         |         |                       |     |  Load C7  |     |      +-----------+    |
            |    |         |         |                       |     |  Firmware |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|-----|  Start C7 |     |      +-----------+    |
            |    |         |---------|-----------------------|-----+-----------+-----|----->| C7 starts |    |
            |    +---------+         |                       |                       |      +-----------+    |
            |                        |                       |                       |                       |
            +------------------------------------------------------------------------+-----------------------+

    .. ifconfig:: CONFIG_part_variant in ('J7200', 'J721S2', 'J784S4','J742S2')

        .. code-block:: text

            +------------------------------------------------------------------------+-----------------------+
            |        SMS             |      MCU R5           |        A72            |  MAIN R5/C7x          |
            +------------------------------------------------------------------------+-----------------------+
            |    +--------+          |                       |                       |                       |
            |    |  Reset |          |                       |                       |                       |
            |    +--------+          |                       |                       |                       |
            |         :              |                       |                       |                       |
            |    +--------+          |   +-----------+       |                       |                       |
            |    | *ROM*  |----------|-->| Reset rls |       |                       |                       |
            |    +--------+          |   +-----------+       |                       |                       |
            |    |        |          |         :             |                       |                       |
            |    |  ROM   |          |         :             |                       |                       |
            |    |services|          |         :             |                       |                       |
            |    |        |          |   +-------------+     |                       |                       |
            |    |        |          |   |  *R5 ROM*   |     |                       |                       |
            |    |        |          |   +-------------+     |                       |                       |
            |    |        |<---------|---|Load and auth|     |                       |                       |
            |    |        |          |   | tiboot3.bin |     |                       |                       |
            |    | Start  |          |   +-------------+     |                       |                       |
            |    |  TIFS  |<---------|---|    Start    |     |                       |                       |
            |    |        |          |   |    TIFS     |     |                       |                       |
            |    +--------+          |   +-------------+     |                       |                       |
            |        :               |   |             |     |                       |                       |
            |    +---------+         |   |   Load      |     |                       |                       |
            |    | *TIFS*  |         |   |   system    |     |                       |                       |
            |    +---------+         |   | Config data |     |                       |                       |
            |    |         |<--------|---|             |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |         :             |                       |                       |
            |    |         |         |         :             |                       |                       |
            |    |         |         |         :             |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |   |  *R5 SPL*   |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |   |    DDR      |     |                       |                       |
            |    |         |         |   |   config    |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |   |    Load     |     |                       |                       |
            |    |         |         |   |  tispl.bin  |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |   |   Load R5   |     |                       |                       |
            |    |         |         |   |   firmware  |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |<--------|---| Start A72   |     |                       |                       |
            |    |         |         |   | and jump to |     |                       |                       |
            |    |         |         |   | DM fw image |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |---------|-----------------------|---->| Reset rls |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |  TIFS   |         |                       |          :            |                       |
            |    |Services |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|---->|*ATF/OPTEE*|     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |          :            |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|---->| *A72 SPL* |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |     |   Load    |     |                       |
            |    |         |         |                       |     | u-boot.img|     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |          :            |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|---->| *U-Boot*  |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |     |  prompt   |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |     |  Load R5  |     |                       |
            |    |         |         |                       |     |  Firmware |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|-----|  Start R5 |     |      +-----------+    |
            |    |         |---------|-----------------------|-----+-----------+-----|----->| R5 starts |    |
            |    |         |         |                       |     |  Load C7  |     |      +-----------+    |
            |    |         |         |                       |     |  Firmware |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|-----|  Start C7 |     |      +-----------+    |
            |    |         |---------|-----------------------|-----+-----------+-----|----->| C7 starts |    |
            |    |         |         |                       |                       |      +-----------+    |
            |    |         |         |                       |                       |                       |
            |    +---------+         |                       |                       |                       |
            |                        |                       |                       |                       |
            +------------------------------------------------------------------------+-----------------------+

    .. ifconfig:: CONFIG_part_variant in ('AM64X')

        .. code-block:: text

            +------------------------------------------------------------------------+-----------------------+
            |        DMSC            |      MAIN R50         |         A53           |   MAIN R51            |
            +------------------------------------------------------------------------+-----------------------+
            |    +--------+          |                       |                       |                       |
            |    |  Reset |          |                       |                       |                       |
            |    +--------+          |                       |                       |                       |
            |         :              |                       |                       |                       |
            |    +--------+          |   +-----------+       |                       |                       |
            |    | *ROM*  |----------|-->| Reset rls |       |                       |                       |
            |    +--------+          |   +-----------+       |                       |                       |
            |    |        |          |         :             |                       |                       |
            |    |  ROM   |          |         :             |                       |                       |
            |    |services|          |         :             |                       |                       |
            |    |        |          |   +-------------+     |                       |                       |
            |    |        |          |   |  *R5 ROM*   |     |                       |                       |
            |    |        |          |   +-------------+     |                       |                       |
            |    |        |<---------|---|Load and auth|     |                       |                       |
            |    |        |          |   | tiboot3.bin |     |                       |                       |
            |    | Start  |          |   +-------------+     |                       |                       |
            |    | SYSFW  |<---------|---|    Start    |     |                       |                       |
            |    |        |          |   |    SYSFW    |     |                       |                       |
            |    +--------+          |   +-------------+     |                       |                       |
            |        :               |   |             |     |                       |                       |
            |    +---------+         |   |   Load      |     |                       |                       |
            |    | *SYSFW* |         |   |   system    |     |                       |                       |
            |    +---------+         |   | Config data |     |                       |                       |
            |    |         |<--------|---|             |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |         :             |                       |                       |
            |    |         |         |         :             |                       |                       |
            |    |         |         |         :             |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |   |  *R5 SPL*   |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |   |    DDR      |     |                       |                       |
            |    |         |         |   |   config    |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |   |    Load     |     |                       |                       |
            |    |         |         |   |  tispl.bin  |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |<--------|---| Start A53   |     |                       |                       |
            |    |         |         |   +-------------+     |                       |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |---------|-----------------------|---->| Reset rls |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |  SYSFW  |         |                       |          :            |                       |
            |    |Services |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|---->|*ATF/OPTEE*|     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |          :            |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|---->| *A53 SPL* |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |     |   Load    |     |                       |
            |    |         |         |                       |     | u-boot.img|     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |          :            |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|---->| *U-Boot*  |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |     |  prompt   |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |         |                       |     |  Load R5  |     |                       |
            |    |         |         |                       |     |  Firmware |     |                       |
            |    |         |         |                       |     +-----------+     |                       |
            |    |         |<--------|-----------------------|-----|  Start R5 |     |      +-----------+    |
            |    |         |---------|-----------------------|-----+-----------+-----|----->| R5 starts |    |
            |    |         |         |                       |                       |      +-----------+    |
            |    |         |         |                       |                       |                       |
            |    +---------+         |                       |                       |                       |
            |                        |                       |                       |                       |
            +------------------------------------------------------------------------+-----------------------+

    .. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX', 'J722S')

        .. code-block:: text

            +------------------------------------------------------------------------+
            |        TIFS            |      Main R5          |        A53            |
            +------------------------------------------------------------------------+
            |    +--------+          |                       |                       |
            |    |  Reset |          |                       |                       |
            |    +--------+          |                       |                       |
            |         :              |                       |                       |
            |    +--------+          |   +-----------+       |                       |
            |    | *ROM*  |----------|-->| Reset rls |       |                       |
            |    +--------+          |   +-----------+       |                       |
            |    |        |          |         :             |                       |
            |    |  ROM   |          |         :             |                       |
            |    |services|          |         :             |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |          |   |  *R5 ROM*   |     |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |<---------|---|Load and auth|     |                       |
            |    |        |          |   | tiboot3.bin |     |                       |
            |    +--------+          |   +-------------+     |                       |
            |    |        |<---------|---| Load sysfw  |     |                       |
            |    |        |          |   | part to TIFS|     |                       |
            |    |        |          |   | core        |     |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |          |         :             |                       |
            |    |        |          |         :             |                       |
            |    |        |          |         :             |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |          |   |  *R5 SPL*   |     |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |          |   |    DDR      |     |                       |
            |    |        |          |   |   config    |     |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |          |   |    Load     |     |                       |
            |    |        |          |   |  tispl.bin  |     |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |          |   |   Load R5   |     |                       |
            |    |        |          |   |   firmware  |     |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |<---------|---| Start A53   |     |                       |
            |    |        |          |   | and jump to |     |                       |
            |    |        |          |   | DM fw image |     |                       |
            |    |        |          |   +-------------+     |                       |
            |    |        |          |                       |     +-----------+     |
            |    |        |----------|-----------------------|---->| Reset rls |     |
            |    |        |          |                       |     +-----------+     |
            |    |  TIFS  |          |                       |          :            |
            |    |Services|          |                       |     +-----------+     |
            |    |        |<---------|-----------------------|---->|*ATF/OPTEE*|     |
            |    |        |          |                       |     +-----------+     |
            |    |        |          |                       |          :            |
            |    |        |          |                       |     +-----------+     |
            |    |        |<---------|-----------------------|---->| *A53 SPL* |     |
            |    |        |          |                       |     +-----------+     |
            |    |        |          |                       |     |   Load    |     |
            |    |        |          |                       |     | u-boot.img|     |
            |    |        |          |                       |     +-----------+     |
            |    |        |          |                       |          :            |
            |    |        |          |                       |     +-----------+     |
            |    |        |<---------|-----------------------|---->| *U-Boot*  |     |
            |    |        |          |                       |     +-----------+     |
            |    |        |          |                       |     |  prompt   |     |
            |    |        |----------|-----------------------|-----+-----------+-----|
            |    +--------+          |                       |                       |
            |                        |                       |                       |
            +------------------------------------------------------------------------+

    Here |__SYSFW_CORE_NAME__| acts as master and provides all the critical services. R5/ARM64
    requests |__SYSFW_CORE_NAME__| to get these services done as shown in the above diagram.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   Unlike with most other K3 SoCs, the AM62LX does not have an Cortext-R5
   MCU core which ROM uses to initialize the SoC. Therefore it uses a 2
   phase ROM boot. The first phase will load the tiboot3.bin image which
   contains Trusted-Firmware-A's BL-1 loader along with the typical X.509
   certificate to authenticate and validate the image which is used to
   intialize the console and DDR for the next phase.

   .. code-block:: text

      ┌───────────────────┐┌───────────────────┐
      │    Secure ROM     ││    Public ROM     │
      │     SMS (M4)      ││   (Cortex-A53)    │
      │                   ││                   │
      │┌─────────────────┐││                   │
      ││  Reset Release  │││                   │
      │└────────┬────────┘││                   │
      │         │         ││                   │
      │┌────────▼────────┐││                   │
      ││    ROM Init     │││                   │
      │└────────┬────────┘││                   │
      │         │         ││                   │
      │┌────────▼────────┐││┌─────────────────┐│
      ││   Release A53   ┼┼┼►   Release A53   ││
      │└─────────────────┘││└────────┬────────┘│
      │                   ││         │         │
      │  Validate Image   ││┌────────▼────────┐│
      │┌─────────────────┐│││    ROM Init     ││
      ││ Integrity Check ◄┼┼┼   (1st Phase)   ││
      │├─────────────────│││└────────┬────────┘│
      ││ Authentication  │││         │         │
      │├─────────────────┤││┌────────▼────────┐│
      ││    Decryption   ││││       WFI       ││
      │└────────┬────────┘││└─────────────────┘│
      │         │         ││                   │
      │┌────────▼────────┐││    End of ROM     │
      ││  Wait for WFI   │││~~~~~~~~~~~~~~~~~~~│
      ││  on Cortex-A53  │││     Start of      │
      │└────────┬────────┘││       BL-1        │
      │         │         ││                   │
      │┌────────▼────────┐││┌─────────────────┐│
      ││    Start BL-1   ┼┼┼►    DDR Init     ││
      │└────────┬────────┘││└────────┬────────┘│
      │         │         ││         │         │
      │┌────────▼────────┐││┌────────▼────────┐│
      ││  Wait for BL-1  ◄┼┼┼  Send BL-1 Done ││
      ││     Done Msg    │││└────────┬────────┘│
      │└─────────────────┘││         │         │
      │                   ││┌────────▼────────┐│
      │                   │││       WFI       ││
      │                   ││└─────────────────┘│
      └───────────────────┘└───────────────────┘

   After the BL-1 sends a message back to the Secure ROM to indicate it
   has completed, the Secure ROM will reset the A53 back into Public ROM
   to begin the 2nd ROM boot phase to load the tispl.bin into the SoC.

   .. code-block:: text

      ┌───────────────────┐┌───────────────────┐
      │    Secure ROM     ││    Public ROM     │
      │     SMS (M4)      ││   (Cortex-A53)    │
      │                   ││                   │
      │┌─────────────────┐││                   │
      ││  Program Reset  │││┌─────────────────┐│
      ││   Vector And    ┼┼┼►   Release A53   ││
      ││    Reset A53    │││└────────┬────────┘│
      │└─────────────────┘││         │         │
      │                   ││         │         │
      │   Validate Image  ││┌────────▼────────┐│
      │┌─────────────────┐│││    ROM Init     ││
      ││ Integrity Check ◄┼┼┼   (2nd Phase)   ││
      │├─────────────────┤││└────────┬────────┘│
      ││ Authentication  │││         │         │
      │├─────────────────┤││┌────────▼────────┐│
      ││   Decryption    ││││       WFI       ││
      │└────────┬────────┘││└─────────────────┘│
      │         │         ││                   │
      │┌────────▼────────┐││     End of ROM    │
      ││  Wait for WFI   │││~~~~~~~~~~~~~~~~~~~│
      ││  on Cortex-A53  │││                   │
      │└────────┬────────┘││                   │
      │         │         ││                   │
      │┌────────▼────────┐││                   │
      ││  Program Reset  │││┌─────────────────┐│
      ││   Vector And    ┼┼┼►   TF-A (BL-31)  ││
      ││    Reset A53    │││└────────┬────────┘│
      │└────────┬────────┘││         │         │
      │         │         ││┌────────▼────────┐│
      │┌────────▼────────┐│││    U-Boot SPL   ││
      ││  Prep M4 Reset  │││└────────┬────────┘│
      │└────────┬────────┘││         │         │
      │         │         ││┌────────▼────────┐│
      │┌────────▼────────┐│││     U-Boot      ││
      ││    Boot TI-FS   │││└────────┬────────┘│
      │└────────┬────────┘││         │         │
      │         │         ││         │         │
      │     End of ROM    ││         │         │
      │~~~~~~~~~~~~~~~~~~~││         │         │
      │         │         ││┌────────▼────────┐│
      │┌────────▼────────┐│││                 ││
      ││                 ││││                 ││
      ││      TI-FS      ││││      Linux      ││
      └┴─────────────────┴┘└┴─────────────────┴┘

   From there TIFS, TF-A and U-Boot will has completed their
   initialization routines which can begin loading the operating system
   and complete the boot process.

U-Boot Environment
^^^^^^^^^^^^^^^^^^

.. note::

   SDK 9.0 will not default to the environments that are saved on the boards,
   It will default to the ones that are given with the particular uboot in
   the release.

By default the SDK builds will have the default environments whenever being
run, to have some custom environments, one needs to rely on uEnv.txt
file.

The added benefit of using uEnv.txt is that it is more granular than the
saveenv counterpart as we can choose to store the variables that are
actually being set during the development workflow.

**Writing to MMC/EMMC**

.. code-block:: console

  => env export -t $loadaddr <list of variables>
  => fatwrite mmc ${mmcdev} ${loadaddr} ${bootenvfile} ${filesize}

The following will update the uEnv.txt file on the bootmedia and then
whenever "run envboot" is run on the board, uEnv.txt will be read based on
mmcdev value to be read either from emmc/sd card.

You can specifically choose the variables that you are changing in your
development process so that the other variables are not affected due to the
whole environment being saved. Optionally, one can save the full
environment too in uEnv.txt by not specifying <list of variables> this
will have some issues with the ethernet mac addresses not being overridden
but other things will be set.

**Reading from MMC/EMMC**

By default run envboot will read it from the MMC/EMMC partition ( based on
mmcdev) and set the environments.

If manually needs to be done then the environment can be read from the
filesystem and then imported

.. code-block:: console

  => fatload mmc ${mmcdev} ${loadaddr} ${bootenvfile}
  => env import -t ${loadaddr} ${filesize}

For production environments if one needs to rely on saveenv counterpart
then they can always refer to the `commit <https://source.denx.de/u-boot/u-boot/-/commit/a5e8678e0a32f85ad012aea7641e9534ada5c0fe>`__

.. rubric:: Networking Environment
   :name: networking-environment

When using a USB-Ethernet dongle a valid MAC address must be set in the
environment. To create a valid address please read `**this
page** <https://github.com/u-boot/u-boot/blob/v2024.04/doc/README.usb#L208>`__.
Then issue the following command:

.. code-block:: console

    => setenv usbethaddr value:from:link:above

You can use the **printenv** command to see if **usbethaddr** is already
set.

Then start the USB subsystem:

.. code-block:: console

    => usb start

The default behavior of U-Boot is to use all information that a DHCP
server passes to us when the user issues the **dhcp** command. This will
include the dhcp parameter *next-server* which indicates where to fetch
files from via TFTP. There may be times however where the dhcp server on
your network provides incorrect information and you are unable to modify
the server. In this case the following steps can be helpful:

.. code-block:: console

    => setenv autoload no
    => dhcp
    => setenv serverip correct.server.ip
    => tftp

Another alternative is to use the full syntax of the tftp command:

.. code-block:: console

    => setenv autoload no
    => dhcp
    => tftp ${loadaddr} server.ip:fileName

Available RAM for image download
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To know the amount of RAM available for downloading images or for other
usage, use ``bdinfo`` command.

.. code-block:: console

    => bdinfo
    arch_number = 0x00000000
    boot_params = 0x80000100
    DRAM bank   = 0x00000000
    -> start    = 0x80000000
    -> size     = 0x7F000000
    baudrate    = 115200 bps
    TLB addr    = 0xFEFF0000
    relocaddr   = 0xFEF30000
    reloc off   = 0x7E730000
    irq_sp      = 0xFCEF8880
    sp start    = 0xFCEF8870
    Early malloc usage: 890 / 2000

After booting, U-Boot relocates itself (along with its various reserved
RAM areas) and places itself at end of available RAM (starting at
``relocaddr`` in ``bdinfo`` output above). Only the stack is located
just before that area. The address of top of the stack is in
``sp start`` in ``bdinfo`` output and it grows downwards. Users should
reserve at least about 1MB for stack, so in the example output above,
RAM in the range of ``[0x80000000, 0xFCE00000]`` is safely available for
use.

Device Trees
^^^^^^^^^^^^

A note about device trees. Now all supported boards are required to use a
device tree to boot. To facilitate this in supported platforms, a command
in U-Boot environment **findfdt** is available that will set the **fdtfile**
variable to the name of the device tree to use, as found with the kernel
sources. In the Keystone-2 family devices (K2H/K/E/L/G), it is specified
by **name\_fdt** variable for each platform. The device tree is expected
to be loaded from the same media as the kernel, and from the same relative path.

.. _AM64-SRAM-Layout-label:

SRAM memory Layout during initial bootloader stage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The SRAM memory layout explains the memory used for Bootloader's operation.

    .. ifconfig:: CONFIG_part_variant in ('AM64X')

        .. code-block:: text

            ┌──────────────────────────────────────┐0x70000000
            │                                      │
            │                                      │
            │                                      │
            │    SPL IMAGE (Max size 1.5 MB)       │
            │                                      │
            │                                      │
            │                                      │
            ├──────────────────────────────────────┤0x7017FFFF
            │                                      │
            │           SPL STACK                  │
            │                                      │
            ├──────────────────────────────────────┤0x70192727
            │          GLOBAL DATA(216 B)          │
            ├──────────────────────────────────────┤0x701927FF
            │                                      │
            │       INITIAL HEAP (32 KB)           │
            │                                      │
            ├──────────────────────────────────────┤0x7019A7FF
            │                                      │
            │          BSS  (20 KB)                │
            ├──────────────────────────────────────┤0x7019F7FF
            │         EEPROM DATA (2 KB)           │
            ├──────────────────────────────────────┤0x7019FFFF
            │                                      │
            │                                      │
            │     UNALLOCATED AREA (123 KB)        │
            │                                      │
            │                                      │
            ├──────────────────────────────────────┤0x701BEBFB
            │   BOOT PARAMETER INDEX TABLE (5124 B)│
            ├──────────────────────────────────────┤0x701BFFFF
            │                                      │
            │             TF-A (128 KB)            │
            │                                      │
            ├──────────────────────────────────────┤0x701DFFFF
            │                                      │
            │      DMSC CODE AREA (128 KB)         │
            │                                      │
            └──────────────────────────────────────┘0x701FFFFF

        - In the last 128 KB of memory used by DMSC during run time, initial 80 KB
          gets freed after a security handover happens. The last 48 KB still will be used by DMSC.
        - For more details on Security handover see `here <https://software-dl.ti.com/tisci/esd/latest/6_topic_user_guides/security_handover.html>`__ .

    .. ifconfig:: CONFIG_part_variant in ('AM62X')

        .. code-block:: text

            ┌──────────────────────────────────────┐0x43c00000
            │                                      │
            │                                      │
            │               SPL IMAGE              │
            │           (Max size 192 KB)          │
            │            (excluding BSS)           │
            │             (196608B  Max)           │
            │                                      │
            ├──────────────────────────────────────┤0x43c30000
            │                                      │
            │                                      │
            │            STACK (13568B Max)        │
            │                                      │
            │                                      │
            ├──────────────────────────────────────┤
            │         Global Data (428B Max)       │
            ├──────────────────────────────────────┤
            │                                      │
            │            HEAP (28KB Max)           │
            │                                      │
            ├──────────────────────────────────────┤0x43c3a7f0
            │                                      │
            │             EMPTY (16B)              │
            │                                      │
            ├──────────────────────────────────────┤0x43c3a800
            │                                      │
            │                                      │
            │         DM config data (2KB)         │
            │                                      │
            │                                      │
            ├──────────────────────────────────────┤0x43c3b000
            │                                      │
            │             BSS (12KB)               │
            │                                      │
            ├──────────────────────────────────────┤0x43c3e000
            │                                      │
            │                                      │
            │           EMPTY (4.5KB)              │
            │        (Reserved for ROM)            │
            │                                      │
            ├──────────────────────────────────────┤0x43c3f1e0
            │                                      │
            │       ROM Boot parameter table       │
            │    + Extended boot info (3.5 KB)     │
            │                                      │
            └──────────────────────────────────────┘0x43c3ffff

    .. ifconfig:: CONFIG_part_variant in ('AM62AX','AM62PX','AM62DX')

        .. code-block:: console

            ┌──────────────────────────────────────┐0x43c00000
            │                                      │
            │                                      │
            │               SPL IMAGE              │
            │           (Max size 188 KB)          │
            │            (excluding BSS)           │
            │             (192512B  Max)           │
            │                                      │
            ├──────────────────────────────────────┤0x43c2f000
            │                                      │
            │                                      │
            │            STACK (17KB Max)          │
            │                                      │
            │                                      │
            ├──────────────────────────────────────┤
            │         Global Data (428B Max)       │
            ├──────────────────────────────────────┤
            │                                      │
            │            HEAP (28997B Max)         │
            │                                      │
            ├──────────────────────────────────────┤0x43c3a7f0
            │                                      │
            │             EMPTY (16B)              │
            │                                      │
            ├──────────────────────────────────────┤0x43c3a800
            │                                      │
            │                                      │
            │         DM config data (2KB)         │
            │                                      │
            │                                      │
            ├──────────────────────────────────────┤0x43c3b000
            │                                      │
            │             BSS (12KB)               │
            │                                      │
            ├──────────────────────────────────────┤0x43c3e000
            │                                      │
            │                                      │
            │           EMPTY (4.5KB)              │
            │        (Reserved for ROM)            │
            │                                      │
            ├──────────────────────────────────────┤0x43c3f1e0
            │                                      │
            │       ROM Boot parameter table       │
            │    + Extended boot info (3.5 KB)     │
            │                                      │
            └──────────────────────────────────────┘0x43c3ffff

    .. ifconfig:: CONFIG_part_variant in ('J722S')

        .. code-block:: console

            ┌──────────────────────────────────────┐0x43c00000
            │                                      │
            │                                      │
            │               SPL IMAGE              │
            │            (excluding BSS)           │
            │            (0x6ce00 B  Max)          │
            │                                      │
            ├──────────────────────────────────────┤0x43C6CE00
            │              EMPTY (0x50 B)          │
            │                                      │
            ├──────────────────────────────────────┤0x43C6CE50
            │                                      │
            │                                      │
            │          STACK (0x5000 B Max)        │
            │                                      │
            │                                      │
            ├──────────────────────────────────────┤0x43C71E50
            │       Global Data (0x1AC B Max)      │
            │                 (+0x4)               │
            │                                      │
            ├──────────────────────────────────────┤0x43C72000
            │                                      │
            │            HEAP (0x9000 B Max)       │
            |                                      |
            ├──────────────────────────────────────┤0x43C7B000
            │                                      │
            │            SPL BSS (0x3000 B)        │
            │                                      │
            ├──────────────────────────────────────┤0x43C7E000
            │                                      │
            │       ROM Boot parameter table       │
            │    + Extended boot info (3.5 KB)     │
            │                                      │
            └──────────────────────────────────────┘0x43C7F290


    .. ifconfig:: CONFIG_part_variant in ('AM62LX')

        .. code-block:: text

           ┌────────────────────┐ 0x7081_8000         ┬
           │   Debug Buffers    │                     │
           ├────────────────────┤ 0x7081_6000         │
           │  TIFS ->  A53 IPC  │                     │
           ├────────────────────┤ 0x7081_5000         │
           │  A53  -> TIFS IPC  │                     │
           ├────────────────────┤ 0x7081_4000         │
           │                    │                     │
           │    *Free Space*    │                     │
           │                    │                     │
           ├────────────────────┤ 0x7081_0000  ┬      │
           │ Translation Table  │              │      │
           ├────────────────────┤ 0x7080_D000  │      │
           │        BSS         │              │      │  MSRAM (96k)
           ├────────────────────┤ 0x7080_B9C0  │      │
           │       Stack        │              │      │
           ├────────────────────┤ 0x7080_B1C0  │ BL-1 │
           │        Data        │              │      │
           ├────────────────────┤ 0x7080_B000  │      │
           │      RO-Data       │              │      │
           ├────────────────────┤ 0x7080_6000  │      │
           │        Code        │              │      │
           ├────────────────────┤ 0x7080_0000  ┘     ─┤
           │                    │                     │
           │      ROM Data      │                     │ PSRAM (64k)
           │                    │                     │
           └────────────────────┘ 0x707F_0000         ┴
