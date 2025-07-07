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

+--------------------------------------------------+-----------------------------------+------------------------------+
| Config File                                      | Description                       | Supported machines/platforms |
+==================================================+===================================+==============================+
| processor-sdk-scarthgap-11.01.05.03-config.txt   | Processor SDK 11.01.05.03 Release | am64xx-evm                   |
+--------------------------------------------------+-----------------------------------+------------------------------+

