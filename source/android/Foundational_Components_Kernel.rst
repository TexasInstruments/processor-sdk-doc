##############
Android Kernel
##############

Android is built around a Linux kernel. By default, Android's
``boot.img`` is build from a binary kernel Image located in:

.. code-block:: text

   ${YOUR_PATH}/ti-aosp-16/device/ti/am62x-kernel/kernel/6.12

This guide describes how to rebuild and customize a Linux kernel for
Android.

.. _android-download-kernel:

*******************
Downloading sources
*******************

Fetch the code using ``repo``:

.. code-block:: console

   $ mkdir ${YOUR_PATH}/ti-kernel-aosp/ && cd $_
   $ repo init -u https://git.ti.com/git/android/manifest.git -b android16-release -m releases/RLS_11_00_01_Kernel.xml
   $ repo sync

.. tip::

   To save some disk space, pass the ``--depth=1`` option to ``repo init``:

   .. code-block:: console

      $ repo init -u https://git.ti.com/git/android/manifest.git -b android16-release -m releases/RLS_11_00_01_Kernel.xml --depth=1

.. _android-build-kernel:

******************
Build Instructions
******************

In this section, we will assume that we already have an Android source
tree which has been fully build and is located in:

.. code-block:: text

   ${YOUR_PATH}/ti-aosp-16/

Building everything from scratch
================================

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    The kernel is compatible with all AM62x boards, such as the SK EVM and the Beagle Play.

.. code-block:: console

   $ cd ${YOUR_PATH}/ti-kernel-aosp/
   $ export DIST_DIR=${YOUR_PATH}/ti-aosp-16/device/ti/am62x-kernel/kernel/6.12
   $ ./tools/bazel run --config=ti //private/devices/ti/am6x:ti_dist -- --destdir=$DIST_DIR

Re-running this command will rebuild incrementally.

Android uses Kleaf, a Bazel-based build system to build the kernel.
AOSP documentation can be found `here <https://source.android.com/docs/setup/build/building-kernels?hl=fr>`__ and
Kleaf documentation `here  <https://android.googlesource.com/kernel/build/+/refs/heads/main/kleaf/README.md>`__

.. attention::

   Kernel builds hangs when using the ``btrfs`` file system.
   This is a known issue according to the `kleaf documentation <https://android.googlesource.com/kernel/build/+/refs/heads/main/kleaf/docs/errors.md#build-hangs-on-btrfs>`_
   Make sure to pass the ``--workaround_btrfs_b292212788`` flag to bazel when using ``btrfs``.


Defconfig/menuconfig changes
============================

The usual (``make menuconfig``) is done via ``bazel`` command :

.. code-block:: console

   $ cd ${YOUR_PATH}/ti-kernel-aosp/
   $ tools/bazel run --config=ti //private/devices/ti/am6x:ti_config -- menuconfig

This will automatically update the :file:`private/devices/ti/am6x/ti.fragment`.

.. note::

   Users must have built the android kernel image prior to building the Android file system.
   Otherwise pre-built kernel images present in :file:`device/ti/am62x-kernel`
   will be used to create :file:`boot.img`


Rebuild Android images
======================

We should re-generate the Android images to include the newly build kernel.
Follow the Android :ref:`android-build-aosp` to do so.

*********************
Flashing instructions
*********************

In order to flash a new kernel, several images should be flashed:

.. code-block:: console

   $ adb reboot fastboot
   < Wait for fastbootd reboot >

   $ cd <PATH/TO/IMAGES>
   $ fastboot flash boot boot.img --disable-verity
   $ fastboot flash vendor_boot vendor_boot.img --disable-verity
   $ fastboot flash vendor_dlkm vendor_dlkm.img --disable-verity
   $ fastboot reboot

The board should boot with the new kernel.

********************
Enabling new drivers
********************

Since the kernel is based on the
`Generic Kernel Image <https://source.android.com/docs/core/architecture/kernel/generic-kernel-image>`_,
new drivers should always be added as **modules**.

To enable new modules:

   #. Run ``menuconfig`` as documented previously, Select ``=m`` for the driver.

   #. Edit :file:`${YOUR_PATH}/ti-kernel-aosp/private/ti/device/am6x/BUILD.bazel` to add your new module.
      Look for the following sections:

      .. code-block:: bazel

         TI_IN_TREE_MODULES = [
             # keep sorted
             "crypto/crc64_iso3309_generic.ko",
             "drivers/char/hw_random/optee-rng.ko",
             "drivers/clk/keystone/sci-clk.ko",
             ...
         ]

         TI_VENDOR_DLKM_MODULES = [
             # keep sorted
             "am65-cpts.ko",
             "cc33xx.ko",
             "cdns-usb-common.ko",
             ...
         ]

   #. Add your new kernel module to the appropriate array:

      - **TI_IN_TREE_MODULES**: For in-tree kernel modules. Use the full path from kernel root (e.g., ``"drivers/your_driver/your_module.ko"``)
      - **TI_VENDOR_DLKM_MODULES**: For vendor-specific dynamically loadable kernel modules. Use only the module filename (e.g., ``"your_module.ko"``)

      Keep the list sorted alphabetically.

   #. Rebuild the kernel as documented in :ref:`android-build-kernel`.

   #. Finally, rebuild the Android images.

********************
Device tree overlays
********************

Mapping ``adtbo_idx`` with filenames
====================================

Device tree overlays can be used to configure additional hardware peripherals.
These overlays are stored in the :file:`dtbo.img`. This image is generated when
building the Android kernel as documented in :ref:`android-build-kernel`.

As listed in :ref:`android-dtbo`, we can configure an overlay to be applied
from U-Boot by setting the ``adtbo_idx`` variable.

To view how the ``adtbo_idx`` maps with the dtbo file, we can inspect the :file:`BUILD.bazel`
from the `kernel source code <https://git.ti.com/cgit/android/kernel-ti-device/tree/BUILD.bazel?h=ti-android-linux-6.12.y>`__.
Looking at the ``TI_DTBOS`` array, we can see:

.. code-block:: bazel

   TI_DTBOS = [
       "k3-am62x-sk-hdmi-audio.dtbo",
       "k3-am62x-sk-csi2-ov5640.dtbo",
       "k3-am62x-sk-csi2-tevi-ov5640.dtbo",
       "k3-am625-sk-microtips-mf101hie-panel.dtbo",
       "k3-am62x-sk-lpm-wkup-sources.dtbo",
       "k3-am62-lp-sk-microtips-mf101hie-panel.dtbo",
       "k3-am625-beagleplay-csi2-ov5640.dtbo",
       "k3-am625-beagleplay-csi2-tevi-ov5640.dtbo",
       "k3-am625-beagleplay-lincolntech-lcd185-panel.dtbo",
       "k3-am62p5-sk-mcan.dtbo",
       "k3-am62p5-sk-microtips-mf101hie-panel.dtbo",
       "k3-am625-sk-m2-cc3351.dtbo",
       "k3-am62p5-sk-m2-cc3351.dtbo",
       "k3-am625-sk-wl1837.dtbo",
       "k3-am62p5-sk-dsi-rpi-7inch-panel.dtbo",
       "k3-j722s-evm-csi2-quad-rpi-cam-imx219.dtbo",
       "k3-j722s-evm-csi2-quad-tevi-ov5640.dtbo",
       "k3-j722s-evm-dsi-rpi-7inch-panel.dtbo",
       "k3-j722s-evm-fpdlink-fusion.dtbo",
   ]

The ``TI_DTBOS`` array order dictates the index. For example:

.. list-table::
   :header-rows: 1

   * - filename
     - index

   * - :file:`k3-am62x-sk-hdmi-audio.dtbo`
     - 0

   * - :file:`k3-am62x-sk-csi2-ov5640.dtbo`
     - 1

   * - :file:`k3-am62x-sk-csi2-tevi-ov5640.dtbo`
     - 2

   * - :file:`k3-am625-sk-microtips-mf101hie-panel.dtbo`
     - 3

   * - :file:`k3-am62x-sk-lpm-wkup-sources.dtbo`
     - 4


Adding more :file:`.dtbo` files to the :file:`dtbo.img`
=======================================================

In this section, we will see how to add more :file:`.dtbo` files to the :file:`dtbo.img`.

   #. Edit :file:`${YOUR_PATH}/ti-kernel-aosp/private/ti/device/am6x/BUILD.bazel`.
      Look for the ``TI_DTBOS`` array and add your new dtbo file:

      .. code-block:: bazel

         TI_DTBOS = [
             "k3-am62x-sk-hdmi-audio.dtbo",
             "k3-am62x-sk-csi2-ov5640.dtbo",
             ...
             "your-new-overlay.dtbo",  # Add your new dtbo here
         ]

      .. important::

         Make sure to add it at the **end** of the array. The order in ``TI_DTBOS`` will determine
         the ``adtbo_idx`` to be used.

   #. Rebuild the kernel as documented in :ref:`android-build-kernel`.
