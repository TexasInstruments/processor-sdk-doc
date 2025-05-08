==============
Release notes
==============

.. _pub_edgeai_new_in_this_release:

New in this Release
===================

   -

Fixed in this Release
=====================
   - EDGEAI_ROBOTICS-1296 - DMABuf import not working with CnM Encoder for resolutions not aligned to 64 bytes
   - EDGEAI_ROBOTICS-1295 - High CPU usage while running EdgeAI Demos
   - EDGEAI_ROBOTICS-867  - v4l2h264dec Decoder not working for mp4 file
   - EDGEAI_ROBOTICS-1258 - TIOVX apps: Buffer management needs to be optimized for v4l2 capture
   - EDGEAI_ROBOTICS-1239	- TIOVX apps: V4L2 Decode does not exit cleanly in tiovx-apps
   - EDGEAI_ROBOTICS-1200	- Device Agent: No error message for unsupported camera
   - EDGEAI_ROBOTICS-1263 - AM62A TIDL: C7x goes into exception with MAIR7 MMU setting for L2 SRAM


.. _pub_edgeai_known_issues:

Known Issues
============

   - EDGEAI_ROBOTICS-1284	- TIOVX Apps: Jitter with using OpenVX buffers directly in OpenMAX wrapper
   - EDGEAI_ROBOTICS-1266 - edgeai-tiovx-apps pipeline latency is the sum of individual components
   - EDGEAI_ROBOTICS-1285 - edgeai-tiovx-apps: OMX_wrapper: QNX decode not working if buffers enqueued in default order


.. _pub_edgeai_software_components:

Software components
===================

List of software components used in this version

+------------------------------+---------------------+
| Component                    | Version             |
+==============================+=====================+
| Foundation Linux             | 10.01.00.08         |
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
| Tensorflow                   | TIDL_PSDK_10.1      |
+------------------------------+---------------------+
| TFLite-runtime               | TIDL_PSDK_10.1      |
+------------------------------+---------------------+
| ONNX-runtime                 | TIDL_PSDK_10.1      |
+------------------------------+---------------------+
| PyYAML                       | 6.0.1               |
+------------------------------+---------------------+
| TI Model Zoo                 | 10.1.0              |
+------------------------------+---------------------+
| edgeai-app-stack             | 10_01_00_00         |
+------------------------------+---------------------+
