.. _pub_edgeai_am62dx_getting_started:

#########################
GStreamer Audio Pipelines
#########################

Introduction
============

The GStreamer pipeline framework on AM62DX enables real-time audio AI inference through two custom
plugins: ``tidspkernel`` and ``titvm``. Together, they offload signal processing and neural network
inference to the C7x™ DSP while orchestrating the data flow from Linux. With GStreamer, you can:

- **Build Custom Pipelines** — Compose audio processing chains using standard GStreamer elements
- **DSP Offload** — Offload DSP signal chains (ex: STFT, ISTFT, and deinterleave/interleave) to the C7x™ DSP
- **TVM Inference** — Run TVM-compiled AI models on the C7x™ NPU via the TVM runtime
- **Flexible I/O** — Read from WAV files, live ALSA input, or other GStreamer sources
- **Direct Command-Line Control** — Use :command:`gst-launch-1.0` to quickly test and prototype pipelines

Supported Pipelines
===================

.. list-table::
   :header-rows: 1
   :widths: 30 30 20 20

   * - Pipeline
     - Use Case
     - Default Input
     - Output
   * - Speech enhancement (GCRN)
     - Noise reduction with spectral reconstruction
     - :file:`input_audio.wav`
     - Enhanced WAV file (playback or file)
   * - Audio classification (YAMNet)
     - 521-class audio event detection
     - :file:`urbansound_16k.wav`
     - Top-k class names and scores (console)
   * - Audio classification (VGGish)
     - 10-class environmental sound classification
     - :file:`urbansound_16k.wav`
     - Top-k class names and scores (console)

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
   * - :command:`meson` / :command:`ninja`
     - Build system for GStreamer plugins
   * - ARM cross-compiler
     - Required only for host-side cross-compilation
   * - :command:`pkg-config`
     - Dependency resolution during build


Native Compilation & Installation on AM62D EVM
----------------------------------------------

The plugins are pre-installed on the AM62DX EdgeAI image. If you need to rebuild them
natively on the AM62D EVM, follow the steps below:

.. code-block:: console

   root@am62dxx-evm:~# cd /opt/edgeai-gst-plugins/
   root@am62dxx-evm:/opt/edgeai-gst-plugins# export SOC=am62d
   root@am62dxx-evm:/opt/edgeai-gst-plugins# meson setup build --prefix=/usr -Dpkg_config_path=pkgconfig \
     -Dtvm-plugins=enabled -Dstft-plugins=enabled \
     -Ddl-plugins=disabled -Denable-tidl=disabled
   root@am62dxx-evm:/opt/edgeai-gst-plugins# ninja -C build
   root@am62dxx-evm:/opt/edgeai-gst-plugins# ninja -C build install
   root@am62dxx-evm:/opt/edgeai-gst-plugins# ldconfig

.. note::

   The EdgeAI image includes pre-compiled plugins. These steps are only needed if you're rebuilding the plugins from source with custom modifications.

Verifying the Installation
--------------------------

Execute the following command to verify the ``tidspkernel`` GStreamer plugin is installed:

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

Execute the following command to verify the ``titvm`` GStreamer plugin is installed:

.. code-block:: console

   root@am62dxx-evm:~# gst-inspect-1.0 titvm
   Factory Details:
   Rank                     none (0)
   Long-name                TI TVM Inference
   Klass                    Transform/ML
   Description              TVM inference on TI processors with C7x™ DSP acceleration
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

.. note::

   Both commands must print the element details. If an element is missing, check that
   :file:`/usr/lib/gstreamer-1.0/libgstti.so` exists and that :command:`ldconfig` has run.

.. _pub_edgeai_am62dx_model_artifacts:

GCRN based Speech Enhancement
=============================

Speech enhancement removes background noise from input audio source while keeping the speech
intelligible — useful for voice calls, meeting recordings, hearables, and any product that
captures speech in a noisy environment. This pipeline runs that speech enhancement full
pipeline on the board: it reads a 16 kHz mono WAV file, converts it to the frequency domain on
the DSP, runs the GCRN model on the result, and converts the enhanced spectrum back to audio
which can be played or saved.

.. _pub_edgeai_am62dx_enhancement_command:

Speech Enhancement Pipeline using GCRN
--------------------------------------

Execute the following command to run the speech enhancement pipeline. The command writes :file:`/tmp/gst_enhanced.wav` and plays the enhanced speech output through ``autoaudiosink``. Connect headphones to J3/J4 as directed in :ref:`pub_edgeai_am62dx_evm_setup` to listen to the enhanced speech.

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

To run without audio playback, remove the ``tee`` branch and keep only the file output:

.. code-block:: bash

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
     wavenc ! filesink location=/tmp/gst_enhanced.wav

.. figure:: /images/am62dx/edgeai/pipeline_gcrn.png
   :scale: 75
   :align: center

   GStreamer data-flow for GCRN speech enhancement: input WAV → STFT → GCRN model inference → ISTFT → output WAV + playback

.. _pub_edgeai_am62dx_audio_classification:

YAMNet & VGGish based Audio Classification
==========================================

Audio classification identifies *what* sound is present in input audio source — a siren, glass
breaking, a dog barking, a machine running — rather than transcribing speech. That makes it
useful for acoustic event detection, environmental and industrial sound monitoring, and
safety or anomaly alerts triggered by sound rather than video. This pipeline runs YAMNet or
VGGish on a 16 kHz mono WAV file on the DSP, and prints the top-k predicted classes and their
scores for each analysis window to the console as the pipeline runs.

YAMNet and VGGish differ mainly in scope: YAMNet recognizes 521 general sound classes, while
VGGish is a smaller, 10-class model. Pick YAMNet for broad coverage, or VGGish when you only
need to distinguish a small, fixed set of sounds and want a lighter model.

Audio Classification Pipeline using YAMNet
------------------------------------------

Execute the following command to run GStreamer based YAMNet audio classification pipeline:

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

YAMNet Command Output
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

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

.. figure:: /images/am62dx/edgeai/pipeline_yamnet.png
   :scale: 75
   :align: center

   GStreamer data-flow for YAMNet based audio classification: input WAV → STFT → YAMNet model inference → console output

Audio Classification Pipeline using VGGish
------------------------------------------

Execute the following command to run GStreamer based VGGish audio classification pipeline:

.. code-block:: bash

   gst-launch-1.0 -v filesrc location=/usr/share/tvm_inference/input/urbansound_16k.wav ! \
     wavparse ! audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
     tidspkernel name=stft msg-type=0x1020 \
       model-path=/usr/share/tvm_inference/artifacts/vggish \
       hop-size=512 window-frames=126 batch-size=64 ! \
     titvm model-path=/usr/share/tvm_inference/artifacts/vggish \
       class-map-path=/usr/share/tvm_inference/labels/vggish_label_list.txt \
       top-k=3 ! \
     fakesink

VGGish Command Output
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: text

   Setting pipeline to PAUSED ...
   [TVM] Live top-3 prediction printing enabled (10 classes from /usr/share/tvm_inference/labels/vggish_label_list.txt)
   eptdev = rpmsg-char-8-1295
   Created endpt device rpmsg-char-8-1295, fd = 7 port = 1027
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
      1. Street music: 8.411190
      2. Children playing: 8.206039
      3. Air conditioner: -4.513321
   Got EOS from element "pipeline0".
   Execution ended after 0:00:00.082239915
   Setting pipeline to NULL ...
   Freeing pipeline ...


.. figure:: /images/am62dx/edgeai/pipeline_vggish.png
   :scale: 75
   :align: center

   GStreamer data-flow for VGGish based audio classification: input WAV → STFT → VGGish model inference → console output

Troubleshooting
===============

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Issue
     - Resolution
   * - ``max-stream-samples must be explicitly set (> 0)``
     - Set ``max-stream-samples`` on the STFT element.
   * - ``padded length ... exceeds dma_input capacity``
     - Increase ``max-stream-samples`` to the padded length.
   * - ``Invalid incoming buffer``
     - The input is longer than ``max-stream-samples``. Increase it.
   * - ``Model daemon handshake failed`` followed by a long wait
     - Start the daemon, or accept the in-process load time.
   * - ``c7x_client_open() failed — is the c7x_compute DSP firmware running?``
     - The DSP firmware is not running. Check ``/sys/class/remoteproc/remoteproc0/state``.
       If it shows ``offline``, reboot the evm. After  the reboot,
       rerun ``/sys/class/remoteproc/remoteproc0/state`` it should now show ``running``
   * - ``DMA heap alloc failed``
     - Not enough contiguous memory for the model. Reboot and retry, then check ``/proc/meminfo``.
   * - ``TI-Offload exchange failed`` or ``DSP kernel failed: remote status=``
     - The DSP firmware does not match the plugin. Check the DSP firmware version.
   * - ``Failed to set pipeline to PAUSED``
     - Run again with ``GST_DEBUG=tidspkernel:6,titvm:6`` and check the first error.
   * - ``Failed to load class-map-path``
     - Check the path, and that the file is readable.
   * - Banner prints but no predictions appear
     - Run with ``GST_DEBUG=titvm:5``. Check that the pipeline reached PLAYING.
   * - Predictions do not match the expected labels
     - Check that the model and label file are a pair: YAMNet with :file:`yamnet_label_list.txt`,
       VGGish with :file:`vggish_label_list.txt`.
   * - ``top-k`` rejected
     - Use a value from 1 to 521.
   * - Long wait before banner prints
     - ``titvm`` is waiting for the model daemon. Start it or accept the in-process load time.
