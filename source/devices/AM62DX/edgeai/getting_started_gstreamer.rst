.. _pub_edgeai_am62dx_getting_started:

========================
Audio AI Using GStreamer
========================

This section lists what must be on the board before the GStreamer pipelines run, how to
build and install the plugins, and how to check the installation.

Requirements
============

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

Step 1: Build and install ``libti_rpmsg_dma``
---------------------------------------------

Use the ``offload`` branch. The plugin needs ``ti_rpmsg_rpc_client.h`` and the
``ti_rpmsg_rpc_generic_execute`` symbol from this library:

.. code-block:: bash

   git clone -b offload https://github.com/v-singh1/rpmsg-dma.git
   cd rpmsg-dma/library
   cmake -S . -B build
   cmake --build build
   sudo cmake --install build
   sudo ldconfig

Confirm the install:

.. code-block:: bash

   ls /usr/local/include/ti_rpmsg_rpc_client.h
   nm -D /usr/local/lib64/libti_rpmsg_dma.so | grep ti_rpmsg_rpc_generic_execute

If ``/usr/lib`` already has an older ``libti_rpmsg_dma.so``, the plugin link step picks
that copy up. Replace it with the new build, or the link fails with an undefined reference
to ``ti_rpmsg_rpc_generic_execute``.

Step 2: Build and install the plugins
-------------------------------------

.. code-block:: bash

   git clone -b develop https://github.com/TexasInstruments/edgeai-gst-plugins.git
   cd edgeai-gst-plugins
   export SOC=am62d
   meson setup build --prefix=/usr -Dpkg_config_path=pkgconfig \
     -Dtvm-plugins=enabled -Dstft-plugins=enabled \
     -Ddl-plugins=disabled -Denable-tidl=disabled
   ninja -C build
   sudo ninja -C build install
   sudo ldconfig

Use the branch that contains the TI-Offload change for ``tidspkernel``. That change is not
yet merged into ``develop``, so check the release notes for the version to install.

``SOC`` must be exported in the same shell. ``tvm-plugins`` and ``stft-plugins`` are only
accepted when ``SOC=am62d``.

Step 3: Refresh the GStreamer registry
--------------------------------------

.. code-block:: bash

   rm -rf ~/.cache/gstreamer-1.0/registry.aarch64.bin

.. _pub_edgeai_am62dx_cross_build:

Cross-Building on a Host
------------------------

Build on a host with the SDK toolchain, following the cross-compile steps in the
``edgeai-gst-plugins`` README. Install into the SDK target filesystem with ``DESTDIR``,
then copy the libraries and headers to the board. Run ``ldconfig`` and step 3 on the board.
The board's glibc and GStreamer versions must match the SDK.

Verifying the Installation
==========================

.. code-block:: bash

   gst-inspect-1.0 tidspkernel
   gst-inspect-1.0 titvm

Both commands must print the element details. If an element is missing, check that
``/usr/lib/gstreamer-1.0/libgstti.so`` exists and that ``ldconfig`` has run.

Check the DSP:

.. code-block:: bash

   cat /sys/class/remoteproc/remoteproc*/name
   cat /sys/class/remoteproc/remoteproc*/state
   ls -l /dev/rpmsg*

The C7x remote processor must report ``running``.

.. _pub_edgeai_am62dx_model_artifacts:

Model Artifacts and Labels
==========================

Model directories are under ``/usr/share/tvm_inference/artifacts/``:

- ``gcrn``: speech enhancement
- ``yamnet``: 521-class audio event classification
- ``vggish``: 10-class audio classification

Each model directory must contain:

.. code-block:: text

   deploy_graph.json     graph description; input and output shapes are read from here
   deploy_lib.so         compiled model library
   deploy_param.params   model weights

Label files are under ``/usr/share/tvm_inference/labels/``:

- ``yamnet_label_list.txt``: 521 lines, one class name per line
- ``vggish_label_list.txt``: 10 lines, one class name per line

Sample input files are under ``/usr/share/tvm_inference/input/``.

Input Audio
===========

The pipelines expect 16 kHz, mono, signed 16-bit PCM WAV. Convert other files with ffmpeg:

.. code-block:: bash

   ffmpeg -i input.wav -ar 16000 -ac 1 -sample_fmt s16 output_16k.wav

Or put ``audioconvert ! audioresample`` before the ``audio/x-raw`` capsfilter in the pipeline.

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

Each stage's output size must equal the next stage's expected input size. The shape of
the model input is read from ``deploy_graph.json``.

Basic Syntax
------------

.. code-block:: bash

   gst-launch-1.0 [-v] element1 property=value ! element2 property=value ! ...

- ``!`` connects the output of the element on its left to the input of the element on its right.
- ``name=`` gives an element a name so later stages can reference it.
- Caps filters such as ``audio/x-raw,format=S16LE,rate=16000,channels=1`` restrict the format
  between two elements.
- Use ``-v`` to print negotiated caps.

The properties of each element are listed in :ref:`pub_edgeai_am62dx_pipeline_elements`.

.. _pub_edgeai_am62dx_audio_enhancement:

Audio Enhancement
=================

The speech enhancement pipeline runs the GCRN model on a 16 kHz mono WAV file. It converts
the audio to the frequency domain on the DSP, runs the model, and converts the result back
to audio.

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

Command
-------

The command below is the one that runs in ``/opt/edgeai-gst-plugins/pipeline.sh``. It
writes ``/tmp/gst_enhanced.wav`` and plays the same output through ``autoaudiosink``:

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

Why ``max-stream-samples`` Is Required
---------------------------------------

``window-frames=401`` is above the 256-frame threshold, so the STFT stage uses
overlap-save chunking. The whole stream is collected in DSP memory before processing, and
``max-stream-samples`` sets how much memory is reserved. If it is missing or too small, the
pipeline fails at start-up or at end of stream.

The minimum value is the padded length of the input:

.. code-block:: text

   chunk_samples = window-frames x hop-size                    = 401 x 160 = 64160
   hop_samples   = (window-frames - overlap-frames) x hop-size = (401 - 100) x 160 = 48160
   n_chunks      = 1 + ceil((N - chunk_samples) / hop_samples)
   padded        = (n_chunks - 1) x hop_samples + chunk_samples

For the 156302-sample ``input_audio.wav`` (N = 156302), ``n_chunks`` is 3 and the padded
length is 160480. Set ``max-stream-samples`` to at least that value.

``overlap-frames`` defaults to 100. The output is trimmed back to the input length.

For a different input file, compute the padded length with the same formula and set
``max-stream-samples`` on both the STFT and ISTFT elements, as the command above does.

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
     - Set ``max-stream-samples`` on the STFT element, using the padded length above.
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

Audio Classification
====================

The classification pipelines run YAMNet or VGGish on a 16 kHz mono WAV file and print the
top-k class names and scores for each window to the console.

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

The VGGish label file contains: Air conditioner, Car horn, Children playing, Dog bark,
Drilling, Engine idling, Gun shot, Jackhammer, Siren, Street music.

The YAMNet label file starts with ``Speech`` (line 1), ``Child speech, kid speaking`` (line 2)
and includes ``Dog`` at line 70.

Pipeline Stages
---------------

.. code-block:: text

   filesrc → wavparse → audio/x-raw (S16LE, 16 kHz, mono)
     → tidspkernel name=stft msg-type=0x1020   STFT on the DSP
     → titvm model-path=.../yamnet (or vggish) model
     → fakesink

The STFT output goes straight to ``titvm``. There is no separate mel-spectrogram element in
these pipelines. If a model needs mel features, that processing must be part of the model
graph. This has not been checked against the YAMNet and VGGish graphs.

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

Both commands omit ``fft-size``. The STFT request does not send an FFT size to the DSP, and
the known-model table sets ``selected-model`` and ``model-elems`` from the path name
(``yamnet`` → ModelId 4, 64 elements per frame; ``vggish`` → ModelId 3, 64 elements per frame).

STFT Settings
-------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 20 40

   * - Model
     - ``hop-size``
     - ``window-frames``
     - ``batch-size``
   * - YAMNet
     - 160
     - 96
     - 64
   * - VGGish
     - 160
     - 126
     - 64

``window-frames`` is at most 256 for both models, so plain windowing is used and
``max-stream-samples`` is not needed.

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

The class count in the banner comes from the label file (521 for YAMNet, 10 for VGGish).
Scores are printed exactly as the model graph produces them. Whether they are probabilities
or logits depends on the model graph and has not been checked for these two models.

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
     - 0 (from name)
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
       is on. See :ref:`pub_edgeai_am62dx_enhancement_chunking`.
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

The robot test and the enhancement pipeline use ``interleave_direction`` (underscore). Use the
same spelling as the working command you copy.

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

- A kernel ID: 1 for STFT, 2 for ISTFT, 3 for deinterleave/interleave.
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
- **Daemon fails during inference:** the element returns an error and does not fall back.

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

   GST_DEBUG=tidspkernel:6,titvm:6,tirpmsgchan:6 gst-launch-1.0 ...

``tidspkernel`` logs its message type, buffer sizes and each DSP request. ``titvm`` logs the
daemon handshake, the shape it detected, and the model load. ``tirpmsgchan`` logs the RPMsg
channel. For a pipeline graph, set ``GST_DEBUG_DUMP_DOT_DIR``.

.. _pub_edgeai_am62dx_advanced_usage:

Advanced Usage
==============

Batch Processing a Directory
-----------------------------

The enhancement pipeline needs ``max-stream-samples`` set to the padded length of each file.
This script computes it for each WAV file in a directory. It assumes 16 kHz mono 16-bit PCM
WAV files with a 44-byte header, which is what the sample files use:

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

This script has not been run on the board. Files shorter than one window (401 frames, about
4 seconds) use the same formula, but that case has not been tested either. Check the output
for those files.

Input Format Conversion
-----------------------

If the source is not 16 kHz mono 16-bit PCM, convert it inside the pipeline before the
``audio/x-raw`` capsfilter:

.. code-block:: bash

   filesrc location=input_44k.wav ! wavparse ! \
     audioconvert ! audioresample ! \
     audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
     ... rest of the pipeline

Or convert the file once with ffmpeg:

.. code-block:: bash

   ffmpeg -i input_44k.wav -ar 16000 -ac 1 -sample_fmt s16 input_16k.wav

Running Classification and Enhancement Together
-----------------------------------------------

A ``tee`` can send the same input to the enhancement chain and to a classifier. Each branch
needs its own ``queue``. This arrangement has not been run on the board.

.. code-block:: bash

   gst-launch-1.0 -v filesrc location=$INPUT ! wavparse ! \
     audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
     tee name=t \
     t. ! queue ! tidspkernel name=stft_y msg-type=0x1020 \
       model-path=/usr/share/tvm_inference/artifacts/yamnet \
       hop-size=160 window-frames=96 batch-size=64 ! \
     titvm model-path=/usr/share/tvm_inference/artifacts/yamnet \
       class-map-path=/usr/share/tvm_inference/labels/yamnet_label_list.txt top-k=3 ! \
     fakesink \
     t. ! queue ! ... enhancement chain from audio_enhancement ... ! \
     wavenc ! filesink location=/tmp/gst_enhanced.wav

Inside one pipeline, the ``tidspkernel`` elements share one RPMsg channel, and the channel
lock serialises their requests. Two separate pipeline processes each open their own channel.
Running them at the same time has not been tested.

Bring-Your-Own Model
--------------------

Use this section when you want to run a model other than GCRN, YAMNet or VGGish.

What Works Without Plugin Changes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``titvm`` loads any directory with ``deploy_graph.json``, ``deploy_lib.so`` and
  ``deploy_param.params``. Input and output shapes come from the graph. There are no
  model-name checks in ``titvm``.
- ``titvm`` sends its input to the model daemon when the daemon is running, so a new model
  can be loaded through the daemon in the same way.

What Needs Care
^^^^^^^^^^^^^^^

The DSP stages (``tidspkernel``) are not model-agnostic:

- ``selected-model`` is the firmware ModelId. The firmware implements the spectral processing
  for each ModelId. The plugin does not check that the ModelId matches your model.
- ``model-elems`` must equal the number of spectral values per frame that your model expects.
  The plugin does not read the graph to check it.
- A ``model-path`` that matches no known name does not log a warning. The element keeps its
  defaults (``selected-model=2``, ``model-elems`` from ``fft-size``). Set ``selected-model``
  and ``model-elems`` explicitly on every ``tidspkernel`` element.

Example
^^^^^^^

For a retrained GCRN model in a different directory, the model must still match the GCRN
spectral layout, and you should keep ModelId 2:

.. code-block:: bash

   MODEL=/usr/share/tvm_inference/artifacts/gcrn_v2
   gst-launch-1.0 filesrc location=$INPUT ! wavparse ! \
     audio/x-raw,format=S16LE,rate=16000,channels=1 ! \
     tidspkernel name=stft msg-type=0x1020 model-path=$MODEL \
       selected-model=2 model-elems=322 hop-size=160 fft-size=320 \
       window-frames=401 batch-size=64 max-stream-samples=160480 ! \
     ... deinterleave, titvm, interleave, istft as in audio_enhancement ...

For a model with a different spectral layout or DSP processing, a new ModelId is needed in the
DSP firmware. That change is outside this repository.

Validation
^^^^^^^^^^

Before you rely on a new model:

1. Run STFT followed by ISTFT with no model in between. Check that the output reproduces the
   input audio.
2. Run the full chain on a known test file. Compare the output with a reference from the
   model's own pipeline. Checking only the output length is not enough.

Debugging
---------

.. code-block:: bash

   GST_DEBUG=tidspkernel:6,titvm:6,tirpmsgchan:6 gst-launch-1.0 -v ...

To write a pipeline graph:

.. code-block:: bash

   mkdir -p /tmp/dot
   GST_DEBUG_DUMP_DOT_DIR=/tmp/dot gst-launch-1.0 ...
   ls /tmp/dot

The graph files are written when the pipeline changes state. Convert them with ``dot`` on a
host machine if the board does not have it.
