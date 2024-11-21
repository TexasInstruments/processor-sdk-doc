..
    This subsection provides details on the migration of the SDK from older
    releases.

#############################
Migration from prior releases
#############################

.. _from-processor-sdk-1-x-to-2-x-for-am3-am4:

******************************************
From Processor SDK 1.x to 2.x for AM3, AM4
******************************************

The SGX driver has been enhanced to support DRM based Full Window
Display in processor SDK 2.0 and the FBdev based Full Window modes are
no longer supported. The System startup and most of the Graphics
applications are backward-compatible except with the following changes.

Window System Libraries
=======================

The FBdev based Full Screen window systems are no longer supported:

   - ``libpvrPVR2D_FRONTWSEGL.so`` (for direct writes to FrameBuffer - FRONT
     mode of operation - directly writes to FrameBuffer without waiting for
     vsync - fastest mode of operation)

   - ``libpvrPVR2D_FLIPWSEGL.so`` (for VSync synchronised writes to Framebuffer
     - slower, but avoids tearing)

   - ``libpvrPVR2D_BLITWSEGL.so`` (for direct writes to back-buffer, which later
     gets written to ``*FrameBuffer`` with sync)

Instead the DRM based Full Screen window system are provided:

   - ``libpvrDRMWSEGL_FRONT.so`` (for direct writes to DRM FrameBuffer - FRONT
     mode of operation - directly writes to FrameBuffer without waiting for
     vsync - fastest mode of operation)

   - ``libpvrDRMWSEGL.so`` (for VSync synchronised writes to DRM Framebuffer -
     slower, but avoids tearing)

The window system is specified by the PVR configuration parameter WindowSystem
at the PVR configuration file :file:`/etc/powervr.ini`. By default, that
parameter is set to ``libpvrDRMWSEGL_FRONT.so`` for nullDRM Front mode. To
configure the PVR SGX to operate in nullDRM FLIP mode, edit the PVR
configuration file to set the parameter WindowSystem to ``libpvrDRMWSEGL.so``.
The change will take effect when any graphic application is launched next time.


Obsolete Test Programs
======================

The following test programs are no longer applicable and removed from
the SDK file system:

   - :file:`/usr/bin/sgx_blit_test`

   - :file:`/usr/bin/sgx_flip_test`

   - :file:`/usr/bin/sgx_render_flip_test`

   - :file:`/usr/bin/sgx_render_test`

.. _from-processor-sdk-2-0-0-to-2-0-x-for-am4:

*****************************************
From Processor SDK 2.0.0 to 2.0.x for AM4
*****************************************

The SGX driver has been enhanced to support DRM/WAYLAND based
Multi-Window Display in processor SDK 2.0.1. The System startup and most
of the Graphics applications are backward-compatible except with the
following changes.

Window System Libraries
=======================

The DRM based Full Screen window systems are no longer supported:

   - ``libpvrDRMWSEGL_FRONT.so`` (for direct writes to DRM FrameBuffer - FRONT
     mode of operation - directly writes to FrameBuffer without waiting for
     vsync - fastest mode of operation)

   - ``libpvrDRMWSEGL.so`` (for VSync synchronised writes to DRM Framebuffer -
     slower, but avoids tearing)

Instead the DRM/WAYLAND based multi-window system are provided:

- ``libpvrws_KMS.so``
- ``libpvrws_WAYLAND.so``

The window system will be dynamically loaded by DDK based on the application use
case, so that the PVR configuration parameter WindowSystem at the PVR
configuration file :file:`/etc/powervr.ini` is no longer used.

.. _from-processor-sdk-2-0-1-to-2-0-x-for-am3-4-5:

**********************************************
From Processor SDK 2.0.1 to 2.0.x for AM3/4/5
**********************************************

The SGX driver has been enhanced to support DRM-based Full
Screen(NullDRM) and Multi-Window(Wayland) Display in processor SDK
2.0.2. The System startup and most of the Graphics applications are
backward-compatible except with the following changes.

Window System Libraries
=======================

The DRM based Full Screen window system is supported:

   - ``libpvrDRMWSEGL.so`` (for VSync synchronised writes to DRM Framebuffer -
     slower, but avoids tearing)

The DRM/WAYLAND based multi-window systems are also provided:

   - ``libpvrGBMWSEGL.so``

   - ``libpvrws_WAYLAND.so``

The window system will be dynamically loaded by DDK based on the
application use case, so that the PVR configuration parameter
WindowSystem at the PVR configuration file /etc/powervr.ini is no longer
required.

.. _from-processor-sdk-3-1-to-3-x-for-am3-4-5:

*****************************************
From Processor SDK 3.1 to 3.x for AM3/4/5
*****************************************

The QT QPA ``eglfs_kms``, which supports multiple screens, has been enabled
and used as the default eglfs platform plugin in processor SDK 3.2. To
fallback to the standard single-screen eglfs plugin, issue the following
instruction at the command line or add the same at the QT environment
configuration file :file:`/etc/profile.d/qt_env.sh`.

.. code-block:: console

   export QT_QPA_EGLFS_INTEGRATION=none

.. _from-processor-sdk-6-1-to-6-2-for-am3-4-5-6:

*******************************************
From Processor SDK 6.1 to 6.2 for AM3/4/5/6
*******************************************

The SGX driver has been enhanced to replace IMG WSEGL with MESA-EGL which
supports the essential EGL 1.5 extensions required by the latest versions
of certain graphics applications such as Chromium browser. The System
startup and most of the Graphics applications are backward-compatible except
with the following changes.

Window System Libraries
=======================

With MESA-EGL, all window system modules are embedded in the libEGL.so, both
GBM(DRM) full-screen and Wayland window systems are supposrted and dynamically
invoked based on the application use case. The following IMG WSEGL libraries are
no longer used and provided:

   - ``libpvrDRMWSEGL.so``

   - ``libpvrGBMWSEGL.so``

   - ``libpvrws_WAYLAND.so``

The QT QPA eglfs raw mode is no longer supported and thus should be replaced
with eglfs_kms by setting the environment variable at the QT environment
configuration file :file:`/etc/profile.d/qt_env.sh`.

.. code-block:: console

   export QT_QPA_EGLFS_INTEGRATION=eglfs_kms
