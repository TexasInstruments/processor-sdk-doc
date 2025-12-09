###
DDR
###

********
Overview
********

The DDR subsystem (DDRSS) comprises DDR controller, DDR PHY and wrapper logic to
integrate these blocks in the device. The K3 DDRSS driver
(drivers/ram/k3-ddrss/k3-ddrss.c) runs during the R5 SPL stage and is
responsible for initializing and configuring the DDR subsystem.

.. _ddr-init-j7:

******************
DDR Initialization
******************

The driver utilizes an auto-generated configuration file containing the
necessary settings for the DDR. It configures the frequency, timing parameters,
training algorithms etc. for DDR initialization. The configuration DTSI can be
generated using the `Sysconfig tool <https://dev.ti.com/sysconfig>`_ and
selecting the software product as "DDR Configuration for \*" as well as the
required device.

.. _ddr-temperature-monitoring-uboot-j7:

**************************
DDR Temperature Monitoring
**************************

For enabling temperature polling in the DDR subsystem the configuration DTSI
(see :ref:`ddr-init-j7`) must be regenerated after selecting 'Yes'
for LPDDR > DDRSS x > Enable DRAM Temperature Polling and also changing the DRAM
Timing Parameters as prompted by the tool.

.. ifconfig:: CONFIG_part_variant in ('J7200', 'J721E')

   The kernel DDR driver utilizes this polling feature to provide base support for
   dynamic DDR refresh rate changes (see :ref:`ddr-temperature-monitoring-linux`)

.. ifconfig:: CONFIG_part_variant not in ('J7200', 'J721E')

   **********
   Inline ECC
   **********

   For SDRAM data integrity, the DDRSS
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

   ECC Handling
   ============

   .. note::

      The inline ECC feature of DDRSS is not enabled by default in U-Boot.

   Enabling inline ECC
   -------------------

      The inline ECC feature of DDRSS can be enabled by adding the
      ``CONFIG_K3_INLINE_ECC`` config to the R5 defconfig:

      .. code-block:: kconfig

         # u-boot/configs/*_r5_defconfig

         CONFIG_PINCTRL_SINGLE=y
         CONFIG_POWER_DOMAIN=y
         CONFIG_TI_POWER_DOMAIN=y
         CONFIG_K3_INLINE_ECC=y
         CONFIG_K3_SYSTEM_CONTROLLER=y
         CONFIG_REMOTEPROC_TI_K3_ARM64=y
         CONFIG_RESET_TI_SCI=y

      This enables inline ECC for the entire region of the DDR.

   Priming with BIST Engine
   ------------------------

      The bootloader has the responsibility to pre-load the ECC protected region with
      known data before functional reads and writes are performed. During the ECC
      initialization, the R5 SPL fills the entire memory with zeros using the BIST
      engine in the DDR controller. The BIST engine method allows priming the entire
      region with zeros in much less time.

   Enabling inline ECC for a partial region of the DDR
   ---------------------------------------------------

   Instead of defaulting to enable inline ECC for the entire DDR region, a partial
   range can also be selected.

   In this case, the DDRSS driver expects such a node within the memory node, in
   the absence of which it resorts to enabling for the entire DDR region:

      .. code-block:: dts

         inline_ecc: protected@9e780000 {
            device_type = "ecc";
            reg = <0x9e780000 0x0080000>;
            bootph-all;
         };

