.. _foundational-components-optee:

OP-TEE
======

OP-TEE is a Trusted Execution Environment (TEE) designed as a companion to a
non-secure Linux kernel running on Arm Cortex-A cores using the TrustZone technology.

#. Furthur information about it can be found at: https://optee.readthedocs.io/en/latest/general/about.html
#. Official OP-TEE documentation: https://optee.readthedocs.io/en/latest
#. OP-TEE advisory listing: https://github.com/OP-TEE/optee_os/security/advisories

The OP-TEE binary (bl32.bin/tee-pager_v2.bin) is bundled into tispl.bin and the following are the instructions to build:

|

Getting the OP-TEE Source Code
------------------------------

The pre-built OPTEE binary should be packaged in TI Processor SDK: <path-to-processor-sdk>/board-support/prebuilt-images/<optional-build-machine-name>/bl32.bin.
Use this binary since it has been tested with TI Processor SDK.

If it is not possible to use pre-build binary, use the following:

.. code-block:: console

   $ git clone https://github.com/OP-TEE/optee_os.git
   $ git checkout <hash>

Where <hash> is the OPTEE commit shown in :ref:`release-specific-build-information`.

|

Setting up the toolchain paths
------------------------------

.. include:: Overview/GCC_ToolChain.rst
   :start-after: .. start_include_yocto_toolchain_host_setup
   :end-before: .. end_include_yocto_toolchain_host_setup

Building OP-TEE OS
------------------

.. ifconfig:: CONFIG_part_variant in ('J721S2', 'J784S4','J742S2')

   .. code-block:: console

      $ export CFG_CONSOLE_UART=0x8

Building the OP-TEE image
*************************

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   .. parsed-literal::

      $ make CROSS_COMPILE="$CROSS_COMPILE_32" CROSS_COMPILE64="$CROSS_COMPILE_64" PLATFORM=|__OPTEE_PLATFORM_FLAVOR__| CFG_ARM64_core=y

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. parsed-literal::

      $ make CROSS_COMPILE64="$CROSS_COMPILE_64" PLATFORM=|__OPTEE_PLATFORM_FLAVOR__| CFG_ARM64_core=y CFG_USER_TA_TARGETS=ta_arm64

Building the OP-TEE image with debug parameters
***********************************************

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   .. parsed-literal::

      $ make CROSS_COMPILE="$CROSS_COMPILE_32" CROSS_COMPILE64="$CROSS_COMPILE_64" PLATFORM=|__OPTEE_PLATFORM_FLAVOR__| CFG_ARM64_core=y CFG_TEE_CORE_LOG_LEVEL=2 CFG_TEE_CORE_DEBUG=y

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. parsed-literal::

      $ make CROSS_COMPILE64="$CROSS_COMPILE_64" PLATFORM=|__OPTEE_PLATFORM_FLAVOR__| CFG_ARM64_core=y CFG_TEE_CORE_LOG_LEVEL=2 CFG_TEE_CORE_DEBUG=y CFG_USER_TA_TARGETS=ta_arm64

.. _building-optee-with-prng:

Building OP-TEE with Pseudo RNG drivers
***************************************

In certain highly specific use-cases the true RNG drivers could have a
detrimental effect to the overall system latency. Using the
``CFG_WITH_SOFTWARE_PRNG`` flag to use OP-TEE's Pseudo RNG drivers as a source
of entropy can work around these issues.

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   .. parsed-literal::

      $ make CROSS_COMPILE="$CROSS_COMPILE_32" CROSS_COMPILE64="$CROSS_COMPILE_64" PLATFORM=k3-|__OPTEE_PLATFORM_FLAVOR__| CFG_ARM64_core=y CFG_WITH_SOFTWARE_PRNG=y

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. parsed-literal::

      $ make CROSS_COMPILE64="$CROSS_COMPILE_64" PLATFORM=k3-|__OPTEE_PLATFORM_FLAVOR__| CFG_ARM64_core=y CFG_WITH_SOFTWARE_PRNG=y CFG_USER_TA_TARGETS=ta_arm64

.. _secure-storage-with-rpmb:

OP-TEE Secure Storage
*********************

OP-TEE provides secure storage functionality through two mechanisms:
**REE FS** (Rich Execution Environment Filesystem) and **RPMB**
(Replay Protected Memory Block).

TI SDK enables REE FS by-default, and configures OP-TEE to store
encrypted binary blobs created by REE FS in
:file:`/var/lib/tee/`.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   .. note::

      Presently, AM62L does not support RPMB. This support will be added
      in subsequent releases. It does support REE FS.

      The remaining devices support both: REE FS by-default and RPMB if
      OP-TEE binaries are re-compiled with required flags.

   For learning more about secure storage in OP-TEE, refer:
   https://optee.readthedocs.io/en/latest/architecture/secure_storage.html

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   RPMB works in TI SoCs with HS configuration. These embed a KEK
   that programs across OP-TEE instances in a derived manner. Each HS
   device has its own HUK signing key (DKEK), which is different from
   other HS devices. TI SDK disables RPMB by-default. To enable it,
   re-compiling OP-TEE with ``CFG_RPMB_FS=y`` flag.

   For learning more about secure storage in OP-TEE, and instructions to
   enable RPMB, refer:
   https://optee.readthedocs.io/en/latest/architecture/secure_storage.html

   There is a hybrid mode in which both the flags i.e `CFG_REE_FS=y` and `CFG_RPMB_FS=y` are enabled.
   This mode stores the state of the Secure Storage directory in RPMB partition to check for the
   integrity of the data present in it. It is the recommended way.

   E.g. For enabling hybrid mode of RPMB along with REE_FS

   .. ifconfig:: CONFIG_part_variant in ('J721S2')

      .. code-block:: console

          $ export CFG_CONSOLE_UART=0x8

   .. parsed-literal::

      $ make CROSS_COMPILE64="$CROSS_COMPILE_64" PLATFORM=|__OPTEE_PLATFORM_FLAVOR__| CFG_ARM64_core=y CFG_REE_FS=y CFG_RPMB_FS=y

   OPTEE-client also needs to be updated to enable the use of real
   emmc instead of the virtual emmc that is enabled by default

As an example to show the usage of secure storage, the filesystem
provides a binary :file:`/usr/bin/optee_examples_secure_storage`.

.. code::

   optee_examples_secure_storage

For more details, see optee_examples:
https://github.com/linaro-swg/optee_examples

Getting OP-TEE Client source code
---------------------------------

To get optee_client source code, do:

.. rubric:: Getting OP-TEE Client source code

.. code-block:: console

   $ git clone https://github.com/OP-TEE/optee_client

.. rubric:: Building OP-TEE Client with RPMB support

To use emulated RPMB, set RPMB_EMU=1. Otherwise, set RPMB_EMU=0.

For example, the following command builds optee_client to use the real RPMB,
instead of the emulated one.

.. code-block:: console

   $ make CROSS_COMPILE="$CROSS_COMPILE_64" PLATFORM=k3 CFG_TEE_SUPP_LOG_LEVEL=2 RPMB_EMU=0 CFG_ARM64_core=y

Now update optee-client binary and libraries on your SD card with the generated ones
in `out/export/usr` folder

|

Building u-boot with OP-TEE OS
------------------------------

As of Processor SDK 9.0, the signing functionality earlier provided by the TI Security Development Package, has
been integrated within U-Boot itself. This means tee-pager_v2.bin does not need to be signed before being packaged
in tispl.bin in U-Boot for HS devices.

Expected binary output

    #. Generated binary: tee-pager_v2.bin
    #. Binary saved saved in: <path-to-optee>/out/arm-plat-k3/core

Integrate binary output into U-boot

    #. Go to u-boot folder <path-to-u-boot>
    #. Re-build U-boot with A72/A53 instructions found under: :ref:`Build-U-Boot-label`, but with the TEE parameter pointing to the newly built tee-pager_v2.bin. i.e. TEE=<path-to-optee>/out/arm-plat-k3/core/tee-pager_v2.bin

.. note::

   tee-pager_v2.bin may be called bl32.bin in other documentation.

|

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

   .. rubric:: PKCS#11

   PKCS#11 is a cryptographic token interface standard that allows applications
   to access cryptographic services through a platform-independent API.

   For userland integration details, refer:
   https://optee.readthedocs.io/en/latest/building/userland_integration.html
