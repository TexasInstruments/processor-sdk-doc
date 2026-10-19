.. _am62dx_edgeai_adding_new_model:

####################
Adding a New Model
####################

This page gives a high-level overview of what is needed to integrate a new deep learning
model into the AM62DX Edge AI system. Each step links to the detailed documentation for
that component.

Overview
========

Adding a new model touches four components in sequence:

1. **Compile the Model** — generate TVM artifacts for the C7x DSP
2. **Firmware Changes** — register and wire the model into the DSP signal chain
3. **Linux Application** — add a pipeline JSON configuration
4. **GStreamer Plugin** — set properties and optionally extend the known-model table

Steps 2–4 are independent once the TVM artifacts from Step 1 are available.

Step 1: Compile the Model
=========================

Use the TVM compilation workflow to produce three artifacts for the C7x DSP:

- ``deploy_graph.json`` — graph description with input/output shapes
- ``deploy_lib.so`` — compiled model library
- ``deploy_param.params`` — model weights

These artifacts are required by both the Linux application and the GStreamer plugin.
See :ref:`Model Compile and Evaluate <audioai-compile-evaluate>`.

Step 2: Firmware Changes
=========================

The DSP firmware selects models at runtime via a ``ModelId`` enum and a dispatcher
``switch``. Adding a new model means adding one entry to the enum and one ``case`` to
the dispatcher. The full step-by-step guide is in the MCU+ SDK Edge AI Add New Model
documentation.

**Files to modify or create:**

.. list-table::
   :header-rows: 1
   :widths: 45 55

   * - File
     - Change
   * - ``common/model_config.h``
     - Add ``MODEL_NEWMODEL`` to the ``ModelId`` enum before ``MODEL_COUNT``; bump
       ``MODEL_COUNT``
   * - ``common/models/<model>/TISP_<model>_signal_chain_memory_map.hpp``
     - New file: STFT/log-mel parameter macros (FFT size, hop size, channel count,
       buffer sizes)
   * - ``common/models/<model>/stft_signal_chain_<model>.hpp``
     - New file: declare ``StftSignalChain<MODEL>`` class interface
   * - ``common/models/<model>/stft_signal_chain_<model>.cpp``
     - New file: implement the signal chain, ``SignalChainOps`` table, and
       ``extern "C" newmodel_get_ops()``
   * - ``common/signal_chain_dispatch.cpp``
     - Add ``extern "C"`` declaration and new ``case MODEL_NEWMODEL`` in
       ``signal_chain_get_ops()``
   * - ``am62dx-evm/.../example.projectspec``
     - Add ``-I`` include path and ``<file>`` entry for the new model source
   * - ``am62dx-evm/.../makefile``
     - Add to ``FILES_cpp_common``, ``FILES_PATH_cpp_common``, and ``INCLUDES_common``

**Key functions to implement in** ``stft_signal_chain_<model>.cpp``:

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

**Two model types are supported:**

- **Reconstruction-style** (e.g. DCCRN, GTCRN, GCRN): STFT pre-graph + ISTFT
  post-graph; implement all six methods
- **Analysis-only** (e.g. VGGish, YAMNet): STFT/log-mel pre-graph only; post-graph
  methods are ``NULL`` in the ``SignalChainOps`` table

Step 3: Linux Application
=========================

The ``rpmsg_inference_example`` application is driven entirely by JSON pipeline files.
Adding a new model requires no C++ source changes if the pipeline type already exists
(``audio_classification`` or ``speech_enhancement``).

**For a new model with an existing pipeline type:**

1. Place compiled artifacts under ``/usr/share/tvm_inference/artifacts/<model_name>/``
2. Copy the nearest existing JSON file from ``example/edge-ai/json_files/`` and update:

   - ``artifacts_path`` — path to new model artifacts
   - ``stages[stft_analysis].parameters.selected_model`` — the new ``ModelId`` integer
     assigned in Step 2
   - ``stages[stft_analysis].parameters.model_elems``, ``hop_size``, ``total_frames``,
     ``batch_n`` — match the model's spectral layout
   - ``stages[tvm_inference].parameters.input_shape`` — match the model input tensor
     shape from ``deploy_graph.json``
   - ``labels_path`` and ``num_classes`` — for classification models

3. Optionally provide a labels file (one class name per line) under
   ``/usr/share/tvm_inference/labels/``

**For a new pipeline type (requires new C++ code):**

If no existing pipeline type matches your model's data flow:

- Create ``example/edge-ai/include/my_pipeline.h`` and
  ``example/edge-ai/src/my_pipeline.cpp`` implementing
  ``run_my_pipeline(PipelineManager::State&, DspTaskClient&, TvmInferenceClient&, bool)``
- In ``pipeline_manager.cpp``, add the new ``pipeline_type`` string to the dispatch
  block in ``run_from_json_file()``
- Add ``src/my_pipeline.cpp`` to ``EDGE_AI_SOURCES`` in
  ``example/edge-ai/CMakeLists.txt``

See :ref:`Linux Audio Inference Application <am62dx_linux_audio_inference_app>` for the
full pipeline configuration reference.

Step 4: GStreamer Plugin
=========================

The GStreamer plugin requires no source changes to use a new model if the pipeline
follows an existing shape (classification or speech enhancement) and the firmware
``ModelId`` is already assigned.

**For a new model with an existing pipeline shape:**

Set these ``tidspkernel`` properties explicitly in the ``gst-launch-1.0`` command
(path-based auto-detection only covers the five reference models):

- ``selected-model`` — firmware ``ModelId`` integer assigned in Step 2
- ``model-elems`` — floats per spectral frame produced by the DSP
- ``hop-size``, ``fft-size``, ``window-frames`` — spectral layout matching the firmware

**To add auto-detection for the new model (optional):**

In ``gstdspkernel.cpp``, add an entry to the ``known_models[]`` table with the path
substring, ``selected_model``, ``model_elems``, ``fft_size``, ``hop_size``, and
``window_frames``. The ``gst_dsp_kernel_detect_model()`` function will then auto-set
these when ``model-path`` contains your model's directory name.

**To add a new plugin property (only if the model needs a new parameter):**

For ``tidspkernel``:

- ``gstdspkernel.h`` — add the field to ``struct _GstDspKernel``
- ``gstdspkernel.cpp`` — add to the ``PROP_*`` enum, register with
  ``g_object_class_install_property()`` in ``class_init()``, handle in
  ``set_property()`` / ``get_property()``, and pass to the DSP request struct

For ``titvm``:

- ``gsttitvm.h`` — add the field to ``struct _GstTiTvm``
- ``gsttitvm.cpp`` — same pattern: enum, ``class_init()``, ``set_property()``,
  ``get_property()``, and use in inference post-processing

See :ref:`Audio AI Using GStreamer <pub_edgeai_am62dx_getting_started>` for the full
pipeline command reference and element property details.

Summary
=======

.. list-table::
   :header-rows: 1
   :widths: 15 45 40

   * - Step
     - Key task
     - Reference
   * - 1. Compile
     - Produce ``deploy_graph.json``, ``deploy_lib.so``, ``deploy_param.params``
     - :ref:`Model Compile and Evaluate <audioai-compile-evaluate>`
   * - 2. Firmware
     - Add ``ModelId``, implement ``StftSignalChain<MODEL>``, register in
       ``signal_chain_get_ops()``
     - MCU+ SDK: Edge AI Add New Model
   * - 3. Linux app
     - Add pipeline JSON; optionally add new ``run_*_pipeline()`` in C++
     - :ref:`Linux Audio Inference Application <am62dx_linux_audio_inference_app>`
   * - 4. GStreamer
     - Set spectral properties explicitly; optionally extend ``known_models[]`` table
     - :ref:`Audio AI Using GStreamer <pub_edgeai_am62dx_getting_started>`
