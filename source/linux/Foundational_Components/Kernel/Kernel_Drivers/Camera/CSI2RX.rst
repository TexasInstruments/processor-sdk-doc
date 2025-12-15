######
CSI2RX
######

************
Introduction
************

The CSI2RX subsystem is present on some TI SoCs which facilitates the capture of
camera frames over a MIPI CSI-2 bus. The driver is based on the Video for Linux
2 (V4L2) API. It implements V4L2's Media Controller (MC) API.

*********************
Hardware Architecture
*********************

The CSI2RX subsystem is composed of 3 IPs: Cadence DPHY, Cadence CSI2RX bridge,
TI CSI2RX DMA wrapper (aka the SHIM layer).

.. Image:: /images/csi2rx-single-camera.png

The CSI2RX subsystem supports the following features:

- Compliant to MIPI CSI v1.3
- Supports up to 16 virtual channels per input (partial MIPI CSI v2.0 feature).
- Data rate up to 2.5 Gbps per lane (wire rate).
- Supports 1, 2, 3, or 4 data lane connection to DPHY_RX.
- Programmable formats including YUV420, YUV422, RGB, Raw, etc.

See the the technical reference manual (TRM) for the SoC in question for more
detailed information.

*******************
Driver Architecture
*******************

The driver is based on the Video 4 Linux 2 (V4L2) API. It is implemented
according to the V4L2 standard for capture devices. The driver is only
responsible for programming the SoC components for capture like the DPHY, CSI
bridge, DMA. For external devices like camera sensors separate V4L2 subdevice
drivers are needed.

The Media Controller API
========================

The driver is implemented using V4L2's Media Controller (MC) API. In the MC API,
each element in the media pipeline is configured individually by the user-space
application. In comparison, in the legacy or non-MC API drivers, only the
/dev/videoX node needs to be configured, and it propagates the configuration up
the chain. With this model, the MC API allows for more flexible pipeline
configurations which can all be controlled from user-space without having to
change the driver or the device tree.

For example, with the legacy API the format is set on /dev/videoX and that will
set it for the entire pipeline (sensor, bridge, DMA engine, etc). With the MC
API, the format needs to be set on each individual element in the pipeline. So
with a single camera setup, for capturing 1920x1080 @ 60fps UYVY, the camera
(/dev/v4l-subdevX) should first be configured to use that format via the V4L2
subdev ioctls. Then the /dev/videoX node (which represents the DMA context)
should be configured to use matching configuration. The Media Controller
framework checks for mismatches and reports errors if something is not right.

In similar fashion, the DMA context does not care about frame rate. It can
capture at any rate, so the driver does not implement the G_PARM or S_PARM
ioctls. Instead, the frame rate should be set on the sensor using
VIDIOC_SUBDEV_S_FRAME_INTERVAL.

Quick links for relevant Linux Kernel documentation:

- `Video for Linux API <https://www.kernel.org/doc/html/latest/userspace-api/media/v4l/v4l2.html>`__
- `Media Controller API
  <https://www.kernel.org/doc/html/latest/userspace-api/media/mediactl/media-controller.html>`__


Utilities to interact with the driver
=====================================

Standard V4L2 utilities can be used to set these formats and frame rates. One
such tool is :command:`media-ctl`.

To see the media pipeline to understand how all the components are connected in
software, the pipeline can be printed to the console using ``media-ctl -p``. This
would list all the elements in the pipeline, what they are connected to, and
their names. This information can then be used to set formats and frame rates on
various elements for the pipeline. For example, below command can be used to set
1920x1080 @ 30fps UYVY format on the sensor node:

.. code-block:: console

   media-ctl --set-v4l2 '"sensor-name 9-0012":0 [fmt:UYVY8_2X8/1920x1080@1/30]'

This just sets the formats on the sensor and bridge. The format on the DMA
context (/dev/videoX) needs to be set separately. This can be done while
starting the capture with :command:`yavta` for example. The below command can
be run next to start capturing the video stream to a file called
:file:`capture`:

.. code-block:: console

   yavta -c -Fcapture -s 1920x1080 -f UYVY /dev/video0

This command first sets the 1920x1080 UYVY format on the DMA context (which must
match the format on the sensor), and then starts capturing frames to a file
called :file:`capture`.

It is often useful to see the pipeline visually. media-ctl can print the
pipeline as a dot graph which can then be converted to an image for viewing. The
below set of commands can achieve this:

.. code-block:: console

   media-ctl --print-dot | dot -Tpng > graph.png

To check for errors during streaming, locate the subdevice for the Cadence CSI2RX in the media pipeline and run the following command:

.. code-block:: console

   v4l2-ctl --log-status -d /dev/v4l-subdevX

Replace /dev/v4l-subdevX with the correct subdevice node of the Cadence CSI2RX receiver. After running the above command, you will be able to see information regarding any errors during streaming such as short packets or ECC errors in the kernel logs.

Building the driver
===================

First, enable the DPHY using CONFIG_PHY_CADENCE_DPHY. Then enable the CSI2RX
bridge using CONFIG_VIDEO_CADENCE and CONFIG_VIDEO_CADENCE_CSI2RX. Finally,
enable CONFIG_VIDEO_TI_J721E_CSI2RX. The config for the sensor should also
be enabled.

The driver can be built-in or it can be a loadable module. If the driver is
built as a module, the module will be called ``j721e-csi2rx``. Along with that,
the Cadence bridge and DPHY modules must also be loaded, which are called
``cdns-csi2rx`` and ``cdns-dphy`` respectively.

*************************************
Creating device tree nodes for sensor
*************************************

Since the sensor is a separate module and any sensor can be plugged in to the
board, the sensor device tree nodes are not included in the base dtb. Instead,
it should be added in as an overlay.

Below overlay is an example for a sensor module connected to the board using
I2C2 and CSI-RX Port 0:

.. code-block:: dts

   // SPDX-License-Identifier: GPL-2.0
   /*
    * Example Camera Module
    * Copyright (C) 2024 Texas Instruments Incorporated - https://www.ti.com/
    */

   /dts-v1/;
   /plugin/;

   #include <dt-bindings/gpio/gpio.h>

   &{/} {
        clk_sensor_fixed: sensor-xclk {
           compatible = "fixed-clock";
           #clock-cells = <0>;
           clock-frequency = <24000000>;
       };
   };

   &main_i2c2 {
       #address-cells = <1>;
       #size-cells = <0>;
       status = "okay";

       camera@10 {
           compatible = "manufacturer,sensor-compatible";
           reg = <0x10>;

           clocks = <&clk_sensor_fixed>;
           clock-names = "xclk";

           port {
               csi2_cam0: endpoint {
                   remote-endpoint = <&csi2rx0_in_sensor>;
                   clock-lanes = <0>;
                   /*
                    * This example sensor uses 2 lanes. Other sensors might use
                    * 1, 2, 3, or 4 lanes. Populate this property accordingly.
                    * See Documentation/devicetree/bindings/media/video-interfaces.yaml
                    * for more info.
                    */
                   data-lanes = <1 2>;
               };
           };
       };
   };

   &cdns_csi2rx0 {
       ports {
           #address-cells = <1>;
           #size-cells = <0>;

           csi0_port0: port@0 {
               reg = <0>;
               status = "okay";

               csi2rx0_in_sensor: endpoint {
                   remote-endpoint = <&csi2_cam0>;
                   bus-type = <4>; /* CSI2 DPHY. */
                   clock-lanes = <0>;
                   data-lanes = <1 2>;
               };
           };
       };
   };

   &ti_csi2rx0 {
       status = "okay";
   };

   &dphy0 {
       status = "okay";
   };

.. _enabling-camera-sensors:

***********************
Enabling camera sensors
***********************

.. ifconfig:: CONFIG_part_variant in ('AM62X','AM62PX')

   |__PART_FAMILY_NAME__| SK supports the following 15-pin FFC compatible
   camera modules with **OV5640** sensor:

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   Arducam V3Link (Fusion Mini) board can also be used to connect these camera modules to SK-AM62P over FPDLink cable.

.. ifconfig:: CONFIG_part_variant in ('AM62X','AM62PX')

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

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. code-block:: text

      # For connecting Digilent PCam5C or ALINX AN5641 on V3Link fusion's RX Port 0:
      => setenv name_overlays ti/k3-am62x-sk-csi2-v3link-fusion.dtbo ti/k3-v3link-ov5640-0-0.dtbo
      => boot

      # For connecting Technexion TEVI-OV5640 on V3Link fusion's RX Port 0:
      => setenv name_overlays ti/k3-am62x-sk-csi2-v3link-fusion.dtbo ti/k3-v3link-tevi-ov5640-0-0.dtbo
      => boot

.. ifconfig:: CONFIG_part_variant in ('AM62X','AM62PX')

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

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

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


.. ifconfig:: CONFIG_part_variant in ('AM62X')

   CSI2RX testing details
   ======================

   Following sensors have been tested with the latest SDK.

   .. csv-table:: Sensor
      :header: "Sensor","Media Bus Format","Video Format","Resolution"

      "IMX219 RPi Camera","MEDIA_BUS_FMT_SRGGB8_1X8","V4L2_PIX_FMT_SRGGB8","1920x1080"
      "OV5640 MIPI CSI Camera","MEDIA_BUS_FMT_YUYV8_1X16","V4L2_PIX_FMT_YUYV","640x480"


.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   CSI2RX testing details
   ======================

   Following sensors and daughter cards have been tested with the latest SDK.

   .. csv-table:: Sensor
      :header: "Sensor","Media Bus Format","Video Format","Resolution"

      "IMX219 RPi Camera","MEDIA_BUS_FMT_SRGGB8_1X8","V4L2_PIX_FMT_SRGGB8","1920x1080"
      "OV5640 MIPI CSI Camera","MEDIA_BUS_FMT_YUYV8_1X16","V4L2_PIX_FMT_YUYV","640x480"

   .. csv-table:: Sensor + Daughter Card
      :header: "Daughter Board + Sensor","Media Bus Format","Video Format","Resolution"

      "V3Link (Fusion Mini) board, OV5640","MEDIA_BUS_FMT_YUYV8_1X16","V4L2_PIX_FMT_YUYV","640x480"

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

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

   Following sensors and daughter cards have been tested with the latest SDK.

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

.. ifconfig:: CONFIG_part_variant in ('J721E')

   J721E has two instances of CSI2RX capture subsystem and can support upto
   eight **IMX390** cameras using FPDLink fusion EVM. J721E EVM and SK also
   supports **OV5640** module connected to MIPI connector. J721E SK has two
   instances of 15-pin FFC camera connector to which **IMX219** based RPi camera
   modules can be interfaced.

   Applying sensor overlays
   ========================

   To enable FPDLink cameras you will need to apply the device tree overlays
   for both the fusion board and the sensor at U-boot prompt:

   .. code-block:: text

      # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on J721E CPB:
      # FPDLink IMX390 camera overlays are named according to the port connected in the following
      # format : ti/k3-fpdlink-imx390-rcm-<csi_port>-<fusion_rx_port>.dtbo
      => setenv name_overlays ti/k3-j721e-evm-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
      => boot

      # For single RCM IMX390 connected to RX port 0 on DS90UB954-Q1 EVM on J721E EVM:
      => setenv name_overlays ti/k3-j721e-evm-ub954.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
      => boot

      # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on J721E SK:222
      => setenv name_overlays ti/k3-j721e-sk-fpdlink-fusion.dtbo  ti/k3-fpdlink-imx390-rcm-0-0.dtbo
      => boot

   To enable IMX219 camera connected to the 22-pin FFC connectoron J721E SK,
   enable the sensor overlay at U-boot prompt:

   .. code-block:: text

      # For IMX219 connected to 15-pin FFC connector
      => setenv name_overlays ti/k3-j721e-sk-csi2-dual-imx219.dtbo
      => boot

   For more details on building or applying overlays permanently, refer to the
   :ref:`How to enable DT overlays in linux <howto_dt_overlays>` guide.


   CSI2RX testing details
   ======================

   The following combinations of sensors are tested in the latest sdk.

       +--------------+---------------------------------------+-----------------------------------+
       | Hardware     | Sensor                                | Default format and resolution     |
       +==============+=======================================+===================================+
       | J721E EVM    | LI OV5640 MIPI CSI Camera             | YUYV8_1X16/1280x720 at 30 fps     |
       +--------------+---------------------------------------+-----------------------------------+
       | J721E EVM    | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
       +--------------+---------------------------------------+-----------------------------------+
       | J721E EVM    | DS90UB954-Q1 EVM, IMX390              | SRGGB12_1X12/1936x1100 at 30 fps  |
       +--------------+---------------------------------------+-----------------------------------+
       | J721E SK     | IMX219 RPi Camera                     | SRGGB8_1X8/1920x1080 at 30 fps    |
       +--------------+---------------------------------------+-----------------------------------+
       | J721E SK     | LI OV5640 MIPI CSI Camera             | YUYV8_1X16/1280x720 at 30 fps     |
       +--------------+---------------------------------------+-----------------------------------+
       | J721E SK     | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
       +--------------+---------------------------------------+-----------------------------------+




.. ifconfig:: CONFIG_part_variant in ('J721S2')

   J721S2 has two instances of CSI2RX capture subsystem and can support upto
   eight **IMX390** cameras using FPDLink fusion EVM, J721S2 EVM and AM68A SK also
   supports **OV5640** module connected to MIPI connector. AM68A SK has two
   instances of 22-pin FFC camera connector to which **IMX219** based RPi camera
   modules can be interfaced.

   Applying sensor overlays
   ========================

   To enable FPDLink cameras you will need to apply the device tree overlays
   for both the fusion board and the sensor at U-boot prompt:

   .. code-block:: text

      # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on J721S2 CPB:
      # FPDLink IMX390 camera overlays are named according to the port connected in the following
      # format : ti/k3-fpdlink-imx390-rcm-<csi_port>-<fusion_rx_port>.dtbo
      => setenv name_overlays ti/k3-j721s2-evm-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
      => boot

      # For single RCM IMX390 connected to RX port 0 on DS90UB954-Q1 EVM on J721S2 EVM:
      => setenv name_overlays ti/k3-j721s2-evm-ub954.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
      => boot

      # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on AM68A SK:
      => setenv name_overlays ti/k3-j721e-sk-fpdlink-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
      => boot

      # For single IMX219 connected to RX port 0 on V3Link fusion on AM68A SK:
      => setenv name_overlays ti/k3-am68-sk-v3link-fusion.dtbo ti/k3-v3link-imx219-0-0.dtbo
      => boot

   To enable IMX219 camera connected to the 22-pin FFC connectoron AM68A SK,
   enable the sensor overlay at U-boot prompt:

   .. code-block:: text

      # For IMX219 connected to 22-pin FFC connector
      => setenv name_overlays ti/k3-j721e-sk-csi2-dual-imx219.dtbo
      => boot

   For more details on building or applying overlays permanently, refer to the
   :ref:`How to enable DT overlays in linux <howto_dt_overlays>` guide.


   CSI2RX testing details
   ======================

   The following combinations of sensors are tested on J721S2 in the latest sdk.

      +--------------+---------------------------------------+-----------------------------------+
      | Hardware     | Sensor                                | Default format and resolution     |
      +==============+=======================================+===================================+
      | J721S2       | LI OV5640 MIPI CSI Camera             | YUYV8_1X16/1280x720 at 30 fps     |
      +--------------+---------------------------------------+-----------------------------------+
      | J721S2       | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
      +--------------+---------------------------------------+-----------------------------------+
      | J721S2       | DS90UB954-Q1 EVM, IMX390              | SRGGB12_1X12/1936x1100 at 30 fps  |
      +--------------+---------------------------------------+-----------------------------------+
      | AM68A        | IMX219 RPi Camera                     | SRGGB8_1X8/1920x1080 at 30 fps    |
      +--------------+---------------------------------------+-----------------------------------+
      | AM68A        | LI OV5640 MIPI CSI Camera             | YUYV8_1X16/1280x720 at 30 fps     |
      +--------------+---------------------------------------+-----------------------------------+
      | AM68A        | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
      +--------------+---------------------------------------+-----------------------------------+
      | AM68A        | V3Link fusion, IMX219                 | SRGGB8_1X8/1920x1080 at 30 fps    |
      +--------------+---------------------------------------+-----------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J784S4','J742S2')

   J784S4/AM69A and J742S2 has three instances of CSI2RX capture subsystem and
   can support upto twelve **IMX390** cameras using FPDLink fusion EVM.
   J784S4-EVM/AM69A-SK and J742S2-EVM also supports **OV5640** module connected
   to MIPI connector. AM69A-SK has two instances of 22-pin FFC camera connector
   to which **IMX219** based RPi camera modules can be interfaced.

   Applying sensor overlays
   ========================

   To enable FPDLink cameras you will need to apply the device tree overlays
   for both the fusion board and the sensor at U-boot prompt:

   .. code-block:: text

      # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on J784S4/J742S2 EVM:
      # FPDLink IMX390 camera overlays are named according to the port connected in the following
      # format : ti/k3-fpdlink-imx390-rcm-<csi_port>-<fusion_rx_port>.dtbo
      => setenv name_overlays ti/k3-j721s2-evm-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
      => boot

      # For single RCM IMX390 connected to port 0 on FPDLink IV Fusion 2 board on J784S4/J742S2 EVM:
      => setenv name_overlays ti/k3-j784s4-evm-fpdlink-iv-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
      => boot

      # For single RCM IMX390 connected to RX port 0 on DS90UB954-Q1 EVM on J784S4 EVM:
      => setenv name_overlays ti/k3-j721s2-evm-ub954.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
      => boot

      # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on AM69A SK:
      => setenv name_overlays ti/k3-j721e-sk-fpdlink-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
      => boot

      # For single IMX219 connected to RX port 0 on V3Link fusion on AM69A SK:
      => setenv name_overlays ti/k3-am68-sk-v3link-fusion.dtbo ti/k3-v3link-imx219-0-0.dtbo
      => boot

      # For using two CSI TX on V3Link fusion to two CSI RX on AM69A SK
      => setenv name_overlays ti/k3-am68-sk-v3link-fusion-dual-csitx.dtbo ti/k3-v3link-imx219-0-2.dtbo ti/k3-v3link-imx219-0-3.dtbo ti/k3-v3link-imx219-1-0.dtbo ti/k3-v3link-imx219-1-1.dtbo
      => boot
      # After booting, configure routing on the V3Link fusion for the above setup using the following commands:
      => media-ctl -R '"ds90ub960 5-0030" [2/0 -> 4/2 [1], 3/0 -> 4/3 [1]]'
      => media-ctl -R '"ds90ub960 6-0030" [0/0 -> 5/0 [1], 1/0 -> 5/1 [1]]'
      => media-ctl --set-v4l2 '"ds90ub960 5-0030" 2/0 [fmt:SRGGB8_1X8/1920x1080 field:none]'
      => media-ctl --set-v4l2 '"ds90ub960 5-0030" 3/0 [fmt:SRGGB8_1X8/1920x1080 field:none]'
      => media-ctl --set-v4l2 '"ds90ub960 6-0030" 0/0 [fmt:SRGGB8_1X8/1920x1080 field:none]'
      => media-ctl --set-v4l2 '"ds90ub960 6-0030" 1/0 [fmt:SRGGB8_1X8/1920x1080 field:none]'
      # The two CSI TX configuration on V3Link fusion described above can be used on relevant platforms using similar commands.

   To enable IMX219 camera connected to the 22-pin FFC connector on AM69A SK,
   enable the sensor overlay at U-boot prompt:

   .. code-block:: text

      # For IMX219 connected to 22-pin FFC connector
      => setenv name_overlays ti/k3-j721e-sk-csi2-dual-imx219.dtbo
      => boot

   For more details on building or applying overlays permanently, refer to the
   :ref:`How to enable DT overlays in linux <howto_dt_overlays>` guide.

   CSI2RX testing details
   ======================

   The following combinations of sensors are tested in the latest sdk.

      +--------------+---------------------------------------+-----------------------------------+
      | Hardware     | Sensor                                | Default format and resolution     |
      +==============+=======================================+===================================+
      | J784S4       | LI OV5640 MIPI CSI Camera             | YUYV8_1X16/1280x720 at 30 fps     |
      +--------------+---------------------------------------+-----------------------------------+
      | J784S4       | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
      +--------------+---------------------------------------+-----------------------------------+
      | J784S4       | FPDLink fusion 2 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
      +--------------+---------------------------------------+-----------------------------------+
      | J784S4       | DS90UB954-Q1 EVM, IMX390              | SRGGB12_1X12/1936x1100 at 30 fps  |
      +--------------+---------------------------------------+-----------------------------------+
      | AM69A        | IMX219 RPi Camera                     | SRGGB8_1X8/1920x1080 at 30 fps    |
      +--------------+---------------------------------------+-----------------------------------+
      | AM69A        | LI OV5640 MIPI CSI Camera             | YUYV8_1X16/1280x720 at 30 fps     |
      +--------------+---------------------------------------+-----------------------------------+
      | AM69A        | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
      +--------------+---------------------------------------+-----------------------------------+
      | AM69A        | V3Link fusion, IMX219                 | SRGGB8_1X8/1920x1080 at 30 fps    |
      +--------------+---------------------------------------+-----------------------------------+
      | J742S2       | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
      +--------------+---------------------------------------+-----------------------------------+




.. ifconfig:: CONFIG_part_variant in ('J722S')

   J722S has two instances of CSI2RX capture subsystem and
   can support upto eight **IMX390** cameras using FPDLink fusion EVM.
   J722S also supports **OV5640** and **IMX219** module connected to MIPI connector.

   Applying sensor overlays
   ========================

   To enable FPDLink cameras you will need to apply the device tree overlays
   for both the fusion board and the sensor at U-boot prompt:

   .. code-block:: text

      # For single RCM IMX390 connected to RX port 0 on Fusion board EVM on J722S EVM:
      # FPDLink IMX390 camera overlays are named according to the port connected in the following
      # format : ti/k3-fpdlink-imx390-rcm-<csi_port>-<fusion_rx_port>.dtbo
      => setenv name_overlays ti/k3-j721s2-evm-fusion.dtbo ti/k3-fpdlink-imx390-rcm-0-0.dtbo
      => boot

      # For single IMX219 connected to RX port 0 on V3Link fusion on J722S EVM:
      => setenv name_overlays ti/k3-j722s-evm-v3link-fusion.dtbo ti/k3-v3link-imx219-0-0.dtbo
      => boot

   For more details on building or applying overlays permanently, refer to the
   :ref:`How to enable DT overlays in linux <howto_dt_overlays>` guide.


   CSI2RX testing details
   ======================

   The following combinations of sensors are tested in the latest sdk.

      +--------------+---------------------------------------+-----------------------------------+
      | Hardware     | Sensor                                | Default format and resolution     |
      +==============+=======================================+===================================+
      | J722S        | OV5640 TEVI/PCAM Rpi Module           | YUYV8_1X16/1280x720 at 30 fps     |
      +--------------+---------------------------------------+-----------------------------------+
      | J722S        | FPDLink fusion 1 EVM, IMX390          | SRGGB12_1X12/1936x1100 at 30 fps  |
      +--------------+---------------------------------------+-----------------------------------+
      | J722S        | IMX219 RPi Camera                     | SRGGB8_1X8/1920x1080 at 30 fps    |
      +--------------+---------------------------------------+-----------------------------------+
      | J722S        | V3Link fusion, IMX219                 | SRGGB8_1X8/1920x1080 at 30 fps    |
      +--------------+---------------------------------------+-----------------------------------+
