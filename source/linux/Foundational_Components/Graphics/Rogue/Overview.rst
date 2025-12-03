.. include:: <isonum.txt>
.. include:: <isopub.txt>

############
Introduction
############

.. ifconfig:: CONFIG_gpu_ip in ('Rogue_8XE')

   |__PART_FAMILY_DEVICE_NAMES__| device is enabled with 3D graphics
   accelerator based on the Rogue 8XE series from Imagination Technologies Inc.
   It enables the support of 3D graphics rendering using OpenGL\ |reg| ES
   API's. The OpenGL\ |reg| ES API's up to and including version 3.2 with
   render surfaces upto 4k and input textures upto 8k sizes are supported by
   the hardware. It also supports Vulkan |reg| up to API version 1.3.

   For more information about OpenGL\ |reg| ES see :ref:`opengles-api-overview`.

   For more information about Vulkan\ |reg| see :ref:`vulkan-api-overview`.

   For more information about OpenCL\ |reg| see :ref:`opencl-api-overview`.

   .. note::

      Libraries are provided at `<https://git.ti.com/cgit/graphics/ti-img-rogue-umlibs/>`_

   The following extensions are supported:

   .. include:: _8XE_Extension_List.rst


.. ifconfig:: CONFIG_gpu_ip in ('Rogue_AXE')

   |__PART_FAMILY_DEVICE_NAMES__| device is enabled with 3D graphics
   accelerator based on the A-Series AXE-1-16M from Imagination Technologies Inc.
   It enables the support of 3D graphics rendering using OpenGL\ |reg| ES
   API's. The OpenGL\ |reg| ES API's up to and including version 3.1 with
   render surfaces upto 2k and input textures upto 4k sizes are supported by
   the hardware. It also supports Vulkan |reg| up to API version 1.3.

   For more information about OpenGL\ |reg| ES see :ref:`opengles-api-overview`.

   For more information about Vulkan\ |reg| see :ref:`vulkan-api-overview`.

   For more information about OpenCL\ |reg| see :ref:`opencl-api-overview`.

   .. note::

      Libraries are provided, at `<https://git.ti.com/cgit/graphics/ti-img-rogue-umlibs/>`_

   The following extensions are supported:

   .. include:: _AXE_Extension_List.rst


.. ifconfig:: CONFIG_gpu_ip in ('Rogue_BXS')

   |__PART_FAMILY_DEVICE_NAMES__| device is enabled with 3D graphics
   accelerator based on the B-Series BXS-4-64 from Imagination Technologies
   Inc. It enables the support of 3D graphics rendering using OpenGL\ |reg| ES
   API's. The OpenGL\ |reg| ES API's up to and including version 3.2 with
   render surfaces upto 4k and input textures upto 8k sizes are supported by
   the hardware. It also supports Vulkan |reg| up to API version 1.3.

   For more information about OpenGL\ |reg| ES see :ref:`opengles-api-overview`.

   For more information about Vulkan\ |reg| see :ref:`vulkan-api-overview`.

   For more information about OpenCL\ |reg| see :ref:`opencl-api-overview`.

   .. note::

      Libraries are provided, at `<https://git.ti.com/cgit/graphics/ti-img-rogue-umlibs/>`_

   The following extensions are supported:

   .. include:: _BXS_Extension_List.rst


.. note::

   Utilize ``vulkaninfo`` and ``eglinfo`` to list supported extensions.

General Features
================

These devices do not use static memory carve-outs. The only reservations made in
device tree are for control registers. Memory is instead dynamically allocated
at runtime depending on the task and will scale as needed. Scanout buffers come
from the Contiguous Memory Allocation (CMA) pool. Other runtime memory
allocations are from standard pages. See the kernel module memory management
subsystem for more information.


Other features of the Rogue series of GPUs include bilinear and trilinear
filtering.

Support for the following pixel formats:

.. list-table:: Supported pixel formats

   * -
     - ARGB4444
     - ARGB8888
     - BGRA8888
     - RGB565
     - RGBA5551
     - YUV420
     - YUYV
     - NV12
   * - Surface
     -
     - |check|
     - |check|
     - |check|
     -
     -
     -
     -
   * - Texture
     - |check|
     - |check|
     - |check|
     - |check|
     - |check|
     - |check|
     - |check|
     - |check|

Support for Ericsson Texture Compression (ETC1 and ETC2) on input textures.
For an example toolkit to interact with these texture compression mechanisms,
see the Khronos `KTX-Software
<https://github.com/KhronosGroup/KTX-Software>`_ project.

Support for OS controlled Active Power Management, enabled by default.

.. ifconfig:: CONFIG_gpu_ip in ('Rogue_AXE')

   Support for OS suspend and resume functions. See
   :doc:`/linux/How_to_Guides/Target/How_to_suspend_to_ram_on_AM62x` for more
   info.

Software architecture
=====================

The following picture shows the software architecture of Graphics in
|__SDK_FULL_NAME__|.

.. figure:: /images/rogue-graphics-software-stack.png
   :align: center

   PSDK Linux Rogue Graphics Software Stack

Please note that the Rogue Graphics Kernel Module (RGX-KM) in this context
refers to ``pvrsrvkm``, which is currently provided at:

   - `<https://git.ti.com/cgit/graphics/ti-img-rogue-driver>`_

The SDK includes this by default. The kernel module is available at 2 possible
locations depending on the kernel version selected. Before kernel 6.6 the
location for external modules was :file:`extra/`, from 6.6 onward the location
is :file:`updates/`:

.. code-block:: console

   # /lib/modules/$(uname -r)/<external_dir>/pvrsrvkm.ko

Please see the :doc:`Build_Guide` for more information about integration of
this software stack into other ecosystems.

Graphics demos
==============

Along with the graphics driver and user space libraries, the SDK also includes
example applications.

The following 3D Graphics demos are available:

.. list-table:: Demos
   :widths: 25 75
   :header-rows: 1

   * - Demo Name
     - Details
   * - ``Kmscube``
     - This demo shows how to render and display multi-colored spinning cube
   * - ``offscreendemo``
     - Lightweight Render Example. Heavily inspired by Eduardo Lima's gpu-playground,
       this attempts to act as the smallest demo of offscreen rendering.
