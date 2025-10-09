#####################
Android Simple UI App
#####################

As part of 9.0 SDK release, Android SDK has included an pre-built app created
by the company Klaralvdalens Datakonsult AB (KDAB). The app is based on Flutter
and the source code of the app is available at https://github.com/KDAB/cabin-demo.

.. note::
    For more information on this application, please visit the KDAB page at https://www.kdab.com/


**********
Background
**********

The default Google UI consists of several UI layers and performs various
memory intensive operations involving alpha blending, anti-aliasing and
composition. On |__PART_FAMILY_NAME__| device this keeps the GPU and DDR throughput fully
occupied. This Android app has simpler UI animations and few layers that
shows good user experience with Android on |__PART_FAMILY_NAME__| device.

*****************
Launching the app
*****************

* Boot the EVM to default Android UI

* Open the app drawer by swiping up from the bottom

* Click on the demo app to launch the KDAB app


  .. Image:: /images/am62x_android_simple_ui_launcher.png
     :width: 600


***********
Screenshots
***********

  .. Image:: /images/am62x_android_simple_ui_demo.gif
