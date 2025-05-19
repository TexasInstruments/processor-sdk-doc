.. include:: <isonum.txt>

Introduction
============

TI SOCs such as AM335x, AM437x, AM57xx and AM65xx have 3D cores capable of
accelerating 3D operations with dedicated hardware. The dedicated hardware is
using the SGX series of devices from Imagination Technologies (IMG). The
graphics cores only accelerate graphics operations, and do not perform video
decode operations. For video acceleration, see the Technical Reference Manuals
for the associated SoC.

The following table lists the various TI families supported by this SDK, and the
SGX core information:

.. list-table:: TI System on Chips, and SGX cores
   :header-rows: 1

   * - TI SoC Name
     - SGX Core
     - SGX Core Revision
     - Max SGX Core Frequency (MHz)
   * - AM335x
     - SGX530
     - 1.2.5
     - 200
   * - AM437x
     - SGX530
     - 1.2.5
     - 200
   * - AM57xx
     - SGX544
     - 1.1.6
     - 532
   * - AM65xx
     - SGX544
     - 1.1.7
     - 450

The SGX cores in AM family support OpenGL\ |reg| ES 1.1 and OpenGL\ |reg| ES
2.0 APIs.

These devices do not use static memory carve-outs. The only reservations made in
device tree are for control registers. Memory is instead dynamically allocated
at runtime depending on the task and will scale as needed. Scanout buffers come
from the Contiguous Memory Allocation (CMA) pool and other runtime memory
allocations come from standard pages. See the kernel module memory management
subsystem for more information.

Software architecture
=====================

The following picture shows the software architecture of Graphics in
|__SDK_FULL_NAME__|.

.. figure:: /images/Graphic_software_stacks_DRM.png
   :align: center

   Graphics Software Stack

Please see the :doc:`Build_Guide` for more information about integration of this
software stack into other ecosystems.

Graphics demos
==============

Along with the graphics driver and user space libraries, the SDK also includes
example applications. Some of the demos are from the IMG Native_SDK examples.

The following demos are available to run under the Wayland windowing system.

.. code-block:: console

   # /usr/bin/SGX/demos/Wayland/OpenGLESDeferredShading
   # /usr/bin/SGX/demos/Wayland/OpenGLESGaussianBlur
   # /usr/bin/SGX/demos/Wayland/OpenGLESImageBasedLighting
   # /usr/bin/SGX/demos/Wayland/OpenGLESIntroducingPVRCamera
   # /usr/bin/SGX/demos/Wayland/OpenGLESIntroducingPVRUtils
   # /usr/bin/SGX/demos/Wayland/OpenGLESIntroducingUIRenderer
   # /usr/bin/SGX/demos/Wayland/OpenGLESNavigation2D
   # /usr/bin/SGX/demos/Wayland/OpenGLESNavigation3D
   # /usr/bin/SGX/demos/Wayland/OpenGLESParticleSystem

Running demos in null window system mode
----------------------------------------

The graphics demos can also run in null-window system mode outside of Wayland
windowing system as full screen applications. To do so, :ref:`stop Weston
<stopping-weston>`. After that, access the command line from serial console, SSH
console, or LCD console.

Please make sure the board has at least one display connected before running
these demos.

.. code-block:: console

   # /usr/bin/SGX/demos/DRM/OGLES2Coverflow
   # /usr/bin/SGX/demos/DRM/OGLES2ChameleonMan
   # /usr/bin/SGX/demos/DRM/OGLES2ExampleUI
   # /usr/bin/SGX/demos/DRM/OGLES2Navigation

After you see the output on the display interface, press *q* to exit the
application.

Some of the demos under null windowing system require the user to pass in
the DRM connector id. For information about how to get connector id,
see the :ref:`finding_the_connector_id` section.

