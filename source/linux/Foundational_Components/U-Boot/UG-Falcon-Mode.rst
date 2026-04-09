.. _U-Boot-Falcon-Mode:

##################
U-Boot Falcon Mode
##################

U-Boot's falcon mode on |__PART_FAMILY_DEVICE_NAMES__| bypasses the A-core SPL
and U-Boot stage, which allows for booting straight to Linux kernel after OP-TEE
and ATF.

**Normal boot flow:**

* R5 SPL -> ATF -> OP-TEE -> *Cortex-A SPL* -> *U-Boot* -> Linux

**With falcon mode:**

* R5 SPL -> ATF -> OP-TEE -> Linux

The following steps show how to build R5 SPL with falcon mode support:

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   * `Falcon Mode - U-Boot documentaiton <https://docs.u-boot.org/en/v2026.01/board/ti/am62ax_sk.html#falcon-mode>`__

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   * `Falcon Mode - U-Boot documentaiton <https://docs.u-boot.org/en/v2026.01/board/ti/am62px_sk.html#falcon-mode>`__

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   * `Falcon Mode - U-Boot documentaiton <https://docs.u-boot.org/en/v2026.01/board/ti/am62x_sk.html#falcon-mode>`__

.. important::

   The following patch is required to enable R5 falcon mode in U-Boot for
   ``12.0`` SDK release:

   .. code-block:: diff

      diff --git a/arch/arm/mach-k3/common.c b/arch/arm/mach-k3/common.c
      index b93516ff806..b5ced6e713b 100644
      --- a/arch/arm/mach-k3/common.c
      +++ b/arch/arm/mach-k3/common.c
      @@ -54,7 +54,7 @@ struct ti_sci_handle *get_ti_sci_handle(void)
       	return (struct ti_sci_handle *)ti_sci_get_handle_from_sysfw(dev);
       }

      -#ifdef CONFIG_SPL_OS_BOOT
      +#if IS_ENABLED(CONFIG_SPL_OS_BOOT) && IS_ENABLED(CONFIG_ARM64)
       void *board_spl_fit_buffer_addr(ulong fit_size, int sectors, int bl_len)
       {
       	return (void *)CONFIG_SPL_LOAD_FIT_ADDRESS;

   * `Patch in ti-u-boot tree <https://git.ti.com/cgit/ti-u-boot/ti-u-boot/commit/?h=ti-u-boot-2026.01-next&id=ee3048ee0822c35312379b6e24b5c80e9a845110>`__

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

**********************
Boot time comparisons:
**********************

Removing A-core SPL and U-Boot from the boot process leads to ~60% reduction in
time to kernel. Saving about 1-2 seconds during boot depending on the platform.

.. figure:: /images/U-Boot_Falcon_Comparison.gif
   :alt: falcon mode and regular boot mode comparison
   :align: center

   Falcon Mode (Left) vs Regular Boot (Right)
