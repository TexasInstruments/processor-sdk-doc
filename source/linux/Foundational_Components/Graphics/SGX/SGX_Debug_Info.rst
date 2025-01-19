.. http://processors.wiki.ti.com/index.php/SGXDbgInfo

##############
SGX Debug Info
##############

************
Introduction
************

The TI OMAP/AM/DM SGX Graphics Driver is closely tied to the environment it is
running under and the configuration it is built with. This article mentions
debugging methods specific to Linux.

*********************************************
Baselining the current SGX driver environment
*********************************************

The current SGX driver environment on the target can be observed using
the below script:

.. code-block:: sh
   :caption: gfx_check.sh
   :name: gfx-check-sh

   #!/bin/sh
   echo "WSEGL settings"
   cat /etc/powervr.ini
   echo "------"
   echo "ARM CPU information"
   cat /proc/cpuinfo
   echo "------"
   echo "SGX driver information"
   cat /proc/pvr/version
   echo "------"
   echo "Framebuffer settings"
   fbset -i
   echo "------"
   echo "Rotation settings"
   cat /sys/class/graphics/fb0/rotate
   echo "------"
   echo "Kernel Module information"
   lsmod
   echo "------"
   echo "Boot settings"
   cat /proc/cmdline
   echo "------"
   echo "Linux Kernel version"
   uname -a

***********************************************
Run-time checks/configuration of the SGX driver
***********************************************

One can confirm whether the SGX drivers have been properly installed by
checking the following:

   - One should have seen the message on serial console: ``Initializing the
     graphics driver ...`` just before getting the Linux command prompt.

   - The ``lsmod`` command shows ``pvrsrvkm`` module inserted successfully
     without any error messages on console.

The SGX driver can be configured at run-time on the target using a configuration
file.

The optional configuration file is installed by the Processor SDK installer at
:file:`/etc/powervr.ini`.

Configuration items are specified using the below syntax

.. code-block:: text

   KeyWord=ParamValue

Important configuration parameters are mentioned below.


WindowSystem
============

This configuration item controls the low level window system that the EGL
implementation should hook it up. This item takes the below values:

   - ``libpvrDRMWSEGL.so`` (DRM-based WS for VSync synchronised writes to
     Framebuffer - slower, but avoids tearing)

   - ``libpvrGBMWSEGL.so`` (GBM-based WS where it is up to application to
     perform KMS operations)

DisableHWTextureUpload
======================

This configuration item enables/disables the use of SGX Transfer queue hardware.

If set to 1, the driver uses software upload (copying from driver to SGX) of
textures, rather than transfer queue (using the SGX hardware).

Useful to rule out problems in TQ.

DefaultPixelFormat
==================

This configuration item sets the default display pixel format.

If one wants to configure the default pixel format, then edit
:file:`/etc/powervr.ini` to have following line:

.. code-block:: text

   DefaultPixelFormat=ARGB8888

For AM3 Beagle Bone Black EVM:

.. code-block:: text

   DefaultPixelFormat=RGB565

***************************************
SGX Driver Failure Modes (Installation)
***************************************

Unable to install the kernel modules (pvrsrvkm.ko)
==================================================

1. The Linux kernel has to be built with "modules" support.

2. The kernel module for the Graphics driver have to be built against a version
   of the kernel that will be run on the target.

3. If the services kernel module (``pvrsrvkm.ko``) does not load, it is likely
   because of mismatches between user mode binaries and kernel module. If the
   kernel module is built correctly, post the issue on the E2E forum with the
   output of the :ref:`gfx-check-sh` script.

***********************************
SGX Driver Failure Modes (Run time)
***********************************

Vertical Tearing / Artifacts / Clipping issues / Missing objects
================================================================

This could be due to an incorrect usage of OpenGL or an issue in the driver.
Note that the deferred rendering mode of the SGX hardware will cause different
behaviour compared to the immediate renderers found on desktops.

Please contact TI through the Linux `E2E forums`_.

Demos are not running at required speed, How to check SGX clock rate?
=====================================================================

If the demos are running slower than expected, check and ensure that the clock
frequency set for the SGX driver is correct. This can be done using the
following code in the KM kernel driver:

| File - :file:`eurasia_km/services4/system/omap/sysutils_linux.c`
| Function - ``EnableSGXClocks()``

You can print the SGX clock rate in a debug build as below:

.. code-block:: c

   IMG_UINT32 rate = clk_get_rate(psSysSpecData->psSGX_FCK);
   PVR_TRACE(("Sgx clock is %dMHz", HZ_TO_MHZ(rate)));

Depending on the TI platform used, this will vary from 200 to 532 MHz. Ensure
that SGX is running at the right clock.

If the clock values are correct and demos are still not running with expected
performance, then application specific optimization will be required.

Qt demos do not work when PowerVR is enabled
============================================

1. Confirm that the GLES2 demos provided in the Graphics SDK are running
   properly with default SDK configuration of the window system.

2. Confirm that kernel module ``pvrsrvkm.ko`` is successfully loaded.

3. Confirm that the alpha value is non-zero using the ``fbset`` command. If not,
   set it to the appropriate value using ``fbset``. QT supports 16 and 32 bpp,
   but it expects a non-zero alpha value when using 32 bpp.

If above has been confirmed and there are still issues, post to E2E forum with
the output of the :ref:`gfx-check-sh` script. Also attach the console log, with
the below environment variable set:

.. code-block:: console

   QT_DEBUG_PLUGINS=1

********************
Posting to E2E forum
********************

For suggestions or recommendations or bug reports, post details of your
application as below to the `E2E forums`_, with below
information:

   - Output of GFX environment baseline script :ref:`gfx-check-sh`.

   - Details of UI application, as shown in below sheet:

      `<https://web.archive.org/web/20170909142430if_/https://gforge.ti.com/gf/download/docmanfileversion/220/3798/UI_graphics_reqs_sheet_v1.xls>`_

These two outputs will help in debugging common issues.

.. _E2E forums: https://e2e.ti.com/
