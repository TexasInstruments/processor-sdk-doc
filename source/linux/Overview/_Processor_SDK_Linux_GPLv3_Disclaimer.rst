************************************
GPLv3 Disclaimer
************************************
.. http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_GPLv3_Disclaimer

There are GPLv3 licensed software components contained within the
Processor SDK for Linux on both the target and the host.  The software
manifest (software\_manifest.htm) for the Linux SDK is located in the
manifest/ directory of the installed SDK.  All GPLv3 components for both
target and host are contained in the SDK directory.

.. warning::
   These GPLv3 components are provided for development purposes
   only and may be removed for production solutions.

.. rubric:: How to Identify the GPLv3 components
   :name: how-to-identify-the-gplv3-components

To idenitfy the GPLv3 components installed on the target file system,
run the gplv3-notice script located on the target file system
located here: **/etc/init.d/gplv3-notice**

The gplv3-notice script will list all Processor SDK Linux installed
packages as shipped.  If you installed additional GPLv3 components this
script may not identify them until the next target reboot.

|

.. rubric:: How to Remove Target side GPLv3 Components
   :name: how-to-remove-target-side-gplv3-components

The gplv3-notice script also outputs how to remove the packages.  To
remove individual packages from the target development file system, use
the opkg remove command which is: **opkg remove <package>**

