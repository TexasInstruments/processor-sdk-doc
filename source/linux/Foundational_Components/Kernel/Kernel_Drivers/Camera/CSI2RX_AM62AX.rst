.. include:: _CSI2RX_common.rst

***********************
Enabling camera sensors
***********************

SK-AM62A supports the following FPDLink cameras using fusion board: **IMX390,
OV2312**; and the following 22-pin FFC compatible cameras: **IMX219**.

For sensors directly connected to the SK using the FFC connector, the media
graph is fairly simple. For example IMX219 is connected to the CSI-RX
bridge directly, which ultimately ends up at a /dev/videoX node:

.. Image:: /images/imx219-pipeline.png

For sensors connected using FPDLink fusion board, the pipeline is a bit
more complicated. For example OV2312 is a multi-stream sensor, which is
first connected to a CSI-to-FPD serializer, and then to FPD-to-CSI
deserializer, finally routing the two virtual channels (streams) to
separate /dev/videoX nodes:

.. Image:: /images/ov2312-pipeline.png

Applying sensor overlays
========================

To enable FPDLink/V3Link cameras you will need to apply the device tree
overlays for both the deserializer board and the sensor at U-boot prompt:

.. code-block:: text

   # For OV2312 connected on Fusion board RX Port 0:
   => setenv name_overlays ti/k3-am62a7-sk-fusion.dtbo ti/k3-fpdlink-ov2312-0-0.dtbo
   => boot

   # For OV2312 connected on DS90UB954-Q1 RX Port 0:
   => setenv name_overlays ti/k3-am62a7-sk-ub954-evm.dtbo ti/k3-fpdlink-ov2312-0-0.dtbo
   => boot

   # For RCM IMX390 connected on Fusion board RX Port 0:
   => setenv name_overlays ti/k3-am62a7-sk-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
   => boot

   # For V3Link IMX219 module connected to V3Link fusion's RX Port 0:
   => setenv name_overlays ti/k3-am62x-sk-csi2-v3link-fusion.dtbo ti/k3-v3link-imx219-0-0.dtbo
   => boot

To enable camera connected to the 22-pin FFC connector, enable the sensor
overlay at U-boot prompt:

.. code-block:: text

   # For IMX219 connected to 22-pin FFC connector
   => setenv name_overlays ti/k3-am62x-sk-csi2-imx219.dtbo
   => boot

For more details on building or applying overlays permanently, refer to the
:ref:`How to enable DT overlays in linux <howto_dt_overlays>` guide.

Configuring media pipeline
==========================

Once the overlay is applied, you can confirm that the sensor is being
probed by checking the output of lsmod or the media graph:

.. code-block:: console

   $ lsmod | grep imx219
   imx219                 24576  1
   v4l2_fwnode            24576  2 imx219,cdns_csi2rx

   $ media-ctl -p
   Media controller API version 6.1.33
   Media device information
   ------------------------
   driver          j721e-csi2rx
   model           TI-CSI2RX
   serial
   bus info        platform:30102000.ticsi2rx
   hw revision     0x1
   driver version  6.6.32

   Device topology
   - entity 1: 30102000.ticsi2rx (7 pads, 7 links, 1 route)
               type V4L2 subdev subtype Unknown flags 0
               device node name /dev/v4l-subdev0
           routes:
                   0/0 -> 1/0 [ACTIVE]
           pad0: Sink
                   [stream:0 fmt:SRGGB8_1X8/1920x1080 field:none]
                   <- "cdns_csi2rx.30101000.csi-bridge":1 [ENABLED,IMMUTABLE]
           pad1: Source
                   [stream:0 fmt:SRGGB8_1X8/1920x1080 field:none]
                   -> "30102000.ticsi2rx context 0":0 [ENABLED,IMMUTABLE]
           pad2: Source
                   -> "30102000.ticsi2rx context 1":0 [ENABLED,IMMUTABLE]
           pad3: Source
                   -> "30102000.ticsi2rx context 2":0 [ENABLED,IMMUTABLE]
           pad4: Source
                   -> "30102000.ticsi2rx context 3":0 [ENABLED,IMMUTABLE]
           pad5: Source
                    -> "30102000.ticsi2rx context 4":0 [ENABLED,IMMUTABLE]
           pad6: Source
                   -> "30102000.ticsi2rx context 5":0 [ENABLED,IMMUTABLE]
   ....
   - entity 15: imx219 4-0010 (1 pad, 1 link, 0 routes)
        type V4L2 subdev subtype Sensor flags 0
        device node name /dev/v4l-subdev2
   pad0: Source
           [stream:0 fmt:SRGGB8_1X8/1920x1080 field:none colorspace:raw xfer:none quantization:full-range
            crop.bounds:(8,8)/3280x2464
            crop:(688,700)/1920x1080]
            -> "cdns_csi2rx.30101000.csi-bridge":0 [ENABLED,IMMUTABLE]

The sensor and other subdevs (for example FPDLink ser/deser) should
automatically get configured by the initialization script on the SD card:

.. code-block:: console

   IMX219 Camera 0 detected
   device = /dev/video-imx219-cam0
   name = imx219
   format = [fmt:SRGGB8_1X8/1920x1080]
   subdev_id = /dev/v4l-imx219-subdev0
   isp_required = yes

For manual configuration, like switching to a different resolution or
bitdepth, you can use media-ctl as `explained above
<#utilities-to-interact-with-the-driver>`__. For example you can switch to
10-bit 1640x1232 capture on IMX219 using:

.. code-block:: console

   $ media-ctl --set-v4l2 '"imx219 4-0010":0[fmt:SRGGB10_1X10/1640x1232]'
   $ media-ctl --set-v4l2 '"30102000.ticsi2rx":0[fmt:SRGGB10_1X10/1640x1232]'

and to switch it back to 8bit 1920x1080 capture :

.. code-block:: console

   $ media-ctl --set-v4l2 '"30102000.ticsi2rx":0[fmt:SRGGB8_1X8/1920x1080]'
   $ media-ctl --set-v4l2 '"imx219 4-0010":0[fmt:SRGGB8_1X8/1920x1080]'

.. note::

   When configuring the media pipe for multi-camera use case, it is recommended to setup routes such
   that CTX 0 is bypassed. This configuration prevents frame corruption in scenarios where high system load results in
   degraded performance of one or more kernel threads assigned for individual camera management. The camera setup
   script in SD card will do this configuration.

Capturing raw frames
====================

Once the media pipeline is configured, you should be able to capture raw
frames from the sensor using any tool compliant with v4l2 apis. For example
you can use :command:`yavta` to capture 100 frames from IMX219 @ 1232p:

.. code-block:: console

   $ yavta -s 1920x1080 -f SRGGB8 /dev/video-imx219-cam0 -c100
   Device /dev/video-imx219-cam0 opened.
   yavta -s 1920x1080 -f SRGGB8 /dev/video-imx219-cam0 -c100
   Device /dev/video-imx219-cam0 opened.
   Device `j721e-csi2rx' on `platform:30102000.ticsi2rx' (driver 'j721e-csi2rx') supports video, capture, without mplanes.
   Video format set: SRGGB8 (42474752) 1920x1080 (stride 1920) field none buffer size 2073600
   Video format: SRGGB8 (42474752) 1920x1080 (stride 1920) field none buffer size 2073600
   8 buffers requested.
   ....
   length: 2073600 offset: 0 timestamp type/source: mono/EoF
   Buffer 0/0 mapped at address 0xffff95415000.
   length: 2073600 offset: 2076672 timestamp type/source: mono/EoF
   Buffer 1/0 mapped at address 0xffff9521a000.
   length: 2073600 offset: 4153344 timestamp type/source: mono/EoF
   Buffer 2/0 mapped at address 0xffff9501f000.
   length: 2073600 offset: 6230016 timestamp type/source: mono/EoF
   ....

By default the frames are copied over to DDR and discarded later. You can
optionally save a few frames to the SD card for debugging purposes:

.. code-block:: console

   $ yavta -s 1920x1080 -f SRGGB8 /dev/video-imx219-cam0 -c5 -Fframe-#.bin
   ....
   $ ls -l frame-*.bin
   -rw-r--r-- 1 root root 2073600 Feb 22 05:24 frame-000000.bin
   -rw-r--r-- 1 root root 2073600 Feb 22 05:24 frame-000001.bin
   -rw-r--r-- 1 root root 2073600 Feb 22 05:24 frame-000002.bin
   -rw-r--r-- 1 root root 2073600 Feb 22 05:24 frame-000003.bin
   -rw-r--r-- 1 root root 2073600 Feb 22 05:24 frame-000004.bin

The raw bayer frames can be viewed directly on the host machine using
utilities like `7yuv <http://datahammer.de/7yuv_manual/index.htm>`__ or `PixelViewer
<https://carinastudio.azurewebsites.net/PixelViewer/>`__, or converted
using OpenCV.

Capture to Display using ISP
============================

To use the full capture to display pipeline, you can use gstreamer to call
the required ISP components to convert the raw frames, apply
auto-exposure/auto-white-balance algorithms and other pre-processing
blocks.

You may have to stop the display manager before running the below pipelines:

.. code-block:: console

   $ systemctl stop emptty

Use the following pipeline for IMX219 1920x1080 RAW8 mode:

.. code-block:: console

   $ gst-launch-1.0 v4l2src io-mode=dmabuf-import device=/dev/video-imx219-cam0 ! video/x-bayer,width=1920,height=1080,format=rggb ! tiovxisp sensor-name=SENSOR_SONY_IMX219_RPI dcc-isp-file=/opt/imaging/imx219/linear/dcc_viss_1920x1080.bin sink_0::dcc-2a-file=/opt/imaging/imx219/linear/dcc_2a_1920x1080.bin sink_0::device=/dev/v4l-imx219-subdev0 ! video/x-raw,format=NV12 ! queue ! kmssink driver-name=tidss plane-properties=s,zpos=1

If the sensor needs to be configured to capture at some other resolution or format
(e.g. 1640x1232, 10bit) you can update media graph and edit the above pipeline with the new width,
height, format and dcc-\*-file parameters:

.. code-block:: console

   $ media-ctl --set-v4l2 '"30102000.ticsi2rx":0[fmt:SRGGB10_1X10/1640x1232]'
   $ media-ctl --set-v4l2 '"imx219 4-0010":0[fmt:SRGGB10_1X10/1640x1232]'
   $ gst-launch-1.0 v4l2src io-mode=dmabuf-import device=/dev/video-imx219-cam0 ! video/x-bayer,width=1640,height=1232,format=rggb10 ! tiovxisp sensor-name=SENSOR_SONY_IMX219_RPI dcc-isp-file=/opt/imaging/imx219/linear/dcc_viss_10b_1640x1232.bin sink_0::dcc-2a-file=/opt/imaging/imx219/linear/dcc_2a_10b_1640x1232.bin sink_0::device=/dev/v4l-imx219-subdev0 format-msb=9 ! video/x-raw,format=NV12 ! queue ! kmssink driver-name=tidss plane-properties=s,zpos=1

For OV2312 use mosaic to display both streams together:

.. code-block:: console

   # Mosaic of RGB and IR streams
   $ gst-launch-1.0 \
   v4l2src device=/dev/video-ov2312-rgb-cam0 io-mode=5 ! video/x-bayer, width=1600, height=1300, format=bggi10 ! queue leaky=2 ! \
   tiovxisp sensor-name=SENSOR_OV2312_UB953_LI \
   dcc-isp-file=/opt/imaging/ov2312/linear/dcc_viss.bin \
   sink_0::dcc-2a-file=/opt/imaging/ov2312/linear/dcc_2a.bin sink_0::device=/dev/v4l-ov2312-subdev0 format-msb=9 \
   sink_0::pool-size=8 src::pool-size=8 ! \
   video/x-raw, format=NV12, width=1600, height=1300 ! queue ! mosaic.sink_0 \
   v4l2src device=/dev/video-ov2312-ir-cam0 io-mode=5 ! video/x-bayer, width=1600, height=1300, format=bggi10 ! queue leaky=2 ! \
   tiovxisp sensor-name=SENSOR_OV2312_UB953_LI \
   dcc-isp-file=/opt/imaging/ov2312/linear/dcc_viss.bin \
   sink_0::dcc-2a-file=/opt/imaging/ov2312/linear/dcc_2a.bin format-msb=9 sink_0::pool-size=8 src_0::pool-size=8 ! \
   video/x-raw, format=GRAY8, width=1600, height=1300 ! videoconvert ! \
   video/x-raw, format=NV12 ! queue ! mosaic.sink_1 \
   tiovxmosaic name=mosaic \
   sink_0::startx="<0>" sink_0::starty="<0>" sink_0::widths="<640>" sink_0::heights="<480>" \
   sink_1::startx="<640>" sink_1::starty="<480>" sink_1::widths="<640>" sink_1::heights="<480>" ! \
   queue ! kmssink driver-name=tidss plane-properties=s,zpos=1

CSI2RX testing details
======================

Following sensors and daughter cards have been tested with the SDK 11.01.07.05

.. csv-table:: Sensor
   :header: "Sensor","Media Bus Format","Video Format","Resolution"

   "IMX219 RPi Camera","MEDIA_BUS_FMT_SRGGB8_1X8","V4L2_PIX_FMT_SRGGB8","1920x1080"

.. csv-table:: Sensor + Daughter Card
   :header: "Daughter Board + Sensor","Media Bus Format","Video Format","Resolution"

   "FPDLink fusion EVM, IMX390","MEDIA_BUS_FMT_SRGGB12_1X12","V4L2_PIX_FMT_SRGGB12","1936x1100"
   "FPDLink fusion EVM, OV2312 ","MEDIA_BUS_FMT_SBGGI10_1X10","V4L2_PIX_FMT_SBGGI10","1600x1300"
   "V3Link (Fusion Mini) board, IMX219","MEDIA_BUS_FMT_SRGGB8_1X8","V4L2_PIX_FMT_SRGGB8","1920x1080"
   "V3Link (Fusion Mini) board, IMX390","MEDIA_BUS_FMT_SRGGB12_1X12","V4L2_PIX_FMT_SRGGB12","1936x1100"
   "V3Link (Fusion Mini) board, OV2312","MEDIA_BUS_FMT_SBGGI10_1X10","V4L2_PIX_FMT_SBGGI10","1600x1300"
   "DS90UB954-Q1 EVM, OV2312","MEDIA_BUS_FMT_SBGGI10_1X10","V4L2_PIX_FMT_SBGGI10","1600x1300"
