.. http://processors.wiki.ti.com/index.php/Linux_Core_VIP_User%27s_Guide

VIP
---------------------------------

.. rubric:: Introduction
   :name: introduction-vip-linux-ug

This page gives a basic description of Video Input Port (VIP) hardware,
the Linux kernel driver (**ti-vip**) and various TI boards which uses
VIP. The technical reference manual (TRM) for the SoC in question, and
the board documentation give more detailed descriptions.

.. rubric:: Release Applicable
   :name: release-applicable

This page applies to TI's v4.4 kernel. Although most of it is also
applicable to TI's v4.1 and v3.14 kernel.

.. rubric:: Supported Devices
   :name: supported-devices

The VIP IP is only available on the following TI SoCs or SoC families:

-  AM5x
-  DRA7x

.. rubric:: Hardware Architecture
   :name: hardware-architecture

On supported SoCs the Video Input Port (VIP) module is used for video
capture from video encoder/decoder and camera sensor.

.. Image:: /images/VIP-block-diagram.png

VIP Instance block diagram

VIP instance has two slices each having one 24/16/8 bit port and one 8
bit video port. Each slice has a color space converter block, a scaler
block and a pair of down-sampler block. A common VPDMA block is used for
writing frames to memory. VIP Parser supports video capture from
discrete sync / embedded sync, YUV / RGB format video sources. It
calculates the frame size based on the count of clocks in hsyncs(width)
and count of hsyncs in vsyncs(height). The complex data path
configurability allows to have up to four parallel ports captures from
one instance. One port per slice can utilize the inline CSC and/or SC
block at a time. VPDMA block has a TI proprietary custom programmable
processor. A custom firmware is needed for this custom processor. VPDMA
programming is descriptor based. It allows to setup, configure, control,
abort DMA transactions from different channels to and from memory. VPDMA
needs physically contiguous buffers for capture. It also supports
addressing in the TILER space.

.. rubric:: SoC Hardware Feature
   :name: soc-hardware-feature

-  AM572x/DRA74x/DRA75x

   -  VIP1 and VIP2 instance each supporting up to

      -  Two separate 24-bit video ports for parallel RGB/YUV/RAW (or
         BT656/1120) data, up to 165 MHz
      -  Two separate 8-bit video ports for YUV/RAW (or BT656) data, up
         to 165 MHz

   -  VIP3 instance supporting up to

      -  Two separate 16-bit video ports for parallel RGB/YUV/RAW (or
         BT656/1120) data, up to 165 MHz

-  AM571x/DRA72x

   -  VIP1 instance supporting up to

      -  Two separate 24-bit video ports for parallel RGB/YUV/RAW (or
         BT656/1120) data, up to 165 MHz
      -  Two separate 8-bit video ports for YUV/RAW (or BT656) data, up
         to 165 MHz

|

.. rubric:: Driver Architecture
   :name: driver-architecture

| The VIP driver is a video capture driver built around the V4L2
  framework and is located in the directory
  drivers/media/platform/ti-vpe/ in the kernel tree.
| It is co-located with the VPE Mem-2-mem driver as it shares the VPDMA,
  color space converter (CSC) and scaler (SC) subcomponents with it.

Linux kernel driver for the VIP is implemented as per the V4L2 standard
for capture devices. VIP driver is responsible only for the programming
of the VIP device. For programming external video devices, we need a
V4L2 subdevice driver which is used in conjunction with the V4L2 driver.
It also uses some of the helper kernel libraries videobuf2 (VB2) for
common buffer operations, queue management and memory management.

-  `Linux Media Subsystem
   Documentation <https://linuxtv.org/downloads/v4l-dvb-apis/>`__
-  `Video for Linux
   API <https://linuxtv.org/downloads/v4l-dvb-apis-new/uapi/v4l/v4l2.html>`__
-  `V4L2 videobuf2 functions and data
   structures <https://linuxtv.org/downloads/v4l-dvb-apis/kapi/v4l2-videobuf2.html>`__
-  `V4L2
   sub-devices <https://linuxtv.org/downloads/v4l-dvb-apis-new/kapi/v4l2-subdev.html>`__

.. rubric:: V4L2 endpoint device tree bindings
   :name: v4l2-endpoint-device-tree-bindings

Different camera / video sources have different configuration parameters
when interfacing with the VIP video ports. Common interfacing properties
like Hsync, Vsync, Pclk polarities can be different across different
devices. V4L2 endpoint allows to describe these as part of device tree
definition. This makes the VIP driver generic enough to have no
dependency on the camera device. It also provides the flexibility to
work with new cameras by doing simple device tree modifications.

-  `V4L2 endpoint
   documentation <https://www.kernel.org/doc/Documentation/devicetree/bindings/media/video-interfaces.txt>`__

Following is an example showcasing the DT entries of VIP device node and
its usage when interfacing different video sources.

+----------------------------------------------------+---------------------------------------------+
| VIP device definition                              | Camera device definition                    |
+====================================================+=============================================+
| ::                                                 | ::                                          |
|                                                    |                                             |
|     vip1 {                                         |     ov10633@37 {                            |
|         #address-cells = <1>;                      |         compatible = "ovti,ov10633";        |
|         #size-cells = <0>;                         |         reg = <0x37>                        |
|         status = "okay";                           |         ...                                 |
|         ports {                                    |         port {                              |
|             vin1a: port@0 {                        |             cam1: endpoint {                |
|                  reg = <0>;                        |                 remote-endpoint = <&vin1a>; |
|                  #address-cells = <1>;             |                 hsync-active = <1>;         |
|                                                    |                 vsync-active = <1>;         |
|                  #size-cells = <0>;                |                 pclk-sample = <0>;          |
|                  status = "okay";                  |                                             |
|                  endpoint@0 {                      |             };                              |
|                      remote-endpoint = <&cam1>;    |         };                                  |
|                                                    |     };                                      |
|                  };                                |                                             |
|             };                                     |                                             |
|             ...                                    |                                             |
|             vin2a: port@2 {                        |                                             |
|                  ...                               |                                             |
|                  reg = <2>;                        |                                             |
|             };                                     |                                             |
|             ...                                    |                                             |
|         };                                         |                                             |
|     };                                             |                                             |
+----------------------------------------------------+---------------------------------------------+


.. rubric:: V4L2 asynchronous subdevice registration
   :name: v4l2-asynchronous-subdevice-registration

Each camera device that VIP driver communicates to is modelled as a V4L2
subdevice. In the probe sequence, VIP and camera drivers are probed at
different time. V4L2 async subdevice binding helps to bind the VIP
device and the camera device together. VIP driver looks for the camera
entries in the endpoints and registers (v4l2\_async\_notifier\_register)
a callback if any of the requested devices become available.
vip\_async\_bound implements the priority based binding which allows to
have multiple cameras muxed against same video port. The device tree
order determines which of these gets picked up by the driver. Note that
the V4L2 g/s\_input ioctls are not supported, userspace won't be able to
select specific camera with these ioctls.

Of course the target subdevice driver also needs to support the
asynchronous registration framework. On top of this the subdevice driver
**must** implements the following ioctls for the handshake with the VIP
driver to work properly:

-  get\_fmt()
-  set\_fmt()
-  enum\_mbus\_code()
-  enum\_frame\_sizes()
-  s\_stream()

|

.. rubric:: Driver Features
   :name: driver-features

Note: this is not a comprehensive list of features supported/not
supported.

.. rubric:: Supported Features
   :name: supported-features

-  VIP input Pixel formats

   -  Sub device is expected to support one of the below format. Only
      YUV422 interleaved format arranged as UYVY is supported in YUV
      mode. This restrictions in pixel arrangements is to take care of
      silicon errata i839 guidelines.
   -  The data formats mentioned in parenthesis in below table is in
      V4L2 Media Bus Format.

      -  For instance, a format where pixels are encoded as 8-bit YUV
         values downsampled to 4:2:2 and transferred as 2 8-bit bus
         samples per pixel in the U, Y, V, Y order is named as
         MEDIA\_BUS\_FMT\_UYVY8\_2X8.

   -  The data bus width can be 8 bit or 16 bit wide when capturing in
      UYVY mode.

      -  Default bus width configuration is 8 bit. When using 16 bit
         wide bus, specify the bus width in dts file as bus-width =
         <16>;

|

+---------------------+--------------------------+-----------------------+
| YUV                 | RGB                      | RAW Bayer 8-bit       |
+=====================+==========================+=======================+
| UYVY (UVYV8\_2x8)   | RGB24 (RGB888\_1X24)     | BGGR8 (SBGGR8\_1X8)   |
+---------------------+--------------------------+-----------------------+
|                     | RGB32 (ARGB8888\_1X32)   | GBRG8 (SGBRG8\_1X8)   |
+---------------------+--------------------------+-----------------------+
|                     |                          | GRBG8 (SGRBG8\_1X8)   |
+---------------------+--------------------------+-----------------------+
|                     |                          | RGGB8 (SRGGB8\_1X8)   |
+---------------------+--------------------------+-----------------------+

Table:  **Supported Input Pixel Format in FOURCC and V4L2
MEDIA\_BUS\_FMT**

|

-  Supported VIP output pixel formats

   -  Runtime pixel format availability is based on the sub-device
      capability.
      Use yavta --enum-formats /dev/video1 to get an accurate list.

+--------+--------+-------------------+
| YUV    | RGB    | RAW Bayer 8-bit   |
+========+========+===================+
| NV12   | RGB3   | BA81              |
+--------+--------+-------------------+
| YUYV   | BGR3   | GBRG              |
+--------+--------+-------------------+
| UYVY   | RGB4   | GRBG              |
+--------+--------+-------------------+
| VYUY   | BGR4   | RGGB              |
+--------+--------+-------------------+
| YVYU   |        |                   |
+--------+--------+-------------------+

Table:  **Supported Output Pixel Format**

-  Scaling (only available with YUV format)

   -  Down-scaling only (will use the closest native resolution larger
      than the desired frame size)
   -  Down-scaling ratio limitations -

      -  Horizontal - up to 1/8th
      -  Vertical - up to 3/16

-  Color Space Conversion

   -  YUV to RGB (tested)
   -  RGB to YUV (untested)

-  V4L2 single-planar buffers and interface
-  Supports MMAP buffers (allocated by kernel from global CMA pool) and
   also allows to export them as DMABUF
-  Supports DMABUF import (Reusing buffers from other drivers)
-  Discrete Sync capture
-  Embedded Sync capture in 8-bit mode
-  Multi-channel capture when using embedded sync

.. rubric:: Unsupported Features/Limitations By VIP Driver
   :name: unsupported-featureslimitations-by-vip-driver

-  Media Controller Framework
-  Cropping/Selection ioctls
-  TILER memory space
-  16 bit embedded capture
-  16 bit RAW capture
-  YUV444 Input format

   -  YUV444 mode is similar to RGB24 mode. Driver can be modified to
      enable YUV44 mode by referring to the RGB24 settings in vip.c file

-  Input format capture for YUV422 mode in arrangements other than UYVY

   -  Refer to the settings of Raw Bayer input format in vip.c file to
      enable other YUV input mode capture

-  Maximum capture resolution restricted to 2048x1536
-  HSYNC and Discrete Basic Mode set as 1 are hard coded in the driver
   and not controlled through dts entries. VIP driver register settings
   will need changes if the signals used for capture are DE (ACTVID)
   and/or Discrete Basic Mode set as 0.

|

.. rubric:: Hardware Limitations
   :name: hardware-limitations

.. Image:: /images/CSC_SC_PORTA_PORTB.png

VIP Slice

-  CSC, SC and/or DS processing in discrete sync mode is supported only
   for following combination -

   -  Input as RGB or UYVY format and output in supported YUV format

-  CSC, SC and/or DS processing is not supported for embedded sync input
   in multiplexed source mode
-  CSC and SC can not be used simultaneously by port A and port B of a
   Slice. For example, if port A is using CSC, then port B can only use
   SC but not CSC
-  Maximum input resolution when using SC is 2047x2047 pixels
   (irrespective of pixel size).
-  Maximum capture width when not using scaling is 8K bytes. This
   translates to maximum frame width of -

   -  4K when capturing in YUV422 mode (2 bytes/pixel)
   -  2.2K when capturing in RGB24 mode (3 bytes/pixel)
   -  8K when capturing as Raw Bayer 8-bit or other format treated as 1
      bytes/pixel

-  No restrictions on height of capture video

|

.. rubric:: Driver Configuration
   :name: driver-configuration-vip

.. rubric:: Kernel Configuration Options
   :name: kconfig-options-vip

ti-vip supports building both as built-in or as a module.

ti-vip can be found under "Device Drivers/Multimedia support/V4L
platform devices" in the kernel menuconfig. You need to enable V4L2
(CONFIG\_MEDIA\_SUPPORT, CONFIG\_MEDIA\_CAMERA\_SUPPORT) and then enable
V4L platform driver (CONFIG\_V4L\_PLATFORM\_DRIVERS) before you can
enable ti-vip (CONFIG\_VIDEO\_TI\_VIP).

|

.. rubric:: Driver Usage
   :name: driver-usage-vip

.. rubric:: Loading ti-vip
   :name: loading-ti-vip

If built as a module, you need to load all the v4l2-common,
videobuf2-core and videobuf2-dma-contig modules before ti-vip will
start.

.. rubric:: Using ti-vip
   :name: using-ti-vip

When ti-vip is enabled, the capture device will appear as /dev/videoX.
Standard V4L2 user space applications can be used as long as the
capability of the application matches.

-  **yavta example**
   Capture 800x600 YUYV video stream to file.

::

    yavta -c60 -fYUYV -Fvout_800x600_yuyv.yuv -s800x600 /dev/video1

yavta can be found from:

::

    http://git.ideasonboard.org/yavta.git

.. rubric:: Debugging
   :name: debugging-vip

As ti-vip driver is based on the V4L2 framework, framework level tracing
can be enable as follows:

-  echo 3 >/sys/class/video4linux/video1/dev\_debug
   This allows V4L2 ioctl calls to be logged.
-  echo 3 > /sys/module/videobuf2\_core/parameters/debug
   This allows VB2 buffers operation to be logged.

In addition ti-vip also has specific debug log which can be enabled as
follows:

-  echo 3 > /sys/module/ti\_vip/parameters/debug

.. rubric:: Troubleshooting common capture problem
   :name: troubleshooting-common-capture-problem

.. rubric:: Bootup/Probe checks
   :name: bootupprobe-checks

First thing to look for is if the video devices are created or not;
Check the bootlog for prints in the kernel bootlog.

::

    Check device probe status
    dmesg | grep ov1063x
    dmesg | grep video

Depending on the camera connected, the following prints can confirm the
probe being successful.

+------------------------------------------------------------+--------------------------------+
| Bootlog print                                              | Result                         |
+============================================================+================================+
| ov1063x 1-0037: ov1063x Product ID a6 Manufacturer ID 33   | Onboard camera probe success   |
+------------------------------------------------------------+--------------------------------+
| ov1063x X-00XX: Failed writing register 0x0103!            | Camera not connected           |
+------------------------------------------------------------+--------------------------------+

.. rubric:: No video captured
   :name: no-video-captured

When the capture application is launched, it is expected to start video
capture and display frames on to display. Sometimes, no video is not
displayed on the screen. To identify this being an issue with capture,
simple test can be done. Each VIP slice has a dedicated interrupt line.
If the capture is successful, the interrupt count should increase
periodically.

::

    Check interrupts to confirm capture failure
    cat /proc/interrupts | grep vip
    362:        941          0       GIC 102  vip1-s0
    363:        183          0       GIC 101  vip1-s1
    364:        241          0       GIC 100  vip2-s0
    365:          0          0       GIC  99  vip2-s1
    366:         46          0       GIC  98  vip3-s0
    367:          2          0       GIC  97  vip3-s1

In the above example, one can conclude that

-  Capture from Vin1, Vin2, Vin3, Vin5 is working fine.
-  Vin4(vip2-s1) capture was never attempted.
-  Vin6(vip3-s1) capture is failing (Note that first two interrupts
   occur even if the camera isn't connected. Refer VPDMA fifo)

Note that the IRQs are shared for different ports of same slice. This
means, vip1-s0 line will carry interrupts from both vin1a and vin1b.
This test can be used when only one of the port is in use.

.. rubric:: VIP Parser is not able to detect the video
   :name: vip-parser-is-not-able-to-detect-the-video

| Most of the time, external factors cause this failure. For a new board
  bringup, this is the most common issue. Following are the common root
  causes.
| As soon as the video port detects the sync signals, parser updates the
  detected video size in the PARSER\_SIZE register. This is useful for
  finding out wheather the video signals are getting to the VIP port or
  not. Note that, the parser size is calculated only based on the
  relative toggling of pclk, hsync, vsync. Also, the size includes any
  blanking data available in the stream. Following checks ensure if the
  video is detected by the video port

+--------------+------------------------+--------------------------+
| Video Port   | Parser size register   | Parser config register   |
+==============+========================+==========================+
| vin1a        | 0x48975530             | 0x48975504               |
+--------------+------------------------+--------------------------+
| vin1b        | 0x48975570             | 0x4897550C               |
+--------------+------------------------+--------------------------+
| vin2a        | 0x48975A30             | 0x48975A04               |
+--------------+------------------------+--------------------------+
| vin2b        | 0x48975A70             | 0x48975A0C               |
+--------------+------------------------+--------------------------+
| vin3a        | 0x48995530             | 0x48995504               |
+--------------+------------------------+--------------------------+
| vin3b        | 0x48995570             | 0x4899550C               |
+--------------+------------------------+--------------------------+
| vin4a        | 0x48995A30             | 0x48995A04               |
+--------------+------------------------+--------------------------+
| vin4b        | 0x48995A70             | 0x48995A0C               |
+--------------+------------------------+--------------------------+
| vin5a        | 0x489B5530             | 0x489B5504               |
+--------------+------------------------+--------------------------+
| vin6a        | 0x489B5A30             | 0x489B5A0C               |
+--------------+------------------------+--------------------------+

.. rubric:: Invalid parser configuration
   :name: invalid-parser-configuration

Depending on the camera used, certain parameters of the video port needs
to be configured correctly. Device tree definition (endpoint nodes) is
used for specifying these parameters.

+-----------------+----------------------------------------------+
| Usecase         | Required parameters                          |
+=================+==============================================+
| Parallel port   | Bus width (8/16bit for YUV, 24bit for RGB)   |
+-----------------+----------------------------------------------+
| Descrete sync   | hsync, vsync, pclk polarities                |
+-----------------+----------------------------------------------+
| Embedded sync   | Multiplexing method, channel numbers         |
+-----------------+----------------------------------------------+

To check if the correct parameters are being passed or not, **procfs**
can be used for checking values of some of the properties on target.

::

    Using procfs to read DT params
    cat /proc/device-tree/ocp/i2c@480720000/ov10635@37/compatible
    hexdump -b /proc/device-tree/ocp/i2c@480720000/ov10635@37/port/endpoint@0/pclk-sample
    hexdump -b /proc/device-tree/ocp/i2c@480720000/ov10635@37/port/endpoint@0/bus-width
    hexdump -b /proc/device-tree/ocp/i2c@480720000/ov10635@37/port/endpoint@0/channels

Note that some of the integer properties are not printable in ASCII
format. Using hexdump gives readability to read integer values from
device tree.

.. rubric:: Camera isn't started, pclk, syncs are dead
   :name: camera-isnt-started-pclk-syncs-are-dead

| This is a root cause where the camera board is not generating video
  signals in the desired format. Subdevice s\_stream op is supposed to
  perform all the I2C transactions to indicate sensor to start
  streaming. Failing to get the pixel clock at this time indicates some
  issue in the camera configuration. Most cameras have a power pin
  driver by one of the GPIO, make sure that the subdev driver requests
  for this GPIO.
| One other cause maybe due to incorrect board mux or pinmux
  configuration. It does not hurt to double check these.

.. rubric:: Video is being captured but image is pixelated or distorted
   :name: video-is-being-captured-but-image-is-pixelated-or-distorted

| If the image is pixelated you should double the signal polarity
  against what is currently set in the DT file. Most often when one or
  more of these are set wrong the image will get pixelated especially at
  higher resolution.
| If the image is distorted, you should double check that the sensor is
  generating the expected pixel clock. Also when trying to view the
  captured video, make sure you use the same frame size as used to
  capture it.

.. rubric:: FAQ
   :name: faq

.. rubric:: Can VIP be used as high speed interface to bring any data
   in?
   :name: can-vip-be-used-as-high-speed-interface-to-bring-any-data-in

VIP can be used as high speed interface to bring any data as is (without
any modifications) into the device. Following points to keep in mind –

-  Data should be sent in discrete sync mode.
-  No other VIP internal processing blocks like color space conversion,
   scaling or chroma format conversion should be used.
-  Refer to
   `Driver\_Features <http://processors.wiki.ti.com/index.php/Linux_Core_VIP_User's_Guide#Unsupported_Features.2FLimitations>`__
   section if there is need to bring data in resolution greater than the
   one supported by driver.
-  If the cropping feature is disabled in VIP parser due to the need for
   capturing larger resolution and if interested in capturing last frame
   (that could be only frame), FPGA need to send additional VSYNC signal
   else the last frame will not get transferred to DDR.
-  Add vip\_fmt entry in the vip\_formats table inside
   drivers/media/platform/ti-vpe/vip.c per sub-device driver need for
   ".fourcc", ".code" and ".colorspace". Keep ".coplanar" as 0. Refer to
   the entries of VPDMA\_DATA\_FMT\_RAW8 in
   drivers/media/platform/ti-vpe/vpdma.c file for "vpdma\_fmt" settings
   when using VIP slice in 8 bit port mode. Refer to the
   VPDMA\_DATA\_FMT\_RAW16 format settings for 16 bit mode. Note that
   VIP driver supports only 8 bit RAW mode. Enabling 16 bit RAW mode
   capture needs minor driver modifications. If custom entries are not
   needed, then any of the raw format entries can be used. In that case,
   sensor driver will need to configure media bus format as ".code"
   settings as shown in the vip\_fmt.

|

.. code-block:: c

    static struct vip_fmt vip_formats[VIP_MAX_ACTIVE_FMT] = {
        {
            .fourcc        = V4L2_PIX_FMT_SBGGR8,
            .code      = MEDIA_BUS_FMT_SBGGR8_1X8,
            .colorspace    = V4L2_COLORSPACE_SMPTE170M,
            .coplanar  = 0,
            .vpdma_fmt = { &vpdma_raw_fmts[VPDMA_DATA_FMT_RAW8],
                      },
        },

    const struct vpdma_data_format vpdma_raw_fmts[] = {
        [VPDMA_DATA_FMT_RAW8] = {
            .type      = VPDMA_DATA_FMT_TYPE_YUV,
            .data_type = DATA_TYPE_CBY422,
            .depth     = 8,
        },

.. rubric:: What’s the maximum frame rate possible for W\*H resolution
   using VIP?
   :name: whats-the-maximum-frame-rate-possible-for-wh-resolution-using-vip

As mentioned in
`Hardware\_Architecture <http://processors.wiki.ti.com/index.php/Linux_Core_VIP_User's_Guide#Hardware_Architecture>`__
section, each slice in VIP instance has one 24/16/8 bit port through
which data can come in. Each video port can be clocked up to 165 MHz.
Assuming 27% left spare for horizontal and vertical blanking, roughly
120 MHz left for actual data. If VIP Slice is configured in 8 bit port
mode, then 1 bytes can be brought in per clock cycle. In 8 bit port mode
and with 120 MHz clock for data capture, maximum possible capture rate
is 120 Mbytes/sec, in 16 bit port mode it will be 240 Mbytes/sec and in
24 bit port mode it will be 360 Mbytes/sec. Now for X\*Y resolution,
maximum possible frame rate can be calculated using following formula –

::

     FPS = 120 * 1000000 * port_mode/(frame_resolution * num_bytes_per_pixel)

In above formula -

-  port\_mode can take value of 1 for 8 bit, 2 for 16 bit and 3 for 24
   bit port mode configuration.
-  Frame\_resolution is product of width and height of frame.
-  num\_bytes\_per\_pixel is number of bytes per pixel. For example, if
   capturing in YUYV format it's value is 2, when capturing in RGB24
   format, it's value is 3.

.. rubric:: What is the maximum frame resolution that can be captured
   using VIP?
   :name: what-is-the-maximum-frame-resolution-that-can-be-captured-using-vip

Refer to
`Hardware\_Limitations <http://processors.wiki.ti.com/index.php/Linux_Core_VIP_User's_Guide#Hardware_Limitations>`__
section to understand maximum possible resolution supported by VIP IP.
Refer to
`Unsupported\_Features/Limitations <http://processors.wiki.ti.com/index.php/Linux_Core_VIP_User's_Guide#Unsupported_Features.2FLimitations_By_VIP_Driver>`__
section to understand the resolution supported by VIP driver. Driver
changes will be needed to capture the resolution beyond the one
supported by the driver but within VIP IP limits. Below are suggested
modifications inside driver. There may be more changes needed.

-  Change MAX\_W and MAX\_H in vip.c file per the desired capture
   resolution.
-  Disable hardware enabled cropping feature inside the driver if the
   desired resolution width is greater than 4K pixels (not bytes) and/or
   height is greater than 4K lines.

   -  To disable cropping, comment the function call to
      vip\_set\_crop\_parser() function inside vip\_setup\_parser()
      function defined in drivers/media/platform/ti-vpe/vip.c file

.. rubric:: Why I am not seeing any interrupt generated from the sensor?
   :name: why-i-am-not-seeing-any-interrupt-generated-from-the-sensor

Not getting any interrupts usually means the module is not
receiving/detecting video data. To proceed with debugging, probe the
pclk, vysnc and hsync signal at the connector. If they look as what you
are expecting, then verify the pinmux.

.. rubric:: How do I capture 10-bit or 12-bit YUV data?
   :name: how-do-i-capture-10-bit-or-12-bit-yuv-data

VIP can capture data in 8, 16 or 24 bus-width size. Configure VIP for 16
bit bus-width size in order to capture pixel of 10-bit or 12-bit size.
This includes dts file configuration and pin-mux configuration. Connect
the pixel size data lanes from the sensor board to VIP input port.
Ground or tie to VDD remaining unused pins. VIP will receive the
10-bit/12-bit data in 16-bit container in memory with 6/4 LSb or MSb bit
always being low or high based on how those unused bits are tied. Note
that when capturing 10-bit/12-bit data in 16 bit container, you can not
use any of the VIP internal processing module like scaling, format
conversion etc.

In dts file, specify the bus-width field as 16

::

    bus-width = <16>;    /* Used data lines */

.. rubric:: TI Board Specific Information
   :name: ti-board-specific-information

None at this time.

