.. include:: _CSI2RX_common.rst

.. _enabling-camera-sensors:

***********************
Enabling camera sensors
***********************

|__PART_FAMILY_NAME__| SK supports the following 15-pin FFC compatible
camera modules with **OV5640** sensor:

Arducam V3Link (Fusion Mini) board can also be used to connect these camera modules to SK-AM62P over FPDLink cable.

   1. TEVI-OV5640-\*-RPI
   2. Digilent PCam5C
   3. ALINX AN5641

They can be tested with the following steps:

Applying sensor overlays
========================

During bootup stop at u-boot prompt by pressing any key and enable camera devicetree overlay:

.. code-block:: text

   # For Digilent PCam5C or ALINX AN5641
   => setenv name_overlays ti/k3-am62x-sk-csi2-ov5640.dtbo
   => boot

   # For Technexion TEVI-OV5640
   => setenv name_overlays ti/k3-am62x-sk-csi2-tevi-ov5640.dtbo
   => boot

.. code-block:: text

   # For connecting Digilent PCam5C or ALINX AN5641 on V3Link fusion's RX Port 0:
   => setenv name_overlays ti/k3-am62x-sk-csi2-v3link-fusion.dtbo ti/k3-v3link-ov5640-0-0.dtbo
   => boot

   # For connecting Technexion TEVI-OV5640 on V3Link fusion's RX Port 0:
   => setenv name_overlays ti/k3-am62x-sk-csi2-v3link-fusion.dtbo ti/k3-v3link-tevi-ov5640-0-0.dtbo
   => boot

Once the overlay is applied, you can confirm that the sensor is being
probed by checking the output of :command:`lsmod` or the media graph:

.. code-block:: console

   $ lsmod | grep ov5640
   ov5640                 36864  1
   v4l2_fwnode            20480  2 ov5640,cdns_csi2rx

   $ media-ctl -p
   Media controller API version 6.1.33
   Media device information
   ------------------------
   driver          j721e-csi2rx
   model           TI-CSI2RX
   serial
   bus info        platform:30102000.ticsi2rx
   hw revision     0x1
   driver version  6.1.33

   Device topology
   ....
   - entity 13: ov5640 4-003c (1 pad, 1 link, 0 route)
                type V4L2 subdev subtype Sensor flags 0
                device node name /dev/v4l-subdev2
           pad0: Source
                   [stream:0 fmt:UYVY8_1X16/640x480@1/30 field:none colorspace:srgb xfer:srgb ycbcr:601 quantization:full-range
                    crop.bounds:(0,0)/2624x1964
                    crop:(16,14)/2592x1944]
                   -> "cdns_csi2rx.30101000.csi-bridge":0 [ENABLED,IMMUTABLE]
   ....


Capturing raw frames
====================

Once the media pipeline is configured, you should be able to capture raw
frames from the sensor using any tool compliant with v4l2 apis. For example
you can use libcamera to capture 20 frames @ 480p:

.. code-block:: console

   $ cam -c1 --stream width=640,height=480,pixelformat=UYVY -C20

You can also capture at other sensor-supported resolutions:

.. code-block:: console

   # List supported resolutions
   $ cam -c1 -I
   # Capture 20 frames @ 1024x768
   $ cam -c1 --stream width=1024,height=768,pixelformat=UYVY -C20

To save the raw YUV frames to SD card for viewing later use the -F option:

.. code-block:: console

   $ cam -c1 --stream width=640,height=480,pixelformat=UYVY -C20 -F#.uyvy
   $ ls *.uyvy
   -rw-r--r-- 1 root root 614400 Jan  1 19:19 cam0-stream0-000000.uyvy
   -rw-r--r-- 1 root root 614400 Jan  1 19:19 cam0-stream0-000001.uyvy
   -rw-r--r-- 1 root root 614400 Jan  1 19:19 cam0-stream0-000002.uyvy
   -rw-r--r-- 1 root root 614400 Jan  1 19:19 cam0-stream0-000003.uyvy
   -rw-r--r-- 1 root root 614400 Jan  1 19:19 cam0-stream0-000004.uyvy

Alternatively you can use tools like :command:`yavta` or
:command:`v4l2-ctl`, but please note they require manual configuration
using media-ctl if you want to stream at a different resolution and formats
than the default (640x480 UYVY):

.. code-block:: console

   $ yavta -s 640x480 -f UYVY /dev/video0 -c20
   ....
   $ v4l2-ctl -d0 --stream-mmap -v width=640,height=480,pixelformat=UYVY


.. note::

   Sometimes the sensor may not stream on the first attempt after sensor
   wakes up from runtime suspend state. To make it work reliably on every
   attempt, you can **disable runtime PM** for the sensor:

   .. code-block:: console

      $ echo "on" > /sys/devices/platform/bus@f0000/20020000.i2c/i2c-2/i2c-4/4-003c/power/control

Capture to display
==================

If a display (HDMI or LVDS) is connected then use the following steps to view the camera frames:

.. code-block:: console

   # As a window within weston desktop
   $ gst-launch-1.0 v4l2src device="/dev/video0" ! video/x-raw, width=640, height=480, format=UYVY ! autovideosink

   # Direct KMS Sink
   $ systemctl stop emptty
   $ gst-launch-1.0 v4l2src device="/dev/video0" ! video/x-raw, width=640, height=480, format=UYVY ! queue ! kmssink driver-name=tidss plane-properties=s,zpos=1

You can also replace v4l2src with libcamerasrc above if you want to test
different sensor-supported resolutions like 480p, 720p etc.

.. code-block:: console

   $ gst-launch-1.0 libcamerasrc ! video/x-raw, width=1024, height=768, format=UYVY ! autovideosink

You can also run mosaic camera to display stream from 4 OV5640 connected to the SK-AM62P using V3Link fusion mini board.

.. note::

   Arm neon accelerated TI elements for video mosaicing and color format conversion namely ``timosaic`` and ``ticolorconvert`` are not present in AM62P SDK 11.00.
   To run the below pipeline, AM62P SDK 10.01 should be used with the SDK 11.00 kernel installed from `here <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/log/?h=ti-linux-6.12.y>`__.

.. code-block:: console

   $ gst-launch-1.0 \
   v4l2src device=/dev/video-ov5640-cam0 ! video/x-raw, width=640,height=480, format=YUY2 ! ticolorconvert ! queue ! mosaic.sink_0 \
   v4l2src device=/dev/video-ov5640-cam1 ! video/x-raw, width=640,height=480, format=YUY2 ! ticolorconvert ! queue ! mosaic.sink_1 \
   v4l2src device=/dev/video-ov5640-cam2 ! video/x-raw, width=640,height=480, format=YUY2 ! ticolorconvert ! queue ! mosaic.sink_2 \
   v4l2src device=/dev/video-ov5640-cam3 ! video/x-raw, width=640,height=480, format=YUY2 ! ticolorconvert ! queue ! mosaic.sink_3 \
   timosaic name=mosaic \
   sink_0::startx=300 sink_0::starty=0 sink_0::width=640 sink_0::height=480 \
   sink_1::startx=980 sink_1::starty=0 sink_1::width=640 sink_1::height=480  \
   sink_2::startx=300 sink_2::starty=500 sink_2::width=640 sink_2::height=480 \
   sink_3::startx=980 sink_3::starty=500 sink_3::width=640 sink_3::height=480 ! \
   video/x-raw, width=1920, height=1080, format=NV12 ! queue ! kmssink driver-name=tidss sync=false force-modesetting=true

.. note::

   When configuring the media pipe for execution of the above GStreamer pipeline, it is recommended to setup routes such that CTX 0 is bypassed.
   This configuration prevents frame corruption in scenarios where high system load results in degraded performance of one or more kernel
   threads assigned for individual camera management.

Suspend to RAM
==============

The camera pipeline supports system supend to RAM on |__PART_FAMILY_NAME__|
SK. You can refer to :ref:`Power Management <lpm_modes>` guide for more
details.

For example, you can start streaming from camera using any of the above
methods and then suspend to RAM for 5 seconds using the following command:

.. code-block:: console

   $ rtcwake -s 5 -m mem

The system will automatically wake-up after 5 seconds, and camera streaming
should resume from where it left (as long as the sensor supports it).

.. attention::

   Only TEVI OV5640 and IMX219 are known to work reliably when system is suspended with capture running.


CSI2RX testing details
======================

Following sensors and daughter cards have been tested with the SDK 12.00.00.07.04

.. csv-table:: Sensor
   :header: "Sensor","Media Bus Format","Video Format","Resolution"

   "IMX219 RPi Camera","MEDIA_BUS_FMT_SRGGB8_1X8","V4L2_PIX_FMT_SRGGB8","1920x1080"
   "OV5640 MIPI CSI Camera","MEDIA_BUS_FMT_YUYV8_1X16","V4L2_PIX_FMT_YUYV","640x480"

.. csv-table:: Sensor + Daughter Card
   :header: "Daughter Board + Sensor","Media Bus Format","Video Format","Resolution"

   "V3Link (Fusion Mini) board, OV5640","MEDIA_BUS_FMT_YUYV8_1X16","V4L2_PIX_FMT_YUYV","640x480"
