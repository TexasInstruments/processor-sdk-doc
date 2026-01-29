AM69 SK Hardware Setup
====================================================

AM69 SK
--------------------------

AM69 SK is a low cost, small form factor board designed
to bring smart cameras, robots and intelligent machines to life.
For more information related to the board, full list of peripherals supported,
pin settings for boot modes and more
visit AM69 SK `User guide <https://www.ti.com/lit/pdf/spruj70>`__

To run the demos on AM69 SK you will require,

    - AM69 SK
    - Minimum 16GB high performance SD card
    - External Power Supply or Power Accessory Requirements
    - USB 2.0 mouse
    - Full-HD (1080p) HDMI display
    - Optional 100Base-T Ethernet cable connected to internet
    - Optional UART cable
    - Optional USB camera (Any V4L2 compliant 1MP/2MP camera, Eg. Logitech C270/C920/C922)

        a. Nominal Output Voltage: 5-20VDC
        b. Maximum Output Current: 5000 mA
        c. Refer to AM69 SK `User guide <https://www.ti.com/lit/pdf/spruj70>`__
           for more details.

Connect the components to the EVM as shown in the image.

.. figure:: /images/AM69_SK_Hardware_Setup/am69_sk.jpg
   :scale: 30
   :align: center

   AM69 SK connections

Set the boot pins to SD boot mode as shown in the following image.

.. figure:: /images/AM69_SK_Hardware_Setup/am69_sk_bootpins.jpg
   :scale: 20
   :align: center

   AM69 SK boot pins

.. _pub_edgeai_usb_camera:

USB Camera
----------

UVC (USB video class) compliant USB cameras are supported by AM69 SK.
The driver for the same is enabled in SDK. The SDK has been tested with
C270/C920/C922 versions of Logitech USB cameras. Streaming from multiple USB cameras
simultaneously is also supported.
