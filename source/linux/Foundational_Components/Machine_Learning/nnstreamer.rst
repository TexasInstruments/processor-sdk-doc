NNStreamer
==========

Introduction
-------------
NNStreamer is a set of Gstreamer plugins that allow Gstreamer developers to adopt neural network models easily and efficiently and neural network developers to manage neural network pipelines and their filters easily and efficiently.

https://nnstreamer.ai/

Supported versions
------------------

  - NNStreamer 2.4.2

Testing NNStreamer
------------------

.. code-block:: console

    root@am62xx-evm:~# nnstreamer-check
    NNStreamer version: 2.4.2
               loaded : TRUE
               path   : /usr/lib/gstreamer-1.0/libnnstreamer.so
    ...

Run the included unit tests:

.. code-block:: console

    root@am62xx-evm:~# NNSTREAMER_SOURCE_ROOT_PATH=/usr/bin/unittest-nnstreamer /usr/bin/unittest-nnstreamer/tests/unittest_filter_onnxruntime
    [==========] Running 10 tests from 1 test suite.
    [----------] Global test environment set-up.
    [----------] 10 tests from nnstreamerFilterOnnxRuntime
    [ RUN      ] nnstreamerFilterOnnxRuntime.openClose00
    ...

To list available elements:

.. code-block:: console
      
    root@am62xx-evm:~# gst-inspect-1.0 | grep nnstreamer
    nnstreamer:  tensor_aggregator: TensorAggregator
    nnstreamer:  tensor_converter: TensorConverter
    nnstreamer:  tensor_crop: TensorCrop
    nnstreamer:  tensor_debug: TensorDebug
    nnstreamer:  tensor_decoder: TensorDecoder
    nnstreamer:  tensor_demux: TensorDemux
    nnstreamer:  tensor_filter: TensorFilter
    nnstreamer:  tensor_if: TensorIf
    nnstreamer:  tensor_merge: TensorMerge
    nnstreamer:  tensor_mux: TensorMux
    nnstreamer:  tensor_rate: TensorRate
    nnstreamer:  tensor_reposink: TensorRepoSink
    nnstreamer:  tensor_reposrc: TensorRepoSrc
    nnstreamer:  tensor_sink: TensorSink
    nnstreamer:  tensor_sparse_dec: TensorSparseDec
    nnstreamer:  tensor_sparse_enc: TensorSparseEnc
    nnstreamer:  tensor_split: TensorSplit
    nnstreamer:  tensor_src_iio: TensorSrcIIO
    nnstreamer:  tensor_trainer: TensorTrainer
    nnstreamer:  tensor_transform: TensorTransform

For details information on an element:

.. code-block:: console

    root@am62xx-evm:~# gst-inspect-1.0 tensor_filter
    Factory Details:
      Rank                     none (0)
      Long-name                TensorFilter
      Klass                    Filter/Tensor
    ...

Example:

.. code-block:: console

    root@am62xx-evm:~# gst-launch-1.0 \
        filesrc location=/usr/bin/unittest-nnstreamer/tests/test_models/data/orange.png ! \
        pngdec ! \
        videoconvert ! video/x-raw,format=RGB,width=224,height=224 ! \
        tensor_converter ! \
        tensor_transform mode=transpose option=1:2:0:3 ! \
        tensor_transform mode=arithmetic option=typecast:float32,div:127.5,add:-1.0 ! \
        tensor_filter framework=onnxruntime model=/usr/bin/unittest-nnstreamer/tests/test_models/models/mobilenet_v2_quant.onnx ! \
        tensor_decoder mode=image_labeling option1=/usr/bin/unittest-nnstreamer/tests/test_models/labels/labels.txt ! \
        filesink buffer-mode=2 location=/dev/stderr 1> /dev/null && echo
