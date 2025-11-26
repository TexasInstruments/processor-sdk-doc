.. _Webserver-Demo-User-Guide-label:

############################
Web server demo - User Guide
############################

********
Overview
********

This document describes the Out of Box Web Server Demo Application, which the Linux
SDK delivers with the |__SDK_FULL_NAME__| |__PART_FAMILY_NAME__|, applicable to boards
such as the `BEAGL-BONE-GRN-ECO <https://www.ti.com/tool/BEAGL-BONE-GRN-ECO>`__ and
`TMDXEVM3358 <https://www.ti.com/tool/TMDXEVM3358>`__. The main purpose of this demo is to
showcase a glimpse of the ARM analytics AI stack integrated into the filesystem,
providing an out-of-box experience even users do not connect a display to the board.

The demo showcases a web server running on an AM335x based board, providing a web interface with three key sections:

*  **Audio Classification Demo**: Users can connect a USB audio capture device to run real-time audio classification, displaying classification statistics.
*  **Live CPU Performance Metrics**: Provides a real-time CPU usage indicator, historical usage data for the last 5 minutes, and detailed CPU information.
*  **Documentation Links**: Offers convenient access to relevant documentation.

This document provides all necessary equipment requirements and instructions.

**********************
Hardware Prerequisites
**********************

-  TI AM335x based board (e.g., `BEAGL-BONE-GRN-ECO <https://www.ti.com/tool/BEAGL-BONE-GRN-ECO>`__ and `TMDXEVM3358 <https://www.ti.com/tool/TMDXEVM3358>`__)
   (Note: For the Beaglebone Green Eco, a display is available via an `HDMI cape <https://wiki.seeedstudio.com/BeagleBone_Green_HDMI_Cape>`__)
-  PC (Windows or Linux)
-  Ethernet cables
-  Ethernet switch or ethernet router with DHCP service
-  SD card (minimum 16GB)
-  Audio Capture Device

***********
Get Started
***********

#.  Flash an SD card with the :file:`tisdk-default-image`. User can download the :file:`tisdk-default-image` wic
    image from |__SDK_DOWNLOAD_URL__|. Please follow the instructions from here to :ref:`Flash an SD card <processor-sdk-linux-create-sd-card>`.

#.  Insert the SD card into the AM335x based board and set it to boot via SD card Boot mode.

#.  Connect an ethernet cable from your ethernet switch or router to the
    AM335x based board.

#.  Connect your PC to the same ethernet switch or router.

#.  Connect the UART to the PC's USB port.

#.  Open a terminal program (like TeraTerm or minicom) and connect to the
    serial port. Set the port to 115200bps, 8 bit, no parity, 1 stop bit, no flow control.

#.  Power on the AM335x based board.

#.  After the Linux boot completes, login as "root". Use the :command:`ifconfig` command
    to find out the IP address of the device.

#. On the host PC, open a Internet Browser and enter in the following: ``http://<IP_ADDRESS_OF_AM335x_Board>:3000``

#. The following web page will be displayed, the home page shows as below.

.. image:: /images/Webserver_home_page.PNG
   :alt: Webserver Demo Page
   :width: 75%

*************************
Audio Classification Demo
*************************

The web interface provides an audio classification demo that uses the integrated ARM analytics AI stack.

.. image:: /images/Webserver_audio_classification.PNG
   :alt: Audio Classification Demo
   :width: 75%

To use the demo:

#.  Connect a USB audio device (e.g., a USB headset) to the AM335x based board.
#.  Click the "Refresh Devices" button to detect the connected audio capture device.
#.  Select the desired audio capture device from the list of available devices.
#.  Click the "Start Classification" button to begin real-time audio classification.
#.  The "Live Classification" section will display the current classification, total classifications, unique classes, session time, and updates per minute.
#.  A "Classification History" log is also available, showing a timestamped record of classifications.
#.  Click the "Stop Classification" button to end the demo.

**Technical Details**

The audio classification demo leverages :ref:`NNStreamer <nnstreamer-label>`, a GStreamer-based neural network framework, to create and run the processing pipeline.

*  **Model:** The demo uses the `YAMNet <https://www.kaggle.com/models/google/yamnet/tfLite>`__ sound classification model.
*  **Deep Learning Runtime:** The model is executed using the :ref:`TensorFlow Lite <tflite-label>` runtime.

**GStreamer Pipeline**

The following GStreamer pipeline is used to process the audio from the microphone, run the inference, and decode the results:

.. code-block:: console

   gst-launch-1.0 alsasrc device=<device> ! \
       audioconvert ! \
       audio/x-raw,format=S16LE,channels=1,rate=16000,layout=interleaved ! \
       tensor_converter frames-per-tensor=3900 ! \
       tensor_aggregator frames-in=3900 frames-out=15600 frames-flush=3900 frames-dim=1 ! \
       tensor_transform mode=arithmetic option=typecast:float32,add:0.5,div:32767.5 ! \
       tensor_transform mode=transpose option=1:0:2:3 ! \
       queue leaky=2 max-size-buffers=10 ! \
       tensor_filter framework=tensorflow2-lite model=/usr/share/oob-demo-assets/models/yamnet_audio_classification.tflite custom=Delegate:XNNPACK,NumThreads:2 ! \
       tensor_decoder mode=image_labeling option1=/usr/share/oob-demo-assets/labels/yamnet_label_list.txt ! \
       filesink buffer-mode=2 location=<fifo_path>

****************************
Live CPU Performance Metrics
****************************

The web interface also provides a live view of the CPU performance metrics.

.. image:: /images/Webserver_CPU_Performance.PNG
   :alt: CPU Performance Metrics
   :width: 75%

This section includes:

*  **CPU Usage**: A real-time gauge showing the current CPU utilization.
*  **CPU History**: A graph displaying the CPU usage history over the last 5 minutes.
*  **Statistics**: Average and maximum CPU usage calculated for the data from CPU History data.

*********************
Software Architecture
*********************

The demo is comprised of three main components: a web interface, a backend web server, and a set of Linux applications.

*  **Web Interface (GUI):** A dynamic HTML page with JavaScript that runs in the user's browser. It provides the user interface for the audio classification demo and CPU performance metrics, making asynchronous requests to the web server for data updates.

*  **Web Server:** A lightweight HTTP server (e.g., Node.js) running on the AM335x's Arm A8 core. It serves the static web page and provides a simple REST API for the frontend to interact with the underlying Linux applications.

*  **Linux Applications:** A set of background applications running on the AM335x, with the following key functions:

    *  A C application that reads real-time system information (like CPU stats from :file:`/proc/stat`) and makes it available to the web server.
    *  The audio classification demo, which is a GStreamer pipeline that leverages the NNStreamer framework. This pipeline reads from a USB audio device, processes the audio with the YAMNet model using the TensorFlow Lite runtime, and sends the classification results to the web server.

*******************
Directory Structure
*******************

Yocto recipe for building this demo can be found at `github:webserver-oob_git.bb <https://github.com/TexasInstruments/meta-tisdk/blob/scarthgap/meta-ti-foundational/recipes-demos/webserver-oob/webserver-oob_git.bb>`__.

The source code for the demo can be found at `github/TexasInstruments/webserver-oob-demo <https://github.com/TexasInstruments/webserver-oob-demo>`__.
For instructions on building the utilities see the `README <https://github.com/TexasInstruments/webserver-oob-demo/blob/main/README.md>`__ file.

.. list-table:: Directory Structure
   :widths: 20 30
   :header-rows: 1

   * - Directory Name
     - Description
   * - :file:`webserver_app/app`
     - GUI code (HTML, CSS, JavaScript)
   * - :file:`webserver_app/linux_app`
     - Linux application code (C code)
   * - :file:`webserver_app/webserver`
     - Web server code (Node.js)
