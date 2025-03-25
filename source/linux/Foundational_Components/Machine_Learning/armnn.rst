Arm NN
======

Introduction
-------------
Arm NN is an open source machine learning inference engine which bridges the gap between existing
neural network frameworks and power-efficient Arm Cortex-A CPUs.

Arm NN is built on top of Arm Compute Library, leveraging its NEON optimized kernels.

Arm NN provides a TensorFlow Lite Delegate and using this delegate from TensorFlow Lite is the
recommended way to use Arm NN.

More information can be found at: https://www.mlplatform.org/

For Sitara devices without dedicated AI accelerators like C7x/MMA, one can use the provided Arm NN
TensorFlow Lite Delegate for supporting inference tasks on Arm CPUs.

On devices with dedicated AI accelerators, the TensorFlow Lite Delegate can be used
in conjunction with the TIDL TensorFlow Lite Delegate.


Supported versions
------------------

  - Arm NN 24.11
