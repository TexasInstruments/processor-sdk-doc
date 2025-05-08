===========
Test Report
===========

Here is the summary of the sanity tests we ran with both Python and C++ demos.
Test cases vary with different inputs, outputs, runtime, models, python/c++ apps.

1. Inputs:

    * USB Camera (Logitech C270, 1280x720, JPEG)
    * IMX219 Camera (Rpi v2 Sony IMX219, 1920x1080, RAW)
    * Image files (images under /opt/edgeai-test-data/images)
    * Video file (video0_1280_768.h264 file under /opt/edgeai-test-data/videos)

2. Outputs:

    * Display (HDMI)
    * File write to SD card

3. Inference Type:

    * Image classification
    * Object detection
    * Semantic segmentation

4. Runtime/models:

    * DLR
    * TFLite
    * ONNX

5. Applications:

    * Python
    * C++
    * Optiflow

6. Platform:

    * Host OS
    * Docker


Apps test report
=====================

Single Input Single Output
--------------------------

.. csv-table::
      :header: "Category", "# test case", "Pass", "Fail"

      Host OS - Python,126,126,0
      Host OS - C++,126,126,0
		Host OS - Optiflow,126,126,0
		Docker - Python,126,126,0
      Docker - C++,126,126,0
		Docker - Optiflow,126,126,0

.. csv-table::
      :header: "S.No", "Models", "Input", "Output", "Host OS - Optiflow", "Host OS - Python App", "Host OS - C++ App", "Docker - Optiflow", "Docker - Python App", "Docker - C++ App", "Comments"

      1,TVM-CL-3090-mobileNetV2-tv,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      2,TVM-CL-3090-mobileNetV2-tv,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      3,TVM-CL-3090-mobileNetV2-tv,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      4,TVM-CL-3090-mobileNetV2-tv,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      5,TVM-CL-3090-mobileNetV2-tv,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      6,TVM-CL-3090-mobileNetV2-tv,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      7,TVM-CL-3090-mobileNetV2-tv,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      8,TVM-CL-3090-mobileNetV2-tv,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      9,TVM-CL-3090-mobileNetV2-tv,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      10,TFL-CL-0000-mobileNetV1-mlperf,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      11,TFL-CL-0000-mobileNetV1-mlperf,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      12,TFL-CL-0000-mobileNetV1-mlperf,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      13,TFL-CL-0000-mobileNetV1-mlperf,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      14,TFL-CL-0000-mobileNetV1-mlperf,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      15,TFL-CL-0000-mobileNetV1-mlperf,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      16,TFL-CL-0000-mobileNetV1-mlperf,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      17,TFL-CL-0000-mobileNetV1-mlperf,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      18,TFL-CL-0000-mobileNetV1-mlperf,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      19,ONR-CL-6360-regNetx-200mf,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      20,ONR-CL-6360-regNetx-200mf,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      21,ONR-CL-6360-regNetx-200mf,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      22,ONR-CL-6360-regNetx-200mf,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      23,ONR-CL-6360-regNetx-200mf,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      24,ONR-CL-6360-regNetx-200mf,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      25,ONR-CL-6360-regNetx-200mf,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      26,ONR-CL-6360-regNetx-200mf,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      27,ONR-CL-6360-regNetx-200mf,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      28,TVM-OD-5120-ssdLite-mobDet-DSP-coco-320x320,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      29,TVM-OD-5120-ssdLite-mobDet-DSP-coco-320x320,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      30,TVM-OD-5120-ssdLite-mobDet-DSP-coco-320x320,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      31,TVM-OD-5120-ssdLite-mobDet-DSP-coco-320x320,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      32,TVM-OD-5120-ssdLite-mobDet-DSP-coco-320x320,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      33,TVM-OD-5120-ssdLite-mobDet-DSP-coco-320x320,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      34,TVM-OD-5120-ssdLite-mobDet-DSP-coco-320x320,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      35,TVM-OD-5120-ssdLite-mobDet-DSP-coco-320x320,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      36,TVM-OD-5120-ssdLite-mobDet-DSP-coco-320x320,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      37,TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      38,TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      39,TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      40,TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      41,TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      42,TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      43,TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      44,TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      45,TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      46,ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      47,ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      48,ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      49,ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      50,ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      51,ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      52,ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      53,ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      54,ONR-OD-8020-ssd-lite-mobv2-mmdet-coco-512x512,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      55,ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      56,ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      57,ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      58,ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      59,ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      60,ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      61,ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      62,ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      63,ONR-OD-8220-yolox-s-lite-mmdet-coco-640x640,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      64,ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      65,ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      66,ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      67,ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      68,ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      69,ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      70,ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      71,ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      72,ONR-OD-8420-yolox-s-lite-mmdet-widerface-640x640,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      73,ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      74,ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      75,ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      76,ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      77,ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      78,ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      79,ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      80,ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      81,ONR-OD-8200-yolox-nano-lite-mmdet-coco-416x416,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      82,ONR-OD-8270-yolox-pico-lite-mmdet-coco-320x320,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      83,ONR-OD-8270-yolox-pico-lite-mmdet-coco-320x320,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      84,ONR-OD-8270-yolox-pico-lite-mmdet-coco-320x320,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      85,ONR-OD-8270-yolox-pico-lite-mmdet-coco-320x320,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      86,ONR-OD-8270-yolox-pico-lite-mmdet-coco-320x320,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      87,ONR-OD-8270-yolox-pico-lite-mmdet-coco-320x320,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      88,ONR-OD-8270-yolox-pico-lite-mmdet-coco-320x320,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      89,ONR-OD-8270-yolox-pico-lite-mmdet-coco-320x320,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      90,ONR-OD-8270-yolox-pico-lite-mmdet-coco-320x320,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      91,TVM-SS-5710-deeplabv3lite-mobv2-cocoseg21-512x512,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      92,TVM-SS-5710-deeplabv3lite-mobv2-cocoseg21-512x512,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      93,TVM-SS-5710-deeplabv3lite-mobv2-cocoseg21-512x512,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      94,TVM-SS-5710-deeplabv3lite-mobv2-cocoseg21-512x512,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      95,TVM-SS-5710-deeplabv3lite-mobv2-cocoseg21-512x512,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      96,TVM-SS-5710-deeplabv3lite-mobv2-cocoseg21-512x512,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      97,TVM-SS-5710-deeplabv3lite-mobv2-cocoseg21-512x512,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      98,TVM-SS-5710-deeplabv3lite-mobv2-cocoseg21-512x512,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      99,TVM-SS-5710-deeplabv3lite-mobv2-cocoseg21-512x512,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      100,TFL-SS-2580-deeplabv3_mobv2-ade20k32-mlperf-512x512,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      101,TFL-SS-2580-deeplabv3_mobv2-ade20k32-mlperf-512x512,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      102,TFL-SS-2580-deeplabv3_mobv2-ade20k32-mlperf-512x512,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      103,TFL-SS-2580-deeplabv3_mobv2-ade20k32-mlperf-512x512,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      104,TFL-SS-2580-deeplabv3_mobv2-ade20k32-mlperf-512x512,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      105,TFL-SS-2580-deeplabv3_mobv2-ade20k32-mlperf-512x512,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      106,TFL-SS-2580-deeplabv3_mobv2-ade20k32-mlperf-512x512,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      107,TFL-SS-2580-deeplabv3_mobv2-ade20k32-mlperf-512x512,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      108,TFL-SS-2580-deeplabv3_mobv2-ade20k32-mlperf-512x512,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      109,ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      110,ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      111,ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      112,ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      113,ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      114,ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      115,ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      116,ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      117,ONR-SS-8610-deeplabv3lite-mobv2-ade20k32-512x512,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      118,ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432,Image,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      119,ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432,Image,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      120,ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432,Image,Image-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      121,ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432,Video,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      122,ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432,Video,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      123,ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432,USB Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      124,ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432,USB Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-
      125,ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432,IMX219 Camera,Display,Pass,Pass,Pass,Pass,Pass,Pass,-
      126,ONR-SS-7618-deeplabv3lite-mobv2-qat-robokit-768x432,IMX219 Camera,Video-Filewrite,Pass,Pass,Pass,Pass,Pass,Pass,-

.. note::

   Please refer to the :ref:`pub_edgeai_known_issues` section for more details
