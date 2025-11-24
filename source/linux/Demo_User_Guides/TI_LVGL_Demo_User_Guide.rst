.. _TI-LVGL-Demo-User-Guide-label:

#########################
TI LVGL Demo - User Guide
#########################

********
Overview
********

TI LVGL Demo is a simple app that showcases the capabilities of the `LVGL - Light and Versatile Graphics Library <https://lvgl.io/>`__.
It includes various demo applications, such as:

- EV Charging

- Arm analytics

- Smart Home

- Smart Meter

- Thermostat

- Security

.. note::

   Platform compatibility varies for different demo applications. Please see the platform compatibility table below:

   .. list-table:: Demo Compatibility by Platform
      :header-rows: 1
      :widths: 20 16 16 16 16 16 16

      * - Platform
        - EV Charging
        - Arm analytics
        - Smart Home
        - Smart Meter
        - Thermostat
        - Security
      * - AM62L
        - ✓
        - ✗
        - ✓
        - ✓
        - ✓
        - ✓
      * - AM62x
        - ✓
        - ✗
        - ✓
        - ✓
        - ✓
        - ✓
      * - AM62P
        - ✓
        - ✗
        - ✓
        - ✓
        - ✓
        - ✓
      * - AM335X
        - ✗
        - ✓
        - ✓
        - ✓
        - ✓
        - ✗
      * - AM437X
        - ✗
        - ✓
        - ✓
        - ✓
        - ✓
        - ✗
      * - AM65X
        - ✗
        - ✓
        - ✓
        - ✓
        - ✓
        - ✗

All necessary equipment and step by step instructions are provided below:

.. note::

   Some of the features within each of these applications are not supported on all platforms. So there will be differences in feature
   enablement across platforms.

**********************
Hardware Prerequisites
**********************

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   -  AM62L Evaluation Module: `TMDS62LEVM <https://www.ti.com/tool/TMDS62LEVM>`__

.. ifconfig:: CONFIG_part_variant in ('AM62X')

   -  TI AM62x SK / TI AM62x-LP SK / TI AM62xSIP SK / BeaglePlay `SK-AM62 <https://www.ti.com/tool/SK-AM62>`__

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   -  TI SK-AM62P-LP `TMDS62LEVM <https://www.ti.com/tool/SK-AM62P-LP>`__

.. ifconfig:: CONFIG_part_variant in ('AM335X')

   -  AM335x Evaluation Module: AM335x EVM  or `BEAGL-BONE-GRN-ECO <https://www.ti.com/tool/BEAGL-BONE-GRN-ECO>`__
   -  BeagleBone Black `BEAGL-BONE-BLACK <https://www.ti.com/tool/BEAGL-BONE-BLACK>`__

.. ifconfig:: CONFIG_part_variant in ('AM437X')

   -  AM437x Evaluation Module: AM437x GP EVM `TMDSEVM437X <https://www.ti.com/tool/TMDSEVM437X>`__

.. ifconfig:: CONFIG_part_variant in ('AM65X')

   -  AM65x Evaluation Module: AM654x GP EVM `TMDX654IDKEVM <https://www.ti.com/tool/TMDX654IDKEVM>`__

-  PC (Windows or Linux, to use serial terminal console)

-  HDMI/DSI Display (to view the Demo on Display)

-  Ethernet Cable or CC33xx WiFi module (to connect EVM to internet)

-  Mouse or Touch Input from HDMI monitor (to control the TI LVGL Demo)

-  SD card (minimum 16GB)

-  Aux cable connected to earphone/speaker

.. ifconfig:: CONFIG_part_variant in ('AM62LX')

   -  Jumper cable (to connect potentiometer to ADC input) or some analog signal connected to ADC input. In the J11 header, pin D7 (A01)
      is the potentiometer out, which needs to be connected to pin D6 (A02) ADC in for channel 0. (Reference schematics can be found in `AM62L schematics <https://www.ti.com/lit/zip/SPRCAL6>`__)

      .. Image:: /images/ti-lvgl-demo-tmds62levm-potentiometer-connection.png
         :height: 300


**************************
Launching the TI LVGL Demo
**************************

.. ifconfig:: CONFIG_sdk in ('SITARA')

   The demo will auto launch upon Linux booting on the EVM. Follow the below instructions to flash the SD card:

   #. Flash an SD card with the :file:`tisdk-default-image`. User can download the :file:`tisdk-default-image` wic image from |__SDK_DOWNLOAD_URL__|.
      Please follow the instructions from here to :ref:`Flash an SD card <processor-sdk-linux-create-sd-card>`.

   #. Insert the flashed SD card to the board, connect the display, mouse/touch-input, ethernet cable, aux cable, jumper wire and power on the EVM.
      The TI LVGL Demo will launch automatically when the device is fully booted.

.. ifconfig:: CONFIG_sdk in ('DebianSDK')

   Upon booting the EVM, Weston is launched automatically. To launch the LVGL demo, refer the following
   instructions:

   #. Flash an SD card with the :file:`tisdk-debian-trixie` wic image. User can download the wic image from |__SDK_DOWNLOAD_URL__|.
      Please follow the instructions from here to :ref:`Flash an SD card <processor-sdk-debian-create-sd-card>`.

   #. Insert the flashed SD card to the board, connect the display, mouse/touch-input, ethernet cable, aux cable, jumper wire and power the EVM on.

   #. Weston is launched on boot. Shut it down with `systemctl stop weston`.

   #. Launch the demo by typing `/usr/bin/lvglsim` into the UART command prompt.


**********************
Using the TI LVGL Demo
**********************

   The landing/home page of the LVGL demo looks like the following:

   .. ifconfig:: CONFIG_part_variant in ('AM335X' 'AM437X' 'AM65X')

      .. Image:: /images/ti-lvgl-demo-legacy-home.png
         :height: 500

   .. ifconfig:: CONFIG_part_variant in ('AM62LX' 'AM62PX' 'AM62X')

      .. Image:: /images/ti-lvgl-demo-home-page.gif
         :height: 500


   - In the demo, scroll through the various widgets to launch different apps.
   - The date/time panel shows the UTC timezone provided the EVM is connected to the internet.
   - Exit button on top left can be used to exit the demo. :code:`systemctl stop ti-lvgl-demo` can also be used to stop the demo.
   - System button (Center button in top-right toolbar) shows FPS of the demo and CPU Utilization of the system.
   - Buttons in bottom-right toolbar enable to switch between light and dark theme.

   .. ifconfig:: CONFIG_part_variant in ('AM62LX')

      -  The temperature panel shows a value derived from the ADC data being input on ADC channel 0 pin.


Launching the EV Charging HMI
=============================

#. To launch the EV Charging HMI demo, click on the `EV Charging` widget in the apps scroll menu.
#. Click on the `Start charging` button to emulate charging of EV. This will increment charge percentage at fixed time intervals.

   .. Image:: /images/ti-lvgl-demo-ev-charging1.png
      :height: 300
   .. Image:: /images/ti-lvgl-demo-ev-charging2.png
      :height: 300


Launching the Arm analytics
=============================

#. Launch the Arm Analytics demo by clicking the **Arm Analytics** widget in the apps scroll menu.
#. Connect the microphone and click the **Play** button to start audio recognition.

   .. Image:: /images/ti-lvgl-demo-arm-analytics1.png
      :height: 300
#. Expose multiple audio sources to the microphone to view the output results. Click the **Stop** button to stop audio recognition.

   .. Image:: /images/ti-lvgl-demo-arm-analytics2.png
      :height: 300
   .. Image:: /images/ti-lvgl-demo-arm-analytics3.png
      :height: 300

**Technical Details:**

The Arm Analytics demo leverages machine learning for real-time audio recognition:

- **ML Framework**: The demo uses :ref:`TensorFlow Lite (LiteRT) <tflite-label>` as the deep learning runtime for efficient on-device inference on Arm Cortex-A cores
- **Pipeline Management**: :ref:`NNStreamer <nnstreamer-label>` is used to manage the neural network pipeline, providing seamless integration between audio capture and ML inference through GStreamer plugins

For more information on the underlying technologies:

- :ref:`TensorFlow Lite (LiteRT) <tflite-label>` - Deep learning inference framework
- :ref:`NNStreamer <nnstreamer-label>` - Neural network pipeline management

Launching the Smart Home HMI
============================

To launch the Smart Home HMI demo, click on the `Smart Home` widget in the apps scroll menu.

   .. Image:: /images/ti-lvgl-demo-smart-home1.png
      :height: 300
   .. Image:: /images/ti-lvgl-demo-smart-home2.png
      :height: 300

   |

*Understanding the MQTT setup of Smart Home*
   - All MQTT messages that are sent/received in this demo are to/from `broker.hivemq.com <https://broker.hivemq.com>`__ over port 8883.
   - MQTT communication example between the demo HMI and online MQTT client can be found in the following images:

      .. Image:: /images/ti-lvgl-demo-mqtt1.png
         :height: 300
      .. Image:: /images/ti-lvgl-demo-mqtt2.png
         :height: 300
   - Please note that the broker service used for this demo is free of charge, however, other broker services can be used as well and here
     are the necessary changes required in `ti-lvgl-demo/lv_port_linux/lvgl/demos/high_res/ <https://github.com/TexasInstruments/ti-lvgl-demo.git/>`__

      .. code-block:: c

         /* In mqtt_temp_pub_init() function in adc.c AND
            in mqtt_sub_init() function in mqtt_sub.c*/

         //Remove the following line if using unencrypted communication, else,
         //Update with path of the broker certificate in the filesystem.
         mosquitto_tls_set(mosq, "/usr/share/ti-lvgl-demo/cert/AmazonRootCA1.pem", NULL, NULL, NULL, NULL);

         //Replace 8883 with 1883 for unencrypted communication
         //Replace "broker.hivemq.com" with URL/IP of the broker to be used
         rc = mosquitto_connect(mosq, "broker.hivemq.com", 8883, 60);

   - All messages transmitted/received are SSL-encrypted MQTT messages.
   - To interact with the HMI remotely, user can use any interface (mobile-app/web-app/website) that implements transmitting/receiving MQTT
     messages over internet. To do this, just set broker to `broker.hivemq.com` on that interface and subscribe to or publish on the below
     mentioned topics:

      - Remote device can subscribe to topic: `SmartHome/temp`
      - Remote device can subscribe to topic: `SmartHome/evCharge`
      - Remote device can publish to topic: `SmartHome/volume`
      - Remote device can publish to topic: `SmartHome/led`

   - Note that there is no restriction on who can publish/subscribe to the above topics. **That means that one device can receive data published
     from some other remote application as well. Concurrent usage by other users on same MQTT topic may impact your GUI.** To minimize
     any issues, try to use unique MQTT topic names, like *<unique ID>/SmartHome/<widget>*. The topics can be changed at following
     locations in `ti-lvgl-demo/lv_port_linux/lvgl/demos/high_res/ <https://github.com/TexasInstruments/ti-lvgl-demo.git/>`__:

      .. code-block:: c

         /* In  on_connect_vol_sub() function in mqtt_sub.c*/
         rc = mosquitto_subscribe(mosq, NULL, "SmartHome/volume", 1);
         :
         rc = mosquitto_subscribe(mosq, NULL, "SmartHome/led", 1);

         /* In  publish_sensor_data() function in adc.c*/
         rc = mosquitto_publish(mosq, NULL, "SmartHome/temp", strlen(payload), payload, 1, false);

         /* In  publish_evCharge_data() function in adc.c*/
         rc = mosquitto_publish(mosq, NULL, "SmartHome/evCharge", strlen(payload), payload, 1, false);

   .. note::

      By default CC33xx is configured at boot, so here are the steps that can be followed to enable it. If you are running as non-root user, run the following using `sudo`:

      .. ifconfig:: CONFIG_sdk in ('SITARA')

         .. code-block:: console

            root@<machine>:~ systemctl stop ti-lvgl-demo
            root@<machine>:~  cd /usr/share/cc33xx
            root@<machine>:~  ./sta_start.sh
            root@<machine>:~  ./sta_connect.sh -s WPA-PSK -n <SSID> -p <PASSWORD>
            root@<machine>:~  udhcpc -i wlan0
            root@<machine>:~  systemctl start ti-lvgl-demo

      .. ifconfig:: CONFIG_sdk in ('DebianSDK')

         .. code-block:: console

            root@<machine>:~  systemctl stop ti-lvgl-demo
            root@<machine>:~  cd /usr/share/cc33xx
            root@<machine>:~  bash ./sta_start.sh
            root@<machine>:~  bash ./sta_connect.sh -s WPA-PSK -n <SSID> -p <PASSWORD>
            root@<machine>:~  udhcpc -i wlan0
            root@<machine>:~  systemctl start ti-lvgl-demo

      For more details on how to enable CC33xx and connect to WiFi, visit :ref:`How to Enable M.2-CC33x1 in Linux <enable_m2cc3301>`

**The application includes the following widgets:**

*Widget#1: Climate Control*

.. note::

   This feature will work on platforms that have on-chip ADC. Following is supported on AM62Lx

- The indoor temperature in this widget displays the digital data obtained from ADC and display (data/10) on the widget.
- The outdoor temperature below the indoor temperature shows the value of (data/10)-6.5, if it is positive, else, shows zero.
- The indoor temperature is sent over SSL-encrypted MQTT messages under the topic `SmartHome/temp`
- This demo uses channel 0 for ADC input. To change the channel being used, modify the following in
   `ti-lvgl-demo/lv_port_linux/lvgl/demos/high_res/adc.c <https://github.com/TexasInstruments/ti-lvgl-demo.git/>`__

.. code-block:: c

   FILE *fp = popen("cat /sys/bus/iio/devices/iio\:device0/in_voltage0_raw", "r");

*Widget#2: Charging*

- The data shown in this widget is the same that is shown in the EV Charging HMI app.
- This percentage completion data is also sent over SSL-encrypted MQTT messages under the topic `SmartHome/evCharge`

*Widget#3: Lock*

.. note::

   Lock screen feature has only been enabled on AM62L

- Sliding the lock to the right will lock the screen (disable all screen input)
- To unlock, press the SW5: User Button on the TMDS62LEVM

   .. Image:: /images/ti-lvgl-demo-tmds62levm-usr-button.png
      :height: 200

*Widget#4: Speaker*

- The play/pause button will play noise in the McASP device.
- Custom audio filecan also be played by making necessary changes as shown below in
   `ti-lvgl-demo/lv_port_linux/lvgl/demos/high_res/audio.c <https://github.com/TexasInstruments/ti-lvgl-demo.git/>`__

   .. code-block:: c

      /* Copy the audio file in the SD file system */
      /* In audio_play() function in audio.c */

      //Modify the following as per the specification of the audio file
      rate     = 48000; //in Hz
      channels = 1;     //1: mono, 2:stereo
      seconds  = 1;     //duration of audio
      :
      :
      //Replace "/usr/share/sounds/alsa/Noise.wav" with the path of the audio file
      char *filename_wav = "/usr/share/sounds/alsa/Noise.wav";

- Volume can be controlled from the vertical slider on the right-side of the widget.
- Volume can also be set by sending values between 1 to 100 over MQTT topic `SmartHome/volume` from remote device over internet.

*Widget#5: Main Light*

- The `Light temperature` slider will increase/decrease the User LED blinking frequency.
- The left-end of slider (0 K) toggles LED every 250ms and the right-end of slider (20000 K) toggles LED every 20ms.
- `Light temperature` can also be set by sending values between 0 to 20000 over MQTT topic `SmartHome/led` from remote device over internet.
- In HMI, the slider `Light temperature` is not associated with any functionality but can be programmed be user to perform any function.

*Widget#6: Sensor Controls*

- The buttons/sliders in this widget are not associated with any functionality but can be programmed by the user to perform any function.

Launching the Smart Meter HMI
=============================

To launch the Smart Meter HMI demo, click on the `Smart Meter` widget in the apps scroll menu.

   .. Image:: /images/ti-lvgl-demo-smart-meter.png
      :height: 300


Launching the Thermostat HMI
============================

To launch the Thermostat HMI demo, click on the `Thermostat` widget in the apps scroll menu.

   .. Image:: /images/ti-lvgl-demo-thermostat.png
      :height: 300


Launching the Security HMI
==========================

To launch the Security HMI demo, click on the `Security` widget in the apps scroll menu.

   .. Image:: /images/ti-lvgl-demo-security.png
      :height: 300

This widget contains a slide-show on Application Processor Security for AM6X devices.

**************************************
Building the TI LVGL Demo from Sources
**************************************

.. ifconfig:: CONFIG_sdk in ('SITARA')

   The TI LVGL Demo is enabled in :file:`tisdk-default-image` yocto filesystem for |__PART_FAMILY_DEVICE_NAMES__| by default.

.. ifconfig:: CONFIG_sdk in ('DebianSDK')

   The TI LVGL Demo is packaged in :file:`tisdk-debian-trixie` wic image for |__PART_FAMILY_DEVICE_NAMES__| by default.

Note, that the binary itself does not have asset images and slides built in it.
The image contains the required assets within :file:`/usr/share/ti-lvgl-demo/`. Place any additional
assets here while making any modifications.

.. ifconfig:: CONFIG_sdk in ('SITARA')

   Yocto recipe for building this demo can be found at
   `github: ti-lvgl-demo.bb <https://github.com/TexasInstruments/meta-tisdk/blob/scarthgap/meta-ti-foundational/recipes-demos/ti-lvgl-demo/ti-lvgl-demo.bb>`__

.. ifconfig:: CONFIG_sdk in ('DebianSDK')

   Debian package for building this demo can be found at
   `github: ti-lvgl-demo debian package <https://github.com/TexasInstruments/debian-repos/blob/master/ti-lvgl-demo/suite/trixie/debian/>`__

The source code is available at `TI LVGL Demo <https://github.com/TexasInstruments/ti-lvgl-demo.git/>`__ and can be re-compiled with the
following steps:


#. First clone the appropriate git repository and its submodules using:

   .. ifconfig:: CONFIG_part_variant in ('AM62LX', 'AM62X', 'AM62PX')

      .. code-block:: console

         $ git clone --recurse-submodules https://github.com/TexasInstruments/ti-lvgl-demo.git

   .. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM65X')

      .. code-block:: console

         $ git clone -b legacy --recurse-submodules https://github.com/TexasInstruments/ti-lvgl-demo.git

#. Create the docker environment and build the application:


      .. code-block:: console

         $ cd ti-lvgl-demo
         $ sudo ./scripts/docker_setup.sh --create-image
         $ sudo ./scripts/docker_setup.sh --build-app

#. Copy the compiled binary to :file:`/usr/bin` directory of the device

   .. ifconfig:: CONFIG_part_variant in ('AM62LX', 'AM62X', 'AM62PX')

      .. code-block:: console

         $ scp lv_port_linux/bin/lvglsim root@<ip-addr-of-device>:/usr/bin/
         $ scp -r lv_port_linux/demos/high_res/assets/* root@<ip-addr-of-device>:/usr/share/ti-lvgl-demo/assets/  #make sure assets directory is there on target
         $ scp -r lv_port_linux/demos/high_res/slides/* root@<ip-addr-of-device>:/usr/share/ti-lvgl-demo/slides/  #make sure slides directory is there on target
         $ scp lv_port_linux/certs/<certificate> root@<ip-addr-of-device>:/usr/share/ti-lvgl-demo/cert/           #make sure cert directory is there on target

   .. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X', 'AM65X')

      .. code-block:: console

         $ scp lv_port_linux/build-arm64/bin/lvglsim root@<ip-addr-of-device>:/usr/bin/
         $ scp -r lv_port_linux/build-arm64/_deps/lv_demos_ext-src/src/high_res/assets/* root@<ip-addr-of-device>:/usr/share/ti-lvgl-demo/assets/     #make sure assets directory is there on target
