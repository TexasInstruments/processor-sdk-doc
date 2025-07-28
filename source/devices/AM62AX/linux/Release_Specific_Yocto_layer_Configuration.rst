.. _yocto-layer-configuration:

*************************
Yocto Layer Configuration
*************************

Processor SDK uses the following oe-layersetup configs to configure the
meta layers. These are the <config> used in the command:

.. code-block:: console

   $ ./oe-layertool-setup.sh -f <config>

The following config files are located in the :file:`configs/processor-sdk-analytics`
directory of the `oe-layersetup git repo <https://git.ti.com/cgit/arago-project/oe-layersetup/>`_.

+-------------------------------------------------------------------+------------------------------------------------------+------------------------------+
| Config File                                                       | Description                                          | Supported machines/platforms |
+===================================================================+======================================================+==============================+
| processor-sdk-analytics-11.01.07.05-config.txt                    | Used for building EdgeAI filesystem                  | am62axx-evm                  |
+-------------------------------------------------------------------+------------------------------------------------------+------------------------------+
| processor-sdk-analytics-selinux-11.01.07.05-config.txt            | Used for building SELinux enabled EdgeAI filesystem  | am62axx-evm                  |
+-------------------------------------------------------------------+------------------------------------------------------+------------------------------+

The oe-layersetup configuration, as defined in :file:`processor-sdk-analytics-11.01.07.05-config.txt` is used for configuring the meta layers in the yocto SD card image available on |__SDK_DOWNLOAD_URL__|.
