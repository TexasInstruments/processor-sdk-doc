.. _onnx-runtime:

ONNX Runtime
============

Introduction
------------

ONNX Runtime is a cross-platform machine-learning model accelerator, with a flexible interface to
integrate hardware-specific libraries. ONNX Runtime is compatible with different hardware, drivers,
and operating systems, and provides optimal performance by leveraging hardware accelerators where
applicable alongside graph optimizations and transforms.

ONNX Runtime can be used with models from PyTorch, Tensorflow/Keras, TFLite, and other frameworks.

https://onnxruntime.ai/

Supported version
-----------------

  - ONNX Runtime 1.20.1

ONNX Runtime test applications
------------------------------

ONNX Runtime test applications are installed in the SDK filesystem at /usr/bin/onnxruntime-tests/examples.

Running benchmark_model
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    # /usr/bin/onnxruntime-tests/onnxruntime_perf_test
    usage: perf_test [options...] model_path [result_file]
    Options:
	-m [test_mode]: Specifies the test mode. Value could be 'duration' or 'times'.
		Provide 'duration' to run the test for a fix duration, and 'times' to repeated for a certain times. 
	-M: Disable memory pattern.
	-A: Disable memory arena
	-I: Generate tensor input binding (Free dimensions are treated as 1.)
	-c [parallel runs]: Specifies the (max) number of runs to invoke simultaneously. Default:1.
	-e [cpu|cuda|dnnl|tensorrt|openvino|dml|acl|nnapi|coreml|qnn|snpe|rocm|migraphx|xnnpack|vitisai|webgpu]: Specifies the provider 'cpu','cuda','dnnl','tensorrt', 'openvino', 'dml', 'acl', 'nnapi', 'coreml', 'qnn', 'snpe', 'rocm', 'migraphx', 'xnnpack', 'vitisai' or 'webgpu'. Default:'cpu'.
	-b [tf|ort]: backend to use. Default:ort
	-r [repeated_times]: Specifies the repeated times if running in 'times' test mode.Default:1000.
	-t [seconds_to_run]: Specifies the seconds to run for 'duration' mode. Default:600.
	-p [profile_file]: Specifies the profile name to enable profiling and dump the profile data to the file.
	-s: Show statistics result, like P75, P90. If no result_file provided this defaults to on.
	-S: Given random seed, to produce the same input data. This defaults to -1(no initialize).
	-v: Show verbose information.
	-x [intra_op_num_threads]: Sets the number of threads used to parallelize the execution within nodes, A value of 0 means ORT will pick a default. Must >=0.
	-y [inter_op_num_threads]: Sets the number of threads used to parallelize the execution of the graph (across nodes), A value of 0 means ORT will pick a default. Must >=0.
	-f [free_dimension_override]: Specifies a free dimension by name to override to a specific value for performance optimization. Syntax is [dimension_name:override_value]. override_value must > 0
	-F [free_dimension_override]: Specifies a free dimension by denotation to override to a specific value for performance optimization. Syntax is [dimension_denotation:override_value]. override_value must > 0
	-P: Use parallel executor instead of sequential executor.
	-o [optimization level]: Default is 99 (all). Valid values are 0 (disable), 1 (basic), 2 (extended), 99 (all).
		Please see onnxruntime_c_api.h (enum GraphOptimizationLevel) for the full list of all optimization levels.
	-u [optimized_model_path]: Specify the optimized model path for saving.
	-d [CUDA only][cudnn_conv_algorithm]: Specify CUDNN convolution algorithms: 0(benchmark), 1(heuristic), 2(default). 
	-q [CUDA only] use separate stream for copy. 
	-z: Set denormal as zero. When turning on this option reduces latency dramatically, a model may have denormals.
	-C: Specify session configuration entries as key-value pairs: -C "<key1>|<value1> <key2>|<value2>" 
	    Refer to onnxruntime_session_options_config_keys.h for valid keys and values. 
	    [Example] -C "session.disable_cpu_ep_fallback|1 ep.context_enable|1" 
	-i: Specify EP specific runtime options as key value pairs. Different runtime options available are: 
	    [Usage]: -e <provider_name> -i '<key1>|<value1> <key2>|<value2>'

	    [ACL only] [enable_fast_math]: Options: 'true', 'false', default: 'false', 

	-T [Set intra op thread affinities]: Specify intra op thread affinity string
	 [Example]: -T 1,2;3,4;5,6 or -T 1-2;3-4;5-6 
		 Use semicolon to separate configuration between threads.
		 E.g. 1,2;3,4;5,6 specifies affinities for three threads, the first thread will be attached to the first and second logical processor.
		 The number of affinities must be equal to intra_op_num_threads - 1

	-D [Disable thread spinning]: disable spinning entirely for thread owned by onnxruntime intra-op thread pool.
	-Z [Force thread to stop spinning between runs]: disallow thread from spinning during runs to reduce cpu usage.
	-n [Exit after session creation]: allow user to measure session creation time to measure impact of enabling any initialization optimizations.
	-l Provide file as binary in memory by using fopen before session creation.
	-R [Register custom op]: allow user to register custom op by .so or .dll file.
	-h: help

Example of running *onnxruntime_perf_test* on target using the pre-installed mobilenet_v3_small_excerpt.onnx model:

.. code-block:: console

    # /usr/bin/onnxruntime-tests/onnxruntime_perf_test -I -m times -r 8 -e acl -P /usr/bin/onnxruntime-tests/testdata/mobilenet_v3_small_excerpt.onnx
    Session creation time cost: 0.0273071 s
    First inference time cost: 20 ms
    Total inference time cost: 0.14188 s
    Total inference requests: 8
    Average inference time cost: 17.735 ms
    Total inference run time: 0.141991 s
    Number of inferences per second: 56.3415 
    Avg CPU usage: 98 %
    Peak working set size: 35299328 bytes
    Avg CPU usage:98
    Peak working set size:35299328
    Runs:8
    Min Latency: 0.0159831 s
    Max Latency: 0.0232702 s
    P50 Latency: 0.0167086 s
    P90 Latency: 0.0232702 s
    P95 Latency: 0.0232702 s
    P99 Latency: 0.0232702 s
    P999 Latency: 0.0232702 s
