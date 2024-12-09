**************************
Yocto Layer Configuration
**************************

Processor SDK uses the following oe-layersetup configs to configure the
meta layers. These are the <config> used in the command:

``$ ./oe-layertool-setup.sh -f <config>``

.. ifconfig:: CONFIG_sdk in ('SITARA')

    The following config files are located in the **configs/processor-sdk** directory of the `oe-layersetup git repo <https://git.ti.com/cgit/arago-project/oe-layersetup/>`_.

    +---------------------------------------------+-----------------------------------+---------------------------------+
    | Config File                                 | Description                       | Supported machines/platforms    |
    +=============================================+===================================+=================================+
    | processor-sdk-09.03.05.02-legacy-config.txt | Processor SDK 09.03.05.02 Release | am335x-evm, am437x-evm          |
    +---------------------------------------------+-----------------------------------+---------------------------------+

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

    |
    | The following config files are located in the **configs/**
      directory of the **configs** directory.  The yocto config can also be
      downloaded directly from the SDK release page.

    +------------------------+-------------------------------------------------+-----------------------------------+
    |      Config File       |                    Description                  | Supported machines                |
    +========================+=================================================+===================================+
    | psdkla-07_01_00.txt    | Processor SDK Linux 07_01_00 Release            | j721e-evm, j7200-evm, am65xx-evm  |
    +------------------------+-------------------------------------------------+-----------------------------------+
