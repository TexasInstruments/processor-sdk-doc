.. http://processors.wiki.ti.com/index.php/Processor_SDK_Linux_Directory_Structure

************************************
Directory Structure Overview
************************************

The Processor SDK for Linux contains the following top-level
directories and files

.. ifconfig:: CONFIG_sdk in ('SITARA')

   .. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X')

      .. code-block:: console

         ./
         ├── bin/
         ├── board-support/
         ├── example-applications/
         ├── external-toolchain-dir/
         ├── filesystem/
         ├── licenses/
         ├── linux-devkit/
         ├── Makefile
         ├── makerules/
         ├── manifest/
         ├── Rules.make
         └── setup.sh*

   .. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X', 'AM57X', 'AM62LX')

      .. code-block:: console

         ./
         ├── bin/
         ├── board-support/
         ├── example-applications/
         ├── filesystem/
         ├── k3r5-devkit/
         ├── licenses/
         ├── linux-devkit/
         ├── Makefile
         ├── makerules/
         ├── manifest/
         ├── Rules.make
         └── setup.sh*

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      .. code-block:: console

         ./
         ├── bin/
         ├── board-support/
         ├── example-applications/
         ├── filesystem/
         ├── licenses/
         ├── linux-devkit/
         ├── Makefile
         ├── makerules/
         ├── manifest/
         ├── Rules.make
         └── setup.sh*

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

   .. ifconfig:: CONFIG_part_variant in ('AM57X')

      .. code-block:: console

         ./
         ├── bin/
         ├── board-support/
         ├── example-applications/
         ├── filesystem/
         ├── licenses/
         ├── linux-devkit/
         ├── Makefile
         ├── makerules/
         ├── manifest/
         ├── Rules.make
         ├── setup.sh*
         └── yocto-build/

   .. ifconfig:: CONFIG_part_variant not in ('AM57X')

      .. code-block:: console

         ./
         ├── bin/
         ├── board-support/
         ├── example-applications/
         ├── filesystem/
         ├── k3r5-devkit/
         ├── licenses/
         ├── linux-devkit/
         ├── Makefile
         ├── makerules/
         ├── manifest/
         ├── Rules.make
         ├── setup.sh*
         └── yocto-build/

These directories contain the code and tools used to develop for
Processor SDK devices.

-  **bin** - Contains the helper scripts for configuring the host system
   and target device. Most of these scripts are used by the setup.sh
   script.
-  **board-support** - Contains the SDK components that need to be
   modified when porting to a custom platform. This includes the kernel
   and boot loaders as well as any out of tree drivers.
-  **manifest** - Contains software manifest files
-  **licenses** - Contains software licenses
-  **example-applications** - Contains the sources for the TI provided
   example applications seen during the out-of-box demonstration.
-  **filesystem** - Contains the reference file systems. These include
   the smaller base file system as well as the full-featured SDK file
   system.

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM57X')

   -  **linux-devkit** - Contains the tools and libraries to speed
      development for the target device for the ARMV7 architechture

.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X')

   -  **external-toolchain-dir** - Contains the external ARM GNU toolchain
      to speed development for the target device for the ARMV7 architechture

.. ifconfig:: CONFIG_part_variant not in ('AM335X', 'AM437X', 'AM57X')

   -  **linux-devkit** - Contains the tools and libraries to speed
      development for the target device for the ARMV8 architechture

.. ifconfig:: CONFIG_part_variant not in ('AM62LX', 'AM57X')

   -  **k3r5-devkit** - Contains the tools and libraries to speed
      development for the target device for the ARMV7 architechture

-  **Makefile** - Provides build targets for many of the SDK components
   from the top-level of the SDK.
-  **makerules** - Make rules for all the topLevel Makefile build targets
-  **Rules.make** - Sets default values used by the top-level Makefile
   as well as sub-component Makefiles.
-  **setup.sh** - Configures the users host system as well as the target
   system for development.

.. ifconfig:: CONFIG_sdk in ('JACINTO','j7_foundational')

    -  **yocto-build** - This directory allows rebuilding SDK components and
       filesystem using yocto bitbake. Refer to `Building the SDK <Overview_Building_the_SDK.html>`__  section
       for more details on running yocto builds.
