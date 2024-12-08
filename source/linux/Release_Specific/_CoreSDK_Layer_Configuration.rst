**************************
Yocto Layer Configuration
**************************

Processor SDK uses the following oe-layersetup configs to configure the
meta layers. These are the <config> used in the command:

``$ ./oe-layersetup.sh -f <config>``


    |
    | The following config files are located in the **configs/coresdk**
      directory of the `oe-layersetup git repo <https://git.ti.com/cgit/arago-project/oe-layersetup/>`_.

    +-----------------------------------+---------------------------------------+--------------------------------------------------------+
    | Config File                       | Description                           | Supported machines/platforms                           |
    +===================================+=======================================+========================================================+
    |  coresdk-10.01.10-config.txt      | CoreSDK 10.01 Sitara Release          | am64x 2.0, am62x, am62sip, am62x-lp, am62a, am62p      |
    +-----------------------------------+---------------------------------------+--------------------------------------------------------+

