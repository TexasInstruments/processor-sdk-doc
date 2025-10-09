###########################
Android Dual Screen Support
###########################

This application note contains steps to enable dual screen with Android in mirror mode or extended mode.

The following panel is currently supported with the |__PART_FAMILY_NAME__| SK EVM revision E3 board:

- **Microtips Technology USA (13-101HIEB0HF0-S) 10.1"  WUXGA (1920x1200) TFT LCD panel**

.. note::

   By default Android configures the displays in mirror mode.

*******************************************************************
How to enable Microtips LVDS panel on |__PART_FAMILY_NAME__| SK EVM
*******************************************************************

**Steps to enable OLDI Panel DT overlay:**

#. Follow the :ref:`android-dtbo` guide.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   **Steps to enable touch on the Microtips Panel on AM625 SK EVM:**

   **Note**: The following steps are only applicable on AM625 SK EVM revision E3 board.

   #. Power off the LVDS board by disconnecting the 12V barrel jack (do not power off the SK EVM)
   #. Run the following commands from the Linux prompt:

      .. code-block:: console

         console:/ $ su
         console:/ # rmmod ili210x
         console:/ # i2ctransfer -f -y 0 w3@0x3f 0x09 0x1 0x0e
         console:/ # i2ctransfer -f -y 0 w6@0x3f 0x08 0x04 0x47 0x50 0x73 0x68

   #. Power on the LVDS board
   #. Run the following command:

      .. code-block:: console

         console:/ # insmod /vendor/lib/modules/ili210x.ko

   After re-initializing the module, the touch IC should now be registered as an input and touch should be functional.

   .. attention::

      This step need to be done each time the board reboots.

*****************************************
How to enable Extended Display in Android
*****************************************

**Step to setup an android build environment:**

#. Follow the :ref:`android-download-aosp` download guide.

**Step to enable Extended Display:**

#. Edit :file:`device.mk` file to add this:

   .. code-block:: makefile

      # Display settings (windowing, system decorations, IME ...)
      PRODUCT_COPY_FILES += \
         device/ti/am62x/display_settings.xml:$(TARGET_COPY_OUT_VENDOR)/etc/display_settings.xml

      # Enable activities on secondary displays
      PRODUCT_COPY_FILES += \
         frameworks/native/data/etc/android.software.activities_on_secondary_displays.xml:system/etc/permissions/android.software.activities_on_secondary_displays.xml

#. Rebuild Android:
   Relaunch command from :ref:`android-build-aosp` build guide.

#. Follow :ref:`android-flashing` guide to flash Android images.
