##############
Flash via UART
##############

This tool uses UART as the transport or interface to send the file to flash to the EVM.

The UART Flash tool is part of MCU+SDK installer and can be downloaded from |__SDK_DOWNLOAD_URL__|.

Detailed instructions on using the tool can be found in MCU+SDK docs.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    `MCU+SDK Flash Tools Documentation  <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62X/latest/exports/docs/api_guide_am62x/TOOLS_FLASH.html>`__.

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   `MCU+SDK Flash Tools Documentation  <https://software-dl.ti.com/mcu-plus-sdk/esd/AM64X/latest/exports/docs/api_guide_am62x/TOOLS_FLASH.html>`__.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   `MCU+SDK Flash Tools Documentation  <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62PX/11_01_01_08/exports/docs/api_guide_am62px/TOOLS_FLASH.html>`__.
