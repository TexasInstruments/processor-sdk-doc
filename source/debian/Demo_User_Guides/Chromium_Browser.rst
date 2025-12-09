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

On TI devices with IMG Rogue class GPUs, the Chromium browser (available from https://chromium.googlesource.com/chromium/src/)
is accelerated using OpenGLES.

The version of Chromium that is built can be obtained with the following command:

.. code-block:: console

    root@am62xx-evm:~# chromium -version
    Chromium 130.0.6723.116 built on Debian GNU/Linux trixie/sid


The above version of Chromium has been verified to support GPU acceleration.

**************************
Launching Chromium Browser
**************************

.. danger::

   For security reasons it is suggested never to run Chromium as the root user. So it's safe to create and switch to another user and then run chromium.

.. note::

   ``--no-sandbox`` option is required only when running as root user.

The following is assuming that you are logged in as the root user. The syntax of the command is as follows:

.. code-block:: console

    $ /usr/bin/chromium [url] --use-gl=angle --ozone-platform=wayland --no-sandbox [options]

For example, the following command opens www.ti.com in a windowed browser on the Weston desktop.

.. code-block:: console

    $ chromium https://www.ti.com --use-gl=angle --ozone-platform=wayland --no-sandbox

The following command opens the aquarium 3D benchmark in a fullscreen window on the Weston desktop, provided you have
network connectivity to the internet from the TI platform. This benchmark uses WebGL/Javascript, and renders an
animation of fish swimming in a fish bowl, using the 3D GPU.

.. code-block:: console

    $ chromium https://webglsamples.org/aquarium/aquarium.html --use-gl=angle --ozone-platform=wayland --no-sandbox --start-fullscreen


The :console:`--start-fullscreen` switch makes the Chromium browser consume the entire screen, including the Weston menu bar.

***********************
Graphics Feature Status
***********************

To see the GPU features in use, enter :code:`chrome://gpu` into the Chromium URL/Navigation bar. The example below shows
what is enabled/disabled when GPU acceleration is working correctly:

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


If, for some reason, you suspect that the GPU is rendering something incorrectly, you can run Chromium with the GPU disabled
using the :console:`--disable-gpu` flag:

.. code-block:: console

    $ chromium https://webglsamples.org/aquarium/aquarium.html --start-fullscreen --disable-gpu


To get raw performance numbers from the GPU, you may want to disable frame sync locking in Chromium. This will tell Chromium to never wait for VSYNC and render as fast as the GPU can.

.. code-block:: console

    $ chromium https://webglsamples.org/aquarium/aquarium.html --start-fullscreen --disable-gpu-vsync --disable-frame-rate-limit


***********
Limitations
***********

* Audio/video within the browser is not supported.
* Hardware acceleration of video decode and/or encode is not supported.
* Minimize and Maximize buttons for the Chromium window are not supported.

***********
Performance
***********

Performance of WebGL Aquarium
=============================

Standard WebGL benchmarks are available at https://webglsamples.org/aquarium/aquarium.html

Run as the root user

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

        +---------------------------------+----------------------+------------------------------------------------+
        | **Platform**                    | **Performance FPS**  | **GPU Utilisation**                            |
        +---------------------------------+----------------------+------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 36 @ 1080p60         | 72%                                            |
        +---------------------------------+----------------------+------------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62X')

        +---------------------------------+----------------------+------------------------------------------------+
        | **Platform**                    | **Performance FPS**  | **GPU Utilisation**                            |
        +---------------------------------+----------------------+------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 11 @ 1080p60         | 100%                                           |
        +---------------------------------+----------------------+------------------------------------------------+

.. note::

    GPU Utilisation is captured using,

    .. code-block:: console

        root@<machine>:~# cat /sys/kernel/debug/pvr/status


Performance of MotionMark
=========================

Standard Javascript benchmarks are available at https://browserbench.org/MotionMark/

Run as the root user

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

        +---------------------------------+-----------------------------------------------------------------------+
        | **Platform**                    | **MotionMark v1.3**                                                   |
        +---------------------------------+-----------------------------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 45.85 @ 1080p60                                                       |
        +---------------------------------+-----------------------------------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62X')

        +---------------------------------+-----------------------------------------------------------------------+
        | **Platform**                    | **MotionMark v1.3**                                                   |
        +---------------------------------+-----------------------------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 1.29 @ 1080p60                                                        |
        +---------------------------------+-----------------------------------------------------------------------+

