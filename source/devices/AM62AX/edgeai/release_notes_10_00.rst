==============================
Release notes version 10.00.00
==============================

.. _pub_edgeai_new_in_this_release:

New in this Release
===================

 - Linux Kernel migrated to 6.6 from 6.1
 - Added OpenMax Support in EdgeAI TIOVX Apps, to interface H264/H265 HW encoder/decoder on QNX
 - GPIO kernel interface migrated to libgpiod v2.1
 - Supports Docker based Ubuntu 24.04 on top of Yocto-Scarthgap
 - Device Tree Overlay changes made (please refer to notes section for each camera in `Getting Started <https://software-dl.ti.com/jacinto7/esd/processor-sdk-linux-am62a/10_00_00/exports/edgeai-docs/devices/AM62A/linux/getting_started.html#hardware-setup>`)

Fixed in this Release
=====================

 - EDGEAI_ROBOTICS-1263 - Manual exposure and white balance not working through GStreamer
 - EDGEAI_ROBOTICS-1257 - TIOVX Apps: Generated dot file names should not have "-"
 - EDGEAI_ROBOTICS-1205 - EdgeAI documentation: Doc : Remove documentation on Setting up RTSP server

.. _pub_edgeai_known_issues:

Known Issues
============

 - EDGEAI_ROBOTICS-1241	- TIOVX apps: Perf stats showing high variance for some targets/cores
 - EDGEAI_ROBOTICS-1284	- TIOVX Apps: Jitter with using OpenVX buffers directly in OpenMAX wrapper
 - EDGEAI_ROBOTICS-1239	- TIOVX apps: V4L2 Decode does not exit cleanly in tiovx-apps
 - EDGEAI_ROBOTICS-1258	- TIOVX apps: Buffer management needs to be optimized for v4l2 capture
 - EDGEAI_ROBOTICS-1200	- Device Agent: No error message for unsupported camera
 - EDGEAI_ROBOTICS-867  - v4l2h264dec Decoder not working for mp4 file
 - EDGEAI_ROBOTICS-1230	- GST pipeline with kmssink and multiplefilesink freezing
 - EDGEAI_ROBOTICS-1295 - High CPU usage while running EdgeAI Demos
 - EDGEAI_ROBOTICS-1296 - DMABuf import not working with CnM Encoder for resolutions not aligned to 64 bytes 
 - EDGEAI_ROBOTICS-1298 - Green screens observed with Ox50B streaming

.. _pub_edgeai_software_components:

Software components
===================

List of software components used in this version

+------------------------------+---------------------+
| Component                    | Version             |
+==============================+=====================+
| Foundation Linux             | 10.00.00.08         |
+------------------------------+---------------------+
| Python                       | 3.12.4              |
+------------------------------+---------------------+
| OpenCV                       | 4.9.0               |
+------------------------------+---------------------+
| GStreamer                    | 1.22.12             |
+------------------------------+---------------------+
| Cmake                        | 3.28.3              |
+------------------------------+---------------------+
| Ninja                        | 1.11.1              |
+------------------------------+---------------------+
| Meson                        | 1.3.1               |
+------------------------------+---------------------+
| NeoAI - DLR                  | 1.13.0              |
+------------------------------+---------------------+
| Tensorflow                   | TIDL_PSDK_10.0      |
+------------------------------+---------------------+
| TFLite-runtime               | TIDL_PSDK_10.0      |
+------------------------------+---------------------+
| ONNX-runtime                 | TIDL_PSDK_10.0      |
+------------------------------+---------------------+
| PyYAML                       | 6.0.1               |
+------------------------------+---------------------+
| TI Model Zoo                 | 10.0.0              |
+------------------------------+---------------------+
| edgeai-app-stack             | 10_00_00_00         |
+------------------------------+---------------------+
