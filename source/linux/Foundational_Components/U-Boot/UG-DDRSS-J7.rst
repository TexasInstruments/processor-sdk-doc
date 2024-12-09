#########
DDRSS ECC
#########

********
Overview
********

The DDR subsystem (DDRSS) comprises DDR controller, DDR PHY and wrapper logic
to integrate these blocks in the device. For SDRAM data integrity, the DDRSS
bridge supports inline ECC on the data written to or read from the SDRAM. ECC
is stored together with the data so that a dedicated SDRAM device for ECC is
not required. The 8-bit single error correction double error detection (SECDED)
ECC data is calculated over 64-bit data quanta. For every 256-byte data block
32 bytes of ECC is stored inline. Thus 1/9th of the total SDRAM space is used
for ECC storage and the remaining 8/9th of the SDRAM data space are seen as
consecutive byte addresses. Even if there are non-ECC protected regions the
previously described 1/9th-8/9th rule still applies and consecutive byte
addresses are seen from system point of view. |__PART_FAMILY_DEVICE_NAMES__|
supports up to 3 ECC protected non-overlapping memory ranges. The current
U-Boot release supports a single region covering the entire SDRAM space.

ECC is calculated for all accesses that are within the address ranges
protected by it. 1-bit error is correctable by ECC, but multi-bit and
multiple 1-bit errors are not correctable and will be treated as an
uncorrectable error. Any uncorrectable error will cause a bus abort.

DDRSS ECC handling
==================

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

