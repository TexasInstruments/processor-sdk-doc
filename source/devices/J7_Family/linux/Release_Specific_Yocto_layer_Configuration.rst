.. include:: /_replacevars.rst

.. _yocto-layer-configuration:

**************************
Yocto Layer Configuration
**************************

.. http://processors.wiki.ti.com/index.php/Processor_SDK_Building_The_SDK#Layer_Configuration

|__SDK_FULL_NAME__| uses the 'oe-layersetup' tool to configure the meta layers. If you do not have the Linux SDK package installed:
::

    git clone https://git.ti.com/git/arago-project/oe-layersetup.git yocto-build
    cd yocto-build
    ./oe-layertool-setup.sh -f configs/processor-sdk-linux/<Config File>

The Linux SDK package also has the above tool cloned at the top level. If you have it installed:
::

    cd <SDK INSTALL DIR>/yocto-build
    ./oe-layertool-setup.sh -f configs/processor-sdk-linux/<Config File>

Use below in place of <Config File>, to setup the meta layers for the current release version.

+----------------------------------------------------+-------------------------------------+--------------------------------+
|                    Description                     |      Config File                    | Supported yocto build machine  |
+====================================================+=====================================+================================+
| |__SDK_FULL_NAME__| : 10_01_00 Release             | processor-sdk-linux-10_01_00.txt    | |__SDK_BUILD_MACHINE__|        |
+----------------------------------------------------+-------------------------------------+--------------------------------+
