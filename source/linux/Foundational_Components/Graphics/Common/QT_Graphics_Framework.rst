..
    This subsection provides details on the QT graphics frameworks

#####################
QT Graphics Framework
#####################

Qt is a powerful C++ toolkit for writing cross-platform graphics
applications, enabling a single code base to run predictably and perform
well on Windows and embedded platforms,

Please refer `<https://www.qt.io/>`_ for additional details on Qt.

The PSDK target file system includes the pre-built Qt libraries under
:file:`/usr/lib` and a rich set of QT demo applications under
:file:`/usr/share/qt5/examples`.

*****
Demos
*****

Demos using the Null Window System / KMS / DRM / EGLFS are
provided with Qt. By default EGLFS will use the ``eglfs_kms`` backend.

.. code-block:: console

   $ /usr/share/qt5/examples/opengl/hellogles3/hellogles3 -platform eglfs
   $ /usr/share/qt5/examples/opengl/2dpainting/2dpainting -platform eglfs
   $ /usr/share/qt5/examples/opengl/paintedwindow/paintedwindow -platform eglfs

The default ``eglfs_kms`` configuration file for Qt5 is located at
:file:`/etc/qt5/eglfs_kms_cfg.json`.

Please note that EGLFS backend is not smart enough to select a display device
automatically. One must be specified in the config file using the ``device``
key. If one is not specified, :file:`/dev/dri/card0` will be used, which can
either point at the GPU or the Display device depending on the order in which
the devices were initialized. We recommend using the :file:`/dev/dri/by-path/*`
path for a persistent device path. If an incorrect device was chosen, an error
like the following can appear: ``Failed to create display device (err=19)``.

For more information about Qt's EGLFS and using Qt5 in embedded
applications see:

   - https://doc.qt.io/qt-5/embedded-linux.html

******
QT QPA
******

The QT5 within PSDK is prebuilt with Wayland enabled and therefore
wayland-egl is the default QPA. Hence all QT applications should be run
on top of Weston. To run QT application without Weston, the user can use
``-platform`` option to specify the desired QPA as ``linuxfb`` or ``eglfs``.

.. note::

   The ``linuxfb`` inteface is deprecated and requires switching the display
   into legacy fb mode.

For example:

.. code-block:: console

   $ /usr/share/qt5/examples/opengl/2dpainting/2dpainting -platform eglfs

*************************************************
Running QT Applications with the Weston IVI shell
*************************************************

To run the QT application with ivi-shell, set the
``QT_WAYLAND_SHELL_INTEGRATION`` environment variable to ivi-shell.

.. code-block:: console

   $ export QT_WAYLAND_SHELL_INTEGRATION=ivi-shell

