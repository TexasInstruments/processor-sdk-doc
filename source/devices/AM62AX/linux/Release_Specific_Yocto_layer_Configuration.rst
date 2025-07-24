.. _yocto-layer-configuration:

**************************
Yocto Layer Configuration
**************************

.. http://processors.wiki.ti.com/index.php/Processor_SDK_Building_The_SDK#Layer_Configuration

Processor SDK uses the following oe-layersetup configs to configure the
meta layers. These are the <config> used in the command:

``$ ./oe-layertool-setup.sh -f <config>``

The following config files are located in the **configs/processor-sdk-analytics**
directory of the `oe-layersetup git repo <https://git.ti.com/cgit/arago-project/oe-layersetup/>`_.

+----------------------------------------------------+------------------------------------------------+--------------------------------+
|                    Description                     |      Config File                               | Supported yocto build machine  |
+====================================================+================================================+================================+
| |__SDK_FULL_NAME__| : 11_01_07_05 Release          | processor-sdk-analytics-11_01_07_05-config.txt | |__SDK_BUILD_MACHINE__|        |
+----------------------------------------------------+------------------------------------------------+--------------------------------+

