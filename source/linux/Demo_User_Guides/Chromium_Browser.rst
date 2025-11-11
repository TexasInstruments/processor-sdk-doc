.. role:: console(code)
  :language: console
  :class: highlight

.. _Chromium_Browser-label:

Chromium Browser - User Guide
=============================

Overview
--------

On TI devices with IMG Rogue class GPU's.  The Chromium browser (available from https://chromium.googlesource.com/chromium/src/)
is accelerated using OpenGLES.

The version of Chromium that is build can be obtained with this command:

.. code-block:: console

    $ chromium --version
    Chromium 123.0.6312.122 stable

The version of Chromium shown here is the one that GPU acceleration is verified to work with.

Launching Chromium Browser
--------------------------

.. danger::

   For security reasons it is suggested never to run Chromium as the root user.

To launch the Chromium browser:

Assuming you are logged in as the root user.

Switch to the weston user:

.. code-block:: console

    $ su weston

And then run the chromium binary:

.. code-block:: console

    $ /usr/bin/chromium [url] [options]

e.g.

.. code-block:: console

    $ chromium https://www.ti.com

Will open www.ti.com in a windowed browser on the Weston desktop.

.. code-block:: console

    $ chromium https://webglsamples.org/aquarium/aquarium.html --start-fullscreen

Will open the aquarium 3d benchmark in a fullscreen window on the Weston desktop.

The :console:`--start-fullscreen` switch will make the chromium browser consume the entire screen including overwriting the Weston menu bar.

This will start chromium and provided you have network connectivity to the internet from the TI platform it will
connect to an example application that uses WebGL/Javascript and renders fish swimming in a fish bowl using the 3D GPU.

Graphics Feature Status
-----------------------

To see the GPU features that are in use, enter :code:`chrome://gpu` into the Chromium URL/Navigation bar. A web page will be
rendered with this information. The below example shows what is enabled/disabled when GPU acceleration is working correctly

.. code-block:: text

    *   Canvas: Hardware accelerated
    *   Canvas out-of-process rasterization: Disabled
    *   Direct Rendering Display Compositor: Disabled
    *   Compositing: Hardware accelerated
    *   Multiple Raster Threads: Enabled
    *   OpenGL: Enabled
    *   Rasterization: Hardware accelerated
    *   Raw Draw: Disabled
    *   Video Decode: Hardware accelerated
    *   Video Encode: Software Only. Hardware acceleration disabled
    *   Vulkan: Disabled
    *   WebGL: Hardware accelerated
    *   WebGL2: Hardware accelerated
    *   WebGPU: Disabled


If for some reason you suspect the GPU is rending something incorrectly, you can run chromium with GPU disabled
using the :console:`--disable-gpu` flag:

.. code-block:: console

    $ chromium https://webglsamples.org/aquarium/aquarium.html --start-fullscreen --disable-gpu


To get raw performance numbers from the GPU, you may want to disable frame sync locking in Chromium. This will tell Chromium never to wait for VSYNC and render as fast as the GPU can achieve.

.. code-block:: console

    $ chromium https://webglsamples.org/aquarium/aquarium.html --start-fullscreen --disable-gpu-vsync --disable-frame-rate-limit 


Running Chromium as the root user
---------------------------------

This is absolutely not recommended, as to do so gives a web page too much access to your system.  
To run in this mode you also have to provide the :console:`--no-sandbox` switch, which disables all sandboxing
of the browser from the base system and could leave you open for a malicious webpage to do something
nefarious.


How to build Chromuim under Yocto
---------------------------------

Pull in the meta-browser and meta-clang layer into a Scarthgap Yocto build.

meta-browser should be pinned to commit:

.. code-block:: text

    commit 1ed2254d72a4c25879014c98be287a7e3e22904c
    Author: Max Ihlenfeldt <max@igalia.com>
    Date:   Wed May 22 14:54:02 2024 +0200

        chromium: Backport missing dependency in NewTabPage (#816)

meta-clang needs to be pinned to HEAD commit of branch "scarthgap", as of the time of writing that equates to this commit:

.. code-block:: text

    commit e7dceb1c92caf7f21ef1d7b49c85328c30cffd90 (HEAD -> scarthgap, origin/scarthgap)
    Author: Etienne Cordonnier <ecordonnier@snap.com>
    Date:   Fri May 3 17:47:46 2024 +0200

        clang: use release tarball instead of git

With these layers pinned to the correct commit, you need to make sure they are referenced in :console:`build/conf/bblayers.conf`
This is done automatically if you use the oe-layersetup tool.

.. code-block:: console

    $ cd yocto_dir
    $ ./oe-layersetup -f config/arago-scarthgap-chromium-config.txt

Once this is done, use bitbake to create the tisdk-default-image. This will 
detect the meta-browser and meta-clang layers, automatically building and 
adding Chromium to the root filesystem image.

.. tip::

    Build times of Chromium can be very long depending on the size of your build machine. It has been found that you need
    at least 64Gigs of RAM, and on a 28 thread Intel Core-I9 with an SSD for the build driver it will still take upwards of 2 hours just
    to build Chromium. A full Yocto Scarthgap build that includes Chromium can easily take 400GBytes of SSD.

The following will initiate a full tisdk-default-image build that would include
Chromium if the meta-browser and meta-clang layers are present:

.. code-block:: console

    $ MACHINE=<machine> bitbake tisdk-default-image

If you want to significantly reduced image size, the IPKs can be built
directly using the following:

.. code-block:: console

    $ MACHINE=<machine> bitbake core-image-weston
    $ MACHINE=<machine> bitbake chromium-ozone-wayland

Where <machine> is defined in the :ref:`Build Options section of "Building the SDK with Yocto" <Build_Options>`

:console:`tisdk-default-image` is the only image that chromium will get built
into by default.  If you want to build it into another image, then you would need to modify the .bb recipe for the image.  Or alternatively
add the line:

.. code-block:: text
    
    IMAGE_INSTALL:append = " chromium-ozone-wayland"

Somewhere into your :file:`build/conf/local.conf` file.

Limitations
-----------

* Audio/video within the browser is not supported.
* Hardware acceleration of video either decode or encode is not supported.

Performance
-----------

**Performance of WebGL Aquarium**

Standard WebGL benchmarks available at these URLS: https://webglsamples.org/aquarium/aquarium.html

Run as the weston user with the command line :console:`chromium https://webglsamples.org/aquarium/aquarium.html --start-fullscreen`


.. ifconfig:: CONFIG_part_variant in ('AM62PX')

        +---------------------------------+----------------------+------------------------------------------------+
        | **Platform**                    | **Performance FPS**  | **GPU Utilisation**                            |
        +---------------------------------+----------------------+------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 36 @ 1080p60         | 72%                                            |
        +---------------------------------+----------------------+------------------------------------------------+

    .. note::

          GPU Utilisation is captured using,

          .. code-block:: console

              root@am62pxx-evm:~# cat /sys/kernel/debug/pvr/status

.. ifconfig:: CONFIG_part_variant in ('AM62X')

        +---------------------------------+----------------------+------------------------------------------------+
        | **Platform**                    | **Performance FPS**  | **GPU Utilisation**                            |
        +---------------------------------+----------------------+------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 11 @ 1080p60         | 100%                                           |
        +---------------------------------+----------------------+------------------------------------------------+
        | Beagleplay                      | 11 @ 1080p60         | 100%                                           |
        +---------------------------------+----------------------+------------------------------------------------+


       .. note::

          GPU Utilisation is captured using,

          .. code-block:: console

              root@<machine>:~# cat /sys/kernel/debug/pvr/status

.. ifconfig:: CONFIG_part_variant in ('J722S')

        +---------------------------------+-----------------------------------------------------------------------+
        | **Platform**                    | **Performance FPS**                                                   |
        +---------------------------------+-----------------------------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 33 @ 1080p60                                                          |
        +---------------------------------+-----------------------------------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J721S2')

        +---------------------------------+-----------------------------------------------------------------------+
        | **Platform**                    | **Performance FPS**                                                   |
        +---------------------------------+-----------------------------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 53 @ 1080p60                                                          |
        +---------------------------------+-----------------------------------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J784S4')

        +---------------------------------+-----------------------------------------------------------------------+
        | **Platform**                    | **Performance FPS**                                                   |
        +---------------------------------+-----------------------------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 60 @ 1080p60                                                          |
        +---------------------------------+-----------------------------------------------------------------------+

**Performance of MotionMarkv1.3**

Standard Javascript benchmarks available at these URLS: https://browserbench.org/MotionMark/

Run as the weston user with the command line :console:`chromium https://browserbench.org/MotionMark/ --start-fullscreen`
use the mouse to click the "Run Benchmark" button.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

        +---------------------------------+-----------------------------------------------------------------------+
        | **Platform**                    | **MotionMark v1.3**                                                   |
        +---------------------------------+-----------------------------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 51.56 @ 1080p60                                                       |
        +---------------------------------+-----------------------------------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('AM62X')

        +---------------------------------+-----------------------------------------------------------------------+
        | **Platform**                    | **MotionMark v1.3**                                                   |
        +---------------------------------+-----------------------------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 1.51 @ 1080p60                                                        |
        +---------------------------------+-----------------------------------------------------------------------+
        | Beagleplay                      | 1.77 @ 1080p60                                                        |
        +---------------------------------+-----------------------------------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J722S')

        +---------------------------------+-----------------------------------------------------------------------+
        | **Platform**                    | **MotionMark v1.3**                                                   |
        +---------------------------------+-----------------------------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 37.56 @ 1080p60                                                       |
        +---------------------------------+-----------------------------------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J721S2')

        +---------------------------------+-----------------------------------------------------------------------+
        | **Platform**                    | **MotionMark v1.3**                                                   |
        +---------------------------------+-----------------------------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 67.88 @ 1080p60                                                       |
        +---------------------------------+-----------------------------------------------------------------------+

.. ifconfig:: CONFIG_part_variant in ('J784S4')

        +---------------------------------+-----------------------------------------------------------------------+
        | **Platform**                    | **MotionMark v1.3**                                                   |
        +---------------------------------+-----------------------------------------------------------------------+
        | |__PART_FAMILY_NAME__|          | 177.11 @ 1080p60                                                      |
        +---------------------------------+-----------------------------------------------------------------------+

