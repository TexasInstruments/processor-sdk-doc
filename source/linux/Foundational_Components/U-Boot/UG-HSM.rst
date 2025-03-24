###############
HSM M4F Loading
###############

Some K3 SoCs like J721S2 and J784S4 have a High Security Module (HSM) M4F
core in the Wakeup Voltage Domain. The HSM M4 core is loaded at R5 SPL stage.
Boot flow for HSM M4 core is different than the general purpose M4F cores,
and is described as below:

  - Request control of HSM M4F remote processor.
  - Assert Reset on the HSM M4F remote processor.
  - Load firmware into HSM M4F core's SRAM memory region.
     - For HS devices, request TIFS to authenticate and load the firmware.
     - For GP devices, load the firmware manually into HSM SRAM.
  - Deassert Reset on the HSM M4F remote processor.
  - Release control of HSM M4F remote processor.

This User Guide documents how to enable HSM core loading.

*****************************
How to enable HSM M4F Loading
*****************************

By default, only the HSM demo firmware for HS-SE device type is packed in
tispl.bin FIT image. See :ref:`how-to-build-u-boot-with-custom-hsm-fw`
section to change the default firmware for other device types.

R5 SPL supports loading of HSM M4 core for all device types, i.e., HS-SE,
HS-FS, GP. However, This feature is disabled by default in SDK. To enable
HSM loading, set the :code:`CONFIG_K3_HSM_FW` config in both
<soc>_evm_r5_defconfig and <soc>_evm_a72_defconfig files.

For example, to enable HSM loading on J721S2 device, make the following
changes:

.. code-block:: diff

   diff --git a/configs/j721s2_evm_r5_defconfig b/configs/j721s2_evm_r5_defconfig
   index 806c97792f6..ebe100c2278 100644
   --- a/configs/j721s2_evm_r5_defconfig
   +++ b/configs/j721s2_evm_r5_defconfig
   @@ -187,3 +187,4 @@ CONFIG_FS_FAT_MAX_CLUSTSIZE=16384
    CONFIG_PANIC_HANG=y
    CONFIG_LIB_RATIONAL=y
    CONFIG_SPL_LIB_RATIONAL=y
   +CONFIG_K3_HSM_FW=y
   diff --git a/configs/j721s2_evm_a72_defconfig b/configs/j721s2_evm_a72_defconfig
   index 6db41cb457e..a07e6d63270 100644
   --- a/configs/j721s2_evm_a72_defconfig
   +++ b/configs/j721s2_evm_a72_defconfig
   @@ -198,3 +198,4 @@ CONFIG_UFS=y
    CONFIG_CADENCE_UFS=y
    CONFIG_TI_J721E_UFS=y
    CONFIG_TI_COMMON_CMD_OPTIONS=y
   +CONFIG_K3_HSM_FW=y

Proceed to build U-Boot (tiboot3.bin and tispl.bin). One can verify if the
HSM binary is packed inside tispl.bin FIT image by using following command:

.. code-block:: console

   mkimage -l <output directory>/a72/tispl.bin
   <...>
   Image 2 (hsm)
    Description:  HSM binary
    Created:      Thu Mar 20 13:26:16 2025
    Type:         Standalone Program
    Compression:  uncompressed
    Data Size:    132694 Bytes = 129.58 KiB = 0.13 MiB
    Architecture: Unknown Architecture
    Load Address: 0x82000000
    Entry point:  0x82000000
   <...>

The HSM core loading can be verified by checking for the following log
at R5 SPL stage: `'Successfully booted HSM core'`.

.. code-block:: console

   U-Boot SPL 2025.01-00391-ga7a25e886202-dirty (Mar 20 2025 - 11:04:05 +0530)
   SYSFW ABI: 4.0 (firmware rev 0x000b '11.0.9--v11.00.09+ (Fancy Rat)')
   Initialized 4 DRAM controllers
   SPL initial stack usage: 13456 bytes
   Trying to boot from MMC2
   Authentication passed
   Authentication passed
   Authentication passed
   Loading Environment from nowhere... OK
   Successfully booted HSM core
   Authentication passed
   Authentication passed
   Starting ATF on ARM64 core...

.. _how-to-build-u-boot-with-custom-hsm-fw:

********************************************
How to build U-Boot with custom HSM firmware
********************************************

To pack the firmware for any other device type, one can update the path in
the SoC binman template to point to the custom binary and re-build U-Boot
images (tispl.bin).

:code:`arch/arm/dts/k3-<soc>-binman.dtsi`

.. code-block:: dts

   hsm {
      hsm: blob-ext {
         filename = <path_to_custom_binary>;
      };
   };

For example, To pack the HSM demo firmware for J784S4 HS-FS device type, make
following changes to :code:`arch/arm/dts/k3-j784s4-binman.dtsi`

.. code-block:: dts

   hsm {
      hsm: blob-ext {
         filename = "ti-hsm/hsm-demo-firmware-j784s4-hs-fs.bin";
      };
   };

A list of all HSM demo firmwares can be found in `ti-linux-firmware repository
<https://git.ti.com/cgit/processor-firmware/ti-linux-firmware/tree/ti-hsm?h=ti-linux-firmware>`__.
