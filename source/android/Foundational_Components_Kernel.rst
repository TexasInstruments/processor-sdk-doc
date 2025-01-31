##############
Android Kernel
##############

Android is built around a Linux kernel. By default, Android's
``boot.img`` is build from a binary kernel Image located in:

.. code-block:: text

   ${YOUR_PATH}/ti-aosp-15/device/ti/am62x-kernel/kernel/6.6

This guide describes how to rebuild and customize a Linux kernel for
Android.

.. _android-download-kernel:

*******************
Downloading sources
*******************

Fetch the code using ``repo``:

.. code-block:: console

   $ mkdir ${YOUR_PATH}/ti-kernel-aosp/ && cd $_
   $ repo init -u https://git.ti.com/git/android/manifest.git -b android15-release -m releases/RLS_10_01_Kernel-6.6.xml
   $ repo sync

.. tip::

   To save some disk space, pass the ``--depth=1`` option to ``repo init``:

   .. code-block:: console

      $ repo init -u https://git.ti.com/git/android/manifest.git -b android15-release -m releases/RLS_10_01_Kernel-6.6.xml --depth=1

.. _android-build-kernel:

******************
Build Instructions
******************

In this section, we will assume that we already have an Android source
tree which has been fully build and is located in:

.. code-block:: text

   ${YOUR_PATH}/ti-aosp-15/

Building everything from scratch
================================

.. ifconfig:: CONFIG_part_variant in ('AM62X')

    The kernel is compatible with all AM62x boards, such as the SK EVM and the Beagle Play.

.. code-block:: console

   $ cd ${YOUR_PATH}/ti-kernel-aosp/
   $ export TARGET_KERNEL_USE="6.6"
   $ export DIST_DIR=${YOUR_PATH}/ti-aosp-15/device/ti/am62x-kernel/kernel/${TARGET_KERNEL_USE}
   $ tools/bazel run //common:ti_dist -- --dist_dir=$DIST_DIR

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
   $ tools/bazel run //common:ti_config -- menuconfig

This will automatically update the :file:`arch/arm64/configs/ti_gki.fragment`.

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
   $ fastboot flash boot boot.img
   $ fastboot flash vendor_boot vendor_boot.img
   $ fastboot flash vendor_dlkm vendor_dlkm.img
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

   #. Edit :file:`${YOUR_PATH}/ti-kernel-aosp/BUILD.bazel` to add your new module.
      Look for the following section:

      .. code-block:: bazel

         _TI_MODULE_OUTS = [
             # keep sorted
             "crypto/af_alg.ko",
             "crypto/algif_hash.ko",

   #. In the ``_TI_MODULE_OUTS`` array, add the path to your new kernel module.

   #. Rebuild the kernel as documented in :ref:`android-build-kernel`.

   #. If the driver module needs to be loaded early (in the ramdisk), edit
      :file:`${YOUR_PATH}/ti-aosp-15/device/ti/am62x/BoardConfig-common.mk`
      and add the path to your module:

      .. code-block:: make

         BOARD_VENDOR_RAMDISK_KERNEL_MODULES += \
                 device/ti/am62x-kernel/kernel/$(TARGET_KERNEL_USE)/your_module.ko

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
from the `kernel source code <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/BUILD.bazel?h=ti-android-linux-6.6.y#n953>`__.
Looking at the ``kernel_images()`` macro, we can see:

.. code-block:: bazel

   kernel_images(
    name = "ti_images",
    build_dtbo = True,
    build_initramfs = True,
    dtbo_srcs = [
        ":ti/k3-am62x-sk-hdmi-audio.dtbo",
        ":ti/k3-am62x-sk-csi2-ov5640.dtbo",
        ":ti/k3-am62x-sk-csi2-tevi-ov5640.dtbo",
        ":ti/k3-am625-sk-microtips-mf101hie-panel.dtbo",
        ":ti/k3-am62x-sk-lpm-wkup-sources.dtbo",
        ":ti/k3-am62-lp-sk-microtips-mf101hie-panel.dtbo",
        ":ti/k3-am625-beagleplay-csi2-ov5640.dtbo",
        ":ti/k3-am625-beagleplay-csi2-tevi-ov5640.dtbo",
        ":ti/k3-am625-beagleplay-lincolntech-lcd185-panel.dtbo",
        ":ti/k3-am62p5-sk-mcan.dtbo",
        ":ti/k3-am62p5-sk-microtips-mf101hie-panel.dtbo",
        ":ti/k3-am625-sk-m2-cc3301.dtbo",
        ":ti/k3-am62p5-sk-m2-cc3301.dtbo",
        ":ti/k3-am625-sk-wl1837.dtbo",

The ``dtbo_srcs`` array order dicates the index. For example:

.. list-table::
   :header-rows: 1

   * - filename
     - index

   * - :file:`ti/k3-am62x-sk-hdmi-audio.dtbo`
     - 0

   * - :file:`ti/k3-am62x-sk-csi2-ov5640.dtbo`
     - 1


Adding more :file:`.dtbo` files to the :file:`dtbo.img`
=======================================================

In this section, we will see how to add more :file:`.dtbo` files to the :file:`dtbo.img`.
Let's see how to add :file:`ti/k3-am62p5-sk-dsi-rpi-7inch-panel.dtbo` for example:

   #. Edit :file:`${YOUR_PATH}/ti-kernel-aosp/BUILD.bazel`.
      Look for the following section:

      .. code-block:: bazel

         kernel_build(
             name = "ti",
             outs = [
                 "Image",
                 "System.map",
                 "k3-am62-lp-sk.dtb",
                 "k3-am62-lp-sk-microtips-mf101hie-panel.dtbo",

   #. In the ``kernel_build()`` section, add ``k3-am62p5-sk-dsi-rpi-7inch-panel.dtbo`` to the ``outs`` array.

   #. Still in ``kernel_build()``, look for the ``make_goals`` array and add ``ti/k3-am62p5-sk-dsi-rpi-7inch-panel.dtbo``.

   #. Now look for the following section:

      .. code-block:: bazel

         kernel_images(
             name = "ti_images",
             build_dtbo = True,
             build_initramfs = True,
             dtbo_srcs = [
                 ":ti/k3-am62x-sk-hdmi-audio.dtbo",
                 ":ti/k3-am62x-sk-csi2-ov5640.dtbo",
                 ":ti/k3-am62x-sk-csi2-tevi-ov5640.dtbo",

   #. In the ``kernel_images()``, add ``:ti/k3-am62p5-sk-dsi-rpi-7inch-panel.dtbo`` at the end of the array.

      .. important::

         Make sure to add the it at the **end** of the array. The order in ``dtbo_srcs`` will determine
         the ``adtbo_idx`` to be used.

   #. Rebuild the kernel as documented in :ref:`android-build-kernel`.
