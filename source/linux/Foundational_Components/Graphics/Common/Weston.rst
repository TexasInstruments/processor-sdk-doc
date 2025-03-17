######
Weston
######

The supported Wayland/Weston version brings in the multiple display support in
extended desktop mode and the ability to drag-and-drop windows from one display
to the other.

Weston has support for multiple backends. By default it will use the ``drm``
backend unless the ``WAYLAND_DISPLAY`` environment variable is set. This backend
will register the compositor as the controller of the kms interface and will
pick up human interface device (HID) input using evdev.

If the ``WAYLAND_DISPLAY`` variable is set, Weston will attempt to use the
``wayland`` backend for nested composition. This is useful for development, but
is normally not what you want for standard composition use. See
:ref:`starting-weston-manually` or `the upstream weston documentation`_ for more
information.

.. ifconfig:: CONFIG_part_variant in ('AM62PX', 'J722S')

   The |__PART_FAMILY_NAME__| group of devices actually utilizes two separate
   DSS modules enumerated under two different :file:`/dev/dri/card*` devices.

   Weston versions newer than ``11.0.91`` can specify additional card devices
   via the ``--additional-devices`` command line parameter when using the
   ``drm`` backend.

   To launch Weston using both card0 and card1, you can use the following
   command:

   .. code-block:: console

      # weston --drm-device=card0 --additional-devices=card1

   You may also modify the weston service to have systemd do this automatically
   on launch by editing :file:`/usr/share/wayland-sessions/weston.desktop` and
   modifying the ``Exec`` line:

   .. code-block:: ini

      [Desktop Entry]
      Exec=weston --drm-device=card0 --additional-devices=card1

   Please note, however, that Weston cannot use by-path identifiers and
   consistent naming of DRI devices is not the default behavior.

***************************
Starting Weston with Emptty
***************************

Starting with SDK 11.0, the preferred way to start Weston is with the ``weston``
user using the display manager ``emptty``. Emptty is a console based display
manager that coordinates the loading of devices with the initialization of any
specified graphical environment. By default, it is configured to automatically
start ``weston`` under the weston user on device startup.

If you need to interact with this instance using any other user then make sure
that user is capable of interacting with the wayland socket :file:`wayland-1`
under the weston user's ``XDG_RUNTIME_DIR``, :file:`/run/user/1000/`. We do not
recommend running graphical applications as root.

To start the systemd service manually, do the following:

.. code-block:: console

   # systemctl start emptty

To inspect the systemd service status, do the following:

.. code-block:: console

   # systemctl status emptty

.. _starting-weston-manually:

************************
Starting Weston Manually
************************

To launch Weston manually with the DRM backend, do the following:

On the default display:

.. code-block:: console

   # weston --display=<default connector-id>

On the secondary display:

.. code-block:: console

   # weston --display=<secondary connector-id>

On all connected displays (LCD and HDMI):

.. code-block:: console

   # weston

By default, the screensaver timeout is configured to 300 seconds. The user can
change the screensaver timeout using a command line option:

.. code-block:: text

   --idle-time=<number of seconds>

For example, to set timeout of 10 minutes and Weston configured to
display on all connectors, use the below command:

.. code-block:: console

   # weston --idle-time=600

To disable the screen timeout and to configure Weston to display on all
connectors, use the below command:

.. code-block:: console

   # weston --idle-time=0

If you face any issues with the above procedure, please refer to `the upstream
weston documentation`_ for troubleshooting tips.

.. _the upstream weston documentation:
   https://wayland.pages.freedesktop.org/weston/toc/running-weston.html

The filesystem comes with a preconfigured :file:`weston.ini` file which will
be located at :file:`/etc/xdg/weston/weston.ini`

.. _stopping-weston:

***************
Stopping Weston
***************

Terminate all Weston clients before exiting Weston. If you have invoked
Weston from the serial console, exit Weston by pressing Ctrl-C.

If Weston was started automatically by the display manager then it can be
stopped with:

.. code-block:: console

   # systemctl stop emptty

It is also possible to invoke Weston from the native console, exit
Weston by pressing Ctrl-Alt-Backspace.

**********************
Running Weston clients
**********************

Weston client examples can run from the command line on a serial port
console or an SSH console. After launching Weston, the user should be
able to use the keyboard and the mouse for various controls.

.. code-block:: console

   # /usr/bin/weston-flower
   # /usr/bin/weston-clickdot
   # /usr/bin/weston-cliptest
   # /usr/bin/weston-dnd
   # /usr/bin/weston-editor
   # /usr/bin/weston-eventdemo
   # /usr/bin/weston-image /usr/share/weston/terminal.png
   # /usr/bin/weston-resizor
   # /usr/bin/weston-simple-egl
   # /usr/bin/weston-simple-shm
   # /usr/bin/weston-simple-touch
   # /usr/bin/weston-smoke
   # /usr/bin/weston-info
   # /usr/bin/weston-terminal

************************************
Running multimedia with Wayland sink
************************************

The GStreamer video sink for Wayland is the waylandsink. To use this
video-sink for video playback:

.. code-block:: console

   # gst-launch-1.0 playbin uri=file://<path-to-file-name> video-sink=waylandsink

***********************
Using IVI shell feature
***********************

The SDK also has support for configuring Weston ivi-shell. The default shell
that is configured in the SDK is the desktop-shell.

To change the shell to ivi-shell, the user will have to add the following lines
into the :file:`/etc/xdg/weston/weston.ini`.

To switch back to the desktop-shell can be done by commenting these lines in the
:file:`/etc/xdg/weston/weston.ini` (comments begin with a '#' at the start of
line).

.. code-block:: ini

   [core]
   shell=ivi-shell.so

After the above configuration is completed, we can restart Weston by
running the following command:

.. code-block:: console

   # systemctl restart emptty

.. note::

   When Weston starts with ivi-shell, the default background is black, this is
   different from the desktop-shell that brings up a window with background.

With ivi-shell configured for Weston, Wayland client applications use
ivi-application protocol to be managed by a central HMI window management.

Applications must support the ``ivi_application`` Wayland protocol to be managed by
the HMI central controller with an unique numeric ID.

Some important references to Weston IVI-shell can be found at the following
link:

   - `<https://wayland.pages.freedesktop.org/weston/toc/ivi-shell.html>`_

