.. _foundational-components-atf:

ARM Trusted Firmware-A
======================
.. rubric:: Overview

Trusted Firmware-A (TF-A) provides a reference implementation of secure world
software for Armv7-A and Armv8-A, including a Secure Monitor executing at
Exception Level 3 (EL3).

Arm Trusted Firmware (ATF) is the initial code on ARMv8-A cores for all K3 platforms.
After setting up the initial core state and applying any needed errata fixes
it sets up itself as the EL3 monitor handler. Following that, it installs the secure
world open source Trusted Execution Environment (OP-TEE) software and passes execution
on to either the Linux kernel or U-Boot in the non-secure world.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. rubric:: Power and Clock Management using SCMI

   The AM62Lx System-on-Chip (SoC) utilizes the System Control and Management Interface
   (SCMI) protocol to manage clocks and power domains. SCMI is a standardized interface for
   system control and management, providing a common way to access and control system resources.
   The SCMI IDs used in the AM62L TF-A implementation are documented in the
   `TF-A documentation <https://github.com/TexasInstruments/arm-trusted-firmware/blob/ti-master/docs/plat/ti-am62l.rst>`__.

|

.. rubric:: Getting the ATF Source Code

The pre-built TF-A binary is in TI Processor SDK: 
<path-to-processor-sdk>/board-support/prebuilt-images/<optional-build-machine-name>/bl31.bin.
Use this binary since it is tested with TI Processor SDK.

If it is not possible to use pre-build binary, use the following:

.. code-block:: console

   $ git clone https://github.com/TexasInstruments/arm-trusted-firmware.git
   $ git checkout <hash>

Where <hash> is the commit shown here: :ref:`tf-a-release-notes` :ref:`release-specific-build-information`.

|

.. rubric:: Setting up the toolchain paths

.. include:: Overview/GCC_ToolChain.rst
   :start-after: .. start_include_yocto_toolchain_host_setup
   :end-before: .. end_include_yocto_toolchain_host_setup

.. rubric:: Building ATF

.. ifconfig:: CONFIG_part_variant in ('AM62LX', 'AM62X', 'AM62AX', 'AM62PX', 'AM64X', 'J722S')

    .. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX', 'AM64X', 'J722S')

            .. code-block:: console

               $ export TFA_DIR=<path-to-arm-trusted-firmware>
               $ cd $TFA_DIR
               $ make ARCH=aarch64 CROSS_COMPILE="$CROSS_COMPILE_64" PLAT=k3 TARGET_BOARD=lite SPD=opteed

    .. ifconfig:: CONFIG_part_variant in ('AM62LX')

        *Without OP-TEE enabled:*

            .. code-block:: console

               $ export TFA_DIR=<path-to-arm-trusted-firmware>
               $ cd $TFA_DIR
               $ make ARCH=aarch64 CROSS_COMPILE="$CROSS_COMPILE_64" PLAT=k3 TARGET_BOARD=am62l

.. ifconfig:: CONFIG_part_variant in ('J721S2')

    .. code-block:: console

       $ make CROSS_COMPILE="$CROSS_COMPILE_64" ARCH=aarch64 PLAT=k3 TARGET_BOARD=generic SPD=opteed K3_USART=0x8

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

    .. code-block:: console

        $ make CROSS_COMPILE="$CROSS_COMPILE_64" ARCH=aarch64 PLAT=k3 TARGET_BOARD=j784s4 SPD=opteed K3_USART=0x8

.. ifconfig:: CONFIG_part_variant not in ('AM64X', 'AM62X', 'AM62LX', 'AM62AX', 'AM62PX', 'J721S2', 'J784S4', 'J742S2', 'J722S')

    .. code-block:: console

       $ make CROSS_COMPILE="$CROSS_COMPILE_64" PLAT=k3 TARGET_BOARD=generic SPD=opteed

|

.. rubric:: Default load locations

.. ifconfig:: CONFIG_part_family in ('AM64X_family')

    .. code-block:: text

       +---------------------------+------------+
       | ATF image                 | 0x701c0000 |
       +---------------------------+------------+
       | OP-TEE image              | 0x9e800000 |
       +---------------------------+------------+
       | U-Boot/Linux kernel image | 0x80080000 |
       +---------------------------+------------+
       | DTB                       | 0x82000000 |
       +---------------------------+------------+

.. ifconfig:: CONFIG_part_family in ('AM62LX_family')

    .. code-block:: text

       +---------------------------+------------+
       | ATF image                 | 0x80000000 |
       +---------------------------+------------+
       | OP-TEE image              | 0x80200000 |
       +---------------------------+------------+
       | U-Boot/Linux kernel image | 0x80080000 |
       +---------------------------+------------+
       | DTB                       | 0x82000000 |
       +---------------------------+------------+

.. ifconfig:: CONFIG_part_family not in ('AM64X_family', 'AM62LX_family')

    .. code-block:: text

       +---------------------------+------------+
       | ATF image                 | 0x70000000 |
       +---------------------------+------------+
       | OP-TEE image              | 0x9e800000 |
       +---------------------------+------------+
       | U-Boot/Linux kernel image | 0x80080000 |
       +---------------------------+------------+
       | DTB                       | 0x82000000 |
       +---------------------------+------------+

.. ifconfig:: CONFIG_part_variant in ('AM64X', 'AM62X', 'AM62AX', 'AM62PX', 'J722S')

    To change the default load address of these binaries, an address has to be changed in several source trees. The following
    is an example for AM64x family devices. Other family devices might not at the moment have binman dtsi files associated with
    them but they could in the future.

    .. code-block:: text

       +-----------------------------------------------------+------------------+-----------------------+---------------------+---------------+-------------------+----------+----------------------------------------+
       | Source                                              | ATF              | OPTEE                 |  A53 SPL            | A53 U-Boot    | DTB               | kernel   | Comments                               |
       +=====================================================+==================+=======================+=====================+===============+===================+==========+========================================+
       | <atf>/plat/ti/k3/board/lite/board.mk                |                  | BL32_BASE             | PRELOADED_BL33_BASE |               | K3_HW_CONFIG_BASE |          | Change K3_HW_CONFIG_BASE for           |
       |                                                     |                  |                       |                     |               |                   |          | u-boot a53 skip case                   |
       +-----------------------------------------------------+------------------+-----------------------+---------------------+---------------+-------------------+----------+----------------------------------------+
       | <optee>/core/arch/arm/plat-k3/conf.mk               |                  | CFG_TZDRAM_START      |                     |               |                   |          |                                        |
       +-----------------------------------------------------+------------------+-----------------------+---------------------+---------------+-------------------+----------+----------------------------------------+
       | <uboot>/configs/am64x_evm_r5_defconfig              | K3_ATF_LOAD_ADDR |                       |                     |               |                   |          |                                        |
       +-----------------------------------------------------+------------------+-----------------------+---------------------+---------------+-------------------+----------+----------------------------------------+
       | <uboot>/configs/am64x_evm_a53_defconfig             |                  |                       | SPL_TEXT_BASE       | SYS_TEXT_BASE |                   |          | SYS_TEXT_BASE can be set in defconfig, |
       |                                                     |                  |                       |                     |               |                   |          | has default value in Kconfig           |
       +-----------------------------------------------------+------------------+-----------------------+---------------------+---------------+-------------------+----------+----------------------------------------+
       | <uboot/linux>/arch/arm/dts/k3-am642*.dts files      |                  | reserved-memory nodes |                     |               |                   |          |                                        |
       +-----------------------------------------------------+------------------+-----------------------+---------------------+---------------+-------------------+----------+----------------------------------------+
       | <uboot>/arch/arm/dts/k3-am642-evm-binman.dtsi file  |                  | tee nodes             | uboot nodes         | uboot nodes   |                   |          |                                        |
       +-----------------------------------------------------+------------------+-----------------------+---------------------+---------------+-------------------+----------+----------------------------------------+
       | <uboot>/include/configs/ti_armv7_common.h           |                  |                       |                     |               | fdtaddr           | loadaddr | If not defined here, u-boot            |
       |                                                     |                  |                       |                     |               |                   |          | will pick any adress                   |
       +-----------------------------------------------------+------------------+-----------------------+---------------------+---------------+-------------------+----------+----------------------------------------+
       | uEnv.txt                                            |                  |                       |                     |               | fdtaddr           | loadaddr | Overwrite the u-boot environment       |
       |                                                     |                  |                       |                     |               |                   |          | variables                              |
       +-----------------------------------------------------+------------------+-----------------------+---------------------+---------------+-------------------+----------+----------------------------------------+
