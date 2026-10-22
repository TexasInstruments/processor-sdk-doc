.. _pub_edgeai_am62dx_getting_started:

##############################
How to run GStreamer Pipelines
##############################

The two GStreamer elements, ``tidspkernel`` and ``titvm``, that
offload audio signal processing and neural-network inference to the C7x DSP on
|__PART_FAMILY_NAME__|. With them you can build a standard ``gst-launch-1.0`` pipeline that
reads a WAV file, runs it through a speech-enhancement or audio-classification model on the
DSP, and writes or prints the result — without writing any DSP-side code yourself.

Prerequisites
=============

All runtime libraries, model artifacts, sample audio files, model daemon, and DSP firmware
verification are pre-packaged in the AM62DX EdgeAI image. See
:ref:`Models, Artifacts and Setup <am62dx_edgeai_models_artifacts_and_setup>` for details.

To build the GStreamer plugins from source, the following host tools are required:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Tool
     - Purpose
   * - ``meson`` / ``ninja``
     - Build system for GStreamer plugins
   * - ARM cross-toolchain
     - Required for host cross-build only
   * - ``pkg-config``
     - Dependency resolution during build

*******************************
Building on AUDIO-AM62D-EVM
*******************************

The plugins are pre-installed on the AM62DX EdgeAI image. If you need to rebuild them
natively on the AUDIO-AM62D-EVM:

.. code-block:: console

   root@am62dxx-evm:~# git clone https://github.com/TexasInstruments/edgeai-gst-plugins.git
   root@am62dxx-evm:~# cd edgeai-gst-plugins
   root@am62dxx-evm:~/edgeai-gst-plugins# export SOC=am62d
   root@am62dxx-evm:~/edgeai-gst-plugins# meson setup build --prefix=/usr -Dpkg_config_path=pkgconfig \
     -Dtvm-plugins=enabled -Dstft-plugins=enabled \
     -Ddl-plugins=disabled -Denable-tidl=disabled
   root@am62dxx-evm:~/edgeai-gst-plugins# ninja -C build
   root@am62dxx-evm:~/edgeai-gst-plugins# ninja -C build install
   root@am62dxx-evm:~/edgeai-gst-plugins# ldconfig

**********************
Building on Host
**********************

.. _pub_edgeai_am62dx_cross_build:

For cross-building on a host machine, follow the cross-compile steps in the
`edgeai-gst-plugins README <https://github.com/TexasInstruments/edgeai-gst-plugins#cross-compiling-the-project>`__.
Install into the SDK target filesystem with ``DESTDIR``, then copy the libraries
to the AUDIO-AM62D-EVM.

**************************
Verifying the Installation
**************************

Execute the following command to verify the tidspkernel GStreamer plugin is installed:

.. code-block:: console

   root@am62dxx-evm:~# gst-inspect-1.0 tidspkernel
   Factory Details:
   Rank                     none (0)
   Long-name                TI DSP Kernel Transform
   Klass                    Transform/DSP
   Description              Generic DSP kernel offload (STFT/ISTFT/Deinterleave/Interleave) via RPMsg-DMA
   Author                   Pratham Deshmukh <p-deshmukh@ti.com>

   Plugin Details:
   Name                     ti
   Description              GStreamer plugin for TI devices
   Filename                 /usr/lib/gstreamer-1.0/libgstti.so
   Version                  0.7.0
   License                  Proprietary
   Source module            GstTIOVX
   Binary package           GstTIOVX source release
   Origin URL               http://ti.com

   GObject
   +----GInitiallyUnowned
        +----GstObject
             +----GstElement
                  +----GstBaseTransform
                       +----GstDspKernel

Execute the following command to verify the titvm GStreamer plugin is installed:

.. code-block:: console

   root@am62dxx-evm:~# gst-inspect-1.0 titvm
   Factory Details:
   Rank                     none (0)
   Long-name                TI TVM Inference
   Klass                    Transform/ML
   Description              TVM inference on TI processors with C7x DSP acceleration
   Author                   Pratham Deshmukh <p-deshmukh@ti.com>

   Plugin Details:
   Name                     ti
   Description              GStreamer plugin for TI devices
   Filename                 /usr/lib/gstreamer-1.0/libgstti.so
   Version                  0.7.0
   License                  Proprietary
   Source module            GstTIOVX
   Binary package           GstTIOVX source release
   Origin URL               http://ti.com

   GObject
   +----GInitiallyUnowned
        +----GstObject
             +----GstElement
                  +----GstBaseTransform
                       +----GstTiTvm


Both commands must print the element details. If an element is missing, check that
``/usr/lib/gstreamer-1.0/libgstti.so`` exists and that ``ldconfig`` has run.

.. _pub_edgeai_am62dx_model_artifacts:

GCRN based Audio Enhancement
=============================

Speech enhancement removes background noise from a recording while keeping the speech
intelligible — useful for voice calls, meeting recordings, hearables, and any product that
captures speech in a noisy environment. This pipeline runs that enhancement end to end on the
board: it reads a 16 kHz mono WAV file, converts it to the frequency domain on the DSP, runs
the GCRN model on the result, and converts the enhanced spectrum back to audio you can play or
save.

.. _pub_edgeai_am62dx_enhancement_command:

How to run GStreamer based GCRN Audio Enhancement
-------------------------------------------------

Execute the following command to run the audio enhancement pipeline. The command writes ``/tmp/gst_enhanced.wav`` and plays the enhanced audio output through ``autoaudiosink``. Connect headphones to J3/J4 as directed in :ref:`pub_edgeai_am62dx_evm_setup` to listen to the enhanced audio.

.. code-block:: bash

   INPUT=/usr/share/tvm_inference/input/input_audio.wav
   MODEL=/usr/share/tvm_inference/artifacts/gcrn

   gst-launch-1.0 -v \
     filesrc location=$INPUT ! wavparse ! \
     audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
     tidspkernel name=stft msg-type=0x1020 model-path=$MODEL \
       hop-size=160 fft-size=320 window-frames=401 batch-size=64 \
       max-stream-samples=160480 ! \
     tidspkernel name=deinterleave msg-type=0x1040 interleave_direction=0 \
       model-path=$MODEL fft-size=320 window-frames=401 ! \
     titvm model-path=$MODEL ! \
     tidspkernel name=interleave msg-type=0x1040 interleave_direction=1 \
       model-path=$MODEL fft-size=320 window-frames=401 ! \
     tidspkernel name=istft msg-type=0x1030 model-path=$MODEL \
       hop-size=160 fft-size=320 window-frames=401 batch-size=64 \
       max-stream-samples=160480 ! \
     audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
     tee name=t \
     t. ! queue ! wavenc ! filesink location=/tmp/gst_enhanced.wav \
     t. ! queue ! audioconvert ! audioresample ! autoaudiosink

For a headless run, remove the ``tee`` branch and keep only the file output:

.. code-block:: bash

   ... ! audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
     wavenc ! filesink location=/tmp/gst_enhanced.wav

.. _pub_edgeai_am62dx_enhancement_chunking:

Troubleshooting
---------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Message
     - Action
   * - ``max-stream-samples must be explicitly set (> 0)``
     - Set ``max-stream-samples`` on the STFT element.
   * - ``padded length ... exceeds dma_input capacity``
     - Increase ``max-stream-samples`` to the padded length.
   * - ``Invalid incoming buffer``
     - The input is longer than ``max-stream-samples``. Increase it.
   * - ``Model daemon handshake failed`` followed by a long wait
     - Start the daemon, or accept the in-process load time.
   * - ``c7x_client_open() failed — is the c7x_compute DSP firmware running?``
     - The DSP firmware is not running. Check ``/sys/class/remoteproc/remoteproc*/state``.
   * - ``DMA heap alloc failed``
     - Not enough contiguous memory for the model. Reboot and retry, then check ``/proc/meminfo``.
   * - ``TI-Offload exchange failed`` or ``DSP kernel failed: remote status=``
     - The DSP firmware does not match the plugin. Check the DSP firmware version.
   * - ``Failed to set pipeline to PAUSED``
     - Run again with ``GST_DEBUG=tidspkernel:6,titvm:6`` and check the first error.

.. _pub_edgeai_am62dx_audio_classification:

YAMNet & VGGish based Audio Classification
============================================

Audio event classification identifies *what* sound is present in a clip — a siren, glass
breaking, a dog barking, a machine running — rather than transcribing speech. That makes it
useful for acoustic event detection, environmental and industrial sound monitoring, and
safety or anomaly alerts triggered by sound rather than video. This pipeline runs YAMNet or
VGGish on a 16 kHz mono WAV file on the DSP, and prints the top-k predicted classes and their
scores for each analysis window to the console as the pipeline runs.

YAMNet and VGGish differ mainly in scope: YAMNet recognizes 521 general sound classes, while
VGGish is a smaller, 10-class model. Pick YAMNet for broad coverage, or VGGish when you only
need to distinguish a small, fixed set of sounds and want a lighter model.

How to run GStreamer based YAMNet Audio Classification
------------------------------------------------------

Execute the following pipeline to run GStreamer based YAMNet audio classification:

.. code-block:: bash

   gst-launch-1.0 -v filesrc location=/usr/share/tvm_inference/input/urbansound_16k.wav ! \
     wavparse ! audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
     tidspkernel name=stft msg-type=0x1020 \
       model-path=/usr/share/tvm_inference/artifacts/yamnet \
       hop-size=160 window-frames=96 batch-size=64 ! \
     titvm model-path=/usr/share/tvm_inference/artifacts/yamnet \
       class-map-path=/usr/share/tvm_inference/labels/yamnet_label_list.txt \
       top-k=3 ! \
     fakesink

The following output appears:

.. code-block:: bash

   root@am62dxx-evm:~# gst-launch-1.0 -v filesrc location=/usr/share/tvm_inference/input/urbansound_16k.wav ! \
   Setting pipeline to PAUSED ...
   [TVM] Live top-3 prediction printing enabled (521 classes from /usr/share/tvm_inference/labels/yamnet_label_list.txt)
   eptdev = rpmsg-char-8-1455
   Created endpt device rpmsg-char-8-1455, fd = 7 port = 1027
   Pipeline is PREROLLING ...
   /GstPipeline:pipeline0/GstWavParse:wavparse0.GstPad:src: caps = audio/x-raw, format=(string)S16LE, layout=(string)interleaved, channels=(int)1, rate=(int)16000
   /GstPipeline:pipeline0/GstCapsFilter:capsfilter0.GstPad:src: caps = audio/x-raw, format=(string)S16LE, layout=(string)interleaved, channels=(int)1, rate=(int)16000
   /GstPipeline:pipeline0/GstDspKernel:stft.GstPad:src: caps = application/octet-stream
   /GstPipeline:pipeline0/GstTiTvm:titvm0.GstPad:src: caps = application/octet-stream
   /GstPipeline:pipeline0/GstFakeSink:fakesink0.GstPad:sink: caps = application/octet-stream
   /GstPipeline:pipeline0/GstTiTvm:titvm0.GstPad:sink: caps = application/octet-stream
   /GstPipeline:pipeline0/GstDspKernel:stft.GstPad:sink: caps = audio/x-raw, format=(string)S16LE, layout=(string)interleaved, channels=(int)1, rate=(int)16000
   /GstPipeline:pipeline0/GstCapsFilter:capsfilter0.GstPad:sink: caps = audio/x-raw, format=(string)S16LE, layout=(string)interleaved, channels=(int)1, rate=(int)16000
   Pipeline is PREROLLED ...
   Setting pipeline to PLAYING ...
   Redistribute latency...
   New clock: GstSystemClock
   Top-3 predictions for window 1:
      1. Speech: 0.532749
      2. Music: -4.261989
      3. Narration, monologue: -4.794737
   Top-3 predictions for window 2:
      1. Music: -1.598246
      2. Speech: -2.663743
      3. Television: -3.729240
   Top-3 predictions for window 3:
      1. Music: -1.065497
      2. Animal: -2.663743
      3. Speech: -3.196491
   Top-3 predictions for window 4:
      1. Speech: -1.598246
      2. Music: -1.598246
      3. Country: -5.860234
   Top-3 predictions for window 5:
      1. Speech: -2.130994
      2. Music: -3.196491
      3. Silence: -4.261989
   Top-3 predictions for window 6:
      1. Silence: 14.916960
      2. Speech: -11.187720
      3. Inside, small room: -15.982457
   Top-3 predictions for window 7:
      1. Silence: 12.253218
      2. Speech: -10.122223
      3. Inside, small room: -15.449709
   Top-3 predictions for window 8:
      1. Silence: 15.449709
      2. Speech: -10.654972
      3. Inside, small room: -14.916960
   Got EOS from element "pipeline0".
   Execution ended after 0:00:00.302017695
   Setting pipeline to NULL ...
   Freeing pipeline ...``

How to run GStreamer based VGGish Audio Classification
------------------------------------------------------

Execute the following pipeline to run GStreamer based VGGish audio classification:

.. code-block:: bash

   gst-launch-1.0 -v filesrc location=/usr/share/tvm_inference/input/urbansound_16k.wav ! \
     wavparse ! audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
     tidspkernel name=stft msg-type=0x1020 \
       model-path=/usr/share/tvm_inference/artifacts/vggish \
       hop-size=160 window-frames=126 batch-size=64 ! \
     titvm model-path=/usr/share/tvm_inference/artifacts/vggish \
       class-map-path=/usr/share/tvm_inference/labels/vggish_label_list.txt \
       top-k=3 ! \
     fakesink

The following output appears:

.. code-block:: bash

   Setting pipeline to PAUSED ...
   [TVM] Live top-3 prediction printing enabled (10 classes from /usr/share/tvm_inference/labels/vggish_label_list.txt)
   eptdev = rpmsg-char-8-1464
   Created endpt device rpmsg-char-8-1464, fd = 7 port = 1027
   Pipeline is PREROLLING ...
   /GstPipeline:pipeline0/GstWavParse:wavparse0.GstPad:src: caps = audio/x-raw, format=(string)S16LE, layout=(string)interleaved, channels=(int)1, rate=(int)16000
   /GstPipeline:pipeline0/GstCapsFilter:capsfilter0.GstPad:src: caps = audio/x-raw, format=(string)S16LE, layout=(string)interleaved, channels=(int)1, rate=(int)16000
   /GstPipeline:pipeline0/GstDspKernel:stft.GstPad:src: caps = application/octet-stream
   /GstPipeline:pipeline0/GstTiTvm:titvm0.GstPad:src: caps = application/octet-stream
   /GstPipeline:pipeline0/GstFakeSink:fakesink0.GstPad:sink: caps = application/octet-stream
   /GstPipeline:pipeline0/GstTiTvm:titvm0.GstPad:sink: caps = application/octet-stream
   /GstPipeline:pipeline0/GstDspKernel:stft.GstPad:sink: caps = audio/x-raw, format=(string)S16LE, layout=(string)interleaved, channels=(int)1, rate=(int)16000
   /GstPipeline:pipeline0/GstCapsFilter:capsfilter0.GstPad:sink: caps = audio/x-raw, format=(string)S16LE, layout=(string)interleaved, channels=(int)1, rate=(int)16000
   Pipeline is PREROLLED ...
   Setting pipeline to PLAYING ...
   Redistribute latency...
   New clock: GstSystemClock
   Top-3 predictions for window 1:
      1. Drilling: 15.796625
      2. Street music: -1.641208
      3. Car horn: -3.077265
   Top-3 predictions for window 2:
      1. Drilling: 10.873002
      2. Car horn: 0.205151
      3. Street music: -2.051510
   Top-3 predictions for window 3:
      1. Drilling: 9.642096
      2. Car horn: 1.025755
      3. Street music: -2.256661
   Top-3 predictions for window 4:
      1. Engine idling: 7.180284
      2. Children playing: 1.436057
      3. Dog bark: -0.820604
   Top-3 predictions for window 5:
      1. Children playing: 1.846359
      2. Dog bark: 1.025755
      3. Engine idling: 0.410302
   Top-3 predictions for window 6:
      1. Children playing: 2.051510
      2. Dog bark: 1.025755
      3. Engine idling: 0.820604
   Got EOS from element "pipeline0".
   Execution ended after 0:00:00.338050160
   Setting pipeline to NULL ...
   Freeing pipeline ...

Troubleshooting
---------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Symptom
     - Action
   * - ``Failed to load class-map-path``
     - Check the path, and that the file is readable.
   * - Banner prints but no predictions appear
     - Run with ``GST_DEBUG=titvm:5``. Check that the pipeline reached PLAYING.
   * - Predictions do not match the expected labels
     - Check that the model and label file are a pair: YAMNet with ``yamnet_label_list.txt``,
       VGGish with ``vggish_label_list.txt``.
   * - ``top-k`` rejected
     - Use a value from 1 to 521.
   * - Long wait before banner prints
     - ``titvm`` is waiting for the model daemon. Start it or accept the in-process load time.
