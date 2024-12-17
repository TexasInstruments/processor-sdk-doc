.. http://processors.wiki.ti.com/index.php/Update_U-Boot_Environment_Variables_stored_in_SPI_Flash_from_Linux

Update U-Boot Environment Variables stored in SPI Flash from Linux
====================================================================

.. rubric:: Purpose
   :name: purpose

The purpose of this article is to demonstrate how the U-Boot Environment
variables stored in SPI Flash can be accessed from a Linux command line
using a tool provided from U-Boot.

.. rubric:: Assumptions

#. This example is based on the AMSDK, AM335x GP EVM and the User is has
   the latest version of the AMSDK installed

|

.. rubric:: Summary/Checklist
   :name: summarychecklist

#. Build(Cross Compile) fw\_printenv/fw\_setenv U-Boot Tool provided
   with U-Boot source in the AMSDK
#. Prepare configuration file for U-Boot Tool fw\_printenv/fw\_setenv
#. Load fw\_printenv/fw\_setenv into target file system
#. Test fw\_printenv/fw\_setenv tool

|

.. rubric:: Overview

To access the environment variables from Linux one of the tools from
u-boot must be cross compiled and copied into the file system. This tool
is located in the board-support/u-boot<version>/tools/env directory of
the latest AMSDK.

.. Image:: /images/Sitara-Linux-Spi_nor_overview_1.png

|

.. rubric:: Build(Cross Compile) fw\_printenv/fw\_setenv U-Boot Tool
   :name: buildcross-compile-fw_printenvfw_setenv-u-boot-tool

Please note that all paths are refereneced to the u-boot source within
the AMSDK, ti-sdk-am335x-<version>/board-support/u-boot<version>.....

Prior to building the The flag in
board-support/u-boot<version>/tools/envfw\_env.h “HAVE\_REDUND” must be
undefined as only a single env partition has been defined in the AMSDK
SPI MTD partitioning.

Please note that the CROSS\_COMPILE flag is not used by the u-boot
makefile here, the HOSTCC= variable must be set.

.. code-block:: console

   host# make HOSTCC=arm-arago-linux-gnueabi-gcc env

This command is issued from the top of the u-boot source directory.
Please be sure to see that the cross compiler was actually called and
not just gcc.

|

.. rubric:: Prepare configuration file for U-Boot Tool
   fw\_printenv/fw\_setenv
   :name: prepare-configuration-file-for-u-boot-tool-fw_printenvfw_setenv

After building the executable a configuration file must be created and
placed into a specific directory that is called in fw\_env.h in the
board-support/u-boot<version>/tools/env directory. The default location
for the configuration file (fw\_env.config) is /etc/.

|
| MTD device name Device offset Env. size Flash sector size (only the
  line below is needed in the file)

::

    /dev/mtd2               0x0000          0x2000          0x1000

|

.. rubric:: Load fw\_printenv/fw\_setenv into target file system
   :name: load-fw_printenvfw_setenv-into-target-file-system

This creates the executable fw\_printenv, this file must be copied into
the target file system, place in /sbin or the user’s directory.

You must copy fw\_printenv to fw\_setenv to be able to set variables.
The program detects the name it was called as and sets the context it
will run in.

|

.. rubric:: Test fw\_printenv/fw\_setenv tool
   :name: test-fw_printenvfw_setenv-tool

The executable fw\_printenv will dump the entire environment space,
individual variables can be read by:

.. code-block:: console

   root@<machine>:~# ./fw_printenv autoload

To set an environment variable use fw\_setenv . This example will set
the variable autoload to no, use fw\_printenv to read back the change.

.. code-block:: console

   root@<machine>:~# ./fw_setenv autoload no

