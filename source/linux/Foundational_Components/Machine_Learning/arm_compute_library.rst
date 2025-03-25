Arm Compute Library
===================

Introduction
-------------
Arm Compute Library is a set of libraries that accelerate Machine Learning on Arm CPUs, optimized for NEON SIMD architecture.

Exact list of functions can be found at https://www.arm.com/products/development-tools/embedded-and-software/compute-library.

Supported versions
------------------

  - ARM Compute Library 24.12

Arm Compute Library Testing
---------------------------

Arm Compute Libraries, tests, and sample executables are included in the SDK filesystem.

.. code-block:: console

    root@am62xx-evm:~# LD_LIBRARY_PATH=/usr/lib/tests/ /usr/lib/tests/arm_compute_validation
    Version = 32bcced2af7feea6969dd1d22e58d0718dc488e3
    CommandLine = /usr/lib/tests/arm_compute_validation 
    Seed = 3778037091
    cpu_has_sve = false
    cpu_has_sve2 = false
    cpu_has_svef32mm = false
    cpu_has_svei8mm = false
    cpu_has_svebf16 = false
    cpu_has_sme = false
    cpu_has_sme2 = false
    cpu_has_fp16 = false
    cpu_has_bf16 = false
    cpu_has_dotprod = false
    cpu_has_i8mm = false
    CPU0 = A53
    CPU1 = A53
    CPU2 = A53
    CPU3 = A53
    Iterations = 1
    Threads = 1
    Dataset mode = PRECOMMIT
    Running [0] 'UNIT/CPPScheduler/RethrowException'
    Wall clock/Wall clock time:    AVG=3466.0000 us


.. code-block:: console

    root@am62xx-evm:~# /usr/bin/arm-compute-library-24.12/examples/graph_alexnet

    /usr/bin/arm-compute-library-24.12/examples/graph_alexnet

    Threads : 1
    Target : Neon
    Data type : F32
    Data layout : NHWC
    Tuner enabled? : false
    Cache enabled? : false
    Tuner mode : Normal
    Tuner file : 
    MLGO file : 
    Fast math enabled? : false

    Test passed


Sample NN related executables (using Arm Compute Library only):

.. code-block:: console

    root@am62xx-evm:~# ls /usr/bin/arm-compute-library-24.12/examples/graph_*
    graph_alexnet              graph_inception_v4         graph_resnext50            graph_vgg19
    graph_deepspeech_v0_4_1    graph_lenet                graph_shufflenet           graph_vgg_vdsr
    graph_edsr                 graph_mobilenet            graph_squeezenet           graph_yolov3
    graph_googlenet            graph_mobilenet_v2         graph_squeezenet_v1_1
    graph_inception_resnet_v1  graph_resnet12             graph_srcnn955
    graph_inception_resnet_v2  graph_resnet50             graph_ssd_mobilenet
    graph_inception_v3         graph_resnet_v2_50         graph_vgg16

.. code-block:: console

    root@am62xx-evm:~# ls /usr/bin/arm-compute-library-24.12/examples/neon_*
    neon_cnn           neon_copy_objects  neon_gemm_qasymm8  neon_gemm_s8_f32   neon_permute       neon_scale         neon_sgemm
