.. _pub_edgeai_configuration:

========================
Configuring applications
========================

The demo config file uses YAML format to define input sources, models, outputs
and finally the flows which defines how everything is connected. Config files
for out-of-box demos are kept in ``edgeai-gst-apps/configs`` folder. The
folder contains config files for all the use cases and also multi-input and
multi-inference case. The folder also has a template YAML file
``app_config_template.yaml`` which has detailed explanation of all the
parameters supported in the config file.

Config file is divided in 4 sections:

#. Inputs
#. Models
#. Outputs
#. Flows

Inputs
======

The input section defines a list of supported inputs like camera, video files etc.
Their properties like shown below.

.. code-block:: yaml

   inputs:
      input0:                                                         #Camera Input
         source: /dev/video-usb-cam0                                 #Device file entry of the camera
         format: jpeg                                                #Input data format supported by camera
         width: 1280                                                 #Width and Height of the input
         height: 720
         framerate: 30                                               #Framerate of the source

      input1:                                                         #Video Input
         source: /opt/edgeai-test-data/videos/video0_1280_768.h264   #Video file
         format: h264                                                #File encoding format
         width: 1280
         height: 768
         framerate: 30

      input2:                                                         #Image Input
         source: /opt/edgeai-test-data/videos/images/%04d.jpg        #Sequence of Image files, printf style formatting is used
         width: 1280
         height: 720
         index: 0                                                    #Starting Index (optional)
         framerate: 1

All supported inputs are listed in template config file.
Below are the details of most commonly used inputs.

.. _pub_edgeai_camera_sources:

Camera sources (v4l2)
---------------------

**v4l2src** GStreamer element is used to capture frames from camera sources
which are exposed as v4l2 devices. In Linux, there are many devices which are
implemented as v4l2 devices. Not all of them will be camera devices. You need
to make sure the correct device is configured for running the demo successfully.

``init_script.sh`` is ran as part of systemd, which detects all cameras connected
and prints the detail like below in the console:

.. code-block:: bash

   /opt/edgeai-gst-apps# ./init_script.sh
   USB Camera detected
      device = /dev/video-usb-cam0
      format = jpeg
   CSI Camera 0 detected
      device = /dev/video-imx219-cam0
      format = [fmt:SRGGB8_1X8/1920x1080]
      subdev_id = /dev/v4l-imx219-subdev0
      isp_required = yes

script can also be run manually later to get the camera details.

From the above log we can determine that 1 USB camera is connected
(/dev/video-usb-cam0), and 1 CSI camera is connected (/dev/video-imx219-cam0) which is IMX219 raw
sensor and needs ISP.

Using this method, you can configure correct device for camera capture in the
input section of config file.

.. code-block:: bash

   input0:
      source: /dev/video-usb-cam0     #USB Camera
      format: jpeg                    #if connected USB camera supports jpeg
      width: 1280
      height: 720
      framerate: 30

   input1:
      source: /dev/video-imx219-cam0     #IMX219 raw sensor that needs ISP
      format: rggb                    #ISP will be added in the pipeline
      width: 1920
      height: 1080
      framerate: 30
      subdev-id: /dev/v4l-imx219-subdev0 #needed by ISP to control sensor params via ioctls

Make sure to configure correct ``format`` for camera input. ``jpeg`` for USB
camera that supports MJPEG (Ex. C270 logitech USB camera). ``auto`` for CSI
camera to allow GStreamer to negotiate the format. ``rggb`` for sensor
that needs ISP.

Video sources
-------------

H.264 and H.265 encoded videos can be provided as input sources to the demos.
Sample video files are provided under ``/opt/edgeai-test-data/videos/``

.. code-block:: yaml

   input1:
      source: /opt/edgeai-test-data/videos/video0_1280_768.h264
      format: h264
      width: 1280
      height: 768
      framerate: 30

   input2:
      source: /opt/edgeai-test-data/videos/video0_1920_1088.h264
      format: h264
      width: 1920
      height: 1088
      framerate: 30

Make sure to configure correct ``format`` for video input as shown above.
By default the format is set to ``auto`` which will then use the GStreamer
bin ``decodebin`` instead.

Image sources
-------------

JPEG compressed images can be provided as inputs to the demos. A sample set of
images are provided under ``/opt/edgeai-test-data/images``. The names of the
files are numbered sequentially and incrementally and the demo plays the files
at the fps specified by the user.

.. code-block:: yaml

   input2:
      source: /opt/edgeai-test-data/images/%04d.jpg
      width: 1280
      height: 720
      index: 0
      framerate: 1

RTSP sources
------------

H.264 encoded video streams either coming from a RTSP compliant IP camera or
via RTSP server running on a remote PC can be provided as inputs to the demo.

.. code-block:: yaml

   input0:
      source: rtsp://172.24.145.220:8554/test # rtsp stream url, replace this with correct url
      width: 1280
      height: 720
      framerate: 30

Models
======

The model section defines a list of models that are used in the demo. Path to
the model directory is a required argument for each model and rest are optional
properties specific to given use cases like shown below.

.. code-block:: yaml

   models:
      model0:
         model_path: /opt/model_zoo/TFL-OD-2020-ssdLite-mobDet-DSP-coco-320x320      #Model Directory
         viz_threshold: 0.6                                                          #Visualization threshold for adding bounding boxes (optional)
      model1:
         model_path: /opt/model_zoo/ONR-CL-6360-regNetx-200mf
         topN: 5                                                                     #Number of top N classes (optional)
      model2:
         model_path: /opt/model_zoo/ONR-SS-8690-fpnlite-aspp-regnetx400mf-ade20k32-384x384
         alpha: 0.4                                                                  #alpha for blending segmentation mask (optional)


Below are some of the use case specific properties:

#. **viz_threshold**: Score threshold to draw the bounding boxes for detected
   objects in object detection. This can be used to control the number of boxes
   in the output, increase if there are too many and decrease if there are very
   few
#. **topN**: Number of most probable classes to overlay on image classification
   output
#. **alpha**: This determines the weight of the mask for blending the semantic
   segmentation output with the input image ``alpha * mask + (1 - alpha) * image``

The content of the model directory and its structure is discussed in detail in
:ref:`pub_edgeai_import_custom_models`


Outputs
=======

The output section defines a list of supported outputs.

.. code-block:: yaml

   outputs:
      output0:                                                         #Display Output
         sink: kmssink
         width: 1920                                                  #Width and Height of the output
         height: 1080
         overlay-perf-type: graph                                     #Overlay performance stat (graph or text default:No overlay)
         connector: 39                                                #Connector ID for kmssink (optional)

      output1:                                                         #Video Output
         sink: /opt/edgeai-test-data/outputs/output_video.mkv         #Output video file
         width: 1920
         height: 1080

      output2:                                                         #Image Output
         sink: /opt/edgeai-test-data/outputs/output_image_%04d.jpg    #Image file name, printf style formatting is used
         width: 1920
         height: 1080

      output3:
         sink: remote                                                 #Publish output to udp port as jpeg encoded frames
         width: 1920
         height: 1080
         port: 8081                                                   #udp port (default:8081)
         host: 127.0.0.1                                              #udp host (default:0.0.0.0)
         encoding: jpeg                                               #encoding type (jpeg or mp4)


All supported outputs are listed in template config file.
Below are the details of most commonly used outputs

Display sink (kmssink)
----------------------

When you have only one display connected to the SK, kmssink will try to use
it for displaying the output buffers. In case you have connected multiple
display monitors (e.g. Display Port and HDMI), you can select a specific display
for kmssink by passing a specific connector ID number.
Following command finds out the connected displays available to use.

.. note::

   Run this command to check which display is connected. The first number in each
   line is the connector-id to be used in the next step.

.. code-block:: bash

   /opt/edgeai-gst-apps# modetest -M tidss -c | grep connected
   39      38      connected       DP-1            530x300         12      38
   48      0       disconnected    HDMI-A-1        0x0             0       47

Configure the required connector ID in the output section of the config file.

Video sinks
-----------
The post-processed outputs can be encoded in H.264 format and stored on disk.
Please specify the location of the video file in the configuration file.

.. code-block:: yaml

   output1:
      sink: /opt/edgeai-test-data/outputs/output_video.mkv    #(.mkv or .mp4 or .mov)
      width: 1920
      height: 1080

Image sinks
-----------
The post-processed outputs can be stored as JPEG compressed images.
Please specify the location of the image files in the configuration file.
The images will be named sequentially and incrementally as shown.

.. code-block:: yaml

   output2:
      sink: /opt/edgeai-test-data/outputs/output_image_%04d.jpg
      width: 1920
      height: 1080

Remote sinks
------------
Post-processed frames can be encoded as jpeg or h264 frames and send as udp packets
to a port. Please specify the sink as remote in the configuration file. The udp port and
host to send packets to can be defined. If not, default port is 8081 and host
is 127.0.0.1.

.. code-block:: yaml

   output3:
      sink: remote
      width: 1920
      height: 1080
      port: 8081
      host: 127.0.0.1
      encoding: jpeg  #(jpeg or h264)

A NodeJS server is provided under  ``/opt/edgeai-gst-apps/scripts/remote_streaming``
which establishes a node server on the target and listens to the udp port (8081)
on localhost (127.0.0.1) and can be used to view the frames remotely.

.. code-block:: bash

   /opt/edgeai-gst-apps# node scripts/remote_streaming/server.js


Flows
=====

The flows section defines how inputs, models and outputs are connected.
Multiple flows can be defined to achieve multi input, multi inference as shown

.. note::

   The format of specifying flows is changed as of 08.05.00 release to enable multiple outputs in the same sub-flow
   The older config files may not be compatible from this release onwards and should be changed to below format

.. code-block:: yaml

   flows:
      # flowname : [input,mode1,output,[mosaic_pos_x,mosaic_pos_y,width,height]]
      flow0: [input0,model0,output0,[160,90,800,450]]
      flow1: [input0,model1,output0,[960,90,800,450]]
      flow2: [input1,model2,output0,[160,540,800,450]]
      flow3: [input1,model3,output0,[960,540,800,450]]

Each flow defined here has exactly **1 input** and **1 model**. If multiple
flows have same input, they are clubbed together internally in the application
for optimization. Along with input, models and outputs it is required to define
**n mosaics** which are the position of the inference output in the final output
plane. This is needed because multiple inference outputs can be rendered to same
output (Ex: Display).


GStreamer plugins
=================

The edgeai-gst-apps essentially constructs GStreamer pipelines for dataflow.
This pipeline is constructed optimally and dynamically based on a pool of
specific plugins available on the platform. The defined pool of plugins for
different platform can be found in ``edgeai-gst-apps/configs/gst_plugin_maps.yaml``
file.

This file contains the plugin used for certain task and the property of plugin
(if applicable).

Default GStreamer plugins map for |__PART_FAMILY_NAME__|
--------------------------------------------------------

.. code-block:: yaml

   <soc-type>:
      dlcolorconvert:
         element: tiovxdlcolorconvert
         property:
            out-pool-size: 4
      colorconvert:
         element: tiovxcolorconvert
         property:
            target: [0,1]
            out-pool-size: 4
      scaler:
         element: tiovxmultiscaler
         property:
            target: [0,1]       #[MSC targets to balance loads across]
      dlpreproc:
         element: tiovxdlpreproc
         property:
            out-pool-size: 4
      mosaic:
         element: tiovxmosaic
      isp:
         element: tiovxisp
      ldc:
         element: tiovxldc
      h264dec:
         element: v4l2h264dec
         property:
            capture-io-mode: 5  #[setting the mode for decoder]
      h265dec:
         element: v4l2h265dec
      h264enc:
         element: v4l2h264enc
      h265enc: null
      jpegenc:
         element: jpegenc
      inferer:
         target: dsp             #[dsp for c7x offload, arm for no offload]
         core-id: [1]            #[specify list of c7x cores to offload models]

