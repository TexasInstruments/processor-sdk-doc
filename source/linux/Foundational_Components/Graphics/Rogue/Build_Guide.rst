.. _rogue-build-guide:

###########
Build guide
###########

The graphics stack on rogue has fluctuated a little over the years as we have
adjusted for binary longevity in the proprietary stack. This will go over some
of the discrepancies between releases and how you can build the releases stand
alone.

*****************
Proprietary stack
*****************

The proprietary stack has been our default offering for all releases so far. It
consists of 3 main components with varying classifications:

   - The kernel module (KM) (Open Source, but out-of-tree)
   - The GLES / Vulkan / OpenCL user mode (UM) libraries (Closed Source, binary
     release)
   - The mesa shim (Open Source, but out-of-tree)

GLES and Vulkan support requires all 3 of these components. Exceptions will are
in :ref:`rogue-proprietary-mesa-components`.

Proprietary kernel module
=========================

The kernel module provides:

   - Memory and power management
   - Loading firmware
   - Monitoring device state
   - Orchestrating hardware recoveries
   - Creating an interface for the user space server

The source is available at:

   https://git.ti.com/cgit/graphics/ti-img-rogue-driver/

.. _rogue-building-the-proprietary-kernel-module:

Building the proprietary kernel module
--------------------------------------

Pick a branch that corresponds to your particular kernel. Keep note of the name.
The UM part must match this release.

The :file:`INSTALL` file gives a brief overview of how to build and install the
module. This gives you the common variables, but it does omit some of the more
important ones for the build. The following variables are key and *must* match
with the values used in the UM release:

   - ``BUILD`` -- Options: ``release`` or ``debug``
   - ``PVR_BUILD_DIR`` -- Options: ``<platform>_linux``, for example ``am62_linux``
   - ``WINDOW_SYSTEM`` -- Options: ``lws-generic``, ``xorg``, ``wayland``, among
     others

These variables are mandatory. To check for updated build variables see the
``EXTRA_OEMAKE`` variable in the `ti-img-rogue-driver recipe in meta-ti`_. This
will always contain the latest required variables to compile the driver.

.. _ti-img-rogue-driver recipe in meta-ti: https://git.ti.com/cgit/arago-project/meta-ti/tree/meta-ti-bsp/recipes-bsp/powervr-drivers/ti-img-rogue-driver_24.1.6554834.bb?h=10.01.09

As before mentioned these build options must match with the corresponding UM
build options. Currently we only release binaries with ``BUILD=release`` and
``WINDOW_SYSTEM=lws-generic``. The UM section will go into exceptions to this.


Proprietary user space components
=================================

All interactions with the GPU require the proprietary user space components. It
has the actual firmware binaries, GLES / Vulkan / OpenCL implementation, and the
primary control server.

The binary release for this part is available at:

   https://git.ti.com/cgit/graphics/ti-img-rogue-umlibs/

Installing the proprietary user space components
------------------------------------------------

The repository has binaries for each platform in release specific branches.
Newer releases will match 1:1 with the kernel module branch name you would have
picked in the :ref:`rogue-building-the-proprietary-kernel-module` stage.

The repository has the following structure:

.. code-block:: text

   .
   ├── LICENSE
   ├── Makefile
   ├── README
   └── targetfs
       ├── am62_linux
       │   └── lws-generic
       │       └── release
       ├── am62p_linux
       │   └── lws-generic
       │       └── release
       ├── j721e_linux
       │   └── lws-generic
       │       └── release
       ├── j721s2_linux
       │   └── lws-generic
       │       └── release
       ├── j722s_linux
       │   └── lws-generic
       │       └── release
       └── j784s4_linux
           └── lws-generic
               └── release

Under the :file:`targetfs` directory there is a subdirectory for each
``PVR_BUILD_DIR`` build variable. Under that directory is a subdirectory
corresponding to the ``WINDOW_SYSTEM`` build variable. Finally, under that
directory is a subdirectory corresponding to the ``BUILD`` build variable.

This is in the :file:`Makefile` as:

.. code-block:: Makefile

   SRCDIR = ./targetfs/${TARGET_PRODUCT}/${WINDOW_SYSTEM}/${BUILD}

The :file:`Makefile` simply unpacks this directory structure and installs the
corresponding files into ``DESTDIR`` in the install step. Do not worry about the
clean step, as this is for development.

.. _rogue-proprietary-mesa-components:

Proprietary mesa components
===========================

Mesa, at this point in time, is a collection of Graphics (GFX) tools and
utilities for setting up and interacting with rendering contexts. It has
everything from a DRI "megadriver" to full GLES/GL implementations. If you're
interested in learning GFX under Linux it is worth familiarizing yourself with
everything else it provides.

For us, the important part is that DRI megadriver. This is the mechanism used to
decide what GLES / GL implementation to pick when you bind one of the earlier
mentioned API to a context. This is also where things get tricky.

Historically there has been some issues with embedded GFX because, unlike your
standard PC GPU, we tend to mix and match actual Graphics Processing Units and
Display Controllers. The megadriver uses the display device name to coordinate
between API implementations. As such, we need a shim to act as a ``tidss`` DRI
driver and coordinate the link with the PVR GLES implementation.

This shim, currently, takes the form of a Gallium Frontend. This is the main
reason for the fork and the 60 odd patches we carry at the following repository:

   https://gitlab.freedesktop.org/StaticRocket/mesa

There are also other nice-to-have features there such as additional pixel
formats, minor fix-ups, and a few performance tweaks Imagination has picked up
over the years. The main reason we need it is for that shim.

Building the proprietary mesa components
----------------------------------------

We recommend following the `Mesa build guide`_ for general options. Currently
the mesa components use a standard interface that allows the use of any
``powervr/*`` branch.

.. note::

   Releases before 1.18 did not use this standard interface. Instead the UM
   binaries include all relevant mesa components for those releases.

The only necessary build options are:

   - ``-Dgallium-drivers=pvr`` -- This is a comma separated list, just make sure
     pvr is present in it.

   - ``-Dgallium-pvr-alias=tidss`` -- This should match the display controller
     you want to bind to. For all K3 devices this is ``tidss``.

   - ``-Dvulkan-drivers=pvr`` -- If using Vulkan

This will produce 2 important files relevant to the shim mechanism we discussed
earlier:

   - :file:`pvr_dri.so` -- Main DRI interface

   - :file:`tidss_dri.so` -- Display controller interface that points back at
     :file:`pvr_dri.so`. This uses the value specified with
     ``-Dgallium-pvr-alias``.

Using the proprietary stack
===========================

Assuming you're using the SDK or you've built and installed the earlier parts
correctly, you should see a message similar to the following in :command:`dmesg`
after the kernel module has loaded:

.. code-block:: dmesg

   [    7.716820] pvrsrvkm: loading out-of-tree module taints kernel.
   [    7.796345] PVR_K:  172: Device: 4e20000000.gpu
   [    7.859807] PVR_K:  172: Read BVNC 36.53.104.796 from HW device registers
   [    7.870809] PVR_K:  172: RGX Device registered BVNC 36.53.104.796 with 1 core in the system
   [    7.881015] [drm] Initialized pvr 24.1.6554834 20170530 for 4e20000000.gpu on minor 0

The BVNC should correspond with the BVNC set in
:file:`build/linux/{PVR_BUILD_DIR}/Makefile` in the kernel module repository. If
the module loads but does not detect the device, make sure your device tree has
defined the node properly. This corresponds to the value of
`SYS_RGX_OF_COMPATIBLE` in the
:file:`services/system/rogue/{platform}/sysinfo.h`.

You should now be able to issue a simple test. The UM repository provides the
:command:`rgx_compute_test` as a simple test that does not depend on the display
or mesa components. You should see the following reported by the kernel module
upon launching that test:

.. code-block:: dmesg

   [  460.674895] PVR_K:  332: RGX Firmware image 'rgx.fw.36.53.104.796' loaded
   [  460.694849] PVR_K:  332: Shader binary image 'rgx.sh.36.53.104.796' loaded

*****************
Open source stack
*****************

The open source driver is currently available for the AXE-1-16M core, but
performance is not up to par with the proprietary driver at the moment.
Performance improvements are on the table, but enabling the core is the main
priority at the moment.

It currently offers experimental Vulkan 1.0 support. In the future it will
provides GL 2.1 through `Zink <https://docs.mesa3d.org/drivers/zink.html>`_.
Please note that Zink support for this driver is not mainline, and it is still
experimental. If you want to follow development check out the `Imagination mesa
fork <https://gitlab.freedesktop.org/imagination/mesa>`_

Open source kernel module
=========================

This is in the upstream `linux
<https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git>`_
repository as of version 6.8. It is in the arm64 ``defconfig`` as a module since
this release as well.

Open source firmware
====================

Firmware is available in `linux-firmware
<https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git>`_
as of tag 20231211.

.. note::

   This a binary, and the firmware itself is still closed source for the moment,
   but this is not the same firmware as the proprietary driver.

Open source mesa components
===========================

The open source stack dramatically reduces the number of moving pieces by
combining the Vulkan implementation with Mesa. This Vulkan implementation is
still marked as experimental, though. Once again, we recommend following the
`Mesa build guide`_ for general options.

The only necessary build options are:

   - ``-Dvulkan-drivers=imagination-experimental`` -- Enable the experimental
     AXE Vulkan driver

   - ``-Dimagination-srv=true`` -- Enable the open control server

   - ``-Dgallium-drivers=zink`` -- Enable GL 2.1 through Zink

Using the open source stack
===========================

After collecting the earlier artifacts you should be able to see the following
message in :command:`dmesg`:

.. code-block:: dmesg

   [    8.489877] powervr fd00000.gpu: [drm] loaded firmware powervr/rogue_33.15.11.3_v1.fw
   [    8.489916] powervr fd00000.gpu: [drm] FW version v1.0 (build 6503725 OS)
   [    8.543073] [drm] Initialized powervr 1.0.0 for fd00000.gpu on minor 1

Once again, if the module loaded but you do not see the device registering, make
sure the device tree node matches the binding provided in the upstream kernel.

At this point you should be able to run a simple test. The tool
:command:`vulkaninfo` from the package ``vulkan-tools`` is useful for printing
information about available Vulkan implementations.

The following will print a brief summary:

.. code-block::

   root@am62xx-evm:~# PVR_I_WANT_A_BROKEN_VULKAN_DRIVER=1 vulkaninfo --summary
   MESA: debug: Found compatible render device '/dev/dri/renderD128'.
   MESA: debug: Found compatible display device '/dev/dri/card0'.
   MESA: error: No hard coded idfwdf program. Returning empty program.
   MESA: error: No hard coded passthrough vertex shader. Returning empty shader.
   MESA: debug: Format VK_FORMAT_X8_D24_UNORM_PACK32(125) not supported
   MESA: debug: Format VK_FORMAT_D16_UNORM_S8_UINT(128) not supported
   MESA: debug: Format VK_FORMAT_D32_SFLOAT_S8_UINT(130) not supported
   MESA: debug: Format VK_FORMAT_X8_D24_UNORM_PACK32(125) not supported
   MESA: debug: Format VK_FORMAT_D16_UNORM_S8_UINT(128) not supported
   MESA: debug: Format VK_FORMAT_D32_SFLOAT_S8_UINT(130) not supported
   ==========
   VULKANINFO
   ==========

   Vulkan Instance Version: 1.3.275


   Instance Extensions: count = 16
   -------------------------------
   VK_EXT_debug_report                    : extension revision 10
   VK_EXT_debug_utils                     : extension revision 2
   VK_EXT_headless_surface                : extension revision 1
   VK_KHR_device_group_creation           : extension revision 1
   VK_KHR_display                         : extension revision 23
   VK_KHR_external_fence_capabilities     : extension revision 1
   VK_KHR_external_memory_capabilities    : extension revision 1
   VK_KHR_external_semaphore_capabilities : extension revision 1
   VK_KHR_get_display_properties2         : extension revision 1
   VK_KHR_get_physical_device_properties2 : extension revision 2
   VK_KHR_get_surface_capabilities2       : extension revision 1
   VK_KHR_portability_enumeration         : extension revision 1
   VK_KHR_surface                         : extension revision 25
   VK_KHR_surface_protected_capabilities  : extension revision 1
   VK_KHR_wayland_surface                 : extension revision 6
   VK_LUNARG_direct_driver_loading        : extension revision 1

   Instance Layers:
   ----------------

   Devices:
   ========
   GPU0:
      apiVersion         = 1.0.296
      driverVersion      = 101068899
      vendorID           = 0x1010
      deviceID           = 0x33011003
      deviceType         = PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU
      deviceName         = PowerVR A-Series AXE-1-16M
   GPU1:
      apiVersion         = 1.3.255
      driverVersion      = 0.0.1
      vendorID           = 0x10005
      deviceID           = 0x0000
      deviceType         = PHYSICAL_DEVICE_TYPE_CPU
      deviceName         = llvmpipe (LLVM 18.1.6, 128 bits)
      driverID           = DRIVER_ID_MESA_LLVMPIPE
      driverName         = llvmpipe
      driverInfo         = Mesa 23.2.1 (git-0e75e7ded3) (LLVM 18.1.6)
      conformanceVersion = 1.3.1.1
      deviceUUID         = 6d657361-3233-2e32-2e31-000000000000
      driverUUID         = 6c6c766d-7069-7065-5555-494400000000

.. _Mesa build guide: https://docs.mesa3d.org/install.html

