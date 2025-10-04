**************************
Yocto Layer Configuration
**************************

Processor SDK uses the following oe-layersetup configs to configure the
meta layers. These are the <config> used in the command:

``$ ./oe-layersetup.sh -f <config>``


    |
    | The following config files located in the **configs/coresdk**
      directory of the `oe-layersetup git repo <https://git.ti.com/cgit/arago-project/oe-layersetup/>`_.

    +-----------------------------------+----------------------------------+----------------------------------------------------------------------------+
    | Config File                       | Description                      | Supported machines/platforms                                               |
    +===================================+==================================+============================================================================+
    |  coresdk-11.01.05-config.txt      | CoreSDK 11.01 Sitara Release     | am64x 2.0, am62x, am62sip, am62x-lp, am62px 1.0, am62px 1.1, am62d         |
    +-----------------------------------+----------------------------------+----------------------------------------------------------------------------+
    |  coresdk-11.01.07-config.txt      | CoreSDK 11.01 Sitara Release     | am62a                                                                      |
    +-----------------------------------+----------------------------------+----------------------------------------------------------------------------+
    |  coresdk-11.01.16-config.txt      | CoreSDK 11.01 Sitara Release     | am62lx 1.1, am62px 1.1, am62px 1.2                                         |
    +-----------------------------------+----------------------------------+----------------------------------------------------------------------------+

