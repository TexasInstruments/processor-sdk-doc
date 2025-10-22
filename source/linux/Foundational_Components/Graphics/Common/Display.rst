#######
Display
#######

TI SoCs with Display Sub-System (DSS) hardware offer hardware acceleration for
alpha blending of overlays and color conversion. The ``libdrm`` module exposes
DSS hardware through the software Direct Render Management (DRM) API. Through
this DRM interface, a user space program can perform *mode setting* of the
display.

The DRM module models the display hardware as a series of abstract hardware
blocks and manages them through the API. The blocks are:

   - CRTC\ [#f1]_\: represents a scanout engine that generates video timing
     signal from the data pointed to by the scanout buffer

   - Connector: represents where the video timing signal goes and how it gets
     there

   - Encoder: transforms the video timing signal from the CRTC to a format that
     is suitable for sending to the connector

   - Plane: represents the overlay buffer that will feed a CRTC

The list of available DRM blocks is viewable using the application
:command:`modetest`.

.. ifconfig:: CONFIG_image_type in ('adas')

    .. note::

       For ADAS parts by default Display is disabled in linux via
       k3-<soc>-vision-apps.dtso and enabled to be controlled by one of the
       real time r5f core. So modetest, kmsxxtest, weston will not work.
       To enabled it you need to modify k3-<soc>-vision-apps.dtso, rebuild
       linux-dtbs and install. Also need to disable Display in r5f, rebuild
       r5f FW using PSDK RTOS.

.. _finding_the_connector_id:

************************
Finding the connector ID
************************

Run the following ``modetest`` command:

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family')

   .. code-block:: console

      # modetest -c

.. ifconfig:: CONFIG_part_family in ('J7_family', 'AM62X_family')

   .. code-block:: console

      # modetest -M tidss -c

Look for the required display device's connector ID - such as High-Definition
Multimedia Interface (HDMI), DisplayPort (DP), and so on.

.. code-block:: text

   Connectors:
   id      encoder status          type    size (mm)       modes   encoders
   4       3       connected       HDMI-A  480x270         20      3
     modes:
           name refresh (Hz) hdisp hss hse htot vdisp vss vse vtot)
     1920x1080 60 1920 2008 2052 2200 1080 1084 1089 1125 flags: phsync, pvsync; type: preferred, driver
   ...
   16      15      connected       unknown 0x0             1       15
     modes:
           name refresh (Hz) hdisp hss hse htot vdisp vss vse vtot)
     800x480 60 800 1010 1040 1056 480 502 515 525 flags: nhsync, nvsync; type: preferred, driver

The modes displayed are the various resolutions supported by the connected
display.

********************
Finding the plane ID
********************

To find the Plane ID, run the ``modetest`` command:

.. ifconfig:: CONFIG_part_family in ('AM335X_family', 'AM437X_family')

   .. code-block:: console

      # modetest -p

.. ifconfig:: CONFIG_part_family in ('J7_family', 'AM62X_family')

   .. code-block:: console

      # modetest -M tidss -p

Which should show something similar to the following:

.. code-block:: text

   Planes:
   id      crtc    fb      CRTC x,y        x,y     gamma size
   19      0       0       0,0             0,0     0
    formats: RG16 RX12 XR12 RA12 AR12 XR15 AR15 RG24 RX24 XR24 RA24 AR24 NV12 YUYV UYVY
    props:
    ...
   20      0       0       0,0             0,0     0
    formats: RG16 RX12 XR12 RA12 AR12 XR15 AR15 RG24 RX24 XR24 RA24 AR24 NV12 YUYV UYVY
    props:
    ...

***********************************
Using the connector ID and plane ID
***********************************

The earlier information is useful when attempting to select what display to
render to. Some user space applications have command line switches to easily
show this. These applications are using Kernel Mode Setting (KMS). For more
information about KMS see the `upstream kms documentation`_. For now, you only
need to keep 2 things in mind:

   #. Applications that intend to interact with the KMS interface usually do not
      need any user input. They can query device info through the interface
      and will normally pick the first connected display automatically.

   #. Only one application can manage the KMS interface at a time. Weston is
      normally the first graphical application started by default and as such
      it will prevent you from starting any other KMS applications. See
      :ref:`stopping-weston` if you want to use another KMS application.

.. _upstream kms documentation: https://www.kernel.org/doc/html/latest/gpu/drm-kms.html

If you want to change rendering behavior for an application check with that
applications documentation for a way to specify a connector, plane, and / or
CRTC information. One KMS application we include is :command:`kmscube`. Below
are some examples on how to avoid the default behavior of automatically choosing
a display to render to.

Run :command:`kmscube` on the default display:

.. code-block:: console

   # kmscube

Run :command:`kmscube` on the secondary display:

.. code-block:: console

   # kmscube -n <connector_id>

For example, if the connector id for the secondary display is 16:

.. code-block:: console

   # kmscube -n 16

.. [#f1]

   CRTC stands for Cathode-Ray Tube Controller, a throw back to the old
   `cathode-ray tubes TV's <https://en.wikipedia.org/wiki/Cathode-ray_tube>`_
   which had a controller that generated video timings based on the data it is
   receiving from a buffer.
