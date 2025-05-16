==============================
Release notes version 09.02.00
==============================

.. _pub_edgeai_new_in_this_release:

New in this Release
===================

 - Added `EdgeAI TIOVX Apps <https://github.com/TexasInstruments/edgeai-tiovx-apps>`_
 - Added support for keypoint detection and semantic segmentation in EdgeAI Studio Agent
 - Added support for `v3link fusion mini <https://docs.arducam.com/V3Link-Camera-Solution/V3Link-Camera-Solution-on-TI-Platform/Quick-Start-Guide/>`_
 - Added support for OX05B1S 5MP RGB-IR sensor
 - Supports dynamic parsing of color map from model directory in post processing
 - Supports newer TFLITE runtime versions (TFLITE 2.12.0)

Fixed in this Release
=====================

 - EDGEAI_ROBOTICS-1242 - Encode not working on linux for tda4vm
 - EDGEAI_ROBOTICS-1228 - Semantic segmentation inference on the target does not colour in the class objects
 - EDGEAI_ROBOTICS-1225 - EdgeAI demo for IMX219 10-bit depth not working
 - EDGEAI_ROBOTICS-1224 - EdgeAI documentation: IMX219 10-bit depth
 - EDGEAI_ROBOTICS-1223 - edgeai-gst-plugins: tiovxmultiscaler cropping not working
 - EDGEAI_ROBOTICS-1219 - Enable keypoint detection task on device agent
 - EDGEAI_ROBOTICS-1218 - Enable segmentation task on device agent
 - EDGEAI_ROBOTICS-1217 - Unable to live preview semantic segmentation
 - EDGEAI_ROBOTICS-820  - python_apps video container formats of .mp4 and .mov results in error while writing

.. _pub_edgeai_known_issues:

Known Issues
============

 - EDGEAI_ROBOTICS-867  - v4l2h264dec Decoder: looping does not working for mp4/mov/avi
 - EDGEAI_ROBOTICS-1258	- TIOVX apps: Buffer management needs to be optimized for v4l2 capture
 - EDGEAI_ROBOTICS-1257	- TIOVX Apps: Generated dot file names should not have "-"
 - EDGEAI_ROBOTICS-1239	- TIOVX apps: V4L2 Decode does not exit cleanly in tiovx-apps
 - EDGEAI_ROBOTICS-1241	- Perf stats on AM62A showing high variance for some targets/cores


.. _pub_edgeai_software_components:

Software components
===================

List of software components used in this version

+------------------------------+---------------------+
| Component                    | Version             |
+==============================+=====================+
| Foundation Linux             | 09.02.00.09         |
+------------------------------+---------------------+
| Python                       | 3.10.13             |
+------------------------------+---------------------+
| OpenCV                       | 4.5.5               |
+------------------------------+---------------------+
| GStreamer                    | 1.20.7              |
+------------------------------+---------------------+
| Cmake                        | 3.22.3              |
+------------------------------+---------------------+
| Ninja                        | 1.10.2              |
+------------------------------+---------------------+
| Meson                        | 0.61.3              |
+------------------------------+---------------------+
| NeoAI - DLR                  | 1.13.0              |
+------------------------------+---------------------+
| Tensorflow                   | TIDL_PSDK_9.2       |
+------------------------------+---------------------+
| TFLite-runtime               | TIDL_PSDK_9.2       |
+------------------------------+---------------------+
| ONNX-runtime                 | TIDL_PSDK_9.2       |
+------------------------------+---------------------+
| PyYAML                       | 6.0                 |
+------------------------------+---------------------+
| TI Model Zoo                 | 9.2.0               |
+------------------------------+---------------------+
| edgeai-app-stack             | 09_02_00_00         |
+------------------------------+---------------------+
