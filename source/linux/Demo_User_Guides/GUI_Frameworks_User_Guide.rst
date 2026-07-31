.. _GUI_Frameworks_User_Guide:

##############
GUI Frameworks
##############

This document provides an overview of how to develop with different GUI frameworks on
the |__PART_FAMILY_NAME__| platform. The SDK supports many GUI frameworks, including
QT, Flutter and Slint. Use these frameworks to create rich graphical user interfaces
for embedded applications.

See the :ref:`TI-Apps-Launcher-User-Guide-label` documentation for more information about Qt-based demos.
This guide provides a brief overview of Flutter and Slint, along with instructions on how to build and run demos for each.

***************************
How to Develop With Flutter
***************************

About Flutter
=============

The `Flutter <https://flutter.dev/>`__ software development kit from Google is a popular
open source framework for building natively compiled, multi-platform applications from a
single codebase. It offers fast development cycles, expressive GUI, and excellent performance.

Building with Flutter
=====================

Developers who want to use Flutter to build applications on TI embedded platforms,
can follow the process described in the following steps:

#. **Prepare your Yocto environment:**
   Complete the one-time setup prerequisites listed in the |__SDK_FULL_NAME__| documentation at :ref:`building-the-sdk-with-yocto`.

#. **Configure and build the SDK:**
   The following commands will set up the necessary flutter layers(`meta-flutter <https://layers.openembedded.org/layerindex/branch/master/layer/meta-flutter/>`__) and build the image.

   .. code-block:: console

      # Set up the base SDK layers
      git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
      cd tisdk

      # Replace <oeconfig-file> with the default oe-config file for the release
      # uncomment the meta-flutter layer configuration in the selected <oeconfig-file>
      ./oe-layertool-setup.sh -f configs/processor-sdk/<oeconfig-file>
      cd build

      # Add the flutter example demo package to the image
      echo 'IMAGE_INSTALL:append = " flutter-wayland-client flutter-samples-material-3-demo"' >> conf/local.conf

      # Source the environment and build the image
      . conf/setenv
      MACHINE=<machine> bitbake -k tisdk-default-image

   .. note::

      See the :ref:`Yocto Layer Configuration <yocto-layer-configuration>` guide to find the
      correct :file:`<oeconfig-file>` for the SDK release. Set the ``<machine>`` variable
      to your target device as in :ref:`Build_Options`.

#. **Flash the SD Card:**
   Once the build is complete, flash the generated image at :file:`build/deploy-ti/images/<machine>/tisdk-default-image-<machine>.wic.xz`
   on to a SD card. See :ref:`Flash an SD card <processor-sdk-linux-create-sd-card>` for instructions.

Running the Demo
================

After booting the board with the new image, the following :file:`flutter-samples-material-3-demo` shows on the Wayland display after running the following commands:

.. code-block:: console

   systemctl stop ti-apps-launcher
   # Run the demo as weston user
   su weston
   WAYLAND_DISPLAY=/run/user/1000/wayland-1 LD_LIBRARY_PATH=/usr/share/flutter/flutter-samples-material-3-demo/3.38.3/release/lib flutter-client --bundle=/usr/share/flutter/flutter-samples-material-3-demo/3.38.3/release

.. image:: /images/flutter-samples-material-3-demo.png
   :width: 50%
   :align: center
   :alt: Flutter Samples Material 3 Demo

For application specific performance imporvements, refer this `App note <https://www.ti.com/lit/po/sprt761a/sprt761a.pdf>`__.

*************************
How to Develop With Slint
*************************

About Slint
===========

`Slint <https://slint.dev/>`_ is a declarative GUI toolkit to build native user interfaces
for embedded systems and desktop applications. It is designed to be lightweight and efficient,
making it a good choice for resource-constrained embedded systems.

Slint uses a flexible architecture with configurable renderers and backends, controlled
by ``PACKAGECONFIG`` in ``meta-slint``. See the `meta-slint features documentation
<https://github.com/slint-ui/meta-slint#features>`__ for the full list of available
renderers and backends and how to configure them.

On |__PART_FAMILY_NAME__|, the image adapts to the board's graphics stack.
Devices with a GPU render through the hardware-accelerated Skia renderer.
GPU-less devices fall back to the Skia software renderer.

Building with Slint
===================

When ``meta-slint`` is included in the Yocto layer configuration, two image targets are available:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Image target
     - What you get
   * - :file:`tisdk-default-image`
     - Full TI SDK image with Slint demo binaries in :file:`/usr/bin` and :command:`slint-viewer`. The user manually starts a specific demo.
   * - :file:`ti-image-slint-demos`
     - Slint-focused image with the same demo binaries and :command:`slint-viewer`, plus :command:`slint-launcher` which starts
       automatically on boot and presents a graphical list of demos to launch.

**Download a pre-built image**

- **TI SDK image:** Download :file:`tisdk-default-image` from |__SDK_DOWNLOAD_URL__|.
- **Slint demo image:** Download from the
  `meta-slint releases page <https://github.com/slint-ui/meta-slint/releases/tag/demo-images>`__
  (based on :file:`ti-image-slint-demos`, includes the demo launcher).

Flash the downloaded image to an SD card as described in :ref:`Flash an SD card <processor-sdk-linux-create-sd-card>`.

**Build from source**

Follow the steps in :ref:`building-the-sdk-with-yocto`. Use the default oe-config file, which includes
the ``meta-slint`` layer. See :ref:`Yocto Layer Configuration <yocto-layer-configuration>` to find the
correct oe-config file for the release.

.. code-block:: console

   # Standard TI SDK image with Slint demos
   MACHINE=<machine> bitbake tisdk-default-image

   # Slint-focused image with demo launcher
   MACHINE=<machine> bitbake ti-image-slint-demos

Flash the generated image at :file:`build/deploy-ti/images/<machine>/<image>-<machine>.wic.xz`
onto a SD card. See :ref:`Flash an SD card <processor-sdk-linux-create-sd-card>` for instructions.

Running the Demos
=================

The following Slint demo binaries are available in :file:`/usr/bin` on both image types:

* :file:`energy-monitor`
* :file:`gallery`
* :file:`home-automation`
* :file:`opengl_texture`
* :file:`opengl_underlay`
* :file:`printerdemo`
* :file:`slide_puzzle`

**With ti-image-slint-demos (or Slint pre-built image):** :command:`slint-launcher` starts automatically on boot.
Select and start any demo from the graphical list.

**With tisdk-default-image:** Run demos manually. Stop the ti-apps-launcher first before starting any demo.
For example, to run the :command:`home-automation` demo on a Wayland display:

.. code-block:: console

   systemctl stop ti-apps-launcher
   # Run the demo as weston user
   su weston
   WAYLAND_DISPLAY=/run/user/1000/wayland-1 /usr/bin/home-automation


.. image:: /images/slint_home_automation.png
   :width: 50%
   :alt: Slint Home Automation Demo

Slint Viewer
------------

The images now include :command:`slint-viewer`, a tool for previewing :file:`.slint` UI files directly
on the board. Run it in remote mode to connect from your development machine and push live UI updates
to the board as you edit, without rebuilding:

.. code-block:: console

   # View all available options
   slint-viewer --help

   # Start in remote mode — board waits for editor to connect
   slint-viewer --remote

In your editor's Slint live preview, select **Remote** and enter the address shown on the board.
See the `Slint Viewer documentation <https://docs.slint.dev/latest/docs/slint/guide/tooling/slint-viewer/>`__
for full usage.

Here are some snapshots of the other demos running on the device (OpenGL demos require a GPU).

.. list-table::
   :widths: 50 50
   :header-rows: 0

   *  -  .. figure:: /images/slint_opengl_texture.png
            :align: center
            :alt: Slint OpenGL Texture Demo

            OpenGL Texture Demo

      -  .. figure:: /images/slint_opengl_underlay.png
            :align: center
            :alt: Slint OpenGL Underlay Demo

            OpenGL Underlay Demo

   *  -  .. figure:: /images/slint_printer_demo.png
            :align: center
            :alt: Slint Printer Demo

            Printer Demo

      -  .. figure:: /images/slint_puzzle_demo.png
            :align: center
            :alt: Slint Puzzle Demo

            Puzzle demo

   *  -  .. figure:: /images/slint_energy_monitor.png
            :align: center
            :alt: Slint Energy Monitor Demo

            Energy Monitor

      -  .. figure:: /images/slint_gallery.png
            :align: center
            :alt: Slint Gallery Demo

            Gallery Demo
