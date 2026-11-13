.. _am62dx_edgeai_integrating_new_model:

#######################
Integrating a New Model
#######################

This page covers what is needed to integrate a new deep learning model into the AM62DX
Edge AI system. Compiling the model and updating the DSP firmware are required for all
use cases. After that, you can run the model using either the Linux inference application
or GStreamer pipelines — both are independent paths.

********
Overview
********

- **Compile the Model** — required; generate TVM artifacts for the C7x™ DSP
- **DSP Firmware Changes** — required; register the model in the DSP signal chain
- **Linux Application** — use the ``rpmsg_inference_example`` application
- **GStreamer** — use ``tidspkernel`` and ``titvm`` GStreamer elements

*****************
Compile the Model
*****************

TI TVM compiles a trained model into deployable artifacts optimized for the AM62DX
C7x™ DSP. Compilation takes place on a host PC and goes through three stages:

.. code-block:: text

    ONNX model
        → Import into TVM
        → Partition
              TIDL-supported layers  →  TIDL artifacts (C7x™ NPU)
              Unsupported layers     →  C7x™ generated code
        → deploy_lib.so + deploy_graph.json + deploy_param.params

**Supported input format:** TI TVM accepts models in **ONNX** format. If your model
is in a different framework (PyTorch, TensorFlow, etc.), export it to ONNX first.

Workflow Overview
=================

#. **Verify the model on host** — Run inference with ``onnxruntime`` before compiling
   to confirm the model is well-formed and establish a reference output for later
   validation.

#. **Prepare calibration data** — TIDL runs inference with quantized fixed-point
   values. Provide a small representative set of real input frames (typically 2–10)
   as a ``.npz`` file. Calibration data must match the distribution of your real
   inference inputs — poor calibration data leads to accuracy loss.

#. **Compile** — Use either the TVMC command-line interface or the Python API
   (``compile_model``). The model is compiled twice: first for x86 host emulation,
   then for AArch64 (EVM). TIDL partitioning results are reused for the EVM build
   via ``REUSE_TIDL_ARTIFACTS``.

   .. code-block:: bash

      python3 -m tvm.driver.tvmc compile model.onnx \
        --target tidl \
        --tidl-config config.yaml \
        --tidl-calibration-input calibration.npz \
        --output ./artifacts/

#. **Validate** — Compare inference output on the EVM against the reference output
   from the host ``onnxruntime`` run to confirm accuracy is acceptable.

Compilation Artifacts
=====================

After a successful compilation, three files are written to the :file:`artifacts_folder`:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - File
     - Description
   * - ``deploy_lib.so``
     - Fat binary containing TIDL subgraphs and C7x™ NPU generated code
   * - ``deploy_graph.json``
     - Execution graph describing nodes, data flow, and input/output shapes
   * - ``deploy_param.params``
     - Quantized model weights

These three files are everything needed to run inference on the AM62D EVM. Deploy
them to :file:`/usr/share/tvm_inference/artifacts/<model_name>/` on the board.

Key Compilation Options
=======================

.. list-table::
   :header-rows: 1
   :widths: 40 15 45

   * - Option
     - Default
     - Description
   * - ``tensor_bits``
     - ``8``
     - Quantization precision: ``8``, ``16``, or ``32``
   * - ``advanced_options:calibration_frames``
     - ``20``
     - Number of calibration frames for quantization
   * - ``advanced_options:calibration_iterations``
     - ``50``
     - Number of calibration iterations per frame

For the complete compilation guide including all options, calibration workflow,
intermediate artifact descriptions, and debugging, see:

- :ref:`Model Compile and Evaluate <edgeai_compile_evaluate>`
- **[TI TVM Compilation Guide — link to be added]**
- **[TI TVM Bring Your Own Model Guide — link to be added]**

********************
DSP Firmware Changes
********************

The DSP firmware selects models at runtime via a ``ModelId`` enum and a dispatcher
``switch``. Adding a new model means adding one entry to the enum and one ``case`` to
the dispatcher. The full step-by-step guide is in the MCU+ SDK Edge AI Add New Model
documentation.

Files to modify or create
=========================

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - File
     - Change
   * - :file:`common/model_config.h`
     - Add ``MODEL_NEWMODEL`` to the ``ModelId`` enum before ``MODEL_COUNT``; bump
       ``MODEL_COUNT``
   * - :file:`common/models/<model>/TISP_<model>_signal_chain_memory_map.hpp`
     - New file: STFT/log-mel parameter macros (FFT size, hop size, channel count,
       buffer sizes)
   * - :file:`common/models/<model>/stft_signal_chain_<model>.hpp`
     - New file: declare ``StftSignalChain<MODEL>`` class interface
   * - :file:`common/models/<model>/stft_signal_chain_<model>.cpp`
     - New file: implement the signal chain, ``SignalChainOps`` table, and
       ``extern "C" newmodel_get_ops()``
   * - :file:`common/signal_chain_dispatch.cpp`
     - Add ``extern "C"`` declaration and new ``case MODEL_NEWMODEL`` in
       ``signal_chain_get_ops()``
   * - :file:`am62dx-evm/.../example.projectspec`
     - Add ``-I`` include path and ``<file>`` entry for the new model source
   * - :file:`am62dx-evm/.../makefile`
     - Add to ``FILES_cpp_common``, ``FILES_PATH_cpp_common``, and ``INCLUDES_common``

Key functions to implement in :file:`stft_signal_chain_<model>.cpp`
===================================================================

- ``create_pre_graph(int16_t *input_addr)`` — allocate arena buffers, generate STFT
  analysis window (or log-mel filterbank), build a ``TISP::opVec`` of
  ``TypeConversion`` + ``Stft`` (or ``LogMelSpectrum``)
- ``execute_pre_graph(void *pre_graph, int16_t *input_addr)`` — bind input address via
  ``setAddr(..., TISP::kAddrModeIn)`` and call ``TISP::execute::graph()``
- ``delete_pre_graph(void *pre_graph)`` — delete the ``TISP::opVec``
- ``create_post_graph`` / ``execute_post_graph`` / ``delete_post_graph`` — only for
  reconstruction-style models; set to ``NULL`` in ``SignalChainOps`` for analysis-only
  models
- ``newmodel_get_preprocess_buf()`` / ``newmodel_get_postprocess_buf()`` — return arena
  buffer addresses
- ``newmodel_reset_arenas()`` — call ``signal_chain_arena_reset_ready()``
- ``newmodel_get_ops()`` — expose the static ``SignalChainOps`` table

Two model types are supported
=============================

- **Reconstruction-style** (e.g. DCCRN, GCRN): STFT pre-graph + ISTFT
  post-graph; implement all six methods
- **Analysis-only** (e.g. VGGish, YAMNet): STFT/log-mel pre-graph only; post-graph
  methods are ``NULL`` in the ``SignalChainOps`` table

*****************
Linux Application
*****************

Using a New Model with an Existing Pipeline Type
================================================

To bring your own model, first compile it for the AM62DX C7x™ NPU using the
:ref:`Model Compile and Evaluate <edgeai_compile_evaluate>` workflow, which produces
the :file:`deploy_graph.json`, :file:`deploy_lib.so` and :file:`deploy_param.params` artifacts.

Once you have the compiled artifacts:

#. Deploy the model artifacts to the target:

   .. code-block:: console

      root@am62dxx-evm:~# mkdir -p /usr/share/tvm_inference/artifacts/my_model/
      root@am62dxx-evm:~# cp deploy_graph.json deploy_lib.so deploy_param.params \
                            /usr/share/tvm_inference/artifacts/my_model/

#. Copy the nearest existing JSON pipeline file as a starting point and adjust it for
   your model. The JSON files in :file:`example/edge-ai/json_files/` are the authoritative
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
   the deployed DSP firmware. Adjust ``selected_model``, ``model_elems``, ``total_frames``
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
=================================

If the existing pipeline types (``speech_enhancement``, ``audio_classification``,
``stft_istft``, ``tvm_only``) do not cover your use case, you can add a new pipeline
type. The dispatch is in :file:`pipeline_manager.cpp` and follows the same pattern for
every pipeline.

**Add a header and source file**

Create :file:`example/edge-ai/include/my_pipeline.h`:

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

Create :file:`example/edge-ai/src/my_pipeline.cpp`:

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

**Register the pipeline type in** :file:`pipeline_manager.cpp`

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

**Add the source file to** :file:`CMakeLists.txt`

In :file:`example/edge-ai/CMakeLists.txt`, add :file:`src/my_pipeline.cpp` to the
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

**Create a JSON pipeline file for the new type**

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
     - Check binary is in :file:`/usr/bin/` and has execute permission.
       Run :command:`ldd` to check for missing shared libraries.
   * - Connection to DSP endpoint fails
     - Verify DSP state is ``running``. Check :file:`/dev/rpmsg*` exists.
       View DSP trace with :command:`trace0`.
   * - Model artifact path not found
     - Verify ``artifacts_path`` in the JSON matches the deployed directory.
       Check :file:`deploy_graph.json`, :file:`deploy_lib.so` and :file:`deploy_param.params` are present.
   * - Audio input device not found
     - Run :command:`arecord -l` to list ALSA devices. Verify ``--device`` name matches.
   * - Long wait before inference starts
     - ``tvm_model_daemon`` is not running. Start it or accept the in-process load time.

*********
GStreamer
*********

.. _pub_edgeai_am62dx_byom:

Bring-Your-Own Model
====================

The three reference pipelines use pre-trained, pre-compiled models so you can see the
plugins working immediately. Most production use cases, though, need a model trained on
your own data — your own set of sound events, or a speech-enhancement model tuned to
your product's microphone and acoustic environment. This section covers what it takes to
run such a model through ``tidspkernel`` and ``titvm`` once it has been compiled for the
AM62Dx C7x™ DSP.

Compiling the model itself — taking an ONNX graph through quantization and generating
:file:`deploy_graph.json`, :file:`deploy_lib.so` and :file:`deploy_param.params` — is covered
separately in :ref:`Model Compile and Evaluate <edgeai_compile_evaluate>`. This section
assumes you already have those three artifacts and focuses on wiring them into a GStreamer
pipeline.

Requirements
------------

A compiled model directory with the same three files the reference models use:

.. code-block:: text

   my_model/
   ├── deploy_graph.json     graph description; input/output shapes read from attrs.shape
   ├── deploy_lib.so         compiled model library
   └── deploy_param.params   model weights

Beyond these files, you must specify two critical model properties that the plugins cannot
auto-detect:

- **Task type**: whether the model performs speech enhancement (like GCRN) or
  classification (like YAMNet/VGGish). This determines which pipeline you should adapt.
- **Spectral layout**: the FFT size, hop size, and window length the model was trained
  with, plus the number of spectral coefficients per frame that the DSP firmware must
  produce.

Example: A New Model
--------------------

Suppose you have a new model with a unique architecture and spectral front-end, and
DSP firmware ModelId ``5`` has already been added to support it. To use it in a GStreamer
pipeline, follow the same pattern as the YAMNet/VGGish examples, but explicitly set all
spectral properties instead of relying on path-based auto-detection:

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

This command uses the same approach as the reference models — the difference is that all
spectral parameters (``selected-model``, ``model-elems``, ``fft-size``, ``hop-size``,
``window-frames``) are now explicitly set for your model rather than auto-detected from
the path. The ``titvm`` element requires no modifications beyond ``model-path`` — it
automatically loads and runs whatever TVM artifacts it finds in that directory.

For a speech-enhancement model with a new architecture, use the same approach: build
your pipeline with the ``deinterleave`` → ``tidspkernel`` (STFT) → ``titvm`` →
``interleave`` → ``tidspkernel`` (ISTFT) chain from the GCRN reference pipeline, then
set the ``tidspkernel`` properties to match your model's spectral layout instead of
GCRN's.

Supporting New Model Architectures in the Plugins
=================================================

If your model introduces a new architecture or spectral processing scheme not covered by
existing DSP firmware ModelIds, the DSP DSP firmware must first add support for that new
ModelId. Once the DSP firmware is updated, the GStreamer plugins can immediately wire it
in by setting the ``selected-model`` property to the new DSP firmware ID.

However, if you need to extend the plugins themselves to better support a new model
category or add automatic detection logic, the following sections show the code you
would modify in the GStreamer plugin source files. Section :ref:`pub_edgeai_am62dx_building_plugin`
shows how to build the new modified plugin.

Adding a New GStreamer Property to ``tidspkernel``
--------------------------------------------------

If your new model requires an additional configuration parameter (for example, a
``model-specific-param`` flag), add it to the plugin header and implementation:

**1. Header: gstdspkernel.h - Add to the struct:**

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

**2. Implementation: gstdspkernel.cpp - Add property enum:**

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

**3. Register the property in class_init():**

.. code-block:: c

   g_object_class_install_property (gobject_class, PROP_MODEL_SPECIFIC_PARAM,
       g_param_spec_uint ("model-specific-param", "Model Specific Param",
           "Custom parameter for new model architecture",
           0, 255, 0,  /* min, max, default */
           (GParamFlags) (G_PARAM_READWRITE | G_PARAM_STATIC_STRINGS)));

**4. Add getter/setter in set_property() and get_property():**

.. code-block:: c

   static void
   gst_dsp_kernel_set_property (GObject * object, guint prop_id,
       const GValue * value, GParamSpec * pspec)
   {
     GstDspKernel *kernel = GST_DSP_KERNEL (object);

     switch (prop_id) {
       /* ... existing properties ... */
       case PROP_MODEL_SPECIFIC_PARAM:
         kernel->model_specific_param = g_value_get_uint (value);
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
       case PROP_MODEL_SPECIFIC_PARAM:
         g_value_set_uint (value, kernel->model_specific_param);
         break;
       default:
         G_OBJECT_WARN_INVALID_PROPERTY_ID (object, prop_id, pspec);
         break;
     }
   }

**5. Verify the property is registered (after rebuild and install):**

After rebuilding and installing the plugin, verify that the new property appears in the
element's property list using ``gst-inspect-1.0``:

.. code-block:: bash

   root@am62dxx-evm:~# gst-inspect-1.0 tidspkernel | grep -A 5 "model-specific-param"

Expected output:

.. code-block:: text

                     model-specific-param : Custom parameter for new model architecture
                            flags: readable, writable
                            Unsigned Integer. Range: 0 - 255 Default: 0

If your new property appears in the output with the correct type, range, and default value,
the registration was successful. You can now use it in GStreamer pipelines:

.. code-block:: bash

   gst-launch-1.0 -v ... tidspkernel name=stft ... model-specific-param=1 ... ! ...

Adding a New Property to ``titvm``
----------------------------------

Similarly, for the TVM inference element, if you need a new parameter (for example,
``inference-threshold`` for filtering low-confidence predictions):

**1. Header: gsttitvm.h - Add to struct:**

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

**2. Implementation: gsttitvm.cpp - Add property enum and register:**

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
       GST_DEBUG_OBJECT (tvm, "Prediction %u: confidence=%.3f (above threshold %.3f)",
           i, confidence, tvm->inference_threshold);
     }
   }

Automatic Model Detection from Path
-----------------------------------

If you want the plugins to auto-detect your new model based on its directory path name,
add a mapping in the model detection logic in ``gstdspkernel.cpp``:

.. code-block:: c

   struct {
     const gchar *path_substring;
     guint selected_model;
     guint model_elems;
     guint fft_size;
     guint hop_size;
     guint window_frames;
   } known_models[] = {
     { "gcrn",   2, 322, 320, 160, 401 },
     { "gtcrn",  1, 322, 320, 160, 401 },
     { "dccrn",  0, 322, 320, 160, 401 },
     { "yamnet", 4,  64, 512, 160,  96 },
     { "vggish", 3, 128, 512, 160,  96 },

     /* NEW: Add your model */
     { "my_custom_model", 5, 256, 512, 256, 100 },

     { NULL, 0, 0, 0, 0, 0 }  /* Sentinel */
   };

The ``gst_dsp_kernel_detect_model()`` function iterates this table and auto-sets
``selected-model``, ``model-elems``, ``fft-size``, ``hop-size``, and ``window-frames``
when ``model-path`` contains the matching substring.

.. _pub_edgeai_am62dx_building_plugin:

Building the Modified Plugins
-----------------------------

Plugin source files are located in the :file:`/opt/edgeai-gst-plugins/` repository.

**Source File Locations:**

- ``ext/ti/gstdspkernel.h`` — Header for DSP kernel element (STFT/ISTFT/deinterleave)
- ``ext/ti/gstdspkernel.cpp`` — Implementation of DSP kernel element
- ``ext/ti/gsttitvm.h`` — Header for TVM inference element
- ``ext/ti/gsttitvm.cpp`` — Implementation of TVM inference element
- ``utility/gsttirpmsgctx.h`` / ``utility/gsttirpmsgctx.cpp`` — RPMsg context utilities

After modifying any of these files, rebuild the plugin. The meson build system automatically
detects all source files in ``ext/ti/`` — **no meson.build file changes are required**.

Native Build on the Board
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   root@am62dxx-evm:/opt/edgeai-gst-plugins# export SOC=am62d
   root@am62dxx-evm:/opt/edgeai-gst-plugins# meson setup build --prefix=/usr \
     -Dpkg_config_path=pkgconfig \
     -Dtvm-plugins=enabled \
     -Dstft-plugins=enabled \
     -Ddl-plugins=disabled \
     -Denable-tidl=disabled
   root@am62dxx-evm:/opt/edgeai-gst-plugins# ninja -C build
   root@am62dxx-evm:/opt/edgeai-gst-plugins# ninja -C build install
   root@am62dxx-evm:/opt/edgeai-gst-plugins# ldconfig

The updated plugin will be installed to :file:`/usr/lib/gstreamer-1.0/libgstti.so`.
