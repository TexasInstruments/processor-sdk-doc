#######
Display
#######

TI SoCs are equipped with Display SubSystem (DSS) hardware to provide hardware
acceleration for alpha blending of overlays and color conversion. The DSS
hardware is exposed to the software drm API available through ``libdrm`` module.
Through this drm interface, a user space program can perform *mode setting* of
the display.

The drm module models the display hardware as a series of abstract hardware
blocks and manages them through the API. The blocks are:

   - CRTC\ [#f1]_\: represents a scanout engine that generates video timing
     signal from the data pointed to by the scanout buffer

   - Connector: represents where the video timing signal is sent across to the
     display

   - Encoder: transforms the video timing signal from CRTC to a format that is
     suitable for sending across the connector

   - Plane: represents the overlay buffer that a CRTC can be fed with

A utility application ``modetest`` can be used to get the list of available drm
blocks. All the information available for the device can be displayed by using
it.

.. ifconfig:: CONFIG_image_type in ('adas')

    .. note::

       For ADAS parts by default Display is disabled in linux via
       k3-<soc>-vision-apps.dtso and enabled to be controlled by one of the
       real time r5f core. So modetest, kmstest, weston will not work.
       To enabled it you need to modify k3-<soc>-vision-apps.dtso, rebuild
       linux-dtbs and install. Also need to disable Display in r5f, rebuild
       r5f FW using PSDK RTOS.

********************
Finding Connector ID
********************

Run the below ``modetest`` command:

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family')

   .. code-block:: console

      # modetest -c

.. ifconfig:: CONFIG_part_family in ('J7_family', 'AM62X_family')

   .. code-block:: console

      # modetest -M tidss -c

Look for the display device for which the connector ID is required -
such as HDMI, LCD etc.

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

****************
Finding Plane ID
****************

To find the Plane ID, run the ``modetest`` command:

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family')

   .. code-block:: console

      # modetest -p

.. ifconfig:: CONFIG_part_family in ('J7_family', 'AM62X_family')

   .. code-block:: console

      # modetest -M tidss -p

Which should show something like below:

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

*******************************
Using Connector ID and Plane ID
*******************************

The above information may be used with some userspace applications to control
which displays are rendered to. These applications are using what is known as
kernel mode setting (kms). For more information about kernel mode setting see
the `upstream kms documentation`_. In this section you only need to keep 2
things in mind:

   #. Applications that intend to interact with the kms interface usually don't
      need any user input. They can query device info through the interface and
      will normally pick the first connected display automatically.

   #. Only one application can manage the kms interface at a time. Weston is
      normally the first graphical application started out of the box and as
      such it will prevent you from starting any other kms applications. See
      :ref:`stopping-weston` if you want to use another kms application.

.. _upstream kms documentation: https://www.kernel.org/doc/html/latest/gpu/drm-kms.html

That being said, if you wish to change rendering behavior for an application
check with that applications documentation for a way to specify connector,
plane, and / or crtc information. One kms application we include is ``kmscube``.
Below are some examples on how to alter it's default behavior.

Run kmscube on the default display:

.. code-block:: console

   # kmscube

Run kmscube on the secondary display:

.. code-block:: console

   # kmscube -n <connector-id>

For example, if the connector id for the secondary display is 16:

.. code-block:: console

   # kmscube -n 16

.. [#f1]

   CRTC stands for cathode-ray tube controller, a throw back to the old
   `cathode-ray tubes TV's <https://en.wikipedia.org/wiki/Cathode-ray_tube>`_
   which had a controller that generated video timings based on the data it is
   being fed by a buffer.
