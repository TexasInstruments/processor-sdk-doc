Neo-AI Deep Learning Runtime
============================

.. ifconfig:: CONFIG_part_family in ('General_family', 'AM335X_family', 'AM437X_family')

  .. rubric:: Introduction
   :name: Introduction-neo-sitara

  `Neo-AI-DLR <https://github.com/neo-ai/neo-ai-dlr>`__ is an open source common runtime
  for deep learning models and decision tree models compiled by TVM, AWS SageMaker Neo,
  or Treelite. |__SDK_FULL_NAME__| has integrated Neo-AI-DLR. DLR stands for Deep Learning
  Runtime. With this integration, the models compiled by AWS SageMaker Neo and TVM can run
  on all Arm core of all Sitara devices (AM3/AM4/AM5/AM6).

  On A5729 and AM5749, TensorFlow models compiled by Neo, if supported by TIDL, are fully
  offloaded to EVE and DSP cores. If not, then they run on Arm core. In future release,
  a graph of any model supported by Neo compiler can be split into sub-graphs, where TIDL
  supported sub-graph will run on EVE/DSP cores, while unsupported layer sub-graph will
  run on Arm core.

  .. rubric:: Examples
   :name: Examples-neo-sitara

  Examples of running inference with Neo-AI-DLR are available in /usr/share/dlr
  of the target filesystem:

  - demos folder: contains examples of Neo-AI-DLR on top of TIDL, which can only
    run on AM5729/49 devices. To run the examples, a neural network model must be
    compiled to generate runtime artifacts according to instructions in
    :ref:`Compiling Network Models`. Once a model is compiled, copy the generated
    artifacts to this folder and run one of the examples, e.g:

  ::

    cd /usr/share/dlr/demos
    Copy artifact, e.g. scp -r <TVM_on_host_machine>/apps/tidl_deploy/output4/mobileNet2 .
    Edit subgraph0.cfg and add the following lines at the end of the file:
        inConvType = 0
        inIsSigned = 1
        inScaleF2Q = 128.0
        inIsNCHW = 0
        outConvType = 0
        outIsSigned = 0
        outScaleF2Q = 255.0
        outIsNCHW = 1
    ./do_tidl4.sh mobileNet2

  For more information about running examples of Neo-Ai-DLR with TIDL, please refer
  to `Neo-ai-dlr Texas Instruments branch in github <https://github.com/TexasInstruments/neo-ai-dlr/tree/dev/examples/tidl>`__.

  - tests folder: contains examples of Neo runtime for ARM cores, which can run on
    any Sitara device. Go to folder python/integration and run the example (http_proxy
    needs to be set properly):

  ::

    cd /usr/share/dlr/tests/python/integration/
    python3 load_and_run_tvm_model.py


  .. _Compiling Network Models:

  .. rubric:: Compiling Network Models to Run with DLR
   :name: Compiling-Network-Models-neo

  SageMaker Neo compiler can compile neural network models to run with DLR on Sitara devices.
  Neo compiler source code supporting Sitara devices is hosted at https://github.com/TexasInstruments/tvm
  and will be periodically upstreamed to https://github.com/neo-ai/tvm.

  - Build Neo Compiler from source

  ::

      git clone --recursive https://github.com/TexasInstruments/tvm.git --branch dev
      cd tvm/
      mkdir build && cd build
      cp ../cmake/config.cmake .
      cmake ..
      make –j8

  - Install Python Package

  Follow instructions at https://docs.tvm.ai/install/from_source.html#python-package-installation for installation.

  - Compile Neural Network Models

  Follow instructions at https://github.com/TexasInstruments/tvm/tree/dev/apps/tidl_deploy to
  compile neural network models. A simple example generating the artifacts needed
  to run the demo above is shown below:

  ::

    python3 NeoTvmCodeGen.py mobileNet2

  .. note::

    - Currently Neo compiler with Sitara support can compile any models supported by Neo,
      but only TensorFlow models can be compiled to run on TIDL for acceleration if the model
      can be supported by TIDL.

  .. rubric:: Benchmarking
   :name: Benchmarking-neo

  Performance with and without TIDL offload is shown below for TensorFlow MobileNet v1 and v2. The performance depends
  significantly on batch size (if batch size is 1, only one EVE is operating and performance would be very poor).

  ==========    ======================    =====================    ======================    =====================
  Batch Size    TIDL MobileNetV1 (fps)    ARM MobileNetV1 (fps)    TIDL MobileNetV2 (fps)    ARM MobileNetV2 (fps)
  ==========    ======================    =====================    ======================    =====================
     4                 30.1260                  2.2018                    30.5178                   3.6843
     16                34.8465                  2.2210                    36.0127                   3.6775
     32                35.5279                                            37.5482
  ==========    ======================    =====================    ======================    =====================

  .. note::

     - This release only supports batch size up to 32.
     - There is no TVM auto-tuning for ARM (using default scheduling) and it is single A15 core execution.

  .. rubric:: Rebuilding DLR from Source
   :name: Rebuilding-DLR-from-Source-neo

  DLR for Sitara devices is included in Proc-SDK Linux target file system. Source
  code is hosted at https://github.com/TexasInstruments/neo-ai-dlr and will be periodically
  upstreamed to https://github.com/neo-ai/neo-ai-dlr. Users may rebuild the latest
  source code before official Proc-SDK release, following steps below:

  - Clone git repo on x86 host to target NFS (git cloning may not work on EVM):

  ::

      git clone --recursive https://github.com/TexasInstruments/neo-ai-dlr.git --branch dev

  - Build and Install DLR on AM57x9 EVM:

  ::

      cd neo-ai-dlr
      mkdir build && cd build
      cmake ..
      make –j2
      make demo democv
      cd ../python
      python3 setup.py install --user

.. ifconfig:: CONFIG_part_family in ('J7_family')

  .. rubric:: Introduction
   :name: Introduction-neo-jacinto

  `Neo-AI-DLR <https://github.com/neo-ai/neo-ai-dlr>`__ is an open source common runtime
  for deep learning models and decision tree models compiled by TVM, AWS SageMaker Neo,
  or Treelite. Processor SDK has integrated Neo-AI-DLR. DLR stands for Deep Learning
  Runtime. With this integration user has below option to compile models for Jacinto devices.

      -  `AWS SageMaker neo Services  <https://aws.amazon.com/sagemaker/neo/>`__
      -  `Offline TVM Compiler <https://github.com/TexasInstruments/tvm.git>`__


  .. rubric:: Examples
   :name: Examples-neo-jacinto

  Examples of running inference with Neo-AI-DLR are available in /usr/share/dlr
  of the target filesystem:

  ::

    cd /usr/share/dlr/tests/python/integration/
    python3 load_and_run_tvm_model.py

  .. note::

     `The Processor SDK RTOS <http://software-dl.ti.com/jacinto7/esd/processor-sdk-rtos-jacinto7/latest/index_FDS.html>`__
     also implements Heterogeneous Execution of CNN models on A72 and C7x-MMA using the  `TVM <https://tvm.apache.org/>`__
     runtime and `Neo-AI-DLR <https://github.com/neo-ai/neo-ai-dlr>`__  runtime. This heterogeneous execution enables

       - TVM/Neo-AI-DLR as the top level inference API for user applications
       - Offloading subgraphs to C7x/MMA for accelerated execution with TIDL
       - Generating code and running on the ARM A72 core for layers that are not supported by TIDL

     Please refer to the section **Open Source Runtime->TVM/Neo-AI-DLR + TIDL Heterogeneous Execution** in TIDL user guide
     (SDK components) for detailed instruction on usage.
