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
   * Runs on all Cortex-A ARM cores (AM3x, AM4x, AM5x, AM6x Sitara devices).
   * Imports Tensorflow Lite models.
   * Uses TIDL import tool to create TIDL offloadable Tensorflow Lite models,
     which can be executed via Tensorflow Lite runtime with TIDL acceleration.

   .. rubric:: `ONNX Runtime <Foundational_Components/Machine_Learning/onnxrt.html>`__

   * Open source inference engine available from Arm.
   * Runs on all Cortex-A ARM cores (AM3x, AM4x, AM5x, AM6x Sitara devices).

   .. rubric:: `Arm NN <Foundational_Components/Machine_Learning/armnn.html>`__

   * Open source inference engine available from Arm.
   * Runs on all Cortex-A ARM cores (AM3x, AM4x, AM5x, AM6x Sitara devices).
   * Imports ONNX and TensorFlow Lite models.
   * Provides TensorFlow Lite delegate.

   .. rubric:: `RNN Library <Examples_and_Demos_Application_Demos.html#deploy-and-integration>`__

   * Provides Long Short-Term Memory (LSTM) and fully connected layers in a standalone library to allow for rapid prototyping of inference applications that require Recurrent Neural Networks.
   * Runs on all Cortex-A ARM cores (AM3x, AM4x, AM5x, AM6x Sitara devices).
   * Integrated into TI's Processor SDK Linux in an OOB demo for `Predictive Maintenance <Examples_and_Demos_Application_Demos.html#predictive-maintenance-demo>`__.

   .. rubric:: `TI Deep Learning (TIDL) <https://downloads.ti.com/mctools/esd/docs/tidl-api/index.html>`__

   * Accelerates deep learning inference on C66x DSP cores and/or on Embedded Vision Engine (EVE) subsystems.
   * Available on AM57x device only.
   * Supports CNN at the moment, and imports Caffe, ONNX, and Tensorflow models.

.. ifconfig:: CONFIG_part_family in ('J7_family')

   Jacinto Machine Learning toolkit brings machine learning to the edge by enabling
   machine learning inference on all Jacinto devices. It is provided as part of
   TI's Processor SDK Linux, free to download and use. Jacinto machine learning today consists
   of Neo-AI-DLR library.

+--------------------------+-----------+-----------------------+--------------------+--------------------+
| ML inference Library     | Version   | Delegate /            | Python API         | C/C++ API          |
|                          |           | Execution provider    |                    |                    |
+==========================+===========+=======================+====================+====================+
| TensorFlow Lite          | 2.18.0    | CPU, XNNPACK, ARMNN   | YES                | YES                |
+--------------------------+-----------+-----------------------+--------------------+--------------------+
| ONNX Runtime             | 1.20.1    | CPU, ACL              | YES                | YES                |
+--------------------------+-----------+-----------------------+--------------------+--------------------+
| Arm NN                   | 1.20.1    | ACL                   | YES                | YES                |
+--------------------------+-----------+-----------------------+--------------------+--------------------+



.. toctree::
   :maxdepth: 2

   Foundational_Components/Machine_Learning/tflite
   Foundational_Components/Machine_Learning/onnxrt
   Foundational_Components/Machine_Learning/armnn
   Foundational_Components/Machine_Learning/arm_compute_library
   Foundational_Components/Machine_Learning/nnstreamer
