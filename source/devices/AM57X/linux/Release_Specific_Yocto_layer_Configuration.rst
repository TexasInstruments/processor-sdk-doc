.. _yocto-layer-configuration:

**************************
Yocto Layer Configuration
**************************

.. http://processors.wiki.ti.com/index.php/Processor_SDK_Building_The_SDK#Layer_Configuration

Processor SDK uses the following oe-layersetup configs to configure the
meta layers. These are the <config> used in the command:

``$ ./oe-layertool-setup.sh -f <config>``

|
| The following config files are located in the **yocto-build/configs/processor-sdk-linux**
  directory.

+-------------------------------------+----------------------------------------------------+--------------------------------+
|      Config File                    |                    Description                     | Supported machines             |
+=====================================+====================================================+================================+
| processor-sdk-linux-11_01_02_01.txt | Processor SDK Linux 11_01 Release                  | am57xx-evm, am57xx-hs-evm      |
+-------------------------------------+----------------------------------------------------+--------------------------------+
