#######
Edge AI
#######

.. ifconfig:: CONFIG_part_family not in ('AM62DX_family')

   The SDK provides software and tools to let the users effectively balance deep learning performance with system power and cost on Texas Instrument's processors for edge AI applications. We offer a practical embedded inference solution for next-generation vehicles, smart cameras, edge AI boxes, and autonomous machines and robots. In addition to general purpose micro processors, AM62Ax has integrated micro controllers, DSP, and accelerators for neural network, image, vision, and multimedia processing. With a few simple steps one can run high performance computer vision and deep learning demos using a live camera and display.

   The SDK also enables an interplay of multiple open-source components such as GStreamer, OpenVx, OpenCV and deep learning runtime such as TFLite, ONNX and TVM-RT. The reference applications showcase perception based examples such as image classification, object detection and semantic segmentation in both Python and C++ variants. The SDK supports edit-build-debug cycles directly on the target and also on PC to cross compile and build the applications.

.. ifconfig:: CONFIG_part_family in ('AM62AX_family')

   For more information on edge AI software stack, refer `Edge AI Documentation <https://software-dl.ti.com/processor-sdk-linux/esd/AM62AX/11_01_07_05/exports/docs/edgeai/sdk_overview.html>`_

.. ifconfig:: CONFIG_part_family in ('AM62DX_family')

   The SDK provides software and tools to let users run high-performance audio deep learning inference on Texas Instruments' AM62DX processor. We offer a practical embedded EdgeAI solution for smart speakers, industrial monitoring, voice interfaces, and acoustic event detection applications. The AM62DX integrates a high-performance A53 ARM processor with a dedicated C7x™ DSP optimized for neural network inference and digital signal processing. With a few simple steps one can run real-time EdgeAI pipelines such as speech enhancement and audio classification on the C7x™ DSP.

   The SDK enables an interplay of open-source components such as GStreamer and deep learning runtimes such as TVM-RT. The reference applications showcase EdgeAI examples such as speech enhancement and audio classification in C++ variants. The SDK supports edit-build-debug cycles directly on the target and also on a host PC to cross compile and build the applications.

   For more information on edge AI software stack, refer `Edge AI Documentation <https://prathamti.github.io/processor-sdk-doc/processor-sdk-edgeai-AM62DX/esd/docs/am62d-edgeai/devices/AM62DX/edgeai/index.html>`_

.. ifconfig:: CONFIG_part_variant in ('J721E')

   For more information on edge AI software stack, refer `Edge AI Documentation <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-sk-tda4vm/10_01_00/exports/edgeai-docs/common/sdk_overview.html>`_

.. ifconfig:: CONFIG_part_variant in ('J721S2')

   For more information on edge AI software stack, refer `Edge AI Documentation <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-am68a/10_01_00/exports/edgeai-docs/common/sdk_overview.html>`_

.. ifconfig:: CONFIG_part_variant in ('J784S4')

   For more information on edge AI software stack, refer `Edge AI Documentation <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-am69a/10_01_00/exports/edgeai-docs/common/sdk_overview.html>`_

.. ifconfig:: CONFIG_part_variant in ('J722S')

   For more information on edge AI software stack, refer `Edge AI Documentation <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-am67a/10_01_00/exports/edgeai-docs/common/sdk_overview.html>`_
