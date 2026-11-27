.. _yocto-layer-configuration:

#########################
Yocto Layer Configuration
#########################

Processor SDK uses oe-layersetup configuration files to initialize the
Yocto build environment. Configure your build with the following command:

.. code-block:: console

   $ ./oe-layertool-setup.sh -f <config>

Replace ``<config>`` with one of the configuration files listed below.

The `oe-layersetup git repository <https://git.ti.com/cgit/arago-project/oe-layersetup/>`__
contains the following configuration files in the :file:`configs/processor-sdk` directory.

.. list-table:: Yocto Layer Configuration
   :widths: 50 50 30
   :header-rows: 1

   * - Config File
     - Description
     - Supported machines/platforms
   * - :file:`processor-sdk-wrynose-12.02.00.07.05-config.txt`
     - Processor SDK 12.02.00.07.05 Release
     - |__SDK_BUILD_MACHINE__|
