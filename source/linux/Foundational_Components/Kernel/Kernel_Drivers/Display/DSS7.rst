.. _dss7:

DSS
#################

Introduction
============

This page gives a basic description of DSS (Display SubSystem) hardware, the Linux kernel drivers (tidss) and various TI boards that use DSS. The technical reference manual (TRM) for the SoC in question, and the board documentation give more detailed descriptions.


Supported Devices
=================

There are many DSS IP versions, all of which support slightly different set of features. DSS versions up to 5 are supported by the omapdrm driver, and DSS versions 6 and up are supported by the tidss driver. This document covers DSS6, DSS7-L, DSS7-UL and DSS7-Nano which are used on the following TI SoCs or SoC families: K2G, AM65x, AM62x, AM62Ax, AM62Px, AM62L, J721E, J721S2, J784S4.


Hardware Architecture
=====================

The Display Subsystem (DSS) is a hardware block responsible for fetching pixel data from memory and sending it to a display peripheral like an LCD panel or an DisplayPort monitor. DSS hardware can be divided into two major parts:

- Display Controller (DISPC), which handles fetching the pixel data, doing color conversions, composition, and other pixel manipulation
- Peripherals, which encode the raw pixel data to standard display signals, like MIPI DPI or DP.

In addition to the SoC's DSS, boards often contain external display bridges (for example, DPI-to-HDMI bridge) and display panels.

.. ifconfig:: CONFIG_part_variant in ('J721E', 'J721S2', 'J784S4','J742S2')

    .. Image:: /images/DSS7_HW.png

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM65X', 'AM62AX', 'AM62PX', 'J722S')

    .. Image:: /images/DSS7Lite_HW.png


The above image gives an overview of the DSS hardware.

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J722S')

    - The |__PART_FAMILY_NAME__| SoC has 2 instances of the DSS7-UL, connected to different display peripherals, inside the SoC.
    - **Note:** The Video Pipelines from one instance of DSS **cannot** overlay image planes via the Overlay Managers of another DSS.

The arrows show how pipelines are connected to overlay managers, which are further connected to video-ports, which finally create an encoded pixel stream for display on the LCD or monitor.

.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    - **Note:** While the DSS7-UL in AM62Ax has 2 video pipelines, there is only one video port (VP) coming out of the SoC. This VP outputs DPI signals. The other pipeline can be used to overlay video data on top of the first pipeline's output. On the AM62A-SK EVM, this DPI output is then forwarded to an on-board HDMI framer.

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

    - **Note:** The DSS7 Nano in AM62LX has a single video pipeline and a single video port (VP) coming out of the SoC. The output of video port is routed to SoC boundary via DPI interface and the DPI signals from the video port are routed to DSI Tx controller present within the SoC. Same DPI signals are also forwarded to an on-board HDMI framer. At a time though, only a single interface i.e. DPI or DSI can be used with the EVM.

Display Controller (DISPC)
--------------------------

DISPC is the block which is responsible for fetching pixel data from the memory through DMA pipelines, and then create a pixel stream for the peripheral. The pixel stream comprises of a composition of one or more image layers which we finally want to present on the display. DISPC can be split into 3 major sub-blocks:

    - Pipelines
    - Overlay Managers (Compositors)
    - Video Ports (Timing generators)

The next three sub-sections provide details on these sub-blocks.


Pipelines
^^^^^^^^^

Pipelines (or DMA channels) consist of the HW block which performs DMA to fetch image pixels (of different color formats) from RAM. Besides performing DMA, pipelines perform other functions like replication, ARGB expansion, scaling, color conversion, VC1 range mapping on the input pixels before it's passed on to the overlay manager. An overlay manager receives pixel data from one or more such pipelines, and performs the task of composing them and passing it on to the video-port.

There are two types of pipelines: VIDL and VID. The difference between the two is that VID pipelines support scaling, and VIDL does not. The number of pipelines within DSS varies with the DSS IP version used in the SoC.


Overlay Managers (Compositors)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Overlay managers are the blocks which take pixel data from one or more pipelines, layer them to form a composition, and create a pixel stream for the video-ports to consume.

The compositor part takes pixel data from multiple pipelines, composing them on the basis of their position with respect to the complete overlay manager size. Tasks like alpha blending, color-keying and z-order are also performed by the compositor in the overlay manager.


Video Ports (Timing generators)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Video ports take a pixel stream from an overlay manager, and encode it into a standard video signal which is understood by the LCD panel/monitor or an internal peripheral (like eDP). These video standards are specified by MIPI or general video/display bodies.

The timing generator part of the video port is responsible for providing the pixel stream generated by the compositor above according to the timings desired by the peripheral. The timing generator is a state machine which provides RGB data along with control signals like pixel clock, hsync, vsync and data enable. This timing info is used by the panel / peripheral to display the composited frame on the screen.


SoC Hardware Description
------------------------

SoC Family: |__PART_FAMILY_DEVICE_NAMES__|

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM65X')

    +-------------+---------------+-------------------+-------------+
    | DSS version | Outputs       | Pipes             | Video ports |
    +=============+===============+===================+=============+
    | DSS7-UL     | DPI, OLDI     | VID, VIDL         | 2           |
    +-------------+---------------+-------------------+-------------+

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

    +-------------+---------------+-------------------+-------------+
    | DSS version | Outputs       | Pipes             | Video ports |
    +=============+===============+===================+=============+
    | DSS7-Nano   | DPI, DSI      | VIDL              | 1           |
    +-------------+---------------+-------------------+-------------+


.. ifconfig:: CONFIG_part_variant in ('AM62AX')

    +-------------+---------------+-------------------+-------------+
    | DSS version | Outputs       | Pipes             | Video ports |
    +=============+===============+===================+=============+
    | DSS7-UL     | DPI           | VID, VIDL         | 1           |
    +-------------+---------------+-------------------+-------------+


.. ifconfig:: CONFIG_part_variant in ('J721E', 'J721S2', 'J784S4','J742S2')

    +-------------+---------------+-------------------+-------------+
    | DSS version | Outputs       | Pipes             | Video ports |
    +=============+===============+===================+=============+
    | DSS7-L      | DPI, DP, DSI  | 2 x VIDL, 2 x VID | 4           |
    +-------------+---------------+-------------------+-------------+

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J722S')

    +-------------+----------------+------------------+-------------+
    | DSS version | Outputs        | Pipes            | Video ports |
    +=============+================+==================+=============+
    | 2x DSS7-UL  | OLDI, DPI, DSI | 2x VID, 2x VIDL  | 4           |
    +-------------+----------------+------------------+-------------+

    Note that while there are 4 video pipes and ports available, only 3 display streams can be
    output at any given time, as there are only 3 PLLs that generate independent pixel clocks.

    The DSS7 hardware also supports resource sharing across multiple processing cores with separate register region per sub-component and interrupt duplication for each processing core, thus allowing independent context update for the associated pipelines.

    .. Image:: /images/DSS7_resource_paritioning_HW.png


Supported Features
------------------

**SoC Outputs**
^^^^^^^^^^^^^^^

- **MIPI DPI**
    - Active matrix
    - RGB

    **Note:**
    TI EVMs do not provide the DPI signals through a connector, but instead pass the RGB
    data through an DP/HDMI transmitters on-board. Custom EVMs based on these SoCs can
    provide such connectors and can use the Active Matrix LCDs.

.. ifconfig:: CONFIG_part_variant in ('J721E', 'J721S2', 'J784S4','J742S2')

    - **DisplayPort**
        - SST
.. ifconfig:: CONFIG_part_variant in ('J721E', 'J721S2', 'J784S4','J742S2', 'AM62PX', 'J722S')

    - **MIPI DSI**
        - 4 Lane MIPI DSI output

.. ifconfig:: CONFIG_part_variant in ('AM65X')

    - **Open LVDS Display Interface (OLDI)**
        -  Single Link OLDI
.. ifconfig:: CONFIG_part_variant in ('AM62X')

    - **Open LVDS Display Interface (OLDI)**
        -  Single Link OLDI
        -  Dual Link OLDI
.. ifconfig:: CONFIG_part_variant in ('AM62LX')

    - **MIPI DSI**
        -  4 Lane MIPI DSI output
.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J722S')

    - **Open LVDS Display Interface (OLDI)**
        -  Single Link OLDI
        -  Dual Link OLDI
        -  2x Single Link Independent OLDI

**EVM Outputs**
^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62AX', 'AM62PX', 'J721E', 'J721S2', 'J784S4','J742S2', 'J722S')

    - **HDMI Output**
        - DPI output from SoC converted to HDMI via HDMI encoders on Starter-Kit (SK) EVMs.

.. ifconfig:: CONFIG_part_variant in ('J721E', 'J721S2', 'J784S4','J742S2')

        **Note:**
        Jacinto CPBs and EVMs do not support DPI to HDMI encoders. It is only available on Jacinto SoCs' SK-EVM variants.

    - **DisplayPort Output**
        - DisplayPort output from SoC directly.
        - DSI output from SoC converted to DP via DSI-to-DP encoder on board.
.. ifconfig:: CONFIG_part_variant in ('AM65X')

    - **DP Output**
        - DPI output from SoC converted to DP (DisplayPort) via DP encoders present on an adapter card.

    - **Open LVDS Display Interface (OLDI)**
        -  Single Link OLDI output from the SoC directly.
.. ifconfig:: CONFIG_part_variant in ('AM62X')

    - **Open LVDS Display Interface (OLDI)**
        -  Single Link OLDI output from the SoC directly.
        -  Dual Link OLDI output from the SoC directly.
.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J722S')

    - **Open LVDS Display Interface (OLDI)**
        -  Single Link OLDI output from the SoC directly.
        -  Dual Link OLDI output from the SoC directly.
        -  2x Single Link Independent OLDI output from the SoC directly.

    - **MIPI DSI**
        - 4 Lane MIPI DSI output from the SoC directly.
        - The connector is compatible with 22 pin RPi DSI Connector.

Driver Architecture
===================

The driver for DSS6 / DSS7-L / DSS7-UL / DSS7-Nano IPs is tidss. tidss is a Direct Rendering Manager (DRM) driver, located in the directory drivers/gpu/drm/tidss/ in the kernel tree. tidss does not implement any 3D GPU features, only the Kernel Mode Setting (KMS) features, used to display pixel data on a display.

In addition to tidss, there are a number of bridge and panel drivers located in drivers/gpu/drm/bridge/ and drivers/gpu/drm/panel/ which provide support for various panels and bridges (both external and internal to SoC).

The mapping of DRM entities to DSS hardware is roughly as follows:

+-----------+--------------------------------+
| DRM term  | HW term                        |
+===========+================================+
| plane     | DSS pipeline                   |
+-----------+--------------------------------+
| crtc      | DSS videoport                  |
+-----------+--------------------------------+
| encoder   | Internal and external bridges  |
+-----------+--------------------------------+
| connector | Connector or a panel           |
+-----------+--------------------------------+


Driver Features
---------------

Note: this is not a comprehensive list of features supported/not supported, and new features may be added in every release.

**DRM Plane Features**
    - CSC
    - Scaler
    - Z-order
    - Global alpha blending
    - Alpha blending (pre-multipled & non-pre-multiplied)
    - Input Video Formats
      (Fourcc codes of supported formats: AR12 AB12 RA12 RG16 BG16 AR15 AB15 AR24 AB24 RA24 BA24 RG24 BG24 AR30 AB30 XR12 XB12 RX12 AR15 AB15 XR24 XB24 RX24 BX24 XR30 XB30 YUYV UYVY NV12)

**DRM CRTC Features**
    - Gamma table

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J722S')

 **Display Sharing mode**

 The display sharing solution at Linux side is designed in such a way that the underlying kernel framework takes care of the display sharing functionality without requiring any updates
 in user-space API. This ensures that existing display server based windowing systems and display applications can leverage display in shared mode directly without any additional update or handling. The DSS resources can be partitioned across multiple processing cores by setting the ti,dss-sharing-mode and associated properties in the device-tree. A static resource partitioning scheme is designed where each of the DSS resources are given attributes related to sharing and ownership as desribed below :

 1. *Display controller register region (Common or Common1 register space)* :

  Each processing core is given separate register region for controlling the display, with only one of the processing cores having access to global configuration region, Also each processing core has access only to the corresponding register region owned by it with other register regions completely inaccessible to it. The processing core running Linux can be assigned one of the available display controller register spaces using the "ti,dss-shared-mode-common" device-tree property.

 2. *Video Pipeline* :

  This resource also can be exclusively owned by only one processing core, thus remaining completely inaccesible to other processing cores which are not owning it, so there is no sharing possible for this resource actually. The processing core running Linux can be assigned one or more of the available video pipelines using "ti,dss-shared-mode-plane" device-tree property. The relative z-order of planes owned by processing core running Linux can be set using ti,dss-shared-mode-plane-zorder.

 3. *Video Port* :

  A video port can drive multiple video pipelines which are being independently controlled by different processing cores, so it can act as shared resource too where although only one of the processing cores has an exclusive write access to it but any other processing cores which are owning the Video piplines driven by this video port can be given read-only access to this Video Port's register space.

 To summarize, this resource can have exclusive ownership attribute with write access to only one processing core but shared attribute for other processing cores which are provided read-only access, but this is for only those processing cores which are using this video port for driving their video pipelines. The read-only access also helps such processing cores to determine the video port configuration like screen width, screen height e.t.c directly from video port registers without any communication requirement with the processing core owning this video port. The corresponding overlay managers associated with this video port are automatically given same ownership and sharing attributes.

 The processing core running Linux can be assigned one or more of the available video ports either with read only access (i.e with only shared attribute) or write access (i.e. with exclusive ownership attribute), but for both the cases the driver enumerates corresponding connectors and video encoders attached to this video port thus making the full display pipeline visible to end user.

 The device-tree property "ti,dss-shared-mode-vp" can be used by processing core running Linux to enlist one or more video ports being used by it and the ownership related information can be set using ti,dss-shared-mode-owned-vp device-tree property.

 To summarize, below is the list of device-tree properties which can be added to display node, using these properties one can set up a resource paritioning scheme tailored as per the desired end use-case::

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J722S')

   .. code-block:: console

     ti,dss-shared-mode :  Enable display sharing mode
     ti,dss-shared-mode-planes : Enumerate Display planes owned by Linux
     ti,dss-shared-mode-vp :  Enumerate Video Ports being used to control above planes
     ti,dss-shared-mode-owned-vp : Specify which of the above Video Ports are actually owned by Linux , i.e. those video ports for which Linux has write access
     ti,dss-shared-mode-common : Specify which of the common region i.e register space should be used by Linux for programming the DSS.
     ti,dss-shared-mode-plane-zorder : Specify the relative plane ordering for the planes owned by Linux

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J722S')

   .. note::

      For display sharing mode to work with chosen resource paritioning between Linux and remote core, the remote core needs to be running appropriate firmware which programs the display hardware by supporting this resource paritioning scheme.

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J722S')

 More detailed description of these properties can be found at:
 `Display device-tree file <https://git.ti.com/cgit/ti-linux-kernel/ti-linux-kernel/tree/Documentation/devicetree/bindings/display/ti/ti,am65x-dss.yaml?h=09.01.00.008>`__
 Also there is a how-to guide available for dss sharing which walks through different examples for resource paritioning using these device-tree properties :
 `How to enable dss sharing between remote core and Linux <../../../../How_to_Guides/Target/How_to_enable_display_sharing_between_remotecore_and_Linux.html>`__

Unsupported Features/Limitations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **DPI output**
    - TDM
    - BT-656/1120
    - MIPI DBI/RFBI
    - Interlace

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM65X', 'AM62AX', 'AM62PX', 'J722S', 'AM62LX')

        - **DisplayPort (MHDP)**
            - The SoC doesn't support the MHDP IP, and doesn't provide the DP output.
.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM65X', 'AM62AX')

        - **MIPI DSI**
            - The SoC doesn't support the DSI / DPHY-Tx, and doesn't provide the MIPI DSI output.
.. ifconfig:: CONFIG_part_variant in ('AM62AX', 'J721E', 'J784S4','J742S2', 'J721S2', 'AM62LX')

        - **Open LVDS Display Interface (OLDI)**
            - The SoC doesn't support the OLDI TXes, and doesn't provide the OLDI output.
.. ifconfig:: CONFIG_part_variant in ('J721E', 'J784S4','J742S2')

        - **DisplayPort (MHDP)**
                - MST
                - 4K@60FPS Resolution
                | For 4k@60FPS resolution, sometimes visual artifacts are seen due to Video Sync Loss.
                | Therefore the maximum supported video resolution as of now is limited to 4K@30FPS (or equivalent)
                | by limiting the dp phy-link rate to 2700Mbps.
.. ifconfig:: CONFIG_part_variant in ('J721S2')

        - **DisplayPort (MHDP)**
                - MST
                - 4K@60FPS Resolution
                | MHDP PHY has only 2 SERDES LANES dedicated to eDP and with the phy-link rate of 5400Mbps, the maximum
                | data rate it can support is 10.8Gbps which is not sufficient for 4k@60FPS. So the maximum supported
                | resolution is 4K@30FPS (and equivalent resolutions).

Driver Configuration
====================

Kernel Configuration Options
----------------------------

tidss supports building both as built-in or as a module.

tidss can be found under "Device Drivers/Graphics support" in the kernel menuconfig. You need to enable DRM (CONFIG_DRM) before you can enable tidss (CONFIG_DRM_TIDSS).

-  Enable DSS Display Subsystem support (CONFIG_DRM_TIDSS)

Additional kernel config options may be needed, depending on the SoC and board.

- Panels under "Device Drivers/Graphics support/Display Panels"
- Bridges under "Device Drivers/Graphics support/Display Interface Bridges"
- PHYs under "Device Drivers/PHY Subsystem"

Device Tree Node
----------------

Documentation for tidss device tree node and its properties can be found in linux kernel device tree bindings in below directory
``Documentation/devicetree/bindings/display/ti/``. Seperate binding files are present for different version of the DSS controller.

For information about configuring Spread Spectrum Clocking (SSC) for DSS, see :ref:`how-to-enable-ssc-for-dss`.


Driver Usage
============

Loading tidss
-------------

If built as a module, you need to load all the drm, tidss, bridge and panel modules before tidss will start. When tidss starts, it will prints something along these lines: ::

    [    9.207746] [drm] Initialized tidss 1.0.0 20180215 for 4a00000.dss on minor 0


Using tidss
-----------

tidss is usually used by the windowing system like X server or Weston, so normally users don't need to use tidss directly.

tidss device appears under /dev/dri/ directory, normally card0.

There is also so called DRM render device node, renderD128, which point to the same tidss device. Only buffer allocations can be done via the render node. The render node can be given more relaxed access restrictions, as the applications can only do buffer allocations from there, and cannot affect the system (except by allocating all the memory).

Low level userspace applications can use tidss via DRM ioctls. This is made a bit easier with libdrm, which is a wrapper library around DRM ioctls, or kms++ which is a C++11 library, or by Python bindings provided by kms++.

libdrm is included in TI releases and its sources can be found from: ::

    https://gitlab.freedesktop.org/mesa/drm

libdrm also contains 'modetest' tool, which can be used to get basic information about DRM state, and to show a test pattern on a display. Refer to the section :ref:`testing_tidss_properties` below for some examples.

Another option is kms++, a C++11 library for kernel mode setting which includes a bunch of test utilities and also V4L2 classes and Python bindings for DRM and V4L2. Some kms++ tools are included in TI releases. kms++ can be found from: ::

    https://github.com/tomba/kmsxx


.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J722S')

    For the |__PART_FAMILY_NAME__|  SoC, there are 2 instances of the DSS7-UL controller, and so will be the number
    of driver instances available. The AM62P5-SK EVM supports Hot Plug Detect for the HDMI output,
    which is currently served from the first DSS instance (DSS0). For the OLDI and DSI outputs, the
    devicetree (DT) overlays can be used to enable them. The OLDI output, configured as Dual-Link in
    the DT overlay, is sourced from DSS0, while the DSI output gets sourced from the DSS1. Either
    DSS instance can be enabled from the DT sources, simultaneously or otherwise. To enable these
    displays on AM62P5-SK, refer the `How to enable DT overlays in linux
    <../../../../How_to_Guides/Target/How_to_enable_DT_overlays_in_linux.html>`__ guide, and enable the
    ``k3-am62p5-sk-microtips-mf101hie-panel.dtbo`` DT overlay for OLDI output, and
    ``k3-am62p5-sk-dsi-rpi-7inch-panel.dtbo`` DT overlay for the DSI output.

    In the event, where a multi display is enabled on the AM62P5-SK/J722S EVM, with each DSS instance
    supporting at-least one display output, there will be two instances of tidss driver, and by
    extension, the drm framework driver, running on the platform. The GUI applications can capture
    them through the DRI card instances. Usually, the DSS0 will be /dev/dri/card0. The DSS1 however,
    can either be /dev/dri/card1 or /dev/dri/card2, depending on whether or not the GPU is enabled
    on the platform. The GPU, if present, associates with the card1, which leaves card2 for DSS1.
    In a case where GPU driver is not present, DSS1 will take up card1.

    - **Note:** Most display applications and windowing managers are programmed in such a way that
    they can only access a display DRM card (card0) and a GPU DRM card (card1). This is why, the
    second DSS instance, will not show up running Weston or any framebuffer application, even when
    GPU is not present, in which case the windowing manager will only use card0. This makes DSS1
    completely available for a 2nd DRM Master. This can be a custom display application, helping out
    in the most niche of use-cases.


Testing tidss
-------------

kmsxxtest from kms++ is a good tool for testing tidss features. Note that any other applications using DRM (Weston, X) must be killed first. Another tool from kms++ is kmsprint, which can be used to print various bits of information about tidss.

.. code-block:: console

  $ kmsprint
  Connector 0 (39) DP-1 (connected)
    Encoder 0 (38) NONE
      Crtc 0 (37) 1920x1080 148.500 1920/88/44/148 1080/4/5/36 60 (60.00)
        Plane 0 (31) fb-id: 62 (crtcs: 0 1) 0,0 1920x1080 -> 0,0 1920x1080 (AR12 AB12 RA12 RG16 BG16 AR15 AB15 AR24 AB24 RA24 BA24 RG24 BG24 AR30 AB30 XR12 XB12 RX12 AR15 AB15 XR24 XB24 RX24 BX24 XR30 XB30 YUYV UYVY NV12)
          FB 62 1920x1080
  Connector 1 (48) HDMI-A-1 (disconnected)
    Encoder 1 (47) NONE

.. code-block:: console

  $ kmsxxtest -c dp -r 640x480
  Connector 0/@39: DP-1
    Crtc 0/@37: 640x480 25.175 640/16/96/48/- 480/10/2/33/- 60 (59.94) 0xa 0x40
    Plane 0/@31: 0,0-640x480
      Fb 63 640x480-XR24
  press enter to exit

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J722S')

  When enabled, the second DSS instance can be tested as follows. Note that if the GPU entity is present, DSS1 will become card2, as GPU will assume the card1 instanciation.

  .. code-block:: console

    $ kmsprint --device=/dev/dri/card2
    Connector 0 (40) DSI-1 (connected)
      Encoder 0 (39) NONE
        Crtc 0 (38) 800x480 28.569 800/48/32/80 480/3/7/6 60 (60.00)
          Plane 0 (31) fb-id: 48 (crtcs: 0) 0,0 800x480 -> 0,0 800x480 (AR12 AB12 RA12 RG16 BG16 AR15 AB15 AR24 AB24 RA24 BA24 RG24 BG24 AR30 AB30 XR12 XB12 RX12 XR15 XB15 XR24 XB24 RX24 BX24 XR30 XB30 YUYV UYVY NV12)
            FB 48 800x480
    $ kmsxxtest --device=/dev/dri/card2
    Connector 0/@40: DSI-1
      Crtc 0/@38: 800x480 28.569 800/48/32/80/- 480/3/7/6/- 60 (60.00) 0xa 0x48
      Plane 0/@31: 0,0-800x480
        Fb 49 800x480-XR24
    press enter to exit

tidss properties
----------------

tidss supports configuration via DRM properties. These are standard DRM properties, and DRM documentation describes them. Also, kmsprint can be used to show the supported properties.

+--------------------+----------+------------------------------------------------------------------------------------------------------+
| Property           | Object   | Description                                                                                          |
+====================+==========+======================================================================================================+
| zpos               | plane    | Z position of a plane                                                                                |
+--------------------+----------+------------------------------------------------------------------------------------------------------+
| COLOR_ENCODING     | plane    | Selects between BT.601 and BT.709 YCbCr color encoding                                               |
+--------------------+----------+------------------------------------------------------------------------------------------------------+
| COLOR_RANGE        | plane    | Selects between full range and limited range YCbCr encoding                                          |
+--------------------+----------+------------------------------------------------------------------------------------------------------+
| alpha              | plane    | Full plane alpha-blending                                                                            |
+--------------------+----------+------------------------------------------------------------------------------------------------------+
| CTM                | crtc     | Color Transformation Matrix blob property. Implemented trough Color phase rotation matrix in DSS IP. |
+--------------------+----------+------------------------------------------------------------------------------------------------------+
| GAMMA_LUT          | crtc     | Blob property to set the gamma lookup table (LUT) mapping pixel data sent to the connector.          |
+--------------------+----------+------------------------------------------------------------------------------------------------------+
| GAMMA_LUT_SIZE     | crtc     | Number of elements in gammma lookup table.                                                           |
+--------------------+----------+------------------------------------------------------------------------------------------------------+

.. _testing_tidss_properties:

Testing tidss properties with modetest and kmsxxtest
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As the name suggests, ``modetest`` is DRM based mode setting test program available along with libdrm.
It is an easy-to-use tool to test different features provided by display HWs. The DRM driver for,
the display HWs, exposes these features as DRM properties, (see the table above), and the ``modetest``
utility uses these properties to configure the display HW.

``modetest`` outputs look different based on the number and types of displays connected, but the
format remains the same. Before looking at this particular ``modetest``  output, ``kmsprint``
output is provided as reference.

.. code-block:: console

        $ kmsprint
        Connector 0 (40) LVDS-1 (connected)
          Encoder 0 (39) LVDS
            Crtc 0 (38) 1920x1200@60.00 150.275 1920/32/52/24/? 1200/24/8/3/? 60 (60.00) 0x0 0x48
              Plane 0 (31) fb-id: 51 (crtcs: 0 1) 0,0 1920x1200 -> 0,0 1920x1200 (AR12 AB12 RA12 RG16 BG16 AR15 AB15 AR24 AB24 RA24 BA24 RG24 BG24 AR30 AB30 XR12 XB12 RX12 XR15 XB15 XR24 XB24 RX24 BX24 XR30 XB30 YUYV UYVY NV12)
                FB 51 1920x1200
        Connector 1 (50) HDMI-A-1 (disconnected)
          Encoder 1 (49) NONE


In the example below, AM625 SK-EVM has been used, but this could extrapolated to all the EVMs
running TI SoCs that support DSS7-L / DSS7-UL. An OLDI display is being run on the AM625 SK-EVM, while
the HDMI is disconnected.

Now, a shortened version of the command: ``modetest -M tidss`` that highlights some information used
in the examples later.

.. code-block:: console

        $ modetest -M tidss
        Encoders:
        id	crtc	type	possible crtcs	possible clones
        39	38	LVDS	0x00000001	0x00000001
        49	0	none	0x00000002	0x00000002

        Connectors:
        id	encoder	status		name		size (mm)	modes	encoders
        40	39	connected	LVDS-1         	217x136		1	39
          modes:
                index name refresh (Hz) hdisp hss hse htot vdisp vss vse vtot
          #0 1920x1200 60.00 1920 1952 2004 2028 1200 1224 1232 1235 150275 flags: ; type: preferred, driver
          props:
        [ ... ]

        50	0	disconnected	HDMI-A-1       	0x0		0	49
          props:
        [ ... ]

        CRTCs:
        id	fb	pos	size
        38	51	(0,0)	(1920x1200)
          #0 1920x1200 60.00 1920 1952 2004 2028 1200 1224 1232 1235 150275 flags: ; type: preferred, driver
          props:
        [ ... ]

        48	0	(0,0)	(0x0)
          #0  nan 0 0 0 0 0 0 0 0 0 flags: ; type:
          props:
        [ ... ]

        Planes:
        id	crtc	fb	CRTC x,y	x,y	gamma size	possible crtcs
        31	38	51	0,0		0,0	0       	0x00000003
          formats: AR12 AB12 RA12 RG16 BG16 AR15 AB15 AR24 AB24 RA24 BA24 RG24 BG24 AR30 AB30 XR12 XB12 RX12 XR15 XB15 XR24 XB24 RX24 BX24 XR30 XB30 YUYV UYVY NV12
          props:
        [ ... ]

        41	0	0	0,0		0,0	0       	0x00000003
          formats: AR12 AB12 RA12 RG16 BG16 AR15 AB15 AR24 AB24 RA24 BA24 RG24 BG24 AR30 AB30 XR12 XB12 RX12 XR15 XB15 XR24 XB24 RX24 BX24 XR30 XB30 YUYV UYVY NV12
          props:
        [ ... ]

From the information above, it can be inferred that the LVDS display ouput has these objects
associated with it.

        - Plane with ID = 31.
        - CRTC with ID = 38.
        - Encoder with ID = 39.
        - Connector with ID = 40.

Note that the plane 31 is the primary plane for CRTC 38 (LVDS Display). And for the HDMI display,
the associated objects are as follows.

        - Encoder with ID = 49.
        - Connector with ID = 50.

Since HDMI display is disconnected at the moment, no CRTC object has been enumerated for it, and
hence plane 41 remains unused.

.. ifconfig:: CONFIG_part_variant not in ('AM62LX')

 - **Z order**

   Z position of the plane when multiple planes are being displayed.

   This property is enumerated as ``zpos`` in the modetest output. This property can be used with the
   ``-w`` option of modetest. However, this property is not useful without plane overlaying, as it
   won't show use any discernible change on the display. Hence, refer the example given in the next
   section.

 - **Plane Overlaying**

   Use unused planes as overlay planes.

   Based on the version, the DSS controller can have 2 to 4 video pipelines, which get
   enumerated as DRM planes. If the number of displays connected is less than the
   number of video pipes in the DSS controller, the extra pipes can be used as overlay planes.

   In this example, plane 41 remains an unused plane, while plane 31 acts as a primary plane
   for CRTC 38. To use plane 41 as an overlay on top of plane 31, the following command can be
   used.

  .. code-block:: console

        $ modetest -M tidss -s 40@38:1920x1200 -P 41@38:1280x720 -w 41:zpos:1
        setting mode 1920x1200-60.00Hz on connectors 40, crtc 38
        testing 1280x720@XR24 overlay plane 41

  In this example, we use the primary plane via its connector and crtc using the ``-s`` option.
  ``-s 40@38:1920x1200`` renders vertical color bars on the LVDS display. Adding the ``-P`` option,
  ``-P 41@38:1280x720``, renders another frame of color bars (diagonal in this case) of resolution
  1280x720. The ``-w 41:zpos:1`` ensures that the plane 41 is displayed on top of plane 31 (or else,
  if plane 31 is on top, then plane 41 will be underneath and hence won't show up on the display).

 - **Global Alpha Blending**

  Full plane alpha-blending

  When displaying multiple planes on top of one another, we can assign transparency levels to each of
  the planes using the ``alpha`` property. For tidss, the value of this property ranges from 0 with
  complete transparency to 65535 with complete opacity.

  .. code-block:: console

          $ modetest -M tidss -s 40@38:1920x1200 -P 41@38:1280x720 -w 41:zpos:0 -w 31:zpos:1 -w 31:alpha:10000
          setting mode 1920x1200-60.00Hz on connectors 40, crtc 38
          testing 1280x720@XR24 overlay plane 41

  In this example, we are displaying the overlay plane (41) behind the primary plane (31) by
  manipulating the ``zpos`` property. Since the overlay plane is of a smaller resolution (1280x720)
  and the primary plane is of resolution 1920x1200, the overlay plane is expected to not be seen.
  However, with the introduction of the alpha property on the primary plane that doesn't happen. With
  ``alpha`` = 10000 (out of 65535), faint vertical color bars can be seen on the display, along with
  diagonal color bars as solid.

 - **Scaling**

  Scale the frame smaller or larger.

  This feature will only work for plane IDs that map to the VID pipeline of tidss (and not the VIDL
  pipe). Follow this simple rule of thumb to find out if a particular DRM plane is VID or not. DSS-7
  has 4 pipelines in total, while DSS7-UL has 2 pipelines. The VIDL pipelines get enumerated as DRM
  planes first, and then the VID pipes do. Therefore

          - For DSS7-L with 4 pipelines and DRM plane IDs 31, 41, 51, and 58, the DRM planes 51 and 58
            are VID pipelines and thus have scaling support.

          - For DSS7-UL with 2 pipelines and DRM plane IDs 31, and 41, the DRM plane 41 is the VID
            pipeline and thus have scaling support.

  The following example was run on DSS7-UL and hence the pipe with scaling capability is DRM plane 41.

  .. code-block:: console

          $ modetest -M tidss -s 40@38:1920x1200@AR24 -P 41@38:400x400*2
          setting mode 1920x1200-60.00Hz on connectors 40, crtc 38
          testing 400x400@XR24 overlay plane 41

  Note that the ``*2`` at the end of ``-P 41@38:400x400*2`` is the scaling factor.

- **Cropping**

``kmsxxtest`` utility can be used to demonstrate cropping in a video frame using a test pattern.
The user can specify the main video frame size and an input color format using the ``-f`` argument. Then the source region, also known as a view region, can be specified using the ``-v`` argument. This takes a secondary width and height to create a rectangle starting at a given coordinate. The destination region, or plane region, for the view can be specified using ``-p`` argument. This takes a third width, height and coordinate position to place an overlay with the associated view region's content.

.. code-block:: console

   $ kmsxxtest -c hdmi -p 0:0,0-1000x1000 -f 1000x1000-XR24 -v 0,0-1000x1000
   Connector 1/@50: HDMI-A-1
   Crtc 1/@48: 1920x1080@59.93 138.500 1920/48/32/80/+ 1080/3/5/23/- 60 (59.93) 0x9 0x48
   Plane 0/@31: 0,0-1000x1000
   Fb 55 1000x1000-XR24

The above example displays a ``1000x1000`` video frame on the screen at coordinates ``0,0``.

.. figure:: /images/DSS_cropping_example_1.jpg
   :height: 600
   :width: 1020

.. code-block:: console

   $ kmsxxtest -c hdmi -p 0:0,0-800x800 -f 1000x1000 -v 0,0-800x800
   Connector 1/@50: HDMI-A-1
   Crtc 1/@48: 1920x1080@59.93 138.500 1920/48/32/80/+ 1080/3/5/23/- 60 (59.93) 0x9 0x48
   Plane 0/@31: 0,0-800x800
   Fb 55 1000x1000-XR24

Taking as an input a video frame of dimensions ``1000x1000``,the example creates a cropped source rectangle of dimensions ``800x800``, starting at coordinates ``0,0`` and displays it on screen at coordinates ``0,0``.

.. figure:: /images/DSS_cropping_example_2.jpg
   :height: 600
   :width: 1020

.. code-block:: console

   $ kmsxxtest -c hdmi -p 0:500,200-800x800 -f 1000x1000 -v 200,100-800x800
   Connector 1/@50: HDMI-A-1
   Crtc 1/@48: 1920x1080@59.93 138.500 1920/48/32/80/+ 1080/3/5/23/- 60 (59.93) 0x9 0x48
   Plane 0/@31: 500,200-800x800
   Fb 54 1000x1000-XR24

Taking as an input a video frame of dimensions ``1000x1000``, this example creates a cropped source rectangle of dimensions ``800x800``, starting at coordinates ``500,200`` and displays it on screen at coordinates ``200,100`` keeping the same dimensions as source rectangle i.e ``800x800`` without scaling.

.. figure:: /images/DSS_cropping_example_3.jpg
   :height: 600
   :width: 1020

- **Gamma Correction**

Gamma correction or gamma is used to adjust the brightness and color of images on a display. It is applied to ensure that the image appears as intended, with accurate brightness and color representation. Displays, such as LCDs and OLEDs, do not respond linearly to input signals. This means that the display's brightness does not increase linearly with the input voltage. Gamma correction compensates for this non-linear response by applying a non-linear transformation to the input signal. Gamma correction is typically applied using a look-up table (LUT) or a mathematical formula. The LUT or formula maps the input pixel values to output values that have been adjusted to compensate for the display’s non-linear response. DSS7 uses a look-up table for gamma correction. The gamma correction curve is usually represented by a power-law function, where the output value is proportional to the input value raised to a power.

.. math::

   V_{out} = AV_{in}^\gamma

To show the effects of Gamma Correction, we have used a script(`<https://github.com/tomba/kmsxx/blob/master/py/tests/gamma.py>`__) that can be used directly from user-space. The script creates and sets the gamma look-up table using gamma value as 2.2. To use the script, first weston/display-manager should be stopped, see :ref:`stopping-weston`.

Now, save the script and run it.

.. code-block:: console

   $ python3 gamma.py
      press enter to apply gamma

      press enter to remove gamma

      press enter to exit

Below is the test pattern image with gamma correction applied

.. figure:: /images/DSS_example_with_gamma.jpg
   :height: 670
   :width: 1020

Below is the test pattern image without gamma correction

.. figure:: /images/DSS_example_without_gamma.jpg
   :height: 670
   :width: 1020

For further information on gamma correction:

*  `<https://www.w3.org/TR/PNG-GammaAppendix.html>`__
*  `<https://www.benq.com/en-us/knowledge-center/knowledge/gamma-monitor.html>`__

Buffers
-------

The buffers used for tidss can be either allocated from tidss or imported from some other driver (dmabuf import). All buffers must be contiguous.

tidss supports generic DRM dumb buffers. Dumb buffers are allocated using the generic DRM_IOCTL_MODE_CREATE_DUMB ioctl.


fbdev emulation (/dev/fb0)
--------------------------

DRM framework supports "emulating" the legacy fbdev API. This feature can be enabled or disabled in the kernel config (CONFIG_DRM_FBDEV_EMULATION). The fbdev emulation offers only basic feature set and the fb is shown on the first display. Fbdev emulation is mainly intended for kernel console or boot splash screens.
