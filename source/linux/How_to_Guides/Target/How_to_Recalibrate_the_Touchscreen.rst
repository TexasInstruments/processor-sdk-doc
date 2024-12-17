.. http://processors.wiki.ti.com/index.php/How_to_Recalibrate_the_Touchscreen

How to Recalibrate the Touchscreen
===================================

.. rubric:: Non-Weston based Graphic System
   :name: non-weston-based-graphic-system

.. rubric:: Where is the pointercal file?
   :name: where-is-the-pointercal-file

The Processor SDK Linux moves the calibration file for the touchscreen
from the default location of /etc/pointercal to instead be placed at
/run/media/mmcblk0p1/pointercal if the SD device is present. This was
done to allow user's to easily delete this file and force a
recalibration without requiring a Linux PC to mount the file system or a
serial console to access the device. In this case the pointercal file is
now written to a FAT partition of the SD card, which can be mounted on
both Windows or Linux.

If the pointercal file is created at /run/media/mmcblk0p1/pointercal,
and there is not already a file in /etc/pointercal then the file is also
copied to the old default location. This is to prevent requiring the
export of the TSLIB\_CALIBFILE variable as described in later sections
of this document.

In the case that there is no SD card available then the pointercal file
will be written to the default /etc/pointercal location.

.. rubric:: Recalibrating by Deleting pointercal
   :name: recalibrating-by-deleting-pointercal

Because the pointercal file is now written to the FAT partition of the
SD card recalibrating the touchscreen can be done by simply inserting
the SD card into a PC and deleting the pointercal file found on the
first partition (assuming the first partition is a FAT partition). When
the system is then rebooted you will be asked to calibrate the
touchscreen.

.. rubric:: Recalibrating over Serial Console
   :name: recalibrating-over-serial-console

If you do have access to the serial console you can always recalibrate
the touchscreen using the **ts\_calibrate** command as normal. However,
in this case if you already have a pointercal file on the SD card you
will need to export the **TSLIB\_CALIBFILE** variable to point to that
location before you run **ts\_calibrate**. i.e.

.. code-block:: console

   root@<machine>:~# export TSLIB_CALIBFILE=/run/media/mmcblk0p1/pointercal
   root@<machine>:~# ts_calibrate

**NOTE:** If you have Matrix or any other GUI application already
running you should stop that application (`How to Stop
Matrix <../../Examples_and_Demos_Matrix_User_Guide.html>`__)
before running **ts\_calibrate** so that you can see the calibration
screen.

.. rubric:: Exporting TSLIB\_CALIBFILE
   :name: exporting-tslib_calibfile

The environment variable TSLIB\_CALIBFILE is used by the *tslib* package
to indicate the location of the pointercal file. The default value for
TSLIB\_CALIBFILE is /etc/pointercal. If you are writing a program that
uses *tslib* you should make sure that you export TSLIB\_CALIBFILE to
point to the location of your pointercal file (as indicated in the
previous section), or that you place a copy of the pointercal file at
the default /etc/pointercal location.

.. rubric:: Weston based Graphic System
   :name: weston-based-graphic-system

.. rubric:: Where is the ws-calibrate.rules file?
   :name: where-is-the-ws-calibrate.rules-file

The Processor SDK Linux moves the Weston calibration file for the
touchscreen from the default location of
/etc/udev/rules.d/ws-calibrate.rules to instead be placed at
/run/media/mmcblk0p1/ws-calibrate.rules if the SD device is present.
This was done to allow user's to easily delete this file and force a
recalibration without requiring a Linux PC to mount the file system or a
serial console to access the device. In this case the ws-calibrate.rules
file is now written to a FAT partition of the SD card, which can be
mounted on both Windows or Linux.

If the ws-calibrate.rules file is created at
/run/media/mmcblk0p1/ws-calibrate.rules, and there is not already a file
in /etc/udev/rules.d/ws-calibrate.rules then the file is also copied to
the old default location.

In the case that there is no SD card available then the
ws-calibrate.rules file will be written to the default
/etc/udev/rules.d/ws-calibrate.rules.

.. rubric:: Recalibrating by Deleting ws-calibrate.rules
   :name: recalibrating-by-deleting-ws-calibrate.rules

To trigger touchscreen re-calibration, both ws-calbration.rules files
need to be deleted. The ws-calbration.rules file which is now written to
the FAT partition of the SD card can be deleted by simply inserting the
SD card into a PC and deleting the ws-calbration.rules file found on the
first partition (assuming the first partition is a FAT partition) and we
also need to delete /etc/udev/rules.d/ws-calibrate.rules from the
filesystem. After both ws-calibration.rules files are removed, you will
be asked to calibrate the touchscreen when the Weston is launched at the
first time or relaunched by issuing "/etc/init.d/weston start" command
at the console.

Alternatively, you may delete the above listed files directly from the
EVM's console by issuing the following commands at EVM's Linux prompt,
and reboot the EVM to allow recalibration of the LCD.

.. code-block:: console

   root@<machine>:~# rm /etc/udev/rules.d/ws-calibrate.rules
   root@<machine>:~# rm /run/media/mmcblk0p1/ws-calibrate.rules
   root@<machine>:~# reboot

