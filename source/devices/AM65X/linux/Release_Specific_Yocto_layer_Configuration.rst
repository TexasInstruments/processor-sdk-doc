.. _yocto-layer-configuration:

**************************
Yocto Layer Configuration
**************************

Processor SDK uses the following oe-layersetup configs to configure the
meta layers. These are the <config> used in the command:

``$ ./oe-layertool-setup.sh -f <config>``

|
| The following config files are located in the **configs/processor-sdk/**
  directory of the `oe-layersetup git repo <https://git.ti.com/cgit/arago-project/oe-layersetup/>`_.

+-----------------------------------------------+----------------------------------------------------+--------------------------------+
|      Config File                              |                    Description                     | Supported machines             |
+===============================================+====================================================+================================+
| processor-sdk-09.03.05.02-legacy-config.txt   | Processor SDK Linux 09.03.05.02 Release            | am65xx-evm                     |
+-----------------------------------------------+----------------------------------------------------+--------------------------------+
