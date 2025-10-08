.. _android-csi-camera:

##############
Android Camera
##############

The AM62x supports 2 camera interfaces:

1. UVC (Usb Video Class) cameras, which are mainly known as webcams.
2. Camera over CSI-2

This page will mainly describe Camera over CSI-2.

.. note::

   Right now, only one YUV sensor is supported: The *Omnivision OV5640*.

**************
Hardware setup
**************

The following hardware is required to use the CSI-2 camera:

- ALINX ov5640 sensor module (AN5641)

  .. image:: ../../../images/alinx_ov5640.jpg
    :width: 300
    :alt: alinx_ov5640

- 15 pin FPC ribbon

  .. image:: ../../../images/15_pin_fpc_ribbon.jpg
    :width: 600
    :alt: 15_pin_fpc_ribbon.jpg

- AM62x SK EVM board

  .. image:: ../../../images/am62x_sk_evm_front.jpg
    :width: 600
    :alt: am62x_sk_evm_front.jpg

  .. image:: ../../../images/am62x_sk_evm_back.jpg
    :width: 600
    :alt: am62x_sk_evm_back.jpg

Plug the 15 pin FPC ribbon in ``J19`` and on the camera module as following:

  .. image:: ../../../images/am62x_sk_evm_with_ov5640.jpg
    :width: 600
    :alt: am62x_sk_evm_with_ov5640.jpg

**********************
Software configuration
**********************

After flashing, make sure to halt in the U-Boot shell and run

.. code-block:: console

   => env set adtbo_idx 1
   => saveenv
   => reset

This ensures that the :file:`k3-am62x-sk-csi2-ov5640.dtbo` device-tree overlay gets
applied by the bootloader.
With the applied overlay, the following drivers should probe:

- ``ov5640``, which is the *sensor* driver
- ``cdns-csi2rx`` which is the *receiver* (CSI2RX) driver
- ``j721e-csi2rx`` which is a TI-specific glue between ``cdns-csi2rx`` and the DMA engine (SHIM)

Once booted to the home screen, we can start a capture session using the
default AOSP provided camera app:

.. code-block:: console

   $ adb shell 'am start -a android.media.action.IMAGE_CAPTURE'

**************
Debugging tips
**************

Using the ``cam`` commandline
=============================

``cam`` is a commandline utility to do low level captures and save them to disk.

Some useful ``cam`` commands are:

.. code-block:: console

   $ adb wait-for-device root && adb wait-for-device

   # get information about streams and formats
   $ adb shell 'cam --camera 1 --info'

   # take a 1920x1080 capture in yuyv
   $ adb shell 'cam -c1 -C1 -s pixelformat=YUYV --file=/data/'

   # pull it from the device and convert it to png using ffmpeg
   $ adb pull '/data/frame-cam0-stream0-000000.bin'
   $ ffmpeg -f rawvideo -s 1920x1080 -pix_fmt yuyv422 -i frame-cam0-stream0-000000.bin picture.png

Since the Android HAL has exclusive access to the camera, the camera app should
not be running when we try to run a capture with ``cam``.

Enabling additional kernel logs
===============================

``v4l2`` has its own logging system. To have additional logs in ``dmesg``, do the following:

.. code-block:: console

   $ adb wait-for-device root && adb wait-for-device

   $ adb shell 'echo 0x3f > /sys/class/video4linux/video0/dev_debug'
   $ adb shell 'echo 1 > /sys/module/videobuf2_common/parameters/debug'

Android specific tricks
=======================

List cameras from Android system
--------------------------------

To list if the camera is enumerated by the Android system, run:

.. code-block:: console

   $ adb shell 'dumpsys media.camera'

Logging
-------

To filter logs from logcat, use:

.. code-block:: console

   $ adb logcat | grep -i -e libcamera -e 'F DEBUG';

To change the log level for libcamera, edit the HAL's :file:`init.rc`

.. code-block:: diff

   diff --git a/camera/android.hardware.camera.provider@2.5-service_64_am62x.rc b/camera/android.hardware.camera.provider@2.5-service_64_am62x.rc
   index 4808aea8dcee..f4637d7213a8 100644
   --- a/camera/android.hardware.camera.provider@2.5-service_64_am62x.rc
   +++ b/camera/android.hardware.camera.provider@2.5-service_64_am62x.rc
   @@ -16,5 +16,5 @@ service vendor.camera-provider-2-5 /vendor/bin/hw/android.hardware.camera.provid
        capabilities SYS_NICE
        task_profiles CameraServiceCapacity MaxPerformance
        override
   -    setenv LIBCAMERA_LOG_LEVELS *:INFO
   +    setenv LIBCAMERA_LOG_LEVELS *:DEBUG
        setenv LIBCAMERA_LOG_FILE syslog

The Camera app disappears after booting Android
-----------------------------------------------

The Android Camera app runs on the first Android boot to detect whether
a physical camera sensor is present and useable by the device. If it
can't find one, it will disable itself and thus disappear from the
launcher.

To re-enable it, use package manager via ``adb``:

.. code-block:: console

   $ adb root
   $ adb shell pm enable com.android.camera2/com.android.camera.CameraLauncher
