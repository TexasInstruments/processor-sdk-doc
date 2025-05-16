==============================
Release notes version 09.00.00
==============================

.. _pub_edgeai_new_in_this_release_09_00_00:

New in this Release
===================

 - Reference applications and custom GStreamer plugins migrated to GStreamer 1.20.6
 - Improved codec performance with zero-buffer-copy exchange between elements
 - OpTIFlow is redesigned as a python application which automatically launches an end-to-end pipeline from YAML config files
 - OpTIFLOW performs automatic load distribution of GST elements across the available accelerators
 - Supports Node JS based remote streaming from target
 - Updated color-convert plugin supports Gray8 to NV12 format
 - Supports Docker based Ubuntu 22.04 on top of Yocto-Kirkstone
 - First release of Robotics SDK 09.00.00 (please refer to `Robotics SDK change log <https://software-dl.ti.com/jacinto7/esd/robotics-sdk/09_00_00/AM62A/docs/source/CHANGELOG.html>`_)

Fixed in this Release
=====================

 - EDGEAI_ROBOTICS-642 - Mosaic element hangs when both instances of MSC are used in multi-input multi-inference usecase
 - EDGEAI_ROBOTICS-648 - tiovxdlcolorconvert fails when the image height/2 is not an even number
 - EDGEAI_ROBOTICS-819 - tiovxisp element infrequently throws error while exiting edgeai-gst-apps
 - EDGEAI_ROBOTICS-1093 - Add support for multiple A72/A53 targets for ARM NEON kernels
 - EDGEAI_ROBOTICS-1137 - Update SDK documentation for HS-FS build

.. _pub_edgeai_known_issues_09_00_00:

Known Issues
============

 - EDGEAI_ROBOTICS-820 - EdgeAI Python Apps does not save output file in .mov or .mp4 format

.. _pub_edgeai_software_components_09_00_00:

Software components
===================

List of software components used in this version

+------------------------------+---------------------+
| Component                    | Version             |
+==============================+=====================+
| Foundation Linux             | 09.00.00.08         |
+------------------------------+---------------------+
| Python                       | 3.10.9              |
+------------------------------+---------------------+
| OpenCV                       | 4.5.5               |
+------------------------------+---------------------+
| GStreamer                    | 1.20.6              |
+------------------------------+---------------------+
| Cmake                        | 3.22.3              |
+------------------------------+---------------------+
| Ninja                        | 1.10.2              |
+------------------------------+---------------------+
| Meson                        | 0.61.2              |
+------------------------------+---------------------+
| NeoAI - DLR                  | 1.13.0              |
+------------------------------+---------------------+
| Tensorflow                   | TIDL_PSDK_9.0       |
+------------------------------+---------------------+
| TFLite-runtime               | TIDL_PSDK_9.0       |
+------------------------------+---------------------+
| ONNX-runtime                 | TIDL_PSDK_9.0       |
+------------------------------+---------------------+
| PyYAML                       | 6.0                 |
+------------------------------+---------------------+
| TI Model Zoo                 | 9.0.0               |
+------------------------------+---------------------+
| edgeai-app-stack             | 09_00_00_00         |
+------------------------------+---------------------+
| edgeai-tidl-tools            | 09_00_00_00         |
+------------------------------+---------------------+
