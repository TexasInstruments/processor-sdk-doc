.. _GUI_Frameworks_User_Guide:

#############
UI Frameworks
#############

This document provides an overview of how to develop with different UI frameworks on
the |__PART_FAMILY_NAME__| platform. The SDK supports many UI frameworks, including
QT, Flutter and Slint. Use these frameworks to create rich graphical user interfaces
for embedded applications.

See the :ref:`TI-Apps-Launcher-User-Guide-label` documentation for more information about Qt-based demos.
This guide provides a brief overview of Flutter and Slint, along with instructions on how to build and run demos for each.

***************************
How to Develop With Flutter
***************************

Overview
========

The `Flutter <https://flutter.dev/>`__ software development kit from Google is a popular
open source framework for building natively compiled, multi-platform applications from a
single codebase. It offers fast development cycles, expressive UI, and excellent performance.

Build Instructions
==================

Developers who want to use Flutter to build applications on TI embedded platforms,
can follow the process described in the following steps:

#. **Prepare your Yocto environment:**
   Complete the one-time setup prerequisites listed in the |__SDK_FULL_NAME__| documentation at :ref:`building-the-sdk-with-yocto`.

#. **Configure and build the SDK:**
   The following commands will set up the necessary flutter layers(`meta-flutter <https://layers.openembedded.org/layerindex/branch/master/layer/meta-flutter/>`__) and build the image.

   .. code-block:: bash

      # Set up the base SDK layers
      git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
      cd tisdk

      # Replace <oeconfig-file> with the appropriate file for the release
      # uncomment the meta-flutter layer configuration in the selected <oeconfig-file>
      ./oe-layertool-setup.sh -f configs/processor-sdk/<oeconfig-file>
      cd build

      # Add the flutter example demo package to the image
      echo 'IMAGE_INSTALL:append = " flutter-wayland-client flutter-samples-material-3-demo"' >> conf/local.conf

      # Source the environment and build the image
      . conf/setenv
      MACHINE=<machine> bitbake -k tisdk-default-image

   .. note::

      Please refer to the :ref:`Yocto Layer Configuration <yocto-layer-configuration>` guide to
      find the correct :file:`<oeconfig-file>` for the SDK release. The ``<machine>`` variable should
      be set to your target device as in :ref:`Build_Options`.

#. **Flash the SD Card:**
   Once the build is complete, flash the generated image at :file:`build/deploy-ti/images/<machine>/tisdk-default-image-<machine>.wic.xz`
   on to a SD card. Please follow the instructions from here to :ref:`Flash an SD card <processor-sdk-linux-create-sd-card>`.

Running the Demo
================

After booting the board with the new image, the following :file:`flutter-samples-material-3-demo` shows on the Wayland display after running the following commands:

.. code-block:: bash

   systemctl stop ti-apps-launcher
   WAYLAND_DISPLAY=/run/user/1000/wayland-1 LD_LIBRARY_PATH=/usr/share/flutter/flutter-samples-material-3-demo/3.38.3/release/lib flutter-client --bundle=/usr/share/flutter/flutter-samples-material-3-demo/3.38.3/release

.. image:: /images/flutter-samples-material-3-demo.png
   :width: 50%
   :align: center
   :alt: Flutter Samples Material 3 Demo

For application specific performance imporvements, refer this `App note <https://www.ti.com/lit/po/sprt761a/sprt761a.pdf>`__.

*************************
How to Develop With Slint
*************************

Overview
========

`Slint <https://slint.dev/>`_ is a declarative GUI toolkit to build native user interfaces
for embedded systems and desktop applications. It is designed to be lightweight and efficient,
making it a good choice for resource-constrained embedded systems.

Slint uses a flexible architecture with interchangeable rendering backends. By default,
it uses its own built-in **FemtoVG** renderer, which is a lightweight, hardware-accelerated
engine that leverages OpenGL ES 2.0. This makes it highly efficient and well-suited for
embedded GPUs like the PowerVR series on the |__PART_FAMILY_NAME__|, providing a great
balance of performance and low resource usage out-of-the-box.

Build Instructions
==================

This guide provides instructions on how to add the `meta-slint <https://layers.openembedded.org/layerindex/branch/master/layer/meta-slint/>`__ layer
to the Yocto build system of the TI Processor SDK to build and run Slint applications.

#. **Prepare your Yocto environment:**
   Complete the one-time setup prerequisites listed in the |__SDK_FULL_NAME__| documentation at :ref:`building-the-sdk-with-yocto`.

#. **Configure and build the SDK:**
   The following commands will set up the necessary Slint and dependent layers and build the image.

   .. code-block:: bash

      # Set up the base SDK layers
      git clone https://git.ti.com/git/arago-project/oe-layersetup.git tisdk
      cd tisdk

      # Create a new config for Slint and add the required meta-layers
      # Replace <oeconfig-file> with the appropriate file for the release
      cp configs/processor-sdk/<oeconfig-file> configs/slint-config.txt
      echo "meta-slint,https://github.com/slint-ui/meta-slint.git,main,7406ee51c140968345b86f3927a8c67984a2dda8,layers=" >> configs/slint-config.txt
      echo "meta-rust-bin,https://github.com/rust-embedded/meta-rust-bin.git,master,79c077fac9694eb5fbcee7b15e800c21e887bb5d,layers=" >> configs/slint-config.txt

      # Set up the bitbake build environment
      ./oe-layertool-setup.sh -f configs/slint-config.txt
      cd build/

      # Add the slint-demos package to the image
      echo 'IMAGE_INSTALL:append = " slint-demos"' >> conf/local.conf

      # Source the environment and build the image
      . conf/setenv
      MACHINE=<machine> bitbake -k tisdk-default-image

   .. note::

      Please refer to the :ref:`Yocto Layer Configuration <yocto-layer-configuration>` guide to
      find the correct ``<oeconfig-file>`` for your SDK release. The ``<machine>`` variable should
      be set to your target device as in :ref:`Build_Options`.

#. **Flash the SD Card:**
   Once the build is complete, flash the generated image at :file:`build/deploy-ti/images/<machine>/tisdk-default-image-<machine>.wic.xz`
   on to a SD card. Please follow the instructions from here to :ref:`Flash an SD card <processor-sdk-linux-create-sd-card>`.

Running the Demos
=================

After booting the board with the new image, you will find several Slint demo binaries located in :file:`/usr/bin`, including:

* :file:`energy-monitor`
* :file:`gallery`
* :file:`home-automation`
* :file:`opengl_texture`
* :file:`opengl_underlay`
* :file:`printerdemo`
* :file:`slide_puzzle`

To run a demo, first stop the ti-apps-launcher that runs out-of-box and then execute the desired binary.
For example, to run the "home-automation" demo on a Wayland display:

.. code-block:: bash

   systemctl stop ti-apps-launcher
   WAYLAND_DISPLAY=/run/user/1000/wayland-1 /usr/bin/home-automation


.. image:: /images/slint_home_automation.png
   :width: 50%
   :alt: Slint Home Automation Demo

Here are some snapshots of the other demos running on the device.

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
