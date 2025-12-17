.. _yocto-layer-configuration:

#########################
Yocto Layer Configuration
#########################

Processor SDK uses oe-layersetup configuration files to initialize the
Yocto build environment. Configure your build with the following command:

.. code-block:: console

   $ ./oe-layertool-setup.sh -f <config>

Replace ``<config>`` with one of the following configuration files.

The :file:`yocto-build/configs/processor-sdk-linux` directory has the following configuration files.

.. list-table:: Yocto Layer Configuration
   :widths: 50 50 30
   :header-rows: 1

   * - Config File
     - Description
     - Supported machines/platforms
   * - :file:`processor-sdk-linux-11_01_02_01.txt`
     - Processor SDK Linux 11_01 Release
     - |__SDK_BUILD_MACHINE__|, am57xx-hs-evm
