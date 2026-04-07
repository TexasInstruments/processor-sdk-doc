.. _foundational-components-machine-learning:

********************
Machine Learning
********************

   Sitara Machine Learning toolkit brings machine learning to the edge by enabling
   machine learning inference on all Sitara devices (Arm-only, Arm + GPU, and Arm + specialized hardware
   accelerators). It is provided as part of TI's Processor SDK Linux, free to download
   and use. Sitara machine learning today consists of ONNX Runtime, TensorFlow Lite, Arm NN,
   NNStreamer, and RNN library.

   .. figure:: ../images/Sitara_machine_learning_stack_diagram.png
       :align: center

       Sitara Machine Learnining Offering


   .. rubric:: `TensorFlow Lite <Foundational_Components/Machine_Learning/tflite.html>`__

   * Open source deep learning runtime for on-device inference.
   * Runs on all Cortex-A ARM cores (AM3x, AM4x, AM6x Sitara devices).
   * Imports Tensorflow Lite models.
   * Uses TIDL import tool to create TIDL offloadable Tensorflow Lite models,
     which can be executed via Tensorflow Lite runtime with TIDL acceleration.

   .. rubric:: `ONNX Runtime <Foundational_Components/Machine_Learning/onnxrt.html>`__

   * Open source inference engine available from Arm.
   * Runs on all Cortex-A ARM cores (AM3x, AM4x, AM6x Sitara devices).

   .. rubric:: `Arm NN <Foundational_Components/Machine_Learning/armnn.html>`__

   * Open source inference engine available from Arm.
   * Runs on all Cortex-A ARM cores (AM3x, AM4x, AM6x Sitara devices).
   * Imports ONNX and TensorFlow Lite models.
   * Provides TensorFlow Lite delegate.

   .. rubric:: `Arm Compute Library <Foundational_Components/Machine_Learning/arm_compute_library.html>`__

   * Open source inference engine available from Arm.
   * Runs on all Cortex-A ARM cores (AM3x, AM4x, AM6x Sitara devices).
   * Provides highly optimized kernels for NEON (Advanced SIMD)  and CPU acceleration.
   * Used as a backend to accelerate ML frameworks like Arm NN.

   .. rubric:: `NNStreamer <Foundational_Components/Machine_Learning/nnstreamer.html>`__

   * Open source framework based on GStreamer for neural network pipelines.
   * Runs on all Cortex-A ARM cores (AM3x, AM4x, AM6x Sitara devices).
   * Supports many backends such as TensorFlow Lite and Arm NN.
   * Enables easy integration of ML inference into streaming pipelines.

.. ifconfig:: CONFIG_part_family in ('J7_family')

   Jacinto Machine Learning toolkit brings machine learning to the edge by enabling
   machine learning inference on all Jacinto devices. It is provided as part of
   TI's Processor SDK Linux, free to download and use. Jacinto machine learning today consists
   of Neo-AI-DLR library.

+--------------------------+-----------+-------------------------+--------------------+--------------------+
| ML inference Library     | Version   | Delegate /              | Python API         | C/C++ API          |
|                          |           | Execution provider      |                    |                    |
+==========================+===========+=========================+====================+====================+
| TensorFlow Lite          | 2.20.0    | CPU, XNNPACK, ARMNN     | Yes                | Yes                |
+--------------------------+-----------+-------------------------+--------------------+--------------------+
| ONNX Runtime             | 1.23.2    | CPU, ACL                | Yes                | Yes                |
+--------------------------+-----------+-------------------------+--------------------+--------------------+
| Arm NN                   | 26.01     | ACL                     | Yes                | Yes                |
+--------------------------+-----------+-------------------------+--------------------+--------------------+
| Arm Compute Library      | 52.7.0    | NA (Backend Library)    | Yes                | Yes                |
+--------------------------+-----------+-------------------------+--------------------+--------------------+
| NNStreamer               | 2.6.0     | NA (Pipeline Framework) | Yes                | Yes                |
+--------------------------+-----------+-------------------------+--------------------+--------------------+


.. toctree::
   :maxdepth: 2

   Foundational_Components/Machine_Learning/tflite
   Foundational_Components/Machine_Learning/onnxrt
   Foundational_Components/Machine_Learning/armnn
   Foundational_Components/Machine_Learning/arm_compute_library
   Foundational_Components/Machine_Learning/nnstreamer
