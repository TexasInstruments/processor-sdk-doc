.. role:: console(code)
  :language: console
  :class: highlight

.. _Chromium_Browser-label:

#############################
Chromium Browser - User Guide
#############################

********
Overview
********

On TI devices with IMG Rogue class GPU's,The Chromium browser (available from https://chromium.googlesource.com/chromium/src/)
is accelerated using OpenGLES.

The version of Chromium that is build can be obtained with this command:

.. code-block:: console

    $ chromium --version
    Chromium 126.0.6478.126 built on Debian trixie/sid, running on Debian trixie/sid

The version of Chromium shown here is the one that GPU acceleration is verified to work with.

**************************
Launching Chromium Browser
**************************

.. danger::

   For security reasons it is suggested never to run Chromium as the root user. So it's safe to create and switch to another user and then run chromium.

.. note::

   ``--no-sandbox`` option is required only when running as root user.

To launch the Chromium browser:

Assuming you are logged in as the root user.

.. code-block:: console

    $ /usr/bin/chromium [url] --use-gl=angle --ozone-platform=wayland --no-sandbox [options]

e.g.

.. code-block:: console

    $ chromium https://www.ti.com --use-gl=angle --ozone-platform=wayland --no-sandbox

Will open www.ti.com in a windowed browser on the Weston desktop.

.. code-block:: console

    $ chromium https://webglsamples.org/aquarium/aquarium.html --use-gl=angle --ozone-platform=wayland --no-sandbox --start-fullscreen

Will open the aquarium 3d benchmark in a fullscreen window on the Weston desktop.

The :console:`--start-fullscreen` switch will make the chromium browser consume the entire screen including overwriting the Weston menu bar.

This will start chromium and provided you have network connectivity to the internet from the TI platform it will
connect to an example application that uses WebGL/Javascript and renders fish swimming in a fish bowl using the 3D GPU.

***********************
Graphics Feature Status
***********************

To see the GPU features that are in use, enter :code:`chrome://gpu` into the Chromium URL/Navigation bar. A web page will be
rendered with this information. The below example shows what is enabled/disabled when GPU acceleration is working correctly

.. code-block:: text

    *   Canvas: Hardware accelerated
    *   Canvas out-of-process rasterization: Enabled
    *   Direct Rendering Display Compositor: Disabled
    *   Compositing: Hardware accelerated
    *   Multiple Raster Threads: Enabled
    *   OpenGL: Enabled
    *   Rasterization: Hardware accelerated on all pages
    *   Raw Draw: Disabled
    *   Skia Graphite: Disabled
    *   Video Decode: Hardware accelerated
    *   Video Encode: Software only. Hardware acceleration disabled
    *   Vulkan: Disabled
    *   WebGL: Hardware accelerated
    *   WebGL2: Hardware accelerated
    *   WebGPU: Disabled
    *   WebNN: Disabled


If for some reason you suspect the GPU is rending something incorrectly, you can run chromium with GPU disabled
using the :console:`--disable-gpu` flag:

.. code-block:: console

    $ chromium https://webglsamples.org/aquarium/aquarium.html --start-fullscreen --disable-gpu


To get raw performance numbers from the GPU, you may want to disable frame sync locking in Chromium. This will tell Chromium never to wait for VSYNC and render as fast as the GPU can achieve.

.. code-block:: console

    $ chromium https://webglsamples.org/aquarium/aquarium.html --start-fullscreen --disable-gpu-vsync --disable-frame-rate-limit


***********
Limitations
***********

* Audio/video within the browser is not supported.
* Hardware acceleration of video either decode or encode is not supported.
* Minimize and Maximize buttons for the Chromium window are not supported.

***********
Performance
***********

Performance of WebGL Aquarium
=============================

Standard WebGL benchmarks available at these URLS: https://webglsamples.org/aquarium/aquarium.html

Run as the root user

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

        +---------------------------------+----------------------+------------------------------------------------+
        | **Platform**                    | **Performance FPS**  | **GPU Utilisation**                            |
        +---------------------------------+----------------------+------------------------------------------------+
        | |__PART_FAMILY_DEVICE_NAMES__|  | 36 @ 1080p60         | 72%                                            |
        +---------------------------------+----------------------+------------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62X')

        +---------------------------------+----------------------+------------------------------------------------+
        | **Platform**                    | **Performance FPS**  | **GPU Utilisation**                            |
        +---------------------------------+----------------------+------------------------------------------------+
        | |__PART_FAMILY_DEVICE_NAMES__|  | 11 @ 1080p60         | 100%                                           |
        +---------------------------------+----------------------+------------------------------------------------+

.. note::

    GPU Utilisation is captured using,

    .. code-block:: console

        root@<machine>:~# cat /sys/kernel/debug/pvr/status


Performance of MotionMark
=========================

Standard Javascript benchmarks available at these URLS: https://browserbench.org/MotionMark/

Run as the root user

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

        +---------------------------------+-----------------------------------------------------------------------+
        | **Platform**                    | **MotionMark v1.3**                                                   |
        +---------------------------------+-----------------------------------------------------------------------+
        | |__PART_FAMILY_DEVICE_NAMES__|  | 45.85 @ 1080p60                                                       |
        +---------------------------------+-----------------------------------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62X')

        +---------------------------------+-----------------------------------------------------------------------+
        | **Platform**                    | **MotionMark v1.3**                                                   |
        +---------------------------------+-----------------------------------------------------------------------+
        | |__PART_FAMILY_DEVICE_NAMES__|  | 1.29 @ 1080p60                                                        |
        +---------------------------------+-----------------------------------------------------------------------+

