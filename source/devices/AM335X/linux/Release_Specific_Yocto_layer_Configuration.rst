.. _yocto-layer-configuration:

#########################
Yocto Layer Configuration
#########################

Processor SDK uses the following oe-layersetup configs to configure the
Yocto build. One of these file paths is specified by the ``<config>`` argument
in the following command:

.. code-block:: console

   $ ./oe-layertool-setup.sh -f <config>

The following Configuration files are located in the :file:`configs/processor-sdk`
directory of the `oe-layersetup git repository <https://git.ti.com/cgit/arago-project/oe-layersetup/>`__.

.. list-table:: Yocto Layer Configuration
   :widths: 50 50 30
   :header-rows: 1

   * - Config File
     - Description
     - Supported machines/platforms
   * - :file:`processor-sdk-scarthgap-11.02.05.02-config.txt`
     - Processor SDK 11.02.05.02 Release
     - |__SDK_BUILD_MACHINE__|
