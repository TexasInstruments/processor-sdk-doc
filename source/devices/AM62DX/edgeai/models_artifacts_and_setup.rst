.. _am62dx_edgeai_models_artifacts_and_setup:

################################################
Pre-Built Model Artifacts and Configuration
################################################

The AM62DX EdgeAI image ships with three pre-compiled, pre-packaged models ready to run
out of the box — no compilation required. These models, artifacts, and setup steps are
common to both the Linux inference application and the GStreamer pipelines.

********************
Pre-Packaged Models
********************

.. list-table::
   :header-rows: 1
   :widths: 15 20 10 25 30

   * - Model
     - Type
     - ModelId
     - Artifacts path
     - Description
   * - GCRN
     - Speech enhancement
     - 2
     - ``/usr/share/tvm_inference/artifacts/gcrn/``
     - Removes background noise from speech; produces enhanced WAV output
   * - YAMNet
     - Audio classification
     - 4
     - ``/usr/share/tvm_inference/artifacts/yamnet/``
     - 521-class AudioSet audio event classification
   * - VGGish
     - Audio classification
     - 3
     - ``/usr/share/tvm_inference/artifacts/vggish/``
     - 10-class UrbanSound8K audio classification

***************
Model Artifacts
***************

Each model directory under ``/usr/share/tvm_inference/artifacts/<model>/`` contains:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - File
     - Description
   * - ``deploy_graph.json``
     - Graph description; defines the neural network topology and input/output shapes
   * - ``deploy_lib.so``
     - Compiled model library; shared object for TVM runtime
   * - ``deploy_param.params``
     - Model weights; binary parameter data

***********
Label Files
***********

Classification models ship with label files under ``/usr/share/tvm_inference/labels/``:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - File
     - Description
   * - ``yamnet_label_list.txt``
     - 521 lines; one AudioSet class name per line for YAMNet
   * - ``vggish_label_list.txt``
     - 10 lines; one UrbanSound8K class name per line for VGGish

***********
Input Audio
***********

All pipelines expect **16 kHz, mono, signed 16-bit PCM WAV** input. Sample files in
this format are pre-installed under ``/usr/share/tvm_inference/input/``:

.. list-table::
   :header-rows: 1
   :widths: 35 25 40

   * - File
     - Used with
     - Description
   * - ``input_audio.wav``
     - GCRN
     - Sample noisy speech recording
   * - ``speech_whistling2.wav``
     - YAMNet
     - Sample audio for event classification
   * - ``urbansound_16k.wav``
     - YAMNet, VGGish
     - Sample urban sound recording

If your source audio is in a different format, convert it before use:

.. code-block:: bash

   ffmpeg -i input.wav -ar 16000 -ac 1 -sample_fmt s16 output_16k.wav

Or convert inline inside a GStreamer pipeline by inserting ``audioconvert`` and
``audioresample`` before the ``audio/x-raw`` capsfilter.

**********************
Pre-Packaged Libraries
**********************

The following libraries are pre-installed on the AM62DX EdgeAI image. No installation
is required to run the out-of-box pipelines on the AM62D EVM.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Library
     - Description
   * - ``libti_rpmsg_dma``
     - RPMsg and DMA client library for inter-processor communication
   * - ``libtvm_runtime.so``
     - Neo-TVM ARM64 runtime for model inference
   * - ``libgstti.so``
     - GStreamer plugin library containing ``tidspkernel`` and ``titvm`` elements
   * - ``libasound``
     - ALSA audio library
   * - ``libsndfile``
     - Audio file I/O library
   * - ``libjson-c``
     - JSON parsing library

************
Model Daemon
************

The ``tvm_model_daemon`` keeps a TVM model loaded in memory and serves inference
requests over a Unix domain socket at ``/var/run/tvm-inference.sock``. Both the Linux
inference application and the GStreamer ``titvm`` element connect to it automatically,
eliminating repeated artifact loading for each run.

Start the daemon:

.. code-block:: console

   root@am62dxx-evm:~# systemctl enable --now tvm-model-daemon.service
   root@am62dxx-evm:~# journalctl -u tvm-model-daemon -f
   Oct 23 08:05:48 am62dxx-evm tvm_model_daemon[997]: rpmsg: Opened endpoint device /dev/rpmsg4
   Oct 23 08:05:48 am62dxx-evm tvm_model_daemon[997]: [daemon] Loading TVM artifacts from: /usr/share/tvm_inference/artifacts/gcrn
   Oct 23 08:05:48 am62dxx-evm tvm_model_daemon[997]: [daemon] C7x firmware OK and already running
   Oct 23 08:05:48 am62dxx-evm tvm_model_daemon[997]: c7x: Connected to compute service
   Oct 23 08:05:48 am62dxx-evm tvm_model_daemon[997]: c7x: Staging buffer:  0xffff6c89e000 (phys 0xa3000000)
   Oct 23 08:05:48 am62dxx-evm tvm_model_daemon[997]: c7x: Result buffer: 0xffff7549e000 (phys 0xabc00000)
   Oct 23 08:05:48 am62dxx-evm tvm_model_daemon[997]: [08:05:48] {TVM_HOME}/src/runtime/contrib/tidl/tidl_runtime_rpmsg.cc:216: TVM AM62D: ping status=0 version=0x20000 uptime=17438ms
   Oct 23 08:05:48 am62dxx-evm tvm_model_daemon[997]: [08:05:48] {TVM_HOME}/src/runtime/contrib/tidl/tidl_runtime_rpmsg.cc:239: TVM AM62D: loading deploy_mod (51527424 bytes) with 1 input name(s)
   Oct 23 08:05:49 am62dxx-evm tvm_model_daemon[997]: c7x: Loaded module handle=1 (text=0 data=0 input_offset=51527443)
   Oct 23 08:05:49 am62dxx-evm tvm_model_daemon[997]: [08:05:49] {TVM_HOME}/src/runtime/contrib/tidl/tidl_runtime_rpmsg.cc:263: TVM AM62D: module loaded, handle=1

To preload artifacts at boot:

.. code-block:: console

   root@am62dxx-evm:~# systemctl enable --now tvm-model-preload.service

If the daemon is not running, both the Linux application and GStreamer ``titvm`` element
will wait up to 30 seconds before falling back to loading the model in-process.

******************
DSP Firmware Check
******************

Both the Linux application and GStreamer pipelines require the C7x™ DSP firmware to be
running. Verify before use:

.. code-block:: console

   root@am62dxx-evm:~# cat /sys/class/remoteproc/remoteproc0/state
   running
