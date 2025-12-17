.. _yocto-layer-configuration:

#########################
Yocto Layer Configuration
#########################

Processor SDK uses oe-layersetup configuration files to initialize the
Yocto build environment. Configure your build with the following command:

.. code-block:: console

   $ ./oe-layertool-setup.sh -f <config>

Replace ``<config>`` with one of the following configuration files.

The `oe-layersetup git repository <https://git.ti.com/cgit/arago-project/oe-layersetup/>`__
has the following configuration files in the :file:`configs/processor-sdk` directory.

.. list-table:: Yocto Layer Configuration
   :widths: 50 50 30
   :header-rows: 1

   * - Config File
     - Description
     - Supported machines/platforms
   * - :file:`processor-sdk-scarthgap-nonqt-11.02.08.02-config.txt`
     - Used for building Yocto based filesystem
     - |__SDK_BUILD_MACHINE__|
