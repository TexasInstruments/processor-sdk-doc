.. _pub_edgeai_am62dx_getting_started:

========================
Audio AI Using GStreamer
========================

The two GStreamer elements, ``tidspkernel`` and ``titvm``, that
offload audio signal processing and neural-network inference to the C7x DSP on
|__PART_FAMILY_NAME__|. With them you can build a standard ``gst-launch-1.0`` pipeline that
reads a WAV file, runs it through a speech-enhancement or audio-classification model on the
DSP, and writes or prints the result — without writing any DSP-side code yourself.

This section takes you from a bare board to a working pipeline: what must already be
installed, how to build and install the plugins if they are not, how to confirm everything is
in place, and then two ready-to-run pipelines — speech enhancement and audio event
classification — that you can use as-is or adapt to your own model.

Requirements
============

A standard AM62D EdgeAI image already has everything in this table.
Check each item once before your first pipeline run.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Component
     - Notes
   * - C7x DSP firmware
     - Must be running. Check with ``cat /sys/class/remoteproc/remoteproc*/state``.
       The firmware must provide the TI-Offload generic service that ``tidspkernel`` uses.
   * - ``libti_rpmsg_dma``
     - RPMsg and DMA client library.
   * - TVM runtime
     - ``libtvm_runtime.so`` and a ``tvm.pc`` in the pkgconfig path.
   * - json-c
     - Used by ``titvm`` to parse ``deploy_graph.json``.
   * - GStreamer 1.0
     - ``gstreamer``, ``gst-plugins-base`` (including allocators) and ``gst-inspect-1.0``.
   * - Plugins
     - ``libgstti.so`` in ``/usr/lib/gstreamer-1.0/``. It contains ``tidspkernel``, ``titvm``
       and the RPMsg channel helper.
   * - Model artifacts
     - Under ``/usr/share/tvm_inference/``. See :ref:`pub_edgeai_am62dx_model_artifacts`.

Building on the Board
=====================

The steps below build natively on the board. For a host cross-build, see
:ref:`pub_edgeai_am62dx_cross_build`.

Build and install the plugins
-------------------------------------

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

Cross-Building on a Host
------------------------

Build on a host with the SDK toolchain, following the cross-compile steps in the
`edgeai-gst-plugins <https://github.com/TexasInstruments/edgeai-gst-plugins#cross-compiling-the-project>`__
README. Install into the SDK target filesystem with ``DESTDIR``,
then copy the libraries and headers to the board.

Verifying the Installation
==========================

.. code-block:: bash

   gst-inspect-1.0 tidspkernel
   gst-inspect-1.0 titvm

Both commands must print the element details. If an element is missing, check that
``/usr/lib/gstreamer-1.0/libgstti.so`` exists and that ``ldconfig`` has run.

.. _pub_edgeai_am62dx_model_artifacts:

Model Artifacts and Labels
==========================

The SDK ships pre-compiled artifacts for the three reference models used throughout this
guide, so users can run a pipeline immediately without compiling anything yourself. To use custom
model instead, see :ref:`pub_edgeai_am62dx_byom`.

Model directories are under ``/usr/share/tvm_inference/artifacts/``:

- ``gcrn``: speech enhancement
- ``yamnet``: 521-class audio event classification
- ``vggish``: 10-class audio classification

Each model directory must contain:

.. code-block:: text

   deploy_graph.json     graph description;
   deploy_lib.so         compiled model library
   deploy_param.params   model weights

Label files are under ``/usr/share/tvm_inference/labels/``:

- ``yamnet_label_list.txt``: 521 lines, one class name per line
- ``vggish_label_list.txt``: 10 lines, one class name per line

Sample input files are under ``/usr/share/tvm_inference/input/``.

Input Audio
===========

Every pipeline in this guide expects 16 kHz, mono, signed 16-bit PCM WAV.
Sample files in this format are already on the board under
``/usr/share/tvm_inference/input/``, so users can try the pipelines before
converting any audio of your own.

If your source audio is a different rate, channel count or sample format, convert it once
ahead of time with ffmpeg:

.. code-block:: bash

   ffmpeg -i input.wav -ar 16000 -ac 1 -sample_fmt s16 output_16k.wav

Or convert it inline, inside the pipeline itself, by inserting ``audioconvert`` and
``audioresample`` before the ``audio/x-raw`` capsfilter that pins the format:

.. code-block:: bash

   filesrc location=input_44k.wav ! wavparse ! \
     audioconvert ! audioresample ! \
     audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
     ... rest of the pipeline


GStreamer Pipelines
===================

.. _pub_edgeai_am62dx_gst_pipelines:

The pipelines split work between the ARM core and the C7x DSP:

- **ARM core**: runs GStreamer, reads and writes files, and drives the pipeline.
- **C7x DSP**: runs the STFT, ISTFT and deinterleave/interleave kernels of ``tidspkernel``.
- **TVM runtime**: runs the neural network models of ``titvm``. See
  :ref:`pub_edgeai_am62dx_titvm_execution` for where it runs.
- **RPMsg**: the command channel between the ARM core and the DSP.
- **DMA-BUF**: buffers shared with the DSP, so data is copied only where the pipeline needs it.

Pipelines Shipped with the Plugins
-----------------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Pipeline
     - Model and input
     - Output
   * - Speech enhancement
     - ``gcrn``, ``input_audio.wav``
     - Enhanced WAV file, optionally played back
   * - Audio event classification
     - ``yamnet``, ``urbansound_16k.wav``
     - Top-k class names and scores printed to the console
   * - Audio classification
     - ``vggish``, ``urbansound_16k.wav``
     - Top-k class names and scores printed to the console

See :ref:`pub_edgeai_am62dx_audio_enhancement` and
:ref:`pub_edgeai_am62dx_audio_classification` for the commands and the stage details.

Data Flow
---------

Speech enhancement uses the full chain of DSP and model stages:

.. code-block:: text

   filesrc → wavparse → caps (S16LE, 16 kHz, mono)
     → tidspkernel stft (0x1020)           DSP: time to spectrum
     → tidspkernel deinterleave (0x1040)   DSP: split real/imaginary
     → titvm gcrn                          model
     → tidspkernel interleave (0x1040)     DSP: recombine real/imaginary
     → tidspkernel istft (0x1030)          DSP: spectrum to time
     → caps (S16LE, 16 kHz, mono) → wavenc → filesink

Classification uses the STFT stage and then the model:

.. code-block:: text

   filesrc → wavparse → caps (S16LE, 16 kHz, mono)
     → tidspkernel stft (0x1020)           DSP
     → titvm yamnet (or vggish)            model
     → fakesink


The properties of each element are listed in :ref:`pub_edgeai_am62dx_pipeline_elements`.

.. _pub_edgeai_am62dx_audio_enhancement:

GCRN based Audio Enhancement
=============================

Speech enhancement removes background noise from a recording while keeping the speech
intelligible — useful for voice calls, meeting recordings, hearables, and any product that
captures speech in a noisy environment. This pipeline runs that enhancement end to end on the
board: it reads a 16 kHz mono WAV file, converts it to the frequency domain on the DSP, runs
the GCRN model on the result, and converts the enhanced spectrum back to audio you can play or
save.

Pipeline Stages
---------------

.. code-block:: text

   filesrc → wavparse → audio/x-raw (S16LE, 16 kHz, mono)
     → tidspkernel name=stft         msg-type=0x1020   STFT
     → tidspkernel name=deinterleave msg-type=0x1040   interleave_direction=0
     → titvm                         model-path=.../gcrn
     → tidspkernel name=interleave   msg-type=0x1040   interleave_direction=1
     → tidspkernel name=istft        msg-type=0x1030   ISTFT
     → audio/x-raw (S16LE, 16 kHz, mono) → tee
           → wavenc → filesink       (WAV file)
           → autoaudiosink           (playback)

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Stage
     - Runs on
     - What it does
   * - ``stft``
     - C7x DSP
     - Converts 16-bit PCM to complex spectral frames. FFT size 320, hop 160 samples,
       401 frames per window, 64 frames per DSP request.
   * - ``deinterleave``
     - C7x DSP
     - Splits the spectral frames into real and imaginary parts for the model.
   * - ``titvm``
     - Model daemon or in-process TVM runtime
     - Runs the GCRN graph. Input and output shape are read from ``deploy_graph.json``
       (``[1, 2, 401, 161]``).
   * - ``interleave``
     - C7x DSP
     - Recombines the real and imaginary parts into the layout ISTFT expects.
   * - ``istft``
     - C7x DSP
     - Converts the enhanced spectrum back to 16-bit PCM.

.. _pub_edgeai_am62dx_enhancement_command:

GCRN GStreamer Command
-----------------------

Execute the following command to run the Audio Enhancement pipeline. It
writes ``/tmp/gst_enhanced.wav`` and plays the same output through ``autoaudiosink``.
Connect headphone to the AM62D EVM to listen to the enhanced audio.

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

Running the Pipeline
--------------------

1. Check the input and the model:

   .. code-block:: bash

      ls -l /usr/share/tvm_inference/input/input_audio.wav
      ls /usr/share/tvm_inference/artifacts/gcrn/

2. Check that the DSP is running:

   .. code-block:: bash

      cat /sys/class/remoteproc/remoteproc*/state

3. Run the command from :ref:`Command <pub_edgeai_am62dx_enhancement_command>`.

4. Check the output:

   .. code-block:: bash

      ls -lh /tmp/gst_enhanced.wav

The model stage prints the shapes it read from ``deploy_graph.json``:

.. code-block:: text

   [TVM] Auto-detected input shape: [1,2,401,161]
   [TVM] Auto-detected output shape: [1,2,401,161]
   [TVM] Output element count known up front from deploy_graph.json: 129122 floats

Startup Time
^^^^^^^^^^^^

``titvm`` first tries the model daemon at ``/var/run/tvm-inference.sock``. If the daemon
does not answer, it waits up to ``daemon-timeout-ms`` (30 seconds by default) before
loading the model in-process. Start the daemon before running the pipeline to avoid that
wait. See :ref:`pub_edgeai_am62dx_titvm_execution`.

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

Models
------

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Model
     - Classes
     - Label file
   * - YAMNet
     - 521
     - ``/usr/share/tvm_inference/labels/yamnet_label_list.txt``
   * - VGGish
     - 10
     - ``/usr/share/tvm_inference/labels/vggish_label_list.txt``


Pipeline Stages
---------------

.. code-block:: text

   filesrc → wavparse → audio/x-raw (S16LE, 16 kHz, mono)
     → tidspkernel name=stft msg-type=0x1020   STFT on the DSP
     → titvm model-path=.../yamnet (or vggish) model
     → fakesink


Commands
--------

YAMNet
^^^^^^

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

VGGish
^^^^^^

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


Output Format
-------------

When ``class-map-path`` is set, ``titvm`` prints a banner when the model loads, then one block
per window:

.. code-block:: text

   [TVM] Live top-3 prediction printing enabled (521 classes from /usr/share/tvm_inference/labels/yamnet_label_list.txt)
     Top-3 predictions for window 1:
       1. <class name>: <score>
       2. <class name>: <score>
       3. <class name>: <score>


Options
-------

``top-k``
  Number of predictions printed per window. Range 1 to 521, default 3.

``class-map-path``
  Label file. If empty, ``titvm`` does not print predictions. The file can be one class name
  per line, or YAML with ``name:`` lines.

Running the Pipeline
--------------------

1. Check the input, model and labels:

   .. code-block:: bash

      ls /usr/share/tvm_inference/input/urbansound_16k.wav
      ls /usr/share/tvm_inference/artifacts/yamnet/
      ls /usr/share/tvm_inference/labels/yamnet_label_list.txt

2. Run one of the commands above. Use ``-v`` to see the caps negotiation.

3. Read the predictions from the console. Use ``fakesink`` as the last element, since the
   output is the console log rather than a file.

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
   * - Long wait before the banner
     - ``titvm`` is waiting for the model daemon. See :ref:`pub_edgeai_am62dx_titvm_execution`.

.. _pub_edgeai_am62dx_pipeline_elements:

Pipeline Elements
=================

The two AM62Dx plugin elements, ``tidspkernel`` and ``titvm``, are built into one library,
``/usr/lib/gstreamer-1.0/libgstti.so``. The standard GStreamer elements used with them are
listed at the end.

tidspkernel
-----------

``tidspkernel`` runs STFT, ISTFT and deinterleave/interleave on the C7x DSP. The operation is
selected by ``msg-type``.

Operations
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 15 25 30 30

   * - ``msg-type``
     - Operation
     - Input
     - Output
   * - ``0x1020``
     - STFT
     - S16LE mono PCM, ``hop-size`` samples per frame
     - ``model-elems`` floats per frame
   * - ``0x1030``
     - ISTFT
     - ``model-elems`` floats per frame
     - S16LE mono PCM, ``hop-size`` samples per frame
   * - ``0x1040``
     - Deinterleave or interleave
     - ``2 x window-frames x (fft-size/2+1)`` floats
     - Same size, reordered. ``interleave-direction`` selects 0 (deinterleave) or 1 (interleave).

If ``msg-type`` is not set, the element picks the operation from its name. The name must end
with ``stft``, ``istft``, ``deinterleave`` or ``interleave``.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 22 12 14 52

   * - Property
     - Type
     - Default
     - Meaning
   * - ``msg-type``
     - uint
     - 0
     - Operation. See the table above.
   * - ``fft-size``
     - uint
     - 0
     - FFT length in samples. Sets the bin count for deinterleave/interleave, and sets
       ``model-elems`` when no known model matches. The STFT and ISTFT requests do not send it.
   * - ``hop-size``
     - uint
     - 0
     - Samples per frame. Needed for STFT and ISTFT.
   * - ``window-frames``
     - uint
     - 0
     - Frames per window. Values above 256 turn on overlap-save chunking.
   * - ``batch-size``
     - uint
     - 0
     - Frames per DSP request. 0 uses ``window-frames``.
   * - ``chunking-mode``
     - int
     - -1
     - -1 chunks when ``window-frames`` is above 256. 0 never chunks. 1 always chunks.
   * - ``overlap-frames``
     - uint
     - 100
     - Overlap between chunks. Must be less than ``window-frames``.
   * - ``max-stream-samples``
     - uint
     - 0
     - Largest input stream, in samples, for overlap-save chunking. Required when chunking
       is on.
   * - ``model-path``
     - string
     - empty
     - Model directory. Its path is matched against the known-model table below.
   * - ``selected-model``
     - uint
     - 2
     - Firmware ModelId sent with each STFT and ISTFT request. Overwritten by the known-model
       table when ``model-path`` matches.
   * - ``model-elems``
     - uint
     - 0
     - Floats per spectral frame. 0 uses the known-model table, or ``(fft-size/2+1) x 2``.
   * - ``interleave-direction``
     - uint
     - 0
     - For ``msg-type=0x1040``: 0 deinterleave, 1 interleave.


Known-Model Table
^^^^^^^^^^^^^^^^^

``model-path`` is matched, ignoring case, against the directory path. A match sets
``selected-model`` and ``model-elems``.

.. list-table::
   :header-rows: 1
   :widths: 25 25 25

   * - Name in path
     - ``selected-model``
     - ``model-elems``
   * - ``dccrn``
     - 0
     - 514
   * - ``gtcrn``
     - 1
     - 514
   * - ``gcrn``
     - 2
     - 322
   * - ``vggish``
     - 3
     - 64
   * - ``yamnet``
     - 4
     - 64

A path that matches no name keeps the property values. The element logs nothing in that case,
so set ``selected-model`` and ``model-elems`` explicitly for a custom model.

DSP Requests
^^^^^^^^^^^^

``tidspkernel`` sends each request using the TI-Offload generic service, on endpoint 13 of
the C7x DSP (processor ID 8). Each request carries:

- One input and one output buffer, each given by a 64-bit physical address and a size.
- Params:

  - STFT and ISTFT: ``selected_model``, ``input_frame``, ``output_frame``. The two frame counts
    are equal.
  - Deinterleave/interleave: ``input_frame``, ``fft_size``, ``flag``.

The reply carries only a header. The plugin treats the frame count it requested as the frame
count it got back.

titvm
-----

``titvm`` runs a TVM-compiled model. Input and output shapes are read from the model's
``deploy_graph.json``. Each buffer is checked against the input size, and a mismatch is an
error.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 22 12 14 52

   * - Property
     - Type
     - Default
     - Meaning
   * - ``model-path``
     - string
     - empty
     - Directory with ``deploy_graph.json``, ``deploy_lib.so`` and ``deploy_param.params``.
   * - ``class-map-path``
     - string
     - empty
     - Label file. Setting it turns on prediction printing. Empty turns it off.
   * - ``top-k``
     - uint
     - 3
     - Predictions printed per window when ``class-map-path`` is set. Range 1 to 521.
   * - ``daemon-timeout-ms``
     - uint
     - 30000
     - Time allowed for each request and reply with the model daemon, in milliseconds.

Model Directory
^^^^^^^^^^^^^^^

.. code-block:: text

   /usr/share/tvm_inference/artifacts/yamnet/
   ├── deploy_graph.json     graph; input and output shapes are read from attrs.shape
   ├── deploy_lib.so         compiled model library
   └── deploy_param.params   model weights

.. _pub_edgeai_am62dx_titvm_execution:

Execution Path
^^^^^^^^^^^^^^

When the element starts, it first connects to the model daemon at
``/var/run/tvm-inference.sock``. It sends a PING, waits for the reply, then sends the model
path to be loaded.

- **Daemon available:** every inference goes to the daemon.
- **Daemon not available:** the element waits up to ``daemon-timeout-ms``, then loads the model
  in-process. The board log shows the in-process load opens the C7x client
  (``c7x_client_open()``), so the in-process path also needs the C7x firmware running.
- **Daemon fails during inference:** the element returns an error and falls back.

Standard GStreamer Elements Used
---------------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Element
     - Use in these pipelines
   * - ``filesrc``
     - Reads the input file. ``location=`` sets the path.
   * - ``wavparse``
     - Parses a WAV file into PCM.
   * - ``audioconvert`` / ``audioresample``
     - Converts other formats and sample rates to the format the pipeline expects.
   * - ``audio/x-raw`` capsfilter
     - Pins the format, for example ``audio/x-raw,format=S16LE,rate=16000,channels=1``.
   * - ``tee`` and ``queue``
     - Split the stream into branches. Each branch needs its own ``queue``.
   * - ``wavenc`` and ``filesink``
     - Writes a WAV file. ``filesink location=`` sets the path.
   * - ``autoaudiosink``
     - Plays audio through the default output.
   * - ``fakesink``
     - Discards the data. Used for classification, where the output is the console log.

Debugging
---------

.. code-block:: bash

   GST_DEBUG=tidspkernel:6,titvm:6 gst-launch-1.0 -v ...

``tidspkernel`` logs its message type, buffer sizes and each DSP request. ``titvm`` logs the
daemon handshake, the shape it detected, and the model load.

To visualize the pipeline graph itself, rather than its runtime log:

.. code-block:: bash

   mkdir -p /tmp/dot
   GST_DEBUG_DUMP_DOT_DIR=/tmp/dot gst-launch-1.0 ...
   ls /tmp/dot

The graph files are written when the pipeline changes state. Convert them with ``dot`` on a
host machine if the board does not have it.

Batch Processing Multiple Files
================================

The commands so far run on one file at a time. To process a whole directory unattended — for
example, enhancing every recording collected during a test run — script it as a loop over
``gst-launch-1.0`` invocations. The GCRN enhancement pipeline needs ``max-stream-samples`` set
to the padded length of each file, so the script below computes that value per file. It assumes
16 kHz mono 16-bit PCM WAV files with a 44-byte header, which is what the sample files use:

.. code-block:: bash

   #!/bin/bash
   # Enhance every 16 kHz mono S16LE WAV file in IN_DIR and write the results to OUT_DIR.

   IN_DIR=/data/audio
   OUT_DIR=/data/enhanced
   MODEL=/usr/share/tvm_inference/artifacts/gcrn
   FRAMES=401
   OVERLAP=100
   HOP=160
   mkdir -p "$OUT_DIR"

   for f in "$IN_DIR"/*.wav; do
     name=$(basename "$f" .wav)
     bytes=$(stat -c %s "$f")
     n=$(( (bytes - 44) / 2 ))
     chunk=$(( FRAMES * HOP ))
     step=$(( (FRAMES - OVERLAP) * HOP ))
     max=$(awk -v n="$n" -v c="$chunk" -v s="$step" \
       'BEGIN { k = (n > c) ? int((n - c + s - 1) / s) + 1 : 1; print (k - 1) * s + c }')

     gst-launch-1.0 -q filesrc location="$f" ! wavparse ! \
       audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
       tidspkernel name=stft msg-type=0x1020 model-path=$MODEL \
         hop-size=$HOP fft-size=320 window-frames=$FRAMES batch-size=64 \
         max-stream-samples=$max ! \
       tidspkernel name=deinterleave msg-type=0x1040 interleave_direction=0 \
         model-path=$MODEL fft-size=320 window-frames=$FRAMES ! \
       titvm model-path=$MODEL ! \
       tidspkernel name=interleave msg-type=0x1040 interleave_direction=1 \
         model-path=$MODEL fft-size=320 window-frames=$FRAMES ! \
       tidspkernel name=istft msg-type=0x1030 model-path=$MODEL \
         hop-size=$HOP fft-size=320 window-frames=$FRAMES batch-size=64 \
         max-stream-samples=$max ! \
       audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
       wavenc ! filesink location="$OUT_DIR/${name}_enhanced.wav"
   done

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
  (like YAMNet/VGGish). This determines which pipeline shape from the :ref:`pipeline overview
  <pub_edgeai_am62dx_gst_pipelines>` you should adapt.
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

