###########################
Building Buildroot Packages
###########################

This document provides a step-by-step guide to building a Buildroot package.
There are two ways you can build a package in buildroot.

- Add existing Buildroot Packages
- Add custom Packages

**********************************
Adding Existing Buildroot Packages
**********************************

Set Up Your Environment
=======================

Ensure you have the Buildroot repository and the buildroot-external-TI tree set up
as described here :ref:`set-up-the-external-tree`.

Enable Packages in the Buildroot Configuration
==============================================

Run make menuconfig to enable the packages you have added in the Buildroot configuration.

.. code-block:: console

    $ make menuconfig

.. figure:: /images/buildroot_menuconfig.png
    :height: 600
    :width: 800

Navigate to the relevant package categories and enable the desired packages.
For **nano** and :command:`htop`, you would typically find them under the Target packages menu.

#. Go to Target packages.
#. Navigate to *Text editors and viewers* and enable **nano**.
#. Navigate to *System tools* and enable :command:`htop`.
#. Save and exit the menuconfig interface.

Build the Image
===============

With the packages configured, you can now build the image. Buildroot will download,
compile, and include the specified packages in the build process.

.. code-block:: console

    $ make

The build process can take some time, depending on your system's resources and
the complexity of the configuration.

Verify the Packages
===================

After the build process is complete, verify that the packages are included in the
output image. You can check the presence of the package binaries in the root
filesystem.

.. code-block:: console

    $ find output/target -name nano
    $ find output/target -name htop

You should see the paths to your package binaries, indicating that they were
successfully included in the build.

By following these steps, you can add existing Buildroot packages. This approach
allows you to leverage the extensive package repository of Buildroot.

**********************
Adding Custom Packages
**********************

Set Up Your Environment
=======================

Ensure you have the Buildroot repository and the buildroot-external-TI tree
set up as described here :ref:`set-up-the-external-tree`.

Understand the Package Directory Structure
==========================================

In Buildroot, packages are typically organized into categories under the
:file:`package/directory`. When using an external tree, you can add new packages
under the :file:`package/directory` of the external tree.

Create the Package Directory
============================

Inside the buildroot-external-TI directory, create a new directory for your package.
For example, if you want to add a package named myapp:

.. code-block:: console

    $ cd buildroot-external-TI/
    $ mkdir -p package/myapp

Create the Package Files
========================

In the myapp directory, you need to create several files:

- Config.in: Describes the configuration options for the package.
- myapp.mk: Contains the build instructions for the package.

Example Config.in:

.. code-block:: console

    config BR2_PACKAGE_MYAPP
    bool "myapp"
    help
      MyApp is an example application.

Example myapp.mk

.. code-block:: console

    MYAPP_VERSION = 1.0
    MYAPP_SITE = http://example.com/downloads
    MYAPP_SOURCE = myapp-$(MYAPP_VERSION).tar.gz

    define MYAPP_BUILD_CMDS
    $(MAKE) -C $(@D)
    endef

    define MYAPP_INSTALL_TARGET_CMDS
    $(INSTALL) -D -m 0755 $(@D)/myapp $(TARGET_DIR)/usr/bin/myapp
    endef

    $(eval $(generic-package))

Add the Package to Buildroot Configuration
==========================================

Edit the Config.in file in the buildroot-external-TI directory to include your
new package. Add the following line:

.. code-block:: console

    $ source "$BR2_EXTERNAL_TI_PATH/package/myapp/Config.in"

Also edit external.mk to include package mk file

.. code-block:: console

   $ include $(sort $(wildcard $(BR2_EXTERNAL_TI_PATH)/package/*/*.mk))

Enable the Package in the Configuration
=======================================

Run make menuconfig in the buildroot directory to enable your new package in the
Buildroot configuration.

.. code-block:: console

    $ cd buildroot/
    $ make menuconfig

Navigate to your package in the External Options menu and enable it. Save and exit
the menuconfig interface.

.. figure:: /images/buildroot_custom_package.png
    :height: 600
    :width: 800

Build the Package
=================

With your package configuration set, build the image. Buildroot will download,
compile, and include your new package in the build process.

.. code-block:: console

    $ make

Verify the Package
==================

After the build process completes, verify that your package is included in the
output image. You can check the presence of your package's binaries in the root
filesystem.

.. code-block:: console

    $ find output/target -name myapp

You should see the path to your package's binary, indicating that it was
successfully included in the build.

By following these steps, you can add and build custom packages in Buildroot using
the buildroot-external-TI tree. This method provides a structured way to extend
the functionality of Buildroot-based systems while keeping customizations organized
and separate from the main Buildroot source.

For more detailed information and advanced package options, refer to the Buildroot
manual. `Buildroot manual <https://buildroot.org/downloads/manual/manual.html>`__.
