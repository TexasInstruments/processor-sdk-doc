.. _pub_edgeai_sdk_development_flow:

====================
SDK development flow
====================

Processor SDK Linux for Edge AI comprises of 3 parts,

   - Edge AI Applications
   - Processor SDK - Linux
   - Processor SDK - RTOS

If you wish to work with just the **Edge AI Applications**, you can edit-build-run
directly on the target by flashing the etcher image as specified
in :ref:`pub_edgeai_prepare_sd_card`. **No need to build the RTOS binaries
as described below!**

If you are modifying any RTOS components such as vision_apps, tiovx, tidl,
tiadalg etc. you will need to rebuilt the RTOS binaries and update the SD card
filesystem with the latest. This requires the Processor SDK RTOS source package
and Processor SDK Linux filesystem packages.

If you are modifying any Linux DTBs, updating u-boot, updating system firmware (sysfw),
device driver and so on, you will need the Processor SDK Linux source package.

Getting PSDK RTOS
-----------------
You can download the latest Processor SDK RTOS for |__PART_FAMILY_NAME__| from the below links,

The Processor SDK RTOS source package:

``https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-bA0wfI4X2g/08.05.00.11/ti-processor-sdk-rtos-j721e-evm-08_05_00_11.tar.gz``

The Processor SDK Linux filesystem and BOOT partition files are also required:

``https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-U6uMjOroyO/08.05.00.08/boot-j7-evm.tar.gz``
``https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-U6uMjOroyO/08.05.00.08/tisdk-default-image-j7-evm.tar.xz``

Building the RTOS SDK from source
----------------------------------

Untar the ti-processor-sdk-rtos-j721e-evm-08_05_00_xx.tar.gz to some location
on PC and copy the tisdk-default-image-j7-evm.tar.xz and boot-j7-evm.tar.gz
into the RTOS SDK folder. Execute the ``setup_psdk_rtos.sh`` script from the
folder below. This will untar the linux filesystem, download GCC cross compile
toolchain and dependencies all in preparation to build the SDK

.. code-block:: bash

   #Run the setup script as shown
   <PSDK-RTOS path>#./psdk_rtos/scripts/setup_psdk_rtos.sh

Ensure that you are building only for the ``target`` and the profile is set to
``release`` mode. In the file ``<PSDK-RTOS path>/tiovx/build_flags.mak``
check for,

.. code-block:: bash

   # Build for SoC
   BUILD_TARGET_MODE?=yes
   # Build for x86 PC
   BUILD_EMULATION_MODE?=no
   # valid values: release debug all
   PROFILE?=release

Navigate to vision_apps folder and build the RTOS components

.. code-block:: bash

   <PSDK-RTOS path>/vision_apps#BUILD_EDGEAI=yes make sdk -j8

Once the build is complete with no errors install the Linux filesystem to
an SD card. A **minimum of 16GB** is highly recommended. Insert an SD card
and unmount its partitions. If you had previously installed using the same
SD card, you might have to unmount the BOOT and rootfs partitions

.. note::
   ``/dev/sda1`` and ``/dev/sda2`` are just examples here, and the SD card might
   be mounted differently on your system. Ensure that you are unmounting the
   correct partitions before reformatting the SD card!

.. code-block:: bash

   umount /dev/sda1
   umount /dev/sda2

Use the script to create required partitions and filesystem format. This will
create two partitions namely BOOT and rootfs

.. code-block:: bash

   <PSDK-RTOS path>#sudo ./psdk_rtos/scripts/mk-linux-card.sh /dev/sda

.. note::
   Follow the interactive menu (mostly press Y and Y) to correctly format the
   SD card for Linux boot. Once successfully complete, PLEASE EJECT THE SD CARD
   AND INSERT AGAIN. This ensures that files are not installed under root
   permissions and the following steps do not require sudo permissions

Use another script to install the filesystem to the rootfs partition

.. code-block:: bash

   <PSDK-RTOS path>#./psdk_rtos/scripts/install_to_sd_card.sh

Next transfer the RTOS component libraries, header files and remote core
binaries to the SD card.

.. code-block:: bash

   <PSDK-RTOS path>/vision_apps# BUILD_EDGEAI=yes make linux_fs_install_sd

- Installs the ``vision_apps.so`` library under ``/usr/lib``
- Copies the vision_apps headers under ``/usr/include/processor_sdk`` folder
- Copies the RTOS binaries under ``/usr/lib/firmware``

Getting PSDK LINUX
------------------

.. note::
   You can skip this step if you don't intend to change anything on the
   Linux kernel, u-boot or file-system

You can download the latest Processor SDK Linux for |__PART_FAMILY_NAME__| from the below link,

``https://dr-download.ti.com/software-development/software-development-kit-sdk/MD-U6uMjOroyO/08.05.00.08/ti-processor-sdk-linux-j7-evm-08_05_00_08-Linux-x86-Install.bin``

Please refer to `Processor SDK Linux documentation <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-jacinto7/08_05_00_08/exports/docs/linux/Overview/Download_and_Install_the_SDK.html>`_
for installation steps.


Building the LINUX SDK from source
----------------------------------

Please refer to `Simplified SDK Build <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-jacinto7/08_05_00_08/exports/docs/linux/Overview_Top_Level_Makefile.html>`_
for quick changes and build in u-boot, sysfw (system firmware) and linux kernel.

Please refer to `Building SDK with Yocto <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-jacinto7/08_05_00_08/exports/docs/linux/Overview_Building_the_SDK.html>`_
for building each individual components. This will require a longer time to build and a powerful machine.

** This completes the PSDK Linux and RTOS setup **

Applications setup
------------------

At this point the SD card is ready with Linux image and RTOS components.
Next we need to clone the target side components under SD card ``/opt``
If the provided steps are not executing you might have to provide permissions
for the scripts to make directory under SD card /opt.

.. note::
   You need to change permissions on SD card /opt folder NOT your Linux PC
   /opt folder. Change permissions of SD card /opt directory
   ``/media/<user-name>/rootfs# sudo chmod -R ugo+w opt``

First clone the ``edgeai-gst-apps`` repo into the SD card under ``/opt``

.. code-block:: bash

   /media/<user-name>/rootfs/opt#git clone --single-branch --branch master git://git.ti.com/edgeai/edgeai-gst-apps.git

Once edgeai-gst-apps is cloned, on the PC itself run the ``setup_script.sh``.
This will clone and install DL dependencies, clone the edgeai-gst-plugins and
edgeai-tiovx-modules repo on the SD card /opt.

.. code-block:: bash

   /media/<user-name>/rootfs/opt/edgeai-gst-apps#./setup_script.sh

Also download the recommended set of models or any model that you would like
to test by running the ``download_models.sh`` script.

.. code-block:: bash

   /media/<user-name>/rootfs/opt/edgeai-gst-apps#./download_models.sh --recommended

** This completes the setup required on PC side **

.. note::
   Before ejecting the SD card issue a 'sync' on the terminal to commit all
   changes.

Target side steps
-----------------
Boot the SK with the prepared SD card. Make sure you have connected the
camera and display. After boot, login as 'root' with no password. If you have
flashed the SD card using Balena etcher tool, then upon login you will notice
the wallpaper displayed on the screen disappears and comes back. The prompt will
also change to ``/opt/edgeai-gst-apps#``. This is done by automatically calling the
``init_script.sh``

If you are building from scratch, upon login you will notice that the wallpaper
is still displayed on the screen. The init_script.sh is not automatically
called during login. You will have to manually navigate to edgeai-gst-apps repo
and execute every time it boots or call it under .profile

.. code-block:: bash

   /opt/edgeai-gst-apps#source ./init_script.sh

Only for first time, you will have to run the setup_script.sh once again. This time
it will not download the dependencies but compile and install the edgeai-gst-plugins,
edgeai-tiovx-modules, edgeai-dl-inferer and apps_cpp demos.

For more information about what init_script does, visit :ref:`init_script <pub_edgeai_getting_started_init_script>`

**Now you are ready to run the Python and C++ demos!**
