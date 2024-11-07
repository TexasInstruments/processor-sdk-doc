.. http://processors.wiki.ti.com/index.php/ARM_Multimedia_Users_Guide

ARM Multimedia Users Guide
=============================


.. rubric:: Overview
   :name: overview-arm-mm-ug

|

Multimedia codecs on ARM based platforms could be optimised for better
performance using the tightly coupled
`**Neon** <http://processors.wiki.ti.com/index.php/Cortex_A8#What_is_Neon.3F>`__ co-processor. Neon
architecture works with its own independent pipeline and register file.
Neon technology is a 128 bit SIMD architecture extension for ARM
Cortex-A series processors. It is designed to provide acceleration for
multimedia applications.

.. rubric:: Supported Platforms
   :name: supported-platforms-arm-mm-ug

-  AM37x
-  Beagleboard-xM
-  AM35x
-  AM335x EVM
-  AM437x GP EVM
-  AM57xx GP EVM

.. rubric:: Multimedia on AM57xx Processor
   :name: multimedia-on-am57xx-processor

On AM57xx processor, ARM offloads H.264, VC1, MPEG-4, MPEG-2 and MJPEG
codecs processing to IVA-HD hardware accelerator. Please refer to
`AM57xx Multimedia
Training <Foundational_Components_Multimedia_IVAHD.html>`__
guide to learn more on AM57xx multimedia capabilities, demos, software
stack, gstreamer plugins and pipelines. Also refer to AM57xx `Graphics
Display Getting Started
Guide <Foundational_Components_Graphics.html>`__
to learn on AM57xx graphics software architecture, demos, tools and
display applications.

.. rubric:: Multimedia on Cortex-A8
   :name: multimedia-on-cortex-a8

.. rubric:: Cortex-A8 Features and Benefits
   :name: cortex-a8-features-and-benefits

-  Support ARM v7 with Advanced SIMD (NEON)
-  Support hierarchical cache memory
-  Up to 1 MB L2 cache
-  Up to 128-bit memory bandwidth
-  13-stage pipeline and enhanced branch prediction engine
-  Dual-issue of instructions

.. rubric:: Neon Features and Benefits
   :name: neon-features-and-benefits

-  Independent HW block to support advanced SIMD instructions
-  Comprehensive instruction set with support of 8, 16 & 32-bit signed &
   unsigned data types
-  256 byte register file (dual 32x64/16x128 view) with hybrid 32/64/128
   bit modes
-  Large register files enables efficient data handling and minimizes
   access to memory, thus enhancing data throughput
-  Processor can sleep sooner which leads to an overall dynamic power
   saving
-  Independent 10-stage pipeline
-  Dual-issue of limited instruction pairs
-  Significant code size reduction

.. rubric:: Neon support on opensource community
   :name: neon-support-on-opensource-community

NEON is currently supported in the following Open Source projects.

|

-  ffmpeg/libav

   -  LGPL media player used in many Linux distros
   -  NEON Video: MPEG-4 ASP, H.264 (AVC), VC-1, VP3, Theora
   -  NEON Audio: AAC, Vorbis, WMA

-  x264 –Google Summer Of Code 2009

   -  GPL H.264 encoder –e.g. for video conferencing

-  Bluez –official Linux Bluetooth protocol stack

   -  NEON sbc audio encoder

-  Pixman (part of cairo 2D graphics library)

   -  Compositing/alpha blending
   -  X.Org, Mozilla Firefox, fennec, & Webkit browsers
   -  e.g. fbCompositeSolidMask\_nx8x0565neon 8xfaster using NEON

-  Ubuntu 09.04 & 09.10 –fully supports NEON

   -  NEON versions of critical shared-libraries

-  Android –NEON optimizations

   -  Skia library, S32A\_D565\_Opaque 5xfaster using NEON
   -  Available in Google Skia tree from 03-Aug-2009

For additional details, please refer the `**NEON - ARM
website** <http://www.arm.com/products/processors/technologies/neon.php>`__.

.. rubric:: SDK Example Applications
   :name: sdk-example-applications

This application can be executed by selecting the "Multimedia" icon at
the top-level matrix.

**NOTE**

The very first GStreamer launch takes some time to initialize outputs or
set up decoders.

|

.. Image:: /images/Main_screen.png

|

.. rubric:: Codec portfolio
   :name: codec-portfolio

Processor SDK includes ARM based multimedia using opensource GPLv2+
FFmpeg/Libav codecs, the codec portfolio includes MPEG-4, H.264 for
video in VGA/WQVGA/480p resolution and AAC codec for audio. Codec
portforlio for Processor SDK on AM57xx device is listed
`here <Foundational_Components_Multimedia_IVAHD.html#capabilities-of-iva-hd-vpe-dsp-and-arm>`__

The script file to launch multimedia demo detects the display enabled
and accordingly decodes VGA or 480p video. In AM37x platform VGA clip is
decoded when LCD is enabled and 480p is decoded when DVI out is enabled.
Scripts in "Settings" menu can be used to switch between these two
displays.

.. rubric:: MPEG4 + AAC Decode
   :name: mpeg4-aac-decode

MPEG-4 + AAC Dec example application demonstrates use of MPEG-4 video
and AAC audio codec as mentioned in the description page below.

|

.. Image:: /images/Mpeg4aac.png

|


The multimedia pipeline is constructed using gst-launch, GStreamer
elements such as qtdemux is used for demuxing AV content. Parsers are
elements with single source pad and can be used to cut streams into
buffers, they do not modify the data otherwise.

::

    gst-launch-0.10 filesrc location=$filename ! qtdemux name=demux demux.audio_00 ! queue ! ffdec_aac ! alsasink sync=false demux.video_00 ! queue ! ffdec_mpeg4 ! ffmpegcolorspace ! fbdevsink device=/dev/fb0

"filename" is defined based on the selected display device which could
be LCD of DVI.

.. rubric:: MPEG4 Decode
   :name: mpeg4-decode

MPEG-4 decode example application demonstrates use of MPEG-4 video codec
as mentioned in the description page below.

|

.. Image:: /images/Mpeg4.png

|

::

    gst-launch-0.10 filesrc location=$filename ! mpeg4videoparse ! ffdec_mpeg4 ! ffmpegcolorspace ! fbdevsink device=/dev/fb0

|

.. rubric:: H.264 Decode
   :name: h.264-decode

H.264 decode example application demonstrates use of H.264 video codec
as mentioned in the description page below.

|

.. Image:: /images/H264.png

|

::

    gst-launch-0.10 filesrc location=$filename ! h264parse ! ffdec_h264 ! ffmpegcolorspace ! fbdevsink device=/dev/fb0

.. rubric:: AAC Decode
   :name: aac-decode

AAC decode example application demonstrates use of AAC video codec as
mentioned in the description page below.

|

.. Image:: /images/Aac.png

|

::

    gst-launch-0.10 filesrc location=$filename ! aacparse ! faad ! alsasink

.. rubric:: Streaming
   :name: streaming

Audio/Video data can be streamed from a server using souphttpsrc. For
example to stream audio content, if you set-up an apache server on your
host machine you can stream the audio file HistoryOfTI.aac located in
the files directory using the pipeline

::

    gst-launch souphttpsrc location=http://<ip address>/files/HistoryOfTI.aac ! aacparse ! faad ! alsasink

|

.. rubric:: Multimedia Peripheral Examples
   :name: multimedia-peripheral-examples

Examples of how to use several different multimedia peripherals can be
found on the `ARM Multimedia Peripheral
Examples <http://processors.wiki.ti.com/index.php/ARM_Multimedia_Peripheral_Examples>`__ page.

|

.. rubric:: SDK Multimedia Framework
   :name: sdk-multimedia-framework

Multimedia framework for cortex-a8 SDK will leverage GStreamer
multimedia stack with gst-ffmpeg plug-in's to support GPLv2+
FFmpeg/libav library code.

.. Image:: /images/SDKMMFwk.png

gst-launch is used to build and run basic multimedia pieplines to
demonstrate audio/avideo decoding examples.

.. Image:: /images/MMFwk.png

.. rubric:: GStreamer
   :name: gstreamer

-  Multimedia processing library
-  Provides uniform framework across platforms
-  Includes parsing & A/V sync support
-  Modular with flexibility to add new functionality via plugins
-  Easy bindings to other frameworks

Some of the build dependencies for GStreamer are shown here:

.. Image:: /images/GstBuildDependancies.png

.. rubric:: Open Source FFmpeg Codecs
   :name: open-source-ffmpeg-codecs

`**FFmpeg** <http://ffmpeg.org/>`__ is an open source project which
provides a cross platform multimedia solution.

-  Free audio and video decoder/encoder code licensed under GPLv2+
   (GPLv3 licensed codecs can be build separately)
-  A comprehensive suite of standard compliant multimedia codecs

| - Audio
| - Video
| - Image
| - Speech

-  Codec software package
-  Codec libraries with standard C based API
-  Audio/Video parsers that support popular multimedia content
-  Use of SIMD/NEON instructions `**cortex-A8 neon
   architecture** <http://processors.wiki.ti.com/index.php/Cortex-A8_Neon_Architecture>`__
-  Neon provides 1.6x-2.5x performance on complex video codecs

.. rubric:: Multimedia Neon Benchmark
   :name: multimedia-neon-benchmark

Test Parameters:

-  Sep 21 2009 snapshot of gst-ffmpeg.org
-  Real silicon measurements on Omap3 Beagleboard

+---------------+-----------+
| Resolution    | 480x270   |
+---------------+-----------+
| Frame Rate    | 30fps     |
+---------------+-----------+
| Audio         | 44.1KHz   |
+---------------+-----------+
| Video Codec   | H.264     |
+---------------+-----------+
| Audio Codec   | AAC       |
+---------------+-----------+

-  Benchmarks released by ARM demonstrating an overall performance
   improvement of ~2x.

.. Image:: /images/NeonPerf.png

.. rubric:: FFmpeg Codecs List
   :name: ffmpeg-codecs-list

.. rubric:: FFmpeg Codec Licensing
   :name: ffmpeg-codec-licensing

FFmpeg libraries include LGPL, GPLv2, GPLv3 and other license based
codecs, enabling GPLv3 codecs subjects the entire framework to GPLv3
license. In the Sitara SDK GPLv2+ licensed codecs are enabled. Enabling
Additional details of `**legal and
license** <http://ffmpeg.org/legal.html>`__ of these codecs can be found
on the FFmpeg/libav webpage.

.. rubric:: GPLv2+ codecs list
   :name: gplv2-codecs-list

+--------------------------------------+--------------------------------------+
| Codec                                | Description                          |
+--------------------------------------+--------------------------------------+
| ffenc\_a64multi                      | FFmpeg Multicolor charset for        |
|                                      | Commodore 64 encoder                 |
+--------------------------------------+--------------------------------------+
| ffenc\_a64multi5                     | FFmpeg Multicolor charset for        |
|                                      | Commodore 64, extended with 5th      |
|                                      | color (colram) encoder               |
+--------------------------------------+--------------------------------------+
| ffenc\_asv1                          | FFmpeg ASUS V1 encoder               |
+--------------------------------------+--------------------------------------+
| ffenc\_asv2                          | FFmpeg ASUS V2 encoder               |
+--------------------------------------+--------------------------------------+
| ffenc\_bmp                           | FFmpeg BMP image encoder             |
+--------------------------------------+--------------------------------------+
| ffenc\_dnxhd                         | FFmpeg VC3/DNxHD encoder             |
+--------------------------------------+--------------------------------------+
| ffenc\_dvvideo                       | FFmpeg DV (Digital Video) encoder    |
+--------------------------------------+--------------------------------------+
| ffenc\_ffv1                          | FFmpeg FFmpeg video codec #1 encoder |
+--------------------------------------+--------------------------------------+
| ffenc\_ffvhuff                       | FFmpeg Huffyuv FFmpeg variant        |
|                                      | encoder                              |
+--------------------------------------+--------------------------------------+
| ffenc\_flashsv                       | FFmpeg Flash Screen Video encoder    |
+--------------------------------------+--------------------------------------+
| ffenc\_flv                           | FFmpeg Flash Video (FLV) / Sorenson  |
|                                      | Spark / Sorenson H.263 encoder       |
+--------------------------------------+--------------------------------------+
| ffenc\_h261                          | FFmpeg H.261 encoder                 |
+--------------------------------------+--------------------------------------+
| ffenc\_h263                          | FFmpeg H.263 / H.263-1996 encoder    |
+--------------------------------------+--------------------------------------+
| ffenc\_h263p                         | FFmpeg H.263+ / H.263-1998 / H.263   |
|                                      | version 2 encoder                    |
+--------------------------------------+--------------------------------------+
| ffenc\_huffyuv                       | FFmpeg Huffyuv / HuffYUV encoder     |
+--------------------------------------+--------------------------------------+
| ffenc\_jpegls                        | FFmpeg JPEG-LS encoder               |
+--------------------------------------+--------------------------------------+
| ffenc\_ljpeg                         | FFmpeg Lossless JPEG encoder         |
+--------------------------------------+--------------------------------------+
| ffenc\_mjpeg                         | FFmpeg MJPEG (Motion JPEG) encoder   |
+--------------------------------------+--------------------------------------+
| ffenc\_mpeg1video                    | FFmpeg MPEG-1 video encoder          |
+--------------------------------------+--------------------------------------+
| ffenc\_mpeg4                         | FFmpeg MPEG-4 part 2 encoder         |
+--------------------------------------+--------------------------------------+
| ffenc\_msmpeg4v1                     | FFmpeg MPEG-4 part 2 Microsoft       |
|                                      | variant version 1 encoder            |
+--------------------------------------+--------------------------------------+
| ffenc\_msmpeg4v2                     | FFmpeg MPEG-4 part 2 Microsoft       |
|                                      | variant version 2 encoder            |
+--------------------------------------+--------------------------------------+
| ffenc\_msmpeg4                       | FFmpeg MPEG-4 part 2 Microsoft       |
|                                      | variant version 3 encoder            |
+--------------------------------------+--------------------------------------+
| ffenc\_pam                           | FFmpeg PAM (Portable AnyMap) image   |
|                                      | encoder                              |
+--------------------------------------+--------------------------------------+
| ffenc\_pbm                           | FFmpeg PBM (Portable BitMap) image   |
|                                      | encoder                              |
+--------------------------------------+--------------------------------------+
| ffenc\_pcx                           | FFmpeg PC Paintbrush PCX image       |
|                                      | encoder                              |
+--------------------------------------+--------------------------------------+
| ffenc\_pgm                           | FFmpeg PGM (Portable GrayMap) image  |
|                                      | encoder                              |
+--------------------------------------+--------------------------------------+
| ffenc\_pgmyuv                        | FFmpeg PGMYUV (Portable GrayMap YUV) |
|                                      | image encoder                        |
+--------------------------------------+--------------------------------------+
| ffenc\_png                           | FFmpeg PNG image encoder             |
+--------------------------------------+--------------------------------------+
| ffenc\_ppm                           | FFmpeg PPM (Portable PixelMap) image |
|                                      | encoder                              |
+--------------------------------------+--------------------------------------+
| ffenc\_qtrle                         | FFmpeg QuickTime Animation (RLE)     |
|                                      | video encoder                        |
+--------------------------------------+--------------------------------------+
| ffenc\_roqvideo                      | FFmpeg id RoQ video encoder          |
+--------------------------------------+--------------------------------------+
| ffenc\_rv10                          | FFmpeg RealVideo 1.0 encoder         |
+--------------------------------------+--------------------------------------+
| ffenc\_rv20                          | FFmpeg RealVideo 2.0 encoder         |
+--------------------------------------+--------------------------------------+
| ffenc\_sgi                           | FFmpeg SGI image encoder             |
+--------------------------------------+--------------------------------------+
| ffenc\_snow                          | FFmpeg Snow encoder                  |
+--------------------------------------+--------------------------------------+
| ffenc\_svq1                          | FFmpeg Sorenson Vector Quantizer 1 / |
|                                      | Sorenson Video 1 / SVQ1 encoder      |
+--------------------------------------+--------------------------------------+
| ffenc\_targa                         | FFmpeg Truevision Targa image        |
|                                      | encoder                              |
+--------------------------------------+--------------------------------------+
| ffenc\_tiff                          | FFmpeg TIFF image encoder            |
+--------------------------------------+--------------------------------------+
| ffenc\_wmv1                          | FFmpeg Windows Media Video 7 encoder |
+--------------------------------------+--------------------------------------+
| ffenc\_wmv2                          | FFmpeg Windows Media Video 8 encoder |
+--------------------------------------+--------------------------------------+
| ffenc\_zmbv                          | FFmpeg Zip Motion Blocks Video       |
|                                      | encoder                              |
+--------------------------------------+--------------------------------------+
| ffenc\_aac                           | FFmpeg Advanced Audio Coding encoder |
+--------------------------------------+--------------------------------------+
| ffenc\_ac3                           | FFmpeg ATSC A/52A (AC-3) encoder     |
+--------------------------------------+--------------------------------------+
| ffenc\_alac                          | FFmpeg ALAC (Apple Lossless Audio    |
|                                      | Codec) encoder                       |
+--------------------------------------+--------------------------------------+
| ffenc\_mp2                           | FFmpeg MP2 (MPEG audio layer 2)      |
|                                      | encoder                              |
+--------------------------------------+--------------------------------------+
| ffenc\_nellymoser                    | FFmpeg Nellymoser Asao encoder       |
+--------------------------------------+--------------------------------------+
| ffenc\_real\_144                     | FFmpeg RealAudio 1.0 (14.4K) encoder |
|                                      | encoder                              |
+--------------------------------------+--------------------------------------+
| ffenc\_sonic                         | FFmpeg Sonic encoder                 |
+--------------------------------------+--------------------------------------+
| ffenc\_sonicls                       | FFmpeg Sonic lossless encoder        |
+--------------------------------------+--------------------------------------+
| ffenc\_wmav1                         | FFmpeg Windows Media Audio 1 encoder |
+--------------------------------------+--------------------------------------+
| ffenc\_wmav2                         | FFmpeg Windows Media Audio 2 encoder |
+--------------------------------------+--------------------------------------+
| ffenc\_roq\_dpcm                     | FFmpeg id RoQ DPCM encoder           |
+--------------------------------------+--------------------------------------+
| ffenc\_adpcm\_adx                    | FFmpeg SEGA CRI ADX ADPCM encoder    |
+--------------------------------------+--------------------------------------+
| ffenc\_g722                          | FFmpeg G.722 ADPCM encoder           |
+--------------------------------------+--------------------------------------+
| ffenc\_g726                          | FFmpeg G.726 ADPCM encoder           |
+--------------------------------------+--------------------------------------+
| ffenc\_adpcm\_ima\_qt                | FFmpeg ADPCM IMA QuickTime encoder   |
+--------------------------------------+--------------------------------------+
| ffenc\_adpcm\_ima\_wav               | FFmpeg ADPCM IMA WAV encoder         |
+--------------------------------------+--------------------------------------+
| ffenc\_adpcm\_ms                     | FFmpeg ADPCM Microsoft encoder       |
+--------------------------------------+--------------------------------------+
| ffenc\_adpcm\_swf                    | FFmpeg ADPCM Shockwave Flash encoder |
+--------------------------------------+--------------------------------------+
| ffenc\_adpcm\_yamaha                 | FFmpeg ADPCM Yamaha encoder          |
+--------------------------------------+--------------------------------------+
| ffenc\_ass                           | FFmpeg Advanced SubStation Alpha     |
|                                      | subtitle encoder                     |
+--------------------------------------+--------------------------------------+
| ffenc\_dvbsub                        | FFmpeg DVB subtitles encoder         |
+--------------------------------------+--------------------------------------+
| ffenc\_dvdsub                        | FFmpeg DVD subtitles encoder         |
+--------------------------------------+--------------------------------------+
| ffenc\_xsub                          | FFmpeg DivX subtitles (XSUB) encoder |
+--------------------------------------+--------------------------------------+
| ffdec\_aasc                          | FFmpeg Autodesk RLE decoder          |
+--------------------------------------+--------------------------------------+
| ffdec\_amv                           | FFmpeg AMV Video decoder             |
+--------------------------------------+--------------------------------------+
| ffdec\_anm                           | FFmpeg Deluxe Paint Animation        |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_ansi                          | FFmpeg ASCII/ANSI art decoder        |
+--------------------------------------+--------------------------------------+
| ffdec\_asv1                          | FFmpeg ASUS V1 decoder               |
+--------------------------------------+--------------------------------------+
| ffdec\_asv2                          | FFmpeg ASUS V2 decoder               |
+--------------------------------------+--------------------------------------+
| ffdec\_aura                          | FFmpeg Auravision AURA decoder       |
+--------------------------------------+--------------------------------------+
| ffdec\_aura2                         | FFmpeg Auravision Aura 2 decoder     |
+--------------------------------------+--------------------------------------+
| ffdec\_avs                           | FFmpeg AVS (Audio Video Standard)    |
|                                      | video decoder                        |
+--------------------------------------+--------------------------------------+
| ffdec\_bethsoftvid                   | FFmpeg Bethesda VID video decoder    |
+--------------------------------------+--------------------------------------+
| ffdec\_bfi                           | FFmpeg Brute Force & Ignorance       |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_binkvideo                     | FFmpeg Bink video decoder            |
+--------------------------------------+--------------------------------------+
| ffdec\_bmp                           | FFmpeg BMP image decoder             |
+--------------------------------------+--------------------------------------+
| ffdec\_c93                           | FFmpeg Interplay C93 decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_cavs                          | FFmpeg Chinese AVS video (AVS1-P2,   |
|                                      | JiZhun profile) decoder              |
+--------------------------------------+--------------------------------------+
| ffdec\_cdgraphics                    | FFmpeg CD Graphics video decoder     |
+--------------------------------------+--------------------------------------+
| ffdec\_cinepak                       | FFmpeg Cinepak decoder               |
+--------------------------------------+--------------------------------------+
| ffdec\_cljr                          | FFmpeg Cirrus Logic AccuPak decoder  |
+--------------------------------------+--------------------------------------+
| ffdec\_camstudio                     | FFmpeg CamStudio decoder             |
+--------------------------------------+--------------------------------------+
| ffdec\_cyuv                          | FFmpeg Creative YUV (CYUV) decoder   |
+--------------------------------------+--------------------------------------+
| ffdec\_dnxhd                         | FFmpeg VC3/DNxHD decoder             |
+--------------------------------------+--------------------------------------+
| ffdec\_dpx                           | FFmpeg DPX image decoder             |
+--------------------------------------+--------------------------------------+
| ffdec\_dsicinvideo                   | FFmpeg Delphine Software             |
|                                      | International CIN video decoder      |
+--------------------------------------+--------------------------------------+
| ffdec\_dvvideo                       | FFmpeg DV (Digital Video) decoder    |
+--------------------------------------+--------------------------------------+
| ffdec\_dxa                           | FFmpeg Feeble Files/ScummVM DXA      |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_eacmv                         | FFmpeg Electronic Arts CMV video     |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_eamad                         | FFmpeg Electronic Arts Madcow Video  |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_eatgq                         | FFmpeg Electronic Arts TGQ video     |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_eatgv                         | FFmpeg Electronic Arts TGV video     |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_eatqi                         | FFmpeg Electronic Arts TQI Video     |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_8bps                          | FFmpeg QuickTime 8BPS video decoder  |
+--------------------------------------+--------------------------------------+
| ffdec\_8svx\_exp                     | FFmpeg 8SVX exponential decoder      |
+--------------------------------------+--------------------------------------+
| ffdec\_8svx\_fib                     | FFmpeg 8SVX fibonacci decoder        |
+--------------------------------------+--------------------------------------+
| ffdec\_escape124                     | FFmpeg Escape 124 decoder            |
+--------------------------------------+--------------------------------------+
| ffdec\_ffv1                          | FFmpeg FFmpeg video codec #1 decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_ffvhuff                       | FFmpeg Huffyuv FFmpeg variant        |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_flashsv                       | FFmpeg Flash Screen Video v1 decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_flic                          | FFmpeg Autodesk Animator Flic video  |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_flv                           | FFmpeg Flash Video (FLV) / Sorenson  |
|                                      | Spark / Sorenson H.263 decoder       |
+--------------------------------------+--------------------------------------+
| ffdec\_4xm                           | FFmpeg 4X Movie decoder              |
+--------------------------------------+--------------------------------------+
| ffdec\_fraps                         | FFmpeg Fraps decoder                 |
+--------------------------------------+--------------------------------------+
| ffdec\_FRWU                          | FFmpeg Forward Uncompressed decoder  |
+--------------------------------------+--------------------------------------+
| ffdec\_h261                          | FFmpeg H.261 decoder                 |
+--------------------------------------+--------------------------------------+
| ffdec\_h263                          | FFmpeg H.263 / H.263-1996, H.263+ /  |
|                                      | H.263-1998 / H.263 version 2 decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_h263i                         | FFmpeg Intel H.263 decoder           |
+--------------------------------------+--------------------------------------+
| ffdec\_h264                          | FFmpeg H.264 / AVC / MPEG-4 AVC /    |
|                                      | MPEG-4 part 10 decoder               |
+--------------------------------------+--------------------------------------+
| ffdec\_huffyuv                       | FFmpeg Huffyuv / HuffYUV decoder     |
+--------------------------------------+--------------------------------------+
| ffdec\_idcinvideo                    | FFmpeg id Quake II CIN video decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_iff\_byterun1                 | FFmpeg IFF ByteRun1 decoder          |
+--------------------------------------+--------------------------------------+
| ffdec\_iff\_ilbm                     | FFmpeg IFF ILBM decoder              |
+--------------------------------------+--------------------------------------+
| ffdec\_indeo2                        | FFmpeg Intel Indeo 2 decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_indeo3                        | FFmpeg Intel Indeo 3 decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_indeo5                        | FFmpeg Intel Indeo Video Interactive |
|                                      | 5 decoder                            |
+--------------------------------------+--------------------------------------+
| ffdec\_interplayvideo                | FFmpeg Interplay MVE video decoder   |
+--------------------------------------+--------------------------------------+
| ffdec\_jpegls                        | FFmpeg JPEG-LS decoder               |
+--------------------------------------+--------------------------------------+
| ffdec\_kgv1                          | FFmpeg Kega Game Video decoder       |
+--------------------------------------+--------------------------------------+
| ffdec\_kmvc                          | FFmpeg Karl Morton's video codec     |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_loco                          | FFmpeg LOCO decoder                  |
+--------------------------------------+--------------------------------------+
| ffdec\_mdec                          | FFmpeg Sony PlayStation MDEC (Motion |
|                                      | DECoder) decoder                     |
+--------------------------------------+--------------------------------------+
| ffdec\_mimic                         | FFmpeg Mimic decoder                 |
+--------------------------------------+--------------------------------------+
| ffdec\_mjpeg                         | FFmpeg MJPEG (Motion JPEG) decoder   |
+--------------------------------------+--------------------------------------+
| ffdec\_mjpegb                        | FFmpeg Apple MJPEG-B decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_mmvideo                       | FFmpeg American Laser Games MM Video |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_motionpixels                  | FFmpeg Motion Pixels video decoder   |
+--------------------------------------+--------------------------------------+
| ffdec\_mpeg4                         | FFmpeg MPEG-4 part 2 decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_mpegvideo                     | FFmpeg MPEG-1 video decoder          |
+--------------------------------------+--------------------------------------+
| ffdec\_msmpeg4v1                     | FFmpeg MPEG-4 part 2 Microsoft       |
|                                      | variant version 1 decoder            |
+--------------------------------------+--------------------------------------+
| ffdec\_msmpeg4v2                     | FFmpeg MPEG-4 part 2 Microsoft       |
|                                      | variant version 2 decoder            |
+--------------------------------------+--------------------------------------+
| ffdec\_msmpeg4                       | FFmpeg MPEG-4 part 2 Microsoft       |
|                                      | variant version 3 decoder            |
+--------------------------------------+--------------------------------------+
| ffdec\_msrle                         | FFmpeg Microsoft RLE decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_msvideo1                      | FFmpeg Microsoft Video 1 decoder     |
+--------------------------------------+--------------------------------------+
| ffdec\_mszh                          | FFmpeg LCL (LossLess Codec Library)  |
|                                      | MSZH decoder                         |
+--------------------------------------+--------------------------------------+
| ffdec\_nuv                           | FFmpeg NuppelVideo/RTJPEG decoder    |
+--------------------------------------+--------------------------------------+
| ffdec\_pam                           | FFmpeg PAM (Portable AnyMap) image   |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_pbm                           | FFmpeg PBM (Portable BitMap) image   |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_pcx                           | FFmpeg PC Paintbrush PCX image       |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_pgm                           | FFmpeg PGM (Portable GrayMap) image  |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_pgmyuv                        | FFmpeg PGMYUV (Portable GrayMap YUV) |
|                                      | image decoder                        |
+--------------------------------------+--------------------------------------+
| ffdec\_pictor                        | FFmpeg Pictor/PC Paint decoder       |
+--------------------------------------+--------------------------------------+
| ffdec\_png                           | FFmpeg PNG image decoder             |
+--------------------------------------+--------------------------------------+
| ffdec\_ppm                           | FFmpeg PPM (Portable PixelMap) image |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_ptx                           | FFmpeg V.Flash PTX image decoder     |
+--------------------------------------+--------------------------------------+
| ffdec\_qdraw                         | FFmpeg Apple QuickDraw decoder       |
+--------------------------------------+--------------------------------------+
| ffdec\_qpeg                          | FFmpeg Q-team QPEG decoder           |
+--------------------------------------+--------------------------------------+
| ffdec\_qtrle                         | FFmpeg QuickTime Animation (RLE)     |
|                                      | video decoder                        |
+--------------------------------------+--------------------------------------+
| ffdec\_r10k                          | FFmpeg AJA Kona 10-bit RGB Codec     |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_rl2                           | FFmpeg RL2 video decoder             |
+--------------------------------------+--------------------------------------+
| ffdec\_roqvideo                      | FFmpeg id RoQ video decoder          |
+--------------------------------------+--------------------------------------+
| ffdec\_rpza                          | FFmpeg QuickTime video (RPZA)        |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_rv10                          | FFmpeg RealVideo 1.0 decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_rv20                          | FFmpeg RealVideo 2.0 decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_rv30                          | FFmpeg RealVideo 3.0 decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_rv40                          | FFmpeg RealVideo 4.0 decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_sgi                           | FFmpeg SGI image decoder             |
+--------------------------------------+--------------------------------------+
| ffdec\_smackvid                      | FFmpeg Smacker video decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_smc                           | FFmpeg QuickTime Graphics (SMC)      |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_snow                          | FFmpeg Snow decoder                  |
+--------------------------------------+--------------------------------------+
| ffdec\_sp5x                          | FFmpeg Sunplus JPEG (SP5X) decoder   |
+--------------------------------------+--------------------------------------+
| ffdec\_sunrast                       | FFmpeg Sun Rasterfile image decoder  |
+--------------------------------------+--------------------------------------+
| ffdec\_svq1                          | FFmpeg Sorenson Vector Quantizer 1 / |
|                                      | Sorenson Video 1 / SVQ1 decoder      |
+--------------------------------------+--------------------------------------+
| ffdec\_svq3                          | FFmpeg Sorenson Vector Quantizer 3 / |
|                                      | Sorenson Video 3 / SVQ3 decoder      |
+--------------------------------------+--------------------------------------+
| ffdec\_targa                         | FFmpeg Truevision Targa image        |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_thp                           | FFmpeg Nintendo Gamecube THP video   |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_tiertexseqvideo               | FFmpeg Tiertex Limited SEQ video     |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_tiff                          | FFmpeg TIFF image decoder            |
+--------------------------------------+--------------------------------------+
| ffdec\_tmv                           | FFmpeg 8088flex TMV decoder          |
+--------------------------------------+--------------------------------------+
| ffdec\_truemotion1                   | FFmpeg Duck TrueMotion 1.0 decoder   |
+--------------------------------------+--------------------------------------+
| ffdec\_truemotion2                   | FFmpeg Duck TrueMotion 2.0 decoder   |
+--------------------------------------+--------------------------------------+
| ffdec\_camtasia                      | FFmpeg TechSmith Screen Capture      |
|                                      | Codec decoder                        |
+--------------------------------------+--------------------------------------+
| ffdec\_txd                           | FFmpeg Renderware TXD (TeXture       |
|                                      | Dictionary) image decoder            |
+--------------------------------------+--------------------------------------+
| ffdec\_ultimotion                    | FFmpeg IBM UltiMotion decoder        |
+--------------------------------------+--------------------------------------+
| ffdec\_vb                            | FFmpeg Beam Software VB decoder      |
+--------------------------------------+--------------------------------------+
| ffdec\_vc1                           | FFmpeg SMPTE VC-1 decoder            |
+--------------------------------------+--------------------------------------+
| ffdec\_vcr1                          | FFmpeg ATI VCR1 decoder              |
+--------------------------------------+--------------------------------------+
| ffdec\_vmdvideo                      | FFmpeg Sierra VMD video decoder      |
+--------------------------------------+--------------------------------------+
| ffdec\_vmnc                          | FFmpeg VMware Screen Codec / VMware  |
|                                      | Video decoder                        |
+--------------------------------------+--------------------------------------+
| ffdec\_vp3                           | FFmpeg On2 VP3 decoder               |
+--------------------------------------+--------------------------------------+
| ffdec\_vp5                           | FFmpeg On2 VP5 decoder               |
+--------------------------------------+--------------------------------------+
| ffdec\_vp6                           | FFmpeg On2 VP6 decoder               |
+--------------------------------------+--------------------------------------+
| ffdec\_vp6a                          | FFmpeg On2 VP6 (Flash version, with  |
|                                      | alpha channel) decoder               |
+--------------------------------------+--------------------------------------+
| ffdec\_vp6f                          | FFmpeg On2 VP6 (Flash version)       |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_vp8                           | FFmpeg On2 VP8 decoder               |
+--------------------------------------+--------------------------------------+
| ffdec\_vqavideo                      | FFmpeg Westwood Studios VQA (Vector  |
|                                      | Quantized Animation) video decoder   |
+--------------------------------------+--------------------------------------+
| ffdec\_wmv1                          | FFmpeg Windows Media Video 7 decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_wmv2                          | FFmpeg Windows Media Video 8 decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_wmv3                          | FFmpeg Windows Media Video 9 decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_wnv1                          | FFmpeg Winnov WNV1 decoder           |
+--------------------------------------+--------------------------------------+
| ffdec\_xan\_wc3                      | FFmpeg Wing Commander III / Xan      |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_xl                            | FFmpeg Miro VideoXL decoder          |
+--------------------------------------+--------------------------------------+
| ffdec\_yop                           | FFmpeg Psygnosis YOP Video decoder   |
+--------------------------------------+--------------------------------------+
| ffdec\_zlib                          | FFmpeg LCL (LossLess Codec Library)  |
|                                      | ZLIB decoder                         |
+--------------------------------------+--------------------------------------+
| ffdec\_zmbv                          | FFmpeg Zip Motion Blocks Video       |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_aac                           | FFmpeg Advanced Audio Coding decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_aac\_latm                     | FFmpeg AAC LATM (Advanced Audio      |
|                                      | Codec LATM syntax) decoder           |
+--------------------------------------+--------------------------------------+
| ffdec\_ac3                           | FFmpeg ATSC A/52A (AC-3) decoder     |
+--------------------------------------+--------------------------------------+
| ffdec\_alac                          | FFmpeg ALAC (Apple Lossless Audio    |
|                                      | Codec) decoder                       |
+--------------------------------------+--------------------------------------+
| ffdec\_als                           | FFmpeg MPEG-4 Audio Lossless Coding  |
|                                      | (ALS) decoder                        |
+--------------------------------------+--------------------------------------+
| ffdec\_amrnb                         | FFmpeg Adaptive Multi-Rate           |
|                                      | NarrowBand decoder                   |
+--------------------------------------+--------------------------------------+
| ffdec\_ape                           | FFmpeg Monkey's Audio decoder        |
+--------------------------------------+--------------------------------------+
| ffdec\_atrac1                        | FFmpeg Atrac 1 (Adaptive TRansform   |
|                                      | Acoustic Coding) decoder             |
+--------------------------------------+--------------------------------------+
| ffdec\_atrac3                        | FFmpeg Atrac 3 (Adaptive TRansform   |
|                                      | Acoustic Coding 3) decoder           |
+--------------------------------------+--------------------------------------+
| ffdec\_binkaudio\_dct                | FFmpeg Bink Audio (DCT) decoder      |
+--------------------------------------+--------------------------------------+
| ffdec\_binkaudio\_rdft               | FFmpeg Bink Audio (RDFT) decoder     |
+--------------------------------------+--------------------------------------+
| ffdec\_cook                          | FFmpeg COOK decoder                  |
+--------------------------------------+--------------------------------------+
| ffdec\_dca                           | FFmpeg DCA (DTS Coherent Acoustics)  |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_dsicinaudio                   | FFmpeg Delphine Software             |
|                                      | International CIN audio decoder      |
+--------------------------------------+--------------------------------------+
| ffdec\_eac3                          | FFmpeg ATSC A/52B (AC-3, E-AC-3)     |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_flac                          | FFmpeg FLAC (Free Lossless Audio     |
|                                      | Codec) decoder                       |
+--------------------------------------+--------------------------------------+
| ffdec\_gsm                           | FFmpeg GSM decoder                   |
+--------------------------------------+--------------------------------------+
| ffdec\_gsm\_ms                       | FFmpeg GSM Microsoft variant decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_imc                           | FFmpeg IMC (Intel Music Coder)       |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_mace3                         | FFmpeg MACE (Macintosh Audio         |
|                                      | Compression/Expansion) 3             |
+--------------------------------------+--------------------------------------+
| ffdec\_mace6                         | FFmpeg MACE (Macintosh Audio         |
|                                      | Compression/Expansion) 6             |
+--------------------------------------+--------------------------------------+
| ffdec\_mlp                           | FFmpeg MLP (Meridian Lossless        |
|                                      | Packing) decoder                     |
+--------------------------------------+--------------------------------------+
| ffdec\_mp1float                      | FFmpeg MP1 (MPEG audio layer 1)      |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_mp2float                      | FFmpeg MP2 (MPEG audio layer 2)      |
|                                      | decoder                              |
|                                      | |                                    |
+--------------------------------------+--------------------------------------+
| ffdec\_mpc7                          | FFmpeg Musepack SV7 decoder          |
+--------------------------------------+--------------------------------------+
| ffdec\_mpc8                          | FFmpeg Musepack SV8 decoder          |
+--------------------------------------+--------------------------------------+
| ffdec\_nellymoser                    | FFmpeg Nellymoser Asao decoder       |
+--------------------------------------+--------------------------------------+
| ffdec\_qcelp                         | FFmpeg QCELP / PureVoice decoder     |
+--------------------------------------+--------------------------------------+
| ffdec\_qdm2                          | FFmpeg QDesign Music Codec 2 decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_real\_144                     | FFmpeg RealAudio 1.0 (14.4K) decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_real\_288                     | FFmpeg RealAudio 2.0 (28.8K) decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_shorten                       | FFmpeg Shorten decoder               |
+--------------------------------------+--------------------------------------+
| ffdec\_sipr                          | FFmpeg RealAudio SIPR / ACELP.NET    |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_smackaud                      | FFmpeg Smacker audio decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_sonic                         | FFmpeg Sonic decoder                 |
+--------------------------------------+--------------------------------------+
| ffdec\_truehd                        | FFmpeg TrueHD decoder                |
+--------------------------------------+--------------------------------------+
| ffdec\_truespeech                    | FFmpeg DSP Group TrueSpeech decoder  |
+--------------------------------------+--------------------------------------+
| ffdec\_tta                           | FFmpeg True Audio (TTA) decoder      |
+--------------------------------------+--------------------------------------+
| ffdec\_twinvq                        | FFmpeg VQF TwinVQ decoder            |
+--------------------------------------+--------------------------------------+
| ffdec\_vmdaudio                      | FFmpeg Sierra VMD audio decoder      |
+--------------------------------------+--------------------------------------+
| ffdec\_wmapro                        | FFmpeg Windows Media Audio 9         |
|                                      | Professional decoder                 |
+--------------------------------------+--------------------------------------+
| ffdec\_wmav1                         | FFmpeg Windows Media Audio 1 decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_wmav2                         | FFmpeg Windows Media Audio 2 decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_wmavoice                      | FFmpeg Windows Media Audio Voice     |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_ws\_snd1                      | FFmpeg Westwood Audio (SND1) decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_pcm\_lxf                      | FFmpeg PCM signed 20-bit             |
|                                      | little-endian planar decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_interplay\_dpcm               | FFmpeg DPCM Interplay decoder        |
+--------------------------------------+--------------------------------------+
| ffdec\_roq\_dpcm                     | FFmpeg DPCM id RoQ decoder           |
+--------------------------------------+--------------------------------------+
| ffdec\_sol\_dpcm                     | FFmpeg DPCM Sol decoder              |
+--------------------------------------+--------------------------------------+
| ffdec\_xan\_dpcm                     | FFmpeg DPCM Xan decoder              |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_4xm                    | FFmpeg ADPCM 4X Movie decoder        |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_adx                    | FFmpeg SEGA CRI ADX ADPCM decoder    |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ct                     | FFmpeg ADPCM Creative Technology     |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ea                     | FFmpeg ADPCM Electronic Arts decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ea\_maxis\_xa          | FFmpeg ADPCM Electronic Arts Maxis   |
|                                      | CDROM XA decoder                     |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ea\_r1                 | FFmpeg ADPCM Electronic Arts R1      |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ea\_r2                 | FFmpeg ADPCM Electronic Arts R2      |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ea\_r3                 | FFmpeg ADPCM Electronic Arts R3      |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ea\_xas                | FFmpeg ADPCM Electronic Arts XAS     |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_g722                          | FFmpeg G.722 ADPCM decoder           |
+--------------------------------------+--------------------------------------+
| ffdec\_g726                          | FFmpeg G.726 ADPCM decoder           |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ima\_amv               | FFmpeg ADPCM IMA AMV decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ima\_dk3               | FFmpeg ADPCM IMA Duck DK3 decoder    |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ima\_dk4               | FFmpeg ADPCM IMA Duck DK4 decoder    |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ima\_ea\_eacs          | FFmpeg ADPCM IMA Electronic Arts     |
|                                      | EACS decoder                         |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ima\_ea\_sead          | FFmpeg ADPCM IMA Electronic Arts     |
|                                      | SEAD decoder                         |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ima\_iss               | FFmpeg ADPCM IMA Funcom ISS decoder  |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ima\_qt                | FFmpeg ADPCM IMA QuickTime decoder   |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ima\_smjpeg            | FFmpeg ADPCM IMA Loki SDL MJPEG      |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ima\_wav               | FFmpeg ADPCM IMA WAV decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ima\_ws                | FFmpeg ADPCM IMA Westwood decoder    |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_ms                     | FFmpeg ADPCM Microsoft decoder       |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_sbpro\_2               | FFmpeg ADPCM Sound Blaster Pro 2-bit |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_sbpro\_3               | FFmpeg ADPCM Sound Blaster Pro       |
|                                      | 2.6-bit decoder                      |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_sbpro\_4               | FFmpeg ADPCM Sound Blaster Pro 4-bit |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_swf                    | FFmpeg ADPCM Shockwave Flash decoder |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_thp                    | FFmpeg ADPCM Nintendo Gamecube THP   |
|                                      | decoder                              |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_xa                     | FFmpeg ADPCM CDROM XA decoder        |
+--------------------------------------+--------------------------------------+
| ffdec\_adpcm\_yamaha                 | FFmpeg ADPCM Yamaha decoder          |
+--------------------------------------+--------------------------------------+
| ffdec\_ass                           | FFmpeg Advanced SubStation Alpha     |
|                                      | subtitle decoder                     |
+--------------------------------------+--------------------------------------+
| ffdec\_dvbsub                        | FFmpeg DVB subtitles decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_dvdsub                        | FFmpeg DVD subtitles decoder         |
+--------------------------------------+--------------------------------------+
| ffdec\_pgssub                        | FFmpeg HDMV Presentation Graphic     |
|                                      | Stream subtitles decoder             |
+--------------------------------------+--------------------------------------+
| ffdec\_xsub                          | FFmpeg XSUB decoder                  |
+--------------------------------------+--------------------------------------+

.. rubric:: Third Party Solutions
   :name: third-party-solutions

Third parties like Ittiam and VisualON provide highly optimized ARM only
codecs on Linux, WinCE and Android OS.

.. rubric:: Software Components & Dependencies
   :name: software-components-dependencies

| The following lists some of the software components and dependencies
  associated with the Sitara SDK.

Dependancies: Required packages to build Gstreamer on Ubuntu:

sudo apt-get install automake autoconf libtool docbook-xml docbook-xsl
fop libxml2 gnome-doc-utils

-  build-essential
-  libtool
-  automake
-  autoconf
-  git-core
-  svn
-  liboil0.3-dev
-  libxml2-dev
-  libglib2.0-dev
-  gettext
-  corkscrew
-  socket
-  libfaad-dev
-  libfaac-dev

Software components for Sitara SDK Release:

-  glib
-  gstreamer
-  liboil
-  gst-plugins-good
-  gst-ffmpeg
-  gst-plugins-bad
-  gst-plugins-base

.. rubric:: Re-enabling Mp3 and Mpeg2 decode in the Processor SDK
   :name: re-enabling-mp3-and-mpeg2-decode-in-the-processor-sdk

Starting with version 05.05.01.00, mp3 and mpeg2 codecs are no longer
distributed as part of the SDK. These plugins can be re-enabled by the
end user through rebuilding the gst-plugins-ugly package. The following
instructions have been tested with gst-plugins-ugly-0.10.19 which can be
found at
`**gstreamer.freedesktop.org** <http://gstreamer.freedesktop.org/>`__.
Note that these instructions will work for any of the gstreamer plugin
packages found in the sdk.

-  Source environment-setup at the terminal
-  Navigate into the example-applications path under the SDK install
   directory
-  Extract the GStreamer plug-in source archive
-  Navigate into the folder that was created
-  On the command line type
   ``./configure --host=arm-arago-linux-gnueabi --prefix=/usr``
-  Notice that some components are not built because they have
   dependencies that are not part of our SDK
-  Run ``make`` to build the plugins.
-  Run ``make install DESTDIR=<PATH TO TARGET ROOT>``

