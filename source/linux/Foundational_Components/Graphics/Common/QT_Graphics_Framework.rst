..
    This subsection provides details on the QT graphics frameworks

#####################
Qt graphics framework
#####################

Qt is a powerful C++ toolkit for writing cross-platform graphics
applications, enabling a single code base to run predictably and perform
well on Windows and embedded platforms,

Please refer `<https://www.qt.io/>`__ for additional details on Qt.

The PSDK target file system includes the pre-built Qt libraries under
:file:`/usr/lib` and a rich set of Qt demo applications under
:file:`/usr/share/examples`.

*****
Demos
*****

Qt provides demos for the Wayland, Linux framebuffer (LINUXFB), and EGL Full
Screen (EGLFS) backends. By default EGLFS will use the ``eglfs_kms`` backend.

.. code-block:: console

   $ /usr/share/examples/opengl/hellogles3/bin/hellogles3 -platform eglfs
   $ /usr/share/examples/opengl/2dpainting/bin/2dpainting -platform eglfs
   $ /usr/share/examples/opengl/openglwindow/bin/openglwindow -platform eglfs

For more information about the EGLFS platform abstraction and using Qt6 in
embedded applications see:

   - https://doc.qt.io/qt-6/embedded-linux.html

***********************
Qt platform abstraction
***********************

The Qt6 within PSDK is prebuilt with Wayland enabled and therefore wayland-egl
is the default Qt Platform Abstraction (QPA). Therefore all Qt applications
should run on top of Weston. To run Qt application without Weston, the user can
use ``-platform`` option to specify the desired QPA as ``linuxfb`` or ``eglfs``.

.. note::

   The ``fbdev`` interface used by default in the ``linuxfb`` platform is
   deprecated. The platform can use `Dumb-Buffer`_ allocations and required
   components of the new KMS interface while still using the same software
   rendering techniques. See ``QT_QPA_FB_DRM`` in the upstream documentation at:
   https://doc.qt.io/qt-6/embedded-linux.html#linuxfb

   .. _Dumb-Buffer: https://man.archlinux.org/man/drm-memory.7.en#Dumb-Buffers

For example:

.. code-block:: console

   $ /usr/share/examples/opengl/2dpainting/bin/2dpainting -platform eglfs

*********************************************************************
Running Qt applications with the Weston In-Vehicle Infotainment shell
*********************************************************************

To run the Qt application with In-Vehicle Infotainment (IVI) shell, set the
following environment variable, ``QT_WAYLAND_SHELL_INTEGRATION=ivi-shell``.

.. code-block:: console

   $ export QT_WAYLAND_SHELL_INTEGRATION=ivi-shell

