.. _TI-Apps-Launcher-User-Guide-label:

TI Apps Launcher - User Guide
=============================

Overview
--------

TI Apps Launcher is a QT Based Application launcher for TI Platforms. Currently, TI Apps Launcher incorporates following applications across all supported platforms,

- Industrial HMI

- Live Camera

- Benchmarks

- GPU Performance

- Seva Store

- Chromium

- Settings

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   Additionally, The below demos are also available on the |__PART_FAMILY_DEVICE_NAMES__| platform specifically:

   - ARM Analytics

   - 3D Demo

All of the necessary equipment requirement and instructions are provided here.

.. note::

   Not all of the above set of applications are supported by each platform. So there will be differences between each.

Hardware Prerequisites
----------------------

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   -  TI AM62x SK / TI AM62x-LP SK / TI AM62xSIP SK / BeaglePlay

.. ifconfig:: CONFIG_part_variant in ('J721S2','J784S4','J722S')

   -  TI |__PART_FAMILY_DEVICE_NAMES__| SK

-  PC (Windows or Linux, to use serial terminal console)

-  HDMI Monitor (to view the Demo on Display)

-  Ethernet Cable (to connect |__PART_FAMILY_DEVICE_NAMES__| SK to internet)

-  USB Camera or OV5640 camera sensor module (for Live Camera)

-  Keyboard & Mouse (to control the TI Apps Launcher)

-  SD card (minimum 16GB)

Launching and Using the TI Apps Launcher
----------------------------------------

The TI Apps Launcher launches on Linux startup. Follow the below instructions to use it.

1. Flash an SD card with the :file:`tisdk-default-image`. User can download the :file:`tisdk-default-image` wic image from |__SDK_DOWNLOAD_URL__|. Please follow the instructions from here to :ref:`Flash an SD card <processor-sdk-linux-create-sd-card>`.

.. note::

   Images may vary between each platform based on the number of supported applications.

2. Insert the flashed SD card to the board, connect the display, mouse, ethernet cable, keyboard and power on the SK-EVM. The TI Apps Launcher will launch automatically when the device is fully booted.

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. Image:: /images/ti-apps-launcher-home-am62x.png
      :height: 400

   .. note::

     TI-Apps-Launcher on AM62SIP is minimal due to it's memory constraints. This experience on AM62SIP looks like the following.


     .. Image:: /images/ti-apps-launcher-home-am62sip.jpg
        :height: 400

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. Image:: /images/ti-apps-launcher-home-am62px.png
      :height: 400

   |

.. ifconfig:: CONFIG_sdk in ('j7_foundational')

   .. Image:: /images/ti-apps-launcher-j7.png
      :height: 400

Launching the Industrial HMI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. note::

      Industrial HMI on AM62xSIP SK varies from the one documented here. This is only valid for AM62x SK, AM62x-LP SK and BeaglePlay.

1. To launch the Industrial HMI demo, click on the `Industrial HMI` button on the left menu.

.. ifconfig:: CONFIG_sdk in ('SITARA')

   .. Image:: /images/ti-apps-launcher-hmi.png
      :height: 400

.. ifconfig:: CONFIG_sdk in ('j7_foundational')

   .. Image:: /images/hmi-demo-j7.png
      :height: 400

2. You can click on the Auto-Manual slider button to switch modes.

3. In Manual mode, you can use the **^** and **v** buttons of each motor to control the RPM.


Launching the Camera App
^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X')


    1. Ensure you have enabled the camera sensors which you have connected to SK-EVM. Refer :ref:`this <enabling-camera-sensors>` to know the list of camera modules supported and how to enable the sensor overlays for them.

    2. To launch the Live Camera demo, click on the `Live Camera` button on the left panel.

    .. ifconfig:: CONFIG_sdk in ('SITARA')

       .. Image:: /images/live-camera-button.jpg
          :height: 400

    .. note:: It takes around 3-5 seconds for Live Camera to start.

    3. The Live Camera demo starts streaming the output of the camera connected in the centre window of TI Apps Launcher. The image below is captured using USB Camera.

    .. ifconfig:: CONFIG_sdk in ('SITARA')

       .. Image:: /images/live-camera.png
          :height: 400

    .. ifconfig:: CONFIG_sdk in ('j7_foundational')

       .. Image:: /images/live-camera-j7.png
          :height: 400


.. ifconfig:: CONFIG_part_variant not in ('AM62X')

    1. |__PART_FAMILY_DEVICE_NAMES__| has hardware codecs which are capable of encoding and decoding H.246 and H.265 Videos.

    2. The Camera app supports recording and playback of video in H264 and H265 formats.

    3. Click on the 'Camera' button on the left menu to start the app.

    .. Image:: /images/ti-apps-launcher-camera-button.png
       :height: 400

    4. If a camera is detected, it will start previewing by default.

    5. By default, the Codec chosen for recording and playback is H264. If you want to use H265 instead, just toggle the switch on the bottom left corner.

    .. Image:: /images/ti-apps-launcher-camera-codecswitch.png
       :height: 400

    6. If there are multiple cameras connected, you can switch between them by selecting the preferred camera from Cameras Dropdown.

    7. Once a camera is selected and the preview is visible, you can start recording by clicking on the Record/Stop button right next to the Cameras Dropdown. The Camera preview will still be available while recording.

    8. The status message on the top right will display the filename into which the video is being recorded.

    .. Image:: /images/ti-apps-launcher-camera-recording.png
       :height: 400

    9. Press the Record/Stop button again to Stop Recording.

    10. To play the recorded videos, Select a video file from the Gallery Dropdown, and click Play Button. The info about the file being played will be displayed on the top left corner.

    .. Image:: /images/ti-apps-launcher-camera-gallery-dropdown.png
       :height: 400

    .. Image:: /images/ti-apps-launcher-camera-playback.png
       :height: 400

    11. This player can be used to play any .h264, .h265 and .mp4 (h264 and h265 only) files. To test with other files instead of recorded videos, copy the test files to ``/opt/ti-apps-launcher/gallery/``.

    .. note::

         The Gallery Dropdown filters files based on the name of the file. So the filename must have "h264" or "h265" as substring.

    12. To delete the recorded files, after selecting the file from Dropdown, click Delete Button next to the Play Button.


Launching the ARM Analytics Demo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX')

    .. note::

       ARM Analytics Demo is only supported on AM62x SK, AM62x-LP SK, AM62PX and BeaglePlay. AM62SIP doesn't support it.

    1. This app tries to showcase the ARM optimized models for Object Detection, Face Detection and Image Classification.

    2. To launch the ARM Analytics demo, click on the `ARM Analytics` button on the left panel.

    .. Image:: /images/ti-apps-launcher-arm-analytics.png
       :height: 400

    3. By default, the ARM Analytics demo shows the results of **Object Detection** Model on existing data.

    4. To test **Face Detection** or **Image Classification**, Click on the respective buttons available at the bottom of the main window.

.. ifconfig:: CONFIG_part_variant not in ('AM62X', 'AM62PX')

   .. note::

      This section is not valid for this platform.


Launching the Benchmarks Demo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. note::

      Benchmarks Demo is not supported on AM62xSIP because it depends on weston-terminal. AM62xSIP uses EGLFS to run the ti-apps-launcher.

1. The Benchmarks Demo includes various System Benchmarks like dhrystone, linpack, nbench, etc. and GPU benchmarks like glmark2.

2. Click on the `Benchmarks` button on the left panel.

.. ifconfig:: CONFIG_sdk in ('SITARA')

   3. User will now see the list of Benchmarks available to test on SK-EVM. Click on the `play button` infront of the benchmark you like to test. The image below is captured while running the `glmark2`.

   .. Image:: /images/ti-apps-launcher-benchmarks-glmark2.png
      :height: 400

   4. Once after the entire benchmark has been run, the FPS & Score will get populated in the table.

.. ifconfig:: CONFIG_sdk in ('j7_foundational')

   3. User will now see the list of Benchmarks available to test on TI |__PART_FAMILY_DEVICE_NAMES__|. Click on the `play button` infront of the benchmark you like to test. The image below is captured while running the `dhrystone`.

   .. Image:: /images/benchmarks-system.png
      :height: 400


Launching the GPU Performance Demo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   .. note::

      GPU Performance Demo is not supported on AM62xSIP because it depends on weston or requires the ownership of EGLFS context.

1. The GPU Performance demo allows users to vary the GPU loads using glmark2. Click on the `GPU Performance` button on the left panel.

2. Now you can choose the GPU Load Level from the buttons available on the right. Choose from '0' which is no load to '4' max load.

.. ifconfig:: CONFIG_sdk in ('SITARA')

   .. Image:: /images/ti-apps-launcher-gpu-performance.png
      :height: 400
   
   3. You will see the updated values of FPS & Score metrices getting populated in the table.
   
.. ifconfig:: CONFIG_sdk in ('j7_foundational')

   3. The image below is captured while running the `glmark2` with **GPU Load Level as 3**.

   .. Image:: /images/gpu-benchmarks-textures.png
      :height: 400

   4. You will see the updated values of FPS & Score metrices getting populated in the table.

Launching the Seva Store
^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX')

   .. note::

      Seva Store is not supported on AM62xSIP due to it's memory constraints.

1. |__SDK_FULL_NAME__| now supports Seva Store. Seva Store is a TI developed demo gallery which allows users to download and install demos on the go. Developers can host their demos as Docker Images on any public Docker Registry and link them to Seva Design Gallery. 

2. Refer :ref:`Seva Store - User Guide <Seva-Store-label>` to know more about Seva Store.

.. ifconfig:: CONFIG_sdk in ('j7_foundational')

   .. Image:: /images/seva-store.png
      :height: 400

Launching the Chromium Browser
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX')

   .. note::

      Chromium Browser is not supported on AM62xSIP due to it's memory constraints.

1. |__SDK_FULL_NAME__| now supports GPU Accelarated Chromium Browser. Click on the Chromium button on the left panel.
  
2. Click Launch button to launch the Chromium Browser. The Browser launches with `WebGL Aquarium <https://webglsamples.org/aquarium/aquarium.html>`__ as the first tab by default.

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      .. Image:: /images/chromium-browser-am62x.png
         :height: 400   

   .. ifconfig:: CONFIG_part_variant in ('AM62PX')

      .. Image:: /images/chromium-browser-am62p.png
         :height: 400

3. Refer :ref:`Chromium_Browser-label` to know more about Chromium Browser.

Launching the 3D Demo
^^^^^^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX')

   .. note::

      3D Demo requires weston to be running or EGLFS context to run. ti-apps-launcher is run on EGLFS so it is not supported on AM62xSIP.

   1. Click on the `3D Demo` button on the left panel.

   2. Click `Launch` button to launch the 3D Demo by Imagination. By default, you would see the Skinning Model running on the screen.

   .. Image:: /images/ti-apps-launcher-3d-demo.png
      :height: 400

   3. You can use mouse buttons or spacebar to pause the 3D Demo and press `ESC` to exit & go back to TI Apps Launcher.

.. ifconfig:: CONFIG_part_variant not in ('AM62X', 'AM62PX')

   .. note::

      This section is not valid for this platform.

Using the Settings Button
^^^^^^^^^^^^^^^^^^^^^^^^^

1. The Settings button on the left panel can be used to set docker's systemd-proxy and system proxy if your SK-EVM is connected to a VPN.

2. Once the user clicks on the Settings button, it will ask for a HTTPS Proxy and No proxy values.

.. Image:: /images/ti-apps-launcher-settings.png
   :height: 400

3. Once you enter the necessary values for both HTTPS and No proxy, click on `Set Proxy` to set the proxy configuration.


Using terminal
^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_sdk in ('SITARA')

   The terminal button on the left panel can be used to open a terminal application, which is
   based on QMLtermwidget.

   .. Image:: /images/terminal.png
      :height: 400

.. ifconfig:: CONFIG_sdk not in ('SITARA')

   This section is not applicable for this platform.

Using Wi-Fi Demo
^^^^^^^^^^^^^^^^

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX')

   1. The *Wifi* button on the left panel allows you to connect to an external Wi-Fi network.
   2. Ensure the required overlay is applied and the M.2 Wi-Fi card is connected to SK-EVM. For more
      information, refer to :ref:`enable_m2cc3301`.
   3. Click the toggle button to turn on Wi-Fi.

   .. Image:: /images/wifi_home.png
      :height: 400

   4. Click on the *Refresh* button to scan for available SSIDs.
   5. Select an SSID from the list, then enter the passphrase and Wi-Fi security type.
   6. For certain security types, you may need to provide additional details.
   7. After entering all the required info, click on *Connect*.

   .. Image:: /images/wifi_ssid.png
      :height: 400

   8. If the all entered details are correct, device will be connected to the selected Wi-Fi
      network. If needed, click *Disconnect* to disconnect from the network and return to
      SSID selection menu.

   .. Image:: /images/wifi_connected.png
      :height: 400

   .. ifconfig:: CONFIG_part_variant in ('AM62X')

      .. note::

         This section is not applicable for AM62xLP and AM62xSIP.

.. ifconfig:: CONFIG_part_variant not in ('AM62X', 'AM62PX')

   This section is not applicable for this platform.


Power Menu
^^^^^^^^^^

1. The top right corner of the TI Apps Launcher is dedicated for the Power Menu.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX')

    2. The Power Menu supports Shutdown, Reboot, Suspend to RAM (For Linux only) and Exit (from TI Apps Launcher) functions.

    .. Image:: /images/ti-apps-launcher-powermenu1.png
       :height: 400

.. ifconfig:: CONFIG_part_variant not in ('AM62X', 'AM62PX')

    2. The Power Menu supports Shutdown, Reboot and Exit (from TI Apps Launcher) functions.

    .. Image:: /images/ti-apps-launcher-powermenu2.png
       :height: 400

Compiling TI Apps Launcher
--------------------------

The ideal way to compile TI Apps Launcher is to trigger a Yocto
build. But for a quicker way to do it, especially during development,
TI provides a `debian-arm64
<https://github.com/TexasInstruments/ti-docker-images/pkgs/container/debian-arm64>`__
Docker image. This image already has all dependencies required
for compiling ti-apps-launcher.

First, clone TI Apps Launcher on host:

.. code:: console

   git clone https://github.com/texasinstruments/ti-apps-launcher.git
   export TI_APPS_LAUNCHER_REPO="$(pwd)/ti-apps-launcher"
   cd ti-apps-launcher

Then, add the following line in :file:`CMakeLists.txt`:

.. code:: console

   add_compile_definitions(SOC_AM62=1) # if target is AM62x or AM62SIP
   add_compile_definitions(SOC_AM62_LP=1) # if target is AM62x-LP
   add_compile_definitions(SOC_AM62P=1) # if target is AM62P

Then, pull TI's debian-arm64 Docker image and run it:

.. code:: console

   docker pull ghcr.io/texasinstruments/debian-arm64:latest
   docker run -it -v ${TI_APPS_LAUNCHER_REPO}:/root/ti-apps-launcher ghcr.io/texasinstruments/debian-arm64 bash

Finally, run:

.. code:: console

   cmake -B build -S . -DRT_BUILD=0 # if target is RT image, make -DRT_BUILD=1
   make -C build

The compiled binary should be :file:`build/ti-apps-launcher`.

Copy the compiled binary to :file:`/usr/bin/` directory of the target:

.. code:: console

   scp ${TI_APPS_LAUNCHER_REPO}/build/ti-apps-launcher root@<ip-addr-of-device>:/usr/bin

If you have modified the scripts in the :file:`scripts/` directory, then copy them too:

.. code:: console

   scp -r ${TI_APPS_LAUNCHER_REPO}/scripts root@<ip-addr-of-device>:/opt/ti-apps-launcher

.. note::

   This is a quick and easy way to compile ti-apps-launcher during
   development, but it is a good idea to validate with Yocto builds
   often. There is a possibility that compiler mismatch could present
   issues in the run up to production.
