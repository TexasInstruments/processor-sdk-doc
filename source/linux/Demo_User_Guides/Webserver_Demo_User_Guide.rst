.. _Webserver-Demo-User-Guide-label:

############################
Web server demo - User Guide
############################

********
Overview
********

The Out-of-Box (OOB) Web Server Demo provides a browser-accessible interface
for exploring key capabilities of the |__PART_FAMILY_NAME__| platform. A
lightweight HTTP server runs on the board and serves a dynamic web application.
Users can interact with the board from any PC on the same network without
requiring a connected display.

The demo uses a plugin architecture that adapts automatically to each target
device. The following table lists the demos available on |__PART_FAMILY_NAME__|:

.. list-table:: Available Demos by Platform
   :widths: 40 10 10 10 10
   :header-rows: 1

   * - Demo
     - AM335x
     - AM62x
     - AM62Px
     - AM62Lx
   * - :ref:`webserver-cpu-monitor`
     - Yes
     - Yes
     - Yes
     - Yes
   * - :ref:`webserver-audio-classification`
     - Yes
     - Yes
     - Yes
     - Yes
   * - :ref:`webserver-speech-to-text`
     - No
     - Yes
     - Yes
     - Yes

.. note::

   This guide uses screenshots from AM62Px. The web interface layout is the
   same across all supported platforms; the device name and board image shown
   on the home page will reflect the actual device in use.

**********************
Hardware Prerequisites
**********************

-  |__PART_FAMILY_NAME__| evaluation board
-  PC (Windows or Linux)
-  Ethernet cable
-  Ethernet switch or router with DHCP service
-  SD card (minimum 32 GB)
-  Audio capture device (required for the Audio Classification and Speech to Text demos)

***********
Get Started
***********

#.  Flash an SD card with the :file:`tisdk-default-image`. Download the
    :file:`tisdk-default-image` wic image from |__SDK_DOWNLOAD_URL__|. Follow
    the instructions at :ref:`Flash an SD card <processor-sdk-linux-create-sd-card>`.

#.  Insert the SD card into the |__PART_FAMILY_NAME__| board and set it to boot
    from SD card.

#.  Connect an Ethernet cable from your switch or router to the board.

#.  Connect your PC to the same Ethernet switch or router.

#.  Connect the UART to the PC USB port.

#.  Open a terminal program (such as TeraTerm or minicom) and connect to the
    serial port at 115200 bps, 8 data bits, no parity, 1 stop bit, no flow
    control.

#.  Power on the board.

#.  After Linux boot completes, log in as ``root``. Use the
    :command:`ifconfig` command to find the board's IP address.

#.  On the host PC, open a browser and navigate to:
    ``http://<BOARD_IP_ADDRESS>:3000``

#.  The home page displays, showing the demos available for your device.

    .. image:: /images/Webserver_home_page.png
       :alt: Webserver Demo Home Page
       :width: 75%

.. _webserver-cpu-monitor:

****************************
Live CPU Performance Metrics
****************************

Available on all supported platforms.

The CPU monitor provides a real-time view of processor usage.

.. image:: /images/Webserver_CPU_Performance.png
   :alt: CPU Performance Metrics
   :width: 75%

*  **CPU Usage**: A real-time gauge showing the current CPU usage.
*  **CPU History**: A graph displaying CPU usage over the last 5 minutes.
*  **Statistics**: Average and maximum CPU usage calculated from the history data.

.. _webserver-audio-classification:

*************************
Audio Classification Demo
*************************

Available on: AM335x, AM62x, AM62Px, AM62Lx.

The audio classification demo uses the integrated AI stack to classify sounds
captured from a microphone in real time.

.. image:: /images/Webserver_audio_classification.png
   :alt: Audio Classification Demo
   :width: 75%

To use the demo:

#.  Connect an audio capture device to the board.
#.  Click **Refresh Devices** to detect the connected audio capture device.
#.  Select the audio capture device from the list.
#.  Click **Start Classification** to begin real-time audio classification.
#.  The **Live Classification** section displays the current classification,
    total classifications, unique classes, session time, and updates per minute.
#.  The **Classification History** log shows a timestamped record of all
    classifications.
#.  Click **Stop Classification** to end the demo.

**Technical Details**

The audio classification demo uses :ref:`NNStreamer <nnstreamer-label>`, a
GStreamer-based neural network framework, to build and run the inference
pipeline.

*  **Model:** `YAMNet <https://www.kaggle.com/models/google/yamnet/tfLite>`__
   sound classification model
   (`yamnet_audio_classification.tflite <https://github.com/TexasInstruments/oob-demo-assets/blob/master/models/yamnet_audio_classification.tflite>`__).
*  **Deep Learning Runtime:** :ref:`TensorFlow Lite <tflite-label>`.
*  **Inference:** XNNPACK delegate on the Arm Cortex-A cores.

**GStreamer Pipeline**

.. code-block:: console

   gst-launch-1.0 alsasrc device=<device> ! \
       audioconvert ! \
       audio/x-raw,format=S16LE,channels=1,rate=16000,layout=interleaved ! \
       tensor_converter frames-per-tensor=3900 ! \
       tensor_aggregator frames-in=3900 frames-out=15600 frames-flush=3900 frames-dim=1 ! \
       tensor_transform mode=arithmetic option=typecast:float32,add:0.5,div:32767.5 ! \
       tensor_transform mode=transpose option=1:0:2:3 ! \
       queue leaky=2 max-size-buffers=10 ! \
       tensor_filter framework=tensorflow2-lite \
           model=/usr/share/oob-demo-assets/models/yamnet_audio_classification.tflite \
           custom=Delegate:XNNPACK,NumThreads:2 ! \
       tensor_decoder mode=image_labeling \
           option1=/usr/share/oob-demo-assets/labels/yamnet_label_list.txt ! \
       filesink buffer-mode=2 location=<fifo_path>

.. _webserver-speech-to-text:

*******************
Speech to Text Demo
*******************

Available on: AM62x, AM62Px, AM62Lx.

The speech-to-text demo uses an on-device speech recognition model to
transcribe spoken words captured from a microphone in real time.

.. image:: /images/Webserver_speech_to_text.png
   :alt: Speech to Text Demo
   :width: 75%

To use the demo:

#.  Connect an audio capture device to the board.
#.  Click **Refresh Devices** to detect connected audio capture devices.
#.  Select the microphone from the list.
#.  Click **Start** to begin transcription. Transcribed text is displayed in
    the output area as you speak.
#.  Click **Stop** to end the demo.

**Technical Details**

The speech-to-text demo uses :ref:`NNStreamer <nnstreamer-label>` and
:ref:`ONNX Runtime <onnx-runtime>` to process audio through a streaming
inference pipeline.

*  **Model:** `Silero STT en_v5 <https://github.com/snakers4/silero-models>`__
   English speech recognition model
   (`en_v5_static.onnx <https://github.com/TexasInstruments/oob-demo-assets/blob/master/models/en_v5_static.onnx>`__).
*  **Deep Learning Runtime:** :ref:`ONNX Runtime <onnx-runtime>`.
*  **Decoder:** Greedy CTC decoder over a 999-token BPE vocabulary, with
   blank-ratio silence gating to suppress output during microphone silence
   or background noise. Implemented in :command:`speech_utils` using the
   ``tensor_sink`` new-data signal.

**GStreamer Pipeline**

The pipeline processes audio in a 3-second sliding window with a 1-second
stride, enabling low-latency continuous transcription.
:command:`speech_utils` builds the pipeline internally through the GStreamer
API; the ``tensor_sink`` new-data callback performs CTC decoding and writes
transcripts to a named FIFO.

.. code-block:: console

   gst-launch-1.0 alsasrc device=<device> ! \
       audioconvert ! audioresample ! \
       audio/x-raw,format=S16LE,channels=1,rate=16000 ! \
       tensor_converter frames-per-tensor=16000 ! \
       tensor_aggregator frames-in=16000 frames-out=48000 \
           frames-flush=16000 frames-dim=1 ! \
       tensor_transform mode=arithmetic option=typecast:float32,div:32768 ! \
       tensor_filter framework=onnxruntime \
           model=/usr/share/oob-demo-assets/models/en_v5_static.onnx ! \
       fakesink


*********************
Software Architecture
*********************

The demo consists of three main layers: a web front end, a backend HTTP
server, and device-specific Linux applications.

*  **Web front end:** A dynamic HTML page with JavaScript that runs in the
   user's browser. It makes asynchronous REST and WebSocket requests to the
   server to update the display in real time.

*  **Web Server:** A Node.js Express server running on the board. It serves the
   static web page and loads demo plugins at startup based on the device
   configuration in :file:`/usr/share/webserver-oob/app/device.json`. Each
   plugin registers its own REST and WebSocket endpoints.

*  **Linux Applications:** Native C utilities built for the target device:

   *  :command:`cpu_stats` - reads CPU load from :file:`/proc/stat` and
      exposes it to the web server.
   *  :command:`audio_utils` - manages the GStreamer+NNStreamer audio
      classification pipeline and writes results to a named FIFO.
   *  :command:`speech_utils` - manages the GStreamer+ONNX Runtime
      speech-to-text pipeline and writes transcripts to a named FIFO.

*******************
Directory Structure
*******************

The Yocto recipe for building this demo is at
`github:webserver-oob_git.bb <https://github.com/TexasInstruments/meta-tisdk/blob/12.01.00.05.03/meta-ti-foundational/recipes-demos/webserver-oob/webserver-oob_git.bb>`__.

The source code is at
`webserver-oob-demo on GitHub <https://github.com/TexasInstruments/webserver-oob-demo>`__.
See the `README <https://github.com/TexasInstruments/webserver-oob-demo/blob/main/README.md>`__
for build instructions.

.. list-table:: Directory Structure
   :widths: 30 70
   :header-rows: 1

   * - Directory
     - Description
   * - :file:`common/app`
     - Generic front end (HTML, CSS, JavaScript)
   * - :file:`common/linux_app`
     - Shared C utilities: :command:`cpu_stats`, :command:`audio_utils`,
       :command:`speech_utils`
   * - :file:`common/webserver`
     - Express server and demo plugin loader
   * - :file:`demos/<id>`
     - Per-demo plugin: :file:`manifest.json` and :file:`server-plugin.js`
   * - :file:`devices/<id>`
     - Per-device metadata (:file:`device.json`), front end overlay, and
       device-specific Linux application build
