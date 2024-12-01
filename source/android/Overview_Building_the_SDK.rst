.. _android-building:

################
Building the SDK
################

**************
Build PC setup
**************

Please refer to the following pages from Android documentation to setup your environment for Android build:

-  `Android's Build
   requirements <https://source.android.com/setup/build/requirements>`__.
-  `Android's Establishing a Build
   Environment <https://source.android.com/setup/build/initializing>`__
   guide.


**Getting the repo tool**

You will need the ``repo`` tool to retrieve repositories.
To install it, please refer to this webpage : https://source.android.com/setup/develop#installing-repo

.. _android-download-aosp:

*******************
Downloading sources
*******************

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX')

    Create a folder for downloading all sources

    .. code-block:: console

       $ mkdir ~/10_01_00 && cd $_
       $ export YOUR_PATH=$PWD

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX')

    Fetch the code using ``repo``:

    .. code-block:: console

       $ mkdir ${YOUR_PATH}/ti-aosp-15 && cd $_
       $ repo init -u https://git.ti.com/git/android/manifest.git -b android15-release -m releases/RLS_10_01.xml
       $ repo sync

.. tip::

   By default the Android build contains **pre-built binaries** for both the kernel
   and the bootloaders.
   The pre-builts are located in in :file:`device/ti/am62x-kernel`
   and :file:`vendor/ti/am62x/bootloader` folder.

   To get the sources, refer to:

   - :ref:`android-download-kernel` for kernel
   - :ref:`android-download-bootloaders` for bootloaders

.. _android-build-aosp:

******************
Build Instructions
******************

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX')

   .. code-block:: console

      $ cd ${YOUR_PATH}/ti-aosp-15
      $ source build/envsetup.sh
      $ lunch <BUILD_TARGET>
      $ m
      [...]
      #### build completed successfully (49:14 (mm:ss)) ####

Where ``<BUILD_TARGET>`` is listed in the table below :

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    ============================= ============================
    Android Build type            Build target
    ============================= ============================
    AM62X-SK Tablet userdebug       ``am62x-userdebug``
    AM62X-SK Tablet user            ``am62x-user``
    AM62X-SK Car userdebug          ``am62x_car-userdebug``
    AM62X-SK Car user               ``am62x_car-user``
    ============================= ============================

    The recommended ``<BUILD_TARGET>`` to use is ``am62x-userdebug``.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

    ============================= ============================
    Android Build type            Build target
    ============================= ============================
    AM62PX-SK Tablet userdebug       ``am62p-userdebug``
    AM62PX-SK Tablet user            ``am62p-user``
    AM62PX-SK Car userdebug          ``am62p_car-userdebug``
    AM62PX-SK Car user               ``am62p_car-user``
    ============================= ============================

    The recommended ``<BUILD_TARGET>`` to use is ``am62p-userdebug``.

It's possible to customize the standard build (``m``), by passing build flags.
For example, the following enables AVB on userdebug builds:

.. code-block:: console

  $ TARGET_AVB_ENABLE=true m

The following build flags are available. **Default** values are **highlighted**.

.. list-table::
   :header-rows: 1

   * - Flag
     - Possible values
     - Description
   * - ``TARGET_AVB_ENABLE``
     - **false**/true
     - Forces AVB feature on userdebug
   * - ``TARGET_ADB_USER_ENABLE``
     - **false**/true
     - Forces enable ADB on user builds (**NOT for production builds**)
   * - ``TARGET_SDCARD_BOOT``
     - **false**/true
     - Boot from SD card instead of eMMC
   * - ``TARGET_KERNEL_USE``
     - **6.1**/6.6
     - Pick kernel version. 6.6 is experimental
   * - ``TARGET_BOOTLOADER_VERSION``
     - **unset**/2024.04
     - Pick U-Boot version (default: ``2023.04``). 2024.04 is experimental

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX')

   After building is complete, the necessary images will be available in
   :file:`${YOUR_PATH}/ti-aosp-15/out/target/product/am62*/`.

   To proceed to flash Android, see :ref:`android-flashing`.

   .. tip::

      As stated previously, Android build contains **pre-built binaries**
      for both the kernel and the bootloaders.
      These are ready to be used as-is with the EVM boards.
      For customization, it's possible to rebuild them.

      - See :ref:`android-build-kernel` for the kernel
      - See :ref:`android-build-bootloaders` for the bootloaders

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    The android images generated for the AM62X-SK EVM are compatible with the Beagle Play board.
    For flashing the Beagle Play, see the `dedicated application note`_.

    .. _dedicated application note: ../devices/AM62X/android/Application_Notes_BeaglePlay.html
