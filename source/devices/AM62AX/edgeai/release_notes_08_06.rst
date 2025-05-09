==============================
Release notes version 08.06.00
==============================

.. _pub_edgeai_new_in_this_release_08_06_00:

New in this Release
===================

 - First release of Edge AI app stack on AM62Ax device
 - Supports popular deep learning runtime frameworks such as TFLite-RT, ONNX-RT, Neo-AI-DLR runtime
 - Validated over 50+ pre-imported models via TI Edge AI model zoo
 - Out-of-box GUI based demo for quick evaluation of different deep learning tasks
 - Reference Python and C++ GStreamer and Open CV based applications for quick prototyping
 - Optimized GStreamer based end-to-end pipelines using OpTIFlow.
 - Easy to use, custom GStreamer plugins to seamlessly access underlying hardware accelerators
 - Supports a wide range of inputs such as compressed video files (H.264/H.265), RTSP sources, USB camera, Rpi v2 camera Out-of-box

Fixed in this Release
=====================

 - None, first release on AM62Ax device

.. _pub_edgeai_known_issues_08_06_00:

Known Issues
============

 - EDGEAI_ROBOTICS-819 - tiovxisp element infrequently throws error while exiting edgeai-gst-apps
 - EDGEAI_ROBOTICS-648 - tiovxdlcolorconvert fails when the image height/2 is not an even number
 - EDGEAI_ROBOTICS-642 - Mosaic element hangs when both instances of MSC are used in multi-input multi-inference usecase
 - EDGEAI_ROBOTICS-640 - LDC introduces image format while working with 1936 x 1096 resolution

.. _pub_edgeai_software_components_08_06_00:

Software components
===================

List of software components used in this version

+------------------------------+---------------------+
| Component                    | Version             |
+==============================+=====================+
| Foundation Linux             | 08.06.00.45         |
+------------------------------+---------------------+
| Python                       | 3.8                 |
+------------------------------+---------------------+
| OpenCV                       | 4.1.0               |
+------------------------------+---------------------+
| GStreamer                    | 1.16.3              |
+------------------------------+---------------------+
| Cmake                        | 3.16.5              |
+------------------------------+---------------------+
| Ninja                        | 1.10.0              |
+------------------------------+---------------------+
| Meson                        | 0.53.2              |
+------------------------------+---------------------+
| Jupyterlab                   | 3.0.14              |
+------------------------------+---------------------+
| NeoAI - DLR                  | 1.10.0              |
+------------------------------+---------------------+
| Tensorflow                   | TIDL_PSDK_8.6       |
+------------------------------+---------------------+
| TFLite-runtime               | TIDL_PSDK_8.6       |
+------------------------------+---------------------+
| ONNX-runtime                 | TIDL_PSDK_8.6       |
+------------------------------+---------------------+
| PyYAML                       | 5.3.1               |
+------------------------------+---------------------+
| TI Model Zoo                 | 8.6.0               |
+------------------------------+---------------------+
| edgeai-app-stack             | 8.6.0.3             |
+------------------------------+---------------------+
| edgeai-tidl-tools            | 08_06_00_02         |
+------------------------------+---------------------+
