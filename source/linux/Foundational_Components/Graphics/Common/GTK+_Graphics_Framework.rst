..
    This subsection provides details on the GTK+ graphics frameworks

#######################
GTK+ graphics framework
#######################

GTK+, or the GIMP Toolkit, is a multi-platform toolkit for creating graphical
user interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application suites.

See `<https://www.gtk.org/>`_ for additional details on GTK+.

The PSDK target file system includes the pre-built GTK+ libraries under
:file:`/usr/lib` for GTK+3 over Wayland support. There is also a comprehensive
GTK+3 demo application (``gtk3-demo``) under :file:`/usr/bin` to demonstrate GTK+3
APIs and their usages.

*****
Demos
*****

GTK+ will interact with a windowing system on startup. If one is not running, or
it fails to connect to one for any reason, you will see the following error:

.. code-block:: text

   (<application_name>:<pid>): Gtk-WARNING **: 21:21:27.361: cannot open display: <display>

If no display value is present, then you are more than likely missing the
``WAYLAND_DISPLAY`` environment variable. Check the :doc:`Weston` section for
more information.

