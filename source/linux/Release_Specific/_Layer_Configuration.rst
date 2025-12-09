**************************
Yocto Layer Configuration
**************************

Processor SDK uses the following oe-layersetup configs to configure the
meta layers. These are the <config> used in the command:

``$ ./oe-layertool-setup.sh -f <config>``

.. ifconfig:: CONFIG_sdk in ('SITARA')

    The following config files are located in the **configs/processor-sdk** directory of the `oe-layersetup git repo <https://git.ti.com/cgit/arago-project/oe-layersetup/>`_.

    +-------------------------------------------------+-----------------------------------+-----------------------------------------------------------------------------------------------+
    | Config File                                     | Description                       | Supported machines/platforms                                                                  |
    +=================================================+===================================+===============================================================================================+
    | processor-sdk-scarthgap-11.02.05.02-config.txt  | Processor SDK 11.02.05.02 Release | am335x-evm, am437x-evm, am65xx-hs-evm                                                         |
    +-------------------------------------------------+-----------------------------------+-----------------------------------------------------------------------------------------------+
    | processor-sdk-scarthgap-11.02.08.02-config.txt  | Processor SDK 11.02.08.02 Release | am64xx-evm, am62xx-evm, am62xx-lp-evm, am62xxsip-evm, am62lxx-evm, am62pxx-evm, am62dxx-evm   |
    +-------------------------------------------------+-----------------------------------+-----------------------------------------------------------------------------------------------+

