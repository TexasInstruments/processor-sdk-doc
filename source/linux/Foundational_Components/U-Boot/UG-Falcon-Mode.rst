.. _U-Boot-Falcon-Mode:

##################
U-Boot Falcon Mode
##################

U-Boot's falcon mode on |__PART_FAMILY_NAME__| bypasses the A-core SPL
and U-Boot stage, which allows for booting straight to Linux kernel after OP-TEE
and ATF.

**Normal boot flow:**

* R5 SPL -> ATF -> OP-TEE -> *Cortex-A SPL* -> *U-Boot* -> Linux

**With falcon mode:**

* R5 SPL -> ATF -> OP-TEE -> Linux

Falcon boot support is added by the ``ti-falcon`` yocto override which can be
enabled before :ref:`building the SDK <building-the-sdk-with-yocto>` as follows:

.. code-block:: console

   $ echo 'DISTROOVERRIDES:append = ":ti-falcon"' >> conf/local.conf
   $ # build the SDK
   $ MACHINE=<machine> bitbake -k tisdk-default-image

*************************************
Changes made by *ti-falcon* override:
*************************************

ATF:
====

To meet the 2MiB alignment requirement for the Linux kernel's load address,
the ``PRELOADED_BL33_BASE`` *(kernel address)* is modified to ``0x82000000``
and ``K3_HW_CONFIG_BASE`` *(DTB address)* is modified from the K3 default to
``0x88000000``.

TI-SPL:
=======

Falcon mode makes use of a cut down variant of the tispl binary called
:file:`tifalcon.bin` with the Cortex-A SPL and its corresponding device-tree
removed. This file is deployed to the boot directory inside the root filesystem
so it can be picked by the R5 SPL at boot time.

R5 SPL:
=======

The R5 SPL loads the kernel :file:`fitImage` and :file:`tifalcon.bin` file. An
x509 certificate with TIFS keys verifies the :file:`fitImage` for falcon boot
instead of making use of signature nodes and keys present in the DT. This allows
for faster authentication since TIFS uses the security accelerator for
authentication, which is much faster than doing the same on R5 core.

This support is present alongside the standard R5 ``defconfig`` when ``ti-falcon``
is enabled due to U-Boot's :file:`k3_r5_falcon.config` fragment. This updates
the R5 memory map at U-Boot SPL stage to the following:

.. code-block::

   0x80000000 +===============================+ Start of DDR
     512KiB   |   ATF reserved memory space   | CONFIG_K3_ATF_LOAD_ADDR
   0x80080000 +-------------------------------+
    31.5MiB   |            Unused             |
   0x82000000 +-------------------------------+ PRELOADED_BL33_BASE in ATF
              |                               | CONFIG_SYS_LOAD_ADDR
      57MiB   |   Kernel + initramfs Image    | CONFIG_SPL_LOAD_FIT_ADDRESS
              |                               |
   0x85900000 +-------------------------------+
              |                               |
              |  R5 U-Boot SPL Stack + Heap   |
      39MiB   |       (size defined by        |
              | SPL_STACK_R_MALLOC_SIMPLE_LEN)|
              |                               |
   0x88000000 +-------------------------------+ CONFIG_SPL_STACK_R_ADDR
              |                               | K3_HW_CONFIG_BASE in ATF
      16MiB   |          Kernel DTB           | CONFIG_SPL_PAYLOAD_ARGS_ADDR
              |                               |
   0x89000000 +-------------------------------+
     331MiB   | Device Manager (DM) Load Addr |
   0x9db00000 +-------------------------------+
      12MiB   |          DM Reserved          |
   0x9e700000 +-------------------------------+
       1MiB   |            Unused             |
   0x9e800000 +-------------------------------+ BL32_BASE in ATF
      24MiB   |             OPTEE             |
   0xa0000000 +===============================+ End of DDR (512MiB)

fitImage:
=========

The system produces the resulting :file:`fitImage` file in the boot directory
of the root filesystem. This file has its constituent binaries pre-signed with
x509 certificates. At boot time, TIFS authenticates this file, which allows for
a lower boot time compared to authenticating on the R5 core.

*******************
Extra Configuration
*******************

OSPI boot:
==========

.. ifconfig:: CONFIG_part_variant not in ('AM62AX')

   For OSPI boot, the :file:`tiboot3.bin` file should be flashed to the same
   addresses in flash as regular boot flow whereas :file:`tifalcon.bin` and the
   :file:`fitImage` are read from the root filesystem's boot directory. The MMC
   device is selected by the ``mmcdev`` env variable for R5 SPL.

   Below U-Boot commands can be used to download :file:`tiboot3.bin` over tftp
   and then flash it to OSPI.

   .. code-block:: console

     => sf probe
     => tftp ${loadaddr} tiboot3.bin
     => sf update $loadaddr 0x0 $filesize

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   This section is not applicable for this platform.

eMMC Boot:
==========

In eMMC boot mode, the :file:`tiboot3.bin` file should be flashed to the
hardware boot partition whereas :file:`tifalcon.bin` and the :file:`fitImage`
are read from the root filesystem inside UDA. Use the U-Boot commands below
to set the correct boot partition and write :file:`tiboot3.bin` to the correct
offset.

.. code-block:: console

   => # Set boot0 as the boot partition
   => mmc partconf 0 1 1 1
   => mmc bootbus 0 2 0 0
   => # Flash tiboot3.bin to boot0
   => mmc dev 0 1
   => fatload mmc 1 ${loadaddr} tiboot3.bin
   => mmc write ${loadaddr} 0x0 0x400

For more information check: :ref:`How to flash eMMC and boot with eMMC Boot
<how-to-emmc-boot>`.

.. _u-boot_falcon_mode_fitImage_creation:

Custom fitImage creation:
=========================

The following steps show how to create a falcon compatible :file:`fitImage`:

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   * `fitImage Creation - U-Boot documentaiton <https://docs.u-boot.org/en/latest/board/ti/am62ax_sk.html#fitimage>`__

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   * `fitImage Creation - U-Boot documentaiton <https://docs.u-boot.org/en/latest/board/ti/am62px_sk.html#fitimage>`__

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   * `fitImage Creation - U-Boot documentaiton <https://docs.u-boot.org/en/latest/board/ti/am62x_sk.html#fitimage>`__

Non-Yocto Users:
================

The following steps show how to enable falcon mode from the R5 SPL standalone:

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   * `Falcon Mode - U-Boot documentaiton <https://docs.u-boot.org/en/latest/board/ti/am62ax_sk.html#falcon-mode>`__

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   * `Falcon Mode - U-Boot documentaiton <https://docs.u-boot.org/en/latest/board/ti/am62px_sk.html#falcon-mode>`__

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   * `Falcon Mode - U-Boot documentaiton <https://docs.u-boot.org/en/latest/board/ti/am62x_sk.html#falcon-mode>`__

**********************
Boot time comparisons:
**********************

Removing A-core SPL and U-Boot from the boot process leads to ~60% reduction in
time to kernel. Saving about 1-2 seconds during boot depending on the platform.

.. figure:: /images/U-Boot_Falcon_Comparison.gif
   :alt: falcon mode and regular boot mode comparison
   :align: center

   Falcon Mode (Left) vs Regular Boot (Right)
