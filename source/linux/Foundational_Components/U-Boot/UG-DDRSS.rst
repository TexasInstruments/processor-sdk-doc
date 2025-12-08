###
DDR
###

********
Overview
********

The DDR subsystem (DDRSS) comprises DDR controller, DDR PHY and wrapper logic to
integrate these blocks in the device. The K3 DDRSS driver
(:file:`drivers/ram/k3-ddrss/k3-ddrss.c`) runs during the R5 SPL stage and is
responsible for initializing and configuring the DDR subsystem.

******************
DDR Initialization
******************

The driver utilizes an auto-generated configuration file containing the
necessary settings for the DDR. It configures the frequency, timing parameters,
training algorithms etc. for DDR initialization. The configuration DTSI can be
generated using the `Sysconfig tool <https://dev.ti.com/sysconfig>`_ and
selecting the software product as "DDR Configuration for \*" as well as the
required device.

**************************
Error Correction Code (ECC)
**************************

For SDRAM data integrity, the DDRSS bridge supports inline ECC on the data
written to or read from the SDRAM. ECC is stored together with the data so that
a dedicated SDRAM device for ECC is not required. The 8-bit single error
correction double error detection (SECDED) ECC data is calculated over 64-bit
data quanta. For every 256-byte data block 32 bytes of ECC is stored inline.
Thus 1/9th of the total SDRAM space is used for ECC storage and the remaining
8/9th of the SDRAM data space are seen as consecutive byte addresses. Even if
there are non-ECC protected regions the previously described 1/9th-8/9th rule
still applies and consecutive byte addresses are seen from system point of view.

|__PART_FAMILY_DEVICE_NAMES__| supports up to 3 ECC protected non-overlapping
memory ranges. The current U-Boot release supports a single region covering the
entire SDRAM space.

ECC is calculated for all accesses that are within the address ranges
protected by it. 1-bit error is correctable by ECC, but multi-bit and
multiple 1-bit errors are not correctable and will be treated as an
uncorrectable error. Any uncorrectable error will cause a bus abort. There are
three ways to handle it:

   1. By default, it is reported as a synchronous data abort to software
   2. Enable ESM pin corresponding to DDRSS ECC uncorrectable error
      ``DDR*SS0_DDRSS_DRAM_ECC_UNCORR_ERR_LVL_0`` which routes an ECC
      uncorrectable error to ESM
   3. Trap it using ``HANDLE_EA_EL3_FIRST_NS`` and with help of a custom
      handler ``plat_ea_handler()`` in trusted-firmware-a report the cause

.. note::

   Options 1 and 2 doesn't report the reason. So, if there is a need to report
   the reason behind uncorrectable error handle it the third way.

ECC Handling
============

.. note::

   The ECC feature of DDRSS is not enabled by default in U-Boot.

Enabling ECC
------------

The ECC feature of DDRSS can be enabled by the following two steps:

   1. Add ``ti,ecc-enable`` boolean property to the ``memorycontroller`` node

      .. code-block:: dts

         // u-boot/arch/arm/dts/k3-*-ddr.dtsi

         &memorycontroller {
            power-domains = <&k3_pds 170 TI_SCI_PD_SHARED>,
                            <&k3_pds 55 TI_SCI_PD_SHARED>;
            clocks = <&k3_clks 170 0>, <&k3_clks 16 4>;
            ti,ecc-enable;
         };

   2. Re-build U-Boot with ``CONFIG_K3_INLINE_ECC`` enabled

      .. code-block:: kconfig

         # u-boot/configs/*_r5_defconfig

         CONFIG_PINCTRL_SINGLE=y
         CONFIG_POWER_DOMAIN=y
         CONFIG_TI_POWER_DOMAIN=y
         CONFIG_K3_INLINE_ECC=y
         CONFIG_K3_SYSTEM_CONTROLLER=y
         CONFIG_REMOTEPROC_TI_K3_ARM64=y
         CONFIG_RESET_TI_SCI=y

Priming with BIST Engine
------------------------

The bootloader has the responsibility to pre-load the ECC protected region with
known data before functional reads and writes are performed. During the ECC
initialization, the R5 SPL fills the entire memory with zeros using the BIST
engine in the DDR controller. The BIST engine method allows priming the entire
region with zeros in much less time.

Simulating ECC error
--------------------

U-Boot command :command:`ddrss` can be used to simulate the ECC error by generating bit
errors in SDRAM data at certain address. The ECC check can be tested by:

   #. Enabling ECC
   #. Shrinking the protected range
   #. Modifying a value
   #. Restoring range to original and
   #. Reading the value will cause the ECC error

The command syntax is

   .. code-block:: text

      => ddrss ecc_err <addr in hex> <bit_err in hex>

The command will read data from ``addr`` and write ``data ^ bit_err`` back to
``addr``.

Single bit error
^^^^^^^^^^^^^^^^

The following example generates a 1-bit error on bit 0 of the data at
address 0x82400000.

   .. code-block:: text

      => ddrss ecc_err 82400000 1
      Testing DDRSS ECC:
         ECC test: Disabling DDR ECC ...
         ECC test: addr 0x82400000, read data 0x0, written data 0x1, err pattern: 0x1, read after write data 0x1
         ECC test: Enabled DDR ECC ...
         ECC test: addr 0x82400000, read data 0x0
         ECC test: DDR ECC 1-bit error
         ECC test: 1-bit ECC err count: 1
         ECC test: 1-bit error in [0x2400000:0x2400008]

Reading from 0x82400000 returns a corrected value, the 1-bit error counter is
incremented, and the offset of the error in the physical memory is reported in
8-byte range.

The following example flips the bit back, which clears the error state.

   .. code-block:: text

      => ddrss ecc_err 82400000 1
      Testing DDR ECC:
         ECC test: Disabling DDR ECC ...
         ECC test: addr 0x82400000, read data 0x1, written data 0x0, err pattern: 0x1, read after write data 0x0
         ECC test: Enabled DDR ECC ...
         ECC test: addr 0x82400000, read data 0x0

Multi bit error and Multiple single bit error
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Synchronous Abort (default)
"""""""""""""""""""""""""""

The following example generates a 2-bit error on bits 0 and 1 of the
data at address 0x82400000.

   .. code-block:: text

      => ddrss ecc_err 82400000 3
      Testing DDR ECC:
         ECC test: Disabling DDR ECC ...
         ECC test: addr 0x82400000, read data 0x0, written data 0x3, err pattern: 0x3, read after write data 0x3
         ECC test: Enabled DDR ECC ...
      "Synchronous Abort" handler, esr 0x96000210
      elr: 0000000080825450 lr : 0000000080825450 (reloc)
      elr: 00000000fff03450 lr : 00000000fff03450
      x0 : 0000000000000000 x1 : 0000000000000000
      x2 : 000000000000000a x3 : 0000000002800000
      x4 : 0000000002800000 x5 : 00000000fde9132f
      x6 : 00000000fffa6762 x7 : 00000000fde91770
      x8 : 00000000fffffff0 x9 : 0000000000000008
      x10: 0000000000000010 x11: 0000000000000002
      x12: 0000000000000002 x13: 00000000fde91948
      x14: 00000000fde91a50 x15: 0000000000000000
      x16: 00000000fff40520 x17: 0000000000000000
      x18: 00000000fde9ddb0 x19: 0000000000000004
      x20: 0000000082400000 x21: 0000000000000000
      x22: 000000000000023f x23: 0000000000000003
      x24: 0000000000000000 x25: 0000000000000000
      x26: 000000000f300134 x27: 000000000000dfff
      x28: 0000000000000000 x29: 00000000fde91770

      Code: 9402415d 90000520 9120c400 940020da (b9400282)
      Resetting CPU ...

      resetting ...

      U-Boot SPL 2024.04-ti-g818c76aed67f (Aug 01 2024 - 19:19:47 +0000)
      SYSFW ABI: 4.0 (firmware rev 0x000a '10.0.8--v10.00.08 (Fiery Fox)')
      ECC is enabled, priming DDR which will take several seconds.
      ECC: priming DDR completed in 1356 msec

The following example generates a 1-bit error on bit 0 of the data at
addresses 0x82400000 and 0x82400008.

   .. code-block:: text

      => ddrss ecc_err 82400000 1
      Testing DDR ECC:
         ECC test: Disabling DDR ECC ...
         ECC test: addr 0x82400000, read data 0x0, written data 0x1, err pattern: 0x1, read after write data 0x1
         ECC test: Enabled DDR ECC ...
         ECC test: addr 0x82400000, read data 0x0
         ECC test: DDR ECC 1-bit error
         ECC test: 1-bit ECC err count: 1
         ECC test: 1-bit error in [0x2400000:0x2400008]
      => ddrss ecc_err 82400008 1
      Testing DDR ECC:
         ECC test: Disabling DDR ECC ...
         ECC test: addr 0x82400008, read data 0x0, written data 0x1, err pattern: 0x1, read after write data 0x1
         ECC test: Enabled DDR ECC ...
      "Synchronous Abort" handler, esr 0x96000210
      elr: 0000000080825450 lr : 0000000080825450 (reloc)
      elr: 00000000fff03450 lr : 00000000fff03450
      x0 : 0000000000000000 x1 : 0000000000000000
      x2 : 000000000000000a x3 : 0000000002800000
      x4 : 0000000002800000 x5 : 00000000fde9132f
      x6 : 00000000fffa6762 x7 : 00000000fde91770
      x8 : 00000000fffffff0 x9 : 0000000000000008
      x10: 0000000000000010 x11: 0000000000000002
      x12: 0000000000000002 x13: 00000000fde91948
      x14: 00000000fde91a50 x15: 0000000000000000
      x16: 00000000fff40520 x17: 0000000000000000
      x18: 00000000fde9ddb0 x19: 0000000000000004
      x20: 0000000082400008 x21: 0000000000000000
      x22: 000000000000023f x23: 0000000000000001
      x24: 0000000000000000 x25: 0000000000000000
      x26: 000000000f300134 x27: 000000000000dfff
      x28: 0000000000000000 x29: 00000000fde91770

      Code: 9402415d 90000520 9120c400 940020da (b9400282)
      Resetting CPU ...

      resetting ...

      U-Boot SPL 2024.04-ti-g818c76aed67f (Aug 01 2024 - 19:19:47 +0000)
      SYSFW ABI: 4.0 (firmware rev 0x000a '10.0.8--v10.00.08 (Fiery Fox)')
      ECC is enabled, priming DDR which will take several seconds.
      ECC: priming DDR completed in 1356 msec

Error Signaling Module (ESM)
""""""""""""""""""""""""""""

The Error Signaling Module (ESM) aggregates events and/or errors from
throughout the device into one location. It can signal both low and
high priority interrupts to a processor to deal with an event and/or
manipulate an I/O error pin to signal an external hardware that an
error has occurred. Therefore an external controller is able to reset
the device or keep the system in a safe, known state.

.. figure:: /images/Uboot_ddrss1.svg
   :width: 800
   :align: center

   DDRSS ESM Overview

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   The ESM pin corresponding to DDRSS ECC uncorrectable error
   ``DDR16SS0_DDRSS_DRAM_ECC_UNCORR_ERR_LVL_0`` is 69. So, enable it
   by adding 69 to the ``ti,esm-pins`` property of ``main_esm`` node.

      .. code-block:: dts

         // u-boot/arch/arm/dts/k3-am642-*.dts

         main_esm: esm@420000 {
            compatible = "ti,j721e-esm";
            reg = <0x0 0x420000 0x0 0x1000>;
            ti,esm-pins = <69>, <160>, <161>;
            bootph-pre-ram;
         };

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   The ESM pin corresponding to DDRSS ECC uncorrectable error
   ``DDR16SS0_DDRSS_DRAM_ECC_UNCORR_ERR_LVL_0`` is 69.
   So, enable it by adding 69 to the ``ti,esm-pins`` property of
   ``main-esm`` node.

      .. code-block:: dts

         // u-boot/arch/arm/dts/k3-am62x-*.dts

         main_esm: esm@420000 {
            compatible = "ti,j721e-esm";
            reg = <0x0 0x420000 0x0 0x1000>;
            ti,esm-pins = <69>, <160>, <161>, <162>, <163>, <177>, <178>;
            bootph-pre-ram;
         };

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

   The ESM pin corresponding to DDRSS ECC uncorrectable error
   ``DDR16SS0_DDRSS_DRAM_ECC_UNCORR_ERR_LVL_0`` is 175.
   So, enable it by adding 175 to the ``ti,esm-pins`` property of
   ``main-esm`` node.

      .. code-block:: dts

         // u-boot/arch/arm/dts/k3-am62a7-*.dts

         main_esm: esm@420000 {
            compatible = "ti,j721e-esm";
            reg = <0x0 0x420000 0x0 0x1000>;
            ti,esm-pins = <160>, <161>, <162>, <163>, <175>, <177>, <178>;
            bootph-pre-ram;
         };

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   The ESM pin corresponding to DDRSS ECC uncorrectable error
   ``DDR32SS0_DDRSS_DRAM_ECC_UNCORR_ERR_LVL_0`` is 175.
   So, enable it by adding 175 to the ``ti,esm-pins`` property of
   ``main-esm`` node.

      .. code-block:: dts

         // u-boot/arch/arm/dts/k3-am62p-*.dts

         main_esm: esm@420000 {
            compatible = "ti,j721e-esm";
            reg = <0x00 0x420000 0x00 0x1000>;
            ti,esm-pins = <160>, <161>, <162>, <163>, <175>, <177>, <178>;
            bootph-pre-ram;
         };

The following example generates a 2-bit error on bits 0 and 1 of the
data at address 0x82400000.

   .. code-block:: text

      => ddrss ecc_err 82400000 3
      Testing DDR ECC:
         ECC test: Disabling DDR ECC ...
         ECC test: addr 0x82400000, read data 0x0, written data 0x3, err pattern: 0x3, read after write data 0x3
         ECC test: Enabled DDR ECC ...�
      U-Boot SPL 2024.04-ti-g818c76aed67f (Aug 01 2024 - 19:19:47 +0000)
      SYSFW ABI: 4.0 (firmware rev 0x000a '10.0.8--v10.00.08 (Fiery Fox)')
      ECC is enabled, priming DDR which will take several seconds.
      ECC: priming DDR completed in 1357 msec

The following example generates a 1-bit error on bit 0 of the data at
addresses 0x82400000 and 0x82400008.

   .. code-block:: text

      => ddrss ecc_err 82400000 1
      Testing DDR ECC:
         ECC test: Disabling DDR ECC ...
         ECC test: addr 0x82400000, read data 0x0, written data 0x1, err pattern: 0x1, read after write data 0x1
         ECC test: Enabled DDR ECC ...
         ECC test: addr 0x82400000, read data 0x0
         ECC test: DDR ECC 1-bit error
         ECC test: 1-bit ECC err count: 1
         ECC test: 1-bit error in [0x2400000:0x2400008]
      => ddrss ecc_err 82400008 1
      Testing DDR ECC:
         ECC test: Disabling DDR ECC ...
         ECC test: addr 0x82400008, read data 0x0, written data 0x1, err pattern: 0x1, read after write data 0x1
         ECC test: Enabled DDR ECC ...�
      U-Boot SPL 2024.04-ti-g818c76aed67f (Aug 01 2024 - 19:19:47 +0000)
      SYSFW ABI: 4.0 (firmware rev 0x000a '10.0.8--v10.00.08 (Fiery Fox)')
      ECC is enabled, priming DDR which will take several seconds.
      ECC: priming DDR completed in 1357 msec

Trusted Firmware-A (TFA) custom handler
"""""""""""""""""""""""""""""""""""""""

``plat_ea_handler`` is invoked by the runtime exception handling
framework for the platform to handle an External Abort received at
EL3 if ``HANDLE_EA_EL3_FIRST_NS`` is enabled.

   1. Add ``plat_ea_handler`` to report ECC uncorrectable error and
      call ``plat_default_ea_handler``

         .. code-block:: c

            // trusted-firmware-a/plat/ti/k3/common/k3_ea.c

            #include <inttypes.h>
            #include <stdint.h>

            #include <common/bl_common.h>
            #include <common/debug.h>
            #include <arch_helpers.h>
            #include <plat/common/platform.h>
            #include <bl31/ea_handle.h>
            #include <lib/mmio.h>

            #include <platform_def.h>

            void plat_ea_handler(unsigned int ea_reason, uint64_t syndrome, void *cookie,
                                 void *handle, uint64_t flags) {
               unsigned long v2a_int_stat_reg;
               v2a_int_stat_reg = mmio_read_32(K3_DDRSS_BASE + K3_DDRSS_V2A_INT_STAT_REG);
               ERROR_NL();
               if(v2a_int_stat_reg & K3_DDRSS_V2A_INT_STAT_REG_ECC2BERR)
                  ERROR("DDR ECC Multi-bit error detected\n");
               else if(v2a_int_stat_reg & K3_DDRSS_V2A_INT_STAT_REG_ECCM1BERR)
                  ERROR("DDR ECC Multiple 1-bit error detected\n");

               console_flush();
               plat_default_ea_handler(ea_reason, syndrome, cookie, handle, flags);
            }

   2. Define the DDRSS registers ``K3_DDRSS_BASE``, ``K3_DDRSS_SIZE`` and
      ``K3_DDRSS_V2A_INT_STAT_REG``

         .. code-block:: c

            // trusted-firmware-a/plat/ti/k3/include/platform_def.h

            #define K3_GIC_BASE     0x01800000
            #define K3_GIC_SIZE     0x200000

            #define K3_DDRSS_BASE                       0x0F300000
            #define K3_DDRSS_SIZE                       0x200
            #define K3_DDRSS_V2A_INT_STAT_REG           0xA4
            #define K3_DDRSS_V2A_INT_STAT_REG_ECC2BERR  BIT(4)
            #define K3_DDRSS_V2A_INT_STAT_REG_ECCM1BERR BIT(5)

            #if !K3_SEC_PROXY_LITE
            #define SEC_PROXY_DATA_BASE     0x32C00000

   3. Map ``K3_DDRSS_BASE`` and ``K3_DDRSS_SIZE``

         .. code-block:: c

            // trusted-firmware-a/plat/ti/k3/common/k3_bl31_setup.c

            /* Table of regions to map using the MMU */
            const mmap_region_t plat_k3_mmap[] = {
                  K3_MAP_REGION_FLAT(K3_USART_BASE,       K3_USART_SIZE,       MT_DEVICE | MT_RW | MT_SECURE),
                  K3_MAP_REGION_FLAT(K3_GIC_BASE,         K3_GIC_SIZE,         MT_DEVICE | MT_RW | MT_SECURE),
                  K3_MAP_REGION_FLAT(K3_GTC_BASE,         K3_GTC_SIZE,         MT_DEVICE | MT_RW | MT_SECURE),
                  K3_MAP_REGION_FLAT(SEC_PROXY_RT_BASE,   SEC_PROXY_RT_SIZE,   MT_DEVICE | MT_RW | MT_SECURE),
                  K3_MAP_REGION_FLAT(SEC_PROXY_SCFG_BASE, SEC_PROXY_SCFG_SIZE, MT_DEVICE | MT_RW | MT_SECURE),
                  K3_MAP_REGION_FLAT(SEC_PROXY_DATA_BASE, SEC_PROXY_DATA_SIZE, MT_DEVICE | MT_RW | MT_SECURE),
                  K3_MAP_REGION_FLAT(K3_DDRSS_BASE,       K3_DDRSS_SIZE,       MT_DEVICE | MT_RW | MT_SECURE),
                  { /* sentinel */ }
            };

   4. Add :file:`trusted-firmware-a/plat/ti/k3/common/k3_ea.c` to
      ``BL31_SOURCES``

         .. code-block:: make

            # trusted-firmware-a/plat/ti/k3/common/plat_common.mk

            BL31_SOURCES            +=      \
                              ${PLAT_PATH}/common/k3_bl31_setup.c     \
                              ${PLAT_PATH}/common/k3_helpers.S        \
                              ${PLAT_PATH}/common/k3_topology.c       \
                              ${PLAT_PATH}/common/k3_ea.c             \
                              ${K3_GIC_SOURCES}                       \
                              ${K3_PSCI_SOURCES}                      \
                              ${K3_SEC_PROXY_SOURCES}                 \
                              ${K3_TI_SCI_SOURCES}                    \

   5. Enable ``HANDLE_EA_EL3_FIRST_NS``

         .. code-block:: make

            # trusted-firmware-a/plat/ti/k3/common/plat_common.mk

            # Allow customizing the UART baud rate
            K3_USART_BAUD := 115200
            $(eval $(call add_define,K3_USART_BAUD))

            HANDLE_EA_EL3_FIRST_NS := 1

            # Libraries
            include lib/xlat_tables_v2/xlat_tables.mk0

The following example generates a 2-bit error on bits 0 and 1 of the
data at address 0x82400000.

   .. code-block:: text

      => ddrss ecc_err 82400000 3
      Testing DDR ECC:
         ECC test: Disabling DDR ECC ...
         ECC test: addr 0x82400000, read data 0x0, written data 0x3, err pattern: 0x3, read after write data 0x3
         ECC test: Enabled DDR ECC ...

      ERROR:   DDR ECC Multi-bit error detected

      ERROR:   Unhandled External Abort received on 0x80000000 from EL2
      ERROR:   exception reason=1 syndrome=0x92000210
      Unhandled Exception from lower EL.
      x0             = 0x0000000000000000
      x1             = 0x0000000000000000
      x2             = 0x000000000000000a
      x3             = 0x0000000002800000
      x4             = 0x0000000002800000
      x5             = 0x00000000fde9132f
      x6             = 0x00000000fffa6762
      x7             = 0x00000000fde91770
      x8             = 0x00000000fffffff0
      x9             = 0x0000000000000008
      x10            = 0x0000000000000010
      x11            = 0x0000000000000002
      x12            = 0x0000000000000002
      x13            = 0x00000000fde91948
      x14            = 0x00000000fde91a50
      x15            = 0x0000000000000000
      x16            = 0x00000000fff40520
      x17            = 0x0000000000000000
      x18            = 0x00000000fde9ddb0
      x19            = 0x0000000000000004
      x20            = 0x0000000082400000
      x21            = 0x0000000000000000
      x22            = 0x000000000000023f
      x23            = 0x0000000000000003
      x24            = 0x0000000000000000
      x25            = 0x0000000000000000
      x26            = 0x000000000f300134
      x27            = 0x000000000000dfff
      x28            = 0x0000000000000000
      x29            = 0x00000000fde91770
      x30            = 0x00000000fff03450
      scr_el3        = 0x000000000000073d
      sctlr_el3      = 0x0000000030cd183f
      cptr_el3       = 0x0000000000000000
      tcr_el3        = 0x0000000080803520
      daif           = 0x00000000000002c0
      mair_el3       = 0x00000000004404ff
      spsr_el3       = 0x00000000000002c9
      elr_el3        = 0x00000000fff03450
      ttbr0_el3      = 0x000000009e793240
      esr_el3        = 0x0000000092000210
      far_el3        = 0x0000000082400000
      spsr_el1       = 0x0000000000000000
      elr_el1        = 0x0000000000000000
      spsr_abt       = 0x0000000000000000
      spsr_und       = 0x0000000000000000
      spsr_irq       = 0x0000000000000000
      spsr_fiq       = 0x0000000000000000
      sctlr_el1      = 0x0000000030d00801
      actlr_el1      = 0x0000000000000000
      cpacr_el1      = 0x0000000000000000
      csselr_el1     = 0x0000000000000000
      sp_el1         = 0x0000000000000000
      esr_el1        = 0x0000000000000000
      ttbr0_el1      = 0x0000000000000000
      ttbr1_el1      = 0x0000000000000000
      mair_el1       = 0x0000000000000000
      amair_el1      = 0x0000000000000000
      tcr_el1        = 0x0000000000800080
      tpidr_el1      = 0x0000000000000000
      tpidr_el0      = 0x0000000000000000
      tpidrro_el0    = 0x0000000000000000
      par_el1        = 0x0000000000000000
      mpidr_el1      = 0x0000000080000000
      afsr0_el1      = 0x0000000000000000
      afsr1_el1      = 0x0000000000000000
      contextidr_el1 = 0x0000000000000000
      vbar_el1       = 0x0000000000000000
      cntp_ctl_el0   = 0x0000000000000002
      cntp_cval_el0  = 0x0801e3088020c0b2
      cntv_ctl_el0   = 0x0000000000000002
      cntv_cval_el0  = 0xaefcc7a67dc999c0
      cntkctl_el1    = 0x0000000000000000
      sp_el0         = 0x000000009e78d6d0
      isr_el1        = 0x0000000000000000
      dacr32_el2     = 0x0000000000000000
      ifsr32_el2     = 0x0000000000000000
      cpuectlr_el1   = 0x0000000000000040
      cpumerrsr_el1  = 0x00000000010405d7
      l2merrsr_el1   = 0x0000000011005408
      cpuactlr_el1   = 0x00001000090ca000

      U-Boot SPL 2024.04-ti-g818c76aed67f (Aug 01 2024 - 19:19:47 +0000)
      SYSFW ABI: 4.0 (firmware rev 0x000a '10.0.8--v10.00.08 (Fiery Fox)')
      ECC is enabled, priming DDR which will take several seconds.
      ECC: priming DDR completed in 1356 msec

The following example generates a 1-bit error on bit 0 of the data at
addresses 0x82400000 and 0x82400008.

   .. code-block:: text

      => ddrss ecc_err 82400000 1
      Testing DDR ECC:
         ECC test: Disabling DDR ECC ...
         ECC test: addr 0x82400000, read data 0x0, written data 0x1, err pattern: 0x1, read after write data 0x1
         ECC test: Enabled DDR ECC ...
         ECC test: addr 0x82400000, read data 0x0
         ECC test: DDR ECC 1-bit error
         ECC test: 1-bit ECC err count: 1
         ECC test: 1-bit error in [0x2400000:0x2400008]
      => ddrss ecc_err 82400008 1
      Testing DDR ECC:
         ECC test: Disabling DDR ECC ...
         ECC test: addr 0x82400008, read data 0x0, written data 0x1, err pattern: 0x1, read after write data 0x1
         ECC test: Enabled DDR ECC ...

      ERROR:   DDR ECC Multiple 1-bit error detected

      ERROR:   Unhandled External Abort received on 0x80000000 from EL2
      ERROR:   exception reason=1 syndrome=0x92000210
      Unhandled Exception from lower EL.
      x0             = 0x0000000000000000
      x1             = 0x0000000000000000
      x2             = 0x000000000000000a
      x3             = 0x0000000002800000
      x4             = 0x0000000002800000
      x5             = 0x00000000fde9132f
      x6             = 0x00000000fffa6762
      x7             = 0x00000000fde91770
      x8             = 0x00000000fffffff0
      x9             = 0x0000000000000008
      x10            = 0x0000000000000010
      x11            = 0x0000000000000002
      x12            = 0x0000000000000002
      x13            = 0x00000000fde91948
      x14            = 0x00000000fde91a50
      x15            = 0x0000000000000000
      x16            = 0x00000000fff40520
      x17            = 0x0000000000000000
      x18            = 0x00000000fde9ddb0
      x19            = 0x0000000000000004
      x20            = 0x0000000082400008
      x21            = 0x0000000000000000
      x22            = 0x000000000000023f
      x23            = 0x0000000000000001
      x24            = 0x0000000000000000
      x25            = 0x0000000000000000
      x26            = 0x000000000f300134
      x27            = 0x000000000000dfff
      x28            = 0x0000000000000000
      x29            = 0x00000000fde91770
      x30            = 0x00000000fff03450
      scr_el3        = 0x000000000000073d
      sctlr_el3      = 0x0000000030cd183f
      cptr_el3       = 0x0000000000000000
      tcr_el3        = 0x0000000080803520
      daif           = 0x00000000000002c0
      mair_el3       = 0x00000000004404ff
      spsr_el3       = 0x00000000000002c9
      elr_el3        = 0x00000000fff03450
      ttbr0_el3      = 0x000000009e793240
      esr_el3        = 0x0000000092000210
      far_el3        = 0x0000000082400008
      spsr_el1       = 0x0000000000000000
      elr_el1        = 0x0000000000000000
      spsr_abt       = 0x0000000000000000
      spsr_und       = 0x0000000000000000
      spsr_irq       = 0x0000000000000000
      spsr_fiq       = 0x0000000000000000
      sctlr_el1      = 0x0000000030d00801
      actlr_el1      = 0x0000000000000000
      cpacr_el1      = 0x0000000000000000
      csselr_el1     = 0x0000000000000000
      sp_el1         = 0x0000000000000000
      esr_el1        = 0x0000000000000000
      ttbr0_el1      = 0x0000000000000000
      ttbr1_el1      = 0x0000000000000000
      mair_el1       = 0x0000000000000000
      amair_el1      = 0x0000000000000000
      tcr_el1        = 0x0000000000800080
      tpidr_el1      = 0x0000000000000000
      tpidr_el0      = 0x0000000000000000
      tpidrro_el0    = 0x0000000000000000
      par_el1        = 0x0000000000000000
      mpidr_el1      = 0x0000000080000000
      afsr0_el1      = 0x0000000000000000
      afsr1_el1      = 0x0000000000000000
      contextidr_el1 = 0x0000000000000000
      vbar_el1       = 0x0000000000000000
      cntp_ctl_el0   = 0x0000000000000002
      cntp_cval_el0  = 0x0801e1088020c0b2
      cntv_ctl_el0   = 0x0000000000000002
      cntv_cval_el0  = 0xaffcc7a67dc989c0
      cntkctl_el1    = 0x0000000000000000
      sp_el0         = 0x000000009e78d6d0
      isr_el1        = 0x0000000000000000
      dacr32_el2     = 0x0000000000000000
      ifsr32_el2     = 0x0000000000000000
      cpuectlr_el1   = 0x0000000000000040
      cpumerrsr_el1  = 0x00000000000405b7
      l2merrsr_el1   = 0x0000000011005808
      cpuactlr_el1   = 0x00001000090ca000

      U-Boot SPL 2024.04-ti-g818c76aed67f (Aug 01 2024 - 19:19:47 +0000)
      SYSFW ABI: 4.0 (firmware rev 0x000a '10.0.8--v10.00.08 (Fiery Fox)')
      ECC is enabled, priming DDR which will take several seconds.
      ECC: priming DDR completed in 1356 msec


.. note::

   ESM is a hardware logic to handle errors in the system. If both ESM
   and trusted-firmware-a logics are enabled, ESM takes charge and resets
   the device, before trusted-firmware-a handles.

The following example shows the message if the ECC is not enabled in DDRSS.

   .. code-block:: text

      => ddrss ecc_err 82400000 1
      ECC not enabled. Please enable ECC any try again
