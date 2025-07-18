.. _foundational-components-u-boot:

######
U-Boot
######

This document covers the general use of Processor SDK Release of U-Boot on
following platform(s):

.. ifconfig:: CONFIG_part_family in ('AM335X_family')

   | `AM335x GP EVM <http://www.ti.com/tool/tmdxevm3358>`__
   | `AM335x EVM-SK <http://www.ti.com/tool/tmdssk3358>`__
   | `AM335x ICE <http://www.ti.com/tool/tmdsice3359>`__
   | `BeagleBone White <http://beagleboard.org/bone>`__
   | `BeagleBone Black <https://beagleboard.org/black>`__

.. ifconfig:: CONFIG_part_family in ('AM437X_family')

   |  `AM437x GP EVM <http://www.ti.com/tool/tmdsevm437x>`__
   |  AM43xx ePOS EVM
   |  `AM437x EVM-SK <http://www.ti.com/tool/tmdxsk437x>`__
   |  `AM437x IDK <http://www.ti.com/tool/TMDSIDK437X>`__

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM57x_family')

   |  `DRA76x EVM <http://www.ti.com/tool/J6PEVM577P>`__
   |  `DRA74x EVM <http://www.ti.com/tool/j6evm5777>`__
   |  `DRA72x EVM <http://www.ti.com/tool/dra72xevm>`__
   |  `DRA71x EVM <http://www.ti.com/product/DRA718>`__
   |  `AM574x IDK <http://www.ti.com/tool/TMDSIDK574>`__
   |  `AM572x GP EVM <http://www.ti.com/tool/tmdsevm572x>`__
   |  `AM572x IDK <http://www.ti.com/tool/TMDXIDK5728>`__
   |  `AM571x IDK <http://www.ti.com/tool/tmdxidk5718>`__
   |  `66AK2H EVM <http://www.ti.com/tool/EVMK2H>`__
   |  K2K EVM
   |  `K2Ex EVM <http://www.ti.com/tool/xevmk2ex>`__
   |  `K2L EVM <http://www.ti.com/tool/xevmk2lx>`__
   |  `K2G GP EVM <http://www.ti.com/tool/evmk2g>`__
   |  `K2G ICE EVM <http://www.ti.com/tool/k2gice>`__
   |  `OMAP-L138 LCDK <http://www.ti.com/product/omap-l138>`__

.. ifconfig:: CONFIG_part_variant in ('AM65X')

   |  `AM65x EVM <http://www.ti.com/tool/TMDX654GPEVM>`__
   |  `AM65x IDK <http://www.ti.com/tool/TMDX654IDKEVM>`__

.. ifconfig:: CONFIG_part_variant in ('J721E')

   |  `J721E EVM <http://www.ti.com/tool/J721EXSOMXEVM>`__
   |  `J721E SK <http://www.ti.com/tool/SK-TDA4VM>`__

.. ifconfig:: CONFIG_part_variant in ('J7200')

   |  `J7200 EVM <http://www.ti.com/tool/J7200XSOMXEVM>`__

.. ifconfig:: CONFIG_part_variant in ('AM64X')

   |  `AM64x EVM <https://www.ti.com/store/ti/en/p/product/?p=TMDS64GPEVM>`__

|

.. toctree::
    :maxdepth: 2

    Foundational_Components/U-Boot/Users-Guide
    Foundational_Components/U-Boot/Applications
