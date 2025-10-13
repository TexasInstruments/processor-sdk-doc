.. _Application_Notes_Android_Secure_Build:

#####################################
Android Secure Build Application Note
#####################################

This page describes how to setup secure Android build.

The process is an example, feel free to adapt following your needs.

.. warning::

   This process is only supported with Android user images

Fetching Bootloader, Kernel, and Android
----------------------------------------

- Bootloaders:

   .. code-block:: console

      $ export YOUR_PATH=~/src/
      $ mkdir ${YOUR_PATH}/ti-bootloader-aosp/ && cd $_
      $ repo init -u https://git.ti.com/git/android/manifest.git -b android16-release -m releases/RLS_11_00_Bootloader.xml
      $ repo sync

- Kernel:

   .. code-block:: console

      $ mkdir ${YOUR_PATH}/ti-kernel-aosp/ && cd $_
      $ repo init -u https://git.ti.com/git/android/manifest.git -b android16-release -m releases/RLS_11_00_Kernel.xml
      $ repo sync

- Android:

   .. code-block:: console

      $ export YOUR_PATH=~/src/
      $ mkdir ${YOUR_PATH}/ti-aosp-16 && cd $_
      $ repo init -u https://git.ti.com/git/android/manifest.git -b android16-release -m releases/RLS_11_00.xml
      $ repo sync

Build Secure Bootloaders
------------------------

- Generate TA cryptographic keys:

   .. code-block:: console

      $ cd ${YOUR_PATH}/ti-bootloader-aosp/build
      $ ./secure.sh generate_ta_keys
      $ ls -1 .keys/
      ta.key
      ta_pub.key

- Generate AVB public/private keys:

   .. code-block:: console

      $ cd ${YOUR_PATH}/ti-bootloader-aosp/build
      $ ./secure.sh generate_avb_keys
      $ ls -1 .keys/
      avb.key
      avb_pub.key

That will generate ``avb.key`` and  ``avb_pub.key`` under ``build/.keys``.

The bootloaders scripts will detect that ``avb_pub.key`` is present and will include it into U-Boot.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   The user can also specify the absolute path of the avb_pub key in yaml config (``build/config/boards/am62x-sk.yaml``):

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   The user can also specify the absolute path of the avb_pub key in yaml config (``build/config/boards/am62p-sk.yaml``):

.. ifconfig:: CONFIG_part_variant in ('AM67A')

   The user can also specify the absolute path of the avb_pub key in yaml config (``build/config/boards/am67a-evm.yaml``):

.. code-block:: yaml

   secure:
     avb_pub_key: ${YOUR_PATH}/ti/avb_pub.key

.. table:: Security Keys

   +---------------------+-----------------------------------------------------------------------------+
   | Key                 | Description                                                                 |
   +=====================+=============================================================================+
   | ``avb.key``         | (Optional) Private key used by Android to sign images                       |
   +---------------------+-----------------------------------------------------------------------------+
   | ``avb_pub.key``     | (Optional) Public key used by U-Boot to verify Android images               |
   +---------------------+-----------------------------------------------------------------------------+
   | ``ta.key``          | (Optional) Private key used to sign Trusted Application (OP-TEE)            |
   +---------------------+-----------------------------------------------------------------------------+
   | ``ta_pub.key``      | (Optional) Public key used to sign Trusted Application (OP-TEE)             |
   +---------------------+-----------------------------------------------------------------------------+


Build and copy secure images to Android:

.. code-block:: console

   $ ./build/release_android.sh --aosp=~${YOUR_PATH}/ti-aosp-16 --mode=factory

.. warning::

   By default on factory mode, OP-TEE is built with this flag:

   - ``CFG_RPMB_WRITE_KEY``:

     This flag configure the RPMB if this one is not initialized yet.

     This operation is performed one time only, once the RPMB is initialized with the key we cannot override it anymore.

.. note::

    **RPMB corruptions**:

    If we do several flashes with different builds, we may be faced with RPMB corruptions.
    Indeed some metadata are stored in the RPMB and by default if there is a mismatch OP-TEE fails to load Trusted Applications.
    Thus the OP-TEE keymaster service fails and the device doesn't boot.
    To avoid this situation we can add the flag ``CFG_REE_FS_ALLOW_RESET=y`` in `build_optee.sh`:

        Allow secure storage in the REE FS to be entirely deleted without causing anti-rollback errors.
        This is used to reset the secure storage to a clean, empty state.

    **Testing Case**:

    If you want to test and be sure to reuse RPMB partition you can set ``CFG_RPMB_TESTKEY=y`` in `build_optee.sh`:

        OP-TEE can either embed a built-in RPMB key or derive it from platform specific secrets.
        The former case might be useful during development while the later is recommended for production devices.

Copy ``avb.key`` in Android:

.. code-block:: console

   $ cd ${YOUR_PATH}/ti-bootloader-aosp/build
   $ cp .keys/avb.key "${YOUR_PATH}/ti-aosp-16/device/ti/am62x/"

Replace the following configs in ``device/ti/am62x/BoardConfigCommon.mk``::

   BOARD_AVB_ALGORITHM := SHA256_RSA4096
   BOARD_AVB_KEY_PATH := device/ti/am62x/avb.key
   BOARD_AVB_BOOT_KEY_PATH := device/ti/am62x/avb.key
   BOARD_AVB_INIT_BOOT_KEY_PATH := device/ti/am62x/avb.key
   BOARD_AVB_VBMETA_VENDOR_DLKM_KEY_PATH := device/ti/am62x/avb.key
   BOARD_AVB_VBMETA_SYSTEM_DLKM_KEY_PATH := device/ti/am62x/avb.key


Check images generated in Android:

.. code-block:: console

   $ cd ~${YOUR_PATH}/ti-aosp-16
   $ git status


Build Kernel
------------

Before building Kernel we need to modify it to support RPMB features.

Download patch : :download:`RPMB_enabling.patch <patches/RPMB_enabling.patch>` and put it ``${YOUR_PATH}/ti-kernel-aosp/common`` folder.

Update symbol list and build kernel:

.. code-block:: console

   $ cd ${YOUR_PATH}/ti-kernel-aosp/common
   $ git am RPMB_enabling.patch
   $ cd ${YOUR_PATH}/ti-kernel-aosp/
   $ export DIST_DIR=${YOUR_PATH}/ti-aosp-16/device/ti/am62x-kernel/kernel/6.12
   $ ./update_symbol_list.sh -d ti -b private/devices/ti/am6x
   $ ./tools/bazel run --config=ti //private/devices/ti/am6x:ti_dist -- --destdir=$DIST_DIR

Build Android
-------------

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. code-block:: console

      $ cd ${YOUR_PATH}/ti-aosp-16
      $ source build/envsetup.sh
      $ lunch am62x-bp2a-user

      $ export FACTORY_BUILD=true
      $ m -j$(nproc)                # OR nice -n19 build/soong/soong_ui.bash --make-mode -j$(nproc)

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. code-block:: console

      $ cd ${YOUR_PATH}/ti-aosp-16
      $ source build/envsetup.sh
      $ lunch am62p-bp2a-user

      $ export FACTORY_BUILD=true
      $ m -j$(nproc)                # OR nice -n19 build/soong/soong_ui.bash --make-mode -j$(nproc)

.. ifconfig:: CONFIG_part_variant in ('AM67A')

   .. code-block:: console

      $ cd ${YOUR_PATH}/ti-aosp-16
      $ source build/envsetup.sh
      $ lunch am67a-bp2a-user

      $ export FACTORY_BUILD=true
      $ m -j$(nproc)                # OR nice -n19 build/soong/soong_ui.bash --make-mode -j$(nproc)

Flash Android
-------------

To reflash on a device which already has Android installed, run:

Reboot to U-Boot

.. code-block:: console

   $ adb reboot bootloader

Flash using the script: in a different terminal,

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   change directory to ``out/target/product/am62x`` and run the ``flashall.sh`` script:

   .. code-block:: console

      # for AM62x SK EVM (GP)
      $ sudo ./flashall.sh --board am62x-sk

      # for AM62x SK EVM (HS-FS)
      $ sudo ./flashall.sh --board am62x-sk --hsfs

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   change directory to ``out/target/product/am62p`` and run the ``flashall.sh`` script:

   .. code-block:: console

      # for AM62P SK EVM
      $ sudo ./flashall.sh --board am62px-sk

.. ifconfig:: CONFIG_part_variant in ('AM67A')

   change directory to ``out/target/product/am67a`` and run the ``flashall.sh`` script:

   .. code-block:: console

      # for AM67A EVM
      $ sudo ./flashall.sh --board am67a-evm

.. warning::

   **Device Locking and Unlock Capability**

   After flashing with secure build, the device will be locked and ``fastboot flashing unlock`` commands will be disabled by default.

   To enable unlock capability, you have several options:

   **Option 1: Enable at compile time**

   Set the U-Boot environment variable before compilation:

   .. code-block:: console

      fastboot.unlock_ability=1

   **Option 2: Enable at runtime**

   Set the U-Boot environment variable in the console (note that ``saveenv`` is disabled in factory mode, so these settings will be lost at each reboot):

   .. code-block:: console

      => setenv fastboot.unlock_ability 1

   **Unlock Process**

   When running ``fastboot flashing unlock`` or ``fastboot flashing unlock_critical``, the system will prompt for confirmation in the console. To bypass this confirmation prompt, you can set (these settings will also be lost at each reboot):

   .. code-block:: console

      => setenv fastboot.unlock_confirm 1
      => setenv fastboot.unlock_critical_confirm 1
