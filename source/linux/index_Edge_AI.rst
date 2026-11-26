#######
Edge AI
#######

.. ifconfig:: CONFIG_part_family not in ('AM62DX_family')

   The SDK provides software and tools to let the users effectively balance deep learning performance with system power and cost on Texas Instrument's processors for edge AI applications. We offer a practical embedded inference solution for next-generation vehicles, smart cameras, edge AI boxes, and autonomous machines and robots. In addition to general purpose micro processors, AM62Ax has integrated micro controllers, DSP, and accelerators for neural network, image, vision, and multimedia processing. With a few simple steps one can run high performance computer vision and deep learning demos using a live camera and display.

   The SDK also enables an interplay of multiple open-source components such as GStreamer, OpenVx, OpenCV and deep learning runtime such as TFLite, ONNX and TVM-RT. The reference applications showcase perception based examples such as image classification, object detection and semantic segmentation in both Python and C++ variants. The SDK supports edit-build-debug cycles directly on the target and also on PC to cross compile and build the applications.

.. ifconfig:: CONFIG_part_family in ('AM62AX_family')

   For more information on edge AI software stack, refer `Edge AI Documentation <https://software-dl.ti.com/processor-sdk-linux/esd/AM62AX/11_01_07_05/exports/docs/edgeai/sdk_overview.html>`_

.. ifconfig:: CONFIG_part_family in ('AM62DX_family')

   Processor SDK Linux for AM62DX offers tools and reference software for running audio AI directly on the device. Linux applications and GStreamer-based pipelines rely on the TVM runtime to offload model inference to the C7x™ DSP, and supported audio processing stages can likewise be offloaded to the DSP.

   Out-of-box web demos are provided for speech enhancement and audio classification, in addition to a C++ inference application and sample GStreamer pipelines. These reference examples rely on GCRN for speech enhancement and on YAMNet and VGGish for audio classification. The C++ inference application can be built natively on the AM62DX EVM or cross-compiled from a host PC.

   A Bring Your Own Model workflow is also available, describing how to compile, deploy, and integrate compatible audio AI models on AM62DX.

   For more information on edge AI software stack, refer `Edge AI Documentation <https://software-dl.ti.com/processor-sdk-linux/esd/AM62DX/12_02_00_07_04/exports/docs/devices/AM62DX/edgeai/index.html>`_

.. ifconfig:: CONFIG_part_variant in ('J721E')

   For more information on edge AI software stack, refer `Edge AI Documentation <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-sk-tda4vm/10_01_00/exports/edgeai-docs/common/sdk_overview.html>`_

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   For more information on edge AI software stack, refer `Edge AI Documentation <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-am68a/10_01_00/exports/edgeai-docs/common/sdk_overview.html>`_

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   For more information on edge AI software stack, refer `Edge AI Documentation <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-am69a/10_01_00/exports/edgeai-docs/common/sdk_overview.html>`_

.. ifconfig:: CONFIG_part_variant in ('J722S')

   For more information on edge AI software stack, refer `Edge AI Documentation <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-am67a/10_01_00/exports/edgeai-docs/common/sdk_overview.html>`_
