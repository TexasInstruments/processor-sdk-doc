.. _am62dx_linux_audio_inference_app:

#################################
Linux Audio Inference Application
#################################

Introduction
============

The AM62DX audio inference application (``rpmsg_inference_example``) is a C++ application
for running configurable audio and tensor pipelines across Linux and the C7x DSP. It is part
of the `rpmsg-dma <https://github.com/TexasInstruments/rpmsg-dma>`__ repository. The
application enables:

- **Real-time Audio Processing** — Process live ALSA audio devices or WAV file inputs
- **DSP Offload** — Offload STFT, ISTFT and deinterleave/interleave to the C7x DSP over RPMsg-DMA
- **TVM Inference** — Run TVM-compiled deep learning models on the C7x NPU
- **Flexible I/O** — WAV files, live ALSA capture, raw PCM streams, or binary tensors
- **JSON Pipeline Configuration** — Define processing chains via JSON files
- **Model Daemon Mode** — Persistent TVM model daemon to avoid repeated artifact loading

Supported Pipelines
===================

.. list-table::
   :header-rows: 1
   :widths: 30 30 20 20

   * - Pipeline
     - JSON file
     - Default input
     - Output
   * - Speech enhancement (GCRN)
     - ``pipeline_speech_enhancement.json``
     - ``input_audio.wav``
     - Enhanced WAV file
   * - Audio classification (YAMNet)
     - ``pipeline_audio_classification_yamnet.json``
     - ``speech_whistling2.wav``
     - Top-k class names and scores
   * - Audio classification (VGGish)
     - ``pipeline_audio_classification_vggish.json``
     - ``urbansound_16k.wav``
     - Top-k class names and scores

Prerequisites
=============

**Board and Firmware**

- AM62DX EVM running Processor SDK Linux
- C7x dual-task firmware providing the generic DSP service and TVM service.
  Refer to `MCU+ SDK Documentation <https://software-dl.ti.com/mcu-plus-sdk/esd/AM62DX/12_00_00_22/exports/docs/api_guide_am62dx/GETTING_STARTED_BUILD.html>`__
  for building the C7x firmware.
- Remoteproc, RPMsg-char, and DMA heap kernel support

**Libraries (on target or SDK sysroot)**

- ``libti_rpmsg_dma`` — RPMsg DMA client library
- ``libtvm_runtime.so`` — Neo-TVM ARM64 runtime. Refer to `TI TVM Documentation <http://tvm-tidl-04.dhcp.ti.com:9090/index.html>`__.
- ``libasound`` — ALSA library
- ``libsndfile`` — Audio file I/O
- ``libjson-c`` — JSON pipeline parsing

**Host Build Tools**

- ARM Clang Toolchain (from Processor SDK Linux devkit)
- CMake 3.10 or higher
- ``make``, ``git``
- Neo-TVM headers (``TVM_ROOT``). Refer to `TI TVM Documentation <http://tvm-tidl-04.dhcp.ti.com:9090/index.html>`__.

Clone the Source
================

The ``edge-ai`` example is part of the ``rpmsg-dma`` repository:

.. code-block:: console

   host# git clone https://github.com/TexasInstruments/rpmsg-dma.git -b main
   host# cd rpmsg-dma

The example is under ``example/edge-ai/`` and contains:

.. code-block:: text

   example/edge-ai/
   ├── CMakeLists.txt
   ├── src/                  application source files
   ├── include/              header files
   ├── json_files/           pipeline JSON configurations
   ├── labels/               classification label files
   ├── input_audio/          sample WAV input files
   ├── tvm-model-daemon.service
   └── tvm-model-preload.service

Build the Linux Application
============================

Building the Linux Binary from Sources
---------------------------------------

#. Download and install the AM62DX Linux SDK from |__SDK_DOWNLOAD_URL__|.
   Extract the SDK tarball and run the installer script on your development host.

#. Prepare the environment for cross compilation:

   .. code-block:: console

      host# source <path to linux installer>/linux-devkit/environment-setup

#. Set the Neo-TVM path. Either pass it directly to CMake or export it as an
   environment variable:

   .. code-block:: console

      host# export NEO_TVM_PATH=/path/to/neo-tvm

   Or pass it on the CMake command line:

   .. code-block:: console

      host# cmake -S . -B build -DTVM_ROOT=/path/to/neo-tvm

   If the TVM runtime library is not at ``${TVM_ROOT}/libtvm_runtime.so``, specify
   it explicitly:

   .. code-block:: console

      host# cmake -S . -B build \
              -DTVM_ROOT=/path/to/neo-tvm \
              -DTVM_RUNTIME_LIB=/path/to/aarch64/libtvm_runtime.so

#. Build only the edge-ai example to avoid building unrelated examples:

   .. code-block:: console

      [linux-devkit]:> cmake -S . -B build -DBUILD_EDGE_AI_EXAMPLE=ON \
                         -DBUILD_AUDIO_OFFLOAD_EXAMPLE=OFF \
                         -DBUILD_2DFFT_OFFLOAD_EXAMPLE=OFF \
                         -DBUILD_SIGNAL_CHAIN_BIQUAD_EXAMPLE=OFF
      [linux-devkit]:> cmake --build build

#. This builds:

   - ``build/example/edge-ai/rpmsg_inference_example`` — main inference application
   - ``build/example/edge-ai/tvm_model_daemon`` — persistent model daemon

#. Install to a staging directory and transfer to the EVM:

   .. code-block:: console

      [linux-devkit]:> cmake --install build --prefix /tmp/edge-ai-install

   Transfer to the EVM:

   .. code-block:: console

      host# scp /tmp/edge-ai-install/bin/rpmsg_inference_example root@<EVM_IP>:/usr/bin/
      host# scp /tmp/edge-ai-install/bin/tvm_model_daemon root@<EVM_IP>:/usr/bin/
      host# scp -r /tmp/edge-ai-install/share/tvm_inference/ root@<EVM_IP>:/usr/share/

   Or copy directly to a mounted SD card:

   .. code-block:: console

      host# cp /tmp/edge-ai-install/bin/rpmsg_inference_example /mnt/rootfs/usr/bin/
      host# cp -r /tmp/edge-ai-install/share/tvm_inference/ /mnt/rootfs/usr/share/

Running the Application
=======================

Basic Syntax
------------

.. code-block:: console

   rpmsg_inference_example <pipeline.json> [options]

Run with a WAV file input:

.. code-block:: console

   root@am62dxx-evm:~# rpmsg_inference_example \
     /usr/share/tvm_inference/json/pipeline_speech_enhancement.json

   root@am62dxx-evm:~# rpmsg_inference_example \
     /usr/share/tvm_inference/json/pipeline_audio_classification_yamnet.json \
     --input-file /usr/share/tvm_inference/input/speech_whistling2.wav

Live ALSA device input (audio classification pipelines only):

.. code-block:: console

   root@am62dxx-evm:~# rpmsg_inference_example \
     /usr/share/tvm_inference/json/pipeline_audio_classification_yamnet.json \
     --device plughw:0,0

Stream raw PCM from stdin (mono, S16_LE, 16 kHz):

.. code-block:: console

   root@am62dxx-evm:~# arecord -t raw -f S16_LE -c 1 -r 16000 | \
     rpmsg_inference_example \
       /usr/share/tvm_inference/json/pipeline_audio_classification_yamnet.json \
       --stream

Additional options:

.. code-block:: console

   rpmsg_inference_example --help
   rpmsg_inference_example --version
   rpmsg_inference_example <pipeline.json> --debug

Model Daemon
============

The ``tvm_model_daemon`` keeps a TVM model loaded in memory and serves inference requests
over a Unix domain socket, eliminating repeated artifact loading for each run.

.. code-block:: console

   root@am62dxx-evm:~# systemctl enable --now tvm-model-daemon.service
   root@am62dxx-evm:~# journalctl -u tvm-model-daemon -f

To preload artifacts at boot using the preload service:

.. code-block:: console

   root@am62dxx-evm:~# systemctl enable --now tvm-model-preload.service

Using a New Model or Custom Pipeline
======================================

Using a New Model with an Existing Pipeline Type
-------------------------------------------------

To bring your own model, first compile it for the AM62DX C7x NPU using the
:ref:`Model Compile and Evaluate <audioai-compile-evaluate>` workflow, which produces
the ``deploy_graph.json``, ``deploy_lib.so`` and ``deploy_param.params`` artifacts.

Once you have the compiled artifacts:

#. Deploy the model artifacts to the target:

   .. code-block:: console

      root@am62dxx-evm:~# mkdir -p /usr/share/tvm_inference/artifacts/my_model/
      root@am62dxx-evm:~# cp deploy_graph.json deploy_lib.so deploy_param.params \
                            /usr/share/tvm_inference/artifacts/my_model/

#. Copy the nearest existing JSON pipeline file as a starting point and adjust it for
   your model. The JSON files in ``example/edge-ai/json_files/`` are the authoritative
   reference. Key fields to update:

   .. code-block:: json

      {
        "pipeline_type": "audio_classification",
        "input_file": "/usr/share/tvm_inference/input/my_audio.wav",
        "artifacts_path": "/usr/share/tvm_inference/artifacts/my_model",
        "labels_path": "/usr/share/tvm_inference/labels/my_model_labels.txt",
        "num_classes": 10,
        "dsp_config": {
          "proc_id": 8,
          "endpoint": 13
        },
        "stages": [
          {
            "stage_id": "stft_analysis",
            "service": "dsp",
            "message_type": "C7X_MSG_STFT_ANALYZE",
            "parameters": {
              "selected_model": 4,
              "hop_size": 160,
              "model_elems": 64,
              "total_frames": 96,
              "batch_n": 64
            }
          },
          {
            "stage_id": "tvm_inference",
            "service": "tvm",
            "message_type": "TVM_INFERENCE",
            "parameters": {
              "input_shape": "1,1,96,64"
            }
          }
        ]
      }

   Keep ``proc_id``, ``endpoint``, and DSP ``message_type`` values consistent with
   the deployed firmware. Adjust ``selected_model``, ``model_elems``, ``total_frames``
   and ``input_shape`` to match your model's spectral layout.

#. If your model outputs classifications, provide a labels file (one label per line):

   .. code-block:: console

      root@am62dxx-evm:~# cat > /usr/share/tvm_inference/labels/my_model_labels.txt << EOF
      Label 0
      Label 1
      ...
      EOF

#. Run the application with the new pipeline:

   .. code-block:: console

      root@am62dxx-evm:~# rpmsg_inference_example /path/to/my_pipeline.json \
                            --input-file /path/to/test_audio.wav

Adding a New Pipeline Type in C++
----------------------------------

If the existing pipeline types (``speech_enhancement``, ``audio_classification``,
``stft_istft``, ``tvm_only``) do not cover your use case, you can add a new pipeline
type. The dispatch is in ``pipeline_manager.cpp`` and follows the same pattern for
every pipeline.

**Step 1: Add a header and source file**

Create ``example/edge-ai/include/my_pipeline.h``:

.. code-block:: cpp

   #pragma once
   #include "pipeline_manager.h"
   #include "dsp_task_client.h"
   #include "tvm_inference_client.h"

   PipelineManager::CommandResult run_my_pipeline(
       PipelineManager::State& state,
       DspTaskClient& dsp_client,
       TvmInferenceClient& tvm_client,
       bool debug);

Create ``example/edge-ai/src/my_pipeline.cpp``:

.. code-block:: cpp

   #include "my_pipeline.h"
   #include "pipeline_common.h"
   #include <iostream>

   PipelineManager::CommandResult run_my_pipeline(
       PipelineManager::State& state,
       DspTaskClient& dsp_client,
       TvmInferenceClient& tvm_client,
       bool debug)
   {
       // Access pipeline config and stages from state
       const auto& config = state.pipeline_config;
       const auto& stages = config.stages;

       // Find your custom stage by message_type
       const PipelineManager::PipelineStage* my_stage = nullptr;
       for (const auto& s : stages) {
           if (s.message_type == "MY_CUSTOM_MSG") {
               my_stage = &s;
               break;
           }
       }
       if (!my_stage)
           throw PipelineError{"my_pipeline requires a MY_CUSTOM_MSG stage"};

       // Read stage parameters
       size_t hop_size = std::stoul(my_stage->parameters.at("hop_size"));

       // ... run DSP and TVM stages using dsp_client and tvm_client ...

       std::cout << "[App] my_pipeline complete" << std::endl;
       return PipelineManager::CommandResult::SUCCESS;
   }

**Step 2: Register the pipeline type in** ``pipeline_manager.cpp``

In ``run_from_json_file()``, add your new ``pipeline_type`` string to the dispatch
block alongside the existing types:

.. code-block:: cpp

   #include "my_pipeline.h"   // add this include at the top

   // ... inside run_from_json_file(), in the dispatch block:
   if (pipeline_type == "speech_enhancement") {
       result = run_speech_enhancement_pipeline(state_, *generic_client_, *tvm_client_, debug_);
   } else if (pipeline_type == "audio_classification") {
       result = run_audio_classification_pipeline(state_, *generic_client_, *tvm_client_, debug_);
   } else if (pipeline_type == "tvm_only") {
       result = run_tvm_pipeline(state_, *tvm_client_);
   } else if (pipeline_type == "stft_istft") {
       result = run_stft_istft_pipeline(state_, *generic_client_, debug_);
   } else if (pipeline_type == "my_pipeline") {          // add this
       result = run_my_pipeline(state_, *generic_client_, *tvm_client_, debug_);
   } else {
       std::cout << "[App] Error: Unknown pipeline_type: " << pipeline_type << std::endl;
       return -1;
   }

**Step 3: Add the source file to** ``CMakeLists.txt``

In ``example/edge-ai/CMakeLists.txt``, add ``src/my_pipeline.cpp`` to the
``EDGE_AI_SOURCES`` list:

.. code-block:: cmake

   set(EDGE_AI_SOURCES
       src/main.cpp
       src/tvm_inference_client.cpp
       src/dsp_task_client.cpp
       src/pipeline_manager.cpp
       src/pipeline_common.cpp
       src/audio_utils.cpp
       src/speech_enhancement_pipeline.cpp
       src/audio_classification_pipeline.cpp
       src/tvm_pipeline.cpp
       src/stft_istft_pipeline.cpp
       src/my_pipeline.cpp          # add this
   )

**Step 4: Create a JSON pipeline file for the new type**

.. code-block:: json

   {
     "pipeline_type": "my_pipeline",
     "input_file": "/usr/share/tvm_inference/input/my_audio.wav",
     "artifacts_path": "/usr/share/tvm_inference/artifacts/my_model",
     "dsp_config": { "proc_id": 8, "endpoint": 13 },
     "stages": [
       {
         "stage_id": "my_stage",
         "service": "dsp",
         "message_type": "MY_CUSTOM_MSG",
         "parameters": { "hop_size": "160" }
       },
       {
         "stage_id": "tvm_inference",
         "service": "tvm",
         "message_type": "TVM_INFERENCE",
         "parameters": { "input_shape": "1,1,96,64" }
       }
     ]
   }

Rebuild with ``cmake --build build`` and run:

.. code-block:: console

   root@am62dxx-evm:~# rpmsg_inference_example /path/to/my_pipeline.json

Debugging and Troubleshooting
=============================

**System checks**

.. code-block:: console

   root@am62dxx-evm:~# grep . /sys/class/remoteproc/remoteproc*/name
   root@am62dxx-evm:~# grep . /sys/class/remoteproc/remoteproc*/state
   root@am62dxx-evm:~# ls -l /dev/rpmsg* /dev/dma_heap/*
   root@am62dxx-evm:~# ldd /usr/bin/rpmsg_inference_example
   root@am62dxx-evm:~# find /usr/share/tvm_inference -maxdepth 3 -type f

**DSP firmware trace**

.. code-block:: console

   root@am62dxx-evm:~# cat /sys/kernel/debug/remoteproc/remoteproc*/trace0

**Enable debug logging**

.. code-block:: console

   root@am62dxx-evm:~# rpmsg_inference_example <pipeline.json> --debug

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Symptom
     - Action
   * - ``rpmsg_inference_example`` not found
     - Check binary is in ``/usr/bin/`` and has execute permission.
       Run ``ldd`` to check for missing shared libraries.
   * - Connection to DSP endpoint fails
     - Verify DSP state is ``running``. Check ``/dev/rpmsg*`` exists.
       View DSP trace with ``trace0``.
   * - Model artifact path not found
     - Verify ``artifacts_path`` in the JSON matches the deployed directory.
       Check ``deploy_graph.json``, ``deploy_lib.so`` and ``deploy_param.params`` are present.
   * - Audio input device not found
     - Run ``arecord -l`` to list ALSA devices. Verify ``--device`` name matches.
   * - Long wait before inference starts
     - ``tvm_model_daemon`` is not running. Start it or accept the in-process load time.
