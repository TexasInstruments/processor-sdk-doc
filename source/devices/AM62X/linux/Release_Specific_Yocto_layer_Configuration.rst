.. _yocto-layer-configuration:

*************************
Yocto Layer Configuration
*************************

Processor SDK uses the following oe-layersetup configs to configure the
meta layers. These are the <config> used in the command:

.. code-block:: console

   $ ./oe-layertool-setup.sh -f <config>

The following config files are located in the ``configs/processor-sdk``
directory of the `oe-layersetup git repo <https://git.ti.com/cgit/arago-project/oe-layersetup/>`_.

+-------------------------------------------------------------------+-----------------------------------+----------------------------------------------------------+
| Config File                                                       | Description                       | Supported machines/platforms                             |
+===================================================================+===================================+==========================================================+
| processor-sdk-scarthgap-chromium-11.02.08.02-config.txt           | Processor SDK 11.02.08.02 Release | am62xx-evm, am62xx-lp-evm, beagleplay-ti                 |
+-------------------------------------------------------------------+-----------------------------------+----------------------------------------------------------+
| processor-sdk-scarthgap-11.02.08.02-config.txt                    | Processor SDK 11.02.08.02 Release | am62xx-evm, am62xx-lp-evm, am62xxsip-evm, beagleplay-ti  |
+-------------------------------------------------------------------+-----------------------------------+----------------------------------------------------------+
| processor-sdk-scarthgap-selinux-11.02.08.02-config.txt            | Processor SDK 11.02.08.02 Release | am62xx-evm, am62xx-lp-evm, am62xxsip-evm, beagleplay-ti  |
+-------------------------------------------------------------------+-----------------------------------+----------------------------------------------------------+

The oe-layersetup configuration, as defined in ``processor-sdk-scarthgap-chromium-11.02.08.02-config.txt``, is used for configuring the meta layers in the yocto SD card image available on |__SDK_DOWNLOAD_URL__|.
