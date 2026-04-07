.. _tflite-label:

########################
TensorFlow Lite (LiteRT)
########################

************
Introduction
************

LiteRT, formerly known as TensorFlow Lite, is an open-source library designed for running machine learning models on mobile and embedded devices.
|__SDK_FULL_NAME__| has integrated open-source `TensorFlow Lite <https://www.tensorflow.org/lite>`__ for deep learning inference at the edge.
TensorFlow Lite runs on Arm for Sitara devices (AM3/AM4/AM5/AM6).

It supports on-device inference with low latency and a compact binary size. You can find more information at `TensorFlow Lite <https://www.tensorflow.org/lite>`__

********
Features
********

  - TensorFlow Lite v2.20.0 via Yocto - `meta-arago-extras/recipes-framework/tensorflow-lite/tensorflow-lite_2.20.0.bb <https://web.git.yoctoproject.org/meta-arago/tree/meta-arago-extras/recipes-framework/tensorflow-lite/tensorflow-lite_2.18.0.bb?h=11.00.09>`__
  - Multithreaded computation with acceleration using Arm Neon SIMD instructions on Cortex-A cores
  - C++ Library and Python interpreter (supported Python version 3)
  - TensorFlow Lite Model benchmark Tool (i.e. :command:`benchmark_model`)

********************************
Inference backends and delegates
********************************

An inference backend is a compute engine designed for the efficient execution of machine learning models on edge devices.
TensorFlow Lite provides options to enable various backends using the delegate mechanism.

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62PX', 'AM62LX', 'AM64X', 'AM65X')

   .. figure:: /images/TFLite-arm-only-armv8-sw-stack.png
      :height: 670
      :width: 1020


.. ifconfig:: CONFIG_part_variant in ('AM335X', 'AM437X')

   .. figure:: /images/TFLite-arm-only-armv7-sw-stack.png
      :height: 670
      :width: 1020

Built-in kernels / CPU Delegate
===============================

The default inference backend for TensorFlow Lite is the CPU, utilizing reference kernels from its implementation.
These built-in kernels fully support the TensorFlow Lite operator set.

XNNPACK Delegate
================

The `XNNPACK library <https://github.com/google/XNNPACK>`__ is a highly optimized collection of floating-point quantized neural network inference operators.
It can be accessed through the XNNPACK delegate in TensorFlow Lite, with computations performed on the CPU.
This library offers optimized implementations for a subset of TensorFlow Lite operators.

.. note::

   The XNNPACK delegate is not supported for ARMv7-based platforms like AM335x and AM437x.
   Refer `XNNPACK supported architectures <https://github.com/google/XNNPACK?tab=readme-ov-file#supported-architectures>`__ for more details.

*******************************
Benchmark Tool for TFLite Model
*******************************

The :file:`tisdk-default-image` wic image from |__SDK_DOWNLOAD_URL__| by default contains a pre-installed benchmarking application named :command:`benchmark_model`.
It's a C++ binary designed to benchmark a TFLite model and its individual operators. It takes a TFLite model, generates random inputs, and repeatedly runs the model
for a specified number of runs. After running the benchmark, it reports aggregate latency statistics.

The :file:`benchmark_model` binary is located at :file:`/opt/tensorflow-lite/tools/`.
Refer `TFLite Model Benchmark Tool - README <https://github.com/tensorflow/tensorflow/blob/v2.18.0/tensorflow/lite/tools/benchmark/README.md#parameters>`__ for more
details.

How to run benchmark using CPU delegate
=======================================

To execute the benchmark using CPU for computation, use the following command:

.. code-block:: console

   root@<machine>:~# /opt/tensorflow-lite/tools/benchmark_model --graph=/usr/share/oob-demo-assets/models/ssd_mobilenet_v2_coco.tflite --use_xnnpack=false

The output of the benchmarking application should be similar to:

.. code-block:: console

   root@am62xx-evm:~# /opt/tensorflow-lite/tools/benchmark_model --graph=/usr/share/oob-demo-assets/models/ssd_mobilenet_v2_coco.tflite --num_threads=4 --use_xnnpack=false
   INFO: STARTING!
   INFO: Log parameter values verbosely: [0]
   INFO: Graph: [/usr/share/oob-demo-assets/models/ssd_mobilenet_v2_coco.tflite]
   INFO: Signature to run: []
   INFO: Use xnnpack: [0]
   INFO: Loaded model /usr/share/oob-demo-assets/models/ssd_mobilenet_v2_coco.tflite
   INFO: The input model file size (MB): 67.3128
   INFO: Initialized session in 5.579ms.
   INFO: Running benchmark for at least 1 iterations and at least 0.5 seconds but terminate if exceeding 150 seconds.
   INFO: count=1 curr=1357602 p5=1357602 median=1357602 p95=1357602

   INFO: Running benchmark for at least 50 iterations and at least 1 seconds but terminate if exceeding 150 seconds.
   INFO: count=50 first=1249964 curr=1240143 min=1238588 max=1252566 avg=1.24027e+06 std=2565 p5=1238753 median=1239807 p95=1247415

   INFO: Inference timings in us: Init: 5579, First inference: 1357602, Warmup (avg): 1.3576e+06, Inference (avg): 1.24027e+06
   INFO: Note: as the benchmark tool itself affects memory footprint, the following is only APPROXIMATE to the actual memory footprint of the model at runtime. Take the information at your discretion.
   INFO: Memory footprint delta from the start of the tool (MB): init=6.36328 overall=109.832

Where,

* ``/opt/tensorflow-lite/tools/benchmark_model``: This is the path to the benchmark_model binary, which is used to benchmark TensorFlow Lite models.
* ``--graph=/usr/share/oob-demo-assets/models/ssd_mobilenet_v2_coco.tflite``: Specifies the path to the TFLite model file to be benchmarked. In this case, it's an SSD MobileNet V2 model trained on the COCO dataset.
* ``--use_xnnpack=false``: Disables the use of the XNNPACK delegate for optimized CPU inference. The model will run without XNNPACK optimizations.
* ``--num_threads=4``: Sets the number of threads to use for inference. In this case, it uses 4 threads.

How to run benchmark using XNNPACK delegate
===========================================

To execute the benchmark with the XNNPACK delegate, use the following command:

.. code-block:: console

   root@<machine>:~# /opt/tensorflow-lite/tools/benchmark_model --graph=/usr/share/oob-demo-assets/models/ssd_mobilenet_v2_coco.tflite --use_xnnpack=true

The output of the benchmarking application should be similar to,

.. code-block:: console

   root@am62xx-evm:~# /opt/tensorflow-lite/tools/benchmark_model --graph=/usr/share/oob-demo-assets/models/ssd_mobilenet_v2_coco.tflite --num_threads=4 --use_xnnpack=true
   INFO: STARTING!
   INFO: Log parameter values verbosely: [0]
   INFO: Graph: [/usr/share/oob-demo-assets/models/ssd_mobilenet_v2_coco.tflite]
   INFO: Signature to run: []
   INFO: Use xnnpack: [1]
   INFO: Loaded model /usr/share/oob-demo-assets/models/ssd_mobilenet_v2_coco.tflite
   INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
   INFO: XNNPACK delegate created.
   INFO: Explicitly applied XNNPACK delegate, and the model graph will be partially executed by the delegate w/ 1 delegate kernels.
   INFO: The input model file size (MB): 67.3128
   INFO: Initialized session in 614.333ms.
   INFO: Running benchmark for at least 1 iterations and at least 0.5 seconds but terminate if exceeding 150 seconds.
   INFO: count=1 curr=905463 p5=905463 median=905463 p95=905463
   INFO: Running benchmark for at least 50 iterations and at least 1 seconds but terminate if exceeding 150 seconds.
   INFO: count=50 first=900416 curr=898333 min=898007 max=906121 avg=899641 std=1549 p5=898333 median=899281 p95=904305
   INFO: Inference timings in us: Init: 614333, First inference: 905463, Warmup (avg): 905463, Inference (avg): 899641
   INFO: Note: as the benchmark tool itself affects memory footprint, the following is only APPROXIMATE to the actual memory footprint of the model at runtime. Take the information at your discretion.
   INFO: Memory footprint delta from the start of the tool (MB): init=146.363 overall=150.141


Where,

* ``--use_xnnpack=true``: Enables the use of the XNNPACK delegate for optimized CPU inference. The model will run with XNNPACK optimizations.

*************************************
Performance Numbers of Benchmark Tool
*************************************

The following performance numbers are captured with :command:`benchmark_model` on different SoCs using :file:`/usr/share/oob-demo-assets/models/ssd_mobilenet_v2_coco.tflite` model
& setting ``--num_threads`` to max value (i.e. number of Cortex-A core)

.. csv-table:: Performance Benchmarks of TFLite on Different SoCs
   :header: "SOC", "Delegates", "Inference Time (sec)", "Initialization Time (ms)", "Overall Memory Footprint (MB)"
   :widths: 10, 10, 20, 20, 20

   "AM62X", "CPU only", "1.24027", "5.579", "109.832"
   "", "XNNPACK", "0.899641", "614.333", "150.141"
   "AM62PX", "CPU only", "1.23341", "252.390", "111.121"
   "", "XNNPACK", "0.875280", "597.639", "150.52"
   "AM64X", "CPU only", "1.26429", "135.579", "110.188"
   "", "XNNPACK", "0.740743", "885.636", "150.484"
   "AM62L", "CPU only", "1.3708", "807.076", "111.152"
   "", "XNNPACK", "0.930577", "769.145", "150.496"

Based on the above data, using the XNNPACK delegate significantly improves inference times across all SoCs, though it generally increases initialization time and overall memory footprint.

.. note::

   The performance numbers mentioned above were recorded after stopping the out-of-box (OOB) demos included in the TI SDK.

********************
Example Applications
********************

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62LX', 'AM62PX')

   |__SDK_FULL_NAME__| has integrated opensource components like NNStreamer which can be used for neural network inferencing using the sample tflite models under :file:`/usr/share/oob-demo-assets/models/`
   Checkout the Object Detection usecase under :ref:`TI Apps Launcher - User Guide <TI-Apps-Launcher-User-Guide-label>`

   Alternatively, if a display is connected, you can run the Object Detection pipeline using this command,

.. ifconfig:: CONFIG_part_variant in ('AM62X', 'AM62LX')

   .. code-block:: console

      gst-launch-1.0 multifilesrc location=/usr/share/oob-demo-assets/videos/oob-gui-video-objects.h264 loop=true ! \
      h264parse ! avdec_h264 ! \
      tee name=tee_split0 \
      tee_split0. ! \
          queue ! \
          videoconvertscale ! video/x-raw,width=300,height=300,format=RGB ! \
          tensor_converter ! \
          tensor_transform mode=arithmetic option=typecast:float32,add:-127.5,div:127.5 ! \
          tensor_filter framework=tensorflow2-lite model=/usr/share/oob-demo-assets/models/ssd_mobilenet_v2_coco.tflite custom=Delegate:XNNPACK,NumThreads:4 latency=1 ! \
          tensor_decoder \
          mode=bounding_boxes \
              option1=mobilenet-ssd \
              option2=/usr/share/oob-demo-assets/labels/coco_labels.txt \
              option3=/usr/share/oob-demo-assets/labels/box_priors.txt \
              option4=1280:720 \
              option5=300:300 ! \
          mix.sink_0 \
      tee_split0. ! \
          queue ! \
          mix.sink_1 \
      compositor name=mix sink_0::zorder=2 sink_1::zorder=1 ! \
      kmssink name=sink

   The above GStreamer pipeline reads an H.264 video file, decodes it, and processes it for object detection using a TensorFlow Lite model, displaying bounding boxes around detected objects. The processed video is then composited and rendered on the screen using the ``kmssink`` element.

.. ifconfig:: CONFIG_part_variant in ('AM62PX')

   .. code-block:: console

      gst-launch-1.0 multifilesrc location=/usr/share/oob-demo-assets/videos/oob-gui-video-objects.h264 loop=true caps=video/x-h264,width=1280,height=720,framerate=1/1 ! \
      h264parse ! v4l2h264dec capture-io-mode=4 ! \
      tee name=tee_split0 \
      tee_split0. ! \
          queue ! \
          videoconvertscale ! video/x-raw,width=300,height=300,format=RGB ! \
          tensor_converter ! \
          tensor_transform mode=arithmetic option=typecast:float32,add:-127.5,div:127.5 ! \
          tensor_filter framework=tensorflow2-lite model=/usr/share/oob-demo-assets/models/ssd_mobilenet_v2_coco.tflite custom=Delegate:XNNPACK,NumThreads:4 latency=1 ! \
          tensor_decoder \
          mode=bounding_boxes \
              option1=mobilenet-ssd \
              option2=/usr/share/oob-demo-assets/labels/coco_labels.txt \
              option3=/usr/share/oob-demo-assets/labels/box_priors.txt \
              option4=1280:720 \
              option5=300:300 ! \
          mix.sink_0 \
      tee_split0. ! \
          queue ! \
          mix.sink_1 \
      compositor name=mix sink_0::zorder=2 sink_1::zorder=1 ! \
      kmssink name=sink

   The above GStreamer pipeline reads an H.264 video file, decodes it, and processes it for object detection using a TensorFlow Lite model, displaying bounding boxes around detected objects. The processed video is then composited and rendered on the screen using the ``kmssink`` element.

.. ifconfig:: CONFIG_part_variant in ('AM62DX')

   |__SDK_FULL_NAME__| has integrated opensource components like NNStreamer which can be used for neural network inferencing using the sample TensorFlow Lite models under :file:`/usr/share/oob-demo-assets/models/`

   If an audio input device is connected, you can run the Audio Classification pipeline using this command:

      .. code-block:: console

         gst-launch-1.0 \
         alsasrc ! \
         audioconvert ! \
         audioresample ! \
         audio/x-raw,format=S16LE,channels=1,rate=16000,layout=interleaved ! \
         tensor_converter frames-per-tensor=3900 ! \
         tensor_aggregator \
               frames-in=3900 \
               frames-out=15600 \
               frames-flush=3900 \
               frames-dim=1 ! \
         tensor_transform \
               mode=arithmetic \
               option=typecast:float32,add:0.5,div:32767.5 ! \
         tensor_transform \
               mode=transpose \
               option=1:0:2:3 ! \
         queue \
               leaky=2 \
               max-size-buffers=10 ! \
         tensor_filter \
               framework=tensorflow2-lite \
               model=/usr/share/oob-demo-assets/models/yamnet_audio_classification.tflite \
               custom=Delegate:XNNPACK,NumThreads:2 ! \
         tensor_decoder \
               mode=image_labeling \
               option1=/usr/share/oob-demo-assets/labels/yamnet_label_list.txt ! \
         filesink \
               buffer-mode=2 \
               location=/dev/stdout

   The above GStreamer pipeline captures real-time audio from an ALSA source, converts it to the required format, and processes it for audio event classification using the YAMNet TensorFlow Lite model. The audio data is aggregated into tensors, normalized for machine learning input, and classified to identify various audio events and sounds. The classification results are decoded to human-readable labels and output to stdout.

.. attention::

   The Example Applications section is not applicable for AM64x
