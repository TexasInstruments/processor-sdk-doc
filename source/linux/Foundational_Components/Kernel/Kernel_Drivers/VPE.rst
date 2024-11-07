.. http://processors.wiki.ti.com/index.php/Linux_Core_VPE_User%27s_Guide

VPE
---------------------------------

.. rubric:: Introduction
   :name: introduction-linux-core-vpe

- This page gives a basic description of VPE mem to mem video IP found
  in `devices <VPE.html#vpe-supported-devices>`__,
  the linux kernel drivers which implement it, how to build the drivers as
  modules or built-in, and how one can test and use the drivers.

- The driver described here is the VPE v4l2 mem-2-mem driver.

- The guide applies to both 3.12 and the current mainline kernel.
  Currently, DRA7x requires additional patches for hwmod and DT support
  for mainline.

- For a generic linux kernel guide, try:

::

    http://processors.wiki.ti.com/index.php/Linux_Kernel_Users_Guide

.. rubric:: VPE Supported Devices
   :name: vpe-supported-devices

DRA7x evm, AM57xx evm

.. rubric:: Driver Features
   :name: driver-features

Video processing Engine(VPE) supports following formats for scaling, csc
and deinterlacing:

-  Supported Input formats: NV12, YUYV, UYVY
-  Supported Output formats: NV12, YUYV, UYVY, RGB24, BGR24, ARGB24,
   ABGR24
-  Scaler supports
-  Horizontal up-scaling up to 8x and Downscaling up to 4x using
   Pre-decimation filter.
-  Vertical up-scaling up to 8x and Polyphase down-scaling up to 4x
   followed by RAV scaling.
-  V4L2 Multiplanar ioctl() supported.
-  Multiple V4L2 device context supported.
-  v4l2 m2m related ioctls.

.. rubric:: Changes from 3.12 to 3.15
   :name: changes-from-3.12-to-3.15

-  Changes in 3.13:

- Basic VPE driver introduced with DEI support.

-  Changes in 3.14:

- Support added for scaler and color space converter.

-  Changes in 3.15:

- Misc fixes found during testing.

.. rubric:: Unsupported Features/Limitations
   :name: unsupported-featureslimitations

-  Following formats are not supported : YUV444, YVYU, VYUY, NV16, NV61,
   NV21, 16bit and Lower RGB formats are not supported.
-  Passing of custom scaler and CSC coeffficients through user space are
   not supported.
-  Only Linear scaling is supported without peaking and trimming.
-  Deinterlacer does not support film mode detection.
-  VPE functional clock is restricted to 152Mhz due to HW constraints.

.. rubric:: Hardware Architecture
   :name: hardware-architecture

VPE(Video Processing Engine) is an IP found on DRA7xx, and in some past
TI multimedia SoCs which don't have baseport support in the mainline
kernel.

VPE is a memory to memory block used for performing de-interlacing,
scaling and color conversion on input buffers. It's primarily used to
de-interlace decoded DVD/Blu Ray video buffers, and provide the content
to progressive display or do some other post processing. VPE can also be
used for other tasks like fast color space conversion, scaling and
chrominance up/down sampling. The scaler in particular is based on a
polyphase filter and supports 32 phases and 5/7 taps.

VPE's De-interlacer IP: The De-interlacer module performs a combination
of spatial and temporal interlacing, it determines the weight-age by
keeping a track of the change in motion between fields by maintaining
and updating a motion vector buffer in the RAM. The de-interlacer needs
the current field and the 2 previous fields (along with the motion
vector info)to generate a progressive frame. It operates on YUV422 data.

VPDMA: All the DMAs are done through a dedicated DMA IP called
VPDMA(Video Port Direct Memory Access). This DMA IP is specialized for
transferring video buffers, the input and output data ports of VPDMA are
configured via descriptor lists loaded to the VPDMA list manager. VPDMA
is also used to load MMRs of the various VPE sub blocks.

VPDMA is advanced enough to support multiple clients like a system DMA,
however, the way it's integrated in the SoC is such that it can be used
only by the VPE IP. The same IP is also used on DRA7x in another block
called VIP (full form) used to capture camera sensor content. It's again
dedicated to the VIP block, and therefore doesn't have multiple clients.
These factors made us consider writing the VPDMA block as a library,
providing functions to VPE(and VIP in the future) to add descriptors and
start DMA. It might have made sense to make it a dmaengine driver if
there were multiple clients using VPDMA.

f, f - 1, and f - 2 are input ports fetching 3 consecutive fields for
the de-interlacer. MVin and MVout are ports which fetch the current
motion vector and output the updated motion vector respectively. There
are 2 output ports, one for YUV output and the other for RGB output if
the color space converter(CSC) is used. The inputs can be YUV packed or
semiplanar formats. The chrominance upsampler(CHR\_USx) is used when the
input format is NV12, the chrominance downsampler(CHR\_DS) is used if
the the output content needs to be NV12 format. The scaler(SC) can be
used to scale the de-interlaced content if needed.

For a diagram, look here:

::

    http://www.spinics.net/lists/linux-media/msg66518.html

.. rubric:: Driver Architecture
   :name: driver-architecture

The VPE driver follows the standard v4l2 mem 2 mem model. An
introduction can be found here:

http://lwn.net/Articles/389081/

Each mem 2 mem context holds a hardware state of VPE, and the software
state of the VPE device. One context can be paused, and another context
can be initiated with it's own VPE state. In this way, the driver
supports multiple open() calls, allowing multiple applications to share
VPE cycles.

.. rubric:: Driver Configuration
   :name: driver-configuration-vpe

.. rubric:: Source Location
   :name: source-location-vpe

-  kernel driver:

::

    drivers/media/platform/ti-vpe/

.. rubric:: Kernel Configuration Options
   :name: kconfig-options-vpe

.. rubric:: Kernel config(built-in)
   :name: kernel-configbuilt-in

-  Start with the default config:

::

    $ make ARCH=arm omap2plus_defconfig

-  Select the following things after a menuconfig:

::

    $ make ARCH=arm menuconfig

-  Go to the Device drivers option:

::

    ...
    ...
    Kernel Features  --->
    Boot options  --->
    CPU Power Management  --->
    Floating point emulation  --->
    Userspace binary formats  --->
    Power management options  --->
    [*] Networking support  --->
    Device Drivers  --->
    ...
    ...

-  Select Multimedia support as a module, and go inside:

::

    ...
    ...
    [ ] ARM Versatile Express platform infrastructure
    -*- Voltage and Current Regulator Support  --->
    <M> Multimedia support  --->
    Graphics support  --->
    <M> Sound card support  --->
    ...
    ...

-  Select Cameras/video grabbers support, Memory-to-memory multimedia
   devices(as a module), and enter the latter:

::

    --- Multimedia support
        *** Multimedia core support ***
    [*]   Cameras/video grabbers support
    [ ]   Analog TV support
    [ ]   Digital TV support
    ...
    ...
    [M]   Memory-to-memory multimedia devices  --->
    ...
    ...

-  Select the VPE mem2mem driver:

::

    --- Memory-to-memory multimedia devices
    < >   Deinterlace support (NEW)
    < >   SuperH VEU mem2mem video processing driver (NEW)
    <M>  TI VPE (Video Processing Engine) driver
    [ ]     VPE debug messages (NEW)

-  Build the kernel image and the modules, ahoy:

::

    make uImage
    make modules

-  User space will require an ioctl base in v4l2-controls.h, so make
   sure you update the headers:

::

    make headers-install

.. rubric:: Kernel config(modules)
   :name: kernel-configmodules

Similar to built-in, just replace with <M>.

.. rubric:: Driver Usage
   :name: driver-usage-vpe

.. rubric:: Loading Modules
   :name: loading-modules

The kernel config above builds vpe as a kernel module(ti-vpe.ko). There
are some dependencies which need to be taken care of. The v4l and
videobuf modules are:

::

    insmod videodev.ko
    insmod videobuf2-core.ko
    insmod videobuf2-memops.ko
    insmod videobuf2-dma-contig.ko
    insmod v4l2-common.ko
    insmod v4l2-mem2mem.ko

And finally:

::

    insmod ti-vpe.ko

.. rubric:: Loading firmware
   :name: loading-firmware

The VPDMA block within VPE requires firmware to be loaded from
userspace. The firmware along with the testcase is put here:

git://git.ti.com/vpe_tests/vpe_tests.git

Build the test case

::

    make install

This builds the test case, and copies it into $(DESTDIR)/usr/bin, and
the firmware into $(DESTDIR)/lib/firmware.

The firmware file name is 'vpdma-1b8.bin'. There are 2 ways to load the
firmware:

-  Place the firmware in the 'lib/firmware/' folder of your filesystem.

-  The manual method:

::

    $ echo 6000 > /sys/class/firmware/timeout
    $ echo 1 > /sys/class/firmware/vpdma-1b8.bin/loading
    $ cat vpdma-1b8.bin > /sys/class/firmware/vpdma-1b8.bin/data
    $ echo 0 > /sys/class/firmware/vpdma-1b8.bin/loading

.. rubric:: Testing the driver
   :name: testing-the-driver

Use the git repository above to try out this low level test case.

The usage is something like this:

::

    $ ./testvpem2m <src-file> <src-width> <src-height> <src-format>
      <dst-file> <dst-width> <dst-height> <dst-format> [<crop-top> <crop-left>
      <crop-width> <crop-height>] <de-interlace> <job-len>

Some points about the arguments:

-  We just support de-interlacing of the source frames for now.
-  If <de-interlace> is set to 1, the testcase tries to perform
   de-interlacing, irrespective of what the content is.
-  If <de-interlace> is set to 0, the DEI block is bypassed. You can
   still use it for scaler and color conversion.
-  Only interlaced content in the form of top-bottom fields are
   supported.
-  When testing higher resolutions, make sure we increase the CMA memory
   through the 'cma' bootarg.
-  <job-len> tells how many times you want your test app to use the VPE
   hardware. In real use cases, this should be decided based upon
   various factors like QoS, video resolution, and so on.
-  We can run multiple instances of this test, and each one will get a
   slice of VPE based on the <job-len> provided for each instance.

An example of de-interlacing a 480i nv12 clip to a 480p yuyv clip:

::

    $ ./testvpem2m 480i_clip.nv12 720 240 nv12 dei_480p_clip.yuv 720 480 yuyv 1 3

An example of just scaling/colorspace-converting a progressive 640x480
nv12 clip to a smaller resolution rgb clip:

::

    $ ./testvpem2m 640_480p.nv12 640 480 nv12 360_240p.rgb24 360 240 rgb24 0 3

The <dst-file> should contain the VPE output content.

This is a standalone VPE test case. In real usage, VPE won't allocate
buffers by itself. It will use dma-bufs shared by a dmabuf exporter(most
likely omapdrm) instead of allocating by itself via the videobuf2 layer.

.. rubric:: Debugging
   :name: debugging-vpe

Debug log can be enabled in the VPE driver by adding “#define DEBUG” at
the first line of drivers/media/platform/ti-vpe/vpe.c.

