..
    This subsection includes content specific to AM3 Beagle Bone Black board


#########################################
AM3 Beagle Bone Black board configuration
#########################################

AM335x has a HW bug, chapter 3.1.1 in the errata: ``The blue and red color
assignments to the LCD data pins are reversed when operating in RGB888 (24bpp)
mode compared to RGB565 (16bpp) mode.`` Therefore, the applications need to
always use either 24 or 16 Bit Per Pixel (BPP) modes, depending on the display
HW connected to the board. The default pixel format ``XRGB8888`` of the graphics
application backends and drivers within PSDK are not supported with the AM3
Beagle Bone Black Board when it is in 16bpp mode. To enable an appropriate
graphics display, make the following changes at various graphics related
configuration files:

   - :file:`/etc/powervr.ini`: add ``DefaultPixelFormat=RGB565``

   - :file:`/etc/weston.ini`: add ``gbm-format=rgb565`` at section ``[core]``

   - :file:`/etc/profile.d/qt_env.sh`: add ``export
     QT_QPA_EGLFS_INTEGRATION=none``

Another restriction of AM335x-based platform is that the width of display
resolution must be divisible by 32. For example, 1360x768 will not work. The
simple workaround is to specify the display resolution as one of the kernel boot
parameters for non-Weston applications and at :file:`/etc/weston.ini` for Weston
itself.

For example:

   #. The following commands should run at u-boot:

      .. code-block:: text

         => setenv optargs video=HDMI-A-1:1024x768
         => saveenv

   #. Add the ``HDMI-A`` configuration to :file:`/etc/weston.ini` in a new
      ``output`` section, as shown below:

      .. code-block:: ini

         [output]
         name=HDMI-A-1
         mode=1024x768

