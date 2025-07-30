.. _booting-over-ethernet:

Booting over Ethernet (Ethernet RGMII)
--------------------------------------

This section documents how to configure the DHCP/BOOTP server to load
bootloaders on to |__PART_FAMILY_NAME__| family of SoCs in Ethernet RGMII Boot mode.

Booting U-Boot from the network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|__PART_FAMILY_NAME__| family of SoCs supports loading SPL and U-Boot over the network
using DHCP/BOOTP protocol. The DHCP server replying to DHCP/BOOTP requests from
the SoC must provide filename to be fetched over TFTP for each stage
depending on the **Vendor-Class-Identifier (VCI)** DHCP field specified in the
request.
**VCI** DHCP field is filled out by the ROM and subsequent stages and corresponding
binaries files to be sent over TFTP are listed in the table below.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   Build tiboot3.bin using ``am64x_evm_r5_defconfig``. Build tispl.bin and u-boot.img using ``am64x_evm_a53_defconfig``.

   .. important::

      - Ethernet RGMII boot is supported over RGMII2 (Second port) on AM64x SoC.
      - RGMII boot is only supported on AM64x SK EVM and not supported on AM64x GP EVM as port is muxed to ICSSG by default
      - CPSW PHYs should be strapped as per ROM's expectation described in part's TRM.
      - Link info Bootmode pin needs to be ON along with RGMII boot mode selection Bootmode pins.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   Build tiboot3.bin using ``am62x_evm_r5_ethboot_defconfig``. Build tispl.bin and u-boot.img using ``am62x_evm_a53_ethboot_defconfig``.

   .. important::

      - Ethernet RGMII boot is supported over RGMII1 (First port) on AM62x SoC.
      - CPSW PHYs should be strapped as per ROM's expectation described in part's TRM.
      - When the link info Bootmode pin is enabled, this means no auto-negotiation or reading of the Ethernet PHY is needed since the ROM will assume the link is up at 1Gbps, full duplex mode.
      - Disable link info Bootmode pin so that ROM can identify the PHY and establishes link with the supported speed and duplex mode.
      - Please note that due to MDIO corruption (Errata i2329), booting over Ethernet is not recommended for production purposes.

.. ifconfig:: CONFIG_part_variant in ('J722S')

   Build tiboot3.bin using ``j722s_evm_r5_ethboot_defconfig``. Build tispl.bin and u-boot.img using ``j722s_evm_a53_ethboot_defconfig``.

   .. important::

      - Ethernet RGMII boot is supported over RGMII on J722s SoC.
      - CPSW PHYs should be strapped as per ROM's expectation described in part's TRM.
      - When the link info Bootmode pin is enabled, this means no auto-negotiation or reading of the Ethernet PHY is needed since the ROM will assume the link is up at 1Gbps, full duplex mode.
      - Disable link info Bootmode pin so that ROM can identify the PHY and establishes link with the supported speed and duplex mode.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   Build tiboot3.bin using ``am62px_evm_r5_ethboot_defconfig``. Build tispl.bin and u-boot.img using ``am62px_evm_a53_ethboot_defconfig``.

   .. important::

      - Ethernet RGMII boot is supported over RGMII on AM62px SoC.
      - CPSW PHYs should be strapped as per ROM's expectation described in part's TRM.
      - When the link info Bootmode pin is enabled, this means no auto-negotiation or reading of the Ethernet PHY is needed since the ROM will assume the link is up at 1Gbps, full duplex mode.
      - Disable link info Bootmode pin so that ROM can identify the PHY and establishes link with the supported speed and duplex mode.

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   Build tiboot3.bin using ``am68_evm_r5_ethboot_defconfig``. Build tispl.bin and u-boot.img using ``am68_evm_a72_ethboot_defconfig``.

   .. important::

      - Ethernet RGMII boot is supported over RGMII on J721S2 SoC.

.. ifconfig:: CONFIG_part_variant in ('AM64X','AM62X','J722S','AM62PX','J721S2')

   If using ISC dhcpd an example host entry would look like this:

   .. parsed-literal::

      subnet 10.0.0.0 netmask 255.0.0.0
      {
         range dynamic-bootp 10.0.0.2 10.0.0.16;
         if substring (option vendor-class-identifier, 0, 16) = "TI K3 Bootp Boot"
         {
            filename "tiboot3.bin";
         } elsif substring (option vendor-class-identifier, 0, |__SPL_VCI_STRING_LEN__|) = "|__SPL_VCI_STRING__|"
         {
            filename "tispl.bin";
         } elsif substring (option vendor-class-identifier, 0, |__UBOOT_VCI_STRING_LEN__|) = "|__UBOOT_VCI_STRING__|"
         {
            filename "u-boot.img";
         }

         range 10.0.0.17 10.0.0.25;
         default-lease-time 60000;
         max-lease-time 720000;
         next-server 10.0.0.1;
      }

For instructions to build the bootloader images please refer to :ref:`Build-U-Boot-label`.

A walk through of these steps to setup isc-dhcp-server on Ubuntu can be found at `here
<https://help.ubuntu.com/community/isc-dhcp-server>`__.
