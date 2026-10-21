.. _pub_edgeai_am62dx_getting_started:

==============================
How to run GStreamer Pipelines
==============================

The two GStreamer elements, ``tidspkernel`` and ``titvm``, that
offload audio signal processing and neural-network inference to the C7x DSP on
|__PART_FAMILY_NAME__|. With them you can build a standard ``gst-launch-1.0`` pipeline that
reads a WAV file, runs it through a speech-enhancement or audio-classification model on the
DSP, and writes or prints the result — without writing any DSP-side code yourself.

This section takes you from a bare board to a working pipeline: what must already be
installed, how to build and install the plugins if they are not, how to confirm everything is
in place, and then two ready-to-run pipelines — speech enhancement and audio event
classification — that you can use as-is or adapt to your own model.

Prerequisites
=============

The EdgeAI AM62D image already has everything in this table.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Component
     - Notes
   * - C7x DSP firmware
     - Must be running. Check with ``cat /sys/class/remoteproc/remoteproc*/state``.
   * - ``libti_rpmsg_dma``
     - RPMsg and DMA client library.
   * - TVM runtime
     - ``libtvm_runtime.so`` and a ``tvm.pc`` in the pkgconfig path.
   * - json-c
     - Used by ``titvm`` to parse ``deploy_graph.json``.
   * - GStreamer Plugins
     - ``libgstti.so`` in ``/usr/lib/gstreamer-1.0/``. It contains ``tidspkernel``, ``titvm``
       and the RPMsg channel helper.
   * - TVM Model artifacts and JSON files
     - Under ``/usr/share/tvm_inference/``.

Model Artifacts and Labels
--------------------------

The SDK ships pre-compiled artifacts for the three reference models used throughout this
guide, so users can run a pipeline immediately without compiling anything yourself. To use custom
model instead, see :ref:`pub_edgeai_am62dx_byom`.

**Model Directories** — Under ``/usr/share/tvm_inference/artifacts/``:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - Model
     - Path
     - Purpose
   * - ``gcrn``
     - ``/usr/share/tvm_inference/artifacts/gcrn/``
     - Speech enhancement
   * - ``yamnet``
     - ``/usr/share/tvm_inference/artifacts/yamnet/``
     - 521-class audio event classification
   * - ``vggish``
     - ``/usr/share/tvm_inference/artifacts/vggish/``
     - 10-class audio classification

Each model directory must contain:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - File
     - Description
   * - ``deploy_graph.json``
     - Graph description; defines the neural network topology
   * - ``deploy_lib.so``
     - Compiled model library; shared object for TVM runtime
   * - ``deploy_param.params``
     - Model weights; binary parameter data

**Label Files** — Under ``/usr/share/tvm_inference/labels/``:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - File
     - Description
   * - ``yamnet_label_list.txt``
     - 521 lines; one AudioSet class name per line for YAMNet model
   * - ``vggish_label_list.txt``
     - 10 lines; one UrbanSound8K class name per line for VGGish model

**Sample Input Files** — Under ``/usr/share/tvm_inference/input/``:

Pre-recorded sample audio files in the correct format (16 kHz, mono, 16-bit PCM WAV) for testing pipelines.

.. note::

   Every pipeline in this guide expects 16 kHz, mono, signed 16-bit PCM WAV.
   Sample files in this format are already on the board under
   ``/usr/share/tvm_inference/input/``, so users can try the pipelines before
   converting any audio of your own.

   If your source audio is a different rate, channel count or sample format, convert it once
   ahead of time with ffmpeg:

   .. code-block:: bash

      ffmpeg -i input.wav -ar 16000 -ac 1 -sample_fmt s16 output_16k.wav

Building and Installing GST Plugins on the EVM
==============================================

The steps below build natively on the board. For a host cross-build, see
`edgeai-gst-plugins <https://github.com/TexasInstruments/edgeai-gst-plugins#cross-compiling-the-project>`__.

.. code-block:: bash

   git clone https://github.com/TexasInstruments/edgeai-gst-plugins.git
   cd edgeai-gst-plugins
   export SOC=am62d
   meson setup build --prefix=/usr -Dpkg_config_path=pkgconfig \
     -Dtvm-plugins=enabled -Dstft-plugins=enabled \
     -Ddl-plugins=disabled -Denable-tidl=disabled
   ninja -C build
   sudo ninja -C build install
   sudo ldconfig

.. _pub_edgeai_am62dx_cross_build:

Verifying the Installation
==========================

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
   * - ``c7x_client_open() failed — is the c7x_compute firmware running?``
     - The C7x firmware is not running. Check ``/sys/class/remoteproc/remoteproc*/state``.
   * - ``DMA heap alloc failed``
     - Not enough contiguous memory for the model. Reboot and retry, then check ``/proc/meminfo``.
   * - ``TI-Offload exchange failed`` or ``DSP kernel failed: remote status=``
     - The DSP firmware does not match the plugin. Check the firmware version.
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

Commands
--------

How to run GStreamer based YAMNet Audio Classification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. _pub_edgeai_am62dx_byom:

Bring-Your-Own Model
=====================

The three reference pipelines above use pre-trained, pre-compiled models so you can see the
plugins working immediately. Most production use cases, though, need a model trained on your
own data — your own set of sound events, or a speech-enhancement model tuned to your product's
microphone and acoustic environment. This section covers what it takes to run such a model
through ``tidspkernel`` and ``titvm`` once it has been compiled for the AM62Dx C7x DSP.

Compiling the model itself — taking an ONNX graph through quantization and generating
``deploy_graph.json``, ``deploy_lib.so`` and ``deploy_param.params`` — is covered separately in
:ref:`Model Compile and Evaluate <audioai-compile-evaluate>`. This section assumes you already
have those three artifacts and focuses on wiring them into a GStreamer pipeline.

Requirements:
--------------

A compiled model directory with the same three files the reference models use:

.. code-block:: text

   my_model/
   ├── deploy_graph.json     graph description; input/output shapes read from attrs.shape
   ├── deploy_lib.so         compiled model library
   └── deploy_param.params   model weights

Beyond these files, you must specify two critical model properties that the plugins cannot
auto-detect:

- **Task type**: whether the model performs speech enhancement (like GCRN) or classification
  (like YAMNet/VGGish). This determines which pipeline you should adapt.
- **Spectral layout**: the FFT size, hop size, and window length the model was trained with,
  plus the number of spectral coefficients per frame that the DSP firmware must produce.

Example: A New Model
----------------------

Suppose you have a new model with a unique architecture and spectral front-end, and firmware
ModelId ``5`` has already been added to support it. To use it in a GStreamer pipeline, follow
the same pattern as the YAMNet/VGGish examples above, but explicitly set all spectral properties
instead of relying on path-based auto-detection:

.. code-block:: bash

   MODEL=/path/to/my_model
   gst-launch-1.0 -v filesrc location=$INPUT ! \
     wavparse ! audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
     tidspkernel name=stft msg-type=0x1020 model-path=$MODEL \
       selected-model=5 model-elems=128 hop-size=160 fft-size=256 \
       window-frames=100 batch-size=64 ! \
     titvm model-path=$MODEL \
       class-map-path=/path/to/my_model/labels.txt top-k=3 ! \
     fakesink

This command uses the same approach as the reference models — the difference is that all spectral
parameters (``selected-model``, ``model-elems``, ``fft-size``, ``hop-size``, ``window-frames``)
are now explicitly set for your model rather than auto-detected from the path. Only ``model-path``
changes between your custom model and the reference implementations. The ``titvm`` element requires
no modifications beyond ``model-path`` — it automatically loads and runs whatever TVM artifacts
(``deploy_graph.json``, ``deploy_lib.so``, ``deploy_param.params``) it finds in that directory.

For a speech-enhancement model with a new architecture, use the same approach: build your pipeline
with the ``deinterleave`` → ``tidspkernel`` (STFT) → ``titvm`` → ``interleave`` → ``tidspkernel``
(ISTFT) chain from the GCRN reference pipeline, then set the ``tidspkernel`` properties to match
your model's spectral layout instead of GCRN's.

Supporting New Model Architectures in the Plugins
---------------------------------------------------

If your model introduces a new architecture or spectral processing scheme not covered by existing
firmware ModelIds (0=DCCRN, 1=GTCRN, 2=GCRN, 3=VGGish, 4=YAMNet), the DSP firmware must first
add support for that new ModelId. Once the firmware is updated, the GStreamer plugins can
immediately wire it in by setting the ``selected-model`` property to the new firmware ID.

However, if you need to extend the plugins themselves to better support a new model category
or add automatic detection logic, the following sections show the code you would modify in the
GStreamer plugin source files.

Adding a New GStreamer Property to ``tidspkernel``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your new model requires an additional configuration parameter (for example, a
``model-specific-param`` flag), add it to the plugin header and implementation:

**1. Header: ``gstdspkernel.h`` - Add to the struct:**

.. code-block:: c

   struct _GstDspKernel
   {
     /* ... existing properties ... */
     guint fft_size;
     guint window_frames;
     guint selected_model;
     guint model_elems;

     /* NEW: Add your custom property */
     guint model_specific_param;  /* New parameter for custom model */
   };

**2. Implementation: ``gstdspkernel.cpp`` - Add property enum:**

.. code-block:: c

   /* Property IDs */
   enum
   {
     PROP_0,
     PROP_MSG_TYPE,
     PROP_INTERLEAVE_DIRECTION,
     PROP_HOP_SIZE,
     PROP_FFT_SIZE,
     PROP_WINDOW_FRAMES,
     PROP_BATCH_SIZE,
     PROP_SELECTED_MODEL,
     PROP_MODEL_ELEMS,
     PROP_MODEL_PATH,
     PROP_OVERLAP_FRAMES,
     PROP_CHUNKING_MODE,
     PROP_MAX_STREAM_SAMPLES,

     /* NEW: Add your property ID */
     PROP_MODEL_SPECIFIC_PARAM
   };

**3. Register the property in ``class_init()``:**

.. code-block:: c

   g_object_class_install_property (gobject_class, PROP_MODEL_SPECIFIC_PARAM,
       g_param_spec_uint ("model-specific-param", "Model Specific Param",
           "Custom parameter for new model architecture (e.g., preprocessing mode: 0=default, 1=legacy)",
           0, 255, 0,  /* min, max, default */
           (GParamFlags) (G_PARAM_READWRITE | G_PARAM_STATIC_STRINGS)));

**4. Add getter/setter in ``set_property()`` and ``get_property()``:**

.. code-block:: c

   static void
   gst_dsp_kernel_set_property (GObject * object, guint prop_id,
       const GValue * value, GParamSpec * pspec)
   {
     GstDspKernel *kernel = GST_DSP_KERNEL (object);

     switch (prop_id) {
       /* ... existing properties ... */
       case PROP_MAX_STREAM_SAMPLES:
         kernel->max_stream_samples = g_value_get_uint (value);
         break;

       /* NEW: Handle your property */
       case PROP_MODEL_SPECIFIC_PARAM:
         kernel->model_specific_param = g_value_get_uint (value);
         GST_DEBUG_OBJECT (kernel, "Set model_specific_param=%u",
             kernel->model_specific_param);
         break;

       default:
         G_OBJECT_WARN_INVALID_PROPERTY_ID (object, prop_id, pspec);
         break;
     }
   }

   static void
   gst_dsp_kernel_get_property (GObject * object, guint prop_id,
       GValue * value, GParamSpec * pspec)
   {
     GstDspKernel *kernel = GST_DSP_KERNEL (object);

     switch (prop_id) {
       /* ... existing properties ... */

       /* NEW: Return your property */
       case PROP_MODEL_SPECIFIC_PARAM:
         g_value_set_uint (value, kernel->model_specific_param);
         break;

       default:
         G_OBJECT_WARN_INVALID_PROPERTY_ID (object, prop_id, pspec);
         break;
     }
   }

**5. Use the property in DSP request:**

In the ``transform_ip()`` or data processing function, send the parameter to the DSP firmware:

.. code-block:: c

   struct dsp_stft_params params = {
     .selected_model = kernel->selected_model,
     .input_frame = kernel->hop_size,
     .output_frame = kernel->hop_size,
     /* NEW: Include your custom parameter in firmware request if needed */
   };

   /* Optionally add metadata to request or logging */
   GST_DEBUG_OBJECT (kernel,
       "Sending STFT request: selected_model=%u, model_specific_param=%u",
       kernel->selected_model, kernel->model_specific_param);


Adding a New Property to ``titvm``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Similarly, for the TVM inference element, if you need a new parameter (for example,
``inference-threshold`` for filtering low-confidence predictions):

**1. Header: ``gsttitvm.h`` - Add to struct:**

.. code-block:: c

   struct _GstTiTvm
   {
     /* ... existing properties ... */
     gchar *model_path;
     gchar *class_map_path;
     guint top_k;
     guint daemon_timeout_ms;

     /* NEW: Add your custom property */
     gfloat inference_threshold;  /* Confidence threshold (0.0-1.0) */
   };

**2. Implementation: ``gsttitvm.cpp`` - Add property enum and register:**

.. code-block:: c

   enum
   {
     PROP_0,
     PROP_MODEL_PATH,
     PROP_CLASS_MAP_PATH,
     PROP_TOP_K,
     PROP_DAEMON_TIMEOUT_MS,

     /* NEW: Add your property ID */
     PROP_INFERENCE_THRESHOLD
   };

   /* In class_init() */
   g_object_class_install_property (gobject_class, PROP_INFERENCE_THRESHOLD,
       g_param_spec_float ("inference-threshold", "Inference Threshold",
           "Minimum confidence score to report predictions (0.0-1.0)",
           0.0f, 1.0f, 0.5f,  /* min, max, default */
           (GParamFlags) (G_PARAM_READWRITE | G_PARAM_STATIC_STRINGS)));

**3. Use in inference post-processing:**

.. code-block:: c

   /* After getting inference output from TVM, filter by threshold */
   for (guint i = 0; i < output_size; ++i) {
     gfloat confidence = output_buffer[i];

     if (confidence >= tvm->inference_threshold) {
       /* Report this prediction */
       GST_DEBUG_OBJECT (tvm, "Prediction %u: confidence=%.3f (above threshold %.3f)",
           i, confidence, tvm->inference_threshold);
     }
   }


Automatic Model Detection from Path
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want the plugins to auto-detect your new model based on its directory path name,
add a mapping in the model detection logic:

**In ``gstdspkernel.cpp``:**

.. code-block:: c

   /* Existing model detection table */
   struct {
     const gchar *path_substring;
     guint selected_model;
     guint model_elems;
     guint fft_size;
     guint hop_size;
     guint window_frames;
   } known_models[] = {
     { "gcrn", 2, 322, 320, 160, 401 },
     { "gtcrn", 1, 322, 320, 160, 401 },
     { "dccrn", 0, 322, 320, 160, 401 },
     { "yamnet", 4, 64, 512, 160, 96 },
     { "vggish", 3, 128, 512, 160, 96 },

     /* NEW: Add your model */
     { "my_custom_model", 5, 256, 512, 256, 100 },

     { NULL, 0, 0, 0, 0, 0 }  /* Sentinel */
   };

   /* Auto-detection function (called in set_property and state_change) */
   static gboolean
   gst_dsp_kernel_detect_model (GstDspKernel * kernel)
   {
     for (guint i = 0; known_models[i].path_substring != NULL; ++i) {
       if (kernel->model_path &&
           g_strrstr (kernel->model_path, known_models[i].path_substring)) {
         kernel->selected_model = known_models[i].selected_model;
         kernel->model_elems = known_models[i].model_elems;
         kernel->fft_size = known_models[i].fft_size;
         kernel->hop_size = known_models[i].hop_size;
         kernel->window_frames = known_models[i].window_frames;

         GST_INFO_OBJECT (kernel,
             "Auto-detected model from path '%s': selected-model=%u",
             kernel->model_path, kernel->selected_model);
         return TRUE;
       }
     }
     return FALSE;
   }

Example: Using a New Model with Extended Plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you rebuild the plugin with your new properties, use them in a GStreamer command:

.. code-block:: bash

   gst-launch-1.0 -v filesrc location=input.wav ! wavparse ! \
     audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
     tidspkernel name=stft msg-type=0x1020 model-path=/path/to/my_custom_model \
       selected-model=5 model-elems=256 hop-size=256 fft-size=512 \
       window-frames=100 \
       model-specific-param=1 ! \
     titvm model-path=/path/to/my_custom_model \
       class-map-path=/path/to/my_custom_model/labels.txt top-k=3 \
       inference-threshold=0.7 ! \
     fakesink

