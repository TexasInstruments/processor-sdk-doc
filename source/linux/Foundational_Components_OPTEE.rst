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

  .. parsed-literal::

     $ make CROSS_COMPILE="$CROSS_COMPILE_32" CROSS_COMPILE64="$CROSS_COMPILE_64" PLATFORM=|__OPTEE_PLATFORM_FLAVOR__| CFG_ARM64_core=y

Building the OP-TEE image with debug parameters
***********************************************

  .. parsed-literal::

     $ make CROSS_COMPILE="$CROSS_COMPILE_32" CROSS_COMPILE64="$CROSS_COMPILE_64" PLATFORM=|__OPTEE_PLATFORM_FLAVOR__| CFG_ARM64_core=y CFG_TEE_CORE_LOG_LEVEL=2 CFG_TEE_CORE_DEBUG=y

.. _building-optee-with-prng:

Building OP-TEE with Pseudo RNG drivers
***************************************

In certain highly specific use-cases the true RNG drivers could have a
detrimental effect to the overall system latency. Using the
``CFG_WITH_SOFTWARE_PRNG`` flag to use OP-TEE's Pseudo RNG drivers as a source
of entropy can work around these issues.

.. parsed-literal::

   $ make CROSS_COMPILE="$CROSS_COMPILE_32" CROSS_COMPILE64="$CROSS_COMPILE_64" PLATFORM=k3-|__OPTEE_PLATFORM_FLAVOR__| CFG_ARM64_core=y CFG_WITH_SOFTWARE_PRNG=y


Secure Storage with RPMB (For HS)
*********************************

OP-TEE provides secure storage functionality. TI SoCs with HS configuration have a
KEK embedded in them that is programmed across OP-TEE instances that are distributed
in a derived manner. Each HS device has its own HUK signing key (DKEK) which is different
from other HS devices.

For enabling RPMB support along with secure storage, additional flags need to be passed to
the build instructions. The information for the flags can be found here.
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

Getting OP-TEE Client source code
---------------------------------

.. code-block:: console

  $ git clone https://github.com/OP-TEE/optee_client

.. rubric:: Building OP-TEE Client with RPMB support

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
