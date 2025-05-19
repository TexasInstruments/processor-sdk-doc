###############################
Display sub-system applications
###############################

Display sub-system (DSS) applications are ``omapdrm`` based. These will show the
clone mode, extended mode, overlay window, z-order and alpha blending features.
To show the clone and extended mode, an HDMI display must be present.

These applications require the supported mode information of connected displays
and plane ids. One can get these information by running the :command:`modetest`
application in the filesystem.

.. code-block:: console

   # modetest

********
drmclone
********

This displays the same test pattern on both LCD and HDMI (clone). Overlay
windows are also displayed on LCD. To test clone mode, run the following
command:

.. code-block:: console

   # drmclone -l <lcd_w>x<lcd_h> -p <plane_w>x<plane_h>:<x>+<y> -h <hdmi_w>x<hdmi_h>

For example:

.. code-block:: console

   # drmclone -l 1280x800 -p 320x240:0+0 -h 640x480

We can change position of overlay window by changing x+y values. For example,
240+120 will display this at the center.

***********
drmextended
***********

This displays different test pattern on LCD and HDMI. Overlay windows are also
displayed on LCD. To test extended mode, run the following command:

.. code-block:: console

   # drmextended -l <lcd_w>x<lcd_h> -p <plane_w>x<plane_h>:<x>+<y> -h <hdmi_w>x<hdmi_h>

For example:

.. code-block:: console

   # drmextended -l 1280x800 -p 320x240:0+0 -h 640x480

*********
drmzalpha
*********

This displays alpha blended patters on the given display. To use it the
following parameters are mandatory:

**Z-order**:

It determines, which overlay window is displayed on top of the other.

Range: 0 to 3
   - lowest value for bottom
   - highest value for top

**Alpha Blend**:

It determines transparency level of image as a result of both global alpha and
pre-multiplied alpha value.

Global alpha range: 0 to 255
   - 0 - fully transparent
   - 127 - semi transparent
   - 255 - fully opaque

Pre-multipled alpha value: 0 or 1
   - 0 - source is not pre-multiply with alpha
   - 1 - source is pre-multiply with alpha

To test ``drmzalpha``, run the following command:

.. code-block:: console

   # drmzalpha -s <crtc_w>x<crtc_h> -w <plane1_id>:<z_val>:<glo_alpha>:<pre_mul_alpha> -w <plane2_id>:<z_val>:<glo_alpha>:<pre_mul_alpha>

For example:

.. code-block:: console

   # drmzalpha -s 1280x800 -w 19:1:255:1 -w 20:2:255:1

